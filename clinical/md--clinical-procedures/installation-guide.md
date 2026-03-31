---
title: Clinical Procedures Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1
group_key: "MD:MD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: > In the Package (#9.4) file, this application is known as Clinical Procedures (CP). The package namespace is MD. File numbers are in the range of 702 to 704 and are stored in the ^MDD and ^MDS globals.
audience: 
keywords: 
  - installation
  - table
  - clinical
  - contents
  - procedures
  - server
  - install
  - client
  - installing
  - application
page_count: 0
word_count: 2149
section_count: 9
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](clinical-procedures-version-1-installation-guide/001.png)

CLINICAL PROCEDURESINSTALLATION GUIDE

April 2004

Revised for National Release August 2006

VistA Health Systems Design and Development

#### Revision History

|                                                                                                                            |             |                                    |
|----------------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------|
| Description                                                                                                            | Date    | Author                         |
| Originally released.                                                                                                       | April 2004  |                                    |
| The following pages were revised for national release: 1, 3-5, 9-10 (“Post Installation Tasks on the M Server” was moved). | August 2006 | <span class="mark">REDACTED</span> |
|                                                                                                                            |             |                                    |

#### Table of Contents

# Installation Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation Guide](#installation-guide)
  - [Overview](#overview)
  - [Clinical Procedures V. 1.0 Installation (General)](#clinical-procedures-v-10-installation-general)
    - [Pre-installation instructions:](#pre-installation-instructions)
  - [Clinical Procedures V. 1.0 Installation (M Server)](#clinical-procedures-v-10-installation-m-server)
    - [Note: If CP is only being installed and not implemented, only the M server installation needs to be completed. If the application is going to be implemented, the M server installation must be done before the client installation.](#note-if-cp-is-only-being-installed-and-not-implemented-only-the-m-server-installation-needs-to-be-completed-if-the-application-is-going-to-be-implemented-the-m-server-installation-must-be-done-before-the-client-installation)
    - [Installation Instructions:](#installation-instructions)
  - [### M Server Installation – Example Screen Listing](#m-server-installation-example-screen-listing)
  - [Post Installation Tasks on the M Server](#post-installation-tasks-on-the-m-server)
  - [Clinical Procedures V. 1.0 Installation (Client)](#clinical-procedures-v-10-installation-client)
    - [> Note:](#note)
    - [Installing the Client](#installing-the-client)
  - [Customizing the Client Installation](#customizing-the-client-installation)
  - [Server Based Installation](#server-based-installation)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> • This is the national release of Clinical Procedures.

> In the Package (#9.4) file, this application is known as Clinical Procedures (CP). The package namespace is MD. File numbers are in the range of 702 to 704 and are stored in the ^MDD and ^MDS globals.

> Clinical Procedures is the custodial package of the Medicine package including the MC namespace and all Medicine files. Contents of this package can be found in the VistA Documentation Library (VDL).

> The Clinical Procedures package is comprised of two parts, the M Server and the Client workstation. This guide addresses both the installation of the KIDS build on the M Server and the executable on the workstation.

> • Requirements for M Server installation:

> The M Server (disk) storage requirements for this package are:

| Globals | Type of Data | Size         | Journaling |
|-------------|------------------|------------------|----------------|
| ^MDS        | Static global    | 25 k             | Yes            |
| ^MDD        | Patient data     | 25-75 k/ patient | Yes            |

> The following describes the installation environment for the Clinical Procedures package on the M server:

1.  VA FileMan V. 22 or greater
2.  Kernel V. 8.0 or greater
3.  Kernel Toolkit V. 7.3 or greater
4.  Kernel RPC Broker V. 1.1 or greater
5.  PIMS (Patient Information Management System) V. 5.3 or greater (including):
    1.  Registration V. 5.3
    2.  Scheduling V. 5.3
6.  Health Summary V. 2.7 or greater
7.  HL7 (Health Level 7) V. 1.6 or greater
8.  Consult/Request Tracking V. 3.0
9.  TIU (Text Integration Utilities) V. 1.0
10. Order Entry V. 3.0 (CPRS (Computerized Patient Record System) V. 1.0 (GUI V. 22.16)) or greater
11. PCE (Patient Care Encounter) V. 1.0 or greater
12. VistA Imaging V. 3.0 or greater (includes installation of background processor and jukebox)
13. Medicine V. 2.3 (optional)

> These packages must be patched up through and including the following patches before Clinical Procedures is installed:

1.  Patch 17 of Consult/Request Tracking V. 3.0 (GMRC\*3.0\*17)
2.  Patch 112 of Order Entry V. 3.0 (OR\*3.0\*112)
3.  Patch 109 of Text Integration Utilities V. 1.0 (TIU\*1.0\*109)
4.  Patch 7 of Imaging V. 3.0 (MAG\*3.0\*7)
5.  Patch 93 of HL7 V. 1.6 (HL\*1.6\*93)
6.  Patch 98 of HL7 V. 1.6 (HL\*1.6\*98)
7.  If Medicine V. 2.3 is installed, you must install Patch 24 of Medicine (MC\*2.3\*24), and Patch 146 of Kernel (XU\*8.0\*146).

> • Requirements for VistA client installation:

> The client (disk) storage requirements are:

| Type of Data | Size |
|------------------|----------|
| Application      | 900 k    |
| Help Files       | 6638 k   |

> The following describes the installation environment for the Clinical Procedures package on the VistA client workstation:

1.  Workstations must be running under Windows NT (V4 or later), Windows 2000, or Windows XP. Refer to <http://vaww.vairm.vaco.va.gov/vadesktop> for additional information on VA standard desktop configurations.
2.  RPC Broker Workstation must be installed.
3.  The workstation must be connected to the local area network.
4.  Twelve (12) megabytes of available disc space is needed to run the program.

## Clinical Procedures V. 1.0 Installation (General)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-installation instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Create, place, and set the journaling option for the globals ^MDD and ^MDS on the volume set. These new globals are released with the Clinical Procedures package. Be sure to coordinate this task with the VistA systems manager to avoid placing the globals in default locations and applying incorrect settings. See below for information on placing globals in Cache.

> 2\. If the link filer is running, shut down HL7 logical link MCAR INST before installing. Refer to the Configuration Instructions section of the Setting Up HL7 Parameters chapter of the Clinical Procedures Implementation Guide for instructions on shutting down MCAR INST.

Global Placement

You are recommended to place the globals ^MDD and ^MDS where the current Medicine globals reside. Dataset size should be estimated based on figures below and the number of studies done at your site.

Instructions for adding a new dataset can be obtained from the Avanti Library located at <u>\<<http://vaww.va.gov/custsvc/cssupp/avanti/Library.htm>\></u>.

Select “Add_Dataset_VMS_Cache’.”

Once the new dataset has been created and mounted, you must add a new entry for the ^MDD and ^MDS globals to the Global Mapping section in the Caché Configuration Manager. You need a new entry for each running and activated Caché configuration , such as Configuration Manager\Namespace\VAH\Global Mapping, and you will need to update each running Caché configuration in the cluster.

The ^MDD and ^MDS globals can be created after the Global Mapping has been updated. Log into the VAH namespace. From the programmer mode prompt, issue the following commands - S ^MDD=”” and S ^MDS=””.

If you have any questions, please contact the Health System Technical Support (HSTS) team for guidance.

DSM Sites

It is recommended to place ^MDD and ^MDS on the volume set where the current Medicine globals reside. These globals must be placed with appropriate protection assignments as indicated in the table.

  
Translation Table Information

| Globals | Type of Data | Size       | Placement       | Journaling | Protection |
|-------------|------------------|----------------|---------------------|----------------|----------------|
| ^MDS        | Static global    | 25 k           | Medicine volume set | Yes            | RWP            |
| ^MDD        | Study data       | 25-75 k/ study | Medicine volume set | Yes            | RWP            |

From the programmer mode prompt, issue the following commands - S ^MDD=”” and S ^MDS=””.

If you have any questions, please contact the Health System Technical Support (HSTS) team for guidance.

## Clinical Procedures V. 1.0 Installation (M Server)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Note: If CP is only being installed and not implemented, only the M server installation needs to be completed. If the application is going to be implemented, the M server installation must be done before the client installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Installation Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Download MD1_0.EXE (Executables), binary and MD1_0.KID (KIDS built), Ascii from the anonymous.software on download.vista.med.va.gov. Move the files to the appropriate directory on your system.

> The client installation executable MD1_0.exe contains the following files:

> CP User.exe

> CP Manager.exe

> CP Gateway.exe

> CP MANAGER.hlp - Help file

> CP MANAGER.cnt - Help file

> CP USER.hlp - Help file

> CP USER.cnt- Help file

> CP GATEWAY.hlp- Help file

> CP GATEWAY.cnt- Help file

> 2\. Copy the MD1_0.kid from the directory selected above to the installation directory on the VistA system, (M Server) Note: ASCII transfer format must be used for this file.

> 3\. Log on to the Vista system, (M Server) where Clinical Procedures is to be installed. Be sure you are set in a programmer environment.

> 4\. Programmer variables can be initiated by executing the command D ^XUP. Validate that DUZ(0)=”@”.

> 5\. Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Load a Distribution to load the MD1_0.kid file into your M system.

> 6\. Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Install Package(s) to install the distribution into your M system. Refer to the M Server Installation example in this manual for additional information.

## ### M Server Installation – Example Screen Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option: INSTALlation

Select Installation Option: LOAD a Distribution

Enter a Host File: MD1_0.KID

KIDS Distribution saved on Mar 17, 2004@10:52:05

Comment: Clinical Procedures version 1.0.

This Distribution contains Transport Globals for the following Package(s):

MD 1.0

Distribution OK!

Want to Continue with Load? YES// \<RET\>

Loading Distribution...

MD 1.0

Use INSTALL NAME: MD 1.0 to install this Distribution.

Select Installation Option: INStall Package(s)

Select INSTALL NAME: MD 1.0 Loaded from Distribution 4/26/04@14:53:56

=\> Clinical Procedures Version 1.0. ;Created on Mar 17, 2004@10:52:05

This Distribution was loaded on Apr 26, 2004@14:53:56 with header of

Clinical Procedures Version 1.0. ;Created on Mar 17, 2004@10:52:05

It consisted of the following Install(s):

MD 1.0

Checking Install for Package MD 1.0

Install Questions for MD 1.0

Incoming Files:

702 CP TRANSACTION

702.01 CP DEFINITION

702.09 CP INSTRUMENT (including data)

703.1 CP RESULT REPORT

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'MD DEVICE ERRORS': SMITH,CHARLENE

CS 162-4 FISCAL SYSTEMS ANALYST

Enter the name of a person who will be the coordinator for the MD Device Errors mail group. This mail group will contain the names of people to be notified if a problem arises with an automated instrument.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<RET\> HOME

Install Started for MD 1.0 :

Apr 26, 2004@14:54:17

Build Distribution Date: Mar 17, 2004

Installing Routines:

Apr 26, 2004@14:54:18

Installing Data Dictionaries:

Apr 26, 2004@14:54:18

Installing Data:

Apr 26, 2004@14:54:18

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing MAIL GROUP

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Located in the MCAR (MEDICINE/CARDIOLOGY) namespace.

Located in the MCAR (MEDICINE/CARDIOLOGY) namespace.

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Apr 26, 2004@14:54:19

Running Post-Install Routine: ^MDPOST

MDPOST-Setting compatible client versions...

MD 1.0

───────────────────────────────────────────────────────────────────────

MDPOST-Applying latest set of valid file types...

MDPOST-Setting CP web link...

MDPOST-Validating Mail Group 'MD DEVICE ERRORS' membership...

There are no local users in the mail group.

Adding 'SMITH,CHARLENE'...

Updating Routine file...

Updating KIDS files...

MD 1.0 Installed.

Apr 26, 2004@14:54:20

Install Message sent \#47598

───────────────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └─────────────────────────────────────────────────────────┘

Install Completed

## Post Installation Tasks on the M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Obtain the following patches from the National Patch Module and install.

> MD\*1\*1

> MD\*1\*2

> MD\*1\*10

> There maybe additional released patches that have been released since the date of this documentation. Please check the National Patch Module for the possibility of additional patches.

2.  Verify that the following globals are journaled and place them in the UCI translation table for each CPU: ^MDD and ^MDS.
3.  Verify that the file security is correct for the following files:

> DD RD WR DEL LAY AUD

> NUMBER NAME GLOBAL NAME ACC ACC ACC ACC ACC ACC

> 702 CP TRANSACTION ^MDD(702, @ @ @

> 702.01 CP DEFINITION ^MDS(702.01, @ \# \# \#

> 702.09 CP INSTRUMENT ^MDS(702.09, @ \# \# \# @

> 703.1 CP RESULT REPORT ^MDD(703.1, @ @ @ @ @

4.  IMPORTANT: If the site is currently running medical device interfaces via the Medicine package and wish to continue this method until they decide to implement CP, the CP Instrument file, (#702.09) field, Processing Code needs to be set to Medicine while the HL7 MCAR INST link is still stopped. See Example:
    1.  D P^DI

> VA FileMan 22.0

2.  Select OPTION: ENTER OR EDIT FILE ENTRIES
3.  INPUT TO WHAT FILE: CP INSTRUMENT//
4.  EDIT WHICH FIELD: ALL// .12 PROCESSING CODE
5.  THEN EDIT FIELD:
6.  Select CP INSTRUMENT NAME: Muse

> 1 Muse EKG

> 2 Muse EKG(Bi-Directional)

> 3 Muse Exercise

> 4 Muse Holter

> 5 Muse Pacemaker EKG

7.  CHOOSE 1-5: 1 Muse EKG
8.  PROCESSING CODE: CP V1.0// Med Medicine
5.  Restart the HL7 logical link MCAR INST after installing Clinical Procedures. Refer to the Configuration Instructions section of the Setting Up HL7 Parameters chapter of the Clinical Procedures Implementation Guide for instructions on restarting MCAR INST.
6.  If the site wishes to automatically populate the CP DEFINITION file, the INIT^MDPOST routine can be run to perform this step. It will install 200+ procedures into the file if they do not exist. No procedure will be overwritten that currently exists in the file. Refer to the Clinical Procedures Implementation Guide for a listing of procedures contained in the MDPOST routine.
7.  The option \[MD GUI MANAGER\] shall be assigned to the Clinical Application Coordinator (CAC), CP package coordinator, and Information Resource Management Service (IRMS) staff so they can enter CP Definitions, Instruments, and System Parameters in the CP Manager application. If this option is not assigned, the user will get an error when trying to access this option.
8.  Prior to implementing Clinical Procedures, IRM shall assign the option \[MD GUI USER\] to the clinical staff (i.e., physicians, nurses, and technicians) who perform and/or interpret studies on medical devices that send data to Clinical Procedures. This allows the clinical staff to complete studies through the CP User application. If this option is not assigned, the user will get an error when trying to access this option.
9.  The user needs to have the MAG WINDOWS option to capture images. The MAGCAP CP key is required to restrict users to capture images to a Clinical Procedures study through Imaging capture.

> .

If the site chooses to only INSTALL Clinical Procedures and not implement, you have completed the install process. The Client side of Clinical Procedures is only required if you are planning to implement the new application.

## Clinical Procedures V. 1.0 Installation (Client)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Procedure application utilizes the RPC Broker connection to the VistA server for operation. Before installing the application, insure that the workstation has connectivity to the required server via the RPC Broker. For help in setting up the RPC Broker on the workstation refer to the Kernel RPC Broker documentation.

### > Note:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- It is recommended that if you have a previous version of CP on your machine, you remove it using Control Panel before you install the new version.
- The CP Gateway must be installed separately from CP User and CP Manager. Install CP User and CP Manager first, then install the CP Gateway on a workstation in a secure area.
- To modify an installation, click on the executable file icon (MD1_0.exe) and select Modify. Do not use Add/Remove Programs under Control Panel to modify an installation. An error will occur if this is done. Use Add/Remove Programs only to add or remove a program.

### Installing the Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run MD1_0.exe from the sharable directory where you placed it and follow the installation steps that will be presented to the user.

> ![](clinical-procedures-version-1-installation-guide/002.png)

> Fig. 1

> 1\. Your first screen is a welcome screen (Fig. 1). Press the Next button to begin the installation process of Clinical Procedures.

> ![](clinical-procedures-version-1-installation-guide/003.png)

> Fig. 2

> 2\. Select the location (i.e., Destination Folder in Fig. 2) on the client where the application is to be installed. By default the installation will be placed on the

> C:\Program Files\VistA\Clinical Procedures

> directory of the client you are installing this application on.

> It is recommended that you use this default as it is in compliance with the GUI SACC guidelines for the location of GUI application installations. The application will operate correctly if placed elsewhere on the client workstation but this is not recommended. Use Browse button to select another destination folder or directory.

> ![](clinical-procedures-version-1-installation-guide/004.png)

> Fig. 3

> 3\. Select of the type of setup that you wish to perform (Fig. 3). Each is described below.

> CP for Clinicians installation includes:

> CP User application and CP User help files

> CP for Coordinators installation includes:

> CP User application and CP User help files

> CP Manager application and CP Manager help files

> CP Gateway installation includes:

> CP Gateway application and CP Gateway help files

> All three setup types install the same way. The same process is followed, and the same screens and defaults appear.

> CP Gateway must be installed separately from CP User and CP Manager. CP Gateway must be installed on a workstation in a secure area, as it must remain active at all times for polling purposes. Only one workstation should be running this CP Gateway.

> CP Manager is used to configure the application parameters and should not be installed in areas where configuration of the package will not be occurring. This window defaults to CP for Clinicians setup option, you must select CP for Coordinators setup if you want both CP User and CP Manager installed on your workstation.

> ![](clinical-procedures-version-1-installation-guide/005.png)

> Fig. 4

> 4\. Clinical Procedures does support the Shared Broker. If you answer "Yes" to this screen, no command line switch is added to the Shortcut executable(s) that will be installed. If you answer "No" to this screen, the command line switch "/NonSharedBroker" will be included with the install and will be added at the end of the Target field that is within the "Shortcut" tab under "Properties" of the Shortcut executable(s). This includes both the Shortcut executables on the desktop and the ones under the Program folder of the Start menu.

> NOTE: The Shared Broker came with patch XWB1_1P29. In order to check if you have the Shared Broker, browse to the standard installation path, C:\Program Files\vista\Common Files and locate the files below. If you cannot locate this directory, you do not have the Shared Broker on your system.

> “RPCSharedBrokerSessionMgr.exe” and

> “RPCSharedBrokerSessionMgr1.exe.”

> If you have these files on your system, then you have the Shared Broker.

> If you discovered, after installing Clinical Procedures, that you are not running the Shared Broker, please re-install the CP executables and click “No” at this screen (Fig. 4) to add the command line switch “/NonSharedBroker” and avoid excessive logon dialog screens for multiple GUI applications.

> ![](clinical-procedures-version-1-installation-guide/006.png)

> Fig. 5

> 5\. Enter any optional command line switches for Clinical Procedures. This screen, will add the following command line switches "/server=BROKERSERVER /port=9200" to the Target field as well. Depending on what you answered at the Shared RPC Broker Support screen (Step 4), you will see either "/NonSharedBroker /server=BROKERSERVER /port=9200" or "/server=BROKERSERVER /port=9200" as the default Command Line Switch Parameters. You can edit and change "BROKERSERVER" and 9200 to the appropriate IP server name and port number for your site. You can also add other optional command line switches in this screen. If your site prefers to use the server list in the Host file, you can simply remove "/server=BROKERSERVER /port=9200" and go to the next install shield screen. Please refer to Appendix A – CP Application Startup Options and Command Line Switches in the Clinical Procedures Implementation Guide for a list of usable command line switches.

> Note: If you mis-typed, or entered the server name or port number in error, please re-install the Clinical Procedures package to correct the command line switch.

> ![](clinical-procedures-version-1-installation-guide/007.png)

> Fig. 6

> 6\. The installation of Clinical Procedures will add icons to both the Start Menu and the Users desktop. By default a program folder of Clinical Procedures will be created and the icons installed there as shown in (Fig. 6). The Shortcuts of the CP applications within the Start Menu and User desktop will contain the command line switches that were indicated in Figures 4, 5 (Steps 4, 5).

> ![](clinical-procedures-version-1-installation-guide/008.png)

> Fig. 7

> 7\. Check the settings listed on this screen before continuing (Fig. 7).

> ![](clinical-procedures-version-1-installation-guide/009.png)

> Fig. 8

> 8\. Once all steps are completed the installation will begin and show the progress as it installs (Fig. 8). If the installation files are located on the client PC, the install screen should complete in less than one minute. Server and network connectivity for installations over the network may cause the installation time to increase.

> ![](clinical-procedures-version-1-installation-guide/010.png)

> Fig. 9

> 9\. Upon completion of the installation this screen will be presented to the user and the installation can be finalized by pressing the Finish button (Fig. 9).

## Customizing the Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The client installation by default installs and builds the icons and program folder items with -command line switches /server, /port, and /nonsharedbroker. Clinical Procedures utilizes the ServerList utility of the RPC Broker for selecting a server to connect to if it is configured on the client workstation. Instructions for configuration and utilization of the ServerList utility can be found in the RPC Broker documentation located on the VDL. If the ServerList utility has not been configured on the client, the applications by default will attempt to connect to the server identified in the users HOSTS file as BROKERSERVER on Listener Port 9200. Refer to Appendix A – CP Application Startup Options and Command Line Switches in the Clinical Procedures Implementation Guide for a list of usable command line switches.

## Server Based Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Procedures package may be installed on a server share and accessed via shortcuts on the user’s desktop to minimize the impact of patching and installation. To do this simply perform a complete install of the application on a workstation and verify that the installation is working. Next, copy all files and sub directories from the target directory (default C:\Program Files\Vista\Clinical Procedures\\’) to the server share. On each individual workstation all that needs to be done is the creation of a shortcut pointing to the CP User.exe and/or CP Manager.exe applications on the server. To create a shortcut, right-click on the application and choose the option Create Shortcut, then move the shortcut onto the desktop of each workstation. These shortcuts can be customized as discussed in the Customizing the Client Installation section. This allows for updates to occur on the single copy of the application on the server and does not require IRM going to each individual workstation to apply updates. As the VA moves towards utilizing Microsoft SMS, Clinical Procedures will be updated to support this method of client installation.

> **NOTE:** Install the CP Gateway on a workstation in a secure area, as it must remain active at all times for polling purposes. Only one workstation should be running this CP Gateway.

> List of all files that need to be copied to the server share for server based installations:

> C:\Program Files\VistA\Clinical Procedures\CP User.exe

> C:\Program Files\VistA\Clinical Procedures\CP Manager.exe

> C:\Program Files\VistA\Clinical Procedures\Help\CP User.hlp

> C:\Program Files\VistA\Clinical Procedures\Help\CP User.cnt

> C:\Program Files\VistA\Clinical Procedures\Help\CP Manager.hlp

> C:\Program Files\VistA\Clinical Procedures\Help\CP Manager.cnt

> C:\Program Files\VistA\Clinical Procedures\Help\Roboex32.dll