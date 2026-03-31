---
title: Functional Independence Measurement (FIM) Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: FIM
app_name: Functional Independence Measurement
section: CLI
app_status: active
pkg_ns: FIM
patch_ver: 1
patch_id: FIM*1
group_key: "FIM:FIM:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this guide is to provide instructions for installing the Functional Independence Measurement (FIM) Version 1.0.
audience: 
keywords: 
  - table
  - contents
  - installation
  - rmim
  - software
  - functional
  - independence
  - measurement
  - server
  - mail
page_count: 0
word_count: 2955
section_count: 17
table_count: 18
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2003
revision_count: 5
revision_newest: 5/02/03
revision_oldest: 2/26/2003
docx_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=134"
---

---
title: |
  ![](functional-independence-measurement-fim-version-1-installation-guide/001.png)

  Functional Independence Measurement (FIM) Installation Guide

  ![](functional-independence-measurement-fim-version-1-installation-guide/002.png)

  Version 1.0

  May 2003

  Department of Veterans Affairs

  VistA System Design and Development
---

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Related Manuals](#related-manuals)
  - [Online Help](#online-help)
- [Orientation](#orientation)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [VistA Intranet](#vista-intranet)
- [Pre-Installation Information](#pre-installation-information)
  - [Test Sites](#test-sites)
  - [Hardware and Operating Systems](#hardware-and-operating-systems)
    - [M Server Requirements](#m-server-requirements)
    - [Client Workstation Requirements](#client-workstation-requirements)
    - [Network communications software](#network-communications-software)
  - [Software Installation Time](#software-installation-time)
  - [Name Space](#name-space)
  - [New Globals](#new-globals)
  - [VistA Software Requirements](#vista-software-requirements)
  - [Routine List](#routine-list)
  - [Skills Required to Perform the Installation](#skills-required-to-perform-the-installation)
  - [Main Installation Procedures](#main-installation-procedures)
    - [Instructions for Network Drive Installation](#instructions-for-network-drive-installation)
    - [Instructions for M Server Installation](#instructions-for-m-server-installation)
  - [Mail Group](#mail-group)
- [Installation Instructions](#installation-instructions)
- [Post Installation](#post-installation)
- [Options](#options)
- [Key Assignment](#key-assignment)
- [Mail Groups](#mail-groups)
- [Protocols](#protocols)
- [Exported RPCs](#exported-rpcs)
- [HL7 Application Parameters](#hl7-application-parameters)
- [HL7 Logical Links](#hl7-logical-links)
- [Bulletins](#bulletins)
|           |                                                 |
|-----------|-------------------------------------------------|
| Date      | Description                                     |
| 2/26/2003 | Updates from <span class="mark">REDACTED</span> |
| 3/31/2003 | Updates from <span class="mark">REDACTED</span> |
| 4/14/2003 | Updates from <span class="mark">REDACTED</span> |
| 4/22/2003 | Updates from <span class="mark">REDACTED</span> |
| 5/02/03   | Updates from <span class="mark">REDACTED</span> |
TABLE OF CONTENTS

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Functional Independence Measurement (FIM) Version 1.0.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Information Resource Management (IRM) staff is required for installing and supporting VistA FIM.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Functional Independence Measurement (FIM) Technical Manual and Security Guide, V.1.0Functional Independence Measurement (FIM) User Manual, V.1.0*

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions, procedures, and other information are available from the FIM online help file. You may access the help file by clicking on Help\|Contents from the menu bar or by pressing the F1 key while you have any FIM screen dialog open.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-installation Information section provides information needed beforehand to install RMIM1_0.KID.

Installation Instructions section contains instructions and examples of RMIM1_0.KID installation process.

Implementation Instructions provides directions for implementing FIM software.

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user’s response in this manual is in bold type, but does not appear on the screen as bold. The bold part of the entry is the letter or letters that you must type so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, you will see the symbol \<RET\>. This symbol is not shown but is implied if there is bold input.

Within the roll and scroll part of the system, help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. You can find this information enclosed in brackets, for example, \[type ward name here\]*,* and will not appear on the screen.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|        |                                                                                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------|
| Symbol | Description                                                                                                       |
|        | Used to inform the reader of general information including references to additional reading material. See example |
|        | Used to caution the reader to take special notice of critical information.                                        |

Table 1: Documentation Symbol Descriptions

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA FIM software files and Installation and Implementation Guide (i.e., RMIM1_0IG.PDF) are available on the following Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directories.

|                |                                    |                                    |
|----------------|------------------------------------|------------------------------------|
| OIFO           | FTP Address                        | Directory                          |
|  Albany        | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Hines          | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Salt Lake City | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

VistA FIM software and documentation are distributed as the following set of files:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
<th>File Size</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RMIM1_0.KID</td>
<td>KIDS build</td>
<td>ASCII</td>
<td>219,648 bytes</td>
</tr>
<tr class="even">
<td>RMIM1_0.ZIP</td>
<td>FIM Executable</td>
<td>BINARY</td>
<td>1,121,792 bytes</td>
</tr>
<tr class="odd">
<td>RMIM1_0IG.pdf<br />
RMIM1_0IG.doc</td>
<td>Installation Guide</td>
<td>BINARY</td>
<td><p>1,350 bytes</p>
<p>28,5700 bytes</p></td>
</tr>
<tr class="even">
<td>RMIM1_0TM.pdf<br />
RMIM1_0TM.doc</td>
<td>Technical Manual and Security Guide</td>
<td>BINARY</td>
<td><p>2,460 bytes</p>
<p>17,530 bytes</p></td>
</tr>
<tr class="odd">
<td>RMIM1_0UM.pdf<br />
RMIM1_0UM.doc</td>
<td>Users Manual</td>
<td>BINARY</td>
<td>19,350 bytes<br />
29,130 bytes</td>
</tr>
</tbody>
</table>

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online Documentation for this product is available on the intranet at the following address: [www.va.gov/vdl](http://www.va.gov/vdl). This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the Clinical Case Registries link and it will take you to the FIM documentation.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information contains recommendations and requirements for the pre-installation of the FIM software.

The Functional Independence Measurement is run on both the client and VistA. The installation is a *two-part* process involving the client workstation, and VistA.

The Functional Independence Measurement comprises the following:

- FIM.exe
- M routines
- VA FileMan files
- Print, Sort, Edit templates
- Options
- Keys
- RPC Broker Calls
- Mailman Groups
- TIU Document Definitions (Titles)
- HL7 logical link
- HL7 APPLICATION PARAMETERs
- PROTOCOLs

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM software was tested at the following sites:

| Test Sites          | Alpha | Beta |
|---------------------|-------|------|
| Augusta, GA         |       | X    |
| Bay Pines, FL       | X     | X    |
| Birmingham, AL      |       | X    |
| Erie, PA            |       | X    |
| Memphis, TN         | X     | X    |
| Milwaukee, WI       | X     | X    |
| Mountain Home, TN   | X     | X    |
| Pittsburgh, PA      |       | X    |
| Seattle, WA         | X     | X    |
| VISN 2, (Syracuse)  | X     | X    |
| West LA, CA         |       | X    |
| West Palm Beach, FL | X     | X    |

## Hardware and Operating Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of the Functional Independence Measurement, certain environmental requirements for both the M server and the client workstation must be satisfied. These requirements are described below.

### M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your M server in order to install and use the Functional Independence Measurement:

One of the following operating systems:

- Digital Standard M (DSM) V6.3-031 for OpenVMS AXP or greater
- InterSystems OpenM for NT version 7
- Micronetics Standard M (MSM) for Windows NT, V. 4.3 or greater

Network communications software:

- Your server needs to have TCP/IP running
- Your server needs to have Broker Listener running

### Client Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum hardware and software tools are required on your client workstation in order to install and use the Functional Independence Measurement:

80x86-based client workstation

One of the following 32-bit operating systems:

- Microsoft Windows 95
- Microsoft Windows NT Workstation V. 3.51 or greater

|     |                                                                                                                                                                                              |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | The VA has made the decision to go to a 32-bit Microsoft Windows environment. Therefore, the Functional Independence Measurement will not operate on Windows 3.1 or Windows 3.1 with WIN32S. |

- Win 2K

### Network communications software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measurement requires networked client workstations running Microsoft’s native TCP/IP stack. (*For more information on RPC Broker communications requirements see RPC Broker V. 1.1 Installation Guide page 7*).

RPC Broker V. 1.1 Listener running on the M server.

## Software Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of this software will not affect users on the system; therefore, there is no need for log on to be disabled. Installation will take less than 10 minutes.

## Name Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM software name space is RMIM.

## New Globals 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM 783 (Functional Independence Measurement Record file) and RMIM 783.9 (Functional Independence Measurement Parameter file) are the new globals supplied with this package.

Note; Be sure to place globals in the appropriate translation table.

It is suggested that journaling be enabled. The global access privileges are as follows:

System = RWP World = RW Group = RW UCI = RWP

## V*ist*A Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before FIM can be installed, the following software applications and patches must be installed and *fully* patched in your accounts.

| Application Name | Minimum Version |
|------------------|-----------------|
| Kernel           | V. 8            |
| Kernel Toolkit   | V. 7.3          |
| VA FileMan       | V. 22           |
| RPC Broker       | V. 1.1          |
| TIU              | V.1.0           |
| OERR             | V.3.0           |
| HL7              | V.1.6           |
| MailMan          | V.8             |

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains the routines included in RMIM Version 1.0

|         |                 |
|---------|-----------------|
| Routine | Checksum Values |
| RMIMHL  | 5598302         |
| RMIMRP  | 7242673         |
| RMIMU   | 3354346         |
| RMIMU1  | 2235473         |
| RMIMV   | 8374421         |

## Skills Required to Perform the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions for performing the needed functions are provided in the vendor-supplied operating system manuals as well as VistA publications.

!DSM for Open VMS sites should refer to the most recent Computer Operations Management and Procedures for AXP Systems (COMPAS) Manual.

!OpenM sites should refer to the “Configuring OpenM” chapter in the VistA -NT Conversion Checklist.

!MSM sites should refer to the most recent 486 Cookbook and MSM System Managers Guide.

You need to know how to do the following:

- Create directories on the host file system

\[client workstation only\]

- Create directories on a network server
- Copy files using commands of the host file system

\[client workstation, network server and the M server\]

- Load routines from: diskettes, tapes, and/or host files

\[both the client workstation and the M server\]

## Main Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Functional Independence Measurement is a *two-part* process involving both your client workstation and VistA. Each part of the installation consists of a few basic steps that are described below.

|     |                                                                                                                                                |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------|
|     | We strongly recommend that you install the Functional Independence Measurement on a network drive and distribute shortcuts to client desktops. |

### Instructions for Network Drive Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Start windows (required)

Start Windows if it is not already running on the end-user client workstation. Before beginning the installation, however, we recommend you shut down all other Windows-based applications running on the workstation.

2\. To install the Functional Independence Measurement:

1.  Create a directory on a network drive. Example: H:\FIM, where H is a network drive.
2.  Copy the WinZip files you received with this manual into the directory you just created.
3.  There are three was to make the FIM.EXE available to users:
1.  If site chooses to pass parameters within the Tools menu of CPRS, then Patient Selection will be controlled by CPRS and CPRS only. A set-up example for FIM.EXE will run in this method, please see below:

Select GUI Parameters Option: GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[WEST-PALM.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 4 System WEST-PALM.MED.VA.GOV

------- Setting CPRS GUI Tools Menu for System: WEST-PALM.MED.VA.GOV -------

Select Sequence: 17

Sequence: 17// 17

Name=Command: &FIM=”H:\FIM.exe” s=%SRV p=%PORT d=%DFN

2.  If site chooses to hang the software within the Tools menu of CPRS without passing parameters, then Patient Selection will be controlled by FIM. FIM will run as a stand alone. A set-up example for FIM.EXE will run in this method, please see below:

Select GUI Parameters Option: GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[WEST-PALM.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 4 System WEST-PALM.MED.VA.GOV

------- Setting CPRS GUI Tools Menu for System: WEST-PALM.MED.VA.GOV -------

Select Sequence: 17

Sequence: 17// 17

Name=Command: &FIM=”H:\FIM.exe”

3.  If site chooses to initiate FIM through other means (i.e. desktop shortcut), then Patient Selection will be controlled by FIM. FIM will run as a stand alone.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><p>If site chooses to launch FIM from CPRS Tools Menu using parameter passing (s=%SRV p=%PORT d=%DFN):</p>
<p>1.Patient Selection will be controlled by CPRS.</p>
<p>2.No Patient Selection will be allowed in FIM.</p>
<p>3.If FIM has an active patient record open, and CPRS changes patient, user will be informed that all current input data will be ignored.</p>
<p>4.FIM will shut down.</p></td>
</tr>
</tbody>
</table>

4.  Run ServerList on each client to ensure a proper connection to an M server.

### Instructions for M Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the WPB Functional Independence Measurement package was created using Kernel V.8.0 and VA FileMan V. 22.0 and requires the following external software:

> Package Name Minimum Required Version

> FUNCTIONAL INDEPENDENCE 1.0

## Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM Coordinators Mail Group RMIM FSOD is used for communication between users of the FIM template and the Coordinators. When a record that goes to FSOD gets created or edited, the FIM template will send a message to this group. Please contact the Rehab Medicine service to determine the appropriate individual as the coordinator of this mail group for your site.

The RMIM FSOD TRANSMISSION Mail Group is used for the transmission of FIM data to the FSOD database in Austin. No members need to be in this group. The mail group should have REMOTE MEMBER: XXX@Q-FIM.MED.VA.GOV, which was created by the FIM install.

The RMIM MAIL SERVER mail group may be used in the future for better communication between Facility System and the Austin Automation Center in regards to ACK or ERR status. No members need to be in this group.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sign into the area where you intend to install the package. Make certain your DUZ variable is set to a valid user number and DUZ(0) equals “@”. Load the KIDS build RMIM1_0.KID using the Load a Distribution option.

> Select INSTALL NAME: FUNCTIONAL INDEPENDENCE 1.0 Loaded from Distribution

> 4/23/03@11:23:03

> =\> FUNCTIONAL INDEPENDENCE 1.0 ;Created on Apr 15, 2003@13:02:54

> This Distribution was loaded on Apr 23, 2003@11:23:03 with header of

> FUNCTIONAL INDEPENDENCE 1.0 ;Created on Apr 15, 2003@13:02:54

> It consisted of the following Install(s):

> FUNCTIONAL INDEPENDENCE 1.0

> Checking Install for Package FUNCTIONAL INDEPENDENCE 1.0

> Install Questions for FUNCTIONAL INDEPENDENCE 1.0

> Incoming Files:

> 783 FUNCTIONAL INDEPENDENCE MEASUREMENT RECORD

> 783.9 FUNCTIONAL INDEPENDENCE MEASUREMENT PARAMETER

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'RMIM FSOD': \<Enter REHAB FSOD/FIM Coordinator\>

> Enter the Coordinator for Mail Group 'RMIM FSOD TRANSMISSION': \<Enter IRM Support\>

> Enter the Coordinator for Mail Group 'RMIM MAIL SERVER': \<Enter IRM Support\>

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// n NO

> Want KIDS to INHIBIT LOGONs during the install? YES// n NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// n NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET DEVICE

> FUNCTIONAL INDEPENDENCE 1.0

> --------------------------------------------------------------------------------

Install Started for FUNCTIONAL INDEPENDENCE 1.0 :

> Apr 23, 2003@11:30:10

Build Distribution Date: Apr 15, 2003

Installing Routines:

Apr 23, 2003@11:30:10

Installing Data Dictionaries:

Apr 23, 2003@11:30:14

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing MAIL GROUP

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

FUNCTIONAL INDEPENDENCE 1.0

--------------------------------------------------------------------------------

Installing PROTOCOL

Located in the RMIM (FUNCTIONAL INDEPENDENCE) namespace.

Located in the RMIM (FUNCTIONAL INDEPENDENCE) namespace.

Installing REMOTE PROCEDURE

Installing OPTION

Apr 23, 2003@11:30:16

Updating Routine file...

Updating KIDS files...

FUNCTIONAL INDEPENDENCE 1.0 Installed.

Apr 23, 2003@11:30:18

Install Message sent \#37277096

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

100% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

Install Completed

# Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For post installation, schedule the following option to run nightly:

1\. Schedule Nightly Task

RMIM NIGHTLY TRANSMISSION TASK option.

This should be done before midnight

2\. Start HL7 Logical Link

> Select HL7 Main Menu Option: Filer and Link Management options

> Select Filer and Link Management Options Option: Start/Stop Links

> This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate.  
> Select HL LOGICAL LINK NODE: RMIM LINK  
> Select one of the following:  
> F FOREGROUND  
> B BACKGROUND  
> Q QUIT  
> Method for running the receiver: B//

3\. Create TIU Document Definitions

The following FIM progress note and consult note titles need to be added to the TIU Document Definition hierarchy using the TIU option Create Document Definitions.

The titles can be entered under the site-appropriate Document Class.

The three mandatory TIU titles can be site specific; however, only three titles are allowed.

For example:

- PM&R FIM NOTE
- PM&R FIM FSOD NOTE
- PM&R FIM CONSULT

  4\. Configuration File Management

The settings in this file are critical to the proper operation of the Functional Independence Measurement. Incorrect or missing settings will cause unpredictable results.

Please have your designated staff member add the FIM progress note and consult note titles to the TIU DOCUMENT DEFINITION file \#8925.1 via the option: Create Document Definitions.

The RMIM FIM SITE PARAMETERS file stores the system parameter data.

Use the option: FIM Site Parameter Edit (RMIM EDIT SITE PARAMETER). This option will edit the RMIM FIM SITE PARAMETERS \#783.9. Only one entry per primary facility for integrated sites.

Example:

Select RMIM FIM SITE PARAMETERS FACILITY NAME: WEST PALM BEACH VAMC Station Name

FACILITY NAME: WEST PALM BEACH VAMC// \<RET\>

MAIL GROUP: RMIM FSOD// \[Type this Mail Group Name.\]

FSOD NOTE TITLE: PM&R FIM TO FSOD NOTE// \[Type the name of the Progress Note title to identify it is an FSOD record.\]

NON FSOD NOTE TITLE: PM&R FIM NOTE// \[Type the name of the Progress Note title to identify a record did not go to FSOD.\]

CONSULT TITLE: PM&R FIM CONSULT// \[Type the name of the Progress Note title to identify Consult Completion.\]

Select FACILITY CODE: 7074// \[Multiple field to hold all of your Facility Codes.\]

FACILITY CODE: 7074//

TYPE OF CARE: CONTINUUM OF CARE// \[Type for the facility Code.\]

5\. Broker Context Menu Option Assignment

Assign Broker Context Menu \[RMIMFIM\] as a secondary menu item to anyone who will be using the FIM application.

# Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options will be created during installation:

|                                |                                             |
|--------------------------------|---------------------------------------------|
| Option                         | Description                                 |
| RMIM EDIT SITE PARAMETER       | FIM Site Parameter Edit                     |
| RMIM NIGHTLY TRANSMISSION TASK | FIM to FSOD Transmission Task               |
| RMIMFIM                        | RMIM FIM Context version 1.0.1.1            |
| RMIMIT                         | FIM Retransmit all records to Austin        |
| RMIM MAIL SERVER               | RMIM Mail Server                            |
| RMIM MAIL SERVER REPORT        | Austin Status Report for FSOD Transmissions |
| RMIM REPORTS                   | FIM Reports                                 |
| RMIMCOORD MENU                 | FIM Coordinators Menu                       |
| RMIMXMIT                       | FIM to FSOD by Patient                      |
| RMIMXMIT DATE                  | FIM to FSOD by Transmission Date            |

# Key Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rehab Medicine Management will determine which roles will require which key.

The following keys will be created during installation:

- RMIM COORD-FIM/FSOD Coordinators
- RMIM FSOD- User who will be sending data to Austin

# Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following mail group will be created during installation:

- RMIM FSOD
- RMIM FSOD TRANSMISSION \<adding members are not necessary\>
- RMIM MAIL SERVER \<adding members are not necessary\>

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM DRIVER

RMIM SUBSCRIBER

# Exported RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM distributes the following remote procedure calls (RPCs):

|                        |          |         |
|------------------------|----------|---------|
| RPC Name               | Line Tag | Routine |
| RMIM AUTHOR LOOKUP     | AL       | RMIMR   |
| RMIM CHECK DUPLICATE   | DUP      | RMIMV   |
| RMIM CONSULT LIST      | CON      | RMIMV   |
| RMIM CONVERT DATE      | DTFMT    | RMIMRP  |
| RMIM FIM PARAMETER     | PRM      | RMIMRP  |
| RMIM GET CASES         | LC       | RMIMRP  |
| RMIM GET DFN           | DFN      | RMIMRP  |
| RMIM GET FORM          | FRM      | RMIMRP  |
| RMIM GET PATIENT DME   | DME      | RMIMRP  |
| RMIM GET SELECTED CASE | GC       | RMIMRP  |
| RMIM GET USER INFO     | DUZ      | RMIMRP  |
| RMIM LOCATION LOOKUP   | LL       | RM IMRP |
| RMIM LOCK PATIENT      | PT L     | RMIMRP  |
| RMIM PATIENT INFO      | PI       | RMIMRP  |
| RMIM PATIENT LOOKUP    | PL       | RMIMRP  |
| RMIM RESTRICTED RECORD | RRN      | RMIMRP  |
| RMIM SAVE FSOD         | SAV      | RMIMRP  |
| RMIM SEND EMAIL        | XM       | RMIMRP  |
| RMIM VERSION           | RPC      | RMIMVP  |

# HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM AAC

RMIM SITE

# HL7 Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMIM LINK

# Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional bulletins are created during the installation the Functional Independence Measurement.