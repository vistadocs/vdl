---
title: EDIS Technical Manual (file name contains _r)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: EDIS  (file name contains _r)
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.2
patch_id: EDIS*2.2
group_key: "EDIS:EDIS:2.2"
file_numbers: 
  - 230
security_keys: []
menu_options: 7
description: "--- title: | <span id=\\"_Toc495855387\\" class=\\"anchor\\"></span>Emergency Department Integration Software (EDIS)"
audience: 
keywords: 
  - class
  - table
  - edis
  - span
  - width
  - style
  - even
  - blockquote
  - patient
  - board
page_count: 0
word_count: 25221
section_count: 27
table_count: 11
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_2_tm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_2_tm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Emergency Department Integration Software (EDIS)

  Technical Manual
---

![](edis-technical-manual-file-name-contains-r/001.png)

Revised June 2021Department of Veterans Affairs (VA)Office of Information and Technology (OIT)

> Revision History

<table>
<caption><p><span id="_Toc54254120" class="anchor"></span>Table 1: Optimal Viewing Requirements</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 53%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/17/2021</td>
<td>3.1</td>
<td><p>EDP*2.0*15:</p>
<p>Added the routine EDP15P in section 4.1, EDIS Routines</p>
<p>Added checksums for routine EDP15P in section 4.2, EDIS Checksums</p>
<p>Removed the routine EDP22PST in Table 3: EDIS Routine Checksums</p>
<p>Updated the Document Conventions section</p>
<p>Moved and updated the EDIS Big Boards section</p>
<p>Updated the EDIS in Production Accounts section</p>
<p>Added EDIS Baseline reference material to the Secure Sockets Layer section</p>
<p>Added the PIV Provisioning section</p>
<p>Added the Big Boards section</p>
<p>Added the Note for the EDPF TRACKING MENU SIGNIN option</p>
<p>Added the Note for the EDPF TRACKING MENU TRIAGE option</p>
<p>Removed the options EDPF TRACKING MENU SIGNIN and EDPF TRACKING MENU TRIAGE from section 7.2 Include EDIS Options in Users Menu Trees</p>
<p>Added the Note for the EDPF WORKSHEETS Security Key</p>
<p>Added the Note for the EDPR ADHOC Security Key</p>
<p>Updated the Title page, Revision History, Table of Contents, List of Tables, and Footers</p>
<p>See the non-redacted EDIS_2_2_TM on the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>12/21/2020</td>
<td>3.0</td>
<td><p>EDP*2.0*13:</p>
<p>Updated document for GUI version 2.2.41</p>
<p>Removed the <strong>Index</strong> since it was improperly created by manual construction</p>
<p>Updated 508 Note</p>
<p>Updated the link location for the reference documents</p>
<p>Updated the file listings in the documents table</p>
<p>Updated Figure 1</p>
<p>Updated the SSQj information</p>
<p>Updated the production account URLs</p>
<p>Updated the EDIS Routines</p>
<p>Updated the EDIS Checksums</p>
<p>Updated Title Page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>5/2018</td>
<td>2.11</td>
<td><p>Patch EDP*2.0*9</p>
<p>Updated the Discharge Diagnosis Files</p>
<p>Removed reference of $$ICDONE^LEXU and corrected ICD9 CODE to remove the 9</p>
<p>Updated title page and footers.</p></td>
<td>HPS Clinical Sustainment Team</td>
</tr>
<tr class="even">
<td>11/2014</td>
<td>2.10</td>
<td><p>Patch EDP*2.0*2, GUI 2.1.2:</p>
<p>Updated title page, headers, and footers.</p>
<p>Corrected table formatting throughout document.</p>
<p>Reformatted all headings to replace manual Table of Contents with automated one.</p>
<p>Added alt text to Figure 1.</p>
<p>Updated Sections 1.3 and 1.4 for EDIS v.2.1.2/EDP*2.0*2.</p>
<p>Updated EDIS URLs in Section 2.1.3 (new URLs for EDIS v.2.1.2/EDP*2.0*2).</p>
<p>Updated Section 4 Routines for EDIS v.2.1.2/EDP*2.0*2.</p>
<p>Removed Provider Report: Deleted EDPRPT6 from Section 4.1 EDIS Routines and from Index; Deleted EDPR PROVIDER Security Key from Section 8.3 and from Index.</p>
<p>Corrected description for CPE Role (#232.5), Field .03 XML ABBREVIATION, in Table 26.</p>
<p>Added notes to Sections 3.1, 7.1, 8.3, 9.1, and 10.1 about EDPF BIGBOARD KIOSKS option/parameter/list template no longer being used as of EDIS v.2.1.1/EDP*2.0*6.</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>August 2014</td>
<td>2.9</td>
<td><p>Patch EDP*2*2, GUI 2.1.1-ICD-10</p>
<p>Added information on EDPLEX routine (p. 12)</p>
<p>Updated to ICD-10 reference (p. 13)</p>
<p>Added and updated routine names and checksums (p.16).</p>
<p>Updated to reference ICD-10 codes and text in the Discharge Diagnosis Files (p. 30)</p>
<p>Updated to reference ICD-10 codes and text in the Tracking Area File (p. 47)</p></td>
<td><mark>REDACTED</mark>,<br />
<mark>REDACTED</mark>,<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/17/2013</td>
<td>2.8</td>
<td>Update to remove zip reference</td>
<td>ProdDev</td>
</tr>
<tr class="odd">
<td>07/10/2013</td>
<td>2.7</td>
<td>Updated checksum value for EDPLOGA.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/10/2013</td>
<td>2.7</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/20/2013</td>
<td>2.6</td>
<td>Incorporate Product Support updates</td>
<td>Prod Development</td>
</tr>
<tr class="even">
<td>06/20/2013</td>
<td>2.6</td>
<td>Updated footer , TOC, and addressed text styles for 508 compliance</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/12/2013</td>
<td>2.5</td>
<td>Final review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/11/2013</td>
<td>2.5</td>
<td>Updated cover page.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/10/2013</td>
<td>2.5</td>
<td>Additional technical reviews</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/20/2013</td>
<td>2.4</td>
<td>Updated URLs</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/14/2013</td>
<td>2.3</td>
<td>Incorporate Product Support Feedback</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/10/13</td>
<td>2.2</td>
<td>Edited file to reflect changes from a patch to a host file.</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark> &amp; <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/04/2013</td>
<td>2.1</td>
<td>Final review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/03/2013</td>
<td>2.1</td>
<td>Addressed Product Support Feedback</td>
<td>EDIS Team</td>
</tr>
<tr class="odd">
<td>11/30/2012</td>
<td>2.0</td>
<td>Final review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/29/2012</td>
<td>2.0</td>
<td>Updated footer</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/30/2012</td>
<td>1.9</td>
<td>Made updates (incorporated edits from [T.S.])</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/26/2012</td>
<td>1.8</td>
<td>Updated links within document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/28/2012</td>
<td>1.7</td>
<td>Additional technical reviews</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark> &amp; <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/05/2012</td>
<td>1.6</td>
<td>Final review prior</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/04/2012</td>
<td>1.6</td>
<td>Review &amp; edits</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/30/2012</td>
<td>1.6</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/22/2012</td>
<td>1.5</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/22/2012</td>
<td>1.5</td>
<td>Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/21/2012</td>
<td>1.4</td>
<td>Final Review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/15/2012</td>
<td>1.4</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/15/2012</td>
<td>1.4</td>
<td>Review</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/04/2012</td>
<td>1.3</td>
<td>Final review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/03/2012</td>
<td>1.3</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/01/2012</td>
<td>1.3</td>
<td>Technical edits and additions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/11/2012</td>
<td>1.2</td>
<td>Final review prior to submission</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/08/2012</td>
<td>1.2</td>
<td>Technical Edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/07/2012</td>
<td>1.1</td>
<td>Technical Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/06/2012</td>
<td>1.0</td>
<td>Draft</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc54254120" class="anchor"></span>Table 1: Optimal Viewing Requirements

Table of Contents

1\. Product Description [6](#_Toc402873895)

1.1. About this Guide [6](#_TOC_250052)

1.2. Section 508 of the Rehabilitation Act of 1973 [6](#section-508-of-the-rehabilitation-act-of-1973)

1.3. Document Conventions [6](#document-conventions)

2\. General Information [7](#general-information)

2.1. Architectural Scope [7](#architectural-scope)

2.1.1. Web Application [7](#_TOC_250047)

2.1.2. URLs [7](#urls)

2.1.3. EDIS Big Boards [8](#edis-big-boards)

2.2. System Performance [9](#system-performance)

2.2.1. Scaling Guide: Memory and Central Processing Unit (CPU) [9](#scaling-guide-memory-and-central-processing-unit-cpu)

2.2.2. Disk Space [9](#disk-space)

3\. Parameters [9](#parameters)

3.1. EDIS (EDPF) Parameters [9](#edis-edpf-parameters)

3.1.1. Setting Up Synchronization with Patient Care Encounters [11](#setting-up-synchronization-with-patient-care-encounters)

4\. Routines [13](#routines)

4.1. EDIS Routines [13](#edis-routines)

4.2. EDIS Checksums [17](#edis-checksums)

5\. Files and Globals [21](#files-and-globals)

5.1. Globals [21](#globals)

5.2. Files [22](#files)

5.2.1. File Descriptions [22](#file-descriptions)

6\. Exported Remote Procedure Calls [64](#exported-remote-procedure-calls)

6.1. EDIS Remote Procedure Calls [64](#edis-remote-procedure-calls)

6.1.1. EDPCBRD RPC [64](#edpcbrd-rpc)

6.1.2. EDPCTRL RPC [64](#edpctrl-rpc)

6.1.3. EDPGLOB RPC [64](#edpglob-rpc)

7\. Exported Options [65](#exported-options)

7.1. EDIS Options [65](#edis-options)

7.2. Include EDIS Options in Users’ Menu Trees [67](#include-edis-options-in-users-menu-trees)

7.2.1. Assign EDIS Views to Users [67](#assign-edis-views-to-users)

8\. Security [69](#security)

8.1. IAM Single Sign-On Internal (SSOi) and VistA Integration Adapter (VIA) [69](#iam-single-sign-on-internal-ssoi-and-vista-integration-adapter-via)

8.2. Secure Sockets Layer [69](#secure-sockets-layer)

8.2.1. PKI Encryption Basics [69](#pki-encryption-basics)

8.3. Security Keys [70](#security-keys)

*8.3.1.EDPF KIOSKS* [70](#edpf-kiosks)

8.3.2. EDPR EXPORT [70](#edpr-export)

8.3.3. EDPF WORKSHEETS [70](#edpf-worksheets)

8.3.4. EDPR ADHOC [70](#edpr-adhoc)

8.3.5. EDPR XREF [70](#edpr-xref)

8.3.6. Assign Keys for Emergency Department Users [70](#assign-keys-for-emergency-department-users)

9\. Protocols [72](#protocols)

9.1. EDIS Protocols [72](#edis-protocols)

9.2. Other Protocols [73](#other-protocols)

10\. List Templates [75](#list-templates)

10.1. EDIS List Templates [75](#edis-list-templates)

11\. Troubleshooting [76](#troubleshooting)

11.1. Check-in via Scheduling [76](#check-in-via-scheduling)

11.2. Blank View [76](#blank-view)

11.3. PCE Visits [76](#pce-visits)

11.3.1. Check the EDPF LOCATION Parameter [76](#check-the-edpf-location-parameter)

11.3.2. Check for Active Person Class [76](#check-for-active-person-class)

11.4. Nurse Assignments [76](#nurse-assignments)

11.5. Intermittent Login Difficulties [77](#intermittent-login-difficulties)

11.6. PIV Provisioning [77](#piv-provisioning)

11.7. Big Boards [77](#big-boards)

11.7.1. Big Board patient data is not updating properly [77](#big-board-patient-data-is-not-updating-properly)

11.7.2. The display on the Big Board does not fit to the screen [77](#the-display-on-the-big-board-does-not-fit-to-the-screen)

List of Tables

Table 1: Optimal Viewing Requirements [9](#_Toc54254120)

Table 2: Parameters [10](#_bookmark4)

Table 3: EDIS Routine Checksums [17](#_Toc54254122)

Table 4: Global Placement and Protection [21](#_bookmark5)

Table 5: XMOS Executable (XE) Files [22](#_Toc54254124)

Table 6: File Descriptions [23](#_bookmark7)

Table 7: Subfile – Discharge Diagnosis Files [30](#_bookmark8)

Table 8: Subfile – XE Orders [31](#_bookmark9)

Table 9: Record Indices for File \#230 [32](#_bookmark10)

Table 10: XE ED Log History Files (#230.1) [33](#_bookmark11)

Table 11: XE File Record Indices (#230.1) [36](#_bookmark12)

Table 12: XE Files – Tracking Staff (#231.7) [37](#_bookmark13)

Table 13: XE Files Record Indices (#231.7) [38](#_bookmark14)

Table 14: XE Files – Tracking Room Bed (#231.8) [38](#_bookmark15)

Table 15: XE Files – Record Indices (#231.8) [41](#_bookmark16)

Table 16: XE Files – Tracking Area (#231.9) [41](#_bookmark17)

Table 17: XE Files Display Board Configuration Subfile [44](#_Toc54254136)

Table 18: Files and Fields that Point to Tracking Code File [44](#_Toc54254137)

Table 19: Tracking Code (#233.1) [45](#_Toc54254138)

Table 20: Tracking Code File Indices (#233.1) [46](#_Toc54254139)

Table 21: Tracking Code Set (#233.2) [46](#_bookmark21)

Table 22: Subfile – Tracking Code Set File – Codes (#233.21) [47](#_bookmark22)

Table 23: CPE Role (#232.5) [47](#_bookmark23)

Table 24: EDP Worksheet Specification (#232.6) [49](#_bookmark24)

Table 25: Subfile – Sections (#232.62) [51](#_Toc54254144)

Table 26: Subfile – Components (#232.622) [51](#_Toc54254145)

Table 27: Subfile – Roles (#232.63) [52](#_Toc54254146)

Table 28: EDP Worksheet Section (#232.71) [52](#_bookmark25)

Table 29: Subfile – Components (#232.711) [53](#_Toc54254148)

Table 30: Subfile – Roles (#232.712) [53](#_Toc54254149)

Table 31: EDP Worksheet Component (#232.72) [54](#_bookmark26)

Table 32: Subfile – Parameters (#232.725) [55](#_Toc54254151)

Table 33: Subfile – Components (#232.727) [56](#_Toc54254152)

Table 34: Subfile – Roles (#232.728) [56](#_Toc54254153)

Table 35: Subfile – Validator (#232.729) [56](#_Toc54254154)

Table 36: EDP Worksheet Component Type (#232.73) [57](#_Toc54254155)

Table 37: NHAMCS Reason for Visit (#233.8) [57](#_bookmark27)

Table 38: NHAMCS Reason for Visit Display (#233.81) [58](#_bookmark28)

Table 39: ED Complaint (#233.82) [58](#_bookmark29)

Table 40: Attribute (#233.821) [59](#_bookmark30)

Table 41: Possible Value (#233.8211) [59](#_bookmark31)

Table 42: Associated Symptom (#233.822) [60](#_bookmark32)

Table 43: Clinical Events (#234) [60](#_bookmark33)

Table 44: EDP Report Template (#232.1) [62](#_Toc54254163)

Table 45: Subfile – Sequence (#232.12) [62](#_Toc54254164)

Table 46: Subfile – Roles (#232.13) [62](#_Toc54254165)

Table 47: EDP Report Elements (#232.11) [63](#_Toc54254166)

Table 48: EDIS Options [65](#_bookmark36)

List of Figures

Figure 1: The EDIS Topology [8](#_bookmark1)<span id="_Toc402873895" class="anchor"></span>

# Product Description


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Product Description](#product-description)
  - [About this Guide](#about-this-guide)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
  - [Document Conventions](#document-conventions)
- [General Information](#general-information)
  - [Architectural Scope](#architectural-scope)
    - [Web Application](#web-application)
    - [URLs](#urls)
    - [EDIS Big Boards](#edis-big-boards)
  - [System Performance](#system-performance)
    - [Scaling Guide: Memory and Central Processing Unit (CPU)](#scaling-guide-memory-and-central-processing-unit-cpu)
    - [Disk Space](#disk-space)
- [Parameters](#parameters)
  - [EDIS (EDPF) Parameters](#edis-edpf-parameters)
    - [Setting Up Synchronization with Patient Care Encounters](#setting-up-synchronization-with-patient-care-encounters)
- [Routines](#routines)
  - [EDIS Routines](#edis-routines)
  - [EDIS Checksums](#edis-checksums)
- [Files and Globals](#files-and-globals)
  - [Globals](#globals)
  - [Files](#files)
    - [File Descriptions](#file-descriptions)
- [Exported Remote Procedure Calls](#exported-remote-procedure-calls)
  - [EDIS Remote Procedure Calls](#edis-remote-procedure-calls)
    - [EDPCBRD RPC](#edpcbrd-rpc)
    - [EDPCTRL RPC](#edpctrl-rpc)
    - [EDPGLOB RPC](#edpglob-rpc)
- [Exported Options](#exported-options)
  - [EDIS Options](#edis-options)
  - [Include EDIS Options in Users’ Menu Trees](#include-edis-options-in-users-menu-trees)
    - [Assign EDIS Views to Users](#assign-edis-views-to-users)
- [Security](#security)
  - [IAM Single Sign-On Internal (SSOi) and VistA Integration Adapter (VIA)](#iam-single-sign-on-internal-ssoi-and-vista-integration-adapter-via)
  - [Secure Sockets Layer](#secure-sockets-layer)
    - [PKI Encryption Basics](#pki-encryption-basics)
  - [Security Keys](#security-keys)
    - [EDPF KIOSKSNOTE: This security key is no longer used as of EDIS v.2.1.1/EDP\2.0\6.](#edpf-kiosksnote-this-security-key-is-no-longer-used-as-of-edis-v211edp206)
    - [EDPR EXPORT](#edpr-export)
    - [EDPF WORKSHEETS](#edpf-worksheets)
    - [EDPR ADHOC](#edpr-adhoc)
    - [EDPR XREF](#edpr-xref)
    - [Assign Keys for Emergency Department Users](#assign-keys-for-emergency-department-users)
- [Protocols](#protocols)
  - [EDIS Protocols](#edis-protocols)
  - [Other Protocols](#other-protocols)
- [List Templates](#list-templates)
  - [EDIS List Templates](#edis-list-templates)
- [Troubleshooting](#troubleshooting)
  - [Check-in via Scheduling](#check-in-via-scheduling)
  - [Blank View](#blank-view)
  - [PCE Visits](#pce-visits)
    - [Check the EDPF LOCATION Parameter](#check-the-edpf-location-parameter)
    - [Check for Active Person Class](#check-for-active-person-class)
  - [Nurse Assignments](#nurse-assignments)
  - [Intermittent Login Difficulties](#intermittent-login-difficulties)
  - [PIV Provisioning](#piv-provisioning)
  - [Big Boards](#big-boards)
    - [Big Board patient data is not updating properly](#big-board-patient-data-is-not-updating-properly)
    - [The display on the Big Board does not fit to the screen](#the-display-on-the-big-board-does-not-fit-to-the-screen)
Emergency Department Integration Software (EDIS) incorporates several Web-based views that extend the current Computerized Patient Record System (CPRS) to help healthcare professionals track and manage the flow of patient care in the emergency - department setting. EDIS views are based on a class-three application developed by the Upstate New York Veterans Health Care Network —or Veterans Integrated Services Network (VISN) 2. Most views are site-configurable. EDIS enables you to:
- Add emergency-department patients to the application’s electronic whiteboard—or big board—display
- View information about patients on the display board
- Edit patient information
- Remove patients from the display board
- Create administrative and operational reports
The application also includes views for entering patients’ dispositions and configuring the display board.<span id="_TOC_250052" class="anchor"></span>

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Emergency Department Integration Software Technical Manual* provides technical information for configuring, managing, and troubleshooting local (M Server) components of the EDIS application.

## Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 508 Compliance Testing is required for an application utilizing a Graphical User Interface (GUI), such as CPRS or BCMA. Roll and scroll VistA Legacy applications written in MUMPS need not comply with Section 508 Compliance requirements.

> **NOTE:** EDIS received a 508 exception on 8/12/2020.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Document conventions include:

- Bold type indicates application elements (e.g. views, panes, links, buttons, prompts, and text boxes) and keyboard key names.
- Keyboard key names appear in angle brackets \< \>.
- *Italicized* text indicates special emphasis or user responses.
- ALL CAPS indicate M routines, parameters, and option names.

# General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Architectural Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS runs as a Web application on a centrally located Oracle WebLogic server that contains program logic and operational emergency-department data in its Java middle tier (refer to XXXX). The presentation tier is a Java Server Faces (JSF) application. The data tier encompasses local sites’ Veterans Health Information Systems and Technology Architecture (VistA) systems and a centrally located relational database management system (RDMS) data store containing Standard Data Services (SDS) tables.

The application uses remote procedure calls (RPCs) from local VistA implementations to populate patient and provider selection lists, provide limited data synchronization between EDIS and CPRS, and determine users’ access levels.<span id="_TOC_250047" class="anchor"></span>

### Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application’s presentation tier runs in users’ Web browsers. The VA’s IAM Single Sign-On Internal (SSOi) solution provides end-user authentication and the VistA Integration Adapter (VIA) facilitates VistA authorization utilizing the SAML token provided by SSOi.

### URLs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### EDIS in Production Accounts

When EDIS is running in your site’s production account, use REDACTED for user access to the main application. Users must be assigned the appropriate EDIS options to gain access to the data in the application. Follow VA and site procedures when granting user access, see Section 7 for a complete list of EDIS options.

#### EDIS in Test Accounts

When EDIS is running in your site’s test account, use REDACTED for user access to the main application.

<span id="_bookmark1" class="anchor"></span>Figure 1: The EDIS Topology

> ![](edis-technical-manual-file-name-contains-r/002.png)

### EDIS Big Boards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites can configure one or more electronic whiteboard (also known as big board) displays. Display boards run in their own browser-based instances.

Use the following address as the main big board display. Replace the sitecode parameter 442 with the local institution number of the current site.

REDACTED

Secondary big board displays can be accessed by appending the above address. For example, if the 442 site has a secondary display board named Lab it would have the following address:

REDACTED

Appending the following arguments in the address will change the site and/or secondary display board:

- Replace sitecode=442 with the respective sitecode=current_site_code.
- Replace board=Lab with the respective board=secondary_board_name.

For assistance setting up the Big Board, refer to local operating system deployment (OSD) processes to properly image the device using the approved EDIS baseline. For imaging assistance, contact the Client Technologies team.

<span class="mark">REDACTED</span>

## System Performance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scaling Guide: Memory and Central Processing Unit (CPU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Workstations should comply with VA Desktop Minimum Acceptable Configurations, see table below for optimal viewing requirements.

<table>
<caption><p><span id="_bookmark4" class="anchor"></span>Table 2: Parameters</p></caption>
<colgroup>
<col style="width: 35%" />
<col style="width: 38%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Resolution</th>
<th>CPU</th>
<th>RAM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>852 x 480 (480 p), 24 frames per second (fps)</td>
<td>Intel Pentium 4 2.33 GHz processor (or equivalent)</td>
<td>256 MB RAM with 64 MB VRAM</td>
</tr>
<tr class="even">
<td><p>1280 x 720 (720 p), 24–30</p>
<p>fps</p></td>
<td>Intel Pentium 4 3 GHz processor (or equivalent)</td>
<td>128 MB RAM with 64 MB VRAM</td>
</tr>
<tr class="odd">
<td>1920 x 1080 (1080 p) 24 fps</td>
<td>Intel Core Duo 1.8 GHz processor (or equivalent)</td>
<td>128 MB RAM with 64 MB VRAM</td>
</tr>
</tbody>
</table>

<span id="_bookmark4" class="anchor"></span>Table 2: Parameters

### Disk Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS installation creates files in two global: ^EDP and ^EDPB.

- You can expect ^EDP to grow at the following yearly rate: 2,000 bytes multiplied by the number of emergency-department visits per year. For example, if your emergency department responds to an average of 12,000 visits every year, you can expect ^EDP to grow at a yearly rate of 24 MB. You should place this global in a volume with sufficient space to manage this growth.
- You can expect ^EDPB to remain small. (It is currently about 50 K.)

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS (EDPF) Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc54254122" class="anchor"></span>Table 3: EDIS Routine Checksums</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>EDPF Parameter Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDPF BIGBOARD KIOSKS</td>
<td><p><strong>NOTE:</strong> This parameter is no longer used as of EDIS v.2.1.1/EDP*2.0*6.</p>
<p>This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.</p></td>
</tr>
<tr class="even">
<td>EDPF DEBUG START TIME</td>
<td>This parameter sets a $H timestamp to signal that EDIS should log out its RPCs for 30 minutes following the debug time stamp.</td>
</tr>
<tr class="odd">
<td>EDPF LOCATION</td>
<td><p>This parameter holds one or more entries from the Hospital Location (#44) file. Entries correspond to hospital locations that the emergency department uses. With this parameter, VistA prompts sites for a time range or sequence. If sites have multiple Hospital Location file entries, they have two choices when responding to the Time Range or Sequence prompt: they can enter a time range or a sequence.</p>
<p>Entering a time range allows EDIS to map Hospital Location entries by time of day. EDIS uses this mapping when users create encounters in the Patient Care Encounters (PCE) package: it matches the Hospital Location entry based on the current time of day. The parameter accepts ranges in military time.</p>
<p>Entering a sequence allows sites to map Hospital Location entries in order of preference. When users create encounters in PCE, EDIS uses the entry with the lowest sequence number to create visits.</p>
<p>When users create appointments by checking in patients via the Scheduling package, any matches on this parameter’s list of locations (be they time- or sequence-based) cause EDIS to add the checked-in patient to the display board.</p></td>
</tr>
<tr class="even">
<td>EDPF NURSE STAFF SCREEN</td>
<td><p>This parameter allows sites to select the type of filtering upon which EDIS bases its nurse-selection list. It applies filtering—or screening— to the New Person file (#200). By default, EDIS allows selections from all entries in the New Person file. Other screening options include the following:</p>
<ul>
<li><p>Allow only persons holding the ORELSE key</p></li>
<li><p>Allow only persons holding the PSJ RNURSE key</p></li>
<li><p>Allow only persons who are present and active in the Nurse Staff file (#210)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>EDPF SCHEDULING TRIGGER</td>
<td><p>This parameter allows sites to specify which Scheduling package event, triggers EDIS to automatically add patients to the board. Sites can choose from one of the following two selections:</p>
<p>1: Patient will be added to the board when an appointment is made</p>
<p>4: Patient will be added to the board when checked in</p>
<p>Sites can set this parameter at the package, system, or division level.</p></td>
</tr>
<tr class="even">
<td>EDPF SCREEN SIZES</td>
<td>This parameter contains a list of selectable screen sizes for sites’ EDIS display boards. The parameter generally lists large-display LCD or plasma screen sizes. Add screen sizes to this parameter using the following format: WxH (width multiplied by height). You can set this parameter at the package, system, or division level.</td>
</tr>
<tr class="odd">
<td>EDP APP COUNTDOWN</td>
<td>This parameter contains the number of countdown seconds before the application closes. Once the timeout is met, this is the number that the counter will start with as it begins countdown for closure. If this parameter is set at 15, after the timeout has occurred, the user will be given 15 seconds to respond to a dialog.</td>
</tr>
<tr class="even">
<td>EDP APP TIMEOUT</td>
<td>This holds the number of seconds until the application times out. If set, this value overrides the user’s DTIME value.</td>
</tr>
</tbody>
</table>

<span id="_Toc54254122" class="anchor"></span>Table 3: EDIS Routine Checksums

### Setting Up Synchronization with Patient Care Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDPF LOCATION parameter should contain the hospital location or locations that your emergency department uses. If yours is a multi -division site, make an entry for each division.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools option prompt, type *ep* (for Edit
4.  Parameter Values) and then press the \<Enter\> key.
5.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf l* (for
6.  EDPF LOCATION)*,* and then press the \<Enter\> key.
7.  At the Select INSTITUTION NAME prompt, type the name or station number of your institution and then press the \<Enter\> key.
8.  At the Select Time Range (ex. 0800-1200) or Sequence prompt, enter the time range during which the clinic location functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department 24 hours a day, type 0001-2400 Alternately, type a number that represents the location’s preference rating (the number 1 represents the most-preferred location). Press the \<Enter\> key. When users create a PCE encounter, EDIS uses time-of-day-based or preference-based criteria to determine the encounter’s location.
9.  NOTE: When selecting time ranges, take care to account for all hours of emergency-department operation. EDIS does not create PCE appointments for patients whom users add during times that you don’t include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE appointment for the patient. Also, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE appointment for the first clinic.
10. At the Are you adding \[*your time range or sequence*\] as a new Time Range or Sequence? Yes// prompt, press the \<Enter\> key to accept the time range or sequence—or, if you’ve made a mistake, type the letter *n* (for *No*) and press the \<Enter\> key.
11. VistA displays a confirmation: Time Range (ex. 0800-1200) or Sequence \[*your time range or sequence*\]//. Press the \<Enter\> key to acknowledge this confirmation.
12. At the ED LOCATION prompt, type the name of the location that serves as your site’s emergency department during this time range (or for this preference rating) and press the \<Enter\> key.
13. Repeat steps 6 through 9 for additional emergency-department locations.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- EDP15P – Pre-init for closing ambulance patients and named patients over 5 days old with a LOC of ‘0.’
- EDP22PST - Post-init for facility install.
- EDP2PST – Post-init for facility install.
- EDPARPT - This routine handles the following functions
- Saving/Modifying report templates
- Building new report templates
- Executing existing report templates as well as ad-hoc reports (fully custom unsaved reports).
- EDPARPT1 – Ad Hoc Reports.
- EDPBCF loads and saves display-board configuration settings—including column values, color maps, room and area values, parameter settings, and screen-size settings. It also loads a list of display boards and their specifications.
- EDPBCM creates and saves configuration settings for color maps. It creates color-map elements, closing tags, map elements for standard urgencies, and single map elements. It also builds color-map selection lists.
- EDPBDL deletes or inactivates configuration entries. It deletes rooms or beds if the application’s log entries are not referencing them; otherwise, it inactivates the rooms or beds.
- EDPBKS supports a list template that maps fully qualified machine names to the names of EDIS big board displays; this routine enables sites to add, change, and delete large displays that run in kiosk mode.;
- EDPBLK handles locking and unlocking for configuration settings. It displays one of three error messages when one user attempts to make or save configuration changes while another user is also making or saving changes.
- EDPBPM loads current and saves updated Configuration view parameter settings (diagnosis required, coded diagnosis required, disposition required, reason for delay required, number of minutes before reason for delay is required, shift start time and duration, include residents, default room or area, and arriving-ambulance area). It also saves time zone differences (in minutes) and sets the fail node.
- EDPBRM loads a list of all rooms and beds in sequence, builds an XML output file containing this list, and keeps the list updated. It also adds and updates room-and-area records, loads multi-assignment areas and choice lists (display-when, single- and multiple-patient assignments, and so forth).
- EDPBRS sets and resets display-board specifications (default-board specifications, display width, scroll-delay time, column size, column headers and size, font size, row colors, baseline rooms, and baseline parameters).
- EDPBSL loads selection lists (acuity, status, mode of arrival, disposition, and reason for delay) and builds XML output files for them. It also saves selection-list changes; creates new code sets; clears codes from, and adds new codes to, the CODES multiple; and updates existing codes in, and adds new codes to, the Tracking Code file (#233.1).
- EDPBST returns a list of staffing matches from VistA’s New Person file (#200). For each of the following three roles, it builds a list of staff members who have an active person class: resident, physician, and nurse. It also saves updated staff members and creates and updates records in the Tracking Staff file (#231.7).
- EDPBWS is the main routine for processing, building, retrieving, and modifying worksheets for the EDIS User Interface.
- EDPCBRD is the controller for the EDIS display board. It processes requests via remote procedure calls (RPCs) and also supports a Caché Server Pages (CSP) mode for processing requests via CSP.
- EDPCDBG is the debugging routine for the display-board controller. It turns debugging on and off, enables the EDIS debugging log, logs debugging activities for 30 minutes after the debugging start time, records debugging start and stop times, and saves debugging requests and XML results.
- EDPCONV processes incoming mail to convert emergency-department visits from Syracuse class-three application files to EDIS class-one files. It stores conversion data in the Tracking Code file (#233.1), Tracking Room/Bed file (#231.8), ED Log file (#230), and ED Log History file (#230.1).
- EDPCONV1 converts configuration data from Syracuse class-three application files to EDIS class-one files. It stores converted data in the Tracking Area file (#231.9).
- EDPCSV is a comma-separated-value (CSV) utility that provides a controller for HyperText Transfer Protocol (HTTP) requests.
- EDPCTRL is the controller for EDIS. It processes requests via remote procedure calls (RPCs) and also supports Caché Server Pages (CSP) mode for processing requests via CSP.
- EDPDD provides a test update log.
- EDPFAA provides RPC calls to the local facility. It also sets up EDIS sessions and returns role-based views for users. (EDPFAA code enabled VHA eHealth University \[VeHU\] training.)
- EDPFLEX provides Lexicon-package utilities: it returns matches from the Lexicon package when users type in dispositions.
- EDPFMON monitors Health Level 7 (HL7) VistA event messages at the facility. It adds new orders to patients’ log entries based on visit-related information from the following packages: Radiology, Laboratory, Pharmacy, Consults, Procedures, Dietetics, and Order Entry. It also updates orders’ statuses and removes orders from patients’ log entries.
- EDPFMOVE is part of the conversion routine. It moves local emergency-department visits to EDIS and provides conversion-related messages—“Visit conversion has completed,” for example. This routine also provides users with several conversion-related options—such as the option to convert Syracuse class-three configuration data (in addition to patient data).
- EDPFPER looks up emergency-department staff (providers, residents, and nurses) in VistA’s New Person file (#200). The routine adds people who match its screening criteria to EDIS staffing lists.
- EDPFPTC performs patient-selection checks. For example, this routine checks to see if selected patients are already on the Active Patients list, have patient records that are marked sensitive (in which case the routine displays a warning), are deceased, or have identifiers that are similar to the identifiers of one or more patients who are already on the Active Patients list. (Patients on the Active Patients list are ipso facto on the display board.) This routine also gets patient record flags (PRFs) for display within EDIS and makes security-log entries when users access records marked sensitive.
- EDPFPTL accepts as its input patient names and social security numbers (including last four social security numbers and last-name initials concatenated with last four social security numbers) and returns from the local VistA system a list of possible matches.
- EDPGLOB – This routine is used to return a global array. If the amount of data is too large, store errors can occur in VistA. Using the EDPGLOB RPC fixes these errors and utilizes global arrays to store and send back the data.
- EDPLEX provides API wrappers for calls to the Lexicon. Used by other EDIS routines.
- EDPLOG updates the EDIS log in response to timestamp changes. It also processes diagnoses and checks for the presence of data in required fields before letting users remove patients from the system.
- EDPLOG1 validates record entries and returns error messages for invalid entries.
- EDPLOGA adds log records for new patients. It sets up patient fields, adds default values to stub entries, creates current log records, and creates initial log-history entries. This routine also deletes the initial history-log stub entry.
- EDPLOGH adds new log-history entries and saves new entries for changed fields. This routine also checks timestamps in the ED Log History file (#230.1) for possible data-entry collisions and displays a warning message—“Since you loaded this entry, changes have been made by someone else”—when collisions are imminent. Similarly, when users update data and select a different view before saving their updates, this routine warns them that they will lose their changes if they exit the view without first saving their changes. Finally, this routine notifies users when their bed choices are no longer available.
- EDPLPCE creates a visit in the CPRS Patient Care Encounters (PCE) package when users select a provider, resident, nurse, or diagnosis in EDIS. It updates diagnoses for emergency-department visits in EDIS if users enter the diagnoses in CPRS, and in CPRS if users enter the diagnoses in EDIS. This routine also coordinates primary providers between CPRS and EDIS.
- EDPMAIL parses and processes incoming VA MailMan messages from SEND^EDPFMON, which monitors order-related events such as new orders, order changes, deleted orders, and so forth. EDPMAIL also parses and processes patient check-in events.
- EDPQAR logs area information. It returns site-configurable parameters and default areas, and adds default areas in cases where no default areas are assigned.
- EDPQDB displays active log entries on the EDIS display board. It gets display-board data—a list of all beds in sequence for a given area, patient data, and so forth—computes order statuses, and formats data for display.
- EDPQDBS gets display-board specifications for room, area, and staff color configurations.
- EDPQLE retrieves log entries by request and returns XML-formatted log entries for patient demographics, diagnoses (ICD-10-CM coded), fields required for closing entries (delay reasons, physician assignments, and so forth), and time stamps.
- EDPQLE1 retrieves supporting information—such as staff and other selection items—and adds the information to XML pick lists. It also builds nodes for code sets.
- EDPQLP returns lists for the log-entry edit context. It also builds duplicate-name and last- four-Social-Security-number lists for counters.
- EDPQPCE retrieves PCE information such as diagnoses (including primary and free-text diagnoses) for emergency-department visits.
- EDPQPPS – routine to handle display board specifications.
- EDPRPT gets data for reports by site and date range. This routine turns on switches that determine the beginning and ending points of the report date range and the report type. It also returns timestamp-related data—such as the times acuities were first assigned, the times patients left the waiting area, the times admitting decisions were entered, and so forth.
- EDPRPT1 gets data for the Activity report based on site and date range. It gets report headers (CSV), calculates times and averages for column values, initializes counters and sums, returns external values for codes, and includes a list of assigned providers.
- EDPRPT10 gets data for the Admissions report based on site and date range. This routine initializes counters and sums, gets report headers (CSV), calculates times and averages, initializes counters and sums, and returns external values for codes.
- EDPRPT11 gets data for the Patient Intake report based on site and date range. This routine initializes counters and sums, gets report headers, returns counts and averages, performs rounding computations, returns hours (24-hour—or military—clock format), and returns name-of-day (Monday, Tuesday, and so forth).
- EDPRPT12 gets data for the Orders by Acuity report based on site and date range. It gets report headers and returns an acuity-based count of lab, imaging, medication, consult, and other orders.
- EDPRPT2 gets data for the Delay report based on site and date range. It initializes counters and sums, returns counts and averages, and gets column headers. The routine also returns disposition indicators for VA admissions and external values for codes.
- EDPRPT3 gets data for the Missed Opportunities report based on site and date range. It initializes counters and returns a 1 (one) or 0 (zero) to indicate missed opportunities. The routine also gets column headers, initializes counters, calculates times, and returns totals as CSV- or XML-formatted data.
- EDPRPT4 gets data for the Delay Summary report based on site and date range. It initializes counters and sums and returns counts and averages as CSV- or XML-formatted data. This routine also returns external values for acuity and other codes, and codes (1 or 0) for IEN statuses that indicate observation.
- EDPRPT5 returns data for the Shift report based on site and day. It initializes counters and sums, calculates the number of visits that carried over, and returns the following: column information (headers, counts and averages—as CSV- and XML-formatted data), the names of shifts (one, two, three, and so forth—based on shift times), and external values for acuity codes.
- EDPRPT7 gets data for the Exposure report based on site and the infected person’s time in and time out of the emergency department. It returns a list of patients who were in the waiting room and treatment rooms during the infected patient’s stay (adding a row for each room the infected patient used —including laboratory and x-ray). It also returns on-duty staff assignments. EDPRPT7 returns external values for codes.
- EDPRPT7C gets data for the Exposure report in CSV format.
- EDPRPT8 gets data for the Acuity report based on site and date range. It initializes counters and sums and returns external values for acuity codes. The routine returns counts and averages for acuity-based entries, all admissions, and VA admissions.
- EDPRPT9 gets data for the Patient Cross Reference (XRef) report based on site and date range. It uses the ED Log file (#230) to provide information about patients’ identities.
- EDPRPTBV gets data for the BVAC report based on site and date range. This routine initializes counters and sums, gets column headers, calculates sums and averages, and returns external values for codes.
- EDPX provides a group of common utilities that includes the following: ESC (X), escape for XML transmission; UES (X), unescape XML; UESREQ (REQ), unescape HTTP post; VAL (X,R), returns parameter value or null; NVPARSE (LST, IN), parses tab and delimited name-value pairs into an array; XMLS (TAG, DATA, LBL), returns an XML node as \<TAG data=“9” label=“XXX” /\>; XMLA (TAG, ATT, END), returns an XML node as \<TAG att1=“a” att2=“b”… /\>; SMLE (SRC), appends lists to XML arrays as elements; XML (X), adds the line of XML that is to be returned; CODE (X), returns internal values for codes; MSG (MSG), writes out error messages.
- EDPYCHK performs a pre-installation environment check.
- EDPYPRE is the pre-initialization routine.
- EDPYPST is the post initialization routine.

## EDIS Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following contains routine names and checksums as of patch EDP\*2.0\*15:

| Routine  | Checksum  |
|----------|-----------|
| EDP15P   | 2688979   |
| EDP2ENV  | 653636    |
| EDP2PRE  | 852824    |
| EDP2PST  | 10565179  |
| EDPARPT  | 95079217  |
| EDPARPT1 | 17834740  |
| EDPBCF   | 26108693  |
| EDPBCM   | 17332251  |
| EDPBDL   | 11063047  |
| EDPBKS   | 15371728  |
| EDPBLK   | 7330093   |
| EDPBPM   | 6261242   |
| EDPBRM   | 26325333  |
| EDPBRS   | 19233483  |
| EDPBSL   | 20029785  |
| EDPBST   | 9812007   |
| EDPBWS   | 235189948 |
| EDPCBRD  | 4768831   |
| EDPCDBG  | 4038807   |
| EDPCONV  | 70928886  |
| EDPCONV1 | 10237522  |
| EDPCSV   | 1174493   |
| EDPCTRL  | 89022760  |
| EDPDD    | 1577854   |
| EDPDTL   | 80102068  |
| EDPFAA   | 37763699  |
| EDPFLEX  | 10693270  |
| EDPFMON  | 26481799  |
| EDPFMOVE | 44917407  |
| EDPFPER  | 4359382   |
| EDPFPTC  | 19115099  |
| EDPFPTL  | 4915038   |
| EDPFX233 | 2082229   |
| EDPGLOB  | 4109172   |
| EDPHIST  | 59451957  |
| EDPLAB   | 51111821  |
| EDPLEX   | 11049187  |
| EDPLOG   | 64279489  |
| EDPLOG1  | 2583250   |
| EDPLOGA  | 12583805  |
| EDPLOGH  | 12593326  |
| EDPLPCE  | 46706543  |
| EDPMAIL  | 7450955   |
| EDPMED   | 4429388   |
| EDPQAR   | 7638401   |
| EDPQDB   | 57296617  |
| EDPQDBS  | 7446153   |
| EDPQLE   | 60984334  |
| EDPQLE1  | 11912520  |
| EDPQLP   | 12368052  |
| EDPQLW   | 6750208   |
| EDPQPCE  | 6816999   |
| EDPQPP   | 92368102  |
| EDPQPPS  | 4046541   |
| EDPRPT   | 25243776  |
| EDPRPT1  | 51586751  |
| EDPRPT10 | 32122849  |
| EDPRPT11 | 8059237   |
| EDPRPT12 | 8703521   |
| EDPRPT13 | 7846285   |
| EDPRPT2  | 26475007  |
| EDPRPT3  | 14278258  |
| EDPRPT4  | 32540898  |
| EDPRPT5  | 54053972  |
| EDPRPT6  | 9636184   |
| EDPRPT7  | 23000869  |
| EDPRPT7C | 24197469  |
| EDPRPT8  | 15923220  |
| EDPRPT9  | 1597193   |
| EDPRPTBV | 30889629  |
| EDPUPD   | 6705060   |
| EDPVIT   | 32884634  |
| EDPWS    | 17524272  |
| EDPWSL   | 7192929   |
| EDPWSLM  | 3855274   |
| EDPWSP   | 7526722   |
| EDPX     | 16354064  |
| EDPXML   | 13678293  |
| EDPYCHK  | 1074868   |
| EDPYP2   | 8435306   |
| EDPYPRE  | 13981628  |
| EDPYPST  | 35872203  |

<span id="_bookmark5" class="anchor"></span>Table 4: Global Placement and Protection

# Files and Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses the following globals:

- ^EDP
- ^EDPB

The ^EDP global holds a list of patients who are currently checked in at the emergency-department (that is, the list of active patients). The ^EDPB global holds a comprehensive list of emergency-department activities.

<table>
<caption><p><span id="_Toc54254124" class="anchor"></span>Table 5: XMOS Executable (XE) Files</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 46%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Global</th>
<th>Type</th>
<th>Placement</th>
<th>Journal</th>
<th>Protection</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^EDP</td>
<td>Dynamic</td>
<td><p>Place this global in a volume set that can accommodate the following yearly growth rate:</p>
<p>2,000 bytes * visits per year</p></td>
<td>Yes</td>
<td>RWP or D</td>
</tr>
<tr class="even">
<td>^EDPB</td>
<td>Static</td>
<td>No recommendation (this global should remain small)</td>
<td>Yes</td>
<td>RWP or D</td>
</tr>
</tbody>
</table>

<span id="_Toc54254124" class="anchor"></span>Table 5: XMOS Executable (XE) Files

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_bookmark7" class="anchor"></span>Table 6: File Descriptions</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 48%" />
<col style="width: 18%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File #</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Root Global</p>
</blockquote></th>
<th><blockquote>
<p>Global Protection</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>230</td>
<td>ED LOG</td>
<td>^EDPB(230)</td>
<td>@</td>
</tr>
<tr class="even">
<td>230.1</td>
<td>ED LOG HISTORY</td>
<td>^EDP(230.1)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>231.6</td>
<td>TRACKING BOARD</td>
<td>^EDPB(231.6)</td>
<td>@</td>
</tr>
<tr class="even">
<td>231.7</td>
<td>TRACKING STAFF</td>
<td>^EDPB(231.7)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>231.8</td>
<td>TRACKING ROOM- BED</td>
<td>^EDPB(231.8)</td>
<td>@</td>
</tr>
<tr class="even">
<td>231.9</td>
<td>TRACKING AREA</td>
<td>^EDPB(231.9)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>232.1</td>
<td>EDP REPORT TEMPLATE</td>
<td>^EDPB(232.1)</td>
<td>@</td>
</tr>
<tr class="even">
<td>232.11</td>
<td>EDP REPORT ELEMENTS</td>
<td>^EDPB(232.11)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>232.5</td>
<td>CPE ROLE</td>
<td>^EDPB(232.5)</td>
<td>@</td>
</tr>
<tr class="even">
<td>232.6</td>
<td>EDP WORKSHEET SPECIFICATION</td>
<td>^EDPB(232.6)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>232.71</td>
<td>EDP WORKSHEET SECTION</td>
<td>^EDPB(232.71)</td>
<td>@</td>
</tr>
<tr class="even">
<td>232.72</td>
<td>EDP WORKSHEET COMPONENT</td>
<td>^EDPB(232.72</td>
<td>@</td>
</tr>
<tr class="odd">
<td>232.74</td>
<td>EDP COMPONENT VALIDATORS</td>
<td>^EDPB(232.74)</td>
<td>@</td>
</tr>
<tr class="even">
<td>233.1</td>
<td>TRACKING CODE</td>
<td>^EDPB(233.1)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>233.2</td>
<td>TRACKING CODE SET</td>
<td>^EDPB(233.2)</td>
<td>@</td>
</tr>
<tr class="even">
<td>233.8</td>
<td>National Hospital Ambulatory Medical Care Survey (NHAMCS) REASON FOR VISIT</td>
<td>^EDPB(233.8)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>233.81</td>
<td>NHAMCS REASON FOR VISIT DISPLAY</td>
<td>^EDPB(233.81)</td>
<td>@</td>
</tr>
<tr class="even">
<td>233.82</td>
<td>ED COMPLAINT</td>
<td>^EDPB(233.82)</td>
<td>@</td>
</tr>
<tr class="odd">
<td>234</td>
<td>CLINICAL EVENTS</td>
<td>^EDP(234)</td>
<td>@</td>
</tr>
</tbody>
</table>

<span id="_bookmark7" class="anchor"></span>Table 6: File Descriptions

### File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ED Log (#230)

The ED Log file serves as the log of emergency-department visits and as EDIS’s key source of information for display-board data. EDIS refreshes the display board every 30 seconds, and many of the indices in this file assist in making the application’s refresh code as efficient as possible.

The file works together with the ED Log History file (#230.1) to track activities associated with typical emergency -department visits from beginning to end. The log records key clinical events—triage and disposition, for example. It also records where each patient went after his or her emergency - department visit, and who was responsible for the patient.

<table>
<caption><p><span id="_bookmark8" class="anchor"></span>Table 7: Subfile – Discharge Diagnosis Files</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References and Record Indices</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>LOG ENTRY TIME</td>
<td><p>The Log Entry field (.01) of the ED Log History file (230.1)</p>
<p>points to this field</p></td>
<td><p>230^B</p>
<p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AO (#784)</p>
<p>AP (#792)</p>
<p>APA (#806)</p>
<p>AS (#793)</p>
<p>ATI (#794)</p>
<p>ATO (#795)</p>
<p>PDFN (#801)</p>
<p>PN (#796)</p></td>
<td><p>Date-and-time field (required):</p>
<p>Contains the date and time EDIS added this log record to the file</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>INSTITUTION</td>
<td>Pointer to the Institution file (#4)</td>
<td><p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AP (#792)</p>
<p>AS (#793)</p>
<p>ATO (#795)</p>
<p>PN (#796)</p>
<p>PDFN (#801)</p></td>
<td><p>Free-text field (required): This field allows EDIS to associate log entries with</p>
<p>the stations that originated</p>
<p>the entries; it allows the same EDIS system to serve multiple institutions</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>AREA</td>
<td>Pointer to the Tracking Area file (#231.9)</td>
<td><p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AP (#792)</p>
<p>AS (#793)</p>
<p>PN (#796)</p>
<p>PDFN (#801)</p></td>
<td>Pointer field: Points to the hospital area to which records apply – initially only to the site’s emergency-department locations; will allow users to expand EDIS’s use to other departments.</td>
</tr>
<tr class="even">
<td>.04</td>
<td>PATIENT NAME</td>
<td></td>
<td></td>
<td><p>Free-text field: Contains the patient’s name. Allows sites to enter patients’ names in cases of humanitarian intervention or where patients do not yet have entries in VistA.</p>
<p>Assists in checking for duplicate names and similar names on the display.</p>
<p>This field is set to the following value in cases where ambulances are arriving and the names of the patients are unknown: (ambulance enroute)</p>
<p>When patients are added to VistA during their ED visits, their names in VistA replace clerk-entered names.</p>
<p>When users select patients from VistA, the software gets the patients’ VistA names and places them in this field.</p>
<p>The field uses this format: Surname,Firstname Names must be between 3 to 30 characters in length.</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>PATIENT SSN</td>
<td></td>
<td>AS (#793)</td>
<td><p>Free-text field: Contains the patient’s Social Security Number.</p>
<p>Allows sites to enter patients’ Social Security Numbers in cases of humanitarian care or when patients do not yet have entries in VistA.</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>PATIENT ID</td>
<td>Pointer to Patient file (#2)</td>
<td><p>AP (#792)</p>
<p>APA (#806)</p>
<p>PDFN (#801)</p></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s data file number (the DFN is the IEN in the Patient file).</p>
<p>Contains the patients in VistA for whom EDIS is creating its log entries; entries may be absent in cases where ambulances are arriving with unknown patients and where sites are rendering humanitarian aid to non- VA patients.</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>CLOSED</td>
<td></td>
<td><p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AP (#792)</p>
<p>AS (#793)</p>
<p>APA (#806)</p>
<p>Triggers CLOSED DATE/TIME (.071)</p></td>
<td><p>A setting:</p>
<ul>
<li><p>1 (Yes)</p></li>
<li><p>0 (No)</p></li>
</ul>
<p>EDIS sets this flag to <em>1</em> when users remove properly disposed patients from the area (emergency department); closed entries no longer appear on the display board.</p></td>
</tr>
<tr class="even">
<td>.071</td>
<td>CLOSED DATE/TIME</td>
<td>Date/Time</td>
<td>Triggered by the CLOSED field (.07)</td>
<td><p>Date-and-time field:</p>
<p>Contains the date/time when the log entry was ‘closed’.</p></td>
</tr>
<tr class="odd">
<td>.072</td>
<td>CLOSED BY</td>
<td>Pointer to New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Contains the IEN of the user who closed the log entry.</p></td>
</tr>
<tr class="even">
<td>.073</td>
<td>REMOVED IN ERROR</td>
<td>Set of Codes</td>
<td></td>
<td><p>Set of codes: 1 (Yes)</p>
<p>This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.</p></td>
</tr>
<tr class="odd">
<td>.074</td>
<td>RESTORED BY</td>
<td>Pointer to New Person file (#200)</td>
<td>Triggers RESTORED BY DATE/TIME</td>
<td><p>Pointer field:</p>
<p>Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.</p></td>
</tr>
<tr class="even">
<td>.075</td>
<td>RESTORED BY DATE/TIME</td>
<td>Date/Time</td>
<td><p>ARIE (#886)</p>
<p>Triggered by ‘RESTORED BY’ field (.074)</p></td>
<td><p>Date/Time:</p>
<p>This holds the date/time when the patient was ‘restored’ to the board.</p></td>
</tr>
<tr class="odd">
<td>.08</td>
<td>TIME IN</td>
<td></td>
<td>ATI (#794)</td>
<td>Date-and-time field: Contains the time and date when the patient actually arrived at the emergency department. EDIS measures patients’ length of visit from this date and time.</td>
</tr>
<tr class="even">
<td>.09</td>
<td>TIME OUT</td>
<td></td>
<td>ATO (#795)</td>
<td><p>Date-and-time field: Contains the patient’s discharge time and date.</p>
<p>EDIS prompts users for delay reasons based on the difference between time- in and time-out entries.</p></td>
</tr>
<tr class="odd">
<td>.1</td>
<td>ARRIVAL MODE</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td>Pointer field: Points to the source of the patient’s visit. Currently applies only to the sources of emergency-department visits, e.g. nursing homes or clinics. Values are associated with the &lt;stn&gt;.arrival and edp.arrival code sets.</td>
</tr>
<tr class="even">
<td>.11</td>
<td>PATIENT BRIEF ID</td>
<td></td>
<td>ADUP2 (#789)</td>
<td><p>Free-text field: Contains the patient’s display-board identifier; can store identifiers for patients who are arriving by ambulance and for non-VA patients; the identifier should be in the X9999 format.</p>
<p>When VistA patients are selected, the field stores X9999-formatted identifiers that the application constructs from the Patient file (#2); this allows the application to indicate on the display board patients who have identical X9999-formatted identifiers.</p></td>
</tr>
<tr class="odd">
<td>.12</td>
<td>VISIT</td>
<td>Pointer to the Visit file (#9000010)</td>
<td><p>230^AVISIT^MUMPS</p>
<p>(increments and decrements the dependency counter in the Visit file [#9000010])</p>
<p>230^V</p>
<p>(PCE uses this cross reference to help identify dependent entries)</p></td>
<td><p>Pointer field: Points to the visit associated with this</p>
<p>emergency-department encounter.</p>
<p>Because emergency departments don’t normally use appointments, EDIS records patient visits in this field; EDIS can then create visits in PCE so subsequent caregivers can associate orders and progress notes with the same visit; EDIS creates this visit when it collects data for any PCE-related field, allowing it to call DATA2PCE; triage nurses usually enter this data.</p></td>
</tr>
<tr class="even">
<td>.13</td>
<td>CREATION SOURCE</td>
<td></td>
<td></td>
<td><p>A setting to identify the visit-creation source:</p>
<ul>
<li><p>0 (EDIS)</p></li>
<li><p>1 (Scheduling)</p></li>
<li><p>2 (CPRS)</p></li>
</ul>
<p>EDIS generally populates the VISIT field by calling DATA2PCE; users can also create visits by entering emergency-department appointments or writing progress notes for emergency-department locations; this field records the mechanism responsible for creating the entry in the Visit file (#9000010).</p></td>
</tr>
<tr class="odd">
<td>.14</td>
<td>CLINIC</td>
<td>Pointer to the Hospital Location file (#44)</td>
<td></td>
<td>Pointer field: Holds a pointer to the specific emergency-department clinic that EDIS will associate with the patient’s visit. When users check in patients through the Scheduling package, EDIS stores a pointer to the clinic they select here until it creates a visit. When the application creates the visit, it uses the location stored in this field.</td>
</tr>
<tr class="even">
<td>1.1</td>
<td>COMPLAINT</td>
<td></td>
<td></td>
<td>Free-text field: Contains the complaint with which the patient presented; sites can include this complaint on the display board, so it should be brief enough to fit within a display-board column; this field accepts 1–50 characters.</td>
</tr>
<tr class="odd">
<td>1.2</td>
<td>DISPOSITION</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td>Pointer field: Points to the patient’s end-of-visit disposition; values for this field are associated with the &lt;stn&gt;.disposition and edp.disposition code sets.</td>
</tr>
<tr class="even">
<td>1.3</td>
<td>DISPOSITION TIME</td>
<td></td>
<td></td>
<td>Time-and-date field: Contains the time and date of the patient’s most recent disposition-field update.</td>
</tr>
<tr class="odd">
<td>1.4</td>
<td>DIAGNOSIS TIME</td>
<td></td>
<td></td>
<td>Time-and-date field: Contains the date and time of the patient’s last diagnosis-field update.</td>
</tr>
<tr class="even">
<td>1.5</td>
<td>DELAY REASON</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td>Pointer field: Points to the reason for delay (for patient stays that exceed the maximum length of stay); associated with the &lt;stn&gt;.delay and edp.delay code sets.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>COMPLAINT (LONG)</td>
<td></td>
<td></td>
<td>Free-text field: The patient’s long complaint (free text); an optional field that allows staff to enter complaints in a longer form than EDIS allows for its display-board complaint; this field holds from 1 to 220 characters.</td>
</tr>
<tr class="even">
<td>3.2</td>
<td>STATUS</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the record of a patient’s statuses during the course of his or her emergency-department visit (awaiting triage, ED patient, and so forth); associated with the &lt;stn&gt;.status and edp.status code sets.</p></td>
</tr>
<tr class="odd">
<td>3.3</td>
<td>ACUITY</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s acuity level, which is based on the Emergency Severity Index (ESI) algorithm (acuity levels 1-5); associated with the edp.acuity code set.</p></td>
</tr>
<tr class="even">
<td>3.4</td>
<td>LOC</td>
<td>Pointer to the Tracking Room-Bed file (#231.8)</td>
<td>AL (#790)</td>
<td><p>Pointer field:</p>
<p>Points to the patient’s current location; locations can be a specific room or bed, or a conceptual area (such as the hallway, parking lot, or radiology department); locations need not be physical locations; this field allows checking for unoccupied beds or areas.</p></td>
</tr>
<tr class="odd">
<td>3.5</td>
<td>MD ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s current physician (provider) assignment.</p></td>
</tr>
<tr class="even">
<td>3.6</td>
<td>NURSE ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s current nurse assignment.</p></td>
</tr>
<tr class="odd">
<td>3.7</td>
<td>RESIDENT ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s current resident assignment.</p></td>
</tr>
<tr class="even">
<td>3.8</td>
<td>COMMENT</td>
<td></td>
<td></td>
<td>Free-text field (optional): Contains comments associated with the patient’s emergency-department stay; users can enter and update this field for patients’ current visits; sites can optionally include comments on the display board; this field accepts 1–80 characters.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>DISCHARGE DIAGNOSIS</td>
<td>Multiple (230.4)</td>
<td></td>
<td>Contains the patient’s diagnosis or diagnoses for this emergency- department visit; when sites have enabled free-text diagnoses, EDIS stores patients’ diagnoses lists in this field; when sites have enabled coded diagnoses, this field holds patients’ diagnoses until their PCE visits become available, after which EDIS transfers their diagnoses lists to PCE; in this latter case, PCE becomes the real holder of patients’ diagnoses lists; however, the lists remain synchronized with EDIS to cover rare cases in which sites change parameter settings to allow free-text diagnoses; the parameter that controls diagnoses lists is in the Tracking Area file (#231.9).</td>
</tr>
<tr class="even">
<td>8</td>
<td>ORDERS</td>
<td>Multiple (230.08)</td>
<td></td>
<td>Tracks orders during the course of the patient’s emergency-department visit; an order-entry event monitor populates this multiple and identifies orders that are related to patients’ current emergency-department visits; the event monitor enables EDIS display boards to offer up-to-date order-related information with every display-board refresh; it also allows reports to track the history of orders related to emergency-department visits.</td>
</tr>
</tbody>
</table>

<span id="_bookmark8" class="anchor"></span>Table 7: Subfile – Discharge Diagnosis Files

#### Discharge Diagnosis 230.04

Sites have the option to synchronize patients’ diagnoses with PCE. If diagnoses are synchronized, every time a diagnosis changes in EDIS, the application passes the change to PCE. If sites do not synchronize patients’ diagnoses with PCE, EDIS simply keeps patient-diagnoses lists in this file. Clinical staff can later access the file’s contents and enter patients’ diagnoses into PCE.

<table>
<caption><p><span id="_bookmark9" class="anchor"></span>Table 8: Subfile – XE Orders</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References and Record Indices</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>DISCHARGE DIAGNOSIS</td>
<td></td>
<td>230.04^B</td>
<td><p>Free-text field (multiply asked):</p>
<p>Contains the free text entries of the patient’s discharge diagnoses for the visit.</p>
<p>If sites set EDIS parameters to require coded diagnoses, the text in this field will be ICD-10-CM text from Clinical Lexicon entries; some entries map to more than one ICD code.</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>ICD CODE</td>
<td>Pointer to the ICD Diagnosis file (#80)</td>
<td></td>
<td>Pointer field: This is the ICD code for the diagnosis. Clinical Lexicon utilities are used by the application to look up diagnoses. Some Clinical Lexicon entries map to more than one ICD code.</td>
</tr>
<tr class="odd">
<td>.03</td>
<td>PRIMARY</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ol type="1">
<li><p>No (secondary)</p></li>
<li><p>Yes (primary)</p></li>
</ol>
<p>This setting indicates which diagnosis is the primary diagnosis.</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark9" class="anchor"></span>Table 8: Subfile – XE Orders

#### Orders 230.08

The order-entry event monitor identifies orders that are related to patients’ current emergency-department visits and populates this multiple with these orders. This subfile enables EDIS to quickly update display boards (which EDIS refreshes every few seconds to provide up -to-date order-status information). It also allows EDIS reporting functionality to track the history of orders that are related to patients’ emergency-department visits.

<table>
<caption><p><span id="_bookmark10" class="anchor"></span>Table 9: Record Indices for File #230</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 20%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References and Record Indices</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>ORDER</td>
<td></td>
<td>230.08^B AO (#784)</td>
<td><p>Free-text field (multiply asked):</p>
<p>Contains order IDs for patients’ emergency- department-related orders (order IEN); EDIS uses this field to locate orders when the event monitor needs to update them</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>SERVICE</td>
<td></td>
<td>230.08^AC</td>
<td><p>A setting:</p>
<ul>
<li><p>M (medication)</p></li>
<li><p>L (lab)</p></li>
<li><p>R (radiology)</p></li>
<li><p>C (consult)</p></li>
<li><p>A (all others)</p></li>
</ul>
<p>Provides a general identification of the service to which orders are related and allows quick checks for orders associated with the patient’s emergency- department visit.</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>STATUS</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>N (new)</p></li>
<li><p>A (active)</p></li>
<li><p>C (complete)</p></li>
</ul>
<p>Provides the general status of orders; sites can use order status to highlight orders on the display board, enabling sites to monitor the board for orders that have been outstanding for too long.</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>STAT</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>1 (STAT)</p></li>
<li><p>0 (not STAT)</p></li>
</ul>
<p>A setting of <em>1</em> indicates stat orders; sites can optionally use colors to highlight stat orders on the display board.</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>RELEASE TIME</td>
<td></td>
<td></td>
<td>Date-and-time field: Contains the date and time of an order’s release to its service; allows sites to monitor orders for delay.</td>
</tr>
</tbody>
</table>

<span id="_bookmark10" class="anchor"></span>Table 9: Record Indices for File \#230

#### Record Indices for File \#230

<table>
<caption><p><span id="_bookmark11" class="anchor"></span>Table 10: XE ED Log History Files (#230.1)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Record Index</th>
<th>Indexed Fields</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AC (#787)</td>
<td><p>SITE, AREA, IEN</p>
<p>(active entries only)</p></td>
<td>EDIS uses this index to list patients with currently active entries on the display board</td>
</tr>
<tr class="even">
<td>ADUP1 (#788)</td>
<td><p>SITE, AREA, LASTNAME, IEN</p>
<p>(active entries only)</p></td>
<td>EDIS uses this index to contribute patients’ last names to the ADUP cross reference, which helps identify patients with similar names or similar brief identities (X9999 formatted identifiers)</td>
</tr>
<tr class="odd">
<td>ADUP2 (#789)</td>
<td><p>SITE, AREA,</p>
<p>LAST4, IEN (active entries only)</p></td>
<td>EDIS uses this index to contribute patients’ identifiers in X9999 format</td>
</tr>
<tr class="even">
<td>AL (#790)</td>
<td><p>SITE, AREA, LOC,</p>
<p>IEN (active entries only)</p></td>
<td>EDIS uses this index to check for beds and areas that are currently occupied</td>
</tr>
<tr class="odd">
<td>AN (#791)</td>
<td><p>SITE, AREA, PTNAME, IEN</p>
<p>(active entries only)</p></td>
<td>EDIS uses this index to check patients’ active statuses in cases where patients do not have DFNs (as is the case with humanitarian interventions); the application references this index before adding patients to the display board to determine whether or not patients are already on the board</td>
</tr>
<tr class="even">
<td>AP (#792)</td>
<td><p>SITE, AREA, DFN,</p>
<p>IEN (active entries only)</p></td>
<td>EDIS uses this index to test for duplicate entries when users select patients who have DFNs (that is, VistA patients) for addition to the display board</td>
</tr>
<tr class="odd">
<td>ARIE (#886)</td>
<td>RESTORED DATE/TIME,IEN</td>
<td>EDIS uses this index to search for patients who were removed in error.</td>
</tr>
<tr class="even">
<td>AS (#793)</td>
<td><p>SITE, AREA, SSN,</p>
<p>IEN (active entries only)</p></td>
<td>EDIS uses this index to see if patients are already on the display board in cases where patients don’t have DFNs and users are identifying these patients by their Social Security numbers (SSNs)</td>
</tr>
<tr class="odd">
<td>ATI (#794)</td>
<td><p>SITE, TIME IN (for</p>
<p>reports)</p></td>
<td>EDIS uses this index to get a range of visits within a user-specified time range</td>
</tr>
<tr class="even">
<td>ATO (#795)</td>
<td><p>SITE, TIME OUT</p>
<p>(for reports)</p></td>
<td>EDIS uses this index to get a range of visits that were closed within a user- specified time span</td>
</tr>
<tr class="odd">
<td>PDFN (#801)</td>
<td><p>SITE, AREA, DFN,</p>
<p>IEN (for all patients)</p></td>
<td>This index organizes all entries by patient DFN. When EDIS performs special lookups against the patient file (by SSN, for example), the lookup service returns a DFN; this index allows EDIS to find visits that correspond to these DFNs; the index contains all visit entries (closed and active)</td>
</tr>
<tr class="even">
<td>PN (#796)</td>
<td><p>SITE, AREA, PTNAME, IEN (for</p>
<p>all patients)</p></td>
<td>EDIS uses this index of <em>all</em> patient names—including the names of patients who do not have DFNs—for selecting patients when visits (closed or otherwise) need to be corrected.</td>
</tr>
</tbody>
</table>

<span id="_bookmark11" class="anchor"></span>Table 10: XE ED Log History Files (#230.1)

#### ED Log History (#230.1)

The ED Log History file provides a forward - and reverse-chronological list of updates to each emergency-department log record. The timestamps contained in this file make it possible to generate a variety of reports.

<table>
<caption><p><span id="_bookmark12" class="anchor"></span>Table 11: XE File Record Indices (#230.1)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References and Record Indices</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>LOG ENTRY</td>
<td>Pointer to the ED Log file (#230)</td>
<td>230.1^B ADF (#797)</td>
<td><p>Pointer field:</p>
<p>Points to an entry in the ED Log file; file entries record modifications (updates) to entries in the ED Log file</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>TIME</td>
<td></td>
<td>ADF (#797)</td>
<td><p>Time-and-date field: Contains the time and date of the log record’s last</p>
<p>modification (if the</p>
<p>patient’s log record was modified)</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>ENTERED BY</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Contains the identities of users who have updated log data</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>PATIENT NAME</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>The updated value of the patient’s name (if updated)</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>PATIENT SSN</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains the updated value of the patient’s social security number (if updated)</p>
<p>The class-three product recorded Social Security numbers when patients without DFNs came to the emergency room; EDIS is not currently using this field; the field is present for the sake of compatibility with the class-three version</p>
<p>Patients’ DFNs are their IENs in the Patient file (#2)</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>PATIENT ID</td>
<td>Pointer to the Patient file (#2)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the patient’s DFN (if updated)</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>COMPLAINT</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains the updated value of the patient’s display- board complaint (if updated)</p></td>
</tr>
<tr class="even">
<td>.0701</td>
<td>CLOSED</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<p>1 (Yes)</p>
<p>0 (No)</p></td>
</tr>
<tr class="odd">
<td>.071</td>
<td>CLOSED DATE/TIME</td>
<td></td>
<td>Triggered by the CLOSED field (.07)</td>
<td><p>Date-and-time field:</p>
<p>Contains the date/time when the log entry was ‘closed’.</p></td>
</tr>
<tr class="even">
<td>.072</td>
<td>CLOSED BY</td>
<td>Pointer to New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Contains the IEN of the user who closed the log entry.</p></td>
</tr>
<tr class="odd">
<td>.073</td>
<td>REMOVED IN ERROR</td>
<td></td>
<td></td>
<td><p>Set of codes: 1 (Yes)</p>
<p>This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.</p></td>
</tr>
<tr class="even">
<td>.074</td>
<td>RESTORED BY</td>
<td>Pointer to New Person file (#200)</td>
<td>Triggers RESTORED BY DATE/TIME</td>
<td><p>Pointer field:</p>
<p>Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.</p></td>
</tr>
<tr class="odd">
<td>.075</td>
<td>RESTORED BY DATE/TIME</td>
<td></td>
<td><p>Triggered by ‘RESTORED BY’</p>
<p>field (.074)</p></td>
<td><p>Date/Time:</p>
<p>This holds the date/time when the patient was ‘restored’ to the board.</p></td>
</tr>
<tr class="even">
<td>.08</td>
<td>TIME IN</td>
<td></td>
<td></td>
<td><p>Time-and-date field: Contains the updated value of the patient’s arrival time</p>
<p>(if updated)</p></td>
</tr>
<tr class="odd">
<td>.09</td>
<td>TIME OUT</td>
<td></td>
<td></td>
<td><p>Time-and-date field: Contains the updated value of the patient’s departure</p>
<p>time (if updated)</p></td>
</tr>
<tr class="even">
<td>.1</td>
<td>ARRIVAL MODE</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the source of the patient’s visit (a nursing home or hospital ward, for example—if updated)</p></td>
</tr>
<tr class="odd">
<td>.11</td>
<td>DISPOSITION</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the patient’s disposition (if updated)</p></td>
</tr>
<tr class="even">
<td>.12</td>
<td>DELAY</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated reason that the patient’s stay exceeded the maximum stay limit (if updated)</p></td>
</tr>
<tr class="odd">
<td>.14</td>
<td>CLINIC</td>
<td>Pointer to the Hospital Location file (#44)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the clinic location (if updated)</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>COMPLAINT (LONG)</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains the updated value of the patient’s long complaint (if updated)</p></td>
</tr>
<tr class="odd">
<td>3.2</td>
<td>STATUS</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the patient’s status (if updated)</p></td>
</tr>
<tr class="even">
<td>3.3</td>
<td>ACUITY</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the patient’s acuity (if updated)</p></td>
</tr>
<tr class="odd">
<td>3.4</td>
<td>LOC</td>
<td>Pointer to the Tracking Room-Bed file (#231.8)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the updated value of the patient’s room, bed, or area assignment (if updated)</p></td>
</tr>
<tr class="even">
<td>3.5</td>
<td>MD ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the identity of the patient’s updated emergency-department physician assignment (if updated)</p></td>
</tr>
<tr class="odd">
<td>3.6</td>
<td>NURSE ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s updated nurse assignment (if updated)</p></td>
</tr>
<tr class="even">
<td>3.7</td>
<td>RESIDENT ASSIGNED</td>
<td>Pointer to the New Person file (#200)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the patient’s updated resident assignment (if updated)</p></td>
</tr>
<tr class="odd">
<td>3.8</td>
<td>COMMENT</td>
<td></td>
<td></td>
<td><p>Free-text field Contains updated</p>
<p>comments associated with</p>
<p>the patient’s emergency- department visit (if any— comments are optional)</p></td>
</tr>
<tr class="even">
<td>9.1</td>
<td>MODIFIED FIELDS</td>
<td></td>
<td></td>
<td><p>Free text field:</p>
<p>Contains a list of fields that users modified in the corresponding ED LOG record at the time of the update; the list contains field numbers and is semicolon delimited</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark12" class="anchor"></span>Table 11: XE File Record Indices (#230.1)

#### Record Indices for File (#230.1)

<table>
<caption><p><span id="_bookmark13" class="anchor"></span>Table 12: XE Files – Tracking Staff (#231.7)</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Record Index</p>
</blockquote></th>
<th><blockquote>
<p>Indexed Fields</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADF (#797)</td>
<td>LOG, TIME, IEN</td>
<td>This index provides a forward- chronological list of updates to the log record of a single entry in the ED Log file.</td>
</tr>
</tbody>
</table>

<span id="_bookmark13" class="anchor"></span>Table 12: XE Files – Tracking Staff (#231.7)

#### Tracking Staff (#231.7)

The Tracking Staff file contains staff assignments for particular areas (currently sites’ emergency departments). It allows for concise staff -selection lists and enables sites to associate colors with staff members so that emergency-department personnel can more easily tell which staff members are assigned to which patients.

<table>
<caption><p><span id="_bookmark14" class="anchor"></span>Table 13: XE Files Record Indices (#231.7)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross Reference</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>PERSON</td>
<td>Pointer to the New Person file (#200)</td>
<td>231.7^B AD (#807)</td>
<td><p>Pointer field:</p>
<p>Points to the identity of a person who is assigned to work as staff in the emergency department (required)</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>INSTITUTION</td>
<td>Pointer to the Institution file (#4)</td>
<td><p>AC (#800)</p>
<p>AD (#807)</p></td>
<td><p>Pointer field:</p>
<p>Points to entries in the Institution file (#4); allows each station to have its own set of staff assignments</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>AREA</td>
<td>Pointer to the Tracking Area file (#231.9)</td>
<td><p>AC (#800)</p>
<p>AD (#807)</p></td>
<td><p>Pointer field: Points to the area to which the person is</p>
<p>assigned as staff</p>
<p>EDIS currently supports only emergency departments but is capable of supporting other areas in the future</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>INACTIVE</td>
<td></td>
<td>AD (#800)</td>
<td><p>A setting: 0 (active)</p>
<p>1 (inactive)</p>
<p>A setting of <em>1</em> indicates that the person is no longer an active staff member in the associated area</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>LOCAL ID</td>
<td></td>
<td></td>
<td>Free-text</td>
</tr>
<tr class="even">
<td>.06</td>
<td>ROLE</td>
<td><p>Pointer to the TRACKING</p>
<p>STAFF file (#232.5)</p></td>
<td>AC(#873)</td>
<td><p>Pointer field:</p>
<p>Points to the role in the CPE ROLE file.</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>INITIALS</td>
<td></td>
<td></td>
<td><p>Free-text:</p>
<p>This is the user’s initials.</p></td>
</tr>
<tr class="even">
<td>.08</td>
<td>COLOR</td>
<td></td>
<td></td>
<td><p>Free-text field: Contains red-green-blue (RGB) values for the</p>
<p>foreground and</p>
<p>background colors (if any) that sites have used to highlight the staff member’s identifier on the display board</p>
<p>Colors are hexadecimal; this field accepts values having the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff)</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark14" class="anchor"></span>Table 13: XE Files Record Indices (#231.7)

#### Record Indices for File (#231.7)

<table>
<caption><p><span id="_bookmark15" class="anchor"></span>Table 14: XE Files – Tracking Room Bed (#231.8)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Record Index</p>
</blockquote></th>
<th><blockquote>
<p>Indexed Fields</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AC (#871)</td>
<td>SITE, AREA, ROLE, IEN</td>
<td>This cross reference supports constructing a list of currently active staff for a particular role.</td>
</tr>
<tr class="even">
<td>AD (#872)</td>
<td>SITE, AREA, DUZ, IEN</td>
<td>This cross reference allows searching the file for an entry matching a particular DUZ (say, to look up a color map). Since a person may work as staff in multiple areas, this cross reference allows finding the staff record that applies to the person's activity in a specific area.</td>
</tr>
</tbody>
</table>

<span id="_bookmark15" class="anchor"></span>Table 14: XE Files – Tracking Room Bed (#231.8)

#### Tracking Room-Bed (#231.8)

As patients progress through their visits, they may stop at a number of areas. The Tracking Room-Bed file allows sites to set up these areas in EDIS so that they can track patients throughout their visits. Areas can be physical or conceptual, and may include specific beds, waiting areas, and other areas of the hospital (radiology, exam rooms, and so forth).

<table>
<caption><p><span id="_bookmark16" class="anchor"></span>Table 15: XE Files – Record Indices (#231.8)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References and Record Indices</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>231.8^B</td>
<td>Free-text field (required): The internal name of the room, bed, or area that the patient is occupying at this stage of his visit</td>
</tr>
<tr class="even">
<td>.02</td>
<td>INSTITUTION</td>
<td>Pointer to Institution file (#4)</td>
<td><p>AC (#802)</p>
<p>C (#803)</p></td>
<td><p>Pointer field:</p>
<p>Allows each station (division, for example) to manage its own set of rooms, beds, and areas</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>AREA</td>
<td>Pointer to the Tracking Area file (#231.9)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the hospital area associated with this room, bed, or area; EDIS currently supports only the emergency department, but will probably support additional areas in the future</p>
<p>Trainers can use this field to set up separate areas for each trainee, allowing each trainee to configure his or her own set of rooms and beds</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>INACTIVE</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (active)</p></li>
<li><p>1 (inactive)</p></li>
</ul>
<p>A setting of <em>1</em> makes the associated room or area unavailable for selection in EDIS; however, inactive rooms and areas still appear on reports and in views for previous entries</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>SEQUENCE</td>
<td></td>
<td></td>
<td><p>A number:</p>
<p>Represents the sequential order in which EDIS should display the associated room or area on the big board display; the field accepts numbers from one (1) to 9999</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>DISPLAY NAME</td>
<td></td>
<td>AC (#802)</td>
<td><p>Free-text field:</p>
<p>Contains the name of the room or area as it should appear on the big board display; display names should be concise to save display-board space; supports names from 1–30 characters in length</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>DISPLAY WHEN</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (occupied)</p></li>
<li><p>1 (always)</p></li>
<li><p>(never)</p></li>
</ul>
<p>A setting of 0, 1, or 2 determines whether EDIS should display the associated room or area when occupied, always, or never, respectively</p></td>
</tr>
<tr class="even">
<td>.08</td>
<td>DEFAULT STATUS</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the default status (if any) of the room, bed, or area; when sites select a default status for a room, bed, or area, EDIS automatically assigns this default status to patients who are occupying the room, bed, or area</p></td>
</tr>
<tr class="odd">
<td>.09</td>
<td>MULTIPLE ASSIGN</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (single—accepts one patient assignment at a time)</p></li>
<li><p>1 (multiple—accepts multiple simultaneous patient assignments)</p></li>
<li><p>2 (waiting—a special case of the multiple-assignments designation for reporting)</p></li>
<li><p>3 (single, non-ED—single- assignment designation in an area outside the emergency department)</p></li>
<li><p>4 (multiple, non-ED— multiple-assignment designation in an area outside the emergency department)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>.1</td>
<td>SHARED NAME</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains a common name for several beds or areas that share the same physical space; using a shared name in such cases allows sites to run reports that identify patients and staff who are at risk for exposure to contagious organisms</p></td>
</tr>
<tr class="odd">
<td>.11</td>
<td>BOARD</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains the name of the particular display board on which the room or area is to appear</p></td>
</tr>
<tr class="even">
<td>.12</td>
<td>COLOR</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Contains values for colors; allows sites to map specific rooms and areas to particular foreground and background colors for use with the display-board’s room-bed-area list; this field accepts values that have the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff)</p></td>
</tr>
<tr class="odd">
<td>.13</td>
<td>PRIMARY</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – Primary</p></li>
<li><p>‘2’ – Secondary</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_bookmark16" class="anchor"></span>Table 15: XE Files – Record Indices (#231.8)

#### Record Indices for (#231.8)

<table>
<caption><p><span id="_bookmark17" class="anchor"></span>Table 16: XE Files – Tracking Area (#231.9)</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Record Index</p>
</blockquote></th>
<th><blockquote>
<p>Indexed Fields</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AC (#873)</td>
<td>SITE, AREA, DISPLAYNAME, IEN</td>
<td>Allows looking for a room with a specific abbreviation, such as AMBU or WAIT (when setting baseline parameters for example).</td>
</tr>
<tr class="even">
<td>C (#874)</td>
<td>INSTITUTION, AREA</td>
<td>Allows collecting all of the rooms for a specific area within a division (station number).</td>
</tr>
</tbody>
</table>

<span id="_bookmark17" class="anchor"></span>Table 16: XE Files – Tracking Area (#231.9)

#### Tracking Area (#231.9)

This file contains parameters that control EDIS’s tracking behavior. It also contains XML descriptions that client software uses to control display -board column appearance, row content, and cell color. The AREA field (#.03) of the ED Log files (#230) points to this file.

<table>
<caption><p><span id="_Toc54254136" class="anchor"></span>Table 17: XE Files Display Board Configuration Subfile</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References and Record Indices</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>231.9^B</td>
<td><p>Free-text field</p>
<p>Contains the name of an area within the hospital; EDIS currently supports only sites’ emergency department areas</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>INSTITUTION</td>
<td>Pointer to Institution file (#4)</td>
<td>231.9^C</td>
<td><p>A pointer field:</p>
<p>Allows each station within a given VistA system to have its own set of areas</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>LAST UPDATE</td>
<td></td>
<td></td>
<td>Date-and-time field: Contains the date and time that the site last updated the display-board configuration; this helps client software determine if it is necessary to reload configuration parameters</td>
</tr>
<tr class="even">
<td>1.1</td>
<td>DIAGNOSIS REQUIRED</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no)</p></li>
<li><p>1 (yes)</p></li>
</ul>
<p>A setting of <em>1</em> indicates that users must enter diagnoses before removing patients from the display board</p></td>
</tr>
<tr class="odd">
<td>1.11</td>
<td>AMBULANCE</td>
<td>Pointer to Tracking Room-Bed file (#231.8)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the entry in the Tracking Room-Bed file that represents an arriving ambulance</p></td>
</tr>
<tr class="even">
<td>1.12</td>
<td>INITIAL ROOM</td>
<td>Pointer to Tracking Room-Bed file (231.8)</td>
<td></td>
<td><p>Pointer field:</p>
<p>Points to the tracking-file entry that specifies the default room or area (often the waiting room) to which patients are first assigned</p></td>
</tr>
<tr class="odd">
<td>1.2</td>
<td>CODED DIAGNOSIS</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no—free-text)</p></li>
<li><p>1 (yes—ICD-10-CM</p></li>
</ul>
<p>A setting of <em>1</em> indicates that users must enter diagnoses using ICD-10-CM codes before removing patients from the board; otherwise, users may enter free-text diagnoses.</p></td>
</tr>
<tr class="even">
<td>1.3</td>
<td>DISPOSITION REQUIRED</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no)</p></li>
<li><p>1 (yes)</p></li>
</ul>
<p>A setting of <em>1</em> indicates that users must enter patients’ dispositions before removing them from the display board</p></td>
</tr>
<tr class="odd">
<td>1.4</td>
<td>DELAY REQUIRED</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no)</p></li>
<li><p>1 (yes)</p></li>
</ul>
<p>For patients whose emergency-department stays have exceeded the number of minutes identified in the DELAY MINUTES field</p>
<p>(#1.5), unless patients are admitted to an observation ward, a setting of <em>1</em> indicates that users must select a reason for delay before removing the patients from the display board</p></td>
</tr>
<tr class="even">
<td>1.5</td>
<td>DELAY MINUTES</td>
<td></td>
<td></td>
<td><p>Number field:</p>
<p>Contains the number of minutes after which EDIS requires a reason for delay as a precondition for removing patients from the display board; accepts whole numbers between 1 and 1440</p></td>
</tr>
<tr class="odd">
<td>1.6</td>
<td>FIRST SHIFT START</td>
<td></td>
<td></td>
<td><p>Number field:</p>
<p>Contains the number of minutes from midnight to the first shift’s starting time; accepts whole numbers between 0 and 1440; EDIS currently assumes that all shifts are of equal length</p></td>
</tr>
<tr class="even">
<td>1.7</td>
<td>SHIFT DURATION</td>
<td></td>
<td></td>
<td><p>Number field:</p>
<p>Contains the number of minutes that comprise the duration of a shift; accepts whole numbers between 0 and 1440; for eight-hour shifts, the value recorded in this field will be 480 (8*60)</p></td>
</tr>
<tr class="odd">
<td>1.8</td>
<td>PROMPT RESIDENTS</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no)</p></li>
<li><p>1 (yes)</p></li>
</ul>
<p>A setting of <em>1</em> indicates that the application must prompt users to enter resident assignments (in addition to provider assignments)</p></td>
</tr>
<tr class="even">
<td>1.9</td>
<td>PROMPT CLINICS</td>
<td></td>
<td></td>
<td><p>A setting:</p>
<ul>
<li><p>0 (no)</p></li>
<li><p>1 (yes)</p></li>
</ul>
<p>A setting of <em>1</em> (yes) indicates that the application must prompt users to select a clinic; this allows EDIS to create visits based on explicitly selected clinics</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>COLOR SPEC</td>
<td></td>
<td></td>
<td>Word-processing field (#231.93) (no wrap): Contains an XML document that maps colors to display-board values</td>
</tr>
<tr class="even">
<td>4</td>
<td>DISPLAY BOARD CONFIG</td>
<td><p>Multiple</p>
<p>#231.94</p></td>
<td></td>
<td>Contains an XML description of each display board’s definition</td>
</tr>
<tr class="odd">
<td>230.1</td>
<td>TRACKING UPDATED</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>This timestamp is set whenever the data that is shown on any display board for an area has been updated.</p></td>
</tr>
<tr class="even">
<td>231.1</td>
<td>CHOICES UPDATED</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>This is a timestamp that is set whenever the definition of any display board for a given area has been modified.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54254136" class="anchor"></span>Table 17: XE Files Display Board Configuration Subfile

#### Display Board Configuration Subfile (231.94)

<table>
<caption><p><span id="_Toc54254137" class="anchor"></span>Table 18: Files and Fields that Point to Tracking Code File</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross Reference</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>231.94^B</td>
<td><p>Free-text field:</p>
<p>Contains the name of a specific display board</p></td>
</tr>
<tr class="even">
<td>1</td>
<td>SPEC</td>
<td></td>
<td></td>
<td><p>Word-processing field #231.941 (no wrap):</p>
<p>Contains the XML description for a specific display board</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54254137" class="anchor"></span>Table 18: Files and Fields that Point to Tracking Code File

#### Tracking Code (#233.1)

The Tracking Code file contains entries that EDIS tracking functionality uses in selection lists. The software may eventually roll up selection-list entries to the emergency-department director for reporting.

The following files point to the Tracking Code file:

| File Name                       | Field                                            |
|---------------------------------|--------------------------------------------------|
| ED Log file (#230)              | ARRIVAL MODE field (#.1)                         |
| ED Log file                     | DELAY REASON field (#1.2)                        |
| ED Log file                     | STATUS field (#3.2)                              |
| ED Log file                     | ACUITY field (#3.3)                              |
| ED Log History file (#230.1)    | ARRIVAL MODE field (#.1)                         |
| ED Log History file             | DISPOSITION field (#.11)                         |
| ED Log History file             | DELAY field (#.12)                               |
| ED Log History file             | STATUS field (#3.2)                              |
| ED Log History file             | ACUITY field (#3.3)                              |
| Tracking Room-Bed file (#233.1) | DEFAULT STATUS field (#.08)                      |
| Tracking Code file (#233.1)     | NATIONAL CODE field (#.04)                       |
| Tracking Code Set (#233.2)      | CODE field (#.02) of the CODES subfield (233.21) |

<span id="_Toc54254138" class="anchor"></span>Table 19: Tracking Code (#233.1)

<table>
<caption><p><span id="_Toc54254139" class="anchor"></span>Table 20: Tracking Code File Indices (#233.1)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.1^B</td>
<td><p>Free-text field: Contains unique names for values in the selection lists that EDIS is using.</p>
<p>To distinguish local list selections from national list selections, EDIS prefixes locally defined entries with sites’ station numbers and nationally defined entries with the letters <em>edp</em></p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>DISPLAY NAME</td>
<td></td>
<td><p>AB (#804)</p>
<p>AC (#805)</p></td>
<td>Free text field: Contains the selection’s display-board name</td>
</tr>
<tr class="odd">
<td>.03</td>
<td>ABBREVIATION</td>
<td></td>
<td>AB (#804)</td>
<td>Free-text field: Contains display-name abbreviations that EDIS uses in some reports</td>
</tr>
<tr class="even">
<td>.04</td>
<td>NATIONAL CODE</td>
<td>Pointer to Tracking Code file (#233.1)</td>
<td></td>
<td>Free-text field: Will contain mappings from site-defined codes to national codes when national codes exist.</td>
</tr>
<tr class="odd">
<td>.05</td>
<td>FLAGS</td>
<td></td>
<td></td>
<td><p>EDIS uses flags to further classify specific codes; possible flags are:</p>
<ul>
<li><p>M (Missed opportunity)</p></li>
<li><p>A (Admission)</p></li>
<li><p>VA (VA admission)</p></li>
<li><p>O (Observation)</p></li>
</ul>
<p>EDIS allows multiple flags with no delimiters.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>DESCRIPTION</td>
<td></td>
<td></td>
<td><p>Word processing field (#233.12):</p>
<p>Contains a further explanation: allows sites to further explain codes (233.12)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54254139" class="anchor"></span>Table 20: Tracking Code File Indices (#233.1)

#### Tracking Code File Indices (#233.1)

<table>
<caption><p><span id="_bookmark21" class="anchor"></span>Table 21: Tracking Code Set (#233.2)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 23%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Record Index</p>
</blockquote></th>
<th><blockquote>
<p>Indexed Fields</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AB (#875)</td>
<td>NAME (without prefix), ABBREVIATION</td>
<td>This allows finding all the abbreviations for a name without regard to the site prefix. (The prefix is "edp." when nationally exported, "nnn." for locally defined, where nnn is the station number.)</td>
</tr>
<tr class="even">
<td>AC (#876)</td>
<td>NAME (without prefix), DISPLAY NAME</td>
<td>This allows finding all the display names for a name without regard to the site prefix. (The prefix is "edp." when nationally exported, "nnn." for locally defined, where nnn is the station number.)</td>
</tr>
</tbody>
</table>

<span id="_bookmark21" class="anchor"></span>Table 21: Tracking Code Set (#233.2)

#### Tracking Code Set (#233.2)

The Tracking Code Set file contains collections of codes that represent specific selection lists (acuities, patient statuses, dispositions, delay reasons, and so forth) used within EDIS.

<table>
<caption><p><span id="_bookmark22" class="anchor"></span>Table 22: Subfile – Tracking Code Set File – Codes (#233.21)</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.2^B</td>
<td><p>Free-text field (required): Contains the names of tracking code sets that</p>
<p>EDIS uses in selection</p>
<p>lists; sites may modify selection lists to meet their needs</p></td>
</tr>
<tr class="even">
<td>1</td>
<td>CODES</td>
<td>Multiple (#233.21)</td>
<td></td>
<td>Contains lists of codes that are available in selection lists</td>
</tr>
</tbody>
</table>

<span id="_bookmark22" class="anchor"></span>Table 22: Subfile – Tracking Code Set File – Codes (#233.21)

#### Codes (233.21)

<table>
<caption><p><span id="_bookmark23" class="anchor"></span>Table 23: CPE Role (#232.5)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>SEQUENCE</td>
<td></td>
<td>233.21^B</td>
<td><p>Number field (multiply asked):</p>
<p>Contains a number that indicates the order in which the associated code should appear in the selection list; accepts whole numbers between 1 and 9999</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>CODE</td>
<td>Pointer to the Tracking Code file (#233.1)</td>
<td>233.2^AS^MUMPS</td>
<td><p>Pointer field:</p>
<p>Points to codes that are to be included in selection lists</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>INACTIVE</td>
<td></td>
<td></td>
<td><p>A setting: 1 (inactive)</p>
<p>0 (active)</p>
<p>A setting of <em>1</em> indicates codes that are temporarily inactivated</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>NAME AT SITE</td>
<td></td>
<td>233.2^AS^MUMPS</td>
<td><p>Free-text field: Contains site-specific names; allows sites to</p>
<p>use different names for</p>
<p>display purposes without changing underlying national codes</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>ABBREVIATION AT SITE</td>
<td></td>
<td>233.2^AS^MUMPS</td>
<td><p>Free-text field: Contains site-specific abbreviations: allows</p>
<p>sites to use different</p>
<p>abbreviations for national-code abbreviations without changing the underlying meaning of the national codes</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark23" class="anchor"></span>Table 23: CPE Role (#232.5)

#### CPE Role (#232.5)

The CPE Role file contains the definitions for roles to be used with EDIS.

<table>
<caption><p><span id="_bookmark24" class="anchor"></span>Table 24: EDP Worksheet Specification (#232.6)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Field Number</p>
</blockquote></th>
<th><blockquote>
<p>Field Name</p>
</blockquote></th>
<th><blockquote>
<p>Pointers</p>
</blockquote></th>
<th><blockquote>
<p>Cross References</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>ROLE</td>
<td>USR CLASS (#8930)</td>
<td>232.5^B</td>
<td><p>Pointer to the USR CLASS file This field contains the role used for the clinical practice environment.</p>
<p>Clerk, Nurse, Provider &amp; Resident</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>ABBREVIATION</td>
<td></td>
<td>232.5^C</td>
<td><p>Free text (Required)</p>
<p>This index holds the abbreviation as well as the IEN for each role.</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>XML ABBREVIATION</td>
<td></td>
<td></td>
<td><p>Free text (Required) This is the xml abbreviation for the role. Previously, logic had been hardcoded to check the role type.</p>
<p>'P' = "@md" 'N' =</p>
<p>"@rn" 'R' = "@res"</p>
<p>These values will remain the same. However, they are now part of the file and can be more easily enhanced to add roles in the future. The roles will now be able to be built without having to release a KIDS build to do so. All role settings are now table-driven. This is accessed and used to build information out of the CLRSTAFF tag in EDPQDBS.</p>
<p>Any time a new role is added, the UI will need to change to be able to consume the new role type. In addition to this field, the XML ROLE NAME will need to be entered in order to pass the needed information back to the client application. There is flexibility in the use of these two fields. However, they MUST be defined when creating a new role. For example: Currently, for the role of 'Provider', the XML ABBREVIATION field is "@md", and the XML ROLE NAME is 'providers'. As long as these fields are unique to this role, the API's will build meaningful information for the client to consume.</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>DEFAULT WORKSHEET</td>
<td><p>Pointer to EDP WORKSHEET SPECIFICATION</p>
<p>file (#232.6)</p></td>
<td></td>
<td><p>Point to the EDP WORKSHEET SPECIFICATIO</p>
<p>N file</p>
<p>This is the default worksheet for this role.</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>DEFAULT BOARD</td>
<td></td>
<td></td>
<td><p>Free Text:</p>
<p>This contains the name of the default board for this role.</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>ALLOW ACUITY EDIT</td>
<td></td>
<td></td>
<td><p>Set of codes: ‘0’ – No</p>
<p>‘1’ – Yes</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>XML STAFF NAME</td>
<td></td>
<td></td>
<td><p>Free Text:</p>
<p>This holds the staff name that is related to building the XML needed for the client portion of the application. This is built from the LOAD tag in EDPBST.</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark24" class="anchor"></span>Table 24: EDP Worksheet Specification (#232.6)

#### EDP Worksheet Specification (#232.6)

The EDP Worksheet Specification file holds worksheet definitions for each institution/area. The EDP Worksheet Specification file also allows worksheets to be associated with user roles.

<table>
<caption><p><span id="_Toc54254144" class="anchor"></span>Table 25: Subfile – Sections (#232.62)</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.6^B</td>
<td><p>Free-text field (required):</p>
<p>Contains the names of worksheets to be used with EDIS.</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>INSTITUTION</td>
<td>INSTITUTION (#4)</td>
<td>232.6^C</td>
<td><p>Pointer to the INSTITUTION file:</p>
<p>Contains the institution associated with this worksheet.</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>AREA</td>
<td>TRACKING AREA (#231.9)</td>
<td></td>
<td><p>Pointer to the TRACKING AREA</p>
<p>file:</p>
<p>The tracking area associated with this worksheet.</p></td>
</tr>
<tr class="even">
<td>.04</td>
<td>TYPE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘V’ for Visit</p></li>
<li><p>‘A’ for Assess</p></li>
<li><p>‘P’ for Plan</p></li>
<li><p>‘E’ for Edit Closed</p></li>
</ul>
<p>This is the type of this worksheet.</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>ROLE</td>
<td>USR CLASS (#8930)</td>
<td></td>
<td><p>Pointer to the USR CLASS file Identifies the role</p>
<p>associated with this</p>
<p>worksheet.</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>DISABLED</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>0 – False</p></li>
<li><p>1 – True</p></li>
</ul>
<p>This indicates whether this worksheet is disabled or not.</p></td>
</tr>
<tr class="odd">
<td>.07</td>
<td>EDITABLE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ – False</p></li>
</ul></td>
</tr>
<tr class="even">
<td>1</td>
<td>SPEC</td>
<td></td>
<td></td>
<td>Word Processing (NOWRAP)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>SECTIONS</td>
<td><p>Multiple</p>
<p>#232.62</p></td>
<td></td>
<td>This multiple holds ‘instances’ of the sections from the EDP WORKSHEET SECTION file. Each instance is tied to the worksheet so that its behavior can change on a case by case basis.</td>
</tr>
</tbody>
</table>

<span id="_Toc54254144" class="anchor"></span>Table 25: Subfile – Sections (#232.62)

#### Subfile: Sections (#232.62)

<table>
<caption><p><span id="_Toc54254145" class="anchor"></span>Table 26: Subfile – Components (#232.622)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>SECTION SEQUENCE</td>
<td></td>
<td></td>
<td>Number</td>
</tr>
<tr class="even">
<td>.02</td>
<td>SECTION</td>
<td>Pointer to EDP Worksheet Section file (#232.71)</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>INITIALLY OPEN</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘0’ – False</p></li>
<li><p>‘1’ - True</p></li>
</ul></td>
</tr>
<tr class="even">
<td>1</td>
<td>CONFIGURATION</td>
<td></td>
<td></td>
<td>Word Processing (NOWRAP)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>COMPONENTS</td>
<td><p>Multiple to</p>
<p>#232.622</p></td>
<td></td>
<td><p>The component multiple points to the EDP WORKSHEET</p>
<p>COMPONENTS file as an 'instance' of the component. This holds specific behavioral flags for this component, as it exists within this worksheet/section.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54254145" class="anchor"></span>Table 26: Subfile – Components (#232.622)

#### Subfile: Components (#232.622)

<table>
<caption><p><span id="_Toc54254146" class="anchor"></span>Table 27: Subfile – Roles (#232.63)</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>COMPONENT SEQUENCE</td>
<td></td>
<td>232.66^B</td>
<td>Number</td>
</tr>
<tr class="even">
<td>.02</td>
<td>COMPONENT</td>
<td>Pointer to EDP Worksheet Component file (#232.72)</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>EDITABLE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ - False</p></li>
</ul></td>
</tr>
<tr class="even">
<td>.04</td>
<td>VISIBLE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ - False</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>INCLUDE IN SUMMARY</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ - False</p></li>
</ul></td>
</tr>
<tr class="even">
<td>3</td>
<td>ROLES</td>
<td><p>Pointer to Multiple</p>
<p>#232.63</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc54254146" class="anchor"></span>Table 27: Subfile – Roles (#232.63)

#### Subfile: Roles (#232.63)

| Field Number | Field Name | Pointers                          | Cross References | Description |
|--------------|------------|-----------------------------------|------------------|-------------|
| .01          | Roles      | Pointer to CPE Role File (#232.5) |                  |             |

<span id="_bookmark25" class="anchor"></span>Table 28: EDP Worksheet Section (#232.71)

#### EDP Worksheet Section (#232.71)

The Worksheet Section file holds the definitions for each section of a worksheet.

<table>
<caption><p><span id="_Toc54254148" class="anchor"></span>Table 29: Subfile – Components (#232.711)</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.71^B</td>
<td><p>Free-text field (required):</p>
<p>This field holds the name of the worksheet section.</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>PACKAGE</td>
<td></td>
<td>C (#891)</td>
<td><p>Free-text field:</p>
<p>Holds the package information</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>SUMMARY PLUGIN</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>.04</td>
<td>DEFAULT DISPLAY NAME</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>.05</td>
<td>TASK TYPE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘0’ – None</p></li>
<li><p>‘1’ – Checkbox</p></li>
<li><p>‘2’ – Timed</p></li>
</ul>
<p>This field contains the ‘type’ associated with this worksheet.</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>INITIALLY OPEN</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>0 – False</p></li>
<li><p>1 – True</p></li>
</ul>
<p>This indicates whether or not the worksheet section should be open or closed initially.</p></td>
</tr>
<tr class="odd">
<td>1</td>
<td>COMPONENTS</td>
<td><p>Multiple (232.711)</p>
<p>Pointer to EDP WORKSHEET COMPONENT</p>
<p>file (#232.72)</p></td>
<td></td>
<td><p>Pointer to EDP WORKSHEET COMPONENT (#232.72) file:</p>
<p>This field holds the components that will be used in this worksheet section.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>ROLES</td>
<td>Pointer to multiple (#232.712)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc54254148" class="anchor"></span>Table 29: Subfile – Components (#232.711)

#### Subfile: Components (#232.711)

| Field Number | Field Name | Pointers                                          | Cross References | Description |
|--------------|------------|---------------------------------------------------|------------------|-------------|
| .01          | COMPONENT  | Pointer to EDP Worksheet Component file (#232.72) |                  |             |
| .02          | ROLES      | Pointer to multiple (#232.712)                    |                  |             |

<span id="_Toc54254149" class="anchor"></span>Table 30: Subfile – Roles (#232.712)

#### Subfile: Roles (#232.712)

| Field Number | Field Name | Pointers                          | Cross References | Description |
|--------------|------------|-----------------------------------|------------------|-------------|
| .01          | ROLES      | Pointer to CPE ROLE FILE (#232.5) |                  |             |

<span id="_bookmark26" class="anchor"></span>Table 31: EDP Worksheet Component (#232.72)

#### EDP Worksheet Component (#232.72)

The Worksheet Component file holds the definition for each worksheet component.

<table>
<caption><p><span id="_Toc54254151" class="anchor"></span>Table 32: Subfile – Parameters (#232.725)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>232.72^B</td>
<td><p>Free-text field (required):</p>
<p>Indicates the name of the worksheet component.</p></td>
</tr>
<tr class="even">
<td>.02</td>
<td>LABEL</td>
<td></td>
<td>C (#892)</td>
<td><p>Free-text field (required):</p>
<p>This holds the label for the worksheet component.</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>DATA PROVIDER</td>
<td></td>
<td></td>
<td>Free-text Computed field: PACKAGE::CLASS</td>
</tr>
<tr class="even">
<td>.04</td>
<td>TYPE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘R’ – Reference</p></li>
<li><p>‘V’ - Visit</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>MONIKER</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>Unknown purpose</p></td>
</tr>
<tr class="even">
<td>.06</td>
<td>WIDGET NAME</td>
<td><p>Pointer to EDP Worksheet Component Type file</p>
<p>#232.73</p></td>
<td></td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>.07</td>
<td>PACKAGE LINK</td>
<td><p>Pointer to Package file</p>
<p>#9.4</p></td>
<td></td>
<td>Pointer</td>
</tr>
<tr class="even">
<td>.08</td>
<td>VALUE</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>.09</td>
<td>SUMMARY LABEL</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>.1</td>
<td>SUMMARY ORDER</td>
<td></td>
<td></td>
<td>NUMBER</td>
</tr>
<tr class="odd">
<td>.11</td>
<td>AVAILABLE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ – False</p></li>
</ul></td>
</tr>
<tr class="even">
<td>.12</td>
<td>VISIBILITY TRIGGER</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>1.1</td>
<td>ASSOCIATED FILE</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>1.2</td>
<td>ASSOCIATED FIELD</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>1.3</td>
<td>LOAD EVENT</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>2.1</td>
<td>LOAD API</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>2.2</td>
<td>SAVE API</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>3</td>
<td>ALTERNATE LOAD LOGIC</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>3.1</td>
<td>PREVIEW TAG</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>3.2</td>
<td>PREVIEW ROUTINE</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>4</td>
<td>ALTERNATE SAVE LOGIC</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>5</td>
<td>PARAMETERS</td>
<td>Multiple (#232.725)</td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="odd">
<td>6</td>
<td>DEFAULT VALUE</td>
<td></td>
<td></td>
<td>Free-text field</td>
</tr>
<tr class="even">
<td>7</td>
<td>REQUIRED COMPONENTS</td>
<td><p>Multiple to</p>
<p>#232.727</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>8</td>
<td>ROLES</td>
<td><p>Pointer to</p>
<p>#232.728</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>VALIDATOR</td>
<td><p>Pointer to</p>
<p>#232.729</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc54254151" class="anchor"></span>Table 32: Subfile – Parameters (#232.725)

#### Subfile: Parameters (#232.725)

<table>
<caption><p><span id="_Toc54254152" class="anchor"></span>Table 33: Subfile – Components (#232.727)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>PARAMETER NAME</td>
<td></td>
<td>232.725^B</td>
<td>Free-text field:</td>
</tr>
<tr class="even">
<td>1</td>
<td>DATA TYPE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘S’ – String</p></li>
<li><p>‘N’ - Numeric</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>2</td>
<td>SAVE/LOAD TYPE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘S’ – For save only</p></li>
<li><p>‘L’ - For load only</p></li>
<li><p>‘B’ – For both load and save</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc54254152" class="anchor"></span>Table 33: Subfile – Components (#232.727)

#### Subfile: Components (#232.727)

| Field Number | Field Name          | Pointers | Cross References | Description     |
|--------------|---------------------|----------|------------------|-----------------|
| .01          | REQUIRED COMPONENTS |          | 232.727^B        | Free-text field |

<span id="_Toc54254153" class="anchor"></span>Table 34: Subfile – Roles (#232.728)

#### Subfile: Roles (#232.728)

| Field Number | Field Name | Pointers                          | Cross References | Description     |
|--------------|------------|-----------------------------------|------------------|-----------------|
| .01          | ROLES      | Pointer to CPE ROLE FILE (#232.5) | 232.727^B        | Free-text field |

<span id="_Toc54254154" class="anchor"></span>Table 35: Subfile – Validator (#232.729)

#### Subfile: Validator (#232.729)

<table>
<caption><p><span id="_Toc54254155" class="anchor"></span>Table 36: EDP Worksheet Component Type (#232.73)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross References</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>VALIDATOR NAME</td>
<td>Pointer to EDP COMPONENT VALIDATORS (#232.74)</td>
<td>232.727^B</td>
<td>Free-text field:</td>
</tr>
<tr class="even">
<td>.02</td>
<td>PROPERTY</td>
<td></td>
<td></td>
<td><p>Set of codes: ‘1’ - text</p>
<p>‘2’ - selectedIndex</p>
<p>‘3’ - _SelectedDate</p></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>MAX LENGTH</td>
<td></td>
<td></td>
<td>Number</td>
</tr>
<tr class="even">
<td>.04</td>
<td>REQUIRED</td>
<td></td>
<td></td>
<td><p>Set of codes: ‘1’ – true</p>
<p>‘0’ – false</p></td>
</tr>
<tr class="odd">
<td>.05</td>
<td>MIN VALUE</td>
<td></td>
<td></td>
<td>Free-text</td>
</tr>
<tr class="even">
<td>.06</td>
<td>LOWER THAN MIN ERROR</td>
<td></td>
<td></td>
<td>Free-text</td>
</tr>
</tbody>
</table>

<span id="_Toc54254155" class="anchor"></span>Table 36: EDP Worksheet Component Type (#232.73)

#### EDP Worksheet Component Type (#232.73)

| Field Number | Field Name | Pointers | Cross References | Description                 |
|--------------|------------|----------|------------------|-----------------------------|
| .01          | NAME       |          | 232.73^B         | Free-text field (Required): |

<span id="_bookmark27" class="anchor"></span>Table 37: NHAMCS Reason for Visit (#233.8)

#### NHAMCS Reason for Visit (#233.8)

The NHAMCS Reason for visit file holds reasons for visits.

<table>
<caption><p><span id="_bookmark28" class="anchor"></span>Table 38: NHAMCS Reason for Visit Display (#233.81)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.8^B</td>
<td><p>Free-text field (required):</p>
<p>Contains the name of the reason for visit</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>CODE</td>
<td></td>
<td>233.8^C</td>
<td><p>Free-text field (required):</p>
<p>The code value associated with this reason for visit.</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>PARENT CODE</td>
<td>NHAMCS REASON FOR VISIT (233.8)</td>
<td></td>
<td><p>Pointer to NHAMCS REASON FOR VISIT FILE:</p>
<p>Holds the parent visit code (if this is a child code).</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark28" class="anchor"></span>Table 38: NHAMCS Reason for Visit Display (#233.81)

#### NHAMCS Reason for Visit Display (#233.81)

The NHAMCS Reason for Visit display file contains the display for an entry in the NHAMCS Reason for Visit file.

<table>
<caption><p><span id="_bookmark29" class="anchor"></span>Table 39: ED Complaint (#233.82)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td><p>233.81^B</p>
<p>233.81^D</p></td>
<td><p>Free-text field (required):</p>
<p>Contains the name of the reason for visit display.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>NHAMCS CODE</td>
<td>NHAMCS REASON FOR VISIT (233.8)</td>
<td>233.81^C</td>
<td>Pointer to NHAMCS REASON FOR VISIT file.</td>
</tr>
</tbody>
</table>

<span id="_bookmark29" class="anchor"></span>Table 39: ED Complaint (#233.82)

#### ED Complaint (#233.82)

The ED Complaint file holds the ED complaints as well as the associated NHAMCS codes, attributes, and possible values.

<table>
<caption><p><span id="_bookmark30" class="anchor"></span>Table 40: Attribute (#233.821)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.82^B</td>
<td><p>Free-text field (required):</p>
<p>Contains the name of the reason for this ED complaint.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>NHAMCS CODE</td>
<td><p>Pointer to NHAMCS REASON FOR</p>
<p>VISIT</p>
<p>DISPLAY (#233.81)</p></td>
<td>233.81^C</td>
<td><p>Pointer to NHAMCS REASON FOR VISIT</p>
<p>DISPLAY file.</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>ATTRIBUTE</td>
<td>Multiple (#233.821)</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>ASSOCIATED SYMPTOM</td>
<td>Multiple (233.822)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_bookmark30" class="anchor"></span>Table 40: Attribute (#233.821)

#### Attribute (233.821)

<table>
<caption><p><span id="_bookmark31" class="anchor"></span>Table 41: Possible Value (#233.8211)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.821^B</td>
<td><p>Free-text field (required):</p>
<p>This is the attribute that will be prompted to the user in the note template when this complaint is selected.</p></td>
</tr>
<tr class="even">
<td>1</td>
<td>POSSIBLE VALUE</td>
<td>Multiple (#233.8211)</td>
<td></td>
<td>Contains a list of possible values for this attribute.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>DISPLAY TEXT</td>
<td></td>
<td></td>
<td>Free-text field: Contains the display value:</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>NHAMCS</p>
<p>Code</p></td>
<td>NHAMCS REASON FOR VISIT DISPLAY (#233.81)</td>
<td></td>
<td><p>Pointer to NHAMCS RESASON FOR VISIT DISPLAY:</p>
<p>Contains the NHAMCS reason for visit.</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark31" class="anchor"></span>Table 41: Possible Value (#233.8211)

#### Possible Value (#233.8211)

<table>
<caption><p><span id="_bookmark32" class="anchor"></span>Table 42: Associated Symptom (#233.822)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>SEQUENCE</td>
<td></td>
<td>233.8211^B</td>
<td><p>Number:</p>
<p>Sequence for this value</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>DISPLAY TEXT</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>This is the display text for this possible value.</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>NHAMCS CODE</td>
<td>NHAMCS REASON FOR VISIT DISPLAY (#233.81)</td>
<td></td>
<td><p>Pointer to NHAMCS REASON FOR VISIT DISPLAY:</p>
<p>This contains the reason for visit display value.</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark32" class="anchor"></span>Table 42: Associated Symptom (#233.822)

#### Associated Symptom (#233.822)

<table>
<caption><p><span id="_bookmark33" class="anchor"></span>Table 43: Clinical Events (#234)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>SEQUENCE</td>
<td></td>
<td>233.822^B</td>
<td><p>Number:</p>
<p>Sequence for this value</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>NAME</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>This is the name of the associated symptom.</p></td>
</tr>
</tbody>
</table>

<span id="_bookmark33" class="anchor"></span>Table 43: Clinical Events (#234)

#### Clinical Events (#234)

The Clinical events file tracks the date/time of clinical events along with vitals, medication, orderable items, and labs associated with the events.

<table>
<caption><p><span id="_Toc54254163" class="anchor"></span>Table 44: EDP Report Template (#232.1)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>DATE/TIME</td>
<td></td>
<td><p>234^B</p>
<p>234^AL</p>
<p>234^AV</p></td>
<td><p>Date/time (required):</p>
<p>This is the date/time of the clinical event.</p></td>
</tr>
<tr class="even">
<td>1</td>
<td>TITLE</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>This is the title of the event, which will be displayed on data graphs</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>PATIENT</td>
<td>PATIENT file (#2)</td>
<td>234^C</td>
<td><p>Pointer to PATIENT file:</p>
<p>This is the patient for this event.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>USER</td>
<td><p>NEW PERSON</p>
<p>file (#200)</p></td>
<td></td>
<td><p>Pointer to the NEW PERSON file:</p>
<p>This is the user responsible for creating this event.</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>TREATMENT</td>
<td><p>ORDERABLE</p>
<p>ITEMS file (#101.43)</p></td>
<td></td>
<td><p>Pointer to the ORDERABLE ITEMS</p>
<p>file:</p>
<p>This is the medication or treatment the patient was receiving at the time of this event.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>LAB TEST</td>
<td><p>Pointer to the LABORATORY</p>
<p>TEST file (#60)</p></td>
<td></td>
<td><p>Pointer to the LABORATORY TEST</p>
<p>file:</p>
<p>This is the lab test used to monitor the efficacy of this treatment, and whose result triggered this event.</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>VITAL SIGN</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<p>‘BP’ – Blood Pressure</p>
<p>*Note* - this DD field appears to be incomplete.. Only BP is listed in the set of codes*</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>DESCRIPTION</td>
<td></td>
<td></td>
<td><p>Free-text field:</p>
<p>The description of this event.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54254163" class="anchor"></span>Table 44: EDP Report Template (#232.1)

#### EDP Report Template (#232.1)

<table>
<caption><p><span id="_Toc54254164" class="anchor"></span>Table 45: Subfile – Sequence (#232.12)</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Number</th>
<th>Field Name</th>
<th>Pointers</th>
<th>Cross Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>NAME</td>
<td></td>
<td>233.822^B</td>
<td>Free-text (Required)</td>
</tr>
<tr class="even">
<td>.02</td>
<td>INACTIVE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ – False</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>.03</td>
<td>EDITABLE</td>
<td></td>
<td></td>
<td><p>Set of codes:</p>
<ul>
<li><p>‘1’ – True</p></li>
<li><p>‘0’ – False</p></li>
</ul></td>
</tr>
<tr class="even">
<td>1</td>
<td>DISPLAY ELEMENTS</td>
<td><p>Multiple to</p>
<p>#232.12</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>ROLES</td>
<td>Multiple to (#232.13)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc54254164" class="anchor"></span>Table 45: Subfile – Sequence (#232.12)

#### Subfile: Sequence (#232.12)

| Field Number | Field Name | Pointers                                      | Cross Reference | Description |
|--------------|------------|-----------------------------------------------|-----------------|-------------|
| .01          | SEQUENCE   |                                               |                 | Number      |
| .02          | ELEMENT    | Pointer to EDP Report Elements file (#232.11) |                 |             |

<span id="_Toc54254165" class="anchor"></span>Table 46: Subfile – Roles (#232.13)

#### Subfile: Roles (#232.13)

| Field Number | Field Name | Pointers                       | Cross Reference | Description |
|--------------|------------|--------------------------------|-----------------|-------------|
| .01          | ROLES      | Pointer CPE ROLE FILE (#232.5) |                 |             |

<span id="_Toc54254166" class="anchor"></span>Table 47: EDP Report Elements (#232.11)

#### EDP Report Elements (#232.11)

| Field Number | Field Name        | Pointers | Cross Reference | Description          |
|--------------|-------------------|----------|-----------------|----------------------|
| .01          | NAME              |          | 232.11^B        | Free-text (Required) |
| .02          | FILE \#           |          |                 | Free-text            |
| .03          | FIELD \#          |          |                 | Free-text            |
| .04          | HISTORY FIELD \#  |          |                 | Free-text            |
| .05          | HEADER            |          |                 | Free-text            |
| 1            | FORMAT LOGIC      |          |                 | Free-text            |
| 2            | EXECUTABLE LOOKUP |          |                 | Free-text            |
| 3            | DESCRIPTION       |          |                 | Free-text            |

<span id="_bookmark36" class="anchor"></span>Table 48: EDIS Options

# Exported Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDPCBRD RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC acts as the front controller for the EDIS display board. It accepts requests that the Java middle tier initially passes to the EDIS Web server. The RPC uses these parameters to determine which command to execute. EDPCBRD allows proxy-user access.

Input parameter SESS identifies requesting users and sites, which the application passes in via its Java middle tier.

Input parameter PARAMS is a list of the parameters that the application passes to the Java middle tier via Hypertext Transfer Protocol ( HTTP) post messages.

EDPCBRD RPC formats and returns data as Extensible Markup Language (XML) documents. The XML structure varies based on the nature of the data request.

### EDPCTRL RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC acts as the front controller for the EDIS tracking application. It accepts requests that the Java middle tier initially passes into the EDIS Web server. The RPC uses the PARAMS parameter to determine which command to execute. The PARAMS parameter is a list of the parameters that users pass to the system’s Java middle tier via HTTP post messages. The RPC’s returned data are formatted as XML documents, the structure of which varies based upon the types of data requests.

### EDPGLOB RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC utilized global arrays to store and return data rather than the previous RPC’s which used only local arrays. During testing, errors were encountered due to stack sized getting too large in the local arrays. Creating and using this RPC for the calls that are more data intensive creates a way to avoid these stack \<STORE\> errors for larger amounts of data. In the future, if the amount of data is in question, this RPC should be used to avoid any potential issues. Currently this RPC is being used for Lab data retrieval, Worksheet.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Type</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDP CONVERSION</td>
<td>Run Routine</td>
<td><p>Allows sites to trigger the conversion of local data in their ^DIZ(1720xx) files to the new EDIS files; the option uses routine EDPFMOVE, which transfers local configuration data first, followed by all currently open visits; EDPFMOVE also queues a task to copy closed visits, thus permitting reporting functionality to run normally.</p>
<p>Uppercase menu text: CONVERT LOCAL ER DATA TO EDIS</p></td>
</tr>
<tr class="even">
<td>EDPF BIGBOARD KIOSKS</td>
<td>Action</td>
<td><p>NOTE: This option is no longer used as of EDIS v.2.1.1/EDP*2.0*6.</p>
<p>Allows facilities to edit the EDPB BIGBOARD KIOSKS parameter; editing parameter values via XPAR utilities is prohibited</p>
<p>Entry Action: D EN^EDPBKS</p>
<p>Uppercase menu text: DISPLAY BOARD KIOSKS</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING MENU ALL</td>
<td>Menu</td>
<td><p>Provides access to all EDPF TRACKING VIEW options Timestamp: 61055,41714</p>
<p>Uppercase menu text: ALL TRACKING VIEWS</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING MENU CLINICIAN</td>
<td>Menu</td>
<td><p>Provides access to EDPF TRACKING VIEW options typically associated with clinicians (the Update, Disposition, and Display Board views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: CLINICIAN TRACKING VIEWS</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING MENU SIGNIN</td>
<td>Menu</td>
<td><p><strong>Note:</strong> This option is no longer used as of EDIS v.2.2/EDP*2.0*13.</p>
<p>Provides access to the EDPF TRACKING VIEW options associated with signing in patients to the emergency department (the Sign In and Display Board views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: SIGN-IN TRACKING VIEWS</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING MENU TRIAGE</td>
<td>Menu</td>
<td><p><strong>Note:</strong> This option is no longer used as of EDIS v.2.2/EDP*2.0*13.</p>
<p>Provides access to the EDPF TRACKING VIEW options associated with triaging patients (the Triage and Display Board views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: TRIAGE TRACKING VIEWS</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING SYSTEM</td>
<td>Broker (client- server)</td>
<td><p>A context option for EDIS remote procedure calls (RPCs) at local facilities; the option uses EDPCTRL RPC and EDPCBRD RPC; assigning any EDPF TRACKING MENU or EDPF TRACKING VIEW</p>
<p>option implicitly provides users with access to this option</p>
<p>Uppercase menu text: EDIS VERSION 1.0-T28</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING VIEW BOARD</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Display Board view.</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: DISPLAY BOARD</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING VIEW CONFIGURE</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Configure view.</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: CONFIGURE TRACKING BOARD</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING VIEW DISPOSITION</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Disposition view.</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: DISPOSITION PATIENT</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING VIEW EDIT CLOSED</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Edit Closed view, which allows users to change any emergency department visit; assign this view to users who are authorized to correct data discrepancies; access should be limited; EDIS logs all changes.</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: EDIT CLOSED PATIENT</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING VIEW REPORTS</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Reports view; security keys further restrict access to some reports. Timestamp: 61514,54336</p>
<p>Uppercase menu text: TRACKING REPORTS</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING VIEW SIGNIN</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Sign In view. Timestamp: 61514,54336</p>
<p>Uppercase menu text: SIGN IN PATIENT</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING VIEW STAFF</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Assign Staff view for configuring staff assignments.</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: ASSIGN STAFF</p></td>
</tr>
<tr class="odd">
<td>EDPF TRACKING VIEW TRIAGE</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Triage view. Timestamp: 61514,54336</p>
<p>Uppercase menu text: TRIAGE PATIENT</p></td>
</tr>
<tr class="even">
<td>EDPF TRACKING VIEW UPDATE</td>
<td>Menu</td>
<td><p>Provides access specifically to the EDIS Update view. Timestamp: 61514,54336</p>
<p>Uppercase menu text: UPDATE TRACKING BOARD</p></td>
</tr>
<tr class="odd">
<td>EDPS BOARD CONTEXT</td>
<td>Broker (client- server)</td>
<td><p>Uses EDPCBRD RPC to set the tracking board’s context.</p>
<p>Uppercase menu text: ED TRACKING BOARD CONTEXT</p></td>
</tr>
<tr class="even">
<td>EDPSERVER</td>
<td>Server</td>
<td><p>Uses the EDPMAIL routine to process incoming scheduling events from VA MailMan.</p>
<p>Uppercase menu text: PROCESS INCOMING SCHEDULING EV</p></td>
</tr>
</tbody>
</table>

## Include EDIS Options in Users’ Menu Trees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Include one or more of the following options in each user’s menu tree:

- EDPF TRACKING MENU ALL
- EDPF TRACKING MENU CLINICIAN
- EDPF TRACKING VIEW BOARD
- EDPF TRACKING VIEW CONFIGURE
- EDPF TRACKING VIEW DISPOSITION
- EDPF TRACKING VIEW EDIT CLOSED
- EDPF TRACKING VIEW REPORTS
- EDPF TRACKING VIEW SIGNIN
- EDPF TRACKING VIEW STAFF
- EDPF TRACKING VIEW TRIAGE
- EDPF TRACKING VIEW UPDATE

### Assign EDIS Views to Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Work with your site’s clinical application coordinators (CACs) and emergency- department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views that he or she needs.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type *1* (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type *User Management* and press the \<Enter\> key.
5.  At the Select User Management Option prompt, type *Edit* (for Edit an Existing User) and press the \<Enter\> key.
6.  At the Select NEW PERSON NAME prompt, type the user’s name using the following format: lastname,firstname. Press the \<Enter\> key. VistA displays the Edit an Existing User dialog.
7.  In the Edit Existing User dialog, press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark \[*?*\] to see a list of the secondary options that are currently assigned to the user.)
8.  Type in the secondary menu options field one of the options listed above and then press the \<Enter\> key.
9.  At the “Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No//” prompt, type *Yes* and press the \<Enter\> key.
10. Press the \<Enter\> key again to accept this new option.
11. In the SYNONYM field, type a synonym for the option (optional). Press the \<Enter\> key.
12. Press the \<Enter\> key to close the COMMAND field and return to the Select
13. SECONDARY MENU OPTIONS field.
14. Repeat steps 8 through 11 to assign other options as necessary.
15. Press the \<Down Arrow\> key to move through the Edit Existing User dialog. At the end of each page, type the letter *n* in the COMMAND field to enter the following page.
16. Stop on page 3.
17. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active.
18. If the user’s person class is not active, select an active person class for the user.
19. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
20. At the Save changes before leaving form (Y/N)? prompt, type the letter *Y* and press the \<Enter\> key.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IAM Single Sign-On Internal (SSOi) and VistA Integration Adapter (VIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses IAM Single Sign-On Internal (SSOi) to authenticate users and VistA Integration Adapter (VIA) and SAML connect to VistA to authorize users. Specifically, it authenticates users via VA issued PIV and uses VistA options and security keys to authorize access to role -based functionality.

## Secure Sockets Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses Secure Sockets Layer (SSL) to secure communications between the EDIS Web server and sites’ display boards. To set up these two-way secure communications for each machine that will power a display board, you must first set up the display board to run in kiosk mode. Kiosk mode locks down the machine’s user interface to protect the application from accidental or deliberate misuse.

For detailed instructions on setting up display boards (also known as big boards), refer to the approved EDIS Baseline.

<span class="mark">REDACTED</span>

### PKI Encryption Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To encrypt communications between the EDIS Web -application server and browsers that sites are using to run their display boards, the server and browsers exchange certificates containing their public keys.

After this exchange takes place, the browser sends a random number that it has encrypted using the server’s public key. The server decrypts this number using its private key. The browser and server then use this random number to generate session keys, which they use in conjunction with their private keys to encrypt and decrypt data exchanges during the communications session.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### *EDPF KIOSKS*NOTE: This security key is no longer used as of EDIS v.2.1.1/EDP\*2.0\*6.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This security key grants access to the EDPF BIGBOARD parameter. This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.*

### EDPR EXPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This security key enables holders to export EDIS reports to Microsoft Excel.

### EDPF WORKSHEETS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This security key is no longer used as of EDIS v.2.2/EDP\*2.0\*13.

This security key controls access to the ability to modify worksheet configurations.

### EDPR ADHOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This security key is no longer used as of EDIS v.2.2/EDP\*2.0\*13.

This security key has been added to control access to ad hoc reports.

### EDPR XREF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This security key enables holders to view and run the EDIS Cross Reference (XRef) report, which matches emergency department visit numbers with associated patient-identity information.

### Assign Keys for Emergency Department Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign keys to users who need access to additional reporting capabilities.

1.  Log in to VistA
2.  At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and then press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type *menu* (for Menu Management) and then press the \<Enter\> key.
5.  At the Select Menu Management Option prompt, type the word *key* (for Key Management) and then press the \<Enter\> key.
6.  At the Select Key Management Option prompt, type the word *allocation* (for Allocation of Security Keys).
7.  At the Allocate key prompt, type the name of the security key you want to assign—*EDPF EXPORT*, for example.
8.  At the Holder of key prompt, type the name of the first user to whom you are assigning the key and then press the \<Enter\> key.
9.  At the Another holder prompt, type the name of a second user to whom you are assigning the key and then press the \<Enter\> key. Repeat this step for all users to whom you are assigning the key.
10. At the You are allocating keys. Do you wish to proceed? YES// prompt, press the \<Enter\> key to accept the default response.

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP CHECK-IN monitors local VistA systems for Scheduling -package events that indicate VA personnel are checking patients into the emergency department. This protocol is placed on the SDAM APPOINTMENT EVENTS protocol, which is an appointment-event driver.

EDP MONITOR monitors order events for the EDIS display board. This protocol is placed on the \* EVSEND OR protocols to check for updates that ancillary packages send to the Order Entry/Results Reporting package. (The asterisk in the expression \* EVSEND OR stands as a placeholder for other package namespaces, such as PS or RA.) It monitors when ancillary packages transmit orders and when they complete the orders.

EDP NEW PATIENT defines variables to support some of the devices that previously monitored SDAM APPOINTMENT EVENTS. The application processes this protocol when users or applications add new patients to the board. Items may look for EDPDATA (EDPDATA = ED Log IEN^DFN^Time In^Hospital Location IEN). This protocol also defines the following variables:

- DFN = Patient file (#2) IEN
- SDT = Time In
- SDCL = Hospital Location file (#44) IEN
- SDATA = ^DFN ^ SDT ^ SDCL
- SDAMEVT = 1 (unscheduled new visit)

EDP OR MONITOR monitors ordering events for the EDIS display board. It is placed on the \* EVSEND OR protocols to look for order numbers that are assigned to new orders from ancillary packages.

EDPF ADD BOARD provides support for an entry action (D ADD^EDPBKS) that adds a display board.

> **NOTE:** The EDPF BIGBOARD MENU protocol and the EDPF BIGBOARD KIOSKS list template and parameter are no longer used as of EDIS v.2.1.1/EDP\*2.0\*6.

*EDPF BIGBOARD MENU defines the menu of actions for the EDPF BIGBOARD KIOSKS list template. This protocol allows facilities to edit the EDPF BIGBOARD KIOSKS parameter. Menu items include:*

- EDPF ADD BOARD (sequence 11)
- EDPF REMOVE BOARD (sequence 12)
- EDPF CHANGE BOARD (sequence 21)
- EDPF SELECT DIVISION (sequence 31)
- EDPF QUIT (sequence 32)
- EDPF BLANK 1 (sequence 22)
- EDPF BLANK 2 (sequence 13)
- EDPF BLANK 3 (sequence 23)

EDPF BLANK 1 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF BLANK 2 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF BLANK 3 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF CHANGE BOARD supports entry action D CHG^EDPBKS, which changes a computer name or display board.

EDPF QUIT supports entry action Q, which exits the EDPF BIGBOARD KIOSKS list template. NOTE: The EDPF BIGBOARD KIOSKS list template is no longer used as of EDIS v.2.1.1/EDP\*2.0\*6.

EDPF REMOVE BOARD supports entry action D REM^EDPBKS, which removes a display board.

EDPF SELECT DIVISION supports entry action D NEWDIV^EDPBKS, which allows the EDIS editor to switch to values for another division.

## Other Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FH EVSEND OR sends Health Level 7 (HL7) messages from the Dietetics package to the Order Entry/Results Reporting package.

GMRC EVSEND OR sends consult requests and tracking data to the Order Entry/Results Reporting package.

LR70 CH EVSEND OR sends orders from the Laboratory package to the Order Entry/Results Reporting package.

OR EVSEND FH sends diet-message events.

OR EVSEND GMRC sends consult-message events.

OR EVSEND LRCH sends laboratory-message events.

OR EVSEND ORG sends generic event messages.

OR EVSEND PS sends pharmacy-message events.

OR EVSEND RA sends radiology and imaging events.

PS EVSEND OR sends inpatient and outpatient medication orders from the Pharmacy package to the Order Entry/Results Reporting package.

RA EVSEND OR sends radiology and imaging message events to the Order Entry/Results Reporting package.

SDAM APPOINTMENT EVENTS performs all necessary actions associated with Scheduling-package events (such as patient check in).

# List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The EDPF BIGBOARD KIOSKS list template is no longer used as of EDIS v.2.1.1/EDP\*2.0\*6.

*EDPF BIGBOARD KIOSKS maps fully qualified machine names to the names of EDIS big board displays.*

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Check-in via Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If EDIS does not automatically add patients when users create an appointment for them or check them in via the Scheduling package, make sure your site's emergency- department location is set in the EDPF LOCATION parameter. Check this parameter to ensure that its value coincides with the value of your emergency department location in file \#44 (Hospital Location). EDIS uses values in the EDPF LOCATION parameter to add patients to its log when you create appointments for, or check in, emergency-department visits.

## Blank View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If users don’t see view selections when they log in to EDIS, you may not have assigned EDIS options for them. Users need at least one assigned option to access EDIS views. If users already have one or more assigned options, you may need to rebuild your site's menu trees in VistA. Rebuilding menus is necessary only after you assign new menu options for the first time.

## PCE Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS creates a Patient Care Encounter (PCE) encounter in CPRS when users select a provider or diagnosis in EDIS. If this functionality isn’t working at your site, check:

- The location entry in the EDPF LOCATION parameter
- Physicians’ and nurses’ person-class status

### Check the EDPF LOCATION Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses the entry in this parameter to create PCE encounters in CPRS.

### Check for Active Person Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before EDIS creates PCE encounters based on physician, nurse, or resident assignments, it checks to make sure the physician, nurse, or resident has an active person class. If a user selects a provider whose person class is expired, EDIS does not create an encounter based on the user’s selection. To remedy this problem, check each person's class for each provider on your site’s staff pick lists.

## Nurse Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, EDIS bases its nursing-staff list on all entries in the New Person file (#200). Sites can elect to have EDIS filter its nurse -selection list to allow only people who hold the ORELSE security key, only people who hold the PSJ RNURSE security key, or only people who are present and active in the Nurse Staff file (#210).

If you do not see emergency-department nurses when you are using the Assign Staff view to create the EDIS Nurse pick list, check the status of your site’s emergency- department nursing staff in the Nurse Staff file. Or, if your site has configured EDIS to base its selection list on the ORELSE or PSJ RNURSE security key, check to make sure your site’s emergency-department nurses hold the appropriate keys.

## Intermittent Login Difficulties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is experiencing intermittent login difficulties and it uses a load balancer that passes control to different instances of VistA, be sure that each VistA instance is running a VistALink listener. Every system that handles VistALink connections must be running a VistALink listener.

## PIV Provisioning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user is unable to sign into EDIS with their PIV card, please reference the below Knowledge Base numbers for assistance.

REDACTED - VistA: Link PIV Card to Vista/CPRS/CAPRI

REDACTED - SSOi: Accessing Applications Using Windows Authentication

## Big Boards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Big Board patient data is not updating properly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the patient data on the Big Board is not updating properly or the data is displaying incorrectly, please reboot the Big Board. It is imperative that any configuration changes, such as adjusting column widths and sizes, are performed in the EDIS desktop application. Do not make configuration changes within the Big Board itself. See Section 8.2.2, Columns, of the *EDIS User Guide* for assistance.

### The display on the Big Board does not fit to the screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a Display Size field in the EDIS desktop application within the Configure view. The value in the Display Size field should match the Display Resolution of the Big Board monitor. Someone with access to the Configure view will need to set the Display Size value in the EDIS desktop application. If the screen size is not available, add it to the EDPF SCREEN SIZES VistA Parameter: