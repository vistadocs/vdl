---
consolidated_title: "vhic release notes"
app_code: VHIC
doc_type: release-note
master_source: "VHIC 4.2.0.6 Release Notes"
master_pub_date: February 2014
consolidated_from: 4 versions
prior_versions:
  - "VHIC 4.5 Release Notes"
  - "VHIC 4.6 Release Notes"
  - "VHIC 4.7 Release Notes"
---

<!-- image -->

**Veteran Health Identification Card (VHIC)**

# Release Notes

## VHIC 4.2.0.6

# February 2014

Department of Veterans Affairs Office of Enterprise Development

## Preface

#### Purpose of the Release Notes

The Release Notes document describes the enhancements and/or defects addressed in VHIC 4.2.0.6.

#### Reference Numbering System

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2.

This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

## Contents

1. OVERVIEW	4
2. DEFECT FIXES WITH REMEDY TICKETS	4
    - 2.1. INC000000903802 - VETERAN ADDRESS DOES NOT MATCH ESR VISTA AFTER 48 HOURS. 4
    - 2.2. INC000000903985 - VHIC REQUEST FILE SHOULD BE SENT TO THE CARD PRINT VENDOR DAILY	5
    - 2.3. INC000000924560 - THE TOTALS REPORTED UNDER VHIC REPORTS DOES NOT SEEM TO BE RIGHT	5
    - 2.4. INC000000930579 - THE INFORMATION IN VHIC REPORTS IS NOT CORRECT	5
    - 2.5. INC000000931627 - A SINGLE FACILITY OR THE WHOLE VISN FOR CARD REQUEST, THE SITE LINKS WILL NOT OPEN	5
    - 2.6. INC000000936582- SITES REPORT AN ERROR STATING THE VETERAN IS NOT ELIGIBLE FOR A VIC	6
    - 2.7. INC000000944333 - THE STANDARD BAR CODE APPS FOR PHONES ARE ABLE TO PULL THE FULL SOCIAL SECURITY NUMBER OFF OF THE VETERAN ID CARDS	6
3. ENHANCEMENTS	6
    - 3.1. ON-SCREEN GUIDANCE TO SUPPORT THE END-USER WHEN CAPTURING THE VETERAN IMAGE	6
    - 3.2. IMPROVED ONLINE HELP	7
    - 3.3. ABILITY TO DESIGNATE THE VETERAN BRANCH OF SERVICE ON THE PHYSICAL CARD . 8 3.4.   ADDITIONAL STATUS REPORTS	9
        - 3.4.1. Card Status Report	9
        - 3.4.2. Cards Printed Without EDIPI	11
        - 3.4.3. Card Issued Multiple Times	11

3.	RELATED DOCUMENTS	12

### Overview

The 4.2 Release of the Veterans Health Identification Card (VHIC) web application addresses a number of issues that were discovered after the national rollout in September 2013 as outlined below:

- Improved ability to meet industry standards relevant to identification cards
- Removal of the Social Security Number (SSN) from the card to eliminate identity risk
- Allow clinical applications to support positive patient identification with the card
- On-screen guidance for improved photo capture to support the end-user when capturing the Veteran image
- Improved reliability surrounding the Veteran in-person proofing process
- Hover-Over help text providing more specific user guidance for the application screens
- Ability to designate the Veteran Branch of Service on the physical card
- Addition of the following status reports necessary for supporting local, regional, and VHIC program operations:

1. Card Status - Card Status Report
2. Card Status - Print Release Status Report
3. Cards Printed without EDIPI
4. Card Issued Multiple Times - Summary Report
5. Card Issued Multiple Times - Detail Report

### Defect Fixes with Remedy Tickets

#### INC000000903802 - Veteran address does not match ESR Vista after 48 hours.

#### Issue

When a VHIC Associate processed a card request for a Veteran, VHIC may retrieve incorrect information from the Enrollment system by using an inactive correlated identifier found in the Master Veteran Index (MVI).

#### Solution

When VHIC gets correlated identifiers from MVI, only active (A) records will be included in the response. Including the passive identifiers affects picking the right correlation data out of MVI, affecting address verification through the ESR.

#### INC000000903985 - VHIC request file should be sent to the Card Print Vendor daily.

#### Issue

After national rollout in September 2013, the card requests were accumulated, yet halted production of the cards until this release. The card request file was not sent to the Print Vendor.

#### Solution

The VHIC card request file will be sent to the Print Vendor after VHIC 4.2.0.6 release.

#### INC000000924560 - The totals reported under VHIC reports does not seem to be right.

#### Issue

The totals reported under VHIC reports are not accurate.

#### Solution

Report performance improved and report content/layout updated per Business requirements to include additional information.

#### INC000000930579 - The information in VHIC reports is not correct.

#### Issue

Report information is not accurate.

#### Solution

Report performance improved and report content/layout updated per Business requirements to include additional information.

#### INC000000931627 - A single facility or the whole VISN for Card Request, the site links will not open.

