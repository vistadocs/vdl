---
title: YS*5.01*78 MH Addiction Severity Index-Multimedia Version Installation and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: MH Addiction Severity Index-Multimedia Version Installation and
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*78
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vista
  - contents
  - table
  - software
  - installation
  - health
  - interface
  - mental
  - asimv
  - patch
page_count: 0
word_count: 7389
section_count: 24
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_asimv_igum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_asimv_igum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/001.png)

MENTAL HEALTH

ADDICTION SEVERITY INDEX MULTIMEDIA VERSION (ASI-MV)

INSTALLATION AND USER GUIDE

PATCH YS\*5.01\*78

November 2004

V*IST*A Health Systems Design and Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
  - [Mental Health ASI-MV Installation and User Guide Orientation:](#mental-health-asi-mv-installation-and-user-guide-orientation)
    - [Installation and User Guide Screen Displays](#installation-and-user-guide-screen-displays)
    - [### Software and Manual Retrieval](#software-and-manual-retrieval)
    - [Website Locations](#website-locations)
    - [Related Manual](#related-manual)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Interface Software](#vista-mental-health-addiction-severity-index-multimedia-version-asi-mv-interface-software)
    - [Commercial Off The Shelf (COTS) ASI-MV Software](#commercial-off-the-shelf-cots-asi-mv-software)
    - [SecureDesktop](#securedesktop)
- [Security Information](#security-information)
- [Pre-Installation Information](#pre-installation-information)
  - [Recommended Users:](#recommended-users)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff)
    - [Mental Health Clinician](#mental-health-clinician)
    - [Patients](#patients)
  - [Test Sites:](#test-sites)
  - [VistA Operating System](#vista-operating-system)
  - [VistA Operating System Performance Capacity](#vista-operating-system-performance-capacity)
  - [VistA MH ASI-MV Hardware and Software Requirements](#vista-mh-asi-mv-hardware-and-software-requirements)
    - [MH ASI-MV Interface Software Requirements](#mh-asi-mv-interface-software-requirements)
    - [Workstation Hardware Requirements and Guidelines](#workstation-hardware-requirements-and-guidelines)
  - [## Software Installation Time:](#software-installation-time)
  - [Users on the System](#users-on-the-system)
  - [Backup Transport Global](#backup-transport-global)
  - [## Mental Health ASI-MV Patch YS\5.01\78 Distribution](#mental-health-asi-mv-patch-ys50178-distribution)
  - [Namespace](#namespace)
  - [## Required VistA Software Applications:](#required-vista-software-applications)
  - [Required Patch:](#required-patch)
  - [## Routines](#routines)
  - [## YS BROKER Option](#ys-broker-option)
  - [YS BROKER1 Option](#ys-broker1-option)
  - [Data Dictionary](#data-dictionary)
- [Installation Instructions](#installation-instructions)
    - [Installation Example:](#installation-example)
- [# Post Installation Instructions](#post-installation-instructions)
  - [COTS ASI-MV Version 4.0VA First Time PC Installation:](#cots-asi-mv-version-40va-first-time-pc-installation)
    - [IRM:](#irm)
  - [VistA MH ASI-MV Interface Software First Time PC Installation:](#vista-mh-asi-mv-interface-software-first-time-pc-installation)
    - [IRM:](#irm-1)
    - [Example: Adding the VistA MH ASI-MV Interface menu to the VistA CPRS GUI Toolbar](#example-adding-the-vista-mh-asi-mv-interface-menu-to-the-vista-cprs-gui-toolbar)
    - [VistA Mental Health ASI-MV Interface Software Installation Examples](#vista-mental-health-asi-mv-interface-software-installation-examples)
    - [Completing the ASI-MV Setup Wizard](#completing-the-asi-mv-setup-wizard)
  - [VistA ASI-MV Interface Software Upgrade Instructions](#vista-asi-mv-interface-software-upgrade-instructions)
    - [IRM Staff:](#irm-staff)
- [VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Patch YS\5.01\78 User Guide](#vista-mental-health-addiction-severity-index-multimedia-version-asi-mv-patch-ys50178-user-guide)
  - [Use of the Software](#use-of-the-software)
    - [Starting MH ASI-MV Patch YS\5.01\78 Software Application](#starting-mh-asi-mv-patch-ys50178-software-application)
    - [ASIMV Error Incomplete File](#asimv-error-incomplete-file)
The Veterans Information Systems and Technology Architecture (Vist*A*) Mental Health (MH) Addiction Severity Index Multimedia Version (ASI-MV) Installation and User Guide for Patch YS\*5.01\*78 provides detailed instructions required for installing and implementing the MH ASI-MV II software update.

## Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Veterans Health Administration (VHA) Office of Information Health Systems Design & Development staff have made every effort during the design, development and testing of this application to ensure full accessibility to all users in compliance with Section 508 of the Rehabilitation Act of 1973, as amended. Please send any comments, questions or concerns regarding the accessibility of this application to:

<span class="mark">REDACTED</span>

## Mental Health ASI-MV Installation and User Guide Orientation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security Information section provides security risk countermeasures information for the VistA Mental Health ASI-MV Patch YS\*5.01\*78.

Pre-installation Information section provides requirements needed prior to the installation of Patch YS\*5.01\*78.

Installation Instructions section contains instructions and examples of VistA MH ASI-MV Patch YS\*5.01\*78.

Post Installation Instructions section provides directions for implementing VistA MH ASI-MV Patch YS\*5.01\*78 and COTS ASI-MV software.

ASI-MV User Guide section provides detailed instructions required to use the VistA MH ASI-MV Patch YS\*5.01\*78 software.

### Installation and User Guide Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Screen Captures

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

#### User Response

User entry response appears in boldface type Courier font, no larger than 10 points.

Example:Boldface type

#### Return Symbol

User response to computer dialogue is followed by the \<RET\> symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<RET\>

#### Tab Symbol

User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<Tab\>

### ### Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All sites are encouraged to use the FTP capability to obtain these files. Use the FTP address “*download.vista.med.va.gov*” (without the quotes) to connect to the first available FTP server where the files are located.

VistA Mental Health ASI-MV Patch YS\*5.01\*78 software files and Installation and User Guide (i.e., YS_ASIMV_IGUM.pdf) are available on the following Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE DIRECTORIES:

OIFOsFTP ADDRESSDIRECTORY

<span class="mark">REDACTED</span>

VistA Mental Health ASI-MV software and Installation and User Guide are exported as part of Patch YS\*5.01\*78 in the formats listed below:

FILE NAME CONTENTS RETRIEVAL FORMAT

YS_501_78.ZIP BINARY

\- YS_501_78_SETUP_1_0_3_10.EXE ASI-MV complete install for version 1.0.3.10 of the ASI-MV

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

-YS_ASIMV_IGUM.pdf YS_ASIMV Installation and User Guide

-YS_ASIMV_IGUM.doc YS_ASIMV Installation and User Guide

### Website Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Mental Health (MH) Addiction Severity Index Multimedia Version (ASI-MV) Installation and User Guide for Patch YS\*5.01\*78 are available in the following formats and Intranet locations:

- YS_ASIMV_IGUM.doc
- YS_ASIMV_IGUM.pdf

VistA Mental Health Version 5.01 Home Page

<span class="mark">REDACTED</span>

VistA Documentation Library (VDL)

<http://www.va.gov/vdl/>

### Related Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Addiction Severity Index Multimedia Version (ASI-MV) Guidebook

*By: Inflexxion*Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Addiction Severity Index (ASI) is the primary instrument used in Veterans Health Administration (VHA) to evaluate individual patients’ response to substance dependence treatment and to evaluate the overall effectiveness of substance dependence treatment programs. Currently the ASI interview is administered through the VistA roll-and-scroll functionality. Patients’ ASI interviews are generally recorded on paper and entered later by the clinician or clerk. The ASI interview is a labor-intensive measure. It requires 45-60 minutes to administer an ASI interview and an additional 20 minutes following the interview to enter the data into the V*ist*A Mental Health (MH) database using the roll-and-scroll method.

The principal objective of the VistA MH ASI-MV Patch YS\*5.01\*78 software is to allow patients to respond to an ASI interview conducted by *virtual* (computer-animated) counselors. The VistA MH ASI-MV software application is a significant time-saver for clinicians, because clinicians need not be present during the interview, and are freed to use this time for other tasks.

A VA clinician logs on to VistA using Computer Patient Record System (CPRS) Graphic User Interface (GUI.) ASI-MV is started by choosing the ASI-MV entry from the Tools menu list in CPRS. Once ASI-MV is started, it keeps synchronized with the patient currently selected in CPRS. This enables a connection for data exchange, for selecting a patient, and performing other configuration tasks. The clinician configures the remaining ASI-MV session parameters, and explains to the patient how to use the self-administered ASI-MV interview software. Immediately after configuring ASI-MV parameters, CPRS is automatically shutdown and the workstation security application (SecureDesktop) is activated. SecureDesktop prevents patients from accessing unauthorized files and programs on the computer, while interacting with ASI-MV software. Patients are then given privacy and allowed time to complete an interview. The time it takes to complete an interview varies from forty-five minutes to one and a half hours, or longer.

After an ASI-MV interview is completed, the clinician must logon to the workstation, start CPRS and invoke ASI-MV from the CPRS Tools menu again, at this time the ASI-MV interview data is translated to a VistA format and uploaded to the VistA database.

### VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Interface Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA MH ASI-MV interface software is updated to accompaniment the existing Addiction Severity Index (ASI) component of the V*ist*A Mental Health V. 5.01 software application. The V*ist*A MH ASI-MV interface introduces the functionality required to run the Commercial off the Shelf (COTS) Addiction Severity Index Multimedia Version (ASI-MV) software. The interface allows clinicians and patients to enter demographics and self-administered ASI-MV interviews via a PC workstation using video and audio technology. The V*ist*A MH ASI-MV interface works mostly in the background. The demographic and interview data is temporarily stored on a PC workstation when an interview is completed and saved to the VistA MH database automatically when the software is executed again.

### Commercial Off The Shelf (COTS) ASI-MV Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The COTS ASI-MV software is an effective, efficient, and scientifically researched tool used in substance abuse treatment centers, employee assistance programs, and other healthcare settings. The software utilizes a mouse-driven personal computer (PC) for administering an ASI-MV interview and gathering clinical data directly from a client/patient/employee. The COTS ASI-MV software generates V*ist*A -compatible data records that can be uploaded to the V*ist*A database.

### SecureDesktop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SecureDesktop software prevents patient access to the Windows desktop and to task-switching functions. This software implements the bulk of security countermeasures for the V*ist*A MH ASI-MV interface software and the COTS ASI-MV software applications.

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vis*t*A MH ASI-MV Patch YS\*5.01\*78 software implements the following security risk countermeasures:

1.  Immediately after the “Start new ASI” button is clicked, CPRS is shutdown automatically and the connection to VistA is closed to prevent unauthorized access to VistA. SecureDesktop is then activated.
2.  No patient-identifiable data is stored locally. The ASI-MV interface interprets the patient Internal Entry Numbers (IENs) to identify the patient in Vis*t*A.
3.  When the security risk countermeasures are invoked in the ASI-MV interface, all active programs NOT required for an ASI-MV interview session are closed. This prevents the patient from accessing unauthorized programs while responding to the ASI-MV interview.
4.  During an ASI-MV interview session the Windows Desktop is disabled and not visible to the patient. The desktop and Taskbar will not respond to mouse clicks or keyboard entries.
5.  After the patient completes an ASI-MV interview the Windows Desktop session is terminated, and the patient is automatically logged off the system. This prevents patients from accessing or starting other programs, after ASI-MV terminates.
6.  All keystrokes are trapped and filtered out with an appropriate response. In all cases, this response is to ignore or cancel the keystroke.
7.  All keystrokes are trapped at the system user level, which detects and processes the keystrokes generated by any application in the current desktop session.
8.  The taskbar is disabled and not visible to the patient. The Start key is neither visible nor active.
9.  The Microsoft Office Shortcut Bar is shutdown and not visible.
10. A maximum of 10 “accidental” keystrokes are allowed. On the 11<sup>th</sup> keystroke, all programs are terminated, the user is logged out of the program, and the PC shuts down the Window’s desktop session.
11. Every keystroke activates the screensaver. After a brief pause the workstation is locked, requiring the user to enter a password to regain access and continue the ASI-MV session.
12. If the ASI-MV Vista Interface software is terminated normally or abnormally, all programs are terminated and the user is logged out of the system.
13. The ASI-MV has a timer event that activates every 200 millisecond. This timer is used to trigger activity detection cycles.
14. On the timer event, the ASI-MV is always the topmost window (covering the entire screen view), hiding any open windows behind it.
15. On the timer event, a keystroke count is updated and evaluated. If the keystrokes count \> 10 then the session is shut down and the user is logged off. This allows for no more than10 accidental keystrokes.
16. On the timer event, if a “Windows NT or WIN2000 Task Manager”, “Windows NT or WIN2000 Security”, or Windows Explorer application is active, it is immediately closed. This prevents the CTRL-ALT-DEL keystroke that allows access to the task manager in Windows NT and WIN2000.
17. On the timer event, the status of the COTS ASI-MV product is detected. If ASI-MV is not running, then the session is closed and the user is logged off.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information contains recommendations and requirements that should be acknowledged prior to installing the VistA Mental Health ASI-MV Patch YS\*5.01\*78:

## Recommended Users:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is recommended for installing and supporting VistA Mental Health ASI-MV Patch YS\*5.01\*78 requirements.

### Mental Health Clinician

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health clinicians enter patient demographic and interview parameters data using VistA CPRS, MH ASI-MV, and COTS ASI-MV software.

### Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patients being treated in the specialized Substance User Disorder treatment programs are required to have an ASI at the beginning of treatment and 6 months later. The ASI-MV is an efficient way of administering the ASI because minimal staff time is required.

## Test Sites:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Mental Health ASI-MV Patch YS\*5.01\*78 has been tested at the following sites on the various Operating Systems (OS):

| Test Sites                     | Operating Systems            |
|------------------------------------|----------------------------------|
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | CACHE NT (TM) Server Version 4.0 |
| <span class="mark">REDACTED</span> | CACHE NT (TM) Server Version 4.0 |
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | DSM VMS V7.3-1                   |
| <span class="mark">REDACTED</span> | DSM VMS V.7.3-1                  |
| <span class="mark">REDACTED</span> | CACHE VMS V.7.3-1                |
| <span class="mark">REDACTED</span> | DSM VMS V.7.3-1                  |
| <span class="mark">REDACTED</span> | CACHE VMS V.7.3-1                |
| <span class="mark">REDACTED</span> | DSM VMS V.7.3-1                  |

## VistA Operating System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.01 software application package currently runs on the standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters, and run either VMS or NT and WIN2000 and the Open M product. All current 486 sites are being converted to Alpha 1000A AXP Cluster, NT and WIN2000, and Open M systems.

## VistA Operating System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no significant changes in the performance capacity of the VistA operating system once the Mental Health ASI-MV Patch YS\*5.01\*78 has been installed. The software should not create any appreciable global growth or network transmission problems. There are no memory constraints.

## VistA MH ASI-MV Hardware and Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NOTES:

1.  The request for workstations, servers, and cabling plants are beyond the basic upgrading of the facility’s main computer cluster to the newer DEC Alpha systems to provide the additional capacity needed to run the Mental Health ASI-MV Patch YS\*5.01\*78 software and related applications (e.g., CPRS, TIU, PCMM, PDM).
2.  VHA facilities are encouraged to budget and purchase PC workstations as replacements for dumb terminals. The VHA LAN and Workstation task force report is recommended as a guide.

### MH ASI-MV Interface Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VistA’s Remote Procedure Call (RPC) Broker Version 1.1 or greater software must be properly installed and configured on the MH ASI-MV PC workstation.
- Audio card with software driver must be installed and properly configured.
- Insure that the Windows screensaver is active and that it is password-protected.
- VistA’s CPRS Client software must be properly installed and configured on the MH ASI-MV PC workstation. CPRS Tools Menu must be configured according to instructions found elsewhere in this document.

### Workstation Hardware Requirements and Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Video card and a software driver capable of a minimum 800x600 dpi and 16-bit color display must be installed and properly configured.
- Computer with CD player, soundcard, and speakers
- Color VGA monitor (set at 24 bit)
- Printer, mouse, and keyboard
- 166 MHz processor with at least, 64 megabytes RAM
- 10 megabytes free hard drive space
- Microsoft Windows NT (with service pack 6) or WIN2000 4.0

## ## Software Installation Time:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health ASI-MV Patch YS\*5.01\*78 installation time is less than 5 minutes during off peak hours, and less than 15 minutes during peak hours (i.e., off peak hours is RECOMMENDED).

## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may remain on the system, but installation should be done during off peak.

## Backup Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that a backup of the transport global be performed before installing the patch.

## ## Mental Health ASI-MV Patch YS\*5.01\*78 Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Mental Health ASI-MV Patch YS\*5.01\*78 is using the Kernel Installation and Distribution System (KIDS).

> **NOTE:** For further instructions on using KIDS, please refer to the Kernel Version 8.0 Systems Manual.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Mental Health software namespace is YS.

## ## Required VistA Software Applications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software Applications Versions

Mental Health 5.01

RPC Broker 1.1

Kernel 8.0

VA FileMan 22.0

Mailman 7.1

Toolkit 7.3

Computer Patient Record System (CPRS) 1.0.24.26

## Required Patch:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*67 MUST be installed prior to installing V*ist*A Mental Health ASI-MV Patch YS\*5.01\*78.

## ## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No routines are being sent out via the Mental Health ASI-MV Patch YS\*5.01\*78.

## ## YS BROKER Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS BROKER \[YS BROKER\] option is deleted during the install of MH ASI_MV patch YS\*5.01\*78.

## YS BROKER1 Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS BROKER1 \[YS BROKER1\] option contains the context necessary to interface the ASI-MV to VistA.

## Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No data dictionary changes are required for the release of Mental Health ASI-MV Patch YS\*5.01\*78.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Mental Health ASI-MV Patch YS\*5.01\*78 is using the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the Kernel V. 8.0 Systems Manual.

IRM Staff:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*IMPORTANT NOTE TO IRM: THIS PATCH MUST BE INSTALLED. ALTHOUGH NO ROUTINES\*\*

\*\*ARE INCLUDED IN THIS PATCH KIDS DELETES THE OPTION YS BROKER \[YS BROKER\]\*\*\*

\*\*WHEN THE PATCH IS INSTALLED.                                             \*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*NOTE: This patch should be installed during ‘OFF PEAK’ hours when few or no users are on the system. Installation of the patch will take less than 5 minutes.

1\. Use the 'INSTALL/CHECK MESSAGE' option on the PackMan menu. This option will load the KIDS package in this message onto your system.

2\. The patch has now been loaded into a Transport global on your system. You now need to use KIDS to install the Transport global. On the KIDS menu, under the 'Installation' menu, use the following options:

Print Transport Global

Compare Transport Global to Current System

Backup a Transport Global

3\. Installation of this patch should be at off peak hours.

4\. Users may remain on the system.

5\. Installation will take less than five minutes. Installation of this patch requires no additional memory space.

6\. From the ‘Installation Menu’ of the KIDS menu, run the option ‘Install Package(s)’ Select the package ‘YS\*5.01\*78’ and proceed with install.

7\. When prompted 'Want KIDS to Rebuild Menu Trees upon Completion of Install? YES//', respond YES. Responding with a yes, will add considerable time to the installation.

8\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond NO.

9\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond NO.

10\. Retrieve and open the file: YS_501_78.ZIP

11\. Place the MENTAL HEALTH ADDICTION SEVERITY INDEX MULTIMEDIA VERSION (ASI-MV) INSTALLATION AND USER GUIDE in a location that can be accessed by ASI-MV users.

12\. Please refer to the POST INSTALLATION INSTRUCTIONS section of the MENTAL HEALTH ADDICTION SEVERITY INDEX MULTIMEDIA VERSION (ASI-MV) INSTALLATION AND USER GUIDE to install the COTS ASI-MV software, YS_ASIMV.EXE, YS_ASIMV_SD.EXE and YS_ASIMV_KH.DLL.

13\. Place the option YS BROKER1 \[YS BROKER1\] on the Mental Health user’s secondary menu.

### Installation Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: 6\<ENTER\> Install Package(s)

Select INSTALL NAME: YS\*5.01\*78 Loaded from Distribution 1/23/04@15:02:10

=\> YS\*5.01\*78 TEST V1

This Distribution was loaded on Jan 23, 2004@15:02:10 with header of YS\*5.01\*78 TEST V1

It consisted of the following Install(s):

YS\*5.01\*78

Checking Install for Package YS\*5.01\*78

Install Questions for YS\*5.01\*78

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO\<ENTER\>

Want KIDS to INHIBIT LOGONs during the install? YES// NO\<ENTER\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO\<ENTER\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<ENTER\> UCX/TELNET

Install Started for YS\*5.01\*78 :

Jan 23, 2004@15:04:51

YS\*5.01\*78

───────────────────────────────────────────────────────────────────────────

Build Distribution Date: Jan 23, 2004

Installing Routines:

Jan 23, 2004@15:04:51

Installing PACKAGE COMPONENTS:

Installing OPTION

Jan 23, 2004@15:04:54

Updating Routine file...

Updating KIDS files...

YS\*5.01\*78 Installed.

Jan 23, 2004@15:04:54

Install Message sent \#1398040

────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

# # Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Mental Health (MH) Addiction Severity Index Multimedia (ASI-MV) Interface Software and the Commercial of the Shelf (COTS) Addiction Severity Index Multimedia (ASI-MV) Version 4.0VA software first time PC installation and upgrade instructions must be completed as follows:

> **NOTE:** The VistA ASI-MV and COTS ASI-MV software first time PC and ASI-MV upgraded software installation MUST be installed on a mouse-driven PC Workstation.

NOTES:

IRM staff installing the VistA ASI-MV software MUST have Administrator privileges on the PC Workstation platform.

Insure that the Windows screensaver is active and that it is password-protected. It is recommended to use one of the screensavers supplied with the original Windows installation. Preferably the “Default Screen Saver.”

## COTS ASI-MV Version 4.0VA First Time PC Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Install the COTS ASI-MV Version 4.0VA software as stated in the manufacturer’s instruction booklet included with the ASI-MV Version 4.0VA CD-ROM.

## VistA MH ASI-MV Interface Software First Time PC Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Assign USERS the YS BROKER1 as a secondary menu option.

Step 2: From one of the following Office of Information Field Offices (OIFOs) Anonymous Software Directories retrieve and open the YS_501_78\_.ZIP file:

OIFO Anonymous Software Directories

<span class="mark">REDACTED</span>

The YS_501_78_ZIP file contains the following files:

FILE NAME CONTENTS RETRIEVAL FORMAT

YS_501_78.ZIP BINARY

\- YS_501_78_SETUP_1_0_3_10.EXE ASI-MV complete install for version 1.0.3.10 of the ASI-MV

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_ASIMV_IGUM.PDF YS\*5.01\*78 ASI-MV Installation Guide User Manual

\- YS_ASIMV_IGUM.doc YS_ASIMV Installation and User Guide

Step 3: Double click on the YS_501_78_SETUP_1_0_3_10.EXE to install version 1.0.3.10 of the ASI-MV interface.

> **NOTE:** See the VistA Mental Health ASI-MV Interface Software Installation examples following Step 6 in this section.

Step 4: VistA MH ASI-MV Interface Software MUST NOW be started from the Computer Patient Record System (CPRS) Tools Menu.

How to add the VistA MH ASI-MV Interface menu entry to the VistA CPRS GUI Toolbar.

VistA MH ASI-MV Interface Software user-definable text will appear in the CPRS drop-down Tools Menu. This text represents the menu entry that the user MUST click on to invoke the VistA MH ASI-MV Interface Software.

C:\Progra~1\asimv4\ys_asimv.exe is the path where the VistA MH ASI-MV Interface Software executable can be found by default. If the path was changed during VistA MH ASI-MV Interface Software installation, this entry must be adjusted accordingly.

> **NOTE:** The tilde-abbreviated notation for the “Program Files” folder is necessary. If CPRS is unable to invoke VistA MH ASI-MV Interface Software, check for spaces in the folder path text and replace the tilde notation according to Windows standards.

s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF these are the five parameters passed by CPRS to VistA MH ASI-MV Interface Software. This section of the NAME=COMMAND line must be included verbatim. All five parameters must be present and they must be listed in the indicated sequence.

### Example: Adding the VistA MH ASI-MV Interface menu to the VistA CPRS GUI Toolbar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^XUP \<Enter\>

Setting up programmer environment

Terminal Type set to: C-VT100 \<Enter\>

Select OPTION NAME: EVE \<Enter\>

1 EVE Systems Manager Menu

2 EVENT DELAYED ORDERS MENU OR DELAYED ORDERS Event Delayed Orders Menu

CHOOSE 1-2: 1 EVE Systems Manager Menu \<Enter\>

Taskman Management ...

DISK Disk Space Management ...

FM VA FileMan ...

HL7 HL7 Main Menu ...

Application Utilities ...

Capacity Management ...

Core Applications ...

Device Management ...

Information Security Officer Menu ...

Manage Mailman ...

Menu Management ...

Operations Management ...

Programmer Options ...

Spool Management ...

User Management ...

Select Systems Manager Menu Option: core Applications \<Enter\>

2000 User Menu for Pharmacy 2000 ...

2000 Pharmacy 2000 Manager Menu ...

AHJL PACKAGE TRACKING MENU ...

AMIE A.M.I.E. Medical Administration Menu ...

COP CHIEF POLICE MENU ...

DENT Dental ...

DUM Document Upload Manager ...

EWO EWO Electronic Work Requests ...

FH Dietetics Management ...

GMTS Health Summary Coordinator's Menu ...

IB Integrated Billing Master Menu ...

IV IV Menu ...

MAS MAS MANAGER ...

NDF National Drug File Menu ...

NRS Nursing System Manager's Menu ...

ODS ODS Supervisor Menu ...

RO A.M.I.E Regional Office Main Menu ...

TIU All TIU/USR Mgr Menus ...

WS Automatic Replenishment ...

ZLBL Transaction & Record Information Menu ...

2NE Policy editing

ADP MENU ...

Career Center Menu ...

Chaplain Menu ...

Communications Menu ...

CPRS Manager Menu ...

Day Hospital Menu ...

Dietetics Roster

Display Lab Tests and Results for Clozapine order

Employee Inquiry Menu ...

Employee Inquiry/Reports Menu ...

Engineering Main Menu ...

Enter/Edit/Print Psych Triage

Environmental Management Menu ...

Fee Service Menu ...

Generic Code Sheet Menu ...

Health Summary Maintenance Menu ...

IFCAP ...

KB SQL

Lab Coordinator Menu ...

Lab Menu ...

List of Override Prescriptions

MAS Admissions Menu ...

Medical Records Menu ...

Medicine Menu ...

Mental Health ...

MHS Manager ...

Occurrence Screening Menu ...

Outpatient Pharmacy Manager ...

Patient Funds (INTEGRATED) System ...

Psychology Menu ...

Rad/Nuc Med Total System Menu ...

Record Tracking Total System Menu ...

Remote Order/Entry System ASPS Menu ...

Seriously Ill list

Social Work Menu ...

Surgery Menu ...

Utilization Management Rollup Main Menu ...

VIST Menu ...

Volunteer Timekeeping Activity ...

Select Core Applications Option: cprs Manager Menu \<Enter\>

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

TOOL General Parameter Tools ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select CPRS Manager Menu Option: pe CPRS Configuration (Clin Coord) \<Enter\>

AL Allocate OE/RR Security Keys

KK Check for Multiple Keys

DC Edit DC Reasons

GP GUI Parameters ...

GA GUI Access - Tabs, RPL

MI Miscellaneous Parameters

NO Notification Mgmt Menu ...

OC Order Checking Mgmt Menu ...

MM Order Menu Management ...

LI Patient List Mgmt Menu ...

FP Print Formats

PR Print/Report Parameters ...

RE Release/Cancel Delayed Orders

US Unsigned orders search

EX Set Unsigned Orders View on Exit

NA Search orders by Nature or Status

DO Event Delayed Orders Menu ...

PM Performance Monitor Report

Select CPRS Configuration (Clin Coord) Option: gp GUI Parameters \<Enter\>

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select GUI Parameters Option: tm GUI Tool Menu Items\<ENTER\>

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[LOMA-LINDA.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 1User NEW PERSON \<Enter\>

Select NEW PERSON NAME: MHUser, One \<Enter\>

----------- Setting CPRS GUI Tools Menu for User: MHUser, One -----------

Select 1: 4 \<Enter\>

Are you adding 4 as a new 1? Yes//\<Enter\> YES

1: 4//\<Enter\> 4

Value: ASI-MV=C:\Progra~1\asimv4\ys_asimv.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

Select 1:

Step 5: Add YOUR SITE to the entries in your HOSTS FILE

> A. Search for a TEXT file named HOSTS (that is right, no filename extender). This file is typically found in c:\WINNT\system32\drivers\etc. Search for it using HOSTS.

> B. Open the HOSTS FILE and append the entry USING NOTEPAD:

Example: Adding YOUR SITE to the entries in your HOSTS FILEYour Site’s IP Address Site Name Port

<span class="mark">REDACTED</span> Bay Pines <span class="mark">REDACTED</span>

> C. Save HOSTS FILE changes.

Step 6: Place the VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Patch YS\*5.01\*78 Installation and User Guide (YS_ASIMV_IGUM.DOC and YS_ASIMV_IGUM.PDF) in a location that is accessible by VistA MH ASI-MV USERS.

### VistA Mental Health ASI-MV Interface Software Installation Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following illustrates the VistA Mental Health ASI-MV Interface Software installation windows. When the default responses are accepted, the VistA Mental Health ASI-MV Interface software is installed into the appropriate VistA directory on the user’s PC workstation.

The VistA Mental Health ASI-MV Interface Software file names of the executables are different than in the first release. The first release executable file names included the patch version number. This new release does not. Therefore, the old executables can safely be deleted to avoid confusion.

> NOTE: When installing on a PC where the VistA ASI-MV software does not exist use the following: YS_501_78_Set_1_0_3_10.exe

Example: From the Setup - ASI-MV, R3 dialog box, click on the Next command button (located at the bottom of the window) to continue with the install.

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/002.png)  
<span id="_Toc87744358" class="anchor"></span><u>Setup - ASI-MV, R3</u>

Example: On the Setup - ASI-MV, R3 dialog box click on the Install command button (located at the bottom of the window) to install the ASI-MV, R3 software application.

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/003.png)  
<span id="_Toc87744359" class="anchor"></span><u>Setup ASI-MV on Your Computer</u>

Example: On the Setup - ASI-MV dialog box click on the Cancel command button (located at the bottom of the window) to cancel the installation the ASI-MV software application.

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/004.png)

### Completing the ASI-MV Setup Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: To exit the completing ASI-MV setup wizard click on the Finish command button (located at the bottom of the window).

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/005.png)

## VistA ASI-MV Interface Software Upgrade Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information provides step-by-step instructions for upgrading the existing VistA ASI-MV interface:

### IRM Staff:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

 \*IMPORTANT NOTE TO IRM: THIS PATCH MUST BE INSTALLED.  ALTHOUGH NO ROUTINES\*

 \*ARE INCLUDED IN THIS PATCH KIDS DELETES THE OPTION YS BROKER \[YS BROKER\] \*

 \*WHEN THE PATCH IS INSTALLED.                                             \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Step: 1. Add YS BROKER1 \[YS BROKER1\] to the MH Users secondary menu.

Step: 2. Delete the following three files from the asimv4 folder:

Example: C:\Program Files\asimv4

> YS50167_ASIMV.exe

> YS50167_SecureDesktop.exe

> YS50167_KeyboardHook.dll

Step: 3. From one of the following Office of Information Field Offices (OIFOs) Anonymous Software Directories retrieve and open the YS_501_78\_.ZIP file:

OIFO Anonymous Software Directories

<span class="mark">REDACTED</span>

FILE NAME CONTENTS RETRIEVAL FORMAT

YS_501_78.ZIP BINARY

\- YS_501_78_SETUP_1_0_3_10.EXE ASI-MV complete install for version 1.0.3.10 of the ASI-MV

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_ASIMV.EXE ASI-MV Interface Executable

\- YS_ASIMV_SD.EXE Secure Desktop Executable

\- YS_ASIMV_KH.DLL Keyboard Hook DLL used by Secure Desktop

-YS_ASIMV_IGUM.pdf YS_ASIMV Installation and User Guide

-YS_ASIMV_IGUM.doc YS_ASIMV Installation and User Guide

Step: 4. Copy the following three files to the asimv4 folder:

Example: C:\Program Files\asimv4

> YS_ASIMV.exe

> YS_ASIMV_SD.exe

> YS_ASIMV_KH.dll

Step 5: VistA MH ASI-MV Interface Software MUST NOW be started from the Computer Patient Record System (CPRS) Tools Menu.

How to add the VistA MH ASI-MV Interface menu entry to the VistA CPRS GUI Toolbar.

VistA MH ASI-MV Interface Software user-definable text will appear in the CPRS drop-down Tools Menu. This text represents the menu entry that the user MUST click on to invoke the VistA MH ASI-MV Interface Software.

C:\Progra~1\asimv4\ys_asimv.exe is the path where the VistA MH ASI-MV Interface Software executable can be found by default. If the path was changed during VistA MH ASI-MV Interface Software installation, this entry must be adjusted accordingly.

> **NOTE:** The tilde-abbreviated notation for the “Program Files” folder is necessary. If CPRS is unable to invoke VistA MH ASI-MV Interface Software, check for spaces in the folder path text and replace the tilde notation according to Windows standards.

s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF these are the five parameters passed by CPRS to VistA MH ASI-MV Interface Software. This section of the NAME=COMMAND line must be included verbatim. All five parameters must be present and they must be listed in the indicated sequence.

Example: Adding the VistA MH ASI-MV Interface menu to the VistA CPRS GUI Toolbar

\>D ^XUP \<Enter\>

Setting up programmer environment

Terminal Type set to: C-VT100 \<Enter\>

Select OPTION NAME: EVE \<Enter\>

1 EVE Systems Manager Menu

2 EVENT DELAYED ORDERS MENU OR DELAYED ORDERS Event Delayed Orders Menu

CHOOSE 1-2: 1 EVE Systems Manager Menu \<Enter\>

Taskman Management ...

DISK Disk Space Management ...

FM VA FileMan ...

HL7 HL7 Main Menu ...

Application Utilities ...

Capacity Management ...

Core Applications ...

Device Management ...

Information Security Officer Menu ...

Manage Mailman ...

Menu Management ...

Operations Management ...

Programmer Options ...

Spool Management ...

User Management ...

Select Systems Manager Menu Option: core Applications \<Enter\>

2000 User Menu for Pharmacy 2000 ...

2000 Pharmacy 2000 Manager Menu ...

AHJL PACKAGE TRACKING MENU ...

AMIE A.M.I.E. Medical Administration Menu ...

COP CHIEF POLICE MENU ...

DENT Dental ...

DUM Document Upload Manager ...

EWO EWO Electronic Work Requests ...

FH Dietetics Management ...

GMTS Health Summary Coordinator's Menu ...

IB Integrated Billing Master Menu ...

IV IV Menu ...

MAS MAS MANAGER ...

NDF National Drug File Menu ...

NRS Nursing System Manager's Menu ...

ODS ODS Supervisor Menu ...

RO A.M.I.E Regional Office Main Menu ...

TIU All TIU/USR Mgr Menus ...

WS Automatic Replenishment ...

ZLBL Transaction & Record Information Menu ...

2NE Policy editing

ADP MENU ...

Career Center Menu ...

Chaplain Menu ...

Communications Menu ...

CPRS Manager Menu ...

Day Hospital Menu ...

Dietetics Roster

Display Lab Tests and Results for Clozapine order

Employee Inquiry Menu ...

Employee Inquiry/Reports Menu ...

Engineering Main Menu ...

Enter/Edit/Print Psych Triage

Environnemental Management Menu ...

Fee Service Menu ...

Generic Code Sheet Menu ...

Health Summary Maintenance Menu ...

IFCAP ...

KB SQL

Lab Coordinator Menu ...

Lab Menu ...

List of Override Prescriptions

MAS Admissions Menu ...

Medical Records Menu ...

Medicine Menu ...

Mental Health ...

MHS Manager ...

Occurrence Screening Menu ...

Outpatient Pharmacy Manager ...

Patient Funds (INTEGRATED) System ...

Psychology Menu ...

Rad/Nuc Med Total System Menu ...

Record Tracking Total System Menu ...

Remote Order/Entry System ASPS Menu ...

Seriously Ill list

Social Work Menu ...

Surgery Menu ...

Utilization Management Rollup Main Menu ...

VIST Menu ...

Volunteer Timekeeping Activity ...

Select Core Applications Option: cprs Manager Menu \<Enter\>

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

TOOL General Parameter Tools ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select CPRS Manager Menu Option: pe CPRS Configuration (Clin Coord) \<Enter\>

AL Allocate OE/RR Security Keys

KK Check for Multiple Keys

DC Edit DC Reasons

GP GUI Parameters ...

GA GUI Access - Tabs, RPL

MI Miscellaneous Parameters

NO Notification Mgmt Menu ...

OC Order Checking Mgmt Menu ...

MM Order Menu Management ...

LI Patient List Mgmt Menu ...

FP Print Formats

PR Print/Report Parameters ...

RE Release/Cancel Delayed Orders

US Unsigned orders search

EX Set Unsigned Orders View on Exit

NA Search orders by Nature or Status

DO Event Delayed Orders Menu ...

PM Performance Monitor Report

Select CPRS Configuration (Clin Coord) Option: gp GUI Parameters \<Enter\>

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select GUI Parameters Option: tm GUI Tool Menu Items\<ENTER\>

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[LOMA-LINDA.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 1User NEW PERSON \<Enter\>

Select NEW PERSON NAME: MHUser, One \<Enter\>

----------- Setting CPRS GUI Tools Menu for User: MHUser, One -----------

Select 1: 4 \<Enter\>

Are you adding 4 as a new 1? Yes//\<Enter\> YES

1: 4//\<Enter\> 4

Value: ASI-MV=C:\Progra~1\asimv4\ys_asimv.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

Select 1:

Step 6. Add YOUR SITE to the entries in your HOSTS FILE:

> A. Search for a TEXT file named HOSTS (that is right, no filename extender). This file is typically found in c:\WINNT\system32\drivers\etc. Search for it using HOSTS.

> B. Open the HOSTS FILE and append the entry USING NOTEPAD:

Example:Your Site’s IP Address Site Name Port

10.4.229.28 Bay Pines 9200

> C. Save HOSTS FILE changes.

Step 7. Place the VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Patch YS\*5.01\*78 Installation and User Guide (YS_ASIMV_IGUM.DOC and YS_ASIMV_IGUM.PDF) in a location that is accessible by MH ASI-MV users.

VistA MENTAL HEALTH (MH) ADDICTION SEVERITYY INDEX MULTIMEDIA VERSION (ASI-MV)

PATCH YS\*5.01\*78 USER GUIDE

# VistA Mental Health Addiction Severity Index Multimedia Version (ASI-MV) Patch YS\*5.01\*78 User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Mental Health ASI-MV User Guide section provides detailed instructions for using the VistA MH ASI- MV software. The software is a combined multimedia product used by clinicians for entering patient demographics and patient self-administered ASI-MV interviews. The software utilizes video and audio technology to simulate an ASI-MV interview. The patient is guided through a series of ASI-MV interview screens throughout the interview session, during which, a patient respond to questions presented on the ASI-MV interview screens. The ASI-MV interview screens require clinicians and patients to use a mouse-driven PC for entering demographics and self-administered MH ASI-MV interviews.

Demographics and ASI-MV interviews are automatically stored on the PC Workstation when the ENTIRE ASI-MV interview is completed. When the ASI-MV software is executed again, demographics and self-administered ASI-MV interviews are saved automatically to the V*ist*A database.

> **NOTE:** If an ASI-MV interview is not ENTIRELY completed, data will not be stored on the PC workstation. Therefore, the ASI-MV interview will need to be repeated.

After the demographics and ASI-MV interview data has been saved to the VistA MH database, clinician can review and print itemized and narrative reports, composite score summaries and utilization reports using the familiar Mental Health assistant (GUI) and the VistA MH roll-and-scroll screens.

### Starting MH ASI-MV Patch YS\*5.01\*78 Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information provides detailed instructions including screen displays to assist clinicians and patients with administering the new ASI-MV interviews.

#### Clinician:

#### Retrieve COTS ASI-MV CD-ROM

1.  Retrieve the COTS ASI-MV CD-ROM and (optional) headphones from a secure storage area.

> **NOTE:** It is recommended that the COTS ASI-MV CD-ROM and (optional) headphones be stored safely away from the PC Workstation when not in use.

#### Start COTS ASI-MV CD-ROM

2.  Insert the COTS ASI-MV CD-ROM into the PC Workstation CD-ROM player.

#### Start Computer Patient Record System (CPRS)

3\. Start CPRS by clicking the CPRS icon.

Example: CPRS icon

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/006.png)

#### Choosing a VistA Server:

4\. Select the VistA server you wish to use.

> **NOTE:** If your PC Workstation is configured to interact with more than one VistA server, you will be prompted to select a server from a list of servers. However, most PC Workstations are not set up this way. Therefore, you may never see the following VistA Server Screen example.

Example: VistA Server Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/007.png)

#### VistA Application Sign-on:

5\. Use the standard VistA Access and Verify Code sign-on procedures to access the VistA software application.

Example: VistA Sign-on Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/008.png)

#### VistA CPRS Cover Sheet Screen

6\. The Tools menu allows you to quickly access the ASI-MV. The ASI-MV menu option allows the clinician to set up their desktop for use by the patient.

> To start the ASI-MV:

> 1\. Select Tools then ASI-MV.

Example: This is an example of the VistA CPRS Cover Sheet Screen.

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/009.png)

#### Choosing Program Types

7\. If necessary, click on the “Choose program type” and the “ASI ordered by” buttons and scroll down the list to make a different selection.

> **NOTE:** Patient selected via CPRS is indicated on the bottom-left of the VistA ASI-MV Interface form. If the displayed patient name is incorrect, return to the CPRS window and select the correct patient name in CPRS. ASI-MV will be updated to synchronize with the patient selected in CPRS. After the selections are made, click the “Start new ASI” tab to advance to the next screen.

The selection examples displayed are default values from the previous interview.

Example: VistA ASI-MV Interface Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/010.png)

#### ASI-MV Interface Security Warning \#1

8\. This screen addresses the security actions that will take place when the user clicks on the “YES” button to continue. If the user clicks on the “Cancel” button you will be exited to the last application you were executing on your Desktop.

NOTES:

Place the keyboard in a position or location where the patient will NOT accidentally cause a keyboard key press.

Each “accidental” keystroke will activate a screensaver, after a brief pause the workstation becomes locked, requiring the re-enter of the password to regain access.

A maximum of 10 “accidental” keystrokes are allowed, on the 11<sup>th</sup> keystroke, the ASI-MV interview session is terminated and logged off.

Example: ASI-MV Interface Security Warning \#1 Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/011.png)

#### ASI-MV Interface Security Warning \#2

9\. This screen instructs the user on what to do with the Desktop’s keyboard from this point on. Click on the “OK” button to continue.

Example: ASI-MV Interface Security Warning \#2 Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/012.png)

#### ASI-MV Access Screen

10\. You MUST enter the following administrator password (1235) by CLICKING on the numbers located on ASI-MV Screen (i.e., typing in the password numbers are not allowed). Once the password is entered, click on the “Enter” button to advance to the next screen.

Example: ASI-MV Administrator Password Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/013.png)  
<span id="_Toc87744377" class="anchor"></span><u>Starting the ASI-MV Screen</u>

11\. Click on the “Run ASI-MV” button to advance to the next screen.

> **NOTE:** Click on the “Purchase More ASI-MV Uses” button to purchase more ASI-MV license uses for the PC workstation.

Example: ASI-MV Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/014.png)

#### ASI-MV Interview Screen

12\. Clinician, this is a good time to instruct the patient on the following functions of the self-administered ASI-MV interview session. From this point on the patient will <u>self-administer</u> the ASI-MV interview.

- Place the keyboard in a position or location where the patient will NOT accidentally cause a keyboard key press.
- Demonstrate to the patient how to correctly use the mouse.
- Give the patient a brief description of the self-administered ASI-MV Interview session
- On the first screen of the self-administered ASI-MV Interview, when the multimedia characters begin to speak, ask the patient to adjust the speaker or headphone’s volume to a comfortable level.

Example: ASI-MV Interview Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/015.png)  
<span id="_Toc87744379" class="anchor"></span>Patient:

#### Patient Begin ASI interview

13\. To begin the ASI interview “Click Screen to Start”

Example: Addiction Severity Index Multimedia Version screen.

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/016.png)

> **NOTE:** When the self-administered ASI-MV interview is <u>totally</u> completed by the patient, the interview session will end automatically. The ASI-MV interview data is <u>temporarily</u> stored on the PC workstation until the ASI-MV software is accessed again.

#### Saving the ASI-MV Interview Data

14\. Launch CPRS, choose a patient, and launch ASI-MV from the CPRS GUI toolbar to automatically save the previously administered interview data to the VistA MH database.

NOTES:

The “Processing” screen will <u>immediately</u> appear displaying “Saving data to VistA. Please wait…” Saving the data is an automatic process requiring NO user interaction. Please DO NOT use the computer while the “Processing” screen is displayed.

When previously administered ASI-MV data has already been uploaded, the “Processing” screen will NOT appear.

Example: Processing screen - Saving Data to VistA

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/017.png)

### ASIMV Error Incomplete File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ValErrors.txt is a file used by the developer to debug the Vista ASI-MV Interface program. It exists so that IRM staff is able to relay malfunction information to the developers. This file is not for use by End Users.

Example: ASIMV Errors Screen

![](ys-5-01-78-mh-addiction-severity-index-multimedia-version-installation-and-user-/018.png)