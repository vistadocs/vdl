---
title: "LA*5.2*17/LR*5.2*65 Laboratory: Universal Interface Installation Guide"
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*17
group_key: "LA:LA:5.2"
file_numbers: 
  - 62
  - 68
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - message
  - contents
  - dhcp
  - routine
  - laboratory
  - instrument
  - interface
  - number
  - class
page_count: 0
word_count: 16699
section_count: 17
table_count: 31
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: October 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labuig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labuig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

![](la-5-2-17-lr-5-2-65-laboratory-universal-interface-installation-guide/001.png)

LABORATORY UNIVERSAL INTERFACEPatch LA\*5.2\*17Patch LR\*5.2\*65

March 30, 1996

Information Resource Management Field Office

Birmingham, Alabama

Preface

The Laboratory Universal Interface patches LA\*5.2\*17 and LR\*5.2\*65 are designed to make the process of interfacing automated instrument easier, faster, and more reliable.

This manual is intended to be used as an installation and setup guide for Information Resource Management (IRM). This manual will aid Laboratory Managers, Automated Data Processing Application Coordinator (ADPAC) and staff in implementing the Laboratory Universal Interface (UI) system for automated instruments.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- DHCP Health Level Seven (HL7) Version 1.6, October 1995, Albany Information Resource Management Field Office (IRMFO), Troy, New York
- Health Level Seven (HL7), Version 2.2®, 1994 Standard
- Documentation from <span class="mark">REDACTED</span>

## Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [References](#references)
  - [Acknowledgments](#acknowledgments)
- [Introduction](#introduction)
  - [Laboratory UI Description](#laboratory-ui-description)
  - [System Instrument Setup](#system-instrument-setup)
  - [Data Flow](#data-flow)
- [Installation Notes](#installation-notes)
  - [Pre-Installation Information](#pre-installation-information)
    - [Required Packages](#required-packages)
    - [Patch Namespace](#patch-namespace)
  - [Installation Procedures](#installation-procedures)
  - [Post-Installation Instructions](#post-installation-instructions)
    - [Non-DHCP Application Parameter Enter/Edit](#non-dhcp-application-parameter-enteredit)
    - [Initiating Background Task](#initiating-background-task)
    - [Start/Stop Log of HL7 Transmissions](#startstop-log-of-hl7-transmissions)
    - [Activate/Inactivate Application](#activateinactivate-application)
    - [Populated DHCP HL7 Files](#populated-dhcp-hl7-files)
    - [Populated Laboratory Universal Interface Files](#populated-laboratory-universal-interface-files)
- [Technical Notes](#technical-notes)
  - [Planning Considerations](#planning-considerations)
    - [Location/Cabling](#locationcabling)
    - [Communications](#communications)
    - [Driver Availability](#driver-availability)
    - [Data Formats](#data-formats)
    - [Implementation Considerations](#implementation-considerations)
    - [Bidirectional Considerations](#bidirectional-considerations)
    - [Support and Troubleshooting](#support-and-troubleshooting)
    - [GIM Backup](#gim-backup)
    - [Checklist for Laboratory Universal Interface Implementation](#checklist-for-laboratory-universal-interface-implementation)
    - [Interface Data Form](#interface-data-form)
  - [Routine Descriptions](#routine-descriptions)
    - [New Routines](#new-routines)
    - [Modified Routines for Laboratory UI Patch LA\5.2\17](#modified-routines-for-laboratory-ui-patch-la5217)
    - [Modified Routines for Laboratory UI Patch LR\5.2\65](#modified-routines-for-laboratory-ui-patch-lr5265)
    - [Init Routines](#init-routines)
  - [Files](#files)
    - [New Files](#new-files)
    - [Modified Files and Fields](#modified-files-and-fields)
    - [Exported Options](#exported-options)
    - [Cross-reference](#cross-reference)
    - [Archiving and Purging](#archiving-and-purging)
    - [Callable Routines](#callable-routines)
    - [External Relations](#external-relations)
    - [Internal Relations](#internal-relations)
    - [All options of the Laboratory UI are stand alone.](#all-options-of-the-laboratory-ui-are-stand-alone)
    - [Package-wide Variables](#package-wide-variables)
- [Universal Identification Number (UID) Specifications](#universal-identification-number-uid-specifications)
    - [Parameters](#parameters)
- [HL7 Standard and DHCP HL7 Package](#hl7-standard-and-dhcp-hl7-package)
  - [Overview](#overview)
    - [HL7](#hl7)
    - [DHCP HL7 Package](#dhcp-hl7-package)
    - [Lower Level Protocols](#lower-level-protocols)
    - [DHCP Interface to the HL7 Protocol](#dhcp-interface-to-the-hl7-protocol)
    - [DHCP HL7 Routines](#dhcp-hl7-routines)
    - [Background Job](#background-job)
- [Messages](#messages)
  - [Segments](#segments)
    - [MSA -Message Acknowledgment](#msa-message-acknowledgment)
    - [MSH - Message Header](#msh-message-header)
    - [OBR - Observation Request](#obr-observation-request)
    - [Notes and Comments](#notes-and-comments)
    - [OBX - Observation Results](#obx-observation-results)
    - [ORC - Common Order](#orc-common-order)
    - [PV1 - Patient Visit](#pv1-patient-visit)
    - [PID - Patient ID](#pid-patient-id)
  - [Message Types](#message-types)
  - [HL7 Messages](#hl7-messages)
  - [## ## ## ReseultNet Configuration](#reseultnet-configuration)
    - [HL7 Host Format Definition](#hl7-host-format-definition)
    - [### HL7 Host Protocol](#hl7-host-protocol)
    - [Operational](#operational)
The Laboratory Universal Interface (UI) is designed to make the process of interfacing automated instrument easier, faster, and more reliable. Laboratory UI uses the standard messaging protocol Health Level Seven (HL7) to communicate with all instruments. HL7 is a standard developed by health care information systems professionals to simplify the communications between computer systems that must exchange information. HL7 was adopted by Decentralized Hospital Computer Program (DHCP) as the primary communications protocol for messaging between systems and even between applications on the same system. Information contained in the HL7 Standard protocol is not repeated here; therefore, anyone wishing to interface with the DHCP Laboratory package should become familiar with the HL7 protocol version 2.2. For an overview of the HL7 Standard and DHCP HL7 package see the HL7 Standard and DHCP HL7 Package section of this manual.
The laboratory technologist sees very little change between the Laboratory UI and the traditional interface system. After the Laboratory Information Manager (LIM) or ADPAC sets up the files and installs the new hardware, the technologist can accession, build Load/Worklists, download, and verify the results as usual. The benefit of using the Laboratory UI is that almost any instrument by any manufacturer can be interfaced quickly and dependably, in unidirectional or bidirectional mode. Interfacing is only subject to the limitations of the instrument.
The key component of the Laboratory UI is a new piece of equipment that performs the protocol conversion between the instrument and DHCP. Since all the instrument manufacturers have not conformed to HL7 Standard, a commercial product is used to convert all the different message types into HL7. The commercial protocol converter puts all the messages into HL7 format, enabling the work required on the DHCP system to be greatly simplified. All messages from any instrument now look the same, so only one interface routine set needs to be used.
With the Laboratory UI, laboratory managers have much more flexibility in choosing the instrumentation that meets requirements, without concern that it might not be interfaced to DHCP. The time required to get a new instrument working could be as little as two days, and generally no more than two months. The time will depend on how quickly the programmer for the commercial protocol converter can write a new protocol. The current method of interfacing instruments (DHCP programmers creating a separate interface for each instrument either through the LSI or direct connect) will continue to work alongside the Laboratory UI for those managers that want to phase-in the Laboratory UI system. However, an instrument may be connected to only one method of interfacing at a time. Switching from one methodology to another for testing purposes is possible.
Software functionality that has been incorporated into the Laboratory HL7 interface is the Universal Identification (UID) number for specimen identification. This functionality gives sites the ability to have a totally unique number attached to every specimen.
This version of the Laboratory UI software will not accept Microbiology subscript data.

## Laboratory UI Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory UI system uses commercial hardware and software products to connect automated instruments to DHCP, very similar to the traditional Large Scale Integrator (LSI). Several vendors have a product available for this purpose. In this document, this product is referred to generically as the Generic Interface Manager (GIM). All the instruments connect to the GIM through an appropriate protocol used by the GIM. This protocol may be the same as the one used for the LSI previously used by the laboratory software, but it is not limited to a single protocol. The GIM then connects to DHCP using one connection configured as a standard device, again analogous to the LSI.

The next two pages show the System Instrument Setup and the Data Flow for

Laboratory UI.

## System Instrument Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-17-lr-5-2-65-laboratory-universal-interface-installation-guide/002.png)

## Data Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-17-lr-5-2-65-laboratory-universal-interface-installation-guide/003.png)

# Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Universal Interface software requires two patches LA\*5.2\*17 and LR\*5.2\*65. Patch LA\*5.2\*17 must be installed and the Numeric Identifier field (#.091) of the ACCESSION file (#68) must be populated before installing patch LR\*5.2\*65. Patch LR\*5.2\*65 references Field \# .091 to create the Universal ID.

Patch LR\*5.2\*65 can be obtained from the Patch Module. This document does not cover the installation of patch LR\*5.2\*65.

### Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing Laboratory UI patch LA\*5.2\*17, the following DHCP packages

must be installed.

|                               |                              |
|-------------------------------|------------------------------|
| Package                   | Minimum Version Required |
| Laboratory                    | 5.2                          |
| DHCP Health Level Seven (HL7) | 1.6                          |
| Kernel                        | 8.0                          |
| VA FileMan                    | 21                           |
| Tool Kit                      | 7.3                          |
|                               |                              |

This software also requires a vendor specific Generic Interface Manager (GIM).Refer to the Laboratory UI Description section of this manual for more information on the GIM.

> **NOTE:** Refer to DHCP HL7 Version 1.6 Installation Guide, Technical and User Manuals for additional information on the HL7 options and communications setup.

### Patch Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LA7 is the namespace assigned to Laboratory UI.

Resource Requirements

The LA 7 MESSAGE PARAMETER file (#62.48) and LA7 MESSAGE LOG BULLETINS file (#62.485) take up minimal space. LA7 MESSAGE QUEUE file (#62.49) with 9455 entries will take up approximately 14,125 blocks. All of this data is stored in the ^LAHM global.

> **NOTE:** Patch LA\*5.2\*17 must be installed before Patch LR\*5.2\*65.

## Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory users must be off the system during installation of Laboratory UI. Sites are encouraged to backup the system before installation.

1.  All systems:
- Unless your site has installed DHCP Laboratory Universal Interface software, there are no routines to unmap.
- Global Placement

> The new global ^LAHM must be placed in the appropriate translation and set to null.

- The HL7 Initiate Background Task job must be stopped.
- No journaling required.
2.  a\. Sign into the UCI where you plan to install the Laboratory UI patch

> LA\*5.2\*17.

> b\. Install the LA7\* routines and LA7 inits from the PackMan message.

Example: Installation

Subj: LA\*5.2\*17 LAB MESSAGING \[#8\] 26 Feb 96 10:03 6224 Lines

From: LABUSER, ONE in 'IN' basket. Page 1

------------------------------------------------------------------------------

Select MESSAGE Action: IGNORE (in IN basket)// X

Select PackMan function: INSTALL

> 1 INSTALL SELECTED ROUTINE(S)

> 2 INSTALL/CHECK MESSAGE

CHOOSE 1-2: 2

> **WARNING:** Installing this message will cause a permanent update of globals

and routines. Do you really want to do this? NO// Y

Shall I preserve what is on disk in a separate back-up message ? YES// \<RET\>

Subject: Backup of LA\*5.2\*17 Lab Messaging

Send mail to: LABUSER, ONE // \<RET\>

> Select basket to send to: IN// \<RET\>

And send to: \<RET\>.

PackMan backup message built with subject Backup of LA\*5.2\*17 Lab Messaging

Routine LA7ADL is not on the disk.

Routine LA7ADL1 is not on the disk.

Routine LA7HL7 is not on the disk.

Routine LA7HLP is not on the disk.

Routine LA7IN001 is not on the disk.

Routine LA7IN002 is not on the disk.

Routine LA7IN003 is not on the disk.

Routine LA7IN004 is not on the disk.

Routine LA7IN005 is not on the disk.

Routine LA7IN006 is not on the disk.

Routine LA7IN007 is not on the disk.

Routine LA7IN008 is not on the disk.

Routine LA7IN009 is not on the disk.

Routine LA7IN00A is not on the disk.

Routine LA7IN00B is not on the disk.

Routine LA7IN00C is not on the disk.

Routine LA7IN00D is not on the disk.

Routine LA7IN00E is not on the disk.

Routine LA7IN00F is not on the disk.

Routine LA7IN00G is not on the disk.

Routine LA7IN00H is not on the disk.

Routine LA7IN00I is not on the disk.

Routine LA7IN00J is not on the disk.

Routine LA7IN00K is not on the disk.

Routine LA7IN00L is not on the disk.

Routine LA7IN00M is not on the disk.

Routine LA7IN00N is not on the disk.

Routine LA7IN00O is not on the disk.

Routine LA7IN00P is not on the disk.

Routine LA7IN00Q is not on the disk.

Routine LA7IN00R is not on the disk.

Routine LA7IN00S is not on the disk.

Routine LA7IN00T is not on the disk.

Routine LA7IN00U is not on the disk.

Routine LA7IN00V is not on the disk.

Routine LA7IN00W is not on the disk.

Routine LA7IN00X is not on the disk.

Routine LA7IN00Y is not on the disk.

Routine LA7IN00Z is not on the disk.

Routine LA7IN010 is not on the disk.

Routine LA7IN011 is not on the disk.

Routine LA7INIS is not on the disk.

Routine LA7INIT is not on the disk.

Routine LA7INIT1 is not on the disk.

Routine LA7INIT2 is not on the disk.

Routine LA7INIT3 is not on the disk.

Routine LA7INIT4 is not on the disk.

Routine LA7INIT5 is not on the disk.

Routine LA7LOG is not on the disk.

Routine LA7NTEG is not on the disk.

Routine LA7POST is not on the disk.

Routine LA7UID is not on the disk.

Routine LA7UID1 is not on the disk.

Routine LA7UID2 is not on the disk.

Routine LA7UIIN is not on the disk.

Routine LA7UIIN1 is not on the disk.

Routine LA7UIIN2 is not on the disk.

Routine LA7UTIL is not on the disk.

Line 3 Message \#6535 Unloading Routine ROU LA7ADL

Line 77 Message \#6535 Unloading Routine ROU LA7ADL1

Line 114 Message \#6535 Unloading Routine ROU LA7HL7

Line 186 Message \#6535 Unloading Routine ROU LA7HLP

Line 318 Message \#6535 Unloading Routine ROU LA7IN001

Line 476 Message \#6535 Unloading Routine ROU LA7IN002

Line 572 Message \#6535 Unloading Routine ROU LA7IN003

Line 712 Message \#6535 Unloading Routine ROU LA7IN004

Line 850 Message \#6535 Unloading Routine ROU LA7IN005

Line 990 Message \#6535 Unloading Routine ROU LA7IN006

Line 1126 Message \#6535 Unloading Routine ROU LA7IN007

Line 1268 Message \#6535 Unloading Routine ROU LA7IN008

Line 1416 Message \#6535 Unloading Routine ROU LA7IN009

Line 1544 Message \#6535 Unloading Routine ROU LA7IN00A

Line 1694 Message \#6535 Unloading Routine ROU LA7IN00B

Line 1854 Message \#6535 Unloading Routine ROU LA7IN00C

Line 2004 Message \#6535 Unloading Routine ROU LA7IN00D

Line 2160 Message \#6535 Unloading Routine ROU LA7IN00E

Line 2172 Message \#6535 Unloading Routine ROU LA7IN00F

Line 2326 Message \#6535 Unloading Routine ROU LA7IN00G

Line 2420 Message \#6535 Unloading Routine ROU LA7IN00H

Line 2480 Message \#6535 Unloading Routine ROU LA7IN00I

Line 2584 Message \#6535 Unloading Routine ROU LA7IN00J

Line 2758 Message \#6535 Unloading Routine ROU LA7IN00K

Line 2818 Message \#6535 Unloading Routine ROU LA7IN00L

Line 3012 Message \#6535 Unloading Routine ROU LA7IN00M

Line 3116 Message \#6535 Unloading Routine ROU LA7IN00N

Line 3232 Message \#6535 Unloading Routine ROU LA7IN00O

Line 3354 Message \#6535 Unloading Routine ROU LA7IN00P

Line 3502 Message \#6535 Unloading Routine ROU LA7IN00Q

Line 3658 Message \#6535 Unloading Routine ROU LA7IN00R

Line 3816 Message \#6535 Unloading Routine ROU LA7IN00S

Line 3966 Message \#6535 Unloading Routine ROU LA7IN00T

Line 4132 Message \#6535 Unloading Routine ROU LA7IN00U

Line 4294 Message \#6535 Unloading Routine ROU LA7IN00V

Line 4434 Message \#6535 Unloading Routine ROU LA7IN00W

Line 4596 Message \#6535 Unloading Routine ROU LA7IN00X

Line 4752 Message \#6535 Unloading Routine ROU LA7IN00Y

Line 4896 Message \#6535 Unloading Routine ROU LA7IN00Z

Line 4916 Message \#6535 Unloading Routine ROU LA7IN010

Line 5090 Message \#6535 Unloading Routine ROU LA7IN011

Line 5124 Message \#6535 Unloading Routine ROU LA7INIS

Line 5171 Message \#6535 Unloading Routine ROU LA7INIT

Line 5221 Message \#6535 Unloading Routine ROU LA7INIT1

Line 5263 Message \#6535 Unloading Routine ROU LA7INIT2

Line 5294 Message \#6535 Unloading Routine ROU LA7INIT3

Line 5366 Message \#6535 Unloading Routine ROU LA7INIT4

Line 5391 Message \#6535 Unloading Routine ROU LA7INIT5

Line 5412 Message \#6535 Unloading Routine ROU LA7LOG

Line 5510 Message \#6535 Unloading Routine ROU LA7NTEG

Line 5582 Message \#6535 Unloading Routine ROU LA7POST

Line 5612 Message \#6535 Unloading Routine ROU LA7UID

Line 5652 Message \#6535 Unloading Routine ROU LA7UID1

Line 5716 Message \#6535 Unloading Routine ROU LA7UID2

Line 5844 Message \#6535 Unloading Routine ROU LA7UIIN

Line 5908 Message \#6535 Unloading Routine ROU LA7UIIN1

Line 6004 Message \#6535 Unloading Routine ROU LA7UIIN2

Line 6084 Message \#6535 Unloading Routine ROU LA7UTIL

Line 6197 Message \#6535 Unloading Routine ROU LADOWN

Line 6255 Message \#6535 Unloading Routine ROU LAGEN

Select PackMan function: \<RET\>

Select MESSAGE Action: IGNORE (in IN basket)// \<RET\>

Ignored

Run Integrity Routines

> **NOTE:** - Please insure that the variables DUZ and DUZ(0) are defined before attempting initialization. The initialization will abort if DUZ is not set to a valid user number and DUZ(0) does not equal "@".

- The variables DT, DTIME, and U must be defined.
- Call your IRM Field Office if any routines fail the integrity routine.

\>D ^LA7NTEG

Checksum routine created on 2960227.130055 by KERNEL V7.3

LA7ADL ok LA7INIT2 ok

LA7ADL1 ok LA7INIT3 ok

LA7HL7 ok LA7LOG ok

LA7HLP ok LA7POST ok

LA7IN001 ok LA7UID ok

LA7IN002 ok LA7UID1 ok

LA7IN003 ok LA7UID2 ok

LA7IN004 ok LA7UIIN ok

LA7IN005 ok LA7UIIN1 ok

LA7IN006 ok LA7UIIN2 ok

LA7IN007 ok LA7UTIL ok

LA7IN008 ok LADOWN1...ok

LA7IN009 ok LAGEN.....ok

LA7IN00A ok

LA7IN00B ok

LA7IN00C ok

LA7IN00D ok

LA7IN00E ok

LA7IN00F ok

LA7IN00G ok

LA7IN00H ok

LA7IN00I ok

LA7IN00J ok

LA7IN00K ok

LA7IN00L ok

LA7IN00M ok

LA7IN00N ok

LA7IN00O ok

LA7IN00P ok

LA7IN00Q ok

LA7IN00R ok

LA7IN00S ok

LA7IN00T ok

LA7IN00U ok

LA7IN00V ok

LA7IN00W ok

LA7IN00X ok

LA7IN00Y ok

LA7IN00Z ok

LA7IN010 ok

LA7IN011 ok

3.  Run the LA7INIT routines to initialize Laboratory files

\>D ^LA7INIT

This version (#5.21) of 'LA7INIT' was created on 21-FEB-1996

> (at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.21.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

> 61 TOPOGRAPHY FIELD (Partial Definition)

> **NOTE:** You already have the 'TOPOGRAPHY FIELD' File.

Shall I write over the existing Data Definition? YES// \<RET\>

> 62.05 URGENCY (Partial Definition)

> **NOTE:** You already have the 'URGENCY' File.

Shall I write over the existing Data Definition? YES// \<RET\>

> 62.4 AUTO INSTRUMENT

> **NOTE:** You already have the 'AUTO INSTRUMENT' File.

Shall I write over the existing Data Definition? YES// \<RET\>

48. LA7 MESSAGE PARAMETER

> 62.485 LA7 MESSAGE LOG BULLETINS (including data)

I will OVERWRITE your data with mine.

> 62.49 LA7 MESSAGE QUEUE

> 68 ACCESSION

> **NOTE:** You already have the 'ACCESSION' File.

Shall I write over the existing Data Definition? YES// \<RET\>

> SHALL I WRITE OVER FILE SECURITY CODES? No// \<RET\> (No)

> **NOTE:** This package also contains INPUT TEMPLATES

> SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? Yes//

\<RET\> (Yes)

> **NOTE:** This package also contains OPTIONS

> SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? Yes// \<RET\> (Yes)

ARE YOU SURE EVERYTHING'S OK? No// Y (Yes)

...HMMM, LET ME THINK ABOUT THAT A

MOMENT.......................................

..........................................

'LA7 APPLICATION PARAMETER FILE' Option Filed

'LA7 MAIN MENU' Option Filed

'LA7 PRINT 0070 TABLE' Option Filed

'LA7 PRINT LAB UI ERROR LOG' Option Filed

'LA7 UPDATE MESSAGE PARAMETER' Option Filed.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\>\>\>Adding HL7 DHCP APPLICATION file entry for LA AUTO INST...

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once installation is completed perform the following steps:

1.  Delete LA7\* and LA7POST routines
2.  . MSM systems
- Move LA7\* routines to other servers.
- Sites running Kurzwiel will need to setup another NULL DEVICE with a different \$I with parameters as follows.

> **NOTE:** Please respond with site specific information when applicable.

Select Port Number: 413

Port Types:

> 1 - PC CONSOLE

> 2 - Serial Communication Ports (COM)

> 3 - Parallel Printers (LPT)

> 4 - ARNET Multiport Card

> 5 - Quadport-AT Card

> 6 - AST 4 Port/XN Card

> 7 - MCC Card

> 8 - Console Window Devices

> 9 - ARNET SmartPort card

> 10 - Bios LPT device

> 11 - LAT Port - connection to a specific port and server

> 12 - DigiBoard multiport card

Select Option \<LAT Port\>: \<RET\> LAT Port - connection to a

specific port and server

Server Name \<EQN17\>: \<RET\>

Port Name \<PORT_43\>: \<RET\>

Tied Terminal Index \<\>: \<RET\>

Terminal Line Width \<132\>: \<RET\> 132

Translate name \<\>: \<RET\>

Select Echo Option:

> 1 - ON

> 2 - OFF

Select Option \<ON\>: \<RET\> ON

Escape Processing Mode:

> 1 - OFF

> 2 - ON

Select Option \<OFF\>: \<RET\> OFF

8-bit Mode:

> 1 - OFF

> 2 - ON

Select Option \<OFF\>: \<RET\> OFF

Pass All Mode:

> 1 - OFF

> 2 - ON

Select Option \<OFF\>: \<RET\> OFF

Line Feed Suppression:

> 1 - OFF

> 2 - ON

Select Option \<OFF\>: \<RET\> OFF

Upper-Case Setup:

> 1 - OFF

> 2 – ON

Select Option \<OFF\>: \<RET\> OFF

Select 'Output-Only' Mode:

> 1 - OFF (Input/Output Device)

> 2 - ON (Output-only device)

Select Option \<OFF\>: \<RET\> OFF (Input/Output Device)

Login Allowed:

> 1 - YES

> 2 – NO

Select Option \<NO\>: \<RET\> NO

CRT Mode:

> 1 - ON

> 2 - OFF

Select Option \<ON\>: \<RET\> ON

Set up the DEVICE file as follows:

Select DEVICE NAME: \<RET\> NULL

> 1 NULL DEVICE IRM 413 PSA

> 2 NULL DEVICE RAD/NULL 434 PSA

> 3 NULL1 NT SYSTEM 46 GSA

CHOOSE 1-3: 1

NAME: NULL DEVICE// \<RET\>

LOCATION OF TERMINAL: IRM// \<RET\>

Select MNEMONIC: \<RET\>

LOCAL SYNONYM: \<RET\>

\$I: 413// \<RET\>

VOLUME SET(CPU): PSA// \<RET\>

SIGN-ON/SYSTEM DEVICE: \<RET\>

TYPE: TERMINAL// \<RET\>

SUBTYPE: P-OTHER// \<RET\>

ASK DEVICE: YES// \<RET\>

ASK PARAMETERS: NO// \<RET\>

ASK HOST FILE: \<RET\>

ASK HFS I/O OPERATION: \<RET\>

QUEUING: \<RET\>

OUT-OF-SERVICE DATE: \<RET\>

NEAREST PHONE: \<RET\>

KEY OPERATOR: \<RET\>

\*MARGIN WIDTH: 255// \<RET\>

\*FORM FEED: \#// \<RET\>

\*PAGE LENGTH: 256// \<RET\>

SUPPRESS FORM FEED AT CLOSE: \<RET\>

\*BACK SPACE: \$C(8)// \<RET\>

SECURITY: \<RET\>

CLOSEST PRINTER: \<RET\>

FORM CURRENTLY MOUNTED: \<RET\>

OPEN PARAMETERS: \<RET\>

CLOSE PARAMETERS: \<RET\>

USE PARAMETERS: \<RET\>

PRE-OPEN EXECUTE: v

POST-CLOSE EXECUTE: \<RET\>

MICOM PRINTER CONTENTION PORT: \<RET\>

MODEM: \<RET\>

PRIORITY AT RUN TIME: \<RET\>

TASKMAN PRINT A HEADER PAGE: \<RET\>

PASSWORD: \<RET\>

SLAVED FROM DEVICE: \<RET\>

\*HUNT GROUP: V02// \<RET\>

Select HUNT GROUP DEVICE: NULL DEVICE// \<RET\>

HUNT GROUP DEVICE: NULL DEVICE// \<RET\>

Select HUNT GROUP DEVICE: \<RET\>

AUTO DESPOOL: \<RET\>

MSM sites: Set up HUNT GROUP DEVICES:

INPUT TO WHAT FILE: DEVICE

EDIT WHICH FIELD: ALL// HUNT GROUP DEVICE

> EDIT WHICH HUNT GROUP DEVICE SUB-FIELD: // ALL

THEN EDIT FIELD: \<RET\>

Select DEVICE NAME: NULL

> 1 NULL DEVICE IRM 413 PSA

> 2 NULL DEVICE RAD/NULL 434 PSA

CHOOSE 1-2: 1

Select HUNT GROUP DEVICE: NULL DEVICE

> 1 NULL DEVICE IRM 413 PSA

> 2 NULL DEVICE RAD/NULL 434 PSA

CHOOSE 1-2: 1

> HUNT GROUP DEVICE ORDER: 1// \<RET\>

Select HUNT GROUP DEVICE: NULL DEVICE IRM 413 PSA

> .OK? YES// N (NO)

> NULL DEVICE RAD/NULL 434 PSA

> HUNT GROUP DEVICE ORDER: 2// \<RET\>

Select HUNT GROUP DEVICE: \<RET\>

Select DEVICE NAME: NULL

> 1 NULL DEVICE IRM 413 PSA

> 2 NULL DEVICE RAD/NULL 434 PSA

CHOOSE 1-2: 3

Select HUNT GROUP DEVICE: NULL DEVICE

> 1 NULL DEVICE IRM 413 PSA

> 2 NULL DEVICE RAD/NULL 434 PSA

CHOOSE 1-2: 2

> HUNT GROUP DEVICE ORDER: 1//

Select HUNT GROUP DEVICE: NULL DEVICE IRM 434 PSA

> .OK? YES// N (NO)

> NULL DEVICE IRM 413 PSA

> HUNT GROUP DEVICE ORDER: 2// \<RET\>

Select HUNT GROUP DEVICE: \<RET\>

The first NULL DEVICE points to the second.

The second NULL DEVICE points to the first.

All systems: Add the Laboratory Universal Interface Menu \[LA7 Main Menu\] for

the appropriate staff.

3.  The HL7 software must be installed and implemented prior to running Laboratory UI. If a previous version of DHCP HL7 V. 1.6 is installed and running on your system do the following:
- Active and pending HLLP jobs must be stopped and restarted using the DHCP HL7 V. 1.5 option Initiate Background Task.
4.  Setup DHCP HL7 Files

From the DHCP HL7 V. 1.6 MAIN MENU access V. 1.5 options. Use the HL7 V. 1.5

options to setup HL7 files and initiate background task. Additional options exist

allowing HL7 transmissions to be logged and purged.

> **NOTE:** - Where appropriate, use site specific entries for the following files.

- In the examples, the XXX means that site specific data is displayed.

### Non-DHCP Application Parameter Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Non-DHCP Application Parameter Enter/Edit option to:

- Enter non-DHCP applications (applications that will be communicating with the DHCP system via the HL7 Protocol) in the HL7 NON-DHCP APPLICATION PARAMETER file (#770).
- Enter or edit parameters associated with non-DHCP applications.
- Delete an application from the HL7 NON-DHCP APPLICATION PARAMETER file (#770).

> **NOTE:** The applications entered in this file are referred to as non-DHCP applications simply as a way of distinguishing them from the DHCP system with which they will be communicating. These non-DHCP applications could also be other DHCP applications (e.g., Laboratory UI).

Example: Non-DHCP Application Parameter Enter/Edit

Select OPTION NAME: HL7 Main Menu

> 1 V1.5 OPTIONS ...

> 2 V1.6 OPTIONS ...

> 3 Activate/Inactivate Application

> 4 Print/Display Menu ...

> 5 Purge Message Text File Entries

Select HL7 Main Menu Option: 1 V1.5 OPTIONS

> 1 Non-DHCP Application Parameter Enter/Edit

> 2 Initiate Background Task

> 3 Start/Stop Log of HL7 Transmissions

Select V1.5 OPTIONS Option: 1 Non-DHCP Application Parameter Enter/Edit

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: ?

> Answer with HL7 NON-DHCP APPLICATION PARAMETER NAME

Choose from:

> EDR-MAS RCP EDR-MAS-DHCP

> IVM CENTER XXX XXX IVM

> LAB INTERFACE XXX YOUR SITE LA7 AUTO INST

> You may enter a new HL7 NON-DHCP APPLICATION PARAMETER, if you wish The name of the application from/to which HL7 messages may be transmitted by the DHCP system. Answer must be 3-15 characters in length and must be unique.

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: LAB INTERFACE XXX

YOUR SITE LA7 AUTO INST

NAME: LAB INTERFACE// \<RET\>

NON-DHCP FACILITY NAME: // *(Enter sites generic interface manager (GIM))*

DHCP STATION NUMBER: // *(Enter sites station number)*

MAXIMUM BLOCK SIZE: // *(Enter maximum block size)*

NUMBER OF RETRIES: // (*Enter number of times to attempt retransmission)*

HL7 DEVICE: *(Enter your HL7 device name)*

HL7 VERSION NUMBER: // *(Enter the version of HL7 your vendor GIM is using)*

DHCP APPLICATION: LA7 AUTO INST// \<RET\>

LOWER LEVEL PROTOCOL TIMEOUT: 5// \<RET\>

MAIL GROUP: \<RET\>

HL7 PROCESSING ID: // *(This field can be used to turn on debugging. Turn off after*

> *debugging is completed to stop producing large amount of data in the ^TMP.)*

PURPOSE: \<RET\>

1\> \<RET\>

### Initiating Background Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to create a background task to start up the lower level protocol routine for the Laboratory UI.

Example: Initiate Background Task

Select HL7 Main Menu Option: 1 V1.5 OPTIONS

1 Non-DHCP Application Parameter Enter/Edit

2 Initiate Background Task

3 Start/Stop Log of HL7 Transmissions

Select V1.5 OPTIONS Option: 2 Initiate Background Task

> **NOTE:** You must select a Non-DHCP Application for which an HL7 Device has been

defined.

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: ?

Answer with HL7 NON-DHCP APPLICATION PARAMETER NAME

Choose from:^

### Start/Stop Log of HL7 Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Start/Stop Log of HL7 Transmission option is a diagnostic tool. Use this option to:

- Test the HL7 interface when the HL7 Hybrid Lower Level Protocol is used as the communication protocol.
- Check that HL7 messages are being properly exchanges with a particular non-DHCP application.

Example: Start/Stop Log of HL7 Transmissions

Select HL7 Main Menu Option: 1 V1.5 OPTIONS

> 1 Non-DHCP Application Parameter Enter/Edit

> 2 Initiate Background Task

> 3 Start/Stop Log of HL7 Transmissions

Select V1.5 OPTIONS Option: 3 Start/Stop Log of HL7 Transmissions

Select the Non-DHCP Application for which you wish to start/stop the HL7 log of transmissions.

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: ?

Answer with HL7 NON-DHCP APPLICATION PARAMETER NAME

Choose from:

> EDR-MAS RCP EDR-MAS-DHCP

> IVM CENTER XXX XXX IVM

> LAB INTERFACE XXX YOUR SITE LA7 AUTO INST

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: LAB INTERFACE XXX YOUR SITE LA AUTO INST

You must define an HL7 Device for this Non-DHCP Application before you can start the log.

HL7 DEVICE: (The name of the device (must exactly match a name in the DHCP Device file)that will be used to send/receive HL7 messages to this non-DHCP application. Answer must be 1-30 characters in length.)

Do you want to purge existing log entries? Yes// \<RET\>

### Activate/Inactivate Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to activate or inactivate a specific DHCP application that exists in the HL7 APPLICATION PARAMETER FILE (#771). Your entry in this option determines if a DHCP application is communicating with a non-DCHP application using the HL7 protocol. An application must be active to send and receive messages.

Example: Activate/Inactivate Application

Select OPTION NAME: HL7 Main Menu

> 1 V1.5 OPTIONS ...

> 2 V1.6 OPTIONS ...

> 3 Activate/Inactivate Application

> 4 Print/Display Menu ...

> 5 Purge Message Text File Entries

Select HL7 Main Menu Option: 3 Activate/Inactivate Application

Select HL7 APPLICATION PARAMETER NAME: ?

Answer with HL7 APPLICATION PARAMETER NAME

Choose from:

EDR-MAS ACTIVE

EDR-MAS-DHCP ACTIVE

IVM ACTIVE

IVM CENTER ACTIVE

LA AUTO INST INACTIVE

RADIOLOGY INACTIVE

Select HL7 APPLICATION PARAMETER NAME: LA AUTO INST INACTIVE

ACTIVE/INACTIVE: ACTIVE// \<RET\>

Populate Laboratory Files with HL7 Codes

The following are examples of how to populate the Laboratory files with HL7 codes using the FileMan option Enter or Edit File Entries.

> **NOTE:** - Field .091 of the ACCESSION file (#68) must be populated after installing LA\*5.2\*17 and before installing LR\*5.2\*65.

- The TOPOGRAPHY FIELD and URGENCY files can be populated once users are back on the system.

Example: How to Populate ACCESSION file (#68)

\>D P^DI

VA FileMan 21.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 68 ACCESSION

(22 entries)

EDIT WHICH FIELD: ALL// .091 NUMERIC IDENTIFIER

THEN EDIT FIELD: .092 TYPE OF ACCESSION NUMBER

THEN EDIT FIELD: \<RET\>

Select ACCESSION AREA: CHEMISTRY

NUMERIC IDENTIFIER: // *(Enter a one or two digit number for each accession area)*

TYPE OF ACCESSION NUMBER: SHORT// ?

> Select the type of Accession Number that will be barcoded and passed in messages. If nothing is entered, the default will be 'L'ong.

> Choose from:

> S SHORT

> L LONG

TYPE OF ACCESSION NUMBER: SHORT// \<RET\>Example: How to Populate TOPOGRAPHY FIELD file (#61)

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: TOPOGRAPHY FIELD// \<RET\>

EDIT WHICH FIELD: ALL// .08 HL7 CODE

THEN EDIT FIELD: \<RET\>

Select TOPOGRAPHY FIELD NAME: ?

> Answer with TOPOGRAPHY FIELD NAME, or SNOMED CODE, or ABBREVIATION, or

> SYNONYM

> Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? NO

> You may enter a new TOPOGRAPHY FIELD, if you wish

> ANSWER MUST BE 2-80 CHARACTERS IN LENGTH

Select TOPOGRAPHY FIELD NAME: AMNIOTIC FLUID 8Y300

HL7 CODE: ?

> Answer must be 2-4 characters in length.

Enter the two to four character code from the left column:

ABS ABCs

AMN Amniotic fluid

ASP Aspirate

BPH Basophils

ABLD Blood arterial

BBL Blood bag

BON Bone

BRTH Breath

BRO Bronchial

BRN Burn

Enter RETURN to continue or '^' to exit: ^

HL7 CODE: AMNExample: How to Populate URGENCY file (#62.05)

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 62.05 URGENCY

(17 entries)

EDIT WHICH FIELD: ALL// ?

> Answer with FIELD NUMBER, or LABEL

Choose from:

> .01 URGENCY

> 1 CAN LAB COLLECT?

> 2 WORKLOAD ONLY

> 3 HL7 CODE

> FOLLOW A FIELD NAME WITH ';"CAPTION"' TO HAVE THE FIELD ASKED AS 'CAPTION: '

> OR WITH ';T' TO USE THE FIELD 'TITLE' AS CAPTION

EDIT WHICH FIELD: ALL// 3 HL7 CODE

THEN EDIT FIELD: \<RET\>

Select URGENCY: ?

> Answer with URGENCY, or NUMBER

> Do you want the entire 17-Entry URGENCY List? Yes (Yes)

Choose from:

> 1 STAT

> 2 ASAP

> 3 PRE-OP

> 4 CALL RESULT

> 5 ADMIT

> 6 OUTPATIENT

> 7 PURPLE TRIANGLE

> 9 ROUTINE

> 50 WKL

> 51 WKL - STAT

> 52 WKL - ASAP

> 53 WKL - PRE-OP

> 54 WKL - CALL RESULT

> 55 WKL - ADMIT

> 56 WKL - OUTPATIENT

> 57 WKL - PURPLE TRIANGLE

> 59 WKL - ROUTINE

> You may enter a new URGENCY, if you wish

> Answer must be 3-30 characters in length.

Select URGENCY: 1 STAT

HL7 CODE: ?

> Enter the corresponding HL7 Table of Priority that most closely matches

> the DHCP Lab urgency.

> Choose from:

> S Stat (do immediately)

> A As soon as possible (a priority lower than stat)

> R Routine

> P Preoperative (to be done prior to surgery)

> T iming critical (do as near as possible to requested time)

HL7 CODE: S

### Populated DHCP HL7 Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of populated DHCP HL7 files.

Example: HL7 APPLICATION PARAMETER file (#771)

This file will be populated during the post-initialization process.

NAME: LA AUTO INST ACTIVE/INACTIVE: ACTIVE

> HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

HL7 MESSAGE: ORU PROCESSING ROUTINE: ORU^LA7HL7

HL7 MESSAGE: ORM PROCESSING ROUTINE: NONE

HL7 SEGMENT: OBR

> FIELDS USED IN THIS SEGMENT: 4,7,8,9,14,22

HL7 SEGMENT: OBX

> FIELDS USED IN THIS SEGMENT: 2,3,4,5,6,7,8

HL7 SEGMENT: MSH

> FIELDS USED IN THIS SEGMENT: 1,2,3,4,5,6,7,8,9,10,11,12

HL7 SEGMENT: PID FIELDS USED IN THIS SEGMENT: 3,5,7,8,19

HL7 SEGMENT: ORC FIELDS USED IN THIS SEGMENT: 1,2,3

HL7 SEGMENT: NTE FIELDS USED IN THIS SEGMENT: 3

If the LA AUTO INST does not look correct (-1), use FileMan to edit the file and

remove the -1.

Example: HL7 Non-DHCP APPLICATION PARAMETER file (#770)

NAME: LAB INTERFACE DHCP STATION NUMBER: XXX

> NON-DHCP FACILITY NAME: Generic Interface Manager

> MAXIMUM BLOCK SIZE: 245 NUMBER OF RETRIES: 3

> HL7 DEVICE: INST MGR HL7 VERSION NUMBER: 2.1

> DHCP APPLICATION: LA AUTO INST LOWER LEVEL PROTOCOL TIMEOUT: 3

> HL7 PROCESSING ID: PRODUCTION START/STOP TRANSMISSION LOG: STOP LOG

### Populated Laboratory Universal Interface Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of populated LA7 files. Use VA FileManager to edit or

update File \#62.48.

Example: LA7 MESSAGE PARAMETER file (#62.48)

CONFIGURATION: UNIVERSAL INTERFACE PROTOCOL: HEALTH LEVEL SEVEN

> STATUS: ACTIVE MODE FOR LOG: NO LOGGING

> HL7 NON-DHCP APPLICATION: LAB INTERFACE

> PROCESS IN: D QUE^LA7UIIN PROCESS DOWNLOAD: D EN^LA7UID1

REMOTE SYSTEM ID: LAB INTERFACE Generic Interface ManagerLA AUTO INSTXXX

The .01 field of File \#770

GIM or name of vendors’ systems. Field \#3 of File \#770

DHCP Application, Field .01 in File \#771 and Field \#8 of File \#770

Your station number

This file is populated by the Laboratory UI software.

Example: LA7 MESSAGE QUEUE file (#62.49)

MESSAGE NUMBER: 13346 TYPE: INCOMING

> STATUS: QUEUED FOR ACTION PRIORITY: 3

> DATE/TIME ENTERED: JUL 10, 1994@00:11:48

> INSTRUMENT NAME: SYSMX1 CONFIGURATION: UNIVERSAL INTERFACE

> MSH: MSH ENCODING CHARACTERS: ~\\

> SENDING APPLICATION: LAB INTERFACE SENDING FACILITY: Generic Interface

> Manager

> RECEIVING APPLICATION: LA AUTO INST RECEIVING FACILITY: XXX

> DATE/TIME OF MESSAGE: JUL 10, 1994@00:14:03

> MESSAGE TYPE: ORU MESSAGE CONTROL ID: 11812

> PROCESSING ID: PRODUCTION VERSION ID: 2.1

HL7 TEXT:

MSH\|^~\\\|LAB INTERFACE\| Generic Interface Manager\|LA AUTO INST\|642

> \|19940710001403\|ORU\|11812\|P\|2.1\|

OBR\|1\|ERR000000003\|\|\|\|\|\|\|\|SYSMX1 ^\|0\|\|19940707

OBX\|1\|ST\|85048^White Blood Count^AS4^\|\|9.1\|k/ul\|\|\|F\|

OBX\|2\|ST\|85041^Red Blood Count^AS4^\|\|3.4\|ma/ul\|L\|\|F\|

OBX\|3\|ST\|83020^Hemoglobin, electrophoresis^AS4^\|\|10.3\|g/dl\|L\|\|F\|

OBX\|4\|ST\|85014^Blood count; other than spun hematocrit^AS4^\|\|32.9\|%\|L\|\|F\|

OBX\|5\|ST\|85021.11^Hemogram, automated;MCV^AS4^\|\|96.8\|fl\|\|\|F\|

OBX\|6\|ST\|85021.21^Hemogram, automated;MCH^AS4^\|\|30.3\|pg\|\|\|F\|

OBX\|7\|ST\|85021.27^Hemogram, automated;MCHC^AS4^\|\|31.3\|g/dl\|L\|\|F\|

OBX\|8\|ST\|85021.47^Hemogram, automated;Platelet count auto^AS4^\|\|20.3\|k/ul\|\|\|F\|

OBX\|9\|ST\|85048.42^White Blood Count;Lymphocyte, %^AS4^\|\|25.3\|%\|\|\|F\|

OBX\|10\|ST\|85048.52^White Blood Count;Monocyte, %^AS4^\|\|4.8\|%\|\|\|F\|

OBX\|11\|ST\|85048.12^White Blood Count;Total neutrophil, %^AS4^\|\|66.8\|%\|\|\|F\|

OBX\|12\|ST\|85048.64^White Blood Count;Eosinophil, %^AS4^\|\|2.7\|%\|\|\|F\|

OBX\|13\|ST\|85048.60^White Blood Count;Basophil, %^AS4^\|\|.4\|%\|\|\|F\|

OBX\|14\|ST\|85048.41^White Blood Count;Lymphocyte count^AS4^\|\|2.3\|k/ul\|\|\|F\|

OBX\|15\|ST\|85048.51^White Blood Count;Monocyte count^AS4^\|\|.44\|k/ul\|\|\|F\|

OBX\|16\|ST\|85048.11^White Blood Count;Total neutrophil count^AS4^\|

> \|6.07\|k/ul\|\|\|F\|

OBX\|17\|ST\|85048.63^White Blood Count;Eosinophil count^AS4^\|\|.25\|k/ul\|\|\|F\|

OBX\|18\|ST\|85048.59^White Blood Count;Basophil count^AS4^\|\|.04\|k/ul\|\|\|F\|

OBX\|19\|ST\|85021.91^^AS4^\|\|17.8\|%\|H\|\|F\|

OBX\|20\|ST\|85021.92^^AS4^\|\|63.3\|fl\|H\|\|F\|

OBX\|21\|ST\|85029.15^^AS4^\|\|12\|fl\|\|\|F\|

OBX\|22\|ST\|85029.11^^AS4^\|\|9.3\|fl\|\|\|F\|

All systems: Allow users back on the laboratory system.

# Technical Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Planning Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is a quick overview of some of the major issues to be considered in the planning and implementation of the Laboratory UI.

### Location/Cabling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you place the GIM PC in the same location as the LSI, then existing cabling can probably be used. If you change the location or decide to use ethernet instead of arnet board, then you may need to recable each instrument. If you are moving direct connect interfaces to the GIM, you may need to recable those instruments. Cables can be purchased from the GIM vendor or done yourself.

If the GIM is in the laboratory, it may be very difficult to route satellite laboratory instrumentation or instruments from other buildings to the GIM. Wherever the GIM is located determines who does the maintenance and support of the GIM.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You probably want to increase the speed to 9600 baud for all instruments which are capable of that speed to keep a good response time.

### Driver Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check with the GIM vendor to see if DHCP HL7 drivers are already written for your instrument models. If not, it will speed the process if you can supply the interface specifications to the GIM vendor. If the vendor request the specifications from the laboratory instrument manufacturer themselves, the possibility exist that vendor may be delayed or be given the wrong version or wrong model. Even if the driver is already written, it may need enhancements or modifications to work in your laboratory. Be very specific and complete when discussing the instrument specific interface software with the vendor. An instrument may have many different data streams for different methods. The existing driver may not include all of the methods.

### Data Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For laboratory instruments that have more than one possible data stream format, the LSI tended to use the simplest format. The GIM drivers tend to use the more complex format which have the maximum amount of error checking in the data transmission. This is to insure that the data received is exactly what was sent. However, it may create more difficulty in establishing proper communications and may result in more rejected transmissions than previously seen with the LSI.

### Implementation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not expect to get each interface going in five minutes. The same process used with the LSI will be repeated with the GIM. Wiring needs to be tested. Communication parameters need to be synchronized on both sides. Incoming data needs to be examined and tested with each instrument driver. The logic in decoding the data may be somewhat different than the old LSI routine so you may have to re-think some of your bench procedures. There are a number of configuration steps to do for each interface. A test mapping screen on the GIM has to be completed to make sure that the tests are defined compatibly between the instrument and DHCP. There are also many new fields in the AUTO INSTRUMENT file (#62.4), TOPOGRAPHY file (#61), URGENCY file (#62.05), and ACCESSION file (#68) to be filled in.

The HL7 package must to be installed and setup with the proper entries to establish the DHCP link with the Laboratory UI. (Refer to DHCP HL7 V. 1.6 documentation.)

If you are going to use bar coded labels, these must be functioning and tested. You may need to change your downtime procedures somewhat to accommodate the new system. Plan to move the instruments over gradually so that you can thoroughly test and incorporate each change in an orderly way.

### Bidirectional Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bidirectional interfaces require more effort to establish. The site needs to decide whether to use automatic download or manual download and whether site wants host query or direct download.

### Support and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The person supporting the Laboratory UI needs to get familiar with the structure of the HL7 messages. Personnel need training in how to check for and start the background job and how to reboot the PC and start the interfaces. Plans need to be made for a backup system and how to implement it. Errors can occur in numerous places and the support person(s) need to be familiar with the path of data back and forth to track problems. The Start/Stop Log of HL7 Transmissions can be used as a debugging tool between DHCP and the GIM system.

DHCP has its regular error log and also has a separate log for HL7 message errors which tracks data streams that did not meet the HL7 standard for a variety of reasons. The Laboratory UI has a Print Laboratory Universal Interface Log option to track message errors. For the bidirectional instruments the errors can occur at any of these levels and in both directions so it can be complicated to track a problem. (Refer to DHCP HL7 Versions 1.5 and 1.6 documentation.)

### GIM Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backups of the vendor's generic interface system must be considered, discussed, and planned with your vendor. Make sure that there is a hardware and software backup available through the vendor or contractor.

### Checklist for Laboratory Universal Interface Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This checklist provides the actions required before implementing the Laboratory

UI.

I. PC - Vendor specific

1\. \_\_\_\_\_\_\_\_ Instrument specific software installed

> 2\. \_\_\_\_\_\_\_\_ Interface software installed

> 3\. \_\_\_\_\_\_\_\_ Configuration of PC

> A. \_\_\_\_\_\_\_\_ System

> B. \_\_\_\_\_\_\_\_ Instrument tests/parameters

> (repeat for each instrument

> that is interfaced)

4\. \_\_\_\_\_\_\_\_ Wiring/ports

> A. \_\_\_\_\_\_\_\_ Connected to DHCP

> \_\_\_\_\_\_\_\_ Wiring

> \_\_\_\_\_\_\_\_ Port configuration

> \_\_\_\_\_\_\_\_ Tested OK

> B. \_\_\_\_\_\_\_\_ Connected to instrument(s)

> \_\_\_\_\_\_\_\_ Wiring

> \_\_\_\_\_\_\_\_ Port configuration if needed (if

> PC is located in the laboratory, this step

> will not be needed)

> \_\_\_\_\_\_\_\_ Tested OK

II\. DHCP

1\. \_\_\_\_\_\_\_\_ HL7 Package

> A. \_\_\_\_\_\_\_\_ Installed

> B. \_\_\_\_\_\_\_\_ Files configured

> \_\_\_\_\_\_\_\_ NON-DHCP APPLICATION PARAMETER file (#770)

> \_\_\_\_\_\_\_\_ HL7 APPLICATION PARAMETER file \#771

> \_\_\_\_\_\_\_\_ Others

> C. \_\_\_\_\_\_\_\_ Debug log on for testing

> **NOTE:** Turn off debug log after testing is completed. Disk full errors can occur if debug log is left on for an extended period (days).

> D. \_\_\_\_\_\_\_\_ Background job running

2\. \_\_\_\_\_\_\_\_ Laboratory HL7 Software

> A. \_\_\_\_\_\_\_\_ Installed

> B. \_\_\_\_\_\_\_\_ Files configured

> \_\_\_\_\_\_\_\_ LA7 MESSAGE PARAMETER file(#62.48)

> \_\_\_\_\_\_\_\_ AUTO INSTRUMENT file (#62.4)

> \_\_\_\_\_\_\_\_ TOPOGRAPHY file (#61)

> \_\_\_\_\_\_\_\_ URGENCY file (#62.05)

> \_\_\_\_\_\_\_\_ ACCESSION file (#68)

III\. Barcode Labels

> A. \_\_\_\_\_\_\_\_ Printer installed

> B. \_\_\_\_\_\_\_\_ Label routine installed

> C. \_\_\_\_\_\_\_\_ Bar codes print OK

> D. \_\_\_\_\_\_\_\_ Bar codes read on instrument(s) OK

IV.Laboratory Instruments (repeat for each one that is interfaced)

> A. \_\_\_\_\_\_\_\_ Wiring

> \_\_\_\_\_\_\_\_ Connected

> \_\_\_\_\_\_\_\_ Communication parameters set on

> instrument

> \_\_\_\_\_\_\_\_ Tested OK

> B. \_\_\_\_\_\_\_\_ Verify compatible communication

> parameters on the PC or DHCP port

> depending on where the PC is located

V. Bidirectional Interfaces

> A. \_\_\_\_\_\_\_\_ Manual download tested OK

> B. \_\_\_\_\_\_\_\_ Auto download tested OK

> \_\_\_\_\_\_\_\_ if using, turn on Autodownload

> field in File \#62.4

> C. \_\_\_\_\_\_\_\_ Host query tested OK

> \_\_\_\_\_\_\_\_ If using host query, turn on at

> the instrument

### Interface Data Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The next page shows a sample form for keeping records of how each interface is setup. This form can be helpful for troubleshooting purposes and for passing on to others who may have to work with problems when the original implementor is no longer available. We recommend that each instrument interface specification be filed with a form such as this one to document the settings on interface. It is also helpful to print out the data in the AUTO INSTRUMENT file that relates to this instrument and the load worklist entry and attach those to the file.

Interface Data

Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name/Model:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Location of instrument:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DecServer/Port:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Hard Wire or Phone Data line:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Port Communication Parameters:

> Baud:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Data:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Stop:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Parity:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Protocol:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Communication Parameters:

> Baud:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Data:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Stop:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Parity:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Protocol:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Software version:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Type of interface:

> Unidirectional:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Bidirectional Cluster:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Manual download:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Auto download:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Bidiretional Direct Download:\_\_\_\_\_\_\_\_

> Manual download:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Auto download:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Other:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTO INSTRUMENT file (#62.4) entry:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

LOAD/WORKLIST file (#68.2) entry:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Notes:

## Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 13 new routines, 3 modified routines, plus 1 NTEG, and 44 init routines

associated with this patch.

### New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of new routines for the Laboratory UI patch LA\*5.2\*17.

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Routine Name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| LA7ADL           | This routine runs in the background to automatically download test orders to each instrument flagged for automatic downloading. It monitors the LA("ADL" node to check for accessions that are to have test orders automatically downloaded to another computer system. All entries in the AUTO INSTRUMENT file (# 62.4) that are flagged for automatic downloading will be checked to see if they contain any tests on the accession. If tests are found, then the appropriate download message is constructed and sent.                           |
| LA7ADL1          | This routine is called by LA7ADL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LA7HL7           | This routine is the main driver for incoming messages. This routine is called by the DHCP HL7 package V. 1.6 to process incoming HL7 messages. Expected variables are those documented in the DHCP HL7 package documentation. The line tag is called if it is entered into the Processing Routine field in the HL7 SEGMENT NAME file (#771.3). Each message type is processed at the line tag of the same name.                                                                                                                                     |
| LA7HLP           | This routine contains the HL7 Source of Specimen Table 0070 from the HL7 standard. This table contains the possible choices for filling in field .08 of the TOPOGRAPHY file (#61).                                                                                                                                                                                                                                                                                                                                                                  |
| LA7LOG           | This routine logs events and errors from Laboratory Messenger. Creates an entry in the log file to record events or errors while processing messages. The calling routine passes the ien for a bulletin in LA7 MESSAGE LOG BULLETIN file (#62.485). Requires the variables LA762485 (ien of bulletin in File \#62.485) and LA76248 (IEN of config in LA MESSAGE PARAMETER file (#62.48) or null if none is defined. Also prints the error log which is stored in ^XTMP. Errors are logged only if the debug log field is turned on in File \#62.48. |

|                  |                                                                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Routine Name | Description                                                                                                                                                                                                                                                                                                               |
| LA7UID1          | This routine converts the information for each test in the load list into HL7 messages and hands them off to the HL7 package for delivery.                                                                                                                                                                                    |
| LA7UID2          | This routine processes download message for an entry in File \#62.48. The various segments required by the HL7 format are constructed in this routine and then stored in the array expected by the HL7 package. Calls are made to the HL7 package to construct the MSH header and to send the completed HL7 message.          |
| LA7UIIN          | This routine is a background task job which processes incoming laboratory result UI messages that are received from the GIM. File \#62.48 should have an entry in the PROCESS IN field. The PROCESS IN field must contain D QUE^LA7UIIN. The LA7UIIN routine runs in the background to check the incoming queue for messages. |
| LA7UIIN1         | If a message is found in the incoming queue, LA7UIIN1 is called to process the message. LA7UIIN1 processes the MSH and OBR segments of the HL7 message.                                                                                                                                                                       |
| LA7UIIN2         | This routine is called from LA7UIIN1 and processes the Notes and Comments Segment (NTE) and OBX segments which contain results and comments. It also checks the PARAM 1 and the other fields (#12-17) in the AUTO INSTRUMENT file (#62.4)which control various characteristics of individual test results.                    |
| LA7UTIL          | This routine has various utilities for the Laboratory HL7 interface.                                                                                                                                                                                                                                                          |

### Modified Routines for Laboratory UI Patch LA\*5.2\*17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                |
|-------------|--------------------------------------------------------------------------------|
| Routine | Name Description                                                           |
| LADOWN      | Utility for manual download options that have special codes for HL7 interface. |
| LADOWN1     | Utility for manual download options that have special codes for HL7 interface. |
| LAGEN       | This routine transfers results to ^LAH.                                        |

### Modified Routines for Laboratory UI Patch LR\*5.2\*65

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of regular laboratory routines that have hooks or special code in them to handle the HL7 laboratory interface. These routines are in Laboratory patch LR\*5.2\*65, and must be installed before running the Laboratory UI.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine</strong></td>
<td><strong>Name Description</strong></td>
</tr>
<tr class="even">
<td>LROLOVER</td>
<td>UID stays the same but traditional accession number changes dates.</td>
</tr>
<tr class="odd">
<td>LRX</td>
<td>Entry point for Extrinsic function call to create unique accession ID number.</td>
</tr>
<tr class="even">
<td>LRLABLD</td>
<td>Code for UID</td>
</tr>
<tr class="odd">
<td>LRLABLD0</td>
<td>Code to suppress UID on future labels.</td>
</tr>
<tr class="even">
<td>LRCONJAM</td>
<td>Added code to create UID on controls and check if auto downloading is being used.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>LRWLST,</p>
<p>LRWLST1</p></td>
<td>Added code to check for auto downloading. Also added code to create UID.</td>
</tr>
<tr class="odd">
<td>LRTSTSET</td>
<td>Added code to check for auto downloading when tests added to an accession.</td>
</tr>
</tbody>
</table>

### Init Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LA7IN001 LA7IN002 LA7IN003 LA7IN004 LA7IN005 LA7IN006 LA7IN007 LA7IN008

LA7IN009 LA7IN00A LA7IN00B LA7IN00C LA7IN00D LA7IN00E LA7IN00F LA7IN00G

LA7IN00H LA7IN00I LA7IN00J LA7IN00K LA7IN00L LA7IN00M LA7IN00N LA7IN00O

LA7IN00P LA7IN00Q LA7IN00R LA7IN00S LA7IN00T LA7IN00U LA7IN00V LA7IN00W

LA7IN00X LA7IN00Y LA7IN00Z LA7IN010 LA7IN011 LA7INIS LA7INIT LA7INIT1

LA7INIT2 LA7INIT3 LA7INIT4 LA7INIT5

> 44 routines

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>File</strong></p>
<p><strong>Number</strong></p></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>62.485</td>
<td><p>LA7 MESSAGE</p>
<p>LOG</p>
<p>BULLETINS</p></td>
<td><p>This file stores canned text for logging errors during message processing. This file is not meant to be edited locally, but if local entries are made, they must be entered at ien &gt;999.</p>
<p>There are about 20 error messages in the file. The most commonly seen errors are:</p>
<ul>
<li><p>Message stored that had no message text</p></li>
<li><p>Message text did not begin with MSH, message rejected</p></li>
<li><p>Field or component separator is bad, message rejected</p></li>
<li><p>OBR segment was not found, message rejected</p></li>
<li><p>OBR contained bad instrument name</p></li>
<li><p>Instrument name in message is not in AUTO INSTRUMENT file (#62.4)</p></li>
<li><p>Unique ID not found in ACCESSION file (#68)</p></li>
<li><p>Accession not found in File #68 for area x, date x, entry x</p></li>
<li><p>Test=null</p></li>
<li><p>Test value=null</p></li>
<li><p>No download code for this test name in File #62.4</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>62.48</td>
<td>LA7 MESSAGE PARAMETER</td>
<td>This file requires site setup. This file stores parameters associated with laboratory messaging configuration. Only one entry is needed to run each Laboratory UI. Other entries can be made if other messaging systems are in use.</td>
</tr>
<tr class="even">
<td>62.49</td>
<td>LA7 MESSAGE QUEUE</td>
<td>This file stores the HL7 messages sent and received by the Laboratory HL7 interface. It is populated by the routines. This file must not be edited by users.</td>
</tr>
</tbody>
</table>

### Modified Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of files and fields from other Laboratory files.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>AUTO INSTRUMENT File # 62.4</strong></td>
</tr>
<tr class="even">
<td><h3 id="field">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td>62.4,.02</td>
<td><p>VENDOR CARD</p>
<p>ADDRESS</p></td>
<td>The vendor card address should be stored in this field for Lab HL7 message downloads using Lab Universal Interface software.</td>
</tr>
<tr class="even">
<td>62.4,.04</td>
<td><p>SHORT</p>
<p>ACCESSION #</p>
<p>LENGTH</p></td>
<td>This field should be used to pad accession numbers based on the fixed length entered for this instrument.</td>
</tr>
<tr class="odd">
<td>62.41,2</td>
<td>PARAM 1</td>
<td><p>This is an old field with a new use. Any M code written into this field will be executed on a given test result which is contained in the variable LA7VAL.</p>
<p>Some examples of code which could be used in PARAM 1:</p>
<p>1.</p>
<p>S LA7VAL=$S(LA7VAL&gt;100:"&gt;100",1:LA7VAL) This code is used on PTT test to convert any numerical value over 100 to &gt;100 result rather than the actual number send by the instrument.</p>
<p>2.</p>
<p>S LA7VAL=LA7VAL*10</p>
<p>This code converts the random urine protein to a concentration unit different from that reported by the instrument.</p>
<p>3.</p>
<p>S LA7VAL=$S(LA7VAL&gt;99,"PRESUMP</p>
<p>POS",1:"NEG")</p>
<p>This code takes numerical drug screen results sent by the instrument and converts any result over 99 to the string PRESUMP POS and any other number to the string NEG.</p></td>
</tr>
<tr class="even">
<td>62.41,6</td>
<td>UI Test Code</td>
<td>Another old field with a new use. This field is used to define the instrument "name" for a test. This "name" is used as an identifier for the test in all messages sent to and from the instrument. It is important that the Universal Interface PC has the name defined in this instrument's configuration exactly as it is here in the File #62.4, including upper and lower case. UI Test Code This field does not have to be the test name, but can be. The name of this field should not be taken literally, it is used for both uploading and downloading, for unidirectional as well as bi-directional. This is the primary identifier in all of the HL7 messages passed between DHCP and the Laboratory UI PC.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>AUTO INSTRUMENT File # 62.4 (continued)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-1">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td><p>62.41,6</p>
<p>continued</p></td>
<td>UI Test Code</td>
<td><p>It must be defined on the PC exactly as it is entered here. This field can be any alphanumeric string that passes the transform . There is an "AC" cross reference on this field that is used as a lookup when a message is received. If test results are not being downloaded or uploaded for this test, it might be because the Download Code does not match exactly with the identifier on the PC for this instrument configuration.</p>
<p>On some GIM systems, the test name is not configured on the PC but just passes the name of the test as sent from the instrument. This can be determined by using the transmission log on the PC if available on that system or by using the LA7 error log option.</p>
<p>Some instruments require a different download code from the upload code. In this case the test would be entered twice and using the fields Accept results for this test and Download to Instrument, the appropriate upload and download tests can be defined.</p></td>
</tr>
<tr class="even">
<td>62.41,12</td>
<td><p>Number of</p>
<p>Decimal Places</p></td>
<td><p>In this field, if nothing is entered, the decimal place of the result will not be modified. Rounding will take place if the number of decimal places is exceeded. This field is used to modify the result returned by the instrument. It is used to force the</p>
<p>result to a certain number of decimal places. If the result has more decimal places than the number entered for this field, the result will be rounded to the number of decimal places specified. If M code exists in PARAM 1, it will be executed before any</p>
<p>modification to the result. If the code in PARAM 1 changes the result such that it is no longer a canonic number, no modification to decimal places will take place. To round off the result based on other factors, or in other words - "on the fly", you can set a variable in PARAM 1 as follows: PARAM 1: S:(CONDITION) LA7XFORM(1)=3 where CONDITION is some M value that equates to true or false, and 3 represents the number of decimal places. 3 is just an example, you can use any number including zero.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>AUTO INSTRUMENT File # 62.4 (continued)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-2">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td>62.41,13</td>
<td><p>Convert Result</p>
<p>to Remark</p></td>
<td>This field should be set to YES if you want the result to be converted to a comment or remark. If M code exists in PARAM 1, it will be executed before converting the result to a comment. Be aware that if field 17 REMOVE SPACES FROM RESULT is set to YES, the comment will have all spaces removed. To convert the result to a comment based on other factors, or in other words - "On the fly." You can set a variable in PARAM 1 as follows: S:(CONDITION) LA7XFORM(2)=1 where CONDITION is some M value that equates to true or false.</td>
</tr>
<tr class="even">
<td>62.41,14</td>
<td><p>Accept Results</p>
<p>for this Test</p></td>
<td>In this field if the null default is YES, it means that results should be moved to ^LAH for verification. If there is M code in PARAM 1, it will be executed regardless of how this field is set. To accept results for this test based on other factors, or in other words - "On the fly," you can set a variable in PARAM 1 as follows: S:(CONDITION) LA7XFORM(3)=1 where CONDITION is some M value that equates to true or false. This field can be used for screening out extraneous test results sent from the instrument or to screen out tests used for downloading only. As noted in the UI Test Code field (#62.41,6), an instrument can use a different code for downloading than uploading. A NO in this field would be appropriate for the download test with a YES in the Download to Instrument field (#62.41,15) and in cases where extra test results are being sent from the instrument, enter a NO in field (#62.41.6) and a NO in the Field (#62.41,15).</td>
</tr>
<tr class="odd">
<td>62.41,15</td>
<td><p>Download to</p>
<p>Instrument</p></td>
<td>This field is used to prevent downloading of calculated tests to CX7. Example: Anion Gap. Even though it may be an ordered test, it is not a "performed" test--just a calculation so the result gets uploaded, but the order is not downloaded. If null, default is YES. If there is M code in PARAM 1 it will be executed regardless of how this field is answered. This field is only used for processing results.</td>
</tr>
<tr class="even">
<td>62.41,16</td>
<td><p>Ignore Results</p>
<p>not Ordered</p></td>
<td>If null, the default will be NO. This field should be set to YES if you want to restrict results to only those tests that were ordered. For example, if an electrolytes panel was ordered consisting of Na, K, Cl, CO2 and the instrument also reported a BUN result, the BUN would not be reported if this field was set to YES.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>AUTO INSTRUMENT File # 62.4 (continued)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-3">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td><p>62.41,16</p>
<p>continued</p></td>
<td><p>Ignore Results</p>
<p>not Ordered</p></td>
<td>To ignore results not ordered based on other factors, "on the fly," you can set variable in PARAM 1 as follows: PARAM 1: S:(CONDITION) LA7XFORM(5)=1 where CONDITION is some M value that equates to true or false.</td>
</tr>
<tr class="even">
<td>62.41,17</td>
<td><p>Remove Spaces</p>
<p>from Result</p></td>
<td><p>Answer YES if you want to strip all space characters from the result before storing it. If answered YES the result from the instrument will be changed so that it contains no spaces, e.g., &gt; 3.2 would be &gt;3.2. If this test is setup to be converted to a comment (see field 13), the spaces will not be removed regardless of how you answer this filed. M code in PARAM 1 will always be executed before any other transformation of the result takes place, including the stripping of spaces. To strip spaces conditionally based on other factors, "on the fly" you can set a variable in PARAM 1 as follows:</p>
<p>PARAM 1: S:(CONDITION) LA7XFORM(6)=1 where CONDITION is some M value that equates to true or false.</p></td>
</tr>
<tr class="odd">
<td>62.4,91</td>
<td>Download Entry</td>
<td>Enter the line tag of the routine used to down load data to the instrument. DO NOT USE '^' ON THIS LINE TAG. IT WILL BE HANDLED BY THE PROCESSING ROUTINE.</td>
</tr>
<tr class="even">
<td>62.4,92</td>
<td><p>Download</p>
<p>Protocol</p></td>
<td>Enter the name of the routine used to down load data to the instrument.</td>
</tr>
<tr class="odd">
<td>62.41,98</td>
<td>Automatic Download</td>
<td>This field checks if the instrument is ready for automatic download. This field is needed for LA7ADL routine.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>Topography File (#61)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-4">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td>61,.08</td>
<td>HL7 Code</td>
<td>This field links DHCP specimen type with the HL7 Specimen Source Table (0070). By entering a code from Table 0070 for each entry in the HL7 Code file, a mapping is made to the HL7 standard codes. The HL7 CODE field should be edited for any specimen types that could possibly be downloaded to an instrument.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>Urgency File (#62.05)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-5">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td>62.05,.08</td>
<td>HL7 Code</td>
<td>This field is a set of codes to map to the HL7 urgencies. This field is used for downloading the urgency to an instrument. By entering a code from the HL7 Specimen Code Table (0070) for each entry in the HL7 Code field, a mapping is made to the HL7 standard codes. The HL7 CODE field should be edited for any specimen types that could possibly be downloaded to an instrument.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>Accession File (# 68)</strong></td>
</tr>
<tr class="even">
<td><h3 id="field-6">Field #</h3></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td>68,.091</td>
<td><p>Numeric</p>
<p>Identifier</p></td>
<td>This field is a one or two digit unique number used to create the UID.</td>
</tr>
<tr class="even">
<td>68,.092</td>
<td><p>Type of</p>
<p>Accession Number</p></td>
<td>This field is a long or short identifier.</td>
</tr>
</tbody>
</table>

Refer to the UID specifications section of this manual, for more information on

Field (#.092).

### Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Give the following options to the appropriate IRM and Laboratory staff. Lab Universal Interface Menu (LA7 MAIN MENU)

\|

\|

1.  Print Source of Specimen Table \[LA7 PRINT 0070 TABLE\]

This option is used to print errors and events logged using the Lab Universal Interface system.

2.  Print Lab Universal Interface Log \[LA7 PRINT LAB UI ERROR LOG\]

This option is used to print the Source of Specimen Table (0070) from the HL7 standard. This table contains the possible choices for filling in field .08 of the TOPOGRAPHY file \#61.

### Cross-reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LA 7 MESSAGE QUEUE file (#62.49)

XREF DD FLD NUM FIELD NAME

--------------- -------- ---------- ------------------------------

\* "AD" 62.49 4 DATE/TIME ENTERED

\* "B" 62.49 .01 MESSAGE NUMBER

\* "C" 62.49 5 INSTRUMENT NAME

\* "Q" 62.49 2 STATUS

LA7 MESSAGE LOG BULLETIN file (#62.485)

XREF DD FLD NUM FIELD NAME

--------------- -------- ---------- ------------------------------

\* "B" 62.485 .01 CODE

LA7 MESSAGE PARAMETER FILE 62.48

XREF DD FLD NUM FIELD NAME

--------------- -------- ---------- ------------------------------

\* "B" 62.48 .01 CONFIGURATION

\* "C" 62.483 .01 REMOTE SYSTEM ID

### Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Archiving

There is no archiving in the Laboratory UI.

#### Purging

Laboratory UI messages that are transmitted successfully will be given a purge status. These messages are purged every 24 hours. Error messages are kept seven days and then purged by Kernel. In addition to the message, an interpretation of the error is given. These error messages are displayed in time sequence with the most recent being first.

Refer to the DHCP HL7 V. 1.6 Technical Manual for purging options within DHCP HL7 application.

### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines in the Laboratory UI.

### External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integration Agreements exist allowing applications to populate and reference HL7 files. Refer to the External Relations section of DHCP HL7 V. 1.6 Technical Manual.

### Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All options of the Laboratory UI are stand alone.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the Laboratory UI software.

# Universal Identification Number (UID) Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the specifications for DHCP UID.

- Automated instrument software needs to allow multiple accession areas to use the same instrument.
- The historical accession number does not lend itself to a pure numeric character bar coded.
- The UID will be a pure numeric bar code accession number.
- The UID will provide positive identification of the specimen for verification purposes, downloading and uploading to the universal interface.

### Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The UID should be a 9 or 10 digit numeric string.
2.  Position 1 and 2 will contain a unique number identifying the accession area.
3.  The range of accession numbers for a daily transform accession should be 1-9999.
4.  The range of accession numbers for a yearly transform should be 1-999999.
5.  The range for quarterly monthly accession areas should be 1-99999.
6.  By accession area select UID functionality to be used for bar coding and downloading messages.
7.  If the accession area uses UID, the UID should appear on barcode labels, and is displayed when the specimen is accessioned.
8.  The system should accept just the accession number portion of UID.
9.  Create a user defined two digit field to contain a unique accession area number with a range of 01-99.
10. Auto instruments should allow multiple load/worklist for downloading test(s) to the interface.
11. Current auto instrument software should be supported for backward compatibility.

Examples of possible UID number by accession transforms. The accession area is user defined as 32. Accession numbers are represented by 9's.

Example 1: Daily Accession Area

Digit Position = 0123456789

Daily accession area = 3262889999

Digit 0-1 = accession area (32) Digit 6-9 = accession number (9999)

Digit 3-5 = Julian Date (288)

Digit 2 = year (6)

The UID number is created during accessioning for all accession areas. The UID is displayed on the labels as shown in this example:

UID: 3262889999

![](la-5-2-17-lr-5-2-65-laboratory-universal-interface-installation-guide/004.png)

CHE 1015 9999 Stat 10/15/96

LABPATIENT, THREE

000-00-0003 Ward: 5CN

RED OR MARB

B CHEM. Order: 120

Example 2: Yearly Accession Area

Digit Position = 0123456789

Yearly accession area = 3296999999

Digit 0-1 = accession area (32) Digit 4-9 = accession number (999999)

Digit 2-3 = year (96)

Example 3: Quarterly and Monthly Accession area

Digit Position = 0123456789

Quarterly/Monthly accession area = 3260399999

Digit 0-1 = accession area (32) Digit 5-9 = accession number (99999)

Digit 2 = Year (6) Digit 3 = Quarter/month (03)

The UID is controlled in ACCESSION file (#68) where it is possible to turn off the long number display for a given accession area in the Type of Accession Number field (#.092). The number is still created, but not displayed or used if turned off. If the long number is used, the barcode will code the UID. If the UID is turned off, the barcode will only code the final digits of the traditional accession number.

Example 4: Of a Barcode with the UID Turned Off and showing the final digits of the traditional accession number

UID: 9999

![](la-5-2-17-lr-5-2-65-laboratory-universal-interface-installation-guide/005.png)

CHE 1015 9999 Stat 10/15/96

WAYNE,JOHN D

023-45-6789 Ward: 5CN

RED OR MARB

B CHEM. Order: 120

If the barcode contains the UID, and for some reason you have to manually program the sample into your instrument, you need to type in the entire number so that it matches the barcode read by the instrument off the tube.

# HL7 Standard and DHCP HL7 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step in understanding the Laboratory UI is a basic understanding of HL7 Standard and the DHCP HL7 Health Level Seven (HL7) package.

### HL7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 is a standard protocol which specifies the implementation of interfaces between two computer applications (sender and receiver) for electronic data exchange in health care environments. HL7 allows health care institutions to exchange key sets of data from different application systems. Specifically, it defines the following:

- The data to be exchanged
- The timing of the interchange
- The communication of errors to the sending/receiving application

The formats are generic in nature, and must be configured to meet the needs of the two applications involved. An HL7 interface specification should be written detailing what formats (events, messages, segments, and fields) will be used, and the lower level protocol that will be implemented in order for the two applications to interface with one another.

The HL7 Protocol defines the content and format of abstract messages and transactions for interface capabilities for the following areas:

- Admission, discharge, and transfer (ADT)
- Order entry
- Query
- Financial applications such as charge, payment adjustments, and insurance
- Ancillary data reporting for Laboratory, Radiology, Pharmacy, etc.

In HL7, information is exchanged using HL7 messages when an event occurs in an application. Each HL7 message consists of one or more HL7 segments. A segment can be thought of as a record in a file. Each segment consists of one or more fields separated by a special character called the field separator. The field separator character is defined in the Message Header (MSH) segment of an HL7 message. The MSH segment is always the first segment in every HL7 message. Each field is assigned an HL7 data type (e.g., numeric, text, etc.).

In addition to the field separator character, there are four other special characters called encoding characters. Encoding characters are also defined in the MSH segment. They operate on a single field in an HL7 segment. Each encoding character must be unique, and serves a specific purpose. None of the encoding characters can be the same as the field separator character.

- The first encoding character is the component separator. Some data fields can be divided into multiple components. The component separator is used to separate adjacent components within a data field.
- The second encoding character is the repetition separator. Some data fields can be repeated multiple times in a segment. The repetition separator character is used to separate multiple occurrences of a field.
- The third encoding character is the escape character. Data fields defined as text or formatted text can include escape sequences. The escape character is used to separate escape sequences from the actual text.
- The fourth encoding character is the sub-component separator. Some data fields can be divided into components, and each component can be further divided into sub-components. The sub-component separator is used to separate adjacent sub-components within a component of a field.

### DHCP HL7 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the DHCP HL7 package is to assist DHCP applications in exchanging health care information with other applications using the HL7 Protocol. The DHCP HL7 package consists of a set of utility routines and files that provide a generic interface to the HL7 Protocol for all DHCP applications. The DHCP HL7 package can be divided into two parts:

- Lower level protocol support between sending and receiving applications
- DHCP interface to the HL7 Protocol

### Lower Level Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term lower level refers to a portion of the Open Systems Interconnect (OSI) model. The OSI model is divided into seven layers or levels. The lower levels (layers 1 through 4) support the actual movement of data between systems. This includes the actual physical connection between the systems and the communications protocol used.

DHCP HL7 V. 1.6 supports the following lower level interfaces:

- HL7 Hybrid Lower Layer Protocol over an RS-232 connection
- DHCP MailMan messages
- X3.28

Using these lower level interfaces, the DHCP HL7 package can support layers one through four of the OSI model and eliminate the need for DHCP applications to write lower level interfaces each time they want to exchange data with another application.

These lower level interfaces provide the following functions:

- Receive and send HL7 messages.
- Validate the HL7 Message Header (MSH) information.
- Invoke the appropriate DHCP application routine to process the data in the message.
- Send HL7 accept acknowledgment (ACK) messages back to the sending application.

### DHCP Interface to the HL7 Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of V. l.6, DHCP HL7 supports several methods for interfacing to the HL7 protocol. The method established by V. 1.5 is still supported (for backwards compatibility), and a new method is introduced, as well as new routines, file structures, templates, menus, and options. There are some significant differences between the V. 1.5 and V. 1.6 interface methods, as shown in the following table.

|                                                     |                                                                                                                                  |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| V. 1.5 Interface Method                         | V. 1.6 Interface Method                                                                                                      |
| One sender and one receiver per message.            | One sender, one or more receivers.                                                                                               |
| Sender and receiver must be on different systems.   | Sender and receiver can be on the same or different systems.                                                                     |
| Messages must go through a communications protocol. | Messages sent to applications on the same system do not have to go through a communications protocol.                            |
| All messages are processed in the background.       | Messages are processed in either the foreground or background, based on the priority assigned by sending/receiving applications. |
| No support for event points.                        | Event points are supported.                                                                                                      |

The DHCP HL7 package assists DHCP applications in interfacing to the HL7 Protocol. In addition to the lower levels mentioned previously, all applications must perform the following upper level functions in order to exchange data with another application:

- Event analysis
- Data extraction
- Data filing
- Data formatting
- Message administration

Currently, the functions of event analysis, data extraction, and data filing must be performed by each application package. The DHCP HL7 package provides the following utilities to assist the application package with data formatting:

- Creation of HL7 Message Header (MSH) segments
- Utility calls to convert HL7 data to VA FileMan formats and vice versa
- Validation of Message Header information for all HL7 messages received
- A set of pre-defined variables for use in building HL7 messages/segments

The DHCP HL7 package provides the following functions to assist the application package with message administration:

- Support for tracking transmissions and providing a status for each
- Generation of reports on pending transmissions and transmissions with errors
- A queue for incoming and outgoing transmissions
- A real-time monitor that monitors active transmission links and their status’s

### DHCP HL7 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following ten DHCP HL7 routines from V. 1.5 and V. 1.6 are used by Laboratory UI.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>HLCHK</td>
<td>Validate data in the HL7 Message Header (MSH) segments of all incoming messages, and creates and "AR" error type acknowledgment messages.</td>
</tr>
<tr class="odd">
<td><p>HLFNC and</p>
<p>HLFNC1</p></td>
<td><p>Performs various functions such as:</p>
<p>Format names, dates, and times in HL7 or VA FileMan format.</p>
<p>Convert lower case letters to upper case, etc.</p></td>
</tr>
<tr class="even">
<td>HLLP</td>
<td>Implements the HL7 Hybrid Lower Level Protocol receiver/sender.</td>
</tr>
<tr class="odd">
<td>HLNTEG</td>
<td>Integrity routine for the DHCP HL7 package. Provides checksum for the DHCP HL7 routines.</td>
</tr>
<tr class="even">
<td>HLOPT</td>
<td>Main menu for HL7 module.</td>
</tr>
<tr class="odd">
<td>HLSERV</td>
<td>Server Routine for HL7 Messages received through MailMan</td>
</tr>
<tr class="even">
<td>HLTASK</td>
<td>Called to create a background task to start the HL7 Lower Level Protocol routine for a non-DHCP application and purge HL7 transmissions.</td>
</tr>
<tr class="odd">
<td>HLTF</td>
<td>Process HL7 transmission file entries for HL7 Messages.</td>
</tr>
<tr class="even">
<td>HLTRANS</td>
<td>Creates mail message and entry in the HL7 transmission file</td>
</tr>
</tbody>
</table>

### Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                  |                                               |
|------------------|-----------------------------------------------|
| Routine Name | Description                               |
| HLLP             | Serial connection driver for DHCP HL7 to GIM. |

Related Manuals

For HL7 information, you might also want to refer to the following manual:

- Health Level Seven (HL7) Standard version 2.2

Health Level Seven

3300 Washtenaw Ave, Suite 227

Ann Arbor, MI 48104-4250

\(313\) 677-7777

Email: <hq@hl7.win.net>

For applications using the V. 1.6 interface method, you might also want to refer to the following manuals:

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

# Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When everything is working correctly, the HL7 messages will not be visible to the user so knowledge of the details of their structure, location and transmission may not seem important.

However, when problems occur, troubleshooting will often require tracking and reading the messages to determine the cause of the problem. Problems often occur when a new instrument is being interfaced, but sporadic problems can be encountered also. New versions of software on the instrument or on DHCP can trigger problems.

Laboratory UI HL7 messages can be located in two different FileMan files. HL7 MESSAGE TEXT file (#772), in the HL7 package stores messages only briefly, but retains parameters about the message for a longer time. Laboratory UI HL7 messages are also stored in the LA7 MESSAGE QUEUE file (#62.49), and its associated information. Messages which are transmitted successfully will be given a purge status. These are purged every 24 hours. Error messages are kept seven days and then purged by Kernel. In addition to the message, an interpretation of the error is given. These messages are displayed in time sequence with the most recent being first.

HL7 FIELD LIST file (#771.1) is currently used for documentation only.

> **CAUTION:** If you use FileMan to print out messages, do not attempt to count the delimiter "\|" characters to determine the field number of a particular piece of data. FileMan uses the vertical bar for some formatting purposes, and will remove some of the bars that are actually in the global causing your field number counts to be erroneous if the segment contained null fields.

Example 1: A Segment Printed Directly from the Global

MSH\|^~\\\|LAB INTERFACE\|GenericInterfaceManager\|LA AUTO INST

\|142\|19940710001403\|\|ORU\|11812\|P\|2.1\|

Example 2: Same Segment Printed by FileMan

MSH\|^~\\\|LAB INTERFACE\|GenericInterfaceManager\|LA AUTO

INST\|642\|19940710001403\|ORU\|11812\|P\|2.1\|

## Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following HL7 segments are used to support the exchange of Laboratory data. Tables referenced in the segments can be found in the HL7 version 2.2 Standard document. For the standard HL7 segments, definitions of each elements are provided for those fields that are utilized in the Laboratory UI.

### MSA -Message Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSA segment contains information sent while acknowledging another message.

|                 |            |                        |
|-----------------|------------|------------------------|
| Sequence \# | Length | Field Element Name |
| 1               | 2          | Acknowledgment Code    |
| 2               | 20         | Message Control ID     |
| 3               | 80         | Text Message           |

MSA Field Definitions

Field 1: Acknowledgment Code (ID)

This field can have the following values.

|           |            |                    |
|-----------|------------|--------------------|
| Value | Length | Description    |
| AA        | 2          | Application Accept |
| AE        | 2          | Application Error  |
| AR        | 2          | Application Reject |

Field 2: Message Control ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

Field 3: Text Message (ST)

This is an optional text field that further describes an error condition. the text may be printed in error logs or presented to an end user.

If the incoming message could not be processed, an MSA segment will be built containing AR in the first field, the message control ID in the second field, and a free text string in the third field that describes the reason for rejecting to be used for debugging purposes. If no reject reason found, AA will be imbedded in the first field, and the message ID in the second field. This is returned to the DHCP HL7 package. It is not seen in the laboratory message queue.

### MSH - Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSH segment defines the intent, source, destination and some specifics of the syntax of a message. It is present in both uploads and downloads. Fields 3-6 will be reversed depending on whether the message is an upload or a download.

Each message is required to start with a MSH segment. In the Laboratory UI messages, immediately after the MSH is the field separator character "\|". Other encoding characters as described in the HL7 Standard section of this manual. Encoding characters operate on a single field in an HL7 segment. Each encoding character must be unique and none of the encoding characters may be the same as the field separator character. Each encoding character serves a specific purpose.

|                 |            |                        |
|-----------------|------------|------------------------|
| Sequence \# | Length | Field Element Name |
| 1               | 1          | Field Separator        |
| 2               | 40         | Encoding Characters    |
| 3               | 15         | Sending Application    |
| 4               | 20         | Sending Facility       |
| 5               | 30         | Receiving Application  |
| 6               | 30         | Receiving Facility     |
| 7               | 26         | Date/Time of Message   |
| 9               | 7          | Message Type           |
| 10              | 20         | Message Control ID     |
| 11              | 1          | Processing ID          |
| 12              | 8          | Version ID             |

MSH Field Definitions:

Field 1: Field Separator (ST)

This field serves as a separator and defines the character to be used as a separator for the rest of the message.

Field 2: Encoding Character Sequence (ST)

This field is four characters in the following order: the component separator, repetition separator, escape character , and subcomponent.

Field 3: Sending Application (ST)

This field is used for interface with lower level protocols.

Field 4: Sending Facility (ST)

This field addresses one of several occurrences of the same application within the sending system. This field is entirely site-defined.

This field is the three digit number identifying the medical center division, as found in the DHCP INSTITUTION file (# 4).

Field 5: Receiving Application (ST)

This field is used for interface with lower level protocols.

Field 6: Receiving Facility (ST)

This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations .

This field is the three digit number identifying the medical center division, as found in the DHCP INSTITUTION file (#4).

Field 7: Date/time of Message (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

YYYYMMDDHHMMSS

Field 9: Message Type ID (CM)

The receiving system uses this field to identify the data segments. This field is a coded value from the Message Type Table 0076.

- ORM=Order message
- ORU=Observation result/unsolicited

Field 10: Message Control ID (ST)

The message control ID is a sequential number that uniquely identifies the message transmitted by the sending system.

|           |                 |
|-----------|-----------------|
| Value | Description |
| P         | Production      |
| D         | Debugging       |
| T         | Training        |

Field 12: Version ID (ID)

This field is matched by the receiving system to its own version to be sure the message is interpreted correctly.

Field 8 and 13 through 17 are not used for laboratory messages.

### OBR - Observation Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBR is used to transmit information specific to an order for a diagnostic study or observation, physical exam or assessment. The observation request segment defines the attributes of a particular request for diagnostic services. For laboratory tests the information in the order segment usually applies to a single specimen. However, there is not a 1 to 1 relationship between specimen and tests ordered. Different test batteries will usually require their own order segments even when they can be performed on a single specimen. In this case the specimen information must be duplicated in each of the order segments that employ that specimen.

One or more OBR segments are present in all uploads and all download messages. The amount of information present in the OBR segment of the uploads will depend on whether it was preceded by a download. Some of the downloaded information is echoed back to DHCP in the corresponding upload. It also depends on whether the instrument is capable of receiving certain information and whether the driver on the GIM system is written to accept particular pieces of information.

<table style="width:100%;">
<colgroup>
<col style="width: 27%" />
<col style="width: 18%" />
<col style="width: 54%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sequence #</strong></td>
<td><strong>Length</strong></td>
<td><strong>Field Element Name</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>4</td>
<td>Set ID - Observation Request</td>
</tr>
<tr class="odd">
<td>2</td>
<td>75</td>
<td>Order Number (short or long ID)</td>
</tr>
<tr class="even">
<td>3</td>
<td>75</td>
<td>Filler Order Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>200</td>
<td>Test Code ^99001^^IEN LABORATORY TEST FILE 60xIEN LAB DATA NAME^TEST NAME^99002</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>Observation Date/Time #</td>
</tr>
<tr class="odd">
<td>8</td>
<td>26</td>
<td>Observation End Date/time #</td>
</tr>
<tr class="even">
<td>9</td>
<td>20</td>
<td>Collection Volume</td>
</tr>
<tr class="odd">
<td>12</td>
<td>60</td>
<td>Danger Code (Infection Warning)</td>
</tr>
<tr class="even">
<td>13</td>
<td>300</td>
<td>Relevant Clinical Information</td>
</tr>
<tr class="odd">
<td>14</td>
<td>26</td>
<td>Specimen Received Date/Time+</td>
</tr>
<tr class="even">
<td>15</td>
<td>300</td>
<td>Specimen Source ^^ "Control"</td>
</tr>
<tr class="odd">
<td>18</td>
<td>60</td>
<td>Placer Field 1 (Analyzer)^Card Address</td>
</tr>
<tr class="even">
<td>19</td>
<td>60</td>
<td><p>Placer Field 2</p>
<p>Tray^Cup^Accession Area^Accession</p>
<p>Date^Accession</p>
<p>Number^Accession^Universal</p>
<p>ID^Sequence Number</p></td>
</tr>
<tr class="odd">
<td>22</td>
<td>26</td>
<td>Results Report/Status Change -Data/Time +</td>
</tr>
<tr class="even">
<td>27</td>
<td>200</td>
<td><p>Quantity/Timing^Quantity^Interval^</p>
<p>Duration^Start Date/Time^End</p>
<p>Date/Time^Priority^Condition^Text^ Conjunction^Order Sequence</p></td>
</tr>
</tbody>
</table>

OBR Field Definitions

Field 1: Set ID - Observation Request (SI)

This field is a sequence number. For the first order transmitted, the sequence number is 1; for the second order, it is 2; and so on.

Field 2: Order Number (CM)

In DHCP this field contains the accession number (short or long UID).

Field 3: Filler Order Number (CM)

This field is the UID.

Field 4: Test Code (CE)

This field is a permanent identifier for an order and its associated observations.

> Subfields are:

> Identifier: CPT code or instrument code

> Test: Instrument code or null

> Name of coding system: "99001" This is a hard coded number used by DHCP to denote a user defined coding system. User defined coding systems start with the digit 9.

> Alternate identifier: ien (file name) file 60_X_ien (file name) file 63

> Alternate text: Test name in File \#60

> Alternate coding system: "99002" This is a hard coded number used by DHCP to denote a user defined coding system. User defined coding systems start with the digit 9.

Field 7: Observation Date/Time (TS)

This field contains the actual date and time of a specimen collection (YYYYMMDDHHMMSS).

Field 8: Observation End Date/Time (TS)

This field contains the end date and time of a specimen collection.

Field 9: Collection Volume (CQ)

This field is the volume of the collected specimen.

Field 12: Danger Code (CE)

This field is used for the infection warning.

Field 13: Relevant Clinical Information (ST)

This field is used to provide specimen comments.

Field 14: Specimen Received Date/Time (TS)

This field is the actual log-in time of a specimen at the diagnostic service.

Field 15: Specimen Source CM

The Specimen Source Table 0070, from the HL7 Standard is encoded in a DHCP routine. A field in the ETIOLOGY FIELD file (#61.2) must be filled in with a choice from the table. That choice will be inserted into the first subcomponent of this field. Other subcomponents defined by the standard are additives such as anticoagulants, method of collection, body site (example: leg) and site modifier (example: left or right).

Field 18: Placers Field \#1 (ST)

This field is used for the name of the instrument entry from the AUTO INSTRUMENT file.

Field 19: Placers field \#2

This field has eight subcomponents which may be used as needed by a particular instrument interface.

> 1\. Tray

> 2\. Cup

> 3\. Accession area (ien)

> 4\. FileMan accession date

> 5\. Accession number (terminal digits only)

> 6\. Accession--traditional (CH 0725 290)

> 7\. Universal ID (1051050200)

> 8\. Sequence \# from the instrument

Field 22: Results Report/Status Change-Date/Time

This field is used to indicate the date and time that the report is released .

Field 27: Quantity/Timing

This field contains information about how many services to perform at one service time and how often the service times are repeated, and to fix duration of the request. This field has 10 subcomponents. Only subcomponent number six, Priority (Star or Routine) is presently used in the laboratory standard.

Fields 3, 5 and 6, 10 and 11, 16 and 17, 20 and 21, 23 through 26, and 28-36 are not used for laboratory messages.

### Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NTE segments follow the OBRs. The NTE segments contain comments from the instrument. Comments contained in the NTE pertain to the entire test battery, not test specific. There can be more than one NTE and each will be stored as a comment in ^LAH.

|                 |                  |
|-----------------|------------------|
| Sequence \# | Element Name |
| 3               | Comments         |

NTE Field Definitions

Field 3: Comments

This field contains the comment.

Fields 1 and 2 are not used for laboratory messages.

### OBX - Observation Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OBX segment is present only in upload messages. The OBX segment is used to transmit a single observation or observation fragment. This segment represents the smallest indivisible unit of a report.

|                 |                                              |
|-----------------|----------------------------------------------|
| Sequence \# | Element Name                             |
| 1               | Set ID - Observational Simple (Sequence\*\*) |
| 2               | Value Type                                   |
| 3               | Observation Identifier                       |
| 4               | Observation Sub-ID                           |
| 5               | Observation Value                            |
| 6               | Units                                        |
| 7               | References Range                             |
| 8               | Abnormal Flags                               |
| 11              | Observe Result Status                        |

OBX Field Definitions

Field 1: Set ID - Observation Simple (SI)

Set ID - Observation Simple is a sequence number used to identify the segment repetitions.

Field 2: Value Type (ID)

This field is the format of the observation value in OBX. Refer to the Value Type Table 0125 of the HL7 Standard.

Field 3: Observation Identifier (CE)

This field is a unique identifier for the observation. There are six components: ID, text, name of coding system, alternate ID, alternate text, name of alternate coding system.

Field 4: Observation Sub-ID (ST)

This field can be used to:

- distinguish between multiple OBX segments with the same observation ID organized under one OBR
- group related components in reports such as surgical pathology,
- organize the reporting of some kinds of fluid intakes and outputs

Field 5: Observation Value (\*)

This field is the value observed by the observation producer.

Field 6: Units (CE)

This field is a coded element made up of identifier, text, and name of coding system. The default coding system for Units consists of the ISO abbreviations as defined in section 7.1.4 of the HL7 version 2.2 Standard.

Field 7: Reference Range (ST)

This field is a numeric value, lower limit - upper limit, e.g., for potassium, 3.5 -4.5.

Field 8: Abnormal Flags (ID)

This field is a table lookup indicating the normalcy status of a report. Refer to Abnormal Flags Table 0078 in the HL7 Standard.

Field 11: Observe Result Status (ID)

This field reflects the current completion status of the results for one Observation Identifier.

Fields 9 - 10 and 12 through 16 are not used in the laboratory messages.

### ORC - Common Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORC segment is present only in downloads. The ORC segment is used to transmit data elements that are common to all orders (all types of services that are requested). The ORC segment is required in the ORM message.

Sequence \# Element Name

|                 |                     |
|-----------------|---------------------|
| Sequence \# | Element Name    |
| 1               | Order Control       |
| 3               | Filler Order Number |
| 5               | Order Status        |
| 12              | Ordering Provider   |

ORC Field Definitions

Field 1: Order Control (ID)

This field determines the function of the order segment. This field may be considered the "trigger event" identifier for orders. The codes fall roughly into the following categories:

- Event request- codes like "NW" (new order) and "CA" (cancel order request) that are intended to initiate an event.
- Event acknowledgment- codes like "OK" (orders accepted) and "CR" (canceled as requested) that are intended to reply to an application that requested an event.
- Event notification - codes like "OC" (order canceled) and "OD" (order discontinued) that are intended to notify another application that an event has occurred.

In the Laboratory UI, NW = New order is hard coded into every ORC segment.

Field 3: Filler Order Number (CM)

This field is the order number associated with the filling application. This field contains the DHCP order number on the download messages.

Field 5: Order Status (ID)

The purpose of this field is to report the status of an order either upon request (solicited).

Field 12: Ordering Provider (CN)

This field contains the identity of the person who is responsible for creating the request (i.e., ordering physician).

Fields 2, 4, 6 through 11, and 13 through 19 are not used in the laboratory messages.

### PV1 - Patient Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV1 segment is present in downloads. PV1 segment will be echoed back in uploads if there was a previous download.

|                 |                           |
|-----------------|---------------------------|
| Sequence \# | Element Name          |
| 1               | Set ID - Patient Visit    |
| 3               | Assigned Patient Location |

PV1 Field Definitions

Field 1: Set ID - Patient Visit (SI)

This field is a number that uniquely identifies this transaction for the purpose of adding, changing, or deleting the transaction. for those messages that permit segments to repeat, the set ID field is used to identify the repetitions. For example, the swap and query transactions allow for multiple PID segments would have Set ID values of 1, 2, then 3, etc. When defined, the sequence is always "1" in Laboratory UI messages.

Field 3: Assigned Patient Location (CM)

This field is the assigned patient location.

Fields 2, and 4 through 25 are not used in the laboratory messages.

### PID - Patient ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment originates on downloads and echoes back on upload. If no downloads, not present on uploads.

|                 |                      |
|-----------------|----------------------|
| Sequence \# | Element Name     |
| 3               | LRDFN^CHECKSUM^M11   |
| 5               | Patient Name         |
| 7               | Date of Birth        |
| 8               | Sex                  |
| 19              | SSN Number - Patient |

PID Field Definitions

Field 3: Patient ID (Internal ID) (CM)

This field is a composite element made up of the following components: patient ID (LRDFN), check digit, and check digit scheme used to calculate the check digit.

Field 5: Patient Name (PN)

The subcomponents are last name, first name, middle initial, and suffix such as Jr., prefix such as Dr., degree such as MD.

Field 7: Date of Birth (DT)

This field is the patient's date of birth (YYYYMMDD)

Field 8: Sex (ID)

This field is the patient's sex.

Field 19: SSN Number (ST)

This field is the patient's social security number.

Fields 1 and 2, 4, 6, 9 through 18, and 20 through 27 are not used in the laboratory messages.

## Message Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Message types are defined by the HL7 Standard in the Message Type Table 0076. There are two types used by the Laboratory HL7 interface.

1\. General Order Message (ORM)

The function of this message is to initiate the transmission of information about an order. This includes placing new orders, cancellation of existing orders, discontinuation, holding, etc.

Downloads are ORM message types.

2\. Unsolicited Transmission of an Observation (ORU)

For each patient order (OBR segment) more results may be transmitted depending upon the number of observations generated by the order.

All uploads are ORU message types.

## HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following are some examples of HL7 messages used in the Laboratory Universal Interface. These are examples of actual download requests and upload results messages. This is not a complete interface specification, but might be useful to begin work toward a DHCP compliant interface.

This first message is a simple results message . A field by field breakdown is included to show the DHCPs particular requirements. A results message requires at least one MSH, Observational Request Segment ( OBR), and Result Segment (OBX).

Example: Simple Results Message

MSH\|~^\\\|LA AUTO INST\|695\|LAB INTERFACE\|Generic Interface Manager

\|19960227084324\|\|ORM\|350988\|P\|2.2

PID\|\|\|33466~0~M11\|\|LABPATIENT~ONE\|\|000000001\|M\|\|\|\|\|\|\|\|\|\|\|111-11-1111

PV1\|\|\|LPC

ORC\|NW\|\|38277\|\|\|\|\|\|\|\|\|~LABPROVIDER, TWO

OBR\|1\|1560580026\|\|441\~~99001~1244X695003~PROSTATE SPECIFIC ANTIGEN~99002\|

\|\|19960227084325\|\|\|\|\|\|\|\|SER\|\|\|AXSYM\|\~~24~2960227~26~SC 022

7 26~1560580026~\|\|\|\|\|\|\|\|\~\~\~\~~R

MSH\|^~\\\|LAB INTERFACE\|Generic Interface Manager\|LA AUTO INST\|695

\|19960227103316\| \|ORU\|53801\|P\|2.2

PID\|1\|\|33466\|\|LABPATIENT~ONE\|\|\|\|\|\|\|\|\|\|\|\|\|\|

OBR\|1\|1560580026\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|AXSYM\|^^24^2960227^26^SC 0227 26^1560580026

OBX\|1\|ST\|441^^^1244X695003^PROSTATE SPECIFIC ANTIGEN^99002\|\|1.15\|ng/ml\|0.00 TO

4.00\|\|\|F

This messages represent a download test request message . The Patient Identification Segment (PID) and Patient Visit Segment (PV1) fields in the download are straight forward.

Example: Download Request Message

MSH\|~^\\\|LA AUTO INST\|695\|LAB INTERFACE\|Generic Interface Manager

\|19950725133514\|\|ORM\|2950725.133514\|P\|2.1

PID\|\|\|56535~2~M11\|\|LABPATIENT~TWO\|\|000000002\|M\|\|\|\|\|\|\|\|\|\|\|111 -11-1111

PV1\|\|\|LORTH

ORC\|NW\|\|130424\|\|\|\|\|\|\|\|\|~LABPROVIDER, THREE

OBR\|1\|1052060288\|\|82374~02A~99001~55X454~BICARBONATE ---------O~99002\|

\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725

288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|2\|1052060288\|\|82251~11A~99001~186X695168~BILIRUBIN, TOTAL

-----~99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~

CHE 0725 288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|3\|1052060288\|\|84075~35A~99001~188X17~ALKALINE PHOSPHATASE

-~99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725

288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|4\|1052060288\|\|84460~31A~99001~191X20~SGPT -----------------~

99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725

288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|5\|1052060288\|\|84132~01B~99001~1442X6~POTASSIUM -----------O~

99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725

288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|6\|1052060288\|\|84295~01A~99001~1443X5~SODIUM --------------O~

99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725 288~

1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

OBR\|7\|1052060288\|\|82435~04A~99001~1444X7~CHLORIDE ------------O~

99002\|\|\|19950725133542\|\|\|\|\|\|\|\|SER\|\|\|CX7CL -IM\|\~~11~2950725~288~CHE 0725

288~1052060288~\|\|\|\|\|\|\|\|\~\~\~\~~R

Example: Upload of Results Message

Some of the fields in the download are echoed back in the results message:

PID\|1\|\|111 -11-1111\|\|

\_SSN echoed, PV1 not required

OBR\|1\|1052060285\|\|\|\|\|\|\|\|\|\|\|\|\|SER\|LABPROVIDER, ONE\|\|CX7A -IM\|46^1^^^^^^42865\|\|\|

\_echoed from download

OBR\|1\|1052060285\|\|\|\|\|\|\|\|\|\|\|\|\|SER\| LABPROVIDER, ONE\|\|CX7A -IM\|46^1^^^^^^42865\|\|\|19

950725135024\|\|\|\|\|^^^^^

\_46^1 represents the tray/cup

as downloaded, but is also used

on unidirectional when tray cup

is the only method for identifying

the specimen. 3rd component is the

tray, 4th component is the cup.

Components 1 and 2 would be empty

in the case of a unidirectional

upload by tray cup.

OBX\|1\|ST\|82251^^^\|\|0.9\|mg/dl\|\|\|\|\|F

\_alternate test code echoed

Glossary

ACK/NAK A type of software handshake method. Before sending data the sender must receive permission from the receiver. If the data is flawed, the receiver sends back the NAK character and the sender will re-send the data.

ArnetBoard PC circuit board to provide multiple serial connections for lab instruments to transmit data.

ASTM American Society for Testing and Materials. This organization has two standards for communication between laboratory analyzers and information systems. E1381 defines protocol and E1394 defines format/content. These standards are totally separate from the HL7 standard. Some of the newer instruments are using these for their data stream, but the various implementations are still not totally similar with each other.

Automatic Download Patient demographics and tests ordered are automatically formatted and transmitted either directly to a lab instrument or to a location where the instrument can query directly for the information. The automatic transmission usually occurs as soon as the accession number is created.

Baud Rate The number of discrete signaling events that occur on a transmission line in a second. For binary digital transmission, a baud is a bit per second. Common rates are usually multiples or halves or quarters of 600. Baud rate divided by 10 is approximately equal to the number of characters/second that are transmitted at a given rate.

Bidirectional Communication between two computers or devices which occurs in both directions. Old style interfaces were usually unidirectional. That is, the host computer "listened" continuously for incoming data. The instrument transmitted whenever there was data available and always assumed the data was received. Bidirectional communications are much more complicated since nothing is assumed and both sides are "listening" continuously. No communication takes place without permission and data received is checked and acknowledged. In newer instruments even unidirectional interfaces have a bidirectional component. That is, the instrument will not release data until it has received permission from the host to send it. This permission may only consist of a single invisible character, but without it there is no data flow. There may also be error checking communications between devices in unidirectional interfaces.

Breakout Box A device used for testing electrical activity on each individual wire in a cable connecting two computers or devices. It is used for troubleshooting interface wiring problems and building communication cables. It allows you to experiment with connector signals by attaching jumper wires between pins that correspond to various RS 232 signals.

Checksum A specific calculation is performed on the contents of a message or packet of data. This checksum is sent with the data. The same calculation is performed by the receiver of the data. If they do not match, the data is rejected and the sender is requested to re-send.

Cluster A term used by a vendor to describe a configuration where similar instruments are functionally treated as a single entity. Test requests are sent to the cluster without specifying a single instrument. The specimen may be placed on any instrument in the cluster. Instruments using this configuration must be capable of host query or test request download.

Communication Parameters Various electronic specifications that define the characteristics of the signals such as the timing and sequence for coding and decoding information being passed from one device to another. Examples of common parameters are baud rate, parity, \# of data bits and \# of stop bits.

Communication Protocol Computer program which defines the rules for data transfer between two devices or computers. The same protocol must be defined at both ends of the transmission. Some common examples of protocols are XON/XOFF, ACK/NAK, Kermit, TCP/IP. Some protocols are designed for modems and some for networks and others intended for devices connected to a single computer. They may have different purposes and varying degrees of complexity.

Data Stream The format, content, sequence and timing of the information transmitted and/or received by computer devices such as lab instruments. There is very little standardization among manufacturers. A given instrument may indeed have several different data streams simultaneously, and it is common for instrument software upgrades to significantly alter the data stream rendering the interface useless.

DB25 Male/Female The RS232 standard specifies the use of a D connector with 25 pins (male) or holes (female) in two rows with 13 on top and 12 on the bottom. The "B: refers to the connector's shell size. Instruments may use either male or female connectors and may have varying numbers of the 25 wires actually connected.

DB9 Male/Female Since most RS232 connections only use a few pins of the RS-232 specification, a 9 pin connector is often used to save space. The pin numbers do not necessarily correspond to the same pin numbers on the DB 25.

Decserver Port Physical connection used to link peripheral devices to the DEC DHCP computers.

Direct Connect A lab DHCP term denoting a lab instrument (which may be either unidirectional or bidirectional) that is connected directly to a dedicated port on the DHCP computer. Such an interface bypasses the LSI or other intermediate data receiver. Each direct connect interface requires a separate background job on DHCP to intercept its data.

Driver Computer program which transports electronic information such as data or commands going between two computers or devices.

DSR Display Response Message

EIA Electronics Industry Association

Equinox Port Physical connection to link peripheral devices to MSM DHCP computers.

Ethernet Card Circuit board which allows network port connections.

EVN Event Type Segment

FRAMING The method used to delimit characters in asynchronous serial communications. Each character is preceded by a start bit (space) and followed by a stop bit (mark), with a continuous marking condition indicating no transmission.

HANDSHAKING An electronic method of granting permission to transmit data between two computers or devices. This can be done via software using a pair of ASCII characters sent over the data send and receive lines such as ACK/NAK or can be done via separate wires specially dedicated to the purpose such as Clear to Send (CTS) and Ready to Send (RTS). Lab instrument interfaces may provide hardware communications, but the DHCP computer does not utilize these so if present, they are disables by directly connecting the corresponding pins in the instrument cable connection.

HL7 Standard Set of written rules and specifications for computer programmers to use to format medical information in a uniform way so it can be transported from one computer system to another.

HL7 DHCP Package Software to manage, store and route HL7 formatted messages between DHCP packages and other computer systems. It handles low level handshaking and physical delivery and receipt of messages between systems.

HL7 LAB Interface Software to encode data into the HL7 format and to decode HL7 messages into lab global for use by standard DHCP lab options.

Host Query A type of bidirectional interface where the instrument requests the ordering information and patient demographics directly from the main computer or some intermediate computer GIM PC when the instrument has a sample accession number read from a bar code off the specimen tube or the instrument has the accession number and location of the specimen by some other means. The Host system must reply to the query within a time frame (usually a few seconds) which is set by the lab instrument.

ISO International Standards Organization. A voluntary international group of national standards organizations including ANSI, that issues standards in all areas including computers and information processing.

Kermit A public domain file transfer protocol developed at Columbia University to transfer files from one computer to another. Some lab instruments use this protocol. Kermit transfers data by breaking it up into pieces and encapsulating the pieces within packets. It requires a special set of routines on both sender and receiver computers to pack and unpack the data being transferred.

LAT Local Area Transport A proprietary network protocol for communicating to multiple devices (computers or terminal servers) via a single physical line.

Line Monitor Device which can be inserted into the cable connecting two computers or devices. The monitor will detect electrical activity on selected wires in an RS232 circuit.

LSI Large Scale Integrator. A "black box" device used to concentrate incoming data from as many as 8 lab instruments and then pass that data to the DHCP computer through a single port.

Manual Download Lab orders and patient demographics are sent directly to a specific lab instrument or to some intermediate device such as the GIM PC. This is initiated manually by a technologist who builds a worklist and then uses a DHCP option to download the information.

MSA Message acknowledgment

MSH Message header

Multiplexor Physical device or circuit board which allows one device to connect to multiple other devices. Specific transport protocol software is needed to route data to and from a multiplexor.

NTE Notes and comments segment. These segments contain comments from the instrument, comments contained in the NTE refer to the entire test battery, not test specific. NTE comments are not allowed anywhere except after the OBR. There can be more than one NTE. Each will be stored as a comment in ^LAH.

Null Modem A pair of connectors usually with cable between them allowing 2 computers or devices to be directly connected without intervening modems ormultiplexers, supplying the required RS-232 signals by means of cross-connections and jumpers.

OBR Observational Request segment

OBX Result segment

ORC Common order segment

OCF Order Confirmation Message type

ORC Observational Result/Record Response Message type

ORM Order message type

ORR Order response message

ORU Observational results unsolicited message type

OSI Open System Interconnection

OSQ Order Status Query Message type

Parity A method to detect errors in binary information. It requires 7 bits to represent a character, but 8 bits are sent. If you are using odd parity, the sender will count the number of 1's in the 7 bits of the character. If it is odd, the sender will put 0 in the 8th bit. If it is even, the sender will put 1 in the 8th bit. In other words odd parity means that the parity bit will be whatever is required to make the total number of 1's in the 8 bit character odd. For even parity, reverse the above procedure. When the receiver gets the character, it also calculates the parity. If it doesn't match with what was received, there is an error and there may be an unusual character displayed on the screen, but there is no provision to correct the error so it is of little help to use it. Mark and space parity always place either a mark or a space in the 8th bit of every character. No parity means the 8th bit is ignored.

PID Patient identification segment

PV1 Patient Visit Segment

QRY Query message type

Router A computer or self-contained unit of a computer which makes decisions about which path incoming and outgoing data traffic will take to reach its destination. A router can also filter traffic to restrict or detect errors in data transmissions.

RS232 An EIA standard that gives the electrical and functional specification for serial binary digital data transmission, the most commonly used interface between computers, terminals and other computer devices and instruments.

Serial Port Physical connection on a computer used for RS232 data transmission. All data is transferred over a single wire in sequential fashion.

Stop Bits In asynchronous serial transmission, the mark (1 bit) that terminates a character. It lasts for at least one bit time and thereafter until the next character starts to arrive.

TCP/IP A network protocol for communicating to multiple systems via a single physical line.

UDM Unsolicited Display Message type

UI Universal Interface

UID Unique identifier. 10 digit number which identifies a specimen.

Unidirectional A type of communication between two computers or devices where data only flows in one direction. In terms of lab interfacing, this is usually from a lab instrument to the DHCP computer directly or to an intermediate device such as the LSI or the Universal Interface which in turn sends the information to the DHCP computer. (See also bidirectional).

URD Results/Update definition Segment

XON/XOFF A data flow control method where the receiver sends an XOFF character when its input buffer is close to being full and an XON when it has room to receive more data. The XON and XOFF are sent over the same wire that the device uses to send data.

Appendix A. Data Innovations Software Configuration

Option \#1: Multi-Port Serial board (8 to 64 connections)

In this configuration, all devices are connected to the Instrument Manager using an

Arnet multi-port serial board. A single connection to DHCP assumes the use of the

DHCP Laboratory Universal Interface (HL7 protocol). If the Universal Interface is

not available, the Instrument Manager can be interfaced to DHCP in Instrument

Emulation Mode. The Instrument Manager can be setup to emulate one of the sites

existing interfaces. Listed below is an example of instrument emulation:

Option \#2: Serial connection to DHCP, DEC LAT to instruments using Terminal

Servers

The above example makes use of the Instrument Managers ability to communicate

using the DEC LAT network protocol. Instruments are connected to Terminal

Servers throughout the institution. The Terminal Servers are attached to the

Ethernet network. The Instrument Manager can connect to the individual Terminal

Server ports using an Ethernet adapter and the LAT protocol. This allows the

Instrument Manager to be placed anywhere in an institution (Lab, IRM, etc.).

Option \#3: TCP/IP connections to DHCP, DEC LAT to instrument using Terminal

Server

The above example demonstrates the Instrument Manager running two network

protocols simultaneously. The DEC LAT protocol is used for communicating with

instruments via Terminal Servers. The TCP/IP protocol is used to communicate

with the DHCP system. Since TCP/IP can use the Ethernet network,

communication speeds between DHCP and GIM are much faster than standard

serial communications.

Option \#4: TCP/IP connection to DHCP, DEC LAT to instruments, remote lab using

T1

The GIM can access instruments in remote (off-site) labs if the remote sites are

connected to the main network. The above example shows the use of a T1 link to

create a wide area network (WAN).

Appendix B. Dawning Software Configuration

## ## ## ## ReseultNet Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Host Format Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SEND Application : Laboratory Interface

Facility : Dawning

RECV Application : LA Auto Instruments

Facility : This field is site specific

DELIM Field : 7C

Component : 5E

Repeat : 7E

Escape : 5C

Sub-Component : 26

DWNLD Details : Yes

### ### HL7 Host Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Device : COM1

Protocol : Hybrid

BLOCK Start : OB

End : 1C

CKSUM Enabled : Yes

PACK Data : Yes

### Operational

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HOST Enabled : Yes

Transmit : Yes

Protocol : Serial

Format : HL7

AUX Enabled : Yes

Transmit : Yes

Protocol : Block

Format : CDF