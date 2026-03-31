---
title: HL7 HL*1.6 HLO System Manager Manual
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: anchor
doc_subject: HLO System Manager Manual
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - span
  - message
  - table
  - contents
  - class
  - mark
  - link
  - listener
  - process
  - service
page_count: 0
word_count: 20860
section_count: 41
table_count: 9
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 3
revision_newest: 10/28/2009
revision_oldest: 4/24/09
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hlo_system_manager_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hlo_system_manager_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

VistA Messaging Services

Health Level Seven Optimized (HLO)

System Manager Manual

![](hl7-hl-1-6-hlo-system-manager-manual/001.png)

Software HL\*1.6

Document Revision 1.1

VA Office of Information and Technology (OI&T)

Veterans Health Information Technology (VHIT)

VistA Messaging Services

(*This page left blank for two sided printing*)

Revision History

|            |          |                                                                      |          |
|------------|----------|----------------------------------------------------------------------|----------|
| Date       | Revision | Description                                                          | Author   |
| 4/24/09    | 1        | Created a System Manager Manual from the Technical Manual (VMS_CR 3) | REDACTED |
| 9/28/09    | 1.1      | Technical Edit (VMS_CR 3)                                            | REDACTED |
| 10/28/2009 | 1.1      | Added changes suggested by SQA                                       | REDACTED |

Patch Revisions

For a complete list of patches related to this software, please refer to the National Patch Module on FORUM.

(*This page left blank for two sided printing*)

Contents

