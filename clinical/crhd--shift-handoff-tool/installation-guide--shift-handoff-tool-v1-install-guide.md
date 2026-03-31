---
title: Shift Handoff Tool Version 1 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Install Guide
app_code: CRHD
app_name: Shift Handoff Tool
section: CLI
app_status: active
pkg_ns: CRHD
patch_ver: 1
patch_id: CRHD*1
group_key: "CRHD:CRHD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - crhd
  - install
  - contents
  - installation
  - table
  - tool
  - shift
  - handoff
  - server
  - transport
page_count: 0
word_count: 1438
section_count: 6
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=175"
---

---
title: |
  Shift Handoff Tool

  Installation Guide

  ![](shift-handoff-tool-version-1-install-guide/001.png)
---

Clinician Desktop Service

Veterans Health Information Technology

Version 1

June 2008

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date      | Description of Change | Technical Writer, Project Manager  |
|-----------|-----------------------|------------------------------------|
| June 2008 | Initial Release       | <span class="mark">REDACTED</span> |
|           |                       |                                    |
|           |                       |                                    |
|           |                       |                                    |
|           |                       |                                    |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Installation](#installation)
  - [Software Retrieval](#software-retrieval)
  - [## Server Installation](#server-installation)
    - [Server Installation Example](#server-installation-example)
  - [## Routine Checksums](#routine-checksums)
  - [Client Installation](#client-installation)
    - [Tools Menu](#tools-menu)
- [Converting from CAIRO Usage](#converting-from-cairo-usage)
This manual covers one time information for the installation of the Shift Handoff Tool Version 1.0. Other information required to maintain this application is included in the Shift Handoff Tool Implementation Guide and Technical Manual.
The Shift Handoff Tool is a utility that assists hospital staff going off shift to create a report for the incoming shift. This report contains demographic and medical information about each patient being handed off. At a minimum it shows medications and allergies, but can be customized to show other medical information that is relevant to the patient’s condition.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is both an M (or Server) component and a Windows (or Client) component. All the required files are contained in the distribution zip file: SHIFTHANDOFFTOOL.ZIP

Contents of SHIFTHANDOFFTOOL.ZIP:

| File                 | Description                                              |
|----------------------|----------------------------------------------------------|
| ShiftHandoffTool.exe | ShiftHandoffTool Executable                              |
| CRHD.HLP             | CRHD Help File                                           |
| CRHDIG.DOC           | Install Guide (Word Version)                             |
| CRHDIG.PDF           | Install Guide                                            |
| CRHDIGTM.DOC         | Implementation Guide and Technical Manual (Word Version) |
| CRHDIGTM.PDF         | Implementation Guide and Technical Manual                |
| CRHDUM.DOC           | User Manual (Word Version)                               |
| CRHDUM.PDF           | User Manual                                              |
| CRHDRN.DOC           | CRHD Release Notes (Word Version)                        |
| CRHDRN.PDF           | CRHD Release Notes                                       |

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Together, the CRHD_1.KID file and the SHIFTHANDOFFTOOL.ZIP file contain all the software and documentation necessary to install the Shift Handoff Tool. These files are available in the Office of Information Field Office (OIFO) ANONYMOUS.SOFTWARE directories listed below:

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Zip file contents:

| File Name                                   | Contents                                       | Retrieval Format |
|---------------------------------------------|------------------------------------------------|------------------|
| SHIFTHANDOFFTOOL.ZIP File(s) indented below |                                                | BINARY           |
| \- ShiftHandoffTool.exe                     | ShiftHandoffTool                               | Executable       |
| \- CRHD.HLP                                 | CRHD Help File                                 | Win Help 4       |
| \- CRHDIG.DOC                               | Install Guide (Word Version)                   | MS Word          |
| \- CRHDIG.PDF                               | Install Guide                                  | PDF              |
| \- CRHDIGTM.DOC                             | Implementation/Technical Manual (Word Version) | MS Word          |
| \- CRHDIGTM.PDF                             | Implementation/Technical Manual                | PDF              |
| \- CRHDUM.DOC                               | User Manual (Word Version)                     | MS Word          |
| \- CRHDUM.PDF                               | User Manual                                    | PDF              |
| \- CRHDRN.DOC                               | CRHD Release Notes (Word Version)              | MS Word          |
| \- CRHDRN.PDF                               | CRHD Release Notes                             | PDF              |

The files listed above may be obtained via FTP. The preferred method is to FTP the files from:

<span class="mark">REDACTED</span>

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| CIO FIELD OFFICE                   | FTP ADDRESS                        | DIRECTORY                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

## ## Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the M component by installing patch CRHD\*1. Installation should take less than 10 minutes, however, we recommend that you perform this installation at non-peak requirement hours.

Follow these steps:

1.  From the Kernel Installation & Distribution System menu, select the Installation menu.
2.  From the Kernel Installation & Distribution System menu, select the LOAD DISTRIBUTION option and load CRHD_1.KID.
3.  From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter CRHD 1.0):
    1.  You do not need to Backup a Transport Global – this patch contains routines in a new namespace, therefore there are not routines to back up.
    2.  You do not need to Compare Transport Global to Current System – this patch only contains new components not previously released, therefore there is nothing to compare.
    3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global – this option allows you to view the contents of the transport global.
4.  Use the Install Package(s) option and select the package CRHD 1.0.
5.  When prompted:

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

6.  When prompted

Want KIDS to INHIBIT LOGONs during the install? YES// NO

7.  When prompted

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

### Server Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

\<CPM\> Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: CRHD 1.0 Loaded from Distribution 6/5/08@13:55:47

=\> CRHD\*1V12 KIDS BUILD ;Created on May 13, 2008@07:07:55

This Distribution was loaded on Jun 05, 2008@13:55:47 with header of

CRHD\*1V12 KIDS BUILD ;Created on May 13, 2008@07:07:55

It consisted of the following Install(s):

CRHD 1.0

Checking Install for Package CRHD 1.0

Install Questions for CRHD 1.0

Incoming Files:

183 CRHD HANDOFF PARAMETERS

183.2 CRHD TEMPORARY DATA

183.3 CRHD HOT TEAM PATIENT LIST

183.4 CRHD TEAM CONTACT LIST

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET PORT

Install Started for CRHD 1.0 :

Jun 05, 2008@14:00:47

Build Distribution Date: May 13, 2008

Installing Routines:

Jun 05, 2008@14:00:47

Installing Data Dictionaries:

Jun 05, 2008@14:00:47

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Jun 05, 2008@14:00:47

Running Post-Install Routine: ENT^CRHDI01

Updating Routine file...

Updating KIDS files...

CRHD 1.0 Installed.

Jun 05, 2008@14:00:47

Not a production UCI

NO Install Message sent

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

## ## Routine Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD\*1.0 Routine CHECK1^XTSUMBLD values:

CRHD value = 1457874

CRHD1 value = 15630604

CRHD10 value = 12600193

CRHD11 value = 12360222

CRHD2 value = 61931550

CRHD3 value = 39552167

CRHD4 value = 54955462

CRHD5 value = 10041807

CRHD6 value = 23982080

CRHD7 value = 4400083

CRHD8 value = 22543750

CRHD9 value = 70845564

CRHDAM value = 18095609

CRHDDNR value = 16560217

CRHDDR value = 9947157

CRHDI01 Routine not in this UCI.(Post-install routine)  
Deleted automatically after installation

CRHDPL value = 15561818

CRHDUD value = 13222509

CRHDUT value = 67060529

CRHDUT2 value = 14775379

## Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Windows component will vary according to your own local management policies. Basically, it consists of the following steps:

1.  Place the executable, ShiftHandoffTool.exe, and the help file, CRHD.hlp, in the same directory on each workstation or on a network drive accessible from each workstation.
2.  Add Shift Handoff Tool to the Tools menu of CPRS.

In addition, you can do the following to workstations in hospital areas that are going to use this tool:

- Place a shortcut to ShiftHandoffTool.exe on the desktop. The parameters on the command line of this shortcut (S= and P=) must be the same as the parameters in the CPRS shortcut.  
  S= vista server P= RPC Broker port number

### Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may set up the tools menu on the User, Location, Service, Division, or System level. The lowest level overrides higher levels.

Select GUI Parameters Option: ?

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

NV GUI Non-VA Med Statements/Reasons

RM GUI Remove Button Enabled

NON GUI Remove Button Enabled for Non-OR Alerts

EIE GUI Mark Allergy Entered in Error

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select GUI Parameters Option: TM GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[DEVCUR.FO-SLC.MED.VA.GOV\]

Enter selection: 3 Division INSTITUTION

Select INSTITUTION NAME: salt

1 SALT LAKE CITY UT EES 925

2 SALT LAKE CITY UT NHC 6609AA

3 SALT LAKE CITY UT USAF 660CZ

4 SALT LAKE CITY HCS UT VAMC 660

5 SALT LAKE CITY OIFO UT ISC 5000

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 5 SALT LAKE CITY OIFO UT ISC 5000

------- Setting CPRS GUI Tools Menu for Division: SALT LAKE CITY OIFO -------Select Sequence: 2

Are you adding 2 as a new Sequence? Yes// y YES

Sequence: 2// 2

Name=Command: &Shift Handoff Tool=C:/CPRS/ShiftHandoffTool.exe S=%SVR P=%PORT

Select Sequence:

# Converting from CAIRO Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We strongly urge all sites using CAIRO (Class III software) to install the ShiftHandoffTool.exe client component and use the Shift Handoff Tool. This insures you will continue to get timely customer support and software updates.

> **NOTE:** Since CAIRO and the Shift Handoff Tool use different data files, you cannot continue to use the CAIRO client executable after the Shift Handoff Tool client executable is installed.

Data is copied from CAIRO into the Shift Handoff Tool file structure during the KIDS build. To seamlessly use the new tool, users need to be given CRHD SHIFT CHANGE HANDOFF in a menu or as a secondary menu option. Additionally, managers need to be given one or both of the following keys:

- CRHD SHIFT CHG HANDOFF MGR (This gives access to Preference Page)
- CRHD HOT TEAM MGR (This gives access to the configuration Handoff Tool (HOT) list)

Most parameters are transferred along with the data. The exceptions are:

| CAIRO Parameter Name (Class III) | ShiftHandoff Tool Parameter Name | Description                        |
|----------------------------------|----------------------------------|------------------------------------|
| AJRCHG DEFAULT PREFERENCE        | CRHD DEFAULT PREFERENCE          | Default Preference                 |
| AJRCHGOV DNR ORDER TITLE         | CRHD DNR ORDER TITLE             | DNR search strings                 |
| AJRCHGOV DNR ORDERABLE ITEMS     | CRHD DNR ORDERABLE ITEMS         | DNR search items                   |
| AJRCHG TEMP FLD EXPIRE           | CRHD TEMP FLD EXPIRE             | Temporary field expiration in days |

The Default Preference is automatically set the first time each user starts the tool. The two DNR parameters can most effectively be set with the DNR Order tab of the Preference Configuration dialog. The temporary field expiration can be set on the Temporary Fields tab of the Preference Configuration dialog.

> **NOTE:** You must explicitly set the CRHD DNR ORDER TITLE, CRHD DNR ORDERABLE ITEMS, and CRHD TEMP FLD EXPIRE parameters with VistA using the XPAR MENU TOOL option or by using the Preference Configuration dialog (preferred method) before using the Shift Handoff Tool.

For more details on implementation refer to the Shift Handoff Tool Implementation Guide and Technical Manual.