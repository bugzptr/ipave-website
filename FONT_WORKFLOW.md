# Font Conversion Workflow

This document describes the workflow for managing fonts in this project.

## Overview

Fonts are stored as **TTF** files and automatically converted to **WOFF2** format for optimal web performance. WOFF2 files are typically 30-50% smaller than TTF files, resulting in faster page loads.

## Quick Start

### When Adding New Fonts

1. Add TTF font files to `assets/fonts/`
2. Run the conversion script:
   ```powershell
   .\convert-fonts.ps1
   ```
   Or on Windows Command Prompt:
   ```cmd
   convert-fonts.bat
   ```
   Or directly with Python:
   ```bash
   python convert-fonts-to-woff2.py
   ```
3. Verify WOFF2 files were created (check `assets/fonts/` directory)
4. Commit both TTF and WOFF2 files to the repository

### When Updating Existing Fonts

1. Replace the TTF file in `assets/fonts/`
2. Run the conversion script (it will automatically regenerate WOFF2)
3. Test locally to ensure fonts load correctly
4. Commit the updated files

## Script Features

The conversion script (`convert-fonts-to-woff2.py`):
- ✅ Automatically finds all TTF files in `assets/fonts/`
- ✅ Skips conversion if WOFF2 is newer than TTF (smart caching)
- ✅ Shows compression statistics (file size reduction)
- ✅ Handles errors gracefully
- ✅ Provides clear success/failure feedback

## Requirements

- Python 3.6+
- `fonttools[woff]` package:
  ```bash
  pip install fonttools[woff]
  ```

## File Structure

```
assets/fonts/
├── font-name-400.ttf          # Source file
├── font-name-400.woff2         # Generated file (smaller, faster)
├── font-name-700.ttf
├── font-name-700.woff2
└── ...
```

## CSS Configuration

The CSS is already configured to use WOFF2 as primary with TTF fallback:

```css
@font-face {
    font-family: 'Font Name';
    src: url('assets/fonts/font-name-400.woff2') format('woff2'),
         url('assets/fonts/font-name-400.ttf') format('truetype');
}
```

This ensures:
- Modern browsers load the smaller WOFF2 files
- Older browsers fall back to TTF
- Optimal performance for all users

## Troubleshooting

### Script fails with "fonttools not installed"
```bash
pip install fonttools[woff]
```

### WOFF2 files not loading in browser
1. Clear browser cache
2. Verify WOFF2 files exist in `assets/fonts/`
3. Check browser console for errors
4. Ensure server serves WOFF2 with correct MIME type (`font/woff2`)

### Fonts look different after conversion
- WOFF2 is a compressed format - visual appearance should be identical
- If issues persist, verify the source TTF file is valid
- Check that the correct font file is being used in CSS

## Best Practices

1. **Always regenerate WOFF2** when TTF files are updated
2. **Commit both formats** to the repository (TTF as source, WOFF2 for performance)
3. **Test fonts locally** before pushing to production
4. **Keep TTF files** as the source of truth (don't delete them)
5. **Run conversion script** as part of your pre-commit workflow

## Integration with CI/CD

For automated workflows, you can add the conversion script to your build process:

```yaml
# Example GitHub Actions workflow
- name: Convert fonts to WOFF2
  run: |
    pip install fonttools[woff]
    python convert-fonts-to-woff2.py
```



