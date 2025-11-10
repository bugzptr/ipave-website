# StaticForms Testing Guide

## Overview
All forms on the site have been migrated from Formspree to StaticForms. This guide will help you verify everything is working correctly.

## StaticForms Configuration

**API Endpoint:** `https://api.staticforms.dev/submit`
**API Key:** `sf_21a1k3bflhbdnf58nh87n7m3`
**Redirect URL:** `https://ipave4u.co.nz/thank-you.html`
**Reply-To:** Uses sender's email address (`@email`)

**Important:** The recipient email address is configured in your StaticForms dashboard account settings, not in the HTML. For testing, configure `dave@intellinet.co.nz` in your StaticForms dashboard.

## Forms Updated (26 forms total)

### Pages with 2 Forms Each (Hero + Footer):
1. ✅ `index.html` - Homepage
2. ✅ `about.html` - About page
3. ✅ `our-process.html` - Process page
4. ✅ `concrete-patio.html` - Concrete patio page
5. ✅ `services/index.html` - Services overview
6. ✅ `services/residential-driveways.html`
7. ✅ `services/commercial-paving.html`
8. ✅ `services/concrete-repair.html`
9. ✅ `services/decorative-concrete.html`
10. ✅ `services/kerbing-services.html`
11. ✅ `contact/index.html` - Contact page

### Pages with 1 Form Each (Footer only):
12. ✅ `gallery/index.html`
13. ✅ `projects/index.html`
14. ✅ `team/index.html`

## Form Configuration

