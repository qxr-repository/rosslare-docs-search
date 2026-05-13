#!/usr/bin/env python3
import json
import re
from pathlib import Path
from datetime import datetime

try:
    from docx import Document as DocxDocument
    HAS_DOCX = True
except:
    HAS_DOCX = False

try:
    from openpyxl import load_workbook
    HAS_OPENPYXL = True
except:
    HAS_OPENPYXL = False

class SmartContentIndexer:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.index = []
        
    def extract_docx(self, file_path):
        """Extract from DOCX files"""
        if not HAS_DOCX:
            return None
        try:
            doc = DocxDocument(file_path)
            text = [p.text for p in doc.paragraphs if p.text.strip()]
            return ' '.join(text) if text else None
        except:
            return None
    
    def extract_excel(self, file_path):
        """Extract from XLS/XLSX files"""
        if not HAS_OPENPYXL:
            return None
        try:
            workbook = load_workbook(file_path)
            text = []
            for sheet in workbook.sheetnames:
                ws = workbook[sheet]
                for row in ws.iter_rows(values_only=True):
                    for cell in row:
                        if cell is not None:
                            text.append(str(cell))
            return ' '.join(text) if text else None
        except:
            return None
    
    def extract_text_file(self, file_path):
        """Extract from TXT/MD/HTML"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except:
            return None
    
    def extract_content(self, file_path):
        """Extract content from supported types"""
        suffix = file_path.suffix.lower()
        
        if suffix == '.docx':
            return self.extract_docx(file_path)
        elif suffix in ['.xls', '.xlsx']:
            return self.extract_excel(file_path)
        elif suffix in ['.txt', '.md', '.html']:
            return self.extract_text_file(file_path)
        
        return None
    
    def get_keywords(self, text):
        """Fast keyword extraction"""
        if not text:
            return []
        
        words = re.findall(r'\b\w{3,}\b', text.lower())
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        
        top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:40]
        return [w for w, _ in top]
    
    def index_file(self, file_path):
        """Index a file"""
        try:
            rel_path = file_path.relative_to(self.root_path)
            file_size = file_path.stat().st_size
            
            # Extract content
            content = self.extract_content(file_path)
            
            if content:
                # Limit content size
                content = ' '.join(content.split())[:40000]
                
                # Get keywords from filename too
                filename_words = re.findall(r'\b\w+\b', file_path.stem)
                keywords = self.get_keywords(content + ' ' + ' '.join(filename_words))
                
                snippet = content[:300] + ("..." if len(content) > 300 else "")
                
                entry = {
                    'path': str(rel_path).replace('\\', '/'),
                    'filename': file_path.name,
                    'file_type': file_path.suffix.lower(),
                    'size_kb': round(file_size / 1024, 1),
                    'snippet': snippet,
                    'keywords': keywords,
                    'content': content
                }
                
                self.index.append(entry)
                return True
        except:
            pass
        
        return False
    
    def build_index(self):
        """Build index for text-based files"""
        print("Building content index (text-based files)...\n")
        
        # Prioritize text-based files (including Excel)
        all_files = list(self.root_path.rglob('*'))
        text_files = [f for f in all_files if f.is_file() and f.suffix in 
                     ['.docx', '.txt', '.md', '.html', '.xls', '.xlsx']]
        
        print(f"Found {len(text_files)} text-based files\n")
        
        for i, f in enumerate(sorted(text_files)):
            if i % 20 == 0:
                print(f"  {i}/{len(text_files)}...")
            self.index_file(f)
        
        print(f"\n✓ Indexed {len(self.index)} files")
        return self.index
    
    def save_index(self, output_dir):
        """Save index"""
        output_file = Path(output_dir) / 'content_index.json'
        
        total_size = sum(len(f.get('content', '')) for f in self.index)
        
        index_data = {
            'created': datetime.now().isoformat(),
            'total_files': len(self.index),
            'total_content_mb': round(total_size / 1024 / 1024, 2),
            'files': self.index
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        
        file_size_mb = output_file.stat().st_size / 1024 / 1024
        print(f"✓ Index saved: {output_file}")
        print(f"  Size: {file_size_mb:.1f} MB")
        return output_file

if __name__ == '__main__':
    indexer = SmartContentIndexer('/sessions/gifted-sharp-feynman/mnt/Rosslare Documentation/')
    indexer.build_index()
    indexer.save_index('/sessions/gifted-sharp-feynman/mnt/outputs')
