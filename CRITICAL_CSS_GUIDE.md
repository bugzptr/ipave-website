# Critical CSS Inlining Guide

## Overview

If `font-display: block` doesn't resolve CLS issues, this guide shows how to inline critical above-the-fold CSS for maximum performance.

## Benefits

- **Eliminates render-blocking CSS** - Critical styles load immediately
- **Prevents layout shifts** - Styles are available before fonts load
- **Faster First Contentful Paint** - No waiting for external CSS
- **Better CLS scores** - Layout is stable from the start

## Implementation Steps

### Option 1: Manual Replacement (Recommended)

1. **Open `index.html`** and locate the `<style>` tag around line 51
2. **Replace the entire `<style>` block** with the contents from `critical-css.html`
3. **Keep the async CSS loading** - The existing line should remain:
   ```html
   <link rel="stylesheet" href="assets/css/style.css" media="print" onload="this.media='all'">
   <noscript><link rel="stylesheet" href="assets/css/style.css"></noscript>
   ```

### Option 2: Using the Provided File

1. Copy the CSS from `critical-css.html` (everything between `<style>` and `</style>`)
2. Paste it into `index.html` replacing the existing inline styles
3. Delete `critical-css.html` after copying (it's just a reference)

## What's Included

The critical CSS includes:

- **Font-face declarations** for critical weights (400, 600, 700)
- **CSS variables** (colors, fonts, spacing)
- **Base reset** (box-sizing, body, img)
- **Header styles** (logo, navigation, phone link)
- **Hero section** (background, overlay, content, form)
- **Responsive breakpoints** (tablet and mobile)

## What's NOT Included (Loads Async)

- Service card styles
- Gallery styles
- Footer styles
- About section styles
- Below-the-fold content styles

These load asynchronously via the external stylesheet, so they don't block rendering.

## Testing

After implementation:

1. **Test visually** - Ensure above-the-fold content renders correctly
2. **Check PageSpeed Insights** - CLS should improve significantly
3. **Verify async loading** - Full stylesheet should load after initial render
4. **Test responsive** - Mobile and tablet views should work correctly

## Performance Impact

Expected improvements:
- **CLS**: Should drop to <0.1 (from current 0.678)
- **FCP**: May improve slightly (no CSS blocking)
- **LCP**: Should remain similar or improve
- **Overall Score**: Should increase to 90+

## Rollback

If issues occur, simply revert to the previous inline CSS in `index.html`. The external stylesheet will continue to work normally.

