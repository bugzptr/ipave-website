# StaticForms Testing Guide

## Overview
All forms on the site have been migrated from Formspree to StaticForms. This guide will help you verify everything is working correctly.

## StaticForms Configuration

**API Endpoint:** `https://api.staticforms.dev/submit`
**API Key:** `sf_21a1k3bflhbdnf58nh87n7m3`
**Redirect URL:** `https://ipave4u.co.nz/thank-you.html`
**Reply-To:** Uses sender's email address (`@email`)

**Recipient Email:** Configured via hidden field `to` with value `dave@intellinet.co.nz` (for testing)

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
  - `to`: `dave@intellinet.co.nz` (recipient email address)

## Testing Checklist

### 1. Form Configuration Check
For each form, verify:
- [ ] Form action is `https://api.staticforms.dev/submit`
- [ ] Hidden field `apiKey` with value `sf_21a1k3bflhbdnf58nh87n7m3` is present
- [ ] Hidden field `redirectTo` with value `https://ipave4u.co.nz/thank-you.html` is present
- [ ] Hidden field `replyTo` with value `@email` is present
- [ ] Hidden field `to` with value `dave@intellinet.co.nz` is present
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
4. Check email inbox (dave@intellinet.co.nz) for submission
5. Verify all form fields are included in email
6. Verify reply-to address is the sender's email

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
- [ ] Test with invalid API key (should show error)

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
1. **Check API Key:** Verify `sf_21a1k3bflhbdnf58nh87n7m3` is correct
2. **Check API Endpoint:** Should be `https://api.staticforms.dev/submit` (not `.xyz`)
3. **Check Recipient Email:** Verify `to` hidden field is present with correct email
4. **Check Browser Console:** Look for JavaScript errors
5. **Verify Email:** Check spam folder for submissions

### Not Redirecting to Thank-You Page
1. **Check Redirect URL:** Should be `https://ipave4u.co.nz/thank-you.html`
2. **Verify Domain:** Ensure domain is live and accessible
3. **Check StaticForms Settings:** Verify redirect is enabled

### Email Not Received
1. **Check Recipient Email:** Verify `to` hidden field has correct email address (`dave@intellinet.co.nz` for testing)
2. **Check Spam Folder:** Emails may be filtered
3. **Verify Email Address:** Should be dave@intellinet.co.nz (for testing)
4. **Check StaticForms Limits:** Free tier has 500 emails/month limit
5. **Verify API Key:** Ensure API key matches dashboard

### Wrong Recipient Email
- **Solution:** Update the `to` hidden field in HTML forms
- Change `<input type="hidden" name="to" value="dave@intellinet.co.nz">` to your desired email
- Reply-to address uses sender's email automatically (`@email`)

## Post-Migration Tasks

- [ ] Test all 26 forms
- [ ] Verify email notifications are received at dave@intellinet.co.nz
- [ ] Update StaticForms spam filters if needed
- [ ] Monitor form submissions for first week
- [ ] After testing, update `to` field in all forms to `admin@ipave.co.nz` for production

## StaticForms Documentation

- Official Docs: https://www.staticforms.xyz/
- API Reference: https://www.staticforms.xyz/docs
- Support: Check StaticForms dashboard for support options

## Notes

- **Recipient Email:** Configured via `to` hidden field in HTML (`dave@intellinet.co.nz` for testing)
- **Reply-To:** Uses sender's email address automatically (`@email`)
- Thank-you page is set to `noindex, nofollow` - will not appear in search results
- All forms redirect to same thank-you page
- StaticForms free tier includes 500 emails/month
- API endpoint is `api.staticforms.dev` (not `.xyz`)

---

**Migration Date:** 2025-01-10
**API Key:** sf_21a1k3bflhbdnf58nh87n7m3
**Status:** ✅ All forms migrated to correct API configuration with recipient email configured in HTML

