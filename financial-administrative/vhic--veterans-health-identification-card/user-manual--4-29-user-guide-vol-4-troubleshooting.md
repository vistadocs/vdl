---
title: VHIC 4.29 User Guide Vol 4 Troubleshooting
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Vol 4 Troubleshooting
app_code: VHIC
app_name: Veterans Health Identification Card
section: FIN
app_status: archive
pkg_ns: VHIC
patch_ver: 4.29
patch_id: VHIC*4.29
group_key: "VHIC:VHIC:4.29"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vhic
  - table
  - contents
  - card
  - request
  - span
  - veteran
  - step
  - hold
  - address
page_count: 0
word_count: 5208
section_count: 15
table_count: 1
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2024
revision_count: 28
revision_newest: 06/18/2222
revision_oldest: 01/06/2015
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v4.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v4.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=274"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Veteran Health Identification Card (VHIC 4.29)

  User Guide
---

![](vhic-4-29-user-guide-vol-4-troubleshooting/001.png)

Volume 4 - Troubleshooting

May 2024

Office of Information and Technology (OI&T)

Revision History

<u>NOTE</u>: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date   | Revision | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Author         |
|------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 05/18/2024 | 11.3         | No functionality changes. Updates to screen shots, VHIC Clerk title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED           |
| 03/27/2024 | 11.2         | No functionality changes. Updates to Date and Version number, formatting and style changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED           |
| 12/14/2023 | 11.1         | No functionality changes. Updates to Date and Version number only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED           |
| 09/18/2023 | 11           | No functionality changes. Updates to help desk number, VHIC card image, bad facility contact information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED           |
| 06/17/2023 | 10           | Updated content, removed information that was duplicated or not relevant to troubleshooting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED           |
| 03/18/2023 | 9.4          | No functionality changes. Date and version number updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED           |
| 12/17/2022 | 9.3          | No functionality changes. Date and version number updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED           |
| 09/18/2022 | 9.2          | No functionality changes. Date and version number updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED           |
| 06/18/2222 | 9.1          | No functionality changes. Date and version number updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED           |
| 04/18/2022 | 9.0          | Updated to reflect VIP 20 Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED           |
| 09/18/2021 | 8.1          | Updated screenshots to remove any appearance of PII per VDL standards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED           |
| 06/20/2021 | 8            | Updated to remove Flash instructions as it is no longer supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED           |
| 03/20/2021 | 7.1          | Updated to remove instances of “Internet Explorer” as Flash is no longer supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED           |
| 12/19/2020 | 7            | Updated to reflect changes in VIP 15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED           |
| 06/20/2020 | 6            | Updated to reflect changes during VIP 13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED           |
| 03/21/2020 | 5            | Updated to reflect changes during VIP 12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED           |
| 11/15/2019 | 4            | Updated to reflect changes to application in VHIC 4.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED           |
| 9/18/2019  | 3            | Updated to reflect OIT Documentation Standards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED           |
| 01/20/2018 | 2.1          | Accepted all changes as approved on anomaly logs, re-paginated document, re-ran TOCs, and created Section 508 compliant PDF for uploading, with Word document, to RTC Jazz Tools as well as SharePoint.                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED           |
| 01/12/2018 | 2.1          | Applied changes from first anomaly log dated 010418.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED           |
| 12/29/2017 | 2.1          | Updated document images to include “Skip to Content” link where necessary. Re-ran TOCs, added Alt Text to all images and figures, and changed document date from “August 2017” to “January 2018.” Updated Appendix entitled “VHIC Roles.”                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED           |
| 08/29/2017 | 2.0          | Checked Alt text for all images and figures. Added Alt text to figures without it. Changed name in footer from “Volume 1 Card Requests” to “Volume 4 Troubleshooting.” Fixed figure numbers for Figures 8-1 through 8-21 by removing the duplicate, leading “8.” Edited Figures 8-16 through 8-21 which still used old VHIC application versions of images. Re-ran TOCs and fixed content/figure pagination issues in the Word document. Document converted to Section 508 compliant PDF as part of VHIC 4.8. Updated document name to match VA naming conventions by replacing spaces in Word document name with underscores. | REDACTED           |
| 08/15/2017 | 2.0          | Updated for VHIC 4.8 release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED, REDACTED |
| 08/11/2016 | 1.6          | Completed technical writer review of document. Ran Spelling and Grammar, added Alt text to all images, and re-ran TOCs. Fixed Table of Tables TOC and footer page numbering. Changed cover date from “August 2016” to match footer date of “September 2016.”                                                                                                                                                                                                                                                                                                                                                                   | REDACTED           |
| 08/04/2016 | 1.6          | Updated content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED           |
| 12/28/2015 | 1.5          | Rebuilt to capture content overhaul to VHIC System and divided this guide into four separate parts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED           |
| 01/06/2015 | 1.4          | Rebuilt to capture content overhaul to VHIC System and divided this guide into three separate parts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED           |
| 07/07/2015 | 1.3          | Rebuilt to capture content overhaul to VHIC System and divided this guide into three separate parts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED           |

<span id="_Toc166065346" class="anchor"></span>Table 1: Enterprise Service Desk Contact Information

Table of Contents

Table of Figures

Table of Tables

Table 1: Enterprise Service Desk Contact Information [8](#_Toc166065346)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Assumptions](#assumptions)
  - [Disclaimers](#disclaimers)
    - [Software Disclaimer](#software-disclaimer)
    - [Documentation Disclaimer](#documentation-disclaimer)
    - [Documentation Conventions](#documentation-conventions)
- [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [Browser](#browser)
  - [Browser Incompatibility Issue](#browser-incompatibility-issue)
  - [Proper Navigation of the VHIC Application](#proper-navigation-of-the-vhic-application)
  - [Roles within VHIC](#roles-within-vhic)
  - [System Menu](#system-menu)
- [VHIC Troubleshooting (FAQ)](#vhic-troubleshooting-faq)
  - [Login Questions](#login-questions)
    - [Cannot log in to the application](#cannot-log-in-to-the-application)
    - [Do not have access to required areas/items](#do-not-have-access-to-required-areasitems)
    - [How to Find VHIC Supervisors](#how-to-find-vhic-supervisors)
  - [Address Questions](#address-questions)
    - [Veteran’s Address is Incorrect at the ‘Step 4: Select Mailing Address’ Screen](#veterans-address-is-incorrect-at-the-step-4-select-mailing-address-screen)
    - [Requesting Facility Address is Incorrect at the ‘Step 4: Select Mailing Address’ Screen](#requesting-facility-address-is-incorrect-at-the-step-4-select-mailing-address-screen)
    - [What does the VHIC Card Look Like](#what-does-the-vhic-card-look-like)
    - [What are the Member ID and the Plan ID on the face of the VHIC card?](#what-are-the-member-id-and-the-plan-id-on-the-face-of-the-vhic-card)
    - [Member ID is Missing from Card](#member-id-is-missing-from-card)
    - [Photo not saved](#photo-not-saved)
  - [Information not updating with radio button selection](#information-not-updating-with-radio-button-selection)
  - [Error Questions](#error-questions)
    - [Can I request a card when ‘Bad MPI Address’ is displayed?](#can-i-request-a-card-when-bad-mpi-address-is-displayed)
    - [Can I request a card when ‘Bad Preferred Facility Address’ is displayed?](#can-i-request-a-card-when-bad-preferred-facility-address-is-displayed)
    - [What to do with “Error accessing MPI” messages](#what-to-do-with-error-accessing-mpi-messages)
    - [What to do with “MPI Did Not Return an Enrollment Identifier” messages on Step 2](#what-to-do-with-mpi-did-not-return-an-enrollment-identifier-messages-on-step-2)
  - [Photo Error Questions](#photo-error-questions)
    - [Step 3: Capture Veteran Image](#step-3-capture-veteran-image)
    - [Step 5: Save Card Request](#step-5-save-card-request)
    - [Wrong Photo on Veteran’s VHIC](#wrong-photo-on-veterans-vhic)
  - [Report Questions](#report-questions)
    - [Report not returning results for selected date range](#report-not-returning-results-for-selected-date-range)
  - [On Hold Reasons](#on-hold-reasons)
    - [Veteran Not Proofed](#veteran-not-proofed)
    - [VHA Enrollment Services Unavailable](#vha-enrollment-services-unavailable)
    - [Eligibility Pending](#eligibility-pending)
    - [Bad Data – Other](#bad-data-other)
    - [No EDIPI](#no-edipi)
    - [Imprecise Date of Birth](#imprecise-date-of-birth)
    - [Manual Review Required](#manual-review-required)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this User Guide is to provide general system information and cover some troubleshooting issues and solutions that will help the VHIC user to be better able to support the Veteran and ensure that the VHIC requests are processed properly.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for the VHIC application.
- User is using *Google Chrome or Microsoft Edge* to do their job of either Creating VHIC Card Requests, Running Reports, or Deactivating VHICs depending on user roles.
- User has validated access to the VHIC application.
- User has completed any prerequisite training.

## Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

### Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

Various fonts are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these fonts:

- <u>NOTE:</u> Used to inform the reader of general information including references to additional reading material
- Descriptive text is presented in a proportional font (as represented by this font).
- “Screenshots” of computer online displays (i.e., character-based screen captures/dialogs) and are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- Cross references and hyperlinks within the document will be represented by italics (*such as this*)
- User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be \[boldface\] type and enclosed in brackets.

# Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The support contact information documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The following table lists the contact information needed by site users for troubleshooting purposes. Support contacts are listed by description of the incident escalation and contact information (phone number and options to select).

<table>
<caption>Support InformationSample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Issue</th>
<th>Contact Info</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>For Provisioning Issues</td>
<td><p>Contact the Enterprise Service Desk at REDACTED, option 2.</p>
<p>When contacted by a support specialist, be ready to supply the employee’s full name, VA user ID and email address.</p></td>
</tr>
<tr class="even">
<td>For Proofing Issues</td>
<td><p>Contact the Enterprise Service Desk at REDACTED, option 2.</p>
<p>When contacted by a support specialist, be ready to supply the Veterans' full name, full SSN, and DOB.</p></td>
</tr>
<tr class="odd">
<td>For All Other VHIC System Issues</td>
<td><p>Contact the Enterprise Service Desk at REDACTED, option 2.</p>
<p>When contacted by a support specialist, be ready to supply the Veterans' full name, full SSN, and DOB.</p></td>
</tr>
</tbody>
</table>

Support InformationSample Tier Support Contact Information, including name, role, organization, and contact information.

# Browser

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once users are logged into their VA desktop, they will access VHIC using "Google Chrome by either entering the URL. The VHIC URL is REDACTED and is case sensitive. After successfully logging in to the VHIC application, users should bookmark this site for easy access in the future. Please do NOT use the \[Refresh\] button at the top of your browser window if you mistype the VHIC URL. The \[Refresh\] button will redirect you to the VA website. Please re-enter the VHIC URL and try again.

## Browser Incompatibility Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In some instances, users may experience image misplacement or misalignment. This is most likely due to the current browser compatibility settings. You will want to ensure that the browser is not set to Compatibility View.

Examples of Image Misplacement and Other Misalignments:

<span id="_Toc166065318" class="anchor"></span>Figure 1: Over-sized icon buttons on the Home Screen

![](vhic-4-29-user-guide-vol-4-troubleshooting/002.png)

<span id="_Toc166065319" class="anchor"></span>Figure 2: Words wrapping around the displayed photo on Step 3

![](vhic-4-29-user-guide-vol-4-troubleshooting/003.png)

<span id="_Toc166065320" class="anchor"></span>Figure 3: Content on the right of the Step 5 screen is shifted down

![](vhic-4-29-user-guide-vol-4-troubleshooting/004.png)

<span id="_Toc166065321" class="anchor"></span>Figure 4: Both the VISN and Facility selection lists are displayed and shifted to the right

![](vhic-4-29-user-guide-vol-4-troubleshooting/005.png)

If you are experiencing misalignment issues, you will need to create an Enterprise ticket through the \[yourIT\] icon on your desktop or by calling REDACTED as your Chrome browser compatibility settings are managed by our IT Organization.

## Proper Navigation of the VHIC Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The correct way to navigate through the VHIC application is to use the *Back* and *Next* buttons that are located at the bottom of each screen instead of using the Browser’s built in Back button. Please do NOT use the *Back* button at the top of your browser window to navigate back to a previous screen; this will cause errors to occur.

<span id="_Toc166065322" class="anchor"></span>Figure 5: VHIC Navigation Buttons

![](vhic-4-29-user-guide-vol-4-troubleshooting/006.png)

The VHIC user can also navigate to the different features within the VHIC application by clicking on one of the navigation links located in the header near the top left of the screen. The user’s assigned role will determine which links are available as seen below.

<span id="_Toc166065323" class="anchor"></span>Figure 6: VHIC Administrator and VHIC Technical Administrator (Tier 3) menu

![](vhic-4-29-user-guide-vol-4-troubleshooting/007.png)

<span id="_Toc166065324" class="anchor"></span>Figure 7: VHIC Clerk and VHIC Supervisor menu

![](vhic-4-29-user-guide-vol-4-troubleshooting/008.png)

<span id="_Toc166065325" class="anchor"></span>Figure 8: VHIC Auditor and VHIC Read-Only User menu

![](vhic-4-29-user-guide-vol-4-troubleshooting/009.png)

## Roles within VHIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC application is built to accommodate a specific set of pre-established user roles. During the provisioning process, the VHIC user will have a role assigned to them, which will determine what aspects of the VHIC application are available to them. Detailed information on VHIC Roles and Access levels can be found in the Veteran Health Identification Card (VHIC) Roles and Access Guide document.

If, while utilizing the VHIC application, a user finds they do not have access to items they feel they should have access to or find that they have access to items they should not, based on the definitions listed below, the VHIC user should report this information to their VHIC Supervisor. The VHIC Supervisor should then verify that the proper role has been assigned.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the VHIC users’ role, they will be presented different Home screens upon logging to the VHIC application.

# VHIC Troubleshooting (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section houses some of VHIC’s most frequently asked questions along with the proper guidance on how to remedy or even avoid the issue. Some of the provided steps can be taken as preventative measures to ensure you are less likely to encounter these situations.

## Login Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Cannot log in to the application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are unable to log in to the VHIC application, make sure you are using the correct URL listed in Section 3 Browser

If you cannot move past the sign on screen and are given a message stating you don’t have access, please log a ticket requesting help by calling the Contact the Enterprise Service Desk at REDACTED.

If you are able to sign on but are taken to the VA home page or to a non-functioning VHIC screen, please check with your VHIC Supervisor to ensure that you have been properly provisioned and have the necessary authorization that would allow you to access VHIC.

### Do not have access to required areas/items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you log in to VHIC and do not have access to specific areas belonging to your specific role, please check with your VHIC Supervisor to ensure that you have been properly provisioned to access the VHIC application.

### How to Find VHIC Supervisors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you do not know your VHIC provisioning supervisor, log a ticket by contacting the Enterprise Service Desk at REDACTED.

## Address Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Veteran’s Address is Incorrect at the ‘Step 4: Select Mailing Address’ Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Veteran’s address is incorrect at ‘Step 4: Select Mailing Address’, it must be fixed in the VHA Enrollment System (VES) by someone at your site before card request. After 48 hours, if the address displayed is not correct, call the contacting the Enterprise Service Desk at REDACTED and log a ticket for assistance. Inform the Enterprise Service Desk which screen holds the incorrect address. When contacted by the Admin support team, give them the Veteran’s name, date of birth and social security number for further evaluation.

### Requesting Facility Address is Incorrect at the ‘Step 4: Select Mailing Address’ Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the address for the Requesting Facility is not correct, notify the Health Economics Resource Center by sending an email to: REDACTED. This department is responsible for facility address changes that are included in the Veteran Administration Site Tracking System (VAST) Card Questions

### What does the VHIC Card Look Like

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc166065326" class="anchor"></span>Figure 9: Example of what the VHIC looks like

![](vhic-4-29-user-guide-vol-4-troubleshooting/010.png)

### What are the Member ID and the Plan ID on the face of the VHIC card?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Member ID is the unique identifier for the person as established by the Department of Defense (DoD). The Member ID is also called the Electronic Data Interchange Personal Identifier (EDIPI).

The Plan ID is the unique Health Plan Identifier assigned to the Department of Veterans Affairs (VA) as established by the Centers for Medicare and Medicaid Services. This number is the same for all VHIC cards.

### Member ID is Missing from Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Service Desk ticket should NOT be created when the Member ID - also called EDIPI - is missing from a VHIC card.

If “No EDIPI” displayed under Reason for Hold, it means that the VA does not have Defense Enrollment Eligibility Reporting System (DEERS) data for that individual at this time. Select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for thirty (30) days and a request will be generated for HC IdM remediation once you select the hold button.

<span id="_Toc166065327" class="anchor"></span>Figure 10: No EDIPI Hold

![](vhic-4-29-user-guide-vol-4-troubleshooting/011.png)

A Confirmation message will appear, select the \[OK\] button.

<span id="_Toc166065328" class="anchor"></span>Figure 11: On Hold Request Confirmation Box

![](vhic-4-29-user-guide-vol-4-troubleshooting/012.png)

The request number will be displayed in a message that can be used for tracking purposes in the Tool Kit.

<span id="_Toc166065329" class="anchor"></span>Figure 12: HC IdM Request Confirmation

![](vhic-4-29-user-guide-vol-4-troubleshooting/013.png)

### Photo not saved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If for any reason you are unable to complete the card request by clicking either the \[Submit\] or \[Hold\] buttons on Step 5, the VHIC system will not save the photo. You would have to either take a new photo or upload a new photo on Step 3 when you process a new card request for that Veteran.

## Information not updating with radio button selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If making certain selections (i.e., check boxes or radio buttons) does not appear to be functioning as expected, this could be due to your browser compatibility settings not being properly set. Follow the steps listed in Section <u>3.1</u> to update these.

## Error Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Can I request a card when ‘Bad MPI Address’ is displayed?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Home addresses are stored in the VHA Enrollment Services database and in the MPI database. When a valid MPI address is unavailable, the ‘Bad MPI Address’ message is displayed in black letters at the top of the screen. When this occurs, select the VHA Enrollment Services address, the requesting facility address, or the preferred facility address and continue with the card request.

### Can I request a card when ‘Bad Preferred Facility Address’ is displayed?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preferred facilities are sent to VHIC from VHA Enrollment Services. Occasionally, a Veteran will not have a preferred facility associated with their enrollment record. When VHIC does not receive a preferred facility from ES, the VHIC system will display the message ‘Bad Preferred Facility Address’ in red letters at the top of the screen. When this occurs, select the VHA Enrollment Services address, MPI address, or the requesting facility address and continue with the card request.

### What to do with “Error accessing MPI” messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The problem will be forwarded to the Admin support team, and Admin will forward to tier 3 DEV-VIC4 for resolution.

This problem occurs during peak workload times and is an intermittent problem. Sites experiencing this problem should periodically retry to process VHIC cards.

### What to do with “MPI Did Not Return an Enrollment Identifier” messages on Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enrollment status is obtained by the VHIC system from the VHA Enrollment Services System. Some Veterans have no defined enrollment status in VES (even though they are known to MPI), as indicated by the “No Enrollment Determination” comment.

During card requests for these “no enrollment status” Veterans, at the ‘Step 2 Select Veteran’ screen, a message stating that the “Eligibility could not be determined. MPI did not return an Enrollment \[sic\] identifier for ICN” is displayed. Inform the Veteran that they will need to have the problem fixed in the VHA Enrollment Services System, (and possibly wait up to 48 hours for the change to become visible to VHIC), and then the card can be requested.

## Photo Error Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A photo collision is the possibility of two Veteran images getting swapped.

We have implemented several checks at different points of the card request process; *Step 3: Capture Veteran Image*, *Step 5: Save Card Request*, and the *Card Monitor Job*, which is the title of a task run every day in the VHIC system.

### Step 3: Capture Veteran Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first set of checks happens at Step 3: Capture Veteran Image when the VHIC user clicks the \[Next\] button after taking a new picture or uploading a photo.

The VHIC system will now check to make sure that the picture being taken or uploaded is not already assigned to another Veteran.

<span id="_Toc166065330" class="anchor"></span>Figure 13: Step 3: Capture Veteran Image

![](vhic-4-29-user-guide-vol-4-troubleshooting/014.png)

If the VHIC application detects a collision, the VHIC user will see the below error show up under the Navigation Bar. If this occurs, then the VHIC user can click the Back button until they get to Step 2: Select Veteran.

<span id="_Toc166065331" class="anchor"></span>Figure 14: Step 3: "Error Saving Picture" error message

![](vhic-4-29-user-guide-vol-4-troubleshooting/015.png)

Click on the Veteran’s name to be taken to Step 3 again to take a new photo or upload a photo. If using the same photo, you will need to rename the file, i.e., upload1.jpg would be renamed as upload2.jpg. You can then proceed with the card request as normal.

<span id="_Toc166065332" class="anchor"></span>Figure 15: Step 2: Select Veteran screen

![](vhic-4-29-user-guide-vol-4-troubleshooting/016.png)

### Step 5: Save Card Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second place that the VHIC application checks for possible photo collisions, is on Step 5: Save Card Request when the VHIC user clicks either the \[Submit\] or \[Hold\] button.

The VHIC system will then check to make sure that the Veteran’s photo is not associated with any other Veteran.

<span id="_Toc166065333" class="anchor"></span>Figure 16: Step 5: Save card Request review screen

![](vhic-4-29-user-guide-vol-4-troubleshooting/017.png)

If the VHIC application detects a collision, the VHIC user will see the below error show up under the Navigation Bar.

When this occurs, the VHIC user MUST start a new Card Request for the Veteran by clicking on the \[Card Request\] link in the header and take a new photo. If using the same photo, you will need to rename the file, i.e., upload1.jpg would be renamed as upload2.jpg. Since the proofing process was completed at Step 5, there is no need to ID proof the Veteran again.

<span id="_Toc166065334" class="anchor"></span>Figure 17: Step 5: "Error accessing VHIC Database. If the error persists, please contact the helpdesk.” error message

![](vhic-4-29-user-guide-vol-4-troubleshooting/018.png)

### Wrong Photo on Veteran’s VHIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a Veteran brings in a VHIC card that has the wrong photo printed on it, the VHIC user needs to create a ticket in this scenario so that system administrators can mark the photo as not valid to prevent reuse. The card will need to be destroyed and the Veteran will need to request a new VHIC.

## Report Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Report not returning results for selected date range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are running a report within a specific date range and find that the results stop well before your end date, this could be a result of having too many results returned. The system limits results to 3000 rows. Any results over this amount will not be returned. Consider modifying the start and end dates for the report in question.

If you specify a large date range, the report might time out and return no results. In that case, retry the report with a smaller date range.

## On Hold Reasons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Veteran Not Proofed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### User did NOT complete the proofing process using the Identity Management Toolkit application PRIOR to creating a VHIC request

If the VHIC user started the VHIC card request BEFORE going into the Identity Management Toolkit application and completing the proofing process, the VHIC application will display the below Warning message on Step 4 of the card request process indicating that the Veteran has NOT been Identity Proofed. The VHIC user will also see “Veteran not proofed” as the Reason for Hold on Step 5. The VHIC application will allow you to save the card request on hold. The card request will be saved for 30 days.

<span id="_Toc166065335" class="anchor"></span>Figure 18: Veteran Not Proofed Warning message on Step 4: Select Mailing Address

![](vhic-4-29-user-guide-vol-4-troubleshooting/019.png)

<span id="_Toc166065336" class="anchor"></span>Figure 19: Reason for Hold: Veteran Not Proofed

![](vhic-4-29-user-guide-vol-4-troubleshooting/020.png)

Once the VHIC user completes the Identity Proofing in the Identity Management Toolkit application, they can return to the VHIC application to take the card request off hold. The VHIC user will start a card request as they would normally. The VHIC user will see the On Hold Reason – Veteran Not Proofed displayed on Step 4 of the card request process.

<span id="_Toc166065337" class="anchor"></span>Figure 20: Card Request Status: On Hold - Veteran Not Proofed

![](vhic-4-29-user-guide-vol-4-troubleshooting/021.png)

Continue with the card request process and submit the card request as outlined in section 5.3 Resuming an On-Hold VHIC Request: Veteran NOT Level 2 Proofed Hold Reason in the *Veteran Health Identification Card User Guide - Volume 2 - Reports* document.

<u>NOTE:</u> There is a background job that runs every morning at 7:00 a.m. Eastern Time that will check the proofing status of any cards placed on hold. As long as there are no other issues with the card request, the job will submit the card request to the print vendor.

### VHA Enrollment Services Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 5 and see the message “Enrollment Unavailable” displayed under Reason for Hold, which means that VHIC is unable to communicate to VHA Enrollment Services at this time, select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for 30 days.

<span id="_Toc166065338" class="anchor"></span>Figure 21: Reason for Hold: VHA Enrollment Unavailable

![](vhic-4-29-user-guide-vol-4-troubleshooting/022.png)

Next, log a ticket by calling the Enterprise Service Desk at REDACTED or create a ticket through the \[yourIT\] shortcut on your desktop.

<u>NOTE:</u> There is a background job that runs every morning at 7:00 a.m. Eastern Time that will check the eligibility status of any cards placed on hold.

- If the Eligibility status is confirmed as “Eligible” and there are no other issues with the card request, the job will submit the card request to the print vendor.
- If the Eligibility status is confirmed as “Not Eligible”, the card request will be terminated, and no card will be issued.

### Eligibility Pending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 5 and see the message “Eligibility Pending” displayed under Reason for Hold, which means that VHA Enrollment Services has returned an eligibility status of “Pending” at this time, select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for seven (7) days.

<span id="_Toc166065339" class="anchor"></span>Figure 22: Reason for Hold: Eligibility Pending

![](vhic-4-29-user-guide-vol-4-troubleshooting/023.png)

<u>NOTE:</u> The Veteran should go to VHA Enrollment Services to have the record updated as needed. There is a background job that runs every morning at 7:00 a.m. Eastern Time that will check the eligibility status of any cards placed on hold.

- If the Eligibility status is confirmed as “Eligible” and there are no other issues with the card request, the job will submit the card request to the print vendor.
- If the Eligibility status is confirmed as “Not Eligible” or is not updated within Seven (7) days, the card request will be terminated, and no card will be issued.

### Bad Data – Other

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 5: Save Card Request and any information that is displayed on the screen needs to get changed/updated, click the checkbox next to “Bad Data” under Reason for Hold. A Details field will be displayed, and you can enter a description on what information needs to be updated. Then select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for 30 days.

<span id="_Toc166065340" class="anchor"></span>Figure 23: Reason for Hold: Bad Data - Name Spelled Wrong

![](vhic-4-29-user-guide-vol-4-troubleshooting/024.png)

The Veteran should go to VHA Enrollment Services to have the record updated as needed. Card requests that have been placed on hold with “Bad Data” as the Reason for Hold will NOT be updated and submitted by the background job.

The Veteran will need to return to complete the card request after they have had the information updated. You will need to start a card request as you would normally. On Step 4 of the card request process, you will see the On Hold Reason – Bad Data: (reason entered when saved) displayed.

<span id="_Toc166065341" class="anchor"></span>Figure 24: Card Request Status: Replacement on Hold - Bad Data: Name Spelled Wrong

![](vhic-4-29-user-guide-vol-4-troubleshooting/025.png)

Continue with the card request process. When you get to Step 5, you will need to <u>uncheck</u> the checkbox next to “Bad Data” in order to be able to submit the card request.

<span id="_Toc166065342" class="anchor"></span>Figure 25: Reason for Hold: Bad Data Unchecked

![](vhic-4-29-user-guide-vol-4-troubleshooting/026.png)

### No EDIPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 5 and see the message “No EDIPI” displayed under Reason for Hold, it means that the veteran does not have an EDIPI number. This requires a review from HC IdM. Click on the \[Hold\] button. This will save the card request for thirty (30) days and generate a request for HC IdM to remediate.<span id="_Hlk56517886" class="anchor"></span>

Figure 26: Reason for Hold No EDIPI

![](vhic-4-29-user-guide-vol-4-troubleshooting/027.png)

Refer to Section 4.2.5 for instructions on how to process requests when this reason for hold occurs.

### Imprecise Date of Birth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 6 and see the message “Invalid Date of Birth” displayed under Reason for Hold, it means that the VA received an imprecise Date of Birth, such as Month/year instead of Month/Date/Year. A request needs to be created for HC IdM remediation. Select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for thirty (30) days and generate the remediation request for HC IdM.

<span id="_Toc166065344" class="anchor"></span>Figure 27: Invalid Date of Death Hold

![](vhic-4-29-user-guide-vol-4-troubleshooting/028.png)

### Manual Review Required 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get to Step 5 and see the message “Manual Review Required” displayed under Reason for Hold, it means that the veteran has submitted their request through the VA Self Service Portal and the request could not be completed without VA review. This request requires a POC to verify the documents that the veteran submitted during their online request for a new card.

<span id="_Toc166065345" class="anchor"></span>Figure 28: Manual Review Required Hold

![](vhic-4-29-user-guide-vol-4-troubleshooting/029.png)