# Post-Launch Documentation

This guide covers tasks and procedures to complete after the site goes live.

## Analytics Setup

### Cloudflare Web Analytics

**Current Status:** Analytics script is in HTML but needs token replacement.

**Setup Steps:**

1. **Enable Web Analytics in Cloudflare:**
   - Log into Cloudflare dashboard
   - Navigate to your domain → **Analytics & Logs** → **Web Analytics**
   - Click **Enable Web Analytics**
   - Copy your unique token (will be provided by Cloudflare)

2. **Update Token in HTML Files:**
   - Find this line in all HTML files:
     ```html
     <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "YOUR_TOKEN_HERE"}'></script>
     ```
   - Replace `YOUR_TOKEN_HERE` with your actual token
   - **Note:** Currently, this script may not be present in all files. Add it to:
     - `index.html` (homepage)
     - Key pages (services, contact, about)

3. **Add Analytics Script:**
   If the script isn't present, add it before `</body>` tag:
   ```html
   <!-- Cloudflare Web Analytics - Privacy-focused analytics without cookies -->
   <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "YOUR_TOKEN_HERE"}'></script>
   ```

4. **Verify Implementation:**
   - Wait 24 hours after adding token
   - Check Cloudflare dashboard for incoming data
   - Real-time data should appear immediately

**Files to Update:** All HTML files (15 files total)

## Image Replacement Guide

### Current Status
All pages currently use placeholder images (`paved-driveway.jpg`). When client images arrive, follow this guide.

### Image Requirements

**Format:** WebP (preferred) or JPG
**Optimization:** Compress before uploading
**Naming Convention:** Descriptive names (e.g., `residential-driveway-exposed-aggregate.jpg`)

### Responsive Image Setup

For each image, create three sizes:

1. **Mobile (≤600px):** ~362x242px, WebP format, ~25KB
2. **Tablet (601-900px):** ~500x334px, WebP format, ~40KB  
3. **Desktop (≥901px):** ~800x534px, WebP format, ~60KB

### Where to Replace Images

#### Gallery Page (`gallery/index.html`)
- Replace 6 gallery items with actual project photos
- Update alt text to match actual projects
- Maintain responsive `<picture>` elements

#### Projects Page (`projects/index.html`)
- Replace 3 project card images
- Update alt text with project-specific descriptions

#### Service Pages (`services/*.html`)
- Add service-specific hero images
- Replace placeholder images with relevant service photos

#### Homepage (`index.html`)
- Replace service highlight image
- Consider adding more service images

### Image Replacement Steps

1. **Optimize Images:**
   - Use Squoosh.app or Paint.NET
   - Export as WebP format
   - Target file sizes listed above

2. **Upload to Repository:**
   - Place in `assets/images/` directory
   - Use descriptive filenames
   - Keep original JPG as fallback

3. **Update HTML:**
   - Replace image `src` attributes
   - Update `srcset` for responsive images
   - Update `alt` text with descriptive, keyword-rich descriptions
   - Maintain `<picture>` element structure

4. **Example Update:**
   ```html
   <!-- Before -->
   <img src="../assets/images/paved-driveway.jpg" alt="Residential driveway">
   
   <!-- After -->
   <picture>
     <source media="(max-width: 600px)" 
             srcset="assets/images/driveway-mobile.webp" 
             type="image/webp">
     <source media="(max-width: 900px)" 
             srcset="assets/images/driveway-tablet.webp" 
             type="image/webp">
     <source media="(min-width: 901px)" 
             srcset="assets/images/driveway-desktop.webp" 
             type="image/webp">
     <img src="assets/images/driveway.jpg" 
          alt="Exposed aggregate residential driveway in Christchurch with custom stone selection" 
          loading="lazy" 
          width="800" 
          height="534" 
          class="service-image">
   </picture>
   ```

5. **Test After Replacement:**
   - Verify images load correctly
   - Check responsive behavior on mobile/tablet/desktop
   - Verify alt text is descriptive
   - Test page load speed (should maintain 90+ scores)

### Image Optimization Tools

- **Squoosh.app:** Online tool, easy to use
- **Paint.NET:** Windows application, supports WebP export
- **ImageOptim:** Mac application
- **Cloudflare Image Resizing:** Can be configured for automatic resizing

## Content Update Procedures

### Adding New Pages

1. **Create HTML file** following existing template structure
2. **Add to navigation** (header and/or footer)
3. **Update sitemap.xml** with new page URL
4. **Add meta tags** (title, description, Open Graph, Twitter)
5. **Test on all devices**
6. **Submit updated sitemap** to Google Search Console

