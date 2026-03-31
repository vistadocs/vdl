---
title: Enterprise Precision Scanning and Indexing (EPSI) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Enterprise Precision Scanning and Indexing (EPSI)
app_code: EPSI
app_name: Enterprise Precision Scanning and Indexing
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - epsi
  - span
  - class
  - indexing
  - table
  - anchor
  - guide
  - enterprise
  - figure
  - precision
page_count: 0
word_count: 20234
section_count: 23
table_count: 5
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Enterprise_Precision_Scanning_and_Indexing_(EPSI)/epsi_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Enterprise_Precision_Scanning_and_Indexing_(EPSI)/epsi_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=431"
---

---
title: |
  <span id="_Hlk123219928" class="anchor"></span>Enterprise Precision Scanning and Indexing (EPSI)

  Software Version 1.49

  User Guide
---

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/001.png)

February 2026

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc222734410" class="anchor"></span>Table 1: Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 61%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/24/2026</td>
<td>5.3</td>
<td><p>Updates made to align with system improvements in EPSI v1.49:</p>
<p>Added figures and instructions to reflect newly added ability for users to update their default time zone (User Preferences).</p></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>10/01/2025</td>
<td>5.2</td>
<td><p>Updates made to align with system improvements in EPSI v1.45.0:</p>
<ul>
<li><p>Replaced figures and added additional detail to reflect new minimal click indexing feature and AI summary functionality.</p></li>
<li><p>Edited sections and removed duplicate content to enhance user workflow efficiency and usage of this document.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/17/2025</td>
<td>5.1</td>
<td><p>Updates made to align with system improvements in EPSI v1.36.0 and v1.37.0:</p>
<ul>
<li><p>Replaced figures and added additional detail to reflect new workflow for Indexers working with Administrative documents.</p></li>
<li><p>Figures updated to reflect newly required Comments field for RFS Nurse transfers.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>05/20/2025</td>
<td>5.0</td>
<td><p>Updates made to align with system improvements in EPSI v1.35.0:</p>
<p>Replaced figures and added instructions to reflect newly added ability for Indexer and Nurse roles to view additional details for Existing Notes.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>05/06/2025</td>
<td>4.9</td>
<td><p>Updates made to align with system improvements in EPSI v1.34.0:</p>
<ul>
<li><p>Replaced figures and added additional detail to reflect new functionality providing the ability to refresh Consult and Note Title lists.</p></li>
<li><p>Replaced figures to reflect the addition of the VA email address as a username identifier in Reports.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>04/01/2025</td>
<td>4.8</td>
<td><p>Updates made to align with system improvements in EPSI v1.32.0:</p>
<p>Replaced figures throughout the document to reflect updated verbiage in the data retention banner.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>03/18/2025</td>
<td>4.7</td>
<td><p>Updates made to reflect changes to EPSI v1.31.0:</p>
<p>Replaced figures throughout the document to reflect UI changes and new functionality: Added additional messaging for users to verify the indexing information saved from a document transfer before final indexing.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>10/15/2024</td>
<td>4.6</td>
<td><p>Updates made to reflect changes to EPSI v1.28.0:</p>
<ul>
<li><p>Replaced figures throughout the document to reflect new functionality and system improvements:</p>
<ul>
<li><p>Care Queue Transfer information displays source of and reasons for transfer, comments, and related transfer detail.</p></li>
<li><p>UI updates for behaviors of <strong>Add a New Addendum</strong> and <strong>Needs Clinical Review</strong> checkboxes.</p></li>
<li><p>QA Detailed Auditing Export report now contains fields displaying consult information.</p></li>
</ul></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>09/24/2024</td>
<td>4.5</td>
<td><p>Updates made to reflect changes to EPSI v1.27.0:</p>
<ul>
<li><p>Replaced figures and updated instructions to reflect new functionality:</p>
<ul>
<li><p>Added ability to select Parent Note or Addendum when indexing a document.</p></li>
<li><p>Added additional information on selected veteran to Upload Queue table.</p></li>
<li><p>Added Indexer name to the Care Queue document view.</p></li>
<li><p>Added ability to transfer documents from the 'Care Queue.</p></li>
</ul></li>
<li><p>Replaced figure to reflect system improvement: Added a file size validation check to the <strong>Add Files</strong> workflow.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/27/2024</td>
<td>4.4</td>
<td>Updated Revision History to reflect prior changes made to Section 4.7.3-Internal Transfer Workflow; updated document title and footers to reflect EPSI v1.25.0 release.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>07/30/2024</td>
<td>4.3</td>
<td><p>Updates made to reflect changes to EPSI v1.23.0:</p>
<ul>
<li><p>Replaced figures in Sections 4.2.3 and 4.3.2.3 to reflect updated functionality: Display and enable editing of Origin, Type, Specialty, and Procedure fields in Existing Note workflow.</p></li>
<li><p>Added note and figure to Section 3.3 to reflect new Timeout Notification feature.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>07/09/2024</td>
<td>4.2</td>
<td><p>Updates made to reflect changes to EPSI v1.22.0:</p>
<ul>
<li><p>Added Section 4.9.6 to reflect new functionality: System updated to include a <strong>Documents Removed by User</strong> report.</p></li>
<li><p>Updated instructions in Section 4.7.3. to reflect new functionality and updated UI for Enhanced Admin Transfer.</p></li>
<li><p>Updated multiple figures within the document to reflect the new functionality and system improvements: Updated labels for indexing steps in the user interface and new columns added to Document Status table.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/18/2024</td>
<td>4.1</td>
<td><p>Updates made to reflect changes to EPSI v1.21.0:</p>
<ul>
<li><p>Added new Section 4.9.3 and updated figures within the document to reflect new functionality: Updated user interface to include a <strong>Problem Documents in Queue Detailed</strong> report.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>06/04/2024</td>
<td>4.0</td>
<td><p>Updates made to reflect changes to EPSI v1.20.0:</p>
<ul>
<li><p>Sections 3.2.6. and 4.10: Added instructions and updated figures to reflect new functionality: Time zone drop-down menu added to Status page.</p></li>
<li><p>Section 4.9.4: Updated Figure 265 to reflect system improvement: Additional column for <strong>VistA Image ID</strong> added to the QA Detailed Auditing Export report.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>05/07/2024</td>
<td>3.9</td>
<td><p>Updates made to reflect changes to EPSI v1.18.0:</p>
<ul>
<li><p>Added additional document details (Veteran DOB and Identifier) in Section 4.6.1: Reviewing Files.</p></li>
<li><p>Replaced figures throughout the document to accurately reflect the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>04/23/2024</td>
<td>3.8</td>
<td><p>Updates made to reflect changes to EPSI v1.17.0:</p>
<ul>
<li><p>Added Section 4.1.1.2.: Viewing File Pages.</p></li>
<li><p>Added Section 4.1.3.1.: Deleting File Pages.</p></li>
<li><p>Updated process steps as well as multiple figures throughout the document to reflect changes made to the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>04/02/2024</td>
<td>3.7</td>
<td><p>Updates made to fix process order errors, remove outdated information and other edits made to correct text and style formatting throughout the document.</p>
<ul>
<li><p>Added Section 3.2.8: Additional Information.</p></li>
<li><p>Added Section 4.2.1.1: EPSI Automation Functions.</p></li>
<li><p>Removed Appendix D: Submitting a YourIT Ticket and Appendix E: How to Update User Accounts.</p></li>
<li><p>Updated figures throughout the document for better readability for the user.</p></li>
<li><p>Updated Table 6: Facility File Name Structures to reflect changes to EPSI v1.16.0.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>02/20/2024</td>
<td>3.6</td>
<td><p>Updates made to reflect changes to EPSI v1.13.0:</p>
<ul>
<li><p>Section 4.1.6. Updated text to reflect new functionality: Users can now transfer a merged file to another user.</p></li>
<li><p>Section 4.9.4. Updated Figure 244 to reflect system improvement: Additional columns for 'Date Audited' and 'Reviewer Note' added to the QA Detailed Export Report.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>02/06/2024</td>
<td>3.5</td>
<td><p>Updates made to reflect changes to EPSI v1.12.0:</p>
<ul>
<li><p>Section 2.2. Updated Figure 3 to reflect updated data flow.</p></li>
<li><p>Section 4.3.1. Updated Figures 106 – 109 to reflect new feature: Added ability to search Nurse Care Queue by document name.</p></li>
<li><p>Section 4.6.1. Updated Figures 178 and 179. Included reference to new feature: Added ability to filter out reviewed documents in QA review queue.</p></li>
<li><p>Updated Administrator role description in Sections 3.3.5 and 4.7.</p></li>
<li><p>Multiple text edits and formatting adjustments made to ensure compliance with Section 508 guidelines including:</p>
<ul>
<li><p>Addition of sections 4.1.4.1 and 4.1.4.2 to prioritize the accessible method of rearranging files; added Figures 33 – 35.</p></li>
</ul></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>01/23/2024</td>
<td>3.4</td>
<td>Minor edits made to correct text formatting in Section 4.3 and the alignment of Figure 58. Corrected table formatting in Appendix A and added alt-text to Figures 56 - 58, 71, 125, 178, 179, 202, and 240.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>01/03/2024</td>
<td>3.3</td>
<td>Update made to provide additional detail in Section 4.6.1.- Reviewing Files. Added new image to step 6 as figure 179: Reasons for Failure.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>12/19/2023</td>
<td>3.2</td>
<td><p>Updates made to reflect changes to EPSI v1.9.0:</p>
<ul>
<li><p>Section 1.2.2 Assumptions added a bullet detailing the screen resolution requirement.</p></li>
<li><p>Section 4.2.3. Adding Patient Documents to Existing Notes added note after step 5 to reflect limited scope of existing notes to 24 months.</p></li>
<li><p>Section 4.3.2.3. Adding Patient Documents to Existing Notes added note after step 8 to reflect limited scope of existing notes to 24 months.</p></li>
<li><p>Section 4.6.1. Reviewing Files: updated figure 178: Reviewing a Document to reflect changes to default state of the Pass/Fail Review option.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>12/04/2023</td>
<td>3.1</td>
<td>Updates made to reflect changes to EPSI v1.7.0 and 1.8.0.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>11/14/2023</td>
<td>3.0</td>
<td>Updates made to reflect changes with EPSI Intelligence Document Processing features.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>11/06/2023</td>
<td>2.9</td>
<td>Updates made to reflect changes to EPSI v1.5.0 and 1.6.0.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>09/18/2023</td>
<td>2.8</td>
<td>Updates made to reflect changes to EPSI v1.4.0.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>09/05/2023</td>
<td>2.7</td>
<td>Updates made to reflect changes to EPSI v1.3.10.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/21/2023</td>
<td>2.6</td>
<td>Updates made to reflect changes to EPSI v1.3.9. Added section for responding to site-related errors. Added Appendix D: Submitting a YourIT Ticket. Added Appendix E: How to Update User Access in IAM.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>08/07/2023</td>
<td>2.5</td>
<td>Updates made to reflect changes to EPSI v1.3.8. Added Appendix C: Facility File Name Structures.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>7/21/2023</td>
<td>2.4</td>
<td>Updates made to reflect changes to EPSI v1.3.7.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>07/10/2023</td>
<td>2.3</td>
<td>Updates made to reflect changes to EPSI v1.3.6. Added Duplicate Files section. Moved appendices to new Troubleshooting section.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>06/20/2023</td>
<td>2.2</td>
<td>Updates made to reflect changes to EPSI v1.3.5.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/05/2023</td>
<td>2.1</td>
<td>Updates made to reflect changes to EPSI v1.3.4.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>05/22/2023</td>
<td>2.0</td>
<td>Changes made for v1.3.2 and v1.3.3. Added Appendix D. Updated steps for Registering for EPSI. Moved Managing Files to section 4.1 and renamed. Moved Uploading Files from Indexer sections to 4.1.1 and removed redundant uploading instructions throughout. Added sections for Rotating File Pages and Reports. Removed redundant Searching for Files section.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>04/24/2023</td>
<td>1.9</td>
<td>Updates made to reflect changes to EPSI 1.3.0 and 1.3.1.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>03/20/2023</td>
<td>1.8</td>
<td>Updates made to reflect changes to EPSI 1.2.10.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>03/06/2023</td>
<td>1.7</td>
<td>Updates made to reflect changes to EPSI v1.2.8 and 1.2.9.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>02/06/2023</td>
<td>1.6</td>
<td>Updates made to reflect changes to EPSI v1.2.7.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>01/27/2023</td>
<td>1.5</td>
<td>Updates made to reflect changes to EPSI v1.2.6.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>01/09/2023</td>
<td>1.4</td>
<td>Updated screenshots to reflect changes to user interface to reflect 1.2.5. Added <strong>Registering for EPSI</strong> section. Added acronyms to Appendix A. Added note to Introduction. Made minor changes to language throughout to increase clarity. Removed Help section (3.2.7) since Help feature is not currently usable.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>11/21/2022</td>
<td>1.3</td>
<td>Updates made to reflect changes to EPSI v1.2.0.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>11/07/2022</td>
<td>1.2</td>
<td>Updates made to reflect changes to EPSI v1.1.1.</td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>10/24/2022</td>
<td>1.1</td>
<td>Updates made to reflect changes to EPSI v1.1.0.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/05/2022</td>
<td>1.0</td>
<td>Initial Release.</td>
<td>VetsEZ</td>
</tr>
</tbody>
</table>

