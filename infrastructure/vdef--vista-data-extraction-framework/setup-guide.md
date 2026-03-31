---
title: VDEF Version 1 Installation and User Configuration Guide
doc_type: CFG
doc_label: Configuration Guide
doc_layer: anchor
doc_subject: Installation and User
app_code: VDEF
app_name: VistA Data Extraction Framework
section: INF
app_status: active
pkg_ns: VDEF
patch_ver: 1
patch_id: VDEF*1
group_key: "VDEF:VDEF:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vdef
  - request
  - queue
  - status
  - table
  - contents
  - package
  - inactivate
  - activate
  - custodial
page_count: 0
word_count: 7777
section_count: 35
table_count: 20
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: December 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_0_installation_and_user_configuration_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_0_installation_and_user_configuration_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=144"
---

VistA Data Extraction Framework 1.0

Installation & User Configuration Guide

Document Revision 1.7

![](vdef-version-1-installation-and-user-configuration-guide/001.png)

VA Office of Information and Technology (OI&T)

Veterans Health Information Technology (VHIT)

VistA Messaging Services

(*This page left blank for two sided printing*)

Revision History

|                |          |                                                                                 |          |
|----------------|----------|---------------------------------------------------------------------------------|----------|
| Date           | Revision | Description                                                                     | Author   |
| December 2004  | 1.0      | Created document                                                                | REDACTED |
| January, 2006  | 1.1      | VDEF\*1.0\*3 - Documents false VDEF alerts and restarting VDEF queue processor. | REDACTED |
| October, 2007  | 1.2      | Technical Edit                                                                  | REDACTED |
| April 3, 2009  | 1.3      | Remove the residual information about HLO. (VDEF_CR8)                           | REDACTED |
| April 6 2009   | 1.4      | Reformatted document, accepted changes. (VDEF_CR8)                              | REDACTED |
| May 5, 2009    | 1.5      | Made changes per developer & SQA feedback. (VDEF_CR8)                           | REDACTED |
| July 23, 2009  | 1.6      | Made changes per developer & SQA feedback. (VDEF_CR8)                           | REDACTED |
| August 5, 2009 | 1.7      | Made changes per developer & SQA feedback. (VDEF_CR8)                           | REDACTED |
|                |          |                                                                                 |          |

