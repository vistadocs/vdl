---
consolidated_title: "technical manual change pages"
app_code: MD
doc_type: TM
master_source: "MD*1*14 Technical Manual change pages"
master_pub_date: March 2008
consolidated_from: 5 versions
prior_versions:
  - "MD*1*11 Technical Manual change pages"
  - "MD*1*20 Technical Manual change pages"
  - "MD*1*21 Technical Manual change pages"
  - "MD*1*29 Technical Manual change pages"
---

#### March 2008

#### This distribution contains change pages for patch MD\*1.0\*14 of the Clinical Procedures 1.0 Technical Manual and Package Security Guide.

#### The following documentation change pages should be inserted before these replacement pages: <u>File Name:</u> <u>Patch:</u>

#### MD_1_P2_TM.PDF MD\*1.0\*2

#### Patch MD\*1.0\*14 pages:

#### <u>Replace Pages:</u> <u>With Pages:</u>

#### Title page Title page

#### Revision History Revision History

#### Table of Contents Table of Contents

#### Chapter 3 to 8 Chapter 3 to 8

#### Chapter 10 Chapter 10

#### Chapter 14 to 16 Chapter 14 to 16

> ![](md-1-14-technical-manual-change-pages/001.png)

CLINICAL PROCEDURESTECHNICAL MANUAL AND PACKAGE SECURITY GUIDE

April 2004

#### Department of Veterans Affairs Health Systems Design and Development

#### Provider Systems

> Revision History

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Description</strong></th>
<th><strong>Date</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Originally released.</td>
<td>April 2004</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark0">1</a>Patch MD*1.0*1 released.</p>
</blockquote></td>
<td>July 2004</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patch MD*1.0*2 released.</p>
</blockquote></td>
<td>August 2006</td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_bookmark1">2</a>Patch MD*1.0*5 released August 2006. Updated File List, Package Default Definition, Parameter Definitions, and menu options.</td>
<td>Documented March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><a href="#_bookmark2">3</a>Patch MD*1.0*14 released. Updated Routine Descriptions, File List, Parameter Definitions, Protocols, menu options, and Cross References. Deleted bad references to Sample Reports in Ch. 15.</td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> <span id="_bookmark0" class="anchor"></span>1 Patch MD\*1.0\*1 and MD\*1.0\*2 July 2004 Patch 2 release added.

> <span id="_bookmark1" class="anchor"></span>2 Patch MD\*1.0\*5 August 2006 Patch 5 release added.

> <span id="_bookmark2" class="anchor"></span>3 Patch MD\*1.0\*14 March 2008 Patch 14 release added.

1.  Introduction 1-1

Benefits 1-1