<span id="_Toc222734410" class="anchor"></span>Table 1: Documentation Symbols and Descriptions

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

List of Figures

List of Tables

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
    - [References and Resources](#references-and-resources)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Roles](#user-roles)
  - [Continuity of Operations](#continuity-of-operations)
  - [Data Retention Policy](#data-retention-policy)
  - [Duplicate Files](#duplicate-files)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
    - [Indexer](#indexer)
    - [Nurse](#nurse)
    - [Quality Assurance](#quality-assurance)
    - [Administrator](#administrator)
    - [Reports](#reports)
    - [Status](#status)
    - [Build Information](#build-information)
    - [Additional Information](#additional-information)
    - [Upload Queue](#upload-queue)
    - [User Preferences](#user-preferences)
    - [Current Site](#current-site)
  - [Logging Out](#logging-out)
- [Using the Software](#using-the-software)
  - [Preparing and Managing Files](#preparing-and-managing-files)
    - [Uploading Files](#uploading-files)
    - [Sorting Files](#sorting-files)
    - [Splitting Files](#splitting-files)
    - [Rearranging File Pages](#rearranging-file-pages)
    - [Removing Files](#removing-files)
    - [Merging Files](#merging-files)
    - [Unmerging Files](#unmerging-files)
    - [Rotating File Pages](#rotating-file-pages)
  - [Indexing Files](#indexing-files)
    - [Indexing a Consult / Referral Workflow](#indexing-a-consult-referral-workflow)
    - [Indexing New Notes Workflow](#indexing-new-notes-workflow)
    - [Indexing Existing Notes Workflow](#indexing-existing-notes-workflow)
    - [Indexing Administrative Documents Workflow](#indexing-administrative-documents-workflow)
  - [Transferring Files](#transferring-files)
  - [Reviewing Files (Clinical Review)](#reviewing-files-clinical-review)
    - [Create AI Summary](#create-ai-summary)
  - [Working with Problem Documents](#working-with-problem-documents)
    - [Replacing Files](#replacing-files)
    - [Missing RFS Signatures](#missing-rfs-signatures)
  - [Quality Assurance Functions](#quality-assurance-functions)
    - [Reviewing Files](#reviewing-files)
  - [Administrator Functions](#administrator-functions)
    - [Consult Notes](#consult-notes)
    - [User Administration Page](#user-administration-page)
    - [Internal Transfer Workflow](#internal-transfer-workflow)
    - [Document Status Page](#document-status-page)
    - [Files can be located by reviewing each page of the file list, entering the file name in the Search by File Name field, or entering a date in the Created or Last Modified fields. Filter by user via the User drop-down menu or by file status via the Status drop-down menu.To remove any search or filter, select the CLEAR button.Exporting Tables Workflow](#files-can-be-located-by-reviewing-each-page-of-the-file-list-entering-the-file-name-in-the-search-by-file-name-field-or-entering-a-date-in-the-created-or-last-modified-fields-filter-by-user-via-the-user-drop-down-menu-or-by-file-status-via-the-status-drop-down-menuto-remove-any-search-or-filter-select-the-clear-buttonexporting-tables-workflow)
  - [Reports](#reports-1)
    - [Documents Indexed by User](#documents-indexed-by-user)
    - [Problem Documents in Queue](#problem-documents-in-queue)
    - [Problem Documents in Queue Detailed Export](#problem-documents-in-queue-detailed-export)
    - [QA Total Files Audited](#qa-total-files-audited)
    - [QA Detailed Auditing Export](#qa-detailed-auditing-export)
    - [Documents Removed by User](#documents-removed-by-user)
    - [Exporting and Printing Reports](#exporting-and-printing-reports)
  - [Status](#status-1)
    - [Checking Current Processing Status](#checking-current-processing-status)
    - [Exporting Document Status Table](#exporting-document-status-table)
  - [Troubleshooting and Common Errors](#troubleshooting-and-common-errors)
    - [EPSI Registration Issues](#epsi-registration-issues)
    - [VistA Upload Errors](#vista-upload-errors)
    - [Token Errors](#token-errors)
- [| Acronym   | Definition                                                      |](#acronym-definition)
- [# | Status                                                                 | Explanation                                                                                                                                                                                                                       |](#status-explanation)
- [<span id="Toc222734214" class="anchor"></span>Appendix C: Facility File Name StructuresWhen documents are uploaded into EPSI, if the file name follows a specific structure, the application will automatically detect patient or consult information. Any information extracted from the file name will auto-populate into the appropriate field. For example, if a patient name is detected, EPSI will generate search results based on the file name structure specific to that facility.](#span-idtoc222734214-classanchorspanappendix-c-facility-file-name-structureswhen-documents-are-uploaded-into-epsi-if-the-file-name-follows-a-specific-structure-the-application-will-automatically-detect-patient-or-consult-information-any-information-extracted-from-the-file-name-will-auto-populate-into-the-appropriate-field-for-example-if-a-patient-name-is-detected-epsi-will-generate-search-results-based-on-the-file-name-structure-specific-to-that-facility)
Enterprise Precision Scanning and Indexing (EPSI) is a collection of processes and automation tools used for indexing and storing documents received from Integrated Veteran Care (IVC) Community Care (CC) providers.
- Indexing involves associating the scanned portable document format (PDF) image document with the patient and consult that triggered the patient’s consult with the IVC provider.
- Storing is the process of sending the document to Veterans Health Information Systems and Technology Architecture (VistA) Imaging.
The scanned Veteran documents arrive via fax and are converted into PDF image documents. The user copies the Veteran documents from their computer system into EPSI.
1.  All documents processed by the EPSI application are in PDF format.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide simple and comprehensive instructions for using the EPSI user interface (UI) screens.

Access to each UI in EPSI is aligned with user roles and responsibilities. Some features included in this User Guide will not be visible or available to all users. Access requests will be routed to the EPSI Product Owner for disposition.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document will explain each screen and all user interface options within the context of an easy-to-understand demonstration data scenario. It is also designed to provide the user with screen-by-screen information on how-to use EPSI.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Section 1:Introduction

This section provides the purpose of this manual, an overview of the EPSI software, project references, and contact information for the user to seek additional information.

- Section 2:System Summary

This section provides a graphical representation of the EPSI data flow and an explanation of EPSI user access levels.

- Section 3:Getting Started

This section provides initial steps to register a user with EPSI, as well as a general walkthrough of the system from initiation through exit, enabling the user to understand the sequence and flow of the system.

- Section 4:Using the Software

This section provides step-by-step instructions for common actions within each user role in EPSI.

- Appendix A: Acronyms and Abbreviations

This section provides a list of acronyms and abbreviations found in this document.

- Appendix B: File Status and Explanations

This section provides a listing of potential file status messages and an explanation for each.

- Appendix C: Facility File Name Structures

This section provides the file name structures for facilities that have been incorporated into EPSI.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- Users have basic knowledge of the Computerized Patient Record System (CPRS) program, such as the use of commands, menu options, and navigation tools, as well as knowledge of importing Community Care (CC) documents into VistA Imaging.
- Users have their VistA header mapped to the site(s) they are requesting access to.
- Users have been provided with the appropriate active roles and access to the EPSI web application.
  - EPSI integrates with the Identity and Access Management (IAM) Provisioning Service which automates the process for creating, approving, granting, and removing system access to VA enterprise applications. Users will be granted access to the ESPI application by their specific site Administrator who is responsible for assigning all user roles via the IAM Provisioning Toolkit.
- Users have completed any prerequisite training on the EPSI web application.
- The screen resolution requirement for using EPSI is 1280 x 768.
  - EPSI may function properly at lower resolutions, but for ease of use, this is the minimal resolution actively tested. The orientation supported is Landscape. For additional legibility of items within the PDF frame, a Zoom button is provided to magnify the contents of uploaded PDF files. Using this Zoom feature will not impact the operation of the layout of other areas of the screen. Using this feature prevents the need for users to adjust the zoom settings of their browser.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code (USC), this software is not subject to copyright protection and is in the public domain. The VA waives all responsibility for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely, provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The inclusion of external hyperlink references in this manual does not constitute endorsement by the VA of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses the following methods to highlight different aspects of the material.

<table>
<caption><p><span id="_Toc222734411" class="anchor"></span>Table 2: RFS Forms</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Symbol</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2">
<li></li>
</ol></td>
<td>Informs the reader of generally useful information related to the topic.</td>
</tr>
<tr class="even">
<td><ol>
<li></li>
</ol></td>
<td><ul>
<li><p>Contain useful information for accomplishing specific tasks.</p></li>
<li><p>Indicates an action or scenario where a user could lose progress on their work.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc222734411" class="anchor"></span>Table 2: RFS Forms

2.  This document contains multiple internal links (e.g., Refer to Section X.X). If you select a link and want to quickly go back to the previous section, select ALT+Left Arrow.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To learn more about CPRS and EPSI, consult the following:

- The VA Software Document Library:
  - [EPSI page](https://www.va.gov/vdl/application.asp?appid=431)
  - CPRS: Consult/Request Tracking
  - Enterprise Precision Scanning and Indexing (EPSI) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues related to EPSI that cannot be resolved by this manual or the site Administrator, please submit a ticket via YourIT.

3.  Add Please Route to EPSI Triage group under the Brief Description of Issue field in the incident ticket.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI is accessed using a secure Internet browser and a secure Virtual Private Network (VPN).

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure displays the EPSI data flow between VistA Imaging and EPSI-Web.

<span id="_Toc126223912" class="anchor"></span>Figure 1: EPSI Data Flow

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/002.png)

## User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four (4) EPSI user roles:

- Indexer: Uploads the documents into EPSI, splits them into new Veteran documents to create a separate file to index, indexes Veteran documents, identifies patients that need clinical review, transfers documents to other EPSI users, and queues documents for upload. Indexers can also check the status of files processed in EPSI and export the document status table to a CSV spreadsheet.
- Nurse: Reviews patient records, indexes documents in need of additional review, transfers documents to other EPSI users, and queues documents for upload. Nurses can also check the status of files processed in EPSI and export the document status table to a CSV spreadsheet.
- Quality Assurance: Reviews documents queued for upload by an Indexer for accuracy. These users can also check the status of files processed in EPSI.
- Administrator: Views user roles, manages consult notes, transfers documents between users, exports consult notes, user access tables, and document status tables, checks the status of files processed in EPSI, and generates/exports/prints user reports.
4.  Multiple roles can be assigned to a user based on the actions they need to complete in EPSI. Some functions included in this User Guide may not be available to users with only one assigned role.

## Continuity of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Affairs Enterprise Cloud (VAEC) handles the Continuity of Operations.

## Data Retention Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI’s data retention policy for Personally Identifiable Information (PII)/Protected Health Information (PHI) is 30 days, starting from when the file is first uploaded into the application. All user queues (e.g., Work Queue, Problem Documents, etc.) will be automatically updated to only show files from the last 30 days. Files uploaded to EPSI will not be retrievable in EPSI after 30 days. A 30-day retention banner is displayed in each tab for all user roles.

<span id="_Toc222734417" class="anchor"></span>Figure 2: Data Retention Policy Banner

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/003.png)

Each item in the file lists across all user roles and queues will display a colored circle next to the file name to indicate the number of days the file will be available in EPSI. A blue circle indicates the file has 20-30 days remaining in EPSI, an orange circle indicates the file has 10-19 days remaining in EPSI, and a red circle indicates the file has zero (0) to nine (9) days remaining in EPSI. The total number of files in the file list is displayed at the top left corner. When the list detail is displayed, the numbers in parentheses indicate how many files in each category are in that file list.

<span id="_Toc222734418" class="anchor"></span>Figure 3: File List Detail Displayed

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/004.png)

Selecting the Hide Detail link at the top right corner of the file list hides this information and enables the Show Detail link.

<span id="_Toc222734419" class="anchor"></span>Figure 4: File List Detail Hidden

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/005.png)

Additionally, if a user moves the cursor over a specific file in a file list, a note stating the number of days remaining until that file will be archived and unavailable in EPSI is displayed.

<span id="_Toc222734420" class="anchor"></span>Figure 5: Remaining Days Example

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/006.png)

## Duplicate Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI is designed to prevent duplicate files within the application and does not allow users to upload an exact copy of a file that already exists in EPSI. Additionally, if a user completes the indexing process within EPSI (i.e., the file is queued for upload to VistA Imaging), a user cannot upload an exact copy of the indexed file into EPSI in the future. This is applicable across all sites and user roles. However, users can re-upload files that were uploaded and then deleted from the application, as this would not create two identical files within EPSI.

3.  Duplicates are not determined by the file name, but by the contents of the file itself. This means that if a file’s contents are modified in any way, the modified file will cease to be a detectable duplicate in EPSI, even if the two file names are identical.

If EPSI detects a user attempting to upload a duplicate file, an error message will display:

<span id="_Toc222734421" class="anchor"></span>Figure 6: Duplicate File Error Message

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/007.png)

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the process of accessing the EPSI web application from initiation to exit as well as the layout of the system menu and its functions.

Identity and Access Management (IAM) Provisioning automates the process for creating, approving, granting, and removing system access to VA enterprise applications. EPSI integrates with the IAM Provisioning Service to provide user access.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[EPSI](https://epsi.va.gov/epsi-web/) is accessed using the VA Single Sign-On Internal (SSOi) login.

<span id="_Toc160546020" class="anchor"></span>Figure 7: VA Single Sign-On for EPSI

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/008.png)

Click Sign In with VA PIV Card to authenticate your Personal Identity Verification (PIV) card and sign on to the VA network. After you have signed in and completed the authentication process, you will gain access to the EPSI application.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPSI application main menu offers six (6) main tabs for various functions: INDEXER, NURSE, QUALITY ASSURANCE, ADMINISTRATOR, REPORTS and STATUS. Once you have been assigned your specific role, you can access its functions.

<span id="_Toc222734423" class="anchor"></span>Figure 8: EPSI Main Menu Header

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/009.png)

### Indexer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three workspaces that can be accessed under the INDEXER tab in EPSI: Work Queue, Received Transfers queue, and Problem Documents queue.

<span id="_Toc222734424" class="anchor"></span>Figure 9: Indexer Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/010.png)

- The Work Queue allows Indexers to upload documents, transfer patient records to Nurses for review, transfer patient records to other Indexers, and queue records for upload. The Indexer Work Queue is organized as follows:
- Add Files: Allows users to upload files into EPSI.
- Merge Files: Allows users to merge selected files into one.
- Remove Files: Allows selected file(s) to be deleted from EPSI.
- File List: Section of the page where files selected for indexing are listed. There are three primary columns in this list:
  - File Name: Name of the document selected.
  - Aged: The length of time the file has been uploaded into EPSI.
  - Pages: The total number of pages contained in the file.
- The Received Transfers queue allows Indexers to transfer patient records and queue records for upload that were transferred to them by other EPSI users.
- The Problem Documents queue allows Indexers to replace, transfer, or queue patient records for upload that had issues such as missing pages or poor-quality images.

Indexers can upload files into EPSI (via File Explorer by selecting the choose from folder link, or by dragging/dropping the file from the user device), rotate file pages, and split files into new PDFs to create a separate file to index. Indexers can also view document statuses at their specific site(s) via the STATUS tab in the EPSI top menu.

### Nurse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three workspaces that Nurses can work out of in EPSI: the Care Queue, the Received Transfers queue, and the Problem Documents queue.

<span id="_Toc126223920" class="anchor"></span>Figure 10: Nurse Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/011.png)

- The Care Queue is where Nurses review documents marked as Need Clinical Review by Indexers or other Nurses.
- The Received Transfers queue allows Nurses to review documents, transfer patient records to other EPSI users, and index records for upload that were transferred to them by other EPSI users.
- The Problem Documents queue allows Nurses to replace, transfer, or index patient records for upload that had issues such as missing pages or poor-quality images.

Nurses can also view document statuses at their specific site(s) via the Status tab in the EPSI main menu.

### Quality Assurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QUALITY ASSURANCE tab allows users to review documents for accuracy that were uploaded by Indexers. In addition, the Quality Assurance role can view document statuses via the Status tab.

<span id="_Toc126223922" class="anchor"></span>Figure 11: Quality Assurance Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/012.png)

### Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADMINISTRATOR tab allows Administrators to view users’ access to EPSI and their roles and permissions at their specific site. Other functions include:

- Managing consult notes
- Transferring documents between Indexers and Nurses
- Exporting consult note tables, user administration tables, and document status tables
- Checking the status of files processed in EPSI

<span id="_Toc126223923" class="anchor"></span>Figure 12: Administrator Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/013.png)

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The REPORTS tab allows EPSI users with the Administrator role to generate six types of reports for the site the user is currently logged into:

- Documents Indexed by User
- Problem Documents in Queue
- Problem Documents in Queue Detailed Export
- QA Total Files Audited
- QA Detailed Auditing Export
- Documents Removed by User

Reports are initially generated as a table within EPSI (excluding QA Detailed Auditing Export, which can only be exported as a CSV file). All reports can be exported to a CSV file, saved as a PDF, or printed. Refer to [Section 4.8](#reports-1) for instructions.

<span id="_Toc222734428" class="anchor"></span>Figure 13: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/014.png)

- The Documents Indexed by User report provides the total number of files that have been uploaded to VistA Imaging for each user for a specified date range.
- The Problem Documents in Queue report provides the total number of files currently in each user’s Problem Documents Queue. This report can also be filtered by the reason a file was placed in the Problem Documents Queue (e.g., missing pages, incomplete record, etc.).
- The Problem Documents in Queue Detailed Export report provides additional details on all the files currently in any user’s Problem Documents Queue within a specified date range.
- The QA Total Files Audited report provides the total number of files audited by the QA role, grouped by Indexer, for a specified date range.
- The QA Detailed Auditing Export report is a detailed report for exporting all the files reviewed by the QA role for a specified date range.
- The Documents Removed by User report is a detailed report displaying all files removed by an EPSI user within a specified date range.

### Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STATUS tab can be used by all user roles to review the current processing status of a file in EPSI.

<span id="_Toc126223924" class="anchor"></span>Figure 14: Status Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/015.png)

On the Status page, files are organized in a table with the following column headings: File Name, Status, File Queue, Created By, Created, Indexed By, and Last Modified. Any EPSI user can export this Document Status table to a spreadsheet (Refer to [Section 4.9.2](#exporting-document-status-table) for instructions).

The following list includes all the possible statuses this table can display:

- Image Passed To VistA and Sent To Registered Nurse (RN) for Review: The document has been sent to the VistA Imaging background processor for upload into VistA Imaging. Additionally, the document was marked as Needs Clinical Review and has been transferred to the selected Nurse for review.
- Parent File Split Complete: The parent document has been received and split into child files. Child files must be handled (i.e., transferred or indexed) to remove the parent file from view.
- Pending Indexing: Document has not yet begun the indexing process or been split.
- Pending Indexing and Sent to RN for Review: The document was transferred to a Nurse and is pending indexing by the Nurse.
- Pending Indexing and Transferred to Another User: The document was transferred to another user and is pending indexing by that user.
- Pending VistA Imaging Processing: The document was sent to the VistA Imaging background processor for upload into VistA Imaging and imaging processing is pending.
- Pending Vista Imaging Processing and Sent to RN for Review: The document has been sent to the Vista Imaging background processor for upload into Vista Imaging. Additionally, the document was marked as high risk and has been transferred to the selected nurse for review.
- Indexing Successful: The document was sent successfully to the Vista Imaging background processor for upload into Vista Imaging.

### Build Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can review any new updates for the latest build/release of the application by selecting the Build number link located at the top-right of the page. The New Changes And Enhancements dialog box will display.

<span id="_Toc222734430" class="anchor"></span>Figure 15: New Changes and Enhancements Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/016.png)

### Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users logged into EPSI can access additional EPSI resources by selecting the question mark icon in the top-right corner, then selecting the EPSI POWER APPS (CHANGE REQUEST) link from the dialog box that displays.

<span id="_Toc222734431" class="anchor"></span>Figure 16: EPSI Power Apps

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/017.png)

Selecting this link will open the EPSI Dashboard, which is a Microsoft Power App that allows users to:

- Submit EPSI Change Requests
- Submit EPSI Consultation and Integration Requests
- View the EPSI SharePoint Site
- Submit EPSI Technical Issues

<span id="_Toc222734432" class="anchor"></span>Figure 17: EPSI Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/018.png)

### Upload Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UPLOAD QUEUE tab can be selected to display a dialog box with the last seven records processed within the last 30 days.

<span id="_Toc222734433" class="anchor"></span>Figure 18: Upload Queue Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/019.png)

The dialog box will display following information:

- Upload Queue Average: Average time for all records in queue
- Name: The name of the file
- Date/Time initiated: Date and time when EPSI queued the file to VistA
- Time in Queue: Time when VistA received the file from EPSI to the time when VistA inserted the file into the Veteran's record
- Status:
- Pending (i.e. pending VistA ingest)
- Complete (i.e. VistA ingested the file)
- Veteran Information: Contains a Veteran Details hyperlink which, when selected, displays the Veteran’s name, Integration Control Number (ICN), Date of Birth, and unique identifier

<span id="_Toc222734434" class="anchor"></span>Figure 19: Upload Queue – Veteran Details Pop-up

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/020.png)

When there is no information to be displayed in this dialog box, EPSI will display a message stating, No available data for last 30 days.

<span id="_Toc222734435" class="anchor"></span>Figure 20: Upload Queue Dialog Box (No Available Data)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/021.png)

### User Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, reports and table columns in EPSI display the current time in the Coordinated Universal Time (UTC) zone. If you would like to change your default time zone, complete the following steps:

1.  Select your Login name to open the User Preferences screen.

<span id="_Toc222734436" class="anchor"></span>Figure 21: User Preferences Time Zone Window

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/022.png)

2.  Select the desired time zone from the radio buttons displayed (Universal UTC, Atlantic, Eastern, Central, Mountain, Pacific, Alaska, or Hawaiian-Aleutian).
3.  Select SAVE to confirm your selection. The current time will now display in your chosen time zone throughout the application.

<span id="_Toc222734437" class="anchor"></span>Figure 22: Time Zone Change Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/023.png)

### Current Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are granted access to the EPSI application, you are assigned to at least one EPSI site location, and the system displays your site number at the top right of the page. Users with access to multiple sites can select the \> icon displayed next to the Current Site label and select the desired site from the list.

<span id="_Toc126223925" class="anchor"></span>Figure 23: Current Site

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/024.png)

5.  If you have access to multiple sites, at initial login, your first valid site number displays by default. Any subsequent logins will automatically display the last site number you selected in the previous session. Any changes made in EPSI will only apply to the site that you are currently logged into.

## Logging Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222734439" class="anchor"></span>Figure 24: EPSI Log Out Link

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/025.png)

To exit the EPSI application, select LOG OUT in the top-right corner of the page. Properly exiting the application helps to prevent personal patient information from being visible to others. To reenter the EPSI application, reload the EPSI weblink.

6.  If a user has been idle or inactive in the application for an extended period, a timeout notification will display stating the amount of time remaining until the system closes automatically. Select the DO NOT CLOSE EPSI button to keep EPSI open or select the CLOSE EPSI button to exit the application.

<span id="_Toc222734440" class="anchor"></span>Figure 25: EPSI Timeout Notification

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/026.png)

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI provides user functionality for the following actions:

- Preparing and Managing Files
- Uploading Files
  - Automated Detection Functions
  - Sorting Files
  - Splitting Files
  - Rearranging File Pages
  - Removing Files
  - Merging/Unmerging Files
  - Rotating File Pages
- Indexing Files
- Indexing a Consult / Referral Workflow
  - Working with Multiple Consults
  - Working from the Received Transfers Queue
- Indexing New Notes Workflow
- Indexing Existing Notes Workflow
- Indexing Administrative Documents Workflow
- Transferring Files
- Reviewing Files
- Create AI Summary
- Working with Problem Documents
- Replacing Files
- Missing RFS Signatures
- Quality Assurance Functions
- Reviewing Files
- Administrator Functions
- Consult Notes
- User Administration Page
- Internal Transfer Workflow
- Document Status Page
- Exporting Tables Workflow
- Reports
- Documents Indexed by User
- Problem Documents in Queue
- Problem Documents in Queue Detailed Export
- QA Total Files Audited
- QA Detailed Auditing Export
- Documents Removed by User
- Exporting and Printing Reports
- Status
- Checking Current Processing Status
- Exporting Document Status Table

## Preparing and Managing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Uploading Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic documents must be uploaded into EPSI before any other actions (e.g., reviewing, manipulating, or queuing files for upload to VistA Imaging) can be performed. Files can only be uploaded into EPSI via the Work Queue under the Indexer tab.

7.  The maximum single file size that can be uploaded into EPSI is 40 megabytes.
1.  Select the Indexer tab to access the Indexer dashboard.

<span id="_Toc222734441" class="anchor"></span>Figure 26: Indexer Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/027.png)

2.  Under the Work Queue tab, select the Add Files button. The Add Files dialog box displays.

<span id="_Toc222734442" class="anchor"></span>Figure 27: Add Files Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/028.png)

4.  Select the choose from folder link. The File Explorer dialog box displays. Users also have the option to drag files into the area labeled Drag files here.

<span id="_Toc222734443" class="anchor"></span>Figure 28: File Explorer Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/029.png)

3.  From File Explorer, select the desired document to upload. You can select multiple documents.
4.  Select Open to upload the file into EPSI. Once the document has been uploaded, it will display on the left side of the Indexer dashboard, and a banner will display in the top-right corner of the page to indicate that the file has been successfully uploaded.

<span id="_Toc222734444" class="anchor"></span>Figure 29: Uploaded Files

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/030.png)

8.  Larger documents take longer to upload to EPSI. During these longer processing times, a Retrieving document dialog box displays to indicate that the document is in the process of being uploaded.

<span id="_Toc222734445" class="anchor"></span>Figure 30: Retrieving Document Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/031.png)

#### Automated Detection Functions

Using optical character recognition (OCR) software via Intelligent Document Processing (IDP) automation powered by Amazon Web Service (AWS) Textract, the EPSI application can detect a variety of elements in uploaded files to confirm their quality and classification.

Once a file has been uploaded and added to the file list in the Indexer Work Queue, the icon displayed to the left of the uploaded file provides information regarding the file’s current stage of processing in EPSI IDP.

<span id="_Toc222734446" class="anchor"></span>Figure 31: Processing Icons

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/032.png)

- A blue lightning bolt means the file has finished processing and detected information to automate.
- A black PDF icon means there was an error in processing or there was no detected information to automate.
- A green PDF icon means there was information extracted from the file name.
- A black Page (AI) icon means the file is still being processed.

EPSI Automation is further demonstrated in two main scenarios during the upload process:

- Multiple Patients Detected: A system message displays if an uploaded file includes data from more than one patient.
- Multiple Dates of Service: A system message displays if an upload PDF includes multiple dates of service for a Veteran.

The following steps provide instruction on what to do in each scenario.

1.  If EPSI has detected multiple patient names in the file, the patient names will be listed, and a detection message will display.

<span id="_Toc222734447" class="anchor"></span>Figure 32: Multiple Patients Detected

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/033.png)

2.  Select the radio button next to the correct Patient Name, then select the INDEX button to continue indexing the file.
3.  If EPSI has detected multiple dates of service in a Veteran’s file, the Dates of Service will be listed, and a message will display that multiple dates were detected.

<span id="_Toc222734448" class="anchor"></span>Figure 33: Multiple Dates of Service

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/034.png)

5.  Select the radio button next to the correct date, then select the INDEX button to continue indexing the file.

#### RFS Form Detection

EPSI can also use IDP to automatically detect if an uploaded file is a Community Care Provider—Request for Service form (VA form 10-10172), also known as an RFS form.

EPSI detects the following items within the RFS form:

- Fax header date
- Patient name(s)
- Birth Date(s) (Precise Patient Validation)
- Date(s) of Service
- Provider signature
- Blank Pages

| RFS Form Version | Detected by EPSI |
|----------------------|----------------------|
| May 2019             | Yes                  |
| February 2021        | Yes                  |
| May 2021             | Yes                  |
| July 2023            | Yes                  |
| October 2025         | Yes                  |

<span id="_Toc222734412" class="anchor"></span>Table 3: Role Scenarios in EPSI

Depending on which user roles are enabled within EPSI, varying actions are enabled when indexing RFS forms. The Role Scenarios table lists a breakdown of the roles that can complete the indexing process for RFS forms.

| Roles Enabled Per User | Actions in EPSI            |
|----------------------------|--------------------------------|
| Indexer Role Only          | Transfer RFS forms to a Nurse. |
| Nurse Role Only            | Can index RFS forms.           |
| Indexer and Nurse Role     | Can index RFS forms.           |

<span id="_Toc222734212" class="anchor"></span>Appendix A: Acronyms and Abbreviations<span id="_Toc222734413" class="anchor"></span>Table 4: Acronyms and Abbreviations

Based on your designated role, you can index and/or transfer RFS forms using the instructions provided in [Section 4.2.- Indexing Files](#indexing-files) and [Section 4.3.- Transferring Files](#transferring-files).

#### Page View Customization

EPSI can detect blank and Request for Service (RFS) pages in documents that have been processed by IDP. Once you have selected a file, it displays on the right side of the screen with the following items located above it:

- Viewdrop-down menu: Allows users to customize their view of the selected file.
- Left button: Rotates the selected pages to the left.
- Split button: Allows users to split a main file into separate files.
- Right button: Rotates the selected pages to the right.
- Delete Pages button: Allows users to delete selected pages from a file.
- Out button: Allows the user to zoom out on the file.
- Zoom: Allows the user to change the viewing scale by moving the slider back and forth.
- In button: Allows the user to zoom in on the file.

<span id="_Toc222734449" class="anchor"></span>Figure 34: Uploaded File with Blank and RFS Pages

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/035.png)

Take the following steps to customize the page view:

1.  Select the View drop-down menu. If blank or RFS pages are detected within the file, those options will display in the list. The numbers in parentheses indicate how many pages of each type have been detected in that file.

<span id="_Toc222734450" class="anchor"></span>Figure 35: Uploaded File - View Drop-down Menu

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/036.png)

2.  Select an option (All, Blank, or RFS) from the menu. Only the pages in that category will display.

<span id="_Toc222734451" class="anchor"></span>Figure 36: Uploaded File – Blank Pages Displayed

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/037.png)

### Sorting Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can sort files from the following locations in EPSI:

- Indexer Received Transfers and Problem Documents queues
- Nurse Care Queue, Received Transfers, and Problem Documents queues
- Quality Assurance Dashboard

The file list is organized under three column headings: File Name, Aged, and Pages. To sort files, select the header for the individual column you wish to sort. This will sort all files listed in ascending order (A, B, C, D or 1,2,3). Selecting the header a second time will sort all files in descending order (D, C, B, A or 3,2,1).

<span id="_Toc222734452" class="anchor"></span>Figure 37: Sorting Files (1 of 3)-Unsorted Files (Default View)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/038.png)

<span id="_Toc222734453" class="anchor"></span>Figure 38: Sorting Files (2 of 3)-Sorted Files Ascending

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/039.png)

<span id="_Toc222734454" class="anchor"></span>Figure 39: Sorting Files (3 of 3)-Sorted Files Descending

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/040.png)

9.  Users can also sort files within the Nurse Care Queue and QA File Queue in ascending or descending order by selecting the blue-underlined Sort text link located at the top of the file list.

### Splitting Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can split files into separate documents for patient records that include multiple patients. Files can also be split to delete pages that do not need to be indexed. The following steps can be followed once a file is selected in EPSI:

<span id="_Toc222734455" class="anchor"></span>Figure 40: File View

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/041.png)

1.  Select the Split button. The Create New PDF dialog box displays.

<span id="_Toc222734456" class="anchor"></span>Figure 41: Create New PDF Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/042.png)

2.  Select the pages to include in the new PDF. Page ranges can be selected in two ways:
    1.  To select the pages using the From and To fields, enter the starting page number in the From field. Enter the ending page number in the To field.
    2.  To select the pages using the Page Range field, enter the range of pages in the Page Range field (e.g., 2-4).
10. EPSI does NOT split documents based on the page numbers included in the document itself.
3.  Select Continue to split the file. The newly separated files will display in the file list.

<span id="_Toc222734457" class="anchor"></span>Figure 42: Successfully Split Files

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/043.png)

11. When you split a document, it creates two distinct child documents made from pages chosen by the user from the parent document. The file that includes the split pages is listed as the second item in a file tree underneath the parent document. For example, if you create a new PDF for pages one (1) through five (5) of a 10-page document, the first child document will include pages six (6)-10, while the second child document will include pages one (1) through five (5).

#### Deleting File Pages

To delete pages within a file, use the following steps:

12. This process can be followed by both Indexers and Nurses once a file has been selected in the appropriate queue.

<span id="_Toc222734458" class="anchor"></span>Figure 43: Uploaded File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/044.png)

1.  Select the page(s) you would like to delete.

<span id="_Toc222734459" class="anchor"></span>Figure 44: File with Selected Pages

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/045.png)

2.  Select the DELETE PAGES button. A Warning message displays stating the deleting of pages cannot be undone and asks if you would like to continue.

<span id="_Toc222734460" class="anchor"></span>Figure 45: Delete Pages Warning Message

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/046.png)

3.  Select CONTINUE to delete the selected pages. A banner will display in the top-right corner to indicate that the file has been successfully deleted.

<span id="_Toc222734461" class="anchor"></span>Figure 46: Deleted Pages Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/047.png)

### Rearranging File Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To rearrange the order of pages within a file, use the steps in the following sections.

13. These steps can be followed by both Indexers and Nurses once a file has been selected in the appropriate queue.

#### Rearrange Pages Using the Keyboard

<span id="_Toc222734462" class="anchor"></span>Figure 47: File View

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/048.png)

1.  Select the page you would like to move using the TAB key.

<span id="_Toc222734463" class="anchor"></span>Figure 48: File Page Selected

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/049.png)

2.  While holding the SHIFT key, press the UP or DOWN arrow to move the page above or below its current location.

<span id="_Toc222734464" class="anchor"></span>Figure 49: File Page Moved

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/050.png)

#### Rearrange Pages Using a Mouse

1.  Hover the mouse cursor over the page you would like to move.

<span id="_Toc222734465" class="anchor"></span>Figure 50: Cursor Hover

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/051.png)

6.  Press and hold the left mouse button to select the page you want to move.

<span id="_Toc222734466" class="anchor"></span>Figure 51: Page Selected

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/052.png)

7.  While still holding down the left mouse button, drag the page up or down to the desired location. The two rows of dots indicate where the page will be placed once you release the mouse button.

<span id="_Toc222734467" class="anchor"></span>Figure 52: Dragging the File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/053.png)

3.  Release the mouse button to snap the selected page into its new position within the file.

### Removing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI users can remove files under the following role queues:

- Indexer Role:Work Queue, Received Transfers, and Problem Documents
- Nurse Role:Received Transfers and Problem Documents
14. Files are only removed from the EPSI application and are not removed from the user’s device.
1.  Select the checkbox next to each file you would like to remove in the file list.
2.  Select the REMOVE FILES button. The Remove Files dialog box displays listing each document the user has selected for deletion.

<span id="_Toc222734468" class="anchor"></span>Figure 53: Remove Files Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/054.png)

15. For user awareness, the Remove Files dialog box includes a note stating that removing files is an action that cannot be undone in EPSI.
3.  Select an option from the Reasons For Removal (\*Required) drop-down menu.

<span id="_Toc222734469" class="anchor"></span>Figure 54: Reasons For Removal Drop-down Menu

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/055.png)

4.  Add text to the Comments field. If Other is selected as a reason for removal, this field will be marked as (\*Required).
5.  Select the REMOVE button. A banner will display for each file confirming that each document was successfully deleted.

<span id="_Toc222734470" class="anchor"></span>Figure 55: Documents Deleted

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/056.png)

### Merging Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Indexer Work Queue, users can merge multiple files that have been uploaded into EPSI into a single document.

The following functionality becomes unavailable when files are merged in EPSI:

- Users cannot split the pages of a document that has been merged.
- Users cannot merge a file with one that has already been merged.

Additionally, users cannot index the individual child documents of a merged file.

1.  From the Indexer’s Work Queue, upload the documents you would like to merge into EPSI. Refer to [Section 4.1.1](#uploading-files) for detailed instructions for this step.
2.  In the file list, select the checkboxes next to each file you would like to merge.
3.  Select the MERGE FILES button at the top of the file list. The File Merge dialog box displays.

<span id="_Toc222734471" class="anchor"></span>Figure 56: File Merge Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/057.png)

16. Files will display in the order that they were selected from the file list.
4.  Rename the file, if necessary. The name defaults to the first file selected in the file list.
5.  Set the order of the files to be merged by selecting the Up or Down arrows. To remove a file from the merge list, select the X next to the file you want to remove.
6.  Select CONFIRM MERGE to merge the files in the order listed. A confirmation banner will display indicating that the merge is complete. The merged files will display in the file list as child documents underneath the file name that was chosen. Alternatively, select CANCEL to cancel merging.

<span id="_Toc222734472" class="anchor"></span>Figure 57: Merge Successful Message

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/058.png)

<span id="_Toc222734473" class="anchor"></span>Figure 58: Merged Documents

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/059.png)

### Unmerging Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Indexer Work Queue, users can unmerge files that were previously merged in EPSI.

1.  From the Indexer Work Queue, select the parent file of the documents that you would like to unmerge from the file list.

<span id="_Toc222734474" class="anchor"></span>Figure 59: Merged File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/060.png)

2.  Select the UNMERGE FILE button. An Unmerge File dialog box will display asking if you would like to unmerge the document.

<span id="_Toc222734475" class="anchor"></span>Figure 60: Unmerge Document Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/061.png)

3.  Select the UNMERGE FILE button. A confirmation message will display, and the merged files will display as separate files in the file list, as they did originally.

<span id="_Toc222734476" class="anchor"></span>Figure 61: Unmerge Successful

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/062.png)

<span id="_Toc222734477" class="anchor"></span>Figure 62: Unmerged Documents

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/063.png)

### Rotating File Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the file view, select the checkbox for each page you would like to reorient.
4.  Select the Select All checkbox to select all pages of the document.

<span id="_Toc222734478" class="anchor"></span>Figure 63: Selected Pages

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/064.png)

8.  Select either the LEFT or RIGHT button. This will rotate the selected files 90 degrees in the chosen direction.

<span id="_Toc222734479" class="anchor"></span>Figure 64: Rotated Pages

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/065.png)

## Indexing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The indexing workflow has been simplified in EPSI through a Document Actions menu that minimizes the number of steps needed to complete the process.

<span id="_Toc126223926" class="anchor"></span>Figure 65: Minimal Click - Document Actions

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/066.png)

The menu consists of the following actions:

- Index Consult: Attach a record to a consult/referral for a selected Patient.
- Search Patients: Identify the Patient record you wish to work with or replace the displayed Patient with the correct one.
- Index New Note: Attach a new note to the Patient’s record.
- Index Existing Note/Addendum: Attach a record to an Existing Note or Addendum for the displayed Patient.
- Index Administrative Documents: Upload administrative documents to the Patient’s record.
- Transfer Document: Transfer document(s) to an Indexer, Nurse, or your own Problem Documents queue.
- File List: Return to the file list in your queue.

  The sections that follow provide instruction on how to index files in EPSI in the most common scenarios: Consult/Referral, New Note, Existing Note, and Administrative Documents.
17. The instructions in these sections can be followed if the user is in the Work Queue or Received Transfers queue.

### Indexing a Consult / Referral Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To initiate indexing functionality, a file must be selected on the left side of the page.

1.  Select a file to index. The selected file displays on the right side of the dashboard.

<span id="_Toc127962372" class="anchor"></span>Figure 66: Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/067.png)

9.  Select the Index link that corresponds to the file you selected. If no Patient name is detected from the document, the Patient Search screen will display.

<span id="_Toc222734482" class="anchor"></span>Figure 67: Patient Search Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/068.png)

10. Enter the first three letters of the patient’s last name in the Patient field and select SEARCH or press Enter. A list of names beginning with those letters will display.

<span id="_Toc126223933" class="anchor"></span>Figure 68: Patient Name Search Results

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/069.png)

18. A Veteran’s date of birth and last four of their SSN will be hidden if their record is considered sensitive. If you select a Veteran that has been flagged as having a sensitive record, a WARNING - RESTRICTED RECORD dialog box will display, and you will need to select YES to unhide the hidden fields.

<span id="_Toc222734484" class="anchor"></span>Figure 69: Restricted Record Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/070.png)

11. Select the desired name. Once a name is selected, the Document Actions screen will display with the Veteran’s Date of Birth and Last Four digits of the social security number auto-populated at the top, confirming their identity.

<span id="_Toc222734485" class="anchor"></span>Figure 70: Document Actions Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/071.png)

19. If at any point you want to return to the file list, select the BACK button. If this button is selected, a warning message will display informing the user that any changes made will not be saved.

<span id="_Toc159918089" class="anchor"></span>Figure 71: Return to File List Warning Message

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/072.png)

12. Select the INDEX button. The Details screen will display containing the patient’s details (Name, Date of Birth, and Last 4) and the Consult Details. All fields are required on this screen.

<span id="_Toc222734487" class="anchor"></span>Figure 72: Details Screen (1 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/073.png)

<span id="_Toc222734488" class="anchor"></span>Figure 73: Details Screen (2 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/074.png)

13. If the fields are not already auto-populated from the document, complete the following:
1.  Choose a Date of Service by selecting the calendar icon and choosing a date.
20. If EPSI detects that a file is a Request for Service (RFS) form, a date will automatically display in the Enter date if RFS field.
2.  Select a title from the Note Title drop-down menu. If needed, you can select the REFRESH NOTE TITLE LIST link to update the list of available options.
3.  If needed, select the radio button that corresponds to the Origin of the file. In most cases, it will auto-populate based on the selected Note Title.
4.  Select the type from the Type drop-down menu.
5.  Select the specialty from the Specialty drop-down menu.
6.  Select the procedure from the Procedure drop-down menu.
7.  Select the location associated with the consult in the Location drop-down menu. If there is no location associated with the consult, select No Location.
5.  If you need to work with another consult, you can select the CHANGE CONSULT button from this screen. The Change Consult screen will display, and you can select the correct one from the list.

