# I Pave Concrete - Site Structure Plan
*Based on WordPress Sitemap Analysis*

## 📋 Current WordPress Site Structure

### **Main Pages (High Priority - Must Create)**
- **Homepage** (`/`) - ✅ Already exists
- **About** (`/about/`) - Company information and story
- **Services** (`/services/`) - Services overview page
- **Gallery** (`/gallery/`) - Project portfolio and images
- **Contact** (`/contact/`) - Contact form and information
- **History** (`/history/`) - Company timeline and milestones
- **Leadership** (`/leadership/`) - Management team information
- **Team** (`/team/`) - Staff and team members
- **Projects** (`/projects/`) - Project showcase and case studies
- **Projects-2** (`/projects-2/`) - Additional project gallery

### **E-commerce Pages (Redirect to Lead Generation)**
- **Shop** (`/shop/`) - Redirect to services overview (generate interest)
- **Cart** (`/cart/`) - Redirect to quote request form (capture leads)
- **Checkout** (`/checkout/`) - Redirect to quote request form (capture leads)
- **My Account** (`/my-account/`) - Redirect to contact page (maintain relationship)

---

## 🏗️ New Site Structure Implementation

### **Phase 1: Core Pages (Weeks 1-2)**
```
/ (homepage) ✅ Already exists
/about/ → Company story, history, leadership
/services/ → Services overview with individual service links
/contact/ → Contact form and quote requests
```

### **Phase 2: Content Pages (Weeks 3-4)**
```
/gallery/ → Project portfolio and before/after images
/projects/ → Detailed project case studies
/team/ → Staff profiles and team information
```

### **Phase 3: Service Detail Pages (Weeks 5-6)**
```
/services/residential-driveways.html
/services/commercial-paving.html
/services/concrete-repair.html
/services/decorative-concrete.html
/services/kerbing-services.html
```

---

## 🔀 Redirect Strategy Implementation

### **Priority 1: Core Business Pages**
```
/about/ → /about/index.html (301 redirect)
/services/ → /services/index.html (301 redirect)
/contact/ → /contact/index.html (301 redirect)
```

### **Priority 2: Content Pages**
```
/gallery/ → /gallery/index.html (301 redirect)
/projects/ → /projects/index.html (301 redirect)
/projects-2/ → /projects/index.html (301 redirect)
/team/ → /team/index.html (301 redirect)
```

### **Priority 3: Company Information**
```
/history/ → /about/index.html#history (301 redirect)
/leadership/ → /about/index.html#leadership (301 redirect)
```

### **Priority 4: E-commerce to Lead Generation Redirects**
```
/shop/ → /services/ (301 redirect - showcase services)
/cart/ → /contact/quote-request.html (301 redirect - capture leads)
/checkout/ → /contact/quote-request.html (301 redirect - capture leads)
/my-account/ → /contact/ (301 redirect - maintain relationship)
```

---

## 📁 File Structure for New Site

```
ipave-website/
├── 📂 assets/
│   ├── 📂 css/
│   │   ├── style.css          # Main stylesheet
│   │   ├── components.css     # Reusable components
│   │   └── pages.css          # Page-specific styles
│   ├── 📂 fonts/              # Self-hosted fonts
│   ├── 📂 images/
│   │   ├── logos/             # Logo variations
│   │   ├── services/          # Service imagery
│   │   ├── projects/          # Project photos
│   │   ├── team/              # Team photos
│   │   └── gallery/           # Portfolio images
│   └── 📂 js/
│       ├── navigation.js      # Navigation functionality
│       └── forms.js           # Form handling
│
├── 📂 about/                   # About section
│   ├── index.html             # Company story, history, leadership
│   └── team.html              # Team members (if separate page needed)
│
├── 📂 services/                # Services section
│   ├── index.html             # Services overview
│   ├── residential-driveways.html
│   ├── commercial-paving.html
│   ├── concrete-repair.html
│   ├── decorative-concrete.html
│   └── kerbing-services.html
│
├── 📂 gallery/                 # Portfolio section
│   ├── index.html             # Gallery overview
│   └── projects.html          # Detailed project showcase
│
├── 📂 contact/                 # Contact section
│   ├── index.html             # Contact form
│   └── quote-request.html     # Quote request form
│
├── index.html                  # Homepage ✅
├── robots.txt                  # Search engine directives
├── sitemap.xml                # New site structure
├── _redirects                  # Cloudflare redirects
└── README.md                   # Project documentation
```