(*This page left blank for two sided printing*)

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation and Configuration Overview](#installation-and-configuration-overview)
  - [Namespace](#namespace)
  - [File Range](#file-range)
  - [Routine Checksums](#routine-checksums)
  - [Globals](#globals)
  - [Estimated Time Taken by the Installation Process](#estimated-time-taken-by-the-installation-process)
  - [Required Patches](#required-patches)
- [VDEF Configuration](#vdef-configuration)
  - [Menu Setup](#menu-setup)
  - [Mail Group Setup](#mail-group-setup)
  - [Security Key Setup](#security-key-setup)
  - [Activating VDEF](#activating-vdef)
- [HL7 Components and Monitoring HL7 Processes](#hl7-components-and-monitoring-hl7-processes)
  - [Creating an HL7 Monitor View for VDEF](#creating-an-hl7-monitor-view-for-vdef)
  - [Setting Up VDEF’s Outbound Logical Links](#setting-up-vdefs-outbound-logical-links)
  - [Starting VISTA HL7 Logical Links](#starting-vista-hl7-logical-links)
- [VDEF Post-Installation Activities](#vdef-post-installation-activities)
  - [Modifying Scheduled Startup Options](#modifying-scheduled-startup-options)
  - [Setup within VISTA](#setup-within-vista)
  - [Activating a VDEF Requestor](#activating-a-vdef-requestor)
  - [Starting the VDEF Request Queue Processor](#starting-the-vdef-request-queue-processor)
  - [Activating VDEF Custodial Packages](#activating-vdef-custodial-packages)
  - [Activating the Applications’ VDEF Event APIs](#activating-the-applications-vdef-event-apis)
  - [Display the Status of VDEF](#display-the-status-of-vdef)
- [Shutting Down VDEF](#shutting-down-vdef)
  - [Controlling Which Requests VDEF Will Accept](#controlling-which-requests-vdef-will-accept)
  - [Inactivate a Requestor](#inactivate-a-requestor)
  - [Inactivating a Specific Custodial Application](#inactivating-a-specific-custodial-application)
  - [Inactivating a Single VDEF API Event](#inactivating-a-single-vdef-api-event)
  - [Controlling Whether VDEF Will Process Queued Up Requests](#controlling-whether-vdef-will-process-queued-up-requests)
  - [Suspend a Request Queue Processor](#suspend-a-request-queue-processor)
- [Troubleshooting](#troubleshooting)
  - [VDEF Error Conditions](#vdef-error-conditions)
  - [Checked Out Status](#checked-out-status)
  - [Errored Out Status](#errored-out-status)
  - [Documenting the Error](#documenting-the-error)
  - [Identify IENs of the Checked Out or Errored Out Records](#identify-iens-of-the-checked-out-or-errored-out-records)
  - [Deleting the Records](#deleting-the-records)
- [Appendix A: KIDS Installation Example](#appendix-a-kids-installation-example)
- [Appendix B: VDEF Configuration Menu Options](#appendix-b-vdef-configuration-menu-options)
- [Appendix C: VDEF Alert Messages](#appendix-c-vdef-alert-messages)
VistA Data Extraction Framework (VDEF) is a VistA package that uses hard-coded MUMPS (M) routines to create and deliver Health Level 7 (HL7) messages. The hard-coded programs are M programs belonging to an application’s namespace. The VDEF package supports queuing requests for messages, control of the timing of message creation, monitoring of the request queue, and recording of errors encountered during message creation. Messages are delivered using the VistA HL7 package.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VDEF\*1.0\*3

## Installation and Configuration Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF installation process uses the Department of Veterans Affairs (VA) Kernel Installation and Distribution System (KIDS) utility to install all routines, globals, and FileMan dictionary references. The following KIDS builds will be installed as part of the VDEF installation: VDEF 1.0. Appendix A contains a capture of a typical install.

> **NOTE:** Per VHA Directive 2004-038, this package should not be modified after installation.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF package has been assigned “VDEF” as its namespace.

## File Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VDEF File Range: 577, 577.4 and 579.1-579.99

## Routine Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VDEFCONT 37180716  
VDEFEL 3669561  
VDEFMNU 46511830  
VDEFMNU1 5498404  
VDEFQM 73176538  
VDEFREQ 32859660  
VDEFREQ1 6429409  
VDEFUTIL 20545927  
VDEFVU 22556922  
VDEFKIDS 14851717  
VDEFMON 8239134

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF package introduces one new global: VDEFHL7. This global is created when loading as a virgin install and should be defined with the following access privileges: RWD for System, World, Group, and User Class Identifier (UCI), using %GLOMAN for Digital Standard MUMPS (DSM) and ^PROTECT for CACHE.

VDEFHL7 should be journaled and placed in a location (database in Cache) where its expected growth will not affect system operations. The original size of the VDEFHL7 global is under 1MB, but depending on the volume of clinical activity within the VistA system and on the VDEF configuration parameters set up by Information Resource Management (IRM) staff, it is estimated that the size of VDEFHL7 may fluctuate between 1Mb and 500Mb.

## Estimated Time Taken by the Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the hardware installed at each site, the VDEF installation process is estimated to take less than three minutes.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Applications</strong></th>
<th><strong>Minimum Version Number</strong></th>
<th><strong>Required Patches</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td>8.0</td>
<td><p>257 SEQ #234</p>
<p>399 SEQ 2</p></td>
</tr>
<tr class="even">
<td>FileMan</td>
<td>22.0</td>
<td>105 SEQ #111</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>8.0</td>
<td>13 SEQ #13</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>1.6</td>
<td>98 SEQ #85</td>
</tr>
</tbody>
</table>

# VDEF Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows the menu options that are included with this build. The option name is shown first, followed by the Menu Text of the option as it is displayed in the Menu System.

The appropriate IRM staff will need to be assigned to the VDEF CONFIGURATION MENU, and it is recommended that this menu be added to the Systems Manager menu (EVE). IRM staff may decide to add one or more of the VDEF options as a secondary menu option on selected users’ menus.

|                                 |                                            |
|---------------------------------|--------------------------------------------|
| Option Name                 | Menu Text                              |
| VDEF Activate/Inac Requestor    | Activate/Inactivate Requestor              |
| VDEF Configuration Menu         | VDEF Configuration And Status              |
| VDEF Custodial Package          | VDEF Custodial Package Activate/Inactivate |
| VDEF Request Processor Schedule | Request Processor Schedule                 |
| VDEF Request Queue Parameters   | Request Queue Parameters                   |
| VDEF Startup Option             | VDEF Startup Option                        |
| VDEF Site-Wide Parameters       | Site-Wide Parameters                       |
| VDEF Status                     | Status Of VDEF Components                  |
| VDEF Suspend/Run Request Queue  | Suspend/Run Request Queue                  |
| VDEF Event API                  | VDEF Event API Activate/Inactivate         |

## Mail Group Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All alerts generated by VDEF will be routed to the VDEF NATIONAL ALERTS mail group using the Application VDEF ALERTS. IRM staff should edit this Mail Group to make sure that the appropriate local IRM staff is included in the Mail Group. A MailMan message containing the text of the alert is also sent to the VDEF developer on FORUM and Outlook.

## Security Key Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new security keys have been added with this build.

## Activating VDEF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several steps involved in activating VDEF once it has been installed before any data will flow from an application trigger event through VDEF and the HL7 package and out to the local Interface Engine (IE). These steps are:

1.  Configuring and starting the VDEF HL7 logical links: This step establishes the TCP connection between VistA and the local Interface Engine using the VDEF links. (§ 3.3)
2.  Activating the VDEF Requestor: This step turns on the basic VDEF process that accepts a request from an application trigger event and stores it in the VDEF queue. If the VDEF Requestor is inactive, <u>no requests from any application will be saved in the VDEF Request Queue</u>. NOTE: In addition, for a request to be stored in the VDEF Request Queue, the Custodial Package and VDEF Event API associated with the application’s trigger must be activated. (§ 4.3)
3.  Starting the VDEF Request Queue Processor: This step turns on the process that allows VDEF to remove a record from the VDEF Request Queue and create and send a message to the VistA HL7 logical link associated with the message. (§ 4.4)
4.  Activating the Custodial Packages: Each application’s trigger software (not part of the VDEF install) is associated with a Custodial Package. In order for VDEF to save requests from an application, its Custodial Package must be activated in VDEF. (§ 4.5)
5.  Activating the VDEF Event APIs: Each application’s trigger software (not part of the VDEF install) is associated with a specific type of HL7 message. In order for VDEF to save requests for a message type, its VDEF Event API must be activated in VDEF. (§ 4.6)
6.  Defining the correct HL7 package for VDEF Events: Each VDEF Event must be set up to use VistA HL7 packages - HL7 engine HL7 1.6.

| WARNING | No messages will flow out of VDEF to the local interface engine until ALL the above steps have been completed. |
|-------------|----------------------------------------------------------------------------------------------------------------|

# HL7 Components and Monitoring HL7 Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are new HL7 Logical Links distributed as part of the VDEF package. The outbound links to the local VistA Interface Engine are named VDEFVIEn or, possibly in the future, VDEFVIEnn (where n is a number). Currently there are four links distributed with VDEF. They are VDEFVIE1, VDEFVIE2, VDEFVIE3, and VDEFVIE4. At this time, the link VDEFVIE4 is used exclusively by lab messages but lab DOES NOT use the VDEF processor to create the messages. Lab messages are created within the lab system and sent to HDR using the VDEFVIE4 link.

The HL7 Application and Protocol definitions that are used by the links are distributed with the custodial package-specific VDEF builds separately from the VDEF build. There are no HL7 Applications or Protocols distributed with the VDEF build.

## Creating an HL7 Monitor View for VDEF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to better monitor VDEF messaging in the VistA HL7 System Link Monitor (menu option HL MESSAGE MONITOR), you will want to define a new “view.” You can do so via the menu option EDIT HL7 SITE PARAMETERS by adding a new view called “VDEF.” Move the cursor to the “System Link Monitor VIEWS” field and enter “VDEF.” You will be asked if you are adding “VDEF” as a “new LINK MONITOR VIEWS.” Answer “YES” and you will be placed in a new sub-window.

Edit HL7 Site Parameters Page 1 of 2

-----------------------------------------------------------------------------

Current Domain: \<your site information\>

Current Institution: \<your institution name\>

Is this a Production or Test Account? Production

Mail Group for Alerts: HL7 TRANS

System Link Monitor VIEWS

-------------------------

VDEF

\[Goto next page to edit Background Process Parameters\]

------------------------------------------------------------------------------

In the “LOGICAL LINK” column, type “VDEFVIE1” and press Enter. In the “DISPLAY ORDER” column, enter “1” and press Enter. Repeat these steps for links VDEFVIE2 through VDEFVIEn, incrementing the DISPLAY ORDER value by one for each additional link. Close the window and save the data.

System Link Monitor View

NAME: VDEF

LOGICAL LINK DISPLAY ORDER

------------ -------------

VDEFVIE1 1

VDEFVIE2 2

VDEFVIE3 3

You can now use this view when monitoring HL7 traffic in the HL MESSAGE MONITOR menu option. When presented with a list of VistA HL7 links defined at your site, press “V” and when prompted to “Select LINK MONITOR VIEWS,” enter “VDEF.” At that point you will only see the VDEF-specific logical links: VDEFVIE1 through VDEFVIEn.

## Setting Up VDEF’s Outbound Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the EVE menu, a user can access the HL7 Main Menu by following the screen shots below.

Core Applications ...

Device Management ...

FM VA FileMan ...

Manage Mailman ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

TaskMan Management ...

User Management ...

CPTI CPT Inquiry

KEYS Options with Keys (Local FM)

Application Utilities ...

Capacity Management ...

HL7 Main Menu ...

Local SPD Equipment Tracking Menu ...

NCP VMS OPTION

Non-Core applications drivers ...

RUM Manager Menu ...

> Select Systems Manager Menu Option:

Enter HL7

> HL7 Main Menu

> Event monitoring menu ...

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option:

> Enter FILER

> SM Systems Link Monitor

> FM Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

> Select Filer and Link Management Options Option:

> Enter ED

> Select HL LOGICAL LINK NODE:

> Enter VDEFVIE1

This example shows the setup screens for one of the outbound VDEF links connected to the local BusinessWare IE.

All of the VDEFVIEn links need to be modified to match site-specific parameters. Using the menu option HL EDIT LOGICAL LINKS, select Logical Link VDEFVIE1. On the first screen, change AUTOSTART to Enabled. Next, move the cursor to the field LLP TYPE and press Enter. This will present the second screen.

First screen:

HL7 LOGICAL LINK

-----------------------------------------------------------------------------

NODE: VDEFVIE1

INSTITUTION:

DOMAIN:

AUTOSTART: ENABLED

QUEUE SIZE: 10

LLP TYPE: TCP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

In the TCP LOWER LEVEL PARAMETERS screen, you will need to change the value of the “TCP/IP ADDRESS” parameter on the HL7 LOGICAL LINK TCP LOWER LEVEL PARAMETERS sub-screen to the Internet Protocol (IP) address of the local interface engine at your site. The address will be provided by your site’s IE Manager. The links are sent with the default settings shown below. These settings should be correct for your site. However, you will need to add the TCP/IP port number. Get the correct value from your site’s IE manager.

Second Screen:

HL7 LOGICAL LINK

-----------------------------------------------------------------------------

TCP LOWER LEVEL PARAMETERS

VDEFVIE1

TCP/IP SERVICE TYPE: CLIENT (SENDER)

TCP/IP ADDRESS: <u>\<IP address of local IE\></u>

TCP/IP PORT: 5561

ACK TIMEOUT: RE-TRANSMISION ATTEMPTS:

READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: restart

BLOCK SIZE: SAY HELO:

STARTUP NODE: PERSISTENT: NO

RETENTION: 15 UNI-DIRECTIONAL WAIT:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

File the changes to the link.

After you have filed the changes for VDEFVIE1, repeat the same changes for logical links VDEFVIE2 and VDEFVIE3.

To view the current status of the links, from the Filer and Link Management Options HL7 Menu:

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Enter “SM” Systems Link Monitor. You will see a screen that looks like this:

SYSTEM LINK MONITOR for \<your site name\>

MESSAGES MESSAGES MESSAGES MESSAGES DEVICE  
NODE RECEIVED PROCESSED TO SEND SENT TYPE STATE

\<link name\> 12293 12293 12636 12636 MM Halting

Incoming filers running =\> Zero TaskMan running

Outgoing filers running =\> Zero \*\*\*LINK MANAGER NOT RUNNING!!!\*\*\*

Monitor DOWN

Select a Command:

(N)EXT (B)ACKUP (A)LL LINKS (S)CREENED (V)IEWS (Q)UIT (?) HELP: V

Enter “V” at the HELP prompt. At the Select LINK MONITOR VIEWS prompt, select VDEF.

You will see a screen that looks like this:

SYSTEM LINK MONITOR for CHEYENNE, WY (T System)

MESSAGES MESSAGES MESSAGES MESSAGES DEVICE

NODE RECEIVED PROCESSED TO SEND SENT TYPE STATE

VDEFVIE1 0 0 7 0 NC Shutdown

VDEFVIE2 Shutdown

VDEFVIE3 Shutdown

Incoming filers running =\> Zero TaskMan running

Outgoing filers running =\> Zero \*\*LINK MANAGER NOT RUNNING!!!\*\*

Monitor DOWN

Select a Command:

(N)EXT (B)ACKUP (A)LL LINKS (S)CREENED (V)IEWS (Q)UIT (?) HELP:

## Starting V*IST*A HL7 Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before data can be transmitted over the VDEFVIEn logical links, the link definitions should be edited. Ensure that you have configured the link definitions as described above (§ 3.2).

| WARNING | Before turning on the VDEFVIEn logical links, ensure that you have correctly and completely defined to all the HL7 components and parameters for each VDEF Event and logical link. Instructions are described in this section. |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

At this point you may turn on the new VDEFVIEn logical links by using the menu option Start/Stop Links \[HL START\] and starting them in “B”ackground mode. Ensure that the VistA HL7 Link Manager is running, because VDEF messaging will not be able to take place without it. The current status of the Link Manager can be checked and started if necessary by accessing the menu option HL START/STOP LINK MANAGER.

| WARNING | Please be advised that the volume of HL7 traffic over these links depends on the number of daily updates to the VistA clinical information at your site and can be significant at larger sites. You may want to monitor the links closely the first few days after the installation and purge HL7 log data as appropriate per your standard HL7 monitoring and purging procedures. |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# VDEF Post-Installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modifying Scheduled Startup Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new queueable option, VDEF STARTUP, was released as part the VDEF build. IRM staff must add it to the list of Scheduled Startup Options in TaskMan before VDEF can become fully functional. To do this, access menu XUTM SCHEDULE on the TaskMan Management menu and select the VDEF STARTUP option. In the first field, QUEUED TO RUN AT WHAT TIME, enter the current date and time + 5 minutes because the time must be in the future. In the fourth field, RESCHEDULING FREQUENCY, enter “300S” (300 seconds). Do not enter “5M” because that is 5 MONTHS. In the last field on the screen, SPECIAL QUEUING, enter “SP” (startup persistent) as the field’s value, and file the data.

Edit Option Schedule

Option Name: VDEF STARTUP OPTION

Menu Text: VDEF STARTUP OPTION TASK ID: 6286886

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: \<Current data & time + 5 minutes\>

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 300S

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

Once the KIDS builds have been successfully installed and VDEF STARTUP option has been added to the list of Scheduled Startup Options in TaskMan, VDEF will be ready to be configured.

See Appendix B for detailed full-screen examples of all the VDEF Configuration Options.

## Setup within VISTA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows users to make various changes to VDEF settings.

To configure VDEF within the VistA application, IRM staff will need to select the menu option VDEF Site-Wide Parameters on the VDEF Configuration and Status menu and set up its parameters as follows:

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option: SITE Site-Wide Parameters

VDEF SYSTEM: \<your site specific information\>// \<accept default\>

VDEF MONITOR DELAY: 5M// \<accept default\>

At this point, VDEF has been configured <u>but not activated.</u> Site management will need to decide when to activate it.

## Activating a VDEF Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows activating or inactivating of the <u>MAIN</u> VDEF process that receives requests from the internal VistA API calls and places them in the VDEF Request Queue.

Once the decision to turn on VDEF messaging has been made, IRM staff will need to go into the VDEF Configuration and Status menu and select option VDEF Activate/Inactivate Requestor. IRM staff will select a defined Requestor, which currently is “MAINTENANCE,” and change its status from “I”nactive to “A”ctive.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter ActR Activate/Inactivate Requestor

Select Requestor:

Enter MAINTENANCE

> **NOTE:** Inactivating a requestor has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests made while the requestor is inactive will be PERMANENTLY lost. Make sure you really want to turn it off.

REQUESTOR ACTIVATION FLAG: INACTIVE//

Enter A(ctive)

## Starting the VDEF Request Queue Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option allows starting and stopping of the VDEF process that selects records from the VDEF Request Queue and creates outgoing HL7 messages.

Next, IRM staff will select the menu option VDEF Suspend/Run Request Queue and change the value of the SUSPENDED FLAG field for the defined VDEF Request Queues (at this time “MAINTENANCE”) from “S”USPENDED to “R”UNNING.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter SUSR Suspend/Run Request Queue

Select Request Queue:

Enter MAINTENANCE

SUSPENDED FLAG: SUSPENDED//

Enter R(unning)

## Activating VDEF Custodial Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the applications that send requests to VDEF belong to a custodial package (Lab, Adverse Reactions, and Outpatient Pharmacy, for example). This option gives users control over which custodial packages are allowed to queue up requests in VDEF. If a custodial package is turned off, the request will be ignored. If a package is turned on and the associated VDEF Event API is activated, the request will be placed into the VDEF Request Queue.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter CUST VDEF Custodial Package Activate/Inactivate

Select Custodial Package: \<Enter name of package\>

(Enter “?” FOR A LIST OF CUSTODIAL PACKAGES CURRENTLY IN VDEF)

Warning Notice: Inactivating a custodial package has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests for HL7 messages associated with this custodial package made while the package is inactivated will be PERMANENTLY lost. Make sure you really want to turn this custodial package off.

ACTIVATION STATUS: INACTIVE//

Enter A(ctive)

| WARNING | While activating a custodial package is a normal part of the initial set up of VDEF, inactivating custodial packages in VDEF is not part of the normal routine. You should inactivate a custodial package only if directed to do so. |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Activating the Applications’ VDEF Event APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the custodial package applications that send requests to VDEF have their trigger events associated with specific message types.

For example, the custodial package Adverse Reaction (Allergies) has three different types of messages. Each event is referred to here as a *VDEF API Event*. This option gives users control over which VDEF API Events are allowed to queue up requests in VDEF. If a VDEF Event API is turned off, the request will be ignored. When an Event is turned on, the request will be placed into the VDEF Request Queue.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter API VDEF Event API Activate/Inactivate

Select VDEF API Event:

Enter “?” for a list of VDEF API Events

ORU-R01-VTLS PATIENT VITALS Status: ACTIVEPkg: GEN. MED. REC. - VITALS

API EVENT ACTIVE FLAG: INACTIVE//

Enter A(ctive)

| WARNING | This is for example only. Inactivating VDEF Event APIs is not part of the normal setup. Do this only if directed to do so. |
|-------------|----------------------------------------------------------------------------------------------------------------------------|

## Display the Status of VDEF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the screen showing the current VDEF parameters, as well as the current status of the VDEF Queues.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter STAT Status of VDEF components.

You will see the following display. This example represents VDEF in a typical state after it has been activated but before any requests have been sent to it.

VDEF Status - DEC 28, 2005@10:47:50

Logical Link Status

VDEFVIE1: running task \#6274200

VDEFVIE2: stopped or caught up

VDEFVIE3: running task \#6281503

Requestor Status

MAINTENANCE: Activated Dest.: VISTA HL7 Req. Queue: MAINTENANCE

Request Processor Status

MAINTENANCE: Running

Current Task \# \[Proc\]: 6257283 \[20B4BBD4\] Task status: Active-Running

Requests waiting for purge: 53832 Last request#: 1441722

Checked Out(0) Queued Up(8) Errored Out(0)

Hit \<return/enter\> to continue or '^' to terminate:

The Logical Link Status shows the logical links (and their status) that are defined for VDEF. If a link is sending messages, the display will show the TaskMan task number. The Requestor Status will show as either Inactivated or Activated. The Dest.: (message destination) will always show VistA HL7. The Req. Queue: with the initial release will show MAINTENANCE. The Request Processor Status will show the name of the process (MAINTENANCE in the example) and its status, “running” or “Suspended.” The counts show:

- Requests waiting for purge: The total number of records in the VDEF Request Queue for all statuses but primarily the number of processed requests that are waiting to be purged.
- Checked Out: The number of requests that are in the state of being processed
- Queued Up: The number of unprocessed requests that are in the Request Queue
- Errored Out: The number of requests that VDEF attempted to process but was unable to because of a non-fatal error condition.

Note that the highest value you will ever see in the ”Checked Out” and “Errored Out” counters is “\>100”. The highest value you will see in the “Queued Up” counter is \>1000.

If there are unprocessed requests in the Request Queue and the Request Processor is running, the Checked Out count will normally remain at one and not go back to zero until all the Queued Up requests are processed.

If there are no unprocessed requests (Queued Up count is at zero) but the Checked Out count is 1 or greater, VDEF encountered a fatal M error.

If there are no unprocessed requests (Queued Up count is at zero) but the Errored Out count is 1 or greater, VDEF encountered a non-fatal error.

| WARNING | If VDEF is not able to send an HL7 message to the IE, the reason must be investigated. See section 6 for troubleshooting this situation. |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|

# Shutting Down VDEF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Appendix B for detailed full-screen examples of all the VDEF Configuration Menu Options.

If a decision is made to turn off VDEF messaging, IRM staff will need to access the VDEF Configuration and Status menu and select the appropriate options. Note that there may be different reasons for shutting down VDEF, and depending on the reason, there can be different actions that IRM staff can take.

If there is an emergency situation due to system resources that necessitates a quick shutdown of VDEF, here are some suggestions. Suspending the VDEF Request Queue is the fastest way to stop VDEF building and sending messages, which is the VDEF activity that accounts for most of the VDEF-related system overhead.

| WARNING | Unless it is an emergency, do not suspend the VDEF Request Queue until all current events have been processed through the system, which is indicated by the Queued Up count on the VDEF Status Display being at zero. |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

There are two types of control the IRM has over VDEF:

1.  Controlling which requests VDEF will accept and queue up, and
2.  Controlling whether VDEF processes the requests that do queue up.

## Controlling Which Requests VDEF Will Accept

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control over which requests VDEF will or will not add to the VDEF Request Queue occurs at several levels as shown here from most to least:

VDEF Requestor: Allows/disallows ALL application trigger events to be eligible to be queued/not queued by VDEF for that Requestor. Whether a request is actually queued up in VDEF depends on the Custodial Package and VDEF Event API settings also.

Custodial Package: Allows/disallows only application trigger events that belong to that custodial package to be queued/not queued by VDEF for that package. An example would be the Adverse Reaction package, which currently has three different API Event messages, Allergy update, Adverse Reaction report, and Allergy assessment. Turning off the Adverse Reaction custodial package will prevent requests from ALL three messages from being queued in VDEF.

VDEF Event API: Allows/disallows application trigger events for a single specific type of message. An example would be the Adverse Reaction package, which currently has three different API Event messages, Allergy update, Adverse Reaction report, and Allergy assessment. You can inactivate one of the Adverse Reaction events without inactivating the other two.

## Inactivate a Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you inactivate a Requestor, you set that Requestor in a state where it will not accept any requests from any application maintenance trigger event. This does not stop the processing of requests that have already been received and queued up in the VDEF Request Queue. It will only prevent new requests from being added to the VDEF Request Queue.

From the main VDEF Configuration Menu, select VDEF Activate/Inactivate Requestor. IRM staff will select a defined Requestor, which currently is “MAINTENANCE,” and change its status from “A”ctive to “I”nactive.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter ActR Activate/Inactivate Requestor

Select Requestor:

Enter MAINTENANCE

> **NOTE:** Inactivating a requestor has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests made while the requestor is inactive will be PERMANENTLY lost. Make sure you really want to turn it off.

REQUESTOR ACTIVATION FLAG: ACTIVE//

Enter I\<nactive\>

## Inactivating a Specific Custodial Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows IRM staff to control which custodial packages are allowed to queue up requests in VDEF. If a custodial package is turned off, the request will be ignored. Stopping the queuing of requests from one custodial package does not stop requests from any other custodial package from being added to the VDEF Request Queue. Inactivating a Custodial Package will stop all the API Events that belong to that package from being added to the VDEF Request Queue.

From the main VDEF Configuration Menu, select the menu option VDEF CUSTODIAL PACKAGE ACTIVATE/INACTIVATE and change the value of the package from “A”ctive to “I”nactive.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter CUST VDEF Custodial Package Activate/Inactivate

Select Custodial Package:

Enter “?” FOR A LIST OF CUSTODIAL PACKAGES

Warning Notice: Inactivating a custodial package has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests for HL7 messages associated with this custodial package made while the package is inactivated will be PERMANENTLY lost. Make sure you really want to turn this custodial package off.

ACTIVATION STATUS: ACTIVE//

ENTER I\<nactive\>

## Inactivating a Single VDEF API Event

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gives IRM staff control over which individual API Events are allowed to queue up requests in VDEF. If an API Event is turned off, the request will be ignored. Stopping the queuing of requests from one API Event does not stop requests from any other API Event from being added to the VDEF Request Queue.

From the main VDEF Configuration Menu, select the menu option VDEF EVENT API ACTIVATE/INACTIVATE and change the value of the event flag from “A”ctive to “I”nactive.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter API VDEF Event API Activate/Inactivate

Select VDEF API Event:

Enter “?” for a list of VDEF API Events

ORU-R01-VTLS PATIENT VITALS Status: ACTIVEPkg: GEN. MED. REC. - VITALS

API EVENT ACTIVE FLAG: ACTIVE//

Enter I\<nactive\>

| WARNING | The simplest way to completely turn off VDEF is to Inactivate the Requestor and Suspend the Request Queue processor. |
|-------------|----------------------------------------------------------------------------------------------------------------------|

## Controlling Whether VDEF Will Process Queued Up Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inactivating a Requestor will not stop the processing of requests that have already been placed in the VDEF Request Queue. This is the VDEF process that uses more system resources than the queuing process.

## Suspend a Request Queue Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you suspend a Request Queue, you are stopping the process where VDEF processes the requests that are already in the VDEF Request Queue and generates the corresponding message for that request. This will not prevent new requests from being added to the VDEF Request Queue by the application’s maintenance triggers.

From the main VDEF Configuration Menu, select the menu option VDEF Suspend/Run Request Queue and change the value of the SUSPENDED FLAG field for the defined VDEF Request Queues (at this time “MAINTENANCE”) from “R”UNNING to “S”USPENDED.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter SUSR Suspend/Run Request Queue

Select Request Queue:

Enter MAINTENANCE

SUSPENDED FLAG: RUNNING//

Enter S\<uspended\>

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VDEF Error Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three conditions where VDEF can encounter an error. Two of these conditions cause a request to remain in either the Checked Out or Errored Out status in the VDEF Status display.

The first error type occurs when an application program sends a request to VDEF for a trigger event that is invalid or cannot be processed. Examples of this type error would be when an application’s trigger software is prematurely installed and there is no event set up in VDEF for that trigger; or when VDEF has either the custodial package or the Event API inactivated for that trigger event. For these type errors, VDEF, essentially, skips the request and the VDEF Requestor returns an error status to the calling application program. These types of errors do show up in the VDEF Status Monitor as Checked Out or Errored Out.

Another type of error is a fatal M error caused by code in a VDEF program that is not robust enough to handle certain types of erroneous data. These errors are unanticipated and will cause the VDEF message process to abort while the request is in the Checked Out status.

The third error type occurs when VDEF encounters a situation where it cannot continue processing a request or message due to corrupt or missing data in a VistA data file. These errors will usually result in an Errored Out status.

Below is a VDEF report showing 1 request in Checked Out and 4 in Errored Out status.

VDEF Status - DEC 28, 2005@10:47:50

Logical Link Status

VDEFVIE1: running task \#6274200

VDEFVIE2: stopped or caught up

VDEFVIE3: running task \#6281503

Requestor Status

MAINTENANCE: Activated Dest.: VISTA HL7 Req. Queue: MAINTENANCE

Request Processor Status

MAINTENANCE: Running

Current Task \# \[Proc\]: 6257283 \[20B4BBD4\] Task status: Active-Running

Requests waiting for purge: 53832 Last request#: 1441722

Checked Out(1) Queued Up(0) Errored Out(4)

Hit \<return/enter\> to continue or '^' to terminate:

## Checked Out Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are unprocessed requests in the VDEF Request Queue (Queued Up count \> 0) and VDEF is actively processing the queued requests, it is normal to see a count of 1 in the Checked Out status. If there are no requests in the VDEF Request Queue to be processed (Queued Up count = 0) and the Checked Out count is 1 or greater, there was a problem with one or more of the requests. VDEF was not able to process these requests. The VDEF Request Processor Monitor will attempt to re-queue Checked Out requests. This is usually successful. However when a request repeatedly gets left in the Checked Out status, it is because either a VDEF program or the message creation program that was called by VDEF terminated with a fatal M error. These errors indicate a problem that has to be researched and fixed. In order to help diagnose the cause of the error, IRM staff will have to find the error in the Kernel Error Trap that is associated to the VDEF error.

## Errored Out Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Controlled error situations that are built into VDEF processes will not result in a fatal M error and instead will cause VDEF to place the request into the Errored Out status with an error message in the record. These errors are generally caused by corrupt or missing data in the VistA database due to a timing error between the queuing process and the queue processor. The VDEF Request Processor Monitor will attempt to re-queue Checked Out requests. This is usually successful. If the cause is missing data in a VistA data file, there is generally no automated fix for this type of error.

## Documenting the Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In both situations the research that the IRM needs to do is similar:

- Find the IEN of the record in the VDEF Request Queue, display the record in the VDEF Request Queue, and copy and paste the global data into a text document.
- In the case of Checked Out records, find the error in the Error Trap log that is associated with the error, copy and paste the error trap data into a text document.

## Identify IENs of the Checked Out or Errored Out Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^%G

Global ^VDEFHL7(579.3,"C","C",1 for checked out records

or ^VDEFHL7(579.3,"C","E",1 for errored out records

VDEFHL7(579.3,"C","C",1

^VDEFHL7(579.3,"C","C",1,<u>133</u>) =

^VDEFHL7(579.3,"C","C",1,<u>182</u>) =

^VDEFHL7(579.3,"C","C",1,<u>192</u>) =

Or

^VDEFHL7(579.3,"C","E",1,<u>130</u>) =

^VDEFHL7(579.3,"C","E",1,<u>213</u>) =

^VDEFHL7(579.3,"C","E",1,<u>421</u>) =

Global ^

| WARNING | The IENs shown above are examples only. |
|-------------|-----------------------------------------|

Make a list of the numbers in the fourth <u>subscript position</u> as shown in the <u>underlined</u> examples above. These are the IENs of the request records in the VDEF Request Queue.

^VDEFHL7(579.3,1,1,IEN,0)=87^C^ORU^R01^^1^1^3041008.133111^<u>3041008.133114</u>^^^^^^3041020.145218^^^7

^VDEFHL7(579.3,1,1,IEN,.05,0)=^579.311^2^2

^VDEFHL7(579.3,1,1,IEN,.05,1,0)=1^SUBTYPE=VTLS

^VDEFHL7(579.3,1,1,IEN,.05,2,0)=2^IEN=15068405

^VDEFHL7(579.3,1,1,IEN,1,"B",1,1)=

^VDEFHL7(579.3,1,1,IEN,1,"B",2,2)=

The <u>bolded underlined</u> data in the example is the FileMan date and time that VDEF tried to process the request. In the example, it is <u>10/08/2004@13:33:11</u>.

CUT AND PASTE THE GLOBAL INFORMATION INTO A TEXT DOCUMENT.

For requests in the Checked Out status, find the error in the Error Trap that corresponds to the date and time in the record as shown above.

From the Error Trap display, use the “^L” option to display the entire symbol table.

CUT AND PASTE THE SYMBOL TABLE DISPLAY AND COPY IT INTO THE SAME TEXT DOCUMENT AS ABOVE.

E-mail the document or attach it to an error report, or add it to a Remedy Ticket as directed.

## Deleting the Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may be notified that it is OK to delete the Checked Out or Error Out requests. You will need the list of record IENs from the step 6.2. From a programmer prompt, do the following:

\>D Q^DI

VA FileMan 22.0

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 579.3 VDEF REQUEST QUEUE

EDIT WHICH FIELD: ALL// .06 REQUEST QUEUE ENTRIES (multiple)

EDIT WHICH REQUEST QUEUE ENTRIES SUB-FIELD: ALL// .01 REQUEST ENTRY NUMBER

THEN EDIT REQUEST QUEUE ENTRIES SUB-FIELD:

THEN EDIT FIELD:

Select VDEF REQUEST QUEUE REQUEST QUEUE NAME: MAINTENANCE

Select REQUEST ENTRY NUMBER: //(enter IEN of problem record found in §6.5, step 1)

REQUEST ENTRY NUMBER: // @

SURE YOU WANT TO DELETE THE ENTIRE 'nnn' REQUEST ENTRY NUMBER? Y (Yes)

Select VDEF REQUEST QUEUE REQUEST QUEUE NAME: MAINTENANCE

Select REQUEST ENTRY NUMBER: // (enter the IEN of a request from step 1)

REQUEST ENTRY NUMBER: // @

SURE YOU WANT TO DELETE THE ENTIRE 'nnn' REQUEST ENTRY NUMBER? Y (Yes)

(Repeat this portion for each record that has to be deleted.)

# Appendix A: KIDS Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INSTall Package(s)

Select INSTALL NAME: VDEF 1.0 Loaded from Distribution 12/21/04@17:11:09

=\> VDEF V1.0 ;Created on Dec 21, 2004@16:36:47

This Distribution was loaded on Dec 21, 2004@17:11:09 with header of

VDEF V1.0 ;Created on Dec 21, 2004@17:05:33

It consisted of the following Install(s):

VDEF 1.0

Checking Install for Package VDEF 1.0

Install Questions for VDEF 1.0

Incoming Files:

577 VDEF EVENT DESCRIPTION

577.4 VDEF EVENT SUBTYPES

579.1 VDEF REQUESTOR (including data)

579.2 VDEF DESTINATION (including data)

579.3 VDEF REQUEST QUEUE (including data)

579.5 VDEF PARAMETERS (including data)

579.6 VDEF CUSTODIAL PACKAGE

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// UCX LOGIN

VDEF 1.0

Install Started for VDEF 1.0:

Dec 21, 2004@17:13:21

Build Distribution Date: Dec 21, 2004

Installing Routines: Dec 21, 2004@17:13:22

Installing Data Dictionaries: Dec 21, 2004@17:14:04

Installing Data: Dec 21, 2004@17:14:04

Installing PACKAGE COMPONENTS:

Installing OPTION Dec 21, 2004@17:14:04

Updating Routine file...

Updating KIDS files...

VDEF 1.0 Installed.

Dec 21, 2004@17:14:05

Install Message sent \#306

Install Completed

| WARNING | This document assumes that a VDEF distribution has been successfully loaded and installed. |
|-------------|--------------------------------------------------------------------------------------------|

# Appendix B: VDEF Configuration Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  This option allows users to make various changes to VDEF settings.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option: SITE Site-Wide Parameters

VDEF SYSTEM: \<your system name\>//

VDEF MONITOR DELAY: 5M//

2.  This option allows setting of parameters used by the VDEF process that selects records from the VDEF Request Queue and creates outgoing HL7 messages.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option: REQ Request Queue Parameters

Select Request Queue: MAINTENANCE

ARCHIVAL PARAMETER: 11D 13H 46M 40S // 7D

CHECK-OUT TIME LIMIT: 16M 40S // 3M

REQUEST QUEUE WAKEUP PERIOD: 20S// 30S

3.  This option allows activating or inactivating of the VDEF process that receives requests from the internal VistA API calls and places them in the VDEF Request Queue.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter ActR Activate/Inactivate Requestor

Select Requestor:

Enter MAINTENANCE

> **NOTE:** Inactivating a requestor has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests made while the requestor is inactive will be PERMANENTLY lost. Make sure you really want to turn it off.

REQUESTOR ACTIVATION FLAG: INACTIVE//

Enter ACTIVE

4.  The option allows starting and stopping of the VDEF process that selects records from the VDEF Request Queue and creates outgoing HL7 messages.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter SUSR Suspend/Run Request Queue

Select Request Queue:

Enter MAINTENANCE

SUSPENDED FLAG: SUSPENDED//

Enter R

5.  This option allows users control over which custodial packages are allowed to queue up request in VDEF. If a custodial package is turned off, the request will be ignored. When a package is turned on, the request will be placed into the VDEF Request Queue.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter CUST VDEF Custodial Package Activate/Inactivate

Select Custodial Package:

Enter “?” FOR LIST CUSTODIAN PACKAGES

(EXAMPLE)

Choose from:

OUTPATIENT PHARMACY

GEN. MED. REC. - VITALS

ADVERSE REACTION TRACKING

Warning Notice: Inactivating a custodial package has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests for HL7 messages associated with this custodial package made while the package is inactivated will be PERMANENTLY lost. Make sure you really want to turn this custodial package off.

ACTIVATION STATUS: ACTIVE//

Enter ? *(You will have two (2) options)*A ACTIVEI INACTIVE

ACTIVATION STATUS: INACTIVE//

Enter A ACTIVE

| WARNING | This is for example only. Inactivating custodial packages in VDEF is not part of normal activities. Do this only if directed to do so. |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------|

6.  This option allows users control over which VDEF API Events are allowed to queue up request in VDEF. If a VDEF Event is turned off, the request will be ignored. When an Event is turned on, the request will be placed into the VDEF Request Queue.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter API VDEF Event API Activate/Inactivate

Select VDEF API Event:

Enter “?” for a list of VDEF API Events

(EXAMPLE)

ORU-R01-VTLS PATIENT VITALS Status: ACTIVEPkg: GEN. MED. REC. - VITALS

API EVENT ACTIVE FLAG: INACTIVE//

Enter

A Active or

I Inactive

| WARNING | This is for example only. Inactivating VDEF Event APIs is not part of the normal activities. Do this only if directed to do so. |
|-------------|---------------------------------------------------------------------------------------------------------------------------------|

7.  This option displays the screen showing the current VDEF parameters, as well as, the current status of the VDEF Queues.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter STAT Status of VDEF components.

You will see the following display. This example represents VDEF in its initial “never-used” State.

VDEF Status - DEC 28, 2005@11:35:19

Logical Link Status

VDEFVIE1: running task \#6274200

VDEFVIE2: stopped or caught up

VDEFVIE3: running task \#6286911

Requestor Status

MAINTENANCE: Activated Dest.: VISTA HL7 Req. Queue: MAINTENANCE

Request Processor Status

MAINTENANCE: Running

Current Task \# \[Proc\]: 6257283 \[20B4BBD4\] Task status: Active-Running

Requests waiting for purge: 53683 Last request#: 1442344

Checked Out(0) Queued Up(1) Errored Out(0)

Hit \<return/enter\> to continue or '^' to terminate:

8.  This option allows the creation of rules that control when the Request Queue Processor can be active or inactive.

Site Site-Wide Parameters

Req Request Queue Parameters

ActR Activate/Inactivate Requestor

SusR Suspend/Run Request Queue

Cust VDEF Custodial Package Activate/Inactivate

API VDEF Event API Activate/Inactivate

Stat Status of VDEF components

Sch Request Processor Schedule

Select VDEF Configuration and Status Option:

Enter Sch Request Processor Schedule

Select Request Queue: MAINTENANCE

No Scheduling Rules currently defined for this queue

Select Entry: 1

Are you adding '1' as a new REQUEST PROCESS SCHEDULE (the 1ST for this VDEF REQUEST QUEUE)? No// Y (Yes)

RULE: 1//

DAY OF THE WEEK: M Monday

FORCED STATUS: S SUSPENDED

Enter time in military form as HH:MM

FROM TIME: 16:00

Enter time in military form as HH:MM

TO TIME: 18:00

Currently defined Scheduling Rules are:

1\) On Monday the request processor is SUSPENDED from 16:00 to 18:00

Select Request Queue:

| WARNING | Although this function has been tested and works properly, do not use this feature of VDEF unless directed to do so. |
|-------------|----------------------------------------------------------------------------------------------------------------------|

# Appendix C: VDEF Alert Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of alerts that VDEF can generate.

1.  VDEF CHECKED OUT MONITOR FAILED TO START. CHECK ERROR TRAP.

(The scheduled task MONITOR^VDEFCONT did not start as requested by the VDEF

STARTUP OPTION.)

2.  RECORD \<IEN\> IN QUEUE \<Queue name\> HUNG IN CHECKED OUT STATUS.

(The request specified by the IEN in the queue specified in the QUEUE NAME has been

in the Checked Out status longer than the allowed time period.)

3.  VDEF REQUEST PROCESS \<Queue name\> FAILED TO START. CHECK ERROR TRAP.

(The task EN^VDEFREQ failed to start as requested by the VDEF STARTUP OPTION)

4.  VDEF QUEUE PROCESS MONITOR DID NOT START. CHECK ERROR TRAP.

(The task MONITOR^VDEFMON failed to start as requested by the VDEF STARTUP

OPTION)

5.  VDEF HAS REQUEUED CHECKED OUT RECORDS. NO ACTION NEEDED.

(The VDEF queue process monitor has requeued one or more requests that were hung in the

Checked Out status).

| WARNING | “NO ACTION NEEDED” is only true when this alert is not occurring every ten minutes. When this alert occurs every ten minutes, that is an indication that there is one or more VDEF requests that are getting hung in the Checked Out status and being re-queued but not processed. The alert cycle will continue until there is human intervention to correct the problem with the request records. |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

6.  VDEF HAS REQUEUED ERRORED OUT RECORDS. NO ACTION NEEDED.

(The VDEF queue process monitor has re-queued one or more requests that were in the

Errored Out status) .

| WARNING | “NO ACTION NEEDED” is only true when this alert is not occurring every ten minutes. When this alert occurs every ten minutes, that is an indication that there is one or more VDEF requests that are getting hung in the Errored Out status and being re-queued but not processed. The alert cycle will continue until there is human intervention to correct the problem with the request records. |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

7.  VDEF QUEUE PROCESS MONITOR HAS EXITED.

(The MONITOR^VDEFMON process has stopped running in response to a request to stop

from TaskMan)

8.  VDEF QUEUE '\<Queue name\>' AUTO-RESTARTED. NO ACTION REQUIRED.

(The MONITOR^VDEFMON process has found that the request queue process is not

running and has restarted it by creating a new EN^VDEFREQ task)

9.  VDEF QUEUE '\<Queue name\>' IS SUSPENDED. PLEASE START IT.

(The MONITOR^VDEFMON process has found that a Request Queue is in the Suspended

state and needs to be reset to the Running state)

10. VDEF REQUEST QUEUE PROCESSOR FOR \<’queue name’\> HAS EXITED.

(The request queue process EN^VDEFREQ has stopped running in response to a request

to stop from TaskMan or because the request queue status has changed to Suspended)