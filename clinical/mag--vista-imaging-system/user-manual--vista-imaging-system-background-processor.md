---
title: VistA Imaging System Background Processor User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: VistA Imaging System Background Processor
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 2005
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - class
  - table
  - queue
  - vista
  - image
  - purge
  - contents
  - imaging
  - tier
  - strong
page_count: 0
word_count: 42600
section_count: 63
table_count: 20
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: December 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_bp_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_bp_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

---
title: |
  VistA ImagingBackground Processor User Manual

  ![](vista-imaging-system-background-processor-user-manual/001.png)

  December 2022
---

Department of Veterans Affairs (VA)Office of Information and Technology (OIT)  
Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Patch</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Dec 2022</td>
<td>Patch 331</td>
<td>20</td>
<td>Updated document with current template and changed 2012 server reference to 2019 server.</td>
</tr>
<tr class="even">
<td>Sept 2019</td>
<td>Patch 238</td>
<td>19</td>
<td>Updated Section 6.4.5: Purge Events Table</td>
</tr>
<tr class="odd">
<td>Dec 2018</td>
<td>Patch 222</td>
<td>18</td>
<td>Added 5.7.1.6 <a href="#bp-verifier-debug-log">BP Verifier Debug Log</a></td>
</tr>
<tr class="even">
<td>Oct 2018</td>
<td>Patch 214</td>
<td>17</td>
<td>Updated Site Parameters window. Encrypted Password.</td>
</tr>
<tr class="odd">
<td>July 2018</td>
<td>Patch 198</td>
<td>16</td>
<td>Updated install section.</td>
</tr>
<tr class="even">
<td>Jun 2018</td>
<td>Patch 198</td>
<td>15</td>
<td>Updated section: 2.4 Installation – Client Requirements; Added section 2.6: New Server Installation; Updated 10:4 Logging; added section10.4.1.4 – creating a debugging for Verifier</td>
</tr>
<tr class="odd">
<td>Mar 2018</td>
<td>Patch 196</td>
<td>14</td>
<td><p>Added section 2.4.1 Client Requirements in the 2.4 Installation Section; added section 4.5.2 Delay Between Queue Processing.</p>
<p>Revised sections: 2.1, 2.2, 2.52, 3.1, 3.6.1, 4.5.1, 4.5.3, 4.6.3, 5.5.1, 6.4, and 7.5.</p></td>
</tr>
<tr class="even">
<td>Sep 2015</td>
<td>Patch 158</td>
<td>13</td>
<td>Added 9.5 because of field testing.</td>
</tr>
<tr class="odd">
<td>June 2015</td>
<td>Patch 158</td>
<td>12</td>
<td>Revised sections 8.5; added sections 9 and 10.</td>
</tr>
<tr class="even">
<td>Sept 2013</td>
<td>Patch 135</td>
<td>11</td>
<td>Revised sections 2.5.2, 3.1, 3.2.1, 3.6.1, 3.6.3, 3.6.4, 4.6.3.4, 3.7. Added section 8.5.</td>
</tr>
<tr class="odd">
<td>Jan 2012</td>
<td>Patch 121</td>
<td>10</td>
<td>Updated sections 4.1, 4.3, 8.2.2. Added sections 4.6.2.17 and 4.6.2.18.</td>
</tr>
<tr class="even">
<td>Mar 2011</td>
<td>Patch 39</td>
<td>9</td>
<td>Revamped content, added new Patch 39 features, merged content from Verifier User Manual. Globally replaced term BP “Workstation” with BP “Server”. 1<sup>st</sup>, 2<sup>nd</sup>, and 3<sup>rd</sup> WPRs completed.</td>
</tr>
<tr class="odd">
<td>May 2006</td>
<td>Patch 20</td>
<td>8</td>
<td>Replaced all “VMC” with “VistA Imaging Shares”.</td>
</tr>
<tr class="even">
<td>Feb 2006</td>
<td>Patch 20</td>
<td>7</td>
<td>Updated sections 5.5.3 thru 5.5.5.1 “VistARad”</td>
</tr>
<tr class="odd">
<td>Dec 2005</td>
<td>Patch 20</td>
<td>6</td>
<td>Updated Background Processor content in this manual.</td>
</tr>
<tr class="even">
<td>June 2005</td>
<td>Patch 20</td>
<td>5</td>
<td>Updated Background Processor content in this manual. Extracted the entire Chapter 4 Verifier content and created a new manual which contains the extracted content.</td>
</tr>
<tr class="odd">
<td>June 2005</td>
<td>Patch 13</td>
<td>4</td>
<td>Expanded and updated Verifier content. Moved Verifier content from the end of initial manual and created a separate manual.</td>
</tr>
<tr class="even">
<td>May 2004</td>
<td>Patch 13</td>
<td>3</td>
<td>Expanded and updated Verifier content. Moved Verifier content from Chapter 4 to end of manual. Appendix B absorbed into Chapters 4 (Purge) and 7 (Verifier)</td>
</tr>
<tr class="odd">
<td>Apr 2004</td>
<td>Patch 3</td>
<td>2</td>
<td>Updated section 3.1.8.10 and 5.5.7.6 to reflect transition to long file names.</td>
</tr>
<tr class="even">
<td>May 2002</td>
<td>Patch 7</td>
<td>1</td>
<td>Updated section 3.1.6.4 “Operational Procedures.”</td>
</tr>
</tbody>
</table>