<span id="_Toc222734489" class="anchor"></span>Figure 74: Change Consult Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/075.png)

6.  When you have selected the correct consult, select the CHANGE CONSULT button and the Consult Details for the newly selected consult will display.
14. Select SAVE AND REVIEW. The Document Details screen displays.

<span id="_Toc126223941" class="anchor"></span>Figure 75: Consult Document Details Screen (1 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/076.png)

<span id="_Toc222734491" class="anchor"></span>Figure 76: Consult Document Details Screen (2 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/077.png)

15. Select the Needs Clinical Review checkbox if you would like to send a copy of the patient record to a Nurse’s Care Queue for review.
16. If applicable, select a Nurse from the Clinical Review Nurse drop-down menu.
17. Provide a description in the Long Description field. This is an optional field with a 2,000-character limit.
18. Provide a description in the Short Description (Image Description) field. This is a required field with a 60-character limit.
21. If needed, you can choose alternate actions for the file by selecting the corresponding button from this screen: TRANSFER, CHANGE CONSULT, or EDIT DETAILS.
19. Select UPLOAD. The system will return you to your work queue and display a confirmation message.

<span id="_Toc222734492" class="anchor"></span>Figure 77: Upload Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/078.png)

#### Working with Multiple Consults

Users can associate a patient record with up to two additional consults/referrals.

