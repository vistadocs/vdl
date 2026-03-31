---
consolidated_title: "technical manual"
app_code: MD
doc_type: TM
master_source: "MD*1*23 Technical Manual (CP Flowsheets)"
master_pub_date: April 2004
consolidated_from: 3 versions
prior_versions:
  - "MD*1*12 Technical Manual (CP Flowsheets)"
  - "MD*1*16 Technical Manual (CP Flowsheets)"
---

> ![](md-1-23-technical-manual-cp-flowsheets/001.png)

> CLINICAL PROCEDURES

> Version 1.0

> TECHNICAL MANUAL AND PACKAGE SECURITY GUIDE

> April 2004

> Revised February 2012

> Department of Veterans Affairs Office of Information & Technology Office of Enterprise Development

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
<td>Patch MD*1.0*2 released.</td>
<td>August 2006</td>
<td></td>
</tr>
<tr class="even">
<td><p>2Patch MD*1.0*5 released August 2006.</p>
<p>Updated File List, Package Default Definition, Parameter Definitions, and menu options.</p></td>
<td>Documented February 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>3Patch MD*1.0*14 released. Updated</p>
<p>Routine Descriptions, File List, Parameter Definitions, Protocols, menu options, and Cross References. Deleted bad references to</p>
<p>Sample Reports in Ch. 15.</p></td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>4Patch MD*1.0*6 released. Added</p>
<p>description of Hemodialysis module and 508 Compliance to Introduction; updated Routine Descriptions, File List, Package Default Definition, Remote Procedure Calls, Parameter Definitions, menu options, Cross References, Callable Routines, External Relations, Internal Relations, and Glossary. Removed individual vendor contact</p>
<p>information from Ch.15.</p></td>
<td>May 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>5Patch MD*1.0*11 released. Updated</p>
<p>Routine Description, File and Field Description, Parameter Definition, and Menu Options By Name.</p></td>
<td>March 2009</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>6Patch MD*1.0*21 released. Updated</p>
<p>Routine Description, Parameter Definition, and Menu Options By Name.</p></td>
<td>May 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*1 and MD\*1.0\*2 July 2004 Patch 2 release added.

> 2 Patch MD\*1.0\*5 August 2006 Patch 5 release added.

> 3 Patch MD\*1.0\*14 March 2008 Patch 14 release added.

> 4 Patch MD\*1.0\*6 May 2008 Patch 6 release added.

> 5 Patch MD\*1.0\*11 March 2009 Patch 11 release added.

> 6 Patch MD\*1.0\*21 May 2010 Patch 21 release added.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>1Patch MD*1.0*20 released. Added new Exported Options and Updated the Routine Descriptions. Added new Parameter Definitions.</th>
<th>November 2010</th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>2Patch MD*1.0*16 released. Added 508 compliance statement. Added new and updated Exported Options and Routine Descriptions. Added Dialogs and Security Keys. Updated File Security. Corrected link to the Clinical Flowsheets website. Added new file entries to the existing Package Default Definition list. Updated the Electronic Signatures section. Updated Cross References. Removed Kardex references. Added file and field descriptions. Added terms to the Glossary. Corrected figure captions. Removed two routines from Routine Descriptions section. Added MDCLI01 and MDTERM to Section 9, Callable Routines. Removed terminology dictionaries for Aware and</p>
<p>Spacelabs from Section 15.</p></td>
<td>January 2011</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>3Patch MD*1.0*12 released. Removed</p>
<p>references to VDEF in chapters 5, 10, and 14. Revised 704.005, 09 and 704.005, 1</p>
<p>field names.</p></td>
<td>October 2011</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Editorial Review</td>
<td>January 2012</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*20 November 2010 Patch 20 release added

> 2 Patch MD\*1.0\*16 January 2011 Patch 16 release added

> 3 Patch MD\*1.0\*12 October 2011 Patch 12 release added
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Benefits](#benefits)
  - [Kardex](#kardex)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [Clinical Instrument Interface Specifications](#clinical-instrument-interface-specifications)
- [Routine Descriptions](#routine-descriptions)
- [File List and Related Information](#file-list-and-related-information)
  - [File and Field Descriptions](#file-and-field-descriptions)
    - [CP Transaction File - \#702](#cp-transaction-file-702)
    - [1CPTransactionTIUHistory File - \#702.001](#1cptransactiontiuhistory-file-702001)
    - [CP Definition File - \#702.01](#cp-definition-file-70201)
    - [CP Instrument File - \#702.09](#cp-instrument-file-70209)
    - [CP Result Report File - \#703.1](#cp-result-report-file-7031)
    - [1Hemodialysis Access Points File - \#704.201](#1hemodialysis-access-points-file-704201)
    - [1Hemodialysis Study File - \#704.202](#1hemodialysis-study-file-704202)
    - [1Hemodialysis Setting File - \#704.209](#1hemodialysis-setting-file-704209)
    - [1CPCONSOLEACL File (704.001)](#1cpconsoleacl-file-704001)
    - [1CPHL7LOG File (#704.002)](#1cphl7log-file-704002)
    - [1CPPROTOCOLLOCATION File (#704.006)](#1cpprotocollocation-file-704006)
    - [1TERMUNITCONVERSION File (#704.104)](#1termunitconversion-file-704104)
    - [1OBSVIEW File (#704.111)](#1obsview-file-704111)
    - [1OBSSET File (#704.116)](#1obsset-file-704116)
    - [1OBS File (#704.117)](#1obs-file-704117)
  - [Package Default Definition](#package-default-definition)
- [Exported Options](#exported-options)
  - [Delphi Components](#delphi-components)
  - [Parameter Definitions](#parameter-definitions)
  - [Protocols](#protocols)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [HL Logical Links](#hl-logical-links)
  - [Menu Options by Name](#menu-options-by-name)
  - [1Dialogs](#1dialogs)
    - [Missing Required HL7 Element](#missing-required-hl7-element)
    - [Invalid Key Passed](#invalid-key-passed)
    - [No Record in Patient File for DFN Passed](#no-record-in-patient-file-for-dfn-passed)
    - [Required Segment Missing](#required-segment-missing)
- [Cross-References](#cross-references)
- [Archiving and Purging](#archiving-and-purging)
  - [Cleanup](#cleanup)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [SAC Exemptions](#sac-exemptions)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Security Features](#security-features)
  - [List of Vendor Interfaces](#list-of-vendor-interfaces)
  - [Device Setup Instructions](#device-setup-instructions)
    - [Vendor Contacts:](#vendor-contacts)
    - [Transmission Instructions:](#transmission-instructions)
    - [Costs:](#costs)
    - [Description:](#description)
    - [Description:](#description-1)
    - [Description:](#description-2)
    - [Setup Instructions (B. Braun Device Settings for CP Manager)](#setup-instructions-b-braun-device-settings-for-cp-manager)
    - [Description:](#description-3)
    - [Setup Instructions (Hypercare Device Settings for CP Manager)](#setup-instructions-hypercare-device-settings-for-cp-manager)
    - [Description:](#description-4)
- [Glossary](#glossary)
> 1CP (Clinical Procedures) is a conduit for passing final patient results, using Health Level 7 (HL7) messaging, between vendor clinical information systems (CIS) and Veterans Health Information Systems and Technology Architecture (VistA). The patient’s test result or report is displayed through the Computerized Patient Record System (CPRS). The report data is stored on the Imaging Redundant Array of Inexpensive Disks (RAID) and in some instances, discrete data is stored in the Medicine database.
> CP provides features that can be used across clinical departments such as general medicine, cardiology, pulmonary, women’s health, neurology, and rehabilitation medicine.
> 2Hemodialysis is a new module of the Clinical Procedures (CP) package that provides features specific to hemodialysis treatment. The Hemodialysis module allows you to collect hemodialysis treatment information from the medical device, and manually enter treatment data into the application.
> Pre-dialysis vitals, information obtained during treatment, and post-dialysis vitals can be entered into the Hemodialysis data entry screens. A Treatment Summary is created and used to fill out Centers for Medicare & Medicaid Services (CMS)/End Stage Renal Disease (ESRD) forms.

## Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Standardized and Common User Interface

> Clinicians can go through the same program, CPRS, to enter, review, interpret, and sign CP orders. CP documents in TIU obey Authorization Subscription Utility (ASU) Business Rules. The update users functionality currently used by Consults determines which users are allowed to access or edit CP documents.

2.  Integration

> The ordering process of a CP procedure is initiated by CPRS and processed through the Consult/Request Tracking Package (Consults). The interpretation of the data is entered and displayed through TIU. The final result of the CP procedure is displayed by VistA Imaging. The ordering, viewing, reviewing, interpreting, and signing of the CP medical record is accessed through one location, the Consults tab in CPRS.

3.  Variety of Accepted File Types

> CP is able to accept data/final result report files from automated instruments in .txt, .rtf,

> .jpg, .jpeg, .bmp, .tiff, .pdf, and .html file types. CP allows additional automated instruments and file types to be added to interface with CP in the future.

> 1 Patch MD\*1.0\*16 January 2011 Spelled out CP acronym on first use.

> 2 Patch MD\*1.0\*6 May 2008 Hemodialysis introduction added.

4.  Links to Other Packages

> CP interfaces with packages such as Computerized Patient Record System (CPRS), Consult/Request Tracking Package, Text Integration Utility Package (TIU), and VistA Imaging. New Health Summary components shall be available in the future.

5.  Interface Between CP and Imaging

> Certain images such as consent forms and report objects are acquired, processed, stored, transmitted, and displayed by the VistA Imaging package. This interface will replace existing capture interface between Medicine 2.3 and VistA Imaging.

6.  Inpatient and Outpatient Workloads

> CP Definition file (#702.01) allows for defining the Hospital Location where the procedure is performed. This determines which Encounter Form is presented to the end user. CPRS and TIU parameters allow for the configuration of TIU software to prompt users to enter workload data which is then passed to the Patient Care Encounter software (PCE) for both inpatients and outpatients.

> <span id="_bookmark2" class="anchor"></span>1508 Compliance

> 2The Department of Veterans Affairs, Office of Enterprise Development (OED), and New Editions have completed the Section 508 compliance testing of MD\*1.0\*16.

- CPFlowsheets (MD\*1.0\*16) is assigned a Section 508 status of compliant.
- CPConsole Manager (MD\*1.0\*16) is assigned a Section 508 status of compliant.

> Note: The following notice applies only to Patch MD\*1.0\*6.

> The Clinical Procedures Hemodialysis Software is exempt from coverage under the Section 508 standards. The definition of "electronic and information technology" in the Section 508 standards specifically excludes "medical equipment where information technology is integral to its operation." 36 C.F.R. Section 1194.4. VHA's use of the Clinical Procedures Hemodialysis Software also does not violate Section 508 because it will not affect access to the data or information provided by that software. 29 U.S.C. Section 794d(a). The data or information collected by the software is immediately made available through the CPRS system, which is accessible to people with disabilities.

> 1 Patch MD\*1.0\*6 May 2008 508 Compliance notice added.

> 2 Patch MD\*1.0\*16 January 2011 Added 508 compliance statement.

Introduction

> <span id="_bookmark3" class="anchor"></span>1Clinical Flowsheets Patch

> The Clinical Flowsheets patch provides an interface to collect patient information from Intensive Care Unit (ICU) monitoring devices, and the subsequent entry and storage of the data in VistA. A large and varied set of patient data is generated in the ICU setting, and it is a challenge for Department of Veterans Affairs (VA) medical providers to easily and consistently collect and analyze patient data without standardization.

> The Clinical Flowsheets patch provides the ICU connectivity that makes the required data available to the Clinical Reminders Index. This functionality is provided by the Clinical Observation database (CliO) Service. The application provides user-friendly, customizable, graphical user interfaces (GUI) with flowsheets to view, edit, and enter patient ICU Vitals, Renal Dialysis, and Intake & Output (I&O). Vendor products include monitors and other instruments, as well as CIS.

> The Clinical Flowsheets patch (MD\*1.0\*16) distributes HL7 links designed to receive clinical observations from ICU monitors and other clinical systems that meet the published CP ORU Conformance Profile. The patch also allows users to enter data manually collected from monitors that cannot electronically send the information. The incoming vendor data is made available concurrently with the manually entered information in the Clinical Flowsheets patch.

> The Clinical Flowsheets patch consists of three executables through which the ICU and VistA communicate: CP Gateway, CP Console, and CP Flowsheets.

- The CP Gateway system allows third party vendor devices to send observational data to a VistA CP system for display and reporting. HL7 messaging is the broadcaster (generator) of the text passed between the devices and VistA. For more information about the CP Gateway, refer to the *Clinical Flowsheets Installation Guide*.
- The CP Console application provides the tools to build the flowsheets that you use in the ICU for patient care, recording vital statistics as necessary. For more information on the CP Console application, refer to *Clinical Procedures (CP) Console Implementation Guide*.
- The CP Flowsheets patch provides CIS functions, such as data entry and validation, patient management, and system administration. For more information on the CP Flowsheets application, refer to *Clinical Procedures V.1.0 CP Flowsheets User Manual*.

## Kardex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Kardex functionality was removed from this application version and will be included in a future release. Some back-end Kardex files remain in place and will not adversely affect application functionality.

> 1 Patch MD\*1.0\*16 January 2011 Added information about the Clinical Flowsheets package. Added Kardex section.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For implementation and maintenance issues, refer to “Chapter 1 – Introduction” of the *Clinical Procedures Implementation Guide*. For implementation and maintenance of Clinical Flowsheets, refer to the *Clinical Procedures (CP) Console Implementation Guide*.<sup>1</sup>

> 1 Patch MD\*1.0\*16 January 2011 Added document reference.

# Clinical Instrument Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to Chapter 10 of the Clinical Procedures Implementation Guide for information on Setting up HL7 Parameters.

> 1Refer to the Clinical Instrument Bi-Directional Interface Specifications document for information on Clinical Procedures instrument interface specifications. Directions for locating the document follow:

1.  Access the Clinical Procedures website: [<u>http://vista.med.va.gov/clinicalspecialties/clinproc/</u>](http://vista.med.va.gov/clinicalspecialties/clinproc/)
2.  On the navigation bar found on the left-hand side of the page, hover your mouse pointer over Clinical Procedures Project, then click Documentation.
3.  Click Clinical Procedures Documents.
4.  2Click the Clinical Procedures Bi-Directional Communication Specification link to view the document or save a copy.

> Click the Clinical Procedures Bi-Directional Communication Specification link to view the document or save a copy.

> 1 Patch MD\*1.0\*14 March 2008 Outdated link removed and replaced with directions to document.

> 2 Patch MD\*1.0\*16 January 2011 Added step number to fourth step.

# Routine Descriptions

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

> 1 Patch MD\*1.0\*20 November 2010 Update routine list with new routines and patch history changes.

> MDKUTLR ; HOIFO/DP - Renal Utilities RPC;11/29/07 14:45

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

Routine Descriptions

> MDRPCOT2 ; HOIFO/NCA - Object RPCs (TMDTransaction) Continued 2;10/29/04 12: 20 ;3/12/08 09:18

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

# File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File and Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CP Transaction File - \#702

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file contains the studies between the instruments and user generated data as it is matched to a consult order and a TIU document is created for the results. It also manages the interface between the images and the Imaging RAID.

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
<td>Patient</td>
<td>702,.01</td>
<td><p>Pointer to Patient</p>
<p>(#2) file</p></td>
<td>This field contains a pointer to the Patient (#2) file for this study.</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>702,.011</td>
<td>Computed</td>
<td><p>This field contains the computed value of the patient’s SSN from</p>
<p>the Patient (#2) file.</p></td>
</tr>
<tr class="odd">
<td>DOB</td>
<td>702,.012</td>
<td>Computed</td>
<td><p>This field contains the computed value of the patient’s date of birth</p>
<p>from the Patient (#2) file.</p></td>
</tr>
<tr class="even">
<td>Created Date/Time</td>
<td>702,.02</td>
<td>Date</td>
<td><p>This field contains the date/time the study was created within the</p>
<p>CP User executable.</p></td>
</tr>
<tr class="odd">
<td>Created By</td>
<td>702,.03</td>
<td><p>Pointer to New</p>
<p>Person (#200) file</p></td>
<td><p>This field contains the DUZ of the</p>
<p>user that created this study.</p></td>
</tr>
<tr class="even">
<td>CP Definition</td>
<td>702,.04</td>
<td>Pointer to CP Definition (#702.01) file</td>
<td><p>This field contains a pointer to the CP Definition (#702.01) file of the procedure definition that this</p>
<p>study represents.</p></td>
</tr>
<tr class="odd">
<td>Consult Number</td>
<td>702,.05</td>
<td>Free Text 1-20 characters in length</td>
<td><p>This field contains an IEN of the Consult (#123) file representing the Consult order that is matched</p>
<p>up to this study.</p></td>
</tr>
</tbody>
</table>

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
<td>TIU Note</td>
<td>702,.06</td>
<td>Pointer to TIU Document (#8925) file</td>
<td><p>This field contains a pointer to the TIU Document (#8925) file representing the note that contains the interpretation of this study as well as the links to the associated</p>
<p>images.</p></td>
</tr>
<tr class="even">
<td>Vstring</td>
<td>702,.07</td>
<td>Free Text 1-50 characters in length</td>
<td><p>1This field contains the vstring.</p>
<p>The vstring is in the following format: Visit Type_”;”_Visit Date/Time_”;”_Hospital Location (internal entry number of the</p>
<p>visit).</p></td>
</tr>
<tr class="odd">
<td>Transaction Message</td>
<td>702,.08</td>
<td>Free Text 1-80 characters in length</td>
<td><p>Contains the message returned</p>
<p>from the VistA Imaging API‟s for storing the images on the server.</p></td>
</tr>
<tr class="even">
<td>Transaction Status</td>
<td>702,.09</td>
<td><p>Set:</p>
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
<td>702.091,.02</td>
<td>Date</td>
<td><p>Date and time this error message</p>
<p>was generated.</p></td>
</tr>
<tr class="odd">
<td>Received From</td>
<td>702.091,.03</td>
<td><p>Free Text 1-30</p>
<p>characters in length</p></td>
<td>Where the error was generated.</td>
</tr>
<tr class="even">
<td>Message</td>
<td>702.091,.09</td>
<td><p>Free Text 1-150</p>
<p>characters in length</p></td>
<td>Text of the error message.</td>
</tr>
<tr class="odd">
<td>Image (multiple)</td>
<td>702.1,.01</td>
<td><p>Number between 1-</p>
<p>999, 0 decimal digits</p></td>
<td>Index of attached image for this study.</td>
</tr>
<tr class="even">
<td>Type</td>
<td>702.1,.02</td>
<td><p>Set:</p>
<p>I - Instrument data U - User supplied file</p></td>
<td>Type of attachment to be processed.</td>
</tr>
<tr class="odd">
<td>Result Report</td>
<td>702.1,.03</td>
<td><p>Pointer to CP Result Report</p>
<p>(#703.1) file</p></td>
<td><p>Pointer to the CP Result Report (#703.1) file containing the</p>
<p>attachment from the instrument.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Erroneous words removed from description.

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
<td>Status</td>
<td>702.1,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Submitted to server</p></li>
<li><p>- Error in submission</p></li>
<li><p>- Error in filing</p></li>
<li><p>- Copied to server</p></li>
</ol></td>
<td>Status of this image.</td>
</tr>
<tr class="even">
<td>UNC</td>
<td>702.1,.1</td>
<td>Free Text 1-245 characters in length</td>
<td><p>Contains the Universal naming</p>
<p>Convention (UNC) for this attachment.</p></td>
</tr>
<tr class="odd">
<td>Submitted to Instrument</td>
<td>702,.11</td>
<td><p>Pointer to CP</p>
<p>Instrument (#702.09) file</p></td>
<td><p>Points to the instrument definition</p>
<p>that this study was submitted to at the time of check-in.</p></td>
</tr>
<tr class="even">
<td>Instrument Order Number</td>
<td>702,.12</td>
<td>Free Text 1-22 characters in length</td>
<td><p>Contains the unique order number for this study that is sent to the bi-</p>
<p>directional instrument.</p></td>
</tr>
<tr class="odd">
<td>1Visit</td>
<td>702,.13</td>
<td><p>Pointer to Visit</p>
<p>(#9000010) file</p></td>
<td><p>This is the Visit number returned</p>
<p>from PCE. Reference IA# 1902.</p></td>
</tr>
<tr class="even">
<td><p>2Scheduled</p>
<p>Date/Time</p></td>
<td>702,.14</td>
<td>Date</td>
<td><p>This field contains the date/time when the HL7 message should be sent by CP to the device for this CP</p>
<p>transaction.</p></td>
</tr>
<tr class="odd">
<td>3Conversion ID Reference</td>
<td>702,.3</td>
<td>Free text 1-30 characters in length.</td>
<td><p>This field is the Reference Conversion ID. It is a variable Pointer to the Medicine files. It indicates which converted Medicine</p>
<p>report record is associated with the CP Transaction study. This field helps to keep track which CP Transaction study was created for</p>
<p>the Medicine report conversion.</p></td>
</tr>
<tr class="even">
<td>Image Count</td>
<td>702,.991</td>
<td>Computed</td>
<td><p>Computed field to return the</p>
<p>number of images associated with this study.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 Field added to support the storing of the Clinical Indicator questions, CPT and ICD9 codes in the CP Transaction file.

> 2 Patch MD\*1.0\*14 March 2008 Field added to support the auto study check-in with scheduled appointment

> date/time.

> 3 Patch MD\*1.0\*5 August 2006 Field added.

### 1CP_Transaction_TIU_History File - \#702.001

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This CP Transaction TIU History file stores all TIU notes that is associated with the CP Transaction study. This will keep track of multiple notes associated with one CP study.

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
<td>Study_ID</td>
<td>702.001,.01</td>
<td><p>Pointer To CP Transaction File</p>
<p>(#702)</p></td>
<td>This field contains a pointer to the CP Transaction file (#702).</td>
</tr>
<tr class="even">
<td>TIU_Note_ID</td>
<td>702.001,.02</td>
<td>Pointer To TIU Document File (#8925)</td>
<td><p>This field contains a pointer to the TIU Document file (#8925) representing the note that contains the interpretation of this CP Transaction. (Reference IA</p>
<p>#3376)</p></td>
</tr>
<tr class="odd">
<td>Date_Assigned</td>
<td>702.001,.03</td>
<td>Date</td>
<td><p>This field contains the date/time when the TIU note was assigned</p>
<p>to this transaction.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 702.001 added.

### CP Definition File - \#702.01

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file defines all the procedures used by the Clinical Procedures package. All elements that define a procedure are in this file. This file is exported with data, but entries may be added by the site.

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
<td>Name</td>
<td>702.01,.01</td>
<td>Free Text 3-30 characters in length</td>
<td><p>This field contains the name of the procedure. It should be descriptive of the procedure and contain 3-30 alphanumeric characters. The first character MUST be a letter. To maintain consistency it is recommended that all procedures be entered in</p>
<p>UPPERCASE letters as well.</p></td>
</tr>
<tr class="even">
<td>Treating Specialty</td>
<td>702.01,.02</td>
<td><p>Pointer to Facility</p>
<p>Treating Specialty (#45.7) file</p></td>
<td>This field defines the specialty that this procedure falls under.</td>
</tr>
<tr class="odd">
<td>Require External Data</td>
<td>702.01,.03</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>Setting this field to Yes will force a consult for this procedure to be processed via the CP User executable for matching whether or not there are instruments</p>
<p>associated with it.</p></td>
</tr>
<tr class="even">
<td>Default TIU Note</td>
<td>702.01,.04</td>
<td><p>Pointer to TIU Document Definition</p>
<p>(#8925.1) file</p></td>
<td><p>This field contains a TIU Note Title to use as the default when CP creates a note for</p>
<p>interpretation for this procedure.</p></td>
</tr>
<tr class="odd">
<td>Hospital Location</td>
<td>702.01,.05</td>
<td>Pointer to Hospital Location (#44) file</td>
<td><p>This is the location that will be used when creating the TIU Note</p>
<p>for interpretation.</p></td>
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
<td><p>This field is used to indicate if this is a Hemodialysis procedure or not. The field is a set of codes, 1=DEFAULT so it will be processed by Clinical Procedures or 2=HEMODIALYSIS and the procedure will be processed by</p>
<p>the Hemodialysis application.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 Field added to the CP Definition file.

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
<td>Auto Submit</td>
<td>702.01,.07</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>This field only applies to bi- directional instruments. It is used to indicate whether or not the image attachment should be automatically submitted to VistA Imaging once the procedure is performed and the result is passed</p>
<p>to CP.</p></td>
</tr>
<tr class="even">
<td>External Data Directory</td>
<td>702.01,.08</td>
<td>Free Text 3-150 characters in length</td>
<td><p>This field contains a reference to a network share where user supplied attachments are located</p>
<p>for this procedure.</p></td>
</tr>
<tr class="odd">
<td>Active</td>
<td>702.01,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>Yes/No to indicate active</p>
<p>procedures that can be linked to Consults.</p></td>
</tr>
<tr class="even">
<td>Instrument (multiple)</td>
<td>702.011,.01</td>
<td><p>Pointer to CP Instrument</p>
<p>(#702.09) file</p></td>
<td><p>Contains a pointer to an instrument that generates results</p>
<p>for this procedure.</p></td>
</tr>
<tr class="odd">
<td>1High Volume</td>
<td>702.01,.11</td>
<td><p>Set:</p>
<ol type="1">
<li><p>FOR No;</p></li>
<li><p>FOR Yes</p></li>
</ol></td>
<td><p>This field is used as a flag</p>
<p>indicator to specify if this procedure is high volume or not.</p></td>
</tr>
<tr class="even">
<td>2Processed Result</td>
<td>702.01,.12</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Final Result</p></li>
<li><p>- Multiple Results 2 – Cumulative Result</p></li>
</ol></td>
<td><p>This field is a flag which indicates whether a final result, multiple results, or cumulative</p>
<p>result is associated with this</p>
<p>procedure.</p></td>
</tr>
<tr class="odd">
<td>ID</td>
<td>702.01,.13</td>
<td>Free Text (Required) (Key field)</td>
<td><p>This is a Globally Unique IDentifier (GUID) for this procedure. This is maintained nationally so it is the same throughout the enterprise. A sample ID could be "{69DBD11E-9A8C-4ECE-</p>
<p>AFA4-73947218807D}".</p></td>
</tr>
<tr class="even">
<td>DESCRIPTION</td>
<td>702.01,.9</td>
<td>Free Text</td>
<td><p>This is a detailed DESCRIPTION of this procedure. A sample DESCRIPTION could be "ABD</p>
<p>Paracentisis follow-up".</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Field descriptions added.

> 2 Patch MD\*1.0\*11 June 2009 New field added.

### CP Instrument File - \#702.09

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file contains the list of instruments used by the Clinical Procedures package. This file is exported with data.

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
<td>Name</td>
<td>702.09,.01</td>
<td>Free Text 3-30 characters in length</td>
<td><p>Name or mnemonic of instrument. Used by vendor in HL7 message</p>
<p>header.</p></td>
</tr>
<tr class="even">
<td>Notification Mailgroup</td>
<td>702.09,.02</td>
<td>Pointer to Mail Group (#3.8) file</td>
<td><p>Mail group that will receive error messages and other notifications dealing with this device from the</p>
<p>interface routines.</p></td>
</tr>
<tr class="odd">
<td>Description</td>
<td>702.09,.03</td>
<td>Free Text 1-50 characters in length</td>
<td><p>This field contains a short informational description for the</p>
<p>instrument.</p></td>
</tr>
<tr class="even">
<td>Delete when Submitted</td>
<td>702.09,.05</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>Select Yes if you want files created by this instrument deleted once they are successfully copied to the VistA Imaging RAID. Deletion will be performed by the</p>
<p>VistA Imaging application.</p></td>
</tr>
<tr class="odd">
<td>Printable Name</td>
<td>702.09,.06</td>
<td><p>Free Text 3-30</p>
<p>characters in length</p></td>
<td><p>Name of instrument that is printed</p>
<p>on the reports, etc.</p></td>
</tr>
<tr class="even">
<td>Default File Ext</td>
<td>702.09,.07</td>
<td><p>Free Text (e.g.,</p>
<p>.txt)</p></td>
<td><p>Default file extension for vendor instrument reports (e.g., .doc,</p>
<p>.pdf).</p></td>
</tr>
<tr class="odd">
<td>Serial Number</td>
<td>702.09,.08</td>
<td><p>Free Text 1-50</p>
<p>characters in length</p></td>
<td><p>Vendor serial number of the</p>
<p>instrument (for reference only).</p></td>
</tr>
<tr class="even">
<td>Active</td>
<td>702.09,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Whether or not the instrument is active on the network.</td>
</tr>
<tr class="odd">
<td>1ID</td>
<td>702.09,.1</td>
<td>Free Text (Required) (Key field)</td>
<td><p>This is a Globally Unique IDentifier (GUID) for this instrument. This is maintained nationally so it is the same throughout the enterprise. A sample ID could be "{69DBD11E-9A8C-4ECE-</p>
<p>AFA4-73947218807D}".</p></td>
</tr>
<tr class="even">
<td>Processing Routine</td>
<td>702.09,.11</td>
<td><p>Free Text 1-8</p>
<p>characters in length</p></td>
<td><p>MUMPS routine used to process</p>
<p>interface information.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Field description added.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 37%" />
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
<td>Processing Code</td>
<td>702.09,.12</td>
<td><p>Set:</p>
<p>M - Medicine C - CP V. 1.0</p>
<p>B - Both</p></td>
<td><p>Where data is to be processed: M - Medicine</p>
<p>C - Clinical Procedures</p>
<p>B - Both</p></td>
</tr>
<tr class="even">
<td>Bi-directional</td>
<td>702.09,.13</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>This field indicates whether or not this device can accept HL7</p>
<p>messages from VistA.</p></td>
</tr>
<tr class="odd">
<td>IP Address</td>
<td>702.09,.14</td>
<td><p>Free Text 7-15</p>
<p>characters in length</p></td>
<td><p>This field contains the IP address of</p>
<p>this instrument.</p></td>
</tr>
<tr class="even">
<td>Port</td>
<td>702.09,.15</td>
<td><p>Number between 1000-99999, 0</p>
<p>decimal digits</p></td>
<td>This field contains the port number for this instrument.</td>
</tr>
<tr class="odd">
<td>HL7 Instrument ID</td>
<td>702.09,.16</td>
<td>Free Text 3-30 characters in length</td>
<td><p>This is the name of the actual device where the device name can</p>
<p>be „”SMC St Louis”.</p></td>
</tr>
<tr class="even">
<td>HL7 Universal Service ID</td>
<td>702.09,.17</td>
<td>Free Text 1-48 characters in length</td>
<td><p>This field defines what type of procedure the device can perform if the device can perform multiple</p>
<p>types of procedures.</p></td>
</tr>
<tr class="odd">
<td>HL7 Logical Link</td>
<td>702.09,.18</td>
<td><p>Pointer to the HL Logical Link (#870)</p>
<p>file</p></td>
<td>This field contains the HL7 logical link.</td>
</tr>
<tr class="even">
<td>Server Name</td>
<td>702.09,.21</td>
<td><p>Free Text 1-30</p>
<p>characters in length</p></td>
<td><p>Network name of instrument server</p>
<p>where the report is stored.</p></td>
</tr>
<tr class="odd">
<td>Server Share</td>
<td>702.09,.22</td>
<td><p>Free Text 1-30</p>
<p>characters in length</p></td>
<td><p>Share folder/drive of the instrument</p>
<p>server where the report is stored.</p></td>
</tr>
<tr class="even">
<td>Server Path</td>
<td>702.09,.23</td>
<td><p>Free Text 1-150</p>
<p>characters in length</p></td>
<td><p>Path on the network where the</p>
<p>report is stored.</p></td>
</tr>
<tr class="odd">
<td>Server Executable</td>
<td>702.09,.24</td>
<td>Free Text 1-30 characters in length</td>
<td><p>Name of server program that is run</p>
<p>to create the report for the interface.</p></td>
</tr>
<tr class="even">
<td>Process UNC</td>
<td>702.09,.301</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces UNC type data.</td>
</tr>
<tr class="odd">
<td>Process Text</td>
<td>702.09,.302</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces text type data.</td>
</tr>
<tr class="even">
<td>Process URL</td>
<td>702.09,.303</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces URL type data.</td>
</tr>
<tr class="odd">
<td>Process DLL</td>
<td>702.09,.304</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces DLL type data.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 37%" />
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
<td>Process UUEncode</td>
<td>702.09,.305</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces UUEncode type data.</td>
</tr>
<tr class="even">
<td>Process XML</td>
<td>702.09,.306</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces XML type data.</td>
</tr>
<tr class="odd">
<td>Process XMS</td>
<td>702.09,.307</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td>Enter Yes if this instrument produces XMS type data.</td>
</tr>
</tbody>
</table>

### CP Result Report File - \#703.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file contains the information for the results uploaded from the medical instruments used by Clinical Procedures. It is distributed without any data. All fields are automatically stuffed by Clinical Procedures. There is no user input.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 23%" />
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
<td>Upload ID</td>
<td>703.1,.01</td>
<td><p>Free Text 1-30</p>
<p>characters in length</p></td>
<td><p>Unique identifier assigned for</p>
<p>each upload.</p></td>
</tr>
<tr class="even">
<td>Patient</td>
<td>703.1,.02</td>
<td>Pointer to Patient (#2) file</td>
<td><p>Pointer to the Patient (#2) file of</p>
<p>the patient uploaded from the result of the instrument.</p></td>
</tr>
<tr class="odd">
<td><p>Date/Time</p>
<p>Performed</p></td>
<td>703.1,.03</td>
<td>Date</td>
<td><p>Date/time the procedure was</p>
<p>performed on the instrument.</p></td>
</tr>
<tr class="even">
<td>Instrument</td>
<td>703.1,.04</td>
<td><p>Pointer to CP Instrument</p>
<p>(#702.09) file</p></td>
<td><p>Pointer to the CP Instrument (#702.09) file of the instrument</p>
<p>that produced these reports.</p></td>
</tr>
<tr class="odd">
<td>Study Reference Number</td>
<td>703.1,.05</td>
<td><p>Pointer to CP Transaction file</p>
<p>(#702)</p></td>
<td>This field is used as a reference to the transaction.</td>
</tr>
<tr class="even">
<td>HL7 Reference Number</td>
<td>703.1,.06</td>
<td>Free Text 1-30 characters in length</td>
<td><p>This field is used to keep the IEN of the HL7 message. It serves as a reference to the message that will be purged once the data has been successfully moved to the</p>
<p>VistA Imaging server.</p></td>
</tr>
<tr class="odd">
<td>Status</td>
<td>703.1,.09</td>
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
<td>703.11,.02</td>
<td>Free Text 1-240 characters in length</td>
<td><p>This field contains the Universal Naming Convention (UNC) for this attachment. This indicates</p>
<p>where the attachment is located.</p></td>
</tr>
</tbody>
</table>

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
<td>Item Value</td>
<td>703.11,.1</td>
<td><p>Free Text 1-245</p>
<p>characters in length</p></td>
<td><p>If the uploaded item is a single</p>
<p>string value, it is stored here.</p></td>
</tr>
<tr class="even">
<td>Item Text</td>
<td>703.11,.2</td>
<td>Word-Processing</td>
<td><p>If the uploaded data is multi-lined,</p>
<p>it is stored here.</p></td>
</tr>
</tbody>
</table>

> <span id="_bookmark15" class="anchor"></span>1CP Conversion File- \#703.9

> This file is used for storing the site parameters needed and used to convert Medicine reports to CP Text reports. This file also stores the status of the conversion process for each converted Medicine report.

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
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>703.9,.01</td>
<td>Free Text (Required)</td>
<td><p>This field contains the name of the CP conversion. It is only accessible by the CP conversion routine. It is exported</p>
<p>with one "DEFAULT" entry.</p></td>
</tr>
<tr class="even">
<td>Mode</td>
<td>703.9,.02</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- test</p></li>
<li><p>- real</p></li>
</ol></td>
<td>This field indicates if the CP conversion is in test or real mode.</td>
</tr>
<tr class="odd">
<td>Administrative Closure User</td>
<td>703.9,.03</td>
<td>Pointer to new person file (#200)</td>
<td><p>This field points to the New Person file (#200). It is used to indicate the Administrative Closure person used to close the TIU documents for the CP</p>
<p>conversion.</p></td>
</tr>
<tr class="even">
<td>Scratch HFS Directory</td>
<td>703.9,.1</td>
<td>Free Text</td>
<td><p>This field stores the scratch HFS directory used for the CP conversion. CP conversion program will use this</p>
<p>directory to convert Medicine reports.</p></td>
</tr>
<tr class="odd">
<td><p>Medicine File Parameters</p>
<p><strong>2</strong>(multiple)</p></td>
<td><p>703.91,.0</p>
<p>1</p></td>
<td>Pointer to File file (#1)</td>
<td><p>This field points to the File file (#1). It is used to store the Medicine file number that this parameter is pertaining to.</p>
<p>(Reference IA #4507)</p></td>
</tr>
<tr class="even">
<td>CP Definition</td>
<td><p>703.91,.0</p>
<p>2</p></td>
<td>Point to CP Definition File (#702.01)</td>
<td><p>This field contains the CP Definition to</p>
<p>which the Medicine Report will be mapped.</p></td>
</tr>
<tr class="odd">
<td>Convert Y/N</td>
<td><p>703.91,.0</p>
<p>3</p></td>
<td><p>Set:</p>
<p>0 - No 1 - Yes</p></td>
<td><p>This field is used as a flag to mark the Medicine Report. Enter 0 for 'to not</p>
<p>convert' or 1 for 'to convert'.</p></td>
</tr>
<tr class="even">
<td>Convert if No Status</td>
<td><p>703.91,.0</p>
<p>4</p></td>
<td><p>Set:</p>
<ol type="1">
<li><p>- No</p></li>
<li><p>- Yes</p></li>
</ol></td>
<td><p>This field is used as a flag to indicate whether the Medicine report should be converted or not be converted, if there is no status for the report. The field is 0</p>
<p>for 'not to convert' or 1 for 'to convert'.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*5 August 2006 CP Conversion File \#703.9 added.

> 2 Patch MD\*1.0\*16 January 2011 Added “(multiple)” to Field Name.

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
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Use TIU Note Title</td>
<td><p>703.91,.0</p>
<p>5</p></td>
<td>Pointer to TIU Document Definition File (#8925.1)</td>
<td><p>This field stores the Historical TIU note title used for the conversion of the Medicine reports to CP reports.</p>
<p>(Reference IA #3377 and 3568)</p></td>
</tr>
<tr class="even">
<td><p>Conversion ID</p>
<p><strong>1</strong>(multiple)</p></td>
<td><p>703.92,.0</p>
<p>1</p></td>
<td>Free Text</td>
<td><p>This field is the Conversion ID. It is a variable pointer to the Medicine files. This field will store an entry for each Medicine file record converted. This field is a variable pointer to the following files:</p>
<ol start="691" type="1">
<li><p>ECHO</p>
<ol type="1">
<li><p>CARDIAC CATHETERIZATION</p></li>
</ol>
<ol start="5" type="1">
<li><p>ELECTROCARDIOGRAM (EKG)</p></li>
<li><blockquote>
<p>HOLTER</p>
</blockquote></li>
<li><p>EXERCISE TOLERANCE TEST</p></li>
<li><p>ELECTROPHYSIOLOGY (EP) 694 HEMATOLOGY</p></li>
</ol></li>
</ol>
<p>694.5 CARDIAC SURGERY RISK ASSESSMENT</p>
<ol start="698" type="1">
<li><p>GENERATOR IMPLANT</p>
<ol type="1">
<li><p>V LEAD IMPLANT</p></li>
<li><p>A LEAD IMPLANT</p></li>
<li><p>PACEMAKER SURVEILLANCE</p></li>
</ol></li>
</ol>
<p>699 ENDOSCOPY/CONSULT</p>
<p>699.5 GENERALIZED PROCEDURE/CONSULT</p>
<p>700 PULMONARY FUNCTION TESTS</p>
<p>701 RHEUMATOLOGY</p></td>
</tr>
<tr class="odd">
<td>Status</td>
<td><p>703.92,.0</p>
<p>2</p></td>
<td><p>Set:</p>
<p>CR - Converted Real Mode</p>
<p>CT - Converted Test Mode</p>
<p>E – Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p></td>
<td><p>This is the status field of the conversion log. There are five set of codes:</p>
<p>CR - Converted Real Mode CT - Converted Test Mode E - Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Added “(multiple)” to Field Name.

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
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>New TIU Document IEN</td>
<td><p>703.92,.0</p>
<p>3</p></td>
<td>Free Text</td>
<td><p>This field contains a pointer to the TIU Document file (#8925). (Reference IA #4796). This will hold the internal entry number of the document of the</p>
<p>converted medicine report.</p></td>
</tr>
<tr class="even">
<td>Lines</td>
<td><p>703.92,.0</p>
<p>4</p></td>
<td>Number</td>
<td><p>This field contains the line count of the</p>
<p>Medicine report that was converted.</p></td>
</tr>
<tr class="odd">
<td>Bytes</td>
<td><p>703.92,.0</p>
<p>5</p></td>
<td>Number</td>
<td><p>This field contains the number of bytes of the Medicine report that was</p>
<p>converted.</p></td>
</tr>
<tr class="even">
<td>Error Msg</td>
<td>703.92,.1</td>
<td>Free Text</td>
<td><p>This field stores the error message during the conversion of the Medicine</p>
<p>report.</p></td>
</tr>
</tbody>
</table>

### 1Hemodialysis Access Points File - \#704.201

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on access points used by the Hemodialysis application.

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
<td>Patient_ID</td>
<td>704.201,.01</td>
<td><p>Pointer to patient</p>
<p>file (#2)</p></td>
<td><p>This field contains the patient</p>
<p>DFN. (Required)</p></td>
</tr>
<tr class="even">
<td>Access Points</td>
<td>704.201,.1</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s access points for dialysis</p>
<p>treatments.</p></td>
</tr>
<tr class="odd">
<td>Access History</td>
<td>704.201,.2</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s access history for dialysis</p>
<p>treatments.</p></td>
</tr>
<tr class="even">
<td>Infection History</td>
<td>704.201,.3</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s infection history for</p>
<p>dialysis treatments.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.201 added.

### 1Hemodialysis Study File - \#704.202

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on hemodialysis studies used by the Hemodialysis application.

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
<td>ID</td>
<td>704.202,.01</td>
<td><p>Pointer to CP</p>
<p>Transaction file (#702)</p></td>
<td><p>This field contains the IEN of the</p>
<p>CP STUDY (File #702) for this dialysis treatment. (Required)</p></td>
</tr>
<tr class="even">
<td>Patient</td>
<td>704.202,.02</td>
<td>Pointer to Patient file (#2)</td>
<td><p>Pointer to the PATIENT (File #2)</p>
<p>of the patient for this dialysis treatment.</p></td>
</tr>
<tr class="odd">
<td>Study_DateTime</td>
<td>704.202,.03</td>
<td>Computed date</td>
<td><p>Computed field used to allow</p>
<p>automated XML creation with appropriate tag/value pairs.</p></td>
</tr>
<tr class="even">
<td>Study_Location</td>
<td>704.202,.04</td>
<td>Computed</td>
<td><p>Computed field used to allow</p>
<p>automated XML creation with appropriate tag/value pairs.</p></td>
</tr>
<tr class="odd">
<td><strong>2</strong>User</td>
<td>704.202,.05</td>
<td><p>0;3 Pointer to NEW PERSON FILE</p>
<p>(#200)</p></td>
<td>This field contains the user who accessed the Hemodialysis study.</td>
</tr>
<tr class="even">
<td>Date/Time Accessed</td>
<td>704.202,.06</td>
<td>0;4 Date</td>
<td><p>This field displays the date/time</p>
<p>when the hemodialysis study was accessed by the user.</p></td>
</tr>
<tr class="odd">
<td>Workstation</td>
<td>704.202,.07</td>
<td>0;5 Free text</td>
<td><p>This field contains the workstation that was used by the user to</p>
<p>access the hemodialysis study.</p></td>
</tr>
<tr class="even">
<td>Status</td>
<td>704.202,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Closed</p></li>
<li><p>- Active</p></li>
</ol></td>
<td>Contains the status of this procedure.</td>
</tr>
<tr class="odd">
<td>Study Data</td>
<td>704.202,.1</td>
<td>Word Processing</td>
<td><p>Contains the study data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Summary</td>
<td>704.202,.2</td>
<td>Word Processing</td>
<td><p>Contains the summary data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="odd">
<td>Flowsheet</td>
<td>704.202,.3</td>
<td>Word Processing</td>
<td><p>Contains the flowsheet data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Med Log</td>
<td>704.202,.4</td>
<td>Word Processing</td>
<td><p>Contains the med log data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="odd">
<td>Note List</td>
<td>704.202,.5</td>
<td>Word Processing</td>
<td><p>This field contains the Note List</p>
<p>data XML document in UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Event Log</td>
<td>704.202,.6</td>
<td>Word Processing</td>
<td><p>This field contains the Event Log data XML document in</p>
<p>UUEncoded format.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.202 added.

> 2 Patch MD\*1.0\*16 January 2011 Fields added.

### 1Hemodialysis Setting File - \#704.209

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on hemodialysis settings used by the Hemodialysis application.

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
<td>Setting Name</td>
<td>704.209,.01</td>
<td><p>Free Text 3-30 characters in length. Not numeric or starting with</p>
<p>punctuation.</p></td>
<td>Contains the descriptive name of the data contained in this setting.</td>
</tr>
<tr class="even">
<td>Owner</td>
<td>704.209,.02</td>
<td><p>Pointer to new</p>
<p>person file (#200)</p></td>
<td><p>If this setting is user specific, this</p>
<p>field will contain that user’s DUZ.</p></td>
</tr>
<tr class="odd">
<td>User</td>
<td>704.209,.03</td>
<td>Pointer to new person file (#200)</td>
<td><p>This field displays the user name that is locking the Hemodialysis</p>
<p>setting option.</p></td>
</tr>
<tr class="even">
<td>Date/Time of Lock</td>
<td>704.209,.04</td>
<td><p>Input transform: S %DT="ET" D</p>
<p>^%DT S X=Y</p>
<p>K:Y&lt;1 X</p></td>
<td>This field will store the date and time of when the Hemodialysis setting option was locked for use.</td>
</tr>
<tr class="odd">
<td>Process ID</td>
<td>704.209,.05</td>
<td><p>Free text 3-40 characters in length. Input transform: K:$L(X)&gt;40!($L(X</p>
<p>)&lt;3) X</p></td>
<td>This field will store the JOB ID of the process that is locking the Hemodialysis setting option.</td>
</tr>
<tr class="even">
<td>XML Document</td>
<td>704.209,.1</td>
<td>Word Processing</td>
<td><p>Contains the XML document for</p>
<p>this setting in UUEncoded format.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.209 added.

### 1CP_CONSOLE_ACL File (704.001)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains the Access Control List (ACL) for items in the console by that item's ID.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ITEM_ID</td>
<td>704.001,.01</td>
<td>Free text (38 char)</td>
<td>This ITEM_ID represents the Global Unique Identifier (GUID) of a console item and Clinical Observation (CliO) record. An appropriate GUID is alphanumeric and 38 characters in length.</td>
</tr>
<tr class="even">
<td>USER_ID</td>
<td>704.001,.02</td>
<td>Pointer to NEW PERSON file (#200)</td>
<td>This is the end-user given access permission to the item (ITEM_ID).</td>
</tr>
<tr class="odd">
<td>ACCESS_LEVEL</td>
<td>704.001,.03</td>
<td><p>SET (Required)</p>
<blockquote>
<p>0 FOR Read Only 1 FOR Read+Write</p>
<p>2 FOR</p>
</blockquote>
<p>Read+Write+Delete 3 FOR Full Control</p></td>
<td>This is the level of edit access to the item (ITEM_ID) the end-user (USER_ID) has been permitted. In addition, "Full Control" will grant the user full edit privileges as well as the ability to grant access of this item to another user. This access permission is granted via the Access Control List Manager, a function within the CP Console application.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### 1CP_HL7_LOG File (#704.002)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains a log of HL7 Messages processed by Clinical Flowsheets.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MESSAGE_ID</p>
</blockquote></td>
<td>704.002,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field identifies the Clinical Flowsheets HL7 message. This MESSAGE_ID is generated by the Clinical Flowsheets system.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td>704.002,.02</td>
<td><p>'1' FOR ENTERED; 2' FOR AWAITING</p>
<p>PROCESSING; 3' FOR ERROR;</p>
<p>4' FOR PROCESSED;</p></td>
<td>This field indicates the status of this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)). This status is maintained by Clinical Flowsheets and HL7 message processing.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAPPING_TAB LE</p>
</blockquote></td>
<td>704.002,.03</td>
<td><p>FREE TEXT (1-</p>
<p>50 CHAR)</p></td>
<td><p>This field contains a copy of the ID field (#.01) in the TERM_MAPPING_TABLE file (#704.108). It</p>
<p>is used to determine which mapping table to use when translating the HL7 message (MESSAGE_ID field (#.01)) into observations.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7_MESSAGE</p>
<p>_ADMINISTRAT ION</p>
</blockquote></td>
<td>704.002,.04</td>
<td>POINTER TO HL7 MESSAGE ADMINISTRAT ION FILE (#773)</td>
<td>This field identifies this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) with an entry in the HL7 Message Administration File (#773).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7_MESSAGE</p>
<p>_TEXT</p>
</blockquote></td>
<td>704.002,.05</td>
<td>POINTER TO HL7 MESSAGE TEXT FILE (#772)</td>
<td>This field identifies this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) text with an entry in the HL7 MESSAGE TEXT File (#772).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td>704.002,.06</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This is the patient supported by the Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STUDY_REFER ENCE_NBR</p>
</blockquote></td>
<td>704.002,.07</td>
<td>POINTER TO CP TRANSACTION FILE (#702)</td>
<td>This field identifies the Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) with a CP TRANSACTION File (#702) entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MESSAGE_DAT E_TIME</p>
</blockquote></td>
<td>704.002,.08</td>
<td>DATE</td>
<td>This is the date/time the HL7 message (MESSAGE_ID field (#.01)) was created as reported by the HL7 system.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PROCESSED_TI MESTAMP</p>
</blockquote></td>
<td>704.002,.09</td>
<td>DATE</td>
<td>This is the date/time the HL7 message (MESSAGE_ID field (#.01)) was processed as reported by the HL7 system.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>REPORTED_LO CATION</p>
</blockquote></td>
<td>704.002,.11</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data as extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be location identifying data that can be used to locate the source of the HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>REPORTED_PA TIENT</p>
</blockquote></td>
<td>704.002,.21</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be patient identifying data used to determine which patient the HL7 message (MESSAGE_ID field (#.01)) supports.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>REPORTED_INS TRUMENT</p>
</blockquote></td>
<td>704.002,.31</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be instrument identifying data used to determine the source-device of the HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
</tbody>
</table>

> <span id="_bookmark21" class="anchor"></span>1CP_HL7_LOG_REASON (#704.004)

> This file monitors Clinical Flowsheets HL7 message processing anomalies. These Clinical Flowsheets HL7 messages are referenced via the CP_HL7_LOG file (#704.002).

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CLIO_HL7_LOG</p>
</blockquote></td>
<td>704.004,.01</td>
<td>POINTER TO CP_HL7_LOG FILE (#704.002)</td>
<td>This field identifies this entry with an entry in the CP_HL7_LOG file (#704.002).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DATE_TIME_EN TERED</p>
</blockquote></td>
<td>704.004,.02</td>
<td>DATE</td>
<td>This is the date/time the file entry was created.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REASON</p>
</blockquote></td>
<td>704.004,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is the reason this file entry was created.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark22" class="anchor"></span>1CP_MOVEMENT_AUDIT File (#704.005)

> This file will hold a subset of patient movement data. This must be done rather than using a direct reference to the PATIENT MOVEMENT file (#405) because, in the instance of cancellations, the internal entry number (IEN) of a patient movement disappears before there is the chance to work with it. This file will coalesce all of a movement's data to send to 3rd party users. That data is sent to 3rd party users via Health Level Seven (HL7) messaging. To ensure that message is available to 3<sup>rd</sup> party users, the ACCEPTED BY <sup>2</sup>QUEUE field (#.09) is set to '1' to confirm the message is in the HL7 outbound queue; that CP MOVEMENT AUDIT file (#704.005) entry will then need to be purged.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td>704.005,.01</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This field is the identifier of the patient involved in the patient movement event.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DATE_TIME_OF_ EVENT</p>
</blockquote></td>
<td>704.005,.02</td>
<td>DATE</td>
<td>This field stores the date/time of the patient movement event.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DIVISION</p>
</blockquote></td>
<td>704.005,.03</td>
<td>POINTER TO MEDICAL CENTER DIVISION FILE (#40.8)</td>
<td>This field identifies the DIVISION per the patient movement event.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td>704.005,.04</td>
<td>POINTER TO WARD LOCATION FILE (#42)</td>
<td>This field identifies the WARD per the patient movement event.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BED</p>
</blockquote></td>
<td>704.005,.05</td>
<td>POINTER TO ROOM-BED FILE (#405.4)</td>
<td>This field identifies the room-BED per the patient movement event.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MESSAGE_TYPE</p>
</blockquote></td>
<td>704.005,.06</td>
<td>FREE TEXT (3 CHAR)</td>
<td>This indicates the HL7 MESSAGE TYPE. The value here can be 'ADT' to indicate an admission/discharge/transfer type message.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVENT_TYPE</p>
</blockquote></td>
<td>704.005,.07</td>
<td>FREE TEXT (3 CHAR)</td>
<td>This indicates the HL7 message EVENT TYPE. The value here can be 'A01' to indicate an Admit/visit notification EVENT TYPE.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

> 2 Patch MD\*1.0\*12 October 2011 Removed reference to VDEF. Revised 704.005, 09 and 704.005, 1 field names.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PIMS_EVENT_ID</p>
</blockquote></td>
<td>704.005,.08</td>
<td>FREE TEXT (1-20 CHAR)</td>
<td><p>This is a copy of the internal entry number (IEN) of the PATIENT MOVEMENT file (#405) entry which correlates to this CP_MOVEMENT_AUDIT file (#704.005)</p>
<p>entry.</p>
<p>If a movement is deleted, the corresponding entry from the patient movement file is deleted as well. This prevents this field from being an actual pointer. This IEN is used only for troubleshooting purposes.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACCEPTED_BY_ QUEUE</p>
</blockquote></td>
<td>704.005,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This indicates whether the HL7 message has been queued.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QUEUE_ERROR_ MSG</p>
</blockquote></td>
<td>704.005,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This field stores the error message, if an error message is returned by the message queue process.</td>
</tr>
</tbody>
</table>

### 1CP_PROTOCOL_LOCATION File (#704.006)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file will be used by the Clinical Flowsheets application to determine the target for an outbound admission, discharge, and transfer (ADT) message. Messages are sent to a target via Health Level 7 messaging (HL7).

> A target is defined here as a receiving CIS or other COTS product that has expressed a desire to be notified when a patient admission, transfer or discharge has occurred for a specific hospital location.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SUBSCRIBER</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.01</p>
</blockquote></td>
<td><blockquote>
<p>POINTER TO PROTOCOL FILE (#101)</p>
</blockquote></td>
<td><blockquote>
<p>This field identifies the subscriber protocol to be used to send the message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DIVISION</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.02</p>
</blockquote></td>
<td><blockquote>
<p>POINTER TO MEDICAL CENTER DIVISION FIL E (#40.8</p>
</blockquote></td>
<td><blockquote>
<p>This field identifies the target MEDICAL CENTER DIVISION for the message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.03</p>
</blockquote></td>
<td><blockquote>
<p>POINTER TO WARD LOCATION FILE (#42)</p>
</blockquote></td>
<td><blockquote>
<p>This field identifies the target WARD location for the message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MESSAGE_TYPE</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.04</p>
</blockquote></td>
<td><blockquote>
<p>FREE TEXT (3 CHAR)</p>
</blockquote></td>
<td><blockquote>
<p>This field is the type of message to be sent. A sample MESSAGE TYPE could be "ADT".</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVENT_TYPE</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.05</p>
</blockquote></td>
<td><blockquote>
<p>FREE TEXT (3 CHAR)</p>
</blockquote></td>
<td><blockquote>
<p>This is the message's EVENT TYPE. A sample EVENT TYPE could be "A01".</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.06</p>
</blockquote></td>
<td><blockquote>
<p>FREE TEXT (32 CHAR)</p>
</blockquote></td>
<td><blockquote>
<p>This field will be the alpha-numeric portion of the message's Global Unique Identifier (GUID), if the message is generated. A sample ID could be "C42AC54282B642F4950E179A3D43AA85".</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>704.006,.07</p>
</blockquote></td>
<td><blockquote>
<p>FREE TEXT (1-30 CHAR)</p>
</blockquote></td>
<td><blockquote>
<p>This field is the assigned name for the message. A sample NAME could be "ADMIT2DEVICEX".</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark24" class="anchor"></span>1CP_SHIFT File (#704.007)

> This file is used to store the site configurable shift definitions.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.007,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field contains the work-shift identifier. A sample ID could be "{1A5A417B-3F04-23ED- B044-4102B19D66E4}"</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.007,.02</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>HELP-PROMPT: Answer must be 1-30 characters in length. This is the NAME of the work-shift. A sample could be "DAY”.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>START_TIME</p>
</blockquote></td>
<td>704.007,.03</td>
<td>FREE TEXT (4 CHAR)</td>
<td>This is the START TIME of the work-shift. An example is "0800" representing the time 8:00 AM.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>STOP_TIME</p>
</blockquote></td>
<td>704.007,.04</td>
<td>FREE TEXT (4 CHAR)</td>
<td>This is the STOP TIME of the work-shift. An example is "1830" representing the time 6:30 PM.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MULTI_DAY</p>
</blockquote></td>
<td>704.007,.05</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field indicates whether a work-shift extends over multiple days or not.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.007,.06</td>
<td>FREE TEXT (1-50 CHAR)</td>
<td>HELP-PROMPT: Answer must be 1-50 characters in length. This field is the text displayed within Clinical Flowsheets for the work-shift. A sample DISPLAY NAME could be "Nights (Midnight - 8:00a)".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.007,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field determines whether the work-shift entry is active or not.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.007,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is a comment about the work-shift.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark25" class="anchor"></span>1CP_SCHEDULE File (#704.008)

> This file is used to store the site configurable schedules for the Kardex.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.008,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field contains the schedule identifier. A sample ID could be "{E24290F6-31F4-C6F6- B310-E37C563FBD64}”.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.008,.02</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>This is the NAME of the schedule. A sample could be "TID/MEALS”.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCHEDULE_TYPE</p>
</blockquote></td>
<td>704.008,.03</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; 1' FOR PRN;</p>
<p>2' FOR One-Time;</p>
<p>3' FOR Stat;</p></td>
<td>This is the type of schedule indicator.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>INTERVAL</p>
</blockquote></td>
<td>704.008,.04</td>
<td><p>NUMBER (0-</p>
<p>525600)</p></td>
<td>This field is the schedule INTERVAL in minutes. An example is "120" to present a schedule INTERVAL of 2 hours.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.008,.05</td>
<td>FREE TEXT (1-50 CHAR)</td>
<td>This field is the text displayed within Clinical Flowsheets for the schedule. A sample DISPLAY NAME could be "3 times daily with meals”.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.008,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field determines whether the schedule entry is active or not.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.008,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is a COMMENT about the schedule.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CUSTOM_SCHED ULE</p>
</blockquote></td>
<td>704.008,.2</td>
<td><p>FREE TEXT (4-</p>
<p>250 CHAR)</p></td>
<td>This field contains actual times a scheduled event is to occur. This data is to be utilized when the schedule intervals are not equal. A sample CUSTOM SCHEDULE could be "0600,1100,1700" for schedule events to occur at 6 AM, 11 AM, and 5 PM.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark26" class="anchor"></span>1TERM File (#704.101)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file stores all terminology elements for the Clinical Flowsheets application. The entries in this file are called "terms". These terms along with CP files \#704.102 -#704.109 constitute the Clinical Data Model.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.101,.01</td>
<td><p>FREE TEXT</p>
<p>(Required) (38 CHAR)</p></td>
<td>This field is the unique identifier for this entry or term. This data is maintained nationally and will be the identifier for this term enterprise-wide. A sample ID could be "{D9FF5CA8-09AF-4318-B784- DEB3A8F819D8}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM</p>
</blockquote></td>
<td>704.101,.02</td>
<td>FREE TEXT (1-7 CHAR)</td>
<td>This field is the name of this TERM entry, in accordance with enterprise-wide terminology standards. A sample TERM could be "PICC LINE".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ABBREVIATION</p>
</blockquote></td>
<td>704.101,.03</td>
<td>FREE TEXT (1-10 CHAR)</td>
<td>This is the enterprise wide ABBREVIATION for this term. This value will be used throughout the Clinical Flowsheets system in dropdowns and list boxes where screen real estate is tight. A sample ABBREVIATION could be "PICC LINE".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.101,.04</td>
<td>FREE TEXT (1-75 CHAR)</td>
<td>This field is a case sensitive, user friendly, DISPLAY NAME for this term. This is the full name for this term for display in the Clinical Flowsheets application. A sample DISPLAY NAME could be "PICC Line".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_TYPE</p>
</blockquote></td>
<td>704.101,.05</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td><p>This field correlates this term with an entry in the TERM TYPE File (#704.102). This field should define the "purpose" of this term in the Clinical Data Model.</p>
<p>CROSS-REFERENCE: 704.101^ATYPE 1)= S</p>
<p>^MDC(704.101,"ATYPE",$E(X,1,30),DA)="" 2)= K</p>
<p>^MDC(704.101,"ATYPE",$E(X,1,30),DA)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DATA_TYPE</p>
</blockquote></td>
<td>704.101,.06</td>
<td><p>SET</p>
<p>'0' FOR Qualifier;</p>
<p>1' FOR Complex;</p>
<p>2' FOR Numeric;</p>
<p>3' FOR PickList;</p>
<p>4' FOR Boolean;</p>
<p>5' FOR String;</p>
<p>6' FOR Range;</p></td>
<td>This field is to specify the type of data this term represents.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VALUE_TYPE</p>
</blockquote></td>
<td>704.101,.07</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Unspecified; 1' FOR</p>
<p>Temperature; 2' FOR Length;</p>
<p>3' FOR Volume;</p>
<p>4' FOR Rate;</p>
<p>5' FOR Time;</p>
<p>6' FOR Mass;</p>
<p>7' FOR Scale;</p></td>
<td>This field is to specify the VALUE TYPE this term represents. This data will be used for more reliable conversion utilities.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.101,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>1' FOR Yes;</p></td>
<td>This field is to indicate whether a term is ACTIVE or not. Only an ACTIVE term can be used in new clinical observations.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td>704.101,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This field is a full DESCRIPTION of this term. A sample DESCRIPTION could be: "Peripherally Inserted Central Catheter Line".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>HELP_TEXT</p>
</blockquote></td>
<td>704.101,.2</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is the text that will display as help for the term, within the Clinical Flowsheets application. A sample HELP TEXT could be: "Peripherally Ins Cen Cath Line".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BOOLEAN_VALU E_TRUE</p>
</blockquote></td>
<td>704.101,.31</td>
<td><p>FREE TEXT (1-</p>
<p>100 CHAR)</p></td>
<td>This field is the text that will display for Boolean DATA TYPE (field #.06) observations that are "true". A sample BOOLEAN VALUE TRUE could be "TRUE".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>BOOLEAN_VALU E_FALSE</p>
</blockquote></td>
<td>704.101,.32</td>
<td><p>.3;2 FREE TEXT</p>
<p>(1-100 CHAR)</p></td>
<td>This field is the text that will display for Boolean DATA TYPE (field #.06) observations that are "false". A sample BOOLEAN VALUE FALSE could be "FALSE".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MULTI_SELECT_ PICKLIST</p>
</blockquote></td>
<td>704.101,.33</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>1' FOR Yes;</p></td>
<td>This field determines if more than one value may be selected from a "picklist" for an observation.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SCHEDULE</p>
</blockquote></td>
<td>704.101,.34</td>
<td>NUMBER</td>
<td>This field is the minutes of interval per SCHEDULE. A sample SCHEDULE could be "120".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCHEDULE_TYPE</p>
</blockquote></td>
<td>704.101,.35</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; 1' FOR PRN;</p>
<p>2' FOR Stat;</p>
<p>3' FOR One-Time;</p></td>
<td>This field is the type of schedule.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>VUID</p>
</blockquote></td>
<td>704.101,99.99</td>
<td>FREE TEXT (1-20 CHAR)</td>
<td>This field is the VHA Unique IDentifier (VUID) for this term.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.102,.001</td>
<td>NUMBER</td>
<td>This is the ordinal position of this term-type entry.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark27" class="anchor"></span>1TERM_TYPE File (#704.102)

> This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td>704.102,.01</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>This is the name for this term TYPE. A sample TYPE could be "OBSERVATION".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XML_TAG</p>
</blockquote></td>
<td>704.102,.02</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>This is the XML TAG this data element is to be stored on when an appropriate XML document is built. A sample XML TAG could be "TERM_ID".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VUID</p>
</blockquote></td>
<td>704.102,.03</td>
<td>FREE TEXT (1-20 CHAR)</td>
<td>This field is the VHA Unique IDentifier (VUID) for this term type. A sample VUID could be "4688703".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark28" class="anchor"></span>1TERM_QUALIFIER_PAIR File (#704.103)

> This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the Clio data store if this file is changed.

> This file is a join table for the Clinical Data Model that matches observations to their allowable qualifiers. A sample could be the observation equating to "weight" and the paired qualifier equating to "lift scale".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.103,.01</td>
<td><p>POINTER TO TERM FILE (#704.101)</p>
<p>(Required) (Key field)</p></td>
<td>This field identifies the primary TERM file (#704.101) entry in the Clinical Data Model for this pairing.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>QUALIFIER_ORD ER</p>
</blockquote></td>
<td>704.103,.02</td>
<td><p>NUMBER</p>
<p>(Between 0-9999)</p></td>
<td>This represents the order that this qualifier will be displayed with the term as well as the order of interpretation for complex terms.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QUALIFIER_ID</p>
</blockquote></td>
<td>704.103,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the qualifier term or subcomponent for this pair.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>RANKING</p>
</blockquote></td>
<td>704.103,.04</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This value will be used in calculations for this pairing as well as future graphing capabilities for pick-list values.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### 1TERM_UNIT_CONVERSION File (#704.104)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file links like units of measure together with required conversion logic to change the value from one unit to another.

> NOTE: Units are presented as entries in the TERM file (#704.101). For example the unit "CENTIMETER" could be identified by the TERM file (#704.101), TERM ID (field \#.01)"{EF700458-8C2D-16E8-02DC-9E1711584C53}".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>UNIT_ID_PRE</p>
</blockquote></td>
<td>704.104,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field is the identifier of the unit that a value will be converted from.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>UNIT_ID_POST</p>
</blockquote></td>
<td>704.104,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field is the identifier of the unit that a value will be converted to.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONVERSION_OF FSET_PRE</p>
</blockquote></td>
<td>704.104,.03</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 6</p>
<p>decimal digits)</p></td>
<td>This field will be used to offset a value prior to executing the conversion logic. A sample CONVERSION OFFSET PRE could be "0".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CONVERSION_OF FSET_POST</p>
</blockquote></td>
<td>704.104,.04</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 6</p>
<p>decimal digits)</p></td>
<td>This is used to offset a value post execution of the conversion logic. A sample CONVERSION OFFSET POST could be "32".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONVERSION_FA CTOR</p>
</blockquote></td>
<td>704.104,.05</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This value is used by the conversion logic as a multiplier of the original value. A sample CONVERSION FACTOR could be "1.8".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DECIMAL_PRECI SION</p>
</blockquote></td>
<td>704.104,.06</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 0</p>
<p>decimal digits)</p></td>
<td>This field is the decimal precision for rounding the resulting conversion value. A sample DECIMAL PRECISION could be "2".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td>704.104,.09</td>
<td><p>FREE TEXT (1-</p>
<p>150 CHAR)</p></td>
<td>This is a DESCRIPTION of the conversion logic. A sample DESCRIPTION could be "DEGREES C -&gt; DEGREES F".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark30" class="anchor"></span>1TERM_UNIT_PAIR File (#704.105)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed. This file matches observation(s) with available units for the observation, and the range settings for each pair.

> Observations are presented as entries in the TERM file (#704.101). For example the observation "TRACTION WEIGHT" could be identified by the TERM file (#704.101), TERM ID (field#.01) "{0C913807-C678-4E94-BD20-B8B2EBE697BE}".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.105,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the Observation in this "observation/unit" pair.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>UNIT_ID</p>
</blockquote></td>
<td>704.105,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the Unit in this "observation/unit" pair.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MIN_VALUE</p>
</blockquote></td>
<td>704.105,.03</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 7</p>
<p>decimal digits)</p></td>
<td>This field contains the minimum value that can be entered for this observation/unit pair. A sample could be "-1".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAX_VALUE</p>
</blockquote></td>
<td>704.105,.04</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 7</p>
<p>decimal digits)</p></td>
<td>This field contains the maximum value that can be entered for this observation/unit pair. A sample could be "31".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEC_PRECISION</p>
</blockquote></td>
<td>704.105,.05</td>
<td><p>NUMBER (0-7) INPUT TRANSFORM: K:+X'=X!(X&gt;7)!(X</p>
<p>&lt;0)!(X?.E1"."1.N) X</p>
<p>LAST EDITED: APR 02, 2009 HELP-PROMPT:</p>
<p>Type a number between 0 and 7, 0 Decimal Digits</p></td>
<td>This is the maximum decimal precision that can be entered for this observation/unit pair. A sample could be "0".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>REFERENCE_LO W</p>
</blockquote></td>
<td>704.105,.06</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This is the value for this observation/unit pair that will cause Clinical Flowsheets to interpret the observed value as "low". A sample REFERENCE LOW could be "0".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REFERENCE_HIG H</p>
</blockquote></td>
<td>704.105,.07</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This is the value for this observation/unit pair that will cause Clinical Flowsheets to interpret the observed value as "high". A sample REFERENCE HIGH could be "30".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark31" class="anchor"></span>1TERM_CHILD_PAIR File (#704.106)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file holds the structure for complex observations by pairing the parent observation to the child observation with an ordinal position as well. Observations are entries in the TERM file (#704.101).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.106,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the primary observation/term for complex term pairs. A sample TERM_ID could identify "blood pressure" as a primary term.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILD_ORDER</p>
</blockquote></td>
<td>704.106,.02</td>
<td>NUMBER (between 1 and 999)</td>
<td>This represents the order of the child pair in association with a complex term.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CHILD_ID</p>
</blockquote></td>
<td>704.106,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the child term for a complex term pair. A sample CHILD_ID could identify "systolic" as a child term of "blood pressure".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILD_UNIT_ID</p>
</blockquote></td>
<td>704.106,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This is the unit(s) to present this child term. A sample CHILD_UNIT_ID could identify "MILLIMETERS OF MERCURY".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALUE_TYPE</p>
</blockquote></td>
<td>704.106,.05</td>
<td><p>SET</p>
<p>'0' FOR Extract;</p>
<p>1' FOR Delimited;</p></td>
<td>This field will indicate whether the observation values are delimited or not.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALUE_DELIMIT ER</p>
</blockquote></td>
<td>704.106,.06</td>
<td>NUMBER (ASCII 32-126)</td>
<td>This is the number between 32 and 126 (0 Decimal Digits) of the ASCII value for the character to be used as the delimiter per delimited values. A sample VALUE_DELIMITER could be "47" to signify the use of the character "/" as delimiter.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALUE_START_P OSITION</p>
</blockquote></td>
<td>704.106,.07</td>
<td><p>NUMBER</p>
<p>(Between 1 and</p>
<p>250)</p></td>
<td>The "child values" may be presented in a string of data. This field is either the position or the delimited piece, of the data to begin extracting child values.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALUE_STOP_PO SITION</p>
</blockquote></td>
<td>704.106,.08</td>
<td><p>NUMBER</p>
<p>(Between 1 and</p>
<p>250)</p></td>
<td>The "child values" may be presented in a string of data. This field is either the last position or the last delimited piece of the data. This is where extracting of child values is to stop.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td>704.106,.09</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a DESCRIPTION of this observation/child term pair. A sample DESCRIPTION could be "Systolic pressure".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark32" class="anchor"></span>1TERM_RANGE_CHECK File (#704.107)

> This file maintains value ranges for related observations/terms.

> An example could be a TERM RANGE CHECK entry that would result in an observed TEMPERATURE of 80 DEGREES FAHRENHEIT for a MALE between 55-150 years of AGE, triggering a "CRITICAL LOW" response by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.107,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the term to which a term range check is applicable. A sample TERM ID could identify the term "TEMPERATURE".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>UNIT_ID</p>
</blockquote></td>
<td>704.107,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the unit of measurement related to the TERM_ID (field #.01). A sample UNIT ID could identify "DEGREES F".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SEX</p>
</blockquote></td>
<td>704.107,.03</td>
<td><p>SET</p>
<p>M' FOR Male; F' FOR Female; N' FOR Non-</p>
<p>Specific;</p></td>
<td>This field indicates the gender to which a term range check is applicable. A sample SEX could be "Male".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AGE_MINIMUM</p>
</blockquote></td>
<td>704.107,.04</td>
<td><p>NUMBER</p>
<p>(Between 0 and</p>
<p>150)</p></td>
<td>This is the minimum age which the term range check is applicable. A sample AGE MINIMUM could be "55".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AGE_MAXIMUM</p>
</blockquote></td>
<td>704.107,.05</td>
<td><p>NUMBER</p>
<p>(Between 0 and</p>
<p>150)</p></td>
<td>This is the maximum age which the term range check is applicable. A sample AGE MAXIMUM could be "150".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT_ID</p>
</blockquote></td>
<td>704.107,.08</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This field identifies a patient for which the term range check is applicable. A sample PATIENT ID could identify "CP FLOWSHEETS,PATIENT1".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td>704.107,.09</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is a DESCRIPTION of the term range check entry. A sample DESCRIPTION could be "Senior male temperature".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRITICAL_LOW</p>
</blockquote></td>
<td>704.107,.11</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "CRITICAL LOW" result when the term range check is applied. A sample CRITICAL LOW could be "80".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ABNORMAL_LO W</p>
</blockquote></td>
<td>704.107,.12</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause an "ABNORMAL LOW" result when the term range check is applied. A sample ABNORMAL LOW could be "85".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NORMAL_LOW</p>
</blockquote></td>
<td>704.107,.13</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "NORMAL LOW" result when the term range check is applied. A sample NORMAL LOW could be "90".</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NORMAL_HIGH</p>
</blockquote></td>
<td>704.107,.14</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "NORMAL HIGH" result when the term range check is applied. A sample NORMAL HIGH could be "100".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ABNORMAL_HIG H</p>
</blockquote></td>
<td>704.107,.15</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause an "ABNORMAL HIGH" result when the term range check is applied. A sample ABNORMAL HIGH could be "103".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRITICAL_HIGH</p>
</blockquote></td>
<td>704.107,.16</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This is the value that will cause a CRITICAL HIGH"" result when the term range check is applied. A sample CRITICAL HIGH could be "106".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark33" class="anchor"></span>1TERM_MAPPING_TABLE File (# 704.108)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file is the anchor for the mapping table structure for the CP Gateway. Each mapping table is called up by elements in the HL7 message. The entries are used to translate the HL7 data into appropriate CP terminology.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.108,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This field is the Global Unique IDentifier (GUID) that identifies the mapping table. A sample ID could be "{4E41823C-CB5B-499F- BAAC-13626A6CD0D2}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.108,.02</td>
<td><p>FREE TEXT</p>
<p>(Between 1-50 char)</p></td>
<td>This field is the NAME of the mapping table. A sample could be "DeviceX ServiceZ".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7_SENDING_A PPLICATION</p>
</blockquote></td>
<td>704.108,.03</td>
<td><p>FREE TEXT (1 to</p>
<p>50 char)</p></td>
<td>This field is the application sending the HL7 message. This will be used for matching purposes. A sample HL7 SENDING APPLICATION could be "ServiceZ".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.108,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this mapping- table is ACTIVE or not.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.108,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is a comment about the mapping- table. A sample COMMENT could be "Default DeviceX ServiceZ mapping table".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SOURCE_ID</p>
</blockquote></td>
<td>704.108,.21</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This field identifies the source of the HL7 message. A sample SOURCE ID could be "DeviceX".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOURCE_APPLIC ATION</p>
</blockquote></td>
<td>704.108,.22</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td><p>This field is the application regarded as the source of the HL7 message. A sample SOURCE APPLICATION could be</p>
<p>"ServiceZ".</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SOURCE_VERSIO N</p>
</blockquote></td>
<td>704.108,.23</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This field is the version of the source of the HL7 message. A sample SOURCE VERSION could be "VerN-ReleaseN.NN".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOURCE_TRUSTE D</p>
</blockquote></td>
<td>704.108,.24</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether data processed via this source/mapping-table is "trusted" or not. Only verified data will be filed. Verification may be done with user intervention or it may be automatic. Trusted mapping-tables will have their data filed as "verified" without user intervention.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark34" class="anchor"></span>1TERM_MAPPING_PAIR File (#704.109)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file correlates a vendor (VENDOR KEY field \#.1) with a mapping-table (MAPPING TABLE ID field \#.01) and an HL7 message segment (TERM TYPE field \#.03). A sample entry could be interpreted as follows: Mapping-TableXX is used for processing when VendorX has sent an XType message.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MAPPING_TABLE</p>
<p>_ID</p>
</blockquote></td>
<td>704.109,.01</td>
<td><p>POINTER TO TERM_MAPPING</p>
<p>_TABLE FILE (#7</p>
<p>04.108)</p></td>
<td>This identifies the mapping-table of this TERM MAPPING PAIR entry. A sample could identify "Mapping-TableXX".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>RECORD INDEXES:</p>
</blockquote></td>
<td></td>
<td>PK (#772)</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_TYPE</p>
</blockquote></td>
<td>704.109,.03</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td>This field will determine the HL7 message segment relating to this term mapping pair; and identifies a term-type in the TERM TYPE File (#704.102). A sample could be a TERM TYPE identifying the HL7 message segment with "XType" data to be related to this term mapping pair.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM</p>
</blockquote></td>
<td>704.109,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the TERM relating to this term mapping pair. A sample TERM could identify "TEMPERATURE".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VENDOR_KEY</p>
</blockquote></td>
<td>704.109,.1</td>
<td><p>FREE TEXT (1-</p>
<p>240 char)</p></td>
<td>This field indicates the vendor related to this term mapping pair. A sample VENDOR KEY could be "111X213".</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### 1OBS_VIEW File (#704.111)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains the views displayed within a flowsheet via the Clinical Flowsheets application. A view is a group of terms displayed together. A sample view could display "ICU VITALS, INPUTS, OUTPUTS, and ICU HEMODYNAMICS" information together in a section of a flowsheet displayed via the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VIEW_ID</p>
</blockquote></td>
<td>704.111,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is the view's Global Unique IDentifier (GUID). This value is maintained nationally and represents this view throughout the enterprise. A sample VIEW ID could be "{11AA9949-B1FA-40A5-A208- 5BB8255BE961}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.111,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the NAME of this view. A sample NAME could be "ICU HEMODYNAMICS".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TIME_INTERVAL</p>
</blockquote></td>
<td>704.111,.03</td>
<td>NUMBER (1-1440)</td>
<td>A view is displayed to the user as part of a "page" on the screen. That page is divided into TIME INTERVALs. This field is the number of minutes within an interval when the page is initially displayed to the user. The maximum is 1440 (1 day). A sample TIME INTERVAL could be "60".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>X_AXIS</p>
</blockquote></td>
<td>704.111,.04</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Terminology;</p>
<p>'1' FOR Date/Time;</p></td>
<td>This field indicates whether the initial layout of the view's horizontal axis shows terminology information or date/time information. The information not indicated to display horizontally will initially display vertically.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.111,.05</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name of this view to display to the user when this view is being used. A sample DISPLAY NAME could be "ICU Hemodynamics".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALLOW_PIVOT</p>
</blockquote></td>
<td>704.111,.06</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether the user is allowed to "pivot" how information is displayed. For example: If initially this view's terminology information displays horizontally and date/time information displays vertically, a '1' value ("YES") in this field gives the user the option to display this view's terminology information vertically and the date/time information horizontally.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NATIONAL_TITL E</p>
</blockquote></td>
<td>704.111,.08</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this view is a NATIONAL TITLE, maintained nationally, and cannot be modified at/by a site.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.111,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether this view is ACTIVE or not. An ACTIVE view can be incorporated into a flowsheet.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.111,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is free-text comment to describe the use and purpose of this view. A sample COMMENT could be "National ICU Flowsheet View".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark36" class="anchor"></span>1OBS_VIEW_TERMINOLOGY File (#704.1111)

> This file maintains the relationships between views of OBS_VIEW File (#704.111) and terms of TERM file (#704.001).

> Some field descriptions are directed to a programming and development audience.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VIEW_ID</p>
</blockquote></td>
<td>704.1111,.01</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This field identifies an entry in the OBS VIEW File (#704.111); correlates this file entry with a view.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM_ORDER</p>
</blockquote></td>
<td>704.1111,.02</td>
<td>NUMBER (1-999)</td>
<td>This field indicates the order this term will display in that view identified by VIEW ID (field #.01).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.1111,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies an entry in the TERM File (#704.001); correlates this file entry with a term.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.1111,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This name will display to the user when the Clinical Flowsheets application shows this term (TERM ID field #.03). A sample DISPLAY NAME could be "IV - Platelets".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_WIDTH</p>
</blockquote></td>
<td>704.1111,.05</td>
<td><p>NUMBER (80-</p>
<p>9999)</p></td>
<td>This field is the number of pixels this term (TERM ID field #.03) will require to be displayed in the Clinical Flowsheets application. A sample could be "120".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_TOTAL</p>
</blockquote></td>
<td>704.1111,.06</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a summation of term (TERM ID field #.03) measurements will display at the bottom of a grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_COUNT</p>
</blockquote></td>
<td>704.1111,.07</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether or not a count of terms (TERM ID field#.03) related to the view (VIEW ID field #.01) will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_AVERA GE</p>
</blockquote></td>
<td>704.1111,.08</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether an average of term (TERM ID field #.03) measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_ONLY</p>
</blockquote></td>
<td>704.1111,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This indicates whether this term (TERM ID field#.03) in this view (VIEW ID field#.01) is only for display and reporting purposes and cannot be modified.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_COLU MNS</p>
</blockquote></td>
<td>704.1111,.1</td>
<td>NUMBER (0-9)</td>
<td>When a "picklist" value is displayed for input in a radio group box this value is used to indicate how many columns this term-value will be displayed in.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_IN_CEL L_TOTAL</p>
</blockquote></td>
<td>704.1111,.11</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a sub-totals of indicated totals (e.g., total(#.06), count(#.07), average(#.08) etc.) display within each TIME INTERVAL (file #704.111 field #.03) of this view (VIEW ID #.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_MINIM UM</p>
</blockquote></td>
<td>704.1111,.12</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the least of a list of term measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_MAXI MUM</p>
</blockquote></td>
<td>704.1111,.13</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the greatest of a list of term measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>REQUIRED_TER M</p>
</blockquote></td>
<td>704.1111,.14</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this term (TERM ID #.03) must be given a value when using this view (VIEW ID #.01) for input.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USE_DROPDOWN</p>
</blockquote></td>
<td>704.1111,.15</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a value for this term will necessitate the use of a "drop down" instead of a "radio group". With long "picklists" it is sometimes necessary to display items in a drop down instead of a radio group.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark37" class="anchor"></span>1OBS_VIEW_FILTER File (#704.1112)

> This file maintains relationships between view entries in the OBS VIEW file (#704.1111) and qualifiers/filters.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VIEW_ID</p>
</blockquote></td>
<td>704.1112,.01</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This field identifies an entry in the OBS VIEW File (#704.111); correlates this file entry with a view.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM_ORDER</p>
</blockquote></td>
<td>704.1112,.02</td>
<td>NUMBER (1-9999)</td>
<td>This is the order of the filter in this file entry.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RECORD INDEXES:</p>
</blockquote></td>
<td></td>
<td>PK (#730)</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FILTER_TYPE</p>
</blockquote></td>
<td>704.1112,.03</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td>This is the type of term this filter uses.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FILTER_TERM</p>
</blockquote></td>
<td>704.1112,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the term this filter relates to; correlates this file entry to a TERM File (#704.101) entry. This is the term/qualifier by which to filter.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>FILTER_USAGE</p>
</blockquote></td>
<td>704.1112,.05</td>
<td><p>SET</p>
<p>'0' FOR DEFAULT VALUE;</p>
<p>'1' FOR MANDATORY VALUE;</p></td>
<td>This field is to indicate whether this filter is mandatory or a default when entering new data.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark38" class="anchor"></span>1OBS_FLOWSHEET File (#704.112)

> This file maintains the flowsheets used by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FLOWSHEET_ID</p>
</blockquote></td>
<td>704.112,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>HELP-PROMPT: Answer with the Global Unique IDentifier (GUID) for this flowsheet. This value is the Global Unique IDentifier for this flowsheet. This value is system generated, maintained nationally, so this value represents the same flowsheet throughout the enterprise. A sample FLOWSHEET ID could be "{E2237CB1-7706-4B43-A96C- D08B812D2A2E}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.112,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the official NAME for this flowsheet (#.01). A sample NAME could be "ICU MONITORING".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.112,.03</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name displayed via the Clinical Flowsheets application for this flowsheet. A sample DISPLAY NAME could be "ICU Monitoring".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.112,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a free-text COMMENT to document the purpose for this flowsheet (#.01). A sample COMMENT could be "Primary flowsheet for ICU patients".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.112,.05</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether this flowsheet (#.01) can be used in the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEFAULT_TIU_N OTE</p>
</blockquote></td>
<td>704.112,.06</td>
<td>POINTER TO TIU DOCUMENT DEFINITION FIL E (#8925.1)</td>
<td>This field correlates this entry to an entry in the TIU DOCUMENT File (#8925).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_KARDE X</p>
</blockquote></td>
<td>704.112,.07</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the "Kardex grid" will be displayed when this flowsheet (#.01) is opened.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark39" class="anchor"></span>1OBS_FLOWSHEET_PAGE File (#704.1121)

> This file maintains the relationships between OBS_FLOWSHEET file (#704.112) entries and pages/view (OBS_VIEW file \#704.111) entries.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FLOWSHEET_ID</p>
</blockquote></td>
<td>704.1121,.01</td>
<td><p>POINTER TO OBS_FLOWSHEE T FILE (#704.11 2)</p>
<p>(Key field)</p></td>
<td>This field identifies the flowsheet that correlates to this file entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAGE_ORDER</p>
</blockquote></td>
<td>704.1121,.02</td>
<td>NUMBER (1-99)</td>
<td>This field is the order of display for this view in the flowsheet (#.01).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VIEW_ID</p>
</blockquote></td>
<td>704.1121,.03</td>
<td><p>POINTER TO OBS_VIEW FILE (#704.111) (Key</p>
<p>field)</p></td>
<td>This field identifies a page/view displayed via this flowsheet (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAGE_TYPE</p>
</blockquote></td>
<td>704.1121,.04</td>
<td><p>SET</p>
<p>'0' FOR Mandatory;</p>
<p>'1' FOR Optional;</p>
<p>'2' FOR</p>
<p>Supplemental;</p></td>
<td>This field indicates how this view (#.03) will be utilized in this flowsheet (#.01).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.1121,.05</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td><p>This is a name to override the default DISPLAY NAME (file #704.112, field #.03).</p>
<p>This name will display when this page/view (#.03) is shown with this flowsheet (#.01). A sample DISPLAY NAME could be "NurseX ICU Monitoring".</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPECIAL_INSTRU CTIONS</p>
</blockquote></td>
<td>704.1121,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td><p>This is free-text to provide a way to give additional instruction, comment, or note about the use of this view (#.03) with this flowsheet (#.01). A sample SPECIAL INSTRUCTIONS</p>
<p>value could be "Pivot the page when possible".</p></td>
</tr>
</tbody>
</table>

> <span id="_bookmark40" class="anchor"></span>1OBS_FLOWSHEET_SUPP_PAGE File (#704.1122)

> This file maintains supplemental pages/views. The supplemental page is a variation of a page as supported via the OBS_FLOWSHEET_PAGE file (#704.1121).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.1122,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally, so this value identifies this supplemental page throughout the enterprise.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>VIEW_ID</p>
</blockquote></td>
<td>704.1122,.02</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This identifies the view for this supplemental page (#.01); correlates this entry with an entry in the OBS_VIEW File (#704.111).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PATIENT_ID</p>
</blockquote></td>
<td>704.1122,.03</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the patient assigned to this supplemental page (#.01); correlates this entry with a PATIENT File (#2) entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEFAULT_METH OD_ID</p>
</blockquote></td>
<td>704.1122,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default method to use with this supplemental page (#.01). This method is a TERM File (#704.101) entry. A sample DEFAULT METHOD ID could be an identifier for the term "ARTERIAL LINE".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEFAULT_POSITI ON_ID</p>
</blockquote></td>
<td>704.1122,.05</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default position to use with this supplemental page (#.01). This position is a TERM File (#704.101) entry. A sample DEFAULT POSITION ID could be an identifier for the term "LYING".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEFAULT_LOCA TION_ID</p>
</blockquote></td>
<td>704.1122,.06</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default location to use with this supplemental page (#.01). This location is a TERM File (#704.101) entry. A sample DEFAULT LOCATION ID could be an identifier for the term "ANKLE".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEFAULT_PROD UCT_ID</p>
</blockquote></td>
<td>704.1122,.07</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default product to use with this supplemental page (#.01). This product is a TERM File (#704.101) entry. A sample DEFAULT PRODUCT ID could be an identifier for the term "5% PRODUCT X".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.1122,.08</td>
<td><p>FREE TEXT (1-</p>
<p>100 char)</p></td>
<td>This is the DISPLAY NAME to override the view display name (file #704.111, field #.05) when activated. A sample DISPLAY NAME could be "IV Input Blood Products".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td>704.1122,.09</td>
<td><p>SET</p>
<p>'0' FOR INACTIVE;</p>
<p>'1' FOR ACTIVE;</p></td>
<td>This indicates whether this supplemental page (#.01) is active or inactive for this patient's (#.03) treatment.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SET_ID</p>
</blockquote></td>
<td>704.1122,.1</td>
<td>POINTER TO OBS_SET FILE (#704.116)</td>
<td>This field identifies the OBSERVATION SET file (#704.116) entry that correlates with this entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVATED_DA TE_TIME</p>
</blockquote></td>
<td>704.1122,.11</td>
<td>DATE</td>
<td>This is the date/time this supplemental page (#.01) is activated.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACTIVATED_BY_ ID</p>
</blockquote></td>
<td>704.1122,.12</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) to activate this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVATED_CO MMENT</p>
</blockquote></td>
<td>704.1122,.13</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td>This is the user supplied comment stored when the page is activated. A sample ACTIVATED COMMENT could be "supplemental page X activated by request".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACTIVATED_AS_ TYPE</p>
</blockquote></td>
<td>704.1122,.14</td>
<td><p>SET</p>
<p>'0' FOR Mandatory;</p>
<p>'<strong>1' FOR Optional;</strong></p>
<p>'2' FOR</p>
<p>Supplemental;</p></td>
<td>This indicates a purpose for the activation of this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEACTIVATED_ DATE_TIME</p>
</blockquote></td>
<td>704.1122,.21</td>
<td>DATE</td>
<td>This is the date/time this supplemental page (#.01) was deactivated.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEACTIVATED_ BY_ID</p>
</blockquote></td>
<td>704.1122,.22</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that deactivated this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEACTIVATED_ COMMENT</p>
</blockquote></td>
<td>704.1122,.23</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td><p>This is a user supplied comment stored when this supplemental page (#.01) is deactivated. A sample DEACTIVATED COMMENT</p>
<p>could be "patient/treatment is no longer applicable".</p></td>
</tr>
</tbody>
</table>

> <span id="_bookmark41" class="anchor"></span>1OBS_FLOWSHEET_TOTAL File (#704.1123)

> This file maintains flowsheets (file \#704.112) and observation totals (file \#704.113) relationships.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FLOWSHEET_ID</p>
</blockquote></td>
<td>704.1123,.01</td>
<td><p>POINTER TO OBS_FLOWSHEE T FILE (#704.11 2)</p>
<p>(Key field)</p></td>
<td>This identifies the flowsheet file entry for this flowsheet total entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL_ID</p>
</blockquote></td>
<td>704.1123,.02</td>
<td>POINTER TO OBS_TOTAL FILE (#704.113)</td>
<td>This identifies an observation total file entry to correlate with this flowsheet total entry.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL_ORDER</p>
</blockquote></td>
<td>704.1123,.03</td>
<td><p>NUMBER</p>
<p>(Between 1 and 99)</p></td>
<td>This field determines the order in which this flowsheet total will be executed and displayed.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark42" class="anchor"></span>1OBS_TOTAL File (#704.113)

> This file maintains observation totals.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.113,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td><p>This field is a unique IDentifier for this TOTAL. This ID is maintained nationally so it identifies this TOTAL throughout the enterprise. A sample ID could be</p>
<p>"{217D131C-13C3-4B9E-A401- D1345766182B}".</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>704.113,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a descriptive NAME for this total (#.01). A sample name could be "OUTTAKE TOTALS".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_NAME</p>
</blockquote></td>
<td>704.113,.03</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a user friendly name. This is used when displaying this total via the Clinical Flowsheets application. A sample DISPLAY NAME could be "New Flowsheet Outtake Total".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEFAULT_UNIT</p>
</blockquote></td>
<td>704.113,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the measurement-unit to be used with the observation total (#.01). The DEFAULT UNIT is an entry in the TERM (#704.101) file. A sample DEFAULT UNIT could identify the term "lbs" or "pounds".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DECIMAL_PRECI SION</p>
</blockquote></td>
<td>704.113,.05</td>
<td><p>NUMBER (1-8</p>
<p>Number Precision)</p></td>
<td>This is the decimal precision to round the total values to.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.113,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This indicates whether this total (#.01) can be used by the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.113,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This is a descriptive COMMENT about this total (#.01) entry. A sample COMMENT could be "New totaling apparatus for OUTTAKE totals - default lbs ".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_TOTAL</p>
</blockquote></td>
<td>704.113,.201</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display a total of all observations.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_COUNT</p>
</blockquote></td>
<td>704.113,.202</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display a count of observations.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_AVERA GE</p>
</blockquote></td>
<td>704.113,.203</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the average of all observations.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_DIFFER ENCE</p>
</blockquote></td>
<td>704.113,.204</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>(Future Use.)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_RATIO</p>
</blockquote></td>
<td>704.113,.205</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>(Future Use.)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISPLAY_MINIM UM</p>
</blockquote></td>
<td>704.113,.206</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the least value registered of all observations.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISPLAY_MAXI MUM</p>
</blockquote></td>
<td>704.113,.207</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the greatest value registered of all observations.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark43" class="anchor"></span>1OBS_TOTAL_TERMINOLOGY File (#704.1131)

> This maintains relationships between OBS TOTAL file (#704.113) entries and TERM file (#704.101) entries.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TOTAL_ID</p>
</blockquote></td>
<td>704.1131,.01</td>
<td>POINTER TO OBS_TOTAL FILE (#704.113)</td>
<td>This identifies the observation total portion of this total-terminology entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.1131,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the term portion of this total- terminology entry.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_ORDER</p>
</blockquote></td>
<td>704.1131,.03</td>
<td><p>NUMBER (Key</p>
<p>field)</p></td>
<td>This field indicates the display order of this term (#.02) within this observation total (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TERM_DISPLAY_ NAME</p>
</blockquote></td>
<td>704.1131,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name to display within the Clinical Flowsheets application for this total terminology entry. A sample TERM DISPLAY NAME could be "TOTs IntakeX".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark44" class="anchor"></span>1OBS_ALARM File (#704.115)

> This file supports the Clinical Flowsheets application "alarm" functionality. And the file maintains the relationships between alarms and patients.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.115,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is a Global Unique IDentifier (GUID) for this alarm. The GUID is maintained nationally so this value represents this item throughout the enterprise.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT_ID</p>
</blockquote></td>
<td>704.115,.02</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the patient for which this alarm (#.01) is applicable.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.115,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This is the term to be monitored when the Clinical Flowsheets application determines whether to signal an alarm.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>UNIT_ID</p>
</blockquote></td>
<td>704.115,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the unit of measurement to use when Clinical Flowsheets compares observed and "alarm" values.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALARM_TYPE</p>
</blockquote></td>
<td>704.115,.05</td>
<td><p>SET</p>
<p>0' FOR Value in range;</p>
<p>1' FOR Value not in range;</p>
<p>2' FOR Value greater than;</p>
<p>3' FOR Value less than;</p>
<p>4' FOR Value in Picklist;</p>
<p>5' FOR Value is True;</p>
<p>6' FOR Value is False;</p></td>
<td>This indicates the case, when satisfied by an observed value, for the assigned patient and term that may cause the Clinical Flowsheets application to trigger the alarm (#01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MIN_VALUE</p>
</blockquote></td>
<td>704.115,.06</td>
<td><p>NUMBER (Number between - 999999999 and</p>
<p>999999999)</p></td>
<td>This field is the minimum value for this term (#.03) and unit (#.04) that will not trigger the alarm (#.01).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAX_VALUE</p>
</blockquote></td>
<td>704.115,.07</td>
<td><p>NUMBER (Number between - 999999999 and</p>
<p>999999999)</p></td>
<td>This field is the maximum value for this term (#.03) and unit (#.04) that will not trigger alarm.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALARM_SET</p>
</blockquote></td>
<td>704.115,.08</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This indicates whether this alarm's (#.01) conditions are satisfied.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 February 2010 File description added.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td>704.115,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This indicates if this alarm (#.01) logic is to be executed on new values (reset).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVATED_DA TE_TIME</p>
</blockquote></td>
<td>704.115,.11</td>
<td>DATE</td>
<td>This field is the date/time this alarm (#.01) is to be activated.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACTIVATED_BY_ ID</p>
</blockquote></td>
<td>704.115,.12</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that activated this alarm (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEACTIVATED_ DATE_TIME</p>
</blockquote></td>
<td>704.115,.13</td>
<td>DATE</td>
<td>This is the date/time this alarm (#.01) is to be deactivated.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEACTIVATED_ BY_ID</p>
</blockquote></td>
<td>704.115,.14</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that deactivated this alarm (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVATED_CO MMENT</p>
</blockquote></td>
<td>704.115,.2</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is the comment entered when this alarm (.01) was activated. A sample ACTIVATED COMMENT could be "Alarm activated for automated monitoring".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEACTIVATED_ COMMENT</p>
</blockquote></td>
<td>704.115,.3</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td><p>This is the comment entered when this alarm (.01) was deactivated. A sample DEACTIVATED COMMENT could be</p>
<p>"Alarm deactivated for staff monitoring".</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PICKLIST_IDS</p>
</blockquote></td>
<td>704.115,.4</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td><p>This field is a list of VA Unique IDentifiers for a "picklist-type" observation. A sample PICKLIST IDS could be: "{65069804-39BF- 41ED-9EA3-BF2C41389F10},{715091C 2-</p>
<p>9668-4678-900E-</p>
<p>6D55D3335A30},{D5B3E135-4D68-4528- BBC9-6E8A7A997104}"</p></td>
</tr>
</tbody>
</table>

### 1OBS_SET File (#704.116)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains sets of observations used by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SET_ID</p>
</blockquote></td>
<td>704.116,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample SET ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENTERED_DATE</p>
<p>_TIME</p>
</blockquote></td>
<td>704.116,.02</td>
<td>DATE</td>
<td>This field is the date/time this set (#.01) was created.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENTERED_BY_ID</p>
</blockquote></td>
<td>704.116,.03</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This field identifies the person (file #200) that created this set (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PUBLIC</p>
</blockquote></td>
<td>704.116,.04</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>(Future use - indicate whether this is used by other applications / public.)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.116,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is the user supplied COMMENT about the purpose of this set (.01). A sample COMMENT could be "Auto-Generated Set".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COUNT</p>
</blockquote></td>
<td>704.116,.911</td>
<td>COMPUTED</td>
<td>This is the number of observations assigned to this set (#.01).</td>
</tr>
</tbody>
</table>

> <span id="_bookmark46" class="anchor"></span>1OBS_SET_OBS_PAIR File (#704.1161)

> This file maintains the relationships between observations and observation sets.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SET_ID</p>
</blockquote></td>
<td>704.1161,.01</td>
<td>POINTER TO OBS_SET FILE (#704.116)</td>
<td>This identifies the set file (#704.116) entry part of this set-observation pair.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>OBS_ID</p>
</blockquote></td>
<td>704.1161,.02</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation file (#704.117) entry part of this set-observation pair.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### 1OBS File (#704.117)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains observations for use with the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OBS_ID</p>
</blockquote></td>
<td>704.117,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is a Globally Unique IDentifier (GUID) for this entry. This is maintained nationally so it is the same throughout the enterprise. A sample OBS ID could be "{69DBD11E-9A8C- 4ECE-AFA4-73947218807D}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PARENT_ID</p>
</blockquote></td>
<td>704.117,.02</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the parent observation in the case of a complex observation.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FACILITY_ID</p>
</blockquote></td>
<td>704.117,.03</td>
<td>POINTER TO DOMAIN FILE (#4.2)</td>
<td>This identifies the domain (file #4.2) relevant to this observation (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>HOSPITAL_LOCA TION_ID</p>
</blockquote></td>
<td>704.117,.04</td>
<td>POINTER TO HOSPITAL LOCATION FILE (#44)</td>
<td>This identifies the hospital location (file #44) relevant to this observation (#.01).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OBSERVED_DAT E_TIME</p>
</blockquote></td>
<td>704.117,.05</td>
<td>DATE</td>
<td>This is the date/time this observation (#.01) took place.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>OBSERVED_BY_I D</p>
</blockquote></td>
<td>704.117,.06</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that made this observation.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TERM_ID</p>
</blockquote></td>
<td>704.117,.07</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the type of observation. This "type" is an entry in the TERM File (#704.101). A sample TERM ID here could reference the term "SYSTOLIC PRESSURE".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT_ID</p>
</blockquote></td>
<td>704.117,.08</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the PATIENT (file #2) for whom this observation (#.01) was taken.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td>704.117,.09</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Removed;</p></td>
<td>This field indicates the current status of this observation (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SVALUE</p>
</blockquote></td>
<td>704.117,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This field represents the value of the observation (#.01). A sample SVALUE could be "122/55".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOURCE</p>
</blockquote></td>
<td>704.117,.21</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This field is the source of the SVALUE (#.1). A sample SOURCE could be "instrument" or "CP Flowsheets".</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SOURCE_COMME NTS</p>
</blockquote></td>
<td>704.117,.22</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td><p>This is any comment type information generated by the source about this observation (#.01). A sample SOURCE COMMENTS</p>
<p>could be "Routine MDZCLIO Tag BUILD".</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SOURCE_DATA_I TEM_ID</p>
</blockquote></td>
<td>704.117,.23</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This field contains source (#.21) generated information for later tagging. A sample SOURCE DATA ITEM ID could be "CPFLOWSHEETS.EXE:C13A6427".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOURCE_VERSIO N</p>
</blockquote></td>
<td>704.117,.24</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This is the version of the source (#.21) that generated this observation (#.01). A sample SOURCE VERSION could be “1.0".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENTERED_DATE</p>
<p>_TIME</p>
</blockquote></td>
<td>704.117,.25</td>
<td>DATE</td>
<td>This is the date and time this entry was placed into this observation file.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENTERED_BY_ID</p>
</blockquote></td>
<td>704.117,.26</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) who entered the data for this observation (#.01).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILD_ORDER</p>
</blockquote></td>
<td>704.117,.27</td>
<td>NUMBER (Number 1 - 999)</td>
<td>This is the order that this observation is placed into its parent observation (#.02).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RANGE</p>
</blockquote></td>
<td>704.117,.28</td>
<td><p>SET</p>
<p>'0' FOR Unknown;</p>
<p>'1' FOR Normal; '2' FOR Out Of</p>
<p>Bounds Low; '3' FOR Out Of</p>
<p>Bounds High; '4' FOR Low;</p>
<p>'5' FOR High;</p></td>
<td>This indicates the condition of the observation value (#.1).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.117,.4</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text for additional clinical COMMENT. A sample COMMENT could be "test O2 saturation".</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUDIT_EXISTS</p>
</blockquote></td>
<td>704.117,.911</td>
<td>COMPUTED</td>
<td>This indicates whether or not any record exists in the audit log for this observation.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CORRECTION_FO R_ID</p>
</blockquote></td>
<td>704.117,.912</td>
<td>COMPUTED</td>
<td>This identifies the record this observation was entered to correct.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark48" class="anchor"></span>1OBS_QUALIFIER File (#704.118)

> This file maintains relationships between observations and qualifiers.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OBS_ID</p>
</blockquote></td>
<td>704.118,.01</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation part of this observation/qualifier pair.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>QUALIFIER_ID</p>
</blockquote></td>
<td>704.118,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the qualifier part of this observation/qualifier pair.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark49" class="anchor"></span>1OBS_AUDIT File (#704.119)

> This file maintains the chains of observation audits for Clinical Flowsheets observations. An audit is defined here as a change in an observation's status, state, or condition.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AUDIT_ID</p>
</blockquote></td>
<td>704.119,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample AUDIT ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUDIT_TYPE</p>
</blockquote></td>
<td>704.119,.02</td>
<td><p>SET</p>
<p>'0' FOR Record Status Update; '1' FOR Record Verified;</p>
<p>'2' FOR Record Marked For Purging;</p>
<p>'3' FOR Record Marked For Archiving;</p>
<p>'4' FOR Record Corrected;</p>
<p>'5' FOR Record Rescinded;</p></td>
<td>This indicates the type of audit; the reason for the audit.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUDIT_OBSERV ATION</p>
</blockquote></td>
<td>704.119,.03</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation that has been audited via this entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUDIT_DATE_TI ME</p>
</blockquote></td>
<td>704.119,.04</td>
<td>DATE</td>
<td>This is the date/time this audit occurred.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUDIT_AUTHOR</p>
</blockquote></td>
<td>704.119,.05</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that created this audit entry.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>STATUS_ORIGIN AL</p>
</blockquote></td>
<td>704.119,.06</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Rescinded;</p></td>
<td>This indicates the status/condition of the observation (#.03) before this audit entry (#.01) was created.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>STATUS_NEW</p>
</blockquote></td>
<td>704.119,.07</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Rescinded;</p></td>
<td>This indicates the status/condition of the observation (#.03) after this audit entry (#.01) was created.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>REPLACEMENT_ OBSERVATION</p>
</blockquote></td>
<td>704.119,.08</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation that was replaced by a new observation via this audit.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.119,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is a COMMENT provided by the person as documentation per this observation audit (#.01). A sample COMMENT could be "Verified with Clinical Flowsheets".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark50" class="anchor"></span>1CP_KARDEX_ACTION File (#704.121)

> This file supports Clinical Flowsheets scheduled tasks and actions functionality.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td>704.121,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TASK_ID</p>
</blockquote></td>
<td>704.121,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies a task in the TERM File (#704.101).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCHEDULE_ID</p>
</blockquote></td>
<td>704.121,.03</td>
<td>POINTER TO CP_SCHEDULE FILE (#704.008)</td>
<td>This identifies the schedule (#704.008) to use with the task (#.02).</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT_ID</p>
</blockquote></td>
<td>704.121,.04</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This field identifies the patient (file #2) assigned to this task.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>START_DATE_TI ME</p>
</blockquote></td>
<td>704.121,.05</td>
<td>DATE</td>
<td>This is the date/time the execution of this task is permitted.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>STOP_DATE_TIM E</p>
</blockquote></td>
<td>704.121,.06</td>
<td>DATE</td>
<td>This is the date/time the execution of this task is no longer permitted.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCHEDULE_TYPE</p>
</blockquote></td>
<td>704.121,.07</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; '1' FOR PRN;</p>
<p>'2' FOR One-Time;</p>
<p>'3' FOR Stat;</p>
<p>'4' FOR Now;</p></td>
<td>This field indicates the type of schedule used for this task.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRN_TYPE</p>
</blockquote></td>
<td>704.121,.08</td>
<td><p>SET</p>
<p>'0' FOR No PRN; '1' FOR PRN-And;</p>
<p>'2' FOR PRN- AndNTE;</p>
<p>'3' FOR PRN-Or;</p></td>
<td>This field indicates the Pro Re Nata (PRN) option for task.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td>704.121,.09</td>
<td><p>SET</p>
<p>'0' FOR Active;</p>
<p>'1' FOR Expired;</p>
<p>'2' FOR</p>
<p>Discontinued; '3' FOR Held;</p></td>
<td>This field indicates the status of the task.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SPECIAL_INSTRU CTIONS</p>
</blockquote></td>
<td>704.121,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text for instructions for this particular task. A sample SPECIAL INSTRUCTIONS could be "Turn patient 90 degrees".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRN_NTE_AMOU NT</p>
</blockquote></td>
<td>704.121,.21</td>
<td>NUMBER (Number 1 - 999)</td>
<td>This field the maximum number of times this task should executed. This field is used in the case of tasks with a PRN option.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FIRST_SCHEDUL ED_TIME</p>
</blockquote></td>
<td>704.121,.22</td>
<td><p>FREE TEXT (1 – 4</p>
<p>char)</p></td>
<td>This is the military time of the first time that this item should be executed once the start date/time has been reached. A sample FIRST SCHEDULED TIME could be "1330" to represent "01:30 PM" as the first time this task should be executed.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CUSTOM_SCHED ULED_TIMES</p>
</blockquote></td>
<td>704.121,.3</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This field is a custom schedule. If the user wished to modify the schedule for this task (#.02), the schedule here in a military times. A sample CUSTOM SCHEDULED TIMES could be "0400,0800,1200,1600,2000".</td>
</tr>
</tbody>
</table>

> <span id="_bookmark51" class="anchor"></span>1CP_KARDEX_EVENTS File (#704.1211)

> This file supports Clinical Flowsheets scheduled events/actions functionality.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EVENT_ID</p>
</blockquote></td>
<td>704.1211,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is a Globally Unique IDentifier (GUID) for this entry. This is maintained nationally so it is the same throughout the enterprise. A sample EVENT ID could be "{69DBD11E- 9A8C-4ECE-AFA4-73947218807D}".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CARE_ACTION_I D</p>
</blockquote></td>
<td>704.1211,.02</td>
<td>POINTER TO CP_KARDEX_AC TION FILE (#704.121)</td>
<td>This identifies the action (#704.121) to which this event will be assigned.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DUE_DATE_TIME</p>
</blockquote></td>
<td>704.1211,.03</td>
<td>DATE</td>
<td>This is the date/time this event is scheduled to be executed.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMPLETED_DA TE_TIME</p>
</blockquote></td>
<td>704.1211,.04</td>
<td>DATE</td>
<td>This is the date/time this event was actually done.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMPLETED_BY</p>
<p>_ID</p>
</blockquote></td>
<td>704.1211,.05</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) who marked this event as completed.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td>704.1211,.09</td>
<td><p>SET</p>
<p>'0' FOR PENDING;</p>
<p>'1' FOR COMPLETED; '2' FOR HELD;</p>
<p>'3' FOR REFUSED;</p></td>
<td>This indicates the status, condition, or state of this event.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMENT</p>
</blockquote></td>
<td>704.1211,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is a free-text, user entered COMMENT for this event. A sample COMMENT could be "This event was completed on time. It was entered late".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUDIT_COUNT</p>
</blockquote></td>
<td>704.1211,.991</td>
<td>COMPUTED</td>
<td>This is a calculated count of the number of audits for this event.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark52" class="anchor"></span>1CP_KARDEX_AUDIT File (#704.1212)

> This file maintains audits of scheduled event/tasks via the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><strong>Field Number</strong></th>
<th><strong>Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACTION_ID</p>
</blockquote></td>
<td>704.1212,.01</td>
<td>POINTER TO CP_KARDEX_AC TION FILE (#704.121)</td>
<td>This identifies the audited scheduled task.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVENT_ID</p>
</blockquote></td>
<td>704.1212,.02</td>
<td>POINTER TO CP_KARDEX_EV ENTS FILE (#704.1211)</td>
<td>This identifies the audited event.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUDIT_DATE_TI ME</p>
</blockquote></td>
<td>704.1212,.03</td>
<td>DATE</td>
<td>This is the date/time that the audit record is created.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUDIT_BY_ID</p>
</blockquote></td>
<td>704.1212,.04</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that created this audit.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUDIT_DESCRIP TION</p>
</blockquote></td>
<td>704.1212,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text automatically generated by the Clinical Flowsheets application when an audit is created. A sample could be AUDIT DESCRIPTION "Event placed in Hold Status".</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUDIT_COMMEN T</p>
</blockquote></td>
<td>704.1212,.2</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text generated by the user (#.04) when creating this audit. A sample AUDIT COMMENT could be "Provider action required a hold".</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

## Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" rowspan="2"></th>
<th><blockquote>
<p>UP</p>
</blockquote></th>
<th>SEND</th>
<th>DATA</th>
<th></th>
<th></th>
<th>USER</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th>SEC.</th>
<th>COMES</th>
<th>SITE</th>
<th>RSLV</th>
<th>OVER</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FILE #</td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td>CODE</td>
<td>W/FILE</td>
<td>DATA</td>
<td>PTS</td>
<td>RIDE</td>
</tr>
<tr class="even">
<td>702</td>
<td><blockquote>
<p>CP TRANSACTION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1702.001</td>
<td><blockquote>
<p>CP_TRANSACTION_TIU_HISTORY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
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
<td>702.01</td>
<td><blockquote>
<p>CP DEFINITION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>702.09</td>
<td><blockquote>
<p>CP INSTRUMENT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td>ADD</td>
<td>NO</td>
<td>NO</td>
</tr>
<tr class="even">
<td>703.1</td>
<td><blockquote>
<p>CP RESULT REPORT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2703.9</td>
<td><blockquote>
<p>CP CONVERSION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
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
<td>3704.001</td>
<td><blockquote>
<p>CP_CONSOLE_ACL</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.002</td>
<td><blockquote>
<p>CP_HL7_LOG</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.004</td>
<td><blockquote>
<p>CP_HL7_LOG_REASON</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.005</td>
<td><blockquote>
<p>CP_MOVEMENT_AUDIT</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.006</td>
<td><blockquote>
<p>CP_PROTOCOL_LOCATION</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.007</td>
<td><blockquote>
<p>CP_SHIFT</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.008</td>
<td><blockquote>
<p>CP_SCHEDULE</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.101</td>
<td><blockquote>
<p>TERM</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.102</td>
<td><blockquote>
<p>TERM_TYPE</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>REPL</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="odd">
<td>704.103</td>
<td><blockquote>
<p>TERM_QUALIFIER_PAIR</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.104</td>
<td><blockquote>
<p>TERM_UNIT_CONVERSION</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.105</td>
<td><blockquote>
<p>TERM_UNIT_PAIR</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.106</td>
<td><blockquote>
<p>TERM_CHILD_PAIR</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.107</td>
<td><blockquote>
<p>TERM_RANGE_CHECK</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.108</td>
<td><blockquote>
<p>TERM_MAPPING_TABLE</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.109</td>
<td><blockquote>
<p>TERM_MAPPING_PAIR</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.111</td>
<td><blockquote>
<p>OBS_VIEW</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.1111</td>
<td><blockquote>
<p>OBS_VIEW_TERMINOLOGY</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.1112</td>
<td><blockquote>
<p>OBS_VIEW_FILTER</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.112</td>
<td><blockquote>
<p>OBS_FLOWSHEET</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.1121</td>
<td><blockquote>
<p>OBS_FLOWSHEET_PAGE</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.1122</td>
<td><blockquote>
<p>OBS_FLOWSHEET_SUPP_PAGE</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.1123</td>
<td><blockquote>
<p>OBS_FLOWSHEET_TOTAL</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.113</td>
<td><blockquote>
<p>OBS_TOTAL</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.1131</td>
<td><blockquote>
<p>OBS_TOTAL_TERMINOLOGY</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.115</td>
<td><blockquote>
<p>OBS_ALARM</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.116</td>
<td><blockquote>
<p>OBS_SET</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.1161</td>
<td><blockquote>
<p>OBS_SET_OBS_PAIR</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.117</td>
<td><blockquote>
<p>OBS</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.118</td>
<td><blockquote>
<p>OBS_QUALIFIER</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.119</td>
<td><blockquote>
<p>OBS_AUDIT</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.121</td>
<td><blockquote>
<p>CP_KARDEX_ACTION</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.1211</td>
<td><blockquote>
<p>CP_KARDEX_EVENTS</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.1212</td>
<td><blockquote>
<p>CP_KARDEX_AUDIT</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.201</td>
<td><blockquote>
<p>HEMODIALYSIS ACCESS POINTS</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>704.202</td>
<td><blockquote>
<p>HEMODIALYSIS STUDY</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>704.209</td>
<td><blockquote>
<p>HEMODIALYSIS SETTINGS</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 1Patch MD\*1.0\*6 May 2008 Default definitions added for 702.001, 704.201, 704.202, and 704.209.

> 2Patch MD\*1.0\*5 August 2006 Default definitions added for 703.9.

> 3 Patch MD\*1.0\*16 January 2011 Default definitions added for 704,001 - 704.1212.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Delphi Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Procedures uses RPC Broker and custom Delphi Components in the display and navigation of screens. Below is a list of the Delphi components this application currently uses along with a short description.

> TMDRecordSource = class(TComponent)

> This is the primary component that all others interact with. This component represents a record within FileMan via the Data Dictionary Number and the IEN. In the event that the record is a sub-file then this component will point to another TMDRecordSource that represents the parent record of the sub-record. There is no limit to the number of sub- records that can be linked together.

> TMDEdit = Class(TEdit)

> This component is designed to manage FileMan Free-Text and Numeric type fields. Other types may be used here with the exception of word-processing but they will require exact data input (i.e. non-ambiguous entries must be entered in the case of pointers or set of codes types). All input and output transforms are applied to the field on validation.

> TMDEditPointer = Class(TComboBox)

> This component is designed to manage FileMan Pointer types. This component currently handles screens via hard coded screens on the server side in routine MDRPCOR.

> TMDLabel = Class(TLabel)

> This component is a static component that can display one of three data elements for a FileMan field. These are 1) Data value 2) Field Title or 3) Field Help Text. There is no server update associated with this component.

> TMDMemo = Class(TMemo)

> This component manages FileMan word-processing data types only. It will validate the data upon leaving the component.

> TMDComboBox = Class(TComboBox)

> This component was designed for either set of codes or pointer type fields. If using a pointer type field the developer must be aware that the entire pointed to file will be retrieved so large files such as the Patient file (#2) is not possible to represent with this component. Files such as the State file (#5) are handled quite well if there are approximately 100 or less entries and the pointed to file does not have complex output transforms on the .01 field.

> TMDRadioGroup = Class(TRadioGroup)

> This field was designed specifically for the FileMan set of codes field. It loads the appropriate codes into the radio group and displays the “Stands For‟ portion of the codes while storing to the database the internal value of the code.

> TMDCheckBox = Class(TCheckBox)

> This component was designed for a set of codes that are restricted to only two codes (i.e. Yes/No, True/False, On/Off).

> Remote Procedure Calls (RPC)

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

> Contains the option for the RPC. RPC is called as shown: Options and other required parameters include:

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

1.  The internal variable pointer (nnn;GLO(123,)
2.  The external format of the variable pointer using the 3 character prefix (prefix.entryname)
3.  The prefix alone to set the parameter based on current entity selected. (prefix)

> Method 3 uses the following values for the following entities: USR Current value of DUZ

> DIV Current value of DUZ(2) SYS System (domain)

> PKG Package to which the parameter belongs

> INPUT PARAMETER: PAR PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: NO

> SEQUENCE NUMBER: 3 DESCRIPTION:

> A parameter is the actual name which values are stored under. The name of the parameter must be namespaced and it must be unique. Parameters can be defined to store the typical package parameter data (e.g. the default add order screen), but they can also be used to store GUI application screen settings a user has selected (e.g. font or window width). When a parameter is defined, the entities, which may set that parameter, are also defined. The definition of parameters is stored in the PARAMETER DEFINITION file (#8989.51).

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

> MAXIMUM DATA LENGTH: 20 REQUIRED: NO

> SEQUENCE NUMBER: 3 DESCRIPTION:

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

> 1NAME: MD TMDCIDC TAG: RPC

> ROUTINE: MDRPCW RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This RPC will do the following:

> 1 Patch MD\*1.0\*6 May 2008 RPCs added.

> Input Parameter: RESULTS - (Both Input/Output) Passed in as the array to

> return the results.

> OPTION - (Input) PROC - obtain a list of Procedures

> defined for a clinic.

> DIAG - obtain a list of diagnosis defined for a clinic.

> SCDISP - Obtain the patient's service connection and rated

> disability.

> DFN - (Input) Patient internal entry number MDSTUD - (Input) CP Study internal entry number

> RETURN PARAMETER DESCRIPTION:

- D RPC^MDRPCW(.RESULTS,"PROC",162,212)
- ZW RESULTS RESULTS=^TMP("MDRPCW",539023945)

> @RESULTS@(0)=count of array element (0 if nothing found) @RESULTS@(1)=^group header

> @RESULTS@(2) = P1 := cpt or icd code / ien of other items P2 := user defined text

> P6 := user defined expanded text to send to PCE P7 := second code or item defined for line item P8 := third code or item defined for line item P9 := associated clinical lexicon term

- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,0) = 7

> ^TMP("MDRPCW",539023945,1) = ^PFT PROCEDURES

> ^TMP("MDRPCW",539023945,2) = G0125^Lung image (PET) ^^^^^^^

> ^TMP("MDRPCW",539023945,3) = S9473^Pulmonary rehabilitation pro^^^^^^^

> ^TMP("MDRPCW",539023945,4) = S2060^Lobar lung transplantation ^^^^^^^

> ^TMP("MDRPCW",539023945,5) = S2060^Lobar lung transplantation ^^^^^^^

> ^TMP("MDRPCW",539023945,6) = A4480^Vabra aspirator ^^^^^^^

> ^TMP("MDRPCW",539023945,7) = 43450^DILAT ESOPH-SOUND/BOUGIE-1/M^^^^^^^

> Global ^

- D RPC^MDRPCW(.RESULTS,"DIAG",162,212)
- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,0) = 31

> ^TMP("MDRPCW",539023945,1) = ^PFT

> ^TMP("MDRPCW",539023945,2) = 397.1^RHEUM PULMON VALVE DIS^^^^^^^269587

> ^TMP("MDRPCW",539023945,3) = 417.1^PULMON ARTERY ANEURYSM^^^^^^^269688

> ^TMP("MDRPCW",539023945,4) = 417.8^PULMON CIRCULAT DIS NEC^^^^^^^269690

> ^TMP("MDRPCW",539023945,5) = 417.9^PULMON CIRCULAT DIS NOS^^^^^^^269691

> ^TMP("MDRPCW",539023945,6) = 424.3^PULMONARY VALVE DISORDER^^^^^^^101164

> ^TMP("MDRPCW",539023945,7) = 516.1^IDIO PULM HEMOSIDEROSIS^^^^^^^61083

> ^TMP("MDRPCW",539023945,8) = 746.01^CONG PULMON VALV ATRESIA^^^^^^^265805

> ^TMP("MDRPCW",539023945,9) = 673.82^PULM EMBOL NEC-DEL W P/P^^^^^^^271756

> ^TMP("MDRPCW",539023945,10) = 747.3^PULMONARY ARTERY ANOM^^^^^^^27406

> ^TMP("MDRPCW",539023945,11) = 770.3^NB PULMONARY HEMORRHAGE^^^^^^^273240

> ^TMP("MDRPCW",539023945,12) = 794.2^ABN PULMONARY FUNC STUDY^^^^^^^273442

> ^TMP("MDRPCW",539023945,13) = 901.41^INJURY PULMONARY ARTERY^^^^^901.42^^275136

> ^TMP("MDRPCW",539023945,14) = 162.3^MAL NEO UPPER LOBE LUNG^^^^^162.4^162.5^73534

> ^TMP("MDRPCW",539023945,15) = 235.7^UNC BEHAV NEO LUNG^^^^^^^267754

> ^TMP("MDRPCW",539023945,16) = 875.0^OPEN WOUND OF CHEST^^^^^^^274991

> ^TMP("MDRPCW",539023945,17) = 162.9^MAL NEO BRONCH/LUNG NOS^^^^^^^73521

> ^TMP("MDRPCW",539023945,18) = 786.6^CHEST SWELLING/MASS/LUMP^^^^^^^273380

> ^TMP("MDRPCW",539023945,19) = 518.89^OTHER DISEASE OF LUNG, NEC^^^^^^^87486

> ^TMP("MDRPCW",539023945,20) = ^BRONCHOSCOPY

> ^TMP("MDRPCW",539023945,21) = 012.20^ISOL TRACHEAL TB- UNSPEC^^^^^012.21^^266107

> ^TMP("MDRPCW",539023945,22) = 012.22^ISOL TRACH TB-EXAM UNKN^^^^^^^266109

> ^TMP("MDRPCW",539023945,23) = 012.23^ISOLAT TRACH TB-MICRO DX^^^^^^^266110

> ^TMP("MDRPCW",539023945,24) = 012.24^ISOL TRACHEAL TB-CULT DX^^^^^^^266111

> ^TMP("MDRPCW",539023945,25) = 748.61^CONGEN BRONCHIECTASIS^^^^^^^265478

> ^TMP("MDRPCW",539023945,26) = 011.50^TB BRONCHIECTASIS- UNSPEC^^^^^011.51^^266056

> ^TMP("MDRPCW",539023945,27) = 784.1^THROAT PAIN^^^^^^^276881

> ^TMP("MDRPCW",539023945,28) = 784.8^HEMORRHAGE FROM THROAT^^^^^^^273371

> ^TMP("MDRPCW",539023945,29) = 034.0^STREP SORE THROAT^^^^^^^114610

> ^TMP("MDRPCW",539023945,30) = 466.11^AC. BRONCH/RESP SYNCYT V

> (RSV)^^^^^466.19^

> ^304309

> ^TMP("MDRPCW",539023945,31) = 530.10^ESOPHAGITIS, UNSP.^^^^^^^295809

> Global ^

- D RPC^MDRPCW(.RESULTS,"SCDISP",17,212)

> @RESULTS@(n)="Lines of text"

- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,1) = Service Connected: 50%

> ^TMP("MDRPCW",539023945,2) = Rated Disabilities: NONE STATED

> Global ^

> NAME: MD TMDENCOUNTER TAG: GETENC

> ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This remote procedure will return the existing data in an encounter. INPUT PARAMETER: STUDY PARAMETER TYPE: REFERENCE

> REQUIRED: YES SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the CP Study internal entry number. RETURN PARAMETER DESCRIPTION:

> The result is returned in ^TMP("MDENC",\$J) global.

> ^TMP("MDENC",\$J,1)="SC";0/1^0/1;"AO";0/1^0/1;"IR";0/1^0/1;"EC";0/1^0/ 1;"MST";0/1^0/1;"HNC";0/1^0/1;"CV";0/1^0/1

> P1 = "SC" - Service Connected

> P2 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P3 = "AO" - Agent Orange Exposure

> P4 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P5 = "IR" - Ionizing Radiation Exposure

> P6 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P7 = "EC" - Environmental Contaminants

> P8 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P9 = "HNC" - Head and/or Neck Cancer

> P10 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P11 = "MST" - Military Sexual Trauma

> P12 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P13 = "CV" - Combat Veteran

> P14 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

> ^TMP("MDENC",\$J,n)="PRV"^CODE^^NARR^^Primary (1=Yes,0=No) P1 = "PRV"- Provider segment

> P2 = CODE - New Person internal Entry Number P3 = Null

> P4 = NARR - Provider name P5 = Null

> P6 = Primary - 1/0/null (1=Yes,0/Null=No)

> ="POV"^ICD9 IEN^ICD9 CODE^provider narrative category^ provider narrative (Short Description)^Primary (1=Yes,0/Null=No)

> P1 = "POV" - ICD segment

> P2 = ICD internal entry number P3 = ICD9 Code

> P4 = Provider Narrative Category P5 = Short Description

> P6 = Primary - 1/0/null (1=Yes,0/Null=No)

> ="CPT"^CPT IEN^CPT CODE^provider narrative category^ provider narrative (Short Description)^^Quantity

> P1 = "CPT" - CPT segment

> P2 = CPT internal entry number P3 = CPT Code

> P4 = Provider Narrative Category (CPT Category Grouping) P5 = Short Description

> P6 = null

> P7 = Quantity

> NAME: MD TMDLEX TAG: LEX

> ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This RPC will return a list of CPT or ICD for a search typed in. INPUT PARAMETER: MDSRCH PARAMETER TYPE: REFERENCE

> REQUIRED: YES SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the text typed in for the look-up.

> INPUT PARAMETER: MDAPP PARAMETER TYPE: REFERENCE REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is the application indicator. It is either "CPT" or "ICD". RETURN PARAMETER DESCRIPTION:

> ^TMP("MDLEX",\$J,#)=P1 - CPT/ICD Code

> P2 - Internal Entry Number P3 - Lexicon text

> \>D LEX^MDRPCW1(.RESULTS,"BORE","CPT")

> \>ZW RESULTS RESULTS="^TMP("MDLEX",539152953)"

> \>D ^%G

> Global ^TMP("MDLEX",\$J -- NOTE: translation in effect

> ^TMP("MDLEX",539152953,1)=86618^302213^Borella Burgdorferi (Lyme Disease) Antibody (CP T-4 86618)

> NAME: MD TMDNOTE TAG: RPC

> ROUTINE: MDRPCNT RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This remote procedure call does the following:

> Accepts the following Inputs:

> RESULTS - Both (Input and Output) - Passed in as the array to return results in.

> OPTION - NEWDOC = Add additional new document to the Hemodialysis study.

> NOTELIST = Returns a list of documents associated with the study. The pieces returned are: Note IEN, Note title, Date/Time Creation, Author, and Hospital Location.

> VIEWTIU = Return the text lines of a document from NOTELST. MDSID - Study internal Entry Number.

> MDTIU - TIU Document Internal Entry Number. MDDTE - Date/Time of Document Creation.

> MDAUTH - Author of document.

> MDESIG - Encrypted Electronic Signature. MDTXT - Text of the new document in an array.

> Return Results are the following:

> OPTION = NEWDOC

- D RPC^MDRPCNT(.RESULTS,"NEWDOC",904,"",3050524.0915,679,74RHLld;flk,MDTXT)
- D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

> ^TMP("MDKUTL",538992716,0) = Note internal entry number or -1^Error Message OPTION = NOTELIST

- D RPC^MDRPCNT(.RESULTS,"NOTELST",476)
- D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

> ^TMP("MDKUTL",538992716,1) = 968^PROCEDURE NOTE^OCT 10, 2001@17:08:36

> ^MDPROVIDER,ONE ^PROSTHETICS

> ^TMP("MDKUTL",538992716,2) = 969^PROCEDURE NOTE^OCT 10, 2001@17:10:44^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,3) = 970^PROCEDURE NOTE^OCT 10, 2001@17:11:50^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,4) = 971^PROCEDURE NOTE^OCT 10, 2001@17:15:45^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,5) = 972^PROCEDURE NOTE^OCT 10, 2001@17:16:34^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,6) = 974^PROCEDURE NOTE^OCT 11, 2001@10:56:03^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,7) = 975^PROCEDURE NOTE^OCT 11, 2001@12:50:29^^PROSTHET

> I

> CS

> Global ^

> OPTION = VIEWTIU

- D RPC^MDRPCNT(.RESULTS,"VIEWTIU",476,968)
- D ^%G

Global ^TMP("TIUVIEW",\$J

TMP("TIUVIEW",\$J

> ^TMP("TIUVIEW",538992716,1) = TITLE: PROCEDURE NOTE

> ^TMP("TIUVIEW",538992716,2) = DATE OF NOTE: OCT 10, 2001@17:08:36 ENTRY DATE:

> O

> CT 10, 2001@17:08:36

> ^TMP("TIUVIEW",538992716,3) = AUTHOR: MDPROVIDER,ONE EXP COSIGNER:

> ^TMP("TIUVIEW",538992716,4) = URGENCY:

> STATUS:

> COMPLETED

> ^TMP("TIUVIEW",538992716,5) =

> ^TMP("TIUVIEW",538992716,6) = PROCEDURE SUMMARY CODE: Abnormal

> ^TMP("TIUVIEW",538992716,7) = DATE/TIME PERFORMED: OCT 15, 2001

> ^TMP("TIUVIEW",538992716,8) =

> ^TMP("TIUVIEW",538992716,9) = \*\*\* PROCEDURE NOTE Has ADDENDA \*\*\*

> ^TMP("TIUVIEW",538992716,10) =

> ^TMP("TIUVIEW",538992716,11) = Complete consult 1104. 6 attached images.

> ^TMP("TIUVIEW",538992716,12) =

> ^TMP("TIUVIEW",538992716,13) = /es/ MDPROVIDER,ONE

> ^TMP("TIUVIEW",538992716,14) =

> ^TMP("TIUVIEW",538992716,15) = Signed: 10/15/2001 13:02

> ^TMP("TIUVIEW",538992716,16) =

> ^TMP("TIUVIEW",538992716,17) = 10/15/2001 ADDENDUM STATUS:

> COMPLETED

> ^TMP("TIUVIEW",538992716,18) = aDDENDUM LA LA LA

> ^TMP("TIUVIEW",538992716,19) = LA LA LA

> ^TMP("TIUVIEW",538992716,20) =

> ^TMP("TIUVIEW",538992716,21) = /es/ MDPROVIDER,ONE

> ^TMP("TIUVIEW",538992716,22) =

> ^TMP("TIUVIEW",538992716,23) = Signed: 10/15/2001 13:04

> NAME: MD TMDSUBMITU TAG: RPC

> ROUTINE: MDRPCOWU RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> NAME: MD TMDWIDGET TAG: RPC

> ROUTINE: MDRPCOW RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> NAME: MDK GET VISTA DATA TAG: RPC

> ROUTINE: MDKRPC1 RETURN VALUE TYPE: ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 8 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the routine tag that will be called to retrieve the data. INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 50 REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is whatever data is needed by the subroutine to process the request

> for data. In many cases it will be a single value (e.g., patient id - DFN).

> RETURN PARAMETER DESCRIPTION:

> Returns an array.

> RESULT(0)=number or RESULT(0)=-1^error message RESULT(1)=data

> RESULT(n)=data

> If data is not found, RESULT(0) will be contain a "-1" in the first piece and an error message in the second piece.

> If data is found, RESULT(0) will contain a number that indicates how many entries are returned.

> RESULT(1) through RESULT(n) will contain the data that is found.

> NAME: MDK GET/SET RENAL DATA TAG: RPC

> ROUTINE: MDKRPC2 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> NAME: MDK UTILITY TAG: RPC

> ROUTINE: MDKUTLR RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> 1NAME: MDCLIO TAG: RPC

> ROUTINE: MDCLIO RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: PUBLIC WORD WRAP ON: TRUE DESCRIPTION:

> This is the primary RPC called by the CliO engine for normal command processing.

> NAME: MDCP CORRECTIONS BY IEN TAG: GETCORR

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: ARRAY

> AVAILABILITY: SUBSCRIPTION INACTIVE: ACTIVE WORD WRAP ON: TRUE

> DESCRIPTION:

> Gets a list of corrections for a given HL7 message.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> The IEN of the message in file 703.1 (the CP REPORT RESULTS file). RETURN PARAMETER DESCRIPTION:

> Returns a global array in the format:

> Correction Type IEN^Uncorrected Value^Corrected Value

> NAME: MDCP MESSAGE BY IEN TAG: GETMSG

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> 1 Patch MD\*1.0\*16 January 2011 Added new remote procedure calls (RPCs).

> AVAILABILITY: SUBSCRIPTION WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This RPC returns an HL7 message based on its IEN.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> This is the IEN of the message in file 772. RETURN PARAMETER DESCRIPTION:

> This returns the value of the message. Note that, at least for the initial version of this call, the MSH segment will NOT be returned as part of the results.

> NAME: MDCP RESULTS BY STATUS TAG: GTMSGIDS

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: SUBSCRIPTION INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This broker call will return a list of IENS from the CP RESULT REPORT file based on the STATUS passed in as a parameter.

> INPUT PARAMETER: MDCPSTAT PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 1 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the EXTERNAL representation of the status to be used to generate the list of IENs.

> RETURN PARAMETER DESCRIPTION:

> Returns an array of IENs.

> NAME: MDCP UPDATE MESSAGE REASON TAG: UPDRSN

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> This RPC call will add word processing text to the CLIO_HL7_LOG file to explain the reason for the current status. It is primarily intended to be used to store error text from CliO.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 250 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the IFN of the HL7 message in the CLIO_HL7_LOG file. INPUT PARAMETER: MDCPTEXT PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 250 REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is the text to add to the CLIO_HL7_LOG file. Note that this text will completely overwrite the text that was already in the reason field.

> NAME: MDCP UPDATE MESSAGE STATUS TAG: UPDATERP

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: ARRAY

> AVAILABILITY: PUBLIC INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This call will update the status of an entry in file 704.002

> (the CLIO_HL7_LOG file). Note that if the status passed through is 'PROCESSED', the CP INSTRUMENT file entry pointed to by field .03 will be

> checked to see if it has a routine in its .11 field. If it does, the HL7 message will be copied to a temp global and the PROCESSING ROUTINE will be invoked.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> The IFN of the message in the CP RESULT REPORT file.

> INPUT PARAMETER: MDCPSTAT PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 1 REQUIRED: YES

> SEQUENCE NUMBER: 2 DESCRIPTION:

> The status to which to change the file entry referenced by the first parameter. Check the data dictionary for field .09 to get a list of valid codes. This parameter must be in internal format.

> INPUT PARAMETER: MDCPDFN PARAMETER TYPE: LITERAL REQUIRED: NO SEQUENCE NUMBER: 3

> DESCRIPTION:

> This is the IFN of the patient in file 2, if available.

> INPUT PARAMETER: MDCPISCR PARAMETER TYPE: LITERAL REQUIRED: NO SEQUENCE NUMBER: 4

> DESCRIPTION:

> If MDCPDFN is set, this tells the linetag that MDCPDFN is a correction, not the original DFN.

> RETURN PARAMETER DESCRIPTION:

> Returns a local variable containing the results of the status update in DIALOG format.

## Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: MD ALLOW EXTERNAL ATTACHMENTS

> DISPLAY TEXT: Allow non-instrument attachments

> MULTIPLE VALUED: No VALUE TERM: Allowed VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to Yes to allow users of CPUser.exe to attach documents to the transaction that are not created by an instrument.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD APPOINT END DATE

> DISPLAY TEXT: End Date for Encounter Appointments MULTIPLE VALUED: No VALUE TERM: Days

> VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

> VALUE HELP: Enter a number from 0 to 365. DESCRIPTION:

> Enter a number from 0 to 365 for the number of days that will be used to add to today as the end date range of the Encounter Appointments. If no value is entered, the default value used will be 0.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD APPOINT START DATE

> DISPLAY TEXT: Start Date for Encounter Appointments MULTIPLE VALUED: No VALUE TERM: Days

> VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

> VALUE HELP: Enter a number from 0 to 365. DESCRIPTION:

> Enter a number from 0 to 365 for the number of days that will be used to subtract from today as the start date range of the Encounter

> Appointments. If no value is entered, the default value used will be 200.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD COMPL PROC DISPLAY DAYS

> DISPLAY TEXT: Completed Proc Display Days

> MULTIPLE VALUED: No VALUE TERM: Days

> VALUE DATA TYPE: numeric VALUE DOMAIN: 1:365

> VALUE HELP: Enter the number of days from 1 to 365 DESCRIPTION:

> The number of days the completed procedure requests will be displayed in the CP Check-in screen.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD CHECK-IN PROCEDURE LIST DISPLAY TEXT: Check-in Procedure List MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Schedule Appointment? VALUE DATA TYPE: set of codes VALUE DOMAIN: 0:None;1:Outpatient;2:Inpatient;3:Both

> 1 Patch MD\*1.0\*6 May 2008 Parameter Definitions added.

> 2 Patch MD\*1.0\*14 March 2008 Parameter Definitions added.

> VALUE HELP: Enter 0 for None, 1 for Outpatient, 2 for Inpatient, or 3 for both.

> INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter procedures that needs the study to be auto checked-in. INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0

> DESCRIPTION:

> This parameter contains a list of procedures that will be used

> to auto check-in the CP studies during the procedures request in CPRS and whether appointments are scheduled for the procedure.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CLINIC QUICK LIST DISPLAY TEXT: Clinic Quick List For CP MULTIPLE VALUED: Yes INSTANCE TERM: Clinic

> VALUE TERM: Procedure VALUE DATA TYPE: pointer VALUE DOMAIN: 702.01

> VALUE HELP: Select a procedure for the clinic.

INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 44

> INSTANCE HELP: Enter clinics that need CP studies to be checked-in. DESCRIPTION:

> List of clinics used as a source to get a list of patients that need to have CP studies checked-in. This only applies to studies with procedures that have multiple results such as Hemodialysis, Respiratory Therapy, and sleep studies.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MD CLINICS WITH MULT PROC

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

> 1 Patch MD\*1.0\*11 March 2009 Parameter Definition added

> 1NAME: MD COMMANDS DISPLAY TEXT: CliO Commands MULTIPLE VALUED: Yes INSTANCE TERM: Command Name

> VALUE TERM: Command Text VALUE DATA TYPE: word processing INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> DESCRIPTION:

> This parameter holds all command scripts for the CliO DB engine to process.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD PARAMETERS DISPLAY TEXT: CP Parameter settings MULTIPLE VALUED: Yes INSTANCE TERM: Parameter Name

> VALUE TERM: Parameter Value PROHIBIT EDITING: No VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> DESCRIPTION:

> This parameter holds all name value pairs for the configuration of the CP/CliO system.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> PRECEDENCE: 2 ENTITY FILE: DIVISION

> PRECEDENCE: 3 ENTITY FILE: LOCATION

> PRECEDENCE: 4 ENTITY FILE: USER

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

> NAME: MD DAYS FOR INSTRUMENT DATA

> DISPLAY TEXT: Temporary instrument data life (Days) MULTIPLE VALUED: No VALUE TERM: Days

> PROHIBIT EDITING: No VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

> DESCRIPTION:

> The number of days to keep data from the auto-instruments after the data has been associated with a Clinical Procedures report.

> 1 Patch MD\*1.0\*16 January 2011 Parameter Definition added.

> 2 Patch MD\*1.0\*16 January 2011 Parameter Definition added.

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

> The number of days after check-in date/time to display the study that has been completed in the CPUser application. This only pertains to studies that have procedures with multiple studies.

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

> 1 Patch MD\*1.0\*6 May 2008 Parameter Definition added.

> 2 Patch MD\*1.0\*20 November 2010 Parameter Definitions Added.

> NAME: MD GATEWAY DISPLAY TEXT: CP Gateway Parameters MULTIPLE VALUED: Yes INSTANCE TERM: Parameter Name

> VALUE TERM: Parameter Value VALUE DATA TYPE: free text VALUE DOMAIN: 1:255 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:255

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD GET HIGH VOLUME DISPLAY TEXT: Get High Volume MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

> VALUE TERM: Get String VALUE DATA TYPE: free text INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

> INSTANCE HELP: Enter a high volume procedure. INSTANCE SCREEN CODE: I

> +\$P(^MDS(702.01,+Y,0),"^",6)'=2&(+\$P(^MDS(702.01,+Y,0)

> ,"^",11)'=2)&(\$P(^MDS(702.01,+Y,0),"^",9)\>0) DESCRIPTION:

> This parameter will contain a free text string that contains two pieces of data delimited by a semicolon ';'. The two pieces of data are: 1) 1/0 (Yes/No) to indicate whether or not the text of the result should be added to the note, 2) 1/0 (Yes/No) to enter the text of the result as the significant finding of the Consult. (If you enter a 0, the note will be auto closed with the text inside.)

> Example string: 1;0

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

> 2 NAME: MDK APPLICATION INSTALL DISPLAY TEXT: MDK Application Install

> MULTIPLE VALUED: Yes

> INSTANCE TERM: Installation Distribution Info

> VALUE TERM: Distribution Info Value PROHIBIT EDITING: No VALUE DATA TYPE: free text VALUE DOMAIN: 1:250 INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

> 1 Patch MD\*1.0\*21 May 2010 Parameter Definition added.

> 2 Patch MD\*1.0\*6 May 2008 Parameter Definition added.

> DESCRIPTION:

> This parameter is used to store the Hemodialysis application distribution information. The information includes the following:

1)  Date/Time when application first launched.
2)  User Name
3)  System Option Loaded (Y/N)
4)  Workstation of where the application was launched. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> NAME: MDK GUI VERSION

> DISPLAY TEXT: Hemodialysis Version Compatibility

> MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version VALUE TERM: Compatible with current server version

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:40

> DESCRIPTION:

> This parameter is used to store the application:versions that are compatible with the current server version of Hemodialysis. Instance format

> of APPLICATION:VERSION (example: HEMODIALYSIS.EXE:0.0.0.0). PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 1NAME: MD MEDICINE CONVERTED DISPLAY TEXT: Medicine Package

> Converted

> MULTIPLE VALUED: No VALUE TERM: Yes/No

> PROHIBIT EDITING: No VALUE DATA TYPE: yes/no DESCRIPTION:

> Used to determine if the Medicine Package has been converted. PRECEDENCE: 1 ENTITY FILE: SYSTEM

> 2NAME: MD NOT ADMN CLOSE MUSE NOTE DISPLAY TEXT: NOT ADMN Close Muse

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

> 3NAME: MD OLYMPUS 7 DISPLAY TEXT: MD OLYMPUS 7 MULTIPLE VALUED: No VALUE TERM: Yes/No

> 1 Patch MD\*1.0\*5 August 2006 Parameter Definition added.

> 2 Patch MD\*1.0\*21 May 2010 Parameter Definition added.

> 3 Patch MD\*1.0\*11 March 2009 Parameter Definitions added.

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

> NAME: MD USE APPOINTMENT DISPLAY TEXT: Use Appointment Location MULTIPLE VALUED: No VALUE TERM: Use Appointment location VALUE DATA TYPE: yes/no

> DESCRIPTION:

> Set this value to Yes to allow CPUser to use the location of the appointment selected during CP study check-in for the workload. Otherwise, the hospital location of the CP Definition will be used.

> Enter RETURN to continue or '^' to exit:

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

> 1 Patch MD\*1.0\*14 March 2008 Parameter Definition added.

> 2 Patch MD\*1.0\*21 May 2010 Parameter Definition Added.

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

> This parameter contains the web address for the Clinical Procedures home page. This can be modified to a local address in the event that the pages are downloaded to be displayed from a local server location.

> PRECEDENCE: 1 ENTITY FILE: SYSTEM

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

> 1NAME: MD DGPM PATIENT MOVEMENT

> ITEM TEXT: CliO DGPM patient movement interface

> TYPE: extended action CREATOR: CLIOPROGRAMMER,ONE DESCRIPTION: This Protocol is an interface to the DGPM Movement Event Protocol that will process ADT Events for patient that are admitted to the hospital and will call the code in CliO to process that movement.

> IDENTIFIER: MD DGPM PATIENT MOVEMENT ENTRY ACTION: D EN^MDCPVDEF TIMESTAMP: 60943,49051

> 2NAME: MD RECEIVE GMRC

> ITEM TEXT: Clinical Procedures receives messages from Consult TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> 1 Patch MD\*1.0\*16 January 2011 Added new and updated protocols.

> 2 Patch MD\*1.0\*14 March 2008 Protocols added to support the auto study check-in.

> DESCRIPTION: This protocol receives messages from Consult. (IA 3140) ENTRY ACTION: D EN^MDWORC(.XQORMSG) TIMESTAMP: 60934,38793

> NAME: MD RECEIVE OR

> ITEM TEXT: Clinical Procedures receives order msgs from CPRS TYPE: action CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This protocol receives order messages from CPRS. (IA 3135) ENTRY ACTION: D EN^MDWOR(.XQORMSG) TIMESTAMP: 60934,38793

> 1NAME: MDC ADT_A01 OUTBOUND

> ITEM TEXT: Outbound ADT A01 Routing Protocol

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A01 messages sent by the CP/CliO system.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A01 RESPONSE MESSAGE TYPE: ADT ROUTING LOGIC: D GENDESTS^MDCPVDEF

> NAME: MDC ADT_A02 OUTBOUND

> ITEM TEXT: Outbound ADT A02 Routing Protocol

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A02 messages send by the CP/CliO system.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A02 RESPONSE MESSAGE TYPE: ADT

> PROCESSING ROUTINE: Q ROUTING LOGIC: D GENDESTS^MDCPVDEF

> NAME: MDC ADT_A03 OUTBOUND

> ITEM TEXT: Outbound ADT A03 Routing Protocol

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A03 messages sent by the CP/CliO system.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A03 RESPONSE MESSAGE TYPE: ADT

> PROCESSING ROUTINE: Q ROUTING LOGIC: D GENDESTS^MDCPVDEF

> NAME: MDC ADT_A11 OUTBOUND

> ITEM TEXT: Outbound ADT A11 Routing Protocol

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A11 messages.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A11 RESPONSE MESSAGE TYPE: ADT PROCESSING ROUTINE: Q

> NAME: MDC ADT_A12 OUTBOUND

> ITEM TEXT: Outbound ADT A12 Routing Protocol

> 1 Patch MD\*1.0\*16 January 2011 Added new protocols.

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A12 messages sent by the CP/CliO system.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A12 RESPONSE MESSAGE TYPE: ADT

> PROCESSING ROUTINE: Q ROUTING LOGIC: D GENDESTS^MDCPVDEF

> NAME: MDC ADT_A13 OUTBOUND

> ITEM TEXT: Outbound ADT A13 Routing Protocol

> TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the outbound routing protocol for all ADT A13 messages sent by the CP/CliO system.

> TIMESTAMP: 60943,49051

> RECEIVING APPLICATION: MDC ADT OUTBOUND SPL

> EVENT TYPE: A13 RESPONSE MESSAGE TYPE: ADT

> PROCESSING ROUTINE: Q ROUTING LOGIC: D GENDESTS^MDCPVDEF

> NAME: MDC CPAN VS

> ITEM TEXT: Outbound for CLIO ADT A01 from MDC

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: Outbound for CLIO ADT A01 from MDC

> TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPAN TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A01

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A01 OUTBOUND

> NAME: MDC CPCAN VS

> ITEM TEXT: Outbound CLIO ADT A11 from MDC

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: CLIO Outbound ADT A11 Cancel Admit from MDC

> TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPCAN TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A11

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A02 OUTBOUND

> NAME: MDC CPDE VS

> ITEM TEXT: Outbound CLIO ADT A03 from MDC

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: CLIO Outbound ADT A03 Discharge from MDC

> TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPDE TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A03

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A03 OUTBOUND

> NAME: MDC CPCT VS

> ITEM TEXT: Outbound CLIO ADT A12 from MDC

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: CLIO Outbound ADT A12 Cancel Transfer from MDC TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPCT TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A12

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A12 OUTBOUND

> NAME: MDC CPCDE VS

> ITEM TEXT: Outbound CLIO ADT A13 from MDC TYPE: event driver

> DESCRIPTION: CLIO Outbound ADT A13 Cancel Discharge from MDC TIMESTAMP: 61257,40262 SENDING APPLICATION: MDC CPCDE TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A13

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A13 OUTBOUND

> NAME: MDC CPTP VS ITEM TEXT: CLIO Transfer a Patient (A02)

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: Outbound for CLIO ADT A02 from MDC

> TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPTP TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A02

> ACCEPT ACK CODE: AL VERSION ID: 2.4 SUBSCRIBERS: MDC ADT_A02 OUTBOUND

> NAME: MDC CPUPI VS

> ITEM TEXT: Outbound CLIO ADT A08 from MDC

> TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: CLIO Outbound ADT A08 Patient Update from MDC TIMESTAMP: 60943,49051 SENDING APPLICATION: MDC CPUPI TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A08

> ACCEPT ACK CODE: AL VERSION ID: 2.4

> NAME: MDHL Device Client ITEM TEXT: Instrument Device Client TYPE: subscriber CREATOR: CLIOPROGRAMMER,ONE PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: Clinical Procedures CliO Client Protocol for UCI Devices TIMESTAMP: 60943,49051 RECEIVING APPLICATION: MDHL-OUT TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P LOGICAL LINK: MDHL IN

> RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D EN^MDCPHL7A SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> NAME: MDHL Device Server ITEM TEXT: Instrument HL7 Event Driver TYPE: event driver CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: Clinical Procedures CliO Server Protocol for ICU Devices. TIMESTAMP: 60943,49051 SENDING APPLICATION: MDHL-IN TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: debug VERSION ID: 2.4

> SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> SUBSCRIBERS: MDHL Device Client

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MCAR-INST ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER

> COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> 1 NAME: MDC ADT OUTBOUND ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC ADT OUTBOUND GE ACTIVE/INACTIVE: ACTIVE FACILITY NAME: GE COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC ADT OUTBOUND PHL ACTIVE/INACTIVE: ACTIVE FACILITY NAME: PHILIPS COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC ADT OUTBOUND PIC ACTIVE/INACTIVE: ACTIVE FACILITY NAME: PICIS COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ~\\ HL7 FIELD SEPARATOR:

> NAME: MDC ADT OUTBOUND SPL ACTIVE/INACTIVE: ACTIVE FACILITY NAME: MDC COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPAN ACTIVE/INACTIVE: ACTIVE FACILITY NAME: HINES_OIFO COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPCAN ACTIVE/INACTIVE: ACTIVE FACILITY NAME: HINES_OIFO COUNTRY CODE: USA

> HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPCDE ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPCT ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\

> 1 Patch MD\*1.0\*16 January 2011 Added new HL7 application parameters.

> HL7 FIELD SEPARATOR: \|

> NAME: MDC CPDE ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPTP ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDC CPUPI ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDHL-IN ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: MDHL-OUT ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR:

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

> PERSISTENT: NO STARTUP NODE: DEV:ISC4A1 IN QUEUE BACK POINTER: 202 IN QUEUE FRONT POINTER: 202

> OUT QUEUE BACK POINTER: 206 OUT QUEUE FRONT POINTER: 202

1NODE: MDHL IN LLP TYPE: TCP

DEVICE TYPE: Single-threaded Server STATE: Listen

> AUTOSTART: Enabled TIME STARTED: JUL 31, 2008@07:42:51

> TASK NUMBER: 3393328 SHUTDOWN LLP ?: NO

> QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

> READ TIMEOUT: 3 ACK TIMEOUT: 3

> TCP/IP PORT: 11660 TCP/IP SERVICE TYPE: SINGLE LISTENER

> PERSISTENT: NO RETENTION: 60

> IN QUEUE BACK POINTER: 17905 IN QUEUE FRONT POINTER: 17905 OUT QUEUE BACK POINTER: 17598 OUT QUEUE FRONT POINTER: 17598

> 1 Patch MD\*1.0\*16 January 2011 Added a new HL logical link.

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

> for procedures that require multiple encounters such as Hemodialysis, Respiratory Therapy, and Sleep Studies.

> ROUTINE: CLINICPT^MDWORSR SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: STUDY CHECK-IN

> 1 NAME: MD HIGH VOLUME PROCEDURE SETUP MENU TEXT: High Volume Procedure Setup TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will populate the XPAR Parameters MD GET HIGH VOLUME and MD NOT ADMN CLOSE MUSE NOTE. It will let the user populate a list of Clinical Procedures procedures set it up for high volume procedure process.

> ROUTINE: EN1^MDARSET

> UPPERCASE MENU TEXT: HIGH VOLUME PROCEDURE SETUP

> NAME: MD PROC W/INCOMPLETE WORKLOAD

> MENU TEXT: Print list of Procedure with incomplete workload

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option prints a list of procedures that has incomplete workload for the visit.

> ROUTINE: E1^MDSTUDW

> UPPERCASE MENU TEXT: PRINT LIST OF PROCEDURE WITH I

> NAME: MD PROCESS RESULTS MENU TEXT: MD Process Results TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

> DESCRIPTION: This task is ran daily for every hour to process results and update Consults package.

> ENTRY ACTION: N ZTSAVE S ZTSAVE("DUZ")=DUZ,ZTSAVE("DUZ(")="" ROUTINE: PROCESS^MDHL7XXX UPPERCASE MENU TEXT: MD PROCESS

> RESULTS

> 2NAME: MD HEMODIALYSIS USER MENU TEXT: HEMODIALYSIS USER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 60387,39853

> RPC: MDK GET VISTA DATA RPC: MDK GET/SET RENAL DATA RPC: MDK UTILITY

> RPC: VAFCTFU CONVERT DFN TO ICN RPC: VAFCTFU CONVERT ICN TO DFN RPC: MD TMDWIDGET

> RPC: MD TMDNOTE RPC: MD TMDCIDC RPC: MD TMDLEX

> RPC: MD TMDENCOUNTER RPC: GMV MANAGER RPC: MD GATEWAY

> RPC: MD TMDSUBMITU RPC: ORWPT PTINQ RPC: GMV PTSELECT

> RPC: DG SENSITIVE RECORD ACCESS RPC: DG SENSITIVE RECORD BULLETIN RPC: MD TMDRECORDID

> 1 Patch MD\*1.0\*21 May 2010 Options added to support high volume procedures enhancement.

> 2 Patch MD\*1.0\*6 May 2008 Hemodialysis User menu option added.

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

> ITEM: MDCVT RUN SYNONYM: 3

> DISPLAY ORDER: 3

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

> complete and are in appropriate statuses.

> ROUTINE: TOTALS^MDCVT

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

> 2NAME: MD DEVICE SURVEY TRANSMISSION MENU TEXT: MD Device Survey

> Transmission

> TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

> PACKAGE: CLINICAL PROCEDURES

> DESCRIPTION: This option will run the device survey collection routine and capture the data for transmission.

> ROUTINE: COL^MDDEVCL

> UPPERCASE MENU TEXT: MD DEVICE SURVEY TRANSMISSION

> 3NAME: MDCP GATEWAY CONTEXT

> MENU TEXT: RPC Broker context for CP Gateway

> TYPE: Broker (Client/Server) CREATOR: CLIOPROGRAMMER,ONE

> PACKAGE: CLINICAL PROCEDURES TIMESTAMP OF PRIMARY MENU: 61354,37203 RPC: MDCP RESULTS BY STATUS

> RPC: MDCP UPDATE MESSAGE STATUS RPC: MDCP UPDATE MESSAGE REASON RPC: MDCP MESSAGE BY IEN

> RPC: MD CLIO

> UPPERCASE MENU TEXT: RPC BROKER CONTEXT FOR CP GATE

> NAME: MD CLIO MENU TEXT: CliO Service Options TYPE: Broker (Client/Server) CREATOR: CLIOPROGRAMMER,ONE

> DESCRIPTION: This is the primary menu option for the entire Flowsheets application. It allows the user access to the MD CLIO RPC and as such all the appropriate calls that are needed based on the key the user has.

> TIMESTAMP OF PRIMARY MENU: 61486,36208 RPC: MD CLIO

> UPPERCASE MENU TEXT: CLIO SERVICE OPTIONS

> 1 Patch MD\*1.0\*11 March 2009 Add new exported option.

> 2 Patch MD\*1.0\*20 November 2010 New option added.

> 3 Patch MD\*1.0\*16 January 2011 Added MDCP GATEWAY CONTEXT option. Added MD CLIO option.

## 1Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Missing Required HL7 Element

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.001 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Missing required HL7 element.

> DESCRIPTION: An element that is required according to the HL7 message profile is missing in the FileMan data for the current record.

> TEXT:

> Required element \|1\| is missing for record \|2\| in File \#\|3\|. PARAMETER SUBSCRIPT: 3

> PARAMETER DESCRIPTION: FileMan file number that is the source of the missing d PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: Missing HL7 element identified by SEGMENT.FIELD\[.COMPON ENT\[.SUBCOMPONENT\]\].

> PARAMETER SUBSCRIPT: 2

> PARAMETER DESCRIPTION: IEN or IENS (comma delimited) of the FileMan record mis sing that is the source of the missing data. A sub-file IEN would be represented as sub-file IEN,file IEN (e.g., 2,121. Where the sub-file IEN=2 and the file IEN

> =121.).

### Invalid Key Passed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.002 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Invalid key passed.

> DESCRIPTION: The passed key has no corresponding entry in the Patient Movement File (#405).

> TEXT:

> No entry in ^DGPM() for IEN \|1\|. PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: IEN of Patient Movement File.

### No Record in Patient File for DFN Passed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.003 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: No record in Patient File for DFN passed.

> DESCRIPTION: There is no entry in ^DPT (file \#2) for the DFN extracted from the Patient Movement File (#405).

> TEXT:

> There is no entry in ^DPT for DFN \|1\|. PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: DFN from Patient Movement File(#405)

### Required Segment Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.004 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Required segment missing

> DESCRIPTION: This error occurs when a segment that is required for a particular message has no data in the database.

> TEXT:

> Required segment \|1\| is not returned for IEN \|2\| in File \#\|3\|.

> PARAMETER SUBSCRIPT: 1 PARAMETER DESCRIPTION: HL7 Segment name. PARAMETER SUBSCRIPT: 2

> PARAMETER DESCRIPTION: IEN of record returning no segment.

> PARAMETER SUBSCRIPT: 3

> PARAMETER DESCRIPTION: File in which there is no data for the IEN.

> 1 Patch MD\*1.0\*16 January 2011 Added Dialogs section.

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Included in this section is the information about the cross-references of the application.

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
<td>1<strong>702</strong></td>
<td>.05</td>
<td>ACON</td>
<td><p>Used for searches when the</p>
<p>user knows the Consult order number.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.3</td>
<td>ACONV</td>
<td><p>This cross reference is used to keep track of which CP transaction study was created during the Medicine report conversion and which Medicine record it is</p>
<p>associated with.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.06</td>
<td>ATIU</td>
<td><p>Used for searches when the</p>
<p>user knows the TIU Note title.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, the patient</p>
<p>name.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.04</td>
<td>ACP</td>
<td><p>Used for searches when the</p>
<p>user knows the CP definition.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.11</td>
<td>AINST</td>
<td><p>Used for searches when the user knows if the study was</p>
<p>submitted to Imaging.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.12</td>
<td>AION</td>
<td><p>Used to quickly retrieve</p>
<p>the study ien from the instrument order number.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.09</td>
<td>AS</td>
<td><p>It is a cross reference on the status of the CP study and it</p>
<p>is used for quick look up.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.13</td>
<td>AVISIT</td>
<td><p>This cross reference is used to make sure that a Visit file entry is not deleted as long</p>
<p>as there is an entry.</p></td>
</tr>
</tbody>
</table>

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
<td></td>
<td>.13</td>
<td>AUPNV</td>
<td><p>This cross reference tells Visit Tracking how many file entries are using (point</p>
<p>to) a Visit file entry.</p></td>
</tr>
<tr class="even">
<td>Subfile 702.091</td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, error messages.</p></td>
</tr>
<tr class="odd">
<td>Subfile 702.1</td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, image.</p></td>
</tr>
<tr class="even">
<td><strong>702.01</strong></td>
<td>.02</td>
<td>ASPEC</td>
<td><p>Used for searches when the</p>
<p>user knows the Treating Specialty.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, name of the</p>
<p>procedure.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>UC</td>
<td><p>Used to validate a new entry</p>
<p>as unique without case sensitivity.</p></td>
</tr>
<tr class="odd">
<td>Subfile 702.011</td>
<td>.01</td>
<td>AINST</td>
<td><p>Used for searches when the user knows the name of the</p>
<p>instrument.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, instrument.</p></td>
</tr>
</tbody>
</table>

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
<td><strong>1702.09</strong></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, name of the</p>
<p>instrument.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>UC</td>
<td><p>Used to validate a new entry as unique without case</p>
<p>sensitivity.</p></td>
</tr>
<tr class="odd">
<td><strong>703.1</strong></td>
<td>.02</td>
<td>ADFN</td>
<td><p>Used for searches when the user knows the patient</p>
<p>name.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.03</td>
<td>ADTP</td>
<td><p>Used for searches when the</p>
<p>user knows the date/time performed.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.04</td>
<td>AINST</td>
<td><p>Used for searches when the user knows the name of the</p>
<p>instrument.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.09</td>
<td>ASTATUS</td>
<td><p>Sets the status for the</p>
<p>Gateway to find studies to process.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.05</td>
<td>ASTUDYID</td>
<td><p>This cross reference provide a quick look up by the study</p>
<p>reference ID.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, the upload</p>
<p>ID.</p></td>
</tr>
<tr class="odd">
<td>Subfile 703.11</td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, upload item.</p></td>
</tr>
<tr class="even">
<td><strong>703.9</strong></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, Name.</p></td>
</tr>
<tr class="odd">
<td>Subfile 703.91</td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, Medicine</p>
<p>File Parameters.</p></td>
</tr>
<tr class="even">
<td>Subfile 703.92</td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, Conversion</p>
<p>ID.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 34%" />
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
<td></td>
<td>.02</td>
<td>AS</td>
<td><p>Used for lookup by</p>
<p>conversion status.</p></td>
</tr>
<tr class="even">
<td>1<strong>704.004</strong></td>
<td></td>
<td>B</td>
<td><p>Regular B Index of file. This cross reference correlates entries in the CP_HL7_LOG FILE (#704.002) with</p>
<p>entries in this file.</p>
<p>A sample cross reference entry would be :</p>
<p>^MDC(704.004,"B",CP_HL 7_LOG_IEN,CP_HL7_LOG</p>
<p>_REASON_IEN)=""</p></td>
</tr>
<tr class="odd">
<td><strong>704.005</strong></td>
<td></td>
<td>B</td>
<td><p>Regular B Index of file. This will make it easy to find and sort the PATIENT(s) involved per</p>
<p>patient movement data</p>
<p>within this file.</p></td>
</tr>
<tr class="even">
<td><strong>704.006</strong></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Index of file. This index quickly sorts file entries based on subscriber</p>
<p>protocol identification.</p></td>
</tr>
<tr class="odd">
<td><strong>704.101</strong></td>
<td>.02</td>
<td>C</td>
<td><p>Regular C Index of file. This will support a quick view of</p>
<p>entries by name.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.05</td>
<td>ATYPE</td>
<td><p>Regular ATYPE Index of file. This supports a quick correlation with TERM TYPE File (#704.102)</p>
<p>entries and entries in this file.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.07</td>
<td>ACTIVE</td>
<td><p>Regular ACTIVE Index of file. This supports quick sorting of entries by VALUE</p>
<p>TYPE.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Cross References added.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 34%" />
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
<td>1<strong>704.102</strong></td>
<td></td>
<td>B</td>
<td><p>Regular B Index of file. This</p>
<p>supports a quick sort of entries by the TYPE name.</p></td>
</tr>
<tr class="even">
<td><strong>704.201</strong></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, PATIENT</p>
<p>ID.</p></td>
</tr>
<tr class="odd">
<td><strong>704.202</strong></td>
<td>.09</td>
<td>AS</td>
<td><p>Used for lookup of active</p>
<p>hemodialysis studies.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference of the .01 field, the</p>
<p>hemodialysis ID.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.02</td>
<td>C</td>
<td><p>C Cross Reference of the .02 field, PATIENT record</p>
<p>number.</p></td>
</tr>
<tr class="even">
<td><strong>704.209</strong></td>
<td>.01</td>
<td>B</td>
<td><p>Regular B Cross Reference</p>
<p>of the .01 field, SETTING NAME.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Cross Reference added.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is no archiving capability at this time. Purging is available in the CPGateway through the Set Maximum Log Entries option. See description below.

> Set Maximum Log Entries allows the user to adjust the number of entries that are displayed in the log file. Once this value is reached, entries will be purged from the beginning of the log to keep the log file from growing too large. This value will take effect after the next polling operation so if the current poll value is 300 seconds it may take up to 5 minutes for the new value to be used. Allowable values are 100 to 10000 entries. When the CP Gateway is shut down, all entries are purged from the log file.

> Note: Purging is also done daily while the CP Gateway is running. This purge deletes the raw data that comes across from the instrument. The CP Gateway keeps data for a specified number of days based on the entry in the system parameter “Days to keep Instrument Data”. Data older than this will be purged. The data to be deleted is already matched with a study. The fields purged are the Item Value field (#.1) and Item Text field (#.2) of the Upload Item multiple in the <sup>1</sup>CP RESULTS file (#703.1).

![](md-1-23-technical-manual-cp-flowsheets/002.png)

> Figure 1, Set Maximum Log Entries

## Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A CP Legacy background task cleans up observations (uuencoded or XML data) from instruments (monitors) that are not in a verified state and are older than the parameter setting (system parameter “Days to Keep Instrument Data”) for unverified observations in the CP Console. This cleanup is designed to run after data is processed, and deletes the unused data. It runs through the UPLOAD ITEM field in the CP RESULT REPORT file (#703.1) and purges unnecessary data from previous uploads.

> 1 Patch MD\*1.0\*16 January 2011 File reference updated to national documentation standards. Added caption to figure. Added new Cleanup task.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1Entry points provided by the Clinical Procedures V. 1.0 package to other packages are listed below.

> Routine: MDAPI (Controlled Subscription) COMPONENT: \$\$EXTDATA(MDPROC) VARIABLES: MDPROC

> Type: Input

> The CP Definition IEN from CP DEFINITION file (702.01)

> Type: Output

> This is an extrinsic function and it returns: 1/0 for Yes/No.

> Entry Point to check if a medical device is associated with the CP Definition.

> COMPONENT: \$\$TIUCOMP(MDNOTE) VARIABLES: MDNOTE Type: Input

> The TIU Document IEN from TIU DOCUMENT file (#8925).

> \$\$TIUCOMP Type: Output

> This is an Extrinsic Function and it returns: 0/1 for fail/success of transaction completion.

> Entry Point to complete a CP transaction.

> COMPONENT: \$\$TIUDEL(MDNOTE) VARIABLES: MDNOTE Type: Input

> The TIU Document IEN from TIU DOCUMENT file (#8925).

> Entry Point to clean up the CP Transaction file entry of the TIU Note that was deleted.

> COMPONENT: ISTAT(MDARR) VARIABLES: MDARR Type: Input

> An array of the following: MDARR(0)="0^error message" or "1^success message"

> MDARR(1)=TrackID (CP;Transaction IEN)

> 1 Patch MD\*1.0\*6 May 2008 Description modified and callable routines added.

> MDARR(2)=Image(s) Queue Number MDARR(3..N)=Warnings, if error(s) exist.

> Entry Point to update Clinical Procedures of the result of

> the image(s) that was copied to the Imaging Server.

> COMPONENT: ITIU(RESULTS,DFN,CONSULT,VSTRING) VARIABLES: RESULTS Type: Output

> RESULTS(0) will equal one of the following (Required)

> ; IEN of the TIU note if successful

> ; or on failure one of the following status messages

> ; -1^No patient DFN

> ; -1^No Consult IEN

> ; -1^No VString

> ; -1^Error in CP transaction

> ; -1^Unable to create CP transaction

> ; -1^Unable to create the TIU document

> ; -1^No such consult for this patient.

> DFN Type: Input

> Patient IEN. (Required) CONSULT Type: Input

> Consult IEN. (Required)

> VSTRING Type: Input

> VString data for TIU Note. (Required) This entry point enables VistA Imaging to retrieve/create a TIU note for a consult for attaching images to.

> COMPONENT:

> \$\$TIUREAS(MDFN,MDOLDC,MDANOTE,MDNDFN,MDNEWC,MDNEWV,MDNTIU) VARIABLES: MDFN Type: Input

> Patient DFN in Patient File (#2).

> MDOLDC Type: Input

> The old consult number that the TIU note is being re-assigned from.

> MDANOTE Type: Input

> The TIU Note internal Entry Number that is being re-assigned.

> MDNDFN Type: Input

> The patient DFN who will be re-assigned to the TIU document.

> MDNEWC Type: Input

> The new consult number that will be

> re-assigned to the TIU document.

> MDNEWV Type: Input

> The new visit for the TIU document assignment.

> MDNTIU Type: Input

> The new re-assigned TIU document internal entry number.

> \$\$TIUREAS Type: Output

> This is an extrinsic function and it returns: 1 for Success or 0^Error Message.

> This entry point enables TIU to notify CP that a TIU note was reassigned and CP needs to clean up and update the TIU note re-assignment.

> ROUTINE: MDRPCOP (Private Subscription)

> COMPONENT: GETVST

> VARIABLES: DFN Type: Input

> Patient's dfn. RESULTS Type: Output

> A subscripted array that contains a list of visits:

> 1st piece has 3 pieces delimited by an ";"

> Patient DFN in Patient File (#2).

- type of visit ("A","I","V")
- date and time
- hospital location ien 2nd piece - date/time of visit (internal format)

> 3rd & 4 piece - (external format) hospital location and status.

> This sub-module returns a list of visits for a given patient.

> ROUTINE: MDAPI1 (Private Subscription)

> COMPONENT: GET(RESULTS,MDARDFN,MDSDT,MDEDT,MDFLDS) VARIABLES: RESULTS Type: Both

> Input: The global ^TMP array in which to return results. (Required)

> Output: Passed by Reference

> Global array returned in the FM DIQ call

> format:

> MDARDFN Type: Input

> The patient DFN (Required).

> MDSDT Type: Input

> The start date of the date range to return the data in. This must be in FM internal format. (Required).

> MDEDT Type: Input

> The end date of the date range to return the data in. This must be in FM internal format. (Required).

> MDFLDS Type: Input

> A list of fields from file \#691.5 to be returned in RESULTS. MDFLDS should contain a list of fields delimited by ";" (Required).

> example: MDFLDS=".01;11;20..."

> Example API call:

> S RESULTS="^TMP(""NAMESPACE"",\$J)" D

> GET^MDAPI1(.RESULTS,162,2900101,3021001, ".01;11")

> return:

> ^TMP("NAMESPACE",\$J,file \#,record ien\_","

> ,field \#,"E")=Data

> ^TMP("NAMESPACE",\$J,subfile \#,entry \#\_","\_

> record ien field of the multiple,"E")=data

> ^TMP("NAMESPACE",\$J,0) will equal one of the

> following,

> If the call failed:

> -1^No Patient DFN.

> -1^No Start Date Range

> -1^No End Date Range.

> -1^Start Date greater than End Date.

> -1^No fields defined.

> If a local variable is defined in RESULTS,

> ^TMP("MDAPI",\$J,0) equals

> -1^Global TMP array only.

> If no return array defined,

> ^TMP("MDAPI",\$J,0) equals

> -1^No return array global.

> If no data,

> ^TMP("NAMESPACE",\$J,0) equals

> -1^No data for patient.

> ROUTINE: MDPS1 (Controlled Subscription)

> COMPONENT: CPA~MDPS1

> VARIABLES: DFN Type: Input

> Patient Internal Entry Number. (Required) GMTS1 Type: Input

> The ending date in inverse date format (9999999-date/time). (Required)

> GMTS2 Type: Input

> The beginning date in inverse date format (9999999-date/time). (Required)

> GMTSNDM Type: Input

> The maximum number of entries to return. (Optional)

> GMTSNPG Type: Input

> The Page Number. (Optional) GMTSQIT Type: Input

> Quit indicator. (Optional)

> This entry point will display Clinical Procedures result

> report that have the Procedure Summary Code of ABNORMAL. The result consists of the Display Result of the Consult procedure request, if it exists, and the TIU document text.

> COMPONENT: CPB~MDPS1

> VARIABLES: DFN Type: Input

> Patient Internal Entry Number. (Required) GMTS1 Type: Input

> The ending date in inverse date format (9999999-date/time). (Required)

> GMTS2 Type: Input

> The beginning date in inverse date format (9999999-date/time). (Required)

> GMTSNDM Type: Input

> The maximum number of entries to return. (Optional)

> GMTSNPG Type: Input

> The Page Number. (Optional) GMTSQIT Type: Input

> Quit indicator. (Optional)

> This entry point will display a brief summary of the Clinical Procedures result Report. It displays the Consults \# (if it exists), Procedure Name, Date/Time Performed, and the Procedure Summary Code.

> COMPONENT: CPF~MDPS1

> VARIABLES: DFN Type: Input

> Patient Internal Entry Number. (Required) GMTS1 Type: Input

> The ending date in inverse date format (9999999-date/time). (Required)

> GMTS2 Type: Input

> The beginning date in inverse date format (9999999-date/time). (Required)

> GMTSNDM Type: Input

> The maximum number of entries to return. (Optional)

> GMTSNPG Type: Input

> The Page Number. (Optional) GMTSQIT Type: Input

> Quit indicator. (Optional)

> This entry point displays the full Clinical Procedures result report. The full report consists of the Display Result of the Consult procedure, if it exists, and the TIU document text.

> COMPONENT: CPS~MDPS1

> VARIABLES: DFN Type: Input

> Patient Internal Entry Number. (Required) GMTS1 Type: Input

> The ending date in inverse date format (9999999-date/time). (Required)

> GMTS2 Type: Input

> The beginning date in inverse date format (9999999-date/time). (Required)

> GMTSNDM Type: Input

> The maximum number of entries to return. (Optional)

> GMTSNPG Type: Input

> The Page Number. (Optional) GMTSQIT Type: Input

> Quit indicator. (Optional)

> This entry point displays a one line summary of the Clinical Procedures result report. The one line summary consists of the Consult Number, if it exists, Procedure

> Name, Date/Time Performed, and the Procedure Summary Code.

> COMPONENT: EN1~MDPS1(MDGLO,MDDFN,MDSDT,MDEDT,MDMAX,MDPSC,MDALL)

> VARIABLES: MDGLO Type: Both

> Return Global Array (Required) MDDFN Type: Input

> Patient DFN (Internal Entry Number) (Required)

> MDSDT Type: Input

> Start Date in FM Internal Format (Optional)

> MDEDT Type: Input

> End Date in FM Internal Format (Optional) MDMAX Type: Input

> Number of studies to return (Optional) MDPSC Type: Input

> Procedure Summary Code to return. The

> four Procedure Summary Code are NORMAL, ABNORMAL, BRODERLINE, and INCOMPLETE. By

> passing this parameter, the entry point will pass studies with this Procedure Summary Code. (Optional)

> MDALL Type: Input

> MDALL is flag. If MDALL =1, it identifies that all text reports with the procedures list should be returned.

> This entry point returns a global Array.

> COMPONENT: PR690~MDPS1 VARIABLES: MCARGDA Type: Input

> The internal entry number of the Medicine report record.

> MCPRO Type: Input

> The free text of the Medicine procedure name in the Procedure/Subspecialty file (#697.2).

> DFN Type: Input

> Patient internal entry number.

> ORHFS Type: Input

> Order Entry Host File.

> Prints the free text of the Medicine report.

> COMPONENT: PR702~MDPS1 VARIABLES: MCARGDA Type: Input

> The internal entry number of the CP Transaction record in file (#702).

> MCPRO Type: Input

> The free text of the CP Definition name in file (#702.01).

> DFN Type: Input

> Patient internal entry number.

> ORHFS Type: Input

> The Order Entry Host File.

> Prints the free text of the Clinical Procedures result interpretation.

> COMPONENT: CPC~MDPS1

> VARIABLES: DFN Type: Input

> Patient Internal Entry Number. (Required) GMTS1 Type: Input

> The ending date in inverse date format (9999999-date/time). (Required)

> GMTS2 Type: Input

> The beginning date in inverse date format (9999999-date/time). (Required)

> GMTSNDM Type: Input

> The maximum number of entries to return. (Optional)

> GMTSNPG Type: Input

> The Page Number. (Optional) GMTSQIT Type: Input

> Quit indicator. (Optional)

> This entry point displays the Captioned Clinical Procedures result report. The captioned report displays the Display Result of the Consult procedure, if it exists, and the TIU document text.

> 1ROUTINE: MDCLIO1

> COMPONENT: QRYDATE(ARRAY,START,END)

> This entry point provides a list of OBS record IDs (FILE

> 1 Patch MD\*1.0\*16 May 2010 Added MDCLIO1 to Callable Routines

> 704.117, Field .01) for the date range specified. Output format:

> ARRAY(0)=number of records returned ARRAY(n)=record ID (FILE 704.117, Field .01)

> n = sequential number starting with 1 Example:

> \>K RESULT

> \>D QRYDATE^MDCLIO1("RESULT",3070301,3070401)

> \>ZW RESULT RESULT(0)=3

> RESULT(1)="{FD0FEBBC-8EC1-42E4-9483-4BDBE6370728}" RESULT(2)="{A7C7FFEB-0CD5-4D55-BB34-35B9620F4ECC}" RESULT(3)="{D0CEA9D2-A519-41C2-A4AE-9C24C7498E56}" VARIABLES: Both ARRAY

> This is the name of the array to return the data in. It is a closed array and surrounded in quotes (e.g., "RESULT" or "^TMP(\$J)"). (required)

> VARIABLES: Input START

> This is the date/time to begin the search. It is in FileMan internal date/time format. If it is not

> defined, all records before the END date/time are returned.

> VARIABLES: Input END

> This is the end date of the search. It is in FileMan internal date/time format. If it is not defined, no records will be returned.

> COMPONENT: QRYOBS(ARRAY,GUID)

> This entry point returns the OBS (704.117) file data for the specified record.

> Output format:

> ARRAY("AUDIT_EXISTS","E")=Field .911 (external)

> ARRAY("AUDIT_EXISTS","I")=Field .911 (internal)

> ARRAY("CHILD_ORDER","E")=Field .27 (external)

> ARRAY("CHILD_ORDER","I")=Field .27 (internal)

> ARRAY("COMMENT","E")=Field .4 (external)

> ARRAY("COMMENT","I")=Field .4 (internal) ARRAY("CONTEXT",0)=Number of "CONTEXT" records (in this example: 2) ARRAY("CONTEXT",1,"METHOD_ID","E")="CONTEXT" nodes are

> returned when the ARRAY("CONTEXT",1,"METHOD_ID","I")=node 'ARRAY("TERM_ID","E")="SpO2%"'.

> ARRAY("CONTEXT",1,"OBS_ID","E")=These "CONTEXT" nodes will

> contain any

> ARRAY("CONTEXT",1,"OBS_ID","I")=records about SUPPLEMENTATL OXYGEN

> ARRAY("CONTEXT",1,"SVALUE","E")=FLOW RATE and SUPPLEMENTAL OXYGEN

> ARRAY("CONTEXT",1,"SVALUE","I")=CONCENTRATION which are

> related to the ARRAY("CONTEXT",1,"TERM_ID","E")=SpO2% reading. ARRAY("CONTEXT",1,"TERM_ID","I")=

> ARRAY("CONTEXT",1,"UNIT_ID","E")=

> ARRAY("CONTEXT",1,"UNIT_ID","I")=

> ARRAY("CONTEXT",2,"OBS_ID","E")=

> ARRAY("CONTEXT",2,"OBS_ID","I")=

> ARRAY("CONTEXT",2,"SVALUE","E")=

> ARRAY("CONTEXT",2,"SVALUE","I")=

> ARRAY("CONTEXT",2,"TERM_ID","E")=

> ARRAY("CONTEXT",2,"TERM_ID","I")=

> ARRAY("CONTEXT",2,"UNIT_ID","E")=

> ARRAY("CONTEXT",2,"UNIT_ID","I")= ARRAY("CORRECTION_FOR_ID","E")=Field .912 (external)

> ARRAY("CORRECTION_FOR_ID","I")=Field .912 (internal)

> ARRAY("ENTERED_BY_ID","E")=Field .26 (external)

> ARRAY("ENTERED_BY_ID","I")=Field .26 (internal)

> ARRAY("ENTERED_DATE_TIME","E")=Field .25 (external)

> ARRAY("ENTERED_DATE_TIME","I")=Field .25 (internal)

> ARRAY("FACILITY_ID","E")=Field .03 (external)

> ARRAY("FACILITY_ID","I")=Field .03 (internal)

> ARRAY("HOSPITAL_LOCATION_ID","E")=Field .04 (external)

> ARRAY("HOSPITAL_LOCATION_ID","I")=Field .04 (internal)

> ARRAY("LOCATION_ID","E")=FILE 704.118, Field .02 (external)

> ARRAY("LOCATION_ID","I")=FILE 704.118, Field .02 (internal)

> ARRAY("METHOD_ID","E")=FILE 704.118, Field .02 (external)

> ARRAY("METHOD_ID","I")=FILE 704.118, Field .02 (internal)

> ARRAY("OBSERVED_BY_ID","E")=Field .06 (external)

> ARRAY("OBSERVED_BY_ID","I")=Field .06 (internal)

> ARRAY("OBSERVED_DATE_TIME","E")=Field .05 (external)

> ARRAY("OBSERVED_DATE_TIME","I")=Field .05 (internal)

> ARRAY("OBS_ID","E")=Field .01 (external)

> ARRAY("OBS_ID","I")=Field .01 (internal)

> ARRAY("PARENT_ID","E")=Field .02 (external)

> ARRAY("PARENT_ID","I")=Field .02 (internal)

> ARRAY("PATIENT_ID","E")=Field .08 (external)

> ARRAY("PATIENT_ID","I")=Field .08 (internal)

> ARRAY("POSITION_ID","E")=FILE 704.118, Field .02 (external)

> ARRAY("POSITION_ID","I")=FILE 704.118, Field .02 (internal)

> ARRAY("RANGE","E")=Field .28 (external)

> ARRAY("RANGE","I")=Field .28 (internal)

> ARRAY("SOURCE","E")=Field .21 (external)

> ARRAY("SOURCE","I")=Field .21 (internal)

> ARRAY("SOURCE_COMMENTS","E")=Field .22 (external)

> ARRAY("SOURCE_COMMENTS","I")=Field .22 (internal)

> ARRAY("SOURCE_DATA_ITEM_ID","E")=Field .23 (external)

> ARRAY("SOURCE_DATA_ITEM_ID","I")=Field .23 (internal)

> ARRAY("SOURCE_VERSION","E")=Field .24 (external)

> ARRAY("SOURCE_VERSION","I")=Field .24 (internal)

> ARRAY("STATUS","E")=Field .09 (external)

> ARRAY("STATUS","I")=Field .09 (internal)

> ARRAY("SVALUE","E")=Field .1 (external)

> ARRAY("SVALUE","I")=Field .1 (internal)

> ARRAY("TERM_ID","E")=Field .07 (external)

> ARRAY("TERM_ID","I")=Field .07 (internal)

> ARRAY("UNIT_ID","E")=FILE 704.118, Field .02 (external)

> ARRAY("UNIT_ID","I")=FILE 704.118, Field .02 (internal)

> Example:

> \>D

> QRYOBS^MDCLIO1("ARRAY","{E24715DE-3DCC-4A04-9F8B- 0A7C6E8E64F4}")

> \>ZW ARRAY ARRAY("AUDIT_EXISTS","E")=0 ARRAY("AUDIT_EXISTS","I")=0 ARRAY("CHILD_ORDER","E")=""

> ARRAY("CHILD_ORDER","I")=""

> ARRAY("COMMENT","E")=""

> ARRAY("COMMENT","I")="" ARRAY("CONTEXT",0)=2

> ARRAY("CONTEXT",1,"METHOD_ID","E")="NASAL CANNULA" ARRAY("CONTEXT",1,"METHOD_ID","I")=4688666 ARRAY("CONTEXT",1,"OBS_ID","E")="{792FD976-2C7B-4BC0-8B6F-E62A520 ED9AA}"

> ARRAY("CONTEXT",1,"OBS_ID","I")="{792FD976-2C7B-4BC0-8B6F-

> E62A520 ED9AA}"

> ARRAY("CONTEXT",1,"SVALUE","E")=1

> ARRAY("CONTEXT",1,"SVALUE","I")=1 ARRAY("CONTEXT",1,"TERM_ID","E")="SUPPLEMENTAL OXYGEN FLOW

> RATE" ARRAY("CONTEXT",1,"TERM_ID","I")=""

> ARRAY("CONTEXT",1,"UNIT_ID","E")="LITERS PER MINUTE" ARRAY("CONTEXT",1,"UNIT_ID","I")="" ARRAY("CONTEXT",2,"OBS_ID","E")="{BED624B4-A519-4928-B6EB-65C9265 3938E}"

> ARRAY("CONTEXT",2,"OBS_ID","I")="{BED624B4-A519-4928-B6EB-

> 65C9265

> 3938E}"

> ARRAY("CONTEXT",2,"SVALUE","E")=100

> ARRAY("CONTEXT",2,"SVALUE","I")=100 ARRAY("CONTEXT",2,"TERM_ID","E")="SUPPLEMENTAL OXYGEN CONCENTRATION"

> ARRAY("CONTEXT",2,"TERM_ID","I")="" ARRAY("CONTEXT",2,"UNIT_ID","E")="PERCENTAGE" ARRAY("CONTEXT",2,"UNIT_ID","I")="" ARRAY("CORRECTION_FOR_ID","E")="" ARRAY("CORRECTION_FOR_ID","I")="" ARRAY("ENTERED_BY_ID","E")="CPPROVIDER,ONE" ARRAY("ENTERED_BY_ID","I")=547 ARRAY("ENTERED_DATE_TIME","E")="AUG 13, 2009@10:23:50" ARRAY("ENTERED_DATE_TIME","I")=3090813.10235 ARRAY("FACILITY_ID","E")=""

> ARRAY("FACILITY_ID","I")="" ARRAY("HOSPITAL_LOCATION_ID","E")="2-AS" ARRAY("HOSPITAL_LOCATION_ID","I")=1 ARRAY("METHOD_ID","E")="MONITOR" ARRAY("METHOD_ID","I")=4688665 ARRAY("OBSERVED_BY_ID","E")="CPPROVIDER,ONE" ARRAY("OBSERVED_BY_ID","I")=547 ARRAY("OBSERVED_DATE_TIME","E")="AUG 13, 2009@10:20" ARRAY("OBSERVED_DATE_TIME","I")=3090813.102 ARRAY("OBS_ID","E")="{E24715DE-3DCC-4A04-9F8B-0A7C6E8E64F4}" ARRAY("OBS_ID","I")="{E24715DE-3DCC-4A04-9F8B-0A7C6E8E64F4}" ARRAY("PARENT_ID","E")=""

> ARRAY("PARENT_ID","I")="" ARRAY("PATIENT_ID","E")="CPPATIENT,ONE" ARRAY("PATIENT_ID","I")=136 ARRAY("RANGE","E")="Normal"

> ARRAY("RANGE","I")=1 ARRAY("SOURCE","E")="CP Flowsheets" ARRAY("SOURCE","I")="CP Flowsheets" ARRAY("SOURCE_COMMENTS","E")="" ARRAY("SOURCE_COMMENTS","I")=""

> ARRAY("SOURCE_DATA_ITEM_ID","E")="CPFLOWSHEETS.EXE:6C6B9A01"

> ARRAY("SOURCE_DATA_ITEM_ID","I")="CPFLOWSHEETS.EXE:6C6B9A01" ARRAY("SOURCE_VERSION","E")="1.0.16.276" ARRAY("SOURCE_VERSION","I")="1.0.16.276" ARRAY("STATUS","E")="Verified"

> ARRAY("STATUS","I")=1

> ARRAY("SVALUE","E")=100

> ARRAY("SVALUE","I")=100

> ARRAY("TERM_ID","E")="SpO2%" ARRAY("TERM_ID","I")=4500637 ARRAY("UNIT_ID","E")="PERCENTAGE" ARRAY("UNIT_ID","I")=""

> Example of record not found:

> \>D QRYOBS^MDCLIO1("ARRAY","")

> \>ZW ARRAY

> ARRAY(0)="-1^No such observation ''" VARIABLES: Both ARRAY

> This is the name of the array to return the data in. It is a closed array and surrounded in quotes (e.g., "RESULT" or "^TMP(\$J)"). (required)

> VARIABLES: Input GUID

> This is the Global Unique ID (aka GUID - FILE 704.117, Field .01) value that identifies a record. (required)

> KEYWORDS: CLINICAL OBSERVATIONS

> 1ROUTINE: MDTERM

> COMPONENT: CVTVAL(MDVAL,MDFR,MDTO,MDROUND)

> This function converts a value from one unit of measurement to another.

> Example:

> \>S MDVAL=99,MDFR="DEGREES F",MDTO="DEGREES C",MDROUND=1

> \>W \$\$CVTVAL^MDTERM(MDVAL,MDFR,MDTO,MDROUND)

> \>37.2

> VARIABLES: Input MDVAL

> Value to convert (Required) VARIABLES: Input MDFR

> VUID or Name of unit to convert from (Must be exact match). (Required)

> VARIABLES: Input MDTO

> VUID or Name of unit to convert to (Must be exact

> 1 Patch MD\*1.0\*16 May 2010 Added MD to Callable Routines

> match) (Required) VARIABLES: Input MDROUND

> Decimal precision (optional to override conversion logic)

> KEYWORDS: CVTVAL

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following describes the installation environment for Version 1.0 of the Clinical Procedures package on the VistA server:
    1.  VA FileMan V. 22 or greater
    2.  Kernel V. 8.0 or greater
    3.  Kernel Toolkit V. 7.3 or greater
    4.  Kernel RPC Broker V. 1.1 or greater
    5.  PIMS (Patient Information Management System) V. 5.3 or greater (including):
        1.  Registration V. 5.3
        2.  Scheduling V. 5.3
    6.  Health Summary V. 2.7 or greater
    7.  HL7 (Health Level 7) V. 1.6 or greater
    8.  Consults/Request Tracking V. 3.0
    9.  TIU (Text Integration Utility) V. 1.0
    10. Order Entry V. 3.0 (CPRS (Computerized Patient Record System) V. 1.0 (GUI

> V. 18.8)) or greater

11. PCE (Patient Care Encounter) V. 1.0 or greater
12. VistA Imaging V. 3.0 or greater (includes installation of background processor and jukebox)
13. Medicine V. 2.3 (optional)
14. Vitals V 5.0 - Patches 25 and 23 must be installed.<sup>1</sup>These packages must be patched up through and including the following patches before Clinical Procedures is installed:
1.  Patch 17 of Consults/Request Tracking V. 3.0 (GMRC\*3.0\*17)
2.  Patch 112 of Order Entry V. 3.0 (OR\*3.0\*112)
3.  Patch 109 of Text Integration Utility V. 1.0 (TIU\*1.0\*109)
4.  Patch 7 of Imaging V. 3.0 (MAG\*3.0\*7) 5. Patch 93 of HL7 V. 1.6 (HL\*1.6\*93)

> 6\. Patch 98 of HL7 V. 1.6 (HL\*1.6\*98)

> 7\. If Medicine V. 2.3 is installed, you must install Patch 24 of Medicine (MC\*2.3\*24), and Patch 146 of Kernel (XU\*8.0\*146).

> 2\. 2Interface Control Registrations (formerly known as Integration Agreements) between the Clinical Procedures software and other VistA applications exist. Database Interface Control Registrations (DICR) are available on the DBA menu on Forum. For complete information regarding the DICRs for Clinical Procedures V. 1.0, please refer to the *Integration Control Registrations (Agreements) Menu* \[DBA IA ISC\] option under the *DBA* \[DBA\] option on FORUM.

> 1 Patch MD\*1.0\*12 October 2011 Removed VDEF reference.

> 2 Patch MD\*1.0\*14 March 2008 External Relations list removed. Integration Agreements renamed Interface Control Registrations.

> 1The following screen capture shows one way to access the DBA option in FORUM:

> 1 Patch MD\*1.0\*14 March 2008 Screen capture added.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1The following are the Clinical Procedures GUI Application menu option, the Clinical Procedures Site Files menu option, and the CP Hemodialysis menu option. Only the MD GUI MANAGER can be invoked independently. The MD GUI USER and MD HEMODIALYSIS USER menu option cannot be invoked independently. They are dependent upon each other. In order to use each module, please refer to the Clinical Procedures Implementation Guide to set up Clinical Procedures.

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

> NAME: MD HEMODIALYSIS USER MENU TEXT: HEMODIALYSIS USER

> TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

> TIMESTAMP OF PRIMARY MENU: 60387,39853

> RPC: MDK GET VISTA DATA RPC: MDK GET/SET RENAL DATA RPC: MDK UTILITY

> RPC: VAFCTFU CONVERT DFN TO ICN RPC: VAFCTFU CONVERT ICN TO DFN RPC: MD TMDWIDGET

> RPC: MD TMDNOTE RPC: MD TMDCIDC RPC: MD TMDLEX

> RPC: MD TMDENCOUNTER RPC: GMV MANAGER RPC: MD GATEWAY

> RPC: MD TMDSUBMITU

> 1 Patch MD\*1.0\*6 May 2008 Description modified. Hemodialysis User menu option added.

> RPC: ORWPT PTINQ RPC: GMV PTSELECT

> RPC: DG SENSITIVE RECORD ACCESS RPC: DG SENSITIVE RECORD BULLETIN RPC: MD TMDRECORDID

> UPPERCASE MENU TEXT: HEMODIALYSIS USER

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No package-wide variables are used in this application.

# SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is one SAC exemption for Clinical Procedures.

> 1\. STANDARD SECTION: 3A Namespacing DATE GRANTED: APR 25,2002

> Since the Medicine package has become a child of the Clinical Procedures package, the Clinical Procedures package is exempt from being required to export the Medicine package as part of the Clinical Procedures package.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No additional security measures are to be applied other than those implemented through Menu Manager and the package routines. Clinical Procedures uses the standard RPC broker log-in procedure to validate the user and allow access to the system.

> No additional licenses are necessary to run the software.

> Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mail groups and alerts.

> There is one mailgroup associated with this software. This mailgroup is called MD DEVICE ERRORS. The purpose of this mailgroup is to store a list of people who will be notified if a problem arises with an automated instrument. There is one alert in the software that occurs on the VistA server if the package installation does not finish. This alert is sent to the IRMS staff member who ran the installation.

2.  Remote systems.

> The application does not transmit data to any remote system/facility database.

3.  Archiving/Purging.

> 1Refer to the chapter on [<u>Archiving and Purging</u>](#archiving-and-purging) in this manual. Purging is available in the CPGateway. Refer to the “CP Gateway Configuration” chapter in the *Clinical Procedures Console Implementation Guide*.

4.  Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems. It is recommended that the CP Gateway be installed on a second machine as a backup in case the initial workstation containing the CP Gateway fails.

> 1 Patch MD\*1.0\*16 January 2011 Updated document reference.

5.  Interfacing.

> 1CP Flowsheets requires HL7 v2.4.

6.  2Electronic signatures.

> CP Flowsheets uses E-sign for notes.

7.  Menus.

> There are no options of special note for the Information Security Officers (ISO‟s) to view.

8.  Security Keys.

> The MD MANAGER key controls access to the 'Update Study Status' and the 'Delete Study' options. A user holding this key will be able to use the 'Update Study Status' option on any study currently displayed on the screen. Holders of this key will also be taken directly to the 'Update Study Status' option when opening a study marked in status 'Error'. The 'Update Study Status' option does not do any validation on the new status assigned to the study. The 'Delete Study' option will attempt to delete the study after checking the business rules on the VistA server for the study given its current status and state on the server. This key should be given only with extreme care and only to those users that fully understand the status structure, and the ramifications of changing the status or deletion of a study.

> The MD ADMINISTRATOR key is the highest level key in CP. This key controls overall maintenance functions such as downloading and installing updates from the web as well as imports of items from other sites.

> The MD HL7 MANAGER key is used to restrict the HL7 management functions.

> The MD READ-ONLY key will prevent a user from being able to file data into the CP system. A user with the MD READ-ONLY key may NOT log on to CP Console and will have limited functionality in CP Flowsheets.

> DO NOT assign MD READ-ONLY to a user concurrently with any flowsheet key other than MD HL7 MANAGER. Doing so will lead to unpredictable results.

> The MD TRAINEE key is used to signify that the signed on user is in trainee status so entries by that person can be flagged for review and approval when appropriate. Entries by a user with a MD TRAINEE key are unverified until verified by a user who is not a trainee.

> 1Patch MD\*1.0\*16 January 2011 Added VDEF reference. Added reference to E-sign. Key descriptions added.

> 2 Patch MD\*1.0\*12 October 2011 Removed VDEF reference from step 5.

Software Product Security

9.  1File Security.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 37%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>NUMBER</th>
<th>NAME</th>
<th><blockquote>
<p>DD ACCESS</p>
</blockquote></th>
<th>RD ACCESS</th>
<th>WR ACCESS</th>
<th>DEL ACCESS</th>
<th><blockquote>
<p>LAYGO ACCESS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>702</td>
<td><blockquote>
<p>CP TRANSACTION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>702.001</td>
<td>CP_TRANSACTION_TIU_HISTORY</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>702.01</td>
<td><blockquote>
<p>CP DEFINITION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
</tr>
<tr class="even">
<td>702.09</td>
<td><blockquote>
<p>CP INSTRUMENT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>#</td>
<td>#</td>
<td><blockquote>
<p>#</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>703.1</td>
<td><blockquote>
<p>CP RESULT REPORT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>703.9</td>
<td><blockquote>
<p>CP CONVERSION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>#</td>
<td>#</td>
<td>#</td>
<td><blockquote>
<p>#</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.001</td>
<td><blockquote>
<p>CP_CONSOLE_ACL</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.002</td>
<td><blockquote>
<p>CP_HL7_LOG</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.004</td>
<td><blockquote>
<p>CP_HL7_LOG_REASON</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.005</td>
<td><blockquote>
<p>CP_MOVEMENT_AUDIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.006</td>
<td><blockquote>
<p>CP_PROTOCOL_LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.007</td>
<td><blockquote>
<p>CP_SHIFT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.008</td>
<td><blockquote>
<p>CP_SCHEDULE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.101</td>
<td><blockquote>
<p>TERM</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.102</td>
<td><blockquote>
<p>TERM_TYPE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.103</td>
<td><blockquote>
<p>TERM_QUALIFIER_PAIR</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.104</td>
<td><blockquote>
<p>TERM_UNIT_CONVERSION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.105</td>
<td><blockquote>
<p>TERM_UNIT_PAIR</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.106</td>
<td><blockquote>
<p>TERM_CHILD_PAIR</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.107</td>
<td><blockquote>
<p>TERM_RANGE_CHECK</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.108</td>
<td><blockquote>
<p>TERM_MAPPING_TABLE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.109</td>
<td><blockquote>
<p>TERM_MAPPING_PAIR</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.111</td>
<td><blockquote>
<p>OBS_VIEW</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.1111</td>
<td><blockquote>
<p>OBS_VIEW_TERMINOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.1112</td>
<td><blockquote>
<p>OBS_VIEW_FILTER</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.112</td>
<td><blockquote>
<p>OBS_FLOWSHEET</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.1121</td>
<td><blockquote>
<p>OBS_FLOWSHEET_PAGE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.1122</td>
<td><blockquote>
<p>OBS_FLOWSHEET_SUPP_PAGE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.1123</td>
<td><blockquote>
<p>OBS_FLOWSHEET_TOTAL</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.113</td>
<td><blockquote>
<p>OBS_TOTAL</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.1131</td>
<td><blockquote>
<p>OBS_TOTAL_TERMINOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.115</td>
<td><blockquote>
<p>OBS_ALARM</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.116</td>
<td><blockquote>
<p>OBS_SET</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.1161</td>
<td><blockquote>
<p>OBS_SET_OBS_PAIR</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.117</td>
<td><blockquote>
<p>OBS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.118</td>
<td><blockquote>
<p>OBS_QUALIFIER</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.119</td>
<td><blockquote>
<p>OBS_AUDIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.121</td>
<td><blockquote>
<p>CP_KARDEX_ACTION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.1211</td>
<td><blockquote>
<p>CP_KARDEX_EVENTS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>704.1212</td>
<td><blockquote>
<p>CP_KARDEX_AUDIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>704.201</td>
<td>HEMODIALYSIS ACCESS POINTS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>704.202</td>
<td><blockquote>
<p>HEMODIALYSIS STUDY</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>704.209</td>
<td><blockquote>
<p>HEMODIALYSIS SETTINGS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td></td>
</tr>
</tbody>
</table>

10. References.

> There are no special reference materials for this package.

> 1 Patch MD\*1.0\*16 January 2011 Updated list.

11. Official Policies.

> There are no special official policies for this package.

> 15\. <span id="_bookmark77" class="anchor"></span>1Vendor Interfaces

> 2The original CP Manager/CP Gateway did not receive discrete data and did not map terminology. Terminology mapping as introduced in Patch 16 allows us to take vendor terminology from a vendor and translate it into VA standard terminology.

## List of Vendor Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Puritan Bennett Clinivision, Olympus Endoworks, GE Healthcare Muse and Cardinal Health Sensormedics V-max automated device interfaces are exported with CP. Many other device interfaces are also available and you can view the complete list by visiting the <u>Clinical Procedures</u> <u>website (<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>. From the Home page, select Find a Device and then search for devices by manufacturer, by type, or by name. Also refer to the ICU web site ([<u>http://vista.med.va.gov/clinicalspecialties/icu/</u>](http://vista.med.va.gov/clinicalspecialties/icu/)) for more information.

> Visit the Clinical Procedures website to view specific information for a particular device. Click the vendor name to view the web page. You can find links to the ICU interfaces at the ICU web site ([<u>http://vista.med.va.gov/clinicalspecialties/icu/findDevice.asp?by=TYPE</u>](http://vista.med.va.gov/clinicalspecialties/icu/findDevice.asp?by=TYPE)).

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 38%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Device</strong></th>
<th><strong>Vendor</strong></th>
<th><strong>Type of Procedure Performed</strong></th>
<th><strong>Type of report with Discrete data included</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Aware Gateway</td>
<td><a href="http://www.gehealthcare.com/worldwide.html"><u>GE Healthcare</u></a></td>
<td>Intensive Care Unit</td>
<td>XML</td>
</tr>
<tr class="even">
<td>Clinivision</td>
<td><a href="http://www.puritanbennett.com/"><u>Puritan Bennett</u></a></td>
<td>Respiratory</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>Endoworks</td>
<td><a href="http://www.olympus.com/"><u>Olympus</u></a></td>
<td><p>Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis,</p>
<p>Sigmoidoscopy</p></td>
<td>Text, GIF, JPG</td>
</tr>
<tr class="even">
<td>Muse</td>
<td><a href="http://www.gehealthcare.com/worldwide.html"><u>GE Healthcare</u></a></td>
<td>ECG, Exercise, Holter, Pacemaker ECG</td>
<td>PDF</td>
</tr>
<tr class="odd">
<td>PC1,PC2</td>
<td><a href="http://www.spacelabshealthcare.com/"><u>Intesys</u></a></td>
<td>Clinical Suite</td>
<td>XML</td>
</tr>
<tr class="even">
<td>Sensormedics V-max</td>
<td><p><a href="http://www.cardinal.com/"><u>Cardinal Health</u></a></p>
<p>(formerly Viasys/Sensormedics)</p></td>
<td>PFT</td>
<td>PDF</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*14 March 2008 Deleted vendor contact information for individual contacts. Updated vendor name list. Directions for finding a device on the CP website changed. Unlinked device names due to unavailable links.

> 2Patch MD\*1.0\*16 January 2011 Added paragraph about terminology mapping. Added reference to ICU web site.

> Added link to the vendor interfaces on the ICU web site. Added vendor.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 38%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>1Exalis</th>
<th><a href="http://www.gambro.com/"><u>Gambro</u></a></th>
<th>Dialysis</th>
<th>XML</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>2Ultraview</p>
<p>series</p></td>
<td><a href="http://www.spacelabshealthcare.com/"><u>Spacelabs</u></a></td>
<td>Intensive Care Unit</td>
<td>XML</td>
</tr>
<tr class="even">
<td><p>UPF</p>
<p>Hemodialysis</p></td>
<td><a href="http://www.bbraun.com/"><u>B.Braun Melsungen</u> <u>AG</u></a></td>
<td>Dialysis</td>
<td>XML</td>
</tr>
<tr class="odd">
<td>Hypercare</td>
<td><a href="http://www.fmc-ag.com/"><u>Fresenius Medical</u></a> <a href="http://www.fmc-ag.com/"><u>Care</u></a></td>
<td>Dialysis</td>
<td>XML</td>
</tr>
</tbody>
</table>

> For the latest vendor information, please see the <u>Clinical Procedures website</u> <u>(<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>.

> The Mapping Tables will change as new terms are requested and approved. Refer to the ICU website ([<u>http://vista.med.va.gov/clinicalspecialties/icu/showMapping.asp?ID=56</u>](http://vista.med.va.gov/clinicalspecialties/icu/showMapping.asp?ID=56))for the latest table.

## Device Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Here are the setup instructions and vendor contact for each device.

> <span id="_bookmark80" class="anchor"></span>Clinivision

> Vendor: Puritan Bennett Type: Respiratory

> Description:

> The uni-directional interface for this instrument is currently available.

> Requirements:

> This instrument requires a Clinivision vendor interface.

> Setup Instructions:

> This section describes the installation setup for the Clinivision system. Note that a new Protocol and HL Logical Link will need to be created for this device since it is a Persistent connected device. Clinivision is not a bi-directional device. Note: Bi-Directional Capabilities checkbox is not checked. Therefore, no outbound HL Logical Link is needed and you do not need to enter any bi-directional information.

> 1 Patch MD\*1.0\*6 May 2008 Hemodialysis exported new device entries.

> 2Patch MD\*1.0\*16 January 2011 Added Vendor. Added reference to ICU mapping tables.

> ![](md-1-23-technical-manual-cp-flowsheets/003.png)1

> <span id="_bookmark81" class="anchor"></span>Figure 2, Clinical Procedures Manager

> [Figure 2, Clinical Procedures Manager](#_bookmark81) displays the settings for the Clinivision device in CP Manager.

> 1 Patch MD\*1.0\*16 January 2011 Name removed from graphic. Added caption to figure.

> <span id="_bookmark82" class="anchor"></span>1Figure 3, Clinivision Entry in the HL Logical Link File

> [Figure 3, Clinivision Entry in the HL Logical Link File](#_bookmark82)

> 3 shows an entry in the HL Logical Link file for the Clinivision device.

> 1 Patch MD\*1.0\*16 January 2011 Added caption to figure.

> 1Figure 4, Link Protocol

> Figure 4 shows the new Protocol that will need to be entered for the Link.

![](md-1-23-technical-manual-cp-flowsheets/004.png)

> Figure 5, Clinical Procedures Manager

> 2 Figure 5 shows that the device will need to be linked to a procedure in CP Manager.

> Contact Clinivision and ask the contact to report the device to the production account, port 1030.

> Transmission Instructions:

> No information available at this time.

> Manuals:

> No information available at this time.

> 1 Patch MD\*1.0\*16 January 2011 Removed name from graphic.

> 2 Patch MD\*1.0\*6 May 2008 Screen capture updated to show new Processing Application field.

### Vendor Contacts:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>http://www.clinivision.com/contact/</u>](http://www.clinivision.com/contact/)

> Trouble Shooting:

> Is the machine plugged in? Is the machine on?

> Are all cables connected correctly?

> <span id="_bookmark83" class="anchor"></span>Endoworks

> Vendor: Olympus Type: Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy

> Description:

> The bi-directional interface for this instrument is currently available.

> Requirements:

> This instrument requires an Advanced Gateway vendor interface.

> Setup Instructions:

> The Olympus Interface is a non-persistent interface and can share its TCP/IP port address with other non-persistent devices. To configure the Olympus (Endoworks) software, it is recommended that you consult Olympus. Olympus has the correct setting for the Endoworks software that is needed to interface with CP.

> 1 The site will need to set up an Olympus type in CPManager.exe for each type of procedure, (such as Olympus (Bronchoscopy), Olympus (Colonoscopy), etc.). Please refer to the Clinical Procedures web site for the device settings for each type of procedure.

> 1Figure 6, Inbound HL Logical Link Settings

> Figure 6 displays the settings for the standard non-persistent inbound HL Logical Link.

> Figure 7, Outbound HL Logical Link Settings

> Error! Reference source not found.7 displays the settings for the standard non-persistent outbound HL Logical Link.

### Transmission Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No information available at this time

> Manuals:

> No information available at this time.

> 1 Patch MD\*1.0\*16 January 2011 Added caption to figure.

### Costs:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No information available at this time.

> Trouble Shooting:

> Is the machine plugged in? Is the machine on?

> Are all cables connected correctly?

> <span id="_bookmark84" class="anchor"></span>Muse

> Vendor: GE Healthcare Type: ECG

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The bi-directional interface for this instrument is currently available.

> Requirements:

> This instrument requires a Muse HL7 vendor interface.

> Setup Instructions:

> The Muse Interface is a Persistent Interface and must have its own TCP/IP Port address. For configuring the Muse software, it is recommended that you consult with GE Healthcare. GE Healthcare has the correct setting for the Muse software that is needed to interface with CP.

> 1The Muse can be set up for different Cardiology procedures such as Holter and Exercise Tolerance Test. Please refer to the Clinical Procedures web page for the setup of the device in CPManager.exe for each type of procedure.

> Transmission Instructions:

> To send data to Clinical Procedures once the results have been sent from the Cart to the MUSE server, follow these steps:

1.  The MUSE generated hard copy is assigned to a cardiologist for over-reading (reviewing).
2.  Changes are made on the interpretation, signed by the doctor and returned to the EKG Department.
3.  EKG Tech logs on to the MUSE. (All users of the MUSE are assigned a number and password with certain levels of NECESSARY access.)
4.  EKG Tech selects over reader (reviewing Cardiologist).
5.  EKG Tech selects the patient.
6.  EKG Tech selects and then edits the interpretation.

> 1 Patch MD\*1.0\*6 May 2008 Added information about setting up different procedures.

7.  EKG Tech selects either Confirm and Print, or Confirm. If Confirm and Print is selected, the HL7 result is sent, and the report is printed. If only Confirm is selected, just the HL7 result is sent.

> Manuals:

> No information available at this time.

> Costs:

> No information available at this time.

> Trouble Shooting:

1.  Is the machine plugged in?
2.  Is the machine on?
3.  Are all cables connected correctly?

> <span id="_bookmark85" class="anchor"></span>Sensormedics V-MAX

> Vendor: Cardinal Health Type: PFT

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The bi-directional interface for this instrument is currently available.

> Requirements:

> This instrument requires a Netlink vendor interface.

> 1Configuration Files:

> This file contains the configuration parameters for the Vmax software. The vendor should already have a copy of this file.

> Setup Instructions:

> The Sensormedics Interface is a Non-Persistent Interface and can share TCP/IP ports with other Non-Persistent device interfaces. The Sensormedics V-MAX software must have a shared directory to hold the report document that is created. The directory might be on the PC or on a network share. The key point is that the directory must be accessible from the Sensormedics V- MAX software.

1.  Start the Sensormedics V-MAX software.
2.  Click on the Reports Button.
3.  Select the Netlinks/IS menu from the menu bar.
4.  Select TCP/IP from the File Menu on the menu bar.
5.  Enter the TCP/IP and Port address to the listener that will be receiving the data from the Sensormedics V-MAX software.
6.  Exit back to the Reports Screen.

> 1 Patch MD\*1.0\*14 March 2008 References to Vmaxconfigfile.zip and sample reports were removed because they are no longer hosted on the Clinical Procedures website.

7.  Select Setup from the File Menu and enter the Full NETWORK path to the Share directory where you want the PDF document to be stored.

> Transmission Instructions:

> A path must be setup where the PDF report will be stored prior to being transmitted to V*IST*A Imaging. This path is usually preset to C:\PDFFiles\\ and should be changed to \\(PC Network name)\PDFFiles\\ Also, the directory C:\PDFFiles should have Share enabled with Read, Write, Delete permissions for both Imaging and the PC on which the share directory exists.

> The following instructions are for transmitting the final patient report to Clinical Procedures. Note: If the patient whose results you wish to send is already being displayed on the monitor, you can start at step 5.

1.  From the Vmax Program Manager screen click the Find Patient Button.

> ![](md-1-23-technical-manual-cp-flowsheets/005.png) The Find Patient window opens. No patients are displayed.

2.  Set search criteria (Last Name, ID, etc.) if any, and click on F1. A list of patients matching your search criteria appears.
3.  Select the patient whose results you wish to send by clicking on their name. The selected patient’s name is highlighted.
4.  Click the F3 button to load the selected patients results data. The Vmax Program Manager screen reappears.
5.  From the Vmax Program Manager screen click the Reports Button.

> ![](md-1-23-technical-manual-cp-flowsheets/006.png) The Reports screen appears.

6.  Select the report to process for this patient from the Reports selection box on the left side of the screen. The selected report appears in the upper left box as the Default Patient Report.
7.  From the Menu bar click the PrintPDF button to compile the PDF report. A dialog box appears momentarily, indicating the progress of the PDF file creation.
8.  From the Menu bar click Netlink/IS® to open the Netlink Transmission Manager.

> ![](md-1-23-technical-manual-cp-flowsheets/007.png) 1 The Transmission Manager screen appears

> Files to be backed up:

> 1 Patch MD\*1.0\*16 January 2011 Name removed from graphic.

> You need to backup these files to preserve the operation of Vmax. These files should be backed up after the Vmax is working in production. This list was last updated on May 13, 2003.

> Vision folder files used in Netlink communications.

> (Depending on software version and configuration, not all files may be present) All files are located in the C:\Vision folder

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

> The following files are shipped standard with the software and are NOT user-modifiable. They should only be loaded from the software install disk.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
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
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Xreplace</p></li>
</ul></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The following files are modified by the software during operation and should NOT be user- modified: They should only be generated by running the software.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
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

> 1Please refer to the Clinical Procedures web page for the device setup in CPManager.exe.

> Manuals:

> No information available at this time.

> Costs:

> No information available at this time.

> Trouble Shooting:

> Is the machine plugged in? Is the machine on?

> Are all cables connected correctly?

> <span id="_bookmark86" class="anchor"></span>B. Braun

> Vendor: B. Braun Melsungen AG Type: Hemodialysis

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Both uni-directional and bi-directional interfaces for this instrument are currently available.

> Requirements:

> This device uses B. Braun’s UPF Hemodialysis software.

> 1 Patch MD\*1.0\*6 May 2008 Added reference to CP web page for device setup. Added Hemodialysis vendor B. Braun.

### Setup Instructions (B. Braun Device Settings for CP Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Setting For:</strong></th>
<th>Clinical Procedures Device Manager</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Procedure Type (HL7 Universal</strong></p>
<p><strong>Service ID)</strong></p></td>
<td>BRAUN (Bi-Directional)</td>
</tr>
<tr class="even">
<td><strong>Settings:</strong></td>
<td><p>Device Setup for the BRAUN (Bi-Directional)</p>
<p>NAME: BRAUN (Bi-Directional) PRINT NAME: BBRAUN</p>
<p>DESCRIPTION: BBraun Dialysis Device Interface M ROUTINE: MDHL7D</p>
<p>PACKAGE CODE: CP V1.0 ATTACH: UNC</p>
<p>BI-DIRECTIONAL: YES HL7 INST: BRAUN</p>
<p>HL7 UNIVERSAL SERVICE ID:</p>
<p>Verified at Hines By: W. A. Ackerman</p></td>
</tr>
</tbody>
</table>

> <span id="_bookmark87" class="anchor"></span>1Fresenius Medical Care

> Vendor: Fresenius Medical Care Type: Hemodialysis

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Both uni-directional and bi-directional interfaces for this instrument are currently available.

> Requirements:

> This device uses Fresenius’s Hypercare software.

> 1 Patch MD\*1.0\*6 May 2008 Added Hemodialysis vendor Fresenius.

### Setup Instructions (Hypercare Device Settings for CP Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Setting For:</strong></th>
<th>Clinical Procedures Device Manager</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Procedure Type (HL7 Universal</strong></p>
<p><strong>Service ID)</strong></p></td>
<td>Fresenius (Bi-directional)</td>
</tr>
<tr class="even">
<td><strong>Settings:</strong></td>
<td><p>Device Setup for the Fresenius (Bi-directional)</p>
<p>NAME: Fresenius (Bi-directional) PRINT NAME: Fresenius</p>
<p>DESCRIPTION: Fresenius Dialysis Device Interface M ROUTINE: MDHL7D</p>
<p>PACKAGE CODE: CP V1.0 ATTACH: UNC</p>
<p>BI-DIRECTIONAL: YES</p>
<p>HL7 INST: Fresenius</p>
<p>HL7 UNIVERSAL SERVICE ID:</p>
<p>Verified at Hines By: W. A. Ackerman</p></td>
</tr>
</tbody>
</table>

> <span id="_bookmark88" class="anchor"></span>1Gambro

> Vendor: Gambro Type: Hemodialysis

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Both uni-directional and bi-directional interfaces for this instrument are currently available.

> Requirements:

> This device uses Gambro’s Exalis software.

> Setup Instructions:

> Interface Notes for Exalis to Hemodialysis

- Exalis runs on a PC. VA-Exalis_Interface runs on the same PC as Exalis. The PC must be networked so that there can be a TCP\IP connection between VistA and VA- Exalis_Interface. The Exalis software runs as a standard application (not a service), thus requiring that the PC has been logged on with some user account rather than simply

> 1 Patch MD\*1.0\*6 May 2008 Added Hemodialysis vendor Gambro.

> turned on. At this time VA-Exalis_Interface, is a standard application. It may become a service if design and resource constraints allow.

- VA-Exalis_Interface is a .NET application and so requires the .NET Framework 1.1 Redistributable which is freely downloadable from Microsoft and will be included on the VA-Exalis_Interface CDROM.

> 1B. Braun Device Settings for CP Manager

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Setting For:</strong></th>
<th>Clinical Procedures Device Manager</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Procedure Type (HL7 Universal Service ID)</strong></td>
<td>GAMBRO_EXALIS</td>
</tr>
<tr class="even">
<td><strong>Settings:</strong></td>
<td><p>Device Setup for the GAMBRO_EXALIS</p>
<p>NAME: GAMBRO_EXALIS</p>
<p>PRINT NAME: Gambro Exalis DESCRIPTION: Cobe Dialysis Device Interface M ROUTINE: MDHL7D</p>
<p>PACKAGE CODE: CP V1.0 ATTACH: UNC</p>
<p>BI-DIRECTIONAL: NO</p>
<p>HL7 INST: GAMBRO_EXALIS HL7 UNIVERSAL SERVICE ID:</p>
<p>-</p>
<p>Verified at Hines By: W. A. Ackerman</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1\*16 May 2010 Removed terminology dictionaries for Aware and Spacelabs.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
> Action A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.
> 1ADP Automated Data Processing
> ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.
> ADT Advanced Data Type (InterSystems Cache). Also Admissions, Discharges, Transfers.
> AP Arterial pressure
> 2API Application programming interface, an interface that a computer system, library or application provides in order to accept requests for services from other programs, and/or to allow data to be exchanged between them.
> Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.
> Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
> Assessment Assessment is the documentation of a clinician ‟s observations and interpretation of a patient’s clinical state based on a particular set of observations. The documentation is in the form of name-value pairs with values selected from a predetermined set, of name-value pairs in which the value is a number or set of numbers, or of free text.
> ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.
> 1 Patch MD\*1.0\*16 January 2011 Glossary terms added.
> 2 Patch MD\*1.0\*6 May 2008 Glossary term added.
> Attachments Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:
> .txt Text files
> .rtf Rich text files
> .jpg JPEG Images
> .jpeg JPEG Images
> .bmp Bitmap Images
> .tiff TIFF Graphics (group 3 and group 4 compressed and uncompressed types)
> .pdf Portable Document Format
> .html Hypertext Markup Language
> .DOC (Microsoft Word files) are not supported. Be sure to convert .doc files to .rtf or to .pdf format.
> Background Processing Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.
> Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
> Boilerplate Text A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.
> 1BP Blood pressure
> 2Broker Software which mediates between two objects, such as a client and a server or a repository and a requestor.
> Browse Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).
> Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
> 1 Patch MD\*1.0\*16 January 2011 Glossary term added.
> 2 Patch MD\*1.0\*6 May 2008 Glossary term added.
> Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).
> 1CAC Clinical Application Coordinator
> Care Action Care action is an intervention scheduled on a patient that may or may not be ordered.
> CCB Change Control Board
> CCDSS Clinical Care Delivery Support System
> CCOW Clinical Context Object Workgroup. An HL7 standard protocol through which applications can synchronize in real-time, enabling Single Sign On and Context Management.
> CDR Clinical Data Repository
> CGI CliO Generic Interface
> CIS Clinical Information System. An ICU Clinical Information System is any hardware/software system that works in concert to collect, store, display, and/or enable manipulation of potential, clinically relevant information. A CIS also acts as an HL7 Gateway. Vendors of monitors and other instruments used in an ICU provide the CIS. The primary distinguishing feature of this CIS is its ability to manually select a subset of all available data and send it to the EMR.
> Class Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
> Clinical Flowsheets A patch to the Clinical Procedures package that allows the collection of discrete data from medical devices or a Clinical Information System. It is a complete HL7 standardized instrument interface developed and owned by the Department of Veterans
> Clinical Reminders A system which allows caregivers to track and improve preventive healthcare and disease treatment for patients and to ensure timely clinical interventions.
> CliO Clinical Observations database
> 1 Patch MD\*1.0\*16 January 2011 Glossary terms added.
> 1CM Configuration Management
> Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
> Contingency Plan A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
> CP Clinical Procedures.
> CP Console An application used by Administrators to configure the CP Flowsheets application and its interface settings.
> CP Definition CP Definitions are procedures within Clinical Procedures.
> CP Flowsheets A GUI component of the Clinical Flowsheets package. Its primary functions are to provide a means to display data collected from a medical device and to allow manual entry of data. Additional functionality is provided to display and print reports, verify incoming observational data, add comments, correct erroneous information, and submit TIU Notes to CPRS.
> 2CP Gateway The service application that prepares the data contents of HL7 messages for use in CP Hemodialysis. It requires no direct user interaction.
> CP Study A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.
> CPRS Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.
> Data Dictionary A description of file structure and data elements within a file.
> DBIA Database integration agreement.
> Delphi A programming language, also known as Object Pascal.
> Device A hardware input/output component of a computer system (e.g., CRT, printer).
> 1Display Interval The amount of time that displays in each column of a flowsheet view. Display interval is configurable from 1 minute to 24 hours. Shorter interval settings can improve readability when a large amount of data is received over a short period of time. Longer interval settings allow you to view longer periods of time while reducing the amount of horizontal scrolling necessary to view all columns.
> 2DLL Dynamically-Linked Library – provides the benefit of shared libraries.
> DOB Date of Birth
> Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.
> Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.
> DUZ The internal entry number inside FileMan for a particular user.
> Edit Used to change/modify data typically stored in a file.
> EMR Electronic Medical Record, the HealtheVet, is the permanent medical record for a patient in VistA
> Field A data element in a file.
> File The M construct in which data is stored for retrieval at a later time. A computer record of related information.
> File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.
> File Server A machine where shared software is stored.
> 1 Patch MD\*1.0\*16 January 2011 Glossary terms added.
> 2 Patch MD\*1.0\*6 May 2008 Glossary terms added.
> 1Flowsheet A flowsheet is a table, chart, spreadsheet, or other method of displaying data on two axes. One axis represents time intervals and the other axis represents the readings from an ICU monitor documented at the various time intervals.
> Flowsheet view A customizable subsection (or page) of a flowsheet. Flowsheet views are created by adding and arranging terms and choosing their default qualifiers. Flowsheet views can be set up to display observations, provide a way to manually enter observations, and display reports.
> Fluid off Cumulative volume of fluid removed from patient.
> Gateway The software that performs background processing for Clinical Procedures.
> Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.
> GUI Graphical User Interface - a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.
> HDR Health Data Repository
> HEP (CUM) Cumulative heparin infusion
> HFS Host File System
> HIPAA Health Insurance Portability and Accountability Act
> 2HL7 Health Level 7 messaging, a language which various healthcare systems use to interface with one another.
> HL7 Gateway Hardware or software provided by a vendor that is able to receive information in a vendor ‟s proprietary format from one or more ICU monitors and other instruments, to translate the data into standardized HL7 message format, and to pass the messages to other systems.
> HR Heart rate
> 1HSD&D Office of Information (OI), Health Systems Design & Development HSITES Health Systems Implementation, Training, Education and Support ICU Intensive Care Unit
> IEN Internal Entry Number
> IJ Internal jugular
> Instrument An instrument is a device used to perform a medical function on a patient. In Clinical Flowsheets instrument refers to ICU monitors, which are electronic devices that collect and/or display information concerning the physical state of a patient. Usually, the monitor attaches to a patient and takes readings over time without requiring intervention for each reading.
> Interpreter Interpreter is a user role exported with USR\*1\*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation.
> Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application.
> These individuals are „clinical update users‟ for a given consult service.
> IRM Information Resource Management.
> IRMS Information Resource Management Service.
> JCAHO Joint Commission on Accreditation of Healthcare Organizations
> Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
> LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
> LPES/CPS Legacy Product Enterprise Support/Clinical Product Support. Enterprise Product Support (formerly Enterprise VistA Support).
> 1Log A list that provides the time and description of events as they occur
> M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi- Programming System. This is the programming language used to write all VistA applications.
> MailMan An electronic mail, teleconferencing, and networking system.
> Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
> Module A component of a software application that covers a single topic or a small section of a broad topic.
> MUMPS Massachusetts General Hospital Utility Multi-Programming System. Obsolete; now known as "M" programming language.
> Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.
> Network Server Share A machine that is located on the network where shared files are stored.
> Notebook This term refers to a GUI screen containing several tabs or pages.
> 2NTE Not to exceed
> OI Office of Information, formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.
> Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.
> Optional page One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pacemaker) on its own flowsheet view. An Optional Page can display only once in a given flowsheet. If an optional page is closed and then redisplayed, any data previously entered still displays.
> Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.
> Page This term refers to a tab on a GUI screen or notebook.
> 1 Patch MD\*1.0\*16 January 2011 Glossary terms added.
> Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
> PCE Patient Care Encounter
> PIMS Patient Information Management System
> Pivot Swap the axes of a table or chart. This causes the values that were displayed along the vertical axis to be displayed along the horizontal axis and the values that were displayed along the horizontal axis to be displayed along the vertical axis.
> PM Project Manager
> Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
> PRN As needed
> Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.
> Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
> 1Protocol A set of rules governing communication within and between computing endpoints.
> 2PS Provider Systems PV Pulmonary Vascular QG Quality Gate
> Qualifiers A word or phrase that provides specific information about an observation. For example, an observation could have qualifiers such as Unit (f=degrees Fahrenheit, c=degrees Celsius, bpm=beats per minute, rpm=respirations per minute, etc.), Method (Cu=cuff BP, Dop=Doppler BP, etc.), Position (Ly=lying, Si=sitting, St=standing, etc.), Location (La=left arm, LL=left leg, RA=right arm, RL=right leg, etc.), Quality (A=accurate, E=Estimated), etc.
> Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
> 1 Patch MD\*1.0\*6 May 2008 Glossary terms added.
> RAID Redundant array of inexpensive disks, a data storage scheme using multiple hard drives to share or replicate data among the drives.
> Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.
> \<RET\> Carriage return.
> Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
> RPC Remote Procedure Call, a protocol that allows a computer program running on one host to cause code to be executed on another host.
> Rx Prescription
> SAC Standards and Conventions.
> Security Key A function which unlocks specific options and makes them accessible to an authorized user.
> Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
> 1Service A long-running executable designed to perform specific functions without user intervention. Windows services can be configured to restart automatically when the operating system is rebooted.
> SGML Standard Generalized Markup Language
> Shift A period of time that can be defined in CP Flowsheets. This often corresponds to the time an individual an individual works.
> Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
> Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
> SQA Software Quality Assurance
> SRS Software Requirements Specification
> SSN Social Security Number
> Status Symbols Codes used in order entry and Consults displays to designate the status of the order.
> STS Standards and Terminology Services. An initiative to create and maintain standardized terminology throughout the VA by assigning a code to every term.
> Supplemental page One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pressure wound) on its own flowsheet view. Multiple supplemental pages can be added to a single flowsheet in order to track numerous specific
> Tab One of the five primary GUI screens of the CP Flowsheets application: Flowsheet, Alarms, Reports, Log Files, and HL7 Monitor.
> Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
> Terminology Standardization of words and terms used in Flowsheets.
> Title Titles are definitions for documents. They store the behavior of the documents which use them.
> TIU Text Integration Utilities. 1TMP Trans membrane pressure UFR Ultrafiltration rate
> UI User Interface
> 2UNC Universal naming Convention.
> Untrusted device A medical instrument which has not been mapped for use with the Clinical Flowsheets package. Data sent from an untrusted device will not display in a flowsheet view until someone reviews it (on the CP Flowsheets Log Files tab) and marks it as verified.
> URL Uniform Resource Locator – a means of finding a resource (such as a web page or a device) on the Internet.
> URR Urea reduction ratio - The reduction in urea as a result of dialysis
> UNC Universal naming Convention.
> URL Uniform Resource Locator – a means of finding a resource (such as a web page or a device) on the Internet.
> User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
> User Class User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.
> User Role User Role identifies the role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).
> Utility An M program that assists in the development and/or maintenance of a computer system.
> UUEncoded format A form of binary to text encoding whose name derives from "Unix-to-Unix encoding."
> VA Department of Veterans Affairs; formerly the Veterans Administration.
> VAMC Department of Veterans Affairs Medical Center
> 1
> Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
> VHA Veterans Health Administration
> VistA Veterans Health Information Systems and Technology Architecture.
> VP Venous pressure
> VUID Veterans Health Administration (VHA) Unique Identifier. A unique identifier that specifies individual data elements or observations. In Clinical Flowsheets, each term is assigned a VUID.
> Workstation A personal computer running the Windows 9x or NT operating system.
> 2XML Extensible Markup Language – A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.
> XMS Extended Memory Specification – The specification describing the use of extended memory in real mode for storing data.


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*16 Technical Manual (CP Flowsheets)

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

> Contains the option for the RPC. RPC is called as shown: Options and other required parameters include:

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

1.  The internal variable pointer (nnn;GLO(123,)
2.  The external format of the variable pointer using the 3 character prefix (prefix.entryname)
3.  The prefix alone to set the parameter based on current entity selected. (prefix)

> Method 3 uses the following values for the following entities: USR Current value of DUZ

> DIV Current value of DUZ(2) SYS System (domain)

> PKG Package to which the parameter belongs

> INPUT PARAMETER: PAR PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: NO

> SEQUENCE NUMBER: 3 DESCRIPTION:

> A parameter is the actual name which values are stored under. The name of the parameter must be namespaced and it must be unique. Parameters can be defined to store the typical package parameter data (e.g. the default add order screen), but they can also be used to store GUI application screen settings a user has selected (e.g. font or window width). When a parameter is defined, the entities, which may set that parameter, are also defined. The definition of parameters is stored in the PARAMETER DEFINITION file (#8989.51).

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

> MAXIMUM DATA LENGTH: 20 REQUIRED: NO

> SEQUENCE NUMBER: 3 DESCRIPTION:

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

> 1NAME: MD TMDCIDC TAG: RPC

> ROUTINE: MDRPCW RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This RPC will do the following:

> 1 Patch MD\*1.0\*6 May 2008 RPCs added.

> Input Parameter: RESULTS - (Both Input/Output) Passed in as the array to

> return the results.

> OPTION - (Input) PROC - obtain a list of Procedures

> defined for a clinic.

> DIAG - obtain a list of diagnosis defined for a clinic.

> SCDISP - Obtain the patient's service connection and rated

> disability.

> DFN - (Input) Patient internal entry number MDSTUD - (Input) CP Study internal entry number

> RETURN PARAMETER DESCRIPTION:

- D RPC^MDRPCW(.RESULTS,"PROC",162,212)
- ZW RESULTS RESULTS=^TMP("MDRPCW",539023945)

> @RESULTS@(0)=count of array element (0 if nothing found) @RESULTS@(1)=^group header

> @RESULTS@(2) = P1 := cpt or icd code / ien of other items P2 := user defined text

> P6 := user defined expanded text to send to PCE P7 := second code or item defined for line item P8 := third code or item defined for line item P9 := associated clinical lexicon term

- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,0) = 7

> ^TMP("MDRPCW",539023945,1) = ^PFT PROCEDURES

> ^TMP("MDRPCW",539023945,2) = G0125^Lung image (PET) ^^^^^^^

> ^TMP("MDRPCW",539023945,3) = S9473^Pulmonary rehabilitation pro^^^^^^^

> ^TMP("MDRPCW",539023945,4) = S2060^Lobar lung transplantation ^^^^^^^

> ^TMP("MDRPCW",539023945,5) = S2060^Lobar lung transplantation ^^^^^^^

> ^TMP("MDRPCW",539023945,6) = A4480^Vabra aspirator ^^^^^^^

> ^TMP("MDRPCW",539023945,7) = 43450^DILAT ESOPH-SOUND/BOUGIE-1/M^^^^^^^

> Global ^

- D RPC^MDRPCW(.RESULTS,"DIAG",162,212)
- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,0) = 31

> ^TMP("MDRPCW",539023945,1) = ^PFT

> ^TMP("MDRPCW",539023945,2) = 397.1^RHEUM PULMON VALVE DIS^^^^^^^269587

> ^TMP("MDRPCW",539023945,3) = 417.1^PULMON ARTERY ANEURYSM^^^^^^^269688

> ^TMP("MDRPCW",539023945,4) = 417.8^PULMON CIRCULAT DIS NEC^^^^^^^269690

> ^TMP("MDRPCW",539023945,5) = 417.9^PULMON CIRCULAT DIS NOS^^^^^^^269691

> ^TMP("MDRPCW",539023945,6) = 424.3^PULMONARY VALVE DISORDER^^^^^^^101164

> ^TMP("MDRPCW",539023945,7) = 516.1^IDIO PULM HEMOSIDEROSIS^^^^^^^61083

> ^TMP("MDRPCW",539023945,8) = 746.01^CONG PULMON VALV ATRESIA^^^^^^^265805

> ^TMP("MDRPCW",539023945,9) = 673.82^PULM EMBOL NEC-DEL W P/P^^^^^^^271756

> ^TMP("MDRPCW",539023945,10) = 747.3^PULMONARY ARTERY ANOM^^^^^^^27406

> ^TMP("MDRPCW",539023945,11) = 770.3^NB PULMONARY HEMORRHAGE^^^^^^^273240

> ^TMP("MDRPCW",539023945,12) = 794.2^ABN PULMONARY FUNC STUDY^^^^^^^273442

> ^TMP("MDRPCW",539023945,13) = 901.41^INJURY PULMONARY ARTERY^^^^^901.42^^275136

> ^TMP("MDRPCW",539023945,14) = 162.3^MAL NEO UPPER LOBE LUNG^^^^^162.4^162.5^73534

> ^TMP("MDRPCW",539023945,15) = 235.7^UNC BEHAV NEO LUNG^^^^^^^267754

> ^TMP("MDRPCW",539023945,16) = 875.0^OPEN WOUND OF CHEST^^^^^^^274991

> ^TMP("MDRPCW",539023945,17) = 162.9^MAL NEO BRONCH/LUNG NOS^^^^^^^73521

> ^TMP("MDRPCW",539023945,18) = 786.6^CHEST SWELLING/MASS/LUMP^^^^^^^273380

> ^TMP("MDRPCW",539023945,19) = 518.89^OTHER DISEASE OF LUNG, NEC^^^^^^^87486

> ^TMP("MDRPCW",539023945,20) = ^BRONCHOSCOPY

> ^TMP("MDRPCW",539023945,21) = 012.20^ISOL TRACHEAL TB- UNSPEC^^^^^012.21^^266107

> ^TMP("MDRPCW",539023945,22) = 012.22^ISOL TRACH TB-EXAM UNKN^^^^^^^266109

> ^TMP("MDRPCW",539023945,23) = 012.23^ISOLAT TRACH TB-MICRO DX^^^^^^^266110

> ^TMP("MDRPCW",539023945,24) = 012.24^ISOL TRACHEAL TB-CULT DX^^^^^^^266111

> ^TMP("MDRPCW",539023945,25) = 748.61^CONGEN BRONCHIECTASIS^^^^^^^265478

> ^TMP("MDRPCW",539023945,26) = 011.50^TB BRONCHIECTASIS- UNSPEC^^^^^011.51^^266056

> ^TMP("MDRPCW",539023945,27) = 784.1^THROAT PAIN^^^^^^^276881

> ^TMP("MDRPCW",539023945,28) = 784.8^HEMORRHAGE FROM THROAT^^^^^^^273371

> ^TMP("MDRPCW",539023945,29) = 034.0^STREP SORE THROAT^^^^^^^114610

> ^TMP("MDRPCW",539023945,30) = 466.11^AC. BRONCH/RESP SYNCYT V

> (RSV)^^^^^466.19^

> ^304309

> ^TMP("MDRPCW",539023945,31) = 530.10^ESOPHAGITIS, UNSP.^^^^^^^295809

> Global ^

- D RPC^MDRPCW(.RESULTS,"SCDISP",17,212)

> @RESULTS@(n)="Lines of text"

- D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

> ^TMP("MDRPCW",539023945,1) = Service Connected: 50%

> ^TMP("MDRPCW",539023945,2) = Rated Disabilities: NONE STATED

> Global ^

> NAME: MD TMDENCOUNTER TAG: GETENC

> ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This remote procedure will return the existing data in an encounter. INPUT PARAMETER: STUDY PARAMETER TYPE: REFERENCE

> REQUIRED: YES SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the CP Study internal entry number. RETURN PARAMETER DESCRIPTION:

> The result is returned in ^TMP("MDENC",\$J) global.

> ^TMP("MDENC",\$J,1)="SC";0/1^0/1;"AO";0/1^0/1;"IR";0/1^0/1;"EC";0/1^0/ 1;"MST";0/1^0/1;"HNC";0/1^0/1;"CV";0/1^0/1

> P1 = "SC" - Service Connected

> P2 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P3 = "AO" - Agent Orange Exposure

> P4 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P5 = "IR" - Ionizing Radiation Exposure

> P6 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P7 = "EC" - Environmental Contaminants

> P8 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P9 = "HNC" - Head and/or Neck Cancer

> P10 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P11 = "MST" - Military Sexual Trauma

> P12 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked

> second "^" piece - If Scheduling has the answer, 1 = yes 0 = no P13 = "CV" - Combat Veteran

> P14 = first "^" piece 1 if the condition can be answered

> 0 if the condition should be null not asked second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

> ^TMP("MDENC",\$J,n)="PRV"^CODE^^NARR^^Primary (1=Yes,0=No)

> P1 = "PRV"- Provider segment

> P2 = CODE - New Person internal Entry Number P3 = Null

> P4 = NARR - Provider name P5 = Null

> P6 = Primary - 1/0/null (1=Yes,0/Null=No)

> ="POV"^ICD9 IEN^ICD9 CODE^provider narrative category^ provider narrative (Short Description)^Primary (1=Yes,0/Null=No)

> P1 = "POV" - ICD segment

> P2 = ICD internal entry number P3 = ICD9 Code

> P4 = Provider Narrative Category P5 = Short Description

> P6 = Primary - 1/0/null (1=Yes,0/Null=No)

> ="CPT"^CPT IEN^CPT CODE^provider narrative category^ provider narrative (Short Description)^^Quantity

> P1 = "CPT" - CPT segment

> P2 = CPT internal entry number P3 = CPT Code

> P4 = Provider Narrative Category (CPT Category Grouping) P5 = Short Description

> P6 = null

> P7 = Quantity

> NAME: MD TMDLEX TAG: LEX

> ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This RPC will return a list of CPT or ICD for a search typed in. INPUT PARAMETER: MDSRCH PARAMETER TYPE: REFERENCE

> REQUIRED: YES SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the text typed in for the look-up.

> INPUT PARAMETER: MDAPP PARAMETER TYPE: REFERENCE REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is the application indicator. It is either "CPT" or "ICD". RETURN PARAMETER DESCRIPTION:

> ^TMP("MDLEX",\$J,#)=P1 - CPT/ICD Code

> P2 - Internal Entry Number P3 - Lexicon text

> \>D LEX^MDRPCW1(.RESULTS,"BORE","CPT")

> \>ZW RESULTS RESULTS="^TMP("MDLEX",539152953)"

> \>D ^%G

> Global ^TMP("MDLEX",\$J -- NOTE: translation in effect

> ^TMP("MDLEX",539152953,1)=86618^302213^Borella Burgdorferi (Lyme Disease) Antibody (CP T-4 86618)

> NAME: MD TMDNOTE TAG: RPC

> ROUTINE: MDRPCNT RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This remote procedure call does the following:

> Accepts the following Inputs:

> RESULTS - Both (Input and Output) - Passed in as the array to return results in.

> OPTION - NEWDOC = Add additional new document to the Hemodialysis study.

> NOTELIST = Returns a list of documents associated with the study. The pieces returned are: Note IEN, Note title, Date/Time Creation, Author, and Hospital Location.

> VIEWTIU = Return the text lines of a document from NOTELST.

> MDSID - Study internal Entry Number.

> MDTIU - TIU Document Internal Entry Number.

> MDDTE - Date/Time of Document Creation.

> MDAUTH - Author of document.

> MDESIG - Encrypted Electronic Signature.

> MDTXT - Text of the new document in an array.

> Return Results are the following:

> OPTION = NEWDOC

- D RPC^MDRPCNT(.RESULTS,"NEWDOC",904,"",3050524.0915,679,74RHLld;flk,MDTXT)
- D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

> ^TMP("MDKUTL",538992716,0) = Note internal entry number or -1^Error Message

> OPTION = NOTELIST

- D RPC^MDRPCNT(.RESULTS,"NOTELST",476)
- D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

> ^TMP("MDKUTL",538992716,1) = 968^PROCEDURE NOTE^OCT 10, 2001@17:08:36

> ^MDPROVIDER,ONE ^PROSTHETICS

> ^TMP("MDKUTL",538992716,2) = 969^PROCEDURE NOTE^OCT 10, 2001@17:10:44^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,3) = 970^PROCEDURE NOTE^OCT 10, 2001@17:11:50^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,4) = 971^PROCEDURE NOTE^OCT 10, 2001@17:15:45^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,5) = 972^PROCEDURE NOTE^OCT 10, 2001@17:16:34^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,6) = 974^PROCEDURE NOTE^OCT 11, 2001@10:56:03^^PROSTHET

> I

> CS

> ^TMP("MDKUTL",538992716,7) = 975^PROCEDURE NOTE^OCT 11, 2001@12:50:29^^PROSTHET

> I

> CS

> Global ^

> OPTION = VIEWTIU

- D RPC^MDRPCNT(.RESULTS,"VIEWTIU",476,968)
- D ^%G

Global ^TMP("TIUVIEW",\$J

TMP("TIUVIEW",\$J

> ^TMP("TIUVIEW",538992716,1) = TITLE: PROCEDURE NOTE

> ^TMP("TIUVIEW",538992716,2) = DATE OF NOTE: OCT 10, 2001@17:08:36 ENTRY DATE:

> O

> CT 10, 2001@17:08:36

> ^TMP("TIUVIEW",538992716,3) = AUTHOR: MDPROVIDER,ONE EXP COSIGNER:

> ^TMP("TIUVIEW",538992716,4) = URGENCY: STATUS:

> COMPLETED

> ^TMP("TIUVIEW",538992716,5) =

> ^TMP("TIUVIEW",538992716,6) = PROCEDURE SUMMARY CODE: Abnormal

> ^TMP("TIUVIEW",538992716,7) = DATE/TIME PERFORMED: OCT 15, 2001

> ^TMP("TIUVIEW",538992716,8) =

> ^TMP("TIUVIEW",538992716,9) = \*\*\* PROCEDURE NOTE Has ADDENDA \*\*\*

> ^TMP("TIUVIEW",538992716,10) =

> ^TMP("TIUVIEW",538992716,11) = Complete consult 1104. 6 attached images.

> ^TMP("TIUVIEW",538992716,12) =

> ^TMP("TIUVIEW",538992716,13) = /es/ MDPROVIDER,ONE

> ^TMP("TIUVIEW",538992716,14) =

> ^TMP("TIUVIEW",538992716,15) = Signed: 10/15/2001 13:02

> ^TMP("TIUVIEW",538992716,16) =

> ^TMP("TIUVIEW",538992716,17) = 10/15/2001 ADDENDUM STATUS:

> COMPLETED

> ^TMP("TIUVIEW",538992716,18) = aDDENDUM LA LA LA

> ^TMP("TIUVIEW",538992716,19) = LA LA LA

> ^TMP("TIUVIEW",538992716,20) =

> ^TMP("TIUVIEW",538992716,21) = /es/ MDPROVIDER,ONE

> ^TMP("TIUVIEW",538992716,22) =

> ^TMP("TIUVIEW",538992716,23) = Signed: 10/15/2001 13:04

> NAME: MD TMDSUBMITU TAG: RPC

> ROUTINE: MDRPCOWU RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> NAME: MD TMDWIDGET TAG: RPC

> ROUTINE: MDRPCOW RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE VERSION: 1

> NAME: MDK GET VISTA DATA TAG: RPC

> ROUTINE: MDKRPC1 RETURN VALUE TYPE: ARRAY

> AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

> INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 8 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the routine tag that will be called to retrieve the data. INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 50 REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is whatever data is needed by the subroutine to process the request for data. In many cases it will be a single value (e.g., patient id - DFN).

> RETURN PARAMETER DESCRIPTION:

> Returns an array.

> RESULT(0)=number or RESULT(0)=-1^error message RESULT(1)=data

> RESULT(n)=data

> If data is not found, RESULT(0) will be contain a "-1" in the first piece and an error message in the second piece.

> If data is found, RESULT(0) will contain a number that indicates how many entries are returned.

> RESULT(1) through RESULT(n) will contain the data that is found.

> NAME: MDK GET/SET RENAL DATA TAG: RPC

> ROUTINE: MDKRPC2 RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> NAME: MDK UTILITY TAG: RPC

> ROUTINE: MDKUTLR RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

> 1NAME: MDCLIO TAG: RPC

> ROUTINE: MDCLIO RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: PUBLIC WORD WRAP ON: TRUE DESCRIPTION:

> This is the primary RPC called by the CliO engine for normal command processing.

> NAME: MDCP CORRECTIONS BY IEN TAG: GETCORR

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: ARRAY

> AVAILABILITY: SUBSCRIPTION INACTIVE: ACTIVE WORD WRAP ON: TRUE

> DESCRIPTION:

> Gets a list of corrections for a given HL7 message.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> The IEN of the message in file 703.1 (the CP REPORT RESULTS file). RETURN PARAMETER DESCRIPTION:

> Returns a global array in the format:

> Correction Type IEN^Uncorrected Value^Corrected Value

> NAME: MDCP MESSAGE BY IEN TAG: GETMSG

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: SUBSCRIPTION WORD WRAP ON: TRUE VERSION: 1

> DESCRIPTION:

> This RPC returns an HL7 message based on its IEN.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL

> 1 Patch MD\*1.0\*16 January 2011 Added new remote procedure calls (RPCs).

> REQUIRED: YES SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the IEN of the message in file 772. RETURN PARAMETER DESCRIPTION:

> This returns the value of the message. Note that, at least for the initial version of this call, the MSH segment will NOT be returned as part of the results.

> NAME: MDCP RESULTS BY STATUS TAG: GTMSGIDS

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: SUBSCRIPTION INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This broker call will return a list of IENS from the CP RESULT REPORT file based on the STATUS passed in as a parameter.

> INPUT PARAMETER: MDCPSTAT PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 1 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the EXTERNAL representation of the status to be used to generate the list of IENs.

> RETURN PARAMETER DESCRIPTION:

> Returns an array of IENs.

> NAME: MDCP UPDATE MESSAGE REASON TAG: UPDRSN

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: GLOBAL ARRAY

> AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE DESCRIPTION:

> This RPC call will add word processing text to the CLIO_HL7_LOG file to explain the reason for the current status. It is primarily intended to be used to store error text from CliO.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 250 REQUIRED: YES

> SEQUENCE NUMBER: 1 DESCRIPTION:

> This is the IFN of the HL7 message in the CLIO_HL7_LOG file. INPUT PARAMETER: MDCPTEXT PARAMETER TYPE: LITERAL

> MAXIMUM DATA LENGTH: 250 REQUIRED: YES SEQUENCE NUMBER: 2

> DESCRIPTION:

> This is the text to add to the CLIO_HL7_LOG file. Note that this text will completely overwrite the text that was already in the reason field.

> NAME: MDCP UPDATE MESSAGE STATUS TAG: UPDATERP

> ROUTINE: MDCPHL7B RETURN VALUE TYPE: ARRAY

> AVAILABILITY: PUBLIC INACTIVE: ACTIVE

> WORD WRAP ON: TRUE VERSION: 1 DESCRIPTION:

> This call will update the status of an entry in file 704.002

> (the CLIO_HL7_LOG file). Note that if the status passed through is 'PROCESSED', the CP INSTRUMENT file entry pointed to by field .03 will be checked to see if it has a routine in its .11 field. If it does, the HL7 message will be copied to a temp global and the PROCESSING ROUTINE will be invoked.

> INPUT PARAMETER: MDCPMSG PARAMETER TYPE: LITERAL REQUIRED: YES SEQUENCE NUMBER: 1

> DESCRIPTION:

> The IFN of the message in the CP RESULT REPORT file.

> INPUT PARAMETER: MDCPSTAT PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 1 REQUIRED: YES

> SEQUENCE NUMBER: 2 DESCRIPTION:

> The status to which to change the file entry referenced by the first parameter. Check the data dictionary for field .09 to get a list of valid codes. This parameter must be in internal format.

> INPUT PARAMETER: MDCPDFN PARAMETER TYPE: LITERAL REQUIRED: NO SEQUENCE NUMBER: 3

> DESCRIPTION:

> This is the IFN of the patient in file 2, if available.

> INPUT PARAMETER: MDCPISCR PARAMETER TYPE: LITERAL REQUIRED: NO SEQUENCE NUMBER: 4

> DESCRIPTION:

> If MDCPDFN is set, this tells the linetag that MDCPDFN is a correction, not the original DFN.

> RETURN PARAMETER DESCRIPTION:

> Returns a local variable containing the results of the status update in DIALOG format.

### Trouble Shooting:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Is the machine plugged in? Is the machine on?

> Are all cables connected correctly?

> <span id="_TOC_250004" class="anchor"></span>Endoworks

> Vendor: Olympus Type: Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy

> Description:

> The bi-directional interface for this instrument is currently available.

> Requirements:

> This instrument requires an Advanced Gateway vendor interface.

> Setup Instructions:

> The Olympus Interface is a non-persistent interface and can share its TCP/IP port address with other non-persistent devices. To configure the Olympus (Endoworks) software, it is recommended that you consult Olympus. Olympus has the correct setting for the Endoworks software that is needed to interface with CP.

> 1 The site will need to set up an Olympus type in CPManager.exe for each type of procedure, (such as Olympus (Bronchoscopy), Olympus (Colonoscopy), etc.). Please refer to the Clinical Procedures web site for the device settings for each type of procedure.

> 1 Patch MD\*1.0\*6 May 2008 Added information about setting up a type for each procedure.

> 1Figure 6, Inbound HL Logical Link Settings

> Figure 6 displays the settings for the standard non-persistent inbound HL Logical Link.

> Figure 7, Outbound HL Logical Link Settings

> Error! Reference source not found.7 displays the settings for the standard non-persistent outbound HL Logical Link.

### Manuals:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No information available at this time.

> Costs:

> No information available at this time.

> Trouble Shooting:

1.  Is the machine plugged in?
2.  Is the machine on?
3.  Are all cables connected correctly?

> <span id="_TOC_250002" class="anchor"></span>Sensormedics V-MAX

> Vendor: Cardinal Health Type: PFT

### From: MD*1*12 Technical Manual (CP Flowsheets)

### [1](\l)CP_Transaction_TIU_History File - \#702.001

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This CP Transaction TIU History file stores all TIU notes that is associated with the CP Transaction study. This will keep track of multiple notes associated with one CP study.

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
<td>Study_ID</td>
<td>702.001,.01</td>
<td><p>Pointer To CP Transaction File</p>
<p>(#702)</p></td>
<td>This field contains a pointer to the CP Transaction file (#702).</td>
</tr>
<tr class="even">
<td>TIU_Note_ID</td>
<td>702.001,.02</td>
<td>Pointer To TIU Document File (#8925)</td>
<td><p>This field contains a pointer to the TIU Document file (#8925) representing the note that contains the interpretation of this CP Transaction. (Reference IA</p>
<p>#3376)</p></td>
</tr>
<tr class="odd">
<td>Date_Assigned</td>
<td>702.001,.03</td>
<td>Date</td>
<td><p>This field contains the date/time</p>
<p>when the TIU note was assigned to this transaction.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 702.001 added.

### [1](\l)Hemodialysis Access Points File - \#704.201

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on access points used by the Hemodialysis application.

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
<td>Patient_ID</td>
<td>704.201,.01</td>
<td><p>Pointer to patient</p>
<p>file (#2)</p></td>
<td><p>This field contains the patient</p>
<p>DFN. (Required)</p></td>
</tr>
<tr class="even">
<td>Access Points</td>
<td>704.201,.1</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s access points for dialysis</p>
<p>treatments.</p></td>
</tr>
<tr class="odd">
<td>Access History</td>
<td>704.201,.2</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s access history for dialysis</p>
<p>treatments.</p></td>
</tr>
<tr class="even">
<td>Infection History</td>
<td>704.201,.3</td>
<td>Word Processing</td>
<td><p>This field holds the XML in UUEncoded format for this patient’s infection history for</p>
<p>dialysis treatments.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.201 added.

### [1](\l)Hemodialysis Study File - \#704.202

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on hemodialysis studies used by the Hemodialysis application.

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
<td>ID</td>
<td>704.202,.01</td>
<td><p>Pointer to CP</p>
<p>Transaction file (#702)</p></td>
<td><p>This field contains the IEN of the</p>
<p>CP STUDY (File #702) for this dialysis treatment. (Required)</p></td>
</tr>
<tr class="even">
<td>Patient</td>
<td>704.202,.02</td>
<td>Pointer to Patient file (#2)</td>
<td><p>Pointer to the PATIENT (File #2) of the patient for this dialysis</p>
<p>treatment.</p></td>
</tr>
<tr class="odd">
<td>Study_DateTime</td>
<td>704.202,.03</td>
<td>Computed date</td>
<td><p>Computed field used to allow</p>
<p>automated XML creation with appropriate tag/value pairs.</p></td>
</tr>
<tr class="even">
<td>Study_Location</td>
<td>704.202,.04</td>
<td>Computed</td>
<td><p>Computed field used to allow automated XML creation with</p>
<p>appropriate tag/value pairs.</p></td>
</tr>
<tr class="odd">
<td><a href="#_bookmark50"><strong>2</strong></a>User</td>
<td>704.202,.05</td>
<td><p>0;3 Pointer to NEW PERSON FILE</p>
<p>(#200)</p></td>
<td>This field contains the user who accessed the Hemodialysis study.</td>
</tr>
<tr class="even">
<td>Date/Time Accessed</td>
<td>704.202,.06</td>
<td>0;4 Date</td>
<td><p>This field displays the date/time when the hemodialysis study was</p>
<p>accessed by the user.</p></td>
</tr>
<tr class="odd">
<td>Workstation</td>
<td>704.202,.07</td>
<td>0;5 Free text</td>
<td><p>This field contains the workstation that was used by the user to</p>
<p>access the hemodialysis study.</p></td>
</tr>
<tr class="even">
<td>Status</td>
<td>704.202,.09</td>
<td><p>Set:</p>
<ol type="1">
<li><p>- Closed</p></li>
<li><p>- Active</p></li>
</ol></td>
<td>Contains the status of this procedure.</td>
</tr>
<tr class="odd">
<td>Study Data</td>
<td>704.202,.1</td>
<td>Word Processing</td>
<td><p>Contains the study data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Summary</td>
<td>704.202,.2</td>
<td>Word Processing</td>
<td><p>Contains the summary data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="odd">
<td>Flowsheet</td>
<td>704.202,.3</td>
<td>Word Processing</td>
<td><p>Contains the flowsheet data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Med Log</td>
<td>704.202,.4</td>
<td>Word Processing</td>
<td><p>Contains the med log data XML</p>
<p>document in UUEncoded format.</p></td>
</tr>
<tr class="odd">
<td>Note List</td>
<td>704.202,.5</td>
<td>Word Processing</td>
<td><p>This field contains the Note List data XML document in</p>
<p>UUEncoded format.</p></td>
</tr>
<tr class="even">
<td>Event Log</td>
<td>704.202,.6</td>
<td>Word Processing</td>
<td><p>This field contains the Event Log data XML document in</p>
<p>UUEncoded format.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.202 added.

> <span id="_bookmark50" class="anchor"></span>2 Patch MD\*1.0\*16 January 2011 Fields added.

### [1](\l)Hemodialysis Setting File - \#704.209

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new file contains information on hemodialysis settings used by the Hemodialysis application.

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
<td>Setting Name</td>
<td>704.209,.01</td>
<td><p>Free Text 3-30 characters in length.</p>
<p>Not numeric or starting with</p>
<p>punctuation.</p></td>
<td>Contains the descriptive name of the data contained in this setting.</td>
</tr>
<tr class="even">
<td>Owner</td>
<td>704.209,.02</td>
<td><p>Pointer to new</p>
<p>person file (#200)</p></td>
<td><p>If this setting is user specific, this</p>
<p>field will contain that user’s DUZ.</p></td>
</tr>
<tr class="odd">
<td>User</td>
<td>704.209,.03</td>
<td>Pointer to new person file (#200)</td>
<td><p>This field displays the user name that is locking the Hemodialysis</p>
<p>setting option.</p></td>
</tr>
<tr class="even">
<td>Date/Time of Lock</td>
<td>704.209,.04</td>
<td><p>Input transform: S %DT="ET" D</p>
<p>^%DT S X=Y</p>
<p>K:Y&lt;1 X</p></td>
<td>This field will store the date and time of when the Hemodialysis setting option was locked for use.</td>
</tr>
<tr class="odd">
<td>Process ID</td>
<td>704.209,.05</td>
<td><p>Free text 3-40 characters in length. Input transform: K:$L(X)&gt;40!($L(X</p>
<p>)&lt;3) X</p></td>
<td>This field will store the JOB ID of the process that is locking the Hemodialysis setting option.</td>
</tr>
<tr class="even">
<td>XML Document</td>
<td>704.209,.1</td>
<td>Word Processing</td>
<td><p>Contains the XML document for</p>
<p>this setting in UUEncoded format.</p></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*6 May 2008 File 704.209 added.

### [1](\l)CP_CONSOLE_ACL File (704.001)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains the Access Control List (ACL) for items in the console by that item's ID.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ITEM_ID</td>
<td>704.001,.01</td>
<td>Free text (38 char)</td>
<td>This ITEM_ID represents the Global Unique Identifier (GUID) of a console item and Clinical Observation (CliO) record. An appropriate GUID is alphanumeric and 38 characters in length.</td>
</tr>
<tr class="even">
<td>USER_ID</td>
<td>704.001,.02</td>
<td>Pointer to NEW PERSON file (#200)</td>
<td>This is the end-user given access permission to the item (ITEM_ID).</td>
</tr>
<tr class="odd">
<td>ACCESS_LEVEL</td>
<td>704.001,.03</td>
<td><p>SET (Required)</p>
<blockquote>
<p>0 FOR Read Only 1 FOR Read+Write</p>
<p>2 FOR</p>
</blockquote>
<p>Read+Write+Delete 3 FOR Full Control</p></td>
<td>This is the level of edit access to the item (ITEM_ID) the end-user (USER_ID) has been permitted. In addition, "Full Control" will grant the user full edit privileges as well as the ability to grant access of this item to another user. This access permission is granted via the Access Control List Manager, a function within the CP Console application.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### [1](\l)CP_HL7_LOG File (#704.002)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains a log of HL7 Messages processed by Clinical Flowsheets.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 46%" />
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
<td>MESSAGE_ID</td>
<td>704.002,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field identifies the Clinical Flowsheets HL7 message. This MESSAGE_ID is generated by the Clinical Flowsheets system.</td>
</tr>
<tr class="even">
<td>STATUS</td>
<td>704.002,.02</td>
<td><p>'1' FOR ENTERED; 2' FOR AWAITING</p>
<p>PROCESSING; 3' FOR ERROR;</p>
<p>4' FOR PROCESSED;</p></td>
<td>This field indicates the status of this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)). This status is maintained by Clinical Flowsheets and HL7 message processing.</td>
</tr>
<tr class="odd">
<td>MAPPING_TAB LE</td>
<td>704.002,.03</td>
<td><p>FREE TEXT (1-</p>
<p>50 CHAR)</p></td>
<td><p>This field contains a copy of the ID field (#.01) in the TERM_MAPPING_TABLE file (#704.108). It</p>
<p>is used to determine which mapping table to use when translating the HL7 message (MESSAGE_ID field (#.01)) into observations.</p></td>
</tr>
<tr class="even">
<td><p>HL7_MESSAGE</p>
<p>_ADMINISTRAT ION</p></td>
<td>704.002,.04</td>
<td>POINTER TO HL7 MESSAGE ADMINISTRAT ION FILE (#773)</td>
<td>This field identifies this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) with an entry in the HL7 Message Administration File (#773).</td>
</tr>
<tr class="odd">
<td><p>HL7_MESSAGE</p>
<p>_TEXT</p></td>
<td>704.002,.05</td>
<td>POINTER TO HL7 MESSAGE TEXT FILE (#772)</td>
<td>This field identifies this Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) text with an entry in the HL7 MESSAGE TEXT File (#772).</td>
</tr>
<tr class="even">
<td>PATIENT</td>
<td>704.002,.06</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This is the patient supported by the Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
<tr class="odd">
<td>STUDY_REFER ENCE_NBR</td>
<td>704.002,.07</td>
<td>POINTER TO CP TRANSACTION FILE (#702)</td>
<td>This field identifies the Clinical Flowsheets HL7 message (MESSAGE_ID field (#.01)) with a CP TRANSACTION File (#702) entry.</td>
</tr>
<tr class="even">
<td>MESSAGE_DAT E_TIME</td>
<td>704.002,.08</td>
<td>DATE</td>
<td>This is the date/time the HL7 message (MESSAGE_ID field (#.01)) was created as reported by the HL7 system.</td>
</tr>
<tr class="odd">
<td>PROCESSED_TI MESTAMP</td>
<td>704.002,.09</td>
<td>DATE</td>
<td>This is the date/time the HL7 message (MESSAGE_ID field (#.01)) was processed as reported by the HL7 system.</td>
</tr>
<tr class="even">
<td>REPORTED_LO CATION</td>
<td>704.002,.11</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data as extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be location identifying data that can be used to locate the source of the HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 46%" />
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
<td>REPORTED_PA TIENT</td>
<td>704.002,.21</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be patient identifying data used to determine which patient the HL7 message (MESSAGE_ID field (#.01)) supports.</td>
</tr>
<tr class="even">
<td>REPORTED_INS TRUMENT</td>
<td>704.002,.31</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is raw-data extracted from the HL7 message (MESSAGE_ID field (#.01)). This should be instrument identifying data used to determine the source-device of the HL7 message (MESSAGE_ID field (#.01)).</td>
</tr>
</tbody>
</table>

> [1](\l)CP_HL7_LOG_REASON (#704.004)

> This file monitors Clinical Flowsheets HL7 message processing anomalies. These Clinical Flowsheets HL7 messages are referenced via the CP_HL7_LOG file (#704.002).

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 43%" />
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
<td>CLIO_HL7_LOG</td>
<td>704.004,.01</td>
<td>POINTER TO CP_HL7_LOG FILE (#704.002)</td>
<td>This field identifies this entry with an entry in the CP_HL7_LOG file (#704.002).</td>
</tr>
<tr class="even">
<td>DATE_TIME_EN TERED</td>
<td>704.004,.02</td>
<td>DATE</td>
<td>This is the date/time the file entry was created.</td>
</tr>
<tr class="odd">
<td>REASON</td>
<td>704.004,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is the reason this file entry was created.</td>
</tr>
</tbody>
</table>

> [1](\l)CP_MOVEMENT_AUDIT File (#704.005)

> This file will hold a subset of patient movement data. This must be done rather than using a direct reference to the PATIENT MOVEMENT file (#405) because, in the instance of cancellations, the internal entry number (IEN) of a patient movement disappears before there is the chance to work with it. This file will coalesce all of a movement's data to send to 3rd party users. That data is sent to 3rd party users via Health Level Seven (HL7) messaging. To ensure that message is available to 3<sup>rd</sup> party users, the ACCEPTED BY [<sup>2</sup>](#_bookmark61)QUEUE field (#.09) is set to '1' to confirm the message is in the HL7 outbound queue; that CP MOVEMENT AUDIT file (#704.005) entry will then need to be purged.

| Field Name       | Field Number | Format                                      | Description                                                                                                            |
|----------------------|------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| PATIENT              | 704.005,.01      | POINTER TO PATIENT FILE (#2)                    | This field is the identifier of the patient involved in the patient movement event.                                        |
| DATE_TIME_OF\_ EVENT | 704.005,.02      | DATE                                            | This field stores the date/time of the patient movement event.                                                             |
| DIVISION             | 704.005,.03      | POINTER TO MEDICAL CENTER DIVISION FILE (#40.8) | This field identifies the DIVISION per the patient movement event.                                                         |
| WARD                 | 704.005,.04      | POINTER TO WARD LOCATION FILE (#42)             | This field identifies the WARD per the patient movement event.                                                             |
| BED                  | 704.005,.05      | POINTER TO ROOM-BED FILE (#405.4)               | This field identifies the room-BED per the patient movement event.                                                         |
| MESSAGE_TYPE         | 704.005,.06      | FREE TEXT (3 CHAR)                              | This indicates the HL7 MESSAGE TYPE. The value here can be 'ADT' to indicate an admission/discharge/transfer type message. |
| EVENT_TYPE           | 704.005,.07      | FREE TEXT (3 CHAR)                              | This indicates the HL7 message EVENT TYPE. The value here can be 'A01' to indicate an Admit/visit notification EVENT TYPE. |

> 1 Patch MD\*1.0\*16 January 2011 File description added.

> <span id="_bookmark61" class="anchor"></span>2 Patch MD\*1.0\*12 October 2011 Removed reference to VDEF. Revised 704.005, 09 and 704.005, 1 field names.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 43%" />
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
<td>PIMS_EVENT_ID</td>
<td>704.005,.08</td>
<td>FREE TEXT (1-20 CHAR)</td>
<td><p>This is a copy of the internal entry number (IEN) of the PATIENT MOVEMENT file (#405) entry which correlates to this CP_MOVEMENT_AUDIT file (#704.005)</p>
<p>entry.</p>
<p>If a movement is deleted, the corresponding entry from the patient movement file is deleted as well. This prevents this field from being an actual pointer. This IEN is used only for troubleshooting purposes.</p></td>
</tr>
<tr class="even">
<td>ACCEPTED_BY_ QUEUE</td>
<td>704.005,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This indicates whether the HL7 message has been queued.</td>
</tr>
<tr class="odd">
<td>QUEUE_ERROR_ MSG</td>
<td>704.005,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This field stores the error message, if an error message is returned by the message queue process.</td>
</tr>
</tbody>
</table>

### [1](\l)CP_PROTOCOL_LOCATION File (#704.006)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file will be used by the Clinical Flowsheets application to determine the target for an outbound admission, discharge, and transfer (ADT) message. Messages are sent to a target via Health Level 7 messaging (HL7).

> A target is defined here as a receiving CIS or other COTS product that has expressed a desire to be notified when a patient admission, transfer or discharge has occurred for a specific hospital location.

| Field Name | Field Number | Format                                      | Description                                                                                                                                                                      |
|----------------|------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSCRIBER     | 704.006,.01      | POINTER TO PROTOCOL FILE (#101)                 | This field identifies the subscriber protocol to be used to send the message.                                                                                                        |
| DIVISION       | 704.006,.02      | POINTER TO MEDICAL CENTER DIVISION FIL E (#40.8 | This field identifies the target MEDICAL CENTER DIVISION for the message.                                                                                                            |
| WARD           | 704.006,.03      | POINTER TO WARD LOCATION FILE (#42)             | This field identifies the target WARD location for the message.                                                                                                                      |
| MESSAGE_TYPE   | 704.006,.04      | FREE TEXT (3 CHAR)                              | This field is the type of message to be sent. A sample MESSAGE TYPE could be "ADT".                                                                                                  |
| EVENT_TYPE     | 704.006,.05      | FREE TEXT (3 CHAR)                              | This is the message's EVENT TYPE. A sample EVENT TYPE could be "A01".                                                                                                                |
| ID             | 704.006,.06      | FREE TEXT (32 CHAR)                             | This field will be the alpha-numeric portion of the message's Global Unique Identifier (GUID), if the message is generated. A sample ID could be "C42AC54282B642F4950E179A3D43AA85". |
| NAME           | 704.006,.07      | FREE TEXT (1-30 CHAR)                           | This field is the assigned name for the message. A sample NAME could be "ADMIT2DEVICEX".                                                                                             |

> [1](\l)CP_SHIFT File (#704.007)

> This file is used to store the site configurable shift definitions.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.007,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field contains the work-shift identifier. A sample ID could be "{1A5A417B-3F04-23ED- B044-4102B19D66E4}"</td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.007,.02</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>HELP-PROMPT: Answer must be 1-30 characters in length. This is the NAME of the work-shift. A sample could be "DAY”.</td>
</tr>
<tr class="odd">
<td>START_TIME</td>
<td>704.007,.03</td>
<td>FREE TEXT (4 CHAR)</td>
<td>This is the START TIME of the work-shift. An example is "0800" representing the time 8:00 AM.</td>
</tr>
<tr class="even">
<td>STOP_TIME</td>
<td>704.007,.04</td>
<td>FREE TEXT (4 CHAR)</td>
<td>This is the STOP TIME of the work-shift. An example is "1830" representing the time 6:30 PM.</td>
</tr>
<tr class="odd">
<td>MULTI_DAY</td>
<td>704.007,.05</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field indicates whether a work-shift extends over multiple days or not.</td>
</tr>
<tr class="even">
<td>DISPLAY_NAME</td>
<td>704.007,.06</td>
<td>FREE TEXT (1-50 CHAR)</td>
<td>HELP-PROMPT: Answer must be 1-50 characters in length. This field is the text displayed within Clinical Flowsheets for the work-shift. A sample DISPLAY NAME could be "Nights (Midnight - 8:00a)".</td>
</tr>
<tr class="odd">
<td>ACTIVE</td>
<td>704.007,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field determines whether the work-shift entry is active or not.</td>
</tr>
<tr class="even">
<td>COMMENT</td>
<td>704.007,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is a comment about the work-shift.</td>
</tr>
</tbody>
</table>

> [1](\l)CP_SCHEDULE File (#704.008)

> This file is used to store the site configurable schedules for the Kardex.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.008,.01</td>
<td>FREE TEXT (38 CHAR)</td>
<td>This field contains the schedule identifier. A sample ID could be "{E24290F6-31F4-C6F6- B310-E37C563FBD64}”.</td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.008,.02</td>
<td>FREE TEXT (1-30 CHAR)</td>
<td>This is the NAME of the schedule. A sample could be "TID/MEALS”.</td>
</tr>
<tr class="odd">
<td>SCHEDULE_TYPE</td>
<td>704.008,.03</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; 1' FOR PRN;</p>
<p>2' FOR One-Time;</p>
<p>3' FOR Stat;</p></td>
<td>This is the type of schedule indicator.</td>
</tr>
<tr class="even">
<td>INTERVAL</td>
<td>704.008,.04</td>
<td><p>NUMBER (0-</p>
<p>525600)</p></td>
<td>This field is the schedule INTERVAL in minutes. An example is "120" to present a schedule INTERVAL of 2 hours.</td>
</tr>
<tr class="odd">
<td>DISPLAY_NAME</td>
<td>704.008,.05</td>
<td>FREE TEXT (1-50 CHAR)</td>
<td>This field is the text displayed within Clinical Flowsheets for the schedule. A sample DISPLAY NAME could be "3 times daily with meals”.</td>
</tr>
<tr class="even">
<td>ACTIVE</td>
<td>704.008,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>1' FOR YES;</p></td>
<td>This field determines whether the schedule entry is active or not.</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.008,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is a COMMENT about the schedule.</td>
</tr>
<tr class="even">
<td>CUSTOM_SCHED ULE</td>
<td>704.008,.2</td>
<td><p>FREE TEXT (4-</p>
<p>250 CHAR)</p></td>
<td>This field contains actual times a scheduled event is to occur. This data is to be utilized when the schedule intervals are not equal. A sample CUSTOM SCHEDULE could be "0600,1100,1700" for schedule events to occur at 6 AM, 11 AM, and 5 PM.</td>
</tr>
</tbody>
</table>

> [1](\l)TERM File (#704.101)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file stores all terminology elements for the Clinical Flowsheets application. The entries in this file are called "terms". These terms along with CP files \#704.102 -#704.109 constitute the Clinical Data Model.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.101,.01</td>
<td><p>FREE TEXT</p>
<p>(Required) (38 CHAR)</p></td>
<td>This field is the unique identifier for this entry or term. This data is maintained nationally and will be the identifier for this term enterprise-wide. A sample ID could be "{D9FF5CA8-09AF-4318-B784- DEB3A8F819D8}".</td>
</tr>
<tr class="even">
<td>TERM</td>
<td>704.101,.02</td>
<td>FREE TEXT (1-7 CHAR)</td>
<td>This field is the name of this TERM entry, in accordance with enterprise-wide terminology standards. A sample TERM could be "PICC LINE".</td>
</tr>
<tr class="odd">
<td>ABBREVIATION</td>
<td>704.101,.03</td>
<td>FREE TEXT (1-10 CHAR)</td>
<td>This is the enterprise wide ABBREVIATION for this term. This value will be used throughout the Clinical Flowsheets system in dropdowns and list boxes where screen real estate is tight. A sample ABBREVIATION could be "PICC LINE".</td>
</tr>
<tr class="even">
<td>DISPLAY_NAME</td>
<td>704.101,.04</td>
<td>FREE TEXT (1-75 CHAR)</td>
<td>This field is a case sensitive, user friendly, DISPLAY NAME for this term. This is the full name for this term for display in the Clinical Flowsheets application. A sample DISPLAY NAME could be "PICC Line".</td>
</tr>
<tr class="odd">
<td>TERM_TYPE</td>
<td>704.101,.05</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td><p>This field correlates this term with an entry in the TERM TYPE File (#704.102). This field should define the "purpose" of this term in the Clinical Data Model.</p>
<p>CROSS-REFERENCE: 704.101^ATYPE 1)= S</p>
<p>^MDC(704.101,"ATYPE",$E(X,1,30),DA)="" 2)= K</p>
<p>^MDC(704.101,"ATYPE",$E(X,1,30),DA)</p></td>
</tr>
<tr class="even">
<td>DATA_TYPE</td>
<td>704.101,.06</td>
<td><p>SET</p>
<p>'0' FOR Qualifier;</p>
<p>1' FOR Complex;</p>
<p>2' FOR Numeric;</p>
<p>3' FOR PickList;</p>
<p>4' FOR Boolean;</p>
<p>5' FOR String;</p>
<p>6' FOR Range;</p></td>
<td>This field is to specify the type of data this term represents.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>VALUE_TYPE</td>
<td>704.101,.07</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Unspecified; 1' FOR</p>
<p>Temperature; 2' FOR Length;</p>
<p>3' FOR Volume;</p>
<p>4' FOR Rate;</p>
<p>5' FOR Time;</p>
<p>6' FOR Mass;</p>
<p>7' FOR Scale;</p></td>
<td>This field is to specify the VALUE TYPE this term represents. This data will be used for more reliable conversion utilities.</td>
</tr>
<tr class="even">
<td>ACTIVE</td>
<td>704.101,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>1' FOR Yes;</p></td>
<td>This field is to indicate whether a term is ACTIVE or not. Only an ACTIVE term can be used in new clinical observations.</td>
</tr>
<tr class="odd">
<td>DESCRIPTION</td>
<td>704.101,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This field is a full DESCRIPTION of this term. A sample DESCRIPTION could be: "Peripherally Inserted Central Catheter Line".</td>
</tr>
<tr class="even">
<td>HELP_TEXT</td>
<td>704.101,.2</td>
<td><p>FREE TEXT (1-</p>
<p>250 CHAR)</p></td>
<td>This is the text that will display as help for the term, within the Clinical Flowsheets application. A sample HELP TEXT could be: "Peripherally Ins Cen Cath Line".</td>
</tr>
<tr class="odd">
<td>BOOLEAN_VALU E_TRUE</td>
<td>704.101,.31</td>
<td><p>FREE TEXT (1-</p>
<p>100 CHAR)</p></td>
<td>This field is the text that will display for Boolean DATA TYPE (field #.06) observations that are "true". A sample BOOLEAN VALUE TRUE could be "TRUE".</td>
</tr>
<tr class="even">
<td>BOOLEAN_VALU E_FALSE</td>
<td>704.101,.32</td>
<td><p>.3;2 FREE TEXT</p>
<p>(1-100 CHAR)</p></td>
<td>This field is the text that will display for Boolean DATA TYPE (field #.06) observations that are "false". A sample BOOLEAN VALUE FALSE could be "FALSE".</td>
</tr>
<tr class="odd">
<td>MULTI_SELECT_ PICKLIST</td>
<td>704.101,.33</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>1' FOR Yes;</p></td>
<td>This field determines if more than one value may be selected from a "picklist" for an observation.</td>
</tr>
<tr class="even">
<td>SCHEDULE</td>
<td>704.101,.34</td>
<td>NUMBER</td>
<td>This field is the minutes of interval per SCHEDULE. A sample SCHEDULE could be "120".</td>
</tr>
<tr class="odd">
<td>SCHEDULE_TYPE</td>
<td>704.101,.35</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; 1' FOR PRN;</p>
<p>2' FOR Stat;</p>
<p>3' FOR One-Time;</p></td>
<td>This field is the type of schedule.</td>
</tr>
<tr class="even">
<td>VUID</td>
<td>704.101,99.99</td>
<td>FREE TEXT (1-20 CHAR)</td>
<td>This field is the VHA Unique IDentifier (VUID) for this term.</td>
</tr>
<tr class="odd">
<td>ID</td>
<td>704.102,.001</td>
<td>NUMBER</td>
<td>This is the ordinal position of this term-type entry.</td>
</tr>
</tbody>
</table>

> [1](\l)TERM_TYPE File (#704.102)

> This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

| Field Name | Field Number | Format            | Description                                                                                                                          |
|----------------|------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE           | 704.102,.01      | FREE TEXT (1-30 CHAR) | This is the name for this term TYPE. A sample TYPE could be "OBSERVATION".                                                               |
| XML_TAG        | 704.102,.02      | FREE TEXT (1-30 CHAR) | This is the XML TAG this data element is to be stored on when an appropriate XML document is built. A sample XML TAG could be "TERM_ID". |
| VUID           | 704.102,.03      | FREE TEXT (1-20 CHAR) | This field is the VHA Unique IDentifier (VUID) for this term type. A sample VUID could be "4688703".                                     |

> [1](\l)TERM_QUALIFIER_PAIR File (#704.103)

> This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the Clio data store if this file is changed.

> This file is a join table for the Clinical Data Model that matches observations to their allowable qualifiers. A sample could be the observation equating to "weight" and the paired qualifier equating to "lift scale".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>TERM_ID</td>
<td>704.103,.01</td>
<td><p>POINTER TO TERM FILE (#704.101)</p>
<p>(Required) (Key field)</p></td>
<td>This field identifies the primary TERM file (#704.101) entry in the Clinical Data Model for this pairing.</td>
</tr>
<tr class="even">
<td>QUALIFIER_ORD ER</td>
<td>704.103,.02</td>
<td><p>NUMBER</p>
<p>(Between 0-9999)</p></td>
<td>This represents the order that this qualifier will be displayed with the term as well as the order of interpretation for complex terms.</td>
</tr>
<tr class="odd">
<td>QUALIFIER_ID</td>
<td>704.103,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the qualifier term or subcomponent for this pair.</td>
</tr>
<tr class="even">
<td>RANKING</td>
<td>704.103,.04</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This value will be used in calculations for this pairing as well as future graphing capabilities for pick-list values.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### [1](\l)TERM_UNIT_CONVERSION File (#704.104)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file links like units of measure together with required conversion logic to change the value from one unit to another.

> NOTE: Units are presented as entries in the TERM file (#704.101). For example the unit "CENTIMETER" could be identified by the TERM file (#704.101), TERM ID (field \#.01)"{EF700458-8C2D-16E8-02DC-9E1711584C53}".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>UNIT_ID_PRE</td>
<td>704.104,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field is the identifier of the unit that a value will be converted from.</td>
</tr>
<tr class="even">
<td>UNIT_ID_POST</td>
<td>704.104,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field is the identifier of the unit that a value will be converted to.</td>
</tr>
<tr class="odd">
<td>CONVERSION_OF FSET_PRE</td>
<td>704.104,.03</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 6</p>
<p>decimal digits)</p></td>
<td>This field will be used to offset a value prior to executing the conversion logic. A sample CONVERSION OFFSET PRE could be "0".</td>
</tr>
<tr class="even">
<td>CONVERSION_OF FSET_POST</td>
<td>704.104,.04</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 6</p>
<p>decimal digits)</p></td>
<td>This is used to offset a value post execution of the conversion logic. A sample CONVERSION OFFSET POST could be "32".</td>
</tr>
<tr class="odd">
<td>CONVERSION_FA CTOR</td>
<td>704.104,.05</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This value is used by the conversion logic as a multiplier of the original value. A sample CONVERSION FACTOR could be "1.8".</td>
</tr>
<tr class="even">
<td>DECIMAL_PRECI SION</td>
<td>704.104,.06</td>
<td><p>NUMBER</p>
<p>(Between - 999999999 and</p>
<p>999999999, 0</p>
<p>decimal digits)</p></td>
<td>This field is the decimal precision for rounding the resulting conversion value. A sample DECIMAL PRECISION could be "2".</td>
</tr>
<tr class="odd">
<td>DESCRIPTION</td>
<td>704.104,.09</td>
<td><p>FREE TEXT (1-</p>
<p>150 CHAR)</p></td>
<td>This is a DESCRIPTION of the conversion logic. A sample DESCRIPTION could be "DEGREES C -&gt; DEGREES F".</td>
</tr>
</tbody>
</table>

> [1](\l)TERM_UNIT_PAIR File (#704.105)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed. This file matches observation(s) with available units for the observation, and the range settings for each pair.

> Observations are presented as entries in the TERM file (#704.101). For example the observation "TRACTION WEIGHT" could be identified by the TERM file (#704.101), TERM ID (field#.01) "{0C913807-C678-4E94-BD20-B8B2EBE697BE}".

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>TERM_ID</td>
<td>704.105,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the Observation in this "observation/unit" pair.</td>
</tr>
<tr class="even">
<td>UNIT_ID</td>
<td>704.105,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the Unit in this "observation/unit" pair.</td>
</tr>
<tr class="odd">
<td>MIN_VALUE</td>
<td>704.105,.03</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 7</p>
<p>decimal digits)</p></td>
<td>This field contains the minimum value that can be entered for this observation/unit pair. A sample could be "-1".</td>
</tr>
<tr class="even">
<td>MAX_VALUE</td>
<td>704.105,.04</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 7</p>
<p>decimal digits)</p></td>
<td>This field contains the maximum value that can be entered for this observation/unit pair. A sample could be "31".</td>
</tr>
<tr class="odd">
<td>DEC_PRECISION</td>
<td>704.105,.05</td>
<td><p>NUMBER (0-7) INPUT TRANSFORM: K:+X'=X!(X&gt;7)!(X</p>
<p>&lt;0)!(X?.E1"."1.N) X</p>
<p>LAST EDITED: APR 02, 2009 HELP-PROMPT:</p>
<p>Type a number between 0 and 7, 0 Decimal Digits</p></td>
<td>This is the maximum decimal precision that can be entered for this observation/unit pair. A sample could be "0".</td>
</tr>
<tr class="even">
<td>REFERENCE_LO W</td>
<td>704.105,.06</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This is the value for this observation/unit pair that will cause Clinical Flowsheets to interpret the observed value as "low". A sample REFERENCE LOW could be "0".</td>
</tr>
<tr class="odd">
<td>REFERENCE_HIG H</td>
<td>704.105,.07</td>
<td><p>NUMBER Between</p>
<p>-999999999 and</p>
<p>999999999, 9</p>
<p>decimal digits)</p></td>
<td>This is the value for this observation/unit pair that will cause Clinical Flowsheets to interpret the observed value as "high". A sample REFERENCE HIGH could be "30".</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 Added file description.

### [1](\l)TERM_CHILD_PAIR File (#704.106)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file holds the structure for complex observations by pairing the parent observation to the child observation with an ordinal position as well. Observations are entries in the TERM file (#704.101).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>TERM_ID</td>
<td>704.106,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the primary observation/term for complex term pairs. A sample TERM_ID could identify "blood pressure" as a primary term.</td>
</tr>
<tr class="even">
<td>CHILD_ORDER</td>
<td>704.106,.02</td>
<td>NUMBER (between 1 and 999)</td>
<td>This represents the order of the child pair in association with a complex term.</td>
</tr>
<tr class="odd">
<td>CHILD_ID</td>
<td>704.106,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the child term for a complex term pair. A sample CHILD_ID could identify "systolic" as a child term of "blood pressure".</td>
</tr>
<tr class="even">
<td>CHILD_UNIT_ID</td>
<td>704.106,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This is the unit(s) to present this child term. A sample CHILD_UNIT_ID could identify "MILLIMETERS OF MERCURY".</td>
</tr>
<tr class="odd">
<td>VALUE_TYPE</td>
<td>704.106,.05</td>
<td><p>SET</p>
<p>'0' FOR Extract;</p>
<p>1' FOR Delimited;</p></td>
<td>This field will indicate whether the observation values are delimited or not.</td>
</tr>
<tr class="even">
<td>VALUE_DELIMIT ER</td>
<td>704.106,.06</td>
<td>NUMBER (ASCII 32-126)</td>
<td>This is the number between 32 and 126 (0 Decimal Digits) of the ASCII value for the character to be used as the delimiter per delimited values. A sample VALUE_DELIMITER could be "47" to signify the use of the character "/" as delimiter.</td>
</tr>
<tr class="odd">
<td>VALUE_START_P OSITION</td>
<td>704.106,.07</td>
<td><p>NUMBER</p>
<p>(Between 1 and</p>
<p>250)</p></td>
<td>The "child values" may be presented in a string of data. This field is either the position or the delimited piece, of the data to begin extracting child values.</td>
</tr>
<tr class="even">
<td>VALUE_STOP_PO SITION</td>
<td>704.106,.08</td>
<td><p>NUMBER</p>
<p>(Between 1 and</p>
<p>250)</p></td>
<td>The "child values" may be presented in a string of data. This field is either the last position or the last delimited piece of the data. This is where extracting of child values is to stop.</td>
</tr>
<tr class="odd">
<td>DESCRIPTION</td>
<td>704.106,.09</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a DESCRIPTION of this observation/child term pair. A sample DESCRIPTION could be "Systolic pressure".</td>
</tr>
</tbody>
</table>

> [1](\l)TERM_RANGE_CHECK File (#704.107)

> This file maintains value ranges for related observations/terms.

> An example could be a TERM RANGE CHECK entry that would result in an observed TEMPERATURE of 80 DEGREES FAHRENHEIT for a MALE between 55-150 years of AGE, triggering a "CRITICAL LOW" response by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>TERM_ID</td>
<td>704.107,.01</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the term to which a term range check is applicable. A sample TERM ID could identify the term "TEMPERATURE".</td>
</tr>
<tr class="even">
<td>UNIT_ID</td>
<td>704.107,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the unit of measurement related to the TERM_ID (field #.01). A sample UNIT ID could identify "DEGREES F".</td>
</tr>
<tr class="odd">
<td>SEX</td>
<td>704.107,.03</td>
<td><p>SET</p>
<p>M' FOR Male; F' FOR Female; N' FOR Non-</p>
<p>Specific;</p></td>
<td>This field indicates the gender to which a term range check is applicable. A sample SEX could be "Male".</td>
</tr>
<tr class="even">
<td>AGE_MINIMUM</td>
<td>704.107,.04</td>
<td><p>NUMBER</p>
<p>(Between 0 and</p>
<p>150)</p></td>
<td>This is the minimum age which the term range check is applicable. A sample AGE MINIMUM could be "55".</td>
</tr>
<tr class="odd">
<td>AGE_MAXIMUM</td>
<td>704.107,.05</td>
<td><p>NUMBER</p>
<p>(Between 0 and</p>
<p>150)</p></td>
<td>This is the maximum age which the term range check is applicable. A sample AGE MAXIMUM could be "150".</td>
</tr>
<tr class="even">
<td>PATIENT_ID</td>
<td>704.107,.08</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This field identifies a patient for which the term range check is applicable. A sample PATIENT ID could identify "CP FLOWSHEETS,PATIENT1".</td>
</tr>
<tr class="odd">
<td>DESCRIPTION</td>
<td>704.107,.09</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is a DESCRIPTION of the term range check entry. A sample DESCRIPTION could be "Senior male temperature".</td>
</tr>
<tr class="even">
<td>CRITICAL_LOW</td>
<td>704.107,.11</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "CRITICAL LOW" result when the term range check is applied. A sample CRITICAL LOW could be "80".</td>
</tr>
<tr class="odd">
<td>ABNORMAL_LO W</td>
<td>704.107,.12</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause an "ABNORMAL LOW" result when the term range check is applied. A sample ABNORMAL LOW could be "85".</td>
</tr>
<tr class="even">
<td>NORMAL_LOW</td>
<td>704.107,.13</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "NORMAL LOW" result when the term range check is applied. A sample NORMAL LOW could be "90".</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>NORMAL_HIGH</td>
<td>704.107,.14</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause a "NORMAL HIGH" result when the term range check is applied. A sample NORMAL HIGH could be "100".</td>
</tr>
<tr class="even">
<td>ABNORMAL_HIG H</td>
<td>704.107,.15</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This value will cause an "ABNORMAL HIGH" result when the term range check is applied. A sample ABNORMAL HIGH could be "103".</td>
</tr>
<tr class="odd">
<td>CRITICAL_HIGH</td>
<td>704.107,.16</td>
<td><p>NUMBER</p>
<p>(Between -9999999</p>
<p>and 9999999, 7</p>
<p>decimal digits)</p></td>
<td>This is the value that will cause a CRITICAL HIGH"" result when the term range check is applied. A sample CRITICAL HIGH could be "106".</td>
</tr>
</tbody>
</table>

> [1](\l)TERM_MAPPING_TABLE File (# 704.108)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file is the anchor for the mapping table structure for the CP Gateway. Each mapping table is called up by elements in the HL7 message. The entries are used to translate the HL7 data into appropriate CP terminology.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.108,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This field is the Global Unique IDentifier (GUID) that identifies the mapping table. A sample ID could be "{4E41823C-CB5B-499F- BAAC-13626A6CD0D2}".</td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.108,.02</td>
<td><p>FREE TEXT</p>
<p>(Between 1-50 char)</p></td>
<td>This field is the NAME of the mapping table. A sample could be "DeviceX ServiceZ".</td>
</tr>
<tr class="odd">
<td>HL7_SENDING_A PPLICATION</td>
<td>704.108,.03</td>
<td><p>FREE TEXT (1 to</p>
<p>50 char)</p></td>
<td>This field is the application sending the HL7 message. This will be used for matching purposes. A sample HL7 SENDING APPLICATION could be "ServiceZ".</td>
</tr>
<tr class="even">
<td>ACTIVE</td>
<td>704.108,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this mapping- table is ACTIVE or not.</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.108,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is a comment about the mapping- table. A sample COMMENT could be "Default DeviceX ServiceZ mapping table".</td>
</tr>
<tr class="even">
<td>SOURCE_ID</td>
<td>704.108,.21</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This field identifies the source of the HL7 message. A sample SOURCE ID could be "DeviceX".</td>
</tr>
<tr class="odd">
<td>SOURCE_APPLIC ATION</td>
<td>704.108,.22</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td><p>This field is the application regarded as the source of the HL7 message. A sample SOURCE APPLICATION could be</p>
<p>"ServiceZ".</p></td>
</tr>
<tr class="even">
<td>SOURCE_VERSIO N</td>
<td>704.108,.23</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This field is the version of the source of the HL7 message. A sample SOURCE VERSION could be "VerN-ReleaseN.NN".</td>
</tr>
<tr class="odd">
<td>SOURCE_TRUSTE D</td>
<td>704.108,.24</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether data processed via this source/mapping-table is "trusted" or not. Only verified data will be filed. Verification may be done with user intervention or it may be automatic. Trusted mapping-tables will have their data filed as "verified" without user intervention.</td>
</tr>
</tbody>
</table>

> [1](\l)TERM_MAPPING_PAIR File (#704.109)

> NOTICE: This file is maintained exclusively by the CP Terminology group and must not be modified or edited in any way. Subsequent releases of CP Terminology may create lasting errors in the CliO data store if this file is changed.

> This file correlates a vendor (VENDOR KEY field \#.1) with a mapping-table (MAPPING TABLE ID field \#.01) and an HL7 message segment (TERM TYPE field \#.03). A sample entry could be interpreted as follows: Mapping-TableXX is used for processing when VendorX has sent an XType message.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td><p>MAPPING_TABLE</p>
<p>_ID</p></td>
<td>704.109,.01</td>
<td><p>POINTER TO TERM_MAPPING</p>
<p>_TABLE FILE (#7</p>
<p>04.108)</p></td>
<td>This identifies the mapping-table of this TERM MAPPING PAIR entry. A sample could identify "Mapping-TableXX".</td>
</tr>
<tr class="even">
<td>RECORD INDEXES:</td>
<td></td>
<td>PK (#772)</td>
<td></td>
</tr>
<tr class="odd">
<td>TERM_TYPE</td>
<td>704.109,.03</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td>This field will determine the HL7 message segment relating to this term mapping pair; and identifies a term-type in the TERM TYPE File (#704.102). A sample could be a TERM TYPE identifying the HL7 message segment with "XType" data to be related to this term mapping pair.</td>
</tr>
<tr class="even">
<td>TERM</td>
<td>704.109,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the TERM relating to this term mapping pair. A sample TERM could identify "TEMPERATURE".</td>
</tr>
<tr class="odd">
<td>VENDOR_KEY</td>
<td>704.109,.1</td>
<td><p>FREE TEXT (1-</p>
<p>240 char)</p></td>
<td>This field indicates the vendor related to this term mapping pair. A sample VENDOR KEY could be "111X213".</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_VIEW File (#704.111)

> This file maintains the views displayed within a flowsheet via the Clinical Flowsheets application. A view is a group of terms displayed together. A sample view could display "ICU VITALS, INPUTS, OUTPUTS, and ICU HEMODYNAMICS" information together in a section of a flowsheet displayed via the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>VIEW_ID</td>
<td>704.111,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is the view's Global Unique IDentifier (GUID). This value is maintained nationally and represents this view throughout the enterprise. A sample VIEW ID could be "{11AA9949-B1FA-40A5-A208- 5BB8255BE961}".</td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.111,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the NAME of this view. A sample NAME could be "ICU HEMODYNAMICS".</td>
</tr>
<tr class="odd">
<td>TIME_INTERVAL</td>
<td>704.111,.03</td>
<td>NUMBER (1-1440)</td>
<td>A view is displayed to the user as part of a "page" on the screen. That page is divided into TIME INTERVALs. This field is the number of minutes within an interval when the page is initially displayed to the user. The maximum is 1440 (1 day). A sample TIME INTERVAL could be "60".</td>
</tr>
<tr class="even">
<td>X_AXIS</td>
<td>704.111,.04</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Terminology;</p>
<p>'1' FOR Date/Time;</p></td>
<td>This field indicates whether the initial layout of the view's horizontal axis shows terminology information or date/time information. The information not indicated to display horizontally will initially display vertically.</td>
</tr>
<tr class="odd">
<td>DISPLAY_NAME</td>
<td>704.111,.05</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name of this view to display to the user when this view is being used. A sample DISPLAY NAME could be "ICU Hemodynamics".</td>
</tr>
<tr class="even">
<td>ALLOW_PIVOT</td>
<td>704.111,.06</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether the user is allowed to "pivot" how information is displayed. For example: If initially this view's terminology information displays horizontally and date/time information displays vertically, a '1' value ("YES") in this field gives the user the option to display this view's terminology information vertically and the date/time information horizontally.</td>
</tr>
<tr class="odd">
<td>NATIONAL_TITL E</td>
<td>704.111,.08</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this view is a NATIONAL TITLE, maintained nationally, and cannot be modified at/by a site.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ACTIVE</td>
<td>704.111,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether this view is ACTIVE or not. An ACTIVE view can be incorporated into a flowsheet.</td>
</tr>
<tr class="even">
<td>COMMENT</td>
<td>704.111,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This field is free-text comment to describe the use and purpose of this view. A sample COMMENT could be "National ICU Flowsheet View".</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_VIEW_TERMINOLOGY File (#704.1111)

> This file maintains the relationships between views of OBS_VIEW File (#704.111) and terms of TERM file (#704.001).

> Some field descriptions are directed to a programming and development audience.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>VIEW_ID</td>
<td>704.1111,.01</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This field identifies an entry in the OBS VIEW File (#704.111); correlates this file entry with a view.</td>
</tr>
<tr class="even">
<td>TERM_ORDER</td>
<td>704.1111,.02</td>
<td>NUMBER (1-999)</td>
<td>This field indicates the order this term will display in that view identified by VIEW ID (field #.01).</td>
</tr>
<tr class="odd">
<td>TERM_ID</td>
<td>704.1111,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies an entry in the TERM File (#704.001); correlates this file entry with a term.</td>
</tr>
<tr class="even">
<td>DISPLAY_NAME</td>
<td>704.1111,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This name will display to the user when the Clinical Flowsheets application shows this term (TERM ID field #.03). A sample DISPLAY NAME could be "IV - Platelets".</td>
</tr>
<tr class="odd">
<td>DISPLAY_WIDTH</td>
<td>704.1111,.05</td>
<td><p>NUMBER (80-</p>
<p>9999)</p></td>
<td>This field is the number of pixels this term (TERM ID field #.03) will require to be displayed in the Clinical Flowsheets application. A sample could be "120".</td>
</tr>
<tr class="even">
<td>DISPLAY_TOTAL</td>
<td>704.1111,.06</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a summation of term (TERM ID field #.03) measurements will display at the bottom of a grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td>DISPLAY_COUNT</td>
<td>704.1111,.07</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether or not a count of terms (TERM ID field#.03) related to the view (VIEW ID field #.01) will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td>DISPLAY_AVERA GE</td>
<td>704.1111,.08</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether an average of term (TERM ID field #.03) measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td>DISPLAY_ONLY</td>
<td>704.1111,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This indicates whether this term (TERM ID field#.03) in this view (VIEW ID field#.01) is only for display and reporting purposes and cannot be modified.</td>
</tr>
<tr class="even">
<td>DISPLAY_COLU MNS</td>
<td>704.1111,.1</td>
<td>NUMBER (0-9)</td>
<td>When a "picklist" value is displayed for input in a radio group box this value is used to indicate how many columns this term-value will be displayed in.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>DISPLAY_IN_CEL L_TOTAL</td>
<td>704.1111,.11</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a sub-totals of indicated totals (e.g., total(#.06), count(#.07), average(#.08) etc.) display within each TIME INTERVAL (file #704.111 field #.03) of this view (VIEW ID #.01).</td>
</tr>
<tr class="even">
<td>DISPLAY_MINIM UM</td>
<td>704.1111,.12</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the least of a list of term measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td>DISPLAY_MAXI MUM</td>
<td>704.1111,.13</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the greatest of a list of term measurements will display at the bottom of the grid shown via the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td>REQUIRED_TER M</td>
<td>704.1111,.14</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this term (TERM ID #.03) must be given a value when using this view (VIEW ID #.01) for input.</td>
</tr>
<tr class="odd">
<td>USE_DROPDOWN</td>
<td>704.1111,.15</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether a value for this term will necessitate the use of a "drop down" instead of a "radio group". With long "picklists" it is sometimes necessary to display items in a drop down instead of a radio group.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_VIEW_FILTER File (#704.1112)

> This file maintains relationships between view entries in the OBS VIEW file (#704.1111) and qualifiers/filters.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>VIEW_ID</td>
<td>704.1112,.01</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This field identifies an entry in the OBS VIEW File (#704.111); correlates this file entry with a view.</td>
</tr>
<tr class="even">
<td>TERM_ORDER</td>
<td>704.1112,.02</td>
<td>NUMBER (1-9999)</td>
<td>This is the order of the filter in this file entry.</td>
</tr>
<tr class="odd">
<td>RECORD INDEXES:</td>
<td></td>
<td>PK (#730)</td>
<td></td>
</tr>
<tr class="even">
<td>FILTER_TYPE</td>
<td>704.1112,.03</td>
<td>POINTER TO TERM_TYPE FILE (#704.102)</td>
<td>This is the type of term this filter uses.</td>
</tr>
<tr class="odd">
<td>FILTER_TERM</td>
<td>704.1112,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This field identifies the term this filter relates to; correlates this file entry to a TERM File (#704.101) entry. This is the term/qualifier by which to filter.</td>
</tr>
<tr class="even">
<td>FILTER_USAGE</td>
<td>704.1112,.05</td>
<td><p>SET</p>
<p>'0' FOR DEFAULT VALUE;</p>
<p>'1' FOR MANDATORY VALUE;</p></td>
<td>This field is to indicate whether this filter is mandatory or a default when entering new data.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_FLOWSHEET File (#704.112)

> This file maintains the flowsheets used by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>FLOWSHEET_ID</td>
<td>704.112,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>HELP-PROMPT: Answer with the Global Unique IDentifier (GUID) for this flowsheet. This value is the Global Unique IDentifier for this flowsheet. This value is system generated, maintained nationally, so this value represents the same flowsheet throughout the enterprise. A sample FLOWSHEET ID could be "{E2237CB1-7706-4B43-A96C- D08B812D2A2E}".</td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.112,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the official NAME for this flowsheet (#.01). A sample NAME could be "ICU MONITORING".</td>
</tr>
<tr class="odd">
<td>DISPLAY_NAME</td>
<td>704.112,.03</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name displayed via the Clinical Flowsheets application for this flowsheet. A sample DISPLAY NAME could be "ICU Monitoring".</td>
</tr>
<tr class="even">
<td>COMMENT</td>
<td>704.112,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a free-text COMMENT to document the purpose for this flowsheet (#.01). A sample COMMENT could be "Primary flowsheet for ICU patients".</td>
</tr>
<tr class="odd">
<td>ACTIVE</td>
<td>704.112,.05</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This field indicates whether this flowsheet (#.01) can be used in the Clinical Flowsheets application.</td>
</tr>
<tr class="even">
<td>DEFAULT_TIU_N OTE</td>
<td>704.112,.06</td>
<td>POINTER TO TIU DOCUMENT DEFINITION FIL E (#8925.1)</td>
<td>This field correlates this entry to an entry in the TIU DOCUMENT File (#8925).</td>
</tr>
<tr class="odd">
<td>DISPLAY_KARDE X</td>
<td>704.112,.07</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether the "Kardex grid" will be displayed when this flowsheet (#.01) is opened.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_FLOWSHEET_PAGE File (#704.1121)

> This file maintains the relationships between OBS_FLOWSHEET file (#704.112) entries and pages/view (OBS_VIEW file \#704.111) entries.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>FLOWSHEET_ID</td>
<td>704.1121,.01</td>
<td><p>POINTER TO OBS_FLOWSHEE T FILE (#704.11 2)</p>
<p>(Key field)</p></td>
<td>This field identifies the flowsheet that correlates to this file entry.</td>
</tr>
<tr class="even">
<td>PAGE_ORDER</td>
<td>704.1121,.02</td>
<td>NUMBER (1-99)</td>
<td>This field is the order of display for this view in the flowsheet (#.01).</td>
</tr>
<tr class="odd">
<td>VIEW_ID</td>
<td>704.1121,.03</td>
<td><p>POINTER TO OBS_VIEW FILE (#704.111) (Key</p>
<p>field)</p></td>
<td>This field identifies a page/view displayed via this flowsheet (#.01).</td>
</tr>
<tr class="even">
<td>PAGE_TYPE</td>
<td>704.1121,.04</td>
<td><p>SET</p>
<p>'0' FOR Mandatory;</p>
<p>'1' FOR Optional;</p>
<p>'2' FOR</p>
<p>Supplemental;</p></td>
<td>This field indicates how this view (#.03) will be utilized in this flowsheet (#.01).</td>
</tr>
<tr class="odd">
<td>DISPLAY_NAME</td>
<td>704.1121,.05</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td><p>This is a name to override the default DISPLAY NAME (file #704.112, field #.03).</p>
<p>This name will display when this page/view (#.03) is shown with this flowsheet (#.01). A sample DISPLAY NAME could be "NurseX ICU Monitoring".</p></td>
</tr>
<tr class="even">
<td>SPECIAL_INSTRU CTIONS</td>
<td>704.1121,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td><p>This is free-text to provide a way to give additional instruction, comment, or note about the use of this view (#.03) with this flowsheet (#.01). A sample SPECIAL INSTRUCTIONS</p>
<p>value could be "Pivot the page when possible".</p></td>
</tr>
</tbody>
</table>

> [1](\l)OBS_FLOWSHEET_SUPP_PAGE File (#704.1122)

> This file maintains supplemental pages/views. The supplemental page is a variation of a page as supported via the OBS_FLOWSHEET_PAGE file (#704.1121).

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.1122,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally, so this value identifies this supplemental page throughout the enterprise.</td>
</tr>
<tr class="even">
<td>VIEW_ID</td>
<td>704.1122,.02</td>
<td>POINTER TO OBS_VIEW FILE (#704.111)</td>
<td>This identifies the view for this supplemental page (#.01); correlates this entry with an entry in the OBS_VIEW File (#704.111).</td>
</tr>
<tr class="odd">
<td>PATIENT_ID</td>
<td>704.1122,.03</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the patient assigned to this supplemental page (#.01); correlates this entry with a PATIENT File (#2) entry.</td>
</tr>
<tr class="even">
<td>DEFAULT_METH OD_ID</td>
<td>704.1122,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default method to use with this supplemental page (#.01). This method is a TERM File (#704.101) entry. A sample DEFAULT METHOD ID could be an identifier for the term "ARTERIAL LINE".</td>
</tr>
<tr class="odd">
<td>DEFAULT_POSITI ON_ID</td>
<td>704.1122,.05</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default position to use with this supplemental page (#.01). This position is a TERM File (#704.101) entry. A sample DEFAULT POSITION ID could be an identifier for the term "LYING".</td>
</tr>
<tr class="even">
<td>DEFAULT_LOCA TION_ID</td>
<td>704.1122,.06</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default location to use with this supplemental page (#.01). This location is a TERM File (#704.101) entry. A sample DEFAULT LOCATION ID could be an identifier for the term "ANKLE".</td>
</tr>
<tr class="odd">
<td>DEFAULT_PROD UCT_ID</td>
<td>704.1122,.07</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the default product to use with this supplemental page (#.01). This product is a TERM File (#704.101) entry. A sample DEFAULT PRODUCT ID could be an identifier for the term "5% PRODUCT X".</td>
</tr>
<tr class="even">
<td>DISPLAY_NAME</td>
<td>704.1122,.08</td>
<td><p>FREE TEXT (1-</p>
<p>100 char)</p></td>
<td>This is the DISPLAY NAME to override the view display name (file #704.111, field #.05) when activated. A sample DISPLAY NAME could be "IV Input Blood Products".</td>
</tr>
<tr class="odd">
<td>STATUS</td>
<td>704.1122,.09</td>
<td><p>SET</p>
<p>'0' FOR INACTIVE;</p>
<p>'1' FOR ACTIVE;</p></td>
<td>This indicates whether this supplemental page (#.01) is active or inactive for this patient's (#.03) treatment.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>SET_ID</td>
<td>704.1122,.1</td>
<td>POINTER TO OBS_SET FILE (#704.116)</td>
<td>This field identifies the OBSERVATION SET file (#704.116) entry that correlates with this entry.</td>
</tr>
<tr class="even">
<td>ACTIVATED_DA TE_TIME</td>
<td>704.1122,.11</td>
<td>DATE</td>
<td>This is the date/time this supplemental page (#.01) is activated.</td>
</tr>
<tr class="odd">
<td>ACTIVATED_BY_ ID</td>
<td>704.1122,.12</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) to activate this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td>ACTIVATED_CO MMENT</td>
<td>704.1122,.13</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td>This is the user supplied comment stored when the page is activated. A sample ACTIVATED COMMENT could be "supplemental page X activated by request".</td>
</tr>
<tr class="odd">
<td>ACTIVATED_AS_ TYPE</td>
<td>704.1122,.14</td>
<td><p>SET</p>
<p>'0' FOR Mandatory;</p>
<p>'<strong>1' FOR Optional;</strong></p>
<p>'2' FOR</p>
<p>Supplemental;</p></td>
<td>This indicates a purpose for the activation of this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td>DEACTIVATED_ DATE_TIME</td>
<td>704.1122,.21</td>
<td>DATE</td>
<td>This is the date/time this supplemental page (#.01) was deactivated.</td>
</tr>
<tr class="odd">
<td>DEACTIVATED_ BY_ID</td>
<td>704.1122,.22</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that deactivated this supplemental page (#.01).</td>
</tr>
<tr class="even">
<td>DEACTIVATED_ COMMENT</td>
<td>704.1122,.23</td>
<td><p>FREE TEXT (1-</p>
<p>200 char)</p></td>
<td><p>This is a user supplied comment stored when this supplemental page (#.01) is deactivated. A sample DEACTIVATED COMMENT</p>
<p>could be "patient/treatment is no longer applicable".</p></td>
</tr>
</tbody>
</table>

> [1](\l)OBS_FLOWSHEET_TOTAL File (#704.1123)

> This file maintains flowsheets (file \#704.112) and observation totals (file \#704.113) relationships.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>FLOWSHEET_ID</td>
<td>704.1123,.01</td>
<td><p>POINTER TO OBS_FLOWSHEE T FILE (#704.11 2)</p>
<p>(Key field)</p></td>
<td>This identifies the flowsheet file entry for this flowsheet total entry.</td>
</tr>
<tr class="even">
<td>TOTAL_ID</td>
<td>704.1123,.02</td>
<td>POINTER TO OBS_TOTAL FILE (#704.113)</td>
<td>This identifies an observation total file entry to correlate with this flowsheet total entry.</td>
</tr>
<tr class="odd">
<td>TOTAL_ORDER</td>
<td>704.1123,.03</td>
<td><p>NUMBER</p>
<p>(Between 1 and 99)</p></td>
<td>This field determines the order in which this flowsheet total will be executed and displayed.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_TOTAL File (#704.113)

> This file maintains observation totals.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.113,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td><p>This field is a unique IDentifier for this TOTAL. This ID is maintained nationally so it identifies this TOTAL throughout the enterprise. A sample ID could be</p>
<p>"{217D131C-13C3-4B9E-A401- D1345766182B}".</p></td>
</tr>
<tr class="even">
<td>NAME</td>
<td>704.113,.02</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a descriptive NAME for this total (#.01). A sample name could be "OUTTAKE TOTALS".</td>
</tr>
<tr class="odd">
<td>DISPLAY_NAME</td>
<td>704.113,.03</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is a user friendly name. This is used when displaying this total via the Clinical Flowsheets application. A sample DISPLAY NAME could be "New Flowsheet Outtake Total".</td>
</tr>
<tr class="even">
<td>DEFAULT_UNIT</td>
<td>704.113,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the measurement-unit to be used with the observation total (#.01). The DEFAULT UNIT is an entry in the TERM (#704.101) file. A sample DEFAULT UNIT could identify the term "lbs" or "pounds".</td>
</tr>
<tr class="odd">
<td>DECIMAL_PRECI SION</td>
<td>704.113,.05</td>
<td><p>NUMBER (1-8</p>
<p>Number Precision)</p></td>
<td>This is the decimal precision to round the total values to.</td>
</tr>
<tr class="even">
<td>ACTIVE</td>
<td>704.113,.09</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This indicates whether this total (#.01) can be used by the Clinical Flowsheets application.</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.113,.1</td>
<td><p>FREE TEXT (1-</p>
<p>250 char)</p></td>
<td>This is a descriptive COMMENT about this total (#.01) entry. A sample COMMENT could be "New totaling apparatus for OUTTAKE totals - default lbs ".</td>
</tr>
<tr class="even">
<td>DISPLAY_TOTAL</td>
<td>704.113,.201</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display a total of all observations.</td>
</tr>
<tr class="odd">
<td>DISPLAY_COUNT</td>
<td>704.113,.202</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display a count of observations.</td>
</tr>
<tr class="even">
<td>DISPLAY_AVERA GE</td>
<td>704.113,.203</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the average of all observations.</td>
</tr>
<tr class="odd">
<td>DISPLAY_DIFFER ENCE</td>
<td>704.113,.204</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>(Future Use.)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>DISPLAY_RATIO</td>
<td>704.113,.205</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>(Future Use.)</td>
</tr>
<tr class="even">
<td>DISPLAY_MINIM UM</td>
<td>704.113,.206</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the least value registered of all observations.</td>
</tr>
<tr class="odd">
<td>DISPLAY_MAXI MUM</td>
<td>704.113,.207</td>
<td><p>SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p></td>
<td>This field indicates whether this total (#.01) will display the greatest value registered of all observations.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_TOTAL_TERMINOLOGY File (#704.1131)

> This maintains relationships between OBS TOTAL file (#704.113) entries and TERM file (#704.101) entries.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>TOTAL_ID</td>
<td>704.1131,.01</td>
<td>POINTER TO OBS_TOTAL FILE (#704.113)</td>
<td>This identifies the observation total portion of this total-terminology entry.</td>
</tr>
<tr class="even">
<td>TERM_ID</td>
<td>704.1131,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the term portion of this total- terminology entry.</td>
</tr>
<tr class="odd">
<td>TERM_ORDER</td>
<td>704.1131,.03</td>
<td><p>NUMBER (Key</p>
<p>field)</p></td>
<td>This field indicates the display order of this term (#.02) within this observation total (#.01).</td>
</tr>
<tr class="even">
<td>TERM_DISPLAY_ NAME</td>
<td>704.1131,.04</td>
<td><p>FREE TEXT (1-50</p>
<p>char)</p></td>
<td>This is the name to display within the Clinical Flowsheets application for this total terminology entry. A sample TERM DISPLAY NAME could be "TOTs IntakeX".</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_ALARM File (#704.115)

> This file supports the Clinical Flowsheets application "alarm" functionality. And the file maintains the relationships between alarms and patients.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.115,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is a Global Unique IDentifier (GUID) for this alarm. The GUID is maintained nationally so this value represents this item throughout the enterprise.</td>
</tr>
<tr class="even">
<td>PATIENT_ID</td>
<td>704.115,.02</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the patient for which this alarm (#.01) is applicable.</td>
</tr>
<tr class="odd">
<td>TERM_ID</td>
<td>704.115,.03</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This is the term to be monitored when the Clinical Flowsheets application determines whether to signal an alarm.</td>
</tr>
<tr class="even">
<td>UNIT_ID</td>
<td>704.115,.04</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the unit of measurement to use when Clinical Flowsheets compares observed and "alarm" values.</td>
</tr>
<tr class="odd">
<td>ALARM_TYPE</td>
<td>704.115,.05</td>
<td><p>SET</p>
<p>0' FOR Value in range;</p>
<p>1' FOR Value not in range;</p>
<p>2' FOR Value greater than;</p>
<p>3' FOR Value less than;</p>
<p>4' FOR Value in Picklist;</p>
<p>5' FOR Value is True;</p>
<p>6' FOR Value is False;</p></td>
<td>This indicates the case, when satisfied by an observed value, for the assigned patient and term that may cause the Clinical Flowsheets application to trigger the alarm (#01).</td>
</tr>
<tr class="even">
<td>MIN_VALUE</td>
<td>704.115,.06</td>
<td><p>NUMBER (Number between - 999999999 and</p>
<p>999999999)</p></td>
<td>This field is the minimum value for this term (#.03) and unit (#.04) that will not trigger the alarm (#.01).</td>
</tr>
<tr class="odd">
<td>MAX_VALUE</td>
<td>704.115,.07</td>
<td><p>NUMBER (Number between - 999999999 and</p>
<p>999999999)</p></td>
<td>This field is the maximum value for this term (#.03) and unit (#.04) that will not trigger alarm.</td>
</tr>
<tr class="even">
<td>ALARM_SET</td>
<td>704.115,.08</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This indicates whether this alarm's (#.01) conditions are satisfied.</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 February 2010 File description added.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ACTIVE</td>
<td>704.115,.09</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>This indicates if this alarm (#.01) logic is to be executed on new values (reset).</td>
</tr>
<tr class="even">
<td>ACTIVATED_DA TE_TIME</td>
<td>704.115,.11</td>
<td>DATE</td>
<td>This field is the date/time this alarm (#.01) is to be activated.</td>
</tr>
<tr class="odd">
<td>ACTIVATED_BY_ ID</td>
<td>704.115,.12</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that activated this alarm (#.01).</td>
</tr>
<tr class="even">
<td>DEACTIVATED_ DATE_TIME</td>
<td>704.115,.13</td>
<td>DATE</td>
<td>This is the date/time this alarm (#.01) is to be deactivated.</td>
</tr>
<tr class="odd">
<td>DEACTIVATED_ BY_ID</td>
<td>704.115,.14</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that deactivated this alarm (#.01).</td>
</tr>
<tr class="even">
<td>ACTIVATED_CO MMENT</td>
<td>704.115,.2</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is the comment entered when this alarm (.01) was activated. A sample ACTIVATED COMMENT could be "Alarm activated for automated monitoring".</td>
</tr>
<tr class="odd">
<td>DEACTIVATED_ COMMENT</td>
<td>704.115,.3</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td><p>This is the comment entered when this alarm (.01) was deactivated. A sample DEACTIVATED COMMENT could be</p>
<p>"Alarm deactivated for staff monitoring".</p></td>
</tr>
<tr class="even">
<td>PICKLIST_IDS</td>
<td>704.115,.4</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td><p>This field is a list of VA Unique Identifiers for a "picklist-type" observation. A sample PICKLIST IDS could be: "{65069804-39BF- 41ED-9EA3-BF2C41389F10},{715091C 2-</p>
<p>9668-4678-900E-</p>
<p>6D55D3335A30},{D5B3E135-4D68-4528- BBC9-6E8A7A997104}"</p></td>
</tr>
</tbody>
</table>

### [1](\l)OBS_SET File (#704.116)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains sets of observations used by the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>SET_ID</td>
<td>704.116,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample SET ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td><p>ENTERED_DATE</p>
<p>_TIME</p></td>
<td>704.116,.02</td>
<td>DATE</td>
<td>This field is the date/time this set (#.01) was created.</td>
</tr>
<tr class="odd">
<td>ENTERED_BY_ID</td>
<td>704.116,.03</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This field identifies the person (file #200) that created this set (#.01).</td>
</tr>
<tr class="even">
<td>PUBLIC</td>
<td>704.116,.04</td>
<td><p>SET</p>
<p>'0' FOR No;</p>
<p>'1' FOR Yes;</p></td>
<td>(Future use - indicate whether this is used by other applications / public.)</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.116,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is the user supplied COMMENT about the purpose of this set (.01). A sample COMMENT could be "Auto-Generated Set".</td>
</tr>
<tr class="even">
<td>COUNT</td>
<td>704.116,.911</td>
<td>COMPUTED</td>
<td>This is the number of observations assigned to this set (#.01).</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_SET_OBS_PAIR File (#704.1161)

> This file maintains the relationships between observations and observation sets.

| Field Name | Field Number | Format                         | Description                                                                          |
|----------------|------------------|------------------------------------|------------------------------------------------------------------------------------------|
| SET_ID         | 704.1161,.01     | POINTER TO OBS_SET FILE (#704.116) | This identifies the set file (#704.116) entry part of this set-observation pair.         |
| OBS_ID         | 704.1161,.02     | POINTER TO OBS FILE (#704.117)     | This identifies the observation file (#704.117) entry part of this set-observation pair. |

> 1 Patch MD\*1.0\*16 January 2011 File description added.

### [1](\l)OBS File (#704.117)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file maintains observations for use with the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>OBS_ID</td>
<td>704.117,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is a Globally Unique IDentifier (GUID) for this entry. This is maintained nationally so it is the same throughout the enterprise. A sample OBS ID could be "{69DBD11E-9A8C- 4ECE-AFA4-73947218807D}".</td>
</tr>
<tr class="even">
<td>PARENT_ID</td>
<td>704.117,.02</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the parent observation in the case of a complex observation.</td>
</tr>
<tr class="odd">
<td>FACILITY_ID</td>
<td>704.117,.03</td>
<td>POINTER TO DOMAIN FILE (#4.2)</td>
<td>This identifies the domain (file #4.2) relevant to this observation (#.01).</td>
</tr>
<tr class="even">
<td>HOSPITAL_LOCA TION_ID</td>
<td>704.117,.04</td>
<td>POINTER TO HOSPITAL LOCATION FILE (#44)</td>
<td>This identifies the hospital location (file #44) relevant to this observation (#.01).</td>
</tr>
<tr class="odd">
<td>OBSERVED_DAT E_TIME</td>
<td>704.117,.05</td>
<td>DATE</td>
<td>This is the date/time this observation (#.01) took place.</td>
</tr>
<tr class="even">
<td>OBSERVED_BY_I D</td>
<td>704.117,.06</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that made this observation.</td>
</tr>
<tr class="odd">
<td>TERM_ID</td>
<td>704.117,.07</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies the type of observation. This "type" is an entry in the TERM File (#704.101). A sample TERM ID here could reference the term "SYSTOLIC PRESSURE".</td>
</tr>
<tr class="even">
<td>PATIENT_ID</td>
<td>704.117,.08</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This identifies the PATIENT (file #2) for whom this observation (#.01) was taken.</td>
</tr>
<tr class="odd">
<td>STATUS</td>
<td>704.117,.09</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Removed;</p></td>
<td>This field indicates the current status of this observation (#.01).</td>
</tr>
<tr class="even">
<td>SVALUE</td>
<td>704.117,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This field represents the value of the observation (#.01). A sample SVALUE could be "122/55".</td>
</tr>
<tr class="odd">
<td>SOURCE</td>
<td>704.117,.21</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This field is the source of the SVALUE (#.1). A sample SOURCE could be "instrument" or "CP Flowsheets".</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>SOURCE_COMME NTS</td>
<td>704.117,.22</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td><p>This is any comment type information generated by the source about this observation (#.01). A sample SOURCE COMMENTS</p>
<p>could be "Routine MDZCLIO Tag BUILD".</p></td>
</tr>
<tr class="even">
<td>SOURCE_DATA_I TEM_ID</td>
<td>704.117,.23</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This field contains source (#.21) generated information for later tagging. A sample SOURCE DATA ITEM ID could be "CPFLOWSHEETS.EXE:C13A6427".</td>
</tr>
<tr class="odd">
<td>SOURCE_VERSIO N</td>
<td>704.117,.24</td>
<td><p>FREE TEXT (1 –</p>
<p>50 char)</p></td>
<td>This is the version of the source (#.21) that generated this observation (#.01). A sample SOURCE VERSION could be “1.0".</td>
</tr>
<tr class="even">
<td><p>ENTERED_DATE</p>
<p>_TIME</p></td>
<td>704.117,.25</td>
<td>DATE</td>
<td>This is the date and time this entry was placed into this observation file.</td>
</tr>
<tr class="odd">
<td>ENTERED_BY_ID</td>
<td>704.117,.26</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) who entered the data for this observation (#.01).</td>
</tr>
<tr class="even">
<td>CHILD_ORDER</td>
<td>704.117,.27</td>
<td>NUMBER (Number 1 - 999)</td>
<td>This is the order that this observation is placed into its parent observation (#.02).</td>
</tr>
<tr class="odd">
<td>RANGE</td>
<td>704.117,.28</td>
<td><p>SET</p>
<p>'0' FOR Unknown;</p>
<p>'1' FOR Normal; '2' FOR Out Of</p>
<p>Bounds Low; '3' FOR Out Of</p>
<p>Bounds High; '4' FOR Low;</p>
<p>'5' FOR High;</p></td>
<td>This indicates the condition of the observation value (#.1).</td>
</tr>
<tr class="even">
<td>COMMENT</td>
<td>704.117,.4</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text for additional clinical COMMENT. A sample COMMENT could be "test O2 saturation".</td>
</tr>
<tr class="odd">
<td>AUDIT_EXISTS</td>
<td>704.117,.911</td>
<td>COMPUTED</td>
<td>This indicates whether or not any record exists in the audit log for this observation.</td>
</tr>
<tr class="even">
<td>CORRECTION_FO R_ID</td>
<td>704.117,.912</td>
<td>COMPUTED</td>
<td>This identifies the record this observation was entered to correct.</td>
</tr>
</tbody>
</table>

> [1](\l)OBS_QUALIFIER File (#704.118)

> This file maintains relationships between observations and qualifiers.

| Field Name | Field Number | Format                      | Description                                                          |
|----------------|------------------|---------------------------------|--------------------------------------------------------------------------|
| OBS_ID         | 704.118,.01      | POINTER TO OBS FILE (#704.117)  | This identifies the observation part of this observation/qualifier pair. |
| QUALIFIER_ID   | 704.118,.02      | POINTER TO TERM FILE (#704.101) | This identifies the qualifier part of this observation/qualifier pair.   |

> [1](\l)OBS_AUDIT File (#704.119)

> This file maintains the chains of observation audits for Clinical Flowsheets observations. An audit is defined here as a change in an observation's status, state, or condition.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>AUDIT_ID</td>
<td>704.119,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample AUDIT ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td>AUDIT_TYPE</td>
<td>704.119,.02</td>
<td><p>SET</p>
<p>'0' FOR Record Status Update; '1' FOR Record Verified;</p>
<p>'2' FOR Record Marked For Purging;</p>
<p>'3' FOR Record Marked For Archiving;</p>
<p>'4' FOR Record Corrected;</p>
<p>'5' FOR Record Rescinded;</p></td>
<td>This indicates the type of audit; the reason for the audit.</td>
</tr>
<tr class="odd">
<td>AUDIT_OBSERV ATION</td>
<td>704.119,.03</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation that has been audited via this entry.</td>
</tr>
<tr class="even">
<td>AUDIT_DATE_TI ME</td>
<td>704.119,.04</td>
<td>DATE</td>
<td>This is the date/time this audit occurred.</td>
</tr>
<tr class="odd">
<td>AUDIT_AUTHOR</td>
<td>704.119,.05</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that created this audit entry.</td>
</tr>
<tr class="even">
<td>STATUS_ORIGIN AL</td>
<td>704.119,.06</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Rescinded;</p></td>
<td>This indicates the status/condition of the observation (#.03) before this audit entry (#.01) was created.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>STATUS_NEW</td>
<td>704.119,.07</td>
<td><p>SET</p>
<p>'0' FOR Unverified;</p>
<p>'1' FOR Verified;</p>
<p>'2' FOR Archived;</p>
<p>'3' FOR Purged;</p>
<p>'4' FOR Corrected;</p>
<p>'5' FOR Rescinded;</p></td>
<td>This indicates the status/condition of the observation (#.03) after this audit entry (#.01) was created.</td>
</tr>
<tr class="even">
<td>REPLACEMENT_ OBSERVATION</td>
<td>704.119,.08</td>
<td>POINTER TO OBS FILE (#704.117)</td>
<td>This identifies the observation that was replaced by a new observation via this audit.</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.119,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is a COMMENT provided by the person as documentation per this observation audit (#.01). A sample COMMENT could be "Verified with Clinical Flowsheets".</td>
</tr>
</tbody>
</table>

> [1](\l)CP_KARDEX_ACTION File (#704.121)

> This file supports Clinical Flowsheets scheduled tasks and actions functionality.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ID</td>
<td>704.121,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This value is the Global Unique IDentifier (GUID) for this entry. This value is maintained nationally and is the same throughout the enterprise. A sample ID could be "{2E0C516D-3858-4A1F-A2F3- BF0AB9E3A7FC}".</td>
</tr>
<tr class="even">
<td>TASK_ID</td>
<td>704.121,.02</td>
<td>POINTER TO TERM FILE (#704.101)</td>
<td>This identifies a task in the TERM File (#704.101).</td>
</tr>
<tr class="odd">
<td>SCHEDULE_ID</td>
<td>704.121,.03</td>
<td>POINTER TO CP_SCHEDULE FILE (#704.008)</td>
<td>This identifies the schedule (#704.008) to use with the task (#.02).</td>
</tr>
<tr class="even">
<td>PATIENT_ID</td>
<td>704.121,.04</td>
<td>POINTER TO PATIENT FILE (#2)</td>
<td>This field identifies the patient (file #2) assigned to this task.</td>
</tr>
<tr class="odd">
<td>START_DATE_TI ME</td>
<td>704.121,.05</td>
<td>DATE</td>
<td>This is the date/time the execution of this task is permitted.</td>
</tr>
<tr class="even">
<td>STOP_DATE_TIM E</td>
<td>704.121,.06</td>
<td>DATE</td>
<td>This is the date/time the execution of this task is no longer permitted.</td>
</tr>
<tr class="odd">
<td>SCHEDULE_TYPE</td>
<td>704.121,.07</td>
<td><p>SET</p>
<p>'0' FOR</p>
<p>Continuous; '1' FOR PRN;</p>
<p>'2' FOR One-Time;</p>
<p>'3' FOR Stat;</p>
<p>'4' FOR Now;</p></td>
<td>This field indicates the type of schedule used for this task.</td>
</tr>
<tr class="even">
<td>PRN_TYPE</td>
<td>704.121,.08</td>
<td><p>SET</p>
<p>'0' FOR No PRN; '1' FOR PRN-And;</p>
<p>'2' FOR PRN- AndNTE;</p>
<p>'3' FOR PRN-Or;</p></td>
<td>This field indicates the Pro Re Nata (PRN) option for task.</td>
</tr>
<tr class="odd">
<td>STATUS</td>
<td>704.121,.09</td>
<td><p>SET</p>
<p>'0' FOR Active;</p>
<p>'1' FOR Expired;</p>
<p>'2' FOR</p>
<p>Discontinued; '3' FOR Held;</p></td>
<td>This field indicates the status of the task.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>SPECIAL_INSTRU CTIONS</td>
<td>704.121,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text for instructions for this particular task. A sample SPECIAL INSTRUCTIONS could be "Turn patient 90 degrees".</td>
</tr>
<tr class="even">
<td>PRN_NTE_AMOU NT</td>
<td>704.121,.21</td>
<td>NUMBER (Number 1 - 999)</td>
<td>This field the maximum number of times this task should executed. This field is used in the case of tasks with a PRN option.</td>
</tr>
<tr class="odd">
<td>FIRST_SCHEDUL ED_TIME</td>
<td>704.121,.22</td>
<td><p>FREE TEXT (1 – 4</p>
<p>char)</p></td>
<td>This is the military time of the first time that this item should be executed once the start date/time has been reached. A sample FIRST SCHEDULED TIME could be "1330" to represent "01:30 PM" as the first time this task should be executed.</td>
</tr>
<tr class="even">
<td>CUSTOM_SCHED ULED_TIMES</td>
<td>704.121,.3</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This field is a custom schedule. If the user wished to modify the schedule for this task (#.02), the schedule here in a military times. A sample CUSTOM SCHEDULED TIMES could be "0400,0800,1200,1600,2000".</td>
</tr>
</tbody>
</table>

> [1](\l)CP_KARDEX_EVENTS File (#704.1211)

> This file supports Clinical Flowsheets scheduled events/actions functionality.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>EVENT_ID</td>
<td>704.1211,.01</td>
<td><p>FREE TEXT (38</p>
<p>char)</p></td>
<td>This is a Globally Unique IDentifier (GUID) for this entry. This is maintained nationally so it is the same throughout the enterprise. A sample EVENT ID could be "{69DBD11E- 9A8C-4ECE-AFA4-73947218807D}".</td>
</tr>
<tr class="even">
<td>CARE_ACTION_I D</td>
<td>704.1211,.02</td>
<td>POINTER TO CP_KARDEX_AC TION FILE (#704.121)</td>
<td>This identifies the action (#704.121) to which this event will be assigned.</td>
</tr>
<tr class="odd">
<td>DUE_DATE_TIME</td>
<td>704.1211,.03</td>
<td>DATE</td>
<td>This is the date/time this event is scheduled to be executed.</td>
</tr>
<tr class="even">
<td>COMPLETED_DA TE_TIME</td>
<td>704.1211,.04</td>
<td>DATE</td>
<td>This is the date/time this event was actually done.</td>
</tr>
<tr class="odd">
<td><p>COMPLETED_BY</p>
<p>_ID</p></td>
<td>704.1211,.05</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) who marked this event as completed.</td>
</tr>
<tr class="even">
<td>STATUS</td>
<td>704.1211,.09</td>
<td><p>SET</p>
<p>'0' FOR PENDING;</p>
<p>'1' FOR COMPLETED; '2' FOR HELD;</p>
<p>'3' FOR REFUSED;</p></td>
<td>This indicates the status, condition, or state of this event.</td>
</tr>
<tr class="odd">
<td>COMMENT</td>
<td>704.1211,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is a free-text, user entered COMMENT for this event. A sample COMMENT could be "This event was completed on time. It was entered late".</td>
</tr>
<tr class="even">
<td>AUDIT_COUNT</td>
<td>704.1211,.991</td>
<td>COMPUTED</td>
<td>This is a calculated count of the number of audits for this event.</td>
</tr>
</tbody>
</table>

> [1](\l)CP_KARDEX_AUDIT File (#704.1212)

> This file maintains audits of scheduled event/tasks via the Clinical Flowsheets application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 41%" />
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
<td>ACTION_ID</td>
<td>704.1212,.01</td>
<td>POINTER TO CP_KARDEX_AC TION FILE (#704.121)</td>
<td>This identifies the audited scheduled task.</td>
</tr>
<tr class="even">
<td>EVENT_ID</td>
<td>704.1212,.02</td>
<td>POINTER TO CP_KARDEX_EV ENTS FILE (#704.1211)</td>
<td>This identifies the audited event.</td>
</tr>
<tr class="odd">
<td>AUDIT_DATE_TI ME</td>
<td>704.1212,.03</td>
<td>DATE</td>
<td>This is the date/time that the audit record is created.</td>
</tr>
<tr class="even">
<td>AUDIT_BY_ID</td>
<td>704.1212,.04</td>
<td>POINTER TO NEW PERSON FILE (#200)</td>
<td>This identifies the person (file #200) that created this audit.</td>
</tr>
<tr class="odd">
<td>AUDIT_DESCRIP TION</td>
<td>704.1212,.1</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text automatically generated by the Clinical Flowsheets application when an audit is created. A sample could be AUDIT DESCRIPTION "Event placed in Hold Status".</td>
</tr>
<tr class="even">
<td>AUDIT_COMMEN T</td>
<td>704.1212,.2</td>
<td><p>FREE TEXT (1 –</p>
<p>250 char)</p></td>
<td>This is free-text generated by the user (#.04) when creating this audit. A sample AUDIT COMMENT could be "Provider action required a hold".</td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*16 January 2011 File description added.

> <span id="Package_Default_Definition" class="anchor"></span>NO

> NO

> 1Patch MD\*1.0\*6 May 2008 Default definitions added for 702.001, 704.201, 704.202, and 704.209.

> 2Patch MD\*1.0\*5 August 2006 Default definitions added for 703.9.

> 3 Patch MD\*1.0\*16 January 2011 Default definitions added for 704,001 - 704.1212.

## [1](\l)Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Missing Required HL7 Element

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.001 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Missing required HL7 element.

> DESCRIPTION: An element that is required according to the HL7 message profile is missing in the FileMan data for the current record.

> TEXT:

> Required element \|1\| is missing for record \|2\| in File \#\|3\|. PARAMETER SUBSCRIPT: 3

> PARAMETER DESCRIPTION: FileMan file number that is the source of the missing d PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: Missing HL7 element identified by SEGMENT.FIELD\[.COMPON ENT\[.SUBCOMPONENT\]\].

> PARAMETER SUBSCRIPT: 2

> PARAMETER DESCRIPTION: IEN or IENS (comma delimited) of the FileMan record mis sing that is the source of the missing data. A sub-file IEN would be represented as sub-file IEN,file IEN (e.g., 2,121. Where the sub-file IEN=2 and the file IEN

> =121.).

### Invalid Key Passed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.002 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Invalid key passed.

> DESCRIPTION: The passed key has no corresponding entry in the Patient Movement File (#405).

> TEXT:

> No entry in ^DGPM() for IEN \|1\|. PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: IEN of Patient Movement File.

### No Record in Patient File for DFN Passed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.003 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: No record in Patient File for DFN passed.

> DESCRIPTION: There is no entry in ^DPT (file \#2) for the DFN extracted from the Patient Movement File (#405).

> TEXT:

> There is no entry in ^DPT for DFN \|1\|. PARAMETER SUBSCRIPT: 1

> PARAMETER DESCRIPTION: DFN from Patient Movement File(#405)

### Required Segment Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DIALOG NUMBER: 7040020.004 TYPE: ERROR

> INTERNAL PARAMETERS NEEDED: YES PACKAGE: CLINICAL PROCEDURES

> SHORT DESCRIPTION: Required segment missing

> DESCRIPTION: This error occurs when a segment that is required for a particular message has no data in the database.

> TEXT:

> Required segment \|1\| is not returned for IEN \|2\| in File \#\|3\|.

> PARAMETER SUBSCRIPT: 1 PARAMETER DESCRIPTION: HL7 Segment name. PARAMETER SUBSCRIPT: 2

> PARAMETER DESCRIPTION: IEN of record returning no segment.

> PARAMETER SUBSCRIPT: 3

> PARAMETER DESCRIPTION: File in which there is no data for the IEN.

> 1 Patch MD\*1.0\*16 January 2011 Added Dialogs section.