#### Issue

When the user selects a single facility or the whole VISN for card request, the site links will not open.

#### Solution

Report performance improved and report content/layout updated per Business requirements to include additional information.

#### INC000000936582 - Sites report an error stating the Veteran is not eligible for a VIC.

#### Issue

The user reports getting an error stating the Veteran is not eligible for a VIC.

#### Solution

When VHIC gets correlated identifiers from MVI, only active (A) records are included in the response.

Including the passive identifiers affects picking the right correlation data out of MVI, affecting eligibility verification through ESR.

#### INC000000944333 - The standard bar code apps for phones are able to pull the full SSN off the Veteran ID cards.

#### Issue

The standard bar code applications for phones are able to pull the full SSN off the Veteran ID cards.

#### Solution

The SSN is removed from the barcode.

### Enhancements

The following section is an overview of the enhancements for VHIC users that have been added in the VHIC 4.2.0.6 release.

#### On-screen guidance to support the end-user when capturing the Veteran image

#### Issue

The Veteran photo must meet VA photo requirements.

#### Solution

On-screen guidance for capturing photo improves the photo quality and lets the user know what photo requirements must be met.

<!-- image -->

#### Improved Online Help

#### Issue

The system shall support improved online and context-sensitive help.

#### Solution

The VHIC application provides context-sensitive help to assist the user throughout the issuance of the card request.

Please see the context-sensitive help example below.

<!-- image -->

#### Ability to Designate the Veteran Branch of Service on the Physical Card

#### Issue

Provide Card Vendor with military branch of service information to be displayed on the face of the VHIC card.

#### Solution

- The military branch of service (BOS) information is retrieved from the ESR to be displayed in the VHIC application.
- If multiple BOSs are available, the VHIC User has to verify with the Veteran which BOS should be displayed on the face of the card.
- The VHIC application passes the BOS to the Print Vendor.
- The Veteran has the option to decline displaying the military BOS on the VHIC card.

REDACTED

#### Additional Status Reports

#### Issue

Leverage existing report capabilities to support local, regional, and VHIC Program operations.

#### Solution

The reports listed below are added to measure usage, effectiveness, and other aspects of VHIC application.

#### Card Status Report

The Card Status - Status Report is provided for four card/card request statuses listed below.

| **Status**   | **Status Description**                             |
|--------------|----------------------------------------------------|
| Active       | The card is active.                                |
| Inactive     | The card is deactivated.                           |
| Processing   | The Print Facility is processing the card request. |
| Request      | The card is sent to the print facility.            |

<!-- image -->

The Card Status - Print Release Status report is provided for the nine card request statuses listed below.

#### Status Code/Reason Code Description

| **Release Status**   | **Release Status Description**                     |
|----------------------|----------------------------------------------------|
| Cancelled            | Request is cancelled                               |
| Error                | Request error: data integrity                      |
| Hold                 | Request is on-hold                                 |
| Ineligible           | Request ineligible for card; phone and data stored |
| Mailed               | Request processed, card has been mailed            |
| Printing             | Card Print Site prints the card                    |
| Received             | Request has been received by Card Print Site       |
| Rejected             | Request rejected by Card Print Site                |
| Sent                 | Request has been sent to Card Print Site           |

<!-- image -->

#### Cards Printed without EDIPI

The Card Printed without EDIPI report shall provide the actual card count of VHIC cards issued to Veterans without an EDIPI populated on the card within the selected date range.

<!-- image -->

#### Card Issued Multiple Times

- Summary Report
- Detail Report

This report provides information on cards that have been requested on more than one occasion for the same Veteran. The user can specify the maximum of Card Requests to search for. The results returned will be equal to or greater than the maximum of Card Requests entered.

<!-- image -->

Summary Report summarizes information by VISN/Facility. Detailed Report provides detailed Veteran information.

### Related Documents

