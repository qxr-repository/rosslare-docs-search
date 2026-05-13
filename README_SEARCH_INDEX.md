# Documentation Search Index

Your Rosslare documentation has been fully indexed for **fast full-text searching**. Here's how to use it:

## 🚀 Quick Start (For Your Team)

**Your team:**
1. Download `search.html` from OneDrive
2. Download `search_index.json` from OneDrive (same folder)
3. Save both files in the same folder on their computer
4. Double-click `search.html` to start searching
5. **Keep doing this for all future updates** - no re-downloads needed!

That's it! The search tool will auto-load the latest index every time they open it.

## 📊 What's Indexed

- **263 documentation files** (search.html filtered out)
- **Filenames & metadata** from all files
- **Full text content** from 24 documents (DOCX, MD, TXT, HTML files)
- **Keywords & snippets** extracted from all indexed content
- File types: PDF, DOCX, MD, TXT, HTML, and more

## 🎯 Search Features

**Toggle Search Modes:**
- ✓ Search in content (full-text search in document text)
- ✓ Search in filenames (search file & folder names)
- ✓ One-click file opening (click result to open file)

**Result Indicators:**
- 📋 Preview - Shows file preview/snippet
- 📄 Content - Indicates file with searchable full text
- ↗ Clickable - Click to open the file directly

## ⚡ Example Searches

- `firmware AC-825` - Find AC-825 firmware documents
- `wiring diagram` - Locate wiring guides
- `panel configuration` - Find panel setup documentation
- `installation` - Find installation guides
- `troubleshooting` - Find troubleshooting resources
- `axtrax` - Find AxtraxNG and AxtraxPro content

## 🔄 Updating the Index (For You)

When you add new files to your documentation folder:

**Windows:** Double-click `UPDATE_INDEX.bat` in this folder
- Automatically rebuilds the index
- Updates `search_index.json` file
- Your team just needs to re-download the new `search_index.json`

**Or manually:**
```bash
python quick_index.py              # Scan all files
python smart_content_index.py      # Extract document content
```

Then upload the updated `search_index.json` to OneDrive.

## 📁 Files for Your Team

- **search.html** - Download once, keep forever ⭐
- **search_index.json** - Re-download when you update the index
- Both files must be in the same folder

## 🛠️ Additional Scripts (For Index Updates)

- **UPDATE_INDEX.bat** - One-click index rebuild (Windows)
- **quick_index.py** - Rebuild metadata only
- **smart_content_index.py** - Extract content from documents

---

**Index created:** 2026-05-13  
**Total files:** 263  
**Files with searchable content:** 24  
**Deployment method:** OneDrive Download  
**Ready to use!** 🚀
