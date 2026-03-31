---
title: VHIC 4.29 User Guide Vol 5 Card Replacement VES Users
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Vol 5 Card Replacement VES Users
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
  - card
  - vhic
  - replacement
  - span
  - table
  - veteran
  - request
  - contents
  - class
  - guide
page_count: 0
word_count: 4117
section_count: 11
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2024
revision_count: 19
revision_newest: 05/18/2024
revision_oldest: 10/02/2018
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v5.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v5.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=274"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Veteran Health Identification Card (VHIC 4.29)

  User Guide
---

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/001.png)

Volume 5 – Card Replacement User

VHA Enrollment Services

May 2024

Office of Information and Technology (OI&T)

Revision History

<u>NOTE</u>: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date   | Revision | Description                                                                                                                                                                                                                                                                                                                                                    | Author    |
|------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 05/18/2024 | 9            | Updated VHIC Clerk title, replaced VHIC card sample                                                                                                                                                                                                                                                                                                                | Dawn Bryant   |
| 03/17/2024 | 8.3          | No changes in functionality updated date and version number, updated styles and formatting                                                                                                                                                                                                                                                                         | Dawn Bryant   |
| 12/14/2023 | 8.2          | No changes in functionality updated date and version number                                                                                                                                                                                                                                                                                                        | Dawn Bryant   |
| 09/18/2023 | 8.1          | No changes in functionality updated date and version number                                                                                                                                                                                                                                                                                                        | Dawn Bryant   |
| 06/17/2023 | 8            | Updated to reflect changes in the VHIC card request functionality during VIP 25, removed duplicate information and information unrelated to VES Users.                                                                                                                                                                                                             | Dawn Bryant   |
| 03/18/2023 | 7            | Updated to reflect changes in the VHIC card request functionality during VIP 24                                                                                                                                                                                                                                                                                    | Dawn Bryant   |
| 12/17/2022 | 6.2          | Updated document title and content to reflect name change from Enrollment Services (ES) to VHA Enrollment Services (VES)                                                                                                                                                                                                                                           | Dawn Bryant   |
| 09/18/2022 | 6.1          | No changes in functionality updated date and version number                                                                                                                                                                                                                                                                                                        | Dawn Bryant   |
| 06/18/2022 | 6.0          | Updated to reflect changes during VIP 21                                                                                                                                                                                                                                                                                                                           | Dawn Bryant   |
| 04/18/2022 | 5.2          | No changes in functionality updated date and version number                                                                                                                                                                                                                                                                                                        | Dawn Bryant   |
| 09/18/2021 | 5.1          | No changes in functionality updated date and version number                                                                                                                                                                                                                                                                                                        | Dawn Bryant   |
| 06/20/2021 | 5.0          | Updated to reflect functionality changes during VIP 17                                                                                                                                                                                                                                                                                                             | Dawn Bryant   |
| 03/20/2021 | 4.1          | Updated to reflect functionality changes during VIP 16                                                                                                                                                                                                                                                                                                             | Dawn Bryant   |
| 12/10/2020 | 4.0          | Updated to reflect changes during VIP 15                                                                                                                                                                                                                                                                                                                           | Dawn Bryant   |
| 06/20/2020 | 3.0          | Updated to reflect changes to application During VIP 13                                                                                                                                                                                                                                                                                                            | Dawn Bryant   |
| 02/15/2020 | 2.0          | Updated to reflect changes to application During VIP 11                                                                                                                                                                                                                                                                                                            | Dawn Bryant   |
| 10/02/2018 | 1.0          | Initial Draft                                                                                                                                                                                                                                                                                                                                                      | Dawn Bryant   |
| 11/09/2018 | 1.0          | Re-ran TOCs, ran Spelling and Grammar, fixed content/figure pagination issues in the Word document, and added Alt text to all images. Created Section 508 compliant PDF for uploading, with revised Word document, to RTC Jazz Tools as well as SharePoint. No technical content changed in editing process. Completed editing 11/09/2018 for 11/14/2018 delivery. | Donnie Canham |
| 09/19/2019 | 2.0          | Updated to reflect changes to application release of version 4.9                                                                                                                                                                                                                                                                                                   | Dawn Bryant   |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

Table of Figures

Table of Tables

