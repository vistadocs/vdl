---
title: EAS Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: This package contains all the routines, files, and options necessary to support the Enrollment Application System v.1.0 package, which represents Phase II of the Enrollment 10-10EZ initiative.
audience: 
keywords: 
  - installation
  - install
  - distribution
  - global
  - package
  - transport
  - table
  - contents
  - installing
  - want
page_count: 0
word_count: 1019
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-version-1-installation-guide/001.png)

enrollment application system

online 10-10EZ

Installation Guide

March 2001

V*IST*A System Design & Development

Table of Contents

# # Installation Instructions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Installation Instructions](#installation-instructions)
  - [Introduction](#introduction)
  - [Installing the Software](#installing-the-software)
  - [Sample Installation](#sample-installation)
  - [Post Installation](#post-installation)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package contains all the routines, files, and options necessary to support the Enrollment Application System v.1.0 package, which represents Phase II of the Enrollment 10-10EZ initiative.

The EAS_1.KID distribution file will be available as a host file at the usual Systems Design & Development software directories. Specific FTP addresses and directory names are provided by National VistA Support in the National Release message for EAS v1.0 on FORUM. Once the distribution file has been copied to your local system, use the Kernel Installation & Distribution System to load and install the software.

Installation will take less than 5 minutes and can be done during normal business hours with users on the system.

1.  Two patches are *required* to have been installed before you install EAS v1.0:
    1.  DG\*5.3\*325
    2.  IB\*2.0\*141
2.  A new entry will be made to your site PACKAGE File (#9.4) during this installation for the ENROLLMENT APPLICATION SYSTEM (EAS).
3.  Two new files will be created with this installation.
    1.  1010EZ MAPPING File (#711) in global ^EAS(711,.

This is a static, table file, which may be updated in future versions of EAS.

2.  1010EZ HOLDING File (#712) in global ^EAS(712,.

This is a dynamic file, which holds all incoming 1010EZ applications that have been electronically submitted (via the web site) to your local facility.

There are two phases to installation: Software installation and post-installation setup.

## Installing the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Alert!

Please establish the ^EAS global root on your system in compliance with your site’s global translation and protection scheme. The EAS global should be journalled.

User responses are bolded and underlined in the following installation steps.

1.  From the Kernel Installation & Distribution System menu, select Installation.

Select Installation Option:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: <u>Installation</u>

2.  From the Installation Option menu, select Load a Distribution

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>1</u> Load a Distribution

Enter a Host File: EAS_1.KID

KIDS Distribution saved on Mar 12, 2001@11:12:57

Comment: EAS v1.0

This Distribution contains Transport Globals for the following Package(s):

EAS 1.0

Distribution OK!

Want to Continue with Load? YES// <u>\<RET\></u>

Loading Distribution...

EAS 1.0

Use INSTALL NAME: EAS 1.0 to install this Distribution.

3.  When the Installation Option menu re-appears, select Verify Checksums in Transport Global.

Select Installation Option: ?

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Installation Option: <u>2</u> Verify Checksums in Transport Global

Select INSTALL NAME: <u>EAS 1.0</u>

This Distribution was loaded on Mar 12, 2001@19:02:54 with header of

EAS v1.0 ;Created on Mar 12, 2001@11:12:57

It consisted of the following Install(s):

EAS 1.0

DEVICE: HOME//

PACKAGE: EAS 1.0T8 Mar 12, 2001 7:03 pm PAGE 1

-------------------------------------------------------------------------------

28 Routines checked, 0 failed.

4.  If the loaded distribution file passed checksum verification , then proceed with the installation. When the Installation Option menu re-appears, select Install Package(s).

Select Installation Option: ?

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Installation Option: <u>6</u> Install Package(s)

Select INSTALL NAME: <u>EAS 1.0</u> Loaded from Distribution 3/12/01@19:02:54

- EAS v1.0 ;Created on Mar 12, 2001@11:12:57
5.  At the Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// prompt, enter “NO”.

    At the Want KIDS to INHIBIT LOGONs during the install? YES// prompt, enter “NO”.

    At the Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// prompt, enter “NO”.

    At the DEVICE: HOME// prompt, do one of the following:
- Press \<Enter\> to display the installation summary on the screen
- Enter the name of a printer and press \<Enter\>. This will send the installation summary to the specified device.
6.  Proceed *immediately* to the Post-Installation Instructions.

## Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: <u>6</u> Install Package(s)

Select INSTALL NAME: <u>EAS 1.0</u> Loaded from Distribution 3/12/01@19:02:54

=\> EAS v1.0 ;Created on Mar 12, 2001@11:12:57

This Distribution was loaded on Mar 12, 2001@19:02:54 with header of

EAS v1.0 ;Created on Mar 12, 2001@11:12:57

It consisted of the following Install(s):

EAS 1.0

Checking Install for Package EAS 1.0

Install Questions for EAS 1.0

Incoming Files:

711 1010EZ MAPPING (including data)

712 1010EZ HOLDING

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// <u>NO</u>

Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// <u>\<RET\></u>

------------------------------------------------------------------------------

Install Started for EAS 1.0 :

Mar 12, 2001@19:04:26

Build Distribution Date: Mar 12, 2001

Installing Routines:

Mar 12, 2001@19:04:30

Installing Data Dictionaries:

Mar 12, 2001@19:04:34

Installing Data: .

Mar 12, 2001@19:04:37

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Mar 12, 2001@19:04:41

Updating Routine file...

Updating KIDS files...

EAS 1.0 Installed.

Mar 12, 2001@19:04:43

Install Message sent \#317254

Install Completed

## Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Alert!

It is critical for the EAS EZ SERVER option to be added as a Remote Member of the VA1010EZ Mail Group immediately after the software is installed

1.  Proceed as follows from programmer mode. User responses are bolded and underlined.

> \><u>D P^DI</u>

> VA FileMan 22.0

> Select OPTION: <u>1</u> ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: PACKAGE// MAIL GROUP (278 entries)

> EDIT WHICH FIELD: ALL// 12 MEMBERS - REMOTE (multiple)

> EDIT WHICH MEMBERS - REMOTE SUB-FIELD: ALL//

> THEN EDIT FIELD:

> Select MAIL GROUP NAME: <u>VA1010EZ</u>

> Select REMOTE MEMBER: <u>?</u>

> You may enter a new MEMBERS - REMOTE, if you wish

> Enter a remote address (name@domain) or local device (D.device)

> or local server (S.device).

> Select REMOTE MEMBER: <u>S.EAS EZ SERVER@YOUR-SITE.VA.GOV</u>

> Are you adding 'S.EAS EZ SERVER@YOUR-SITE.VA.GOV' as

> a new MEMBERS - REMOTE (the 1ST for this MAIL GROUP)? No// <u>Y</u> (Yes)

> Select REMOTE MEMBER:

> Use your site’s Domain name in place of ‘YOUR-SITE.VA.GOV’. Enter the Domain name exactly as it appears in ^XMB(“NETNAME”).

2.  Provide the *10-10EZ Menu* option \[EAS EZ MENU\] to the appropriate users. This option may be placed on the user’s Secondary Menu with a Synonym for ease of access, such as “EZ”.