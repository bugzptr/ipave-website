

# I Pave Concrete Website

A fast, modern, and maintainable static website for I Pave Concrete, built with pure HTML, CSS, and vanilla JavaScript. This project replaces a previous WordPress site and is hosted on Cloudflare Pages for optimal performance and security.

## Project Overview

*   **Goal:** To create a high-performance, secure, and easily updatable marketing website.
*   **Methodology:** A static site build that removes the overhead and security vulnerabilities of a dynamic CMS like WordPress. Reusable components like the header and footer are handled client-side with a minimal JavaScript loader.

## Tech Stack & Hosting

*   **Frontend:** HTML5, CSS3 (with Custom Properties), Vanilla JavaScript (ES6)
*   **Hosting:** [Cloudflare Pages](https://pages.cloudflare.com/)
*   **Form Handling:** [Formspree](https://formspree.io/) for processing contact form submissions.

---

## Design System & Brand Guidelines

This site is built according to the official I Pave Concrete brand guide. All styling is managed through CSS Custom Properties (variables) for easy maintenance and brand consistency.

### Color Palette

The color system is defined in `:root` within `assets/css/style.css`.

| Role | Name | Hex Code | CSS Variable |
| :--- | :--- | :--- | :--- |
| **Primary** | Engineer Blue | `#212161` | `var(--color-primary)` |
| **Accent** | Safety Vest Yellow | `#FDE906` | `var(--color-accent)` |
| **Neutral** | Concrete Gray | `#E0E0E0` | `var(--color-light-gray)` |
| **Neutral** | Asphalt Black | `#000000` | `var(--color-dark)` |
| **Neutral** | White | `#FFFFFF` | `var(--color-white)` |
| **Text** | Body Text | `#333333` | `var(--color-text-body)` |

### Typography

All font files are self-hosted in the `/assets/fonts/` directory for performance and privacy.

| Role | Font Family | Weight | Implementation |
| :--- | :--- | :--- | :--- |
| **Headings** | Montserrat | 700 (Bold) | `var(--font-family-heading)` |
| **Body Text** | ABeeZee | 400 (Regular) | `var(--font-family-body)` |

---

## Project Structure

The file structure is organized for clarity and separation of concerns.

```
i-pave-website/
├── 📂 assets/
│   ├── 📂 css/
│   │   ├── style.css          # Main stylesheet
│   │   ├── components.css     # Reusable component styles
│   │   └── pages.css          # Page-specific styles
│   ├── 📂 fonts/
│   │   └── (font files .woff2) # Self-hosted web fonts
│   ├── 📂 images/
│   │   ├── logos/             # Logo variations
│   │   ├── services/          # Service-specific imagery
│   │   ├── projects/          # Project portfolio images
│   │   └── team/              # Team member photos
│   └── 📂 js/
│       ├── navigation.js      # Navigation functionality
│       └── forms.js           # Form handling and validation
│
├── 📂 services/               # Service pages directory
│   ├── residential-driveways.html
│   ├── commercial-paving.html
│   ├── concrete-repair.html
│   ├── decorative-concrete.html
│   ├── kerbing-services.html
│   └── index.html             # Services overview page
│
├── 📂 about/                  # About pages directory
│   ├── index.html             # Company story
│   ├── team.html              # Team members
│   └── projects.html          # Portfolio showcase
│
├── 📂 contact/                # Contact pages directory
│   ├── index.html             # Contact form
│   └── quote-request.html     # Quote request form
│
├── index.html                 # Homepage
├── robots.txt                 # Search engine directives
├── sitemap.xml                # Site structure for search engines
└── README.md                  # Project documentation
```

## Development Guidelines

### CSS Variables
All design tokens (colors, fonts, spacing) are defined as CSS variables in `:root`. **Always use these variables** instead of hardcoding hex values or font names to maintain consistency.

```css
/* Example Usage */
.cta-banner {
  background-color: var(--color-accent);
  font-family: var(--font-family-heading);
}
```

### Responsive Design
The site is designed to be fully responsive. Media queries are used to adjust layouts for tablet and mobile devices. All new components should be tested across a range of screen sizes.

---

## Getting Started

### Prerequisites

*   A modern code editor (e.g., VS Code, Cursor).
*   The **Live Server** extension for VS Code/Cursor is highly recommended for local development.

### Local Development

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd ipave-website
    ```
3.  **Launch the development server:**
    *   Right-click on the `index.html` file in your editor.
    *   Select "Open with Live Server".
    *   This will open the site in your default browser and automatically reload the page whenever you save a file.

## Deployment

The site is configured for continuous deployment on **Cloudflare Pages**. Any push to the `main` branch of the Git repository will automatically trigger a new build and deploy the changes to the live website.

## Service Pages Development Plan

### Phase 1: Services Overview Page (`/services/index.html`)
**Purpose:** Central hub for all services with cross-linking strategy
**Content Structure:**
- Hero section with services overview
- Grid layout of all service categories
- Each service card links to detailed service page
- Call-to-action for quote requests
- Internal linking to homepage and contact page

**SEO Strategy:**
- Primary keyword: "concrete services Christchurch"
- Secondary keywords: "driveway paving", "commercial paving", "concrete repair"
- Internal links to all service detail pages
- Schema markup for Service schema type

### Phase 2: Individual Service Pages
**Residential Driveways (`/services/residential-driveways.html`)**
- Hero with service-specific imagery
- Detailed service description and benefits
- Process explanation (3-4 steps)
- Before/after gallery
- FAQ section
- Related services cross-links
- Quote request CTA

**Commercial Paving (`/services/commercial-paving.html`)**
- Commercial-specific benefits and applications
- Project types (parking lots, warehouse floors, etc.)
- Durability and maintenance information
- Case studies or testimonials
- Related services cross-links

**Concrete Repair (`/services/concrete-repair.html`)**
- Common repair scenarios
- Repair techniques and materials
- Maintenance tips
- Emergency repair information
- Related services cross-links

**Decorative Concrete (`/services/decorative-concrete.html`)**
- Decorative options and finishes
- Color and texture choices
- Application areas
- Maintenance requirements
- Related services cross-links

**Kerbing Services (`/services/kerbing-services.html`)**
- Kerbing types and materials
- Installation process
- Maintenance and durability
- Design options
- Related services cross-links

### Phase 3: Cross-Linking Strategy for SEO
**Homepage Integration:**
- Update "Our Services" section to link to `/services/`
- Add service-specific CTAs linking to individual service pages
- Include service highlights with "Learn More" links

**Navigation Updates:**
- Main navigation includes "Services" dropdown
- Footer services list links to individual pages
- Breadcrumb navigation on all service pages

**Internal Linking Structure:**
```
Homepage → Services Overview → Individual Service Pages
Individual Service Pages → Related Services (cross-links)
All Pages → Contact/Quote Request Forms
```

### Phase 4: Content Optimization
**Each Service Page Includes:**
- Unique, detailed content (800-1200 words minimum)
- Service-specific keywords and long-tail phrases
- Local SEO elements (Christchurch, Canterbury references)
- Customer testimonials and case studies
- Clear calls-to-action
- Contact information and quote request forms

**Technical SEO Requirements:**
- Unique meta titles and descriptions
- Proper heading hierarchy (H1, H2, H3)
- Image alt text optimization
- Schema markup for services
- Fast loading times (maintain PageSpeed scores)
- Mobile-first responsive design

### Phase 5: Performance & Maintenance
**Performance Considerations:**
- Optimize images for each service page
- Lazy load non-critical images
- Minimize CSS and JavaScript for each page
- Maintain critical CSS inlining strategy

**Content Maintenance:**
- Regular content updates and seasonal promotions
- Customer feedback integration
- Portfolio updates and new project showcases
- Service area expansion updates

---

## Important Considerations

### Contact Forms

*   The contact and footer forms are static HTML elements.
*   They submit to **Formspree** to process the data and send an email notification.
*   The `action` attribute of each `<form>` tag must be set to the correct Formspree endpoint URL.

### Asset Management

*   **Images:** Place all images in the `/assets/images/` folder. Use descriptive filenames (e.g., `residential-driveway-paving.jpg`). Use SVGs for logos and icons whenever possible.
*   **Fonts:** All fonts are self-hosted in `/assets/fonts/`. Ensure you have the correct `.woff2` files for any new font styles or weights.

### Image Optimization with Squoosh - Hybrid Approach

For optimal performance AND quality, we use a hybrid approach: WebP for mobile/tablet (speed) and PNG for desktop (maximum quality).

#### Current Image: `paved-driveway.jpg`
**Required sizes for responsive design (based on PageSpeed Insights):**

1. **Mobile (≤600px):** `paved-driveway-mobile.webp`
   - Dimensions: 362x242px (actual display size)
   - Format: WebP
   - Quality: 90-95% (for sharpness)
   - Target file size: <25KB
   - **Savings:** 114.6KB (from 139.6KB)

2. **Tablet (601-900px):** `paved-driveway-tablet.webp`
   - Dimensions: 500x334px (intermediate size)
   - Format: WebP
   - Quality: 90-95% (for sharpness)
   - Target file size: <40KB
   - **Savings:** 99.6KB (from 139.6KB)

3. **Desktop (≥901px):** `paved-driveway-desktop.webp`
   - Dimensions: 800x534px (actual display size per PageSpeed)
   - Format: WebP
   - Quality: 85-90% (excellent quality, much smaller than lossless)
   - Target file size: <60KB
   - **Savings:** 79.6KB (from 139.6KB)

#### Image Optimization Tools:

**Option 1: Paint.NET (Recommended)**
- **File Format:** Save as WebP
- **Quality Settings:** 
  - Mobile: 90-95% quality
  - Tablet: 90-95% quality  
  - Desktop: 85-90% quality
- **Resize:** Use Image → Resize to exact dimensions
- **Save Settings:** Enable "Lossy" compression (not lossless)

**Option 2: Squoosh (Alternative)**
- **For Mobile/Tablet (WebP):**
  - **Compression:** WebP
  - **Quality:** 90-95% (for sharpness)
  - **Resize:** Enable, maintain aspect ratio
  - **Metadata:** Remove unnecessary metadata
  - **Advanced:** Enable "Sharp YUV" if available

- **For Desktop (WebP):**
  - **Compression:** WebP
  - **Quality:** 85-90% (excellent quality, much smaller than lossless)
  - **Resize:** Enable, maintain aspect ratio
  - **Metadata:** Remove unnecessary metadata
  - **Advanced:** Enable "Sharp YUV" if available

#### Paint.NET Workflow:

1. **Open your original image** in Paint.NET
2. **Resize for each target size:**
   - **Mobile:** Image → Resize → 362 × 242 pixels
   - **Tablet:** Image → Resize → 500 × 334 pixels  
   - **Desktop:** Image → Resize → 800 × 534 pixels
3. **Save as WebP:** File → Save As → WebP format
4. **Quality settings:**
   - **Mobile/Tablet:** 90-95% quality (sharp, fast)
   - **Desktop:** 85-90% quality (excellent, optimized)
5. **Ensure "Lossy" is enabled** (not lossless)
6. **Fallback:** Keep original `paved-driveway.jpg` for browsers without WebP support

#### Benefits:
- **Mobile users:** Download only 25KB instead of 139.6KB (82% reduction)
- **Tablet users:** Download only 40KB instead of 139.6KB (71% reduction)
- **Desktop users:** Download only 60KB instead of 139.6KB (57% reduction) + **excellent quality**
- **Total savings:** ~120KB per image
- **Best of both worlds:** Speed on mobile, excellent quality on desktop
- **Improved LCP:** Faster image loading on all devices
- **Better Core Web Vitals:** Reduced CLS and improved performance scores
- **User satisfaction:** All users get fast-loading, high-quality images

### SEO & Content Strategy

*   **Keywords:** Each service page should target specific, relevant keywords while maintaining natural readability.
*   **Internal Linking:** Implement strategic internal linking between related services and the homepage.
*   **Content Updates:** Regular content updates help maintain search engine relevance and user engagement.
*   **Local SEO:** Include location-specific information and references to service areas.

---

## Redirect Strategy for Legacy Pages

### Current Sitemap Analysis
The existing `sitemap.xml` currently only references the homepage. However, if there are legacy WordPress URLs or other existing pages that need to be maintained, proper redirects must be implemented.

### Redirect Implementation for Cloudflare Pages

**Option 1: Cloudflare Pages Redirects (Recommended)**
Create a `_redirects` file in the root directory:
```
# Legacy page redirects
/old-page /new-page 301
/old-service /services/new-service 301
/blog/post-name /about/projects 301

# Catch-all for old WordPress structure
/wp-content/* / 301
/wp-admin/* / 301
/wp-includes/* / 301

# Redirect old service URLs to new service pages
/services/driveway-paving /services/residential-driveways 301
/services/commercial-concrete /services/commercial-paving 301
/services/concrete-maintenance /services/concrete-repair 301
```

**Option 2: HTML Meta Refresh Redirects**
For pages that can't use Cloudflare redirects, implement meta refresh:
```html
<meta http-equiv="refresh" content="0; url=/new-page-url">
```

### Redirect Types and SEO Impact

**301 Redirects (Permanent)**
- Use for permanently moved content
- Passes 90-99% of SEO value
- Ideal for service page migrations
- Update internal links accordingly

**302 Redirects (Temporary)**
- Use for temporary content moves
- Minimal SEO value transfer
- Good for maintenance periods
- Update to 301 when permanent

### Redirect Audit Process

1. **Identify Legacy URLs:**
   - Export existing sitemap from WordPress
   - Check Google Search Console for indexed URLs
   - Review analytics for incoming traffic sources

2. **Map Redirect Destinations:**
   - Legacy service pages → New service pages
   - Blog posts → Relevant service pages or about section
   - Category pages → Services overview page

3. **Implement Redirects:**
   - Create `_redirects` file for Cloudflare Pages
   - Test redirects locally before deployment
   - Monitor 404 errors after deployment

4. **Update Internal Links:**
   - Scan existing content for old URLs
   - Update all internal references
   - Ensure new service pages are properly linked

### SEO Considerations for Redirects

*   **Maintain Link Equity:** Proper redirects preserve SEO value from old pages
*   **User Experience:** Redirects prevent broken links and improve navigation
*   **Search Engine Crawling:** Clear redirect paths help search engines understand site structure
*   **Local SEO:** Preserve local business citations and directory listings
*   **Analytics Continuity:** Maintain tracking of user journeys and conversion paths

### Monitoring and Maintenance

*   **Regular 404 Monitoring:** Check for new broken links after redirect implementation
*   **Search Console Updates:** Monitor redirect performance in Google Search Console
*   **User Feedback:** Track user complaints about broken links or navigation issues
*   **Performance Impact:** Ensure redirects don't significantly impact page load times