### Updating Existing Content

1. **Edit HTML file** directly
2. **Maintain NAP consistency** (Name, Address, Phone)
3. **Update lastmod date** in sitemap.xml if significant changes
4. **Test changes** before deploying
5. **Commit and push** to trigger Cloudflare Pages deployment

### Blog/News Section (Future)

If adding a blog section:
- Create `/blog/` directory
- Use consistent URL structure: `/blog/post-name.html`
- Add to sitemap.xml
- Consider RSS feed for syndication

## SEO Monitoring Checklist

### Weekly Tasks

- [ ] Check Google Search Console for errors
- [ ] Monitor search rankings for key terms
- [ ] Review analytics for traffic patterns
- [ ] Check for 404 errors
- [ ] Verify forms are receiving submissions

### Monthly Tasks

- [ ] Review and update content
- [ ] Check backlinks and citations
- [ ] Update sitemap.xml if new pages added
- [ ] Review and optimize underperforming pages
- [ ] Check mobile usability in Search Console

### Quarterly Tasks

- [ ] Comprehensive SEO audit
- [ ] Review and update meta descriptions
- [ ] Check and fix broken links
- [ ] Update structured data if needed
- [ ] Review competitor strategies

## Google Business Profile Updates

### After Domain Launch

1. **Update Website URL:**
   - Log into Google Business Profile
   - Go to **Info** section
   - Update website URL to new domain
   - Verify NAP matches website exactly

2. **Verify NAP Consistency:**
   - Name: I Pave Concrete & Asphalt
   - Address: 335 Kainga Road, Kainga, Christchurch 8083, New Zealand
   - Phone: 0800 472 8348
   - Website: [your new domain]

3. **Add Photos:**
   - Upload project photos
   - Add team photos
   - Update cover photo

4. **Monitor Reviews:**
   - Respond to reviews promptly
   - Encourage satisfied customers to leave reviews

## Performance Monitoring

### Key Metrics to Track

- **PageSpeed Scores:** Maintain 90+ mobile, 95+ desktop
- **Core Web Vitals:** CLS (0), LCP (<2.5s), FID (<100ms)
- **Uptime:** Should be 99.9%+ with Cloudflare Pages
- **Form Submissions:** Monitor Formspree dashboard

### Tools for Monitoring

- **Google PageSpeed Insights:** Weekly checks
- **Google Search Console:** Daily monitoring
- **Cloudflare Analytics:** Real-time traffic
- **Formspree Dashboard:** Form submission tracking

## Backup and Version Control

### Current Setup

- Site is in Git repository
- Cloudflare Pages auto-deploys from `main` branch
- All changes are version controlled

### Best Practices

- **Commit frequently** with descriptive messages
- **Test locally** before pushing to main
- **Keep backups** of important content
- **Document major changes** in commit messages

## Troubleshooting Common Issues

### Forms Not Submitting

1. Check Formspree endpoint URL
2. Verify form has `action` attribute
3. Check browser console for errors
4. Test with different email addresses
5. Verify Formspree account is active

### Images Not Loading

1. Check file paths (relative vs absolute)
2. Verify images are in correct directory
3. Check file permissions
4. Verify image format is supported
5. Check browser console for 404 errors

### Performance Issues

1. Run PageSpeed Insights
2. Check image file sizes
3. Verify WebP images are loading
4. Check for render-blocking resources
5. Review Cloudflare cache settings

### SEO Issues

1. Verify sitemap.xml is accessible
2. Check robots.txt allows crawling
3. Verify canonical URLs are correct
4. Check structured data with Google Rich Results Test
5. Monitor Search Console for errors

## Contact Information

**For Technical Issues:**
- Check Cloudflare Pages dashboard
- Review Cloudflare documentation
- Check Formspree documentation for form issues

**For Content Updates:**
- Edit HTML files directly
- Follow content update procedures above
- Test changes before deploying

## Quick Reference

### Important URLs (Update with Production Domain)

- **Homepage:** `https://ipave-website.pages.dev/`
- **Sitemap:** `https://ipave-website.pages.dev/sitemap.xml`
- **Robots:** `https://ipave-website.pages.dev/robots.txt`

### Key Files

- **Navigation:** Header in each HTML file
- **Footer:** Footer in each HTML file  
- **Sitemap:** `sitemap.xml`
- **Redirects:** `_redirects`
- **Styles:** `assets/css/style.css`

### Form Endpoint

- **Formspree:** `https://formspree.io/f/xjkodern`
- **Email:** admin@ipave.co.nz

---

**Last Updated:** 2025-01-10
**Next Review:** After launch + 1 month