[Table 1: Enterprise Service Desk Contact Information [6](#_Toc439918773)](#_Toc439918773)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
  - [Assumptions](#assumptions)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [Veteran Health Identification Card – What is it?](#veteran-health-identification-card-what-is-it)
- [Getting Started](#getting-started)
  - [Roles Within VHIC](#roles-within-vhic)
  - [Proper Navigation of the VHIC Application](#proper-navigation-of-the-vhic-application)
  - [Logging On: VHA Enrollment System Link to VHIC](#logging-on-vha-enrollment-system-link-to-vhic)
  - [VHIC Home Screen](#vhic-home-screen)
    - [Veteran Card Details Page](#veteran-card-details-page)
- [Requesting a Replacement VHIC Card](#requesting-a-replacement-vhic-card)
  - [Card Replacement Eligibility](#card-replacement-eligibility)
  - [Requesting a Replacement Card](#requesting-a-replacement-card)
    - [VHIC Card Replacement Request](#vhic-card-replacement-request)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this User Guide is to provide general system information, as well as accessibility and user roles with the VHIC application. This User Guide will provide a detailed walkthrough of creating a Veteran Health Identification Card replacement request using the VHIC application.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Guide is divided into sections to allow you to quickly obtain the information you need.

The first section will provide an overview of the documentation.

The second section explains what a VHIC is and what the eligibility requirements are.

The third section reviews the various user roles and their accessibility within the VHIC application and will walk the user through the steps needed to access the VHIC application, as well as some general guidelines on using the VHIC application.

The fourth section will give the user step-by-step details of how to complete the Replacement Card Request. Once all of the required information has been provided, the final step in the process will allow a VHIC request to be submitted for processing.

Each day, these card requests are transmitted from the VHIC system to a vendor to print and mail the cards to the Veterans, the preferred facility, or the requesting facility. Typically, the cards are received in 7-10 business days from date of request. To ensure the VHIC is received at the appropriate address, the VHIC Clerk must verify that the correct address is used, and the Print Vendor verifies that the address is valid. If the U.S. Postal Service cannot deliver the card, it is returned to the requesting facility.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide has been written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles required for the VHIC application.
- User is using Google Chrome or Microsoft Edge to do their job of either Creating a VHIC Card Request, Running Reports, or Managing VHICs depending on user roles.
- User has validated access to the VHIC application.
- User has completed any prerequisite training.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

Various fonts and symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

- Descriptive text is presented in a proportional font (as represented by this font).
- “Screenshots” of computer online displays (i.e., character-based screen captures/dialogs) and are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- Screen shot and section cross references will be seen in italic font (*such as this*)
- User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be \[boldface\] type and enclosed in brackets.

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The support contact information documented herein is intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The following table lists the contact information needed by site users for troubleshooting purposes. Support contacts are listed by description of the incident escalation and contact information (phone number and options to select).

<span id="_Toc439918773" class="anchor"></span>Table 1: Enterprise Service Desk Contact Information

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Issue</strong></th>
<th><strong>Contact Info</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>For Provisioning Issues</td>
<td><p>Contact the Enterprise Service Desk at (855) 673-4357, option 2.</p>
<p>When contacted by a support specialist, be ready to supply the employee’s full name, VA user ID and email address.</p></td>
</tr>
<tr class="even">
<td>For Proofing Issues</td>
<td><p>Contact the Enterprise Service Desk at (855) 673-4357, option 2.</p>
<p>When contacted by a support specialist, be ready to supply the Veterans' full name, full SSN, and DOB.</p></td>
</tr>
<tr class="odd">
<td>For All Other VHIC System Issues</td>
<td>Contact the Enterprise Service Desk at (855) 673-4357, option 2 When contacted by a support specialist, be ready to supply the Veterans' full name, full SSN, and DOB.</td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# Veteran Health Identification Card – What is it?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC serves as an identification mechanism for Veterans that are enrolled in the VA Healthcare system and supports efficiencies at VA medical facilities throughout the United States. Although not required by Veterans to receive medical care at a VA facility, it does enable Veterans to check in for VA appointments more quickly. The VHIC system is a web-based application that VHIC Clerks use to issue VHICs to enrolled Veterans.

<span id="_Toc166068571" class="anchor"></span>Figure : Example of what the VHIC looks like

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/002.png)

In order to be able to receive a VHIC, a Veteran must meet the following eligibility criteria:

- Be eligible for VA medical benefits
- Be enrolled in the VA Healthcare system
- Be Level 2 proofed at a VA medical facility
- Veteran identity must be recognized in the Master Person Index (MPI), which is managed by the Identity and Access Management (IAM) of the VA

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Roles Within VHIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC application is built to accommodate a specific set of pre-established user roles. During the provisioning process, the VHIC user will have a role assigned to them, which will determine what aspects of the VHIC application are available to them. The following breaks down the specific roles and the areas of access that accompany each role.

If, while utilizing the VHIC application, a user finds they do not have access to items they feel they should have access to or find that they have access to items they should not, based on the definitions listed below, the VHIC user should report this information to their VHIC Supervisor. The VHIC Supervisor should then verify that the proper role has been assigned.

For a complete list of Roles and Access levels please refer to the VHIC Roles and Access document.

## Proper Navigation of the VHIC Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The correct way to navigate through the VHIC application is to use the buttons that are located at the bottom of each screen instead of using the Browser’s built in Back button. Please do NOT use the *Back* button at the top of your browser window to navigate back to a previous screen; this will cause errors to occur.

## Logging On: VHA Enrollment System Link to VHIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once users are logged into the Enrollment System, an eligible user will be able to click on a hyperlink in the VHA Enrollment System and be directed to VHIC. Their VHIC role of Card Replacement User provides access to features in the VHIC application for VES Users use only.

<span id="_Hlk526247498" class="anchor"></span>Figure : VHIC VES Hyperlink

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/003.png)

## VHIC Home Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the hyperlink has been selected, a second browser tab will be opened and VHIC Users will be directed to the Home screen assigned to their roles. To the eligible HEC VES users (Card Replacement Role), the Veteran Card Details page serves as their Home page for the application.

<span id="_Hlk526247529" class="anchor"></span>Figure : VHIC VES User Home Page

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/004.png)

### Veteran Card Details Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran Card Details page provides the latest Card Status information based on the card ID received from the VHA Enrollment System and provides capability to request a replacement VHIC card based on the business rules for card replacement.

The Veteran Card Details page is broken into three sections.

1.  Veteran Identity Information

This section provides the Veteran Identity Information including:

- Veteran’s Full Name
- Date of Birth
- Gender
- Branch of Service
- Enrollment Status
- Person ID

<span id="_Hlk526247596" class="anchor"></span>Figure : Veteran Identity Section

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/005.png)

<u>NOTE:</u> If the Veteran has a Preferred Name on file it will appear within parenthesis where the Full Name appears as seen in the below example.

<span id="_Toc166068575" class="anchor"></span>Figure . Veteran Identity Section with Preferred Name

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/006.png)

2.  Veteran Card Details

This section provides the Veteran Identity Information including:

- Card ID
- VISN
- Facility
- Current Card Status
- Current MPI Status
- Current Print Status
- Card Request Date
- Date of Mailing
- Expiration Date
- Mailing Address

<span id="_Toc166068576" class="anchor"></span>Figure : Card Detail Section

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/007.png)

3.  Veteran Card History

This section provides the Veteran Card Information including:

- Card ID
- Card Status
- MPI Status
- Print Status
- Print Message
- Card Status
- Change Date
- ID of User that facilitated last Card Status change

<span id="_Toc166068577" class="anchor"></span>Figure : Veteran Card History Section

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/008.png)

# Requesting a Replacement VHIC Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Card Replacement Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Card Replacement option is only available to veterans with an active VHIC card.

A card replacement request may not be made within 10 days of the submission of a previous card request.

If the replacement requirements are not met, the user will see a notification at the top of the page, and the \[Get Replacement Card\] button will be shown but greyed out and not available.

<span id="_Toc166068578" class="anchor"></span>Figure : Card Not Eligible for Replacement

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/009.png)

If the card is Eligible for Replacement, the \[Get Replacement Card\] button can be seen and selected.

<span id="_Toc166068579" class="anchor"></span>Figure : Card Eligible for Replacement

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/010.png)

## Requesting a Replacement Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will give the VES user the step-by-step details of the process to replace a card in VHIC.

### VHIC Card Replacement Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have been transferred from the VHA Enrollment System to the VHIC system, review and verify all information found on the Veteran Card Details Page. When all details have been verified, click on the \[Get Replacement Card\] button.

<span id="_Toc166068580" class="anchor"></span>Figure : Select the Get Replacement Card Button

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/011.png)

After clicking the \[Get Replacement Card\] button, you will be directed to the Veteran Identity Confirmation page. This screen displays the information retrieved from the Master Person Index (MPI) and the VHA Enrollment System (VES) for the selected Veteran.

The purpose of this screen is to verify the displayed information, select the reason for replacement, and to determine where the Veteran’s card should be mailed.

<span id="_Toc166068581" class="anchor"></span>Figure : Veteran Identity Confirmation Page

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/012.png)

<u>  
</u><u>NOTE:</u> If the Veteran has a Preferred Name on file it will appear in the Veteran Identity Attribute section as shown.

<span id="_Toc166068582" class="anchor"></span>Figure . Veteran Identity Attributes with Preferred Name

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/013.png)

Select the reason for replacement from the drop-down menu. Confirm the Veteran and Facility information and move down to the Address section of the screen to select where the replacement card will be delivered.

<span id="_Toc166068583" class="anchor"></span>Figure : Select Replacement Reason

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/014.png)

