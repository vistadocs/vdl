---
title: OR*3.0*453 Provider Role Tool Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Provider Role Tool
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*453
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - provider
  - role
  - tool
  - order
  - software
  - requirements
  - security
  - manual
page_count: 0
word_count: 1927
section_count: 20
table_count: 3
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 2021
revision_count: 6
revision_newest: 07/28/2021
revision_oldest: 06/12/2020
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/prt_tm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/prt_tm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Hlk527034419" class="anchor"></span>

  Provider Role Tool (PRT)

  Technical Manual
---

![](or-3-0-453-provider-role-tool-technical-manual/001.png)

July 2021

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date   | Revision | Description                                                                                                                      | Author            |
|------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 07/28/2021 | 0.07         | OR\*3\*453: Redacted the manual for the VA Document Library (VDL). Removed names links to software builds.                           | CPRS Development Team |
| 07/16/2021 | 0.06         | OR\*3\*453: Updated the Remote Procedure Calls section.                                                                              | REDACTED              |
| 11/30/2020 | 0.05         | OR\*3\*453: Removed the embedded RACI because it is not required in the Technical Manual.                                            | REDACTED              |
| 07/30/2020 | 0.04         | OR\*3\*453: Fixed a typo in the 6/12/2020 Revision History. J. Crumley’s name was misspelled.                                        | REDACTED              |
| 06/26/2020 | 0.03         | OR\*3\*453: Removed the patch number from the title page, updated the RACI, fixed an error in section 1.3 (changed tier 2 to tier 3) | REDACTED              |
| 06/12/2020 | 0.02         | OR\*3\*453: Revised dates on title page and footers                                                                                  | REDACTED              |
| 07/2019    | 0.01         | OR\*3\*453: Initial Draft                                                                                                            | REDACTED              |

Artifact Rational

