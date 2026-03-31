---
title: ROES Version 3 Security Guide
doc_type: SG
doc_label: Security Guide
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
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - roes
  - table
  - contents
  - application
  - dalc
  - strong
  - security
  - order
  - class
  - entry
page_count: 0
word_count: 4272
section_count: 32
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=99"
---

![](roes-version-3-security-guide/001.png)

Remote Order Entry System

(ROES)

Security Guide

![](roes-version-3-security-guide/002.png)

Version 3.0\*4

Updated February 2011

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
- [Introduction](#introduction)
  - [Purpose of ROES 3.0](#purpose-of-roes-30)
  - [Benefits of ROES 3.0](#benefits-of-roes-30)
  - [General Rules for ROES 3.0 Data Entry pages](#general-rules-for-roes-30-data-entry-pages)
- [Orientation](#orientation)
  - [Recommended Desktop Minimums for ROES 3.0](#recommended-desktop-minimums-for-roes-30)
  - [ROES 3.0 Display Considerations](#roes-30-display-considerations)
  - [Symbols Used in Manual](#symbols-used-in-manual)
  - [Getting Additional Information](#getting-additional-information)
  - [Generating Menu Diagrams](#generating-menu-diagrams)
- [Chapter 1: Security Management](#chapter-1-security-management)
  - [Legal Requirements](#legal-requirements)
  - [Security Measures](#security-measures)
  - [Modification Restrictions](#modification-restrictions)
  - [Integration Agreements](#integration-agreements)
  - [User Training](#user-training)
  - [Unique Features](#unique-features)
  - [Additional ISO Information](#additional-iso-information)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
  - [Informational Websites](#informational-websites)
  - [Files](#files)
  - [File Structure of file 791814](#file-structure-of-file-791814)
  - [Remote Systems](#remote-systems)
  - [Archiving/Purging](#archivingpurging)
  - [Contingency Planning](#contingency-planning)
  - [Electronic Signatures](#electronic-signatures)
  - [Menus](#menus)
    - [ROES3 Patient Order from CPRS (GUI)](#roes3-patient-order-from-cprs-gui)
    - [Station Orders from the Desktop (GUI)](#station-orders-from-the-desktop-gui)
    - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [References](#references)
  - [Policies](#policies)
- [Acronyms](#acronyms)
- [Glossary](#glossary)
- [Index](#index)
|                    |                                        |                                    |
|--------------------|----------------------------------------|------------------------------------|
| Date           | Description                        | Author                         |
| September 16, 2003 | Format manual and input revisions      | <span class="mark">REDACTED</span> |
| September 18, 2003 | Revised format                         | <span class="mark">REDACTED</span> |
| October 21, 2003   | Revised base on NVS input              | <span class="mark">REDACTED</span> |
| July 2007          | Changed DDC to DALC                    | <span class="mark">REDACTED</span> |
| February 2009      | Update for changes due to ROES\*3.0\*4 | <span class="mark">REDACTED</span> |
| February 2010      | Changes to eligibility process         | <span class="mark">REDACTED</span> |

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the Remote Order Entry System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System (ROES) version 3.0 gives authorized end users at VHA facilities the ability to order products and services from the VA Acquisition & Logistics Acquisition & Logistics Center (DALC).

## Scope of Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides instructions for the installation and maintenance of the ROES 3.0\*4 software.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is intended for facility Information Security Officers (ISO) and Information Resource Management staff.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Remote Order Entry System (ROES) Version 3.0\*4 Release NotesRemote Order Entry System (ROES) Version 3.0\*4 Technical ManualRemote Order Entry System (ROES) Version 3.0\*4 User ManualRemote Order Entry System (ROES) Version 3.0\*4 Installation Guide*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 was developed to simplify and enhance the ordering of products and services from the Denver Acquisition & Logistics Center (DALC) including hearing aids and numerous other commodities. Ancillary functions such as updating patient records and registering devices may also be done through the web interface. ROES 3.0 is accessed from your PC as a web application through your browser allowing orders to be placed using an interactive, real time point and click interface. ROES 3.0 also accommodates keyboard navigation and entry.

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
4.  Only use the ![](roes-version-3-security-guide/003.png) ![](roes-version-3-security-guide/004.png) or ![](roes-version-3-security-guide/005.png) command buttons provided on the ROES 3.0 pages for navigation - never use the windows provided "back" and "forward" commands.
5.  The command buttons within the application perform background housekeeping functions that maintain the integrity of the order as a user navigates through the ordering process. The Windows browser's 'Forward' and 'Back' commands bypass those functions and could result in loss of information from the order.
6.  “Grayed out” fields cannot be accessed.
7.  Any ![](roes-version-3-security-guide/006.png) button will return you to the *View OrderHistory* page.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

A system meeting the above specifications can be expected to provide the functionality necessary for ROES 3.0. The VA Assistant Secretary for Information and Technology has established a set of minimum configurations for any new procurement of desktop systems across the enterprise (VA Directive 6401). For most of the specifications listed above, the VA minimum baseline exceeds the recommended minimum for ROES 3.0. The above specifications are provided to allow for use of equipment in current inventory, if necessary. In assessing procurement and/or other resource acquisition actions to meet ROES 3.0 desktop requirements, each facility is advised to give consideration to the specifications mandated by the above-mentioned Directive. Conformance with these established and/or emerging VA standards is encouraged. A dynamic update of the VA desktop standards is maintained at <span class="mark">REDACTED</span>

## ROES 3.0 Display Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: ROES 3.0 application pages display best at a display resolution of 1024x768. If this is not an end user's preferred resolution, ROES pages may not appear properly formatted. This will not affect application functionality, but may make page content more difficult to understand and navigate. If an end user chooses to increase their resolution from 1024x768, they should be aware that all other Windows applications and objects in their Windows environment will be reduced in size.

## Symbols Used in Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In code examples, the caret (^) or 'U' may be used interchangeably as separators.

The caret is also used to designate a global reference when used in front of a global name as in "^DPT(".

## Getting Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Visit the V*ist*A document library at <http://www.va.gov/vdl/> for the ROES PDF and WORD documentation.

Use the KIDS Build File Print option if you would like a complete listing of package components exported with this software.

Use the KIDS Install File Print option if you'd like to print out the results of the installation process.

Option XUPRROU (List Routines) prints a list of any or all of the ROES routines.

## Generating Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RMPF ROES3 is a client/server menu option, and therefore cannot be diagramed in the usual sense of the word. An "Inquire" into the OPTION file (#19) will display the menu information.

# Chapter 1: Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DALC (on behalf of VA, as a covered entity) maintains compliance with the Health Insurance Portability and Accountability Act (HIPAA) through Business Associate Agreements with contractors.

## Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 is structured around standard accepted VA and industry information security controls. While including components of a typical broker-based V*ist*A application, the majority of the ROES application is a Web-based application residing at the DALC. While the application is Web-based, it is designed to be accessible only from within the VA enterprise security perimeter or through the authorized VA authentication infrastructure. Typical ROES end users include staff in VAMC Audiology & Speech Pathology Services (ASPS), and some VAMC Prosthetics & Sensory Aids Services (PSAS). Appropriate DALC user accounts are also necessary in order to access ROES. All user accounts are granted only through authorized VA procedures.

All users accessing the DALC must have completed, approved, and signed Security Agreements returned the DALC to obtain Access and Verify codes. Upon access to the DALC for the first time, users are required to enter the assigned Access and Verify codes, but after that time, they will be matched up with the user information stored at the DALC, to allow automatic entry to the Web page.

In addition, supervisors are given access to a Web application that allows them to grant access to a limited group of other users, and assign their level of access. It is the responsibility of the supervisor to maintain this record of who has access to ROES and for what options.

Any suspected or confirmed breach of ROES information security, including compromise of Access and Verify codes, should be reported immediately to the DALC Chief, IRM Division at 303-914-5160.

The V*ist*A option RMPF ROES3 is the main V*ist*A option that is exported with ROES 3.0. It should be assigned to all users of either the Desktop or CPRS Tools applications to access the DALC Web site. These two options are generally assigned to PSAS users and others who may be designated by PSAS.

## Modification Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No local modifications of this package are authorized.

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Integration Agreements are used in ROES 3.0

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 26%" />
<col style="width: 32%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ROUTINE</strong></td>
<td><strong>FILE NUMBER</strong></td>
<td><strong>AGREEMENT #</strong></td>
</tr>
<tr class="even">
<td>RMPFRPC0</td>
<td><p>2</p>
<p>38.1</p></td>
<td><p># 174</p>
<p># 767</p></td>
</tr>
<tr class="odd">
<td>RMPFRPC1</td>
<td>38.1</td>
<td># 767</td>
</tr>
</tbody>
</table>

Many supported Integration Agreements (IA’s) are addressed in the included routines. They are listed at the top of each routine. Those referenced are: 2343, 2701, 3006, 4055, 4440, 10003, 10009, 10015, 10035, 10061, 10063, 10064, 10066, 10070, 10081, 10086, 10089, 10103, and 10104.

## User Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that all users of ROES 3.0 complete and understand the procedures presented in the ROES 3.0 Training package. This training provides instruction on the proper usage of the ROES 3.0 application for maximum accuracy, efficiency, and security.

## Unique Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As previously mentioned, ROES 3.0 represents a departure from the traditional V*ist*A package by integrating established V*ist*A components with a primarily Web-based application. As such, much of the application maintenance takes place at the DALC application server and is performed by DALC IRM staff. However, installation and maintenance of certain VAMC-resident components continues to require local IRM involvement and coordination with the end user community. This support generally involves work with existing V*ist*A data structures and data exchange methods, including V*ist*A menu systems, VA FileMan, the RPC broker, broker-based Delphi applications, and typical desktop system configuration and maintenance. For further information, please reference the ROES 3.0 Technical Manual and the ROES 3.0 Installation Guide.

ROES 3.0 users generate orders for products and services provided by the DALC. The DALC maintains national contracts for these products and services. The orders generated through ROES 3.0 are subsequently delivered to commercial contract vendors via standardized secure electronic data exchange processes or via paper-based fax transmission. The DALC (on behalf of VA, as a covered entity) maintains compliance with the Health Insurance Portability and Accountability Act (HIPAA) through Business Associate Agreements with contractors.

## Additional ISO Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There should be no local requirements of the ISO beyond the normal file and computer safety concerns.  
<span id="_Toc284939017" class="anchor"></span>Chapter 2: Security Features

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mailman messages regarding changes and additional information are passed to two mail groups: RMPF ROES UPDATES (ASPS) and RMPF ROES UPDATES (PSAS). To ensure appropriate security and confidentiality, membership in these mail groups should be limited to designated staff in the respective (ASPS or PSAS) Services.

## Informational Websites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following Websites for downloads and additional information:

V*ist*A RPC Broker Download site: <span class="mark">REDACTED</span>

V*ist*A document library: [www.va.gov/vdl](http://www.va.gov/vdl)

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One FileMan file is installed on the local VAMC V*ist*A system as part of ROES 3.0. The ROES ELIGIBILITY CONFIRMATION file was used in the initial release to store requests for veteran eligibility assessments from ASPS and the responses to those requests by PSAS. This file references patient entries from the local Patient file (#2), and eligibility information needed prior to accessing the ROES Web application for actions related to specific patients. This ROES ELIGIBILITY CONFIRMATION file is subject to typical V*ist*A security protection. It is no longer being added to and used only to reference previously assigned eligibilities. It will be phased out in future patches.

The ROES ELIGIBILITY CONFIRMATION file global is name spaced as ^RMPF(791814, and should not be modified locally or accessed other than through the following ROES component:

- Broker-based application ROES3.EXE

The ROES ELIGIBILITY CONFIRMATION file (#791814) global is cross referenced by the fields:

- PATIENT(B)
- APPROVE/REJECT(C)
- EXPIRATION DATE(D)

## File Structure of file 791814

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FIELD NUMBER | FIELD NAME                        |
|------------------|---------------------------------------|
| .01              | PATIENT (RP2'), \[0;1\]               |
| .02              | DATE REQUEST ENTERED (D), \[0;2\]     |
| .03              | ENTERING USER (ASPS) (P200'), \[0;3\] |
| .04              | EXPIRATION DATE (D), \[0;4\]          |
| 1.01             | SUGGESTED ELIGIBILITY (F), \[1;1\]    |
| 1.02             | EMAIL MSG NUMBER (P3.9'), \[1;2\]     |
| 2.01             | PSAS ELIGIBILITY (F), \[2;1\]         |
| 2.02             | APPROVE/REJECT (S), \[2;2\]           |
| 2.03             | USER (PSAS) (P200'), \[2;3\]          |
| 2.04             | ACTION DATE (D), \[2;4\]              |

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 includes application components that reside on two systems: the VAMC V*ist*A system and the DALC system. The VAMC components include ‘M’ routines, RPC Broker calls, and Delphi executables. The general purpose of these components is to gather information and initiate an interactive session to the DALC-resident ROES 3.0 Web application. ROES users place orders and perform other order management functions within the ROES Web application.

The DALC-resident component of ROES 3.0 exists as a Web-based order entry application. The interactive order entry process utilizes the browser as the application interface. Depending on which of two ROES 3.0 entry points is accessed (determined by the calling Delphi executable), end users have access to specific functional modules associated with the entry and management of orders for DALC products and services. Navigation and order entry is accomplished using typical Windows and Web methods, including drop-down selection, check boxes, radio buttons, free text, etc. Information entered in the Web application is processed by the DALC order fulfillment system.

ROES 3.0 passes patient and end user information to the DALC Web application using HTTP and a smart URL. When patient information is included, the patient SSN is encrypted before insertion into the URL and decrypted by the DALC. A secure https connection is used. All order information is created and stored at the DALC.

When the executable (ROES3.exe) and associated set of broker calls are invoked from an option on the CPRS Tools menu, the following information is passed in the URL:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Patient information</p></li>
</ul></th>
<th><ul>
<li><p>Name</p></li>
</ul></th>
<th><ul>
<li><p>SSN (encrypted)</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>ROES 3 calculated eligibility</p></li>
</ul></td>
<td><ul>
<li><p>Date of birth</p></li>
</ul></td>
<td><ul>
<li><p>Date of death</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>ICN</p></li>
</ul></td>
<td><ul>
<li><p>City</p></li>
</ul></td>
<td><ul>
<li><p>Address line 1</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Address line 2</p></li>
</ul></td>
<td><ul>
<li><p>Address line 3</p></li>
</ul></td>
<td><ul>
<li><p>State</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Zip</p></li>
</ul></td>
<td><ul>
<li><p>Temporary address start date</p></li>
</ul></td>
<td><ul>
<li><p>Temporary address end date</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Phone number</p></li>
</ul></td>
<td><ul>
<li><p>Eligibility status</p></li>
</ul></td>
<td><ul>
<li><p>Sensitive record flag</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Primary eligibility</p></li>
</ul></td>
<td><ul>
<li><p>Priority group</p></li>
</ul></td>
<td><ul>
<li><p>End user information</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>First five characters of last name</p></li>
</ul></td>
<td><ul>
<li><p>Title</p></li>
</ul></td>
<td><ul>
<li><p>Station</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Service</p></li>
</ul></td>
<td><ul>
<li><p>Production system flag</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

The second Delphi executable (ROES3DeskTop.exe), and its associated set of broker calls, comprises an application that can be invoked directly (separate from CPRS) or from an application shortcut. The DESKTOP APPLICATION inserts the following information into the URL:

- End user number (DUZ)
- First five characters of the user’s last name
- Service
- Station

## Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 has no package-specific archiving or purging procedures or recommendations. A small amount of information is maintained on the local system in the ROES ELIGIBILITY CONFIRMATION file(#791814). In general, retention of entries is required for a minimum of two years from the date an eligibility assessment is entered into the file. Based on the small size of entries in this file and that no new entries will be created, purging of entries beyond this time frame and will be issued in a future ROES 3.0 patch. Set and kill dates for these entries are managed by the ROES package. No archiving is necessary.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No package-specific contingency planning procedures are required on the local system beyond those typically protecting the V*ist*A system. Using services are responsible for developing local contingency plans to accommodate unavailability of this module in a production environment.

Protection for the Web application residing at the DALC is maintained within the DALC’s contingency planning resources, procedures, and documentation. Since access to the Web application depends on the availability of enterprise WAN resources, disruption of WAN service may lead to delays in order submission or require alternative (paper-based) delivery on a temporary basis

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures are not used in ROES 3.0 at this time.

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ROES3 Patient Order from CPRS (GUI) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main option necessary for placing orders and performing other actions that are patient specific is RMPF ROES3. This option is typically assigned to ASPS staff and other staff who might order products or services from the DALC (e.g., PSAS staff at some facilities). This option is accompanied by a ROES3.EXE executable, which is normally placed on end users’ CPRS Tools menu (see *ROES 3.0 Installation Guide*).

NAME: RMPF ROES3

MENU TEXT: ROES3 OPTION ACCESS

TYPE: Broker (Client/Server)

PACKAGE: REMOTE ORDER/ENTRY SYSTEM

DESCRIPTION: This is the option that allows user's to access the Delphi Executables that connects the user to the DALC Web site from the desktop or CPRS Tools menu.

RPC: RMPFDEMOG

RPC: DDR GETS ENTRY DATA

RPC: DDR LISTER

RPC: DDR FINDER

RPC: DDR KEY VALIDATOR

RPC: DDR GET DD HELP

RPC: DDR VALIDATOR

RPC: XUS AV CODE

RPC: XUS SIGNON SETUP

RPC: XUS AV HELP

RPC: XUS GET USER INFO

RPC: XWB CREATE CONTEXT

RPC: XWB GET VARIABLE VALUE

### Station Orders from the Desktop (GUI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

End users can also place general station orders through ROES3 by using a desktop application separate from CPRS. This also requires that the user have the RMPF ROES3 option assigned as described above. In this case, the option is accompanied by a Roes3Desktop.exe executable, which is usually placed on an end user’s desktop system or network drive (see *ROES 3.0 Installation Guide*).

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No security keys are exported with ROES 3.0.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No file security is provided.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following documents for additional information:
*ROES 3.0\*4 Installation GuideROES 3.0\*4 Release NotesROES 3.0\*4 Technical ManualROES 3.0\*4 User Manual*

## Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of ROES and DALC resources for providing audiology and speech devices to veteran beneficiaries is referenced in *VHA Directive 1173* and *VHA Handbook 1173.7, Audiology and Speech Devices*

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TERM    | DESCRIPTION                                                                                                                                                 |
| ASPS    | Audiology and Speech Pathology Service                                                                                                                          |
| CPRS    | Computerized Patient Record System                                                                                                                              |
| DALC    | Denver Acquisition & Logistics Center. A part of the Department of Veteran's Affairs that is located in Denver, Colorado.                                       |
| DFN     | The internal number of the patient in the PATIENT file (#2).                                                                                                    |
| GUI     | Graphical User Interface. Existing in a Windows environment that allows users to interact using a mouse or keyboard.                                            |
| HIPPA   | The Health Insurance Portability and Accountability Act                                                                                                         |
| HTTP    | HyperText Transfer Protocol. A protocol for connecting to a Web site.                                                                                           |
| HTTPS   | Hypertext Transfer Protocol over Secure Socket Layer                                                                                                            |
| ISO     | Information Security Officer                                                                                                                                    |
| KIDS    | Kernel Installation and Distribution System                                                                                                                     |
| PSAS    | Prosthetics and Sensory Aids Service                                                                                                                            |
| ROES    | Remote Order Entry System. A package for ordering various supplies and services from the DALC.                                                                  |
| RPC     | Remote Procedure Call. M code that takes optional parameters to do some work and then returns either a single value or an array back to the client application. |
| URL     | Uniform Resource Locator                                                                                                                                        |
| VAMC    | Veterans Affairs Medical Center                                                                                                                                 |
| V*ist*A | Veterans Health Information Systems and Technology Architecture.                                                                                                |
| WAN     | Wide Area Network                                                                                                                                               |
| WORD    | Microsoft word processing software                                                                                                                              |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                         |                                                                                                                                                                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TERM                | DESCRIPTION                                                                                                                                                                                                                                        |
| ALERTS              | Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide notification of pending computing activities.                                                                           |
| APPLICATION PACKAGE | Software and documentation that support the automation of a service. In this case, the Remote Order Entry System.                                                                                                                                      |
| KERNEL              | A set of V*ist*A software routines that function as an intermediary between the host operating system and the V*ist*A application package (in this case ROES).                                                                                         |
| LISTENER            | In ROES this is the RPC Broker on the workstation and the server.                                                                                                                                                                                      |
| NAME SPACING        | A convention for naming V*ist*A package elements, assigned by the Database Administrator (DBA). For ROES the name spacing is RMPF.                                                                                                                     |
| OPTION              | An item in the V*ist*A OPTION file (#19).                                                                                                                                                                                                              |
| ROUTINE             | Groups of program lines that are saved, loaded, and called as a single unit via a specific name.                                                                                                                                                       |
| SECURITY KEY        | A non-visual object or code that provides a layer of protection on the range of computing capabilities available with a particular software package. Access to ROES options is controlled via assignable privileges that control access to ROES menus. |
| SUBSCRIPT           | A numeric or string value that identifies a specific node within an array or global.                                                                                                                                                                   |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Date of birth 11
Date of death 11
DESKTOP APPLICATION 11
ELIGIBILITY CONFIRMATION file 11
Eligibility status 11
End user information 11
End user number (DUZ) 11
ICN 11
Name 11
Patient file 9
Patient information 11
Primary eligibility 11
Priority group 11
RMPF ROES UPDATES (ASPS) 9
RMPF ROES UPDATES (PSAS) 9
RMPF ROES3 6, 7, 12, 13
RMPFRPC0 8
RMPFRPC1 8
ROES 3 calculated eligibility 11
ROES ELIGIBILITY CONFIRMATION file 9
ROES3.EXE 9, 12
Roes3Desktop.exe 13
Sensitive record flag 11
Service 11
SSN 10, 11
Station 11, 13
Temporary address end date 11
Temporary address start date 11
URL 10