2.  Implementation and Maintenance 2-1
3.  [Clinical Instrument Interface Specifications 3-1](#clinical-instrument-interface-specifications)
4.  [Routine Descriptions 4-1](#routine-descriptions)
5.  [File List and Related Information 5-1](#file-list-and-related-information)

[File and Field Descriptions 5-1](#file-list-and-related-information)

[Package Default Definition 5-13](#_bookmark11)

6.  [Exported Options 6-1](#exported-options)
7.  [Cross-References 7-1](#cross-references)
8.  [Archiving and Purging 8-1](#archiving-and-purging)
9.  Callable Routines 9-1
10. [External Relations 10-1](#external-relations)
11. Internal Relations 11-1
12. Package-wide Variables 12-1
13. SAC Exemptions 13-1
14. [Software Product Security 14-1](#software-product-security)

[Security Management 14-1](#software-product-security)

[Security Features 14-1](#software-product-security)

15. [Vendor Interfaces 15-1](#15.__Vendor_Interfaces_)
16. [Glossary 16-1](#glossary)

> April 2004 Clinical Procedures V. 1.0 i

# Clinical Instrument Interface Specifications


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Clinical Instrument Interface Specifications](#clinical-instrument-interface-specifications)
- [Routine Descriptions](#routine-descriptions)
- [File List and Related Information](#file-list-and-related-information)
  - [File and Field Descriptions](#file-and-field-descriptions)
  - [Package Default Definition](#package-default-definition)
- [Exported Options](#exported-options)
  - [Delphi Components](#delphi-components)
  - [Remote Procedure Calls (RPC)](#remote-procedure-calls-rpc)
  - [Parameter Definitions](#parameter-definitions)
  - [Protocols](#protocols)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [HL Logical Links](#hl-logical-links)
  - [Menu Options by Name](#menu-options-by-name)
- [Cross-References](#cross-references)
- [Archiving and Purging](#archiving-and-purging)
- [External Relations](#external-relations)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Security Features](#security-features)
  - [List of Vendor Interfaces](#list-of-vendor-interfaces)
  - [Device Setup Instructions](#device-setup-instructions)
    - [Clinivision](#clinivision)
    - [Endoworks](#endoworks)
    - [Muse](#muse)
    - [Sensormedics V-MAX](#sensormedics-v-max)
- [Glossary](#glossary)

#### Refer to Chapter 10 of the Clinical Procedures Implementation Guide for information on Setting up HL7 Parameters.

#### [1](#_bookmark4)Refer to the Clinical Instrument Bi-Directional Interface Specifications document for information on Clinical Procedures instrument interface specifications. Directions for locating the document follow:

#### Access the Clinical Procedures website: [<u>http://vista.med.va.gov/clinicalspecialties/clinproc/</u>](http://vista.med.va.gov/clinicalspecialties/clinproc/)

1.  On the navigation bar found on the left-hand side of the page, hover your mouse pointer over Clinical Procedures Project, then click Documentation.

#### Click Clinical Procedures Documents.

2.  Click the Clinical Procedures Bi-Directional Communication Specification link to view the document or save a copy.
> <span id="_bookmark4" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Bad link removed and replaced with directions to document.
> April 2004 Clinical Procedures V. 1.0 3-1
> Clinical Instrument Interface Specifications

# Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [1](#_bookmark6)MDAPI ; HOIFO/DP/NCA - CP API Calls ; \[05-05-2003 10:28\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDAPI1 ; HOIFO/NCA - Electrocardiogram Data Extraction ;12/4/02 12:32

> ;;1.0;CLINICAL PROCEDURES;\*\*1\*\*;Apr 01, 2004

> MDARP3 ; HOIFO/NCA - Get Procedures for Medicine ;1/13/04 14:35

> ;;1.0;CLINICAL PROCEDURES;\*\*10,13\*\*;Apr 01, 2004;Build 19

> MDCVT ; HOIFO/DP/NCA - Medicine Package Conversion ;10/20/04 12:49

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDCVT1 ; HOIFO/NCA - Medicine Package Conversion (Cont.) ;1/6/05 15:12

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDCVTU ; HOIFO/NCA - Medicine Conversion Verification Utility ; \[08-28-2003 11:34\];;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDESPRT ;HOIFO/NCA - ELECTRONIC SIGNATURE PRINT ;12/21/04 09:24

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDHL7A ; HOIFO/WAA - Routine to Decode HL7 for CP ; \[05-07-2001 10:38\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7B ; HOIFO/WAA -Bi-directional interface routine ;7/23/01 11:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7BH ; HOIFO/WAA -Bi-directional interface (HL7) routine ;7/23/01 11:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7E ; HOIFO/WAA -Olympus/CMore/Pentax Endoscopy ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7K2 ; HOIFO/WAA -HP EnConcert Echo ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004 MDHL7M1 ; HOIFO/WAA - Muse EKG ; \[02-06-2002 16:13\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7MCA ; HIRMFO/REL-Routine to Decode HL7 for MEDICINE ; \[05-07-2001 10:38\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7MCX ; HIRMFO/WAA - Generate HL7 Error Message for MEDICINE ; \[05-07-2001 10:38\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7P1 ; HOIFO/WAA-Sensormedics,Jaeger Pulmonary ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7R1 ; HOIFO/WAA -Clinivision Resporatory ; 06/13/02

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7U ; HOIFO/WAA -Routine utilities for CP ;7/23/01 11:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7U1 ; HOIFO/WAA -Routine utilities for CP PROCESSING OBX ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7U2 ; HOIFO/WAA -Utilities for CP PROCESSING OBX text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7U3 ; HOIFO/WAA -Utilities for CP to process HL7 messages ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> <span id="_bookmark6" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Updated Routine Description with routines exported with patch.

> Routine Descriptions

> MDHL7X ; HOIFO/WAA -Generate HL7 Error Message ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDHL7XXX ; HOIFO/DP - Loopback device for CP ; 22-MAY-2003 13:37:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDKUTL ; HOIFO/DP - Renal Utilities ;11/29/07 14:45

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01, 2004;Build 20

> MDOUTOR ; HOIFO/NCA - Post Conversion Routine ; \[04-14-2003 10:51\]

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDPCE ; HIRMFO/NCA - Routine For Data Extract ; \[05-28-2002 12:55\]

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1 MDPFTP1 ;HOIFO/NCA - PFT REPORT-DEMO INFO ;3/15/04 11:55

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004 MDPFTP2 ; HOIFO/NCA - PFT REPORT-VOLUMES ;3/15/04 10:00

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004 MDPFTP2A ; HOIFO/NCA - PFT REPORT-FLOWS ;3/17/04 08:22

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

> MDPFTP3 ; HOIFO/NCA - PFT REPORT-SPECIAL STUDIES (PT 2) ;3/17/04 12:48

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004 MDPOST ; HOIFO/DP - Post Init ;2/18/04 11:39

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004 MDPOST04 ; HOIFO/DP - Post Init ; 2/18/04 11:39

> ;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 3

> MDPOST1 ; HOIFO/NCA/DP - Build CP DEFINITION file (#702.01) - Optional Post Init ; \[12-04-2002 13:06\];;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDPS1 ; HOIFO/NCA - CP/Medicine Report Generator ;5/18/04 09:48

> ;;1.0;CLINICAL PROCEDURES;\*\*2,10,13\*\*;Apr 01, 2004;Build 19

> MDPS2 ; HOIFO/NCA - CP/Medicine Report Generator (Cont.) ;5/18/04 09:41

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPS3 ; HOIFO/NCA - Remote Data View Data Retriever for CP ;8/26/05 14:37

;;1.0;CLINICAL PROCEDURES;\*\*2,5,13\*\*;Apr 01, 2004;Build 19

> MDPS4 ; HOIFO/NCA - Retrieve List of Consult Procedures ;1/26/06 12:45

> ;;1.0;CLINICAL PROCEDURES;\*\*13\*\*;Apr 01, 2004;Build 19

> MDPS5 ; HOIFO/NCA - Retrieve List of Consult Procedures for RDV ;3/4/05 1 3:29;;1.0;CLINICAL PROCEDURES;\*\*13\*\*;Apr 01, 2004;Build 19

> MDRPCOD ; HOIFO/DP - Object RPCs (TMDProcedureDef) ; \[01-09-2003 15:20\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004 MDRPCOG ; HOIFO/DP - CP Gateway ; \[01-09-2003 15:20\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCOL ; HOIFO/DP - Object RPCs (Logfile) ; \[02-11-2002 13:41\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCOO ; HOIFO/DP - Object RPCs (TMDOutput) ; \[03-24-2003 15:44\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCOP ; HOIFO/DP - Object RPCs (TMDPatient) ; \[01-09-2003 15:21\]

> ;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 3 MDRPCOR ; HOIFO/DP - Object RPCs (TMDRecordId) ; \[01-10-2003 09:14\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCOT ; HOIFO/DP/NCA - Object RPCs (TMDTransaction) ;12/5/02 15:33

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDRPCOT1 ; HOIFO/NCA/DP - Object RPCs (TMDTransaction) - Continued ; \[08-02-2 002 12:55\];;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

Routine Descriptions

> MDRPCOU ; HOIFO/DP - Object RPCs (TMDUser) ; \[01-09-2003 15:21\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCOV ; HOIFO/DP - Object RPCs (TMDParameter) ; \[04-15-2003 12:42\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

> MDRPCU ; HOIFO/DP - Object RPC Utilities ; \[05-23-2003 10:16\]

> ;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 3

> MDSTATU ; HOIFO/NCA - Print List of Document Titles Needed ;10/21/04 13:44

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

> MDWCHK ; HOIFO/NCA - Create CP Studies for Existing Procedures ;9/24/07 15:04;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

> MDWOR ; HOIFO/NCA - Main Routine to Decode HL7 ;5/23/07 10:49

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

> MDWORC ; HOIFO/NCA - Main Routine to Decode HL7 from Consult ;3/9/00 15:45

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

> MDWORSR ; HOIFO/NCA - Daily Schedule Studies;7/2/04 12:39 ;5/17/07 16:09

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

> MDWSETUP ; HOIFO/NCA - Auto Study Check-In Setup ;9/10/07 15:43

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01, 2004;Build 20

> Routine Descriptions

# File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File and Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### CP Transaction File - \#702

#### This file contains the studies between the instruments and user generated data as it is matched to a consult order and a TIU document is created for the results. It also manages the interface between the images and the Imaging RAID.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient</td>
<td><blockquote>
<p>702,.01</p>
</blockquote></td>
<td>Pointer to Patient (#2) file</td>
<td>This field contains a pointer to the Patient (#2) file for this study.</td>
</tr>
<tr class="even">
<td>SSN</td>
<td><blockquote>
<p>702,.011</p>
</blockquote></td>
<td>Computed</td>
<td>This field contains the computed value of the patient’s SSN from the Patient (#2) file.</td>
</tr>
<tr class="odd">
<td>DOB</td>
<td><blockquote>
<p>702,.012</p>
</blockquote></td>
<td>Computed</td>
<td>This field contains the computed value of the patient’s date of birth from the Patient (#2) file.</td>
</tr>
<tr class="even">
<td>Created Date/Time</td>
<td><blockquote>
<p>702,.02</p>
</blockquote></td>
<td>Date</td>
<td>This field contains the date/time the study was created within the CP User executable.</td>
</tr>
<tr class="odd">
<td>Created By</td>
<td><blockquote>
<p>702,.03</p>
</blockquote></td>
<td>Pointer to New Person (#200) file</td>
<td>This field contains the DUZ of the user that created this study.</td>
</tr>
<tr class="even">
<td>CP Definition</td>
<td><blockquote>
<p>702,.04</p>
</blockquote></td>
<td>Pointer to CP Definition (#702.01) file</td>
<td>This field contains a pointer to the CP Definition (#702.01) file of the procedure definition that this study represents.</td>
</tr>
<tr class="odd">
<td>Consult Number</td>
<td><blockquote>
<p>702,.05</p>
</blockquote></td>
<td>Free Text 1-20 characters in length</td>
<td>This field contains an IEN of the Consult (#123) file representing the Consult order that is matched up to this study.</td>
</tr>
<tr class="even">
<td>TIU Note</td>
<td><blockquote>
<p>702,.06</p>
</blockquote></td>
<td>Pointer to TIU Document (#8925) file</td>
<td>This field contains a pointer to the TIU Document (#8925) file representing the note that contains the interpretation of this study as well as the links to the associated images.</td>
</tr>
<tr class="odd">
<td>Vstring</td>
<td><blockquote>
<p>702,.07</p>
</blockquote></td>
<td>Free Text 1-50 characters in length</td>
<td>This field contains This field contains the vstring. The vstring is in the following format: Visit Type_”;”_Visit Date/Time_”;”_Hospital Location (internal entry number of the visit).</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Transaction Message</td>
<td><blockquote>
<p>702,.08</p>
</blockquote></td>
<td>Free Text 1-80 characters in length</td>
<td>Contains the message returned from the VistA Imaging API’s for storing the images on the server.</td>
</tr>
<tr class="even">
<td>Transaction Status</td>
<td><blockquote>
<p>702,.09</p>
</blockquote></td>
<td><blockquote>
<p>Set:</p>
</blockquote>
<ol type="1">
<li><p>- New</p></li>
<li><p>- Submitted</p></li>
<li><p>- Error</p></li>
<li><p>- Complete</p></li>
</ol></td>
<td>This field contains the status of this study.</td>
</tr>
<tr class="odd">
<td>Error Messages (multiple)</td>
<td>702.091,.01</td>
<td><p>Number between 1-</p>
<p>9999, 0 decimal digits</p></td>
<td>Error message number.</td>
</tr>
<tr class="even">
<td>Date Received</td>
<td><blockquote>
<p>702.091,.02</p>
</blockquote></td>
<td>Date</td>
<td>Date and time this error message was generated.</td>
</tr>
<tr class="odd">
<td>Received From</td>
<td><blockquote>
<p>702.091,.03</p>
</blockquote></td>
<td>Free Text 1-30 characters in length</td>
<td>Where the error was generated.</td>
</tr>
<tr class="even">
<td>Message</td>
<td><blockquote>
<p>702.091,.09</p>
</blockquote></td>
<td>Free Text 1-150 characters in length</td>
<td>Text of the error message.</td>
</tr>
<tr class="odd">
<td>Image (multiple)</td>
<td><blockquote>
<p>702.1,.01</p>
</blockquote></td>
<td><p>Number between 1-</p>
<p>999, 0 decimal digits</p></td>
<td>Index of attached image for this study.</td>
</tr>
<tr class="even">
<td>Type</td>
<td><blockquote>
<p>702.1,.02</p>
</blockquote></td>
<td><p>Set:</p>
<p>I - Instrument data</p>
<p>U - User supplied file</p></td>
<td>Type of attachment to be processed.</td>
</tr>
<tr class="odd">
<td>Result Report</td>
<td><blockquote>
<p>702.1,.03</p>
</blockquote></td>
<td>Pointer to CP Result Report (#703.1) file</td>
<td>Pointer to the CP Result Report (#703.1) file containing the attachment from the instrument.</td>
</tr>
<tr class="even">
<td>Status</td>
<td><blockquote>
<p>702.1,.09</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Submitted to server</p></li>
<li><p>- Error in submission</p></li>
<li><p>- Error in filing</p></li>
<li><blockquote>
<p>- Copied to server</p>
</blockquote></li>
</ol></td>
<td>Status of this image.</td>
</tr>
<tr class="odd">
<td>UNC</td>
<td><blockquote>
<p>702.1,.1</p>
</blockquote></td>
<td>Free Text 1-245 characters in length</td>
<td>Contains the Universal naming Convention (UNC) for this attachment.</td>
</tr>
<tr class="even">
<td>Submitted to Instrument</td>
<td>702,.11</td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Points to the instrument definition that this study was submitted to at the time of check-in.</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Instrument Order Number</td>
<td>702,.12</td>
<td>Free Text 1-22 characters in length</td>
<td>Contains the unique order number for this study that is sent to the bi- directional instrument.</td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark8">1</a>Scheduled</p>
</blockquote>
<p>Date/Time</p></td>
<td>702,.14</td>
<td>Date</td>
<td>This field contains the date/time when the HL7 message should be sent by CP to the device for this CP transaction.</td>
</tr>
<tr class="odd">
<td><a href="#_bookmark9">2</a>Conversion ID Reference</td>
<td>702,.3</td>
<td>Free text 1-30 characters in length.</td>
<td><p>This field is the Reference Conversion ID. It is a variable Pointer to the Medicine files. It</p>
<p>indicates which converted Medicine</p>
<p>report record is associated with the CP Transaction study. This field helps to keep track which CP Transaction study was created for the Medicine report conversion.</p></td>
</tr>
<tr class="even">
<td>Image Count</td>
<td><blockquote>
<p>702,.991</p>
</blockquote></td>
<td>Computed</td>
<td>Computed field to return the number of images associated with this study.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark8" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Field added to support the auto study check-in with scheduled appointment date/time.

> <span id="_bookmark9" class="anchor"></span>2 Patch MD\*1.0\*5 August 2006 Field added.

> File List and Related Information

#### CP Definition File - \#702.01

#### This file defines all the procedures used by the Clinical Procedures package. All elements that define a procedure are in this file. This file is exported with data, but entries may be added by the site.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td><blockquote>
<p>702.01,.01</p>
</blockquote></td>
<td>Free Text 3-30 characters in length</td>
<td>This field contains the name of the procedure. It should be descriptive of the procedure and contain 3-30 alphanumeric characters. The first character MUST be a letter. To maintain consistency it is recommended that all procedures be entered in UPPERCASE letters as well.</td>
</tr>
<tr class="even">
<td>Treating Specialty</td>
<td><blockquote>
<p>702.01,.02</p>
</blockquote></td>
<td>Pointer to Facility Treating Specialty (#45.7) file</td>
<td>This field defines the specialty that this procedure falls under.</td>
</tr>
<tr class="odd">
<td>Require External Data</td>
<td>702.01,.03</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Setting this field to Yes will force a consult for this procedure to be processed via the CP User executable for matching whether or not there are instruments associated with it.</td>
</tr>
<tr class="even">
<td>Default TIU Note</td>
<td><blockquote>
<p>702.01,.04</p>
</blockquote></td>
<td>Pointer to TIU Document Definition (#8925.1) file</td>
<td>This field contains a TIU Note Title to use as the default when CP creates a note for interpretation for this procedure.</td>
</tr>
<tr class="odd">
<td>Hospital Location</td>
<td><blockquote>
<p>702.01,.05</p>
</blockquote></td>
<td>Pointer to Hospital Location (#44) file</td>
<td>This is the location that will be used when creating the TIU Note for interpretation.</td>
</tr>
<tr class="even">
<td>Auto Submit</td>
<td><blockquote>
<p>702.01,.07</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>This field only applies to bi- directional instruments. It is used to indicate whether or not the image attachment should be automatically submitted to VistA Imaging once the procedure is performed and the result is passed to CP.</td>
</tr>
<tr class="odd">
<td>External Data Directory</td>
<td>702.01,.08</td>
<td>Free Text 3-150 characters in length</td>
<td>This field contains a reference to a network share where user supplied attachments are located for this procedure.</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active</td>
<td><blockquote>
<p>702.01,.09</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Yes/No to indicate active procedures that can be linked to Consults.</td>
</tr>
<tr class="even">
<td>Instrument (multiple)</td>
<td>702.011,.01</td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Contains a pointer to an instrument that generates results for this procedure.</td>
</tr>
</tbody>
</table>

> File List and Related Information

#### CP Instrument File - \#702.09

#### This file contains the list of instruments used by the Clinical Procedures package. This file is exported with data.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td><blockquote>
<p>702.09,.01</p>
</blockquote></td>
<td>Free Text 3-30 characters in length</td>
<td>Name or mnemonic of instrument. Used by vendor in HL7 message header.</td>
</tr>
<tr class="even">
<td>Notification Mailgroup</td>
<td>702.09,.02</td>
<td>Pointer to Mail Group (#3.8) file</td>
<td>Mail group that will receive error messages and other notifications dealing with this device from the interface routines.</td>
</tr>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>702.09,.03</p>
</blockquote></td>
<td>Free Text 1-50 characters in length</td>
<td>This field contains a short informational description for the instrument.</td>
</tr>
<tr class="even">
<td>Delete when Submitted</td>
<td>702.09,.05</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Select Yes if you want files created by this instrument deleted once they are successfully copied to the VistA Imaging RAID. Deletion will be performed by the VistA Imaging application.</td>
</tr>
<tr class="odd">
<td>Printable Name</td>
<td><blockquote>
<p>702.09,.06</p>
</blockquote></td>
<td>Free Text 3-30 characters in length</td>
<td>Name of instrument that is printed on the reports, etc.</td>
</tr>
<tr class="even">
<td>Default File Ext</td>
<td><blockquote>
<p>702.09,.07</p>
</blockquote></td>
<td>Free Text (e.g., .txt)</td>
<td>Default file extension for vendor instrument reports (e.g., .doc, .pdf).</td>
</tr>
<tr class="odd">
<td>Serial Number</td>
<td><blockquote>
<p>702.09,.08</p>
</blockquote></td>
<td>Free Text 1-50 characters in length</td>
<td>Vendor serial number of the instrument (for reference only).</td>
</tr>
<tr class="even">
<td>Active</td>
<td><blockquote>
<p>702.09,.09</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Whether or not the instrument is active on the network.</td>
</tr>
<tr class="odd">
<td>Processing Routine</td>
<td><blockquote>
<p>702.09,.11</p>
</blockquote></td>
<td>Free Text 1-8 characters in length</td>
<td>MUMPS routine used to process interface information.</td>
</tr>
<tr class="even">
<td>Processing Code</td>
<td><blockquote>
<p>702.09,.12</p>
</blockquote></td>
<td><p>Set:</p>
<p>M - Medicine C - CP V. 1.0</p>
<p>B - Both</p></td>
<td><p>Where data is to be processed: M - Medicine</p>
<p>C - Clinical Procedures</p>
<p>B - Both</p></td>
</tr>
<tr class="odd">
<td>Bi-directional</td>
<td><blockquote>
<p>702.09,.13</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>This field indicates whether or not this device can accept HL7 messages from VistA.</td>
</tr>
<tr class="even">
<td>IP Address</td>
<td><blockquote>
<p>702.09,.14</p>
</blockquote></td>
<td>Free Text 7-15 characters in length</td>
<td>This field contains the IP address of this instrument.</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Port</td>
<td>702.09,.15</td>
<td><p>Number between 1000-99999, 0</p>
<p>decimal digits</p></td>
<td>This field contains the port number for this instrument.</td>
</tr>
<tr class="even">
<td>HL7 Instrument ID</td>
<td><blockquote>
<p>702.09,.16</p>
</blockquote></td>
<td>Free Text 3-30 characters in length</td>
<td>This is the name of the actual device where the device name can be ‘”SMC St Louis”.</td>
</tr>
<tr class="odd">
<td>HL7 Universal Service ID</td>
<td>702.09,.17</td>
<td>Free Text 1-48 characters in length</td>
<td>This field defines what type of procedure the device can perform if the device can perform multiple types of procedures.</td>
</tr>
<tr class="even">
<td>HL7 Logical Link</td>
<td><blockquote>
<p>702.09,.18</p>
</blockquote></td>
<td>Pointer to the HL Logical Link (#870) file</td>
<td>This field contains the HL7 logical link.</td>
</tr>
<tr class="odd">
<td>Server Name</td>
<td><blockquote>
<p>702.09,.21</p>
</blockquote></td>
<td>Free Text 1-30 characters in length</td>
<td>Network name of instrument server where the report is stored.</td>
</tr>
<tr class="even">
<td>Server Share</td>
<td><blockquote>
<p>702.09,.22</p>
</blockquote></td>
<td>Free Text 1-30 characters in length</td>
<td>Share folder/drive of the instrument server where the report is stored.</td>
</tr>
<tr class="odd">
<td>Server Path</td>
<td><blockquote>
<p>702.09,.23</p>
</blockquote></td>
<td>Free Text 1-150 characters in length</td>
<td>Path on the network where the report is stored.</td>
</tr>
<tr class="even">
<td>Server Executable</td>
<td><blockquote>
<p>702.09,.24</p>
</blockquote></td>
<td>Free Text 1-30 characters in length</td>
<td>Name of server program that is run to create the report for the interface.</td>
</tr>
<tr class="odd">
<td>Process UNC</td>
<td><blockquote>
<p>702.09,.301</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces UNC type data.</td>
</tr>
<tr class="even">
<td>Process Text</td>
<td><blockquote>
<p>702.09,.302</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces text type data.</td>
</tr>
<tr class="odd">
<td>Process URL</td>
<td><blockquote>
<p>702.09,.303</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces URL type data.</td>
</tr>
<tr class="even">
<td>Process DLL</td>
<td><blockquote>
<p>702.09,.304</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces DLL type data.</td>
</tr>
<tr class="odd">
<td>Process UUEncode</td>
<td><blockquote>
<p>702.09,.305</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces UUEncode type data.</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Process XML</td>
<td><blockquote>
<p>702.09,.306</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces XML type data.</td>
</tr>
<tr class="even">
<td>Process XMS</td>
<td><blockquote>
<p>702.09,.307</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><blockquote>
<p>- Yes</p>
</blockquote></li>
</ol></td>
<td>Enter Yes if this instrument produces XMS type data.</td>
</tr>
</tbody>
</table>

> File List and Related Information

#### CP Result Report File - \#703.1

#### This file contains the information for the results uploaded from the medical instruments used by Clinical Procedures. It is distributed without any data. All fields are automatically stuffed by Clinical Procedures. There is no user input.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Upload ID</td>
<td><blockquote>
<p>703.1,.01</p>
</blockquote></td>
<td>Free Text 1-30 characters in length</td>
<td>Unique identifier assigned for each upload.</td>
</tr>
<tr class="even">
<td>Patient</td>
<td><blockquote>
<p>703.1,.02</p>
</blockquote></td>
<td>Pointer to Patient (#2) file</td>
<td>Pointer to the Patient (#2) file of the patient uploaded from the result of the instrument.</td>
</tr>
<tr class="odd">
<td>Date/Time Performed</td>
<td>703.1,.03</td>
<td>Date</td>
<td>Date/time the procedure was performed on the instrument.</td>
</tr>
<tr class="even">
<td>Instrument</td>
<td><blockquote>
<p>703.1,.04</p>
</blockquote></td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Pointer to the CP Instrument (#702.09) file of the instrument that produced these reports.</td>
</tr>
<tr class="odd">
<td>Study Reference Number</td>
<td>703.1,.05</td>
<td>Free Text 1-12 characters in length</td>
<td>This field is used as a reference to the transaction.</td>
</tr>
<tr class="even">
<td>HL7 Reference Number</td>
<td>703.1,.06</td>
<td>Free Text 1-30 characters in length</td>
<td>This field is used to keep the IEN of the HL7 message. It serves as a reference to the message that will be purged once the data has been successfully moved to the VistA Imaging server.</td>
</tr>
<tr class="odd">
<td>Status</td>
<td><blockquote>
<p>703.1,.09</p>
</blockquote></td>
<td><p>Set:</p>
<p>U - Unmatched M - Matched</p></td>
<td><p>Status of the results: U - Unmatched</p>
<p>M - Matched</p></td>
</tr>
<tr class="even">
<td>Upload Item (multiple)</td>
<td>703.11,.01</td>
<td><p>Set:</p>
<p>1 - Impression Text 2 - Report Text</p>
<p>3 - Attachment UNC 4 - Attachment URL 5 - UUEncoded Data 6 - DLL</p>
<ol start="7" type="1">
<li><p>- XML Data</p></li>
<li><p>- XML Style Sheet</p></li>
</ol></td>
<td>This field contains the type of data element that was uploaded from the instrument.</td>
</tr>
<tr class="odd">
<td>Attachment UNC</td>
<td><blockquote>
<p>703.11,.02</p>
</blockquote></td>
<td>Free Text 1-240 characters in length</td>
<td>This field contains the Universal Naming Convention (UNC) for this attachment. This indicates where the attachment is located.</td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Item Value</td>
<td><blockquote>
<p>703.11,.1</p>
</blockquote></td>
<td>Free Text 1-245 characters in length</td>
<td>If the uploaded item is a single string value, it is stored here.</td>
</tr>
<tr class="even">
<td>Item Text</td>
<td><blockquote>
<p>703.11,.2</p>
</blockquote></td>
<td>Word-Processing</td>
<td>If the uploaded data is multi-lined, it is stored here.</td>
</tr>
</tbody>
</table>

> File List and Related Information

#### [1](#_bookmark10)CP Conversion File- \#703.9

#### This file is used for storing the site parameters needed and used to convert Medicine reports to CP Text reports. This file also stores the status of the conversion process for each converted Medicine report.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><strong>Format</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td><blockquote>
<p>703.9,.01</p>
</blockquote></td>
<td>Free Text (Required)</td>
<td>This field contains the name of the CP conversion. It is only accessible by the CP conversion routine. It is exported with one "DEFAULT" entry.</td>
</tr>
<tr class="even">
<td>Mode</td>
<td><blockquote>
<p>703.9,.02</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- test</p></li>
<li><p>- real</p></li>
</ol></td>
<td><blockquote>
<p>This field indicates if the CP conversion is in test or real mode.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Administrative Closure User</td>
<td><blockquote>
<p>703.9,.03</p>
</blockquote></td>
<td>Pointer to new person file (#200)</td>
<td><blockquote>
<p>This field points to the New Person file (#200). It is used to indicate the Administrative Closure person used to close the TIU documents for the CP conversion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Scratch HFS Directory</td>
<td><blockquote>
<p>703.9,.1</p>
</blockquote></td>
<td>Free Text</td>
<td>This field stores the scratch HFS directory used for the CP conversion. CP conversion program will use this directory to convert Medicine reports.</td>
</tr>
<tr class="odd">
<td>Medicine File Parameters</td>
<td><blockquote>
<p>703.91,.01</p>
</blockquote></td>
<td>Pointer to File file (#1)</td>
<td>This field points to the File file (#1). It is used to store the Medicine file number that this parameter is pertaining to. (Reference IA #4507)</td>
</tr>
<tr class="even">
<td>CP Definition</td>
<td><blockquote>
<p>703.91,.02</p>
</blockquote></td>
<td>Point to CP Definition File (#702.01)</td>
<td><blockquote>
<p>This field contains the CP Definition to which the Medicine Report will be mapped.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Convert Y/N</td>
<td><blockquote>
<p>703.91,.03</p>
</blockquote></td>
<td><p>Set:</p>
<p>0 - No 1 - Yes</p></td>
<td><blockquote>
<p>This field is used as a flag to mark the Medicine Report. Enter 0 for 'to not convert' or 1 for 'to convert'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Convert if No Status</td>
<td><blockquote>
<p>703.91,.04</p>
</blockquote></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><blockquote>
<p>This field is used as a flag to indicate whether the Medicine report should be converted or not be converted, if there is no status for the report. The field is 0 for 'not to convert' or 1 for 'to convert'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Use TIU Note Title</td>
<td><blockquote>
<p>703.91,.05</p>
</blockquote></td>
<td>Pointer to TIU Document Definition File (#8925.1)</td>
<td><blockquote>
<p>This field stores the Historical TIU note title used for the conversion of the Medicine reports to CP reports. (Reference IA #3377 and 3568)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Conversion ID</td>
<td><blockquote>
<p>703.92,.01</p>
</blockquote></td>
<td>Free Text</td>
<td><blockquote>
<p>This field is the Conversion ID. It is a</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark10" class="anchor"></span>1 Patch MD\*1.0\*5 August 2006 CP Conversion File \#703.9 added.

> File List and Related Information

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>variable pointer to the Medicine files. This field will store an entry for each Medicine file record converted. This field is a variable pointer to the following files:</p>
</blockquote>
<ol start="691" type="1">
<li><p>ECHO</p>
<ol type="1">
<li><p>CARDIAC CATHETERIZATION</p></li>
</ol>
<ol start="5" type="1">
<li><p>ELECTROCARDIOGRAM (EKG)</p></li>
<li><p>HOLTER</p></li>
<li><p>EXERCISE TOLERANCE TEST</p></li>
<li><blockquote>
<p>ELECTROPHYSIOLOGY (EP) 694 HEMATOLOGY</p>
</blockquote></li>
</ol></li>
</ol>
<blockquote>
<p>694.5 CARDIAC SURGERY RISK ASSESSMENT</p>
</blockquote>
<ol start="698" type="1">
<li><p>GENERATOR IMPLANT</p>
<ol type="1">
<li><p>V LEAD IMPLANT</p></li>
<li><p>A LEAD IMPLANT</p></li>
<li><blockquote>
<p>PACEMAKER SURVEILLANCE 699 ENDOSCOPY/CONSULT</p>
</blockquote></li>
</ol></li>
</ol>
<blockquote>
<p>699.5 GENERALIZED PROCEDURE/CONSULT</p>
<p>700 PULMONARY FUNCTION TESTS</p>
<p>701 RHEUMATOLOGY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Status</td>
<td><blockquote>
<p>703.92,.02</p>
</blockquote></td>
<td><p>Set:</p>
<p>CR - Converted Real Mode CT - Converted Test Mode E – Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p></td>
<td><blockquote>
<p>This is the status field of the conversion log. There are five set of codes:</p>
<p>CR - Converted Real Mode CT - Converted Test Mode E - Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p>
</blockquote></td>
</tr>
<tr class="even">
<td>New TIU Document IEN</td>
<td><blockquote>
<p>703.92,.03</p>
</blockquote></td>
<td>Free Text</td>
<td>This field contains a pointer to the TIU Document file (#8925). (Reference IA #4796). This will hold the internal entry number of the document of the converted medicine report.</td>
</tr>
<tr class="odd">
<td>Lines</td>
<td><blockquote>
<p>703.92,.04</p>
</blockquote></td>
<td>Number</td>
<td>This field contains the line count of the Medicine report that was converted.</td>
</tr>
<tr class="even">
<td>Bytes</td>
<td><blockquote>
<p>703.92,.05</p>
</blockquote></td>
<td>Number</td>
<td>This field contains the number of bytes of the Medicine report that was converted.</td>
</tr>
<tr class="odd">
<td>Error Msg</td>
<td>703.92,.1</td>
<td>Free Text</td>
<td>This field stores the error message during the conversion of the Medicine report.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark11" class="anchor"></span>File List and Related Information

## Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE #</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>UP DATE</p>
<p>DD</p>
</blockquote></th>
<th><blockquote>
<p>SEND SEC.</p>
<p>CODE</p>
</blockquote></th>
<th><blockquote>
<p>DATA COMES</p>
<p>W/FILE</p>
</blockquote></th>
<th>SITE DATA</th>
<th><blockquote>
<p>RSLV PTS</p>
</blockquote></th>
<th><blockquote>
<p>USER OVER</p>
<p>RIDE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>702</p>
</blockquote></td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td>TRANSACTION</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>702.01</p>
</blockquote></td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td>DEFINITION</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>702.09</p>
</blockquote></td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td>INSTRUMENT</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>MERG</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>703.1</p>
</blockquote></td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td>RESULT REPORT</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark12">1</a> 703.9</p>
</blockquote></td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>CONVERSION</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark12" class="anchor"></span>1 Patch MD\*1.0\*5 August 2006 Default definitions added for 703.9.

> File List and Related Information

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Delphi Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Clinical Procedures uses RPC Broker and custom Delphi Components in the display and navigation of screens. Below is a list of the Delphi components this application currently uses along with a short description.

#### TMDRecordSource = class(TComponent)

#### This is the primary component that all others interact with. This component represents a record within FileMan via the Data Dictionary Number and the IEN. In the event that the record is a sub-file then this component will point to another TMDRecordSource that represents the parent record of the sub-record. There is no limit to the number of sub- records that can be linked together.

#### TMDEdit = Class(TEdit)

#### This component is designed to manage FileMan Free-Text and Numeric type fields. Other types may be used here with the exception of word-processing but they will require exact data input (i.e. non-ambiguous entries must be entered in the case of pointers or set of codes types). All input and output transforms are applied to the field on validation.

#### TMDEditPointer = Class(TComboBox)

#### This component is designed to manage FileMan Pointer types. This component currently handles screens via hard coded screens on the server side in routine MDRPCOR.

#### TMDLabel = Class(TLabel)

#### This component is a static component that can display one of three data elements for a FileMan field. These are 1) Data value 2) Field Title or 3) Field Help Text. There is no server update associated with this component.

#### TMDMemo = Class(TMemo)

#### This component manages FileMan word-processing data types only. It will validate the data upon leaving the component.

#### TMDComboBox = Class(TComboBox)

#### This component was designed for either set of codes or pointer type fields. If using a pointer type field the developer must be aware that the entire pointed to file will be retrieved so large files such as the Patient file (#2) is not possible to represent with this component. Files such as the State file (#5) are handled quite well if there are approximately 100 or less entries and the pointed to file does not have complex output transforms on the .01 field.

> Exported Options

#### TMDRadioGroup = Class(TRadioGroup)

#### This field was designed specifically for the FileMan set of codes field. It loads the appropriate codes into the radio group and displays the ‘Stands For’ portion of the codes while storing to the database the internal value of the code.

#### TMDCheckBox = Class(TCheckBox)

#### This component was designed for a set of codes that are restricted to only two codes (i.e. Yes/No, True/False, On/Off).

<span id="_bookmark14" class="anchor"></span>Exported Options

## Remote Procedure Calls (RPC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: MD GATEWAY TAG: RPC

> ROUTINE: MDRPCOG RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> NAME: MD TMDOUTPUT TAG: RPC

> ROUTINE: MDRPCOO RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> Manages the output of VistA data to the client via the default HFS device. INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 30 REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> Currently set to EXECUTE as the only option.

> INPUT PARAMETER: RTN PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: YES

> SEQUENCE NUMBER: 2 DESCRIPTION:

> Contains the routine to produce the output. Currently to client produces this parameter in the form of TAG^ROUTINE(needed parameters) to simplify the calling process.

> RETURN PARAMETER DESCRIPTION:

> Text of the requested report.

> NAME: MD TMDPARAMETER TAG: RPC

> ROUTINE: MDRPCOV RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> Used to set/retrieve/modify parameters in the Kernel ToolKit PARAMETERS (XPAR) files.

> RPC is called as follows:

> Param\[0\] := OPTION

> Param\[1\] := Entity Param\[2\] := Parameter name Param\[3\] := Instance Param\[4\] := Value

> INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 10 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> Contains the option for the RPC. RPC is called as shown:

> Exported Options

> Options and other required parameters include:

> ENTVAL ENT

> GETPAR ENT,PAR,INST GETLST ENT,PAR

> GETWP ENT,PAR,INST SETPAR ENT,PAR,INST,VAL

> SETLST ENT,PAR,,.VAL (Uses instance 0-n) SETWP ENT,PAR,INST,.VAL

> DELPAR ENT,PAR,INST DELLST ENT,PAR

> INPUT PARAMETER: ENTITY PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 20 REQUIRED: NO

> SEQUENCE NUMBER: 2 DESCRIPTION:

> An entity is a level at which you can define a parameter. The entities allowed are stored in the Parameter Entity file (#8989.518). The list of allowable entities at the time this utility was released were:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>Prefix</th>
<th><blockquote>
<p>Message</p>
</blockquote></th>
<th><blockquote>
<p>Points to File</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PKG</td>
<td><blockquote>
<p>Package</p>
</blockquote></td>
<td><blockquote>
<p>Package (9.4)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SYS</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td><blockquote>
<p>Domain (4.2)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIV</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td><blockquote>
<p>Institution (4)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRV</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td><blockquote>
<p>Service/Section (49)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LOC</td>
<td><blockquote>
<p>Location</p>
</blockquote></td>
<td><blockquote>
<p>Hospital Location (44)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TEA</td>
<td><blockquote>
<p>Team</p>
</blockquote></td>
<td><blockquote>
<p>Team (404.51)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CLS</td>
<td><blockquote>
<p>Class</p>
</blockquote></td>
<td><blockquote>
<p>Usr Class (8930)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>USR</td>
<td><blockquote>
<p>User</p>
</blockquote></td>
<td><blockquote>
<p>New Person (200)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>BED</td>
<td><blockquote>
<p>Room-Bed</p>
</blockquote></td>
<td><blockquote>
<p>Room-Bed (405.4)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OTL</td>
<td><blockquote>
<p>Team (OE/RR)</p>
</blockquote></td>
<td><blockquote>
<p>OE/RR List (101.21)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The entity may be referenced as follows:

1)  The internal variable pointer (nnn;GLO(123,)
2)  The external format of the variable pointer using the 3 character prefix (prefix.entryname)
3)  The prefix alone to set the parameter based on current entity selected. (prefix)

> Method 3 uses the following values for the following entities: USR Current value of DUZ

> DIV Current value of DUZ(2) SYS System (domain)

> PKG Package to which the parameter belongs

> INPUT PARAMETER: PAR PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: NO

> SEQUENCE NUMBER: 3 DESCRIPTION:

> A parameter is the actual name which values are stored under. The name of the parameter must be namespaced and it must be unique. Parameters can be

Exported Options

> defined to store the typical package parameter data (e.g. the default add order screen), but they can also be used to store GUI application screen settings a user has selected (e.g. font or window width). When a parameter is defined, the entities, which may set that parameter, are also defined. The definition of parameters is stored in the PARAMETER DEFINITION file (#8989.51).

> NOTE: This utility restricts the parameter name to those in the Clinical Procedures namespace (MD\*).

> INPUT PARAMETER: INST PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: NO

> SEQUENCE NUMBER: 4 DESCRIPTION:

> Most parameters will set instance to 1. Instances are used when more than one value may be assigned to a given entity/parameter combination. An example of this would be lab collection times at a division. A single division may have multiple collection times. Each collection time would be assigned a unique instance.

> INPUT PARAMETER: VAL PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 80 REQUIRED: NO

> SEQUENCE NUMBER: 5 DESCRIPTION:

> A value may be assigned to every parameter for the entities allowed in the parameter definition. Values are stored in the PARAMETERS file (#8989.5). VAL may be passed in external or internal format. If using internal format for a pointer type parameter, VAL must be preceded with the grave (\`) character. If VAL is being assigned to a word processing parameter, the text is passed in the subordinate nodes of VAL (e.g. VAL(0-n)=Text).

> RETURN PARAMETER DESCRIPTION:

> Returns requested data from the specified option.

> NAME: MD TMDPATIENT TAG: RPC

> ROUTINE: MDRPCOP RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> NAME: MD TMDPROCEDURE TAG: RPC

> ROUTINE: MDRPCOD RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> NAME: MD TMDRECORDID TAG: RPC

> ROUTINE: MDRPCOR RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> General RPC for VA Fileman functions.

> Param 1 is passed in as the function to perform and includes the following:

> Exported Options

> LOOKUP: Performs very generic file lookup functionality VALIDATE: Validates input to a fileman field and saves to FDA DELREC: Validates ability to delete and if able deletes a record SETFDA: Validates input and stores in FDA

> SAVEFDA: Saves any data stored in FDA

> CLEARFDA: Clears any data in the FDA without saving GETDATA: Retrieves a single field value

> GETCODES: Retrieves the set of codes for a field GETLABEL: Retrieves a fields TITLE or LABEL if no Title GETIDS: Returns required identifiers for a DD Number GETHELP: Returns Fileman help for a field

> RENAME: Validates and renames .01 field if valid NEWREC: Creates a new record

> CHANGES: Returns 0/1 if changes exist in FDA CHKVER: Version check Client \<-\> Server LOCK: Locks a record by DD and IENS UNLOCK: Unlocks record locked by LOCK option

> INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> See description of RPC.

> INPUT PARAMETER: DDNUM PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 10 REQUIRED: NO

> SEQUENCE NUMBER: 2 DESCRIPTION:

> Contains the Data Dictionary number of the item being manipulated. INPUT PARAMETER: IENS PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 20 REQUIRED: NO SEQUENCE NUMBER: 3

> DESCRIPTION:

> Contains the IENS of the record being manipulated.

> INPUT PARAMETER: FLD PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 10 REQUIRED: NO

> SEQUENCE NUMBER: 4 DESCRIPTION:

> Contains field specifications for the record.

> INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: NO

> SEQUENCE NUMBER: 5 DESCRIPTION:

> Contains any other needed information for the call. RETURN PARAMETER DESCRIPTION:

> Returns global array of requested data or status.

> NAME: MD TMDTRANSACTION TAG: RPC

> ROUTINE: MDRPCOT RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

Exported Options

> NAME: MD TMDUSER TAG: RPC

> ROUTINE: MDRPCOU RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> Manages the VistA interface to the TMDUser object.

> Available options:

> SIGNON Connects session to the server and attempts signon. ESIG Verifies passed e-sig.

> CHKVER Verifies client version is compatible with server. INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 30 REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> See RPC description.

> INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 250 REQUIRED: NO

> SEQUENCE NUMBER: 2 DESCRIPTION:

> Required data for selected option. RETURN PARAMETER DESCRIPTION:

> Returns global array of status or requested data.

> NAME: MD UTILITIES TAG: RPC

> ROUTINE: MDRPCU RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> <span id="_bookmark15" class="anchor"></span>Exported Options

## Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NAME: MD ALLOW EXTERNAL ATTACHMENTS

> DISPLAY TEXT: Allow non-instrument attachments

> MULTIPLE VALUED: No VALUE TERM: Allowed VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to Yes to allow users of CPUser.exe to attach documents to the transaction that are not created by an instrument.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> [1](#_bookmark16)NAME: MD CHECK-IN PROCEDURE LIST DISPLAY TEXT: Check-in Procedure List MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Schedule Appointment? VALUE DATA TYPE: set of codes VALUE DOMAIN: 0:None;1:Outpatient;2:Inpatient;3:Both

> VALUE HELP: Enter 0 for None, 1 for Outpatient, 2 for Inpatient, or 3 for both.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter procedures that needs the study to be auto checked-in. INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0

> DESCRIPTION:

> This parameter contains a list of procedures that will be used

> to auto check-in the CP studies during the procedures request in CPRS and whether appointments are scheduled for the procedure.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CLINIC QUICK LIST DISPLAY TEXT: Clinic Quick List For CP MULTIPLE VALUED: Yes INSTANCE TERM: Clinic

> VALUE TERM: Procedure VALUE DATA TYPE: pointer VALUE DOMAIN: 702.01

> VALUE HELP: Select a procedure for the clinic.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 44

> INSTANCE HELP: Enter clinics that need CP studies to be checked-in. DESCRIPTION:

> List of clinics used as a source to get a list of patients that need to have CP studies checked-in. This only applies to studies with procedures that have multiple results such as Hemodialysis, Respiratory Therapy, and sleep studies.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

#### NAME: MD CLINICS WITH MULT PROC

> <span id="_bookmark16" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Parameter Definitions added.

Exported Options

> DISPLAY TEXT: Clinics With Multiple Procedures

> MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Clinic VALUE DATA TYPE: pointer VALUE DOMAIN: 44

> VALUE HELP: Enter a clinic for the procedure.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter a procedure.

> INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0 DESCRIPTION:

> If you have a clinic for multiple procedures, populate this parameter with the procedure and associate it to a clinic.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CRC BYPASS DISPLAY TEXT: Bypass CRC Checking MULTIPLE VALUED: No VALUE TERM: Bypass CRC Checking VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to 'Yes' to prevent the client application from verifying its CRC Value at startup.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CRC VALUES

> DISPLAY TEXT: Clinical Procedures CRC Values MULTIPLE VALUED: Yes

> INSTANCE TERM: Executable or Library Name

> VALUE TERM: CRC Value PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:15 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

> DESCRIPTION:

> This parameter is used to store the CRC values for the most recent versions of executable and libraries. Use the Tools menu on the CPManager program to calculate the needed CRC Values of the current versions.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

#### NAME: MD DAYS FOR INSTRUMENT DATA

> DISPLAY TEXT: Temporary instrument data life (Days) MULTIPLE VALUED: No VALUE TERM: Days

> PROHIBIT EDITING: No VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

> DESCRIPTION:

> The number of days to keep data from the auto-instruments after the data has been associated with a Clinical Procedures report.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD FILE EXTENSIONS DISPLAY TEXT: Imaging File Types MULTIPLE VALUED: Yes INSTANCE TERM: Extension

> Exported Options

> VALUE TERM: File type PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:80

> VALUE HELP: Enter a description of this file type

> INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 2:10

> INSTANCE HELP: Enter the extension of the file type with a '.' INSTANCE VALIDATION CODE: K:X'?1".".9ULN X

> DESCRIPTION:

> This parameter stores a list of valid file types and the associated extensions of these files.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD GATEWAY DISPLAY TEXT: CP Gateway Parameters MULTIPLE VALUED: Yes INSTANCE TERM: Parameter Name

> VALUE TERM: Parameter Value VALUE DATA TYPE: free text VALUE DOMAIN: 1:255 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:255

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD HFS SCRATCH

> DISPLAY TEXT: VistA Scratch HFS Directory

> MULTIPLE VALUED: No VALUE TERM: Directory name

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

> VALUE HELP: Enter in an OS level directory DESCRIPTION:

> Contains the directory specification for the Kernel OPEN^%ZISH call. This directory should be accessible for read/write operations by all CP users.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD IMAGING XFER DISPLAY TEXT: Imaging Network Share MULTIPLE VALUED: No VALUE TERM: Imaging Network Share

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 DESCRIPTION:

> This parameter contains the name of a network server, share, and path (UNC) to a location where Clinical Procedures can put files for pick-up by the Imaging background processor for archiving.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> [1](#_bookmark17)NAME: MD MEDICINE CONVERTED DISPLAY TEXT: Medicine Package

> Converted

> MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> Used to determine if the Medicine Package has been converted.

> <span id="_bookmark17" class="anchor"></span>1 Patch MD\*1.0\*5 August 2006 Parameter Definition added.

Exported Options

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD OFFLINE MESSAGE DISPLAY TEXT: Offline message

> MULTIPLE VALUED: No VALUE TERM: Offline Message VALUE DATA TYPE: word processing

> DESCRIPTION:

> This parameter contains a message to display to the users when the Clinical Procedures application is offline.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD ONLINE

> DISPLAY TEXT: Clinical Procedure Online/Offline MULTIPLE VALUED: No

> VALUE TERM: Is Clinical Procedures Online

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

> VALUE HELP: Enter 'Yes' to allow access to CP DESCRIPTION:

> This parameter controls access to the Clinical Procedures package. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> [1](#_bookmark18)NAME: MD USE APPT WITH PROCEDURE

> DISPLAY TEXT: Use Appointment With Procedure MULTIPLE VALUED: No

> VALUE TERM: Use appointment with procedure

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> Enter "Y" or "N" for Yes/No on whether your site selects the appointment scheduled for outpatients during the procedure request in CPRS.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD USER DEFAULTS DISPLAY TEXT: CP User Defaults

> MULTIPLE VALUED: Yes INSTANCE TERM: Parameter setting VALUE TERM: Parameter value PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> DESCRIPTION:

> This parameter is used to store a users default parameter settings. Each setting is defined on the client.

> PRECEDENCE: 1 ENTITY FILE: USER

> NAME: MD VERSION CHK DISPLAY TEXT: Version Compatibility MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version VALUE TERM: Compatible with current server version

> <span id="_bookmark18" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Parameter Definition added.

> Exported Options

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

> DESCRIPTION:

> This parameter is used to store the application:versions that are compatible with the current server version of Clinical Procedures. Instance format

> of APPLICATION:VERSION (example: CPMANAGER.EXE:0.0.0.0). PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD WEBLINK

> DISPLAY TEXT: Clinical Procedures Home Page

> MULTIPLE VALUED: No VALUE TERM: Web Address

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 DESCRIPTION:

> This parameter contains the web address for the Clinical Procedures home page. This can be modified to a local address in the event that the pages are downloaded to be displayed from a local server location.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

<span id="_bookmark19" class="anchor"></span>Exported Options

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: MCAR Device Client ITEM TEXT: Instrument Device Client TYPE: subscriber CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: MEDICINE

> DESCRIPTION: Subscriber protocol for sending data to Vista from clinical instruments.

> TIMESTAMP: 59276,54156 RECEIVING APPLICATION: MCAR-INST TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P LOGICAL LINK: MCAR INST

> VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> NAME: MCAR Device Server ITEM TEXT: Instrument HL7 Event Driver TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: MEDICINE

> DESCRIPTION: This protocol is used by the HL7 package to send results to Vista from various clinical instrumentation.

> TIMESTAMP: 59276,54156 SENDING APPLICATION: INST-MCAR TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P VERSION ID: 2.3

> SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> SUBSCRIBERS: MCAR Device Client

> NAME: MCAR ORM CLIENT TYPE: subscriber

> CREATOR: <span class="mark">REDACTED</span> RECEIVING APPLICATION: INST-MCAR EVENT TYPE: O02 RESPONSE MESSAGE TYPE: ORR SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO ROUTING LOGIC: Q

> NAME: MCAR ORM SERVER

> ITEM TEXT: Clinical Procedures ORM Protocol Server

> TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP: 59276,54156 SENDING APPLICATION: MCAR-INST TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

> VERSION ID: 2.3 SUBSCRIBERS: MCAR ORM CLIENT

> <span id="_bookmark20" class="anchor"></span>Exported Options

> [1](#_bookmark21)NAME: MD RECEIVE GMRC

> ITEM TEXT: Clinical Procedures receives messages from Consult TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This protocol receives messages from Consult. (IA 3140) ENTRY ACTION: D EN^MDWORC(.XQORMSG) TIMESTAMP: 60934,38793

> NAME: MD RECEIVE OR

> ITEM TEXT: Clinical Procedures receives order msgs from CPRS TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This protocol receives order messages from CPRS. (IA 3135) ENTRY ACTION: D EN^MDWOR(.XQORMSG) TIMESTAMP: 60934,38793

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MCAR-INST ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER

> COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> <span id="_bookmark21" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Protocols added to support the auto study check-in.

<span id="_bookmark22" class="anchor"></span>Exported Options

## HL Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NODE: MCAR INST LLP TYPE: TCP

> DEVICE TYPE: Single-threaded Server STATE: Reading

> AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:46:17

> TASK NUMBER: 526320 SHUTDOWN LLP ?: NO QUEUE SIZE: 100

> RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

> ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

> TCP/IP PORT: 9026 TCP/IP SERVICE TYPE: SINGLE LISTENER

> PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

> IN QUEUE BACK POINTER: 331 IN QUEUE FRONT POINTER: 331 OUT QUEUE BACK POINTER: 220 OUT QUEUE FRONT POINTER: 210

> NODE: MCAR OUT LLP TYPE: TCP

> DEVICE TYPE: Non-Persistent Client STATE: Openfail

> AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:45:47

> TASK NUMBER: 529066 SHUTDOWN LLP ?: NO

> QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

> READ TIMEOUT: 60 ACK TIMEOUT: 60

> EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: 10.3.17.157

> TCP/IP PORT: 9028 TCP/IP SERVICE TYPE: CLIENT (SENDER)

> PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

> IN QUEUE BACK POINTER: 202 IN QUEUE FRONT POINTER: 202 OUT QUEUE BACK POINTER: 206 OUT QUEUE FRONT POINTER: 202

## Menu Options by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: MD GUI USER MENU TEXT: MD GUI USER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 59331,44145

> RPC: MD TMDOUTPUT RPC: MD TMDPARAMETER RPC: MD TMDPATIENT RPC: MD TMDPROCEDURE RPC: MD TMDRECORDID

> RPC: MD TMDTRANSACTION RPC: MD TMDUSER

> RPC: MD UTILITIES

> UPPERCASE MENU TEXT: MD GUI USER

> NAME: MD GUI MANAGER MENU TEXT: MD GUI MANAGER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 59385,45622

> Exported Options

> RPC: MD TMDOUTPUT RPC: MD TMDPARAMETER RPC: MD TMDPATIENT RPC: MD TMDPROCEDURE RPC: MD TMDRECORDID

> RPC: MD TMDTRANSACTION RPC: MD TMDUSER

> RPC: MD UTILITIES RPC: MD GATEWAY

> UPPERCASE MENU TEXT: MD GUI MANAGER

> [1](#_bookmark23)NAME: MD AUTO CHECK-IN SETUP MENU TEXT: Auto Study Check-In Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is used to populate the XPAR parameters MD USE APPT WITH PROCEDURE, MD CHECK-IN PROCEDURE LIST, MD CLINIC QUICK LIST, and MD

> CLINICS WITH MULT PROC. The four XPAR parameters are used for the auto study check-in. Users can use the option to indicate whether their site use and schedule appointments. They can populate a list of procedures and associated clinics that need a CP study checked-in.

> ROUTINE: EN1^MDWSETUP

> UPPERCASE MENU TEXT: AUTO STUDY CHECK-IN SETUP

> NAME: MD SCHEDULED STUDIES MENU TEXT: Scheduled Studies TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is tasked to run daily. It will process the HL7 messages that need to be sent to the device on a daily basis for CP studies.

> ROUTINE: EN1^MDWORSR SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: SCHEDULED STUDIES

> NAME: MD STUDY CHECK-IN MENU TEXT: Study Check-in TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is tasked to run daily. It checks-in CP studies for procedures that require multiple encounters such as Hemodialysis, Respiratory Therapy, and Sleep Studies.

> ROUTINE: CLINICPT^MDWORSR SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: STUDY CHECK-IN

> [2](#_bookmark24)NAME: MDCVT MANAGER

> MENU TEXT: Medicine to CP Conversion Manager

> TYPE: menu CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This is the Medicine to CP Manager menu option. This menu

> <span id="_bookmark23" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Options added to support the auto study check-in.

> <span id="_bookmark24" class="anchor"></span>2 Patch MD\*1.0\*5 August 2006 Patch 5 menu options added.

Exported Options

> option consists of options to assist the site in converting the Medicine reports to Clinical Procedures text reports.

> ITEM: MDCVT SETUP SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: MDCVT RUN SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: MDCVT SUMMARY SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: MDCVT DISK SPACE SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: MDCVT LIST OF TIU TITLES SYNONYM: 6 DISPLAY ORDER: 6

> ITEM: MDCVT TOTALS SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: MDCVT ERROR LOG SYNONYM: 8 DISPLAY ORDER: 8

> ITEM: MDCVT CONVERSION LOCKOUT SYNONYM: 9 DISPLAY ORDER: 9

> ITEM: MDCVT BUILD CONVERSION LIST SYNONYM: 2 DISPLAY ORDER: 2

> TIMESTAMP: 60459,53192 TIMESTAMP OF PRIMARY MENU: 59904,24363 UPPERCASE MENU TEXT: MEDICINE TO CP CONVERSION MANA

> NAME: MDCVT SETUP MENU TEXT: Conversion Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES X ACTION PRESENT: YES

> DESCRIPTION: This option will bring up a setup screen for the site to setup the Medicine Report Conversion parameter setup. This parameter setup allows the site to control which Medicine reports will be converted and which CP Definition and TIU title to link to.

> EXIT ACTION: K DDSFILE,DR,DA ROUTINE: SETUP^MDCVT UPPERCASE MENU TEXT: CONVERSION SETUP

> NAME: MDCVT RUN MENU TEXT: Run the Conversion Process TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will start the Medicine Report conversion to Clinical Procedures. This option will only convert reports for procedures that have the "CONVERT Y/N" field set to "Yes" under the MEDICINE FILE PARAMETERS in the CP CONVERSION file (#703.9).

> ROUTINE: EN^MDCVT

> UPPERCASE MENU TEXT: RUN THE CONVERSION PROCESS

> NAME: MDCVT SUMMARY MENU TEXT: Summary of Conversion Process

> TYPE: print CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> Exported Options

> DESCRIPTION: This option will generate a Medicine Report Conversion report. This report consists of a listing of all Medicine records that were processed in the conversion in variable pointer format and the status of the conversion whether the record was converted, skipped, or errored. If the record was converted, the total number of lines and bytes that the record was converted to in a TIU document will be displayed. If the record errored, the reason

> why

> it errored will be displayed. If the record was skipped, the reason why it was skipped will be displayed.

> DIC {DIP}: MDD(703.9, L.: 0

> FLDS: \[MD CONVERSION SUMMARY\] BY: \[MD CONVERSION SUMMARY\] UPPERCASE MENU TEXT: SUMMARY OF CONVERSION PROCESS

> NAME: MDCVT DISK SPACE MENU TEXT: Disk Space Requirements TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will generate a summary of the Medicine report conversion. This summary consists of a list of the files converted to Clinical Procedures, the count of records converted, the total lines and

> Bytes

> the records were converted in each file. ROUTINE: SUMMARY^MDCVT

> UPPERCASE MENU TEXT: DISK SPACE REQUIREMENTS

> NAME: MDCVT LIST OF TIU TITLES MENU TEXT: List of TIU Titles Needed TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will allow the user to generate a list of Medicine procedures and the TIU titles needed to be created for the procedures that will be used for the Medicine report conversion. The PRINT NAME of the procedures in the PROCEDURE/SUBSPECIALTY file (#697.2) will be used in the display. This list will list the procedures and titles for a Medicine

> Package

> Procedure, if the "Convert Y/N" parameter is set to "Yes" and the "Use TIU Note Title" parameter is blank in the Conversion Setup option.

> ROUTINE: DISP^MDSTATU

> UPPERCASE MENU TEXT: LIST OF TIU TITLES NEEDED

> NAME: MDCVT TOTALS MENU TEXT: Conversion Totals By Status TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will verify that the Medicine reports conversion is

> complete and are in appropriate statuses. ROUTINE: TOTALS^MDCVT

> UPPERCASE MENU TEXT: CONVERSION TOTALS BY STATUS

Exported Options

> NAME: MDCVT ERROR LOG MENU TEXT: Error Log

> TYPE: print CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option generates a log of all the errors that occurred with each Medicine report during the conversion. The listing consists of the CONVERSION ID and ERROR MESSAGE. The CONVERSION ID consists of the record \# concatenated with a ";" and the global location (e.g.,"345;MCAR(699,").

> DIC {DIP}: MDD(703.9, L.: 0

> FLDS: \[MD CONVERSION ERRORS\] BY: \[MD CONVERSION ERRORS\] UPPERCASE MENU TEXT: ERROR LOG

> NAME: MDCVT CONVERSION LOCKOUT MENU TEXT: Conversion Lockout TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will let the user place a specialty/procedure or ALL specialty/procedures Enter/Edit and Report options 'OUT OF SERVICE' in

> the

> Medicine package. It will also set Kernel site parameter MD MEDICINE CONVERTED to "YES" when all specialties/procedures enter/edit and report options are disabled or when the user indicated that all Medicine reports has been converted.

> ROUTINE: LOCKOUT^MDCVT UPPERCASE MENU TEXT: CONVERSION LOCKOUT

> NAME: MDCVT BUILD CONVERSION LIST MENU TEXT: Build Conversion List TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

> X ACTION PRESENT: YES

> DESCRIPTION: The user will need to run this option before using the \[MDCVT RUN\], Run the Conversion Process, option. This option will let the user

> build

> the conversion list of the Medicine file records for the CP CONVERSION file (#703.9). It will populate the CONVERSION LOG sub-file (#703.92) with all entries in the "AC" cross reference in the MEDICAL PATIENT file (#690) and

> set

> the STATUS field as "Ready to Convert" for each entry. This option can be queued. Once the conversion list is built, this option can also be used to add new additional entries in the Medicine file into the conversion list.

> This option will not overwrite the existing entries in the CONVERSION LOG but add to the list.

> EXIT ACTION: K MDS ENTRY ACTION: S MDS=\$\$BLD^MDCVT1() UPPERCASE MENU TEXT: BUILD CONVERSION LIST

> Exported Options

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Included in this section is the information about the cross-references of the application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FILE NUMBER</strong></th>
<th><strong>FIELD NUMBER</strong></th>
<th><strong>CROSS REFERENCE</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>702</strong></td>
<td>.05</td>
<td>ACON</td>
<td>Used for searches when the user knows the Consult order number.</td>
</tr>
<tr class="even">
<td></td>
<td>.3</td>
<td>ACONV</td>
<td><p>This cross reference is used to keep track of which CP transaction study was created during the Medicine</p>
<p>report conversion and which</p>
<p>Medicine record it is associated with.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.06</td>
<td><blockquote>
<p>ATIU</p>
</blockquote></td>
<td>Used for searches when the user knows the TIU Note title.</td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, the patient name.</td>
</tr>
<tr class="odd">
<td></td>
<td>.04</td>
<td>ACP</td>
<td>Used for searches when the user knows the CP definition.</td>
</tr>
<tr class="even">
<td></td>
<td>.11</td>
<td>AINST</td>
<td>Used for searches when the user knows if the study was submitted to Imaging.</td>
</tr>
<tr class="odd">
<td></td>
<td>.12</td>
<td><blockquote>
<p>AION</p>
</blockquote></td>
<td><blockquote>
<p>Used to quickly retrieve</p>
</blockquote>
<p>the study ien from the instrument order number.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.14</td>
<td><blockquote>
<p>ASD</p>
</blockquote></td>
<td>This cross reference contains the scheduled sending HL7 message. This cross reference contains the scheduled date/time as to when the HL7 message should be sent to the device for the CP transaction. It is used for easy look up to</td>
</tr>
</tbody>
</table>

> Cross-References

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th>process the study.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Subfile 702.091</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, error messages.</td>
</tr>
<tr class="even">
<td>Subfile 702.1</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, image.</td>
</tr>
<tr class="odd">
<td><strong>702.01</strong></td>
<td>.02</td>
<td>ASPEC</td>
<td>Used for searches when the user knows the Treating Specialty.</td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, name of the procedure.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td><blockquote>
<p>UC</p>
</blockquote></td>
<td>Used to validate a new entry as unique without case sensitivity.</td>
</tr>
<tr class="even">
<td>Subfile 702.011</td>
<td>.01</td>
<td>AINST</td>
<td>Used for searches when the user knows the name of the instrument.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, instrument.</td>
</tr>
</tbody>
</table>

Cross-References

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FILE NUMBER</strong></th>
<th><strong>FIELD NUMBER</strong></th>
<th><strong>CROSS REFERENCE</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>702.09</strong></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, name of the instrument.</td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td><blockquote>
<p>UC</p>
</blockquote></td>
<td>Used to validate a new entry as unique without case sensitivity.</td>
</tr>
<tr class="odd">
<td><strong>703.1</strong></td>
<td>.02</td>
<td>ADFN</td>
<td>Used for searches when the user knows the patient name.</td>
</tr>
<tr class="even">
<td></td>
<td>.03</td>
<td>ADTP</td>
<td>Used for searches when the user knows the date/time performed.</td>
</tr>
<tr class="odd">
<td></td>
<td>.04</td>
<td>AINST</td>
<td>Used for searches when the user knows the name of the instrument.</td>
</tr>
<tr class="even">
<td></td>
<td>.09</td>
<td>ASTATUS</td>
<td>Sets the status for the Gateway to find studies to process.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, the upload ID.</td>
</tr>
<tr class="even">
<td>Subfile 703.11</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, upload item.</td>
</tr>
<tr class="odd">
<td><strong>703.9</strong></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, Name.</td>
</tr>
<tr class="even">
<td>Subfile 703.91</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, Medicine File Parameters.</td>
</tr>
<tr class="odd">
<td>Subfile 703.92</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, Conversion ID.</td>
</tr>
<tr class="even">
<td></td>
<td>.02</td>
<td>AS</td>
<td>Used for lookup by conversion status.</td>
</tr>
</tbody>
</table>

> Cross-References

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### There is no archiving capability at this time. Purging is available in the CPGateway through the Set Maximum Log Entries option. See description below.

#### Set Maximum Log Entries allows the user to adjust the number of entries that are displayed in the log file. Once this value is reached, entries will be purged from the beginning of the log to keep the log file from growing too large. This value will take effect after the next polling operation so if the current poll value is 300 seconds it may take up to 5 minutes for the new value to be used. Allowable values are 100 to 10000 entries. When the CP Gateway is shut down, all entries are purged from the log file.

#### Note: Purging is also done daily while the CP Gateway is running. This purge deletes the raw data that comes across from the instrument. The CP Gateway keeps data for a specified number of days based on the entry in the system parameter “Days to keep Instrument Data”. Data older than this will be purged. The data to be deleted is already matched with a study. The fields purged are the Item Value field (#.1) and Item Text field (#.2) of the Upload Item multiple in the CP Results file (#703.1).

![](md-1-14-technical-manual-change-pages/002.png)

#### Figure 8-1

> Archiving and Purging

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The following describes the installation environment for Version 1.0 of the Clinical Procedures package on the VistA server:

#### VA FileMan V. 22 or greater

#### Kernel V. 8.0 or greater

#### Kernel Toolkit V. 7.3 or greater

#### Kernel RPC Broker V. 1.1 or greater

#### PIMS (Patient Information Management System) V. 5.3 or greater (including):

#### Registration V. 5.3

#### Scheduling V. 5.3

#### Health Summary V. 2.7 or greater

#### HL7 (Health Level 7) V. 1.6 or greater

#### Consults/Request Tracking V. 3.0

#### TIU (Text Integration Utility) V. 1.0

#### Order Entry V. 3.0 (CPRS (Computerized Patient Record System) V. 1.0 (GUI

#### V. 18.8)) or greater

#### PCE (Patient Care Encounter) V. 1.0 or greater

#### VistA Imaging V. 3.0 or greater (includes installation of background processor and jukebox)

#### Medicine V. 2.3 (optional)

#### These packages must be patched up through and including the following patches before Clinical Procedures is installed:

#### Patch 17 of Consults/Request Tracking V. 3.0 (GMRC\*3.0\*17)

#### Patch 112 of Order Entry V. 3.0 (OR\*3.0\*112)

#### Patch 109 of Text Integration Utility V. 1.0 (TIU\*1.0\*109)

#### Patch 7 of Imaging V. 3.0 (MAG\*3.0\*7) 5. Patch 93 of HL7 V. 1.6 (HL\*1.6\*93)

#### Patch 98 of HL7 V. 1.6 (HL\*1.6\*98)

#### If Medicine V. 2.3 is installed, you must install Patch 24 of Medicine (MC\*2.3\*24), and Patch 146 of Kernel (XU\*8.0\*146).

#### [1](#_bookmark28)Interface Control Registrations (formerly known as Integration Agreements) between the Clinical Procedures software and other VistA applications exist. Database Interface Control Registrations (DICR) are available on the DBA menu on Forum. For complete information regarding the DICRs for Clinical Procedures V. 1.0, please refer to the *Integration Control*

> <span id="_bookmark28" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 External Relations list removed. Integration Agreements renamed Interface Control Registrations.

> External Relations

> *Registrations (Agreements) Menu* \[DBA IA ISC\] option under the *DBA* \[DBA\] option on FORUM.

#### [1](#_bookmark29)The following screen capture shows one way to access the DBA option in FORUM:

> <span id="_bookmark29" class="anchor"></span>1 Patch MD\*1.0\*14 March 2008 Screen capture added.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### No additional security measures are to be applied other than those implemented through Menu Manager and the package routines. Clinical Procedures uses the standard RPC broker log-in procedure to validate the user and allow access to the system.

#### No additional licenses are necessary to run the software.

#### Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Mail groups and alerts.

#### There is one mailgroup associated with this software. This mailgroup is called MD DEVICE ERRORS. The purpose of this mailgroup is to store a list of people who will be notified if a problem arises with an automated instrument. There is one alert in the software that occurs on the VistA server if the package installation does not finish. This alert is sent to the IRMS staff member who ran the installation.

#### Remote systems.

#### The application does not transmit data to any remote system/facility database.

#### Archiving/Purging.

#### Refer to the chapter on [<u>Archiving and Purging</u>](#archiving-and-purging), in this manual. Purging is available in the CPGateway, refer to the Clinical Procedures Gateway chapter in the Clinical Procedures Implementation Guide for more information.

#### Contingency Planning.

#### It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems. It is recommended that the CP Gateway be installed on a second machine as a backup in case the initial workstation containing the CP Gateway fails.

#### Interfacing.

> Software Product Security

#### No specialized (non VA) interfaces are used or required by the application.

#### Electronic signatures.

#### Electronic signatures are not used in the Clinical Procedures package.

#### Menus.

#### There are no options of special note for the Information Security Officers (ISO’s) to view.

#### Security Keys.

#### The MD MANAGER key controls access to the 'Update Study Status' and the 'Delete Study' options. A user holding this key will be able to use the 'Update Study Status' option on any study currently displayed on the screen. Holders of this key will also be taken directly to the 'Update Study Status' option when opening a study marked in status 'Error'. The 'Update Study Status' option does not do any validation on the new status assigned to the study. The 'Delete Study' option will attempt to delete the study after checking the business rules on the VistA server for the study given its current status and state on the server. This key should be given only with extreme care and only to those users that fully understand the status structure, and the ramifications of changing the status or deletion of a study.

#### File Security.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 28%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p>DD</p>
</blockquote></th>
<th>RD</th>
<th>WR</th>
<th>DEL</th>
<th>LAY</th>
<th>AUD</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NUMBER NAME</td>
<td><blockquote>
<p>GLOBAL NAME</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
<td>ACC</td>
<td>ACC</td>
<td>ACC</td>
<td>ACC</td>
<td>ACC</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th>702</th>
<th>CP</th>
<th>TRANSACTION</th>
<th><blockquote>
<p>^MDD(702,</p>
</blockquote></th>
<th><blockquote>
<p>@</p>
</blockquote></th>
<th></th>
<th>@</th>
<th></th>
<th>@</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>702.01</td>
<td>CP</td>
<td>DEFINITION</td>
<td><blockquote>
<p>^MDS(702.01,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>#</td>
<td>#</td>
<td>#</td>
<td></td>
</tr>
<tr class="even">
<td>702.09</td>
<td>CP</td>
<td>INSTRUMENT</td>
<td><blockquote>
<p>^MDS(702.09,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>#</td>
<td>#</td>
<td>#</td>
<td>@</td>
</tr>
<tr class="odd">
<td>703.1</td>
<td>CP</td>
<td>RESULT REPORT</td>
<td><blockquote>
<p>^MDD(703.1,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

> [1](#_bookmark31) 703.9 CP CONVERSION ^MDD(703.9, @ \# \# \# \# \#

#### References.

#### There are no special reference materials for this package.

#### Official Policies.

#### There are no special official policies for this package.

> <span id="_bookmark31" class="anchor"></span>1 Patch MD\*1.0\*5 August 2006 Files added.

> <span id="15.__Vendor_Interfaces_" class="anchor"></span>15. [19](#_bookmark33)Vendor Interfaces

## List of Vendor Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### [20](#_bookmark34)The Puritan Bennett Clinivision, Olympus Endoworks, GE Healthcare Muse and Cardinal Health Sensormedics V-max automated device interfaces are exported with CP. Many other device interfaces are also available and you can view the complete list by visiting the <u>Clinical</u> <u>Procedures website (<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>. [<sup>21</sup>](#_bookmark35)From the Home page, select Find a Device and then search for devices by manufacturer, by type, or by name.

#### Visit the Clinical Procedures website to view specific information for a particular device. Click the vendor name to view the web page.

| Device                    | Vendor                                                                        | Type of Procedure Performed                                                                                                  | Type of report with Discrete data included |
|-------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [22](#_bookmark36)Clinivision | [<u>Puritan Bennett</u>](http://www.puritanbennett.com/)                          | Respiratory                                                                                                                      | Text                                           |
| Endoworks                     | [<u>Olympus</u>](http://www.olympus.com/)                                         | Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy | Text, GIF, JPG                                 |
| Muse                          | [<u>GE Healthcare</u>](http://www.gemedicalsystems.com/)                          | ECG, Exercise, Holter, Pacemaker ECG                                                                                             | PDF                                            |
| Sensormedics V-max            | [<u>Cardinal Health</u>](http://www.cardinal.com/) (formerly Viasys/Sensormedics) | PFT                                                                                                                              | PDF                                            |

#### For the latest vendor information, please see the <u>Clinical Procedures website</u> <u>(<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>.

> <span id="_bookmark33" class="anchor"></span>19 Patch MD\*1.0\*14 March 2008 Deleted vendor contact information for individual contacts.

> <span id="_bookmark34" class="anchor"></span>20 Patch MD\*1.0\*14 March 2008 Updated vendor name list.

> <span id="_bookmark35" class="anchor"></span>21 Patch MD\*1.0\*14 March 2008 Directions for finding a device on the CP website changed.

> <span id="_bookmark36" class="anchor"></span>22 Patch MD\*1.0\*14 March 2008 Device names unlinked due to unavailable links.

> <span id="_bookmark37" class="anchor"></span>Vendor Interface List

## Device Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Here are the setup instructions and vendor contact for each device.

### Clinivision

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vendor: Puritan Bennett Type: Respiratory

#### Description:

#### The uni-directional interface for this instrument is currently available.

#### Requirements:

#### This instrument requires a Clinivision vendor interface.

#### Setup Instructions:

#### This section describes the installation setup for the Clinivision system. Note that a new Protocol and HL Logical Link will need to be created for this device since it is a Persistent connected device.

Vendor Interface List

![](md-1-14-technical-manual-change-pages/003.png)

(Fig. 1)

#### Figure 1 displays the settings for the Clinivision device in CP Manager.

> Vendor Interface List

> OUT QUEUE BACK POINTER: 1789 OUT QUEUE FRONT POINTER: 1789

(Fig. 2)

#### Figure 2 shows an entry in the HL Logical Link file for the Clinivision device.

> NAME: MCAR3 Device Client ITEM TEXT: Instrument HL7 Event Driver

> TYPE: subscriber CREATOR: ACKERMAN,BILL

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This Protocol is used by the HL7 Package to send results to Vista from the Clinivision Instrument.

> IDENTIFIER: E TIMESTAMP: 59039,32152

> SENDING APPLICATION: INST-MCAR RECEIVING APPLICATION: MCAR-INST

> TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P LOGICAL LINK: MCAR3 INST

> VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK

> PROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NO

> RECEIVING FACILITY REQUIRED?: NO

(Fig. 3)

#### Fig. 3 shows the new Protocol that will need to be entered for the Link.

Vendor Interface List

![](md-1-14-technical-manual-change-pages/004.png)

(Figure 4)

#### [23](#_bookmark38)Figure 4. The device will need to be linked to a procedure in CP Manager.

#### Contact Clinivision and ask the contact to report the device to the production account, port 1030.

#### Transmission Instructions:

#### No information available at this time.

#### Manuals:

#### No information available at this time.

#### Vendor Contacts:

#### [<u>http://www.clinivision.com/contact/</u>](http://www.clinivision.com/contact/)

> <span id="_bookmark38" class="anchor"></span>23 Patch MD\*1.0\*6 March 2008 Screen capture updated to show new Processing Application field.

> <span id="_bookmark39" class="anchor"></span>Vendor Interface List

#### Trouble Shooting:

#### Is the machine plugged in? Is the machine on?

#### Are all cables connected correctly?

### Endoworks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Vendor: Olympus Type: Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy

#### Description:

#### The bi-directional interface for this instrument is currently available.

#### Requirements:

#### This instrument requires an Advanced Gateway vendor interface.

#### Setup Instructions:

#### The Olympus Interface is a non-persistent interface and can share its TCP/IP port address with other non-persistent devices. To configure the Olympus (Endoworks) software, it is recommended that you consult Olympus. Olympus has the correct setting for the Endoworks software that is needed to interface with CP.

#### Transmission Instructions:

#### No information available at this time

#### Manuals:

#### No information available at this time.

#### Costs:

#### No information available at this time.

#### Trouble Shooting:

#### Is the machine plugged in? Is the machine on?

#### Are all cables connected correctly?

<span id="_bookmark40" class="anchor"></span>Vendor Interface List

### Muse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vendor: GE Healthcare Type: ECG

#### Description:

#### The bi-directional interface for this instrument is currently available.

#### Requirements:

#### This instrument requires a Muse HL7 vendor interface.

#### Setup Instructions:

#### The Muse Interface is a Persistent Interface and must have its own TCP/IP Port address. For configuring the Muse software, it is recommended that you consult with GE Healthcare. GE Healthcare has the correct setting for the Muse software that is needed to interface with CP.

#### Transmission Instructions:

#### To send data to Clinical Procedures once the results have been sent from the Cart to the MUSE server, follow these steps:

#### The MUSE generated hard copy is assigned to a cardiologist for over-reading (reviewing).

#### Changes are made on the interpretation, signed by the doctor and returned to the EKG Department.

#### EKG Tech logs on to the MUSE. (All users of the MUSE are assigned a number and password with certain levels of NECESSARY access.)

#### EKG Tech selects over reader (reviewing Cardiologist).

#### EKG Tech selects the patient.

#### EKG Tech selects and then edits the interpretation.

#### EKG Tech selects either Confirm and Print, or Confirm. If Confirm and Print is selected, the HL7 result is sent, and the report is printed. If only Confirm is selected, just the HL7 result is sent.

#### Manuals:

#### No information available at this time.

#### Costs:

#### No information available at this time.

#### Trouble Shooting:

#### Is the machine plugged in?

> <span id="_bookmark41" class="anchor"></span>Vendor Interface List

#### Is the machine on?

#### Are all cables connected correctly?

### Sensormedics V-MAX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vendor: Cardinal Health Type: PFT

#### Description:

#### The bi-directional interface for this instrument is currently available.

#### Requirements:

#### This instrument requires a Netlink vendor interface.

#### [24](#_bookmark42)Configuration Files:

#### This file contains the configuration parameters for the Vmax software. The vendor should already have a copy of this file.

#### Setup Instructions:

#### The Sensormedics Interface is a Non-Persistent Interface and can share TCP/IP ports with other Non-Persistent device interfaces. The Sensormedics V-MAX software must have a shared directory to hold the report document that is created. The directory might be on the PC or on a network share. The key point is that the directory must be accessible from the Sensormedics V- MAX software.

#### Start the Sensormedics V-MAX software.

#### Click on the Reports Button.

#### Select the Netlinks/IS menu from the menu bar.

#### Select TCP/IP from the File Menu on the menu bar.

#### Enter the TCP/IP and Port address to the listener that will be receiving the data from the Sensormedics V-MAX software.

#### Exit back to the Reports Screen.

> <span id="_bookmark42" class="anchor"></span>24 Patch MD\*1.0\*14 March 2008 References to Vmaxconfigfile.zip and sample reports were removed because they are no longer hosted on the Clinical Procedures website.

Vendor Interface List

#### Select Setup from the File Menu and enter the Full NETWORK path to the Share directory where you want the PDF document to be stored.

#### Transmission Instructions:

#### A path must be setup where the PDF report will be stored prior to being transmitted to V*IST*A Imaging. This path is usually preset to C:\PDFFiles\\ and should be changed to \\(PC Network name)\PDFFiles\\ Also, the directory C:\PDFFiles should have Share enabled with Read, Write, Delete permissions for both Imaging and the PC on which the share directory exists.

#### The following instructions are for transmitting the final patient report to Clinical Procedures. Note: If the patient whose results you wish to send is already being displayed on the monitor, you can start at step 5.

#### From the Vmax Program Manager screen click the Find Patient Button.

#### ![](md-1-14-technical-manual-change-pages/005.png) The Find Patient window opens. No patients are displayed.

#### Set search criteria (Last Name, ID, etc.) if any, and click on F1. A list of patients matching your search criteria appears.

#### Select the patient whose results you wish to send by clicking on their name. The selected patient’s name is highlighted.

#### Click the F3 button to load the selected patients results data. The Vmax Program Manager screen reappears.

#### From the Vmax Program Manager screen click the Reports Button.

#### ![](md-1-14-technical-manual-change-pages/006.png) The Reports screen appears.

#### Select the report to process for this patient from the Reports selection box on the left side of the screen. The selected report appears in the upper left box as the Default Patient Report.

#### From the Menu bar click the PrintPDF button to compile the PDF report. A dialog box appears momentarily, indicating the progress of the PDF file creation.

#### From the Menu bar click Netlink/IS® to open the Netlink Transmission Manager.

#### ![](md-1-14-technical-manual-change-pages/007.png) The Transmission Manager screen appears

#### Files to be backed up:

#### You need to backup these files to preserve the operation of Vmax. These files should be backed up after the Vmax is working in production. This list was last updated on May 13, 2003.

> Vendor Interface List

#### Vision folder files used in Netlink communications.

#### (Depending on software version and configuration, not all files may be present) All files are located in the C:\Vision folder

> The following files always exist and have user-modifiable content

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Id_text.dbf</p></li>
</ul></th>
<th><ul>
<li><p>Invalid.dbf</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Text_cfg.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmit_cfg.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Xmitcom.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmithdft.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Xmithost.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitparm.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Xmitpath.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitxref.dbf</p></li>
</ul></td>
</tr>
</tbody>
</table>

> The following files sometimes exist and have user-modifiable content: They should be manually copied if needed.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Except</p></li>
</ul></th>
<th><ul>
<li><p>Replace</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>User_1.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_2.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>User_3.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_4.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>User_5.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_6.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>User_7.dbf</p></li>
</ul></td>
<td><blockquote>
<p>•</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### The following files are shipped standard with the software and are NOT user-modifiable. They should only be loaded from the software install disk.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Batchsnd.db1</p></li>
</ul></th>
<th><ul>
<li><p>Ctrl_str.dbf</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Received.txt</p></li>
</ul></td>
<td><ul>
<li><p>Response.txt</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Smascii.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Smhl7def.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Smvadef.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xexcept.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Xmiticon.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitprm.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Xreplace</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

Vendor Interface List

> The following files are modified by the software during operation and should NOT be user- modified: They should only be generated by running the software.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Batchsnd.dbf</p></li>
</ul></th>
<th><ul>
<li><p>Fileout1.txt</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Fileout2.txt</p></li>
</ul></td>
<td><ul>
<li><p>Text_rpt.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Text_rpt.fpt</p></li>
</ul></td>
<td><ul>
<li><p>Usehost</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### Manuals:

#### No information available at this time.

#### Costs:

#### No information available at this time.

#### Trouble Shooting:

#### Is the machine plugged in? Is the machine on?

#### Are all cables connected correctly?

> Vendor Interface List

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.

#### Action A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.

#### ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.

#### Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.

#### Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.

#### ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.

#### Attachments Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:

#### .txt Text files

#### .rtf Rich text files

#### .jpg JPEG Images

#### .jpeg JPEG Images

#### .bmp Bitmap Images

#### .tiff TIFF Graphics (group 3 and group 4 compressed and uncompressed types)

#### .pdf Portable Document Format

#### .html Hypertext Markup Language

#### .DOC (Microsoft Word files) are not supported. Be sure to convert .doc files to .rtf or to .pdf format.

> Glossary

#### Background Processing Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.

#### Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.

#### Boilerplate Text A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.

#### Browse Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).

#### Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.

#### Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).

#### Class Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.

#### Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.

#### Contingency Plan A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.

#### CP Clinical Procedures.

#### CP Definition CP Definitions are procedures within Clinical Procedures.

#### CP Study A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.

Glossary

#### CPRS Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.

#### Data Dictionary A description of file structure and data elements within a file.

#### Device A hardware input/output component of a computer system (e.g., CRT, printer).

#### Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.

#### Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.

#### Edit Used to change/modify data typically stored in a file.

#### Field A data element in a file.

#### File The M construct in which data is stored for retrieval at a later time. A computer record of related information.

#### File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.

> File Server A machine where shared software is stored.

#### Gateway The software that performs background processing for Clinical Procedures.

#### Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.

#### GUI Graphical User Interface - a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.

> Glossary

#### Interpreter Interpreter is a user role exported with USR\*1\*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation.

#### Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.

#### IRMS Information Resource Management Service.

#### Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.

#### LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.

#### M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi- Programming System. This is the programming language used to write all VistA applications.

#### MailMan An electronic mail, teleconferencing, and networking system.

#### Menu A set of options or functions available to users for editing, formatting, generating reports, etc.

#### Module A component of a software application that covers a single topic or a small section of a broad topic.

#### Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.

> Network Server Share A machine that is located on the network where shared files are stored.

#### Notebook This term refers to a GUI screen containing several tabs or pages.

#### OI Office of Information, formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.

Glossary

#### Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.

#### Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.

#### Page This term refers to a tab on a GUI screen or notebook.

#### Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).

#### Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.

#### Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.

#### Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

#### Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.

#### Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.

> \<RET\> Carriage return.

#### Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

#### Security Key A function which unlocks specific options and makes them accessible to an authorized user.

#### Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.

#### Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.

> Glossary

#### Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.

#### Status Symbols Codes used in order entry and Consults displays to designate the status of the order.

#### Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.

#### Title Titles are definitions for documents. They store the behavior of the documents which use them.

#### TIU Text Integration Utilities.

#### User A person who enters and/or retrieves data in a system, usually utilizing a CRT.

#### User Class User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.

#### User Role User Role identifies the role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).

#### Utility An M program that assists in the development and/or maintenance of a computer system.

#### Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.

#### VistA Veterans Health Information Systems and Technology Architecture.

#### Workstation A personal computer running the Windows 9x or NT operating system.


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*11 Technical Manual change pages

### June 2009

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This distribution contains change pages for patch MD\*1.0\*11 of the Clinical Procedures 1.0 Technical Manual and Package Security Guide.

> The change pages for CP Patch 2, CP Patch 14, and CP Patch 6 should be inserted before the change pages for CP Patch 11:

> <u>File Name:</u> <u>Patch:</u>

> MD_1_P2_TM. PDF MD\*1.0\*2

> MD_1_P14\_ TM.PDF MD\*1.0\*14

> MD_1_P6_TM.PDF MD\*1.0\*6

> MD_1_P11_TM.PDF MD\*1.0\*11

> Patch MD\*1.0\*11 pages:

> <u>Replace Pages:</u> <u>With Pages:</u>

> Title page Title page

> Revision History Revision History

> Table of Contents Table of Contents

> 4-1 to 4-4 4-1 to 4-4

> 5-5 to 5-6 5-5 to 5-6

> 6-3 to 6-28 6-3 to 6-26

> ![](md-1-11-technical-manual-change-pages/001.png)

CLINICAL PROCEDURESTECHNICAL MANUAL AND PACKAGE SECURITY GUIDE

April 2004

### CP Definition File - \#702.01

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This file defines all the procedures used by the Clinical Procedures package. All elements that define a procedure are in this file. This file is exported with data, but entries may be added by the site.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>702.01,.01</td>
<td>Free Text 3-30 characters in length</td>
<td><blockquote>
<p>This field contains the name of the procedure. It should be descriptive of the procedure and contain 3-30 alphanumeric characters. The first character MUST be a letter. To maintain consistency it is recommended that all procedures be entered in</p>
<p>UPPERCASE letters as well.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Treating Specialty</td>
<td>702.01,.02</td>
<td><p>Pointer to Facility Treating Specialty</p>
<p>(#45.7) file</p></td>
<td><blockquote>
<p>This field defines the specialty that this procedure falls under.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Require External Data</td>
<td>702.01,.03</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><blockquote>
<p>Setting this field to Yes will force a consult for this procedure to be processed via the CP User executable for matching whether or not there are instruments</p>
<p>associated with it.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Default TIU Note</td>
<td>702.01,.04</td>
<td><p>Pointer to TIU Document Definition</p>
<p>(#8925.1) file</p></td>
<td><blockquote>
<p>This field contains a TIU Note Title to use as the default when CP creates a note for</p>
<p>interpretation for this procedure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Hospital Location</td>
<td>702.01,.05</td>
<td>Pointer to Hospital Location (#44) file</td>
<td><blockquote>
<p>This is the location that will be</p>
<p>used when creating the TIU Note for interpretation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>1Processing</p>
<p>Application</p></td>
<td>702.01,.06</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Default</p></li>
<li><p>– Hemodialysis</p></li>
</ol></td>
<td><blockquote>
<p>This field is used to indicate if this is a Hemodialysis procedure or not. The field is a set of codes, 1=DEFAULT so it will be processed by Clinical Procedures or 2=HEMODIALYSIS and the procedure will be processed by</p>
<p>the Hemodialysis application.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Auto Submit</td>
<td>702.01,.07</td>
<td>Set:</td>
<td><blockquote>
<p>This field only applies to bi-</p>
</blockquote></td>
</tr>
</tbody>
</table>

> File List and Related Information

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></th>
<th><blockquote>
<p>directional instruments. It is used to indicate whether or not the image attachment should be automatically submitted to VistA Imaging once the procedure is performed and the result is passed</p>
<p>to CP.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>External Data Directory</td>
<td>702.01,.08</td>
<td>Free Text 3-150 characters in length</td>
<td><blockquote>
<p>This field contains a reference to a network share where user supplied attachments are located</p>
<p>for this procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Active</td>
<td>702.01,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><blockquote>
<p>Yes/No to indicate active procedures that can be linked to</p>
<p>Consults.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Instrument (multiple)</td>
<td>702.011,.01</td>
<td><p>Pointer to CP Instrument</p>
<p>(#702.09) file</p></td>
<td><blockquote>
<p>Contains a pointer to an instrument that generates results</p>
<p>for this procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>1Processed Result</td>
<td>702.01,.12</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Final Result</p></li>
<li><p>- Multiple Results 2 – Cumulative Result</p></li>
</ol></td>
<td><blockquote>
<p>This field is a flag which indicates whether a final result, multiple results, or cumulative result is associated with this</p>
<p>procedure.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Exported Options

### From: MD*1*20 Technical Manual change pages

## Revised November 2010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Department of Veterans Affairs Office of Information & Technology Office of Enterprise Development

> Revision History

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Description</strong></th>
<th><strong>Date</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Originally released.</td>
<td>April 2004</td>
<td></td>
</tr>
<tr class="even">
<td>1Patch MD*1.0*1 released.</td>
<td>July 2004</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patch MD*1.0*2 released.</p>
</blockquote></td>
<td>August 2006</td>
<td></td>
</tr>
<tr class="even">
<td>2Patch MD*1.0*5 released August 2006. Updated File List, Package Default Definition, Parameter Definitions, and menu options.</td>
<td>Documented February 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3Patch MD*1.0*14 released. Updated Routine Descriptions, File List, Parameter Definitions, Protocols, menu options, and Cross References. Deleted bad references to Sample Reports in Ch. 15.</td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>4Patch MD*1.0*6 released. Added</p>
<p>description of Hemodialysis module and 508 Compliance to Introduction; updated Routine Descriptions, File List, Package Default Definition, Remote Procedure Calls, Parameter Definitions, menu options, Cross References, Callable Routines, External Relations, Internal Relations, and Glossary. Removed individual vendor contact information from Ch.15.</p></td>
<td>May 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5Patch MD*1.0*11 released. Updated Routine Description, File and Field Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2009</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6Patch MD*1.0*21 released. Updated Routine Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7Patch MD*1.0*20 released. Added new Exported Options and Updated the Routine Descriptions. Added new Parameter Definitions.</td>
<td>November 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*1 and MD\*1.0\*2 July 2004 Patch 2 release added.

> 2 Patch MD\*1.0\*5 August 2006 Patch 5 release added.

> 3 Patch MD\*1.0\*14 March 2008 Patch 14 release added.

> 4 Patch MD\*1.0\*6 May 2008 Patch 6 release added.

> 5 Patch MD\*1.0\*11 June 2009 Patch 11 release added.

> 6 Patch MD\*1.0\*21 June 2010 Patch 21 release added.

> 7 Patch MD\*1.0\*20 November 2010 Patch 20 release added

## Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1MDAPI ; HOIFO/DP/NCA - CP API Calls ; \[05-05-2003 10:28\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

MDAPI1 ; HOIFO/NCA - Electrocardiogram Data Extraction ;12/4/02 12:32

> ;;1.0;CLINICAL PROCEDURES;\*\*1\*\*;Apr 01, 2004;Build 4

> MDAR7M ; HOIFO/NCA - Get Text Impression ;2/27/09 12:38

> ;;1.0;Clinical Procedures;\*\*21\*\*;Apr 01, 2004;Build 24 MDARP3 ; HOIFO/NCA - Get Procedures for Medicine ;1/13/04 14:35

;;1.0;CLINICAL PROCEDURES;\*\*10,13\*\*;Apr 01, 2004;Build 22

MDARSET ; HOIFO/NCA - High Volume Check-In Setup ;6/30/09 10:00

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

MDCLN ;HIOFO/NCA - Cleanup Disabled Studies ;4/19/01 11:52

> ;;1.0;Clinical Procedures;\*\*21\*\*;Apr 01, 2004;Build 24

MDCVT ; HOIFO/DP/NCA - Medicine Package Conversion ;10/20/04 12:49

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4

MDCVT1 ; HOIFO/NCA - Medicine Package Conversion (Cont.) ;1/6/05 15:12

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4

> MDCVTU ; HOIFO/NCA - Medicine Conversion Verification Utility ; \[08-28-2003 11:34\]

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4 MDESPRT ;HOIFO/NCA - ELECTRONIC SIGNATURE PRINT ;12/21/04 09:24

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4

MDDEVCL ;HOIFO/NCA - Collect Device Data ;8:34 AM 9 Jun 2005

> ;;1.0;CLINICAL PROCEDURES;\*\*20\*\*;Apr 01, 2004

MDHL7A ; HOIFO/WAA - Routine to Decode HL7 for CP ;05/21/09 15:57

;;1.0;CLINICAL PROCEDURES;\*\*6,11,21\*\*;Apr 01, 2004;Build 24

> MDHL7B ; HOIFO/WAA -Bi-directional interface routine ;7/23/01 11:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7BH ; HOIFO/WAA -Bi-directional interface (HL7) routine ;10/26/09 09:21

> ;;1.0;CLINICAL PROCEDURES;\*\*11,21,20\*\*;Apr 01, 2004;Build 30

> MDHL7D ; HOIFO/WAA -B-Braun, Fresenius Dialysis ; 06/08/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

MDHL7E ; HOIFO/WAA -Olympus/CMore/Pentax Endoscopy ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7K1 ; HOIFO/WAA-KenitDx Interface ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDHL7K2 ; HOIFO/WAA -HP EnConcert Echo ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4 MDHL7M1 ; HOIFO/WAA - Muse EKG ; \[02-06-2002 16:13\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7MCA ; HOIFO/REL-Routine to Decode HL7 for MEDICINE ; \[05-07-2001 10:38\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDHL7MCX ; HIRMFO/WAA - Generate HL7 Error Message for MEDICINE ; \[05-07-2001 10:38\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7P1 ; HOIFO/WAA-Sensormedics,Jaeger Pulmonary ; 06/08/00

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

MDHL7R1 ; HOIFO/WAA -Clinivision Resporatory ; 06/13/02

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7U ; HOIFO/WAA -Routine utilities for CP ;7/23/01 11:41

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7U1 ; HOIFO/WAA -Routine utilities for CP PROCESSING OBX ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;\*\*11\*\*;Apr 01, 2004;Build 68

> MDHL7U2 ; HOIFO/WAA -Utilities for CP PROCESSING OBX text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDHL7U3 ; HOIFO/WAA -Utilities for CP to process HL7 messages ;02/17/10 15

> :59

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21\*\*;Apr 01, 2004;Build 24

> MDHL7X ; HOIFO/WAA -Generate HL7 Error Message ; 06/08/00

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDHL7XXX ; HOIFO/DP - Loopback device for CP ;4/10/09 09:20

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDKRPC1 ;HIOFO/FT-RPC to return patient data ;2/19/08 13:13

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103 MDKRPC2 ; HOIFO/DP - RPC Calls (Cont.) ;11/27/07 09:42

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDKUTL ; HOIFO/DP - Renal Utilities ;11/29/07 14:45

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01, 2004;Build 22

> MDKUTLR ; HOIFO/DP - Renal Utilities RPC;11/29/07 14:45

> 1 Patch MD\*1.0\*20 November 2010 Update routine list with new routines and patch history changes.

> April 2004 Clinical Procedures V. 1.0 4-1

> Technical Manual and Package Security Guide

> Routine Descriptions

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

MDNCHK ; HOIFO/NCA - CP Multiple Result Check ;4/26/05 15:17

> ;;1.0;CLINICAL PROCEDURES;\*\*11,21,20\*\*;Apr 01, 2004;Build 68

> MDOUTOR ; HOIFO/NCA - Post Conversion Routine ; \[04-14-2003 10:51\]

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4

> MDPCE ; HIRMFO/NCA - Routine For Data Extract ;6/9/08 13:29

> ;;1.0;CLINICAL PROCEDURES;\*\*5,21\*\*;Apr 01, 2004;Build 24

> MDPCE1 ; HOIFO/NCA - Updated Routine For Data Extract ; \[05-28-2002 12:55\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDPCE2 ; HOIFO/NCA - Routine For Data Extract For Hemo Dialysis;9/10/04 11

> :23 ;1/20/10 10:00

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21\*\*;Apr 01, 2004;Build 24 MDPFTP1 ;HOIFO/NCA - PFT REPORT-DEMO INFO ;3/15/04 11:55

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004;Build 4 MDPFTP2 ; HOIFO/NCA - PFT REPORT-VOLUMES ;3/15/04 10:00

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004;Build 4 MDPFTP2A ; HOIFO/NCA - PFT REPORT-FLOWS ;3/17/04 08:22

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004;Build 4

MDPFTP3 ; HOIFO/NCA - PFT REPORT-SPECIAL STUDIES (PT 2) ;3/17/04 12:48

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004;Build 4 MDPOST ; HOIFO/DP - Post Init ;2/18/04 11:39

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4 MDPOST04 ; HOIFO/DP - Post Init ; 2/18/04 11:39

> ;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 6 MDPOST06 ; HOIFO/DP - Post Init ;2/7/07 16:15

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDPOST1 ; HOIFO/NCA/DP - Build CP DEFINITION file (#702.01) - Optional Post Init ; \[12-04-2002 13:06\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4 MDPOST21 ; HOIFO/NCA - Post Init ;2/7/07 16:15

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDPOST6A ;HOIFO/NCA-Convert Existing Notes to New File ;11/28/07 14:31

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDPS1 ; HOIFO/NCA - CP/Medicine Report Generator ;5/18/04 09:48

> ;;1.0;CLINICAL PROCEDURES;\*\*2,10,13,21\*\*;Apr 01, 2004;Build 24

> MDPS2 ; HOIFO/NCA - CP/Medicine Report Generator (Cont.) ;5/18/04 09:41

> ;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004;Build 4

MDPS3 ; HOIFO/NCA - Remote Data View Data Retriever for CP ;8/26/05 14:37

> ;;1.0;CLINICAL PROCEDURES;\*\*2,5,13\*\*;Apr 01, 2004;Build 22

> MDPS4 ; HOIFO/NCA - Retrieve List of Consult Procedures ;1/26/06 12:45

> ;;1.0;CLINICAL PROCEDURES;\*\*13\*\*;Apr 01, 2004;Build 22

> MDPS5 ; HOIFO/NCA - Retrieve List of Consult Procedures for RDV ;3/4/05 1 3:29

> ;;1.0;CLINICAL PROCEDURES;\*\*13\*\*;Apr 01, 2004;Build 22

MDPSU ; HOIFO/NCA - CP/Medicine Report Generator Utility;5/18/04 09:48

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDPSUL ; HOIFO/NCA - HS Component Utility;5/18/04 09:48 ;10/5/09 09:33

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

MDPURGE ;HOIFO/NCA - Study Clean-Up process ;6/18/08 10:15

> ;;1.0;CLINICAL PROCEDURES;\*\*11\*\*;Apr 01, 2004;Build 68

MDRPCNT ; HOIFO/NCA - Document Handler Object (TMDNOTE) ;5/23/05 15:50

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDRPCNT1 ; HOIFO/NCA - Object RPCs (TMDNOTE) Continued 2;10/29/04 12:20 ;2/2 5/09 16:08

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21\*\*;Apr 01, 2004;Build 24 MDRPCOD ; HOIFO/DP - Object RPCs (TMDProcedureDef) ; \[01-09-2003 15:20\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4 MDRPCOG ; HOIFO/DP - CP Gateway ; \[01-09-2003 15:20\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103 MDRPCOL ; HOIFO/DP - Object RPCs (Logfile) ; \[02-11-2002 13:41\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

MDRPCOO ; HOIFO/DP - Object RPCs (TMDOutput) ; \[03-24-2003 15:44\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4 MDRPCOP ; HOIFO/DP - Object RPCs (TMDPatient) ;8/3/09 10:39

> ;;1.0;CLINICAL PROCEDURES;\*\*4,6,11,20\*\*;Apr 01, 2004;Build 85 MDRPCOP1 ; HOIFO/DP - Object RPCs (TMDPatient) - Cont. ; 01-09-2003 15:21

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103 MDRPCOR ; HOIFO/DP - Object RPCs (TMDRecordId) ; \[01-10-2003 09:14\]

> ;;1.0;CLINICAL PROCEDURES;\*\*17,20\*\*;Apr 01, 2004

MDRPCOT ; HOIFO/DP/NCA - Object RPCs (TMDTransaction) ;10/26/09 10:23

;;1.0;CLINICAL PROCEDURES;\*\*5,6,11,21\*\*;Apr 01, 2004;Build 24

> MDRPCOT1 ; HOIFO/NCA/DP - Object RPCs (TMDTransaction) - Continued ;3/13/09 11:18

> ;;1.0;CLINICAL PROCEDURES;\*\*5,11,21\*\*;Apr 01, 2004;Build 24

> MDRPCOT2 ; HOIFO/NCA - Object RPCs (TMDTransaction) Continued 2;10/29/04 12:

> 4-2 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Routine Descriptions

> 20 ;3/12/08 09:18

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21,20\*\*;Apr 01, 2004;Build 24

> MDRPCOTA ; HOIFO/NCA - Object RPCs (TMDTransaction) Continued 2;10/29/04 12: 20 ;3/12/08 09:18

> ;;1.0;CLINICAL PROCEDURES;\*\*20\*\*;Apr 01, 2004;Build 85

> MDRPCOTH ; HOIFO/NCA - Process High Volume Procedure Results ;2/27/09 10:08

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24 MDRPCOU ; HOIFO/DP - Object RPCs (TMDUser) ; \[01-09-2003 15:21\]

> ;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

> MDRPCOV ; HOIFO/DP - Object RPCs (TMDParameter) ; \[04-15-2003 12:42\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004;Build 4

MDRPCOW ; HOIFO/DP/NCA - Billing Widget ;10/3/05 12:17

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103 MDRPCU ; HOIFO/DP - Object RPC Utilities ; \[05-23-2003 10:16\]

> ;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 6 MDRPCW ; HOIFO/NCA - Calls to AICS;04/01/2003 ;01/21/10 11:51

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21,20\*\*;Apr 01, 2004;Build 24

> MDRPCW1 ; HOIFO/NCA - MD TMDENCOUNTER Object; \[05-28-2002 12:55\] ;2/16/10 1 6:17

> ;;1.0;CLINICAL PROCEDURES;\*\*6,21,20\*\*;Apr 01, 2004;Build 24 MDRPCWU ; HOIFO/NCA - CPT Code Query; \[05-28-2002 12:55\] ;2/16/10 16:17

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDSTATU ; HOIFO/NCA - Print List of Document Titles Needed ;10/21/04 13:44

> ;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 4

MDSTUDL ; HOIFO/NCA - Clinical Procedures Studies List ;10/26/05 11:46

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

MDSTUDW ; HOIFO/NCA - Print a List of Procedures With Incomplete Workload ;3

> /2/09 10:00

> ;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 24

> MDUXML ; HOIFO/WAA -Utilities for XML text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDUXMLM ; HOIFO/WAA -Utilities for XML text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDUXMLOX ; HOIFO/WAA -OBX converter XML text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> MDUXMLU1 ; HOIFO/WAA -Utilities for XML text ; 7/26/00

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

MDWCAN ;HOIFO/NCA - Process No-Shows and Cancels ;7/29/08 09:50

;;1.0;CLINICAL PROCEDURES;\*\*11,21\*\*;Apr 01, 2004;Build 24

> MDWCHK ; HOIFO/NCA - Create CP Studies for Existing Procedures ;12/13/07 1 5:52

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 22

> MDWOR ; HOIFO/NCA - Main Routine to Decode HL7 ;9/8/08 15:20

> ;;1.0;CLINICAL PROCEDURES;\*\*14,11,21,20\*\*;Apr 01,2004;Build 24

> MDWORC ; HOIFO/NCA - Main Routine to Decode HL7 from Consult ;1/8/08 15:00

> ;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 22

MDWORSR ; HOIFO/NCA - Daily Schedule Studies;7/2/04 12:39 ;10/15/08 13:39

> ;;1.0;CLINICAL PROCEDURES;\*\*14,11,21,20\*\*;Apr 01,2004;Build 24

> MDWSETUP ; HOIFO/NCA - Auto Study Check-In Setup ;3/18/08 14:14

> ;;1.0;CLINICAL PROCEDURES;\*\*14,11\*\*;Apr 01, 2004;Build 68 MDXMLFM ; HOIFO/DP - Fileman -\> XML Utilities ; \[01-10-2003 09:14\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103 MDXMLFM1 ; HOIFO/DP/NCA - Data -\> XML Utilities ; \[01-10-2003 09:14\]

> ;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 103

> April 2004 Clinical Procedures V. 1.0 4-3

> Technical Manual and Package Security Guide

> Routine Descriptions

> 4-4 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> VALUE HELP: Enter 0 for None, 1 for Outpatient, 2 for Inpatient, or 3 for both.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter procedures that needs the study to be auto checked-in. INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0

> DESCRIPTION:

> This parameter contains a list of procedures that will be used

> to auto check-in the CP studies during the procedures request in CPRS and whether appointments are scheduled for the procedure.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CLINIC QUICK LIST DISPLAY TEXT: Clinic Quick List For CP MULTIPLE VALUED: Yes INSTANCE TERM: Clinic

> VALUE TERM: Procedure VALUE DATA TYPE: pointer VALUE DOMAIN: 702.01

> VALUE HELP: Select a procedure for the clinic.

INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 44

> INSTANCE HELP: Enter clinics that need CP studies to be checked-in. DESCRIPTION:

> List of clinics used as a source to get a list of patients that need to have CP studies checked-in. This only applies to studies with procedures that have multiple results such as Hemodialysis, Respiratory Therapy, and sleep studies.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

#### NAME: MD CLINICS WITH MULT PROC

> DISPLAY TEXT: Clinics With Multiple Procedures

> MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Clinic VALUE DATA TYPE: pointer VALUE DOMAIN: 44

> VALUE HELP: Enter a clinic for the procedure.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter a procedure.

> INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0 DESCRIPTION:

> If you have a clinic for multiple procedures, populate this parameter with the procedure and associate it to a clinic.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD CLINIC ASSOCIATION DISPLAY TEXT: MD Clinic Association MULTIPLE VALUED: Yes INSTANCE TERM: Sequence

> VALUE TERM: Clinic;Procedure Association Value

> PROHIBIT EDITING: No VALUE DATA TYPE: free text INSTANCE DATA TYPE: numeric INSTANCE DOMAIN: 1:9999

> INSTANCE HELP: Enter the sequence to associate a clinic and procedure. DESCRIPTION:

> This parameter is used to identify the clinic and procedure association. Each item should be entered with the following format

> Clinic internal entry number\_";"\_Procedure internal entry number PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1 Patch MD\*1.0\*11 June 2009 Parameter Definition added

> April 2004 Clinical Procedures V. 1.0 6-15

> Technical Manual and Package Security Guide

> Exported Options

> NAME: MD CRC BYPASS DISPLAY TEXT: Bypass CRC Checking MULTIPLE VALUED: No VALUE TERM: Bypass CRC Checking VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to 'Yes' to prevent the client application from verifying its CRC Value at startup.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CRC VALUES

> DISPLAY TEXT: Clinical Procedures CRC Values MULTIPLE VALUED: Yes

> INSTANCE TERM: Executable or Library Name

> VALUE TERM: CRC Value PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:15 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

> DESCRIPTION:

> This parameter is used to store the CRC values for the most recent versions of executable and libraries. Use the Tools menu on the CPManager program to calculate the needed CRC Values of the current versions.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

#### NAME: MD DAYS FOR INSTRUMENT DATA

> DISPLAY TEXT: Temporary instrument data life (Days) MULTIPLE VALUED: No VALUE TERM: Days

> PROHIBIT EDITING: No VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

> DESCRIPTION:

> The number of days to keep data from the auto-instruments after the data has been associated with a Clinical Procedures report.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD DAYS TO RETAIN COM STUDY

> DISPLAY TEXT: Days to Retain Completed Study

> MULTIPLE VALUED: No VALUE TERM: Days

> PROHIBIT EDITING: No VALUE DATA TYPE: numeric VALUE DOMAIN: 1:365

> VALUE HELP: Enter the number of days from 1 to 365 DESCRIPTION:

> The number of days after check-in date/time to display the study that has been complete in the CPUser application. Studies that have procedures with multiple or cumulative results are NOT included.

> Cumulative and multiple results studies will have a default value of 365.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD DAYS TO RET COM MULT

> DISPLAY TEXT: Days to Retain Completed Multiple Study MULTIPLE VALUED: No VALUE TERM: Days

> VALUE DATA TYPE: numeric VALUE DOMAIN: 1:365

> VALUE HELP: Enter the number of days from 1 to 365 DESCRIPTION:

> The number of days after check-in date/time to display the study

> 1 Patch MD\*1.0\*6 May 2008 Parameter Definition added.

> 2 Patch MD\*1.0\*20 November 2010 Parameter Definitions Added.

16. Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> that has been completed in the CPUser application. This only pertains to studies that have procedures with multiple studies.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD DEVICE SURVEY TRANSMISSION DISPLAY TEXT: Device Survey

> Transmission

> MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

> VALUE HELP: Enter 'Y' for 'YES' or 'N' for 'NO'. DESCRIPTION:

> Used to determine if the site wants to transmit the device survey to Hines. Enter 'Y' for 'YES' to send the survey or 'N' for 'NO' to suppress the transmission.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD FILE EXTENSIONS DISPLAY TEXT: Imaging File Types MULTIPLE VALUED: Yes INSTANCE TERM: Extension

> VALUE TERM: File type PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:80

> VALUE HELP: Enter a description of this file type

> INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 2:10

> INSTANCE HELP: Enter the extension of the file type with a '.' INSTANCE VALIDATION CODE: K:X'?1".".9ULN X

> DESCRIPTION:

> This parameter stores a list of valid file types and the associated extensions of these files.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD GATEWAY DISPLAY TEXT: CP Gateway Parameters MULTIPLE VALUED: Yes INSTANCE TERM: Parameter Name

> VALUE TERM: Parameter Value VALUE DATA TYPE: free text VALUE DOMAIN: 1:255 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:255

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD GET HIGH VOLUME DISPLAY TEXT: Get High Volume MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Get String VALUE DATA TYPE: free text INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter a high volume procedure. INSTANCE SCREEN CODE: I

> +\$P(^MDS(702.01,+Y,0),"^",6)'=2&(+\$P(^MDS(702.01,+Y,0)

> ,"^",11)'=2)&(\$P(^MDS(702.01,+Y,0),"^",9)\>0) DESCRIPTION:

> This parameter will contain a free text string that contains two pieces of data delimited by a semicolon ';'. The two pieces of data are: 1) 1/0 (Yes/No) to indicate whether or not the text of the result should be

> added to the note, 2) 1/0 (Yes/No) to enter the text of the result as the significant finding of the Consult. (If you enter a 0, the note will be auto closed with the text inside.)

> Example string: 1;0

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1 Patch MD\*1.0\*21 June 2010 Parameter Definition added.

> April 2004 Clinical Procedures V. 1.0 6-17

> Technical Manual and Package Security Guide

> Exported Options

> NAME: MD HFS SCRATCH

> DISPLAY TEXT: VistA Scratch HFS Directory

> MULTIPLE VALUED: No VALUE TERM: Directory name

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

> VALUE HELP: Enter in an OS level directory DESCRIPTION:

> Contains the directory specification for the Kernel OPEN^%ZISH call. This directory should be accessible for read/write operations by all CP users.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD IMAGING XFER DISPLAY TEXT: Imaging Network Share MULTIPLE VALUED: No VALUE TERM: Imaging Network Share

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 DESCRIPTION:

> This parameter contains the name of a network server, share, and path (UNC) to a location where Clinical Procedures can put files for pick-up by the Imaging background processor for archiving.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1 NAME: MDK APPLICATION INSTALL DISPLAY TEXT: MDK Application Install

> MULTIPLE VALUED: Yes

> INSTANCE TERM: Installation Distribution Info

> VALUE TERM: Distribution Info Value PROHIBIT EDITING: No VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> DESCRIPTION:

> This parameter is used to store the Hemodialysis application distribution information. The information includes the following:

1.  Date/Time when application first launched.
2.  User Name
3.  System Option Loaded (Y/N)
4.  Workstation of where the application was launched. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MDK GUI VERSION

> DISPLAY TEXT: Hemodialysis Version Compatibility

> MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version VALUE TERM: Compatible with current server version

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:40

> DESCRIPTION:

> This parameter is used to store the application:versions that are compatible with the current server version of Hemodialysis. Instance format

> of APPLICATION:VERSION (example: HEMODIALYSIS.EXE:0.0.0.0). PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD MEDICINE CONVERTED DISPLAY TEXT: Medicine Package

> Converted

> 1 Patch MD\*1.0\*6 May 2008 Parameter Definition added.

> 2 Patch MD\*1.0\*5 August 2006 Parameter Definition added.

> 6-18 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> Used to determine if the Medicine Package has been converted. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD NOT ADMN CLOSE MUSE NOTE DISPLAY TEXT: NOT ADMN Close Muse

> Note

> MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> This parameter is used to indicate the note should not be administratively closed with the proxy user CLINICAL, DEVICE PROXY SERVICE but the interpreter of the procedure for the MUSE device. The default is "No".

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD OFFLINE MESSAGE DISPLAY TEXT: Offline message

> MULTIPLE VALUED: No VALUE TERM: Offline Message VALUE DATA TYPE: word processing

> DESCRIPTION:

> This parameter contains a message to display to the users when the Clinical Procedures application is offline.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD OLYMPUS 7 DISPLAY TEXT: MD OLYMPUS 7 MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

> VALUE HELP: Enter Yes/No whether you have Olympus version 7.3.7. DESCRIPTION:

> This parameter definition indicates whether the Olympus device is version 7.3.7. The value is Yes/No. The default value

> is "No".

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD ONLINE

> DISPLAY TEXT: Clinical Procedure Online/Offline MULTIPLE VALUED: No

> VALUE TERM: Is Clinical Procedures Online

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

> VALUE HELP: Enter 'Yes' to allow access to CP DESCRIPTION:

> This parameter controls access to the Clinical Procedures package. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 3NAME: MD USE APPOINTMENT DISPLAY TEXT: Use Appointment

> Location

> MULTIPLE VALUED: No VALUE TERM: Use Appointment location VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to Yes to allow CPUser to use the location of the appointment selected during CP study check-in for the workload.

> 1 Patch MD\*1.0\*21 June 2010 Parameter Definition added. 2 Patch MD\*1.0\*11 June 2009 Parameter Definition added. 3 Patch MD\*1.0\*11 June 2009 Parameter Definition added.

> April 2004 Clinical Procedures V. 1.0 6-19

> Technical Manual and Package Security Guide

> Exported Options

> Otherwise, the hospital location of the CP Definition will be used. Enter RETURN to continue or '^' to exit:

> If no value is entered, the default value is No. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD USE APPT WITH PROCEDURE

> DISPLAY TEXT: Use Appointment With Procedure MULTIPLE VALUED: No

> VALUE TERM: Use appointment with procedure

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> Enter "Y" or "N" for Yes/No on whether your site selects the appointment scheduled for outpatients during the procedure request in CPRS.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD USE NOTE DISPLAY TEXT: Use Note VALUE TERM: Yes/No VALUE DATA TYPE: yes/no

> DESCRIPTION:

> This parameter indicates that Clinical Procedures will use the note for the text of the result instead of the Significant Finding field in Consult.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD USER DEFAULTS DISPLAY TEXT: CP User Defaults

> MULTIPLE VALUED: Yes INSTANCE TERM: Parameter setting VALUE TERM: Parameter value PROHIBIT EDITING: No

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> DESCRIPTION:

> This parameter is used to store a users default parameter settings. Each setting is defined on the client.

> PRECEDENCE: 1 ENTITY FILE: USER

> NAME: MD VERSION CHK DISPLAY TEXT: Version Compatibility MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version VALUE TERM: Compatible with current server version

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

> DESCRIPTION:

> This parameter is used to store the application:versions that are compatible with the current server version of Clinical Procedures. Instance format

> of APPLICATION:VERSION (example: CPMANAGER.EXE:0.0.0.0). PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD WEBLINK

> DISPLAY TEXT: Clinical Procedures Home Page

> MULTIPLE VALUED: No VALUE TERM: Web Address

> VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 DESCRIPTION:

> This parameter contains the web address for the Clinical Procedures home

> 1 Patch MD\*1.0\*14 March 2008 Parameter Definition added.

> 2 Patch MD\*1.0\*21 June 2010 Parameter Definition Added.

> 6-20 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> page. This can be modified to a local address in the event that the pages are downloaded to be displayed from a local server location.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> April 2004 Clinical Procedures V. 1.0 6-21

> Technical Manual and Package Security Guide

> Exported Options

> Protocols

> NAME: MCAR Device Client ITEM TEXT: Instrument Device Client TYPE: subscriber CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: MEDICINE

> DESCRIPTION: Subscriber protocol for sending data to Vista from clinical instruments.

> TIMESTAMP: 59276,54156 RECEIVING APPLICATION: MCAR-INST TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P LOGICAL LINK: MCAR INST

> VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> NAME: MCAR Device Server ITEM TEXT: Instrument HL7 Event Driver TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: MEDICINE

> DESCRIPTION: This protocol is used by the HL7 package to send results to Vista from various clinical instrumentation.

> TIMESTAMP: 59276,54156 SENDING APPLICATION: INST-MCAR TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P VERSION ID: 2.3

> SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> SUBSCRIBERS: MCAR Device Client

> NAME: MCAR ORM CLIENT TYPE: subscriber

> CREATOR: <span class="mark">REDACTED</span> RECEIVING APPLICATION: INST-MCAR EVENT TYPE: O02 RESPONSE MESSAGE TYPE: ORR SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO ROUTING LOGIC: Q

> NAME: MCAR ORM SERVER

> ITEM TEXT: Clinical Procedures ORM Protocol Server

> TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP: 59276,54156 SENDING APPLICATION: MCAR-INST TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

> VERSION ID: 2.3 SUBSCRIBERS: MCAR ORM CLIENT

> 1NAME: MD RECEIVE GMRC

> ITEM TEXT: Clinical Procedures receives messages from Consult TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This protocol receives messages from Consult. (IA 3140) ENTRY ACTION: D EN^MDWORC(.XQORMSG) TIMESTAMP: 60934,38793

> NAME: MD RECEIVE OR

> ITEM TEXT: Clinical Procedures receives order msgs from CPRS TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This protocol receives order messages from CPRS. (IA 3135) ENTRY ACTION: D EN^MDWOR(.XQORMSG) TIMESTAMP: 60934,38793

> 1 Patch MD\*1.0\*14 March 2008 Protocols added to support the auto study check-in.

> 6-22 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

### HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MCAR-INST ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER

> COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> April 2004 Clinical Procedures V. 1.0 6-23

> Technical Manual and Package Security Guide

> Exported Options

### HL Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NODE: MCAR INST LLP TYPE: TCP

> DEVICE TYPE: Single-threaded Server STATE: Reading

> AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:46:17

> TASK NUMBER: 526320 SHUTDOWN LLP ?: NO QUEUE SIZE: 100

> RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

> ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

> TCP/IP PORT: 9026 TCP/IP SERVICE TYPE: SINGLE LISTENER

> PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

> IN QUEUE BACK POINTER: 331 IN QUEUE FRONT POINTER: 331 OUT QUEUE BACK POINTER: 220 OUT QUEUE FRONT POINTER: 210

> NODE: MCAR OUT LLP TYPE: TCP

> DEVICE TYPE: Non-Persistent Client STATE: Openfail

> AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:45:47

> TASK NUMBER: 529066 SHUTDOWN LLP ?: NO

> QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

> READ TIMEOUT: 60 ACK TIMEOUT: 60

> EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: 10.3.17.157

> TCP/IP PORT: 9028 TCP/IP SERVICE TYPE: CLIENT (SENDER)

> PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

> IN QUEUE BACK POINTER: 202 IN QUEUE FRONT POINTER: 202 OUT QUEUE BACK POINTER: 206 OUT QUEUE FRONT POINTER: 202

> 6-24 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

### Menu Options by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: MD GUI USER MENU TEXT: MD GUI USER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 59331,44145

> RPC: MD TMDOUTPUT RPC: MD TMDPARAMETER RPC: MD TMDPATIENT RPC: MD TMDPROCEDURE RPC: MD TMDRECORDID

> RPC: MD TMDTRANSACTION RPC: MD TMDUSER

> RPC: MD UTILITIES

> UPPERCASE MENU TEXT: MD GUI USER

> NAME: MD GUI MANAGER MENU TEXT: MD GUI MANAGER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 59385,45622

> RPC: MD TMDOUTPUT RPC: MD TMDPARAMETER RPC: MD TMDPATIENT RPC: MD TMDPROCEDURE RPC: MD TMDRECORDID

> RPC: MD TMDTRANSACTION RPC: MD TMDUSER

> RPC: MD UTILITIES RPC: MD GATEWAY

> UPPERCASE MENU TEXT: MD GUI MANAGER

> 1NAME: MD AUTO CHECK-IN SETUP MENU TEXT: Auto Study Check-In Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is used to populate the XPAR parameters MD USE APPT WITH PROCEDURE, MD CHECK-IN PROCEDURE LIST, MD CLINIC QUICK LIST, and MD

> CLINICS WITH MULT PROC. The four XPAR parameters are used for the auto study check-in. Users can use the option to indicate whether their site use and schedule appointments. They can populate a list of procedures and associated clinics that need a CP study checked-in.

> ROUTINE: EN1^MDWSETUP

> UPPERCASE MENU TEXT: AUTO STUDY CHECK-IN SETUP

> NAME: MD SCHEDULED STUDIES MENU TEXT: Scheduled Studies TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is tasked to run daily. It will process the HL7 messages that need to be sent to the device on a daily basis for CP studies.

> ROUTINE: EN1^MDWORSR SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: SCHEDULED STUDIES

> NAME: MD STUDY CHECK-IN MENU TEXT: Study Check-in TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is tasked to run daily. It checks-in CP studies

> 1 Patch MD\*1.0\*14 March 2008 Options added to support the auto study check-in.

> April 2004 Clinical Procedures V. 1.0 6-25

> Technical Manual and Package Security Guide

> Exported Options

> for procedures that require multiple encounters such as Hemodialysis, Respiratory Therapy, and Sleep Studies.

> ROUTINE: CLINICPT^MDWORSR SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: STUDY CHECK-IN

> 1 NAME: MD HIGH VOLUME PROCEDURE SETUP MENU TEXT: High Volume Procedure Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will populate the XPAR Parameters MD GET HIGH VOLUME and MD NOT ADMN CLOSE MUSE NOTE. It will let the user populate a list of Clinical Procedures procedures set it up for high volume procedure process.

> ROUTINE: EN1^MDARSET

> UPPERCASE MENU TEXT: HIGH VOLUME PROCEDURE SETUP

#### NAME: MD PROC W/INCOMPLETE WORKLOAD

> MENU TEXT: Print list of Procedure with incomplete workload

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option prints a list of procedures that has incomplete workload for the visit.

> ROUTINE: E1^MDSTUDW

> UPPERCASE MENU TEXT: PRINT LIST OF PROCEDURE WITH I

> NAME: MD PROCESS RESULTS MENU TEXT: MD Process Results TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

> DESCRIPTION: This task is ran daily for every hour to process results and update Consults package.

> ENTRY ACTION: N ZTSAVE S ZTSAVE("DUZ")=DUZ,ZTSAVE("DUZ(")=""

> ROUTINE: PROCESS^MDHL7XXX UPPERCASE MENU TEXT: MD PROCESS RESULTS

> 2NAME: MD HEMODIALYSIS USER MENU TEXT: HEMODIALYSIS USER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 60387,39853

> RPC: MDK GET VISTA DATA RPC: MDK GET/SET RENAL DATA RPC: MDK UTILITY

> RPC: VAFCTFU CONVERT DFN TO ICN RPC: VAFCTFU CONVERT ICN TO DFN RPC: MD TMDWIDGET

> RPC: MD TMDNOTE RPC: MD TMDCIDC RPC: MD TMDLEX

> RPC: MD TMDENCOUNTER RPC: GMV MANAGER RPC: MD GATEWAY

> RPC: MD TMDSUBMITU RPC: ORWPT PTINQ RPC: GMV PTSELECT

> RPC: DG SENSITIVE RECORD ACCESS RPC: DG SENSITIVE RECORD BULLETIN RPC: MD TMDRECORDID

> 1 Patch MD\*1.0\*21 June 2010 Options added to support high volume procedures enhancement.

> 2 Patch MD\*1.0\*6 May 2008 Hemodialysis User menu option added.

> 6-26 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> UPPERCASE MENU TEXT: HEMODIALYSIS USER

> NAME: MD STUDIES LIST

> MENU TEXT: Clinical Procedures Studies List

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will generate a list of Clinical Procedures studies.

> ROUTINE: EN2^MDSTUDL

> UPPERCASE MENU TEXT: CLINICAL PROCEDURES STUDIES LI

> 1NAME: MDCVT MANAGER

> MENU TEXT: Medicine to CP Conversion Manager

> TYPE: menu CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This is the Medicine to CP Manager menu option. This menu option consists of options to assist the site in converting the Medicine reports to Clinical Procedures text reports.

> ITEM: MDCVT SETUP SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: MDCVT RUN SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: MDCVT SUMMARY SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: MDCVT DISK SPACE SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: MDCVT LIST OF TIU TITLES SYNONYM: 6 DISPLAY ORDER: 6

> ITEM: MDCVT TOTALS SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: MDCVT ERROR LOG SYNONYM: 8 DISPLAY ORDER: 8

> ITEM: MDCVT CONVERSION LOCKOUT SYNONYM: 9 DISPLAY ORDER: 9

> ITEM: MDCVT BUILD CONVERSION LIST SYNONYM: 2 DISPLAY ORDER: 2

> TIMESTAMP: 60459,53192 TIMESTAMP OF PRIMARY MENU: 59904,24363 UPPERCASE MENU TEXT: MEDICINE TO CP CONVERSION MANA

> NAME: MDCVT SETUP MENU TEXT: Conversion Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES X ACTION PRESENT: YES

> DESCRIPTION: This option will bring up a setup screen for the site to setup the Medicine Report Conversion parameter setup. This parameter setup allows the site to control which Medicine reports will be converted and which CP Definition and TIU title to link to.

> EXIT ACTION: K DDSFILE,DR,DA ROUTINE: SETUP^MDCVT UPPERCASE MENU TEXT: CONVERSION SETUP

> NAME: MDCVT RUN MENU TEXT: Run the Conversion Process TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will start the Medicine Report conversion to

> 1 Patch MD\*1.0\*5 August 2006 Patch 5 menu options added.

> April 2004 Clinical Procedures V. 1.0 6-27

> Technical Manual and Package Security Guide

> Exported Options

> Clinical Procedures. This option will only convert reports for procedures that have the "CONVERT Y/N" field set to "Yes" under the MEDICINE FILE PARAMETERS in the CP CONVERSION file (#703.9).

> ROUTINE: EN^MDCVT

> UPPERCASE MENU TEXT: RUN THE CONVERSION PROCESS

> NAME: MDCVT SUMMARY MENU TEXT: Summary of Conversion Process

> TYPE: print CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will generate a Medicine Report Conversion report. This report consists of a listing of all Medicine records that were processed in the conversion in variable pointer format and the status of the conversion whether the record was converted, skipped, or errored. If the record was converted, the total number of lines and bytes that the record was converted to in a TIU document will be displayed. If the record errored, the reason

> why

> it errored will be displayed. If the record was skipped, the reason why it was skipped will be displayed.

> DIC {DIP}: MDD(703.9, L.: 0

> FLDS: \[MD CONVERSION SUMMARY\] BY: \[MD CONVERSION SUMMARY\] UPPERCASE MENU TEXT: SUMMARY OF CONVERSION PROCESS

> NAME: MDCVT DISK SPACE MENU TEXT: Disk Space Requirements TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will generate a summary of the Medicine report conversion. This summary consists of a list of the files converted to Clinical Procedures, the count of records converted, the total lines and

> Bytes

> the records were converted in each file. ROUTINE: SUMMARY^MDCVT

> UPPERCASE MENU TEXT: DISK SPACE REQUIREMENTS

> NAME: MDCVT LIST OF TIU TITLES MENU TEXT: List of TIU Titles Needed TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will allow the user to generate a list of Medicine procedures and the TIU titles needed to be created for the procedures that will be used for the Medicine report conversion. The PRINT NAME of the procedures in the PROCEDURE/SUBSPECIALTY file (#697.2) will be used in the display. This list will list the procedures and titles for a Medicine

> Package

> Procedure, if the "Convert Y/N" parameter is set to "Yes" and the "Use TIU Note Title" parameter is blank in the Conversion Setup option.

> ROUTINE: DISP^MDSTATU

> UPPERCASE MENU TEXT: LIST OF TIU TITLES NEEDED

> NAME: MDCVT TOTALS MENU TEXT: Conversion Totals By Status TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will verify that the Medicine reports conversion is

> complete and are in appropriate statuses. ROUTINE: TOTALS^MDCVT

> 6-28 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

Exported Options

> UPPERCASE MENU TEXT: CONVERSION TOTALS BY STATUS

> NAME: MDCVT ERROR LOG MENU TEXT: Error Log

> TYPE: print CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option generates a log of all the errors that occurred with each Medicine report during the conversion. The listing consists of the CONVERSION ID and ERROR MESSAGE. The CONVERSION ID consists of the record \# concatenated with a ";" and the global location (e.g.,"345;MCAR(699,").

> DIC {DIP}: MDD(703.9, L.: 0

> FLDS: \[MD CONVERSION ERRORS\] BY: \[MD CONVERSION ERRORS\] UPPERCASE MENU TEXT: ERROR LOG

> NAME: MDCVT CONVERSION LOCKOUT MENU TEXT: Conversion Lockout TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will let the user place a specialty/procedure or ALL specialty/procedures Enter/Edit and Report options 'OUT OF SERVICE' in

> the

> Medicine package. It will also set Kernel site parameter MD MEDICINE CONVERTED to "YES" when all specialties/procedures enter/edit and report options are disabled or when the user indicated that all Medicine reports has been converted.

> ROUTINE: LOCKOUT^MDCVT UPPERCASE MENU TEXT: CONVERSION LOCKOUT

> NAME: MDCVT BUILD CONVERSION LIST MENU TEXT: Build Conversion List TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

> X ACTION PRESENT: YES

> DESCRIPTION: The user will need to run this option before using the \[MDCVT RUN\], Run the Conversion Process, option. This option will let the user

> build

> the conversion list of the Medicine file records for the CP CONVERSION file (#703.9). It will populate the CONVERSION LOG sub-file (#703.92) with all entries in the "AC" cross reference in the MEDICAL PATIENT file (#690) and

> set

> the STATUS field as "Ready to Convert" for each entry. This option can be queued. Once the conversion list is built, this option can also be used to add new additional entries in the Medicine file into the conversion list.

> This option will not overwrite the existing entries in the CONVERSION LOG but add to the list.

> EXIT ACTION: K MDS ENTRY ACTION: S MDS=\$\$BLD^MDCVT1() UPPERCASE MENU TEXT: BUILD CONVERSION LIST

> 1NAME: MD PROCESS NOSHOW/CANCEL

> MENU TEXT: Process No Show/Cancel Studies

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option is tasked to run daily. It will check for any appointment that is No Show or Cancelled for CP studies in the "Pending Instrument Data" status.

> ROUTINE: EN1^MDWCAN

> UPPERCASE MENU TEXT: PROCESS NO SHOW/CANCEL STUDIES

> 1 Patch MD\*1.0\*11 June 2009 Add new exported option.

> April 2004 Clinical Procedures V. 1.0 6-29

> Technical Manual and Package Security Guide

> Exported Options

> 1NAME: MD DEVICE SURVEY TRANSMISSION MENU TEXT: MD Device Survey

> Transmission

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will run the device survey collection routine and capture the data for transmission.

> ROUTINE: COL^MDDEVCL

> UPPERCASE MENU TEXT: MD DEVICE SURVEY TRANSMISSION

> 1 Patch MD\*1.0\*20 November 2010 New option added.

> 6-30 Clinical Procedures V. 1.0 April 2004 Technical Manual and Package Security Guide

### From: MD*1*21 Technical Manual change pages

## Revised June 2010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Department of Veterans Affairs Office of Information & Technology Office of Enterprise Development

> Revision History

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Description</strong></th>
<th><strong>Date</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Originally released.</td>
<td>April 2004</td>
<td></td>
</tr>
<tr class="even">
<td>1Patch MD*1.0*1 released.</td>
<td>July 2004</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patch MD*1.0*2 released.</p>
</blockquote></td>
<td>August 2006</td>
<td></td>
</tr>
<tr class="even">
<td>2Patch MD*1.0*5 released August 2006. Updated File List, Package Default Definition, Parameter Definitions, and menu options.</td>
<td>Documented February 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3Patch MD*1.0*14 released. Updated Routine Descriptions, File List, Parameter Definitions, Protocols, menu options, and Cross References. Deleted bad references to Sample Reports in Ch. 15.</td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>4Patch MD*1.0*6 released. Added</p>
<p>description of Hemodialysis module and 508 Compliance to Introduction; updated Routine Descriptions, File List, Package Default Definition, Remote Procedure Calls, Parameter Definitions, menu options, Cross References, Callable Routines, External Relations, Internal Relations, and Glossary. Removed individual vendor contact information from Ch.15.</p></td>
<td>May 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5Patch MD*1.0*11 released. Updated Routine Description, File and Field Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2009</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6Patch MD*1.0*21 released. Updated Routine Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*1 and MD\*1.0\*2 July 2004 Patch 2 release added.

> 2 Patch MD\*1.0\*5 August 2006 Patch 5 release added.

> 3 Patch MD\*1.0\*14 March 2008 Patch 14 release added.

> 4 Patch MD\*1.0\*6 May 2008 Patch 6 release added.

> 5 Patch MD\*1.0\*11 June 2009 Patch 11 release added.

> 6 Patch MD\*1.0\*21 June 2010 Patch 21 release added.
