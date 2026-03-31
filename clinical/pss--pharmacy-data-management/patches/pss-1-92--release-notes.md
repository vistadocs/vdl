---
title: PSS*1*92 PSN*4*103 Patient Financial Services System (PFSS) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PSN*4*103 Patient Financial Services System (PFSS)
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*92
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - table
  - contents
  - service
  - drug
  - pfss
  - functionality
  - billing
  - patch
  - product
page_count: 0
word_count: 1129
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/psn_4_103_pss_1_92_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/psn_4_103_pss_1_92_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-92-psn-4-103-patient-financial-services-system-pfss-release-notes/001.png)

Patient Financial Services System (PFSS) 1B Pilot

National Drug File (NDF)

and

Pharmacy Data Management (PDM)

Release Notes

> PSN\*4\*103

> PSS\*1\*92

June 2006

VistA Health Systems Design & Development

Table of Contents

*(This page intentionally left blank for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Software Interfaces](#software-interfaces)
  - [Overview of New Functionality](#overview-of-new-functionality)
- [National Drug File Enhancements](#national-drug-file-enhancements)
  - [Files and Fields](#files-and-fields)
  - [New Routine](#new-routine)
- [Pharmacy Data Management Enhancements](#pharmacy-data-management-enhancements)
  - [Files and Fields](#files-and-fields-1)
  - [Changed Option](#changed-option)
  - [Other Functionality](#other-functionality)
These two patches are part of the Patient Financial Services System (PFSS) project. PFSS patches are being released on various schedules. Some patch functionality will not be active until a new PFSS switch is activated during final implementation. PFSS will initially be implemented at select pilot sites ONLY.
The purpose of the PFSS project is to prepare the Veterans Health Information Systems and Technology Architecture (VistA) environment for the implementation of a commercial off-the-shelf (COTS) billing replacement system. The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system. Significant changes to VistA legacy systems and ancillary packages are necessary.
Some of the PFSS software components are not operational until the PFSS On/Off Switch, distributed with patch IB\*2\*260, is set to “ON”. The ability for the local site to set the switch to “ON” will be provided at the appropriate time with the release of a subsequent Integrated Billing (IB) patch.
For more information about the PFSS project, review the documentation accompanying this patch and refer to the following website: <span class="mark">REDACTED</span>.
These release notes present a brief description of the new features and functions of the National Drug File (NDF) in Patch PSN\*4\*103 and Pharmacy Data Management (PDM) in Patch PSS\*1\*92.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OP will interface with the new COTS billing replacement system. These new interfaces are documented in the PFSS 1B Pilot [Admission/Discharge/Transfer (ADT) Software Requirements Specification (SRS)](http://tspr.vista.med.va.gov/warboard/ProjectDocs/PFSS_Cleveland_Pilot_1B/PFSS_SRS_ADT_Bed_Control_PTF.doc) and Charge Messaging Interface Control Document (ICD).

The following applications must be running to support the new PFSS functionality:

|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
| Kernel                                       | 8.0                        |
| VA FileMan                                   | 22.0                       |
| MailMan                                      | 8.0                        |
| National Drug File (NDF)                     | 4.0                        |
| Pharmacy Data Management (PDM)               | 1.0                        |
| Outpatient Pharmacy (OP)                     | 7.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP) | 2.0                        |
| Controlled Substances (CS)                   | 3.0                        |
| Health Level 7 (HL7)                         | 2.4                        |
| Computerized Patient Record System (CPRS)    | 26.0                       |
| Integrated Billing (IB)                      | 2.0                        |
| VistA Data Extraction Framework (VDEF)       | 1.0                        |

> NOTE: The Clinical Indicator Data Capture (CIDC) patches PSO\*7\*143 and IB \*2\*260 are required and must be installed and operational.

Patches PSS\*1\*92 and PSN\*4\*103 provide the new Charge Description Master (CDM) functionality to patch PSO\*7\*201 once the PFSS switch is active. The CDM provides Service Codes for each drug, supply item, etc., to uniquely identify them to the new COTS billing system.

## Overview of New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality for National Drug File, Patch PSN\*4\*103, establishes a Service Code—a six-digit field that will be established/approved by a central Change Control Board (CCB)— for each entry in the VA PRODUCT file (#50.68).

Pharmacy Data Management, Patch PSS\*1\*92, is modified to allow the user to enter a Service Code in the DRUG file (#50).

The following described changes are implemented only when the PFSS Switch is set to ON, unless specifically noted otherwise.

# National Drug File Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation of the COTS billing system requires the VA Product file/Drug file to link a Service Code to every Pharmacy prescription fill. The concept of a Charge Description Master (CDM) is the method taken to accomplish this task.

The CDM is an industry-standard financial tool common to all commercial billing systems and used in virtually every private hospital. It is a comprehensive listing of all services performed, drugs supplied, or supplies provided in a particular hospital, along with the value of those services/drugs/items, or charge amounts. Each of these entries is represented by a Charge Code, and the Charge Code is made up of a Department Code and Service Code. Pharmacy’s assigned Department Code is 160.

The Service Code is a six-digit field that will be established/approved by a central CDM Change Control Board (CCB).

National Drug File (NDF) is modified to create and populate a Service Code (in the 600001–699999 range) for each entry in the VA PRODUCT file (#50.68). Initially, the Service Code will be populated by this NDF patch. Subsequently, the CDM CCB assigned Service Codes will be distributed as data update patches within the NDF releases.

> **NOTE:** For drugs that are not associated with an entry in the VA Product file, the user must enter the CCB-approved Service Code. (*See* Pharmacy Data Management Enhancements.)

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains updated files and fields in the NDF package.

#### VA PRODUCT file (#50.68) Update

#### New Field

SERVICE CODE field (#2000)

## New Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Post-install routine initially populates the new SERVICE CODE field (#2000) for every entry in the VA PRODUCT file (#50.68) with a six-digit number within the range of 600001–699999. The number is created by taking the Internal Entry number (IEN), padding it with zeroes as needed, and adding a “6” on the front to make up a six-digit number. This routine will be deleted upon completion of this task.

# Pharmacy Data Management Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pharmacy Data Management (PDM) is modified to allow the user to enter a Service Code in the DRUG file (#50).

If a drug is associated to an entry in the VA PRODUCT file of the NDF package, the Service Code will be derived from the VA PRODUCT entry the DRUG file is linked to. If a drug is not associated to an entry in the VA PRODUCT file, the user should enter the approved Service Code in the new SERVICE CODE field of the DRUG file.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains updated files and fields in the PDM package.

#### DRUG file (#50) Update

#### New Field

SERVICE CODE field (#400)

## Changed Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSSCOMMON input template portion of the *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option is modified to allow entry of the new SERVICE CODE field.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The encapsulation API DATA^PSS50 is modified to return the new SERVICE CODE field (#400). The new PFSS functionality uses this API to retrieve the Service Code as well as other drug-related information needed for billing.

If the Service Code exists in the VA PRODUCT file (#50.68), it will be used. Otherwise, the Service Code defined in the DRUG file (#50) will be sent to the COTS billing system. For drugs that are not associated with an entry in the VA PRODUCT file (#50.68) and do not have a Service Code defined in the DRUG file (#50), a default value of 600000 will be passed in the charge message to the COTS billing system.