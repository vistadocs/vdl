---
title: ROES Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: ROES
app_name: Remote Order Entry System
section: CLI
app_status: active
pkg_ns: ROES
patch_ver: 3
patch_id: ROES*3
group_key: "ROES:ROES:3"
file_numbers: []
security_keys: []
menu_options: 1
description: - [Revision History](#revision-history) - [Preface](#preface) - [Purpose of the Remote Order Entry System](#purpose-of-the-remote-order-entry-system) - [Scope of Manual](#scope-of-manual) - [Audience](#audience) - [Related Manuals](#related-manuals) - [Purpose of ROES 3.0](#purpose-of-roes-30) - [Be
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - roes
  - table
  - strong
  - contents
  - application
  - installation
  - mail
  - rmpf
  - desktop
  - group
page_count: 0
word_count: 5081
section_count: 29
table_count: 16
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=99"
---

![](roes-version-3-installation-guide/001.png)

Remote Order Entry System

(ROES)

Installation Guide

![](roes-version-3-installation-guide/002.png)

Version 3.0\*4

Updated June 2013

VistA Health Systems Design and Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Preface](#preface)
  - [Purpose of the Remote Order Entry System](#purpose-of-the-remote-order-entry-system)
  - [Scope of Manual](#scope-of-manual)
  - [Audience](#audience)
  - [Related Manuals](#related-manuals)
  - [Purpose of ROES 3.0](#purpose-of-roes-30)
  - [Benefits of ROES 3.0](#benefits-of-roes-30)
  - [General Rules for ROES 3.0 Data Entry pages](#general-rules-for-roes-30-data-entry-pages)
- [Orientation](#orientation)
  - [Symbols used in manual](#symbols-used-in-manual)
  - [Getting additional information](#getting-additional-information)
  - [Application Architecture Overview](#application-architecture-overview)
- [Chapter 1: Pre-Installation Issues](#chapter-1-pre-installation-issues)
  - [Recommended Desktop Minimums for ROES 3.0](#recommended-desktop-minimums-for-roes-30)
  - [System Configuration Issues](#system-configuration-issues)
  - [Routines and Checksums](#routines-and-checksums)
  - [## ROES 3.0\4 Display Considerations](#roes-304-display-considerations)
  - [FTP Software and Documentation](#ftp-software-and-documentation)
- [Chapter 2: ROES 3.0 System](#chapter-2-roes-30-system)
  - [VistA Option in ROES 3.0](#vista-option-in-roes-30)
  - [VistA Mail Groups used in ROES 3.0](#vista-mail-groups-used-in-roes-30)
  - [VistA Remote Procedure](#vista-remote-procedure)
  - [Delphi Executable List](#delphi-executable-list)
  - [VistA File](#vista-file)
- [Chapter 3: ROES 3.0\4 Installation Instructions](#chapter-3-roes-304-installation-instructions)
  - [Installation Overview](#installation-overview)
  - [Step 1: Install KIDS](#step-1-install-kids)
  - [Step 2: Setup Mail Groups if not previously done](#step-2-setup-mail-groups-if-not-previously-done)
    - [Mail Group - RMPF ROES UPDATES (ASPS)](#mail-group-rmpf-roes-updates-asps)
    - [Mail Group - RMPF ROES UPDATES (PSAS)](#mail-group-rmpf-roes-updates-psas)
  - [Step 3: Assign RMPF ROES3 Menu Option to <u>New</u> Users](#step-3-assign-rmpf-roes3-menu-option-to-unewu-users)
  - [Step 4: Add ROES 3.0 Application to CPRS Tools Menu](#step-4-add-roes-30-application-to-cprs-tools-menu)
  - [Step 5: Add ROES 3.0 Application to User Desktop Environment](#step-5-add-roes-30-application-to-user-desktop-environment)
  - [Archiving/Purging](#archivingpurging)
- [Glossary](#glossary)
- [# Appendix](#appendix)
  - [Setting Up Mail Group Members:](#setting-up-mail-group-members)
- [Index](#index)
|                    |                                      |                                    |
|--------------------|--------------------------------------|------------------------------------|
| Date           | Description                      | Author                         |
| September 15, 2003 | Format manual and input revisions.   | <span class="mark">REDACTED</span> |
| September 18, 2003 | Revised format.                      | <span class="mark">REDACTED</span> |
| October 15, 2003   | Revised document based on NVS input. | <span class="mark">REDACTED</span> |
| July 2007          | Changed DDC to DALC                  | <span class="mark">REDACTED</span> |
| February 2009      | Enhancements and Modifications       | <span class="mark">REDACTED</span> |
| February 2011      | Changes to eligibility process added | <span class="mark">REDACTED</span> |
| June 2013          | Minor naming convention changes      | <span class="mark">REDACTED</span> |
Table of Contents

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the Remote Order Entry System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System (ROES) version 3.0 gave authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC).

## Scope of Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides updated instructions for the installation and maintenance of the ROES version 3.0\*4 software. Future references to ROES3 in this manual will refer to the updated ROES 3.0\*4 version released in patch RMPF3_0P4.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is intended for Information Resource Management (IRM) staff. However it may also be helpful to: National V*ist*A Support (NVS), Health System Design & Development (HSD&D), and ADPACs in Audiology and Speech Pathology Service (ASPS) and Prosthetics and Sensory Aids Service (PSAS).

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Remote Order Entry System (ROES) Version 3.0\*4 Release NotesRemote Order Entry System (ROES) Version 3.0\*4 Technical ManualRemote Order Entry System (ROES) Version 3.0\*4 User ManualRemote Order Entry System (ROES) Version 3.0\*4 Security Guide*

  
<span id="_Toc358725992" class="anchor"></span>Introduction

## Purpose of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES version 3.0 was developed to simplify and enhance the ordering of products and services from the Denver Acquisition & Logistics Center (DALC) including hearing aids and numerous other commodities. Ancillary functions such as updating patient records and registering devices may also be done through the web interface. ROES 3.0 is accessed from your PC as a web application through your browser allowing orders to be placed using an interactive, real time point and click interface. ROES version 3.0 also accommodates keyboard navigation and entry.

ROES 3.0 was designed to use advanced technologies and practices in software design, supporting hardware platform, database management, and network integration to provide DALC customers and staff with simple and easy to use ordering capabilities. The application provides patient care providers and associated Veterans Health Administration (VHA) staff with comprehensive patient information and order histories. It was also designed to use progressive procurement and distribution practices, advanced general business practices, and current VA Regulations, which have evolved since the introduction of ROES 2.0

A definitive criterion used to establish the strategic direction and development path for ROES 3.0 involved combining:

- The necessity to optimize compatibility and data communications capability with established VA systems and business practices
- The objective of applying leading edge information technology resources to strategic business systems development, comparable to the best that can be found in the private sector
- The desire to provide a "progressive continuity" to DALC customers, implementing significant enhancements to the existing application, while minimizing transition apprehension for end users.

## Benefits of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES 3.0 application architecture makes available, for the first time, a web-based application for activities such as order placement and inquiry functions, while retaining and improving upon the character-based interface formerly used in ROES 2.0. It is expected that a web interface, enabling point-and-click functionality, allows information to be presented in a more organized fashion, enhancing the navigation and data entry procedures.

In another departure from previous versions, the majority of ROES 3.0 system software and data files reside on DALC computer resources, leaving only selected key components on local Medical Center systems. There are a number of factors supporting this transition. These include:

- Insurance of a singularity and consistency of the available product database
- Opportunity for immediate real-time processing of orders placed
- Reduced dependency on VAMC application of patches and file modifications

Higher capacity VA wide area network resources implemented since ROES 2.0 enable these architectural changes.

In addition to the overall architecture, ROES 3.0 provides a number of process-specific benefits, features, and functionality improvements, such as the following:

1.  Provides users with a simplified ordering process.
2.  Includes cost comparison functionality for display/selection of all contract hearing aids meeting selected specifications.
3.  Allows repair orders to be entered by the provider.
4.  Includes a module to enter audiometric data and display or print the resulting audiogram in graph or tabular format.
5.  Provides information in "real time".
6.  Provides enhanced commodity ordering capabilities.
7.  Provides enhanced device registration capabilities.
8.  Provides enhanced display/update capabilities for authorized aids.
9.  Provides enhanced station stock ordering capabilities.
10. Decreases delivery time to patients since orders are submitted immediately for processing.
11. Links with the CPRS clinical record application already in place in the VHA environment.
12. Provides increased accuracy in patient eligibility determination prior to order placement, with improvements to subsequent reporting and statistical analysis.
13. Provides access to multiple ROES 3.0 functions (clinical and administrative) through a comprehensive entry point.
14. Provides supervisory designation of user authorization/approval levels.
15. Provides a Cochlear Implant registry for tracking of cochlear implant information.
16. Reduces the likelihood of erroneous orders such as, orders for combinations of device specifications that cannot be accommodated by hearing aid manufacturers.

## General Rules for ROES 3.0 Data Entry pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  There are no "double clicks" in ROES 3.0. Click the selection one time only.
2.  There are no "right mouse button” commands in ROES 3.0.

> NOTE: There is a key distinction between Windows-based applications (where double-clicks and right-button functionality are common) and web applications. There will not be a noticeable consequence to the user for these actions; however, the results may be unexpected. Double clicking may cause a drop-down list to open and close quickly. Right-clicking will produce selectable functions made available by the browser, but nothing specific to ROES. We strongly discourage use of the right-click in order to prevent the use of the browser's back and forward functions.

3.  It is recommended that users not click the "X" in the top right hand section of the ROES 3.0 browser window to close a window. Use the navigational links and buttons provided within the application to exit the system. Closing the browser window without properly exiting the application will not have any detrimental effects on the user but may leave an open user session and incomplete or 'phantom' order information in the application.
4.  Only use the ![](roes-version-3-installation-guide/003.png) ![](roes-version-3-installation-guide/004.png) or ![](roes-version-3-installation-guide/005.png) command buttons provided on the ROES 3.0 pages for navigation - never use the windows provided "back" and "forward" commands.
5.  The command buttons within the application perform background housekeeping functions that maintain the integrity of the order as a user navigates through the ordering process. The Windows browser's 'Forward' and 'Back' commands bypass those functions and could result in loss of information from the order.
6.  “Grayed out” fields cannot be accessed.
7.  Any ![](roes-version-3-installation-guide/006.png) button will return you to the *View OrderHistory* page.

# Orientation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Symbols used in manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In code examples, the caret (^) or 'U' may be used interchangeably as separators.

The caret is also used to designate a global reference when used in front of a global name as in ^DPT(.

## Getting additional information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Visit the V*ist*A document library web site at <http://www.va.gov/vdl/> for the ROES 3.0 PDF and WORD documentation.

Use the KIDS Build File Print option \[XPD PRINT BUILD\] if you would like a complete listing of package components exported with this software.

Use the KIDS Install File Print option \[XPD PRINT INSTALL FILE\] if you'd like to print out the results of the installation process.

## Application Architecture Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 includes application components that reside on two systems: the VA V*ist*A system and the DALC system. The VAMC components include ‘M’ routines, RPC Broker calls, and Delphi executables. The general purpose of these components is to gather information and initiate an interactive session to the DALC-resident ROES 3.0 Web application, passing the assembled information to the application.

Two Delphi executables invoke different capabilities within ROES 3.0. One executable and associated set of broker calls integrates as an option on the CPRS Tools menu (see also the chapter: *Charts in the ROES 3.0 Technical Manual*). This set of components performs the following functions:

- Gathers patient information for the selected patient
- Determines the patient’s eligibility for DALC services
- Assembles patient and user information
- Initiates a browser session to the ROES 3.0 web application and passes the assembled information to the ROES3PATIENT web site.
- Allows for copying of specified order information to the Windows clipboard with subsequent pasting to a CPRS Progress Note or to an external application

The second combination of Delphi executable and associated set of broker calls comprises an executable application that can be invoked directly (separate from CPRS) or from an application shortcut, and performs the following functions:

- Assembles user information from the RPCBroker connection information.
- Initiates a browser session to the ROES 3.0 web application and passes the Assembled information to ROES3HOME application site.

The DALC-resident component of ROES 3.0 exists as a Web-based order entry application. The browser is used as the application interface. Users have access to specific functional modules depending on which ROES 3.0 entry point is accessed and which privileges they have been assigned.

# Chapter 1: Pre-Installation Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: Because the VAMC-resident components are structured to link directly to the DALC production processing system, installation of the ROES 3.0 distribution package in a 'Test' or other non-production UCI/namespace should not be performed. Installation in a non-production environment could cause fictitious orders to be processed to fulfillment by the DALC. If you need additional information regarding this issue, contact the DALC IRM Division (303-914-5160).

Estimated installation and setup time: 30 minutes

## Recommended Desktop Minimums for ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SPECIFICATION</strong></td>
<td><strong>RECOMMENDED MINIMUM</strong></td>
</tr>
<tr class="even">
<td><strong>Processor</strong></td>
<td>866 MHz</td>
</tr>
<tr class="odd">
<td><strong>Memory</strong></td>
<td>512 Mb</td>
</tr>
<tr class="even">
<td><strong>Hard Drive</strong></td>
<td>20Gb</td>
</tr>
<tr class="odd">
<td><strong>Video Card</strong></td>
<td>Super VGA</td>
</tr>
<tr class="even">
<td><strong>CD-ROM/DVD Drive</strong></td>
<td>32x CD</td>
</tr>
<tr class="odd">
<td><strong>Monitor</strong></td>
<td>17" VGA, .28 pixel resolution</td>
</tr>
<tr class="even">
<td><strong>LAN Interface</strong></td>
<td>10/100 remote wake-on-LAN Ethernet interface</td>
</tr>
<tr class="odd">
<td><strong>Keyboard</strong></td>
<td>101 -key</td>
</tr>
<tr class="even">
<td><strong>Mouse</strong></td>
<td>Microsoft Compatible</td>
</tr>
<tr class="odd">
<td><strong>Operating System*</strong></td>
<td><p>Microsoft Windows 9x</p>
<p>Microsoft Windows NT Workstation v4.0 or Windows 2000 Pro strongly recommended.</p></td>
</tr>
<tr class="even">
<td><strong>Browser</strong></td>
<td>Internet Explorer v6+</td>
</tr>
</tbody>
</table>

\*NOTE: ROES 3.0 is compatible with Microsoft Windows XP.

\*\*NOTE: There are no minimum Browser Service Pack requirements.

A system meeting the above specifications can be expected to provide the functionality necessary for ROES 3.0. The VA Assistant Secretary for Information and Technology has established a set of minimum configurations for any new procurement of desktop systems across the enterprise (VA Directive 6401). For most of the specifications listed above, the VA minimum baseline exceeds the recommended minimum for ROES 3.0. The above specifications are provided to allow for use of equipment in current inventory, if necessary. In assessing procurement and/or other resource acquisition actions to meet ROES 3.0 desktop requirements, each facility is advised to give consideration to the specifications mandated by the above-mentioned Directive. Conformance with these established and/or emerging VA standards is encouraged. A dynamic update of the VA desktop standards is maintained at <span class="mark">REDACTED</span>.

## System Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES application requires that the user's browser have JAVA available and enabled in order to function. Sun has not developed a 64-bit version of JAVA, so on 64-bit terminal server installations the browser is not JAVA capable. This may prevent some ROES features from working properly. 64-bit installations also have a 32-bit browser which resides at a location different from the normal 32-bit location. That new location is:

C:\Program Files (x86)\Internet Explorer\IEXPLORE.EXE.

In order to ensure full functionality of ROES features, the ROES executables that invoke the browser for connection to the web application have been modified to check the (x86) location in addition to the previous locations:

C:\Program Files\Internet Explorer\IEXPLORE.EXE or

C:\Program Files\PLUS!\Microsoft Internet\IEXPLORE.EXE

If the ROES application does not work properly after installing the new executables, please ensure “IEXPLORE.EXE" does exist in one of these locations.

Two Delphi executable files are included in the ROES 3.0 distribution package. One file (ROES3.exe) is designed for integration with CPRS and depends on a patient being identified prior to the option being invoked. Upon completion of the installation procedures, this should appear as a selectable option on the CPRS Tools menu.

The other file (ROES3DeskTop.exe) is designed as a stand-alone (non-CPRS) application and ROES 3.0 entry point. It does not require pre-identification of a specific patient. It is intended that this option be made available to end users via a desktop shortcut to the application path, although other typical Windows methods of invoking the option can be considered, such as adding the option to the Windows Programs menu. The instructions throughout this document assume that the application files have been installed in a specific location and that a desktop shortcut to the application is available to the end user.

Desired placement of these ROES 3.0 Delphi files should be determined in advance and may vary based on facility-specific practices regarding broker-based applications. A common and recommended practice is to place the files on a central shared network resource. The appropriate CPRS and desktop setup procedures can then reference that central location using a standard UNC path (\\*servername*\\*sharename*\\*filename*). An alternative practice may be to place the files on each client computer, referencing that application path in the CPRS and desktop setup. If this is done, be sure to maintain a record of locations for future updates to the application.

ROES 3.0 transmits user and patient data to the DALC web application using HTTP and a smart URL. All order information is created and stored at the DALC.

It is recommended that proper coordination be done with ASPS and PSAS for determination of menu option assignment (see detailed description in [*Chapter 3*](#chapter-3-roes-3.04-installation-instructions)) and mail group membership (see detailed descriptions in *[Chapters 2](#_VistA_Mail_Groups), [3](#step-2-setup-mail-groups-if-not-previously-done) and the [Appendix](#setting-up-mail-group-members)*). In most cases, the RMPF ROES UPDATES (ASPS) and RMPF ROES UPDATES (PSAS) mail groups should already exist on the local VistA system. If not, the names of mail group coordinators for these mail groups will be required during the installation process. The names of the coordinators should be obtained from or verified by the respective Services prior to installation.

DALC ROES 3.0 order processing also incorporates patient-specific audiometric information from the Quality: Audiology and Speech Pathology Audit and Review (QUASAR) package. A companion QUASAR patch (Audiogram Module: ACKQ\*3.0\*13) provides end users with data entry and display capabilities for this information. It is recommended that ACKQ\*3.0\*13 be installed concurrently with ROES 3.0, if not already in place.

## Routines and Checksums 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the routines and checksums for ROES 3.0\*4.

> **NOTE:** All routines and checksums are new for ROES 3.04 and do not need to be mapped.

|              |              |                                                                                              |
|--------------|--------------|----------------------------------------------------------------------------------------------|
| ROUTINE  | CHECKSUM | DESCRIPTION                                                                              |
| RMPFRPC0 | 45,495,358   | Called from RMPFRPC1 to collect information and calculate eligibility and return to the GUI. |
| RMPFRPC1 | 22,103,813   | Used by RPC RMPFDEMOG to collect patient demographic information and return to the GUI.      |

## ## ROES 3.0\*4 Display Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: ROES 3.0\*4 application pages display best at a display resolution of 1024x768. If this is not an end user's preferred resolution, ROES pages will not appear properly formatted. This will not affect application functionality, but may make page content more difficult to understand and navigate. If an end user chooses to increase their resolution from 1024x768, they should be aware that all other Windows applications and objects in their Windows environment will be reduced in size.

## FTP Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software for this patch is available for retrieval via FTP. All VA Medical Centers are encouraged to use the TCPIP FTP functionality to obtain the software from one of the following OI Field Office ANONYMOUS.SOFTWARE directories:

| OI FIELD OFFICE                | FTP ADDRESS                    |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

| FILE NAME | TITLE               | TRANSFER MODE |
|---------------|-------------------------|-------------------|
| RMPF3_0P4.KID | KIDS File               | ASCII             |
| RMPF3_0P4.ZIP | ZIP File of Executables | Binary            |

| FILE NAME | TITLE          | TRANSFER MODE |
|---------------|--------------------|-------------------|
| RMPF3_0P4IG   | Installation Guide | Binary            |
| RMPF3_0P4SG   | Security Guide     | Binary            |
| RMPF3_0P4TM   | Technical Manual   | Binary            |
| RMPF3_0P4UM   | User Manual        | Binary            |

> **NOTE:** The KIDS file must be transferred in ASCII mode. The .DOC, .PDF and .ZIP files must be transferred in binary mode. The .PDF files can be read using the Adobe Acrobat Reader program, the .DOC files with Microsoft WORD application.

# Chapter 2: ROES 3.0 System 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS Build installs and maintains the following options, mail groups, remote procedure calls and routines to the V*ist*A system:

## VistA Option in ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                |                                                                                             |
|----------------|---------------------------------------------------------------------------------------------|
| OPTION     | DESCRIPTION                                                                             |
| RMPF ROES3 | VistA User Option for context access to either ROES3 Patient or ROES3 Desktop applications. |

<span id="_VistA_Mail_Groups" class="anchor"></span>

## VistA Mail Groups used in ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These mail groups may already exist at your site from previous versions of ROES, but if not, you will need to name a coordinator at installation and enter appropriate users.

1\. RMPF ROES UPDATES (ASPS) receives periodic messages and updates about ROES3.

2\. RMPF ROES UPDATES (PSAS) receives periodic messages and updates about ROES3.

## VistA Remote Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|               |                                                  |
|---------------|--------------------------------------------------|
| PROCEDURE | DESCRIPTION                                  |
| RMPFDEMOG | Collects demographic and eligibility information |

## Delphi Executable List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                      |                                                                  |
|----------------------|------------------------------------------------------------------|
| EXECUTABLE       | DESCRIPTION                                                  |
| ROES3.exe        | Main application for patient orders run from the CPRS Tools Menu |
| ROES3DeskTop.exe | Main station order routine to be run from the desktop.           |

## VistA File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one file that exists in the ROES 3.0 package. It is for the storage of eligibility requests and replies. It is a standard ROES name spaced (RMPF), FileMan-compatible file ^RMPF(791814,)

This file is currently only used for reference and will be removed in a future patch. No new entries are setup with the new architecture for ROES 3.0\*4.

This eligibility file contains entries in the "^RMPF (791814," global in the following format:

^RMPF(791814,IEN,0)=DFN ^ entry date ^ DUZ of entering user ^ expiration date

^RMPF(791814,IEN,1)=ASPS suggested eligibility ^ msg number to PSAS

^RMPF(791814,IEN,2)=PSAS selected eligibility ^ rejected(0), approved(1), or pending(2) ^DUZ of PSAS user ^ action date

# Chapter 3: ROES 3.0\*4 Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES 3.0\*4 distribution package includes a KIDS Build and the RMPF3_0P4.ZIP file. The KIDS installation will set up the menu option, mail groups, remote procedure call and routines. The VistA file (#791814) was created in required build RMPF\*3.0\*1. The Broker-based Delphi executables, ROES3.exe and ROES3DeskTop.exe, will be extracted from the RMPF3_0P4.ZIP file. VistA Option RMPF ROES3 is used to establish context (for both Delphi executables) and therefore allow access to the DALC web applications.

ROES 3.0 requires that the RPC Broker V1.1 be installed and accessible from any workstation from which the GUI will be executed. If a workstation can already connect successfully via CPRS, BCMA, or PCMM, then the RPC Broker has already been installed. If you need to install the RPC Broker, please refer to the RPC Broker website <span class="mark">REDACTED</span> for configuration information and to download the installation file.

The workstation used to access either of the Delphi executables will need to have the RPC Broker Listener set up the same way that it is for CPRS, BCMA or PCMM. The serverlist.exe application, which comes with the RPC Broker installation file, determines which accounts a particular workstation can access. If you need more information on serverlist.exe, please refer to the RPC BROKER TECHNICAL MANUAL.

As described in [*Chapter 1*](#chapter-1-pre-installation-issues), desired placement of the two ROES 3.0 Delphi executable files should be determined in advance and may vary based on facility-specific practices regarding broker-based applications. A common and recommended practice is to place the files on a central shared network resource. The appropriate CPRS and desktop setup procedures can then reference that central location using a standard universal naming convention (UNC) path (\\*servername*\\*sharename*\\*filename*). An alternative practice may be to place the files on each client computer, referencing that application path in the CPRS and desktop setup.

The following sequence summarizes the procedures necessary for installation of all ROES 3.0 components. Detailed descriptions of these procedural steps follow.

1.  Install KIDS
2.  Setup Mail Groups if not already set up.
3.  Assign RMPF ROES3 Menu Option to Users
4.  Add ROES3.exe application to CPRS Tools Menu (copy over existing executables of the same name after making a backup of the original).
5.  Add ROES3DeskTop.exe application to the user desktop environment (copy over existing executables of the same name after making a backup of the original).

## Step 1: Install KIDS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Consider the following items before beginning Step 1:

- Users are allowed to be on the system during the installation.
- It will take less than two minutes to run the KIDS installation.
- You do not need to stop TaskMan or the background filers.

While performing step number 2 of this procedure, you may be prompted to enter your ASPS and PSAS Mail Group Coordinators if they are not already identified in the system. Sign into the account where the package is installed. Make certain your DUZ variable is set to a valid user number and DUZ(0) equals "@". Invoke the KIDS menu (XPD Installation Menu option or D ^XPDKRN) to load the HFS file that contains the Distribution global and run the Install Package(s) option. This installation example assumes TaskMan is running.

1.  Select Programmer Options Option: Kernel Installation & Distribution System

> Edits and Distribution …

> Utilities …

> Installation …

2.  Select Kernel Installation & Distribution System Option: Installation

> Load a Distribution

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Install Package(s)

> Restart Install of Package (s)

> Unload a Distribution

3.  Select Installation Option: Load a Distribution

> Enter a Host File: RMPF3_4.KID

> Reply YES when asked if you want to continue with the load.

4.  The patch has now been loaded into a Transport Global on your system.

> NOTE: At this point you may wish to run the Verify Checksums in Transport Global option. If any of the routine checksums failed you should contact your distributing OI Field Office and not proceed with the installation process.

5.  Select Installation Option: Install Package(s)

> Select INSTALL NAME: ROES 3_4

> A comment may appear stating that you are running a previous version of ROES and ask if you want to continue installing ROES3.0. Respond YES

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

> When prompted respond: RMPF ROES3.

## Step 2: Setup Mail Groups if not previously done

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Group - RMPF ROES UPDATES (ASPS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This mail group may exist from prior versions of ROES, but if not, you will be asked to provide a coordinator during the installation process. All ASPS providers being assigned the RMPF ROES3 option should be made members of this group.

### Mail Group - RMPF ROES UPDATES (PSAS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This mail group may also exist from prior versions of ROES, but if not, you will be asked to provide a coordinator during the installation process.

## Step 3: Assign RMPF ROES3 Menu Option to <u>New</u> Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All ROES 3.0 users should have access to the RMPF ROES3 VistA Broker option to place orders or perform actions in the ROES 3.0 system. If there are new users of ROES, these staff should be identified by the Audiology (ASPS) and Prosthetics (PSAS) Service Chiefs prior to installation, along with the desired menu placement (Primary Menu, Secondary Menu, or other menu placement). For the new users attach the option to a V*ist*A menu, use the Kernel Menu Management Option as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>From <strong>the Menu Management Option [XUMAINT]</strong></p>
<p>Select Menu Management Option: <strong>ED</strong>it options</p>
<p>Select OPTION to edit: <strong>enter name of menu option to add to</strong></p>
<p>NAME: echoes back option// <strong>&lt;RETURN&gt;</strong></p>
<p>MENU TEXT: echoes back option menu text Replace <strong>&lt;RETURN&gt;</strong></p>
<p>PACKAGE<strong>: &lt;RETURN&gt;</strong></p>
<p>OUT OF ORDER MESSAGE: <strong>&lt;RETURN&gt;</strong></p>
<p>LOCK: <strong>&lt;RETURN&gt;</strong></p>
<p>REVERSE/NEGATIVE LOCK: <strong>&lt;RETURN&gt;</strong></p>
<p>DESCRIPTION: <strong>&lt;RETURN&gt;</strong></p>
<p>TYPE: Broker (Client/Server)// <strong>&lt;RETURN&gt;</strong></p>
<p>HEADER: <strong>&lt;RETURN&gt;</strong></p>
<p>ENTRY ACTION: <strong>&lt;RETURN&gt;</strong></p>
<p>EXIT ACTION: <strong>&lt;RETURN&gt;</strong></p>
<p>Select RPC: <strong>&lt;RETURN&gt;</strong></p>
<p>Select ITEM: xxxxxx// <strong>RMPF ROES3</strong> ROES3 OPTION ACCESS</p>
<p>Are you adding 'RMPF ROES3' as a new MENU (the 3RD for this OPTION)? No// <strong>Y</strong></p>
<p>(Yes)</p>
<p>MENU SYNONYM: <strong>R3</strong></p>
<p>SYNONYM: R3// <strong>&lt;RETURN&gt;</strong></p>
<p>DISPLAY ORDER: <strong>&lt;RETURN&gt;</strong></p>
<p>Select ITEM: <strong>&lt;RETURN&gt;</strong></p>
<p>CREATOR: POSTMASTER// <strong>&lt;RETURN&gt;</strong></p>
<p>HELP FRAME: <strong>&lt;RETURN&gt;</strong></p>
<p>PRIORITY: <strong>&lt;RETURN&gt;</strong></p>
<p>Select TIMES PROHIBITED: <strong>&lt;RETURN&gt;</strong></p>
<p>Select TIME PERIOD: <strong>&lt;RETURN&gt;</strong></p>
<p>RESTRICT DEVICES?: <strong>&lt;RETURN&gt;</strong></p>
<p>Select PERMITTED DEVICE: <strong>&lt;RETURN&gt;</strong></p>
<p>Select OPTION to edit: <strong>&lt;RETURN&gt;</strong></p></td>
</tr>
</tbody>
</table>

## Step 4: Add ROES 3.0 Application to CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Unzip RMPF3_0P4.zip and extract ROES3.exe.
2.  Locate, backup and replace all existing versions of the same name. If new copies are needed in different locations complete the following actions, otherwise jump to Step 5 (next pg).
3.  Copy ROES3.exe to a folder either on a shared network resource or on each ROES 3.0 user's workstation. Installation to a shared resource is recommended, in which case a server-based folder and corresponding share name would need to be created. Ensure proper folder- or share-level permissions are applied to allow access for ROES 3.0 users. A share name of V*ist*A is recommended. If the file is placed in a shared location, the UNC path to that location can be used in the setup below. If placed on each workstation, the local path to that location can be used.
4.  From the \[OR PARAM COORDINATOR\] menu select the option: GUI Parameters
5.  From this option select: GUI TOOL MENU ITEMS

> CPRS GUI Tools Menu may be set for the following:

|     |          |                                       |
|-----|----------|---------------------------------------|
| 1   | User     | USR \[choose from NEW PERSON\]        |
| 2   | Location | LOC \[choose from HOSPITAL LOCATION\] |
| 2.5 | Service  | SRV \[choose from SERVICE/SECTION\]   |
| 3   | Division | DIV \[choose from INSTITUTION\]       |
| 4   | System   | SYS (will vary by site)               |
| 9   | Package  | PKG \[ORDER ENTRY/RESULTS REPORTING\] |

> NOTE: Selection number 4, “System”, is the recommended scope selection; however, you should determine which scope selection is appropriate based on the facility’s established practices regarding management of the Tools menu. Ensure that the ROES 3.0 option is added at the proper level of granularity to make it available to all identified ROES 3.0 users.

6.  Enter selection: 4 System \[SITENAME\].MED.VA.GOV (or other appropriate scope selection)

> A list of existing entries for the Tools menu will be displayed.

7.  Select Sequence: 1 if none exist or the next sequence number

> Name=Command: ROES3="*path to executable* \ROES3.EXE" DFN=%DFN

> Optionally, you may append (after adding a space) s=BROKERSERVER (or correct server name) and p= 9200 (or correct port number).

8.  Re-enter the CPRS menu to verify that the ROES3 application appears on the tools list.
9.  See the CPRS Technical Manual if further instructions are desired.

## Step 5: Add ROES 3.0 Application to User Desktop Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Unzip RMPF3_0P4.zip and extract ROES3DeskTop.exe.
2.  Locate, backup and replace all existing versions of the same name. If this can be done you have finished. If new copies are needed in different locations complete the following actions.
3.  Copy ROES3DeskTop.exe to a folder on the workstation or shared network resource.

> NOTE: Installation to a shared resource is recommended, in which case a server-based folder and corresponding share name would need to be created. Ensure proper folder- or share-level permissions are applied to allow access for ROES 3.0 users. A share name of V*ist*A is recommended. The procedures in this document assume installation to this path. If installed to a different path, the shortcut procedure will need to be modified accordingly. This file can be placed in the same location as the ROES3.EXE file.

4.  Create a shortcut on each ROES 3.0 user's desktop to ROES3DeskTop.exe by right clicking on a blank region of the desktop and selecting NEW \| SHORTCUT.
5.  When asked for location, type the location in which ROES3DeskTop.exe has been placed, along with your local server and port information as parameters:

> *“[\\servername\VistA\ROES3DeskTop.exe](file:///\\servername\VistA\ROES3Desktop.exe)”*

> NOTE: Include the quotes around the directory string.

> Optionally, you may append (after adding a space) s=server and p=port number.

> NOTE: Appending the server and port limits the application to the designated server and port for users who have access to more than one server and port combination.

6.  Press NEXT.
7.  When asked for name, type: ROES 3 Desktop.
8.  Press FINISH.

Click the shortcut to ensure it connects successfully. A browser window indicating you are online with the VA Denver Acquisition & Logistics Center confirms that you have connected successfully.

## Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-specific archiving or purging procedures or recommendations for the ROES 3.0 package. All product and order detail information is stored and maintained on the DALC system. The only locally-stored information is that related to patient eligibility determination, in the soon to be expired VistA global: ^RMPF(791814, the ROES ELIGIBILITY CONFIRMATION file.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| TERM                |                                                                                                                                                                                                                   | DEFINITION                                                                                                                                                                                                                      |     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| ALERTS              |                                                                                                                                                                                                                   | Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide notification of pending computing activities, such as the need to process a request for eligibility. |     |
| APPLICATION PACKAGE |                                                                                                                                                                                                                   | Software and documentation that support the automation of a service. In this case, the Remote Order Entry System.                                                                                                                   |     |
| ASPS                |                                                                                                                                                                                                                   | Audiology and Speech Pathology Service.                                                                                                                                                                                             |     |
| DALC                |                                                                                                                                                                                                                   | Denver Acquisition & Logistics Center.                                                                                                                                                                                              |     |
| DFN                 |                                                                                                                                                                                                                   | The internal number of the patient in the PATIENT file (#2).                                                                                                                                                                        |     |
| GUI                 |                                                                                                                                                                                                                   | Graphical User Interface. Existing in a Windows environment that allows users to interact using a mouse or keyboard.                                                                                                                |     |
| HTTP                |                                                                                                                                                                                                                   | Hypertext Transfer Protocol. A protocol for connecting to a web site.                                                                                                                                                               |     |
| HTTPS               |                                                                                                                                                                                                                   | Hypertext Transfer Protocol over Secure Socket Layer                                                                                                                                                                                |     |
| IRM                 |                                                                                                                                                                                                                   | Information Resource Management.                                                                                                                                                                                                    |     |
| KERNEL              |                                                                                                                                                                                                                   | A set of V*ist*A software routines that function as an intermediary between the host operating system and the V*ist*A application package (in this case ROES 3.0).                                                          |     |
| LISTENER            |                                                                                                                                                                                                                   | In ROES 3.0 this is the RPC Broker on the workstation and the server.                                                                                                                                                               |     |
| NAME SPACING        |                                                                                                                                                                                                                   | A convention for naming V*ist*A package elements, assigned by the Database Administrator (DBA). For ROES 3.0 the name spacing is RMPF.                                                                                              |     |
| OPTION              | An item in the V*ist*A OPTION file (#19).                                                                                                                                                                         |                                                                                                                                                                                                                                     |     |
| PSAS                | Prosthetics and Sensory Aids Service                                                                                                                                                                              |                                                                                                                                                                                                                                     |     |
| ROES                | Remote Order Entry System.                                                                                                                                                                                        |                                                                                                                                                                                                                                     |     |
| ROUTINE             | Groups of program lines that are saved, loaded, and called as a single unit via a specific name.                                                                                                                  |                                                                                                                                                                                                                                     |     |
| RPC                 | Remote Procedure Call. M code that takes optional parameters to do some work and then returns either a single value or an array back to the client application.                                                   |                                                                                                                                                                                                                                     |     |
| SECURITY KEY        | A non-visual object or code that provides a layer of protection on the range of computing capabilities available with a particular software package. ROES 3.0 uses menu access for controlling access to options. |                                                                                                                                                                                                                                     |     |
| SUBSCRIPT           | A numeric or string value that identifies a specific node within an array or global.                                                                                                                              |                                                                                                                                                                                                                                     |     |
| UNC                 | Universal Naming Convention.                                                                                                                                                                                      |                                                                                                                                                                                                                                     |     |
| V*ist*A             | Veterans Health Information Systems and Technology Architecture.                                                                                                                                                  |                                                                                                                                                                                                                                     |     |

# # Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Setting Up Mail Group Members:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generally the mail group coordinator will add members, but if IRM is asked to do so, it can be done from the following options:

Manage MailMan Option \[XMMGR\]

Group/Distribution Management ...\[XMMGR-GROUP-MAINTENANCE\]

Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

1.  Select MAIL GROUP NAME: RMPF ROES UP

> 1 RMPF ROES UPDATES (ASPS)

> 2 RMPF ROES UPDATES (PSAS)

2.  CHOOSE 1-2: 1 RMPF ROES UPDATES (ASPS) \[for ASPS users identified by supervisor\]
3.  Select MEMBER: USER,GENERAL// USER,ASPS {Enter ASPS user name}
4.  To the following prompt: Are you adding 'USER,ASPS' as a new MEMBER (the 3RD for this MAIL GROUP)? Select No//Y (Yes)
5.  TYPE: I (INFO)
6.  Select MEMBER
7.  Select MEMBER GROUP NAME
8.  To the following prompt: Do you wish to forward past mail group messages to the user(s) you just added to the mail group(s)? Select No// NO
9.  Select MAIL GROUP NAME:
10. Repeat for RMPF ROES UPDATES (PSAS) with new users from PSAS

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BROKERSERVER 18
CPRS Tools Menu 18
Desktop 19
Desktop Minimums 6
Installation 13
LISTENER 20
Mail Group 16
Mail Group Members 22
Name=Command 18
RMPF ROES UPDATES 16
RMPF ROES3 13, 16, 17
RMPFDEMOG 8, 11
RMPFRPC0 8
RMPFRPC1 8
ROES 3.0 Delphi files 7
ROES3.exe 7, 11, 13, 18
ROES3DeskTop.exe 7, 11, 13, 19
V*ist*A File 12
