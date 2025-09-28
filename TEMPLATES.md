# I Pave Concrete & Asphalt - Standardized Templates

This file contains the standardized header and footer templates that must be used on ALL pages to ensure NAP consistency and prevent Google Business Profile suspension issues.

## 📋 NAP Information (DO NOT CHANGE)

**Business Name:** I Pave Concrete & Asphalt  
**Phone:** 0800 472 8348  
**Address:** 335 Kainga Road, Kainga, Christchurch 8083, New Zealand  
**Email:** admin@ipave.co.nz

## 🚨 CRITICAL: NAP Consistency Rules

1. **NEVER** change the business name, phone, address, or email
2. **ALWAYS** use the exact same format shown in these templates
3. **ALWAYS** include the complete NAP in the footer
4. **ALWAYS** use the same phone number format: 0800 472 8348
5. **ALWAYS** use the same address format with line breaks as shown

## 📄 How to Use These Templates

### For New Pages:
1. Copy the header template exactly as shown
2. Copy the footer template exactly as shown
3. Include the NAP CSS styling
4. Update only the page-specific content between header and footer

### For Existing Pages:
1. Replace the existing header with the template header
2. Replace the existing footer with the template footer
3. Ensure NAP CSS is included
4. Verify all NAP information matches exactly

## 🔧 Template Components

### Header Template Features:
- Consistent logo with proper alt text
- Phone number prominently displayed
- Navigation menu with current page links
- Quote button for lead generation

### Footer Template Features:
- Complete NAP information in structured format
- Service links (update as new services are added)
- Contact form for lead generation
- Copyright notice with current year

### CSS Requirements:
- NAP styling for consistent appearance
- Responsive design considerations
- Hover effects for links
- Proper spacing and typography

## 📝 Checklist for New Pages

- [ ] Header copied exactly from template
- [ ] Footer copied exactly from template
- [ ] NAP CSS included
- [ ] Business name: "I Pave Concrete & Asphalt"
- [ ] Phone: "0800 472 8348"
- [ ] Address: "335 Kainga Road, Kainga, Christchurch 8083, New Zealand"
- [ ] Email: "admin@ipave.co.nz"
- [ ] All links work correctly
- [ ] Page title includes business name
- [ ] Meta description includes location keywords

---

<!-- STANDARDIZED HEADER TEMPLATE -->
<!-- Copy this header section to all pages for consistency -->

<header class="site-header">
    <div class="container">
        <div class="header-top">
            <a href="/" class="site-logo">
                <img src="assets/images/logo-horizontal.svg" alt="I Pave Concrete & Asphalt Logo">
                <span class="visually-hidden">I Pave Concrete & Asphalt</span>
            </a>
            <div class="header-phone">
                <a href="tel:08004728348" class="phone-link">0800 472 8348</a>
            </div>
        </div>
        
        <div class="header-bottom">
            <nav class="main-nav" aria-label="Main navigation">
                <ul>
                    <li><a href="/" aria-label="Go to homepage">Home</a></li>
                    <li><a href="#" aria-label="Learn about our process">Our Process</a></li>
                    <li><a href="concrete-patio.html" aria-label="View our concrete patio services">Concrete Patio Christchurch</a></li>
                    <li><a href="#" aria-label="See our projects">Our Projects</a></li>
                    <li><a href="#" aria-label="Read our story">Our Story</a></li>
                </ul>
            </nav>
            <a href="#" class="button-accent header-quote-button">Get a quote</a>
        </div>
    </div>
</header>

<!-- STANDARDIZED FOOTER TEMPLATE -->
<!-- Copy this footer section to all pages for consistency -->

<footer class="site-footer">
    <div class="container footer-grid">
        <div class="footer-contact">
            <img src="assets/images/logo-horizontal.svg" alt="I Pave Concrete & Asphalt Logo" class="footer-logo">
            <h4>Contact Info</h4>
            <div class="nap-info">
                <p><strong>I Pave Concrete & Asphalt</strong></p>
                <p>335 Kainga Road<br>
                Kainga, Christchurch 8083<br>
                New Zealand</p>
                <p>Phone: <a href="tel:08004728348">0800 472 8348</a><br>
                Email: <a href="mailto:admin@ipave.co.nz">admin@ipave.co.nz</a></p>
            </div>
        </div>
        <div class="footer-services">
            <h4>Services</h4>
            <ul>
                <li><a href="concrete-patio.html">Concrete Patio Christchurch</a></li>
                <li><a href="#">Concrete Services</a></li>
                <li><a href="#">Decorative Concrete</a></li>
                <li><a href="#">Kerbing Services</a></li>
                <li><a href="#">Landscape Services</a></li>
            </ul>
        </div>
        <div class="footer-form">
            <h4>Send Us a Message</h4>
            <form action="https://formspree.io/f/xjkodern" method="POST">
                <input type="text" name="name" placeholder="First Name" required>
                <input type="email" name="email" placeholder="Email" required>
                <textarea name="message" placeholder="Tell us about your project" rows="3" required></textarea>
                <button type="submit" class="button-primary">Submit</button>
            </form>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2025 I Pave Concrete & Asphalt. All Rights Reserved.</p>
    </div>
</footer>

<!-- STANDARDIZED NAP CSS STYLING -->
<!-- Include this CSS in all pages for consistent NAP styling -->

<style>
/* NAP (Name, Address, Phone) Styling */
.nap-info { margin-top: 1rem; }
.nap-info p { margin-bottom: 0.5rem; line-height: 1.4; }
.nap-info a { color: var(--color-white); text-decoration: underline; }
.nap-info a:hover { color: var(--color-accent); }
</style>
