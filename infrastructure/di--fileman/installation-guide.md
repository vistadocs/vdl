---
title: FM 22.2 Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: Installation, Back-Out, and Rollback Guide
app_code: DI
app_name: FileMan
section: INF
app_status: active
pkg_ns: DI
patch_ver: 22.2
patch_id: DI*22.2
group_key: "DI:DI:22.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - span
  - fileman
  - back
  - installation
  - class
  - install
  - mark
  - rollback
page_count: 0
word_count: 3359
section_count: 31
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=5"
---

---
title: |
  VA FileMan 22.2

  Installation, Back-Out, and Rollback Guide
---

![](fm-22-2-installation-back-out-and-rollback-guide/001.png)

August 2016

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

![](fm-22-2-installation-back-out-and-rollback-guide/002.png) NOTE: The revision history cycle begins once changes or enhancements are requested after the Installation, Back-Out, and Rollback Guide has been baselined.

<table>
<caption><p><span id="_Toc457395538" class="anchor"></span>Table 1: VA FileMan 22.2 Documentation</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/03/2016</td>
<td>1.0</td>
<td><p>Initial release of VA FileMan 22.2 Installation, Back-Out, and Rollback Guide.</p>
<p>Based on the ProPath Installation, Back-Out, and Rollback Guide template; released February 2016; Version 2.1.</p></td>
<td>VA FileMan 22.2 Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc457395538" class="anchor"></span>Table 1: VA FileMan 22.2 Documentation

Table of Contents

List of Figures

List of Tables

