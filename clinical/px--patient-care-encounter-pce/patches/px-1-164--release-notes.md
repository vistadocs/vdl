---
title: PX*1*164 Visit Tracking Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Visit Tracking
app_code: PX
app_name: Patient Care Encounter (PCE)
section: CLI
app_status: active
pkg_ns: PX
patch_ver: 1
patch_id: PX*1*164
group_key: "PX:PX:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# # Introduction](#introduction) - [Patient Financial Services System](#patient-financial-services-system) - [Software Interfaces](#software-interfaces) - [Overview of New Functionality](#overview-of-new-functionality) - [Package Name Enhancements](#package-name-enhancements) - [Options and Actio
audience: 
keywords: 
  - table
  - contents
  - pfss
  - account
  - procedure
  - charge
  - files
  - visit
  - patient
  - package
page_count: 0
word_count: 1263
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2006
revision_count: 2
revision_newest: 01/06/06
revision_oldest: 10/20/05
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/px_1_p164_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/px_1_p164_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=82"
---

![](px-1-164-visit-tracking-release-notes/001.png)

PATIENT CARE ENCOUNTER  
(PCE)  
  
Release Notes  
PX\*1.0\*164

February 2006

V*IST*A Health System Design & Development

Revision History

|          |              |                                                                                                                          |                                    |
|----------|--------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date | Revision | Description                                                                                                          | Author                         |
| 10/20/05 | 0.1          | Added two modifications patch includes, removed PXCEPRV routine, and updated checksum values to reflect correct numbers. | <span class="mark">REDACTED</span> |
| 01/06/06 | 1.0          | Added new functionality, enhancements to the software                                                                    | <span class="mark">REDACTED</span> |

Table of Contents

# # # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # Introduction](#introduction)
  - [Patient Financial Services System](#patient-financial-services-system)
  - [Software Interfaces](#software-interfaces)
  - [Overview of New Functionality](#overview-of-new-functionality)
- [Package Name Enhancements](#package-name-enhancements)
  - [Options and Actions](#options-and-actions)
  - [Reports and Profiles](#reports-and-profiles)
  - [Files and Fields](#files-and-fields)
    - [New Files](#new-files)
    - [Changed Files](#changed-files)
  - [Other Functionality](#other-functionality)
    - [Charge Message SC/EI Classifications](#charge-message-scei-classifications)
    - [API Changes](#api-changes)

## Patient Financial Services System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Care Encounter (PCE) patch is part of the Patient Financial Services System (PFSS) project. PFSS patches are being released on various schedules. Some patch functionality will not be active until a new PFSS switch is activated during final implementation. PFSS will initially be implemented at select pilot sites ONLY.

The purpose of the PFSS project is to prepare the Veterans Health Information Systems and Technology Architecture (VistA) environment for the implementation of a commercial off-the-shelf (COTS) billing replacement system. The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system. Significant changes to VistA legacy systems and ancillary packages are necessary.

These PFSS software components are not operational until the PFSS On/Off Switch, distributed with patch IB\*2\*260, is set to "ON". The ability for the local site to set the switch to "ON" will be provided at the appropriate time with the release of a subsequent Integrated Billing (IB) patch. For more information about the PFSS project, review the documentation accompanying this patch and refer to the following website: <span class="mark">REDACTED</span>/.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCE processing assumes the following VistA packages are installed and fully patched:

Kernel V.8.0

VA FileMan V.22.0

MailMan V.8.0

CPT/HCPCS Codes V.6.0

DSS V.3.0

PCE V.1.0

ICD V.18

LEX V.2.0

IB V.2.0

PX\*1.0\*164 requires the prior installation of the following patches:

IB\*2\*286

SD\*5.3\*430

## Overview of New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE PFSS 1B project will add the following new functionality to the PCE Application:

- A new field, PFSS Account Reference, which is used by the external billing system to attach charges for 1<sup>st</sup> and 3<sup>rd</sup> party billing.
- PCE now determines if there is a PFSS Account Reference available either by being passed-in with a DATA2PCE API call, or by association with a scheduled appointment, or through association with an order.
- If no PFSS Account Reference is available, PCE will call the Integrated Billing subsystem (IBB) Get Account API to create a new PFSS Account Reference.
- A new field, Department Code, which defines the service area for a charge.
- A new field, PFSS Charge ID, which uniquely identifies each charge item in the external billing system.
- Changes to the DATA2PCE API and Visit Tracking to accommodate the new fields.
- A new filer routine used to file charges into the Integrated Billing subsystem (IBB) cache buffer*.*
- New dynamically created Charge Message SC/EI classifications for procedures that are auto-populated based on the procedure clinical indicators and are filed with the charge message into the IBB cache buffer.
- A new post-installation routine to activate the Order/Entry Result Reporting package in the Visit Tracking Parameters (#150.9) file.

# Package Name Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the PCE package are grouped and discussed in detail in the following sections.

## Options and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new additions or changes to any of the menu options in the PCE package.

## Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new reports or changes to the reports in the PCE package.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files and fields in the PCE package.

### New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new files added to the PCE package.

### Changed Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VISIT file (#9000010)

Field Number Field Name

.26 PFSS ACCOUNT REFERENCE

#### VCPT file (#9000010.18)

Field Number Field Name

.19 DEPARTMENT CODE

.2 PFSS CHARGE ID

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Charge Message SC/EI Classifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on the associated clinical indicators, the Charge Message SC/EI classifications will be auto-populated according to the following rules:

If the SC/EI for at least one ICD-9 is "Yes", then the Charge Message SC/EI will automatically be set to "Yes".

If the SC/EI for all ICD-9's is "No", then the Charge Message SC/EI will automatically be set to "No".

If at least one ICD-9 is missing an SC/EI and none of the other ICD-9's SC/EI is "Yes", use the Encounter Level SC/EI.

### API Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NAME: DBIA 1889-A (DATA2PCE)

#### ACCOUNT

Add a dotted variable to the calling parameters which represents the PFSS Account Reference.

\$\$DATA2PCE^PXAPI(INPUTROOT,PKG,SOURCE,.VISIT,USER,ERRDISP,.ERRARRAY,PPEDIT,.ERRPROB, .ACCOUNT) This is a function which will return a value identifying the status of the call. Data that is processed by PCE will be posted on the PXK VISIT DATA EVENT protocol.

Modified Parameter Description:

(Optional) A dotted variable name, where ACCOUNT is the PFSS Account Reference associated with the data being passed by the calling application. Each PFSS Account Reference represents an internal entry number in the PFSS ACCOUNT file (# 375).

#### PROCEDURE

Add a new DEPARTMENT subscript to the procedure level for the DATA2PCE API.

The "PROCEDURE" node may have multiple entries (i). Only active CPT/HCPCS codes will be accepted. The "PROCEDURE" node documents the procedure(s), the number of times the procedure was performed, the diagnosis the procedure is associated with and the narrative that describes the procedure. It also enables documentation of the provider who performed the procedure, the date/time the procedure was performed and any comments that are associated with the procedure. To delete the entire "PROCEDURE" entry, set the "DELETE" node to 1.

"PROCEDURE",i,"DEPARTMENT") A 3-digit code that defines the service area. Missing Department Codes will be assigned a Department Code. The Department Code will be the Stop Code associated (in the HOSPITAL LOCATION file, \#44) with the Hospital Location of the patient visit.

108::=Laboratory

160::=Pharmacy

419::=Anesthesiology

423::=Prosthetics

180::=Oral Surgery

401::=General Surgery

402::=Cardiac Surgery

401::=General Surgery

402::=Cardiac Surgery

403::=Otorhinolaryngology (ENT)

404::=Gynecology

406::=Neurosurgery

407::=Ophthalmology

409::=Orthopedics

410::=Plastic Surgery (inc. H&N)

411::=Podiatry

412::=Proctology

413::=Thoracic Surgery

415::=Peripheral Vascular

457::=Transplantation

105::=General Radiology

109::=Nuclear Medicine

109::=Cardiology Studies (Nuclear Med)

115::=Ultrasound

703::=Mammography

150::=CT Scan

151::=Magnetic Resonance Imaging

152::=Angio-Neuro-Interventional

421::=Vascular Lab

#### NAME: DBIA 1900-A

Visit Tracking is a utility that can be used by a variety of VISTA modules (usually via PCE), with potential benefits for clinical, administrative, and fiscal applications. Visit Tracking will allow VISTA packages to link an event to a patient visit entry, thereby linking that event to any number of events occurring throughout the hospital during the patient's outpatient and/or inpatient episode.

#### ^VSIT 

Field Number Variable Description

.26 VSIT("ACT") PFSS ACCOUNT REFERENCE (pointer

> PFSS ACCOUNT file \#375)