A Technical Manual is a required end-user document for all OI&T software releases. The intended audience for this document is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

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
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
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
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix A. Parameters](#appendix-a-parameters)
- [Parameter Definitions](#parameter-definitions)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Technical Manual is to familiarize users and support personnel with the features and internal workings of the Provider Role Tool (PRT).

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool application enables authorized users to reassign future alerts for *qualifying patient orders* from a current provider to one or more new providers. The goal of this is to handle the cases where a provider changes roles while remaining at the same site (for example, a provider who moves from VA to DOD but does not relocate or a resident rotates from one specialty service to another, i.e.: Oncology to Surgery). The goal is for the current provider to no longer receive notifications for orders written in the previous role, while being able to receive notifications for orders written in the new role. The purpose is to improve patient care by having alerts available to the provider now responsible for continuing that treatment/therapy for the patient.

The Provider Role Tool is a Graphical User Interface (GUI) application that can run standalone or can be added to the Computerized Patient Record System (CPRS) Tools Menu.

The anticipated responsible group for this reassignment would be the one the provider was leaving. However, it is possible that a site may determine that the reassignment duties would be assigned to a different team – such as the Clinical Application Coordinators. Of course, input from the team the provider is leaving will be required. For example, if a provider is leaving Oncology, the Oncology chief will have to inform the person doing reassignment what provider will pick up the treatment of the patients that are affected.

The following picture shows the architecture from a high level:

![](or-3-0-453-provider-role-tool-technical-manual/002.png)

Figure 1: High-level Architecture (hardware and communication)

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Audience: Local support staff, such as CACs, Information Technology (IT) Operations and Services (ITOPS) support, Product Support, and development personnel for tier 3 sustainment support.

Assumptions: This manual assumes a working knowledge of VistA.

Document Conventions: This manual uses several methods to highlight different aspects of the material:

- Descriptive text is presented in a proportional font (as represented by this font).
- Note: Notes are used to call a user’s attention to an important matter or idea. It will be in bold.
- Warning: This paragraph is a caution for users that if they do something, the result could be serious including loss of data.
- “Snapshots” of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Product Documentation

The following documents apply to this release:
- Provider Role Tool Deployment, Installation, Back-Out, and Rollback Guide
- Provider Role Tool Technical Manual
- Provider Role Tool User Guide
- Provider Role Tool Release Notes
All CPRS documents are available at the VA (Software) Documentation Library (VDL) web site at the following CAPRI link: <https://www.va.gov/vdl/section.asp?secid=1>
This website is usually updated within 1-3 days of the patch release date.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VistA software is a Kernel Installation and Distribution System (KIDS) software release. The initial distribution will be done via a host file distribution. In addition, there is a GUI executable and help files that will be released as a ZIP file.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool has no specific additional hardware, server, or workstation requirements. It will run under the existing hardware architecture.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool expects a fully patched VistA system for installation.

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool utilizes and updates the data in the ORDER file (#100).

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For detailed information on the installation and setup required for the Provider Role Tool, please refer to the associated Deployment, Installation, and Rollback Guide. Summary information about what is exported with the application follows.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool does not export any new files. However, it does modify the existing ORDER file (#100) as follows:

- ORDER TRANSFERS multiple (#70) field and it’s sub-fields:
  - TRANSFER DATE/TIME (#.01) field
  - TRANSFERRED FROM (#.02) field
  - TRANSFERRED TO (#.03) field
  - TRANSFER USER (#.04) field
- New Indices:
  - EPRTRDT created on the ORDER TRANSFERS multiple (#70) field of the ORDER (#100) file. The index is by the:
    - TRANSFERRED TO (.02) field of the ORDER TRANSFERS (#100.011) sub-file of the ORDER (#100) file
    - TRANSFER DATE/TIME (.01) field of the ORDER TRANSFERS (#100.011) sub-file of the ORDER (#100) file
    - ORDER \# (.01) field of the ORDER (#100) file
  - EPRACDT created on the ORDER ACTIONS multiple (#.8) field of the ORDER (#100) file. The index is by the:
    - PROVIDER (#3) field of the ORDER ACTION (#100.08) sub-file of the ORDER (#100) file.
    - DATE/TIME ORDERED (#.01) field of the ORDER ACTION (#100.08) sub-file of the ORDER (#100) file.
    - ORDER \# (.01) field of the ORDER (#100) file

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool utilizes routines that were already present in the Order Entry/Results Reporting (OR) package.

The initial distribution created/modified the following routines:

ORB3

ORCSAVE

ORELR5

ORQ2

ORQ3

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only menu option associated with the Provider Role Tool is the GUI context menu: OR PRT GUI.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no new mail groups, alerts, or bulletins distributed with the Provider Role Tool.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Integration Control Registrations (ICRs) were created or modified with the Provider Role Tool.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other than supported ICR types of Application Programming Interfaces (APIs), the following APIs are utilized by the Provider Role Tool:

ORDERER^ORQOR2

STATUS^ORQOR2

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool created and exported the following Remote Procedure Calls (RPCs):

ORQ3 AUTHUSR

ORQ3 EN

ORQ3 XFER

QRQ3 AUDIT

QRQ3 LOADALL

QRQ3 SAVEALL

QRQ3 XER HISTORY

The Provider Role Tool makes use of the following pre-existing RPCs:

ORWU USERINFO

ORWU DT

ORQOR DETAIL

ORWU NEWPERS

ORWU VERSRV

ORWUX SYMTAB

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

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For security information, refer to the Post Installation Considerations in the OR_3_453 Install Guide.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool requires that the user hold the OR PRT ACCESS key.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool creates no new files.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool uses the VistA broker architecture for communicating from the VistA server to the GUI application.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

National Service Desk, REDACTED

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| 2FA   | Two-Factor Authentication                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------|
| CAC   | Clinical Application Coordinator                                                                            |
| CD2   | Critical Decision Point \#2                                                                                 |
| CPRS  | Computerized Patient Record System.                                                                         |
| DOD   | Department of Defense                                                                                       |
| GUI   | Graphical User Interface                                                                                    |
| ICR   | Integration Control Registrations                                                                           |
| ITOPS | Information Technology Operations and Services (formerly known as Service Delivery and Engineering \[SDE\]) |
| KIDS  | Kernel Installation and Distribution System                                                                 |
| MVI   | Master Veteran Index                                                                                        |
| NSR   | New Service Request                                                                                         |
| PIN   | Personal Identification Number                                                                              |
| PIV   | Personal Identification Verification                                                                        |
| PRT   | Provider Role Tool                                                                                          |
| RACI  | Responsible, Accountable, Consulted, Informed                                                               |
| SDE   | Service Delivery and Engineering                                                                            |
| VA    | Veterans Affairs                                                                                            |
| VDL   | VA Document Library                                                                                         |
| VIP   | Veteran-focused Integration Process                                                                         |
| VistA | Veterans Health Information Systems and Technology Architecture                                             |

# Appendix A. Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter Name   | Parameter Definition                                                                                                                                                                                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRT EXCEPTION LOGGER | When this parameter is set to "yes", the application will display a custom access violation screen to the user as well as logging the error stack and allowing this to be sent via an email (if PRT EXCEPTION EMAIL is not blank).                                                   |
| PRT EXCEPTION EMAIL  | When the Exception Logger is enabled (PRT EXCEPTION LOGGER), the user has the ability to pre populate an email through Microsoft Outlook. If this parameter is not empty, the user can email the error log and this email address will be used for the pre population of that email. |
| PRT EXCEPTION PURGE  | When an error occurs and the Exception Logger is enabled (PRT EXCEPTION LOGGER), any file(s) that are older than the number of days set in this parameter will be removed from the user's machine.                                                                                   |