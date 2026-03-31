---
title: VHIC 4.29 User Guide Vol 6 Self Service Processing
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Vol 6 Self Service Processing
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
  - span
  - service
  - self
  - table
  - contents
  - task
  - class
  - processing
  - guide
page_count: 0
word_count: 4472
section_count: 13
table_count: 1
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2024
revision_count: 10
revision_newest: 05/18/2024
revision_oldest: 04/18/2022
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v6.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/vhic_4_29_um_v6.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=274"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Veteran Health Identification Card (VHIC 4.29)

  User Guide
---

![](vhic-4-29-user-guide-vol-6-self-service-processing/001.png)

Volume 6 – Self-Service Request Processing

May 2024

Office of Information and Technology (OIT)

Revision History

<u>NOTE:</u> The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description                                                                               | Author   |
|------------|----------|-------------------------------------------------------------------------------------------|----------|
| 05/18/2024 | 4.1      | No functionality changes, updated date, and version number                                | REDACTED |
| 03/17/2024 | 4        | Updated to reflect changes to functionality in VIP 28 release                             | REDACTED |
| 12/14/2023 | 3.1      | No functionality changes, updated date, and version number                                | REDACTED |
| 09/18/2023 | 3        | No functionality changes, updated help desk service option, date, and version number      | REDACTED |
| 06/17/2023 | 2.3      | No changes to functionality during VIP 25 release Updated to remove duplicate information | REDACTED |
| 03/18/2023 | 2.2      | No changes to functionality during VIP 24 release Date and version numbers updated        | REDACTED |
| 12/17/2022 | 2.1      | No changes to functionality during VIP 23 release Date and version numbers updated        | REDACTED |
| 09/18/2022 | 2.0      | Updated to reflect changes to functionality during VIP 22 release                         | REDACTED |
| 06/18/2022 | 1.0      | Updated to reflect changes to functionality during VIP 21                                 | REDACTED |
| 04/18/2022 | 0.1      | Created to support ACS Self-Service VHIC card requests                                    | REDACTED |

<span id="_Toc439918773" class="anchor"></span>Table 1: Enterprise Service Desk Contact Information

- 

Table of Contents

Table of Figures

Table of Tables

