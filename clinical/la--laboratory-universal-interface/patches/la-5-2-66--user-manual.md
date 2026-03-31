---
title: "LA*5.2*66 Laboratory: Universal Interface HL V1.6 Upgrade Installation and User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: "Laboratory: Universal Interface HL V1.6 Upgrade Installation and"
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*66
group_key: "LA:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - interface
  - vista
  - laboratory
  - software
  - patch
  - installation
  - universal
  - auto
page_count: 0
word_count: 5969
section_count: 43
table_count: 42
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_52_la66_install_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_52_la66_install_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

![](la-5-2-66-laboratory-universal-interface-hl-v1-6-upgrade-installation-and-user-g/001.png)

LABORATORYUNIVERSAL INTERFACE (UI)HEALTH LEVEL (HL) V1.6UPGRADEINSTALLATION AND USER GUIDEPATCH LA\*5.2\*66Version 5.2August 2008Department of Veterans AffairsVistA Health Systems Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Staffing Requirements:](#staffing-requirements)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff)
    - [Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)](#laboratory-information-manager-limautomated-data-processing-application-coordinator-adpac)
  - [User Interfaces](#user-interfaces)
  - [Blood Bank Clearance](#blood-bank-clearance)
    - [VistA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT](#vista-blood-bank-software-v52-device-product-labeling-statement)
- [Orientation](#orientation)
  - [Screen Captures:](#screen-captures)
  - [User Response:](#user-response)
  - [Return Symbol:](#return-symbol)
  - [Tab Symbol:](#tab-symbol)
  - [References:](#references)
  - [Software and Documentation Retrieval Locations and Formats](#software-and-documentation-retrieval-locations-and-formats)
    - [### OIFO’s ANONYMOUS SOFTWARE Directories:](#oifos-anonymous-software-directories)
    - [Software Retrieval:](#software-retrieval)
    - [Documentation Retrieval Formats:](#documentation-retrieval-formats)
  - [## ## VistA Website Locations:](#vista-website-locations)
    - [VistA Laboratory Version 5.2 Home Page](#vista-laboratory-version-52-home-page)
    - [VistA Documentation Library (VDL)](#vista-documentation-library-vdl)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [Flow Diagram](#flow-diagram)
- [Enhancements and Modifications](#enhancements-and-modifications)
  - [Enhancements](#enhancements)
  - [Modifications:](#modifications)
  - [# Security Information](#security-information)
  - [Security](#security)
    - [Security Management](#security-management)
    - [Security Features:](#security-features)
    - [Remote Systems](#remote-systems)
    - [Archiving Capabilities](#archiving-capabilities)
    - [### Purging Capabilities](#purging-capabilities)
    - [Contingency Planning](#contingency-planning)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [### ### References](#references-1)
    - [### Official Policies](#official-policies)
- [Pre-Installation Information](#pre-installation-information)
  - [Test Sites](#test-sites)
  - [Test Accounts](#test-accounts)
  - [Staffing Requirements:](#staffing-requirements-1)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff-1)
    - [Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)](#laboratory-information-manager-limautomated-data-processing-application-coordinator-adpac-1)
  - [Hardware Interfaces and Operating System:](#hardware-interfaces-and-operating-system)
  - [Generic Instrument Manager (GIM):](#generic-instrument-manager-gim)
  - [## System Performance Capacity:](#system-performance-capacity)
  - [## Memory Constraints:](#memory-constraints)
  - [Global Growth:](#global-growth)
  - [## Installation Time:](#installation-time)
  - [## Users Off the System](#users-off-the-system)
  - [Background Jobs:](#background-jobs)
  - [Backup Routines:](#backup-routines)
  - [Lab Universal Interface Auto Download:](#lab-universal-interface-auto-download)
  - [## Kernel Installation and Distribution System (KIDS):](#kernel-installation-and-distribution-system-kids)
  - [## Required VistA Software Applications:](#required-vista-software-applications)
  - [## Required Patches:](#required-patches)
  - [Namespace:](#namespace)
  - [Database Integration Agreements (DBIAs):](#database-integration-agreements-dbias)
  - [Data Dictionary (DD) Changes:](#data-dictionary-dd-changes)
  - [New Option:](#new-option)
  - [## ## New Protocols:](#new-protocols)
- [Installation Instructions](#installation-instructions)
  - [NOTE: Routine LA66 will be deleted after successful patch installation.](#note-routine-la66-will-be-deleted-after-successful-patch-installation)
  - [Installation Example:](#installation-example)
- [Lab Auto-Instrument Configuration](#lab-auto-instrument-configuration)
  - [Staffing Requirements:](#staffing-requirements-2)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff-2)
    - [Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)](#laboratory-information-manager-limautomated-data-processing-application-coordinator-adpac-2)
  - [Lab Auto-Instrument Set-Up](#lab-auto-instrument-set-up)
  - [Creating a New Lab UI or Converting an Existing Lab UI](#creating-a-new-lab-ui-or-converting-an-existing-lab-ui)
- [VistA LABORATORY UNIVERSAL INTERFACE (UI) HL v1.6 UPGRADE](#vista-laboratory-universal-interface-ui-hl-v16-upgrade)
- [PATCH LA\5.2\66 USER GUIDE](#patch-la5266-user-guide)
- [Use of the Software](#use-of-the-software)
  - [Lab Universal Interface Setup \[LA7 UI SETUP\] option:](#lab-universal-interface-setup-la7-ui-setup-option)
- [Glossary](#glossary)
The Veterans Health Information Systems and Architecture (VistA) Laboratory Universal Interface (UI) Health Level (HL) V1.6 UPGRADE Patch LA\*5.2\*66 Installation and User Guide Version 5.2 provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) staff and the Laboratory Information Manager (LIM) with a straightforward means for implementing the software application.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that an IRM staff perform the installation and provide maintenance support for the VistA Laboratory UI HL v1.6 Upgrade patch LA\*5.2\*66 software release.

> **NOTE:** Patch installation and auto-instrument set-up should to be coordinated between IRM staff, Laboratory Information Manager (LIM), or Laboratory’s Automated Data Processing Application Coordinator (ADPAC).

### Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and auto-instrument set-up for this patch requires interactive input between IRM staff and LIM/ADPAC who are well versed in the VistA Laboratory V. 5.2 software package.

## User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users are not required to enter data.

## Blood Bank Clearance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*66 does not contain any changes to the VISTA BLOOD BANK Software as defined by VHA DIRECTIVE 2004-058 titled VISTA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*66 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LA\*5.2\*66 have no effect on Blood Bank software functionality, therefore RISK is none.

VALIDATION REQUIREMENTS BY OPTION: Because of the nature of the changes made, no specific validation requirements exist as a result of installation of this patch.
# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses package-or audience-specific notations or directions (e.g., symbols used to indicate terminal dialogues and user responses).

## Screen Captures:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

## User Response:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry response appears in boldface type Courier font, no larger than 10 points.

Example:Boldface type

## Return Symbol:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<RET\> symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<ENTER\>

## Tab Symbol:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<Tab\>

## References:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<http://www.va.gov/vdl/application.asp?appid=120>

Generic Interface Manager (GIM) Vendor’s Documentation

## Software and Documentation Retrieval Locations and Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 UPGRADE Patch LA\*5.2\*66 software and Installation and User Guide Version 5.2 distributions are as follows:

> **NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “download.VistA.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

### ### OIFO’s ANONYMOUS SOFTWARE Directories:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 UPGRADE patch LA\*5.2\*66 Installation/User Guide and VistA Laboratory Universal Interface HL v1.6 Upgrade Patch LA\*5.2\*66 HL7 Specifications Document are available at the following Office of Information Field Offices (OIFOs) ANONYMOUS.SOFTWARE directories:

| OI Field Offices               | FTP Addresses                  | Directories                    |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|                                    |                                    |                                    |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|                                    |                                    |                                    |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

### Software Retrieval:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 UPGRADE Patch LA\*5.2\*66 software is distributed by Packman.

### Documentation Retrieval Formats:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 UPGRADE Installation/User Guide and HL7 Specifications for Patch LA\*5.2\*66 documentation files are exported in the following formats:

| File Names                     | Contents                                                                                 | Retrieval Formats |
|------------------------------------|----------------------------------------------------------------------------------------------|-----------------------|
| LAB_52_LA66_INSTALL_USER_GUIDE.doc | Laboratory Universal Interface HL V1.6 Upgrade Installation and User Guide Patch LA\*5.2\*66 | BINARY                |
| LAB_52_LA66_INSTALL_USER_GUIDE.pdf | Laboratory Universal Interface HL V1.6 Upgrade Installation and User Guide Patch LA\*5.2\*66 | BINARY                |
| LAB_52_LA66_HL7_SPECIFICATIONS.doc | Laboratory Universal Interface HL V1.6 Upgrade Installation and User Guide Patch LA\*5.2\*66 | BINARY                |
| LAB_52_LA66_HL7_SPECIFICATIONS.pdf | Laboratory Universal Interface HL V1.6 Upgrade Installation and User Guide Patch LA\*5.2\*66 | BINARY                |

## ## ## VistA Website Locations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 UPGRADE Patch LA\*5.2\*66 Installation and User Guide Version 5.2 is accessible in Portable Document Format (PDF) and MS Word (DOC) Format at the following locations:

### VistA Laboratory Version 5.2 Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

### VistA Documentation Library (VDL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[www.va.gov/vdl/](http://www.va.gov/vdl/)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the VistA Laboratory Universal Interface (UI) Health Level (HL) v1.6 Upgrade Patch LA\*5.2\*66 software release is to improve the transmission of laboratory test results from clinical analyzers to the VistA system. This release upgrades Lab UI from VistA’s Health Level Seven (HL) v1.5 to VistA’s HL v1.6, which includes the use of version 1.6 Transmission Control Protocol/Internet Protocol (TCP/IP) functionality. This functionality supports the current Lab UI HL7 Interface Specifications based on the HL7 Standard V2.2.

The current UI interface using the HL v1.5 interface will continue to function after patch installation. The transition to the HL V1.6 interface can be accomplished after patch installation on a connection by connection basis. When possible, switching from the old interface to the new interface should be done on a per instrument basis instead of all instruments at once. Follow the post installation instructions to convert an interface to the HL V1.6 interface.

The Generic Instrument Manager (GIM) is a locally procured commercial device that controls communications between the Laboratory instruments and VistA. The VistA system downloads work lists through the GIM to the various instruments, and the instruments upload results to VistA through the GIM, eliminating the need for Laboratory developers to write a new interface for each different instrument. Due to the increased laboratory workload, higher instrument throughput, longer and more textual lab results, and the emergence of more efficient communications platforms have rendered HL7 v1.5 obsolete. HL7 v1.6 allows faster transmission, longer messages, and more advanced queue handling than HL7 v1.5.

> **NOTE:** New Generic Instrument Manager (GIM) software must be obtained from the vendor in order for this new interface to work.

Additionally, HL7 messaging depends on VistA’s HEALTH LEVEL SEVEN package for validation and routing messages. Infrastructure Information Service (IIS) has recommended that all VistA applications upgrade to HL7 v1.6 as soon as feasible.

> **NOTE:** Information Infrastructure Systems (IIS) will make no further enhancements to the VistA HL v1.5 package.

Significant differences between the two versions are listed in the table below.

|                                                     |                                                                                                                                  |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| HL7 v1.5                                        | HL7 v1.6                                                                                                                     |
| One sender and one receiver per message.            | One sender, one or more receivers.                                                                                               |
| Sender and receiver must be on different systems.   | Sender and receiver can be on the same or different systems.                                                                     |
| Messages must go through a communications protocol. | Messages sent to applications on the same system do not have to go through a communications protocol.                            |
| All messages are processed in the background.       | Messages are processed in either the foreground or background, based on the priority assigned by sending/receiving applications. |
| No support for event points.                        | Event points are supported.                                                                                                      |

The current UI using the VistA HL v1.5 interface will continue to function normally after installation of this patch. The transition to the VistA HL V1.6 interface can be accomplished after patch installation on a connection by connection basis. There are post installation instructions to convert an interface to the HL V1.6 interface.

There are no special implementation interfaces required for this new functionality.

Implementation of this enhancement is expected to cause no changes to the process of reporting lab results. Although faster, more efficient, and easier to manage, the process itself will not change. Since the release of Laboratory Electronic Data Interchange (LEDI) II to the field, sites are familiar with the configuration and file structure of HL7 v1.6.

Vendors of the GIM devices have been notified of VistA’s enhanced capabilities. The three primary vendors are:

- Data Innovations
- Dade
- Dawning Technologies

Because HL7 v1.6 is backward compatible, the time of these vendor modifications is critical. After the VistA conversion is complete, the GIM may be updated at any time using the vendor’s update process. Timing would be arranged between each site and the vendor.

### Flow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-66-laboratory-universal-interface-hl-v1-6-upgrade-installation-and-user-g/002.png)

# Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Universal Interface HL V1.6 Upgrade Patch LA\*5.2\*66 exports the following enhancements and modifications:

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Patch LA\*5.2\*66 release allows sites to interface automated testing devices via the supported TCP/IP functionality. Prior to the release of this patch, laboratory instruments interfaced via TCP/IP using a non-supported modified HL7 routine. This release also contains the following 13 new protocols:

> LA7UI ORM-O01 EVENT 2.2

> ORM event driver for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2.

> LA7UI ORM-O01 SUBS 2.2

> ORM subscriber for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2.

> LA7UI ORU-R01 SUBS 2.2

> ORU subscriber for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2.

The following are ORU event drivers for Lab Universal Interface (HL7v1.6 upgrade) using HL7 messaging v2.2:

> LA7UI1 ORU-R01 EVENT 2.2

> LA7UI2 ORU-R01 EVENT 2.2

> LA7UI3 ORU-R01 EVENT 2.2

> LA7UI4 ORU-R01 EVENT 2.2

> LA7UI5 ORU-R01 EVENT 2.2

> LA7UI6 ORU-R01 EVENT 2.2

> LA7UI7 ORU-R01 EVENT 2.2

> LA7UI8 ORU-R01 EVENT 2.2

> LA7UI9 ORU-R01 EVENT 2.2

> LA7UI10 ORU-R01 EVENT 2.2

2\. The new Lab Universal Interface Setup \[LA7 UI SETUP\] option allows sites to configure Lab Universal Interface entries (LAUI\*) in the LA7 MESSAGE PARAMETER file (#62.48), and corresponding entries in the AUTO INSTRUMENT file (#62.4), which use the Lab Universal Interface. It also allows editing of fields pertaining to Laboratory UI only. This option is located on ‘Lab Universal Interface Menu \[LA7 MAIN MENU\] menu.’

3\. This software enhancement allows the sites to manage these interfaces using the HL7 v1.6 package’s tools.

4\. HL7 messages are HL7 version 2.2 and the messaging is composed of ORM~O01 and ORU~R01 messages. Messaging uses original mode acknowledgements. ORM messages use “LA7LAB” as the Sending Application and “LA7UIx” (where “x” is an integer 1-10) as the Receiving Application. ORU messages use “LA7UIx” as the Sending Application and "LA7LAB" as the Receiving Application.

5\. This software enhancement creates conventions to allow sites to interface with multiple Generic Instrument Managers (GIMs). Each of the following four files has 10 entries using the following naming conventions examples that contain “LA7UIx” (where “x” is an integer 1-10) such as “LA7UI1 ORU-R01 EVENT 2.2,” and “LA7UI1.”

- PROTOCOL file (#101)
- HL7 APPLICATION PARAMETER file (#771)
- HL LOGICAL LINK file (#870)
- LA7 MESSAGE PARAMETER file (#62.48)

> **NOTE:** New GIM drivers must be obtained from the vendors in order for this new interface to work.

## Modifications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications are added to the existing Universal Interface (UI) software via patch LA\*5.2\*66 release and installation:

1\. This software modification sends ORM messages as an ORC/OBR segment pair. The v1.5 interface constructed ORM message segments were not in compliance with the HL7 standard. Previously an ORC segment was followed by one or more OBR segments. The HL7 standard specifies that ORC/OBR segments should exist as a pair, so in this interface each ordered test will be sent in the ORM message as an ORC/OBR segment pair.

Example: PID...

> PV1...

> ORC...

> OBR...

> ORC...

> OBR...

2\. HL7 message data is now checked for conflicts with HL7 delimiters. If data conflicts with the message’s delimiters then the data with be escape encoded according to HL7 rules.

3\. In an ORM message, OBR-18 is constructed as an HL7 string data type. The HL7 v1.5 interface constructed it as a coded element (CE) data type.

4\. For Lab UI messages, if the specimen source received does not match the accession’s topography related HL7 specimen source, an interface error will be generated and the results rejected. The error will not be created if the specimen is related to the LAB CONTROL NAME file (#62.3).

5\. For Lab UI messages, any units/reference ranges received from an instrument are discarded as the units/reference ranges from the associated LABORATORY TEST file (#60) are used.

6\. For Lab UI messages, abnormal flags received from an instrument are not stored. Abnormality is determined by settings in the corresponding LABORATORY TEST file (#60) for the related test.

7\. The Lab UI Auto Download process (routine LA7ADL) is changed to support the FileMan system wide lock timeout via supported API LOCK^DILF.

8\. To provide for data entry consistency, results received via this interface are validated against the input transform for the data field used to store the test results. Test results received from an instrument that do not conform to the input transform for the related Lab Data Name will be rejected.

If SET OF CODES is utilized as the data type for a particular interfaced test, the internally stored code needs to be brought into alignment with what the instrument is reporting. If the instrument sends a result that does not match what is entered in the SET OF CODES that result is considered not to be verifiable data.

## # Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All participating systems must maintain their own C2 certifications as required by their governing security, privacy act, and data protection regulations and laws.

### Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory UI HL V1.6 Upgrade Patch LA\*5.2\*66 software release uses functionality provided by VistA HL7 v1.6 package.

### Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Mail Group

> The LMI mail group is required with the installation of this patch (i.e., sending install started alert to mail group LMI). The LAB MESSAGING mail group is used to notify laboratory and IRM personnel of exception conditions encountered during operation of the software.

#### Alerts

Sending install started alert to mail group G.LMI.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software does not transmit data to any remote system/site.

### Archiving Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional archiving capabilities are included in this software release.

### ### Purging Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 messages transmitted and received by VistA's HL7 v1.6 package are purged automatically using the existing purging functionality in that package. Copies of these HL7 messages created by this software are purged automatically via software using the site specified settings in the LA7 MESSAGE PARAMETER file (#62.48), GRACE PERIOD FOR MESSAGES field (#3). This purging is accomplished by the tasked Lab Messaging Nightly Cleanup \[LA7TASK NIGHTY\] option.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each facility using the VistA Laboratory UI Patch LA\*5.2\*66 software must develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan must identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no non-VA embedded software in this release.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures are not used in this product.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional menu security actions are needed with this software.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional Security Keys are required for this software product.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan security access Ll code is recommended if file security is deemed necessary by the VA facilities. It is strongly recommended that Kernel’s File Access security be utilized to provide file security.

### ### ### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following references may be helpful when installing and implementing the VistA Laboratory UI Patch LA\*5.2\*66 software application:

- Kernel Systems Manual V. 8.0
- Kernel Toolkit V. 7.3
- VA FileMan V. 22.0
- VA MailMan V. 8.0

#### Related Manuals

For HL7 information please refer to the following manual:

- Health Level Seven (HL7) Standard version 2.2

> Health Level Seven

> 3300 Washtenaw Ave, Suite 227

> Ann Arbor, MI 48104-4250

> \(313\) 677-7777

> Email: <hq@hl7.win.net>

For applications using the V. 1.6 interface method please refer to the following manuals:

- DHCP HL7 V. 1.6 Installation Guide
- DHCP HL7 V. 1.6 Package Security Guide
- DHCP HL7 V. 1.6 Release Notes
- DHCP HL7 V. 1.6 Technical Manual
- DHCP HL7 V. 1.6 User Manual

For applications using the V. 1.5 interface method, you might also want to refer to the following manuals:

- DHCP HL7 V. 1.5 Developer Manual
- DHCP HL7 V. 1.5 Installation Guide
- DHCP HL7 V. 1.5 Package Security Guide
- DHCP HL7 V. 1.5 Release Notes
- DHCP HL7 V. 1.5 Technical Manual
- DHCP HL7 V. 1.5 User Manual

Generic Interface Manager (GIM) Vendor’s Documentation

### ### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no official policies unique to the VistA Laboratory UI v1.6 Upgrade Patch LA\*5.2\*66 software application distribution.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides pre-installation information that should be adhered to prior to installing the VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 product.

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 software release has been tested at the following VA sites:

| VA Test Sites                  | Operating System Platform | Test Site Size |
|------------------------------------|-------------------------------|--------------------|
|                                    |                               |                    |
| <span class="mark">REDACTED</span> | Cache/VMS                     | Large              |
|                                    |                               |                    |
|                                    |                               |                    |
| <span class="mark">REDACTED</span> | Cache/VMS                     | Large/Integrated   |
|                                    |                               |                    |
| <span class="mark">REDACTED</span> | Cache/VMS                     | Large              |
|                                    |                               |                    |

## Test Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the software initially be installed and tested in test accounts prior to installation in production accounts.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Patch installation and auto-instrument set-up should to be coordinated between IRM staff, Laboratory Information Manager (LIM), or Laboratory’s Automated Data Processing Application Coordinator (ADPAC).

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that an IRM staff perform the installation, auto-instrument set-up, and provide maintenance support of the VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 software release.

### Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and auto-instrument set-up for this patch requires interactive input between IRM staff and LIM/ADPAC who are well versed in the VistA Laboratory V. 5.2 package.

## Hardware Interfaces and Operating System:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory UI Patch LA\*5.2\*66 software runs on the standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities.

## Generic Instrument Manager (GIM):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Generic Instrument Manager (GIM) drivers must be obtained from the vendors in order for this new interface to work.

## ## System Performance Capacity:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no significant changes in the performance of the system once the enhancement VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 is installed.

## ## Memory Constraints:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no memory constraints on the system with the installation of this enhancement patch.

## Global Growth:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The use of the VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 functionality should not create any appreciable global growth or network transmission problems.

## ## Installation Time:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The install time for this patch is less than 2 minutes. Suggested time to install is non-peak hours.

## ## Users Off the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed when Laboratory users are off the system.

## Background Jobs:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lab Universal Interface Auto Download should be shut down before installing this patch. This can be done via the Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] option. No options need to be placed out of service.

## Backup Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that a backup of the transport global is performed before installing VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66.

## Lab Universal Interface Auto Download:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Universal Interface Auto Download should be shut down before installing this patch. This can be done via the Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] menu option.

## ## Kernel Installation and Distribution System (KIDS):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 distribution is using KIDS.

> **NOTE:** For further instructions on using KIDS, please refer to the Kernel Version 8.0 Systems Manual.

## ## Required VistA Software Applications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following applications must be installed before installing VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66:

| VistA Software Applications | Versions                              |
|---------------------------------|-------------------------------------------|
| Kernel                          | 8.0                                       |
| VA FileMan                      | 22.0                                      |
| VA Mailman                      | 8.0                                       |
| VistA Laboratory                | 5.2 (with all released patches installed) |

## ## Required Patches:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before installing VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66:

| Required Patches                                                  | Versions |
|-----------------------------------------------------------------------|--------------|
| LA\*5.2\*57 LAB UNIVERSAL INTERFACE AUTO DOWNLOAD FIXES               | 5.2          |
| LA\*5.2\*72 FIX UNDEF IN LA7VIN5A PRDID+11                            | 5.20         |
| HL\*1.6\*93 DYNAMIC ROUTING ENHANCEMENT                               | 1.6          |
| HL\*1.6\*122 LOCKING CODE ENHANCEMENT, DON'T PING FUNCTION AND OTHERS | 1.6          |

## Namespace:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 uses AUTOMATED LAB INSTRUMENTS LA namespace.

## Database Integration Agreements (DBIAs):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no DBIAs required for this software release.

## Data Dictionary (DD) Changes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no DD changes required for this release.

## New Option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Lab Universal Interface Setup \[LA7 UI SETUP\] option allows configuring Lab Universal Interface entries (LA7UI\*) in the LAB MESSAGE PARAMETER file (#62.48) and corresponding entries in the AUTO INSTRUMENT file (#62.4) which use the Lab Universal Interface

## ## ## New Protocols:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software release contains the following new protocols:

> LA7UI ORM-O01 EVENT 2.2

> ORM event driver for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2

> LA7UI ORM-O01 SUBS 2.2

> ORM subscriber for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2

> LA7UI ORU-R01 SUBS 2.2

> ORU subscriber for Lab Universal Interface (HL7 v1.6 upgrade) using HL7 messaging v2.2

The following are ORU event drivers for Lab Universal Interface (HL7) v1.6 upgrade) using HL7 messaging v2.2:

LA7UI1 ORU-R01 EVENT 2.2LA7UI2 ORU-R01 EVENT 2.2LA7UI3 ORU-R01 EVENT 2.2LA7UI4 ORU-R01 EVENT 2.2LA7UI5 ORU-R01 EVENT 2.2LA7UI6 ORU-R01 EVENT 2.2LA7UI7 ORU-R01 EVENT 2.2LA7UI8 ORU-R01 EVENT 2.2LA7UI9 ORU-R01 EVENT 2.2LA7UI10 ORU-R01 EVENT 2.2

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The install time for this patch is less than 2 minutes. This patch should be installed when Laboratory users are off the system.

The Lab Universal Interface Auto Download should be shut down before installing this patch. This can be done via the Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] menu option.

The KIDS environment check determines if the Lab UI Auto Download process is currently running:

> If it is running it will be automatically shut down during patch installation and automatically restarted after patch installation.

> If the Lab UI Auto Download process is not running at patch installation time then KIDS will take no action with the Lab UI Auto download process.

After patch installation is complete, check the status of the Lab UI Auto Download process using the option Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] and configure to normal operational setting (see step 6 below).

Suggested time to install: Non-peak requirement hours. The installation should NOT be queued.

> **NOTE:** Patch installation needs to be coordinated with the Laboratory Information Manager (LIM/ADPAC).

1\. Use the 'INSTALL/CHECK MESSAGE' option of the PackMan menu. This option will load the KIDS patch onto your system.

2\. On the 'Kernel Installation & Distribution System' Menu (KIDS), select the 'Installation' menu.

3\. Use the 'Verify Checksum in Transport Global' option and verify that all routines have the correct checksums.

4\. On the KIDS menu, under the 'Installation' menu, use the following options:

Print Transport Global

Compare Transport Global to Current System

Backup a Transport Global

5\. Use the 'Install Package(s)' option under the 'Installation' menu and select the package ‘LA\*5.2\*66.’

When prompted

‘Want KIDS to Rebuild Menu Trees Upon Completion of Install?’ choose ‘NO’

> **NOTE:** Responding “Yes” to the prompt for rebuilding menu trees can significantly increase install time.

When prompted

‘Want KIDS to INHIBIT LOGONs during the install?’ choose ‘NO’

When prompted

‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//’ choose ‘NO’ unless the site has additional laboratory options that should be disabled during install.

6\. If the Lab Universal Interface Auto Download process was stopped manually, restart it via the Start/Stop Auto Download Background Job \[LA7 ADL START/STOP\] menu option.

If the process was stopped by the KIDS install itself, the process will restart automatically.

## NOTE: Routine LA66 will be deleted after successful patch installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: Install Package(s)\<ENTER\>

Select INSTALL NAME: LA\*5.2\*66 Loaded from Distribution

9/13/07@15:03:06

=\> LA\*5.2\*66 ;Created on Sep 13, 2007@13:07:05

This Distribution was loaded on Sep 13, 2007@15:03:06 with header of

LA\*5.2\*66 ;Created on Sep 13, 2007@13:07:05

It consisted of the following Install(s):

LA\*5.2\*66

Checking Install for Package LA\*5.2\*66

Will first run the Environment Check Routine, LA66

Sending install started alert to mail group G.LMI

Shutting down Lab Universal Interface Auto Download Job

..........

N O T E: If you abort this installation

restart the Lab Universal Interface background job.

--- Environment is okay ---

Install Questions for LA\*5.2\*66

Incoming Files:

62.48 LA7 MESSAGE PARAMETER (including data)

> **NOTE:** You already have the 'LA7 MESSAGE PARAMETER' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// n NO

Want KIDS to INHIBIT LOGONs during the install? YES// n NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// n NO

Enter the Device you want to print the Install messages.

Enter a '^' to abort the install.

DEVICE: HOME//\<ENTER\> TELNET

Install Started for LA\*5.2\*66 :

Sep 13, 2007@15:03:27

Build Distribution Date: Sep 13, 2007

Installing Routines:

Sep 13, 2007@15:03:28

Running Pre-Install Routine: PRE^LA66

\*\*\* Pre install started \*\*\*

\*\*\* Pre install completed \*\*\*

Installing Data Dictionaries:

Sep 13, 2007@15:03:28

Installing Data:

Sep 13, 2007@15:03:28

Installing PACKAGE COMPONENTS:

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Located in the LA7 (LAB MESSAGING) namespace.

Installing OPTION

Sep 13, 2007@15:03:29

LA\*5.2\*66

------------------------------------------------------------------------

Running Post-Install Routine: POST^LA66

\*\*\* Post install started \*\*\*

\*\*\* Updating facility name for LA7UI\* entries in file \#771 \*\*\*

\*\*\* Updating facility name completed \*\*\*

--- No actions required for post install ---

Restarting Lab Universal Interface Auto Download Job

\*\*\* Post install completed \*\*\*

Sending install completion alert to mail group G.LMI

Updating Routine file...

Updating KIDS files...

LA\*5.2\*66 Installed.

Sep 13, 2007@15:03:32

Install Message sent \#nnnnn

------------------------------------------------------------------------

--------------------------------------------------------------

100% \| 25 50 75 \|

Complete --------------------------------------------------------------

Install Completed

# Lab Auto-Instrument Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information and steps must be adhered to for the software to perform successfully as designed:

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that an IRM staff perform the installation, and provide maintenance support of the VistA Laboratory UI HL v1.6 Upgrade Patch LA\*5.2\*66 software release.

> **NOTE:** Patch installation and auto-instrument set-up should to be coordinated between IRM staff, Laboratory Information Manager (LIM), or Laboratory’s Automated Data Processing Application Coordinator (ADPAC).

### Laboratory Information Manager (LIM)/Automated Data Processing Application Coordinator (ADPAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and auto-instrument set-up for this patch requires interactive input between IRM staff and LIM/ADPAC who are well versed in the VistA Laboratory V. 5.2 package.

## Lab Auto-Instrument Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps to set-up a Lab auto-instrument:

> **NOTE:** The current UI interface using the HL v1.5 interface continues to function after patch installation. The transition to the HL V1.6 interface can be accomplished after patch installation on a connection by connection basis.

> **NOTE:** PROTOCOL file (#101), HL7 APPLICATION PARAMETER file (#771), HL LOGICAL LINK file (#870), and LA7 MESSAGE PARAMETER file (#62.48) each have 10 entries using a naming convention which contains “LA7UIx” (i.e., where “x” is an integer) such as “LA7UI1 ORU-R01 EVENT 2.2” and “LA7UI1.” This naming convention allows the site to interface with multiple Generic Interface Managers (GIMs). The vendor’s system communicating with VistA is called Generic Interface Manager (GIM).

Step \#1: AUTO INSTRUMENT file (#62.4), MESSAGE CONFIGURATION field (#8) must be set to the appropriate entry (i.e., LA7UI1).

> **NOTE:** VistA Laboratory UI software is distributed with support for the following 10 UI interfaces: LA7UI1, LA7UI2, LA7UI3, LA7UI4, LA7UI5, LA7UI6, LA7UI7, LA7UI8, LA7UI9, and LA7UI10.

Example: MESSAGE CONFIGURATION field (#8) appropriate entry

MESSAGE CONFIGURATION (#8) = LA7 MESSAGE PARAMETER entry (ie LA7UI1)

> **NOTE:** This naming convention LA7UIx is used throughout the software for consistency and linking of the corresponding Lab and HL7 packages. Deviation from this naming convention will have unpredictable effects.

Step \#2: In order to send/receive messages the configuration must be set to ACTIVE in the LA7 MESSAGE PARAMETER file (#62.48), STATUS field (#2). The configuration must also specify which routine is used to process messages in LA7 MESSAGE PARAMETER file (#62.48), PROCESS DOWNLOAD field (#6). This field must be set to D EN^LA7UIO for Lab Universal Interfaces.

Example: PROCESS DOWNLOAD field (#6), set to D EN^LA7UIO

LA7 MESSAGE PARAMETER (#62.48)

STATUS (#2) = ACTIVE

PROCESS DOWNLOAD (#6) = D EN^LA7UIO

## Creating a New Lab UI or Converting an Existing Lab UI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps to create a new Lab UI or convert an existing Lab UI:

> **NOTE:** The old HL7 v1.5 and new HL7 v1.6 Universal Interfaces can run at the same time. It is strongly advised that, whenever possible, the switchover from the old interface to the new interface be done on a per instrument basis instead of all instruments at once.

The Lab UI software is distributed with support for ten UI interfaces, named LA7UI1 through LA7UI10. This naming convention (LA7UIx) is used throughout the software for consistency and linking of the corresponding Lab and Health Level Seven packages. Deviation from this name spacing will have unpredictable effects.

Step 1: Determine which Lab UI will be used for the interface (i.e., LA7UIx where ‘x’ is a number 1-10).

When switching to HL v1.6 interface, different entries in HL7 APPLICATION PARAMETER file (#771) are utilized.

> **NOTE:** Vendor’s system communicating with VistA is called Generic Interface Manager (GIM).

The VistA HL v1.6 does NOT use HL7 NON-DHCP APPLICATION PARAMETER file (#770).

All related Lab Universal Interface entries are referenced in HL7 APPLICATION PARAMETER file (#771).

Example: Orders (ORM messages) from VistA to the GIM use the following values in addressing messages:

- Sending application: LA7LAB
- Sending facility: VA station number of primary facility
- Receiving application: LA7UIx (where x is an integer)
- Receiving facility: VA station number of primary facility

Example: Results (ORU messages) from the GIM to VistA GIM use the following values in addressing messages:

- Sending application: LA7UIx (where x is an integer)
- Sending facility: VA station number of primary facility
- Receiving application: LA7LAB
- Receiving facility: VA station number of primary facility

Step 2: The person(s) supporting the HL package will use the Link Edit \[HL EDIT LOGICAL LINKS\] option to configure the logical link associated with the interface (i.e. LA7UIx). These links come pre-configured with some information.

Configure the following fields:

On screen 1

> a\. AUTOSTART - per site's preference

> b\. LLP TYPE - per site's preference.

Example: HL7 LOGICAL LINK (Screen 1)

HL7 LOGICAL LINK (Screen 1)

-------------------------------------------------------------------------

NODE: LA7UI1

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Disabled

QUEUE SIZE: 10

LLP TYPE: TCP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

On screen 2

> c\. TCP/IP ADDRESS - if using TCP as the communication protocol then the IP address of the GIM.

> d\. TCP/IP PORT - if using TCP as the communication protocol then the port the GIM will be listening on.

Example: HL7 LOGICAL LINK (Screen 2)

HL7 LOGICAL LINK (Screen 2)

-------------------------------------------------------------------------

\[--------------------TCP LOWER LEVEL PARAMETERS----------------------\]

\| LA7UI1 \|

\| \|

\| TCP/IP SERVICE TYPE: CLIENT (SENDER) \|

\| TCP/IP ADDRESS: \|

\| TCP/IP PORT: \|

\| TCP/IP PORT (OPTIMIZED):                                  \|

\| \|

\| ACK TIMEOUT: 60 RE-TRANSMISION ATTEMPTS: 5 \|

\| READ TIMEOUT: 3 EXCEED RE-TRANSMIT ACTION: ignore \|

\| BLOCK SIZE: SAY HELO: \|

\| DIRECT CONNECT OPEN TIMEOUT: \|

\| STARTUP NODE: PERSISTENT: YES \|

\| RETENTION: 120 UNI-DIRECTIONAL WAIT: 3 \|

COMMAND: Press \<PF1\>H for help Insert

Step 3: Edit AUTO INSTRUMENT file (#62.4), MESSAGE CONFIGURATION field (#8). Select the appropriate LA7UIx entry to switch this automated instrument to use the HL v1.6 interface. This can be done using the new Lab Universal Interface Setup \[LA7 UI SETUP\] menu option.

The FILE BUILD ENTRY field (#93) should equal “EN” and the FILE BUILD ROUTINE field (#94) should equal “LA7UID”. These fields are automatically configured using the new Lab Universal Interface Setup \[LA7 UI SETUP\] menu option.

> **NOTE:** AUTO INSTRUMENT file (#62.4), CHEM TESTS subfile (#30), REMOVE SPACES FROM RESULT field (#17), has its default behavior changed with this patch. This field now shares the same default behavior as it does with the Laboratory Electronic Data Interchange (LEDI) and Point of Care (POC) interfaces. If the REMOVE SPACES FROM RESULT field (#17) is empty, it defaults to “NO” -- in the old universal interface, if this field was empty it defaulted to “YES”. Be sure to set this field as appropriate for use with this patch.

Step 4: Make the appropriate changes on the GIM to configure it to communicate with the VistA HL v1.6 package logical links.

> **NOTE:** Refer to GIM vendor’s documentation and instructions and the sending application/facility and receiving application/facility as specified above.

Check and verify that specimen source mappings on the GIM system are mapped to the appropriate HL7 table 0070 specimen source codes for each instrument. Results transmitted by the GIM need to use the HL7 table 0070 specimen source code that matches the HL7 table 0070 specimen source specified on VistA for the accession’s specimen (topography). On VistA an accession’s specimen is specified via the TOPOGRAPHY file (#61). The HL7 table 0070 mapping is via TOPOGRAPHY file (#61), LEDI HL7 (#.09). This is a pointer to LAB ELECTRONIC CODES file (#64.061). The HL7 table 0070 mapping is stored in HL7 ABBR field (#2). Refer to the GIM product support and documentation to configure this information for their specific product.

Sample message:

Msg \# 123, specimen source GLASS in message does not match accession's UID 1234567891 related topography code. See file \#61, TOPOGRAPHY entry \# 72.

Step 5: Activate the new HL7 Application(s) (LA7UIx) as needed using the HL7 package’s Application Edit \[HL EDIT APPL PARAM\] menu option. If the existing HL7 Application LA7LAB is not set to ACTIVE, it needs to be set to ACTIVE also.

Step 6: Activate the corresponding configuration (LA7UIx) from step 5 above in the LA7 MESSAGE PARAMETER file (#62.48). This can be done using the new Lab Universal Interface Setup \[LA7 UI SETUP\] menu option.

> **NOTE:** To provide for data entry consistency, results received via this interface are validated via the input transform for the data field used to store the test results. Test results received from an instrument that do not conform to the input transform for the related Lab Data Name will be rejected. Adjustment to the type of results transmitted by the instrument, modification of results via AUTO INSTRUMENT file (#62.4), CHEM TESTS subfile (#30), PARAM 1 field (#2) or modification of the input transform of the related Lab Data Name maybe required.

Results that fail this check will be reported with an error message

Sample message:

Msg \# 123 - The value 'xxx ' for field URINE YEAST in CHEM, HEM, TOX, RIA, SER, etc. SUB-FIELD in file LAB DATA is not valid.

# VistA LABORATORY UNIVERSAL INTERFACE (UI) HL v1.6 UPGRADE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PATCH LA\*5.2\*66 USER GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides users with step-by-step instructions and examples.

## Lab Universal Interface Setup \[LA7 UI SETUP\] option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Lab Universal Interface Setup \[LA7 UI SETUP\] option is located on the Lab Universal Interface Menu \[LA7 MAIN MENU\] menu. This new option allows sites to configure the LA7 MESSAGE PARAMETER file (#62.48) and AUTO INSTRUMENT file (#62.4). This option also allows editing of fields pertaining to Laboratory UI only.

Example: How to configure LA7 MESSAGE PARAMETER file (#62.48)

> LA7 MESSAGE PARAMETER file (#62.48)

> STATUS (#2)

> GRACE PERIOD FOR MESSAGES (#3)

> LOG ERRORS (#4)

> ALERT CONDITION: (#20)

Example: How to configure AUTO INSTRUMENT file (#62.4)

> AUTO INSTRUMENT file (#62.4)

> NAME (#.01)

> LOAD/WORK LIST (#3)

> ENTRY for LAGEN ROUTINE (#5)

> CROSS LINKED BY (#6)

> MESSAGE CONFIGURATION (#8)

> METHOD (#10)

> DEFAULT ACCESSION AREA (#11)

> OVERLAY DATA (#12)

> STORE REMARKS (#18)

> VENDOR CARD ADDRESS (#.02)

> SEND TRAY/CUP LOCATION (#95)

> AUTO DOWNLOAD (#98)

> TEST: (#30) (subfile \#62.41)

> TEST (#.01)

> PARAM 1 (#2)

> UI TEST CODE (#6)

> DOWNLOAD TO INSTRUMENT (#15)

> ACCESSION AREA (#7)

> SPECIMEN (#8)

> URGENCY(#9)

> NUMBER OF DECIMAL PLACES (#12)

> CONVERT RESULT TO REMARK (#13)

> ACCEPT RESULTS FOR THIS TEST (#14)

> IGNORE RESULTS NOT ORDERED (#16)

> REMOVE SPACES FROM RESULT (#17)

> STORE REMARKS (#18)

> REMARK PREFIX (#20)

> SITE NOTES DATE: (#107)

Example: How to use the new Lab Universal Interface Setup \[LA7 UI SETUP\] option.

Lab Universal Interface Setup

Select one of the following: \<ENTER\>

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

Select which file to setup: 1\<ENTER\> LA7 MESSAGE PARAMETER (#62.48)

Select LA7 MESSAGE PARAMETER CONFIGURATION: LA7UI1\<ENTER\>

STATUS: ACTIVE// \<ENTER\>

GRACE PERIOD FOR MESSAGES: 5// \<ENTER\>

LOG ERRORS: ON// \<ENTER\>

Select ALERT CONDITION: \<ENTER\>

Select one of the following: \<ENTER\>

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

Select which file to setup: 2\<ENTER\>

Select AUTO INSTRUMENT NAME: Vitros\<ENTER\>

NAME: Vitros//\<ENTER\>

LOAD/WORK LIST: CHEMISTRY//\<ENTER\>

ENTRY for LAGEN ROUTINE: Accession cross-reference//\<ENTER\>

CROSS LINKED BY: IDE//\<ENTER\>

MESSAGE CONFIGURATION: LA7UI1//\<ENTER\>

METHOD: VITROS//\<ENTER\>

DEFAULT ACCESSION AREA: CHEMISTRY//\<ENTER\>

OVERLAY DATA: YES//\<ENTER\>

STORE REMARKS: NO//\<ENTER\>

VENDOR CARD ADDRESS:\<ENTER\>

SEND TRAY/CUP LOCATION: no//\<ENTER\>

AUTO DOWNLOAD: YES//\<ENTER\>

Select TEST: ANION GAP//\<ENTER\>

TEST: ANION GAP//\<ENTER\>

PARAM 1:\<ENTER\>

UI TEST CODE: 1//\<ENTER\>

DOWNLOAD TO INSTRUMENT:\<ENTER\>

ACCESSION AREA:\<ENTER\>

SPECIMEN:\<ENTER\>

URGENCY:\<ENTER\>

NUMBER OF DECIMAL PLACES: \<ENTER\>

CONVERT RESULT TO REMARK: \<ENTER\>

ACCEPT RESULTS FOR THIS TEST: \<ENTER\>

IGNORE RESULTS NOT ORDERED: \<ENTER\>

REMOVE SPACES FROM RESULT: \<ENTER\>

STORE REMARKS: \<ENTER\>

REMARK PREFIX: \<ENTER\>

Select TEST: \<ENTER\>

Select SITE NOTES DATE:\<ENTER\>

Select AUTO INSTRUMENT NAME:^\<ENTER\>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary of terms relates to the VistA Laboratory Universal Interface HL v1.6 Upgrade software release.
| Glossary of Terms                     | Definitions                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ADPAC:                                | Automated Data Processing Coordinator                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Automatic Download:                   | Patient demographics and tests ordered are automatically formatted and transmitted either directly to a lab instrument or to a location where the instrument can query directly for the information. The automatic transmission usually occurs as soon as the accession number is created.                                                                                                                                                 |
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Checksum:                             | A specific calculation is performed on the contents of a message or packet of data. This checksum is sent with the data. The same calculation is performed by the receiver of the data. If they do not match, the data is rejected and the sender is requested to re-send.                                                                                                                                                                 |
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Communication Protocol:               | Computer program which defines the rules for data transfer between two devices or computers. The same protocol must be defined at both ends of the transmission. Some common examples of protocols are XON/XOFF, ACK/NAK, Kermit, TCP/IP. Some protocols are designed for modems and some for networks and others intended for devices connected to a single computer. They may have different purposes and varying degrees of complexity. |
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Driver:                               | Computer program which transports electronic information such as data or commands going between two computers or devices.                                                                                                                                                                                                                                                                                                                  |
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Generic Instrument Manager (GIM): | Vendor system communicating with VistA is called a Generic Interface Manager (GIM).                                                                                                                                                                                                                                                                                                                                                        |
| Glossary of Terms  | Definitions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HANDSHAKING:       | An electronic method of granting permission to transmit data between two computers or devices. This can be done via software using a pair of ASCII characters sent over the data send and receive lines such as ACK/NAK or can be done via separate wires specially dedicated to the purpose such as Clear to Send (CTS) and Ready to Send (RTS). Lab instrument interfaces may provide hardware communications, but the DHCP computer does not utilize these so if present, they are disables by directly connecting the corresponding pins in the instrument cable connection. |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HL7 Standard:      | Set of written rules and specifications for computer programmers to use to format medical information in a uniform way so it can be transported from one computer system to another.                                                                                                                                                                                                                                                                                                                                                                                             |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HL7 VistA:         | Package Software to manage, store and route HL7 formatted messages between VistA packages and other computer systems. It handles low level handshaking and physical delivery and receipt of messages between systems.                                                                                                                                                                                                                                                                                                                                                            |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HL7 Lab Interface: | Software to encode data into the HL7 format and to decode HL7 messages into lab global for use by standard DHCP lab options.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IIS:               | Information Infrastructure Systems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Lab Data Name:     | Field located within the LAB DATA file (#63), CHEM, HEM, TOX, RIA, SER, etc. multiple (#4) which specifies the storage location of a specific test result and the data characteristics associated with the result.                                                                                                                                                                                                                                                                                                                                                               |
| Glossary of Terms | Definitions                                                                      |
|-----------------------|--------------------------------------------------------------------------------------|
|                       |                                                                                      |
| LIM:              | Laboratory Information Manager                                                       |
|                       |                                                                                      |
| MSA:              | Message acknowledgment                                                               |
|                       |                                                                                      |
| MSH:              | Message header                                                                       |
|                       |                                                                                      |
| OBR:              | Observational Request segment                                                        |
|                       |                                                                                      |
| OBX:              | Result segment                                                                       |
|                       |                                                                                      |
| ORC:              | Common order segment                                                                 |
|                       |                                                                                      |
| ORM:              | Order message type                                                                   |
|                       |                                                                                      |
| ORR:              | Order response message                                                               |
|                       |                                                                                      |
| ORU:              | Observational results unsolicited message type                                       |
|                       |                                                                                      |
| PID:              | Patient identification segment                                                       |
|                       |                                                                                      |
| PV1:              | Patient Visit Segment                                                                |
|                       |                                                                                      |
| TCP/IP:           | A network protocol for communicating to multiple systems via a single physical line. |
|                       |                                                                                      |
| UI:               | Universal Interface                                                                  |