Each form includes:
- **Action:** `https://api.staticforms.dev/submit`
- **Method:** `POST`
- **Hidden Fields:**
  - `apiKey`: `sf_21a1k3bflhbdnf58nh87n7m3`
  - `redirectTo`: `https://ipave4u.co.nz/thank-you.html`
  - `replyTo`: `@email` (uses sender's email as reply-to)

## Testing Checklist

### 1. StaticForms Dashboard Setup
**CRITICAL:** Configure recipient email in StaticForms dashboard:
- [ ] Log into StaticForms dashboard
- [ ] Find form with API key `sf_21a1k3bflhbdnf58nh87n7m3`
- [ ] Set recipient email to `dave@intellinet.co.nz` (for testing)
- [ ] Save settings

### 2. Form Configuration Check
For each form, verify:
- [ ] Form action is `https://api.staticforms.dev/submit`
- [ ] Hidden field `apiKey` with value `sf_21a1k3bflhbdnf58nh87n7m3` is present
- [ ] Hidden field `redirectTo` with value `https://ipave4u.co.nz/thank-you.html` is present
- [ ] Hidden field `replyTo` with value `@email` is present
- [ ] Form method is `POST`

### 3. Form Submission Testing
Test each form type:

**Hero Forms (with phone field):**
- [ ] Homepage hero form
- [ ] About page hero form
- [ ] Our Process hero form
- [ ] Concrete Patio hero form
- [ ] Services overview hero form
- [ ] All 5 service detail page hero forms
- [ ] Contact page main form

**Footer Forms (simpler):**
- [ ] All 14 footer forms across all pages

**Test Each Form:**
1. Fill out all required fields
2. Submit the form
3. Verify redirect to `https://ipave4u.co.nz/thank-you.html`
4. Check email inbox (dave@intellinet.co.nz) for submission
5. Verify all form fields are included in email
6. Verify reply-to address is the sender's email

### 4. Thank-You Page Testing
- [ ] Page loads correctly at `/thank-you.html`
- [ ] Page has `noindex, nofollow` meta tag (not indexed by search engines)
- [ ] "Return to Homepage" button works
- [ ] Phone number link works
- [ ] Page displays correctly on mobile

### 5. Error Handling
Test error scenarios:
- [ ] Submit form with empty required fields (should show browser validation)
- [ ] Submit form with invalid email format (should show browser validation)
- [ ] Test with JavaScript disabled (form should still work)
- [ ] Test with invalid API key (should show error)

### 6. StaticForms Dashboard
Check StaticForms dashboard:
- [ ] Log into StaticForms account
- [ ] Verify form submissions are being received
- [ ] Check email notifications are working
- [ ] Verify recipient email is set to `dave@intellinet.co.nz` (for testing)
- [ ] Verify spam filtering is configured (if needed)

## Form Field Mapping

**Hero Forms Include:**
- `name` (required)
- `email` (required)
- `phone` (optional)
- `message` (required)

**Footer Forms Include:**
- `name` (required)
- `email` (required)
- `message` (required)

## Common Issues & Solutions

### Forms Not Submitting
1. **Check API Key:** Verify `sf_21a1k3bflhbdnf58nh87n7m3` is correct
2. **Check API Endpoint:** Should be `https://api.staticforms.dev/submit` (not `.xyz`)
3. **Check StaticForms Dashboard:** Ensure form is active and recipient email is configured
4. **Check Browser Console:** Look for JavaScript errors
5. **Verify Email:** Check spam folder for submissions

### Not Redirecting to Thank-You Page
1. **Check Redirect URL:** Should be `https://ipave4u.co.nz/thank-you.html`
2. **Verify Domain:** Ensure domain is live and accessible
3. **Check StaticForms Settings:** Verify redirect is enabled

### Email Not Received
1. **Check StaticForms Dashboard:** Verify recipient email is configured correctly
2. **Check Spam Folder:** Emails may be filtered
3. **Verify Email Address:** Should be dave@intellinet.co.nz (for testing)
4. **Check StaticForms Limits:** Free tier has 500 emails/month limit
5. **Verify API Key:** Ensure API key matches dashboard

### Wrong Recipient Email
- **Solution:** Update recipient email in StaticForms dashboard (not in HTML)
- The recipient email is configured in your StaticForms account settings
- HTML only controls reply-to address (uses sender's email)

## Post-Migration Tasks

- [ ] Configure recipient email in StaticForms dashboard (dave@intellinet.co.nz for testing)
- [ ] Test all 26 forms
- [ ] Verify email notifications
- [ ] Update StaticForms spam filters if needed
- [ ] Monitor form submissions for first week
- [ ] After testing, update recipient email to admin@ipave.co.nz in dashboard

## StaticForms Documentation

- Official Docs: https://www.staticforms.xyz/
- API Reference: https://www.staticforms.xyz/docs
- Support: Check StaticForms dashboard for support options

## Notes

- **Recipient Email:** Configured in StaticForms dashboard, not in HTML
- **Reply-To:** Uses sender's email address automatically (`@email`)
- Thank-you page is set to `noindex, nofollow` - will not appear in search results
- All forms redirect to same thank-you page
- StaticForms free tier includes 500 emails/month
- API endpoint is `api.staticforms.dev` (not `.xyz`)

---

**Migration Date:** 2025-01-10
**API Key:** sf_21a1k3bflhbdnf58nh87n7m3
**Status:** ✅ All forms migrated to correct API configuration

## Testing Checklist

### 1. Form Configuration Check
For each form, verify:
- [ ] Form action is `https://api.staticforms.xyz/submit`
- [ ] Hidden field `accessKey` with value `sf_21a1k3bflhbdnf58nh87n7m3` is present
- [ ] Hidden field `redirectTo` with value `https://ipave4u.co.nz/thank-you.html` is present
- [ ] Form method is `POST`

### 2. Form Submission Testing
Test each form type:

**Hero Forms (with phone field):**
- [ ] Homepage hero form
- [ ] About page hero form
- [ ] Our Process hero form
- [ ] Concrete Patio hero form
- [ ] Services overview hero form
- [ ] All 5 service detail page hero forms
- [ ] Contact page main form

**Footer Forms (simpler):**
- [ ] All 14 footer forms across all pages

**Test Each Form:**
1. Fill out all required fields
2. Submit the form
3. Verify redirect to `https://ipave4u.co.nz/thank-you.html`
4. Check email inbox (admin@ipave.co.nz) for submission
5. Verify all form fields are included in email

### 3. Thank-You Page Testing
- [ ] Page loads correctly at `/thank-you.html`
- [ ] Page has `noindex, nofollow` meta tag (not indexed by search engines)
- [ ] "Return to Homepage" button works
- [ ] Phone number link works
- [ ] Page displays correctly on mobile

### 4. Error Handling
Test error scenarios:
- [ ] Submit form with empty required fields (should show browser validation)
- [ ] Submit form with invalid email format (should show browser validation)
- [ ] Test with JavaScript disabled (form should still work)

### 5. StaticForms Dashboard
Check StaticForms dashboard:
- [ ] Log into StaticForms account
- [ ] Verify form submissions are being received
- [ ] Check email notifications are working
- [ ] Verify spam filtering is configured (if needed)

## Form Field Mapping

**Hero Forms Include:**
- `name` (required)
- `email` (required)
- `phone` (optional)
- `message` (required)

**Footer Forms Include:**
- `name` (required)
- `email` (required)
- `message` (required)

## Common Issues & Solutions

### Forms Not Submitting
1. **Check Access Key:** Verify `sf_21a1k3bflhbdnf58nh87n7m3` is correct
2. **Check StaticForms Dashboard:** Ensure form is active
3. **Check Browser Console:** Look for JavaScript errors
4. **Verify Email:** Check spam folder for submissions

### Not Redirecting to Thank-You Page
1. **Check Redirect URL:** Should be `https://ipave4u.co.nz/thank-you.html`
2. **Verify Domain:** Ensure domain is live and accessible
3. **Check StaticForms Settings:** Verify redirect is enabled in dashboard

### Email Not Received
1. **Check StaticForms Dashboard:** Verify email is configured
2. **Check Spam Folder:** Emails may be filtered
3. **Verify Email Address:** Should be admin@ipave.co.nz
4. **Check StaticForms Limits:** Free tier has submission limits

## Post-Migration Tasks

- [ ] Test all 26 forms
- [ ] Verify email notifications
- [ ] Update StaticForms spam filters if needed
- [ ] Monitor form submissions for first week
- [ ] Remove old Formspree account (optional)

## StaticForms Documentation

- Official Docs: https://www.staticforms.xyz/
- API Reference: https://www.staticforms.xyz/docs
- Support: Check StaticForms dashboard for support options

## Notes

- Thank-you page is set to `noindex, nofollow` - will not appear in search results
- All forms redirect to same thank-you page
- Form submissions are sent to admin@ipave.co.nz
- StaticForms free tier includes spam protection

---

**Migration Date:** 2025-01-10
**Access Key:** sf_21a1k3bflhbdnf58nh87n7m3
**Status:** ✅ All forms migrated

