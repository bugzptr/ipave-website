

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
│   │   └── style.css          # Main stylesheet
│   ├── 📂 fonts/
│   │   └── (font files .woff2) # Self-hosted web fonts
│   └── 📂 images/
│       └── (logos, photos)    # Site imagery and assets
│
├── index.html                 # Homepage
└── (about.html, etc.)         # Additional static pages
```
*(Note: As of this version, the project is a single-page proof-of-concept. Reusable partials will be implemented as the site is built out.)*

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

## Important Considerations

### Contact Forms

*   The contact and footer forms are static HTML elements.
*   They submit to **Formspree** to process the data and send an email notification.
*   The `action` attribute of each `<form>` tag must be set to the correct Formspree endpoint URL.

### Asset Management

*   **Images:** Place all images in the `/assets/images/` folder. Use descriptive filenames (e.g., `residential-driveway-paving.jpg`). Use SVGs for logos and icons whenever possible.
*   **Fonts:** All fonts are self-hosted in `/assets/fonts/`. Ensure you have the correct `.woff2` files for any new font styles or weights.