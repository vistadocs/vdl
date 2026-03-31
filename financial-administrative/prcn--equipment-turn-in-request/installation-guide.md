---
title: PRCN Version 1 Installation Guide Release Notes
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes
app_code: PRCN
app_name: Equipment / Turn-In Request
section: FIN
app_status: active
pkg_ns: PRCN
patch_ver: 1
patch_id: PRCN*1
group_key: "PRCN:PRCN:1"
file_numbers: []
security_keys: []
menu_options: 5
description: - [PREFACE](#preface) - [CHAPTER 1 RELEASE NOTES](#chapter-1-release-notes) - [CHAPTER 2 PRE-INSTALLATION](#chapter-2-pre-installation) - [Equipment Request Menu table](#equipment-request-menu-table) - [Turn-In Menus](#turn-in-menus) - [Set-Up Procedures](#set-up-procedures) - [Patches](#patches) -
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - strong
  - class
  - rowspan
  - installation
  - equipment
  - turn
  - even
page_count: 0
word_count: 1528
section_count: 10
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=113"
---

> [Department of Veterans Affairs Decentralized Hospital Computer Program](\l)

[EQUIPMENT/TURN-IN REQUEST INSTALLATION GUIDE](#_bookmark0)

[RELEASE NOTES](#_bookmark0)

> [Version 1.0 June 1996](#_bookmark0)

> [Information Resource Management Field Office Washington, DC](#_bookmark0)

# [PREFACE](\l)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PREFACE](#preface)
- [CHAPTER 1 RELEASE NOTES](#chapter-1-release-notes)
- [CHAPTER 2 PRE-INSTALLATION](#chapter-2-pre-installation)
  - [Equipment Request Menu table](#equipment-request-menu-table)
  - [Turn-In Menus](#turn-in-menus)
  - [Set-Up Procedures](#set-up-procedures)
  - [Patches](#patches)
  - [Description of Installation:](#description-of-installation)
- [CHAPTER 3 INSTALLATION](#chapter-3-installation)
  - [\> D ^XPDKRN \<RET\>](#d-xpdkrn-ret)
  - [\>D ^XPDKRN \<RET\>](#d-xpdkrn-ret-1)
  - [\<RET\>](#ret)
  - [\\\ NOTE: If you are installing on an MSM system, you will be asked to move routines to other CPUs. Make sure you move routines to all Compute/Print Servers..\\\](#note-if-you-are-installing-on-an-msm-system-you-will-be-asked-to-move-routines-to-other-cpus-make-sure-you-move-routines-to-all-computeprint-servers)
- [CHAPTER 4 POST-INSTALLATION](#chapter-4-post-installation)
- [APPENDIX](#appendix)
> [This document describes new features and functionality of the Equipment/Turn-In Request Module V. 1.0, and is included among the following mandatory components of DHCP software documentation.:](#table-of-contents)
- [Installation Guide/Release Notes (combined or as separate documents)](#table-of-contents)
- [Technical Manual](#table-of-contents)
- [Package Security Guide](#table-of-contents)
- [User Manual(s)](#table-of-contents)
> [This document uses a paragraph numbering system that helps the reader understand how the sections of the document relate to each other. For example, suppose this paragraph was section 1.3. Under the numbering system, this paragraph would be the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections. 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. Actually, what you have is a tool (numbering system) in place that allows the reader to more easily follow the logic of sections of information that contain several subsections.](#table-of-contents)
> Preface

# [CHAPTER 1 RELEASE NOTES](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [The Equipment/Turn-In Request Module has two components; it includes the ability to request new non-expendable equipment and replacement equipment and also the ability to turn-in old equipment. Non-expendable equipment must go through many stages of review and approval before it can finally be ordered. This module is meant to help track a request through each step and also to maintain important information about requests that can be used later for reports. Turn-Ins must also go through several stages of review and approval before equipment can be removed from inventory.](#table-of-contents)

> [This module introduces a new type of official to IFCAP, the Consolidated Memorandum of Receipt (CMR) Official. This is the person who is ultimately responsible for non-expendable equipment that currently exists at the Medical Center and who will be reponsible for any new equipment that will be ordered.](#table-of-contents)

> [The Equipment/Turn-In Request Module has very close ties to the Engineering package, particularly for the Turn-In part of the module. Removal of old equipment may generate a work order for removal and final disposition will remove the item from inventory. Engineering plays a part in an equipment request also, providing information about the installation, training, and maintenance impact of any new equipment that may be purchased.](#table-of-contents)

> [Release Notes](#table-of-contents)

# [CHAPTER 2 PRE-INSTALLATION](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Equipment/Turn-In Request Version 1.0 introduces new functionality in IFCAP to track both equipment requests up to 2237 processing and turn-in requests through final Personal Property Manager disposition. Please review Chapter 1 Release Notes and the User Manual for more detailed information on this new functionality.](#table-of-contents)

> [The Equipment/Turn-In Request Package has been assigned PRCN as its namespace.](#table-of-contents)

> [Installation of the following packages must be accomplished for Equipment/Turn-In Request V. 1.0 to function properly.](\l)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#table-of-contents"><u>Application</u></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><u>Minimum Version Number</u></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Kernel</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">8.0</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">VA FileMan</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">21.0</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Engineering</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">7.0</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">Patch</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">EN*7*25</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">IFCAP</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">5.0</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents"><strong>2.2.3 File Range</strong></a></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> [Equipment Request/Turn-In File Range: 413 - 413.9](#table-of-contents)

> [The PRCN global is created when loading as a virgin install. PRCN should be defined with access privileges; RWD for System, World, Group and UCI, using %GLOMAN for DSM and %GCH for MSM. This should be the same access level as the Engineering and IFCAP globals.](#table-of-contents)

> [No special hardware or software is needed for this package.](#table-of-contents)

> [Before you begin the installation, please get together with potential users to determine who will be assigned which menus and security keys. Signature codes may also have to be entered. Please ensure that your CMR file in AEMS/MERS is complete and up-to-date as this module depends on the CMR responsible officials.](#table-of-contents)

> [Some of the users of the Equipment Request/Turn-In File are as follows:](#table-of-contents)

> Pre-Installation

- Requestor
- CMR Official
- Personal Property Manager (PPM)
- Engineering
- Concurring Officials
- Equipment Committee
- Warehouse

> The following table shows the main menu and associated security key that are to be assigned to a particular type of user. Some users may have overlapping capabilities assigned if necessary.

Pre-Installation

## Equipment Request Menu table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"><strong>User</strong></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p><strong>Electronic</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>Menu Text</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Associated</strong></p>
</blockquote></th>
<th><strong>Signature</strong></th>
</tr>
<tr class="header">
<th><strong>(seen by user)</strong></th>
<th><strong>(used by computer)</strong></th>
<th><strong>Security key(s)</strong></th>
<th><blockquote>
<p><strong>Required</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Requestor</td>
<td>Equipment Request Menu (Requestor)</td>
<td>PRCN NX MENU</td>
<td></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">CMR Official</td>
<td><blockquote>
<p>CMR Official</p>
</blockquote></td>
<td>PRCN NX CMR</td>
<td rowspan="3">PRCNCMR</td>
<td rowspan="3"><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Equipment Request</td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Personal Property</td>
<td>Equipment Request</td>
<td>PRCN NX PPM</td>
<td rowspan="2">PRCNPPM</td>
<td rowspan="2"><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Manager</td>
<td><blockquote>
<p>Menu (PPM)</p>
</blockquote></td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3">Engineering</td>
<td>Engineering</td>
<td>PRCN NX ENG</td>
<td rowspan="3">PRCNEN</td>
<td rowspan="3"><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Equipment Request</td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="3">Concurring Officials</td>
<td>Equipment</td>
<td>PRCN NX CONC</td>
<td rowspan="3"></td>
<td rowspan="3"><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Concurring Official</p>
</blockquote></td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Equipment</td>
<td>Equipment</td>
<td>PRCN NX EQ</td>
<td rowspan="3">PRCNEQP</td>
<td rowspan="3"><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Committee</td>
<td><blockquote>
<p>Committee Menu</p>
</blockquote></td>
<td><blockquote>
<p>COMM MENU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Members</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Either the PPM or</td>
<td rowspan="4"><blockquote>
<p>Rank NX Requests</p>
</blockquote></td>
<td>PRCN NX EQ</td>
<td rowspan="4">PRCNRNK</td>
<td rowspan="4"><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>other Equipment</td>
<td><blockquote>
<p>COMM MENU or</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Committee member</td>
<td>PRCN NX PPM</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pre-Installation

## Turn-In Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"><span id="2.2.7_Set-Up_Procedures" class="anchor"></span><strong>User</strong></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p><strong>Electronic</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>Menu Text</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Associated</strong></p>
</blockquote></th>
<th><strong>Signature</strong></th>
</tr>
<tr class="header">
<th><strong>(seen by user)</strong></th>
<th><strong>(used by computer)</strong></th>
<th><strong>Security key(s)</strong></th>
<th><blockquote>
<p><strong>Required</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">Requestor</td>
<td>Process Turn-Ins</td>
<td>PRCN TURN</td>
<td rowspan="2"></td>
<td rowspan="2"><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CMR Official</td>
<td>Process Turn-Ins Menu</td>
<td>PRCN TURN MENU</td>
<td>PRCNCMR</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Personal Property Manager</td>
<td>Process Equipment Turn-In Request (PPM)</td>
<td>PRCN TURN PPM</td>
<td rowspan="3">PRCNPPM</td>
<td rowspan="3"><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Final Turn-In</td>
<td>PRCN TURN DISP</td>
</tr>
<tr class="even">
<td>Request Disposition (PPM)</td>
<td></td>
</tr>
<tr class="odd">
<td>Warehouse</td>
<td><blockquote>
<p>Warehouse Turn-In Menu</p>
</blockquote></td>
<td>PRCN TURN WHSE MENU</td>
<td>PRCNWHSE</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Set-Up Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no special set-up procedures prior to installation. Please review 4.2 for post-installation set-up procedures.

## Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please be sure that you have loaded Engineering Patch 25 prior to installation of this package.

## Description of Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are a beta or alpha site, please make sure you do not have Equipment/Turn-In users on the system and that a backup has been made of your system before running the installation. Other users can be on the system during installation of this package.

# [CHAPTER 3 INSTALLATION](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Estimated time to install this module is approximately 10 minutes. Expect to spend at least 30 minutes setting up users, security keys, and options.](#table-of-contents)

> [\>K \<RET\>](#table-of-contents)

> [Setting up programmer environment Access Code: CODE \<RET\>](#table-of-contents)

> [Terminal Type set to: C-VT220 Select OPTION NAME: \<RET\>](#table-of-contents)

> [KIDS 8.0](#table-of-contents)

> [Select KIDS OPTION: LOAD A DISTRIBUTION \<RET\>](#table-of-contents)

> [Enter a Host File: PRCN.KID \<RET\>](#table-of-contents)

> [KIDS Distribution saved on Jun 21, 1996@13:06:57 Comment: EQUIPMENT/TURN-IN REQUEST VERSION 1.0](#table-of-contents)

> [This Distribution contains Transport Globals for the following Package(s): EQUIPMENT/TURN-IN REQUEST 1.0](#table-of-contents)

> [Want to Continue with Load? YES// \<RET\>](#table-of-contents)

> [Loading Distribution...](#table-of-contents)

> [Want to RUN the Environment Check Routine? YES// \<RET\>](#table-of-contents)

> [Will first run the Environment Check Routine, PRCNINST](#table-of-contents)

> [A Report on the State of Your CMR file (6914.1) follows. DEVICE: HOME// QUEUE TO PRINT ON \<RET\> DEVICE: HOME// R88 \<RET\> HPLASERII](#table-of-contents)

> Installation

> Requested Start Time: NOW// \<RET\> (JUN 21, 1996@13:19:09) Use EQUIPMENT/TURN-IN REQUEST 1.0 to install this Distribution. Other possible environment check messages installer may see:

## \> D ^XPDKRN \<RET\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> KIDS 8.0

> Select KIDS OPTION: 5 \<RET\> VERIFY CHECKSUMS IN TRANSPORT GLOBAL

> Select INSTALL NAME: EQUIPMENT/TURN-IN REQUEST 1.0 \<RET\> Loaded

> from Distribution 6/27/96@15:20:23

> =\> EQUIPMENT/TURN-IN REQUEST VERSION 1.0 ;Created on Jun 21, 1996@13:06:57

> DEVICE: HOME// \<RET\>

> PACKAGE: EQUIPMENT/TURN-IN REQUEST 1.0 Jun 21, 1996 1:19 pm PAGE 1

> -------------------------------------------------------------------------------

> 40 Routine checked, 0 failed.

## \>D ^XPDKRN \<RET\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation

> KIDS 8.0

> Select KIDS OPTION: INSTALL PACKAGE(S) \<RET\>

> Select INSTALL NAME: EQUIPMENT/TURN-IN REQUEST 1.0 \<RET\>

> Loaded from Distribution

> This Distribution was loaded on Jun 21, 1996@13:18:36 with header of EQUIPMENT/TURN-IN REQUEST VERSION 1.0 ;Created on Jun 21, 1996@13:06:57

> It consisted of the following Install(s): EQUIPMENT/TURN-IN REQUEST 1.0

> Will first run the Environment Check Routine, PRCNINST A Report on the State of Your CMR file (6914.1) follows.

> DEVICE: HOME// \<RET\>

> Install Questions for EQUIPMENT/TURN-IN REQUEST 1.0

413. EQUIPMENT REQUEST
     1.  TURN-IN REQUEST
     2.  EQUIPMENT COMMITTEE
     3.  CONCURRING OFFICIALS
     4.  SPECIAL HANDLING CODES (including data)
     5.  NX STATUS (including data)

> 413.7 COUNTER

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

## \<RET\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation

## \*\*\* NOTE: If you are installing on an MSM system, you will be asked to move routines to other CPUs. Make sure you move routines to all Compute/Print Servers..\*\*\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> WANT TO MOVE ROUTINES TO OTHER CPUS? NO// YES \<RET\>

> ENTER VOLUME SET YOU WANT ME TO UPDATE SELECT VOLUME SET:

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<RET\>

> Install Started for EQUIPMENT/TURN-IN REQUEST 1.0 : Jun 21, 1996@13:20:58

> Installing Routines:.........................................

> Jun 21, 1996@13:21:09

> Installing Data Dictionaries: ........

> Jun 21, 1996@13:22:05

> Installing Data:

> Jun 21, 1996@13:22:08

> Installing PACKAGE COMPONENTS: Installing BULLETIN............

> Installing SECURITY KEY........

> Installing PRINT TEMPLATE.........

> Installing SORT TEMPLATE.. Installing INPUT TEMPLATE...............

> Installing OPTION.................................................

> Jun 21, 1996@13:26:24

> Updating Routine file....

> The following Routines were created during this install:

Installation

> PRCNX PRCNX1 PRCNX2 PRCNX3 PRCNX4 PRCNX5 PRCNX6 PRCNX7 PRCNX8..

> Updating KIDS files.......

> EQUIPMENT/TURN-IN REQUEST 1.0 Installed.

> Jun 21, 1996@13:27:12

> Install Message sent \#nnnnn Install completed

> \>

> Installation

# [CHAPTER 4 POST-INSTALLATION](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Please do the following after the successful installation of Version 1.0:](#table-of-contents)

> [a. Assign menu options and security keys.](#table-of-contents)

> [Mail Groups will not be needed for the new bulletins installed. However, you will need to do the following steps:](#table-of-contents)

> [During the install a check will be performed on the CMR File (6914.1). This check will look for the following problems; no CMR Official, no CMR Service, non-pointer data, and non-existing data in the pointed to file.](#table-of-contents)

> [Note: Please ensure that there are valid entries for the Responsible Official and the Alternate Responsible Official before using the Equipment/Turn-In Module.](#table-of-contents)

> [Post-Installation](#table-of-contents)

# [APPENDIX](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [VERSION 5.0 OF IFCAP HAS NOT BEEN LOADED](#table-of-contents)

> [Your site has not loaded version 5.0 of IFCAP or the version number has not been set correctly in the Package file (9.4).](#table-of-contents)

2.  [VERSION 7.0 OF ENGINEERING HAS NOT BEEN LOADED](#table-of-contents)

> [Your site has not loaded version 7.0 of Engineering or the version number has not been set correctly in the Package file (9.4).](#table-of-contents)

3.  [Engineering Patch 25 not loaded yet!](#table-of-contents)

> [Two Engineering programs released in patch 25 are missing. Please load patch EN\*7\*25 and start installation again.](#table-of-contents)

> [Prior to release of Engineering v.7.0, the RESPONSIBLE OFFICIAL and the SERVICE fields were defined as free text fields but were changed in version 7.0 to point to their respective files; \#200 and \#49. If you receive a message about a pointer, it means that the free text was never edited to the correct entry. Please be sure that the appropriate A&MM person has menu option, CMR File Enter/Edit \[ENCMR\] so that the entries may be corrected.](#table-of-contents)

> [The install report:](#table-of-contents)

1.  [Lists CMRs with no defined CMR Responsible Official.](#table-of-contents)
2.  [Lists CMRs with no defined Service.](#table-of-contents)
3.  [Lists CMRs with non-pointer CMR Responsible Official.](#table-of-contents)
4.  [Lists CMRs with non-pointer Service.](#table-of-contents)
5.  [Lists CMRs with missing pointer value for CMR Responsible Official.](#table-of-contents)
6.  [Lists CMRs with missing pointer value for Service.](#table-of-contents)

> [A Report on the State of Your CMR file (6914.1) follows. DEVICE: HOME// 0;;65 VIRTUAL TERMINAL](#table-of-contents)

> [CMR OFFICIAL IS NOT POINTER FOR 140 CMR OFFICIAL IS NOT POINTER FOR 160 CMR OFFICIAL IS NOT POINTER FOR 204 NO CMR OFFICIAL DEFINED FOR 230 NO CMR OFFICIAL DEFINED FOR 360 CMR OFFICIAL IS NOT POINTER FOR 470 NO CMR OFFICIAL DEFINED FOR 501 NO CMR SERVICE DEFINED FOR 501](#table-of-contents)

> Appendix