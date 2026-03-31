---
title: National Clozapine Registry Technical Manual (YS*5.01*227)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: NCR
app_name: "Registry: National Clozapine Coordination"
section: CLI
app_status: active
pkg_ns: NCR
patch_ver: 5.01
patch_id: NCR*5.01
group_key: "NCR:NCR:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - clozapine
  - supported
  - reference
  - vista
  - software
  - patient
  - class
  - span
page_count: 0
word_count: 4210
section_count: 22
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Registries_National_Clozapine_Coordination/ys_5_01_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Registries_National_Clozapine_Coordination/ys_5_01_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=236"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>National Clozapine Registry

  VistA Mental Health Package

  Patch YS\*5.01\*227

  Technical Manual
---

![](national-clozapine-registry-technical-manual-ys-5-01-227/001.png)

April 2024

Office of Information and Technology

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description                                                                         | Author               |
|------------|----------|-------------------------------------------------------------------------------------|----------------------|
| April 2024 | 1.0      | VistA Mental Health package, Patch YS\*5.01\*227, in support of NCR VistA Wishlist. | Liberty IT Solutions |

<span id="ColumnTitle_01" class="anchor"></span>Table 1 Revision History

Artifact Rational

A Technical Manual is a required end-user document for all OIT software releases. The intended audience for the *National Clozapine Registry Technical Manual* is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

Table of Contents

Table of Figures

