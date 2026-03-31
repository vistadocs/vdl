---
title: MMRS*1*4 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: MMRS
app_name: Methicillin Resistant Staph Aurerus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1*4
group_key: "MMRS:MMRS:1"
file_numbers: 
  - 104
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - mark
  - mmrs
  - class
  - site
  - blockquote
  - mdro
  - parameters
  - software
page_count: 0
word_count: 6018
section_count: 24
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2017
revision_count: 1
revision_newest: 01/30/2017
revision_oldest: 01/30/2017
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

VistA Lab Enhancements – Microbiology

Releases: LR\*5.2\*463 and MMRS\*1.0\*4

Technical Manual

AndSecurity Guide

![](mmrs-1-4-technical-manual/001.png)

January 2017

Document Version 1.0

Office of Information and Technology (OI&T)

Revision History

| Date       | Revision | Description         | Author                             |
|------------|----------|---------------------|------------------------------------|
| 01/30/2017 | 1.0      | Document baselined. | <span class="mark">REDACTED</span> |

<span id="_Ref251310381" class="anchor"></span>Table 1: Text Conventions

Artifact Rational

A Technical Manual is a required end-user document for all OI&T software releases. The intended audience for this document is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
  - [Text Conventions](#text-conventions)
    - [Disclaimers](#disclaimers)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
- [Files](#files)
  - [Kernel Patches](#kernel-patches)
  - [Global Growth](#global-growth)
- [Routines](#routines)
- [Templates](#templates)
- [Parameters](#parameters)
- [Data Dictionary](#data-dictionary)
- [Exported Options](#exported-options)
- [Menus](#menus)
- [Forms](#forms)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-wide Variables](#software-wide-variables)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
  - [Warning Message that Lab Test or Etiology Parameters are not configured](#warning-message-that-lab-test-or-etiology-parameters-are-not-configured)
  - [Warning Message that Etiology Parameter is not configured](#warning-message-that-etiology-parameter-is-not-configured)
  - [Warning Message that Specimen is not Configured](#warning-message-that-specimen-is-not-configured)
- [RACI Chart](#raci-chart)
- [Parameter Setup Checklist](#parameter-setup-checklist)
- [Glossary](#glossary)
The LR\*5.2\*463 patch includes the necessary microbiology enhancements to allow Department of Veterans Affairs (VA) labs the ability to document and utilize standard data in VistA/Computerized Patient Record System (CPRS) for CRE and other Multi-Drug Resistant Organisms (MDROs). In addition, it includes the ability to distribute nationally these microbiology enhancements and other MDRO standardized reporting etiologies without requiring each individual lab to update its own local files manually.
Patch MMRS\*1.0\*4 shall support the timely identification of multi-drug resistant organisms (MDROs), provide enhanced reporting capabilities for Carbapenem Resistant Enterobacteriaceae (CRE) and Clostridium Difficile Infection (CDI) positive cases, and streamline the MDRO initiative by updating the existing MRSA Program Tools menu options and naming conventions to MDRO where applicable.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the guide is to familiarize users with the important features and navigational elements of LR\*5.2\*463 and MMRS\*1.0\*4.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the LR\*5.2\*463 patch has been installed and post-installation procedures have been applied, the following organisms will be available for viewing or for report capture purposes:

- Klebsiella pneumoniae, Carbapenem Resistant (CRE)
- Klebsiella oxytoca, Carbapenem Resistant (CRE)
- Escherichia coli, Carbapenem Resistant (CRE)
- Enterobacter cloacae, Carbapenem Resistant (CRE)
- Enterobacter spp, Carbapenem Resistant (CRE)

The features and functionality provided in the MMRS\*1.0\*4 patch will provide technicians, MDRO Prevention Coordinators (MPCs) and Infection Prevention (IP) personnel automated tools thereby increasing efficiency and reducing the labor hours required previously with manual data mining.

In regards to enhanced reporting capabilities, the MMRS\*1.0\*4 patch shall provide the following new reporting capabilities:

- CDI reporting functionality shall capture positive cases for the wards of a particular facility.
- CRE reporting functionality shall capture positive cases within a facility.

> **NOTE:** As indicated in the Installation Guide, it is required that patch LR\*5.2\*463 and MMRS\*1.0\*3 are installed prior to patch MMRS\*1.0\*4.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for the Technical Manual and Security Guide are the following:

- Laboratory Information Managers (LIMs)
- Microbiology Technologists
- Automated Data Processing Application Coordinators (ADPACs)
- Information Resources Management (IRM) staff

Installation of the patches requires interactive participation between IRM staff and LIM or ADPAC personnel.

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:

| Font              | Use                              | Example                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the link: <http://www.va.gov/vdl>                                                      |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
|                       | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
|                       | VistA filenames                      | XYZ file \#798.1                                                                                                          |
|                       | VistA field names                    | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.” |
| Courier New, bold     | User responses to screen prompts     | NO                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                          |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | “There are no changes in the performance of the system once the installation process is complete.”                        |
| Times New Roman Bold  | Emphasis                             | Note: You can also type the access code, followed by a semicolon, followed by the verify code.                        |

<span id="_Toc473531787" class="anchor"></span>Table 2: List of Routines

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following references were used in preparation of this document:
- LR\*5.2\*463 Patch Description. February 2016.
- MMRS\*1.0\*4 Patch Description. December 2016.
- Microbiology Systems Design Document (SDD). March 2016, version 0.6.
- MMRS\*1.0\*3 User Manual. July 2010, version 1.0
- MMRS\*1.0\*3 Technical Manual. July 2010, version 1.0.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram depicts the overall data flows between the VistA Lab package and CPRS.

<span id="_Toc473531791" class="anchor"></span>Figure 1: High-level Process Flowchart

![](mmrs-1-4-technical-manual/002.png)

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA software is a Kernel Installation and Distribution System (KIDS) software release and will be distributed as a PackMan message via Forum.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*463 and MMRS\*1.0\*4 patches operate on the current VA computer hardware systems.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*463 and MMRS\*1.0\*4 patches operate on the current VA computer systems, which includes Kernel 8.0 and FileMan 22.

The following prerequisite releases are required prior to the installation of MMRS\*1.0\*4:

- MMRS\*1.0\*3
- LR\*5.2\*463

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan 22 is the only database requirement for the LR\*5.2\*463 and MMRS\*1.0\*4 patches.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of the patches requires interactive participation between IRM staff and LIM or ADPAC personnel.

You may wish to install the patches during non-peak hours.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Kernel Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patches must be current on the target system to avoid problems loading and/or installing the patches.

## Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no significant change to global growth.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of routines applies to the LR\*5.2\*463 and MMRS\*1.0\*4 releases:

| Routine | Release  | Brief Description                                                                                                      |
|-------------|--------------|----------------------------------------------------------------------------------------------------------------------------|
| MMRSCDI     | MMRS\*1.0\*4 | This routine was created for the CDI report to capture positive C. diff. cases as well as to track the patients’ movement. |
| MMRSCDI1    | MMRS\*1.0\*4 | This routine is a continuation of MMRSCDI.                                                                                 |
| MMRSCRE     | MMRS\*1.0\*4 | This routine was created for the CRE report for admitted patients to capture the number of cases.                          |
| MMRSCRE2    | MMRS\*1.0\*4 | This routine is a continuation of MMRSCRE.                                                                                 |
| MMRSCRE3    | MMRS\*1.0\*4 | This routine is a continuation of MMRSCRE2.                                                                                |
| MMRSCRE4    | MMRS\*1.0\*4 | This routine is a continuation of MMRSCRE3.                                                                                |
| MMRSCRE5    | MMRS\*1.0\*4 | This routine was created for the CRE report (tasked) and for Taskman to schedule the report.                               |
| MMRSIPCP    | MMRS\*1.0\*4 | This routine was created for the CRE report for multiple specimens.                                                        |
| MMRSP4      | MMRS\*1.0\*4 | This routine was created for the Setup MDRO Tools Software Parameters.                                                     |
| LR463ETI    | LR\*5.2\*463 | This routine is for the post install to change the package name.                                                           |

<span id="_Toc473531789" class="anchor"></span>Table 4: RACI Chart

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New templates were not created for the releases.

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New parameters are not associated with the releases.

# Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The figure below is an illustration of the Data Dictionary for file \#104, MDRO Site Parameters. Changes to fields are highlighted.

<span id="_Toc473531792" class="anchor"></span>Figure 2: Data Dictionary for \#104

<table>
<caption><p><span id="_Toc473531790" class="anchor"></span>Table 5: Parameter Setup Checklist</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:27 PAGE 1</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>This file holds the set of parameters which modify the operation of the MRSA</p>
<p>Program Tools to suit the needs of your site. For multi-divisional facilities,</p>
<p>each division should have a separate entry in this file.</p>
<p>DD ACCESS: @</p>
<p>RD ACCESS: @</p>
<p>WR ACCESS: @</p>
<p>DEL ACCESS: @</p>
<p>LAYGO ACCESS: @</p>
<p>AUDIT ACCESS: @</p>
<p>(NOTE: Kernel's File Access Security has been installed in this UCI.)</p>
<p>POINTED TO BY: DIVISION field (#1) of the MDRO TOOLS LAB SEARCH/EXTRACT File</p>
<p>(#104.1)</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:28 PAGE 2</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>DIVISION field (#.01) of the DIVISION sub-field (#104.22) of</p>
<p>the MDRO TYPES File (#104.2)</p>
<p>DIVISION field (#1) of the MDRO WARD MAPPINGS File (#104.3)</p>
<p>CROSS</p>
<p>REFERENCED BY: SPECIMEN(AB), SPECIMEN(AC), DIVISION(B)</p>
<p>104,.01 DIVISION 0;1 POINTER TO MEDICAL CENTER DIVISION FIL</p>
<p>E (#40.8) (Required)</p>
<p>LAST EDITED: OCT 28, 2008</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:30 PAGE 3</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>HELP-PROMPT: Enter the division the parameters are for.</p>
<p>DESCRIPTION: This field contains the division the parameters</p>
<p>are defined for.</p>
<p>CROSS-REFERENCE: 104^B</p>
<p>1)= S ^MMRS(104,"B",$E(X,1,30),DA)=""</p>
<p>2)= K ^MMRS(104,"B",$E(X,1,30),DA)</p>
<p>104,1 RECEIVING UNIT SCREEN 0;2 SET</p>
<p>'0' FOR NO;</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:31 PAGE 4</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>'1' FOR YES;</p>
<p>LAST EDITED: MAR 04, 2009</p>
<p>HELP-PROMPT: Enter 'Yes' if at your site the admitting (or</p>
<p>receiving) unit screens patients on</p>
<p>unit-to-unit transfers.</p>
<p>DESCRIPTION: This field should be set to 'Yes' if at your</p>
<p>site the admitting (or receiving) unit screens</p>
<p>patients on unit-to-unit transfers.</p>
<p>104,2 DISCHARGING UNIT SCREEN 0;3 SET</p>
<p>'0' FOR NO;</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:32 PAGE 5</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>'1' FOR YES;</p>
<p>LAST EDITED: OCT 28, 2008</p>
<p>HELP-PROMPT: Enter 'Yes' if at your site the discharging</p>
<p>unit screens patients on unit-to-unit</p>
<p>transfers.</p>
<p>DESCRIPTION: This field should be set to 'Yes' if at your</p>
<p>site the discharging unit screens patients on</p>
<p>unit-to-unit transfers.</p>
<p>104,3 SCREEN POS ON TRANSFER IN 0;4 SET</p>
<p>'0' FOR NO;</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:32 PAGE 6</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>'1' FOR YES;</p>
<p>LAST EDITED: MAR 04, 2009</p>
<p>HELP-PROMPT: Enter 'Yes' if at your site you are screening</p>
<p>all patients on transfers into the unit,</p>
<p>regardless of MRSA status.</p>
<p>DESCRIPTION: This field should be set to 'Yes' if at your</p>
<p>site you are screening all patients on</p>
<p>transfers into the unit, regardless of MRSA</p>
<p>status. This field should be set to 'No' if you</p>
<p>only screen patients not known to be infected</p>
<p>and/or colonized with MRSA on transfers into</p>
<p>the unit.</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:34 PAGE 7</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>104,4 SCREEN POS ON DISCHARGE 0;5 SET</p>
<p>'0' FOR NO;</p>
<p>'1' FOR YES;</p>
<p>LAST EDITED: MAR 16, 2009</p>
<p>HELP-PROMPT: Enter 'Yes' if at your site you are screening</p>
<p>patients on discharge, death, or transfer out</p>
<p>from the unit, regardless of MRSA status.</p>
<p>DESCRIPTION: This field should be set to 'Yes' if at your</p>
<p>site you are screening patients on discharge,</p>
<p>death, or transfer out from the unit,</p>
<p>regardless of MRSA status.</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:35 PAGE 8</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>This field should be set to 'No' if you only</p>
<p>screen patients not known to be infected and/or</p>
<p>colonized with MRSA on discharge, death, or</p>
<p>transfer out from the unit.</p>
<p>104,5 ISOLATION ORDERS 1;0 POINTER Multiple #104.05</p>
<p>(Add New Entry without Asking)</p>
<p>104.05,.01 ISOLATION ORDER 0;1 POINTER TO ORDERABLE ITEMS FILE (#10</p>
<p>1.43)</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:38 PAGE 9</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>(Required) (Multiply asked)</p>
<p>LAST EDITED: MAR 04, 2009</p>
<p>HELP-PROMPT: Enter the isolation orderable item.</p>
<p>DESCRIPTION: The orderable item that is used at your</p>
<p>facility for isolation purposes.</p>
<p>CROSS-REFERENCE: 104.05^B</p>
<p>1)= S ^MMRS(104,DA(1),1,"B",$E(X,1,30),DA)=""</p>
<p>2)= K ^MMRS(104,DA(1),1,"B",$E(X,1,30),DA)</p>
<p>104.05,1 EXPANDED PRECAUTION TYPE 0;2 SET</p>
<p>'1' FOR CONTACT PRECAUTIONS;</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:39 PAGE 10</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>'2' FOR CONTACT PRECAUTIONS SPECIAL;</p>
<p>'3' FOR AIRBORNE INFECTION;</p>
<p>'4' FOR DROPLET;</p>
<p>'5' FOR PROTECTIVE ENVIRONMENT;</p>
<p>'6' FOR ISOLATION ORDER;</p>
<p>LAST EDITED: AUG 17, 2009</p>
<p>HELP-PROMPT: Enter the expanded precaution type this order</p>
<p>is used for.</p>
<p>DESCRIPTION: The expanded precaution type this order is</p>
<p>used for.</p>
<p>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</p>
<p>JAN 26,2017@11:13:40 PAGE 11</p>
<p>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</p>
<p>ROU (VERSION 1.0)</p>
<p><mark>DATA NAME GLOBAL DATA</mark></p>
<p><mark>ELEMENT TITLE LOCATION TYPE</mark></p>
<p><mark>-------------------------------------------------------------------------------</mark></p>
<p><mark>104,216061 SPECIMEN 61;0 POINTER Multiple #104.0216061</mark></p>
<p><mark>DESCRIPTION: This subfile contains specimen(s) for each</mark></p>
<p><mark>division.</mark></p>
<p><mark>104.0216061,.01 SPECIMEN 0;1 POINTER TO TOPOGRAPHY FIELD FILE (#6</mark></p>
<p><mark>1) (Multiply asked)</mark></p>
<p><mark>LAST EDITED: AUG 25, 2016</mark></p>
<p><mark>HELP-PROMPT: Select the specimen to be associated with</mark></p>
<p><mark>this division.</mark></p>
<p><mark>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</mark></p>
<p><mark>JAN 26,2017@11:13:47 PAGE 12</mark></p>
<p><mark>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</mark></p>
<p><mark>ROU (VERSION 1.0)</mark></p>
<p><mark>DATA NAME GLOBAL DATA</mark></p>
<p><mark>ELEMENT TITLE LOCATION TYPE</mark></p>
<p><mark>-------------------------------------------------------------------------------</mark></p>
<p><mark>DESCRIPTION: This field contains the specimens mapped to</mark></p>
<p><mark>this particular institution.</mark></p>
<p><mark>CROSS-REFERENCE: 104.0216061^B</mark></p>
<p><mark>1)= S ^MMRS(104,DA(1),61,"B",$E(X,1,30),DA)="</mark></p>
<p><mark>"</mark></p>
<p><mark>2)= K ^MMRS(104,DA(1),61,"B",$E(X,1,30),DA)</mark></p>
<p><mark>CROSS-REFERENCE: 104^AB</mark></p>
<p><mark>1)= S ^MMRS(104,"AB",$E(X,1,30),DA(1),DA)=""</mark></p>
<p><mark>STANDARD DATA DICTIONARY #104 -- MDRO SITE PARAMETERS FILE</mark></p>
<p><mark>JAN 26,2017@11:13:47 PAGE 13</mark></p>
<p><mark>STORED IN ^MMRS(104, (5 ENTRIES) SITE: TEST.XXXXX.XXX.XX.XXX UCI: VISTA,</mark></p>
<p><mark>ROU (VERSION 1.0)</mark></p>
<p><mark>DATA NAME GLOBAL DATA</mark></p>
<p><mark>ELEMENT TITLE LOCATION TYPE</mark></p>
<p><mark>-------------------------------------------------------------------------------</mark></p>
<p><mark>2)= K ^MMRS(104,"AB",$E(X,1,30),DA(1),DA)</mark></p>
<p><mark>This cross reference is on the entire file by</mark></p>
<p><mark>specimen - division</mark></p>
<p><mark>CROSS-REFERENCE: 104^AC^MUMPS</mark></p>
<p><mark>1)= S ^MMRS(104,"AC",DA(1),$E(X,1,30),DA)=""</mark></p>
<p><mark>2)= K ^MMRS(104,"AC",DA(1),$E(X,1,30),DA)</mark></p>
<p><mark>This cross reference is on the entire file</mark></p>
<p><mark>sorted by division, specimen, IEN.</mark></p>
<p><mark>FILES POINTED TO FIELDS</mark></p>
<p><mark>MEDICAL CENTER DIVISION (#40.8) DIVISION (#.01)</mark></p>
<p><mark>ORDERABLE ITEMS (#101.43) ISOLATION ORDERS:ISOLATION ORDER (#.01)</mark></p>
<p><mark>TOPOGRAPHY FIELD (#61) SPECIMEN:SPECIMEN (#.01)</mark></p>
<p>INDEX AND CROSS-REFERENCE LIST -- FILE #104 01/26/17 PAGE 14</p>
<p>-------------------------------------------------------------------------------</p>
<p>INPUT TEMPLATE(S):</p>
<p>PRINT TEMPLATE(S):</p>
<p>SORT TEMPLATE(S):</p>
<p>FORM(S)/BLOCK(S):</p>
<p>MMRSISLTORD MAR 02, 2009@11:09 USER #0</p>
<p>MMRSISLTORDHDR DD #104</p>
<p>MMRSISLTORDEDITHDR DD #104</p>
<p>MMRSISLTORDEDIT2 DD #104.05</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473531790" class="anchor"></span>Table 5: Parameter Setup Checklist

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches LR\*5.2\*463 and MMRS\*1.0\*4 do not contain any associated exported options or protocols.

# Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new menus will be available after the installation of MMRS\*1.0\*4:

- MMRS CDI REPORT 
- MMRS CDI REPORT (Tasked)            
- MMRS CRE REPORT               
- MMRS MDRO HIST DAYS EDIT      
- MMRS MDRO LAB PARAMETER SETUP 
- MMRS CRE SITE PARAMETER SETUP
- MMRS MDRO WARD MAPPING SETUP  

# Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the forms associated with MMRS\*1.0\*4:

> <span id="_Toc473531793" class="anchor"></span>Figure 3: Forms

| Form     | Associated File |
|--------------|---------------------|
| MMRSISLTORD  | 104                 |
| MMRSLABPARAM | 104.1               |

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail groups, alerts, and bulletins were not created, required, or used by the software.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the public interfaces associated with patches LR\*5.2\*463 and MMRS\*1.0\*4.

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integration Control Registrations (ICRs) were not required.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

API’s are not applicable.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC’s are not applicable.

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Web services were not created and/or used.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAC exemptions for this software were not required.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All related routines are listed in Section 4, Routines.

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAC exemptions for this software were not required.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Privacy represents information that must be protected and covers the collection, use, and disclosure of personal information. Security represents how information must be protected and encompasses the methods for accessing and protecting the information. A Security Guide aids in controlling the release of sensitive information related to nationally released software. LR\*5.2\*463 and MMRS\*1.0\*4 do not contain any highly sensitive information. Information may be obtained through the Freedom of Information Act (FOIA) requests. There are no unique/atypical features or other information that would be of interest to security personnel or other support groups.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security menus and options are not distributed with the releases.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various menu options are available to the user*.* However, it should be noted that users who have not been assigned a MMRS Setup security key will only have access to the MDRO Tools Reports Menu.

The following security key is required for MMRS\*1.0\*4:

- MMRS SETUP

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any additional file security for the software is not required.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures are not applicable.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software does not provide any secure data transmission capabilities.

The following websites address encryption of data exchanged over any facility connection:

- Federal Information Security Management Act (FISMA): [http://csrc.nist.gov/groups/SMA/fisma/index.html](http://csrc.nist.gov/groups/SMA/fisma/index.html%20)

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software does not provide any data archiving capabilities.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-standard or special cross-references are not applicable.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The table below lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information.

<span id="_Ref390770787" class="anchor"></span>Table 3: Tier Support Contact Information

| Name                                  | Role                   | Org | Contact Information             |
|-------------------------------------------|----------------------------|---------|-------------------------------------|
| Clinical Application Coordinator          | Tier 0 Support             | VHA     | To be determined (TBD).             |
| OI&T National Service Desk                | Tier 1 Support             | OI&T    | <span class="mark">REDACTED</span>  |
| OI&T Local Support                        | Tier 2 Support             | OI&T    | OI&T Local Helpdesk                 |
| Health Product Support                    | Tier 2 Support             | VHA     | <span class="mark">REDACTED</span>  |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T    | <span class="mark">REDACTED</span>  |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T    | <span class="mark">REDACTED</span>  |
| Enterprise Operations                     | Tier 3 & 4 Support         | OI&T    | OI&T Enterprise Operations Helpdesk |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

## Warning Message that Lab Test or Etiology Parameters are not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Laboratory Test or Etiology parameters have not been configured, and a user attempts to generate the CDI Report, the following message will be displayed to the user:

<span id="_Toc473301375" class="anchor"></span>Figure 4: Warning Dialog regarding Lab Test/Etiology Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The report cannot be run because the Laboratory Test(s) or</p>
<p>the Etiology is not configured in the MDRO TOOLS LAB</p>
<p>SEARCH/EXTRACT file, (104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Consult the on MDRO Tools Lab Parameter Setup for information on how to enter laboratory and/or etiology parameters for historical reporting of multi-drug resistant organisms (MDROs).

## Warning Message that Etiology Parameter is not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Etiology parameter has not been configured, and a user attempts to generate the CRE Report, the following message will be displayed to the user:

<span id="_Toc473301376" class="anchor"></span>Figure 5: Warning Dialog regarding Etiology Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The report cannot be run because the Etiology has not been</p>
<p>configured in the MDRO TOOLS LAB SEARCH/EXTRACT file,</p>
<p>(#104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Correct the issue by configuring the etiology parameters. Consult the section regarding MDRO Tools Lab Parameter Setup for more information.

## Warning Message that Specimen is not Configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site has not configured specimen(s), and a user attempts to run the CRE Report, the following message will be displayed to the user:

<span id="_Toc473301377" class="anchor"></span>Figure 6: Warning Dialog regarding Specimen Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Make sure a division and/or a Surveillance specimen has been</p>
<p>setup using the option: 'CRE Tools Site Parameter Setup'</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Consult the section regarding the CRE Tools Parameter Setup menu option on how to configure the CRE parameters for division(s).

# RACI Chart 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Responsible (R): The persons or groups who execute the task are responsible for the correct execution of the process and activities.
- Accountable (A): For each activity, only one role (person or group) should be answerable for owning the end result and process quality.
- Consulted (C): A person or group that provides additional knowledge and information.
- Informed (I): A person or group that only receives process execution and quality information (per activity or in summary form).

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Functional Roles</strong></th>
<th><blockquote>
<p><strong>Requirements</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Design</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Development</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Test</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Documentation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Training</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Deployment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Program Manager</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Project Manager</td>
<td>R</td>
<td>R</td>
<td>R</td>
<td>R, I, C</td>
<td>R</td>
<td>R</td>
<td>R</td>
</tr>
<tr class="odd">
<td>Project Planner</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
</tr>
<tr class="even">
<td>Technical Architect</td>
<td>I, C</td>
<td>A, R</td>
<td>A, R</td>
<td>R, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
</tr>
<tr class="odd">
<td>Functional Analyst</td>
<td>R, I, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, I, C</td>
<td>R, I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Requirements Manager</td>
<td>A, R</td>
<td>R, I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
<td>R, I, C</td>
<td>I, C</td>
</tr>
<tr class="odd">
<td>Configuration Manager</td>
<td>I</td>
<td>I</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I</td>
<td>A, R</td>
</tr>
<tr class="even">
<td>Test Manager</td>
<td>I</td>
<td>I</td>
<td>I, C</td>
<td>A, R</td>
<td>R, I, C</td>
<td>I</td>
<td>I, C</td>
</tr>
<tr class="odd">
<td>Test Analyst</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>R, C</td>
<td>I, C</td>
<td>I</td>
<td>I</td>
</tr>
<tr class="even">
<td>Lead Developer</td>
<td>I, C</td>
<td>I, C</td>
<td>R, C</td>
<td>R, C</td>
<td>R, I, C</td>
<td>I, C</td>
<td>R, I, C</td>
</tr>
<tr class="odd">
<td>Developer</td>
<td>I, C</td>
<td>I, C</td>
<td>R, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
</tr>
<tr class="even">
<td>Training Manager</td>
<td>I</td>
<td>I, C</td>
<td>I, C</td>
<td>I, C</td>
<td>R, I, C</td>
<td>A, R</td>
<td>I</td>
</tr>
<tr class="odd">
<td>Technical Writer</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>I</td>
<td>A, R</td>
<td>I</td>
<td>I</td>
</tr>
</tbody>
</table>

# Parameter Setup Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parameter setup section should be completed prior to running any reports. The Information Resource Manager (IRM), MRSA Prevention Coordinator (MPC), or Laboratory Information Manager (LIM) are responsible for each step as noted in the table below.

| Step \# | Description                                                                                                                                                                                                                                                                                          | Responsible |  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------|
| 1       | Install patch LR\*5.2\*463 and perform post-installations as outlined in the Deployment, Installation, Back-out, and Rollback Guide.                                                                                                                                                                     | IRM             |       |
| 2       | Install patch MMRS \*1.0\*4                                                                                                                                                                                                                                                                              | IRM             |       |
| 3       | Assign users the appropriate menus and keys.                                                                                                                                                                                                                                                             | IRM             |       |
| 4       | Using option MDRO Tools Parameter Setup (Main), add the division(s) that the facility will require. For integrated or co-located sites more than one division will most likely need to be added. After the division is added, answer the prompts based on the business rules in place for that division. | MPC/IRM         |       |
| 5       | Using option MDRO Tools Lab Parameter Setup, add the appropriate lab parameters for the different MDROs.                                                                                                                                                                                                 | MPC/LIM         |       |
| 6       | Using option MDRO Tools Ward Mapping Setup, setup the ward mappings. (Remember to separate out OBS units from the geographical units and to create all OBS units as separate units).                                                                                                                     | MPC             |       |
| 7       | Using option MDRO Historical Days Edit, enter the time frame to search for the last positive MDRO result?                                                                                                                                                                                                | MPC             |       |
| 8       | Using option Isolation Orders Add/Edit add the orders that are used for isolation purposes. (Only needed if the site uses Isolation Orders).                                                                                                                                                             | MPC             |       |
| 9       | Setup the tasked options: Print Isolation Report (Tasked)and Print Nares Screen Compliance List (Tasked) to the appropriate printers (optional).                                                                                                                                                         | IRM/MPC         |       |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Glossary of Terms</strong></th>
<th><strong>Definitions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access Code</td>
<td><p>A code that allows the computer to identify</p>
<p>you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator.</p></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td><p>Automated Data Processing Coordinator.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM). Also, the designated individual responsible for user-level management and maintenance of an application package (<em>e.g.</em>, Laboratory).</td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td><p>FileMan is a set of <a href="#Glos_M">M</a> or MUMPS utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<blockquote>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FORUM</td>
<td><blockquote>
<p>FORUM is the VA’s national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The National Patch Module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (<em>e.g.,</em> a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>File Transfer Protocol (FTP)</td>
<td><blockquote>
<p>A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in Internet Standard 9, Request for Comments 959.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Globals</td>
<td><p>M uses <em>globals</em>: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
<p>SET ^A(“first_name”)=”Keeley”</p>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<blockquote>
<p>For all of these reasons, one of the most common M programs is a database management system. FileMan is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel Installation and Distribution System (KIDS)</td>
<td><blockquote>
<p>KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LIM</td>
<td><blockquote>
<p>Laboratory Information Manager.</p>
<p>The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other Computerized Patient Record System (CPRS) functions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>M</td>
<td><p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. M data structures are sparse, using strings of characters as subscripts.</p>
<blockquote>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><blockquote>
<p>MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MUMPS</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Namespace</td>
<td><blockquote>
<p>A logical partition on a physical device that contains all the artifacts for a complete M system, including globals, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MDRO-PT.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td><blockquote>
<p>A specific type of MailMan message used to distribute KIDS builds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VAMC</td>
<td><blockquote>
<p>Department of Veterans Affairs Medical Center.</p>
</blockquote></td>
</tr>
</tbody>
</table>