<span id="_Toc166068584" class="anchor"></span>Figure : Select Mailing Address

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/015.png)

This step provides several mailing options for the card:

- Mail to the address received from Enrollment Services
- Mail to the address received from MPI
- Mail to the requesting facility If requesting facility is not known a message will be displayed above for the on-hold condition and the Requesting facility button will be grayed out as seen in *Figure 15: Select Next Button to Continue*
- Mail to the preferred facility

<u>NOTE</u>: If Enrollment has flagged the Veteran’s address as bad, a message stating why, as well as additional guidance on how to proceed, will be displayed near the top of the screen. At this point, if the Veteran opts to not update their information with VES, the Clerk MUST choose one of the remaining viable address options for mailing the card in order to proceed with the card request process.

<u>NOTE:</u> If MPI has flagged the Veteran’s address as bad, a message stating why, as well as additional guidance on how to proceed, will be displayed near the top of the screen. At this point, if the Veteran opts not to update their information with MPI or VES, the Clerk MUST choose one of the remaining viable address options for mailing the card in order to proceed with the card request process. Selecting a radio button will automatically update the address information based on the selection. The process cannot continue until the appropriate radio button has been selected.

<u>NOTE:</u> If no preferred facility information has been received from VES or the preferred facility address is flagged as bad, a message stating why, as well as additional guidance on how to proceed, will be displayed near the top of the screen. The Clerk MUST choose one of the remaining viable address options for mailing the card in order to proceed with the card request process. Selecting a radio button will automatically update the address information based on the selection. The process cannot continue until the appropriate radio button has been selected.