22. Please note that the addition of a secondary consult in EPSI will create a note in CPRS referencing its link to the primary consult and associated documentation.

The steps in this section can be followed in the following roles and queues:

- Indexer: Work Queue, Received Transfers, and Problem Documents
- Nurse: Received Transfers and Problem Documents

<span id="_Toc222734493" class="anchor"></span>Figure 78: Consult Document Details Screen (1 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/079.png)

1.  From the Document Details screen of your consult, select the ADD CONSULT hyperlink text located below the Patient information. The Select Secondary Consult screen displays.

<span id="_Toc222734494" class="anchor"></span>Figure 79: Select Secondary Consult Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/080.png)

7.  Selecting the REFRESH CONSULT LIST link will update the list of available secondary consults. You can also view further information about the selected consult by selecting CONSULT DETAILS.
2.  Select a consult from the list then select ADD CONSULT. The Document Details screen will display with the secondary consult added.

<span id="_Toc222734495" class="anchor"></span>Figure 80: Document Details with Secondary Consult

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/081.png)

3.  Select the REMOVE hyperlink if you wish to remove the consult.

#### Working from the Received Transfers Queue

To review, index, or transfer consult files that were transferred to you, complete the steps that follow.

1.  From the Received Transfers tab, select the file you want to work with.

<span id="_Toc222734496" class="anchor"></span>Figure 81: Received Transfers Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/082.png)

20. Select the Index link to view the Document Transfer Details. Since the selected file was transferred to you from another user, additional fields will display that provide information about the transfer (Document transferred from, Reasons for Transfer, and Note).

<span id="_Toc222734497" class="anchor"></span>Figure 82: Document Transfer Information Displayed

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/083.png)

21. From this screen, you can choose your desired action to continue working with the file (Index, Transfer, or attach a New Note).

### Indexing New Notes Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select a file to index. The selected file displays on the right side of the dashboard.

<span id="_Toc222734498" class="anchor"></span>Figure 83: Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/084.png)

22. Select the Index link that corresponds to the file you selected. If no Patient name is detected from the document, the Patient Search screen will display.

<span id="_Toc222734499" class="anchor"></span>Figure 84: Patient Search Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/085.png)

23. Users can rotate pages, zoom in and out, rearrange pages, or split the PDF to create a new file if there are multiple patients within the original PDF. For more information on these topics, refer to [Section 4.1](#preparing-and-managing-files).
23. Enter the first three letters of the patient’s last name in the Patient field and select SEARCH or press Enter. A list of names beginning with those letters will display.

<span id="_Toc222734500" class="anchor"></span>Figure 85: Patient Name Search Results

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/086.png)

24. A Veteran’s date of birth and last four of their SSN will be hidden if their record is considered sensitive. If you select a Veteran that has been flagged as having a sensitive record, a WARNING - RESTRICTED RECORD dialog box will display, and you will need to select YES to unhide the hidden fields.

<span id="_Toc222734501" class="anchor"></span>Figure 86: Restricted Record Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/087.png)

24. Select the desired name. Once a name is selected, the Document Actions screen will display with the Veteran’s Date of Birth and Last Four digits of the social security number auto-populated at the top, confirming their identity.

<span id="_Toc222734502" class="anchor"></span>Figure 87: Document Actions Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/088.png)

25. If at any point you want to return to the file list, select the BACK button. If this button is selected, a warning message will display informing the user that any changes made will not be saved.
25. Select the NEW NOTE button. The New Note Details screen will display. All fields are required on this screen.

<span id="_Toc222734503" class="anchor"></span>Figure 88: New Note Details Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/089.png)

26. If the fields are not already auto-populated, complete the following:
1.  Choose a Date of Service by selecting the calendar icon and choosing a date.
26. If EPSI detects that a file is a Request for Service (RFS) form, a date will automatically display in the Enter date if RFS field.
2.  Select a title from the Note Title drop-down menu. If needed, you can select the REFRESH NOTE TITLE LIST link to update the list of available options.
3.  Select the radio button that corresponds to the Origin of the file.
4.  Select the type from the Type drop-down menu.
5.  Select the specialty from the Specialty drop-down menu.
6.  Select the procedure from the Procedure drop-down menu.
7.  Select the location associated with the consult in the Location drop-down menu. If there is no location associated with the consult, select No Location.
27. Select SAVE AND REVIEW. The Document Details screen displays.

<span id="_Toc222734504" class="anchor"></span>Figure 89: New Note Document Details Screen (1 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/090.png)

<span id="_Toc222734505" class="anchor"></span>Figure 90: New Note Document Details Screen (2 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/091.png)

28. Select the Needs Clinical Review checkbox if you would like to send a copy of the patient record to a Nurse’s Care Queue for review.
29. If applicable, select a Nurse from the Clinical Review Nurse drop-down menu.
30. Provide a description in the Long Description field. This is an optional field with a 2,000-character limit.
31. Provide a description in the Short Description (Image Description) field. This is a required field with a 60-character limit.
27. If needed, you can choose alternate actions for the file by selecting the corresponding button from this screen: TRANSFER or EDIT DETAILS.
32. Select UPLOAD. The system will return you to your work queue and display a confirmation message.

<span id="_Toc222734506" class="anchor"></span>Figure 91: Upload Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/092.png)

### Indexing Existing Notes Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To attach a Patient record to an existing note, complete the following steps:

1.  From the list of files, select the file to index. The selected file will display on the right side of the screen.

<span id="_Toc222734507" class="anchor"></span>Figure 92: Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/093.png)

33. Select the Index link that corresponds to the file you selected. If no Patient name is detected from the document, the Patient Search screen will display.

<span id="_Toc222734508" class="anchor"></span>Figure 93: Patient Search Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/094.png)

28. Users can rotate pages, zoom in and out, rearrange pages, or split the PDF to create a new file if there are multiple patients within the original PDF. For more information on these topics, refer to [Section 4.1](#preparing-and-managing-files).
34. Enter the first three letters of the patient’s last name in the Patient field and select SEARCH or press Enter. A list of names beginning with those letters will display.

<span id="_Toc222734509" class="anchor"></span>Figure 94: Patient Name Search Results

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/095.png)

29. A Veteran’s date of birth and last four of their SSN will be hidden if their record is considered sensitive. If you select a Veteran that has been flagged as having a sensitive record, a WARNING - RESTRICTED RECORD dialog box will display, and you will need to select YES to unhide the hidden fields.

<span id="_Toc222734510" class="anchor"></span>Figure 95: Restricted Record Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/096.png)

35. Select the desired name. Once a name is selected, the Document Actions screen will display with the Veteran’s Date of Birth and Last Four digits of the social security number auto-populated at the top, confirming their identity.

<span id="_Toc222734511" class="anchor"></span>Figure 96: Document Actions Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/097.png)

30. If at any point you want to return to the file list, select the BACK button. If this button is selected, a warning message will display informing the user that any changes made will not be saved.
36. Select the APPEND button. The Existing Note Details screen will display. (The Type, Specialty and Procedure fields are optional on this screen).

<span id="_Toc222734512" class="anchor"></span>Figure 97: Existing Note Details Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/098.png)

37. If the fields are not already auto-populated, complete the following:
1.  Choose a Date of Service by selecting the calendar icon and choosing a date.
31. If EPSI detects that a file is a Request for Service (RFS) form, a date will automatically display in the Enter date if RFS field.
2.  Select a title from the Note Title/Addendum drop-down menu. (If needed, you can select the NOTE DETAILS link, and the full details of the existing note will display in a separate window).
38. Select SAVE AND REVIEW. The Document Details screen displays.

