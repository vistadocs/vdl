---
title: LA*5.2*64/LR*5.2*286 LEDI III Implementation and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*64
group_key: "LEDI:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - shipping
  - test
  - host
  - laboratory
  - facility
  - collection
  - ledi
  - edit
  - specimen
  - manifest
page_count: 0
word_count: 31753
section_count: 11
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iii_imp_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iii_imp_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

![](la-5-2-64-lr-5-2-286-ledi-iii-implementation-and-user-guide/001.png)

LABORATORY

ELECTRONIC DATA INTERCHANGE III (LEDI III)

IMPLEMENTATION AND

USER GUIDE

LA\*5.2\*64/LR\*5.2\*286

December 2004

VistA Health System Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Staffing Requirements:](#staffing-requirements)
    - [IRM Staff:](#irm-staff)
    - [IRM and LIM Staff:](#irm-and-lim-staff)
  - [### Intended Users:](#intended-users)
    - [Users Interface:](#users-interface)
  - [VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT](#vista-blood-bank-software-v52-device-product-labeling-statement)
    - [### Patch LR\5.2\286](#patch-lr52286)
  - [VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT](#vista-blood-bank-software-v52-device-product-labeling-statement-1)
    - [Patch LA\5.2\64:](#patch-la5264)
  - [# Orientation](#orientation)
  - [LEDI III Implementation and User Guide](#ledi-iii-implementation-and-user-guide)
    - [LEDI III Implementation and User Guide Screen Displays](#ledi-iii-implementation-and-user-guide-screen-displays)
  - [LEDI III Software and Documentation Retrieval Locations](#ledi-iii-software-and-documentation-retrieval-locations)
    - [LEDI III Software and Documentation Retrieval Formats](#ledi-iii-software-and-documentation-retrieval-formats)
    - [VistA Website Locations:](#vista-website-locations)
    - [References](#references)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [VistA Laboratory Electronic Data Interchange Phase III (LEDI III)](#vista-laboratory-electronic-data-interchange-phase-iii-ledi-iii)
  - [LEDI III Enhancements and Modifications](#ledi-iii-enhancements-and-modifications)
    - [Enhancements:](#enhancements)
    - [Modifications:](#modifications)
  - [Data Dictionary Changes](#data-dictionary-changes)
    - [LABORATORY TEST file (#60)](#laboratory-test-file-60)
    - [TOPOGRAPHY FIELD file (#61)](#topography-field-file-61)
    - [AUTO INSTRUMENT file (#62.4)](#auto-instrument-file-624)
    - [#### Renamed Field:](#renamed-field)
    - [LA7 MESSAGE LOG BULLETINS file (#62.485)](#la7-message-log-bulletins-file-62485)
    - [LA7 MESSAGE QUEUE file (#62.49)](#la7-message-queue-file-6249)
    - [LAB SHIPPING MANIFEST file (#62.8)](#lab-shipping-manifest-file-628)
    - [LAB SHIPPING CONFIGURATION file (#62.9)](#lab-shipping-configuration-file-629)
    - [LOAD/WORK LIST (#68.2)](#loadwork-list-682)
    - [### LAB PENDING ORDERS ENTRY file (#69.6)](#lab-pending-orders-entry-file-696)
    - [LEDI III New Options](#ledi-iii-new-options)
    - [Modified Options](#modified-options)
- [LEDI III Implementation Instructions](#ledi-iii-implementation-instructions)
    - [LEDI III Two-Part Implementation Setup](#ledi-iii-two-part-implementation-setup)
    - [COLLECTION facility – VA to Commercial Reference Laboratory](#collection-facility-va-to-commercial-reference-laboratory)
    - [LEDI III Implementation Configuration Setup Checklist](#ledi-iii-implementation-configuration-setup-checklist)
    - [HOST facility setting up COLLECTION facility ChecklistNOTE: Use this checklist to ensure that Step 6—LIM (HOST facility): LAB SHIPPING CONFIGURATION file (#62.9) setup, located in the Implementation section of this manual, has been completed.](#host-facility-setting-up-collection-facility-checklistnote-use-this-checklist-to-ensure-that-step-6lim-host-facility-lab-shipping-configuration-file-629-setup-located-in-the-implementation-section-of-this-manual-has-been-completed)
- [Use of the Software](#use-of-the-software)
    - [INTENDED END USERS: Laboratory Information Manager (LIM)/Laboratory Automated Data Processing Application Coordinator (ADPAC)](#intended-end-users-laboratory-information-manager-limlaboratory-automated-data-processing-application-coordinator-adpac)
    - [Electronic Catalog Menu \[LA7S CATALOG MENU\]](#electronic-catalog-menu-la7s-catalog-menu)
    - [INTENDED END USERS: LIM/Lab ADPAC, HOST and COLLECTION facility Laboratory staff](#intended-end-users-limlab-adpac-host-and-collection-facility-laboratory-staff)
    - [INTENDED END USER: COLLECTION and HOST facility Laboratory Staff](#intended-end-user-collection-and-host-facility-laboratory-staff)
    - [INTENDED END USER: HOST facility Laboratory Staff](#intended-end-user-host-facility-laboratory-staff)
    - [INTENDED END USER: HOST facility Laboratory Staff](#intended-end-user-host-facility-laboratory-staff-1)
    - [Information-help menu \[LRHELP\]](#information-help-menu-lrhelp)
    - [INTENDED END USER: Laboratory Staff](#intended-end-user-laboratory-staff)
    - [General Lab User Parameters \[LRUSER PARAM\] option](#general-lab-user-parameters-lruser-param-option)
    - [General report for selected tests \[LRGEN\] option](#general-report-for-selected-tests-lrgen-option)
    - [Interim report for selected tests as ordered \[LRRSP\] option](#interim-report-for-selected-tests-as-ordered-lrrsp-option)
    - [Order/test status \[LROS\] option](#ordertest-status-lros-option)
    - [Review by order number \[LRCENLKUP\] option](#review-by-order-number-lrcenlkup-option)
    - [Test description information \[LREV\] option](#test-description-information-lrev-option)
    - [Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] Option](#lab-messaging-nightly-cleanup-la7task-nighty-option)
    - [INTENDED END USER LAB INFORMATION MANAGER/IT SUPPORT](#intended-end-user-lab-information-managerit-support)
    - [Lab Interface Menu \[LA INTERFACE\]Example: This menu contains the Laboratory auto instrument options](#lab-interface-menu-la-interfaceexample-this-menu-contains-the-laboratory-auto-instrument-options)
    - [INTENDED END USER: Laboratory Information Manager (LIM)/It Support](#intended-end-user-laboratory-information-manager-limit-support)
    - [INTENDED USER: Laboratory Information Manager (LIM)](#intended-user-laboratory-information-manager-lim)
- [Glossary](#glossary)
The Veterans Health Information Systems and Architecture (VistA) Laboratory Electronic Data Interchange III (LEDI III) Lab Data Sharing Interoperability (LDSI) Patch LA\*5.2\*64 and Patch LR\*5.2\*286 Implementation and User Guide Version 5.2 provides the Department of Veterans Affairs) Medical Center (VAMC) Information Resource Management (IRM) staff, Laboratory Information Manager (LIM), and other VAMC users with a straightforward means for implementing and using the new LEDI III LDSI software product.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM Staff:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for installing patches LA\*5.2\*64/LR\*5.2\*286, establishing mail groups, and menu assignments.

### IRM and LIM Staff:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The COLLECTION and HOST facilities IRM and LIM staff must coordinate the implementation of the LEDI III setup after the patches are installed. The LEDI III setup process must be performed in the sequence specified in the VistA LEDI III User Guide section.

## ### Intended Users:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users of this software enhancement project include VA medical center’s laboratory personnel and Department of Defense (DoD) facilities laboratory personnel.

### Users Interface:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users will build orders, create shipping manifests, close/ship shipping manifest, and verify/ release and modify results into VistA for VA facilities and Composite Health Care System (CHCS) for DoD laboratories via LEDI III LDSI. Patches LA\*5.2\*64 and LR\*5.2\*286 provide enhancements to the existing laboratory software functionality for data entry and retrieval between the VA and DoD facilities.

## VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Patch LR\*5.2\*286

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Package patch LR\*5.2\*286 contains changes to software controlled by VHA DIRECTIVE 99-053, titled VISTA BLOOD BANK SOFTWARE VERSION 5.2. Change includes:

The addition of the “USE FOR REFERENCE TESTING” field (#13) to the “SITE/SPECIMEN SUB-FIELD” (#60.01) of the LABORATORY TEST file (#60).

The addition of the “USE FOR REFERENCE TESTING” field to the “LR ATOMIC TESTS” Input Template.

The above change has been reviewed by the VISTA Blood Bank Developer and found to have no impact on the VISTA BLOOD BANK SOFTWARE version 5.2 control functions.

RISK ANALYSIS: Changes made by patch LR\*5.2\*286 have no effect on Blood Bank software functionality, therefore RISK is none.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR\*5.2\*286 does not alter or modify any software design safeguards or safety critical elements functions.

POTENTIAL IMPACT ON SITES: This patch contains changes to a Data Dictionary identified in Veterans Health Administration (VHA) Directive 99-053. The changes have no effect in Blood Bank functionality or medical device control functions. There is no adverse potential to sites.

VALIDATION REQUIREMENTS BY OPTION: There are no required validation scenarios to be completed by sites after installing LR\*5.2\*286.

## VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch LA\*5.2\*64:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*64 does not contain any changes to the VISTA BLOOD BANK Software as defined by VHA DIRECTIVE 99-053 titled VISTA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*64 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LA\*5.2\*64 have no effect on Blood Bank software functionality, therefore RISK is none.

VALIDATION REQUIREMENTS BY OPTION: Because of the nature of the changes made, no specific validation requirements exist as a result of installation of this patch.

Test Sites:

The following 11 test sites listed below assisted in testing the LEDI III LDSI software enhancements and modifications on the following hardware platforms prior to the actual release date of the software:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 22%" />
<col style="width: 23%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VA Test Sites and</p>
<p>Hardware Platform</p></th>
<th>Test Site Partner</th>
<th>Bi-directional or Unidirectional</th>
<th>Which direction?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Albuquerque VAMC VMS/DSM - VMS/Cache</td>
<td>Brooks AFB DoD</td>
<td>Unidirectional</td>
<td>VA↔︎DoD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Boston (HCS) VMS/DSM &amp; - VMS/Cache</td>
<td>VAMCs</td>
<td>Bi-directional</td>
<td>VA↔︎VA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>El Paso HCS - NT/Cache - VMS/Cache</td>
<td>WBAMC DoD</td>
<td>Unidirectional</td>
<td>VA→DoD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Hines VAMC (BETA test site)</p>
<p>VMS/DSM - VMS/Cache</p></td>
<td>Naval Hospital Great Lakes</td>
<td>Unidirectional</td>
<td><p>DoD→VA</p>
<p>VA←VA</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Honolulu VAMC - NT/Cache</td>
<td>Tripler AMC DoD</td>
<td>Unidirectional</td>
<td>VA←DoD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Manchester VAMCVMS/Cache &amp; NT/Cache</td>
<td>VAMCs</td>
<td>Bi-directional</td>
<td>VA↔︎VA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Milwaukee VAMC VMS/DSM</td>
<td>VAMCs</td>
<td>Bi-directional</td>
<td>VA↔︎VA</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>North Chicago VAMC (BETA test site) VMS/DSM</td>
<td>Naval Hospital Great Lakes</td>
<td>Bi-directional</td>
<td>VA←DoD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Salt Lake City VAMC VMS/DSM</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>San Diego VAMC (ALPHA test site) VMS/DSM - VMS/Cache</td>
<td>Naval Medical Center San Diego DoD</td>
<td>Bi-directional</td>
<td>VA↔︎DoD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Upstate New York HCS VMS/DSM and VMS/Cache</td>
<td>VAMCs</td>
<td>Bi-directional</td>
<td>VA↔︎VA</td>
</tr>
</tbody>
</table>

## # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the guide addresses package or audience specific notations or directions (e.g., symbols used to indicate terminal dialogues or user responses).

## LEDI III Implementation and User Guide 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This user guide contains of the following sections:

Introduction: This section of the user guide supplies a brief statement identifying the document in terms of its purpose, scope, and targeted audience. It also provides an overview that describes the major functions and purpose of the software product, and how the software accomplishes the objects.

LEDI III Implementation Guide (Implementation Instructions): This section contains detailed instructions to successfully implement the LEDI III LDSI software product. IRM and LIM staff must perform LEDI III setup instructions in sequence. The setup instructions are listed in step-by-step order.

LEDI III User Guide (User of the Software): The LEDI III User Guide “Use of the Software” section contain information for END USERS to competently operate the software application using a task-oriented approach. Examples for using LEDI III LDSI software are provided in this section of the User Guide.

Glossary: This section provides terms relates to LEDI III software application and documentation:

### LEDI III Implementation and User Guide Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen Captures: The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

User Response: User entry response appears in boldface type Courier font, no larger than 10 points.

Example:Boldface typeReturn Symbol: User response to computer dialogue is followed by \<RET\> or \<ENTER\>symbol that appears in Courier font, no larger than 10 points, and bolded.

Example:\<RET\> or \<ENTER\>Tab Symbol: User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded.

Example:\<Tab\>

## LEDI III Software and Documentation Retrieval Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All facilities are encouraged to use File Transfer Protocol (FTP) capability. Use the FTP address “download.VistA.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

VistA LEDI III software, Installation Guide, and Implementation and User Guide are available at the following Office of Information Field Offices (OIFOs) on the ANONYMOUS.SOFTWARE directories:

| OI FIELD OFFICE                    | FTP ADDRESS                        | DIRECTORY                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

### LEDI III Software and Documentation Retrieval Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA LEDI III software and documentation files are exported in the following retrieval formats:

| FILE NAMES              | CONTENTS                                                 | RETRIEVAL FORMATS |
|-------------------------|----------------------------------------------------------|-------------------|
|                         |                                                          |                   |
| LAB_LEDI_III.KID        | LA\*5.2\*64 KIDS build                                   | ASCII             |
|                         | LR\*5.2\*286 KIDS build                                  | ASCII             |
|                         |                                                          |                   |
| LAB_LEDI_III_IG.PDF     | LABORATORY ELECTRONIC DATA INSTALLATION GUIDE            | BINARY            |
| LAB_LEDI_III_IMP_UG.PDF | LABORATORY ELECTRONIC DATA IMPLEMENTATION AND USER GUIDE | BINARY            |
|                         |                                                          |                   |
| LAB_LEDI_III_IG.DOC     | LABORATORY ELECTRONIC DATA INSTALLATION GUIDE            | BINARY            |
| LAB_LEDI_III_IMP_UG.DOC | LABORATORY ELECTRONIC DATA IMPLEMENTATION AND USER GUIDE | BINARY            |

### VistA Website Locations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA LEDI III Installation Guide (i.e., LAB_LEDI_III_IG.PDF and LAB_LEDI_III_IG.DOC) and LEDI III Implementation and User Guide (i.e., LAB_LEDI_III_IMP_UG.PDF and LAB_LEDI_III_IMP_UG.DOC) in Portable Document Format (PDF) and MS Word (DOC) Formats are available at the following VistA Intranet locations:

#### Laboratory Version 5.2 Home Page

<span class="mark">REDACTED</span>

#### VistA Documentation Library (VDL)

[www.va.gov/vdl/](http://www.va.gov/vdl/)

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Laboratory Universal Interface Patch LA\*5.2\*17-Patch LR\*5.2\*65 V. 1.0
- VA FileMan V. 21.0
- VA MailMan V. 7.1
- VistA Laboratory Health Level Seven (HL7) Interface Standard Specifications V. 1.2
- Health Level Seven Standard Version 2.3.1 © 1997 by the Health Level Seven, Inc.
- Health Level Seven Standard Version 2.2 © 1994 by the Health Level Seven, Inc.
Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran Integrated Service Network (VISN) mission is to consolidate electronic lab test ordering and lab test result reporting throughout all Veterans Affairs (VA) Health Care Facilities laboratories within a VISN, between VISNs, and non-VA organizations (i.e., commercial reference laboratories, Department of Defense (DoD), and etc.) without diminishing the quality of services in the patient medical care.

VistA Laboratory Electronic Data Interchange (LEDI) software application provided the new electronic messaging functionality for lab test ordering and result reporting between VA Health Care facilities laboratories. This electronic messaging functionality is based on the Health Level Seven (HL7) Version 2.3 and VistA Health Level Seven (HL7) Version 1.6 Standard Specifications. These specifications are used as the basis for defining VistA Laboratory Universal Interface (UI) and LEDI HL7 Interface Standard Specification Version 1.2. The following new electronic features and functionalities were implemented by the release of the VistA LEDI software application:

- Electronic Messaging
- Electronic Lab Test Ordering
- Electronic Lab Test Results Reporting
- Bar-code Specimen Accessioning
- Workload

### VistA Laboratory Electronic Data Interchange Phase III (LEDI III)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of the VistA LEDI III software enhancements involves the development of a bi-directional interface that allows VA and DoD facilities to be reference laboratories for each other. Laboratory test orders and results are transmitted via VA VistA systems using LEDI III for VA facilities and Laboratory Data Sharing and Interoperability (LDSI) software via DoD Composite Health Care System (CHCS) systems for DoD facilities. The VA/DoD LEDI III LDSI project was designed to determine a methodology that has the capacity and features necessary for sharing secure encrypted laboratory data between the two agencies. This patch adds support for sending/receiving LEDI orders/results between VA and DoD facilities and implements enhancements to general LEDI functionality. The exchange of clinical chemistry laboratory data between VA and DoD facilities is a process of data transmission between VistA and CHCS systems using the HL-7 messaging protocol over a TCP/IP connection utilizing a secure Virtual Private Network (VPN)/firewall.

#### DoD as Reference Laboratory (Host Laboratory)

The VA medical center using the VistA Laboratory LEDI software creates a HL7 formatted electronic order message. The order message contains all required patient information that indicates to the DoD HOST Laboratory CHCS system what procedures are to be performed. The order message contains the patient’s demographics (patient’s name, social security number, patient’s location, and ordering physician) as well as the test information. The LEDI software hands the HL7 formatted message to the VistA HL7 software for delivery to the DoD HL7 server. The DoD HL7 server processes the VA COLLECTING facilities order message. The DoD HOST laboratory performs the analytical test procedures generating tests results. The test result are verified and released in CHCS by authorized laboratory personnel. The DoD HOST laboratory creates an HL7-formatted message containing result information, and sends the message to the VA COLLECTING laboratory’s VistA HL7 server. The VA COLLECTING laboratory VistA HL7 server accepts and processes the HL7 message. The HL7 server then passes the message to the LEDI software for further processing. The VistA LEDI III software then stores the electronic result message to be accepted by VA medical laboratory personnel. The submitting laboratory technicians/technologists review the results on the screen for completeness and clinical believability. If the results are acceptable, the submitting laboratory personnel will certify them and record them in the patient’s electronic clinical record.

#### VA as Reference Laboratory (Host Laboratory)

A DoD medical facility using the CHCS and LSDI software creates a HL7 formatted electronic order message. The order message contains all required patient information that indicates to the VA HOST laboratory VistA system what procedures are to be performed. The order message contains the patient’s demographics (patient’s name, social security number, patient’s location, and ordering physician) as well as the test information. The CHCS LSDI software hands the HL7 formatted message to the CHCS HL7 software for delivery to the VA VistA HL7 server. The VA VistA HL7 server processes the DoD COLLECTING sites order message. The VA HOST laboratory performs the analytical test procedures generating tests results. The test result are verified and released in VistA by authorized laboratory personnel. VA HOST laboratory creates an HL7-formatted message containing result information, and sends the message to the DoD COLLECTING laboratory’s HL7 server. The DoD COLLECTING Laboratory HL7 server accepts and processes the HL7 message. The HL7 server then passes the message to the LSDI software for further processing. The LSDI software then stores the electronic result message to be accepted by the DoD medical laboratory personnel. The submitting laboratory technicians/technologists review the results on the screen for completeness and clinical believability. If the results are acceptable, the submitting laboratory personnel will certify them and record them in the patient’s electronic clinical record.

## LEDI III Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enhancements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NOTES: With this release of LEDI, the verification, release and storage in VistA of laboratory test results for “CH” subscript tests has been changed as follows:

- Laboratory result verification has been enhanced to allow the designation of a performing laboratory and the use of the performing laboratory's units, normals, and normalcy status in results reporting.

> User during the verification process is able to specify the performing laboratory. The performing laboratory is selected from the list of available entries in the site’s INSTITUTION file (#4). The selection of entries is screened as follows:

> a\. User can select the division they are logged on.

> b\. User can select an institution that is configured in the LAB SHIPPING CONFIGURATION file (#62.9) as a host facility with their division as the COLLECTING facility.

> During acceptance and verification of results received from a reference laboratory via an HL7 interface (LEDI), the performing laboratory, results, units, normals and normalcy status contained in the HL7 message are stored “as is”.

- Users using the Enter/verify/modify data (manual) \[LRENTER\] option to enter results manually from a reference laboratory can use the units and normals specified in LABORATORY TEST file (#60) by configuring USE FOR REFERENCE TESTING field (#13) within the SITE/SPECIMEN subfile (#100).

> If this field is not enabled for reference laboratory result data entry, then the user is prompted for units, normals, high and low reference ranges to store with the results. The Edit atomic tests \[LRDIEATOMIC\] option allows Laboratory Information Manager (LIM) to designate this functionality for affected tests.

- Amended reports received via a LEDI HL7 interface can be processed via the Enter/verify/modify data (manual) option \[LRENTER\].
- Test result normals and units for all verified tests are now stored with the results in LAB DATA file (#63). Changes to units and normals can now be made to existing tests in LABORATORY TEST file (#60) without affecting previously reported results.

However, there are potentially situations, which do not allow this feature to be implemented for a specific test. If a site has old results or has never archived then there may be results stored under a data name with no normals/units etc., which were entered using previous versions of the Laboratory package. When test results in LAB DATA file \#63 are found with no unit and/or normals the software goes back to LABORATORY TEST file \#60 to retrieve these values. Changing the units and/or normals associated with a File \#63 data name in File \#60 would alter the units/ and/or normals reported on previous results.

*1. General LEDI Functionality*

- The process of building orders in the LAB PENDING ORDERS ENTRY file (#69.6) is enhanced to use additional information from the HL7 Order (ORM) message. This new functionality will store comments and other test results that accompany an order in the LAB PENDING ORDERS ENTRY file (#69.6).
- Added the new Start a Shipping Manifest \[LA7S MANIFEST START\] option, which allows a manifest to be started without performing a manifest build. Specimens can then be added manually, instead of automatically, using the Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option.
- Added the new Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option which is used to enter relevant clinical information that should accompany a test order on a manifest.
- Enhanced routine LA7VHL to call HL7 supported API.
  - Enhanced routine LA7VMSG1 to check if \$QUERY of ^TMP global has returned a null value. Under certain conditions an illegal function call error could be observed Enhanced routine LA7VLL, LA7VSTP, and LA7VSTP1 to setup LA7V\* logical links without \<space\> between "LA7V" and station number. Allows HL7 package to display logical links for DoD sites which utilize DoD DMIS ID codes as facility identifiers similar to VA station numbers. HL7 package only displays first 8 characters of logical link name. Option LEDI Setup \[LA7V SETUP\] will only support creation of TCP logical links. When setting up LEDI between VA facilities the software will default to using TCP/IP via the standard HL package logical links VAxxx.
  - Enhanced routine LA7PURG to purge shipping manifests from LAB SHIPPING MANIFEST file (#62.8) when all related accessions have been purged from ACCESSION file (#68) (E3R \#18036). Orders in the LAB PENDING ORDERS ENTRY file (#69.6) are purged when the date completed is \>365 days, when the order transmitted date is \>720 days or when the order transmitted date is \>360 and the order status is Results/data Received.
  - Enhanced the display of manifest list in inverse order
  - Enhanced shipping manifest to add requesting provider's contact information.
  - Added four new alerts/mail bulletins

  
*2. Laboratory Result Verification*

- Enhanced verification process to specify the performing laboratory.
- Enhanced results from reference lab to store test results “as is”
- Enhanced receipt of amended reports to generate a Mail Man bulletin.
- Enhanced amended reports to be processed via the EM Enter/verify/modify data (manual) \[LRENTER\] option.
- Enhanced the system to add units and normal values specified in File \#60
- Enhanced the evaluation of normalcy status dealing with results of zero.
- Enhanced audit trail normalcy status change triggers audit trail comments.
- Enhanced verification process to display ordering provider's phone and pager information.
- Enhanced CPRS GUI lab results display to include units and normal values –Display of lab results in CPRS GUI and Laboratory Interim Reports has been modified to display units and normals associated with results at time of verification. Results that are derived from a Set of Codes will be reported using the external form of the code.
- Enhanced CPRS GUI display to include the performing laboratory.
- Enhanced EA and EM options to display patient information - Enter/verify data (auto instrument) \[LRVR\] and Enter/verify/modify data (manual) \[LRENTER\] options will display patient information from field PAT. INFO. (#.091) in LAB DATA file (#63), patient’s sex and age at time of specimen collection date/time during result verification.
- Enhanced result alignment to display right-justified.
- Enhanced routine LRWLST1 to check and set the ACCESSION file (#68) DATE sub-file's zero nodes via FileMan DBS call.
- Enhanced routine LRWLST1 to determine treating specialty

### Modifications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modified routine LR7OB63 to correct trimming leading and trailing spaces but leave embedded spaces when displaying lab test results.
- Modified routine LR7OR2tocorrect trimming leading and trailing spaces but leave embedded spaces when displaying lab test results.
- Modified Referral Patient Multi-purpose Accession option to check pending orders.
- Modified EM option to allow entering verifier’s initials in mixed case.
- Modified LRWLST11 to store the correct ordering and collecting sites.
- Modified routine LR7OGMP to increase the space allocated on display
- Modified display of results using the external value for set of codes data types.
- Modified supported API call \$\$FMDATE^HLFNC to recommended Kernel supported API's \$\$HL7TFM^XLFDT and \$\$FMTHL7^XLFDT respectively.
- Modified supported API call \$\$HLDATE^HLFNC to recommended Kernel supported API's \$\$HL7TFM^XLFDT and \$\$FMTHL7^XLFDT respectively.
- Modified input transform of DATE/TIME OF MESSAGE field (#106) in LA7 MESSAGE QUEUE file (#62.49) to use Kernel supported API \$\$HL7TFM^XLFDT instead of \$\$HLDATE^HLFNC.
- Modified routine LA7VHL to call HL7 supported RSPINIT^HLFNC2 to obtain message delimiters that HL7 package will use when building MSH header of application acknowledgement message. Previous call to INIT^HLFNC2 would return incorrect headers under certain conditions.

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files were modified in support of the LEDI III software application enhancement release:

### LABORATORY TEST file (#60)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LABORATORY TEST file (#60), SITE/SPECIMEN sub-file (#100) has been modified to support the use of the local laboratory test units and normals for the reference laboratory results. The new USE FOR REFERENCE TESTING field (#60.01,13) has been added to this sub-file.

#### New Field:

#### USE FOR REFERENCE TESTING field (#60.01,13)

This new field supports the manual entry of reference laboratory test results and source of normals to apply to test result and indicates when the reference ranges and units associated with this specimen type can be used when manually entering results of testing performed at another laboratory.

### TOPOGRAPHY FIELD file (#61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been modified to only allow mapping to HL7 Table specimen source codes.

#### Modified Field: 

#### LEDI HL7 field (#61,.09)

This field has been modified to only allow selection of codes that have an associated HL7 code from table 0070. This field contains the standard HL7 specimen type code and Limits the selection of only Specimen type codes with approved HL7 specimen codes.

### AUTO INSTRUMENT file (#62.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file is modified in support of processing Electronic Result Messages. The following new field is site-configurable using the LEDI Setup \[LA7V SETUP\] option:

### #### Renamed Field: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NOTIFY ABNORMAL FLAGS field (# 22)

The existing STORE ABNORMAL FLAGS field (# 22) has been renamed to NOTIFY ABNORMAL FLAGS field (# 22) to meet the CAP requirements for HL7 messages received from reference labs that will always use/store abnormal flags sent by the producer of results. This renamed field is used to determine if an alert and bulletin should be created when results are processed with an associated abnormal flag. It also allows sites to be notified by alert/mail bulletin when results are abnormal.

### LA7 MESSAGE LOG BULLETINS file (#62.485)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III software application uses the following error code numbers to build the text of the error message. This file has been changed to add two new codes and to modify one existing code. The existing CODE 28 text field has been modified and/or the build logic changed.

#### Modified Code:

#### CODE: 28:

TEXT: Msg \# \|1\| encountered the following HL7 generation error: \|2\|.

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=\$G(LA7X(1)),LA7TXT(2)=\$G(LA7X(2))

#### New Codes:

#### CODE: 46:

TEXT: Msg \# \|1\|, 'PID' segment was not found, message processing aborted.

SEND ALERT: YES BUILD LOGIC: S LA7TXT(1)=LA76249

#### CODE: 47:

A new error bulletin \#47 has been added to LA7 MESSAGE LOG BULLETINS file (#62.485). When processing LEDI orders if any of the following are incomplete - local test, local urgency, local topography or local collection sample then the bulletin will be triggered. This is to insure that orders sent by the collecting facility are not missed when processed during LEDI Referral Patient Accessioning. If this bulletin is triggered it indicates that the host site's shipping configuration is not properly configured to process orders from its collecting site.

TEXT: Msg \# \|1\| - the \|2\| order for \|3\| has \|4\|

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=\$G(LA76249),LA7TXT(2)=\$G(LA7OTST),LA7TXT(3)=\$G(LA7PNM),LA7TXT(4)=\$G(LA7X)

#### CODE: 48:

TEXT: Message \#\|1\| was rejected because \|2\|

SEND ALERT: YES

BUILD LOGIC: S LA7TXT(1)=LA76249,LA7TXT(2)=\$G(LA7MSATM)

### LA7 MESSAGE QUEUE file (#62.49*)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been changed to include two new fields and one modified field that are used to store internal information regarding the HL7 environment that existed when a message was received and send that corrected results messages.

#### Modified/New Fields:

#### #### HL7 ENV field (# 700)

This new HL7 ENV field (# 700) stores information regarding HL7 message internal entry numbers (IEN), HL7 protocol, and HL7 application to enable the Laboratory software to call the HL7 package reprocessing and purge/no purge API's.

#### CH SUBSCRIPT field (#62.49162,.01)

The CH SUBSCRIPT sub-file (# 162) existing CH SUBSCRIPT field (#62.49162,.01) has been modified to correct spelling errors in the field description. This multiple field contains the "CH" subscript node where the results are stored in the LAB DATA file (#63). The field is used in the processing and transmission of HL7 result messages.

#### CORRECTED RESULTS field (# 62.49162,.02)

The CH SUBSCRIPT sub-file (# 162) contains the new CORRECTED RESULTS field (# 62.49162,.02). This new field is use to flag HL7 ORU messages when results have been amended. The HL7 message will indicate the status when transmitting these results.

### LAB SHIPPING MANIFEST file (#62.8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been modified to add the following new fields. These new fields allow support for non-HL7 specimen coding systems. This field support VA/DoD Laboratory Interoperability (Lab Interop) by providing support for DoD’s test, specimen and collection sample coding system:

#### New and Modified Fields: 

#### SPECIMEN CODING SYSTEM field (#62.8,.06)

This new SPECIMEN CODING SYSTEM field (#62.8,.06) allows VistA to function with DoD CHCS system which does not use HL7 standard table 0070. When orders are sent to a non-VA facility and the facility cannot receive HL7 specimen codes from HL7 table 0070 then answer with the type of coding system "LOCAL".

#### SPECIMEN CODING SYSTEM field (#62.8,.060;6)

This new SPECIMEN CODING SYSTEM field (#62.8,.060;6) is used if orders are sent to a non-VA facility and the facility cannot receive HL7 specimen codes from HL7 table 0070 then answer with the type of coding system "LOCAL".

#### #### RELEVANT CLINICAL INFORMATION (#62.801,.1)

This new RELEVANT CLINICAL INFORMATION field (#62.801,.1) allow sites to specify information that needs to accompany a HL7 ORM order message. This field contains additional clinical information about the patient or specimen. It is used to report the suspected diagnosis and clinical findings on requests for interpreted diagnostic studies.

#### NON-NLT TEST ORDER CODE (#62.801,5.1)

This field name was modified to accommodate DBA request. If sending test orders to a non-VistA facility this field is used to store the test order codes used by the non-VistA system. It is valued by VistA from the corresponding field in LAB SHIPPING CONFIGURATION file (#62.9) during shipping manifest building.

NON-NLT TEST ORDER NAME (#62.801,5.2)

This field name was modified to accommodate DBA request. If sending test orders to a non-VistA system this field is used to store the test order name used by the non-VistA system. It is valued VistA from the corresponding field in LAB SHIPPING CONFIGURATION file (#62.9) during shipping manifest building.

#### NON-HL7 SPECIMEN CODE field (#62.801,5.3)

This new NON-HL7SPECIMEN CODE field (#62.801,5.3) is used when sending test orders to a non-VA facility that does not use HL7 Table 0070 Specimen Source, use this field to store the specimen code used by the non- VISTA system. It is only used when the value of SPECIMEN CODING SYSTEM field (#.06) is LOCAL-NON HL7. It provides a means for a collecting facility to map non standard specimen codes to the host site. This is a free text field.

#### NON-HL7 SPECIMEN NAME field (#62.801, 5.4):

This new NON-HL7 SPECIMEN NAME field (#62.801,5.4) is use when sending test orders to a non-VA facility that does not use HL7 Table 0070 Specimen Source, use this field to store the specimen name used by the non- VISTA system. It is only used when the value of SPECIMEN CODING SYSTEM field (#.06) is LOCAL-NON HL7. It provides a means for a collecting facility to map non standard specimen names to the site's TOPOGRAPHY FIELD file (#61). This is a free text field.

#### NON-NLT TEST CODING SYSTEM field (#62.801,5.5):

If sending test orders to a non-VistA system use this new field to store the name of the coding system used by the non-VistA system. It will be used when the TEST CODING SYSTEM field (#.14) is set to "NON-VA". Name usually begins with "99" to indicate a local coding system in the HL7 Standard.

#### NON-HL7 SPECIMEN CODING SYSTEM field (#62.801,5.6)

This new NON-HL7 SPECIMEN CODING SYSTEM field (#62.801,5.6) is use when sending test orders to a non- VistA facility that does not use HL7 Table 0070 Specimen Source. Use this field to store the name of the coding system used by the non-HL7 system. It will be used when the value of the SPECIMEN CODING SYSTEM field (#.06) is set to LOCAL-NON HL7. Name usually begins with "99" to indicate a local coding system in the HL7 Standard. This is a free text field.

#### COLLECTION SAMPLE CODE field (#62.801,5.7):

This new COLLECTION SAMPLE CODE field (#62.801,5.7) is use when sending test orders to a non-VistA facility that also requires a collection sample code use this field to store the collection sample code used by the non-VistA system. It is only used when the value of the SPECIMEN CODING SYSTEM field (#.15) is set to LOCAL-NON HL7. This is a free text field.

#### #### COLLECTION SAMPLE NAME field (#62.801,5.8):

The new COLLECTION SAMPLE NAME field (#62.801,5.8) is use when sending test orders to a non-VistA facility that requires a collection sample name. This new field is used to store the collection sample name used by the non- HL7 system. It is only used when the value of the SPECIMEN CODING SYSTEM field (#.06) is set as LOCAL-NON HL7. This is a free text field.

#### COLLECT SAMPLE SYSTEM field (#62.801,5.9)

This new COLLECT SAMPLE SYSTEM field (#62.801,5.9) is use when sending collection sample codes/names to a non-VistA facility. Use this field to store the name of the coding system used by the non- VistA system. This field is used when the TEST CODING SYSTEM field (#.14) is set to "NON-VistA". The name usually begins with "99" to indicate a local coding system in the HL7 Standard. This is a free text field.

#### INVOICE filed (#.01).

This field is modified to add the new –style cross-reference “C”. This cross-reference allows for lookup and display of shipping manifests in inverse order by providing reverse x-ref for shipping manifest invoices.

### LAB SHIPPING CONFIGURATION file (#62.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file contains the following modified/new fields. These fields are designed to support VA/DoD Lab Interop that allows VA facilities to handle DoD coding systems.

#### Modified/New Fields: 

#### COLLECTING FACILITY'S SPEC ID field (# .05)

This existing COLLECTING FACILITY'S SPEC ID field (# .05) was modified to correct a spelling error in the set of codes.

#### #### OTHER SYSTEM IDENTIFIER field (# .11)

This existing OTHER SYSTEM IDENTIFIER field (# .11) was modified to added additional information in the field description.

#### #### SPECIMEN CODING SYSTEM field (# .15)

This existing SPECIMEN CODING SYSTEM field (# .15) was modified to added additional information to the help prompt and field description.

#### NON-NLT TEST ORDER CODE field (# 62.9001, 5.1)

This field name was modified to accommodate DBA request. If sending test orders to a non-VistA system this field is used to store the test order codes used by the non-VistA system.

NON-NLT TEST ORDER NAME (# 62.9001, 5.2)

This field name was modified to accommodate DBA request. If sending test orders to a non-VistA system this field is used to store the test order name used by the non-VistA system.

#### NON-HL7 SPECIMEN CODE field (# 62.9001, 5.3)

This existing NON-HL7 SPECIMEN CODE field (# .9001, 5.3) was modified to added additional information to the field description.

#### NON-HL7 SPECIMEN NAME field (# 62.9001, 5.4)

This existing NON-HL7 SPECIMEN NAME field (# .9001, 5.4) was modified to added additional information in field description.

#### NON-NLT TEST CODING SYSTEM field (# 62.9001, 5.5)

COLLECTING facilities: This new NON-NLT TEST CODING SYSTEM field (# 62.9001, 5.5) is used when sending test orders to a non- VistA facility. This new field is also used to store the name of the coding system used by the non- VISTA system. It is used when the TEST CODING SYSTEM field (#.14) is set to "NON-VistA." The name usually begins with "99" to indicate a local coding system in the HL7 Standard.

HOST facilities: When receiving test orders from a non-VISTA collecting facility that does not use VA NLT codes, use this new field to store the name of the coding system used by the non-VistA system. It is used when the TEST CODING SYSTEM field (#.14) is set to "NON-VistA". The name usually begins with "99" to indicate a local coding system in the HL7 Standard.

#### NON-HL7 SPECIMEN CODING SYSTEM field (# 62.9001, 5.6)

This new NON-HL7 SPECIMEN CODING SYSTEM field (# 62.9001, 5.6) is used when sending test orders to a non-VistA facility that does not use HL7 Table 0070 Specimen Source. Use this new field to store the name of the coding system used by the non-VistA system. This field is used when the value of the SPECIMEN CODING SYSTEM field (#.15) is set to LOCAL-NON HL7. The name usually begins with "99" to indicate a local coding system in the HL7 Standard.

HOST Facilities: If receiving test orders from a non-VistA facility that does not use HL7 Table 0070 Specimen Source, use this field to store the name of the coding system used by the non- VistA system. It will be used when the TEST CODING SYSTEM field (#.14) is set to "NON- VistA." The name usually begins with "99" to indicate a local coding system in the HL7 Standard.

#### #### COLLECTION SAMPLE CODE field (# 62.9001, 5.7)

COLLECTING facilities: This new COLLECT SAMPLE CODE field (# 62.9001, 5.7) ) is used when sending test orders to a non-VISTA facility that also requires a collection sample code use this field to store the collection sample code used by the non-VISTA system. It is only used when the value of the SPECIMEN CODING SYSTEM field (#.15) is set to LOCAL-NON HL7.

HOST facilities: used to map collecting facility's "MI" subscript test's collection sample to host site's collection sample.

#### #### COLLECTION SAMPLE NAME field (#62.9001,5.8)

COLLECTING facilities: If sending test orders to a non-VISTA facility that also requires a collection sample name use this field to store the collection sample name used by the non-VA system. It is only used when the value of the SPECIMEN CODING SYSTEM field (#.15) is set to LOCAL-NON HL7.

HOST facilities: used to map collecting facility's "MI" subscript test's collection sample to host site's collection sample.

#### #### COLLECT SAMPLE SYSTEM field (#62.9001,5.9)

COLLECTING facilities: If sending collection sample codes/names to a non-VISTA facility use this field to store the name of the coding system used by the non- VISTA system. This field is used when the TEST CODING SYSTEM field (#.14) is set to "NON-VISTA". The name usually begins with "99" to indicate a local coding system in the HL7 Standard.

HOST facilities: Used this field to map the collecting facility's "MI" subscript test's collection sample to the host site's collection sample.

### LOAD/WORK LIST (#68.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been modified to allow site to specify a default reference laboratory for a specific load/list profile.

#### New Field: 

#### DEFAULT REFERENCE LABORATORY field (#2.3)

The PROFILE sub-file (# 50) has been modified to include the new DEFAULT REFERENCE LABORATORY field (#2.3). This new field specifies the default performing laboratory that is commonly associated with this profile. It will be presented as the default performing laboratory when a user is setting up a verifying session using this profile.

### ### LAB PENDING ORDERS ENTRY file (#69.6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been changed to add one new field and modifications to four existing fields in support of the LEDI III software enhancements.

#### New Field: 

#### RACE field (#69.6,.06)

This new RACE field (#69.6,.06) supports the race received via HL7 message and stores the patient's race using HL7 code and text.. It is also used to populate corresponding existing field in the REFERRAL PATIENT file (#67) when specimens are accessioned.

#### Modified Fields: 

#### PAT ID field (#69.6,.09)

This existing PAT ID field (#69.6,.09) was modified to increase the field length to 5-30 characters. This is a free text field.

#### ORDERING SITE ACC \# (#69.6,3.2)

This existing ORDERING SITE ACC \#, field (#69.6,3.2) was modified to increase the field length 1-20 characters. This is a free text field.

#### HL PID-2 field (#69.6,700.02)

This existing HL PID-2 field (#69.6,700.02) stores the placer's patient identification information from PID-2 for transmittal back to the placer when the order is completed. This field was modified to increase the field length 1-250 characters. This is a free text field.

#### HL PID-4 field (#69.6,700.04)

This existing HL PID-4 field (#69.6,700.04) stores the placer's patient identification information from PID-4 for transmittal back to the placer when the order is completed. This field was modified to increase the field length 1-250 characters. This is a free text field

### LEDI III New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three new options were created to accommodate LEDI III new functionality:

1. Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option

The new Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option is used to enter relevant clinical information that should accompany a test order on a manifest. This new option is located on the Lab Shipping Menu \[LA7S MAIN MENU\], located on the Laboratory DHCP Menu \[LRMENU\].

2. Start a Shipping Manifest \[LA7S MANIFEST START\] option

The new Start a Shipping Manifest \[LA7S MANIFEST START\] option will allow a manifest to be started without performing a manifest build. Specimens can then be added manually, instead of automatically, using the existing Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option. This new option is located on the Lab Shipping Menu \[LA7S MAIN MENU\], located on the Laboratory DHCP Menu \[LRMENU\].

3. General Lab User Parameters \[LR USER PARAM\] option

The new General Lab User Parameters \[LR USER PARAM} option allows a user to modify various user selectable parameters used with the laboratory package. This new option is located on the Information-help menu \[LRHELP\].

### Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following 22 options were modified to accommodate LEDI III new functionality:

#### Edit Shipping Configuration \[LA7S EDIT 62.9\] option 

This option has been modified to support laboratory testing with DoD facilities. It allows the entering of non-HL7 specimen and collection sample codes, Non-VA test codes used by DoD facilities.

#### Print Shipping Manifest \[LA7S MANIFEST PRINT\] option

This option has been modified to print additional information on the manifests. Requesting provider's office phone, voice and digital pager numbers, and specimen container will be printed on working copies of shipping manifest. Manifests used for shipping documents will have relevant clinical information printed. (See the new Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO option).

#### #### Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\] option

This option has been modified to print ordering provider.

#### Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option

This option has been modified to purge shipping manifests from LAB SHIPPING MANIFEST file (#62.8) when all related accessions have been purged from ACCESSION file (#68). Orders in the LAB PENDING ORDERS ENTRY file (#69.6) are purged when the date completed is \>365 days, when the order transmitted date is \>720 days or when the order transmitted date is \>360 and the order status is Results/data Received

#### LEDI Setup \[LA7V SETUP\] option

This option has been modified to setup LA7V\* logical links without \<space\> between "LA7V" and station number. Allows HL7 package to display logical links for DoD sites which utilize DoD DMIS ID codes as facility identifiers similar to VA station numbers. HL7 package only displays first 8 characters of logical link name. Option LEDI Setup \[LA7V SETUP\] will only support creation of TCP logical links.

#### Enter/verify data (auto instrument) \[LRVR\] option

This option has been modified to display patient information from the PAT. INFO. field (#.091) in LAB DATA file (#63) during result verification. When verifying results from a reference laboratory using Enter/verify data (auto instrument) \[LRVR\] option any test results that have not been verified will be displayed to the user after verification. The display will list the test names, results, abnormal flags and units if available. This display will list the test(s) as not reviewed. This may indicate that additional or reflex testing has been added by the reference laboratory. These additional tests may need to be added to the accession to process these results.

#### Enter/verify/modify data (manual) \[LRENTER\] options 

This option contains the following modifications:

- This option now displays patient information from the PAT. INFO. field (#.091), in LAB DATA file (#63) during result verification.
- When using this option to amend previously released results user can now enter their verifying initials in mixed case. (E3R \#13408)
- A defect was reported during lab result verification using which caused the previous patient demographics to be displayed when entering results on an accession. If the previous selected accession was in an uncollected state the option was skipping the uncollected accession and incrementing the default accession number to the next available accession. If the user selects this or another accession the patient demographics of the selected accession were not being displayed. Instead the patient demographics of the uncollected accession were displayed. The Enter/verify/modify data (manual) \[LRENTER\] option has been modified to display the patient demographics of the currently selected accession.

#### Referral Patient Multi-purpose Accession \[LR LEDI\] option

The Referral Patient Multi-purpose Accession \[LR LEDI\] option contains the following three modifications:

- This option was prompting user for CPRS Nature of Order which is not used during accessioning of non-PATIENT file (#2) patients. It has been modified to only prompt user for CPRS Nature of Order when accessioning a patient from the PATIENT file (#2).
- This option has been modified to check for pending orders when performing accessioning without a bar code scanner.
- This option has been modified to display to user and store order comments that accompanies electronic orders with order in LAB ORDER ENTRY file (#69).

#### Interim report \[LRRP2\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

10. Interim report by provider \[LRRD\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### #### Interim report for chosen tests \[LRRP3\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### Interim report for selected tests as ordered \[LRRSP\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### Interim reports by location (manual queue) \[LRRS\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### #### Interim reports for 1 location (manual queue) \[LRRS BY LOC\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### Interim reports for 1 provider (manual queue) \[LRRD BY MD\] option

This option has been modified to display month portion of date/times using the three letter abbreviation instead of the two number designations to eliminate potential confusion with day portion of dates. Time is displayed using 24 hour time format.

#### Enter/verify data (auto instrument) \[LRVR\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### Enter/verify data (Load list) \[LRVRW2\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### #### Enter/verify/modify data (manual) \[LRENTER\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### Enter/verify data (Work list) \[LRVRW\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### #### Fast Bypass Data Entry/Verify \[LRFASTS\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### Bypass normal data entry \[LRFAST\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

#### Batch data entry (chem, hem, tox, etc.) \[LRSTUF\] option

This option has been modified because during verification of laboratory results comments for a previous result are displayed, along with the previous result, when entering results manually or by automated instrument for user-selected tests. Users can indicate which tests should have previous test comments displayed during verification by flagging the test using option General Lab User Parameters \[LR USER PARAM\] located on the Information-help menu \[LRHELP\].

![](la-5-2-64-lr-5-2-286-ledi-iii-implementation-and-user-guide/002.png)

LEDI III Implementation Guide

# LEDI III Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains detailed instructions to successfully implement the LEDI III software application. IRM and LIM staff must perform LEDI III setup instructions in sequence. The setup instructions are listed in step-by-step order.

> **NOTE:** A checklist is provided at the end of this implementation section to ensure that LEDI III implementation process has been completed as instructed in this section.

NOTES: With this release of LEDI, the verification, release and storage in VistA of laboratory test results for “CH” subscript tests has been changed as follows:

- Laboratory result verification has been enhanced to allow the designation of a performing laboratory and the use of the performing laboratory's units, normals, and normalcy status in results reporting.

> User during the verification process is able to specify the performing laboratory. The performing laboratory is selected from the list of available entries in the site’s INSTITUTION file (#4). The selection of entries is screened as follows:

> a\. User can select the division they are logged on.

> b\. User can select an institution that is configured in the LAB SHIPPING CONFIGURATION file (#62.9) as a host facility with their division as the COLLECTING facility.

> During acceptance and verification of results received from a reference laboratory via an HL7 interface (LEDI), the performing laboratory, results, units, normals and normalcy status contained in the HL7 message are stored “as is”.

- Users using the Enter/verify/modify data (manual) \[LRENTER\] option to enter results manually from a reference laboratory can use the units and normals specified in LABORATORY TEST file (#60) by configuring USE FOR REFERENCE TESTING field (#13) within the SITE/SPECIMEN subfile (#100).

> If this field is not enabled for reference laboratory result data entry, then the user is prompted for units, normals, high and low reference ranges to store with the results. The Edit atomic tests \[LRDIEATOMIC\] option allows Laboratory Information Manager (LIM) to designate this functionality for affected tests.

- Amended reports received via a LEDI HL7 interface can be processed via the Enter/verify/modify data (manual) option \[LRENTER\].
- Test result normals and units for all verified tests are now stored with the results in LAB DATA file (#63). Changes to units and normals can now be made to existing tests in LABORATORY TEST file (#60) without affecting previously reported results.

> However, there are potentially situations, which do not allow this feature to be implemented for a specific test. If a site has old results or has never archived then there may be results stored under a data name with no normals/units etc., which were entered using previous versions of the Laboratory package. When test results in LAB DATA file \#63 are found with no unit and/or normals the software goes back to LABORATORY TEST file \#60 to retrieve these values. Changing the units and/or normals associated with a File \#63 data name in File \#60 would alter the units/ and/or normals reported on previous results.LEDI III Menus and Options Assignments

The following menus and options are exported via the LEDI III software release:

- Lab Shipping Management Menu \[LA7S MGR MENU\] should be assigned to the LIM.
- Electronic Catalog Menu \[LA7S CATALOG MENU\] should be assigned to the LIM.
- Lab Shipping Menu \[LA7S MAIN MENU\]) should be assigned to the Lab User.
- Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] is not assigned.
- Lab Universal Interface Menu \[LA7 MAIN MENU\] should be assigned to the LIM.
- Accessioning Menu \[LR IN\] should be assigned to the Lab User.

### LEDI III Two-Part Implementation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI III software application requires the following two-part implementation setup:

COLLECTION facility:

The COLLECTION facility laboratories must be setup to perform the following:

- Create an electronic Shipping Manifest (i.e., specifying lab tests to be performed by the receiving host facility laboratory).
- Transmit the Shipping Manifest to the host facility laboratory.
- Transport the specimens to the host facility laboratory.

HOST facility:

The HOST facility laboratories must be setup to perform the following:

- Receive the electronic Shipping Manifest List (transmitted by the collection facility laboratory).
- Accession the shipping manifest upon specimen arrival at the host facility either by scanning the manifest bar codes or manually selecting the electronic orders.
- Perform the specified lab tests and verifies the lab test results.
- Transmit lab test results back to the collection facility.

#### COLLECTION facility – VA to DoD Laboratory Implementation Instructions

LEDI III software instructions must be coordinated by the IRM and LIM staffs and performed in sequence for a successful implementation.

> **NOTE:** When implementing this interface with a DoD facility consult the LDSI National Implementation Plan for guidance to establish communication with the DoD facility via the VA/DoD VPN.

1. IRM: INSTITUTION file (#4) Setup Instructions

> Load the DoD DMIS ID codes into your INSTITUION file (#4) using the Load DMIS ID's \[XUMF DMIS ID LOAD\] option installed by Kernel patch XU\*8.0\*261. LEDI software uses the following four fields from the INSTITUION file (#4). Check both the HOST and COLLECTION institutions.

- Name Field (#.01): The Institution Master File maintains nationally controlled entries for VA and DoD facilities.
- Agency code Field (#95): This field indicates to the LEDI III software whether the facility is a VA or DoD facility
- VA facilities should be set to:‘VA’
- DoD facilities should be set to:

> ‘AF’ - AIR FORCE

> ‘ARMY’ - ARMY

> ‘N’ – NAVY

- Station Number Field (#99): For VA facilities
- Identifier (#9999): For DoD facilities indicate the DMIS ID for this facility

2\. IRM: Use Mail Group Edit \[XMEDITMG\] option to create the following LEDI-related mail group(s)

> A local mail group for the NEW RESULTS Alert: Notifies members when the Lab Universal Interface software has processed an HL7 message containing test results. An example of this information type of alert is, “Lab Messaging – New results received for LA7V HOST 578.” Note: It is recommended that the LIM be made coordinator of this mail group.

> Local mail group for the ERROR ON MESSAGE Alert: Notifies members of error conditions encountered during the processing of a Laboratory HL7 message. If preferred, the LAB MESSAGING mail group is recommended for this function. Note: It is recommended that the LIM be a member of this mail group also. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action. The members of this mail group should, at the minimum, include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.

1. LIM: Setup Lab Test Files to send specimens to HOST facility laboratory

> Contact the reference laboratory to acquire the following information:

- Specimen collection requirements
- Specimen handling/minimum requirements
- Alternate specimen (if any)
- Stability (for shipping conditions)
- Patient prep instructions
- Schedule of testing and TAT
- Order code to order the tests
- Exact test name for Non-VA test name
- DoD specimen code and name for each test
- DoD collection sample code and name for each test
- List of tests for panel tests
- Result code(s) used to report the results
- Normal Range and Critical Values
- Units of measure

> Edit LABORATORY TEST file (#60) to send specimens to the HOST facility laboratory. New lab test can be created to match the HOST facility requirements, or existing labs may be utilized IF the entries are compatible with the HOST facilities requirements.

> Create a Load List to define and accept lab test results transmitted by the HOST facility lab. The Load List must contain ALL lab tests that are processed by the HOST facility lab.

2. LIM: Setup the Lab Shipping Files

> Use the Lab Shipping Management \[LA7S MGR MENU\] Menu, located on the Lab Liaison \[LRLIAISON\] Menu to configure the following four files in the order listed in the instructions below:

> First – SHIPPING METHOD file (#62.92)

> Second - LAB SHIPPING CONDITION file (#62.93)

> Third - LAB SHIPPING CONTAINER file (#62.91)

> Fourth - LAB SHIPPING CONTAINER file (#62.91)

NOTES: The first three files may already be set up IF a VA to VA interface exists for your facility. Online help is available by entering two question marks (??) at the field prompt.

> a. The SHIPPING METHOD file (#62.92) is use to ship specimens via Courier, Taxi, FEDEX, UPS, etc. Configure this file FIRST using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option.

Example: CME Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab liaison menu Option: SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?\<RET\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Lab Shipping Management Menu Option: CME\<RET\> Edit Shipping Method

Select SHIPPING METHOD: ?\<RET\>

Answer with LAB SHIPPING METHOD NAME

You may enter a new LAB SHIPPING METHOD, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING METHOD: FEDEX\<RET\>

Are you adding 'FEDEX' as a new LAB SHIPPING METHOD (the 1ST)? Y\<RET\> (Yes)

NAME: FEDEX//\<RET\>

Select Lab Shipping Management Menu Option: CME\<RET\> Edit Shipping Method

Select SHIPPING METHOD: COURIER\<RET\>

Are you adding 'COURIER' as a new LAB SHIPPING METHOD (the 2ND)? Y\<RET\>

(Yes)

NAME: COURIER//\<RET\>

> b\. LAB SHIPPING CONDITION file (#62.93) contains entries that describe the conditions under which a lab shipment is transported (i.e., Ambient temperature, Frozen, Refrigerated, etc.). Configure this file SECOND using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Example: How to configure the LAB SHIPPING CONDITION file (#62.93) using the CDE Edit Shipping Condition \[LA7S EDIT 62.93\] option

Select Lab liaison menu Option: SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ??\<RET\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CDE\<RET\> Edit Shipping Condition

Use this option to setup the Lab Shipping Condition file.

Select SHIPPING CONDITION: ?\<RET\>

Answer with LAB SHIPPING CONDITIONS NAME

You may enter a new LAB SHIPPING CONDITIONS, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONDITION: Room Temperature\<RET\>

Are you adding 'Room Temperature' as

a new LAB SHIPPING CONDITIONS (the 1ST)? No// Y\<RET\> (Yes)

NAME: Room Temperature//\<RET\>

ABBREVIATION: RT\<RET\>

3.  LAB SHIPPING CONTAINER file (#62.91) contains the type of containers that the laboratory uses to ship lab test specimens. Configure this file THIRD using the CTE Edit Shipping Container \[LA7S EDIT 62.91\] option.

> There are basically three types of containers used for shipping lab test specimens as follows:

- Primary – specimen is shipped in the original collection container (i.e., Lavender top tube).
- Aliquot – specimen transferred to a tube/jar before shipment (i.e., Plastic Transport Tube, Brown Plastic Tube).
- Packaging – packaging containers used for holding the specimen containers (i.e., box).
- This is the THIRD file to be configured using the option, CTE or Edit Shipping Container \[LA7S EDIT 62.91\].

Example: How to configure the LAB SHIPPING CONTAINER file (#62.91) using the CTE Edit Shipping Container \[LA7S EDIT 62.91\] option

Select Lab liaison menu Option: SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CTE\<RET\> Edit Shipping Container

Use this option to setup the Lab Shipping Container file.

Select SHIPPING CONTAINER: ?\<RET\>

Answer with LAB SHIPPING CONTAINER NAME

You may enter a new LAB SHIPPING CONTAINER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONTAINER: Plastic Tube\<RET\>

Are you adding 'Plastic Tube' as

a new LAB SHIPPING CONTAINER (the 1ST)? No// Y\<RET\> (Yes)

NAME: Plastic Tube//\<RET\>

TYPE: ?\<RET\>

Enter what this container is used for.

Choose from:

1 PACKAGING

2 PRIMARY

3 ALIQUOT

TYPE: 3 ALIQUOT\<RET\>

> d\. LAB SHIPPING CONFIGURATION file (#62.9) contains the specimen volume, weight, collection end date/time (collection duration), patient height and weight. LOINC codes are used to identify patient height, weight and specimen weight when deemed appropriate. This is the FOURTH and final file to be configured by the COLLECTION facility using the CFE Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Example: How to use the CFE Edit Shipping Configuration \[LA7S EDIT 62.9\] option to configure the LAB SHIPPING CONFIGURATION file (#62.9) for the COLLECTION facility.

Select Lab Shipping Management Menu Option: CFE Edit Shipping Configuration \<ENTER\>

Select SHIPPING CONFIGURATION: TRIPLER AMC\<ENTER\>

Are you adding 'TRIPLER AMC' as

a new LAB SHIPPING CONFIGURATION (the 14TH)? No// Y (Yes) \<Enter\>

LAB SHIPPING CONFIGURATION COLLECTING FACILITY: HONOLULU

LAB SHIPPING CONFIGURATION HOST FACILITY: TRIPLER ARMY MEDICAL CENTER

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: 1 Collecting facility

NAME: TRIPLER AMC//\<Enter\>

COLLECTING FACILITY: HONOLULU//\<Enter\>

COLLECTING FACILITY'S SYSTEM: HONOLULU \<Enter\>

HOST FACILITY: TRIPLER ARMY MEDICAL CENTER//\<Enter\>

HOST FACILITY'S SYSTEM: TRIPLER ARMY MEDICAL CENTER

STATUS: A ACTIVE

LAB MESSAGING LINK: \<Enter\>

SHIPPING METHOD: COURIER

BARCODE MANIFEST: N \<Enter\> NO

MANIFEST RECEIPT: Y \<Enter\> YES

INCLUDE UNCOLLECTED SPECIMENS: N\<Enter\> NO

Example: How to use the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option to configure the LAB SHIPPING CONFIGURATION file (#62.9) for the collection facility – continued.

Select TEST/PROFILE: GLUCOSE-DOD

Are you adding 'GLUCOSE-DOD' as a new TEST/PROFILE (the 1ST for this LAB SHIPPING CONFIGURATION)? No// Y\<Enter\>(Yes)

ACCESSION AREA: SEND OUT

DIVISION:

SPECIMEN: SERUM 0X500

URGENCY:

SPECIMEN CONTAINER: PLASTIC TUBE

SHIPPING CONDITION: REFRIGERATE

PACKAGING CONTAINER: PAINT CAN

NON-VA TEST ORDER CODE: 1234

NON-VA TEST ORDER NAME: GLUCOSE

NON-VA SPECIMEN CODE: 72

NON-VA SPECIMEN NAME: SERUM

COLLECTION SAMPLE CODE: 99

COLLECTION SAMPLE NAME: BLOOD

REQUIRE PATIENT HEIGHT: N NO

REQUIRE PATIENT WEIGHT: N NO

REQUIRE COLLECTION VOLUME: N NO

REQUIRE COLLECTION WEIGHT: N NO

REQUIRE COLLECTION END D/T: N NO

Select TEST/PROFILE:

3\. LIM: Setup the Lab Auto-instrument and HL7 Environment to receive results from HOST facility labs

> Use the LEDI Setup \[LA7V SETUP\] option. This option is located on the Lab Shipping Management menu \[LA7S MGR MENU\] of the Lab Liaison menu \[LRLIASON\].

NOTES: TCP/IP must be used as the HL7 transport protocol for VA to DoD Lab interfaces.

> **NOTE:** The two-institution names used in the following screen captures are examples ONLY.

DO NOT use the following two institutions HOST or COLLECTION facility names when defining your institution names.

Example: How to use the LEDI Setup \[LA7V SETUP\] option to setup Lab Auto-instrument and HL7 Environment to receive results from HOST facility labs

Select OPTION NAME: LEDI SETUP LA7V SETUP LEDI Setup

LEDI Setup

---------------------------------------------------------------------------

LEDI Setup

----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): 1\<Enter\>

---------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. Add HOST Lab

Enter a number (1-1): 1\<Enter\>

---------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab:\<Enter\>

Enter a number (1-1): 1\<Enter\>

Select INSTITUTION NAME: TRIPLER ARMY MEDICAL CENTER HI USAH 459CN

Setting up the following Host Labs for REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Receive Results from 0052

LA7V Process Results from 0052

LA7V Order to 0052

LA7V Send Order to 0052

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V HOST 0052

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V HOST 0052

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit:

---------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052

Enter a number (1-4): 2\<Enter\>

---------------------------------------------------------------------------

Logical Link for transmissions to/from TRIPLER ARMY MEDICAL CENTER

---------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from 0052

LA7V Send Order to 0052

Enter a Logical Link: (MM/TCP): TCP/IP

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

Enter RETURN to continue or '^' to exit:

---------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable) \<Enter\>

2\. Logical Link: LA7V0052\<Enter\>

3\. Message Configuration: LA7V HOST 0052\<Enter\>

4\. Auto Instrument: LA7V HOST 0052\<Enter\>

Enter a number (1-4): 3 \<Enter\>

GRACE PERIOD FOR MESSAGES: 5\<Enter\>

LOG ERRORS: ON//\<Enter\>

MULTIPLE ORDERS: ? \<Enter\>

Select if multiple/single patients/orders should be sent in a single message. See description (??) for additional help.

Choose from:

0 MULTIPLE PATIENTS

1 SINGLE PATIENT

2 SINGLE ORDER

MULTIPLE ORDERS: 2 SINGLE ORDER \<Enter\>

Select ALERT CONDITION: ERROR (2 ERROR ON MESSAGE) \<Enter\>

Are you adding 'ERROR ON MESSAGE' as a new ALERT CONDITION (the 1ST for this LA7 MESSAGE PARAMETER)? No// Y (Yes) \<Enter\>

MAIL GROUP: LAB MESSAGING

Select ALERT CONDITION: ? \<Enter\>

Answer with ALERT CONDITION: \<Enter\>

ERROR ON MESSAGE

You may enter a new ALERT CONDITION, if you wish

Enter "1" to receive alerts for new results, a "2" to receive alerts

for errors during processing. and "3" when orders are received.

Error on message alert may only be selected if Field \#4, LOG

ERRORS,is set to "ON".

Choose from:

1 NEW RESULTS

2 ERROR ON MESSAGE

3 ORDERS RECEIVED

Select ALERT CONDITION: 1 (1 NEW RESULTS) \<Enter\>

Are you adding 'NEW RESULTS' as a new ALERT CONDITION (the 2ND for this LA7 MESSAGE PARAMETER)? No// Y (Yes) \<Enter\>

MAIL GROUP: LAB MESSAGING\<Enter\>

Select ALERT CONDITION: \<Enter\>

--------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052

Enter a number (1-4): 4\<Enter\>

AUTOMATED INSTRUMENT: LA7V HOST 0052

LOAD/WORK LIST: DOD

METHOD: DOD

DEFAULT ACCESSION AREA: SEND OUT

OVERLAY DATA: Y \<Enter\>YES

STORE REMARKS: YES//\<Enter\>

Select SITE NOTES DATE: \<Enter\>

Add Chem Tests to the LA7V HOST 0052 Automated Instrument for TRIPLER ARMY MEDICAL CENTER.

Select CHEM TESTS: GLUCOSE

Are you adding 'GLUCOSE' as a new CHEM TESTS (the 1ST for this

AUTO INSTRUMENT)? No// Y \<Enter\> (Yes)

CHEM TESTS NUMBER: 1//\<Enter\>

CHEM TESTS TEST: GLUCOSE//\<Enter\>

TEST: GLUCOSE//\<Enter\>

PARAM 1: \<Enter\>

UI TEST CODE: 84330.0000// 1234

ACCEPT RESULTS FOR THIS TEST: Y \<Enter\> YES

IGNORE RESULTS NOT ORDERED: Y \<Enter\> YES

STORE REMARKS: YES// YES\<Enter\>

REMARK PREFIX: For Glu: \<Enter\>

NOTIFY ABNORMAL FLAGS: NO//\<Enter\> NO

Select CHEM TESTS: \<Enter\>

--------------------------------------------------------------------------

HOST Lab(s)

-------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052\<Enter\>

Enter a number (1-4): \<Enter\>

3\. IRM: Complete the HL7 Environment Setup for TCP/IP HL7 transport protocol

> The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information used within the Systems Link Monitor, which provides the users feedback regarding the status of each link.

> Select the logical link created for the DoD facility (LA7Vnnnn) where nnnn is the 4-digit DMIS ID of the DoD facility.

> Use the Link Edit \[HL EDIT LOGICAL LINKS\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\] to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section. Set the AUTOSTART field (#4.5) entry to ‘1’ (Enabled) if you want this to start automatically after TaskMan is restarted. Otherwise, these links will need to be manually started using the Start/Stop Links \[HL START\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\].

> **NOTE:** Please consult the VistA HEALTH LEVEL SEVEN (HL7) SITE MANAGER & DEVELOPER MANUAL for information on single and multi-threaded listeners.

> Set up this client device for the HOST lab. The client device is the link that connects to the other facilities’ listener device to transmit order messages from a COLLECTION facility and to transmit result messages from a HOST facility. A separate client device needs to be created for each facility that you will be sending the LEDI manifests to. The setup is as follows:

- NODE: LA7Vnnnn (where nnnn is the HOST lab DoD DMIS ID)
- LLP TYPE: TCP
- DEVICE TYPE: Non-Persistent Client
- QUEUE SIZE: 10
- RE-TRANSMISSION ATTEMPTS: 5
- TCP/IP ADDRESS: 10.224.129.80 (IP address of the Austin Automation Center’s (AAC) Vitria Interface Engine (IE))
- TCP/IP PORT: 27316 the port the AAC Vitria IE listener device is listening on
- TCP/IP SERVICE TYPE: CLIENT (Sender)
- PERSISTENT: NO (If a link gets tied up, other systems will not be able to connect and transmit messages to you. Therefore it must be set to persistent: NO).

4\. LIM: Work with the interface coordinator at the reference laboratory to test the system

> **NOTE:** Order laboratory test(s) on a test patient, build them on a shipping manifest, close and ship the manifest, then provide the interface coordinator with the manifest \#. The interface coordinator should be able to receive in the manifest and enter test results. The collecting site LIM should then be able to verify the lab test result(s) on the test patient via EA Enter/verify data (auto instrument) using the Load List and workload areas created in step 4 above.

5. LIM: Train END USERS

#### HOST Facility – DoD to VA Laboratory Implementation InstructionsNOTE: When implementing this interface with a DoD facility consult the LDSI National Implementation Plan for guidance to establish communication with the DoD facility via the VA/DoD VPN.

LEDI III instructions must be coordinated by the IRM and LIM staffs and performed in sequence for a successful implementation.

1\. IRM: INSTITUTION file (#4) Setup

> Load the DoD DMIS ID codes into your INSTITUION file (#4) using the Load DMIS ID's \[XUMF DMIS ID LOAD\] option installed by Kernel patch XU\*8.0\*261. LEDI software uses the following four fields from the INSTITUION file (#4). Check both the host and collection institutions.

- Name Field (#.01): The Institution Master File maintains nationally controlled entries for VA and DoD facilities
- Agency code Field (#95): This field indicates to the LEDI software whether the facility is a VA or DoD facility
- VA facilities should be set to:‘VA’
- DoD facilities should be set to:

> ‘AF’ - AIR FORCE

> ‘ARMY’ - ARMY

> 'N’ – NAVY

- Station Number Field (#99): For VA facilities
- Identifier (#9999): For DoD facilities indicate the DMIS ID for this facility.

1\. LIM: Provide the DoD laboratory with your electronic test catalog

> Contact the DoD laboratory to acquire the following information:

> The following information is needed by VistA to handle the Non-HL7 codes that DoD CHCS systems use to identify specimens and collection samples. These codes will be entered on VistA when setting up the shipping configuration used to process lab test orders from a DoD facility. It will map the DoD specimen/collection sample code to the corresponding VA VistA specimen/collection sample.

- DoD specimen code and name for each test
- DoD collection sample code and name for each test

2\. LIM: Setup Lab Shipping Configuration file

> Use the Lab Shipping Management \[LA7S MGR MENU\] Menu, Edit Shipping Configuration \[LA7S EDIT 62.9\] to configure the file.

> **NOTE:** LAB SHIPPING CONFIGURATION file (#62.9) contains the test information to process orders received from the DoD facility.

#### #### 3\. LIM: Setup HL7 Environment to receive orders from COLLECTING facility labs

> Use the LEDI Setup \[LA7V SETUP\] option. This option is located on the Lab Shipping Management menu \[LA7S MGR MENU\] of the Lab Liaison menu \[LRLIASON\].

> **NOTE:** TCP/IP MUST be used as the HL7 transport protocol for VA to DoD Lab interfaces.

> **NOTE:** The two-institution names used in the following screen captures are examples ONLY. DO NOT use these two institution names as your HOST or COLLECTION facility.

Example: How to use the LEDI Setup \[LA7V SETUP\] option to receive orders from COLLECTING facility labs.

Select OPTION NAME: LA7V SETUP LEDI Setup

LEDI Setup

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): 2\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. Add COLLECTION Lab

Enter a number (1-10): 1\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab:

Enter a number (1-1): 1\<ENTER\>

Select INSTITUTION NAME: TRIPLER ARMY MEDICAL CENTER HI USAH 459CN

Setting up the REMOTE Lab, TRIPLER ARMY MEDICAL CENTER and HOST Lab REGION 7 ISC, TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Results Reporting to 0052

LA7V Send Results to 0052

LA7V Receive Order from 0052

LA7V Process Order from 0052

Updating LA7 MESSAGE PARAMETER file (#62.48) for the REMOTE Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V COLLECTION 0052

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: RIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3): 2\<ENTER\>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from RIPLER ARMY MEDICAL CENTER

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Order from 0052 LA7V0052 (TCP)

LA7V Send Results to 0052 LA7V0052 (TCP)

Enter a Logical Link: (MM/TCP): TCP/IP

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: RIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3): 3\<ENTER\>

GRACE PERIOD FOR MESSAGES: 3\<ENTER\>

LOG ERRORS: ON//\<ENTER\>

MULTIPLE ORDERS: 2 \<ENTER\> SINGLE ORDER

Select ALERT CONDITION: ):\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: RIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052\<ENTER\>

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3):\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. RIPLER ARMY MEDICAL CENTER (LA7V COLLECTION 0052)

2\. Add COLLECTION Lab

Enter a number (1-2): \<ENTER\>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs: Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2):\<ENTER\>

2\. IRM: Complete HL7 Environment setup for TCP/IP HL7 transport protocol

> The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information used within the Systems Link Monitor, which provides the users feedback regarding the status of each link.

> *Select the logical link created for the DoD facility (LA7Vnnnn) where nnnn is the 4-digit DMIS ID of the DoD facility.*

> Use the Link Edit \[HL EDIT LOGICAL LINKS\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\] to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section. Set the AUTOSTART field (#4.5) entry to ‘1’ (Enabled) if you want this to start automatically after TaskMan is restarted. Otherwise, these links will need to be manually started using the Start/Stop Links \[HL START\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\].

> **NOTE:** Please consult the VistA HEALTH LEVEL SEVEN (HL7) SITE MANAGER & DEVELOPER MANUAL for information on single and multi-threaded listeners.

Set up this client device for the COLLECTING lab. The client device is the link that connects to the other facilities’’ listener device to transmit order messages from a COLLECTION facility and to transmit result messages from a HOST facility. A separate client device needs to be created for each facility that you will be sending the LEDI manifests to.

> The client device setup is as follows:

- NODE: LA7Vnnnn (where nnnn is the COLLECTING lab DoD DMIS ID).
- LLP TYPE: TCP
- DEVICE TYPE: Non-Persistent Client
- QUEUE SIZE: 10
- RE-TRANSMISSION ATTEMPTS: 5
- TCP/IP ADDRESS: 10.224.129.80 (IP address of the Austin Automation Center’s (AAC) Vitria Interface Engine (IE)).
- TCP/IP PORT: 27316 (the port the AAC IE listener device is listening on).
- TCP/IP SERVICE TYPE: CLIENT (Sender)
- PERSISTENT: NO (If a link gets tied up, other systems will not be able to connect and transmit messages to you. Therefore, it must be set to persistent: NO).  
  4. LIM: Work with the interface coordinator at the COLLECTION facility laboratory to test system.

> **NOTE:** Have the COLLECTING facility interface coordinator order laboratory test(s) on a test patient, build them on a shipping manifest, close and ship the manifest, then provide the manifest \# to the LIM of the HOST facility. The HOST facility LIM should be able to receive in the manifest and enter test results. The COLLECTING facility interface coordinator should then be able to verify the lab test result(s) on the test patient via the appropriate Composite Health Care System (CHCS) options in the COLLECTING system.

5\. LIM: Train END USERS

#### COLLECTION Facility – VA to VA Implementation Instructions

LEDI III instructions must be coordinated by the IRM and LIM staffs and performed in sequence for a successful implementation.

1\. IRM: Setup INSTITUTION file (#4)

> Load/update your local INSITUTION file (#4) using Update/refresh Institution file with IMF data \[XUMF LOAD INSTITUTION\] option. LEDI software uses the following four fields from the INSITUTION file (#4). Check both the HOST and COLLECTION institutions.

- Name Field (#.01): The Institution Master File maintains nationally controlled entries.
- Domain Field (#60): Used by previous version of LEDI when utilizing MailMan as the HL7 transport protocol. Used to create LA7V mail groups created by the LEDI Setup \[LA7V SETUP\] option. This field is not used by the LEDI Setup \[LA7V SETUP\] option for new connections.
- Agency Code Field (#95): Should be set to VA. Used to determine the status of the facility and how to setup the LEDI software application.
- Station Number Field (#99): This field is controlled nationally by the Institution Master File. It is used for configuring VA facilities and creating the Lab Shipping fields setup entries in the Lab Shipping Management \[LA7S MGR MENU\] menu.

2\. IRM: Use Mail Group Edit \[XMEDITMG\] option to create the following LEDI-related mail group(s)

> A local mail group for the NEW RESULTS Alert: Notifies members when the Lab Universal Interface software has processed an HL7 message containing test results. An example of this information type of alert is, “Lab Messaging – New results received for LA7V HOST 578’. It is recommended that the LIM be made coordinator of this mail group.

> Local mail group for the ERROR ON MESSAGE Alert: Notifies members of error conditions encountered during the processing of a Laboratory HL7 message. If preferred, the LAB MESSAGING mail group is recommended for this function. It is recommended that the LIM be a member of this mail group also. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action. The members of this mail group should, at the minimum, include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.

1\. LIM: Set up Lab Test files to send specimens to HOST facility lab

> **NOTE:** Contact the HOST facility LIM to acquire the following information:

> a\) Accession Area numeric identifier (these are two character alphanumeric codes). Only required when HOST facility lab will be using COLLECTION facility’s specimen labels and identifiers. Try to get an identifier that is not already in active use in your system.

> **NOTE:** If the HOST facility will be re-labeling the COLLECTION facility specimens, then the COLLECTION facility may use any accession area for these specimens/lab tests.

> b\) Specific test information to send to the HOST facility

> The HOST Systems Electronic Catalog Menu \[LAS7 CATALOG MENU\] can be used to produce this information.

- Specimen collection requirements
- Schedule of testing
- List of tests for panel tests
- Normal Range and Critical Values
- Patient prep instructions
- National Lab Test (NLT) order codes to order the tests
- NLT Result and LOINC codes used to report the results

> c\) Create/Edit an accession area in ACCESSION file (#68) for specimens to be sent to the HOST lab. Use VA FileMan \[DIUSER\], Enter or Edit \[DIEDIT\] option. If your VA HOST lab will be utilizing your specimen labels then assign the NUMERIC IDENTIFIER provided by the host facility to ACCESSION file (#68), NUMERIC IDENTIFIER field (#4). Existing or multiple accession areas can be utilized for reference testing.

> d\) Edit the LABORATORY TEST file (#60) to send specimens to the HOST facility laboratory. New Lab tests can be created to match the HOST facility requirements, or existing lab tests may be utilized IF the entries are compatible with the HOST facilities requirements. All tests must utilize the Accession Area from step b as stated above.

> e\) Create a Load List to define and accept lab test results transmitted by the HOST lab. The Load List must contain ALL of the lab tests that are processed by the HOST facility lab.

2\. LIM: Setup Lab Shipping Files

> Use the Lab Shipping Management Menu \[LA7S MGR MENU\], located on the Lab Liaison Menu \[LRLIAISON\] to configure the following four files in order:

> **NOTE:** Online help is available by entering two question marks (??) at the field prompt.

> LAB SHIPPING METHOD file (#62.92) contains the transport method used to ship specimens (i.e., Courier, Taxi, FEDEX, UPS, etc.). Configure this file FIRST using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option.

Example: How to the LAB SHIPPING METHOD file (#62.92) using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab Shipping Management Menu Option: CME Edit Shipping Method\<ENTER\>

Select SHIPPING METHOD: FEDEX\<ENTER\>

Are you adding 'FEDEX’ as a new LAB SHIPPING METHOD (the 3RD)? No// Y (Yes) \<ENTER\>

NAME: FEDEX//\<ENTER\>

Select Lab Shipping Management Menu Option: \<ENTER\>

LAB SHIPPING CONDITION file (#62.93) contains entries that describe the conditions under which a lab shipment is transported (i.e., Ambient temperature, Frozen, Refrigerated, etc.). Configure this file SECOND using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Example: How to configure the LAB SHIPPING CONDITION file (#62.93) using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Select Lab Shipping Management Menu Option: CDE Edit Shipping Condition\<ENTER\>

Select SHIPPING CONDITION: ROOM TEMPERATURE\<ENTER\>

Are you adding 'ROOM TEMPERATURE' as

a new LAB SHIPPING CONDITIONS (the 4TH)? No// Y (Yes) \<ENTER\>

NAME: ROOM TEMPERATURE//\<ENTER\>

ABBREVIATION: RT\<ENTER\>

Select Lab Shipping Management Menu Option:\<ENTER\>

LAB SHIPPING CONTAINER file (#62.91) contains the type of containers that the laboratory uses to ship lab test specimens. There are basically three types of containers used for shipping lab test specimens:

- Primary – specimen is shipped in the original collection container (i.e., Lavender top tube).
- Aliquot – specimen transferred to a tube/jar before shipment (i.e., Plastic Transport Tube, Brown Plastic Tube).
- Packaging - packaging containers user for holding the specimen containers (i.e., box).

> **NOTE:** This is the THIRD file to be configured using the CTE or Edit Shipping Container \[LA7S EDIT 62.91) option.

Example: How to configure the LAB SHIPPING CONTAINER file (#62.91) using the CTE or Edit Shipping Container \[LA7S EDIT 62.91) option.

Select Lab Shipping Management Menu Option: Edit Shipping Container\<ENTER\>

Select SHIPPING CONTAINER: STYROFOAM BOX\<ENTER\>

Are you adding 'STYROFOAM BOX' as

a new LAB SHIPPING CONTAINER (the 3RD)? No// Y (Yes)\<ENTER\>

NAME: STYROFOAM BOX//\<ENTER\>

TYPE: 1 PACKAGING\<ENTER\>

LAB SHIPPING CONFIGURATION (#62.9) contains the specimen volume, weight, collection end date/time (collection duration), patient height, and weight. LOINC codes are used to identify patient height, weight and specimen weight when deemed appropriate. This is the FOURTH and final file to be configured by the collection facility using the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Example: How to configure the LAB SHIPPING CONFIGURATION (#62.9) using the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Select Lab Shipping Management Menu Option: Edit Shipping Configuration\<ENTER\>

Select SHIPPING CONFIGURATION: MILWAUKEE HOST LAB\<ENTER\>

Select one of the following:\<ENTER\>

1 Collecting facility

2 Host facility

Are you editing this entry as the: 1 Collecting facility:\<ENTER\>

NAME: MILWAUKEE HOST LAB//:\<ENTER\>

COLLECTING FACILITY: REGION 7 ISC,TX (DEMO)//\<ENTER\>

COLLECTING FACILITY'S SYSTEM: REGION 5//\<ENTER\>

HOST FACILITY: MILWAUKEE VAMC//\<ENTER\>

HOST FACILITY'S SYSTEM: MILWAUKEE VAMC//\<ENTER\>

STATUS: ACTIVE//\<ENTER\>

LAB MESSAGING LINK: LA7V HOST 695//\<ENTER\>

SHIPPING METHOD: FEDEX//\<ENTER\>

BARCODE MANIFEST: YES-COMPACT//\<ENTER\>

MANIFEST RECEIPT: NO// Y YES\<ENTER\>

INCLUDE UNCOLLECTED SPECIMENS: NO//\<ENTER\>

Select TEST/PROFILE: CREATININE (INCLUDES EGFR)//\<ENTER\>

TEST/PROFILE: CREATININE (INCLUDES EGFR)//\<ENTER\>

ACCESSION AREA: CHEMISTRY//\<ENTER\>

DIVISION: \<ENTER\>

SPECIMEN: SERUM//\<ENTER\>

URGENCY: ROUTINE

SPECIMEN CONTAINER: PLASTIC TUBE//\<ENTER\>

SHIPPING CONDITION: REFRIGERATE//\<ENTER\>

PACKAGING CONTAINER: PAINT CAN//\<ENTER\>

REQUIRE PATIENT HEIGHT: N NO\<ENTER\>

REQUIRE PATIENT WEIGHT: N NO\<ENTER\>

REQUIRE COLLECTION VOLUME: N NO\<ENTER\>

REQUIRE COLLECTION WEIGHT: N NO\<ENTER\>

REQUIRE COLLECTION END D/T: N NO\<ENTER\>

Select TEST/PROFILE: \<ENTER\>

3\. LIM: Setup Lab Auto-Instrument and HL7 Environment to receive results from HOST labs

> Use the LEDI Setup \[LA7V SETUP\] option. This option is located on the Lab Shipping Management \[LA7S MGR MENU\] menu of the Lab Liaison \[LRLIASON\] menu.

NOTES: Multi-divisional facilities should ONLY use the LEDI Setup option for the primary facility. All other facilities with a multi-divisional facility will use the primary facility to transmit and receive HL7 messages.

To convert from MailMan to TCP/IP communication protocol on existing LEDI interfaces between VA facilities both sites should use the LEDI Setup option to select TCP as the communication protocol. This switch should be coordinated and occur at the same time at both facilities. The HL package will encounter difficulties in transmitting and processing messages when the send and receiver are using different communication protocols. Conversion should occur when the affected LA7V\* HL7 messaging queues for both facilities have no messages awaiting transmission.

Example: How to set up the Lab Auto-Instrument and HL7 Environment to receive results from HOST labs using the LEDI Setup \[LA7V SETUP\] option.

Select Lab Shipping Management Menu Option: LSU LEDI Setup\<ENTER\>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): 1\<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. TRIPLER ARMY MEDICAL CENTER (LA7V HOST 0052)

2\. WILFORD HALL MEDICAL CENTER (LA7V HOST 0117)

3\. ANCH6A BAY PINES (LA7V HOST 170BP)

4\. ZZ ALBANY (LA7V HOST 500)

5\. NEW MEXICO HCS (LA7V HOST 501)

6\. BROCKTON VAMC (LA7V HOST 525)

7\. HOUSTON VAMC (LA7V HOST 580)

8\. MEMPHIS VAMC (LA7V HOST 614)

9\. Add HOST Lab

Enter a number (1-9): 9\<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: \<ENTER\>

Enter a number (1-1): 1\<ENTER\>

Select INSTITUTION NAME: MILWAUKEE VAMC WI VAMC 695

Setting up the following Host Labs for REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Receive Results from 695

LA7V Process Results from 695

LA7V Order to 695

LA7V Send Order to 695

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab MILWAUKEE VAMC.

Adding LA7V HOST 695

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab MILWAUKEE VAMC.

Adding LA7V HOST 695

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: \<ENTER\>

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): 2\<ENTER\>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from MILWAUKEE VAMC

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from 695 VAMIW (TCP)

LA7V Send Order to 695 VAMIW (TCP)

Setup/update Logical Link? YES\<ENTER\>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): 3\<ENTER\>

GRACE PERIOD FOR MESSAGES: 1//\<ENTER\>

LOG ERRORS: ON//\<ENTER\>

MULTIPLE ORDERS: MULTIPLE PATIENTS//\<ENTER\>

Select ALERT CONDITION: ERROR ON MESSAGE//\<ENTER\>

ALERT CONDITION: ERROR ON MESSAGE//\<ENTER\>

MAIL GROUP: LAB MESSAGING//\<ENTER\>

Select ALERT CONDITION: NEW (1 NEW RESULTS)\<ENTER\>

ALERT CONDITION: NEW RESULTS//\<ENTER\>

MAIL GROUP: LAB MESSAGING//\<ENTER\>

Select ALERT CONDITION: \<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): 4\<ENTER\>

AUTOMATED INSTRUMENT: LA7V HOST 695

LOAD/WORK LIST: CHEMISTRY//\<ENTER\>

METHOD: VAMC695//\<ENTER\>

DEFAULT ACCESSION AREA: CHEMISTRY//\<ENTER\>

OVERLAY DATA: YES//\<ENTER\>

STORE REMARKS: YES//\<ENTER\>

Select SITE NOTES DATE: \<ENTER\>

Add Chem Tests to the LA7V HOST 695 Automated Instrument for MILWAUKEE VAMC.

Select CHEM TESTS: GLUCOSE FBS

...OK? Yes// \<ENTER\> (Yes)

TEST: GLUCOSE//\<ENTER\>

PARAM 1: \<ENTER\>

UI TEST CODE: 2345-7// \<ENTER\>

ACCEPT RESULTS FOR THIS TEST: YES// \<ENTER\>

IGNORE RESULTS NOT ORDERED: Y YES\<ENTER\>

STORE REMARKS: YES//\<ENTER\>

REMARK PREFIX: For GLU:// \<ENTER\>

NOTIFY ABNORMAL FLAGS: YES// \<ENTER\>

Select CHEM TESTS: \<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4):\<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. TRIPLER ARMY MEDICAL CENTER (LA7V HOST 0052)

2\. WILFORD HALL MEDICAL CENTER (LA7V HOST 0117)

3\. ANCH6A BAY PINES (LA7V HOST 170BP)

4\. ZZ ALBANY (LA7V HOST 500)

5\. NEW MEXICO HCS (LA7V HOST 501)

6\. ZZ BROCKTON VAMC (LA7V HOST 525)

7\. HOUSTON VAMC (LA7V HOST 580)

8\. MEMPHIS VAMC (LA7V HOST 614)

9\. MILWAUKEE VAMC (LA7V HOST 695)

10\. Add HOST Lab

Enter a number (1-10): \<ENTER\>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2):\<ENTER\>

Select Lab Shipping Management Menu Option: \<ENTER\>

3\. IRM: HL7 Environment

> No further action is required for VA to VA LEDI interfaces. The LEDI software uses the site’s standard HL7 TCP listeners and clients (VAxxx links).

4\. LIM: Work with the LIM at the HOST facility to test the system

> Order laboratory test(s) on a test patient, build them on a shipping manifest, close and ship the manifest, then provide the HOST facility LIM with the manifest \#. The HOST facility LIM should be able to receive in the manifest and enter test results. A View Alert will be generated in the collecting site indicating results are available. The COLLECTING facility LIM should then be able to verify the lab test result(s) on the test patient via EA Enter/verify data (auto instrument) using the Load List and workload areas created in step 4 above.

5.  LIM: Train END USERS

> **NOTE:** Please see ‘Use of the Software’ section in the following User Guide to assist with training the END USERS.

COLLECTION Facility – VA to VA (Intra-division) Implementation Instructions

Used when a VistA system is multi-divisional and/or integrated and sending specimens between divisions. When sending specimens from a CBOC to a main lab or between laboratories of a multi-divisional facility only the Lab Shipping Configuration setup is required. Do NOT use the LEDI Setup option. When both facilities reside on the same VistA system there is no LEDI HL7 interface needed or setup.

Use of LEDI involves the collecting facility starting, building and shipping a manifest. Once this has occurred there is no further use of LEDI. At this time there is no further action for the host lab with regards to LEDI. Accessions related to specimen shipped are already available with the VistA Lab package and are processed and reported using regular Laboratory package options.

LEDI III instructions must be coordinated by the LIM staffs at both divisions and performed in sequence for a successful implementation.

1\. LIM: Setup Lab Shipping Files

> Use the Lab Shipping Management Menu \[LA7S MGR MENU\], located on the Lab Liaison Menu \[LRLIAISON\] to configure the following four files in order:

> **NOTE:** Online help is available by entering two question marks (??) at the field prompt.

> LAB SHIPPING METHOD file (#62.92) contains the transport method used to ship specimens (i.e., Courier, Taxi, FEDEX, UPS, etc.). Configure this file FIRST using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option.

Example: How to the LAB SHIPPING METHOD file (#62.92) using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab Shipping Management Menu Option: CME Edit Shipping Method\<ENTER\>

Select SHIPPING METHOD: FEDEX\<ENTER\>

Are you adding 'FEDEX’ as a new LAB SHIPPING METHOD (the 3RD)? No// Y (Yes) \<ENTER\>

NAME: FEDEX//\<ENTER\>

Select Lab Shipping Management Menu Option: \<ENTER\>

LAB SHIPPING CONDITION file (#62.93) contains entries that describe the conditions under which a lab shipment is transported (i.e., Ambient temperature, Frozen, Refrigerated, etc.). Configure this file SECOND using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Example: How to configure the LAB SHIPPING CONDITION file (#62.93) using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Select Lab Shipping Management Menu Option: CDE Edit Shipping Condition\<ENTER\>

Select SHIPPING CONDITION: ROOM TEMPERATURE\<ENTER\>

Are you adding 'ROOM TEMPERATURE' as

a new LAB SHIPPING CONDITIONS (the 4TH)? No// Y (Yes) \<ENTER\>

NAME: ROOM TEMPERATURE//\<ENTER\>

ABBREVIATION: RT\<ENTER\>

Select Lab Shipping Management Menu Option:\<ENTER\>

LAB SHIPPING CONTAINER file (#62.91) contains the type of containers that the laboratory uses to ship lab test specimens. There are basically three types of containers used for shipping lab test specimens:

- Primary – specimen is shipped in the original collection container (i.e., Lavender top tube).
- Aliquot – specimen transferred to a tube/jar before shipment (i.e., Plastic Transport Tube, Brown Plastic Tube).
- Packaging - packaging containers user for holding the specimen containers (i.e., box).

> **NOTE:** This is the THIRD file to be configured using the CTE or Edit Shipping Container \[LA7S EDIT 62.91) option.

Example: How to configure the LAB SHIPPING CONTAINER file (#62.91) using the CTE or Edit Shipping Container \[LA7S EDIT 62.91) option.

Select Lab Shipping Management Menu Option: Edit Shipping Container\<ENTER\>

Select SHIPPING CONTAINER: STYROFOAM BOX\<ENTER\>

Are you adding 'STYROFOAM BOX' as

a new LAB SHIPPING CONTAINER (the 3RD)? No// Y (Yes)\<ENTER\>

NAME: STYROFOAM BOX//\<ENTER\>

TYPE: 1 PACKAGING\<ENTER\>

LAB SHIPPING CONFIGURATION (#62.9). This is the FOURTH and final file to be configured by the collection facility using the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Example: How to configure the LAB SHIPPING CONFIGURATION (#62.9) using the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Select Lab Shipping Management Menu Option: Edit Shipping Configuration\<ENTER\>

Select SHIPPING CONFIGURATION: MILWAUKEE HOST LAB\<ENTER\>

Select one of the following:\<ENTER\>

1 Collecting facility

2 Host facility

Are you editing this entry as the: 1 Collecting facility:\<ENTER\>

NAME: MILWAUKEE HOST LAB//:\<ENTER\>

COLLECTING FACILITY: REGION 7 ISC,TX (DEMO)//\<ENTER\>

COLLECTING FACILITY'S SYSTEM: REGION 5//\<ENTER\>

HOST FACILITY: MILWAUKEE VAMC//\<ENTER\>

HOST FACILITY'S SYSTEM: MILWAUKEE VAMC//\<ENTER\>

STATUS: ACTIVE//\<ENTER\>

LAB MESSAGING LINK: \<ENTER\> (Note: leave this field blank)

SHIPPING METHOD: FEDEX//\<ENTER\>

BARCODE MANIFEST: YES-COMPACT//\<ENTER\>

MANIFEST RECEIPT: NO// Y YES\<ENTER\>

INCLUDE UNCOLLECTED SPECIMENS: NO//\<ENTER\>

Select TEST/PROFILE: CREATININE (INCLUDES EGFR)//\<ENTER\>

TEST/PROFILE: CREATININE (INCLUDES EGFR)//\<ENTER\>

ACCESSION AREA: CHEMISTRY//\<ENTER\>

DIVISION: \<ENTER\>

SPECIMEN: SERUM//\<ENTER\>

URGENCY: ROUTINE

SPECIMEN CONTAINER: PLASTIC TUBE//\<ENTER\>

SHIPPING CONDITION: REFRIGERATE//\<ENTER\>

PACKAGING CONTAINER: PAINT CAN//\<ENTER\>

REQUIRE PATIENT HEIGHT: N NO\<ENTER\>

REQUIRE PATIENT WEIGHT: N NO\<ENTER\>

REQUIRE COLLECTION VOLUME: N NO\<ENTER\>

REQUIRE COLLECTION WEIGHT: N NO\<ENTER\>

REQUIRE COLLECTION END D/T: N NO\<ENTER\>

Select TEST/PROFILE: \<ENTER\>

#### HOST Facility – VA to VA

LEDI III instructions must be coordinated by the IRM and LIM staffs and performed in sequence for a successful implementation.

1\. IRM: Setup INSTITUTION file (#4).

> Load/update your local INSITUTION file (#4) using the Update/refresh Institution file with IMF data \[XUMF LOAD INSTITUTION\] option. LEDI III software uses the following four fields from the INSTITUTION file (#4). Check both the HOST and COLLECTION facilities institutions.

- Name Field (#.01): Institution Master File maintains nationally controlled entries.
- Domain Field (#60): Used by previous version of LEDI when utilizing MailMan as the HL7 transport protocol. Used to create LA7V\* mail group that is created by the LEDI Setup \[LA7V SETUP\] option. Note: This field is not used by the LEDI Setup \[LA7V SETUP\] option for new connections.
- Agency Code Field (#95): Should be set to VA. Used to determine the status of the facility and how to setup the LEDI software application.
- Station Number Field (#99): This field is controlled nationally by the Institution Master File. It is used for configuring VA facilities and creating the Lab Shipping fields setup entries in the Lab Shipping Management \[LA7S MGR MENU\] menu.

2\. IRM: Use Mail Group Edit \[XMEDITMG\] option to create LEDI-related mail group(s)

> Local mail group for ORDERS RECEIVED Alert: Notifies members when the Lab Universal Interface software has processed an HL7 message containing test results. An example of this information type of alert is, “Lab Messaging – New results received for LA7V HOST 578’. Note: It is recommended that the LIM be made coordinator of this mail group.

> Local mail group for ERROR ON MESSAGE Alert: Notifies members of error conditions encountered during the processing of a Laboratory HL7 message. If preferred, the LAB MESSAGING mail group is recommended for this function. Note: It is recommended that the LIM be a member of this mail group also. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action. The members of this mail group should, at the minimum, include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI III software.

1\. LIM: Coordinate lab test files to receive specimens from COLLECTION facility labs

> Be prepared to supply the COLLECTION facility’s LIM the following information:

- Accession Area numeric identifier: These are two digit codes, can be alphabetic, numeric or alphanumeric. Offer an identifier that is not already in active use in your system.

> **NOTE:** The HOST facility must not use that specific NUMERIC IDENTIFIER for any local accessioning. This NUMERIC IDENTIFIER is to be used ONLY by the COLLECTION facility laboratory for which it was assigned.

> If the HOST facility will be re-labeling the collection facility specimens, then the COLLECTION facility may use any accession area for these specimens/lab tests.

> Specific test information to receive tests from the COLLECTION facility.

> The HOST systems Electronic Catalog \[LA7S CATALOG MENU\] Menu can be used to produce this information;

- Specimen collection requirements
- Schedule of testing
- List of tests for panel tests
- Normal Range and Critical Values
- Patient prep instructions
- National Lab Test (NLT) order codes to order the tests
- NLT Result and LOINC codes used to report the results

2\. LIM: HOST facility must setup the following file

> **NOTE:** HOST facilities that are also COLLECTION facilities must follow the setup instructions for the COLLECTION facilities, as it pertains to the specimens that are shipped to HOST facilities.

> LAB SHIPPING CONFIGURATION file (#62.9) is used to define the two members (institutions) that have a relationship. This file is used to group the Collection and Host facilities and describe particulars of their relationship (i.e., what specimen ID is used, what types of tests/specimens are shipped, who is the Collection/Host facility, are the facilities linked electronically, and are they on the same computer system).

> Use the Lab Shipping Management \[LA7S MGR MENU\] menu, Edit Shipping Configuration \[LA7S EDIT 62.9\] option to configure the LAB SHIPPING CONFIGURATION file (#62.9) for a VA facility.

Example: How to use Edit Shipping Configuration \[LA7S EDIT 62.9\] option to configure the LAB SHIPPING CONFIGURATION file (#62.9) for a VA facility.

Select Lab Shipping Management Menu Option: Edit Shipping Configuration\<ENTER\>

Select SHIPPING CONFIGURATION: MILWAUKEE REMOTE\<ENTER\>

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: 2 Host facility\<ENTER\>

Select one of the following:

0 Do NOT copy

1 Another Shipping Configuration

2 Test Catalog - LABORATORY TEST File \#60

Copy a test profile from: Do NOT copy//\<ENTER\>

NAME: MILWAUKEE REMOTE//\<ENTER\>

COLLECTING FACILITY: MILWAUKEE VAMC//\<ENTER\>

COLLECTING FACILITY'S SYSTEM: MILWAUKEE VAMC//\<ENTER\>

HOST FACILITY: REGION 7 ISC,TX (DEMO)//\<ENTER\>

HOST FACILITY'S SYSTEM: REGION 7 ISC,TX (DEMO)//\<ENTER\>

STATUS: ACTIVE//

COLLECTING FACILITY'S SPEC ID: HOST FACILITY//\<ENTER\>

Select TEST/PROFILE: GLUCOSE

TEST/PROFILE: GLUCOSE//\<ENTER\>

URGENCY: ROUTINE

HOST COLLECTION SAMPLE: SERUM//\<ENTER\>

Select TEST/PROFILE:\<ENTER\>

3\. LIM: Setup for HL7 Environment

> The LEDI Setup \[LA7V SETUP\] option allows the LIM to setup a COLLECTION and/or HOST facility HL7 environment. This option is located on the Lab Shipping Management \[LA7S MGR MENU\] menu of the Lab Liaison \[LRLIAISON\] menu.

> **NOTE:** <u>Multi-divisional facilities:</u> If the COLLECTION facility is a division of a multi-divisional facility then setup the primary facility’s system as the COLLECTION facility.

To convert from MailMan to TCP/IP communication protocol on existing LEDI interfaces between VA facilities both sites should use the LEDI Setup option to select TCP as the communication protocol. This switch should be coordinated and occur at the same time at both facilities. The HL package will encounter difficulties in transmitting and processing messages when the send and receiver are using different communication protocols. Conversion should occur when the affected LA7V\* HL7 messaging queues for both facilities have no messages awaiting transmission.

Example: How to use the LEDI Setup \[LA7V SETUP\] option to setup a COLLECTION and/or HOST facility HL7 environment.

Select Lab Shipping Management Menu Option: LEDI Setup

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): 2\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

----------------------------------------------------------------------------

1\. MILWAUKEE VAMC (LA7V COLLECTION 695)

2\. Add COLLECTION Lab

Enter a number (1-2): 2\<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): 1\<ENTER\>

Are you sure you want to update the MILWAUKEE VAMC interface? YES

Setting up the REMOTE Lab, MILWAUKEE VAMC and HOST Lab REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Results Reporting to 695

LA7V Send Results to 695

LA7V Receive Order from 695

LA7V Process Order from 695

Updating LA7 MESSAGE PARAMETER file (#62.48) for the REMOTE Lab MILWAUKEE VAMC.

Adding LA7V COLLECTION 695

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): LA7V 695

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): 2\<ENTER\>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from MILWAUKEE VAMC

----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Order from 695 VAMIW (TCP)

LA7V Send Results to 695 VAMIW (TCP)

Setup/update Logical Link? YES\<ENTER\>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): 3\<ENTER\>

GRACE PERIOD FOR MESSAGES: 1//\<ENTER\>

LOG ERRORS: ON//\<ENTER\>

MULTIPLE ORDERS: 0 MULTIPLE PATIENTS

Select ALERT CONDITION: ERROR ON MESSAGE// \<ENTER\>

ALERT CONDITION: ERROR ON MESSAGE// \<ENTER\>

MAIL GROUP: LAB MESSAGING//\<ENTER\>

Select ALERT CONDITION: OR (3 ORDERS RECEIVED)

ALERT CONDITION: ORDERS RECEIVED// \<ENTER\>

MAIL GROUP: LAB MESSAGING// \<ENTER\>

Select ALERT CONDITION: \<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW\<ENTER\>

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): \<ENTER\>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. MILWAUKEE VAMC (LA7V COLLECTION 695)

2\. Add COLLECTION Lab

Enter a number (1-2): \<ENTER\>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): \<ENTER\>

Select Lab Shipping Management Menu Option: \<ENTER\>

3\. IRM: No further action required

> For VA to VA LEDI interfaces the LEDI III software uses the site’s standard HL7 TCP listeners and clients (VAxxx links).

4\. LIM: Work with the LIM at the HOST facility to test the system

> Order laboratory test(s) on a test patient, build them on a shipping manifest, close and ship the manifest, then provide the HOST facility LIM with the manifest \#. The HOST facility LIM should be able to receive in the manifest and enter test results. A View Alert will be generated in the COLLECTING facility indicating results are available. The COLLECTING facility LIM should then be able to verify the lab test result(s) on the test patient via EA Enter/verify data (auto instrument).

5\. LIM: Train END USERS

> Please refer to the ‘Use of the Software’ section of this guide.

### COLLECTION facility – VA to Commercial Reference Laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI instructions must be coordinated by the IRM and LIM staffs and performed in sequence for a successful implementation.

1\. IRM: Setup INSTITUTION file (#4)

> LEDI software uses the following four fields from the INSTITUTION file (#4). Check both the HOST and COLLECTION institutions. Use VA FileMan {DIUSER\], Enter or Edit File Entries \[DIEDIT\] option to appropriately define each of these fields:

1.  Name Field (#.01): Enter the name of the institution for both the HOST and COLLECTING facilities institutions. This applies ONLY for non-VA entries. The Institution Master File maintains nationally controlled entries.
2.  Agency code Field (#95): This field indicates to the LEDI III software whether the facility is a VA or non-VA facility. Applicable only for non-VA entries. The Institution Master File maintains nationally controlled entries. The AGENCY CODE filed (#95) should be defined as follows: This should be set to OTHER for commercial reference laboratories and non-US government health care facilities.

2\. IRM: Use Mail Group Edit \[XMEDITMG\] option to create LEDI-related mail group(s)

> Local mail group for ORDERS RECEIVED Alert: Notifies members when the Lab Universal Interface software has processed an HL7 message containing test results. An example of this information type of alert is, “Lab Messaging – New results received for LA7V HOST 578’. It is recommended that the LIM be made coordinator of this mail group.

> Local mail group for ERROR ON MESSAGE Alert: Notifies members of error conditions encountered during the processing of a Laboratory HL7 message. If preferred, the LAB MESSAGING mail group is recommended for this function. It is recommended that the LIM be a member of this mail group also. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action. The members of this mail group should, at the minimum, include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI III software.

1\. LIM: Setup Lab Test Files to send specimens to commercial reference laboratory.

3.  Contact the reference laboratory to acquire the following information:
    - Specimen collection requirements
      - Specimen handling/minimum requirements
      - Alternate specimen (if any)
      - Stability (for shipping conditions)
      - Patient prep instructions
    - Schedule of testing and TAT
    - Order code to order the tests
    - Exact test name for Non-VA test name
    - List of tests for panel tests
    - Result code(s) used to report the results
    - Normal Range and Critical Values
    - Units of measure
    - Account number for use with the interface samples
4.  Create/Edit an accession area in the ACCESSION file (#68) for specimens to be sent to the HOST lab. Using VA FileMan \[DIUSER\], Enter or Edit \[DIEDIT\] option, assign a NUMERIC IDENTIFIER to the NUMERIC IDENTIFIER field (#4). The accession area MUST be used ONLY for tests/specimens being sent to the Host facility lab for processing.
5.  Edit the LABORATORY TEST file (#60) to send specimens to the HOST facility laboratory. New lab test can be created to match the HOST facility requirements, or existing labs may be utilized IF the entries are compatible with the HOST facilities requirements. All tests must utilize the Accession Area from step b. above.
6.  Create a Load List to define and accept lab test results transmitted by the HOST facility lab. The Load List MUST contain ALL of the lab tests that are processed by the HOST facility lab

2\. LIM: Setup Lab Shipping Files

> Using the Lab Shipping Management Menu \[LA7S MGR MENU\], FOUND ON THE Lab Liaison Menu \[LRLIASON\] configures the following four files in order:

NOTES: The first three files may already be set up if a VA to VA interface exists for your facility. Online help is available by entering two question marks (??) at the field prompt.

1.  LAB SHIPPING METHOD file (#62.92) contains the transport method used to ship specimens (i.e., Courier, Taxi, FEDEX, UPS, etc.). Configure this file FIRST using the CME or Edit Shipping Method \[LA7S EDIT 62.92\] option.

Example: How to use the CME Edit Shipping Method \[LA7S EDIT 62.92\] option to configure the LAB SHIPPING METHOD file (#62.92)

Select Lab liaison menu Option: SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?\<RET\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Lab Shipping Management Menu Option: CME\<RET\> Edit Shipping Method

Select SHIPPING METHOD: ?\<RET\>

Answer with LAB SHIPPING METHOD NAME

You may enter a new LAB SHIPPING METHOD, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING METHOD: FEDEX\<RET\>

Are you adding 'FEDEX' as a new LAB SHIPPING METHOD (the 1ST)? Y\<RET\> (Yes)

NAME: FEDEX//\<RET\>

Select Lab Shipping Management Menu Option: CME\<RET\> Edit Shipping Method

Select SHIPPING METHOD: COURIER\<RET\>

Are you adding 'COURIER' as a new LAB SHIPPING METHOD (the 2ND)? Y\<RET\>

(Yes)

NAME: COURIER//\<RET\>

2.  LAB SHIPPING CONDITION file (#62.93) contains entries that describe the conditions under which a lab shipment is transported (i.e., Ambient temperature, Frozen, Refrigerated, etc.). Configure this file SECOND using the CDE or Edit Shipping condition \[LA7S EDIT 62.93\] option.

Example: CDE Edit Shipping Condition \[LA7S EDIT 62.93\] option

Select Lab liaison menu Option: SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ??\<RET\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CDE\<RET\> Edit Shipping Condition

Use this option to setup the Lab Shipping Condition file.

Select SHIPPING CONDITION: ?\<RET\>

Answer with LAB SHIPPING CONDITIONS NAME

You may enter a new LAB SHIPPING CONDITIONS, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONDITION: Room Temperature\<RET\>

Are you adding 'Room Temperature' as

a new LAB SHIPPING CONDITIONS (the 1ST)? No// Y\<RET\> (Yes)

NAME: Room Temperature//\<RET\>

ABBREVIATION: RT\<RET\>

3.  LAB SHIPPING CONTAINER file (#62.91) contains the type of containers that the laboratory uses to ship lab test specimens. There are basically three types of containers used for shipping lab test specimens:
- Primary – specimen is shipped in the original collection container (i.e., Lavender top tube).
- Aliquot – specimen transferred to a tube/jar before shipment (i.e., Plastic Transport Tube, Brown PlasticTube).
- Packaging – packaging containers used for holding the specimen containers (i.e., box).

> This is the THIRD file to be configured using the CTE or Edit Shipping Container \[LA7S EDIT 62.91\] option.

Example: How to use the CTE Edit Shipping Container \[LA7S EDIT 62.91\] option

Select Lab liaison menu Option:SMGR\<RET\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CTE\<RET\> Edit Shipping Container

Use this option to setup the Lab Shipping Container file.

Select SHIPPING CONTAINER: ?\<RET\>

Answer with LAB SHIPPING CONTAINER NAME

You may enter a new LAB SHIPPING CONTAINER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONTAINER: Plastic Tube\<RET\>

Are you adding 'Plastic Tube' as

a new LAB SHIPPING CONTAINER (the 1ST)? No// Y\<RET\> (Yes)

NAME: Plastic Tube//\<RET\>

TYPE: ?\<RET\>

Enter what this container is used for.

Choose from:

1 PACKAGING

2 PRIMARY

3 ALIQUOT

TYPE: 3ALIQUOT\<RET\>

4.  LAB SHIPPING CONFIGURATION file (#62.9) contains the specimen volume, weight, collection end date/time (collection duration), patient height and weight. LOINC codes are used to identify patient height, weight and specimen weight when deemed appropriate. This is the FOURTH and final file to be configured by the COLLECTION facility using the CFE or Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

Example: How to use the CFE Edit Shipping Configuration option

\<TEST ACCOUNT\>Select Lab Shipping Management Menu Option: CFE Edit Shipping Configuration

Select SHIPPING CONFIGURATION: MAD

1 MADISON TO HINES

2 MADISON TO MILWAUKEE

3 MADISON TO QUEST

CHOOSE 1-3: 3 MADISON TO QUEST

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: 1 Collecting facility

NAME: MADISON TO QUEST//

COLLECTING FACILITY: WM S MIDDLETON MEM VA HOSP//

COLLECTING FACILITY'S SYSTEM: WM S MIDDLETON MEM VA HOSP

//

HOST FACILITY: QUEST//

HOST FACILITY'S SYSTEM: QUEST//

NON-VA SYSTEM IDENTIFIER: QDI// ??

If this is used to communicate with a non-VA system, enter the 2-3

character identifier used to name the HL7 application.

NON-VA SYSTEM IDENTIFIER: QDI//

ACCOUNT NUMBER: 113779// ??

If the system that you are shipping to requires an account number for

billing or other purposes enter the number here. It will be printed on

shipping manifests and transmitted in electronic messages if applicable.

ACCOUNT NUMBER: 113779// \<\<\< from Step 4a above.

TEST CODING SYSTEM: NON-VA// ??

If orders are being sent to a non-VA facility and the facility

cannot accept VA test order codes then answer with the type of

coding system. "NON-VA" indicates that the other system is using

a local coding system. The laboratory shipping software will then

use the non-VA test codes entered for each test on this

configuration.

If the non-VA facility can accept VA test codes then answer "NLT"

and the software will sent VA test order codes.

VA test order codes are usually NLT codes but in the future may

be LOINC codes. Selecting "LOINC" is currently not supported.

Support will be added in a future version of the LEDI software

when LOINC coding has been implemented within VA facilities.

Choose from:

0 NLT

1 NON-VA

2 LOINC

TEST CODING SYSTEM: NON-VA//

SPECIMEN CODING SYSTEM: ??

Collecting facility:

If orders are sent to a non-VA facility and the

facility cannot receive HL7 specimen codes from HL7

table 0070 then answer with the type of coding system

"LOCAL".

Choose from:

0 HL7 TABLE 0070

1 LOCAL-NON HL7

SPECIMEN CODING SYSTEM:

STATUS: ACTIVE// ??

This field is used to designate whether this shipping configuration is

"active", i.e. selectable by the user for use in building, processing

and receipting shipments of laboratory test.

Choose from:

0 INACTIVE

1 ACTIVE

STATUS: ACTIVE//

LAB MESSAGING LINK: LA7V HOST QDI// ??

This field is used to link a shipping configuration with an electronic

transmission of shipping manifests. When a shipping manifest is shipped, this field is checked to determine if the software should transmit the orders on the manifest to the host facility. It identifies the entry in the LA7 MESSAGE PARAMETER file \#62.8 to use for building and transmitting the manifest.

Choose from:

LA7V COLLECTION 585

LA7V COLLECTION 676

LA7V COLLECTION 695

LA7V HOST 578

LA7V HOST 695

LA7V HOST QDI

UNIVERSAL INTERFACE

LAB MESSAGING LINK: LA7V HOST QDI//

SHIPPING METHOD: COURIER// ??

This field is used to designate the method of shipment used by a shipping configuration. Examples could be courier, taxi, commercial carrier, etc.

COURIER

SHIPPING METHOD: COURIER// \<ENTER\>

BARCODE MANIFEST: YES// ??

This field determines if site/patient/specimen information is barcoded

on the shipping manifest when it has a status of "shipped".

There are two styles of bar codes. The regular style (code="YES"), which was released with the original version of Laboratory Electronic Data Interchange (LEDI), produces a long bar code. If the receiving site, which is reading these type of bar codes, has problems then switch to the compact style (code="YES-COMPACT"). This will produce a shorter bar code.

Choose from:

0 NO

1 YES

2 YES-COMPACT

BARCODE MANIFEST: YES//

MANIFEST RECEIPT: YES// ??

Allows site to have a receipt printed with a shipping manifest when the status of the manifest is "SHIPPED". This receipt can be used to record acknowledgment of receipt of the shipment by the courier service used to transport the specimens to the host facility.

Choose from:

0 NO

1 YES

MANIFEST RECEIPT: YES//

INCLUDE UNCOLLECTED SPECIMENS: NO// ??

If specimens that are still pending receipt in lab are to build on a

shipping manifest then answer "YES". If only specimens that have been received in the lab, i.e. have a lab arrival time, are to build then

answer "NO".

If field is blank then default is "NO".

Choose from:

0 NO

1 YES

INCLUDE UNCOLLECTED SPECIMENS: NO//

Select TEST/PROFILE: INTERLEUKIN 6// ??

You may enter a new TEST/PROFILE, if you wish

Enter the laboratory test that is used by this shipping

configuration.

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or

PRINT NAME

Do you want the entire 3537-Entry LABORATORY TEST List?

Select TEST/PROFILE: INTERLEUKIN 6//

TEST/PROFILE: INTERLEUKIN 6//

ACCESSION AREA: QUEST// ??

COLLECTION FACILITIES:

This field is used to designate the accession area to check when

searching for tests to build onto a shipping manifest. If it is blank

then the building process will skip over this test.

ACCESSION AREA: QUEST//

DIVISION: WM S MIDDLETON MEM VA HOSP// ??

Collecting facilities:

If the manifest building process should only build accessions'

from a certain division on a manifest then enter the division

to screen these accessions. The division used here will be the

division associated with the user who created the accession.

This field will allow a site to screen accessions from

multiple divisions, only placing on the manifest an accession

from the specified division.

DIVISION: WM S MIDDLETON MEM VA HOSP//

SPECIMEN: ??

This field is used to determine if a test for a particular specimen type should build on the shipping manifest. If left blank, i.e. no entry then

all specimens for this test are eligible for building on a shipping manifest. If a specimen type is entered then the specimen type of the accession must match before the test is eligible for building onto a shipping manifest. SPECIMEN:

URGENCY: ??

COLLECTING FACILITIES:

If shipping laboratory tests that are a certain

urgency, specify the urgency that must match the

test urgency of the accession for the accession/test

to be placed on the shipping manifest.

Choose from:

1 EMERGENCY

2 STAT

3 PRIORITY

4 PRE-OP

5 OPR

6 ADMIT

7 OUTPATIENT

8 TODAY

9 ROUTINE

URGENCY:

SPECIMEN CONTAINER: ALIQUOT// ??

COLLECTING FACILITIES:

The container used to hold the specimen. This could be the original collection container or a tube/vial/jar that the specimen is transferred to prior to shipment to another facility. It is the container that actually hold/contains the specimen.

Choose from:

ALIQUOT

PRIMARY

TRANS MEDIA

SPECIMEN CONTAINER: ALIQUOT//

SHIPPING CONDITION: FROZEN// ??

COLLECTING FACILITIES:

This field describes under what temperature/environmental condition the specimen is to be shipped. Examples would be frozen, refrigerated or ambient temperature.

Choose from:

FECES-ROOM TEMP

FROZEN

INCUBATOR

REFRIGERATED

ROOM TEMPERATURE

URINE-REF

SHIPPING CONDITION: FROZEN//

PACKAGING CONTAINER: PACKAGE// ??

COLLECTING FACILITIES:

This field is used to determine what packaging container a test's specimen container is placed in when the specimen is being shipped to another facility.

Choose from:

PACKAGE

PACKAGING CONTAINER: PACKAGE//

NON-VA TEST ORDER CODE: 46557P// ??

Collecting facilities:

If sending test orders to a non-VA facility use

this field to store the test order codes used

by the non-VA system. It will be used when the

TEST CODING SYSTEM field (#.14) is set to "NON-VA".

NON-VA TEST ORDER CODE: 46557P//

NON-VA TEST ORDER NAME: INTERLEUKIN 6// ??

Collecting facility:

If sending test orders to a non-VA facility use

this field to store the test order name used

by the non-VA system. The lab software to identify

the test name on the non-VA system when orders are

transmitted electronically uses this field. It will

be used when the TEST CODING SYSTEM field (#.14) is

set to "NON-VA".

NON-VA TEST ORDER NAME: INTERLEUKIN 6// \<ENTER\>

NON-VA TEST CODING SYSTEM: ??\<ENTER\>

Collecting facilities: \<ENTER\>

If sending test orders to a non-VA facility use

this field to store the name of the coding system

used by the non-VA system. It will be used when the

TEST CODING SYSTEM field (#.14) is set to "NON-VA".

Name usually begins with "99" to indicate a local

coding system in the HL7 Standard.

NON-VA TEST CODING SYSTEM:

REQUIRE PATIENT HEIGHT: ??

Allows site to specify that the patient's height be sent with

an order for this test. Patient's height will be prompted for

and printed on manifest.

Choose from:

0 NO

1 YES

REQUIRE PATIENT HEIGHT: Y YES

PATIENT HEIGHT UNITS: ??

Units used to measure the patient's height.

Select an entry from the LAB ELECTRONIC CODE

file (#64.061) that are measurements.

PATIENT HEIGHT UNITS: IN in MEASUREMENTS Inches

PATIENT HEIGHT CODE: ??

Select the appropriate LOINC code to identify

the patient's height.

PATIENT HEIGHT CODE:

REQUIRE PATIENT WEIGHT: YES// ??

Determines if the patient's weight is required

to be sent in the HL7 ORM order message and

printed on the shipping manifest. Actual

shipping and/or electronic transmission of a

shipping manifest will check for entry of the

patient's weight and prevent release if absent.

Choose from:

0 NO

1 YES

REQUIRE PATIENT WEIGHT: Y YES

PATIENT WEIGHT UNITS: ??

Units used to measure the patient's weight.

Select an entry from the LAB ELECTRONIC CODE

file (#64.061) that are measurements.

PATIENT WEIGHT UNITS:

PATIENT WEIGHT CODE: ??

Select the appropriate LOINC code to identify

the patient's weight.

PATIENT WEIGHT CODE: \<ENTER\>

REQUIRE COLLECTION VOLUME: YES// ??\<ENTER\>

Determines if the specimen's collection volume

is required to be sent in the HL7 ORM order

message and printed on the shipping manifest.

Actual shipping and/or electronic transmission

of a shipping manifest will check for entry of

the specimen's collection volume and prevent

release if absent.

Choose from:

0 NO

1 YES

REQUIRE COLLECTION VOLUME: NO// Y YES \<ENTER\>

COLLECTION VOLUME UNITS: ml// ??\<ENTER\>

Units used to measure the specimen's collection

volume. Select an entry from the LAB ELECTRONIC

CODE file \#64.061) that is a measurement.

COLLECTION VOLUME UNITS: ml// \<ENTER\>

COLLECTION VOLUME CODE: 3160// ??\<ENTER\>

Enter the appropriate LOINC code to identify

the specimen's collection volume.

COLLECTION VOLUME CODE: 3160// 3160 -9\<ENTER\>

SPECIMEN VOLUME:VOL:PT:SMN:QN \<ENTER\>

REQUIRE COLLECTION WEIGHT: YES// ??\<ENTER\>

Determines if the specimen's collection weight

is required to be sent in the HL7 ORM order

message and printed on the shipping manifest.

Actual shipping and/or electronic transmission

of a shipping manifest will check for entry of

the specimen's collection weight and prevent

release if absent.

Choose from: \<ENTER\>

0 NO

1 YES

REQUIRE COLLECTION WEIGHT: Y YES \<ENTER\>

COLLECTION WEIGHT UNITS: ??\<ENTER\>

Units used to measure the specimen's collection weight.

Select an entry from the LAB ELECTRONIC CODE file

( \#64.061) that is a measurement.

COLLECTION WEIGHT UNITS: \<ENTER\>

COLLECTION WEIGHT CODE: ??\<ENTER\>

Enter the appropriate LOINC code to identify

the specimen's collection weight.

COLLECTION WEIGHT CODE: \<ENTER\>

REQUIRE COLLECTION END D/T: YES// ??\<ENTER\>

Determines if the specimen's collection end

date/time is required to be sent in the HL7 ORM

order message and printed on the shipping

manifest. Actual shipping and/or electronic

transmission of a shipping manifest will check

for entry of the specimen's collection end

date/time and prevent release if absent.

Choose from: \<ENTER\>

0 NO

1 YES

REQUIRE COLLECTION END D/T: YESCOLLECTION DURATION UNITS: hr// ?? \<ENTER\>

Units used to calculate the specimen's

collection duration. Select an entry from the

LAB ELECTRONIC CODE file (#64.061) that is a

measurement and relates to time. // Y YES\<ENTER\>

Choose from:

hr hr MEASUREMENTS Hour

min min MEASUREMENTS Minute

s s MEASUREMENTS Seconds

COLLECTION DURATION UNITS: hr// \<ENTER\>

COLLECTION DURATION CODE: 24454// ??\<ENTER\>

Enter the appropriate LOINC code to identify

the specimen's collection duration.

COLLECTION DURATION CODE: 24454// 24454 -1\<ENTER\>

COLLECTION DURATION:TIME:\*:GAST:QN\<ENTER\>

Select TEST/PROFILE: \<ENTER\>

3\. LIM: Setup the Lab Auto-instrument and HL7 Environment to receive results from HOST facility labs.

> Use the LEDI Setup \[LA7V SETUP\] option to setup the Lab Auto-instrument and HL7 Environment. This option is located on the Lab Shipping Management menu \[LA7S MGR MENU\] of the Lab Liaison menu \[LRLIASON\].

NOTES: TCP/IP MUST be used as the HL7 transport protocol for VA to Reference Lab interfaces.

> **NOTE:** The two-institution names used in the following screen displays are examples ONLY. Do NOT use these two institutions host or collection facility.

Example: How to use the LEDI Setup \[LA7V SETUP\] option to setup the Lab Auto-instrument and HL7 Environment.

Select Lab Shipping Management Menu Option: lsu\<RET\> LEDI Setup

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. HINES HOSPITAL (LA7V HOST 578)

2\. MILWAUKEE VAMC (LA7V HOST 695)

3\. Add HOST Lab

Enter a number (1-2): 1\<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HINES HOSPITAL (LA7V HOST 578)

2\. MILWAUKEE VAMC (LA7V HOST 695)

3\. QUEST (LA7V HOST QDI)

4\. Add HOST Lab

Enter a number (1-3): 3\<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab:

Enter a number (1-1): 1\<ENTER\>

Select INSTITUTION NAME: ??\<ENTER\>

Choose from: \<ENTER\>

13TH & MISSION CA D 662BU

410TH STRATEGIC HOSPITAL SGAM MI

ABERDEEN SD CBOC 438GD

ABILENE, KS (CBOC) KS CBOC 589GK

ABILENE, TX (CBOC) TX CBOC 519HC

ABILENE, TX (ORC) TX ORC 519HA

AIR FORCE USAF 381

AKRON OH CBOC 541GG

ALAMOGORDO NM CBOC 501GI

Select INSTITUTION NAME: QUEST\<ENTER\>

Setting up the following Host Labs for QUEST

Updating HL7 APPLICATION PARAMETER file (#771).

Adding LA7V HOST QDI

Updating PROTOCOL file (#101).

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Receive Results from QDI

Adding LA7V Receive Results from QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Process Results from QDI

Adding LA7V Process Results from QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Order to QDI

Adding LA7V Order to QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Send Order to QDI

Adding LA7V Send Order to QDI

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab QUEST.

Adding LA7V HOST QDI

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab QUEST.

Adding LA7V HOST QDI

HL7 v1.6 Environment setup is complete!!

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: KA7VQDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): 2\<ENTER\>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from TOMAH VAMC

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from QDI

LA7V Send Order to QDI

Enter a Logical Link: (MM/TCP): \<RET\> tcp TCP/IP

Updating the PROTOCOL file (#101).

------------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: LA7QDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): 3\<ENTER\>

GRACE PERIOD FOR MESSAGES: ??

Grace period determines the number of days that messages for this configuration are kept on the system before purging when the message status is "purgeable". If this field is left blank, the system assumes 3 days. These messages are found in the LA7 MESSAGE QUEUE file (#62.49).

When messages have status of "error" they remain on the system until their corresponding error message is removed from the XTMP global by a KERNEL cleanup task. The messages then become "purgeable".

GRACE PERIOD FOR MESSAGES: 30

LOG ERRORS: ON// ??

If turned on, errors or exceptional conditions that occur during message processing are stored in the ^XTMP global for review. To review the log, in programmer mode, type D PRINT^LA7LOG.

Choose from:

0 OFF

1 ON

LOG ERRORS: ON//

MULTIPLE ORDERS: ??

Determines when building a HL7 message if message should contain only

one patient/order or multiple patients/orders.

Default is multiple patients per message if possible.

This allows site to configure message building when communicating with

a non-VA system that cannot handle a message that has more than one

patient in the message. It applies to both order (ORM) and result

(ORU) messages.

When communicating with a VA facility this field can be left blank

(default) or set to 0 - MULTIPLE PATIENTS

If the receiving system can only accept one patient per HL7 message

then select 1 - SINGLE PATIENT. This will place multiple orders or

results for multiple orders in one message but only one patient will

be contained in the message.

If the receiving system can only accept one order per HL7 message then

select 2 - SINGLE ORDER. This will place in the message one order or

the results associated with one order for a single patient

> **NOTE:** An order in the VA is considered those tests found on one

accession. What the VA considers as an accession other non-VA systems

may refer to as an order.

Choose from:

0 MULTIPLE PATIENTS

1 SINGLE PATIENT

2 SINGLE ORDER

MULTIPLE ORDERS: 2 SINGLE ORDER

Select ALERT CONDITION: ??

You may enter a new ALERT CONDITION, if you wish

This field allows the user to identify whether to receive alerts when

there are new results and when an error is logged to the ^XTMP global.

Choose from:

1 NEW RESULTS

2 ERROR ON MESSAGE

3 ORDERS RECEIVED

Select ALERT CONDITION: 1 (1 NEW RESULTS) \<ENTER\>

Are you adding 'NEW RESULTS' as a new ALERT CONDITION (the 1ST for this LA7 ME

SSAGE PARAMETER)? No// y (Yes) \<ENTER\>

MAIL GROUP: lab ledI\<ENTER\>

Select ALERT CONDITION: 2 (2 ERROR ON MESSAGE)

Are you adding 'ERROR ON MESSAGE' as a new ALERT CONDITION

(the 2ND for this LA7 MESSAGE PARAMETER)? No// y (Yes) \<ENTER\>

MAIL GROUP: lab ledi\<ENTER\>

Select ALERT CONDITION: \<ENTER\>

-----------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: LA7VQDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): 4\<ENTER\>

AUTOMATED INSTRUMENT: LA7V HOST QDI

LOAD/WORK LIST: QUEST// ??

This points to the single worklist where processed data from the LA global is to be directed.

Choose from:

This will list available Load/Work lists in your system

LOAD/WORK LIST: QUEST//

METHOD: ??\<ENTER\>

This is the name of the method or instrument used.

METHOD:

DEFAULT ACCESSION AREA: ??

This field contains the default accession list name for this instrument.

Points to FILE \#68.

Choose from:

Lists available accession areas for your system

DEFAULT ACCESSION AREA: SEND

1 SEND SEND OUT

2 SENDOUT HINES

3 SENDOUT MILWAUKEE

4 SENDOUT UW

CHOOSE 1-4: 1 SEND OUT

OVERLAY DATA: ??

Setting this field to YES will cause a rerun of instrument data

to overlay existing data.

Choose from:

0 NO

1 YES

OVERLAY DATA:

STORE REMARKS: YES// ??

This field controls if comments that are associated with an accession

or specimen are stored with the results. The default is NO.

There is a similar companion field at the test level which controls

comments associated with tests results.

Choose from:

0 NO

1 YES

STORE REMARKS: YES// \<RET\>

Add Chem Tests to the LA7V HOST 676 Automated Instrument for TOMAH VAMC.

Select CHEM TESTS: ??

You may enter a new CHEM TESTS, if you wish

This contains the test names for this instrument.

Choose from:

\#DRUG 1

\#DRUG 1 IN COMBINATION

\#DRUG 2

^

Select CHEM TESTS: LAMOTRIGINE

Are you adding 'LAMOTRIGINE' as a new CHEM TESTS (the 1ST for this AUTO INSTRUMENT)? No// Y\<RET\> (Yes)

CHEM TESTS NUMBER: 1// ????\<RET\>

TYPE A WHOLE NUMBER BETWEEN 1 AND 999

CHEM TESTS NUMBER: 1//

CHEM TESTS TEST: LAMOTRIGINE// ??

This contains the test names for this instrument.

CHEM TESTS TEST: LAMOTRIGINE//\<RET\>

TEST: LAMOTRIGINE// \<RET\>

PARAM 1: ??\<RET\>

This is used to extract a test from a data stream. It may contain a line number or character number.

PARAM 1: \<RET\>

UI TEST CODE: 81499.0000// ??\<RET\>

For traditional interfaces:

This is the code to send the instrument for downloading of load lists

that this test is requested.

This field used by various BI-DIRECTIONAL INTERFACES

eg. for test BUN enter / as the download code for the ETACHEM instrument.

For Universal Interfaces:

For sites using this instrument in a Universal Interface

configuration, this field is used to define the instrument 'name' for

a test. This 'name' is used as an identifier for the test in all

messages sent to and from the instrument. It is important that the

Universal Interface PC has the name defined in this instrument's

configuration exactly as it is here in the auto instrument file,

including upper and lower case.

This field does NOT have to be the test name, but can be. The name of

this field should not be taken literally, it is used for both

uploading and downloading, uni-directional as well as bi-directional.

UI TEST CODE: 81499.0000//78901 \<\<\<Result code provided by Ref. Lab

ACCEPT RESULTS FOR THIS TEST: ??

Determines if results (HL7 OBX segments) are processed and stored.

If nothing is entered, the default will be 'Yes'.

If "YES" is selected then all test results are processed and stored.

Select "NO" to suppress the processing and storing any test result.

Selecting "FINAL ONLY" will only process/store test results when the

result has a status of C,F,U as defined in table 0085 below.

If there is MUMPS code in PARAM 1, it will be executed regardless of

how this field is set.

To accept results for this test based on other factors, or in other

word s -

'On the fly', you can set a variable in PARAM 1 as follows:

PARAM 1: S:(CONDITION) LA7XFORM(3)=1

Where CONDITION is some MUMPS value that equates to true or false. Consult a programmer before trying this.

Table 0085 - Observation result status codes interpretation

Value Description

C Record coming over is a correction and thus replaces a final result

D Deletes the OBX record

F Final results; Can only be changed with a corrected result.

I Specimen in lab; results pending

P Preliminary results

R Results entered -- not verified

S Partial results

X Results cannot be obtained for this observation

U Results status change to Final. without retransmitting results

already sent as 'preliminary.' E.g., radiology changes status

from preliminary to final

W Post original as wrong, e.g., transmitted for wrong patient

Choose from:

0 NO

1 YES

2 FINAL ONLY

ACCEPT RESULTS FOR THIS TEST: Y YES \<ENTER\>  

IGNORE RESULTS NOT ORDERED: ??

This field should be set to 'Yes' if you want to restrict results to

only those tests that were ordered.

For example, if an electrolytes panel was ordered consisting of:

Sodium

Potassium

Chloride

CO2

And the instrument running the sample also reported a BUN result, the

BUN would not be reported if this field was set to 'Yes'.

To ignore results not ordered based on other factors, or in other words

'On the fly', you can set a variable in PARAM 1 as follows:

PARAM 1: S:(CONDITION) LA7XFORM(5)=1

Where CONDITION is some MUMPS value that equates to true or false. Consult

a programmer before trying this.

Choose from:

0 NO

1 YES

IGNORE RESULTS NOT ORDERED:

STORE REMARKS: YES// ??

Determines if remarks/comments (HL7 NTE segments) are processed and

stored with results. This applies only to remarks/comments that

relate to a test.

Select "NO" to suppress the processing and storing of any

remarks/comments associated with a test result.

If "YES" is selected then all remarks/comments associated with a

test result are processed and stored.

The default value is "NO".

Selecting "FINAL ONLY" will only process and store remarks/comments

when the associated test result has a status of C,F,U as defined in

table 0085 below. This only applies to NTE segments that follow OBX

segments.

Table 0085 - Observation result status codes interpretation

Value Description

C Record coming over is a correction and thus replaces a final result

D Deletes the OBX record

F Final results; Can only be changed with a corrected result.

I Specimen in lab; results pending

P Preliminary results

R Results entered -- not verified

S Partial results

X Results cannot be obtained for this observation

U Results status change to Final. without retransmitting results

already sent as 'preliminary.' E.g., radiology changes status

from preliminary to final

Choose from: \<ENTER\>

0 NO

1 YES

2 FINAL ONLY

STORE REMARKS: YES// YES\<ENTER\>

REMARK PREFIX: ??\<ENTER\>

Used by the Lab Universal Interface software when processing HL7

messages that contain NTE (notes) segments which follow OBX (test results)

segments. These NTE segments apply to the test, not to the specimen.

This field is used in conjunction with field STORE REMARKS (#18)

in the CHEM TESTS multiple. If field STORE REMARKS is set to YES

then the value of this field, if any, will be used as the prefix

to the remarks when storing the remark in the LAH global.

Example: If the text "For test POTASSIUM: " is entered in this field

and a remark is received associated with this test that states

"Specimen hemolyzed" then the remark which will be stored is

"For test POTASSIUM: Specimen hemolyzed".

REMARK PREFIX: \<ENTER\>

Select CHEM TESTS: \<ENTER\>  
2. IRM: Complete HL7 Environment Setup for TCP/IP HL7 Transport Protocol

> The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information used within the Systems Link Monitor, which provides the users feedback regarding the status of each link.

> Use the Link Edit \[HL EDIT LOGICAL LINKS\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\] to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section. Set the AUTOSTART field (#4.5) entry to ‘1’ (Enabled) if you want this to start automatically after TaskMan is restarted. Otherwise, these links will need to be manually started using the Start/Stop Links \[HL START\] option within the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu within the HL7 Main Menu \[HL MAIN MENU\].

> **NOTE:** Please consult the VistA HEALTH LEVEL SEVEN (HL7) SITE MANAGER & DEVELOPER MANUAL for information on single and multi-threaded listeners.

> For VA to commercial reference lab LEDI interfaces the LEDI III software uses the site’s standard HL7 TCP listener on port 5000 to receive HL7 messages.

Setup the ‘client’ device(s) for the HOST facility laboratory. The client device is the link that connects to the other facilities’ listener device to transmit order messages from a COLLECTION facility and to transmit result messages from a HOST facility. A separate client device needs to be created for each facility that you will be sending the LEDI manifests to.

> The setup is as follows:

- NODE: LA7Vyyy - Where yyy is the commercial reference lab three character identifier specified in the LAB SHIPPING CONFIGURATION file (#62.9)
- LLP TYPE: TCP
- DEVICE TYPE: Non-Persistent Client
- QUEUE SIZE: 10HL7 package default
- RE-TRANSMISSION ATTEMPTS: 5 - pick a reasonable attempt value.
- TCP/IP ADDRESS: nnn.nnn.nnn.nnn - IP address of the commercial reference lab system.
- TCP/IP PORT: - The port the host lab’s listener device is listening on.
- TCP/IP SERVICE TYPE: CLIENT (Sender)
- PERSISTENT: NO – unless volume of message traffic dictates a persistent connection.

5\. LIM: Work with interface coordinator at reference laboratory to test system

> **NOTE:** Use a mirrored account to test the interface if possible. Order laboratory test(s) on a test patient, build them on a shipping manifest, close and ship the manifest, then provide the interface coordinator with the manifest \#. The interface coordinator should be able to receive in the manifest and enter test results. A View Alert will be generated in the collecting site indicating results are available. The COLLECTING facility LIM should then be able to verify the lab test result(s) on the test patient via EA Enter/verify data (auto instrument) using the Load List and workload areas created in Step 4 above.

6. LIM: Train Users

> Please see the ‘Use of the Software’ section of this guide.

### LEDI III Implementation Configuration Setup Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This checklist is provided to ensure that all required LEDI III Implementation setup instructions have been completed.

Checklist for COLLECTION facility setting up HOST facilityNOTE: Use this checklist to confirm that the *LEDI III* Step 5—LIM (COLLECTION facility): Lab Shipping Files Setup, located in the Implementation Section of this manual, has been completed as instructed.

1\. Enter the name of the HOST facility in the INSTITUTION file (#4), NAME field (.01).

> The Institution Master File maintains nationally controlled entries. Currently the VA Institution Master File maintains entries for VAMC and DoD facilities.

> **NOTE:** DoD facilities are added by Kernel patch XU\*8.0\*161. Follow instructions contained in this patch to install these DoD facilities in your local INSTITUION file (#4). At the current time VAMC’s will need to locally add non-VISTA, Non-DoD organizations to the local INSTITUION file (#4) using the Kernel options to maintain this file.

> If the HOST facility is a VA Institution, then verify that the:

> AGENCY CODE field (#95) = “VA” and the

> STATION NUMBER field (#99) = A unique Central Office assigned station number.

> If the host facility is a DoD Facility, then verify that the:

> AGENCY CODE field (#95) =

> “AF” - AIR FORCE

> “ARMY” - ARMY

> “N” - NAVY”

> CODING SYSTEM: DMIS ID: 4 digit id

> If the HOST facility is a non-VistA, non-DoD Institution then verify that the:

> AGENCY CODE field (#95) = “OTHER” and the

> STATION NUMBER field (#99) = \<blank\>

2\. Set up LAB SHIPPING METHOD file (#62.92).

> Use the Edit Shipping Method \[LA7S EDIT 62.92\] option.

3\. Set up LAB SHIPPING CONDITION file (#62.93).

> Use Edit Shipping Condition \[LA7S EDIT 62.93\] option.

4\. Set up LAB SHIPPING CONTAINER file (#62.91)

> Use Edit Shipping Container \[LA7S EDIT 62.91\] option.

5\. Set up LAB SHIPPING CONFIGURATION (#62.9)

> Use the Edit Shipping Configuration \[LA7S EDIT 62.9\] option to configure this file. When initially setting up the lab shipping configuration, DO NOT edit the LAB MESSAGING LINK field (#.07) of this file. This field will be filled in after the LEDI Setup option \[LA7V SETUP\] configures the HL7 interface for this configuration. If the host facility is a non-VA/non-DoD facility, then determine a three-letter identifier to assign in lieu of the VA Station Number/DoD DMIS ID code.

> **NOTE:** See Step 5—LIM (COLLECTION facility): Lab Shipping Files Setup in the Implementation Section of this manual for examples used during software testing for several Commercial Reference Laboratories.

6\. When setting up an electronic link (HL7 interface) to the HOST facility laboratory, use the LEDI Setup \[LA7V SETUP\] option to add/edit a HOST lab. This option will setup the Lab and HL7 files for the HL7 interface to the host facility.

7\. If using the HL7 TCP/IP communication protocol, have IRM complete the HL LOGICAL LINK file (#870) setup using the HL package option Link Edit \[HL EDIT LOGICAL LINKS\] to edit a logical link when communicating with non-VA facilities. When setting up LEDI between VA facilities the standard HL7 VAxxx logical links are utilized.

8\. If an electronic link (HL7 interface) has been setup for this HOST facility, then use the Edit Shipping Configuration \[LA7S EDIT 62.9\] option to edit the LAB MESSAGING LINK field (#.07) to link the shipping configuration to the HL7 interface. Select the message configuration “LA7V HOST xxx” (i.e., xxx is the VA station number of the HOST facility, the 4 digit DMIS ID of DoD facilities or the three-letter identifier previously assigned for a non-VA, non-DoD facility). The LEDI Setup \[LA7V SETUP\] option will attempt to fill in this field. However, if you have multiple shipping configurations for the same COLLECTION and HOST facility you will need to manually setup these configurations.

### HOST facility setting up COLLECTION facility ChecklistNOTE: Use this checklist to ensure that Step 6—LIM (HOST facility): LAB SHIPPING CONFIGURATION file (#62.9) setup, located in the Implementation section of this manual, has been completed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Enter/configure the collecting facility entry in INSTITUTION file (#4).

> The Institution Master File maintains nationally controlled entries.

> If the collecting facility is a VA institution, then verify that:

> AGENCY CODE field (#95) = “VA”

> STATION NUMBER field (#99) = Unique Central Office assigned station number.

> If the collecting facility is a DoD Facility, then verify that:

> AGENCY CODE field (#95) =

> “AF” - AIR FORCE

> “ARMY “ - ARMY

> “N” - NAVY”

> CODING SYSTEM: DMIS ID: 4 digit id

> If the collecting facility is a non-VistA, non-DoD institution (then verify that):

> AGENCY CODE field (#95) = “OTHER”

> STATION NUMBER field (#99) = \<blank\>

2\. Set up SHIPPING CONFIGURATION file (#62.9).

> Use the Edit Shipping Configuration \[LA7S EDIT 62.9\] option.

> When asked how the configuration is being edited, specify “HOST facility.”

> Add local lab tests that the COLLECTING facility will be shipping, specifying local collection sample and urgency to use to build the LAB PENDING ORDERS ENTRY file (#69.6) entries. If COLLECTING facility is a non-VA facility, then determine a three-letter identifier to assign in lieu of the VA Station Number. See Step 5—LIM: Lab Shipping Files Setup above for suggested values of some commercial reference laboratories.

> If setting up an electronic link (HL7 interface) to the COLLECTION lab use LEDI Setup \[LA7V SETUP\] option to add/edit a COLLECTION lab. This option will setup the Lab and HL7 files for the HL7 interface to the collection facility.

> If using HL7 TCP/IP interface have IRM complete the HL LOGICAL LINK file (#870) setup.

> If using the HL7 TCP/IP interface, have IRM complete the HL LOGICAL LINK file (#870) setup using the HL package option Link Edit \[HL EDIT LOGICAL LINKS\] to edit a logical link when communicating with non-VA facilities. When setting up LEDI between VA facilities the standard HL7 VAxxx logical links are utilized.

LEDI III USER GUIDE

# Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the LEDI III User Guide contains information for END USERS to competently operate the software application using a task-oriented approach. Examples for using the LEDI III software are also provided.

NOTES: With this release of LEDI, the verification, release and storage in VistA of laboratory test results for “CH” subscript tests has been changed as follows:

- Laboratory result verification has been enhanced to allow the designation of a performing laboratory and the use of the performing laboratory's units, normals, and normalcy status in results reporting.

> User during the verification process is able to specify the performing laboratory. The performing laboratory is selected from the list of available entries in the site’s INSTITUTION file (#4). The selection of entries is screened as follows:

> a\. User can select the division they are logged on.

> b\. User can select an institution that is configured in the LAB SHIPPING CONFIGURATION file (#62.9) as a host facility with their division as the COLLECTING facility.

> During acceptance and verification of results received from a reference laboratory via an HL7 interface (LEDI), the performing laboratory, results, units, normals and normalcy status contained in the HL7 message are stored “as is”.

- Users using the Enter/verify/modify data (manual) \[LRENTER\] option to enter results manually from a reference laboratory can use the units and normals specified in LABORATORY TEST file (#60) by configuring USE FOR REFERENCE TESTING field (#13) within the SITE/SPECIMEN subfile (#100).

> If this field is not enabled for reference laboratory result data entry, then the user is prompted for units, normals, high and low reference ranges to store with the results. The Edit atomic tests \[LRDIEATOMIC\] option allows Laboratory Information Manager (LIM) to designate this functionality for affected tests.

- Amended reports received via a LEDI HL7 interface can be processed via the Enter/verify/modify data (manual) option \[LRENTER\].
- Test result normals and units for all verified tests are now stored with the results in LAB DATA file (#63). Changes to units and normals can now be made to existing tests in LABORATORY TEST file (#60) without affecting previously reported results.

> However, there are potentially situations, which do not allow this feature to be implemented for a specific test. If a site has old results or has never archived then there may be results stored under a data name with no normals/units etc., which were entered using previous versions of the Laboratory package. When test results in LAB DATA file \#63 are found with no unit and/or normals the software goes back to LABORATORY TEST file \#60 to retrieve these values. Changing the units and/or normals associated with a File \#63 data name in File \#60 would alter the units/ and/or normals reported on previous results.

#### Lab Shipping Management Menu \[LA7S MGR MENU\]

### INTENDED END USERS: Laboratory Information Manager (LIM)/Laboratory Automated Data Processing Application Coordinator (ADPAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Lab Shipping Management Menu \[LA7S MGR MENU\] contains implementation related menus and options that should be assigned to the LIM. This menu is located on the Lab liaison menu \[LRLIAISON\].

Select Lab liaison menu Option: SMGR \<Enter\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?? \<Enter\>

CFE Edit Shipping Configuration \[LA7S EDIT 62.9\]

CTE Edit Shipping Container \[LA7S EDIT 62.91\]

CME Edit Shipping Method \[LA7S EDIT 62.92\]

CDE Edit Shipping Condition \[LA7S EDIT 62.93\]

LSU LEDI Setup \[LA7V SETUP\]

CAT Electronic Catalog Menu ... \[LA7S CATALOG MENU\]

#### Edit Shipping Configuration \[LA7S EDIT 62.9\] option

Example: This option is used to configure the LAB SHIPPING CONFIGURATION file (#62.9).

Select Lab Shipping Management Menu Option: CFE Edit Shipping Configuration \<Enter\>

Select SHIPPING CONFIGURATION: TRIPLER AMC\<Enter\>

Are you adding 'TRIPLER AMC' as

a new LAB SHIPPING CONFIGURATION (the 14TH)? No// Y (Yes) \<Enter\>

LAB SHIPPING CONFIGURATION COLLECTING FACILITY: HONOLULU

LAB SHIPPING CONFIGURATION HOST FACILITY: TRIPLER ARMY MEDICAL CENTER

Select one of the following: \<Enter\>

1 Collecting facility

2 Host facility

Are you editing this entry as the: 1 Collecting facility

NAME: TRIPLER AMC//\<Enter\>

COLLECTING FACILITY: HONOLULU//\<Enter\>

COLLECTING FACILITY'S SYSTEM: HONOLULU \<Enter\>

HOST FACILITY: TRIPLER ARMY MEDICAL CENTER//\<Enter\>

HOST FACILITY'S SYSTEM: TRIPLER ARMY MEDICAL CENTER

STATUS: A ACTIVE

LAB MESSAGING LINK: \<Enter\>

SHIPPING METHOD: COURIER

BARCODE MANIFEST: N \<Enter\> NO

MANIFEST RECEIPT: Y \<Enter\> YES

INCLUDE UNCOLLECTED SPECIMENS: N NO\<Enter\>

#### Edit Shipping Container \[LA7S EDIT 62.91\] option

Example: This option is to sets up the LAB SHIPPING CONTAINER file (#62.91).

Select Lab liaison menu Option: SMGR\<Enter\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ?

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CTE\<Enter\> Edit Shipping Container

Use this option to setup the Lab Shipping Container file.

Select SHIPPING CONTAINER: ?\<Enter\>

Answer with LAB SHIPPING CONTAINER NAME

You may enter a new LAB SHIPPING CONTAINER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONTAINER: Plastic Tube\<Enter\>

Are you adding 'Plastic Tube' as

a new LAB SHIPPING CONTAINER (the 1ST)? No// Y\<Enter\> (Yes)

NAME: Plastic Tube//\<Enter\>

TYPE: ?\<Enter\>

Enter what this container is used for.

Choose from:

1 PACKAGING

2 PRIMARY

3 ALIQUOT

TYPE: 3 ALIQUOT\<Enter\>

#### Edit Shipping Method \[LA7S EDIT 62.92\] option

Example: This option is use to configure the LAB SHIPPING METHOD file (#62.92).

Select Lab liaison menu Option: SMGR\<Enter\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ??\<Enter\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CME\<Enter\> Edit Shipping Method

Select SHIPPING METHOD: ?\<Enter\>

Answer with LAB SHIPPING METHOD NAME

You may enter a new LAB SHIPPING METHOD, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING METHOD: FEDEX\<Enter\>

Are you adding 'FEDEX' as a new LAB SHIPPING METHOD (the 1ST)? Y\<Enter\> (Yes)

NAME: FEDEX//\<Enter\>

Select Lab Shipping Management Menu Option: CME\<Enter\> Edit Shipping Method

Select SHIPPING METHOD: COURIER\<Enter\>

Are you adding 'COURIER' as a new LAB SHIPPING METHOD (the 2ND)? Y\<Enter\>

(Yes)

NAME: COURIER//\<Enter\>

#### Edit Shipping Condition \[LA7S EDIT 62.93\] option

Example: This option is used to sets up the LAB SHIPPING CONDITIONS file (#62.93).

Select Lab liaison menu Option: SMGR\<Enter\> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: ??\<Enter\>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

CAT Electronic Catalog Menu

Select Lab Shipping Management Menu Option: CDE\<Enter\> Edit Shipping Condition

Use this option to setup the Lab Shipping Condition file.

Select SHIPPING CONDITION: ?\<Enter\>

Answer with LAB SHIPPING CONDITIONS NAME

You may enter a new LAB SHIPPING CONDITIONS, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONDITION: Room Temperature\<Enter\>

Are you adding 'Room Temperature' as

a new LAB SHIPPING CONDITIONS (the 1ST)? No// Y\<Enter\> (Yes)

NAME: Room Temperature//\<Enter\>

ABBREVIATION: RT\<Enter\>

#### LEDI Setup \[LA7V SETUP\] option

This option sets up the HL7 and Lab Auto Instrument environment for a HOST or COLLECTION system and entries in the HL7 APPLICATION PARAMETER file (#771), HL LOGICAL LINK file (#870), HL LOWER LEVEL PROTOCOL PARAMETER file (#869.2)

PROTOCOL file (#101), AUTO INSTRUMENT file (#62.4), and the LA7 MESSAGE PARAMETER file (#62.48).

> **NOTE:** See examples in the Implementation guide section Steps \#6 and \#7.

### Electronic Catalog Menu \[LA7S CATALOG MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains the three options that are used to maintain, produce, and print the laboratory test available for the COLLECTION facility to order. This submenu is located on the Lab Shipping Management Menu \[LA7S MGR MENU\] consisting of the following options.

### INTENDED END USERS: LIM/Lab ADPAC, HOST and COLLECTION facility Laboratory staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Electronic Catalog Information Entry \[LA7S CATALOG ENTRY\] Option

Example: This option allows the user to enter laboratory test information for the electronic catalog.

ENT Electronic Catalog Information Entry \[LA7S CATALOG ENTRY\]

IND View Individual Electronic Catalog Entry \[LA7S VIEW

INDIVIDUAL ENTRY\]

ALL Electronic Catalog Print \[LA7S PRINT CATALOG\]

Select Electronic Catalog Menu Option: ENT Electronic Catalog Information Entry\<Enter\>

Select LABORATORY TEST NAME: PROSTATE SPECIFIC ANTIGEN

NAME: PROSTATE SPECIFIC ANTIGEN Replace

NATIONAL VA LAB CODE: Prostate Specific Ag// \<Enter\>

RESULT NLT CODE: Prostate Specific Ag//\<Enter\>

CATALOG ITEM: YES//\<Enter\>

COST: 11.18

PRICE: 22.36

Select SPECIMEN: SERUM//\<Enter\>

SPECIMEN: SERUM//\<Enter\>

SP COST: 21.32

SP PRICE: 32.72

Select SPECIMEN: ^

#### View Individual Electronic Catalog Entry \[LA7S VIEW INDIVIDUAL ENTRY\] option

Example: This option allows the user to view or print an individual entry in the Electronic Test Catalog.

ENT Electronic Catalog Information Entry

IND View Individual Electronic Catalog Entry

ALL Electronic Catalog Print

Select Electronic Catalog Menu Option: IND View Individual Electronic

Catalog Entry

Select LABORATORY TEST NAME: PROSTATE SPECIFIC ANTIGEN

DEVICE: VIRTUAL TERMINAL

Electronic Test Catalog JUL 10,1997 14:08 PAGE 1

-----------------------------------------------------------------------

PROSTATE SPECIFIC ANTIGEN

Collection Tube: BLOOD RED OR GOLD

Ship 1 ml aliquot; Refrigerate

Site/Specimen: SERUM

Snomed: 0X500

Reference Low: 0

Reference High: 4.0

Units: ng/mL

NLT Code: 89760.0000 +Prostate Specific Ag

NLT Result Code: 89760.0000 +Prostate Specific Ag

Default Cost: 11.18 Default Price: 22.36

Specimen: SERUM

Specimen Cost: 21.32 Specimen Price: 32.72

#### Electronic Catalog Print \[LA7S PRINT CATALOG\] option

Example: This option allows the user to produce a report of all catalog entries.

Select Electronic Catalog Menu Option: ALL Electronic Catalog Print \<ENTER\>

DEVICE: \<ENTER\> UCX/TELNET Right Margin: 80//

Electronic Test Catalog JUL 22,2004 13:48 PAGE 1

---------------------------------------------------------------------------

AMIKACIN

NUMERIC TYPE A NUMBER BETWEEN 0 AND 999

Collection Tube: BLOOD/SMT MARBLED TOP

MIN VOL (in mls.): 3

MAIL OUT

Collection Tube: BLOOD/SG GENERAL

MIN VOL (in mls.): 3

Site/Specimen: SERUM

HL7 Specimen:Serum

Reference Low: 1.0

Reference High: 6.0

Critical Low: .5

Critical High: 9

Units: ug/ml

NLT Order Code: 81098.0000 Amikacin

NLT Result Code: 81098.0000 Amikacin

Default Cost: Default Price:

Specimen: SERUM

Electronic Test Catalog JUL 22,2004 13:48 PAGE 2

-----------------------------------------------------------------------

Specimen Cost: Specimen Price:

Electronic Test Catalog JUL 22,2004 13:48 PAGE 3

-----------------------------------------------------------------------

CERULOPLASMIN

NUMERIC TYPE A NUMBER BETWEEN 0 AND 999

Collection Tube: BLOOD/SMT MARBLED TOP

MIN VOL (in mls.): 3

Site/Specimen: SERUM

HL7 Specimen:Serum

Reference Low: 18

Reference High: 45

Units: mg/dl

NLT Order Code: 82390.0000 Ceruloplasmin (Copper O)

NLT Result Code: 82390.0000 Ceruloplasmin (Copper O)

Default Cost: Default Price:

Specimen: SERUM

Specimen Cost: Specimen Price:

Lab Shipping Menu \[LA7S MAIN MENU\]

### INTENDED END USER: COLLECTION and HOST facility Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Lab Shipping Menu \[LA7S MAIN MENU\] contains two new options (i.e., Start a Shipping Manifest \[LA7S MANIFEST START\] and Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\]). This menu should be assigned to the LIM and all lab users who process send out tests to referral facilities or HOST facility users who process testing from a COLLECTING facility.

Select Lab Shipping Menu Option: ?\<Enter\>

SMB Build Shipping Manifest

SSM Start a Shipping Manifest (NEW)

SMS Close/Ship a Shipping Manifest

ART Add/Remove a Shipping Manifest Test

SMR Edit Required Test Information

SMI Edit Relevant Clinical Information (NEW)

SMC Cancel a Shipping Manifest

PSM Print Shipping Manifest

STA Order Status Report

RSM Retransmit Shipping Manifest

RLR Retransmit LEDI Lab Results

SMP Print LEDI Pending Orders

#### Build Shipping Manifest \[LA7S MANIFEST BUILD\] option

Example: This option builds specimens onto a shipping manifest.

Select Lab Shipping Menu Option: Build Shipping Manifest\<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB\<Enter\>

There's no open shipping manifest for MILWAUKEE HOST LAB

Do you want to start one? NO// YES \<Enter\>

Use default accession dates? YES//\<Enter\>

Exclude previously removed tests from building? YES// \<Enter\>

Using shipping manifest# 170-20040722-2

Searching accession area: CHEMISTRY

Searching accession area: MICROBIOLOGY

Searching accession area: TOXICOLOGY

There were 1 specimens added

Print Shipping Manifest? NO// \<Enter\>

#### Start a Shipping Manifest \[LA7S MANIFEST START\] option (NEW)

Example: This new option is used to create or start a shipping manifest without performing the building of the manifest. It can be used to start a manifest and manually add specific accessions when a regular manifest build would add accessions that are not intended. An example is when a test on a specific accession or group of accessions usually performed in house needs to be sent to an outside laboratory for analysis. Use in conjunction with Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option.

Select Lab Shipping Menu Option: ssm Start a Shipping Manifest\<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB\<Enter\>

There's no open shipping manifest for MILWAUKEE HOST LAB

Do you want to start one? NO// y\<Enter\> YES

Shipping manifest# 170-20040722-4 is available

Select Lab Shipping Menu Option: \<Enter\>

#### Close/Ship a Shipping Manifest

Example: Close marks a shipping manifest as closed and/or shipped.

Select Lab Shipping Menu Option: Close/Ship a Shipping Manifest\<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-2 MILWAUKEE HOST LAB Status: OPEN as of Jul 22, 2004@13:02

Select one of the following: \<Enter\>

1 Close manifest

2 Ship manifest

Select action to perform: 1// 1 Close manifest\<Enter\>

Print Shipping Manifest? NO//\<Enter\>

Select Lab Shipping Menu Option: Close/Ship a Shipping Manifest \<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-2 MILWAUKEE HOST LAB Status: CLOSED as of Jul 22, 2004@13:03

Do you want to ship this manifest? NO// YES\<Enter\>

Enter Manifest Shipping Date: NOW//\<Enter\> (JUL 22, 2004@13:03)

Electronic Transmission of Shipping Manifest queued as task# 204941

Print Shipping Manifest? NO// \<Enter\>

Select Lab Shipping Menu Option:

#### Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option 

Example: This option allows a test to be added or removed from an “Open” shipping manifest.

Select Lab Shipping Menu Option: Add/Remove a Shipping Manifest Test \<ENTER\>

Select Shipping Configuration: VA/DOD Testing (VA Remote)

Select Shipping Manifest: 170-20040510-2 VA/DOD Testing (VA Remote) Status: OPEN as of May 10, 2004@17:11 \<ENTER\>

Select one of the following:

1 Add test to manifest

2 Remove test from manifest

Select action to perform: 1// Add test to manifest\<ENTER\>

Select Accession or UID: CH 0722 1\<ENTER\>

CHEMISTRY (JUL 22, 2004) 1

Select TEST to Add: CHEM 7 CHEM 7\<ENTER\>

Select Accession or UID: \<ENTER\>

Print Shipping Manifest? NO//\<ENTER\>

Select Lab Shipping Menu Option: Add/Remove a Shipping Manifest Test \<ENTER\>

Select Shipping Configuration: VA/DOD Testing (VA Remote) \<ENTER\>

Select Shipping Manifest: 170-20040510-2 VA/DOD Testing (VA Remote) Status: OPEN as of May 10, 2004@17:11\<ENTER\>

Select one of the following:

1 Add test to manifest

2 Remove test from manifest

Select action to perform: 1// 2 Remove test from manifest \<ENTER\>

Select Accession or UID: CH 0722 1\<Enter\>

CHEMISTRY (JUL 22, 2004) 1

1 CHEM 7

Select test(s) to remove: (1-1): 1 \<Enter\>

Select Accession or UID: \<Enter\>

Print Shipping Manifest? NO// \<Enter\>

#### Edit Required Test Information \[LA7S MANIFEST TEST REQ INFO\] option

Example: This option allows a user to enter/edit information required to be sent with a lab test when it is shipped. Examples can be the total volume of urine collected for a timed urine test, weight of specimen collected, duration of specimen collection, patient height and weight.

Select Lab Shipping Menu Option: SMR Edit Required Test Information\<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB\<Enter\>

Select Shipping Manifest: 170-20040722-4 MILWAUKEE HOST LAB Status: OPEN as of Jul 22, 2004@13:10

Select Accession or UID: 0442040004 (CH 0722 4) \<Enter\>

PATIENT HEIGHT (in cm): 30\<Enter\>

PATIENT WEIGHT (in kg): 97\<Enter\>

Select Accession or UID: \<Enter\>

Print Shipping Manifest? NO// \<Enter\>

Select Lab Shipping Menu Option:

#### Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option (NEW)

Example: The new option allows a user to enter/edit relevant clinical information that should be sent with a test when it is shipped. The following screen capture examples include reporting the amount of inspired carbon dioxide for blood gasses, the point in the menstrual cycle for cervical pap tests, other conditions that influence test interpretations, peak and trough times for antibiotic, and therapeutic drug levels.

Select Lab Shipping Menu Option: SMI Edit Relevant Clinical Information \<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-3 MILWAUKEE HOST LAB Status: OPEN as of Jul 22, 2004@13:08

Select Accession or UID: 0442040003\<Enter\>

(CH 0722 3) 1 GLUCOSE

Select test(s) to edit clinical info: (1-1): 1 \<Enter\>

For test: GLUCOSE\<Enter\>

Relevant clinical information: Patient is diabetic

Select Lab Shipping Menu Option: \<Enter\>

#### Cancel a Shipping Manifest \[LA7S MANIFEST CANCEL\] option

Example: This option cancels an open shipping manifest. All tests are removed and made available for building on another shipping manifest

Select Lab Shipping Menu Option: Cancel a Shipping Manifest \<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-1 MILWAUKEE HOST LAB Status: CLOSED as of Jul 22, 2004@12:44

Do you want to cancel this manifest? NO// y YES \<Enter\>

#### Print Shipping Manifest \[LA7S MANIFEST PRINT\] option

Example: This option allows the user to print a shipping manifest list for lab specimens sent outside the facility to a reference lab.

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-4 MILWAUKEE HOST LAB Status: OPEN as of Jul 22, 2004@13:10

DEVICE: HOME// \<Enter\>QUEUE TO PRINT ON

DEVICE: HOME// \<Enter\>NULL DEV NULL DEVICE NULL DEV

Requested Start Time: NOW// (JUL 22, 2004@13:16:42)

Request queued - Task \#204947

Select Lab Shipping Menu Option: \<Enter\>

#### Order Status Report \[LA7S ORDER STATUS REPORT\] option 

This option allows the user to produce a report based on selected criteria.

> **NOTE:** This option is presently non-functional. Functionality will be restored in the next version of LEDI.

#### Retransmit Shipping Manifest \[LA7S MANIFEST RETRANSMIT\] option

Example: This option allows the users to retransmit a shipping manifest electronically to the HOST facility. Manifest needs to be in status of “SHIPPED” to be able to select and the shipping configuration associated with the manifest must be “ACTIVE”.

Select Lab Shipping Menu Option: Retransmit Shipping Manifest \<Enter\>

Select Shipping Configuration: MILWAUKEE HOST LAB \<Enter\>

Select Shipping Manifest: 170-20040722-2 MILWAUKEE HOST LAB Status: SHIPPED as of Jul 22, 2004@13:03

Sure you want to retransmit this manifest? NO// YES \<Enter\>

Electronic Transmission of Shipping Manifest queued as task# 204948

Select Lab Shipping Menu Option: \<Enter\>

#### Retransmit LEDI Lab Results \[LA7S RESULTS RETRANSMIT\] option

### INTENDED END USER: HOST facility Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: This option allows a user at a HOST facility to select one or more accessions that were received from other LEDI COLLECTING facilities and retransmit results associated with the accession(s) to the sending/COLLECTING facility via HL7 messaging.

Select Lab Shipping Menu Option: RLR Retransmit LEDI Lab Results \<Enter\>

Select one of the following: \<Enter\>

1 Range of Accessions

2 Selected Accessions

Selection Method: 1// 2 Selected Accessions\<Enter\>

Select Accession or UID: HE 0130 6\<Enter\>

HEMATOLOGY (JAN 30, 2004) 6

Select Accession or UID: \<Enter\>

Found 1 accessions that can be retransmitted.

Ready to retransmit? NO// YES\<Enter\>

Working...Done

1 accession scheduled for retransmitting of results!

Task# 204951 queued for processing

Select Lab Shipping Menu Option: \<Enter\>

#### ### Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\] option

### INTENDED END USER: HOST facility Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: This option is used to print a COLLECTING facility’s LEDI shipping manifest from the HOST facility’s LAB PENDING ORDER ENTRY file (#69.6). This option could be used to reprint a shipping manifest lost or damaged during shipment. The user is prompted for the shipping manifest number. The option will then print a bar-coded-shipping manifest containing all of the patients on that manifest. The format is similar to the regular shipping manifest received from the COLLECTING (shipping) facility.

Select Lab Shipping Menu Option: SMP Print LEDI Pending Orders \<Enter\>

Select Shipping Manifest: ASALT,TDIYHN C\<Enter\>

Pat ID: 101160248 DOB: Jan 21, 1922 Sex: MALE\<Enter\>

Spec ID: 6104000011 Manifest: 695-20040330-1 Site: MILWAUKEE VAMC

DEVICE: HOME// UCX/TELNET Right Margin: 80//\<Enter\>

\*\*\* DO NOT USE FOR SHIPPING DOCUMENT - WORK COPY ONLY \*\*\*

Shipping Manifest: 695-20040330-1 Page: 1

to Site: REGION 7 ISC,TX (DEMO) Printed: Jul 22, 2004@14:14

from Site: MILWAUKEE VAMC

Status: Electronic Manifest Ship via: Electronic manifest

Shipping Condition: None Specified Container: None Specified

Patient Name Patient ID Accession

Date of Birth Sex Specimen UID

Requested By Collect Date/Time

-----------------------------------------------------------------------

Item: 1 ASALT,TDIYHN C 101160248 SEND 04 11

Jan 21, 1922 Male 6104000011

CPRS,PHYSICIAN Mar 30, 2004@14:47

-------------------------------

TEST-TEST SERUM

VA NLT code \[Name\]: 87283.0000 \[Misc Flow Test 1\]

### Information-help menu \[LRHELP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains the Lab information help menu options

### INTENDED END USER: Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Information-help menu \[LRHELP\] contains the new General Lab User Parameters \[LR USER PARAM\] option.

Select Information-help menu (LRHELP): ?\<Enter\>

PP General Lab User Parameters (NEW)

General report for selected tests

Inquiry to LAB TEST file

Interim report for selected tests as ordered

Order/test status

Review by order number

Test description information

### General Lab User Parameters \[LRUSER PARAM\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: This new General Lab User Parameters \[LRUSER PARAM\] option allows a user to modify various user selectable parameters used with the laboratory package. This new option is located on the Information-help menu \[LRHELP\].

Select Laboratory DHCP Menu Option: 6\<Enter\> Information-help menu

Select Information-help menu Option: gen\<Enter\>

1 General Lab User Parameters

2 General report for selected tests

CHOOSE 1-2: 1\<Enter\> General Lab User Parameters

Lab User Level Parameters for User: LAB USER, TECH  
-----------------------------------------------------------------------

Display previous comments for test  
-----------------------------------------------------------------------

For Display previous comments for test -  
Select Laboratory Test: CBC

1 CBC

2 CBC. LRL CBC  
CHOOSE 1-2: 1CBC  
Are you adding CBC as a new Laboratory Test? Yes// YES

Laboratory Test: CBC// \<Enter\> CBC CBC  
Display previous result's comments: ?\<Enter\>

Answer with yes/no to display previous result's comments during  
verification.

 

Display previous result's comments: YES

 

For Display previous comments for test

Select Laboratory Test: \<Enter\>

### General report for selected tests \[LRGEN\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option function displays data in a highly generalized fashion. All tests requested are displayed (up to 18 fields) in a cumulative format. If more than 18 tests are to be displayed, an alternate format is used. If a test has a special format (predefined in the 'LABORATORY TEST' file (#60)) then that test must be requested separately. If a specimen is specified, normal ranges are displayed if available.

> **NOTE:** IF a specimen is chosen for which there is no data, no data will be displayed.

Example:

Select Information-help menu Option: GENERAL REport for selected tests \<Enter\>

GENERAL LAB DATA DISPLAY

Select Patient Name: LSpatient,one MALE 01/01/1950 000112222 \<Enter\>

Select LABORATORY TEST NAME: MAGNESIUM MG\<Enter\>

Select LABORATORY TEST NAME: \<Enter\>

Specify specimen actually tested. Use BLOOD when Whole blood is tested;

use SERUM when Serum is tested; etc. In doubt press the Return key.

Select SITE/SPECIMEN: ANY//\<Enter\>

Date to START with: TODAY//\<Enter\> (OCT 15, 2004)

Date to END with: T-14//T (OCT 15, 2004) \<Enter\>

DEVICE: HOME//\<Enter\> UCX/TELNET Right Margin: 80//

WORK COPY: LSpatient,one 000-11-2222 Age:54 Prt Date:10/15/2004@18:31

Report Range \[ 10/15/2004 - 10/15/2004 \] Pg:1

SPEC MG

==============================================================================

10/15/2004@17:59

SER 2.9 H

10/15/2004@17:55

SER 1.4 L

10/15/2004@17:50

SER 1.4 H

------------------------------------------------------------------------------

WORK COPY - DO NOT FILE LSpatient,one 000-11-2222

#### Inquiry to LAB TEST file \[LRTESTDIQ\] option

This option function displays information from the LABORATORY TEST file (#60). All defined fields that are associated with the requested test in File 60 are displayed. If information is missing on a particular test, the desired information must be first added to File 60. This option is just a "lookup" option to allow the user to inquire about how a test is defined in the "LABORATORY TEST file (#60)."

Example:

Select Information-help menu Option: Inquiry to LAB TEST file \<Enter\>

Select LABORATORY TEST NAME: MAGNESIUM MG\<Enter\>

DEVICE: 0;80;99999 UCX/TELNET\<Enter\>

LABORATORY TEST LIST OCT 15,2004 18:25 PAGE 1

-----------------------------------------------------------------------------

NAME: MAGNESIUM TYPE: BOTH

SUBSCRIPT: CHEM, HEM, TOX, SER, RIA, ETC.

LOCATION (DATA NAME): CH;29;1 UNIQUE ACCESSION \#: YES

LAB COLLECTION SAMPLE: BLOOD/SMT TEST COST: 5.00

FIELD: DD(63.04,29, HIGHEST URGENCY ALLOWED: ASAP

REQUIRED COMMENT: ORDER COMMENT MODIFIED

PRINT NAME: MG PRINT ORDER: 18.2

DATA NAME: MAGNESIUM

SITE/SPECIMEN: SERUM REFERENCE LOW: 2

REFERENCE HIGH: 2.6 UNITS: mg/dL

DEFAULT VALUE: 1.4 USE FOR REFERENCE TESTING: YES

SITE/SPECIMEN: PLASMA REFERENCE LOW: .7

REFERENCE HIGH: 1.4 CRITICAL LOW: 3

CRITICAL HIGH: .5 UNITS: IU/L

DEFAULT VALUE: .9

COLLECTION SAMPLE: BLOOD/SMT MIN VOL (in mls.): 5

WARD REMARKS: THIS IS IN THE FIELD WARD REMARKS UNDER THE COLLECTION

MULTIPLE. THIS IS JUST A TEST...

LAB PROCESSING INSTRUCTIONS: LAB PROCESSING INSTRUCTIONS....THIS IS JUST A TEST

SYNONYM: MG

GENERAL WARD INSTRUCTIONS: This is in the General Ward Instructions field in

File 60....

INSTITUTION: REGION 7 ISC,TX (DEMO) ACCESSION AREA: CHEMISTRY

NATIONAL VA LAB CODE: Magnesium RESULT NLT CODE: Magnesium

Select LABORATORY TEST NAME: \<Enter\>

### Interim report for selected tests as ordered \[LRRSP\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed report format for an individual patient. Report is done for selected tests as they are ordered. If the orders have been purged, the results will not be found because the result look-up is dependent on the orders. This option allows the user to select a specific test or panel, or select the "ANY" test default which will output all the verified tests for that patient during the time period specified. If no results are available, the option will ask for another patient. This option will only print verified results and should be used for information only. The option should not be charted. The report prints site codes for tests. You will be asked if you would like to print an address page. The address page prints on a separate page(s) at the end of the report and lists the performing lab name, address and site code.

Example: Interim report for selected tests as ordered \[LRRSP\] option

Select Information-help menu Option: Interim reportfor selected tests as ordered \<Enter\>

Select Patient Name: LSpatient,oneMALE 01/01/1950 000112222\<Enter\>

Select ORDERED TEST: ANY//MAGNESIUM MG\<Enter\>

Date to START with: TODAY// \<Enter\> (OCT 15, 2004)

Date to END with: T-7//T\<Enter\> (OCT 15, 2004)

Print address page? NO// \<Enter\>YES

DEVICE: HOME// \<Enter\>0;80;60 UCX/TELNET

Printed at: page 1

Dallas Office of Information Field Office (170)

2301 East Lamar Blvd. Arlington, TX 76006

LSpatient,one Report date: Oct 15, 2004@18:29

SSN: 000-11-2222 SEX: M DOB: Jan 01, 1950 LOC: DODOP

Provider: LSprovider,one

Specimen: SERUM

Accession \[UID\]: CH 1015 6 \[0442890006\]

Specimen Collection Date: Oct 15, 2004@17:50

Test name Result units Ref. range Site Code

MAGNESIUM 1.4 H MD/DL .5 - 1.2 \[8739\]

=============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

Provider: LSprovider,one

Specimen: SERUM

Accession \[UID\]: CH 1015 7 \[0442890007\]

Specimen Collection Date: Oct 15, 2004@17:55

Test name Result units Ref. range Site Code

MAGNESIUM 1.4 L mg/dL 2 - 2.6 \[8739\]

=============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

Provider: LSprovider,one

Specimen: SERUM

Example: Interim report for selected tests as ordered \[LRRSP\] option *continued*

Accession \[UID\]: CH 1015 8 \[0442890008\]

Specimen Collection Date: Oct 15, 2004@17:59

Test name Result units Ref. range Site Code

MAGNESIUM 2.9 H mg/dL 2 - 2.6 \[8739\]

=============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LSpatient,one 000-11-2222 Oct 15, 2004 6:29 pm

page 2

LSpatient,one 000-11-2222 10/15/2004 6:29 pm

PERFORMING LAB SITES

\[8739\] WILFORD HALL USAF MEDICAL CENTER 59 MDW LACKLAND AFB, TX 78236-5300

### Order/test status \[LROS\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After selecting a patient, for each day prompted, the statuses for all tests for that day are given. The report will output for a specified patient, Order \#, Urgency, Status (i.e., test complete, on collection list, collected), Provider, and Accession \#.

Example: Inquiry to LAB TEST file

Select Information-help menu Option: Inquiry to LAB TEST file \<ENTER\>

Select LABORATORY TEST NAME: \<ENTER\>

Select Information-help menu Option: ORDer/test status \<ENTER\>

Select Patient Name: LSpatient,one MALE 01/01/1950 00011

2222

DATE to begin review: TODAY// \<ENTER\> (OCT 15, 2004)

Test Urgency Status Accession

-Lab Order \# 1109 Provider: REF:7054

BLOOD/SMT SERUM

CHEM 7 ROUTINE Collected 10/15/2004@17:24 CH 1015 5

: ~For Test: CHEM 7

: ~Testing LEDI

-Lab Order \# 1110 Provider: LRProvider,One

SERUM

MAGNESIUM ROUTINE Test Complete 10/15/2004@17:53 CH 1015 6

-Lab Order \# 1111 Provider: LRProvider,One

SERUM

MAGNESIUM ROUTINE Test Complete 10/15/2004@17:59 CH 1015 7

-Lab Order \# 1112 Provider: LRProvider,One

SERUM

MAGNESIUM ROUTINE Test Complete 10/15/2004@17:59 CH 1015 8

No orders for 10/14/2004

No orders for 10/13/2004

No orders for 10/12/2004

No orders for 10/11/2004

No orders for 10/10/2004

No orders for 10/09/2004

Select Patient Name:\<ENTER\>

### Review by order number \[LRCENLKUP\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the order number is known, essential information related to the order can be displayed with this function.

Example: How to REVIEW by order number

Select Information-help menu Option: REVIEW by order number \<ENTER\>

Order Number or UID: 1109 \<ENTER\>

ORDER \#: 1109 PAT: LSpatient,one SSN: 000-11-2222

-----------------------------------------------------------------------------

Oct 15, 2004

WHO ENTERED: LRUser, One TYPE OF COLLECTION: R

COLLECTION STATUS: C

DRAW TIME: 10/15/2004@17:24

LAB ARRIVAL: 10/15/2004@17:24

SPECIMEN: BLOOD/SMT

TEST: CHEM 7 ROUTINE CHEMISTRY 5 \<0442890005\>

~For Test: CHEM 7

~Testing LEDI

Order has already been accessioned.

Order Number or UID: \<ENTER\>

### Test description information \[LREV\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function displays limited information from the LABORATORY TEST file (#60), such as special ordering information, normal ranges, etc.

Example: How to display TEST description information

Select Information-help menu Option: TEST description information \<ENTER\>

Select LABORATORY TEST NAME: MAGNESIUM MG\<ENTER\>

Lab test Highest allowed urgency Cost

MAGNESIUM ASAP 5.00

Synonym: \<ENTER\>

MG

Reference Values Ref Low Ref High Critical Low Critical High

\<--- ---\>

SERUM 2 2.6 mg/dL

PLASMA .7 1.4 3 .5 IU/L

General Ward Instructions:

This is in the General Ward Instructions field in File 60....

Collection Sample VA Lab Slip Container Vol Req(ml)

BLOOD/SMT MARBLED TOP 5

Ward Instructions:

THIS IS IN THE FIELD WARD REMARKS UNDER THE COLLECTION MULTIPLE.

THIS IS JUST A TEST...

Select LABORATORY TEST NAME: \<ENTER\>

### Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### INTENDED END USER LAB INFORMATION MANAGER/IT SUPPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a stand-alone option that should be scheduled to run daily via TaskMan as a scheduled task. This task option is used to check the integrity of the LA7 MESSAGE QUEUE file (#62.49), and to purge messages that are eligible for purging. It also purges the following files related to LEDI:

LAB SHIPPING MANIFEST (#62.8)

LAB SHIPPING EVENT (#62.85)

LAB PENDING ORDERS ENTRY (#69.6)

This option should be tasked daily, preferably during a period when activity in the Lab Messaging (that is, Universal Interface, LEDI) package is at a minimum. Before the purge of LA7 MESSAGE QUEUE file (#62.49), an integrity check is performed. The integrity check can be run with a couple of switches.

LA7FIX = 0 - do not fix errors

1 - do fix errors

LA7LOG = 0 - do not log errors in XTMP global.

1 - do log errors in XTMP global

LA7ION = name of device to print error report if set to log errors (LA7LOG=1)

These parameters can be setup by TaskMan if the site defines them when scheduling the task.

Example: Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] Option

Edit Option Schedule Option Name: LA7TASK NIGHTY

VARIABLE NAME: LA7FIX VALUE: 0

VARIABLE NAME: LA7ION VALUE: "IRM DEVELOP LASER1"

VARIABLE NAME: LA7LOG VALUE: 1

If errors are found, an alert is sent to members of the mail group “LAB MESSAGING” notifying them that errors were detected. If logging of errors occurred then alert recipients will be able to print or view error log from the alert system. Alternatively the error report can be printed using the Print Lab Messaging Integrity Check Report \[LA7 PRINT INTEGRITY CHECK\] option. The integrity report can be run alone using Lab Messaging File Integrity Checker \[LA7 CHECK FILES\] option.

### Lab Interface Menu \[LA INTERFACE\]Example: This menu contains the Laboratory auto instrument options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Supervisor menu Option: LAB INTERface menu

-----------------------------------------------------------------------------

LSI INTERFACE STATUS

-----------------------------------------------------------------------------

LSI INST. DATA DATA ++ PROGRAM STATUS ++

PORT \# NAME IN LA? IN LAH? NAME ACTIVE \$J

-----------------------------------------------------------------------------

Change instrument run mode.

Check the lab interface

Direct Connect Auto-Instrument Start

Lab Error Trap Listing

Lab Universal Interface Menu...

Restart processing of instrument data

Set instrument to run by Accession

Set instrument to run by load list

Watch the data in the LA global.

#### Lab Universal Interface Menu \[LA7 MAIN MENU\]

Lab Universal Interface Menu \[LA7 MAIN MENU\] is a submenu located on the Lab interface Menu \[LA INTERFACE\]. This submenu contains options used by LEDI III software to setup and manage the lab universal interface functionality. The Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] option has been modified to accommodate the new LEDI III functionality.

### INTENDED END USER: Laboratory Information Manager (LIM)/It Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Lab Universal Interface Menu \[LA7 MAIN MENU\] options

Lab Universal Interface Menu (LA7 MAIN MENU)

1 Print Source of Specimen Table \[LA7 PRINT 0070 TABLE\]

2 Print Lab Universal Interface Log \[LA7 PRINT LAB UI ERROR LOG\]

Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\]

Download to Universal Interface \[LA7 ADL SEND\]

Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\]

FIC Lab Messaging File Integrity Checker \[LA7 CHECK FILES\]

PIC Print Lab Messaging Integrity Check Report \[LA7 PRINTINTEGRITY CHECK\]

#### Print Source of Specimen Table \[LA7 PRINT 0070 TABLE\] option

Example: Enter the two to four character codes from the left column:

ABS Abscess

AMN Amniotic fluid

ASP Aspirate

BPH Basophils

ABLD Blood arterial

BBL Blood bag

BON Bone

BRTH Breath

BRO Bronchial

BRN Burn

CALC Calculus

CDM Cardiac muscle

CNL Cannula

CTP Catheter tip

CSF Cerebral spinal fluid

CVM Cervical mucus

CVX Cervix

COL Colostrum

CBLD Cord blood

CNJT Conjunctiva

CUR Curettageputum

CYST Cyst

DRN Drain

EAR Ear

ELT Electrode

ENDC Endocardium

ENDM Endometrium

EOS Eosinophils

RBC Erythrocytes

FIB Fibrolasts

FLT Filter

FIST Fistula

FLU Body fluid, unsp

GAST Gastric fluid

GEN Genital

GENC Genital, cervix

GENL Genital lochia

GENV Genital vaginal

HAR Hair

IT Intubation tube

LAM Lamella

WBC Leucocytes

LN Line

LNA Line arterial

LNV Line venous

LYM Lymphocytes

MAC Macrophages

MAR Marrow

MEC Meconium

MBLD Menstrual blood

MLK Milk

MILK Breast Milk

NAIL Nail

Example: Print Source of Specimen Table \[LA7 PRINT 0070 TABLE\] option *continued*

NOS Nose (nasal passage)

ORH Other

PRT Peritoneal fluid ascites

PER Peritoneum

PLC Placenta

PLAS Plasma

PLB Plasma bag

PLR Pleural fluid (thoracentesis fld)

PMN Polymorphonuclear neutrophils

PUS Pus

SAL Saliva

SEM Seminal fluid

SER Serum

SKN Skin

SKM Skeletal muscle

SPRM Spermatozoa

SPT Sputum

SPTC Sputum coughed

SPTT Sputum tracheal aspirate

STON Stone

STL Stool = Fecal

SWT Sweat

SNV Synovial fluid = Joint fluid

TEAR Tears

THRT Throat

THRB Thrombocyte (platelet)

TISS Tissue

TISB Tissue bone marrow

TISG Tissue gall bladder

TISL Tissue lung

TISP Tissue peritoneum

TISU Tissue ulcer

TISC Tissue curettage

TISPL Tissue placenta

ULC Ulcer

UMB Umbilical blood

UR Urine

URTH Urethra

URC Urine clean catch

URT Urine catheter

VOM Vomitus

BLD Whole blood

BDY Whole body

WICK Wick

WND Wound

WNDA Wound abscess

WNDE Wound exudate

WNDD Wound drainage

#### Print Lab Universal Interface Log \[LA7 PRINT LAB UI ERROR LOG\] option

This option should be used to print errors and events logged using the Lab Universal Interface system.

Example: How to Print Lab Universal Interface Log

Select Lab Universal Interface Menu Option: ?\<Enter\>

1 Print Source of Specimen Table

2 Print Lab Universal Interface Log

Display Lab Universal Interface Message

Download to Universal Interface

Start/Stop Auto Download Background Job

FIC Lab Messaging File Integrity Checker

PIC Print Lab Messaging Integrity Check Report

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Lab Universal Interface Menu Option: 2 Print Lab Universal Interface Log\<Enter\>

Look at log for what date? TODAY// T-4 (SEP 10, 2004) \<Enter\>

Select CONFIGURATION: LA7V HOST DOD\<Enter\>

Print message text with error? YES//\<Enter\>

DEVICE: HOME//\<Enter\> UCX/TELNET

#### Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] option

This option allows user to select a range of messages, up to 20, for printing or displaying on a terminal. When displaying on terminal that supports screen handling, the Kernel Browser is used to display the message(s). This option has been modified to no longer prompt the user if an alert should be saved when called via the Kernel Alert system. This functionality is now part of Kernel Alert processing.

Example: Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] option

Select Lab Universal Interface Menu Option: Display Lab Universal Interface Message

Select Message: 6007 LA7V HOST 695-I-2441820001

Select another Message:

Parse message fields based on HL7 segments? NO//

DEVICE: HOME//

\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Message Statistics \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\]

CONFIGURATION: LA7V HOST 695 DATE/TIME ENTERED: JUL 20, 2004@18:40:

DATE/TIME OF MESSAGE: JUL 20, 2004@17:40:38

INSTRUMENT NAME: LA7V HOST 695-I-2441820001

MESSAGE CONTROL ID: 69520035677 MESSAGE NUMBER: 6007

MESSAGE TYPE: ORU PRIORITY: 3

PROCESSING ID: TRAINING RECEIVING APPLICATION: LA7V REMOTE 170

RECEIVING FACILITY: 170 SENDING APPLICATION: LA7V HOST 695

SENDING FACILITY: 695 STATUS: ERROR

TYPE: INCOMING VERSION ID: 2.3

\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Error Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\]

Date: Jul 20, 2004@18:40:47

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

Date: Jul 20, 2004@18:43:50

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

Date: Jul 21, 2004@09:20:56

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

Date: Jul 21, 2004@09:28:47

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

Date: Jul 21, 2004@09:36:55

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

  
Example: Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] option *continued*

Date: Jul 21, 2004@09:39:38

Text: Msg \# 6007, Test code '10466-1' was returned with a result but is not entered

\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Text of Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\]

MSH^~\|\\^LA7V HOST 695^695^LA7V REMOTE 170^170^20040720174038-0500^^ORU~R01^69520035677^T^2.3^^^AL^AL^

PID^1^287080747~6~M11\~~SS\|6564641~2~M11\~~PI~170&FS.ISC-XXXXX.XXX.XX.XXX&DNS\|1700000150V554301\~\~~USVHA&&HL70363~NI~VA FACILITY ID&170&L^287080747~6~M11^223849~7~M11^LSpatient~one~^^19500807^F^^2106-3~WHITE~HL70005^

PV1^1^O^^

ORC^RE^2441820001^2441820001^170-20040630-1^^^^^^^^~REF:7934~^^^^^170~Dallas Office of Information Field Office~99VA4^

OBR^1^2441820001^2441820001^81357.0000~Electrolytes~99VA64^^^20040630083623-0500^^^^A^~^^20040630083623-0500^SER&Serum&HL70070&SER&Serum&LN^

~REF:7934~^^LA7V HOST695^\F\\F\\F\\F\\F\\F\2441820001^223849\F\CH\F\\

6959368.916377^^20040720174031-0500^^CH^

NTE^1^L^GLUCOSE-------------O reported incorrectly as 156 by \[235-VA695\].^

NTE^2^L^Changed to 155 on Jul 20, 2004@17:33 by \[235-VA695\].^

NTE^3^L^GLUCOSE-------------O reported incorrectly as 155 by \[235-VA695\].^

NTE^4^L^Changed to 154 on Jul 20, 2004@17:40 by \[235-VA695\].^

NTE^5^L^SODIUM--------------O reported incorrectly as 133 by \[235-VA695\].^

NTE^6^L^Changed to 134 on Jul 20, 2004@17:40 by \[235-VA695\].^

OBX^1^ST^84016.0000~Fractional Extraction NA~99VA64~CH5~SODIUM~99VA63^^

134^mmol/L^136-145^L^^^C^^^20040630083623-0500^695~ LRPatient~ONE~99VA4^235-VA695~LSUser~ONE1^.3118~PRECISION G~99VA64_2^

OBX^2^NM^2823-3~POTASSIUM:SCNC:PT:SER/PLAS:QN~LN~84140.0000~Potassium~

99VA64~CH6~ POTASSIUM~99VA63^^3.1^mmol/L^3.5-5.1^L^^^F^^^20040

-00083623-0500^695~ LRUser~ONE~99VA4^235-VA695~LRUser~One^.3118~PRECISION G~99VA64_2^

Example: Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] option *continued*

OBX^3^ST^2075-0~CHLORIDE:SCNC:PT:SER/PLAS:QN~LN~82435.0000~Chloride~99VA64~

CH7~CHLORIDE~99VA63^^80^mmol/L^98-107^L^^^F^^^2004063008

3623-0500^695~ LRPatient~ONE ~99VA4^235-VA695~LRUSER~ONE^.3118~PRECISION G~99VA64_2^

OBX^4^NM^2028-9~CARBON DIOXIDE:SCNC:PT:SER/PLAS:QN~LN~81216.0000~Bicarbonate~99V

A64~CH454~BICARBONATE~99VA63^^10^mmol/L^22-29^L^^^F

^^^20040630083623-0500^695~ LRPatient~ONE~99VA4^235-VA695~LSUSER~ONE^.3118~PRECISION G~99VA64_2^

OBX^5^ST^10466-1~ANION GAP 3:SCNC:PT:SER/PLAS:QN~LN~81213.0000~Anion Gap~99VA64~

CH695816~ANION GAP\*~99VA63^^^mmol/L^10-20^^^^I^^^20

040630083623-0500^695~ LRPatient~ONE~99VA4^235-VA695~LSUSER~ONE^.3118~PRECISION G~99VA64_2^

ORC^RE^2441820001^2441820001^170-20040630-1^^^^^^^^~REF:7934~^^^^^170~Dallas Office of Information Field Office~99VA4^

OBR^2^2441820001^2441820001^84330.0000~Glucose Quant~99VA64^^^20040630083623-0500^^^^A^~^^20040630083623-0500^SER&Serum&HL70070&SER

&Serum&LN^~REF:7934~^^LA7V HOST 695^\F\\F\\F\\F\\F\\F\2441820001^223849\F\CH

\F\6959368.916377^^20040720174031-0500^^CH^

NTE^1^L^GLUCOSE-------------O reported incorrectly as 156 by \[235-VA695\]^

NTE^2^L^Changed to 155 on Jul 20, 2004@17:33 by \[235-VA695\]^

NTE^3^L^GLUCOSE-------------O reported incorrectly as 155 by \[235-VA695\]^

NTE^4^L^Changed to 154 on Jul 20, 2004@17:40 by \[235-VA695\]^

NTE^5^L^SODIUM--------------O reported incorrectly as 133 by \[235-VA695\]^

NTE^6^L^Changed to 134 on Jul 20, 2009@17:40 by \[235-VA695\].^

OBX^1^NM^2345-7~GLUCOSE:MCNC: PT:SER/PLAS:QN~LN~84330.0000~Glucose Quant~99VA64~C

H2~GLUCOSE~99VA63^^154^MG/DL^70-110^H^^^C^^^2004063

0083623-0500^695~ LRPatient~ONE~99VA4^235-VA695~LRUSER~ONE^.3118~PRECISION G~99VA64_2^

Col\> 1 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 87 of 87 Screen\> 4 of 4

#### Download to Universal Interface \[LA7 ADL SEND\] option

Example: This option should be used to schedule for downloading an accession or group of accessions by the Lab Universal Interface. It will create messages containing orders for those instrument designated for auto downloading. This option can be used in those situations where accessions need to be re-downloaded because of changes to the auto instrument file setup, recovery from a system interruption or switch to an alternate/backup system.

Select Lab Universal Interface Menu Option: DOWNLoad to Universal Interface \<ENTER\>

Select one of the following:

1 Range of Accessions

2 Selected Accessions

Selection Method: 1// 2 Selected Accessions \<Enter\>

Select Accession or UID: (CH 0722 4) \<Enter\>

Select Accession or UID: \<Enter\>

Found 1 accessions that can be downloaded.

Ready to download? NO// YES \<Enter\>

.

Done - 1 accession scheduled for downloading!

Select Lab Universal Interface Menu Option: \<Enter\>

#### Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] option:

Example: This option allows user to start/restart/stop the lab messaging package’s auto download background job. This option can be used to restart the auto download job after changes have been made to the auto instrument file and the auto download job needs to be updated to reflect the changes. It can also be used to temporarily suspend auto downloading while making changes. It will then keep a list of accessions to process and use this list when auto downloading is resumed.

Select Lab Universal Interface Menu Option: START/Stop Auto Download Background Job \<Enter\>

Select one of the following: \<Enter\>

1 Start/Restart Auto Download Job

2 Shutdown Auto Download Job

3 Shutdown Auto Download Job and Stop Collecting Accessions

Current Status is: Running

at: Jul 22, 2004@14:10:03

by: MCCORMACK,JOHN J

There are NO accessions waiting checking

Select action: 1 Start/Restart Auto Download Job\<Enter\>

Auto Download flag set to Start/Restart Auto Download Job

Auto Download - Queued to run as task \#204957

Select Lab Universal Interface Menu Option: \<Enter\>

#### Lab Messaging File Integrity Checker \[LA7 CHECK FILES\] option

This option performs the following checks:

- Integrity of LA7 MESSAGE QUEUE file (#62.49).
- Entries having proper cross-references and cross-references pointing to the correct entry.
- Checks for bad entries.
- Fixes bad entries.
- Provides a printed report of errors found.

Example: Lab Messaging File Integrity Checker option

Select Lab Universal Interface Menu Option: FIC Lab Messaging File Integrity Checker \<Enter\>

Select one of the following: \<Enter\>

1 Check File Integrity

2 Fix File Entries

Select Option: 1// 2 Fix File Entries\<Enter\>

Print Report? YES//\<Enter\>

Select Device: NULL Bit Bucket\<Enter\>

Requested Start Time: NOW// \<Enter\> (JUL 22, 2004@14:10:39)

Request Queued

Select Lab Universal Interface Menu Option: \<Enter\>

#### Print Lab Messaging Integrity Check Report \[LA7 PRINT INTEGRITY CHECK\] option

#### Example: This option is used to prints the Lab Messaging Integrity Check Report.

Select Lab Universal Interface Menu Option: PIC Print Lab Messaging File Integrity Checker\<Enter\>

Select one of the following: \<Enter\>

1 Check File Integrity

2 Fix File Entries

Select Option: 1// 2 Fix File Entries \<Enter\>

Print Report? YES//\<Enter\>

Select Device: NULL Bit Bucket \<Enter\>

Requested Start Time: NOW// \<Enter\> (JUL 22, 2004@14:10:39)

Request Queued

Select Lab Universal Interface Menu Option: \<Enter\>

#### #### ### Accessioning menu \[LR IN\] 

This menu is used to order laboratory tests.

Example: The Accessioning menu \[LR IN\] is located on the Laboratory DHCP menu \[LRMENU\].

Select Laboratory DHCP Menu Option: Accessioning menu \<ENTER\>

Select Accessioning menu Option: ? \<ENTER\>

Accessioning tests ordered by ward order entry

Accessioning, standard (Microbiology)

Add tests to a given accession.

Bypass normal data entry

Delete entire order or individual tests

Delete test from an accession

Fast lab test order (IMMEDIATE COLLECT)

Fast lab test order (ROUTINE)

Fast lab test order (SEND PATIENT)

Inquiry to LAB TEST file

Lab add test(s) to an existing order

Lab orders by collection type

Lookup accession

Manual Enter Clinic Stop Codes

Manually accession QC, Environmental, etc.

Merge Accessions

Multipurpose accessioning

Order/test status

Print accession list(s) ...

Print future collection labels

Print single future collection label

Recollect Canceled Orders

Referral Patient Multi-purpose Accession

Remove an accession

Reprint accession label(s)

Reprint order accession label(s)

Review by order number

Show list of accessions for a patient

Special test accessioning

Test description information

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Accessioning menu Option: \<ENTER\>

#### Referral Patient Multi-purpose Accession \[LRLEDI\] option

This option is used to accession referral patients from another medical center. The patient must already exist in the PATIENT file (#2) to be selected. The option will accession the patient into the REFERRAL PATIENT file (#67) if it does not already exist. The user will be prompted for the Unique Identifier. The user will then be able to order tests for that patient.

The Referral Patient Multi-purpose Accession \[LRLEDI\] option prompts the user to respond to the question, “Are you using a bar-code reader?” The user may accept the default of “YES” or may type “NO” as a response.

When the default of “YES” (“are you using a bar-code reader?”) is accepted for the Shipping Configuration, the user may scan the bar coded Shipping Manifest list (initiated by the Collection facility laboratory). The bar coded Shipping Manifest list contains the patient’s demographics and specimens accessioning data. The Shipping Manifest data are stored in the LAB SHIPPING MANIFEST file (#62.8) at the collection facility or the LAB PENDING ORDERS ENTRY file (#62.9) at the host facility.

If the user does not user a bar code reader then the option to manually select orders from the LAB PENDING ORDERS ENTRY file (#62.9) is provided which requires the user to enter the shipping manifest and specimen id of the accession. If the user does not select manual lookup of pending orders or they are not available the user will be prompted to type in the patient’s demographics (i.e., name or social security number) before the specimens can be accessioned. This selection allows typographical mistakes and the possibility of duplicate entries.

Example: Referral Patient Multi-purpose Accession \[LRLEDI\] option

Select Accessioning menu Option: Referral Patient Multi-purpose Accession \<ENTER\>

Are you using a barcode reader? YES//\<ENTER\>Scan Remote Site Barcode (SM): stx^site^695^3041018.1308^695-20041018-3^etx101

Select ACCESSION TEST GROUP:    SPECIMEN RECEIVING\<ENTER\>

Scan Patient/Accession Barcode (PD): \<ENTER\>

stx^pd^000054065^695^7304000005^m^3041018.130644^etx101  
LAB Order number: 1116

You have just selected the following tests for LRPatient,One 000-00-0000  
     entry no. Test                          Sample  
     1            CAROTENE               SERUM  
Other tests? N//\<ENTER\>  
   
You have just selected the following tests for LRPatient,One 000-00-0000

     entry no. Test                          Sample  
     1            CAROTENE               SERUM  
   
All satisfactory? Yes//   (Yes)  
   
LAB Order number: 1116  
   
   
Print labels on: 244// HOME  UCX/TELNET  
   
~For Test: CAROTENE   SERUM  
Enter Order Comment: Testing LEDI bar code accessioning  (~Testing LEDI bar code accessioning)  
  OK? Yes// \<ENTER\> (Yes)  
   
   
ACCESSION:  SEND 1000 2  \<1841000002\>  
CAROTENE                      SERUM  
   
Scan Patient/Accession Barcode (PD): \<ENTER\>

     Barcode error \#1 - User timeout/abort

Select Accessioning menu Option: \<ENTER\>

#### Example 1: Referral Manual Accession

Select Accessioning menu Option:REF Referral Patient Multi-purpose Accession

\<Enter\>

Are you using a barcode reader? YES// NO\<Enter\>

Select Shipping Configuration: VA/DOD Testing (VA Host)

SHIPPING MANIFEST: 170-123456-1

No manifest '170-123456-1' found on file.

Use manifest '170-123456-1' anyway? NO// YES\<Enter\>

Select ACCESSION TEST GROUP: SPECIMEN RECEIVING\<Enter\>

Select Patient Name -'^M' To enter New Name : LRPatient,One\<Enter\>

Searching for a Patient file entry

Searching for a Referral Patient

Searching for a Patient file entry

Searching for a Referral Patient

Enter one of the following: \<ENTER\>

PAT.EntryName to select a Patient file entry

REF.EntryName to select a Referral Patient

To see the entries in any particular file type \<Prefix.?\>

Select Patient Name -'^M' To enter New Name : ^M\<ENTER\>

Manual Referral Patient Entry

Patient ID (SSN): 000000000\<Enter\>

Patient Name: LRPatient,One\<Enter\>

SEX: m MALE\<Enter\>

DOB: 1-1-1950 (JAN 01, 1950) \<Enter\>

Enter Remote UID: AB123445678\<Enter\>

LAB Order number: 1109\<Enter\>Example 1: Referral Manual Accession *continued*

'?' for list, TEST number(s): ? \<ENTER\>

Choose one (or more, separated by commas) ('\*' AFTER NUMBER TO CHANGE URGENCY)

1 CHEM 7 9 ELECTROLYTES

2 CBC & MORPHOLOGY (WITH DIFF) 10 MAGNESIUM

3 CBC 11 PO4

4 CBC & MORPHOLOGY (NO DIFF) 12 CELL COUNT (CSF)

5 ETHANOL 13 CELL COUNT (PLEURAL)

6 URINALYSIS 14 CELL COUNT (PERITONEAL)

7 COAGULATION (PT & PTT) 15 CELL COUNT (SYNOVIAL)

8 CHEM 20

TEST number(s): 1\<Enter\>

Other tests? N//\<Enter\>

You have just selected the following tests for LSpatient,one 000-11-2222

entry no. Test Sample

1 CHEM 7 BLOOD/SMT SERUM

All satisfactory? Yes// \<Enter\> (Yes)

LAB Order number: 1109

Collection Date@Time: NOW// \<Enter\> OCT 15, 2004@17:24:58

Print labels on: 244// HOME UCX/TELNET

~For Test: CHEM 7 BLOOD/SMT SERUM

Enter Order Comment: Testing LEDI (~Testing LEDI)

OK? Yes// \<Enter\> (Yes)

ACCESSION: CH 1015 5 \<0442890005\>

CHEM 7 BLOOD/SMT SERUM

Select Patient Name -'^M' To enter New Name : \<Enter\>

#### Example 2: Using a Bar Code Reader

Select Accessioning menu Option: Referral Patient Multi-purpose Accession \<Enter\>  
   
Are you using a barcode reader? YES//\<Enter\>  
Scan Remote Site Barcode (SM): stx^site^695^3041018.1308^695-20041018-3^etx101  
   
   
Select ACCESSION TEST GROUP:    SPECIMEN RECEIVING\<Enter\>  
   
Scan Patient/Accession Barcode (PD): \<Enter\> stx^pd^000054065^695^7304000005^m^3041018.130644^etx101  
LAB Order number: 1116  
   
You have just selected the following tests for LRPatient,One 000-00-0000  
     entry no. Test                          Sample  
     1            CAROTENE               SERUM  
Other tests? N//\<Enter\>  
   
You have just selected the following tests for LRPatient,One 000-00-0000

     entry no. Test                          Sample  
     1            CAROTENE               SERUM  
   
All satisfactory? Yes//\<Enter\> (Yes)  
   
LAB Order number: 1116\<Enter\>  
   
   
Print labels on: 244// \<Enter\>HOME  UCX/TELNET  
   
~For Test: CAROTENE   SERUM  
Enter Order Comment: Testing LEDI bar code accessioning  (~Testing LEDI bar code accessioning)  
  OK? Yes// \<Enter\>  (Yes)  
   
   
ACCESSION:  SEND 1000 2  \<1841000002\>  
CAROTENE                      SERUM  
   
Scan Patient/Accession Barcode (PD): \<Enter\>

     Barcode error \#1 - User timeout/abort  
   
Select Accessioning menu Option: \<Enter\>

#### Example 3: Using manual lookup of LAB PENDING ORDERS file (# 69.6)

Select Accessioning menu Option:REF\<Enter\> Referral Patient Multi-purpose Accession

Are you using a barcode reader? YES// NO \<ENTER\>

Select Shipping Configuration: VA/DOD Testing (VA Host) \<ENTER\>

SHIPPING MANIFEST: 170-N00183-213

Lookup orders using this manifest? YES//\<Enter\>

Select ACCESSION TEST GROUP: SPECIMEN RECEIVING

Enter UID of specimen: 040412 IMM 823 INTEROP,NEWONE DOD-SAIC 040412 IMM 823 170-N00183-213

LAB Order number: 962\<ENTER\>

Choose one (or more, separated by commas) ('\*' AFTER NUMBER TO CHANGE URGENCY)

1 CHEM 7 9 ELECTROLYTES

2 CBC & MORPHOLOGY (WITH DIFF) 10 MAGNESIUM

3 CBC 11 PO4

4 CBC & MORPHOLOGY (NO DIFF) 12 CELL COUNT (CSF)

5 ETHANOL 13 CELL COUNT (PLEURAL)

6 URINALYSIS 14 CELL COUNT (PERITONEAL)

7 COAGULATION (PT & PTT) 15 CELL COUNT (SYNOVIAL)

8 CHEM 20

You have just selected the following tests for INTEROP,NEWONE 803-66-0304

entry no. Test Sample

1 COMPLEMENT C3 BLOOD/SG SERUM

Other tests? N//\<ENTER\>

You have just selected the following tests for INTEROP,NEWONE 803-66-0304

entry no. Test Sample

1 COMPLEMENT C3 BLOOD/SG SERUM

All satisfactory? Yes// \<ENTER\> (Yes)

LAB Order number: 962\<ENTER\>

Print labels on: 244// NULL Bit Bucket \<ENTER\>

Do you wish to test the label printer: NO//\<Enter\>

~For Test: COMPLEMENT C3 BLOOD/SG SERUM

Enter Order Comment:

ACCESSION: SEROL 0423 1 \<2041140001\>

COMPLEMENT C3 BLOOD/SG SERUM

Enter UID of specimen: \<ENTER\>

#### Process data in lab menu \[LR DO!\]

### INTENDED USER: Laboratory Information Manager (LIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: This menu contains the Enter/verify data (auto instrument) \[LRVR\] and Enter/verify/modify data (manual) \[LRENTER\] options used for the verification of reference laboratory test results.

Select Process data in lab menu Option:

EA Enter/verify data (auto instrument)

EL Enter/verify data (Load list)

EM Enter/verify/modify data (manual)

EW Enter/verify data (Work list)

GA Group verify (EA, EL, EW)

MP Misc. Processing Menu ...

Accession order then immediately enter data

Batch data entry (chem, hem, tox, etc.)

Build a load/work list

Bypass normal data entry

Download a load list to an Instrument.

Fast Bypass Data Entry/Verify

Lookup accession

Order/test status

Print a load/work list

Std/QC/Reps Manual Workload count

Unload Load/Work List

#### Enter/verify data (auto instrument) \[LRVR\] option

Results verified using the Enter/verify data (auto instrument) \[LRVR\] option are based on the HL7 messages containing the test results that the VistA Laboratory package has received via an HL7 interface. When these results are processed by the COLLECTING facility the test results, units, normals and abnormality reported by the reference laboratory are accepted ‘as is’ by VistA. Users are not allowed to edit, modify, change or delete the reported results using this option. The performing host laboratory is recorded with the results in VistA. It is determined from the HL7 message if available or based on the performing laboratory the user selected when entering the option.

NOTE LIM: The default performing laboratory presented to the user when using this option can be configured using <u>Edit the default parameters Load/Work list \[LRLLE DFT\] option.</u>

If test results are received from the reference laboratory and are not in the editing profile or ordered on the accession then the user will be displayed these results and prompted for a disposition action.

Example: Enter/verify data (auto instrument) \[LRVR\] option

Select Process data in lab menu Option: Enter/verify data (auto instrument) \<ENTER\>

Select LOAD/WORK LIST NAME: CHEMISTRY\<ENTER\>

Select PROFILE: CHEMISTRY\<ENTER\> CHEMISTRY

Select Performing Laboratory: MILWAUKEE VAMC//\<ENTER\> WI VAMC 695

Work Load Area: CHEMISTRY//\<ENTER\>

Would you like to see the test list? No// \<ENTER\> NO

Do you wish to modify the test list? NO//\<ENTER\>

You have selected 49 tests to work with.

Do you want to review the data before and after you edit? YES//\<ENTER\>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// 2 Unique Identifier (UID) \<ENTER\>

Unique Identifier: 2442890001//\<ENTER\>

LRPatient,One 000-00-0000

ORDER \#: 1113

Seq \#: 3 Accession: TOX 1015 1 Results received: Oct 15, 2004@19:25

UID: 2442890001 Last updated: Oct 15, 2004@19:25

Sample: BLOOD/SMT

Specimen: SERUM

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRProvider,One Voice pager:

Phone: Digital pager:

ACCESSION: TOX 1015 1

CHEMISTRY 10/15 19:21d

PROCAINAMIDE 30.5 CRITICAL HIGH!!H\* ug/mL

SELECT ('C' for Comments, 'W' Workload):

Approve for release by entering your initials: JM

Test(s) Not Reviewed:

N-ACETYL = 14 ug/mL

Purge these test results? NO// \<ENTER\>

Unique Identifier: 0440700005// \<ENTER\>

#### Enter/verify/modify data (manual) \[LRENTER\] option

Results that are not received via a HL7 interface are entered using Enter/verify/modify data (manual) \[LRENTER\] option. The user selects the name of the performing laboratory to be stored with the results.

LIM NOTE: If the test is a referral test, the test entry in File 60 can be set up to accept the units, reference range, and critical values designated in the Site/Specimen through the use of the new field 13 “USE FOR REFERENCE TESTING” set to YES; or not to accept the values in the file 60 set up thereby enabling the tech to be prompted to enter the units and ranges of the referral lab at the time of verification by setting the field to NO or leaving it NULL. <u>Use Edit atomic tests \[LRDIEATOMIC\] option to configure this functionality.</u>

The Enter/verify/modify data (manual) \[LRENTER\] option has been enhanced to process amended reference laboratory results that have been transmitted via a LEDI interface – see example \#3.

  
Example \#1: File 60 test Site/Specimen “USE FOR REFERENCE TESTING field (#13)” set to YES:

Select Process data in lab menu Option: Enter/verify/modify data (manual) \<ENTER\>

Do you want to review the data before and after you edit? YES//\<ENTER\>

Do you wish to see all previously verified results? NO//\<ENTER\>

Select one of the following: \<ENTER\>

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// Accession Number\<ENTER\>

Select Accession: CH T 8 \<ENTER\>

CHEMISTRY (OCT 15, 2004) 8

Select Performing Laboratory: REGION 7 ISC,TX (DEMO)// \<ENTER\> WILFORD HALL MEDICAL CENTER TX USAF 671CZ

Work Load Area: CHEMISTRY

LRPatient,One 000-11-2222

Sample: SERUM

Specimen: SERUM

1 MAGNESIUM

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: DOG,HOUND Voice pager:

Phone: Digital pager:

ACCESSION: CH 1015 7 CH 1015 8

10/15 17:55d 10/15 17:59d

Current Ref Range: 2-2.6 Units: mg/dL

MAGNESIUM //2.9

Select COMMENT: \<ENTER\>

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRProvider,One Voice pager:

Phone: Digital pager:

ACCESSION: CH 1015 7 CH 1015 8

10/15 17:55d 10/15 17:59d

MAGNESIUM 1.4 2.9 H mg/dL

SELECT ('E' to Edit, 'C' for Comments, 'W' Workload):

Approve for release by entering your initials: JM

LAST IN WORK LIST

Example \#2: File 60 test Site/Specimen new “USE FOR REFERENCE TESTING” field (#13) set to NO or NULL

Select Process data in lab menu Option: EM Enter/verify/modify data (manual) \<ENTER\>

Do you want to review the data before and after you edit? YES//\<ENTER\>

Do you wish to see all previously verified results? NO//\<ENTER\>

Select one of the following: \<ENTER\>

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// Accession Number\<ENTER\>

Select Accession: CH 1015 6 \<ENTER\>

CHEMISTRY (OCT 15, 2004) 6

Select Performing Laboratory: REGION 7 ISC,TX (DEMO)// \<ENTER\> WILFORD

HALL MEDICAL CENTER TX USAF 671CZ

Work Load Area: CHEM\<ENTER\>

1 CHEM 7

2 CHEMISTRY

CHOOSE 1-2: 2 CHEMISTRY\<ENTER\>

LSpatient,one 000-11-2222

Sample: SERUM\<ENTER\>

Specimen: SERUM 1 MAGNESIUM \<ENTER\>

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRProvider,One Voice pager: \<ENTER\>

Phone: Digital pager: \<ENTER\>

ACCESSION: CH 1015 6

10/15 17:50d

For test MAGNESIUM

UNITS: MD/DL

REFERENCE LOW: .5

REFERENCE HIGH: 1.2

CRITICAL LOW: .3

CRITICAL HIGH: 1.5

Result's Abnormality: Calculate from entered values// ? \<ENTER\>Example \#2: File 60 test Site/Specimen new “USE FOR REFERENCE TESTING” field (#13) set to NO or NULL *continued*

Select the abnormality if it cannot be calculated from reference values.

Select one of the following: \<ENTER\>

0 Calculate from entered values

1 Abnormal Low

2 Critical Low

3 Abnormal High

4 Critical High

Result's Abnormality: Calculate from entered values//\<ENTER\>

MAGNESIUM 1.4//1.4\<ENTER\>

Select COMMENT: \<ENTER\>

LRPatient,one SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRProvider,One Voice pager: \<ENTER\>

Phone: Digital pager: \<ENTER\>

ACCESSION: CH 1015 6

10/15 17:50d

MAGNESIUM 1.4 H MD/DL

SELECT ('E' to Edit, 'C' for Comments, 'W' Workload): \<ENTER\>

Approve for release by entering your initials: LRPO

LAST IN WORK LIST

#### Example \#3: Processing amended results from a reference laboratory

Select Process data in lab menu Option: EM Enter/verify/modify data (manual) \<ENTER\>

Do you want to review the data before and after you edit? YES//\<ENTER\>

Do you wish to see all previously verified results? NO//\<ENTER\>

Select one of the following: \<ENTER\>

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// Accession Number\<ENTER\>

Select Accession: TOX 1015 1

TOXICOLOGY (OCT 15, 2004) 1

Select Performing Laboratory: REGION 7 ISC,TX (DEMO)// \<ENTER\>MILWAUKEE VAMC WI VAMC 695

LRPatient,One 000-00-0000

Sample: BLOOD/SMT

These results have been approved by LRuser, One

on Oct 15, 2004@19:27:24

Specimen: SERUM

1 PROCAINAMIDE verified

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRProvider, One Voice pager:

Phone: Digital pager:

ACCESSION: TOX 1015 1

10/15 19:21d

PROCAINAMIDE 30.5 H\* ug/mL CRITICAL HIGH!!

If you need to change something, enter your initials: LRUO

SELECT ('E' to Edit, 'C' for Comments, 'W' Workload): Edit \<ENTER\>

PROCAINAMIDE 30.5

Amended result: 10 flag: None units: ug/mL

Accept amended results: Yes// \<ENTER\>

Inst Comments: PROCAINAMIDE reported incorrectly as 30.5 by \[235-VA695\].

Inst Comments: Changed to 10 on Oct 15, 2004@18:37 by \[235-VA695\].

Inst Comments: PROCAINAMIDE normalcy reported incorrectly as H\* by

Inst Comments: \[235-VA695\].

Inst Comments: Changed to normal on Oct 15, 2004@18:37 by \[235-VA695\].

Select COMMENT: Changed to normal on Oct 15, 2004@18:37 by \[235-VA695\].

//\<ENTER\>

COMMENT: Changed to normal on Oct 15, 2004@18:37 by \[235-VA695\].

Replace

Select COMMENT: \<ENTER\>

LRPatient,One SSN: 000-00-0000

Pat Info: Sex: MALE Age: 54yr as of Oct 15, 2004

Provider: LRprovider, One Voice pager: \<ENTER\>

Phone: Digital pager: \<ENTER\>

ACCESSION: TOX 1015 1

10/15 19:21d

PROCAINAMIDE 10 ug/mL

COMMENTS: PROCAINAMIDE reported incorrectly as 30.5 by \[235-VA695\].

COMMENTS: Changed to 10 on Oct 15, 2004@18:37 by \[235-VA695\].

COMMENTS: PROCAINAMIDE normalcy reported incorrectly as H\* by

COMMENTS: \[235-VA695\].

COMMENTS: Changed to normal on Oct 15, 2004@18:37 by \[235-VA695\].

If you need to change something, enter your initials:

Approve update of data by entering your initials: LRUO

PROCAINAMIDE reported incorrectly as 30.5 by \[235-VA170\].

Changed to 10 on Oct 15, 2004@19:39 by \[235-VA170\].

PROCAINAMIDE normalcy reported incorrectly as H\* by \[235-VA170\].

Changed to normal on Oct 15, 2004@19:39 by \[235-VA170\].

#### LAST IN WORK LIST

#### Turnaround times By Urgency \[LR TAT URGENCY\] option

Example: This option generates a report of the turnaround times for selected lab test for selected urgencies.

Select Lab statistics menu Option: TURnaround times By Urgency \<ENTER\>

LEDI Utility - Urgency Turnaround Time

This option generates a report of the turnaround time for selected

lab tests. Enter only those urgencies you want extracted. WKLD urgencies

will be included for each normal urgency selected. Enter the

test(s) you want the report display.

A detailed report is available to show the data being used to

compute the turnaround times.

Regular hours are from 7:01 AM to 5:00 PM

Irregular hours includes all other times, holidays and weekends.

Date to START with: TODAY// \<Enter\> (JUL 16, 1997)

Date to END with: 07/16/97// T (JUL 16, 1997) \<ENTER\>

Select the laboratory tests to be used in this report --

LABORATORY TEST: GLUCOSE

LABORATORY TEST: \<Enter\>

Urgencies: \<Enter\>

STAT

PLEASE DO NOT USE

ROUTINE

Enter all urgencies you want extracted.

URGENCY: STAT

URGENCY: \<Enter\>

Include a detailed report? No// \<Enter\> (No)

DEVICE: HOME// PRINTER\[NOTE: Enter site’s printer name\]

#### Example: Turnaround Times by Urgency—*continued*

LEDI Management Report - Urgency Turnaround Time

From JUL 16,1997 To JUL 16,1997

Date Printed: JUL 16,1997@11:25:26

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Turnaround Time (TAT) - Regular (0701-1700) hours

Number of tests Total time Ave TAT

---------------------- ---------- -------

2 62 min 31 min

Turnaround Time (TAT) - Irregular hours

Number of tests Total time Ave TAT

---------------------- ---------- -------

13 300 min 23 min

Urgencies:

STAT

WKL - STAT

Tests:

GLUCOSE

#### Edit the default parameters Load/Work list \[LRLLE DFT\] option

Example: This function allows the user to edit the default parameters of the Load/Work list file so that the preparation of load or work lists can reflect the way the tests are being done on the instrument or at the bench. Use this option to set a default reference laboratory for a specific profile on a load/work list that is used to process reference lab oratory results via a LEDI interface.

Select Supervisor menu Option: Edit the default parameters Load/Work list\<ENTER\>

Select LOAD/WORK LIST NAME: CHEMISTRY \<ENTER\>

LOAD TRANSFORM: \<ENTER\>

TYPE: SEQUENCE/BATCH//\<ENTER\>

CUPS PER TRAY: 100//\<ENTER\>

FULL TRAY'S ONLY: NO//\<ENTER\>

EXPAND PANELS ON PRINT: YES//\<ENTER\>

INITIAL SETUP: \<ENTER\>

VERIFY BY: ACCESSION//\<ENTER\>

SUPPRESS SEQUENCE \#: NO//\<ENTER\>

INCLUDE UNCOLLECTED ACCESSIONS: NO//\<ENTER\>

SHORT TEST LIST: NO//\<ENTER\>

WKLD METHOD: DU PONT ACA//\<ENTER\>

Select PROFILE: CHEMISTRY CHEMISTRY\<ENTER\>

ACCESSION AREA: CHEMISTRY//\<ENTER\>

UID VERIFICATION: ANY ACCESSION AREA//\<ENTER\>

STORE DUPLICATE COMMENTS: \<ENTER\>

DEFAULT REFERENCE LABORATORY: MILWAUKEE VAMC WI VAMC 695\<ENTER\>

Select PROFILE: \<ENTER\>

#### Edit atomic tests \[LRDIEATOMIC\] option

Use this option to designate if the values for test units and normals are to be used when a user is manually entering reference laboratory results or should the user be prompted for these values.

Example: Edit fields in the LABORATORY TEST file (#60) for tests which are single valued.

Select Supervisor menu Option: Edit atomic tests \<ENTER\>

Select LABORATORY TEST NAME: MAGNESIUM MG\<ENTER\>

NAME: MAGNESIUM//\<ENTER\>

Select SYNONYM: MG//\<ENTER\>

TYPE: BOTH//\<ENTER\>

SUBSCRIPT: CHEM, HEM, TOX, SER, RIA, ETC.// \<ENTER\>

DATA NAME: MAGNESIUM//\<ENTER\>

Select SITE/SPECIMEN: PLASMA/\<ENTER\>/

SITE/SPECIMEN: PLASMA//\<ENTER\>

REFERENCE LOW: .7//\<ENTER\>

REFERENCE HIGH: 1.4//\<ENTER\>

CRITICAL LOW: 3//\<ENTER\>

CRITICAL HIGH: .5// \<ENTER\>

INTERPRETATION: \<ENTER\>

1\>

UNITS: IU/L//\<ENTER\>

TYPE OF DELTA CHECK: \<ENTER\>

DELTA VALUE: \<ENTER\>

DEFAULT VALUE: .9//\<ENTER\>

USE FOR REFERENCE TESTING: y YES\<ENTER\>

Select SITE/SPECIMEN: serum 0X500

...OK? Yes//\<ENTER\> (Yes)

SITE/SPECIMEN: SERUM//\<ENTER\>

REFERENCE LOW: 2//\<ENTER\>

REFERENCE HIGH: 2.6//\<ENTER\>

CRITICAL LOW: \<ENTER\>

CRITICAL HIGH: \<ENTER\>

INTERPRETATION: \<ENTER\>

1\>

UNITS: mg/dL//\<ENTER\>

TYPE OF DELTA CHECK: \<ENTER\>

DELTA VALUE: \<ENTER\>

DEFAULT VALUE: 1.4//\<ENTER\>

USE FOR REFERENCE TESTING: YES// ?? \<ENTER\>

Indicates if the reference ranges and units associated with this

specimen type can be used when manually entering results of testing

performed at another laboratory.

Choose from:

0 NO

1 YES

USE FOR REFERENCE TESTING: YES//\<ENTER\>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary of terms relates to the LEDI III software application and documentation:
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Glossary of Terms</td>
<td>Descriptions</td>
</tr>
<tr class="even">
<td>AA</td>
<td></td>
</tr>
<tr class="odd">
<td>AAC</td>
<td>Austin Automation Center</td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CAP</td>
<td>College of American Pathologists</td>
</tr>
<tr class="even">
<td>COLLECTION Facility</td>
<td><p>The laboratory that collects the patient’s specimen. After the specimen is collected, the COLLECTION facility should:</p>
<p><strong>*</strong>Create an electronic Shipping Manifest (specifying the lab tests to be performed by the HOST facility laboratory).</p>
<p><strong>*</strong>Transmit the Shipping Manifest List to HOST facility laboratory.</p>
<p><strong>*</strong>Transport the specimen by carrier to HOST facility laboratory.</p></td>
</tr>
<tr class="odd">
<td>CHCS</td>
<td>Composite Health Care System</td>
</tr>
<tr class="even">
<td>CMOP</td>
<td>Consolidated Mail Outpatient Pharmacy</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Data Fields</td>
<td>The information base associated with a segment.</td>
</tr>
<tr class="odd">
<td>Data Type (DT)</td>
<td>Restrictions on the contents of the data field as defined by the HL7 Standard.</td>
</tr>
<tr class="even">
<td>DISA</td>
<td>Defense Information Systems Administration</td>
</tr>
<tr class="odd">
<td>DoD</td>
<td>Department of Defense</td>
</tr>
<tr class="even">
<td>DVAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Electronic Catalog</td>
<td>The Electronic Catalog contains laboratory tests available for the COLLECTION facility to order.</td>
</tr>
<tr class="odd">
<td>Element Name</td>
<td>Globally unique descriptive name for the field.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FTP</td>
<td>File Transfer Protocol</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level Seven (standard for electronic data exchange/messaging protocol</td>
</tr>
<tr class="even">
<td>HOST Facility</td>
<td>The laboratory that receives the patient’s specimen and performs the requested specimen testing and analysis.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Glossary of Terms</td>
<td>Descriptions</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>IKE</td>
<td>Internet Key Exchange</td>
</tr>
<tr class="even">
<td>IP</td>
<td>Internet Protocol</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LDSI</td>
<td>Laboratory Data Sharing and Interoperability</td>
</tr>
<tr class="even">
<td>LEDI</td>
<td>Laboratory Electronic Data Interchange</td>
</tr>
<tr class="odd">
<td>Length (LEN)</td>
<td>The maximum number of characters that one occurrence of the data field may occupy.</td>
</tr>
<tr class="even">
<td>LIM</td>
<td>Laboratory Information Manager</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NLT</td>
<td>National Laboratory Test</td>
</tr>
<tr class="odd">
<td>NLTS</td>
<td>VA National Laboratory Test File</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OIFOs</td>
<td>Office of Information Field Offices</td>
</tr>
<tr class="even">
<td>Optionally (R/O/C)</td>
<td><p>Whether the data field is required, optional, or conditional in a segment. The designations are:</p>
<p>*R - required</p>
<p>*O (null) - optional</p>
<p>*C - conditional on the trigger event</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PID</td>
<td>Patient Identification</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Repetition (RP/#)</td>
<td><p>Whether the field may repeat. The designations are:</p>
<p><strong>N (null)</strong> - for no repetition allowed; <strong>Y</strong> - the field may (null) - for no repetition allowed; <strong>Y</strong> - the field may repeat an indefinite or site determined number of times; and (integer) - the field may repeat up to the number of times specified in the integer. The ordinal position of the data field within.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Segments</td>
<td>A logical grouping of data fields.</td>
</tr>
<tr class="odd">
<td>Sequence Number (SEQ)</td>
<td>The ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table.</td>
</tr>
<tr class="even">
<td>Shipping Manifest</td>
<td>The shipping manifest is a document listing of lab specimens sent outside the facility to a reference lab for processing.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Glossary of Terms</td>
<td>Descriptions</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Table (TBL#)</td>
<td>This is a table of values that may be defined by HL7 or negotiated between the VistA Laboratory application and the vendor system.</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td>Transmission Communication Protocol/Internet Protocol</td>
</tr>
<tr class="odd">
<td>Trading Partners</td>
<td>An established relationship between two or more laboratories for receiving and processing lab specimens.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>UI</td>
<td>Universal Interface</td>
</tr>
<tr class="even">
<td>UID</td>
<td>Unique Identifier assigned to each laboratory accession.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="odd">
<td>VDL</td>
<td>VistA Documentation Library</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="even">
<td>VistA Laboratory UI and LEDI HL7 Interface Standard Specifications<br />
V. 1.1</td>
<td>This document specifies an interface to the VistA Laboratory software application based upon the Health Level Seven (HL7) Standard. This interface forms the basis for the exchange of healthcare information between the VistA Laboratory software application and all non- VistA systems. Especially those non-VistA systems that generate laboratory result information.</td>
</tr>
<tr class="odd">
<td>VPN</td>
<td>Virtual Private Network (firewall)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>WAN</td>
<td>Wide Area Network</td>
</tr>
<tr class="even">
<td>Workload System</td>
<td>This is a method of tracking number of LEDI specimens processed.</td>
</tr>
</tbody>
</table>
