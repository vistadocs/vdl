---
title: LA*5.2*64/LR*5.2*286 LEDI III Installation Guide
doc_type: IG
doc_label: Installation Guide
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
  - table
  - contents
  - ledi
  - laboratory
  - vista
  - test
  - software
  - results
  - message
  - modified
page_count: 0
word_count: 14645
section_count: 35
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iii_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iii_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

![](la-5-2-64-lr-5-2-286-ledi-iii-installation-guide/001.png)

LABORATORY ELECTRONIC DATA INTERCHANGE lII (LEDI III)

INSTALLATION GUIDE

LA\*5.2\*64/LR\*5.2\*286

December 2004

Department of Veterans AffairsVistA Health Systems Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Staffing Requirements:](#staffing-requirements)
    - [Information Resource Management (IRM) Staff](#information-resource-management-irm-staff)
    - [IRM and LIM Staff](#irm-and-lim-staff)
  - [### Intended Users](#intended-users)
  - [VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT](#vista-blood-bank-software-v52-device-product-labeling-statement)
    - [Patch LR\5.2\286](#patch-lr52286)
    - [Patch LA\5.2\64](#patch-la5264)
- [Orientation](#orientation)
    - [LEDI III Installation Guide Screen Displays](#ledi-iii-installation-guide-screen-displays)
  - [LEDI III Software and Documentation Retrieval Locations](#ledi-iii-software-and-documentation-retrieval-locations)
    - [LEDI III Software and Documentation Retrieval Formats](#ledi-iii-software-and-documentation-retrieval-formats)
    - [VistA Website Locations:](#vista-website-locations)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [VistA Laboratory Electronic Data Interchange Phase III (LEDI III)](#vista-laboratory-electronic-data-interchange-phase-iii-ledi-iii)
  - [LEDI III Enhancements and Modifications](#ledi-iii-enhancements-and-modifications)
    - [Enhancements:](#enhancements)
    - [Modifications:](#modifications)
- [Security Information](#security-information)
  - [Security Management:](#security-management)
    - [Overview of VA/DOD Communications Functionality](#overview-of-vadod-communications-functionality)
    - [Technical Requirements](#technical-requirements)
    - [VA Security](#va-security)
  - [Security Features:](#security-features)
    - [Mail Groups](#mail-groups)
    - [### Alerts](#alerts)
    - [MailMan Bulletins](#mailman-bulletins)
    - [Remote Systems](#remote-systems)
    - [### Archiving Capabilities](#archiving-capabilities)
    - [Purging Capabilities](#purging-capabilities)
    - [Contingency Planning](#contingency-planning)
    - [Users Interface](#users-interface)
    - [### Instrument Interfacing](#instrument-interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [### Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [References](#references)
    - [Official Policies](#official-policies)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Test Account](#test-account)
  - [Staffing Requirements:](#staffing-requirements-1)
    - [Information Resource Management (IRM) Staff](#information-resource-management-irm-staff-1)
    - [IRM and LIM Staff](#irm-and-lim-staff-1)
  - [### Intended Users](#intended-users-1)
    - [Users Interface](#users-interface-1)
  - [Communications Interfaces](#communications-interfaces)
  - [Hardware Platform](#hardware-platform)
  - [## Hardware Interfaces](#hardware-interfaces)
  - [LEDI III Equipment Requirements](#ledi-iii-equipment-requirements)
  - [### Collection Facility Equipment Requirements](#collection-facility-equipment-requirements)
    - [HOST Facility Equipment Requirements](#host-facility-equipment-requirements)
  - [Performance Requirements](#performance-requirements)
  - [LEDI III Implementation Requirements](#ledi-iii-implementation-requirements)
  - [Memory Constraints](#memory-constraints)
  - [## ## Disk Space Requirements](#disk-space-requirements)
  - [Performance/Capacity Impact](#performancecapacity-impact)
  - [## Kernel Installation and Distribution System (KIDS)](#kernel-installation-and-distribution-system-kids)
  - [Health Level Seven (HL7)](#health-level-seven-hl7)
  - [## ^VASITE](#vasite)
  - [Namespace](#namespace)
  - [Nightly Task](#nightly-task)
  - [Data Base Integration Agreements (DBIAs)](#data-base-integration-agreements-dbias)
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
  - [LEDI III New and Modified Options](#ledi-iii-new-and-modified-options)
    - [New Options](#new-options)
    - [Modified Options](#modified-options)
  - [## VistA Software Requirements](#vista-software-requirements)
  - [VistA Patch Requirements](#vista-patch-requirements)
  - [Patch LA\5.2\64 Routine Summary List](#patch-la5264-routine-summary-list)
  - [Patch LR\5.2\286 Routine Summary List](#patch-lr52286-routine-summary-list)
- [Installation Instructions](#installation-instructions)
    - [Suggested Time to Install Patches](#suggested-time-to-install-patches)
    - [Example: LEDI III Installation Process:](#example-ledi-iii-installation-process)
- [Post-Installation Instructions](#post-installation-instructions)
  - [IRM Staff:](#irm-staff)
    - [Step 1:](#step-1)
    - [Step 2:](#step-2)
    - [Step 3:](#step-3)
The Veterans Health Information Systems and Architecture (Vist*A*) Laboratory Electronic Data Interchange III (LEDI III) Patch LA\*5.2\*64 and Patch LR\*5.2\*286 Installation Guide Version 5.2 provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) staff, Laboratory Information Manager (LIM), and other DVAMC users with a straightforward means for installing the LEDI III software application.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resource Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for installing patches LA\*5.2\*64 and LR\*5.2\*286, defining mail groups, and menu assignments.

### IRM and LIM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The COLLECTION and HOST facilities IRM and LIM staff must coordinate the implementation of the LEDI III setup after the patches are installed. The LEDI III setup process must be performed in the sequence specified in the VistA LEDI III Implementation and User Guide.

## ### Intended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users of this software enhancement project include VA medical center’s laboratory personnel and DoD medical center laboratory personnel.

## VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch LR\*5.2\*286

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Package patch LR\*5.2\*286 contains changes to software controlled by VHA DIRECTIVE 99-053, titled VistA BLOOD BANK SOFTWARE VERSION 5.2. Change includes:

The addition of the “USE FOR REFERENCE TESTING” field (#13) to the “SITE/SPECIMEN SUB-FIELD” (#60.01) of the LABORATORY TEST file (#60).

The addition of the “USE FOR REFERENCE TESTING” field to the “LR ATOMIC TESTS” Input Template.

The above change has been reviewed by the VistA Blood Bank Developer and found to have no impact on the VistA BLOOD BANK SOFTWARE version 5.2 control functions.

RISK ANALYSIS: Changes made by patch LR\*5.2\*286 have no effect on Blood Bank software functionality, therefore RISK is none.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR\*5.2\*286 does not alter or modify any software design safeguards or safety critical elements functions.

POTENTIAL IMPACT ON SITES: This patch contains changes to a Data Dictionary identified in Veterans Health Administration (VHA) Directive 99-053. The changes have no effect in Blood Bank functionality or medical device control functions. There is no adverse potential to sites.

VALIDATION REQUIREMENTS BY OPTION: There are no required validation scenarios to be completed by sites after installing LR\*5.2\*286.

### Patch LA\*5.2\*64

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*64 does not contain any changes to the VistA BLOOD BANK Software as defined by VHA DIRECTIVE 99-053 titled VistA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*64 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LA\*5.2\*64 have no effect on Blood Bank software functionality, therefore RISK is none.

VALIDATION REQUIREMENTS BY OPTION: Because of the nature of the changes made, no specific validation requirements exist as a result of installation of this patch.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III Installation Guide (Patches LA\*5.2\*64/LR\*5.2\*286) focuses on easy-to-follow step-by-step instructions. This document consists of the following sections:

Pre-Installation Information: This section lists the requirements that must be acknowledged prior to installing the software.

Installation Instructions: This section contains installation instruction including detailed examples of the actual installation process.

Post Installation Information: This section provides all the necessary instructions required to implement the software after the installation process is completed.

### LEDI III Installation Guide Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Screen Captures

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

#### User Response

User entry response appears in boldface type Courier font, no larger than 10 points. Example:Boldface type

#### #### Return Symbol

User response to computer dialogue is followed by the \<RET\> symbol that appears in Courier font, no larger than 10 points, and bolded. Example: \<RET\>

#### Tab Symbol

User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded. Example: \<Tab\>

## LEDI III Software and Documentation Retrieval Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

VistA LEDI III software, Installation Guide, and User Manual are available at the following Office of Information Field Offices (OIFOs) on the ANONYMOUS.SOFTWARE directories:

| OI FIELD OFFICE                    | FTP ADDRESS                    | DIRECTORY                      |
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
| LAB_LEDI_III_IG.DOC     | LABORATORY ELECTRONIC DATA INSTALLATION GUIDE            | BINARY            |
| LAB_LEDI_III_IMP_UG.DOC | LABORATORY ELECTRONIC DATA IMPLEMENTATION AND USER GUIDE | BINARY            |

### VistA Website Locations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA LEDI III Installation Guide (i.e., LAB_LEDI_III_IG.PDF and LAB_LEDI_III_IG.DOC) and LEDI III User Manual (i.e., LAB_LEDI_III_IMP_UG.PDF and LAB_LEDI_III_IMP_UG.DOC) in Portable Document Format (PDF) and MS Word (DOC) Format are available at the following VistA Intranet locations:

#### Laboratory Version 5.2 Home Page

<span class="mark">REDACTED</span>

#### VistA Documentation Library (VDL)

[www.va.gov/vdl/](http://www.va.gov/vdl/)

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

> However, there are potentially situations, which do not allow this feature to be implemented for a specific test. If a site has old results or has never archived then there may be results stored under a data name with no normals/units etc., which were entered using previous versions of the Laboratory package. When test results in LAB DATA file \#63 are found with no unit and/or normals the software goes back to LABORATORY TEST file \#60 to retrieve these values. Changing the units and/or normals associated with a File \#63 data name in File \#60 would alter the units/ and/or normals reported on previous results.

*1. General LEDI Functionality*

- The process of building orders in the LAB PENDING ORDERS ENTRY file (#69.6) is enhanced to use additional information from the HL7 Order (ORM) message. This new functionality will store comments and other test results that accompany an order in the LAB PENDING ORDERS ENTRY file (#69.6).
- Added the new Start a Shipping Manifest \[LA7S MANIFEST START\] option, which allows a manifest to be started without performing a manifest build. Specimens can then be added manually, instead of automatically, using the Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option.
- Added the new Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option which is used to enter relevant clinical information that should accompany a test order on a manifest.
- Enhanced routine LA7VHL to call HL7 supported API.
  - Enhanced routine LA7VMSG1 to check if \$QUERY of ^TMP global has returned a null value. Under certain conditions an illegal function call error could be observed Enhanced routine LA7VLL, LA7VSTP, and LA7VSTP1 to setup LA7V\* logical links without \<space\> between "LA7V" and station number. Allows HL7 package to display logical links for DoD sites which utilize DoD DMIS ID codes as facility identifiers similar to VA station numbers. HL7 package only displays first 8 characters of logical link name. Option LEDI Setup \[LA7V SETUP\] will only support creation of TCP logical links. When setting up LEDI between VA facilities the software will default to using TCP/IP via the standard HL package logical links VAxxx.
  - Enhanced routine LA7PURG to purge shipping manifests from LAB SHIPPING MANIFEST file (#62.8) when all related accessions have been purged from ACCESSION file (#68) (E3R \#18036). Orders in the LAB PENDING ORDERS ENTRY file (#69.6) are purged when the date completed is \>365 days, when the order transmitted date is \>720 days or when the order transmitted date is \>360 and the order status is Results/data Received.
  - Enhanced the display of manifest list in inverse order.
  - Enhanced shipping manifest to add requesting provider's contact information.
  - Added four new alerts/mail bulletins

  
*2. Laboratory Result Verification*

- Enhanced verification process to specify the performing laboratory
- Enhanced results from reference lab to store test results “as is”
- Enhanced receipt of amended reports to generate a Mail Man bulletin
- Enhanced amended reports to be processed via the EM Enter/verify/modify data (manual) \[LRENTER\] option
- Enhanced the system to add units and normal values specified in File \#60
- Enhanced the evaluation of normalcy status dealing with results of zero.
- Enhanced audit trail normalcy status change triggers audit trail comments
- Enhanced verification process to display ordering provider's phone and pager information
- Enhanced CPRS GUI lab results display to include units and normal values –Display of lab results in CPRS GUI and Laboratory Interim Reports has been modified to display units and normals associated with results at time of verification. Results that are derived from a Set of Codes will be reported using the external form of the code.
- Enhanced CPRS GUI display to include the performing laboratory.
- Enhanced EA and EM options to display patient information - Enter/verify data (auto instrument) \[LRVR\] and Enter/verify/modify data (manual) \[LRENTER\] options will display patient information from field PAT. INFO. (#.091) in LAB DATA file (#63), patient’s sex and age at time of specimen collection date/time during result verification.
- Enhanced result alignment to display right-justified.
- Enhanced routine LRWLST1 to check and set the ACCESSION file (#68) DATE sub-file’s zero nodes via FileMan DBS call.
- Enhanced routine LRWLST1 to determine treating specialty.

### Modifications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modified routine LR7OB63 to correct trimming leading and trailing spaces but leave embedded spaces when displaying lab test results.
- Modified routine LR7OR2tocorrect trimming leading and trailing spaces but leave embedded spaces when displaying lab test results.
- Modified Referral Patient Multi-purpose Accession option to check pending orders.
- Modified EM option to allow entering verifier’s initials in mixed case.
- Modified LRWLST11 to store the correct ordering and collecting sites.
- Modified routine LR7OGMP to increase the space allocated on display
- Modified display of results using the external value for set of codes data types.

> NOTE: If existing tests using the data type SET OF CODES are configured in reverse, such as Neg stands for N, then these tests should be edited and the values reversed.

- Modified supported API call \$\$FMDATE^HLFNC to recommended Kernel supported API's \$\$HL7TFM^XLFDT and \$\$FMTHL7^XLFDT respectively.
- Modified supported API call \$\$HLDATE^HLFNC to recommended Kernel supported API's \$\$HL7TFM^XLFDT and \$\$FMTHL7^XLFDT respectively.
- Modified input transform of DATE/TIME OF MESSAGE field (#106) in LA7 MESSAGE QUEUE file (#62.49) to use Kernel supported API \$\$HL7TFM^XLFDT instead of \$\$HLDATE^HLFNC.
- Modified routine LA7VHL to call HL7 supported RSPINIT^HLFNC2 to obtain message delimiters that HL7 package will use when building MSH header of application acknowledgement message. Previous call to INIT^HLFNC2 would return incorrect headers under certain conditions.

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Memorandum, Department of Veteran Affairs, dated July 3, 2003, Subject: Full Authority to Operate the VHA Virtual Private Network (VPN) Supporting the DoD/VA Consolidated Mail Outpatient Pharmacy (CMOP).

### Overview of VA/DOD Communications Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Connectivity closely follows that established by the DoD-VA Consolidated Mail Outpatient Pharmacy (CMOP). Electronic requests, generated by VistA LEDI software, will be sent from VA medical center COLLECTION laboratory to a designated HOST Laboratory (DoD MTF) using HL7 messaging format over a TCP/IP connection. The DoD HOST Laboratory, upon receipt of the physical specimen, will process the electronic request order. An HL7 formatted message is created by the HOST Laboratory containing test results and is returned to the VA COLLECTING Laboratory. Upon receipt of the test results, the clinical data is stored in the patient’s electronic clinical record.

> 1\. The VA medical center using the VistA LEDI software creates a HL7 formatted electronic order message. The order message contains all required patient information to indicate to the DoD HOST Laboratory what procedures are to be performed. The LEDI software hands the HL7 formatted message to the VistA HL7 software for delivery to the DoD HL7 server.

1.  The DoD HL7 server processes the VA COLLECTING facilities order message. The DoD Host Laboratory performs the analytical testing generating tests results. The test result are verified and released by the technologist. The DoD HOST Laboratory creates an HL7-formatted message containing result information, and sends the message to the VA COLLECTING Laboratory’s HL7 server.
2.  The VA Collecting Laboratory HL7 server accepts and processes the HL7 message. The HL7 server then passes the message to the LEDI software for further processing. The LEDI software then stores the electronic result message to be accepted by the VA medical technologist.
3.  The submitting laboratory technicians/technologists review the results on the screen for completeness and clinical believability. If the results are acceptable, the submitting laboratory personnel certify them and record them in the patient’s electronic clinical record.

### Technical Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software impact on the Veterans Health Information System and Technology Architecture (VistA) is expected to be minimal. The DoD interface will directly connect to an existing DoD-VA gateway at the Austin Automation Center (AAC), and from that point will be processed like any other VistA laboratory request from a remote VA facility. Functional requirements include:

1.  The Austin gateway shall support HL7 messaging over an interactive TCP/IP connection to the DoD connection point. This HL7 interface will allow the agencies to share data. The VistA HL7 software will manage data transmission over the TCP/IP connection ensuring message delivery.
4.  The Austin gateway shall develop encryption/decryption processes that meet VHA and DoD standards. All data files must be encrypted/decrypted using an approved encryption algorithm to meet standards set by VHA and DoD. An existing DoD-VA gateway will be used that provides a secure VPN connection and firewall DMZ with proxy servers and appropriate routing entries to ensure that only legitimate sources and destinations are allowed through for transmission. The DoD-CMOP system already has an IATO in place, signed May 9, 2002.

#### Methodology

CHCS and VistA exchange data using HL7 messages that are transmitted when triggering events occur. Computer connectivity between CHCS and VistA is over a transient TCP/IP connection. Two TCP sockets on each system provide communications between the two systems. Within the context of each TCPIP socket, VistA and multiple CHCS sites may connect as a client or a server. Lower-level connectivity is provided via HL7 Minimal Lower Layer Protocol.

A Virtual Private Network (VPN) will be established on an isolated tunnel from the VA national gateway to DoD medical treatment facilities. The outbound communication will be from the VA COLLECTING Laboratory requests to the DoD facilities. Inbound traffic will contain released data from DoD HOST Laboratory as illustrated in the following diagram.

![](la-5-2-64-lr-5-2-286-ledi-iii-installation-guide/002.png)

HL7 messages will be generated from CHCS sites, transported securely over the DoD-VA VPN, and then routed to VAMCs where requests will be processed by the LEDI software on the existing VistA systems.

The service is to provide an inbound access method that is a system-to-system connection, not a user to system connection. A hardware server-to-server VPN will be used to connect the VA Wide Area Network (WAN) to the DoD Wide Area Network WAN.

The need for this connection is to enable connectivity for the current network architecture under each agency’s existing network umbrella, utilizing existing firewalls, gateways, and other security measures. Interfaces and protocols will be developed to electronically communicate transactions between DoD and VA testing facilities.

The file size transferred daily would be approximately 14.2 MB, but also dependent upon the type of laboratory tests requested. The data will be transmitted as needed and not associated with a scheduled time.

This initiative will use the existing Avaya VPN Service Unit (VSU) 5000 to create a virtual private network at the AAC national gateway. The VSU 5000 is a commercial product that enables organizations to securely connect remote users in a cost effective manner. Additional Avaya product information will be reviewed in subsequent sections of this document. The DoD will use the VSU 5000s to provide the isolated tunnel that will connect the source and destination points for the laboratory data. For VA, the desired destination point is the AAC.

### VA Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security and protective measures for this project will utilize the existing capabilities and strengths currently employed by the Austin Automated Center. Specific security controls will comply with the VA's Office of Cyber Security, DoD's security standards for C2, and current industry practices. In the document "VA Confidentiality" dated November 2001, there are three business cases for which security and confidentiality are required to support and protect sensitive information. The first and foremost business case, which directly applies to this initiative, is for VA to provide VA business partners "some controlled access to VA internal networks via a secured end-to-end connection". By employing VPN technology, coupled with Internet Key Exchange (IKE), 3DES encryption (DH group 2), SHA (Secure Hash Algorithm)-1, and PFS (Perfect Forward Secrecy), the requirements for security and confidentiality can be met.

The information that will be processed over the VHA systems, as defined by the Computer Security Act of 1987, the Privacy Act, and VHA Security Directive 0170, has been categorized as Level 2: Sensitive. This category of information includes sensitive information with a medium level of sensitivity that requires the implementation of protection measures that are stronger than the minimum levels permitted by VHA regulations and policy.

> *Automated systems of record subject to the Privacy Act which contain information that meets the qualification for Exemption 6 of the Freedom of Information Act; i.e. for which unauthorized disclosure would constitute a “clearly unwarranted invasion of person privacy” and likely lead to specific detrimental consequences for the individual in terms of financial, employment, medical, psychological or social standing.*

The roles and responsibilities associated with the Certification & Accreditation (C&A) process demonstrate the collaborative effort that has been undertaken by both agencies. VHA and DoD are jointly responsible to address the required security elements and processes necessary to establish this initiative. An overview of the C&A process is outlined in the ITSCAP, VHA Handbook 6214.

The DoD Defense Information Systems Agency (DISA) has provided one VSU-5000 VPN device located and operational at the AAC. The AAC will have primary responsibility for operations and security functions that relate to the VSU-5000. DISA has management responsibility for the VSU-5000 located at the AAC. However, the VA has been granted console access to the VSU-5000 that allows VA visibility into the configuration of the device and construction of the VPN security associations.

## Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following mail groups are required to successfully utilize the LEDI III functionality. LEDI III uses VA MailMan or TCP/IP as the medium to transmit and receive data from remote systems.

#### #### LAB MESSAGING Mail Group

This is a general mail group used by the LAB Universal Interface and LEDI III software to address alerts when conditions are detected requiring review and/or corrective action. The members of this mail group should, at the minimum, include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI III software. The software utilizes several Kernel Alerts. These alerts are triggered and sent to members of the LAB MESSAGING mail group for the following conditions:

When the scheduled tasked Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option or the Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] option is run and more than 500 entries are found scheduled for downloading via the Lab Universal Interface an alert is sent notifying members of this condition.

When the scheduled tasked Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option or the Lab Messaging File Integrity Checker \[LA7 CHECK FILES\] option is run and LA7 MESSAGE QUEUE file (#62.49) is found to have bad entries and/or cross-references. An alert is sent notifying members of this condition.

#### LA7V\* Mail Group

These mail groups are used by the HEALTH LEVEL SEVEN (HL7) package for transmitting LEDI HL7 messages when VA MailMan is selected as the HL7 communication protocol. These mail groups are created by the LEDI Setup \[LA7V SETUP\] option using the LA7V name space concatenated with the receiving facility’s primary station number. For example, to send HL7 messages to Dallas OI Field Office, VA Station Number 170, the LEDI Setup option would create a mail group LA7V 170. Other than the remote member added by the LEDI Setup option, no local or remote members should be added to these mail groups.

#### Local Mail Group

It is highly recommended that each facility designate local mail groups for receiving the “New Results”, “Orders Received”, and the “Error on Message “ alerts associated with the LEDI III software application. Please review the following section on Alerts and MailMan Bulletins for information on the various alerts that are generated by LEDI III.

### ### Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III software uses the LA7 MESSAGE PARAMETER file (#62.48) for sending alerts to the mail group specified in the ALERT CONDITION subfile (#62.481). The facility should designate a local mail group to use for notification of the alerts. These alerts and the associated mail group are configured using the LEDI Setup \[LEDI SETUP\] option, within the message configuration section of this option. The following are the three types of alerts that can be turned on for each configuration:

New Results Alert: Notifies members when the Lab Universal Interface software has processed an HL7 message containing test results. An example of this information type of alert is Lab Messaging – New results received for LA7V HOST 578.

Error Alert: Notifies members of error conditions encountered during the processing of a Laboratory Universal Interface message. Recommend that sites utilize the LAB MESSAGING mail group to notify local users of error conditions within the Laboratory Universal Interface/LEDI software. Processing the alert allows the user to view/print the error message and the associated HL7 message. An example of this action type of alert is “Lab Messaging error \#17 on message \#246164473.”

New Orders Received Alert: Notifies members when the Laboratory Universal Interface software has received electronic orders related to a collecting facility’s shipping manifest. An example of this information type of alert is Lab Messaging - Manifest# 537-20011030-3 received from LA7V COLLECTION 537.

### MailMan Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Four new alerts/mail bulletins are generated when processing LEDI HL7messages. These alerts and corresponding bulletins are addressed to the mail group designated to receive the NEW RESULTS alert specified by the site in LA7 MESSAGE PARAMETER file (#62.48) for LEDI type interfaces.

> a\. Mail bulletin: LA7 ABNORMAL RESULTS RECEIVED - Mail bulletin created by Laboratory package when processing a LEDI interface type HL7 result (ORU) message which contains laboratory testing results that are flagged as critical or abnormal. Values that are critical will always trigger the alert and bulletin. Values that are abnormal low or high will be triggered when site has flagged the corresponding test in AUTO INSTRUMENT file (#62.4), NOTIFY ABNORMAL FLAGS field (#22) within the CHEM TEST multiple (#30) for the interface.

> b\. Mail bulletin: LA7 AMENDED RESULTS RECEIVED - Mail bulletin created by Laboratory package when processing a LEDI interface type HL7 result (ORU) message which contains laboratory testing results that are flagged as amended.

> c\. Mail bulletin: LA7 UNITS/NORMALS CHANGED - Mail bulletin created by Laboratory package when processing a LEDI interface type HL7 result (ORU) message which contains laboratory test result units and/or normals different from values specified for test in LABORATORY TEST file (#60) and which are flagged to be used for reference testing purposes.

> d\. Mail bulletin: LA7 ORDER STATUS CHANGED - Mail bulletin created by Laboratory package when processing a LEDI interface type HL7 message.

When an order acknowledgment (ORR) message that contains laboratory test order status changes that indicates the order is not correct or cannot be performed/completed. Currently only supported on LEDI interfaces with DoD facilities.

When an order result (ORU) message and it indicates that the reference laboratory has added a laboratory test to the original order.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remote systems are defined as any computer system sending to and receiving HL7 messages from the HOST laboratory computer system. In VA-to-VA configurations, this can be within the same system (i.e. multidivisional sites), or it can be from one system to another system, (i.e. non-related sites). In the case of non-VA computer systems connection to remote systems for:

- DoD facility (CHCS systems) via approved VA/DoD VPN
- All others via a Generic Interface Manager (GIM). The GIM is the remote system, not the non-VA computer system.

Implementation of an HL7 messaging interface between the VA VistA Laboratory package and a non-VA information system consists basically of three parts:

- VistA Laboratory LEDI III software.
- Certified communication software and hardware.
- Non-VA information system capable of sending and receiving Laboratory HL7 order and result messages.

All three parts must be functional to utilize the capabilities of this LEDI III software patch. The implementation, setup, and configuration of vendor provided hardware and software are NOT addressed by this documentation. Consult the vendor provided documentation and instructions to interface to the VistA Laboratory package. LEDI III in support of VA/DoD Laboratory Data Sharing Initiative (LDSI) uses the VA/DoD VPN located at the Austin Automation Center to provide secure encrypted communications between VA and DoD facilities.

LEDI III utilizes the HL7 V. 2.3 Standard (HL7 V2.2 Standard with DoD Facilities) and the VistA HL V 1.6 software to transmit and receive HL7 messages via VA MailMan or Transmission Control Protocol/Internet Protocol (TCP/IP). The software transmits unsolicited order and result messages and receives acknowledgments back confirming or opposing the proper delivery of the messages. One or more order messages are transmitted for every manifest or lab delivery to a remote facility system. One or more result messages are sent to each facility per verifying session. To reduce the turn around time and network mail traffic, TCP/IP is recommended as the message delivery medium.

### ### Archiving Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently there are no archiving capabilities required for this software release.

### Purging Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III purging capabilities are provided through the Universal Interface (UI) software. The Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option is used to purge messages in the LA7 MESSAGE QUEUE file (#62.49) when the messages become eligible for purging. This option must be scheduled to run daily, preferably during a period when activity in the Lab Messaging (i.e., UI and LEDI software) is at a minimum. See the Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option description for additional information and functionality. Purging of messages for each configuration can be set in the LA7 MESSAGE PARAMETER file (#62.48) using the GRACE PERIOD FOR MESSAGES field (#3). The Default value is 3 days.

Purging of LAB PENDING ORDERS ENTRY file (#69.6) is performed when orders that have a status of Results/data Received and are older that 360 days. Orders are also purged when they reach 730 days.

Purging of manifests in LAB SHIPPING MANIFEST file (#62.8) and related events in LAB SHIPPING EVENT file (#62.85) occurs when all related accessions have been purged from ACCESSION file (#68).

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each facility using the LEDI III software application must develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan must identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

### Users Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users build orders, create shipping manifests, close/ship shipping manifest, and verify/ release and modify results into VistA for VA facilities and CHCS for DoD laboratories via LDSI. Patches LA\*5.2\*64 and LR\*5.2\*286 provide enhancements to the already existing laboratory software functionality for data entry and retrieval between the VA and DoD.

### ### Instrument Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III is an enhancement to Laboratory V. 5.2 and does not specifically involve instrument interfacing. All electronic communication is via established HL7 procedures for transmitting messages. The VistA Laboratory HL7 Interface Standards have been enhanced to accommodate expanded messaging capability.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures utilized in the VistA LEDI III software application.

### ### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently there are no menu/options being exported with this software release that would be of particular interest to the Information Security Officers (ISOs).

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI III software does not utilize security keys other than the general Laboratory security keys to control menu access within the Laboratory V. 5.2 package.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III changes and enhancements did not modify any existing file security schemes. New files exported by the patch installation have no file security applied. However, VA FileMan security access Ll code is recommended if file security is deemed necessary by the facilities. It is strongly recommended that Kernel’s File Access security be utilized to provide file security.

#### LAB DATA (#63), sub file \#63.04 CHEM, HEM, TOX, RIA, SER, etc. data storage

This following data is stored in non-FileMan compatible format on each test’s node in File \#63.04 sub file with each test result.

#### Sub file \#63.04 CHEM, HEM, TOX, RIA, SER, etc. data storage

Data map for CH subscripts (63.04)

^LR(70,"CH",6999895.824397,5)=164^\*H^84295.0000!84295.0000!2947!3103!A^104^72!135!145!120!150!!meq/L!!!144^^^^170^Instrument ID

|                           |                                 |                                 |
|---------------------------|---------------------------------|---------------------------------|
| Data Element position | Data Description            | Data                        |
| 1                         | Test Result                     | 164                             |
| 2                         | Normal Range flag               | \*H                             |
| 3                         | Test Coding                     | 84295.0000!84295.0000!2947!3103 |
| 3a                        | NLT code of  ordered test       | 84295.0000                      |
| 3b                        | NLT code of reported test       | 84295.0000                      |
| 3c                        | LOINC code of reported test     | 2947                            |
| 3d                        | Method Suffix of reported test  | 3103                            |
| 3e                        | Historically Mapped             | A                               |
| 4                         | Verifier DUZ                    | 104                             |
| 5                         | Normal Ranges                   | 72!135!145!120!150!!meq/L!!!144 |
| 5a                        | SITE/SPECIMEN Pointer to LAB(61 | 72                              |
| 5b                        | REFERENCE LOW                   | 135                             |
| 5c                        | REFERENCE HIGH                  | 145                             |
| 5d                        | CRITICAL LOW                    | 120                             |
| 5e                        | CRITICAL HIGH                   | 150                             |

#### Sub file \#63.04 CHEM, HEM, TOX, RIA, SER, etc. data storage *(continued)*

Data map for CH subscripts (63.04)

^LR(70,"CH",6999895.824397,5)=164^\*H^84295.0000!84295.0000!2947!3103!A^104^72!135!145!120!150!!meq/L!!!144^^^^170^Instrument ID

|                           |                                                          |               |
|---------------------------|----------------------------------------------------------|---------------|
| Data Element position | Data Description                                     | Data      |
| 5f                        | UNITS                                                    | meq/L         |
| 5g                        | TYPE OF DELTA CHECK                                      | Null          |
| 5h                        | DELTA VALUE                                              | Null          |
| 5i                        | DEFAULT VALUE                                            | 144           |
| 5j                        | THERAPEUTIC LOW                                          | Null          |
| 5k                        | THERAPEUTIC HIGH                                         | Null          |
| 6                         | Empty                                                    | Null          |
| 7                         | Empty                                                    | Null          |
| 8                         | Empty                                                    | Null          |
| 9                         | Verifying Institution (Pointer to INSTITUTION file (#4)) | 170           |
| 10                        | HL7 Equipment Entity Identifier –EEI                     | Instrument ID |

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following references may be helpful when installing and implementing the LEDI III software application:
- Kernel Systems Manual V. 8.0
- Kernel Toolkit V. 7.3
- Laboratory Universal Interface Patch LA\*5.2\*17-Patch LR\*5.2\*65 V. 1.0
- VA FileMan V. 21.0
- VA MailMan V. 7.1
- VistA Health Level Seven Site Manager & Developer Manual Version 1.6\*56
- VistA Laboratory Health Level Seven (HL7) Interface Standard Specifications V. 1.2
- Health Level Seven Standard Version 2.3.1 © 1997 by the Health Level Seven, Inc.
- Health Level Seven Standard Version 2.2 © 1994 by the Health Level Seven, Inc.

### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no official policies unique to the LEDI III software modification and distribution of the product.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-installation instructions establishes specific requirements that must be accomplished before installing the VistA LEDI III patches LA\*5.2\*64 and LR\* 5.2\*286.

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

## Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that VistA LEDI III software be installed into a test account before installing into a live production account. The test and production accounts must include all required software versions and patches to ensure a successful test installation of the LEDI III patches LA\*5.2\*64/LR\*5.2\*286.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resource Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for installing patches LA\*5.2\*64/LR\*5.2\*286, establishing mail groups, and menu assignments.

### IRM and LIM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Collection and HOST facilities IRM and LIM staff must coordinate the implementation of the LEDI III setup after the patches are installed. The LEDI III setup process must be performed in the sequence specified in the VistA LEDI III Implementation and User Guide.

## ### Intended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users of this software enhancement project include VA medical center laboratory personnel and DoD facility laboratory personnel.

### Users Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users will build orders, create shipping manifests, close/ship shipping manifest, and verify/ release and modify results into VistA for VA facilities and Composite Health Care System (CHCS) for DoD laboratories via LEDI III LDSI. Patches LA\*5.2\*64 and LR\*5.2\*286 provide enhancements to the existing laboratory software functionality for data entry and retrieval between the VA and DoD facilities.

## Communications Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DoD interface directly connects to an existing DoD-VA gateway at the AAC, and from that point will be processed like any other VistA laboratory request from a remote VA facility. On the VA side, the communication is transmitted through the Vitria Interface Engine (Austin) to the Austin firewall to Austin VPN to the DISA VPN to the DoD network. Transmission from DoD is basically the opposite of what has been described for the VA.

## Hardware Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA LEDI III software application operates on the current VA computer hardware systems.

## ## Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Connectivity will have to be established between the VA and DoD facilities.

VistA exchange data using HL7 messages are transmitted when triggering events occur.

Computer connectivity between CHCS and VistA is over transient TCP/IP connection. Two TCP sockets on each system provide communications between the two systems. Within the context of each TCP/IP socket, VistA and multiple CHCS sites may connect as a client or a server. Lower-level connectivity is provided via HL7 Minimal Lower Layer Protocol.

A Virtual Private Network (VPN) is established on an isolated tunnel from the VA national gateway to DoD medical treatment facilities. The outbound communication is from the Collecting Laboratory as an order requests to the Host Site for testing and results sent from Host Site returning to the Collecting Laboratory. Inbound traffic will contain Host Laboratory receiving orders and the Collecting Laboratory accepting results.

HL7 messages are generated from VA sites, transported securely over the VA-DoD VPN, and then routed to DoD medical centers where LSDI on the existing CHCS system will process the message.

The service is to provide an inbound access method that is a system-to-system connection, not a user to system connection. A hardware server-to-server VPN will be used to connect the VA WAN to the DoD WAN.

The need for this connection is to enable connectivity for the current network architecture under each agency’s existing network umbrella, utilizing existing firewalls, gateways, and other security measures. Interfaces and protocols will be developed to electronically communicate transactions between DoD and VA testing facilities.

The file size transferred daily would be approximately 14.2 MB, but also dependent upon the type of laboratory tests requested. The data will be transmitted as needed and not associated with a scheduled time.

This software release uses the existing VPN Service Unit (VSU) 5000 to create a virtual private network at the Austin Automation Center (AAC) national gateway. The VSU 5000 is a commercial product that enables organizations to securely connect remote users in a cost effective manner. The DoD will use the VSU 5000s to provide the isolated tunnel that connects the source and destination points for the laboratory data. For VA, the desired destination point is the AAC.

## LEDI III Equipment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To realize the maximum benefit of the VistA LEDI III software functionality, barcode printers, barcode accession labels, and scanners are required for accessioning patient’s specimen. The manual accessioning method is intended as a backup procedure for accessioning patient’s specimen.

> **NOTE:** Using the manual accessioning method will result in significant risk of transcription errors and increased accessioning time.

## ### Collection Facility Equipment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Laser quality printer - capable of supporting Hewlett Packard PC Language Version 3 or higher for printing Code 128 symbology Shipping Manifest bar code.

2\. Accession label bar code printer - capable of multiple formats, multi-font, 360-degree print orientation, supporting Code 39, Code 128, and PDF417.

### HOST Facility Equipment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Bar code laser scanner gun, 1D/2D, auto discriminating, Raster scanning scan element, immune to fluorescent lighting. Auto-Decodes following symbologies: Code 39, Code 39 full ASCII, Code 128, PDF417, and 1 and 2 dimensional bar code.

> **NOTE:** Bar code laser scanner guns are recommended because future development will provide two-dimensional bar codes shipping manifest. Experience has been much more favorable with scanner guns compared to wands or pens.

2\. Hands-free stand for laser guns.

3\. Appropriate power supply for scanner gun.

## Performance Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under normal working conditions, 95% of the results shall reach the collection site in less than 3 seconds after it is released from the host site. All released results and error messages shall return a clearly identifiable view alert upon receipt of results at the collection site. Laboratory administrators shall enforce policies governing the set times and numbers of times within 24 hours that results will be released into the computer system by authorized personnel in their laboratories.

## LEDI III Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation of a HL7 messaging interface between the VA VistA Laboratory package and a non-VA information system consists basically of three parts:

1.  VistA Laboratory LEDI III software
2.  Certified communication software and hardware
3.  Non-VA information system capable of sending and receiving Laboratory HL7 order and result messages

All three requirements must be functional to utilize the capabilities of the LEDI III software.

> **NOTE:** Implementation, setup, and configuration of vendor provided hardware and software is NOT addressed by this documentation. Consult the Vendor.

## Memory Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No memory constraints are associated with the release of the LEDI III software.

## ## ## Disk Space Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The required disk space is difficult to predict because the amount of disk space depends on what extent the new features are used. Due to the new requirement to journal the ^LAHM global, there will be an immediate increase in journal disk space. If none of the LEDI messaging features are implemented a 5-15% increase in disk space can be expected in the ^LR and ^LRO globals. If VA MailMan is used as the HL7 messaging protocol the ^XMB global will experience increased growth. Depending on the LEDI messaging activity and the number of trading partners, one could expect 20-40% disk space increase overall.

## Performance/Capacity Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performance estimates and capacity measures are difficult to obtain because LEDI III software has components in several applications. It is estimated that LAB SERVICE and AUTOMATED LAB INSTRUMENTS applications may impact the system by requiring 5-12% more Central Processing Unit (CPU) cycles.

## ## Kernel Installation and Distribution System (KIDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III software distribution is using KIDS.

> **NOTE:** For further instructions on using KIDS please refer to the Kernel V. 8.0 Systems Manual.

## Health Level Seven (HL7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI III is using the VistA HL7 V. 1.6 software to transport data. The software will send lab orders (ORM), order acknowledgment (ORR), and lab results (ORU) messages via VA MailMan or TCP/IP.

## ## ^VASITE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^VASITE routine call is used to determine the COLLECTION facilities Institution Number. This information is needed and used to establish clear and concise linking of entries in the following files:

1.  HL APPLICATION PARAMETER file (#771)
2.  HL LOGICAL LINK file (#870)
3.  AUTO INSTRUMENT file (#62.4)
4.  LA7 MESSAGE PARAMETER file (#62.48), (i.e., both COLLECTION and HOST facilities laboratory databases).

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI III patches are using the following namespaces:

- Patch LA\*5.2\*64 is using the LA namespace
- Patch LR\*5.2\*286 is using the LR namespace

## Nightly Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option must be scheduled to run on a daily basis. This option is used to purge the data in the LA7 MESSAGE QUEUE file (#62.49), LAB SHIPPING MANIFEST file (#62.8), LAB SHIPPINT EVENT file (#62.85), and LAB PENDING ORDERS ENTRY file (#69.6).

## Data Base Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new DBIAs were required for the release of the LEDI III product.

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

A new error bulletin \#47 has been added to LA7 MESSAGE LOG BULLETINS file (#62.485). When processing LEDI orders if any of the following are incomplete - local test, local urgency, local topography or local collection sample then the bulletin will be triggered. This is to insure that orders sent by the collecting facility are not missed when processed during LEDI Referral Patient Accessioning. If this bulletin is triggered it indicates that the host site's shipping configuration is not properly configured to process orders from it's collecting site.

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

This new SPECIMEN CODING SYSTEM field (#62.8,.06) allows VistA to function with DoD CHCS system which does not use HL7 standard table 0070. When orders are sent to a non-VA facility and the facility can not receive HL7 specimen codes from HL7 table 0070 then answer with the type of coding system "LOCAL".

#### SPECIMEN CODING SYSTEM field (#62.8,.060;6)

This new SPECIMEN CODING SYSTEM field (#62.8,.060;6) is used if orders are sent to a non-VA facility and the facility can not receive HL7 specimen codes from HL7 table 0070 then answer with the type of coding system "LOCAL".

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

This existing HL PID-4 field (#69.6,700.04) stores the placer's patient identification information from PID-4 for transmittal back to the placer when the order is completed. This field was modified to increase the field length 1-250 characters. This is a free text field.

## LEDI III New and Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three new options were created to accommodate LEDI III new functionality:

#### Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option

The new Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\] option is used to enter relevant clinical information that should accompany a test order on a manifest. This new option is located on the Lab Shipping Menu \[LA7S MAIN MENU\], located on the Laboratory DHCP Menu \[LRMENU\].

#### Start a Shipping Manifest \[LA7S MANIFEST START\] option

The new Start a Shipping Manifest \[LA7S MANIFEST START\] option will allow a manifest to be started without performing a manifest build. Specimens can then be added manually, instead of automatically, using the existing Add/Remove a Shipping Manifest Test \[LA7S MANIFEST TEST ADD/REMOVE\] option. This new option is located on the Lab Shipping Menu \[LA7S MAIN MENU\], which is located on the Laboratory DHCP Menu \[LRMENU\].

#### General Lab User Parameters \[LR USER PARAM\] option

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

#### Referral Patient Multi-purpose Accession \[LRLEDI\] option

The Referral Patient Multi-purpose Accession \[LRLEDI\] option contains the following three modifications:

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

## ## VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 0%" />
<col style="width: 48%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="package-name">Package Name</h4></td>
<td colspan="2"><strong>Versions</strong></td>
</tr>
<tr class="even">
<td>Health Level Seven (HL7)</td>
<td colspan="2">1.6 (with all patches installed)</td>
<td></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td colspan="2">8.0 (with all patches installed)</td>
<td></td>
</tr>
<tr class="even">
<td>Laboratory</td>
<td colspan="2">5.2 (with all patches installed)</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Information Management System (PIMS)</td>
<td colspan="2">5.3 (with all patches installed)</td>
<td></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td colspan="2">22.0 (with all patches installed)</td>
<td></td>
</tr>
<tr class="odd">
<td>VA MailMan</td>
<td colspan="2">7.1 (with all patches installed)</td>
<td></td>
</tr>
</tbody>
</table>

## VistA Patch Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the installation of the LEDI III patches LA\*5.2\*64/LR\*5.2\*286, the following patches must be installed:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package Name</strong></td>
<td><strong>Required Patches</strong></td>
</tr>
<tr class="even">
<td>Health Level Seven (HL7)</td>
<td><p>HL*1.6*101</p>
<p>HL*1.6*108</p></td>
</tr>
<tr class="odd">
<td>Kernel V. 8.0</td>
<td>XU*8.0*261</td>
</tr>
<tr class="even">
<td>Laboratory V. 5.2</td>
<td><p>LA*5.2*27</p>
<p>LA*5.2*46</p>
<p>LA*5.2*55</p>
<p>LA*5.2*61</p>
<p>LA*5.2*62</p>
<p>LA*5.2*63</p>
<p>LA*5.2*65</p>
<p>LA*5.2*70</p>
<p>LR*5.2*121</p>
<p>LR*5.2*153</p>
<p>LR*5.2*187</p>
<p>LR*5.2*201</p>
<p>LR*5.2*202</p>
<p>LR*5.2*220</p>
<p>LR*5.2*221</p>
<p>LR*5.2*222</p>
<p>LR*5.2*230</p>
<p>LR*5.2*232</p>
<p>LR*5.2*256</p>
<p>LR*5.2*261</p>
<p>LR*5.2*263</p>
<p>LR*5.2*269</p>
<p>LR*5.2*271</p>
<p>LR*5.2*282</p>
<p>LR*5.2*283</p>
<p>LR*5.2*285</p>
<p>LR*5.2*287</p>
<p>LR*5.2*312</p></td>
</tr>
</tbody>
</table>

## Patch LA\*5.2\*64 Routine Summary List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** List of preceding patches: LA\*5.2\*46, LA\*5.2\*61, LA\*5.2\*62, LA\*5.2\*63, LA\*5.2\*65. Sites should use CHECK^XTSUMBLD to verify checksums.

Example: LA\*5.2\*64 Checksums

ROUTINE SUMMARY  
===============  
  The following routines are included in this patch. The second line  
  of each of these routines now looks like:  
  \<tab\> ;;5.2;AUTOMATED LAB INSTRUMENTS;\<patchlist\>;Sep 27, 1994  
   
                    Checksum       Checksum  
   Routine Name     Before Patch   After Patch    Patch List  
   ------------     ------------   -----------    ------------  
   LA64             N/A            5936440        \*\*64\*\* (Deleted by KIDS)  
   LA7PURG          3834284        4599657        \*\*27,64\*\*  
   LA7SBCR1         4924406        5434157        \*\*27,46,64\*\*  
   LA7SBCR2         2564479        2593598        \*\*27,46,64\*\*  
   LA7SCE           11501726       13339015       \*\*27,46,61,64\*\*  
   LA7SM2           12143125       16026225       \*\*46,64\*\*  
   LA7SMB           14649107       12799432       \*\*27,46,64\*\*  
   LA7SMP           11746903       12373162       \*\*27,45,46,64\*\*  
   LA7SMP0          9303222        10961615       \*\*46,64\*\*  
   LA7SMPXL         3215234        4682314        \*\*27,42,46,64\*\*  
   LA7SMU           7104257        7255424        \*\*27,46,64\*\*  
   LA7SMU1          6300206        6311796        \*\*27,46,65,64\*\*  
   LA7SMU2          5290542        7549846        \*\*46,64\*\*  
   LA7SRR           6233015        7637904        \*\*46,64\*\*  
   LA7UTILA         10237097       10662046       \*\*23,27,46,64\*\*  
   LA7VHL           4568355        5811383        \*\*27,46,62,64\*\*  
   LA7VHLU          4487468        5914870        \*\*46,62,64\*\*  
   LA7VHLU1         2323481        3267492        \*\*46,61,64\*\*  
   LA7VHLU2         4100825        4356637        \*\*46,61,64\*\*  
   LA7VHLU3         2007360        2799232        \*\*46,64\*\*  
   LA7VHLU4         5424804        4836094        \*\*46,64\*\*  
   LA7VHLU5         5541950        7828952        \*\*46,64\*\*  
   LA7VIN1          5261630        5855016        \*\*46,64\*\*  
   LA7VIN1A         N/A            13987419       \*\*64\*\*  
   LA7VIN2          5808892        8339412        \*\*46,64\*\*  
   LA7VIN3          2061956        3081309        \*\*46,64\*\*  
   LA7VIN4          7936019        12162627       \*\*46,64\*\*  
   LA7VIN5          5205707        10570600       \*\*46,64\*\*  
   LA7VIN5A         5039195        8695039        \*\*46,64\*\*Example: LA\*5.2\*64 Checksums *continued*

   LA7VLL           5170411        6390054        \*\*27,51,55,64\*\*  
   LA7VMSG          3253314        5080421        \*\*27,50,56,46,64\*\*  
   LA7VMSG1         8227296        8679432        \*\*56,46,61,64\*\*  
   LA7VOBR          2129056        2455598        \*\*46,64\*\*  
   LA7VOBRA         5326634        8044290        \*\*46,64\*\*  
   LA7VOBX          2088674        2633711        \*\*46,64\*\*  
   LA7VOBX1         4057776        4535705        \*\*46,61,63,64\*\*  
   LA7VOBX2         4350324        4309250        \*\*46,64\*\*  
   LA7VOBX3         5240738        6460347        \*\*46,64\*\*  
   LA7VOBXA         6416931        6372995        \*\*46,70,64\*\*  
   LA7VORC          1565653        1713732        \*\*46,64\*\*  
   LA7VORM          6471896        12116142       \*\*27,42,46,64\*\*  
   LA7VORM1         7594289        9199759        \*\*27,51,46,61,64\*\*  
   LA7VORM3         6787219        7257153        \*\*46,64\*\*  
   LA7VORU          6241961        8366274        \*\*27,46,61,64\*\*  
   LA7VORU1         4734718        4842743        \*\*46,64\*\*  
   LA7VORU2         1962290        2531397        \*\*46,64\*\*  
   LA7VORUA         2199285        2385822        \*\*61,64\*\*  
   LA7VPID          4123683        4823699        \*\*46,64\*\*  
   LA7VSET          15979413       14514051       \*\*27,51,55,46,64\*\*  
   LA7VSET1         9065449        7835525        \*\*27,51,55,46,64\*\*  
   LA7VSTP          6079680        4597827        \*\*27,44,51,46,64\*\*  
   LA7VSTP1         3317926        3042573        \*\*27,46,64\*\*  
   LAGEN            8522786        8715369        \*\*1,17,22,27,47,46,64\*\*  
   
 List of preceding patches: 46, 61, 62, 63, 65, 70  
 Sites should use CHECK^XTSUMBLD to verify checksums.

## Patch LR\*5.2\*286 Routine Summary List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** List of preceding patches: LR\*5.2\*187, LR\*5.2\*202, LR\*5.2\*220, LR\*5.2\*222, LR\*5.2\*230, LR\*5.2\*232, LR\*5.2\*256, LR\*5.2\*261, LR\*5.2\*269, LR\*5.2\*271, LR\*5.2\*282, LR\*5.2\*283, LR\*5.2\*285, LR\*5.2\*287, and LR\*5.2\*312. Sites should use CHECK^XTSUMBLD to verify checksums.

Example: LR\*5.2\*286

ROUTINE SUMMARY  
===============  
  The following routines are included in this patch.  The second line  
  of each of these routines now looks like:  
  \<tab\> ;;5.2;LAB SERVICE;\<patchlist\>;Sep 27, 1994  
   
                    Checksum       Checksum  
   Routine Name     Before Patch   After Patch    Patch List  
   ------------     ------------   -----------    ------------  
   LR286            N/A            5465218        \*\*286\*\* (Deleted by KIDS)  
   LR7OB63          9973912        9132350        \*\*121,187,286\*\*  
   LR7OGM           8016197        8279122        \*\*187,220,312,286\*\*  
   LR7OGMC          5100174        5463477        \*\*187,230,312,286\*\*  
   LR7OGMG          3593445        3973477        \*\*187,230,286\*\*  
   LR7OGMP          5548341        6065382        \*\*187,246,282,286\*\*  
   LR7OR2           9125008        8919494        \*\*121,187,219,285,286\*\*  
   LR7OSUM1         12883059       12868699       \*\*121,187,256,286\*\*  
   LR7OSUM6         7911216        5450631        \*\*121,201,187,286\*\*  
   LRAFUNC          5202410        5809534        \*\*286\*\*  
   LRDIDLE0         5463932        6544739        \*\*140,171,153,286\*\*  
   LRDPAREF         5111405        7469302        \*\*153,222,286\*\*  
   LRDPAREX         7190033        6456580        \*\*153,286\*\*  
   LREVENT          3678954        2907416        \*\*153,286\*\*  
   LRFAST           19691126       18799737       \*\*100,121,201,286\*\*  
   LRFASTS          6423167        6524547        \*\*30,95,121,271,286\*\*  
   LRGP1            3988622        4165501        \*\*112,269,286\*\*  
   LROE             14550901       11534796       \*\*100,121,201,221,263,286\*\*  
   LRORD            12009917       12806626       \*\*100,121,153,286\*\*  
   LRORD1           9848796        9190513        \*\*1,8,121,153,201,286\*\*  
   LRORDB           3782224        7231598        \*\*153,222,286\*\*  
   LROW3            7497722        6459972        \*\*33,121,286\*\*  
   LRRP             11838355       9427993        \*\*195,221,283,286\*\*  
   LRRP1            8015031        6556852        \*\*153,221,283,286\*\*  
   LRRPU            N/A            3220194        \*\*286\*\*  
   LRSTUF1          13209134       11668378       \*\*153,286\*\*  
   LRVER            17228890       15441873       \*\*153,286\*\*Example: LR\*5.2\*286 *continued*

   LRVER1           8587449        7330679        \*\*42,153,201,215,239,240,  
                                                  263,232,286\*\*  
   LRVER3           14311842       13055299       \*\*42,100,121,140,171,153,  
                                                  221,286\*\*  
   LRVER4           19639169       14489554       \*\*14,42,112,121,140,171,  
                                                  153,188,279,283,286\*\*  
   LRVER5           14564045       14854455       \*\*42,153,283,286\*\*  
   LRVERA           690805         5764794        \*\*153,271,286\*\*  
   LRVR             13316120       11130012       \*\*42,153,263,286\*\*  
   LRVR1            11269859       11667912       \*\*42,153,221,286\*\*  
   LRVR3            10486080       11176919       \*\*42,121,153,286\*\*  
   LRVR4            8885642        9645653        \*\*14,42,121,153,221,263,  
                                                  279,283,287,286\*\*  
   LRVR5            11950773       4666781        \*\*1,42,153,263,283,286\*\*  
   LRWLST1          18457202       12664045       \*\*48,65,121,153,261,286\*\*  
   LRWLST11         21393713       16883055       \*\*121,128,153,202,286\*\*  
   
 List of preceding patches: 187, 202, 222, 230, 232, 256, 261, 269, 271  
 282, 283, 285, 287, 312  
 Sites should use CHECK^XTSUMBLD to verify checksums.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NOTES:

Kernel, MailMan, and HL patches must be current on the target system to avoid problems loading and/or installing this patch.

Patch installation must to be coordinated with the Laboratory Information Manager (LIM/ADPAC).

LIM/ADPAC must perform the LEDI III Implementation process as stated in the VistA LEDI III Implementation and User Guide.

Installation Time

The install time for this patch is less than 5 minute. This patch can be installed when Laboratory users are on the system. However these users should not be using any of the Laboratory's package accessioning or verifying options.

### Suggested Time to Install Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-peak hours.

1\. Obtain the file LAB_LEDI_III.KID from one of the following directories:

| OI FIELD OFFICE                    | FTP ADDRESS                    | DIRECTORY                      |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2\. If any routines are mapped, disable mapping.

3\. On the 'Kernel Installation & Distribution System' Menu (KIDS), select the 'Installation' menu.

4\. Use Load a Distribution using LAB_LEDI_III.KID when prompted to Enter a Host File name. You may need to prepend a directory name.

> If given the option to run any Environment Check Routine(s), answer

> "YES".

5\. From the Installation menu, you may then elect to use the following options (when prompted for the INSTALL NAME, enter LA\*5.2\*64):

> a\. Print Transport Global

> b\. Backup a Transport Global

> c\. Compare Transport Global to Current System

> d\. Verify Checksums in Transport Global

> Use the 'Verify Checksum in Transport Global' option and verify that all routines have the correct checksums.

6\. Perform the following steps if applicable:

> All Lab LEDI (LA7V\*) related HL v1.6 LLPs should be shutdown.

> Use the HL menu option Start/Stop Links \[HL START\] to shutdown these LLPs if they are running.

7\. Use the 'Install Package(s)' option under the 'Installation' menu and select the package 'LA\*5.2\*64'.

> When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES// choose 'NO'.

> When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//' choose 'NO' unless site has additional local laboratory accessioning and verifying options that should be disabled during install.

> The install will automatically disable the following options:

> Accession order then immediately enter data LR ACC THEN DATA

> Accessioning tests ordered by ward order entry LROE

> Accessioning, standard (Microbiology) LRMICROLOGIN

> Add tests to a given accession. LRADD TO ACC

> Add tests to an already existing order number. LRADD TO ORDER

> Batch data entry (chem, hem, tox, etc.) LRSTUF

> Bypass normal data entry LRFAST

> Delete entire order or individual tests LRCENDEL

> Delete test from an accession LRTSTOUT

> Edit atomic tests LRDIEATOMIC

> Enter/verify data (Load list) LRVRW2

> Enter/verify data (Work list) LRVRW

> Enter/verify data (auto instrument) LRVR

> Enter/verify/modify data (manual) LRENTER

> Fast Bypass Data Entry/Verify LRFASTS

> Fast lab test order (IMMEDIATE COLLECT) LROW IMMED COLLECT

> Fast lab test order (ROUTINE) LROW ROUTINE

> Fast lab test order (SEND PATIENT) LROW SEND PAT

> Fast lab test order (WARD COLLECT) LROW WARD COL

> Group data review (verified & EM) LRGVP

> Group verify (EA, EL, EW) LRGV

> Itemized routine lab collection LRPHITEM

> Lab add test(s) to an existing order LRADDTST

> Lab test order LROW

> Manually accession QC, Environmental, etc. LRQCLOG

> Merge Accessions LRACC MERGE

> Multipurpose accessioning LRQUICK

> Receipt of routine lab collection from wards LRPHEXCPT

> Referral Patient Multi-purpose Accession LRLEDI

> Remove an accession LRDELOG

> Special test accessioning LRNONCOM

8.  On a mapped system, rebuild your map set.

> **NOTE:** LA\*5.2\* 64 and LR\*5.2\*286 routines are deleted after a successful software installation.

### Example: LEDI III Installation Process:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: 6  Install Package(s)\<ENTER\>

Select INSTALL NAME: LA\*5.2\*64       Loaded from Distribution  <11/8/04@10:28:22>  
     =\> LA\*5.2\*64/LR\*5.2\*286  ;Created on Nov 08, <2004@11:43:25>  
   
This Distribution was loaded on Nov 08, <2004@10:28:22> with header of  
   LA\*5.2\*64/LR\*5.2\*286  ;Created on Nov 08, <2004@11:43:25>  
   It consisted of the following Install(s):  
      LA\*5.2\*64     LR\*5.2\*286  
Checking Install for Package LA\*5.2\*64  
Will first run the Environment Check Routine, LA64  
   
   
                        --- Environment Check is Ok ---  
   
Install Questions for LA\*5.2\*64  
   
Incoming Files:  
   
   
   62.4      AUTO INSTRUMENT  (Partial Definition)  
> **NOTE:** You already have the 'AUTO INSTRUMENT' File.  
   
   
   62.485    LA7 MESSAGE LOG BULLETINS  (including data)  
> **NOTE:** You already have the 'LA7 MESSAGE LOG BULLETINS' File.  
I will OVERWRITE your data with mine.  
   
   
   62.49     LA7 MESSAGE QUEUE  (Partial Definition)  
> **NOTE:** You already have the 'LA7 MESSAGE QUEUE' File.  
   
   
   62.8      LAB SHIPPING MANIFEST  (Partial Definition)  
> **NOTE:** You already have the 'LAB SHIPPING MANIFEST' File.  
   
   
   62.9      LAB SHIPPING CONFIGURATION  (Partial Definition)  
> **NOTE:** You already have the 'LAB SHIPPING CONFIGURATION' File.  
   
Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// n NO\<ENTER\>  
   
Checking Install for Package LR\*5.2\*286  
Will first run the Environment Check Routine, LR286

#### Example: LEDI III Installation Process *continued*

               Sending install started alert to mail group G.LMI  
   
                        --- Environment Check is Ok ---

Install Questions for LR\*5.2\*286  
   
Incoming Files: \<ENTER\>  
  
   60        LABORATORY TEST  (Partial Definition)  
> **NOTE:** You already have the 'LABORATORY TEST' File.  
   
   
   61        TOPOGRAPHY FIELD  (Partial Definition)  
> **NOTE:** You already have the 'TOPOGRAPHY FIELD' File.  
   
   
   68.2      LOAD/WORK LIST  (Partial Definition)  
> **NOTE:** You already have the 'LOAD/WORK LIST' File.  
   
   
   69.6      LAB PENDING ORDERS ENTRY  
> **NOTE:** You already have the 'LAB PENDING ORDERS ENTRY' File.  
   
Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// n NO\<ENTER\>

   
   
Want KIDS to INHIBIT LOGONs during the install? YES// n NO\<ENTER\>  
Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// n NO\<ENTER\>  
   
Enter the Device you want to print the Install messages.  
You can queue the install by enter a 'Q' at the device prompt.  
Enter a '^' to abort the install.  
   
DEVICE: HOME//   TELNET VIRTUAL  
   
   
 Install Started for LA\*5.2\*64 :  
               Nov 08, <2004@10:30:39>  
   
Build Distribution Date: Nov 08, 2004  
   
 Installing Routines:......................................................  
               Nov 08, <2004@10:30:40>

#### Example: LEDI III Installation Process *continued*

 Running Pre-Install Routine: PRE^LA64.  
   
               Sending install started alert to mail group G.LMI  
   
                          \*\*\* Pre install started \*\*\*  
   
                  --- No actions required for pre install ---  
   
                         \*\*\* Pre install completed \*\*\*  
   
 Installing Data Dictionaries: ......  
               Nov 08, <2004@10:30:40>  
   
 Installing Data:  
               Nov 08, <2004@10:30:40>  
   
 Installing PACKAGE COMPONENTS:  
   
 Installing BULLETIN.....  
   
 Installing OPTION.....  
               Nov 08, <2004@10:30:40>  
   
 Running Post-Install Routine: POST^LA64.  
   
                          \*\*\* Post install started \*\*\*  
   
    \*\*\* Starting reindexing of field \#.01 of LAB SHIPPING MANIFEST file \*\*\*  
..............................................  
   
    \*\*\* Completed reindexing of field \#.01 of LAB SHIPPING MANIFEST file \*\*\*  
   
   \*\*\* Set INTERFACE TYPE for LA7V\* entries in LA7 MESSAGE PARAMETER file \*\*\*  
   
                         \*\*\* Post install completed \*\*\*  
   
              Sending install completion alert to mail group G.LMI  
   
 Updating Routine file......  
   
 Updating KIDS files.......  
   
 LA\*5.2\*64 Installed.  
               Nov 08, <2004@10:30:44>  
   
 Install Message sent \#19304  
 

#### Example: LEDI III Installation Process *continued*

 Install Started for LR\*5.2\*286 :  
               Nov 08, <2004@10:30:44>  
   
Build Distribution Date: Nov 08, 2004  
   
 Installing Routines:........................................  
               Nov 08, <2004@10:30:45>  
   
 Running Pre-Install Routine: PRE^LR286.  
   
                          \*\*\* Pre install started \*\*\*  
   
   \*\*\* Deleting Data Dictionary for LAB PENDING ORDERS ENTRY file (#69.6) \*\*\*  
   
                 \*\*\* Will be reinstalled by this KIDS build \*\*\*  
   
                         \*\*\* Pre install completed \*\*\*  
   
 Installing Data Dictionaries: .....  
               Nov 08, <2004@10:30:45>  
   
 Installing PACKAGE COMPONENTS:  
   
 Installing INPUT TEMPLATE...  
   
 Installing OPTION..................................  
   
 Installing PARAMETER DEFINITION..  
   
 Installing PARAMETER TEMPLATE..  
               Nov 08, <2004@10:30:45>  
   
 Running Post-Install Routine: POST^LR286.  
   
                          \*\*\* Post install started \*\*\*  
   
    \*\*\* Tasking reindexing of field \#18 of LAB PENDING ORDERS ENTRY file \*\*\*  
   
                         \*\*\* Post install completed \*\*\*  
   
              Sending install completion alert to mail group G.LMI  
   
 Updating Routine file......  
   
 Updating KIDS files.......  
   
 LR\*5.2\*286 Installed.  
               Nov 08, <2004@10:30:46>  
   
 Install Message sent \#19305  
   
  
Select Installation Option: \<ENTER\>

# Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps must be performed after a successful installation of the LEDI III software:

## IRM Staff: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Start LLP \[HL START\] option to RESTART any LA7V\* HL v1.6 LLP’s shutdown performed by the LEDI III software installation process.

### Step 2:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Schedule the Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option to run daily via TaskMan (i.e., is a stand-alone option). The Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option must be scheduled to run on a daily basis. This option is used to purge the data in the LA7 MESSAGE QUEUE file (#62.49), LAB SHIPPING MANIFEST file (#62.8), LAB SHIPPINT EVENT file (#62.85), and LAB PENDING ORDERS ENTRY file (#69.6).

Example: How to schedule the Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option to run daily.

Edit Option Schedule Option Name: LA7TASK NIGHTY \<Enter\>

VARIABLE NAME: LA7FIX VALUE: 0\<Enter\>

VARIABLE NAME: LA7ION VALUE: "IRM DEVELOP LASER1"\<Enter\>

VARIABLE NAME: LA7LOG VALUE: 1\<Enter\>

If errors are found, an alert is sent to members of the “LAB MESSAGING” mail group notifying them that errors were detected. If logging of errors occurred then alert recipients will be able to print or view an error log from the alert system. Alternatively the error report can be printed using the Print Lab Messaging Integrity Check Report \[LA7 PRINT INTEGRITY CHECK\] option. The integrity report can also be run alone using Lab Messaging File Integrity Checker \[LA7 CHECK FILES\] option.

### Step 3:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option is also used to check the integrity of the LA7 MESSAGE QUEUE file (#62.49) and to purge messages. Before the LA7 MESSAGE QUEUE file (#62.49) is purged, an integrity check should be performed. The integrity check can be run using the following two switches:

Examples: How to check the integrity of LA7 MESSAGE QUEUE file (#62.49).

LA7FIX = 0 - do not fix errors

1 - do fix errors

LA7LOG = 0 - do not log errors in XTMP global.

1 - do log errors in XTMP global

LA7ION = name of device to print error report if set to log errors (LA7LOG=1)

Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option also purges the following LEDI related files:

- LAB SHIPPING MANIFEST (#62.8)
- LAB SHIPPING EVENT (#62.85)
- LAB PENDING ORDERS ENTRY (#69.6)

NOTES:

1\. Please see the VistA LEDI III Implementation and User Guide for instructions on how to setup the software. The LEDI III setup process must be performed in the sequence specified in the guide.

2\. The COLLECTION and HOST facilities IRM and LIM staff must coordinate the implementation of the LEDI III setup process after the patches are installed.