<span id="_Toc222734513" class="anchor"></span>Figure 98: Existing Note Document Details Screen (1 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/099.png)

<span id="_Toc222734514" class="anchor"></span>Figure 99: Existing Note Document Details Screen (2 of 2)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/100.png)

39. Select the Needs Clinical Review checkbox if you would like to send a copy of the patient record to a Nurse’s Care Queue for review.
40. If applicable, select a Nurse from the Clinical Review Nurse drop-down menu.
41. If needed, select the Add a NewAddendum to Parent Note and Attach File checkbox and enter text in the (now required) Add Text for the New Addendum field. There is a 2,000-character limit for this field.
32. These fields will not be displayed if an Addendum was already selected from the Note Title/Addendum drop-down menu.
42. Provide a description in the Short Description (Image Description) field. This is a required field with a 60-character limit.
33. If needed, you can choose alternate actions for the file by selecting the corresponding button from this screen: TRANSFER or EDIT DETAILS.
43. Select UPLOAD. The system will return you to your work queue and display a confirmation message.

<span id="_Toc222734515" class="anchor"></span>Figure 100: Upload Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/101.png)

### Indexing Administrative Documents Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To attach administrative documents to a Patient record, complete the following steps:

1.  From the list of files, select the file to index. The selected file will display on the right side of the screen.

<span id="_Toc222734516" class="anchor"></span>Figure 101: Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/102.png)

44. Select the Index link that corresponds to the file you selected. If no Patient name is detected from the document, the Patient Search screen will display.

<span id="_Toc222734517" class="anchor"></span>Figure 102: Patient Search Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/103.png)

45. Enter the first three letters of the patient’s last name in the Patient field and select SEARCH or press Enter. A list of names beginning with those letters will display.

<span id="_Toc222734518" class="anchor"></span>Figure 103: Patient Name Search Results

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/104.png)

46. Select the desired name. Once a name is selected, the Document Actions screen will display with the Veteran’s Date of Birth and Last Four digits of the social security number auto-populated at the top, confirming their identity.

<span id="_Toc222734519" class="anchor"></span>Figure 104: Document Actions Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/105.png)

47. Select the UPLOAD button. The Administrative Document Details screen will display. All fields are required on this screen.

<span id="_Toc222734520" class="anchor"></span>Figure 105: Administrative Document Details Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/106.png)

48. Enter a Date of Service by selecting the calendar icon and choosing a date.
49. Select the radio button that corresponds to the Origin of the file.
50. Select a Document/Image Type from the drop-down menu.
51. Select SAVE AND REVIEW. The Document Details summary screen displays.

<span id="_Toc222734521" class="anchor"></span>Figure 106: Administrative Document Details Upload Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/107.png)

52. Provide a description in the Long Description field. This is an optional field with a 2,000-character limit.
53. Provide a description in the Short Description (Image Description) field. This is a required field with a 60-character limit.
34. If needed, you can choose alternate actions for the file by selecting the corresponding button from this screen: TRANSFER or EDIT DETAILS.
54. Select UPLOAD. The system will return you to your work queue and display a confirmation message.

<span id="_Toc222734522" class="anchor"></span>Figure 107: Upload Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/108.png)

## Transferring Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete the following steps to transfer a file from your work queue. Files can also be transferred while indexing or reviewing files.

1.  Select the file you want to transfer from the file list.

<span id="_Toc222734523" class="anchor"></span>Figure 108: Selected File

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/109.png)

55. Select the Index link to select a Patient and open the Document Actions screen.

<span id="_Toc222734524" class="anchor"></span>Figure 109: Document Actions Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/110.png)

35. If you are working from the Received Transfers queue and the selected file was transferred to you from another user, additional fields will display that provide information about the transfer (Document transferred from, Reasons for Transfer, and Note).

<span id="_Toc222734525" class="anchor"></span>Figure 110: Document Transfer Information Displayed

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/111.png)

56. Select TRANSFER. The Transfer Document screen will display. All fields are required on this screen.

<span id="_Toc222734526" class="anchor"></span>Figure 111: Transfer Document Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/112.png)

57. Confirm the name in the Document Name field.
58. Select the Type of transfer from the radio buttons displayed (Indexer, Nurse, or Problem Document). Nurse is chosen by default.
36. Selecting Problem Document will transfer the file to the current user’s Problem Documents queue. You cannot send records to other EPSI users’ Problem Documents queues.
59. Select a user from the Transfer To drop-down menu.
60. Select a choice in the Reasons For Transfer (\*Required) drop-down menu.

<span id="_Toc222734527" class="anchor"></span>Figure 112: Reasons for Transfer

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/113.png)

61. Add to the comment in the Comments field.
62. Select TRANSFER to complete the transfer process.

## Reviewing Files (Clinical Review)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with a Nurse role can review consult files in the Care Queue. The files in this list are attached to Patients who have consults that require clinical review and immediate follow-up. To review documents in the Care Queue, complete the following steps:

8.  If you are a user assigned to multiple roles, confirm the Nurse role by selecting the NURSE tab from the EPSI main menu. The Nurse dashboard displays.

<span id="_Toc222734528" class="anchor"></span>Figure 113: Nurse Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/114.png)

1.  The CareQueue will be selected by default and displays the files that require follow-up in the left side panel. (The file list may also include previously reviewed files which are indicated by a green check mark).

<span id="_Toc222734529" class="anchor"></span>Figure 114: Care Queue – Files Displayed

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/115.png)

63. Select a file to review from the list. The selected file will display on the right, along with general information about the document and additional options: Review Document, Transfer, and Create AI Summary.

<span id="_Toc222734530" class="anchor"></span>Figure 115: Selected File to Review

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/116.png)

64. Select the REVIEW DOCUMENT button after appropriate review and follow-up actions have been completed. A green check mark will display next to the file name indicating the review was completed. A banner will display stating the file has been successfully updated to reviewed.

<span id="_Toc126223981" class="anchor"></span>Figure 116: Review Complete

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/117.png)

### Create AI Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Nurse role can generate and view an AI-generated summary of a selected file (containing more than 3 pages) while conducting a clinical review.

1.  After choosing a file from the Care Queue, select the CREATE AI SUMMARY button. An AI Summary Confirmation dialog box will display.
37. The document must contain more than 3 pages to enable the AI Summary function, otherwise the button will be disabled.

<span id="_Toc222734532" class="anchor"></span>Figure 117: AI Summary Confirmation Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/118.png)

65. Select the I CONFIRM button to continue. The dialog box will disappear, and the screen will display confirmation that the summary is being generated.

<span id="_Toc222734533" class="anchor"></span>Figure 118: Care Queue Dashboard – AI Processing

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/119.png)

66. Depending on the length of the file, the summary generation may take a few minutes, but once complete, a confirmation message will display, and the VIEW AI SUMMARY button will be enabled.

<span id="_Toc222734534" class="anchor"></span>Figure 119: AI Summary Successfully Created

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/120.png)

<span id="_Toc222734535" class="anchor"></span>Figure 120: Care Queue Dashboard – View AI Summary

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/121.png)

67. Select VIEW AI SUMMARY to generate the summary details.

<span id="_Toc222734536" class="anchor"></span>Figure 121: AI Summary Details

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/122.png)

9.  The content in the AI Summary can be copied and pasted into the consult’s long description field or directly into CPRS.
68. The AI Summary is organized under headings that can be selected to view various sections of the summary. When you are done reviewing, select the Close link at the top to return to the main dashboard. Once an AI Summary has been generated, it will always be associated with that file and can be reviewed at any time.

## Working with Problem Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Documents queue allows users to replace, transfer, or index patient records for upload that had issues such as missing pages or poor-quality images.

### Replacing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Indexer or Nurse dashboard, select Problem Documents. The Problem Documents file list will display. Select the file you would like to replace from the list. The document will be displayed on the right of the dashboard.

<span id="_Toc222734537" class="anchor"></span>Figure 122: Problem Documents Queue

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/123.png)

38. You cannot upload files in the Problem Documents queue. Files can only be uploaded via the Indexer Work Queue.
2.  Select the Index link. A details window will display with information related to why the document was originally transferred to the Problem Documents queue. This includes the Date of the transfer, the Uploader, the Reasons for the transfer, and Comments.

<span id="_Toc126223977" class="anchor"></span>Figure 123: Problem Documents Detail

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/124.png)

3.  Select the REPLACE button. The Replace Document dialog box displays.

<span id="_Toc222734539" class="anchor"></span>Figure 124: Replace Document Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/125.png)

4.  Select choose from folder. The File Explorer dialog box will display. Users also have the option to drag files into the file box.

<span id="_Toc222734540" class="anchor"></span>Figure 125: File Explorer Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/126.png)

5.  From File Explorer, select the desired document to upload.

<span id="_Toc222734541" class="anchor"></span>Figure 126: Replace Document Dialog Box – File Selected

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/127.png)

6.  Select an option from the Issues Corrected (\*Required) drop-down menu. Users may select multiple options.
7.  Add a comment in the Comments (\*Required) field.
8.  Select REPLACE DOCUMENT to complete the process.
39. The replaced file will remain in the Problem Documents queue. If you would like to index or transfer the file, you can do so from the Problem Documents queue by selecting file in the file list, then selecting the INDEX button. Further instructions on indexing can be found in [Section 4.2](#indexing-files). For further instructions on transferring files, refer to [Section 4.3](#transferring-files).

### Missing RFS Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If EPSI detects a missing signature on an RFS form, the TransferDocument window will display with options pre-populated to send the document to the user’s Problem Documents queue.

<span id="_Toc222734542" class="anchor"></span>Figure 127: Transfer Document Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/128.png)

1.  Review the pre-populated fields and modify the choices as needed. For example, add an additional reason to the Reasons For Transfer field, if necessary.
2.  Select the TRANSFER DOCUMENT button. A confirmation banner will display to indicate that the transfer was successful.

<span id="_Toc222734543" class="anchor"></span>Figure 128: Transfer Successful

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/129.png)

## Quality Assurance Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Quality Assurance monitoring role determines if a file has been indexed, submitted, and queued for upload correctly.

### Reviewing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To review files, complete the following steps:

1.  From the EPSI main menu, confirm the Quality Assurance role by selecting the QUALITY ASSURANCE tab. The Quality Assurance dashboard page displays.

<span id="_Toc222734544" class="anchor"></span>Figure 129: Quality Assurance Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/130.png)

69. From the Select Indexer drop-down menu, select the Indexer that needs auditing. The files associated with the selected Indexer will display below their name and the number of files will display at the top. By default, reviewed files are hidden from the list.

<span id="_Toc222734545" class="anchor"></span>Figure 130: QA File List Default View

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/131.png)

10. To view all files from the default view, select the file number link to expand the list.
40. In the file list, icons will display to the right of files that have been reviewed. A redX indicates that a file has previously failed QA review. A greencheckmark indicates that a file has previously passed QA review. If there is no icon next to a file, that file has not yet been reviewed by that QA user.

<span id="_Toc222734546" class="anchor"></span>Figure 131: QA File List Icons

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/132.png)

11. To switch to a different Indexer, select the blueX in the Select Indexer drop-down menu to clear the current name, then select a new user.
70. Select the file that needs reviewing. The document details and review fields display. The document details include:
- Veteran Name
- Integration Control Number (ICN)
- Date of Birth
- Identifier (Last Name Initial + Last 4 of SSN)
- Consult/New Note/Existing Note
- Date of Service (Procedure/Event)
- Specialty
- Procedure
- Total Pages in Document
- Indexed By

<span id="_Toc222734547" class="anchor"></span>Figure 132: Reviewing a Document

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/133.png)

71. Review each page of the file for quality and accuracy. The naming convention of the file includes the patient’s name and the Date of Service (Procedure/Event).
72. If the file was indexed and uploaded correctly, select the Passed radio option. If the file was not indexed and uploaded correctly, select the Failed option. When this option is selected, Reasons for Failure will convert to a required field.

<span id="_Toc222734548" class="anchor"></span>Figure 133: Quality Assurance – Reasons for Failure

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/134.png)

73. If the file failed, select the reason from the Reasons for Failure (\*Required) drop-down menu. Users can add multiple reasons, if necessary.
74. Add text to the Reviewer Note field. This is an optional field with a 4,096-character limit.
75. Select the REVIEW DOCUMENT button. A green check mark next to the file name in the QA file list will indicate that the review was completed. A banner will display stating the file has been successfully updated to reviewed.

<span id="_Toc127351778" class="anchor"></span>Figure 134: Quality Assurance - Reviewed Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/135.png)

76. If the file was incorrectly indexed, contact the appropriate user to have it corrected.

## Administrator Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administrator role monitors the users that can access EPSI and view their access roles and permissions. The Administrator can also create, edit, and export data tables.

<span id="_Toc126224018" class="anchor"></span>Figure 135: Administrator Settings

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/136.png)

