---
title: AMPL Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: AMPL
app_code: PREA
app_name: "Pharmacy: Advanced Medication Platform"
section: CLI
app_status: archive
pkg_ns: PREA
patch_ver: 1.13
patch_id: PREA*1.13
group_key: "PREA:PREA:1.13"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - ampl
  - release
  - applicable
  - software
  - requirements
  - security
  - access
  - options
page_count: 0
word_count: 1604
section_count: 21
table_count: 3
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_13_AMPL_GUI_TM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_13_AMPL_GUI_TM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=398"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Advanced Medication Platform (AMPL)  
  Graphical User Interface (GUI)

  Technical Manual
---

![](ampl-technical-manual/001.png)

August 2025

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date    | Revision | Description                                                                     | Author        |
|---------|----------|---------------------------------------------------------------------------------|---------------|
| 08/2025 | 1.13     | [Section 1.2](#system-overview). Added Pharmacogenomics to the list of domains. | AMPL GUI Team |
| 07/2025 | 1.12     | No Update                                                                       | AMPL GUI Team |
| 04/2024 | 1.11     | Updated dates, updated revision number to match builds                          | AMPL GUI Team |
| 06/2024 | 1.2      | No Update                                                                       | AMPL GUI Team |
| 02/2024 | 1.1      | Content Update                                                                  | AMPL GUI Team |
| 08/2023 | 1.0      | Document Baseline                                                               | AMPL GUI Team |

Table 1: Minimum Version of Software Packages

Table of Contents

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
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [Stand-Alone Options](#stand-alone-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
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
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix A: Post-Implementation Access or Removal Requests](#appendix-a-post-implementation-access-or-removal-requests)
The Advanced Medication Platform (AMPL) Graphic User Interface (GUI) is a front-end  
application supporting the Department of Veterans Affairs (VA) pharmacists by fulfilling the need for clinical decision support during patient care. Access to relevant medical knowledge can lead to increased quality of care, better efficiency, and improved health results. It can also decrease the potential for errors and adverse events resulting in decreased cost and increased provider and patient satisfaction. Incorporating GUI capabilities into the processing of pharmacy medication orders is a way to minimize risks and enhance healthcare.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual will document the Veterans Health Information Systems and Technology Architecture (VistA) components released in support of the AMPL GUI.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI is a GUI application tailored to users of the VistA Pharmacy packages. The AMPL GUI provides pharmacists with a single point of access to patients’ medical data from all VA medical centers in a clearer and more user-friendly display. The AMPL GUI intends to advance VA’s ongoing efforts to employ robust electronic health records and improve the efficiency and safety of the medication order process.

The AMPL GUI supports the current workflow as well as the development and incorporation of new technology/functionality and techniques. It will allow users to make more informed decisions using clinical knowledge and patient-specific information, intelligently filtered, organized and presented as care is being delivered.

The AMPL GUI displays data from the following domains:

- Allergy
- Appointments
- Consults
- Demographics
- Immunizations
- Lab
- Pharmacy
- Problem List
- Progress Notes
- Vitals
- Pharmacogenomics

  Figure 1 shows the data flow of an AMPL GUI user requesting allergy data from all VA facilities.

Figure 1: AMPL GUI Health Share Data Flow

![](ampl-technical-manual/002.png)

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience of this document is local Information Technology Support, Office of Information and Technology (OIT) personnel, and anyone who needs to know the VistA components that support the AMPL GUI.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All AMPL GUI documentation is available in the VistA documentation Library, located under the Advanced Medication Platform section.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VistA parameters in the AMPL GUI application.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no initial VistA software package release of the AMPL GUI. All updates to VistA components of the AMPL GUI will occur as patches using the Kernel Installation and Distribution (KIDS) system.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI package requires the minimum version, stated on the following external packages, to run effectively:

| Package              | Minimum Version Needed |
|--------------------------|----------------------------|
| Kernel                   | 8.0                        |
| VA FileMan               | 22.2                       |
| MailMan                  | 8.0                        |
| Master Patient Index     | 1.0                        |
| Virtual Patient Record   | 1.0                        |
| Outpatient Pharmacy      | 7.0                        |
| Inpatient Medications    | 5.0                        |
| Pharmacy Data Management | 1.0                        |

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are used by the Advanced Medication Platform application: PREAPO2, PREAPO3.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Stand-Alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information is a list of all stand-alone options that are NOT exported as part of any pharmacy menu:

AMPL GUI option

\[PREA AMPL GUI\]

The purpose of this option is to serve as the context option for the ADVANCED MEDICATION PLATFORM entry in the REMOTE APPLICATION (#8994.5) File.

AMPL GUI USER IDENTIFICATION

\[PREA AMPL GUI ACCESS\]

This option is run at the request of the Advanced Medication Platform (AMPL) GUI Implementation Manager. It identifies which users will get AMPL access based on Keys and Person Class, upon initial rollout of the AMPL GUI. This option will be disabled after the task is complete.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Software-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to AMPL GUI is granted by membership in an Active Directory (AD) group.

See Appendix A: Post-implementation Access or Removal Requests.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For problems or questions with the Advanced Medication Platform application, a ticket must be entered by contacting the Enterprise Service Desk.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                   |
|-------------|------------------------------------------------------------------|
| AD          | Active Directory                                                 |
| AMPL        | Advanced Medication Platform                                     |
| ePAS        | Electronic Permissions Access                                    |
| EUO         | End-User Operations                                              |
| GUI         | Graphical User Interface                                         |
| ICR         | Integration Control Registrations                                |
| ITOPS       | IT Operations and Services                                       |
| KIDS        | Kernel Installation and Distribution System                      |
| NARS        | Network Access Request                                           |
| OIT         | Office of Information and Technology                             |
| VDL         | Veterans Document Library                                        |
| VistA       | Veterans' Health Information Systems and Technology Architecture |

# Appendix A: Post-Implementation Access or Removal Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to AMPL GUI is granted by membership in an AD group. After initial implementation, a site may request access or removal of an individual by submitting a SNOW ticket by contacting the Enterprise Service Desk or by using the YourIT portal. The SNOW ticket must be assigned to the SPM.Health.PCS.Sub_1. AMPL Engineering group.