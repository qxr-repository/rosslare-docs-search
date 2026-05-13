#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path
from datetime import datetime

class QuickIndexer:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.index = []
        
    def tokenize(self, text):
        """Extract key terms"""
        tokens = re.findall(r'\b\w{3,}\b', text.lower())
        return sorted(list(set(tokens)))[:30]
    
    def extract_text_basic(self, file_path):
        """Fast text extraction"""
        suffix = file_path.suffix.lower()
        try:
            if suffix in ['.txt', '.md']:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(2000)  # First 2KB only
                    return content if content else None
            elif suffix == '.html':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(2000)
                    return content if content else None
        except:
            pass
        return None
    
    def index_file(self, file_path):
        """Create minimal but useful index entry"""
        try:
            rel_path = file_path.relative_to(self.root_path)
            file_size = file_path.stat().st_size
            
            # Extract basic text content if available
            text_content = self.extract_text_basic(file_path)
            tokens = self.tokenize(text_content) if text_content else []
            
            # Use filename as additional search tokens
            filename_tokens = re.findall(r'\b\w+\b', file_path.stem.lower())
            tokens.extend(filename_tokens)
            tokens = sorted(list(set(tokens)))[:30]
            
            entry = {
                'path': str(rel_path).replace('\\', '/'),
                'filename': file_path.name,
                'file_type': file_path.suffix.lower(),
                'size_mb': round(file_size / (1024*1024), 2),
                'keywords': tokens
            }
            self.index.append(entry)
            return True
        except:
            return False
    
    def build_index(self):
        """Fast index build"""
        print(f"Building quick index for {self.root_path}...")
        
        all_files = sorted([f for f in self.root_path.rglob('*') if f.is_file()])
        
        for i, file_path in enumerate(all_files):
            if i % 50 == 0:
                print(f"  Processed {i}/{len(all_files)}...")
            
            # Skip large binaries
            if file_path.suffix in ['.bin', '.exe', '.dll', '.so']:
                continue
            
            self.index_file(file_path)
        
        print(f"✓ Indexed {len(self.index)} files")
        return self.index
    
    def save_index(self, output_dir):
        """Save as JSON"""
        output_file = Path(output_dir) / 'search_index.json'
        
        index_data = {
            'created': datetime.now().isoformat(),
            'total_files': len(self.index),
            'files': self.index
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Index saved: {output_file}")
        return output_file

if __name__ == '__main__':
    indexer = QuickIndexer('/sessions/gifted-sharp-feynman/mnt/Rosslare Documentation/')
    indexer.build_index()
    indexer.save_index('/sessions/gifted-sharp-feynman/mnt/outputs')
