---
title: VAP Version 1 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: VAP
app_name: Veterans Authorization and Preferences
section: CLI
app_status: active
pkg_ns: VAP
patch_ver: 1
patch_id: VAP*1
group_key: "VAP:VAP:1"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Veterans Authorizations and Preferences (VAP) project in the Virtual Lifetime Electronic Record (VLER) Initiative is responsible for authorizing Health Information Exchange (HIE) to trusted external partners and managing Veteran Electronic Consent Directives. The VAP project creates an enterpr
audience: 
keywords: 
  - date
  - report
  - patient
  - table
  - strong
  - facility
  - figure
  - exchange
  - contents
  - ehealth
page_count: 0
word_count: 37275
section_count: 30
table_count: 0
figure_count: 1
appendix_count: 4
has_toc: False
is_stub: False
pub_date: August 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Veterans_Authorization_and_Preferences_(VAP)/VAPE_User_Guide_2_7_0_20170427.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Veterans_Authorization_and_Preferences_(VAP)/VAPE_User_Guide_2_7_0_20170427.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=222"
---

# Veterans Authorizations and Preferences (VAP) User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Veterans Authorizations and Preferences (VAP) User Guide](#veterans-authorizations-and-preferences-vap-user-guide)
    - [August 2018 Department of Veterans Affairs](#august-2018-department-of-veterans-affairs)
    - [Revision History](#revision-history)
    - [Artifact Rationale](#artifact-rationale)
    - [Table of Figures](#table-of-figures)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
    - [Log In to the Application](#log-in-to-the-application)
  - [System Menu](#system-menu)
    - [Primary Menu Options](#primary-menu-options)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Understanding the Workflow](#understanding-the-workflow)
  - [Exit System](#exit-system)
    - [Log Out of the VAP Application](#log-out-of-the-vap-application)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Using the Software](#using-the-software)
  - [Searching for a Patient](#searching-for-a-patient)
    - [Search for a Patient](#search-for-a-patient)
    - [Patient Summary Tab](#patient-summary-tab)
  - [Patient Details Screen](#patient-details-screen)
    - [Health Summary (C32) Tab](#health-summary-c32-tab)
    - [Health Summary (C-CDA) Tab](#health-summary-c-cda-tab)
  - [Patient Consent Directive](#patient-consent-directive)
    - [eHealth Exchange Record Sharing](#ehealth-exchange-record-sharing)
    - [Restricting eHealth Exchange Record Sharing](#restricting-ehealth-exchange-record-sharing)
  - [Admin](#admin)
    - [Batch Announce Patients](#batch-announce-patients)
    - [Manage Batches](#manage-batches)
    - [Service Audit](#service-audit)
    - [Partner Organization](#partner-organization)
    - [Monthly Received Documents](#monthly-received-documents)
    - [Facilities](#facilities)
  - [Generating Summary Reports](#generating-summary-reports)
    - [Dashboard](#dashboard)
    - [Disclosures Summary](#disclosures-summary)
    - [Received eHealth Exchange Documents Summary](#received-ehealth-exchange-documents-summary)
    - [Document Size](#document-size)
    - [Consent Directive Summary](#consent-directive-summary)
    - [Opt-In Summary](#opt-in-summary)
    - [Delayed Consent Summary](#delayed-consent-summary)
    - [Patient Discovery Audit Summary](#patient-discovery-audit-summary)
  - [Generating Detailed Reports](#generating-detailed-reports)
    - [Disclosures Detailed](#disclosures-detailed)
    - [Received eHealth Exchange Documents Detailed](#received-ehealth-exchange-documents-detailed)
    - [Consent Directive Detailed](#consent-directive-detailed)
    - [Opt-In Detailed](#opt-in-detailed)
    - [Expiring Consent](#expiring-consent)
    - [Delayed Consent Detailed](#delayed-consent-detailed)
    - [Patient Discovery Audit Detailed](#patient-discovery-audit-detailed)
    - [Scheduled Exports](#scheduled-exports)
    - [Data Quality Export](#data-quality-export)
    - [Data Quality Upload Transmission Log](#data-quality-upload-transmission-log)
  - [Viewing the User Guide](#viewing-the-user-guide)
    - [View the User Guide for the Application](#view-the-user-guide-for-the-application)
  - [Advanced Scheduling](#advanced-scheduling)
  - [Expiring Consent Notification](#expiring-consent-notification)
    - [Schedule Expiring Consent Details](#schedule-expiring-consent-details)
  - [Setting a Default Facility](#setting-a-default-facility)
    - [Setting a Default Facility When No Default is in Place](#setting-a-default-facility-when-no-default-is-in-place)
  - [Viewing Build Information](#viewing-build-information)
    - [View Build Information for the Application](#view-build-information-for-the-application)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix](#appendix)
  - [Appendix A: Definitions](#appendix-a-definitions)
  - [Appendix B: Changing the File Type Associated with a Document](#appendix-b-changing-the-file-type-associated-with-a-document)
  - [Appendix C: Batch Announce](#appendix-c-batch-announce)
    - [Challenges](#challenges)
    - [Batch Announce Steps](#batch-announce-steps)
    - [Story Description](#story-description)
    - [Conversation/Narrative](#conversationnarrative)
    - [Analysis Steps and Process](#analysis-steps-and-process)
    - [Acceptance Criteria/Compliance](#acceptance-criteriacompliance)
  - [Appendix D: Tool Tips and User Friendly Error Messages](#appendix-d-tool-tips-and-user-friendly-error-messages)
    - [Tool Tips (Hover Overs)](#tool-tips-hover-overs)
    - [User Friendly Error Messages](#user-friendly-error-messages)
![](vap-version-1-user-guide/001.png)

### August 2018 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/07/2018</td>
<td>6.2</td>
<td>PMO Review</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>08/01/2019</td>
<td>6.1</td>
<td><p>Updated documentation provides details of the VAP 3.2.0 functionality. Enhancements within this release include the following:</p>
<ul>
<li><p>Additional error-handling and modifications to the batch announce workflow</p></li>
<li><p>Revisions to the Patient Details page</p></li>
<li><p>Non-functional enhancements to the system configuration files (detailed within the System Design Document (SDD)</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>07/12/2018</td>
<td>6.0</td>
<td>Updated for 508 compliance</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>6/13/2018</td>
<td>5.9</td>
<td>Updated for 508 compliance</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>06/11/2018</td>
<td>5.8</td>
<td>Updated for 508 compliance</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>05/17/2018</td>
<td>5.7</td>
<td>PMO Review</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>05/09/2018</td>
<td>5.6</td>
<td><p>Updated documentation to provide details of the VAP Release 3.1.0 functionality. Enhancements within this release include the following:</p>
<ul>
<li><p>Modification of C-CDA stylesheets to use latest</p></li>
</ul>
<blockquote>
<p>R.2.1 stylesheet templates</p>
</blockquote>
<ul>
<li><p>Functionality to delete exports from the <em>Scheduled Exports</em> queue</p></li>
<li><p>Revisions of the <em>Dashboards</em> section for 508 compliance</p></li>
<li><p>Creation of <em>Advanced Scheduling</em> functionality to allow users to schedule exporting of reports in advance</p></li>
<li><p>Minor modifications due to 508 Compliance updates</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>3/1/2018</td>
<td>5.5</td>
<td>Updated phrasing in sections 4.5.8.1 and 4.6.7. to address feedback from HPS.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2/23/2018</td>
<td>5.4</td>
<td>Updated for 508 compliance</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>01/26/2018</td>
<td>5.3</td>
<td><p>Updated document to add VAP 3.0.0 functionality. This included:</p>
<ul>
<li><p>Updates to the Opt-In (Summary and Detailed) reports, Patient Discovery Audit (Summary and Detailed) reports, and Received eHealth Exchange report (Detailed) to add additional filtering options and display columns.</p></li>
<li><p>Updates to calendar date pickers to be 508 compliant</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>12/26/2017</td>
<td>5.2</td>
<td>Template review and formatting in preparation for VAPP2 Build 1 updates.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>10/10/2017</td>
<td>5.1</td>
<td><p>Updated sub-sections 4.5.2, 4.5.3, 4.5.4, 4.5.5, 4.5.6, 4.5.7,</p>
<p>4.6.1, 4.6.2, 4.6.3, 4.6.4, 4.6.5, 4.6.6, and 4.6.7 by removing</p>
<p>sentence: The name of the file is generated in the following format: [Report_Title]_[Detail/Summary]_Report_YYYYMMDD_HH mmss.[xls/csv]; Updated Cover Page, and footers.</p></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>09/28/2017</td>
<td>5.0</td>
<td>Delivery to VA (Build 4)</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>09/28/2017</td>
<td>4.5</td>
<td>Updated section 4.4 removing invalid “[Report_Title]_YYYYMMDD_HHmmss.xls”sentences (subsections 4.4.4, 4.4.5, and 4.4.6). Updated cover page with new version.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>09/05/2017</td>
<td>4.4</td>
<td>PM Review</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>08/31/2017</td>
<td>4.3</td>
<td>Updated figure 165- About VAP</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>08/25/2017</td>
<td>4.2</td>
<td>Technical Writer Review; re-numbered figures and updated figure cross-references; updated paragraph formatting, cover page, footer, and tables of contents, tables and figures</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>08/14/2017</td>
<td>4.1</td>
<td>eHXE Build 4 (2.7.4) updates: Added new section for DQ Transmission Log report, updated DQ Export section and C-CDA tab, updated cover page, headers and footers, and ran 508 compliance check.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>07/20/2017</td>
<td>4.0</td>
<td>Delivery to VA Build 3, 2.7.2</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>07/18/2017</td>
<td>3.5</td>
<td>Technical Writer Review – Applied suggested changes from OIT/EPMO / HMPS Admin Team, in “review of User Guide” email from Donna Fitch.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/17/2017</td>
<td>3.4</td>
<td>Technical Writer Review – Applied suggested changes from OIT/EPMO / HMPS Admin Team, and addressed stakeholder comments.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>07/07/2017</td>
<td>3.3</td>
<td>Updated for Build 3, 2.7.2</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>06/20/2017</td>
<td>3.2</td>
<td>Technical Writer Review; re-numbered figures and updated figure cross-references; updated paragraph formatting, cover page, footer, and tables of contents, tables and figures</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>06/18/2017</td>
<td>3.1</td>
<td><p>Updated screen shots and text for Build 3 eHX Enhancements; updated sections include:</p>
<p>4.2.1 updated figures; added new section 4.2.3 Health Summary (CCDA) Tab; 4.6.9 updated figures;</p></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>05/19/2017</td>
<td>3.0</td>
<td>Delivery to VA</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>05/10/2017</td>
<td>2.4</td>
<td>Final Review – eHXE – Build 2</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>05/10/2017</td>
<td>2.3</td>
<td>Reposted eHXE Build 2 updates as follows: US.01.01.01 - CDAs are Downloaded in Bulk from VAP Interface. Added new section for Data Quality Export under Detailed Reports</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>05/02/2017</td>
<td>2.2</td>
<td>Technical Writer Review - updated Title Page, Version Number, Revision History and Footnote, TOC Indents</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>04/27/2017</td>
<td>2.1</td>
<td>Tech Review</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>04/25/2017</td>
<td>2.0</td>
<td>Validation of the final content in preparation for Build 4 Release.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>03/22/2017</td>
<td>1.9</td>
<td>Updated Version Number, Revision History, ToC, ToT, ToF.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>03/03/2017</td>
<td>1.8</td>
<td><p>This document contains all of the updates associated to the VAP 2.7.0 Release. This includes the following:</p>
<ul>
<li><p>All screenshots are updated with the new user interface updates to modernize the look and field</p></li>
<li><p>Content was added around the new report Document Size (Summary) and admin features (facility management)</p></li>
<li><p>Minor Build 4 updates to include Partner Description field</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>01/27/2017</td>
<td>1.7</td>
<td>Updated Section 3.1 with the new Logging On instructions and PIV authorization</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>12/09/2016</td>
<td>1.6</td>
<td>Updated Version Number, Revision History, ToC, ToT, ToF.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/08/2016</td>
<td>1.5</td>
<td><p>Updated document to add VAP 2.6.0 functionality. This included:</p>
<ul>
<li><p>Updated with VAP 2.6.0 screenshots containing page layout revisions</p></li>
<li><p>Updated records per page</p></li>
<li><p>Adding Section 4.1 (Reporting Dashboard)</p></li>
<li><p>Addition of Scheduled Exports</p></li>
<li><p>Addition of Monthly Received Documents Report</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>09/20/2016</td>
<td>1.4</td>
<td>Updated Version Number, Revision History, TOC, TOT, TOF.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>09/14/2016</td>
<td>1.3</td>
<td><p>Updated Section 3 to include a note about Compatibility Mode</p>
<p>Updated the document with the latest screenshots referring to VAP 2.5.0 functionality (Build 2) to include changes from User Acceptance Testing. These included:</p>
<ul>
<li><p>Screenshots</p></li>
<li><p>Addition of OID to exported reports</p></li>
<li><p>Facility Station IDs</p></li>
<li><p>Close “tabs” upon exiting pop-up reminder</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>09/07/2016</td>
<td>1.2</td>
<td>Converted to VIP template. Updated Version Number, Revision History, Artifact Rational, and ToC.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>07/15/2016</td>
<td>1.1</td>
<td><p>Update document to add VAP 2.5.0 functionality. This included:</p>
<ul>
<li><p>Delayed Consent Reports (Summary and Detailed)</p></li>
<li><p>Adding/Approving/Canceling/Printing Delayed Status authorizations</p></li>
<li><p>Mailed letters and dates</p></li>
<li><p>Facility parent/child multi-selection</p></li>
<li><p>Updated screenshots</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>05/24/2016</td>
<td>1.0</td>
<td>Tech Writer Review: Removed Section 1.2.4.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>05/23/2016</td>
<td>.08</td>
<td><p>Tech Writer Review:</p>
<p>Removed embedded cross-references.</p></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>05/09/2015</td>
<td>.07</td>
<td><p>Tech Writer Review:</p>
<p>Reviewed updates requested by the HMPS Admin Team.</p></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>05/09/2015</td>
<td>0.06</td>
<td><p>Update to incorporate feedback to User Guide updates for Version 2.4. Changes include the following:</p>
<ul>
<li><p>Clarify VAP is only accessible on VA network</p></li>
<li><p>Noted VAP links in which access may need to be requested</p></li>
<li><p>Grammatical Updates</p></li>
</ul></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/18/2016</td>
<td>.05</td>
<td><p>Tech Writer Review:</p>
<p>Incorporated User Guide content into the latest PMAS template.</p></td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>03/18/2016</td>
<td>.04</td>
<td>Updated for VAPE Version 2.4 Build 1 to include the interfacing with kiosks and electronic management of consent directives.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>10/20/2015</td>
<td>.03</td>
<td>Updated for Veterans Authorization and Preferences Enhancements Version 2.4 Build 1.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="even">
<td>8/17/2015</td>
<td>.02</td>
<td>Updated for Veterans Authorizations and Preferences (VAP) Enhancements Version 2.3 Builds 6/8.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
<tr class="odd">
<td>02/13/2015</td>
<td>.01</td>
<td>Updated for Veterans Authorization Preference (VAP) Enhancements Version 2.2 Build 3.</td>
<td><a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></td>
</tr>
</tbody>
</table>

### Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

### Table of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 1: VAP High Level Application Design 22](#_bookmark17)
> [Figure 2: VAP Access Control System High](#logging-on)[-](#3.1.1._Log_In_to_the_Application)[Level Design](#3.2._System_Menu) [23](#_bookmark26)
> [Figure 3: Compatibility View Settings 24](#logging-on)
> [Figure 4: Login Screen 25](#3.1.1._Log_In_to_the_Application)
> [Figure 5: Home Page for ROI Administrator or ROI Operator 26](#3.2._System_Menu)
> [Figure 6: Using the Application 26](#_bookmark26)
> [Figure 7: VAP Logout 30](#_bookmark37)
> [Figure 8: Logout Confirmation 30](#_bookmark38)
> [Figure 9: Logout Screen 31](#_bookmark40)
> [Figure 10: Patient Search Screen 32](#_bookmark44)
> [Figure 11: Patient Search Results Screen with No Results 33](#_bookmark46)
> [Figure 12: Patient Search Results Screen with Multiple Results 33](#_bookmark47)
> [Figure 13: Patient Details Screen / Comments Section 34](#_bookmark50)
> [Figure 14: Add Comment Box 35](#_bookmark51)
> [Figure 15: Add Comment 35](#_bookmark52)
> [Figure 16: Patient Details Screen / Manage Access to Veteran Health Records 36](#_bookmark54)
> [Figure 17: Patient Details – Manage Access to Veteran Health Records 36](#_bookmark55)
> [Figure 18: Patient Details Screen / Announce 37](#_bookmark57)
> [Figure 19: Patient Details Screen / Re-Announce 37](#_bookmark58)
> [Figure 20: Announce Alert 38](#status-history-table)
> [Figure 21: Patient Details Screen / Status History Table 38](#_bookmark61)
> [Figure 22: Status History / Authorization Active 42](#_bookmark63)
> [Figure 23: Patient Details Screen / eHealth Exchange Correlations Table 43](#_bookmark65)
> [Figure 24: Patient Details Screen / Health Summary (C32) Tab – Top 44](#_bookmark69)
> [Figure 25: Patient Details Screen / Health Summary / Medical History, Part 1 44](#_bookmark70)
> [Figure 26: Patient Details Screen / Health Summary / Medical History, Part 2 45](#_bookmark71)
> [Figure 27: Patient Details Screen / Health Summary / Medical History, Part 3 46](#_bookmark72)
> [Figure 28: Patient Details Screen / Health Summary (C-CDA) Tab – Top 47](#_bookmark75)
> [Figure 29: Patient Details Screen / Health Summary / Medical History, Part 1 47](#_bookmark76)
> [Figure 30: Patient Details Screen / Health Summary / Medical History, Part 2 50](#_bookmark77)
> [Figure 31: Patient Details Screen / Health Summary / Medical History, Part 3 50](#_bookmark78)
> [Figure 32: Patient Details Screen / Health Summary / Medical History, Part 4 51](#_bookmark79)
> [Figure 33: Patient Details Screen / Health Summary / Medical History, Part 5 51](#_bookmark80)
> [Figure 34: Patient Details Screen / Health Summary / Medical History, Part 6 52](#4.3._Patient_Consent_Directive)
> [Figure 35: Patient Details Screen – Patient Has Not Authorized eHealth Exchange Record](#_bookmark84) [Sharing 53](#_bookmark84)
> [Figure 36: Patient Details Authorize eHealth Exchange Dialog Box 53](#_bookmark86)
> [Figure 37: Patient Details Authorize eHealth Exchange Dialog Box – Ready to Authorize 54](#_bookmark87)
> [Figure 38: Patient Details – Patient Has Authorized Health Record Sharing 55](#_bookmark88)
> [Figure 39: Patient Details Revoke eHealth Exchange Dialog Box – No Reason Selected 56](#_bookmark91)
> [Figure 40: Patient Details with Revoke eHealth Exchange Dialog Box – Entered in Error 57](#_bookmark92)
> [Figure 41: Patient Details Revoke eHealth Exchange Dialog Box – Revoked 58](#_bookmark93)
> [Figure 42: Patient Details Revoke eHealth Exchange Dialog Box – Patient Deceased 59](#_bookmark94)
> [Figure 43: Patient Details Revoke eHealth Exchange Dialog Box – New Authorization 59](#_bookmark95)
> [Figure 44: Patient Details Revoke eHealth Exchange Dialog Box – Ready to Revoke and Create](#_bookmark96) [New Authorization 60](#_bookmark96)
> [Figure 45: Patient Details – Patient Has Revoked Health Record Sharing with eHealth Exchange](#_bookmark97)
> [....................................................................................................................................................... 61](#_bookmark97)
> [Figure 46: Patient Details Screen – Patient has Created a New eHealth Exchange Authorization](#_bookmark98)
> [....................................................................................................................................................... 61](#_bookmark98)
> [Figure 47: Delay Authorization with Reason(s) for Delay 62](#_bookmark100)
> [Figure 48: Delayed Status Shown in Manage Access to Veteran Health Records 63](#_bookmark101)
> [Figure 49: Delayed Status Shown in Status History 64](#_bookmark102)
> [Figure 50: Notification Letter of Authorization Delay 64](#_bookmark103)
> [Figure 51: Approve Pending eHealth Exchange Authorization 65](#_bookmark105)
> [Figure 52: Cancel Pending eHealth Exchange Authorization 66](#_bookmark106)
> [Figure 53: Generate Notification Letter of Authorization Delay 66](#_bookmark107)
> [Figure 54: Status History – Click Edit Icon to Edit/Add/Delete Mailed Dates 67](#_bookmark108)
> [Figure 55: Mailed Date(s) – Edit Current Date 68](#4.3.2._Restricting_eHealth_Exchange_Reco)
> [Figure 56: Mailed Date(s) – Red Trash Icon to Delete Mailed Date(s) 68](#_bookmark110)
> [Figure 57: Mailed Date(s) – Add Another Mailed Date(s) 68](#_bookmark111)
> [Figure 58: Patient Details Screen – Patient Has Not Restricted Health Record Sharing 69](#_bookmark114)
> [Figure 59: Patient Details eHealth Exchange Restrictions Dialog Box – Top 70](#_bookmark115)
> [Figure 60: Patient Details Screen with eHealth Exchange Restrictions Dialog Box – Bottom 71](#_bookmark116)
> [Figure 61: eHealth Exchange Restrictions Dialog Box – Ready to Restrict 72](#_bookmark117)
> [Figure 62: Patient Details Screen after Successful Restrictions Authorization 72](#_bookmark118)
> [Figure 63: Patient Details Screen – Restrictions View/Modify Option 73](#_bookmark120)
> [Figure 64: Patient Details Screen with View/Modify eHealth Exchange Organization Restrictions](#_bookmark121) [Dialog Box – Top 73](#_bookmark121)
> [Figure 65: Patient Details Screen with View/Modify eHealth Exchange Organization Restrictions](#_bookmark122) [Dialog Box – Bottom 74](#_bookmark122)
> [Figure 66: View/Modify eHealth Exchange Organization Restrictions Dialog Box – Ready to](#_bookmark123) [Modify 75](#_bookmark123)
> [Figure 67: Patient Details Screen after Successful Restrictions Modification 76](#_bookmark124)
> [Figure 68: Patient Details Screen – Restrictions Revocation Option 76](#_bookmark126)
> [Figure 69: Patient Details Screen with Revoke Restrictions Dialog Box – No Reason Selected 77](#_bookmark127) [Figure 70: Patient Details Screen with Revoke Restrictions Dialog Box – Entered in Error 78](#_bookmark128)
> [Figure 71: Patient Details Screen with Revoke Restrictions Dialog Box – Revoked 79](#_bookmark129)
> [Figure 72: Patient Details Screen with Revoke Restrictions Dialog Box – Patient Deceased 79](#_bookmark130)
> [Figure 73: Patient Details Screen after Successful Restrictions Revocation 80](#_bookmark131)
> [Figure 74: Batch Announcement Patients Screen – No Selections 81](#_bookmark135)
> [Figure 75: Batch Announcement Patients Screen – Organizations Selected 82](#_bookmark137)
> [Figure 76: Batch Announce Patients Screen - Announcement Review 83](#_bookmark138)
> [Figure 77: Batch Announce Patients Results Screen - No Patients Found 84](#_bookmark139)
> [Figure 78: Batch Announce Patients Results Screen – Some Patients Not Found 84](#_bookmark140)
> [Figure 79: Batch Announce Patients Results Screen – Announce Limit Exceeded 85](#_bookmark141)
> [Figure 80: Batch Announce Patients Listed in an Excel or CSV File 86](#_bookmark143)
> [Figure 81: Batch Announce Patients from Listed in an Excel or CSV File 86](#_bookmark144)
> [Figure 82: Batch Announce Patients Results Screen – Some Patients Not Found 88](#4.4.2._Manage_Batches)
> [Figure 83: Batch Announce Patients Results Screen – Batch Announce Limit Exceeded 88](#_bookmark146)
> [Figure 84: Batch Announce Patients Results Screen – Uploaded File Issue 88](#_bookmark147)
> [Figure 85: Manage Batches Query Screen 89](#_bookmark150)
> [Figure 86: Batch Announcements Search Results Screen 90](#_bookmark151)
> [Figure 87: Batch Announce Detail Pop-Up 91](#service-audit)
> [Figure 88: Service Audit Report 92](#4.4.4._Partner_Organization)
> [Figure 89: Partner Organization Report 93](#_bookmark157)
> [Figure 90: Editing an Existing Partner Organization 93](#_bookmark159)
> [Figure 91: Monthly Received Documents Report 95](#_bookmark162)
> [Figure 92: Facilities Report 96](#edit-the-facilities)
> [Figure 93: Edit an Existing Facility 97](#_bookmark168)
> [Figure 94: Add New Facility 98](#_bookmark170)
> [Figure 95: Reporting Dashboard 100](#_bookmark174)
> [Figure 96: Disclosures Summary Report Query Screen (eHealth Exchange) 102](#_bookmark177)
> [Figure 97: Disclosures Summary Report Query Screen (Direct) 102](#_bookmark178)
> [Figure 98: Disclosure Summary Report Screen - No Results Found 103](#_bookmark179)
> [Figure 99: Disclosures Summary Report Screen (eHealth Exchange) 104](#_bookmark180)
> [Figure 100: Disclosures Summary Report Screen (Direct) 104](#_bookmark181)
> [Figure 101: Received eHealth Exchange Documents Summary Report Query Screen 105](#_bookmark185)
> [Figure 102: Received eHealth Exchange Documents Summary Report Screen 107](#_bookmark186)
> [Figure 103: Document Size Report Query Screen 108](#_bookmark189)
> [Figure 104: Document Size Report Screen 109](#_bookmark191)
> [Figure 105: Consent Directive Summary Report Query Screen 110](#_bookmark194)
> [Figure 106: Select Facilities Pop-Up Window 112](#_bookmark196)
> [Figure 107: Consent Directive Summary Report Screen (Top) 112](#_bookmark197)
> [Figure 108: Consent Directive Summary Report Screen (Bottom) 112](#_bookmark198)
> [Figure 109: Opt-In Summary Report Results (Top) 114](#_bookmark201)
> [Figure 110: Opt-In Summary Report Results (Bottom) 114](#_bookmark202)
> [Figure 111: Select Facilities Pop-Up Window 115](#_bookmark204)
> [Figure 112: Delayed Consent Summary Report 116](#_bookmark207)
> [Figure 113: Select Facilities Pop-Up Windows 118](#_bookmark209)
> [Figure 114: Delayed Consent Summary Report 119](#_bookmark210)
> [Figure 115: Patient Discovery Audit Summary Report 121](#_bookmark213)
> [Figure 116: Patient Discovery Audit Summary Report Results 122](#_bookmark215)
> [Figure 117: Accounting of Disclosures Report Query Screen (Exchange) 124](#_bookmark220)
> [Figure 118: Accounting of Disclosures Report Screen (Exchange) 126](#_bookmark221)
> [Figure 119: Accounting of Disclosures Report Screen (Direct) 126](#_bookmark222)
> [Figure 120: Document View Screen for Summarization of Episode Note 127](#_bookmark223)
> [Figure 121: Document View Screen for Discharge Summarization Note 128](#_bookmark224)
> [Figure 122: Print Dialog Box 129](#_bookmark225)
> [Figure 123: Export Warning Message and Exported Excel 130](#_bookmark227)
> [Figure 124: Received eHealth Exchange Documents Report Query Screen 131](#_bookmark230)
> [Figure 125: Received eHealth Exchange Documents Report Screen 133](#_bookmark231)
> [Figure 126: Export Warning Message 134](#4.6.3._Consent_Directive_Detailed)
> [Figure 127: User ID Parsed in Columns 134](#_bookmark234)
> [Figure 128: Exported Received eHealth Exchange Documents Report Displaying OID (Excel)](#_bookmark235)
> [..................................................................................................................................................... 134](#_bookmark235)
> [Figure 129: Consent Directive Report Query Screen 135](#_bookmark238)
> [Figure 130: Select Facilities Pop-Up Window 137](#_bookmark239)
> [Figure 131: Restriction Details (Restricted Organization) 138](#_bookmark240)
> [Figure 132: Consent Directive Detailed Report Screen 139](#_bookmark241)
> [Figure 133: Consent Directive Detailed Report Screen (Showing View) 139](#_bookmark242)
> [Figure 134: Export Warning Message 140](#4.6.4._Opt-In_Detailed)
> [Figure 135: Opt-In Detailed Report Query Screen 140](#_bookmark247)
> [Figure 136: Select Facilities Pop-Up Windows 141](#_bookmark248)
> [Figure 137: Opt-In Patients Detailed Report Screen 142](#_bookmark249)
> [Figure 138: Export Warning Message 143](#_bookmark251)
> [Figure 139: Expiring Consent Report Query Screen 143](#_bookmark254)
> [Figure 140: Select Facilities Pop-Up Window 144](#_bookmark255)
> [Figure 141: Expiring Consent Report Screen 145](#_bookmark256)
> [Figure 142: Export Warning Message 146](#_bookmark258)
> [Figure 143: Delayed Consent Detail Report 146](#_bookmark261)
> [Figure 144: Select Facilities Pop-Up Window 148](#_bookmark262)
> [Figure 145: Delayed Consent Detail Report 149](#_bookmark263)
> [Figure 146: Export Warning Message 150](#4.6.7._Patient_Discovery_Audit_Detailed4)
> [Figure 147: Patient Discovery Audit Report Query Screen 151](#_bookmark268)
> [Figure 148: Patient Discovery Audit Report Screen (Top) 152](#_bookmark269)
> [Figure 149: Patient Discovery Audit Report Screen (Bottom) without Test Patients 152](#_bookmark270)
> [Figure 150: Patient Discovery Audit Report Screen (Bottom) with Test Patients 152](#_bookmark271)
> [Figure 151: Export Warning Message 154](#_bookmark273)
> [Figure 152: Exported Patient Discovery Audit Report Displaying OID (Excel) 154](#_bookmark274)
> [Figure 153: Export Warning Message (Reports Exceeding 1000 Rows) 155](#_bookmark276)
> [Figure 154: Scheduled Exports Report 155](#_bookmark277)
> [Figure 155: Data Quality Export Search Screen 157](#_bookmark279)
> [Figure 156: Data Export Query Page 158](#_bookmark281)
> [Figure 157: File Download Dialog Box 158](#_bookmark282)
> [Figure 158: Zip File Export Options 159](#4.6.10._Data_Quality_Upload_Transmission)
> [Figure 159: Data Quality Upload Transmission Log Search Criteria 159](#_bookmark285)
> [Figure 160: Data Quality Upload Transmission Log Report 160](#_bookmark288)
> [Figure 161: Export Notice 162](#4.7._Viewing_the_User_Guide)
> [Figure 162: Scheduled Exports Screen 162](#_bookmark291)
> [Figure 163: Windows File Options 162](#_bookmark292)
> [Figure 164: Data Quality Upload Transmission Log Excel Export 162](#_bookmark293)
> [Figure 165: User Guide Option under Welcome Menu 163](#4.7.1._View_the_User_Guide_for_the_Appli)
> [Figure 166: Schedule Button on Detailed Reports (Example) 163](#_bookmark298)
> [Figure 162: Advanced Schedule: Task Creation Pop-Up Model 164](#_bookmark299)
> [Figure 168: Advanced Scheduling User Menu (Under Welcome VAP User) 166](#_bookmark301)
> [Figure 169: View Advanced Scheduled Tasks 167](#4.9._Expiring_Consent_Notification)
> [Figure 170: Edit Advanced Scheduled Tasks 167](#_bookmark303)
> [Figure 171: Expiring Consent Notification Query Screen 168](#_bookmark306)
> [Figure 172: VAP Expiring Consent Report Email 168](#_bookmark307)
> [Figure 173: Set Default Facility Screen 169](#_bookmark310)
> [Figure 174: Set Default Facility – Manually Set 169](#_bookmark311)
> [Figure 175: About VAP Option Under the Welcome Menu 170](#_bookmark314)
> [Figure 176: About VAP Screen 170](#_bookmark315)
> [Figure 177: Folder Options 183](#_bookmark325)
> [Figure 178: File Types 183](#_bookmark326)
> [Figure 179: Open With Dialog Box 184](#_bookmark327)
> [Figure 180: Batch Announce Use Case Diagram 187](#_bookmark334)
> [Figure 181: Example of a Consent Directive Summary Report Search Criteria Screen 188](#_bookmark337)
> [Figure 182: Example of a Consent Directive Summary Report Screen 188](#_bookmark338)
> [Figure 183: Tooltip (Hover Over) - Start/End Date 189](#_bookmark342)
> [Figure 184: Tooltip (Hover Over) – Patient Preferred Facility 190](#_bookmark343)
> [Figure 185: Tooltip (Hover Over) – Patient Preferred Facility Station ID 190](#_bookmark344)
> [Figure 186: Tooltip (Hover Over) – SSN 191](#7.4.2._User_Friendly_Error_Messages)
> [Figure 187: Error Message 191](#_bookmark347)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Authorizations and Preferences (VAP) project in the Virtual Lifetime Electronic Record (VLER) Initiative is responsible for authorizing Health Information Exchange (HIE) to trusted external partners and managing Veteran Electronic Consent Directives. The VAP project creates an enterprise-wide electronic solution capable of supporting Veteran Authorization Preferences/Consent Directives, and organizational policies on privacy and security relative to Release of Information (ROI), the disclosure of individually-identifiable health information to carry out treatment, payment, or healthcare operations. The VAP application is comprised of both user and machine interfaces to set patient preferences for how patient data can be shared.

> The focus of this release (Veterans Authorization and Preferences Phase 2 (VAPP2) version

> 3.2.0) is to provide technical enhancements in relation to the batch announce workflow and system configuration. Changes made to the system include limits added to restrict the size of a batch announce, removal of the retry functionality in the batch announce workflow due to performance limitations, and revision of the Manage Batches report. These changes are further detailed in Section 4.4.1 Batch Announce. Additionally, this release contains changes to the Status History table to display the entry date on a consent, if a consent has been entered manually into the system. Not included within this User Guide, are the technical configuration enhancements made to externalize the system configuration files. For details on the configuration changes, refer to the VAP Product Operations Manual (POM).

> The VAP application resides on the VA Intranet. The application can be accessed by way of the VAP User Interface (UI) using any standard Web browser (e.g., Chrome, Firefox, or Internet Explorer) on a computer that is connected to the VA network.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of the VAP User Guide (UG) is to provide detailed information to the ROI personnel and other authorized users about using the VAP application.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The UG is targeted to ROI personnel, including ROI Administrators, ROI Operators, ROI Reporters, ROI Testers, and other authorized users. These authorized users use the VAP system to create Consent Directives to enforce constraints on sharing Veteran health data with the network of partners and communities participating in the eHealth Exchange, including the SSA. VAP users are tasked with the following responsibilities.

> <span id="_bookmark3" class="anchor"></span>Table 1: Target Audience for VAP User Guide

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of User</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROI Reporters</td>
<td>Reporters run the detailed and summary reports. These users see the Consent Directive Summary Report screen when they log into the application.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of User</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROI Operators</td>
<td><p>In addition to all tasks supported by the Reporter role, the Operators search for patients and authorize, restrict, or revoke record sharing with the network of eHealth Exchange partners and communities and/or authorize or revoke record sharing with the SSA. These users see the Patient Search screen when they log into the application.</p>
<p>This is the role typically assigned to ROI personnel and other authorized users.</p></td>
</tr>
<tr class="even">
<td>ROI Administrators</td>
<td>The Administrators initiate Batch Announcements in addition to all tasks supported by the ROI Operator and ROI Reporter roles. These users see the Patient Search screen when they log into the application. These users are also able to see the Service Audit report, which shows system transactions made to VAP from VA systems (e.g., eBenefits, Exchange).</td>
</tr>
<tr class="odd">
<td>ROI Testers</td>
<td>The Testers can view the Extensible Markup Language (XML) code and perform other functions required for testing in addition to all tasks supported by the ROI Administrator, ROI Operator, and ROI Reporter roles. This role is only available to the developers and select VA personnel who do testing. These users see the Patient Search screen when they log into the application.</td>
</tr>
</tbody>
</table>

> For the purposes of the User Guide, all four categories of user roles are referred to as VAP system users.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The UG covers all VAP system functionality, including logging into the application, performing patient searches, making batch announcements, managing batches, managing facilities and partner organizations, preparing summary and detailed reports, reviewing the UG, setting the expiring consent notification and default facility, viewing the current build and logging out of the application.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools)
- User has been provided the appropriate active roles, menus, and security keys required for the VAP system
- User is using the VAP system to create Consent Directives to enforce constraints on sharing Veteran health data with the network of partners and communities participating in the eHealth Exchange, including the SSA
- User has validated access to VAP
- User has completed any prerequisite training

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All releases of new functionality, upgrades, or patches for the VAP application must be coordinated with the VLER Program Office and the associated VAP OIT Program Manager, Danna Landry. The VAP application has several connections to interfacing systems, to include Master Veteran Index (MVI), eHealth Exchange (eHX), Direct Secure Messaging, Identity Access Management (IAM) Single Sign-On Integration (SSOi), and others. In the event of planned or unexpected downtime, the VAP Business Office will contact all system users to provide updates and notifications on the status of the system. All technical coordination regarding the resolution of any issues will be coordinated between the VAP Phase 2 (VAPP2) Technical teams and the Austin Information Technology Center (AITC) hosting vendor.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

> *This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.*

#### Documentation Disclaimer

> *The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.*

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Conventions for this document include:

- Notes – Additional information is included in notes, which begin with the word “Note” in

> boldface font

- User Input – User’s responses to online prompts (e.g. taps, clicks, etc.) are shown in

> boldface font

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is available at the following VA Software Document Library (VDL) location: [<u>https://www.va.gov/vdl/application.asp?appid=222</u>](https://www.va.gov/vdl/application.asp?appid=222)

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information (email and phone number).

- Tier 0 Support – For Tier 0 Support, contact the Veterans Health Administration Local Point of Contacts (POCs). These support teams can assist users with how to use the VAP system, explanations on data and information in the reports or specifics applicable to your area, and general VAP issues. Please contact your local Communicate Care Coordinator or local Clinical App Coordinator.
- Tier 1 Support – When encountering an issue with using the VAP system or experiencing performance issues, the first step is to contact the OIT National Service Desk or local VA Help Desk. The following contact information is available:

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

- Tier 2 Support – If the VA Help Desk is not able to resolve the issue, open tickets will be escalated to Tier 2 support. These will be automatically routed to the correct party (i.e., OIT System Admin, Health Product Support, or appropriate maintenance team).
- Tier 3 Support: In the event there is an issue with the VAP application and resolution is needed from the vendor, the VAP Development and Sustainment teams will be tasked with the issue resolution. For issues needing Tier 3 support, users are advised to open a ticket with the VA Help Desk and requests and updates will be routed accordingly.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of VAP is to create a secure and compliant methodology for the exchange of Veteran health information between authorized parties. The VAP service provides Release of Information (ROI)/consent directive management and information disclosure tracking. Veterans receive care from both Department of Veterans Affairs (VA) and non-VA facilities. Sharing information between entities where the patient has been treated is needed to support appropriate clinical decision making and patient care. From entrance into military service, throughout their careers, and into retirement, Veterans, Service members (SM), and their family members are legally required to fill out authorizations/forms required by VA and other agencies that authorize or restrict the ROI. Electronic management of these forms and tracking of the information disclosed (whether submitted manually or electronically via benefits or a partner organization) is accomplished in the VAP application. Some of the enhancements will enforce VA and Veteran security policies, adhere to organizational security and privacy policies, while other enhancements within the scope of the VAPP2 development relate to addressing performance issues, reporting enhancements, and changes in policies related to consent management. This document is meant to outline the intended uses of the application at a high-level, to support the activities of the users.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For the purposes of the end user, there are no specific configurations needed to access the VAP application. The system is accessible if on the VA intranet network with a standard internet browser. Refer to Section 3.0 Getting Started for further information.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP application is hosted at the Austin Information Technology Center (AITC). The system is only accessible within the VA intranet to authorized users. VAP interfaces with numerous other VA applications such as eHealth Exchange, eBenefits, Master Patient Index (MPI)/Master Veteran Index (MVI), and SAC. <u>Figure 1</u> below breaks the VAP application down into the high- level components of the system.

![](vap-version-1-user-guide/002.png)

> Figure 1: VAP High Level Application Design

> The figure above illustrates VAP user community and interfacing systems. VAP user community consists of Veterans, ROI agents, system administrators and other authorized users. VAP interfaces with MVI, SSOi, eBenefits, VPS Kiosks, eHealth Exchange, ESR Web Services and SAC. While the system interface details are not necessarily integral to using the system, from a user standpoint, it is important to note VAP relies on data from several sources in order to provide the reports and consent information displayed within the system.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User authentication and authorization is performed with a combination of validating a user's VA credentials through the Identity Access Management (IAM) Single Sign-On Integration (SSOi)

> service and validation within VAP (as referenced in the figure below). Once a user has been authenticated, the headers are passed to VAP and are then mapped to the user roles. The following diagram, Figure 2, provides a high-level view of the system access. As a user, if you do not have permissions to the needed functionality, contact your local Communicate Care Coordinator or VAP Point of Contact to submit an elevated privileges form.

![](vap-version-1-user-guide/003.png)

> <span id="_bookmark17" class="anchor"></span>Figure 2: VAP Access Control System High-Level Design

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Standby systems are in place at AITC. In the event of system failure, systems can be migrated to other host servers via VMotion tool of the VMWare Server Farm. In the event of a database failure, a redundant database server has been allocated for this purpose. These Continuity of Operations infrastructure adjustments are seamless to the user. In the event of performance degradation or system outages, the VAP Business Owner will send communication to the field.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains the VAP application screen layout and workflow.

> Note: The UG displays test data on the screens and uses test data in the text. There is no Personal Identifiable Information (PII) included in this guide.

> ![](vap-version-1-user-guide/004.png)Additionally, it is important to note that certain features within the VAP application cannot be used with Compatibility Mode turned on in Internet Explorer (IE). Please ensure that this option is turned off prior to accessing. To turn this feature off, click on Compatibility View Settings. A pop-up should appear, as shown below, that provides the option to check/un-check display intranet sites in Compatibility View. This feature should be unchecked, as shown in Figure 3.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 3: Compatibility View Settings

> After logging into the VA network using your VHA user identification (ID) and password or PIV credentials, click on the following link to navigate to the VAP application: [<u>VAP Application</u>](https://nvpapp-prd.va.gov/nvap-web/Login.do). It is important to note that the VA has migrated systems to enforce two-factor authentication. As part of this effort to ensure VA applications are securely accessed, the authentication aspect of VAP will be completed by the Identity Access Management (IAM) Single Sign-On System (SSOi) system. Upon navigating to the VAP application, the user will be automatically routed to the SSOi user login for PIV authentication. Once the user has entered his or her PIV credentials and been validated, SSOi will re-route to the VAP application.

> In order to access this link, access to the VAP application is needed. Please work with your local site Point of Contact (POC) to submit a request for VAP access.

> ![](vap-version-1-user-guide/005.png)

> <span id="3.1.1._Log_In_to_the_Application" class="anchor"></span>Figure 4: Login Screen

### Log In to the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter your PIV card into the card reader and click Login. Enter your PIN when prompted.
2.  Once authorized, you will be routed to VAP application (Figure 5) and your user name is displayed after the Welcome message in the top right corner of the screen.
3.  The menu at the top of the screen is based on your role when you logged into the application. It allows you to select options available to your role.

> ![](vap-version-1-user-guide/006.png)The Patient Search screen is displayed automatically when you successfully log into the VAP system as a ROI Administrator or ROI Operator. ROI Reporters see the Consent Directive Summary Report screen at login.

> <span id="3.2._System_Menu" class="anchor"></span>Figure 5: Home Page for ROI Administrator or ROI Operator

> If you are not an authorized user, the \[Login\] Not Authorized screen is displayed. Click the Login button to try again, or click the Close button to exit the application. Contact your supervisor or the help desk number at the bottom of the Login screen to determine what needs to be done to get access.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vap-version-1-user-guide/007.png)The VAP application runs as a web application on the VA Intranet. The application is divided into three distinct components on the browser screen as shown in Figure 6.

> <span id="_bookmark26" class="anchor"></span>Figure 6: Using the Application

- A frame at the top displays a horizontal application menu after you have logged into the application. This menu only displays the items available to your role. The menu in the illustrations reflects the options available to ROI Administrators (i.e., the users with the highest level of production access) to allow all options to be discussed in the UG.
- The central part of the screen displays the active VAP system component.
- The bottom of the screen contains a list of standard links that provide access to Section 508 Accessibility information, the Intranet Privacy Policy, the No Fear Act, Terms of Use, links to related Intranet sites, and a Disclaimer.

> Note: VAP Administrators are able to see Admin reports and additional functionality for managing the application. VA information is also displayed allowing access to the VA Intranet through the Resources menu.

### Primary Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The menu displays the following primary options:

- Patient Search
- Summary Reports
- Detailed Reports
- Admin
- Resources
- Welcome \[UserName\]

> Note: There is no menu associated with the Patient Search.

#### Summary Reports Menu

> The Summary Reports menu item has eight (8) options that link to the query screens used to generate three (3) summary reports:

- Dashboard
- Disclosures
- Received eHealth Exchange Documents
- Document Size
- Consent Directives
- Opt-In Patients
- Delayed Consent
- Patient Discovery Audit

#### Detailed Reports Menu

> The Detailed Reports menu option contains options that link to the query screens used to generate eight (8) reports:

- Disclosures
- Received eHealth Exchange Documents
- Consent Directives
- Opt-In Patients
- Expiring Consent
- Delayed Consent
- Patient Discovery Audit
- Scheduled Exports

#### Admin Menu

> There are six (6) submenu options under the Admin menu heading:

- Batch Announce Patients
- Manage Batches
- Service Audit
- Partner Organizations
- Monthly Received Documents
- Facilities

#### Resources Menu

> There are five (5) submenu options under the Resources menu heading:

- VA Intranet Home
- About VA
- Organizations
- Find a Facility
- Employee Resources

#### Welcome Menu

> There are six (6) submenu options under the Welcome “UserName” menu heading:

- User Guide
- Advanced Scheduling
- Expiring Consent Notification
- Set Default Facility
- About
- Logout

> The Set Default Facility menu item contains options to change the facility associated with a user ID. The preferred facility for the Veteran is the facility that will appear in the VAP reports.

> Note: Each of these options is discussed in more detail in the following sections.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is important to note the VAP application no longer relies on username and passwords. As a result, all access management is handled through the Identity Access Management (IAM) Single Sign-on Integration (SSOi).

## Understanding the Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP system event flow (workflow) describes the work that is accomplished by using the application:

- Log into the application (All Users)
- Manage Consent (Administrators, Operators, and Testers)
- Patient Search
- Authorize/Revoke/Delay Record Sharing
- Restrict Record Sharing
- Generate Batch Announcements (Administrators)
- View Manage Batches (Administrators)
- Access Service Audit Report (Administrators)
- View/Edit Partner Organizations (Administrators)
- View/Edit/Add Facilities (Administrators)
- View Monthly Received Documents Report (Administrators)
- Generate and View Reports (All Users)
- Generate and View Summary Reports
- Generate and View Detailed Reports
- View User Guide (All Users)
- Edit Expiring Consent Notification
- Set Default Facility
- Review Build Information (All Users)
- Log out of the application (All Users)

> The VAP system event flow (workflow) will interface with kiosks to provide additional functionality outside the application at a future date.

> External to the system, the VAP Subsystem provides the functionality to receive a request or query from kiosks to include a Veteran’s current active status, a list of active partners, and a restriction list. VAP will prepare and return a response. This functionality will be available upon VPS Kiosk functionality deployment.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Log out of the VAP system by selecting the Logout option under the Welcome menu at the top of the screen.

### Log Out of the VAP Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click the Logout menu item under the Welcome menu at the top of any screen to log out of the VAP system application. (Figure 7 shows the Patient Search screen, but ROI Reporters will not see this screen. They see one of the summary or detailed report screens).

> ![](vap-version-1-user-guide/008.png)

> ![](vap-version-1-user-guide/009.png)<span id="_bookmark37" class="anchor"></span>Figure 7: VAP Logout

> <span id="_bookmark38" class="anchor"></span>Figure 8: Logout Confirmation

#### Logout Option Under the Welcome Menu

1.  A pop-up message appears with the following messages: “Are you sure you want to log out” and “After you logout, please close all browser windows to ensure cached information is removed.” Click Logout to proceed.
2.  The Logout screen (Figure 9) appears with no application menu and displays the message, “You have been logged out of VAP.” This confirms that you are logged out (The Welcome message also disappears from the top right corner of the screen).
3.  ![](vap-version-1-user-guide/010.png)The Log Out button appears below the message. Click the button to log out of the VA SSOi session, shown in Figure 9.

> <span id="_bookmark40" class="anchor"></span>Figure 9: Logout Screen

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within the VAP application, there are certain reports that contain data which can exceed the Microsoft Excel limit of 55,000 rows within a spreadsheet. When trying to run reports of this magnitude, it is recommended to use the export to CSV option.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP application allows the ROI Administrator and Operator roles to search for a patient and then authorize, restrict, or revoke record sharing for the patient. ROI Administrators can generate batch announcements, and view/edit facility and partner information. All users can generate and view detailed and summary reports.

> This section describes how to use the application. (The ROI Tester role has the same privileges as the ROI Administrator role in this guide. The additional functions available to Testers will be documented separately.)

> You cannot access the VAP application unless you meet the following three (3) requirements:

- You must have a Veterans Health Administration (VHA) user name and password and valid PIV card
- You must have access to the VA network
- The Austin Information Technology Center (AITC) must have associated your user name with an ROI role

> Consult your supervisor or the VA Help Desk if you need help meeting any of these conditions.

## Searching for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Search screen, Figure 10, is automatically displayed when you successfully log into the VAP system as an ROI Administrator or ROI Operator. (ROI Reporters see the Consent Directive Summary Report screen at login). You can navigate back to this screen from within the application by selecting the Patient Search option on the menu at the top of the screen.

> ![](vap-version-1-user-guide/011.png)Note: The User Guide displays test data on the screens and uses test data in the text. There is no Personally Identifiable Information (PII) included in this guide.

> <span id="_bookmark44" class="anchor"></span>Figure 10: Patient Search Screen

### Search for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All three (3) fields must be filled with valid data to search for a patient.

1.  Enter a complete Social Security Number (SSN) – nine (9) numbers with no hyphens – in the SSN field (required).
2.  Enter the last name (not case-sensitive) of the person that matches the SSN entry in the

> Last Name field (required).

3.  Enter the first name (not case-sensitive) of the person that matches the SSN entry in the

> First Name field (required).

4.  Click the Search button. This displays Patient Summary tab information on the Patient Details screen (Figure 13). Use the scroll bar at the right of the screen to view the information at the bottom of the screen.
    1.  Typically, the search results in only one match, because you must enter the patient’s SSN, last name, and first name. Searches that yield a unique entry display the patient information on the Patient Summary tab of the Patient Details screen (Figure 13) for the person found by the search.
    2.  If the search does not find any matches, the Patient Search Results screen, Figure 11, indicates no patients were found. This either means that the information you

> ![](vap-version-1-user-guide/012.png)entered was not correct or the patient you are seeking is not in the system. Reenter the data on the Patient Search screen and try again. If the data you entered was correct, the patient is not in the system.

> ![](vap-version-1-user-guide/013.png)

> <span id="_bookmark46" class="anchor"></span>Figure 11: Patient Search Results Screen with No Results

3.  If the search results in more than one match, as seen in Figure 12, it displays a list of matches and allows the user to select the correct person from the list as shown below. The search targets the Master Veteran Index (MVI). The MVI uses probabilistic, instead of exact matching based on different weights associated with demographic traits. If the MVI finds two records that are almost the same and its matching algorithm cannot determine which record is a unique match, it displays both results as shown below and lets the user decide which listing indicates the correct patient.

> <span id="_bookmark47" class="anchor"></span>Figure 12: Patient Search Results Screen with Multiple Results

> i\. Note: This screen can only appear in the Production application and is not seen by the Development teams. The screen print shown is from an older version (build) of the application and does not show the correct menu at the top of the screen (Figure 12)

4.  If the system fails to connect to MVI, it will retry the MVI call. If the connection keeps failing past the configuration defined number of attempts (five attempts), then failure via timeout from MVI is tracked and logged within the VAP system

> administrator logs. An error message noting the page is unavailable will be displayed to the user.

5.  Click the radio button next to the record that is the best match and click the View Details button. This displays Patient Summary tab information on the Patient Details screen for the selected patient.

### Patient Summary Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are six (6) parts to the Patient Summary tab on the Patient Details screen:

- Patient Information
- Comments
- Manage Access to Veteran Health Records
- Announce
- Status History
- eHealth Exchange Correlations

#### Patient Information

> The Patient Summary Information includes the Veteran’s name (first name and last name), address (street address, city, state, and ZIP code), gender (male or female), Veterans Health Information Systems and Technology Architecture (VistA) Integration Control Number (ICN), multiple birth status (YES or NO), date of birth (mm/dd/yyyy), telephone number, marital status (married, divorced, widowed, or single) and SSN, as shown in Figure 13. The data displayed within this section is not stored within the VAP system; instead, this information is pulled from the Master Veterans Index (MVI) upon selection of a patient through the Patient Search.

> ![](vap-version-1-user-guide/014.png)Within each Patient Detail view, there are two locations in which users can leave comments: the Comments and the Status History sections.

> <span id="_bookmark50" class="anchor"></span>Figure 13: Patient Details Screen / Comments Section

> In the Comments section, when a user selects Add Comment, a pop-up text input form (Figure 14) opens in the center of the screen, which can be used to write and save a comment.

> ![](vap-version-1-user-guide/015.png)

> <span id="_bookmark51" class="anchor"></span>Figure 14: Add Comment Box

> ![](vap-version-1-user-guide/016.png)In the Status History section, users can leave comments pertaining to a specific Consent Directive that a patient has completed, Figure 15. In the same process as above, users are able to select Add Comment and write remarks in a popup window. Once added, a comment cannot be deleted. In addition, the user is able to see the timestamp and username of the individual who entered the comment.

> <span id="_bookmark52" class="anchor"></span>Figure 15: Add Comment

#### Manage Access to Veteran Health Records

> The Patient Summary tab also indicates the patient’s current authorization, restrictions, and revocation settings, and allows ROI Administrators and ROI Operators to authorize, restrict, or revoke the disclosure of protected health information to eHealth Exchange providers, organizations, and the SSA. Users can change the authorization, restrictions, and revocation settings on behalf of and upon explicit request from the Veteran. See Section 4.3 Patient Consent Directive for instructions on changing authorization, restrictions, and revocation settings.

> Figure 16 illustrates the options on this tab if eHealth Exchange sharing and restrictions and SSA sharing have <u>not</u> been authorized. These options allow you to perform the following actions if you have a signed Consent Directive from a Veteran:

- The Share Veteran Electronic Health Information (eHealth Exchange) option allows ROI Administrators and Operators to authorize sharing records with non-VA provider organizations for treatment purposes using eHealth Exchange. See “To Authorize Patient Health Record Sharing with eHealth Exchange” in Section 4.3.1 eHealth Exchange Record Sharing.
- The Manage Veteran Restrictions option allows ROI Administrators and Operators to restrict sharing records with non-VA provider organizations for treatment purposes using eHealth Exchange. See “To Create Patient Health Record Sharing Restrictions with eHealth Exchange” in Section 4.3.2 Restricting eHealth Exchange Record Sharing*.*

> Note: Social Security Administration (SSA) authorizations can only be submitted electronically through system interfaces.

> ![](vap-version-1-user-guide/017.png)

> <span id="_bookmark54" class="anchor"></span>Figure 16: Patient Details Screen / Manage Access to Veteran Health Records

> The figure below illustrates the options on this tab of the screen if eHealth Exchange sharing and restrictions and SSA sharing <u>have</u> been authorized. These options allow you to perform the following actions:

- The Revoke Access to Veteran Electronic Health Information (eHealth Exchange) option allows ROI Administrators and Operators to revoke sharing records with non-VA provider organizations for treatment purposes using eHealth Exchange. See “To Revoke Patient Health Record Sharing with eHealth Exchange” in Section 4.3.1 eHealth Exchange Record Sharing.
- The View/Modify Veteran’s Existing Restrictions option allows ROI Administrators and Operators to view and/or modify restrictions on sharing records with non-VA provider organizations for treatment purposes using eHealth Exchange. See “To View and Modify Patient Health Record Sharing Restrictions with eHealth Exchange” in Section 4.3.2 Restricting eHealth Exchange Record Sharing.
- The Revoke or Terminate Veteran’s Existing Restrictions option allows ROI Administrators and Operators to revoke any or all restrictions on sharing records with non-VA provider organizations for treatment purposes using eHealth Exchange. See “To Revoke Patient Health Record Sharing Restrictions with eHealth Exchange” in Section

> ![](vap-version-1-user-guide/018.png)4.3.2 Restricting eHealth Exchange Record Sharing.

> <span id="_bookmark55" class="anchor"></span>Figure 17: Patient Details – Manage Access to Veteran Health Records

> Note: SSA consent forms can only be submitted electronically through system interfaces.

#### Announce

> Regardless of whether a patient has an eHealth Exchange Authorization, the Announce button initiates announcements to all eHealth Exchange Partners, except to the SSA, and defers to the eHealth Exchange Adapter to carry out the announcements. The Adapter sends (broadcasts) these announcements (Patient Discovery messages) containing the patient’s demographics to the targeted eHealth Exchange partners in an attempt to establish a patient correlation. The eHealth Exchange partners reply with messages indicating whether or not the patient is known to them. This information is returned to eHealth Exchange. If they know the patient, the partners send the

> correlated patient identifier, which could get registered under the VA MVI. It is important to note that if the individual has a restriction for a particular organization, an announcement can still be made.

> ![](vap-version-1-user-guide/019.png)The authorize button notifies the user that the announcement has been requested and that it will process in the background and that they can move on to other activities. If the patient has already been announced, the language of the Announce button, shown in Figure 18, changes to Re- Announce, as shown in Figure 19. If a correlation has been established and registered with MVI, this data will appear on the correlations table, refer to Section 4.2.1.5 eHealth Exchange Correlations.

> <span id="_bookmark57" class="anchor"></span>Figure 18: Patient Details Screen / Announce

> ![](vap-version-1-user-guide/020.png)

> <span id="_bookmark58" class="anchor"></span>Figure 19: Patient Details Screen / Re-Announce

> The alert function is updated to provide users the ability to announce a patient and be directed to the search screen without having to click on a confirm dialog as following steps:

1.  User will click on the Announce/Re-announce button (Figure 18\[Announce\] and Figure 19 \[Re-announce\]).
2.  User will be directed to the Patient Search screen (Figure 20). The system will provide notification that an announcement has been kicked off but it will not require input from

> the user.

#### Status History Table

> Figure 20: Announce Alert

> ![](vap-version-1-user-guide/021.png)![](vap-version-1-user-guide/022.png)The Patient Details page contains sections called Status History and eHealth Exchange Correlations. Both of these sections are able to be expanded, as well as minimized through the plus and minus options. The Consent Directive Status table at the bottom of the Patient Details screen provides a record of the authorization, restrictions, delays, and revocation actions performed by the VAP system users. The figure below displays the Status History Table screen and Table 3 describes its column headings. Consent can be managed internally within the Patient Details page or submitted by external systems such an eBenefits or the VPS Kiosk. SSA can also create an authorization entry by providing an electronic authorization document during the patient discovery process. A new feature within Release 3.2.0, is the addition of an Entry Date column. This column displays the date a consent was manually entered into the VAP system by an ROI user. The Signature date displays the date an individual signed the form (which is what was previously displayed by the system).

> <span id="_bookmark61" class="anchor"></span>Figure 21: Patient Details Screen / Status History Table

> <span id="_bookmark62" class="anchor"></span>Table 2: Consent Directive Status

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column Heading</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type of Consent Directive</td>
<td>Status History section of the Patient Details page</td>
<td><ul>
<li><p>eHealth Exchange Organization Authorization or Revocation</p></li>
<li><p>eHealth Exchange Organization Restriction Authorization or Revocation</p></li>
<li><p>SSA Authorization or Revocation</p></li>
<li><p>Kiosk Authorization or Revocation</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Purpose</td>
<td>Status History section of the Patient Details page</td>
<td>eHealth Exchange Treatment or SSA Coverage</td>
</tr>
<tr class="odd">
<td>Authorization/Revocation</td>
<td>Status History section of the Patient Details page</td>
<td><p>A message indicating an Authorization, Restriction, or Revocation for:</p>
<ul>
<li><p>eHealth Exchange providers and organizations</p></li>
<li><p>Social Security Administration</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Entry Date</td>
<td>Status History section of the Patient Details page</td>
<td>Date when the authorization, restriction, or revocation was entered into the system through the VAP system portal</td>
</tr>
<tr class="odd">
<td>Signature Date</td>
<td>Status History section of the Patient Details page</td>
<td>Date when the authorization, restriction or revocation was signed by the individual</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column Heading</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Expiration Date</td>
<td>Status History section of the Patient Details page</td>
<td>The expiration date for the authorization (i.e., patient signature date plus five years for eHealth Exchange or two years for SSA)</td>
</tr>
<tr class="even">
<td>Inactivation Date</td>
<td>Status History section of the Patient Details page</td>
<td>The inactivation date for the revocation or restriction (i.e., date when the patient revoked or restricted consent through the VAP system portal, eBenefits or Kiosk)</td>
</tr>
<tr class="odd">
<td>Status</td>
<td>Status History section of the Patient Details page</td>
<td>The Status of the Consent Directive: ACTIVE or INACTIVE. If the entry is INACTIVE (i.e., a restriction with no prior authorization or revocation), a message appears explaining the reason for the status. The following five (5) entries may appear: Authorization Expired, Entered in Error, New Authorization, Patient Deceased, and Revoked, as shown in Figure 21 and Figure 22.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column Heading</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>View Consent Form</td>
<td>Status History section of the Patient Details page</td>
<td>If the entry is an authorization added by eBenefits, the Social Security Administration, or the VPS Kiosk, a <strong>View/Print</strong> link appears in the View Consent Form column in the table. For an eBenefits authorization, clicking the link will open a standard Windows File Download dialog box that you can use to print, save, or view a Portable Document Format (PDF) copy of the consent form generated by eBenefits. For a SSA authorization or the Kiosk authorization, clicking the link will allow you to view the PDF embedded in the page and will give you the option of downloading and saving that authorization.</td>
</tr>
<tr class="even">
<td>Entered By</td>
<td>Status History section of the Patient Details page</td>
<td>Displays the username of the individual who entered the consent directive. Consent Directive entered online through external system such as eBenefits will get recorded in the Entered By column as eBenefits or the system for which the call is entered by.</td>
</tr>
<tr class="odd">
<td>Mail Date(s)</td>
<td>Status History section of the Patient Details page</td>
<td>User can Add/Edit/Delete letter Mailed Date(s) from Status History Table. The Mail date feature is applicable only for Delayed eHealth/SSA Authorizations, eHealth Revocation, or expiring eHealth authorizations.</td>
</tr>
<tr class="even">
<td>Facility Number</td>
<td>eHealth Exchange Correlations</td>
<td>The number of the associated facility is displayed.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column Heading</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>eHealth Exchange Organization Name</td>
<td>eHealth Exchange Correlations</td>
<td>The eHealth Exchange Organization Name is the name of the external partner with whom a correlation was made and a match was found for that patient in their system.</td>
</tr>
<tr class="even">
<td>eHealth Exchange Organization Assigning Authority</td>
<td>eHealth Exchange Correlations</td>
<td>The eHealth Exchange Organization Assigning Authority is the unique number associated to that partner.</td>
</tr>
<tr class="odd">
<td>Patient ID</td>
<td>eHealth Exchange Correlations</td>
<td>This field displays the patient ID for that particular individual in the partner system.</td>
</tr>
</tbody>
</table>

![](vap-version-1-user-guide/023.png)

> <span id="_bookmark63" class="anchor"></span>Figure 22: Status History / Authorization Active

> This view-only Status History table cannot be modified or deleted. The order of records is based on the date when the authorization, restriction, and/or revocation actions occurred. Sorting has been added to the columns to allow the user to order the dates. However, the action with the most recent entry date is displayed first.

#### eHealth Exchange Correlations Table

> The eHealth Exchange Correlations table at the bottom of the Patient Summary tab (on the Patient Details screen) shows with which organizations the patient has been “correlated” (i.e., patient identity is known and patient has received services), so an exchange of data can happen with those organizations. It appears immediately after the table that shows the Status History. Figure 23 displays the following information:

- Facility Number
- eHealth Exchange Organization Name
- eHealth Exchange Organization Assigning Authority
- Patient ID

> ![](vap-version-1-user-guide/024.png)Note: If a correlation needs to be removed, contact your local Master Veteran’s Index (MVI) point of contact (POC). The POC can work with the national Healthcare Identity Management (HC IdM) team to remove the correlation.

> <span id="_bookmark65" class="anchor"></span>Figure 23: Patient Details Screen / eHealth Exchange Correlations Table

> This view-only eHealth Exchange Correlations table cannot be modified or deleted.

## Patient Details Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Details screen displays the patient information on the Patient Summary tab found by the search. A second tab on this screen, Health Summary (C32), displays the health information stored in the Veteran’s C32 Health Summary.

### Health Summary (C32) Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Healthcare Information Technology Standards Panel (HITSP) C32 record summarizes a Veteran’s medical status for the purpose of information exchange. It may include administrative (e.g., registration, demographics, insurance, etc.) and clinical (problem list, medication list, allergies, test results, etc.) information. VAP system incorporates the latest C32 stylesheets from VistA Web for proper display of the received data elements for the Health Summary (C32) page.

#### View a Health Summary

1.  Click the Health Summary (C32) tab at the top of the Patient Details screen to display the Patient Health Summary screen for the patient found by the search (Figure 24 – Figure 27). Use the scroll bar at the right of the screen to view the information at the bottom of the screen.
2.  The Printer icon at the top left of the screen allows you to print the document. Click the icon to open a standard Windows Print dialog box that you can use to print or view a copy of the C32 information. Step 17 of Section 4.6.1.1 Generate an Accounting of Disclosures Report, and Figure 117 detail this process.

> ![](vap-version-1-user-guide/025.png)

> <span id="_bookmark69" class="anchor"></span>Figure 24: Patient Details Screen / Health Summary (C32) Tab – Top

> The Health Summary information includes the date the record was created (month dd, yyyy, e.g. January 7, 2017 or February 11, 1982), the patient’s name (first name and last name), the patient’s Veterans Health Information Systems and Technology Architecture (VistA) Integration Control Numbers (ICNs), contact information (street address, city, state, ZIP code, and home phone number) for the patient, date of birth (month dd, yyyy, e.g. January 7, 2017 or February 11, 1982), sex (male or female), language or languages, and the source of this information.

> ![](vap-version-1-user-guide/026.png)This screen (shown in Figure 24 to Figure 27) contains a large amount of information – more information than can be displayed in a standard window. Use the scroll bar at the right side of the screen to scroll down to reveal any information not displayed when you first select the tab.

> <span id="_bookmark70" class="anchor"></span>Figure 25: Patient Details Screen / Health Summary / Medical History, Part 1

> The following patient medical history information can appear at the bottom of the screen as shown in Figure 25 to Figure 27. (Not all categories appear for every patient.) A dynamic internal Table of Contents before this section contains links that provides direct access to each category of patient information. This information cannot be deleted or modified.

- ![](vap-version-1-user-guide/027.png)The Allergies category (Figure 25) displays the following information for each entry: Allergens, Count (##), Verification Date, Event Type, Reaction, Severity, and Source (## indicates the number of allergens listed).
- The History of Encounters category (Figure 25) displays the following information for each entry: Date / Time, Count (##), Encounter Type, Encounter Comments, and Provider (## indicates the number of encounters listed).
- The History of Procedures category (Figure 26) displays the following information for each entry: Date / Time, Count (##), Procedure Type, Procedure Comments, and Provider (## indicates the number of procedures listed).
- The Immunizations category (Figure 26) displays the following information for each entry: Immunizations, Count (##), Series, Date Issued, Reaction, and Comments (## indicates the number of immunizations listed).

> <span id="_bookmark71" class="anchor"></span>Figure 26: Patient Details Screen / Health Summary / Medical History, Part 2

- The Medications – Prescription and Non-Prescription category (Figure 26) displays the following information for each entry: Medications, Count (##), Status, Quantity, Order Expiration, Provider, Prescription \#, Dispense Date, Sig, and Source (## indicates the number of medications listed).
- The Problems/Conditions category (Figure 27) displays the following information for each entry: Problems, Count (##), Status, Problem Code, Date of Onset, Provider, and Source (## indicates the number of problems listed).
- The Results category (not pictured in this example) displays the following information for each entry: Date / Time, Count (##), Result Type, Source, Result Unit, Interpretation, Reference Range, Status, and Comment (## indicates the number of results listed).
- The Vital Signs category (Figure 27) displays the following information for each entry: Date, Count (##), TEMP (temperature), PULSE, RESP (respiration), BP (blood pressure), Ht (height), Ht (height) – Lying, Wt (weight), POx, OCF, and Source (## indicates the number of vital signs listed).
- ![](vap-version-1-user-guide/028.png)The following Emergency Contact information (Figure 27) may be displayed at the end of the Medical Record: Name, address, home telephone number, and relationship to the patient.

> <span id="_bookmark72" class="anchor"></span>Figure 27: Patient Details Screen / Health Summary / Medical History, Part 3

### Health Summary (C-CDA) Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Healthcare Information Technology Standards Panel (HITSP) C-CDA record summarizes a Veteran’s medical status for the purpose of information exchange. It may include administrative (e.g., registration, demographics, insurance, etc.) and clinical (problem list, medication list, allergies, test results, etc.) information. VAP system incorporates the latest C-CDA stylesheets for proper display of the received data elements for the Health Summary (C-CDA) page.

#### View a Health Summary

1.  Click the Health Summary (C-CDA) tab at the top of the Patient Details screen to display the Patient Health Summary screen for the patient found by the search (Figure 28

> – Figure 31). Use the scroll bar at the right of the screen to view the information at the bottom of the screen.

2.  The Printer icon at the top left of the screen allows you to print the document. Click the icon to open a standard Windows Print dialog box that you can use to print or view a copy of the C-CDA information. Step 17 of Section 4.6.1.1 Generate an Accounting of

> ![](vap-version-1-user-guide/029.png)Disclosures Report, and Figure 117 detail this process.

> <span id="_bookmark75" class="anchor"></span>Figure 28: Patient Details Screen / Health Summary (C-CDA) Tab – Top

> The Health Summary information includes the date the record was created (“month dd, yyyy”,

> e.g. January 7, 2017 or February 11, 1982), the patient’s name (first name and last name), the patient’s Veterans Health Information Systems and Technology Architecture (VistA) Integration Control Numbers (ICNs), contact information (street address, city, state, ZIP Code, and home phone number) for the patient, date of birth (“month dd, yyyy”, e.g. January 7, 2017 or February 11, 1982), sex (male or female), language or languages, and the source of this information.

> ![](vap-version-1-user-guide/030.png)This screen (shown in Figure 28 to Figure 34) contains a large amount of information, more information than can be displayed in a standard window. Use the scroll bar at the right of the screen to scroll down to reveal any information not displayed when you first select the tab.

> <span id="_bookmark76" class="anchor"></span>Figure 29: Patient Details Screen / Health Summary / Medical History, Part 1

> The following patient medical history information can appear at the bottom of the screen as shown in Figure 29 – Figure 33. Not all categories appear for every patient. A dynamic internal Table of Contents before this section contains links that provides direct access to each category of patient information. This information cannot be deleted or modified.

- The Allergies and Adverse Reactions (ADRs) category (Figure 29) displays the following information for each entry: Allergens, Event Date, Event Type, Reaction, Severity, and

> Source (## indicates the number of allergens listed). This section includes Allergies and Adverse Reactions (ADRs) on record with VA for the patient. The data comes from all VA treatment facilities. It does not list Allergies/ADRs that were removed or entered in error. Some allergies/ADRs may be reported in the Immunization section

- Encounters: Outpatient Encounters with Notes category (Figure 29) contains a list of completed VA Outpatient Encounters for the patient with associated Encounter Notes from the last 18 months. The data comes from all VA treatment facilities. Consult Notes, History & Physical Notes, and Discharge Summaries are provided separately in subsequent sections.
- The Vital Signs category (Figure 33) displays the following information for each entry: Date, Count (##), TEMP (temperature), PULSE, RESP (respiration), BP (blood pressure), Ht (height), Ht (height) – Lying, Wt (weight), POx, OCF, and Source (## indicates the number of vital signs listed).
- The Problems/Conditions category (Figure 32) displays the following information for each entry: Problems, Status, Problem Code, Date of Onset, Date of Rehabilitation, Comments, Provider, and Source (## indicates the number of problems listed).
- Insurance Providers category (Figure 30) displays the following information for each entry: Insurance Provider, Type of Coverage, Plan Name, Start of Policy Coverage, End of policy coverage, Group Number, Member Id, Insurance Providers Telephone, Policy Holder’s Name, and Patients Relationship to Policy Holder.
- Advanced Directives (Figure 30) displays the following information for each entry: Date, Advanced Directives, Provider, Source. The Advance Directives category displays a list of a patient's completed, amended, or rescinded VA Advance Directives, but an actual copy is not included.
- The Medications – Prescription and Non-Prescription category (Figure 31) displays the following information for each entry: Medication Name, Pharmacy Term, Instructions, Quantity Ordered, Prescription Expiration, Prescription Number, Last Dispense Date, and Ordering Provider. Pharmacy terms refer to VA pharmacy’s work on prescriptions. VA patients are advised to take their medications as instructed by their health care team. The data comes from all VA treatment facilities. This section includes:
  - Prescriptions processed by a VA pharmacy in the last 15 months
  - All medications recorded in the VA medical record as "non-VA medications"
- The Results category (not pictured in this example) displays the following information for each entry: Date / Time, Result Type, Source, Result Unit, Interpretation, Reference Range, Status, and Comment.
- The Immunizations (Figure 31) category displays the following information for each entry: Immunization, Series, Date Issued, Reaction, Comments. This section includes Immunizations on record with VA for the patient. The data comes from all VA treatment facilities. A reaction to an immunization may also be reported in the Allergy section. The data within this section is from the patient’s data of birth to the date the document was created.
- The Social History (Figure 33) category displays the following information for each entry: Date/Time, Smoking Status, Comment, and Facility.
- Plan of Treatment (Figure 32) category displays a listing of several types of active, pending, and scheduled orders, including clinic medication orders, diagnostic test orders, procedure orders and consult orders; where the start date of the order is 45 days before

> the current date or 45 days after the current date. Each entry contains the following: Test Date/time, Test Type, Test Details, and Facility Name.

- The Procedures category (Figure 31) displays a list of the surgical procedures performed at the VA for the patient. The associated surgical notes on record are listed. The data within this section shows the last 18 months, with all data coming from VA treatment facilities. Clinical procedure notes are provided in a subsequent section.
- Functional Status (not pictured) is a score that reflects physical and cognitive abilities of the patient at different times during their hospital stay (i.e. can the patient eat and dress on their own, etc.). A patient’s cognitive functions are scored to determine their cognitive abilities.
- HealthCare Providers (Figure 34) indicates providers who contribute data to the Health Summary
- ![](vap-version-1-user-guide/031.png)The following Emergency Contact information (Figure 34) may be displayed at the end of the Medical Record: Name, address, home telephone number, and relationship to the patient.

> ![](vap-version-1-user-guide/032.png)<span id="_bookmark77" class="anchor"></span>Figure 30: Patient Details Screen / Health Summary / Medical History, Part 2

> ![](vap-version-1-user-guide/033.png)<span id="_bookmark78" class="anchor"></span>Figure 31: Patient Details Screen / Health Summary / Medical History, Part 3

> ![](vap-version-1-user-guide/034.png)<span id="_bookmark79" class="anchor"></span>Figure 32: Patient Details Screen / Health Summary / Medical History, Part 4

> ![](vap-version-1-user-guide/035.png)<span id="_bookmark80" class="anchor"></span>Figure 33: Patient Details Screen / Health Summary / Medical History, Part 5

> <span id="4.3._Patient_Consent_Directive" class="anchor"></span>Figure 34: Patient Details Screen / Health Summary / Medical History, Part 6

## Patient Consent Directive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ROI Administrators and ROI Operators can authorize, restrict, or revoke health information record-sharing for patients who have agreed in writing to share or not share their data. By default, <u>no</u> electronic health information is shared across the eHealth Exchange until a valid, signed authorization form has been received. After a patient chooses to share health data with eHealth Exchange partners, the shared data is used only for treatment purposes. After a patient chooses to share health data with the SSA, the shared data is used only to determine the eligibility for benefits (coverage).

> If a patient has previously authorized sharing, he or she can submit a form that lets the ROI personnel and other authorized users revoke the authorization decision.

> Two items related to authorizing sharing of health information are especially noteworthy:

- If a patient has an active authorization for sharing with eHealth Exchange organizations and a new organization is added to the list of eHealth Exchange providers and organizations, the patient’s data is automatically shared with the new partner.
- In most cases, a paper form is received and validated before a patient’s authorized, restricted, and revoked status can be changed. A ROI Administrator or ROI Operator enters the requested information from the form into the appropriate fields in the VAP system application software. The form is then scanned into VistA Imaging by appropriate personnel.

### eHealth Exchange Record Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vap-version-1-user-guide/036.png)This section describes how to authorize, revoke, and delay record sharing with non-VA healthcare provider organizations using eHealth Exchange, Figure 35.

> <span id="_bookmark84" class="anchor"></span>Figure 35: Patient Details Screen – Patient Has Not Authorized eHealth Exchange Record Sharing

#### Authorize Patient Health Record Sharing with eHealth Exchange

> The Manage Access to Veteran Health Records section (immediately below the Patient Information section of the Patient Summary tab) informs the user of the patient’s eHealth Exchange access status. The default option is that the health records are <u>not</u> shared. Health record sharing that previously has been authorized can also is revoked (see below). The message in this section describes the status of health record sharing for the individual Veteran. In this case the message reads as follows: “The Veteran has currently NOT authorized the release of protected health information through the eHealth Exchange.” The patient must authorize health record sharing before the ROI personnel and other authorized users can change the status from not authorized to authorized. VA Form 10-0485 is used to obtain patient authorization for the eHealth Exchange data sharing.

1.  Click the Authorize eHealth button as shown in Figure 36. This opens the Authorize eHealth Exchange dialog box as shown in Figure 37.

> ![](vap-version-1-user-guide/037.png)

> <span id="_bookmark86" class="anchor"></span>Figure 36: Patient Details Authorize eHealth Exchange Dialog Box

2.  Read the information in the dialog box, “The Veteran authorizes the sharing of his/her electronic health information with non-VA health care provider organizations participating in the eHealth Exchange and partnering with VA for treatment purposes.”

> Do not initiate an authorize action unless you have a valid VA Form 10-0485 on file for the patient. You only announce them from the bottom of the Patient Details screen (Figure 38).

3.  Select the facility that authenticated the patient’s request for authorization from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. (A complete list of all approved Location Codes is available at: [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities.)
4.  Check the 10-0485 Form Validation checkbox to verify that an Authorization Form was received and validated (required).
5.  Enter the date (format: mm/dd/yyyy) of the patient’s signature from the Authorization Form in the Patient Signature Date field (required). The date of the signature for eHealth Exchange authorizations must be between the current date and a date no more than five (5) years prior to the current date. You can also select the date from the date range picker dropdown.

> ![](vap-version-1-user-guide/038.png)

> <span id="_bookmark87" class="anchor"></span>Figure 37: Patient Details Authorize eHealth Exchange Dialog Box – Ready to Authorize

6.  Click the Authorize button to authorize record sharing for the patient. (The Authorize transaction will not be completed until all required fields are filled out.). The VAP system

> creates the authorization and displays the Patient Details screen with the Status History and eHealth Exchange Correlations (Figure 23) sections (if they exist).

7.  The message in the Manage Access to Veteran Health Records section on the screen changes to read as follows: “The Veteran has currently authorized the release of protected health information from mm/dd/yyyy \[authorization date\] through the eHealth Exchange,” Figure 38. The authorization expires ten (10) years from the date it was signed, but it can be revoked at any time by an ROI Administrator or ROI Operator if a Veteran submits a new authorization form to request a change.
8.  The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> ![](vap-version-1-user-guide/039.png)

> <span id="_bookmark88" class="anchor"></span>Figure 38: Patient Details – Patient Has Authorized Health Record Sharing

#### Authorize Patient Health Record Sharing Using a Kiosk Device

> Note: Further details of how VA systems are able to use the VAP Application Programming Interface (API) web services are included within the VAP Interface Control Document.

> The functionality for the VPS Kiosks is not yet available until the kiosk development is completed.

#### Revoke Patient Health Record Sharing with eHealth Exchange

> The Manage Access to Veteran Health Records section (immediately below the Patient Information section of the Patient Summary tab) informs the user of the patient’s eHealth Exchange access status. The default option is that the health records are <u>not</u> shared. Health record sharing that previously has been authorized can be revoked.

> The message in this section describes the status of health record sharing for the individual Veteran. In this case the message reads as follows: The Veteran has currently authorized the release of protected health information through the eHealth Exchange. The patient must revoke health record sharing before the ROI personnel and other authorized users can change the status from Authorized to Not Authorized.

9.  Click the Revoke eHealth Exchange button as shown in Figure 39. This opens the Revoke eHealth Exchange dialog box as shown in Figure 40.
    1.  Note: The fields on this screen change after you select an Inactivation Reason as shown in Figure 40 - Figure 42.
10. Read the information in the dialog box. Do not initiate a revocation action unless you have entered an authorization in error or have a valid VA Form10-0484 (for revocation of a previously signed authorization) or proof of death on file for the patient.
11. Select the facility that authenticated the patient’s request for revocation from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. (A complete list of all approved Location Codes is available at [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities).

> ![](vap-version-1-user-guide/040.png)

> <span id="_bookmark91" class="anchor"></span>Figure 39: Patient Details Revoke eHealth Exchange Dialog Box – No Reason Selected

12. Select the reason the patient is revoking sharing from the list of reasons in the Inactivation Reason list box (required). There are four (4) available options: Entered in Error, Patient Deceased, Revoked, and New Authorization.
    1.  The Entered in Error list option activates the Revoke button without entering any additional data as shown in Figure 39. Click the Revoke button to stop sharing

> ![](vap-version-1-user-guide/041.png)data after you have verified that sharing was not authorized.

> <span id="_bookmark92" class="anchor"></span>Figure 40: Patient Details with Revoke eHealth Exchange Dialog Box – Entered in Error

2.  The Revoked list option adds the 10-0484 Form Validation check box and

> Patient Signature Date fields as shown in Figure 41.

3.  Click the 10-0484 Form Validation checkbox to acknowledge that the patient’s revocation form was received and validated.
4.  Enter the date on which the patient signed the revocation form in the Patient Signature Date field in the format mm/dd/yyyy (e.g., 12/26/2014). You can also select the date from the date range picker dropdown.
5.  The date of signature for an eHealth Exchange revocation must be between the date the eHealth Exchange authorization form was signed and the current date.
6.  The effective date for a manually-entered revocation is the date entered by ROI personnel and other authorized users as date- and time-stamped by the system instead of the actual date of the signature on the revocation form.
7.  Click the Revoke button to stop sharing data after you have certified that you have a valid revocation form and entered the date on which it was signed. The

> ![](vap-version-1-user-guide/042.png)Revoke transaction will not be completed until all required fields are filled out.

> <span id="_bookmark93" class="anchor"></span>Figure 41: Patient Details Revoke eHealth Exchange Dialog Box – Revoked

8.  The Patient Deceased list option adds the Patient Deceased Date field as shown in Figure 42.
9.  Enter the date on which the patient died in the Patient Deceased Date field in the format mm/dd/yyyy (e.g., 12/26/2014). Dates of death must not be entered unless they have been verified by an official source in accordance with VHA Directive 2006-036, Guidelines for Data Entry and Maintenance Related to Identity Management. You can also select the date from the date range picker dropdown.
10. Click the Revoke button to stop sharing data after you have entered the date on which the patient died. The Revoke transaction will not be completed until all required fields are filled out.
11. Form Validation for Revocation 10-0484 Form Received and Validated check box indicates a new form was received and validated. When checked, users

> ![](vap-version-1-user-guide/043.png)revoke the current authorization and no sharing is permitted.

> <span id="_bookmark94" class="anchor"></span>Figure 42: Patient Details Revoke eHealth Exchange Dialog Box – Patient Deceased

![](vap-version-1-user-guide/044.png)

> <span id="_bookmark95" class="anchor"></span>Figure 43: Patient Details Revoke eHealth Exchange Dialog Box – New Authorization

12. The New Authorization list option adds the New Authorization fields as shown in Figure 43.
13. Click the 10-0485 Form Validation checkbox to acknowledge that the patient’s new authorization form was received and validated.
14. ![](vap-version-1-user-guide/045.png)Enter the date on which the patient signed the new authorization form in the Patient Signature Date field in the format mm/dd/yyyy (e.g., 12/26/2014) (required). The date of the signature for the new authorization must be between the current date and a date no more than ten (10) years prior to the current date. You can also select the date from the date range picker dropdown.

> <span id="_bookmark96" class="anchor"></span>Figure 44: Patient Details Revoke eHealth Exchange Dialog Box – Ready to Revoke and Create New Authorization

15. Click the Revoke and Submit New Authorization button (Figure 44) to revoke the existing authorization and create a new authorization after you have certified that you have a valid new authorization form and entered the date on which it was signed. Submission of a new authorization even if it is outside of the 180 days window from the expiration date will automatically revoke the existing authorization and reset the expiration date to ten (10) years from the date the new authorization was signed. The Revoke and Submit New Authorization transaction will not be completed until all required fields are filled out
13. If sharing has been revoked with reasons of Revoked, Patient Deceased, New Authorization, or Entered in Error as described above, the message in the Manage Access to Veteran Health Records section on the screen changes to read as follows: “The Veteran has currently NOT authorized the release of protected health information through the eHealth Exchange,” Figure 44. The revocation remains in place until the Veteran

> reauthorizes sharing.

> ![](vap-version-1-user-guide/046.png)

> <span id="_bookmark97" class="anchor"></span>Figure 45: Patient Details – Patient Has Revoked Health Record Sharing with eHealth Exchange

14. If the current authorization is revoked and a new authorization is created, the message in the Manage Access to Veteran Health Records section on the screen changes to read as follows: “The Veteran has currently authorized the release of protected health information from {authorization date} that expires on {authorization date plus ten years}, through eHealth Exchange” as shown in Figure 45. The new authorization remains in place until it expires, it is revoked, or it is revoked and another new authorization is created.

> ![](vap-version-1-user-guide/047.png)

> <span id="_bookmark98" class="anchor"></span>Figure 46: Patient Details Screen – Patient has Created a New eHealth Exchange Authorization

#### Delay an Authorization Due to Missing or Invalid Information

> The Manage Access to Veteran Health Records section (immediately below the Patient Information and Announce sections of the Patient Summary tab) informs the user of the patient’s eHealth Exchange access status. The default option is that the health records are <u>not</u> shared.

> However, there are times when a form is received with missing or invalid information. In this

> ![](vap-version-1-user-guide/048.png)case, consent directives may be entered as delayed by the ROI user by completing the following steps:

15. Click the Authorize eHealth Exchange button as shown in Figure 47.
16. Read the information in the dialog box. Do not initiate a delayed authorize action unless you have a VA Form 10-0485 on file for the patient.
    1.  In certain cases, a VA Form 10-0485 is received with either missing or invalid information. In those cases, an individual’s authorization can be entered into a “delayed status” so that it can be tracked within the system.

> <span id="_bookmark100" class="anchor"></span>Figure 47: Delay Authorization with Reason(s) for Delay

17. Click the Delay this Authorization checkbox, shown in Figure 47, to delay authorization.
18. Multiple reasons for delay appear on screen as seen in Figure 47. These include form not signed, form content altered, demographic changes, privacy office review, signature verification, and power of attorney not on file. Check one or multiple reason(s) listed. A reason for delay must be selected in order to enter a delayed authorization into the VAP system, otherwise, the system will not allow the delay to be entered and the Delay Authorization button will not complete the transaction.
19. Additional space is provided to include any comments. It is not mandatory to enter a comment. As a note, all comments that are entered can be viewed on the Patient Details screen in the Status History in the row associated to the delay transaction. There is no

> ![](vap-version-1-user-guide/049.png)functionality in place to delete comments; all entered comments will be stored in the system.

20. Select Authorize to save changes and delay authorization.
21. Once delayed, you will be able to see the status of the authorization on the Patient Details page under Manage Access to Veterans Health Records and Status History sections as seen in Figure 47 and Figure 48. A delayed status report is in place to view both summary and detailed information on individuals in a delay.
22. Within the Manage Access to Veteran Health Records section, the reason for delay and delayed status is shown in Figure 48. This section also allows the user to approve an authorization (which removes the delayed status and creates a valid authorization), cancel a delayed authorization (which removes the delayed status but does not create a valid authorization), and print a delayed status letter. A delayed status letter is used to notify the user via print that, “…one or more items are needed to provide VA with permissions to share your health information.” A preview of this letter is seen in Figure 50. You will find further steps on how to approve/cancel/print delayed statuses on the following pages.

> ![](vap-version-1-user-guide/050.png)

> <span id="_bookmark101" class="anchor"></span>Figure 48: Delayed Status Shown in Manage Access to Veteran Health Records

![](vap-version-1-user-guide/051.png)

> <span id="_bookmark102" class="anchor"></span>Figure 49: Delayed Status Shown in Status History

> <span id="_bookmark103" class="anchor"></span>Figure 50: Notification Letter of Authorization Delay

23. Within the Status History table, a row is entered to show the delayed authorization event associated to the patient. In the first column, Type of Consent Directive, the event is populated to note, “Delayed eHealth Authorization.” The entry date column indicates the date the delayed consent is entered. Additionally, the print icon allows the user to generate a letter. The new entry icon allows for accessing the mailed dates functionality and adding/editing mailed dates.

#### Approve, Cancel, or Print a Delayed Authorization

24. To remove the consent from a delayed status, click the Approve Authorization button seen in Figure 48, which will then direct you to the approval pop-up windows shown in Figure 50.
25. Select the facility that authenticated the patient’s request from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. A complete list of all approved Location Codes is available at [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities.

> ![](vap-version-1-user-guide/052.png)

> <span id="_bookmark105" class="anchor"></span>Figure 51: Approve Pending eHealth Exchange Authorization

26. Click the 10-0485 Form Validation checkbox to acknowledge that the patient’s approval authorization form was received and validated.
27. Enter the date on which the patient signed the approval authorization form in the Patient Signature Date field in the format mm/dd/yyyy (e.g., 12/26/2014) (required). The date of the signature for the new authorization must be between the current date and a date no more than ten (10) years prior to the current date. You can also select the date from the date range picker dropdown.
28. ![](vap-version-1-user-guide/053.png)![](vap-version-1-user-guide/054.png)Click the Authorize button to approve record sharing for the patient. (The Authorize transaction will not be completed until all required fields are filled out.). This change can now be seen in Status History under Patient Details page.
29. To cancel the delayed authorization, click the Cancel Authorization button seen in Figure 48 which will then direct you to the cancelation pop-up windows shown in Figure 52.

> <span id="_bookmark106" class="anchor"></span>Figure 52: Cancel Pending eHealth Exchange Authorization

30. Enter a new comment in the box explaining the reasoning behind the cancellation decision. This field is required.
    1.  Note: The Cancel Authorization transaction will not be completed until a comment is entered.
31. To print a delay notification letter, click the Print Notification Letter button under

> Manage Access to Veteran Health Records, Figure 48.

> <span id="_bookmark107" class="anchor"></span>Figure 53: Generate Notification Letter of Authorization Delay

1.  Click the arrow at the right of Authenticating Facility list box to select the patient’s authenticating facility (Figure 53).
2.  Enter a signature in the Signature field box with your name (first and last), facility role, and contact information. Note that the Generate transaction will not be completed until all required fields are filled out.
3.  Click the checkbox to mark the letter as mailed.
4.  ![](vap-version-1-user-guide/055.png)Click the Generate button to generate the notification letter of authorization delay. An example of this letter can be seen in Figure 50.
5.  Once generated, the letter then appears in Status History Report. To edit, add, or delete the mailed date, click the link under Edit Mail Dates as show in Figure 54.

> <span id="_bookmark108" class="anchor"></span>Figure 54: Status History – Click Edit Icon to Edit/Add/Delete Mailed Dates

6.  Once the pop-up window (Figure 55) appears, you can edit the date currently selected. To delete a date, click the red trash icon shown to the right of the Date box, also shown in Figure 55. Then, to add another date, click the Add another button below the Date box, this can be seen in Figure 56. Click on the Date field for the calendar to pop-up to select the date. The system will not allow the user to enter duplicate dates.

> ![](vap-version-1-user-guide/056.png)

> <span id="4.3.2._Restricting_eHealth_Exchange_Reco" class="anchor"></span>Figure 55: Mailed Date(s) – Edit Current Date

![](vap-version-1-user-guide/057.png)

> ![](vap-version-1-user-guide/058.png)<span id="_bookmark110" class="anchor"></span>Figure 56: Mailed Date(s) – Red Trash Icon to Delete Mailed Date(s)

> <span id="_bookmark111" class="anchor"></span>Figure 57: Mailed Date(s) – Add Another Mailed Date(s)

> Note: By selecting the Show Log feature, additional details can be seen of when a mailed date was added/modified/or deleted, as well as the user whom initiated the change.

### Restricting eHealth Exchange Record Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to create, view, modify, and revoke restrictions to record sharing with eHealth Exchange.

#### Create Patient Health Record Sharing Restrictions with eHealth Exchange

> ROI personnel and other authorized users can create eHealth Exchange record sharing restrictions for only one (1) provider and/or organization as requested by a Veteran. Restrictions should not be created unless the ROI personnel and other authorized users entering the restriction has a valid signed and dated VA Form 10-0525a completed by the Veteran requesting the restriction or restrictions.

1.  ![](vap-version-1-user-guide/059.png)Click the Manage Restrictions button under the Restrictions subheading of the Manage Access to Veteran Health Records section of the Patient Summary tab on the Patient Details screen (Figure 58). This opens the eHealth Exchange Restrictions dialog box as shown in Figure 59 and Figure 60.

> <span id="_bookmark114" class="anchor"></span>Figure 58: Patient Details Screen – Patient Has Not Restricted Health Record Sharing

2.  Read the information in the dialog box. Do not initiate a restriction action unless you have a valid VA Form 10-0525a on file for the patient.
3.  Select organizations from the list of allowed organizations in the All Providers and Organizations box on the left of the screen shown in Figure 59 and Figure 60 and move them to the eHealth Exchange Providers and Organizations who will NOT have access to the records box on the right of the screen.
    1.  Click the Move All \>\> button to move all organizations from the All Providers and Organizations box to the second box. This adds <u>all</u> of these providers and organizations to the list of providers and organizations that will not have access to the patient’s health records. You must move at least one of the providers or organizations <u>back</u> to the All Providers and Organizations box before the Restrict button can activate.
    2.  You can choose to add specific providers and/or organizations to the list of providers and organizations that will not have access to the patient’s health records. Select one or more providers and organizations from the list in the All Providers and Organizations box. Click a single name to select one provider or organization or hold the Ctrl key down while clicking more than one provider or organization name to select multiple (but not all) providers and/or organizations (Figure 59). Double-clicking on the name of a provider or organization in the list also moves that name to the eHealth Exchange Providers and Organizations who

> ![](vap-version-1-user-guide/060.png)will NOT have access to the records box.

> <span id="_bookmark115" class="anchor"></span>Figure 59: Patient Details eHealth Exchange Restrictions Dialog Box – Top

3.  Click the Move Selected \> button to move the selected providers and/or organizations to the eHealth Exchange Providers and Organizations who will NOT have access to the records box. The names of the selected providers and/or organizations disappear from the All Providers and Organizations box after they have been moved.
4.  You can remove individual providers and organizations that were on the restricted list. Select one or more providers and/or organizations from the list on the right side in the eHealth Exchange Providers and Organizations who will NOT have access to the records box. Click a single name to select one provider or organization or hold the Ctrl key down while clicking more than one (but not all) provider and/or organization names to select multiple providers and/or organizations. Double-clicking on the name of a provider or organization in the list also moves that name back to the All Providers and Organizations box.
5.  Click the \< Move Selected button to move all selected providers and/or organizations to the All Providers and Organizations box. The names of the selected providers and/or organizations disappear from the eHealth Exchange Providers and Organizations who will NOT have access to the records box after they have been moved.
6.  Click the Clear button to remove all of the previously selected providers and/or organizations from the eHealth Exchange Providers and Organizations who will

> ![](vap-version-1-user-guide/061.png)NOT have access to the records box.

> <span id="_bookmark116" class="anchor"></span>Figure 60: Patient Details Screen with eHealth Exchange Restrictions Dialog Box – Bottom

4.  Select the facility that authenticated the patient’s request to restrict access from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. A complete list of all approved Location Codes is available at [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities.
5.  Check the 10-0525a Form Validation check box to verify that a restriction form was received and validated (required). Checking this check box activates the Restrict button (Figure 61) as long as there is at least one other entry in the All Providers and Organizations.
6.  Enter the date (format: mm/dd/yyyy) of the patient’s signature from the restriction form in the Patient Signature Date field (required). The date of the signature for eHealth Exchange restrictions must be less than or equal to the current date. You can also select

> the date from the date range picker dropdown.

> ![](vap-version-1-user-guide/062.png)

> <span id="_bookmark117" class="anchor"></span>Figure 61: eHealth Exchange Restrictions Dialog Box – Ready to Restrict

7.  Click the Restrict button. This displays the Patient Details screen. The Manage Access to Veteran Health Records Restrictions section shows two new links: View/Modify Veteran’s existing restrictions and Revoke or terminate Veteran’s existing restrictions. Restrictions remain in place until specifically revoked or replaced by the Veteran. If an active authorization is not on file permitting the disclosure of health information through the eHealth Exchange, the restriction remains in an inactive status until an active authorization is filed.
8.  The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> ![](vap-version-1-user-guide/063.png)

> <span id="_bookmark118" class="anchor"></span>Figure 62: Patient Details Screen after Successful Restrictions Authorization

#### View and Modify Patient Health Record Sharing Restrictions with eHealth Exchange

> ROI personnel and other authorized users can view and modify (add or remove) eHealth Exchange record sharing restrictions for single or multiple providers and/or organizations as requested by a Veteran. Restrictions should not be modified unless the ROI personnel and other authorized users entering the restriction has a valid signed and dated VA Form 10-0525a

> completed by the Veteran requesting that the restriction or restrictions be modified. There must be at least one provider in the All Providers and Organizations (left) box in order to restrict sharing.

> ![](vap-version-1-user-guide/064.png)

> <span id="_bookmark120" class="anchor"></span>Figure 63: Patient Details Screen – Restrictions View/Modify Option

9.  Click the View/Modify Restrictions button under the Restrictions subheading of the Manage Access to Veteran Health Records section of the Patient Summary tab on the Patient Details screen (Figure 63). This opens the View/Modify eHealth Exchange Organization Restrictions dialog box, shown in Figure 64 and Figure 65, which allows the ROI personnel and other authorized users to view any existing record sharing restrictions for the patient currently being reviewed.
10. Read the information in the dialog box. Do not initiate a modify action unless you have a valid VA Form 10-0525a on file for the patient. VA patient information is always shared with the DoD, so any action you can perform here does not stop sharing with the DoD.

> ![](vap-version-1-user-guide/065.png)

> <span id="_bookmark121" class="anchor"></span>Figure 64: Patient Details Screen with View/Modify eHealth Exchange Organization Restrictions Dialog Box

> – Top

11. Select organizations from the list of allowed organizations in the All Providers and Organizations box on the left of the screen and move them to the eHealth Exchange Providers and Organizations who will NOT have access to the records box on the right of the screen or vice versa.
    1.  Click the Move All \>\> button to move all organizations from the All Providers and Organizations box to the second box. This adds <u>all</u> of these providers and organizations to the list of providers and organizations that will not have access to

> ![](vap-version-1-user-guide/066.png)the patient’s health records. You must move at least one of the providers or organizations <u>back</u> to the All Providers and Organizations box before the Restrict button can activate.

2.  You can choose to add specific providers and/or organizations to the list of providers and organizations that will not have access to the patient’s health records. Select one or more providers and organizations from the list in the All Providers and Organizations box. Click a single name to select one provider or organization or hold the Ctrl key down while clicking more than one provider or organization name to select multiple (but not all) providers and/or organizations (Figure 65). Double-clicking on the name of a provider or organization in the list also moves that name to the eHealth Exchange Providers and Organizations who will NOT have access to the records box.

> <span id="_bookmark122" class="anchor"></span>Figure 65: Patient Details Screen with View/Modify eHealth Exchange Organization Restrictions Dialog Box

> – Bottom

3.  Click the Move Selected \> button to move the selected providers and/or organizations to the eHealth Exchange Providers and Organizations who will NOT have access to the records box. The names of the selected providers and/or organizations disappear from the All Providers and Organizations box after they have been moved.
4.  You can remove individual providers and organizations that were on the restricted list. Select one or more providers and/or organizations from the list on the right side in the eHealth Exchange Providers and Organizations who will NOT have access to the records box. Click a single name to select one provider or organization or hold the Ctrl key down while clicking more than one (but not all) provider and/or organization names to select multiple providers and/or organizations. Double-clicking on the name of a provider or organization in the list also moves that name back to the All Providers and Organizations box.
5.  ![](vap-version-1-user-guide/067.png)Click the \< Move Selected button to move all selected providers and/or organizations to the All Providers and Organizations box. The names of the selected providers and/or organizations disappear from the eHealth Exchange Providers and Organizations who will NOT have access to the records box after they have been moved.
6.  Click the Clear button to remove all of the previously selected providers and/or organizations from the eHealth Exchange Providers and Organizations who will NOT have access to the records box.

> <span id="_bookmark123" class="anchor"></span>Figure 66: View/Modify eHealth Exchange Organization Restrictions Dialog Box – Ready to Modify

12. Select the facility that authenticated the patient’s request to restrict access from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. A complete list of all approved Location Codes is available at [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities.
13. Check the 10-0525a Form Validation check box to verify that a restriction form was received and validated (required).
14. Enter the date (format: mm/dd/yyyy) of the patient’s signature from the restriction form in the Patient Signature Date field (required). The date of the signature for eHealth Exchange restrictions must be between the current date and a date no more than five years prior to the current date. You can also select the date from the date range picker dropdown.
15. Click the Restrict button. (The Restrict button is not activated until all required fields have been filled and there is at least one entry in each box on the screen, excluding the Comments box.) This displays the Patient Details screen. If at least one restriction remains, the Manage Access to Veteran Health Records Restrictions section shows the same two links (i.e., the options do not change): View/Modify Veteran’s existing restrictions, and Revoke or terminate Veteran’s existing restrictions (Figure 67). Restrictions remain in place until specifically revoked or replaced by the Veteran. If an active authorization is not on file permitting the disclosure of health information through

> ![](vap-version-1-user-guide/068.png)the eHealth Exchange, the restriction remains in an inactive status until an active authorization is filed.

16. You cannot remove all restrictions using this process. You must select the Revoke Restrictions button as shown in Figure 68 Patient Details Screen – Restrictions Revocation Option, and documented in the next section.
17. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> <span id="_bookmark124" class="anchor"></span>Figure 67: Patient Details Screen after Successful Restrictions Modification

#### Revoke Patient Health Record Sharing Restrictions with eHealth Exchange

> ROI personnel and other authorized users can revoke (terminate) eHealth Exchange record sharing restrictions for all providers and/or organizations as requested by a Veteran. Restrictions should not be revoked unless the ROI personnel and other authorized users entering the revocation has a valid signed and dated VA Form10-0525 completed by the Veteran requesting that the restriction or restrictions be revoked.

![](vap-version-1-user-guide/069.png)

> <span id="_bookmark126" class="anchor"></span>Figure 68: Patient Details Screen – Restrictions Revocation Option

18. Click the Revoke Restrictions button under the Restrictions subheading of the Manage Access to Veteran Health Records section of the Patient Summary tab on the Patient Details screen. This opens the Revoke or Terminate eHealth Exchange Organization Restriction dialog box shown below.
19. Read the information in the dialog box. Do not initiate a revocation action unless you have entered a restriction in error or have a valid VA Form 10-0525 or proof of death on file for the patient. VA patient information is always shared with the DoD, so any action you can perform here does not stop sharing with the DoD.
20. Select the facility that authenticated the patient’s request for revocation from the list in the Authenticating Facility list box (required). The default authenticating facility is selected based on the Location Code (characters four through six) used in the ROI user’s VA User ID. A complete list of all approved Location Codes is available at [Approved Location Codes](http://vaww4.va.gov/NamingConventions/ApprovedLOCATIONCodes.asp). Not all codes correspond to VistA facilities.

> ![](vap-version-1-user-guide/070.png)

> <span id="_bookmark127" class="anchor"></span>Figure 69: Patient Details Screen with Revoke Restrictions Dialog Box – No Reason Selected

21. Select the reason the patient is revoking restrictions from the list of reasons in the Inactivation Reason list box (required). There are three available options: Entered in Error, Patient Deceased, and Revoked.
22. The Entered in Error list option activates the Revoke button without entering any additional data as shown in Figure 70. Click the Revoke button to revoke the sharing

> restrictions.

> ![](vap-version-1-user-guide/071.png)

> <span id="_bookmark128" class="anchor"></span>Figure 70: Patient Details Screen with Revoke Restrictions Dialog Box – Entered in Error

23. The Revoked list option adds the 10-0525 Form Validation check box and Patient Signature Date fields as shown in Figure 71.
    1.  Click the 10-0525 Form Validation checkbox to acknowledge that the patient’s restrictions revocation form was received and validated.
    2.  Enter the date on which the patient signed the revocation form in the Patient Signature Date field in the format mm/dd/yyyy. You can also select the date from the date range picker dropdown.
        1.  The date of signature for an eHealth Exchange restrictions revocation must be between the date the eHealth Exchange restrictions authorization form was signed and the current date.
        2.  The effective date for a manually-entered restriction revocation is the date entered by ROI personnel and other authorized users as date- and time- stamped by the system instead of the actual date of the signature on the restrictions revocation form.
    3.  The Revoke button is not activated until all required fields have been filled. Click the Revoke button to revoke the sharing restrictions after you have certified that you have a valid restrictions revocation form and entered the date on which it was signed.

> ![](vap-version-1-user-guide/072.png)![](vap-version-1-user-guide/073.png)

> <span id="_bookmark129" class="anchor"></span>Figure 71: Patient Details Screen with Revoke Restrictions Dialog Box – Revoked

24. The Patient Deceased list option adds the Patient Deceased Date field as shown in Figure 72.
    1.  Enter the date on which the patient died in the Patient Deceased Date field in the format mm/dd/yyyy. Dates of death must not be entered unless they have been verified by an official source in accordance with VHA Directive 2006-036, Guidelines for Data Entry and Maintenance Related to Identity Management. You can also select the date from the date range picker dropdown.
    2.  Click the Revoke button to revoke the sharing restrictions after you have entered the date on which the patient died. The Revoke transaction will not be completed until all required fields are filled out.

> <span id="_bookmark130" class="anchor"></span>Figure 72: Patient Details Screen with Revoke Restrictions Dialog Box – Patient Deceased

25. Successfully revoking sharing restrictions displays the Patient Details screen. All restrictions are removed by this process and the View/Modify Restrictions and Revoke Restrictions buttons in the Restrictions section are replaced with the Manage Restrictions (Figure 73). If the Veteran has an active eHealth Exchange authorization on

> file, sharing with all eHealth Exchange organizations (i.e., unrestricted sharing) will resume.

26. ![](vap-version-1-user-guide/074.png)The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> <span id="_bookmark131" class="anchor"></span>Figure 73: Patient Details Screen after Successful Restrictions Revocation

#### Create or Revoke Patient Health Record Sharing Restrictions with Trusted VA Systems

> VAP Subsystem enhancements will allow Veterans to manage their health consent directives electronically through VA systems leveraging the VAP API web services. For this functionality enables systems to submit a web service request for consent management information and creates a “plug-in” between the two systems. As VA systems leverage the web service, this User Guide will be updated to note other entry points for consent management.

## Admin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From a system owner and user perspective, system functions were desired to allow for tracking and managing trusted partners. Additionally, functionality was desired to allow other systems to verify if a partner is trusted prior to accepting or transferring data to be processed by internal VA systems. Within the Admin area of the VAP application, pages were created that display the list of partners, detail if the partner is active, whether or not these partners are trusted clinical sources, and any associated details related to the Organization, such as contact information. VAP Admins have the capability to edit certain details related to a partner, such as name and phone number, and to check whether or not they are trusted. Additionally, capability is provided allowing the Admin to export the list of partners to Excel.

> Administrators have the ability to manage facilities. This includes the ability to add, edit, or inactivate facilities that are used on reports leveraging the VAP database (Opt-In, Consent Directive, Expiring Consents, and Delayed Status) and their associated parent-child relationships.

### Batch Announce Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Announcements are made to share patient identifiers, such as ICNs, with partner systems to facilitate data sharing. Announcements occur automatically when you authorize sharing of patient records. ROI personnel and other authorized users can make ad hoc announcements by clicking the Announce button (Figure 18).

> Batch Announcements offer an alternate mechanism to accomplish the above. These allow ROI Administrators to selectively announce to one or many eHealth Exchange organizations.

> ![](vap-version-1-user-guide/075.png)The fields in the Batch Announce Criteria box on the Batch Announcements Patients screen (Figure 74 and Figure 75) allow you to make announcements to one or more eHealth Exchange organizations for patients who have authorized sharing within a specified date range. Batch Announce functionality allows ROI personnel and other authorized users to announce all the patients who have authorized sharing to a new eHealth Exchange organization when the partner gets access to the application or who have contained in an uploaded Excel or csv file.

> <span id="_bookmark135" class="anchor"></span>Figure 74: Batch Announcement Patients Screen – No Selections

> Release 3.2.0 provides enhancements and modification to the Batch Announce functionality to include changes to the number of retries the system will make to send a batch announce request, addition of limits to the number of threads that can be included in a batch announce, and implementation of a flag to indicate an eHealth Exchange partner who does not wish to receive announcements. In addition, enhancements within this release include increased error handling to notify the user if the limits are exceeded or if an individual cannot be announced.

#### Batch Announce Patients that have Opted-In

1.  Click the Batch Announce Patients menu item under the Admin menu at the top of the screen to display the Batch Announce Patients screen.
2.  Select organizations from the list of allowed organizations to which you want to announce patients in the All Organizations box on the left of the screen and move them to the “Organizations to which you want to announce patients” box on the right side of the screen.
    1.  Click the Move All \>\> button to move all organizations from the All Organizations box to the second box. This adds all of these providers and organizations to the list of providers and organizations that will receive announcements.
        1.  Note: Due to recently identified performance issues (August 2018), it is not recommended for users to use the batch announce function to announce individuals to all eHealth Exchange partners. At the time of release of this document, the total number of partners is around 170. If 10

> ![](vap-version-1-user-guide/076.png)individuals are announced to all partners, that would be 1,700 simultaneous requests. Downstream dependent systems will receive a multiple of those requests and reply accordingly.

2.  You can choose to add individual organizations to which you want to announce patients who have authorized record sharing. Select one or more organizations from the list in the All Organizations box. Click a single name to select one organization or hold the Ctrl key down while clicking more than one organization name to select multiple organizations (Figure 75). Double-clicking on the name of an organization in the list also moves that name to the Organizations to which you want to announce patient’s box.
3.  Click the Move Selected \> button to move selected organizations to the Organizations to which you want to announce patients box. The names of the selected organizations disappear from the All Organizations box after they have been moved.
4.  You can remove individual organizations that were on the list to which you want to announce the patient. Select one or more organizations from the list on the right side under Organizations to whom you want to announce patient’s box. Click a single name to select one organization or hold the Ctrl key down while clicking more than one organization name to select multiple organizations. Double- clicking on the name of an organization in the list also moves that name back to the All Organizations box.
5.  Click the \< Move Selected button to move all selected organizations to the All Organizations box. The names of the selected organizations disappear from the Organizations to whom you want to announce patients box after they have been moved.

> <span id="_bookmark137" class="anchor"></span>Figure 75: Batch Announcement Patients Screen – Organizations Selected

6.  Click the Clear button to remove all of the previously selected organizations from the Organizations to whom you want to announce patient’s box. If you exercise this option, you must repopulate the Organizations to which you want to announce patient’s box before you can announce patients.
7.  On certain occasions, an eHealth Exchange partner may not appear on the list of available organizations to batch announce. There are two reasons this may occur:

> a\) the partner is no longer an active or b) the partner system has requested to opt- out of receiving batch announces. For example, there are certain partners who are not equipped to handle batch announcements who have reached out to the VA Program and asked to not be included. A VAP Administrator is able to check/uncheck whether batch announcements are allowed on the Partner Organization page of the VAP application.

3.  Select the Batch announce patients that have opted-in radio button.
4.  Enter the start date for the announcement in the Start Date field in the format mm/dd/yyyy (e.g., 01/05/2015). This date reflects the earliest date from which records will be shared. It is not recommended to leave date fields blank, which would announce all patients who have authorized record sharing. Instead, users are recommended to use the date filters to narrow the search.
5.  Enter the end date for the announcement in the End Date field in the format mm/dd/yyyy (e.g., 01/06/2015). This date reflects the latest date from which records will be shared. You can also select the date from the date range picker dropdown.
6.  Click the Re-announce check box if you want to re-announce patients who have authorized record sharing and have previously been announced.
7.  ![](vap-version-1-user-guide/077.png)Click the Query button. This displays the Batch Announce Patients Results screen (Figure 76). The result shows the number of patients who have been announced to each individual organization.

> <span id="_bookmark138" class="anchor"></span>Figure 76: Batch Announce Patients Screen - Announcement Review

8.  Click the Continue button as shown in Figure 76 to begin the announcements and display the Manage Batches Query screen. Clicking this button initiates the Manage Batches process as described in the next section. Click the Cancel button to stop the announcement process.
9.  If the search yields no results, as shown in Figure 77, no announcements have been made recently. You must return to the Batch Announcements screen, select one or more Organizations, and select a date or range of dates if appropriate. Click the Re-announce check box before you click the Query button. The Batch Announce Patients Query Results screen will display the results for the Organizations that you re-announced.

![](vap-version-1-user-guide/078.png)

> <span id="_bookmark139" class="anchor"></span>Figure 77: Batch Announce Patients Results Screen - No Patients Found

10. If the search results indicate that an individual was not found in MVI, the user is alerted through a yellow warning message. Within the message, there is a (+/-) symbol, that allows the user to expand the pane and view the list of individuals who cannot be announced. At this point, it is recommended to validate the individuals and return to the prior page to modify the query.

> ![](vap-version-1-user-guide/079.png)

> <span id="_bookmark140" class="anchor"></span>Figure 78: Batch Announce Patients Results Screen – Some Patients Not Found

11. If the search results exceeded the system limit, then a red message will alerting the user that the individuals and partners to be included in the batch announce exceed the system limitation. Recently, as a result of performance issues, the announce limit has been modified to restrict Administrators from batch announcing during certain times. This change is a modification within Release 3.2.0. As a way of implementing this feature, the configuration limit can be modified by VAP System Administrators without a new build, to adjust if there are any performance degradations. When an announce limit is encountered, either reduce the number of individuals or the number of partners.

> ![](vap-version-1-user-guide/080.png)

> <span id="_bookmark141" class="anchor"></span>Figure 79: Batch Announce Patients Results Screen – Announce Limit Exceeded

#### Batch Announce Patients Listed in an Excel or CSV File

12. Click the Batch Announce Patients menu item under the Admin menu at the top of the screen to display the Batch Announce Patients screen.
13. Follow Step 2 of the Batch Announce Patient That Have Opted-In section above to select organizations from the list of allowed organizations to which you want to announce patients in the All Organizations box on the left of the screen and move them to the “Organizations to which you want to announce patients” box on the right of the screen. As mentioned in the prior section, if an organization does not appear on the list, the organization may have elected to not receive batch announcements. This preference is set in the Manage Partner Organizations section of the VAP application by Administrators.
14. Select Batch announce patients listed in an Excel or CSV file radio button.
15. Click the Browse button to select the desired file from your local computer (Figure 80).
    1.  ![](vap-version-1-user-guide/081.png)Note: The fields in the Excel or csv file contain the patients’ first names, last names, and SSN in a sequence of nine digits with no hyphens.

> <span id="_bookmark143" class="anchor"></span>Figure 80: Batch Announce Patients Listed in an Excel or CSV File

16. If you want to remove the previously selected file, select the Clear button. Otherwise, click the Query button to upload the file.
17. ![](vap-version-1-user-guide/082.png)Click the Continue button to begin the announcements or click the Cancel button to stop the announcement process, Figure 80.

> <span id="_bookmark144" class="anchor"></span>Figure 81: Batch Announce Patients from Listed in an Excel or CSV File

18. As noted in the section above, if the announce limit is exceeded the Batch Announce Patients – Query results page displays an error. If the individuals included within the spreadsheet cannot be found in the MVI system, then a warning box will appear alerting the user to validate the information before continuing or continue with the batch announce without these individuals in question. If the connection to MVI is down or none

> of the patients are found, then the user will not be able to continue and the error will say, “Uploaded file doesn’t contain any known patients.”

> ![](vap-version-1-user-guide/083.png)

> <span id="4.4.2._Manage_Batches" class="anchor"></span>Figure 82: Batch Announce Patients Results Screen – Some Patients Not Found

![](vap-version-1-user-guide/084.png)

> ![](vap-version-1-user-guide/085.png)<span id="_bookmark146" class="anchor"></span>Figure 83: Batch Announce Patients Results Screen – Batch Announce Limit Exceeded

> <span id="_bookmark147" class="anchor"></span>Figure 84: Batch Announce Patients Results Screen – Uploaded File Issue

### Manage Batches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ROI Administrators can manage batches after selecting the organizations to receive batch announcements. Announcements scheduled to be made to any or all organizations can be deleted from the queue.

#### ![](vap-version-1-user-guide/086.png)Manage Batches

1.  Click the Manage Batches menu item under the Admin menu at the top of the screen to display the Manage Batches Query screen (Figure 85). Clicking the Continue button on the Batch Announce Patients screen to begin the announcement process also displays the Manage Batch Announcements screen.
2.  Enter the start date for the announcement search in the Start Date field in the format mm/dd/yyyy. This date reflects the earliest date of the announcements in the search. Leave this field and the End Date field blank to find all announcements regardless of their dates. You can also select the date from the date range picker dropdown.
3.  Enter the end date for the announcement in the End Date field in the format mm/dd/yyyy. This date reflects the last date of the announcements in the search. Due to performance issues, it is not recommended to run this report for more than two weeks. Leaving the dates empty on both the Start and End Date will search for all batch announce records available on the system and use a significant amount of system resources.

> <span id="_bookmark150" class="anchor"></span>Figure 85: Manage Batches Query Screen

4.  Click the arrow at the right of the eHealth Exchange Organization list box to select the organization you want to display in the report. You can only select one entry from the list. The default option for this list box is All, so do not select a specific organization if you want to see all eHealth Exchange organizations in the report.
5.  Click the Search button to display the Batch Announcements Search Results screen (Figure 86).
6.  Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. This field allows users to select by 10, 25, 50, 100, 250 and 500.
7.  Each row displays the Organization Name, Date Created (CT) which is the date the batch announce was sent, Scheduled, Requested, Batch Size and Action. The Scheduled column indicates that VAP is in the process of initiating the batch announce request to eHealth Exchange. The Requested column indicates the batch announce request has been completed and the workflow to contact the eHealth Exchange partner has been triggered

> ![](vap-version-1-user-guide/087.png)and initiated. Within Release 3.1.1, a change was made to stop the system from retrying to initiate an announce with eHealth Exchange. This was identified as causing a performance impact. If an announce appears to remain in the Scheduled column for more than a day, this indicates the announcement was not successfully initiated. The user should retry sending this batch announcement. Within an upcoming release (Release 3.3.0, October 2018) changes will be made to identify if a batch announce request has failed due to a timeout or another reason, and to indicate which individuals must be re- announced.

8.  If more records are available than can be displayed on one screen, the Previous and Next buttons at the bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
9.  To select one or more organizations to be deleted from the list of organizations to which the batch announcement is directed, click the check box before the organization name or names (e.g., Kaiser Permanente) to mark them for deletion.

> <span id="_bookmark151" class="anchor"></span>Figure 86: Batch Announcements Search Results Screen

10. When you have marked the organizations to be deleted, click the Delete button to remove the selected organizations from the list of organizations that receive the announcements.
11. Click the View Details button to view a complete list of individuals included in a batch announcement, seen in Figure 87.

> ![](vap-version-1-user-guide/088.png)

### Service Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 87: Batch Announce Detail Pop-Up

> The system provides Service Audit Reports which contain a log of all electronic information requests made to the VAP system from VA systems. Each record in these logs includes a source identifier (or which VA system made the web service request to VAP for consent management information). Specifically, a source identifier is descriptive information about the origin of the information request, tracked so that VAP administrators know who is making data requests.

> These audit reports are only available to users with administrator access. The service audit reports can be filtered to identify which web services were called (i.e. Get Restrictions), the duration of the call, if the call was successful, and the domain of the call sender. See Figure 88.

> ![](vap-version-1-user-guide/089.png)The default display order of the Service Audit report is by the descending order of the Event Date field. The report could be sorted by all the columns. The default number of records displayed in the report is 25.

> <span id="4.4.4._Partner_Organization" class="anchor"></span>Figure 88: Service Audit Report

### Partner Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP application generates a partner management report to provide the ability to track and manage trusted partners, and allow other systems to verify if a partner is trusted. The main Partner Organization page provides a tabular view of all the VAP partners, organization information available, and indicates whether or not these are active partners and if these are trusted clinical sources.

#### Generate the Partner Organization Report

> To navigate to the Partner Organization view, click on the Partner Organization menu item under the Admin reports heading.

> Once selected, the Partner Organization page will appear. Figure 89 displays the tabular main Partner Organization view. This has various features that allow the VAP Admins to view the VAP partners and export the information displayed onto an Excel spreadsheet. Each row on this view is associated to a different and unique partner. The Active column denotes if this partner is still an active partner or if no longer active (indicated by Yes/No). Columns 2-8 display any information available regarding the partner such as Name, Phone, whether the Partner is a consumer (or not), and Organization ID. If this partner is a trusted clinical source, a “yes” label will be displayed. The Action column allows the user to navigate to the Edit page to modify selected attributes of this partner.

> Within Release 3.2.0, the Partner Organization functionality was modified to allow administrative users to mark if a partner does not wish to receive batch announces. Through technical analysis, it has been identified that several partners do not have the technical capacity to receive batch announces or do not wish to receive batch announces. In order to ensure that these preferences are captured, a new column has been added labeled “Batch Announce Enabled.” Yes indicates the partner does allow batch announces. If No, then the partner does not wish to receive batch announces and that partner will not be displayed as an option when sending batch announces.

> Note: For the purposes of this section, screenshots of the VAP Production system are not yet deployed. Therefore, all partners displayed within the image correspond to test partners within a VAP testing environment.

> ![](vap-version-1-user-guide/090.png)![](vap-version-1-user-guide/091.png)

> <span id="_bookmark157" class="anchor"></span>Figure 89: Partner Organization Report

#### Edit the Organization

> The Partner Organizations - Edit view, as displayed in Figure 90, allows the Admin User to modify selected fields. These fields include Organization Name, Organization Description, Organization Number, Contact Name, Contact Phone, whether the Partner is a trusted source, and whether Batch Announce is enabled. The Organization Name, Description, Number, Phone, and Contact Name are text fields that allow for special characters and hyphens if needed within the Partner Name.

1.  Click on the Edit button on the Partner Organization report, seen in Figure 89 to navigate to the Partner Organizations – Edit view see in Figure 90.

> <span id="_bookmark159" class="anchor"></span>Figure 90: Editing an Existing Partner Organization

2.  Enter the name of the organization in the Organization Name field box. This is a required entry. Failing to fill in this item box will result in an error message that will not allow you to save changes.
3.  Enter the organization description in the Organization Description field box. This entry is also required to proceed.
4.  Enter the organization number in the Organization Number field box. This entry is also required to proceed.
5.  Enter the contact name in the Contact Name field box.
6.  Enter the contact phone number in the Contact Phone field. There is no restriction on the format of the numbers.
7.  Check the Is trusted clinical source checkbox if the organization is trusted. Uncheck if otherwise.
8.  Check the Is Batch Announce enabled checkbox if the partner wishes to permit batch announces to be sent to them. Uncheck if the partner has elected not to receive batch announces. Please note that individual announcements will still be permitted.
9.  Click the Save button to save changes made.
10. The Cancel button cancels the process of editing Partner Organization. Changes will not take place.

#### Export the Partner Organizations Report

11. Select the Export to Excel option on the top right side of the report section seen in Figure 89.
12. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: No privacy warning is displayed prior to completing the export; however, users are reminded to follow standard VA policies and procedures for information handling.

### Monthly Received Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Monthly Received Documents report page is an administrative function of VAP. This report is used by VA VLER stakeholders to maintain an audit and count record of users who have received documents, on a per partner basis. This report is set to generate by calendar month and displays the partner organization, the VA user who received a document, and the total count.

1.  Select the Monthly Received Documents menu item under Summary Reports heading on the menu at the top of the screen, to display the Monthly Received Documents query screen.
2.  Click the arrow on the Start Month/Year list dropdown to select the data to be included within the generated report.
3.  ![](vap-version-1-user-guide/092.png)Click the Search button to display the Monthly Received Documents Report as shown in Figure 91.

> <span id="_bookmark162" class="anchor"></span>Figure 91: Monthly Received Documents Report

4.  The Show Entries dropdown provides the user the option to select the number of records to be displayed on each page of the search. The default option for this list box is 25.
5.  If more records are available than the page display record setting, the Previous and Next buttons at the top and bottom right of the screens are activated. The user can use these buttons to navigate back and forward through the list of records found by the search.
6.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Select the down arrow icon to sort the column by descending order.

#### Export the Monthly Received Documents Report

1.  Select the Export to Excel option on the top-right side of the report section seen in Figure 91.
2.  Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: No privacy warning is displayed prior to completing the export; however, users are reminded to follow standard VA policies and procedures for information handling.

### Facilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within VAP, there is an administrative function to manage the facilities used for reporting on the VAP-generated reports (Consent Directive, Opt-In, Expiring Consents, and Delayed Status). The VAP administrator will have the capability to manage facilities information (add, edit, inactivate, and change parent/child relationships). The main Facilities page provides a tabular view of all the facilities, parents, children, facility information available, and indicates whether or not these are shown in the drop down when manually entering an authorization.

#### Generate the Facilities Report

> To navigate to the Facilities view, click on the Facilities menu item under the Admin reports heading.

> ![](vap-version-1-user-guide/093.png)Once selected, the Facilities page will appear. Figure 92 displays the tabular main view. This has various features that allow the VAP Admins to view the facilities and export the information displayed onto an Excel spreadsheet. Each row on this view is associated to a different and unique facility. Columns 1-10 display any information available regarding the facility such as name, phone, address, station number, parent, child, and VISN. The Allowed column denotes if this facility can be seen in the drop down for when manually entering an authorization (indicated by Yes/No).

#### Edit the Facilities

> Figure 92: Facilities Report

> The Edit Facility view, as displayed in Figure 93, allows the Administrator to modify selected fields. These fields include Station Number, Facility Name, Address, City, State, Zip Code, Phone Number, VISN, Parent, and Allowed checkmark. All fields, except for VISN and Parent, are text fields that allow for special characters and hyphens if needed.

1.  To navigate to the Edit Facility page (Figure 93), click on the Edit button on the Facilities report, seen in Figure 92.

> ![](vap-version-1-user-guide/094.png)

> <span id="_bookmark168" class="anchor"></span>Figure 93: Edit an Existing Facility

2.  Enter the station number in the Station Number field box. This is a required entry. Failing to fill out this item box will result in an error message that will not allow you to save changes.
3.  Enter the name of the facility in the Facility Name field box. This is a required entry. Failing to fill out this item box will result in an error message that will not allow you to save changes.
4.  Enter the facility address in the Address field box. This entry is also required to proceed.
5.  Enter the city in the City field box. This entry is also required to proceed.
6.  Enter the state in the State field box. This entry is also required to proceed.
7.  Enter the zip code in the Zip Code field. There is no restriction on the format of the numbers.
8.  Enter the facility phone number in the Phone Number field. There is no restriction on the format of the numbers.
9.  Click on the down arrow to the right of VISN to view all VISNs, and make a selection.
10. Click on the down arrow to the right of Parent to view all parents, and make a selection. It is important to note that selecting a facility as a parent allows the user to use the Aggregate feature in summary reports. The reports will roll up and aggregate all counts of the children facilities up to the parent level based on these relationships.
11. Check the Allowed checkbox if the facility should be displayed on the dropdown within the Authorizations modal for when manually entering when entering an authorization.
12. To inactivate a facility, select the Inactivate button. This button will remove the facility from the facilities drop-down. It is important to note that in order to inactivate a parent facility with children facilities underneath, the children must be disassociated from the parent.
13. Click the Save button to save changes made.
14. The Cancel button cancels the process of editing the Facility, and changes will not take place.

#### Add a New Facility

> The Add Facility view, as displayed in Figure 94, allows the Admin User to add a new facility. The fields to be filled out include Station Number, Facility Name, Address, City, State, Zip Code, Phone Number, VISN, Parent, and Allowed checkmark. All fields, except for VISN and Parent, are text fields that allow for special characters and hyphens if needed.

15. Click on the Add Facility option on the top right side of the screen, Figure 92, next to

#### Export to Excel.

> ![](vap-version-1-user-guide/095.png)

> <span id="_bookmark170" class="anchor"></span>Figure 94: Add New Facility

16. Enter the station number in the Station Number field box. This is a required entry. Failing to fill out this item box will result in an error message that will not allow you to save changes.
17. Enter the name of the facility in the Facility Name field box. This is a required entry. Failing to fill out this item box will result in an error message that will not allow you to save changes.
18. Enter the facility address in the Address field box. This entry is also required to proceed.
19. Enter the city in the City field box. This entry is also required to proceed.
20. Enter the state in the State field box. This entry is also required to proceed.
21. Enter the zip code in the Zip Code field. There is no restriction on the format of the numbers.
22. Enter the facility phone number in the Phone Number field. There is no restriction on the format of the numbers.
23. Click on the down arrow to the right of VISN to view all VISNs, and make a selection.
24. Click on the down arrow to the right of Parent to view all parents, and make a selection.
25. Check the Allowed checkbox if the facility is allowed to be manually entered when entering an authorization.
26. Click the Save button to save changes made.
27. The Cancel button cancels the process of editing Facility. Changes will not take place.

#### Export the Facilities Report

28. Select the Export to Excel option on the top right side of the report section seen in Figure 92.
29. Report data is exported into an Excel spreadsheet. For Excel format, report name, current date, and all filtering criteria are exported as a file header.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: No privacy warning is displayed prior to completing the export; however, users are reminded to follow standard VA policies and procedures for information handling.

## Generating Summary Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP application generates eight (8) summary reports.

- Dashboard
- Disclosures
- Received eHealth Exchange Documents
- Document Size
- Consent Directive
- Opt-In Patients
- Delayed Consent
- Patient Discovery Audit

> Each report is described below in more detail. These report options are available to all users.

### Dashboard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To navigate to the Dashboard view, click on the Dashboard menu item under the Summary Reports heading. A set of widgets, seen in Figure 95, will be displayed just under the Patient Search field. The widgets provide a more advantageous method for tracking performance and statistics of the application with real-time metrics and counts.

> The four (4) widgets displayed are:

- Expiring Authorizations (within 30 Days)
- New Consent Authorizations (by month)
- VAP Application User Logins (within 24 hours)
- VAP Application Web Calls (within 24 hours)

> ![](vap-version-1-user-guide/096.png)

> <span id="_bookmark174" class="anchor"></span>Figure 95: Reporting Dashboard

> The Expiring Authorizations (within 30 Days) widget displays two entries: eHealth Exchange Expiring Authorizations, and SSA Expiring Authorizations. The number to the right of each entry represents the number of authorizations expiring within a 30-day window, including today’s date. The counts displayed within the dashboard excludes test patients within the system, and filters results by All consents respectively for eHealth Exchange and SSA. If a user has a default facility selected within the VAP application, the counts displayed will be for only the facility selected and do not aggregate the counts of any children facilities. If a facility is not set by the user, as the default facility, then the counts will include all facilities.

> The New Consent Authorizations (by month) widget displays four entries: eBenefits, Manually Added, Re-Authorizations, and SSA Automated. The numbers to the right of each entry represent new consents and exclude records for test patients. The count of eBenefits consents is set to include all eHealth Exchange authorizations for the consent type. The count of manually added consents is set to include all eHealth Exchange authorizations and exclude consents submitted through web services from VA system (e.g., eBenefits). The count for Total Reauthorizations is set to pull all revocations with an inactivation reason of new authorization. If a user has a default facility selected within the VAP application, the counts displayed will be for only the facility selected and do not aggregate the counts of any children facilities. If a facility is

> not set by the user, as the default facility, then the counts will include all facilities. Use the Previous and Next buttons at the top of the widget to go back and forward through the list of months.

> The VAP Application User Logins (within 24 hours) widget displays a tabular chart with the number of VAP system user logins. Additionally, there is a view that graphically displays the user logins. On the graph, the vertical axis (y-axis) of the chart shows the past 24-hour timeframe, on the horizontal axis (x-axis) the user logins are displayed. This widget tallies the user logins for the VAP system as a whole, and is not specific to a facility.

> The VAP Application Web Calls (within 24 hours) widget displays a tabular chart of the number of web service calls. Additionally, there is a view that allows the user to display this table in a graphical format. The graph shows the number of web service calls made on the vertical axis (y-axis) and the past 24-hour Time frame on the horizontal axis (x-axis). This widget tallies the user logins for the VAP system as a whole, and is not specific to a facility.

#### Notes:

- Metric counts displayed contain only real patient values and exclude test patients.
- The changes to show tabular views of the VAP Application User Logins and VAP Application Web calls widgets were made to ensure Section 508 compliance.

### Disclosures Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Disclosures Summary Report query screen (Figure 96) allow you to select the disclosure source from either eHealth Exchange (Exchange) or Direct Secure Messaging (Direct). For both reports, the user may enter a search range which is inclusive of the start and end date supplied. For the eHealth Exchange Summary Disclosure report, the user may select a Patient Preferred facility or all VA Patient Preferred facilities, select an eHealth Exchange organization or all external eHealth Exchange organizations, and include or exclude test patients from the report in the system. The report provides a numerical summary of the disclosures for a selected range of dates at specific combinations of selected eHealth Exchange organizations and Patient Preferred facilities.

> Per request, updates were made to clarify whether a VA Facility is an Authenticating Facility or the Patient Preferred Facility. Field labels within the application were updated accordingly. This does not change the data that has been displayed within the system in prior releases, but simply clarifies the source VA Facility within the report.

#### ![](vap-version-1-user-guide/097.png)Generate a Disclosures Summary Report

1.  Click the Disclosures menu item under the Summary Reports heading on the menu at the top of the screen to display the Disclosures Summary Report query screen.

> <span id="_bookmark177" class="anchor"></span>Figure 96: Disclosures Summary Report Query Screen (eHealth Exchange)

![](vap-version-1-user-guide/098.png)

> <span id="_bookmark178" class="anchor"></span>Figure 97: Disclosures Summary Report Query Screen (Direct)

2.  Click on the down arrow to select the Disclosure Source either from Exchange (default) or Direct.
3.  For either report, enter the start date for the Disclosures Summary Report in the Start Date field in the format mm/dd/yyyy (i.e., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
4.  For either report, enter the end date for the Disclosures Summary Report in the End Date field in the format mm/dd/yyyy (i.e., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
5.  The following steps (a – c) are for eHealth Exchange Disclosure Summary Report.
    1.  Click the arrow at the right of the Patient Preferred Facility list box to select the facility you want to display in the report. All VA Patient Preferred facilities, not just supported ones, appear in the list. The list is sorted in ascending alphabetical order. You can only select one entry from the list.
        1.  The default VA Patient Preferred facility associated with the logged on (current) user is automatically selected from the list in the VA Patient Facility list box based on the user’s VA User ID. This default can be changed from Set Default User menu item under the Welcome menu.
        2.  ![](vap-version-1-user-guide/099.png)The All option is no longer the default setting. You must select it from the list if you want the report to include all VA Patient Preferred facilities.
        3.  If you are not sure of the name of a VA Patient Preferred facility, you can search for the facility by typing the beginning letter of the facility description (e.g., If the user types “N” in the VA Facility list box, the selection bar will move to the first VA facility that begins with “N.”) into the blank entry in the list.
    2.  Click the arrow at the right of the Organization list box to select the eHealth Exchange organization you want to display in the report. This reflects the organizations to which the VA disclosed records. You can only select one entry from the list. The default option for this list box is All. Organization names are formatted and spelled with uniformity across each input form and generated report.
    3.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
6.  For both reports, click the Search button to display the Disclosures Summary Report screen for Direct as shown in Figure 97 and for eHealth Exchange as shown in Figure 96.
    1.  Two of the possible entries in the eHealth Exchange Organization report column need additional explanation. UNKNOWN means that the eHealth Exchange Organization could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID field. NULL indicates invalid data from before UNKNOWN was defined.
    2.  Three of the entries in the VA Patient Preferred Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.
7.  If the eHealth Exchange Disclosures Summary Report (or any other report) finds no records (Figure 98), you probably selected your default VA Patient Preferred Facility on the query screen. The entry in the Patient Preferred Facility list box defaults to the VA Facility associated with your user name. Select All at the top of the list in the list box or a different VA Facility and search again.

> <span id="_bookmark179" class="anchor"></span>Figure 98: Disclosure Summary Report Screen - No Results Found

8.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order, (Null,

> Unavailable, and Unknown appear in line with the related Patient Preferred Facilities and/or eHealth Exchange Organizations when they occur).

> ![](vap-version-1-user-guide/100.png)

> <span id="_bookmark180" class="anchor"></span>Figure 99: Disclosures Summary Report Screen (eHealth Exchange)

![](vap-version-1-user-guide/101.png)

> <span id="_bookmark181" class="anchor"></span>Figure 100: Disclosures Summary Report Screen (Direct)

9.  The eHealth Exchange Report displays the following fields for each listing: eHealth Exchange Organization, Patient Preferred Facility, Patient Preferred Facility Station ID, and a Total indicating the number of disclosures for each combination of eHealth Exchange organization and Patient Facility. A total at the bottom right of the screen indicates the total number of disclosures covered by the report.
10. The Direct Report displays the following fields for each listing: Direct Endpoint, and a total indicating the number of disclosures for Direct. A total at the bottom of the screen indicates the total number of disclosures covered by the report.

#### Export the Disclosures Summary Report

11. Select the Export to Excel option on the top-right side of the report section seen in Figure 99 and Figure 100.
12. Unlike the detailed reports, no privacy warning is displayed prior to the export completing, as these summary-level reports do not contain personally identifiable

> ![](vap-version-1-user-guide/102.png)information. However, users are reminded to follow standard VA policies and procedures for information handling.

13. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report. and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

### Received eHealth Exchange Documents Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Received eHealth Exchange Documents Summary Report query screen (Figure 101) allow you to enter a range of dates, select a VA Patient Preferred facility or all VA Patient Preferred facilities, select an eHealth Exchange organization or all external eHealth Exchange organizations, and include/exclude test patients. The report provides a numerical summary of the eHealth Exchange documents received for a selected range of dates at specific combinations of selected eHealth Exchange organizations and VA facilities.

#### Generate a Received eHealth Exchange Documents Summary Report

1.  Click the Received eHealth Exchange Documents menu item under Summary Reports heading on the menu at the top of the screen to display the Received eHealth Exchange Documents Summary Report query screen.
2.  Enter the start date for the Received eHealth Exchange Documents Summary Report in the Start Date field in the format mm/dd/yyyy (i.e., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.

> <span id="_bookmark185" class="anchor"></span>Figure 101: Received eHealth Exchange Documents Summary Report Query Screen

3.  Enter the end date for the Received eHealth Exchange Documents Summary Report in the End Date field in the format mm/dd/yyyy (i.e., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
4.  Enter a user ID in the User ID field if you want to search by a specific user. The User ID field allows the report to be filtered either by full or partial name of the entity associated to the transaction. This field can refer to either the DVA User ID that entered a record. Search on the field is case insensitive, that is “smith” or “SMITH” will produce the same result set.
    1.  Note: Do not enter a User ID in this field if you want to search for all users.
5.  Click the arrow at the right of the Patient Preferred Facility list box to select the facility you want to display in the report. All Patient Preferred facilities, not just supported ones, now appear in the list. The list, except the entry for the Department of Veterans Affairs, is sorted in ascending alphabetical order. You can only select one entry from the list.
    1.  The default Patient Preferred facility associated with the logged on (current) user is automatically selected from the list in the VA Patient Facility list box based on the user’s VA User ID. This default can be changed by the user from the Set Default Facility menu item.
    2.  The All option is no longer the default setting. You must select it from the list if you want the report to include all VA facilities.
    3.  If you are not sure of the name of a VA facility, you can search for the facility by typing the beginning letter of the facility description (e.g., If the user types “N” in the VA Facility list box, the selection bar will move to the first VA facility that begins with “N.”) into the blank entry in the list.
6.  Click the arrow at the right of the Organization list box to select the eHealth Exchange organization you want to display in the report. This reflects the organizations from which the VA received records. You can only select one entry from the list. The default option for this list box is All, so do not select a specific organization if you want to see all external eHealth Exchange organizations in the report. The DEPARTMENT OF VETERANS AFFAIRS entry appears at the end of the list, not in alphabetical order.
7.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
8.  Click the Search button to display the Received eHealth Exchange Documents Report as shown in Figure 102.
    1.  Two of the possible entries in the eHealth Exchange Organization report column need additional explanation. UNKNOWN means that the eHealth Exchange Organization could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. NULL indicates invalid data from before UNKNOWN was defined.
    2.  Two of the entries that can appear in the VA Patient Preferred Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and

> ![](vap-version-1-user-guide/103.png)UNAVAILABLE were defined.

> <span id="_bookmark186" class="anchor"></span>Figure 102: Received eHealth Exchange Documents Summary Report Screen

9.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Null, Unavailable and Unknown appear in line with the related VA Patient Preferred Facilities and/or eHealth Exchange Organizations when they occur.)
10. The report displays the following fields for each listing: eHealth Exchange Organization, Patient Preferred Facility, Patient Preferred Facility Station ID, and a Total indicating the number of received eHealth Exchange documents for each combination of eHealth Exchange organization and VA facility. A grand total at the bottom of the screen indicates the total number of received eHealth Exchange documents covered by the report.

#### Export the Disclosures Summary Report

11. Select the Export to Excel option on the top-right side of the report section seen in Figure 102.
12. Unlike the detailed reports, no privacy warning is displayed prior to completing the export, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
13. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> Note: Not displayed within the VAP User Interface, and only within the export, is the Organization Identifier Code (OID).

### Document Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vap-version-1-user-guide/104.png)The fields on the Document Size Report query screen (Figure 103) allow you to enter a range of dates, select an eHealth Exchange Organization or all organizations, and select the Action Type. This report displays the count of received and disclosed documents, to partners, along with the minimum, maximum, and average document sizes for a selected time period. The data within this report is received from the eHealth Exchange system. It is important to note that the file sizes within this report are displayed in kilobytes (kb). VAP does not store this information within its system boundary, and similarly to the Received eHealth Exchange and the Disclosures report, this document is retrieved on demand via web service.

> <span id="_bookmark189" class="anchor"></span>Figure 103: Document Size Report Query Screen

#### Generate a Document Size Report

1.  Click the Document Size menu item under Summary Reports heading on the menu at the top of the screen to display the Document Size Summary Report query screen.
2.  Enter the start date for the Document Size report in the Start Date field in the format mm/dd/yyyy (i.e., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
3.  Enter the end date in the End Date field in the format mm/dd/yyyy (i.e., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
4.  Click the arrow at the right of the Organization list box to select the eHealth Exchange organization you want to display in the report. All eHealth Exchange Organizations, not just supported ones, now appear in the list and is set as default. The list, except the entry for the Department of Veterans Affairs, is sorted in ascending alphabetical order. You can only select one entry from the list. All Active Organizations are listed followed by the Inactive Organizations.
5.  Click the arrow at the right of the Action Type list box to select to include the counts of only received documents from partners, disclosed documents to partners, or both. This allows the user to filter out the resultant data within the report by received documents only, disclosed, or both.
6.  ![](vap-version-1-user-guide/105.png)Click the Search button to display the Document Size Report as shown in Figure 104.

> <span id="_bookmark191" class="anchor"></span>Figure 104: Document Size Report Screen

7.  The report displays the following fields for each listing: eHealth Exchange Organizations, LOINC Code (results type), Title (of documents exchanged), Number of Documents, Average Size (of documents exchanged in kb), Minimum Size (smallest document in kb), and Maximum Size (largest document in kb).

#### Export the Document Size Report

8.  Select the Export to Excel option on the top right side of the report section, as seen in Figure 103.
9.  Unlike the detailed reports, no privacy warning is displayed prior to the export completing, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
10. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel.

### Consent Directive Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Consent Directive Summary Report query screen (Figure 105) allow you to enter a range of dates, select an Authenticating facility or all Authenticating facilities, select the consent type, and include/exclude test. This report provides a summary listing of the selected Consent Directive totals for a selected range of dates at the selected Authenticating facility or

> facilities.

> ![](vap-version-1-user-guide/106.png)

> <span id="_bookmark194" class="anchor"></span>Figure 105: Consent Directive Summary Report Query Screen

#### Generate a Consent Directive Summary Report

1.  Click the Consent Directive menu item under Summary Reports heading on the menu at the top of the screen to display the Consent Directive Summary Report query screen.
2.  Enter the start date for the Consent Directive Summary Report in the Start Date field in the format mm/dd/yyyy (i.e., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
3.  Enter the end date for the Consent Directive Summary Report in the End Date field in the format mm/dd/yyyy (i.e., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
4.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The All option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections. For each section, you may Select/Unselect all from the top right, seen in Figure 106 below.
    2.  The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 106. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked. If selected, aggregate data at the facility level, this means the data will be rolled- up and aggregated to the parent-level. All children-level facilities will not be displayed and the counts will be included within the parent. This functionality is based on the relationships set within the Facilities administrator section of the VAP application.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that is displaying all facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/107.png)

> ![](vap-version-1-user-guide/108.png)<span id="_bookmark196" class="anchor"></span>Figure 106: Select Facilities Pop-Up Window

5.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see Real Patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
6.  Click the Search button to display the Consent Directive Summary Report as shown in Figure 107 and Figure 108.
7.  The entries that can appear in the VA Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.

> <span id="_bookmark197" class="anchor"></span>Figure 107: Consent Directive Summary Report Screen (Top)

![](vap-version-1-user-guide/109.png)

> <span id="_bookmark198" class="anchor"></span>Figure 108: Consent Directive Summary Report Screen (Bottom)

8.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Null, Unavailable, and Unknown appear in line with the related Authenticating Facilities and/or eHealth Exchange Organizations when they occur).
9.  The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.
10. The report displays the following fields for each listing: Authenticating Facility, eHealth Exchange Authorizations, eHealth Exchange Revocations, eHealth Exchange Restrictions, eHealth Exchange Restriction Revocations, SSA Authorizations, and SSA Revocations.

#### Export the Consent Directive Summary Report

11. Select the Export to Excel option on the top-right side of the report section seen in Figure 107.
12. Unlike the detailed reports, no privacy warning is displayed prior to completing the export, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
13. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

### Opt-In Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Opt-In Summary Report displays the transaction history without regard to the current status of all patients with opt in status as shown in Figure 109. In this report, the user may filter by Authenticating Facilities, Consent Type, Entered By, and Patient Types.

![](vap-version-1-user-guide/110.png)

> ![](vap-version-1-user-guide/111.png)<span id="_bookmark201" class="anchor"></span>Figure 109: Opt-In Summary Report Results (Top)

> <span id="_bookmark202" class="anchor"></span>Figure 110: Opt-In Summary Report Results (Bottom)

#### Generate an Opt-In Summary Report

1.  Click the Opt-In Patients menu item under Summary Reports heading on the menu at the top of the screen to display the Opt-In Summary Report query screen.
2.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The All option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 111 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 111. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection, will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that’s displaying all facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/112.png)

> <span id="_bookmark204" class="anchor"></span>Figure 111: Select Facilities Pop-Up Window

3.  Click the arrow to the right of Consent Types list box to select the types of consents to be displayed on the report. The default option for this list box is All Types. There are three options in the list: All, eHealth Exchange Authorizations, or, SSA Authorizations. If results should be limited to eHealth Exchange Authorizations, then no SSA counts will be displayed (shown as 0). If SSA Authorizations are selected, then, alternatively, no eHealth Exchange counts will be displayed (shown as 0).
4.  Enter a valid VA username in the Entered By field, if desired, to filter the results by counts manually submitted by that ROI administrator/user within the VAP application. It is important to note that this will only function on consents manually submitted through the VAP application. To search by eBenefits, type “eBenefits” into the box.
5.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
6.  The report, seen in Figure 109 and Figure 110 under search fields, displays the Authenticating Facility, eHealth Exchange Authorization, SSA Authorization, and Facility Total.

#### Export the Opt-In Patient Summary Report

7.  Select the Export to Excel option on the top-right side of the report section seen in Figure 109.
8.  Unlike the detailed reports, no privacy warning is displayed prior to completing the export, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
9.  Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

### Delayed Consent Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vap-version-1-user-guide/113.png)The Delayed Consent Summary Report, Figure 112, allows you to select Authenticating Facility(s), reason or reasons for delay, days since delayed, consent type, and patient types. This report provides a summary listing of the selected Delayed Consent totals at the selected Authenticating facility or facilities.

> <span id="_bookmark207" class="anchor"></span>Figure 112: Delayed Consent Summary Report

#### Generate a Delayed Consent Summary Report

1.  Click the Delayed Consent menu item under Summary Reports heading on the menu at the top of the screen to display the Delayed Consent Summary Report query screen.
2.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The All option is not the default setting; you must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 113 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the Facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 113. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection, will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that is displaying all

> facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/114.png)

> <span id="_bookmark209" class="anchor"></span>Figure 113: Select Facilities Pop-Up Windows

3.  Check one or multiple of the reason(s) for delay checkboxes that you want to display in your Delayed Consent Summary Report. By default, All reasons for delay will be displayed. Do not select a specific option if you want to see all reasons in the report.
4.  Click the arrow at the right of the Days Since Delayed list box to select the range of days, since the status have been delayed, you want to display in the report.
5.  Click the arrow at the right of the Consent Type list box to select the types of consent you want to display in the report. The default option for this list box is All, so do not select a specific option if you want to see all types of consent. There are two other options in the list: eHealth Exchange Authorizations, SSA Authorizations. You can only select one entry from the list.
6.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in

> ![](vap-version-1-user-guide/115.png)the list: All (Real and Test Patients), Real Patients, and Test Patients.

> <span id="_bookmark210" class="anchor"></span>Figure 114: Delayed Consent Summary Report

7.  Click the Search button to display the Delayed Consent Summary Report as shown in Figure 114.
    1.  Two of the possible entries in the eHealth Exchange Organization report column need additional explanation. UNKNOWN means that the eHealth Exchange Organization could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. NULL indicates invalid data from before UNKNOWN was defined.
    2.  Two of the entries that can appear in the VA Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.
8.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Null, Unavailable, and Unknown appear in line with the related VA Facilities and/or eHealth Exchange Organizations when they occur.)
9.  The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> Note: The report displays the Authenticating Facility, Consent Type, and Total.

#### Export the Delayed Consent Summary Report

10. Select the Export to Excel option on the top-right side of the report section seen in Figure 114.
11. Unlike the detailed reports, no privacy warning is displayed prior to completing the export, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
12. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

### Patient Discovery Audit Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Discovery Audit Summary Report, Figure 115, allows you to enter a range of dates, select a Patient Preferred facility or all Patient Preferred facilities, and select an eHealth Exchange Organization or all eHealth Exchange Organizations. This report displays a summary listing of the number of real versus test patient transactions and whether they succeeded or failed as shown in Figure 115. The Patient Discovery audit log is ordered to ensure that the sequence of events recorded is a reflection of what actually transpired. A recent change to this report is the ability to filter the resultant report by hour/minute. Due to the increasing amount of data and the millions of records, this allows the user to fine-tune the results to obtain better counts on a daily basis. It is important to note that due to the immense quantity of data within this report (millions of records), searching for several weeks or months may take a few minutes to process.

> ![](vap-version-1-user-guide/116.png)Note: Field labels within the application clarify whether a VA Facility within a report is an Authenticating Facility or the Patient Preferred Facility.

> <span id="_bookmark213" class="anchor"></span>Figure 115: Patient Discovery Audit Summary Report

#### Generate a Patient Discovery Audit Summary Report

1.  Click the Patient Discovery Audit menu item under Summary Reports heading on the menu at the top of the screen to display the Patient Discovery Audit Summary Report query screen.
2.  Enter the start date for the Patient Discovery Audit Summary Report in the Start Date field in the format mm/dd/yyyy (i.e., 07/20/2015). You can also select the date from the date range picker dropdown. Select a starting time frame using the Start Time fields. Use the dropdowns to select the hours, minutes, and meridian. As a user, you should be mindful that the VAP application is hosted at the Austin Information Technology Center (AITC) and uses Central Standard Time (CST). If you are located in a different time zone and are looking for a particular announcement made by you, remember the time difference!
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
3.  Enter the end date for the Patient Discovery Audit Summary Report in the End Date field in the format mm/dd/yyyy (i.e., 10/18/2015). You can also select the date from the date range picker dropdown. Select an ending time frame using the End Time fields. Use the dropdowns to select the hours, minutes, and meridian. Again, be mindful of the time difference, if located in a different time zone. VAP is on Central Standard Time (CST).
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
4.  Enter a user ID in the User ID field if you want to search for a specific user.
    1.  Note: Do not enter a User ID in this field if you want to search for all users.
5.  Click the arrow to the right of the Patient Preferred Facility list box to select the facility you want to display in the report. The list of facilities to be displayed within this menu is stored internally within the VAP application. To add or delete a facility, contact your VAP administrator to make the modifications on the “Facilities” management pages in the admin section of the VAP application. You can only select one entry from the list.
    1.  The default Patient Preferred facility associated with the logged on (current) user is automatically selected from the list in the Patient Facility list box based on the user’s VA User ID. This default can be changed by the user from the Set Default Facility menu item.
    2.  The All option is not set as a default setting. If you would like to run a report for all VA facilities, then you must select the “All Facilities” option.
    3.  If you are not sure of the name of a VA facility, you can search for the facility by typing the beginning letter of the facility description (e.g., If the user types “N” in the VA Facility list box, the selection bar will move to the first VA facility that begins with “N.”) into the blank entry in the list.
6.  Click the arrow at the right of the Sending Organization or Receiving Organization list box to select the eHealth Exchange organization you want to display in the report. Both Senders and Receivers cannot be selected as filters, and the VAP application will display

> ![](vap-version-1-user-guide/117.png)a user reminder if both are used. This is due to the fact that VAP only tracks outbound transactions leaving Department of VA and inbound transactions to the Department of VA. Communication between partners (such as an instance when the Sender is Epic and the Receiver is Kaiser Permanente) will not be found within the system. All Active Organizations are listed first, followed by the Inactive Organizations.

7.  Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see Real Patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
8.  Click the Search button to display the Patient Discovery Audit Summary Report as shown in Figure 116.

> <span id="_bookmark215" class="anchor"></span>Figure 116: Patient Discovery Audit Summary Report Results

9.  The report, Figure 116, displays the eHealth Exchange Organization, Patient Preferred Facility, Audits, Unique Real Patients, Matches Found for Real Patients, Match Fails for Real Patients, Unique Test Patients, Matches Found for Test Patients, and Match Fails for Test Patients. The total audits are shown at the bottom of the report page.

#### Export the Patient Discovery Audit Summary Report

10. Select the Export to Excel option on the top-right side of the report section seen in Figure 114.
11. Unlike the Detailed reports, no privacy warning is displayed prior to completing the export, as these summary-level reports do not contain personally identifiable information. However, users are reminded to follow standard VA policies and procedures for information handling.
12. Report data is exported into an Excel spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

## Generating Detailed Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VAP application generates eight (8) detailed reports:

- Disclosures
- Received eHealth Exchange Documents
- Consent Directive
- Opt-In Patients
- Expiring Consent
- Delayed Consent
- Patient Discovery Audit
- Scheduled Exports

> Each report is described below in more detail. The Report options are available to all users.

> If there is a document which linked to a row in a report (i.e., a View link appears at the end of the row), the document may be viewed by clicking the link. The displayed document can then be printed by clicking the Printer icon at the top of the screen. This process is detailed below at the end of Section 4.6.1 Disclosures Report.

### Disclosures Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Accounting of Disclosure Report query screen (Figure 117) allow you to create an accounting of disclosures report for all health information released to non-VA providers through the use of Exchange or Direct. Enter a Veteran’s SSN, Last Name and First Name, enter a range of Start Date and End Date, select an authenticating facility or all facilities, select an eHealth Exchange organization or all external eHealth Exchange organizations, include/exclude test patients and set the number of records per page for the report. This report provides a detailed listing of one or multiple records of patient information for one or more Veterans for a selected range of dates with a combination of selected VA facilities and eHealth Exchange organization or organizations.

#### Generate an Accounting of Disclosures Report

1.  Click the Disclosures menu item under Detailed Reports heading on the menu at the top of the screen to display the Accounting of Disclosures Report query screen.
2.  Click on the down arrow to select the Disclosure Source either from Exchange (default) or Direct.
3.  Enter the SSN for a specific patient in the format \######### (no hyphens) in the SSN field. Do not enter a SSN in this field or names in the Last Name and First Name fields if you want to search for all patients in the context of the other parameters you enter.
4.  Enter a last name for one or more patients in the Last Name field. Leave the SSN and First Name fields blank if you want to search for patients with the same Last Name. Do not enter a last name in this field or a first name in the First Name field if you want to

> search for a patient based on his or her SSN.

> ![](vap-version-1-user-guide/118.png)

> <span id="_bookmark220" class="anchor"></span>Figure 117: Accounting of Disclosures Report Query Screen (Exchange)

5.  Enter a first name for one or more patients in the First Name field. Leave the SSN and Last Name fields blank if you want to search for patients with the same first name. Do not enter a first name in this field or a last name in the Last Name field if you want to search for a patient based on his or her SSN.
6.  Enter the start date for the Accounting of Disclosures Report in the Start Date field in the format mm/dd/yyyy (i.e., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
7.  Enter the end date for the Accounting of Disclosures Report in the End Date field in the format mm/dd/yyyy (i.e., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
8.  Click the arrow at the right of the Purpose of Use list box to select one entry of the following options: Treatment, Emergency, or Coverage.
9.  Click the arrow at the right of the Patient Preferred Facility list box to select the facility you want to display in the report. All VA Patient Preferred facilities, not just supported ones, appear in the list. The list, except the entry for the Department of Veterans Affairs, is sorted in ascending alphabetical order. You can only select one entry from the list.
    1.  The default VA facility associated with the logged on (current) user is automatically selected from the list in the VA Patient Facility list box based on the user’s VA User ID. This default can be changed by the user from the Set Default Facility menu item.
    2.  The All option is not the default setting. You must select it from the list if you want the report to include all VA Patient Preferred facilities. If you are generating this report for a specific patient request, select the All option to ensure that all records that have been disclosed for that particular patient are returned.
    3.  If you are not sure of the name of a VA facility, you can search for the facility by typing the beginning letter of the facility description (e.g., If the user types “N” in

> the VA Patient Preferred Facility list box, the selection bar will move to the first VA facility that begins with “N.”) into the blank entry in the list.

10. Click the arrow to the right of the Organization list box to select the eHealth Exchange organization you want to display in the report. This reflects the organizations to which the VA disclosed records. You can only select one entry from the list. The default option for this list box is All, so do not select a specific organization if you want to see all external eHealth Exchange organizations in the report.
    1.  If you are generating this report for a specific patient request, select the All option to ensure that all records that have been disclosed for that particular patient are returned.
    2.  The DEPARTMENT OF VETERANS AFFAIRS entry appears at the end of the list, not in alphabetical order.
11. Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
12. Click the Search button to display the Accounting of Disclosures Report as shown in Figure 118 for Exchange Disclosures and as shown in Figure 119 for Direct Disclosures.
    1.  The entries in the VA Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.
    2.  The possible entries in the eHealth Exchange Organization report column need additional explanation. UNKNOWN means that the eHealth Exchange Organization could not be resolved by the ESR for the given Patient ID. NULL indicates invalid data from before UNKNOWN was defined.
13. Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. The All option has been removed for performance reasons. To allow users to display additional options, 250 and 500 records per page were added. This field now allows users to select by 10, 25, 50, 100, 250 and 500.
    1.  In Figure 118, SSN (9 digits), Patient Last Name, Patient First Name, Date of Disclosures, Disclosures, Patient Preferred Facility, Patient Preferred Facility Station ID, eHealth Exchange Organization, User ID, Purpose of Use, User Role, and View are available fields for the Disclosures Report if the disclosure source

> ![](vap-version-1-user-guide/119.png)![](vap-version-1-user-guide/120.png)from eHealth Exchange.

> <span id="_bookmark221" class="anchor"></span>Figure 118: Accounting of Disclosures Report Screen (Exchange)

2.  In Figure 119, SSN (9 digits), Patient Last Name, Patient First Name, Date of Disclosures, Disclosures, Direct Address, User ID, and Purpose of Use are available fields for the Disclosures Report if the disclosure source is Direct.

> <span id="_bookmark222" class="anchor"></span>Figure 119: Accounting of Disclosures Report Screen (Direct)

14. A View link in Figure 118 at the end of each listing allows authorized users to review the actual record disclosed on a Document View screen (Figure 119 and Figure 120). The entries in the Disclosures column of the report indicate whether the View links display Summarization of Episode Notes (C32), Discharge Summarization Notes (C62), other C62 documents if they are available, or CCDAs. The C62 documents can be viewed in a non-editable PDF format. Since the C62 documents are unstructured, the generated PDFs simply capture the unstructured information in PDF format without any manipulations. The latest CCDA stylesheet was added.
    1.  If the entry in this column reads "Department of Veterans Affairs Summarization of Episode Note," the View link displays a C32 Form as shown in Figure 120. The Summarization of Episode Note (C32) displays the information available on the specific C32 form referenced in the report. (Entries linked to different rows can have different content.) The information that can appear in this document is

> discussed above in detail in Section 4.2.2 Health Summary (C32) Tab (Figure 24 to Figure 27).

> ![](vap-version-1-user-guide/121.png)

> <span id="_bookmark223" class="anchor"></span>Figure 120: Document View Screen for Summarization of Episode Note

2.  If the entry reads "Department of Veterans Affairs Discharge Summary," the View link displays a C62 Form as shown in Figure 121. The Discharge summarization note (C62) shows the following information about the discharged patient: date the note was created, patient first name, patient last name, patient address, Patient ID, home telephone number, birth date, sex, language(s), source of the note (VA Facility and author), emergency contact information, and date the note was electronically generated. (Entries linked to different rows have different content.) Other C62-related documents may be available.
15. Click the View attachment link (immediately above the Emergency Contact information section) to display the following detailed Discharge summarization note information in a text file: local title (Discharge Summary), standard title (Discharge Summary), dictated date (mm, dd, yyyy), entry date (mm, dd, yyyy), name of person dictating the note, attending \[provider\], urgency (e.g., Routine), status (e.g., Completed), date of admission (mm/dd/yyyy), date of discharge (mm/dd/yyyy), principle discharge diagnosis, additional diagnoses, consultant(s), procedure(s), brief admission history, brief admission physical exam, admission lab/EKG/x-ray results, hospital course, condition on discharge, discharge instructions (activity, diet, medications, special Instructions, and follow-up plans), and provider and cosigner signatures. Different fields may appear on different

> documents.

> ![](vap-version-1-user-guide/122.png)

> <span id="_bookmark224" class="anchor"></span>Figure 121: Document View Screen for Discharge Summarization Note

1.  Note: If the .txt file does not display properly when opened, you may need to modify the program that is associated with opening the file. See the instructions in Appendix A.
16. Click the Back to Report Results link to exit either Document View screen and return to the report display.
17. Click the Printer icon in the upper left corner of the Document View screen to open a standard Windows Print dialog box (Figure 122) that allows you to print the document.
    1.  Click the Print button to send the document to a printer. You can print the document using standard Windows printing functionality.
        1.  Note: Warning! The documents printed with this option display personal health information. They should be retrieved quickly from the printer and managed in accordance with all applicable privacy rules and standards.
    2.  Click the Cancel button to clear the dialog box and return to the Document View screen.
    3.  The Apply button is activated if you change any of the settings in the Print dialog box. Click the button to apply any changes you made.

> ![](vap-version-1-user-guide/123.png)

> <span id="_bookmark225" class="anchor"></span>Figure 122: Print Dialog Box

18. If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
19. Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Unknown and Unavailable sort to the top in ascending order sorts while other facilities and organizations sort alphabetically in ascending order. Unknown and Unavailable sort to the bottom in descending order sorts while other facilities and organizations sort alphabetically in descending order.)
20. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.
    1.  As shown in Figure 118, the report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Date of Disclosure (including time), Disclosures, Patient Preferred Facility, Patient Preferred Facility Station ID, eHealth Exchange Organization (the organization to which the VA disclosed records), User ID (of the person who retrieved the data), Purpose of Use (i.e., how the information disclosed will be used (Coverage (SSA), Emergency, and Treatment), User Role, and a View link.
    2.  As shown in Figure 119, the report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Date of Disclosure (including time), Disclosures, Direct Address, User ID (of the person who retrieved the data), and Purpose of Use (i.e., how the information disclosed will be used (Coverage (SSA), Emergency, and Treatment).

#### Export the Disclosure Detailed Report

21. Select the Export to Excel or Export to CSV option on the top-right side of the report section seen in Figure 118 and Figure 119.
22. Unlike the summary reports, a privacy warning, Figure 123, is displayed prior to the export completing, as these detailed-level reports contain personally identifiable information.
23. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The Column Headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> ![](vap-version-1-user-guide/124.png)Note: Not displayed within the VAP User Interface, and only in the Export, the VAP system displays Organization Identifier Code (OID).

> <span id="_bookmark227" class="anchor"></span>Figure 123: Export Warning Message and Exported Excel

### Received eHealth Exchange Documents Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Received eHealth Exchange Documents Report query screen (Figure 124) allow you to enter a Veteran’s SSN and name or select all Veterans, enter a range of dates, select a Patient Preferred facility or all Patient Preferred facilities, select an eHealth Exchange organization or all external eHealth Exchange organizations, include/exclude test patients and set the number of records per page for the report. This report provides a detailed listing of reports requested and received for one or more patients for a selected range of dates with a combination of selected VA Patient Preferred facilities and eHealth Exchange organizations.

#### Generate a Received eHealth Exchange Documents Report

1.  Click the Received eHealth Exchange Documents menu item under the Detailed Reports heading on the menu at the top of the screen to display the Received eHealth

> ![](vap-version-1-user-guide/125.png)Exchange Documents Report query screen.

> <span id="_bookmark230" class="anchor"></span>Figure 124: Received eHealth Exchange Documents Report Query Screen

2.  Enter the SSN for a specific patient in the format \######### (no hyphens) in the SSN field. Do not enter a SSN in this field or names in the Last Name and First Name fields if you want to search for all patients in the context of the other parameters you enter.
3.  Enter a last name for one or more patients in the Last Name field. Leave the SSN and First Name fields blank if you want to search for patients with the same last name. Do not enter a last name in this field or a first name in the First Name field if you want to search for a patient based on his or her SSN.
4.  Enter a first name for one or more patients in the First Name field. Leave the SSN and Last Name fields blank if you want to search for patients with the same first name. Do not enter a first name in this field or a last name in the Last Name field if you want to search for a patient based on his or her SSN.
5.  Enter a user ID in the User ID field if you want to search for a specific user.
    1.  Note: Do not enter a User ID in this field if you want to search for all users.
6.  Enter the start date for the Received eHealth Exchange Document Report in the Start Date field in the format mm/dd/yyyy (e.g., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
7.  Enter the end date for the Consent Directive Report in the End Date field in the format mm/dd/yyyy (e.g., 02/14/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
8.  Click the arrow at the right of the Purpose of Use list box to select one entry of the following options: Treatment, Emergency, or Coverage.
9.  Click the arrow at the right of the Patient Preferred Facility list box to select the facility you want to display in the report. All VA Patient Preferred facilities, not just supported ones, now appear in the list. You can only select one entry from the list.
    1.  The default Patient Preferred VA facility associated with the logged on (current) user is automatically selected from the list in the VA Patient Preferred Facility list box based on the user’s VA User ID. This default can be changed by the user from the Set Default Facility menu item.
    2.  The All option is not the default setting. You must select it from the list if you want the report to include all VA Patient Preferred facilities.
    3.  If you are not sure of the name of a VA Patient Preferred facility, you can search for the facility by typing the beginning letters of the facility description (e.g., If the user types “N” in the VA Facility list box, the selection bar will move to the first VA facility that begins with “N.”) into the blank entry in the list.
10. Click the arrow at the right of the Organization list box to select the eHealth Exchange organization you want to display in the report. You can only select one entry from the list. The default option for this list box is All, so do not select a specific organization if you want to see all external eHealth Exchange organizations in the report. The Department of Veterans Affairs entry appears at the end of the list, not in alphabetical order.
11. Click the Search button to display the Received eHealth Exchange Documents Report as shown in Figure 125.
    1.  Three of the entries in the VA Patient Preferred Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.
    2.  Two of the possible entries in the eHealth Exchange Organization report column need additional explanation. UNKNOWN means that the eHealth Exchange Organization could not be resolved by the ESR for the given Patient ID. NULL indicates invalid data from before UNKNOWN was defined.
12. Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. This field also allows users to select 10, 25, 50, 100, 250 and 500.
13. A View link at the end of each listing allows authorized users to review the actual record requested (Figure 124). The Printer icon at the top left of the screen displaying the record allows you to print the document. Click the link to open a standard Windows File Download dialog box. Steps 15-17 of Section 4.6.1 Disclosures Report, and Figure 120 – Figure 122 detail this process.
14. For some reports there may be a View Attachment link above the Emergency Contact information. Click the link to open the report.
    1.  Note: If the report does not display properly when the link is clicked you may need to modify the program that is associated with opening the file. See Appendix A, Section 7.2 for help setting Windows to open the document with the correct application.
15. If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
16. Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Unknown and

> ![](vap-version-1-user-guide/126.png)Unavailable sort to the top in ascending order sorts while other facilities and organizations sort alphabetically in ascending order. Unknown and Unavailable sort to the bottom in descending order sorts while other facilities and organizations sort alphabetically in descending order.)

17. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> <span id="_bookmark231" class="anchor"></span>Figure 125: Received eHealth Exchange Documents Report Screen

18. The report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Date Received (including time), Document Title (name of the document), Patient Preferred Facility, Patient Preferred Facility Station ID, eHealth exchange Organization (source of the document), User ID (person requesting the disclosure), User Facility, Purpose of Use (i.e., how the information disclosed will be used: Coverage (SSA), Emergency, and Treatment), User Role, System ID and a View link. Within the report results, the User Facility is a computed field. This field is derived from the User’s Facility Code. The System ID is used by the VAP Technical teams to troubleshoot which system the transaction originated from.

#### Export the Received eHealth Exchange Documents Detailed Report

19. Select the Export to Excel or Export to CSV option on the top-right side of the report section seen in Figure 125.
20. Unlike the summary reports, a privacy warning, Figure 126, is displayed prior to completing the export, as these detailed-level reports contain personally identifiable information.
21. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> ![](vap-version-1-user-guide/127.png)

> <span id="4.6.3._Consent_Directive_Detailed" class="anchor"></span>Figure 126: Export Warning Message

> ![](vap-version-1-user-guide/128.png)This report differs from other reports, in that the columns on the user interface do not exactly match the columns on the Excel report. The User ID column is parsed in the Excel spreadsheet as four separate columns: User ID, User Facility Code, User Facility, and User Name.

> <span id="_bookmark234" class="anchor"></span>Figure 127: User ID Parsed in Columns

> ![](vap-version-1-user-guide/129.png)Additionally, not displayed within the VAP User Interface, and only in the export, the VAP system displays Organization Identifier Code (OID), as highlighted in Figure 128.

> <span id="_bookmark235" class="anchor"></span>Figure 128: Exported Received eHealth Exchange Documents Report Displaying OID (Excel)

### Consent Directive Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Consent Directive Report query screen (Figure 128) allow users to enter a Veteran’s SSN and name or select all Veterans, enter a range of dates, select an Authenticating Facility or all Authenticating Facilities, select the actions to be covered, select a type of consent or all types, select a reason for revoking record sharing or all reasons, include/exclude test patients and set the number of records per page for the report. This report provides a detailed listing of specified authorization, restriction, and revocation activity for one or more patients for a selected range of dates at selected VA Authenticating facilities.

#### ![](vap-version-1-user-guide/130.png)Generate a Consent Directive Report

1.  Click the Consent Directive menu item under the Detailed Reports heading on the menu at the top of the screen to display the Consent Directive Report query screen.

> <span id="_bookmark238" class="anchor"></span>Figure 129: Consent Directive Report Query Screen

2.  Enter the SSN for a specific patient in the format \######### (no hyphens) in the SSN field. Do not enter a SSN in this field or names in the Last Name and First Name fields if you want to search for all patients in the context of the other parameters you enter.
3.  Enter a last name for one or more patients in the Last Name field. Leave the SSN and First Name fields blank if you want to search for patients with the same last name. Do not enter a last name in this field or a first name in the First Name field if you want to search for a patient based on his or her SSN.
4.  Enter a first name for one or more patients in the First Name field. Leave the SSN and Last Name fields blank if you want to search for patients with the same first name. Do not enter a first name in this field or a last name in the Last Name field if you want to search for a patient based on his or her SSN.
5.  Enter the start date for the Consent Directive Report in the Start Date field in the format mm/dd/yyyy (e.g., 02/12/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the End Date field if you want to search for all dates.
6.  Enter the end date for the Consent Directive Report in the End Date field in the format mm/dd/yyyy (e.g., 02/13/2015). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
7.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The ALL option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 130 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box under the middle section, seen in Figure 130. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that is displaying all

> facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/131.png)

> <span id="_bookmark239" class="anchor"></span>Figure 130: Select Facilities Pop-Up Window

8.  Click the arrow at the right of the Consent Type list box to select the types of consent you want to display in the report. The default option for this list box is All, so do not select a specific option if you want to see all types of consent. There are eight other options in the list: All Authorizations, All Revocations, eHealth Exchange Authorizations, SSA Authorizations, eHealth Exchange Revocations, SSA Revocations, eHealth Exchange Restrictions, and eHealth Exchange Restrictions Revocations. You can only select one entry from the list.
9.  The Inactivation Reason list box is not pictured in Figure 129. It does not appear on the query screen until one of the Revocation entries in the Consent Type list box is selected. When the field does appear, click the arrow at the right of this list box to select the reason why the Consent Directive became inactive. The default option for this list box is All, so do not select a specific option if you want to see all inactivation reasons. There are six options in the list: All, New Authorization, Patient Deceased, Entered in Error, Authorization Expired, and Revoked. You can only select one entry from the list.
10. Enter a name or User ID in the Entered By field to filter by either full or partial name of the entity associated with the transaction. This field can refer to either DVA User ID that entered a record (for example, "smith"), or a system that initiated a transaction (for example, "eBenefits"). Search on this field is case insensitive; that is, values of "smith" and "SMITH" will produce the same result set.
11. Click the Search button to display the Consent Directive Report as shown in Figure 132.
12. Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. This field allows users to select 10, 25, 50, 100, 250 and 500.
13. The entries in the VA Authenticating Facility report column need additional explanation. UNKNOWN means that the Patient Preferred Facility could not be resolved by the Enrollment System Redesign (ESR) for the given Patient ID. UNAVAILABLE means that ESR is not available. NULL indicates invalid data from before UNKNOWN and UNAVAILABLE were defined.
14. A View button at the end allows authorized users to review the actual record requested (Figure 133) when available. Click the View button to view.
15. ![](vap-version-1-user-guide/132.png)A View Restriction button at the end, Figure 132 and Figure 133, allows authorized users to review the restriction details of the restricted organization(s), seen in Figure 131.

> <span id="_bookmark240" class="anchor"></span>Figure 131: Restriction Details (Restricted Organization)

16. If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
17. Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order. (Null, Unavailable, and Unknown appear inline when they occur.)

> ![](vap-version-1-user-guide/133.png)

> <span id="_bookmark241" class="anchor"></span>Figure 132: Consent Directive Detailed Report Screen

![](vap-version-1-user-guide/134.png)

> <span id="_bookmark242" class="anchor"></span>Figure 133: Consent Directive Detailed Report Screen (Showing View)

18. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.
19. The report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Time of Event (including date), Patient Signature / Patient Deceased Date, Purpose of Use (i.e., how the information disclosed will be used: Coverage (SSA), Emergency, and Treatment), Consent Type, Inactivation Reason, Entered By (person initiating the event listed), Authenticating Facility, Authenticating Facility Station ID, VISN, and a View link.

#### Export the Consent Directive Detailed Report

20. Select the Export to Excel or Export to CSV option on the top right side of the report section seen in Figure 132.
21. Unlike the summary reports, a privacy warning, Figure 134, is displayed prior to completing the export, as these detailed-level reports contain personally identifiable information.
22. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same as the generated report, and data in the exported file is sorted as it was on the report.

> ![](vap-version-1-user-guide/135.png)Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> ![](vap-version-1-user-guide/136.png)<span id="4.6.4._Opt-In_Detailed" class="anchor"></span>Figure 134: Export Warning Message

### Opt-In Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields on the Opt-In Detailed Report query screen (Figure 134) allow you to enter VA Authenticating Facility, Consent Type, Entered By, Start Date and End Date for the report. A new feature is the functionality to select by either Opt-In Date or Entry Date. The Entry Date is the date which consent was entered into the VAP application (manually) by a VAP system user. The other selection date option is to choose to generate the report by Opt-In Date. This date indicates the date which the Veteran signed the consent authorization form. This is done to allow VAP users to view both the date the consent was entered into the system and the date the consent was signed. As of July 2018, it is highly advised and requested to not search by Entry Date. This is a complex search that touches two of the largest tables in the database and negatively impacts performance. A fix is planned within Release 3.2.0; however, at this time, users are advised not to utilize the entry date option until further notice. This report provides a detailed listing of opt-in patients at selected VA Authenticating facilities.

#### Generate an Opt-In Detailed Report

1.  Click the Opt-In Patients menu item under the Detailed Reports heading on the menu at the top of the screen to display the Opt-In Detailed Report query screen.

> <span id="_bookmark247" class="anchor"></span>Figure 135: Opt-In Detailed Report Query Screen

2.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The ALL option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 136 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 136. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection, will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that’s displaying all facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/137.png)

> <span id="_bookmark248" class="anchor"></span>Figure 136: Select Facilities Pop-Up Windows

3.  The default option for Consent Type is All Authorizations. If you want to select a specific Consent Type, click on the drop down arrow to choose from the list. The other two options are eHealth Exchange Authorizations, and SSA Authorizations.
4.  Use the Entered By dropdown to search this report by users who have entered a consent into the VAP application. For example, to view records using eBenefits, type eBenefits into the search box.
5.  ![](vap-version-1-user-guide/138.png)Select the date range criteria to generate the report. The options are Entry Date or Opt- In Date. The Entry Date is generated based on the system checking the corresponding transaction for that record for when the consent was entered into the system. The Opt-In Date is based on the date the consent was signed.
6.  Click the Search button to display the Opt-Detailed Report shown in Figure 137.
7.  Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. This field allows users to select by 10, 25, 50, 100, 250 and 500.
8.  If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
9.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order.
10. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> <span id="_bookmark249" class="anchor"></span>Figure 137: Opt-In Patients Detailed Report Screen

11. The report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Patient Middle Name, Consent Type, Entry Date, Opt-In Date, Expiration Date, Entered By, Authenticating Facility, and a View column.

#### Export the Opt-In Patient Detailed Report

12. Select the Export to Excel or Export to CSV option on the top-right side of the report section seen in Figure 137.
13. Unlike the summary reports, a privacy warning, Figure 138, is displayed prior to completing the export, as these detailed-level reports contain personally identifiable information.
14. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in

> ![](vap-version-1-user-guide/139.png)the exported Excel file.

> ![](vap-version-1-user-guide/140.png)

> <span id="_bookmark251" class="anchor"></span>Figure 138: Export Warning Message

### Expiring Consent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Expiring Consent Report provides a detailed listing of consents at selected range in days which were set in the Expiring Consent Notification, Section 4.9. The fields on the Expiring Consent Report query screen (Figure 139) allow you to set the number of records per page for the report and include/exclude test patients as well as filter on Authenticating Facility, Consent Type, and Entered By. It is important to note that the Expiring Consent Report is only for upcoming expirations and does not track historical expired patients (i.e. deceased, etc.).

#### Generate an Expiring Consent Report

1.  Click the Expiring Consent menu item under the Detailed Reports heading on the menu at the top of the screen to display the Expiring Consent Report query screen.

> <span id="_bookmark254" class="anchor"></span>Figure 139: Expiring Consent Report Query Screen

2.  The Start Date and End Date run as default within the range of the days which were set for the Days until Expiration of the Expiring Consent Notification, Figure 139.
3.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The ALL option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 140 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 140. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection, will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that’s displaying all facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/141.png)

> <span id="_bookmark255" class="anchor"></span>Figure 140: Select Facilities Pop-Up Window

4.  The default option for Consent Type is All Authorizations. If you want to select a specific Consent Type, click on the drop down arrow to choose from the list.
5.  ![](vap-version-1-user-guide/142.png)The default option for Entered By is All. If you want to select a specific Entered By, click on the drop down arrow to choose from the list.
6.  Click the Search button to display the Expiring Consent Report shown in Figure 141.
7.  Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. This field allows users to select by 10, 25, 50, 100, 250 and 500.
8.  If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
9.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order.
10. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.

> <span id="_bookmark256" class="anchor"></span>Figure 141: Expiring Consent Report Screen

11. The report displays the following fields for each listing: SSN, Patient Last Name, Patient First Name, Patient Middle Name, Opt-In Date, Expiration Date, Consent Type, Entered By, and Authenticating Facility.

#### Export the Expiring Consent Detailed Report

12. Select the Export to Excel or Export to CSV option on the top-right side of the report section seen in Figure 141.
13. Unlike the summary reports, a privacy warning, Figure 142, is displayed prior to completing the export, as these detailed-level reports contain personally identifiable information.
14. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it appears on the report.

> ![](vap-version-1-user-guide/143.png)![](vap-version-1-user-guide/144.png)Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> <span id="_bookmark258" class="anchor"></span>Figure 142: Export Warning Message

### Delayed Consent Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Delayed Consent Detailed Report, Figure 143, allows you to select one or multiple SSN’s, Last Name, First Name, Authenticating facilities(s), reason or reasons for delay, days since delayed, consent type, and patient types. This report provides a summary listing of the selected Delayed Consent totals at the selected Authenticating facility or facilities.

#### Generate a Delayed Consent Detailed Report

1.  Click the Delayed Consent menu item under Detailed Reports heading on the menu at the top of the screen to display the Delayed Consent Detailed Report query screen.

> <span id="_bookmark261" class="anchor"></span>Figure 143: Delayed Consent Detail Report

2.  Enter one or multiple SSNs, separated by comma, in the format \######### (no hyphens) in the SSN field. Do not enter a SSN in this field or names in the Last Name and First Name fields if you want to search for all patients in the context of the other parameters you enter.
3.  Enter a last name for one or more patients in the Last Name field. Leave the SSN and First Name fields blank if you want to search for patients with the same last name. Do not enter a last name in this field or a first name in the First Name field if you want to search for a patient based on his or her SSN.
4.  Enter a first name for one or more patients in the First Name field. Leave the SSN and Last Name fields blank if you want to search for patients with the same first name. Do

> not enter a first name in this field or a last name in the Last Name field if you want to search for a patient based on his or her SSN.

5.  Click the Select button at the right of Authenticating Facilities to select one or more facilities you want to display in the report. The default authenticating facility filter is set to the User Default Facility. This default can be changed by the user from the Set Default Facility menu item under the Welcome menu. The All option is the default setting, unless a default facility is selected. You must select the Select All button if you want the report to include all VA facilities.
    1.  A pop-up window will show displaying all VISNs, their associated facilities, and your selection in three (3) separate sections.
    2.  For each section, you may Select/Unselect all from the top right, as highlighted in Figure 144 below. The first and second columns are used to filter by VISN and Facilities. The third column to the right displays the selected VISNs and Facilities to be included within the resultant report.
    3.  The VISN column, to the left-hand side of the pop-up, displays all 21 VISNs stored within the VAP application. This column allows the user to filter and/unselect by VISNs.
    4.  The middle column, Facilities, shows a listing of all the facilities. By default, facilities in the middle section are grouped by VISN. This default can be changed if you uncheck the Display facilities grouped by VISN box, under the middle section, highlighted in Figure 144. Once unchecked, facilities will be listed in alphabetical order. If any VISNs, from the VISN column are unchecked, the Facilities list will update to remove these facilities from the view.
    5.  Once the selection is made and the first two columns, VISNs and Facilities, are filtered, the last column to the right, Your Selection, will display the resultant facilities associated with the filter selection from the other two boxes.
    6.  The other two checkboxes within this page are Include consents with unknown VISN, and Aggregate data at the facility level. By default, both are unchecked.
    7.  Click OK to confirm your selection and implement it in the search results.
    8.  Click Cancel on the bottom right to cancel your selection and go back to the previously selected filter option. Click Restore last selection to go back to the last selection of facilities used. For example, if the last selection you made only included VISN 1 facilities, clicking this button on a window that’s displaying all

> facilities will change the selection to show only VISN 1 facilities.

> ![](vap-version-1-user-guide/145.png)

> <span id="_bookmark262" class="anchor"></span>Figure 144: Select Facilities Pop-Up Window

6.  Check one or multiple of the reason(s) for delay checkboxes that you want to display in your Delayed Consent Detailed Report. By default, all reasons for delay will be displayed. Do not select a specific option if you want to see all reasons in the report.
7.  Click the arrow at the right of the Days Since Delayed list box to select the range of days, since the status have been delayed, you want to display in the report.
8.  Click the arrow at the right of the Consent Type list box to select the types of consent you want to display in the report. The default option for this list box is All, so do not select a specific option if you want to see all types of consent. There are two options in the list: eHealth Exchange Authorizations and SSA Authorizations. You can only select one entry from the list.
9.  Click the arrow at the right of the Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
10. Enter a name or User ID in the Entered By field to filter by either full or partial name of the entity associated with the transaction. This field can refer to either DVA User ID that entered a record (for example, "smith"), or a system that initiated a transaction (for example, "eBenefits"). Search on this field is case insensitive; that is, values of "smith" and "SMITH" will produce the same result set.
11. ![](vap-version-1-user-guide/146.png)Click the Search button to display the Delayed Consent Report shown in Figure 145.

> <span id="_bookmark263" class="anchor"></span>Figure 145: Delayed Consent Detail Report

12. Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. The All option has been removed for performance reasons. This field allows users to select by 10, 25, 50, 100, 250 and 500.
13. If more records are available than can be displayed on one screen, the Previous and Next buttons at the bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
14. Each individual column of the report can be sorted if the up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order.
15. The menu at the top of the screen is based on your role when you logged into the application. It allows you to select other options available to your role.
16. The report displays the following fields for each listing: Date Entered (CT), ICN, SSN, Patient Last Name, Patient First Name, Patient Middle Initial, Consent Type, Reason(s) for Delay, Entered By, Authenticating Facility, and Mailed Dates.

#### Export the Delayed Consent Detailed Report

17. Select the Export to Excel or Export to CSV option on the top right side of the report section seen in Figure 145.
18. Unlike the summary reports, a privacy warning, Figure 146, is displayed prior to the export completing, as these detailed-level reports contain personally identifiable information.
19. For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order as the generated report, and data in the exported file is sorted as it was on the report.

> Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel. The name of the file is generated in the following format: \[Report_Title\]\_\[Detail/Summary\]\_Report_YYYYMMDD_HHmmss.\[xls/csv\]

> ![](vap-version-1-user-guide/147.png)

> <span id="4.6.7._Patient_Discovery_Audit_Detailed4" class="anchor"></span>Figure 146: Export Warning Message

### Patient Discovery Audit Detailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fields in the Search Details box on the Patient Discovery Audit Report query screen (Figure 147) allow you to enter the SSN, First Name and Last Name, User ID, set a range of dates and times, select MPI results and Sending/Receiving organization (partner), and select whether to include/exclude test patients or obtain results by all patients. This report displays the records relating to the announcements sent to partners, responses from partners to eHealth Exchange (Match Found), or Check Policy records.

> A recent change to this report is the ability to filter the resultant report by hour/minute. Due to the increasing amount of data and the millions of records, this allows the user to fine-tune the results to obtain better counts on a daily basis. It is important to note that due to the immense quantity of data within this report (millions of records), searching for several weeks or months may take a few minutes to process.

#### Generate a Patient Discovery Audit Report

1.  Click the Patient Discovery Audit menu item under Detailed Reports heading on the menu at the top of the screen to display the Patient Discovery Audit Report query screen.
2.  Enter one or multiple SSNs, separated by comma, in the format \######### (no hyphens) in the SSN field. Do not enter a SSN in this field or names in the Last Name and First Name fields if you want to search for all patients in the context of the other parameters you enter.
3.  Enter a last name for one or more patients in the Last Name field. Leave the SSN and First Name fields blank if you want to search for patients with the same last name. Do not enter a last name in this field or a first name in the First Name field if you want to search for a patient based on his or her SSN.
4.  Enter a first name for one or more patients in the First Name field. Leave the SSN and Last Name fields blank if you want to search for patients with the same first name. Do not enter a first name in this field or a last name in the Last Name field if you want to search for a patient based on his or her SSN.
5.  Enter a user ID in the User ID field if you want to search for a specific user.
    1.  Note: Do not enter a User ID in this field if you want to search for all users.
6.  Enter the Start Date and Start Time, for the Patient Discovery Audit Report in the Start Date field in the format mm/dd/yyyy (e.g., 06/11/2014). You can also select the date from the date range picker dropdown. Select a starting time frame, using the Start Time

> ![](vap-version-1-user-guide/148.png)fields. Use the dropdowns to select the hours, minutes, and meridian. As a user, be mindful that the VAP application is hosted at the Austin Information Technology Center (AITC) and uses Central Standard Time (CST). If you are located in a different time zone and are looking for a particular announcement made by you, remember the time difference! Do not enter a date in this field or the End Date field if you want to search for all dates. However, searching for all dates is *strongly discouraged.* In one day, the VAP application can receive millions of records, so running by all dates may significantly affect the performance of the system.

> <span id="_bookmark268" class="anchor"></span>Figure 147: Patient Discovery Audit Report Query Screen

7.  Enter the end date and end time for the Patient Discovery Audit Report in the End Date field in the format mm/dd/yyyy (e.g., 06/25/2014). You can also select the date from the date range picker dropdown.
    1.  Note: Do not enter a date in this field or the Start Date field if you want to search for all dates.
8.  Enter the UserID, of a valid Veterans Affair user, within the free-text search, to filter the generated results by that particular UserID to
9.  Click the arrow at the right of the MPI Results list box to select the MPI results you want to display in the report. The default option for this list box is All, so do not select a specific result if you want to see all MPI results in the report. Other options in the list are Match Found and Match Failed. You can only select one entry from the list. If you select Match Failed you will be able to see a report containing only the failed matches and when they occurred.
10. Click the arrow at the right of the Sending Organization or Receiving Organization list box to select the results associated to the eHealth Exchange organization you want to display in the report. You can only select one entry from the list. The default option for this list box is All, so do not select a specific organization if you want to see all external eHealth Exchange organizations in the report. Users may filter the results in the report by only Sending Organization or Receiving Organization, but not both. This is due to the scope of the VAP system. VAP only tracks messages received from partners and disclosed to partners, therefore filtering from partner to partner, would not return results.
11. Click the arrow at the right of Patient Types list box to select the types of patients you want to display in the report. The default option for this list box is Real Patients, so do not select a specific option if you want to see real patients only. There are three options in the list: All (Real and Test Patients), Real Patients, and Test Patients.
12. ![](vap-version-1-user-guide/149.png)Click the Search button to display the Patient Discovery Audit Report as shown in Figure 148.
13. Click the Show Entries list box to select the number of records you want to display on each page of the search. The default option for this list box is 25. The field allows users to select by 10, 25, 50, 100, 250 and 500.
14. If more records are available than can be displayed on one screen, the Previous and Next buttons at the top and bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
15. Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order.

> <span id="_bookmark269" class="anchor"></span>Figure 148: Patient Discovery Audit Report Screen (Top)

![](vap-version-1-user-guide/150.png)

> <span id="_bookmark270" class="anchor"></span>Figure 149: Patient Discovery Audit Report Screen (Bottom) without Test Patients

![](vap-version-1-user-guide/151.png)

> <span id="_bookmark271" class="anchor"></span>Figure 150: Patient Discovery Audit Report Screen (Bottom) with Test Patients

> The report displays the following fields for each listing:

- Date Received
- SSN (or SSN Unknown for patients whose SSN cannot be established)
- Patient Last Name
- Patient First Name
- Patient Middle Name (The Middle Name column only displays if middle name is tracked in Exchange)
- Sender
- Sender OID (When exported to Excel or CSV, Figure 152)
- Purpose of Use (i.e., how the information disclosed will be used: Coverage (SSA), Emergency, and Treatment)
- Receiver
- Receiver OID (When exported to Excel or CSV, Figure 152)
- Message
- Explanation of Failure
- Details

> The bottom left of the report screen shows the real/test patient messages, real/test patient fails, real/test patient matches, and unique teal/test patients.

> The Details column displays the patient’s place of birth city and state, date of birth, mother’s maiden name, social security number, phone number, and address. The Details column also if there was a failure to announce patients (listed below). Announcement failure may occur due to one of the following reasons:

- Failure – Partner did not respond with Patient information
  - A response to the announce call was not received from the partner
- Failure – Outbound PD: Partner is not registered with the system
  - A partner is not registered with the system (Partner is not permitting patient discovery requests). Therefore, the announce was not sent out from eHealth Exchange to this partner.

> Patient Discovery Audit logging typically displays one row due to the fan-out functionality. eHealth Exchange records a row for every patient-partner announce transaction. Thus, if the announce was sent to five partners for one individual, five rows are displayed within the report. If there was a failure for either of the two reasons listed above – for example, two of the five announces failed – then two of the rows will show for which patient-partner the failures were recorded.

#### Export the Patient Discovery Audit Detailed Report

1.  Select the Export to Excel or Export to CSV option on the top-right side of the report section seen in Figure 148.
2.  Unlike the summary reports, a privacy warning is displayed prior to the export completing, as these detailed-level reports contain personally identifiable information.
3.  For Excel, report data is exported into a spreadsheet. For Excel format, the report name, current date, and all filtering criteria are exported as file headers.
    1.  Report data is exported with columns in the same order of columns as the generated report, and data in the exported file is sorted as it was on the report.

> ![](vap-version-1-user-guide/152.png)Note: The column headings are exported only when there are matching records. If the search did not generate any records, a “No records found” message is displayed in the report, as well as in the exported Excel file.

> <span id="_bookmark273" class="anchor"></span>Figure 151: Export Warning Message

> ![](vap-version-1-user-guide/153.png)Note: Not displayed within the VAP User Interface, and only in the Export, the VAP system displays Organization Identifier Code (OID), as highlighted in Figure 152.

> <span id="_bookmark274" class="anchor"></span>Figure 152: Exported Patient Discovery Audit Report Displaying OID (Excel)

### Scheduled Exports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Scheduled Exports provides a detailed listing of completed exports available for download. For exports that are under 1000 rows, the user will be prompted to download their report immediately; however, for reports that exceed the 1000 rows, the user will be prompted to navigate to Scheduled Exports for download, as seen in the export privacy warning message seen in Figure 153. Additional functionality has been added allowing Administrators to schedule exports to run in advance; the details of this functionality are documented within Section 4.8:

> ![](vap-version-1-user-guide/154.png)![](vap-version-1-user-guide/155.png)Advanced Scheduling. These report exports will also be displayed for download within the Scheduled Exports page.

> <span id="_bookmark276" class="anchor"></span>Figure 153: Export Warning Message (Reports Exceeding 1000 Rows)

1.  Click the Scheduled Exports menu item under Detailed Reports heading on the menu at the top of the screen to display the Scheduled Exports query screen. This page displays all of the scheduled or advanced scheduled exports. For each listing, the following fields are displayed: Report, Format, Date Generated (CT), Status, and Download.
2.  Click the Show Entries list box, shown in Figure 154, to select the number of records you want to display on each page of the search. The default option for this list box is 25.

> <span id="_bookmark277" class="anchor"></span>Figure 154: Scheduled Exports Report

3.  If more records are available than can be displayed on one screen, the Previous and Next buttons at the bottom right of the screens are activated. You can use these buttons to page back and forward through the list of records found by the search.
4.  Click the Refresh button on the top right on the report to refresh the results.
5.  Each individual column of the report can be sorted if up and down arrow icons appear below the column heading. Click the up arrow icon to sort the column by ascending order. Click the down arrow icon to sort the column by descending order.
6.  In Scheduled Exports, below the Show Entries dropdown, a Select All checkbox is visible. This checkbox allows the users to select all exported entries on the current page with one action. Once an export entry has been selected, the Download and the Remove buttons are activated/enabled.
7.  To download one or multiple files, use the checkboxes on the left side of the page. One or more exports must be selected in order to download files. If multiple files are selected,

> then the system will download all of these into one zip file. Click on the Download button to download the files. The browser will show the status of the download progress. Once these files are ready, the user can elect to either Save or Open.

8.  To delete one or multiple export rows from this report, also use the checkboxes on the left. One or more exports must be selected in order to delete. Click on the Remove button. Upon selecting the Remove button, a prompt will appear asking, “Are you sure you want to permanently remove this (1) export? This cannot be undone.” The user must confirm if they would like to remove these scheduled exported files from their queue to download. Once the user confirms, then the scheduled export files are removed. It is important to note if a user unintentionally removes a report, they can navigate again to the desired report and export it with the same criteria as before.

### Data Quality Export

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Data Quality (DQ) Export Detailed Report allows data analysts to efficiently access the raw XML clinical documents that are stored in the eHealth Exchange audit record. This is essential to a more efficient performance of data quality analysis on VA and Partner documents. The DQ Export Search page is broken into four (4) main parts (two of the four parts in shown in the figure below):

9.  Start and End Date parameters.
10. List of providers and/or organizations.
11. Selected providers and/or organizations.
12. Patient detail parameters.

![](vap-version-1-user-guide/156.png)

> <span id="_bookmark279" class="anchor"></span>Figure 155: Data Quality Export Search Screen

#### Begin a Data Quality Export

1.  Enter a Start Date using MM/DD/YYYY format in the Start Date field, or you may use the calendar to make your selection.
2.  Enter an End Date using MM/DD/YYYY format in the End Date field, or you may use the calendar to make your selection.
    1.  Note: Date fields are required to perform an export.
3.  Select the Providers or Organizations you wish to include in the export from the List of Providers and Organizations. If you are using a mouse or a mouse pad, you can make your selection by double clicking on the provider/organization name from the List of Providers and Organizations. Or, if you prefer to use keyboard strokes, you may use the up and down arrow keys to navigate to the desired providers/organizations and click Enter.
    1.  ![](vap-version-1-user-guide/157.png)![](vap-version-1-user-guide/158.png)![](vap-version-1-user-guide/159.png)Note*: *At least one (1) provider or organization is required to perform an export.

> <span id="_bookmark281" class="anchor"></span>Figure 156: Data Export Query Page

4.  Review your selected Providers and Organizations. To remove a selected provider/organization from the Selected list, if you are using a mouse pad or mouse, use the scroll bar to navigate to the desired provider/organization and double click to remove. If you prefer to use a key board, use the up and down keys to navigate to the desired provider/organization and press Enter to remove.
5.  If you wish to restrict the results to a single patient (optional), you may enter the patient’s Social Security Number (SSN) and name.
    1.  In the SSN field, enter the patient’s nine-digit SSN using format xxxxxxxx (no dashes).
    2.  In the Last Name field, enter the patient’s last name.
    3.  In the First Name field, enter the patient’s first name.
6.  Click the Generate button to start the download process.
7.  This action displays the File Download dialog box, which gives you the options to Open, Save, or Cancel the generated zip file.

> <span id="_bookmark282" class="anchor"></span>Figure 157: File Download Dialog Box

> *Generated Download dialog box options:*

1.  Open – When you select this option, Windows File Explorer opens and displays the zip folder that contains the organizations/providers selected in your query. You may move the zip folder to another location within your personal folder structure or you may extract all zip folder contents.
2.  Save – This option provides three additional choices:
    1.  Save – This option allows to save the zip folder to your default setting; selecting this option populates additional choices (displayed in the figure below)

> <span id="4.6.10._Data_Quality_Upload_Transmission" class="anchor"></span>Figure 158: Zip File Export Options

1.  Open – This option allows you to select Open, which opens Windows File Explorer
2.  Open With - Allows you to open the download with an application of your choice.
3.  View Downloads – Allows you to review all downloads you have performed from IE. When viewing downloads, you may choose Open or Open With (discussed above), or you may clear your download list.
2.  Save As – This option opens Windows File Explorer so you may choose a destination in which to store the file until a later time.
3.  Save and Open – This option saves the zip file in a temporary folder location and opens the temporary folder location.

### Data Quality Upload Transmission Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Data Quality (DQ) Transmission Log displays the data logged for the daily, clinical data file upload batch processing, performed by the Adapter Data Quality Services upload application.

> Batch processing consists of three events, which include:

1.  Uploading the individual XML file to Diameter Health.
2.  Packaging a copy of files sent to DQT in a zip file.
3.  Moving the completed zip file to a shared location for DQ team for consumption.

> ![](vap-version-1-user-guide/160.png)These data files consist of the clinical health data XML files which have been retrieved via the VA eHX Adapter application, both for inbound VA requests and disclosures to external health partners, are stored in the audit table in the eHX Adapter database.

> <span id="_bookmark285" class="anchor"></span>Figure 159: Data Quality Upload Transmission Log Search Criteria

#### Generate the Data Quality Upload Transmission Log Report

1.  Select an Event Type from the dropdown menu options. You may choose from:
    1.  All – Selecting this default value displays report results for all event types. value
    2.  DiameterHealth_Uploaddatafile – Selecting this option restricts report results to display only this event type.
    3.  DQZipFile_PackDataFileInside – Selecting this option restricts report results to display only this event type.
    4.  DQZipFile_MoveZipFileForPickup – Selecting this option restricts report results to display only this event type.
2.  Select a file transmission status from the dropdown menu options. You may select one of the following statuses:
    1.  All – When selecting this option, report results display failed and successful transmission events.
    2.  Success – Selecting this option restricts report results to display only this status.
    3.  Fail – Selecting this option restricts report results to display only this status.
3.  File Name – To restrict report results to a specific file, enter the name of the file.
4.  Start Date – Enter the date you want the report to begin with. Enter a date using the following format: mm/dd/yyyy, or you may make a selection using the calendar icon.
5.  End Date – Enter the date you want the report to end on. Enter a date using the following format: mm/dd/yyyy, or you may make a selection using the calendar icon.
6.  Once the desired criteria is entered, click the Search button to execute the report.

#### Data Quality Upload Transmission Log Results

> ![](vap-version-1-user-guide/161.png)Use the scroll bar to review report results.

> <span id="_bookmark288" class="anchor"></span>Figure 160: Data Quality Upload Transmission Log Report

> Below is a brief explanation of report fields:

- DQ Transmission ID – System generated file identifier; this identifier is generated so the same file identifier is not sent twice to Diameter Health
- Batch ID – System generated identifier used to identify all files included in a specific batch
- Event Type – Used to define the events that occurred with each file
- Start Time – Date/Time stamp of when the batch process began
- End Time – Date/Time stamp of when the batch process ended
- Host Name – The name of the environment/server that started and ended the batch process
- File Name – Standard filing naming conventions identify: provider_document type_date (yyyymmdd)\_Document Id\_unique index.file extension
- File Type – Identifies the type of file transmitted for each event
- File Size – Identifies the size of the file transmitted
- Destination – Identifies the destination of each file during each event
- Status – Identifies successful or failed file transmission
- Local Doc ID – Identifies the documents unique storage ID in the VA database
- Remote Doc ID – Identifies the documents unique storage ID in the Diameter Health database
- Error – Identifies the reason for failed file transmission for each event

#### Exporting the Data Quality Upload Transmission Log Report

> You may export this report to a csv or Excel file format. Follow the steps outlined below to export to either csv or Excel file format.

1.  Click Export to Excel.
    1.  Note: When exporting more than 1,000 rows of data, the system will generate an Export Notice (shown in the figure below), letting you know this report will be available to download from the Scheduled Exports page when complete.

> ![](vap-version-1-user-guide/162.png)

> ![](vap-version-1-user-guide/163.png)<span id="4.7._Viewing_the_User_Guide" class="anchor"></span>Figure 161: Export Notice

2.  Click the Export button to continue with the export, or Cancel to end the action.
3.  Navigate to Scheduled Exports.

> <span id="_bookmark291" class="anchor"></span>Figure 162: Scheduled Exports Screen

4.  From the Scheduled Exports screen, click the Download button for the report you wish to open.

> ![](vap-version-1-user-guide/164.png)

> <span id="_bookmark292" class="anchor"></span>Figure 163: Windows File Options

> Note*: *Windows displays options to Open, Save, or Cancel the export. If selecting Save, be sure to follow the prompts at the bottom of your screen.

> ![](vap-version-1-user-guide/165.png)The figure below shows an example of the exported Excel report.

> <span id="_bookmark293" class="anchor"></span>Figure 164: Data Quality Upload Transmission Log Excel Export

## Viewing the User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The User Guide (this document) for the current VAP application can be viewed by selecting the User Guide option on the menu at the top under the Welcome menu. This option displays the version stored in the VA Software Document Library (VDL).

> ![](vap-version-1-user-guide/166.png)

> <span id="4.7.1._View_the_User_Guide_for_the_Appli" class="anchor"></span>Figure 165: User Guide Option under Welcome Menu

### View the User Guide for the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to the Welcome menu.
2.  Click User Guide from the available options.

## Advanced Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Scheduled Exports were designed to assist the users to export large reports to Excel and CSV without having to stay on the same screen and wait for the report completion. In certain cases, users may want to schedule large exports during off-peak or weekend hours. To avoid the user having to initiate the scheduled export on off-hours, the advanced schedule functionality was created. This functionality is limited to Administrators. Users are able to navigate to any detailed report, with exception of the Data Quality Export report, and schedule a task to run an export.

> ![](vap-version-1-user-guide/167.png)For administrators, there is a button available labeled Schedule, as shown in Figure 166.

> <span id="_bookmark298" class="anchor"></span>Figure 166: Schedule Button on Detailed Reports (Example)

> Prior to selecting the Schedule button, use the search criteria form to fill out the desired search parameters for the scheduled task to use. All of the search criteria parameters, with the exception of dates, will be used to generate the export. After selecting the desired search parameters, select the Schedule button. A pop-up window displays, as shown in Figure 167. This window allows the user to set a task to run an advanced scheduled export for the report which the user is currently in. Administrators are able to set up to three recurring tasks within the system. After the

> ![](vap-version-1-user-guide/168.png)limit of three tasks has been set, the user must delete one of their recurring tasks to specify a new one.

> <span id="_bookmark299" class="anchor"></span>Figure 162: Advanced Schedule: Task Creation Pop-Up Model

> The Advanced Scheduling pop-up window displays the search parameters that were selected on the previous page and used to create the export. It is important to note that the date parameters are not included. The Advanced Scheduling tool will then pull in the selected parameters for use when the task runs. If any report has dates that can be specified, these parameters will not be brought in, as the reporting period is set in the task itself.

> The second portion of the Advanced Schedule pop-up, is the Task Name field. This field permits the use of alphanumeric characters, spaces, and hyphens. A user is restricted from creating task names longer than 255 characters.

> The third portion of advanced scheduling is selecting the reporting period. The reporting period option is used every time the task is run. This is used in place of start/end dates for the generated report. When selecting a reporting period, frequency should be taken into account. For example, it would not make sense to create a monthly report that runs on the first of the month and select a reporting period of “Yesterday.” The table below describes the options that can be selected for a reporting period.

> <span id="_bookmark300" class="anchor"></span>Table 3: VAP Advanced Scheduling Reporting Periods

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Advanced Scheduling Reporting Period</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Yesterday</td>
<td>This option sets the reporting period on the exported file, such that the start and end date for the prior day from when the scheduled report is included in the export. For example, if selecting to run the task daily, then the exported file will include all results for the prior day.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Advanced Scheduling Reporting Period</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Last Week</td>
<td>This option sets the reporting period on the exported file such that the start and end date are set to the entire prior week, for the complete week. For example, if selecting to run the task weekly on Friday, then the exported file will include all results from Sunday to Sunday of the prior week.</td>
</tr>
<tr class="even">
<td>Current Week</td>
<td>This option sets the reporting period on the exported file such that the start and end date are set to the run for the current week. For example, if selecting to run the task weekly on Friday, then the exported file will include all results from Sunday to Friday of the current week.</td>
</tr>
<tr class="odd">
<td>Last Month</td>
<td>This option sets the reporting period on the exported file such that the start and end date are set to the run for the entire prior month. For example, if selecting to run this report on a monthly basis for the last month, the exported file will include all results from the past completed month.</td>
</tr>
<tr class="even">
<td>Current Month</td>
<td>This option sets the reporting period on the exported file such that the start and end date are set to the run for the entire current month. For example, if selecting to run this report on a weekly basis for the current month, the exported file will include all results up to that date for the current month.</td>
</tr>
<tr class="odd">
<td>Current Quarter</td>
<td>This option sets the reporting period on the exported file such that the start and end date are set to the run for quarter including the date when the report is run. For example, if the report ran monthly and was run on the last day of February, it would return results from January 1<sup>st</sup> until the date of task run, as the task was run during the first quarter.</td>
</tr>
</tbody>
</table>

> Users are able to select the reporting period they desire, based on their reporting needs. It is important to note that if the data exceeds the Excel limitations for the number of records that can be obtained in an exported file, it may not complete. For Microsoft Excel 2016, a spread sheet may not exceed more than 1,048,576 rows by 16,384 columns. For these cases, it is recommended to export the report with a smaller reporting period.

> The next step is to specify the format for the exported report. Similarly to Scheduled exports, an Advanced Scheduling Task can return an export in either a CSV or Excel format. The user is required to fill the desired option through the user of radio buttons, as shown in Figure 167.

> After selecting a format, the user is required to select a frequency or recurrence setting for the advanced scheduled export task to run. An administrator is able to specify a task to run daily, weekly, or monthly. If the weekly option is chosen, a selection of how many weeks between occurrences and what day of the week to run the task on are required. For example, a user can specify a task to run weekly every two weeks. This would thereby specify the report to be exported every other week. If three weeks is selected, the task would run every three weeks. Users also have the ability to select monthly recurrences. If the monthly option is chosen, a selection of how many months between occurrences and what day of the month to run the task on are required. For example, the user can specify run on the first of the month, the 15<sup>th</sup> of the month or last day of the month.

> After selecting the frequency for the task to run, the user must specify an end date or timeframe for the task. The end date for an advanced scheduled task can be set to end after 1-30 occurrences or set to a specific date between the day after the Advanced Scheduled Task is created and six months from the date of that creation. This eliminates the system from running unnecessary tasks or tasks that are no longer used. From a system performance perspective, it is suggested that if a task is no longer needed, please delete; otherwise the tasks will continue to recur unnecessarily until the end date. After entering all of the criteria to set the advanced schedule task to recur, the user must select the Submit button, as shown previously in Figure 167.

> ![](vap-version-1-user-guide/169.png)The system will run all advanced scheduled tasks in the queue for a given day during the early morning. Tasks will begin to run at 2:00AM CST time. Once the task has ran, the export file will be available for download on the *Scheduled Exports* page. A user is able to view which task or tasks have been created by navigating under the user menu, as shown in Figure 167, to view their scheduled tasks, under Advanced Scheduling.

> <span id="_bookmark301" class="anchor"></span>Figure 168: Advanced Scheduling User Menu (Under Welcome VAP User)

> Upon navigating to the Advanced Scheduling page, the user will be able to see all of the tasks they have created, as shown in Figure 169. For each task, the task name, report type, format, date created, start date, end date, and frequency are shown. Since tasks are specific to a user, these tasks shown on that page are only visible to that specific user. To delete a task from the queue, the checkboxes can be used to select a task. Once a task is selected, the Remove button will be activated. The user must confirm to remove a task; once confirmed, it will be deleted.

> ![](vap-version-1-user-guide/170.png)

> <span id="4.9._Expiring_Consent_Notification" class="anchor"></span>Figure 169: View Advanced Scheduled Tasks

> To edit a task, the user is able to click on the Task Name, which is displayed with a hyperlink. Upon selecting the hyperlinked title, the Advanced Scheduling – Edit page is displayed, as shown in Figure 170.

![](vap-version-1-user-guide/171.png)

> <span id="_bookmark303" class="anchor"></span>Figure 170: Edit Advanced Scheduled Tasks

> This page will display the parameters and schedule options, including Task Name, Format, Frequency, and End Date. The user is able to modify any of these constraints to modify the advanced task. Select the Save button to confirm the modifications and update the task or the Cancel button to return to the prior page without modifying the task.

## Expiring Consent Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Expiring Consent Notification is the configuration mechanism for automatically running expiring consent reports of patients whose consent for participation in HIE is within a user- specified expiration window (i.e., 90 days) and can be sent to a distribution list.

### Schedule Expiring Consent Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click the Expiring Consent Notification menu item under the Welcome menu at the top of the screen to display the Expiring Consent Notification query screen (Figure 171).

3.  Set the Frequency (i.e. Daily, Weekly, Monthly).
4.  Set the Days Until Expiration (i.e., 5, 10, 15, 20, 30, or 90).
    1.  ![](vap-version-1-user-guide/172.png)![](vap-version-1-user-guide/173.png)Note: The date range of Expiring Consent Report, Section 4.6.5, will automatically set as default for Start Date and End Date within the range of the days (i.e., 90) which were set for the Days until Expiration.
5.  Set the Distribution List with one email address per line.
6.  Click on Save.

> <span id="_bookmark306" class="anchor"></span>Figure 171: Expiring Consent Notification Query Screen

> 4\. When Save is clicked, the user will receive an email notification in the appropriate time. The email contains a link that will take the user to the report with the previously identified date range Figure 172.

> <span id="_bookmark307" class="anchor"></span>Figure 172: VAP Expiring Consent Report Email

## Setting a Default Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setting a Default Facility allows users to designate a facility preference, which will be associated with the user for VAP Consent Management and VAP Reporting (Figure 173). There are several scenarios where users might want to set a default facility:

- A user might not have a designated default facility because the user ID is not associated with a site
- A user might have an ID which is not associated with any facility in VistA
- An automatic default facility is in place for a user ID associated with a site but the user wishes to change it to a different default facility
- ![](vap-version-1-user-guide/174.png)![](vap-version-1-user-guide/175.png)A manual default facility is in place, but the user wishes to change it

### Setting a Default Facility When No Default is in Place

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the top menu bar, click the Set Default Facility option under the Welcome menu (Figure 168).

> <span id="_bookmark310" class="anchor"></span>Figure 173: Set Default Facility Screen

2.  A message indicates that no default facility is currently set. This message occurs because the User ID does not correspond to a VistA facility and no manual facility has been established. Since default facility is set, the first facility listed in the VA Facility dropdown box is displayed.
3.  From the VA Facility dropdown list, select a new default facility.
4.  Click the Set Default Facility button to designate the selected facility as the default (Figure 173 and Figure 174).

> <span id="_bookmark311" class="anchor"></span>Figure 174: Set Default Facility – Manually Set

## Viewing Build Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The current build number for the application can be viewed by selecting the About VAP option on the menu at the top of any screen except the Login screen. This information also is displayed at the bottom of the Login screen (Figure 4).

### View Build Information for the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Click the About VAP menu item under the Welcome menu at the top of any screen to view the current build information for the VAP application. (Figure 165 shows the link on the Patient Search screen, but ROI Reporters will not see this screen. They see one of

> ![](vap-version-1-user-guide/176.png)the summary or detailed report screens.)

> ![](vap-version-1-user-guide/177.png)

> <span id="_bookmark314" class="anchor"></span>Figure 175: About VAP Option Under the Welcome Menu

6.  The Build Information screen (Figure 176) displays the message “The Current Version of VAP is: x.x.x.x”.
    1.  Note: In Production, these numbers will be followed by the VA Release convention. There is no other information on this screen.
7.  Select an option on the menu at the top of the screen to return to the application.

> <span id="_bookmark315" class="anchor"></span>Figure 176: About VAP Screen

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark318" class="anchor"></span>Table 4: VAP Error Messages with Causes and Resolutions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VAP Login Screen</td>
<td>User does not have permissions.</td>
<td>This is caused when the username, passed from SSOi, is not mapped to the VAP user access list.</td>
<td>If you have existing permissions, contact the Help Desk for support. If you do not have access yet, contact your local Community Care Coordinator to submit a request for access.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VAP Patient Search Screen</td>
<td><p>SSN is required.</p>
<p>Last Name is required.</p>
<p>First Name is required.</p></td>
<td><p>The SSN, Last Name, and First Name fields must be filled before pressing the <strong>Search</strong> button.</p>
<p>Any or all of these errors can occur depending on which fields were filled in and which were not.</p></td>
<td>The SSN, Last Name, and First Name fields must all be filled in before pressing the <strong>Search</strong> button.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>VAP Patient Search Screen</td>
<td>SSN is not valid.</td>
<td>The SSN field needs to contain nine (9) numeric characters. This error occurs if less than nine (9) numeric characters or any non-numeric characters are entered.</td>
<td>The SSN field must contain exactly nine (9) numeric and no other characters before pressing the <strong>Search</strong> button. (The Last Name and First Name fields must also be populated.)</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>VAP Patient Search Screen</td>
<td><p>Last Name is not valid.</p>
<p>First Name is not valid.</p></td>
<td><p>The Last Name and First Name fields must contain alphabetic characters only.</p>
<p>Some special characters, such as periods and apostrophes, are allowed. Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The Last Name and First Name fields must contain only alphabetic characters before pressing the <strong>Search</strong> button. (Some special characters are allowed, such as periods and apostrophes.)</td>
<td>The team needs to determine the entire list of special characters allowed.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Revoke eHealth Exchange Screen</td>
<td>Patient Signature Date must be after the date the authorization was signed.</td>
<td>This message occurs when you choose the “Revoked” option on the Revoke eHealth Exchange screen if the patient signature date entered is earlier than the date the authorization was originally signed.</td>
<td>The Patient Signature Date field on the Revoke eHealth Exchange screen must be filled with a date later than the date the authorization was originally signed if you choose "Revoked" as the reason.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Revoke or Terminate eHealth Exchange Organization Restriction Screen</td>
<td>Patient Signature Date must be after the date the authorization was signed.</td>
<td>This message occurs when you choose the “Revoked” option on the Revoke or Terminate eHealth Exchange Organization Restriction screen if the patient signature date entered is earlier than the date the restrictions were originally signed.</td>
<td>The Patient Signature Date field on the Revoke or Terminate eHealth Exchange Organization Restriction screen must be filled with a date later than the date the restrictions were originally signed if you choose "Revoked" as the reason.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Revoke SSA Screen</td>
<td>Patient Signature Date must be after the date the authorization was signed.</td>
<td>This message occurs when you choose the “Revoked” option on the Revoke SSA screen if the patient signature date entered is earlier than the date the authorization was originally signed.</td>
<td>The Patient Signature Date field on the Revoke SSA screen must be filled with a date later than the date the authorization was originally signed if you choose "Revoked" as the reason.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Batch Announce Patients Screen</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Batch Announce Patients Screen</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Batch Announce Patients Screen</td>
<td>Organization is required.</td>
<td>This message occurs when no organizations were moved to the "Organizations to whom you want to announce patients" box.</td>
<td>You must select at least one organization from the "All Organizations" list box to announce and move it to the "Organizations to whom you want to announce patients" list box.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Manage Batches Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Manage Batches Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Disclosures Summary Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Disclosures Summary Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Received eHealth Exchange Documents Summary Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Received eHealth Exchange Documents Summary Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Consent Directive Summary Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Consent Directive Summary Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Accounting of Disclosures Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Accounting of Disclosures Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accounting of Disclosures Report Screen (Search)</td>
<td>SSN is not valid.</td>
<td>The SSN field needs to contain nine (9) numeric characters. This error occurs if less than nine (9) numeric characters or any non-numeric characters are entered.</td>
<td>The SSN field must contain exactly nine (9) numeric and no other characters before pressing the <strong>Search</strong> button. (The Last Name and First Name fields must also be filled.)</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Received eHealth Exchange Documents Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Received eHealth Exchange Documents Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Received eHealth Exchange Documents Report Screen (Search)</td>
<td>SSN is not valid.</td>
<td>The SSN field needs to contain nine (9) numeric characters. This error occurs if less than nine (9) numeric characters or any non-numeric characters are entered.</td>
<td>The SSN field must contain exactly nine (9) numeric and no other characters before pressing the <strong>Search</strong> button. (The Last Name and First Name fields must also be filled.)</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Consent Directive Detailed Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Consent Directive Detailed Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>User Interface</strong></p>
</blockquote></th>
<th><strong>Error</strong></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Consent Directive Detailed Report Screen (Search)</td>
<td>SSN is not valid.</td>
<td>The SSN field needs to contain nine (9) numeric characters. This error occurs if less than nine (9) numeric characters or any non-numeric characters are entered.</td>
<td>The SSN field must contain exactly nine (9) numeric and no other characters before pressing the <strong>Search</strong> button. (The Last Name and First Name fields must also be filled.)</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Patient Discovery Audit Report Screen (Search)</td>
<td>End Date must be a later date than Start Date.</td>
<td>This message occurs when the start date entered is later than the end date entered.</td>
<td>The start date entered must occur before the end date entered or be the same date as the end date.</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Patient Discovery Audit Report Screen (Search)</td>
<td><p>Start Date is not a valid date.</p>
<p>End Date is not a valid date.</p></td>
<td><p>This message occurs when the dates entered in the Start Date and/or End Date fields are not valid dates or are not in the proper format (mm/dd/yyyy).</p>
<p>Either or both of these errors can occur depending on which fields were filled incorrectly.</p></td>
<td>The start and end dates entered must be valid dates and must be in the format: mm/dd/yyyy.</td>
<td>N/A</td>
</tr>
</tbody>
</table>

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below lists the acronyms used in this User Guide.

> <span id="7._Appendix" class="anchor"></span>Table 5: Acronyms

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>508</td>
<td>Section 508 Accessibility</td>
</tr>
<tr class="even">
<td>AITC</td>
<td>Austin Information Technology Center</td>
</tr>
<tr class="odd">
<td>CSV</td>
<td>Comma-Separated Values</td>
</tr>
<tr class="even">
<td>DoD</td>
<td>Department of Defense</td>
</tr>
<tr class="odd">
<td>ESR</td>
<td>Enrollment System Redesign</td>
</tr>
<tr class="even">
<td>HC IdM</td>
<td>Healthcare Identity Management</td>
</tr>
<tr class="odd">
<td>HIE</td>
<td>Health Information Exchange</td>
</tr>
<tr class="even">
<td>HITSP</td>
<td>Healthcare Information Technology Standards Panel</td>
</tr>
<tr class="odd">
<td>ICN</td>
<td>Integration Control Number (VistA)</td>
</tr>
<tr class="even">
<td>ID</td>
<td>Identifier or Identification</td>
</tr>
<tr class="odd">
<td>MVI</td>
<td>Master Veteran Index</td>
</tr>
<tr class="even">
<td>PDF</td>
<td>Portable Document Format</td>
</tr>
<tr class="odd">
<td>PII</td>
<td>Personally Identifiable Information</td>
</tr>
<tr class="even">
<td>POC</td>
<td>Point of Contact</td>
</tr>
<tr class="odd">
<td>ROI</td>
<td>Release of Information</td>
</tr>
<tr class="even">
<td>SSA</td>
<td>Social Security Administration</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="even">
<td>TSPR</td>
<td>Technical Service Project Repository</td>
</tr>
<tr class="odd">
<td>UG</td>
<td>User Guide</td>
</tr>
<tr class="even">
<td>UI</td>
<td>User Interface</td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Uniform Resource Locator</td>
</tr>
<tr class="even">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>VAP</td>
<td>Veterans Authorizations and Preferences</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="even">
<td>VLER</td>
<td>Virtual Lifetime Electronic Record</td>
</tr>
<tr class="odd">
<td>WWW</td>
<td>World Wide Web</td>
</tr>
<tr class="even">
<td>XML</td>
<td>Extensible Markup Language</td>
</tr>
</tbody>
</table>

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A: Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below lists definitions for terms used in this User Guide.

> <span id="_bookmark323" class="anchor"></span>Table 6: Definitions

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Authorized</td>
<td>The patient has expressed authorization for inclusion in the health information exchange and allowed all of his or her data to be shared.</td>
</tr>
<tr class="even">
<td>Clinician</td>
<td>Clinicians interact with the VAP system indirectly through the eHealth Exchange Gateway and Adapter applications when requesting information for a Veteran who has authorized record sharing. When the clinician (or clinical system) makes a request for information through the VA eHealth Exchange Gateway, an inquiry is made to the VAP to determine whether the request should be fulfilled or denied. If the request is fulfilled, a report containing the patient’s health summary data is returned to the clinical system (and the clinician).</td>
</tr>
<tr class="odd">
<td>Consent Directive</td>
<td>A Consent Directive as the record of a healthcare consumer’s privacy policy that grants or withholds consent for one or more principals (identified entity or role) performing one or more operations (e.g., access, amend, collect, delete, disclose, or use) for purposes, such as health status evaluation by third parties, operations, payment, public health, quality measures, research, treatment; or marketing or under certain conditions (e.g., unconscious a specified time period or in an emergency).</td>
</tr>
<tr class="even">
<td>Release of Information (ROI)</td>
<td>ROI is the disclosure of individually-identifiable health information to carry out treatment, payment, or health care operations.</td>
</tr>
<tr class="odd">
<td>Restricted</td>
<td>The patient has expressed authorization for provider or organizational exclusions in the health data to be shared.</td>
</tr>
<tr class="even">
<td>Revoked</td>
<td>The patient has elected, either by not submitting a required authorization or by revoking a previously submitted authorization, not to participate in the health information exchange.</td>
</tr>
<tr class="odd">
<td>ROI Administrator</td>
<td>ROI Administrators use the VAP system through a Web portal to support administration of user access and roles within the system. The Administrators generate Batch Announcements in addition to all tasks supported by the ROI Operator and ROI Reporter roles. These users see the Patient Search screen when they log into the application.</td>
</tr>
<tr class="even">
<td>ROI Operator</td>
<td>ROI Operators use the VAP system through a Web portal to support searching for patients and authorizing, restricting, or revoking sharing of patient health record data with the network of partners and communities participating in the eHealth Exchange in addition to all tasks supported by the ROI Reporter role. These users see the Patient Search screen when they log into the application.</td>
</tr>
<tr class="odd">
<td>ROI Reporter</td>
<td>ROI Reporters use the VAP system through a Web portal to run detailed and summary reports. These users see the Consent Directive Summary Report screen when they log into the application.</td>
</tr>
<tr class="even">
<td>ROI Tester</td>
<td>ROI Testers use the VAP system through a Web portal to view the XML code and perform other functions required for testing in addition to all tasks supported by the ROI Administrator, ROI Operator, and ROI Reporter roles. This role is only available to the developers and select VA personnel and other authorized users who do testing. These users see the Patient Search screen when they log into the application.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Section 508 Accessibility</td>
<td>Section 508 of the Rehabilitation Act of 1973, as amended (29 U.S.C. 794d) requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, Federal employees with disabilities have access to and use of information and data that is comparable to the access and use by Federal employees who are not individuals with disabilities, unless an undue burden would be imposed on the agency. Section 508 also requires that individuals with disabilities, who are members of the public seeking information or services from a Federal agency, have access to and use of information and data that is comparable to that provided to the public who are not individuals with disabilities, unless an undue burden would be imposed on the agency.</td>
</tr>
<tr class="even">
<td>Veteran</td>
<td>Veterans interact with the VAP system through the eBenefits portal. The portal allows them to electronically file a Consent Directive to share their VA data with the partners and communities participating in the eHealth Exchange. The portal allows the Veterans to control when their data is shared and with which communities or partners their data is shared.</td>
</tr>
</tbody>
</table>

## Appendix B: Changing the File Type Associated with a Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a report does not display properly when the link is clicked, you may need to modify the program associated with opening the .txt file.

1.  From the Start button, click My Computer.
2.  Select Tools and click Folder Options (Figure 177).

> ![](vap-version-1-user-guide/178.png)

> <span id="_bookmark325" class="anchor"></span>Figure 177: Folder Options

3.  Click on the File Types tab and scroll down to the file type extension details to change, in this case TXT (Figure 178).

> ![](vap-version-1-user-guide/179.png)

4.  <span id="_bookmark326" class="anchor"></span>Click the Change button.

> Figure 178: File Types

5.  In the Open With window click Notepad or WordPad (Figure 179).

> ![](vap-version-1-user-guide/180.png)

> <span id="_bookmark327" class="anchor"></span>Figure 179: Open With Dialog Box

6.  Make sure to check the box for Always use the selected program to open this kind of file, then click OK.

## Appendix C: Batch Announce

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Announcements are notifications for exchanging Veteran Identifier information with partner systems thereby facilitating subsequent health-information exchange between VA and its partners. These identifiers once exchanged are also termed correlations.

> The key actors involved with announcements are:

- VA’s CONNECT Gateway/ eHealth Exchange Adapter – Handles all messaging and communication pertinent to announcements.
- MVI – A VA repository that reconciles multiple identifiers for a patient including, VistA facility level identifiers and partner correlations, with an enterprise-wide unique identifier. The eHealth Exchange Adapter collaborates with the MVI during announcements.
- VAP – Provisions a GUI capability for VA staff to initiate announcements

> Note: The announcements are not actually performed by VAP. VAP captures announcement subject (patient) and target (partner) information and defers to the eHealth Exchange Adapter to carry out the announcement.

- Partner Systems – Front-ended by the CONNECT Gateway/equivalent thereof; these systems share their identifiers for the patient with the VA if certain demographic traits match across the two systems

> Announcements may be:

- Patient-Centric – Announcements to all organizations for a given patient
- Organization-Centric – Announcements for all opted-in patients to one or more organization(s)

> Batch announcements are organization-centric announcements. They are high volume announcements and are performed infrequently. The main drivers for batch announcements are scenarios such as those listed below:

- A partner has recently on-boarded with the VA and correlations needs to be established for the first time
- VA and/or its partners has modified Veteran identifiers and they need to be re-correlated

### Challenges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The complexity of batch announcements stems from a dependency on a multitude of systems and a high magnitude of volume, presenting the following challenges:

- Announcements could span numerous days and weeks
- Availability of all the dependent systems for the entire duration of the announcements needs to be ensured
- Maintenance patches, system upgrades on one or more of the dependent systems need to be factored in
- Existing restrictions on when announcements can be performed. For example, MVI stipulates that high volume batch announcements can only be performed during off-hours and weekends

### Batch Announce Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To overcome challenges described above, the following steps should be performed:

1.  Perform analysis to determine the scope of the announcements, split them across multiple batches, and establish a schedule for these batches.
2.  Coordinate with all stakeholders and dependent systems based on the schedule, modifications to the schedule if needed, and eventual execution of the batches.

#### Analysis

> Scope of the announcements needs to be determined. The following questions could help establish the scope:

- To how many partners are the announcements targeted?
- How many opted-in patients are being announced?
  - Should all opted-in patients be announced?
- Should all patients opted-in within a certain time frame be announced?

> Answers to these questions can be provided by the Business via a Service Request submitted to the eHealth Exchange Adapter/Legacy VAP team (see Section 7.3.2.2).

> Once the scope is determined, the candidate patients for announcement are distributed across numerous batches based on opt-in date ranges for those patients, thereby establishing a submission schedule. Important considerations for sizing a batch are the following:

- Batches cannot run beyond stipulated durations
  - MVI has off-hour batch announce execution stipulations

> Due to recent performance issues between eHealth Exchange, JLV, VAP and partner systems it is not recommended to include more than 32 patients a time. A system configuration was set in place to limit the number of announces that can take place, and this will be adjusted to increase the limit as the hardware and software infrastructure for these applications is increased over the coming weeks.

#### Coordination and Execution

> These are to be performed by Business, IdM, eHealth Exchange Adapter/Legacy VAP, and Partner Integration.

> Business roles and responsibilities:

1.  Submit a Service Request (SR) to the IdM team requesting that they manually de- correlate the Correlations within the MVI. De-correlation may or may not be required, but coordination with the MVI is still required with details about the announcements – scope, duration et.al.
2.  \*Email the VA EPMO with the information listed below.
    1.  Full Name of Partner
    2.  Partner OID
    3.  Date Authorizations (Opt-Ins) began that resulted in correlations with that Partner
    4.  List of Date ranges and number of patients opted in
    5.  Date Announces can start (Partner systems available)
    6.  Expected number of correlations.

> \*Note: Use this step until a formal Service Request (SR) process is in place.

> IdM roles and responsibilities:

1.  Go through the approval process with the SR received from Business.
2.  Develop a script to unlink the correlations (if applicable).
3.  Schedule the date/time on the AITC Calendar for running the script.
4.  Run the script.
5.  Notify the Business when completed. Product Development Team:

> 1\. Submit a Help Desk Request by calling the National Service Desk 1-888-596-4357. eHealth Exchange Adapter/Legacy VAP:

1.  Perform analysis.
2.  Create a schedule/plan.
3.  Run batches in the Production system.
4.  Monitor all batches for Announce errors.
5.  Validate and document successes and errors.
6.  Evaluate and document correlation count.
7.  Validate correlations count against expected correlation count.
8.  Provide a report of the batch announce results to the business.

### Story Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Event: Batch Announce (Figure 180)
- ![](vap-version-1-user-guide/181.png)Actor: eHealth Exchange Adapter/Legacy VAP Team

> <span id="_bookmark334" class="anchor"></span>Figure 180: Batch Announce Use Case Diagram

### Conversation/Narrative

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Business will email the VA EPMO with a table provided as a rough indicator as to the scope of the batch announcements. The table will indicate the number of patients that were opted-in for the site in question and the date ranges of opt-ins. Each line item could perhaps constitute a batch.

> Then VAP team can utilize the Consent Directive Summary Report and evaluate the number of opt-ins for the business-specified date ranges. If the number of opt-ins is large, the likelihood of the batch executing for a long time is very high. It must then be determined if the batches need to be split up further to satisfy stipulated execution time constraints (for instance, by MVI).

> Note: The Consent Directive report does not show counts of opt-ins grouped by the patient’s preferred facility (as provided by the business). Instead, it shows a count of patients (potentially

> ![](vap-version-1-user-guide/182.png)![](vap-version-1-user-guide/183.png)belonging to other facilities as well) opted-in by various facilities. In other words, the summary reports generated by entering in the Business-provided date ranges will not necessarily reflect counts identical to what the Business provided; however, it helps with sizing the batch.

> In summary, to establish a schedule of batches, the eHealth Exchange Adapter/Legacy VAP team should:

- Start with the information provided by the Business
- Establish scope of announcements using the Consent Directive Report

### Analysis Steps and Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into the Legacy VAP system.
2.  Access the Consent Directive Summary Report (Figure 181).
    1.  Enter an end-date (date specified by the business in a table, as part of the SR): for example 01/05/2018.

> <span id="_bookmark337" class="anchor"></span>Figure 181: Example of a Consent Directive Summary Report Search Criteria Screen

3.  Generate the CD report by clicking the Search button.

> <span id="_bookmark338" class="anchor"></span>Figure 182: Example of a Consent Directive Summary Report Screen

4.  The generated report shows the patients opted-in during this duration.
5.  Pick the next row from the Business-specified table, i.e., date range and repeat the steps until all the rows in the business specified table are accounted for.
6.  Once the announcements are tabulated, they can be submitted per schedule and the results are tabulated as shown.
7.  Based on the approved schedule of announcements, complete the Batch Announces and verify results generated show the number of patient announced and correlated.
8.  Provide the Business with a report of the findings.

### Acceptance Criteria/Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Acceptance criteria will be a table of batches that will be performed to announce the patients in the specified date range for the site in question.

> The batches are performed according to the approved schedule and demonstrate the number of patients correlated in the date range. A report of the findings will be delivered to the Business.

## Appendix D: Tool Tips and User Friendly Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Tool Tips (Hover Overs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VAP provides tooltips throughout the system entry fields and reports. The user hovers the pointer over an item and a tooltip may appear. A tooltip is a small hover pop-up box that appears on screen containing information regarding the field hovered over. Figure 183 through Figure 186 display a number of screenshots taken from the Disclosures Summary Report tooltips.

> Tooltips across the application have been modified for Section 508 compliance. These were revised to ensure that any assistive technology or screen readers used on the VAP application pages can read the tooltip prompts and provide the same information to visually-impaired users using the VAP application as the prompts provide to sighted users.

![](vap-version-1-user-guide/184.png)

> <span id="_bookmark342" class="anchor"></span>Figure 183: Tooltip (Hover Over) - Start/End Date

> When the user hovers over Start Date or End Date (Figure 183), a tooltip appears with the following message, “Enter the date in MM/DD/YYY format. Do not enter date in ‘Start Date’ or ‘End Date’ field to search for all dates.”

> ![](vap-version-1-user-guide/185.png)

> ![](vap-version-1-user-guide/186.png)<span id="_bookmark343" class="anchor"></span>Figure 184: Tooltip (Hover Over) – Patient Preferred Facility

> <span id="_bookmark344" class="anchor"></span>Figure 185: Tooltip (Hover Over) – Patient Preferred Facility Station ID

> ![](vap-version-1-user-guide/187.png)Tooltips are also provided with report headers. In Figure 185, the column header Patient Preferred Facility Station ID is hovered over as a box appears with the following message, “This column displays the facility ID of the preferred facility.”

> <span id="7.4.2._User_Friendly_Error_Messages" class="anchor"></span>Figure 186: Tooltip (Hover Over) – SSN

> The system provides tooltips for reports. This includes filter/search entry pages and report headers.

### User Friendly Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vap-version-1-user-guide/188.png)The VAP application provides error-message handling for display of user friendly errors. Instead of seeing code errors a standard error message is displayed to the user. For example, an error could be displayed when system connection is unavailable or when system timeout occurs. Error messages may appear when a connection with eHealth Exchange, Master Veterans Index (MVI), or Direct is unavailable. If this error is repeatedly seen, please call the VA Help Desk for assistance. These errors can also be seen for when a page does not exist.

> <span id="_bookmark347" class="anchor"></span>Figure 187: Error Message