# Rosslare Documentation Search Tool

Fast full-text search across your entire Rosslare documentation library.

**🔍 Search Tool:** https://qxr-repository.github.io/rosslare-docs-search

## Features

- ⚡ **Lightning-fast search** - Instant results as you type
- 📄 **Full-text content search** - Search within document content
- 🔗 **One-click file opening** - Click results to open files directly
- 🔄 **Auto-updating** - Always shows the latest documentation index
- 📊 **263+ documents indexed** - Searchable metadata and content

## For Your Team

**Just bookmark this URL:**
```
https://qxr-repository.github.io/rosslare-docs-search
```

No downloads, no updates needed. It always shows the latest index!

### How to Use

1. Open the search tool (bookmark the URL above)
2. Type your search term (e.g., "firmware", "AC-825", "wiring")
3. Results appear instantly
4. Click any result to open the file

## For Maintenance (Josiah)

### When You Add New Documentation

1. Add files to your OneDrive `Rosslare Documentation` folder
2. Run the update script:
   ```bash
   UPDATE_INDEX.bat
   ```
3. Push the updated index to GitHub:
   ```bash
   git add search_index.json
   git commit -m "Update index - added new documentation"
   git push
   ```

That's it! Your team will automatically see the new files in their next search.

### Files in This Repository

- **index.html** - The search interface (hosted on GitHub Pages)
- **search_index.json** - The searchable index (metadata and snippets)
- **README.md** - This file

### Note on Document Files

The actual document files (PDFs, Word docs, etc.) are stored on OneDrive, not in this repository. The search index contains metadata and snippets only, keeping this repository small and fast.

---

**Deployment:** GitHub Pages  
**Last Updated:** 2026-05-13  
**Total Indexed Files:** 263  
**Search Tool Status:** ✅ Active