- Consult Notes: This function allows users to view, edit, and delete consult notes.
- User Administration: This function allows admin users to view user access roles and permissions.
- Internal Transfer: This function allows users to transfer files from one Indexer to another.
- Document Status: This function allows users to review file statuses.

### Consult Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consult Notes section within the Administrator tab allows consults to be mapped to a Note Title, Specialty, Procedure, Type, and Origin.

#### Adding Consult Notes Workflow

To add consult notes, complete the following steps:

1.  From the EPSI main menu, confirm the Administrator role by selecting the ADMINISTRATOR tab. The Administrator dashboard displays.

<span id="_Toc126224019" class="anchor"></span>Figure 136: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/137.png)

2.  To add a consult note, select the ADD ROW button in the top right corner of the Administrator dashboard. The Add Consult Note dialog box will display.

<span id="_Toc126224021" class="anchor"></span>Figure 137Error! No sequence specified.: Add Consult Note Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/138.png)

3.  Select a Consult Name (\*Required) from the drop-down menu.
4.  Select a Note Title (\*Required) from the drop-down menu.
5.  Select a Specialty(\*Required) from the drop-down menu.
6.  Select a Procedure(\*Required) from the drop-down menu.
7.  Select a Type (\*Required) from the drop-down menu.
8.  Select an Origin (\*Required) from the drop-down menu.
9.  Select ADD CONSULT NOTE to finish adding the consult note. A banner will display to indicate the consult note was successfully added.

<span id="_Toc126224022" class="anchor"></span>Figure 138: Consult Note Added Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/139.png)

#### Editing Consult Notes Workflow

To edit consult notes, complete the following steps:

<span id="_Toc222734554" class="anchor"></span>Figure 139: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/140.png)

1.  

From the Administrator dashboard, select the blue pencil icon \[![](enterprise-precision-scanning-and-indexing-epsi-user-guide/141.png)\] under the Actions column. The Edit Consult Note dialog box will display to make the appropriate updates.<span id="_Toc222734555" class="anchor"></span>Figure 140: Edit Consult Note Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/142.png)

77. Update the consult note as needed.
78. Select EDIT CONSULT NOTE to complete the update. A banner will display to indicate the consult note was successfully updated.

<span id="_Toc222734556" class="anchor"></span>Figure 141: Consult Note Edited Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/143.png)

#### Deleting Consult Notes Workflow

To delete consult note mappings within EPSI, complete the following steps:

<span id="_Toc222734557" class="anchor"></span>Figure 142: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/144.png)

1.  

Error! No sequence specified.: Delete Consult Note Dialog BoxFrom the Administrator dashboard, select red ‘X’ under the Actions column. A Delete Consult Note dialog box will display to confirm the deletion.<span id="_Toc222734558" class="anchor"></span>Figure 143

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/145.png)

79. Select DELETE CONSULT NOTE. A banner will display to indicate the consult note was successfully deleted.

<span id="_Toc126224026" class="anchor"></span>Figure 144: Consult Note Deleted Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/146.png)

### User Administration Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In EPSI, the User Administration page displays all users for a given site, along with their currently assigned roles. This page is view-only and is provided for informational and reporting purposes.

41. Changes to active users or user roles cannot be made within EPSI. To add new users, remove users, or alter user roles, EPSI site Administrators must make changes via the IAM Provisioning Toolkit.

To view a site’s current user roles, complete the following steps:

1.  

From the EPSI top menu, select the Administrator role by selecting the ADMINISTRATOR tab. The Administrator dashboard page displays.<span id="_Toc222734560" class="anchor"></span>Figure 145: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/147.png)

2.  

From the bottom left corner of the dashboard, select the SETTINGS button, and select User Administration. The User Administration page displays.<span id="_Toc222734561" class="anchor"></span>Figure 146: User Administration Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/148.png)

3.  
12. All users for the site you are logged into will be listed. To look up assigned roles of a specific user, enter a name in the Search By User field and select the SEARCH button.For instructions on exporting the User Administration table, refer to [Section 4.7.5](#files-can-be-located-by-reviewing-each-page-of-the-file-list-entering-the-file-name-in-the-search-by-file-name-field-or-entering-a-date-in-the-created-or-last-modified-fields.-filter-by-user-via-the-user-drop-down-menu-or-by-file-status-via-the-status-drop-down-menu.to-remove-any-search-or-filter-select-the-clear-button.exporting-tables-workflow).

### Internal Transfer Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators can transfer files from one EPSI user to another user within the same site that the Administrator is logged into. To transfer files, complete the following steps:

1.  

From the EPSI main menu, select the ADMINISTRATOR tab. The Administrator dashboard page displays.<span id="_Toc222734562" class="anchor"></span>Figure 147: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/149.png)

2.  

From the bottom left corner of the dashboard, select the SETTINGS button, and select Internal Transfer. The Internal Transfer page displays.<span id="_Toc222734563" class="anchor"></span>Figure 148: Internal Transfer Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/150.png)

42. If the selected user’s document list contains split files, the checkboxes for the parent files will be greyed out, indicating that these items are not selectable for transfer. Only the child documents of split files are transferable.
43. If all children of a split are transferred by an Administrator, the parent document will no longer display in that user’s queue.
3.  
44. Select a user from the TransferFrom list.If the selected user does not have any documents pending indexing, the following message will display in the file list: Selected user has no documents that are pending indexing.
4.  

Once a user has been selected, you can select the appropriate file(s) to transfer. A check mark will be displayed next to all selected files.<span id="_Toc222734564" class="anchor"></span>Figure 149: Transfer Documents-Checkbox Selected

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/151.png)

5.  
6.  

Select a user from the TransferTo list.Select the TRANSFER DOCUMENTS button to complete the file transfer. A banner will display to indicate that the file has been successfully transferred.<span id="_Toc222734565" class="anchor"></span>Figure 150: File Transferred Confirmation

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/152.png)

45. If a user with the Indexer role is selected, the document list will include files from that user’s Work Queue and Received Transfers queue, with the Work Queue files listed first.
46. If transferring a file for a Nurse, the document list will only be populated with files from the chosen user’s Received Transfers queue.
47. Administrators cannot transfer files that are in a user’s Problem Documents queue.

### Document Status Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators—along with all other users—can review the status of the files within EPSI.

To review a file’s status using the Administrator role, complete the following steps:

1.  

From the EPSI main menu, select the ADMINISTRATOR tab. The Administrator dashboard page displays.<span id="_Toc222734566" class="anchor"></span>Figure 151: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/153.png)

2.  

From the bottom left corner of the dashboard, select the SETTINGS button, and select Document Status. The Document Status page displays.<span id="_Toc222734567" class="anchor"></span>Figure 152: Document Status Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/154.png)

3.  
4.  
5.  

### Files can be located by reviewing each page of the file list, entering the file name in the Search by File Name field, or entering a date in the Created or Last Modified fields. Filter by user via the User drop-down menu or by file status via the Status drop-down menu.To remove any search or filter, select the CLEAR button.Exporting Tables Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For EPSI Administrators, three tables can be exported into a spreadsheet: the Consult Notes table, the User Administration table, and the DocumentStatus table. To export a table as a comma-separated values (CSV) file, complete the following steps:

1.  

Select the ADMINISTRATOR tab. The Administrator dashboard displays.<span id="_Toc222734568" class="anchor"></span>Figure 153: Administrator Dashboard

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/155.png)

2.  
13. Ensure you are on the correct page for the table you would like to export. The Consult Notes table displays by default when first navigating to the Administrator tab. If you would like to export a different table, select the SETTINGS button, choose the desired table from the available options (Consult Notes, User Administration, Transfer Documents, or Document Status), then select CLOSE.

<span id="_Toc222734569" class="anchor"></span>Figure 154: Settings Button Options

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/156.png)

3.  

Select the Export to CSV link at the far-right of the page. A dialog box will display asking what you would like to do with the file (Open or Save as).<span id="_Toc222734570" class="anchor"></span>Figure 155: Open or Save As Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/157.png)

48. The CSV file will include all pages of the table regardless of which page of the table you’re currently viewing.
4.  
5.  

Choose whether you would like to Open the file or Save as. The default name of the file will depend on which table you choose to export.If Open is selected, the CSV file will open in Excel.<span id="_Toc222734571" class="anchor"></span>Figure 156: CSV File Example

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/158.png)

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

49. Reports can only be generated by EPSI users with the Administrator role.

To generate a report for the site you are currently logged into, complete the steps in the sections that follow.

### Documents Indexed by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  

Select the REPORTS tab from the EPSI top menu. The Reports dashboard displays. The Documents Indexed by User page is displayed by default.<span id="_Toc222734572" class="anchor"></span>Figure 157: Documents Indexed by User Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/159.png)

50. The From and To fields both default to the current date.
51. Report date ranges cannot include dates more than 30 days before the current date. Report date ranges also cannot include future dates.
2.  
3.  
4.  

Select the desired date in the From (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar.Select the desired date in the To (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar. Select the GET REPORT button to generate the report table. The report displays.<span id="_Toc222734573" class="anchor"></span>Figure 158: Generated Report

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/160.png)

14. Selecting a user’s name from the report opens a Status page with detailed information on all files uploaded by that user.
15. Users can sort columns in ascending or descending order by selecting individual table headers.

### Problem Documents in Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  

Select the REPORTS tab from the EPSI top menu. The Reports page displays.<span id="_Toc222734574" class="anchor"></span>Figure 159: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/161.png)

80. Select Problem Documents in Queue in the left-side panel. The Problem Documents in Queue page displays.

<span id="_Toc222734575" class="anchor"></span>Figure 160: Problem Documents in Queue Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/162.png)

81. Select the Reason drop-down menu and make a selection.

<span id="_Toc222734576" class="anchor"></span>Figure 161: Reason Drop-Down Menu

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/163.png)

82. Select the GET REPORT button. The report is generated.
52. If there is no data available for a given selection, the following message will be displayed instead of a report: No data found, please try adjusting your filters.

<span id="_Toc222734577" class="anchor"></span>Figure 162: No Data Found

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/164.png)

<span id="_Toc222734578" class="anchor"></span>Figure 163: Generated Report

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/165.png)

16. Users can sort columns in ascending or descending order by selecting individual table headers.

### Problem Documents in Queue Detailed Export

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  

Select the REPORTS tab from the EPSI top menu. The Documents Indexed by User page displays by default.<span id="_Toc222734579" class="anchor"></span>Figure 164: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/166.png)

83. Select Problem Documents in Queue Detailed Export in the left-side panel. The Problem Documents in Queue Detailed Export page displays.

<span id="_Toc222734580" class="anchor"></span>Figure 165: Problem Documents in Queue Detailed Export Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/167.png)

84. Select the EXPORT REPORT button. A Downloads dialog box will display asking what you would like to do with the file (Open or Save as).

<span id="_Toc222734581" class="anchor"></span>Figure 166: Downloads Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/168.png)

85. Choose whether you would like to Open the file or Save as. If Open is selected, the CSV file will open in Excel.

<span id="_Toc222734582" class="anchor"></span>Figure 167: Problem Documents in Queue Detailed Export Example

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/169.png)

### QA Total Files Audited

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

53. VistA QA and EPSI QA are not linked. Running reports using VistA QA will not generate data for documents within EPSI. Users who want to run QA reports on files in EPSI must do so within the EPSI application.
1.  

Select the REPORTS tab from the EPSI main menu. The Documents Indexed by User page displays by default.<span id="_Toc222734583" class="anchor"></span>Figure 168: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/170.png)

2.  

Select QA Total Files Audited in the left-side panel. The QA Total Files Audited page displays.<span id="_Toc222734584" class="anchor"></span>Figure 169: QA Total Files Audited Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/171.png)

54. The From and To fields both default to the current date.
55. Report date ranges cannot include dates more than 30 days before the current date. Report date ranges also cannot include future dates.
3.  
4.  
5.  

Select the desired date in the From (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar.Select the desired date in the To (\*Required) field.Select the GET REPORT button to generate the report table. The report displays.<span id="_Toc222734585" class="anchor"></span>Figure 170: QA Total Files Audited

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/172.png)

17. Users can sort columns in ascending or descending order by selecting individual table headers.

### QA Detailed Auditing Export

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  

Select the REPORTS tab from the EPSI main menu. The Documents Indexed by User page displays by default.<span id="_Toc222734586" class="anchor"></span>Figure 171: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/173.png)

86. Select QA Detailed Auditing Export in the left-side panel. The QA Detailed Auditing Export page displays.

<span id="_Toc222734587" class="anchor"></span>Figure 172: QA Detailed Auditing Export Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/174.png)

56. The From and To fields both default to the current date.
57. Report date ranges cannot include dates more than 30 days before the current date. Report date ranges also cannot include future dates.
87. Select the desired date in the From (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar.
88. Select the desired date in the To (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar.
89. Select the EXPORT REPORT button. A Downloads dialog box will display asking what you would like to do with the file (Open or Save as).

<span id="_Toc222734588" class="anchor"></span>Figure 173: Downloads Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/175.png)

90. Choose whether you would like to Open or Save the file. If Open is selected, the CSV file will open in Excel.

<span id="_Toc222734589" class="anchor"></span>Figure 174: QA Detailed Auditing Export Example

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/176.png)

### Documents Removed by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  

Select the REPORTS tab from the EPSI main menu. The Documents Indexed by User page displays by default.<span id="_Toc222734590" class="anchor"></span>Figure 175: Reports Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/177.png)

6.  

Select Documents Removed by User in the left-side panel. The Documents Removed By User page displays.<span id="_Toc222734591" class="anchor"></span>Figure 176: Documents Removed By User Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/178.png)

58. The From and To fields both default to the current date.
59. Report date ranges cannot include dates more than 30 days before the current date. Report date ranges also cannot include future dates.
7.  
8.  
9.  

Select the desired date in the From (\*Required) field. Users can either type in the date manually or select the calendar icon within the field and choose a date from the calendar.Select the desired date in the To (\*Required) field.Select the GET REPORT button to generate the report table.<span id="_Toc222734592" class="anchor"></span>Figure 177: Documents Removed By User Report Table

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/179.png)

60. If you wish to review the history of the file, select the See Details link under the File History column. A File History dialog box will display listing the previous actions completed on the file.

<span id="_Toc222734593" class="anchor"></span>Figure 178: File History Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/180.png)

10. 

Select the EXPORT button. A Downloads dialog box will display asking what you would like to do with the file (Open or Save as).<span id="_Toc222734594" class="anchor"></span>Figure 179: Downloads Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/181.png)

11. 

Choose whether you would like to Open or Save the file. If Open is selected, the CSV file will open in Excel.<span id="_Toc222734595" class="anchor"></span>Figure 180: Documents Removed Report Example

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/182.png)

### Exporting and Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After generating a report in EPSI, users have the option to either EXPORT the report as a CSV file or PRINT the report.

<span id="_Toc222734596" class="anchor"></span>Figure 181: Example Report

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/183.png)

1.  

To export a report, select the EXPORT button. A Downloads dialog box will display asking what you would like to do with the file (Open or Save as).<span id="_Toc222734597" class="anchor"></span>Figure 182: Downloads Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/184.png)

2.  
3.  

Choose whether you would like to Open or Save the file.Alternatively, to print the file, select the PRINT button under the generated report in EPSI. A new tab will open displaying the report table.<span id="_Toc222734598" class="anchor"></span>Figure 183: Report Table – Print View

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/185.png)

4.  

From the newly generated report tab, print the page by pressing CTRL+P or selecting Print from the browser menu. The Print dialog box displays.<span id="_Toc222734599" class="anchor"></span>Figure 184: Print Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/186.png)

5.  
18. Select the desired printer from the Printer drop-down menu, then select the Print button.You can save the report as a PDF by selecting Print to PDF from the Printer drop-down menu.

## Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All user roles can review the status of the files within EPSI. Refer to [Appendix B](#_Appendix_B:_File) for an explanation of each status.

### Checking Current Processing Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To review a file’s current processing status, complete the following steps:

1.  

From the main menu, select the STATUS tab. The Status page displays.<span id="_Toc222734600" class="anchor"></span>Figure 185: Status Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/187.png)

2.  
- Files can be located by reviewing each page of the file list or filtering by any of the following column headings:File Name
- Status
- File Queue
- Created By
- Created
- Indexed By
- Last Modified
3.  
19. Select the magnifying glass icon in the File Name, Created, or Last Modified fields to enter a search term. Documents containing that term will display in the file list.To view more information on a given status, select the text in the Status column and a dialog box will display with additional details.

<span id="_Toc222734601" class="anchor"></span>Figure 186: Status Detail Dialog Box (Pending)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/188.png)

<span id="_Toc222734602" class="anchor"></span>Figure 187: Status Detail Dialog Box (Complete)

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/189.png)

### Exporting Document Status Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All EPSI user roles can export the DocumentStatus table to an Excel spreadsheet (CSV file). To export the table, complete the following steps:

1.  

Select the STATUS tab. The Current Processing Status page will display.<span id="_Toc222734603" class="anchor"></span>Figure 188: Current Processing Status Page

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/190.png)

2.  

Select the Export to CSV link on the right side of the page. A Downloads dialog box will display asking what you would like to do with the file (Open or Save as).<span id="_Toc222734604" class="anchor"></span>Figure 189: Downloads Dialog Box

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/191.png)

61. The CSV file will include all pages of the table regardless of which page you’re currently viewing.
3.  
4.  

Choose whether you would like to Open or Save the file. The default name of the file will be Current Processing Status.If Open is selected, the CSV file will open in Excel.<span id="_Toc222734605" class="anchor"></span>Figure 190: Exported Document Status Table Data

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/192.png)

## Troubleshooting and Common Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EPSI Registration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you completed the steps detailed in [Section 3.1](#logging-on) and you are still having issues logging into EPSI, complete the steps that follow.

When you register with EPSI, confirmation emails go to the site Administrator and your Active Directory Supervisor. However, if your supervisor is incorrect in Active Directory, your approval email will be sent to the wrong person. If you need to change the Active Directory Supervisor listed, you must contact your Local IT to change it to the correct name.

20. If you need to change the Active Directory Supervisor listed, you must contact your Local IT to change it to the correct name.
21. If both the Active Directory Supervisor and Site Administrator have approved your request and you still cannot log in to EPSI, please submit a YourIT ticket that contains as much information as you can provide, including your site number, errors, consult IDs, names, screenshots, and timestamps (as necessary). Include Please route to EPSI Triage Assignment Group in the Brief Description of Issue.

### VistA Upload Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222734606" class="anchor"></span>Figure 191: Step 4 - Upload Screen

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/193.png)

Users with an Indexer or Nurse role can send a document into a queue to be uploaded to VistA Imaging by selecting the QUEUE UPLOAD button in the final step of their consult.

If a user queues a document for upload but the document fails to be passed to VistA Imaging, an error message will display.

<span id="_Toc222734607" class="anchor"></span>Figure 192: Upload Failure Message

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/194.png)

Here is a dissection of the error message:

- Error: Pre Check Failure:0^Invalid Association between Spec/SubSpec and Proc/Event Type
  - 
  - 
- Error: Pre Check Failure is EPSI stating VistA will not accept this upload.0^Invalid Association between Spec/SubSpec and Proc/Event Type is the error message that VistA generated.Class: MEDICAL RECORD - CLIN
  - 
- Context for the conflicting data.Specialty/SubSpecialty: MEDICINE
  - 
- The Specialty with the conflicting Procedure.Procedure/Event: OCCUPATIONAL THERAPY
  - 

The Procedure in conflict with the Specialty.VistA can return a wide variety of error messages, but this example is a common one that occurs when a user attempts to complete an action in EPSI using a Specialty/Procedure combination that VistA does not allow.

62. If the site Administrator has completed the consult mappings correctly, these types of errors should not occur.

### Token Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Switching Sites

Another common error a user might encounter when attempting to log into EPSI is a token error message that states, Token is not valid.

<span id="_Toc222734608" class="anchor"></span>Figure 193: Token Error

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/195.png)

If you receive this error and have access to multiple sites, you can attempt to log in from another site. Follow the steps below to log in from another site:

1.  

Select the \> icon next to Current Site in the top-right corner of the page. A list of available sites will display.<span id="_Toc222734609" class="anchor"></span>Figure 194: Site List

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/196.png)

91. Select a different site from the Sites drop-down list and that site number will display in the Current Site field.

#### Invalid Token Error for Cerner Users

The VA is in the process of replacing VistA with Cerner, a commercial-off-the-shelf (COTS) electronic health record system. As part of the rollout, some EPSI users are being given access to Cerner. However, the process of granting Cerner access involves de-linking a user’s VistA account from their VA account for all sites. Since a user cannot access EPSI without a linked VistA account, users will not have access to EPSI until their VistA account link is reestablished.

If a user has been granted access to Cerner and attempts to log in to EPSI, a Token is not valid error message will display.

<span id="_Toc222734610" class="anchor"></span>Figure 195: EPSI Error: Invalid Token

![](enterprise-precision-scanning-and-indexing-epsi-user-guide/197.png)

If you encounter this error, navigate to the [Identity Management Toolkit page](https://mvitk.iam.va.gov/imdquiWeb/login.action) and verify if your VA account is still linked to VistA.

# | Acronym   | Definition                                                      |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----------|-----------------------------------------------------------------|
| API   | Application Programming Interface                               |
| AWS   | Amazon Web Services                                             |
| BIM   | Business Implementation Manager                                 |
| CC    | Community Care                                                  |
| CD2   | Critical Decision 2                                             |
| CDW   | Corporate Data Warehouse                                        |
| CPRS  | Computerized Patient Record System                              |
| COTS  | Commercial Off The Shelf                                        |
| CSV   | Comma-Separated Values                                          |
| CTB   | Consult Toolbox                                                 |
| CVIX  | Central VistA Imaging Exchange                                  |
| DB    | Database                                                        |
| DOB   | Date of Birth                                                   |
| EHR   | Electronic Health Record                                        |
| EPSI  | Enterprise Precision Scanning and Indexing                      |
| FAQ   | Frequently Asked Questions                                      |
| IAM   | Identity and Access Management                                  |
| ICN   | Integration Control Number                                      |
| IDP   | Intelligence Document Processing                                |
| IVC   | Integrated Veteran Care                                         |
| MVP   | Minimum Viable Product                                          |
| OCR   | Optical Character Recognition                                   |
| PDF   | Portable Document Format                                        |
| PII   | Personally Identifiable Information                             |
| PHI   | Protected Health Information                                    |
| PIV   | Personal Identity Verification                                  |
| REST  | Representational State Transfer                                 |
| RFS   | Request for Service                                             |
| RN    | Registered Nurse                                                |
| SSN   | Social Security Number                                          |
| UI    | User Interface                                                  |
| URL   | Uniform Resource Locator                                        |
| USC   | United States Code                                              |
| VA    | Department of Veterans Affairs                                  |
| VAEC  | VA Enterprise Cloud                                             |
| VIP   | Veteran-focused Integration Process                             |
| VISN  | Veterans Integrated Service Network                             |
| VistA | Veterans Health Information Systems and Technology Architecture |
| VIX   | VistA Imaging Exchange                                          |
| VPN   | Virtual Private Network                                         |

<span id="_Appendix_B:_File" class="anchor"><span id="_Toc222734213" class="anchor"></span></span>Appendix B: File Status and Explanations<span id="_Toc222734414" class="anchor"></span>Table 5: File Status and Explanations

# # | Status                                                                 | Explanation                                                                                                                                                                                                                       |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Indexing Successful                                                | The document was sent successfully to the Vista Imaging background processor for upload into Vista Imaging.                                                                                                                       |
| Image Passed To VistA and Sent To Registered Nurse (RN) for Review | The document has been sent to the VistA Imaging background processor for upload into VistA Imaging. Additionally, the document was marked as Needs Clinical Review and has been transferred to the selected Nurse for review. |
| Parent File Split Complete                                         | The parent document has been received and split into child files. Child files must be handled (i.e., transferred or indexed) to remove the parent file from view.                                                                 |
| Pending Indexing                                                   | Document has not yet begun the indexing process or been split.                                                                                                                                                                    |
| Pending Indexing and Sent to RN for Review                         | The document was transferred to a Nurse and is pending indexing by the Nurse.                                                                                                                                                     |
| Pending Indexing and Transferred to Another User                   | The document was transferred to another user and is pending indexing by that user.                                                                                                                                                |
| Pending VistA Imaging Processing                                   | The document was sent to the VistA Imaging background processor for upload into VistA Imaging and imaging processing is pending.                                                                                                  |
| Pending Vista Imaging Processing and Sent to RN for Review         | The document has been sent to the Vista Imaging background processor for uploading into Vista Imaging. Additionally, the document was marked as high risk and has been transferred to the selected nurse for review.              |

<span id="_Toc222734415" class="anchor"></span>Table 6: Facility File Name Structures

# <span id="_Toc222734214" class="anchor"></span>Appendix C: Facility File Name StructuresWhen documents are uploaded into EPSI, if the file name follows a specific structure, the application will automatically detect patient or consult information. Any information extracted from the file name will auto-populate into the appropriate field. For example, if a patient name is detected, EPSI will generate search results based on the file name structure specific to that facility.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Station ID/Site Number | Facility                                                                         | File Name Structure                                                                 |
|------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 618                    | Minneapolis VA Medical Center – Minneapolis MN                                   | VeteranLastName_FirstName_last4SSN_DateOfService                                    |
| 621                    | James H. Quillen Department of Veterans Affairs Medical Center—Mountain Home, TN | veteranname,last4_SSN,dateofservice,consultnumber,uniquecode,location,bypasslowrisk |
| 636                    | Omaha VA Medical Center—VA Nebraska-Western Iowa HCS                             | VeteranLastName_FirstName_last4SSN_DateOfService                                    |