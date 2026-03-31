---
title: Emergency Dept Integration Software (EDIS) Version 2.1.1 Increment 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: Increment 3
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.1
patch_id: EDIS*2.1.1
group_key: "EDIS:EDIS:2.1.1"
file_numbers: 
  - 9
  - 232
security_keys: []
menu_options: 10
description: ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/001.png)
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - table
  - width
  - style
  - contents
  - even
  - edis
  - colgroup
page_count: 0
word_count: 30958
section_count: 28
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

> Department of Veterans Affairs

## Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Technical Manual

![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/001.png)

> July 2013

> Document Version 2.8

> Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Document Version</strong></p>
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
<td><blockquote>
<p>01/06/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Draft</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/07/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Technical Review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>01/08/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/11/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/01/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Technical edits and additions</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/03/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/04/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/15/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5/15/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5/21/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Final Review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6/22/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6/22/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8/30/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9/04/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Review &amp; edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/05/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/28/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>Additional technical reviews</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/26/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.8</p>
</blockquote></td>
<td><blockquote>
<p>Updated links within document</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/30/2012</p>
</blockquote></td>
<td><blockquote>
<p>1.9</p>
</blockquote></td>
<td><blockquote>
<p>Made updates (incorporated edits from [T.S.])</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11/29/2012</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Updated footer</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11/30/2012</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>01/03/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td><blockquote>
<p>Addressed Product Support Feedback</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/04/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1/10/13</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
<td><blockquote>
<p>Edited file to reflect changes from a patch to a host file.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1/14/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.3</p>
</blockquote></td>
<td><blockquote>
<p>Incorporate Product Support Feedback</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2/20/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.4</p>
</blockquote></td>
<td><blockquote>
<p>Updated URLs</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5/10/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>Additional technical reviews</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/11/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>Updated cover page.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/12/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>Final review prior to submission</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>06/20/2013</p>
</blockquote></th>
<th><blockquote>
<p>2.6</p>
</blockquote></th>
<th><blockquote>
<p>Incorporate Product Support updates</p>
</blockquote></th>
<th><blockquote>
<p>Prod Development</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>06/20/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.6</p>
</blockquote></td>
<td><blockquote>
<p>Updated footer , TOC, and addressed text styles for 508 compliance</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/10/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td><blockquote>
<p>Updated checksum value for EDPLOGA.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07/10/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td><blockquote>
<p>Technical Edits</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/17/2013</p>
</blockquote></td>
<td><blockquote>
<p>2.8</p>
</blockquote></td>
<td><blockquote>
<p>Update to remove zip reference</p>
</blockquote></td>
<td><blockquote>
<p>ProdDev</p>
</blockquote></td>
</tr>
</tbody>
</table>
# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/014.png)Product Description


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3](#emergency-department-integration-software-edis-version-211-increment-3)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/014.png)Product Description](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man014pngproduct-description)
  - [About this Guide](#about-this-guide)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
  - [Referenced Documents](#referenced-documents)
    - [Table 1: Types of Documentation](#table-1-types-of-documentation)
  - [Document Conventions](#document-conventions)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/015.png)General Information](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man015pnggeneral-information)
  - [Architectural Scope](#architectural-scope)
    - [Web Application](#web-application)
    - [EDIS Display Boards](#edis-display-boards)
    - [URLs](#urls)
    - [Figure 1: The EDIS topology—version 2.1.1](#figure-1-the-edis-topologyversion-211)
  - [System Performance](#system-performance)
    - [Scaling Guide: Memory and CPU](#scaling-guide-memory-and-cpu)
    - [Minimum Hardware Requirements Table 2: Minimum Hardware Requirements](#minimum-hardware-requirements-table-2-minimum-hardware-requirements)
    - [Disk Space](#disk-space)
  - [EDIS KIDS Host File Install](#edis-kids-host-file-install)
    - [Retrieve patch EDP\2\6](#retrieve-patch-edp26)
    - [Install patch EDP\2\6](#install-patch-edp26)
    - [VistA Download Site download.vista.med.va.gov anonymous.software Namespace and Number Space](#vista-download-site-downloadvistamedvagov-anonymoussoftware-namespace-and-number-space)
    - [Timeouts](#timeouts)
    - [Response Times](#response-times)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/017.png)Parameters](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man017pngparameters)
  - [EDIS (EDPF) Parameters](#edis-edpf-parameters)
    - [Table 4: Parameters](#table-4-parameters)
    - [Setting Up Synchronization with Patient Care Encounters](#setting-up-synchronization-with-patient-care-encounters)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/018.png)Routines](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man018pngroutines)
  - [EDIS Routines](#edis-routines)
  - [EDIS Checksums](#edis-checksums)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/019.png)Files and Globals](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man019pngfiles-and-globals)
  - [Globals](#globals)
    - [Table 5: Global Placement and Protection](#table-5-global-placement-and-protection)
  - [Files](#files)
    - [File Descriptions](#file-descriptions)
    - [Table 7: File Descriptions](#table-7-file-descriptions)
    - [Table 8 Subfile: Discharge Diagnosis Files](#table-8-subfile-discharge-diagnosis-files)
    - [Table 9: Subfile: XE Orders](#table-9-subfile-xe-orders)
    - [Table 10: Record Indices for File#230](#table-10-record-indices-for-file230)
    - [Table 11: XE ED Log History Files (#230.1)](#table-11-xe-ed-log-history-files-2301)
    - [Table 12: XE File Record Indices: (230.1)](#table-12-xe-file-record-indices-2301)
    - [Table 13: XE Files: Tracking Staff (#231.7)](#table-13-xe-files-tracking-staff-2317)
    - [Table 14: XE Files Record Indices: (231.7)](#table-14-xe-files-record-indices-2317)
    - [Table 15: XE Files: Tracking Room Bed (#231.8)](#table-15-xe-files-tracking-room-bed-2318)
    - [Table 16: XE Files: Record Indices (#231.8)](#table-16-xe-files-record-indices-2318)
    - [Table 17: XE Files Tracking Area (#231.9)](#table-17-xe-files-tracking-area-2319)
    - [Table 18: XE Files Display Board Configuration Subfile](#table-18-xe-files-display-board-configuration-subfile)
    - [Table 19: Tracking Code (#233.1)](#table-19-tracking-code-2331)
    - [Table 20: Tracking Code file (#233.1)](#table-20-tracking-code-file-2331)
    - [Table 21: Tracking Code Set (#233.2)](#table-21-tracking-code-set-2332)
    - [Table 22: Subfile: Tracking Code Set file - Codes (#233.21)](#table-22-subfile-tracking-code-set-file-codes-23321)
    - [Table 23: CPE Role (#232.5)](#table-23-cpe-role-2325)
    - [Table 24: EDP Worksheet Specification (#232.6)](#table-24-edp-worksheet-specification-2326)
    - [Table 25: EDP Worksheet Section (#232.71)](#table-25-edp-worksheet-section-23271)
    - [Table 26: EDP Worksheet Component (#232.72)](#table-26-edp-worksheet-component-23272)
    - [Table 29: EDP Worksheet Component Type(#232.73)](#table-29-edp-worksheet-component-type23273)
    - [Table 27: NHAMCS Reason for Visit (#233.8)](#table-27-nhamcs-reason-for-visit-2338)
    - [Table 28: NHAMCS Reason for Visit Display (#233.81)](#table-28-nhamcs-reason-for-visit-display-23381)
    - [Table 29: ED Complaint (#233.82)](#table-29-ed-complaint-23382)
    - [Table 30: Attribute (#233.821)](#table-30-attribute-233821)
    - [Table 31: Possible Value (#233.8211)](#table-31-possible-value-2338211)
    - [Table 32: Associated Symptom (#233.822)](#table-32-associated-symptom-233822)
    - [Table 33: Clinical Events (#234)](#table-33-clinical-events-234)
    - [Table 35: EDP Report Elements (#232.11)](#table-35-edp-report-elements-23211)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/020.png)Exported Remote Procedure Calls](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man020pngexported-remote-procedure-calls)
  - [EDIS Remote Procedure Calls](#edis-remote-procedure-calls)
    - [EDPCBRD RPC](#edpcbrd-rpc)
    - [EDPCTRL RPC](#edpctrl-rpc)
    - [EDPGLOB RPC](#edpglob-rpc)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/021.png)Exported Options](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man021pngexported-options)
  - [EDIS Options](#edis-options)
    - [Table 36: EDIS Options](#table-36-edis-options)
  - [Include EDIS Options in Users’ Menu Trees](#include-edis-options-in-users-menu-trees)
    - [Assign EDIS Views to Users](#assign-edis-views-to-users)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/022.png)Security](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man022pngsecurity)
  - [KAAJEE](#kaajee)
  - [Secure Sockets Layer](#secure-sockets-layer)
    - [PKI Encryption Basics](#pki-encryption-basics)
  - [Security Keys](#security-keys)
    - [EDPF KIOSKS](#edpf-kiosks)
    - [EDPR EXPORT](#edpr-export)
    - [EDPR PROVIDER](#edpr-provider)
    - [EDPF WORKSHEETS](#edpf-worksheets)
    - [EDPR ADHOC](#edpr-adhoc)
    - [EDPR XREF](#edpr-xref)
    - [Assign Keys for Emergency Department Users](#assign-keys-for-emergency-department-users)
    - [Allocation of Security Keys).](#allocation-of-security-keys)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/023.png)Protocols](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man023pngprotocols)
  - [EDIS Protocols](#edis-protocols)
  - [Other Protocols](#other-protocols)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/024.png)List Templates](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man024pnglist-templates)
  - [EDIS List Templates](#edis-list-templates)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/025.png)Troubleshooting](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man025pngtroubleshooting)
  - [Check-in via Scheduling](#check-in-via-scheduling)
  - [Blank View](#blank-view)
  - [PCE Visits](#pce-visits)
    - [Check the EDPF LOCATION Parameter](#check-the-edpf-location-parameter)
    - [Check for Active Person Class](#check-for-active-person-class)
  - [Nurse Assignments](#nurse-assignments)
  - [Intermittent Login Difficulties](#intermittent-login-difficulties)
- [Index](#index)
> Emergency Department Integration Software (EDIS) incorporates several Web-based views that extend the current Computerized Patient Record System (CPRS) to help healthcare professionals track and manage the flow of patient care in the emergency - department setting. EDIS views are based on a class-three application developed by the Upstate New York Veterans Health Care Network—or Veterans Integrated Services Network (VISN) 2. Most views are site-configurable. EDIS enables you to:
- Add emergency-department patients to the application’s electronic whiteboard—or big board—display
- View information about patients on the display board
- Edit patient information
- Remove patients from the display board
- Create administrative and operational reports
> The application also includes views for entering patients’ dispositions and configuring the display board.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Emergency Department Integration Software Technical Manual* provides technical information for configuring, managing, and troubleshooting local (M Server) components of the EDIS application.

## Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Section 508 Compliance Testing is required for an application utilizing a Graphical User Interface (GUI), such as CPRS or BCMA. Roll and scroll VistA Legacy applications written in MUMPS need not comply with Section 508 Compliance requirements.

> EDIS received a 508 exception on 12/17/12.

## Referenced Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following documents are available on the VistA Documentation Library (VDL), which is located at [<u>http://www.va.gov/vdl/application.asp?appid=179</u>](http://www.va.gov/vdl/application.asp?appid=179) :

- EDIS Client Installation Guide
- EDIS Server Installation Guide
- IRM Big Board Installation Guide
- EDIS User Manual
- EDIS Glossary
- EDIS Technical Manual

> From the ANONYMOUS software directories:

> OIFO FTP Address Directory

- <span class="mark">REDACTED</span>

### Table 1: Types of Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Title</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Mode</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDP_2_1_1_SrvrIG.PDF</p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version 2.1.1 Server</u> <u>Installation Guide</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>EDP_2_1_1_TM.PDF</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version 2.1.1 Technical</u> <u>Manual</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>EDP_2_1_1_UM.PDF</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version2.1.1 User Manual</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>EDP_2_1_1_ClientIG.PDF</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version2.1.1 Client</u> <u>Installation Guide</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>EDP_2_1_1_BigBoardIG.PDF</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version2.1.1 IRM Big</u> <u>Board Installation Guide</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>EDP_2_1_1_Glossary.PDF</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Emergency Department Integration</u> <u>Software Version2.1.1 Glossary</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Binary</u></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bold type indicates application elements (views, panes, links, buttons, text boxes, and so forth) and key names.

> Key names appear in angle brackets \<\>.

> *Italicized text* indicates special emphasis or user responses. ALL CAPS indicates M routines and options.

> … (Ellipses) indicate omitted text.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/015.png)General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Architectural Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS runs as a Web application on a centrally located Oracle WebLogic server that contains program logic and operational emergency-department data in its Java middle tier. (Refer to Figure 1.) The presentation tier is a Flash Player application. The data tier encompasses local sites’ Veterans Health Information Systems and Technology Architecture (VistA) systems and a centrally located relational database management system (RDMS) data store containing Standard Data Services (SDS) tables.

> The application uses remote procedure calls (RPCs) from local VistA implementations to populate patient- and provider-selection lists, provide limited data synchronization between EDIS and CPRS, and determine users’ access levels.

### Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The application’s presentation tier runs in users’ Web browsers via Adobe Flash Player. The VA’s Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE) provides end-user authentication.

### EDIS Display Boards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites can configure one or more electronic whiteboard—or big board—displays. Display boards run in their own browser-based instances of Flash Player.

### URLs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  EDIS in Production Accounts

> When EDIS is running in your site’s production account, use [<u>https://</u>](https://vaww.edis2.med.va.gov/main) [<u>vaww.edis2.med.va.gov /main</u>](https://vaww.edis2.med.va.gov/main) for user access to the main application and [<u>https://vaww.edis2.med.va.gov/bigboard/bigboard.html</u>](https://vaww.edis.med.va.gov/main/board.html) for your main big-board display. For secondary big-board displays, append the following argument: board=your_secondary_board_name. For example, if your site has a secondary display board named *Lab;* its URL would be

> https://vaww.edis2.med.va.gov/main/board.html?sitecode=442&board=Lab. and your institution must be placed in the sitecode parameter.

2.  EDIS in Test Accounts

> When EDIS is running in your site’s test account, use [<u>https://</u>](https://preprod.edis2.med.va.gov/main) [<u>preprod.edis2.med.va.gov /main</u>](https://preprod.edis2.med.va.gov/main) for user access to the main application.

### Figure 1: The EDIS topology—version 2.1.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/016.png)

## System Performance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scaling Guide: Memory and CPU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workstations should comply with VA Desktop Minimum Acceptable Configurations ([<u>http://vaww.vairm.vaco.va.gov/VADesktop</u>](http://vaww.vairm.vaco.va.gov/VADesktop)). In addition, users’ workstations should meet the minimum hardware requirements for running Adobe Flash Player:

### Minimum Hardware Requirements Table 2: Minimum Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Optimal Viewing Requirements<span id="_bookmark3" class="anchor"></span> Table 3: Optimal Viewing Requirements

### Disk Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS installation creates files in two global: ^EDP and ^EDPB.

- You can expect ^EDP to grow at the following yearly rate: 2,000 bytes multiplied by the number of emergency-department visits per year. For example, if your emergency department responds to an average of 12,000 visits every year, you can expect ^EDP to grow at a yearly rate of 24 MB. You should place this global in a volume with sufficient space to manage this growth.
- You can expect ^EDPB to remain small. (It is currently about 50 K.)

## EDIS KIDS Host File Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Retrieve patch EDP\*2\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: *The EDP .ear file for the Graphical User Interface will show a version*

> *of 2.1.1, while patch 6 for VistA will show a version of 2.0. This is okay and should not be a reason for concern. The application guides will appear with version 2.1.1*

> Patch 6 (EDP\*2\*6) is a FORUM patch and will be pushed to the IRM’s by product support. Once you have been notified that the patch has been pushed, you can retrieve and extract the patch from Mail Manager.

### Install patch EDP\*2\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow these instructions to install EDIS patch 6. Installation time is less than one minute.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch \#(ex. EDP\*2.0\*6):
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch(routines, DDstemplates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install (EDP\*2\*6).
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer ‘NO’
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer ‘NO’.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// , answer ‘NO’.
8.  If prompted “Delay Install (Minutes): (0 – 60): 0// respond 0.

> Note: In the event a person is not part of the ED staff, or does not have an entry in the tracking staff file, they can be added manually. This may be required due to the user not having the appropriate keys to be identified as a physician or nurse. If they do not have the appropriate keys, they will not show up in the search boxes in the Tracking staff functionality. These are the manual instructions for IRM’s/support staff to add themselves to the TRACKING STAFF file (#231.7).

> VA FileMan 22.0

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: TRACKING STAFF// 231.7 TRACKING STAFF

> (34 entries)

> EDIT WHICH FIELD: ALL//

> Select TRACKING STAFF PERSON: last,first LF 192 OI&T STAFF

> Are you adding 'last,first' as a new TRACKING STAFF (the 35TH)? No// Y (Yes)

> INSTITUTION: 442

1.  442 CHEYENNE VAMC WY M&ROC 442
2.  4429AA CHEYENNE NHCU WY NHC 4429AA
3.  442DT SCOTTSBLUFF ANNEX NE STNB 442DT
4.  442GA ZZ CASPER CBOC WY CBOC 442GA INACTIVE
5.  442GB SIDNEY CBOC NE CBOC 442GB Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 CHEYENNE VAMC WY M&ROC 442

> AREA: Emergency Department INACTIVE:

> LOCAL ID\*:

> ROLE: Provider INITIALS\*: BWF COLOR:

### VistA Download Site download.vista.med.va.gov anonymous.software Namespace and Number Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The namespace for EDIS is EDP. The number space is 230 -234.

### Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses the timeout parameter ( EDP APP TIMEOUT). If this parameter is not set for the site’s users, EDIS uses the kernel function \$\$DTIME^XUP to determine timeout. If users’ DTIME is set to null, EDIS uses DEFAULT TIME- READ in the Kernel Parameters file. If this file is set to zero, the application uses a timeout of 300 seconds.

### Response Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Insufficient data: response times are still to be determined (TBD).

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/017.png)Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS (EDPF) Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 4: Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>EDPF Parameter Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDPF BIGBOARD KIOSKS</p>
</blockquote></td>
<td><blockquote>
<p>This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF DEBUG START TIME</p>
</blockquote></td>
<td><blockquote>
<p>This parameter sets a $H timestamp to signal that EDIS should log out its RPCs for 30 minutes following the debug time stamp.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>This parameter holds one or more entries from the Hospital Location (#44) file. Entries correspond to hospital locations that the emergency department uses. With this parameter, VistA prompts sites for a time range or sequence. If sites have multiple Hospital Location file entries, they have two choices when responding to the <strong>Time Range or Sequence</strong> prompt: they can enter a time range or a sequence.</p>
<p>Entering a time range allows EDIS to map Hospital Location entries by time of day. EDIS uses this mapping when users create encounters in the Patient Care Encounters (PCE) package: it matches the Hospital Location entry based on the current time of day. The parameter accepts ranges in military time.</p>
<p>Entering a sequence allows sites to map Hospital Location entries in order of preference. When users create encounters in PCE, EDIS uses the entry with the lowest sequence number to create visits.</p>
<p>When users create appointments by checking in patients via the Scheduling package, any matches on this parameter’s list of locations (be they time- or sequence-based) cause EDIS to add the checked-in patient to the display board.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF NURSE STAFF SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>This parameter allows sites to select the type of filtering upon which EDIS bases its nurse-selection list. It applies filtering—or screening— to the New Person file (#200). By default, EDIS allows selections from all entries in the New Person file. Other screening options include the following:</p>
</blockquote>
<ul>
<li><p>Allow only persons holding the ORELSE key</p></li>
<li><p>Allow only persons holding the PSJ RNURSE key</p></li>
<li><p>Allow only persons who are present and active in the Nurse Staff file (#210)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EDPF SCHEDULING TRIGGER</p>
</blockquote></th>
<th><blockquote>
<p>This parameter allows sites to specify which Scheduling package event, triggers EDIS to automatically add patients to the board. Sites can choose from one of the following two selections:</p>
<p><strong>1: Patient will be added to the board when an appointment is made</strong></p>
<p><strong>4: Patient will be added to the board when checked in</strong></p>
<p>Sites can set this parameter at the package, system, or division level.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDPF SCREEN SIZES</p>
</blockquote></td>
<td><blockquote>
<p>This parameter contains a list of selectable screen sizes for sites’ EDIS display boards. The parameter generally lists large-display LCD or plasma screen sizes. Add screen sizes to this parameter using the following format: WxH (width multiplied by height). You can set this parameter at the package, system, or division level.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDP APP COUNTDOWN</p>
</blockquote></td>
<td><blockquote>
<p>This parameter contains the number of countdown seconds before the application closes. Once the timeout is met, this is the number that the counter will start with as it begins countdown for closure. If this parameter is set at 15, after the timeout has occurred, the user will be given 15 seconds to respond to a dialog.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDP APP TIMEOUT</p>
</blockquote></td>
<td><blockquote>
<p>This holds the number of seconds until the application times out. If set, this value over rides the user’s DTIME value.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Setting Up Synchronization with Patient Care Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EDPF LOCATION parameter should contain the hospital location or locations that your emergency department uses. If yours is a multi-division site, make an entry for each division.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools option prompt, type *ep* (for Edit Parameter Values) and then press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf l* (for

> EDPF LOCATION)*,* and then press the \<Enter\> key.

5.  At the Select INSTITUTION NAME prompt, type the name or station number of your institution and then press the \<Enter\> key.
6.  At the Select Time Range (ex. 0800-1200) or Sequence prompt, type the time range during which the clinic location you are about to select functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department 24 hours a day, type *0001-2400* Alternately, type a number that represents the location’s preference rating (the number *1* represents the most-preferred location). Press the \<Enter\> key. When users create a PCE encounter, EDIS uses time-of-day-based or preference-based criteria to determine the encounter’s location.

> Note: When selecting time ranges, take care to account for all hours of emergency-department operation. EDIS does not create PCE appointments for patients whom users add during times that you don’t include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE appointment for the

> patient. Also, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE appointment for the first clinic.

7.  At the Are you adding \[*your time range or sequence*\] as a new Time Range or Sequence? Yes// prompt, press the \<Enter\> key to accept the time range or sequence—or, if you’ve made a mistake, type the letter *n* (for *No*) and press the

> \<Enter\> key.

8.  VistA displays a confirmation: Time Range (ex. 0800-1200) or Sequence \[*your time range or sequence*\]//. Press the \<Enter\> key to acknowledge this confirmation.
9.  At the ED LOCATION prompt, type the name of the location that serves as your site’s emergency department during this time range (or for this preference rating) and press the \<Enter\> key.
10. Repeat steps 6 through 9 for additional emergency-department locations.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/018.png)Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- EDP2PST – Post-init for facility install.
- EDPARPT - This routine handles the following functions
  - Saving/Modifying report templates
  - Building new report templates
  - Executing existing report templates as well as ad-hoc reports (fully custom unsaved reports).
- EDPARPT1 – Ad Hoc Reports.
- EDPBCF loads and saves display-board configuration settings—including column values, color maps, room and area values, parameter settings, and screen-size settings. It also loads a list of display boards and their specifications.
- EDPBCM creates and saves configuration settings for color maps. It creates color-map elements, closing tags, map elements for standard urgencies, and single map elements. It also builds color-map selection lists.
- EDPBDL deletes or inactivates configuration entries. It deletes rooms or beds if the application’s log entries are not referencing them; otherwise, it inactivates the rooms or beds.
- EDPBKS supports a list template that maps fully qualified machine names to the names of EDIS big-board displays; this routine enables sites to add, change, and delete large displays that run in kiosk mode.
- EDPBLK handles locking and unlocking for configuration settings. It displays one of three error messages when one user attempts to make or save configuration changes while another user is also making or saving changes.
- EDPBPM loads current and saves updated Configuration view parameter settings (diagnosis required, coded diagnosis required, disposition required, reason for delay required, number of minutes before reason for delay is required, shift start time and duration, include residents, default room or area, and arriving-ambulance area). It also saves time zone differences (in minutes) and sets the fail node.
- EDPBRM loads a list of all rooms and beds in sequence, builds an XML output file containing this list, and keeps the list updated. It also adds and updates room-and-area records, loads multi-assignment areas and choice lists (display-when, single- and multiple- patient assignments, and so forth).
- EDPBRS sets and resets display-board specifications (default-board specifications, display width, scroll-delay time, column size, column headers and size, font size, row colors, baseline rooms, and baseline parameters).
- EDPBSL loads selection lists (acuity, status, mode of arrival, disposition, and reason for delay) and builds XML output files for them. It also saves selection-list changes; creates new code sets; clears codes from, and adds new codes to, the CODES multiple; and updates existing codes in, and adds new codes to, the Tracking Code file (#233.1).
- EDPBST returns a list of staffing matches from VistA’s New Person file (#200). For each of the following three roles, it builds a list of staff members who have an active person class: resident, physician, and nurse. It also saves updated staff members and creates and updates records in the Tracking Staff file (#231.7).
- EDPCBRD is the controller for the EDIS display board. It processes requests via remote procedure calls (RPCs) and also supports a Caché Server Pages (CSP) mode for processing requests via CSP.
- EDPCDBG is the debugging routine for the display-board controller. It turns debugging on and off, enables the EDIS debugging log, logs debugging activities for 30 minutes after the debugging start time, records debugging start and stop times, and saves debugging requests and XML results.
- EDPCONV processes incoming mail to convert emergency-department visits from Syracuse class-three application files to EDIS class-one files. It stores conversion data in the Tracking Code file (#233.1), Tracking Room/Bed file (#231.8), ED Log file (#230), and ED Log History file (#230.1).
- EDPCONV1 converts configuration data from Syracuse class-three application files to EDIS class-one files. It stores converted data in the Tracking Area file (#231.9).
- EDPCSV is a comma-separated-value (CSV) utility that provides a controller for HyperText Transfer Protocol (HTTP) requests.
- EDPCTRL is the controller for EDIS. It processes requests via remote procedure calls (RPCs) and also supports Caché Server Pages (CSP) mode for processing requests via CSP.
- EDPDD provides a test update log.
- EDPFAA provides RPC calls to the local facility. It also sets up EDIS sessions and returns role-based views for users. (EDPFAA code enabled VHA eHealth University \[VeHU\] training.)
- EDPFLEX provides Lexicon-package utilities: it returns matches from the Lexicon package when users type in free-text dispositions.
- EDPFMON monitors Health Level 7 (HL7) VistA event messages at the facility. It adds new orders to patients’ log entries based on visit-related information from the following packages: Radiology, Laboratory, Pharmacy, Consults, Procedures, Dietetics, and Order Entry. It also updates orders’ statuses and removes orders from patients’ log entries.
- EDPFMOVE is part of the conversion routine. It moves local emergency-department visits to EDIS and provides conversion-related messages—“Visit conversion has completed,” for example. This routine also provides users with several conversion-related options—such as the option to convert Syracuse class-three configuration data (in addition to patient data).
- EDPFPER looks up emergency-department staff (providers, residents, and nurses) in VistA’s New Person file (#200). The routine adds people who match its screening criteria to EDIS staffing lists.
- EDPFPTC performs patient-selection checks. For example, this routine checks to see if selected patients are already on the Active Patients list, have patient records that are marked sensitive (in which case the routine displays a warning), are deceased, or have identifiers that are similar to the identifiers of one or more patients who are already on the Active Patients list. (Patients on the Active Patients list are ipso facto on the display board.) This routine also gets patient record flags (PRFs) for display within EDIS and makes security-log entries when users access records marked sensitive.
- EDPFPTL accepts as its input patient names and social security numbers (including last four social security numbers and last-name initials concatenated with last four social security numbers) and returns from the local VistA system a list of possible matches.
- EDPGLOB – This routine is used to return a global array. If the amount of data is too large, store errors can occur in VistA. Using the EDPGLOB RPC fixes these errors and utilizes global arrays to store and send back the data.
- EDPLOG updates the EDIS log in response to timestamp changes. It also processes diagnoses and checks for the presence of data in required fields before letting users remove patients from the system.
- EDPLOG1 validates record entries and returns error messages for invalid entries.
- EDPLOGA adds log records for new patients. It sets up patient fields, adds default values to stub entries, creates current log records, and creates initial log-history entries. This routine also deletes the initial history-log stub entry.
- EDPLOGH adds new log-history entries and saves new entries for changed fields. This routine also checks timestamps in the ED Log History file (#230.1) for possible data-entry collisions and displays a warning message—“Since you loaded this entry, changes have been made by someone else”—when collisions are imminent. Similarly, when users update data and select a different view before saving their updates, this routine warns them that they will lose their changes if they exit the view without first saving their changes. Finally, this routine notifies users when their bed choices are no longer available.
- EDPLPCE creates a visit in the CPRS Patient Care Encounters (PCE) package when users select a provider, resident, nurse, or diagnosis in EDIS. It updates diagnoses for emergency- department visits in EDIS if users enter the diagnoses in CPRS, and in CPRS if users enter the diagnoses in EDIS. This routine also coordinates primary providers between CPRS and EDIS.
- EDPMAIL parses and processes incoming VA MailMan messages from SEND^EDPFMON, which monitors order-related events such as new orders, order changes, deleted orders, and so forth. EDPMAIL also parses and processes patient check-in events.
- EDPQAR logs area information. It returns site-configurable parameters and default areas, and adds default areas in cases where no default areas are assigned.
- EDPQDB displays active log entries on the EDIS display board. It gets display-board data—a list of all beds in sequence for a given area, patient data, and so forth—computes order statuses, and formats data for display.
- EDPQDBS gets display-board specifications for room, area, and staff color configurations.
- EDPQLE retrieves log entries by request and returns XML-formatted log entries for patient demographics, diagnoses (ICD-9-CM coded), fields required for closing entries (delay reasons, physician assignments, and so forth), and time stamps.
- EDPQLE1 retrieves supporting information—such as staff and other selection items—and adds the information to XML pick lists. It also builds nodes for code sets.
- EDPQLP returns lists for the log-entry edit context. It also builds duplicate-name and last- four-Social-Security-number lists for counters.
- EDPQPCE retrieves PCE information such as diagnoses (including primary and free-text diagnoses) for emergency-department visits.
- EDPRPT gets data for reports by site and date range. This routine turns on switches that determine the beginning and ending points of the report date range and the report type. It also returns timestamp-related data—such as the times acuities were first assigned, the times patients left the waiting area, the times admitting decisions were entered, and so forth.
- EDPRPT1 gets data for the Activity report based on site and date range. It gets report headers (CSV), calculates times and averages for column values, initializes counters and sums, returns external values for codes, and includes a list of assigned providers.
- EDPRPT10 gets data for the Admissions report based on site and date range. This routine initializes counters and sums, gets report headers (CSV), calculates times and averages, initializes counters and sums, and returns external values for codes.
- EDPRPT11 gets data for the Patient Intake report based on site and date range. This routine initializes counters and sums, gets report headers, returns counts and averages, performs rounding computations, returns hours (24-hour—or military—clock format), and returns name-of-day (Monday, Tuesday, and so forth).
- EDPRPT12 gets data for the Orders by Acuity report based on site and date range. It gets report headers and returns an acuity-based count of lab, imaging, medication, consult, and other orders.
- EDPRPT2 gets data for the Delay report based on site and date range. It initializes counters and sums, returns counts and averages, and gets column headers. The routine also returns disposition indicators for VA admissions and external values for codes.
- EDPRPT3 gets data for the Missed Opportunities report based on site and date range. It initializes counters and returns a 1 (one) or 0 (zero) to indicate missed opportunities. The routine also gets column headers, initializes counters, calculates times, and returns totals as CSV- or XML-formatted data.
- EDPRPT4 gets data for the Delay Summary report based on site and date range. It initializes counters and sums and returns counts and averages as CSV- or XML-formatted data. This routine also returns external values for acuity and other codes, and codes (1 or 0) for IEN statuses that indicate observation.
- EDPRPT5 returns data for the Shift report based on site and day. It initializes counters and sums, calculates the number of visits that carried over, and returns the following: column information (headers, counts and averages—as CSV- and XML-formatted data), the names of shifts (one, two, three, and so forth—based on shift times), and external values for acuity codes.
- EDPRPT6 gets data for the Provider report based on site and date range. It initializes counters and sums, calculates and returns averages as CSV- and XML-formatted data, and returns external values for acuity codes.
- EDPRPT7 gets data for the Exposure report based on site and the infected person’s time in and time out of the emergency department. It returns a list of patients who were in the waiting room and treatment rooms during the infected patient’s stay (adding a row for each room the infected patient used —including laboratory and x-ray). It also returns on-duty staff assignments. EDPRPT7 returns external values for codes.
- EDPRPT7C gets data for the Exposure report in CSV format.
- EDPRPT8 gets data for the Acuity report based on site and date range. It initializes counters and sums and returns external values for acuity codes. The routine returns counts and averages for acuity-based entries, all admissions, and VA admissions.
- EDPRPT9 gets data for the Patient Cross Reference (XRef) report based on site and date range. It uses the ED Log file (#230) to provide information about patients’ identities.
- EDPRPTBV gets data for the BVAC report based on site and date range. This routine initializes counters and sums, gets column headers, calculates sums and averages, and returns external values for codes.
- EDPX provides a group of common utilities that includes the following: ESC (X), escape for XML transmission; UES (X), unescape XML; UESREQ (REQ), unescape HTTP post; VAL (X,R), returns parameter value or null; NVPARSE (LST, IN), parses tab and delimited name-value pairs into an array; XMLS (TAG, DATA, LBL), returns an XML node as \<TAG data=“9” label=“XXX” /\>; XMLA (TAG, ATT, END), returns an XML node as \<TAG att1=“a” att2=“b”… /\>; SMLE (SRC), appends lists to XML arrays as elements; XML (X), adds the line of XML that is to be returned; CODE (X), returns internal values for codes; MSG (MSG), writes out error messages.
- EDPYCHK performs a pre-installation environment check.
- EDPYPRE is the pre-initialization routine.
- EDYPST is the post initialization routine.
- EDPBWS is the main routine for processing, building, retrieving, and modifying worksheets for the EDIS User Interface
- EDPQPPS – routine to handle display board specifications.

## EDIS Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following list contains routine names with checksums:

> Routine Name: EDP2PRE Before: N/A After: 852824

> Routine Name: EDP2PST

> Before: N/A After: 10565179 Routine Name: EDPARPT

> Before: N/A After: 95079217 Routine Name: EDPARPT1

> Before: N/A After: 17834740 Routine Name: EDPBCF

> Before: 25433175 After: 26108693 Routine Name: EDPBRM

> Before: 25575594 After: 26325333 Routine Name: EDPBST

> Before: 8664749 After: 9812007 Routine Name: EDPBWS

> Before: 52550125 After: 229022529 Routine Name: EDPCSV

> Before: 906612 After: 1174493 Routine Name: EDPCTRL

> Before: 73485587 After: 89022760 Routine Name: EDPFAA

> Before: 24518510 After: 36904209 Routine Name: EDPFPER

> Before: 3427509 After: 4359382 Routine Name: EDPGLOB

> Before: 2277682 After: 4109172 Routine Name: EDPLAB

> Before: 49753454 After: 51111821 Routine Name: EDPLOG

> Before: 56585715 After: 58048189 Routine Name: EDPLOGA

> Before: 11867179 After: 12583805 Routine Name: EDPLOGH

> Before: 12449970 After: 12593326 Routine Name: EDPQAR

> Before: 6897621 After: 7638401 Routine Name: EDPQDB

> Before: 55055961 After: 56093021 Routine Name: EDPQDBS

> Before: 3118586 After: 7446153 Routine Name: EDPQLE

> Before: 41785417 After: 43232281

> Routine Name: EDPQLE1

> Before: 10666213 After: 11912520 Routine Name: EDPQPCE

> Before: 2442064 After: 3317665 Routine Name: EDPQPPS

> Before: 3126500 After: 4046541 Routine Name: EDPRPT1

> Before: 44256046 After: 50357723 Routine Name: EDPRPT10

> Before: 26044910 After: 30220543 Routine Name: EDPRPT12

> Before: 7802924 After: 8703521 Routine Name: EDPRPT13

> Before: 7380759 After: 7846285 Routine Name: EDPRPT2

> Before: 22188672 After: 24332800 Routine Name: EDPRPT3

> Before: 14278258 After: 14278258 Routine Name: EDPRPT4

> Before: 25030915 After: 32540898 Routine Name: EDPRPT7C

> Before: 20628134 After: 22153636 Routine Name: EDPRPT8

> Before: 15247059 After: 15923220 Routine Name: EDPRPTBV

> Before: 21134846 After: 28273730 Routine Name: EDPX

> Before: 10778850 After: 12709600

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/019.png)Files and Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses the following globals:

> ^EDP

> ^EDPB

> The ^EDP global holds a list of patients who are currently checked in at the emergency-department (that is, the list of active patients). The ^EDPB global holds a comprehensive list of emergency-department activities.

### Table 5: Global Placement and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 13%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Placement</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Journal</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Protection</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>^EDP</p>
</blockquote></td>
<td><blockquote>
<p>Dynamic</p>
</blockquote></td>
<td><blockquote>
<p>Place this global in a volume set that can accommodate the following yearly growth rate:</p>
<p>2,000 bytes * visits per year</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>RWP or D</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>^EDPB</p>
</blockquote></td>
<td><blockquote>
<p>Static</p>
</blockquote></td>
<td><blockquote>
<p>No recommendation (this global should remain small)</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>RWP or D</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark6" class="anchor"></span>Table 6: XE Files

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Root Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global Protection</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>230</p>
</blockquote></td>
<td><blockquote>
<p>ED LOG</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(230)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>230.1</p>
</blockquote></td>
<td><blockquote>
<p>ED LOG HISTORY</p>
</blockquote></td>
<td><blockquote>
<p>^EDP(230.1)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>231.6</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING BOARD</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(231.6)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>231.7</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING STAFF</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(231.7)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>231.8</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING ROOM- BED</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(231.8)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>231.9</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING AREA</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(231.9)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>232.1</p>
</blockquote></td>
<td><blockquote>
<p>EDP REPORT TEMPLATE</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.1)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>232.11</p>
</blockquote></td>
<td><blockquote>
<p>EDP REPORT ELEMENTS</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.11)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>232.5</p>
</blockquote></td>
<td><blockquote>
<p>CPE ROLE</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.5)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>232.6</p>
</blockquote></td>
<td><blockquote>
<p>EDP WORKSHEET SPECIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.6)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>232.71</p>
</blockquote></td>
<td><blockquote>
<p>EDP WORKSHEET SECTION</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.71)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>232.72</p>
</blockquote></td>
<td><blockquote>
<p>EDP WORKSHEET COMPONENT</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.72</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Root Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global Protection</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>232.74</p>
</blockquote></td>
<td><blockquote>
<p>EDP COMPONENT VALIDATORS</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(232.74)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>233.1</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING CODE</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(233.1)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>233.2</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING CODE SET</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(233.2)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>233.8</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(233.8)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>233.81</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT DISPLAY</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(233.81)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>233.82</p>
</blockquote></td>
<td><blockquote>
<p>ED COMPLAINT</p>
</blockquote></td>
<td><blockquote>
<p>^EDPB(233.82)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>234</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL EVENTS</p>
</blockquote></td>
<td><blockquote>
<p>^EDP(234)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

### File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 5.2.1.1. ED Log (#230)

> The ED Log file serves as the log of emergency-department visits and as EDIS’s key source of information for display-board data. EDIS refreshes the display board every 30 seconds, and many of the indices in this file assist in making the application’s refresh code as efficient as possible.

> The file works together with the ED Log History file (#230.1) to track activities associated with typical emergency-department visits from beginning to end. The log records key clinical events—triage and disposition, for example. It also records where each patient went after his or her emergency - department visit, and who was responsible for the patient.

### Table 7: File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>LOG ENTRY TIME</p>
</blockquote></td>
<td><blockquote>
<p>The Log Entry field (.01) of the ED Log History file (230.1)</p>
<p>points to this field</p>
</blockquote></td>
<td><blockquote>
<p>230^B</p>
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
<p>PN (#796)</p>
</blockquote></td>
<td><blockquote>
<p>Date-and-time field (required):</p>
<p>Contains the date and time EDIS added this log record to the file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Institution file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AP (#792)</p>
<p>AS (#793)</p>
<p>ATO (#795)</p>
<p>PN (#796)</p>
<p>PDFN (#801)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required): This field allows EDIS to associate log entries with</p>
<p>the stations that originated</p>
<p>the entries; it allows the same EDIS system to serve multiple institutions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>AREA</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Area file (#231.9)</p>
</blockquote></td>
<td><blockquote>
<p>AC (#787)</p>
<p>ADUP1 (#788)</p>
<p>ADUP2 (#789)</p>
<p>AL (#790)</p>
<p>AN (#791)</p>
<p>AP (#792)</p>
<p>AS (#793)</p>
<p>PN (#796)</p>
<p>PDFN (#801)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field</p>
<p>Points to the hospital area to which records apply— initially only to the site’s emergency-department locations; will allow sites to expand EDIS’s use to other departments</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field: Contains the patient’s name</p>
<p>Allows sites to enter patients’ names in cases of humanitarian intervention or where patients do not yet have entries in VistA; assists in checking for duplicate names and similar names on the display; this field is set to the following value in cases where ambulances are arriving and the names of the patients are unknown: (ambulance enroute); when patients are added to VistA during their ED visits, their names in VistA replace clerk- entered names; when users select patients from VistA, the software gets the patients’ VistA names and places them in this field</p>
<p>The field uses this format: Surname,Firstname</p>
<p>Names must be 3 to 30 characters in length</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT SSN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AS (#793)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains the patient’s Social Security number</p>
<p>Allows sites to enter patients’ Social Security numbers in cases of humanitarian care or when patients do not yet have entries in VistA</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Patient file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>AP (#792)</p>
<p>APA (#806)</p>
<p>PDFN (#801)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s data file number (the DFN is the IEN in the Patient file)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Contains the patients in VistA for whom EDIS is creating its log entries; entries may be absent in cases where ambulances are arriving with unknown patients and where sites are rendering humanitarian aid to non- VA patients</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED</p>
</blockquote></td>
<td rowspan="9"></td>
<td><blockquote>
<p>AC (#787)</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>A setting:</p>
<p>1 (Yes)</p>
<p>0 (No)</p>
<p>EDIS sets this flag to <em>1</em> when users remove properly disposed patients from the area (emergency department); closed entries no longer appear on the display board</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ADUP1 (#788)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>ADUP2 (#789)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>AL (#790)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>AN (#791)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>AP (#792)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>AS (#793)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>APA (#806)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Triggers CLOSED DATE/TIME (.071)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.071</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>Triggered by the CLOSED field (.07)</p>
</blockquote></td>
<td><blockquote>
<p>Date-and-time field:</p>
<p>Contains the date/time when the log entry was ‘closed’.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.072</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED BY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Contains the IEN of the user who closed the log entry.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.073</p>
</blockquote></td>
<td><blockquote>
<p>REMOVED IN ERROR</p>
</blockquote></td>
<td><blockquote>
<p>Set of Codes</p>
</blockquote></td>
<td rowspan="3"></td>
<td><blockquote>
<p>Set of codes:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>1 (Yes)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.074</p>
</blockquote></td>
<td><blockquote>
<p>RESTORED BY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to New Person file (#200)</p>
</blockquote></td>
<td><blockquote>
<p>Triggers RESTORED BY DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.075</p>
</blockquote></td>
<td><blockquote>
<p>RESTORED BY DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>ARIE (#886)</p>
<p>Triggered by ‘RESTORED BY’</p>
<p>field (.074)</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time:</p>
<p>This holds the date/time when the patient was ‘restored’ to the board.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>TIME IN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ATI (#794)</p>
</blockquote></td>
<td><blockquote>
<p>Date-and-time field: Contains the time and date when the patient actually</p>
<p>arrived at the emergency</p>
<p>department</p>
<p>EDIS measures patients’ length of visit from this date and time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.09</p>
</blockquote></td>
<td><blockquote>
<p>TIME OUT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ATO (#795)</p>
</blockquote></td>
<td><blockquote>
<p>Date-and-time field: Contains the patient’s discharge time and date</p>
<p>EDIS prompts users for delay reasons based on the difference between time- in and time-out entries</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.1</p>
</blockquote></td>
<td><blockquote>
<p>ARRIVAL MODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the source of the patient’s visit</p>
<p>Currently applies only to the sources of emergency- department visits— nursing homes or clinics, for example; values are associated with the</p>
<p>&lt;stn&gt;.arrival and edp.arrival code sets</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.11</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT BRIEF ID</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ADUP2 (#789)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains the patient’s display-board identifier;</p>
<p>can store identifiers for</p>
<p>patients who are arriving by ambulance and for non-VA patients; the identifier should be in the X9999 format</p>
<p>When VistA patients are selected, the field stores X9999-formatted identifiers that the application constructs from the Patient file (#2); this allows the application to indicate on the display board patients who have identical X9999-formatted identifiers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.12</p>
</blockquote></td>
<td><blockquote>
<p>VISIT</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Visit file (#9000010)</p>
</blockquote></td>
<td><blockquote>
<p>230^AVISIT^MUMPS</p>
<p>(increments and decrements the dependency counter in the Visit file [#9000010])</p>
<p>230^V</p>
<p>(PCE uses this cross reference to help identify dependent entries)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the visit associated with this emergency-department encounter</p>
<p>Because emergency departments don’t normally use appointments, EDIS records patient visits in this field; EDIS can then create visits in PCE so subsequent caregivers can associate orders and progress notes with the same visit; EDIS creates this visit when it collects data for any PCE-related field, allowing it to call DATA2PCE; triage nurses usually enter this data</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.13</p>
</blockquote></td>
<td><blockquote>
<p>CREATION SOURCE</p>
</blockquote></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
<td><blockquote>
<p>A setting to identify the visit-creation source:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>0 (EDIS)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>1 (Scheduling)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>2 (CPRS)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>EDIS generally populates the VISIT field by calling DATA2PCE; users can also create visits by entering emergency- department appointments or writing progress notes for emergency-department locations; this field records the mechanism responsible for creating the entry in the Visit file (#9000010)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.14</p>
</blockquote></td>
<td><blockquote>
<p>CLINIC</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Hospital Location file (#44)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field</p>
<p>Holds a pointer to the specific emergency- department clinic that EDIS will associate with the patient’s visit. When users check in patients through the Scheduling package, EDIS stores a pointer to the clinic they select here until it creates a visit. When the application creates the visit, it uses the location stored in this field</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>COMPLAINT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field: Contains the complaint with which the patient</p>
<p>presented; sites can</p>
<p>include this complaint on the display board, so it should be brief enough to fit within a display-board column; this field accepts 1–50 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>DISPOSITION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s end-of-visit disposition; values for this field are associated with the</p>
<p>&lt;stn&gt;.disposition and edp.disposition code sets</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>DISPOSITION TIME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Time-and-date field: Contains the time and date of the patient’s most</p>
<p>recent disposition-field</p>
<p>update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>DIAGNOSIS TIME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Time-and-date field: Contains the date and time of the patient’s last</p>
<p>diagnosis-field update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>DELAY REASON</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the reason for delay (for patient stays that exceed the maximum length of stay); associated with the &lt;stn&gt;.delay and edp.delay code sets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>COMPLAINT (LONG)</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field The patient’s long</p>
<p>complaint (free text); an</p>
<p>optional field that allows staff to enter complaints in a longer form than EDIS allows for its display-board complaint; this field holds from 1 to 220 characters</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.2</p>
</blockquote></td>
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the record of a patient’s statuses during the course of his or her emergency-department visit (awaiting triage, ED patient, and so forth); associated with the</p>
<p>&lt;stn&gt;.status and edp.status code sets</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.3</p>
</blockquote></td>
<td><blockquote>
<p>ACUITY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s acuity level, which is based on the Emergency Severity Index (ESI) algorithm (acuity levels 1</p>
<p>– 5); associated with the edp.acuity code set</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.4</p>
</blockquote></td>
<td><blockquote>
<p>LOC</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Room-Bed file (#231.8)</p>
</blockquote></td>
<td><blockquote>
<p>AL (#790)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s current location; locations can be a specific room or bed, or a conceptual area (such as the hallway, parking lot, or radiology department); locations need not be physical locations; this field allows checking for unoccupied beds or areas</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.5</p>
</blockquote></td>
<td><blockquote>
<p>MD ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s current physician (provider) assignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.6</p>
</blockquote></td>
<td><blockquote>
<p>NURSE ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s current nurse assignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.7</p>
</blockquote></td>
<td><blockquote>
<p>RESIDENT ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s current resident assignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.8</p>
</blockquote></td>
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field (optional): Contains comments associated with the</p>
<p>patient’s emergency</p>
<p>department stay; users can enter and update this field for patients’ current visits; sites can optionally include comments on the display board; this field accepts 1–80 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 24%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE DIAGNOSIS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (230.4)</p>
</blockquote></td>
<td rowspan="26"></td>
<td><blockquote>
<p>Contains the patient’s diagnosis or diagnoses for this emergency-</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>department visit; when</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>sites have enabled free-</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>text diagnoses, EDIS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>stores patients’ diagnoses</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>lists in this field; when</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>sites have enabled coded</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>diagnoses, this field holds</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>patients’ diagnoses until</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>their PCE visits become</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>available, after which</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>EDIS transfers their</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>diagnoses lists to PCE; in</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>this latter case, PCE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>becomes the real holder of</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>patients’ diagnoses lists;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>however, the lists remain</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>synchronized with EDIS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>to cover rare cases in</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>which sites change</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>parameter settings to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>allow free-text diagnoses;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>the parameter that controls</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>diagnoses lists is in the</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Tracking Area file</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>(#231.9)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>ORDERS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple</p>
</blockquote></td>
<td rowspan="19"></td>
<td><blockquote>
<p>Tracks orders during the</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(230.08)</p>
</blockquote></td>
<td><blockquote>
<p>course of the patient’s</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>emergency-department</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>visit; an order-entry event</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>monitor populates this</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>multiple and identifies</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>orders that are related to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>patients’ current</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>emergency-department</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>visits; the event monitor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>enables EDIS display</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>boards to offer up-to-date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>order-related information</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>with every display-board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>refresh; it also allows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>reports to track the history</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>of orders related to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>emergency-department</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>visits</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Discharge Diagnosis 230.04

> Sites have the option to synchronize patients’ diagnoses with PCE. If diagnoses are synchronized, every time a diagnosis changes in EDIS, the application passes the change to PCE. If sites do not synchronize patients’ diagnoses with PCE, EDIS simply keeps patient-diagnoses lists in this file. Clinical staff can later access the file’s contents and enter patients’ diagnoses into PCE.

### Table 8 Subfile: Discharge Diagnosis Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE DIAGNOSIS</p>
</blockquote></td>
<td rowspan="3"></td>
<td><blockquote>
<p>230.04^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (multiply asked):</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Contains the free text entries of the patient’s discharge diagnoses for the visit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>If sites set EDIS parameters to require coded diagnoses, the text in this field will match ICD-9-CM text from Clinical Lexicon entries; some entries map to more than one ICD code;</p>
<p>$$ICDONE^LEXU</p>
<p>determines which code to store in this field</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>ICD9 CODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the ICD Diagnosis file (#80)</p>
</blockquote></td>
<td rowspan="3"></td>
<td><blockquote>
<p>Pointer field: Contains ICD-9-CM codes for the patient’s</p>
<p>diagnoses</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>The application uses Clinical Lexicon utilities to look up diagnoses; some Clinical Lexicon entries map to more than one ICD 9 CM code; EDIS uses</p>
<p>$$ICDONE^LEXU to determine which code to store here; this becomes</p>
<p>the code that EDIS stores in PCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>The diagnosis-coding system will likely switch from ICD-9-CM to SNOMED CT in the future</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>PRIMARY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>No (secondary)</p></li>
<li><blockquote>
<p>Yes (primary) This setting indicates which diagnosis is the</p>
</blockquote></li>
</ol>
<blockquote>
<p>primary diagnosis</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Orders 230.08

> The order-entry event monitor identifies orders that are related to patients’ current emergency-department visits and populates this multiple with these orders. This subfile enables EDIS to quickly update display boards (which EDIS refreshes every few seconds to provide up-to-date order-status information). It also allows EDIS reporting functionality to track the history of orders that are related to patients’ emergency-department visits.

### Table 9: Subfile: XE Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>230.08^B AO (#784)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (multiply asked):</p>
<p>Contains order IDs for patients’ emergency- department-related orders (order IEN); EDIS uses this field to locate orders when the event monitor needs to update them</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>230.08^AC</p>
</blockquote></td>
<td><blockquote>
<p>A setting:</p>
<p>M (medication) L (lab)</p>
<p>R (radiology) C (consult) A (all others)</p>
<p>Provides a general identification of the service to which orders are related and allows quick checks for orders associated with the patient’s emergency- department visit</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
<p>N (new) A (active)</p>
<p>C (complete)</p>
<p>Provides the general status of orders; sites can use order status to highlight orders on the display board, enabling sites to monitor the board for orders that have been outstanding for too long</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>STAT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
<p>1 (STAT)</p>
<p>0 (not STAT)</p>
<p>A setting of <em>1</em> indicates stat orders; sites can optionally use colors to highlight stat orders on the display board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>RELEASE TIME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Date-and-time field: Contains the date and time of an order’s release to its</p>
<p>service; allows sites to</p>
<p>monitor orders for delay</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Record Indices for File \#230.

### Table 10: Record Indices for File#230

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AC (#787)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, IEN</p>
<p>(active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to list patients with currently active entries on the display board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADUP1 (#788)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, LASTNAME, IEN</p>
<p>(active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to contribute patients’ last names to the ADUP cross reference, which helps identify patients with similar names or similar brief identities (X9999 formatted identifiers)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ADUP2 (#789)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA,</p>
<p>LAST4, IEN (active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to contribute patients’ identifiers in X9999 format</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AL (#790)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, LOC,</p>
<p>IEN (active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to check for beds and areas that are currently occupied</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AN (#791)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, PTNAME, IEN</p>
<p>(active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to check patients’ active statuses in cases where patients do not have DFNs (as is the case with humanitarian interventions); the application references this index before adding patients to the display board to determine whether or not patients are already on the board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AP (#792)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, DFN,</p>
<p>IEN (active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to test for duplicate entries when users select patients who have DFNs (that is, VistA patients) for addition to the display board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ARIE (#886)</p>
</blockquote></td>
<td><blockquote>
<p>RESTORED DATE/TIME,IEN</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to search for patients who were removed in error.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AS (#793)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, SSN,</p>
<p>IEN (active entries only)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to see if patients are already on the display board in cases where patients don’t have DFNs and users are identifying these patients by their SSNs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ATI (#794)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, TIME IN (for</p>
<p>reports)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to get a range of visits within a user-specified time range</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ATO (#795)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, TIME OUT</p>
<p>(for reports)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index to get a range of visits that were closed within a user- specified time span</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PDFN (#801)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, DFN,</p>
<p>IEN (for all patients)</p>
</blockquote></td>
<td><blockquote>
<p>This index organizes all entries by patient DFN. When EDIS performs special lookups against the patient file (by SSN, for example), the lookup service returns a DFN; this index allows EDIS to find visits that correspond to these DFNs; the index contains all visit entries (closed and active)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PN (#796)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, PTNAME, IEN (for</p>
<p>all patients)</p>
</blockquote></td>
<td><blockquote>
<p>EDIS uses this index of <em>all</em> patient names—including the names of patients who do not have DFNs—for selecting patients when visits (closed or otherwise) need to be corrected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  ED Log History (230.1)

> The ED Log History file provides a forward- and reverse-chronological list of updates to each emergency-department log record. The timestamps contained in this file make it possible to generate a variety of reports.

### Table 11: XE ED Log History Files (#230.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>LOG ENTRY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the ED Log file (#230)</p>
</blockquote></td>
<td><blockquote>
<p>230.1^B ADF (#797)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to an entry in the ED Log file; file entries record modifications (updates) to entries in the ED Log file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ADF (#797)</p>
</blockquote></td>
<td><blockquote>
<p>Time-and-date field: Contains the time and date of the log record’s last</p>
<p>modification (if the</p>
<p>patient’s log record was modified)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>ENTERED BY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Contains the identities of users who have updated log data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>The updated value of the patient’s name (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the updated value of the patient’s social security number (if updated)</p>
<p>The class-three product recorded Social Security numbers when patients without DFNs came to the emergency room; EDIS is not currently using this field; the field is present for the sake of compatibility with the class-three version</p>
<p>Patients’ DFNs are their IENs in the Patient file (#2)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Patient file (#2)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the patient’s DFN (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>COMPLAINT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the updated value of the patient’s display- board complaint (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.0701</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>1 (Yes)</p>
<p>0 (No)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.071</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED DATE/TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Triggered by the CLOSED field (.07)</p>
</blockquote></td>
<td><blockquote>
<p>Date-and-time field:</p>
<p>Contains the date/time when the log entry was ‘closed’.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.072</p>
</blockquote></td>
<td><blockquote>
<p>CLOSED BY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Contains the IEN of the user who closed the log entry.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.073</p>
</blockquote></td>
<td><blockquote>
<p>REMOVED IN ERROR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>1 (Yes)</p>
<p>This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.074</p>
</blockquote></td>
<td><blockquote>
<p>RESTORED BY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to New Person file (#200)</p>
</blockquote></td>
<td><blockquote>
<p>Triggers RESTORED BY DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.075</p>
</blockquote></td>
<td><blockquote>
<p>RESTORED BY DATE/TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Triggered by ‘RESTORED BY’</p>
<p>field (.074)</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time:</p>
<p>This holds the date/time when the patient was ‘restored’ to the board.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>TIME IN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Time-and-date field: Contains the updated value of the patient’s arrival time</p>
<p>(if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.09</p>
</blockquote></td>
<td><blockquote>
<p>TIME OUT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Time-and-date field: Contains the updated value of the patient’s departure</p>
<p>time (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.1</p>
</blockquote></td>
<td><blockquote>
<p>ARRIVAL MODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the source of the patient’s visit (a nursing home or hospital ward, for example—if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.11</p>
</blockquote></td>
<td><blockquote>
<p>DISPOSITION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the patient’s disposition (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.12</p>
</blockquote></td>
<td><blockquote>
<p>DELAY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated reason that the patient’s stay exceeded the maximum stay limit (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.14</p>
</blockquote></td>
<td><blockquote>
<p>CLINIC</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Hospital Location file (#44)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the clinic location (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>COMPLAINT (LONG)</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the updated value of the patient’s long complaint (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.2</p>
</blockquote></td>
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the patient’s status (if updated)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.3</p>
</blockquote></td>
<td><blockquote>
<p>ACUITY</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the patient’s acuity (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.4</p>
</blockquote></td>
<td><blockquote>
<p>LOC</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Room-Bed file (#231.8)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the updated value of the patient’s room, bed, or area assignment (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.5</p>
</blockquote></td>
<td><blockquote>
<p>MD ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the identity of the patient’s updated emergency-department physician assignment (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.6</p>
</blockquote></td>
<td><blockquote>
<p>NURSE ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s updated nurse assignment (if updated)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.7</p>
</blockquote></td>
<td><blockquote>
<p>RESIDENT ASSIGNED</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the patient’s updated resident assignment (if updated)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.8</p>
</blockquote></td>
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field Contains updated</p>
<p>comments associated with</p>
<p>the patient’s emergency- department visit (if any— comments are optional)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9.1</p>
</blockquote></td>
<td><blockquote>
<p>MODIFIED FIELDS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free text field:</p>
<p>Contains a list of fields that users modified in the corresponding ED LOG record at the time of the update; the list contains field numbers and is semicolon delimited</p>
</blockquote></td>
</tr>
</tbody>
</table>

5.  Record Indices for File (230.1)

### Table 12: XE File Record Indices: (230.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 30%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADF (#797)</p>
</blockquote></td>
<td><blockquote>
<p>LOG, TIME, IEN</p>
</blockquote></td>
<td><blockquote>
<p>This index provides a forward- chronological list of updates to the log record of a single entry in the ED Log file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

6.  Tracking Staff (231.7)

> The Tracking Staff file contains staff assignments for particular areas (currently sites’ emergency departments). It allows for concise staff -selection lists and enables sites to associate colors with staff members so that emergency-department personnel can more easily tell which staff members are assigned to which patients.

### Table 13: XE Files: Tracking Staff (#231.7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>PERSON</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the New Person file (#200)</p>
</blockquote></td>
<td><blockquote>
<p>231.7^B AD (#807)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the identity of a person who is assigned to work as staff in the emergency department (required)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Institution file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>AC (#800)</p>
<p>AD (#807)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to entries in the Institution file (#4); allows each station to have its own set of staff assignments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>AREA</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Area file (#231.9)</p>
</blockquote></td>
<td><blockquote>
<p>AC (#800)</p>
<p>AD (#807)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field: Points to the area to which the person is</p>
<p>assigned as staff</p>
<p>EDIS currently supports only emergency departments but is capable of supporting other areas in the future</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AD (#800)</p>
</blockquote></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(active)</p></li>
<li><p>(inactive)</p></li>
</ol>
<blockquote>
<p>A setting of <em>1</em> indicates that the person is no longer an active staff member in the associated area</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL ID</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>ROLE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the TRACKING</p>
<p>STAFF file (#232.5)</p>
</blockquote></td>
<td><blockquote>
<p>AC(#873)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the role in the CPE ROLE file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>INITIALS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text:</p>
<p>This is the user’s initials.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>COLOR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field: Contains red-green-blue (RGB) values for the</p>
<p>foreground and</p>
<p>background colors (if any) that sites have used to highlight the staff member’s identifier on the display board</p>
<p>Colors are hexadecimal; this field accepts values having the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff)</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Record Indices for File (231.7)

### Table 14: XE Files Record Indices: (231.7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 27%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AC (#871)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, ROLE, IEN</p>
</blockquote></td>
<td><blockquote>
<p>This cross reference supports constructing a list of currently active staff for a particular role.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 27%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AD (#872)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, DUZ, IEN</p>
</blockquote></td>
<td><blockquote>
<p>This cross reference allows searching the file for an entry matching a particular DUZ (say, to look up a color map). Since a person may work as staff in multiple areas, this cross reference allows finding the staff record that applies to the person's activity in a specific area.</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Tracking Room-Bed (#231.8)

> As patients progress through their visits, they may stop at a number of areas. The Tracking Room-Bed file allows sites to set up these areas in EDIS so that they can track patients throughout their visits. Areas can be physical or conceptual, and may include specific beds, waiting areas, and other areas of the hospital (radiology, exam rooms, and so forth).

### Table 15: XE Files: Tracking Room Bed (#231.8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>231.8^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required): The internal name of the room, bed, or area that the</p>
<p>patient is occupying at this</p>
<p>stage of his visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Institution file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>AC (#802)</p>
<p>C (#803)</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Allows each station (division, for example) to manage its own set of rooms, beds, and areas</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>AREA</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Area file (#231.9)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the hospital area associated with this room, bed, or area; EDIS currently supports only the emergency department, but will probably support additional areas in the future</p>
<p>Trainers can use this field to set up separate areas for each trainee, allowing each trainee to configure his or her own set of rooms and beds</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(active)</p></li>
<li><p>(inactive)</p></li>
</ol>
<blockquote>
<p>A setting of <em>1</em> makes the associated room or area unavailable for selection in EDIS; however, inactive rooms and areas still appear on reports and in views for previous entries</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>SEQUENCE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A number:</p>
<p>Represents the sequential order in which EDIS should display the associated room or area on the big-board display; the field accepts numbers from one (1) to 9999</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AC (#802)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the name of the room or area as it should appear on the big-board display; display names should be concise to save display-board space; supports names from 1–30 characters in length</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY WHEN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(occupied)</p></li>
<li><p>(always)</p></li>
<li><p>(never)</p></li>
</ol>
<blockquote>
<p>A setting of <em>0</em>, <em>1</em>, or <em>2</em> determines whether EDIS should display the associated room or area when occupied, always, or never, respectively</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT STATUS</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the default status (if any) of the room, bed, or area; when sites select a default status for a room, bed, or area, EDIS automatically assigns this default status to patients who are occupying the room, bed, or area</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.09</p>
</blockquote></td>
<td><blockquote>
<p>MULTIPLE ASSIGN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
<p>0 (single—accepts one patient assignment at a time) 1 (multiple—accepts</p>
<p>multiple simultaneous</p>
<p>patient assignments)</p>
</blockquote>
<ol start="2" type="1">
<li><p>(waiting—a special case of the multiple-assignments designation for reporting)</p></li>
<li><p>(single, non-ED—single- assignment designation in an area outside the emergency department)</p></li>
<li><p>(multiple, non-ED— multiple-assignment designation in an area outside the emergency department)</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.1</p>
</blockquote></td>
<td><blockquote>
<p>SHARED NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains a common name for several beds or areas that share the same physical space; using a shared name in such cases allows sites to run reports that identify patients and staff who are at risk for exposure to contagious organisms</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.11</p>
</blockquote></td>
<td><blockquote>
<p>BOARD</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the name of the particular display board on which the room or area is to appear</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.12</p>
</blockquote></td>
<td><blockquote>
<p>COLOR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains values for colors; allows sites to map specific rooms and areas to particular foreground and background colors for use with the display-board’s room-bed-area list; this field accepts values that have the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.13</p>
</blockquote></td>
<td><blockquote>
<p>PRIMARY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – Primary</p>
<p>‘2’ - Secondary</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Record Indices for (#231.8)

### Table 16: XE Files: Record Indices (#231.8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 20%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AC (#873)</p>
</blockquote></td>
<td><blockquote>
<p>SITE, AREA, DISPLAYNAME, IEN</p>
</blockquote></td>
<td><blockquote>
<p>Allows looking for a room with a specific abbreviation,</p>
<p>such as AMBU or WAIT (when setting baseline parameters for example).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C (#874)</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION, AREA</p>
</blockquote></td>
<td><blockquote>
<p>Allows collecting all of the rooms for a specific area within a division (station number).</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Tracking Area (#231.9)

> This file contains parameters that control EDIS’s tracking behavior. It also contains XML descriptions that client software uses to control display -board column appearance, row content, and cell color. The AREA field (#.03) of the ED Log files (#230) points to this file.

### Table 17: XE Files Tracking Area (#231.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>231.9^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field</p>
<p>Contains the name of an area within the hospital; EDIS currently supports only sites’ emergency department areas</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Institution file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>231.9^C</p>
</blockquote></td>
<td><blockquote>
<p>A pointer field:</p>
<p>Allows each station within a given VistA system to have its own set of areas</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>LAST UPDATE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Date-and-time field: Contains the date and time that the site last updated the</p>
<p>display-board configuration;</p>
<p>this helps client software determine if it is necessary to reload configuration parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>DIAGNOSIS REQUIRED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(no)</p></li>
<li><p>(yes)</p></li>
</ol>
<blockquote>
<p>A setting of <em>1</em> indicates that users must enter diagnoses before removing patients from the display board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.11</p>
</blockquote></td>
<td><blockquote>
<p>AMBULANCE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Tracking Room-Bed file (#231.8)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the entry in the Tracking Room-Bed file that represents an arriving ambulance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.12</p>
</blockquote></td>
<td><blockquote>
<p>INITIAL ROOM</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Tracking Room-Bed file (231.8)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to the tracking-file entry that specifies the default room or area (often the waiting room) to which patients are first assigned</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>CODED DIAGNOSIS</p>
</blockquote></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td><blockquote>
<p>A setting:</p>
<p>0 (no—free-text)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>1 (yes—ICD-9-CM)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>A setting of <em>1</em> indicates that users must enter diagnoses using ICD-9-CM codes before removing patients from the board; otherwise, users may enter free-text diagnoses</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>DISPOSITION REQUIRED</p>
</blockquote></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td><blockquote>
<p>A setting: 0 (no)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>1 (yes)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>A setting of <em>1</em> indicates that users must enter patients’ dispositions before removing them from the display board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>DELAY REQUIRED</p>
</blockquote></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td><blockquote>
<p>A setting: 0 (no)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>1 (yes)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>For patients whose emergency-department stays have exceeded the number of minutes identified in the DELAY MINUTES field</p>
<p>(#1.5), unless patients are admitted to an observation ward, a setting of <em>1</em> indicates that users must select a reason for delay before removing the patients from the display board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>DELAY MINUTES</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number field:</p>
<p>Contains the number of minutes after which EDIS requires a reason for delay as a precondition for removing patients from the display board; accepts whole numbers between 1 and 1440</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><strong>Field Name</strong></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>FIRST SHIFT START</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number field:</p>
<p>Contains the number of minutes from midnight to the first shift’s starting time; accepts whole numbers between 0 and 1440; EDIS currently assumes that all shifts are of equal length</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>SHIFT DURATION</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number field:</p>
<p>Contains the number of minutes that comprise the duration of a shift; accepts whole numbers between 0 and 1440; for eight-hour shifts, the value recorded in this field will be 480 (8*60)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.8</p>
</blockquote></td>
<td><blockquote>
<p>PROMPT RESIDENTS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(no)</p></li>
<li><p>(yes)</p></li>
</ol>
<blockquote>
<p>A setting of <em>1</em> indicates that the application must prompt users to enter resident assignments (in addition to provider assignments)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.9</p>
</blockquote></td>
<td><blockquote>
<p>PROMPT CLINICS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
</blockquote>
<ol type="1">
<li><p>(no)</p></li>
<li><p>(yes)</p></li>
</ol>
<blockquote>
<p>A setting of <em>1</em> (yes) indicates that the application must prompt users to select a clinic; this allows EDIS to create visits based on explicitly selected clinics</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>COLOR SPEC</td>
<td></td>
<td></td>
<td><blockquote>
<p>Word-processing field (#231.93) (no wrap): Contains an XML document</p>
<p>that maps colors to display-</p>
<p>board values</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY BOARD CONFIG</p>
</blockquote></td>
<td><blockquote>
<p>Multiple #231.94</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Contains an XML description of each display board’s definition</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References and Record Indices</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>230.1</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING UPDATED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>This timestamp is set whenever the data that is shown on any display board for an area has been updated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>231.1</p>
</blockquote></td>
<td><blockquote>
<p>CHOICES UPDATED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>This is a timestamp that is set whenever the definition of any display board for a given area has been modified.</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Display Board Configuration Subfile (231.94)

### Table 18: XE Files Display Board Configuration Subfile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>231.94^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Contains the name of a specific display board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>SPEC</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Word-processing field #231.941 (no wrap):</p>
<p>Contains the XML description for a specific display board</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Tracking Code (233.1)

> The Tracking Code file contains entries that EDIS tracking functionality uses in selection lists. The software may eventually roll up selection -list entries to the emergency-department director for reporting.

> The following files point to the Tracking Code file:

> ED Log file (#230) ARRIVAL MODE field (#.1)

> ED Log file DELAY REASON field (#1.2)

> ED Log file STATUS field (#3.2)

> ED Log file ACUITY field (#3.3)

> ED Log History file (#230.1) ARRIVAL MODE field (#.1) ED Log History file DISPOSITION field (#.11)

> ED Log History file DELAY field (#.12)

> ED Log History file STATUS field (#3.2)

> ED Log History file ACUITY field (#3.3)

> Tracking Room-Bed file (#233.1) DEFAULT STATUS field (#.08) Tracking Code file (#233.1) NATIONAL CODE field (#.04)

> Tracking Code Set (#233.2) CODE field (#.02) of the CODES

> subfield (233.21)

### Table 19: Tracking Code (#233.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.1^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains unique names for values in the</p>
<p>selection lists that EDIS</p>
<p>is using.</p>
<p>To distinguish local list selections from national list selections, EDIS prefixes locally defined entries with sites’ station numbers and nationally defined entries with the letters <em>edp</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AB (#804)</p>
<p>AC (#805)</p>
</blockquote></td>
<td><blockquote>
<p>Free text field: Contains the selection’s display-board name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>ABBREVIATION</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AB (#804)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains display-name abbreviations that EDIS</p>
<p>uses in some reports</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL CODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Tracking Code file (#233.1)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Will contain mappings from site-defined codes to national codes when national codes exist</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>FLAGS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>EDIS uses flags to further classify specific codes; possible flags are:</p>
<p>M (Missed opportunity) A (Admission)</p>
<p>VA (VA admission) O (Observation)</p>
<p>EDIS allows multiple flags with no delimiters</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Word processing field (#233.12):</p>
<p>Contains a further explanation: allows sites to further explain codes (233.12)</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  Tracking Code file (#233.1)

### Table 20: Tracking Code file (#233.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Record Index</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indexed Fields</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AB (#875)</p>
</blockquote></td>
<td><blockquote>
<p>NAME (without prefix), ABBREVIATION</p>
</blockquote></td>
<td><blockquote>
<p>This allows finding all the abbreviations for a name without regard to the site prefix. (The prefix is "edp."</p>
<p>when nationally exported, "nnn." for locally defined, where nnn is the station number.)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AC (#876)</p>
</blockquote></td>
<td><blockquote>
<p>NAME (without prefix), DISPLAY NAME</p>
</blockquote></td>
<td><blockquote>
<p>This allows finding all the display names for a name without regard to the site prefix. (The prefix is "edp."</p>
<p>when nationally exported, "nnn." for locally defined, where nnn is the station number.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

5.  Tracking Code Set (#233.2)

> The Tracking Code Set file contains collections of codes that represent specific selection lists (acuities, patient statuses, dispositions, delay reasons, and so forth) used within EDIS.

### Table 21: Tracking Code Set (#233.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.2^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required): Contains the names of tracking code sets that</p>
<p>EDIS uses in selection</p>
<p>lists; sites may modify selection lists to meet their needs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CODES</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (#233.21)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Contains lists of codes that are available in selection lists</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 5.2.1.16. Codes (233.21)

### Table 22: Subfile: Tracking Code Set file - Codes (#233.21)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>SEQUENCE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.21^B</p>
</blockquote></td>
<td><blockquote>
<p>Number field (multiply asked):</p>
<p>Contains a number that indicates the order in which the associated code should appear in the selection list; accepts whole numbers between 1 and 9999</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the Tracking Code file (#233.1)</p>
</blockquote></td>
<td><blockquote>
<p>233.2^AS^MUMPS</p>
</blockquote></td>
<td><blockquote>
<p>Pointer field:</p>
<p>Points to codes that are to be included in selection lists</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>A setting:</p>
<p>1 (inactive)</p>
<p>0 (active)</p>
<p>A setting of <em>1</em> indicates codes that are temporarily inactivated</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>NAME AT SITE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.2^AS^MUMPS</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains site-specific names; allows sites to</p>
<p>use different names for</p>
<p>display purposes without changing underlying national codes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>ABBREVIATION AT SITE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.2^AS^MUMPS</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field: Contains site-specific abbreviations: allows</p>
<p>sites to use different</p>
<p>abbreviations for national-code abbreviations without changing the underlying meaning of the national codes</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 5.2.1.17. CPE Role (#232.5)

> The CPE Role file contains the definitions for roles to be used with EDIS.

### Table 23: CPE Role (#232.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference s</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>ROLE</p>
</blockquote></td>
<td><blockquote>
<p>USR CLASS (#8930)</p>
</blockquote></td>
<td><blockquote>
<p>232.5^B</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the USR CLASS file This field</p>
<p>contains the role</p>
<p>used for the clinical practice environment.</p>
<p>Clerk, Nurse, Provider &amp; Resident</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>ABBREVIATION</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.5^C</p>
</blockquote></td>
<td><blockquote>
<p>Free text (Required)</p>
<p>This index holds the abbreviation as well as</p>
<p>the IEN for each role.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference s</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote>
<p>1</p>
<p>al Manual</p></td>
<td><blockquote>
<p>XML ABBREVIATION</p>
</blockquote>
<p>52</p></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free text (Required) This is the xml abbreviation for the role.</p>
<p>Previously, logic had been hardcoded to check the role type.</p>
<p>'P' = "@md" 'N' =</p>
<p>"@rn" 'R' = "@res"</p>
<p>These values will remain the same, however they are now part of the file, and can be more easily enhanced to add roles in the future. The roles will now be able to be built without having to release a kids build to do so. All role setting are now table driven.</p>
<p>This is accessed and used to build information out of the CLRSTAFF tag in EDPQDBS.</p>
</blockquote>
<p>: Any</p>
<blockquote>
<p>time a new role is</p>
<p>added, the UI will need</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference s</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT WORKSHEET</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP WORKSHEET SPECIFICATION</p>
<p>file (#232.6)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Point to the EDP WORKSHEET SPECIFICATIO</p>
<p>N file</p>
<p>This is the default worksheet for this role.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT BOARD</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free Text</p>
<p>This contains the name of the default board for this role.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>ALLOW ACUITY EDIT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘0’ – No</p>
<p>‘1’ – Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>XML STAFF NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free Text</p>
<p>This holds the staff name that is related to building the XML needed for the client portion of the application. This is built from the LOAD</p>
<p>tag in EDPBST.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 5.2.1.18. EDP Worksheet Specification (#232.6)

> The EDP Worksheet Specification file holds worksheet definitions for each institution/area. The EDP Worksheet Specification file also allows worksheets to be associated with user roles.

### Table 24: EDP Worksheet Specification (#232.6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.6^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>Contains the names of worksheets to be used with EDIS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION (#4)</p>
</blockquote></td>
<td><blockquote>
<p>232.6^C</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the INSTITUTION file:</p>
<p>Contains the institution associated with this worksheet.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>AREA</p>
</blockquote></td>
<td><blockquote>
<p>TRACKING AREA (#231.9)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to the TRACKING AREA</p>
<p>file:</p>
<p>The tracking area associated with this worksheet.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>‘V’ for Visit ‘A’ for Assess ‘P’ for Plan</p>
<p>‘E’ for Edit Closed</p>
<p>This is the type of this worksheet.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>ROLE</p>
</blockquote></td>
<td><blockquote>
<p>USR CLASS (#8930)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to the USR CLASS file Identifies the role</p>
<p>associated with this</p>
<p>worksheet.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>DISABLED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
</blockquote>
<ol type="1">
<li><p>– False</p></li>
<li><p>– True</p></li>
</ol>
<blockquote>
<p>This indicates whether this worksheet is disabled or not.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>EDITABLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ – False</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>SPEC</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Word Processing (NOWRAP)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SECTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple #232.62</p>
</blockquote></td>
<td rowspan="4"></td>
<td><blockquote>
<p>This multiple holds ‘instances’ of the</p>
<p>sections</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>from the EDP WORKSHEET</p>
<p>SECTION file. Each</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>instance is tied to the worksheet so that its</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>behavior can change on a case by case basis.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>5.2.1.19.</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Subfile: Sections (#232.62)</strong></p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SECTION SEQUENCE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SECTION</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP Worksheet Section file (#232.71)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INITIALLY OPEN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘0’ – False</p>
<p>‘1’ - True</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CONFIGURATION</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Word Processing (NOWRAP)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>COMPONENTS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple to #232.622</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>The component multiple points to the EDP WORKSHEET</p>
<p>COMPONENTS file as an 'instance' of the component. This holds specific behavioral flags for this component, as it exists within this worksheet/section.</p>
</blockquote></td>
</tr>
</tbody>
</table>

20. Subfile: Components (#232.622)

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>COMPONENT SEQUENCE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.66^B</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>COMPONENT</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP Worksheet Component file (#232.72)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>EDITABLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ - False</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>VISIBLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ - False</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>INCLUDE IN SUMMARY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ - False</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Multiple #232.63</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

21. Subfile: Roles (#232.63)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>Roles</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to CPE Role File (#232.5)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

22. EDP Worksheet Section (#232.71)

> The Worksheet Section file holds the definitions for each section of a worksheet.

### Table 25: EDP Worksheet Section (#232.71)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.71^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>This field holds the name of the worksheet section.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C (#891)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Holds the package information</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>SUMMARY PLUGIN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT DISPLAY NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>TASK TYPE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>‘0’ – None</p>
<p>‘1’ – Checkbox</p>
<p>‘2’ – Timed</p>
<p>This field contains the ‘type’ associated with this worksheet.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>INITIALLY OPEN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
</blockquote>
<ol type="1">
<li><p>– False</p></li>
<li><p>– True</p></li>
</ol>
<blockquote>
<p>This indicates whether or not the worksheet section should be open or closed initially.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>COMPONENTS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (232.711)</p>
<p>Pointer to EDP WORKSHEET COMPONENT</p>
<p>file (#232.72)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to EDP WORKSHEET COMPONENT (#232.72) file:</p>
<p>This field holds the components that will be used in this worksheet section.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to multiple (#232.712)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

20. Subfile: Components (#232.711)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>COMPONENT</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP Worksheet Component file (#232.72)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to multiple (#232.712)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

21. Subfile: Roles (#232.712)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
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
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to CPE ROLE FILE (#232.5)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

22. EDP Worksheet Component (#232.72)

> The Worksheet Component file holds the definition for each worksheet component.

### Table 26: EDP Worksheet Component (#232.72)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.72^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>Indicates the name of the worksheet component.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>LABEL</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C (#892)</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>This holds the label for the worksheet component.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>DATA PROVIDER</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text Computed field: PACKAGE::CLASS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘R’ – Reference</p>
<p>‘V’ - Visit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>MONIKER</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>Unknown purpose</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>WIDGET NAME</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP Worksheet Component Type file #232.73</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.07</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE LINK</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to Package file #9.4</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>VALUE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.09</p>
</blockquote></td>
<td><blockquote>
<p>SUMMARY LABEL</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.1</p>
</blockquote></td>
<td><blockquote>
<p>SUMMARY ORDER</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.11</p>
</blockquote></td>
<td><blockquote>
<p>AVAILABLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ – False</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.12</p>
</blockquote></td>
<td><blockquote>
<p>VISIBILITY TRIGGER</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>ASSOCIATED FILE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>ASSOCIATED FIELD</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>LOAD EVENT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td><blockquote>
<p>LOAD API</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.2</p>
</blockquote></td>
<td><blockquote>
<p>SAVE API</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ALTERNATE LOAD LOGIC</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.1</p>
</blockquote></td>
<td><blockquote>
<p>PREVIEW TAG</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.2</p>
</blockquote></td>
<td><blockquote>
<p>PREVIEW ROUTINE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>ALTERNATE SAVE LOGIC</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (#232.725)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>DEFAULT VALUE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>REQUIRED COMPONENTS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple to #232.727</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to #232.728</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>VALIDATOR</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to #232.729</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

23. Subfile: Parameters (#232.725)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>PARAMETER NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.725^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>DATA TYPE</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>Set of codes: ‘S’ – String ‘N’ - Numeric</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>SAVE/LOAD TYPE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>‘S’ – For save only ‘L’ - For load only</p>
<p>‘B’ – For both load and save</p>
</blockquote></td>
</tr>
</tbody>
</table>

24. Subfile: Components (#232.727)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>REQUIRED COMPONENTS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.727^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
</tbody>
</table>

25. Subfile: Roles (#232.728)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to CPE ROLE FILE (#232.5)</p>
</blockquote></td>
<td><blockquote>
<p>232.727^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
</tbody>
</table>

26. Subfile: Validator (#232.729)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>VALIDATOR</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP</p>
</blockquote></td>
<td><blockquote>
<p>232.727^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>COMPONENT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>VALIDATORS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(#232.74)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>PROPERTY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>‘1’ - text</p>
<p>‘2’ - selectedIndex</p>
<p>‘3’ - _SelectedDate</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>MAX LENGTH</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>REUQIRED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – true</p>
<p>‘0’ – false</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>MIN VALUE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>LOWER THAN MIN ERROR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Table 29: EDP Worksheet Component Type(#232.73)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross References</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.73^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (Required):</p>
</blockquote></td>
</tr>
</tbody>
</table>

27. NHAMCS Reason for Visit (#233.8)

> The NHAMCS Reason for visit file holds reasons for visits.

### Table 27: NHAMCS Reason for Visit (#233.8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.8^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>Contains the name of the reason for visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.8^C</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>The code value associated with this reason for visit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>PARENT CODE</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT (233.8)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to NHAMCS REASON FOR VISIT FILE:</p>
<p>Holds the parent visit code (if this is a child code).</p>
</blockquote></td>
</tr>
</tbody>
</table>

28. NHAMCS Reason for Visit Display (#233.81)

> The NHAMCS Reason for Visit display file contains the display for an entry in the NHAMCS Reason for Visit file.

### Table 28: NHAMCS Reason for Visit Display (#233.81)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td rowspan="4"></td>
<td><blockquote>
<p>233.81^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>233.81^D</p>
</blockquote></td>
<td><blockquote>
<p>(required):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Contains the name of the</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>reason for visit display.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS CODE</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT (233.8)</p>
</blockquote></td>
<td><blockquote>
<p>233.81^C</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to NHAMCS REASON FOR VISIT</p>
<p>file:</p>
</blockquote></td>
</tr>
</tbody>
</table>

29. ED Complaint (#233.82)

> The ED Complaint file holds the ED complaints as well as the associated NHAMCS codes, attributes, and possible values.

### Table 29: ED Complaint (#233.82)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.82^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>Contains the name of the reason for this ED complaint.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS CODE</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to NHAMCS REASON FOR</p>
<p>VISIT</p>
<p>DISPLAY (#233.81)</p>
</blockquote></td>
<td><blockquote>
<p>233.81^C</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to NHAMCS REASON FOR VISIT</p>
<p>DISPLAY file:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>ATTRIBUTE</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (#233.821)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ASSOCIATED SYMPTOM</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (233.822)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

30. Attribute (233.821)

### Table 30: Attribute (#233.821)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.821^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text field (required):</p>
<p>This is the attribute that will be prompted to the user in the note template when this complaint is selected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>POSSIBLE VALUE</p>
</blockquote></td>
<td><blockquote>
<p>Multiple (#233.8211)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Contains a list of possible values for this attribute.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY TEXT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field: Contains the display value:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS</p>
<p>Code</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT DISPLAY (#233.81)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to NHAMCS RESASON FOR VISIT DISPLAY:</p>
<p>Contains the NHAMCS reason for visit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

31. Possible Value (#233.8211)

### Table 31: Possible Value (#233.8211)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>SEQUENCE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.8211^B</p>
</blockquote></td>
<td><blockquote>
<p>Number:</p>
<p>Sequence for this value</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY TEXT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>This is the display text for this possible value.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS CODE</p>
</blockquote></td>
<td><blockquote>
<p>NHAMCS REASON FOR VISIT DISPLAY (#233.81)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pointer to NHAMCS REASON FOR VISIT DISPLAY</p>
<p>This contains the reason for visit display value.</p>
</blockquote></td>
</tr>
</tbody>
</table>

32. Associated Symptom (#233.822)

### Table 32: Associated Symptom (#233.822)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>SEQUENCE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.822^B</p>
</blockquote></td>
<td><blockquote>
<p>Number:</p>
<p>Sequence for this value</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>This is the name of the associated symptom.</p>
</blockquote></td>
</tr>
</tbody>
</table>

33. Clinical Events (#234)

> The Clinical events file tracks the date/time of clinical events along with vitals, medication, orderable items, and labs associated with the events.

### Table 33: Clinical Events (#234)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>DATE/TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>234^B</p>
<p>234^AL</p>
<p>234^AV</p>
</blockquote></td>
<td><blockquote>
<p>Date/time (required):</p>
<p>This is the date/time of the clinical event.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>TITLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>This is the title of the event, which will be displayed on data graphs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file</p>
</blockquote></td>
<td><blockquote>
<p>234^C</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to PATIENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(#2)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>file:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>This is the patient for</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>this event.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>USER</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
<p>file (#200)</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Pointer to the NEW PERSON file:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>This is the user responsible for creating this event.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>TREATMENT</p>
</blockquote></td>
<td><blockquote>
<p>ORDERABLE</p>
<p>ITEMS file (#101.43)</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Pointer to the ORDERABLE ITEMS</p>
<p>file:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>This is the medication or treatment the patient was receiving at the time of this event.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>LAB TEST</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to the LABORATORY</p>
<p>TEST file (#60)</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Pointer to the LABORATORY TEST</p>
<p>file:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>This is the lab test used to monitor the efficacy of this treatment, and whose result triggered this event.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>VITAL SIGN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes:</p>
<p>‘BP’ – Blood Pressure</p>
<p>*Note* - this DD field appears to be incomplete.. Only BP is listed in the set of codes*</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text field:</p>
<p>The description of this event.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark34" class="anchor"></span>Table 34: EDP Report Template (#232.1)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>233.822^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text (Required)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ – False</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>EDITABLE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Set of codes: ‘1’ – True</p>
<p>‘0’ – False</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>DISPLAY ELEMENTS</p>
</blockquote></td>
<td><blockquote>
<p>Multiple to #232.12</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Multiple to (#232.13)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

34. Subfile: Sequence (#232.12)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>SEQUENCE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>ELEMENT</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to EDP Report Elements file (#232.11)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

35. Subfile: Roles (#232.13)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>ROLES</p>
</blockquote></td>
<td><blockquote>
<p>Pointer CPE ROLE FILE (#232.5)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Table 35: EDP Report Elements (#232.11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pointers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cross Reference</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>232.11^B</p>
</blockquote></td>
<td><blockquote>
<p>Free-text (Required)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>FILE #</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>FIELD #</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td><blockquote>
<p>HISTORY FIELD #</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>HEADER</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>FORMAT LOGIC</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>EXECUTABLE LOOKUP</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Free-text</p>
</blockquote></td>
</tr>
</tbody>
</table>

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/020.png)Exported Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDPCBRD RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This RPC acts as the front controller for the EDIS display board. It accepts requests that the Java middle tier initially passes to the EDIS Web server. The RPC uses these parameters to determine which command to execute. EDPCBRD allows proxy-user access.

> Input parameter SESS identifies requesting users and sites, which the application passes in via its Java middle tier.

> Input parameter PARAMS is a list of the parameters that the application passes to the Java middle tier via Hypertext Transfer Protocol ( HTTP) post messages.

> EDPCBRD RPC formats and returns data as Extensible Markup Language (XML) documents. The XML structure varies based on the nature of the data request.

### EDPCTRL RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This RPC acts as the front controller for the EDIS tracking application. It accepts requests that the Java middle tier initially passes into the EDIS Web server. The RPC uses the PARAMS parameter to determine which command to execute. The PARAMS parameter is a list of the parameters that users pass to the system’s Java middle tier via HTTP post messages. The RPC’s returned data are formatted as XML documents, the structure of which varies based upon the types of data requests.

### EDPGLOB RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This RPC utilized global arrays to store and return data rather than the previous RPC’s which used only local arrays. During testing, errors were encountered due to stack sized getting too large in the local arrays. Creating and using this RPC for the calls that are more data intensive creates a way to avoid these stack \<STORE\> errors for larger amounts of data. In the future, if the amount of data is in question, this RPC should be used to avoid any potential issues. Currently this RPC is being used for Lab data retrieval, Worksheet.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/021.png)Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 36: EDIS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDP CONVERSION</p>
</blockquote></td>
<td><blockquote>
<p>Run Routine</p>
</blockquote></td>
<td><blockquote>
<p>Allows sties to trigger the conversion of local data in their ^DIZ(1720xx) files to the new EDIS files; the option uses routine EDPFMOVE, which transfers local configuration data first, followed by all currently open visits; EDPFMOVE also queues a task to copy closed visits, thus permitting reporting functionality to run normally</p>
<p>Uppercase menu text: CONVERT LOCAL ER DATA TO EDIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF BIGBOARD KIOSKS</p>
</blockquote></td>
<td><blockquote>
<p>Action</p>
</blockquote></td>
<td><blockquote>
<p>Allows facilities to edit the EDPB BIGBOARD KIOSKS parameter; editing parameter values via XPAR utilities is prohibited</p>
<p>Entry Action: D EN^EDPBKS</p>
<p>Uppercase menu text: DISPLAY BOARD KIOSKS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING MENU ALL</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access to all EDPF TRACKING VIEW options Timestamp: 61055,41714</p>
<p>Uppercase menu text: ALL TRACKING VIEWS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING MENU CLINICIAN</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access to EDPF TRACKING VIEW options typically associated with clinicians (the <strong>Update</strong>, <strong>Disposition</strong>, and <strong>Display Board</strong> views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: CLINICIAN TRACKING VIEWS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING MENU SIGNIN</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access to the EDPF TRACKING VIEW options associated with signing in patients to the emergency department (the <strong>Sign In</strong> and <strong>Display Board</strong> views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: SIGN-IN TRACKING VIEWS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING MENU TRIAGE</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access to the EDPF TRACKING VIEW options associated with triaging patients (the <strong>Triage</strong> and <strong>Display Board</strong> views)</p>
<p>Timestamp: 61055,41714</p>
<p>Uppercase menu text: TRIAGE TRACKING VIEWS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>Broker (client- server)</p>
</blockquote></td>
<td><blockquote>
<p>A context option for EDIS remote procedure calls (RPCs) at local facilities; the option uses EDPCTRL RPC and EDPCBRD RPC; assigning any EDPF TRACKING MENU or EDPF TRACKING VIEW</p>
<p>option implicitly provides users with access to this option</p>
<p>Uppercase menu text: EDIS VERSION 1.0-T28</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING VIEW BOARD</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Display Board</strong></p>
<p>view</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: DISPLAY BOARD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING VIEW CONFIGURE</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Configure</strong></p>
<p>view</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: CONFIGURE TRACKING BOARD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING VIEW DISPOSITION</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Disposition</strong></p>
<p>view</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: DISPOSITION PATIENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING VIEW EDIT CLOSED</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Edit Closed</strong> view, which allows users to change any emergency department visit; assign this view to users who are authorized to correct data discrepancies; access should be limited; EDIS logs all changes</p>
<p>Timestamp: 61514,54336</p>
<p>Uppercase menu text: EDIT CLOSED PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING VIEW REPORTS</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Reports</strong> view; security keys further restrict access to some reports Timestamp: 61514,54336</p>
<p>Uppercase menu text: TRACKING REPORTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING VIEW SIGNIN</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Sign In</strong> view Timestamp: 61514,54336</p>
<p>Uppercase menu text: SIGN IN PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING VIEW STAFF</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Assign Staff</strong></p>
<p>view for configuring staff assignments Timestamp: 61514,54336</p>
<p>Uppercase menu text: ASSIGN STAFF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPF TRACKING VIEW TRIAGE</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Triage</strong> view Timestamp: 61514,54336</p>
<p>Uppercase menu text: TRIAGE PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDPF TRACKING VIEW UPDATE</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Provides access specifically to the EDIS <strong>Update</strong> view Timestamp: 61514,54336</p>
<p>Uppercase menu text: UPDATE TRACKING BOARD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPS BOARD CONTEXT</p>
</blockquote></td>
<td><blockquote>
<p>Broker (client- server)</p>
</blockquote></td>
<td><blockquote>
<p>Uses EDPCBRD RPC to set the tracking board’s context</p>
<p>Uppercase menu text: ED TRACKING BOARD CONTEXT</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDPSERVER</p>
</blockquote></td>
<td><blockquote>
<p>Server</p>
</blockquote></td>
<td><blockquote>
<p>Uses the EDPMAIL routine to process incoming scheduling events from VA MailMan</p>
<p>Uppercase menu text: PROCESS INCOMING SCHEDULING EV</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Include EDIS Options in Users’ Menu Trees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Include one or more of the following options in each user’s menu tree:

- EDPF TRACKING MENU ALL
- EDPF TRACKING MENU CLINICIAN
- EDPF TRACKING MENU SIGNIN
- EDPF TRACKING MENU TRIAGE
- EDPF TRACKING VIEW BOARD
- EDPF TRACKING VIEW CONFIGURE
- EDPF TRACKING VIEW DISPOSITION
- EDPF TRACKING VIEW EDIT CLOSED
- EDPF TRACKING VIEW REPORTS
- EDPF TRACKING VIEW SIGNIN
- EDPF TRACKING VIEW STAFF
- EDPF TRACKING VIEW TRIAGE
- EDPF TRACKING VIEW UPDATE

> Note: The KIDS installation process does not rebuild VistA menu trees before you assign new EDIS menus. You must therefore perform a menu rebuild after you assign these menus for the first time. If you do not, graphical user interface (GUI) applications like EDIS won’t know who has access to the new options. Again, performing a menu rebuild is necessary only once, and only for menus that have never before been assigned *.*

### Assign EDIS Views to Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Work with your site’s clinical application coordinators ( CACs) and emergency- department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views that he or she needs.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type *1* (for EVE Systems Manager Menu) and press the

> \<Enter\> key.

4.  At the Select Systems Manager Menu Option prompt, type *User Management* and press the \<Enter\> key.
5.  At the Select User Management Option prompt, type *Edit* (for Edit an Existing User) and press the \<Enter\> key.
6.  At the Select NEW PERSON NAME prompt, type the user’s name using the following format: lastname,firstname. Press the \<Enter\> key. VistA displays the Edit an Existing User dialog.
7.  In the Edit Existing User dialog, press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark \[*?*\] to see a list of the secondary options that are currently assigned to the user.)
8.  Type in the secondary menu options field one of the options listed above and then press the \<Enter\> key:
9.  At the Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No// prompt, type *Yes* and press the \<Enter\> key.
10. Press the \<Enter\> key again to accept this new option.
11. In the SYNONYM field, type a synonym for the option (optional). Press the \<Enter\> key.
12. Press the \<Enter\> key to close the COMMAND field and return to the Select

> SECONDARY MENU OPTIONS field.

13. Repeat steps 8 through 11 to assign other options as necessary.
14. Press the \<Down Arrow\> key to move through the Edit Existing User dialog. At the end of each page, type the letter *n* in the COMMAND field to enter the following page.
15. Stop on page 3.
16. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active.
17. If the user’s person class is not active, select an active person class for the user.
18. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
19. At the Save changes before leaving form (Y/N)? prompt, type the letter *Y* and press the \<Enter\> key.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/022.png)Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses Kernel Authentication and Authorization for J2EE (KAAJEE) to authenticate users. KAAJEE enables Java applications to use VistA security features. Specifically, it authenticates users against your local VistA (M) system and uses VistA options and security keys to authorize access to role-based functionality.

> KAAJEE also transforms VistA login credentials into J2EE-compatible login credentials. For more information about KAAJEE, visit [<u>http://vista.med.va.gov/kernel/kaajee</u>](http://vista.med.va.gov/kernel/kaajee).

## Secure Sockets Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses Secure Sockets Layer (SSL) to secure communications between the EDIS Web server and sites’ display boards. To set up these two-way secure communications for each machine that will power a display board, you must first set up the display board to run in kiosk mode. Kiosk mode locks down the machine’s user interface to protect the application from accidental or deliberate misuse. You must then contact the VA National Helpdesk at 888.596.4357 or create a Remedy ticket. If you call the helpdesk, inform the helpdesk analyst that you are making a display-board setup request. If you create a Remedy ticket, select the Display Board Setup Request option.

> The helpdesk analyst will add the computer to a group that enables it to automatically receive its SSL certificate for two-way authentication. This group also forces a lockdown on the machine to run in kiosk mode. See the EDIS Server Installation Guide for detailed instructions on setting up large display boards.

### PKI Encryption Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To encrypt communications between the EDIS Web-application server and browsers that sites are using to run their display boards, the server and browsers exchange certificates containing their public keys.

> After this exchange takes place, the browser sends a random number that it has encrypted using the server’s public key. The server decrypts this number using its private key. The browser and server then use this random number to generate session keys, which they use in conjunction with their private keys to encrypt and decrypt data exchanges during the communications session.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDPF KIOSKS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key grants access to the EDPF BIGBOARD parameter. This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.

### EDPR EXPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key enables holders to export EDIS reports to Microsoft Excel.

### EDPR PROVIDER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key enables holders to view and run the EDIS Provider report, which lists statistics for each emergency department provider.

### EDPF WORKSHEETS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key controls access to the ability to modify worksheet configurations (this MAY be removed before release).

### EDPR ADHOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key has been added to control access to adhoc reports.

### EDPR XREF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This security key enables holders to view and run the EDIS Cross Reference (XRef) report, which matches emergency department visit numbers with associated patient-identity information.

### Assign Keys for Emergency Department Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign keys to users who need access to additional reporting capabilities.

1.  Log in to VistA
2.  At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and then press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type *menu* (for Menu Management) and then press the \<Enter\> key.
5.  At the Select Menu Management Option prompt, type the word *key* (for Key Management) and then press the \<Enter\> key.
6.  At the Select Key Management Option prompt, type the word *allocation* (for

### Allocation of Security Keys).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  At the Allocate key prompt, type the name of the security key you want to assign—*EDPF EXPORT*, for example.
8.  At the Holder of key prompt, type the name of the first user to whom you are assigning the key and then press the \<Enter\> key.
9.  At the Another holder prompt, type the name of a second user to whom you are assigning the key and then press the \<Enter\> key. Repeat this step for all users to whom you are assigning the key
10. At the You are allocating keys. Do you wish to proceed? YES// prompt, press the \<Enter\> key to accept the default response.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/023.png)Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDP CHECK-IN monitors local VistA systems for Scheduling-package events that indicate VA personnel are checking patients into the emergency department. This protocol is placed on the SDAM APPOINTMENT EVENTS protocol, which is an appointment-event driver.

> EDP MONITOR monitors order events for the EDIS display board. This protocol is placed on the \* EVSEND OR protocols to check for updates that ancillary packages send to the Order Entry/Results Reporting package. (The asterisk in the expression *\* EVSEND OR* stands as a placeholder for other package namespaces, such as PS or RA.) It monitors when ancillary packages transmit orders and when they complete the orders.

> EDP NEW PATIENT defines variables to support some of the devices that previously monitored SDAM APPOINTMENT EVENTS. The application processes this protocol when users or applications add new patients to the board. Items may look for EDPDATA (EDPDATA = ED Log IEN^DFN^Time In^Hospital Location IEN). This protocol also defines the following variables:

- DFN = Patient file (#2) IEN
- SDT = Time In
- SDCL = Hospital Location file (#44) IEN
- SDATA = ^DFN ^ SDT ^ SDCL
- SDAMEVT = 1 (unscheduled new visit)

> EDP OR MONITOR monitors ordering events for the EDIS display board. It is placed on the \* EVSEND OR protocols to look for order numbers that are assigned to new orders from ancillary packages.

> EDPF ADD BOARD provides support for an entry action (D ADD^EDPBKS) that adds a display board.

> EDPF BIGBOARD MENU defines the menu of actions for the EDPF BIGBOARD KIOSKS list template. This protocol allows facilities to edit the EDPF BIGBOARD KIOSKS parameter. Menu items include:

- EDPF ADD BOARD (sequence 11)
- EDPF REMOVE BOARD (sequence 12)
- EDPF CHANGE BOARD (sequence 21)
- EDPF SELECT DIVISION (sequence 31)
- EDPF QUIT (sequence 32)
- EDPF BLANK 1 (sequence 22)
- EDPF BLANK 2 (sequence 13)
- EDPF BLANK 3 (sequence 23)

> EDPF BLANK 1 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

> EDPF BLANK 2 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

> EDPF BLANK 3 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

> EDPF CHANGE BOARD supports entry action D CHG^EDPBKS, which changes a computer name or display board.

> EDPF QUIT supports entry action Q, which exits the EDPF BIGBOARD KIOSKS list template.

> EDPF REMOVE BOARD supports entry action D REM^EDPBKS, which removes a display board.

> EDPF SELECT DIVISION supports entry action D NEWDIV^EDPBKS, which allows the EDIS editor to switch to values for another division.

## Other Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FH EVSEND OR sends Health Level 7 (HL7) messages from the Dietetics package to the Order Entry/Results Reporting package.

> GMRC EVSEND OR sends consult requests and tracking data to the Order Entry/Results Reporting package.

> LR70 CH EVSEND OR sends orders from the Laboratory package to the Order Entry/Results Reporting package.

> OR EVSEND FH sends diet-message events.

> OR EVSEND GMRC sends consult-message events. OR EVSEND LRCH sends laboratory-message events. OR EVSEND ORG sends generic event messages.

> OR EVSEND PS sends pharmacy-message events.

> OR EVSEND RA sends radiology and imaging events.

> PS EVSEND OR sends inpatient and outpatient medication orders from the Pharmacy package to the Order Entry/Results Reporting package.

> RA EVSEND OR sends radiology and imaging message events to the Order Entry/Results Reporting package.

> SDAM APPOINTMENT EVENTS performs all necessary actions associated with Scheduling-package events (such as patient check in).

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/024.png)List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EDIS List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDPF BIGBOARD KIOSKS maps fully qualified machine names to the names of EDIS big-board displays.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/025.png)Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Check-in via Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If EDIS does not automatically add patients when users create an appointment for them or check them in via the Scheduling package, make sure your site's emergency- department location is set in the EDPF LOCATION parameter. Check this parameter to ensure that its value coincides with the value of your emergency department location in file \#44 (Hospital Location). EDIS uses values in the EDPF LOCATION parameter to add patients to its log when you create appointments for, or check in, emergency-department visits.

## Blank View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If users don’t see view selections when they log in to EDIS, you may not have assigned EDIS options for them. Users need at least one assigned option to access EDIS views. If users already have one or more assigned options, you may need to rebuild your site's menu trees in VistA. Rebuilding menus is necessary only after you assign new menu options for the first time.

## PCE Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS creates a Patient Care Encounter (PCE) encounter in CPRS when users select a provider or diagnosis in EDIS. If this functionality isn’t working at your site, check:

- The location entry in the EDPF LOCATION parameter
- Physicians’ and nurses’ person-class status

### Check the EDPF LOCATION Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses the entry in this parameter to create PCE encounters in CPRS.

### Check for Active Person Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before EDIS creates PCE encounters based on physician, nurse, or resident assignments, it checks to make sure the physician, nurse, or resident has an active person class. If a user selects a provider whose person class is expired, EDIS does not create an encounter based on the user’s selection. To remedy this problem, check each person's class for each provider on your site’s staff pick lists.

## Nurse Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> By default, EDIS bases its nursing-staff list on all entries in the New Person file (#200). Sites can elect to have EDIS filter its nurse-selection list to allow only people who hold the ORELSE security key, only people who hold the PSJ RNURSE security key, or only people who are present and active in the Nurse Staff file (#210).

> If you do not see emergency-department nurses when you are using the Assign Staff view to create the EDIS Nurse pick list, check the status of your site’s emergency- department nursing staff in the Nurse Staff file. Or, if your site has configured EDIS to base its selection list on the ORELSE or PSJ RNURSE security key, check to make sure your site’s emergency-department nurses hold the appropriate keys.

## Intermittent Login Difficulties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site is experiencing intermittent login difficulties and it uses a load balancer that passes control to different instances of VistA, be sure that each VistA instance is running a VistALink listener. Every system that handles VistALink connections must be running a VistALink listener.

> ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-technical-man/026.png)

> 230

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDPBDL
> Files 20
> 230.04
> Files 30
> Architecture 3
> Blank View Troubleshooting 78
> Check-in via Scheduling Troubleshooting 78
> Codes
> 233.21 ..........................................................50
> CPRS Synchronization 9
> Discharge Diagnosis
> Files 30
> Disk Space
> Requirements 5
> Display Board 3
> URLs 3
> Display Board Configuration Subfile
> 231.94 ..........................................................47
> ED Log
> Files 20
> ED Log History
> 230.1 ............................................................34
> Files 34
> EDIS Protocols
> APPOINTMENT EVENTS 75
> EDP CHECK-IN 75
> EDP MONITOR 75
> EDP NEW PATIENT 75
> EDP OR MONITOR 75
> EDPAF ADD BOARD 75
> EDPF BIG BOARD MENU 75
> EDPF BLANK 1 75
> EDPF BLANK 2 75
> EDPF BLANK 3 75
> EDPF CHANGE BOARD 76
> EDPF QUIT 76
> EDPF REMOVE BOARD 76
> EDPF SELECT DIVISION 76
> Protocols 75
> EDIS Templates
> Templates 77
> EDP
> Globals 19
> EDP CONVERSION
> Exported Options 69
> EDPB
> Globals 19
> Routines 11
> EDPBLK Routines 11
> EDPBPM Routines 11
> EDPBRM Routines 11
> EDPBRS Routines 11
> EDPBSL Routines 11
> EDPBST Routines 11
> EDPCBRD
> Remote Procedure Calls 68
> Routines 12
> EDPCDBG Routines 12
> EDPCONV Routines 12
> EDPCONV1 Routines 12
> EDPCSV Routines 12
> EDPCTRL
> Remote Procedure Calls 68
> Routines 12
> EDPDD
> Routines 12
> EDPF
> Parameters 8
> EDPF BIGBOARD KIOSKS
> Exported Options 69
> Parameters 8
> EDPF DEBUG START TIME
> Parameters 8
> EDPF LOCATION
> Parameters 8
> EDPF NURSE STAFF SCREEN
> Parameters 8
> EDPF SCHEDULING TRIGGER
> Parameters 9
> EDPF SCREEN SIZES
> Parameters 9
> EDPF TRACKING MENU ALL
> Exported Options 69
> EDPF TRACKING MENU CLINICIAN Exported Options 69
> EDPF TRACKING MENU SIGNIN
> Exported Options 69
> EDPF TRACKING MENU TRIAGE
> Exported Options 69
> EDPF TRACKING SYSTEM
> Exported Options 69
> EDPF TRACKING VIEW BOARD
> Exported Options 70
> EDPF TRACKING VIEW CONFIGURE Exported Options 70
> EDPF TRACKING VIEW DISPOSITION Exported Options 70
> EDPF TRACKING VIEW EDIT CLOSED Exported Options 70
> EDPF TRACKING VIEW REPORTS
> Exported Options 70
> EDPF TRACKING VIEW SIGNIN
> Exported Options 70
> EDPF TRACKING VIEW STAFF
> Exported Options 70
> EDPF TRACKING VIEW TRIAGE
> Exported Options 70
> EDPF TRACKING VIEW UPDATE
> Exported Options 70
> EDPFAA
> Routines 12
> EDPFLEX
> Routines 12
> EDPFMON
> Routines 12
> EDPFMOVE
> Routines 12
> EDPFPER
> Routines 12
> EDPFPTC
> Routines 12
> EDPFPTL
> Routines 12
> EDPLOG
> Routines 13
> EDPLOG1
> Routines 13
> EDPLOGA
> Routines 13
> EDPLOGH
> Routines 13
> EDPLPCE
> Routines 13
> EDPMAIL
> Routine 13
> EDPQAR
> Routines 13
> EDPQDB Routines 13
> EDPQDBS Routines 13
> EDPQLE Routines 13
> EDPQLE1 Routines 13
> EDPQLP Routines 13
> EDPQPCE Routines 13
> EDPR EXPORT
> Security Keys 73
> EDPR PROVIDER
> Security Keys 73, 74
> EDPR XREF
> Security Keys 74
> EDPRPT Routines 13
> EDPRPT1 Routines 13
> EDPRPT10 Routines 13
> EDPRPT11 Routines 14
> EDPRPT12 Routines 14
> EDPRPT2 14
> EDPRPT3 Routines 14
> EDPRPT4 Routines 14
> EDPRPT5 Routines 14
> EDPRPT6 Routines 14
> EDPRPT7 Routines 14
> EDPRPT7C Routines 14
> EDPRPT8 Routines 14
> EDPRPT9 Routines 14
> EDPRPTBV Routines 14
> EDPS BOARD CONTEXT
> Exported Options 70
> EDPSERVER
> Exported Options 71
> EDPX
> Routines 14
> EDPYCHK
> Routines 14
> EDPYPRE
> Routines 14
> EDPYPST
> Routines 15
> Exported Options 69
> Assign Views 71
> Files 19
> Codes 50
> Display Board Configuration Subfile 47
> Record Indices \#230 32
> Record Indices 230.1 38
> Record Indices 231.7 39
> Record Indices 231.8 43
> Tracking Area 43
> Tracking Code File 47
> Tracking Code Set 49, 51, 67
> Tracking Room-Bed 40
> Tracking Staff (#231.7) 38
> Globals 19
> KAAJEE Security 73
> Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE) 3
> Minimum Hardware Requirements
> System Performance 4
> Namespace and Number Space 7
> Nurse Assignments Troubleshooting 78
> Optimal Viewing Requirements
> System Performance 5
> Orders
> 230.08 ..........................................................31
> Files 31
> Parameters 8
> EDPF 8
> EDPF BIGBOARD KIOSKS 8
> EDPF DEBUG START TIME 8
> EDPF LOCATION 8
> EDPF NURSE STAFF SCREEN 8
> EDPF SCHEDULING TRIGGER 9
> EDPF SCREEN SIZES 9
> PCE Visits
> Troubleshooting 78
> presentation tier 3
> Protocols 75
> FH EVSEND OR 76
> GMRC EVSEND OR 76
> LR70 CH EVSEND OR 76
> OR EVSEND FH 76
> OR EVSEND GMRC 76
> OR EVSEND LRCH 76
> OR EVSEND ORG 76
> OR EVSEND PS 76
> OR EVSEND RA 76
> PS EVSEND OR 76
> RA EVSEND OR 76
> SDAM APPOINTMENT EVENTS 76
> Rehabilitation Act of 1973 (Section 508) 1
> Remote Procedure Calls 68
> Requirements
> Disk Space 5
> Minimum Hardware 4
> Optimal Viewing 5
> Response Times
> System 7
> Routines 11
> EDPBCF 11
> EDPBCM 11
> EDPBDL 11
> EDPBLK 11
> EDPBPM 11
> EDPBRM 11
> EDPBRS 11
> EDPBSL 11
> EDPBST 11
> EDPCBRD 12
> EDPCDBG 12
> EDPCONV 12
> EDPCONV1 12
> EDPCSV 12
> EDPCTRL 12
> EDPDD 12
> EDPFAA 12
> EDPFLEX 12
> EDPFMON 12
> EDPFMOVE 12
> EDPFPER 12
> EDPFPTC 12
> EDPFPTL 12
> EDPLOG 13
> EDPLOG1 13
> EDPLOGA 13
> EDPLOGH 13
> EDPLPCE 13
> EDPMAIL 13
> EDPQAR 13
> EDPQDB 13
> EDPQDBS 13
> EDPQLE 13
> EDPQLE1 13
> EDPQLP 13
> EDPQPCE 13
> EDPRPT 13
> EDPRPT1 13
> EDPRPT10 13
> EDPRPT11 14
> EDPRPT12 14
> EDPRPT2 14
> EDPRPT3 14
> EDPRPT5 14
> EDPRPT6 14
> EDPRPT7 14
> EDPRPT7C 14
> EDPRPT8 14
> EDPRPT9 14
> EDPRPTBV 14
> EDPX 14
> EDPYCHK 14
> EDPYPRE 14
> EDPYPST 15
> EPTRPT4 14
> Scaling Guide Memory and CPU
> System Performance 4
> Security 73
> KAAJEE 73
> PKI Encryption 73
> Secure Sockets Layer (SSL) 73
> Security keys 73
> Security Keys
> Assign Keys 74
> Security 73
> System
> Response Times 7
> Timeouts 7
> System Performance 4
> Templates 77
> EDPF BIGBOARD KISOKS 77
> Timeouts
> System 7
> Tracking Code File
> 233.1............................................................ 47
> Record Indices
> 233.1 ....................................................... 49
> Tracking Code Set
> 233.2................................................ 49, 51, 67
> Tracking Room-Bed
> 231.8............................................................ 40
> Tracking Staff File
> 231.7............................................................ 38
> Troubleshooting 78
> Blank View 78
> Check-in via Scheduling 78
> Nurse Assignments 78
> PCE Visits 78
> URLs
> Production Account 3
> Test Account 3
> Web Application 3
