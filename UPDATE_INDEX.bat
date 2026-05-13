@echo off
REM This script updates the search index with any new files you've added
REM Just run this whenever you add new documents to your Rosslare Documentation folder

echo.
echo ========================================
echo  Updating Rosslare Documentation Index
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    pause
    exit /b 1
)

REM Run the index update scripts
echo Building index from files...
echo.

cd /d "%~dp0"

REM Update metadata index
python smart_content_index.py
if errorlevel 1 (
    echo ERROR: Failed to build content index
    pause
    exit /b 1
)

REM Update metadata index
python quick_index.py
if errorlevel 1 (
    echo ERROR: Failed to build metadata index
    pause
    exit /b 1
)

REM Merge the indexes
python << 'PYTHON_SCRIPT'
import json
from pathlib import Path

# Load both indexes
with open('search_index.json', 'r') as f:
    metadata_index = json.load(f)

with open('content_index.json', 'r') as f:
    content_index = json.load(f)

# Create a combined index
combined = {}
for file in metadata_index['files']:
    path = file['path']
    combined[path] = {
        'path': path,
        'filename': file['filename'],
        'file_type': file['file_type'],
        'keywords': file.get('keywords', []),
        'snippet': file.get('snippet', ''),
        'content': '',
        'has_content': False
    }

# Add content where available
for file in content_index['files']:
    path = file['path']
    if path in combined:
        combined[path]['content'] = file.get('content', '')
        combined[path]['snippet'] = file.get('snippet', '')
        combined[path]['keywords'] = list(set(combined[path]['keywords'] + file.get('keywords', [])))[:50]
        combined[path]['has_content'] = True
    else:
        combined[path] = {
            'path': path,
            'filename': file['filename'],
            'file_type': file['file_type'],
            'keywords': file.get('keywords', []),
            'snippet': file.get('snippet', ''),
            'content': file.get('content', ''),
            'has_content': True
        }

# Filter out search tools
combined = {k: v for k, v in combined.items()
            if not v['filename'].lower().startswith('search')
            and v['file_type'] != '.html'}

# Save merged index
merged_data = {
    'created': metadata_index['created'],
    'total_files': len(combined),
    'files_with_content': sum(1 for f in combined.values() if f['has_content']),
    'files': list(combined.values())
}

with open('search_index.json', 'w') as f:
    json.dump(merged_data, f, indent=2, ensure_ascii=False)

print(f"✓ Index updated successfully!")
print(f"  Total files: {len(combined)}")
print(f"  Files with content: {merged_data['files_with_content']}")
PYTHON_SCRIPT

echo.
echo ========================================
echo  ✓ Index updated successfully!
echo ========================================
echo.
echo Your team can now download the new search_index.json file
echo search.html stays the same - it auto-loads the new index!
echo.
pause
