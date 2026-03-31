---
title: PSB*3*70 BCMA Clinic Orders, High Risk, etc T@Project Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: BCMA Clinic Orders, High Risk, etc T@Project Install Guide
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*70
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Bar Code Medication Administration (BCMA) Clinic Orders, High Risk High Alert Drugs, IV Bag Logic, and T@0 project.
audience: 
keywords: 
  - install
  - table
  - contents
  - installation
  - bcma
  - patch
  - want
  - backup
  - software
  - options
page_count: 0
word_count: 3725
section_count: 19
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p70_imr6_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p70_imr6_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-install-guide/001.png)

BCMA Clinic Orders, High Risk/High Alert Drugs, IV Bag Logic, T@0 ProjectINSTALLATION GUIDE

PSB\*3\*70

PSJ\*5\*279

PSS\*1\*172

OR\*3\*266

December 2013

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Purpose](#purpose)
- [Scope](#scope)
- [Before You Begin](#before-you-begin)
- [Section 1: Pre-Installation](#section-1-pre-installation)
  - [User Interfaces](#user-interfaces)
  - [## Hardware Interfaces](#hardware-interfaces)
  - [Software Interfaces](#software-interfaces)
  - [Communication Interfaces](#communication-interfaces)
  - [User Characteristics](#user-characteristics)
  - [Acronyms](#acronyms)
  - [Dependencies and Constraints](#dependencies-and-constraints)
  - [N/A](#na)
  - [BCMA Backup System (BCBU)](#bcma-backup-system-bcbu)
  - [# Section 2: Installation of Patches](#section-2-installation-of-patches)
  - [Installing PSS\1\172](#installing-pss1172)
  - [Installing OR\3\266](#installing-or3266)
  - [Installing PSJ\5\279](#installing-psj5279)
  - [## Installing PSB\3\70](#installing-psb370)
  - [# Section 3: Backing out of Patches](#section-3-backing-out-of-patches)
  - [Backing out BCMA GUI Patch (PSB\3\70)](#backing-out-bcma-gui-patch-psb370)
  - [## Backing out VistA Patches\ (PSB\3\70, PSJ\5\279, PSS\1\172, and OR\3\266)](#backing-out-vista-patches-psb370-psj5279-pss1172-and-or3266)
  - [This procedure assumes that a backup copy of the routines was made during the installation process.](#this-procedure-assumes-that-a-backup-copy-of-the-routines-was-made-during-the-installation-process)
- [Section 4: Documentation](#section-4-documentation)
|          |              |                  |                                    |
|----------|--------------|------------------|------------------------------------|
| Date | Revision | Description  | Author                         |
| 12/13    | 1.0          | Original Version | <span class="mark">REDACTED</span> |
*(This page included for two-sided copying.)*Table of Contents
*  
(This page included for two-sided copying.)*

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Bar Code Medication Administration (BCMA) Clinic Orders, High Risk High Alert Drugs, IV Bag Logic, and T@0 project.

The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing patches, and BCMA and Inpatient Medications staff responsible for maintaining the pharmacy files.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA and Inpatient Medications applications were modified to allow for the following:

- Clinic Orders enhancement. This enhancement modifies Inpatient Medications and BCMA to allow the administration of Clinic order medications. Clinic orders will be processed via BCMA Client GUI by displaying these orders on the Virtual Due List (VDL) and Coversheet screens. The VDL & Coversheet screens will display in either one of two modes, Inpatient Medications (IM) Order mode or the new Clinic Order (CO) mode. This enhancement will resolve portions of NSR 20070506: Clinic Orders.
- Witness for High Risk/High Alert Drugs enhancement. This enhancement modifies BCMA and Pharmacy Data Management to prompt for witness sign-on to complete the administration in BCMA of an order that involves an Orderable Item that is flagged as a High Risk/High Alert Drug requiring or recommending a witness for administration. This enhancement will resolve NSR 20070607: Witness Function for High Risk/High Alert Medications.
- Modify IV Bag Logic enhancement. This enhancement modifies the Inpatient Medications order entry process to check the BCMA IV parameters against any edits to an IV order. When the Pharmacist is verifying an IV order in Inpatient Medications, the logic compares the changes in the original order to the IV parameter settings in BCMA, to determine if the bags are still valid. If there are invalid bags, the system displays a list of the invalid bag numbers, along with a message to the Pharmacist. This enables the pharmacist to proactively retrieve the invalid bags and send the replacement bags. The user is not allowed to reprint the old labels for the invalid bag numbers. The user may reprint the new labels for the replacement bags. Local site policy determines the process for managing the bags. This enhancement resolves a portion of NSR 20010504: Check for invalid bags; prompt pharmacist to print new labels.

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-install-guide/002.png)

# Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is organized into four major sections: “Pre-Installation,” “Installation of Patches,” “Backing out of Patches,” and Documentation.

Having the proper setup of parameters and settings is critical to the success of the implementation.

# Section 1: Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information that helps you determine patch and system requirements before installing the patches that are included in this project. It also helps you understand the updates that the installation process makes. Additionally, descriptions are provided regarding the specific parameters that you must set up to implement the interface.

## User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinicians interface with Inpatient Medications using personal computers. Inpatient Medications is compatible with the standard software and hardware platforms outlined in Hardware and Software Detailed Design.

Clinicians interface with BCMA using PCs and bar code scanners at the patient’s point of care. BCMA uses bar code technology – compatible with the standard software and hardware platforms outlined in Hardware and Software Detailed Design.

## ## Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Personal computers (PCs) and bar code readers are used at the patient point of care. BCMA is bar code technology-compatible with the standard hardware and software platforms outlined in this section and in Software Detailed Design.

The bar code scanner must interface with the PC in a way that is transparent to the Microsoft (MS) Windows operating system. This means that when a bar code is scanned, the value in the bar code will be, to the operating system, as if the value had been typed on the keyboard. The scanner installation must not require modification to the MS Windows-based application (in this case, BCMA) that will use the scanner.

Inpatient Medications functions on the following standard server platforms used in VAMCs:

Open M V. 4.0 route 43 and MS Windows 7, 2000, NT, XP and VMS

BCMA functions on the following standard server platforms used in VAMCs:

Digital Equipment Corporation’s Standard M V. 6.3<sup>+</sup> and VMS V. 6.1<sup>+</sup>

Open M V. 4.0 route 43 and MS Windows 7, 2000, NT, XP and VMS

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA requires the following versions (or higher) of VA software packages for proper implementation. The software listed is not included in this build and must be installed for the build to be completely functional. Resource and Patient Management System (RPMS) uses the same version numbers as VistA.

| Package              | Version |
|--------------------------|-------------|
| Inpatient Medications    | 5.0         |
| Kernel                   | 8.0         |
| MailMan                  | 8.0         |
| Nursing                  | 4.0         |
| CPRS                     | 1.0         |
| Pharmacy Data Management | 1.0         |
| RPC Broker (32-bit)      | 1.1         |
| Toolkit                  | 7.3         |
| VA FileMan               | 22.0        |
| Vitals/Measurements      | 5.0         |

ICR 2828, 2829, 2830, and 5763 are used to allow BCMA to gain access to Inpatient Medications Pharmacy Software to provide specific information for displaying on BCMA Reports.

ICR 10035 is used to allow BCMA to gain access to Registrations Software to provide specific information for displaying on BCMA reports.

## Communication Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications – N/A

BCMA - The Shared RPC Broker uses TCP/IP to communicate with the VistA server. It requires a minimum of 10 Mbps (Megabits per second) throughput on the network connection. VistA electronic mail is used to send notifications to a site-defined mail group.

The Shared RPC Broker patch XWB\*1.1\*29 must be installed prior to running BCMA.  The Shared RPC Broker supports communication between BCMA and the BcmaOrderCom.DLL which is used by the CPRS Med Order Button.  The Shared RPC Broker installation can be found on the RPC Broker Archive page <span class="mark">REDACTED</span>.

The installation is found in the following link: <span class="mark">REDACTED</span>.

The Shared RPC Broker Installation Guide is found in the following link: <span class="mark">REDACTED</span>.

## User Characteristics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users for this application include clinicians who are responsible for administering active medication orders to “inpatients” at Veterans Affairs Medical Centers (VAMCs).

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                 |
|-------|-----------------------------------------------------------------|
| Term  | Definition                                                      |
| BCMA  | Bar Code Medication Administration                              |
| CHUI  | Character-based User Interface                                  |
| CPRS  | Computerized Patient Record System                              |
| DBIA  | Data Base Integration Agreement                                 |
| EPS   | Enterprise Product Support                                      |
| GUI   | Graphical User Interface                                        |
| HSD&D | Health Systems Design and Development                           |
| NCPS  | National Center for Patient Safety                              |
| PBM   | Pharmacy Benefits Management                                    |
| SDS   | Systems Development Support                                     |
| SQA   | Software Quality Assurance                                      |
| SRS   | Software Requirements Specification                             |
| VAMC  | Department of Veterans Administration Medical Center            |
| VHA   | Veterans Health Administration                                  |
| VHIT  | Veterans Health Information Technology                          |
| VistA | Veterans Health Information Systems and Technology Architecture |
| ICR   | Interface Control Registrations                                 |

## Dependencies and Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## N/A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## BCMA Backup System (BCBU) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA patch PSB\*3\*70 does not provide contingency backup for Clinic Orders.  PSB\*3\*73 has been developed so that the Class 1 Bar Code Back Up (BCBU) will include Clinic Orders. This patch is currently in test and is expected to be released in the next month.  If you have questions please file a REMEDY ticket.

## # Section 2: Installation of Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation is comprised of PSB\*3\*70, PSJ\*5\*279, and PSS\*1\*172, and OR\*3\*266. Please read the following installation instructions carefully before beginning the installation.

Patches should be installed in the following order:

- PSS\*1\*172
- OR\*3\*266
- PSJ\*5\*279
- PSB\*3\*70

## Installing PSS\*1\*172

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Post Install routine EN^PSS172PO checks for the existence of the "NO ALLERGY ASSESSMENT" entry in the APSP INTERVENTION TYPE (#9009032.3) file, and for the existence of the "UNABLE TO ASSESS" entry in the APSP INTERVENTION RECOMMENDATION (#9009032.5) file. If either entry does not exist, it is added at the first available Internal Entry Number (IEN) in the file.

These file entries were originally exported by patch PSJ\*5\*267, but could not be added to the files at sites that contained custom entries in the files.

Do not queue this patch to install at a later time nor install this patch while users are on the system. Installation will take no longer than 5 minutes for the software components.

To install PSS\*1\*172

1.  Choose the PackMan message containing this patch.
2.  Choose the *INSTALL/CHECK MESSAGE* PackMan option.
3.  From the *Kernel Installation and Distribution System* (KIDS) menu, select the Installation menu.
4.  From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter PSS\*1.0\*172:
1.  *Backup a Transport Global -* This option will create a backup message of any routines exported with this patch. It will NOT backup any other changes such as DD's or templates.
2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  *Verify Checksums in Transport Global -* This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter PSS\*1.0\*172.
6.  When prompted “Want *KIDS* to Rebuild Menu Trees Upon Completion of Install? YES//”, accept the default of YES.
7.  When prompted “Want *KIDS* to INHIBIT LOGONs during the install? NO//” respond NO.
8.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//” respond NO.
9.  If prompted "Delay Install (Minutes): (0 - 60): 0// respond 0.

Example of PSS\*1\*172 Installation

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSS\*1.0\*172 4/12/13@09:23:30

=\> Copy of: PSS\*1\*172

This Distribution was loaded on Apr 12, 2013@09:23:30 with header of

Copy of: PSS\*1\*172

It consisted of the following Install(s):

PSS\*1.0\*172

Checking Install for Package PSS\*1.0\*172

Install Questions for PSS\*1.0\*172

Incoming Files:

50.7 PHARMACY ORDERABLE ITEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY ORDERABLE ITEM' File.

53.47 INFUSION INSTRUCTIONS

> **NOTE:** You already have the 'INFUSION INSTRUCTIONS' File.

55 PHARMACY PATIENT

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

Rebuilding Menus



ZZ TRAINING MENU Training Menu 30 08/29/96 04/12/13

TIU MAIN MENU MRT Text Integration Utilitie... 2 02/07/95 04/12/13

TIU MAIN MENU MGR Text Integration Utilitie... 1 11/01/94 04/12/13

TIU MAIN MENU TRANSCRIPTION

Text Integration Utilitie... 1 09/11/96 04/12/13

TIU MAIN MENU REMOTE USER

Text Integration Utilitie... 1 02/27/95 04/12/13

TIU MAIN MENU PN CLINICIAN

Progress Notes User Menu 1 04/12/13

TIU MAIN MENU CLINICIAN

Progress Notes/Discharge ... 1 03/11/94 04/12/13

PSB BCBU WRKSTN MAINBCMA Backup System (Wrkstn) 5 08/07/12 04/12/13

Building secondary menu trees....

Merging.... done.

Menu Rebuild Complete: Apr 12, 2013@09:24:54





100%  25 50 75 

Complete 

Install Completed

## Installing OR\*3\*266

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not queue this patch to install at a later time nor install this patch while users are on the system. Installation will take no longer than 5 minutes for the software components.

To install OR\*3\*266

1.  Choose the PackMan message containing this patch.
2.  Choose the *INSTALL/CHECK MESSAGE* PackMan option.
3.  From the *Kernel Installation and Distribution System* (KIDS) menu, select the Installation menu.
4.  From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter OR\*3.0\*266:
1.  *Backup a Transport Global -* This option will create a backup message of any routines exported with this patch. It will NOT backup any other changes such as DD's or templates*.*
2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  *Verify Checksums in Transport Global -* This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter OR\*3.0\*266.
6.  When prompted “Want *KIDS* to INHIBIT LOGONs during the install? NO//” respond NO.
7.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//” respond NO.
8.  If prompted "Delay Install (Minutes): (0 - 60): 0// respond 0.

Example of OR\*3\*266 Installation

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: OR\*3.0\*266 4/12/13@09:48:50

=\> Copy of: OR\*3\*266

This Distribution was loaded on Apr 12, 2013@09:48:50 with header of

Copy of: OR\*3\*266

It consisted of the following Install(s):

OR\*3.0\*266

Checking Install for Package OR\*3.0\*266

Install Questions for OR\*3.0\*266

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

OR\*3.0\*266



Install Started for OR\*3.0\*266 :

Apr 12, 2013@09:49:03

Build Distribution Date: Sep 12, 2012

Installing Routines:

Apr 12, 2013@09:49:03

Updating Routine file...

Updating KIDS files...

OR\*3.0\*266 Installed.

Apr 12, 2013@09:49:03

Not a production UCI

NO Install Message sent





100%  25 50 75 

Complete 

Install Completed

## Installing PSJ\*5\*279

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **REMINDER:** Do NOT queue this patch to install at a later time.

Verify users are logged off the Inpatient Medications V. 5.0 application. This patch should take less than 5 minutes to install.

To install PSJ\*5\*279

1.  Choose the PackMan message containing this patch.
2.  Choose the *INSTALL/CHECK MESSAGE* PackMan option.
3.  From the *Kernel Installation and Distribution System* (KIDS) Menu, select the Installation Menu.
4.  From this menu, you may elect to use the following options. When prompted for the INSTALL enter PSJ\*5.0\*279.
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
6.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', accept the default, 'NO'.
7.  When prompted “Enter the Coordinator for Mail Group ‘PSJ CLINIC DEFINITION”, enter the name of the person responsible for maintaining membership in pharmacy mail groups.
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', accept the default, 'NO'.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', enter 'NO'.
10. If prompted "Delay Install (Minutes): (0 - 60): 0// respond 0.

Example of PSJ\*5\*279 Installation

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSJ\*5.0\*279 4/12/13@09:19:17

=\> PSJ\*5\*279

This Distribution was loaded on Apr 12, 2013@09:19:17 with header of

PSJ\*5\*279

It consisted of the following Install(s):

PSJ\*5.0\*279

Checking Install for Package PSJ\*5.0\*279

Install Questions for PSJ\*5.0\*279

Incoming Files:

53.1 NON-VERIFIED ORDERS (Partial Definition)

> **NOTE:** You already have the 'NON-VERIFIED ORDERS' File.

53.46 CLINIC DEFINITION (Partial Definition)

> **NOTE:** You already have the 'CLINIC DEFINITION' File.

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'PSJ CLINIC DEFINITION': COORDINATOR,NAME//

NC

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

PSJ\*5.0\*279



PSGXR314

PSGXR32

PSGXR33

PSGXR34

PSGXR35

PSGXR36

PSGXR37

PSGXR38

PSGXR39

Updating KIDS files...

PSJ\*5.0\*279 Installed.

Apr 12, 2013@09:19:42

Not a production UCI

NO Install Message sent





100%  25 50 75 

Complete 

Install Completed

## ## Installing PSB\*3\*70

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software distribution includes these modified files:

| File Name | Description        | File Version | Bytes | Checksum |
|---------------|------------------------|------------------|-----------|--------------|
| BCMA.CHM      | Client Help File       |                  | 1,065 KB  | n/a          |
| BCMA.EXE      | Client                 | 3.0.70.65        | 2,623 KB  | n/a          |
| BCMAPar.CHM   | Parameters Client Help |                  | 143 KB    | n/a          |
| BCMApar.EXE   | Parameters Client      | 3.0.70.9         | 1.066 KB  | n/a          |

1.  Prior client compatible with patch: NO
2.  Client can be copied instead of installed: YES
3.  Is your site running the CareFusion Wireless Medication Administration (WMA) software? If YES, please contact CareFusion to ensure your site has the latest compatible WMA patch.

> **NOTE:** Use Binary mode to retrieve the .EXE file.

To obtain the updated .EXE, use FTP to retrieve PSB3_0P70.EXE (5,003 KB) from one of the following OI Field Offices' ANONYMOUS.SOFTWARE directories:

| OI Field Office                | FTP Address                    | Directory                      |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

If BCMA is currently running, please exit BCMA. This client installation patch file can be used to upgrade an existing version of BCMA, or can be used for a brand new installation.

1.  Double Click on PSB3_0P70.EXE which will launch the InstallShield Wizard.
2.  When the InstallShield Wizard Welcome screen is displayed, click "Next."
3.  On the Choose Destination Location screen, simply click "Next" If you would like to change the destination folder to one other than default, click "Browse" to navigate to the folder of your choice. Click "Next."
4.  On the "Setup Type" Screen select one of the following:

a\. Typical - installs only the BCMA client program which is necessary for medication administration.

b\. Complete - installs the BCMA client and the GUI BCMA Site Parameters definition program.

c\. Custom - allows you to select which programs to install. Typical is selected by default. Click Next."

5.  The InstallShield Wizard Ready to Install the Program screen will display. Click "Install" to proceed with the installation.
6.  The InstallShield Wizard Complete screen will be displayed. Click "Finish" and the BCMA installation is now complete.

  
To install PSB\*3\*70:

Do not queue this patch to install at a later time nor install this patch while BCMA users are on the system. Installation will take no longer than 5 minutes for the software components and new division parameter.

1.  Choose the *PackMan* message containing this patch.
2.  Choose the *‘INSTALL/CHECK MESSAGE’* PackMan option.
3.  From the *Kernel Installation and Distribution System* (KIDS) menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL enter the patch PSB\*3.0\*70:
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter PSB\*3.0\*70.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' respond YES.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' respond NO.
8.  If prompted "Delay Install (Minutes): (0 - 60): 0// respond 0.

Example of PSB\*3\*70 Installation

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSB\*3.0\*70 4/11/13@15:49:40

=\> PSB\*3\*70

This Distribution was loaded on Apr 11, 2013@15:49:40 with header of

PSB\*3\*70

It consisted of the following Install(s):

PSB\*3.0\*70

Checking Install for Package PSB\*3.0\*70

Install Questions for PSB\*3.0\*70

Incoming Files:

53.68 BCMA MISSING DOSE REQUEST (Partial Definition)

> **NOTE:** You already have the 'BCMA MISSING DOSE REQUEST' File.

53.69 BCMA REPORT REQUEST (Partial Definition)

> **NOTE:** You already have the 'BCMA REPORT REQUEST' File.

53.79 BCMA MEDICATION LOG (Partial Definition)

> **NOTE:** You already have the 'BCMA MEDICATION LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

Rebuilding Menus



ZZ TRAINING MENU Training Menu 30 08/29/96 04/11/13

TIU MAIN MENU MRT Text Integration Utilitie... 2 02/07/95 04/11/13

TIU MAIN MENU MGR Text Integration Utilitie... 1 11/01/94 04/11/13

TIU MAIN MENU TRANSCRIPTION

Text Integration Utilitie... 1 09/11/96 04/11/13

TIU MAIN MENU REMOTE USER

Text Integration Utilitie... 1 02/27/95 04/11/13

TIU MAIN MENU PN CLINICIAN

Progress Notes User Menu 1 04/11/13

TIU MAIN MENU CLINICIAN

Progress Notes/Discharge ... 1 03/11/94 04/11/13

PSB BCBU WRKSTN MAINBCMA Backup System (Wrkstn) 5 08/07/12 04/11/13

Building secondary menu trees....

Merging.... done.

Menu Rebuild Complete: Apr 11, 2013@15:50:51





100%  25 50 75 

Complete 

Install Completed

## # Section 3: Backing out of Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Backing out BCMA GUI Patch (PSB\*3\*70)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From Control Panel, select Programs and Features, select BCMA (PSB\*3\*70), and select Uninstall from the right-click menu.
2.  Install previous version of BCMA from the VistA FTP site at <span class="mark">REDACTED</span>.

Detailed instructions on installation steps are outlined in this Installation Guide.

## ## Backing out VistA Patches\* (PSB\*3\*70, PSJ\*5\*279, PSS\*1\*172, and OR\*3\*266)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This procedure assumes that a backup copy of the routines was made during the installation process.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only routines are backed-up; other components such as DDs, templates, protocols, options or HL7 components are not backed up.

1.  To back out the patches, restore the backup copy saved in the MailMan message. This action will restore the routines to their state prior to installing the IMR 6 patches.

\* VistA patches include the PSB\*3\*70 M patch. 

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-install-guide/003.png)Note: In order to completely back out all components, development will make a patch available for each package that will restore non-routine components to their pre-IMR 6 state.

# Section 4: Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by these patches is available.

The preferred method to retrieve documentation is to FTP the files from <span class="mark">REDACTED</span>. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| OI Field Office                | Server                         |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The documentation is in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library (VDL) at: http://www.va.gov/vdl/.

See the Release Notes for each patch for a complete listing of the documentation and associated file names.