# Custom Domain Setup Guide for Cloudflare Pages

This guide will help you connect your custom domain to your Cloudflare Pages site.

## Prerequisites

- Your custom domain registered and accessible
- Cloudflare account with your domain added
- Cloudflare Pages project deployed and working on `ipave-website.pages.dev`

## Step 1: Add Custom Domain in Cloudflare Pages

1. Log into your Cloudflare dashboard
2. Navigate to **Pages** → Select your project (`ipave-website`)
3. Go to **Custom domains** tab
4. Click **Set up a custom domain**
5. Enter your domain (e.g., `ipave.co.nz` or `www.ipave.co.nz`)
6. Click **Continue**

## Step 2: DNS Configuration

Cloudflare Pages will provide you with DNS records to add. You have two options:

### Option A: CNAME Record (Recommended for subdomains)

If you're using a subdomain like `www.ipave.co.nz`:

**DNS Record:**
- **Type:** CNAME
- **Name:** www (or your subdomain)
- **Target:** `ipave-website.pages.dev`
- **Proxy status:** Proxied (orange cloud)

### Option B: A Record (For root domain)

If you're using the root domain `ipave.co.nz`:

**DNS Record:**
- **Type:** A
- **Name:** @ (or root domain)
- **IPv4 address:** Use the IP addresses provided by Cloudflare Pages
- **Proxy status:** Proxied (orange cloud)

**Note:** Cloudflare Pages will provide specific IP addresses. These may change, so check the Cloudflare Pages dashboard for current values.

## Step 3: SSL Certificate

Cloudflare will automatically provision an SSL certificate for your custom domain. This typically takes a few minutes to a few hours.

**To verify SSL:**
1. Wait 5-10 minutes after adding the domain
2. Check the **Custom domains** tab in Cloudflare Pages
3. The SSL status should show "Active" when ready
4. You can test by visiting `https://yourdomain.co.nz`

## Step 4: Update Site URLs

After your domain is active, you need to update all URLs in the site files:

### Files to Update:

1. **All HTML files** - Update canonical URLs, Open Graph URLs, and Twitter card URLs
2. **sitemap.xml** - Update all location URLs
3. **robots.txt** - Update sitemap URL if needed

### Search and Replace:

Find and replace `https://ipave-website.pages.dev` with `https://yourdomain.co.nz` (or `https://www.yourdomain.co.nz`)

**Key locations in each HTML file:**
- `<link rel="canonical" href="...">`
- `<meta property="og:url" content="...">`
- `<meta property="twitter:url" content="...">`

**In sitemap.xml:**
- All `<loc>` tags

## Step 5: Verify Domain Setup

1. **Test HTTPS:** Visit `https://yourdomain.co.nz` - should load without certificate warnings
2. **Test Redirects:** Visit `https://yourdomain.co.nz/about/` - should redirect properly
3. **Test Forms:** Submit a test form to ensure Formspree still works
4. **Check SSL:** Use [SSL Labs](https://www.ssllabs.com/ssltest/) to verify certificate

## Troubleshooting

### Domain Not Resolving

- **Wait:** DNS changes can take up to 48 hours (usually much faster with Cloudflare)
- **Check DNS:** Use `dig yourdomain.co.nz` or online DNS checker
- **Verify Records:** Ensure DNS records match exactly what Cloudflare Pages shows

### SSL Certificate Not Issuing

- **Wait:** Can take up to 24 hours (usually 5-10 minutes)
- **Check DNS:** Ensure domain is properly configured
- **Contact Support:** If issues persist after 24 hours, contact Cloudflare support

### Mixed Content Warnings

- Ensure all URLs use `https://` not `http://`
- Check that all external resources (images, fonts) load over HTTPS
- Update any hardcoded URLs in HTML/CSS

## Post-Setup Checklist

- [ ] Custom domain added in Cloudflare Pages
- [ ] DNS records configured correctly
- [ ] SSL certificate active
- [ ] All HTML files updated with new domain
- [ ] sitemap.xml updated with new domain
- [ ] robots.txt updated (if needed)
- [ ] Site loads correctly on custom domain
- [ ] Forms still working
- [ ] All internal links working
- [ ] Redirects functioning properly

## Important Notes

- **Keep Pages.dev URL:** The `ipave-website.pages.dev` URL will continue to work and redirect to your custom domain
- **WWW vs Non-WWW:** Decide whether to use `www.yourdomain.co.nz` or `yourdomain.co.nz` and set up redirects accordingly
- **Google Search Console:** Update your property URL after domain change
- **Google Business Profile:** Update website URL if you have a GBP listing

## Need Help?

- Cloudflare Pages Documentation: https://developers.cloudflare.com/pages/platform/custom-domains/
- Cloudflare Support: Available in dashboard