Selecting a radio button will automatically update the address information based on the selection. The process cannot continue until the appropriate radio button has been selected.

If the information on the screen is a correct match, select the \[Next\] button in the lower right hand to move forward.

<span id="_Ref140838076" class="anchor"></span>Figure : Select Next Button to Continue

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/016.png)

You will be directed to the Save Card Request page (*Figure 20: Save Card Request*) which gives the VHIC user and the Veteran one more opportunity to review all of the information on the screen for accuracy.

This screen contains the following information for review:

- Name as it will appear on card
- Address card will be mailed to (*this also contains the name as it will appear in the mailing address*)
- Replacement reason (*if applicable*)
- Reason for hold (*if applicable*)
- Service-connected status
- Medal of Honor status
- Purple Heart status
- Prisoner of War status
- Branch of Service selection
- Date of Birth

Other fields that either will be populated or will populate upon final submission are:

- Card Number (populates upon final submission)
- Member ID
- ICN
- Member Benefit Plan ID
- VISN and Facility where request is being processed

#### Branch of Service

If available, the Veteran’s Branch of Service options will be displayed on screen. The Veteran should be given the opportunity to select which logo they would prefer to appear on their card or if they would like to decline the logo option altogether (*decline is the default option*). The appropriate radio button should be selected based upon the Veteran’s preference. Only those branches of service that are listed in the VHA Enrollment System and in which the Veteran has served will be shown. This will need to be chosen before submitting the card request.

<u>NOTES:</u>

- Only one Branch of Service logo can appear on the card; those with more than one branch will have to select one or decline to show any logo.
- The Preferred Name listed on the preview screen will not be printed on the card. It is only housed in the VHIC system.

<span id="_Toc166068586" class="anchor"></span>Figure : Branch of Service Selection

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/017.png)