Table of Contents

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
  - [What is the Background Processor?](#what-is-the-background-processor)
    - [Background Processor Applications](#background-processor-applications)
  - [VistA Imaging and the Background Processor](#vista-imaging-and-the-background-processor)
  - [VistA Imaging Functional Flow](#vista-imaging-functional-flow)
  - [Features of the Background Processor](#features-of-the-background-processor)
  - [The Background Processor Usage and Maintenance of RAID Groups](#the-background-processor-usage-and-maintenance-of-raid-groups)
    - [RAID Group Guidelines](#raid-group-guidelines)
    - [Scheduling a RAID Group Advance](#scheduling-a-raid-group-advance)
    - [Additional Maintenance of Tier 1](#additional-maintenance-of-tier-1)
- [Setting Up Your BP System](#setting-up-your-bp-system)
  - [Software Requirements](#software-requirements)
  - [Hardware Requirements](#hardware-requirements)
  - [Setup Requirements](#setup-requirements)
    - [Windows Security](#windows-security)
    - [VistA Security](#vista-security)
  - [Installation](#installation)
    - [Logging In](#logging-in)
  - [Configuring BP Servers](#configuring-bp-servers)
    - [Guidelines](#guidelines)
    - [Adding a BP Server to the VistA Imaging System](#adding-a-bp-server-to-the-vista-imaging-system)
    - [Assigning Tasks (Queues) to a BP Server](#assigning-tasks-queues-to-a-bp-server)
    - [Removing a BP Server from the VistA Imaging System](#removing-a-bp-server-from-the-vista-imaging-system)
    - [Specifying the Log File Location and Size](#specifying-the-log-file-location-and-size)
  - [New Server Installation](#new-server-installation)
- [Configuring the Application](#configuring-the-application)
  - [Introduction](#introduction-1)
    - [Overall Guidelines](#overall-guidelines)
  - [Configuring the VistA Imaging Site Parameters](#configuring-the-vista-imaging-site-parameters)
    - [Imaging Site Parameters Window](#imaging-site-parameters-window)
    - [Administrative Settings](#administrative-settings)
  - [Configuring Mail Messages](#configuring-mail-messages)
    - [Mail Messages Window](#mail-messages-window)
  - [Configuring Mail Groups](#configuring-mail-groups)
    - [Mail Groups Window](#mail-groups-window)
  - [Configuring the Purge, Verifier, and RAID Group Advance Settings](#configuring-the-purge-verifier-and-raid-group-advance-settings)
    - [Purge Settings](#purge-settings)
    - [Verifier Settings](#verifier-settings)
    - [RAID Group Advance Settings](#raid-group-advance-settings)
  - [Queue Manager](#queue-manager)
    - [Queue Manager Operations](#queue-manager-operations)
    - [Purging a Queue](#purging-a-queue)
    - [Re-Queuing a Failed Image File](#re-queuing-a-failed-image-file)
    - [Refreshing a Queue Display](#refreshing-a-queue-display)
    - [Setting a Queue Partition](#setting-a-queue-partition)
    - [Accessing Import Queue Properties](#accessing-import-queue-properties)
  - [Network Location Manager](#network-location-manager)
  - [Configuring the Network Location Manager](#configuring-the-network-location-manager)
    - [Adding a New Location to Network Location Manager](#adding-a-new-location-to-network-location-manager)
    - [Editing the Properties of a Network Location](#editing-the-properties-of-a-network-location)
    - [Adding a RAID Group](#adding-a-raid-group)
    - [GCC Queue for PhotoID](#gcc-queue-for-photoid)
- [Queue Processor](#queue-processor)
  - [Application Description](#application-description)
  - [Setup Guidelines](#setup-guidelines)
  - [Tasking](#tasking)
  - [Understanding Processing](#understanding-processing)
  - [Starting/Running the Application](#startingrunning-the-application)
    - [Starting the Application and Analyzing the Activity](#starting-the-application-and-analyzing-the-activity)
    - [Delay Between Queue Processing.](#delay-between-queue-processing)
    - [Getting Help](#getting-help)
  - [Reports](#reports)
    - [Log Files](#log-files)
    - [Email Messages](#email-messages)
    - [Screen-Generated Output](#screen-generated-output)
- [Verifier](#verifier)
  - [Application Description](#application-description-1)
  - [Setting Up the Verifier](#setting-up-the-verifier)
  - [Tasking](#tasking-1)
  - [Understanding Processing](#understanding-processing-1)
    - [Reasons for Running the Verifier](#reasons-for-running-the-verifier)
  - [Maintenance Operations](#maintenance-operations)
    - [Integrity Checks](#integrity-checks)
  - [Starting/Running the Verifier](#startingrunning-the-verifier)
  - [Reports](#reports-1)
    - [Log Files](#log-files-1)
- [Purge](#purge)
  - [Application Description](#application-description-2)
  - [Setting Up](#setting-up)
  - [Tasking](#tasking-2)
  - [Understanding Processing](#understanding-processing-2)
    - [Setting Purge Parameters](#setting-purge-parameters)
    - [File Types for Purge](#file-types-for-purge)
    - [Purge by Dates](#purge-by-dates)
    - [Express Purge Options](#express-purge-options)
    - [Purge Events Table](#purge-events-table)
  - [Starting/Running the Purge](#startingrunning-the-purge)
  - [Reports](#reports-2)
    - [Log Files](#log-files-2)
    - [Emails](#emails)
    - [Screen-Generated Output](#screen-generated-output-1)
- [System Monitoring](#system-monitoring)
  - [Description of the BP Server Monitor Utility](#description-of-the-bp-server-monitor-utility)
    - [Evaluating EVAL Queues](#evaluating-eval-queues)
    - [Reporting Using Mail Messages](#reporting-using-mail-messages)
  - [Configuring Mail MessagesConfiguring the BP Server Monitor](#configuring-mail-messagesconfiguring-the-bp-server-monitor)
  - [Scheduling the BP Server Monitor](#scheduling-the-bp-server-monitor)
    - [Example of Scheduling](#example-of-scheduling)
    - [Tasking BP Server Monitor Menu Options](#tasking-bp-server-monitor-menu-options)
  - [Monitoring the BP Queue Processor](#monitoring-the-bp-queue-processor)
    - [Precautionary Guidelines](#precautionary-guidelines)
    - [Daily Monitoring](#daily-monitoring)
  - [Monitoring the BP Verifier](#monitoring-the-bp-verifier)
  - [Monitoring the BP Purge](#monitoring-the-bp-purge)
    - [Precautionary Guidelines](#precautionary-guidelines-1)
- [Troubleshooting](#troubleshooting)
  - [General Startup](#general-startup)
    - [Unable to connect to server](#unable-to-connect-to-server)
    - [Logging In](#logging-in-1)
  - [Network Connection](#network-connection)
    - [Broker Failures](#broker-failures)
    - [Not Enough Server Cache](#not-enough-server-cache)
    - [Not Enough Process Memory](#not-enough-process-memory)
    - [Not Enough Write Cache Available](#not-enough-write-cache-available)
  - [Queue Processor](#queue-processor-1)
    - [Startup](#startup)
    - [Runtime](#runtime)
  - [Verifier](#verifier-1)
    - [Start/Run](#startrun)
    - [Output HTML Messages](#output-html-messages)
    - [Integrity Messages on Patient Data](#integrity-messages-on-patient-data)
  - [Purge](#purge-1)
  - [Import API](#import-api)
- [Abstract/Thumbnail Maker](#abstractthumbnail-maker)
  - [Application Description](#application-description-3)
  - [Setup](#setup)
    - [Menu](#menu)
  - [Process Flow](#process-flow)
  - [Logging](#logging)
    - [Log Files](#log-files-3)
  - [Error Messages](#error-messages)
- [Import OCX](#import-ocx)
  - [Application Description](#application-description-4)
  - [Setup](#setup-1)
  - [Process Flow](#process-flow-1)
  - [Logging](#logging-1)
  - [Log Files](#log-files-4)
    - [Debug Modes](#debug-modes)
  - [Log File Management](#log-file-management)
  - [Log File Format](#log-file-format)
- [Broker Server Configuration](#broker-server-configuration)
- [File Formats](#file-formats)
- [Verifier Integrity Samples](#verifier-integrity-samples)
- [Glossary](#glossary)
- [Index](#index)
The purpose of this manual is to provide users with instructions on using the VistA Imaging Background Processor (BP) V. 3.0 software and system components. It includes explanations of the options and controls available from the VistA Imaging Background Processor. Instructions are provided about how to perform various system tasks.
> **NOTE:** Additional information about the various VistA Imaging components such as servers, workstations, Remote Procedure Call (RPC) Broker software, and OTG-Disk Extender Jukebox software can be found in the *VistA Imaging Installation Guide*.
The VistA Imaging System documentation suite includes…
- Release Notes
- Installation Guides
- Security Guide
- Technical Manual
- User Manuals
Terms of Use
Use of the Background Processor is subject to the following provisions:
![](vista-imaging-system-background-processor-user-manual/002.png)Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.
![](vista-imaging-system-background-processor-user-manual/003.png)No modifications may be made to the software workstation without the express written consent of the VistA Imaging National Project Manager.
Intended Audience
This software should be maintained by trained Imaging Coordinators who have IT experience and a thorough knowledge of the Imaging product.
Conventions
This document uses the following conventions:
- The most current patch will be signified by “MAG\*3.0\*NNN”.
- Change bars in margins indicate content added or updated since the last revision.
- Controls, options, and button names are shown in bold.
- Keyboard key names are shown in bold and in brackets \< \>.
- Sample output is shown in monospace.
- When this document is used online, hyperlinks are indicated by blue text.
- Useful or supplementary information is shown in a Tip.
- Required or important information is shown with the word Note or Important.
- Critical information is indicated by ![](vista-imaging-system-background-processor-user-manual/004.png).
Related Information
The VistA Imaging System documentation suite includes:
- Release Notes
- Installation Guides
- Security Guide
- Technical Manual
> **NOTE:** Additional information about the various VistA Imaging components such as servers, workstations, Remote Procedure Call (RPC) Broker software, and OTG-Disk Extender Jukebox software can be found in the VistA Imaging Installation Guide.
VistA Imaging Support
If you encounter any problems using VistA Imaging Background Processor, which cannot be resolved follow your local, VISN, or regional procedures for problem resolution/escalation.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the Background Processor?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System is an extension to the Veterans Health Information System Technology Architecture (VistA) hospital information system that captures clinical images, scanned documents, motion images, and other non-textual data files and makes them part of the patient's electronic health record (EHR).

The VistA Imaging Background Processor (hereafter referred to as the Background Processor or BP) is a component in the VistA Imaging System. The BP runs on a Windows file server. The Background Processor ensures the archiving of DICOM and clinical images from Tier 1 (configured in RAID groups) onto the Tier 2 shares for long-term storage. These images are stored indefinitely on the archive device.

### Background Processor Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Background Processor consists of three applications:

- BP Queue Processor

> The Queue Processor moves image data between Tier 1 and Tier 2 or remote location.

- BP Verifier

> The Verifier maintains location integrity and checks data integrity between the VistA database and the storage media.

- BP Purge

> The BP Purge removes image files from the Tier 1 Image shares based on file dates.

The combination of these applications ensures that users can access the images for display and analysis in an efficient and timely manner. The three applications are explained in the chapters that follow.

## VistA Imaging and the Background Processor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below shows a network configuration of the VistA Imaging system. The system requires a minimum bandwidth of 100MB/sec.

Typically, the Clinical workstations and EKG systems are on this span.

The VistARad workstations, Tier 1, and Tier 2 are required to reside on a span that has a 1GB/sec bandwidth.

This high bandwidth results in faster viewing times for studies on those VistARad workstations.

![](vista-imaging-system-background-processor-user-manual/005.png)

## VistA Imaging Functional Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below shows the functional flow of the VistA Imaging system related to the Background Processor products. Images originate from a variety of sources and are stored for the short term on Tier 1. The Background Processor's Queue Processor copies these images to Tier 2, where they are stored permanently. The Background Processor's Purge application manages free space on Tier 1 by deleting older images. The Queue Processor can restore these images to Tier 1 when requested by the display workstations. The Background Processor's Verifier application maintains the integrity of image records, including location pointers, stored in the VistA database.

Vista Imaging Functional Flow

![](vista-imaging-system-background-processor-user-manual/006.png)

## Features of the Background Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Background Processor provides the following features:

- Manages image storage on various shared network devices
- Migrates image files between magnetic VistA Imaging shares and jukebox storage units
- Maintains adequate free storage space on VistA Imaging shares
- Copies image files to the VistA Imaging shares whenever they are requested by image display workstations
- Validates VistA Imaging network file references
- Verifies the integrity of the location of image files on Imaging shares recorded in the VistA database
- Configures local VistA Imaging site parameters
- Manages error recovery
- Logs activities and errors
- Imports images into VistA Imaging
- Exports images from VistA Imaging.

## The Background Processor Usage and Maintenance of RAID Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A RAID Group is a group of one-to-many shares that will be recognized as a unit within the Imaging storage network. Its purpose is to reduce the number of active storage shares to facilitate quicker tape backups (both incremental and full). Newly acquired images are distributed evenly among all the shares within a RAID Group.

![](vista-imaging-system-background-processor-user-manual/007.png)

### RAID Group Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Distribute the shares among multiple RAID Groups.
- Fill the shares in each group to the Server Size, then switch the current RAID group to the next.
- New image files will be distributed over all the shares assigned to that group.
- Nightly incremental tape backups as well as monthly/quarterly tape backups must be done only on active RAID Groups.
- When it has reached capacity, a final full backup should be done on all the shares and nightly incremental tape backups and monthly/quarterly tape backups started on the next current write group.

### Scheduling a RAID Group Advance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A RAID Group Advance can be scheduled, as follows:

You may choose to establish a pattern to utilize your entire RAID by scheduling a weekly RAID Group Advance and coordinating this with a scheduled purge followed by weekly backup of the RAID Group that was most previously active. See section *3.5.3, RAID Group Advance Settings,* for details.

An automatic RAID Group Advance occurs, as follows:

When the used space on all the shares in a RAID Group exceeds the high-water mark, the software will change the current write RAID Group to the next one in sequence. This event will be captured in the BackProc.log file. See section *3.2.2.1 Storage Functions Settings*, for more details.

A diagram of the changing of a RAID Group follows.

> ![](vista-imaging-system-background-processor-user-manual/008.png)

### Additional Maintenance of Tier 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following utilities support the Background Processor:

- MagDexter used to create summary and detail platter reports containing platter information such as the name, serial number, and status of each jukebox platter
- MagKat used to backfill specific fields in the IMAGE file (#2005) in the VistA database using data from the text files associated with images
- MagUtility used to report and resolve problems with “orphan” files, delete obsolete or incorrect entries from the NETWORK LOCATION file (#2005.2), update the VistA database with image information, and copy images and text files

For details, see the *Storage Utilities User Manual*.

# Setting Up Your BP System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- Software Requirements
- Hardware Requirements
- Setup Requirements -Security
- Installing the BP software
- Configuring BP Servers

====================================================================

This chapter provides all the steps necessary to set up your Background Processor system.

> **NOTE:** Configuration information that applies to site requirements is explained in *Chapter 3 Configuring the Application*.

1.  

## Software Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Background Processor software, MAG3_0P*NNN*T1_Background_Processor_Setup.exe , is distributed with the VistA Imaging system. Three components are included in this file: the Queue Processor, the Verifier, and the Purge software.

The Background Processor software presumes the presence of the proper Imaging KIDS package installed on VistA. Refer to the most recent *Imaging Patch Description* for the Background Processor for compatibility information. Once they are installed, the executables for the Background Processor applications are in the C:\Program Files (x86)\Vista\Imaging\BackProc directory and are named:

Patch 222

- Magbtm.exe - Queue Processor
- MagVerifier.exe -Verifier
- MagPurge.exe - Purge.

## Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 50 GB local disk space (minimum)
- 1 GB RAM (minimum)
- Server class machine (The BP can be run on Image servers. However, the Schedule and Auto events (Verifier & Purge) only execute on a Server class machine.) To run patch MAG\*3.0\*NNN executables, the minimum Operating System must be Windows Server 2012.
- 100MB/sec network bandwidth or better
- Local or remote archive device – jukebox, storage grid, etc. (when possible).

## Setup Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are some initial checks that must be done on the server/client where the BP will run and on the VistA system where Caché will exist. The following sections describe the setup requirements on each platform.

### Windows Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Use the established Windows Imaging Administrator (VHAxxxIA) account for accessing the Background Processor.
- The Imaging Administrator account is a domain account that has READ/WRITE permissions to the Imaging Tier 1 and Tier 2 shares. This account will be used to log into the BP Server.
- Remote IMPORT share permissions must match the Windows OS login on the server running the BP software.
- Remote EXPORT share permissions must match the Windows OS login on the server running the BP software.
- The Imaging Administrator account is a domain account that has READ/WRITE share/folder/file permissions on the Imaging Tier 1 shares and Tier 2 shares (see the *Imaging Installation Guide*) to the Windows account that will log into the BP Server.

### VistA Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Background Processor requires authentication to VistA via a Broker connection to function. This account must have the following permissions:

- MAG SYSTEM security key
- All MAG\* RPC's \[MAG WINDOWS\] secondary menu option.

> Since it is essential that the Background Processor can continue to perform its function without human interaction, a site can establish a special “service account” for which the access and verify codes will not expire. When a Background Processor loses a network connection because of an interruption, it is important that the Background Processor have access to a continuously available service account to reestablish connectivity without user interaction. See the section 5.3 in the *DICOM Gateway Installation Guide* for information on how to initially set up this account if not done already.

- The VistA Imaging service account for VistA should be assigned one account per division. This is required because each division is defined by an entry in the IMAGING SITE PARAMETERS file (#2006.1).

> Note: When an end-user signs into the VistA database, the user’s default division is used or the Division selected at log-on when an end-user has multi-divisions assigned.

- The credentials for the VistA Imaging service account for VistA should be entered into the following fields in the IMAGING SITE PARAMETERS file (#2006.1). They are the Service account Access/Verify codes.
- DICOM GATEWAY ACCESS CODE (field \#124)
- DICOM GATEWAY VERIFY CODE (field \#125)

#### Security Keys, RPCs, and Menu Options in VistA

Both the primary and Service accounts should have the security access listed.

- MAG SYSTEM as a security key
- All MAG\* RPCs \[MAG WINDOWS\] as a Secondary Menu Option.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the *VistA Imaging System Installation Guide* for detailed steps on installing Background Processor applications.

![](vista-imaging-system-background-processor-user-manual/009.png) Important: Any Background Processor applications that are running must be stopped and closed prior to the installation of the KIDS and Client software. Any image capture application (Clinical Capture and DICOM Gateway processing) can continue to run during the installation.

Both the client software and the KIDS build installations are mandatory for operating the BP software. See the Patch Description for patch-specific installation steps.

### Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Background Processor software requires a VistA login and password.

1.  To log in, use a valid set of credentials. Upon launching Queue Processor, you will be prompted to select a server.
2.  Select a server from the screen below

> ![](vista-imaging-system-background-processor-user-manual/010.png)

3.  Then enter your credentials in the following login screen:

![](vista-imaging-system-background-processor-user-manual/011.png)

## Configuring BP Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- It is necessary to configure a BP Server only if the site is capturing images for storage on VistA Imaging servers.
- At least one BP Server must be present to perform utility functions such as copying image files to and from Imaging servers (the Tier 1 shares) and Tier 2 (a jukebox/storage grid).
- The software does not permit redundant assignments of BP activities. For example, you cannot specify that more than one BP Server perform the JUKEBOX task.
- The JUKEBOX and DELETE tasks must be run on the same server. If not, the Deletes may be processed in advance of their being written to the Jukebox. In this case, the image may be lost before it is archived and the Delete will eventually fail. These Failed Deletes must be Re-Queued.
- The IMPORT and ABSTRACT tasks should be run on the same server. There will be occasional archived FULL files that do not have abstracts. If these ABSTRACT tasks are failing, the JBTOHD task should be added to server running the IMPORT/ABSTRACT task. Please note the IMPORT can execute on a single server.
- If the Verifier and Purge are to be run on servers other than those running the Queue Processor tasks, a BP Server must be configured for those servers. If the Verifier and Purge are to be automatically run, then another queue process must be running on that BP Server for the Scheduled task to be started.
- When PREFET is added to the VistA Imaging display workstation configuration, this activity must be checked on the BP Server configuration window in order to have these queue types processed.
- A directory can be created on the Tier 1 shares or remote storage location to archive BP log files for later reference.

### Adding a BP Server to the VistA Imaging System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most sites will find that a single BP Server provides adequate performance; however, the product does provide the capability for adding additional BP Servers. Adding additional BP Servers will improve performance by allowing the distribution of tasks among the newly assigned BP Servers.

To set up a BP Server application:

1.  From the Windows Start \> Programs menu, select VistA Imaging Programs \> Background Processor \>Queue Processor.
2.  Enter the Access/Verify code for the BP account with the VistA security properties listed in section *2.3.2VistA Security*.

> The BP Queue Processor application window opens.

![](vista-imaging-system-background-processor-user-manual/012.png)

3.  From Queue Processor menu bar, select Edit \> BP Servers.
- The BP Server Parameters window enables you to create a unique server name for a server and assign tasks to that server. The properties on these servers enable you to specify the location of the log files for each application and the file’s size limit (described in section *2.5.5*, *Specifying the Log File Location and Size*).

> ![](vista-imaging-system-background-processor-user-manual/013.png)

4.  Click the Add New BP Server button at the bottom of the tree pane.

> In the BP Server Add dialog box displayed, enter a logical name for the BP Server, for example, BP1.  
> Note: The name must be at least three characters in length and can contain alpha and numeric characters and must be unique. Once the name is saved, it cannot be renamed. It can only be deleted when all the tasks assigned to it are de-assigned.

If the name is not valid, an error message is displayed. Correct the name and repeat the steps.

### Assigning Tasks (Queues) to a BP Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, no tasks are assigned to BP Servers. The tasks will need to be assigned for that function of the BP software to operate. Assign tasks based on the needs of your facility. As previously mentioned, a queue name identifies the task that the Queue Processor performs. All queues are available to assign to a BP Server, except EVAL.

> **NOTE:** Assign Purge as well as the Scheduled Verify to BP Servers. These features help maintain the system without operator monitoring and control.

1.  Drag and drop a task from the *Unassigned Tasks* in the tree pane (shown) to the server that is designated to run that task.

> ![](vista-imaging-system-background-processor-user-manual/014.png)

> Note: The priority of tasks running on the same server is set internally and cannot be changed. The functions of each task are:

1)  JBTOHD – populates the VistA Imaging shares with images that have been deleted from the Tier 1 shares through the Purge function.
2)  PREFET – populates the VistA Imaging shares with images that were requested based on VistA Imaging Display workstation configuration parameters.
3)  ABSTRACT – creates ABS derivative thumbnail files from FULL/BIG files when the file type is missing on the Tier 1 shares and Tier 2 (jukebox)
4)  IMPORT – provides a means for external applications to archive images in the VistA Imaging environment.
5)  JUKEBOX – copies images to the long-term archival storage device
6)  DELETE – removes images from the VistA Imaging shares.
7)  GCC – exports images to a share that is external to the local VistA Imaging network.
8)  PURGE – This assignment includes both the auto purge and the scheduled purge tasks. Refer to the purge section of this document for more details.
9)  SCHEDULED VERIFY – automatically runs the Verifier at the assigned time to check the integrity of the Image records in VistA with the file locations on Tier 1 and Tier 2 storage. Only the most recent unchecked IENs are verified.
2.  Click Apply to save the changes or OK to save the changes and exit.

### Removing a BP Server from the VistA Imaging System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Queue Processor menu bar, select Edit \> BP Servers.
2.  In the tree pane, right-click the server name and select Delete BP Server from the pop-up menu displayed.  
    > Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.

> ![](vista-imaging-system-background-processor-user-manual/015.png)  

> The selected BP Server is removed from the tree pane.  
> Note: This same name can be added later.

### Specifying the Log File Location and Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click a BP Server name in the tree pane and select Server Properties from the pop-up menu displayed.  
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.  
      
    ![](vista-imaging-system-background-processor-user-manual/016.png)  
      
    The BP Server Properties dialog box is displayed.

> ![](vista-imaging-system-background-processor-user-manual/017.png)

2.  Enter the size in megabytes in the Log File Size field.

> The default log file size limit is 2 MB, if left blank.

3.  Specify the Network Log file location on a local machine or a remote network location.

> Note: By default, the log files are created on the local drive in the directory *Program Files (x86)\VistA\Imaging\BackProc\Log*. If a remote network location is entered, the Background Processor must have Read and Write access to it. Use the \\computer name\share name\\ format and do not use a letter drive.

4.  Click OK to save the information and close the window.

## New Server Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*NNN contains all the Background Processor and Background Processor utility applications. It will install on a new server that hasn’t had a previous BP installed.

Desktop shortcuts for the Purge, Verifier and Background Processor Queue Processor are automatically created on the desktop.

When installing the BP Queue Processor, BP Verifier, and BP Purge on a 64-bit operating system such as Windows 2012 Server, “Run as administrator” must be manually set using the check box in the Advanced Properties window on each of the desktop shortcuts and the menu options. Do this for all three client applications.

If the MAG\*3.0\*NNN Background Processor client is installed before installing the MAG\*3.0\*NNN KIDS, when the client is run, a message will display that states the versions of the Background Processor client and the version of the VistA Imaging host system are not compatible. The user will be prompted to install compatible versions of the Background Processor client and the VistA system host software. If such a message displays, complete the following steps:

1)  Shut down the Background Processor client.
2)  Install the MAG\*3.0\*NNN KIDS.
3)  Now run the MAG\*3.0\*NNN Background Processor client.

# Configuring the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

====================================================================

- Configuring the Imaging Site Parameters
- Configuring Mail Messages
- Configuring Mail Groups
- Configuring the Purge, Verifier, and RAID Group Advance Settings
- Configuring the Queue Manager
- Configuring the Network Location Manager

====================================================================

2.  

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the parameters for running the BP applications (Queue Processor/Verifier/Purge) are managed through the Queue Processor GUI. There are multiple parameter windows to change settings for each BP application. The parameter windows are accessed through the Edit menu on the BP Queue Processor application menu bar.

### Overall Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The three BP applications (Queue Processor, Verifier, and Purge) are installed with a default configuration. However, each of these applications will need to be configured depending on how/when/where they are to be run. When the BP is first installed, review the parameters to insure the products are set up according to your site’s needs.
- A BP Server will need to be defined for each Windows server that will be running a task and/or the Purge and/or Verifier.
- A specific task (JUKEBOX, JBTOHD, IMPORT, etc.) on the Queue Processor can be run only on one server.
- A task must be assigned to a BP Server before that task will run when the Queue Processor starts.
- Some parameter windows have Apply buttons. Be sure to click the Apply button to commit changes to the database. (Cancel resets any changed parameters.) The windows that do not have Apply buttons are committed when the change is made. The OK button also commits the changes and closes the main parameter window.

## Configuring the VistA Imaging Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parameters on the Imaging Site Parameters window control activities within the Queue Processor as well as the DICOM Gateways, Clinical Capture, Clinical Display and VistARad. The site parameters can be configured for these functionalities:

- Access to the image shares
- Service account login information
- Routing share configuration
- Display and capture workstations
- DICOM Gateways
- Jukebox configuration
- RAID Groups configuration

### Imaging Site Parameters Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit \> Imaging Site Parameters menu on the Queue Processor menu bar opens the Imaging Site Parameters window used to modify entries in the VistA database. Each of the boxed areas in the window is described below.

![](vista-imaging-system-background-processor-user-manual/018.png)

### Administrative Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-background-processor-user-manual/019.png)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Descript ion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Current Namespace</td>
<td><blockquote>
<p>Each VHA facility has its own unique 3-character designator. The Current Namespace file is used to store this 3-letter facility designator. It is used in Imaging as the first 3 characters of the 14-character name given to image files captured at this site. The VistA Imaging development and support teams maintain a central database with each site’s 3 letter designator. The Current Namespace field is not configurable. This is necessary to ensure that image file names across VHA are unique.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Tier 1 Write Location</td>
<td>All images from the gateways, Capture, etc. will be written to this share. The selected Current RAID Group determines which shares are listed on this dropdown list.</td>
</tr>
<tr class="odd">
<td>Generic Carbon Copy</td>
<td>Remote share where files will be exported. The share permissions must match the login credentials for the BP Server.</td>
</tr>
<tr class="even">
<td>Current RAID Group</td>
<td>The current active RAID Group includes the Tier 1 Write Location (described above). When new images are processed, they are stored on the Tier 1 Write Location share within this group. The RAID Groups are set up with the Network Location Manager.</td>
</tr>
<tr class="odd">
<td>Import Queue Security</td>
<td>Checks users Imaging security keys for permission to capture images.</td>
</tr>
<tr class="even">
<td>Site Code</td>
<td>Three-letter acronym for the site location. This is used for AutoRouting and MUSE.</td>
</tr>
<tr class="odd">
<td>Associated Institutions</td>
<td><p>This set of institution values will allow users from other institutions to access local images.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete pop-up menu that can also be accessed from the keyboard by using<br />
Shift + F10.</p></td>
</tr>
<tr class="even">
<td>VistARad Grouping</td>
<td><p>The radiologist can lock/interpret exams for other divisions (including the Parent Institution or other Associated Institutions), when those divisions are included in this set of institutions. Note that this setting controls exam locking and updating, as well as filtering of the UNREAD Exams lists to show only the Institutions that are defined here.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete pop-up menu that can also be accessed from the keyboard by using<br />
Shift + F10.</p></td>
</tr>
</tbody>
</table>

#### Storage Functions Settings

> ![](vista-imaging-system-background-processor-user-manual/020.png)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Tier 2 Write Location</td>
<td>Tier 2 share where newly acquired images are currently being written.</td>
</tr>
<tr class="even">
<td>% Tier 1 Reserve</td>
<td><p>The purpose of the reserve is to provide a significant amount of reserved primary storage to allow time for corrective action to create more space on the shares. Enter an integer between 1 and 50. The system defaults to 5 if the integer is outside the normal range.</p>
<p>When the used space on a share exceeds the specified percentage, then actions are taken within the BP (mail message sent, auto purging initiates (if scheduled).). In addition, the AutoWrite Location Update will be disabled and images will be written to that share until the free space is exhausted.</p></td>
</tr>
<tr class="odd">
<td>% Tier 2 Reserve</td>
<td>The default value is 5%. The values can be set in the range 0-50%. When the allocated space does not meet this watermark, then no JUKEBOX queues will be processed and Tier 2 retrieval requests may be compromised, depending on the Tier 2 technology.</td>
</tr>
<tr class="even">
<td>Auto Write Location Update</td>
<td><p>At the interval of every 20 minutes or 100 images written to a share, the Queue Processor will determine which share within a group has the most space and will use that share as the current write location for newly acquired images.</p>
<p>To manually select a Tier 1Write Location, uncheck the Auto Write Location Update box. Images will be written to the selected Tier 1 share until it is filled or manually changed to another share.</p></td>
</tr>
<tr class="odd">
<td>Multiple Namespace</td>
<td><p>List of all the legacy namespaces that have been used at a site and are reflected in the filenames on Tier 1 and Tier 2 shares.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete pop-up menu that can also be accessed from the keyboard by using Shift + F10.</p></td>
</tr>
<tr class="even">
<td>File Types</td>
<td><p>File extensions outside of the standard extensions that the BP products will recognize and treat as a standard extension file. These files will be copied from Tier 1 to Tier 2 with the execution of a JUKEBOX Queue, and copied from Tier 2 to Tier 1 with execution of a JBTOHD of the parent file(s), FULL or ABS. They will be purged from Tier 1 once the FULL file has purged.</p>
<p>TXT is a recommended member of this list.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete pop-up menu that can also be accessed from the keyboard by using Shift + F10.</p></td>
</tr>
</tbody>
</table>

#### TeleReader Settings

> ![](vista-imaging-system-background-processor-user-manual/021.png)

| Field or Checkbox  | Description                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Net Site Service   | Used by the Remote Image Views application to gain access to remote sites.                                 |
| Timeout TeleReader | The number of minutes that the TeleReader application will remain active before closing due to inactivity. |

#### Clinical Workstation Settings

![](vista-imaging-system-background-processor-user-manual/022.png)

| Field or Checkbox   | Description                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Capture Keys        | Check users’ Imaging security keys for permission to capture images.                                                                                |
| Timeout Windows Display | Number of minutes until the Imaging Display application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600).          |
| Timeout Windows Capture | Number of minutes until the Imaging Capture application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600).          |
| Timeout VistARad        | Number of minutes until the Imaging VistARad application will close due to inactivity. There is no default setting.                                 |
| Default MUSE Site \#    | MUSE site number that the Imaging Display application will connect to. Site numbers are usually 1, 2, 3, …. If left empty, the field defaults to 1. |
| Default User Preference | A specified user’s parameter settings will be used for first-time users of the Imaging system.                                                      |

#### Service Accounts Settings

These credentials are shared among the DICOM Gateway, Image cluster, Jukebox Server, and Background Processor.

![](vista-imaging-system-background-processor-user-manual/023.png)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr class="odd">
<th>Windows Username</th>
<th>Domain account used to access the Imaging shares on Tier 1 and Tier 2 (jukebox) shares. Both the Tier 1 and Tier 2 (jukebox) shares must have READ/WRITE permission to this account.</th>
</tr>
<tr class="header">
<th>Windows Password</th>
<th>Domain password used to access the Imaging shares on the Tier 1 and Tier 2 (jukebox) shares.</th>
</tr>
<tr class="odd">
<th>VistA Access</th>
<th><p>Encrypted access code for the Imaging Service Account in VistA. This account will be used to automatically re- log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).</p>
<p><strong>Note</strong>: The Imaging Service Account must have the MAG SYSTEM security key and secondary menu option All MAG* RPC's [MAG WINDOWS].</p></th>
</tr>
<tr class="header">
<th>VistA Verify</th>
<th>Encrypted verify code for the Imaging Service Account in VistA. This account will be used to automatically re-log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### DICOM Interface Settings

![](vista-imaging-system-background-processor-user-manual/024.png)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DICOM Gateway Write Location</td>
<td>Tier 1 share where newly acquired images are currently being written.</td>
</tr>
<tr class="even">
<td>DICOM Gateway Interface Switch Update</td>
<td>Indicates presence of a DICOM Gateway on the system.</td>
</tr>
<tr class="odd">
<td>Retention Days HL7 – Modality Work Lists</td>
<td><p>This field is used as the default value, in days, by the DICOM Text Gateway for three different user menu driven purges:</p>
<ul>
<li><p>This field is used by the Purge Old Modality Worklist Entries menu option to determine the number of retention days from the date of creation of Modality Worklist Entries.</p></li>
<li><p>This field is used by the Purge Old DICOM Message Files menu option to determine the number of retention days from the date of creation of DICOM messages that were sent to commercial PACS.</p></li>
<li><p>This field is used by the Purge Old HL7 Transaction Global Nodes menu option to determine the number of retention days from the date of creation of HL7 messages sent from VistA to the DICOM Text Gateway.</p></li>
</ul>
<p><strong>Note</strong>: This value may be overridden by the user when executing any of these menu options.</p></td>
</tr>
<tr class="even">
<td>% Free Space DICOM Messages</td>
<td>Minimum percentage of free disk space for DICOM HL7 messages on the text gateway. A typical value is 25%.</td>
</tr>
<tr class="odd">
<td>Retention Days DICOM Messages</td>
<td>Number of days to retain DICOM HL7 messages on the text gateway, 30 days is recommended.</td>
</tr>
</tbody>
</table>

## Configuring Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the BP products are running, they generate various alerts and informational messages. These messages/alerts are formatted into mail messages and can be sent to different levels of management within a facility. The Mail Message subject lines describe the condition with the content of the message containing the specific information. The recipients for each Mail Message Subject type can be set up using the Mail Message Manager.

### Mail Messages Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit \>Mail Messages menu on the Queue Processor menu bar opens the Mail Messages window used to set up recipients for each message type. The tab Mail Messages can also be selected.

![](vista-imaging-system-background-processor-user-manual/025.png)

#### Displaying Mail Users 

The list of the hospital users in the Mail Users section is not displayed until you click in the area shown in the previous screen image. The list may take a few minutes to appear, depending on the number of end-users defined in the site’s VistA database. The following is an example of a displayed list of mail users.

![](vista-imaging-system-background-processor-user-manual/026.png)

#### Adding Names

To select a name and associate it with a Mail Message type, drag the name from one of the windows on the right to the Mail Message Manager window on the left. The change will be stored in VistA when the name is dropped into the Mail Message category. Add as many names as needed to each Mail Message on the left.

#### Removing Names

When a user no longer wishes to receive a specific warning/alert, the user’s name can be removed from that message list at any time. VistA will be automatically updated to reflect the change.

1.  Locate the warning/alert message and right-click the username under the message title.
2.  Select Delete from the pop-up menu displayed.

> VistA will automatically be updated to reflect the change.

#### Notification Intervals

The mail messages are sent out to the designated users at specific intervals (default is 6 hours). These intervals can be adjusted per message name. To change a notification interval for a Mail Message, follow the steps below.

![](vista-imaging-system-background-processor-user-manual/027.png)

1.  Right-click a message name and select Properties from the pop-up menu displayed
2.  Change the Transmission frequency (in hours) to the new value.
3.  Click OK to close the window.

> VistA will automatically be updated to reflect the change.

#### Field Descriptions

The fields for the Mail Message Manager are described below.

| Field                 | Description                                                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kernel Mail Groups        | Alert/ informational message names                                                                                                                     |
| VistA Imaging Mail Groups | Complete list of the Imaging mail groups defined in the VistA database. Users in the selected Mail Group will be sent the alert/informational message. |
| Mail Users                | Complete list of users with mailboxes defined in the VistA database.                                                                                   |
| Security Key Holders      | Complete list of the Imaging security keys in the VistA database. Users that have the selected key will be sent the alert/informational message.       |

## Configuring Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can be added to existing mail groups using the Mail Groups window. These Mail Groups can be used to send alerts and informational messages to users through the Mail Message Manager window.

### Mail Groups Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mail Groups window can be opened using the Edit \>Mail Groups menu on the Queue Processor menu bar.

![](vista-imaging-system-background-processor-user-manual/028.png)

| Field or Checkbox | Description                                                         |
|-----------------------|-------------------------------------------------------------------------|
| Mail Groups           | List of the existing Imaging Mail Groups defined in the VistA database. |
| Users box         |                                                                         |
| Name                  | Complete list of users with mailboxes defined in the VistA database.    |

#### Displaying Mail Users

The list of the hospital users in the Mail Groups section is not displayed until you click in the area shown above. The list may take a few minutes to appear depending on the number of end-users defined in the site’s VistA database. The following is an example of a displayed list of mail users.

![](vista-imaging-system-background-processor-user-manual/029.png)

#### Guidelines on Adding Mail Groups

- Only active VistA users can be added as members to mail groups. An active user has an “IN” basket defined in VistA.
- Important: When adding a new member to a mail group, use the same email address as the one in the domain, which may or may not be the same as the user’s \*@va.gov address.
- This group is initialized during the install process.
- The installer is automatically added as a local member.
- The REDACTED is added as a required remote recipient to comply with the Food and Drug Administration requirements.
- It is recommended that the local VistA Imaging PACS Administrator, Imaging Coordinator, and any Imaging managers be added as a member as well as any network administrators who are responsible for the support of the VistA Imaging system.
- It is recommended that a local text pager recipient be added as a remote member. The pager service needs to provide email pager response. The standard email addressing format is supported by this system: “name@mail_domain”.
- Only individuals with the MAG SYSTEM security key will be displayed in the lookup dialogue for the local mail group.

#### Adding Members to Mail Groups

1.  From the Queue Processor menu bar, select Edit \> Mail Messages to open the Mail Groups window or select the Mail Messages tab.
2.  Drag and drop selected VistA users from the right list boxes to the Mail Groups list box.

> VistA will automatically be updated to reflect the change.

#### Adding Remote Members to Mail Groups

1.  Right-click a mail group and select Add Remote Mail Member from the pop-up menu displayed.  
      
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.
2.  In the Adding Remote Member dialog box displayed, type the following:

> Email username or phone number, followed by the “@” sign, followed by the domain

> The system uses SMTP Protocol.

3.  Click OK.

#### Deleting Members from Mail Groups

When a user or group of users no longer wishes to receive mail messages for a specific alert, that user/user group can be removed using the following steps:

1.  From the Queue Processor menu bar, select Edit \> Mail Messages to open the Mail Groups window or select the Mail Messages tab.
2.  Right-click a user/mail group and select Delete Group Member from the pop-up menu. VistA will automatically be updated to reflect the change.

#### Specifying Properties for Mail Groups

1.  From the Queue Processor menu bar, select Edit \> Mail Messages to open the Mail Groups window or select the Mail Messages tab.
2.  Right-click a mail group and select Properties from the pop-up menu displayed.  
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.
3.  ![](vista-imaging-system-background-processor-user-manual/030.png)
4.  When the Mail Group (properties) dialog box is displayed, enter the data.
5.  Click OK in the dialog box and then Apply in the Mail Groups window.

> ![](vista-imaging-system-background-processor-user-manual/031.png)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td>Describes the purpose of the mail group (Editable).</td>
</tr>
<tr class="even">
<td>Organizer</td>
<td>The organizer is the person who set up/created the mail group.</td>
</tr>
<tr class="odd">
<td>Type</td>
<td><p>Public: Can receive mail from anyone.</p>
<p>Private: Can only receive mail from a predefined Public group.</p>
<p>(Display only)</p></td>
</tr>
<tr class="even">
<td>Restrictions</td>
<td><p>Unrestricted: Used when creating a Public mail account. Anyone can mail to this account.</p>
<p>Organizer Only: An organizer can add new members to a "Private" mail group. (Display only)</p></td>
</tr>
<tr class="odd">
<td>Member</td>
<td>Lists the users in the mail group.</td>
</tr>
<tr class="even">
<td>Member group Name</td>
<td>The parent group name for this mail group.</td>
</tr>
<tr class="odd">
<td>Remote Member</td>
<td>E-mail address of a VA user who is external to the site but part of the domain.</td>
</tr>
</tbody>
</table>

## Configuring the Purge, Verifier, and RAID Group Advance Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge / Verifier / RAID Groups window is used for setting up the Scheduled Verifier, Scheduled Purge and RAID Group Advance activities. In addition, the parameters for the Purge activity are set up through this window.

Selecting the Edit \> Purge \> Verifier \> RG Settings menu on the Queue Processor menu bar opens the Purge / Verifier / RAID Groups window.

![](vista-imaging-system-background-processor-user-manual/032.png)

### Purge Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge process is used to remove image files from Tier 1 when the free space is low or when older and/or not recently viewed image files can be purged to allow room for newly acquired images. It is important to note that no file is purged from Tier 1 shares if it has not been verified and confirmed as saved on the Tier 2.

The Purge can be run manually in standalone mode or as a part of the Queue Processor. The Purge Parameters are used to control the purge activities in auto, manual and scheduled modes.

#### Guidelines for Setting Retention Days on Files for the Purge

General guidelines:

- Determine the span of dates of images that will be preserved on the Imaging shares.
- The shorter the timeframe, the more space will be free on the disk when the purge completes.
- Multiple purges may be required to determine the retention days. It is advisable to start with one share with a large retention day’s value.
- Not all sites capture all the file types specified in the parameter list.
- If the frequency and the results of purging are acceptable, then it is not advisable to change the purge values.
- If there is still not enough free space after the purge, decrease the Purge Parameters (BIG and FULL files, in particular) and repeat the purge until the desired free space is obtained.

Factors that determine the best set of purge parameters for an individual site are:

- The frequency of purges
- The volume of image acquisition rate
- The volume of image file retrieval
- The use of Pre-Fetch
- The capacity of disk space for VistA Imaging shares

Some sites have extended their Tier 1 capacities and are able to maintain five or more years of images on the shares. These sites may only need to purge once per year to purge off the latest year of images (year 6). Others who have smaller Tier 1 sets must purge more frequently and can only have a limited number of images on their shares.

For your site, strive to keep the shares between 80% and 90% full (or between 10% and 20% free space). When the Purge process completes and the resulting free space is more than this value, adjust the parameters accordingly.

#### Configuring the Retention Days Settings

![](vista-imaging-system-background-processor-user-manual/033.png)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Retention Days and Retention Dates box</strong></td>
</tr>
<tr class="even">
<td>Full Files</td>
<td><p>Source: Images from the DICOM Gateways, Clinical Capture workstations and Imports.</p>
<p>File extensions: 756, ASC, AVI, BMP, BW, DCM, DOC, HTM, HTML, JPG, MHT, MHTML, MP3, MP4, MPEG, MPG, PAC, PDF, RTF, TGA, TIF, WAV</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
<tr class="odd">
<td>Big Files</td>
<td><p>Source: Images from the DICOM gateway and Clinical Capture workstations.</p>
<p>File extensions: BIG</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
<tr class="even">
<td>Abstract Files</td>
<td><p>Source: Images from the DICOM gateways, Clinical Capture workstations and Imports. Abstract files are derivatives of the TGA/BIG format files.</p>
<p>File extensions: ABS</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p>
<p>Recommended: 99999</p></td>
</tr>
<tr class="odd">
<td>Photo IDs / Advance Directives</td>
<td><p>Source: Patient photo images from the Clinical Capture workstations /Advance Directives</p>
<p>File extension: JPG</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p>
<p>Recommended: 99999</p></td>
</tr>
</tbody>
</table>

1.  Enter the number of days that each file type should remain on the shares based on the 3 file date purge criteria described in section *3.5.1 Purge Settings* (Date Accessed, Date Created, and Date Modified).

> Note: The FULL and BIG files are typically larger file sizes and consume more free space on the shares than the abstracts and photo IDs /Ad Direct.

2.  Due to their size, set the retention days to fewer days to free more space.
3.  Because the abstracts and photo IDs/Ad Direct are smaller files, set the retention days for purging these two types of files to a higher value than the values for the FULL/BIG file retention days.
4.  Because the abstract files are viewed as thumbnails on the Clinical Display workstation, set the retention days to retain a minimum of 5 years (1,825 days) on the shares regardless of the capacity of Tier 1 to make viewing on the Clinical Display workstations more efficient.

#### Configuring Scheduled/Express Purge Settings

![](vista-imaging-system-background-processor-user-manual/034.png)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto Purge</td>
<td>Enables the Purge to run when the high-water mark is reached on a RAID Group.</td>
</tr>
<tr class="even">
<td>Last Purge BP Server</td>
<td>BP Server on which the last purge was run.</td>
</tr>
<tr class="odd">
<td>Purge Factor</td>
<td>Multiple of the % Server Reserve. When the free space falls below this value, a purge is initiated on the next available online RAID Group. The default value is 2.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Express Purge Section</strong></td>
</tr>
<tr class="odd">
<td>Active</td>
<td>Enables an Express Purge.</td>
</tr>
<tr class="even">
<td>Purge Rate</td>
<td><p>When the number of image entries that have been evaluated for purging (based on the date criterion), without deletion, the purge process for that share will cease.</p>
<p>The default Purge Rate value is 100,000.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Scheduled Purge Section</strong></td>
</tr>
<tr class="even">
<td>Active</td>
<td>Enable scheduled purges.</td>
</tr>
<tr class="odd">
<td>Last Purge Date:</td>
<td>Date when the last purge was run.</td>
</tr>
<tr class="even">
<td>Frequency (in days)</td>
<td><p>The number of days added to the Last Purge Date to determine the next Scheduled Purge Date. This occurs at the end of a Scheduled Purge.</p>
<p>If this field is left blank, the Scheduled Purge can be scheduled for a single event. When the event takes place, the Next Purge Date is cleared.</p></td>
</tr>
<tr class="odd">
<td>Next Purge Date</td>
<td>Next scheduled Purge date.</td>
</tr>
<tr class="even">
<td>Purge Time</td>
<td>Time of day for the next scheduled Purge.</td>
</tr>
</tbody>
</table>

> Note: Before an automatic purge is set up, a manual purge should be run on a share to make sure the Purge Parameters are set properly.

> The automatic purge will use these same Purge Parameters and if not set properly, will result in unsatisfactory results. As the volume of images increases from the gateways, etc., these parameters should be adjusted to compensate for the increase.

> Scheduled purges typically are set up monthly, but this will vary per site. The goal is to keep the shares between 80% and 90% full. Some adjustments in scheduling will need to be made after a scheduled purge cycle has completed.

> Enabling Express Purge will greatly enhance the purging process by eliminating unnecessary file traversals that are not candidates for purging and thus significantly decrease the time to purge a share. The Purge Factor is set to control when the purge on a share is terminated. When the number of files that are traversed and not deleted has exceeded the number in the Purge Factor, the purge stops on that share and begins purging the next share (automatic mode).

#### Configuring Purge Date Criteria Settings

> ![](vista-imaging-system-background-processor-user-manual/035.png)

| Purge Criteria |                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------|
| Date Accessed      | Date when the file (image) was last viewed on a VI workstation.                                                   |
| Date Created       | Date when the file was copied to the current disk share.                                                          |
| Date Modified      | Date when the file was last changed. On the initial save, the Date Created will be the same as the Date Modified. |

Any of the three-file date/times can be used (date accessed, date modified, date created) to purge the shares. There have been instances where third-party utilities have changed the access dates on all the files it “touched” to the same recent date.

When the purge is activated, no files are deleted as none of the file access dates are purge candidates. It is recommended that the Date Modified be used. This date is retained when files are moved across storage media and is a reliable date for purging.

#### Running the Scheduled Purge

The Scheduled Purge option is used when the Purge is to be run at periodic intervals, for example, weekends (when activity is low at a site) or when images are to be kept on Tier 1 for a certain period, for example annual removal of images older than 5 years. The application that runs for the Scheduled Purge is the same as the Manual Purge. Reference the Manual Purge (above) for specific information about the GUI and log files.

> **NOTE:** Set the Purge Retention Days and Purge By as the Scheduled Purge process uses those parameters.

1.  Select Edit \> BP Servers.
2.  Drag the PURGE task to the BP Server where the purge is to be run (Best if run on an Imaging server).
3.  Click OK to close the window.
4.  Select Edit \> Purge / Verifier /RG Settings tab.
5.  Set the following fields:

| Field                 | Setting                        |
|---------------------------|------------------------------------|
| Auto Purge                | Unchecked                      |
| Express Purge \| Active   | Checked                        |
| Scheduled Purge \| Active | Checked                        |
| %Server Reserve           | *(not used for this option)*       |
| Purge Factor              | (*not used for this option)*       |
| Frequency (in days)       | *(select interval in days*)        |
| Next Purge Date           | *(starting date)*                  |
| Purge Time                | *(time of day the Purge will run)* |

6.  Click OK to close the window.

When a Scheduled Purge starts, the time is recorded in the VistA database in the field Last Purge Date. The Last Purge Date and the Next Purge Date are kept in synch, while the scheduled purge is active to prevent additional scheduled purges from being activated. When the scheduled purge is complete the Frequency is added to this date to determine when the purge will start next. All online Tier 1 shares in the next RAID Group will be purged when this scheduled application runs.

> **IMPORTANT:** The Queue Processor must be in the running state on the server where the Purge is scheduled for it to run i.e. the Start button on the Queue Processor GUI must be clicked.

#### Running the Auto Purge

There are two configurations where the Auto Purge is used:

- In the first configuration, all the Tier 1 shares are in the same RAID Group.
- In the second configuration, the shares are distributed into two or more RAID Groups. The setup is the same for both groups except that the Purge Factor must be set for the second configuration.

The application that runs for the Auto Purge is the same as the manual purge. Reference the Manual Purge (above) for specific information about the GUI and log files.

> **IMPORTANT:** If the PC that has Scheduled or Auto events is not a server class, the task will not start.

> **NOTE:** The Auto Purge process uses these parameters: Purge Retention Days and Purge By.

1.  Select Edit \> BP Servers.
2.  Drag the PURGE task to the BP Server where the purge is to be run (best if run on an Imaging server).
3.  Click OK to close the window.
4.  Select Edit \> Purge / Verifier /RG Settings tab.
5.  Set the following fields:

| Field                 | Setting                                          |
|---------------------------|------------------------------------------------------|
| Auto Purge                | Checked                                          |
| Express Purge \| Active   | Checked                                          |
| Scheduled Purge \| Active | Unchecked                                        |
| %Server Reserve           | *(use the current value that is set on your site)*   |
| Purge Factor              | 2 *(used only with multiple active RAID Groups)* |

6.  Click OK to close the window.

When any share in a *single* RAID Group configuration has less than the %Server Reserve free space, the Purge will start and process all the active shares in that group. On the *multiple* RAID Group configurations, the Purge will start on the next selectable RAID Group when the free space on any share in the current RAID Group falls below the Purge Factor times the % Server Reserve. This Purge Factor is set to allow time for the purge to complete on that next RAID Group before the Queue Processor changes the Current RAID Group to that group.

The Express Purge setting (described in a previous section) will dramatically lower the time it will take to purge a share/ RAID Group.

> **NOTE:** The Queue Processor must be in the running state for the Auto Purge to run on the designated server; i.e., the Start button must be clicked.

### Verifier Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier validates image storage pointers in VistA by checking the physical locations of those pointers to ensure the file(s) exist on the specific storage media. To maintain a valid database, corrective action is taken when these physical files are not found on the media. In addition to these file checks; the Verifier examines the integrity of the imaging records in VistA. Any corruption is reported in the log files.

#### Scheduled Verifier Settings

![](vista-imaging-system-background-processor-user-manual/036.png)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Last Verify BP Server</td>
<td>BP Server on which the Verifier was last run (Display only, set by application)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Scheduled Verifier</strong></td>
</tr>
<tr class="odd">
<td>Active</td>
<td>Enables scheduling the Verifier</td>
</tr>
<tr class="even">
<td>Check Text Files</td>
<td><p>Read text files on the Tier 1 shares and determine if:</p>
<ol type="1">
<li><p>the file is binary or unreadable</p></li>
<li><p>there are unprintable characters in the file</p></li>
<li><p>The SSN does not match the one in VistA</p></li>
<li><p>SOP Instance UID mismatch with VistA</p></li>
<li><p>Study Instance UID mismatch with VistA</p></li>
<li><p>SOP Instance UID and/or Study Instance UID are blank</p></li>
<li><p>SSN in the top part of the text file does not match the bottom.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Frequency (in days)</td>
<td>Number of days added to the date of the last time the Verifier application ran to determine the next time the Scheduled Verifier should be run.</td>
</tr>
<tr class="even">
<td>Last Verifier Date</td>
<td>Date when the Verifier was last run.</td>
</tr>
<tr class="odd">
<td>Next Verifier Date</td>
<td>Date of the next scheduled Verifier will run based on the Frequency (in days) parameter.</td>
</tr>
<tr class="even">
<td>Verifier Time</td>
<td>Time of day when the Verifier will run.</td>
</tr>
</tbody>
</table>

#### Guidelines for Setting Parameters for the Scheduled Verifier

The Scheduled Verifier should be set up to run nightly. It will verify the integrity of any image records not validated since the previous Verifier run (Manual or Scheduled). It is suggested that the Verifier be run manually over the entire range of image records before incremental Verifier runs are started. The application that runs for the Scheduled Verifier is the same as the Manual Verifier. Reference the Manual Verifier (above) for specific information about the GUI and log files.

The following guidelines for using the Scheduled Verifier will help maintain the integrity of the Imaging records in the VistA database.

> **IMPORTANT:** If the PC that has Scheduled or Auto events is not a server class, the task will not start.

- Set the Active check box to enable scheduled runs of the BP Verifier. The scheduled runs of the Verifier will only check the most recent VistA records of new images that have been created since the last Scheduled Verifier run.
- Do not select the Check Text Files check box. The contents of the text files on Tier 1 will be compared to the information in VistA. This processing will slow down the Verifier processing and utilities are not available now to correct any issues that surface.
- The Last Verifier Date field is set by the system and cannot be set by the user.
- When the Active parameter is checked, the Frequency (in days) field setting should be 1 so that the Verifier runs daily.
- Initially set the Next Verifier Date to today’s date. The scheduling frequency will be based on this date.
- Set the Verifier Time to an inactive period of the day –typically after hours when image creation activity is low.

#### Running the Scheduled Verifier

Use the following steps to schedule the Verifier:

1.  Select Edit \> BP Servers.
2.  Drag the SCHEDULED VERIFY task to the BP Server where the verifier is to be run.
3.  Click OK to close the window
4.  Select Edit \> Purge / Verifier /RG Settings tab
5.  Set the following fields in the Scheduled Verifier box:

| Field               | Setting                                                 |
|-------------------------|-------------------------------------------------------------|
| Active              | Checked                                                 |
| Check Text Files    | Unchecked                                               |
| Frequency (in days) | 1                                                       |
| Next Verifier Date  | *(starting date)*                                           |
| Verifier Time       | *(time of day the Verifier will run – after hours is best)* |

6.  Click OK to close the window.
7.  Click Start on the Queue Processor main window. (The Queue Processor must be in the running state for the Scheduled Verifier to run on the designated server.)

When a Scheduled Verifier starts, the time is recorded in the VistA database in the field Last Verifier Date. The Frequency is added to this date to determine when the Verifier will run again.

### RAID Group Advance Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RAID groups are used to organize Tier 1 shares into logical groups for easy tape backup and restore processing. During the install all existing online Imaging shares are placed into the first RAID Group RG-GO1. This configuration is the same that has been in existence for past years. The auto update functionality is also the same. At regular intervals, the current write location will change to the share with the freest space. The Auto-Write function will reset the current write location to provide load balancing within the RAID group. When the % Server Reserve within the group has been breached the Auto-Write will set the next RAID group as the current write group. In addition, when the used space in that RAID Group has reached the high-water mark, the next RAID Group that has online shares will become the current RAID Group.

#### Configuring the Scheduled RAID Group Advance Settings

![](vista-imaging-system-background-processor-user-manual/037.png)

| Field or Checkbox                | Description                                                                                                                                                                                                             |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduled RAID Group Advance box |                                                                                                                                                                                                                             |
| Active                               | Enable RAID Group Advance scheduling                                                                                                                                                                                        |
| Last RAID Advance                    | Date when the last scheduled RAID Group Advance occurred                                                                                                                                                                    |
| Frequency (in days)                  | Number of days added to the date of the last RAID Group Advance to determine the next time the RAID Group Advance will run. If the Frequency parameter is set, the next RAID Group Advance will be scheduled automatically. |
| Next Advance Date                    | Date of the next scheduled RAID Group Advance                                                                                                                                                                               |
| Advance Time                         | Required. Time of day of the next scheduled RAID Group Advance                                                                                                                                                              |

#### Parameter Guidelines for the Scheduled RAID Group Advance

Sites can choose a configuration that suits them best, as follows:

- Use the initial configuration where all the shares are in the same RAID Group. The new images will be evenly distributed among all the shares.
- Nightly incremental tape backups as well as monthly/quarterly tape backups must be done on a regular basis on all the shares.
- Distribute the shares among multiple RAID Groups. Fill the shares in each group to the Server Size, and then switch the current write group to the next. New image files will be distributed over all the shares assigned to that group.
- Nightly incremental tape backups as well as monthly/quarterly tape backups must be done only on that RAID Group.
- When it has reached capacity, a final full backup should be done on all the shares and nightly incremental tape backups and monthly/quarterly tape backups started on the next current write group.

#### Running the Scheduled RAID Group Advance

This option is applicable when the there are multiple active RAID Groups.

1.  Select the Edit \> Purge / Verifier /RG Settings tab.
2.  Set the following fields in the Scheduled RAID Group Advance box:

| Field           | Setting                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| Active              | Checked                                                                                      |
| Frequency (in days) | Set by determining how long a span of time images will be written to a set of shares in a Group. |
| Next Advance Date   | Set the starting date when the system will move to the next RAID Group.                          |
| Advance Time        | Set the starting time of day when the system will move to the next RAID Group.                   |

3.  Click OK to close the window.
4.  Click Start on the Queue Processor main window.  
    (The Queue Processor must be in the running state for the Scheduled RAID Group Advance to run on the designated server.)

## Queue Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Queue Processor is tasked by other Imaging products and external sources to perform various activities with new images emanating from those sources. These tasks are placed on a queue structure (FIFO with each type of task) in VistA. These tasks are described in section *2.5.3, Assigning Tasks (Queues) to a BP Server*.

> **NOTE:** To execute these tasks, they must be assigned to a BP Server. This can be done using the BP Servers window which is an option on the main BP window.

The Queue Manager window shows each of the queues that have been assigned to a server. It displays Failed and Active status categories under each task. The Active branches show unprocessed entries for new images. The Queue Processor executes each task in a priority order starting with JBTOHD as the highest. When a queue entry for a task does not complete successfully, it is placed on the Failed list for that task. The error condition is listed below the Failed entry in the tree. There can be different reasons for the failure for each task. Each one is listed in the Queue Manager tree.

The Queue Manager displays the status counts (Active/Failed) for each task as well as details about the entry. In the Queue Manager the queues are subdivided into a tree structure. The lowest node of the tree represents an individual queue file entry. You can move the active queue pointer to entries anywhere in the queue list for a task. The Queue Processor will process entries from this new location. In addition, you can re-queue Failed tasks and delete tasks from both the Active and Failed queue lists.

### Queue Manager Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit \> Queue Manager menu on the Queue Processor menu bar opens the Queue Manager main window. You can select to display either all queues or a specific queue by choosing the relevant option from the submenu. The data is loaded in batches preventing failures.

Displaying a specific queue type allows you to limit the data that is displayed preventing large arrays from causing timeouts or out of memory errors.

To display all queues:

From the main BP Queue Processor window, with the Queue Processor stopped, select  
Edit \> Queue Manager \> All.

![](vista-imaging-system-background-processor-user-manual/038.png)

All queue types display grouped by queue type and status (Failed or Active). Click the plus sign to display the next level of detail. Hovering on a queue displays a tooltip with details about the queue.

![](vista-imaging-system-background-processor-user-manual/039.png)

To select a queue to display:

From the main BP Queue Processor window, with the Queue Processor stopped, select  
Edit \> Queue Manager \> *Queue* where *Queue* is the queue type and can be Abstract, Delete, GCC, Import, JBTOHD, Jukebox, and Prefet.

When the queues of the type display, you can carry out certain operations on individual queues through the shortcut menu. The operations that you can carry out depend on the type and status of the queue or queues.

The following image shows the Jukebox queues with a failed queue selected. The shortcut menu is displayed with the two operations available for this queue: Re-Queue and Purge Queue.

![](vista-imaging-system-background-processor-user-manual/040.png)

### Purging a Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Circumstances may arise when single or multiple queue entries need to be deleted. One example involves JBTOHD tasks. When JBTOHD entries have not been processed in a period (a day or more), the usefulness of retrieving these images diminishes. There may be hundreds of these queue entries for a study. You can select multiple entries using the Queue Manager and delete them.

1.  Select the entries to be deleted.
2.  Right click in the selected area.
3.  In the pop-up menu displayed, select Purge Queue.  
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.

> ![](vista-imaging-system-background-processor-user-manual/041.png)

4.  Acknowledge the verification popup. The entries will be deleted and the Active/Failed queue count will be changed to reflect the change.

### Re-Queuing a Failed Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Queue Processor will attempt to process an entry three times to get a successful result. After the third attempt, the entry is placed in the Failed category. In most cases, the cause of the failure can be corrected and the Failed entry re-queued with success.

1.  Right-click a Failed status and select Re-Queue from the pop-up menu to re-queue the single queue or all queues with that status, as shown in the example.  
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.

> ![](vista-imaging-system-background-processor-user-manual/042.png)

2.  Click Yes in the confirmation message.  
      
    The queue entry will move from the Failed queue to the Active queue for that task. The queue counts will be updated.

### Refreshing a Queue Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vista-imaging-system-background-processor-user-manual/043.png)

After working with queues, the state of the queue file will have changed due to real time captures and possibly activity by the sites’ other Queue servers. The Queue Manager operator can select the Refresh submenu option to get an updated view of the queue selected. It would be prudent not to manage queues that are actively being processed by another queue processor to avoid errors in the updating queues that may no longer be there.

### Setting a Queue Partition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each queue type has an active queue pointer that designates the next queue to be processed. This pointer can be manually moved to begin processing at another location in the specific queue type. A typical situation is when a queue is corrupted. The queue pointer can be moved to the next queue where processing continues with the rest of the queues of that type.

1.  To move the active queue pointer (Set Queue Partition), right-click an active queue.  
    Note: This pop-up menu can also be accessed from the keyboard by using Shift + F10.

> ![](vista-imaging-system-background-processor-user-manual/044.png)

2.  From the pop-up menu, select Set Queue Partition.  
    The selected entry and the ones above it will move to the Failed queue.

> ![](vista-imaging-system-background-processor-user-manual/045.png)

### Accessing Import Queue Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can access the failed Import Queue properties by right-clicking a failed IMPORT queue node and selecting Import Queue Properties.  
> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

> ![](vista-imaging-system-background-processor-user-manual/046.png)

For details, see section *4.6.3.3, IMPORT Queue Status Report*.

## Network Location Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP processor applications send/receive images to/from physical devices and networks using different types of media. These types of media need to be recorded in the VistA database. The information that is stored includes the type of media, the location, online status, security access, etc. This information can be entered into VistA using the Network Location Manager.

![](vista-imaging-system-background-processor-user-manual/047.png)

## Configuring the Network Location Manager 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit \> Network Location Manager menu on the Queue Processor menu bar opens the Network Location Manager window. Seven types of entries are displayed using the tabs. They are described in the table.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Tier 1</td>
<td><p>Tier 1 shares on the Imaging server cluster.</p>
<p><strong>Note</strong>: Use “XXX-MAGnH” names for these shares. “n” is a unique number. “H” indicates the file directory structure is hashed “XXX-MAGc-nnH” names for these shares. “c” is the cluster number. “nn” is the image share.</p></td>
</tr>
<tr class="even">
<td>Tier 2</td>
<td><p>Cache shares on the archive device (Storage Grid/Archive Appliance/Jukebox)</p>
<p><strong>Note</strong>: Use “WORMOTGn” names for JB and AA. Use “XXX-GWV0n-SGnn” for SG locations, where XXX is the site abbrev, n is the proper number describing the location.</p></td>
</tr>
<tr class="odd">
<td>Routers</td>
<td><p>Network shares on remote servers/desktops where new images are transmitted using the Imaging AutoRouter product.</p>
<p>Security: Access to these locations requires a Windows Username and Password.</p>
<p><strong>Note</strong>: Use meaningful names as these names are used in the routing rules file (ROUTE.DIC) on the routing gateways.</p></td>
</tr>
<tr class="even">
<td>GCC</td>
<td><p>External network shares where images can be transferred for non-VistA Imaging usage.</p>
<p>Security: Access to these locations requires a Windows Username and Password.</p></td>
</tr>
<tr class="odd">
<td>EKG</td>
<td><p>Remote GE Muse server share locations where the Electrocardiograms are stored. The EKG strips can be viewed from these remote locations using the Clinical Display software.</p>
<p>Security: Access to these locations requires a Windows Username and Password.</p></td>
</tr>
<tr class="even">
<td>URLs</td>
<td>Remote Image Views is a feature of the Clinical Display software that allows users to view patient images from any VA hospital in the country. These images are processed through a web service on remote server. The URL for this web service is stored here.</td>
</tr>
<tr class="odd">
<td>Diagrams</td>
<td>Annotation diagrams (templates and mark-ups) are stored at these share locations. The Clinical Display software has a tool that can be used to edit and save these marked-up diagrams for a patient.</td>
</tr>
</tbody>
</table>

#### Tier 1 Tab 

Each site has Imaging Tier 1 storage where images from the gateways, scanners, cameras, etc. are stored for quick access for display on VistARad and Clinical Display workstations. This storage resides on the Imaging cluster. Shares can have different capacities for storage. The physical location for each of these shares is stored under the Tier 1 storage type in the Network Location Manager.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/048.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>Name of a Tier 1 share on the Imaging cluster.</p>
<p><strong>Note</strong>: Use “MAGnH” names for these shares. “n” is a unique number. “H” indicates the file directory structure is hashed or use “XXX-MAGc-nnH” names for these shares. “c” is the cluster number. “nn” is the image share.</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location.</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>The UNC (Universal Naming Convention) containing the server and share name for the Tier 1 storage.</td>
</tr>
<tr class="even">
<td>TOTAL SPACE</td>
<td>Storage capacity for the share.</td>
</tr>
<tr class="odd">
<td>FREE SPACE</td>
<td>Free space remaining on the share.</td>
</tr>
<tr class="even">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the share (“ONLINE" or “OFFLINE”).</td>
</tr>
<tr class="odd">
<td>READ ONLY</td>
<td>If set, data can be read but not written to this share. In addition, Purge and Auto Write will not consider this share as a candidate for purge or new image storage.</td>
</tr>
<tr class="even">
<td>STORAGE TYPE</td>
<td>“Tier 1” formerly: RAID</td>
</tr>
<tr class="odd">
<td>HASH SUBDIRECTORY</td>
<td>A hierarchal folder structure will be created/used (default is hashed, display only).</td>
</tr>
</tbody>
</table>

#### Tier 2 Tab 

Most sites have local Tier 2 storage (jukebox). Some sites have a remote archive where multiple sites share the same storage. The images that are initially copied to Tier 1 are copied from the Tier 1 to Tier 2. The Tier 2 devices have one or more shares where the images are copied for long term storage. For remote consolidated Tier 2 storage, each site has its own share to keep the images segregated.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/049.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>Name of a share on the server containing the archive device.</p>
<p><strong>Note</strong>:</p>
<p>Use “WORMOTGn” names for JB and AA. Use “XXX-GWV0n-SGnn” for SG locations, where XXX is the site abbrev, n is the proper number describing the location.</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location.</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>The UNC (Universal Naming Convention) containing the server and share name for the archive storage.</td>
</tr>
<tr class="even">
<td>TOTAL SPACE</td>
<td>Storage capacity for the share.</td>
</tr>
<tr class="odd">
<td>FREE SPACE</td>
<td>Free space remaining on the share.</td>
</tr>
<tr class="even">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the share (“ONLINE" or “OFFLINE”)</td>
</tr>
<tr class="odd">
<td>STORAGE TYPE</td>
<td>“Tier 2” formerly Jukebox archive media.</td>
</tr>
<tr class="even">
<td>HASH SUBDIRECTORY</td>
<td>A flat or hierarchal folder structure will be created/used (default is hashed, display only).</td>
</tr>
</tbody>
</table>

#### Routers Tab

Some types of images are routed to remote Radiologists using the VistA Imaging AutoRouting software. These images are written to a share on their remote server using the Username/Password contained in the properties of this storage type.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/050.png)

![](vista-imaging-system-background-processor-user-manual/051.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>Name of a share on the remote Radiologist’s server</p>
<p><strong>Note</strong>: Use a name that reflects the location where these images will be sent. This name is used in the ROUTE. DIC file on the Routing Gateway.</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location.</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>The UNC (Universal Naming Convention) containing the server and share name for the remote storage location.</td>
</tr>
<tr class="even">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the share (“ONLINE" or “OFFLINE”).</td>
</tr>
<tr class="odd">
<td>STORAGE TYPE</td>
<td>“ROUTER”</td>
</tr>
<tr class="even">
<td>HASH SUBDIRECTORY</td>
<td>A flat or hierarchal folder structure will be created/used (default is hashed, display only).</td>
</tr>
<tr class="odd">
<td>ABSTRACT</td>
<td>Abstract files can be copied.</td>
</tr>
<tr class="even">
<td>FULL</td>
<td>Full files can be copied.</td>
</tr>
<tr class="odd">
<td>BIG</td>
<td>BIG files can be copied.</td>
</tr>
<tr class="even">
<td>DICOM</td>
<td>DCM files can be copied.</td>
</tr>
<tr class="odd">
<td>COMPRESSION</td>
<td>Data compression/decompression is used on the files being sent to the remote server. (Either none or JPEG-2000, found on the table, not on the properties page, can be edited by VA Fileman)</td>
</tr>
<tr class="even">
<td>USERNAME</td>
<td>Windows login Username for the remote server where the images will be sent. This account must have READ/WRITE access to the remote share.</td>
</tr>
<tr class="odd">
<td>PASSWORD</td>
<td>Windows login Password for the remote server where the images will be sent.</td>
</tr>
<tr class="even">
<td>MAX # RETRY ON CONNECT</td>
<td>Number of times that will be attempted to get a connection to the remote server using the AutoRouter software before a failure message is generated.</td>
</tr>
<tr class="odd">
<td>MAX # RETRY ON TRANSMIT</td>
<td>Number of times that a copy will be attempted to the remote server using the AutoRouter software before a failure message is generated.</td>
</tr>
<tr class="even">
<td>SYNTAX</td>
<td><p>“UNC”.</p>
<p>The connection to the share will be in the format \\server\share_name.(Found on the table, not on the properties page, can be edited by VA Fileman)</p></td>
</tr>
<tr class="odd">
<td>SUBDIRECTORY</td>
<td>Name of a subdirectory where files are to be stored. The value of this field is concatenated to the name of the network location (the 'physical name') to create the complete path-name.</td>
</tr>
<tr class="even">
<td>RETENTION PERIOD</td>
<td>Time in days that image files are kept on the remote server before they are purged.</td>
</tr>
<tr class="odd">
<td>LAST PURGE DATE</td>
<td>Date/time of last purge on the remote server.</td>
</tr>
<tr class="even">
<td>SITE</td>
<td><p>Name of the remote location.</p>
<p><strong>Note</strong>: Use a name different from the NETWORK LOCATION name. This string is displayed in VistARad in the “RC” column.</p></td>
</tr>
<tr class="odd">
<td>TIME OFFLINE</td>
<td>Date and time that this server was inaccessible. Set by the routing application, found on the table, not on the properties page.</td>
</tr>
</tbody>
</table>

#### GCC Tab

Photo ID images, etc. can be sent to a remote location directly from the Queue Processor software. These images are written to a share on the remote server using the Username/Password contained in the properties of this storage type.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/052.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>Name of a share on the server where the Photo ID, etc. will be sent.</p>
<p><strong>Note</strong>: Use names to reflect the type of transfer for these shares.</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location.</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>The UNC (Universal Naming Convention) containing the server and share name for the remote storage location.</td>
</tr>
<tr class="even">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the share (“ONLINE" or “OFFLINE”).</td>
</tr>
<tr class="odd">
<td>STORAGE TYPE</td>
<td>“GCC” for Global Carbon Copy (Displays as: EXPORT)).</td>
</tr>
<tr class="even">
<td>HASH SUBDIRECTORY</td>
<td>A flat or hierarchal folder structure will be created/used</td>
</tr>
<tr class="odd">
<td>User Name</td>
<td>IA User Name</td>
</tr>
<tr class="even">
<td>Password</td>
<td>IA Password</td>
</tr>
</tbody>
</table>

#### EKG Tab

The Clinical Display software has the capability to display EKG strips from local and remote MUSE servers. When a patient is selected, the software maps to these MUSE locations using the NET USERNAME field (#50) login in the IMAGING SITE PARAMETERS file (#2006.1) and looks for the patient data. When it finds the image data, it is copied from the MUSE server to the Display station and viewed by the user.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/053.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>Name of a share on the MUSE server where the EKG data is stored.</p>
<p><strong>Note</strong>: Use names to reflect the type of transfer for these shares.</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location.</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>The UNC (Universal Naming Convention) containing the MUSE server and share name.</td>
</tr>
<tr class="even">
<td>USER NAME</td>
<td>MUSE Network Administrator Name</td>
</tr>
<tr class="odd">
<td>PASSWORD</td>
<td>MUSE Network Administrator password (encrypted)</td>
</tr>
<tr class="even">
<td>STORAGE TYPE</td>
<td>“MUSE-EKG”</td>
</tr>
<tr class="odd">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the share (“ONLINE" or “OFFLINE”)</td>
</tr>
<tr class="even">
<td>MUSE SITE #</td>
<td>MUSE EKG network location number. Typically, a site with a single MUSE server that holds EKGs for one site would use 1.</td>
</tr>
<tr class="odd">
<td>MUSE VERSION #</td>
<td>MUSE software version</td>
</tr>
</tbody>
</table>

#### URLs Tab

The Remote Image Views functionality in the Clinical Display application uses a Network Location entry that points to the VistA Site Service to determine the server and port of remote VistA databases. This Network Location entry is a WEB service running on a centralized accessible server on the network.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/054.png)

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NETWORK LOCATION</td>
<td><p>The name of this WEB service.</p>
<p><strong>Note</strong>: suggested name- VISTASITESERVICE</p></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The record number in VistA for this Network Location</td>
</tr>
<tr class="odd">
<td>PHYSICAL REFERENCE</td>
<td>URL name of the location of the WEB service.</td>
</tr>
<tr class="even">
<td>OPERATIONAL STATUS</td>
<td>Logical state of the service (“ONLINE" or “OFFLINE”)</td>
</tr>
<tr class="odd">
<td>STORAGE TYPE</td>
<td>“URL”</td>
</tr>
</tbody>
</table>

#### Diagrams Tab

The Diagram Annotation tool is an optional Imaging component that is accessed from CPRS. The Diagram Annotation tool is used to annotate online diagram ‘templates’ and then save the results directly to a patient’s electronic medical record.

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/055.png)

| Field          | Description                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| NETWORK LOCATION   | The name of this template location.                                                                   |
| IEN                | The record number in VistA for this Network Location.                                                 |
| PHYSICAL REFERENCE | The UNC (Universal Naming Convention) containing the server and share name for the template location. |
| OPERATIONAL STATUS | Logical state of the service (“ONLINE" or “OFFLINE”).                                                 |
| STORAGE TYPE       | DIAGRAM                                                                                               |

### Adding a New Location to Network Location Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The following procedure applies to all the tabs in the Network Location Manager window.

1.  From the Queue Processor menu bar, select Edit \> Network Location Manager to open the following window.

> The Tier 1 tab is automatically selected.

2.  To add a new network location, click the New button at the bottom. The Network Location Properties window will be displayed.

> ![](vista-imaging-system-background-processor-user-manual/056.png)

3.  Type the Share Name.
4.  At the Network Share field, either type the path to the location where images are to be stored, or click the browse (…) button and specify the path.
5.  Select the appropriate option at the Storage Type field.
6.  Click Apply.

> Additional fields relevant to the storage type are displayed. The example below is for Storage Type Tier 1 only.

> Note: The STORAGE TYPE field is preselected depending on the Network Location tab selected. If the EKG tab is selected, then the STORAGE TYPE will be set to EKG, and so forth. However, the preselected value can be modified.

7.  Leave the Operational Status check box selected by default setting, or clear it.
8.  Leave the Read Only check box cleared by default setting or select it.
9.  Click Apply to add the changes to the database or click OK to add the changes and exit.

### Editing the Properties of a Network Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit the properties of a network location, right-click the entry and select Properties on the pop-up menu.

> **NOTE:** This pop-up menu can also be accessed from the keyboard by using Shift + F10.

![](vista-imaging-system-background-processor-user-manual/057.png)

1.  From the Queue Processor menu bar, select Edit \> Network Location Manager and select the appropriate tab.
2.  Right-click a row in a table grid and select Properties from the pop-up menu displayed above.  
    Note: only the properties applicable to the selected Storage Type are editable.

> The Network Location Properties dialog box is displayed. The Share Name and Network Share are displayed based on your selection.

> ![](vista-imaging-system-background-processor-user-manual/058.png)

3.  Modify any of the enabled settings.
4.  Click Apply and OK to add the changes to the database and exit or click OK to add the changes and exit.

### Adding a RAID Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Queue Processor menu bar, select Edit \> Network Location Manager to open the following window.

> The Tier 1 tab is automatically selected.

> ![](vista-imaging-system-background-processor-user-manual/059.png)

2.  Click the Add Group button at the bottom.

> A new RAID group is added to the tree. For this example, the name would be RG-ATG5.

### GCC Queue for PhotoID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GCC has a method for exporting photo IDs to a designated share as a post-capture process. Its implementation requires an entry in the IMAGE ACTIONS file (#2005.86). Its purpose is to export the files to a site specified print server or share either within the local area network or external to the local area network.

This protocol was requested by Indian Health Service (IHS) and called for the exported file to have the patient’s DFN included in the file name so that the operator could correctly assign a patient photo IDs.

To activate this functionality, create one or more GCC locations to receive the exported photo IDs using Network Location Manager. Edit the protocol in the IMAGE ACTIONS file (#2005.86) using Fireman.

Example:

VA FileMan 2\<.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 2005.86 IMAGE ACTIONS

(2 entries)

EDIT WHICH FIELD: ALL// ACTIVE

THEN EDIT FIELD: TAG

THEN EDIT FIELD: ROUTINE

THEN EDIT FIELD: TYPE (multiple)

EDIT WHICH TYPE SUB-FIELD: ALL//\<*enter\>*

THEN EDIT FIELD: EXPORT LOCATION

THEN EDIT FIELD: \<*enter\>*

STORE THESE FIELDS IN TEMPLATE: \<*enter\>*

Select IMAGE ACTIONS NAME: PHOTO-ID COPY

ACTIVE: NO// Y YES

TAG: PID//\<*enter\> \*\

ROUTINE: MAGQBGCC//\<*enter\>\*\

Select TYPE: PHOTO ID//\< *enter\>*

EXPORT LOCATION: *GCC21 \<\<\<this field points to the NETWORK LOCATION (#2005.2) file, select the network location to receive the exported image file.*

\*\*the TAG and ROUTINE fields are predefined by VistA Imaging patch MAG\*3.0\*39 with the routine to be used by the HIS. The files created at the exported location will be named using the patient DFN. If a site wishes to change this, they can use a locally defined routine.

# Queue Processor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- Application Description
- Setting up
- Tasking
- Understanding Processing
- Starting/Running the application
- Reports

====================================================================

3.  

## Application Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Queue Processor application is the main application in the BP product suite. It processes all the I/O operations between the Tier 1 shares and the Tier 2 device (jukebox). It is important that this process be monitored daily and kept running continuously. It performs the following tasks:

- Copies new images from the Tier 1 to Tier 2.
- Retrieves images from Tier 2 to Tier 1.
- Triggers Purge events (automatic and scheduled).
- Triggers Verifier events (scheduled).
- Manages disk space consumption specified by the Imaging Coordinator.
- Processes queue entries.
- Creates abstract files from Full/BIG files.
- Processes images from remote cameras and capture device in Clinical procedures.
- Copies images to remote destinations outside of Imaging.
- Watermarks images associated with a Rescinded Advance Directive with the text “Rescinded”.

## Setup Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Once the Queue Processor is installed, one or more BP Servers are required for processing.
- Tasks are assigned to each BP Server. One task cannot be assigned to multiple servers; however, a task can be assigned to any server to change the priority of processing.
- In addition to setting up the task assignments, there are various parameters that need to be set up as described in this document.
- Once the parameters are set up, the Queue Processor can be started to process active queue entries.

> **NOTE:** The Queue Processor runs without operator intervention and should operate continuously to keep pace with the workload. It should be monitored daily and it is highly recommended to task the BP Monitor utility. For details, see *Chapter 7 System Monitoring*.

## Tasking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Queue Processor has a set list of tasks that it performs. The specific requests for each task originate on the local Queue Processor or from another VistA Imaging product.

The process is as follows:

1.  These requests are sent to the VistA database and are stored on FIFO lists called queues.
2.  The Queue Processor dynamically checks these queues to determine if there is work to be completed.
3.  When an entry is found, the processing is started based on the queue type.
4.  When the processing is successfully completed, the queue count is decremented and the Queue Processor waits for another task to be sent.
5.  When the processing fails the entry is re-queued twice before it is placed on a failed queue for that task. Failed IMPORT queues must be manually re-queued; there is no retry.  
    Note: You will be required to investigate and determine the reason for the failure and re-queue the item once the problem is resolved.

When all the tasks are assigned to one server, the queues are processed in the following order of priority:

- JBTOHD (jukebox to hard drive) restores images to the Tier 1 shares from the Tier 2 device based on requests for viewing these images on display workstations or creating missing abstract files.

> Note: images can only be viewed from the Tier 1 shares.

> ![](vista-imaging-system-background-processor-user-manual/060.png)

- PREFET (pre-fetch) populates the Tier 1 shares with images that were requested on display workstations by users with the MAG PREFETCH security key.

> ![](vista-imaging-system-background-processor-user-manual/061.png)

- ABSTRACT creates thumbnail files with the .abs file extension, when this file type does not exist for an image set. These file derivatives only exist for certain types of files and can only be created when the Full or BIG files are present for an image set. See [Chapter 9](#Chapter_9) for additional information about the Abstract/Thumbnail maker.

> ![](vista-imaging-system-background-processor-user-manual/062.png)

- IMPORT provides a means for external applications to store images in the VistA Imaging environment using the IMPORT API. It also watermarks images associated with a Rescinded Advance Directive with the text “Rescinded”.

> ![](vista-imaging-system-background-processor-user-manual/063.png)

- JUKEBOX copies images from a Tier 1 share to Tier 2.

> ![](vista-imaging-system-background-processor-user-manual/064.png)

- DELETE removes images from the VistA Imaging shares. The DELETE queue is set when an end-user, who has the MAG DELETE security key, selects an image to be deleted in the Clinical Display software. Typically, these are images that are of poor quality or saved against the wrong patient.

> ![](vista-imaging-system-background-processor-user-manual/065.png)

- GCC (generic carbon copy) copies images to specified remote locations.

> ![](vista-imaging-system-background-processor-user-manual/066.png)

- EVAL entries are initiated by the DICOM Gateways to facilitate auto routing of images to remote display workstations.  
  Note: The EVAL queue is not processed by the BP Queue Processor but may be purged using the Queue Management by Type option.

> ![](vista-imaging-system-background-processor-user-manual/067.png)

## Understanding Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the BP Server tasks are set up and the parameters are set to the values determined by the site, click the Start button to start processing queue (task) entries. The processing steps for a typical JUKEBOX request are described below:

1.  When an image is processed by the DICOM Gateway or Clinical Capture workstation, the image file is copied to a Tier 1 share. The VistA record for that image is updated with the Tier 1 share location.
2.  The Clinical Workstation application or DICOM Image Gateway then requests that an image be saved to the jukebox by creating an entry in the JUKEBOX queue file on VistA. The queue entry identifies the file path, the origination of the file and other pertinent data that the Queue Processor will need to successfully complete the processing.
3.  When the JUKEBOX queue entry is processed, the image file is copied from the Tier 1 share to the Tier 2 device (jukebox) and the queue entry is deleted from the queue file. The queue count for the JUKEBOX queue is decremented to reflect the number of remaining queue entries to be processed.

## Starting/Running the Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Starting the Application and Analyzing the Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Windows Start \> Programs menu, select VistA Imaging Programs \> Background Processor \>Queue Processor.
2.  Log into the application using a valid VistA access and verify code.  
    Note: The secondary menu option All MAG\* RPC's \[MAG WINDOWS\] is required for access to the Queue Processor.

> The Queue Processor application window opens.

> ![](vista-imaging-system-background-processor-user-manual/068.png)

3.  Click the Start button in the upper right-hand corner.

> If the Queue Processor is not properly configured, the application will send alert messages. Review the steps in section *2.5 Configuring BP Servers*.

4.  After one or two minutes, click the Stop button and view the populated fields.  
    If no queues have entries, only the storage statistics are displayed in the VistA Storage section of the window.

> The following example shows a sample output of processed activity. The queues being processed are displayed under the Start button.

> ![](vista-imaging-system-background-processor-user-manual/069.png)

VistA Storage

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Network Location Name</td>
<td>Name of the entry in the NETWORK LOCATION file</td>
</tr>
<tr class="even">
<td>Storage Type</td>
<td><p>Types of storage:</p>
<p>Tier 1</p>
<p>Tier 2</p>
<p>Group (GRP)</p>
<p><strong>Note</strong>: These types are also defined in the Network Location Properties dialog box.</p></td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Internal Entry Number in the NETWORK LOCATION file for the Storage Type device</td>
</tr>
<tr class="even">
<td>Free Space</td>
<td>Disk free space available in megabytes</td>
</tr>
<tr class="odd">
<td>Disk Size</td>
<td>Disk space capacity in megabytes</td>
</tr>
<tr class="even">
<td>Share Path</td>
<td>UNC path of the share</td>
</tr>
<tr class="odd">
<td>RAID Group</td>
<td>RAID share group name</td>
</tr>
<tr class="even">
<td colspan="2"><strong>(Queue Activity box)</strong></td>
</tr>
<tr class="odd">
<td>Queue</td>
<td>Name of the queue identifying the task being processed</td>
</tr>
<tr class="even">
<td>Active</td>
<td>Number of active files to be processed</td>
</tr>
<tr class="odd">
<td>Failed</td>
<td>Number of files that failed in processing. Failed queues should be checked. For details, see <em>Chapter 8 Troubleshooting.</em></td>
</tr>
<tr class="even">
<td colspan="2"><strong>BP Event Log - <em>{log file location}</em></strong></td>
</tr>
<tr class="odd">
<td>Event Time</td>
<td>Date and time of the last run of the log</td>
</tr>
<tr class="even">
<td>Process: Queue IEN</td>
<td>Queue type, queue number, and status check info</td>
</tr>
<tr class="odd">
<td>Process Status</td>
<td>Source and destination of each file transfer, creation, or deletion</td>
</tr>
</tbody>
</table>

### Delay Between Queue Processing.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th>Icon</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>On the BP Main window, there is a panel to the left of the Start button. It shows the time of day.</td>
<td>![](vista-imaging-system-background-processor-user-manual/070.png)</td>
</tr>
<tr class="even">
<td><p>If the user double–clicks on the time of day, a panel with a list of selectable delays will show. The user will not have to stop the BP. The entries in the list are in milliseconds (ms).</p>
<p>When the BP is started, 1000 ms is selected. The user can select a different delay to speed up the processing of queues.</p></td>
<td>![](vista-imaging-system-background-processor-user-manual/071.png)</td>
</tr>
<tr class="odd">
<td>The Delay pane can be shown by clicking on the menu option: Edit | Set Queue pause (delay)</td>
<td>![](vista-imaging-system-background-processor-user-manual/072.png)</td>
</tr>
<tr class="even">
<td>If there are “0” active queues, the phrase “(0 Active)” will be displayed and the delay will change to 3 seconds. When there are active queues, the “(0 Active)” will be hidden, and the delay will change back to what is selected in the Delay drop down list.</td>
<td>![](vista-imaging-system-background-processor-user-manual/073.png)</td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>Note:</strong> The time of day has been added as a visual indicator that the BP is running and isn't hung or frozen. The time of day is updated every second (or every 3 seconds if there are 0 active queues).</p>
<p>The time of day will switch between being underlined and not underlined every time the BP checks VistA for queues to process as another visual indicator that the BP is running. The entries in the list of queues will not be highlighted and will not flash anymore as the list is updated.</p></td>
</tr>
</tbody>
</table>

### Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help is available from different sources:

- Queue Processor GUI
- Hovering the cursor over the application window and pressing the F1 key
- Selecting Help from the menu bar
  - Call customer support at the National Helpdesk.

> Note: Be sure to have the information shown in the example of the table that follows and a copy of the most recent log files.

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version</td>
<td>Software version, build number and CRC number.</td>
</tr>
<tr class="even">
<td>C:\Program Files\VistA\Imaging\<br />
BackProc\Magbtm.exe</td>
<td>Location of the Background Processor executable on your hard drive.</td>
</tr>
<tr class="odd">
<td>6030 KB {<em>date}</em></td>
<td>File size and date of executable.</td>
</tr>
<tr class="even">
<td>Mag_MakeAbs.exe</td>
<td>Executable and version number of the ABSTRACT queue used to create the abstracts (thumbnails) of images.</td>
</tr>
<tr class="odd">
<td>System Installations</td>
<td>Version and installation date of Imaging patches.<br />
<strong>Note</strong>: The latest patch is listed at the bottom.</td>
</tr>
</tbody>
</table>

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three types of output are produced to notify users of important occurrences:

- Log files
- Emails
- Screen-generated output

### Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New log files are created as HTML files at the beginning of every session. HTML files are viewable, printable, and searchable. By default, the BP Queue Processor log files reside in the C:\Program Files\VistA\Imaging\BackProc\log\BackProc directory. These files can be accessed by:

- Selecting File \> Open Log on the BP Queue Processor menu bar
- Using an internet browser

> **NOTE:** The log files can be imported into an Excel spreadsheet.

> **IMPORTANT:** These files should be kept for historical/troubleshooting reasons and added to the tape backup process to safeguard the files. (See *Appendix B: Backups* in the *VistA Imaging System Installation Guide.*)

#### Log File Format

BP Queue Processor log files are archived as HTML files and have the year-month-day and sequence number imbedded in the file name, as shown in the right pane of the window.

![](vista-imaging-system-background-processor-user-manual/074.png)

If more than one log file is run on the same day, the system adds a sequence number such as “01” following the date in the file name. For multiple runs on the same day, the highest sequence number is the latest log file run for the day.

The Queue Processor produces multiple log files for a processing run. Each file contains different information.

#### BackProc Log

The BackProc.log file records all activity in the Event Log section in the Queue Processor window.

> ![](vista-imaging-system-background-processor-user-manual/075.png)

| Name        | Description                                               |
|-----------------|---------------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed         |
| Event_Queue_Ref | Queue name and entry number and status check info             |
| Message/Path    | Description of action taken (or statistics for status checks) |

#### BP Error Log

The BPError.log file records error conditions with the operating system and Broker.

![](vista-imaging-system-background-processor-user-manual/076.png)

| Name        | Description                                       |
|-----------------|-------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed |
| Event_Queue_Ref | Error category                                        |
| Message/Path    | Description of error condition                        |

### Email Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following messages, listed in alphabetical order<u>,</u> are generated or triggered by the Queue Processor.

> **IMPORTANT:** Be sure to add the local Image support staff person to the local MAG SERVER mail group, and at least one pager number in the MEMBERS REMOTE multiple.

#### Ad_Hoc_Image_Site_Usage 

This message is sent when the menu option Ad hoc Enterprise Site Report \[MAG ENTERPRISE\] is used and it has completed gathering information.

Example:

> Subj: Ad Hoc Image Site Usage: SALT LAKE CITY^660 \[#31177\] 10/14/09@15:20

> 168 lines

> From: IMAGPROVIDERONETWOSIX,ONETWOSIX In 'IN' basket. Page 1

> ------------------------------------------------------------------------

> SITE: SALT LAKE CITY^660

> Reporting Period: Jul 06, 2009 - Oct 14, 2009

> DATE: OCT 14, 2009@15:20:48 EST

> DOMAIN: IMGxxxxx.REDACTED

> 2005 ENTRIES: 17805

> 2006.81 ENTRIES: 5

> Production Account: 0

> WS DIS VERS: 3.0.59.31^Win XP.5.1.2600^1

> WS DIS VERS: 3.0.72.30^Win Server.5.2.3790^1

> WS CAP VERS: 3.0.72.30^Win XP.5.1.2600^1

#### Application Process Failure 

This message is sent by several of the Imaging applications when the PLACE value cannot be resolved for the image entry. The PLACE value is a valid entry in the IMAGING SITE PARAMETERS file (#2006.1) or a value in the ASSOCIATED INSTITUTION field (#.04) of this file.

Example:

> Subj: Application process failure \[#846445\] 23 Oct 2009 09:45:30 -0400 (EDT)

> 18 lines

> From: \<xxx@DETROIT. REDACTED \>

> --------------------------------------------------------------------

> SITE: DETROIT. REDACTED

> DATE: OCT 23, 2009@09:45:30 EDT

> Cannot determine 'place' (location, division, institution) for image.

> At: GETPLACE+5^MAGBAPI +3 = I 'PLACE,\$\$MAXREP(10) D

> Called From: PLACE+1^MAGBAPI +1 = Q \$\$GETPLACE(+\$O(^MAG(2006.1,"B",IEN,""))

Application Process Failure messages are generated when the Imaging system cannot determine which Imaging platform to use because it cannot identify the division of either the user or of the image.

- Division of user not clear – This indicates that there is not cross reference for the Imaging user (DUZ(2)) in the SITE PARAMETER file (#2006.1). To correct this, the VistA Imaging administrator must define the ASSOCIATED INSTITUTION field (#.04) for that user (DUZ(2)) in the SITE PARAMETER file (#2006.1).
- Division of image not clear – When the storage software (the Background Processor Verifier or the Background Processor Purge) cannot determine the division of an image it is attempting to store the VistA Imaging administrator must define the division in the ACQUISITION SITE field (#.05) in either the IMAGE file (#2005) or the IMAGE ARCHIVE file (#2005.1).

> Example 1: Background Processor Verifier Application Process Failure Message

> Subj: Application process failure \[#52970\] 12/19/12@13:46 23 lines

> From: VistA Imaging \$\$GETPLACE_MAGBAPI In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> SITE: IMGDEM01. REDACTED

> DATE: Dec 19, 2012@13:46:08 EST

> Production Account: 0

> At: GETPLACE+5^MAGBAPI +3 = I 'PLACE,\$\$MAXREP(10) D

> Called From: PLACE+1^MAGBAPI +1 = Q \$\$GETPLACE(+\$O(^MAG(2006.1,"B",IEN,"")))

> Called From: CNP2+27^MAGQBPG1 +1 = . S PLACEOK=\$S(\$\$PLACE^MAGBAPI(+ACQSITE)=\$\$

> PLACE^MAGBAPI(\$G(DUZ(2))):1,1:"")

> Called From: CNP2+20^MAGQBPG1 +3 = F D SCAN^MAGQBPG1(.IEN,ORDER,.GL) D Q:(((

> 'OFFLINE)&PLACEOK)!('IEN)!(\$P(RESULT,U,21)="DUPE")!'\$G(ACQSITE))

> Called From: CAPI+11^XWBBRK2 +1 = D @R

> Called From: CALLP+18^XWBBRK +1 = . D CAPI^XWBBRK2(.XWBP,XWB(2,"RTAG"),XWB(2,"

> RNAM"),S)

> Called From: CALLP+15^XWBBRK +3 = IF '+ERR,(+S=0)!(+S\>0) D

> Called From: MAIN+30^XWBTCPC +1 = . . D CALLP^XWBBRK(.XWBR,XWBTBUF)

> Called From: MAIN+26^XWBTCPC +2 = . IF TYPE D

> Called From: MAIN+2^XWBTCPC +2 = F D Q:XWBTBUF="#BYE#"

> Called From: RESTART+3^XWBTCPC +2 = U XWBTDEV D MAIN

> XWBTBUF: 007XWB;;;;000420MAGQ JBSCN^000250020000503305005033050010

> MAGDA: 3305

> This is the new example 1(from Feb. 1, 2013)

> Subj: Application process failure \[#52970\] 12/19/12@13:46 23 lines

> From: VistA Imaging \$\$GETPLACE_MAGBAPI In 'WASTE' basket. Page 1

> -------------------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Dec 19, 2012@13:46:08 EST

> Production Account: 0

> At: GETPLACE+5^MAGBAPI +3 = I 'PLACE,\$\$MAXREP(10) D

> Called From: PLACE+1^MAGBAPI +1 = Q \$\$GETPLACE(+\$O(^MAG(2006.1,"B",IEN,"")))

> Called From: CNP2+27^MAGQBPG1 +1 = . S PLACEOK=\$S(\$\$PLACE^MAGBAPI(+ACQSITE)=\$\$

> PLACE^MAGBAPI(\$G(DUZ(2))):1,1:"")

> Called From: CNP2+20^MAGQBPG1 +3 = F D SCAN^MAGQBPG1(.IEN,ORDER,.GL) D Q:(((

> 'OFFLINE)&PLACEOK)!('IEN)!(\$P(RESULT,U,21)="DUPE")!'\$G(ACQSITE))

> Called From: CAPI+11^XWBBRK2 +1 = D @R

> Called From: CALLP+18^XWBBRK +1 = . D CAPI^XWBBRK2(.XWBP,XWB(2,"RTAG"),XWB(2,"

> RNAM"),S)

> Called From: CALLP+15^XWBBRK +3 = IF '+ERR,(+S=0)!(+S\>0) D

> Called From: MAIN+30^XWBTCPC +1 = . . D CALLP^XWBBRK(.XWBR,XWBTBUF)

> Called From: MAIN+26^XWBTCPC +2 = . IF TYPE D

> Called From: MAIN+2^XWBTCPC +2 = F D Q:XWBTBUF="#BYE#"

> Called From: RESTART+3^XWBTCPC +2 = U XWBTDEV D MAIN

> XWBTBUF: 007XWB;;;;000420MAGQ JBSCN^000250020000503305005033050010

> MAGDA: 3305

Example 2: Background Processor Purge Application Process Failure Message

> Subj: Application process failure \[#52971\] 12/19/12@15:12 22 lines

> From: VistA Imaging \$\$GETPLACE_MAGBAPI In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Dec 19, 2012@15:12:15 EST

> Production Account: 0

> At: GETPLACE+5^MAGBAPI +3 = I 'PLACE,\$\$MAXREP(10) D

> Called From: PLACE+1^MAGBAPI +1 = Q \$\$GETPLACE(+\$O(^MAG(2006.1,"B",IEN,"")))

> Called From: FILEREF+77^MAGQBPRG +1 = I PLACE'=\$\$PLACE^MAGBAPI(+\$P(\$G(^MAG(200

> 5,IEN,100)),U,3)) D Q

> Called From: CAPI+11^XWBBRK2 +1 = D @R

> Called From: CALLP+18^XWBBRK +1 = . D CAPI^XWBBRK2(.XWBP,XWB(2,"RTAG"),XWB(2,"

> RNAM"),S)

> Called From: CALLP+15^XWBBRK +3 = IF '+ERR,(+S=0)!(+S\>0) D

> Called From: MAIN+30^XWBTCPC +1 = . . D CALLP^XWBBRK(.XWBR,XWBTBUF)

> Called From: MAIN+26^XWBTCPC +2 = . IF TYPE D

> Called From: MAIN+2^XWBTCPC +2 = F D Q:XWBTBUF="#BYE#"

> Called From: RESTART+3^XWBTCPC +2 = U XWBTDEV D MAIN

> <span class="mark">XWBTBUF</span>: 007XWB;;;;001160<span class="mark">MAGQBP FREF</span>^000980400\\VHAISWIMGS1\IMAGE6\$\DM00\00\00\\

> 00\33\0190DM000000003305.ABS0040abs0230\\VHAISWIMGS1\IMAGE6\$\\

> <span class="mark">MAGDA: 3305</span>

> This is the new example 2(from Feb. 1, 2013)

> Subj: Application process failure \[#52971\] 12/19/12@15:12 22 lines

> From: VistA Imaging \$\$GETPLACE_MAGBAPI In 'WASTE' basket. Page 1

> -------------------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Dec 19, 2012@15:12:15 EST

> Production Account: 0

> At: GETPLACE+5^MAGBAPI +3 = I 'PLACE,\$\$MAXREP(10) D

> Called From: PLACE+1^MAGBAPI +1 = Q \$\$GETPLACE(+\$O(^MAG(2006.1,"B",IEN,"")))

> Called From: FILEREF+77^MAGQBPRG +1 = I PLACE'=\$\$PLACE^MAGBAPI(+\$P(\$G(^MAG(200

> 5,IEN,100)),U,3)) D Q

> Called From: CAPI+11^XWBBRK2 +1 = D @R

> Called From: CALLP+18^XWBBRK +1 = . D CAPI^XWBBRK2(.XWBP,XWB(2,"RTAG"),XWB(2,"

> RNAM"),S)

> Called From: CALLP+15^XWBBRK +3 = IF '+ERR,(+S=0)!(+S\>0) D

> Called From: MAIN+30^XWBTCPC +1 = . . D CALLP^XWBBRK(.XWBR,XWBTBUF)

> Called From: MAIN+26^XWBTCPC +2 = . IF TYPE D

> Called From: MAIN+2^XWBTCPC +2 = F D Q:XWBTBUF="#BYE#"

> Called From: RESTART+3^XWBTCPC +2 = U XWBTDEV D MAIN

> XWBTBUF: 007XWB;;;;001160MAGQBP FREF^000980400\\VHAISWIMGS1\IMAGE6\$\DM00\00\00\\

> 00\33\0190DM000000003305.ABS0040abs0230\\VHAISWIMGS1\IMAGE6\$\\

> MAGDA: 3305

> The USER was: IMAGPROVIDERONETWOSIX,ONETWOSIX DUZ: 126

Key elements are used in the messages generated by the Background Processor components to identify the Internal Entry Number (IEN) of the image and the storage application that generated the message. These elements and their values are highlighted in the examples.

- The value of the label XWBTBUF contains the Remote Procedure call associated with the storage application.

> The value of MAGQJBSCN in Example 1 indicates that the storage application is the Background Processor Verifier.

> <span class="mark">XWBTBUF</span>: 007XWB;;;;000420<span class="mark">MAGQ JBSCN</span>^000250020000503305005033050010

> The value of MAGQBP in Example 2 indicates that the storage application is the Background Processor Verifier.

> <span class="mark">XWBTBUF</span>: 007XWB;;;;001160<span class="mark">MAGQBP FREF</span>^000980400\\VHAISWIMGS1\IMAGE6\$\DM00\00\00\\

- The value of the labels MAGDA, MAGGDA, and MAGIEN is the image IEN.

> In Example 1, the value of the label MAGDA indicates that the IEN of the image is 3305.

> <span class="mark">MAGDA: 3305</span>

> In Example 2, the value of the label MAGDA indicates that the IEN of the image is 3305.

> <span class="mark">MAGDA: 3305</span>

#### Auto_RAID_Group_Purge 

This message is sent by the Queue Processor when the following conditions occur:

- The Scheduled RAID Advance Group is scheduled and the Auto Purge is set.
- The next share in the RAID group reaches the Percent Server Reserve and a purge is automatically started.

Example:

> Subj: Auto_RAID_group_purge \[#31180\] 10/27/09@15:04 2 lines

> From: VistA Imaging Auto_RAID_group_purge In 'IN' basket. Page 1 \*New\*

> -----------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Oct 27, 2009@15:04:37 EST

#### GCC Copy Error 

This message is sent during processing when GCC queues have connectivity problems.

Example:

> Subj: GCC Copy Error \[#31157\] 10/07/09@20:36 6 lines

> From: VistA Imaging GCC Queue Error In 'IN' basket. Page 1 \*New\*

> --------------------------------------------------------------------

> SITE: IMGxxx.REDACTED

> DATE: Oct 07, 2009@20:36:22 EST

> "The GCC queue processor is having difficulty copying files to the network location. The last copy attempt failed 3 times with an error status of : \\VHAxxxx400\GCC24\$: Cannot connect to the Export Share. The next notification will occur in 6 hours.

#### Get_Next_RAID_Group_Failure 

This message is sent by the Queue Processor when the Scheduled RAID Advance is set and it cannot advance to the next RAID Group perhaps because all the shares in the group are set to READ ONLY or there is a connectivity problem.

Example:

> Subj: Get_Next_RAID_Group_failure \[#31173\] 10/27/09@13:51 4 lines

> From: VistA Imaging Get_Next_RAID_Group_failure In 'IN' basket. Page 1 \*New\*

> -----------------------------------------------------------------------

> SITE: IMGxxxx.REDACTED

> DATE: Oct 27, 2009@13:51:46 EST

> Production Account: 0

> The get next raid group function failed!

#### Image_Cache_Critically_Low 

This message is sent by the Queue Processor when it determines that the cache is below the Percent Server Reserve factor and the Auto Purge has not been set.

Example:

> Subj: Image Cache Critically Low at \[#31158\] 10/07/09@21:40 22 lines

> From: BACKGROUND,USER I In 'IN' basket. Page 1

> ----------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Oct 07, 2009@21:40:01 EST

> SENDER: SALT LAKE CITY Imaging Background Processor

> Total Cache Free: VistA Imaging RAID storage is Critically Low gigabytes

> Total Cache Available: 2131 gigabytes

> The Automatic Purge process is NOT configured. The 4 Imaging cache servers will require operator intervention to ensure continued availability. The following MAG SERVER members are being notified:

> IMAGPROVIDERONETWOSIX,ONETWOSIX

> IMAGPROVIDERONETHREETHREE,ONETHREETHREE

> The next notifications will occur in: 0 hours.

#### Image_File_Size_Variance

This message is sent during a purge when a file on Tier 1 has met the criterion for deletion but the copy of this file on the jukebox is a different size.

Example:

> Subj: Image File Size Variance: \[#852162\] 2 Dec 2009 16:28:45 -0500 (EST)

> 6 lines

> From: Image_File_Size_Variance In 'IN' basket. Page 1 \*New\*

> -------------------------------------------------------------------------------

> SITE: IMGxxxx.REDACTED

> DATE: DEC 02, 2009@16:28:45 EST

> DOMAIN: IMGxxxx.REDACTED

> Filename: False Positive CopySBY00012248164.TIF

> VistA Cache Size: 14650

> Jukebox Size: 919190

#### INSTALLATION 

This message is sent when the KIDS for this patch is installed.

Example:

> Subj: KIDS-MAG\*3.0\*39 INSTALLATION \[#853149\] 10 Dec 2009 08:34:54 -0500 (EST)

> 3 lines

> From: INSTALLATION In 'IN' basket. Page 1 \*New\*

> PACKAGE INSTALL

> SITE: IMGxxxx.REDACTED

> PACKAGE: IMAGING

> VERSION: 3.0

> Start time: Dec 10, 2009@08:34:51

> Completion time: Dec 10, 2009@08:34:54

> Run time: 0:00:03

> DATE: 3091210

> Installed by: INSTALLER

> Install Name: MAG\*3.0\*39

> Distribution Date: 3091005

> VistA Imaging V3.0 - Patch 39 - Test 22 10/05/2009 11:16AM ;Created on Oct 05,

> 2009@11:16:02

#### Monthly_Image_Site_Usage 

This message is sent when the monthly site usage report is finished gathering information. At completion, the task is re-queued for the next month.

Example:

> Subj: Monthly Image Site Usage: SALT LAKE CITY^660 (Sep 2009) \[#31135\]

> 10/01/09@04:01 143 lines

> From: IMAGPROVIDERONETWOONEFOUR,ONETWOONEFOUR In 'IN' basket. Page 1

> ------------------------------------------ ----------------------------

> SITE: SALT LAKE CITY^660

> Reporting Period: Sep 01, 2009 - Sep 30, 2009

> DATE: OCT 01, 2009@04:01:03 EST

> DOMAIN: IMGxxxx.REDACTED

> 2005 ENTRIES: 17798

> 2006.81 ENTRIES: 5

> WS DIS VERS: 3.0.59.31^Win XP.5.1.2600^1

> WS DIS VERS: 3.0.72.30^Win Server.5.2.3790^1

> WS CAP VERS: 3.0.72.30^Win XP.5.1.2600^1

> WS VR VERS: 3.0.41.17^Win XP.5.1.2600^2

#### Photo_ID_Action 

This message is sent by the Queue Processor when processing a GCC queue that was triggered from a Photo ID image.

Example of the message when the PHOTO-ID COPY entry is not properly defined:

> Subj: Photo_I_D_Action \[#31190\] 10/27/09@08:57 7 lines

> From: VistA Imaging PHOTO ID ACTION In 'IN' basket. Page 1 \*New\*

> --------------------------------------------------------------------

> SITE: IMGxxxx.REDACTED

> DATE: Oct 27, 2009@08:57:21 EST

> Production Account: 0

> The Photo ID protocol in the IMAGE ACTION file (#2005.86) could not resolve the target export location as currently defined.

> Update the EXPORT LOCATION field for the PHOTO-ID COPY entry in IMAGE ACTION file.

#### Scheduled_Purge_Failure 

This message is sent when the Scheduled Purge does not start at the designated time.

Example:

> Subj: Scheduled_Purge_failure \[#31195\] 10/27/09@12:40 4 lines

> From: VistA Imaging MAGQCBP In 'IN' basket. Page 1 \*New\*

> -------------------------------------------------------------------------------

> SITE: IMGxxxxx.REDACTED

> DATE: Oct 27, 2009@12:40:01 EST

> The SALT LAKE CITY implementation of VistA Imaging has failed to start the sche

> dule Purge activity!

> The task is currently assigned to BP Server: ISW-xxxxx-LT

#### Scheduled_RAID_Group_Advance_Failure 

This message is sent when the system cannot change to another RAID Group because none of the groups has enough free space.

Example:

> Subj: Scheduled_RAID_Group_Advance_failure! \[#31783\] 04/02/10@03:20 3 lines

> From: VistA Imaging MAGQ FS CHNGE In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Apr 02, 2010@03:20:06 EST

> The scheduled RAID Group Advance failed!

#### Scheduled_Verifier_Failure 

This message is sent when the Scheduled Verifier does not start at the designated time.

Example:

> SITE: SALT LAKE.REDACTED

> DATE: Feb 11, 2010@00:30:04 PST The SALT LAKE HCS implementation of VistA Imaging has failed to start the schedule Verifier activity!

> The task is currently assigned to BP Server: VHASLCBP1

#### Site_Report_Task_Was_Restarted

This message is sent by the Monitor Background Processor Activity \[MAGQ BPMONITOR\] menu option if the monthly Imaging Site Usage report has to be re-tasked.

Example:

> Subj: Site_report_task_was_restarted \[#31231\] 10/27/09@07:13 4 lines

> From: VistA Imaging MAGQCBP In 'IN' basket. Page 1 \*New\*

> ----------------------------------------------------------------------

> SITE: IMGxxxx.REDACTED

> DATE: Oct 27, 2009@07:13:01 EST

> The inactive monthly Imaging Site Usage report task was restarted

> The problem was: Inactive

#### VI_BP_Eval_Queue

This message is sent when number of entries on the EVAL queue exceeds a user defined threshold.

Example:

> SITE: SALT LAKE.REDACTED

> DATE: Mar 30, 2010@13:25 EDT The total number of EVAL queues is 9451. Please review the DICOM Gateways to ensure Routing is appropriately setup with the correct destination.

> If your site is not using DICOM Gateway for Routing then review the Imaging DICOM Gateway Installation Guide, Section 4.3.

> On-Demand Routing will not generate EVAL queues, if your site is doing only On-Demand Routing then the DICOM Gateway parameters are set incorrectly.

> Check the following DICOM parameters on all your Gateways:

> (On-Demand routing does not require these parameters to be set.)

> Will this computer be a Routing Processor? // NO Will this computer be part of a system where 'autorouting' is active? // NO

#### VI_BP_Queue_Processor_Failure

This message is sent by the Monitor Background Process when a user defined threshold for an activity is exceeded.

Example:

> Subj: VI_BP_Queue_Processor_failure \[#31186\] 10/27/09@06:45 6 lines

> From: VistA Imaging MAGQCBP In 'IN' basket. Page 1 \*New\*

> ---------------------------------------------------------------------

> SITE: IMGDEM01.REDACTED

> DATE: Oct 27, 2009@06:45 EST

> VistA Imaging BP Server, ISW-xxxxx-LT has failed to process a JUKEBOX queue for 25 minutes.

> The last date/time a queue was processed was on: Oct 26, 2009@11:38:27

> Total JUKEBOX queues are: 100.

> This BP Queue processor was supporting the VI implementation serving: SALT LAKE CITY

#### “Rescinded” Watermarking Successful

The following is an example of the email message generated when an image associated with a Rescinded Advance Directive is successfully watermarked with the text “Rescinded”.

> Subj: Import API Report \[#31292\] 06/22/11@08:14 8 lines

> From: PROVIDER, ONE In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> 0\) 1^1 Image(s) Copied OK. 0 Errors.

> 1\) MAGRSND;3110622.081451.3

> 2\) 31

> 3\) RESCINDED IMAGE FILE^\\SERVER1\IMAGE1\$\SLA0\00\00\02\05\SLA00000020542.TIF

> The preceding array was generated by

> the VistA Imaging Import API while

> processing a 'RESCIND' Image action.

> Enter message action (in IN basket): Ignore//

#### “Rescinded” Watermarking Failed

The following is an example of the email message generated when an image associated with a Rescinded Advance Directive cannot be watermarked with the text “Rescinded”.

> Subj: Import API Report \[#31341\] 06/23/11@09:52 9 lines

> From: PROVIDER, ONE In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> 0\) 0^Image is already Rescinded.

> 1\) Image(1) 0^\<*error message for Rescind Failure*\>.

> 2\) Image(1) RESCIND Action is Canceled.

> 3\) Image(1) IEN: 20924

> 4\) TIU Note: 697

> The preceding array was generated by

> the VistA Imaging Import API while

> processing a 'RESCIND' Image action.

> Enter message action (in IN basket): Ignore//

### Screen-Generated Output 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Server Size

This window shows the amount of total space, free space and % Server Reserve space for Tier 1 and Tier 2 as well as RAID Groups.

Select View \> Server Size from the menu bar to view this window.

> **NOTE:** This option can be accessed at any time the Queue Processor is running.

> ![](vista-imaging-system-background-processor-user-manual/077.png)

The VistA Storage area on the Queue Processor GUI can be refreshed with the most current storage utilization statistics for RAID Groups and Tier 1 shares by clicking the buttons Refresh Current Write Group or Refresh All (Tier 1 Shares).

#### JBTOHD Report

When selecting View \> JBTOHD Report from the menu bar, the following graphic is displayed. This window displays a summary of all the entries in the JBTOHD queue and the file types that will be retrieved for all the entries. This report can be saved to the disk with the File menu. The fields in this window are described below.

Select View \> JBTOHDReport from the main menu bar to view this window.

> ![](vista-imaging-system-background-processor-user-manual/078.png)

| Name             | Description                                                  |
|----------------------|------------------------------------------------------------------|
| Current JBTOHD Queue | Number of entries in the JBTOHD queue and the request date/time. |
| Image Queue          | User who requested the images and title                          |
| Number of Queues     | Total number of files that will be copied                        |
| Number of ABSTRACT   | Number of abstract files that will be copied                     |
| Number of BIG        | Number of BIG files that will be copied                          |
| Number of FULL       | Number of Full files that will be copied                         |
| Patient:             | List of patients for the requested images and their patient ID   |

#### IMPORT Queue Status Report

The IMPORT Queue Status window displays queue, parameter, and log information for IMPORT queue entries (processed or unprocessed). When the entry has not been processed, the window will display the data in the queue entry in VistA and also the parameters that will be used in extracting the data from the remote location. More information will be displayed after the IMPORT queue entry has processed. The window will show the progressive steps of the queue entry processing. It will also show any errors that occur. The field descriptions are described below.

Select View \> Import Queue from the main menu bar to view this window.

(Windows Session Tab displayed)

![](vista-imaging-system-background-processor-user-manual/079.png)

(Acquisition Session File tab displayed)

![](vista-imaging-system-background-processor-user-manual/080.png)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">Import Tracking ID Lookup</td>
<td>Unique identifier for each IMPORT entry</td>
</tr>
<tr class="even">
<td colspan="2">Import Queue Lookup</td>
<td><p>IEN for IMPORT queue entry in the IMAGE BACKGROUND QUEUE file (#2006.03).</p>
<p>This number is displayed in the Queue Processor GUI in the <em>Process: Queue IEN</em> column (e.g., IMPORT:<mark>1234</mark>).</p></td>
</tr>
<tr class="odd">
<td colspan="2">ACQUISITION SESSION file (#2006.041)</td>
<td>Logs all pertinent data when a queue entry is processed</td>
</tr>
<tr class="even">
<td></td>
<td>IEN</td>
<td>IEN for IMPORT queue entry in the IMAGE BACKGROUND QUEUE file (#2006.03).</td>
</tr>
<tr class="odd">
<td></td>
<td>QUEUE field (#.01)</td>
<td>Sequence # of events for processing the queue entry.</td>
</tr>
<tr class="even">
<td></td>
<td>TRACKING ID field (#.02)</td>
<td>Unique identifier for the IMPORT entry.</td>
</tr>
<tr class="odd">
<td></td>
<td>ACTIVITY field (#1)</td>
<td>Category of the session output.</td>
</tr>
<tr class="even">
<td></td>
<td>TIME field (#2)</td>
<td>Time stamp for processing step.</td>
</tr>
<tr class="odd">
<td></td>
<td>QUEUE STATUS field (*#3)</td>
<td>Status logged for each processing step.</td>
</tr>
<tr class="even">
<td colspan="2"><p>IMAGING WINDOW SESSIONS file</p>
<p>(#2006.82)</p></td>
<td>Displays error information when an attempt to queue an IMPORT failed.</td>
</tr>
<tr class="odd">
<td colspan="2"><p>IMPORT QUEUE file</p>
<p>(#2006.034)</p></td>
<td>Displays parameter information that was initiated by the remote source.</td>
</tr>
</tbody>
</table>

> **NOTE:** If there are conflicts caused by the volume of imports being processed, it may be necessary for the IMPORT queue to hold (pause) and try processing the IMPORT queue again. The IMPORT queue logs this event in the XTMP global and is held there for 30 days.

![](vista-imaging-system-background-processor-user-manual/081.png)

#### Purge ReQueue by Type Entries

Occasionally, some queues build to a large number of entries because the queues are not assigned to a BP Server or a setting was made unintentionally. For some queue types, the entries are no longer needed or were erroneously placed on a queue and can be entirely deleted.

When the queue counts are high for any of the queues, the GUI may take an extended period of time to display the entries. The Queue Management by Type window, which displays the same information on the queue counts, opens immediately no matter how many entries are in each queue.

In addition to deleting queue entries for a particular queue, you can re-queue all the entries in a particular queue. If specific entries need to be re-queued, use the Queue Manager window.

Select Active or Failed queue entries, as follows:

- Failed Queues = all of the queue types are selectable and their entries can be purged/re-queued.
- Active Queues = only the Purge option is available and only for the JBTOHD, GCC, PREFET and EVAL queues. The Requeue option is not available.

Select View \> Purge / ReQueue by type from the main menu bar to view this window.

> ![](vista-imaging-system-background-processor-user-manual/082.png)

#### Compliance

The purpose of this option is to implement section 508 of the Rehabilitation Act of 1973, as amended (29 U.S.C. 794d). Section 508 requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, Federal employees with disabilities have access to and use of information and data that is comparable to the access and use by Federal employees who are not individuals with disabilities, unless an undue burden would be imposed on the agency. Section 508 also requires that individuals with disabilities who are members of the public seeking information or services from a Federal agency have access to and use of information and data that is comparable to that provided to the public who are not individuals with disabilities, unless an undue burden would be imposed on the agency.

Select View \> 508 Mode from the menu bar to view this option.

# Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- Application Description
- Setting up
- Tasking
- Understanding Processing
- Starting/Running the application
- Reports

=====================================================================

4.  

## Application Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier validates the VistA Imaging network file references and consolidates Tier 2 image files. It is used to identify, and in some cases, correct inconsistencies within the VistA database, as well as identify incorrect image file locations in VistA. Specifically, the Verifier:

- Performs multiple patient integrity checks
- Sets or clears invalid file location pointers in the database
- Checks for mismatches between image file contents and the database
- Checks for mismatches between specific fields in the text files and the database
- Re-creates missing file types, when possible
- Copies files to Tier 2 and de-queues JUKEBOX queues when doing so, if such a queue exists.

## Setting Up the Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier software needs to be installed on a Server class machine. The Verifier requires a BP Server defined for the server on which it will run (section *2.5.2, Adding a BP Server to the VistA Imaging System*). In addition, the Broker port connection needs to be configured. See *Appendix A* for configuration information.

Check the network connections to the Tier 1 shares and archive device shares to make sure they are online and the Windows account that will be used for logging into the workstation has READ/WRITE permission to those shares.

## Tasking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Verifier is to be run on a daily/weekly/monthly schedule, the SCHEDULEDVERIFY task will need to be assigned to the BP Server.

## Understanding Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process is:

1.  Select a range of IENs to be processed.
2.  The Verifier steps through each IEN in VistA and validates the image pointer locations (Full, abstract and BIG types) for both the Tier 1 shares and Tier 2 devices (jukebox).  
    The validation is done by physically checking the share for the existence of each file type. There are two different types of checks:
- When a Tier 1 file is not found, the Verifier clears the appropriate pointer in VistA for that file type.
- If the Tier 1 file is found at the pointer location, then no change is made to the database.
3.  The Verifier also searches all the online Tier 2 shares for the file.
4.  If the file is not found on the Images Tier 2 pointer location, but is found on an alternate the Tier 2 location the pointer in VistA is updated to that alternate location.
5.  If the archive file is found at the pointer location, then no change is made to the database.
6.  The Verifier creates missing files when it finds other files that can be used to create these missing files.  
    The following table shows the specific file extensions needed to create a particular file type. Those extensions not listed must be resent/recaptured from the source.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Missing file</strong></th>
<th><strong>Create from master</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abstract</td>
<td><ul>
<li><blockquote>
<p>756</p>
</blockquote></li>
<li><blockquote>
<p>BIG</p>
</blockquote></li>
<li><blockquote>
<p>BM</p>
</blockquote></li>
<li><blockquote>
<p>BW</p>
</blockquote></li>
<li><blockquote>
<p>DCM</p>
</blockquote></li>
<li><blockquote>
<p>JPG</p>
</blockquote></li>
<li><blockquote>
<p>PAC</p>
</blockquote></li>
<li><blockquote>
<p>TGA</p>
</blockquote></li>
<li><blockquote>
<p>TIF</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>TGA</td>
<td><ul>
<li><blockquote>
<p>BIG</p>
</blockquote></li>
<li><blockquote>
<p>DCM</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

For sites that use multiple online Tier 2 shares the process is:

1.  When a file in the set of images is missing and a master file (see table above) is available on the network, the verifier creates the derivative file(s) and will then copy the complete set to the current Tier 2 Write location. The pointers are updated in VistA to reflect this location change.
2.  Patient data integrity checks are automatically performed on the IENs as the pointers are being examined and validated. There are 14 integrity checks. Any inconsistencies found are reported.

### Reasons for Running the Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following scenarios have happened at the sites and are stated here as justification for running the Verifier on a regular basis.

1.  Each day, images are saved on the VistA Imaging Tier 1 and Tier 2. There are occasions when an undetected problem occurs and a file in an image set is not copied to the Tier 1/ Tier 2 device. The Verifier will report these missing files. If done in a timely manner, missing files can be recaptured/resent from the source before they are removed from those sources.
2.  In cases where image storage application did not complete the file creation, the Verifier will clean up the database pointers. For example, when capture events time out prior to the file being copied to Tier 1, they are automatically deleted by the capture application; this results in an NO ARCHIEVE event. The image entry will be in the IMAGE ARCHIVE (#2005.1) file with no reason for deletion.
3.  References are set in patient reports for the images in order to support archiving and viewing. Occasionally, images on a report belong to another patient. The Verifier will detect these inconsistencies and report them.
4.  Files are removed from Tier 1 to free up storage space and files are recalled from Tier 2 when they need to be viewed. Pointers are reset/set for each of these studies (100’s of images). The Verifier will detect and possibly repair any inconsistencies.
5.  Resolve inconsistencies in the database that can result because of discrepancies between files that interact, manual corrections, network anomalies, power outages, hardware failures, and incomplete database updates.
6.  The BP Verifier can be used to accelerate the process of migrating files to Tier 2 either with a setting of the manual range of IENs or by through the use of the Scheduled Verifier. As the verifier copies files to Tier 2 it will check the Queue file for that entry and de-queue JUKEBOX queue if there is one.

## Maintenance Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verifier scans can be run any time of the day as there is minimal impact on VistA. They should be run based on the following events:

- Routine scanning of newly acquired images

> The Verifier should be run every 1 or 2 weeks to verify new entries in the IMAGE file (#2005). In some cases, if images are missing they can be resent from the modality.

- Periodic maintenance of the VistA Imaging system

> The Verifier should be run once a year to verify the entire range of Image Internal Entry Number (IENs) in the IMAGE file (#2005). During the year, many files will be retrieved from the jukebox and pointers updated in the database. Allowing the Scheduled Verifier to run on a regular basis will insure that files on Tier 1 and Tier 2can be accurately located.

- Large Image Share population events

> There may be occasions where files were not copied and incorrect file pointers set in the database with this large volume of files being moved to Tier 1. Running the Verifier over the range of Image IENs that were copied back to the Image shares from Tier 2will insure correct pointers.

- Image share or Tier 2 outages

> The Verifier should be run after the resolution of any event that interrupted the flow of images to Tier 2. The Queue Processor will make three attempts to process JUKEBOX queues, each queue failure re-queue will go to the end of the queue. Note that these files ONLY reside on the Image shares and therefore MUST be either re-queued using the Queue Manager or copied to Tier 2 using the Verifier.

> To handle cases where the share is taken off line by a scheduled or unscheduled process: The BP Verifier will not clear pointers if it cannot detect the folder that the image is supposed to be in.

### Integrity Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier steps through each of the IENs within the range looking for specific types of problems. The following sections describe the integrity checks performed on these files.

#### File Integrity

Referential integrity of the Database Network pointers and the Imaging Storage system

File location references in the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1) are physically checked to determine the existence of the file(s) on their assigned Imaging Tier 1 and Tier 2 shares. The Verifier checks for the existence of the folder on the Tier 1 shares. If the folder does not exist, then it is presumed either the file server or cluster is off-line and these Tier 1 file references are left as found and the “Tier 1 *File Type* location is offline” event is logged, otherwise, If any file (excluding TXT) is missing from the Image shares, the pointer will be cleared in the IMAGE file (#2005) record or the IMAGE AUDIT file (#2005.1) record. If all files are missing on any on-line Tier 2, the Tier 2 pointer will be cleared. The Verifier will set the Tier 2 pointer if any of the files in the set are found on the current or alternate Tier 2. The Verifier will also look at the IMAGE AUDIT file (#2005.1) to ensure the file set exists at the location(s) specified in this file.

#### File Corruption

When IMAGE FILE (#2005) or IMAGE AUDIT (#2005.1) is corrupt or otherwise is lacking required fields to identify the Image, the Capture events, and/or the patient, the BP Verifier removes or kills the nodes and logs what was found in an html log file.

These records are expected to result from network latency or image capture failures of other causes. The entire state of the global node will be logged in a VKILLJournal\_*Date_Seq_No*.html file and the entire node will be removed from the database.

![](vista-imaging-system-background-processor-user-manual/083.png)

#### Patient Integrity Vs. File Integrity

Patient-related values in the IMAGE file (#2005) are checked for consistency within the group Image entries and the associated report files.

The following table lists the integrity issues that will prevent images from being displayed. The following integrity error messages will be generated when the image is retrieved for viewing.

| Message Generated                | Explanation                                                                                                                                                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No Image Ptr in AP                   | The Clinical Association Report (AP) for this image does not contain an image entry that points back to this image.                                                                                                       |
| GP has no images                     | The image series does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition.                                                   |
| Conflicting AP & Image DFNs          | The patient file reference (DFN) in the Clinical Association Report (AP) does not match the DFN in the IMAGE file (#2005).                                                                                                |
| Invalid Image Ptr to AP              | The Clinical Association Report (AP has image references that are not in the IMAGE file (#2005).                                                                                                                          |
| Conflicting GP and GO DFN            | The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.                                                                                                                  |
| GP & GO AP Mismatch                  | The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.                                                                                                                  |
| GP Missing GO Ptr                    | The Group Object multiple of the referenced Group Parent does not reference this group object.                                                                                                                            |
| No AP Mult Ptr                       | This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005) record is missing the *PARENT DATA FILE IMAGE POINTER* for a Clinical Association Report (AP). |
| GO DFN mismatches                    | Some image file Group Objects have different PATIENT file (#2) references (DFN).                                                                                                                                          |
| Image entry is structurally abnormal | The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non-Group image (NG) is corrupt.                                                                                          |
| Missing Group Objects                | The Group Parent has Group Object references that are missing.                                                                                                                                                            |
| DFN Mismatches in AP Image Mult      | The Clinical Association Report (AP) references a Group Parent that has image files with a PATIENT file (#2) reference (DFN) that is different from the report.                                                           |

> **NOTE:** The following integrity issues <u>will not prevent</u> their respective images from being displayed. These are informational messages.

| Message Generated | Explanation                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No AP Ptr             | The IMAGE file (#2005) record is missing the PARENT DATA FILE file (#2005.03) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified. |
| No AP entry Ptr       | This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the *PARENT GLOBAL ROOT IEN* for a Clinical Association Report (AP).         |

#### Text File Integrity

When the *Check* option is selected in the *Check Image Text* window, the Verifier compares specific fields in the text file with those in the associated IMAGE file (#2005) record in VistA. The following is a list of problems that the Verifier detects. Included in the list is a suggested way of correcting these problems.

- Text file is binary or unreadable.

> Correction- Copy the version from the jukebox or get a copy from the backup tapes

- Text file is ASCII but has unprintable characters or truncated.

> Correction- Copy the version from the jukebox or get a copy from the backup tapes

- *Patients ID* (SSN) field in the text file does not match that in VistA.

> Correction- Contact the National Help Desk.

The following fields are in the DICOM DATA block (lower section of the text file). These fields are generated by the modality and should not be altered.

- *SOP InstanceUID* field (DICOM- 0008,0018) in the text file does not match the one in VistA. (“PACS” node – PACS UID field (#60) in the IMAGE file (#2005) )

> Correction- Most likely the text file has the correct UID. Make the correction in VistA (*PACS UID* field \#60 in the IMAGE file (#2005) to match the DICOM field (0008,0018).

- *Study Instance UID* field (DICOM- 0020,000D) in the text file does not match the one in VistA. (“PACS” node – PACS UID field (#60) on the PARENT IEN.)

> Correction- Most likely the text file has the correct UID. Make the correction in VistA (*PACS UID* field (#60) in the IMAGE file (#2005) ) to match the DICOM field (0020,000D).

- *SOP* (DICOM- 0008,0018) and/or *Study Instance UID* (DICOM- 0020,000D) are/is blank in the text file.

> Correction- If these fields are blank and the image is stored in VistA in TGA format, then this crucial information is lost and it will be impossible to reconstitute the DICOM image. Call the National Help Desk.

- *Patient ID* (SSN) in the top section (*DATA1*) of the text file does not match the DICOM field (0010,0020) in the bottom section (*DICOM DATA*).

> Correction- This file has already been corrected and needs no further correction if the *Patients ID* field (SSN) in the top section (*DATA1*) matches VistA.

## Starting/Running the Verifier 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier can be started as an independent application or can be scheduled to run in the background at prescribed time intervals (See Section 3.5). The following steps describe how to run the Verifier in the foreground:

1.  From the Windows Start \> Programs menu, select VistA Imaging Programs \> Background Processor \>Verifier.
2.  Log into the application using a valid VistA access and verify code. (The secondary menu option All MAG\* RPC's \[MAG WINDOWS\]is required for access to the Verifier).

> The BP Verifier window opens.

3.  In the Scope box, select one of the following options:
- Range - Type a start and stop IEN. The Verifier will process this range of IENs (inclusively). If the Start IEN is greater than Stop IEN, the Verifier will scan the image records backwards.
- All – Every IEN record in VistA will be processed
- Auto – The Verifier will process IENs from the highest backwards to an IEN that was previously processed. This is the mode used by the Scheduled Verifier, and cannot be selected in Manual mode.
4.  In the Check Image Text box, select one of the following options:
- Check - Compare specific fields in the text files on Tier 1 with data contained in the associated IMAGE file (#2005) records in VistA. (Processing time will increase moderately.)
- Don’t Check – Do not do any comparison of the text files with VistA.

> Note: This is the preferred option as the procedure to correct inconsistencies is under development.

5.  Click the Start button to begin processing.  
    Processing activity will be displayed in the GUI window.

![](vista-imaging-system-background-processor-user-manual/084.png)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Image Shares</strong></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>Entry number in the NETWORK LOCATION file (#2005.2)</td>
</tr>
<tr class="odd">
<td>Network Location</td>
<td>Name of the entry in the NETWORK LOCATION file (#2005.2)</td>
</tr>
<tr class="even">
<td>Physical Reference</td>
<td>Network path of this Network Location entry</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Scan Controls</strong></td>
</tr>
<tr class="even">
<td>Scope</td>
<td><p>Setting:</p>
<ul>
<li><p>Range = Scan records in specified range</p></li>
<li><p>All = Scan all records</p></li>
<li><p>Auto = Automatically scan newly acquired files after the last scanned record</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Check Image Text</td>
<td><p>Setting:</p>
<ul>
<li><p>Check = Compare specific fields in the text files on Tier 1 with data contained in the associated IMAGE file (#2005) records in VistA.</p></li>
<li><p>Don’t check = Don’t compare fields above.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Progress</td>
<td>Number of records processed</td>
</tr>
<tr class="odd">
<td>Range</td>
<td><p>Setting:</p>
<ul>
<li><p>Start = Beginning IEN in range to scan</p></li>
<li><p>Stop = Ending IEN in range to scan</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Summary</strong></td>
</tr>
<tr class="odd">
<td>Start Time</td>
<td>Date/Time this Verifier scan was started</td>
</tr>
<tr class="even">
<td>Run Time</td>
<td>Total elapsed time the Verifier ran</td>
</tr>
<tr class="odd">
<td>Total IENs</td>
<td>Number of image file entries processed in this scan</td>
</tr>
<tr class="even">
<td>No Refs</td>
<td>Number records with no Tier 1 or Tier 2 location references</td>
</tr>
<tr class="odd">
<td>Bad VC Refs</td>
<td>The number of IMAGE file (#2005) entries with Image share references that could not be matched to an actual file stored on an image share (Tier 1).</td>
</tr>
<tr class="even">
<td>Bad JB Refs</td>
<td>The number of IMAGE file (#2005) entries with Tier 2 references that could not be matched to an actual file stored on a jukebox.</td>
</tr>
<tr class="odd">
<td>Alt JB Refs</td>
<td>The number of files found on multiple Tier 2 share locations are listed. (These are copied to the current Tier 2 share using the aggregate function).</td>
</tr>
<tr class="even">
<td>Size Zeros</td>
<td>The number of zero length files found on the Image shares and archive Tier 2 shares.</td>
</tr>
<tr class="odd">
<td>Size Zero Deleted</td>
<td>Number of files deleted that had a size of zero. Only image share files will be deleted.</td>
</tr>
<tr class="even">
<td>Duplicates</td>
<td>Number of Image entries that are duplicated in the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1). These images are not viewable because the image files themselves have the same file names and therefore have ambiguous patient and procedure references.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Tier 1 and Tier 2 Shares boxes</strong></td>
</tr>
<tr class="even">
<td>IEN</td>
<td>Entry number in the NETWORK LOCATION file (#2005.2)</td>
</tr>
<tr class="odd">
<td>Network Location Name</td>
<td>The name of the entry in the NETWORK LOCATION file (#2005.2)</td>
</tr>
<tr class="even">
<td>Physical Reference</td>
<td>Network path of this Network Location entry</td>
</tr>
<tr class="odd">
<td>Operational Status</td>
<td><p>Status:</p>
<ul>
<li><p>On-line = READ/WRITE access to this share</p></li>
<li><p>Off-line = no access to this share</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Hash Subdirectory</td>
<td><p>Setting:</p>
<ul>
<li><p>Yes = Directory hashing is used. Files are maintained in a 5-level deep subdirectory structure where no directory will contain more than 100 unique filenames with their various extensions. (Both 8.3 and 14.3 format files are valid)</p></li>
<li><p>No = Image files are stored in the top-level folder in a flat file structure, which means that files are placed and retrieved from the root directory of the share. <strong>Do not use this structure.</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Share Availability</td>
<td><p>Setting:</p>
<ul>
<li><p>On-line = Software can access shares on the network.</p></li>
<li><p>Off-line = Software cannot access shares on the network.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Activities box</strong></td>
</tr>
<tr class="odd">
<td>Time</td>
<td>Actual time when the IMAGE file (#2005) was processed</td>
</tr>
<tr class="even">
<td>Activity</td>
<td>Description of the action taken</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>IMAGE record number currently being processed</td>
</tr>
<tr class="even">
<td>File</td>
<td>Filename in the current IMAGE file (#2005) record being processed</td>
</tr>
<tr class="odd">
<td>JB Full</td>
<td>The DISK &amp; VOLUME, WORM (#2.2) value for the Tier 2 share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where Full image is located. Other extensions will be listed here except the BIG file (listed in the JB Big column).</td>
</tr>
<tr class="even">
<td>JB Big</td>
<td>The BIG JUKEBOX PATH (#103) value for the Tier 2 share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where BIG image is located. The extensions of all files on Tier 2 will be listed</td>
</tr>
<tr class="odd">
<td>VC Full</td>
<td>The DISK &amp; VOLUME, MAGNETIC (#2) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where FULL image is located</td>
</tr>
<tr class="even">
<td>VC Abstract</td>
<td>The DISK &amp; VOLUME, ABSTRACT (#2.1) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) share where abstract image is located</td>
</tr>
<tr class="odd">
<td>VC Big</td>
<td>The BIG MAGNETIC PATH (#102) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where BIG image is located</td>
</tr>
<tr class="even">
<td>CWL</td>
<td>Image share that is the current write location. This will change automatically if the AUTO WRITE LOCATION UPDATE option is selected. The check for space is done after 100 Writes to the share or after 20 minutes since the last check, whichever comes first.</td>
</tr>
<tr class="odd">
<td>JB Path 1</td>
<td>The IEN for the entry in NETWORK LOCATION (#2005.2) file of first alternate Tier 2</td>
</tr>
<tr class="even">
<td>JB Path 2</td>
<td>The IEN for the entry in NETWORK LOCATION (#2005.2) file of second alternate Tier 2</td>
</tr>
<tr class="odd">
<td>(status bar at bottom)</td>
<td>Parameters for this run are listed.</td>
</tr>
</tbody>
</table>

> Note: When the IEN range includes files that have been saved in a flat file structure, there will be a noticeable increase in the time it takes to complete the scan.

> The Verifier stops when it has processed all the IENs in the range specified.

6.  Click Stop to terminate processing at any time.

> When the Verifier run is complete, enter a new set of Start/Stop IENs in the SCOPE and start a new run.

Creating a Debug Log:

A new Help menu item is provided for debugging purposes.

![](vista-imaging-system-background-processor-user-manual/085.png)

The user will need to check the menu Help \| Debugging Log, to have a Debug Log created with detailed trace of the Verifier process.

> **NOTE:** This setting is intended to be used when debugging issues in conjunction with CLIN 3 support personnel.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two types of reports are produced:

- Log files
- Emails

### Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New log files are created as HTML files each day and each time the Verifier is run. HTML files are viewable, printable, and searchable. By default, they reside in the C:\Program Files\VistA\Imaging\BackProc\log\Verifier directory. These files can be accessed by:

- File \> Open Log on the BP Verifier menu bar
- Internet browser

These log files can be imported into an Excel spreadsheet.

> **IMPORTANT:** These files should be kept for historical reasons and added to the tape backup storage process to safeguard the files. (See *Appendix B: Backups* in the *VistA Imaging System Installation Guide.*) For this reason, it is important to set a Network Log file location for each BP Server (see [*Section 2.5.5*](#specifying-the-log-file-location-and-size)).

<u>Log File Format</u>

Verifier log files are archived as HTML files and have the year-month-day and sequence number imbedded in the file name, as shown in the right pane of the window.

![](vista-imaging-system-background-processor-user-manual/086.png)

If more than one log file is run on the same day, the system adds a sequence number such as “0001” following the date in the file name. For multiple runs on the same day, the highest sequence number is the latest log file run for the day, as shown for the “Scan2019_03_19_0007.html” file.

BP Verifier produces the following types of log files.

#### Scan Log File

The Scan log file lists entries with potential file integrity problems. The log records the operational events that take place to correct a particular problem. They are used to determine if and how the Verifier corrected the faulty condition. The IENs that the Verifier could not fix are listed in the ScanError log file. For the complete list of messages, see Output HTML Messages.

> **NOTE:** No action is required on entries found in the Scan.Log file.

![](vista-imaging-system-background-processor-user-manual/087.png)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Date/Time</td>
<td>Actual time when the IMAGE record was processed.</td>
</tr>
<tr class="even">
<td>Message</td>
<td>Description of action taken.</td>
</tr>
<tr class="odd">
<td>IMAGE_PTR</td>
<td>Image record currently being processed including the version/dates/log file names.</td>
</tr>
<tr class="even">
<td>FILE_NAME</td>
<td>Filename for the Image record.</td>
</tr>
<tr class="odd">
<td>FULL_JB_PTR</td>
<td>The DISK &amp; VOLUME, WORM (#2.2) value for the Tier 2share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where FULL image is located. Other extensions will be listed here except the BIG file (listed in the JB BIG column).</td>
</tr>
<tr class="even">
<td>BIG_JB_PTR</td>
<td>The BIG JUKEBOX PATH (#103) value for the Tier 2 share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where BIG image is located. The extensions of all files on the jukebox will be listed.</td>
</tr>
<tr class="odd">
<td>FULL_VC_PTR</td>
<td>The DISK &amp; VOLUME, MAGNETIC (#2) value for the share in the IMAGE file (#2005) and\or in IMAGE AUDIT file (#2005.1) where FULL image is located. (Other file extensions on this share are also listed.)</td>
</tr>
<tr class="even">
<td>ABS_VC_PTR</td>
<td>The DISK &amp; VOLUME, ABSTRACT (#2.1) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where abstract image is located. (Other file extensions on this share are also listed.)</td>
</tr>
<tr class="odd">
<td>BIG_VC_PTR</td>
<td>The BIG MAGNETIC PATH (#102) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where the BIG image is located.</td>
</tr>
<tr class="even">
<td>Current_Write_PTR</td>
<td>Image share that is the current write location. This will change automatically if the AUTO WRITE LOCATION UPDATE option is selected. The check for space is done after 100 Writes to the share or after 20 minutes since the last check, whichever comes first.</td>
</tr>
<tr class="odd">
<td>JB_ALT_1<br />
(2, 3, …)</td>
<td>Network Location of Tier 2. If a site has 2 or more Tier 2 shares, then the second, third, etc. are the “alternate” Tier 2.</td>
</tr>
</tbody>
</table>

#### NoArchive Log File

The NoArchive log file contains image file names that are missing on the jukebox and could not be created from existing files and/or could not be found on the Tier 1. The Verifier examines both the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1) for missing files. The *2005.1* column shown below indicates those missing files that have been deleted and the IMAGE file (#2005) record has been moved to the IMAGE AUDIT file (#2005.1).

> ![](vista-imaging-system-background-processor-user-manual/088.png)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Filename</td>
<td>Name of the missing file.</td>
</tr>
<tr class="even">
<td>2005.1</td>
<td><p>If the column contains “2005.1”, then the Image has been deleted and the image information is in the IMAGE AUDIT file (#2005.1).</p>
<p>If the column is blank, the file is missing from Tier 1 and Tier 2 storage and must be restored using one of the methods listed above.</p></td>
</tr>
</tbody>
</table>

> **NOTE:** When the 2005.1 column is blank, the file is missing and must be recovered from the backup tapes or other means.

These files must be restored using one of the following methods:

- Restore from backup tape(s).
- Resend from the gateway.
- Re-capture on the Capture workstation.
- File restore from platter on the jukebox.

If the missing file cannot be located, the Patient ID information and provided information for these missing field(s) should be sent to the hospital staff persons for their records.

#### ScanError Log File

The ScanError log file lists problems with IENs that could not be corrected. When a Verifier scan is completed, the contents of this file are sent as a mail message to the MAG SERVER mail group.

> **NOTE:** Action is required to correct any problems listed in this file.

Guidelines on Handling Errors:

- The most important columns are *FULL_JB_PTR* and *BIG_JB_PTR*, shown below, which display the files that are on the jukebox (there is not always a BIG file with an image).

> Important: The FULL, ABS, BIG, and TXT files should reside on the jukebox.

- The *Message* column describes the errors. (See section *8.3.1 Start/Run* for the complete list of messages in the Troubleshooting chapter.)
- All file types in a set may not be on the image shares as some may have been purged.
- If the *Check Text* option was used, see “*Check Text Option Messages*”. These are potential problems that need to be corrected.

![](vista-imaging-system-background-processor-user-manual/089.png)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Date/Time</td>
<td>Actual time when the IMAGE record was processed.</td>
</tr>
<tr class="even">
<td>Message</td>
<td>Description of problem.</td>
</tr>
<tr class="odd">
<td>IMAGE_PTR</td>
<td>IMAGE record currently being processed.</td>
</tr>
<tr class="even">
<td>FILE_NAME</td>
<td>Filename for the current IMAGE file (#2005) record being processed.</td>
</tr>
<tr class="odd">
<td>FULL_JB_PTR</td>
<td>The DISK &amp; VOLUME, WORM (#2.2) value for the archive (jukebox) share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where FULL image is located. Other extensions will be listed here except the BIG file. (It is listed in the JB Big column.)</td>
</tr>
<tr class="even">
<td>BIG_JB_PTR</td>
<td>The BIG JUKEBOX PATH (#103) value for the archive (jukebox) share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where BIG image is located. The extensions of all files on the archive (jukebox) will be listed.</td>
</tr>
<tr class="odd">
<td>FULL_VC_PTR</td>
<td>The DISK &amp; VOLUME, MAGNETIC (#2) value for the share in the IMAGE file (#2005) and\or in IMAGE AUDIT file (#2005.1) where FULL image is located. (Other file extensions that are on this share are listed, also.)</td>
</tr>
<tr class="even">
<td>ABS_VC_PTR</td>
<td>The DISK &amp; VOLUME, ABSTRACT (#2.1) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where abstract image is located. (Other file extensions on this share are also listed.)</td>
</tr>
<tr class="odd">
<td>BIG_VC_PTR</td>
<td>The BIG MAGNETIC PATH (#102) value for the share in the IMAGE file (#2005) and\or IMAGE AUDIT file (#2005.1) where the BIG image is located.</td>
</tr>
<tr class="even">
<td>Current_Write_PTR</td>
<td>Image share that is the current write location. This will change automatically if the AUTO WRITE LOCATION UPDATE option is selected. The check for space is done after 100 Writes to the share or after 20 minutes since the last check, whichever comes first.</td>
</tr>
<tr class="odd">
<td>JB_ALT_1<br />
(2, 3, …)</td>
<td>The IEN for the Tier 2share in the NETWORK LOCATION (#2005.2) file. If a site has 2 or more archive devices (jukeboxes), then the second, third, etc. are the “alternate” archive devices (jukeboxes).</td>
</tr>
</tbody>
</table>

#### DFNError Log File

The DFNError log file displays integrity issues with patient data. The *Memo* column messages, shown below, are described in checks on *Patient Integrity*.

> **NOTE:** Call the National Help Desk for assistance in fixing any of these issues.

![](vista-imaging-system-background-processor-user-manual/090.png)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Image_IEN</td>
<td>IMAGE record currently being processed</td>
</tr>
<tr class="even">
<td>Patient_Name_1</td>
<td>Patient name for current IEN</td>
</tr>
<tr class="odd">
<td>DFN_1</td>
<td>Patient file IEN for current record</td>
</tr>
<tr class="even">
<td>SSN_1</td>
<td>Social Security Number for current patient</td>
</tr>
<tr class="odd">
<td>Patient_Name_2</td>
<td>Patient name in linked Radiology report/TIU Note</td>
</tr>
<tr class="even">
<td>DFN_2</td>
<td>IMAGE file (#2005) IEN in linked report</td>
</tr>
<tr class="odd">
<td>SSN_2</td>
<td>Social Security Number of Patient in linked report</td>
</tr>
<tr class="even">
<td>Package</td>
<td>PROCEDURE, field (#6) in IMAGE file (#2005)</td>
</tr>
<tr class="odd">
<td>Package_IEN</td>
<td><p>PARENT GLOBAL ROOT, field (#17) in IMAGE file (#2005), (the number in the left column)</p>
<p>3.9: MAIL MESSAGE</p>
<p>63: AUTOPSY (MICROSCOPIC)</p>
<p>63.02: ELECTRON MICROSCOPY</p>
<p>63.08: SURGICAL PATHOLOGY</p>
<p>63.09: CYTOLOGY</p>
<p>63.2: AUTOPSY (GROSS)</p>
<p>74: RADIOLOGY</p>
<p>130: SURGERY</p>
<p>691: ECHOCARDIOGRAM</p>
<p>691.1: CARDIAC CATHETERIZATION</p>
<p>691.5: ELECTROCARDIOGRAPHY</p>
<p>694: HEMATOLOGY</p>
<p>699: ENDOSCOPY</p>
<p>699.5: GENERIC MEDICINE</p>
<p>8925: TIU</p></td>
</tr>
<tr class="even">
<td>Image_Class</td>
<td>Hierarchy in a study (parent, child)</td>
</tr>
<tr class="odd">
<td>Error_Level</td>
<td><p>Severity level:</p>
<p>1= highest</p>
<p>2 = high</p></td>
</tr>
<tr class="even">
<td>Memo</td>
<td>Integrity issues to resolve</td>
</tr>
</tbody>
</table>

#### BP Verifier Kill Journal

> The BP Verifier cleans out corrupted Image file and Image Audit file entries. It also changes the status of automatically deleted images from Deleted to Image Never Existed. A byproduct of network latency, we see increase in timeouts by capture software that results corrupt file records and automatically Deleted Image file entries. The BP Verifier cleans out the corrupted records and corrects the status of the deleted records. It also reports these actions in the VKillJournal log files, a sample of which follows.

> ![](vista-imaging-system-background-processor-user-manual/091.png)

#### BP Verifier Debug Log

A Debug Log can be turned on for the Verifier. The Verifier debug information is only logged when an error occurs. After 30 errors, debug mode will be turned off. This will keep the size of the Debug Log small and will not fill up the local hard drive with repetitive data.

To Turn Debug Mode On (both manual and Scheduled Verifier):

1.  Modify configuration file: C:\program files (x86)\vista\imaging\backproc\magBP.ini,
    1.  Open Microsoft Notepad as Administrator by right clicking the Notepad and selecting “Run as administrator”.
    2.  Select File-\>Open from the menu bar and navigate to the C:\program files (x86)\vista\imaging\backproc\\ directory.
    3.  Make sure All Files (\*.\*) is selected in the lower right hand corner and select the magBP.ini file and click Open.
2.  Add ‘\[Verifier\] (if it isn’t there) and add the line ‘DebugToFile = TRUE’

*Example:*

> \[Verifier\]

> DebugToFile=TRUE

To Enable Debug Mode for the Verifier:

1.  Set DebugToFile=TRUE
2.  When the first error occurs, the verifier will create the following file:

C:\Program Files (x86)\Vista\imaging\backproc\log\verifier\VerifierDebugLog-\<mmdd-hhmmss\>.log

To Disable Debug Mode for the Verifier:

1.  Set DebugToFile=FALSE

Locating the Debug log:

When the first error occurs, the Verifier will create the following file:

C:\program files (x86)\Vista\imaging\backproc\log\verifier\VerifierDebugLog-\<mmdd-hhmmss\>.log

If DebugToFile=FALSE, debugging will be off when the Verifier starts. Check daily if you need the debugger set to TRUE for the Verifier, because it may be turned off by the Debugger.

If the Verifier is started manually, the debugging can be turned on by checking the menu item: 'Help \| Debugging Log'. See section [*Starting/Running the Verifier*](#startingrunning-the-verifier) for more information.

#### Imaging_Integrity_Check Message

This message is sent when the Verifier completes a scan. The message identifies the time span involved and a summary of integrity errors.

Example:

> Subj: Imaging Integrity Check \[#31164\] 10/26/09@22:32 6 lines

> From: VistA Imaging DFN_Summary In 'IN' basket. Page 1 \*New\*

> -------------------------------------------------------------------------------

> SITE: IMGxxxx.REDACTED

> DATE: Oct 26, 2009@22:32:51 EST

> 51 entries scanned.

> Summary:

> 2 occurrences of : NO IMAGE PTR IN AP~1 type errors.

> Database scan took 0:0:5

#### Imaging_Site_Verification_Issue 

This message is sent when there is a network issue that is preventing the Verifier from accessing shares.

Example:

> Subj: Imaging Site Verification Issue \[#853534\]

> 14 Dec 2009 08:50:04 -0600 (CST) 8 lines

> From: \<USER.BGP@CENTRAL-ALABAMA.REDACTED\> In 'VERIFIER' basket. Page 1

> \*New\*

> -------------------------------------------------------------------------------

> SITE: CENTRAL-ALABAMA.REDACTED

> DATE: DEC 14, 2009@08:50:04 CST

> 12/14/2009 8:50:04 AM

> The Jukebox share: \\VHACAVIMMJB1\IMAGEJB1\$ is not available!

> All VistA Imaging Jukebox servers should be fully operational

> when operating the BP Verifier!

> 31271^CB031271.TGA^7.ABS.TXT.BIG.TGA^7^^^^27^^^

> when operating the BP Verifier!

#### Verifier_Scan_Error_Log message

This message is sent by the BP Verifier at completion of the scan. The report identifies the image entries in question.

Example:

> Subj: Verifier Scan Error log \[#31165\] 10/26/09@22:32 165 lines

> From: VistA Imaging Scan_Errors In 'IN' basket. Page 1 \*New\*

> ---------------------------------------------------------------------

> SITE: IMGxxx.REDACTED

> DATE: Oct 26, 2009@22:32:51 EST

> 10/26/2009 10:32:43 PM^No Full VC Files^21158^QRT00000019369.ASC^^^2^^^74^^^

> 10/26/2009 10:32:43 PM^No Jukebox Full Files^21158^QRT00000019369.ASC^^^^^^74^^

> ^

> 10/26/2009 10:32:43 PM^Not Certed^21158^QRT00000019369.ASC^^^^^^74^^^

> 10/26/2009 10:32:43 PM^No Full VC Files^21157^QRT00000019368.BMP^^^2^2^^74^^^

> 10/26/2009 10:32:43 PM^No ABS file VC Ptr Cleared^21157^QRT00000019368.BMP^^^^^

> ^74^^^

# Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- Application Description
- Setting up
- Tasking
- Understanding Processing
- Starting/Running the application
- Reports

=====================================================================

## Application Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image files are part of the patient’s record and must be preserved for the required number of years. Image files may be kept online indefinitely in long-term storage. However, image files in temporary storage must be purged periodically to provide ongoing free disk space for new images. The primary purpose of the Purge is to delete files in temporary storage in order to maintain a percentage of free disk space at all times. The Purge can be run manually, scheduled or run automatically. An express purge is available to dramatically decrease the time it takes to purge a share.

5.  <span id="_Toc121822809" class="anchor"></span>
    1.  

## Setting Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge software will need to be installed on a Server class machine. The Purge requires a BP Server defined for the server on which it will run (Section 3). In addition, the Broker port connection needs to be set up (Appendix A)

Check the network connections to the Tier 1 shares and Tier 2 shares to make sure they are online and the Windows account that will be used for logging into the workstation has READ/WRITE permission to those shares.

## Tasking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Purge is to be run automatically when a Tier 1/RAID Group exceeds the % Server Reserve threshold, the *PURGE* task will need to be assigned to the BP Server.

## Understanding Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Guidelines:

1.  First determine how much free space is needed on the Tier 1 shares for non-interrupted processing of new images.
2.  Once that has been determined, the Purge Parameters need to be set.
3.  Specify which file date the Purge parameters will use. The Windows date options are:
- Modified
- Created
- Accessed
4.  Select the Express Purge option as this will minimize the time it takes to delete files from the Tier 1shares.
5.  Select which shares (or all) are to be purged.

Purge Process:

1.  When the purge starts, the application begins at the top of the directory tree on a selected Tier 1 share and traverses to the bottom of the tree before starting on another share.
2.  When the purge finds a file that is a candidate for deletion based on the file date option selected, it first checks to make sure the file is on Tier 2 and has the same file properties (size, etc.):
- If the file exists on the archive, then the file is deleted from the Tier 1 share and its location pointer in VistA is cleared.
- If the file does not exist on the archive device, the JUKEBOX entry is queued where the file will be copied to Tier 2. The file is not deleted and no pointer in VistA is cleared.
- Warning: See section 7.6.1 for circumstances when NOT to run the Purge.
3.  The purge application then moves onto the next file. This process continues until all the selected Tier 1 shares have been processed at which point, the purge displays a summary page indicating its processing is complete for this session.

### Setting Purge Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Typically, the Abstract file parameter is set 99999 days. These files are small in size and are viewed as thumbnails on the Clinical Display workstations.

Keeping Patient Photo IDs and Advance Directives on Tier 1 can safeguard access to these images; the loss of which on primary storage can result in delays to patient care.

Locating images for a patient is much less time consuming when these images are available on Tier 1 versus having to wait for retrievals from the Tier 2.

The keep days for the Full and BIG files should be kept reasonably large to start.

1.  Start a test run on one share and determine how much free space is available after the run.
2.  If the free space is adequate, use the current parameters to purge the remaining shares.
3.  If more free space is needed, change the FULL and BIG retention/keep days to a lower number and start another test run on one share.
4.  When the right settings have been found, start the purge on the other shares.

> These values can be kept in place until the rate of images per day increases substantially. At that time, the FULL and BIG parameters will have to be decreased to remove more images from the shares.

Some sites have enough Tier 1 storage to keep 5 years of images. These sites need only purge once per year to remove the sixth year's images off the Tier 1. The Purge Parameters can be set to 5 years (in days) for the Abstract, Full, and BIG files.

Recommendation: VistA Imaging Cache or Tier 1 share devices operate more efficiently when 10 percent of disk capacity is available.

Some degradation occurs as the storage devices fill and files become fragmented. The system is designed to notify the VistA Imaging system manager when VistA Imaging shares resources have reached a critical level (default is 5% free space remaining). This value is too low for normal workflow. At this point, the Automatic Write Location update option no longer operates.

### File Types for Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, the file extensions (except TXT) in Appendix B are automatically purged from the Tier 1 shares. In order to have the TXT files purged, an entry must be made for “TXT” in the File Types field on the Imaging Site Parameters window on the Queue Processor application (this is set up by the installation). These files are purged when there is no FULL or BIG file type in the folder.

### Purge by Dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge uses the following Windows file dates. Every file in Windows has these dates set.

- Date Created
- Date Accessed
- Date Modified

Recommendation: Use the Date Modified for most cases.

### Express Purge Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Express Purge option can be used for any of the three types of purges described below—auto, scheduled, and manual. The algorithm is based on the principle that most files that are deleted during a purge are older files. The newer files remain on the share as they are within the keep dates for the Purge Parameters. The time it takes to traverse through these newer files can be lengthy with no files being deleted in the process. Some sites have a large number of shares and this “dead’ time for purging can be extreme. The Express option causes the purge to stop the file traversal on a share when the number of consecutive files that have not been deleted is greater than the Purge Rate (measured in file count).

The three ways to initiate a purge are:

- Auto

> The application monitors the amount of free space on the current RAID Group and determines if there are multiple RAID Groups. If only one RAID Group exists, when all the shares have reached the high-water mark indicated by the % Server Reserve, a purge is initiated on all the shares. If multiple RAID Groups are present and all the shares in the next RAID Group are above the high-water mark, the purge on that next RAID Group will start when the free space on the current RAID Group falls below the %Server Reserve times the Purge Factor. The Purge Factor is a whole number and is set to a value that allows enough time for the purge to complete on the next RAID Group before the application moves the current write location to that group. It is recommended that the Express Purge option be set on the Auto Purge. These parameters are specified on the Imaging Site Parameters window.

> Note: A BP Server must be assigned the PURGE task to run the Auto Purge.

- Scheduled

> The Purge will run at set intervals over all the Tier 1shares starting at a specified date/time as specified on the Imaging Site Parameters window.

> **NOTE:** A BP Server must be assigned the PURGE task to run the Scheduled Purge.

- Manual

> User-initiated Purge. Select one or more Tier 1 shares. The Purge Parameters and Express Purge options apply.

> Note: A BP Server does <u>not</u> have to be assigned the PURGE task to run a manual Purge.

### Purge Events Table 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the result codes for the Purge. Each file that is traversed is listed in either the Purge.html or PurgeError.html log file with its corresponding result code (See the Reports section)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 2%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Position</strong></th>
<th colspan="2"><strong>Field</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><strong>Purge.html/PurgeError.html</strong> (TGA, ABS, BIG extensions only)</td>
</tr>
<tr class="even">
<td><strong>Position</strong></td>
<td colspan="2"><strong>Field</strong></td>
<td colspan="2"><strong>Comments</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td colspan="2">Action</td>
<td colspan="2"><p>-3 = Foreign file. Not a valid file extension, do not purge.</p>
<p>-2 = Queued for Jukebox copy, do not purge.</p>
<p>-1 = Do not purge.</p>
<p>1 = If file is confirmed on Tier 2, meets normal date criteria and Tier 1 file size equals Tier 2 file size, then purge. If Tier 1 file size does not equal Tier 2 file size, then do not purge and do requeue file for Jukebox.</p>
<p>3 = If file is at alternate network location site , then purge and update Tier 1 pointer. If Tier 1 file size does not equal Tier 2 file size, then do not purge and do requeue file for Jukebox.</p>
<p>5 = If file is at alternate site, then purge and queue for Jukebox. If Tier 1 file size does not equal alternate site file size, then do not purge and do requeue file for Jukebox.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2">File Type</td>
<td colspan="2"><p>0 = Foreign</p>
<p>1 = Abstract</p>
<p>2 = Full</p>
<p>3 = Big</p>
<p>4 = Photo ID</p>
<p>5 = Advance Directive</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2">Status</td>
<td colspan="2"><p>1 = No 2005 entry. No Purge.</p>
<p>6 = Tier 2 pointer set. File on Tier 2. Tier 1 pointer incorrect location. Purge if image at other location.</p>
<p>7 = Tier 2 pointer set. File on Tier 2. No Tier 1 pointer set. Found file on Tier 1. Set Tier 1 pointer. No purge.</p>
<p>8 = Tier 2 pointer set. File on Tier 2. Tier 1 pointer set. File on Tier 1. Purge if file size match else queue for Jukebox.</p>
<p>9 = Record not in the IMAGE file (#2005). If queued for Jukebox, No Purge. If not in file #2005 or #2005.1, Purge.</p>
<p>10 = Foreign Image File, No Purge.</p>
<p>11 = Not an Image File, No Purge.</p>
<p>14 = Duplicate 2005/2005.1 entry. No Purge.</p>
<p>15 = Foreign Place. No Purge.</p>
<p>16 = Record only in Audit (2005.1) file. No Purge.</p>
<p>17 = Tier 2 offline. No Purge.</p></td>
</tr>
<tr class="even">
<td colspan="5"><strong>(File Types files - TXT extension is required - only)</strong></td>
</tr>
<tr class="odd">
<td colspan="2">1</td>
<td colspan="2">"AltLastFile"</td>
<td>Last non-ABS file on the share Neither a Full nor BIG file present in the share folder. Purge. Previous versions kept the File Types files in support of the ABS file.</td>
</tr>
</tbody>
</table>

## Starting/Running the Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purge can be started as an independent application, can be configured to run automatically in the background (see section *3.5.1 Purge Settings*), or can be scheduled to run in the background at prescribed time intervals (see section *3.5.1 Purge Settings*). The following steps describe how to run the purge in the foreground:

> **NOTE:** The Purge Retention Days and Purge By file dates are used by all the options listed below. Set these parameters before any of the purge options are run / scheduled.

1.  From the Windows Start \> Programs menu, select VistA Imaging Programs \> Background Processor \> Purge.
2.  Log into the application using a valid VistA access and verify code. (The secondary menu option All MAG\* RPC's \[MAG WINDOWS\] is required for access to all the BP Storage applications).

> The Purge application window opens.

> ![](vista-imaging-system-background-processor-user-manual/092.png)

3.  Select Edit \> Select Shares.

> The Purge Share Select window displays the shares.

> ![](vista-imaging-system-background-processor-user-manual/093.png)

4.  Highlight the shares to be purged and click OK.
5.  Click the Start button.
6.  Click OK in the message to confirm the shares to be purged.  
      
    The window closes and the purge starts. When the purge is complete, a summary sheet is displayed.

> ![](vista-imaging-system-background-processor-user-manual/094.png)

> Note: View the results in a log by selecting File \> Open log from the menu bar.

> The purge results are displayed by file type in the lower section of the window, along with a purge results summary. The resulting data is described in the table that follows.

> ![](vista-imaging-system-background-processor-user-manual/095.png)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Purged Files – DATE MODIFIED</p>
<p>Other possible values:</p>
<p>DATE ACCESSED</p>
<p>DATE CREATED</p></td>
<td>List of files on the current Tier 1 share (highlighted in the Share Processing window) that are deleted because they met the Purge criteria.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Activities</strong></td>
</tr>
<tr class="odd">
<td>Start Date</td>
<td>Start date of purge.</td>
</tr>
<tr class="even">
<td>Start Time</td>
<td>Start time of purge.</td>
</tr>
<tr class="odd">
<td>Run Time (hrs: mins: secs:)</td>
<td>Time to complete the purge.</td>
</tr>
<tr class="even">
<td>Total Files</td>
<td>Number of files checked.</td>
</tr>
<tr class="odd">
<td>Purge Count</td>
<td>Number of files purged.</td>
</tr>
<tr class="even">
<td>JB Queues</td>
<td>Number of files that were purge candidates, but not found on Tier 2. A JUKEBOX queue entry was created to copy the file to the archive. The file is not deleted.</td>
</tr>
<tr class="odd">
<td><p>Purge Criteria:</p>
<p>DATE MODIFIED</p>
<p>Other possible values:</p>
<p>DATE ACCESSED</p>
<p>DATE CREATED</p></td>
<td>Date criterion used to determine which files to delete.</td>
</tr>
<tr class="even">
<td>IEN Count</td>
<td><p>Number of unpurged IENs traversed since the last IEN purged on the current share. When the Purge operation is traversing through an IEN range that is rich with purge candidates, this number will be rapidly reset to zero. A continually growing IEN Count indicates that the Purge utility is in a range low in purge candidates. During a manual purge, the user may opt to stop the purge at that point.</p>
<p>The IEN Count is used in conjunction with the Express Purge Rate when Express Purge is active.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Purge Parameters</strong></td>
</tr>
<tr class="even">
<td>Site File Prefix: DM, IE, QRT</td>
<td>Namespace and multi-namespace names for the site.</td>
</tr>
<tr class="odd">
<td>Abstract keep days</td>
<td>Purge parameter indicating the time frame for keeping abstract files on Tier 1.</td>
</tr>
<tr class="even">
<td>Full keep days</td>
<td>Purge parameter indicating the time frame for keeping Full files on Tier 1.</td>
</tr>
<tr class="odd">
<td>Big keep days</td>
<td>Purge parameter indicating the time frame for keeping BIG files on Tier 1.</td>
</tr>
<tr class="even">
<td>Photo ID / Advance Directives keep days</td>
<td>Purge parameter indicating the time frame for keeping Photo ID / Advance Directives files on Tier 1.</td>
</tr>
<tr class="odd">
<td>Purge Criteria</td>
<td>Date criterion used to determine which files to purge. Options are Date Modified, Date Created or Date Accessed.</td>
</tr>
<tr class="even">
<td>Express Purge</td>
<td>Indicates if the Express Purge feature was used in this purge.</td>
</tr>
<tr class="odd">
<td>Express Purge Rate</td>
<td>The Express Purge will stop on a share when the IEN Count value reaches this threshold value.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Share Processing</strong></td>
</tr>
<tr class="odd">
<td>Tier 1 share paths</td>
<td>Location of shares being processed.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Original File Counts</strong></td>
</tr>
<tr class="odd">
<td>Abstract, Full Image, Big, Text, Photo ID, Advance Directives, Foreign</td>
<td><p>Breakdown by file type of original files processed</p>
<p><strong>Note</strong>: Legend on the right displays the count by file type. Text refers to File Types (extensions).</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Purged Files</strong></td>
</tr>
<tr class="odd">
<td>Abstract, Full Image, Big, Text, Photo ID, Advance Directives, Foreign</td>
<td><p>Breakdown by file type of files purged.</p>
<p><strong>Note</strong>: Legend on the right displays the count by file type. Text refers to File Types (extensions).</p></td>
</tr>
</tbody>
</table>

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three types of reports are produced to notify the site of important occurrences:

- Log files
- Emails
- Screen-generated output

### Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New log files are created as HTML files at the beginning of every session. HTML files are viewable, printable, and searchable. By default setting, the BP Purge log files reside in the C:\Program Files\VistA\Imaging\BackProc\log\purge directory. These files can be accessed by:

- Selecting File \> Open Log on the BP Verifier menu bar
- Using an Internet browser

They can be imported into an Excel spreadsheet.

#### Log File Format

Purge log files have the year-month-day and sequence number imbedded in the file name, as shown in the right pane of the window.

> ![](vista-imaging-system-background-processor-user-manual/096.png)

If more than one log file is run on the same day, the system adds a sequence number such as “01” following the date in the file name, as shown for the “PurgeError2009_08_18_01.html” file. For multiple runs on the same day, the highest sequence number is the latest log file run for the day.

The Purge run produces two types of log files shown—Purge*{date}*.html and PurgeError*{date}*.html.

#### Purge Log File

The Purge.html log file records the current share being purged as well as all of the successful deletions and the reason they were deleted. The following example shows a copy of the purge results.

> ![](vista-imaging-system-background-processor-user-manual/097.png)

| Name   | Description                                                                      |
|------------|--------------------------------------------------------------------------------------|
| Date/Time  | Date and Time of purge.                                                              |
| Event_Type | Displays the final purge criteria for the file listed. (See Purge Criteria section.) |
| Message    | Image file and access, creation, or modified date depending on the criteria.         |

#### PurgeError Log File

The PurgeError.html log file records the current share being purged as well as all of the files that were not deleted and the reason they were not deleted or other details related to the event. The following example shows a copy of the purge results.

![](vista-imaging-system-background-processor-user-manual/098.png)

| Name   | Description                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Date/Time  | Date and Time of purge.                                                                                                                |
| Event_Type | Displays the final purge criteria for the file listed and/or the share path on which the file was found. (See Purge Criteria section.) |
| Message    | Image file and access, creation, or modified date depending on the criteria.                                                           |

### Emails

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following e-mail messages are generated or triggered by the purge.

#### Scheduled_Purge_Failure Message

This message is sent by the Monitor Background Processor Activity \[MAGQ BPMONITOR\] menu option to indicate that the Scheduled Purge did not run. The BP Server may not have been assigned the PURGE task, therefore there is a risk that the shares will run out of free space. Run a manual purge, if necessary, until the problem is resolved.

Example of the message when the Purge is scheduled but fails to start:

> Subj: Scheduled_Purge_failure \[#31195\] 10/27/09@12:40 4 lines

> From: VistA Imaging MAGQCBP In 'IN' basket. Page 1 \*New\*

> ------------------------------------------------------------------

> SITE: IMGxxxxx.REDACTED

> DATE: Oct 27, 2009@12:40:01 EST

> The SALT LAKE CITY implementation of VistA Imaging has failed to start the sche

> dule Purge activity!

> The task is currently assigned to BP Server: ISW-xxxxx-LT

Example of the message when the PURGE task is not assigned to a BP Server:

> Subj: Scheduled_Purge_failure \[#31199\] 10/27/09@12:55 4 lines

> From: VistA Imaging MAGQCBP In 'IN' basket. Page 1 \*New\*

> --------------------------------------------------------------

> SITE: IMGxxx.REDACTED

> DATE: Oct 27, 2009@12:55 EST

> The SALT LAKE CITY implementation of VistA Imaging has failed to start the schedule Purge activity!

> The task is currently assigned to BP Server: Auto Purge is not currently assigned

### Screen-Generated Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the purge completes the Stop button is clicked, the results are displayed in a summary window. Use the option *print to file* to save this data.

#### Purge Results 

![](vista-imaging-system-background-processor-user-manual/099.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>[Purge Run Summary]</strong></td>
</tr>
<tr class="even">
<td>Start Date</td>
<td>Start date of purge.</td>
</tr>
<tr class="odd">
<td>Start Time</td>
<td>Start time of purge.</td>
</tr>
<tr class="even">
<td>Run Time</td>
<td>Time to complete the purge (hrs: mins: secs:).</td>
</tr>
<tr class="odd">
<td>Total Files</td>
<td>Number of files checked.</td>
</tr>
<tr class="even">
<td>JB Queues</td>
<td>Number of files that were purge candidates, but not found on Tier 2 A JUKEBOX queue entry was created to copy the file to the archive. The file is not deleted.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>[Purge Site Parameters]</strong></td>
</tr>
<tr class="even">
<td>Site File Prefix: DM, IE, QRT</td>
<td>Namespace and multi-namespace names for the site.</td>
</tr>
<tr class="odd">
<td>Abstract keep days</td>
<td>Purge parameter indicating the time frame for keeping abstract files on Tier 1.</td>
</tr>
<tr class="even">
<td>Full keep days</td>
<td>Purge parameter indicating the time frame for keeping Full files on Tier 1.</td>
</tr>
<tr class="odd">
<td>Big keep days</td>
<td>Purge parameter indicating the time frame for keeping BIG files on Tier 1.</td>
</tr>
<tr class="even">
<td>Photo ID keep days</td>
<td>Purge parameter indicating the time frame for keeping Photo ID files on Tier 1. (Includes Advance Directives)</td>
</tr>
<tr class="odd">
<td><p>Purge Criteria: DATE MODIFIED</p>
<p>Other possible values:</p>
<p>DATE ACCESSED</p>
<p>DATE CREATED</p></td>
<td>Date criterion used to determine which files to delete.</td>
</tr>
<tr class="even">
<td>Express Purge</td>
<td>Indicates if the Express Purge feature was used in this purge.</td>
</tr>
<tr class="odd">
<td>Express Purge Term</td>
<td>This value is file count. The purge will stop on a share when it processes this number of files and none have met the purge criteria to be deleted.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>[</strong>Tier 1 <strong>Share Count]</strong></td>
</tr>
<tr class="odd">
<td>Total Share Files</td>
<td>Total number of files traversed on the shares.</td>
</tr>
<tr class="even">
<td>Total Abstracts</td>
<td>Total number of .ABS files found.</td>
</tr>
<tr class="odd">
<td>Total Full</td>
<td>Total number of Full files found.</td>
</tr>
<tr class="even">
<td>Total Big</td>
<td>Total number of .BIG files found.</td>
</tr>
<tr class="odd">
<td>Total Text</td>
<td>Total number of .TXT files found /TXT refers to File Types (extensions).</td>
</tr>
<tr class="even">
<td>Total Photo ID</td>
<td>Total number of Photo ID files found.</td>
</tr>
<tr class="odd">
<td>Total Advance Directive</td>
<td>Total number of Advance Directive files found.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>[Purge File Count]</strong></td>
</tr>
<tr class="odd">
<td>Total Share Files Deleted</td>
<td>Total number of files deleted on all the shares processed.</td>
</tr>
<tr class="even">
<td>Purged Abstracts</td>
<td>Total number of .ABS files deleted on all the shares.</td>
</tr>
<tr class="odd">
<td>Purged Full</td>
<td>Total number of Full files deleted on all the shares.</td>
</tr>
<tr class="even">
<td>Purged Big</td>
<td>Total number of .BIG files deleted on all the shares.</td>
</tr>
<tr class="odd">
<td>Purged TXT</td>
<td><p>Total number of .txt files deleted on all the shares.</p>
<p>/TXT refers to File Types (extensions).</p></td>
</tr>
<tr class="even">
<td>Purged Photo ID</td>
<td>Total number of Photo IDs deleted on all shares.</td>
</tr>
<tr class="odd">
<td>Purged Advance Directive</td>
<td>Total number of Advance Directives deleted on all shares.</td>
</tr>
</tbody>
</table>

# System Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- Description of the BP Server Monitor Utility
- Configuring the BP Server Monitor
- Scheduling the BP Server Monitor
- Monitoring the BP Queue Processor
- Monitoring the BP Verifier
- Monitoring the BP Purge

=====================================================================

> **IMPORTANT:** The Imaging Coordinator's primary tasks involve monitoring the BP by reviewing the log files on a daily basis.

6.  

## Description of the BP Server Monitor Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP Server Monitor is a utility that sites can configure to monitor the activity of BP Server(s) in the VistA Imaging system. The utility sends an e-mail when one or more BP Servers are not operating properly and it monitors the <u>assigned</u> tasks of BP Server(s) to determine if:

- A task is lagging behind.
- The task has too many failed queues.
- A scheduled task has not executed.

The utility enables the Imaging Coordinator to evaluate the BP Server(s) to determine whether a network traffic problem exists, and to maintain the tasks effectively.

### Evaluating EVAL Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP Server Monitor does not evaluate <u>unassigned</u> tasks with the exception of the EVAL task. The EVAL queues are generated by DICOM Gateways where the Routing parameters have been set. Occasionally, sites mistakenly set the Routing parameters and thus create EVAL queues inadvertently. The BP Server Monitor utility reports on unprocessed EVAL queues when they reach a specified quantity. A site having a large number of EVAL queues may slow the BP Server client software when displaying the Queue Manager window.

### Reporting Using Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All reporting by the BP Server Monitor uses the following Mail Messages subject texts:

- VI_BP_Queue_Processor_failure
- Scheduled_Purge_failure
- Scheduled_Verifier_failure
- VI_BP_EVAL_Queue

Descriptions of these messages are in the Mail Messages section of the chapters *Queue Processor*, *Verifier*, and *Purge*.

> Recommendation: These Mail Messages should be configured to include the appropriate personnel responsible for resolving a problem, and to set up the message interval to control the number of messages sent. For details, see section *3.3 Configuring Mail Messages*.

## Configuring Mail MessagesConfiguring the BP Server Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP Server Monitor is a menu item in VistA, Monitor Background Processor Activity \[MAGQ BPMONITOR\] . This menu option must be executed on a regular basis and should be tasked using the VistA TaskMan Management menus.

The BP Server Monitor can be configured with site specific values when the utility is scheduled using the Kernel Scheduling menu (explained in the next section). The site configurable parameters are:

- MAGMIN – determines the lapse time between processing tasks. If the variable is undefined, then the default value is 15 minutes. If an active queue has not processed within *<u>specified</u>* minutes then a mail message is sent.
- MAGFQ – determines if failed queues per queue type have reached this limit. If the variable is undefined, then the default value is 1,000. If failed queues are above *<u>this limit</u>*, then a mail message is sent.
- MAGEVAL – determines if EVAL queues have reached this limit. If the variable is undefined, then the default value is 10,000. If EVAL queues are above *<u>this limit</u>*, then a mail message is sent.

## Scheduling the BP Server Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example of Scheduling 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If MAGMIN minutes have transpired since processing the last queue and there is another queue to be processed, then a MailMan message with subject text “VI_BP_Queue_Processor_failure” will be sent.  
Recommendation: Schedule this task to run every 10 to 15 minutes (site configurable).

### Tasking BP Server Monitor Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recommendation: Task the menu to run daily using the Kernel Scheduling menu option in the following example.

#### Example 1

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>On VistA, use the Schedule/Unschedule option [XUTM SCHEDULE] to task the activity:</p>
<p>Add the MAGQ BPMONITOR.</p>
<p>Set the date and time to run the monitor the first time.</p>
<p>Set the Rescheduled Freq., for example, 600S for 10 minutes. If the time is set for 10 minutes then the job will execute every 10 minutes. The S must be capitalized.</p>
<p>Example:</p>
<p>Select Taskman Management Option: Schedule/Unschedule Options</p>
<p>Example:</p>
<p>Select OPTION to schedule or reschedule: <strong>MAGQ BPMONITOR</strong> Monitor Background Processor Activity</p>
<p>Are you adding 'MAGQ BPMONITOR' as a new OPTION SCHEDULING (the 39TH)? No// <strong>Yes</strong></p>
<p>Option Name: MAGQ BPMONITOR</p>
<p>Menu Text: Monitor Background Processor Act TASK ID:</p>
<p>__________________________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: OCT 20,2009@24:00</p>
<p>DEVICE FOR QUEUED JOB OUTPUT:</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: <strong>600S</strong>__________________________</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________________________</p>
<p>If this field is blank then the job will run only once.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example 2

The following example is obtained by entering NEXT at the COMMAND prompt. Arrow down to the bottom to see the COMMAND: prompt. This example uses the parameters mentioned in section *7.2, Configuring the BP Server Monitor* to configure the utility to meet the needs at your site.

> **IMPORTANT:** When configuring the MAGMIN parameter, consider your site’s Imaging network topology. If your site’s Imaging network has remote network locations, then 15 minutes may be too low for the lapse time and should be adjusted accordingly.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Optional parameters are:</p>
<ul>
<li><p>MAGFQ, the variable for the sensitivity value for failed queues.</p></li>
<li><p>MAGMIN, the variable for the sensitivity value for the time lapse between queue processing.</p></li>
<li><p>MAGEVAL, the variable for the sensitivity value for EVAL queues.</p></li>
</ul>
<p>Edit Option Schedule</p>
<p>Option Name: MAGQ BPMONITOR</p>
<p>_____________________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: <strong>MAGFQ</strong> VALUE: <strong>50</strong></p>
<p>VARIABLE NAME: <strong>MAGMIN</strong> VALUE: <strong>25</strong></p>
<p>VARIABLE NAME: <strong>MAGEVAL</strong> VALUE: <strong>50000</strong></p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________________________</p>
<p>COMMAND:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Arrow down until “Command:” appears and then enter E for Exit, answer YES to Save changes that have been made.

## Monitoring the BP Queue Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP Server Utility handles all the entries that exist in the BP SERVER file (#2006.8) and the BP queues assigned to each server.

> **NOTE:** The following procedures are not required. They are suggested as efficient ways to monitor the BP Queue Processor as a preventative measure.

### Precautionary Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-background-processor-user-manual/100.png)The BP Queue Processor should not be run under the following conditions:

- When network outages or VistA Hospital Information System outages occur
- During upgrades and file server malfunctions that result in the loss of connectivity to all VistA Imaging shares or to all Tier 2 devices
- When jukebox maladies occur such as configuration management tool outages, jammed picker arms, or shortages of newly formatted platters

### Daily Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Make sure the BP Server Monitor is running in the background in TaskMan.
2.  If BP Monitor is not used, verify queue entries are being processed.
3.  Monitor email for alerts that were set up through the application.
4.  Check Queue Manager for any failed JUKEBOX, IMPORT, JBTOHD or GCC entries that need to be re-queued.
5.  Run the Verifier daily or weekly over the range of images that were processed in that time period. This can be scheduled to run for your chosen interval.
6.  Examine the Verifier log file *No_Archive.log* for entries with a blank in the “2005.1”column. These files are missing on your Imaging system (Tier 1 and Tier 2 storage).

## Monitoring the BP Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verifier scans can be run any time of the day as there is minimal impact on VistA. They should be run based on the following reasons:

- Routine Scanning Of Newly Acquired Images

> The Verifier should be run every 1 or 2 weeks to verify new entries in the IMAGE file (#2005). In some cases, if images are missing, they can be resent from the modality.

- Periodic Maintenance of the VistA Imaging System

> The Verifier should be run several times each year to verify the entire range of Image Internal Entry Numbers (IENs). During the year, many files will be retrieved from Tier 2 and pointers updated in the database. This will ensure that files on the Tier 1 and the Tier 2 can be accurately located.

- Large Image Share Population Events

> The Verifier should be run over the range of Image (IENs) that were copied back to the Image shares from the Tier 2. There may be occasions where files were not copied and incorrect file pointers set in the database with this large volume of files being moved to the Tier 1.

- Tier 1 share or Tier 2 outages

> The Verifier should be run after the resolution of any event that interrupted the flow of images to Tier 2. The Queue Processor will attempt to copy files to Tier 2 three times. At that point it will indicate failure and begin processing the next entry in the queue.

> Note: These files reside ONLY on the Image shares and therefore MUST be copied promptly to Tier 2 using the Verifier.

- Offline Platters

> When the jukebox is physically full and space is needed to add additional platters, the OFFLINE IMAGE utility MUST be used (See *Chapter 9 Jukebox Archive* in the *VistA Imaging System Technical Manual*) prior to physically removing the platters. This utility will mark the IENs as being archived and the Verifier will skip these while processing.

## Monitoring the BP Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Precautionary Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-background-processor-user-manual/101.png)The BP Purge should not be run under the following conditions:

- When Tier 2or VistA Imaging shares access is compromised
- When excessive jukebox copies will automatically be queued by the BP Purge because copies cannot be verified on Tier 2
- When the BP Purge does not have access to the VistA Imaging shares it is intended to purge
- When the VistA hospital system is not available
- When the RPC Broker Listener is not active
- When the network is down

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=====================================================================

- General Startup
- Queue Processor
- Verifier
- Purge
- Import API

=====================================================================

7.  

## General Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unable to connect to server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the server is incorrectly entered, or an inaccessible server is specified, the following error may be displayed by the application:

![](vista-imaging-system-background-processor-user-manual/102.png)

- Restart the Queue Processor, which opens the”Connect To” dialog, shown below.

> ![](vista-imaging-system-background-processor-user-manual/103.png)

- Within this window, you should choose one of the following options:
- Try to reconnect to the server if you are sure the server information is correct. If the error reoccurs, you may have to request a System Administrator to check for connectivity issues.
- Add a new server by clicking New.
- Then enter new server information in the dialog that opens (below).

![](vista-imaging-system-background-processor-user-manual/104.png)

### Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user enters invalid Access/Verify Codes while logging into VistA, the system may display the following error message.

![](vista-imaging-system-background-processor-user-manual/105.png)

This message could mean that the credentials were incorrectly entered, or the ACCESS CODE/VERIFY CODE pair are not configured on the selected VistA Server.

- Click OK, and carefully reenter the user’s credentials.
- Should the issue continue to occur, contact the System Administrator to verify user credentials.

## Network Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check all the online VistA Imaging Tier 1 shares and Tier 2 shares by one of the following means to determine if the BP has access to the folders/files on the shares. There are several methods to test the connectivity:

1.  From the Main BP window, select the View \> Server Size option.  
    The free space should display for each share.

> ![](vista-imaging-system-background-processor-user-manual/106.png)

2.  Using Windows Explorer on the destination device (Image cluster or Windows-based Jukebox server), show the properties of the VistA Imaging Tier 1 shares and Tier 2 shares.  
    The VHAxxxIA account that is used to log into the BP Server should have READ/WRITE access to both the shares and folders/files on those shares.

> Note: For sites using the Archive Appliance (AA), contact the HP Expert Center.

3.  Open a DOS window. At the command prompt type *dir [\\server\share](file://server/share)* (the server could be a cluster server or the jukebox server). Traverse down a couple folders under the main level the folders/files should be visible
4.  If any of these methods fail, open a DOS window and use the DOS *ping* command to see if the server is accessible on the network.
5.  If the server is accessible, try mapping the share thru Windows Explorer. Explorer will display any error messages. If the server is not accessible, contact the network admin to troubleshoot.

### Broker Failures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the connection to the Broker fails:

- Verify the PORT and Server are correct in the registry
- Close and restart the application.
- Open a DOS window and use the *ping* command to see if the VistA server is available
- Verify that the listener is running in VistA
- Validate that the Access/Verify codes have not expired.
- Check the security on the Access/Verify account. Make sure:
  - The MAG SYSTEM security key is assigned
  - The All MAG\* RPC's \[MAG WINDOWS\] menu option is assigned

### Not Enough Server Cache

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message indicates that:

- The share on the server is not accessible. Follow the steps in section *8.1.1 Network Connection* to troubleshoot.
- The free space on the Image shares is below the % Server Reserve.
  - Disable the Auto Write Location Update option.
  - Set the write location manually to a share with cache space available.
  - If no share has adequate free space, create a second BP Server and manually launch a Purge (in *Chapter 6Purge*) to run on all shares. When the Purge has run and generated free space on a share, set the Write location manually to that share.

### Not Enough Process Memory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Close all the applications and reboot the server. If the problem persists, contact the National Help Desk.

### Not Enough Write Cache Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This message refers to the DiskXtender cache on the jukebox and indicates there is no free space on the jukebox share, or for Archive Appliance sites a possible space issue exists.

- Verify the share is accessible. Follow the steps in section *8.1.1 Network Connection* to troubleshoot.
- Click the Extended Drive in DiskXtender to see if there is free space available. Also, use Windows Explorer on the JB server to see if Windows is properly reporting free space.
- Check the Move Group within the DiskXtender application to see if there are platters with available space. If not, add additional optical platters to the Move Group. See the *DiskXtender User Manual*.
- Run a Drive Scan on the share. See the *DiskXtender User Manual*.

## Queue Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Create Process failed'+ProgramName</td>
<td>A system error occurred staring the process</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
<tr class="even">
<td>Increment <em>queue_name</em> Ptr^Failed</td>
<td>The QUEUE POINTER (#1) in the IMAGE BACKGROUND QUEUE POINTER file (#2006.031) in VistA could not be updated</td>
<td>On the main BP window, use the Edit &gt; Refresh Queue Counts to correct the current counts. Close the BP and restart the application.</td>
</tr>
<tr class="odd">
<td>Initialization Failure^Log Files at: C:\Program Files(x86)\Vista\Imaging\Backproc\Log\BackProc\BPError.log</td>
<td>Log file could not be created</td>
<td>Check permissions on the log folder</td>
</tr>
<tr class="even">
<td>RAID groups not properly configured</td>
<td>An active RAID Group has no online shares</td>
<td><p>Make sure online RAID Group has online shares.</p>
<p>Use the Network Location Manager to reset your RAID groups</p></td>
</tr>
<tr class="odd">
<td>Requeue Failure trying to Requeue:</td>
<td>An attempt to re-queue a failed queue entry failed</td>
<td>Use the Queue Manager and step past the queue entry. Determine the problem with the entry that would not re-queue.</td>
</tr>
<tr class="even">
<td>SetTime Handle – Destin: C:\Program Files (x86)\Vista\Imaging\Backproc\Log\BackProc\BPError.log Access is Denied</td>
<td>Could not write the Access Date on the log file</td>
<td>Check the file permissions on the log folder listed.</td>
</tr>
<tr class="odd">
<td>The Background Processor client software is version <em>n.n.n.n</em>. VistA Imaging Host system has version <em>m</em> installed. Please update to compatible client and host software. Shutting down the Background Processor...</td>
<td>The client software that is installed does not match the KIDS version installed on VistA.</td>
<td>Shut down the Background Processor client and install the required KIDS on VistA.</td>
</tr>
<tr class="even">
<td>The Site parameter context could not be determined. The application will terminate.</td>
<td>The PLACE global is corrupt</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation. </td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-background-processor-user-manual/107.png)</td>
<td>The Broker is not properly configured in the registry of this server.</td>
<td><p>Edit the registry on this server to meet the connection requirements on the host server with proper host server name and port number.</p>
<p>Note: on 64-bit OS the hive is</p>
<p>[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Vista\Broker\Servers]</p></td>
</tr>
<tr class="even">
<td>This server is not yet configured for BP queue task processing!</td>
<td>There is either no BP Server name with this network name in the BP Server file (#2006.8) or there are no task(s) assigned to this server</td>
<td>Create a BP Server and assign tasks to it in Edit | BP Servers</td>
</tr>
<tr class="odd">
<td>InitLogFile: procedure NewCreationDate | SetFileTime Failed <em>WIN32_Error</em></td>
<td>Log File Initialization error</td>
<td>The log files should not have a local drive in the BP Server Parameters. The designated path should be a network share and should end with a backslash “\”. Note: The Computer name is automatically set by the application software. Setting the server name in the parameter will create a confusing duplicate descendant server tree on the Network share.</td>
</tr>
</tbody>
</table>

### Runtime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0^Accusoft Control creation error : &lt; <em>error message</em> &gt;</td>
<td>The Import API uses the AccuSoft Image Gear Toolkit to create the watermarked image. If an error occurs during the creation of AccuSoft controls, the error message displays describing the error.</td>
<td>The AccuSoft controls are installed during MAG client installation. If this error message occurs, contact the VistA Imaging system manager.</td>
</tr>
<tr class="even">
<td>0^Image is missing from input data.</td>
<td>The image to be watermarked is not in the Import Queue Data.</td>
<td>Check the IMAGE file (#2005) to see if the data is corrupt.</td>
</tr>
<tr class="odd">
<td>0^Watermark failure : &lt;<em>error message</em>&gt;</td>
<td>The process of burning the “Rescinded” watermark onto the image file failed.</td>
<td><p>The AccuSoft ToolKit could not create the watermarked image.</p>
<p>Check if the rescinded bitmap exists in the image directory <strong>C:\Program Files (x86)\VistA\Imaging\BackProc\MagRescinded.bmp</strong>.</p>
<p>You may need to reinstall the Current KIDS to correct AccuSoft ImageGear problems.</p></td>
</tr>
<tr class="even">
<td>An Abstract for this file is on the Jukebox, a JBTOHD is being queued</td>
<td>ABSTRACT - The abstract pointer on the Tier 1 is empty. The abstract will be copied from the jukebox</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Could not complete</td>
<td>DELETE - file could not be deleted</td>
<td>Check permissions on Tier 1 share</td>
</tr>
<tr class="even">
<td>Could not complete/Requeued</td>
<td>DELETE - file could not be deleted</td>
<td>Check permissions on Tier 1 share</td>
</tr>
<tr class="odd">
<td>Current Tier 1 Shares^Exception: No RAID group Assigned</td>
<td>The Tier 1 share must be assigned to a RAID Group</td>
<td>On the BP main window, use Edit &gt; Network Location Manager to assign the Tier 1 share(s) to a RAID Group.</td>
</tr>
<tr class="even">
<td>False Positive Copy f<em>ilename(Source)</em>,<br />
<em>filenames source file size</em>, <em>file size(jukebox)</em></td>
<td>File sizes on source and destination don’t match. File not copied.</td>
<td>Determine if images are for different patients</td>
</tr>
<tr class="odd">
<td>File copied was of size zero</td>
<td>IMPORT - The file size is zero</td>
<td>Resend image from import source</td>
</tr>
<tr class="even">
<td>File of size zero created then deleted</td>
<td>MAKEABS - file of zero length was created by Mag_MakeAbs.exe. It was deleted.</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
<tr class="odd">
<td>File was not found</td>
<td>IMPORT - file does not exist on the image share</td>
<td>Resend image from import source</td>
</tr>
<tr class="even">
<td><em>filename</em> Source file does not exist.</td>
<td>Could not find source file</td>
<td>Run Verifier to correct VistA pointers</td>
</tr>
<tr class="odd">
<td><em>fileshare</em>: Cannot connect to the Export Share.</td>
<td>EXPORT - Cannot map to the remote share</td>
<td>Check for network connectivity.<br />
Check permissions.</td>
</tr>
<tr class="even">
<td>ForceDirectories failed:</td>
<td>DELETE - could not create directory on Tier 2 share</td>
<td>Check permissions on Tier 2 share</td>
</tr>
<tr class="odd">
<td>Image File type: <em>filename.ext</em> is an Unsupported Format</td>
<td>ABSTRACT - The Full file is not a supported Imaging file type so the abstract cannot be created.</td>
<td>Examine the "foreign" file and determine if the extension was misnamed.</td>
</tr>
<tr class="even">
<td>Invalid Imaging Network Username or Password.</td>
<td>The BP processor operator does not have write permissions on Tier 1, Tier 2, the Network Log file share, or the IMPORT share.</td>
<td>Check permissions on the share the write share associated with this error.</td>
</tr>
<tr class="odd">
<td>Jukebox is not available: <em>filepath</em> <em>Volume label</em></td>
<td>JUKEBOX – The Tier 2 share is not available</td>
<td>Ping the Tier 2 server. Check the Tier 2 share permissions.</td>
</tr>
<tr class="even">
<td>Jukebox sourcefile unavailable</td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is not set.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>JUKEBOX: <em>queue _pointer</em> ^f<em>ile_extension<br />
</em> Not copied</td>
<td>JUKEBOX - Alternate file extension (i.e. .TXT) was<br />
not copied</td>
<td>Check file permissions</td>
</tr>
<tr class="even">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>Check for network connectivity.</td>
</tr>
<tr class="odd">
<td>Login Message^Silent Login attempt failed!</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>In Imaging Site Parameters, re-enter the VistA Access and VistA Verify codes for the BP User. Also check that this user has only one Division assigned in file 200, New Person file.</td>
</tr>
<tr class="even">
<td>Make AbstractError / abs is already present</td>
<td>ABSTRACT- file already exists at the Tier 1 location specified in VistA</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Make AbstractError / f<em>ilename</em></td>
<td>MAKEABS- the Mag_MakeAbs.exe could not create the abstract file</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
<tr class="even">
<td>NetConError Using User credentials <em>WIN32_Error</em></td>
<td>GCC - Could not logon to the remote location with the Username/Password in VistA</td>
<td>Correct the Username/Password for the<br />
GCC location in Network Location Manager.</td>
</tr>
<tr class="odd">
<td>NetConError, There is no password associated with this Network Location: <em>share_name</em></td>
<td>GCC - The password field is empty for this Network Location</td>
<td>Enter a password for this GCC location</td>
</tr>
<tr class="even">
<td>No Image file entry was created!</td>
<td>IMPORT - an IEN was not created in the image file</td>
<td>Resend image from import source</td>
</tr>
<tr class="odd">
<td>No Jukebox sourcefile available / Attempting Abstract Queue</td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is set. The Queue Processor will attempt to make one from the Full or BIG file.</td>
<td>None</td>
</tr>
<tr class="even">
<td>No Tracking ID IMPORT failed</td>
<td>IMPORT - unique Tracking ID parameter is missing from IMPORT</td>
<td><p>Resend image from import source.</p>
<p>Use the Queue Manager to check the Import Queue Properties for failed IMPORTS.</p></td>
</tr>
<tr class="odd">
<td>Problem renaming log file: <em>filename</em></td>
<td>Could not rename log file to a versioned copy</td>
<td>Check permissions on the existing folder/files</td>
</tr>
<tr class="even">
<td><em>queue_pointer</em> ^Size Mismatch <em>queue_type</em> copy not overwritten.</td>
<td>File sizes on source and destination don’t match. File not copied.</td>
<td>Determine if images are for different patients</td>
</tr>
<tr class="odd">
<td>SetFileTime Failed</td>
<td>Could not set Access date on the log file.</td>
<td>None</td>
</tr>
<tr class="even">
<td>The BP Queue executed a scheduled RAID Group Advance</td>
<td>The Queue Processor performed a scheduled RAID Group Advance to the next group with adequate free space per the site parameter configuration</td>
<td>Verify that the tape backup schedule is synchronized with this Tier 1 write location update</td>
</tr>
<tr class="odd">
<td>The BP Queue executed an automatic RAID Group Advance</td>
<td>The Queue Processor performed an automatic RAID Group Advance to the next group with adequate free space per the site parameter configuration</td>
<td>Verify that the tape backup schedule is synchronized with this Tier 1 write location update</td>
</tr>
<tr class="even">
<td>The jukebox copy: <em>filename</em> does not exist -- attempting a copy...</td>
<td>DELETE -Could not find the file on jukebox shares. Try to copy from Tier 1 shares to jukebox</td>
<td>None</td>
</tr>
<tr class="odd">
<td>The RAID share is not on-line</td>
<td>IMPORT - The Tier 1 share is not available</td>
<td>Check the permissions on the image share indicated</td>
</tr>
<tr class="even">
<td>The <em>src_filename</em> to <em>dest_filename</em> copy failed.</td>
<td>EXPORT - file could not be copied</td>
<td>Check for network connectivity.<br />
Check permissions.</td>
</tr>
<tr class="odd">
<td>The VistA cache file: <em>filename</em> not found</td>
<td>DELETE -Could not find the file on Tier 1 share to delete</td>
<td>None</td>
</tr>
<tr class="even">
<td>This Server is not yet configured!</td>
<td>A BP Server has not been associated with this server.</td>
<td>Create a BP Server entry for this processor using Edit | BP Servers</td>
</tr>
<tr class="odd">
<td>Unable to copy to the Jukebox: Not enough write cache available</td>
<td>JUKEBOX - The Tier 2 share is not available or is full</td>
<td>Determine why the Tier 2 share is full. Possibly add new platters to the jukebox or add storage. Check network connection.</td>
</tr>
<tr class="even">
<td>Zero size <em>queue_type</em> copy NOT overwritten</td>
<td>Zero size file on the destination could not be overwritten</td>
<td>Remove zero size file</td>
</tr>
<tr class="odd">
<td>No Connection to VISTA</td>
<td>The VistA Access and Verify codes of the user or service account are invalid.</td>
<td>Update the Access and Verify codes on the BP Site parameter window.</td>
</tr>
</tbody>
</table>

## Verifier 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start/Run

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>About to exit without processing: 0</td>
<td>There are no IEN records within the range.</td>
<td>Choose another IEN range</td>
</tr>
<tr class="even">
<td>Broker Connection to server could not be established!</td>
<td>VistA RPC Broker is not currently in a listening state OR the application has timed out.</td>
<td>Close the application and restart. Check with the VistA system manager for the status of the Broker listener.</td>
</tr>
<tr class="odd">
<td>CC:createcontext<br />
("MAG WINDOWS") could not be established!</td>
<td>The user does not have All MAG* RPC's [MAG WINDOWS] menu option assigned.</td>
<td>Assign the user this menu option.</td>
</tr>
<tr class="even">
<td>lbCacheShare.items.Count &lt; 1: MAGQ SHARES</td>
<td>There are no online, non-router VistA Imaging Shares .</td>
<td>Use the Queue Processor’s Network Location Manager to check/add the shares.</td>
</tr>
<tr class="odd">
<td>Invalid Input Range</td>
<td>The From and To values entered in the Range are not correct (e.g. Start: 0 End: 0).</td>
<td>Enter a valid <em>From</em> and <em>To</em> range.</td>
</tr>
<tr class="even">
<td>jukebox shares are not setup</td>
<td>The Tier 2 share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).</td>
<td>Create/Edit the Tier 2 shares in the Network Location Manager on the Queue Processor.</td>
</tr>
<tr class="odd">
<td>This workstation is not currently setup as a Background Processor.</td>
<td>There is no BP Server set up for this machine.</td>
<td>Use the option <em>BP Servers</em> on the Queue Processor to register this server.</td>
</tr>
<tr class="even">
<td>Verifier client software is version nnn. VistA Imaging Host software is version mmm. Please update to compatible client and host software. Shutting down Verifier...</td>
<td>The version of the KIDS file installed on VistA does not match the executable version on the workstation.</td>
<td>Install the latest KIDS and client software.</td>
</tr>
<tr class="odd">
<td>VistA shares are not setup</td>
<td>The image share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).</td>
<td>Create/Edit the shares in the Network Location Manager on the Queue Processor.</td>
</tr>
</tbody>
</table>

### Output HTML Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Aggregate JB Copy Error:</td>
<td>Could not copy from alternate Tier 2 to the current Tier 2 Write location.</td>
<td>Check permissions</td>
</tr>
<tr class="even">
<td>Abs to JB:</td>
<td>Abstract has been created and copied to the jukebox</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Aggregate Function - Enabled</td>
<td>Software is enabled to copy files from secondary Tier 2, if necessary</td>
<td>None</td>
</tr>
<tr class="even">
<td>BIG Aggregate Failed</td>
<td>Could not copy BIG file from secondary Tier 2</td>
<td>Check file existence/permissions</td>
</tr>
<tr class="odd">
<td>Create Process failed</td>
<td>Could not create process on VistA for Verifier</td>
<td>Check Error Trap</td>
</tr>
<tr class="even">
<td>Empty FBIG node</td>
<td>"FBIG" node has no pointers set in IMAGE file (#2005) record.</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="odd">
<td>File of size zero created then deleted</td>
<td>Abstract file created of size zero. Then it is deleted.<br />
(Likely corruption of BIG and/or TGA file)</td>
<td>None</td>
</tr>
<tr class="even">
<td>FULL Aggregate Failed</td>
<td>Could not copy FULL file from secondary Tier 2.</td>
<td>Check file existence/permissions</td>
</tr>
<tr class="odd">
<td>Images JB share is OFF-LINE:</td>
<td>Tier 2 is offline</td>
<td>Set Tier 2 back ONLINE</td>
</tr>
<tr class="even">
<td>Make AbstractError</td>
<td>Abstract file could not be created from TGA/BIG<br />
(BIG/TGA not found or image file corruption).</td>
<td>Check shares for existence of BIG/TGA file. If not found, restore BIG/TGA file from backup tapes.</td>
</tr>
<tr class="odd">
<td>New Abs to CWL</td>
<td>An abstract file has been created and copied to the current write image share</td>
<td>None</td>
</tr>
<tr class="even">
<td>No ABS file VC Ptr Cleared</td>
<td>Abstract file not found on the Image share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>No ABS file VC Share OFF-Line</td>
<td>Image share is offline at location of abstract file</td>
<td>Set share back online and re-run Verifier</td>
</tr>
<tr class="even">
<td>No ABS JB Files</td>
<td>No abstract file found on Tier 2</td>
<td>Check shares for existence of ABS file. If not found, restore ABS file from backup tapes</td>
</tr>
<tr class="odd">
<td>No Acquisition Site in Image file</td>
<td>The ACQUISITION SITE field #100 in the IMAGE file (#2005) is missing. This is a required field.</td>
<td><p>Contact IRM</p>
<p>Update the field with the proper site ID.</p></td>
</tr>
<tr class="even">
<td>No FULL JB Files</td>
<td>FULL file not found on the Tier 2</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes</td>
</tr>
<tr class="odd">
<td>No FULL VC Files</td>
<td>FULL file not found on the Tier 1 share</td>
<td>None</td>
</tr>
<tr class="even">
<td>No jukebox BIG Files</td>
<td>BIG file not found on the Tier 2</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="odd">
<td>No jukebox FULL Files</td>
<td>FULL file not found on the Tier 2</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes.</td>
</tr>
<tr class="even">
<td>No Network References</td>
<td>No IMAGE file (#2005) record exists for this image</td>
<td>Re-import image thru the Capture client</td>
</tr>
<tr class="odd">
<td>No Network References: Archived Image</td>
<td>Image has been archived, resides in the IMAGE AUDIT file (#2005.1)</td>
<td>None</td>
</tr>
<tr class="even">
<td>No VC BIG Files</td>
<td>Could not find the BIG file on the Tier 1 share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Not Certed</td>
<td>Could not find/create file type on Tier 2</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="even">
<td>Problem rename log file:</td>
<td>Permission problem with log file</td>
<td>Set WRITE permissions set on share/folder/file for Windows login account.</td>
</tr>
<tr class="odd">
<td>Text file Patient ID not in VistA</td>
<td>Could not locate patient ID in VistA</td>
<td>Contact IRM</td>
</tr>
<tr class="even">
<td>TXT to BIG VC</td>
<td>Copy TXT file to same share as BIG file</td>
<td>None</td>
</tr>
<tr class="odd">
<td>TXT to FULL VC</td>
<td>Copy TXT file to same share as FULL file</td>
<td>None</td>
</tr>
<tr class="even">
<td colspan="3"><strong>"Check Text" Option Messages</strong></td>
</tr>
<tr class="odd">
<td>Text File Corruption Error Type 1:</td>
<td>Text file is binary or unreadable</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="even">
<td>Cannot determine Text file type:</td>
<td>Foreign text file was not likely generated on the image gateway</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="odd">
<td>Text File Corruption Error Type 2:</td>
<td>Text file is ASCII but has unprintable characters or truncated</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="even">
<td>Text/Image DFN Mismatch:</td>
<td>Patient ID in text file does not match that in VistA</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Text/Image SOP/UID Mismatch</td>
<td>The Series Instance UID in the text file does not match the one in VistA</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Text/Image Study/UID Mismatch</td>
<td>The Study Instance UID in the text file does not match the one in VistA</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Text/Image UID Mismatch</td>
<td>SOP and/or Study UID are/is blank in text file</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Updated Text file</td>
<td>Text file has been edited</td>
<td>Validate file has been copied to Tier 2</td>
</tr>
<tr class="odd">
<td>No SSN Found</td>
<td>Patient ID field missing in text file</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

### Integrity Messages on Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are integrity issues that will prevent their respective images from being displayed and others that will not impact the viewing. See Appendix C for sample output.

#### Conditions Preventing Viewing

An integrity error message will be generated when the image is retrieved for viewing on these conditions and the patient image will not be viewable until the condition is corrected, or the user has the proper key to view these images.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No Image Ptr in AP</td>
<td><blockquote>
<p>The Clinical Association Report (AP) for this image does not contain an image entry that points back to this image.</p>
</blockquote></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP has no images</td>
<td>Image series that does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting AP &amp; Image DFNs</td>
<td>The patient file reference (DFN) in the Clinical Association Report (AP) does not match the DFN in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Invalid Image Ptr to AP</td>
<td>The Clinical Association Report (AP) has image references that are not in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting GP and GO DFN</td>
<td>The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP &amp; GO AP Mismatch</td>
<td>The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>GP Missing GO Ptr</td>
<td>The Group Object multiple of the referenced Group Parent does not reference this group object.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>No AP Mult Ptr</td>
<td>This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005).record is missing the <em>PARENT DATA FILE IMAGE POINTER</em> (#17) for a Clinical Association Report (AP).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>GO DFN mismatches</td>
<td>Some image file Group Objects have different PATIENT references (DFN).</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Image entry is structurally abnormal</td>
<td>The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non-Group image (NG) is corrupt.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Missing Group Objects</td>
<td>The Group Parent has Group Object references that are missing.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>DFN Mismatches in AP Image Mult</td>
<td>The Clinical Association Report (AP) references a Group Parent that has image files with a different PATIENT reference (DFN) than the report.</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

#### Conditions Allowing Viewing

The following integrity issues will not prevent their respective images from being displayed. These are informational messages.

| Message     | Explanation                                                                                                                                                                                   | Action           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| No AP Ptr       | The IMAGE file (#2005) record is missing the PARENT DATA FILE# (#16) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified.       | Future utility patch |
| No AP entry Ptr | This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the *PARENT GLOBAL ROOT DO (#17)* for a Clinical Association Report (AP). | Future utility patch |

## Purge 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Broker Reconnection failed</td>
<td>Auto login after a Broker disconnect failed</td>
<td><p>Check network.</p>
<p>Re-enter Access and Verify codes for the BP user and be sure the user has only one Division.</p></td>
</tr>
<tr class="even">
<td>Create Process failed <em>ProgramName</em>,</td>
<td>Windows failed to create a process.</td>
<td>Reboot the server.</td>
</tr>
<tr class="odd">
<td>Express Purge Rate limit reached: <em>PurgeRate</em> on share: <em>CurrentShare</em></td>
<td>The purge terminated on the given share because Express Purge was active and the Purge process exceeded the user defined purge rate.</td>
<td>None</td>
</tr>
<tr class="even">
<td>File Delete failure: <em>filename</em></td>
<td>The file listed could not be deleted.</td>
<td>Check permissions on the share/folder/file</td>
</tr>
<tr class="odd">
<td>File in use: <em>filename</em></td>
<td>The log file is in use</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td>File purged: <em>filename</em>. 'The Image file (#2005) was not updated'</td>
<td>The file was deleted on Tier 1, but the pointer in VistA could not be updated.</td>
<td>Validate the IEN record exists in VistA.</td>
</tr>
<tr class="odd">
<td>Findfirst failed <em>filename</em></td>
<td>The directory traversal failed</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td>Log File Archival reset to: <em>FilePath2</em> instead of: <em>FilePath1</em></td>
<td>The logs files are now being stored at another location.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Login Message^Broker Reconnection Successful</td>
<td>After a Broker disconnect, the application was able to reconnect to VistA.</td>
<td>None</td>
</tr>
<tr class="even">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>After a Broker disconnect, the application tries 3 times to reconnect to VistA</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Login Message^Silent Login attempt failed!</td>
<td>After a Broker disconnect, the application was not able to reconnect to VistA.</td>
<td>Check network connections. Check Access and Verify codes and single division for BP user.</td>
</tr>
<tr class="even">
<td>NewCreationDate^SetFileTime Failed <em>filename</em></td>
<td>Could not set the date of last Access on filename</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Non-Connection related Broker error</td>
<td>Broker disconnected</td>
<td>Check VistA for error trap</td>
</tr>
<tr class="even">
<td>NOT Purged criteria: <em>EvalCriteria</em> NOT PURGED-JUKEBOX QUEUED <em>filename date</em></td>
<td>File was not deleted. See Section 6.4 Purge Criteria.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Problem renaming log file <em>filename1</em> -&gt; <em>filename2</em></td>
<td>Could not rename log file to versioned log file name</td>
<td>Check permissions.</td>
</tr>
<tr class="even">
<td>Purge Criteria: <em>EvalCriteria</em> <em>filename filedate</em></td>
<td>See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Purge Criteria: <em>EvalCriteria</em> NOT PURGED <em>filename filedate</em></td>
<td>File was deleted. See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="even">
<td>Silent Login attempt</td>
<td>Broker was disconnected. Auto login is initiated.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Start Date failure</td>
<td>Problem with Date of Last Purge on Scheduled Purge</td>
<td>Clear the record in the Imaging Site Parameter file (#2006.1).</td>
</tr>
</tbody>
</table>

## Import API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Import API OCX (IAPI OCX) traps System Error Codes in all of the Windows function calls that are made during Import processing. When an Error occurs, the Error Code and Error Description are listed in the Result Array that is returned by the Import API.

Descriptions of the error codes are returned using the Windows function: GetLastError.

> **NOTE:** The System Error Codes are very broad. Each one can occur in one of many hundreds of locations in the system. Consequently, the descriptions of these codes cannot be very specific. Use of these codes requires some amount of investigation and analysis. Make note of the run-time context in which these errors occur.

Along with the System Error code and description, the values of other IAPI parameters will also be listed in the Result Array when an error occurs. The other values will help determine the exact cause of the error.

Not all of the values listed below will be returned in the Result Array. Depending on the type of error, some values will be listed while others may or may not exist at the point in the process when the error occurred.

An example of this is the Access Verify codes. These values will be listed if an error occurs during login to the database only.

Other values include:

- Import Queue number
- Image Share File Path
- Password
- Tracking ID
- Server\Share Name
- Access Code
- File to Import Full Patch
- Username
- Verify Code

Example

The following is an example of returned Error array

(0): 0~\<description of error\> \<\<\< see below for list of most common errors.

(1): MAG135;20130122 12:31:21-43 \<\< Tracking ID

(2): 21 \<\< Import Queue Number

(3): ------ Image Security for Filename: \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg

(4): ------ ParseServerShare: Input= \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg

(5): ------ ExtractFilePath : \\vhaiswclu4\User1\$\TestImages\\

(6): ------ Result \\Server\Share: \\vhaiswclu4\User1\$

(7): ------ Confirming UserName and Password...

(8): ------ Username: vhamaster\vhaiswIU Password Access1.

(9): ------ OSConnectToServer Start : 1/22/2013 12:32:35 PM

(10): ------ GetLastError: 1219 - Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again

(11): ------ Credential conflict, continuing as current User...

(12): ------ OSConnectToServer Success: 1/22/2013 12:32:35 PM

(13): ------ Success: Image Directory is accessible. \\vhaiswclu4\User1\$

(14): Error copying \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg

to Server : 30168~\\isw-kirin-lt\image1\$\GFB0\00\00\03\01\\GFB00000030168.JPG

(15): :File doesn't exist : \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg

(16): 1~VistA Image Entry deleted: 30168

(17): 1~Status Callback was called

The most common types of errors that will occur in the IAPI OCX are network connection errors and network read/write errors.

The exact errors that may occur at a site are unknown, but the most probable are listed below:

2 : The system cannot find the file specified

3 : The system cannot find the path specified

4 : The system cannot open the file

5 : Access is denied

8 : Not enough storage is available to process this command

12 : The access code is invalid

14 : Not enough storage is available to complete this operation

15 : The system cannot find the drive specified

19 : The media is write protected

20 : The system cannot find the device specified

21 : The device is not ready

25 : The drive cannot locate a specific area or track on the disk

26 : The specified disk or diskette cannot be accessed

29 : The system cannot write to the specified device

30 : The system cannot read from the specified device

31 : A device attached to the system is not functioning

32 : The process cannot access the file because it is being used by another process

33 : The process cannot access the file because another process has locked a portion of the file

36 : Too many files opened for sharing

39 : The disk is full

51 : Windows cannot find the network path. Verify that the network path is correct, and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator

52 : You were not connected because a duplicate name exists on the network. Go to System in Control Panel to change the computer name and try again

53 : The network path was not found

54 : The network is busy

57 : A network adapter hardware error occurred

59 : An unexpected network error occurred

64 : The specified network name is no longer available

65 : Network access is denied

67 : The network name cannot be found

70 : The remote server has been paused or is in the process of being started

71 : No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept

80 : The file exists

82 : The directory or file cannot be created

86 : The specified network password is not correct

88 : A write fault occurred on the network

89 : The system cannot start another process at this time Import API : System Error Codes

# Abstract/Thumbnail Maker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Application Description
- Setup
- Process Flow
- Logging

## Application Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The thumbnail maker (MagThumbnailMaker.exe) is the BP utility application that creates thumbnail/abstracts on the BP workstation. The thumbnail maker and another utility application, mag_makeabs.exe, work together to create thumbnails. The thumbnail maker uses AccuSoft ImageGear controls to create thumbnails. These are the same components used by VistA Imaging Capture to create thumbnails.

## Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MagThumbnailMaker.exe is installed into the …\VistA\Imaging\Backproc directory when the patch is installed. No other setup is needed.

The thumbnail maker can be started on its own but this is not necessary. The thumbnail maker will be started by the BP, as needed. Windows messages from mag_makeabs tell the utility which thumbnail to create.

When it is run, it will display as shown below. The BP user can decide to leave the thumbnail maker displayed, or it can be minimized to the taskbar. The size and position of the panels in the main window can be changed and the thumbnail maker can be minimized. The size, position and minimized state are saved, and will be maintained each time it is started. The last created abstract will be displayed in the image box. A list of the current abstracts it has created is maintained in the memo area.

A sample page of the new MagThumbnailMaker.exe is shown in the figure below:

![](vista-imaging-system-background-processor-user-manual/108.png)

### Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>File</p>
<p>Exit.</p></th>
<th>Closes the application.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Options</p>
<p>Clear memo</p>
<p>Create Log</p></td>
<td><p>The memo area of the display will be cleared.</p>
<p>A log file will be created for all activity.</p>
<p>Open Explorer window to the log directory:</p>
<p>C:\program files (x86)\vista\imaging\backproc\log\utility</p></td>
</tr>
<tr class="even">
<td><p>Help</p>
<p>About</p>
<p>Versions…</p></td>
<td><p>Displays the About Box for the application.</p>
<p>Clicking “Versions…” will display a message window that contains the versions and application date times of all BP and BP Utility applications.</p></td>
</tr>
</tbody>
</table>

An example of the Help \| Versions… path is given below:

![](vista-imaging-system-background-processor-user-manual/109.png)

## Process Flow 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process starts when the BP Queue Processor processes an Abstract queue.

BP Queue Processor

- Executes the mag_MakeAbs.exe program and sends the full path to the Image file and the name of the abstract file as command line parameters.
- Waits for the mag_makeabs process to terminate.

mag_MakeAbs.exe:

- Sends windows message to MagThumbnailMaker.exe
- Message contains reference to Full Image file, and name of thumbnail to create.

> MagThunbnailMaker.exe

- Creates the thumbnail from the Image file.
- Writes status of the operation to MagAbsError.txt file.
- Sends windows message to mag_MakeAbs.exe

> mag_MakeAbs.exe

- Receives windows message
- Terminates

> BP Queue Processor

- Gets notification that mag_makeabs has terminated.
- Reads the status of the abstract creation from MagAbsError.txt file

![](vista-imaging-system-background-processor-user-manual/110.png)

## Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the application is installed, logging is turned off. The logging mechanism of MagThumbmailMaker.exe is intended to be used when issues arise with the creation of thumbnails/abstracts.

The log messages produced from these two BP utility applications are:

- the date and time of the abstract request
- the success or failure
- the time the process ended

The main window of the application will display the last five Thumbnail attempts. If an error occurs, details of the error message are always saved to the Log File. To record all history of successful and failed abstracts, check the menu options ‘Create Log File’. To see the log, click the menu option: Options \>Open Log directory. The Log file is named ‘MagThumbLog.log’

> Also on the main window, the total number of successful and failed abstracts is displayed. The numbers include all abstract attempts since the Start Time of the MagThumbnailMaker application. The current TIER1 Share is also displayed.

![](vista-imaging-system-background-processor-user-manual/111.png)

### Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is an example log for one successful abstract:

> 05 14:42:21 - mma- Message sent: MAKETHUMBNAIL^7867678^\<Full FileName\> ^ \<Abstract FileName\>

> 05 14:42:21 - 03/05/15 14:42:21 DXP00000034156.ABS Success

> 05 14:42:21 - mma- Received message:THUMBNAILDONE^\<Abstract FileName\>

> 05 14:42:21 - mma- Terminating

> **NOTE:** “mma” is a code that means this message was logged from the mag_MakeAbs utility. Messages without “mma” were logged from the MagThumbnailMaker utility.

Logging is turned on or off by changing the DebugON setting in the MagThumbnailMaker.ini file.

Below is an example from MagThumbnailMaker.ini:

> \[SETTINGS\]

> DEBUGON=TRUE

> LogFileSizeKB=300

Set DebugON=TRUE to turn on logging.

The application handles maintenance of log files by deleting older log files. MagLogThumb\*.log files that are older than 24 hours are deleted.

#### Log File Format

MagLogThumb.log is the name of the current log file. When this file size is greater than LogFileSizeKB, it will be saved as a time stamped file. MagLogThumb is then cleared and reused. MagLogThumb.log is always the current log file.

Format: MagLogThumb yymmdd_hhmmss.log

![](vista-imaging-system-background-processor-user-manual/112.png)

## Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Imaging Thumbnail Maker examines the image file first. If the file is valid, image properties will be displayed. If the file is invalid, a detailed message will be displayed and the abstract will not be attempted. The detailed message will be returned to the BP giving support personnel a detailed reason why the abstract failed.

Imaging Thumbnail Maker

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Example of successful abstract creation:</p>
<p>Image Properties and the status of abstract creation are displayed.</p>
<p>![](vista-imaging-system-background-processor-user-manual/113.png)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Example failed abstract creation:</p>
<p>File access error message is displayed. Abstract not attempted.</p>
<p>![](vista-imaging-system-background-processor-user-manual/114.png)</p></td>
</tr>
<tr class="even">
<td><p>BP Failed Abstract Queue:</p>
<p>![](vista-imaging-system-background-processor-user-manual/115.png)</p></td>
</tr>
</tbody>
</table>

# Import OCX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Application Description
- Setup
- Process Flow
- Logging
- Log File Management
- Log File Format

## Application Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging Import API is an application developed to enable other VA and Non-VA applications to import documents and images into VistA Imaging without user interaction. The scope of that functionality is beyond the needs of this manual. The details of developing applications to interact with the Import API are contained in the VistA_Imaging_System_Import_API_Programmer_Guide.

This section will detail the interaction between the BP and one of the Import API components: the Import OCX.

Import OCX is an Active X component that is called by the BP to import Images into VistA Imaging. The BP calls the ImportQueue function of the OCX, passing the Import Queue number as a parameter. The BP will then wait for the OCX to process the import and return a result array. Details of the returned array are described in the troubleshooting section, 8.5 Import API.

## Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MagImportXControl1.ocx is installed into the …\VistA\Imaging\lib directory when the patch is installed. During install, the OCX is automatically registered using operating system (OS) Active X registration functions. For Win OS, this is the regsvr32.exe registration utility. No manual setup is needed.

## Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BP – Import OCX interaction

BP Queue Processor

- Calls the ImportQueue function of the Import OCX
- Waits for the return array

Import OCX

- Processes the Import Queue. Copies the imported image to the Image Network Tier2 storage defined for the site.
- Returns a result array with success or failure of the process.

BP Queue Processor

- Updates the status of the Import Queue in VistA Database
- If Import failed, the Import is re-queued up to three times.

All image copies are processed in a secondary thread. The main thread of the OCX maintains active communication to VistA while the secondary thread is processing the copy. This enables the connection to VistA to remain active even when the time it takes to copy an image is longer than the Kernel Broker connection timeout.

If the Kernel Broker connection to Vista is broken, the Import OCX silently re-connects to VistA.

If an import fails, the Import OCX returns a descriptive error message to the Background Processor. Imaging personnel can see why the import failed, and can take actions on all imports that failed for the same reason, at the same time. An example is given in the figure below:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Four imports were processed and failed. The error messages returned to the BP describes the cause of the error:</p>
<ul>
<li><p>FATAL Failed to connect. No Network</p></li>
<li><p>File Size Zero</p></li>
<li><p>File doesn’t Exist</p></li>
</ul></th>
<th>![](vista-imaging-system-background-processor-user-manual/116.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Import OCX is installed, logging is turned off. The logging mechanism of the Import OCX is intended to be used when import queues are failing.

The log messages produced from the import OCX include detailed history of all internal function calls of the OCX.

## Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages from the Import OCX have always been saved to the IMAGING WINDOWS SESSION File (#2006.82). Messages are saved after the process is finished.

8.  
9.  1.  
    2.  
    3.  
    4.  
    5.  

### Debug Modes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two debug modes that can be used by site personnel to debug failed imports.

1)  DebugON: This debug mode creates more detailed messages from the entire Import Process. Messages are saved to the IMAGING WINDOWS SESSION file (#2006.82); the detailed information will enable support personnel to determine the cause of the issue.
2)  DebugToLogFileON: This second debug mode saves debug messages to a log file on the BP local drive. Messages are saved to the log file as the process is running. If the application crashes or hangs, support personnel will be able to view the message history up to the time of the crash.

#### Registry Entries to Control Debugging

The default registry entries are created by the application. The registry path is:

HKEY_CURRENT_USER\software\vista\imaging\importOCX\debugoptions

The user can modify the registry entries to turn debugging on or off.

| Key              | Default Value                         | Description                                                                                                                                                                                               |
|------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DebugON          | FALSE                                 | If TRUE, then detailed log messages will be saved to IMAGING WINDOWS SESSION File in addition to normal messages.                                                                                         |
| DebugToLogFileON | FALSE                                 | If TRUE, then detailed log messages will be saved to the log file in real time.                                                                                                                           |
| LastDebugRunTime | \<empty\>                             | This is managed by the application. This is the date time when DebugON was set to TRUE. After 24 hours DebugON will be set to FALSE, and detailed logging to the IMAGING WINDOWS SESSION file is stopped. |
| LogFileDirectory | .…\vista\imaging\backproc\log\utility | This is set by application. Its purpose is purely informative so that users can know where the log files are created.                                                                                     |
| LogFileSizeKB    | 300                                   | Size of log file to be created. If the current log file is greater than this value, the new log file is started with date time stamp of “Now”. For example: MagOCX_150305_143158.log                      |

#### Debug Off

After 24 hours, DebugON will be set to FALSE and detailed log messages will no longer be saved to an IMAGING WINDOWS SESSION file.

## Log File Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log files are stored in the: \VistA\Imaging\backproc\log\utility folder.

The Import OCX manages the log files. When a file reaches the size limit, a new log file is created. Log files older than 24 hours are deleted from the folder. To store log files for future review, they will have to be moved to a different folder.

## Log File Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MagOCX\_\*.log is the format for Import OCX log files. The log file with the most current date/time is the active log file. When this file size is greater than LogFileSizeKB, a new log file is created with the current date/time in the following format: MagOCX_yymmdd_hhmmss.log. Files are stored in the \log\utility subdirectory of the Application Directory.

For an example, see the following figure:

![](vista-imaging-system-background-processor-user-manual/117.png)

# Broker Server Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BP communicates with the VistA database by using the VistA RPC Broker. The following steps briefly explain the installation of the RPC Broker Client Agent software. For more detailed information, see the *RPC Broker Installation Manual*.

1.  Log in to the workstation as an administrator, start the Registry editor (Start \> Run \> Regedit) and navigate to

> For 64-bit OS: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Vista\Broker\Servers

2.  Create a new string value (Edit \> New \> String Value) and use the remote server name and port number as the name of the value.

> Note: Separate the name and the port number with a comma.

64 bit OS

![](vista-imaging-system-background-processor-user-manual/118.png)

3.  Close the Registry Editor.
4.  If the server name is not resolved through DNS, open the HOSTS file (located in either WINNT\system32\drivers\etc. or WINDOWS\system32\drivers\etc.).
5.  Add a line to the file that includes the IP address and name of the remote site’s Broker server.

> \#HOSTS  
> 10.2.1.1 Washington  
> 10.2.1.2 Baltimore  
> \#END

6.  Save and close the HOSTS file.
7.  If you set up servers to connect to a server that can be resolved automatically through domain name server (DNS) (e.g. alpha3.yourva.gov), no entries are needed in the server’s HOSTS file.
8.  Reboot the server and run the Kernel Broker test program.

> RPCTest.exe is a test program distributed and installed on your PC in the C:\Program Files\VISTA\BROKER folder when the Kernel Broker Client Agent software is installed. When executed, it can be used to test the connection to the VistA System. This is valuable in troubleshooting problems with the VistA Imaging System. Please review the Kernel Broker documentation for more information and examples on the test application.

# File Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BP Processor can process the following file formats typically used in the VistA system.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Extension</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ABS</td>
<td>A graphics file used to contain abstract data. The file can normally be accessed through the VistA Imaging Clinical Display application.</td>
</tr>
<tr class="even">
<td>ASC</td>
<td>A text file containing text in ASCII code. The file can normally be accessed by most text editors on multiple platforms.</td>
</tr>
<tr class="odd">
<td>AVI</td>
<td>A video file containing compressed data and normally accessed by Windows-based applications.</td>
</tr>
<tr class="even">
<td>BIG</td>
<td>An image file containing full diagnostic resolution data normally accessed through the VistA Imaging Clinical Display application.</td>
</tr>
<tr class="odd">
<td>BMP</td>
<td>An image file containing an uncompressed bitmap of the image. The file is normally accessed through Windows-based applications.</td>
</tr>
<tr class="even">
<td>BW</td>
<td>An image file containing an uncompressed or compressed bitmap of the image. The images can be either monochrome or color and are generated by Silicon Graphics Inc equipment. The file can normally be accessed through the VistA Imaging Clinical Display application.</td>
</tr>
<tr class="odd">
<td>DCM</td>
<td>An image file created using the Digital Imaging and Communications in Medicine (DICOM) format. These files will normally contain both image data and metadata about the patient and the image. The file can be accessed on multiple platforms but can require the use of specialized readers to separate and properly display the image and the metadata.</td>
</tr>
<tr class="even">
<td>DOC</td>
<td>A text file containing data, formatting instructions and possibly some image data created by Microsoft Word, WordPerfect or WordStar applications. The file can be accessed by various word processor or text editor applications on multiple platforms.</td>
</tr>
<tr class="odd">
<td>HTM or HTML</td>
<td>A text file containing both data and Hyper Text Markup Language (HTML) which describes the structure of the data. HTML is usually a set of tags which describe structural information, such as text, paragraph or document formatting information. The file can be accessed through either numerous text editors or browser applications on multiple platforms. When displayed through a browser, the tag information will be used to format the data in the file.</td>
</tr>
<tr class="even">
<td>JPG or JPEG</td>
<td>An image file containing a compressed bitmap of the image. The degree of compression can be adjusted during file creation and is performed using algorithms developed by the Joint Photographic Experts Group. This format is a standard image format that can be accessed by numerous applications on multiple platforms.</td>
</tr>
<tr class="odd">
<td>MP3</td>
<td>An audio file containing encoded digital audio data based on the MPEG-1 Audio Layer 3 standard. The files will normally contain lossy compressed data and is a standard sound format that can be accessed by numerous applications on multiple platforms.</td>
</tr>
<tr class="even">
<td>MP4</td>
<td>A multimedia file containing encoded digital audio and video data based on the MPEG-4, part 14 standard. The files can be streamed over the internet and can be accessed by numerous applications on multiple platforms.</td>
</tr>
<tr class="odd">
<td>MPG or MPEG</td>
<td><p>A media file based on one of several encoding methodologies created by the Moving Pictures Experts Group. Some of the more common methodologies are:</p>
<p>• MPEG-1, or MP3, used for audio data</p>
<p>• MPEG-2 used for broadcast quality television</p>
<p>• MPEG-4, or MP4, used for video and computer graphics</p></td>
</tr>
<tr class="even">
<td>PAC</td>
<td>An image file used in earlier versions of VistA imaging similar to a TGA file. The file can normally be accessed through the VistA Imaging Clinical Display application. PACS files are files imported through the DICOM Gateway and shown by the Clinical Display workstation.</td>
</tr>
<tr class="odd">
<td>PDF</td>
<td>A document file containing document text, images, fonts and formatting information developed by Adobe. Once the document has been created it will retain its format and style across multiple applications and platforms. Numerous applications are available for viewing the file; however, a lesser number of applications are available for creating the file.</td>
</tr>
<tr class="even">
<td>RTF</td>
<td>A text file containing text and some formatting information developed by Microsoft. The file can normally be accessed by most word processors or text editors on multiple platforms.</td>
</tr>
<tr class="odd">
<td>TGA</td>
<td>An image file containing uncompressed or lossless compressed raster graphics data developed by Truevision. The file can be accessed through several paint applications on multiple platforms.</td>
</tr>
<tr class="even">
<td>TIF or TIFF</td>
<td>An image file containing an uncompressed or lossless compressed bitmap of the image. The degree of compression can be adjusted during file creation. This format is a standard image format that can be accessed by numerous applications on multiple platforms.</td>
</tr>
<tr class="odd">
<td>TXT</td>
<td>A text file containing data and very limited formatting instructions. The file can be accessed by all text editors and word processors on multiple platforms. Unless the TXT file is a designated primary or full Image source file it is necessary for TXT to be in the File Types array on the Image Site parameters. It will be purged when the Tier 1 folder it is in does not contain either a full or big file of the same file name.</td>
</tr>
<tr class="even">
<td>WAV</td>
<td>An audio file normally containing uncompressed waveform data. The file is normally used with Windows based audio applications.</td>
</tr>
</tbody>
</table>

# Verifier Integrity Samples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Text file is binary or unreadable

> ![](vista-imaging-system-background-processor-user-manual/119.png)

Text file

1.  Text file is ASCII, but has unprintable characters or is truncated.

> ![](vista-imaging-system-background-processor-user-manual/120.png)

Text file

1.  *Patients ID* (SSN) field in the text file does not match that in VistA.
- IEN for this sample is *1800*

> ![](vista-imaging-system-background-processor-user-manual/121.png)

Text file

> ![](vista-imaging-system-background-processor-user-manual/122.png)

VistA Global

1.  *SOP Instance UID* field in the text file does not match the one in VistA.

> ![](vista-imaging-system-background-processor-user-manual/123.png)

Text File

> ![](vista-imaging-system-background-processor-user-manual/124.png)

VistA Global

1.  *Study Instance UID* field in the text file does not match the one in VistA.

> ![](vista-imaging-system-background-processor-user-manual/125.png)

Text file

> ![](vista-imaging-system-background-processor-user-manual/126.png)

VistA Global (Note the *Study Instance UID* is found in the parent file.)

1.  *SOP* and/or *Study Instance UID* are/is blank in the text file..

![](vista-imaging-system-background-processor-user-manual/127.png)

Text file

1.  *Patients BIRTH DATE* in the top section (*DATA1*) of the text file does not match DICOM- 0010,0030 field in the bottom section (*DICOM DATA*).

> ![](vista-imaging-system-background-processor-user-manual/128.png)

Text file

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA</td>
<td>Acronym for Archive Appliance</td>
</tr>
<tr class="even">
<td>Abstract</td>
<td>A “thumbnail” version of an image, which requires less computer processing resources to display than the actual image. Abstract images typically have an *.abs extension. One of the queues of the BP queue processor is also called the ABSTRACT queue.</td>
</tr>
<tr class="odd">
<td>Aggregate</td>
<td>To gather together as into a single referenced location. The parent term “aggregate function” is triggered by any action that causes a portion of an image set to be copied to the current jukebox location. The aggregate function ensures that the entire image set is copied to the same location.</td>
</tr>
<tr class="even">
<td>Archive</td>
<td>Long-term storage of data or images. A jukebox is the most common archive type presently used at sites.</td>
</tr>
<tr class="odd">
<td>Archive Appliance</td>
<td>A brand of enterprise-level archival storage software.</td>
</tr>
<tr class="even">
<td>Auto Write update</td>
<td>Process that checks each Image share and designates the share with the most free space as the current write location. The check for space is done after 100 Writes to the share or after 20 minutes since the last check, whichever comes first.</td>
</tr>
<tr class="odd">
<td>BP</td>
<td>Acronym for the Background Processor in the VistA Imaging System.</td>
</tr>
<tr class="even">
<td>BPWS</td>
<td>Former term for a Background Processor Workstation, now called a Background Processor Server.</td>
</tr>
<tr class="odd">
<td>Cache</td>
<td>Short name for the arcane term VistA Magnetic Cache or VistA Imaging Cache, alternative terms for RAID and Tier 1. See <em>Raid</em>. Contrast with <em>Caché.</em></td>
</tr>
<tr class="even">
<td>Caché</td>
<td>Commercial product name of the software used to install and set up the VistA database. Contrast with <em>Cache</em>.</td>
</tr>
<tr class="odd">
<td>CBOC</td>
<td>Acronym for community-based outpatient clinic.</td>
</tr>
<tr class="even">
<td>Critical low message</td>
<td>Email to alert key personnel that free space on an Image share has fallen below the %Server Reserve watermark.</td>
</tr>
<tr class="odd">
<td>Current Queue pointer</td>
<td>Queue type specific database reference to the next file copy, create, or destroy request.</td>
</tr>
<tr class="even">
<td>Current Write location (CWL)</td>
<td>Reference to the network share where images and associated files are stored that are newly acquired or retrieved from Tier 2.</td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>Internal entry number (IEN) of a PATIENT file (#2) entry.</td>
</tr>
<tr class="even">
<td>DICOM</td>
<td>Acronym for Digital Imaging and Communications in Medicine, a protocol for sharing and viewing medical images. DICOM has traditionally been used for radiology images, and recently has been used for images in other specialties such as cardiology, dental, gastrointestinal endoscopy, and ophthalmology.</td>
</tr>
<tr class="odd">
<td>Directory hashing</td>
<td><p>Process of storing files in multiple subdirectories based on the filename, as follows:</p>
<p>If hashing is used, files are maintained in a 5-level deep subdirectory structure where no directory will contain more than 100 unique filenames with their various extensions.</p>
<p>If hashing is not used, files are placed and retrieved from the root directory of the share.</p>
<p>VistA Imaging recommends using hashing.</p></td>
</tr>
<tr class="even">
<td>EHR</td>
<td>Electronic Health Record</td>
</tr>
<tr class="odd">
<td>File</td>
<td>In the VistA database, the equivalent of a database table, as well as a file in the generic sense.</td>
</tr>
<tr class="even">
<td>File types</td>
<td><p>In VistA Imaging:</p>
<p>ABS = Abstract or thumbnail image file</p>
<p>BIG = Large image file that takes up a lot of storage space</p>
<p>FULL = Full size/full resolution image file</p>
<p>TXT = Site-specific installation or setting file</p></td>
</tr>
<tr class="odd">
<td>Hash</td>
<td>See <em>Directory Hashing</em>.</td>
</tr>
<tr class="even">
<td>HIS</td>
<td>Acronym for hospital information system, which is a comprehensive, integrated information system designed to manage a hospital’s administrative, financial and clinical information related to patient data (electronic patient records).</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Acronym for Internal Entry Number.</td>
</tr>
<tr class="even">
<td>IMAGE file</td>
<td>File in the VistA database that contains entries of images.</td>
</tr>
<tr class="odd">
<td>IMAGE AUDIT file</td>
<td>File in the VistA database that keeps a record of any image entries that were deleted or missing. Also, used by the Verifier to ensure that a file set exists at the location(s) specified.</td>
</tr>
<tr class="even">
<td>Image Set</td>
<td>Includes the FULL/ABS/TXT files and possibly the BIG file.</td>
</tr>
<tr class="odd">
<td>Imaging server</td>
<td>Server used to store the most recently acquired and accessed image files</td>
</tr>
<tr class="even">
<td>Internal Entry Number</td>
<td>Unique record number for a specific entry in a FileMan file. Depending on the context, IENs can serve as identifiers for an image set, a single site, or other unique records in files in the VistA database.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Acronym for Information Resources Management, the Imaging support staff at a VA hospital.</td>
</tr>
<tr class="even">
<td>Jukebox</td>
<td>Long-term storage device in VistA that holds multiple optical discs or platters and can load and unload them as needed. Also called Archive, and with version of the software it is now referred to as Tier 2.</td>
</tr>
<tr class="odd">
<td>Magnetic cache</td>
<td>Same term as Tier 1. See <em>Tier 1</em>.</td>
</tr>
<tr class="even">
<td>Namespace</td>
<td>First three characters of the 14-character name given to image files captured at a site. Each VHA facility has its own unique 3-character namespace.</td>
</tr>
<tr class="odd">
<td>Offline</td>
<td>VistA Imaging shares designation used to isolate shares from auto-write candidacy and the purge function.</td>
</tr>
<tr class="even">
<td>Online</td>
<td>Connected to, served by, or available through a system and especially a computer or telecommunications system (as the Internet).</td>
</tr>
<tr class="odd">
<td>PACS</td>
<td>Acronym for Picture Archiving and Communication System. If a site has integrated a commercially available PACS with VistA Imaging, images from that PACS are treated in a manner similar to images produced by modalities such as a CT or MR.</td>
</tr>
<tr class="even">
<td>Purge</td>
<td>One of the three applications in the Background Processor used to process the removal of files from Tier 1 shares when the last access date exceeds the age specification within the local site parameters. The purge process will not delete a file if it cannot locate a copy of that file on the archive. If such a file is detected, purge will create a JUKEBOX queue entry for that file. See also <em>Verifier</em> and <em>Queue Processor</em>.</td>
</tr>
<tr class="odd">
<td>Queue</td>
<td>A request by the VistA Imaging System to create, move, or delete a clinical image file for the purpose of system efficiency.</td>
</tr>
<tr class="even">
<td>Queue pointer</td>
<td>Database file reference to the next queue to be processed within the queue file.</td>
</tr>
<tr class="odd">
<td>Queue Processor</td>
<td>One of the three applications in the Background Processor used to handle requests by the VistA Imaging System to manage clinical Tier 1 files for the purpose of system efficiency. Managing the files involves processing multiple queues (tasks). See also <em>Verifier</em> and <em>Purge</em>.</td>
</tr>
<tr class="even">
<td>RAID or RAID shares</td>
<td><p>Acronym for Redundant Array of Inexpensive Disks, the primary storage area for recently acquired and recently accessed clinical images. Also, the term used to identify a specific type of Network Location defined using the Background Processor Queue Manager.</p>
<p>See Tier 1.</p></td>
</tr>
<tr class="odd">
<td>Referenced network files</td>
<td>Image Tier 1 pointers to the network locations of each of the file types stored within the VistA Imaging System.</td>
</tr>
<tr class="even">
<td>Routers</td>
<td>Specific type of Network Location defined using the Background Processor Queue Manager.</td>
</tr>
<tr class="odd">
<td>RPCs</td>
<td>Acronym for Remote Procedure Calls.</td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td>Short name for the VA Kernel RPC Broker, the Client-Server interface component. RPC Broker 1.1 is required for interfacing with the hospital database.</td>
</tr>
<tr class="odd">
<td>Site Parameters</td>
<td>A set of specifications that is configurable to meet the individual needs of each VistA Imaging System implementation.</td>
</tr>
<tr class="even">
<td>Tier 1</td>
<td>Primary storage shares where Images are first held at capture time and are available to Display applications; previously referred to as RAID.</td>
</tr>
<tr class="odd">
<td>Tier 2</td>
<td>Secondary storage, previously referred to as JUKEBOX, refers to the configured secondary storage shares.</td>
</tr>
<tr class="even">
<td>UNC</td>
<td>Universal Naming Convention indicated by the format <a href="file://SERVER/SHARENAME">\\SERVER\SHARENAME</a></td>
</tr>
<tr class="odd">
<td>Verifier</td>
<td>One of the three applications in the Background Processor used to validate the VistA Imaging network file references in the IMAGE file (#2005) and to consolidate files on Tier 2. See also <em>Purge</em> and <em>Queue Processor</em>.</td>
</tr>
<tr class="even">
<td>Veterans Health Information System Technology Architecture</td>
<td>VistA is built on a client-server architecture, which ties together workstations and personal computers with graphical user interfaces at Veterans Health Administration (VHA) facilities, as well as software developed by local medical facility staff.</td>
</tr>
<tr class="odd">
<td>VIC</td>
<td>Veteran ID card, one of several images that the IMPORT queue can import from external applications.</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Service Network(s)</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Acronym for Veterans Health Information System Technology Architecture.</td>
</tr>
<tr class="even">
<td>VistA Imaging Cache</td>
<td>Also called VistA Magnetic Cache, an alternative term for Tier 1. See <em>Tier 1</em>. Contrast with <em>Caché</em>.</td>
</tr>
<tr class="odd">
<td>VistA Imaging shares</td>
<td>Same as VistA Imaging Cache. Contrast with <em>Caché.</em></td>
</tr>
<tr class="even">
<td>Win32</td>
<td>The set Microsoft Windows operating systems internal function calls which support all operating system activity.</td>
</tr>
<tr class="odd">
<td>WORM</td>
<td>Acronym for Write Once Read Many.</td>
</tr>
<tr class="even">
<td>Write Once Read Many</td>
<td><p>Once written to the disc, data is only available for reading and cannot be altered. Tier 2 should be:</p>
<p>WORM-DG for Data General Jukeboxes under OpenNetware</p>
<p>WORM-PDT for Pegasus Jukeboxes</p>
<p>WORM-OTG for OTG Disk Extender</p>
<p><strong>Note</strong>: WORM-DG and WORM-PDT are for backward compatibility only.</p></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

%
% Free Space DICOM Messages · 25
% Server Reserve · 5, 35, 38, 83, 89, 117, 119, 140
% Tier 1 Reserve · 21
…
…508 Compliance · 95
A
ABS_VC_PTR · 108, 111
Abstract Files · 34
ABSTRACT queue · 13, 67
Access/Verify codes · 8, 140
Active parameter · 35, 36
Active queue list · 43
Active queue pointer · 43
Active queues · 94
Ad Hoc Enterprise Site Report · 79
Ad Hoc Image Site Usage message · 79
Alt JB Refs · 104
Annotation diagrams · 51
Annotation tool · 59
Application Process Failure message · 80
Applications of the BP Processor · 1
Archive Appliance · 139, 140
ASSOCIATED INSTITUTION field (#.04) · 80
Associated Institutions · 20
Auto option in BP Verifier · 102
Auto Purge · 35, 83
AUTO PURGE queue · 13
Auto Write Location Update · 21
Auto_RAID_Group_Purge message · 83
AutoRouter · 50
B
Background Processor
applications of · 1
features · 4
VistA Imaging, in · 2
What is? · 1
BackProc log file · 78
Bad JB Refs · 104
Bad VC Refs · 104
Big Files · 34
BIG_JB_PTR · 108, 111
BIG_VC_PTR · 109, 111
BP Server Monitor
configuring · 134
daily monitoring · 136
description · 133
email message sent · 87
monitoring the BP Purge · 138
monitoring the BP Queue Processor · 136
monitoring the BP Verifier · 137
scheduling · 134
BP Servers
adding · 10
assigning tasks · *12*
assigning tasks to · 43
configuring · 10
required for processing · 64
server properties · 14
BPError log file · 79
Broker failure · 140
C
Capture Keys, use · 23
Check Image Text · 102
Check text files · 39, 41
Clinical Association Report (AP) · 100, 101, 149
Compression/decompression · 55
Configuring
BP applications, overall guidelines · *17*
mail groups · 27
mail messages · *25*
site parameters · *18*
Conflicting AP & Image DFNs · 100
Conflicting GP and GO DFN · 100
Current_Write_PTR · 109, 111
CWL · 106
D
Delay Between Queue Processing, Patch 196 · 75
DELETE queue · 13, 71
Deleting queues · *See* Purging queues
DFN Mismatches in AP Image Mult · 101
DFN_1 · 112
DFN_2 · 112
DFNError log file · 112
Diagram Annotation tool · 59
Diagrams
annotation · 51
in Network Location Manager · 51
storage type · 59
DICOM Gateway
BP Server processing · 72
EVAL queue · 72
full and abstract files · 34
Interface Switch Update · 24
PAC files · 170
Write Location · 24
Domain, in adding mail groups · 29
E
EKG
in network location · 51
strips for viewing · 51
strips from local and remote MUSE servers · 57
where data is stored · 57
Email messages
Ad Hoc Image Site Usage · 79
Application process failure · 80
Auto_RAID_group_purge · 83
GCC Copy Error · 84
Get_Next_RAID_Group_failure · 84
Image Cache Critically Low · 84
Image_File_Size_Variance · 85
Imaging Integrity Check · 114
Imaging Site Verification Issue · 114
INSTALLATION · 85
listing · 79
Monthly Image Site Usage · 85
Photo ID Action · 86
Scheduled Purge Failure · 86
Scheduled RAID Group Advance Failure · 87
Scheduled Verifier Failure · 87
Site Report Task Was Restarted · 87
Verifier Scan Error log · 115
VI BP Eval Queue · 87
VI BP Queue Processor Failure · 88
Error_Level · 113
EVAL queue · 12, 72, 87, 133
EVAL, task in BP Server Monitor · 133
Excel spreadsheet · 77, 107, 126
Extensions on missing files · 97
F
F1 key for Help · 76
Failed image or entry · 47
Failed queue list · 43
Failed queues · 94
File types · 22, 169
Full files · 34
FULL_JB_PTR · 108, 111
FULL_VC_PTR · 108, 111
Functional flow of VistA Imaging · 2
G
GCC
Copy Error message · 84
Generic Carbon Copy field · 20
in Network Location Manager · 50
queue · 13, 71
queue for photo IDs · 63
window · 56
Generic carbon copy · *See* GCC
Get Next Raid Group Failure message · 84
GO DFN mismatches · 101
GP & GO AP Mismatch · 100
GP has no images · 100
GP Missing GO Ptr · 100
H
Hardware requirements · 7
Hash subdirectory · 50, 52, 53, 54, 55, 57, 105
Help, getting · 76
HTML files · 76, 77, 107
I
IEN
count tranversed in Purge · 125
for IMPORT queue · 93
for processing in Verifier · 97
image record currently being processed · 105
in NETWORK LOCATION file · 74
in Process Queue · 75
in record number in Network Location · 59
in Scheduled Verify · 14
in the NETWORK LOCATION file · 103, 104
integrity checks · 99
marked by Offline Image utility · 137
patient data integrity check · 97
range to set in Verifier · 102
record in Network Location · 52
record number in Network Location · 53, 55, 56, 57, 58
text file integrity check · 102
verifying · 98
verifying range · 137
verifying range copied to Image shares · 137
IMAGE AUDIT file
file integrity · 99
IMAGE AUDIT file (#2005.1)
duplicate image entries · 104
Full image · 105
No Archive log file · 109
Image Cache Critically Low message · 84
Image entry is structurally abnormal · 101
IMAGE file (#2005)
file integrity checking · 99
Full image · 105
patient integrity checking · 100, 101
running Verifier · 98
validating network file references · 177
Image File Size Variance message · *85*
Image_Class · 113
Image_IEN · 112
IMAGE_PTR · 110
IMAGING SITE PARAMETERS file (#2006.1) · 8, 80
Imaging Site Usage report · 87
IMPORT queue · 13, 69, 91
Import queue properties · 49
Import Queue Security · 20
IMPORT Queue Status report · 91
Installation · *See* the Background Processor Patch Description
INSTALLATION message · 85
Integrity
checks · 96
image file · *99*
patient · *100*
text file · *101*
Internal Entry Number · *See* IEN
Invalid Image Ptr to AP · 100
J
JB Big · 105
JB Full · 105
JB Path 1 · 106
JB Path 2 · 106
JB_ALT_1 · 109
JBTOHD queue · 13, 66
JUKEBOX
in Network Location Manager · 50
queue · 13, 70
Jukebox Write Location · 21
L
log directory, default · 15
Log files
BackProc · 78
BPError · 79
DFNError · 112
NoArchive · 109
Purge.html · 127
PurgeError.html · 128
Scan Log File · 108
ScanError · 110
specifying location and size on a BP Server · 14
M
MAG ENTERPRISE · 79
MAG SERVER · 79
MAG SYSTEM security key · 8, 9, 24, 29
MAG WINDOWS secondary menu option · 8, 24, 73
MAG WINDOWS security key · 9
MagBPSetup.exe · 7
Magbtm.exe · 7
MagDexter utility, description of · 6
MAGEVAL · 134
MAGFQ · 134
MagKat utility, description of · 6
MAGMIN · 134
MAGnH · 50
MagPurge.exe · 7
MAGQ BPMONITOR · 87, 134
MAGQ BPMONITOR menu option · 87
MagUtility utility, description of · 6
MagVerifier.exe · 7
Mail groups
adding members · 29
adding remote members · 29
configuring · 27
deleting members · 30
displaying lists of users · 28
domain · 29
guidelines for adding · 29
MAG SERVER · 79
MEMBERS REMOTE · 79
specifying properties · 30
Mail messages · 25
adding names · 26
configuring · 25
displaying lists of users · 26
fields descriptions · 27
notification intervals · 27
removing names · 26
transmission frequency · 27
MEMBERS REMOTE · 79
Memo · 113
Mismatches · 96
Missing files in Verifier · 97
Missing Group Objects · 101
Monthly Image Site Usage message · 85
MUSE
default site number · 23
locations on EKG tab · 57
remote GE Muse server · 51
server · 57
setting for site location · 20
site \# · 58
version \# · 58
N
Namespace · 20
NameSpace, multiple · 22
Network bandwidth · 7
Network configuration · 2
Network connection, troubleshooting · 139
Network Location Manager
adding a new network location · 60
configuring · 50
modifying properties · 61
window · 49
No AP entry Ptr · 101
No AP Mult Ptr · 100
No AP Ptr · 101
No Image Ptr in AP · 100
NoArchive log file · 109
Not enough process memory · 140
Not enough server cache · 140
Not enough write cache available · 140
O
operational status · 52, 54, 55, 56, 58, 59, 105
P
Package · 112
Package_IEN · 113
PACS UID · 102
PACS UID field \#60 · 102
PARENT DATA FILE file (#2005.03) · 101
Partition, queue · 48
Password, Windows · 24, 55
Patient ID · 102
Patient_Name_1 · 112
Patient_Name_2 · 112
Percent Server Reserve · 84, *See* % Server Reserve
Permissions
EXPORT share · 8
IMPORT share · 8
READ/WRITE on the domain acct · 8
READ/WRITE on the share/folder/file · 8
Photo ID Action message · 86
Photo IDs · 34, 56, 63, 86, 125
Physical reference · 52, 53, 55, 56, 57, 59, 103, 105
PLACE value · 80
pointer · *See* Queues
PREFET queue · 13, 67
Purge
Auto · 119
auto purge, running · 38
automatic · 36
date criteria, configuring · 37
description · 117
express · 119
express settings · 35
file types purged · 119
manual · 36, 120
processing, understanding · 117
queues · 46
result codes · 120
results output · 129
retention days, configuring · 35
retention times, guidelines for setting · 33
Scheduled · 120
scheduled and express, configuring · 36
scheduled settings · 35
scheduled, running · 37
setting parameters · 118
settings · 32
troubleshooting · 151
What is? · 1
Purge Error log file · 128
Purge Events Table · 120
Purge Factor · 35, 36, 38
Purge log file · 127
Purge queue by type entries · 93
Purge Rate · 36
Q
Queue Management by Type option · 72
Queue Manager
active/failed status counts · 43
description · 43
priority order · 43
window · 44
Queue Processor
description · 43, 64
setup guidelines · 64
starting the application · 73
tasking · 65
understanding processing · 72
What is? · 1
Queues
ABSTRACT · 67
accessing failed Import Queue properties · 49
active queue pointer · 43
assigning to BP Servers · *12*
concept of · 65
corrupted entry · 48
DELETE · 71
EVAL · 72
GCC · 71
IMPORT · 69
JBTOHD · 66
JUKEBOX · 70
PREFET · 67
purging · 46
re-queuing · 47
setting queue partition · 48
R
RAID Group Advance · 5
RAID Groups
advance settings · 41
automatic RAID Group advance · 5
current · 20
description · 4
guidelines for setting parameters · 42
guidelines on shares · 4
in Network Location Manager · 50
running the Scheduled RAID Group Advance · 42
setting parameters for RAID Group Advance · 42
Write Location · 20
Range · 102, 103
Rehabilitation Act of 1973 · 95
Reports · *See* Log File, Emails, and Screen-Generated Output
Re-queuing a failed image · 47
Re-queuing entries to be kept · 94
Retention Days DICOM Messages · 25
Retention Days HL7 – Modality Work Lists · 25
Retention days, configuring · 35
ROUTE.DIC · 50, 54
Router in Network Location Manager · 50
Routing rules file · 50
RPC Broker, configuring · 167
S
Scan · 102
Scan log file · 108
ScanError log file · 110
Scheduled Purge Failure message · 86, 128
Scheduled RAID Group Advance Failure · 87
Scheduled Verifier Failure message · 87
SCHEDULED VERIFIER task · 96
SCHEDULED VERIFY queue · 14
Screen-generated output
508 Compliance · 95
IMPORT Queue Status · 91
JBTOHD Report · 90
Purge Queue by Type entries · 93
Server Size · 89
Section 508 · 95
Security
Windows · 8
Security keys
MAG SYSTEM · 8, 9, 24
MAG WINDOWS · 9
Server Size, output · 89
Setting up your BP system · 7
Setup requirements · 8
Site
code · 20
configuring parameters · 18
name of remote location · 55
Site Report Task Was Restarted message · 87
Site usage report · 85
Software requirements · 7
SOP · 102
SOP Instance · 102
SSN_1 · 112
SSN_2 · 112
Status counts, active/failed · 43
Storage Type · 74
Study Instance UID · 102
T
Tape backup · 77
Tasks
ABSTRACT · 67
assigned as queues · 13
assigned to BP Servers · 64
DELETE · 71
EVAL · 72
GCC · 71
IMPORT · 69
JBTOHD · 66
JUKEBOX · 70
PREFET · 67
Timeout VistARad · 23
Timeout Windows Capture · 23
Timeout Windows Display · 23
Transmission frequency, mail messages · 27
Troubleshooting
broker failure · 140
general startup · 139
integrity messages on patient data · 149
network connection · 139
not enough process memory · 140
not enough server cache · 140
not enough write cache available · 140
output HTML messages · 147
Purge · 151
Verifier · 146
U
UID field · 102
UNC · 55, 56, 57, 59, 74
URLs · 51
in Network Location Manager · 51
storage type · 59
WEB service location · 59
window · 58
User Preference, default · 23
Username, Windows · 24, 55
V
Variance · 85
VC Abstract · 105
VC Big · 106
VC Full · 105
Verifier
description · 96
integrity checks · 99
integrity samples · 172
maintenance operations · 98
manual · 40
missing files · 97
processing · 97
reasons for running · 98
scheduled, guidelines for setting · 40
scheduling · 40
setting up · 96
settings · 39
starting · 102
tasking · 96
troubleshooting · 146
What is? · 1
VI BP Eval Queue message · 87
VI BP Queue Processor Failure message · 88
VistA Access · 24
VistA Imaging
functional flow · 2
VistA Verify · 24
VistARad Grouping · 20
W
Watermarking Failed message · 89
Watermarking Successful messsage · 88
WEB service · 58
Windows
BP Verifier · 102
Diagrams · 59
EKG · 57
Event Log · 78
GCC · 56
GO VistA Storage · 89
Imaging Site Parameters · 18
IMPORT Queue Status · 91
JBTOHD Report · 90
Jukebox · 53
Mail Groups · 28
Mail Message Manager · 25
Network Location Manager · 49
Purge / Verifier / RAID Groups · 32
Queue Management by Type · 93
Queue Manager · 44
Queue Processor application · 73
Routers · 54
URLs · 58
X
XTMP global · 93