[Table 1: VA FileMan 22.2 Documentation [3](#_Toc457395538)](#_Toc457395538)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [MUMPS OPERATING SYSTEM File Considerations](#mumps-operating-system-file-considerations)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Back Up System](#back-up-system)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
    - [Software](#software)
    - [Documentation](#documentation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
- [Installation Procedure](#installation-procedure)
  - [Log onto the System](#log-onto-the-system)
  - [Check the Current VA FileMan Version](#check-the-current-va-fileman-version)
  - [Production Environment: Shut Down System](#production-environment-shut-down-system)
  - [Production Environment: Restart System](#production-environment-restart-system)
  - [Production Environment: Inhibit Logons for Each Volume Set](#production-environment-inhibit-logons-for-each-volume-set)
  - [Environment Check](#environment-check)
  - [Production Environment: Load the VA FileMan 22.2 Distribution](#production-environment-load-the-va-fileman-222-distribution)
  - [Install the VA FileMan 22.2 Package](#install-the-va-fileman-222-package)
  - [Post-Install TaskMan Procedures](#post-install-taskman-procedures)
  - [Production Environment: Enable Logons](#production-environment-enable-logons)
- [Implementation Procedure](#implementation-procedure)
  - [Database Tuning](#database-tuning)
  - [Verify Installation](#verify-installation)
- [Back-Out Plan](#back-out-plan)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure)
- [Rollback Plan](#rollback-plan)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure)
This guide provides instructions for installing Department of Veterans Affairs (VA) FileMan 22.2. VA FileMan is designed to be used either with the Kernel or as a standalone application; however, these installation instructions are provided only for sites running Kernel 8.0. Since Kernel is dependent on VA FileMan 22.0, that version of VA FileMan is already installed on your system.
This guide is written specifically for the Caché Operating System (OS). It does not contain OS-specific instructions for other OSs, such as routing mapping and manually moving %routines into the Manager account.
![](fm-22-2-installation-back-out-and-rollback-guide/003.png) REF: For identifying other OSs to VA FileMan and Kernel, see Section <u>1.1</u>.
This installation is significantly different from previous versions. You no longer must manually move the new VA FileMan routines into the account. The routines are present in the Kernel Installation & Distribution System (KIDS) build and are loaded as part of the install. DINIT is run *non*-interactively during the KIDS pre-install to update the VA FileMan files.
After this installation, the current version of the VA FileMan files will be installed and updated with data as appropriate.
![](fm-22-2-installation-back-out-and-rollback-guide/004.png) CAUTION: Do *not* run DINIT to update the VA FileMan files after the install is complete. Running DINIT from the Command line at any time will cause data corruption.

## MUMPS OPERATING SYSTEM File Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Install, Back-Out, and Rollback Guide assumes an install on Caché. You are not asked to identify your OS during the install.

VA FileMan 22.2 populates the MUMPS OPERATING SYSTEM file (#.7) with values for the following operating systems:

- CACHE/OpenM
- DSM for OpenVMS
- DTM-PC
- GT.M(UNIX)
- GT.M(VAX)
- MSM
- OTHER—This placeholder is for a user defined OS

In order to notify VA FileMan that you are using an OS other than Cache after the install completes enter the following command to identify your OS:

\>D OS^DINIT

In order to complete the identification to Kernel that you are running an OS other than Cache, run the appropriate routine from the following list:

ZOSFGTM            GTM on VMS

ZOSFGUX            GTM on Unix

ZOSFONT            Cache

ZOSFVXD            DSM on VMS

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back Up System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back up your system as a safeguard *before* the installation. In order to back out the VA FileMan 22.2 installation, restore your back up (see the “<u>Back-Out Plan</u>” section).

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan 22.2 requires pre-existing Kernel 8.0 software.

Patches DI\*22.2\*1 *and* HL7\*1.6\*167 resolve a known VA FileMan (FM) 22.2 issue, SDM I9259370. User cannot select HL7 messages directly from the list in the HL View Transmission Log option. For ease of installation, sites may delay installing FM 22.2 until release of patches DI\*22.2\*1 and HL7\*1.6\*167; both patches will be released shortly. Although the two patches can be installed while users are on the system, installing both patches right after installing FM 22.2, before allowing users back on the system, is more efficient and will eliminate any possible errors.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software being released as a Kernel Installation and Distribution System (KIDS) file and documentation describing the new functionality introduced by this patch is available.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software can be downloaded from the Product Support (PS) Anonymous Directories via Secure File Transfer Protocol (SFTP).

Download the VA_FILEMAN_22_2.KID file from the appropriate server to a directory on your system.

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation can be downloaded from the Product Support (PS) Anonymous Directories via Secure File Transfer Protocol (SFTP).

Documentation can also be found on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=5>

| File Name     | FTP Mode | Description                                                |
|---------------|----------|------------------------------------------------------------|
| fm22_2um1.pdf | Binary   | VA FileMan 22.2 User Manual                                |
| fm22_2um2.pdf | Binary   | VA FileMan 22.2 Advanced User Manual                       |
| fm22_2dg.pdf  | Binary   | VA FileMan 22.2 Developer’s Guide                          |
| fm22_2ig.pdf  | Binary   | VA FileMan 22.2 Installation, Back-Out, and Rollback Guide |
| fm22_2tm.pdf  | Binary   | VA FileMan 22.2 Technical Manual                           |
| fm22_2rn.pdf  | Binary   | VA FileMan 22.2 Release Notes                              |

VSM DocumentationVSM Documentation

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for VA FileMan 22.2.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no cron scripts for the VA FileMan 22.2.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only those with system management knowledge and access should install VA FileMan 22.2.

![](fm-22-2-installation-back-out-and-rollback-guide/005.png) REF: For instructions on performing OS-level tasks, see your OS system management documentation.

The installer needs to know how to do the following:

- Obtain Veterans Health Information Systems and Technology Architecture (VistA) software from FORUM and Secure File Transfer Protocol (SFTP) download sites (i.e., Product Support Anonymous Directories).
- Run a Kernel Installation and Distribution System (KIDS) installation.
- Logging onto the system and getting to the M prompt (Programmer Mode).
- Execute commands in Programmer mode when given VistA Programmer Access.
- Running system status reports.
- Terminating processes.
- Accessing host files (i.e., KIDS build file).
- Inhibiting Logons.
- Stopping TaskMan.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Log onto the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log onto the Production account.

## Check the Current VA FileMan Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check that current version in the PACKAGE FILE (#9.4) is set to 22.0.

<span id="_Toc458001745" class="anchor"></span>Figure 1: Check the Current VA FileMan Version

\><span class="mark">D P^DI</span>

VA FileMan 22.2

Select OPTION: <span class="mark">1 \<Enter\></span> ENTER OR EDIT FILE ENTRIES

Input to what File: DEVICE// <span class="mark">PACKAGE</span>

1 PACKAGE (294 entries)

2 PACKAGE INTERFACE (128 entries)

3 PACKAGE SIZE (5182 entries)

4 PACKAGE TYPE (529 entries)

CHOOSE 1-4: <span class="mark">1 \<Enter\></span> PACKAGE (294 entries)

EDIT WHICH FIELD: ALL// <span class="mark">CURRENT VERSION</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select PACKAGE NAME: <span class="mark">VA FILEMAN \<Enter\></span> DI

CURRENT VERSION: 22.2// <span class="mark">22.0</span>

Select PACKAGE NAME:

## Production Environment: Shut Down System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Production, shut down Caché/system using your regular shutdown procedures.

## Production Environment: Restart System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Production, restart Caché/system using your regular startup procedures.

- Do not restart TaskMan or any background filers.
- Do not allow any users back on the system.

## Production Environment: Inhibit Logons for Each Volume Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the operating system (OS) command to prevent logons. Using the OS command does not cause a problem and allows you to work within the menu system as needed during the installation. Caché/OpenM sites can stop the LAT and TELNET services.

Use VA FileMan to edit the VOLUME SET file (#14.5).

<span id="_Toc458001746" class="anchor"></span>Figure 2: Inhibit Logons for Each Volume Set

\><span class="mark">D Q^DI</span>

VA FileMan 22.0

Select OPTION: <span class="mark">ENTER OR EDIT FILE ENTRIES</span>

INPUT TO WHAT FILE: VOLUME SET// <span class="mark">14.5</span>

EDIT WHICH FIELD: ALL// <span class="mark">INHIBIT LOGONS ?</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select VOLUME SET: *<span class="mark">\<Production Account\></span>*

INHIBIT LOGONS?: NO// <span class="mark">YES</span>

## Environment Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA FileMan 22.2 distribution includes an Environment Check routine (DI222ENV). It is run automatically during the Install. Also, you are asked if you want to run it during the Load of the distribution. Answer “YES.”

The Environment Check examines the status of your system to verify that TaskMan is stopped and that Logons are inhibited (see steps above). If the install is stopped because your system is not in the proper state, stop TaskMan and inhibit Logons. Then proceed with the install.

The Environment Check also validates the integrity of File \#1 (the File of Files) on your system. If a zero node for an entry in File \#1 is missing, you are notified of the offending entry and the install is stopped. The problem *must* be resolved before proceeding with the install.

## Production Environment: Load the VA FileMan 22.2 Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You are now ready to Load the Kernel Installation and Distribution System (KIDS) build and Install VA FileMan 22.2.

1.  Use the ^XUP and Q^DI entry points to set your DUZ and set DUZ(0) to "@".
1.  To set DUZ when responding to the Access code prompt. Press Enter at the OPTION prompt.

\>D ^XUP

2.  To set DUZ(0)="@"

\>D Q^DI

1.  <u>IMPORTANT:</u> Invoke the ^XPDKRN menu and select the LOAD A DISTRIBUTION option. Enter the appropriate Host file name to load the VA FileMan 22.2 distribution file (FM22_0.KID).

<span id="_Toc458001747" class="anchor"></span>Figure 3: load the VA FileMan 22.2 distribution file

\><span class="mark">D ^XPDKRN</span>

KIDS 8.0

Select KIDS OPTION: <span class="mark">1 \<Enter\></span> LOAD A DISTRIBUTION

Enter a Host File: <span class="mark">/nfsftp/FLM22/sqakids/VA_FILEMAN_22_2.KID</span>

KIDS Distribution saved on Mar 18, 2016@16:57:48

Comment: VA FileMan 22.2 KIDS Build

This Distribution contains Transport Globals for the following Package(s):

   VA FILEMAN 22.2

Distribution OK!

Want to Continue with Load? YES// <span class="mark">\<Enter\></span>

Loading Distribution...

Build VA FILEMAN 22.2 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// <span class="mark">\<Enter\></span>

VA FILEMAN 22.2

Will first run the Environment Check Routine, DI222ENV

Use INSTALL NAME: VA FILEMAN 22.2 to install this Distribution.

## Install the VA FileMan 22.2 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Invoke the ^XPDKRN menu again and select the INSTALL PACKAGE(S) option. Select VA FILEMAN 22.2 as the package you want to install.

The VA FileMan 22.2 installation takes approximately 10 minutes.

<span id="_Toc458001748" class="anchor"></span>Figure 4: Sample installation dialogue

\><span class="mark">D ^XPDKRN</span>

KIDS 8.0

Select KIDS OPTION: <span class="mark">6 \<Enter\></span> INSTALL PACKAGE(S)

Select INSTALL NAME: <span class="mark">VA FILEMAN 22.2 \<Enter\></span> 2/18/16@11:51:17

=\> VA FileMan 22.2 KIDS build ;Created on Feb 18, 2016@11:34

This Distribution was loaded on Feb 18, 2016@11:51:17 with header of

VA FileMan 22.2 KIDS build ;Created on Feb 18, 2016@11:34

It consisted of the following Install(s):

VA FILEMAN 22.2

Checking Install for Package VA FILEMAN 22.2

Will first run the Environment Check Routine, DI222ENV

Install Questions for VA FILEMAN 22.2

Incoming Files:

.85 LANGUAGE (including data)

> **NOTE:** You already have the 'LANGUAGE' File.

I will OVERWRITE your data with mine.

.9 META DATA DICTIONARY

> **NOTE:** You already have the 'META DATA DICTIONARY' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// <span class="mark">\<Enter\></span>

Want KIDS to INHIBIT LOGONs during the install? NO// <span class="mark">\<Enter\></span>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// <span class="mark">\<Enter\></span>

Enter the Device you want to print the Install messages.

Enter a '^' to abort the install.

DEVICE: HOME// <span class="mark">\<Enter\></span> TELNET

Install Started for VA FILEMAN 22.2 :

Feb 18, 2016@11:51:32

Build Distribution Date: Feb 18, 2016

Installing Routines:

Feb 18, 2016@11:51:33

Running Pre-Install Routine: EN^DI222PRE

Initializing FileMan version 22.2...

......................................

Now loading DIALOG and LANGUAGE Files...........................................

................................................................................

................................................................................

................................................................................

.........................................

..........

The following files have been installed:

.11 INDEX

.2 DESTINATION

.31 KEY

.4 PRINT TEMPLATE

.401 SORT TEMPLATE

.402 INPUT TEMPLATE

.403 FORM

.404 BLOCK

.44 FOREIGN FORMAT

.46 IMPORT TEMPLATE

.5 FUNCTION

.6 DD AUDIT

.7 MUMPS OPERATING SYSTEM

.81 DATA TYPE

.83 COMPILED ROUTINE

.84 DIALOG

.85 LANGUAGE

.9 META DATA DICTIONARY

1 FILE

1.1 AUDIT

1.11 ARCHIVAL ACTIVITY

1.12 FILEGRAM HISTORY

1.13 FILEGRAM ERROR LOG

1.2 ALTERNATE EDITOR

1.521 SQLI_SCHEMA

1.52101 SQLI_KEY_WORD

1.5211 SQLI_DATA_TYPE

1.5212 SQLI_DOMAIN

1.5213 SQLI_KEY_FORMAT

1.5214 SQLI_OUTPUT_FORMAT

1.5215 SQLI_TABLE

1.5216 SQLI_TABLE_ELEMENT

1.5217 SQLI_COLUMN

1.5218 SQLI_PRIMARY_KEY

1.5219 SQLI_FOREIGN_KEY

1.52191 SQLI_ERROR_TEXT

1.52192 SQLI_ERROR_LOG

Re-indexing entries in the DIALOG file..........................

Compiling all forms ...

DICATT (#.001)

DIPTED (#.1001)

DIKC EDIT (#.1101)

DIKC EDIT UI (#.1102)

DIKK EDIT (#.3101)

DIBTED (#.40001)

DIETED (#.40101)

DIEDIT (#.40201)

DDGF BLOCK EDIT (#.40301)

DDGF PAGE ADD (#.40302)

DDGF PAGE EDIT (#.40303)

DDGF PAGE SELECT (#.40304)

DDGF FORM EDIT (#.40305)

DDGF HEADER BLOCK EDIT (#.40306)

DDGF FIELD ADD (#.40401)

DDGF FIELD CAPTION ONLY (#.40402)

DDGF FIELD DD (#.40403)

DDGF FIELD FORM ONLY (#.40404)

DDGF FIELD COMPUTED (#.40405)

DDGF BLOCK ADD (#.40406)

DDGF BLOCK DELETE (#.40407)

DDGF HEADER BLOCK SELECT (#.40408)

DDXP FF FORM1 (#.441)

DDMP SPECIFY IMPORT (#.461)

XUEDIT CHARACTERISTICS (#1)

XUEXISTING USER (#2)

.

.

.

INITIALIZATION COMPLETED IN 3 SECONDS.

Initialization of FileMan version 22.2 has been completed.

Installing Data Dictionaries:

Feb 18, 2016@11:51:36

Installing Data:

Feb 18, 2016@11:51:36

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY ....

Installing REMOTE PROCEDURE .............

Installing OPTION ................................

Feb 18, 2016@11:51:37

Running Post-Install Routine: POST^DI222POS

Saving Routine: DIDT, As: %DT

Saving Routine: DIDTC, As: %DTC

Saving Routine: DIRCR, As: %RCR

Routine: DIDT Loaded, Saved as %DT

Routine: DIDTC Loaded, Saved as %DTC

Routine: DIRCR Loaded, Saved as %RCR

DIDT ;SFISC/GFT-DATE/TIME UTILITY ;2014-12-26 12:32 PM

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

DIDTC ;SFISC/XAK-DATE/TIME OPERATIONS ;3JAN2011

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

DIRCR ;SFISC/GFT-DELETE THIS LINE AND SAVE AS '%RCR'\*\*\* ;13DEC2012

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

Updating Routine file...

Updating KIDS files...

VA FILEMAN 22.2 Installed.

Feb 18, 2016@11:51:38

Not a production UCI

NO Install Message sent

Call MENU rebuild

Starting Menu Rebuild: Feb 18, 2016@11:51:40

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

.

.

.

Building secondary menu trees....

Merging.... done.

Install Completed

## Post-Install TaskMan Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan should have started when you rebooted or restarted the system. If TaskMan is not running, start TaskMan.

\>D ^ZTMB

## Production Environment: Enable Logons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use VA FileMan to edit the Inhibit Logon field in the VOLUME SET file (#14.5) for each volume set. This allows TaskMan to start tasks.

<span id="_Toc458001749" class="anchor"></span>Figure 5: Enable Logons

\><span class="mark">D Q^DI</span>

VA FileMan 22.2

Select OPTION: <span class="mark">ENTER OR EDIT FILE ENTRIES</span>

INPUT TO WHAT FILE: <span class="mark">VOLUME SET</span>

EDIT WHICH FIELD: ALL// <span class="mark">INHIBIT LOGONS ?</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select VOLUME SET: *<span class="mark">\<Production Account\></span>*

INHIBIT LOGONS?: YES// <span class="mark">NO</span>\*\*\*\* You have now completed the installation of VA FileMan. \*\*\*\*

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special database tuning requirements for VA FileMan 22.2.

## Verify Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the installation. Use KIDS option Install File Print, under the Utilities menu, and enter VA FILEMAN 22.2.  Confirm that the STATUS field is “Install Complete”.

# Back-Out Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

The method of backing out the VA FileMan (FM) 22.2 patch is to restore from the backup that was taken in the “<u>Back Up System</u>” section. Due to the fact that FM 22.2 is a change to the system infrastructure, this is the only way to put the system back to the pre FM 22.2 state.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release a back-out would include removal of data, files and routines. In the case of future patches and releases the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production VistA end-users and impact on Wide Area Network.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for FM 22.2.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FM 22.2 User Acceptance Testing (UAT) is performed during VistA patch testing at test sites.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FM 22.2 back-out criteria follow existing VistA back-out procedures.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FM 22.2 back-out risks are the same risks established with existing VistA back-out procedures.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with VHA and EPMO representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out FM 22.2, do the following:

- Restore backup to reset the system to the pre FM 22.2 state.
- You will lose everything that has happened since the install.

![](fm-22-2-installation-back-out-and-rollback-guide/006.png) CAUTION: Once the system has been restarted, the backout procedure is no longer possible.

# Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data.

VA FileMan (FM) 22.2 does *not* export any data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. FM 22.2 does not export any data.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. FM 22.2 does not export any data.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. FM 22.2 does not export any data.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. Enterprise Program Management Office (EPMO) should be informed immediately via a MailMan message sent to:

REDACTED

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. FM 22.2 does not export any data.