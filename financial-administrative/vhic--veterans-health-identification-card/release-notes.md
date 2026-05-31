---
title: VHIC 4.2.0.6 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: VHIC
app_name: Veterans Health Identification Card
section: FIN
app_status: archive
pkg_ns: VHIC
patch_ver: 4.2.0
patch_id: VHIC*4.2.0
group_key: VHIC:VHIC:4.2.0
file_numbers: []
security_keys: []
menu_options: 4
description: '''> The 4.2 Release of the Veterans Health Identification Card (VHIC) web application addresses a number of issues that were discovered after the national rollout in September 2013 as outlined below: - Improved ability to meet industry standards relevant to identification cards - Removal of the Social'''
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 1437
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: February 2014
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_2_0_6_release_notes.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_2_0_6_release_notes.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=274
audit_applied: '2026-05-31'
master_source: VHIC 4.2.0.6 Release Notes
master_pub_date: February 2014
consolidated_from: 4 versions
prior_versions:
- VHIC 4.5 Release Notes
- VHIC 4.6 Release Notes
- VHIC 4.7 Release Notes
consolidated_title: vhic release notes
---

> ![](vhic-4-2-0-6-release-notes/001.png)

> Veteran Health Identification Card (VHIC)

> Release Notes

# VHIC 4.2.0.6


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VHIC 4.2.0.6](#vhic-4206)
- [Preface](#preface)
- [Contents](#contents)
  - [Overview](#overview)
  - [Defect Fixes with Remedy Tickets](#defect-fixes-with-remedy-tickets)
    - [INC000000903802 - Veteran address does not match ESR Vista after 48 hours.](#inc000000903802-veteran-address-does-not-match-esr-vista-after-48-hours)
    - [INC000000903985 - VHIC request file should be sent to the Card Print Vendor daily.](#inc000000903985-vhic-request-file-should-be-sent-to-the-card-print-vendor-daily)
    - [INC000000924560 - The totals reported under VHIC reports does not seem to be right.](#inc000000924560-the-totals-reported-under-vhic-reports-does-not-seem-to-be-right)
    - [INC000000930579 - The information in VHIC reports is not correct.](#inc000000930579-the-information-in-vhic-reports-is-not-correct)
    - [INC000000931627 - A single facility or the whole VISN for Card Request, the site links will not open.](#inc000000931627-a-single-facility-or-the-whole-visn-for-card-request-the-site-links-will-not-open)
    - [INC000000936582 - Sites report an error stating the Veteran is not eligible for a VIC.](#inc000000936582-sites-report-an-error-stating-the-veteran-is-not-eligible-for-a-vic)
    - [INC000000944333 - The standard bar code apps for phones are able to pull the full SSN off the Veteran ID cards.](#inc000000944333-the-standard-bar-code-apps-for-phones-are-able-to-pull-the-full-ssn-off-the-veteran-id-cards)
  - [Enhancements](#enhancements)
    - [On-screen guidance to support the end-user when capturing the Veteran image](#on-screen-guidance-to-support-the-end-user-when-capturing-the-veteran-image)
    - [Improved Online Help](#improved-online-help)
    - [Ability to Designate the Veteran Branch of Service on the Physical Card](#ability-to-designate-the-veteran-branch-of-service-on-the-physical-card)
    - [Additional Status Reports](#additional-status-reports)
  - [Related Documents](#related-documents)
February 2014
> Department of Veterans Affairs Office of Enterprise Development

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Purpose of the Release Notes

> The Release Notes document describes the enhancements and/or defects addressed in VHIC 4.2.0.6.

#### Reference Numbering System

> This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2.

> This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [OVERVIEW 4](#overview)
2.  [DEFECT FIXES WITH REMEDY TICKETS 4](#defect-fixes-with-remedy-tickets)
    1.  [INC000000903802 - VETERAN ADDRESS DOES NOT MATCH ESR VISTA AFTER 48 HOURS. 4](#inc000000903802---veteran-address-does-not-match-esr-vista-after-48-hours.)
    2.  [INC000000903985 - VHIC REQUEST FILE SHOULD BE SENT TO THE CARD PRINT VENDOR DAILY 5](#inc000000903985---vhic-request-file-should-be-sent-to-the-card-print-vendor-daily.)
    3.  [INC000000924560 - THE TOTALS REPORTED UNDER VHIC REPORTS DOES NOT SEEM TO BE RIGHT 5](#inc000000924560---the-totals-reported-under-vhic-reports-does-not-seem-to-be-right.)
    4.  [INC000000930579 - THE INFORMATION IN VHIC REPORTS IS NOT CORRECT 5](#inc000000930579---the-information-in-vhic-reports-is-not-correct.)
    5.  [INC000000931627 - A SINGLE FACILITY OR THE WHOLE VISN FOR CARD REQUEST, THE SITE LINKS WILL NOT OPEN 5](#inc000000931627---a-single-facility-or-the-whole-visn-for-card-request-the-site-links-will-not-open.)
    6.  [INC000000936582- SITES REPORT AN ERROR STATING THE VETERAN IS NOT ELIGIBLE FOR A VIC 6](#inc000000936582---sites-report-an-error-stating-the-veteran-is-not-eligible-for-a-vic.)
    7.  [INC000000944333 - THE STANDARD BAR CODE APPS FOR PHONES ARE ABLE TO PULL THE FULL SOCIAL SECURITY NUMBER OFF OF THE VETERAN ID CARDS 6](#inc000000944333---the-standard-bar-code-apps-for-phones-are-able-to-pull-the-full-ssn-off-the-veteran-id-cards.)
3.  [ENHANCEMENTS 6](#enhancements)
    1.  [ON-SCREEN GUIDANCE TO SUPPORT THE END-USER WHEN CAPTURING THE VETERAN IMAGE 6](#on-screen-guidance-to-support-the-end-user-when-capturing-the-veteran-image)
    2.  [IMPROVED ONLINE HELP 7](#improved-online-help)
    3.  [ABILITY TO DESIGNATE THE VETERAN BRANCH OF SERVICE ON THE PHYSICAL CARD . 8](#ability-to-designate-the-veteran-branch-of-service-on-the-physical-card) [3.4. ADDITIONAL STATUS REPORTS 9](#additional-status-reports)
        1.  [Card Status Report 9](#card-status-report)
        2.  [Cards Printed Without EDIPI 11](#cards-printed-without-edipi)
        3.  [Card Issued Multiple Times 11](#card-issued-multiple-times)
[3. RELATED DOCUMENTS 12](#related-documents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The 4.2 Release of the Veterans Health Identification Card (VHIC) web application addresses a number of issues that were discovered after the national rollout in September 2013 as outlined below:
- Improved ability to meet industry standards relevant to identification cards
- Removal of the Social Security Number (SSN) from the card to eliminate identity risk
- Allow clinical applications to support positive patient identification with the card
- On-screen guidance for improved photo capture to support the end-user when capturing the Veteran image
- Improved reliability surrounding the Veteran in-person proofing process
- Hover-Over help text providing more specific user guidance for the application screens
- Ability to designate the Veteran Branch of Service on the physical card
- Addition of the following status reports necessary for supporting local, regional, and VHIC program operations:
1.  Card Status - Card Status Report
2.  Card Status - Print Release Status Report
3.  Cards Printed without EDIPI
4.  Card Issued Multiple Times - Summary Report
5.  Card Issued Multiple Times - Detail Report

## Defect Fixes with Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### INC000000903802 - Veteran address does not match ESR Vista after 48 hours.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> When a VHIC Associate processed a card request for a Veteran, VHIC may retrieve incorrect information from the Enrollment system by using an inactive correlated identifier found in the Master Veteran Index (MVI).

#### Solution

> When VHIC gets correlated identifiers from MVI, only active (A) records will be included in the response. Including the passive identifiers affects picking the right correlation data out of MVI, affecting address verification through the ESR.

### INC000000903985 - VHIC request file should be sent to the Card Print Vendor daily.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> After national rollout in September 2013, the card requests were accumulated, yet halted production of the cards until this release. The card request file was not sent to the Print Vendor.

#### Solution

> The VHIC card request file will be sent to the Print Vendor after VHIC 4.2.0.6 release.

### INC000000924560 - The totals reported under VHIC reports does not seem to be right.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> The totals reported under VHIC reports are not accurate.

#### Solution

> Report performance improved and report content/layout updated per Business requirements to include additional information.

### INC000000930579 - The information in VHIC reports is not correct.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> Report information is not accurate.

#### Solution

> Report performance improved and report content/layout updated per Business requirements to include additional information.

### INC000000931627 - A single facility or the whole VISN for Card Request, the site links will not open.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> When the user selects a single facility or the whole VISN for card request, the site links will not open.

#### Solution

> Report performance improved and report content/layout updated per Business requirements to include additional information.

### INC000000936582 - Sites report an error stating the Veteran is not eligible for a VIC.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> The user reports getting an error stating the Veteran is not eligible for a VIC.

#### Solution

> When VHIC gets correlated identifiers from MVI, only active (A) records are included in the response.
> Including the passive identifiers affects picking the right correlation data out of MVI, affecting eligibility verification through ESR.

### INC000000944333 - The standard bar code apps for phones are able to pull the full SSN off the Veteran ID cards.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> The standard bar code applications for phones are able to pull the full SSN off the Veteran ID cards.

#### Solution

> The SSN is removed from the barcode.

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following section is an overview of the enhancements for VHIC users that have been added in the VHIC 4.2.0.6 release.

### On-screen guidance to support the end-user when capturing the Veteran image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> The Veteran photo must meet VA photo requirements.

#### Solution

> On-screen guidance for capturing photo improves the photo quality and lets the user know what photo requirements must be met.
> ![](vhic-4-2-0-6-release-notes/002.png)

### Improved Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> The system shall support improved online and context-sensitive help.

#### Solution

> The VHIC application provides context-sensitive help to assist the user throughout the issuance of the card request.
> Please see the context-sensitive help example below.
> ![](vhic-4-2-0-6-release-notes/003.png)

### Ability to Designate the Veteran Branch of Service on the Physical Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> Provide Card Vendor with military branch of service information to be displayed on the face of the VHIC card.

#### Solution

- The military branch of service (BOS) information is retrieved from the ESR to be displayed in the VHIC application.
- If multiple BOSs are available, the VHIC User has to verify with the Veteran which BOS should be displayed on the face of the card.
- The VHIC application passes the BOS to the Print Vendor.
- The Veteran has the option to decline displaying the military BOS on the VHIC card.
> REDACTED

### Additional Status Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Issue

> Leverage existing report capabilities to support local, regional, and VHIC Program operations.

#### Solution

> The reports listed below are added to measure usage, effectiveness, and other aspects of VHIC application.

#### Card Status Report

> The Card Status - Status Report is provided for four card/card request statuses listed below.
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Status Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active</td>
<td>The card is active.</td>
</tr>
<tr class="even">
<td>Inactive</td>
<td>The card is deactivated.</td>
</tr>
<tr class="odd">
<td>Processing</td>
<td>The Print Facility is processing the card request.</td>
</tr>
<tr class="even">
<td>Request</td>
<td>The card is sent to the print facility.</td>
</tr>
</tbody>
</table>
> ![](vhic-4-2-0-6-release-notes/004.png)
> The Card Status - Print Release Status report is provided for the nine card request statuses listed below.

#### Status Code/Reason Code Description

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Release Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Status Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cancelled</td>
<td><blockquote>
<p>Request is cancelled</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Error</td>
<td><blockquote>
<p>Request error: data integrity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Hold</td>
<td><blockquote>
<p>Request is on-hold</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Ineligible</td>
<td><blockquote>
<p>Request ineligible for card; phone and data stored</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Mailed</td>
<td><blockquote>
<p>Request processed, card has been mailed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Printing</td>
<td><blockquote>
<p>Card Print Site prints the card</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Received</td>
<td><blockquote>
<p>Request has been received by Card Print Site</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Rejected</td>
<td><blockquote>
<p>Request rejected by Card Print Site</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Sent</td>
<td><blockquote>
<p>Request has been sent to Card Print Site</p>
</blockquote></td>
</tr>
</tbody>
</table>
> ![](vhic-4-2-0-6-release-notes/005.png)

#### Cards Printed without EDIPI

> The Card Printed without EDIPI report shall provide the actual card count of VHIC cards issued to Veterans without an EDIPI populated on the card within the selected date range.
![](vhic-4-2-0-6-release-notes/006.png)

#### Card Issued Multiple Times

- Summary Report
- Detail Report
> This report provides information on cards that have been requested on more than one occasion for the same Veteran. The user can specify the maximum of Card Requests to search for. The results returned will be equal to or greater than the maximum of Card Requests entered.
> ![](vhic-4-2-0-6-release-notes/007.png)Summary Report summarizes information by VISN/Facility. Detailed Report provides detailed Veteran information.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The [<u>VA software Documentation Library (VDL) website</u>](http://www.va.gov/vdl/application.asp?appid=140) will contain the VHIC 4.2.0.6 Release Notes and the updated VHIC User Guide. This website is usually updated within 1–3 days of the patch release date.


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VHIC 4.5 Release Notes

## Card Deactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIC Business desired the ability to have Administrators deactivate a Veteran's cards from within the VHIC Application.

> Solution

- The VHIC system has been modified to allow the VHIC Administrator to change the card status to "deactivated." (The MVI record will be unlinked, and the image will be retained in the VHIC system.)
- The VHIC system displays the option to deactivate a card as a third tab to the VHIC user.
- The VHIC system displays the deactivation functionality as a Utility Card Administrative Function.
- Users must enter in a deactivation reason during the process. This reason is recorded by the VHIC system.

## Report Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIC Business requested a number of changes to the Veteran Report and Card History Report within the VHIC application.

### Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIC Application has been modified based on the agreed upon changes.

- The Card History Report has been enhanced with new fields, more descriptive data and improved labels
- The Veteran Report has been enhanced with new fields, more descriptive data and improved labels

## Card Request Enhancement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIC System allows the clerk to choose between multiple possible addresses when determining where to mail a Veteran's card. In prior releases, the clerk could select Facility, which was determined by the VHIC clerk's location. A new Preferred Facility choice has been added which is determined from the Veterans' record in Enrollment System.

### Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users will be able to select to mail the card to the Veteran's preferred facility (as dictated by Enrollment Services).

## User Guide Reorganization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIC User Guide is a very long and complex document. It can be difficult to find the desired content.

### Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The User Guide has been restructured into three volumes for clarity and ease of distribution.

- VHIC 4.5 Volume 1 - Card Requests and Card Deactivations
- VHIC 4.5 Volume 2 - Reports
- VHIC 4.5 Volume 3 - Troubleshooting

### From: VHIC 4.6 Release Notes

### January 2016 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Office of Information and Technology (OI&T)
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the new features and functions added to the VHIC 4.6 release.

- Decouples VHIC from the Access Services (AcS) Identity Proofing (IP) solution.
  - AcS IP is being sunset in March 2016.
  - Any required Veteran proofing activities will occur in the Master Veteran Index. (MVI) Toolkit application prior to starting the card request process in the VHIC application.
- Updates the business logic to limit Veterans to a single active VHIC.
  - Provides better support for consuming applications that swipe / scan VHICs. Many applications only support a single identifier per Veteran and are unable to retrieve Veteran data if the card scanned is not the card the system has used as the identifier.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are the enhancements and modifications to the VHIC 4.6 release.

- <span id="_bookmark6" class="anchor"></span>Streamlined the card issuance process now that identity proofing activities must occur prior to card request.
- Created a new VHIC Print Service Batch Error Summary Report Query Screen.
- Made minor adjustments to a number of other reports as requested by the VHIC Business Office.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No known issues.

### Template Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 45%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>November 2015</td>
<td>1.0</td>
<td>Initial draft</td>
<td><blockquote>
<p>OI&amp;T Documentation Standards Committee</p>
</blockquote></td>
</tr>
</tbody>
</table>