<u>NOTE:</u> If the Veteran has a Preferred Name on file, it will appear as seen in below. Though Preferred Name appears in the system; it does NOT appear on the VHIC card at this time.

<span id="_Toc166068587" class="anchor"></span>Figure . Branch of Service Selection Preferred Name Highlighted

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/018.png)

#### Mailing Address Verification

Veterans with a foreign mailing address, have different postage requirements. To ensure they are handled appropriately, select the check box indicating Foreign mailing address.

<span id="_Toc166068588" class="anchor"></span>Figure . Veteran With Foreign Mailing Address

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/019.png)

A pop-up message will appear asking you to confirm the Foreign Address Setting. Click \[Yes\] to continue or \[Cancel\] to return.

<span id="_Toc166068589" class="anchor"></span>Figure . Confirm Foreign Address Setting

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/020.png)

After the card and information have been confirmed, click the \[Submit\] button at the bottom of the page to advance the request.

<span id="_Ref140837730" class="anchor"></span>Figure : Save Card Request

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/021.png)

#### Photograph Verification

After reviewing and approving the card details the VHIC user will click the \[Submit\] button. A pop-up box will appear requiring the clerk to acknowledge that they have approved the final picture that will be submitted for card printing. Selecting ok will allow the process to continue and submitting the request possible.

<span id="_Toc166068591" class="anchor"></span>Figure : Validate Veteran Photo

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/022.png)

Should a new photograph be needed, the user selects \[Cancel\] and will need to refer the veteran to the VHIC office for a new photo and replacement card.

<span id="_Toc166068592" class="anchor"></span>Figure : Photo Does Not Meet VHIC Standards

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/023.png)

<u>NOTE:</u> Greyscale pictures are not permitted to appear on the VHIC card.

Should the Veteran photo be Black and White or Greyscale, the VES User should select the \[Cancel\]

And refer the veteran to the VHIC office.

<span id="_Toc166068593" class="anchor"></span>Figure : Cancel Black and White Photo

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/024.png)

Once veteran photo has been approved and the \[Submit\] button selected the request will now show a Submitted status.

Upon submission, a Card Number will be generated as well as an Expiration Date and Card Request Date. The colored field will change from yellow to green and the corresponding Card Status will change from Pending to Submitted as seen below.

<span id="_Toc166068594" class="anchor"></span>Figure : Card Request Submitted

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/025.png)

This action has been completed. To exit the application, click the \[X\] button to close this browser window.

<span id="_Toc166068595" class="anchor"></span>Figure : Close Browser Window

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/026.png)

<u>NOTE:</u> If the veteran does not have an EDIPI number, the card request will be marked as Pending and saved for thirty (30) days. A request will be generated for HC IdM to investigate and resolve once you select the hold button.

<span id="_Toc166068596" class="anchor"></span>Figure : Pending Request No EDIPI

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/027.png)

A Confirmation message will appear, select the \[OK\] button.

<span id="_Toc166068597" class="anchor"></span>Figure : On Hold Request Confirmation Box

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/028.png)

The VHIC REQUEST ON HOLD – EDIPI request number will be displayed in a message that can be used for tracking purposes in the Tool Kit. Should anything prevent the card hold from resolving in 30 days an email will be generated to the VHIC Team for additional action.

<span id="_Toc166068598" class="anchor"></span>Figure : HC IdM Request Confirmation

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/029.png)

If a second request is generated before the thirty (30) days, the user will get a message indicating that a request is open in the system.

<span id="_Toc166068599" class="anchor"></span>Figure : Active Request Exists in System Message

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/030.png)

<u>NOTE:</u> If the VA received an imprecise Date of Birth, such as Month/year instead of Month/Date/Year. A request needs to be created for HC IdM remediation. Select the Branch of Service (if available) and click on the \[Hold\] button. This will save the card request for thirty (30) days and generate the remediation request for HC IdM.

<span id="_Toc166068600" class="anchor"></span>Figure : Reason for Hold: No EDIPI

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/031.png)

A Confirmation request message will appear, select the \[OK\] button.

<span id="_Toc166068601" class="anchor"></span>Figure : On Hold Request Confirmation Request

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/032.png)

The screen will change showing that the Card Request Status has been updated and saved.

<span id="_Toc166068602" class="anchor"></span>Figure : Saved on Hold

![](vhic-4-29-user-guide-vol-5-card-replacement-ves-users/033.png)