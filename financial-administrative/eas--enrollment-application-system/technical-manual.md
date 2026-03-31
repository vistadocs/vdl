---
title: EAS Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
file_numbers: 
  - 712
security_keys: []
menu_options: 0
description: The purpose of this Technical Manual is to provide technical background information to the VISTA system manager and other operations personnel to effectively manage Enrollment Application System (EAS) Version 1.0.
audience: 
keywords: 
  - table
  - contents
  - class
  - mail
  - action
  - group
  - even
  - server
  - application
  - security
page_count: 0
word_count: 4104
section_count: 12
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-version-1-technical-manual/001.png)

enrollment application system

online 10-10EZ

TECHNICAL Manual

March 2001

V*IST*A System Design & Development

Table of Contents

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
  - [Related Manuals](#related-manuals)
- [# Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
  - [Maintenance](#maintenance)
- [# Files](#files)
- [# Routines](#routines)
- [Exported Options](#exported-options)
- [Archiving & Purging](#archiving-purging)
- [# Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)](#callable-routines-entry-points-and-application-programmer-interfaces-apis)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Integration Agreements](#integration-agreements)
  - [Forum Components](#forum-components)
- [# Internal Relations](#internal-relations)
- [Package-wide Variable](#package-wide-variable)
- [Other Software Elements](#other-software-elements)
  - [List Templates](#list-templates)
  - [## Protocols](#protocols)
  - [Help Frames](#help-frames)
- [# # Software Product Security](#software-product-security)
  - [Security Features](#security-features)
    - [Mail Groups and Alerts](#mail-groups-and-alerts)
    - [Remote Systems](#remote-systems)
    - [Archiving/Purging](#archivingpurging)
    - [Contingency Planning](#contingency-planning)
    - [Interfaces](#interfaces)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
- [# Glossary](#glossary)
- [# Index](#index)
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 58%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision Date</th>
<th>Brief Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>June, 2001</td>
<td><p>Updated for patches EAS*1*1 and EAS*1*2.</p>
<p>Revisions made to the following sections:</p>
<ul>
<li><p>Exported Options</p></li>
<li><p>External Relations</p></li>
<li><p>Other Software Components</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>February/March, 2005</td>
<td><p>Updated for patch EAS*1*P57 (Phase 3)</p>
<p>Revisions made to the following sections:</p>
<ul>
<li><p>Introduction/Overview</p></li>
<li><p>Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)</p></li>
<li><p>External Relations</p></li>
<li><p>Routines (added EASEZ Name space routines)</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>June, 2005</td>
<td><p>Updated for patch EAS*1*P57 June enhancements and schedule variance (1010EZ Phase 3) for August Release</p>
<p>Added EASEZP63 to Routines table on page 6 per REDACTED</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June, 2009</td>
<td><p>Updated cover page to reflect the new VistA LOGO.</p>
<p>Posted document into the new VES section of the VDL</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>August, 2009</td>
<td><p>Updated cover page to reflect the old VistA LOGO.</p>
<p>Posted document back into the EAS section of the VDL</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August, 2020</td>
<td>Updated Overview and Protocols section to reflect that EAS*1.0*190 in Host File DG_53_P993.KID disables the Link to Patient (LZ) action in the Electronic 10-10EZ Processing option.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Technical Manual is to provide technical background information to the V*IST*A system manager and other operations personnel to effectively manage Enrollment Application System (EAS) Version 1.0.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL NEW ONLINE VA-FORM 10-10EZs ARE TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient (LZ) action in the Electronic 10-10EZ Processing option.

This initial release consists of a single module, the *10-10EZ Enrollment Application Processor*. EAS V. 1.0 represents Phase 2 of the 10-10EZ enrollment initiative. This module enables the local V*IST*A system to electronically process a 10-10EZ Application for enrollment and healthcare benefits, which has been submitted by a veteran via a web-based application located on the VA web server. The URL for the web-based 10-10EZ is:

https://www.1010ez.med.va.gov/sec/vha/1010ez/

The web-based application bundles the 10-10EZ data into two e-mail messages. One message is a simple listing of the data, easily readable and intended for staff members who are involved in enrollment activities. The other is a specially formatted data “dump”, which is automatically processed into a holding file by the 10-10EZ software.

Since the only channel of communication with the VA web server is through e-mail, the VA1010EZ mail group plays a critical role. This mail group was established through Patch DG\*5.3\*325 as a part of *10-10EZ Phase 1* functionality, released nationally in November, 2000.

Basically, the 10-10EZ Phase 2 module provides two important things requested by enrollment users:

1.  A user interface for review and management of the 10-10EZ Applications
2.  A holding file for 10-10EZ data, which is completely separate from other V*IST*A database files

The 10-10EZ Phase 3 enhancements, i.e., EAS\*1\*57, DG\*5.3\*624, were necessary to keep V*IST*A synchronized with the changes on the public 1010EZ web site and the official, OMB-approved 1010EZ paper form dated February 2005.

To briefly summarize, Phase 3:

1.  Creates several permanent V*IST*A storage locations for 1010-related fields
2.  Updates the help text of several fields added with DG\*5.3\*597 (Phase 2)
3.  Allows the display and edit of fields added with DG\*5.3\*597 within the Registration, Patient Load/Edit, and Means Test options, and
4.  Removes routines, options, and protocols related to printing the obsolete 1010 forms.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals are also being released with EAS V. 1.0:

- Enrollment Application System (EAS) V. 1.0 Installation Guide
- Enrollment Application System (EAS) V. 1.0 User Manual

# # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software module resides in the EAS namespace. It consists of the software items referenced in this manual, which include Routines, Files, Protocols, List Templates, and Menu Options.

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation occurs as soon as the server option, EAS EZ SERVER, has been entered as a remote member of the VA1010EZ Mail Group. The server routine will then be invoked as each 10-10EZ Application is received via e-mail.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Proper setup and maintenance of the VA1010EZ mail group is critically important. A FileMan listing of this group from the Mail Group File (#3.8) must show the following:

NAME: VA1010EZ

TYPE: public

ALLOW SELF ENROLLMENT?: NO

RESTRICTIONS: UNRESTRICTED

REMOTE MEMBER: S.EAS EZ SERVER@your-site.VA.GOV

The character string in “your-site.VA.GOV” should exactly match the contents of ^XMB(“NETNAME”) for your V*IST*A system.

Additionally, consult with your local HAS ADPAC or management to confirm the identity of an appropriate organizer for the mail group. Since self-enrollment is not allowed, this person will be responsible for maintenance of group membership. Insure that the Organizer has sufficient system access to add and remove mail group members as needed. Ideally, the Organizer should also be a Member of the group in order to receive all in-coming messages.

The Organizer should then verify that all facility staff with responsibilities to review and process 10-10EZ Applications are included as Members of the mail group. All Members of the VA1010EZ mail group should also be given access to the EAS EZ 1010EZ PROCESSING option, which is the entry point to the processing module.

There are no other routine maintenance procedures required by EAS V. 1.0.

Please see the Enrollment Application System (EAS) V.1 Installation Guide for important information pertinent to installation and post-installation setup procedures.

# # Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two files are exported in EAS V. 1.0 as shown in the table below. The files are exported with a high level of FileMan access security.

No data operations should be attempted on the files directly through FileMan. Any local modification to File \#711 will degrade database integrity. For data entry and update to File \#712, users should employ the Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\] menu option exclusively. However, it is certainly acceptable to use FileMan to generate ad hoc reports and listings as needed.

|            |                |                     |          |                       |                         |
|------------|----------------|---------------------|----------|-----------------------|-------------------------|
| Number | Name       | Global Location | Type | Size              | Exported with data? |
| 711        | 1010EZ MAPPING | ^EAS(711,           | Static   | ~ 350 Kbytes          | Yes                     |
| 712        | 1010EZ HOLDING | ^EAS(712,           | Dynamic  | 2-4 Kbytes per record | No                      |

A number of cross-references on File \#712, crucial to the proper functioning of the 1010EZ module, are maintained by the EAS\* routines during normal operation. User data entry through FileMan or re-indexing of File \#712 will lead to anomalous behavior of the user interface.

There are no FileMan templates distributed with this package.

# # Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine set distributed with EAS V. 1.0 is confined to the 1010EZ module and name spaced as EASEZ.

|                                                                                                                                                                                                                                                                  |                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Routine subsets                                                                                                                                                                                                                                              | Function           |
| EASEZC1, EASEZC2, EASEZC3                                                                                                                                                                                                                                        | Comparison to database |
| EASEZF1, EASEZF2, EASEZF3, EASEZF4, EASEZF5, EASEZFM, EASEZF1A, EASEZDD                                                                                                                                                                                          | Filing to database     |
| EASEZI, EASEZI1                                                                                                                                                                                                                                                  | Patient database match |
| EASEZL1, EASEZL2, EASEZLM                                                                                                                                                                                                                                        | List Manager control   |
| EASEZPF, EASEZPF1, EASEZPF2, EASEZPF3, EASEZPU, EASEZP64, EASEZP6F, EASEZP6M, EASEZP6U, EASEZPDG, EASEZPDU, EASEZPU2, EASEZPU3, EASEZPV2, EASEZPVD, EASEZPVI, EASEZRP1, EASEZRP2, EASEZRP3, EASEZRPD, EASEZRPF, EASEZRPI, EASEZRPM, EASEZRPP, EASEZRPU, EASEZP63 | 10-10EZ form print     |
| EASEZQ                                                                                                                                                                                                                                                           | Quick lookup           |
| EASEZT1, EASEZT2                                                                                                                                                                                                                                                 | Data transforms        |
| EASEZU1, EASEZU2, EASEZU3, EASEZU4, EASEZU5, EASEZU6                                                                                                                                                                                                             | Assorted utilities     |
| EASEZW                                                                                                                                                                                                                                                           | Mail server            |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Menu Text</strong></td>
<td><strong>Description</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr class="even">
<td>EAS EZ MENU</td>
<td>10-10EZ Menu</td>
<td>Main 10-10EZ user menu.</td>
<td>Menu</td>
</tr>
<tr class="odd">
<td>EAS EZ QUICK LOOKUP</td>
<td>10-10EZ Quick Lookup</td>
<td>Lookup and screen display of basic 10-10EZ information.</td>
<td><p>Run Routine</p>
<p>Entry point: EN^EASEZQ</p></td>
</tr>
<tr class="even">
<td>EAS EZ 1010EZ PROCESSING</td>
<td>Electronic 10-10EZ Processing</td>
<td>Provides access to 10-10EZ user interface.</td>
<td><p>Run Routine</p>
<p>Entry point: EN^EASEZLM</p></td>
</tr>
<tr class="odd">
<td>EAS EZ SERVER</td>
<td>10-10EZ Server</td>
<td>Receives 10-10EZ Applications via e-mail and places data in File #712.</td>
<td><p>Run Routine</p>
<p>Entry point: EN^EASEZW</p></td>
</tr>
<tr class="even">
<td>EAS EZ REMOVE SIGNATURE</td>
<td>Remove Signature Verification</td>
<td><p>Allows the user to remove Signature Verification from the</p>
<p>10-10EZ Application. The status of the Application reverts from 'Signed' to either 'Printed, Pending Signature' or 'In Review'.</p></td>
<td><p>Run Routine</p>
<p>Entry point: REMSIG^EASEZU5</p></td>
</tr>
</tbody>
</table>

Distribution of the EAS EZ 1010EZ PROCESSING option should be restricted to staff with registration and enrollment responsibilities. These users are normally also members of the VA1010EZ Mail Group. For detailed information on the use of the EAS EZ 1010EZ PROCESSING option, please see the *User Manual*.

# Archiving & Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging capabilities contained in this software package.

# # Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS contains 1 new callable entry point API Routine EASEZPDG under Integration Agreement 4600 for Phase 3.

# External Interfaces 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA MailMan provides an interface between EAS V. 1.0 and the web-based application where veterans submit their 10-10EZ Applications. The user interface contained in EAS V. 1.0 relies heavily on Kernel, VA FileMan, and List Manager.

The requirements for proper operation of EAS V. 1.0 are:

1.  TCP/IP channels to the internet from the local site are functioning.
2.  The EAS EZ SERVER option is a Remote Member of the VA1010EZ Mail Group.
3.  VA MailMan is operational and fully patched at minimum version 7.1.
4.  Kernel software is fully patched at minimum version 8.0.
5.  VA FileMan software is fully patched at minimum version 22.0.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database Integration Agreements have been established with V*IST*A Registration and Integrated Billing applications. Details can be found through the DBA Menu in FORUM for the following:

|              |                       |                                              |
|--------------|-----------------------|----------------------------------------------|
| DBIA ID# | Custodial Package | Needed for                               |
| 3302         | INTEGRATED BILLING    | Use of BUFF^IBCNBES1                         |
| 3325         | REGISTRATION          | Use of GETPAT^DGRPTU                         |
| 3326         | REGISTRATION          | Use of LST^DGMTU                             |
| 3327         | REGISTRATION          | Read & write via FileMan to File \#2.        |
| 3328         | REGISTRATION          | Read & write via FileMan to File \#408.12.   |
| 3329         | REGISTRATION          | Read & write via FileMan to File \#408.13.   |
| 3330         | REGISTRATION          | Read & write via FileMan to File \#408.21.   |
| 3331         | REGISTRATION          | Read & write via FileMan to File \#408.22.   |
| 4600         | EAS                   | Allow Registration to Print the 10-10EZ Form |

## Forum Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are also EAS\* software components residing on the *Forum*V*IST*A system. Again, VA MailMan serves as the interface between the 1010EZ module operating in your local V*IST*A system and *Forum*. Each 1010EZ data message (i.e., a 1010EZ submission) is routed to its target facility through REDACTED The web server application sends a copy of each submission to 1010EZ.1010EZ@FORUM.VA.GOV.

The following outlines the *Forum* software components and their functions:

1.  A server option, EAS EZ MGR SERVER, processes all MailMan messages sent to 1010EZ.1010EZ@FORUM.VA.GOV. These messages include:
    - Copies of all 1010EZ data messages from the web server; placed in RETAIN Mail Basket with vaporization date set to date received plus 180 days.
    - Acknowledgement messages from the V*IST*A field facilities; placed in ACK Mail Basket with vaporization date set to date received plus 14 days.
    - Daily Submissions List messages from the web server; placed in LIST Mail Basket with vaporization date set to date received plus 14 days.
2.  A file, EAS EZ TRANSMISSION MANAGEMENT (#711.1), holds a record for each 1010EZ data message received at *Forum*. As acknowledgement messages from the field facilities are received, the appropriate File \#711.1 record is updated with the acknowledgement date/time. The content of the Daily Submissions List is also compared to the File \#711.1 records to discover discrepancies.
3.  If more than one day elapses without an acknowledgement from the field facility to which the 1010EZ data message was addressed, the data message will be re-sent to the VA1010EZ Mail Group at the facility. If five (5) days elapse without receipt of an acknowledgement message at *Forum*, then the 1010EZ module will log a NOIS on behalf of the field facility to the National V*IST*A Support (NVS) team that supports the EAS package. The facility can expect to be contacted by NVS for resolution of the transmission problem.
4.  Another option, EAS EZ MGR CHECK, is run at *Forum* via Task Manager every 12 hours to check how long it has been since receipt of the last Daily Submissions List from the web server. If more than one day has elapsed, an alert message is directed to members of the 1010EZMGR Mail Group at *Forum*. Failure to receive a submissions list may signal a problem on the web server for On-Line 10-10EZ or in the communications link between the web server and Forum. In addition, the 1010EZ module will log a NOIS to report this problem to the NVS team that supports the EAS package.
5.  A daily report is provided via a MailMan message to members of the 1010EZMGR Mail Group. This report lists (a) all 1010EZ data messages, which have not been acknowledged by the appropriate field facility, and (b) any discrepancies between the Daily Submissions List and the 1010EZ data messages logged in File \#711.1. Problem items remain on the list for a maximum of 10 days.

It is important to note that the EAS software at Forum will not attempt to re-send a 1010EZ data transmission to a field facility until the facility has: (a) installed patch EAS\*1\*2 in its V*IST*A system, and (b) acknowledged receipt of at least one 1010EZ data message.

# # Internal Relations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS V. 1.0 consists of only one module, which contains three options, at present:

1)  server function
2)  user interface for processing
3)  user lookup function

There are no internal relationships that constrain the proper operation of the module. However, use of the user interface option (EAS EZ 1010EZ PROCESSING) assumes that the server option (EAS EZ SERVER) has been correctly enrolled as a Remote Member of the VA1010EZ Mail Group.

# Package-wide Variable 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables contained in the EAS V. 1.0 software.

# Other Software Elements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A number of List Templates, i.e., entries in the LIST TEMPLATE File (#409.61), and Protocols, i.e., entries in the PROTOCOL File (#101), are included in the EAS module. These elements are required for the operation of the List Manager-based user interface. Additionally, a number of Help Frames, i.e., entries in the HELP FRAME File (#9.2), are included to provide the user with basic terminology and functional help.

## List Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                              |          |                           |
|------------------------------|----------|---------------------------|
| Name                     | Type | Protocol Menu         |
| EAS EZ 1010EZ INITIAL SCREEN | Protocol | EAS EZ 1010EZ APPLICATION |
| EAS EZ 1010EZ REVIEW1        | Protocol | EAS EZ 1010EZ REVIEW1     |
| EAS EZ 1010EZ REVIEW2        | Protocol | EAS EZ 1010EZ REVIEW2     |
| EAS EZ 1010EZ REVIEW3        | Protocol | EAS EZ 1010EZ REVIEW3     |
| EAS EZ 1010EZ REVIEW4        | Protocol | EAS EZ 1010EZ REVIEW4     |
| EAS EZ 1010EZ REVIEW5        | Protocol | EAS EZ 1010EZ REVIEW5     |
| EAS EZ 1010EZ REVIEW6        | Protocol | EAS EZ 1010EZ REVIEW6     |

## ## Protocols 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL NEW ONLINE VA-FORM 10-10EZs ARE TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient (LZ) action in the EAS EZ LINK TO FILE 2 protocol.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 12%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Menu Items</strong></td>
</tr>
<tr class="even">
<td>EAS EZ 1010EZ APPLICATION</td>
<td>menu</td>
<td>EAS EZ CONTINUE PROCESSING</td>
</tr>
<tr class="odd">
<td>EAS EZ 1010EZ REVIEW1</td>
<td>menu</td>
<td><p>EAS EZ CLOSE/INACTIVATE 1010EZ</p>
<p>EAS EZ LINK TO FILE 2</p></td>
</tr>
<tr class="even">
<td>EAS EZ 1010EZ REVIEW2</td>
<td>menu</td>
<td><p>EAS EZ ACCEPT FIELD</p>
<p>EAS EZ ACCEPT ALL</p>
<p>EAS EZ CLEAR ALL</p>
<p>EAS EZ RESET TO NEW</p>
<p>EAS EZ CLOSE/INACTIVATE 1010EZ</p>
<p>EAS EZ PRINT 1010EZ</p>
<p>EAS EZ VERIFY SIGNATURE</p>
<p>EAS EZ UPDATE FIELD</p></td>
</tr>
<tr class="odd">
<td>EAS EZ 1010EZ REVIEW3</td>
<td>menu</td>
<td><p>EAS EZ RESET TO NEW</p>
<p>EAS EZ CLOSE/INACTIVATE 1010EZ</p>
<p>EAS EZ PRINT 1010EZ</p>
<p>EAS EZ VERIFY SIGNATURE</p></td>
</tr>
<tr class="even">
<td>EAS EZ 1010EZ REVIEW4</td>
<td>menu</td>
<td><p>EAS EZ PRINT 1010EZ</p>
<p>EAS EZ UPDATE FIELD</p>
<p>EAS EZ FILE 1010EZ DATA</p></td>
</tr>
<tr class="odd">
<td>EAS EZ 1010EZ REVIEW5</td>
<td>menu</td>
<td>EAS EZ PRINT 1010EZ</td>
</tr>
<tr class="even">
<td>EAS EZ 1010EZ REVIEW6</td>
<td>menu</td>
<td>EAS EZ QUIT</td>
</tr>
<tr class="odd">
<td>EAS EZ ACCEPT ALL</td>
<td>action</td>
<td>D ACCALL^EASEZU3</td>
</tr>
<tr class="even">
<td>EAS EZ ACCEPT FIELD</td>
<td>action</td>
<td>D ACCFLD^EASEZU3</td>
</tr>
<tr class="odd">
<td>EAS EZ CLEAR ALL</td>
<td>action</td>
<td>D CLEAR^EASEZU3</td>
</tr>
<tr class="even">
<td>EAS EZ CLOSE/INACTIVATE 1010EZ</td>
<td>action</td>
<td>D CLOSE^EASEZU4</td>
</tr>
<tr class="odd">
<td>EAS EZ CONTINUE PROCESSING</td>
<td>action</td>
<td>D EXPND^EASEZL1</td>
</tr>
<tr class="even">
<td>EAS EZ FILE 1010EZ DATA</td>
<td>action</td>
<td>D FILE^EASEZU4</td>
</tr>
<tr class="odd">
<td>EAS EZ LINK TO FILE 2</td>
<td>action</td>
<td>D LINK^EASEZU3</td>
</tr>
<tr class="even">
<td>EAS EZ PRINT 1010EZ</td>
<td>action</td>
<td>D PRT1010^EASEZU4</td>
</tr>
<tr class="odd">
<td>EAS EZ QUIT</td>
<td>action</td>
<td>S VALMBCK="Q" Q</td>
</tr>
<tr class="even">
<td>EAS EZ RESET TO NEW</td>
<td>action</td>
<td>D RESET^EASEZU3</td>
</tr>
<tr class="odd">
<td>EAS EZ UPDATE FIELD</td>
<td>action</td>
<td>D UPDATE^EASEZU5</td>
</tr>
<tr class="even">
<td>EAS EZ VERIFY SIGNATURE</td>
<td>action</td>
<td>D VERSIG^EASEZU4</td>
</tr>
</tbody>
</table>

## Help Frames 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The help frame system for EAS V. 1.0 is accessed by entry of “??” at the initial user prompt upon entry to the 1010EZ module.

> 10-10EZ Application Processing --

> Select one of the following:

> 1 New

> 2 In Review

> 3 Printed, Pending Signature

> 4 Signed

> 5 Filed

> 6 Inactivated

> Select Applications to View: ??

|                         |                                |
|-------------------------|--------------------------------|
| Help Frame          | Related Help Frames        |
| EAS EZ ACTION AF        |                                |
| EAS EZ ACTION AZ        |                                |
| EAS EZ ACTION CZ        |                                |
| EAS EZ ACTION FZ        |                                |
| EAS EZ ACTION IZ        |                                |
| EAS EZ ACTION LZ        |                                |
| EAS EZ ACTION PZ        |                                |
| EAS EZ ACTION RZ        |                                |
| EAS EZ ACTION UF        |                                |
| EAS EZ ACTION VZ        | EAS EZ OPTION REMOVE SIG VERIF |
| EAS EZ DEFINE APP#      |                                |
| EAS EZ DEFINE APPLICANT |                                |
| EAS EZ DEFINE LINE#     |                                |
| EAS EZ DEFINE PRINT     |                                |

*Help Frames (continued)*

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Help Frame</strong></td>
<td><strong>Related Help Frames</strong></td>
</tr>
<tr class="even">
<td>EAS EZ DEFINE REC'D</td>
<td></td>
</tr>
<tr class="odd">
<td>EAS EZ DEFINE SSN</td>
<td></td>
</tr>
<tr class="even">
<td>EAS EZ DEFINE TO</td>
<td></td>
</tr>
<tr class="odd">
<td>EAS EZ DEFINE VET TYPE</td>
<td></td>
</tr>
<tr class="even">
<td>EAS EZ OPTION LOOKUP</td>
<td></td>
</tr>
<tr class="odd">
<td>EAS EZ OPTION PROCESS</td>
<td><p>EAS EZ STATUS NEW</p>
<p>EAS EZ STATUS IN REVIEW</p>
<p>EAS EZ STATUS SIGNED</p>
<p>EAS EZ STATUS FILED</p>
<p>EAS EZ STATUS INACTIVE</p>
<p>EAS EZ SCREEN INITIAL</p>
<p>EAS EZ OPTION LOOKUP</p>
<p>EAS EZ STATUS PRINTED</p></td>
</tr>
<tr class="even">
<td>EAS EZ OPTION REMOVE SIG VERIF</td>
<td></td>
</tr>
<tr class="odd">
<td>EAS EZ SCREEN INITIAL</td>
<td><p>EAS EZ DEFINE APP#</p>
<p>EAS EZ DEFINE APPLICANT</p>
<p>EAS EZ DEFINE PRINT</p>
<p>EAS EZ DEFINE REC'D</p>
<p>ES EZ DEFINE SSN</p>
<p>EAS EZ DEFINE TO</p>
<p>EAS EZ DEFINE VET TYPE</p>
<p>EAS EZ DEFINE LINE#</p></td>
</tr>
<tr class="even">
<td>EAS EZ STATUS FILED</td>
<td>EAS EZ ACTION PZ</td>
</tr>
<tr class="odd">
<td>EAS EZ STATUS IN REVIEW</td>
<td><p>EAS EZ ACTION AF</p>
<p>EAS EZ ACTION AZ</p>
<p>EAS EZ ACTION CZ</p>
<p>EAS EZ ACTION IZ</p>
<p>EAS EZ ACTION PZ</p>
<p>EAS EZ ACTION RZ</p>
<p>EAS EZ ACTION UF</p>
<p>EAS EZ ACTION VZ</p></td>
</tr>
<tr class="even">
<td>EAS EZ STATUS INACTIVE</td>
<td>EAS EZ OPTION LOOKUP</td>
</tr>
<tr class="odd">
<td>EAS EZ STATUS NEW</td>
<td><p>EAS EZ ACTION LZ</p>
<p>EAS EZ ACTION IZ</p></td>
</tr>
<tr class="even">
<td>EAS EZ STATUS PRINTED</td>
<td><p>EAS EZ ACTION IZ</p>
<p>EAS EZ ACTION PZ</p>
<p>EAS EZ ACTION RZ</p>
<p>EAS EZ ACTION VZ</p></td>
</tr>
<tr class="odd">
<td>EAS EZ STATUS SIGNED</td>
<td><p>EAS EZ ACTION FZ</p>
<p>EAS EZ ACTION PZ</p>
<p>EAS EZ ACTION UF</p>
<p>EAS EZ OPTION REMOVE SIG VERIF</p></td>
</tr>
</tbody>
</table>

# # # Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA1010EZ mail group, which was exported to field sites nationally though patch DG\*5.3\*325, is the only mail group used by EAS V. 1.0. All 10-10EZ Application transmissions will be routed to this mail group from the external web server.

Much of the 10-10EZ data is sensitive and covered by Privacy Act regulations. Therefore, only authorized personnel, normally involved in veteran Registration and Enrollment processes, may be members of the VA1010EZ mail group. Ideally, a local Enrollment Coordinator will be assigned as Coordinator of this mail group.

There are no BULLETIN File (#3.6) or ALERT File (#8992) entries associated with EAS V. 1.0.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 10-10EZ Enrollment Application Processor module exported by EAS V. 1.0 depends on receipt of electronic data transmission from the web server located at the following URL:

https://www.1010ez.med.va.gov/sec/vha/1010ez/

The data transmission is in the form of an ASCII text e-mail message, which is delivered to the VA1010EZ Mail Group at the local site.

### Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging procedures entailed in EAS V. 1.0.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special contingency plans have been identified for EAS V. 1.0.

### Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no non-VA software or hardware products needed for direct interface with EAS V. 1.0.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS V. 1.0 does not employ electronic signature functionality.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no menus/options in EAS V. 1.0 that are specifically designed for security purposes.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SECURITY KEY File (#19.1) entries associated with the EAS V. 1.0.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recommended file security as distributed with EAS V. 1.0:

FILE LIST

DD RD WR DEL LAYGO

NUMBER NAME GLOBAL NAME

-----------------------------------------------------------------------------------------

711 1010EZ MAPPING ^EAS(711, @ @ @ @ @

712 1010EZ HOLDING ^EAS(712, @ @ @ @ @

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                              |                                                                                                                                                                                            |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10-10EZ                                  | A VA form used by veterans to apply for VHA health benefits                                                                                                                                |
| 10-10EZ Enrollment Application Processor | An application that allows local V*IST*A systems to electronically process applications for enrollment and healthcare benefits filled out by veterans via a web-based application. |
| EAS                                      | Enrollment Application System                                                                                                                                                              |
| VA                                       | Department of Veterans Affairs                                                                                                                                                             |
| VHA                                      | Veterans Health Administration                                                                                                                                                             |
| V*IST*A                                  | VHA Information Systems and Technology Architecture                                                                                                                                        |

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Archiving & Purging 7

Archiving/Purging 15

C

Callable Entry Points & APIs 8

Contingency Planning 15

E

Electronic Signatures 16

Exported Options 6

External Interfaces 8

External Relations 8

F

File Security 16

Files 5

Forum Components 9

G

Glossary 17

H

Help Frames 13

I

Implementation 4

Implementation and Maintenance 4

Integration Agreements 8

Interfaces 15

Internal Relations 11

Introduction 2

L

List Templates 12

M

Mail Groups and Alerts 15

Maintenance 4

Menus 16

O

Other Software Elements 11

Overview 2

P

Package-wide Variable 11

Protocols 12

Purpose 2

R

Related Manuals 3

Remote Systems 15

Routines 6

S

Security 15

Security Features 15

Security Keys 16