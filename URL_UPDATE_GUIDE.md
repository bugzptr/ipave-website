# URL Update Guide - Production Domain Migration

This guide lists all files and locations that need URL updates when moving from the development domain (`ipave-website.pages.dev`) to your production domain.

## Quick Find & Replace

Once you know your production domain (e.g., `ipave.co.nz` or `www.ipave.co.nz`), perform a global find and replace:

**Find:** `https://ipave-website.pages.dev`
**Replace:** `https://yourdomain.co.nz` (or `https://www.yourdomain.co.nz`)

## Files That Need Updates

### Root Level HTML Files

1. **index.html**
   - Line ~18: `<meta property="og:url" content="...">`
   - Line ~24: `<meta property="twitter:url" content="...">`
   - Line ~34: `<link rel="canonical" href="...">`

2. **about.html**
   - Same meta tags as above

3. **our-process.html**
   - Same meta tags as above

4. **concrete-patio.html**
   - Same meta tags as above

### Services Directory

5. **services/index.html**
   - Line ~18: `<meta property="og:url" content="...">`
   - Line ~24: `<meta property="twitter:url" content="...">`
   - Line ~34: `<link rel="canonical" href="...">`

6. **services/residential-driveways.html**
   - Same meta tags

7. **services/commercial-paving.html**
   - Same meta tags

8. **services/concrete-repair.html**
   - Same meta tags

9. **services/decorative-concrete.html**
   - Same meta tags

10. **services/kerbing-services.html**
    - Same meta tags

### Contact Directory

11. **contact/index.html**
    - Same meta tags

### Gallery Directory

12. **gallery/index.html**
    - Same meta tags

### Projects Directory

13. **projects/index.html**
    - Same meta tags

### Team Directory

14. **team/index.html**
    - Same meta tags

### XML Files

15. **sitemap.xml**
    - All `<loc>` tags (approximately 14 URLs)

16. **robots.txt**
    - Line ~5: `Sitemap: https://...`

## Specific Locations in Each File

Each HTML file has these three locations that need updating:

```html
<!-- Location 1: Canonical URL -->
<link rel="canonical" href="https://ipave-website.pages.dev/[path]/">

<!-- Location 2: Open Graph URL -->
<meta property="og:url" content="https://ipave-website.pages.dev/[path]/">

<!-- Location 3: Twitter Card URL -->
<meta property="twitter:url" content="https://ipave-website.pages.dev/[path]/">
```

## Automated Update Script (Optional)

If you have many files, you can use a command-line tool:

### Using PowerShell (Windows):
```powershell
Get-ChildItem -Recurse -Include *.html,*.xml,*.txt | ForEach-Object {
    (Get-Content $_.FullName) -replace 'https://ipave-website.pages.dev', 'https://yourdomain.co.nz' | Set-Content $_.FullName
}
```

### Using sed (Linux/Mac):
```bash
find . -type f \( -name "*.html" -o -name "*.xml" -o -name "*.txt" \) -exec sed -i 's|https://ipave-website.pages.dev|https://yourdomain.co.nz|g' {} +
```

## Verification Checklist

After updating URLs:

- [ ] All HTML files updated
- [ ] sitemap.xml updated
- [ ] robots.txt updated
- [ ] Test homepage loads correctly
- [ ] Test all service pages
- [ ] Test contact page
- [ ] Test gallery/projects/team pages
- [ ] Verify canonical URLs in page source
- [ ] Check Open Graph tags with Facebook Debugger
- [ ] Verify sitemap.xml is accessible at new domain
- [ ] Test all internal links still work
- [ ] Test forms still submit correctly

## Important Notes

- **WWW vs Non-WWW:** Decide on one format and use consistently. Set up redirects in Cloudflare if needed.
- **Trailing Slashes:** Be consistent - either use trailing slashes everywhere or nowhere
- **HTTPS:** Always use `https://` not `http://`
- **Google Search Console:** Update your property URL after domain change
- **Google Business Profile:** Update website URL if applicable

## After URL Update

1. Submit updated sitemap to Google Search Console
2. Update Google Business Profile website URL
3. Update any external links/citations
4. Monitor for 404 errors in Google Search Console
5. Set up redirects if changing from www to non-www (or vice versa)

