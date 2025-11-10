# Pre-Launch Technical Checklist

Use this checklist to verify all technical aspects of the site before going live.

## Forms Testing

### Formspree Forms
All forms submit to: `https://formspree.io/f/xjkodern`

**Forms to test:**
- [ ] Homepage hero form (index.html)
- [ ] Footer form (all pages)
- [ ] Contact page form (contact/index.html)

**Test each form:**
- [ ] Form displays correctly
- [ ] Required fields are marked
- [ ] Form validation works (try submitting empty)
- [ ] Form submits successfully
- [ ] Success message appears (or redirects)
- [ ] Email notification received at admin@ipave.co.nz

**Files with forms:** 15 files total (all HTML pages)

## Links Testing

### Internal Links
- [ ] All navigation links work
- [ ] Footer service links work
- [ ] Cross-page links (gallery → projects, etc.)
- [ ] "Learn More" buttons on service pages
- [ ] "Get a quote" buttons
- [ ] Breadcrumb navigation (if implemented)

### External Links
- [ ] Phone links (`tel:08004728348`) work on mobile
- [ ] Email links (`mailto:admin@ipave.co.nz`) work
- [ ] NZCCA logo link works
- [ ] All links open in correct tabs (target="_blank" where appropriate)

### Phone Links
**Test on mobile device:**
- [ ] Clicking phone number initiates call
- [ ] Phone number displays correctly: 0800 472 8348
- [ ] Phone links work on all pages (15 files)

## Mobile Responsiveness

### Test on Multiple Devices
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] iPad/Tablet
- [ ] Desktop (Chrome, Firefox, Edge, Safari)

### Key Mobile Checks
- [ ] Navigation menu works (hamburger menu if implemented)
- [ ] Text is readable (no horizontal scrolling)
- [ ] Images scale properly
- [ ] Forms are easy to fill out
- [ ] Buttons are tappable (minimum 44x44px)
- [ ] Phone number is clickable
- [ ] Footer displays correctly
- [ ] Hero sections display properly

### Responsive Breakpoints
- [ ] Mobile (≤600px)
- [ ] Tablet (601-900px)
- [ ] Desktop (≥901px)

## Performance Testing

### PageSpeed Insights
Test key pages:
- [ ] Homepage (index.html)
- [ ] Services overview (services/index.html)
- [ ] Contact page (contact/index.html)
- [ ] One service detail page

**Target Scores:**
- Mobile: 90+ (currently achieving 98+)
- Desktop: 95+ (currently achieving 100)

**Key Metrics:**
- [ ] CLS (Cumulative Layout Shift): 0 (currently perfect)
- [ ] LCP (Largest Contentful Paint): < 2.5s
- [ ] FID (First Input Delay): < 100ms
- [ ] Speed Index: < 3.4s

### Image Optimization
- [ ] All images have responsive srcsets (WebP format)
- [ ] Images have descriptive alt text
- [ ] Images use lazy loading where appropriate
- [ ] Logo images load immediately (not lazy)

## SEO & Meta Tags

### Meta Tags Check
On each page verify:
- [ ] Unique `<title>` tag
- [ ] Unique `<meta name="description">`
- [ ] Open Graph tags (og:title, og:description, og:url, og:image)
- [ ] Twitter Card tags
- [ ] Canonical URL present
- [ ] Robots meta tag (index, follow)

### Structured Data
- [ ] LocalBusiness JSON-LD on homepage
- [ ] Service schema on service pages (if implemented)
- [ ] Validate with Google Rich Results Test

### Sitemap & Robots
- [ ] sitemap.xml accessible at `/sitemap.xml`
- [ ] robots.txt accessible at `/robots.txt`
- [ ] robots.txt references sitemap correctly
- [ ] All pages included in sitemap.xml

## Accessibility

### Basic Checks
- [ ] All images have alt text
- [ ] Form labels are present (visually hidden where appropriate)
- [ ] Headings follow logical hierarchy (h1 → h2 → h3)
- [ ] Links have descriptive text (not just "click here")
- [ ] Color contrast meets WCAG AA standards
- [ ] Keyboard navigation works

### ARIA Labels
- [ ] Navigation has `aria-label`
- [ ] Forms have proper `aria-required` attributes
- [ ] Skip links present (if implemented)

## Browser Compatibility

### Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Key Features to Verify
- [ ] CSS Grid/Flexbox displays correctly
- [ ] Fonts load properly
- [ ] Forms work
- [ ] JavaScript functions (if any)
- [ ] Images display

## Redirects Testing

### _redirects File
Test all redirects:
- [ ] `/about/` → `/about.html` (301)
- [ ] `/history/` → `/about.html` (301)
- [ ] `/leadership/` → `/about.html` (301)
- [ ] `/projects-2/` → `/projects/` (301)
- [ ] `/shop/` → `/services/` (301)
- [ ] `/cart/` → `/contact/` (301)
- [ ] `/checkout/` → `/contact/` (301)
- [ ] `/my-account/` → `/contact/` (301)

**Note:** Redirects work on Cloudflare Pages automatically

## NAP Consistency

### Name, Address, Phone
Verify consistent across all pages:
- [ ] Business Name: "I Pave Concrete & Asphalt"
- [ ] Address: "335 Kainga Road, Kainga, Christchurch 8083, New Zealand"
- [ ] Phone: "0800 472 8348"
- [ ] Email: "admin@ipave.co.nz"

**Check locations:**
- [ ] Footer on all pages
- [ ] Contact page
- [ ] Structured data (JSON-LD)

## Security

### HTTPS
- [ ] Site loads over HTTPS
- [ ] No mixed content warnings
- [ ] SSL certificate valid
- [ ] HSTS headers (handled by Cloudflare)

### Forms
- [ ] Formspree endpoint uses HTTPS
- [ ] No sensitive data in HTML source
- [ ] CSRF protection (Formspree handles this)

## Content Review

### Spelling & Grammar
- [ ] No typos in content
- [ ] Consistent terminology
- [ ] Professional tone throughout

### Content Completeness
- [ ] All service pages have content
- [ ] Gallery page has descriptions
- [ ] Projects page has case studies
- [ ] Team page has bios
- [ ] Contact page has all information

## Analytics Setup (Post-Launch)

### Cloudflare Web Analytics
- [ ] Token obtained from Cloudflare dashboard
- [ ] Token added to HTML (replace `YOUR_TOKEN_HERE`)
- [ ] Analytics script loads correctly
- [ ] Data appears in dashboard (after 24 hours)

## Post-Launch Tasks

### Immediate (Day 1)
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Update Google Business Profile website URL
- [ ] Test all forms in production
- [ ] Monitor for errors

### Week 1
- [ ] Check Google Search Console for indexing
- [ ] Monitor analytics for traffic
- [ ] Check for 404 errors
- [ ] Verify all redirects working
- [ ] Test on multiple devices/browsers

### Month 1
- [ ] Review analytics data
- [ ] Check search rankings
- [ ] Gather user feedback
- [ ] Plan content updates

## Quick Test Script

Run these quick checks:

```bash
# Check all HTML files exist
find . -name "*.html" | wc -l  # Should be 15+

# Check for broken internal links (manual review)
# Check sitemap.xml is valid XML
# Check robots.txt format
```

## Notes

- Forms use Formspree - test with real submissions
- Phone links need mobile device testing
- Performance scores are already excellent - maintain them
- All images currently use placeholder - ready for client images
- Domain URLs need updating when custom domain is configured

## Issues Found

Document any issues found during testing:

1. 
2. 
3. 

---

**Last Updated:** 2025-01-10
**Tested By:** ________________
**Date:** ________________

