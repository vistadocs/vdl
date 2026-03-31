---
title: PSU*4*3 Release Notes Extract Enhancements Phase III
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Extract Enhancements Phase III
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4*3
group_key: "PSU:PSU:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - modified
  - interfaces
  - software
  - messages
  - options
  - functionality
  - project
  - extract
page_count: 0
word_count: 1244
section_count: 13
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_p3_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_p3_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

> ![](psu-4-3-release-notes-extract-enhancements-phase-iii/001.png)

PHARMACY BENEFITS MANAGEMENT(PBM)EXTRACT ENHANCEMENTSRELEASE NOTES

PSU\*4\*3

February 2006

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [User Interfaces](#user-interfaces)
  - [Hardware Interfaces](#hardware-interfaces)
  - [Software Interfaces](#software-interfaces)
  - [Communications Interfaces](#communications-interfaces)
  - [Enhancements Summary](#enhancements-summary)
  - [Pre-Installation Setup](#pre-installation-setup)
- [New Features](#new-features)
  - [New Options](#new-options)
  - [New Fields](#new-fields)
  - [New Reports](#new-reports)
- [Modified Features](#modified-features)
  - [Modified Options](#modified-options)
  - [Modified Fields](#modified-fields)
  - [Modified Reports](#modified-reports)
- [New Functionality](#new-functionality)
- [Impact on Other VistA Software Packages](#impact-on-other-vista-software-packages)
Pharmacy Benefits Management (PBM) Version 4.0 is a new enhanced version of the software and replaces PBM Version 3.0. It contains enhancements to support the Veterans Affairs National Formulary (VANF), disease management issues, and patient safety initiatives.

## User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software product shall conform to the existing VistA conventions and utilize a roll and scroll based interface. Software modifications shall be tested by Department of Veterans Affairs (VA) facilities to ensure that the software modifications meet the needs of the Veterans Health Administration (VHA) user.

Phase III requires the creation and configuration of an HL LOGICAL LINK called PSU SEND.

## Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product shall run on the standard hardware platform used by the Department of Veterans Affairs Healthcare facilities, Cache VMS.

Phase III utilizes HLO (Health Level 7 Optimized) technology, which requires port 5026 in test areas and port 5001 in live areas.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software must be running to support the enhancements requested.

|                                                              |                            |
|--------------------------------------------------------------|----------------------------|
| Package                                                  | Minimum Version Needed |
| Adverse Reaction Tracking (ART)                              | 4.0                        |
| Auto Replenishment/Ward Stock (AR/WS)                        | 2.3                        |
| Controlled Substances (CS)                                   | 3.0                        |
| Drug Accountability                                          | 3.0                        |
| HLO (Health Level 7 Optimized)                               | 1.6                        |
| Inpatient Medications                                        | 5.0                        |
| Integrated Funds Control, Accounting and Procurement (IFCAP) | 5.1                        |
| Kernel                                                       | 8.0                        |
| Laboratory                                                   | 5.2                        |
| MailMan                                                      | 8.0                        |
| National Drug File (NDF)                                     | 4.0                        |
| Outpatient Pharmacy                                          | 7.0                        |
| Patient Care Encounter (PCE)                                 | 1.0                        |
| Patient Information Management System (PIMS)                 | 5.3                        |
| Pharmacy Data Management (PDM)                               | 1.0                        |
| VA FileMan                                                   | 22.0                       |
| Visit Tracking                                               | 2.0                        |

## Communications Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The extracted data is electronically exported via MailMan to the PBM national database at <span class="mark">REDACTED</span> from each VA Medical Center (VAMC) or Outpatient clinic. MailMan messages are downloaded to text files onto the PBM network and run through a translation program. The data is then appended to an existing PBM Pharmacy dispensing master file.

In addition, PSU\*4\*3 introduces the new functionality of sending Chemistry Lab results to the PBM database via Health Level 7 (HL7). HLO is used to send and receive messages.

When a Chemistry Lab test is resulted, the creation and transmission of an HL7 message containing data about that patient and test result is sent real-time to the CMOP-NAT server. A PBM process on CMOP-NAT parses the received messages into a temporary holding area. A nightly job on the CMOP-NAT server loads these messages into a flat file for the PBM team and then cleans up old data from yesterday’s load.

## Enhancements Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following summarizes changes that were made to the PBM application during this enhancement. More detailed descriptions may be found in the remainder of this document.

Phase III Enhancements

The following enhancements are being introduced with the release of PBM V. 4.0 (PSU\*4\*3).

Rather than using the messaging method (MailMan), PSU\*4\*3 incorporates HL7 to send chemistry lab data in real-time to the PBM national database. Each VAMC or Outpatient clinic will send a PBM HL7 message each time a Chemistry Lab test is verified. It is then sent to the CMOP-NAT server. A PBM process will receive and store the messages and a nightly PBM job will load the messages into text files. PBM personnel will retrieve these files.

HLO and TCP/IP are the communication protocols that will be used to transmit messages between the VistA databases and PBM. Two links will be required for message transactions. VistA will send HL7 messages and receive a commit acknowledgement over the same link, and the link will then be disconnected.

## Pre-Installation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Parameters

None.

HL7 Links and Protocols

PSU logical link and HL7 protocols must be loaded at all facilities and on the national PBM server in order for the messaging to function properly.

*(This page included for two-sided copying.)*

# New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents features that were added during the PBM Extract Enhancement III project.

This project introduces the real-time collection and transmission of verified chemistry lab results to the PBM server.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options were added during this project.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new fields were added during this project.

## New Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new reports were added during this project.

*(This page included for two-sided copying.)*

# Modified Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current Functionality

The extracted lab data is electronically exported via MailMan to the PBM national database at <span class="mark">REDACTED</span> from each VAMC or Outpatient clinic. MailMan messages are downloaded to text files onto the PBM network and run through a translation program. The data is then appended to an existing PBM pharmacy dispensing master file.

New Functionality

This new functionality works in conjunction with all existing functionality. No existing functionality was modified.

Real-time transmission of PBM lab HL7 messages will be created and sent to the CMOP-NAT server each time a Chemistry Lab test is resulted at a VAMC. Two links will be required for message transactions. VistA will send HL7 messages and receive a commit acknowledgement over the same link, then the link will be disconnected. The laboratory data will be sent from each VAMC or Outpatient clinic via the HL7 link to the PBM national database and appended to a daily PBM master file.

![](psu-4-3-release-notes-extract-enhancements-phase-iii/002.png)Note: The laboratory extract that exists within the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] and *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] options will not be replaced by the HL7 transmission of laboratory data to the national database. This functionality is in addition to the laboratory extract that generates MailMan messages transmitted to the PBM national database at <span class="mark">REDACTED</span> that sites run on a monthly basis.

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes modifications made to options during the PBM Extract Enhancement III project.

There were no modifications made to the options during this project.

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No fields were modified during the PBM Extract Enhancement III project.

## Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reports were modified during the PBM Extract Enhancement III project.

*(This page included for two-sided copying.)*

# New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PBM Extract Enhancement III project provides automatic real-time transmission of PBM HL7 Chemistry Lab Results to the PBM national database. This process will be transparent to the users. The data will be stored in flat files on the CMOP-NAT server for the PBM team.

*(This page included for two-sided copying.)*

# Impact on Other VistA Software Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements described in this document do not have any impact on other VistA software packages.

*(This page included for two-sided copying.)*