The [VA software Documentation Library (VDL) website](http://www.va.gov/vdl/application.asp?appid=140) will contain the VHIC 4.2.0.6 Release Notes and the updated VHIC User Guide. This website is usually updated within 1–3 days of the patch release date.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VHIC 4.5 Release Notes

### Card Deactivation

#### Issue

The VHIC Business desired the ability to have Administrators deactivate a Veteran’s cards from within the VHIC Application.

Sol **ution**

- The VHIC system has been modified to allow the VHIC Administrator to change the card status to “deactivated.” (The MVI record will be unlinked, and the image will be retained in the VHIC system.)

- The VHIC system displays the option to deactivate a card as a third tab to the VHIC user.
- The VHIC system displays the deactivation functionality as a Utility Card Administrative Function.
- Users must enter in a deactivation reason during the process. This reason is recorded by the VHIC system.

### Report Enhancements

#### Issue

The VHIC Business requested a number of changes to the Veteran Report and Card History Report within the VHIC application.

#### Solution

The VHIC Application has been modified based on the agreed upon changes.

- The Card History Report has been enhanced with new fields, more descriptive data and improved labels
- The Veteran Report has been enhanced with new fields, more descriptive data and improved labels

### Card Request Enhancement

#### Issue

The VHIC System allows the clerk to choose between multiple possible addresses when determining where to mail a Veteran’s card. In prior releases, the clerk could select Facility, which was determined by the VHIC clerk's location. A new Preferred Facility choice has been added which is determined from the Veterans' record in Enrollment System.

#### Solution

Users will be able to select to mail the card to the Veteran’s preferred facility (as dictated by Enrollment Services).

### User Guide Reorganization

#### Issue

The VHIC User Guide is a very long and complex document. It can be difficult to find the desired content.

#### Solution

The User Guide has been restructured into three volumes for clarity and ease of distribution.

- VHIC 4.5 Volume 1 - Card Requests and Card Deactivations
- VHIC 4.5 Volume 2 - Reports
- VHIC 4.5 Volume 3 - Troubleshooting

### From: VHIC 4.7 Release Notes

## VHIC 4.7

**Release Notes**

<!-- image -->

**September 2016 Department of Veterans Affairs**

**Office of Information and Technology (OI&amp;T)**

**Table of Contents**

1. Introduction	1
2. Purpose	1
3. Audience	1
4. This Release	1
    - 4.1. New Features and Functions Added	1
    - 4.2. Enhancements and Modifications to Existing	1
    - 4.3. Known Issues	1
5. Product Documentation	2

## Introduction

VA provides the Veterans Health Identification Card (VHIC) to eligible Veterans for use at VA medical facilities. The VHIC currently displays the Veteran’s name, picture, and special eligibility indicators, such as Service Connection, Purple Heart, Medal of Honor, and Former Prisoner of War (POW) on the front of the card. After a Veteran’s identity is verified in person, a Veteran who is eligible for VA medical benefits can request the card. After the Veteran has had their picture taken or uploaded at the VA medical facility, and after eligibility is verified, the card request is completed and sent to the print vendor. The card is then mailed to the Veteran and should be received within ten (10) days. If the USPS cannot deliver the card, it is returned to the VA Preferred Facility of the Veteran.

## Purpose

These release notes cover the changes to VHIC for release 4.7.

## Audience

This document targets users and administrators of VHIC and applies to the changes made between this release and any previous release for this software.

## This Release

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for VHIC 4.7.

### New Features and Functions Added

The following are the new features and functions added to the VHIC 4.7 release.

- A new report with dynamic reason selection has been created to show the number of VHICs on hold. It will enable facilities to drill down and identify issues/progress/reasons. It will be available to supervisor and associates, limited to their facility.

### Enhancements and Modifications to Existing

The following are the enhancements and modifications to the VHIC 4.7 release.

- Improvements to report functionality

- A national summary total is now included on all national level reports.

- When copying the Integration Control Number (ICN) from the Master Veteran Index (MVI) Toolkit Identity Proofing (IP) application into the VHIC application to search for the Veteran, an unreadable space is copied over. The VHIC application now trims the ICN field on Step 1 of the Card Request Process so that the VHIC user does not have to physically perform a backspace or delete spaces.

- Ability to monitor service calls
### Known Issues

- The VHIC system now logs the metrics of each service call received by the Card Picture Service and Card Detail Service.

No known issues.

## Product Documentation

The following documents apply to this release:

The [VA software Documentation Library (VDL) website](http://www.va.gov/vdl/application.asp?appid=140) will contain the VHIC 4.7 Release Notes and the updated VHIC User Guides (Volume 1 – Card Requests, Volume 2 – Reports, Volume 3 – Card Deactivations, Volume 4 – Troubleshooting).

This website is usually updated within 1–3 days of the patch release date.

**Template Revision History**

| **Date**      |   **Version** | **Description**   | **Author**                             |
|---------------|---------------|-------------------|----------------------------------------|
| November 2015 |             1 | Initial draft     | OI&T Documentation Standards Committee |

### From: VHIC 4.6 Release Notes

### New Features and Functions Added

The following are the new features and functions added to the VHIC 4.6 release.

- Decouples VHIC from the Access Services (AcS) Identity Proofing (IP) solution.
- Any required Veteran proofing activities will occur in the Master Veteran Index. (MVI) Toolkit application prior to starting the card request process in the VHIC application.

- AcS IP is being sunset in March 2016.

- Provides better support for consuming applications that swipe / scan VHICs. Many applications only support a single identifier per Veteran and are unable to retrieve Veteran data if the card scanned is not the card the system has used as the identifier.

### Enhancements and Modifications to Existing

The following are the enhancements and modifications to the VHIC 4.6 release.

- Streamlined the card issuance process now that identity proofing activities must occur prior to card request.

- Created a new VHIC Print Service Batch Error Summary Report Query Screen.
- Made minor adjustments to a number of other reports as requested by the VHIC Business Office.

### Known Issues

No known issues.
