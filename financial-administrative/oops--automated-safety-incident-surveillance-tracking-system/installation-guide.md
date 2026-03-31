---
title: ASISTS GUI Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: OOPS
app_name: Automated Safety Incident Surveillance Tracking System
section: FIN
app_status: active
pkg_ns: OOPS
patch_ver: 2
patch_id: OOPS*2
group_key: "OOPS:OOPS:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this Installation Guide is to provide details on the installation of the Automated Safety Incident Surveillance Tracking System (ASISTS) Graphical User Interface (GUI) software.
audience: 
keywords: 
  - asists
  - installation
  - table
  - contents
  - install
  - server
  - oops
  - package
  - client
  - hosts
page_count: 0
word_count: 2749
section_count: 12
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2017
revision_count: 2
revision_newest: 03/07/2017
revision_oldest: 01/06/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=56"
---

![](asists-gui-version-2-installation-guide/001.png)

Automated Safety Incident Surveillance Tracking System (ASISTS) V. 2.0Graphical User Interface (GUI)Installation GuideJune 2002

(Revised March 2017)

Office of Enterprise Development

Management & Financial Systems

Revision History

|            |                                                                     |                     |                      |
|------------|---------------------------------------------------------------------|---------------------|----------------------|
| Date   | Description (Patch \# if applicable)                            | Project Manager | Technical Writer |
| 03/07/2017 | Update for Patch OOPS\*2\*29                                        | REDACTED            | REDACTED             |
| 01/06/09   | Enhancements from Patch OOPS\*2\*18 – Checksums, GUI Client Install | REDACTED            | REDACTED             |
| 06/2002    | Initial Version                                                     |                     | REDACTED             |

Table of Contents

1 Introduction [1](#introduction)

1.1 Purpose [1](#purpose)

1.2 Scope [1](#scope)

1.3 Acronyms [1](#acronyms)

2 Install Requirements [3](#install-requirements)

2.1 Package Integration [3](#package-integration)

2.2 Server Requirements [3](#server-requirements)

2.3 Client Requirements [4](#client-requirements)

3 Server Installation [5](#server-installation)

3.1 Server Instructions [5](#server-instructions)

3.1.1 Verify Checksums in the transport global [6](#verify-checksums-in-the-transport-global)

3.1.2 Back up all systems as deemed appropriate [6](#back-up-all-systems-as-deemed-appropriate)

3.2 Installation Example ASISTS 2. 0 [7](#installation-example-asists-2.-0)

3.3 ASISTS 2. 0 Checksums [12](#asists-2.-0-checksums)

4 Client Installation [15](#client-installation)

4.1 RPC Broker and HOSTS file [15](#rpc-broker-and-hosts-file)

4.2 ASISTS GUI Client Installation [18](#asists-gui-client-installation)

4.2.1 Instructions [21](#instructions)

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Acronyms](#acronyms)
- [Install Requirements](#install-requirements)
  - [Package Integration](#package-integration)
  - [Server Requirements](#server-requirements)
  - [Client Requirements](#client-requirements)
- [Server Installation](#server-installation)
  - [Server Instructions](#server-instructions)
    - [Verify Checksums in the transport global](#verify-checksums-in-the-transport-global)
    - [Back up all systems as deemed appropriate](#back-up-all-systems-as-deemed-appropriate)
  - [Installation Example ASISTS 2. 0](#installation-example-asists-2-0)
  - [ASISTS 2. 0 Checksums](#asists-2-0-checksums)
- [Client Installation](#client-installation)
  - [RPC Broker and HOSTS file](#rpc-broker-and-hosts-file)
  - [ASISTS GUI Client Installation](#asists-gui-client-installation)
    - [Instructions](#instructions)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide details on the installation of the Automated Safety Incident Surveillance Tracking System (ASISTS) Graphical User Interface (GUI) software.

The intended audience of this document includes Technical Services and National VISTA Support.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS V. 2.0 is the first ASISTS release to provide a Graphical User Interface to the ASISTS application. It offers the current roll-n-scroll functionality in a well-organized and user-friendly GUI environment. The GUI design is consistent in look and feel with current VistA GUI applications. The intent of the new GUI version was to mimic the existing roll-n-scroll versions. With the exception of new reports, no new functionality has been added. See the Release Notes for further information.

ASISTS GUI offers the following features.

- The user will be able to access on line help for the software.
- The user will be able to print the following reports:
- Log of Federal Occupational Injuries and Illness
- Log of Needlestick Incidents
- Accident Report Status
- Report of Accident
- Seven Different types of Incident Reports
- Process CA1/CA2 forms

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS Automated Safety Incident Surveillance Tracking System
DOL Department Of Labor
GUI Graphical User Interface
HFS Host File Server
IG Installation Guide
RPC Remote Procedure Call
VA Department of Veterans Affairs
VISTA Veterans Health Information Systems and Technology Architecture

# Install Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Package Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following package versions (or higher) must be installed prior to loading this patch of ASISTS.

> Kernel 8.0

> ToolKit 7.3

> RPC Broker 1.1

> MailMan 7.1

> VA FileMan 22.0

> PAID 4.0

## Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any site not currently running the ASISTS application and wishing to install ASISTS GUI need not install all previous ASISTS patches since it is a complete install.

After installation, every VistA user should be assigned (in their secondary menu) the OOPS GUI EMPLOYEE menu so that they may be able to file a workers’ compensation claim using ASISTS GUI. This menu option must be assigned to every user, in addition to any menu(s) assigned from the list below, for ASISTS GUI to function properly.

Other menu options that should be assigned to the appropriate user in their secondary menu are as follows.

OOPS GUI EMPLOYEE HEALTH MENU ASISTS GUI Employee Health Menu (Context)

OOPS GUI SAFETY OFFICER MENU ASISTS GUI Safety Menu (Context)

OOPS GUI SUPERVISOR MENU ASISTS GUI Supervisor Menu (Context)

OOPS GUI UNION MENU ASISTS GUI Union Menu (Context)

OOPS GUI WORKERS' COMP MENU ASISTS GUI Workers' Comp Menu (Context)

There are three items to consider when using ASISTS after the GUI version has been installed.

1.  Any claim initiated using the roll-n-scroll version must be completed using the roll-n-scroll version. The reason for this is that portions of the claim are now filed at different times in the new GUI version. Therefore, toggling back and forth between the old and new version may cause claims to be incomplete and rejected when filing with DOL.
2.  To prevent the above from occurring, it is strongly recommended that the roll-n-scroll menu options be removed from the users menu prior to assigning the new GUI menus.
3.  If you are an integrated facility with a large number of claims (over 2500) or you anticipate running reports spanning large time periods, we recommend that the Kernel System Parameter, BROKER ACTIVITY TIMEOUT be set to 600. This will help prevent “connection to server” timeout errors that occur when large amounts of data are processed both on the client and server machines.

## Client Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This initial version of ASISTS GUI should be run in a test environment before installation on a production system.

To run this Delphi-based application, the following configuration is recommended.

- Intel Pentium 90 or higher (P166 recommended)
- Microsoft Windows 95, 98, NT 4.0,or Windows 2000
- Memory: 32MB of RAM (64MB or more recommended)
- Hard disk space: 8MB
- VGA or higher resolution monitor
- Mouse or other pointing device
- Networks supported: Any Microsoft Windows 95, 98, Windows NT, or Windows 2000 or higher compatible network

# Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This distribution contains a full package release of ASISTS. If the system you are installing into is not fully patched, it does not need to be. This distribution contains bug fixes to the roll-n-scroll as well as all functionality for ASISTS GUI and must be installed to run the ASISTS GUI and to implement the bug fixes in the ASISTS roll-n-scroll. The bug fixes to the ASISTS roll-n-scroll were implemented mainly to alleviate problems with the electronic transmission of claims to the Department of Labor until the GUI became fully integrated at all facilities.

We recommend that you install ASISTS V. 2.0 into a training or test account that is a mirror of your production account and test prior to installing in your production account.

A pre-installation routine is run that changes the .01 field in the ASIST DOL CAUSE OF INJURY CODE file (#2263.2); therefore, the global protection on this file must be set to allow sets and kills (RWP).

Instructions for loading the distribution for ASISTS V. 2.0.

> Total time estimated for installation is less than 15 minutes.

> NOTE: We recommend that you set your PC or terminal for scroll-back (with a large enough buffer size) and plan to run the installation to the screen. This will allow you to monitor the process and include the scrolling region data in the history log.

> Select the option *Kernel Installation and Distribution System*, XPD MAIN. Choose the *Installation* option, followed by the option, *Load the distribution*. When prompted to enter a host file, enter OOPS2_0.KID, as shown in the following example:

\>D ^XUP

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INstallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: OOPS2_0.KID;1

KIDS Distribution saved on Feb 21, 2002@16:21:06

Comment: ASISTS - VERSION 2.0 built on 2/21/01

This Distribution contains Transport Globals for the following Package(s):

OOPS 2.0

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

OOPS 2.0

Use INSTALL NAME: OOPS 2.0 to install this Distribution.

(Optional) Print a list of package components with the KIDS Build File Print option if you would like a complete listing of package components (e.g., files, routines, and options) exported with this software.

### Verify Checksums in the transport global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the option Verify Checksums in Transport Global to verify that all routines have the correct checksum. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Log a NOIS and/or call the national Help Desk and report the problem.

### Back up all systems as deemed appropriate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Example ASISTS 2. 0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Although no new mail groups have been added, since this is a complete package release we have included the mail groups. Someone will have to be assigned as the mail group coordinator. All existing mail groups will be left intact and existing members will not need to be re-added.

> Note that the ASISTS roll-n-scroll menu options should be disabled when installing this release.

> Select the option Kernel Installation and Distribution System, XPD MAIN. Choose the Installation option, followed by the option, Installation. When prompted to enter the install name, enter ASISTS 2.0 as shown below:

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: OOPS 2.0 Loaded from Distribution 2/27/02@14:45:54

> =\> ASISTS - VERSION 2.0 built on 2/21/01 ;Created on Feb 21, 2002@16:21:

> This Distribution was loaded on Feb 27, 2002@14:45:54 with header of

> ASISTS - VERSION 2.0 built on 2/21/01 ;Created on Feb 21, 2002@16:21:06

> It consisted of the following Install(s):

> OOPS 2.0

> Checking Install for Package OOPS 2.0

> Install Questions for OOPS 2.0

> Incoming Files:

> 2260 ASISTS ACCIDENT REPORTING

> Note: You already have the 'ASISTS ACCIDENT REPORTING' File.

> 2261 ASISTS CHARACTERIZATION OF INJURY (including data)

> Note: You already have the 'ASISTS CHARACTERIZATION OF INJURY' File.

> I will OVERWRITE your data with mine.

> 2261.1 ASISTS DOL ANATOMICAL LOCATION CODES (including data)

> \*BUT YOU ALREADY HAVE 'ASISTS BODY PARTS' AS FILE \#2261.1!

> Shall I write over your ASISTS BODY PARTS File? YES// YES - respond yes

> I will OVERWRITE your data with mine.

> 2261.2 ASISTS CRITICAL TRACKING ISSUES (including data)

> Note: You already have the 'ASISTS CRITICAL TRACKING ISSUES' File.

> I will OVERWRITE your data with mine.

> 2261.3 ASISTS PERSONAL PROTECTIVE EQUIPMENT (including data)

> Note: You already have the 'ASISTS PERSONAL PROTECTIVE EQUIPMENT' File.

> I will OVERWRITE your data with mine.

> 2261.4 ASISTS SETTING OF INJURY (including data)

> Note: You already have the 'ASISTS SETTING OF INJURY' File.

> I will OVERWRITE your data with mine.

> 2261.5 ASISTS PURPOSE FOR USING SHARPS (including data)

> Note: You already have the 'ASISTS PURPOSE FOR USING SHARPS' File.

> I will OVERWRITE your data with mine.

> 2261.6 ASISTS OCCURRENCE OF SHARPS INJURY (including data)

> Note: You already have the 'ASISTS OCCURRENCE OF SHARPS INJURY' File.

> I will OVERWRITE your data with mine.

> 2261.7 ASISTS DEVICE/EQUIPMENT (including data)

> Note: You already have the 'ASISTS DEVICE/EQUIPMENT' File.

> I will OVERWRITE your data with mine.

> 2261.8 ASISTS RESULTS (including data)

> Note: You already have the 'ASISTS RESULTS' File.

> I will OVERWRITE your data with mine.

> 2261.9 ASISTS SAFETY CHARACTERISTICS (including data)

> Note: You already have the 'ASISTS SAFETY CHARACTERISTICS' File.

> I will OVERWRITE your data with mine.

> 2262 ASISTS SITE PARAMETER

> Note: You already have the 'ASISTS SITE PARAMETER' File.

> 2262.1 ASISTS DOL DISTRICT OFFICE (including data)

> Note: You already have the 'ASISTS DOL DISTRICT OFFICE' File.

> I will OVERWRITE your data with mine.

> 2262.2 ASISTS DEVICE SIZE (including data)

> Note: You already have the 'ASISTS DEVICE SIZE' File.

> I will OVERWRITE your data with mine.

> 2262.3 ASISTS NEEDLESTICK BRANDS

> Note: You already have the 'ASISTS NEEDLESTICK BRANDS' File.

> 2263 ASISTS DOL TYPE OF INJURY CODES (including data)

> I will OVERWRITE your data with mine.

> 2263.1 ASISTS DOL SOURCE OF INJURY CODES (including data)

> I will OVERWRITE your data with mine.

> 2263.2 ASISTS DOL CAUSE OF INJURY CODES (including data)

> I will OVERWRITE your data with mine.

> 2263.3 ASISTS DOL NATURE OF INJURY CODES (including data)

> I will OVERWRITE your data with mine.

> 2263.5 ASISTS DOL PROVIDER TITLE (including data)

> I will OVERWRITE your data with mine.

> 2263.6 ASISTS OWCP CHARGEBACK CODES (including data)

> I will OVERWRITE your data with mine.

> 2263.7 ASISTS UNION INFORMATION

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'OOPS SAFETY': ENTER COORDINATOR NAME

> Enter the Coordinator for Mail Group 'OOPS INJURY': ENTER COORDINATOR NAME

> Enter the Coordinator for Mail Group 'OOPS EH': ENTER COORDINATOR NAME

> Enter the Coordinator for Mail Group 'OOPS UNION': ENTER COORDINATOR NAME

> Enter the Coordinator for Mail Group 'OOPS NDB MESSAGES': ENTER COORDINATORNAME

> Enter the Coordinator for Mail Group 'OOPS WCP': ENTER COORDINATOR NAME

> Enter the Coordinator for Mail Group 'OOPS WC MESSAGE': ENTER COORDINATOR NAME

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

> When prompted to select the options you would like to place out of order, enter the following:

> ASISTS Employee Menu OOPS EMP MENU

> ASISTS Employee Health Menu OOPS EMP HEALTH MENU

> ASISTS Safety Officers Menu OOPS SAFETY MENU

> ASISTS Supervisor Menu OOPS SUP MENU

> ASISTS Union Menu OOPS UNION MENU

> ASISTS Worker's Compensation Menu OOPS WORKER'S COMP MENU

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// Enter - We recommend that you print this to the screen so that you can monitor the progress

ASISTS Install Print Example

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: UT Utilities

Build File Print

Install File Print

Convert Loaded Package for Redistribution

Display Patches for a Package

Purge Build or Install Files

Rollup Patches into a Build

Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities Option: INStall File Print

Select INSTALL NAME: OOPS 2.0 Install Completed 2/28/02@16:05:03

=\> ASISTS - VERSION 2.0 built on 2/21/01 ;Created on Feb 21, 2002@16:21:

DEVICE: HOME// UCX/TELNET

STATUS: Install Completed DATE LOADED: FEB 12, 2002@15:57:26

INSTALLED BY: ASISTS,PROGRAMMER

NATIONAL PACKAGE: ASISTS

INSTALL STARTED: FEB 28, 2002@16:00:06 16:05:03 0:04:57

ROUTINES: 16:00:26 0:00:20

PRE-INIT CHECK POINTS:

XPD PREINSTALL STARTED 16:00:29 0:00:03

XPD PREINSTALL COMPLETED 16:00:29

FILES:

ASISTS ACCIDENT REPORTING 16:01:11 0:00:42

ASISTS CHARACTERIZATION OF INJURY 16:01:12 0:00:01

ASISTS DOL ANATOMICAL LOCATION CODES 16:01:13 0:00:01

ASISTS CRITICAL TRACKING ISSUES 16:01:14 0:00:01

ASISTS PERSONAL PROTECTIVE EQUIPMENT 16:01:15 0:00:01

ASISTS SETTING OF INJURY 16:01:16 0:00:01

ASISTS PURPOSE FOR USING SHARPS 16:01:16

ASISTS OCCURRENCE OF SHARPS INJURY 16:01:17 0:00:01

ASISTS DEVICE/EQUIPMENT 16:01:18 0:00:01

ASISTS RESULTS 16:01:19 0:00:01

ASISTS SAFETY CHARACTERISTICS 16:01:21 0:00:02

ASISTS SITE PARAMETER 16:01:24 0:00:03

ASISTS DOL DISTRICT OFFICE 16:01:24

ASISTS DEVICE SIZE 16:01:25 0:00:01

ASISTS NEEDLESTICK BRANDS 16:01:26 0:00:01

ASISTS DOL TYPE OF INJURY CODES 16:01:28 0:00:02

ASISTS DOL SOURCE OF INJURY CODES 16:01:29 0:00:01

ASISTS DOL CAUSE OF INJURY CODES 16:01:31 0:00:02

ASISTS DOL NATURE OF INJURY CODES 16:01:32 0:00:01

ASISTS DOL PROVIDER TITLE 16:01:36 0:00:01

ASISTS OWCP CHARGEBACK CODES 16:01:36

ASISTS UNION INFORMATION 16:01:39 0:00:03

ASISTS Install Print Example, cont.

BULLETIN 16:04:05 0:02:26

SECURITY KEY 16:04:06 0:00:01

MAIL GROUP 16:04:08 0:00:02

REMOTE PROCEDURE 16:04:15 0:00:07

OPTION 16:04:57 0:00:42

INSTALL QUESTION PROMPT ANSWER

XPF2261.1#1 Shall I write over your ASISTS BODY PARTS File YES

XPM187#1 Enter the Coordinator for Mail Group 'OOPS SAFETY' ASISTSEMP,ONE

XPM188#1 Enter the Coordinator for Mail Group 'OOPS INJURY' ASISTSEMP,ONE

XPM189#1 Enter the Coordinator for Mail Group 'OOPS EH' ASISTSEMP,ONE

XPM190#1 Enter the Coordinator for Mail Group 'OOPS UNION' ASISTSEMP,ONE

XPM234#1 Enter the Coordinator for Mail Group 'OOPS NDB MESSAGES' ASISTSEMP,ONE

XPM272#1 Enter the Coordinator for Mail Group 'OOPS WCP' ASISTSEMP,ONE

XPM273#1 Enter the Coordinator for Mail Group 'OOPS WC MESSAGE' ASISTSEMP,ONE

XPO1 Want KIDS to Rebuild Menu Trees Upon Completion of Install NO

XPI1 Want KIDS to INHIBIT LOGONs during the install NO

XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols YES

MESSAGES:

Install Started for OOPS 2.0 :

Feb 28, 2002@16:00:06

Build Distribution Date: Feb 21, 2002

Installing Routines:

Feb 28, 2002@16:00:26

Running Pre-Install Routine: ^OOPSXV2

Modifying ASISTS DOL CAUSE OF INJURY CODE Table File (#2263.2)

Table update complete.

Installing Data Dictionaries:

Feb 28, 2002@16:01:39

Installing Data:

Feb 28, 2002@16:04:03

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing SECURITY KEY

ASISTS Install Print Example, cont.

Installing MAIL GROUP

Installing REMOTE PROCEDURE

Installing OPTION

Feb 28, 2002@16:04:57

Updating Routine file...

Updating KIDS files...

OOPS 2.0 Installed.

Feb 28, 2002@16:05:03

## ASISTS 2. 0 Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine name Before Patch After Patch Patch List

------------ ------------ ----------- ----------

OOPSCA 2301151 2310751

OOPSCA1 15500850 15500850

OOPSCA2 12275378 12275378

OOPSCC 12321330 12345236

OOPSCSN 380273 380273

OOPSDIS 3554915 3554915

OOPSDM 2547198 2547198

OOPSDOL 15614480 15721159

OOPSDOL1 13466377 13360473

OOPSDOL2 11995337 12309298

OOPSDOLX 5676301 5717339

OOPSDS12 932431 932431

OOPSEMP1 5698604 5698604

OOPSEMP2 19244605 19244605

OOPSEMPB 12343058 12343058

OOPSESIG 1505770 1505770

OOPSESP 422796 434193

OOPSESR 3608495 3608495

OOPSEUT 448543 448543

OOPSF167 1505245 1505245

OOPSGUI0 New 9070286

OOPSGUI1 New 7386076

OOPSGUI2 New 7721031

OOPSGUI3 New 7239317

OOPSGUI4 New 10494219

OOPSGUI5 New 8718900

OOPSGUI6 New 9464099

Routine name Before Patch After Patch Patch List

------------ ------------ ----------- ----------

OOPSGUI7 New 3239568

OOPSGUI8 New 5822984

OOPSGUI9 New 11558303

OOPSGUIF New 5830210

OOPSGUIT New 14519272

OOPSLOG 12819248 12819248

OOPSMBUL 3042701 3094362

OOPSNDB 10569029 10569029

OOPSNDBX 6114982 6085669

OOPSP50 20469378 20469378

OOPSPC10 23139938 23139938

OOPSPC11 9956072 9956072

OOPSPC20 24134848 24134848

OOPSPC21 15501347 15501347

OOPSPC30 32369369 32369369

OOPSPC40 23264208 23264208

OOPSPC41 14796052 14796052

OOPSPC50 20536076 20536076

OOPSPC51 12041348 12041348

OOPSPC60 32841819 32841819

OOPSPC70 12504559 12504559

OOPSPC71 15381737 15381737

OOPSPC80 17073219 17073219

OOPSPC81 15720404 15720404

OOPSPCA 4423009 4423009

OOPSPI2 13682 13682

OOPSPRT 15564255 15564193

OOPSPRT1 6581442 6592295

OOPSPRT2 2026357 2026357

OOPSPUT1 4161692 4161692

OOPSSOF1 2772099 2772099

OOPSSOF2 1160174 1160174

OOPSSUP1 8823897 9290597

OOPSSUP2 21889563 21889563

OOPSSUP3 6096383 6096383

OOPSSUPB 16710763 16710763

OOPSUTL1 7558696 7993041

OOPSUTL2 9875415 10310661

OOPSUTL3 9184013 9184013

OOPSUTL4 11500958 11393323

OOPSUTL5 9903548 9902702

OOPSUTL6 4360724 5085028

OOPSVAL1 11839452 11999948

OOPSWCE 11277164 12998182

OOPSWCE1 16611391 16611391

OOPSWCE2 23782367 23782367

OOPSWCSE 5901255 5901255

OOPSXV2 New 6571246

Total number of routines: 75

--------

# Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## RPC Broker and HOSTS file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>RPC BROKER</u>

The assumption is made that the user’s PC has the required RPC Broker Client Workstation set up. If this is not the case, the user should first install this software. The RPC Broker files and installation instructions can be found on the VA’s RPC Broker web page. These files must be installed before running the ASISTS GUI application and can be found at the following web site:

<http://vista.med.va.gov/broker/>

There are two ways in which ASISTS can communicate with the Server. The first is the use of the hosts file and serverlist utility (explained in detail below). The second option, which allows the user to bypass the “Connect To” popup screen, is to add two command line parameters to the shortcut used to execute ASISTS 2.0. The first parameter is the DNS entry\definition for the host system; the second parameter is the port the RPC listener is running under. The command line parameters should follow the shortcut definition by a single space and the parameters should be separated by a single space.

Here is a sample of how to bypass the use of the HOSTS file.

" C:\Program Files (x86)\ASISTS\ASISTS.exe" isc1az3.REDACTEDva.gov 9201

Notice how the parameters are outside of the final quote (“), and separated by a single space. In this example, isc1az3.REDACTEDva.gov is the DNS entry for the host (fictitious) and 9201 is the RPC listener port.

Following are the directions on how to use the traditional method of a HOSTS file and serverlist utility.

<u>HOSTS file</u>

A link must be established between the client and the server via the PC's Hosts file and the PC's Windows Registry. The Hosts file (no extension) is in the following:

> C:\Windows - for Windows 95 or 98

> C:\WinNt\System32\Drivers\Etc - for Windows NT 4

If the Hosts file does not exist, it must be created. (There may be a hosts.sam sample file already in place.) Note that if you create the file with notepad, notepad automatically adds a .txt extension. To remove the extension, use Explorer to rename it, leaving off the .txt.

If the Hosts file already exists, do not delete anything. Follow these instructions for updating the Hosts file:

1\. If the user needs to access only one ASISTS GUI Server, and the ServerPort is 9200, then add a line to the Hosts file, as shown in the example below, using the IP address provided by the server administrator. (There must be at least one space between the address and the name. There can be no spaces in the name itself.)

> REDACTED

2.  If the user needs to access only one ASISTS GUI Server and the ServerPort is not 9200, then add one line to the Hosts file as shown in Scenario 1 above and run the ServerList utility described in Scenario 3 below.
3.  If the user needs to access multiple ASISTS GUI Servers and/or the ServerPort is NOT 9200, add the ASISTS GUI Server names to the Hosts file:
    333. BrokerServer1 (The names can be anything you like)

> 152.111.222.444 BrokerServer2

Run the ServerList Utility installed via the installation of the ASISTS GUI install package. The left window of the ServerList utility shows those servers that have been set up as Host Servers in the HOSTS file. The right window shows those servers that have been set up as BrokerServers. To enable a BrokerServer, double-click on the name in the left window to move it to the right window and then enter the corresponding ServerPort number. (Note: the order of the names in the right list is the order they will be displayed in the drop-down box when starting ASISTS GUI. If only one server is listed on the right, then you won’t see the drop down box. It will automatically select that server as the default). A left-click in the ‘Del’ column marks and unmarks servers for deletion. See the following ServerList screen print for an example.

![](asists-gui-version-2-installation-guide/002.png)

## ASISTS GUI Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS GUI.exe software can be installed on each PC or placed on a shared drive. Do not place the executable directly on the desktop. There is a note in the instructions section below if you wish to install the software on a shared drive.

Follow these instructions to install ASISTS GUI on the client machine.

- Double Click on oops2_p29.exe. This will launch the InstallShield Wizard.

![](asists-gui-version-2-installation-guide/003.png)

- When the “Welcome” screen is displayed, click "Next".

> ![](asists-gui-version-2-installation-guide/004.png)

- On the “Choose Destination Location” Click Next, unless you wish to change the folder to which ASISTS will install to. It’s recommended to use the default/displayed folder unless installing to a network drive.

> ![](asists-gui-version-2-installation-guide/005.png)

- Click “Install” to begin the installation.

> ![](asists-gui-version-2-installation-guide/006.png)

- The ASISTS GUI will be installed and the “InstallShield Wizard Completed” screen will be displayed. Click "Finish" and the ASISTS GUI installation is now complete.

> Please note: It is not necessary to re-boot your machine after the installation.

### Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This installation installs the GUI executable on the user’s workstation at location: C:\Program Files (x86)\ASISTS\ASISTS.exe (unless another directory was specified on the “Choose Designation Location” screen). Using Explorer, go to the directory location of the ASISTS.exe (on the user’s workstation), create a Shortcut, and paste or copy it to the user’s Desktop for convenient access to the application.

> If placed on a Network, then a shortcut to the executable on the shared drive (specified in the “Destination Folder” screen) can be created on the users’ desktop. It is very important to remember that even if the executable is installed on a shared drive, the installation of the RPC Client software and Hosts file (Section 4.1) still must be installed on each user’s workstation for ASISTS GUI to work.

> If any prior versions of the applications exist on in the user’s directory location referenced above, these should be deleted.