[Table 1: Enterprise Service Desk Contact Information [3](#_Toc439918773)](#_Toc439918773)

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
- [Self-Service VHIC Card Request – What is it?](#self-service-vhic-card-request-what-is-it)
- [Getting Started](#getting-started)
  - [Accessing the VHIC Application](#accessing-the-vhic-application)
    - [Single Sign-On Internal (SSOi)](#single-sign-on-internal-ssoi)
  - [System Menu](#system-menu)
  - [Accessing the Identity Management Toolkit](#accessing-the-identity-management-toolkit)
    - [Accessing the Identity Management Toolkit Directly](#accessing-the-identity-management-toolkit-directly)
    - [Accessing Identity Management Toolkit from within the VHIC Application](#accessing-identity-management-toolkit-from-within-the-vhic-application)
- [VHIC Application Home Page](#vhic-application-home-page)
  - [VHIC System Status Banner](#vhic-system-status-banner)
  - [VHIC Self-Service Request Notifications](#vhic-self-service-request-notifications)
  - [Viewing Self Service New Card Requests](#viewing-self-service-new-card-requests)
    - [View Unassigned Requests by VISN](#view-unassigned-requests-by-visn)
    - [View Unassigned Requests by Facility](#view-unassigned-requests-by-facility)
    - [Assigned Requests](#assigned-requests)
- [Self Service Request Processing](#self-service-request-processing)
  - [Person Verification Task- Accepted Image](#person-verification-task-accepted-image)
  - [Person Verification Task- Rejected Image](#person-verification-task-rejected-image)
  - [Communication For Veteran](#communication-for-veteran)
- [Troubleshooting](#troubleshooting)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this User Guide is to provide information and a detailed walkthrough of processing a Veteran Health Identification Card request submitted by the veteran through the VA Access Self-Service application.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Guide is divided into six sections for quick access to information needed.

The first section will provide an overview of what a VHIC is and what the eligibility requirements are, and the various user roles and their accessibility within the VHIC application.

To be able to receive a VHIC, a Veteran must meet the following eligibility criteria:

- Be eligible for VA medical benefits
- Be enrolled in the VA Healthcare system
- Be Level 2 proofed at a VA medical facility
- Veteran identity must be recognized in the Master Veteran Index (MPI), which is managed by the Identity and Access Management (IAM) of the VA

<u>NOTE:</u> The level 2 proofing process is a method to verify the identity of Veterans. VA requires Veterans to provide approved identification documents to access Personal Identifiable Information (PII), Personal Health Information (PHI) and request a Veterans Health Identification Card (VHIC).

The second and third sections will explain system requirements and log in instructions

The fourth section review and discuss the information found on the VHIC Menu/Home page.

The fifth section will give the user step-by-step details of how to complete the Identity Proofing process for a Veteran that has submitted a VHIC Card request remotely. The VHIC user must verify the Veteran’s Identity Proofing Level is at Level 2 in the Identity Management Toolkit.

The last section covers some troubleshooting issues and solutions that will help the VHIC user to better able to support the Veteran and ensure that the VHIC requests are processed properly.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide has been written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system such as:
  - How to log in
  - The use of commands
  - Menu options
  - Navigation tools
- User has an understanding of the roles within VHIC
- User has been provided the appropriate active roles required for the VHIC application.
- User is using *Google Chrome or Microsoft Edge* to do their job of either Creating a VHIC Card Request, Running Reports, or Managing VHICs depending on user roles.
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

- Descriptive text is presented in a proportional font (as represented by this font).
- “Screenshots” of computer online displays (i.e., character-based screen captures/dialogs) and are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be \[boldface\] type and enclosed in brackets.

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The support contact information documented herein is intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The following table lists the contact information needed by site users for troubleshooting purposes. Support contacts are listed by description of the incident escalation and contact information (phone number and options to select).

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
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

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# Self-Service VHIC Card Request – What is it?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC Self-Service Application was created to allow Veterans to request VHIC card(s) without having to visit their local facilities offering them convenience and safely limiting exposure to Covid 19. VHIC users will be responsible for monitoring and processing new card requests submitted through the Self-Service Tool. Self-Service New Card Requests require remote veteran proofing the process will be outlined in this user guide.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing the VHIC Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Single Sign-On Internal (SSOi)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHIC is a web-based application that users will access via a web browser. The recommended browser is *Google Chrome or Microsoft Edge*.

The VHIC URL is REDACTED and is case sensitive – it must be entered exactly as shown. After successfully logging in to the VHIC application, users should bookmark this site for easy access in the future.

Users will be presented with the Single Sign On – internal (SSOi) login screen (*shown below*).

Here the VHIC user will need to use their PIV card to log into the VHIC application.

<span id="_Toc166070673" class="anchor"></span>Figure 1. SSOi Login Screen

![](vhic-4-29-user-guide-vol-6-self-service-processing/002.png)

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC application is built to accommodate a specific set of pre-established user roles. During the provisioning process, the VHIC user will have a role assigned to them, which will determine what aspects of the VHIC application are available to them. For more information on the areas of access that accompanies each role, please refer to VHIC Roles and Access document.

Depending on the VHIC users’ role, they will be presented different Home screens upon logging into the VHIC application.

## Accessing the Identity Management Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Accessing the Identity Management Toolkit Directly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC user will need to go to the Identity Management Toolkit application to look up the Veteran and verify their proofing level and if needed complete the proofing process.

The Identity Management Toolkit can be accessed by using the URL in the next section entitled “SSOi.”

SSOi: <span id="_Toc166070674" class="anchor"></span>REDACTED

Figure 2. Identity Management Toolkit SSOi Logon Screen

![](vhic-4-29-user-guide-vol-6-self-service-processing/003.png)

The URLs are case sensitive – they must be entered exactly as shown. After successfully logging into the Identity Management Toolkit application, users should bookmark this site for easy access in the future. Instructions on how to do just that can be found REDACTED.

The best time to bookmark the site is after the user is in the application itself rather than attempting to bookmark the Login screen.

### Accessing Identity Management Toolkit from within the VHIC Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Step 1 of the VHIC Card Request 

When the VHIC user starts the Card Request process, they will see a message on Step 1: Enter Search Terms. “IMPORTANT: Have you Identity Proofed the Veteran in Identity Management Toolkit? (Click here to openREDACTEDin another window)”

The VHIC user can click on the blue words REDACTED which is a hyperlink that will take the user to the Identity Management Toolkit application.

<span id="_Toc166070675" class="anchor"></span>Figure 3. Step 1: Enter Search Terms with Identity Management Toolkit hyperlink

![](vhic-4-29-user-guide-vol-6-self-service-processing/004.png)

#### Veteran Link in Assigned Self Service Requests for Manual Review List

Selecting the Full Name link from the Assigned Request list will open the Toolkit directly to the 1998 Person Verification \[Self-Service\] Task.

<span id="_Toc166070676" class="anchor"></span>Figure 4. Veteran Link to MPI Toolkit Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/005.png)

<u>NOTE:</u> If the Veteran has a Preferred Name on file it will appear within parenthesis where the <u>Full Name</u> appears as seen below.

<span id="_Toc166070677" class="anchor"></span>Figure 5. Veteran Link to MPI Toolkit Task with Preferred Name

![](vhic-4-29-user-guide-vol-6-self-service-processing/006.png)

<span id="_Toc166070678" class="anchor"></span>Figure 6. MPI Toolkit Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/007.png)

# VHIC Application Home Page 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VHIC System Status Banner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VHIC System will display a Status Banner at the top of the screen to notify users of reported issues with the system and/or during maintenance activities that do not require downtime such as high volume or preferred browser reminder.

<span id="_Toc166070679" class="anchor"></span>Figure 7. VHIC System Banner Page

REDACTED

## VHIC Self-Service Request Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the VHIC User logs into the VHIC Application, they will see Self-Service request information for their facility listed on the Home page.

This information includes:

1.  The number of facility specific requests that have been submitted through the Self-Service Application for that have not been assigned to a proofer for review.
2.  The number of requests that the user has assigned to them
3.  The number of requests that are in an ON HOLD status that will expire within seven days.

<span id="_Toc166070680" class="anchor"></span>Figure 8. Self Service Request Notifications

![](vhic-4-29-user-guide-vol-6-self-service-processing/008.png)

## Viewing Self Service New Card Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Self-Service request information listed on the Home screen serves as a link to review the New Card Requests.

### View Unassigned Requests by VISN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking on the VISN Unassigned Card Request message will direct the user to the list of requests that need to be assigned to a Proofer within their VISN

<span id="_Toc166070681" class="anchor"></span>Figure 9. Link to View Self Service Requests by VISN

![](vhic-4-29-user-guide-vol-6-self-service-processing/009.png)

<span id="_Toc166070682" class="anchor"></span>Figure 10. List of Requests Submitted by VISN

![](vhic-4-29-user-guide-vol-6-self-service-processing/010.png)

Users with the appropriate access will have the ability to view and filter the unassigned lists of other VISNs by selecting the VISN from the dropdown list.

<span id="_Toc166070683" class="anchor"></span>Figure 11. Unassigned Self-Service Requests by VISN, additional VISN Selection List

![](vhic-4-29-user-guide-vol-6-self-service-processing/011.png)

After selecting the desired facility from the dropdown, click the filter button to see the list of unassigned requests from that VISN

<span id="_Toc166070684" class="anchor"></span>Figure 12. List of Unassigned Requests by Chosen VISN

![](vhic-4-29-user-guide-vol-6-self-service-processing/012.png)

### View Unassigned Requests by Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking on the Facility Unassigned Card Request message will direct the user to the list of facility requests that need to be assigned to a Proofer.

<span id="_Toc166070685" class="anchor"></span>Figure 13. Facility Unassigned Request Information

![](vhic-4-29-user-guide-vol-6-self-service-processing/013.png)

A list of unassigned requests will be displayed offering the following details:

- Photograph currently on file in the system
- Full Name
- Card ID
- ICN
- Hold Date
- Hold Reason(s)

Selecting the Veteran Name Link will assign the request to the user.

<span id="_Toc166070686" class="anchor"></span>Figure 14. Unassigned Self-Service Requests for Manual Review

![](vhic-4-29-user-guide-vol-6-self-service-processing/014.png)

The user will be able to see the updated number of requests in their queue on the home page.

<span id="_Toc166070687" class="anchor"></span>Figure 15. Request Information Changed

![](vhic-4-29-user-guide-vol-6-self-service-processing/015.png)

### Assigned Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking on the Assigned Card Request message will direct the user to the list of facility requests assigned to them for proofing.

<span id="_Toc166070688" class="anchor"></span>Figure 16. Assigned Request Information

![](vhic-4-29-user-guide-vol-6-self-service-processing/016.png)

The list of assigned requests will be displayed offering the following details:

- Photograph currently on file in the system
- Full Name
- Card ID
- ICN
- Hold Date
- Hold Reason(s)

<span id="_Toc166070689" class="anchor"></span>Figure 17. Assigned Self-Service Requests for Manual Review

![](vhic-4-29-user-guide-vol-6-self-service-processing/017.png)

<u>NOTE:</u> If the Veteran has a Preferred Name on file it will appear within parenthesis where the Full Name appears as seen below.

<span id="_Toc166070690" class="anchor"></span>Figure 18. Assigned Self-Service Requests for Manual Review with Preferred Name

![](vhic-4-29-user-guide-vol-6-self-service-processing/018.png)

When the user is ready to review the request(s) the Proofer will need to access the Toolkit through one of the methods listed in *Section 3.3 Accessing the Identity Management Toolkit*. Once Toolkit access has been established, selecting the Veteran Name link will open a new window giving the VHIC user access to the new Proofing Task in the Toolkit.

# Self Service Request Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new 1998 Person Verification \[Self-Service\] Task is created in the Toolkit to proof veterans that have submitted VHIC card requests through the VA Access application. These requests will fall under two categories based on manual review performed by the VHIC User.

- Accepted Image
- Rejected Image

Reviewing a card request submitted thru VHIC Self Service requires the user to review the proofing document and photo submitted by the veteran. If either artifact does not meet required standards, then follow the steps outlined under Rejected Image. If both artifacts meet required standards, then follow the steps outlined under Accepted Image.

## Person Verification Task- Accepted Image 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Full Name link from the Assigned Request list will open the 1998 Person Verification \[Self-Service\] Task.

<span id="_Toc166070691" class="anchor"></span>Figure 19. Link to Person Verification Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/019.png)

To process:

1.  Select the Task Number to open the Task for review.

<span id="_Toc166070692" class="anchor"></span>Figure 20. Select Task Number

![](vhic-4-29-user-guide-vol-6-self-service-processing/020.png)

4.  The Proofer will need to navigate to the Task Notes tab to assign the Task to themselves.

<span id="_Toc166070693" class="anchor"></span>Figure 21. Task Notes Tab

![](vhic-4-29-user-guide-vol-6-self-service-processing/021.png)

<span id="_Toc166070694" class="anchor"></span>Figure 22. Assign Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/022.png)

5.  After assigning the Task they will open to Task Details Tab, then Select Person Verification Tab to process the Task

<span id="_Toc166070695" class="anchor"></span>Figure 23. Figure 23. Person Verification Task Details

![](vhic-4-29-user-guide-vol-6-self-service-processing/023.png)

6.  The Person Verification tab will open to the Data Review section of the Task. The Data Review tab of the Person Verification Tool is used to verify the identity traits and/or document changes to the traits. To verify traits, the Proofer will need to view the identification submitted by the Veteran.
7.  The Identification can be found on the Self-Service Images tab.

<span id="_Toc166070696" class="anchor"></span>Figure 24. Person Verification Data Review Screen

![](vhic-4-29-user-guide-vol-6-self-service-processing/024.png)

8.  On the Self-Service Images tab, click Person Verification Document link (s) to open the submitted images for review. The documents will open in a separate window. Review the Proofing Document(s) and return to the Data Review tab

<span id="_Toc166070697" class="anchor"></span>Figure 25. Self Service Images Tab

![](vhic-4-29-user-guide-vol-6-self-service-processing/025.png)

9.  The MPI Value column will contain Primary View data. Verify matching traits by checking the corresponding check box in the Verify column. The target trait will highlight green. Click the Submit button after trait verification.

<span id="_Toc166070698" class="anchor"></span>Figure 26. Data Review Tab Verify Traits

![](vhic-4-29-user-guide-vol-6-self-service-processing/026.png)

10. The Proofer will return to the Self-Service Image tab once the Traits are verified. The Data Review tab now shows a check mark indicating that section is complete. Here the Proofer can Accept or Reject the uploaded image based on acceptability criteria.

<span id="_Toc166070699" class="anchor"></span>Figure 27. Accept Veteran Submitted Image

![](vhic-4-29-user-guide-vol-6-self-service-processing/027.png)

<u>NOTE:</u> The Veteran is informed during the Request Process that if a trait needs to be modified (for example, Last Name changes), they must come into the facility. If the Veteran submits a request under the following conditions:

- Photo submitted is not acceptable
- Verification document uploaded is not acceptable
- Identification traits do not match

The POC will need to make a note under the Task Notes Tab and continue through the *Person Verification Task- Rejected Image in Section 5.2.*

11. After accepting the uploaded image, the task will progress. The Self-Service Images tab will now show a check mark. and the Proofer will move to the Documentation tab.

<span id="_Toc166070700" class="anchor"></span>Figure 28. Documentation Tab

![](vhic-4-29-user-guide-vol-6-self-service-processing/028.png)

12. The Proofer will select the documentation type submitted from the list of acceptable documents and click Submit.

<span id="_Toc166070701" class="anchor"></span>Figure 29. Submit Document Details

![](vhic-4-29-user-guide-vol-6-self-service-processing/029.png)

13. A pop-up box will show that the task has been completed. Select OK button.

<span id="_Toc166070702" class="anchor"></span>Figure 30. Select OK Button

![](vhic-4-29-user-guide-vol-6-self-service-processing/030.png)

Documentation Requirements Met, Check Marks indicate that all Proofing Tasks have been Completed

<span id="_Toc166070703" class="anchor"></span>Figure 31. Task Competed

![](vhic-4-29-user-guide-vol-6-self-service-processing/031.png)

14. Once the Task is completed, the POC will need to go back to the Task Notes tab and mark it as Resolved.

<span id="_Toc166070704" class="anchor"></span>Figure 32. Add Task Notes

![](vhic-4-29-user-guide-vol-6-self-service-processing/032.png)

From the Primary View the user can confirm that the LOA Changed to 2

<span id="_Toc166070705" class="anchor"></span>Figure 33. LOA Changed

![](vhic-4-29-user-guide-vol-6-self-service-processing/033.png)

From the Correlations tab the user can confirm that the Proofing Correlation Added

<span id="_Toc166070706" class="anchor"></span>Figure 34. Proofing Correlation Added

![](vhic-4-29-user-guide-vol-6-self-service-processing/034.png)

## Person Verification Task- Rejected Image 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Processing a Person Verification Task when the Veteran has submitted an unacceptable image follows the same process outlined above, until the Proofer reaches the Self-Service Images approval page.

1.  The VHIC Proofer will select the Full Name link from the Assigned Request list, which will open a window into the MPI Toolkit 1998 Person Verification \[Self-Service\] Task.

<span id="_Toc166070707" class="anchor"></span>Figure 35. Link to Toolkit Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/035.png)

15. To review, click on the 1998-Person verification \[Self Service\] Task hyperlink.

<span id="_Toc166070708" class="anchor"></span>Figure 36. MPI Toolkit Task Number Link

![](vhic-4-29-user-guide-vol-6-self-service-processing/036.png)

The Task Details page will open

<span id="_Toc166070709" class="anchor"></span>Figure 37. New Person Verification Task Details

![](vhic-4-29-user-guide-vol-6-self-service-processing/037.png)

16. The Proofer will assign the Task to themselves on the Task Notes tab.

<span id="_Toc166070710" class="anchor"></span>Figure 38. Assign Task

![](vhic-4-29-user-guide-vol-6-self-service-processing/038.png)

17. After assigning the Task they will open to Task Details Tab, then Select Person Verification Tab to process the Task

On the Task Details Screen, the user will need to click on the Person Verification tab to continue the Proofing Task.

<span id="_Toc166070711" class="anchor"></span>Figure 39. Select Person Verification Tab

![](vhic-4-29-user-guide-vol-6-self-service-processing/039.png)

18. The Person Verification tab will open to the Data Review section of the Task. The Data Review tab of the Person Verification Tool is used to verify the identity traits and/or document changes to the traits. To verify traits, the Proofer will need to view the identification submitted by the Veteran.
19. The Identification can be found on the Self-Service Images tab.

<span id="_Toc166070712" class="anchor"></span>Figure 40. Select Self-Service Images Tab

![](vhic-4-29-user-guide-vol-6-self-service-processing/040.png)

20. On the Self-Service Images tab, clicking the Proofing Verification Document link will cause a separate window to open showing the supporting documentation the Veteran uploaded for the request.

<span id="_Toc166070713" class="anchor"></span>Figure 41. Compare Veteran Images

![](vhic-4-29-user-guide-vol-6-self-service-processing/041.png)

21. Upon review if the images do not match, or if they fall under any other rejection reason, the user will select the ![](vhic-4-29-user-guide-vol-6-self-service-processing/042.png)button. This will open the drop-down list of rejection reasons. VHIC Proofers will mark all check boxes that apply.

<span id="_Toc166070714" class="anchor"></span>Figure 42. Rejection Reason Menu

![](vhic-4-29-user-guide-vol-6-self-service-processing/043.png)

<u>NOTE:</u> Rejection reasons can include:

- Altered photo
- Does not meet Facial Requirements
- Expired Proofing Document
- Glasses or Electronics (i.e., Ear Pods, etc. not allowed)
- Missing Photo
- Non-Solid Light-Colored Background
- Phot of an ID
- Picture of a picture
- Unacceptable Proofing Document
- Unauthorized Head Gear/Attire
- Use of Filters
22. With the reasons selected, click the Reject Image button.

<span id="_Toc166070715" class="anchor"></span>Figure 43. Select Reject Image Button

![](vhic-4-29-user-guide-vol-6-self-service-processing/044.png)

23. A pop up will appear to confirm the rejection. Select OK to confirm. Confirming the image rejection, the Proofing Task will auto-resolve and cancel the request.

<span id="_Toc166070716" class="anchor"></span>Figure 44. Reject/Resolve Confirmation Message

![](vhic-4-29-user-guide-vol-6-self-service-processing/045.png)

Auto resolved tasks will go to Task Details tab instead of staying on the Person Verification Tab. Navigating to the Task Notes tab will show the Task Status as Resolved and will show the system generated notes showing the reason(s) for rejection.

<span id="_Toc166070717" class="anchor"></span>Figure 45. Resolved Task Status

![](vhic-4-29-user-guide-vol-6-self-service-processing/046.png)

The LOA on the Primary View will remain at 1

<span id="_Toc166070718" class="anchor"></span>Figure 46. Level of Assurance Does Not Change

![](vhic-4-29-user-guide-vol-6-self-service-processing/047.png)

## Communication For Veteran 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran will receive an email indicating that their request was cancelled and direct them to come into their nearest facility to resolve any issues that may keep them from qualifying for a VHIC card.

Examples of these emails are:

- The card request was cancelled due to review issues such as a bad photo, unacceptable documents submitted, etc.

<span id="_Toc166070719" class="anchor"></span>Figure 47. Request Cancellation Review Issue

REDACTED

- The card request was cancelled due to other reasons such as 30-day timeout.

<span id="_Toc166070720" class="anchor"></span>Figure 48. Request Cancellation Email Timed Out

REDACTED

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a through set of troubleshooting guidelines, please refer to the *Veteran Health Identification Card User Guide - Volume 4 - Troubleshooting* document.