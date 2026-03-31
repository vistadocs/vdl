---
title: HL7 HL*1.6*126 Installation Manual/Release Notes
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
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
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - listener
  - service
  - class
  - cache
  - link
  - span
  - port
  - process
page_count: 0
word_count: 11564
section_count: 32
table_count: 59
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: September 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl_1_6_126_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl_1_6_126_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

![](hl7-hl-1-6-126-installation-manual-release-notes/001.png)

VistA HL7- Optimized (HLO)Supplement toVistA Health Level Seven (HL7)Version 1.6

INSTALLATION MANUAL/RELEASE NOTES

Patch HL\*1.6\*126

September 2005

Revision 1.4

Revision History

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>8/2005</td>
<td>1.0</td>
<td>Initial Draft</td>
</tr>
<tr class="odd">
<td>08/22/2005</td>
<td>1.1</td>
<td>Updated by REDACTED</td>
</tr>
<tr class="even">
<td>08/26/2005</td>
<td>1.2</td>
<td>Updated by Daou Systems, Inc.</td>
</tr>
<tr class="odd">
<td>08/29/2005</td>
<td>1.3</td>
<td>Updated by REDACTED – added patch HL*1.6*118 as a required build</td>
</tr>
<tr class="even">
<td>09/02/2005</td>
<td>1.3</td>
<td>Made a note – Interface Engine will show as ‘NOT OPERATIONAL’ until the HL LOGICAL LINK entry named ‘VA-VIE’ is distributed as another patch.</td>
</tr>
<tr class="odd">
<td>9/6/2005</td>
<td>1.3</td>
<td><p>Warnings added by REDACTED:</p>
<ol type="1">
<li><p>When adding a new listener for HLO, if an already-existing entry in the HL LOGICAL LINK File (#870) is used for an existing listener, don’t alter certain fields.</p></li>
<li><p>Sites running under VMS or Cache should use a multi-listener.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>9/16/2005</td>
<td>1.4</td>
<td><p>Updates by Daou:</p>
<ol type="1">
<li><p>Synchronized Tech Manual install section with this install.</p></li>
<li><p>Added more scenarios and solutions to Trouble-Shooting</p></li>
<li><p>Updated Chapter 2 with new components from distribution from 9/14/2005 AM</p></li>
<li><p>Took out indexing tags as they were mistakenly copied from tech manual, no need for indexing install manual</p></li>
<li><p>Added info about translating globals for DSM and Cache sites</p></li>
<li><p>Reviewed for flow and content</p></li>
</ol></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Patch Revisions

For a complete list of patches related to this software, please refer to the National Patch Module on FORUM.

Comments

Technical Services welcomes your comments on this manual. Please send your comments to:

> REDACTEDTable of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Related Resources](#related-resources)
    - [VistA HL7 Package Homepage](#vista-hl7-package-homepage)
    - [VistA Data Systems and Integration (VDSI) HL7 Homepage](#vista-data-systems-and-integration-vdsi-hl7-homepage)
    - [HL7 Standard Documentation](#hl7-standard-documentation)
  - [Documentation Conventions](#documentation-conventions)
    - [Screen Dialog](#screen-dialog)
    - [Software Processes and Code](#software-processes-and-code)
    - [Documentation Icons](#documentation-icons)
  - [Software Requirements](#software-requirements)
    - [Manuals](#manuals)
    - [Namespace](#namespace)
    - [File Range](#file-range)
    - [Globals](#globals)
    - [Software Dependencies](#software-dependencies)
  - [Staffing](#staffing)
- [New Software Components for HLO](#new-software-components-for-hlo)
  - [Namespace](#namespace-1)
  - [New Routines](#new-routines)
  - [New Routine Categories](#new-routine-categories)
  - [New Files](#new-files)
  - [Modified Files](#modified-files)
  - [New Protocols](#new-protocols)
  - [New List Templates](#new-list-templates)
  - [New Input Templates](#new-input-templates)
  - [Modified Forms](#modified-forms)
  - [New Options](#new-options)
  - [HLO Options Organization](#hlo-options-organization)
    - [HLO System Monitor](#hlo-system-monitor)
    - [HLO Message Viewer](#hlo-message-viewer)
    - [HLO Application Registry](#hlo-application-registry)
  - [Scheduled Options](#scheduled-options)
- [Pre-Installation Checklist](#pre-installation-checklist)
- [HLO Installation and Configuration](#hlo-installation-and-configuration)
  - [Install the HLO Software Patch](#install-the-hlo-software-patch)
  - [Define the Server Logical Link](#define-the-server-logical-link)
  - [Update the HLO SYSTEM PARAMETERS File (#779.1)](#update-the-hlo-system-parameters-file-7791)
  - [Update the HLO PROCESS REGISTRY File (#779.3)](#update-the-hlo-process-registry-file-7793)
  - [Schedule the HLO COUNT RECORDS Option](#schedule-the-hlo-count-records-option)
  - [Schedule the HLO SYSTEM STARTUP Option](#schedule-the-hlo-system-startup-option)
  - [Start HLO using the HLO System Monitor](#start-hlo-using-the-hlo-system-monitor)
  - [Create and Activate the TCP/IP Services for Open VMS](#create-and-activate-the-tcpip-services-for-open-vms)
- [Listeners](#listeners)
  - [Introduction](#introduction-1)
    - [TCP/IP Connection Requirements](#tcpip-connection-requirements)
  - [Multi-Threaded Listeners](#multi-threaded-listeners)
  - [TCP/IP Services for Open VMS](#tcpip-services-for-open-vms)
    - [Introduction](#introduction-2)
    - [TCP/IP Services for OpenVMS](#tcpip-services-for-openvms)
    - [TCP/IP Services and VistA HLO](#tcpip-services-and-vista-hlo)
    - [Requirements for Setting up a TCP/IP Service on OpenVMS](#requirements-for-setting-up-a-tcpip-service-on-openvms)
    - [Recommended Naming Conventions](#recommended-naming-conventions)
    - [Creating a TCP/IP Services for Open VMS with Cache](#creating-a-tcpip-services-for-open-vms-with-cache)
    - [Creating a TCP/IP Service for Open VMS with DSM](#creating-a-tcpip-service-for-open-vms-with-dsm)
  - [TaskMan Multi-Threaded Listener](#taskman-multi-threaded-listener)
    - [Set up the Server Logical Link](#set-up-the-server-logical-link)
    - [Configure the TaskMan Multi-Listener Record in the HLO Process Registry](#configure-the-taskman-multi-listener-record-in-the-hlo-process-registry)
- [Daily Oversight and Troubleshooting](#daily-oversight-and-troubleshooting)
  - [Daily Oversight](#daily-oversight)
    - [HLO System Monitor](#hlo-system-monitor-1)
    - [HLO Message Viewer](#hlo-message-viewer-1)
  - [Troubleshooting](#troubleshooting)
Welcome to the *VistA HLO Installation Manual/ Release Notes*. The goal of this manual is to provide Veterans Health Information Systems and Technology Architecture (VistA) Information Resource Mangers (IRMs) and system managers with descriptions of the components included in patch HL\*1.6\*126 and all of the information needed to install and configure the VistA Health Level 7 Optimized (HLO) software package.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO is a complete rewrite of the current VistA package, HL Version 1.6. It consists of new processes, programs, and FileMan files. The new HLO Process Manager uses a process pooling method which allows a greater number of queues (incoming and outgoing) to run concurrently. New HLO System Monitoring and HLO Message Viewing utilities are designed to provide users with a more straightforward interface for monitoring and management of Health Level 7 (HL7) applications. HLO and HL 1.6 can run simultaneously to allow for a gradual migration to HLO.

## Related Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA HL7 Package Homepage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides the latest information on the VistA HL7 package, including the full documentation set, latest news, and links to other sites:

http://vista.med.va.gov/messaging/hl7

### VistA Data Systems and Integration (VDSI) HL7 Homepage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The web site of the VistA HL7 Messaging Administrator, this provides information on HL7, including the HL7 standard and the VistA HL7 Specification Repository:

<http://vista.med.va.gov/vdsi/>

### HL7 Standard Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The best source of information about the *Health Level Seven* standard is the standard itself. It is available at the VistA HL7 package's homepage and the VDSI homepage, listed above.

For more information about the HL7 body of standards, please see their web site, at:

<http://www.hl7.org/>

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Screen Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual presents snapshots of computer dialogue or other online displays in a non-proportional font. User responses to online prompts are highlighted in bold. Pressing the return key is illustrated as \<RET\>, and is only shown when the user doesn’t type anything at the prompt besides pressing the Return key. For example, the following indicates that the user should enter two question marks followed by \<RET\> when prompted:

> Select Primary Menu option: ??

> Following menu options are available……

> Select Primary Menu option: \<RET\>

### Software Processes and Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Processes are indicated with single quotes.

Code is indicated with double quotes.

### Documentation Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These icons, placed in the left-hand margin, highlight passages in the documentation as follows:

|                                                   |                        |
|---------------------------------------------------|------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/002.png) | Important Information. |
| ![](hl7-hl-1-6-126-installation-manual-release-notes/003.png) | Caution.               |

## Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation is available on the following OI Field Offices' Anonymous Software Directories. Use the appropriate FTP capability to retrieve the files.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 36%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong><u>OI FIELD OFFICE</u></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><u>FTP ADDRESS</u></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><u>DIRECTORY</u></strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALBANY</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HINES</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SALT LAKE</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FIRST AVAILABLE SERVER</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
</tbody>
</table>

The following files are required for installation and implementation.

Host File Names:

hl71_6_p126_ig.doc installation guide - Word format

hl71_6_p126_ig.pdf installation guide - Acrobat format

hl71_6_p126_tm.doc technical manual - Word format

hl71_6_p126_tm.pdf technical manual - Acrobat format

These documents can also be downloaded from the VISTA Documentation

Library (VDL) on the HL7 Web page:

<http://www.va.gov/vdl/Infrastructure.asp?appID=8>

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch has been assigned Routine Namespace HLO.

### File Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch has been assigned file range 777.000-779.999

### Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch defines five new globals as listed in the following table. These globals may need to be created and mapped prior to patch installation depending on storage requirements at the individual site.

Using the appropriate global management utility (i.e. %GLOMAN), create these globals and assign the following global access privileges: System = RWD (or RWP), World = RWD (or RWP), Group = RWD (or RWP) and UCI = RWD (or RWP). This may require assistance from a System Manager.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 36%" />
<col style="width: 29%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Global Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Storage</strong></th>
<th><strong>Journaling</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^HLA</td>
<td>HLO MESSAGE BODY (File# 777)</td>
<td>Potentially large depending on the number of messages the site is sending and receiving.</td>
<td>Journal.</td>
</tr>
<tr class="even">
<td>^HLB</td>
<td>HLO MESSAGES (File# 778)</td>
<td>Potentially large depending on the number of messages the site is sending and receiving.</td>
<td>Journal.</td>
</tr>
<tr class="odd">
<td>^HLC</td>
<td>Temporary global for system counters used by HLO</td>
<td>Defined while HLO software is running. Purged on shutdown/restart of the software. Minimal storage required.</td>
<td>Journal</td>
</tr>
<tr class="even">
<td>^HLD</td>
<td><p>Dictionaries</p>
<p>HLO SYSTEM PARAMETERS (File# 779.1)</p>
<p>HLO APPLICATION REGISTRY (File# 779.2)</p>
<p>HLO PROCESS REGISTRY (File# 779.3)</p>
<p>HLO SUBSCRIPTION REGISTRY (File# 779.4)</p></td>
<td>Installed with HL*1.6*126 patch. Storage not expected to increase significantly after that time.</td>
<td>Journal</td>
</tr>
<tr class="odd">
<td>^HLTMP</td>
<td>Temporary global used for HLO process, message, and other statuses.</td>
<td>Defined while HLO software is running. Purged on shutdown/restart of the software. Minimal storage required.</td>
<td>Journal</td>
</tr>
</tbody>
</table>

### Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before HL\*1.6\*126 can be installed:

- HL\*1.6\*118
- XU\*8\*388

## Staffing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed by an IRM. In addition, sites using the VMS level multi-listener need access to VMS system privileges in order to configure the multi-listener. This may require assistance from a VMS system manager.

Please schedule five minutes for initial KIDS install and about 20-25 minutes for post-installation set up of the package.

# New Software Components for HLO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch has been assigned namespace HL and sub-namespace HLO.

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new routines are included in this software:

| HLMA3    | HLOAPI   | HLOAPI1  | HLOAPI2  | HLOAPI3  | HLOAPP   |
|----------|----------|----------|----------|----------|----------|
| HLOASUB  | HLOASUB1 | HLOCLNT  | HLOCLNT1 | HLOCLNT2 | HLOCLNT3 |
| HLOCNRT  | HLOCVU   | HLOF777  | HLOF778  | HLOF778A | HLOFILER |
| HLOMSG   | HLOMSG1  | HLOPBLD  | HLOPBLD1 | HLOPOST  | HLOPROC  |
| HLOPROC1 | HLOPRS   | HLOPURGE | HLOQUE   | HLOSITE  | HLOSRVR  |
| HLOSRVR1 | HLOT     | HLOTCP   | HLOTLNK  | HLOUSR   | HLOUSR1  |
| HLOUSR2  | HLOUSR3  |          |          |          |          |

## New Routine Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new routines are categorized in the following manner:

HLMA3

\- APIs for HL LOGICAL LINK File (#870)

HLOAPI\*

\- APIs for sending and receiving messages

HLOAPP\*

\- Application registry

HLOASUB\*

\- Subscription registry

HLOCNRT, HLOCVU

\- API’s for converting HL 1.6 applications to HLO

HLOCLNT\*

\- Client process

HLOF\*

\- Filer processes

HLOMSG\*, HLOPBLD\*

\- Parts of API

HLOPRS\*

\- Parsing of incoming messages

HLOPROC\*

\- Process manager

HLOT\*

\- TCP access routines

HLOQUE\*

\- Queue management

HLOSITE\*

\- Site parameters

HLOTLNK\*

\- Logical link

HLOUSR\*

\- System status and message monitor menu screens

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new files are included in this software:

777 (^HLA)

HLO MESSAGE BODY

Contains the body of an HL7 message, which excludes the message header segment. For batch messages, it does not include the individual message header segments or the batch trailer segment.

778 (^HLB)

HLO MESSAGES

Used to record each message as it is sent or received. The content of the message is stored in a file \#777, as it might be sent to multiple locations and applications.

779.1 (^HLD(779.1))

HLO SYSTEM PARAMETERS

This file contains parameters used by the HLO (HL7 Optimized) that are specific to the system the software is installed on.

779.2 (^HLD(779.2))

HLO APPLICATION REGISTRY

This file is used to register sending and receiving applications for HL7 messaging. For receiving applications, the process of registration consists of registering what messages the application is prepared to receive.

For both sending and receiving applications, it is necessary to specify what package the application belongs to. For sending applications, that is the only field that applies, other than the name of the sending application.

An application can be either a sender or a receiver of messages, or both. In order for an application to receive messages, it must specify an action (M tag^routine) for each type of message that it is capable of receiving, or a default action that applies when no message-specific action is defined.

779.3 (^HLD(779.3))

PROCESS REGISTRY

The process registry is used by the HLO process manager to start, stop, and manage all of the processes used by the HLO system.

779.4 (^HLD(779.4))

HLO SUBSCRIPTION REGISTRY

This file is used to store static routing lists for messages.

Static routing lists are lists of recipients that an application may create in advance for its messages. The alternate routing method is dynamic routing, whereby the recipient list is created by the application at the time the message is created.

## Modified Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most files included in this software are new. One existing HL 1.6 file that is also used by HLO is the HL LOGICAL LINK file (#870).

870 (^HLCS)

HL LOGICAL LINK

Two new fields have been added to the HL LOGICAL LINK File (#870). They are:

- DNS DOMAIN (#.08)
- TCP/IP PORT (OPTIMIZED) (#400.08)

Field DOMAIN (#.03) has been renamed to MAILMAN DOMAIN (#.03)

## New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols have been added to the PROTOCOL File (#101) to support the list templates for the System Status and HLO Message monitors. These new protocols are:

| Protocol Name                   | Display Name                 |
|-------------------------------------|----------------------------------|
| HLO APPLICATION ERRORED MESSAGES    | HLO APPLICATION ERRORED MESSAGES |
| HLO BRIEF SYSTEM STATUS             | BRIEF SYSTEM STATUS              |
| HLO DISPLAY OUT-GOING QUEUES        | VIEW QUEUES                      |
| HLO DISPLAY PROCESSES               | VIEW PROCESSES                   |
| HLO DISPLAY SINGLE MESSAGE          | DISPLAY A MESSAGE                |
| HLO DISPLAY SYSTEM ERRORED MESSAGES | SYSTEM ERRORED MESSAGES          |
| HLO DOWN LINKS                      | DOWN LINKS                       |
| HLO INCOMING QUEUES                 | INCOMING QUEUES                  |
| HLO MESSAGE SEARCH                  | MESSAGE SEARCH                   |
| HLO MESSAGE SEARCH MENU             | MESSAGE SEARCH                   |
| HLO MESSAGE VIEWER MENU             | MESSAGE VIEWER MENU              |
| HLO MONITOR MODE                    | MONITOR MODE                     |
| HLO SCROLL MODE                     | SCROLL MODE                      |
| HLO START MENU                      | START HLO                        |
| HLO START/STOP ONE QUEUE            | STRT/STP QUEUE                   |
| HLO STOP SYSTEM                     | STOP HLO                         |
| HLO SYSTEM MONITOR MENU             |                                  |
| HLO TEST LINK                       | TEST LINK                        |
| HLO TRANSMISSION FAILURES           | HLO TRANSMISSION FAILURES        |
| HLO VIEW A LINK                     | VIEW LINK                        |

## New List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list templates are included in this software:

- HLO SYSTEM MONITOR
- HLO MESSAGE VIEWER
- HLO MESSAGE SEARCH
- HLO SINGLE MESSAGE DISPLAY

## New Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One new input template is included in this software:

- HLOAPREG – HLO APPLICATION REGISTRY (File \#779.2) Input Template

## Modified Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One modified form is included in this software:

- HL LOGICAL LINK (File \#870)
  - Added TCP/IP PORT (OPTIMIZED) Field \#400.08
  - Added DNS DOMAIN Field \#.08

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are included in this software:

HLO APPLICATION REGISTRY

This option allows the user to register an HL7 (Optimized) application in the Application Registry File (779.2).

HLO COUNT RECORDS

This option will run daily on off-hours to count records in files 777 & 778.

HLO MAIN MENU

This menu contains all the options developed for HLO.

HLO MESSAGE VIEWER

This option is for viewing messages. It is a ListManager interface that provides a variety of methods for selecting messages for viewing.

HLO SYSTEM MONITOR

This option is for IRM staff to monitor the operational aspects of HLO.

HLO SYSTEM STARTUP

This option should be scheduled upon system startup to start HLO running.

## HLO Options Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new HLO options are organized as described in the following menu structures:

HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

SM HLO SYSTEM MONITOR

MV HLO MESSAGE VIEWER

APPS HLO APPLICATION REGISTRY

### HLO System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- LIST PROCESSES
- DOWN LINKS
- OUTGOING QUEUES
- INCOMING QUEUES
- BRIEF STATUS
- MONITOR LINK
- STOP HLO
- START HLO
- TEST TCP LINK
- RealTime Mode
- Scroll Mode
- STRT/STP QUE

### HLO Message Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- DISPLAY MSG
- SYSTEM ERRORS
- APPLICATION ERRORS
- TRANSMISSION FAILURES
- MESSAGE SEARCH

### HLO Application Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: There are no submenu options under this option.

## Scheduled Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These options should be scheduled in TaskMan after installation of the HL\*1.6\*126 patch. Further instructions on how to schedule these options can be found in Sections 4.5 and 4.6 of this document.

- HLO COUNT RECORDS
- HLO SYSTEM STARTUP

# Pre-Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Decide what type of listener to use. If running under VMS, the most efficient listener is the TCP/IP Service for OpenVMS. The TCP/IP Service for OpenVMS requires a TCP/IP port number. The port officially assigned to HLO is 5001 for production systems and 5026 for test systems
2.  There should be enough available TaskMan sub-processes to run HLO. Most installations need at least four defined.
3.  Read and understand the installation instructions.
4.  TCP/IP Service for OpenVMS Setup:
- Do you have VMS system privileges?
5.  Have you installed patches XU\*8.0\* 388, HL\*1.6\*84, and HL\*1.6\*118? These are required builds.

# HLO Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch HL\*1.6\*126 contains all of the components needed to support HLO and was created using the Kernel Installation and Distribution System (KIDS). Please review the KIDS documentation patch description, and familiarize yourself with KIDS prior to installing this package.

ALWAYS back up your system prior to loading any software.

To correctly install HLO and configure it for proper development and usage:

VistA Steps:

1)  Install the HLO Software Patch, HL\*1.6\*126.
2)  Define the Server Logical Link.
3)  Update the HLO SYSTEM PARAMETERS File (#779.1).
4)  Update the HLO PROCESS REGISTRY File (#779.3).
5)  Schedule the HLO COUNT RECORDS Option.
6)  Schedule the HLO SYSTEM STARTUP Option.
7)  Start HLO using the HLO System Monitor.

VMS Step:

8)  Create and activate the TCP/IP Services for OpenVMS.

|                                                   |                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/004.png) | WARNING: Incoming messages and application acknowledgements are dependent upon the TCP/IP Services for OpenVMS being defined and active. |

## Install the HLO Software Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO package arrives as a standard KIDS Build. It will install the following elements:

1)  New fields in the HL LOGICAL LINK File (#870). TCP/IP PORT (OPTIMIZED) (field \#400.08) and DNS DOMAIN (field \#.08) are added.
2)  New files, HLO MESSAGE BODY (#777) and HLO MESSAGES (#778), for holding messages.
3)  A new file, HLO SYSTEM PARAMETERS (#779.1), which contains system parameters specific to the installing site.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/005.png)</td>
<td><p><strong>A Note about System Parameters</strong></p>
<p>The System Parameters are automatically configured as part of the installation. However, if it becomes necessary to modify them, they can be accessed in the HLO SYSTEM PARAMETERS File (#779.1). The key fields are:</p>
<ul>
<li><p>Domain Name – The domain name of your system.</p></li>
<li><p>Station Number – A number which uniquely identifies your site from others.</p></li>
</ul></td>
</tr>
</tbody>
</table>

4)  A new file, HLO APPLICATION REGISTRY (#779.2), which contains information for both sending and receiving applications.
5)  A new file, HLO PROCESS REGISTRY (#779.3), which contains information on HLO processes. This file will arrive configured and should not be modified except for adding links and activating listeners.
6)  A new file, HLO SUBSCRIPTION REGISTRY (#779.4). This file is very similar to file HL7 SUBSCRIPTION REGISTRY (#774), with the exception that it contains subscriptions in format appropriate to the HLO package.
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

Enter options you wish to mark as 'Out Of Order':\<RET\>

Enter protocols you wish to mark as 'Out Of Order':\<RET\>

Delay Install (Minutes): (0-60): 0//:\<RET\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<RET\>

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

|                                                   |                                                                                                                                                                                                                              |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/006.png) | WARNING: As part of HLO configuration, DSM sites should check the settings of all global max string lengths. They should be set to the maximum of 512. This enables HLO to read and process long HL7 segments correctly. |

|                                                   |                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/007.png) | WARNING: Error trap displays of extremely long variables may be limited to 255 characters and may be truncated under certain versions of M. |

## Define the Server Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO requires a Server Logical Link for receiving messages. If HLO (either server or client) is using the same link as HL 1.6, the only requirements are to define the TCP/IP PORT (OPTIMIZED) and the DNS DOMAIN fields for that link and to verify that all other elements are properly defined for HLO. If this is not possible, a new link must be created.

The default port number for the HLO Server Logical Link (listener) is 5001 for production systems and 5026 for main test systems. If port number 5001 is already in use by another listener, that listener must be re-assigned to a new port number.

|                                                   |                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/008.png) | The HL7 1.6 listener and the HLO listener can use the same HL Logical Link entry, but cannot use the same port number. If re-using an existing HL7 1.6 entry with HLO, do not delete or modify any of the existing fields. The HL7 1.6 listener still uses them even if the HLO listener does not. |

The preferred listener method for running HLO is the TCP/IP Services for Open VMS. It is unlikely that more than one listener will be needed. However, HLO is capable of serving several listeners at the same time.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/009.png)</td>
<td><p><u>Multi-Listener vs. Single Listener</u> –</p>
<p><strong>IRM staffs initially installing HLO</strong>: If your system is a VMS or Cache system, use a multi-listener! If your system is VMS, the multi-listener should run under VMS TCP. If it is not VMS, but is Cache, you should set up a TaskMan multi-listener. Only if your system is neither VMS nor Cache should you set up a single listener.</p>
<p><strong>Application Developers</strong>: Normally, your application should use the site’s standard listener. If you must create your own listener (highly discouraged), if only one connection request will be created at a time and the interfacing application requires its own server, then a single listener would be applicable. Otherwise, if there is a possibility of multiple connection requests, then the multi-listener is appropriate.</p></td>
</tr>
</tbody>
</table>

For more details on setting up listeners, please refer to the next chapter, “Listeners.”

|                                                   |                                                                                                                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/010.png) | WARNING –The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS. For any system required to use the TaskMan Multi-Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first. |

To create or edit a server Logical Link definition, use the *Link Edit* option on the HL7 Interface Developer Options menu:

Select Interface Developer Options Option: Link Edit

Select HL LOGICAL LINK NODE: VABAY

To edit the TCP/IP server level parameters, tab down to the LLP Type field (in the *Link Edit* option) and press \<RET\> to display a form to edit the field’s specific to the LLP type of the selected Link:

HL7 LOGICAL LINK

-------------------------------------------------------

NODE: VABAY

INSTITUTION: REDACTED

MAILMAN DOMAIN: REDACTED

AUTOSTART: *\*\*see below*

QUEUE SIZE: *\*\*see below*

<span class="mark">LLP TYPE: TCP \<RET\></span>

<span class="mark">DNS DOMAIN:</span> redacted

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/011.png)</td>
<td><ul>
<li><blockquote>
<p>Production system’s domain name should be registered on the VHA DNS Domain server. If not currently registered, sites should do this as soon as possible.</p>
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

│ VABAY │

│ │

│ TCP/IP SERVICE TYPE: <span class="mark">MULTI LISTENER</span> │

│ TCP/IP ADDRESS: <span class="mark">152.199.199.199</span> │

│ TCP/IP PORT: *\*\* see below* │

│ TCP/IP PORT (OPTIMIZED): <span class="mark">5001</span> │

│ │

│ ACK TIMEOUT: *\*\*see below* RE-TRANSMISION ATTEMPTS: \*\see below* │

│ READ TIMEOUT: *\*\*see below* EXCEED RE-TRANSMIT ACTION: *\*\*see below* │

│ BLOCK SIZE: │

│ │

│STARTUP NODE: *\*\*see below* PERSISTENT: YES │

<u>│ RETENTION: *\*\*see below*</u> <u>UNI-DIRECTIONAL WAIT: │</u>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

|                                                   |                                                                                                                                                                                                                                                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/012.png) | WARNING – Please make sure that the *TCP/IP PORT (OPTIMIZED)* field is used and not the *TCP/IP PORT* field. All VistA sites must use Port \#5001 for the HLO Standard Listener for production systems. For test accounts Port \#5026 must be used. |

|                                                   |                                                                                                                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/013.png) | \*\* WARNING: If the existing HL Logical Link for the HL7 1.6 listener is reused for HLO, DO NOT modify or delete any of the fields marked above (\*\*see below)! Even though HLO does not use them, HL7 1.6 does. |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/014.png)</td>
<td><p>Please contact the site IRM to obtain the specific domain name and port number to be used by the client side communicating with VistA. For example, at many sites the HL 1.6 multi-listener uses HL7.SITENAME.MED.VA.GOV with port 5000.</p>
<p>Currently, HLO uses the same domain name with port 5001 on production systems and 5026 on test systems.</p>
<p>If a site has more than one test system, it may use additional port numbers.</p></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/015.png) | Start/Stop Link – For HLO processing the server and client HL Logical Link entries DO NOT need to be started or stopped via the HL 1.6 Start/Stop links option as currently done. The links must be defined with the specific HLO fields (DNS Domain and TCP/IP Port (Optimized)) and HLO System started for the link to be available for receiving or transmitting messages. However, if the link must continue to process applications for the existing HL 1.6 messaging engine as well as HLO, then the link still needs to be started as before. |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/016.png)</td>
<td><p>Please obtain the specific domain name and port number to be used by the client side communicating with VistA.</p>
<p>For example, at many sites the HL 1.6 multi-listener uses: HL7.SITENAME.MED.VA.GOV with port 5000.</p>
<p>Currently, HLO uses the same domain name with port 5001 on production systems and 5026 on test systems.</p>
<p>If a site has more than one test system, additional port numbers may be used.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/017.png)</td>
<td><ul>
<li><p>The port number you select must be an available TCP/IP port number. The port number will also be used in the configuration and naming of the TCP/IP service described in the following sections.</p></li>
<li><p>The port numbers recommended in this chapter, 5001 for production, 5026 for test, have been registered for use by VistA HLO. Everything should be done to free port 5001 for use by HLO.</p></li>
<li><p>If the HLO multi-listener is to be used by an application at the national level and you are not using port number 5001, you must register the port number with the DBIA manager on Forum.</p></li>
</ul></td>
</tr>
</tbody>
</table>

For configuring client logical links please refer to Section 6.2 of the HLO Technical Manual

## Update the HLO SYSTEM PARAMETERS File (#779.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the HLO System Monitor screen, the Standard Listener is used to monitor the primary server link (or “listener”) for HLO. In most instances, this is the only listener that is configured. In order for the Standard Listener status to function properly, the name of the link must be added to the HLO STANDARD LISTENER field in the HLO SYSTEM PARAMETERS File (#779.1). This must be done using FileMan, as shown below.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/018.png)</td>
<td><p><strong>A Note about System Parameters</strong></p>
<p>The System Parameters are automatically configured as part of the installation. However, if it becomes necessary to modify them, they can be accessed in the HLO SYSTEM PARAMETERS File (#779.1). The key fields are:</p>
<ul>
<li><p>Domain Name – The domain name of your system.</p></li>
<li><p>Station Number – A number which uniquely identifies your site from others.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: //HLO SYSTEM PARAMETERS

EDIT WHICH FIELD: ALL// HLO STANDARD LISTENER

THEN EDIT FIELD: \<RET\>

Select HLO SYSTEM PARAMETERS DOMAIN NAME: HL7.VAABC.MED.VA.GOV *<span class="mark">This is the DNS domain name for this system (VAABC.MED.VA.GOV). Also, there will always be only one entry in the HLO System Parameters file and its IEN is 1.</span>*

HLO STANDARD LISTENER: VABAY *<span class="mark">This is the name of the entry in the HL LOGICAL LINK File (#870) that is the default listener to which most remote applications will send messages, as shown above</span>*

Select HLO SYSTEM PARAMETERS DOMAIN NAME: \<RET\>

Select OPTION: \<RET\>

VAH\>

## Update the HLO PROCESS REGISTRY File (#779.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields need to be updated in the HLO PROCESS REGISTRY File (#779.3) for the site’s HLO Standard Listener process (for most sites this is the VMS TCP Listener):

- ACTIVE Field (#.02) – Set to “YES”
- DEDICATED LINK Field (#.14) – Site’s listener link (HL Logical Link record defined in Section 4.2)

The following table summarizes recommendations for the HLO PROCESS REGISTRY entry to activate as the HLO Standard Listener.

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SYSTEM TYPE</strong></th>
<th><strong>HLO PROCESS REGISTRY ENTRY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Cache on OpenVMS</p>
<p>DSM on Open VMS</p></td>
<td>VMS TCP LISTENER</td>
</tr>
<tr class="even">
<td><p>Cache on NT</p>
<p>Other M systems</p></td>
<td>TASKMAN MULTI-LISTENER</td>
</tr>
<tr class="odd">
<td>COTS interfaces unable to use a multi-listener</td>
<td>SINGLE LISTENER</td>
</tr>
</tbody>
</table>

Select HLO PROCESS REGISTRY PROCESS NAME: <span class="mark">VMS TCP LISTENER</span>

PROCESS NAME: VMS TCP LISTENER// \<RET\>

<span class="mark">ACTIVE: NO// YES</span>

MINIMUM ACTIVE PROCESSES: 1// \<RET\>

MAXIMUM ACTIVE PROCESSES: 1// \<RET\>

SCHEDULING FREQUENCY (minutes): 9999// \<RET\>

DT/TM LAST STARTED OR STOPPED: \<RET\>

HANG TIME (seconds): 1// \<RET\>

GET WORK FUNCTION (TAG): // \<RET\>

GET WORK FUNCTION (ROUTINE): // \<RET\>

DO WORK FUNCTION (TAG): \<RET\>

DO WORK FUNCTION (ROUTINE): \<RET\>

MAX TRIES FINDING WORK: 0// \<RET\>

PERSISTENT: NO// \<RET\>

<span class="mark">DEDICATED LINK: VABAY</span> *This is the name of the entry in the HL LOGICAL LINK File (#870) that is the default listener to which most remote applications will send messages, as shown above*

VMS TCP SERVICE: YES// \<RET\>

Select HLO PROCESS REGISTRY PROCESS NAME: \<RET\>

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

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

## Schedule the HLO SYSTEM STARTUP Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO SYSTEM STARTUP option should be scheduled after installing and configuring HLO. Once this option is scheduled, HLO starts automatically at system startup. This option can be scheduled from the TaskMan Management Menu.

|                                                   |                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/019.png) | WARNING – Not scheduling this option requires the IRM to start HLO manually from the HLO System Monitor. |

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

Option Name: HLO SYSTEM STARTUP

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

To start HLO, select the START HLO action protocol from the HLO System Monitor. Please refer to Section 5.2 of the HLO Technical Manual for more detailed instructions.

HLO SYSTEM MONITOR Aug 26, 2005@09:40:25 Page: 1 of 1

Brief Operational Overview

SYSTEM STATUS: STOPPED

PROCESS MANAGER: STOPPED

STANDARD LISTENER: NOT OPERATIONAL

INTERFACE ENGINE: NOT OPERATIONAL

TASKMAN: RUNNING

DOWN LINKS: 0

CLIENT LINK PROCESSES: 0

IN-FILER PROCESSES: 0

MESSAGES PENDING TRANSMISSION: 0

STOPPED OUTGOING QUEUES:

MESSAGES PENDING ON APPLICATIONS: 0

STOPPED INCOMING QUEUES:

FILE 777 RECORD COUNT: 7 --\> as of Aug 14, 2005@07:53:01

FILE 778 RECORD COUNT: 7 --\> as of Aug 14, 2005@07:53:01

Brief System Status

LP LIST PROCESSES BS BRIEF STATUS TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK RT RealTime Mode

OQ OUTGOING QUEUES STOP HLO SM Scroll Mode

IQ INCOMING QUEUES START HLO SQ STRT/STP QUE

Select Action:Quit// START START HLO

After start up of HLO, the following should be verified:

- SYSTEM STATUS is RUNNING.
- PROCESS MANAGER is RUNNING.
- STANDARD LISTENER will still be NOT OPERATIONAL until TCP Service is created and enabled, see 4.8 below.
- INTERFACE ENGINE is OPERATIONAL, if the Interface Engine is used.
- TASKMAN is RUNNING.

## Create and Activate the TCP/IP Services for Open VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the next chapter ‘Listeners’ for information on configuring the TCP/IP Services for Open VMS.

|                                                   |                                                                                                                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/020.png) | WARNING –The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS. For any system required to use the TaskMan Multi-Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first. |

# Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO uses TCP/IP listeners to "listen" on a particular port for incoming TCP/IP connections from other systems. Listeners are necessary so that other systems may initiate a connection to this VistA system over TCP/IP.

Client and Server Roles in HLO over TCP/IP

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

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/021.png)</td>
<td><ul>
<li><p>One Single Listener server process is currently provided in the HLO software. However, configuration of multiple Single Listeners is NOT supported by HLO at this time.</p></li>
<li><p>Applications that require a dedicated Single Listener should continue to use the original HL 1.6 implementation. A subsequent HLO patch is being developed for a future release that provides full support of multiple Single Listeners and additional Multi-Threaded Listeners.</p></li>
<li><p>When trying to decide between a single listener and a multi-listener, if only one connection request will be created at a time and the interfacing application requires its own server, then a single listener would be applicable. Otherwise, if there is a possibility of multiple connection requests, then the multi-listener is appropriate.</p></li>
<li><p>The remainder of this chapter will focus on the two types of Multi-Threaded Listener.</p></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/022.png) | HLO highly recommends use of the TCP/IP Services for Open VMS. However, sites NOT on the OpenVMS platform will be required to use the TaskMan Multi-Threaded Listener. |

To reference additional information on listener configuration, please refer to the following documents in the VistA Documentation Library:

- User Manual: TCP/IP Supplement – HL\*1.6\*19 (January 1999)
- Site Manager & Developer Manual – HL\*1.6\*56 (December 1999)

## Multi-Threaded Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-threaded listeners are useful when multiple connection requests come to a single port from many devices or systems. Because multi-threaded listeners spawn off separate handlers for each client connection request, they enable multiple concurrent connections.

> VistA HL7 supports two types of multi-threaded listeners:

- TCP/IP Services for Open VMS (for DSM or Cache)
- TaskMan Multi-Threaded Listener

## TCP/IP Services for Open VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](hl7-hl-1-6-126-installation-manual-release-notes/023.png) | Sections 5.3.1 through 5.3.5 are for both Cache on OpenVMS and DSM on Open VMS. 5.3.6 is for Cache users only and 5.3 7 is for DSM users only |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-Listeners using TCP/IP Services for Open VMS for Cache/DSM sites were introduced in patch HL\*1.6\*84. This chapter documents the setup for creating multi-listeners for HLO using TCP/IP Services for OpenVMS. It assumes that a DCL command file for HL7 1.6 already exists and can be copied as the starting basis for the new HLO service.

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

|                                                   |                                                                                                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/024.png) | The person implementing the instructions in this document must have OpenVMS system administrator privileges to create the above components and be familiar with the OpenVMS TCP/IP Services Management Control Program. |

### Recommended Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following names are used in the description for creating a TCP/IP service and are referenced throughout this chapter. All these names are suggestions. Your site might already have its own naming convention:

- HLSEVEN ― OpenVMS user account name for an HLO TCP/IP service.
- \[HLSEVEN\] ― Name of home directory for the above HLSEVEN user.
- HLSEVEN ― Name of the owner.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](hl7-hl-1-6-126-installation-manual-release-notes/025.png)</th>
<th><ul>
<li><p>Sites that have previously established a VMS user account for HL7 1.6 may reuse the same account for HLO, i.e., another VMS account need not be created.</p></li>
<li><p>The same user name, HLSEVEN, is recommended for HL7 prior to the release of HLO.</p></li>
<li><p>However, a new TCP/IP service command procedure specific for HLO must be created and placed in the same home directory as the old HL7 1.6 TCP/IP service.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- HLS\<port\>\<M environment\>.COM― Name of DCL command procedure, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual VistA M environment. For example:
  - HLS5001DSM.COM― represents the command procedure for a TCP/IP service listening on port 5001 (production systems) that starts up a DSM HLO listener process.
  - HLS5001CACHE.COM― represents the command procedure for a TCP/IP service listening on port 5001 (production systems) that starts up a CACHE HLO listener process.
  - HLS5026DSM.COM― represents the command procedure for a TCP/IP service listening on port 5026 (test systems) that starts up a DSM HLO listener process.
  - HLS5026CACHE.COM― represents the command procedure for a TCP/IP service listening on port 5026 (test systems) that starts up a CACHE HLO listener process.
- HLS\<port\>\<M environment\>― Name of a TCP/IP service, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual VistA M environment. For example:
  - HLS5001DSM― represents the TCP/IP service listening on port 5001 that starts up a DSM HLO listener process.
  - HLS5001CACHE― represents the TCP/IP service listening on port 5001 that starts up a CACHE HLO listener process.
  - HLS5026DSM― represents the TCP/IP service listening on port 5026 (test systems) that starts up a DSM HLO listener process.
  - HLS5261CACHE― represents the TCP/IP service listening on port 5026 (test systems) that starts up a CACHE HLO listener process.

|                                                   |                                                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/026.png) | WARNING – The TCP/IP PORT (OPTIMIZED) field value for the DEDICATED LINK assigned to the VMS TCP LISTENER process must match the Port Number associated with the VMS TCP/IP service. |

![](hl7-hl-1-6-126-installation-manual-release-notes/027.png)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/028.png)</td>
<td><ul>
<li><p>More than one TCP/IP service for HLO may be set up, although it is not necessary to do this. To set up more than one TCP/IP service for HLO, follow the steps in this document for each listener. However, a different command file name, TCP/IP service name, and port number must be defined for each listener.</p></li>
<li><p>Optionally, different user accounts and directories may be specified for each listener.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Creating a TCP/IP Services for Open VMS with Cache

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General steps for creating a TCP/IP Services for Open VMS with Cache are as follows:

1.  Create an OpenVMS User Account (If a user account already exists for HL7 1.6, use the same user account and home directory.)
2.  Create an OpenVMS Home Directory (If a user account already exists for HL7 1.6, use the same user account and home directory.)
3.  Create a DCL Command Procedure
4.  Set up the TCP/IP Service
5.  Enable and Save the TCP/IP Service
6.  Control the Number of Log Files Created by TCP/IP Services
7.  Other TCP/IP Service Commands

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/029.png)</td>
<td><p><strong>Note for Multi-Node Cluster Sites:</strong></p>
<p>For sites configured with a multi-node cluster, more than one node may be advertised under the domain name HL7.SITENAME.MED.VA.GOV and the TCP/IP service may be running on multiple nodes.</p>
<p>In addition, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process to remain uninterrupted if the TCP/IP service is enabled on all nodes in the cluster.</p>
<p>If this is the case for your site, be sure to enable the service on all these nodes, after setting up the TCP/IP service and COM file on one of these nodes.</p></td>
</tr>
</tbody>
</table>

#### Create an OpenVMS User Account

To create an OpenVMS User Account:

1.  If an account already exists for HL7 1.6, use the same user account. Review the settings for that user account to insure conformance to the screen below, then skip to Section 5.3.6.3, “Create a DCL Command Procedure.”
2.  Determine an unused User Identification Code (UIC), typically in the same group as other Cache for OpenVMS accounts.
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

#### Create an OpenVMS Home Directory

If a home directory already exists for HL7 1.6, then use the same home directory. Skip to Section 5.3.6.3, “Create a DCL Command Procedure.”

This directory will house the DCL command procedure, which is executed whenever a client connects. A log file is created for every instance of a connection for that listener. Make sure that the owner of the directory is the HLSEVEN account.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

\$ CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

#### Create a DCL Command Procedure

Create a DCL command procedure (shown below) in the home directory for the HLSEVEN user account and name it according to the recommended convention. Make sure the command procedure file is owned by the HLSEVEN user account.

1.  To create a DCL command procedure that will use a given port, for port 5001, name your command procedure file as HLS5001CACHE.COM.
2.  Adjust the Cache command line (Cache configuration, UCI, and volume set) for your system.
3.  Ensure that the name of the DCL command file, as described in step 1, matches the port assignment. For example, if you changed the port number from 5001 to 6788, rename your HLS5001CACHE.COM file to HLS6788CACHE.COM.

|                                                   |                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/030.png) | WARNING – All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts Port \#5026 must be used. |

Before creating the Command Procedure file determine the proper Cache configuration to use for the environment where you want to start your listener. To do that, use command “CCONTROL LIST” and it will list all Cache configurations that are defined. The Cache configuration you will most likely need is the one marked as (default).

If you are not running a cluster or if the listener is to run on only a single node of the cluster, you can use the name of that default Cache configuration as the first parameter to the ‘CSESSION’ command.

If you are running a cluster and the listener is to run on multiple nodes of that cluster, then you need to make sure that the DCL Command Procedure file can resolve the proper name of the default Cache configuration on each node of the cluster where it is to run. Keep in mind that same DCL command file has to work on each participating node.

On most VistA systems, the name of the Cache configuration will be the same as the name of the node, or perhaps a derivative of the name of the node. So, if the node is 74A01, the configuration will be 74A01 or maybe BRX74A01. In those cases, the DCL Command Procedure file will need to use ‘F\$GETSYS(“NODENAME”)’ to obtain the node name or BRX’F\$GETSYS(“NODENAME”) to obtain the node name and put “BRX” in front of it.

For your convenience, you can cut and paste the following DCL command procedure file into your OpenVMS HLSEVEN device and directory.

Sample DCL Command Procedure file:

\$! HLS5001CACHE.COM - for incoming tcp connect requests with port=5001 and

\$! using "Cache" command line to enter the M environment

\$! File name HLS5001CACHE.COM is recommended to be changed to reflect the

\$! change of the TCPIP port number. For example, file name could be

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

After creating/editing the command file, run the following command and make sure that the “Owner:” field matches the user account which will be running the command file. (In our examples that is 'HLSEVEN' as shown.)

\$ dir/full hls5001cache.com

Directory DKC0:\[USER.HLSEVEN\]

hls5001cache.com;1 File ID: (13869,1,0)

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

hls5001cache.com;1 File ID: (13868,1,0)

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

\$ dir/owner hls5001cache.com

Directory DKC0:\[USER.HLSEVEN\]

hls5001cache.com;1 \[USERS,HLSEVEN\]

Total of 1 files.

#### Set up the TCP/IP Service

To create the TCP/IP service to listen for connections:

1.  Choose the OpenVMS node where you want to run the TCP/IP service listener. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener.
2.  Use TCP/IP port number 5001 for production systems and 5026 for main test systems.

|                                                   |                                                                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/031.png) | WARNING – All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts, Port \#5026 must be used. |

- Use user account HLSEVEN.
- Use DCL command file name HLS5001CACHE.COM.

|                                                   |                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/032.png) | Since TCP/IP Services are node specific, make sure to set up the listener on the same node on which it will be running. |

Ensure that your new TCP/IP service uses the recommended naming convention. For example, to set up a service that will be listening on port 5001 and use a corresponding DCL command file HLS5001CACHE.COM.

Set the service name as HLS5001CACHE as follows:\$ TCPIP (must use continuation character "-" at end of long lines)

TCPIP\> SET SERVICE HLS5001CACHE/USER=HLSEVEN/PROC=HLS5001CACHE/PORT=-

\_TCPIP\> 5001/PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> <span class="mark">/LIMIT=50/</span>FILE=USER\$:\[HLSEVEN\]HLS5001CACHE.COM/INACTIVITY=1

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/033.png) | In this command, <span class="mark">/LIMIT=50</span> specifies the maximum number of TCP/IP connections that can be made at any time. The limit of 50 is appropriate for most local sites, but for systems that serve as national databases the limit should be set initially to 500. The system manager is responsible for monitoring the peak number of connections made, and if the peak approaches the limit, the limit should be increased. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/034.png)</td>
<td><p>If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.</p>
<blockquote>
<p>TCPIP&gt; <strong>SET CONFIG ENABLE NOSERVICE HLS5001CACHE</strong></p>
<p>TCPIP&gt; <strong>SET NOSERVICE HLS5001CACHE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

TCPIP\> SHO SERVICE HLS5001CACHE/FULL

Service: HLS5001CACHE

State: Disabled

Port: 5001 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5001CACHE

#### Enable and Save the TCP/IP Service

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCPIP\> ENABLE SERVICE HLS5001CACHE *<span class="mark">(enable service immediately)</span>*

TCPIP\> SET CONFIG ENABLE SERVICE HLS5001CACHE *<span class="mark">(save service for reboot)</span>*

TCPIP\> SHO SERVICE/FULL HLS5001CACHE

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

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, <span class="mark">HLS5001CACHE</span>, MPI, TELNET, XMINETMM

TCPIP\> EXIT

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/035.png)</td>
<td><p><strong>Note for Multi-Node Cluster Sites:</strong></p>
<p>For sites configured with a multi-node cluster, more than one node may be advertised under the domain name HL7.SITENAME.MED.VA.GOV and the TCP/IP service may be running on multiple nodes.</p>
<p>In addition, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process to remain uninterrupted if the TCP/IP service is enabled on all nodes in the cluster.</p>
<p>If this is the case for your site, be sure to enable the service on all these nodes, after setting up the TCP/IP service and COM file on one of these nodes.</p></td>
</tr>
</tbody>
</table>

#### Control the Number of Log Files Created by TCP/IP Services

The HLS5001CACHE TCP/IP service automatically creates log files (TCP/IP services does this and it cannot be prevented) in the HLSEVEN directory named HLS5001CACHE.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME USER\$:\[HLSEVEN\]HLS5001CACHE.LOG; USER\$:\[HLSEVEN\]HLS5001CACHE.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 USER\$:\[HLSEVEN\]HLS5001CACHE.LOG;

|                                                   |                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/036.png) | This cannot be done until the first log file has actually been created. |

You probably should not limit the number of versions of the log file until you know that your HLS5001CACHE service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

#### Other TCP/IP Service Commands

|                                                   |                                                                                                                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/037.png) | WARNING – If HLO is stopped or disabled for two hours or more, the VMS Multi-Listener service should be disabled and then re-enabled before restarting HLO. |

The definition of a link is required for the multi-threaded listener for Open VMS systems. This link never needs to be started or stopped through the VistA HL 1.6 or HLO options. Instead, it is normally started and stopped via TCP/IP services. For example:

TCPIP\> DISABLE SERVICE HLS5001CACHE *(Stop* TCP/IP *service)*

TCPIP\> ENABLE SERVICE HLS5001CACHE *(Start* TCP/IP *service)*

Any questions about configuring TCP/IP Service for OpenVMS should be directed to EVS for assistance.

### Creating a TCP/IP Service for Open VMS with DSM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General steps for creating a TCP/IP Services for Open VMS with DSM are as follows:

(For more detailed information on creating a TCP/IP Services for Open VMS with DSM, please refer to Appendix F in the HLO Technical Manual.)

1.  Create an OpenVMS User Account (If an account already exists for HL7 1.6, use the same user and home directory.)
2.  Create an OpenVMS Home Directory (If an account already exists for HL7 1.6, use the same user and home directory.)
3.  Create a DCL Command Procedure
4.  Set up the TCP/IP Service
5.  Enable and Save the TCP/IP Service
6.  Resolve Access Control List (ACL) Issues
7.  Control the Number of Log Files Created by TCP/IP Services
8.  Other TCP/IP Service Commands

## TaskMan Multi-Threaded Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration of the TaskMan Multi-Threaded listener involves the following steps:

1.  Set up the server logical link in the HL LOGICAL LINK File (#870). This step may have been done already. If that is the case, proceed to the next step.
2.  Configure the TASKMAN MULTI-LISTENER record in the HLO PROCESS REGISTRY File (#779.3):
    1.  Assign the server logical link name (defined in step \#1) to the DEDICATED LINK field.
    2.  Set the ACTIVE field to “YES.”

|                                                   |                                                                                                                                                                                                                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/038.png) | WARNING –The TaskMan Multi-Listener should NOT be used on systems running Cache under OpenVMS. For any system required to use the TaskMan Multi-Threaded Listener (such as those running Cache under NT), patch XU\*8.0\*388 must be installed first. |

|                                                   |                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/039.png) | Please contact the site IRM to obtain the specific domain name and port number to be used by the client side communicating with VistA. For example, at many sites the HL 1.6 multi-listener uses HL7.SITENAME.MED.VA.GOV with port 5000. Currently, HLO uses the same domain name with port 5001 on production systems and 5026 on test systems. |

|                                                   |                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/040.png) | REMINDER: TaskMan must be running for the TaskMan Multi-Threaded Listener to function. |

### Set up the Server Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistA HL LOGICAL LINK File (#870), create an entry for the Multi-Threaded Listener with the fields populated as follows. If more assistance is required for defining the HL Logical Link, please refer to the section ‘Define the Server Logical Link’ of the chapter ‘HLO Installation and Configuration’ for more specific instructions.

Link Settings for the TaskMan Multi-Threaded Listener in the Logical Link File (#870)

|                         |                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| Field               | Description                                                                                                     |
| LLP TYPE                | Set to ‘TCP’                                                                                                        |
| TCP/IP SERVICE TYPE     | Set to ‘MULTI LISTENER’                                                                                             |
| TCP/IP ADDRESS          | IP Address for your server                                                                                          |
| TCP/IP PORT (OPTIMIZED) | Port to listen on, e.g., 5001 for production systems and 5026 for test systems (make note of the exact port number) |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-126-installation-manual-release-notes/041.png)</td>
<td><ul>
<li><p>The port number you select must be an available TCP/IP port number. The port number will also be used in the configuration and naming of the TCP/IP service described in the following sections.</p></li>
<li><p>The port numbers recommended in this chapter, 5001 for production and 5026 for test, are registered for use by VistA HLO. Everything should be done to free port 5001 or 5026 for use by HLO.</p></li>
<li><p>If the HLO multi-listener is to be used by an application at the national level and you are not using port number 5001 for production, you must register the port number with the DBIA manager on Forum.</p></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/042.png) | WARNING – All VistA sites must use Port \#5001 for the HLO Standard Listener for production accounts. For test accounts, Port \#5026 must be used. |

|                                                   |                                                                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/043.png) | If the TCP/IP Address is not defined, it is resolved automatically by the VHA DNS Domain server. If the system’s domain is NOT registered in the VHA DNS server, the IP address should be defined. |

For configuring client logical links please refer to Section 6.2 of the HLO Technical Manual.

### Configure the TaskMan Multi-Listener Record in the HLO Process Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Logical Link name defined in Section 5.4.1 must be added to the DEDICATED LINK field (#.14) in the VMS TCP Listener Process entry of the HLO PROCESS REGISTRY File (#779.3). The ACTIVE field (#.02) should also be checked to make sure that it is set to “YES.”

Select HLO PROCESS REGISTRY PROCESS NAME: <span class="mark">TASKMAN MULTI LISTENER</span>

PROCESS NAME: TASKMAN MULTI LISTENER// \<RET\>

<span class="mark">ACTIVE: NO// YES\<RET\></span>

MINIMUM ACTIVE PROCESSES: 1// \<RET\>

MAXIMUM ACTIVE PROCESSES: 1// \<RET\>

SCHEDULING FREQUENCY (minutes): 9999// \<RET\>

DT/TM LAST STARTED OR STOPPED: \<RET\>

HANG TIME (seconds): 1// \<RET\>

GET WORK FUNCTION (TAG): // \<RET\>

GET WORK FUNCTION (ROUTINE): // \<RET\>

DO WORK FUNCTION (TAG): \<RET\>

DO WORK FUNCTION (ROUTINE): \<RET\>

MAX TRIES FINDING WORK: 0// \<RET\>

PERSISTENT: NO// \<RET\>

<span class="mark">DEDICATED LINK: // VABAY\<RET\></span>

VMS TCP SERVICE: NO// \<RET\>

Select HLO PROCESS REGISTRY PROCESS NAME: \<RET\>

# Daily Oversight and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Daily Oversight

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HLO System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM staff should check the operational status of HLO several times daily using the HLO System Monitor. Please refer to Section 5.2 of the HLO Technical Manual for complete instructions. The Brief System Status screen provides all the information necessary. The following should be verified:

- SYSTEM STATUS is RUNNING
- PROCESS MANAGER is RUNNING
- STANDARD LISTENER is OPERATIONAL
- TASKMAN is RUNNING
- DOWN LINKS is 0 (zero)
- MESSAGES PENDING TRANSMISSION is not unusually large
- STOPPED OUTGOING QUEUES is blank
- MESSAGES PENDING ON APPLICATION is not unusually large
- STOPPED INCOMING QUEUES is blank
- IF Interface Engine is used, then INTERFACE ENGINE is operational

|                                                   |                                                                                                                                                                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-126-installation-manual-release-notes/044.png) | At the time this was written, the status of the Interface Engine will show as “NOT OPERATIONAL.” This will continue until a new entry in the HL LOGICAL LINK named ‘VA-VIE’ is distributed in a future patch. |

If any of these conditions indicate that there may be a problem, then investigate further by following instructions found in Section 5.2 of the HLO Technical Manual.

### HLO Message Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IRM should run three reports on a daily basis and review them for signs of problems. Refer to Section 5.3 of the HLO Technical Manual for further details on these reports. Potential problems should be fully investigated and either corrected or referred to the appropriate subject experts. For example, if a message is not processed due to an application error, the problem might need to be referred to the appropriate package expert.

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
3.  Double-check that the HLO SYSTEM PARAMETERS File (#779.1) IEN=1 (there should be exactly one entry) for the HLO STANDARD LISTENER field (#.1) points to the correct listener entry in the HL LOGICAL LINK File (#870). (see 2. above).
4.  Double-check the HLO PROCESS REGISTRY File (#779.3) record for the site’s listener process. Most sites will be using the VMS TCP Listener process. The record should include the following:
    1.  Field ACTIVE (#.02) is set to YES
    2.  Field DEDICATED LINK (#.14) points to the correct listener entry in the HL LOGICAL LINK File (#870). (see 2 above).

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