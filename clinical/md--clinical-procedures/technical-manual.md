---
title: Clinical Procedures Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1
group_key: "MD:MD:1"
file_numbers: 
  - 2
  - 702
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - procedures
  - clinical
  - class
  - description
  - build
  - strong
  - table
  - number
  - parameter
  - procedure
page_count: 0
word_count: 24449
section_count: 16
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

Clinical Procedures (CP)Technical Manual and Package Security Guide

![](clinical-procedures-version-1-technical-manual/001.png)

Version 1.0April 2004Revised December 2018Department of Veterans AffairsOffice of Information and Technology (OI&T)Product Development

#### Revision History

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 20%" />
<col style="width: 31%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Description</strong></td>
<td><strong>Date</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td><p>Patch MD*1.0*65</p>
<p>High Volume Procedure Edit option update and Consult to CP Conversion utilities</p></td>
<td>December 2018</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>Patch MD*1.0*60</p>
<p>Updated CP Instrument File table and Option list.</p></td>
<td>July 2018</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Patch MD*1.0*42:</p>
<p>Updated cover page and Revision History.</p>
<p>Added new CONSULT KEEP OPEN field to CP Instrument File table on page <u><a href="#consult_keep_open">5-9</a>.</u></p></td>
<td>March 2016</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>Patch MD*1.0*29 – Updated for ICD-10 release.</p>
<p>Updated Title page</p>
<p>Added Revision History, pp. i-ii</p>
<p>Updated Table of Contents, pp. iii-iv</p>
<p>Updated option to read the generic ICD in place of ICD-9, pp. <a href="#icd10">6-9</a> .</p></td>
<td>August 2014</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a>Patch MD*1.0*20 released. Added new Exported Options and Updated the Routine Descriptions. Added new Parameter Definitions.</td>
<td>November 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a>Patch MD*1.0*21 released. Updated Routine Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a>Patch MD*1.0*11 released. Updated Routine Description, File and Field Description, Parameter Definition, and Menu Options By Name.</td>
<td>June 2009</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><a href="#fn6" class="footnote-ref" id="fnref6" role="doc-noteref"><sup>6</sup></a>Patch MD*1.0*6 released. Added description of Hemodialysis module and 508 Compliance to Introduction; updated Routine Descriptions, File List, Package Default Definition, Remote Procedure Calls, Parameter Definitions, menu options, Cross References, Callable Routines, External Relations, Internal Relations, and Glossary. Removed individual vendor contact information from Ch.15.</td>
<td>May 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn7" class="footnote-ref" id="fnref7" role="doc-noteref"><sup>7</sup></a>Patch MD*1.0*14 released. Updated Routine Descriptions, File List, Parameter Definitions, Protocols, menu options, and Cross References. Deleted bad references to Sample Reports in Ch. 15.</td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p><a href="#fn8" class="footnote-ref" id="fnref8" role="doc-noteref"><sup>8</sup></a>Patch MD*1.0*5 released August 2006. Updated File List, Package Default</p>
<p>Definition, Parameter Definitions, and menu options.</p></td>
<td>Documented February 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Patch MD*1.0*2 released.</td>
<td>August 2006</td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#fn9" class="footnote-ref" id="fnref9" role="doc-noteref"><sup>9</sup></a>Patch MD*1.0*1 released.</td>
<td>July 2004</td>
<td></td>
</tr>
<tr class="even">
<td>Originally released.</td>
<td>April 2004</td>
<td></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch MD*1.0*42 March 2016 Patch 42 release added<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Patch MD*1.0*29 August 2014 Patch 29 release added<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Patch MD*1.0*20 November 2010 Patch 20 release added<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>Patch MD*1.0*21 June 2010 Patch 21 release added.<a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5"><p>Patch MD*1.0*11 June 2009 Patch 11 release added.<a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn6"><p>Patch MD*1.0*6 May 2008 Patch 6 release added.<a href="#fnref6" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn7"><p>Patch MD*1.0*14 March 2008 Patch 14 release added.<a href="#fnref7" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn8"><p>Patch MD*1.0*5 August 2006 Patch 5 release added.<a href="#fnref8" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn9"><p>Patch MD*1.0*1 and MD*1.0*2 July 2004 Patch 2 release added.<a href="#fnref9" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

######### Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Benefits](#benefits)
  - [[^2]508 Compliance](#2508-compliance)
- [Implementation and Maintenance](#implementation-and-maintenance)
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
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [SAC Exemptions](#sac-exemptions)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Security Features](#security-features)
- [[^42]Vendor Interfaces](#42vendor-interfaces)
  - [List of Vendor Interfaces](#list-of-vendor-interfaces)
  - [Device Setup Instructions](#device-setup-instructions)
    - [Clinivision](#clinivision)
    - [Endoworks](#endoworks)
    - [Muse](#muse)
    - [Sensormedics V-MAX](#sensormedics-v-max)
    - [[^52]B. Braun](#52b-braun)
    - [[^53]Fresenius Medical Care](#53fresenius-medical-care)
    - [[^54]Gambro](#54gambro)
- [Glossary](#glossary)
- [[^67]XML Extensible Markup Language – A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.](#67xml-extensible-markup-language-a-simplified-subset-of-standard-generalized-markup-language-sgml-its-primary-purpose-is-to-facilitate-the-sharing-of-data-across-different-information-systems)
CP is a conduit for passing final patient results, using Health Level 7 (HL7) messaging, between vendor clinical information systems (CIS) and Veterans Health Information Systems and Technology Architecture (VistA). The patient’s test result or report is displayed through the Computerized Patient Record System (CPRS). The report data is stored on the Imaging Redundant Array of Inexpensive Disks (RAID) and in some instances, discrete data is stored in the Medicine database.
CP provides features that can be used across clinical departments such as general medicine, cardiology, pulmonary, women’s health, neurology, and rehabilitation medicine.
[^1]Hemodialysis is a new module of the Clinical Procedures (CP) package that provides features specific to hemodialysis treatment. The Hemodialysis module allows you to collect hemodialysis treatment information from the medical device, and manually enter treatment data into the application.
Pre-dialysis vitals, information obtained during treatment, and post-dialysis vitals can be entered into the Hemodialysis data entry screens. A Treatment Summary is created and used to fill out Centers for Medicare & Medicaid Services (CMS)/End Stage Renal Disease (ESRD) forms.

## Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> a. Standardized and Common User Interface

> Clinicians can go through the same program, CPRS, to enter, review, interpret, and sign CP orders. CP documents in TIU obey Authorization Subscription Utility (ASU) Business Rules. The update users functionality currently used by Consults determines which users are allowed to access or edit CP documents.

> b. Integration

> The ordering process of a CP procedure is initiated by CPRS and processed through the Consult/Request Tracking Package (Consults). The interpretation of the data is entered and displayed through TIU. The final result of the CP procedure is displayed by VistA Imaging. The ordering, viewing, reviewing, interpreting, and signing of the CP medical record is accessed through one location, the Consults tab in CPRS.

> c. Variety of Accepted File Types

> CP is able to accept data/final result report files from automated instruments in .txt, .rtf, .jpg, .jpeg, .bmp, .tiff, .pdf, and .html file types. CP allows additional automated instruments and file types to be added to interface with CP in the future.

> d. Links to Other Packages

> CP interfaces with packages such as Computerized Patient Record System (CPRS), Consult/Request Tracking Package, Text Integration Utility Package (TIU), and VistA Imaging. New Health Summary components shall be available in the future.

> e. Interface Between CP and Imaging

> Certain images such as consent forms and report objects are acquired, processed, stored, transmitted, and displayed by the VistA Imaging package. This interface will replace existing capture interface between Medicine 2.3 and VistA Imaging.

> f. Inpatient and Outpatient Workloads

> CP Definition file (#702.01) allows for defining the Hospital Location where the procedure is performed. This determines which Encounter Form is presented to the end user. CPRS and TIU parameters allow for the configuration of TIU software to prompt users to enter workload data which is then passed to the Patient Care Encounter software (PCE) for both inpatients and outpatients.

## [^2]508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The following notice applies only to Patch MD\*1.0\*6.

The Clinical Procedures Hemodialysis Software is exempt from coverage under the Section 508 standards. The definition of "electronic and information technology" in the Section 508 standards specifically excludes "medical equipment where information technology is integral to its operation." 36 C.F.R. Section 1194.4. VHA's use of the Clinical Procedures Hemodialysis Software also does not violate Section 508 because it will not affect access to the data or information provided by that software. 29 U.S.C. Section 794d(a). The data or information collected by the software is immediately made available through the CPRS system, which is accessible to people with disabilities.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to Chapter 1 – Introduction of the Clinical Procedures Implementation Guide for implementation and maintenance issues.

# Clinical Instrument Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to Chapter 10 of the Clinical Procedures Implementation Guide for information on Setting up HL7 Parameters.

[^3]Refer to the Clinical Instrument Bi-Directional Interface Specifications document for information on Clinical Procedures instrument interface specifications. Directions for locating the document follow:

1.  Access the Clinical Procedures website: <http://vista.med.va.gov/clinicalspecialties/clinproc/>
2.  On the navigation bar found on the left-hand side of the page, hover your mouse pointer over Clinical Procedures Project, then click Documentation.
3.  Click Clinical Procedures Documents.

Click the Clinical Procedures Bi-Directional Communication Specification link to view the document or save a copy.

# Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MDAPI ; HOIFO/DP/NCA - CP API Calls ; \[05-05-2003 10:28\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDAPI1 ; HOIFO/NCA - Electrocardiogram Data Extraction ;12/4/02 12:32

;;1.0;CLINICAL PROCEDURES;\*\*1\*\*;Apr 01, 2004

MDAR7M ; HOIFO/NCA - Get Text Impression ;2/27/09 12:38

;;1.0;Clinical Procedures;\*\*21,24\*\*;Apr 01, 2004;Build 8

MDARP3 ; HOIFO/NCA - Get Procedures for Medicine ;1/13/04 14:35

;;1.0;CLINICAL PROCEDURES;\*\*10,13,24\*\*;Apr 01, 2004;Build 8

MDARSET ; HOIFO/NCA - High Volume Check-In Setup ; 7/11/18 1:14pm

;;1.0;CLINICAL PROCEDURES;\*\*21,65\*\*;Apr 01, 2004;Build 1

MDCA01 ;HINES OIFO/DP/BJ/TJ - HL7 Build Admit/Visit Message (A01);15-AUG-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA02 ;HINES OIFO/DP/BJ/TJ - HL7 Build Transfer a Patient (A02) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA03 ;HINES OIFO/DP/BJ/TJ - HL7 Build Discharge/End Visit (A03) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA08 ;HINES OIFO/DP/BJ/TJ - HL7 Build Update Patient Info (A08) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA11 ;HINES OIFO/DP/BJ/TJ - HL7 Build Cancel Admit/Visit Notice (A11) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA12 ;HINES OIFO/DP/BJ/TJ - HL7 Build Cancel Transfer (A12) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCA13 ;HINES OIFO/DP/BJ/TJ - HL7 Build Cancel Discharge/Visit End (A13) Message;21-JUN-2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCADT ;HINES OIFO/DP/BJ/TJ - HL7 Build ADT Axx Messages;10 Aug 2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12\*\*;Apr 01, 2004;Build 318

MDCEVN ;HINES OIFO/DP/BJ/TJ - Wrapper to create HL7 EVN segment;30 May 2006

;;1.0;CLINICAL PROCEDURES;\*\*16,12,23\*\*;Apr 01, 2004;Build 281

MDCLIO ;HINES OIFO/DP - CliO backend driver;02 Feb 2005

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCLIO1 ;HINES OIFO/DP - CliO backend driver (Continuation);02 Sep 2005

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCLIOV ;HINES OIFO/DP - CliO Vitals Link;15 Nov 2010

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCLN ;HIOFO/NCA - Cleanup Disabled Studies ;4/19/01 11:52

;;1.0;Clinical Procedures;\*\*21\*\*;Apr 01, 2004;Build 30

MDCONUTL ; WOIFO/KLM - CP Conversion Utility ; 7/11/18 1:08pm

;;1.0;CLINICAL PROCEDURES;\*\*65\*\*;Apr 01, 2004;Build 2

MDCPHL7A ;HINES OIFO/BJ - CliO HL7 Handler/validator;09 Aug 2006

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCPHL7B ;HINES OIFO/BJ - CliO HL7 Handler/validator;09 Aug 2006

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCPHL7C ; HINES OIFO/BJ - CP Outbound message record maintenance routine.;26OCT 2011

;;1.0;CLINICAL PROCEDURES;\*\*23\*\*;OCT 26, 2011;Build 281

MDCPID ;HINES OIFO/DP/BJ - Wrapper for PID Segment Builder;23 Nov 2005

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCPMESQ ;HINES OIFO/TJ - CP Outbound message queue routine.;30 Jul 2007 ;10/5/11 15:39

;;1.0;CLINICAL PROCEDURES;\*\*12,23\*\*;Apr 01, 2004;Build 281

MDCPROTD ;ASMR/BLJ,SRG - CliO backend driver;02 Feb 2005 ; 12/10/15 10:58am

;;1.0;CLINICAL PROCEDURES;\*\*38\*\*;Sep 25, 2015;Build 290

MDCPSIGN ;HINES OIFO/BJ - CliO HL7 Handler/validator;23 Aug 2006

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCPURG ;HINES OIFO/DP - CP Nightly Purge Options;27 Jan 2008

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDCPV1 ;HINES OIFO/DP/BJ - PV1 Segment Routine;08 Aug 2007

;;1.0;CLINICAL PROCEDURES;\*\*16,23\*\*;Apr 01, 2004;Build 281

MDCPVDEF ;HINES OIFO/BJ/TJ - CP Outbound message record maintenance routine.;30 Jul 2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12,23\*\*;Apr 01, 2004;Build 281

MDCSPV1 ;HINES OIFO/DP/BJ - Build Segment PV1 Routine;17 Aug 2007

;;1.0;CLINICAL PROCEDURES;\*\*16,23\*\*;Apr 01, 2004;Build 281

MDCUTL ;HINES OIFO/DP/BJ/TJ - HL7 Message Utilities;07 June 2007

;;1.0;CLINICAL PROCEDURES;\*\*16,12,23\*\*;Apr 01, 2004;Build 281

MDCVT ; HOIFO/DP/NCA - Medicine Package Conversion ;10/20/04 12:49

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDCVT1 ; HOIFO/NCA - Medicine Package Conversion (Cont.) ;1/6/05 15:12

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDCVTU ; HOIFO/NCA - Medicine Conversion Verification Utility ; \[08-28-2003 11:34\]

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDDEVCL ;HOIFO/NCA - Collect Device Data ;8:34 AM 9 Jun 2005

;;1.0;CLINICAL PROCEDURES;\*\*20\*\*;Apr 01, 2004;Build 9

MDESPRT ;HOIFO/NCA - ELECTRONIC SIGNATURE PRINT ;12/21/04 09:24

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDHL7A ; HOIFO/WAA - Routine to Decode HL7 for CP ;05/21/09 15:57

;;1.0;CLINICAL PROCEDURES;\*\*6,11,21\*\*;Apr 01, 2004;Build 30

MDHL7B ; HOIFO/WAA -Bi-directional interface routine ;7/23/01 11:41

;;1.0;CLINICAL PROCEDURES;\*\*41\*\*;Apr 01, 2004;Build 3

MDHL7BH ; HOIFO/WAA,WOIFO/PMK -Bi-directional interface (HL7) routine ;15 Jun 2018 12:46 PM

;;1.0;CLINICAL PROCEDURES;\*\*11,21,20,60\*\*;Apr 01, 2004;Build 11

MDHL7D ; HOIFO/WAA -B-Braun, Fresenius Dialysis ; 06/08/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDHL7E ; HOIFO/WAA -Olympus/CMore/Pentax Endoscopy ; 06/08/00

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7K1 ; HOIFO/WAA-KenitDx Interface ; 06/08/00

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 30

MDHL7K2 ; HOIFO/WAA -HP EnConcert Echo ; 06/08/00

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7M1 ; HOIFO/WAA - Muse EKG ; \[02-06-2002 16:13\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7M3 ; HOIFO/WAA-GE IMAGE VAULT INTERFACE ; 08/08/07

;;1.0;CLINICAL PROCEDURES;\*\*37\*\*;Apr 15, 2003;Build 4

MDHL7MCA ; HOIFO/REL-Routine to Decode HL7 for MEDICINE ; \[05-07-2001 10:38\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDHL7MCX ; HIRMFO/WAA - Generate HL7 Error Message for MEDICINE ; \[05-07-2001 10:38\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7P1 ; HOIFO/WAA-Sensormedics,Jaeger Pulmonary ; 06/08/00

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7R1 ; HOIFO/WAA -Clinivision Resporatory ; 06/13/02

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7U ; HOIFO/WAA -Routine utilities for CP ;7/23/01 11:41

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7U1 ; HOIFO/WAA -Routine utilities for CP PROCESSING OBX ; 7/26/00

;;1.0;CLINICAL PROCEDURES;\*\*11\*\*;Apr 01, 2004;Build 67

MDHL7U2 ; HOIFO/WAA -Utilities for CP PROCESSING OBX text ; 7/26/00

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDHL7U3 ;HOIFO/WAA - Utilities for CP to process HL7 messages ;02/17/10 15:59

;;1.0;CLINICAL PROCEDURES;\*\*6,21,29\*\*;Apr 01, 2004;Build 22

MDHL7X ; HOIFO/WAA -Generate HL7 Error Message ; 06/08/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDHL7XXX ; HOIFO/DP - Loopback device for CP ;4/10/09 09:20

;;1.0;CLINICAL PROCEDURES;\*\*21,34\*\*;Apr 01, 2004;Build 1

MDIPS60 ;WOIFO/DAC - Install code for MD\*1.0\*60 ;18 Apr 2018 7:38 AM

;;3.0;IMAGING;\*\*60\*\*;Mar 19, 2002;Build 2

MDKRPC1 ;HIOFO/FT-RPC to return patient data ;8/12/16 10:45am

;;1.0;CLINICAL PROCEDURES;\*\*6,47\*\*;Apr 01, 2004;Build 3

MDKRPC2 ; HOIFO/DP - RPC Calls (Cont.) ;11/27/07 09:42

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDKUTL ; HOIFO/DP - Renal Utilities ;11/29/07 14:45

;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01, 2004;Build 20

MDKUTLR ; HOIFO/DP - Renal Utilities RPC;11/29/07 14:45

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDNCHK ; HOIFO/NCA - CP Multiple Result Check ;7/26/10 14:27

;;1.0;CLINICAL PROCEDURES;\*\*11,21,20\*\*;Apr 01, 2004;Build 9

MDOUTOR ; HOIFO/NCA - Post Conversion Routine ; \[04-14-2003 10:51\]

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDPCE ; HIRMFO/NCA - Routine For Data Extract ;6/9/08 13:29

;;1.0;CLINICAL PROCEDURES;\*\*5,21\*\*;Apr 01, 2004;Build 30

MDPCE1 ; HOIFO/NCA - Updated Routine For Data Extract ; \[05-28-2002 12:55\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDPCE2 ; HOIFO/NCA - Routine For Data Extract For Hemo Dialysis ;1/20/10 10:00

;;1.0;CLINICAL PROCEDURES;\*\*6,21,29\*\*;Apr 01, 2004;Build 22

MDPFTP1 ;HOIFO/NCA - PFT REPORT-DEMO INFO ;3/15/04 11:55

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPFTP2 ; HOIFO/NCA - PFT REPORT-VOLUMES ;3/15/04 10:00

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPFTP2A ; HOIFO/NCA - PFT REPORT-FLOWS ;3/17/04 08:22

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPFTP3 ; HOIFO/NCA - PFT REPORT-SPECIAL STUDIES (PT 2) ;3/17/04 12:48

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPOST ; HOIFO/DP - Post Init ;2/18/04 11:39

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDPOST04 ; HOIFO/DP - Post Init ; 2/18/04 11:39

;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 3

MDPOST06 ; HOIFO/DP - Post Init ;2/7/07 16:15

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDPOST1 ; HOIFO/NCA/DP - Build CP DEFINITION file (#702.01) - Optional Post

Init ; \[12-04-2002 13:06\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDPOST16 ;HINES OIFO/DP - Post Installation Tasks;02 Mar 2008

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDPOST21 ; HOIFO/NCA - Post Init ;2/7/07 16:15

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 30

MDPOST23 ;HINES OIFO/DP/BJ - Post Installation Tasks;06 OCTOBER 2011

;;1.0;CLINICAL PROCEDURES;\*\*23\*\*;Apr 01, 2004;Build 281

MDPOST38 ;ASMR/MKB - Post Installation Tasks;02 Mar 2008 ; 12/12/13 8:52pm

;;1.0;CLINICAL PROCEDURES;\*\*38\*\*;Sep 25, 2015;Build 290

MDPOST49 ;MNTVBB/RRA - Post Installation Tasks;01/07/17

;;1.0;CLINICAL PROCEDURES;\*\*49\*\*;Apr 01, 2004;Build 2

MDPOST50 ;MNTVBB/RRA - Post Installation Tasks;01/07/17

;;1.0;CLINICAL PROCEDURES;\*\*50\*\*;Apr 01, 2004;Build 2

MDPOST51 ;MNTVBB/RRA - Post Installation Tasks;01/07/17

;;1.0;CLINICAL PROCEDURES;\*\*51\*\*;Apr 01, 2004;Build 8

MDPOST52 ;MNTVBB/RRA - Post Installation Tasks;01/07/17

;;1.0;CLINICAL PROCEDURES;\*\*52\*\*;Apr 01, 2004;Build 6

MDPOST61 ;Post Installation Tasks ; 4/30/18 8:41am

;;1.0;CLINICAL PROCEDURES;\*\*61\*\*;Apr 01, 2004;Build 1

MDPOST6A ;HOIFO/NCA-Convert Existing Notes to New File ;11/28/07 14:31

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDPRE12 ;HINES OIFO/TJ - Pre Installation Tasks;02 Mar 2008

;;1.0;CLINICAL PROCEDURES;\*\*12\*\*;Apr 01, 2004;Build 318

MDPRE16 ;HINES OIFO/DP - Installation Tasks;02 Mar 2008

;;1.0;CLINICAL PROCEDURES;\*\*16\*\*;Apr 01, 2004;Build 280

MDPRE23 ;HINES OIFO/BJ - Installation Tasks;07 OCTOBER 2011

;;1.0;CLINICAL PROCEDURES;\*\*23\*\*;Apr 01, 2004;Build 281

MDPS1 ; HOIFO/NCA - CP/Medicine Report Generator ;5/17/10 08:57

;;1.0;CLINICAL PROCEDURES;\*\*2,10,13,21,24\*\*;Apr 01, 2004;Build 8

MDPS2 ; HOIFO/NCA - CP/Medicine Report Generator (Cont.) ;5/18/04 09:41

;;1.0;CLINICAL PROCEDURES;\*\*2\*\*;Apr 01, 2004

MDPS3 ; HOIFO/NCA - Remote Data View Data Retriever for CP ;8/26/05 14:37

;;1.0;CLINICAL PROCEDURES;\*\*2,5,13,24\*\*;Apr 01, 2004;Build 8

MDPS4 ; HOIFO/NCA - Retrieve List of Consult Procedures ;1/26/06 12:45

;;1.0;CLINICAL PROCEDURES;\*\*13,24\*\*;Apr 01, 2004;Build 8

MDPS5 ; HOIFO/NCA - Retrieve List of Consult Procedures for RDV ;3/4/05 13:29

;;1.0;CLINICAL PROCEDURES;\*\*13\*\*;Apr 01, 2004;Build 19

MDPSU ; HOIFO/NCA - CP/Medicine Report Generator Utility;5/18/04 09:48

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 30

MDPSUL ; HOIFO/NCA - HS Component Utility;5/18/04 09:48 ;10/5/09 09:33

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 30

MDPURGE ;HOIFO/NCA - Study Clean-Up process ;6/18/08 10:15

;;1.0;CLINICAL PROCEDURES;\*\*11\*\*;Apr 01, 2004;Build 67

MDRPCNT ; HOIFO/NCA - Document Handler Object (TMDNOTE) ;5/23/05 15:50

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDRPCNT1 ; HOIFO/NCA - Object RPCs (TMDNOTE) Continued 2;10/29/04 12:20 ;2/25/09 16:08

;;1.0;CLINICAL PROCEDURES;\*\*6,21\*\*;Apr 01, 2004;Build 30

MDRPCOD ; HOIFO/DP - Object RPCs (TMDProcedureDef) ; \[01-09-2003 15:20\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDRPCOG ; HOIFO/DP - CP Gateway ; \[01-09-2003 15:20\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDRPCOL ; HOIFO/DP - Object RPCs (Logfile) ; \[02-11-2002 13:41\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDRPCOO ; HOIFO/DP - Object RPCs (TMDOutput) ; \[03-24-2003 15:44\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDRPCOP ; HOIFO/DP - Object RPCs (TMDPatient) ;8/3/09 10:39

;;1.0;CLINICAL PROCEDURES;\*\*4,6,11,20,42\*\*;Apr 01, 2004;Build 12

MDRPCOP1 ; HOIFO/DP - Object RPCs (TMDPatient) - Cont. ; 01-09-2003 15:21

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDRPCOR ; HOIFO/DP - Object RPCs (TMDRecordId) ; \[01-10-2003 09:14\]

;;1.0;CLINICAL PROCEDURES;\*\*17,20\*\*;Apr 01, 2004;Build 9

MDRPCOT ; HOIFO/DP/NCA - Object RPCs (TMDTransaction) ;10/26/09 10:23

;;1.0;CLINICAL PROCEDURES;\*\*5,6,11,21\*\*;Apr 01, 2004;Build 30

MDRPCOT1 ; HOIFO/NCA/DP,WOIFO/PMK - Object RPCs (TMDTransaction) - Continued ;03 Jul 2018 9:09 AM

;;1.0;CLINICAL PROCEDURES;\*\*5,11,21,41,60\*\*;Apr 01, 2004;Build 11

MDRPCOT2 ; HOIFO/NCA - Object RPCs (TMDTransaction) Continued 2;10/29/04 12:20 ;3/12/08 09:18

;;1.0;CLINICAL PROCEDURES;\*\*6,21,20\*\*;Apr 01, 2004;Build 9

MDRPCOTA ; HOIFO/NCA - Object RPCs (TMDTransaction) Continued 2;10/29/04 12:20 ;3/12/08 09:18

;;1.0;CLINICAL PROCEDURES;\*\*20\*\*;Apr 01, 2004;Build 9

MDRPCOTH ; HOIFO/NCA - Process High Volume Procedure Results ;2/1/12 16:39

;;1.0;CLINICAL PROCEDURES;\*\*21,24\*\*;Apr 01, 2004;Build 8

MDRPCOU ; HOIFO/DP - Object RPCs (TMDUser) ; \[01-09-2003 15:21\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDRPCOV ; HOIFO/DP - Object RPCs (TMDParameter) ; \[04-15-2003 12:42\]

;;1.0;CLINICAL PROCEDURES;;Apr 01, 2004

MDRPCOW ; HOIFO/DP/NCA - Billing Widget ;10/3/05 12:17

;;1.0;CLINICAL PROCEDURES;\*\*6,29\*\*;Apr 01, 2004;Build 22

MDRPCU ; HOIFO/DP - Object RPC Utilities ; \[05-23-2003 10:16\]

;;1.0;CLINICAL PROCEDURES;\*\*4\*\*;Apr 01, 2004;Build 3

MDRPCW ; HOIFO/NCA - Calls to AICS ;01/21/10 11:51

;;1.0;CLINICAL PROCEDURES;\*\*6,21,20,29\*\*;Apr 01, 2004;Build 22

MDRPCW1 ; HOIFO/NCA - MD TMDENCOUNTER Object ;2/16/10 16:17

;;1.0;CLINICAL PROCEDURES;\*\*6,21,20,29\*\*;Apr 01, 2004;Build 22

MDRPCWU ;HOIFO/NCA - CPT Code Query ;2/16/10 16:17

;;1.0;CLINICAL PROCEDURES;\*\*21,29\*\*;Apr 01, 2004;Build 22

MDSTATU ; HOIFO/NCA - Print List of Document Titles Needed ;10/21/04 13:44

;;1.0;CLINICAL PROCEDURES;\*\*5\*\*;Apr 01, 2004;Build 1

MDSTUDL ; HOIFO/NCA - Clinical Procedures Studies List ;10/26/05 11:46

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDSTUDW ; HOIFO/NCA - Print a List of Procedures With Incomplete Workload ;3/2/09 10:00

;;1.0;CLINICAL PROCEDURES;\*\*21\*\*;Apr 01, 2004;Build 30

MDTERM ;HINES OIFO/DP - Terminology Utilities;04 Jan 2006

;;1.0;CLINICAL PROCEDURES;\*\*16,23\*\*;Apr 01, 2004;Build 281

MDTERMX ;HINES OIFO/DP - Installation Tasks;02 Mar 2008 ; 8/4/17 6:45am

;;1.0;CLINICAL PROCEDURES;\*\*48\*\*;Aug 2, 2012;Build 5

MDUXML ; HOIFO/WAA -Utilities for XML text ; 7/26/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDUXMLM ; HOIFO/WAA -Utilities for XML text ; 7/26/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDUXMLOX ; HOIFO/WAA -OBX converter XML text ; 7/26/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDUXMLU1 ; HOIFO/WAA -Utilities for XML text ; 7/26/00

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDWCAN ;HOIFO/NCA - Process No-Shows and Cancels ;7/29/08 09:50

;;1.0;CLINICAL PROCEDURES;\*\*11,21\*\*;Apr 01, 2004;Build 30

MDWCHK ; HOIFO/NCA - Create CP Studies for Existing Procedures ;12/13/07 15:52

;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

MDWOR ; HOIFO/NCA - Main Routine to Decode HL7 ;9/8/08 15:20

;;1.0;CLINICAL PROCEDURES;\*\*14,11,21,20,37,42\*\*;Apr 01,2004;Build 12

MDWORC ; HOIFO/NCA - Main Routine to Decode HL7 from Consult ;1/8/08 15:00

;;1.0;CLINICAL PROCEDURES;\*\*14\*\*;Apr 01,2004;Build 20

MDWORSR ; HOIFO/NCA - Daily Schedule Studies;7/2/04 12:39 ;26 Sep 2017 2:24 PM

;;1.0;CLINICAL PROCEDURES;\*\*14,11,21,20\*\*;Apr 01,2004;Build 9

MDWSETUP ; HOIFO/NCA - Auto Study Check-In Setup ;3/18/08 14:14

;;1.0;CLINICAL PROCEDURES;\*\*14,11,37,45\*\*;Apr 01, 2004;Build 1

MDXMLFM ; HOIFO/DP - Fileman -\> XML Utilities ; \[01-10-2003 09:14\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

MDXMLFM1 ; HOIFO/DP/NCA - Data -\> XML Utilities ; \[01-10-2003 09:14\]

;;1.0;CLINICAL PROCEDURES;\*\*6\*\*;Apr 01, 2004;Build 102

# File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File and Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Transaction File - \#702

This file contains the studies between the instruments and user generated data as it is matched to a consult order and a TIU document is created for the results. It also manages the interface between the images and the Imaging RAID.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Patient</td>
<td>702,.01</td>
<td>Pointer to Patient (#2) file</td>
<td>This field contains a pointer to the Patient (#2) file for this study.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>702,.011</td>
<td>Computed</td>
<td>This field contains the computed value of the patient’s SSN from the Patient (#2) file.</td>
</tr>
<tr class="even">
<td>DOB</td>
<td>702,.012</td>
<td>Computed</td>
<td>This field contains the computed value of the patient’s date of birth from the Patient (#2) file.</td>
</tr>
<tr class="odd">
<td>Created Date/Time</td>
<td>702,.02</td>
<td>Date</td>
<td>This field contains the date/time the study was created within the CP User executable.</td>
</tr>
<tr class="even">
<td>Created By</td>
<td>702,.03</td>
<td>Pointer to New Person (#200) file</td>
<td>This field contains the DUZ of the user that created this study.</td>
</tr>
<tr class="odd">
<td>CP Definition</td>
<td>702,.04</td>
<td>Pointer to CP Definition (#702.01) file</td>
<td>This field contains a pointer to the CP Definition (#702.01) file of the procedure definition that this study represents.</td>
</tr>
<tr class="even">
<td>Consult Number</td>
<td>702,.05</td>
<td>Free Text 1-20 characters in length</td>
<td>This field contains an IEN of the Consult (#123) file representing the Consult order that is matched up to this study.</td>
</tr>
<tr class="odd">
<td>TIU Note</td>
<td>702,.06</td>
<td>Pointer to TIU Document (#8925) file</td>
<td>This field contains a pointer to the TIU Document (#8925) file representing the note that contains the interpretation of this study as well as the links to the associated images.</td>
</tr>
<tr class="even">
<td>Vstring</td>
<td>702,.07</td>
<td>Free Text 1-50 characters in length</td>
<td>This field contains This field contains the vstring. The vstring is in the following format: Visit Type_”;”_Visit Date/Time_”;”_Hospital Location (internal entry number of the visit).</td>
</tr>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Transaction Message</td>
<td>702,.08</td>
<td>Free Text 1-80 characters in length</td>
<td>Contains the message returned from the VistA Imaging API’s for storing the images on the server.</td>
</tr>
<tr class="odd">
<td>Transaction Status</td>
<td>702,.09</td>
<td><p>Set:</p>
<p>0 - New</p>
<p>1 - Submitted</p>
<p>2 - Error</p>
<p>3 - Complete</p></td>
<td>This field contains the status of this study.</td>
</tr>
<tr class="even">
<td>Error Messages (multiple)</td>
<td>702.091,.01</td>
<td>Number between 1-9999, 0 decimal digits</td>
<td>Error message number.</td>
</tr>
<tr class="odd">
<td>Date Received</td>
<td>702.091,.02</td>
<td>Date</td>
<td>Date and time this error message was generated.</td>
</tr>
<tr class="even">
<td>Received From</td>
<td>702.091,.03</td>
<td>Free Text 1-30 characters in length</td>
<td>Where the error was generated.</td>
</tr>
<tr class="odd">
<td>Message</td>
<td>702.091,.09</td>
<td>Free Text 1-150 characters in length</td>
<td>Text of the error message.</td>
</tr>
<tr class="even">
<td>Image (multiple)</td>
<td>702.1,.01</td>
<td>Number between 1-999, 0 decimal digits</td>
<td>Index of attached image for this study.</td>
</tr>
<tr class="odd">
<td>Type</td>
<td>702.1,.02</td>
<td><p>Set:</p>
<p>I - Instrument data</p>
<p>U - User supplied file</p></td>
<td>Type of attachment to be processed.</td>
</tr>
<tr class="even">
<td>Result Report</td>
<td>702.1,.03</td>
<td>Pointer to CP Result Report (#703.1) file</td>
<td>Pointer to the CP Result Report (#703.1) file containing the attachment from the instrument.</td>
</tr>
<tr class="odd">
<td>Status</td>
<td>702.1,.09</td>
<td><p>Set:</p>
<p>0 - Submitted to server</p>
<p>1 - Error in submission</p>
<p>2 - Error in filing</p>
<p>3 - Copied to server</p></td>
<td>Status of this image.</td>
</tr>
<tr class="even">
<td>UNC</td>
<td>702.1,.1</td>
<td>Free Text 1-245 characters in length</td>
<td>Contains the Universal naming Convention (UNC) for this attachment.</td>
</tr>
<tr class="odd">
<td>Submitted to Instrument</td>
<td>702,.11</td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Points to the instrument definition that this study was submitted to at the time of check-in.</td>
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
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Instrument Order Number</td>
<td>702,.12</td>
<td>Free Text 1-22 characters in length</td>
<td>Contains the unique order number for this study that is sent to the bi-directional instrument.</td>
</tr>
<tr class="odd">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Visit</td>
<td>702,.13</td>
<td>Pointer to Visit (#9000010) file</td>
<td>This is the Visit number returned from PCE. Reference IA# 1902.</td>
</tr>
<tr class="even">
<td><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>Scheduled Date/Time</td>
<td>702,.14</td>
<td>Date</td>
<td>This field contains the date/time when the HL7 message should be sent by CP to the device for this CP transaction.</td>
</tr>
<tr class="odd">
<td><a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a>Conversion ID Reference</td>
<td>702,.3</td>
<td>Free text 1-30 characters in length.</td>
<td><p>This field is the Reference Conversion ID. It is a variable</p>
<p>Pointer to the Medicine files. It indicates which converted Medicine</p>
<p>report record is associated with the CP Transaction study. This field helps to keep track which CP Transaction study was created for the Medicine report conversion.</p></td>
</tr>
<tr class="even">
<td>Image Count</td>
<td>702,.991</td>
<td>Computed</td>
<td>Computed field to return the number of images associated with this study.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch MD*1.0*6 May 2008 Field added to support the storing of the Clinical Indicator questions, CPT and ICD9 codes in the CP Transaction file.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Patch MD*1.0*14 March 2008 Field added to support the auto study check-in with scheduled appointment date/time.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Patch MD*1.0*5 August 2006 Field added.<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

[^4]CP_Transaction_TIU_History File - \#702.001

This CP Transaction TIU History file stores all TIU notes that is associated

with the CP Transaction study. This will keep track of multiple notes

associated with one CP study.

|                |                  |                                       |                                                                                                                                                                     |
|----------------|------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Name | Field Number | Format                            | Description                                                                                                                                                     |
| Study_ID       | 702.001,.01      | Pointer To CP Transaction File (#702) | This field contains a pointer to the CP Transaction file (#702).                                                                                                    |
| TIU_Note_ID    | 702.001,.02      | Pointer To TIU Document File (#8925)  | This field contains a pointer to the TIU Document file (#8925) representing the note that contains the interpretation of this CP Transaction. (Reference IA \#3376) |
| Date_Assigned  | 702.001,.03      | Date                                  | This field contains the date/time when the TIU note was assigned to this transaction.                                                                               |

CP Definition File - \#702.01

This file defines all the procedures used by the Clinical Procedures package. All elements that define a procedure are in this file. This file is exported with data, but entries may be added by the site.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Name</td>
<td>702.01,.01</td>
<td>Free Text 3-30 characters in length</td>
<td>This field contains the name of the procedure. It should be descriptive of the procedure and contain 3-30 alphanumeric characters. The first character MUST be a letter. To maintain consistency it is recommended that all procedures be entered in UPPERCASE letters as well.</td>
</tr>
<tr class="odd">
<td>Treating Specialty</td>
<td>702.01,.02</td>
<td>Pointer to Facility Treating Specialty (#45.7) file</td>
<td>This field defines the specialty that this procedure falls under.</td>
</tr>
<tr class="even">
<td>Require External Data</td>
<td>702.01,.03</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Setting this field to Yes will force a consult for this procedure to be processed via the CP User executable for matching whether or not there are instruments associated with it.</td>
</tr>
<tr class="odd">
<td>Default TIU Note</td>
<td>702.01,.04</td>
<td>Pointer to TIU Document Definition (#8925.1) file</td>
<td>This field contains a TIU Note Title to use as the default when CP creates a note for interpretation for this procedure.</td>
</tr>
<tr class="even">
<td>Hospital Location</td>
<td>702.01,.05</td>
<td>Pointer to Hospital Location (#44) file</td>
<td>This is the location that will be used when creating the TIU Note for interpretation.</td>
</tr>
<tr class="odd">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Processing Application</td>
<td>702.01,.06</td>
<td><p>Set:</p>
<p>1 - Default</p>
<p>2 – Hemodialysis</p></td>
<td>This field is used to indicate if this is a Hemodialysis procedure or not. The field is a set of codes, 1=DEFAULT so it will be processed by Clinical Procedures or 2=HEMODIALYSIS and the procedure will be processed by the Hemodialysis application.</td>
</tr>
<tr class="even">
<td>Auto Submit</td>
<td>702.01,.07</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>This field only applies to bi-directional instruments. It is used to indicate whether or not the image attachment should be automatically submitted to VistA Imaging once the procedure is performed and the result is passed to CP.</td>
</tr>
<tr class="odd">
<td>External Data Directory</td>
<td>702.01,.08</td>
<td>Free Text 3-150 characters in length</td>
<td>This field contains a reference to a network share where user supplied attachments are located for this procedure.</td>
</tr>
<tr class="even">
<td>Active</td>
<td>702.01,.09</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Yes/No to indicate active procedures that can be linked to Consults.</td>
</tr>
<tr class="odd">
<td>Instrument (multiple)</td>
<td>702.011,.01</td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Contains a pointer to an instrument that generates results for this procedure.</td>
</tr>
<tr class="even">
<td><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>Processed Result</td>
<td>702.01,.12</td>
<td><p>Set:</p>
<p>0 - Final Result 1 - Multiple Results 2 – Cumulative Result</p></td>
<td><p>This field is a flag which indicates whether a final result, multiple results, or cumulative</p>
<p>result is associated with this procedure.</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch MD*1.0*6 May 2008 Field added to the CP Definition file.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Patch MD*1.0*11 June 2009 New field added.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

CP Instrument File - \#702.09

This file contains the list of instruments used by the Clinical Procedures package. This file is exported with data.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Name</td>
<td>702.09,.01</td>
<td>Free Text 3-30 characters in length</td>
<td>Name or mnemonic of instrument. Used by vendor in HL7 message header.</td>
</tr>
<tr class="odd">
<td>Notification Mailgroup</td>
<td>702.09,.02</td>
<td>Pointer to Mail Group (#3.8) file</td>
<td>Mail group that will receive error messages and other notifications dealing with this device from the interface routines.</td>
</tr>
<tr class="even">
<td>Description</td>
<td>702.09,.03</td>
<td>Free Text 1-50 characters in length</td>
<td>This field contains a short informational description for the instrument.</td>
</tr>
<tr class="odd">
<td>Delete when Submitted</td>
<td>702.09,.05</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Select Yes if you want files created by this instrument deleted once they are successfully copied to the VistA Imaging RAID. Deletion will be performed by the VistA Imaging application.</td>
</tr>
<tr class="even">
<td>Printable Name</td>
<td>702.09,.06</td>
<td>Free Text 3-30 characters in length</td>
<td>Name of instrument that is printed on the reports, etc.</td>
</tr>
<tr class="odd">
<td>Default File Ext</td>
<td>702.09,.07</td>
<td>Free Text (e.g., .txt)</td>
<td>Default file extension for vendor instrument reports (e.g., .doc, .pdf).</td>
</tr>
<tr class="even">
<td>Serial Number</td>
<td>702.09,.08</td>
<td>Free Text 1-50 characters in length</td>
<td>Vendor serial number of the instrument (for reference only).</td>
</tr>
<tr class="odd">
<td>Active</td>
<td>702.09,.09</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Whether or not the instrument is active on the network.</td>
</tr>
<tr class="even">
<td>Processing Routine</td>
<td>702.09,.11</td>
<td>Free Text 1-8 characters in length</td>
<td>MUMPS routine used to process interface information.</td>
</tr>
<tr class="odd">
<td>Processing Code</td>
<td>702.09,.12</td>
<td><p>Set:</p>
<p>M - Medicine</p>
<p>C - CP V. 1.0</p>
<p>B - Both</p></td>
<td><p>Where data is to be processed:</p>
<p>M - Medicine</p>
<p>C - Clinical Procedures</p>
<p>B - Both</p></td>
</tr>
<tr class="even">
<td>Bi-directional</td>
<td>702.09,.13</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>This field indicates whether or not this device can accept HL7 messages from VistA.</td>
</tr>
<tr class="odd">
<td>IP Address</td>
<td>702.09,.14</td>
<td>Free Text 7-15 characters in length</td>
<td>This field contains the IP address of this instrument.</td>
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
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Port</td>
<td>702.09,.15</td>
<td>Number between 1000-99999, 0 decimal digits</td>
<td>This field contains the port number for this instrument.</td>
</tr>
<tr class="odd">
<td>HL7 Instrument ID</td>
<td>702.09,.16</td>
<td>Free Text 3-30 characters in length</td>
<td>This is the name of the actual device where the device name can be ‘”SMC St Louis”.</td>
</tr>
<tr class="even">
<td>HL7 Universal Service ID</td>
<td>702.09,.17</td>
<td>Free Text 1-48 characters in length</td>
<td>This field defines what type of procedure the device can perform if the device can perform multiple types of procedures.</td>
</tr>
<tr class="odd">
<td>HL7 Logical Link</td>
<td>702.09,.18</td>
<td>Pointer to the HL Logical Link (#870) file</td>
<td>This field contains the HL7 logical link.</td>
</tr>
<tr class="even">
<td>CP - DICOM Interoperability</td>
<td>702.09,.19</td>
<td>Set of Codes</td>
<td><p>0:No special action</p>
<p>1:Use VistA Imaging accession number sss-GMR-nnnnnnnn</p>
<p>2:Use VistA Imaging HL7 instead of CP's HL7</p></td>
</tr>
<tr class="odd">
<td>Server Name</td>
<td>702.09,.21</td>
<td>Free Text 1-30 characters in length</td>
<td>Network name of instrument server where the report is stored.</td>
</tr>
<tr class="even">
<td>Server Share</td>
<td>702.09,.22</td>
<td>Free Text 1-30 characters in length</td>
<td>Share folder/drive of the instrument server where the report is stored.</td>
</tr>
<tr class="odd">
<td>Server Path</td>
<td>702.09,.23</td>
<td>Free Text 1-150 characters in length</td>
<td>Path on the network where the report is stored.</td>
</tr>
<tr class="even">
<td>Server Executable</td>
<td>702.09,.24</td>
<td>Free Text 1-30 characters in length</td>
<td>Name of server program that is run to create the report for the interface.</td>
</tr>
<tr class="odd">
<td>Process UNC</td>
<td>702.09,.301</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces UNC type data.</td>
</tr>
<tr class="even">
<td>Process Text</td>
<td>702.09,.302</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces text type data.</td>
</tr>
<tr class="odd">
<td>Process URL</td>
<td>702.09,.303</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces URL type data.</td>
</tr>
<tr class="even">
<td>Process DLL</td>
<td>702.09,.304</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces DLL type data.</td>
</tr>
<tr class="odd">
<td>Process UUEncode</td>
<td>702.09,.305</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces UUEncode type data.</td>
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
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Process XML</td>
<td>702.09,.306</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces XML type data.</td>
</tr>
<tr class="odd">
<td>Process XMS</td>
<td>702.09,.307</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes if this instrument produces XMS type data.</td>
</tr>
<tr class="even">
<td>Consult Keep Open<span id="consult_keep_open" class="anchor"></span></td>
<td>702.09,.401</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>Enter Yes to keep consult note open or No to close consult note.</td>
</tr>
</tbody>
</table>

CP Result Report File - \#703.1

This file contains the information for the results uploaded from the medical instruments used by Clinical Procedures. It is distributed without any data. All fields are automatically stuffed by Clinical Procedures. There is no user input.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Upload ID</td>
<td>703.1,.01</td>
<td>Free Text 1-30 characters in length</td>
<td>Unique identifier assigned for each upload.</td>
</tr>
<tr class="odd">
<td>Patient</td>
<td>703.1,.02</td>
<td>Pointer to Patient (#2) file</td>
<td>Pointer to the Patient (#2) file of the patient uploaded from the result of the instrument.</td>
</tr>
<tr class="even">
<td>Date/Time Performed</td>
<td>703.1,.03</td>
<td>Date</td>
<td>Date/time the procedure was performed on the instrument.</td>
</tr>
<tr class="odd">
<td>Instrument</td>
<td>703.1,.04</td>
<td>Pointer to CP Instrument (#702.09) file</td>
<td>Pointer to the CP Instrument (#702.09) file of the instrument that produced these reports.</td>
</tr>
<tr class="even">
<td>Study Reference Number</td>
<td>703.1,.05</td>
<td>Pointer to CP Transaction file (#702)</td>
<td>This field is used as a reference to the transaction.</td>
</tr>
<tr class="odd">
<td>HL7 Reference Number</td>
<td>703.1,.06</td>
<td>Free Text 1-30 characters in length</td>
<td>This field is used to keep the IEN of the HL7 message. It serves as a reference to the message that will be purged once the data has been successfully moved to the VistA Imaging server.</td>
</tr>
<tr class="even">
<td>Status</td>
<td>703.1,.09</td>
<td><p>Set:</p>
<p>U - Unmatched</p>
<p>M - Matched</p></td>
<td><p>Status of the results:</p>
<p>U - Unmatched</p>
<p>M - Matched</p></td>
</tr>
<tr class="odd">
<td>Upload Item (multiple)</td>
<td>703.11,.01</td>
<td><p>Set:</p>
<p>1 - Impression Text</p>
<p>2 - Report Text</p>
<p>3 - Attachment UNC</p>
<p>4 - Attachment URL</p>
<p>5 - UUEncoded Data</p>
<p>6 - DLL</p>
<p>7 - XML Data</p>
<p>8 - XML Style Sheet</p></td>
<td>This field contains the type of data element that was uploaded from the instrument.</td>
</tr>
<tr class="even">
<td>Attachment UNC</td>
<td>703.11,.02</td>
<td>Free Text 1-240 characters in length</td>
<td>This field contains the Universal Naming Convention (UNC) for this attachment. This indicates where the attachment is located.</td>
</tr>
</tbody>
</table>

|                |                  |                                      |                                                                   |
|----------------|------------------|--------------------------------------|-------------------------------------------------------------------|
| Field Name | Field Number | Format                           | Description                                                   |
| Item Value     | 703.11,.1        | Free Text 1-245 characters in length | If the uploaded item is a single string value, it is stored here. |
| Item Text      | 703.11,.2        | Word-Processing                      | If the uploaded data is multi-lined, it is stored here.           |

[^5]CP Conversion File- \#703.9

 

This file is used for storing the site parameters needed and used to convert Medicine reports to CP Text reports. This file also stores the status of the conversion process for each converted Medicine report.

 

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Name</td>
<td>703.9,.01</td>
<td>Free Text (Required)</td>
<td>This field contains the name of the CP conversion.  It is only accessible by the CP conversion routine.  It is exported with one "DEFAULT" entry.</td>
</tr>
<tr class="odd">
<td>Mode</td>
<td>703.9,.02</td>
<td><p>Set:</p>
<p>0 - test</p>
<p>1 - real</p></td>
<td>This field indicates if the CP conversion is in test or real mode.</td>
</tr>
<tr class="even">
<td>Administrative Closure User</td>
<td>703.9,.03</td>
<td>Pointer to new person file (#200)</td>
<td>This field points to the New Person file (#200).  It is used to indicate the Administrative Closure person used to close the TIU documents for the CP conversion.</td>
</tr>
<tr class="odd">
<td>Scratch HFS Directory</td>
<td>703.9,.1</td>
<td>Free Text</td>
<td>This field stores the scratch HFS directory used for the CP conversion.  CP conversion program will use this directory to convert Medicine reports.</td>
</tr>
<tr class="even">
<td>Medicine File Parameters</td>
<td>703.91,.01</td>
<td>Pointer to File file (#1)</td>
<td>This field points to the File file (#1).  It is used to store the Medicine file number that this parameter is pertaining to. (Reference IA #4507)</td>
</tr>
<tr class="odd">
<td>CP Definition</td>
<td>703.91,.02</td>
<td>Point to CP Definition File (#702.01)</td>
<td>This field contains the CP Definition to which the Medicine Report will be mapped.</td>
</tr>
<tr class="even">
<td>Convert Y/N</td>
<td>703.91,.03</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>This field is used as a flag to mark the Medicine Report. Enter 0 for 'to not convert' or 1 for 'to convert'.</td>
</tr>
<tr class="odd">
<td>Convert if No Status</td>
<td>703.91,.04</td>
<td><p>Set:</p>
<p>0 - No</p>
<p>1 - Yes</p></td>
<td>This field is used as a flag to indicate whether the Medicine report should be converted or not be converted, if there is no status for the report.  The field is 0 for 'not to convert' or 1 for 'to convert'.</td>
</tr>
<tr class="even">
<td>Use TIU Note Title</td>
<td>703.91,.05</td>
<td>Pointer to TIU Document Definition File (#8925.1)</td>
<td>This field stores the Historical TIU note title used for the conversion of the Medicine reports to CP reports. (Reference IA #3377 and 3568)</td>
</tr>
<tr class="odd">
<td>Conversion ID</td>
<td>703.92,.01</td>
<td>Free Text</td>
<td><p>This field is the Conversion ID. It is a variable pointer to the Medicine files. This field will store an entry for each Medicine file record converted. This field is a variable pointer to the following files:</p>
<p>691 ECHO</p>
<p>691.1 CARDIAC CATHETERIZATION</p>
<p>691.5 ELECTROCARDIOGRAM (EKG)</p>
<p>691.6 HOLTER</p>
<p>691.7 EXERCISE TOLERANCE TEST</p>
<p>691.8 ELECTROPHYSIOLOGY (EP)</p>
<p>694 HEMATOLOGY</p>
<p>694.5 CARDIAC SURGERY RISK ASSESSMENT</p>
<p>698 GENERATOR IMPLANT</p>
<p>698.1 V LEAD IMPLANT</p>
<p>698.2 A LEAD IMPLANT</p>
<p>698.3 PACEMAKER SURVEILLANCE</p>
<p>699 ENDOSCOPY/CONSULT</p>
<p>699.5 GENERALIZED PROCEDURE/CONSULT</p>
<p>700 PULMONARY FUNCTION TESTS</p>
<p>701 RHEUMATOLOGY</p></td>
</tr>
<tr class="even">
<td>Status</td>
<td>703.92,.02</td>
<td><p>Set:</p>
<p>CR - Converted Real Mode</p>
<p>CT - Converted Test Mode</p>
<p>E – Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p></td>
<td><p>This is the status field of the conversion log. There are five set of codes:</p>
<p>CR - Converted Real Mode</p>
<p>CT - Converted Test Mode   </p>
<p>E - Error</p>
<p>S - Skipped</p>
<p>R - Ready to Convert</p></td>
</tr>
</tbody>
</table>

|                      |            |           |                                                                                                                                                                                   |
|----------------------|------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New TIU Document IEN | 703.92,.03 | Free Text | This field contains a pointer to the TIU Document file (#8925). (Reference IA \#4796). This will hold the internal entry number of the document of the converted medicine report. |
| Lines                | 703.92,.04 | Number    | This field contains the line count of the Medicine report that was converted.                                                                                                     |
| Bytes                | 703.92,.05 | Number    | This field contains the number of bytes of the Medicine report that was converted.                                                                                                |
| Error Msg            | 703.92,.1  | Free Text | This field stores the error message during the conversion of the Medicine report.                                                                                                 |

[^6]Hemodialysis Access Points File - \#704.201

This new file contains information on access points used by the Hemodialysis application.

|                   |                  |                              |                                                                                                            |
|-------------------|------------------|------------------------------|------------------------------------------------------------------------------------------------------------|
| Field Name    | Field Number | Format                   | Description                                                                                            |
| Patient_ID        | 704.201,.01      | Pointer to patient file (#2) | This field contains the patient DFN. (Required)                                                            |
| Access Points     | 704.201,.1       | Word Processing              | This field holds the XML in UUEncoded format for this patient’s access points for dialysis treatments.     |
| Access History    | 704.201,.2       | Word Processing              | This field holds the XML in UUEncoded format for this patient’s access history for dialysis treatments.    |
| Infection History | 704.201,.3       | Word Processing              | This field holds the XML in UUEncoded format for this patient’s infection history for dialysis treatments. |

[^7]Hemodialysis Study File - \#704.202

This new file contains information on hemodialysis studies used by the Hemodialysis application.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>ID</td>
<td>704.202,.01</td>
<td>Pointer to CP Transaction file (#702)</td>
<td>This field contains the IEN of the CP STUDY (File #702) for this dialysis treatment. (Required)</td>
</tr>
<tr class="odd">
<td>Patient</td>
<td>704.202,.02</td>
<td>Pointer to Patient file (#2)</td>
<td>Pointer to the PATIENT (File #2) of the patient for this dialysis treatment.</td>
</tr>
<tr class="even">
<td>Study_DateTime</td>
<td>704.202,.03</td>
<td>Computed date</td>
<td>Computed field used to allow automated XML creation with appropriate tag/value pairs.</td>
</tr>
<tr class="odd">
<td>Study_Location</td>
<td>704.202,.04</td>
<td>Computed</td>
<td>Computed field used to allow automated XML creation with appropriate tag/value pairs.</td>
</tr>
<tr class="even">
<td>Status</td>
<td>704.202,.09</td>
<td><p>Set:</p>
<p>0 - Closed</p>
<p>1 - Active</p></td>
<td>Contains the status of this procedure.</td>
</tr>
<tr class="odd">
<td>Study Data</td>
<td>704.202,.1</td>
<td>Word Processing</td>
<td>Contains the study data XML document in UUEncoded format.</td>
</tr>
<tr class="even">
<td>Summary</td>
<td>704.202,.2</td>
<td>Word Processing</td>
<td>Contains the summary data XML document in UUEncoded format.</td>
</tr>
<tr class="odd">
<td>Flowsheet</td>
<td>704.202,.3</td>
<td>Word Processing</td>
<td>Contains the flowsheet data XML document in UUEncoded format.</td>
</tr>
<tr class="even">
<td>Med Log</td>
<td>704.202,.4</td>
<td>Word Processing</td>
<td>Contains the med log data XML document in UUEncoded format.</td>
</tr>
<tr class="odd">
<td>Note List</td>
<td>704.202,.5</td>
<td>Word Processing</td>
<td>This field contains the Note List data XML document in UUEncoded format.</td>
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

[^8]Hemodialysis Setting File - \#704.209

This new file contains information on hemodialysis settings used by the Hemodialysis application.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Field Number</strong></td>
<td><strong>Format</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Setting Name</td>
<td>704.209,.01</td>
<td>Free Text 3-30 characters in length. Not numeric or starting with punctuation.</td>
<td>Contains the descriptive name of the data contained in this setting.</td>
</tr>
<tr class="odd">
<td>Owner</td>
<td>704.209,.02</td>
<td>Pointer to new person file (#200)</td>
<td>If this setting is user specific, this field will contain that user’s DUZ.</td>
</tr>
<tr class="even">
<td>User</td>
<td>704.209,.03</td>
<td>Pointer to new person file (#200)</td>
<td>This field displays the user name that is locking the Hemodialysis setting option.</td>
</tr>
<tr class="odd">
<td>Date/Time of Lock</td>
<td>704.209,.04</td>
<td>Input transform:<br />
S %DT="ET" D ^%DT S X=Y K:Y&lt;1 X</td>
<td>This field will store the date and time of when the Hemodialysis setting option was locked for use.</td>
</tr>
<tr class="even">
<td>Process ID</td>
<td>704.209,.05</td>
<td><p>Free text 3-40 characters in length.</p>
<p>Input transform:<br />
K:$L(X)&gt;40!($L(X)&lt;3) X</p></td>
<td>This field will store the JOB ID of the process that is locking the Hemodialysis setting option.</td>
</tr>
<tr class="odd">
<td>XML Document</td>
<td>704.209,.1</td>
<td>Word Processing</td>
<td>Contains the XML document for this setting in UUEncoded format.</td>
</tr>
</tbody>
</table>

## Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

702 CP TRANSACTION YES YES NO

[^9]702.001 CP_TRANSACTION_TIU_HISTORY YES YES NO

702.01 CP DEFINITION YES YES NO

702.09 CP INSTRUMENT YES YES YES ADD NO NO

703.1 CP RESULT REPORT YES YES NO

[^10]703.9 CP CONVERSION YES YES NO

[^11]704.201 HEMODIALYSIS ACCESS POINTS YES YES NO

704.202 HEMODIALYSIS STUDY YES YES NO

704.209 HEMODIALYSIS SETTINGS YES YES NO

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Delphi Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Procedures uses RPC Broker and custom Delphi Components in the display and navigation of screens. Below is a list of the Delphi components this application currently uses along with a short description.

TMDRecordSource = class(TComponent)

This is the primary component that all others interact with. This component represents a record within FileMan via the Data Dictionary Number and the IEN. In the event that the record is a sub-file then this component will point to another TMDRecordSource that represents the parent record of the sub-record. There is no limit to the number of sub-records that can be linked together.

TMDEdit = Class(TEdit)

This component is designed to manage FileMan Free-Text and Numeric type fields. Other types may be used here with the exception of word-processing but they will require exact data input (i.e. non-ambiguous entries must be entered in the case of pointers or set of codes types). All input and output transforms are applied to the field on validation.

TMDEditPointer = Class(TComboBox)

This component is designed to manage FileMan Pointer types. This component currently handles screens via hard coded screens on the server side in routine MDRPCOR.

TMDLabel = Class(TLabel)

This component is a static component that can display one of three data elements for a FileMan field. These are 1) Data value 2) Field Title or 3) Field Help Text. There is no server update associated with this component.

TMDMemo = Class(TMemo)

This component manages FileMan word-processing data types only. It will validate the data upon leaving the component.

TMDComboBox = Class(TComboBox)

This component was designed for either set of codes or pointer type fields. If using a pointer type field the developer must be aware that the entire pointed to file will be retrieved so large files such as the Patient file (#2) is not possible to represent with this component. Files such as the State file (#5) are handled quite well if there are approximately 100 or less entries and the pointed to file does not have complex output transforms on the .01 field.

TMDRadioGroup = Class(TRadioGroup)

This field was designed specifically for the FileMan set of codes field. It loads the appropriate codes into the radio group and displays the ‘Stands For’ portion of the codes while storing to the database the internal value of the code.

TMDCheckBox = Class(TCheckBox)

This component was designed for a set of codes that are restricted to only two codes (i.e. Yes/No, True/False, On/Off).

## Remote Procedure Calls (RPC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: MD GATEWAY TAG: RPC

ROUTINE: MDRPCOG RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

NAME: MD TMDOUTPUT TAG: RPC

ROUTINE: MDRPCOO RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

DESCRIPTION:

Manages the output of VistA data to the client via the default HFS device.

INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Currently set to EXECUTE as the only option.

INPUT PARAMETER: RTN PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Contains the routine to produce the output. Currently to client produces

this parameter in the form of TAG^ROUTINE(needed parameters) to simplify

the calling process.

RETURN PARAMETER DESCRIPTION:

Text of the requested report.

NAME: MD TMDPARAMETER TAG: RPC

ROUTINE: MDRPCOV RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

DESCRIPTION:

Used to set/retrieve/modify parameters in the Kernel ToolKit PARAMETERS

(XPAR) files.

RPC is called as follows:

Param\[0\] := OPTION

Param\[1\] := Entity

Param\[2\] := Parameter name

Param\[3\] := Instance

Param\[4\] := Value

INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Contains the option for the RPC. RPC is called as shown:

Options and other required parameters include:

ENTVAL ENT

GETPAR ENT,PAR,INST

GETLST ENT,PAR

GETWP ENT,PAR,INST

SETPAR ENT,PAR,INST,VAL

SETLST ENT,PAR,,.VAL (Uses instance 0-n)

SETWP ENT,PAR,INST,.VAL

DELPAR ENT,PAR,INST

DELLST ENT,PAR

INPUT PARAMETER: ENTITY PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 20 REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

An entity is a level at which you can define a parameter. The entities

allowed are stored in the Parameter Entity file (#8989.518). The list of

allowable entities at the time this utility was released were:

Prefix Message Points to File

PKG Package Package (9.4)

SYS System Domain (4.2)

DIV Division Institution (4)

SRV Service Service/Section (49)

LOC Location Hospital Location (44)

TEA Team Team (404.51)

CLS Class Usr Class (8930)

USR User New Person (200)

BED Room-Bed Room-Bed (405.4)

OTL Team (OE/RR) OE/RR List (101.21)

The entity may be referenced as follows:

1\) The internal variable pointer (nnn;GLO(123,)

2\) The external format of the variable pointer using the 3 character

prefix (prefix.entryname)

3\) The prefix alone to set the parameter based on current entity selected.

(prefix)

Method 3 uses the following values for the following entities:

USR Current value of DUZ

DIV Current value of DUZ(2)

SYS System (domain)

PKG Package to which the parameter belongs

INPUT PARAMETER: PAR PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: NO

SEQUENCE NUMBER: 3

DESCRIPTION:

A parameter is the actual name which values are stored under. The name of

the parameter must be namespaced and it must be unique. Parameters can be

defined to store the typical package parameter data (e.g. the default add

order screen), but they can also be used to store GUI application screen

settings a user has selected (e.g. font or window width). When a

parameter is defined, the entities, which may set that parameter, are also

defined. The definition of parameters is stored in the PARAMETER

DEFINITION file (#8989.51).

> **NOTE:** This utility restricts the parameter name to those in the Clinical

Procedures namespace (MD\*).

INPUT PARAMETER: INST PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: NO

SEQUENCE NUMBER: 4

DESCRIPTION:

Most parameters will set instance to 1. Instances are used when more than

one value may be assigned to a given entity/parameter combination. An

example of this would be lab collection times at a division. A single

division may have multiple collection times. Each collection time would

be assigned a unique instance.

INPUT PARAMETER: VAL PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 80 REQUIRED: NO

SEQUENCE NUMBER: 5

DESCRIPTION:

A value may be assigned to every parameter for the entities allowed in the

parameter definition. Values are stored in the PARAMETERS file (#8989.5).

VAL may be passed in external or internal format. If using internal

format for a pointer type parameter, VAL must be preceded with the grave

(\`) character. If VAL is being assigned to a word processing parameter,

the text is passed in the subordinate nodes of VAL (e.g. VAL(0-n)=Text).

RETURN PARAMETER DESCRIPTION:

Returns requested data from the specified option.

NAME: MD TMDPATIENT TAG: RPC

ROUTINE: MDRPCOP RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

NAME: MD TMDPROCEDURE TAG: RPC

ROUTINE: MDRPCOD RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

NAME: MD TMDRECORDID TAG: RPC

ROUTINE: MDRPCOR RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

DESCRIPTION:

General RPC for VA Fileman functions.

Param 1 is passed in as the function to perform and includes the

following:

LOOKUP: Performs very generic file lookup functionality

VALIDATE: Validates input to a fileman field and saves to FDA

DELREC: Validates ability to delete and if able deletes a record

SETFDA: Validates input and stores in FDA

SAVEFDA: Saves any data stored in FDA

CLEARFDA: Clears any data in the FDA without saving

GETDATA: Retrieves a single field value

GETCODES: Retrieves the set of codes for a field

GETLABEL: Retrieves a fields TITLE or LABEL if no Title

GETIDS: Returns required identifiers for a DD Number

GETHELP: Returns Fileman help for a field

RENAME: Validates and renames .01 field if valid

NEWREC: Creates a new record

CHANGES: Returns 0/1 if changes exist in FDA

CHKVER: Version check Client \<-\> Server

LOCK: Locks a record by DD and IENS

UNLOCK: Unlocks record locked by LOCK option

INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

See description of RPC.

INPUT PARAMETER: DDNUM PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10 REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

Contains the Data Dictionary number of the item being manipulated.

INPUT PARAMETER: IENS PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 20 REQUIRED: NO

SEQUENCE NUMBER: 3

DESCRIPTION:

Contains the IENS of the record being manipulated.

INPUT PARAMETER: FLD PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10 REQUIRED: NO

SEQUENCE NUMBER: 4

DESCRIPTION:

Contains field specifications for the record.

INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: NO

SEQUENCE NUMBER: 5

DESCRIPTION:

Contains any other needed information for the call.

RETURN PARAMETER DESCRIPTION:

Returns global array of requested data or status.

NAME: MD TMDTRANSACTION TAG: RPC

ROUTINE: MDRPCOT RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

NAME: MD TMDUSER TAG: RPC

ROUTINE: MDRPCOU RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

DESCRIPTION:

Manages the VistA interface to the TMDUser object.

Available options:

SIGNON Connects session to the server and attempts signon.

ESIG Verifies passed e-sig.

CHKVER Verifies client version is compatible with server.

INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

See RPC description.

INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 250 REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

Required data for selected option.

RETURN PARAMETER DESCRIPTION:

Returns global array of status or requested data.

NAME: MD UTILITIES TAG: RPC

ROUTINE: MDRPCU RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

[^12]NAME: MD TMDCIDC TAG: RPC

ROUTINE: MDRPCW RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

WORD WRAP ON: TRUE VERSION: 1

DESCRIPTION:

This RPC will do the following:

Input Parameter: RESULTS - (Both Input/Output) Passed in as the array to

return the results.

OPTION - (Input) PROC - obtain a list of Procedures

defined for a clinic.

DIAG - obtain a list of diagnosis

defined for a clinic.

SCDISP - Obtain the patient's service

connection and rated disability.

DFN - (Input) Patient internal entry number

MDSTUD - (Input) CP Study internal entry number

RETURN PARAMETER DESCRIPTION:

\> D RPC^MDRPCW(.RESULTS,"PROC",162,212)

\> ZW RESULTS

RESULTS=^TMP("MDRPCW",539023945)

@RESULTS@(0)=count of array element (0 if nothing found)

@RESULTS@(1)=^group header

@RESULTS@(2) = P1 := cpt or icd code / ien of other items

P2 := user defined text

P6 := user defined expanded text to send to PCE

P7 := second code or item defined for line item

P8 := third code or item defined for line item

P9 := associated clinical lexicon term

\> D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

^TMP("MDRPCW",539023945,0) = 7

^TMP("MDRPCW",539023945,1) = ^PFT PROCEDURES

^TMP("MDRPCW",539023945,2) = G0125^Lung image (PET) ^^^^^^^

^TMP("MDRPCW",539023945,3) = S9473^Pulmonary rehabilitation pro^^^^^^^

^TMP("MDRPCW",539023945,4) = S2060^Lobar lung transplantation ^^^^^^^

^TMP("MDRPCW",539023945,5) = S2060^Lobar lung transplantation ^^^^^^^

^TMP("MDRPCW",539023945,6) = A4480^Vabra aspirator ^^^^^^^

^TMP("MDRPCW",539023945,7) = 43450^DILAT ESOPH-SOUND/BOUGIE-1/M^^^^^^^

Global ^

\> D RPC^MDRPCW(.RESULTS,"DIAG",162,212)

\> D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

^TMP("MDRPCW",539023945,0) = 31

^TMP("MDRPCW",539023945,1) = ^PFT

^TMP("MDRPCW",539023945,2) = 397.1^RHEUM PULMON VALVE DIS^^^^^^^269587

^TMP("MDRPCW",539023945,3) = 417.1^PULMON ARTERY ANEURYSM^^^^^^^269688

^TMP("MDRPCW",539023945,4) = 417.8^PULMON CIRCULAT DIS NEC^^^^^^^269690

^TMP("MDRPCW",539023945,5) = 417.9^PULMON CIRCULAT DIS NOS^^^^^^^269691

^TMP("MDRPCW",539023945,6) = 424.3^PULMONARY VALVE DISORDER^^^^^^^101164

^TMP("MDRPCW",539023945,7) = 516.1^IDIO PULM HEMOSIDEROSIS^^^^^^^61083

^TMP("MDRPCW",539023945,8) = 746.01^CONG PULMON VALV ATRESIA^^^^^^^265805

^TMP("MDRPCW",539023945,9) = 673.82^PULM EMBOL NEC-DEL W P/P^^^^^^^271756

^TMP("MDRPCW",539023945,10) = 747.3^PULMONARY ARTERY ANOM^^^^^^^27406

^TMP("MDRPCW",539023945,11) = 770.3^NB PULMONARY HEMORRHAGE^^^^^^^273240

^TMP("MDRPCW",539023945,12) = 794.2^ABN PULMONARY FUNC STUDY^^^^^^^273442

^TMP("MDRPCW",539023945,13) = 901.41^INJURY PULMONARY ARTERY^^^^^901.42^^275136

^TMP("MDRPCW",539023945,14) = 162.3^MAL NEO UPPER LOBE LUNG^^^^^162.4^162.5^73534

^TMP("MDRPCW",539023945,15) = 235.7^UNC BEHAV NEO LUNG^^^^^^^267754

^TMP("MDRPCW",539023945,16) = 875.0^OPEN WOUND OF CHEST^^^^^^^274991

^TMP("MDRPCW",539023945,17) = 162.9^MAL NEO BRONCH/LUNG NOS^^^^^^^73521

^TMP("MDRPCW",539023945,18) = 786.6^CHEST SWELLING/MASS/LUMP^^^^^^^273380

^TMP("MDRPCW",539023945,19) = 518.89^OTHER DISEASE OF LUNG, NEC^^^^^^^87486

^TMP("MDRPCW",539023945,20) = ^BRONCHOSCOPY

^TMP("MDRPCW",539023945,21) = 012.20^ISOL TRACHEAL TB-UNSPEC^^^^^012.21^^266107

^TMP("MDRPCW",539023945,22) = 012.22^ISOL TRACH TB-EXAM UNKN^^^^^^^266109

^TMP("MDRPCW",539023945,23) = 012.23^ISOLAT TRACH TB-MICRO DX^^^^^^^266110

^TMP("MDRPCW",539023945,24) = 012.24^ISOL TRACHEAL TB-CULT DX^^^^^^^266111

^TMP("MDRPCW",539023945,25) = 748.61^CONGEN BRONCHIECTASIS^^^^^^^265478

^TMP("MDRPCW",539023945,26) = 011.50^TB BRONCHIECTASIS-UNSPEC^^^^^011.51^^266056

^TMP("MDRPCW",539023945,27) = 784.1^THROAT PAIN^^^^^^^276881

^TMP("MDRPCW",539023945,28) = 784.8^HEMORRHAGE FROM THROAT^^^^^^^273371

^TMP("MDRPCW",539023945,29) = 034.0^STREP SORE THROAT^^^^^^^114610

^TMP("MDRPCW",539023945,30) = 466.11^AC. BRONCH/RESP SYNCYT V (RSV)^^^^^466.19^

^304309

^TMP("MDRPCW",539023945,31) = 530.10^ESOPHAGITIS, UNSP.^^^^^^^295809

Global ^

\> D RPC^MDRPCW(.RESULTS,"SCDISP",17,212)

@RESULTS@(n)="Lines of text"

\> D ^%G

Global ^TMP("MDRPCW",\$J

TMP("MDRPCW",\$J

^TMP("MDRPCW",539023945,1) = Service Connected: 50%

^TMP("MDRPCW",539023945,2) = Rated Disabilities: NONE STATED

Global ^

NAME: MD TMDENCOUNTER TAG: GETENC

ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

DESCRIPTION:

This remote procedure will return the existing data in an encounter.

INPUT PARAMETER: STUDY PARAMETER TYPE: REFERENCE

REQUIRED: YES SEQUENCE NUMBER: 1

DESCRIPTION:

This is the CP Study internal entry number.

RETURN PARAMETER DESCRIPTION:

The result is returned in ^TMP("MDENC",\$J) global.

^TMP("MDENC",\$J,1)="SC";0/1^0/1;"AO";0/1^0/1;"IR";0/1^0/1;"EC";0/1^0/

1;"MST";0/1^0/1;"HNC";0/1^0/1;"CV";0/1^0/1

P1 = "SC" - Service Connected

P2 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P3 = "AO" - Agent Orange Exposure

P4 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P5 = "IR" - Ionizing Radiation Exposure

P6 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P7 = "EC" - Environmental Contaminants

P8 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P9 = "HNC" - Head and/or Neck Cancer

P10 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P11 = "MST" - Military Sexual Trauma

P12 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

P13 = "CV" - Combat Veteran

P14 = first "^" piece 1 if the condition can be answered

0 if the condition should be null not asked

second "^" piece - If Scheduling has the answer, 1 = yes 0 = no

^TMP("MDENC",\$J,n)="PRV"^CODE^^NARR^^Primary (1=Yes,0=No)

P1 = "PRV"- Provider segment

P2 = CODE - New Person internal Entry Number

P3 = Null

P4 = NARR - Provider name

P5 = Null

P6 = Primary - 1/0/null (1=Yes,0/Null=No)

="POV"^ICD IEN^ICD CODE^provider narrative category^

provider narrative (Short Description)^Primary (1=Yes,0/Null=No)

P1 = "POV" - ICD segment

P2 = ICD internal entry number

P3 = ICD Code<span id="icd10" class="anchor"></span>

P4 = Provider Narrative Category

P5 = Short Description

P6 = Primary - 1/0/null (1=Yes,0/Null=No)

="CPT"^CPT IEN^CPT CODE^provider narrative category^

provider narrative (Short Description)^^Quantity

P1 = "CPT" - CPT segment

P2 = CPT internal entry number

P3 = CPT Code

P4 = Provider Narrative Category (CPT Category Grouping)

P5 = Short Description

P6 = null

P7 = Quantity

NAME: MD TMDLEX TAG: LEX

ROUTINE: MDRPCW1 RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

DESCRIPTION:

This RPC will return a list of CPT or ICD for a search typed in.

INPUT PARAMETER: MDSRCH PARAMETER TYPE: REFERENCE

REQUIRED: YES SEQUENCE NUMBER: 1

DESCRIPTION:

This is the text typed in for the look-up.

INPUT PARAMETER: MDAPP PARAMETER TYPE: REFERENCE

REQUIRED: YES SEQUENCE NUMBER: 2

DESCRIPTION:

This is the application indicator. It is either "CPT" or "ICD".

RETURN PARAMETER DESCRIPTION:

^TMP("MDLEX",\$J,#)=P1 - CPT/ICD Code

P2 - Internal Entry Number

P3 - Lexicon text

\>D LEX^MDRPCW1(.RESULTS,"BORE","CPT")

\>ZW RESULTS

RESULTS="^TMP("MDLEX",539152953)"

\>D ^%G

Global ^TMP("MDLEX",\$J -- NOTE: translation in effect

^TMP("MDLEX",539152953,1)=86618^302213^Borella Burgdorferi (Lyme Disease)

Antibody (CP T-4 86618)

NAME: MD TMDNOTE TAG: RPC

ROUTINE: MDRPCNT RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

WORD WRAP ON: TRUE VERSION: 1

DESCRIPTION:

This remote procedure call does the following:

Accepts the following Inputs:

RESULTS - Both (Input and Output) - Passed in as the array to return

results in.

OPTION - NEWDOC = Add additional new document to the Hemodialysis

study.

NOTELIST = Returns a list of documents associated with the

study. The pieces returned are: Note IEN, Note

title, Date/Time Creation, Author, and Hospital

Location.

VIEWTIU = Return the text lines of a document from NOTELST.

MDSID - Study internal Entry Number.

MDTIU - TIU Document Internal Entry Number.

MDDTE - Date/Time of Document Creation.

MDAUTH - Author of document.

MDESIG - Encrypted Electronic Signature.

MDTXT - Text of the new document in an array.

Return Results are the following:

OPTION = NEWDOC

\> D RPC^MDRPCNT(.RESULTS,"NEWDOC",904,"",3050524.0915,679,74RHLld;flk,MDTXT)

\> D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

^TMP("MDKUTL",538992716,0) = Note internal entry number or -1^Error Message

OPTION = NOTELIST

\> D RPC^MDRPCNT(.RESULTS,"NOTELST",476)

\> D ^%G

Global ^TMP("MDKUTL",\$J

TMP("MDKUTL",\$J

^TMP("MDKUTL",538992716,1) = 968^PROCEDURE NOTE^OCT 10, 2001@17:08:36

^MDPROVIDER,ONE ^PROSTHETICS

^TMP("MDKUTL",538992716,2) = 969^PROCEDURE NOTE^OCT 10, 2001@17:10:44^^PROSTHET

I

CS

^TMP("MDKUTL",538992716,3) = 970^PROCEDURE NOTE^OCT 10, 2001@17:11:50^^PROSTHET

I

CS

^TMP("MDKUTL",538992716,4) = 971^PROCEDURE NOTE^OCT 10, 2001@17:15:45^^PROSTHET

I

CS

^TMP("MDKUTL",538992716,5) = 972^PROCEDURE NOTE^OCT 10, 2001@17:16:34^^PROSTHET

I

CS

^TMP("MDKUTL",538992716,6) = 974^PROCEDURE NOTE^OCT 11, 2001@10:56:03^^PROSTHET

I

CS

^TMP("MDKUTL",538992716,7) = 975^PROCEDURE NOTE^OCT 11, 2001@12:50:29^^PROSTHET

I

CS

Global ^

OPTION = VIEWTIU

\> D RPC^MDRPCNT(.RESULTS,"VIEWTIU",476,968)

\> D ^%G

Global ^TMP("TIUVIEW",\$J

TMP("TIUVIEW",\$J

^TMP("TIUVIEW",538992716,1) = TITLE: PROCEDURE NOTE

^TMP("TIUVIEW",538992716,2) = DATE OF NOTE: OCT 10, 2001@17:08:36 ENTRY DATE:

O

CT 10, 2001@17:08:36

^TMP("TIUVIEW",538992716,3) = AUTHOR: MDPROVIDER,ONE EXP COSIGNER:

^TMP("TIUVIEW",538992716,4) = URGENCY: STATUS:

C

OMPLETED

^TMP("TIUVIEW",538992716,5) =

^TMP("TIUVIEW",538992716,6) = PROCEDURE SUMMARY CODE: Abnormal

^TMP("TIUVIEW",538992716,7) = DATE/TIME PERFORMED: OCT 15, 2001

^TMP("TIUVIEW",538992716,8) =

^TMP("TIUVIEW",538992716,9) = \*\*\* PROCEDURE NOTE Has ADDENDA \*\*\*

^TMP("TIUVIEW",538992716,10) =

^TMP("TIUVIEW",538992716,11) = Complete consult 1104. 6 attached images.

^TMP("TIUVIEW",538992716,12) =

^TMP("TIUVIEW",538992716,13) = /es/ MDPROVIDER,ONE

^TMP("TIUVIEW",538992716,14) =

^TMP("TIUVIEW",538992716,15) = Signed: 10/15/2001 13:02

^TMP("TIUVIEW",538992716,16) =

^TMP("TIUVIEW",538992716,17) = 10/15/2001 ADDENDUM STATUS:

COMPLETED

^TMP("TIUVIEW",538992716,18) = aDDENDUM LA LA

^TMP("TIUVIEW",538992716,19) = LA LA LA

^TMP("TIUVIEW",538992716,20) =

^TMP("TIUVIEW",538992716,21) = /es/ MDPROVIDER,ONE

^TMP("TIUVIEW",538992716,22) =

^TMP("TIUVIEW",538992716,23) = Signed: 10/15/2001 13:04

NAME: MD TMDSUBMITU TAG: RPC

ROUTINE: MDRPCOWU RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

NAME: MD TMDWIDGET TAG: RPC

ROUTINE: MDRPCOW RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

VERSION: 1

NAME: MDK GET VISTA DATA TAG: RPC

ROUTINE: MDKRPC1 RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED INACTIVE: ACTIVE

INPUT PARAMETER: OPTION PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 8 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

This is the routine tag that will be called to retrieve the data.

INPUT PARAMETER: DATA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 50 REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

This is whatever data is needed by the subroutine to process the request

for data. In many cases it will be a single value (e.g., patient id -

DFN).

RETURN PARAMETER DESCRIPTION:

Returns an array.

RESULT(0)=number or

RESULT(0)=-1^error message

RESULT(1)=data

RESULT(n)=data

If data is not found, RESULT(0) will be contain a "-1" in the first piece

and an error message in the second piece.

If data is found, RESULT(0) will contain a number that indicates how many

entries are returned.

RESULT(1) through RESULT(n) will contain the data that is found.

NAME: MDK GET/SET RENAL DATA TAG: RPC

ROUTINE: MDKRPC2 RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

NAME: MDK UTILITY TAG: RPC

ROUTINE: MDKUTLR RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: TRUE

## Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: MD ALLOW EXTERNAL ATTACHMENTS

DISPLAY TEXT: Allow non-instrument attachments

MULTIPLE VALUED: No VALUE TERM: Allowed

VALUE DATA TYPE: yes/no

DESCRIPTION:

Set this value to Yes to allow users of CPUser.exe to attach documents to

the transaction that are not created by an instrument.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^13]NAME: MD APPOINT END DATE

DISPLAY TEXT: End Date for Encounter Appointments

MULTIPLE VALUED: No VALUE TERM: Days

VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

VALUE HELP: Enter a number from 0 to 365.

DESCRIPTION:

Enter a number from 0 to 365 for the number of days that will be

used to add to today as the end date range of the Encounter

Appointments. If no value is entered, the default value used

will be 0.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD APPOINT START DATE

DISPLAY TEXT: Start Date for Encounter Appointments

MULTIPLE VALUED: No VALUE TERM: Days

VALUE DATA TYPE: numeric VALUE DOMAIN: 0:365

VALUE HELP: Enter a number from 0 to 365.

DESCRIPTION:

Enter a number from 0 to 365 for the number of days that will be

used to subtract from today as the start date range of the Encounter

Appointments. If no value is entered, the default value used

will be 200.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD COMPL PROC DISPLAY DAYS

DISPLAY TEXT: Completed Proc Display Days

MULTIPLE VALUED: No VALUE TERM: Days

VALUE DATA TYPE: numeric VALUE DOMAIN: 1:365

VALUE HELP: Enter the number of days from 1 to 365

DESCRIPTION:

The number of days the completed procedure requests will be

displayed in the CP Check-in screen.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^14]NAME: MDCHECK-IN PROCEDURE LIST DISPLAY TEXT: Check-in Procedure List

MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

VALUE TERM: Schedule Appointment? VALUE DATA TYPE: set of codes

VALUE DOMAIN: 0:None;1:Outpatient;2:Inpatient;3:Both

VALUE HELP: Enter 0 for None, 1 for Outpatient, 2 for Inpatient, or 3 for both.

INSTANCE DATA TYPE: pointer

INSTANCE DOMAIN: 702.01

INSTANCE HELP: Enter procedures that needs the study to be auto checked-in.

INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0

DESCRIPTION:

This parameter contains a list of procedures that will be used

to auto check-in the CP studies during the procedures request in CPRS

and whether appointments are scheduled for the procedure.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD CLINIC QUICK LIST DISPLAY TEXT: Clinic Quick List For CP

MULTIPLE VALUED: Yes INSTANCE TERM: Clinic

VALUE TERM: Procedure VALUE DATA TYPE: pointer

VALUE DOMAIN: 702.01

VALUE HELP: Select a procedure for the clinic.

INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 44

INSTANCE HELP: Enter clinics that need CP studies to be checked-in.

DESCRIPTION:

List of clinics used as a source to get a list of patients

that need to have CP studies checked-in. This only applies

to studies with procedures that have multiple results such

as Hemodialysis, Respiratory Therapy, and sleep studies.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD CLINICS WITH MULT PROC

DISPLAY TEXT: Clinics With Multiple Procedures

MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

VALUE TERM: Clinic VALUE DATA TYPE: pointer

VALUE DOMAIN: 44

VALUE HELP: Enter a clinic for the procedure.

INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

INSTANCE HELP: Enter a procedure.

INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",9)\>0

DESCRIPTION:

If you have a clinic for multiple procedures, populate this

parameter with the procedure and associate it to a clinic.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^15]NAME: MD CLINIC ASSOCIATION DISPLAY TEXT: MD Clinic Association

MULTIPLE VALUED: Yes INSTANCE TERM: Sequence

VALUE TERM: Clinic;Procedure Association Value

PROHIBIT EDITING: No VALUE DATA TYPE: free text

INSTANCE DATA TYPE: numeric INSTANCE DOMAIN: 1:9999

INSTANCE HELP: Enter the sequence to associate a clinic and procedure.

DESCRIPTION:

This parameter is used to identify the clinic and procedure

association. Each item should be entered with the following format

Clinic internal entry number\_";"\_Procedure internal entry number

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD CRC BYPASS DISPLAY TEXT: Bypass CRC Checking

MULTIPLE VALUED: No VALUE TERM: Bypass CRC Checking

VALUE DATA TYPE: yes/no

DESCRIPTION:

Set this value to 'Yes' to prevent the client application from verifying

its CRC Value at startup.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD CRC VALUES

DISPLAY TEXT: Clinical Procedures CRC Values

MULTIPLE VALUED: Yes

INSTANCE TERM: Executable or Library Name

VALUE TERM: CRC Value PROHIBIT EDITING: No

VALUE DATA TYPE: free text VALUE DOMAIN: 1:15

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

DESCRIPTION:

This parameter is used to store the CRC values for the most recent

versions of executable and libraries. Use the Tools menu on the CPManager

program to calculate the needed CRC Values of the current versions.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD DAYS FOR INSTRUMENT DATA

DISPLAY TEXT: Temporary instrument data life (Days)

MULTIPLE VALUED: No VALUE TERM: Days

PROHIBIT EDITING: No VALUE DATA TYPE: numeric

VALUE DOMAIN: 0:365

DESCRIPTION:

The number of days to keep data from the auto-instruments after

the data has been associated with a Clinical Procedures report.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^16]NAME: MD DAYS TO RETAIN COM STUDY

DISPLAY TEXT: Days to Retain Completed Study

MULTIPLE VALUED: No VALUE TERM: Days

PROHIBIT EDITING: No VALUE DATA TYPE: numeric

VALUE DOMAIN: 1:365

VALUE HELP: Enter the number of days from 1 to 365

DESCRIPTION:

The number of days after check-in date/time to display the study

that has been complete in the CPUser application. Studies that have

procedures with multiple or cumulative results are NOT included.

Cumulative and multiple results studies will have a default value of

365\.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^17]NAME: MD DAYS TO RET COM MULT

DISPLAY TEXT: Days to Retain Completed Multiple Study

MULTIPLE VALUED: No VALUE TERM: Days

VALUE DATA TYPE: numeric VALUE DOMAIN: 1:365

VALUE HELP: Enter the number of days from 1 to 365

DESCRIPTION:

The number of days after check-in date/time to display the study

that has been completed in the CPUser application. This only

pertains to studies that have procedures with multiple studies.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD DEVICE SURVEY TRANSMISSION DISPLAY TEXT: Device Survey Transmission

MULTIPLE VALUED: No VALUE TERM: Yes/No

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

VALUE HELP: Enter 'Y' for 'YES' or 'N' for 'NO'.

DESCRIPTION:

Used to determine if the site wants to transmit the device survey to

Hines. Enter 'Y' for 'YES' to send the survey or 'N' for 'NO' to

suppress the transmission.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD FILE EXTENSIONS DISPLAY TEXT: Imaging File Types

MULTIPLE VALUED: Yes INSTANCE TERM: Extension

VALUE TERM: File type PROHIBIT EDITING: No

VALUE DATA TYPE: free text VALUE DOMAIN: 1:80

VALUE HELP: Enter a description of this file type

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 2:10

INSTANCE HELP: Enter the extension of the file type with a '.'

INSTANCE VALIDATION CODE: K:X'?1".".9ULN X

DESCRIPTION:

This parameter stores a list of valid file types and the associated

extensions of these files.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD GATEWAY DISPLAY TEXT: CP Gateway Parameters

MULTIPLE VALUED: Yes INSTANCE TERM: Parameter Name

VALUE TERM: Parameter Value VALUE DATA TYPE: free text

VALUE DOMAIN: 1:255 INSTANCE DATA TYPE: free text

INSTANCE DOMAIN: 1:255

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^18]NAME: MD GET HIGH VOLUME DISPLAY TEXT: Get High Volume

MULTIPLE VALUED: Yes INSTANCE TERM: Procedure

VALUE TERM: Get String VALUE DATA TYPE: free text

INSTANCE DATA TYPE: pointer INSTANCE DOMAIN: 702.01

INSTANCE HELP: Enter a high volume procedure.

INSTANCE SCREEN CODE: I +\$P(^MDS(702.01,+Y,0),"^",6)'=2&(+\$P(^MDS(702.01,+Y,0)

,"^",11)'=2)&(\$P(^MDS(702.01,+Y,0),"^",9)\>0)

DESCRIPTION:

This parameter will contain a free text string that contains two pieces

of data delimited by a semicolon ';'. The two pieces of data are: 1)

1/0 (Yes/No) to indicate whether or not the text of the result should be

added to the note, 2) 1/0 (Yes/No) to enter the text of the result as the

significant finding of the Consult. (If you enter a 0, the note will be

auto closed with the text inside.)

Example string: 1;0

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD HFS SCRATCH

DISPLAY TEXT: VistA Scratch HFS Directory

MULTIPLE VALUED: No VALUE TERM: Directory name

VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

VALUE HELP: Enter in an OS level directory

DESCRIPTION:

Contains the directory specification for the Kernel OPEN^%ZISH call. This

directory should be accessible for read/write operations by all CP users.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD IMAGING XFER DISPLAY TEXT: Imaging Network Share

MULTIPLE VALUED: No VALUE TERM: Imaging Network Share

VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

DESCRIPTION:

This parameter contains the name of a network server, share, and path

(UNC) to a location where Clinical Procedures can put files for pick-up by

the Imaging background processor for archiving.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^19] NAME: MDK APPLICATION INSTALL DISPLAY TEXT: MDK Application Install

MULTIPLE VALUED: Yes

INSTANCE TERM: Installation Distribution Info

VALUE TERM: Distribution Info Value PROHIBIT EDITING: No

VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

DESCRIPTION:

This parameter is used to store the Hemodialysis application

distribution information. The information includes the following:

1\) Date/Time when application first launched.

2\) User Name

3\) System Option Loaded (Y/N)

4\) Workstation of where the application was launched.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MDK GUI VERSION

DISPLAY TEXT: Hemodialysis Version Compatibility

MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version

VALUE TERM: Compatible with current server version

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:40

DESCRIPTION:

This parameter is used to store the application:versions that are compatible

with the current server version of Hemodialysis. Instance format

of APPLICATION:VERSION (example: HEMODIALYSIS.EXE:0.0.0.0).

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^20]NAME: MD MEDICINE CONVERTED DISPLAY TEXT: Medicine Package Converted

MULTIPLE VALUED: No VALUE TERM: Yes/No

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

DESCRIPTION:

Used to determine if the Medicine Package has been converted.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^21]NAME: MD NOT ADMN CLOSE MUSE NOTE DISPLAY TEXT: NOT ADMN Close Muse Note

MULTIPLE VALUED: No VALUE TERM: Yes/No

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

DESCRIPTION:

This parameter is used to indicate the note should not be

administratively closed with the proxy user CLINICAL, DEVICE PROXY

SERVICE but the interpreter of the procedure for the MUSE device.

The default is "No".

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD OFFLINE MESSAGE DISPLAY TEXT: Offline message

MULTIPLE VALUED: No VALUE TERM: Offline Message

VALUE DATA TYPE: word processing

DESCRIPTION:

This parameter contains a message to display to the users when the Clinical

Procedures application is offline.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^22]NAME: MD OLYMPUS 7 DISPLAY TEXT: MD OLYMPUS 7

MULTIPLE VALUED: No VALUE TERM: Yes/No

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

VALUE HELP: Enter Yes/No whether you have Olympus version 7.3.7.

DESCRIPTION:

This parameter definition indicates whether the Olympus device

is version 7.3.7. The value is Yes/No. The default value

is "No".

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD ONLINE

DISPLAY TEXT: Clinical Procedure Online/Offline

MULTIPLE VALUED: No

VALUE TERM: Is Clinical Procedures Online

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

VALUE HELP: Enter 'Yes' to allow access to CP

DESCRIPTION:

This parameter controls access to the Clinical Procedures package.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^23]NAME: MD USE APPOINTMENT DISPLAY TEXT: Use Appointment Location

MULTIPLE VALUED: No VALUE TERM: Use Appointment location

VALUE DATA TYPE: yes/no

DESCRIPTION:

Set this value to Yes to allow CPUser to use the location of the

appointment selected during CP study check-in for the workload.

Otherwise, the hospital location of the CP Definition will be used.

If no value is entered, the default value is No.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^24]NAME: MDUSE APPT WITH PROCEDURE

DISPLAY TEXT: Use Appointment With Procedure

MULTIPLE VALUED: No

VALUE TERM: Use appointment with procedure

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

DESCRIPTION:

Enter "Y" or "N" for Yes/No on whether your site selects the appointment

scheduled for outpatients during the procedure request in CPRS.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

[^25]NAME: MD USE NOTE DISPLAY TEXT: Use Note

VALUE TERM: Yes/No VALUE DATA TYPE: yes/no

DESCRIPTION:

This parameter indicates that Clinical Procedures will use the note

for the text of the result instead of the Significant Finding field in

Consult.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD USER DEFAULTS DISPLAY TEXT: CP User Defaults

MULTIPLE VALUED: Yes INSTANCE TERM: Parameter setting

VALUE TERM: Parameter value PROHIBIT EDITING: No

VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:250

DESCRIPTION:

This parameter is used to store a users default parameter settings. Each

setting is defined on the client.

PRECEDENCE: 1 ENTITY FILE: USER

NAME: MD VERSION CHK DISPLAY TEXT: Version Compatibility

MULTIPLE VALUED: Yes INSTANCE TERM: Application:Version

VALUE TERM: Compatible with current server version

PROHIBIT EDITING: No VALUE DATA TYPE: yes/no

INSTANCE DATA TYPE: free text INSTANCE DOMAIN: 1:30

DESCRIPTION:

This parameter is used to store the application:versions that are compatible

with the current server version of Clinical Procedures. Instance format

of APPLICATION:VERSION (example: CPMANAGER.EXE:0.0.0.0).

PRECEDENCE: 1 ENTITY FILE: SYSTEM

NAME: MD WEBLINK

DISPLAY TEXT: Clinical Procedures Home Page

MULTIPLE VALUED: No VALUE TERM: Web Address

VALUE DATA TYPE: free text VALUE DOMAIN: 1:250

DESCRIPTION:

This parameter contains the web address for the Clinical Procedures home

page. This can be modified to a local address in the event that the pages

are downloaded to be displayed from a local server location.

PRECEDENCE: 1 ENTITY FILE: SYSTEM

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: MCAR Device Client ITEM TEXT: Instrument Device Client

TYPE: subscriber CREATOR: <span class="mark">REDACTED</span>

PACKAGE: MEDICINE

DESCRIPTION: Subscriber protocol for sending data to Vista from clinical

instruments.

TIMESTAMP: 59276,54156 RECEIVING APPLICATION: MCAR-INST

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: P LOGICAL LINK: MCAR INST

VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO

NAME: MCAR Device Server ITEM TEXT: Instrument HL7 Event Driver

TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

PACKAGE: MEDICINE

DESCRIPTION: This protocol is used by the HL7 package to send results to

Vista from various clinical instrumentation.

TIMESTAMP: 59276,54156 SENDING APPLICATION: INST-MCAR

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: P VERSION ID: 2.3

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SUBSCRIBERS: MCAR Device Client

NAME: MCAR ORM CLIENT TYPE: subscriber

CREATOR: <span class="mark">REDACTED</span>

RECEIVING APPLICATION: INST-MCAR

EVENT TYPE: O02 RESPONSE MESSAGE TYPE: ORR

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO ROUTING LOGIC: Q

NAME: MCAR ORM SERVER

ITEM TEXT: Clinical Procedures ORM Protocol Server

TYPE: event driver CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP: 59276,54156 SENDING APPLICATION: MCAR-INST

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.3

SUBSCRIBERS: MCAR ORM CLIENT

[^26]NAME: MD RECEIVE GMRC

ITEM TEXT: Clinical Procedures receives messages from Consult

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This protocol receives messages from Consult. (IA 3140)

ENTRY ACTION: D EN^MDWORC(.XQORMSG) TIMESTAMP: 60934,38793

NAME: MD RECEIVE OR

ITEM TEXT: Clinical Procedures receives order msgs from CPRS

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This protocol receives order messages from CPRS. (IA 3135)

ENTRY ACTION: D EN^MDWOR(.XQORMSG) TIMESTAMP: 60934,38793

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVE

COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

NAME: MCAR-INST ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VISTA MAIL GROUP: POSTMASTER

COUNTRY CODE: USA HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

## HL Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NODE: MCAR INST LLP TYPE: TCP

DEVICE TYPE: Single-threaded Server STATE: Reading

AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:46:17

TASK NUMBER: 526320 SHUTDOWN LLP ?: NO

QUEUE SIZE: 100

RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

TCP/IP PORT: 9026 TCP/IP SERVICE TYPE: SINGLE LISTENER

PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

IN QUEUE BACK POINTER: 331 IN QUEUE FRONT POINTER: 331

OUT QUEUE BACK POINTER: 220 OUT QUEUE FRONT POINTER: 210

NODE: MCAR OUT LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client STATE: Openfail

AUTOSTART: Enabled TIME STARTED: MAR 04, 2004@06:45:47

TASK NUMBER: 529066 SHUTDOWN LLP ?: NO

QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

READ TIMEOUT: 60 ACK TIMEOUT: 60

EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: 10.3.17.157

TCP/IP PORT: 9028 TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: NO STARTUP NODE: DEV:ISC4A1

IN QUEUE BACK POINTER: 202 IN QUEUE FRONT POINTER: 202

OUT QUEUE BACK POINTER: 206 OUT QUEUE FRONT POINTER: 202

## Menu Options by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: MD GUI USER MENU TEXT: MD GUI USER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 59331,44145

RPC: MD TMDOUTPUT

RPC: MD TMDPARAMETER

RPC: MD TMDPATIENT

RPC: MD TMDPROCEDURE

RPC: MD TMDRECORDID

RPC: MD TMDTRANSACTION

RPC: MD TMDUSER

RPC: MD UTILITIES

UPPERCASE MENU TEXT: MD GUI USER

NAME: MD GUI MANAGER MENU TEXT: MD GUI MANAGER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 59385,45622

RPC: MD TMDOUTPUT

RPC: MD TMDPARAMETER

RPC: MD TMDPATIENT

RPC: MD TMDPROCEDURE

RPC: MD TMDRECORDID

RPC: MD TMDTRANSACTION

RPC: MD TMDUSER

RPC: MD UTILITIES

RPC: MD GATEWAY

UPPERCASE MENU TEXT: MD GUI MANAGER

[^27]NAME: MD AUTO CHECK-IN SETUP MENU TEXT: Auto Study Check-In Setup

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is used to populate the XPAR parameters MD USE APPT WITH PROCEDURE, MD CHECK-IN PROCEDURE LIST, MD CLINIC QUICK LIST, and MD

CLINICS WITH MULT PROC. The four XPAR parameters are used for the auto study

check-in. Users can use the option to indicate whether their site use and

schedule appointments. They can populate a list of procedures and associated

clinics that need a CP study checked-in.

ROUTINE: EN1^MDWSETUP

UPPERCASE MENU TEXT: AUTO STUDY CHECK-IN SETUP

NAME: MD SCHEDULED STUDIES MENU TEXT: Scheduled Studies

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It will process the HL7

messages that need to be sent to the device on a daily basis for CP studies.

ROUTINE: EN1^MDWORSR SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: SCHEDULED STUDIES

NAME: MD STUDY CHECK-IN MENU TEXT: Study Check-in

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It checks-in CP studies

for procedures that require multiple encounters such as Hemodialysis,

Respiratory Therapy, and Sleep Studies.

ROUTINE: CLINICPT^MDWORSR SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: STUDY CHECK-IN

[^28] NAME: MD HIGH VOLUME PROCEDURE SETUP MENU TEXT: High Volume Procedure Setup

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option will populate the XPAR Parameters MD GET HIGH

VOLUME and MD NOT ADMN CLOSE MUSE NOTE. It will let the user populate a list

of Clinical Procedures procedures set it up for high volume procedure process.

ROUTINE: EN1^MDARSET

UPPERCASE MENU TEXT: HIGH VOLUME PROCEDURE SETUP

NAME: MD PROC W/INCOMPLETE WORKLOAD

MENU TEXT: Print list of Procedure with incomplete workload

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option prints a list of procedures that has incomplete

workload for the visit.

ROUTINE: E1^MDSTUDW

UPPERCASE MENU TEXT: PRINT LIST OF PROCEDURE WITH I

NAME: MD PROCESS RESULTS MENU TEXT: MD Process Results

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

DESCRIPTION: This task is ran daily for every hour to process results

and update Consults package.

ENTRY ACTION: N ZTSAVE S ZTSAVE("DUZ")=DUZ,ZTSAVE("DUZ(")=""

ROUTINE: PROCESS^MDHL7XXX UPPERCASE MENU TEXT: MD PROCESS RESULTS

[^29]NAME: MD HEMODIALYSIS USER MENU TEXT: HEMODIALYSIS USER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 60387,39853

RPC: MDK GET VISTA DATA

RPC: MDK GET/SET RENAL DATA

RPC: MDK UTILITY

RPC: VAFCTFU CONVERT DFN TO ICN

RPC: VAFCTFU CONVERT ICN TO DFN

RPC: MD TMDWIDGET

RPC: MD TMDNOTE

RPC: MD TMDCIDC

RPC: MD TMDLEX

RPC: MD TMDENCOUNTER

RPC: GMV MANAGER

RPC: MD GATEWAY

RPC: MD TMDSUBMITU

RPC: ORWPT PTINQ

RPC: GMV PTSELECT

RPC: DG SENSITIVE RECORD ACCESS

RPC: DG SENSITIVE RECORD BULLETIN

RPC: MD TMDRECORDID

UPPERCASE MENU TEXT: HEMODIALYSIS USER

NAME: MD STUDIES LIST

MENU TEXT: Clinical Procedures Studies List

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option will generate a list of Clinical Procedures

studies.

ROUTINE: EN2^MDSTUDL

UPPERCASE MENU TEXT: CLINICAL PROCEDURES STUDIES LI

[^30]NAME: MDCVT MANAGER

  MENU TEXT: Medicine to CP Conversion Manager

  TYPE: menu                            CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This is the Medicine to CP Manager menu option.  This menu

 option consists of options to assist the site in converting the Medicine

 reports to Clinical Procedures text reports. 

ITEM: MDCVT SETUP                       SYNONYM: 1

  DISPLAY ORDER: 1

ITEM: MDCVT RUN                         SYNONYM: 3

  DISPLAY ORDER: 3

ITEM: MDCVT SUMMARY                     SYNONYM: 4

  DISPLAY ORDER: 4

ITEM: MDCVT DISK SPACE                  SYNONYM: 5

  DISPLAY ORDER: 5

ITEM: MDCVT LIST OF TIU TITLES          SYNONYM: 6

  DISPLAY ORDER: 6

ITEM: MDCVT TOTALS                      SYNONYM: 7

  DISPLAY ORDER: 7

ITEM: MDCVT ERROR LOG                   SYNONYM: 8

  DISPLAY ORDER: 8

ITEM: MDCVT CONVERSION LOCKOUT          SYNONYM: 9

  DISPLAY ORDER: 9

ITEM: MDCVT BUILD CONVERSION LIST       SYNONYM: 2

  DISPLAY ORDER: 2

  TIMESTAMP: 60459,53192                TIMESTAMP OF PRIMARY MENU: 59904,24363

  UPPERCASE MENU TEXT: MEDICINE TO CP CONVERSION MANA

NAME: MDCVT SETUP                       MENU TEXT: Conversion Setup

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES          X ACTION PRESENT: YES

 DESCRIPTION:   This option will bring up a setup screen for the site to setup

 the Medicine Report Conversion parameter setup.  This parameter setup allows

 the site to control which Medicine reports will be converted and which CP

 Definition and TIU title to link to. 

  EXIT ACTION: K DDSFILE,DR,DA          ROUTINE: SETUP^MDCVT

  UPPERCASE MENU TEXT: CONVERSION SETUP

NAME: MDCVT RUN                         MENU TEXT: Run the Conversion Process

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will start the Medicine Report conversion to

 Clinical Procedures.  This option will only convert reports for procedures

 that have the "CONVERT Y/N" field set to "Yes" under the MEDICINE FILE

 PARAMETERS in the CP CONVERSION file (#703.9). 

  ROUTINE: EN^MDCVT

  UPPERCASE MENU TEXT: RUN THE CONVERSION PROCESS

NAME: MDCVT SUMMARY                     MENU TEXT: Summary of Conversion Process

  TYPE: print                           CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will generate a Medicine Report Conversion report.

 This report consists of a listing of all Medicine records that were processed

 in the conversion in variable pointer format and the status of the conversion

 whether the record was converted, skipped, or errored.  If the record was

 converted, the total number of lines and bytes that the record was converted

 to in a TIU document will be displayed.  If the record errored, the reason why

 it errored will be displayed.  If the record was skipped, the reason why it

 was skipped will be displayed. 

  DIC {DIP}: MDD(703.9,                 L.: 0

  FLDS: \[MD CONVERSION SUMMARY\]         BY: \[MD CONVERSION SUMMARY\]

  UPPERCASE MENU TEXT: SUMMARY OF CONVERSION PROCESS

NAME: MDCVT DISK SPACE                  MENU TEXT: Disk Space Requirements

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will generate a summary of the Medicine report

 conversion.  This summary consists of a list of the files converted to

 Clinical Procedures, the count of records converted, the total lines and Bytes

 the records were converted in each file. 

  ROUTINE: SUMMARY^MDCVT

  UPPERCASE MENU TEXT: DISK SPACE REQUIREMENTS

NAME: MDCVT LIST OF TIU TITLES          MENU TEXT: List of TIU Titles Needed

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will allow the user to generate a list of Medicine

 procedures and the TIU titles needed to be created for the procedures that

 will be used for the Medicine report conversion.  The PRINT NAME of the

 procedures in the PROCEDURE/SUBSPECIALTY file (#697.2) will be used in the

 display.  This list will list the procedures and titles for a Medicine Package

 Procedure, if the "Convert Y/N" parameter is set to "Yes" and the "Use TIU

 Note Title" parameter is blank in the Conversion Setup option. 

  ROUTINE: DISP^MDSTATU

  UPPERCASE MENU TEXT: LIST OF TIU TITLES NEEDED

NAME: MDCVT TOTALS                      MENU TEXT: Conversion Totals By Status

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will verify that the Medicine reports conversion is

 complete and are in appropriate statuses. 

  ROUTINE: TOTALS^MDCVT

  UPPERCASE MENU TEXT: CONVERSION TOTALS BY STATUS

NAME: MDCVT ERROR LOG                   MENU TEXT: Error Log

  TYPE: print                           CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option generates a log of all the errors that occurred

 with each Medicine report during the conversion.  The listing consists of the

 CONVERSION ID and ERROR MESSAGE.  The CONVERSION ID consists of the record \#

 concatenated with a ";" and the global location (e.g.,"345;MCAR(699,"). 

  DIC {DIP}: MDD(703.9,                 L.: 0

  FLDS: \[MD CONVERSION ERRORS\]          BY: \[MD CONVERSION ERRORS\]

  UPPERCASE MENU TEXT: ERROR LOG

NAME: MDCVT CONVERSION LOCKOUT          MENU TEXT: Conversion Lockout

  TYPE: run routine                     CREATOR: <span class="mark">REDACTED</span>

  PACKAGE: CLINICAL PROCEDURES

 DESCRIPTION:   This option will let the user place a specialty/procedure or

 ALL specialty/procedures Enter/Edit and Report options 'OUT OF SERVICE' in the

 Medicine package.  It will also set Kernel site parameter MD MEDICINE

 CONVERTED to "YES" when all specialties/procedures enter/edit and report

 options are disabled or when the user indicated that all Medicine reports has

 been converted. 

  ROUTINE: LOCKOUT^MDCVT                UPPERCASE MENU TEXT: CONVERSION LOCKOUT

NAME: MDCVT BUILD CONVERSION LIST MENU TEXT: Build Conversion List

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES E ACTION PRESENT: YES

X ACTION PRESENT: YES

DESCRIPTION: The user will need to run this option before using the \[MDCVT

RUN\], Run the Conversion Process, option. This option will let the user build

the conversion list of the Medicine file records for the CP CONVERSION file

(#703.9). It will populate the CONVERSION LOG sub-file (#703.92) with all

entries in the "AC" cross reference in the MEDICAL PATIENT file (#690) and set

the STATUS field as "Ready to Convert" for each entry. This option can be

queued. Once the conversion list is built, this option can also be used to

add new additional entries in the Medicine file into the conversion list.

This option will not overwrite the existing entries in the CONVERSION LOG

but add to the list.

EXIT ACTION: K MDS ENTRY ACTION: S MDS=\$\$BLD^MDCVT1()

UPPERCASE MENU TEXT: BUILD CONVERSION LIST

[^31]NAME: MD PROCESS NOSHOW/CANCEL

MENU TEXT: Process No Show/Cancel Studies

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It will check for any

appointment that is No Show or Cancelled for CP studies in the "Pending

Instrument Data" status.

ROUTINE: EN1^MDWCAN

UPPERCASE MENU TEXT: PROCESS NO SHOW/CANCEL STUDIES

[^32]NAME: MD DEVICE SURVEY TRANSMISSION MENU TEXT: MD Device Survey Transmission

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option will run the device survey collection routine and

capture the data for transmission.

ROUTINE: COL^MDDEVCL

UPPERCASE MENU TEXT: MD DEVICE SURVEY TRANSMISSION

NAME: MD COORDINATOR MENU TEXT: CP Coordinator Menu

TYPE: menu

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This is the menu for the person that is the ADPAC for Clinical

Procedures. It includes all of the user interface options.

ITEM: MD AUTO CHECK-IN SETUP

ITEM: MD HIGH VOLUME PROCEDURE SETUP

ITEM: MD DICOM

ITEM: MD CARTCL

ITEM: MD UTILITIES

NAME: MD DICOM MENU TEXT: CP - DICOM Interoperability

TYPE: edit

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option improves interoperability between Clinical

Procedures and VistA Imaging CPRS Consult Request Tracking DICOM. There are

three capabilities:

First, the VistA Imaging consult accession number sss-GMR-nnnnnnnn can be

used for the Clinical Procedures Instrument Order Number.

Second, the timing of the DICOM Modality Worklist creation is changed from

order release to check-in, making it much more useful.

Third, the VistA Imaging HL7 message body can be used instead of the CP HL7

message body. (The VistA Imaging HL7 has much more information than the CP

HL7.)

> **NOTE:** This is for bidirectional CP instruments only. Also, the CP must have

an entry in the CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) to have

DICOM Modality Worklist and HL7.

DIC {DIC}: MDS(702.09, DIC(0): AEQM

DIE: MDS(702.09, DR {DIE}: .19

UPPERCASE MENU TEXT: CP - DICOM INTEROPERABILITY

NAME: MD CARTCL MENU TEXT: Keep Consult Open for CART-CL

TYPE: edit

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This Clinical Procedures Uni-directional Configuration flag

'CONSULT KEEP OPEN' provides the following functionality:

The CP procedure is automatically placed in Completed status after the HL7

message is sent, thus preventing an "inbound" HL7 message containing the

test results from being sent back to the CPRS Consult Note.

The physician can then edit the Consult Note by manually pasting in data

from a test result reporting system to complete the Consult.

This modification is beneficial for users of reporting systems-such as the

Clinical Assessment, Reporting, and Tracking System for Cardiac

Catheterization Laboratories (CART-CL) application-who do not want the test

results from the medical instrument to populate the CPRS Consult Note, but

prefer to manually paste the test results from the reporting system into

the Consult Note.

The 'CONSULT KEEP OPEN' flag must be set to Yes for this functionality to

work.

DIC {DIC}: MDS(702.09, DIC(0): AEQM

DIE: MDS(702.09, DR {DIE}: .401

UPPERCASE MENU TEXT: KEEP CONSULT OPEN FOR CART-CL

NAME: MD UTILITIES MENU TEXT: Conversion Utilities

TYPE: menu

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: Menu for the CP conversion utility options

ITEM: MD CONCONVERT SYNONYM: CO

ITEM: MD PROCONVERT SYNONYM: PR

TIMESTAMP: 64875,49164

UPPERCASE MENU TEXT: CONVERSION UTILITIES

NAME: MD CONCONVERT

MENU TEXT: Consult to Clinical Procedure conversion utility

TYPE: run routine

LOCK: MD ADMINISTRATOR PACKAGE: CLINICAL PROCEDURES

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: This utility will convert existing (non-CP) consults in a

pending status to a GMRC procedure.

EXIT ACTION: K MDOPT("CONCONVERT") ENTRY ACTION: S MDOPT("CONCONVERT")=""

ROUTINE: CONVERT^MDCONUTL

UPPERCASE MENU TEXT: CONSULT TO CLINICAL PROCEDURE

NAME: MD PROCONVERT

MENU TEXT: Procedure to Clinical Procedure conversion utility

TYPE: run routine

LOCK: MD ADMINISTRATOR PACKAGE: CLINICAL PROCEDURES

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: This utility will get all the pending, active and scheduled

procedures for the selected REQUEST SERVICE and convert them to CP.

EXIT ACTION: K MDOPT("PROCONVERT") ENTRY ACTION: S MDOPT("PROCONVERT")=""

ROUTINE: CONVERT^MDCONUTL

UPPERCASE MENU TEXT: PROCEDURE TO CLINICAL PROCEDUR

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Included in this section is the information about the cross-references of the application.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>FILE NUMBER</strong></td>
<td><strong>FIELD NUMBER</strong></td>
<td><strong>CROSS REFERENCE</strong></td>
<td><strong>DESCRIPTION</strong></td>
</tr>
<tr class="even">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>702</strong></td>
<td>.05</td>
<td>ACON</td>
<td>Used for searches when the user knows the Consult order number.</td>
</tr>
<tr class="odd">
<td> </td>
<td>.3</td>
<td>ACONV</td>
<td><p>This cross reference is used to keep track of which CP</p>
<p>transaction study was created during the Medicine report conversion and which</p>
<p> Medicine record it is associated with.</p></td>
</tr>
<tr class="even">
<td></td>
<td>.06</td>
<td>ATIU</td>
<td>Used for searches when the user knows the TIU Note title.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, the patient name.</td>
</tr>
<tr class="even">
<td></td>
<td>.04</td>
<td>ACP</td>
<td>Used for searches when the user knows the CP definition.</td>
</tr>
<tr class="odd">
<td></td>
<td>.11</td>
<td>AINST</td>
<td>Used for searches when the user knows if the study was submitted to Imaging.</td>
</tr>
<tr class="even">
<td></td>
<td>.12</td>
<td>AION</td>
<td><p>Used to quickly retrieve</p>
<p>the study ien from the instrument order number.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.09</td>
<td>AS</td>
<td>It is a cross reference on the status of the CP study and it is used for quick look up.</td>
</tr>
<tr class="even">
<td> </td>
<td>.13</td>
<td>AVISIT</td>
<td>This cross reference is used to make sure that a Visit file entry is not deleted as long as there is an entry.</td>
</tr>
<tr class="odd">
<td> </td>
<td>.13</td>
<td>AUPNV</td>
<td>This cross reference tells Visit Tracking how many file entries are using (point to) a Visit file entry.</td>
</tr>
<tr class="even">
<td>Subfile 702.091</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, error messages.</td>
</tr>
<tr class="odd">
<td>Subfile 702.1</td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, image.</td>
</tr>
<tr class="even">
<td><strong>702.01</strong></td>
<td>.02</td>
<td>ASPEC</td>
<td>Used for searches when the user knows the Treating Specialty.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, name of the procedure.</td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>UC</td>
<td>Used to validate a new entry as unique without case sensitivity.</td>
</tr>
<tr class="odd">
<td>Subfile 702.011</td>
<td>.01</td>
<td>AINST</td>
<td>Used for searches when the user knows the name of the instrument.</td>
</tr>
<tr class="even">
<td></td>
<td>.01</td>
<td>B</td>
<td>Regular B Cross Reference of the .01 field, instrument.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch MD*1.0*6 May 2008 Cross References added.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

|                 |                  |                     |                                                                         |
|-----------------|------------------|---------------------|-------------------------------------------------------------------------|
| FILE NUMBER | FIELD NUMBER | CROSS REFERENCE | DESCRIPTION                                                         |
| [^33]702.09 | .01              | B                   | Regular B Cross Reference of the .01 field, name of the instrument.     |
|                 | .01              | UC                  | Used to validate a new entry as unique without case sensitivity.        |
| 703.1       | .02              | ADFN                | Used for searches when the user knows the patient name.                 |
|                 | .03              | ADTP                | Used for searches when the user knows the date/time performed.          |
|                 | .04              | AINST               | Used for searches when the user knows the name of the instrument.       |
|                 | .09              | ASTATUS             | Sets the status for the Gateway to find studies to process.             |
|                 | .05              | ASTUDYID            | This cross reference provide a quick look up by the study reference ID. |
|                 | .01              | B                   | Regular B Cross Reference of the .01 field, the upload ID.              |
| Subfile 703.11  | .01              | B                   | Regular B Cross Reference of the .01 field, upload item.                |
| 703.9       | .01              | B                   | Regular B Cross Reference of the .01 field, Name.                       |
| Subfile 703.91  | .01              | B                   | Regular B Cross Reference of the .01 field, Medicine File Parameters.   |
| Subfile 703.92  | .01              | B                   | Regular B Cross Reference of the .01 field, Conversion ID.              |
|                 | .02              | AS                  | Used for lookup by conversion status.                                   |
| 704.201     | .01              | B                   | Regular B Cross Reference of the .01 field, PATIENT ID.                 |
| 704.202     | .09              | AS                  | Used for lookup of active hemodialysis studies.                         |
|            | .01              | B                   | Regular B Cross Reference of the .01 field, the hemodialysis ID.        |
|            | .02              | C                   | C Cross Reference of the .02 field, PATIENT record number.              |
| 704.209     | .01              | B                   | Regular B Cross Reference of the .01 field, SETTING NAME.               |

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving capability at this time. Purging is available in the CPGateway through the Set Maximum Log Entries option. See description below.

Set Maximum Log Entries allows the user to adjust the number of entries that are displayed in the log file. Once this value is reached, entries will be purged from the beginning of the log to keep the log file from growing too large. This value will take effect after the next polling operation so if the current poll value is 300 seconds it may take up to 5 minutes for the new value to be used. Allowable values are 100 to 10000 entries. When the CP Gateway is shut down, all entries are purged from the log file.

> **NOTE:** Purging is also done daily while the CP Gateway is running. This purge deletes the raw data that comes across from the instrument. The CP Gateway keeps data for a specified number of days based on the entry in the system parameter “Days to keep Instrument Data”. Data older than this will be purged. The data to be deleted is already matched with a study. The fields purged are the Item Value field (#.1) and Item Text field (#.2) of the Upload Item multiple in the CP Results file (#703.1).

![](clinical-procedures-version-1-technical-manual/002.png)

Figure ‑

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^34]Entry points provided by the Clinical Procedures V. 1.0 package to other packages are listed below.

Routine: MDAPI (Controlled Subscription)

COMPONENT: \$\$EXTDATA(MDPROC)

VARIABLES: MDPROC

Type: Input

The CP Definition IEN from CP DEFINITION

file (702.01)

Type: Output

This is an extrinsic function and it

returns: 1/0 for Yes/No.

Entry Point to check if a medical device is associated with

the CP Definition.

COMPONENT: \$\$TIUCOMP(MDNOTE)

VARIABLES: MDNOTE Type: Input

The TIU Document IEN from TIU DOCUMENT

file (#8925).

\$\$TIUCOMP Type: Output

This is an Extrinsic Function and it

returns: 0/1 for fail/success of

transaction completion.

Entry Point to complete a CP transaction.

COMPONENT: \$\$TIUDEL(MDNOTE)

VARIABLES: MDNOTE Type: Input

The TIU Document IEN from TIU DOCUMENT

file (#8925).

Entry Point to clean up the CP Transaction file entry of

the TIU Note that was deleted.

COMPONENT: ISTAT(MDARR)

VARIABLES: MDARR Type: Input

An array of the following:

MDARR(0)="0^error message" or "1^success

message"

MDARR(1)=TrackID (CP;Transaction IEN)

MDARR(2)=Image(s) Queue Number

MDARR(3..N)=Warnings, if error(s) exist.

Entry Point to update Clinical Procedures of the result of

the image(s) that was copied to the Imaging Server.

COMPONENT: ITIU(RESULTS,DFN,CONSULT,VSTRING)

VARIABLES: RESULTS Type: Output

RESULTS(0) will equal one of the

following (Required)

; IEN of the TIU note if successful

; or on failure one of the following status messages

; -1^No patient DFN

; -1^No Consult IEN

; -1^No VString

; -1^Error in CP transaction

; -1^Unable to create CP transaction

; -1^Unable to create the TIU document

; -1^No such consult for this patient.

DFN Type: Input

Patient IEN. (Required)

CONSULT Type: Input

Consult IEN. (Required)

VSTRING Type: Input

VString data for TIU Note. (Required)

This entry point enables VistA Imaging to retrieve/create a

TIU note for a consult for attaching images to.

COMPONENT: \$\$TIUREAS(MDFN,MDOLDC,MDANOTE,MDNDFN,MDNEWC,MDNEWV,MDNTIU)

VARIABLES: MDFN Type: Input

Patient DFN in Patient File (#2).

MDOLDC Type: Input

The old consult number that the TIU note

is being re-assigned from.

MDANOTE Type: Input

The TIU Note internal Entry Number that

is being re-assigned.

MDNDFN Type: Input

The patient DFN who will be re-assigned

to the TIU document.

MDNEWC Type: Input

The new consult number that will be

re-assigned to the TIU document.

MDNEWV Type: Input

The new visit for the TIU document

assignment.

MDNTIU Type: Input

The new re-assigned TIU document internal

entry number.

\$\$TIUREAS Type: Output

This is an extrinsic function and it

returns: 1 for Success or 0^Error

Message.

This entry point enables TIU to notify CP that a TIU note

was reassigned and CP needs to clean up and update the TIU

note re-assignment.

ROUTINE: MDRPCOP (Private Subscription)

COMPONENT: GETVST

VARIABLES: DFN Type: Input

Patient's dfn.

RESULTS Type: Output

A subscripted array that contains a list

of visits:

1st piece has 3 pieces delimited by an

";"

Patient DFN in Patient File (#2).

\- type of visit ("A","I","V")

\- date and time

\- hospital location ien

2nd piece - date/time of visit

(internal format)

3rd & 4 piece - (external format)

hospital location and status.

This sub-module returns a list of visits for a given

patient.

ROUTINE: MDAPI1 (Private Subscription)

COMPONENT: GET(RESULTS,MDARDFN,MDSDT,MDEDT,MDFLDS)

VARIABLES: RESULTS Type: Both

Input: The global ^TMP array in which to

return results. (Required)

Output: Passed by Reference

Global array returned in the FM

DIQ call

format:

MDARDFN Type: Input

The patient DFN (Required).

MDSDT Type: Input

The start date of the date range to

return the data in. This must be in FM

internal format. (Required).

MDEDT Type: Input

The end date of the date range to return

the data in. This must be in FM internal

format. (Required).

MDFLDS Type: Input

A list of fields from file \#691.5 to be

returned in RESULTS. MDFLDS should

contain a list of fields delimited by ";"

(Required).

example: MDFLDS=".01;11;20..."

Example API call:

S RESULTS="^TMP(""NAMESPACE"",\$J)"

D

GET^MDAPI1(.RESULTS,162,2900101,3021001,

".01;11")

return:

^TMP("NAMESPACE",\$J,file \#,record

ien\_","

,field \#,"E")=Data

^TMP("NAMESPACE",\$J,subfile \#,entry

\#\_","\_

record ien field of the

multiple,"E")=data

^TMP("NAMESPACE",\$J,0) will equal

one of the

following,

If the call failed:

-1^No Patient DFN.

-1^No Start Date Range

-1^No End Date Range.

-1^Start Date greater than

End Date.

-1^No fields defined.

If a local variable is defined

in RESULTS,

^TMP("MDAPI",\$J,0) equals

-1^Global TMP array only.

If no return array defined,

^TMP("MDAPI",\$J,0) equals

-1^No return array global.

If no data,

^TMP("NAMESPACE",\$J,0) equals

-1^No data for patient.

ROUTINE: MDPS1 (Controlled Subscription)

COMPONENT: CPA~MDPS1

VARIABLES: DFN Type: Input

Patient Internal Entry Number. (Required)

GMTS1 Type: Input

The ending date in inverse date format

(9999999-date/time). (Required)

GMTS2 Type: Input

The beginning date in inverse date format

(9999999-date/time). (Required)

GMTSNDM Type: Input

The maximum number of entries to return.

(Optional)

GMTSNPG Type: Input

The Page Number. (Optional)

GMTSQIT Type: Input

Quit indicator. (Optional)

This entry point will display Clinical Procedures result

report that have the Procedure Summary Code of ABNORMAL.

The result consists of the Display Result of the Consult

procedure request, if it exists, and the TIU document text.

COMPONENT: CPB~MDPS1

VARIABLES: DFN Type: Input

Patient Internal Entry Number. (Required)

GMTS1 Type: Input

The ending date in inverse date format

(9999999-date/time). (Required)

GMTS2 Type: Input

The beginning date in inverse date format

(9999999-date/time). (Required)

GMTSNDM Type: Input

The maximum number of entries to return.

(Optional)

GMTSNPG Type: Input

The Page Number. (Optional)

GMTSQIT Type: Input

Quit indicator. (Optional)

This entry point will display a brief summary of the

Clinical Procedures result Report. It displays the

Consults \# (if it exists), Procedure Name, Date/Time

Performed, and the Procedure Summary Code.

COMPONENT: CPF~MDPS1

VARIABLES: DFN Type: Input

Patient Internal Entry Number. (Required)

GMTS1 Type: Input

The ending date in inverse date format

(9999999-date/time). (Required)

GMTS2 Type: Input

The beginning date in inverse date format

(9999999-date/time). (Required)

GMTSNDM Type: Input

The maximum number of entries to return.

(Optional)

GMTSNPG Type: Input

The Page Number. (Optional)

GMTSQIT Type: Input

Quit indicator. (Optional)

This entry point displays the full Clinical Procedures

result report. The full report consists of the Display

Result of the Consult procedure, if it exists, and the TIU

document text.

COMPONENT: CPS~MDPS1

VARIABLES: DFN Type: Input

Patient Internal Entry Number. (Required)

GMTS1 Type: Input

The ending date in inverse date format

(9999999-date/time). (Required)

GMTS2 Type: Input

The beginning date in inverse date format

(9999999-date/time). (Required)

GMTSNDM Type: Input

The maximum number of entries to return.

(Optional)

GMTSNPG Type: Input

The Page Number. (Optional)

GMTSQIT Type: Input

Quit indicator. (Optional)

This entry point displays a one line summary of the

Clinical Procedures result report. The one line summary

consists of the Consult Number, if it exists, Procedure

Name, Date/Time Performed, and the Procedure Summary Code.

COMPONENT: EN1~MDPS1(MDGLO,MDDFN,MDSDT,MDEDT,MDMAX,MDPSC,MDALL)

VARIABLES: MDGLO Type: Both

Return Global Array (Required)

MDDFN Type: Input

Patient DFN (Internal Entry Number)

(Required)

MDSDT Type: Input

Start Date in FM Internal Format

(Optional)

MDEDT Type: Input

End Date in FM Internal Format (Optional)

MDMAX Type: Input

Number of studies to return (Optional)

MDPSC Type: Input

Procedure Summary Code to return. The

four Procedure Summary Code are NORMAL,

ABNORMAL, BRODERLINE, and INCOMPLETE. By

passing this parameter, the entry point

will pass studies with this Procedure

Summary Code. (Optional)

MDALL Type: Input

MDALL is flag. If MDALL =1, it

identifies that all text reports with the

procedures list should be returned.

This entry point returns a global Array.

COMPONENT: PR690~MDPS1

VARIABLES: MCARGDA Type: Input

The internal entry number of the Medicine

report record.

MCPRO Type: Input

The free text of the Medicine procedure

name in the Procedure/Subspecialty file

(#697.2).

DFN Type: Input

Patient internal entry number.

ORHFS Type: Input

Order Entry Host File.

Prints the free text of the Medicine report.

COMPONENT: PR702~MDPS1

VARIABLES: MCARGDA Type: Input

The internal entry number of the CP

Transaction record in file (#702).

MCPRO Type: Input

The free text of the CP Definition name

in file (#702.01).

DFN Type: Input

Patient internal entry number.

ORHFS Type: Input

The Order Entry Host File.

Prints the free text of the Clinical Procedures result

interpretation.

COMPONENT: CPC~MDPS1

VARIABLES: DFN Type: Input

Patient Internal Entry Number. (Required)

GMTS1 Type: Input

The ending date in inverse date format

(9999999-date/time). (Required)

GMTS2 Type: Input

The beginning date in inverse date format

(9999999-date/time). (Required)

GMTSNDM Type: Input

The maximum number of entries to return.

(Optional)

GMTSNPG Type: Input

The Page Number. (Optional)

GMTSQIT Type: Input

Quit indicator. (Optional)

This entry point displays the Captioned Clinical Procedures

result report. The captioned report displays the Display

Result of the Consult procedure, if it exists, and the TIU

document text.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. The following describes the installation environment for Version 1.0 of the Clinical Procedures package on the VistA server:

> 1\. VA FileMan V. 22 or greater

> 2\. Kernel V. 8.0 or greater

> 3\. Kernel Toolkit V. 7.3 or greater

> 4\. Kernel RPC Broker V. 1.1 or greater

> 5\. PIMS (Patient Information Management System) V. 5.3 or greater (including):

> a\. Registration V. 5.3

> b\. Scheduling V. 5.3

> 6\. Health Summary V. 2.7 or greater

> 7\. HL7 (Health Level 7) V. 1.6 or greater

> 8\. Consults/Request Tracking V. 3.0

> 9\. TIU (Text Integration Utility) V. 1.0

> 10\. Order Entry V. 3.0 (CPRS (Computerized Patient Record System) V. 1.0 (GUI V. 18.8)) or greater

> 11\. PCE (Patient Care Encounter) V. 1.0 or greater

> 12\. VistA Imaging V. 3.0 or greater (includes installation of background processor and jukebox)

> 13\. Medicine V. 2.3 (optional)

> 14\. Vitals V 5.0 (optional)

> These packages must be patched up through and including the following patches before Clinical Procedures is installed:

> 1\. Patch 17 of Consults/Request Tracking V. 3.0 (GMRC\*3.0\*17)

> 2\. Patch 112 of Order Entry V. 3.0 (OR\*3.0\*112)

> 3\. Patch 109 of Text Integration Utility V. 1.0 (TIU\*1.0\*109)

> 4\. Patch 7 of Imaging V. 3.0 (MAG\*3.0\*7)

> 5\. Patch 93 of HL7 V. 1.6 (HL\*1.6\*93)

> 6\. Patch 98 of HL7 V. 1.6 (HL\*1.6\*98)

> 7\. If Medicine V. 2.3 is installed, you must install Patch 24 of Medicine (MC\*2.3\*24), and Patch 146 of Kernel (XU\*8.0\*146).

2\. [^35]Interface Control Registrations (formerly known as Integration Agreements) between the Clinical Procedures software and other VistA applications exist. Database Interface Control Registrations (DICR) are available on the DBA menu on Forum. For complete information regarding the DICRs for Clinical Procedures V. 1.0, please refer to the *Integration Control Registrations (Agreements)Menu* \[DBA IA ISC\] option under the *DBA* \[DBA\] option on FORUM.

[^36]The following screen capture shows one way to access the DBA option in FORUM:

> Select Software Services Primary Menu Option: DBA

> Select DBA Option: IA  Integration Control Registrations (Agreements)

> Select Integration Control Registrations (Agreements) Option: CUST  Custodial Package Menu

> Select Custodial Package Menu Option: ?

>    1      ACTIVE ICRs by Custodial Package

>    2      Print ALL ICRs by Custodial Package

>    3      Supported References Print All

> Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

> Select Custodial Package Menu Option: 1  ACTIVE ICRs by Custodial Package

> Select PACKAGE NAME: MD  CLINICAL PROCEDURES     MD

> DEVICE: HOME//

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^37]The following are the Clinical Procedures GUI Application menu option, the Clinical Procedures Site Files menu option, and the CP Hemodialysis menu option. Only the MD GUI MANAGER can be invoked independently. The MD GUI USER and MD HEMODIALYSIS USER menu option cannot be invoked independently. They are dependent upon each other. In order to use each module, please refer to the Clinical Procedures Implementation Guide to set up Clinical Procedures.

NAME: MD GUI USER MENU TEXT: MD GUI USER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 59331,44145

RPC: MD TMDOUTPUT

RPC: MD TMDPARAMETER

RPC: MD TMDPATIENT

RPC: MD TMDPROCEDURE

RPC: MD TMDRECORDID

RPC: MD TMDTRANSACTION

RPC: MD TMDUSER

RPC: MD UTILITIES

UPPERCASE MENU TEXT: MD GUI USER

NAME: MD GUI MANAGER MENU TEXT: MD GUI MANAGER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 59385,45622

RPC: MD TMDOUTPUT

RPC: MD TMDPARAMETER

RPC: MD TMDPATIENT

RPC: MD TMDPROCEDURE

RPC: MD TMDRECORDID

RPC: MD TMDTRANSACTION

RPC: MD TMDUSER

RPC: MD UTILITIES

RPC: MD GATEWAY

UPPERCASE MENU TEXT: MD GUI MANAGER

[^38]NAME: MD HEMODIALYSIS USER MENU TEXT: HEMODIALYSIS USER

TYPE: Broker (Client/Server) CREATOR: <span class="mark">REDACTED</span>

TIMESTAMP OF PRIMARY MENU: 60387,39853

RPC: MDK GET VISTA DATA

RPC: MDK GET/SET RENAL DATA

RPC: MDK UTILITY

RPC: VAFCTFU CONVERT DFN TO ICN

RPC: VAFCTFU CONVERT ICN TO DFN

RPC: MD TMDWIDGET

RPC: MD TMDNOTE

RPC: MD TMDCIDC

RPC: MD TMDLEX

RPC: MD TMDENCOUNTER

RPC: GMV MANAGER

RPC: MD GATEWAY

RPC: MD TMDSUBMITU

RPC: ORWPT PTINQ

RPC: GMV PTSELECT

RPC: DG SENSITIVE RECORD ACCESS

RPC: DG SENSITIVE RECORD BULLETIN

RPC: MD TMDRECORDID

UPPERCASE MENU TEXT: HEMODIALYSIS USER

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No package-wide variables are used in this application.

# SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one SAC exemption for Clinical Procedures.

1\. STANDARD SECTION: 3A Namespacing

> DATE GRANTED: APR 25,2002

> Since the Medicine package has become a child of the Clinical Procedures package, the Clinical Procedures package is exempt from being required to export the Medicine package as part of the Clinical Procedures package.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional security measures are to be applied other than those implemented through Menu Manager and the package routines. Clinical Procedures uses the standard RPC broker log-in procedure to validate the user and allow access to the system.

No additional licenses are necessary to run the software.

Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Mail groups and alerts.

> There is one mailgroup associated with this software. This mailgroup is called MD DEVICE ERRORS. The purpose of this mailgroup is to store a list of people who will be notified if a problem arises with an automated instrument. There is one alert in the software that occurs on the VistA server if the package installation does not finish. This alert is sent to the IRMS staff member who ran the installation.

2\. Remote systems.

> The application does not transmit data to any remote system/facility database.

3\. Archiving/Purging.

> Refer to the chapter on [Archiving and Purging](#archiving-and-purging), in this manual. Purging is available in the CPGateway, refer to the Clinical Procedures Gateway chapter in the Clinical Procedures Implementation Guide for more information.

4\. Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems. It is recommended that the CP Gateway be installed on a second machine as a backup in case the initial workstation containing the CP Gateway fails.

5\. Interfacing.

> No specialized (non VA) interfaces are used or required by the application.

6\. Electronic signatures.

> Electronic signatures are not used in the Clinical Procedures package.

7\. Menus.

> There are no options of special note for the Information Security Officers (ISO’s) to view.

8\. Security Keys.

> The MD MANAGER key controls access to the 'Update Study Status' and the 'Delete Study' options. A user holding this key will be able to use the 'Update Study Status' option on any study currently displayed on the screen. Holders of this key will also be taken directly to the 'Update Study Status' option when opening a study marked in status 'Error'. The 'Update Study Status' option does not do any validation on the new status assigned to the study. The 'Delete Study' option will attempt to delete the study after checking the business rules on the VistA server for the study given its current status and state on the server. This key should be given only with extreme care and only to those users that fully understand the status structure, and the ramifications of changing the status or deletion of a study.

9\. File Security.

> DD RD WR DEL LAYGO AUD

> NUMBER NAME GLOBAL NAME ACC ACC ACC ACC ACC ACC

> 702 CP TRANSACTION ^MDD(702, @ @ @

> [^39]702.001 CP_TRANSACTION_TIU_HISTORY ^MDD(702.001, @ @ @ @ @ @

> 702.01 CP DEFINITION ^MDS(702.01, @ \# \# \#

> 702.09 CP INSTRUMENT ^MDS(702.09, @ \# \# \# @

> 703.1 CP RESULT REPORT ^MDD(703.1, @ @ @ @ @

> [^40]703.9 CP CONVERSION ^MDD(703.9, @ \# \# \# \# \#

> [^41]704.201 HEMODIALYSIS ACCESS POINTS ^MDK(704.201, @ @ @

> 704.202 HEMODIALYSIS STUDY ^MDK(704.202 @ @ @

> 704.209 HEMODIALYSIS SETTINGS ^MDK(704.209 @ @ @

10\. References.

> There are no special reference materials for this package.

11\. Official Policies.

> There are no special official policies for this package.

# [^42]Vendor Interfaces 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List of Vendor Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^43]The Puritan Bennett Clinivision, Olympus Endoworks, GE Healthcare Muse and Cardinal Health Sensormedics V-max automated device interfaces are exported with CP. Many other device interfaces are also available and you can view the complete list by visiting the <u>Clinical Procedures website (<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>. [^44]From the Home page, select Find a Device and then search for devices by manufacturer, by type, or by name.

Visit the Clinical Procedures website to view specific information for a particular device.

Click the vendor name to view the web page.

|                    |                                                                            |                                                                                                                                  |                                                |
|--------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Device         | Vendor                                                                 | Type of Procedure Performed                                                                                                  | Type of report with Discrete data included |
| [^45]Clinivision   | [Puritan Bennett](http://www.puritanbennett.com/)                          | Respiratory                                                                                                                      | Text                                           |
| Endoworks          | [<u>Olympus</u>](http://www.olympus.com)                                   | Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy | Text, GIF, JPG                                 |
| Muse               | [<u>GE Healthcare</u>](http://www.gehealthcare.com/worldwide.html)         | ECG, Exercise, Holter, Pacemaker ECG                                                                                             | PDF                                            |
| Sensormedics V-max | [Cardinal Health](http://www.cardinal.com/) (formerly Viasys/Sensormedics) | PFT                                                                                                                              | PDF                                            |
| [^46]Exalis        | [Gambro](http://www.gambro.com/)                                           | Dialysis                                                                                                                         | XML                                            |
| UPF Hemodialysis   | [B.Braun Melsungen AG](http://www.bbraun.com/)                             | Dialysis                                                                                                                         | XML                                            |
| Hypercare          | [Fresenius Medical Care](http://www.fmc-ag.com/)                           | Dialysis                                                                                                                         | XML                                            |

For the latest vendor information, please see the <u>Clinical Procedures website (<http://vista.med.va.gov/ClinicalSpecialties/clinproc>)</u>.

## Device Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here are the setup instructions and vendor contact for each device.

### Clinivision

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: Puritan Bennett   Type: Respiratory

Description:

The uni-directional interface for this instrument is currently available. 

Requirements:

This instrument requires a Clinivision vendor interface.

Setup Instructions:

This section describes the installation setup for the Clinivision system. Note that a new Protocol and HL Logical Link will need to be created for this device since it is a Persistent connected device. Clinivision is not a bi-directional device. Note: Bi-Directional Capabilities checkbox is not checked. Therefore, no outbound HL Logical Link is needed and you do not need to enter any bi-directional information.

![](clinical-procedures-version-1-technical-manual/003.png)

Figure ‑

Figure 15‑1 displays the settings for the Clinivision device in CP Manager.

NODE: MCAR3 INST LLP TYPE: TCP

DEVICE TYPE: Single-threaded Server STATE: Reading

TIME STARTED: SEP 18, 2002@11:45:27 TASK NUMBER: 321004

SHUTDOWN LLP ?: NO QUEUE SIZE: 100

RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

TCP/IP PORT: 1030 TCP/IP SERVICE TYPE: SINGLE LISTENER

PERSISTENT: YES STARTUP NODE: ROU:614A01

IN QUEUE BACK POINTER: 1790 IN QUEUE FRONT POINTER: 1790

OUT QUEUE BACK POINTER: 1789 OUT QUEUE FRONT POINTER: 1789

Figure ‑

Figure 15‑2 shows an entry in the HL Logical Link file for the Clinivision device.

NAME: MCAR3 Device Client ITEM TEXT: Instrument HL7 Event Driver

TYPE: subscriber CREATOR: ACKERMAN,BILL

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This Protocol is used by the HL7 Package to send results to Vista from the Clinivision Instrument.

IDENTIFIER: E TIMESTAMP: 59039,32152

SENDING APPLICATION: INST-MCAR RECEIVING APPLICATION: MCAR-INST

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: P LOGICAL LINK: MCAR3 INST

VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO

Figure ‑

Figure 15‑3 shows the new Protocol that will need to be entered for the Link.

![](clinical-procedures-version-1-technical-manual/004.png)

Figure ‑

[^47]Figure 15‑4. The device will need to be linked to a procedure in CP Manager.

Contact Clinivision and ask the contact to report the device to the production account, port 1030.

Transmission Instructions:

No information available at this time.

Manuals:

No information available at this time.

Vendor Contacts:

<http://www.clinivision.com/contact/>

Trouble Shooting:

Is the machine plugged in?

Is the machine on?

Are all cables connected correctly?

### Endoworks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: Olympus    Type: Bronchoscopy, Colonoscopy, EGD, EGDPEG, Endoscopy, ERCP, Endo Ultrasound, Enteroscopy, Liver Biopsy, Paracentesis, Sigmoidoscopy

Description:

The bi-directional interface for this instrument is currently available.  

Requirements:

This instrument requires an Advanced Gateway vendor interface.

Setup Instructions:

The Olympus Interface is a non-persistent interface and can share its TCP/IP port address with other non-persistent devices. To configure the Olympus (Endoworks) software, it is recommended that you consult Olympus. Olympus has the correct setting for the Endoworks software that is needed to interface with CP.

[^48] The site will need to set up an Olympus type in CPManager.exe for each type of procedure, (such as Olympus (Bronchoscopy), Olympus (Colonoscopy), etc.). Please refer to the Clinical Procedures web site for the device settings for each type of procedure.

NODE: MCAR INST LLP TYPE: TCP

DEVICE TYPE: Single-threaded Server STATE: Reading

TIME STARTED: SEP 18, 2002@11:45:27 TASK NUMBER: 321004

SHUTDOWN LLP ?: NO QUEUE SIZE: 100

RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

TCP/IP PORT: 1030 TCP/IP SERVICE TYPE: SINGLE LISTENER

PERSISTENT: NO STARTUP NODE: ROU:614A01

IN QUEUE BACK POINTER: 1790 IN QUEUE FRONT POINTER: 1790

OUT QUEUE BACK POINTER: 1789 OUT QUEUE FRONT POINTER: 1789

Figure ‑

Figure 15‑5 displays the settings for the standard non-persistent inbound HL Logical Link.

NODE: MCAR OUT LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client STATE: Idle

AUTOSTART: Enabled TIME STARTED: FEB 25, 2008@08:57:54

TASK NUMBER: 3231951 SHUTDOWN LLP ?: NO

QUEUE SIZE: 100

RE-TRANSMISSION ATTEMPTS: 3 READ TIMEOUT: 60

ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

TCP/IP ADDRESS: 10.3.17.141 TCP/IP PORT: 9027

TCP/IP SERVICE TYPE: CLIENT (SENDER) PERSISTENT: NO

STARTUP NODE: DEV:DEVISC4A1 IN QUEUE BACK POINTER: 244

IN QUEUE FRONT POINTER: 244 OUT QUEUE BACK POINTER: 251

OUT QUEUE FRONT POINTER: 244

Figure ‑

Figure 15‑6 displays the settings for the standard non-persistent outbound HL Logical Link.

Transmission Instructions:

No information available at this time

Manuals:

No information available at this time.

Costs:

No information available at this time.

Trouble Shooting:

Is the machine plugged in?

Is the machine on?

Are all cables connected correctly?

### Muse 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: GE Healthcare    Type: ECG

Description:

The bi-directional interface for this instrument is currently available.  

Requirements:

This instrument requires a Muse HL7 vendor interface.

Setup Instructions:

The Muse Interface is a Persistent Interface and must have its own TCP/IP Port address. For configuring the Muse software, it is recommended that you consult with GE Healthcare. GE Healthcare has the correct setting for the Muse software that is needed to interface with CP.

[^49]The Muse can be set up for different Cardiology procedures such as Holter and Exercise Tolerance Test. Please refer to the Clinical Procedures web page for the setup of the device in CPManager.exe for each type of procedure.

Transmission Instructions:

To send data to Clinical Procedures once the results have been sent from the Cart to the MUSE server, follow these steps:

1.  The MUSE generated hard copy is assigned to a cardiologist for over-reading (reviewing).
2.  Changes are made on the interpretation, signed by the doctor and returned to the EKG Department.
3.  EKG Tech logs on to the MUSE. (All users of the MUSE are assigned a number and password with certain levels of NECESSARY access.)
4.  EKG Tech selects over reader (reviewing Cardiologist).
5.  EKG Tech selects the patient.
6.  EKG Tech selects and then edits the interpretation.
7.  EKG Tech selects either Confirm and Print, or Confirm.  If Confirm and Print is selected, the HL7 result is sent, and the report is printed.  If only Confirm is selected, just the HL7 result is sent.

Manuals:

No information available at this time.

Costs:

No information available at this time.

Trouble Shooting:

1.  Is the machine plugged in?
2.  Is the machine on?
3.  Are all cables connected correctly?

### Sensormedics V-MAX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: Cardinal Health    Type: PFT

Description:

The bi-directional interface for this instrument is currently available.

 

Requirements:

This instrument requires a Netlink vendor interface.

[^50]Configuration Files:

This file contains the configuration parameters for the Vmax software.  The vendor should already have a copy of this file. 

Setup Instructions:

The Sensormedics Interface is a Non-Persistent Interface and can share TCP/IP ports with other Non-Persistent device interfaces. The Sensormedics V-MAX software must have a shared directory to hold the report document that is created. The directory might be on the PC or on a network share. The key point is that the directory must be accessible from the Sensormedics V-MAX software.

1.  Start the Sensormedics V-MAX software.
2.  Click on the Reports Button.
3.  Select the Netlinks/IS menu from the menu bar.
4.  Select TCP/IP from the File Menu on the menu bar.
5.  Enter the TCP/IP and Port address to the listener that will be receiving the data from the Sensormedics V-MAX software.
6.  Exit back to the Reports Screen.
7.  Select Setup from the File Menu and enter the Full NETWORK path to the Share directory where you want the PDF document to be stored.

Transmission Instructions:

A path must be setup where the PDF report will be stored prior to being transmitted to V*IST*A Imaging. This path is usually preset to C:\PDFFiles\\ and should be changed to \\(PC Network name)\PDFFiles\\ Also, the directory C:\PDFFiles should have Share enabled with Read, Write, Delete permissions for both Imaging and the PC on which the share directory exists.

The following instructions are for transmitting the final patient report to Clinical Procedures.

> **NOTE:** If the patient whose results you wish to send is already being displayed on the monitor, you can start at step 5.

1.  From the Vmax Program Manager screen click the Find Patient Button. ![](clinical-procedures-version-1-technical-manual/005.png)  The Find Patient window opens. No patients are displayed.
2.  Set search criteria (Last Name, ID, etc.) if any, and click on F1.  A list of patients matching your search criteria appears.
3.  Select the patient whose results you wish to send by clicking on their name.  The selected patient’s name is highlighted.
4.  Click the F3 button to load the selected patients results data.  The Vmax Program Manager screen reappears.
5.  From the Vmax Program Manager screen click the Reports Button. ![](clinical-procedures-version-1-technical-manual/006.png)   The Reports screen appears.
6.  Select the report to process for this patient from the Reports selection box on the left side of the screen.  The selected report appears in the upper left box as the Default Patient Report.
7.  From the Menu bar click the PrintPDF button to compile the PDF report.  A dialog box appears momentarily, indicating the progress of the PDF file creation.
8.  From the Menu bar click Netlink/IS® to open the Netlink Transmission Manager. ![](clinical-procedures-version-1-technical-manual/007.png) The Transmission Manager screen appears

Files to be backed up:

You need to backup these files to preserve the operation of Vmax.  These files should be backed up after the Vmax is working in production.  This list was last updated on May 13, 2003.

Vision folder files used in Netlink communications.

(Depending on software version and configuration, not all files may be present) All files are located in the C:\Vision folder

The following files always exist and have user-modifiable content

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Id_text.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Invalid.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Text_cfg.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmit_cfg.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Xmitcom.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmithdft.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Xmithost.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitparm.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Xmitpath.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitxref.dbf</p></li>
</ul></td>
</tr>
</tbody>
</table>

The following files sometimes exist and have user-modifiable content: They should be manually copied if needed.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Except</p></li>
</ul></td>
<td><ul>
<li><p>Replace</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>User_1.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_2.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>User_3.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_4.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>User_5.dbf</p></li>
</ul></td>
<td><ul>
<li><p>User_6.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>User_7.dbf</p></li>
</ul></td>
<td><ul>
<li><p> </p></li>
</ul></td>
</tr>
</tbody>
</table>

The following files are shipped standard with the software and are NOT user-modifiable. They should only be loaded from the software install disk.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Batchsnd.db1</p></li>
</ul></td>
<td><ul>
<li><p>Ctrl_str.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Received.txt</p></li>
</ul></td>
<td><ul>
<li><p>Response.txt</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Smascii.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Smhl7def.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Smvadef.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xexcept.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Xmiticon.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Xmitprm.dbf</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Xreplace</p></li>
</ul></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

The following files are modified by the software during operation and should NOT be user-modified: They should only be generated by running the software.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Batchsnd.dbf</p></li>
</ul></td>
<td><ul>
<li><p>Fileout1.txt</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Fileout2.txt</p></li>
</ul></td>
<td><ul>
<li><p>Text_rpt.dbf</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Text_rpt.fpt</p></li>
</ul></td>
<td><ul>
<li><p>Usehost</p></li>
</ul></td>
</tr>
</tbody>
</table>

[^51]Please refer to the Clinical Procedures web page for the device setup in CPManager.exe.

Manuals:

No information available at this time.

Costs:

No information available at this time.

Trouble Shooting:

Is the machine plugged in?

Is the machine on?

Are all cables connected correctly?

### [^52]B. Braun

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: B. Braun Melsungen AG Type: Hemodialysis

Description:

Both uni-directional and bi-directional interfaces for this instrument are currently available.

Requirements:

This device uses B. Braun’s UPF Hemodialysis software.

Setup Instructions (B. Braun Device Settings for CP Manager)

#### <table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Setting For:</strong></td>
<td>Clinical Procedures Device Manager</td>
</tr>
<tr class="even">
<td><strong>Procedure Type (HL7 Universal Service ID)</strong></td>
<td>BRAUN (Bi-Directional)</td>
</tr>
<tr class="odd">
<td><strong>Settings:</strong></td>
<td>Device Setup for the BRAUN (Bi-Directional)<br />
-------------------------------------------------------------------------------<br />
NAME: BRAUN (Bi-Directional)<br />
PRINT NAME: BBRAUN<br />
DESCRIPTION: BBraun Dialysis Device Interface<br />
M ROUTINE: MDHL7D<br />
PACKAGE CODE: CP V1.0<br />
ATTACH: UNC<br />
BI-DIRECTIONAL: YES<br />
HL7 INST: BRAUN<br />
HL7 UNIVERSAL SERVICE ID:<br />
-------------------------------------------------------------------------------<br />
Verified at Hines By: W. A. Ackerman</td>
</tr>
</tbody>
</table>

### [^53]Fresenius Medical Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: Fresenius Medical Care Type: Hemodialysis

Description:

Both uni-directional and bi-directional interfaces for this instrument are currently available.

Requirements:

This device uses Fresenius’s Hypercare software.

#### Setup Instructions (Hypercare Device Settings for CP Manager)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Setting For:</strong></td>
<td>Clinical Procedures Device Manager</td>
</tr>
<tr class="even">
<td><strong>Procedure Type (HL7 Universal Service ID)</strong></td>
<td>Fresenius (Bi-directional)</td>
</tr>
<tr class="odd">
<td><strong>Settings:</strong></td>
<td>Device Setup for the Fresenius (Bi-directional)<br />
-------------------------------------------------------------------------------<br />
NAME: Fresenius (Bi-directional)<br />
PRINT NAME: Fresenius<br />
DESCRIPTION: Fresenius Dialysis Device Interface<br />
M ROUTINE: MDHL7D<br />
PACKAGE CODE: CP V1.0<br />
ATTACH: UNC<br />
BI-DIRECTIONAL: YES<br />
HL7 INST: Fresenius<br />
HL7 UNIVERSAL SERVICE ID:<br />
-------------------------------------------------------------------------------<br />
Verified at Hines By: W. A. Ackerman</td>
</tr>
</tbody>
</table>

### [^54]Gambro

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor: Gambro Type: Hemodialysis

Description:

Both uni-directional and bi-directional interfaces for this instrument are currently available.

Requirements:

This device uses Gambro’s Exalis software.

Setup Instructions:Interface Notes for Exalis to Hemodialysis

- Exalis runs on a PC. VA-Exalis_Interface runs on the same PC as Exalis. The PC must be networked so that there can be a TCP\IP connection between VistA and VA-Exalis_Interface. The Exalis software runs as a standard application (not a service), thus requiring that the PC has been logged on with some user account rather than simply turned on. At this time VA-Exalis_Interface, is a standard application. It may become a service if design and resource constraints allow.
- VA-Exalis_Interface is a .NET application and so requires the .NET Framework 1.1 Redistributable which is freely downloadable from Microsoft and will be included on the VA-Exalis_Interface CDROM.

#### B. Braun Device Settings for CP Manager

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Setting For:</strong></td>
<td>Clinical Procedures Device Manager</td>
</tr>
<tr class="even">
<td><strong>Procedure Type (HL7 Universal Service ID)</strong></td>
<td>GAMBRO_EXALIS</td>
</tr>
<tr class="odd">
<td><strong>Settings:</strong></td>
<td>Device Setup for the GAMBRO_EXALIS<br />
-------------------------------------------------------------------------------<br />
NAME: GAMBRO_EXALIS<br />
PRINT NAME: Gambro Exalis<br />
DESCRIPTION: Cobe Dialysis Device Interface<br />
M ROUTINE: MDHL7D<br />
PACKAGE CODE: CP V1.0<br />
ATTACH: UNC<br />
BI-DIRECTIONAL: NO<br />
HL7 INST: GAMBRO_EXALIS<br />
HL7 UNIVERSAL SERVICE ID:<br />
-------------------------------------------------------------------------------<br />
Verified at Hines By: W. A. Ackerman</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
Action A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.
ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.
[^55]API Application programming interface, an interface that a computer system, library or application provides in order to accept requests for services from other programs, and/or to allow data to be exchanged between them.
Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.
Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.
Attachments Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:
> .txt Text files
> .rtf Rich text files
> .jpg JPEG Images
> .jpeg JPEG Images
> .bmp Bitmap Images
> .tiff TIFF Graphics (group 3 and group 4 compressed and uncompressed types)
> .pdf Portable Document Format
> .html Hypertext Markup Language
> .DOC (Microsoft Word files) are not supported. Be sure to convert .doc files to .rtf or to .pdf format.
Background Processing Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.
Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
Boilerplate Text A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.
[^56]Broker Software which mediates between two objects, such as a client and a server or a repository and a requestor.
Browse Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).
Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).
Class Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
Contingency Plan A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
CP Clinical Procedures.
CP Definition CP Definitions are procedures within Clinical Procedures.
[^57]CP Gateway The service application that prepares the data contents of HL7 messages for use in CP Hemodialysis. It requires no direct user interaction.
CP Study A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.
CPRS Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.
Data Dictionary A description of file structure and data elements within a file.
[^58]DBIA Database integration agreement.
Delphi A programming language, also known as Object Pascal.
Device A hardware input/output component of a computer system (e.g., CRT, printer).
[^59]DLL Dynamically-Linked Library – provides the benefit of shared libraries.
Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.
Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.
[^60]DUZ The internal entry number inside FileMan for a particular user.
Edit Used to change/modify data typically stored in a file.
Field A data element in a file.
File The M construct in which data is stored for retrieval at a later time. A computer record of related information.
File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.
File Server A machine where shared software is stored.
Gateway The software that performs background processing for Clinical Procedures.
Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.
GUI Graphical User Interface - a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.
[^61]HFS Host File System
HL7 Health Level 7 messaging, a language which various healthcare systems use to interface with one another.
IEN Internal Entry Number
Interpreter Interpreter is a user role exported with USR\*1\*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.
IRMS Information Resource Management Service.
Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all VistA applications.
MailMan An electronic mail, teleconferencing, and networking system.
Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
Module A component of a software application that covers a single topic or a small section of a broad topic.
Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.
Network Server Share A machine that is located on the network where shared files are stored.
Notebook This term refers to a GUI screen containing several tabs or pages.
OI Office of Information, formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.
Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.
Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.
Page This term refers to a tab on a GUI screen or notebook.
Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.
Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
[^62]Protocol A set of rules governing communication within and between computing endpoints.
Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
[^63]RAID Redundant array of inexpensive disks, a data storage scheme using multiple hard drives to share or replicate data among the drives.
Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.
\<RET\> Carriage return.
Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
[^64]RPC Remote Procedure Call, a protocol that allows a computer program running on one host to cause code to be executed on another host.
SAC Standards and Conventions.
Security Key A function which unlocks specific options and makes them accessible to an authorized user.
Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
Status Symbols Codes used in order entry and Consults displays to designate the status of the order.
Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
Title Titles are definitions for documents. They store the behavior of the documents which use them.
TIU Text Integration Utilities.
[^65]UNC Universal naming Convention.
URL Uniform Resource Locator – a means of finding a resource (such as a web page or a device) on the Internet.
User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
User Class User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.
User Role User Role identifies the role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).
Utility An M program that assists in the development and/or maintenance of a computer system.
[^66]UUEncoded format A form of binary to text encoding whose name derives from "Unix-to-Unix encoding."
Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
VistA Veterans Health Information Systems and Technology Architecture.
Workstation A personal computer running the Windows 9x or NT operating system.

# [^67]XML Extensible Markup Language – A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XMS Extended Memory Specification – The specification describing the use of extended memory in real mode for storing data.

[^1]: Patch MD\*1.0\*6 May 2008 Hemodialysis introduction added.

[^2]: Patch MD\*1.0\*6 May 2008 508 Compliance notice added.

[^3]: Patch MD\*1.0\*14 March 2008 Outdated link removed and replaced with directions to document.

[^4]: Patch MD\*1.0\*6 May 2008 File 702.001 added.

[^5]: Patch MD\*1.0\*5 August 2006 CP Conversion File \#703.9 added.

[^6]: Patch MD\*1.0\*6 May 2008 File 704.201 added.

[^7]: Patch MD\*1.0\*6 May 2008 File 704.202 added.

[^8]: Patch MD\*1.0\*6 May 2008 File 704.209 added.

[^9]: Patch MD\*1.0\*6 May 2008 Default definition added for 702.001.

[^10]: Patch MD\*1.0\*5 August 2006 Default definitions added for 703.9.

[^11]: Patch MD\*1.0\*6 May 2008 Default definitions added for 704.201, 704.202, and 704.209.

[^12]: Patch MD\*1.0\*6 May 2008 RPCs added.

[^13]: Patch MD\*1.0\*6 May 2008 Parameter Definitions added.

[^14]: Patch MD\*1.0\*14 March 2008 Parameter Definitions added.

[^15]: Patch MD\*1.0\*11 June 2009 Parameter Definition added

[^16]: Patch MD\*1.0\*6 May 2008 Parameter Definition added.

[^17]: Patch MD\*1.0\*20 November 2010 Parameter Definitions Added.

[^18]: Patch MD\*1.0\*21 June 2010 Parameter Definition added.

[^19]: Patch MD\*1.0\*6 May 2008 Parameter Definition added.

[^20]: Patch MD\*1.0\*5 August 2006 Parameter Definition added.

[^21]: Patch MD\*1.0\*21 June 2010 Parameter Definition added.

[^22]: Patch MD\*1.0\*11 June 2009 Parameter Definition added.

[^23]: Patch MD\*1.0\*11 June 2009 Parameter Definition added.

[^24]: Patch MD\*1.0\*14 March 2008 Parameter Definition added.

[^25]: Patch MD\*1.0\*21 June 2010 Parameter Definition Added.

[^26]: Patch MD\*1.0\*14 March 2008 Protocols added to support the auto study check-in.

[^27]: Patch MD\*1.0\*14 March 2008 Options added to support the auto study check-in.

[^28]: Patch MD\*1.0\*21 June 2010 Options added to support high volume procedures enhancement.

[^29]: <sup>2</sup> Patch MD\*1.0\*6 May 2008 Hemodialysis User menu option added.

[^30]: Patch MD\*1.0\*5 August 2006 Patch 5 menu options added.

[^31]: Patch MD\*1.0\*11 June 2009 Add new exported option.

[^32]: Patch MD\*1.0\*20 November 2010 New option added.

[^33]: Patch MD\*1.0\*6 May 2008 Cross References added.

[^34]: Patch MD\*1.0\*6 May 2008 Description modified and callable routines added.

[^35]: Patch MD\*1.0\*14 March 2008 External Relations list removed. Integration Agreements renamed Interface Control Registrations.

[^36]: Patch MD\*1.0\*14 March 2008 Screen capture added.

[^37]: Patch MD\*1.0\*6 May 2008 Description modified.

[^38]: Patch MD\*1.0\*6 May 2008 Hemodialysis User menu option added.

[^39]: Patch MD\*1.0\*6 May 2008 File added.

[^40]: Patch MD\*1.0\*5 August 2006 Files added.

[^41]: Patch MD\*1.0\*6 May 2008 Files added.

[^42]: Patch MD\*1.0\*14 March 2008 Deleted vendor contact information for individual contacts.

[^43]: Patch MD\*1.0\*14 March 2008 Updated vendor name list.

[^44]: Patch MD\*1.0\*14 March 2008 Directions for finding a device on the CP website changed.

[^45]: Patch MD\*1.0\*14 March 2008 Device names unlinked due to unavailable links.

[^46]: Patch MD\*1.0\*6 May 2008 Hemodialysis exported new device entries.

[^47]: Patch MD\*1.0\*6 May 2008 Screen capture updated to show new Processing Application field.

[^48]: Patch MD\*1.0\*6 May 2008 Added information about setting up a type for each procedure.

[^49]: Patch MD\*1.0\*6 May 2008 Added information about setting up different procedures.

[^50]: Patch MD\*1.0\*14 March 2008 References to Vmaxconfigfile.zip and sample reports were removed because they are no longer hosted on the Clinical Procedures website.

[^51]: Patch MD\*1.0\*6 May 2008 Added reference to CP web page for device setup.

[^52]: Patch MD\*1.0\*6 May 2008 Added Hemodialysis vendor B. Braun.

[^53]: Patch MD\*1.0\*6 May 2008 Added Hemodialysis vendor Fresenius.

[^54]: Patch MD\*1.0\*6 May 2008 Added Hemodialysis vendor Gambro.

[^55]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^56]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^57]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^58]: Patch MD\*1.0\*6 May 2008 Glossary terms added.

[^59]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^60]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^61]: Patch MD\*1.0\*6 May 2008 Glossary terms added.

[^62]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^63]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^64]: Patch MD\*1.0\*6 May 2008 Glossary terms added.

[^65]: Patch MD\*1.0\*6 May 2008 Glossary terms added.

[^66]: Patch MD\*1.0\*6 May 2008 Glossary term added.

[^67]: Patch MD\*1.0\*6 May 2008 Glossary terms added.