(*This page left blank for two sided printing*)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Documentation Conventions](#documentation-conventions)
  - [Screen Dialog](#screen-dialog)
  - [Software Processes and Code](#software-processes-and-code)
  - [API Parameters](#api-parameters)
- [HL7 (Health Level Seven)](#hl7-health-level-seven)
  - [Brief Overview](#brief-overview)
  - [HL7 Standard](#hl7-standard)
    - [Unsolicited Updates](#unsolicited-updates)
    - [Acknowledgements](#acknowledgements)
    - [Queries](#queries)
  - [History of the VistA HL7 Package](#history-of-the-vista-hl7-package)
    - [HL7 Standard Support](#hl7-standard-support)
    - [Evolution of VistA HL7](#evolution-of-vista-hl7)
- [HL Optimized (HLO)](#hl-optimized-hlo)
  - [Overview and Background](#overview-and-background)
  - [Design Highlights](#design-highlights)
  - [HLO Developer Perspective](#hlo-developer-perspective)
  - [HLO System Manager Perspective](#hlo-system-manager-perspective)
- [HLO Installation and Configuration](#hlo-installation-and-configuration)
  - [Install the HLO Software Patch](#install-the-hlo-software-patch)
    - [A Note About System Parameters](#a-note-about-system-parameters)
  - [Define the Server Logical Link](#define-the-server-logical-link)
  - [Update the HLO SYSTEM PARAMETERS File (#779.1)](#update-the-hlo-system-parameters-file-7791)
  - [Schedule the HLO COUNT RECORDS Option](#schedule-the-hlo-count-records-option)
  - [Schedule the HLO SYSTEM STARTUP and the HLO DAILY STARTUP Option](#schedule-the-hlo-system-startup-and-the-hlo-daily-startup-option)
  - [Start HLO using the HLO System Monitor](#start-hlo-using-the-hlo-system-monitor)
  - [Create and Activate the TCP/IP Services for Open VMS](#create-and-activate-the-tcpip-services-for-open-vms)
- [Listeners](#listeners)
  - [Introduction](#introduction-1)
    - [Client and Server Roles in HLO over TCP/IP](#client-and-server-roles-in-hlo-over-tcpip)
    - [TCP/IP Connection Requirements](#tcpip-connection-requirements)
  - [Multi-Threaded Listeners](#multi-threaded-listeners)
  - [TCP/IP Services for Open VMS](#tcpip-services-for-open-vms)
    - [Introduction](#introduction-2)
    - [TCP/IP Services for OpenVMS](#tcpip-services-for-openvms)
    - [TCP/IP Services and VistA HLO](#tcpip-services-and-vista-hlo)
    - [Requirements for Setting up a TCP/IP Service on OpenVMS](#requirements-for-setting-up-a-tcpip-service-on-openvms)
    - [Recommended Naming Conventions](#recommended-naming-conventions)
    - [Creating TCP/IP Services for Open VMS with Cache](#creating-tcpip-services-for-open-vms-with-cache)
    - [Creating a TCP/IP Services for Open VMS with DSM](#creating-a-tcpip-services-for-open-vms-with-dsm)
  - [TaskMan Multi-Threaded Listener](#taskman-multi-threaded-listener)
    - [Set up the Server Logical Link](#set-up-the-server-logical-link)
    - [Configure the HLO Standard Listener Record in the HLO System Parameter File](#configure-the-hlo-standard-listener-record-in-the-hlo-system-parameter-file)
- [HLO Management System](#hlo-management-system)
  - [Main Menu](#main-menu)
  - [System Monitor](#system-monitor)
    - [Overview](#overview)
    - [Actions](#actions)
  - [Message Viewer](#message-viewer)
    - [Overview](#overview-1)
    - [Actions](#actions-1)
    - [DM – Display Message/Resend:](#dm-display-messageresend)
    - [DM – Display Message/Reprocess:](#dm-display-messagereprocess)
    - [DM – Display Message/Visual Parser:](#dm-display-messagevisual-parser)
    - [MS – Message Search](#ms-message-search)
  - [Application Registry (HLO)](#application-registry-hlo)
    - [Overview](#overview-2)
  - [TaskMan-Scheduled Options](#taskman-scheduled-options)
    - [HLO COUNT RECORDS](#hlo-count-records)
    - [HLO SYSTEM STARTUP](#hlo-system-startup)
    - [HLO Daily STARTUP](#hlo-daily-startup)
  - [HLO MESSAGE STATISTICS REPORT](#hlo-message-statistics-report)
- [Appendix A - The HLO Process Registry](#appendix-a-the-hlo-process-registry)
  - [HLO Processes](#hlo-processes)
  - [The HLO Process Manager](#the-hlo-process-manager)
    - [HLO PROCESS REGISTRY File (#779.3)](#hlo-process-registry-file-7793)
    - [Process Manager Operation](#process-manager-operation)
    - [Generic Framework Process](#generic-framework-process)
- [Appendix B – Creating TCP/IP Services for Open VMS with DSM](#appendix-b-creating-tcpip-services-for-open-vms-with-dsm)
  - [Create OpenVMS User Account](#create-openvms-user-account)
  - [Create OpenVMS Home Directory](#create-openvms-home-directory)
  - [Create a DCL Command Procedure](#create-a-dcl-command-procedure)
  - [Set Up the TCP/IP Service](#set-up-the-tcpip-service)
  - [Enable and Save the TCP/IP Service](#enable-and-save-the-tcpip-service)
  - [Access Control List (ACL) Issues](#access-control-list-acl-issues)
  - [Control the Number of Log Files Created by TCP/IP Services](#control-the-number-of-log-files-created-by-tcpip-services)
  - [Other TCP/IP Service Commands](#other-tcpip-service-commands)
- [Appendix C – Daily Oversight and Troubleshooting](#appendix-c-daily-oversight-and-troubleshooting)
  - [Daily Oversight](#daily-oversight)
    - [HLO System Monitor](#hlo-system-monitor)
  - [HLO Message Viewer](#hlo-message-viewer)
  - [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [# Index](#index)
Welcome to the *VistA HLO System Manager Manual*. The goal of this manual is to provide VistA developers and system managers with all the information they need to build VistA HL7 interfaces and manage the VistA HLO software package.
The Technical Manual is organized for the following user types:
> All Users Chapters 1 and 2
> Installer Chapters 3 and 4 plus Installation Manual
> Manager/Maintenance Chapter 5
> Developer Chapter 6 and Appendices

# Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Screen Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual presents snapshots of computer dialogue or other online displays in a non-proportional font. User responses to online prompts are highlighted in bold. Pressing the Enter key is illustrated as \<Enter\>, and is only shown when the user doesn’t type anything at the prompt besides pressing the Enter key. For example, the following indicates that the user should enter two question marks followed by \<Enter\> when prompted:

> Select Primary Menu option: ??

> Following menu options are available……

> Select Primary Menu option: \<Enter\>

## Software Processes and Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Processes are indicated with single quotes.

Code is indicated with double quotes.

## API Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each API that is documented for developer use also includes input and output parameters. If a parameter isn’t specifically documented as being passed by reference, then it is to be passed by value.

# HL7 (Health Level Seven)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Brief Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 is an ANSI messaging transaction standard for healthcare. It is the main strategy used by a variety of healthcare providers and applications vendors to achieve Enterprise Application Integration (EAI) between disparate clinical applications.

From the HL7 standard:

> Health Level Seven (HL7) is an application protocol for electronic data exchange in health care environments. The HL7 protocol is a collection of standard formats which specify the implementation of interfaces between computer applications from different vendors. This communication protocol allows healthcare institutions to exchange key sets of data among different application systems. Flexibility is built into the protocol to allow compatibility for specialized data sets that have facility-specific needs.[^1]

Because many vendors support the HL7 standard, it allows healthcare institutions to exchange key sets of data from very different application systems. HL7 defines:

- The data to be exchanged
- The timing of the interchange
- The communication of errors to the sending/receiving application

HL7 *messages* are the unit of data exchange between systems. HL7 message formats, although standardized, are generic in nature, and must be configured (negotiated) to meet the specific needs of the two applications involved. As such, HL7 interfaces between applications are not "plug and play” and must be formally negotiated between the two applications.

The HL7 standard defines standard messages for the following healthcare application areas:

- Patient Administration (e.g., admission, discharge, transfer)
- Order Entry
- General Queries
- Financial Management (e.g., charges, payments, adjustments, and insurance)
- Observation Reporting
- Master Files
- Medical Records/Information Management
- Scheduling
- Patient Referral
- Patient Care

## HL7 Standard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An HL7 message is the atomic unit for transferring data between systems in the HL7 standard. Each message has a header segment composed of a number of fields, including fields containing the message type (for HL7 versions 2.2 and above) and event type. These are each three-character codes, defined by the HL7 standard. The type of a transaction is defined by the message type/event type pair (again for HL7 versions 2.2 and above). Rules for constructing message headers and messages are provided in the *Control* chapter of the HL7 standard.

An HL7 message consists of one or more HL7 *segments*. A segment is similar to a record in a file. Each segment consists of one or more fields separated by a special character called the *field separator*. The field separator character is defined in the Message Header (MSH) segment of an HL7 message. The MSH segment is always the first segment in every HL7 message, except for batch HL7 messages, which begin with the Batch Header (BHS) segment.

In addition to the field separator character, four other special characters, called *encoding characters*, are used as delimiters. The encoding characters and the field separator are defined in the MSH or BHS segment. Each encoding character must be unique and serves a specific purpose. None of the encoding characters can be the same as the field separator character. The four encoding characters are defined as:

- *Component separator*. Some data fields can be divided into multiple components. The component separator character separates adjacent components within a data field.
- *Repetition separator*. Some data fields can be repeated multiple times in a segment. The repetition separator character separates multiple occurrences of a field.
- *Escape character*. Data fields defined as text or formatted text can include escape sequences. The escape character is used to start and end escape sequences within the actual text.
- *Sub-component separator*. Some data fields can be divided into components, and each component can be further divided into sub-components. The sub-component separator character separates adjacent sub-components within a component of a field.

The following is an example of an HL7 message:

MSH\|^~\\\|ORDER\|REDACTED\|RESULTS\|500\|19900314130405\|ORU^R01\|523123\|D\|2.3\|

PID\|\|7777790^2^M10\|\|HL7Patient^One\|\|\|\|\|\|\|\|123456789\|

OBR\|\|2930423.08^1^L\|\|199304230800\|\|\|\|\|\|\|DERMATOLOGY\|

OBX\|CE\|10040\|OV\|1^0^0^0^0\|

OBX\|CE\|11041\|PR\|

OBX\|CE\|216.6\|P\|

OBX\|ST\|VW^WEIGHT^L\|\|120\|KG

OBX\|ST\|VB^BLOOD PRESSURE^L\|\|120/80\|MM HG

OBX\|ST\|VT^TEMPERATURE^L\|\|99\|C

OBX\|ST\|VP^PULSE^L\|\|75\|/MIN

The following is an analysis of the message:

- The first line of the message is the message header (MSH) segment.
- The message type (from the MSH segment) is Observation Result/Unsolicited (ORU).
- The event type (from the MSH segment) is an unsolicited transmission of an observation message (R01).
- The second line of the message is the second segment, Patient Identification (PID).
- The third line of the message is the third segment, an Observation Request (OBR).
- The subsequent lines of the message are multiple Observation/Results (OBX) segments.

### Unsolicited Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary characteristic of an unsolicited message is that it is broadcast by an application to one or more recipients, without being solicited by those recipients. Unsolicited updates are typically sent by an application when an *event point* occurs in that application:

> The Standard is written from the assumption that an event in the real world of healthcare creates the need for data to flow among systems. The real-world event is called the trigger event. For example, when a patient is admitted, a trigger event might occur that will send data about that patient to a number of other systems. The trigger event might occur when an observation (e.g., a CBC result) for a patient is available, causing information from the observation to be sent to a number of other systems. When the transfer of information is initiated by the application system that deals with the triggering event, the transaction is termed an unsolicited update.[^2]

Healthcare information systems that support HL7 typically provide a mechanism for applications to subscribe to event points that may be of interest. Each unsolicited update, representing a clinical event, is distributed to every "interested" application that subscribes to the event. For example, when a patient is registered by VistA, an ADT A04 message is generated and delivered to all subscriber applications interested in patient registrations.

Unsolicited updates are also used to aggregate data from VistA systems to Austin and other centralized databases.

### Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a message is sent to a system, return of an *acknowledgement* (also referred to as an “ACK”) message from the receiving system may be required as part of the defined transaction:

- An *accept acknowledgement* (also called a commit acknowledgement) confirms that the receiving system has received the message that was sent.
- An *application acknowledgement* confirms that the receiving application was able to process the sender’s message.

The type of acknowledgement returned for any given message depends on the negotiated interface between the systems.

### Queries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary characteristic of a query message is that the system that needs the information connects as a client to the server system that has the needed information. For example, to query the Master Patient Index (MPI) for demographic data and a list of treating facilities for a patient, a VQQ (virtual table query) message is sent from the VA facility to the MPI.

## History of the VistA HL7 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA HL7 is an *implementation* of an HL7 interface engine. It is an M-based software product that assists M-based VistA applications by providing a means for those applications to send and receive HL7 messages.

VistA HL7 does not provide tools to map VistA data directly to HL7 messages. It does provide a repository of supported HL7 transactions, connectivity between systems, and guaranteed delivery of messages using supported Lower Layer Protocols (LLPs). It supports point-to-point interfaces, publish and subscribe, and content-based dynamic routing.

M-based VistA applications can use VistA HL7 to interface with any other system that also supports standard HL7 messaging, including many standalone medical devices, non-M-based applications on other systems, and VistA M-based applications running on a different VA facility's systems. As such, VistA HL7 acts as an Enterprise Application Integration (EAI) solution for VistA applications.

### HL7 Standard Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA HL7 supports message transactions for each of the following versions of the HL7 standard:

- 2.1 (HL7 standard publication date: 6/1990)
- 2.2 (HL7 standard publication date: 12/1994)
- 2.3 (HL7 standard publication date: 4/1997)
- 2.3.1 (HL7 standard publication date: 5/1999)
- 2.4 (HL7 standard publication date: 11/2000)

### Evolution of VistA HL7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first released version of VistA HL7 was 1.5, and supported simple point-to-point HL7 transactions between VistA and a local COTS system using Hybrid Lower Layer Protocol (HLLP), and to other VA facilities using VA MailMan. The initial release of version 1.6 added the ability to "broadcast" a message to multiple recipients, and support for the X3.28 LLP. A continuing increase in the demand for additional messaging services has resulted in enhancements to HL 1.6, released through patches, including more complex message routing (dynamic addressing), and messaging using Minimal Lower Layer Protocol (MLLP) over TCP.

The current release of HLO is a substantial redesign of HL 1.6. It is designed to be able to operate alongside HL 1.6, and provides significantly higher operating efficiency and the ability to operate with a substantially decreased system load. In addition, HLO has some enhancements in the way it provides support for building and parsing of HL7 messages.

Since the early 1990’s, the VA has maintained a corporate membership with the Health Level Seven standards organization, and has been an active participant in the evolution of the HL7 standard. Application developers for VistA's Radiology, Pharmacy, Lab, PIMS, and other packages have aggressively enhanced those packages to support HL7-defined event points. Examples include "patient registration," "admit a patient," "lab results available," and "place an order." When one of these event points occurs, the VistA application now generates a corresponding HL7 message, which VistA HL7 distributes to all interested subscribers.

# HL Optimized (HLO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview and Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HLO is an optimized version of HL 1.6.
- All but one file used by HLO is new. The only HL 1.6 file that is used by HLO is the HL LOGICAL LINK File (#870).
- There are more than 30 new routines used by HLO, as opposed to approximately 200 routines in the existing HL 1.6.
- The new namespace is HLO\*.
- HLO engine will co-exist with the existing HL 1.6 engine.
- Existing HL7 applications written for the HL 1.6 engine (HL 1.6 applications) can continue to run without modification.
- The conversion of existing HL 1.6 applications to HLO applications can be fairly straightforward, though testing of the application is essential.
- There is virtually no shared code between the HL 1.6 and HLO engines. Thus, modifications and enhancements of applications written for one HL7 engine can be made without extensive testing of the application being required on the other HL7 engine.
- Goals of HLO:
- Improve the messaging throughput.
- Make it easier for application developers to use.
- Make the software more robust, less susceptible to bugs, and require minimal maintenance overhead.

## Design Highlights

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In HLO, the HLO MESSAGE BODY File (#777) corresponds to the HL7 MESSAGE TEXT File (#772), the HLO MESSAGES File (#778) corresponds to the HL7 MESSAGE ADMINISTRATION File (#773), and the HLO SUBSCRIPTION REGISTRY File (#779.4) corresponds to the HL7 SUBSCRIPTION Control File (#774). There are fewer fields and cross-references in HLO, compared to HL7.
- The PROTOCOL File (#101) is no longer used for HLO. In place of protocols, HLO requires that receiving and sending applications be defined in the new HLO APPLICATION REGISTRY File (#779.2).
- HL Logical Links are still used. HLO requires a different port than the original HL 1.6 implementation (5000 production, 5025 test). Port 5001 will be the standard default port for HLO on production systems and port 5026 for main test systems.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used.

- HLO consists of an assortment of co-operating processes (client links, server links, in-filers, purge processes, etc.). These processes operate under a common framework, the HLO Process Manager, which uses the new HLO PROCESS REGISTRY File (#779.3).
- Processes use a pooling method which allows for a greater number of queues (incoming and outgoing) to run concurrently. This allows fewer processes to service more queues and do more work.
- Processes running under the process manager are dynamic, starting and stopping in response to changing workload.
- Concurrency is maximized by allowing applications to designate private queues for their messages, allowing many more queues to be processed concurrently. This pertains to the outgoing message queues & the incoming applications queues.
- Domain becomes the standard method for identifying sending and receiving facilities.
- There are five new globals in HLO. They are:
- ^HLA - HLO MESSAGE BODY File (#777).
- ^HLB - HLO MESSAGES File (#778).
  - ^HLC - System counters (i.e., for assigning message IENs).
- ^HLD - Static HLO parameter files, including system parameters,

> application registry, process registry, and subscription registry.

- ^HLTMP - System scratch space.
- Commit acknowledgements will not be stored as separate records. Instead, the MSA segment will be stored with the original message. Application acknowledgements will be stored as separate records.
- HLO supports only TCP messaging.
- HLO does not support:
- Synchronous mode (direct connect) or original mode acknowledgements.
- Sequence number protocol.

## HLO Developer Perspective

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The HLO developer APIs are new and include:
- Message parsing.
- Improved support for batch messages.
- Improved support for building messages.
- Automated escape sequence processing.
- Support for acknowledgement messages.
- Internal data structures are encapsulated and accessed via a set of programmer interfaces, protecting them from corruption. The many variables of the HL 1.6 implementation have been replaced in HLO by arrays with more meaningful subscripts, allowing parameters which are applicable to different parts of the HLO system to be grouped together.

## HLO System Manager Perspective

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user interface has been completely re-designed and will have its own menu. Tools include:

- A system monitor for starting and stopping the HLO engine, displaying status information, and viewing message queues and HLO processes.
- A message viewer for viewing messages, displaying errors, and message searching.
- A developer front end for the application registry.

# HLO Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch HL\*1.6\*126 contains all of the components needed to support HLO and was created using the Kernel Installation and Distribution System (KIDS). Please review the KIDS documentation patch description, and familiarize yourself with KIDS prior to installing this package.

> **NOTE:** The following patches are required before installation of HL\*1.6\*126.

- XU\*8\*388
- HL\*1.6\*84
- HL\*1.6\*118

ALWAYS back up your system prior to loading any software.

To correctly install HLO and configure it for proper development and usage:

VistA Steps:

1)  Install the HLO Software Patch.
2)  Define the Server Logical Link.
3)  Update the HLO SYSTEM PARAMETERS File (#779.1).
4)  Update the HLO PROCESS REGISTRY File (#779.3).
5)  Schedule the HLO COUNT RECORDS Option.
6)  Schedule the HLO SYSTEM STARTUP Option.
7)  Start HLO using the HLO System Monitor.

VMS Step:

> Create and activate the TCP/IP Services for OpenVMS.

> **WARNING:** Incoming messages and application acknowledgements depend upon the TCP/IP Services for OpenVMS being defined and active.

## Install the HLO Software Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO package arrives as a standard KIDS Build. It will install the following elements:

1)  New fields in the HL LOGICAL LINK File (#870). TCP/IP PORT (OPTIMIZED) field (#400.08) and DNS DOMAIN field (#.08) are added.
2)  New files, HLO MESSAGE BODY (#777) and HLO MESSAGES (#778), for holding messages.
3)  A new file, HLO SYSTEM PARAMETERS (#779.1), which contains system parameters specific to the installing site. (See section 5.1.1, A *Note About System Parameters* for more information.)
4)  A new file, HLO APPLICATION REGISTRY (#779.2), which contains information for both sending and receiving applications.
5)  A new file, HLO PROCESS REGISTRY (#779.3), which contains information on HLO processes. This file will arrive configured and should not be modified except for adding links and activating listeners.
6)  A new file, HLO SUBSCRIPTION REGISTRY (#779.4). This file is very similar to file HL7 SUBSCRIPTION Control (#774), with the exception that it contains subscriptions in format appropriate to the HLO package.
7)  New entries for the OPTION File (#19) for monitoring and changing the behavior of the HLO system.
8)  A set of routines in the HLO\* namespace.

First, load the KIDS distribution and install the HL\*1.6\*126 package. For more details on the installation of packages, please see the KIDS manual.

Example Install of patch HL\*1.6\*126

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: ?

1 Load a Distribution \[XPD LOAD DISTRIBUTION\]

2 Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\]

3 Print Transport Global \[XPD PRINT INSTALL\]

4 Compare Transport Global to Current System \[XPD COMPARE TO SYSTEM\]

5 Backup a Transport Global \[XPD BACKUP\]

6 Install Package(s) \[XPD INSTALL BUILD\]

Restart Install of Package(s) \[XPD RESTART INSTALL\]

Unload a Distribution \[XPD UNLOAD DISTRIBUTION\]

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: HL\*1.6\*126 Loaded from Distribution 9/15/05@13:34:50

=\> HL\*1.6\*126 (SEP14)

This Distribution was loaded on Sep 15, 2005@13:34:50 with header of

HL\*1.6\*126 (SEP14)

It consisted of the following Install(s):

HL\*1.6\*126

Checking Install for Package HL\*1.6\*126

Install Questions for HL\*1.6\*126

Incoming Files:

777 HLO MESSAGE BODY

778 HLO MESSAGES

779.1 HLO SYSTEM PARAMETERS

779.2 HLO APPLICATION REGISTRY

779.3 HLO PROCESS REGISTRY (including data)

779.4 HLO SUBSCRIPTION REGISTRY

870 HL LOGICAL LINK

> **NOTE:** You already have the 'HL LOGICAL LINK' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

Enter options you wish to mark as 'Out Of Order': HL MAIN MENU HL7 Main Menu

Enter options you wish to mark as 'Out Of Order':\<Enter\>

Enter protocols you wish to mark as 'Out Of Order':\<Enter\>

Delay Install (Minutes): (0-60): 0//:\<Enter\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

--------------------------------------------------------------------------------

Install Started for HL\*1.6\*126 :

Sep 15, 2005@13:35:46

Build Distribution Date: Sep 14, 2005

Installing Routines:

Sep 15, 2005@13:35:47

Installing Data Dictionaries:

Sep 15, 2005@13:35:48

Installing Data:

Sep 15, 2005@13:35:48

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing FORM

Installing PROTOCOL

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Located in the HL (HEALTH LEVEL SEVEN) namespace.

Installing LIST TEMPLATE

Installing OPTION

Sep 15, 2005@13:35:49

Running Post-Install Routine: ^HLOPOST

Updating Routine file...

Updating KIDS files...

HL\*1.6\*126 Installed.

Sep 15, 2005@13:35:49

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

100% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

Install Message sent \# nnnnnnn

Install Completed

### A Note About System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The System Parameters are automatically configured as part of the installation. However, if it becomes necessary to modify them, they can be accessed in the HLO SYSTEM PARAMETERS File (#779.1). The fields are:

- Domain Name – The domain name of your system.
- Station Number – A number which uniquely identifies your site from others.
- PRODUCTION ID - ENTER P if this is a production system, T otherwise.
- MAXIMUM STRING LENGTH – This is the maximum length for strings built by HLO when local applications create new messages to send.
- BUFFER SIZE FOR HL7 (BYTES) - This parameter represents the size of the buffer used by HLO for its background processes. It defaults to 15000 bytes, but may be set from 10,000 bytes to 20,000 bytes.
- BUFFER SIZE FOR USER (BYTES) - This parameter is the size of the buffer used by HLO in the context of an online user. It defaults to 5000, but may be reset to between 512 and 10000 bytes.
- NORMAL MSG RETENTION (HOURS) - How many hours should successfully completed messages remain on your system? (36-96 hours, defaults to 36 hours)
- BAD MESSAGE RETENTION (DAYS) - How many days should message with errors remain on your system? (7-45 days, defaults to 7 days)
- HLO ON/OFF SWITCH - Set to 0 to turn off messaging and all HL7 processes.

> Choose from:

> 0 - OFF

> 1 - ON

- HLO STANDARD LISTENER - Select an entry from the HL Logical Link file that is the listener that remote applications will normally connect to. This screen allows only server entries to be selected.

> Answer with HL LOGICAL LINK NODE, or INSTITUTION, or MAILMAN DOMAIN, or DNS DOMAIN, or TCP/IP ADDRESS, or TCP/IP SERVICE TYPE, or IEN772 OutQ-Non-TCP, or IEN772 InQ-Non-TCP

- HLO RECOUNT ON/OFF FLAG - Set to 1 to disallow update of queues when a recount is being performed.

> Choose from:

> 0 - OFF

> 1 - ON

UNSENT MSG RETENTION (DAYS) - How many days should an unsent message be kept before it is purged? (default value is 45 days)

> **WARNING:** As part of HLO configuration, DSM sites should check the settings of all global max string lengths. They should be set to the maximum of 512. This enables HLO to read and process long HL7 segments correctly.

> **WARNING:** Error trap displays of extremely long variables may be limited to 255 characters and may be truncated under certain versions of M.

## Define the Server Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO requires a Server Logical Link for receiving messages. If HLO (either server or client) is using the same link as HL 1.6, the only requirements are to define the TCP/IP PORT (OPTIMIZED) and the DNS DOMAIN fields, and to verify that all other elements are properly defined for HLO. If this is not possible, a new link must be created.

The default port number for the HLO Server Logical Link (listener) is 5001 on production systems and 5026 on main test systems. If port number 5001 is already in use by another listener, that listener must be re-assigned to a new port number.

The HL 1.6 listener and the HLO listener can use the same HL Logical Link entry, but cannot use the same port number. If using an all-ready existing entry for HLO, don’t delete or modify any of the existing fields, and the “old” listener uses them even if the “new” HLO listener doesn’t.

The preferred listener method for running HLO is the TCP/IP Services for Open VMS. It is unlikely that more than one listener will be needed. However, more than one listener could be configured to run concurrently as long as they have different port assignments.

- <u>Multi-Listener vs. Single Listener</u> – IRM staffs initially installing HLO: If your system is a VMS or Cache system, use a multi-listener! If your system is VMS, the multi-listener should run under VMS TCP. If it is not VMS, but is Cache, you should set up a Taskman multi-listener. Only if your system is neither VMS nor Cache should you set up a single listener.
- <u>Application Developers</u> – Normally, your application should use the site’s standard listener. If you must create your own listener (highly discouraged), if only one connection request will be created at a time and the interfacing application requires its own server, then a single listener would be applicable. Otherwise, if there is a possibility of multiple connection requests, then the multi-listener is appropriate.

For more details on setting up listeners, please refer to Section 6.0, *Listeners*.

> **WARNING:** The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS, use a multi-listener running as a VMS TCP/IP Service instead. For any system required to use the TaskMan Multi-Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first.

To create or edit a server Logical Link definition, use the *Link Edit* option, on the Interface Developer Options menu:

Select Interface Developer Options Option: Link Edit

Select HL LOGICAL LINK NODE: REDACTED

To edit the TCP/IP server level parameters, tab down to the LLP Type field (in the *Link Edit* option) and press \<Enter\> to display a form to edit the fields specific to the LLP type of the selected Link:

HL7 LOGICAL LINK

-------------------------------------------------------

NODE: REDACTED

INSTITUTION: REDACTED

MAILMAN DOMAIN: REDACTED

AUTOSTART: *\*\*see below*

QUEUE SIZE: *\*\*see below*

<span class="mark">LLP TYPE: TCP</span>

<span class="mark">DNS DOMAIN: HL7.</span>REDACTED

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><ul>
<li><blockquote>
<p>The production system’s domain name should be registered on the VHA DNS Domain server. If not currently registered, sites should do this as soon as possible.</p>
</blockquote></li>
<li><blockquote>
<p>If the TCP/IP Address is not entered, or if it changes after being entered, it will be resolved automatically using the system’s registered domain name via the VHA DNS Domain server.</p>
</blockquote></li>
<li><blockquote>
<p>If the domain name is not registered on the VHA DNS Domain server, the TCP/IP Address must be defined.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

For creating a server logical link, key LLP set-up information includes:

|                         |                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| Field               | Description                                                                                                     |
| TCP/IP SERVICE TYPE     | Set to ‘MULTI LISTENER’                                                                                             |
| TCP/IP ADDRESS          | IP Address of the site’s server                                                                                     |
| TCP/IP PORT (OPTIMIZED) | Port to listen on, e.g., 5001 for production systems and 5026 for test systems (make note of the exact port number) |

HL7 LOGICAL LINK

-------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ REDACTED │

│ │

│ TCP/IP SERVICE TYPE: <span class="mark">MULTI LISTENER</span> │

│ TCP/IP ADDRESS: <span class="mark">152.199.199.199</span> │

│ TCP/IP PORT: *\*\* see below* │

│ TCP/IP PORT (OPTIMIZED): <span class="mark">5001</span> │

│ │

│ ACK TIMEOUT: *\*\*see below* RE-TRANSMISION ATTEMPTS: \*\see below* │

│ READ TIMEOUT: *\*\*see below* EXCEED RE-TRANSMIT ACTION: *\*\*see below* │

│ BLOCK SIZE: SAY HELO: │

│ TCP/IP OPENFAIL TIMEOUT: │

│STARTUP NODE: *\*\*see below* PERSISTENT: YES │

<u>│ RETENTION: *\*\*see below*</u> <u>UNI-DIRECTIONAL WAIT: │</u>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

> **WARNING:** Please make sure that the *TCP/IP PORT (OPTIMIZED)* field is used and not the *TCP/IP PORT* field. All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used.

> **WARNING:** If the existing HL Logical Link for the HL7 1.6 listener is reused for HLO, DO NOT modify or delete any of the fields shown in the screen capture above and marked as “\*\*see below”! Even though HLO does not use them, HL7 1.6 does.

Please contact the site IRM to obtain the specific domain name and port number to be used by the client side communicating with VistA. For example, at many sites the HL 1.6 multi-listener uses HL7.SITENAME.MED.VA.GOV with port 5000. Currently, HLO uses the same domain name with port 5001 on production systems and 5026 on test systems. If a site has more than one test system, they may use additional port numbers.

> **NOTE:** Start/Stop Link – For HLO processing the server and client HL Logical Link entries DO NOT need to be started or stopped via the HL 1.6 Start/Stop links option as currently done. The links must be defined with the specific HLO fields (DNS Domain and TCP/IP Port (Optimized)) and HLO System started for the link to be available for receiving or transmitting messages. However, if the link must continue to process applications for the existing HL 1.6 messaging engine then the link still needs to be started as before.

Please obtain the specific domain name and port number to be used by the client side communicating with VistA. For example, at many sites the HL 1.6 multi-listener uses: HL7.SITENAME.MED.VA.GOV with port 5000. Currently, HLO uses the same domain name with port 5001 on production systems and 5026 on test systems. If a site has more than one test system, additional port numbers may be used.

- The port number you select must be an available TCP/IP port number. The port number will also be used in the configuration and naming of the TCP/IP service described in the following sections.
- The port numbers recommended in this chapter, 5001 for production, 5026 for test, have been registered for use by VistA HLO. Everything should be done to free port 5001 for use by HLO.
- If the HLO multi-listener is to be used by an application at the national level and you are not using port number 5001, you must register the port number with the DBIA manager on Forum.

For configuring client logical links, please refer to Section 2.4 of the *VistA Health level Seven (HL7) Site Manager & Developer Manual,* Version 1.6\*56 December, 1999.

.

## Update the HLO SYSTEM PARAMETERS File (#779.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the HLO System Monitor screen, the Standard Listener is used to monitor the primary server link (or “listener”) for HLO. In most instances, this is the only listener that is configured. In order for the Standard Listener status to function properly, the name of the link must be added to the HLO STANDARD LISTENER field in the HLO SYSTEM PARAMETERS File (#779.1). This must be done using FileMan, as shown below.

The System Parameters are automatically configured as part of the installation. However, if it becomes necessary to modify them, they can be accessed in the HLO SYSTEM PARAMETERS File (#779.1). The key fields are:

- Domain Name – the domain name of your system.
- Station Number – a number which uniquely identifies your site from others.

The rest of the system parameters are explained in detail in section 5.1, Install *the HLO Software Patch*.

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: //HLO SYSTEM PARAMETERS

EDIT WHICH FIELD: ALL// HLO STANDARD LISTENER

THEN EDIT FIELD: \<Enter\>

Select HLO SYSTEM PARAMETERS DOMAIN NAME: HL7.VAABC.VA.MED.GOV *<span class="mark">This is the DNS domain name for this system. Also, there will always be only one entry in the HLO System Parameters file and its IEN is 1.</span>*

HLO STANDARD LISTENER: REDACTED *<span class="mark">This is the name of the entry in the HL LOGICAL LINK File (#870) that is the default listener to which most remote applications will send messages, as shown above</span>*

Select HLO SYSTEM PARAMETERS DOMAIN NAME: \<Enter\>

Select OPTION: \<Enter\>

## Schedule the HLO COUNT RECORDS Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO COUNT RECORDS option triggers HLO to count incoming and outgoing messages at a user specified frequency. This option should be scheduled to run at least once a day and can be scheduled to run more frequently, if desired. The “RESCHEDULING FREQUENCY” parameter determines how often this process runs. In the example below, the process is scheduled to run once every six hours. While “H” is used here to denote hours, “M” can be used to denote minutes.

Select OPTION NAME: XUTM MGR Taskman Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queuing

Select Taskman Management Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: HLO COUNT RECORDS COUNT HL7 MESSAGE RECORDS

Are you adding 'HLO COUNT RECORDS' as

a new OPTION SCHEDULING (the 201ST)? No// Y (Yes)

-----------------------------------------------------------------------

Edit Option Schedule

Option Name: HLO COUNT RECORDS

Menu Text: COUNT HL7 MESSAGE RECORDS TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: T+1@1AM (AUG 25, 2005@01:00)

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 6H

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

-------------------------------------------------------------------------

(Save and Exit from the Edit Option Schedule screen)

## Schedule the HLO SYSTEM STARTUP and the HLO DAILY STARTUP Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO SYSTEM STARTUP option should be scheduled after installing and configuring HLO. Once this option is scheduled, HLO starts automatically at system startup. This option can be scheduled from the Taskman Management Menu.

> **WARNING:** Not scheduling this option requires the IRM to start HLO manually from the HLO System Monitor.

Select OPTION NAME: XUTM MGR Taskman Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queuing

Select Taskman Management Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: HLO SYSTEM STARTUP

Are you adding 'HLO SYSTEM STARTUP' as

a new OPTION SCHEDULING (the 202ND)? No// Y (Yes)

-----------------------------------------------------------------

Edit Option Schedule

Option Name: <span class="mark">HLO SYSTEM STARTUP</span> or <span class="mark">HLO DAILY STARTUP</span>

Menu Text: HL7 (Optimized) SYSTEM STARTUP TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING: STARTUP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

------------------------------------------------------------------

(Save and Exit from the Edit Option Schedule screen)

## Start HLO using the HLO System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start HLO, select the START HLO action protocol from the HLO System Monitor. Please refer to Section 7.2 of this document for more detailed instructions.

HLO SYSTEM MONITOR Aug 26, 2005@09:40:25 Page: 1 of 1

<span class="mark">Brief Operational Overview</span>

SYSTEM STATUS: STOPPED

PROCESS MANAGER: STOPPED

STANDARD LISTENER: NOT OPERATIONAL

TASKMAN: RUNNING

DOWN LINKS: 0

CLIENT LINK PROCESSES: 0

IN-FILER PROCESSES: 0

MESSAGES PENDING ON OUT QUEUES: 0 ON SEQUENCE QUEUES: 0

STOPPED OUTGOING QUEUES:

MESSAGES PENDING ON APPLICATIONS: 0

STOPPED INCOMING QUEUES:

FILE 777 RECORD COUNT: 7 --\> as of Aug 14, 2005@07:53:01

FILE 778 RECORD COUNT: 7 --\> as of Aug 14, 2005@07:53:01

MESSAGES SENT TODAY: 0

MESSAGES RECEIVED TODAY: 0

MESSAGE ERRORS TODAY: 0

<span class="mark">Brief System Status</span>

LP LIST PROCESSES BS BRIEF STATUS TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK RT RealTime MODE

OQ OUTGOING QUEUES STOP HLO SEQ SEQUENCE QUEUES

IQ INCOMING QUEUES START HLO SQ START/STOP QUEUE

Select Action:Quit// START START HLO

After start up of HLO, the following should be verified:

- SYSTEM STATUS is RUNNING
- PROCESS MANAGER is RUNNING
- STANDARD LISTENER will still be NOT OPERATIONAL until TCP Service is created and enabled, see 3.8 below
- TASKMAN is RUNNING

## Create and Activate the TCP/IP Services for Open VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the next chapter ‘Listeners’ for information on configuring the TCP/IP Services for Open VMS.

> **WARNING:** The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS. For any system required to use the TaskMan Multi-Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first.

# Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO uses TCP/IP listeners to "listen" on a particular port for incoming TCP/IP connections from other systems. Listeners are necessary so that other systems may initiate a connection to this VistA system over TCP/IP.

### Client and Server Roles in HLO over TCP/IP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two separate sets of M code define the roles of client and server over TCP/IP channels:

- Sending System = TCP Client (initiates connection to the Receiving System)
- Receiving System = TCP Server (listens for connections)

### TCP/IP Connection Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the system connecting to VistA is a non-VistA system, it must support synchronous bi-directional TCP/IP transmission. This means that when a message is sent over a TCP/IP connection, the expected response to that message is returned immediately over the same open connection. The sending system must not initiate a new transmission until the current transmission is complete. The receiving system must respond to the original message without attempting to initiate a new connection.

The sending and receiving system cannot change roles over the same connection. If the receiver needs to send transmissions (other than commit acknowledgements), then it must open a new connection.

If VistA is to connect to a target system, the target system must have its own TCP/IP listener process that responds to connection requests.

The TCP/IP connection can be *persistent* or *non-persistent*. This is determined by the connecting system. If the connecting system drops the connection after a transmission completes, the connection is non-persistent. If it is left open, the connection is persistent.

Three types of listeners or server processes are provided in the current HLO software distribution. The three listeners included are:

1.  TCP/IP Services for Open VMS
2.  TaskMan Multi-Threaded Listener
3.  Single Listener

> **WARNING:** One Single Listener server process is currently provided in the HLO software. However, configuration of multiple Single Listeners is NOT supported by HLO at this time.

Applications that require a dedicated Single Listener should continue to use the original HL 1.6 implementation. A subsequent HLO patch is being developed for a future release that provides full support of multiple Single Listeners and additional Multi-Threaded Listeners.

When trying to decide between a single listener and a multi-listener, if only one connection request will be created at a time and the interfacing application requires its own server, then a single listener would be applicable. Otherwise, if there is a possibility of multiple connection requests then the multi-listener is appropriate.

The remainder of this chapter will focus on the two types of Multi-Threaded Listener.

> **WARNING:** HLO highly recommends use of the TCP/IP Services for Open VMS. However, sites NOT on the OpenVMS platform will be required to use the TaskMan Multi-Threaded Listener.

To reference additional information on listener configuration, please refer to the following documents in the VistA Documentation Library:

- User Manual: TCP/IP Supplement – HL\*1.6\*19 (January 1999)
- Site Manager & Developer Manual – HL\*1.6\*56 (December 1999)

## Multi-Threaded Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-threaded listeners are useful when multiple connection requests come to a single port from many devices or systems. Because multi-threaded listeners spawn separate handlers for each client connection request, they enable multiple concurrent connections.

VistA HL7 supports two types of multi-threaded listeners:

- TCP/IP Services for Open VMS (for DSM or Cache)
- TaskMan Multi-Threaded Listener

## TCP/IP Services for Open VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sections 6.3.1 through 6.3.5 are for both Cache on OpenVMS and DSM on Open VMS. Section 6.3.6 is for Cache users only and section 6.3 7 is for DSM users only

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-Listeners using TCP/IP Services for Open VMS for Cache/DSM sites were introduced in patch HL\*1.6\*84. This chapter documents the set up for creating multi-listeners for HLO using TCP/IP Services for OpenVMS. It assumes that a DCL command file for HL7 1.6 already exists and can be copied as the starting basis for the new HLO service.

### TCP/IP Services for OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCP/IP is an open communications standard that enables any connected host to communicate with any other connected host. TCP/IP Services for OpenVMS is a product that implements several of the protocols in the TCP/IP standard for the OpenVMS operating system. This section focuses only on those TCP/IP services configured to run as a TCP/IP server (listener) process.

### TCP/IP Services and VistA HLO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A TCP/IP service configured to run as a server permits multiple remote TCP/IP clients to connect and run concurrently up to the limits established by the service. A server listens on a particular TCP/IP communication port and launches a specified DCL (Digital Command Language) Command file that serves as a startup process for each client connection process. This startup file contains the necessary commands to execute the entry point into VistA HLO.

### Requirements for Setting up a TCP/IP Service on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure a TCP/IP service, the following components within VistA HLO and OpenVMS will need to be configured:

- VistA HLO logical link for the Multi-Threaded Listener.
- An OpenVMS account. (If an account already exists for HL7 1.6, use the same user and home directory.)
- An OpenVMS home directory. (If an account already exists for HL7 1.6, use the same user and home directory.)
- An OpenVMS DCL command procedure. This is the startup command file that executes on every concurrent process. Default DCL command files are provided in this document.
- An OpenVMS TCP/IP service.

The person implementing the instructions in this document must have OpenVMS system administrator privileges to create the above components and be familiar with the OpenVMS TCP/IP Services Management Control Program.

### Recommended Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following names are used in the description for creating a TCP/IP service and are referenced throughout this chapter. All these names are suggestions. Your site might already have its own naming convention.

- HLSEVEN ― OpenVMS user account name for an HLO TCP/IP service.
- \[HLSEVEN\] ― Name of home directory for the above HLSEVEN user.
- HLSEVEN ― Name of the owner.
- Sites that have previously established a VMS user account for HL7 1.6 may reuse the same account for HLO, i.e., another VMS account need not be created.
- The same user name, HLSEVEN, is recommended for HL7 prior to the release of HLO.
- However, a new TCP/IP service command procedure specific for HLO must be created and placed in the same home directory as the old HL7 1.6 TCP/IP service.
- HLS\<port\>\<M environment\>.COM― Name of DCL command procedure, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual VistA M environment. For example:
- HLS5001DSM.COM― represents the command procedure for a TCP/IP service listening on port 5001 (production systems) that starts a DSM HLO listener process.
- HLS5001CACHE.COM― represents the command procedure for a TCP/IP service listening on port 5001 (production systems) that starts a CACHE HLO listener process.
- HLS5026DSM.COM― represents the command procedure for a TCP/IP service listening on port 5026 (test systems) that starts a DSM HLO listener process.
- HLS5026CACHE.COM― represents the command procedure for a TCP/IP service listening on port 5026 (test systems) that starts a CACHE HLO listener process.
- HLS\<port\>\<M environment\>― Name of a TCP/IP service, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual VistA M environment. For example:
- HLS5001DSM― represents the TCP/IP service listening on port 5001 that starts a DSM HLO listener process.
- HLS5001CACHE― represents the TCP/IP service listening on port 5001 that starts a CACHE HLO listener process.
- HLS5026DSM― represents the TCP/IP service listening on port 5026 (test systems) that starts a DSM HLO listener process.
- HLS5261CACHE― represents the TCP/IP service listening on port 5026 (test systems) that starts a CACHE HLO listener process.

  To set up a TCP listener: type TCP in the LLP type field and press \<ENTER\>. The screens below show the results. We have entered Multi Listener, since we are hosted on a VMS site.

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

<u>NODE</u>: NXT5011 DESCRIPTION:

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Disabled

QUEUE SIZE: 10

<u>LLP TYPE</u>: <span class="mark">TCP</span>

DNS DOMAIN:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ NXT5011 │

│ │

│ TCP/IP SERVICE TYPE: MULTI LISTENER │

│ TCP/IP ADDRESS: 10.237.198.230 │

│ TCP/IP PORT: 5001 │

│ TCP/IP PORT (OPTIMIZED): 5011 │

│ │

│ ACK TIMEOUT: RE-TRANSMISION ATTEMPTS: │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: │

│ BLOCK SIZE: SAY HELO: │

│ TCP/IP OPENFAIL TIMEOUT: │

│STARTUP NODE: PERSISTENT: NO │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

- More than one TCP/IP service for HLO may be set up, although it is not necessary to do this. To set up more than one TCP/IP service for HLO, follow the steps in this document for each listener. However, a different command file name, TCP/IP service name, and port number must be defined for each listener.
- Optionally, different user accounts and directories may be specified for each listener.

### Creating TCP/IP Services for Open VMS with Cache

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General steps for creating TCP/IP Services for Open VMS with Cache are as follows:

1.  Create OpenVMS User Account. (If a user account already exists for HL7 1.6, use the same user account and home directory.)
2.  Create OpenVMS Home Directory. (If a user account already exists for HL7 1.6, use the same user account and home directory.)
3.  Create a DCL Command Procedure.
4.  Set up the TCP/IP Service.
5.  Enable and Save the TCP/IP Service.
6.  Control the Number of Log Files Created by TCP/IP Services.
7.  Start and Stop the TCP/IP Service.

#### Note for Multi-Node Cluster Sites:

For sites configured with a multi-node cluster, more than one node may be advertised under the domain name HL7.SITENAME.MED.VA.GOV and the TCP/IP service may be running on multiple nodes.

In addition, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process to remain uninterrupted if the TCP/IP service is enabled on all nodes in the cluster.

If this is the case for your site, be sure to enable the service on all these nodes, after setting up the TCP/IP service and COM file on one of these nodes.

#### Create OpenVMS User Account

To Create an OpenVMS User Account:

- If an account already exists for HL7 1.6, use the same user account. Review the settings for that user account to insure conformance to the screen below, then skip to section 6.3.6.4 *Create a DCL Command Procedure*.
- Determine an unused User Identification Code (UIC), typically in the same group, as the other Cache for OpenVMS accounts.
- Using the OpenVMS Authorize utility, add the new HLSEVEN account with the unused UIC. You must have SYSPRV to do this.
- Verify that the account settings for the new HLSEVEN account are the same as they appear in the example that follows; or, if they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY, Restricted, and Captive flags are set.

There are two different ways to set up a new user account, and you are free to choose the one you prefer. The following two examples illustrate two different ways to set up an OpenVMS User account:

One way to set up an OpenVMS User account is to copy your existing XMINET (TCP/IP MailMan) account to a new account with an unused UIC. For example:

> \$ MC AUTHORIZE

> UAF\> COPY /ADD XMINET HLSEVEN/UIC=\[51,45\]/DIR=\[HLSEVEN\]

> %UAF-I-COPMSG, user record copied

> %UAF-W-DEFPWD, copied or renamed records must receive new password

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000051,000045\] added to rights database

> UAF\>

The other way to set up an Open VMS User account is to add the new HLSEVEN OpenVMS account directly. For example:

> \$ MC AUTHORIZE

> UAF\> ADD HLSEVEN /UIC=\[100,45\]/OWNER="HLSEVEN" - (must use continuation character "-")

> \_UAF\> /DEVICE=USER\$/DIRECTORY=\[HLSEVEN\] -

> \_UAF\> /NOACCESS/NETWORK/FLAGS=(DISCTLY,RESTRICTED,NODISUSER) -

> \_UAF\> /PRIV=(NETMBX,TMPMBX) -

> \_UAF\> /DEF=(NETMBX,TMPMBX)/LGICMD=NL:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000100,000045\] added to rights data

> base

> UAF\>

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: HLSEVEN

> Account: UIC: \[100,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[HLSEVEN\]

> LGICMD: NL:

> Flags: DisCtlY Restricted

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 100 Bytlm: 64000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 150 WSdef: 2000

> Prio: 4 ASTlm: 250 WSquo: 4000

> Queprio: 4 TQElm: 10 WSextent: 16384

> CPU: (none) Enqlm: 2000 Pgflquo: 50000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

> UAF\> Exit

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> \$

#### Create OpenVMS Home Directory

If a home directory already exists for HL7 1.6, then use the same home directory. Skip to section 6.3.6.4 *Create a DCL Command Procedure*.

This directory will house the DCL command procedure, which is executed whenever a client connects. A log file is created for every instance of a connection for that listener. Make sure that the owner of the directory is the HLSEVEN account.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

\$ CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

#### Create a DCL Command Procedure

Create a DCL command procedure (shown below) in the home directory for the HLSEVEN account and name it according to the recommended convention. Make sure the command procedure file is owned by the HLSEVEN account.

1.  To create a DCL command procedure that will use a given port (for example, port 5001), name your command procedure file as HLS5001CACHE.COM.
2.  Adjust the Cache command line (Cache configuration, UCI, and volume set) for your system.
3.  Ensure that the name of the DCL command file, as described in step 1, matches the port assignment. For example, if you changed the port number from 5001 to 6788, rename your HLS5001CACHE.COM file to HLS6788CACHE.COM.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used.

Before creating the Command Procedure file, determine the proper Cache configuration to use for the environment where you want to start your listener. To do that, use command “CCONTROL LIST” and it will list all Cache configurations that are defined. The Cache configuration you will most likely need is the one marked as (default).

If you are not running a cluster or if the listener is to run on only a single node of the cluster, you can use the name of that default Cache configuration as the first parameter to the ‘CSESSION’ command.

If you are running a cluster and the listener is to run on multiple nodes of that cluster, then you need to make sure that the DCL Command Procedure file can resolve the proper name of the default Cache configuration on each node of the cluster where it is to run. Keep in mind that same DCL command file has to work on each participating node.

On most VistA systems, the name of Cache configuration will be the same as name of the node or perhaps a derivative of the name of the node. So, if the node is 74A01, the configuration will be 74A01 or maybe BRX74A01. In those cases, the DCL Command Procedure file will need to use ‘F\$GETSYS(“NODENAME”)’ to obtain node name or BRX’F\$GETSYS(“NODENAME”) to obtain the node name and put “BRX” in front of it.

For your convenience, you can cut and paste the following DCL command procedure file into your OpenVMS HLSEVEN device and directory.

Sample DCL Command Procedure file:

\$! HLS5001CACHE.COM - for incoming tcp connect requests with port=5001 and

\$! using "Cache" command line to enter the M environment

\$! File name HLS5001CACHE.COM is recommended to be changed to reflect the

\$! change of the TCP/IP port number. For example, file name could be

\$! changed to HLS6788CACHE.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5001CACHE.COM and HLS5001DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is

\$! \*\*enabled, that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$! \*\*Also, comment or uncomment the appropriate lines for your system.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM

\$!dsm/env=dsmmgr/uci=vah/vol=tou VMS^HLOSRVR

<span class="mark">\$!-------------------------------------------------------------</span><span class="mark">\$! for Cache</span><span class="mark">\$! The first parameter after csession is the name of Cache configuration that</span><span class="mark">\$! corresponds to the environment where listener should be run</span><span class="mark">\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET</span><span class="mark">\$!</span><span class="mark">\$! The following line is an example for single or integrated sites</span><span class="mark">\$ csession ‘F\$GETSYI("NODENAME") "-U" "VAH" "VMS^HLOSRVR"</span><span class="mark">\$!</span><span class="mark">\$! The following line is an example for consolidated sites</span><span class="mark">\$! csession BRX’F\$GETSYI("NODENAME") "-U" "VAH" "VMS^HLOSRVR"</span><span class="mark">\$!</span><span class="mark">\$! The following line is an example for non-cluster sites</span><span class="mark">\$! csession MYSITE "-U" "VAH" "VMS^HLOSRVR"</span><span class="mark">\$!</span><span class="mark">\$! The following live is an example for a single test account</span><span class="mark">\$! csession MYSITE "-U" "TST" "VMS^HLOSRVR"</span><span class="mark">\$!-------------------------------------------------------------</span>\$ endif\$ exit:\$ logout/briefDouble Checking the Setup:

After creating/editing the command file, run the following command and make sure that the “Owner:” field matches the user account which will be running the command file. (In our examples that is “HLSEVEN” as shown.)

\$ dir/full hls5001cache.com

Directory DKC0:\[USER.HLSEVEN\]

HLS5001CACHE.COM;1 File ID: (13869,1,0)

Size: 6/6 Owner: \[USERS,HLSEVEN\]

Created: 23-FEB-2005 16:59:14.91

Revised: 23-FEB-2005 17:01:16.70 (3)

Expires: \<None specified\>

Backup: \<No backup recorded\>

Effective: \<None specified\>

Recording: \<None specified\>

Accessed: \<None specified\>

Attributes: \<None specified\>

Modified: \<None specified\>

Linkcount: 1

File organization: Sequential

Shelved state: Online

Caching attribute: Writethrough

File attributes: Allocation: 6, Extend: 0, Global buffer count: 0

No version limit

Record format: Variable length, maximum 255 bytes, longest 77 bytes

Record attributes: Carriage return carriage control

RMS attributes: None

Journaling enabled: None

File protection: System:RWED, Owner:RWED, Group:RE, World:

Access Cntrl List: None

Client attributes: None

HLS5001CACHE.COM;1 File ID: (13868,1,0)

Size: 6/6 Owner: \[USERS,HLSEVEN\]

Created: 23-FEB-2005 16:54:25.63

Revised: 23-FEB-2005 17:01:16.72 (3)

Expires: \<None specified\>

Backup: \<No backup recorded\>

Effective: \<None specified\>

Recording: \<None specified\>

Accessed: \<None specified\>

Attributes: \<None specified\>

Modified: \<None specified\>

Linkcount: 1

File organization: Sequential

Shelved state: Online

Caching attribute: Writethrough

File attributes: Allocation: 6, Extend: 0, Global buffer count: 0

No version limit

Record format: Variable length, maximum 255 bytes, longest 77 bytes

Record attributes: Carriage return carriage control

RMS attributes: None

Journaling enabled: None

File protection: System:RWED, Owner:RWED, Group:RE, World:

Access Cntrl List: None

Client attributes: None

Total of 2 files, 12/12 blocks.

> **NOTE:** Could also use the following command if you think this is more clear.

\$ dir/owner HLS5001CACHE.COM

Directory DKC0:\[USER.HLSEVEN\]

HLS5001CACHE.COM;1 \[USERS,HLSEVEN\]

Total of 1 files.

#### Set up the TCP/IP Service

To Create the TCP/IP Service to Listen for Connections:

1.  Choose the OpenVMS node where you want to run the TCP/IP service listener. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener.
2.  Use TCP/IP port number 5001 for production systems and 5026 for the main test system.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used.

3.  Use user account HLSEVEN.
4.  Use DCL command file name HLS5001CACHE.COM.
5.  Since TCP/IP Services are node specific, make sure to set up the listener on the same node on which it will be running.
6.  Ensure that your new TCP/IP service uses the recommended naming convention. For example, to set up a service that will be listening on port 5001 and use a corresponding DCL command file HLS5001CACHE.COM.
7.  Set the service name as HLS5001CACHE as follows:

\$ TCP/IP (must use continuation character "-" at end of long lines)

TCP/IP \> SET SERVICE HLS5001CACHE/USER=HLSEVEN/PROC=HLS5001CACHE/PORT=-

\_TCP/IP \> 5001/PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCP/IP \> <span class="mark">/LIMIT=50/</span>FILE=USER\$:\[HLSEVEN\]HLS5001CACHE.COM/INACTIVITY=1

In this command, <span class="mark">/LIMIT=50</span> specifies the maximum number of TCP/IP connections that can be made at any time. The limit of 50 is appropriate for most local sites, but for systems that serve as national databases the limit should be set initially to 500. The system manager is responsible for monitoring the peak number of connections made, and if the peak approaches the limit, the limit should be increased.

If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you use the following commands to remove the corrupted service and repeat the above commands.

> TCP/IP \> SET CONFIG ENABLE NOSERVICE HLS5001CACHE

> TCP/IP \> SET NOSERVICE HLS5001CACHE

TCP/IP \> SHO SERVICE HLS5001CACHE/FULL

Service: HLS5001CACHE

State: Disabled

Port: 5001 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5001CACHE

#### Enable and Save the TCP/IP Service

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCP/IP \> ENABLE SERVICE HLS5001CACHE *(<span class="mark">enable service immediately)</span>*

TCP/IP \> SET CONFIG ENABLE SERVICE HLS5001CACHE *<span class="mark">(save service for reboot)</span>*

TCP/IP \> SHO SERVICE/FULL HLS5001CACHE

Service: HLS5001CACHE

State: <u>Enabled</u>

Port: 5001 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5001CACHE

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\] HLS5001CACHE.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCP/IP \> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, <span class="mark">HLS5001CACHE</span>, MPI, TELNET, XMINETMM

TCP/IP \> EXIT

#### Note for Multi-Node Cluster Sites

For sites configured with a multi-node cluster, more than one node may be advertised under the domain name HL7.SITENAME.MED.VA.GOV and the TCP/IP service may be running on multiple nodes.

In addition, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process to remain uninterrupted if the TCP/IP service is enabled on all nodes in the cluster.

If this is the case for your site, be sure to enable the service on all these nodes, after setting up the TCP/IP service and COM file on one of these nodes.

#### Control the Number of Log Files Created by TCP/IP Services

The HLS5001CACHE TCP/IP service automatically creates log files (TCP/IP services does this and it cannot be prevented) in the HLSEVEN directory named HLS5001CACHE.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME USER\$:\[HLSEVEN\]HLS5001CACHE.LOG; USER\$:\[HLSEVEN\]HLS5001CACHE.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 USER\$:\[HLSEVEN\]HLS5001CACHE.LOG;

> **NOTE:** This cannot be done until the first log file has actually been created.

You probably should not limit the number of versions of the log file until you know that your HLS5001CACHE service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

#### Other TCP/IP Service Commands

> **WARNING:** If HLO is stopped or disabled for two hours or more, the VMS Multi-Listener service should be disabled and then re-enabled before restarting HLO.

The definition of a link is required for the multi-threaded listener for Open VMS systems. This link never needs to be started or stopped through the VistA HL 1.6 or HLO options. Instead, it is normally started and stopped via TCP/IP services. For example:

TCP/IP \> DISABLE SERVICE HLS5001CACHE *(Stop* TCP/IP *service)*

TCP/IP \> ENABLE SERVICE HLS5001CACHE *(Start* TCP/IP *service)*

Any questions about configuring TCP/IP Service for OpenVMS should be directed to EVS for assistance.

### Creating a TCP/IP Services for Open VMS with DSM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General steps for creating a TCP/IP Services for Open VMS with DSM are as follows:

(For more detailed information on creating TCP/IP Services for Open VMS with DSM, please refer to Appendix F.)

1.  Create OpenVMS User Account (If an account already exists for HL7 1.6, use the same user and home directory.)
2.  Create OpenVMS Home Directory (If an account already exists for HL7 1.6, use the same user and home directory.)
3.  Create a DCL Command Procedure.
4.  Set up the TCP/IP Service.
5.  Enable and Save the TCP/IP Service.
6.  Resolve Access Control List (ACL) Issues.
7.  Control the Number of Log Files Created by TCP/IP Services.
8.  Start and stop the TCP/IP Service.

## TaskMan Multi-Threaded Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration of the TaskMan Multi-Threaded listener involves the following steps:

1.  Set up the server logical link in the HL LOGICAL LINK File (#870). This step may have been done already. If that is the case, proceed to the next step. Otherwise refer to Section 5.2 of this document for set up details.
2.  Configure the TASKMAN MULTI-LISTENER record in the HLO PROCESS REGISTRY File (#779.3): Please refer to Section 5.4 of this document for setup details.
    1.  Assign the server logical link name (defined in step \#1) to the DEDICATED LINK field.
    2.  Set the ACTIVE field to ‘YES’.

> **WARNING:** The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS. For any system required to use the TaskMan Multi-Threaded Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first.

Please contact the site IRM to obtain the specific domain name and port number to be used by the client side communicating with VistA. For example, at many sites the HL 1.6 multi-listener uses HL7.SITENAME.MED.VA.GOV with port 5000. Currently, HLO uses the same domain name with port 5001on production systems and 5026 on test systems.

> **REMINDER:** TaskMan must be running for the TaskMan Multi-Threaded Listener to function.

### Set up the Server Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistA HL LOGICAL LINK File (#870), create an entry for the Multi-Threaded Listener with the fields populated as follows. If more assistance is required for defining the HL Logical Link, please refer to Section 5.2 in the chapter *HLO Installation and Configuration* for more specific instructions.

#### Link Settings for the TaskMan Multi-Threaded Listener in the Logical Link File (#870)

|                         |                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| Field               | Description                                                                                                     |
| LLP TYPE                | Set to ‘TCP’                                                                                                        |
| TCP/IP SERVICE TYPE     | Set to ‘MULTI LISTENER’                                                                                             |
| TCP/IP ADDRESS          | IP Address for your server                                                                                          |
| TCP/IP PORT (OPTIMIZED) | Port to listen on, e.g., 5001 for production systems and 5026 for test systems (make note of the exact port number) |

- The port number you select must be an available TCP/IP port number. The port number will also be used in the configuration and naming of the TCP/IP service described in the following sections.
- The port number recommended in this chapter, 5001 for production and 5026 for test, has been registered for use by VistA HLO. Everything should be done to free port 5001 for use by HLO.
- If the HLO multi-listener is to be used by an application at the national level and you are not using port number 5001 for production, you must register the port number with the DBIA manager on Forum.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used.

If the TCP/IP Address is not defined, it is resolved automatically by the VHA DNS Domain server. If the system’s domain is NOT registered in the VHA DNS server, the IP address should be defined.

For configuring client logical links please refer to Section 6.2 of this document.

### Configure the HLO Standard Listener Record in the HLO System Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Logical Link name defined in section 6.4.1 must be added to the HLO Standard Listener field (#.1) in the HLO SYSTEM PARAMETER File (#779.1). This field is a pointer to field \#.01 in file \#870.

Once this field is entered, the HLO System Monitor knows what port the listener is using.

Select HLO SYSTEM PARAMETERS DOMAIN NAME: REDACTED

DOMAIN NAME: REDACTED Replace

STATION NUMBER: 998//

PRODUCTION ID: training//

MAXIMUM STRING LENGTH: 512//

BUFFER SIZE FOR HL7 (BYTES): 10000//

BUFFER SIZE FOR USER (BYTES): 5000//

NORMAL MSG RETENTION (HOURS): 36//

BAD MESSAGE RETENTION (DAYS): 7//

HLO ON/OFF SWITCH: ON//

HLO STANDARD LISTENER: <span class="mark">ZZJGTCPS</span>//

HLO RECOUNT ON/OFF FLAG: OFF//

UNSENT MSG RETENTION (DAYS): 30//

# HLO Management System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO Main Menu is the primary entry point for managing and monitoring the HLO system. Two primary types of users will find the Main Menu useful. IRMs will find it useful for managing the various HLO processes, as well as monitoring the status of the system. Developers will find it useful for defining and modifying system parameters, as well as locating, tracking, and analyzing messages.

The following is a sample view of the options from the HLO Main Menu:

SM HLO SYSTEM MONITOR

MV HLO MESSAGE VIEWER

STAT HLO MESSAGE STATISTICS

ES HLO ERROR STATISTICS

SP EDIT HLO SYSTEM PARAMETERS

Select HL7 (Optimized) MAIN MENU Option:

> **NOTE:** Some of these options are protected by security keys and may or may not be displayed for certain users who have not been assigned those keys.

## System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The System Monitor, a ListMan utility, is the primary utility for managing HLO. Within it, one can start and stop all processes and queues associated with HLO, as well as monitor all queues, links and processes. The System Monitor displays information appropriate to the selected option as well as a list of different actions that can be taken within the monitor. When the System Monitor is opened, the “Brief Status” screen is displayed. This is the same display shown when selecting action “BS” from within the System Monitor.

The following screen is the HLO System Monitor. Please reference letters A-C (below) for the explanations of the line items (A and B) and the action items (C).

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:27:23 Page: 1 of 1</u>

<u>Brief Operational Overview \></u>

SYSTEM STATUS: RUNNING <span class="mark">A.1</span>

PROCESS MANAGER: RUNNING <span class="mark">A.2</span>

STANDARD LISTENER: OPERATIONAL <span class="mark">A.3</span>

TASKMAN: RUNNING <span class="mark">A.4</span>

DOWN LINKS: 0 <span class="mark">B.1</span>

CLIENT LINK PROCESSES: 0 <span class="mark">B.2</span>

IN-FILER PROCESSES: 0 <span class="mark">B.3</span>

MESSAGES PENDING ON OUT QUEUES: <span class="mark">B.4</span> 0 ON SEQUENCE QUEUES: 0 <span class="mark">B.5</span>

STOPPED OUTGOING QUEUES: <span class="mark">B.6</span>

MESSAGES PENDING ON APPLICATIONS: 0 <span class="mark">B.7</span>

STOPPED INCOMING QUEUES: <span class="mark">B.8</span>

FILE 777 RECORD COUNT: <span class="mark">B.1</span> 28 --\> as of Feb 14, 2005@14:27

FILE 778 RECORD COUNT: <span class="mark">B.2</span> 28 --\> as of Feb 14, 2005@14:27

MESSAGES SENT TODAY: <span class="mark">B.3</span> 0

MESSAGES RECEIVED TODAY: <span class="mark">B.4</span> 0

MESSAGE ERRORS TODAY: <span class="mark">B.5</span> 0

<span class="mark"><u>\_ Brief System Status \_</u></span>

LP LIST PROCESSES <span class="mark">C.1</span> BS BRIEF STATUS <span class="mark">C.5</span> TL TEST TCP LINK <span class="mark">C.9</span>

DL DOWN LINKS <span class="mark">C.2</span> ML MONITOR LINK <span class="mark">C.6</span> RT RealTime MODE <span class="mark">C.10</span>

OQ OUTGOING QUEUES <span class="mark">C.3</span> STOP HLO <span class="mark">C.7</span> SEQ SEQUENCE QUEUES <span class="mark">C.11</span>

IQ INCOMING QUEUES <span class="mark">C.4</span> START HLO <span class="mark">C.8</span> SQ START/STOP QUEUE <span class="mark">C.12</span>

Select Action: Quit//

<u>A.</u> - The system monitor is used for starting and stopping the HLO engine, displaying status information, and viewing message queues and HLO processes.

To start HLO, select the START HLO action protocol from the HLO System Monitor. The result of starting HLO will automatically shut down then start up the HLO System Monitor.

After start up of HLO, the following should be verified:

1.  SYSTEM STATUS is RUNNING (or STOPPED). This indicates whether or not the HLO system is running. Note that when starting the system, it will show the status of “RUNNING” even if not all processes have started. Similarly, when stopping, it will display a status of “STOPPED,” even if some processes have not yet responded to the STOP signal. When in doubt, it is always a good idea to select “LP” to make sure that all processes are running or stopped, depending on what you are trying to do.
1.  PROCESS MANAGER is RUNNING (or STOPPED). This indicates whether or not the HLO process manager is running. The process manager is required to be running to maintain and monitor the HLO processes.
2.  STANDARD LISTENER is OPERATIONAL (or NOT OPERATIONAL). If not operational, you must start the VMS TCP/IP Service (read warning below). This indicates whether or not the Standard Listener is running. The name of the Standard Listener must be added to the HLO SYSTEM PARAMETERS File (#779.1) in order for it to function properly. Please refer to Chapter 3 for more detailed instructions.

> **WARNING:** If HLO is stopped or disabled for two hours or more and the TCP/IP Services for Open VMS is being used, it should be disabled at the VMS level and then re-enabled before restarting HLO. Please refer to Section 6.3.6.9 for further instructions on enabling and disabling the TCP/IP Services for Open VMS service.

3.  TASKMAN is RUNNING (or STOPPED). This indicates whether TaskMan is operational. TaskMan is required for the operation of HLO. If TaskMan is not operational, it must be started before HLO can be started properly.

<u>B.</u> - The following are definitions of each line of the HLO System Monitor screen.

1.  <u>Down Links</u>: Will show the names of links if they are down. Messages will not be able to be transmitted on links listed. This number should usually be zero.
2.  <u>Client Link Processes</u>: Represents a count of the number of outgoing client link processes that are currently running. A system should have at least two outgoing links running at one time.
3.  <u>In-Filer Processes</u>: Represents a count of the number of incoming link processes that are currently running. A system should have at least two incoming links running at one time.
4.  <u>Messages Pending on Out Queues</u>: This is a counter for the total number of messages on the out queue waiting to be transmitted.
5.  <u>Messages Pending on Sequence Queues</u>: This is a counter for the total number of messages waiting on the sequence queue to be processed.
6.  <u>Stopped Outgoing Queues</u>: These are the names of the outgoing queues that are currently down. Messages will not be able to be transmitted over these queues. Only the first three queues are shown. If there are more than three, the line will end in “…”.
7.  <u>Messages Pending on Applications</u>: This is a count for the total number of messages on the inbound queue waiting to be processed.
8.  <u>Stopped Incoming Queues</u>: These are the names of the incoming queues that are currently down. Messages will not be received over these queues. It displays a list of currently stopped incoming queues. Only the first three queues are shown. If there are more than three, the line ends in “…”.
9.  <u>File 777 Record Count</u>: Displays the number of records in the HLO MESSAGE BODY File (#777) as of the date and time the HLO RECORD COUNT process was run.
10. <u>File 778 Record Count</u>: Displays the number of records in the HLO MESSAGES File (#778) as of the date and time the HLO RECORD COUNT process was run.
11. <u>Messages Sent Today</u>: The total number of messages sent “today.”
12. <u>Messages Received Today</u>: The total number of messages received “today.”
13. <u>Message Errors Today</u>: The total number of message errors “today.”

<u>C.</u> - The following are explanations of actions that can be chosen from the bottom of the HLO System Monitor screen. More detailed information regarding these action items follows in the next section.

1.  <u>LP-List Processes: Will list all the processes that are currently running.</u>
2.  <u>DL-Down Links: Links will appear if they are down. To restart, choose option ‘DL’ to display all down links then choose ‘RL’ (b)to restart a link. (Please note: if you wish to stop a link, choose ‘SL’(a) to stop a link.</u>
3.  <u>OQ-Outgoing Queues: Any down links will be listed with an asterisk ‘\*’ preceding the name. Links that are stopped will be listed with a ‘!’ exclamation point preceding it.</u>
- <u>DQ-Delete Queue</u>: Use this option with caution since you can lose messages!! Enter the link name to delete.
- <u>DM-Display Message</u>: Displays a single message. For explanations regarding these actions, please reference the explanation for MV-HLO MESSAGE VIEWER.
- <u>DT-Del Top Msg</u>: Use this option with caution since you can lose messages!! Also if you wish to delete the top message in a queue, use this option.
- <u>RT-Real Time Display</u>: This option will provide a continuous update display of message data. Press any key to exit this mode.
4.  <u>IQ-Incoming Queues: Choosing this option to display information regarding incoming queues. The ‘From’ (a) column lists the source of the messages. The ‘Queue’ (b) column lists the name of the incoming queue. The count (c) shows the number of messages on that particular queue.</u>
5.  <u>BS-Brief Status: Choosing this option is similar to a ‘refresh’ screen button in windows. It will re-paint the screen with any new data.</u>
6.  <u>ML-Monitor Link: This option will display how many messages are currently pending transmission.</u>
7.  <u>STOP HLO: Use this option to shutdown HLO. All sending and receiving of messages will be halted.</u>
8.  <u>START HLO: Use this option to startup HLO. All sending and receiving of messages will be resumed. Please note: If you want to restart HLO, you do not have to STOP HLO then START HLO. This command issues a STOP HLO before it restarts.</u>
9.  <u>TL-TEST TCP LINK: Enter a TCP link and port then this option will tell you whether the link is operational or not.</u>
10. <u>RT-Real Time MODE: Similar to option (3d) except it will display in real-time any changes to the HLO System Monitor screen.</u>
11. <u>SEQ-SEQUENCE QUEUES: Lists information regarding sequence queues.</u>
12. <u>SQ-START/STOP QUEUE: Use this option to start/stop any incoming/outgoing queue.</u>

### Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### LP – List Processes

This is an action protocol for displaying currently running processes and the system parameters governing those processes. Please refer to Appendix A for a complete overview of the HLO Process Registry.

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:48:36 Page: 1 of 1</u>

<u>Process Type <span class="mark">a</span> MIN <span class="mark">b</span> MAX <span class="mark">c</span> \#RUNNING <span class="mark">d</span> \#QUEUED <span class="mark">e</span></u>

PROCESS MANAGER 1 1 1 0

CHECK PROCESS COUNTS 0 1 0 0

OUTGOING CLIENT LINK 1 10 1 0

INCOMING QUEUES 1 10 1 0

PURGE OLD MESSAGES 0 3 0 0

CLIENT MESSAGE UPDATES 0 0 0 0

REPORT MISSING APP ACKS 0 0 0 0

SET SEARCH X-REF 1 1 1 0

TOTAL MESSAGE COUNTS 0 1 0 0

FIND SEQUENCING PROBLEMS 1 2 1 0

\$J: 14470 -\> OUTGOING CLIENT LINK \<- started at Feb 10, 2005@12:21:01

\$J: 18556 -\> PROCESS MANAGER \<- started at Feb 10, 2005@12:21:01

\$J: 20103 -\> INCOMING QUEUES \<- started at Feb 10, 2005@12:21:01

\$J: 20105 -\> CLIENT MESSAGE UPDATES \<- started at Feb 10, 2005@12:21:01

<span class="mark"><u>\_ Running Processes \_</u></span>

<span class="mark">LP LIST PROCESSES</span> BS BRIEF STATUS TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK RT RealTime MODE

OQ OUTGOING QUEUES STOP HLO SEQ SEQUENCE QUEUES

IQ INCOMING QUEUES START HLO SQ START/STOP QUEUE

Select Action: Quit//

The displayed parameters are:

- <span class="mark">a.</span> Process Type: The name of the process.
- <span class="mark">b.</span> MIN: The minimum number of processes for each process type that must be running on a properly functioning system.
- <span class="mark">c.</span> MAX: The maximum number of processes for each process type that can be running on a properly functioning system.
- <span class="mark">d.</span> \#RUNNING: The number of processes for each process type that are currently running. When HLO is started, only the HLO PROCESS MANAGER process is started. It is the job of the HLO PROCESS MANAGER to start and manage the remaining HLO processes. The \#RUNNING parameter should always be at least as large as the MIN parameter on a fully operational system and no larger than the MAX parameter.
- <span class="mark">e.</span> \#QUEUED: The number of processes for each process type that are scheduled to be started. Usually this number will be zero.

In addition to showing process parameters, the System Monitor screen displays a listing of all currently running processes. Each line in the display shows the job number of a running HLO process, the type of process, and when it was started.

#### BS – Brief Status

This is an action protocol for displaying an overview of the current system. Choosing this option is similar to a “refresh” screen button in windows. It will re-paint the screen with any new data.

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Brief Operational Overview \_</u>

SYSTEM STATUS: RUNNING

PROCESS MANAGER: RUNNING

STANDARD LISTENER: OPERATIONAL

TASKMAN: RUNNING

DOWN LINKS: 0

CLIENT LINK PROCESSES: 0

IN-FILER PROCESSES: 0

MESSAGES PENDING ON OUT QUEUES: 2 ON SEQUENCE QUEUES: 2

STOPPED OUTGOING QUEUES:

MESSAGES PENDING ON APPLICATIONS: 0

STOPPED INCOMING QUEUES:

FILE 777 RECORD COUNT: 28 --\> as of Feb 14, 2005@14:59:02

FILE 778 RECORD COUNT: 28 --\> as of Feb 14, 2005@14:59:02

MESSAGES SENT TODAY: 63432

MESSAGES RECEIVED TODAY: 4318

MESSAGE ERRORS TODAY: 3

<span class="mark"><u>\_ Brief System Status \_</u></span>

LP LIST PROCESSES <span class="mark">BS BRIEF STATUS</span> TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK RT RealTime Mode

OQ OUTGOING QUEUES STOP HLO SEQ SEQUENCE QUEUES

IQ INCOMING QUEUES START HLO SQ START/STOP QUEUE

Select Action: Quit//

#### TL – Test Link

This is an action protocol for determining if a link is operational. User is prompted for a link name. Then the screen displays whether or not the link can be opened.

Select Action: Quit// TL TEST TCP LINK

Select a TCP link: DAYTON OUT

PORT: (1-65535): 5031//

DAYTON OUT IS operational...

Hit any key to continue...

#### DL – Down Links:

This action takes the user to another screen that displays a list of currently failing links and links that have been shutdown, including the number of messages waiting to be transmitted on each link and the time the link was first marked as down. The entry is shown as “SHUTDOWN” if the link was deliberately turned off. The screen contains the actions SHUTDOWN LINK (<span class="mark">a</span>) and RESTART LINK (<span class="mark">b</span>) for starting and stopping messages flowing out of a particular link.

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:47:43 Page: 1 of 1</u>

<u>Client Link Pending Messages Date/Time Down \_</u>

VACLE:5001 33 Mar 23, 2005@15:48:51 SHUTDOWN

VAMAR:5001 1232 Mar 23, 2005@15:49:39

<span class="mark"><u>\_ Down Client Links \_</u></span>

SL SHUTDOWN LINK <span class="mark">a</span> RL RESTART LINK <span class="mark">b</span>

Select Action:Quit//

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:47:43 Page: 1 of 1</u>

<u>Client Link Pending Messages Date/Time Down \_</u>

VACLE:5001 33 Mar 23, 2005@15:48:51 SHUTDOWN

<span class="mark">VAMAR</span>:5001 1232 Mar 23, 2005@15:49:39

<span class="mark"><u>\_ Down Client Links \_</u></span>

SL SHUTDOWN LINK RL RESTART LINK

Select Action:Quit// RL RESTART LINK

Select a TCP Client Link (Outgoing):<span class="mark">VAMAR</span>

#### ML – Monitor Link:

This is an action protocol for monitoring a link. The user is asked for a link name. The protocol displays the number of messages pending transmission for that link. This display automatically refreshes itself periodically.

Select Action: Quit// ML MONITOR LINK

Select a TCP link: DAYTON OUT

Hit any key to stop...

MESSAGES PENDING TRANSMISSION: 0

#### RT – Real Time Mode:

#### This is an action protocol that refreshes whichever screen is currently displayed in “Real Time” mode. The current display is refreshed periodically, with the updated display appearing in the same position as the previous one.

#### OQ – Outgoing Queues:

This is an action protocol for listing all outgoing queues with pending messages and the current number of messages waiting in each queue. Listed links with an asterisk (“\*”) next to them are down. Listed links with an exclamation mark (“!”) next to them are stopped.

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461782

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

<span class="mark"><u>\_ Outgoing Queues \*down links !stopped queues \_</u></span>

DQ DELETE QUEUE DT DEL TOP MSG

DM DISPLAY MESSAGE RT Real Time Display

Select Action: Quit//

<u>OUTGOING QUEUE/DQ-Delete Queue</u>: Use this option with caution since you can lose messages!! Enter the link name to delete.

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461782

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

<span class="mark"><u>\_ Outgoing Queues \*down links !stopped queues \_</u></span>

<span class="mark">DQ DELETE QUEUE</span> DT DEL TOP MSG

DM DISPLAY MESSAGE RT Real Time Display

Select Action: Quit//<span class="mark">DQ</span>

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461782

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

<span class="mark"><u>\_ Outgoing Queues \*down links !stopped queues \_</u></span>

<span class="mark">DQ DELETE QUEUE</span> DT DEL TOP MSG

DM DISPLAY MESSAGE RT Real Time Display

Select Action: Quit//<span class="mark">DQ</span>

!!!!! WARNING! - What you are about to do can result in lost messages !!!!!

!!!!! message sequencing problems and database corruption

Are you sure you want to continue? Enter \<Yes\> to continue? <span class="mark">Yes</span> YES

Please verify by entering \<ConTinue\> EXACTLY as shown : <span class="mark">ConTinue</span>

Enter link name :<span class="mark">VACLE:5001</span>

Enter queue name : <span class="mark">DEFAULT</span>//

The queue of messages that you are about to delete will be purged.

You may now set the planned purge date/time to whatever you would

like, or accept the default.

Enter the purge date/time: Feb 14, 2005@14:59:46//

<u>OUTGOING QUEUE/DM-Display Message</u>: Displays a single message. For explanations regarding these actions, please reference the explanation for MV-HLO MESSAGE VIEWER.

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461930

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

<span class="mark"><u>\_ Outgoing Queues \*down links !stopped queues \_</u></span>

DQ DELETE QUEUE DT DEL TOP MSG

<span class="mark">DM</span> DISPLAY MESSAGE RT Real Time Display

Select Action: Quit//<span class="mark">DM</span> DISPLAY MESSAGE

Message ID: <span class="mark">998 1461930</span>

<u>Single Message Display Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<span class="mark">Administrative Information</span>

MsgID: 998 1461930

Status: PENDING ON OUTGOING QUEUE

Direction: OUT TransDt/Tm: Purge DT/TM:

Link: ZZRH OEX Queue: DEFAULT

<span class="mark">Message Text</span>

MSH\|^~\\\|ZZRN SEND\|998^HL7.REDACTED:5011^DNS\|ZZRN RECEIVE\|050^OEX.F

REDACTED:5031^DNS\|20090413001507-0800\|\|MDM^T02^\|998 1461930\|T^\|2.4\|\|

\|AL\|AL\|USA

PID\|\|\|000000001\|\|HLPATIENT^ONE

PV1\|\|U

TXA\|0001\|OP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|DI

OBX\|\|ST\|\|\| THIS IS THE DOCUMENT TEXT\|\|\|\|\|\|F

<span class="mark">Enter ?? for more actions</span>

SP SET PURGE RP REPROCESS

RS RESEND VP VISUAL PARSER

Select Action:Quit//

<u>OUTGOING QUEUE/DT-Del Top Msg</u>: Use this option with caution since you can lose messages! Also, if you wish to delete the top-most messages in a queue, use this option.

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461782

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

<span class="mark"><u>\_ Outgoing Queues \*down links !stopped queues \_</u></span>

DQ DELETE QUEUE DT DEL TOP MSG

DM DISPLAY MESSAGE RT Real Time Display

Select Action: Quit//<span class="mark">DT</span>

!!!!! WARNING! - What you are about to do can result in lost messages !!!!!

!!!!! message sequencing problems and database corruption

Are you sure you want to continue? Enter \<Yes\> to continue? <span class="mark">Yes</span> YES

Please verify by entering \<ConTinue\> EXACTLY as shown : <span class="mark">ConTinue</span>

Enter link name :<span class="mark">VACLE:5001</span>

Enter queue name : <span class="mark">DEFAULT</span>//

<u>  
OUTGOING QUEUE/RT-Real Time Display</u>: This option will provide a continuous update display of message data. Press any key to exit this mode.

<u>HLO Outbound Queues Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>Link Queue Count Top Message \_</u>

VACLE:5001 DEFAULT 33 998 1461782

\*VAMAR:5001 DEFAULT 1232

!VAROA:5001 DEFAULT 374

Hit any key to escape realtime display mode...

#### STOP HLO:

This is an action protocol for stopping HLO. The process manager sends a request to all currently running processes to stop. Each process responds to the request when it sees it. Some processes will stop immediately and others will stop once they have completed their current task. Use the action “LP” to check for processes that are still running after using this action.

> **WARNING:** If HLO is stopped or disabled for two hours or more, the TCP/IP Service for Open VMS should be disabled at the VMS level and then re-enabled before restarting HLO. Please refer to Section 6.3.6.9 for further instructions on enabling and disabling the TCP/IP Services for Open VMS service.

<u>SEQ-SEQUENCE QUEUES</u>: Lists information regarding sequence queues..

#### IQ – Incoming Queues:

This is an action protocol for listing all incoming queues with pending messages and the current number of messages waiting in each queue (<span class="mark">c</span>). The “From” (<span class="mark">a</span>) column lists the source of the messages. The “Queue” (<span class="mark">b</span>) column lists the name of the incoming queue. Entries with an exclamation mark (“!”) next to them are stopped queues.

<u>HLO SYSTEM MONITOR Feb 14, 2005@14:59:46 Page: 1 of 1</u>

<u>From <span class="mark">a</span> Queue <span class="mark">b</span> Count <span class="mark">c</span> \_</u>

151~FELIX.DAOU.COM:5001~DNS !DEFAULT 21

152~DSI-ALPHA.DAOU.COM:5001~DNS DEFAULT 227

<span class="mark"><u>\_ Incoming Queues (‘!’ = stopped queues) \_</u></span>

LP LIST PROCESSES BS BRIEF STATUS TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK RT RealTime MODE

OQ OUTGOING QUEUES STOP HLO SEQ SEQUENCE QUEUES

IQ INCOMING QUEUES START HLO SQ START/STOP QUEUE

Select Action: Quit//

#### START HLO:

This is an action protocol for starting HLO. When HLO is started, the HLO Process Manager is also started. The HLO Process Manager then starts all the other processes. It will usually take a few seconds for the processes to start. Use the “LP” action to make sure that all necessary processes have started before checking for any results.

> **WARNING:** TaskMan must be running for HLO to start properly.

#### SQ – Start/Stop Queue:

This is an action protocol to start or stop the processing of a selected queue. The user is prompted to:

1.  Start or stop the queue.
2.  Determine if the queue is incoming or outgoing.
3.  Enter the full name of the queue.

> WARNING: There is no verification for the queue name. The user must make sure that the name of an existing queue is entered correctly and in full, at the “Enter the name of queue:” prompt.

<u>  
</u>

Select Action: Quit// SQ START/STOP QUEUE

Select one of the following:

1 START

2 STOP

Do you want to START or STOP a queue: 1// 2 STOP

Select one of the following:

I INCOMING

O OUTGOING

Do you want to stop an incoming queue or an outgoing queue: I// \<Enter\> NCOMING

Enter the name of queue:

#### Q – Quit

This is an action protocol for exiting the System Monitor.

## Message Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Viewer allows users to review individual messages and various error reports. The initial Message Viewer screen is shown below.

<u>HLO MESSAGE VIEWER Aug 03, 2005@09:57:23 Page: 0 of 0</u>

<u>MsgID MsgType Dt/Tm Error Text \_</u>

<span class="mark"><u>\_ Enter ?? for more actions \_</u></span>

DM DISPLAY MSG ER MESSAGE ERRORS MS MESSAGE SEARCH

Select Action: Quit//

### Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### DM – Display Message

This is an action protocol for displaying incoming or outgoing messages. The Message ID is required to perform this action. The user is prompted for a message ID (the string contained in MSH-10). The content of the message is displayed with the message ID.

When a message is displayed, there are several items worth noting:

- Detailed administrative information about the message can be found at the top of the display screen.
- The message text can be found in the middle of the display screen.
- Message segments that are too long to display on just one line will wrap to the next line. Segments requiring additional display lines will be denoted with a reverse video dash placed in front of it (“-“). These specially displayed characters are not part of the actual message. There are three examples of this in the sample displayed below.
- Many messages will require more than one display screen to view the entire message. As with the message below, additional screens can be accessed by selecting the “Next Screen” default when not on the last display screen.

<u>Single Message Display Aug 03, 2005@09:59:39 Page: 1 of 1</u>

<u>\_ \_</u>

<span class="mark">Administrative Information</span>

MsgID: 151 824

Status: SUCCESSFUL

Direction: OUT Trans Dt/Tm: 2/12/05@17:11:04 Purge DT/TM:

Link: TIGER OUT Queue: DEFAULT

Accept Ack: 151 824 At: 2/12/05@17:11:04

MSA\|CA\|151 824\|\|\|\|\|

Accept Ack Rtn: n/a

<span class="mark">Message Text</span>

MSH\|^~\\\|HLOZ MFN\|151^VAABC.MED.VA.GOV:5001^DNS\|HLOZMFN\|^VAXYZ.MED.VA.GOV:5001^

-DNS\|20050212101628-0500\|\|ADT^A08^\|151 824\|T^\|2.4\|\|\|AL\|NE\|USA

EVN\|A08\|20050212101609-0500

PID\|\|63324\|999058704\|369-2958097\|GROZENSO^TED^M\|\|19571230\|M\|\|\|\|\|\|\|\|\|\|\|101058704

PD1\|8\|3\|\|\|5\|\|\|\|\|\|\|N

PV1\|\|O\|1425\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|14\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200402031230-0500\|2004020

–31230-0500

IN1\|1\|\|1348\|XYZ FOUNDATION FOR MEDICAL CARE\|PO BOX 909^^TUSCAN^AZ^12345^USA\|\|\|\|

-L'AUBERGE\|\|\|20010601\|20030131\|\|40\|\|\|\|\|\|1\|\|\|\|\|\|\|\|20020226

IN3\|1\|1\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|1

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

SP SET PURGE RP REPROCESS

RS RESEND VP VISUAL PARSER

#### DM – Display Message/Set Purge:

This option allows you to set a purge date for this single message.

<u>Single Message Display Aug 03, 2005@09:59:39 Page: 1 of 1</u>

<u>\_ \_</u>

<span class="mark">Administrative Information</span>

MsgID: 151 824

Status: SUCCESSFUL

Direction: OUT Trans Dt/Tm: 2/12/05@17:11:04 Purge DT/TM:

Link: TIGER OUT Queue: DEFAULT

Accept Ack: 151 824 At: 2/12/05@17:11:04

MSA\|CA\|151 824\|\|\|\|\|

Accept Ack Rtn: n/a

<span class="mark">Message Text</span>

MSH\|^~\\\|HLOZ MFN\|151^VAABC.MED.VA.GOV:5001^DNS\|HLOZMFN\|^VAXYZ.MED.VA.GOV:5001^

-DNS\|20050212101628-0500\|\|ADT^A08^\|151 824\|T^\|2.4\|\|\|AL\|NE\|USA

EVN\|A08\|20050212101609-0500

PID\|\|63324\|999058704\|369-2958097\|GROZENSO^TED^M\|\|19571230\|M\|\|\|\|\|\|\|\|\|\|\|101058704

PD1\|8\|3\|\|\|5\|\|\|\|\|\|\|N

PV1\|\|O\|1425\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|14\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200402031230-0500\|2004020

–31230-0500

IN1\|1\|\|1348\|XYZ FOUNDATION FOR MEDICAL CARE\|PO BOX 909^^TUSCAN^AZ^12345^USA\|\|\|\|

-L'AUBERGE\|\|\|20010601\|20030131\|\|40\|\|\|\|\|\|1\|\|\|\|\|\|\|\|20020226

IN3\|1\|1\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|1

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

SP SET PURGE RP REPROCESS

RS RESEND VP VISUAL PARSER

Select Action:Quit// SP SET PURGE

When should the message be purged?: (8/3/2005 - 10/13/2005):

### DM – Display Message/Resend:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to resend an outgoing message.

<u>Single Message Display Aug 03, 2005@09:59:39 Page: 1 of 1</u>

<u>\_ \_</u>

<span class="mark">Administrative Information</span>

MsgID: 151 824

Status: SUCCESSFUL

Direction: OUT Trans Dt/Tm: 2/12/05@17:11:04 Purge DT/TM:

Link: TIGER OUT Queue: DEFAULT

Accept Ack: 151 824 At: 2/12/05@17:11:04

MSA\|CA\|151 824\|\|\|\|\|

Accept Ack Rtn: n/a

<span class="mark">Message Text</span>

MSH\|^~\\\|HLOZ MFN\|151^VAABC.MED.VA.GOV:5001^DNS\|HLOZMFN\|^VAXYZ.MED.VA.GOV:5001^

-DNS\|20050212101628-0500\|\|ADT^A08^\|151 824\|T^\|2.4\|\|\|AL\|NE\|USA

EVN\|A08\|20050212101609-0500

PID\|\|63324\|999058704\|369-2958097\|GROZENSO^TED^M\|\|19571230\|M\|\|\|\|\|\|\|\|\|\|\|101058704

PD1\|8\|3\|\|\|5\|\|\|\|\|\|\|N

PV1\|\|O\|1425\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|14\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200402031230-0500\|2004020

–31230-0500

IN1\|1\|\|1348\|XYZ FOUNDATION FOR MEDICAL CARE\|PO BOX 909^^TUSCAN^AZ^12345^USA\|\|\|\|

-L'AUBERGE\|\|\|20010601\|20030131\|\|40\|\|\|\|\|\|1\|\|\|\|\|\|\|\|20020226

IN3\|1\|1\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|1

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

SP SET PURGE RP REPROCESS

RS RESEND VP VISUAL PARSER

Select Action:Quit// RS RESEND

!!!!! WARNING! - What you are about to do can result in lost messages !!!!!

!!!!! message sequencing problems and database corruption

Are you sure you want to continue? Enter \<Yes\> to continue? Yes YES

Please verify by entering \<ConTinue\> EXACTLY as shown : ConTinue

The message has been copied to MsgID 825 which will be displayed next

Do you want the original message purged?? NO//

### DM – Display Message/Reprocess:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to reprocess an incoming message.

### DM – Display Message/Visual Parser:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to manually parse any message.

MSH\|^~\\ ZZRN SEND 998 HL7.REDACTED:5011 DNS\|ZZRN RECEIVE\|050^OEX.F

REDACTED:5011^DNS\|20090424235517-0800\|\|MDM^T02^\|998 1462614\|T^\|2.4\|\|

\|AL\|AL\|USA

PID 000000001 HLPATIENT <span class="mark">ONE</span>

PV1\|\|U

TXA\|0001\|OP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|DI

OBX\|\|ST\|\|\| THIS IS THE DOCUMENT TEXT\|\|\|\|\|\|F

<span class="mark">Q:quit ?:help \[Up/Down/Left/Right Arrow\]:navigation</span>

Segment: \#2 PID Patient identification

Field: \#5 Patient Name Repetition: \#1

Repeating: yes MaxLength: 250 Item \#: 00108

DataType: XPN Table:

Comp: \#2 given name

DataType: ST Table:

Value: <span class="mark">ONE</span>

#### ER – MESSAGE ERRORS:

This is an action protocol for displaying messages for which HLO received application errors (negative application acknowledgements). Application errors can be viewed from a specified date to the present and for a specific application.

Select Action: Quit// ER MESSAGE ERRORS

Enter the beginning date: T-1// \<Enter\> (MAR 10, 2005)

Maximum List Size: (1-30000): 1000//

Include ALL applications? YES// \<Enter\>

Information in the Message Error screen includes:

- Header Line 1, including:
  - Current date and time.
  - Current page number of the results.
  - Total page count of the results.
- Header Line 2, consisting of data column labels, including:
  - MsgID – Message ID, consisting of the site station number and a sequential number, as stored in the querying system.
  - MsgType – Message and Event Type (separated by “~”)
  - Dt/Tm – Message Date and Time (date and time the message was stored for either sending or receiving).
  - Error Text – Brief error description.
- Data Line 1, including:
  - Application – Application Name, based on an application from the HLO APPLICATION REGISTRY File (#779.2).
- Data Line 2, including:
  - Message ID information
  - Message and Event type
  - Message Date and Time
  - Error Text

Below is an example of a system error display. To display more information about the message, select the “DM” action protocol.

<u>HLO MESSAGE VIEWER Mar 11, 2005@17:22:54 Page: 1 of 1</u>

<u>MsgID MsgType Dt/Tm Error Text \_</u>

Application: HLOZ NMQ

151 7499 NMQ~N01 3/10/05@23:43:27 INVALID EVENT CODE

<span class="mark"><u>\_ Enter ?? for more actions \_</u></span>

DM DISPLAY MSG ER MESSAGE ERRORS MS MESSAGE SEARCH

Select Action: Quit//

### MS – Message Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an action protocol for querying existing incoming or outgoing HLO message queues. Message search queries are based on six criteria:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Criteria</strong></th>
<th><strong>Default</strong></th>
<th><strong>Required?</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Beginning Date</td>
<td>T-1 (yesterday)</td>
<td>Yes</td>
<td>The earliest date for which messages should be selected.</td>
</tr>
<tr class="even">
<td>Ending Date/Time</td>
<td>NOW (current date/time)</td>
<td>Yes</td>
<td>The latest date/time for which messages should be selected.</td>
</tr>
<tr class="odd">
<td>Application</td>
<td>NONE</td>
<td>No</td>
<td>Name of a specific application from the HLO APPLICATION REGISTRY File (#779.2).</td>
</tr>
<tr class="even">
<td>Message Type</td>
<td>NONE</td>
<td>No</td>
<td>Three-character message type code.</td>
</tr>
<tr class="odd">
<td>Event Type</td>
<td>NONE</td>
<td>No</td>
<td>Three-character event type code.</td>
</tr>
<tr class="even">
<td>Incoming or Outgoing</td>
<td>NONE</td>
<td>Yes</td>
<td><p>“I” for incoming messages</p>
<p>“O” for outgoing messages</p></td>
</tr>
</tbody>
</table>

Selection will be based on all messages transmitted or received from the beginning date to the selected ending date and time. A blank entry for Application, Message Type, or Event Type will cause all entries to be selected regardless of the value in that field.

The six query criteria are presented to the user in a scrolling format at the bottom of the message viewer screen. Prompting begins after the user has selected the action “MS.” Refer to the screen below for an example.

<u>HLO MESSAGE VIEWER Mar 20, 2005@14:31:16 Page: 0 of 0</u>

<u>MsgID MsgType Dt/Tm Error Text \_</u>

<span class="mark"><u>\_ Enter ?? for more actions \_</u></span>

DM DISPLAY MSG ER MESSAGE ERRORS MS MESSAGE SEARCH

Select Action: Quit// <span class="mark">MS</span> MESSAGE SEARCH

Enter the beginning date: Mar 19, 2005// \<Enter\> (MAR 19, 2005)

Enter the ending date/time: NOW// \<Enter\> (MAR 20, 2005@14:31:33)

Application: XYZ VISTA

HL7 Message Type: ADT

HL7 Event: A08

Select one of the following:

I INCOMING

O OUTGOING

Incoming or Outgoing: OUTGOING

After the message search parameters are entered, all matching messages are listed in the Message Search result screen (see example below). Information in the results screen includes:

- Header Line 1, including:
  - Current date and time
  - Current page number of the results
  - Total page count of the results
- Header Line 2, consisting of data column labels, including:
  - MsgID – Message ID, consisting of the site station number and a sequential number, as stored in the querying system
  - Application – Application Name, based on an application from the HLO APPLICATION REGISTRY File (#779.2)
  - MsgType – Message and Event Type (separated by “~”)
- Header Line 3, consisting of data column labels, including:
  - Dt/Tm – Message Date and Time (date and time the message was stored for either sending or receiving
  - Facility – Information for the facility either sending the message (for incoming messages) or receiving the message (for outgoing messages)
- Data Line 1, including:
  - Message ID information
  - Application name
  - Message and Event type
- Data Line 2, including:
  - Message date and time
  - Sending or Receiving facility

At the bottom of each result screen is the “Select Action” prompt. If the displayed page is not the last page, the default action will be “Next Screen,” which displays the next screen of results. If the displayed page is the last page, the default action is “Quit,” which takes the user back to the original Message Viewer screen (see the next two example screens).

<u>Message Search Mar 20, 2005@14:31:57 Page: 1 of 1</u>

MsgID Application MsgType

<u>Dt/Tm Facility \_</u>

151 94 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 95 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 96 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 97 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 98 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 99 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

DM Display Message

Select Action: Next Screen// \<Enter\>

<u>Message Search Mar 20, 2005@14:32:12 Page: 2 of 2</u>

MsgID Application MsgType

<u>+ Dt/Tm Facility \_</u>

151 247 XYZ VISTA ADT~A08

3/19/05@10:16:14 ^VAXYZ.VA.MED.GOV:5001^DNS

151 248 XYZ VISTA ADT~A08

3/19/05@10:16:14 ^VAXYZ.VA.MED.GOV:5001^DNS

151 249 XYZ VISTA ADT~A08

3/19/05@10:16:14 ^VAXYZ.VA.MED.GOV:5001^DNS

151 250 XYZ VISTA ADT~A08

3/19/05@10:16:14 ^VAXYZ.VA.MED.GOV:5001^DNS

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

DM Display Message

Select Action: Quit// \<Enter\>

To display a message selected by the message search, use the action of “DM” (Display Message). After entering “DM,” enter the message ID associated with the message to be displayed (see example below).

<u>Message Search Mar 20, 2005@14:31:57 Page: 1 of 2</u>

MsgID Application MsgType

<u>Dt/Tm Facility \_</u>

151 94 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 95 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 96 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 97 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 98 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 99 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

DM Display Message

Select Action: Next Screen// DM Display Message

Message ID: 151 97

Once a message ID has been entered, the Single Message Display screen appears. The screen consists of:

- Administrative Information, including:
  - MsgID – Message ID, consisting of the site station number and a sequential number, as stored in the querying system
  - Status – Message Status (Successful of Unsuccessful)
  - Dir – Message direction (Incoming or Outgoing)
  - Trans Dt/Tm – Transmission Date and Time
  - Link: Port Number – Sending (for incoming) or Receiving (for outgoing) link followed by a colon and the port number of the link
  - Queue – Message queue
  - Accept Ack – Accept Ack information
  - At – Date and Time Ack received

Accept Ack Rtn – Optional routine call for responding to an Accept Ack. (Please see Section 2.3 of the *Health Level Seven Optimized (HLO) Developer Manual* for more details on creating the routine.)

- Message Text – Segment-by-segment display of the message. Segments requiring more than one display line are denoted with a reverse video dash placed in front of it (<span class="mark">-</span>). These specially displayed characters are not part of the actual message.

In cases where a message requires more than one screen, the user will be prompted to go to the next screen with a default Select Action of “Next Screen.” If the Single Message Display screen contains the end of the message, the default Select Action will be “Quit,” which will return the user back to the query results. The Select Action of “Quit” can be used at any time to return to the previous activity.

Please refer to the next three sample screens as examples of how the message display works within a message search.

First Message Display Screen:

<u>Single Message Display Mar 20, 2005@14:35:18 Page: 1 of 2</u>

<u>\_</u>

<span class="mark">Administrative Information</span>

MsgID: 151 97

Status: SUCCESSFUL

Dir: OUT Trans Dt/Tm(1X): 3/19/05@10:16:57 Purge DT/TM: 3/24/05@10:16:57

Link: VAXYZ Queue: DEFAULT

Accept Ack: 151 97 DT.TM Ack’d: 3/19/05@10:16:57

MSA\|CA\|151 97\|\|\|\|\|

Accept Ack Rtn: n/a

<span class="mark">Message Text</span>

MSH\|^~\\\|XYZ VISTA\|151^VAABC.MED.VA.GOV:5001^DNS\|XYZ HDM\|^VAXYZ.MED.VA.GOV:5001^

<span class="mark">-</span>DNS\|20050319-101612-0500\|\|ADT^A08^\|151 97\|T^\|2.4\|\|\|AL\|NE\|USA

EVN\|A08\|20050319101529-0500

PID\|\|55126\|999074037\|649-2959460\|ZEAL^ROBERT^U\|\|19350709\|M\|\|\|\|\|\|\|\|\|\|\|101074037

PD1\|5\|\|\|\|5\|\|\|\|\|\|\|Y

PV1\|\|O\|68\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|14\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200405071030-0500\|2004050710

<span class="mark">-</span>30-0500

IN1\|1\|\|1156\|MEDICARE (WNR)\|PO BOX ^844 N MAIN ST^PHOENIX^MD^20765-5520^USA\|\|\|\|PA

<span class="mark">-</span>RT A\|\|\|20000701\|\|\|33\|\|\|\|\|\|1\|\|\|\|\|\|\|\|20030709

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

Select Action: Next Screen// \<Enter\>

Second Message Display Screen:

<u>Single Message Display Mar 20, 2005@14:35:36 Page: 2 of 2</u>

<u>+ \_</u>

IN3\|1\|1\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|0

ZN1\|1\|WITHIN 1YR FROM DOS\|

IN3\|2\|2\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|0

ZN1\|1\|WITHIN 1YR FROM DOS\|

IN3\|3\|3\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|0

ZN1\|1\|WITHIN 1YR FROM DOS\|

IN3\|4\|4\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|0

ZN1\|1\|WITHIN 1YR FROM DOS\|

IN3\|5\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|0

ZN1\|1\|WITHIN 1YR FROM DOS\|

Z3M\|1\|^N\|^N\|^N\|^N\|^N\|\|^N

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

Select Action: Quit// \<Enter\>

Back to Message Search Result Screen After Selecting “Quit”:

<u>Message Search Mar 20, 2005@14:38:12 Page: 1 of 28</u>

MsgID Application MsgType

<u>Dt/Tm Facility \_</u>

151 94 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 95 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 96 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 97 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 98 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

151 99 XYZ VISTA ADT~A08

3/19/05@10:16:12 ^VAXYZ.VA.MED.GOV:5001^DNS

<span class="mark"><u>+ Enter ?? for more actions \_</u></span>

DM Display Message

Select Action: Next Screen//

#### Q – Quit

This is an action protocol for exiting the Message Viewer.

## Application Registry (HLO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application developers must create entries in the application registry as part of building a new HLO messaging application. Application registries are usually required in conjunction with the installation of a new or updated messaging application that is using HLO.

> **WARNING:** This option is for the use of application developers only. IRMs should not normally be accessing this option unless directed by a developer. Refer to Chapter 6 for additional information.

## TaskMan-Scheduled Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In HLO, there are two TaskMan-scheduled options not listed on the main HLO menu: the HLO COUNT RECORDS option and the HLO SYSTEM STARTUP option.

### HLO COUNT RECORDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to Section 5.4 for detailed instructions on scheduling this option.

### HLO SYSTEM STARTUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to Section 5.5 for detailed instructions on scheduling this option.

### HLO Daily STARTUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to Section 5.5 for detailed instructions on scheduling this option.

## HLO MESSAGE STATISTICS REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides counts of messages by application over a period selected by the user. The user is given a choice of reporting monthly, daily, or hourly statistics. Hourly statistics are generally maintained only for the last 48 hours, daily statistics are available for the last 31 days, and monthly statistics are kept indefinitely.

# Appendix A - The HLO Process Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DANGER: This section is for information only. Do not use the information in this section to modify the HLO Process Registry. Only the two fields, ACTIVE and DEDICATED LINK should ever be modified by IRMs or application developers. However, this section may be useful for troubleshooting problems with the HLO system.

## HLO Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The processes involved with the HLO system are:

- PROCESS MANAGER – This process should always be running while HLO is turned on. It starts the other HLO processes via Taskman as they are needed. The listener running under VMS is a notable exception since it is created as a VMS TCP/IP Service and is not managed by the HLO Process Manager.
- SINGLE LISTENER – The server process for the listener that is designed to only accept a single connection, receive messages, and put them on designated inbound queues.
- TASKMAN MULTI-LISTENER – The server process for the listener that is started from TaskMan and can accept multiple connections, receive messages, and put them on designated inbound queues. Used for sites which are not running under OpenVMS.
- OUTGOING CLIENT LINK – These processes initiate the sending of messages that are pending on outbound queues.
- INCOMING QUEUES – These processes take received messages from inbound queues and invoke the appropriate applications’ logic.
- CHECK PROCESS COUNTS – This process intermittently recounts the running and scheduled processes.
- CLIENT MESSAGE UPDATES – This process updates message status information as requested by other processes.
- PURGE OLD MESSAGES – This process removes messages that are older than the defined purge date/time.
- TOTAL MESSAGE COUNTS – This process totals message counts by message type for hourly, daily, and monthly intervals.
- FIND SEQUENCING PROBLEMS - When using sequence queues, If an application acknowledgment is still outstanding after the time limit specified by the application, then this process will execute the application’s exception routine.

> **NOTE:** The sequence queue is stalled until the application acknowledgment is returned, so the application team needs to investigate.

HLD(779.2,D0,0)= (#.01) APPLICATION NAME \[1F\] ^ (#.02) RESPONSE LINK

               ==\>(OPTIONAL) \[2F\] ^ (#.03) DEFAULT PRIVATE IN-QUEUE \[3F\] ^

               ==\>(#.04) BATCH ACTION TAG \[4F\] ^ (#.05) BATCH ACTION ROUTINE

               ==\>\[5F\] ^ (#.06) DEFAULT ACTION TAG \[6F\] ^ (#.07) DEFAULT

               ==\>ACTION ROUTINE \[7F\] ^ (#.08) BATCH PRIVATE IN-QUEUE \[8F\] ^

               ==\>(#.09) APPLICATION SPECIFIC LISTENER \[9P:870\] ^ (#.1)

               ==\>SEQUENCE EXCEPTION TAG \[10F\] ^ (#.11) SEQUENCE EXCEPTION

               ==\>ROUTINE \[11F\] ^ (#.12) SEQUENCING TIMEOUT \[12N\] ^

## The HLO Process Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO Process Manager is the HLO component that manages all of the processes that make up the HLO system. It uses the HLO PROCESS REGISTRY File (#779.3) which contains information about each type of process under the Process Manager’s control. Since only the HLO development team should require access to the HLO PROCESS REGISTRY File (#779.3), it does not require a special user input screen.

*Processes running under the Process Manager are dynamic; they start and stop in response to changing workload.*

### HLO PROCESS REGISTRY File (#779.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file contains these fields:

| PROCESS NAME                   | FREE TEXT       | A unique name for the type of process.                                                                                                                                                                                                                                                                  |
|--------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTIVE                         | SET (YES or NO) | A flag that indicates whether or not this type of process is active under the HLO Process Manager. Some processes may not apply to some systems; for example, a particular site may not use the TaskMan multi-listener.                                                                                 |
| MINIMUM ACTIVE PROCESSES       | NUMERIC         | This field indicates the minimum number of concurrent processes of this type. The actual number of processes changes as the HLO Process Manager starts and stops processes in response to changes in workload, but there should always be at least as many as this field indicates.                     |
| MAXIMUM ACTIVE PROCESSES       | NUMERIC         | This field indicates the maximum number of concurrent processes of this type. The actual number of processes changes as the HLO Process Manager starts and stops processes in response to changes in workload, but it should never exceed the number specified in this field.                           |
| SCHEDULING FREQUENCY (minutes) | NUMERIC         | This is how long the Process Manager should wait between checks to see if another process of this type should be started.                                                                                                                                                                               |
| DT/TM LAST STARTED OR STOPPED  | DATE/TIME       | The date and time when a process of this type was last started or stopped.                                                                                                                                                                                                                              |
| HANG TIME (seconds)            | NUMERIC         | This is how long a process should wait between attempts to find work to do.                                                                                                                                                                                                                             |
| GET WORK FUNCTION (TAG)        | FREE TEXT       | The M entry point for the process’s GET WORK function.                                                                                                                                                                                                                                                  |
| GET WORK FUNCTION (ROUTINE)    | FREE TEXT       | The routine in which the process’s GET WORK function is located.                                                                                                                                                                                                                                        |
| DO WORK FUNCTION (TAG)         | FREE TEXT       | The M entry point for the process's DO WORK function.                                                                                                                                                                                                                                                   |
| DO WORK FUNCTION (ROUTINE)     | FREE TEXT       | The routine in which the process's DO WORK function is located.                                                                                                                                                                                                                                         |
| MAX TRIES FINDING WORK         | NUMERIC         | The number of times the process looks for work before quitting. It will hang between attempts the specified length of time.                                                                                                                                                                             |
| PERSISTENT                     | SET (YES or NO) | Setting this field to YES results in the process being made persistent via the TaskMan persistent parameter.                                                                                                                                                                                            |
| DEDICATED LINK                 | FREE TEXT       | The primary use of this field is for TCP/IP listener processes, and indicates on which port (via the HL Logical Link) the process should be listening. However, it could be used to dedicate a client link process to a particular link.                                                                |
| VMS TCP SERVICE                | SET (YES or NO) | VMS services are not started or stopped via the HLO Process Manager. However, on a VMS system, these services are an important part of the HLO system, and an entry in the HLO PROCESS REGISTRY File (#779.3) should be created for them. The Process Manager will verify that the listener is running. |

### Process Manager Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Manager runs continuously after the HLO system is started. A scheduled option ensures that the HLO system is started at system start up. There are also actions in the HLO System Monitor that allow the HLO system to be started or stopped. Starting the HLO system starts a new instance of the process manager, which in turn starts all of the other necessary processes found in the process registry. A lock is used to ensure that only one instance of the process manager is running.

The Process Manager itself also has an entry in the HLO PROCESS REGISTRY File (#779.3), and executes within the same framework as all the other processes.

### Generic Framework Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All processes (including the process manager) execute the same framework process, starting at the same entry point. The processes are started via TaskMan knowing only the process name. The process then looks up its entry in the HLO Process Registry and tailors its behavior according to the parameters defined there; the primary ones are the GET WORK function and the DO WORK function. The framework process is as follows:

- Get the process parameters from the process registry using the process name to do a look up.
- The process manager checks the minimum and maximum parameters of the process and determines whether or not another process needs to be started. The information on the current number of processes running is periodically updated by the CHECK PROCESS COUNTS process.

> **NOTE:** If the process counts seem to be out of sync, a little time may be needed for re-synchronization.

- The process manager calls the GET WORK function of the process that is executing. If work is found, then the DO WORK function is called. This procedure is repeated until either the HLO system is shut down or GET WORK fails to find work. Once GET WORK fails to find work it will try the ‘MAX TRIES FINDING WORK’ to find work waiting the ‘HANG TIME (seconds)’ between attempts. If no work found the process exits after rescheduling itself to try later.

# Appendix B – Creating TCP/IP Services for Open VMS with DSM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Note for Multi-Node Cluster Sites:</u>

For sites configured with a multi-node cluster, more than one node may be advertised under the domain name HL7.SITENAME.MED.VA.GOV and the TCP/IP service may be running on multiple nodes.

In addition, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process to remain uninterrupted if the TCP/IP service is enabled on all nodes in the cluster.

If this is the case for your site, be sure to enable the service on all these nodes after setting up the TCP/IP service and COM file on one of these nodes.

## Create OpenVMS User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create an OpenVMS User Account:

1.  If an account already exists for HL7 1.6, use the same user account. Review the settings for that user account to insure conformance to the screen below, then skip to Section 9.3 below to “Create a DCL Command Procedure.”
2.  Determine an unused User Identification Code (UIC), typically in the same group as other DSM for OpenVMS accounts.
3.  Using the OpenVMS Authorize utility, add the new HLSEVEN account with the unused UIC. You must have SYSPRV to do this.
4.  Verify that the account settings for the new HLSEVEN account are the same as they appear in the example that follows; or, if they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY, Restricted, and Captive flags are set.

There are two different ways to set up a new user account, and you are free to choose the one you prefer. The following two examples illustrate two different ways to set up an OpenVMS User account:

One way to set up an OpenVMS User account is to copy your existing XMINET (TCP/IP MailMan) account to a new account with an unused UIC. For example:

> \$ MC AUTHORIZE

> UAF\> COPY /ADD XMINET HLSEVEN/UIC=\[51,45\]/DIR=\[HLSEVEN\]

> %UAF-I-COPMSG, user record copied

> %UAF-W-DEFPWD, copied or renamed records must receive new password

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000051,000045\] added to rights database

> UAF\>

The other way to set up an Open VMS User account is to add the new HLSEVEN OpenVMS account directly. For example:

> \$ MC AUTHORIZE

> UAF\> ADD HLSEVEN /UIC=\[100,45\]/OWNER="HLSEVEN" - (must use continuation character "-")

> \_UAF\> /DEVICE=USER\$/DIRECTORY=\[HLSEVEN\] -

> \_UAF\> /NOACCESS/NETWORK/FLAGS=(DISCTLY,RESTRICTED,NODISUSER) -

> \_UAF\> /PRIV=(NETMBX,TMPMBX) -

> \_UAF\> /DEF=(NETMBX,TMPMBX)/LGICMD=NL:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000100,000045\] added to rights data

> base

> UAF\>

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: HLSEVEN

> Account: UIC: \[100,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[HLSEVEN\]

> LGICMD: NL:

> Flags: DisCtlY Restricted

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 100 Bytlm: 64000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 150 WSdef: 2000

> Prio: 4 ASTlm: 250 WSquo: 4000

> Queprio: 4 TQElm: 10 WSextent: 16384

> CPU: (none) Enqlm: 2000 Pgflquo: 50000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

> UAF\> Exit

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> \$

## Create OpenVMS Home Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a home directory already exists for HL7 1.6, then use the same home directory. Skip to Section 9.3 below to “Create a DCL Command Procedure.”

This directory will house the DCL command procedure which is executed whenever a client connects. A log file is created for every instance of a connection for that listener. Make sure that the owner of the directory is the HLSEVEN account.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

\$ CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

## Create a DCL Command Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure (shown below) in the home directory for the HLSEVEN account and name it according to the recommended convention. Make sure the command procedure file is owned by the HLSEVEN account.

1.  To create a DCL command procedure that will use port 5001, name your command procedure file as HLS5001DSM.COM.
2.  Adjust the DSM command line (environment, UCI, and volume set) for your system.
3.  If access control is enabled, ensure that the HLSEVEN account has access to this UCI, volume set, and routine (see “Access Control List (ACL) Issues” later in this chapter).
4.  Ensure that the name of the DCL command file, as described in step 1, matches the port assignment. For example, if you changed the port number from 5001 to 6788, rename your HLS5001DSM.COM file to HLS6788DSM.COM.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts, Port \#5026 must be used.

For your convenience, you can cut and paste the following DCL command procedure file into your OpenVMS HLSEVEN device and directory.

Sample DCL Command Procedure file:

\$! HLS5001DSM.COM - for incoming tcp connect requests with port=5001 and

\$! using "DSM" command line to enter the M environment

\$! File name HLS5001DSM.COM is recommended to be changed to reflect the

\$! change of the TCP/IP port number. For example, file name could be

\$! changed to HLS6788DSM.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5001CACHE.COM and HLS5001DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is

\$! \*\*enabled, that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$! \*\*Also, comment or uncomment the appropriate lines for your system.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------\$! for DSM\$ dsm/env=dsmmgr/uci=vah/vol=tou VMS^HLOSRVR\$!-------------------------------------------------------------

\$! for Cache

\$!assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!csession cache "-U" "VAH" "VMS^HLOSRVR"

\$!-------------------------------------------------------------

\$ endif

\$ exit:

\$ logout/brief

## Set Up the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the TCP/IP service to listen for connections:

1.  Choose the OpenVMS node where you want to run the TCP/IP service listener. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener.
2.  Use TCP/IP port number 5001 on production systems and 5026 on test systems.
3.  Use user account HLSEVEN.
4.  Use DCL command file name HLS5001DSM.COM.

> **WARNING:** All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts, Port \#5026 must be used

> **NOTE:** Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

Ensure that your new TCP/IP service uses the recommended naming convention. For example, set up a service that will be listening on port 5001 and use a corresponding DCL command file HLS5001DSM.COM.

Set the service name as HLS5001DSM as follows:

\$ TCP/IP (must use continuation character "-" at end of long lines)

TCP/IP \> SET SERVICE HLS5001DSM/USER=HLSEVEN/PROC=HLS5001DSM /PORT=5001-

\_TCP/IP \> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCP/IP \> <span class="mark">/LIMIT=50/</span>FILE=USER\$:\[HLSEVEN\]HLS5001DSM.COM

In this command, <span class="mark">/LIMIT=50/</span> specifies the maximum number of TCP/IP connections that can be made at any time. The limit of 50 is appropriate for most local sites, but for systems that serve as national databases the limit should be set initially to 500. The system manager is responsible for monitoring the peak number of connections made, and if the peak approaches the limit, the limit should be increased.

If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.

> TCP/IP \> SET CONFIG ENABLE NOSERVICE HLS5001DSM

> TCP/IP \> SET NOSERVICE HLS5001DSM

TCP/IP \> SHO SERVICE HLS5001DSM/FULL

Service: HLS5001DSM

State: Disabled

Port: 5001 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5001DSM

## Enable and Save the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since TCP/IP Services is node specific, make sure you are on the same node on which the listener will run.

TCP/IP \> ENABLE SERVICE HLS5001DSM *<span class="mark">(enable service immediately)</span>*

TCP/IP \> SET CONFIG ENABLE SERVICE HLS5001DSM *<span class="mark">(save service for reboot)</span>*

TCP/IP \> SHO SERVICE/FULL HLS5001DSM

Service: HLS5001DSM

State: <u>Enabled</u>

Port: 5001 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5001DSM

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\] HLS5001DSM.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCP/IP \> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, <span class="mark">HLS5001DSM</span>, MPI, TELNET, XMINETMM

TCP/IP \> EXIT

## Access Control List (ACL) Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some sites use DSM's ACL feature, which controls access explicitly to each OpenVMS account that needs to enter that DSM environment. If your site is using ACL, you should set up the HLSEVEN account with PROGRAMMER access, and then specify the Volume set and UCI name that the HLSEVEN user account has authorization to access. Ensure that the OpenVMS HLSEVEN account prohibits Batch, Local, Dialup, and Remote logins, allowing only Network logins.

An example of setting this level of access for an HLSEVEN account is provided below:

\$ DSM /MAN ^ACL

Environment Access Utilities

1\. ADD/MODIFY USER (ADD^ACL)

2\. DELETE USER (DELETE^ACL)

3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

4\. PRINT AUTHORIZED USERS (PRINT^ACL)

Select Option \> 1 \<Enter\> ADD/MODIFY USER

OpenVMS User Name: \> HLSEVEN

ACCESS MODE VOL UCI ROUTINE

----------- --- --- -------

No access rights for this user.

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> P

Volume set name: \> VAH

UCI: \> ROU

UCI: \> \<Enter\>

Volume set name: \> \<Enter\>

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> \<Enter\>

USER ACCESS MODE VOL UCI ROUTINE

---- ----------- --- --- -------

HLSEVEN PROGRAMMER ROU VAH

OK to file? \<Y\> \<Enter\>

OpenVMS User Name: \> \<Enter\>

OK to activate changes now? \<Y\> \<Enter\>

Creating access authorization file: USER\$:\[DSMMGR\]DSM\$ACCESS.DAT.

## Control the Number of Log Files Created by TCP/IP Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLS5001DSM TCP/IP service automatically creates log files (TCP/IP services does this and it cannot be prevented) in the HLSEVEN directory named HLS5001DSM.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME USER\$:\[HLSEVEN\]HLS5001DSM.LOG; USER\$:\[HLSEVEN\]HLS5001DSM.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 USER\$:\[HLSEVEN\]HLS5001DSM.LOG;

> **NOTE:** This cannot be done until the first log file has actually been created.

You probably should not limit the number of versions of the log file until you know that your HLS5001DSM service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

## Other TCP/IP Service Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** If HLO is stopped or disabled for two hours or more, the VMS Multi-Listener service should be disabled and then re-enabled before restarting HLO.

The definition of a link is required for the multi-threaded listener for Open VMS systems. This link never needs to be started or stopped through the VistA HL 1.6 or HLO options. Instead, it is normally started and stopped via TCP/IP services. For example:

TCP/IP \> DISABLE SERVICE HLS5001DSM *(Stop* TCP/IP *service)*

TCP/IP \> ENABLE SERVICE HLS5001DSM *(Start* TCP/IP *service)*

Any questions about configuring TCP/IP Service for OpenVMS should be directed to EVS for assistance

# Appendix C – Daily Oversight and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Daily Oversight

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HLO System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM staff should check the operational status of HLO several times daily using the HLO System Monitor. Please refer to Section 7.2 of this document for complete instructions. The Brief System Status screen provides all the information necessary. The following should be verified:

- SYSTEM STATUS is RUNNING
- PROCESS MANAGER is RUNNING
- STANDARD LISTENER is OPERATIONAL
- TASKMAN is RUNNING
- DOWN LINKS is 0 (zero)
- MESSAGES PENDING ON OUT QUEUES is not unusually large
- STOPPED OUTGOING QUEUES is blank
- MESSAGES PENDING ON APPLICATIONS is not unusually large
- STOPPED INCOMING QUEUES is blank

If any of these conditions indicate that there may be a problem, then investigate further by following instructions found in Section 7.2 of this document.

## HLO Message Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IRM should run three reports on a daily basis and review them for signs of problems. Refer to Section 7.3 of this document for further details on these reports. Potential problems should be fully investigated and either corrected or referred to the appropriate subject experts. For example, if a message is not processed due to an application error, the problem might need to be referred to the appropriate package expert.

> The reports are:

- System Errors – these are messages that were not passed to the Receiving Application for any reason. An example might be a message whose header lacked the Receiving Application field.
- Application Errors – these are messages that were passed to the Receiving Application, but the application was unable to fully process the message. Usually errors of this type require subject matter expertise to resolve.
- Transmission Failures – these are messages that could not be transmitted after three days, despite multiple attempts. Errors of this type occur when the listener process at the receiving facility is running but for some reason it is unable to respond properly.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem \#1:

After installing patch HL\*1.6\*126 and establishing the HLO standard listener, the existing HL7 1.6 listener stopped working.

Solution:

Were any of the field values in the HL LOGICAL LINK File (#870) used by the existing listener modified or deleted? Some fields in the HL LOGICAL LINK File (#870) are not used by HLO, but listeners running under the existing HL7 1.6 still need them. If any field was altered where the set up instructions did not explicitly state to do so, restore the old value.

Problem \#2:

The HLO System Monitor shows the status of the Standard Listener as NOT OPERATIONAL even though the listener set up was completed.

Solution:

1.  Double-check that the VMS TCP/IP service was enabled.
2.  Double-check that the entry in the HL LOGICAL LINK File (#870) for the listener has these fields completed:
    1.  TCP/IP PORT (OPTIMIZED) field (#400.08)
    2.  TCP/IP ADDRESS field (#400.01)
3.  Double-check that the HLO SYSTEM PARAMETERS File (#779.1) IEN=1 (there should be exactly one entry) for the HLO STANDARD LISTENER field (#.1) points to the correct listener entry in the HL LOGICAL LINK File (#870). (see 2. above)

Problem \#3:

The HLO Message Monitor shows “SE” System Errors for a newly installed application.

Solution:

Check the HL Logical Link record for the application and verify the following:

1.  The DNS DOMAIN field (#.08) is set to the correct domain.
2.  The TCP/IP ADDRESS field (#400.01) is set to the correct address.
3.  The TCP/IP PORT (OPTIMIZED) field (#400.08) is set to the correct port number (production is 5001 and test is 5026).

Problem \#4:

A DOWN LINK is found when checking the HLO System Monitor.

Solution:

Check the following:

1.  The link entry parameters in the HL LOGICAL LINK File (#870) are correct.
2.  The listener process at the receiving facility is running.
3.  Network connections between the sending and receiving facility are operating normally.

For any questions or problems related to installation issues or other errors not described in this document, please contact EVS and request technical support.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accept Acknowledgement                   | From the HL7 standard: "The receiving system commits the message to safe storage in a manner that releases the sending system from any obligation to resend the message. A response is returned to the initiator indicating successful receipt and secure storage of the information."[^3]                                                                                                                                                                           |
| Acknowledgement                          | A software handshake method used by HL7. When a system receives a message, it may send back an "accept acknowledgement" message to confirm the data was received. It may also send back an "application acknowledgement" message to confirm if the data received was appropriate.                                                                                                                                                                                    |
| Application                              | In the terminology of VistA HLO, an application sends and/or receives messages through the interface between two systems. The application consists of a sending and receiving entry in the HLO APPLICATION REGISTRY File (#779.2).                                                                                                                                                                                                                                   |
| Application Acknowledgement              | From the HL7 standard: "The appropriate application on the receiving system receives the transaction and processes it successfully. The receiving system returns an application-dependent response to the initiator."[^4]                                                                                                                                                                                                                                            |
| Commit Acknowledgement                   | See Accept Acknowledgement                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Enterprise Application Integration (EAI) | Combines the technologies and processes that enable COTS and/or in-house-developed software applications to exchange information in the formats and contexts that each understands.                                                                                                                                                                                                                                                                                  |
| Event                                    | A healthcare event, such as an admission, discharge or bed transfer, inter-ward transfer, transfer to a new treating specialty, etc., that causes a need for information to flow between two or more applications.                                                                                                                                                                                                                                                   |
| Event Driver Protocol                    | For VistA HL 1.6, an event driver protocol represents the sending application's side of a transaction for a particular message type/event type, whether the message originates on the VistA side of the interface, or on the other side of the interface. Protocols are used in HL 1.6 but not in HLO. HLO conversion APIs use the HL 1.6 protocol to retrieve application parameters.                                                                               |
| Event Type                               | Trigger event code (one component of a message header's Message Type field) defined by *HL7 table 0003 - Event typ*e.                                                                                                                                                                                                                                                                                                                                                |
| Field                                    | A specific unit of data within an HL7 *segment*. Each field is defined by the following set of characteristics: Position in the Segment, Maximum Length, Data Type, Optionality, Repetition, Table Assignment (optional), ID Number, and Name.                                                                                                                                                                                                                       |
| Header                                   | The first segment in an HL7 message. Usually it is a message header segment (MSH) but it can also be the batch header segment (BHS) or file header segment (FHS). The header defines the intent, source, destination, and some specifics of the syntax of a message.                                                                                                                                                                                                 |
| HL7                                      | Health Level Seven. An ANSI standard that specifies how information exchange should occur between healthcare applications in a healthcare environment. It permits data exchange between heterogeneous applications and systems through a messaging architecture.                                                                                                                                                                                                     |
| HLO                                      | “HL7 Optimized” Enhanced HL7 engine for VistA HL7, Version 1.6.                                                                                                                                                                                                                                                                                                                                                                                                      |
| HLO Standard Listener                    | This is the HL Logical Link entry that defines the primary listener for facility. Port number must be 5001 on production systems and 5026 on a sites main test system.                                                                                                                                                                                                                                                                                               |
| Interface                                | The negotiated HL7 specification between two or more systems, defining the supported transactions.                                                                                                                                                                                                                                                                                                                                                                   |
| Link                                     | An entry in the HL Logical Link File (#870) that links VistA HLO to a particular destination. The destination is a TCP/IP address and port or a DNS DOMAIN.                                                                                                                                                                                                                                                                                                          |
| Logical Link                             | See Link.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Message                                  | From the HL7 standard, "A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT Message type is used to transmit portions of a patient’s ADT data from one system to another. A three character code contained within each message identifies its type."[^5]                                                  |
| Message Type                             | Message type code (one component of a message header's Message Type field) defined by *HL7 table 0076 - Message typ*e.                                                                                                                                                                                                                                                                                                                                               |
| Protocol                                 | For each message type (e.g., A01) sent or received by any given interface (e.g., Radiology), one PROTOCOL File (#101) entry on your system is used to represent the sending application (event driver protocol) and one PROTOCOL File (#101) entry on your system is used to represent the receiving application (subscriber protocol). Protocols are used in HL 1.6 but not in HLO. HLO conversion APIs use the HL 1.6 protocol to retrieve application parameters. |
| Segment                                  | From the HL7 standard, "An HL7 segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is identified by a unique three character code known as the Segment ID."[^6]                                                                                                                                                                    |
| Subscriber                               | An application that subscribes to a particular event point, registering its interest so it can receive unsolicited updates. This is used in HL 1.6 but not in HLO. HLO conversion APIs use the HL 1.6 protocol to retrieve application parameters.                                                                                                                                                                                                                   |
| Subscriber Protocol                      | For VistA HL7, a subscriber protocol represents the receiving application's side of a particular transaction for a particular message type/event type, whether the message is being received by the VistA side of the interface, or by the other side of the interface. Protocols are used in HL 1.6 but not in HLO. HLO conversion APIs use the HL 1.6 protocol to retrieve application parameters.                                                                 |
| Queue                                    | Incoming and outgoing queues are used by VistA HLO to manage message delivery.                                                                                                                                                                                                                                                                                                                                                                                       |
| Trigger Event                            | An event that initiates an action. In the case of HL7, a specific event within an application might trigger the generation of a message.                                                                                                                                                                                                                                                                                                                             |

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Acknowledgements, 6

Application Registry, HLO Management System, 79

C

COUNT RECORDS Option, Scheduling, 23

D

Daily Oversight and Troubleshooting, 94

G

Glossary, 97

H

HL Optimized (HLO)

Design Highlights, 8

HLO Developer Perspective, 9

Overview and Background, 8

HL7 Overview, 3

HL7 Standard, 4

HLO Management System

Application Registry, 79

Main Menu, 49

Message Viewer, 65

System Monitor, 50

Taskman-Scheduled Options, 79

HLO System Manager Perspective

HLO System Manager Perspective, 10

L

Listener, TaskMan Multi-Threaded, 46

Listener, UCX Multi-Threaded for Open VMS, 30

Listeners, Introduction, 27

Listeners, Multi-Threaded, 29

M

Main Menu, HLO Management System, 49

Message Viewer, HLO Management System, 65

Multi-Threaded Listener for OpenVMS with DSM, Creating, 46

Multi-Threaded Listeners, 29

P

Process Registry, 80

Q

Queries, 6

S

Server Logical Link, Defining, 17

Software Patch, Installing, 12

Standard Listener

Configure Record in HLO System Parameter File, 47

System Monitor, HLO Management System, 50

System Monitor, Start HLO With, 25

SYSTEM PARAMETERS File, Updating, 22

SYSTEM STARTUP Option, Scheduling, 24

T

TaskMan Multi-Threaded Listener, 46

Taskman Multi-Threaded Listner

Set Up the Server Logical Link, 46

Taskman-Scheduled Options

HLO Management System, 79

TCP/IP Connection Requirements, 28

TCP/IP Service

Recommended Naming Conventions, 31

TCP/IP Services

and VistA HLO, 30

for OpenVMS, 30

Requirements for Setting Up on OpenVMS, 30

TCP/IP Services, Creating, 84

Troubleshooting, 95

U

UCX Multi-Threaded Listener for OpenVMS, 30

UCX Multi-Threaded Listener for OpenVMS with Cache, Creating, 33

UCX Multi-Threaded Listener for OpenVMS, Create and Activate, 27

Unsolicited Updates, 5

V

VistA HL7 Package, history of, 6

[^1]: Health Level Seven, *Health Level Seven, Version 2.4.* © 2000, p. D-17.

[^2]: Health Level Seven, *Health Level Seven, Version 2.3.1*, ©1999, p. 2-1.

[^3]: Health Level Seven, *Health Level Seven, Version 2.3.1*, ©1999, p. E-1.

[^4]: Health Level Seven, *Health Level Seven, Version 2.3.1*, ©1999, p. E-2.

[^5]: Health Level Seven, *Health Level Seven, Version 2.3.1*, ©1999, p. E-18.

[^6]: Health Level Seven, *Health Level Seven, Version 2.3.1*, ©1999, p. E-28.