Table of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
    - [Disclaimers](#disclaimers)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
- [Files](#files)
  - [VistA Mental Health Files](#vista-mental-health-files)
  - [VistA File Updates](#vista-file-updates)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-Wide Variables](#software-wide-variables)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [Appendix A: Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)
The National Clozapine Registry (NCR) is the Department of Veterans Affairs (VA) enterprise Clozapine patient registry. NCR is sponsored by the Veterans Affairs, National Pharmacy Benefits Management (PBM) organization. The National Clozapine Coordinating Center (NCCC) staff use the NCR to track VA Clozapine patients, their history of Clozapine use in the VA, and related laboratory results. It is the source of data used to prepare reports of VA Clozapine prescriptions and blood test results to the Food and Drug Administration (FDA) Clozapine Risk Evaluation and Mitigation Strategy (REMS) – a legally mandated public health registry. The system contains records of VA Clozapine patients since 1993 including patient demographic information, FDA-required Clozapine identifiers, laboratory results from each time they receive a Clozapine prescription, and any Clozapine pharmacy lock-out overrides that result from VA programmed safety order checks.
This patch modifies VistA to introduce expanded National Clozapine functionality. This update, implemented as patch YS\*5.01\*227, is also referred to as the VistA Wishlist.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Technical Manual provides information about the VistA Mental Health package, Patch YS\*5.01\*227. As further outlined in the patch description document, the purpose of this patch is to implement requested feature enhancements in the VistA Clozapine logic.

The Clozapine order check logic has been updated to use the value of a new field in the Clozapine Parameters file to determine how far back to look for blood test labs when placing Clozapine orders. In addition, lab results entered with only a date in the collection time will no longer be excluded from the search. The nightly process has also been updated to allow 74 days without activity before automatically discontinuing a patient as a Clozapine patient instead of the old period of 28 days for newly-registered patients and 56 days for established patients.

The DCON (discontinue) command in the YSCL MailMan server logic has been modified to toggle the patient's Clozapine status between Active and Discontinued.

The CLOZAPINE PATIENT LIST (#603.01) FILE has been updated to add a new index on the CLOZAPINE REGISTRATION NUMBER (#.01) and CLOZAPINE PATIENT (#1) fields that will trigger when the record is deleted and automatically discontinue that patient as a Clozapine patient in the PHARMACY PATIENT (#55) file.

This document describes how to maintain the components of the NCR as well as how to troubleshoot problems that might occur with this product in production. The intended audience for this document is the Information Technology (IT) teams responsible for hosting and maintaining the system after production release.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCR is a web-based Graphical User Interface (GUI) application that contains information on VA Clozapine users and saves data to an Azure Structured Query Language (SQL) database. The NCR application and supporting database are hosted in the VA Enterprise Cloud (VAEC) Microsoft Azure Government (MAG) environment.

The functionality added to VistA as part of YS\*5.01\*227 is specific to VistA and does not have a dependency on the NCR web application.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The audience for this Technical Manual is local IT support (formerly known as IRM), management, and development personnel. It is assumed that the reader has access to VistA.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the manuals related to NCR that are available to view in the [VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=236) or the NCR GitHub repository.
| File Name                      | Document Name                                                                                             | Location                         |
|------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------|
| YS_5.01_227_DIBRG.pdf              | National Clozapine Registry Deployment, Installation, Back-out and Rollback Guide (updated for YS\*5.01\*227) | Located in the VDL                   |
| YS_5.01_227 patch description.docx | National Clozapine Registry Patch Description                                                                 | Located in the NCR GitHub repository |
| YS_5.01_227_VDD                    | National Clozapine Registry Version Description Document                                                      | Located in the NCR GitHub repository |
| NCR_UG_ADMIN.pdf                   | National Clozapine Registry User Guide: Admin (updated for YS\*5.01.227)                                      | Located in the VDL                   |
| NCR_UG_STAFF.pdf                   | National Clozapine Registry User Guide: Staff (updated for YS\*5.01.227)                                      | Located in the VDL                   |
<span id="_Ref158639151" class="anchor"></span>Table 2 NCR Reference Material

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 provides an overview of the connections and data flows between the NCR web application, VDIF-EP, and VistA sites. The arrows labeled as REST calls and responses with a JSON payload depict the multi-system, end-to-end transactions.

Patch YS\*5.01\*227 functionality is located within the VistA Sites box.

<span id="_Ref158630170" class="anchor"></span>Figure Overview Flow Chart

![](national-clozapine-registry-technical-manual-ys-5-01-227/002.png)

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VistA software is a Kernal Installation and Distribution System (KIDS) software release, distributed as a Packman message via the National Patch Module. It should be installed on an up-to-date VistA system. This software also requires that the local VistA system be accessible to VDIF to receive the data passed from the NCR GUI through the API call added in this release.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCR Web App does not employ a physical hardware infrastructure. The infrastructure is composed of logical cloud components hosted in Azure in the VAEC. Each of the Web App environments consists of the following (Figure 2):

<span id="_Ref158629275" class="anchor"></span>Figure Azure Environment Components

![](national-clozapine-registry-technical-manual-ys-5-01-227/003.png)

While no change to the existing infrastructure is anticipated, it is expected that the Azure application services will handle the integration between the Clozapine Application process and VA MPI.

This integration’s code progression and testing progression will go from VA MPI DEV to VA MPI SQA to SQA UAT then to VA MPI Production. Change control and quality requirements will be met and approved by IDM subject matter experts in each environment before Clozapine Application is allowed to connect to the next environment.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product (Patch YS\*5.01\*227) runs on standard software platforms that are used by each VHA facility. These enhancements are compatible with existing VistA database platforms, compilers, utilities, operating systems, and communication software. The programming language is MUMPS/M/Cache on the Cache Studio developer interface toolset.

The NCR software is not a separate system; it is code contained in the Outpatient Pharmacy, Inpatient Medications, and Mental Health packages located in each VAMCs VistA database. It uses VistA data files as its main database source. The NCR software application has a presentation layer at the top, a service layer in the middle, and a data services layer at the bottom.

As described in more detail earlier, this patch modifies the Clozapine order check logic to use the value of a new field in the Clozapine Parameters file to determine the look-back for blood test labs when placing Clozapine orders. Additionally, lab results entered with only a date in the collection time will not be excluded from the search. The nightly process has been updated to allow 74 days without activity before automatically discontinuing a patient as a Clozapine patient as opposed to the prior 28-day period for newly-registered patients and 56 days for established patients.

The DCON command in the YSCL MailMan server logic now toggles patient Clozapine status between Active and Discontinued.

The CLOZAPINE PATIENT LIST file has a new index on the CLOZAPINE REGISTRATION NUMBER and CLOZAPINE PATIENT fields that triggers when the record is deleted and automatically discontinues the patient as a Clozapine patient in the PHARMACY PATIENT file.

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database requirements in VistA for this patch.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To request access to the NCR application, users must complete a new user registration form (details in section 3.1.1 of YS_5.01_227_UG_Admin) or contact the NCCC Administration staff to be added manually to the system (Details in section 4.3.1 of YS_5.01_227_UG_Admin).

Figure 3, below, provides an overview of the NCR application components as deployed within the Microsoft Azure Government environment. This figure also shows the connectivity points with external systems, including VDIF-EP integration introduced with Patch 242.

<span id="_Ref158630940" class="anchor"></span>Figure NCR Application Components

![](national-clozapine-registry-technical-manual-ys-5-01-227/004.png)

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Mental Health Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 provides a listing of the applicable VistA Mental Health package files associated with this patch.

| File Number | File Name                     |
|-------------|-------------------------------|
| 601         | MH INSTRUMENT                 |
| 601.2       | PSYCH INSTRUMENT PATIENT      |
| 601.3       | COPYRIGHT HOLDER              |
| 601.4       | INCOMPLETE PSYCH TEST PATIENT |
| 601.6       | MH MULTIPLE SCORING           |
| 601.71      | MH TESTS AND SURVEYS          |
| 601.72      | MH QUESTIONS                  |
| 601.73      | MH INTRODUCTIONS              |
| 601.74      | MH RESPONSE TYPES             |
| 601.75      | MH CHOICES                    |
| 601.751     | MH CHOICETYPES                |
| 601.76      | MH INSTRUMENT CONTENT         |
| 601.77      | MH BATTERIES                  |
| 601.78      | MH BATTERY CONTENTS           |
| 601.781     | MH BATTERY USERS              |
| 601.79      | MH SKIPPED QUESTIONS          |
| 601.81      | MH SECTIONS                   |
| 601.82      | MH RULES                      |
| 601.83      | MH INSTRUMENTRULES            |
| 601.84      | MH ADMINISTRATIONS            |
| 601.85      | MH ANSWERS                    |
| 601.86      | MH SCALEGROUPS                |
| 601.87      | MH SCALES                     |
| 601.88      | MH DISPLAY                    |
| 601.89      | MH CHOICEIDENTIFIERS          |
| 601.91      | MH SCORING KEYS               |
| 601.92      | MH RESULTS                    |
| 601.93      | MH REPORT                     |
| 601.94      | MH CR SCRATCH                 |
| 603.01      | CLOZAPINE PATIENT LIST        |
| 603.02      | CLOZAPINE LAB TEST            |
| 603.03      | CLOZAPINE PARAMETERS          |
| 603.04      | CLOZAPINE TESTS               |
| 604         | ADDICTION SEVERITY INDEX      |
| 604.26      | ASI PROGRAM TYPE              |
| 604.3       | ASI LEGAL CODE                |
| 604.4       | ASI LIVING ARRANGEMENTS       |
| 604.45      | ASI PATIENT RATING SCALE      |
| 604.48      | ASI ROUTE OF ADMINISTRATION   |
| 604.5       | ASI FAMILY HX CODES           |
| 604.55      | ASI FOLLOW UP                 |
| 604.66      | ASI QUICK FORM                |
| 604.68      | ASI NARRATIVE                 |
| 604.77      | ASI SUBSTANCE CODE            |
| 604.8       | ASI PARAMETERS                |
| 615.2       | SECLUSION/RESTRAINT           |
| 615.5       | S/R REASONS                   |
| 615.6       | S/R CATEGORY                  |
| 615.7       | S/R RELEASE CRITERIA          |
| 615.8       | S/R ALTERNATIVES              |
| 615.9       | S/R OBSERVATION CHECKLIST     |
| 627.7       | DSM                           |

<span id="_Ref158629373" class="anchor"></span>Table 3 VistA Mental Health Files

## VistA File Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the CLOZAPINE PATIENT LIST (603.01) file. This file is stored in the ^YSCL global.

CLOZAPINE PATIENT LIST (File 603.01)

CLOZAPINE REGISTRATION NUMBER (Field .01)

CLOZAPINE PATIENT (Field 1)

A new index (AD) has been created referencing field .01 and field 1 and triggers when the record is deleted – discontinues the patient as a Clozapine patient in PHARMACY PATIENT (file 55).

CLOZAPINE PARAMETER (File 603.03)

LAB LOOKBACK DEFAULT (Field 12) – New field holding the number of days to pull historical blood test labs when placing Clozapine orders.

DISCONTINUE LOOKBACK (Field 13) – New field holding the number of days of inactivity before the nightly process will discontinue a patient as a Clozapine patient.

The patch will set the two fields on install.

Lab Lookback Default is being set to 30 days.

Discontinue Lookback is being set to 74 days.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Six routines are being delivered with patch YS\*5.01\*227:

- Routine Name: YSCLDIS 
- Routine Name: YSCLHLAB 
- Routine Name: YSCLP227 (New)
- Routine Name: YSCLSRV2
- Routine Name: YSCLTST2
- Routine Name: YSCLTST4

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options are exported in this patch.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA MailMan will continue to serve as a communications interface to transmit data between the applications, as well as between NCCC and the facilities. Moving from weekly data Clozapine transmission to “real-time” Clozapine data transmission will increase the number of emails generated on a weekly basis to approximately 1000 to 1500.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no public interfaces for NCR.

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 defines the difference between Controlled Subscriptions and Supported References in VistA.

<table>
<caption><p><span id="_Ref158629478" class="anchor"></span>Table Controlled Subscription versus Supported Reference</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Controlled Subscription</td>
<td>Describes attributes/functions that must be controlled in their use. The decision to restrict the Integration Control Registration (ICR) is based on the maturity of the custodian package. Typically, these ICRs are created by the requesting package based on their independent examination of the custodian package's features. For the ICR to be approved the custodian grants permission to other VistA packages to use the attributes/functions of the ICR; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="even">
<td>Supported Reference</td>
<td><p>This applies where any VistA application may use the attributes/functions defined by the ICR (these are also called “Public”). An example is an ICR that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the ICR database. There is no need for other VistA packages to request an ICR to use these references; they are open to all by default.</p>
<p>NOTE: ICRs categorized as Supported References are listed on the DBA menu on FORUM and are open for use by everyone.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref158629478" class="anchor"></span>Table Controlled Subscription versus Supported Reference

All the Integration Control Registrations in the patch are supported references, as listed below in Table 5.

<table>
<caption><p><span id="_Ref158629323" class="anchor"></span>Table Integration Control Registrations</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>ICR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YSCLDIS</td>
<td><p>Reference to ^DPT supported by IA #10035</p>
<p>Reference to ^PS(55 supported by IA #787</p>
<p>Reference to $$SITE^VASITE supported by IA #10112</p>
<p>Reference to ^DIC supported by DBIA #2051</p>
<p>Reference to ^DIE supported by DBIA #2053</p>
<p>Reference to ^DIQ supported by DBIA #2056</p>
<p>Reference to ^XLFDT supported by DBIA #10103</p>
<p>Reference to ^XMD supported by DBIA #10070</p>
<p>Reference to ^%DTC supported by DBIA #10000</p></td>
</tr>
<tr class="even">
<td>YSCLHLAB</td>
<td><p>Reference to ^LAB(60 supported by IA #333</p>
<p>Reference to ^PS(55 supported by IA #787</p>
<p>Reference to ^LR7OR1 supported by IA #2503</p>
<p>Reference to ^DIC supported by DBIA #2051</p>
<p>Reference to ^DIQ supported by DBIA #2056</p>
<p>Reference to ^XLFDT supported by DBIA #10103</p>
<p>Reference to ^%DTC supported by DBIA #10000</p>
<p>Reference to ^VA(200 supported by DBIA #10060</p></td>
</tr>
<tr class="odd">
<td>YSCLP227</td>
<td>None</td>
</tr>
<tr class="even">
<td>YSCLSRV2</td>
<td><p>Reference to ^%ZOSF supported by IA #10096</p>
<p>Reference to ^DPT supported by IA #10035</p>
<p>Reference to ^DD("DD" supported by IA #10017</p>
<p>Reference to ^PS(55 supported by IA #787</p>
<p>Reference to ^PSDRUG supported by IA #25</p>
<p>Reference to ^PSRX supported by IA #780</p>
<p>Reference to ^VA(200 supported by IA #10060</p>
<p>Reference to $$SITE^VASITE supported by IA #10112</p>
<p>Reference to $$FMTE^XLFDT() supported by IA #10103</p>
<p>Reference to ^PSDRUG supported by IA #221</p>
<p>Reference to ^LAB(60 supported by IA #333</p>
<p>Reference to ^%DT supported by DBIA #10003</p></td>
</tr>
<tr class="odd">
<td>YSCLTST2</td>
<td><p>Reference to ^LAB(60 supported by IA #333</p>
<p>Reference to ^PSDRUG supported by IA #25</p>
<p>Reference to ^PS(55 supported by IA #787</p>
<p>Reference to ^XMD supported by IA #10070</p>
<p>Reference to ^LR7OR1 supported by IA #2503</p>
<p>Reference to ^DIC supported by DBIA #2051</p>
<p>Reference to ^DIE supported by DBIA #2053</p>
<p>Reference to ^DIQ supported by DBIA #2056</p>
<p>Reference to ^DIR supported by DBIA #10026</p>
<p>Reference to $$SITE^VASITE supported by DBIA #10112</p>
<p>Reference to ^XLFDT supported by DBIA #10103</p>
<p>Reference to MIX^DIC1 supported by DBIA #10007</p>
<p>Reference to ^%ZTLOAD supported by DBIA #10063</p>
<p>Reference to ^%DTC supported by DBIA #10000</p>
<p>Reference to ^%DT supported by DBIA #10003</p>
<p>Reference to PSS^PSS781 supported by DBIA #4480</p>
<p>Reference to $$GETREGYS^PSOCLUTL supported by DBIA #7314</p></td>
</tr>
<tr class="even">
<td>YSCLTST4</td>
<td><p>Reference to ^LAB(60 supported by IA #333</p>
<p>Reference to ^LR7OR1 supported by IA #2503</p>
<p>Reference to ^DIC supported by DBIA #2051</p>
<p>Reference to ^DIQ supported by DBIA #2056</p>
<p>Reference to ^%DTC supported by DBIA #10000</p></td>
</tr>
</tbody>
</table>

<span id="_Ref158629323" class="anchor"></span>Table Integration Control Registrations

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 6 lists the software interfaces for the current patch.

<table>
<caption><p><span id="_Ref158629663" class="anchor"></span>Table 6 Software Interfaces</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Package</th>
<th>Min. Version Required</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FileMan</td>
<td>1.0*2</td>
<td>FileMan is VistA’s database management system (DBMS)</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>8.0</td>
<td><p>The VistA MailMan software is designed to allow users, or VistA software applications, to send and receive mail from individuals or groups, electronically, through communication lines, modems, and other networks.</p>
<p>Note: Mailman does not support encryption.</p></td>
</tr>
<tr class="odd">
<td>Outpatient Pharmacy</td>
<td>7.0</td>
<td><p>Outpatient Pharmacy provides a method for managing the medications given to Veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital. Outpatient Pharmacy is known as the “Back Door”.</p>
<p>When orders are processed using the back door, Outpatient Pharmacy utilizes the Mental Health software to perform checks to see if the patient is registered and has a Clozapine authorization number.</p>
<p>Outpatient Pharmacy is used to register patients within the Clozapine program.</p>
<p>Outpatient Pharmacy uses the Mental Health Clozapine Software to perform safety checks.</p>
<p>Once an order passes safety checks, the order is dispensed by the Pharmacist. The Clozapine data is transmitted to the national Clozapine database.</p></td>
</tr>
<tr class="even">
<td>Inpatient Medications</td>
<td>5.0</td>
<td><p>The Inpatient Medications package provides a method of management, dispensing, and administration of inpatient drugs within the hospital.</p>
<p>When orders are processed using the back door, Inpatient Medications utilizes the Mental Health software to perform authorization number.</p>
<p>Inpatient Medications uses the Mental Health Clozapine Software to perform safety checks and verify changes in the Dose per Day.</p>
<p>Once an order passes safety checks, the order is activated by the Pharmacist. The Clozapine data is transmitted via MailMan messages to the Hines OI&amp;T VistA RUCL package, and is subsequently downloaded to the National VA Clozapine Registry in Dallas.</p></td>
</tr>
<tr class="odd">
<td>Mental Health</td>
<td>5.01</td>
<td><p>The Mental Health module provides computer support for both clinical and administrative patient care activities associated with mental health care.</p>
<p>The Mental Health software contains the YSCL server that provides the capability for the NCCC in Dallas to interact (both read and write) with a local VistA system’s Clozapine-related files through MailMan messages.</p>
<p>The Mental Health software also contains Clozapine-related software including the CLAPI and other Clozapine APIs.</p>
<p>CLAPI is called by CPRS and the Pharmacy applications, when a patient’s WBC and ANC lab results must be checked. CLAPI interfaces with the Laboratory system to obtain a patient’s WBC and ANC lab results, calculates if Clozapine can safely be dispensed, and returns the results to CPRS, and the Pharmacy applications.</p></td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Current</td>
<td><p>CPRS is a VistA computer application. CPRS is the Computerized Patient Record System where authorized providers utilize CPOE Computerized Order Entry.</p>
<p>CPRS enables doctors and medical professionals to initiate a Clozapine order utilizing the Order or Meds Tab.</p>
<p>Prior to initiating the order, CPRS utilizes the Mental Health software to perform checks to see if the patient is registered and has a Clozapine authorization number.</p>
<p>Once an order is initiated, it is sent to a Pharmacy application depending on a patient’s status either as an Inpatient Medications or an Outpatient Pharmacy for processing.</p></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>8.0</td>
<td>Kernel provides a portability layer between the underlying operating system and the application code. This results in the entire VistA system being portable among different computers, operating systems, and M implementations.</td>
</tr>
</tbody>
</table>

<span id="_Ref158629663" class="anchor"></span>Table 6 Software Interfaces

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Software-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VistA menus or options required for operation of this patch. Technical staff may be interested in the following related menus listed below:

- CLOZAPINE MULTI TEST LINK
- HLO MAIN MENU
- HL7 MAIN MENU
- PSOL MANAGER
- YSCL HL7 MAIN

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following keys are required for operation of this patch.

- YSCL AUTHORIZED

Other associated keys of interest are listed below.

- ORES
- PROVIDER
- PSDRPH
- PSOLOCKCLOZ
- PSORPH

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application troubleshooting within the production environment is a collaborative effort that includes Tire 1, Tier 2, and Tier 3 resources. Initial communication of a production defect is reported through the ServiceNow/YourIT ticketing system.

The NCR development and sustainment team does not have access to VA production environments, so involvement of this team entails screen sharing and over-the-shoulder analysis with the help of Tier 1 and/or Tier 2 staff, or production users.

Evaluation of results within VistA can be done by checking the standard VistA/Mumps error trap. This can be done via the Mumps command line or through a VistA menu option.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

Specific error correction guidance is provided in the NCR DIBRG, which can be found in the [VA Software Documentation Library](#references) (VDL).

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enterprise Service Desk (ESD) Provides critical IT support to Veterans Affairs. Contact information can be found online at the VA YourIT service portal.

# Appendix A: Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 7 provides the abbreviations and acronyms used throughout the NCR Technical Manual.

| Acronym  | Description                                                     |
|----------|-----------------------------------------------------------------|
| ANC      | Absolute Neutrophil Count (Lab Test)                            |
| API      | Application Programming Interface                               |
| CLAPI    | Clozapine Application Programming Interface                     |
| CPOE     | Computerized Order Entry                                        |
| CPRS     | Computerized Patient Record System                              |
| DBA      | Database Administrator                                          |
| DBMS     | Database Management System                                      |
| DIBRG    | Deployment, Installation, Back-out, and Rollback Guide          |
| ESD      | Enterprise Service Desk                                         |
| FDA      | Food and Drug Administration                                    |
| GUI      | Graphical User Interface                                        |
| IT       | Information Technology                                          |
| ICR      | Integration Control Registration                                |
| IdM      | Identity Management                                             |
| IRM      | Incident Response Message                                       |
| JSON     | JavaScript Object Notation                                      |
| KIDS     | Kernal Installation and Distribution System                     |
| M        | MUMPS                                                           |
| MAG      | Microsoft Azure Government                                      |
| MPI      | Master Patient Index                                            |
| MUMPS    | Massachusetts General Hospital Utility Multi-Programming System |
| NCCC     | National Clozapine Coordinating Center                          |
| NCR      | National Clozapine Registry                                     |
| OIT      | Office of Information and Technology                            |
| PBM      | Pharmacy Benefits Management                                    |
| Power BI | Power Business Intelligence                                     |
| REMS     | Risk Evaluation and Mitigation Strategy                         |
| REST     | Representational State Transfer                                 |
| RUCL     | Roll-Up Clozaril                                                |
| SQA      | Software Quality Assurance                                      |
| SQL      | Structured Query Language                                       |
| UAT      | User Acceptance Test                                            |
| VA       | Department of Veterans Affairs                                  |
| VAEC     | VA Enterprise Cloud                                             |
| VDIF     | Veterans Data Integration and Federation                        |
| VDIF-EP  | Veterans Data Integration and Federation Enterprise Platform    |
| VDL      | VA Software Documentation Library                               |
| VistA    | Veterans Health Information Systems and Technology Architecture |
| WBC      | White Blood Count (Lab Test)                                    |

<span id="_Ref148962500" class="anchor"></span>Table 7 Acronyms and Abbreviations