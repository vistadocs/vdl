---
title: ACKQ*3*13 QUASAR Audiogram Module Install/Implement Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: QUASAR Audiogram Module Install/Implement Guide
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3*13
group_key: "ACKQ:ACKQ:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - installation
  - table
  - contents
  - class
  - audiogram
  - install
  - ackq
  - vista
  - strong
  - quasar
page_count: 0
word_count: 3496
section_count: 11
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0p13_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0p13_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

![](ackq-3-13-quasar-audiogram-module-install-implement-guide/001.png)

QUASAR Audiogram Module  
Installation and Implementation Guide

Patch ACKQ\*3.0\*13

July 2007

Health Systems Design & Development

Table of Contents

*This page intentionally left blank for double-sided printing.*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Documentation](#related-documentation)
- [Pre-installation Considerations](#pre-installation-considerations)
  - [M Server Requirements](#m-server-requirements)
  - [Client Requirements](#client-requirements)
    - [Desktop Minimums](#desktop-minimums)
    - [PC Hardware Minimums](#pc-hardware-minimums)
    - [Monitor/Keyboard Placement](#monitorkeyboard-placement)
- [Installation](#installation)
  - [Pre-installation Instructions](#pre-installation-instructions)
  - [M Server Installation](#m-server-installation)
  - [Client (GUI) Installation](#client-gui-installation)
    - [Client Server](#client-server)
    - [Client Workstation](#client-workstation)
- [Customizing the Client Installation](#customizing-the-client-installation)
  - [Assign ACKQROES3E Option to Users and Selected Staff](#assign-ackqroes3e-option-to-users-and-selected-staff)
  - [Adding Audiogram Edit to CPRS Tools](#adding-audiogram-edit-to-cprs-tools)
- [Post-installation Considerations](#post-installation-considerations)
  - [Vendor Installation Wizard](#vendor-installation-wizard)
  - [Audiogram Display through CPRS](#audiogram-display-through-cprs)
- [Glossary](#glossary)
- [Index](#index)
QUASAR (Quality: Audiology and Speech Analysis and Reporting) is a VistA software package written for the Audiology and Speech Pathology Service (ASPS). QUASAR is used to enter, edit, and retrieve data for each audiometric exam of a patient and provides for the transmission of this data to various programs.
Patch ACKQ\*3.0\*13 adds the ability to retrieve data directly from certain audiometric devices, and combines the Edit and Display components into one application. Recommended users (not doing data entry or capture), can use the Graph Display tab to view a graphic display of a record.
The QUASAR Audiogram Module is a Windows-based GUI interface, developed to simplify and enhance the entry, display, and use of information obtained during an audiometric exam of a patient.
The Audiogram Edit component (ACKQROES3E.exe) is a Windows-based software application that allows clinicians to enter, edit, and view a patient's audiometric exam record and a patient's audiogram graph. You access the component from the Computerized Patient Record System (CPRS) Tools menu.
The QUASAR Audiogram Module includes components that reside on two systems: the local facility VistA system and the Denver Acquisition & Logistics Center (Denver ALC) system. The local facility components include a VistA file, 'M' routines and options, remote procedure calls, and a Delphi executable. The Denver ALC ROES\*3.0 (Remote Order Entry System) order processing application incorporates patient-specific audiometric information that is taken from data transmitted to a national database from the QUASAR Audiogram Module. The information is used by vendors to produce customized hearing related items.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Related documentation is located in the VistA Document Library:

<http://www.va.gov/vdl/>

*QUASAR Audiogram Module Release Notes* for Patch ACKQ\* 3.0\*13

*QUASAR Audiogram Module Technical Manual and Package Security Guide* for Patch ACKQ\* 3.0\*13

*QUASAR Package User Manual* for Patch ACKQ\* 3.0\*13

*This page intentionally left blank for double-sided printing.*

# Pre-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following packages and patches must be installed and fully patched for the installation environment.

1.  VA FileMan V.22 or greater.
2.  Kernel V.8.0 or greater.
3.  Kernel Toolkit V.7.3 or greater.
4.  Kernel RPC Broker V.1.1 or greater.
5.  Patch ACKQ\*3.0\*12 must be installed prior to installing Patch ACKQ\*3.0\*13.

Each site’s system requires configuration.

1.  The VistA Server must be running the VistA Broker listener.
6.  The VistA Broker client must be installed and functional on the end user’s desktop system.
7.  The VistA system must have VA MailMan connectivity to the Denver ALC (that is, DDC.VA.GOV domain open), in order to transmit the audiometric data to the Denver ALC.

## Client Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Desktop Minimums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A system with the following specifications can provide the functionality necessary for this application.

|                   |                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------|
| Specification | Recommended Minimum                                                                         |
| Processor         | 200 MHz                                                                                         |
| Memory            | 64 MB                                                                                           |
| Hard Drive        | 4GB                                                                                             |
| Video             | AGP 2x w/4MB                                                                                    |
| CD-ROM            | 8x                                                                                              |
| Monitor           | 17" VGA, .28 pixel resolution                                                                   |
| LAN Interface     | 10/100 Mbps Ethernet                                                                            |
| Keyboard          | 101 -key                                                                                        |
| Mouse             | Microsoft Compatible                                                                            |
| Operating System  | The end user's desktop system must be running a Windows operating system (WinNT, Win2K, WinXP). |

- The VA Assistant Secretary for Information and Technology established a set of minimum configurations for new procurement of desktop systems across the enterprise (VA Directive 6401).
- The VA minimum baseline exceeds the recommended minimum for this application and applies to most of the specifications listed above. The specifications are provided for use with existing equipment, if necessary.
- Each facility is advised to consider the specifications mandated by Directive 6401 when assessing procurement and/or other resource acquisitions to meet the requirements of the QUASAR Audiogram Module.

Conforming to these established and/or emerging VA standards is recommended.

A dynamic update of the VA Desktop Standards is maintained at <span class="mark">REDACTED</span>

### PC Hardware Minimums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following PC hardware requirements are the recommended minimums to run the QUASAR Audiogram Module with interface functionality.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Specification</strong></td>
<td><strong>Recommended Minimum</strong></td>
</tr>
<tr class="even">
<td>Processor</td>
<td>1.4 GHz</td>
</tr>
<tr class="odd">
<td>Memory</td>
<td>512 Mb</td>
</tr>
<tr class="even">
<td>Hard Disk Space</td>
<td>50 MB (for vendor installations and updated GUI)</td>
</tr>
<tr class="odd">
<td>Keyboard</td>
<td>Standard US keyboard (PS/2, USB, or IR)</td>
</tr>
<tr class="even">
<td>Operating System</td>
<td>Microsoft Windows XP or greater (SP2 or higher)</td>
</tr>
<tr class="odd">
<td>Port</td>
<td><p>Available COM, USB, or Ethernet ports as required by individual device</p>
<p><strong>Note:</strong> If the audiometer is connected to the computer through a COM port, you must connect the audiometer to COM1.</p></td>
</tr>
</tbody>
</table>

### Monitor/Keyboard Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch ACKQ\*3.0\*13 requires attention be given to the setup of the keyboard and monitor.

- PC keyboard and PC monitor must be connected (cable) to the PC running the QUASAR Audiogram Module.
- Locate the keyboard adjacent to or directly below the audiometer device controls.
- Locate the PC monitor in a physical position, so that the clinician can comfortably view and analyze the data imported to the QUASAR Audiogram Module.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of the QUASAR Audiogram Module includes a KIDS build and a zip file containing one Delphi executable file: ACKQROES3E.exe.

> **NOTE:** The installation instructions allow you to place the zip file in a location on your hard drive. The desktop is a suggested location or \<root\>:\Program Files\VistA\QUASAR

The steps to set up the application must be completed incrementally and during the same session, in order for all of the new features to function correctly.

1.  Install KIDS.
8.  Download ACKQ3_0P13_EDIT.ZIP.
9.  Assign the ACKQROES3E VistA menu option to selected users and ASPS staff.
10. Add the name of the executable (Audiogram Edit) to the CPRS Tools menu.

## Pre-installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Remove both standalone (desktop) executables, Audiogram Edit ACKQROES3E and Audiogram Display ACKQROES3, from all desktops.

Before installing the patch, complete the following steps.

1.  Coordinate the installation with the IRMS of your facility.
11. Forward the ACKQ\*3.0\*13 patch message from Forum to your system. The Forum message contains the KIDS build.
12. Download ACKQ3_0P13_EDIT.ZIP. Only one file, setup.exe, is included in the ZIP file.

The preferred method is to FTP the files from the following website: <span class="mark">REDACTED</span>

This transmits the file from the first available FTP server. Sites may also elect to retrieve the ZIP directly from a specific server as follows:

CIO Field Office FTP Address Directory

1.  

<span class="mark">REDACTED</span>

2.  After saving the ZIP file, double-click it to unzip.
13. Highlight the file and click Extract.
14. Save the file to a directory of your choice.

## M Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch 13 can be loaded with users on the system. You can install it during non-peak hours. Installation takes less than two minutes. Follow your facility’s policy regarding the rebuilding of the menu trees upon patch completion.

> **NOTE:** The M server installation must be done before the Client installation.

1.  On the VistA system, set the variables DUZ and DUZ(0) by executing the command  
    D ^XUP. Verify DUZ(0) = @.
15. Load the ACKQ\*3.0\*13 KIDS build from the MailMan message.

> **NOTE:** MailMan and Kernel patches must be current on the target system to avoid problems loading and installing this patch.

16. Use the INSTALL/CHECK MESSAGE option of your KIDS menu to load the KIDS distribution onto your system.
17. On the Kernel Installation & Distribution System Menu (KIDS), select the Installation menu. From the menu choose the following options prior to installing the patch:
1.  Backup a Transport Global - this option creates a backup message of any routines exported with the patch. It does not backup any other changes, such as data dictionaries or templates
2.  Compare Transport Global to Current System - this option allows you to view all changes that are made when the patch is installed. It compares all components of the patch (routines, DDs, templates, and so on).
3.  Verify Checksums in Transport Global - this option allows you to ensure the integrity of the routine that is in the transport global.
18. Use the Install Package(s) option under the Installation menu.

    When prompted for INSTALL NAME, enter: ACKQ\*3.0\*13.
1.  When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//", respond NO.
2.  When prompted "Want to DISABLE Scheduled Options and Menu Options? YES//", respond YES.  
    Options to disable:  
    ACKQROES3E
19. If prompted ‘Delay Install (Minutes): 0-60): 0//; respond 0.
20. Verify that the patch installation completed correctly by using the KIDS Utilities... \[XPD UTILITY\] option Install File Print \[XPD PRINT INSTALL FILE\] and selecting this patch (ACKQ\*3.0\*13).

    Example of M Server Installation

\> D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select Option Name: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution…

Utilities…

KIDS Installation…

Patch Monitor Main Menu…

Select Kernel Installation & Distribution System Option: KIDS Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: ACKQ\*3.0\*13 Loaded from Distribution 5/21/07@10:19:57

=\> ACKQ\*3\*13

This Distribution was loaded on May 21, 2007@10:19:57 with header of

ACKQ\*3\*13

It consisted of the following Install(s):

ACKQ\*3.0\*13

Checking Install for Package ACKQ\*3.0\*13

Install Questions for ACKQ\*3.0\*13

Incoming Files:

509850.9 AUDIOMETRIC EXAM DATA (Partial Definition)

> **NOTE:** You already have the 'AUDIOMETRIC EXAM DATA' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//", respond 'YES' or 'NO' according to site's policy.

Want KIDS to INHIBIT LOGONs during the install? YES//, respond NO.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// , respond 'YES'.

Enter options you wish to mark as 'Out Of Order': ACKQROES3E

Enter protocols you wish to mark as 'Out Of Order': respond

with \<ENTER\>

Delay Install (Minutes): (0-60): 0// respond with '0'.

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<ENTER\>

Install Started for ACKQ\*3.0\*13 :

May 21, 2007@10:32:36

Build Distribution Date: May 09, 2007

Installing Routines:

May 21, 2007@10:32:36

ACKQ\*3.0\*13

Installing Data Dictionaries: ....

May 21, 2007@10:32:36

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

May 21, 2007@10:32:36

Updating Routine file...

Updating KIDS files...

ACKQ\*3.0\*13 Installed.

May 21, 2007@10:32:36

Install Message sent \#159434

100% 25 50 75

Complete

Install Completed

## Client (GUI) Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on site-specific implementation strategy, the executable may be located either on a shared network drive and/or on each client workstation.

Remove previous versions of the application, ACKQROES3E, before running the Installation Wizard.

> **NOTE:** The M Server installation must be done before the Client installation; exit all Windows applications prior to running the WinZip Wizard.

### Client Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default the client installation installs ACKQROES3E.EXE and builds a program folder at

\<root\>:\Program Files\VistA\QUASAR.

The recommended practice is to place the file on a central, shared network resource, where the appropriate CPRS setup procedures can reference the central location using a standard UNC path ([\\servername\sharename\filename](file:///\\servername\sharename\filename)).

### Client Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You saved the file to a directory on your workstation (pre-installation instructions).

1.  Unzip the file and install the executable.
21. Double-click setup.exe.
22. Click OK. The Open File – Security Warning screen may display.

> **NOTE:** The display of the security screen depends on how you download–from a local drive, from the web, from the desktop.

![](ackq-3-13-quasar-audiogram-module-install-implement-guide/002.png)

23. Click Run. The QUASAR Audiogram Module – InstallShield Wizard displays the Welcome screen.

![](ackq-3-13-quasar-audiogram-module-install-implement-guide/003.png)

24. Click Next and continue through the screens of the InstallShield Wizard. The Program Maintenance screen displays.

> **NOTE:** If no previous ACKQROES3E.EXE is detected, you will move through a series of screens, which includes the License Agreement, different from the screens that follow.

![](ackq-3-13-quasar-audiogram-module-install-implement-guide/004.png)

25. Select Repair and click Next.
26. Click Install. The InstallShield Wizard Completed screen displays.

![](ackq-3-13-quasar-audiogram-module-install-implement-guide/005.png)

27. Click Finish.

*This page intentionally left blank for double-sided printing.*

# Customizing the Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Assign ACKQROES3E Option to Users and Selected Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- All audiologists and designated staff editing audiograms must have VistA option: ACKQROES3E added to their VistA menu options, if not done in the original installation.
- The ASPS Chief should identify additional staff prior to installation.
- Use the VA FileMan to edit the SECONDARY MENU OPTIONS of all designated users.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION: 1 ENTER OR EDIT FILE ENTRIES</p>
<p>INPUT TO WHAT FILE: NEW PERSON// <strong>200</strong> NEW PERSON</p>
<p>EDIT WHICH FIELD: ALL// <strong>SECONDARY MENU</strong> OPTIONS (multiple)</p>
<p>EDIT WHICH SECONDARY MENU OPTIONS SUB-FIELD: ALL// <strong>.01</strong> SECONDARY MENU OPTIONS</p>
<p>THEN EDIT SECONDARY MENU OPTIONS SUB-FIELD: <strong>&lt;RETURN&gt;</strong></p>
<p>THEN EDIT FIELD:</p>
<p>Select NEW PERSON NAME: <u>USER, ASPS</u> (designated ASPS user name)</p>
<p>Select SECONDARY MENU OPTIONS: <strong>ACKQROES3E</strong> Audiogram Data Edit</p>
<p>...OK? Yes// <strong>&lt;RETURN&gt;</strong> (Yes)</p>
<p>SECONDARY MENU OPTIONS: ACKQROES3E// <strong>&lt;RETURN&gt;</strong></p>
<p>Select SECONDARY MENU OPTIONS: <strong>&lt;RETURN&gt;</strong></p>
<p>Select NEW PERSON NAME: <strong>&lt;RETURN&gt;</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Assign only the VistA option: ACKQROES3E, to a common VistA menu, and place the application on CPRS Tools in a place accessible by the users.
- Users are able to run the application only if they have the associated VistA menu option assigned to them.

## *Adding Audiogram Edit to CPRS Tools*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QUASAR Audiogram Module ACKQROES3E.exe file is designed for integration with CPRS; a patient must be identified prior to invoking the application. The application option displays on the CPRS Tools menu, when the installation procedures are complete.

1.  If not already done, copy ACKQROES3E.exe to a folder on either a shared network resource or on each user's workstation.
1.  It is recommended that you install to a shared resource; if you use a shared resource, you need to create a server-based folder and corresponding share name.

> **NOTE:** Ensure proper folder- or share-level permissions are applied to allow access for QUASAR Audiogram Module users.

1.  It is recommended that you use a share name of VistA;
- If you place the file in a shared location, the UNC path to that location can be used in the CPRS GUI Tools menu setup.
- If you place the file on each user’s workstation, the local path to that location must be used.
28. From the \[OR PARAM COORDINATOR\] menu, select GUI Parameters.
29. From GUI Parameters, select GUI TOOL MENU ITEMS.

> CPRS Tools menu setup:

| 1   | User     | USR \[choose from NEW PERSON\]        |
|-----|----------|---------------------------------------|
| 2   | Location | LOC \[choose from HOSPITAL LOCATION\] |
| 2.5 | Service  | SRV \[choose from SERVICE/SECTION\]   |
| 3   | Division | DIV \[choose from INSTITUTION\]       |
| 4   | System   | SYS (varies by site)                  |
| 9   | Package  | PKG \[REMOTE ORDER ENTRY SYSTEM\]     |

30. Determine which scope selection is appropriate based on the facility's established practice(s) regarding management of the Tools menu.

> **NOTE:** Ensure that the ACKQROES3E option is added at the proper level of granularity to make the option available to all identified QUASAR Audiogram Module users.

1.  Enter selection: \# of your choice.
2.  Make your choice from the selected file.
3.  Select Sequence: 1, if none exist or 1 greater than the highest number.
4.  Name=Command: AudiogramEdit="\\servername\sharename\ACKQROES3E.exe" DFN=%DFN  
    You can append, after adding a space, s=*server name*and p=*port number*.
31. Select the CPRS menu to verify that the applications display on the Tools list.

For additional instructions, refer to the *CPRS Technical Manual: GUI Version*.

<http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguitm.pdf>

> **NOTE:** This process is similar to the installation instructions for all other RPC Broker-enabled applications, such as CPRS, BCMA, CAPRI, and PCMM.

# Post-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Vendor Installation Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vendor Installation Wizard places DLLs in a specific folder on the PC used for hearing tests: C:\Program Files\VistA\QUASAR\Plugins\\

> **NOTE:** GSI 61 may require a firmware chip update. Follow your site’s procurement process for contacting the vendor: Viasys Grason-Stadler.

Obtain the current driver installer for your device from the QUASAR website.

<span class="mark">REDACTED</span>

To create a download account:

1.  From the VistA menu on the left, click Downloads.
32. Follow the directions for creating an account.
33. Download the appropriate installer.
34. Follow the instructions for installing the driver for your device.

> **NOTE:** The driver installation process varies from installer to installer. Instructions are within the installer executable.

## Audiogram Display through CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any doctor with access to the local system can view the Audiogram Display within the application to aid in treatment and diagnosis decisions. They may also continue to view the display as assigned in patch ACKQ\*3.0\*12. For information on Audiogram Display, refer to *Installation Guide - Audiometric Exam Module*, November 2005 in the VistA Document Library.

> [www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal\_(QUASAR)/ackq3_0_p12ig.pdf](http://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12ig.pdf)

*This page intentionally left blank for double-sided printing.*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Word/Acronym</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Alerts</td>
<td>Brief online notices that are issued to users as they complete a cycle through the menu system.<br />
Alerts are designed to provide notification of pending computing activities, such as the need to process a request for eligibility.</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Programmer Interface</td>
</tr>
<tr class="odd">
<td>Application Package</td>
<td>Software and documentation that support the automation of a service, such as ROES.</td>
</tr>
<tr class="even">
<td>ASPS</td>
<td>Audiology and Speech Pathology Service</td>
</tr>
<tr class="odd">
<td>C&amp;P</td>
<td>Compensation and Pension</td>
</tr>
<tr class="even">
<td>CAPRI</td>
<td>Compensation and Pension Records Interchange</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td>Computerized Patient Record Service</td>
</tr>
<tr class="even">
<td>Denver ALC</td>
<td>Denver Acquisition and Logistics Center<br />
A part of the Department of Veteran's Affairs, Office of Acquisition and Logistics, and located in Denver, Colorado.</td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>The internal number of the patient in the PATIENT file (#2).</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphical User Interface<br />
A Windows environment that allows users to interact using a mouse or keyboard.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td>KERNEL</td>
<td>A set of VistA software routines that function as an intermediary between the host operating system and the VistA application package, such as ROES.</td>
</tr>
<tr class="odd">
<td>Listener</td>
<td>In ROES, it is the RPC Broker on the workstation and the server.</td>
</tr>
<tr class="even">
<td>Name Spacing</td>
<td>A convention for naming VistA package elements, assigned by the Database Administrator (DBA), such as RMPF for ROES.</td>
</tr>
<tr class="odd">
<td>OPTION</td>
<td>An entry in the VistA OPTION file (#19).</td>
</tr>
<tr class="even">
<td>PCMM</td>
<td>Patient Care Management Module</td>
</tr>
<tr class="odd">
<td>PSAS</td>
<td>Prosthetics and Sensory Aids Service</td>
</tr>
<tr class="even">
<td>QUASAR</td>
<td>Quality: Audiology and Speech Analysis and Reporting</td>
</tr>
<tr class="odd">
<td>ROES</td>
<td>Remote Order Entry System<br />
A package for ordering various supplies from the Denver ALC.</td>
</tr>
<tr class="even">
<td>Routine</td>
<td>Groups of program lines that are saved, loaded, and called as a single unit by way of a specific name.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td>Remote Procedure Call.<br />
M code that takes optional parameters to do some work and then returns either a single value or an array to the client application.</td>
</tr>
<tr class="even">
<td>Security Key</td>
<td>A non-visual object or code that provides a layer of protection on the range of computing capabilities available with a particular software package.</td>
</tr>
<tr class="odd">
<td>Subscript</td>
<td>A numeric or string value that identifies a specific node within an array or global.</td>
</tr>
<tr class="even">
<td>UNC</td>
<td>Universal Naming Convention</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
ACKQ\*3.0\*12 15
ACKQROES3 5
ACKQROES3E 1, 13
Assign option to selected staff 13
Assign option to users 13
Audiogram display 5
CPRS Tools 15
Audiogram edit 1
CPRS Tools 13
Audiogram module
Installation 5
C
Checksums 6
Client server 9
Client workstation 9
CPRS 1
CPRS Tools Menu 14
D
Desktop minimums 3
DFN reference 14
Distribution system 6
F
FTP server 5
I
Installation
Client (GUI) 9
Customizing client 13
Kernel 6
M server 6
UNC path 9
Installer, Vendor 15
InstallShield wizard 10
K
Keyboard placement 4
KIDS 6
M
Monitor placement 4
P
PC Hardware minimums 4
Post-installation considerations 15
Pre-installation considerations 3
Pre-installation instructions 5
Q
QUASAR 1
QUASAR audiogram module 1
R
Related manuals 1
Requirements
Client 3
M server 3
ROES 1
T
Transport global 6
U
UNC path 13
V
VA MailMan connectivity 3
Vendor installation wizard 15
Vendor installer 15
VistA Broker client 3
VistA Broker listener. 3
VistA document library 1
VistA Server 3
W
WinZip wizard 9