---

## 🎯 Content Migration Strategy

### **About Section Content**
- **Company Story**: Merge content from `/about/`, `/history/`, `/leadership/`
- **Team Information**: Consolidate `/team/` content
- **Company Timeline**: Extract from `/history/` page

### **Services Section Content**
- **Services Overview**: Expand `/services/` content
- **Individual Services**: Create detailed pages for each service type
- **Service Benefits**: Extract from existing service descriptions

### **Portfolio Section Content**
- **Gallery**: Consolidate images from `/gallery/`
- **Projects**: Merge content from `/projects/` and `/projects-2/`
- **Case Studies**: Create detailed project showcases

### **Contact Section Content**
- **Contact Form**: Enhance existing contact functionality for general inquiries
- **Quote Request Forms**: Create dedicated, service-specific quote request forms
- **Service Areas**: Include Christchurch and Canterbury coverage
- **Lead Capture**: Multiple touchpoints to capture phone calls and form submissions

---

## 📱 Navigation Structure

### **Main Navigation Menu**
```
Home
About (dropdown)
├── Our Story
├── Company History
├── Leadership
└── Team
Services (dropdown)
├── Overview
├── Residential Driveways
├── Commercial Paving
├── Concrete Repair
├── Decorative Concrete
└── Kerbing Services
Gallery
├── Portfolio
└── Projects
Contact
├── Contact Us
└── Get a Quote
```

### **Footer Navigation**
```
Company
├── About Us
├── Our Team
├── Company History
└── Leadership

Services
├── Residential
├── Commercial
├── Repair
├── Decorative
└── Kerbing

Portfolio
├── Gallery
├── Projects
└── Case Studies

Contact
├── Contact Form
├── Quote Request
└── Service Areas
```

---

## 🚀 Implementation Timeline

### **Week 1-2: Foundation**
- Create directory structure
- Implement redirects file
- Build About section pages
- Update navigation

### **Week 3-4: Content Pages**
- Create Gallery/Portfolio pages
- Build Team page
- Implement contact forms
- Add internal linking

### **Week 5-6: Service Pages**
- Build individual service pages
- Add service-specific content
- Implement cross-linking
- Optimize for SEO

### **Week 7-8: Polish & Launch**
- Content review and optimization
- SEO implementation
- Performance testing
- Launch preparation

---

## 🔍 SEO Considerations

### **URL Structure**
- **Clean URLs**: `/services/residential-driveways/` instead of `/services/residential-driveways.html`
- **Descriptive URLs**: Use service names in URLs
- **Consistent Structure**: Maintain hierarchy across all pages

### **Content Optimization**
- **Unique Content**: Each page should have 800-1200 words minimum
- **Local SEO**: Include Christchurch and Canterbury references
- **Service Keywords**: Target specific service-related keywords
- **Image Optimization**: Use descriptive alt text and file names

### **Internal Linking**
- **Service Cross-links**: Link related services together
- **Portfolio Integration**: Link projects to relevant services
- **CTA Placement**: Strategic call-to-action placement
- **Breadcrumb Navigation**: Implement on all pages

---

## 📊 Success Metrics

### **SEO Performance**
- **PageSpeed Scores**: Maintain 98+ mobile, 100 desktop
- **Core Web Vitals**: Keep CLS at 0, optimize LCP and FID
- **Search Rankings**: Target top 3 positions for local keywords
- **Organic Traffic**: Increase month-over-month

### **User Experience**
- **Navigation**: Intuitive menu structure
- **Content**: Engaging and informative service descriptions
- **Forms**: Easy contact and quote request process
- **Mobile**: Responsive design across all devices

### **Business Goals**
- **Lead Generation**: Maximize phone calls and contact form submissions
- **Service Awareness**: Better showcase of service offerings to generate interest
- **Brand Recognition**: Professional and trustworthy appearance
- **Local Presence**: Strong Christchurch/Canterbury visibility
- **Conversion Focus**: Guide visitors to contact/quote rather than purchase
