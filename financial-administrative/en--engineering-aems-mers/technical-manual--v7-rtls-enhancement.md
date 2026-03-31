---
title: EN Version 7 RTLS Enhancement Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: RTLS Enhancement
app_code: EN
app_name: Engineering (AEMS / MERS)
section: FIN
app_status: active
pkg_ns: EN
patch_ver: 7
patch_id: EN*7
group_key: "EN:EN:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - class
  - even
  - style
  - width
  - table
  - colspan
  - colgroup
  - thead
  - tbody
page_count: 0
word_count: 14267
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/eng_tm_en_7_100.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/eng_tm_en_7_100.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=37"
---

> Department of Veterans Affairs Decentralized Hospital Computer System

ENGINEERING TECHNICAL MANUAL

> Version 7.0

> August 1993

> Revised August 2017

> Information Systems Center Washington, D.C.

> Preface

> This Technical Manual presents the major features of the Engineering system Automated Engineering Management System /Medical Equipment Reporting System (AEMS/MERS). This manual may be used by anyone having access to the system, from novice user to system manager, as a reference text and as a guide to understanding the package as a whole.

> Note: patch EN\*7.0\*100 added new cross-references to the EQUIPMENT INV. file (#6914) and ENG SPACE file (#6928) for support of the Real Time Location System (RTLS) interface between VistA and Intelligent Insites. However, the new cross references do not change any menu options available in the Engineering package.

> Preface

[Introduction 1-1](#introduction)

[Manual Use 1-1](#manual-use)

[On-line Access](#introduction) 1-1

Standard [Package Conventions](#introduction) 1-1

Ge[neral Description](#_bookmark2) 1-2

Imp[lementation and Maintenance 2-1](#_bookmark3)

[Naming Conventions 2-1](#naming-conventions)

[Files](#implementation-and-maintenance) 2-1

Se[curity Keys](#implementation-and-maintenance) 2-1

Gl[obals](#_bookmark6) 2-2

[Utilities](#_bookmark7) 2-2

[Resource Requirements](#_bookmark8) 2-2

Te[mplates](#utilities) 2-2

[New Functionality](#resource-requirements) 2-4

[Implementation and Maintenance](#_bookmark11) 2-5

[Engineering Software Options](#_bookmark12) 2-7

Routine [Descriptions](#_bookmark13) 3-1

[File List](#routine-descriptions) 4-1

[File List 4-1](#_bookmark16)

[Pointer Relationships of Files](#file-list) 4-6

Fil[es with Security Access](#file-list) 4-22

Expo[rted Options](#_bookmark17) 5-1

[Cross References](#exported-options) 6-1

[File Diagram](#cross-references) 7-1

[Archiving/Purging Data](#_bookmark20) 8-1

[Callable Routines](#archivingpurging-data) 9-1

[External Relations](#callable-routines) 10-1

[Internal Relations](#external-relations) 11-1

[Package-Wide Variables](#internal-relations) 12-1

[On-Line Documentation](#package-wide-variables) 13-1

[Glossary](#on-line-documentation) 14-1

> Revision History

> Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Description (Patch # if applic.)</p>
</blockquote></th>
<th><blockquote>
<p>Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Technical Writer</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>08/2017</p>
</blockquote></td>
<td><blockquote>
<p>Updated with Patch EN*7.0*100, ENGINEERING SUPPORT FOR</p>
<p>RTLS (Section 6-2)</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/2008</p>
</blockquote></td>
<td><blockquote>
<p>*Updated with Patch EN*7*87, IT EQUIPMENT TRACKING ENHANCEMENT</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192-352 Displaying Sensitive</p>
<p>Data.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Pdf file checked for accessibility to readers with disabilities.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \* Please note that the technical manual has been updated for enhancement patches EN\*7\*87 (IT Equipment Tracking) and EN\*7\*100 (RTLS), but has not been updated for other patches since the release of Version 7.0 in August 1993.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Manual Use](#manual-use)
  - [On-line Access](#on-line-access)
  - [Standard Package Conventions](#standard-package-conventions)
  - [General Description](#general-description)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Naming Conventions](#naming-conventions)
  - [Files](#files)
  - [Security Keys](#security-keys)
  - [Globals](#globals)
  - [Utilities](#utilities)
  - [Resource Requirements](#resource-requirements)
  - [Templates](#templates)
  - [New Functionality](#new-functionality)
  - [Implementation and Maintenance](#implementation-and-maintenance-1)
  - [Engineering Software Options](#engineering-software-options)
- [Routine Descriptions](#routine-descriptions)
- [File List](#file-list)
  - [Pointer Relationships of Files](#pointer-relationships-of-files)
  - [Files with Security Access](#files-with-security-access)
- [Exported Options](#exported-options)
- [Cross-References](#cross-references)
- [Archiving/Purging Data](#archivingpurging-data)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [On-Line Documentation](#on-line-documentation)
- [Glossary](#glossary)
    - [ALD - Abbreviation for appropriation, limitation, department.](#ald-abbreviation-for-appropriation-limitation-department)

## Manual Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Engineering system is designed for effective interaction for all user levels, from the novice user to the site manager. A knowledge of VA FileMan user protocol is all<span id="_bookmark2" class="anchor"></span> that is required to use the system.

## On-line Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon gaining access to the system, the user is prompted for a menu selection at each level of the system. If the user wishes a list of available selections entering a

> \<?\> will bring up a list of available selections. \<??\> will give additional information, and \< ?OPTIONS\> will list further options. The user should enter a carriage return to accept a default answer, or enter a new value.

> Entries may be made in either upper case or lower case characters, as the fields are not case sensitive. If a long entry is being entered, only the first few letters of the entry should be typed, as three letters are sufficient for entry identification. If an entry is ambiguous, a question mark will appear, and the selection prompt is automatically reprinted for the viewer. If there is more than one selection for an entry, a list of all possible selections appears, from which the viewer can choose a selection by entering either the name or number of the selection.

## Standard Package Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the Engineering User Manual for information on standard package conventions.

> <span id="_bookmark3" class="anchor"></span>Introduction

## General Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DHCP Engineering package consists of nine (9) separate but interrelated modules.

1.  Work Order and MERS
2.  Project Planning
3.  Project Tracking
4.  Equipment Management
5.  Space/Facility Management
6.  Program Management
7.  2162 Accident Reporting
8.  Assign (Transfer) Electronic Work Orders
9.  IT Equipment Tracking

> Work Order and MERS

> The Work Order and MERS module generates control numbers for Engineering work requests and provides a way of assigning work requests to specific Engineering shops, assigning personnel to work orders, and charging work orders to specific pieces of equipment. It is the basis for automated repair histories on all types of equipment. Although preventive maintenance inspections are scheduled and recorded using the Equipment Management module, the actual PM work orders that constitute a PM worklist are physically stored in the Work Order file. Special options exist for displaying incomplete work orders and for transferring electronic work orders (work requests typed into DHCP by end-users and not by Engineering) from a "receiving area" to a working shop.

> Project Planning

> The Project Planning module provides enter/edit options for information that appears on the 5-Year Plan for each project. It also has options to process information required for project application forms and Prioritization Scoring Sheets for NRM, Minor, and Minor Misc. programs.

> The Approval of Project Application option controls the Chief Engineer's and VAMC Director's sign off on the project application. The security key ENPLK001 controls the Chief Engineer's approval. The security key ENPLK002 controls the VAMC Director's approval. The Chief Engineer must sign off before the VAMC Director.

> Both must approve before the project application can be transmitted electronically to higher approval authorities.

> The Report/Print Menu options provide print-outs of the reports and forms required by project planning.

> The Electronic Transmission Menu contains options for electronic transmission of the 5-Year Plan and Project Application data elements.

Introduction

> Project Tracking

> The Project Tracking module is used to record significant events during construction and nonrecurring maintenance projects when the management of such a project has been delegated to the facility. Selected data elements are extracted from the Construction Project file and electronically transmitted to the Regional Construction Office and VACO. In this way, up-to-date project tracking information is made available to all interested parties with a minimum of data entry.

> The content of the most recent electronic project progress report is always available for reference. Printouts of progress reports will include an asterisk beside data that differs from what was previously reported. If progress reports are directed to a CRT, changes will be highlighted.

> Equipment Management

> The Equipment Management module contains the options to maintain inventory and preventive maintenance information, print bar code labels, download control programs to portable bar code readers, upload data from portable bar code readers to DHCP, and to manage CMR (Consolidated Memoranda of Receipt).

> Equipment records generally exist for non-expendable personal property, building service equipment, and for equipment that is classified as expendable from the materiel management point of view but which must be periodically inspected by Engineering. These inspections are necessary to satisfy the requirements of JCAHO (Joint Commission on the Accreditation of Healthcare Organizations) and/or other regulatory bodies. The Equipment Management module includes all options necessary for establishing and maintaining a comprehensive preventive maintenance program. Bar coding is now an integral part of the equipment management strategies.

> The reports available through the Equipment Management module include:

1.  Repair histories,
2.  CMR listings,
3.  Aggregated repair histories (b y Equipment Category),
4.  Warranty expiration listings,
5.  Equipment replacement listings,
6.  Equipment with high failure rates, and
7.  Preventive maintenance workload (by shop).

> The Equipment Management module is tightly coupled to the Work Order module. Equipment Histories are automatically updated as work orders are closed out. Redundant data entry is avoided whenever possible.

> Introduction

> Although entries in the Equipment Repair Histories are most commonly made by the system when work orders are closed out, users can also make entries without going through the Work Order module. Equipment records to be updated by direct posting may be selected individually or they may be contained in a VA FileMan sort template. If a sort template is used, it must begin with "ENPOST."

> Program Management

> The Program Management module contains options for site-specific population and/or maintenance of files used in the Engineering package. This option is only available to the Engineering Applications Manager or Engineering Site Manager. It is where the various lists are established and maintained. The Engineering Employee file and the Equipment Category list must be maintained on a continuing basis. Populated copies of the Equipment Category file are available from your supporting ISC upon request.

> Space/Facility Management

> This module is used to maintain data on physical locations within the host facility (usually a VA Medical Center). Data elements include square footage; wall, ceiling and floor finishes; window types and treatments; and other architectural features. This module also provides control of locks and keys throughout a facility. Bar coded location labels are printed from the Space file on the basis of room number.

> Facilities that intend to take advantage of the bar code features in the Equipment Management module should insure that the Building file is completely current and that the Space file contains at least a room number (including building and division, if applicable) for each physical location. The proper format for a room number (which must be unique and unambiguous) is Room-Building-Division. Most single division facilities will need to enter only Room-Building.

> The 2162 Accident Reporting

> This module collects the data elements of VA Form 2162 so that accidents and on- the-job injuries can be aggregated and analyzed by Service/Section, cause of accident, nature of accident, etc.

> Assign (Transfer) Electronic Work Orders

> This option was developed to facilitate the process of transferring electronic work orders from the receiving area(s) to a working shop. Users may also disapprove electronic work orders when necessary. In such a case, the COMMENTS field is automatically mailed to whoever entered the work order, along with the information that the request has been disapproved.

Introduction

> IT Equipment Tracking

> This module contains options for IT staff to edit selected equipment inventory data of IT equipment, track IT equipment, and assign responsibility for IT equipment to individuals. The module contains options for individuals to accept responsibility for IT equipment by signing an electronic hand receipt. The module also provides IT staff with access to select Equipment Management module options.

> IT equipment is identified based on the CMR (EIL) field. If an equipment item is on a CMR with IT TRACKING equal to YES, the equipment is considered tracked IT equipment. The CMR File Enter/Edit \[ENCMR\] option can be used by Acquisition & Materiel Management (A&MM) to edit the IT TRACKING field.

> Only tracked IT equipment can be edited using the Inventory Edit (IT) option. All tracked IT equipment is expected to be assigned to individual IT owners.

> The IT Equipment Tracking module is tightly coupled with the Equipment Management module.

> Introduction

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark6" class="anchor"></span>The namespace used by the Engineering package is EN. Within this package namespace, the Equipment Management module uses a namespace of ENEQ; the Work Order module uses the namespace of ENWO; the IT equipment tracking functionality uses the namespace ENIT and ENTI; and the Project Planning and Project Tracking modules use the namespace ENP.

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Engineering package contains 34 files. The file numbers range from 6910 through (and including) 6929; and 7330 through 7339.9.

> <span id="_bookmark7" class="anchor"></span>The File List section of this manual provides additional file information.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Engineering contains the following security keys.

> ENEDCLWO - Enables holders of this key to edit closed work orders.

> ENEDNX - Safeguards critical data elements of non-expendable (NX) equipment records in File 6914. Users must hold this key to edit CMR, COST, OWNERSHIP, or CATEGORY STOCK NUMBER using the data entry screens.

> ENEDPM - Enables holders to edit Preventive Maintenance parameters of entries in the Equipment Inv. file at completion of screen edit of an equipment record.

> ENMGR - Enables holders to access the Engineering Program Management functions. (The appropriate menu option will also need to be assigned.)

> ENPLK001 - Controls the Chief Engineer/Designee approval of Construction Project Application.

> ENPLK002 - Controls the VAMC Director/Designee approval of Construction Project Application.

> ENPLK003 - Controls access to electronic transmission of 5-Yr Plan and Project Application.

> ENROOM - Enables holders to edit data elements in the Space file from the Room Display option (ENSPROOMD).

> EN IT ASSIGNMENT - Enables holders to create, transfer, and terminate assignments of responsibility for IT equipment. Also provides access to the Add Entry to New Person File option.

> EN IT INVENTORY - Enables holders to edit IT equipment in the EQUIPMENT INV. File using the Inventory Edit (IT) option.

> <span id="_bookmark8" class="anchor"></span>Implementation and Maintenance

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Engineering package uses four (4) namespaced globals: ENG, ENAR, ENGS and OFM. Journalling is only recommended for the ENG global.

## Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> General purpose utility functions are contained in ENLIB, ENLIB1, and ENLIB2 routines. Bar code utilities are found in routines ENCTFLD, ENCTQUES, ENCTRCH, ENCTRED, and ENCTUTL. Routines in the ENCT namespace are the work of IFCAP developers. The Engineering developer gratefully acknowledges their contributions.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Disk space required for data storage will vary greatly from site to site depending upon such<span id="_bookmark11" class="anchor"></span> variables as level of activity and archiving policies. At an average site, Engineering files would probably consume between 50 and 100 megabytes of disk space.

> This version frequently invokes VA Kernel Version 6.5 or later and VA FileMan Version

1.  or later for device selection, task queuing, data entry, and data presentation.

> The Project Application, 5-Yr Plan and Environmental Analysis (Form 1193a) reports require a printer capable of printing 132 columns. A laser printer is highly recommended for this. Bar code printers and bar code readers are required to use the bar code feature of the Equipment Management module.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Wherever possible, Engineering gives sites the option of defining input, print, and sort templates to be used instead of those that are distributed with the package. The general convention is that ENZ\* templates take precedence over all others.

> For example, input template ENWOWARD was developed for entry of electronic work orders by non-Engineering personnel. If, however, an input template named ENZWOWARD has been defined then it will be used instead of ENWOWARD.

> Allowable ENZ\* templates and their affects are listed below.

> INPUT TEMPLATES

> ENZEQENTER Entry of new equipment records via FileMan line editor. ENZPMCLOSE Close out of preventive maintenance (PM) work orders. ENZSPENTER Entry of data into the Space file.

> ENZWOBIOCLSE Close out of unscheduled biomedical (shop \#35) work orders. ENZWOCLOSE Close out regular work orders (non-biomedical).

> ENZWOEDIT Edit regular work orders (including those generated by failed PM inspections).

> ENZWONEW Entry of new work orders by Engineering personnel.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Implementation and Maintenance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENZWONEWCLOSE</p>
</blockquote></td>
<td><blockquote>
<p>Close out of work orders at the time the work order is entered.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZWOWARD</p>
</blockquote></td>
<td><blockquote>
<p>Edit of electronic work order s by the initiator.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZWOWARDXFER</p>
</blockquote></td>
<td><blockquote>
<p>Transfer of electronic work orders from a receiving area to a</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>working shop.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZWOXFER</p>
</blockquote></td>
<td><blockquote>
<p>Transfer of work orders from one working shop to another.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PRINT TEMPLATES</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZCMR</p>
</blockquote></td>
<td><blockquote>
<p>CMR Report (Consolidated Memorandum of Receipt).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZEQ EQUIP. LIST</p>
</blockquote></td>
<td><blockquote>
<p>Inventory lists by EQUIPMENT CATEGORY, LOCATION,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>OWNING SERVICE, RESPONSIBLE SHOP, or USE STATUS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Engineering Software Option INVENTORY TEMPLATE must be</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>set to "L" before this template will take effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZEQ REPLACEMENT</p>
</blockquote></td>
<td><blockquote>
<p>Equipment replacement report. Engineering Software Option</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EQUIPMENT REPLACEMENT TEMPLATE must be set to "L"</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>before this template will take effect.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZEQ WARRANTY</p>
</blockquote></td>
<td><blockquote>
<p>Warranty expiration report. Engineering Software Option</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WARRANTY EXPIRATION TEMPLATE must be set to "L"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>before this template will take effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZFSA1</p>
</blockquote></td>
<td><blockquote>
<p>Accident reports. Engineering Software Option SAFETY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PRINTOUT must be set to "L" before this template will take</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>effect.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZSPRM</p>
</blockquote></td>
<td><blockquote>
<p>Space survey reports. Engineering Software Option SPACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SURVEY PRINTOUT must be set to "L" before this template will</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>take effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZWOD1</p>
</blockquote></td>
<td><blockquote>
<p>Work Orders. Locally developed preamble and postamble</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>routines which should consist of one or more WRITE commands.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Output from this routine will appear at the top of the formatted</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>work orders.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZWOD2</p>
</blockquote></td>
<td><blockquote>
<p>Work Orders. ENZWO2 should also consist of one or more</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>WRITE commands. Output from this routine will appear at the</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>bottom of the formatted work orders.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>SORT TEMPLATES</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENZCMR</p>
</blockquote></td>
<td><blockquote>
<p>CMR Report (Consolidated Memorandum of Receipt).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENZLEASE</p>
</blockquote></td>
<td><blockquote>
<p>Space survey of leased buildings.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark12" class="anchor"></span>Implementation and Maintenance

## New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Work Orders/MERS

> Work orders are automatically generated for failed preventive maintenance inspections if the preventive maintenance is recorded via bar code reader or electrical safety analyzer. If being done manually, the user will be prompted for the creation of a regular work order.

> The Incomplete Work Order option now allows counts (by shop) as well as by incomplete work orders.

> The LOCATION field is now a pointer to the Space file rather than free text.

> There is a new set of work actions which includes 31 choices. Before installing Version 7.0, sites must install Patch EN\*6.5\*5. Pointers to the New Work Action file must be established for all existing WORK ACTIONS before Version 7.0 can be installed.

> With Version 7.0, as many as four different work actions may be associated with each work order. Work order numbers can now be printed in bar code on the hard copy of the work order.

> Projects

> The Five Year Facility Plans can now be prepared within AEMS/MERS and transmitted to the Regions electronically. They may also be printed in hard copy.

> Project applications (Form 1193, and Form 1193a) may be entered into AEMS/MERS and electronically transmitted to the Regional Construction Offices for approval. The information will be carried over into the Construction Project Progress Reporting options.

> Prioritization scores are calculated for proposed projects in the Nonrecurring Maintenance (NRM), Minor Misc., and Minor programs. The prioritization methodology sheets may be printed.

> The Construction Project Progress Report (Form 10-0051) has been redesigned to meet the needs of the regions.

> Equipment Management

> The LOCATION field is now a pointer to the Space file rather than free text.

> Information can be posted to the Equipment Repair Histories without going through the Work Order module. VA FileMan sort templates may be used for this purpose.

> nSpace/Facility Managemen

> DUsers may now distinguish between leased buildings and other types of space

> DProvisions have been made for entering data on planned space as well as actual space. Planne buildings may be associated with projects.

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Implementation and Maintenance

> Engineering Initialization Parameters

> The Engineering Initialization Parameters of interest are: PM Hourly Labor Cost

> Delete PM Work Orders? Temporary Work Order Section Region

> Equipment Category on Bar code label? Equipment Label Print Field Companion List Print Field

> Space Function on Location Label? Multi-division (Y/N)

> Each is described below.

> PM HOURLY LABOR COST

> Default value. If a device has an entry for estimated PM hours AND an entry for responsible tech, the labor cost will be taken from the Engineering Employee file (No. 6929). If there is an entry for estimated hours but NO entry for responsible tech, then this hourly figure will be used to compute total labor cost.

> DELETE PM WORK ORDERS?

> Setting this field to "YES" will cause PM work orders to be deleted from the system at close out time. Deletion of PM work orders is strongly recommended for sites that are short on disk space. The PMI will be posted to the equipment history (File 6914) before the actual work order is deleted.

> TEMPORARY WORK ORDER SECTION

> Intended for use at sites that allow direct entry of Engineering work orders by end-users. Since assignment of work requests to specific shops is an Engineering responsibility, "electronic work orders" are initially directed to a "fictitious shop" (or receiving area).

> Engineering should clean out a receiving area at least once a day. Electronic work orders may be transferred to working shops or disapproved. The system will keep a permanent record of the number originally assigned to each work order. This number may always be used to look up the request, no matter how many times it's transferred. Initial requesters may edit their requests; but not after Engineering has transferred them. "Fictitious" shops should have numbers in the range of 90 to 99, inclusive. Multi-division sites may have more than one receiving area. If there is more than one receiving area AND if this field (TEMPORARY WORK ORDER SECTION) is left blank, end-users will be asked to specify the appropriate receiving area when they enter a work order.

> REGION

> The VA Region (1 through 4) in which facility is located. Used in electronic transmission of Construction Project Progress reports, since exact routing may differ from region to region.

> EQPT CAT ON BAR CODE LABEL?

> Should be set to "YES" if you want to print the EQUIPMENT CATEGORY at the top of your bar coded equipment labels (instead of the words "EQUIPMENT LABEL"). Due to space limitations on label stock, only the first 20 characters of the EQUIPMENT CATEGORY will be printable.

> EQUIPMENT LABEL PRINT FIELD

> Implementation and Maintenance

> Enter the FIELD NUMBER (from the Equipment file) of a field that you want to have printed in human readable format on your bar coded equipment labels. Please do not enter more than two (2) such fields. If more than two fields are specified, the system will accept the first two and ignore all others. Multiple fields, word processing fields, and computed fields should not be selected for inclusion on bar coded equipment labels.

> COMPANION LIST PRINT FIELD

> Enter the FIELD NUMBER (from the Equipment file) of a field that you want to have printed on the "Companion Listings" that are produced along with bar coded equipment labels. Please do not enter more than two such fields. Fields selected for inclusion (in human readable format) on bar code labels are NOT automatically printed on Companion Listings. multiple fields, word processing fields, and computed fields cannot be printed on Companion Lists.

> SPACE FUNCTION ON LOCATION LABEL?

> If set to "YES" and if a SPACE FUNCTION exists for the subject location, then the first 20 characters of the SPACE FUNCTION will be printed in human readable format at the top of the location label.

> MULTI-DIVISION (Y/N)

> An indicator of whether a site is single or multi-divisional. Used primarily to determine whether or not users should be prompted for DIVISION when sorting selected reports.

> <span id="_bookmark13" class="anchor"></span>Implementation and Maintenance

## Engineering Software Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following Engineering Software Options are of interest: Auto Print New Work Orders

> Equipment Replacement Template

> Expanded PM Work Orders Inventory Template

> PM Device Type Identification PM Sort

> Print Bar Code on W. O.

> Safety Printout

> Space Survey Printout Warranty Expiration Template

> Each is described below. AUTO PRINT NEW W.O.

> Choices for this feature are:

> \<S\> will print a short summary work order each time a new one is entered

> \<L\> will print a long W.O. each time one is entered

> \<N\> will suspend the printing of newly entered work orders

> EQUIPMENT REPLACEMENT TEMPLATE

> One standard output of the DHCP Equipment Management module is a listing of all non- expendable equipment due for replacement within a user specified date range. The fields to be printed on this listing are defined by output template ENEQ REPLACEMENT.

> You can specify that a different set of fields be printed at your facility. To do this, simply set this software option to "L" and create an output template named ENZEQ REPLACEMENT.

> Choices are \<L\> for local, or \<S\> for standard (default). EXPANDED PM WORK ORDERS

> \<Y\> will cause all the equipment related fields in PM work orders to be filled in using data from the Equipment file.

> If this option is not set to \<Y\>, the system will produce skeleton PM work orders to conserve disk space. Note that information from the Equipment file is always

> printed on the PM worklists.

> Implementation and Maintenance

> INVENTORY TEMPLATE

> One standard output of the DHCP Equipment Management module is a listing of all non- expendable equipment sorted by CMR, EQUIPMENT CATEGORY, LOCATION, OWNING SERVICE, RESPONSIBLE SHOP (Engineering Section), or USE STATUS. The standard output for these reports is defined by output template ENEQ EQUIP. LIST.

> If you so desire, you can use a different output template at your facility. To do this, just enter an

> \<L\> for this software option and be sure to call your local template ENZEQ EQUIP. LIST. Choices are \<L\> for local, or \<S\> for standard (default).

> PM DEVICE TYPE IDENTIFIER

> Choices for this feature are as follows:

> \<E\> will stand for EQUIPMENT CATEGORY

> \<M\> will stand for MFG. EQUIPMENT NAME

> This option determines what is printed on PMI worklists under the heading of "Equip Category". EQUIPMENT CATEGORY will be printed unless \< M\> is explicitly entered as the option of choice.

> PM SORT

> PM lists are automatically sorted by responsible shop, and by responsible technician within shop. Within tech, a site may choose to have the PM list sorted by PM \#, Local Identifier, Location, Device Type, or Owning Service. Choices are, therefore:

> \<P\> for PM \#

> \<I\> for Local Identifier

> \<L\> for Location

> \<C\> for Equipment Category

> \<S\> for Owning Service

> If no choice is made via this file, the user will be asked for a Sort By parameter each time a PM list is requested. Note that all data for the PM lists comes from the Equipment Inventory (File 6914).

> PRINT BAR CODES ON W.O.

> \<Y\> will cause bar code to be printed at the bottom of hard-copy work orders, provided the printer is capable of printing bar code

> \<N\> will cause work orders to be printed without bar code

> SAFETY PRINTOUT

> Choices for this feature are as follows:

> \<L\> for local template (template name must be ENZFSA1)

> \<S\> for standard template

> Implementation and Maintenance

> SPACE SURVEY PRINTOUT

> Choices for this feature are as follows:

> \<L\> for local template (template name must be ENZSPRM)

> \<S\> for standard template (ENSPRM)

> WARRANTY EXPIRATION TEMPLATE

> One standard output of the DHCP Equipment Management module is a list of equipment whose warranty expires within a user specified date range. The standard output for this report is defined by output template ENEQ WARRANTY.

> You may create a different template for use at your facility. To make this work, you should enter an

> \<L\> for this software option and be sure to call your template ENZEQ WARRANTY. Choices are as follows:

> \<L\> for local template

> \<S\> for standard template (default)

# Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Wherever possible, Engineering V. 7.0 references ^TMP instead of the ^UTILITY global. However, since the Archiving module includes routines that were generated via VA FileMan, the ^UTILITY global is still used in this module.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EN</p>
</blockquote></th>
<th><blockquote>
<p>Initializes Engineering System variables.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENAR</p>
</blockquote></td>
<td><blockquote>
<p>Driver (and Kernel entry point) for Engineering Archive module. This module</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>allows old Engineering Work Orders and old Accident Reports to be stored on</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>tape and then purged from disk.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENAR1</p>
</blockquote></td>
<td><blockquote>
<p>Checks appearance of Engineering archive global and sets up a few local</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>variables for use in the following archival operations:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>1. Find and assemble records</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2. Archive and verify records</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3. Delete archive global</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4. Recall archived records</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENAR2</p>
</blockquote></td>
<td><blockquote>
<p>Displays the identifier of the current "archive data set".</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENARG</p>
</blockquote></td>
<td><blockquote>
<p>Queries the user as to the criteria for archiving (e.g., All Electric Shop work</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>orders completed in FY 90).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENARG1</p>
</blockquote></td>
<td><blockquote>
<p>Invokes routine ENARG2 to search for records subject to archiving and</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>reports the count to the user for confirmation. If confirmation is given, an</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>archival data set identifier is placed in permanent storage and the user is</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>invited to add a local description. This routine also controls the incorporation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>of current data dictionaries onto the archive tape.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENARG2</p>
</blockquote></td>
<td><blockquote>
<p>Builds skeleton archive global (internal entry numbers of records to be</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>archived) and keeps a count.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENARG21</p>
</blockquote></td>
<td><blockquote>
<p>Extracts data from Work Order file and stores them in the archive global. All</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>pointers are resolved. Work Orders being archived are deleted from the Work</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Order file at this point in order to reclaim disk space.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENARG22</p>
</blockquote></td>
<td><blockquote>
<p>Extracts data from the Accident Report file and stores them in the archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>global. Pointers are resolved. Accident Reports being archived are deleted from</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the Accident Report file (#6924) at this point in order to reclaim disk space.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Descriptions

> ENARGO

> ENARGR

> ENARL

> ENARY101

> ENARY102 ENARY11

> ENARY12 ENARY13 ENARY14 ENARY201

> ENARY202 ENARY203 ENARY21

> ENARY22 ENARY23 ENARY24 ENBCPM

> Moves the archive global onto tape. A tape verification process (just a check to be sure that what was written can actually be read) is performed in program segment V (at the end of disk-to-tape data transfer).

> Recalls data from an archive tape. Loads and i nitializes data dictionaries and loads data elements. Will either load all archived records or search for one particular record (as specified by the user).

> Maintains a permanent record of all archival transactions by archive data set. Records the date(s) on which an archive data set was assembled, purged from disk, recalled from tape, etc.

> Data dictionary for use in archiving Engineering work orders. This routine is saved to archive tape as ENARX101.

> Continuation of ENARY101. Saved to archive tape as ENARX101.

> Initialization routine for a set of archived Engineering work orders. This routine is saved to archive tape as ENARX11.

> Continuation of ENARY11. Saved to archive tape as ENARX11. Continuation of ENARY11. Saved to archive tape as ENARX13. Continuation of ENARY11. Saved to archive tape as ENARX14.

> Data dictionary used in archiving Accident Reports (Form 2162). This routine is saved to archive tape as ENARX201.

> Continuation of ENARY201. Saved to archive tape as ENARX201.

> Continuation of ENARY201. Saved to archive tape as ENARX203.

> Initialization routine for a set of archived Accident Reports (Form 2162). This routine is saved to archive tape as ENARX21.

> Continuation of ENARY21. Saved to archive tape as ENARX22. Continuation of ENARY21. Saved to archive tape as ENARX23. Continuation of ENARY21. Saved to archive tape as ENARX24.

> Hard-coded driver for bar code based preventive maintenance inspection module.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Routine Descriptions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENBCPM1</p>
</blockquote></td>
<td><blockquote>
<p>Controls the download of data acquisition software from DHCP to portable bar code readers. Also initiates the processing of uploaded data by establishing the specific PMI worklist and then looping through the uploaded data to parse out each equipment identifier.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENBCPM2</p>
</blockquote></td>
<td><blockquote>
<p>Updates basic inventory information for each equipment record in the uploaded data set and handles Exception Messages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENBCPM3</p>
</blockquote></td>
<td><blockquote>
<p>Attempts to identify equipment records on the basis of MODEL and SERIAL NUMBER, or VA PM NUMBER.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENBCPM4</p>
</blockquote></td>
<td><blockquote>
<p>Attempts to post completed Preventive Maintenance Inspections to the Equipment History sub-file by closing out PM work orders.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENBCPM5</p>
</blockquote></td>
<td><blockquote>
<p>Attempts to post completed Preventive Maintenance Inspections directly to the Equipment History sub-file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENBCPM6</p>
</blockquote></td>
<td><blockquote>
<p>Invoked (by routine ENBCPM1) to explain the significance of PMI Exception Messages. Program segment WOCHK checks the Equipment History sub-file to see if PM work order has already been closed out and returns ENWOX=1 if it has.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENBCPM7</p>
</blockquote></td>
<td><blockquote>
<p>Invoked when a piece of equipment has failed a preventive maintenance inspection. Annotates an existing work order or creates a new one, whichever is most appropriate. User intervention is not expected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENBCPM8</p>
</blockquote></td>
<td><blockquote>
<p>Updates the running totals of PM man-hours that are maintained in the Engineering Section file. Invoked by the bar coded preventive maintenance module and by the manual PM work order close-out routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENBCPM9</p>
</blockquote></td>
<td><blockquote>
<p>Physically gener ates an unscheduled work order. Invoked by routine ENBCPM7.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENCTBAR</p>
</blockquote></td>
<td><blockquote>
<p>Downloads a data acquisition program from DHCP to a portable bar code reader. References the Barcode Program file (#446.4).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENCTFLD</p>
</blockquote></td>
<td><blockquote>
<p>Enter/edit entries in a user-created file (#446.5) of bar code label specifications. This file is not needed for bar code based Equipment Management, since hard</p>
<p>coded options exist for both equipment labels and location labels.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Descriptions

> ENCTLAB

> ENCTMAN

> ENCTMES1 ENCTMES2

> ENCTPRG ENCTQUES ENCTRCH ENCTREAD

> ENCTRED ENCTTI ENCTUTL ENEQ ENEQ1

> Uses FileMan to print bar code labels in accordance with specifica tions contained in the Custom Report file (#446.5). Contains a program segment (SPC) for issuing special instructions to bar code devices. The main portion of this routine (program segment EN) is not explicitly referenced by the Engineering package, since hard coded options exist to print location labels and equipment labels.

> Schedules processing of data uploaded to DHCP from a portable bar code reader. Not used if the Barcode Program entry (File 446.4) includes a POST UPLOAD ROUTINE (Field \#.03). Both of the bar code programs distributed with Engineering 7.0 contain POST UPLOAD ROUTINES.

> Contains error messages and help text intended to support the use of portable bar code readers in conjunction with DHCP.

> Help text intended to support the printing of bar code labels in accordance with a user-specified label format. Not explicitly referenced in Engineering 7.0, since hard coded options exist for printing location labels and equipment labels.

> Uses FileMan (routine DIK) to purge data from the Barcode Program file (#446.4).

> Miscellaneous utility functions useful in interfacing portable bar code readers with DHCP.

> A routine for checking the integrity of user-specified bar code label formats. Not explicitly referenced by Engineering 7.0.

> Controls the upload of data from a portable bar code reader to DHCP. In Engineering 7.0, this routine transfers control to the designated POST UPLOAD ROUTINE upon completion of a successful data upload.

> Processes (compiles) a user-specified bar code label format. Not explicitly referenced by the Engineering package.

> Time handling utility. Used to obtain a unique entry in the Barcode Program file (#446.4) for each discrete data upload.

> Miscellaneous utility functions related to entries in the Barcode Program file (#446.4).

> Main driver for Engineering Equipment Management module. Directly callable. Calls ENEQ1, ENEQRP, ENEQPMP, ENEQPMS and ENEQPMR.

> Processes entry of new record into Equipment Inv. file (single and multiple), as well as edits and displays of equipment records.

> Entry of single records may be done via Screen Handler (EN^ENJ) or conventional FileManager (^DIE). The selection of internal entry numbers is made in this routine, but the actual addition of records is made via a call to

> ^DIC so that bulletins may be triggered. As a safeguard against duplicate entries, users are asked for a PM number (if available) before a new record is created.

Routine Descriptions

> There are three entry points for editing equipment records. EDA^ENEQ1 gives write access to all fields; whereas EDE^ENEQ1 and EDS^ENEQ1 give write access to Engineering and Supply data elements, respectively. Editing is performed via the Engineering Screen Handler. ENEQ1 calls ENEQ2 for a portion of multiple record entry and the PM sub-module (routines ENEQPMP and ENEQPMP3) for entry/edit of preventive maintenance parameters.

> ENEQ2 Called by ENEQ1 when multiple record entry is desired. Once user has input the first record in its entirety, ENEQ1 calls ENEQ2 for processing of second and subsequent records. ENEQ2 copies all fields from the first entry except for SERIAL NUMBER, LOCATION, NXRN, PM NUMBER, and LOCAL

> IDENTIFIER. User is prompted for these five fields via a call to ^DIE. ENEQ2 calls ENR^ENEQ1 for the purpose of creating new records.

> ENEQCMR Prints the actual signature page at the end of each CMR (Consolidated Memorandum of Receipt).

> ENEQHS Posts closed out Work Order info rmation to the Equipment Inv. file (Equipment History sub-file).

> ENEQNX Main driver for non-expendable (NX) inventory module. Driver functionality is used primarily in software development and testing. Calls routines ENEQNX1, ENEQNX3, and ENEQNX4.

> ENEQNX1 The first step in processing a non-expendable inventory reconciliation.

> Intended to be invoked immediately after data is uploaded to DHCP from a portable bar code reader. The routine essentially steps through the bar code data list identified by ENNXTI (date/time, including seconds). Data elements from this list will belong to one of three possible categories; location labels, equipment labels, or equipment descriptions. Location labels and equipment labels consist of a single record and are normally the result of a successful bar code read (although bar coded information may be entered manually if a bar code label itself is unreadable). Equipment descriptions consist of three records (some of which may be null). These records are (in order of occurrence) Model Number, Serial Number, and Description (free text). IT IS THE RESPONSIBILITY OF SOFTWARE RESIDENT ON THE PORTABLE BAR CODE READER TO INSURE THE EXISTENCE OF THESE THREE RECORDS.

> Each time a location label is found, the location itself is stored in local variable ENLOC. Each location label is assumed to be followed by information on all non-expendable equipment found in that location. The usual entry point is at line EN. Routine will be entered at line RES if and only if a particular session is being restarted. "Session" should be taken to mean processing of data uploaded from a portable bar code reader at a specific date and time.

> Individual sessions are uniquely associated with entries in the DATE/TIME OF DATA UPLOAD field of the Barcode Program file (#446.4).

> The station number (ENSTA) is extracted from the Engineering Init Parameters file (#6910) and subsequently used to check equipment labels. Labels from other VAMCs (if any) will be reported in Exception Messages and will not be otherwise processed. The check for station number is followed by a prompt for a device on which to print Exception Messages. Possible Exception Messages include LOCATION EXPECTED (if a session fails to begin with a location label); FOREIGN EQUIPMENT (if an equipment label identifies another VAMC); ITEM NOT IN DATABASE; RECORD LOCKED (if another

> Routine Descriptions

> user is updating an equipment record); and BAR CODE LABEL MISSING (if a piece of equipment is in the database but does not have a bar code label). The text of Exception Messages is stored in local variable ENMSG. Additional descriptive information may be found in a local array whose root is "ENMSG(0,". Printing of Exception Messages begins at line XCPTN.

> The task of processing data uploaded from a portable bar code reader will be queued if queuing is requested by the user in response to the "Select Device for Exception Messages" prompt OR if the TIME TO QUEUE ROUTINE field of the Barcode Program file contains data. Physical data processing begins at line CONT. This label is used as an entry point for tasks queued through

> %ZTLOAD.

> A location label (in the form "SP"\_Room\_"-"\_Building) is expected at line NEWLOC. When a location label is encountered in the course of processing a list of equipment, control is transferred back to NEWLOC (c.f., line NEWNX+2). THE PROGRAM RESIDENT IN THE PORTABLE READER MAY REQUIRE THE USER TO SCAN LOCATION LABELS TWICE (ONCE ON ENTERING A ROOM, AND AGAIN ON LEAVING) BUT IT IS ASSUMED THAT LOCATION LABELS WILL APPEAR ONLY ONCE IN

> THE RESULTANT "^PRCT(446.4," GLOBAL, AND THAT THEY WILL IMMEDIATELY PRECEDE A LIST OF EQUIPMENT (IF ANY) FOUND IN THAT LOCATION. IN OTHER WORDS, BAR CODE READERS ARE FREE TO REQUIRE A SECOND SCAN BUT THEY MUST NOT ACTUALLY RECORD IT.

> Program segment NEWNX steps through the list of equipment and calls the appropriate subroutine (if necessary) to process each item. Control is transferred to line DONE at the end of the list.

> Program segment UPDATE is called by program segment NEWNX and operates on the Equipment Inv. file (#6914). It moves the present value of LOCATION into PREVIOUS LOCATION; stores the content of ENLOC in LOCATION; and inserts the current date (DT) in PHYSICAL INVENTORY DATE. If an update has already occurred on the current date, no action is taken. The assumption in this case is that the transaction in question has already been recorded (perhaps a bar code reader was uploaded twice). In any event, we don't want to reprocess the update because doing so would effectively remove the true PREVIOUS LOCATION.

> Program segment DONE deletes the processed portion of the "^PRCT(446.4," global by deleting the subject entry (DATE/TIME OF DATA UPLOAD) from the Barcode Program file.

> Program segment ZTSK controls queuing.

> ENEQNX2 Invoked by ENEQNX1.

> Program segment NOLBL processes pieces of equipment that do not have bar code labels. In such cases, it is assumed that the portable bar code reader has prompted the user for Model Number, Serial Number, and a brief Description. These three pieces of information must reside in three separate nodes of the "^PRCT(446.4," global. THESE NODES MAY BE NULL (OR EQUAL TO A SINGLE SPACE CHARACTER) BUT THEY MUST EXIST. Local array

> EN(0..2) is loaded with the content of these three nodes.

Routine Descriptions

> Program segment MATCH is executed only if the model and serial numbers match those of an entry in the Equipment Inv. file. Otherwise the piece of equipment is reported in the Exception Messages.

> Program segment MATCH also contains code analogous to that found in program segment UPDATE of routine ENEQNX1.

> Program segment MSG is invoked early in the execution of routine ENEQNX1 and simply displays explanatory text regarding Exception Messages to the user.

> Program segment ERR is invoked whenever abnormal termination of an update process seems to be in order. The user is presented with the information needed to restart processing of the session at some later time.

> ENEQNX3 This routine examines the Equipment Inv. file (#6914) and lists items NOT found in the course of a physical inventory. The listing itself is called an Exception List. The user must specify a start date (ENFR) for the inventory process. Default value will be the first day of the current month. User will then be asked to select a CMR, unless reconciliation of all CMRs is desired (ENCMR(0)="ALL"). CMR selection is handled in program segment ASK. Note that CMR should be taken to mean an entry in the CMR file (#6914.1) and NOT a list of equipment (which is the general LOG 1 usage of the term).

> Program segment DEV prompts the user for a printer on which to produce an Exception List. The actual data processing task will be queued if the user enters a "Q" at this point.

> Actual examination of the database begins at line CONT. The first step is to acquire (or confirm) the current date (DT). If reconciliation of ALL CMRs has been requested, this is done in program segments ALL and CMRA. Reconciliation of a single CMR is done within program segment CMR. In either case, the code uses the "AD" cross-reference to step through the Equipment Inv. file and look at each piece of equipment on the subject CMR(s). If PHYSICAL INVENTORY DATE predates ENFR (user specified starting date) or is non-existent, program segment PRNT is invoked. The item in question will now appear on the Exception List unless its USE STATUS (ENSTAT) is LOANED OUT, TURNED IN, or LOST OR STOLEN.

> Routine Descriptions

> The following fields are printed on the Exception List: Control Number (.01 field)

> VA PM Number Location Previous Location

> Date Last Inventoried

> Manufacturer Equipment Name (Description) Use Status

> If the Exception List is produced on a 132 column printer (IOM\>100), Equipment Category will also be printed.

> Queuing logic is contained in program segment ZTSK.

> ENEQNX4 This routine is used to manually update the inventory fields of an individual equipment record. Lookup is performed in line DIC, after which data on file is displayed.

> Line CNFRM asks user to verify that he does indeed wish to update the selected record. If so, routine DIE will be called twice. The first call is transparent to the user and stuffs LOCATION (if it exists) into PREVIOUS LOCATION and stuffs the current date into PHYSICAL INVENTORY DATE. The second call to DIE allows the user to update the LOCATION field and modify PREVIOUS LOCATION and PHYSICAL INVENTORY DATE if

> necessary.

> ENEQNX5 Manual update of basic inventory information (Equipment LOCATION and last PHYSICAL INVENTORY DATE). The intent is to give a limited number of users a means of entering these data elements via CRT. Under normal circumstances, these fields are automatically updated on the basis of data that's uploaded from portable bar code readers.

> ENEQPMP Main driver for PM Parameters sub-module. Calls ENEQPMP1 and ENEQPMP2. Also contains code to edit PM schedule of a specific device.

> If there is no PM schedule on file, this routine attempts to copy one from the Equipment Category file (using ^%RCR) unless the user indicates a desire to do otherwise. If a schedule copied from the Equipment Category file does not contain a STARTING MONTH, the routine will prompt for one (PMSESM^ENEQPMP). Routine is called at line XNPMSE by Equipment Inv. entry/edit routine (ENEQ1). This feature gives users who hold the appropriate security key (ENEDPM) the opportunity to edit PM data along with other components of the equipment record.

> Finally, routine ENEQPMP is callable at line PMSE3 in the event that a user changes the PM schedule for an EQUIPMENT CATEGORY and wishes to apply the changes to existing entries in the Equipment Inv. file. In this case, existing STARTING MONTHs in the Equipment Inv. file will be stored in variable ENB while the PM schedule is being updated. If the new schedule from the Equipment Category file does not contain a STARTING MONTH, then the old STARTING MONTH (if any) is re-entered into the Equipment Record. This feature enables sites to easily change PM FREQUENCIES, CRITICALITY, RESPONSIBLE TECH, and other PM parameters for existing devices without altering an established PM workload balance. The exception flag (ENXP) is defined (set to 1) whenever this routine is called at line XNPMSE. This causes control to be returned to the calling program once the requested edit is complete.

Routine Descriptions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ENEQPMP1</p>
</blockquote></th>
<th><blockquote>
<p>Controls display of PM schedules from both the Equipment Inv. and</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Equipment Category files. Calls ENEQPMP3 for actual display generation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Processes edits of Equipment Category file (line DTE). Allows user to assign a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>new PM schedule to all existing equipment records in the subject Equipment</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Category via a call to PMSE3^ENEQPMP in line DTE5 (c.f., description of</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>routine ENEQPMP). Line SKPCK is called by input transform of SKIP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MONTHS subfield of RESPONSIBLE SHOP field of both the Equipment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Category and the Equipment Inv. files.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENEQPMP2</p>
</blockquote></td>
<td><blockquote>
<p>Controls entry, edit and printing of PM Procedures (File 6914.2).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENEQPMP3</p>
</blockquote></td>
<td><blockquote>
<p>Displays PM schedule in screen-like format. Calls ENLIB1 for date</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>conversion. Expects values (escape sequences) for high and low intensity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>display (ENHI and ENLO, respectively).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENEQPMR</p>
</blockquote></td>
<td><blockquote>
<p>Main driver for reporting (posting) completed PM inspections. Calls</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ENEQPMR1, ENEQPMR2 and ENEQPMR4.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENEQPMR1</p>
</blockquote></td>
<td><blockquote>
<p>Processes manual close-out of PM worklists. Asks user about automatic</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>deletion of PM work orders after posting, unless the appropriate ENG INIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PARAMETER has been set (c.f., Site Configurable Files and Fields). The</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>initial work order is selected via a call to routine DIC with variable DIC("S")</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>set to screen out all but PM work orders. Subsequently, work orders may be</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>selected by entering the sequential portion only (for ease of use). Close out is</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>performed using template ENPMCLOSE.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Descriptions

> ENEQPMR2 Entry point for rapid close-out of PM work orders. Rapid close-out essentially assigns a status of PASSED and standard values (if any) for time and materials to each "work order" on the specified PM worklist, except for those "work orders" identified by the user as exceptions. The first program segment (line RCO to RCO2) establishes which worklist is to be closed out. Segment RCO2T explains to the user what is about to happen. Segments RCO21 and RCO3 allow the user to close out work orders individually as necessary. When there are no more work orders to be individually closed out, control is transferred to ENEQPMR3 (G RCO4^ENEQPMR3).

> ENEQPMR3 Completes the rapid close out process. Begins by displaying those PM work orders that were closed out individually under control of ENEQPMR2 and giving the user one last chance to back out.

> Actual closeout is performed by stepping through the "B" cross- reference on the Work Order \# file beginning with the first work order on the chosen worklist and ending when the next available work order does not belong to said worklist. Worklist specification is contained in variable ENPMWO("P"). The user may elect to have the actual closeout processed as a background job (thereby freeing up his/her terminal), but the process may not be queued for some later time. The advantages of having these important tasks performed on an attended system are thought to outweigh any degradation in response time that may ensue.

> ENEQPMR4 Processes the posting of individual unscheduled PM inspections to the Equipment History. Performance of PM inspections off-schedule generally occur as a result of other maintenance activity. Calls outine ENEQPMR5.

> Routine first queries user for shop, date, and type (MONTHLY or WEEKLY) of PM inspection. Responses are used to construct non-sequential portion of PM work order. User is then asked to identify the piece of equipment to be inspected. If a work order for the specified PM already exists, the user is asked to close it out (program segment SDPM3). If such a work order does not exist, control is transferred to routine ENEQPMR5. ENEQPMR4 also contains help text for questions dealing with PM worklists (segment COH and COBH).

Routine Descriptions

> ENEQPMR5 Completes posting of individual PM inspections. Work order is created in lines SDPM4 to SDPM42. Sequential portion is generated only if the user wishes

> to retain the work order after posting. Once work order is created, it is immediately closed out. If COMPLETION DATE is not entered, work order is retained (sequential portion is added if necessary) and control is returned to the calling program (G SDPM2^ENEQPMR4). If COMPLETION DATE does exist (as is normally the case) routine displays the next scheduled PMI (program segment SDPM5) if appropriate and gives the user an opportunity to adjust the PMI schedule (line SDPM71). Control is then returned to the calling program.

> ENEQPMR6 Automatically assigns a PM STATUS of DEFERRED to all work orders on a user-specified PM worklist. The current date is used as the work order close• out date. PM work orders are deleted after the deferral has been posted to the Equipment History unless the user specifies otherwise.

> Program segments RD and RD1 establish the identity of the PM worklist.

> Program segment RD2 explains the action that is a bout to take place and solicits confirmation from the user.

> Rapid deferral works by stepping through the "B" cross-reference of the Work Order file.

> ENEQPMS Main driver for generation of preventive maintenance (PM) worklists and systematic deletion of PM work orders. Calls ENEQPMS1 for PM worklist generation and ENEQPMS4 for PM work order deletion.

> Generation of PM worklists may be thought of as a four step process.

1.  Establish the type of worklist desired and how it is to be sorted.
2.  Identify the specific devices that should be included on said worklist.
3.  Create a PM work order (unless one already exists or has been closed out and deleted) for each device identified in Step 2.
4.  Print the worklist. The inter-relationship of Steps 1 through 3 is sequential, whereas Steps 3 and 4 are performed in parallel.

> Routine Descriptions

> ENEQPMS1 Collects parameters needed for generation of PM worklist; including month, week number (weekly worklists only), sort parameter, responsible technician, responsible shop(s) and levels of CRITICALITY. If a PM SORT parameter has been entered in the Eng Software Options file (c.f., Site Configurable Files and Fields) the user will not be prompted for sort parameter. Calls ENEQPMS3 for processing sort parameters other than VA PM NUMBER and ENEQPMS2 for selection of devices to be included on subject worklist.

> ENEQPMS2 Creates sorted list in the ^TMP global of internal entry number of all devices meeting the criteria for inclusion in subject worklist.

> The "AB" cross-reference on File 6914 is used to examine each device for which the Engineering Shop in question has PM responsibility. If a device qualifies for inclusion on the basis of parameters specified by the user in requesting the worklist (line LSTC to LSTC1), the routine then examines the stored PM schedule to see if it is due for inclusion on that basis as well. Monthly worklists encompass the following frequencies: ANNUAL, SEMI-ANNUAL, QUARTERLY, BI-MONTHLY and MONTHLY. Weekly worklists are composed solely of the frequencies BI-WEEKLY and WEEKLY. In preparing a

> monthly worklist, the STARTING MONTH (variable ENSTMN) is taken into account for all frequencies except MONTHLY.

> ENEQPMS3 Establishes range for all sort parameters except VA PM NUMBER, for which the concept of range is unsupported. Called by ENEQPMS1. Establishment of a range at this point will generally result in a subset of what would have otherwise been the entire worklist. If the user indicates (line SPL0) that the entire worklist is desired, then ENSRT ("ALL") is set to 1 and control is returned to the calling program. Otherwise control is directed to the program segment (I, L, D, or S) that has been coded for the chosen sort parameter. If the sort parameter (ENSRT) is "L" for LOCATION, the routine will attempt to interpret LOCATION as the value of WING in the Eng Space file. For the purpose of producing a PM worklist, WING is a more meaningful sorting parameter than ROOM-BUILDING.

> ENEQPMS4 Contains help text for choosi ng the sort parameter and controls deletion of individual PM work orders and entire PM worklists. PM worklists are intended to be deleted immediately after being printed at sites that choose not to post them to the Equipment Histories. Program segment DEL1 processes deletion of individual PM work orders. The first selection must be entered in its entirety, whereas subsequent selections may be specified by entering only the sequential portion of the PM work order number. Calls to ^DIC are used to validate selections. Actual deletion is achieved by invoking ^DIK.

> Segment DEL2 handles worklist deletion. Once the user has specified the worklist itself (lines DEL2 to DEL22), the routine tallies the number of PM work orders on said list and presents the result to the user for confirmation. Actual deletion of entire worklists may be queued to run during non-peak hours and invokes ^DIK.

> ENEQPMS5 Reads the sorted list generated by ENEQPMS2 and creates PM work orders as needed. Called by ENEQPMS2. Calls ENEQPMS6 to print header and ENEQPMS7 to print worklist entries.

> The sorted list contained in the ^TMP global contains five subscripts in addition to \$J (four sort parameters and the equipment identifier). The first two sort parameters (ENSHKEY and ENTECH) are the shop and responsible

Routine Descriptions

> technician, respectively. If a device does not have a RESPONSIBLE TECHNICIAN assigned, ENTECH will be zero. If there were no RESPONSIBLE SHOP, the device would not be in the sorted list to begin with.

> The next two sort parameters are "read into" variables ENC and ENE. If the user chose VA PM NUMBER as the sort parameter (ENSRT="P") when building the list, then ENC will equal the PM NUMBER and ENE will be zero. Otherwise ENC will equal the value of the user specified sort parameter and ENE will equal the PM NUMBER.

> The "G" cross-reference on the Work Order \# file is used to determine if the necessary work order already exists and the Equipment History is searched to be sure that such a work order hasn't already been posted and deleted (lines PR2 and PR2+1).

> PM work orders are created via hard code and are designed to contain as little redundant information as possible. TEST^ENWOCOMP is called to add newly created PM work orders to the cross-reference of incomplete work orders.

> ENEQPMS6 Prints page header for PM work lists. Called by ENEQPMS5. Also contains code to print special messages on worklists for devices that may require extra attention. This program segment (line WARNG) is called by routine ENEQPMS7.

> Routine Descriptions

> ENEQPMS7 Prints entire PM worklists. Called by ENEQPMS5. Expects internal entry number of Equipment Inv. record in variable DA. Fields from the record pointed to by DA are stored in local variables until printed, primarily for clarity and ease of maintenance.

> ENEQPMS8 Sorts the PM Worklist by LOCATION. Expects LOCATION to be in the standard format (ROOM-BUILDING-DIVISION). Sorts first by DIVISION (if applicable), then by BUILDING, and finally by ROOM.

> ENEQRP Main driver for Equipment Reports. Calls ENEQRP1, ENEQRP2, ENEQRP3 and ENEQRP5.

> ENEQRP1 Produces FileManager printouts of entries in the Equipment Inv. file where warranty expires within a user specified date range.

> Produces a similar listing of non-expendable equipment scheduled for replacement within a user specified date range. Sites may elect to specify the output themselves by creating print templates ("ENZEQ WARRANTY" and/or "ENZEQ REPLACEMENT") and setting the appropriate ENG SOFTWARE OPTION(S). Please refer to the Site Configurable Files and Fields section for more information.

> ENEQRP1 also produces equipment maintenance histories in the segment from line HS to HSD1+2. These histories include acquisition data and all parts and labor costs (including vendor service and preventive maintenance) that are on file. If the device in question has been identified as a PARENT SYSTEM, then maintenance histories of each of its components will be generated as well (with page breaks between each). Totals and Grand Totals (in the case of PARENT SYSTEMs) are accumulated in variables ENT and ENGT, respectively.

> ENEQRP2 Produces an aggregated repair history for all devices belonging to a user specified Equipment Category (i.e., discrete entry in File 6911). Once Equipment Category has been specified, ENEQRP2 uses the "G" cross- reference to select appropriate records from the Equipment Inv. file (#6914). Data is collected from the EQUIPMENT HISTORY field (node 6 of File 6914) and held in subscripted scratch variables until print time.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Routine Descriptions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENEQRP3</p>
</blockquote></td>
<td><blockquote>
<p>Produces a listing of discrete devices which have experienced more than a</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>user specified number of repairs within a user specified time frame. User may</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>elect to examine all entries in the Equipment Inv. file, or only those belonging</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>to a specific Equipment Category. User specifies whether or not vendor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service is to be counted.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Routine examines EQUIPMENT HISTORY field (node 6 of File 6914) of each</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>candidate device (SEARCH^ENEQPR3). If the number of repairs is found to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>exceed the user specified minimum, the internal entry number of the device is</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>stored in the ^TMP global. When all candidates have been examined,</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ENEQRP3 transfers execution to FAP^ENEQRP4 for report generation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENEQRP4</p>
</blockquote></td>
<td><blockquote>
<p>Prints listing defined by routine ENEQRP3. Reads Equipment Inv. internal</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>entry from the ^TMP global. Root used is ^TMP($J,"ENEQFA".</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENEQRP5</p>
</blockquote></td>
<td><blockquote>
<p>Performs gross analysis of preventive maintenance (PM) workload. For a user</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>specified shop (ENGINEERING SECTION), the output of this routine will</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>indicate how many devices are scheduled for PM inspections each month and</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>the approximate amount of time required (assuming standard hours have been</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>entered for each scheduled PM).</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Variable ENA has 12 pieces (one for each month). It contains the scheduled</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PM workload distribution for each subject device, exclusive of WEEKLY and</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BI-WEEKLY PMs which are reflected in variable ENA("W"). ENA and</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ENA("WT") are re-initialized with the selection of each new device.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Subscripted variables ENC and ENT (subscripts are integers from 1 to 12)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>contain running totals of device counts and scheduled hours, respectively, for</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>each month.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENEQRPI</p>
</blockquote></td>
<td><blockquote>
<p>Uses FileManager (D EN1^DIP) to generate a listing of non-expendable</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>equipment by CMR, EQUIPMENT CATEGORY, LOCATION, OWNING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SERVICE, RESPONSIBLE SHOP, or USE STATUS. Sites may elect to specify</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>their own output by creating a print template called ENZEQ EQUIP. LIST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>and setting the ENG SOFTWARE OPTION called INVENTORY TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>to "L".</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENETRAN</p>
</blockquote></td>
<td><blockquote>
<p>Gathers internal entry numbers of pending Electronic Work Orders into the</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>^TMP global in preparation for screen display. If the site has defined an</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>explicit TEMPORARY WORK ORDER SECTION, this is the "shop" that will</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>be processed. If not, all shops with SECTION NUMBERs between 90 and 99</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>(inclusive) will be processed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENETRAN1</p>
</blockquote></td>
<td><blockquote>
<p>Collects data elements from the work orders gathered by routine ENETRAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>and presents them to the user in the form of a screen. User is asked which (if</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>any) of these work orders should be transferred (assigned) to a working shop.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Users may pick individual work orders from the list; select a range of work</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>orders; or elect to process ALL candidate work orders.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENETRAN2</p>
</blockquote></td>
<td><blockquote>
<p>Actually transfers the work orders selected in routine ENETRAN1 from their</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>temporary receiving area to a working shop. User has the ability to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>DISAPPROVE Electronic Work Orders as well as to transfer them. Uses input</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>template ENWOWARDXFER in transferring (unless ENZWOWARDXFER is</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>on file) and input template ENWODISAP in disapproving (unless</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ENZWODISAP is on file).</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Descriptions

> ENEWOD

> ENEWOD1

> ENFSA ENFSA1 ENFSA2 ENJ

> ENJC2 ENJDPL ENJINJ ENJINJ1 ENJINJ2 ENJINJ3 ENJINK ENJINQ ENJMUL ENJPARAM ENLBL ENLBL1 ENLBL10

> ENLBL11

> Collects data elements from an Engineering Work Order in preparation for screen display. The actual screen format is a modified version of a display screen commonly used by Engineering personnel. The goal was a display format that does not include unnecessary or sensitive information. This routine is intended for use by end-users of the Electronic Work Order module.

> Physically displays (or prints) the data elements gathered by routine ENEWOD. Unlike its more conventional analog in the Engineering package (routine ENWOD1) this routine does not allow users to screen-edit Engineering work orders. Developed in support of the Electronic Work Order module.

> 2162 Accident Form entry point; contains hardcoded menu driver for module. 2162 Summary Report parameters are specified and set up for FileManager. 2162 Summary report time intervals are selected and set up.

> The ENJ\* routines constitute the screen handler current ly used by the Engineering package. This screen handler is serviceable; but is not considered optimal and will be abandoned in favor of the screen handler included with the VA Kernel as soon as that software becomes available.

> Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ. Continuation of routine ENJ.

> Hard-coded driver for printing bar coded equipment and location labels. Hard-coded driver for printing bar coded Location labels.

> Prints bar coded equipment labels for a user specified range of VA PM Numbers (program segment PM) or in concert with an existing PM Worklist (program segment WRKLST). Although equipment is selected on the basis of PM Number (in program segment PM), the final printout is sorted by LOCATION.

> Prints bar coded equipment labels for all items on a user-specified PM worklist. Labels are produced in the same order as items on the worklist.

Routine Descriptions

> ENLBL12 Prints bar coded equipment labels for all items on a user-specified purchase order.

> ENLBL15 Prints bar coded equipment labels by the LOCAL IDENTIFIER field. Labels may be sorted either by LOCATION or by LOCAL IDENTIFIER (user is asked).

> ENLBL16 Handles the printing of data elements on bar coded equipment labels in human readable format. Each site is allowed to choose which (if any) fields are

> to be included on bar code labels.

> ENLBL2 Hard-coded driver for printing bar coded equipment labels.

> Routine Descriptions

> ENLBL3

> ENLBL4

> ENLBL5

> ENLBL6 ENLBL7

> ENLBL8 ENLBL9

> ENLIB ENLIB1 ENLIB2 ENMAN

> Program segment SD prints a bar coded equipment label for a particular device.

> Program segment CAT prints bar coded equipment labels for all devices belonging to a user specified Equipment Category. Within the Equipment Category; labels are sorted first by LOCATION and then by EQUIPMENT ID# within LOCATION.

> Physical print of bar coded location labels (program segment LOCPRT). Calls routine ENLBL7 to format the bar code printer (assumed to be an Intermec 8646 or equivalent). Prints an individual room (program segment RM); an entire wing (program segment WING); an entire building (program segment BLDG); or the entire Space file (program segment ALL). All printing is done on the basis of entries in the Space file (File Number 6928). If this routine is being run on an Engineering 6.4 system {as determined by inspection of the

> ^ENG("VERSION") global}, program segment BLDG will transfer control to routine ENLBL14. This is necessary because the Building file (#6928.3) does not exist on Engineering 6.4 systems.

> Prints bar coded equipment labels for an entire CMR (program segment CMR) or by EQUIPMENT ID (program segment ALL). Note that program segment ALL can easily print labels for the entire Equipment file; if that's what's desired. Labels are first sorted by LOCATION, and then by EQUIPMENT ID# within LOCATION.

> Prints bar coded equipment labels for devices within a general (program segment WING) or specific (program segment RM) location.

> Physical print of equipment labels (program segments NXPRT and PRT). Also writes the proper format specification to the bar code printer (program segment FORMAT).

> Context sensitive help processor useful in the generation of bar coded location labels.

> Prints a "Companion Listing" for a batch of bar coded equipment labels. Companion Listings contain the descriptive information necessary to locate and positively identify a particular piece of equipment. Companion Listings (which are optional) are printed in exactly the same order as the bar code labels themselves. This routine is repeatedly called by the same routine that calls for the physical print of a bar code label.

> Package library; contains output port selector, fiscal year and quarter selection.

> Package utility routine. Contains code called by input transforms in the Equipment and Work Order files.

> Package utility routine. Gets data for equipment records from the Control Point Activity file.

> Program management routine for Engineering package; allows edit of controlled files and site-specific parameters; contains hardcoded menu for module.

Routine Descriptions

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 4%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ENNEWPK2</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Programmer written initialization routine for Engineering package. This</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>routine deletes former Data Dictionary definitions in preparation for</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>installation of new version.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENNEWPKG</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pre-initialization routine for the Engineering package. Checks for</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>prerequisite conditions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENPL1</p>
</blockquote></td>
<td><blockquote>
<p>a.</p>
</blockquote></td>
<td><blockquote>
<p>Entry point "A" is referenced in the computed expression for field BLDG</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>DISPLAY (#178) of Construction Project file (#6925). This subroutine</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>concatenates the multiple BUILDING NUMBERs into a string for display in</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>reports, like the project application.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>b.</p>
</blockquote></td>
<td><blockquote>
<p>Entry point "V" is referenced in input transforms for field OFFICIALS NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(#5) of CITATIONS multiple (#164) and field EVALUATOR (#194.6) of</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Construction Project file (#6925). This subroutine is used to validate the</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>format of a person's name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENPL1A</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Entry point "CHKDATA" is called from ENPL4 and ENPL2, the routines</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>invoked by enter/edit procedures for the 5-Year Facility Plan's construction</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>projects and the Project Application's construction projects, respectively. Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>in this module performs consistency checks for critical fields in the project file,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>in the event the user has Up-Arrowed out of the edit process.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENPL10</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>This routine is referenced by option ENPLM06. This routine controls the</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>printing of the Project Application Executive Summary. In the process, it</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>makes direct calls to routine ENPLPB and then depending on Project Program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>to routine ENPLPA or ENPLPD, which are compiled routines generated from</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>print templates ENPLP006, ENPLP008 and ENPLP009, respectively.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENPL11</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>The entry point "A" is referenced by option ENPLM08. This routine controls</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>the printing of the EMIS Construction Program Environmental Analysis form</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>VAF 10-1192a.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENPL2</p>
</blockquote></td>
<td><blockquote>
<p>a.</p>
</blockquote></td>
<td><blockquote>
<p>Entry point "ENT" is referenced in option ENPLM05. This subroutine controls</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>the Enter/Edit process for Project Application information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>b.</p>
</blockquote></td>
<td><blockquote>
<p>Entry point "ACT" is referenced in option ENPLM18. This subroutine controls</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>the Enter/Edit process for Activation Information for projects already on file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Descriptions

> ENPL3 This routine calculates the Prioritization Methodology Score for Minor and Minor Design projects. It is called at line tag "K" as the Computed Expression for field VAMC MINOR/MINOR MISC SCORE (#233) of Construction Project file (#6925) and at line tag "IN" by routine ENPL3A during the printing of the Prioritization Methodology Scoring Sheet.

> ENPL3A The entry point "A" is referenced by option ENPLM03. ENPL3A and ENPL3B, together print the Minor Design/Minor Misc. Scoring Sheet. ENPL3A calls ENPL3 for the section scores and total score.

> ENPL3B ENPL3A and ENPL3B, together print the Minor Design/Minor Misc. Scoring Sheet. ENPL3A calls ENPL3B at entry point "D".

> ENPL4 The entry point "ENT" is referenced by option ENPLM02. This routine controls the Enter/Edit of information for projects to be included in the 5-Year Plan.

> ENPL5 The entry point "IN" is referenced by option ENPLM11. ENPL5, ENPL5A, ENPL5B, and ENPL5C, together print the 5-Year Facility Plan. This routine prompts the user for information needed to compile and print the report and compiles the list of projects by year which will be included.

> ENPL5A ENPL5, ENPL5A, ENPL5B, and ENPL5C, together print the 5-Year Facility Plan. The entry point "IN" is called by routine ENPL5. This routine prints the list of projects for a given Fiscal Year and the list of High Tech/High Cost Equipment for that year.

> ENPL5B ENPL5, ENPL5A, ENPL5B, and ENPL5C, together print the 5-Year Facility Plan. The entry point "L" is called by routine ENPL5A. This routine prints the detail information for projects proposed for the Budget Year of the Plan.

> ENPL5C ENPL5, ENPL5A, ENPL5B, and ENPL5C, together print the 5-Year Facility Plan. The entry point "FE" is called by routine ENPL5. This routine prints the Project Summary by Programs and Fiscal Years.

> ENPL6 The entry point "ENT" is referenced by option ENPLM09. This routine controls the Enter/Edit of Environmental Analysis information for the project application.

Routine Descriptions

> ENPL7 ENPL7, ENPL7A, ENPL7B, and ENPL7C, together set up the mail message with data from the project application for transmission to higher approval authorities. This routine collects from the user, information necessary to select the project and to determine whether the message is created as a foreground or a background process. It also sets up the initial message segments. Note: The 5-Year Plan Project, Electronic Transmission process uses portions of code from ENPL7 and ENPL7A calling ENPL7 at entry point "ST".

> ENPL7A ENPL7, ENPL7A, ENPL7B, and ENPL7C, together create the MailMan message containing data from the project application. The entry point "B" is called from routine ENPL7. This routine sets up the remaining segments common to the electronic transmission of both the Project Application and the 5-Year Facility Plan Project.

> ENPL7B ENPL7, ENPL7A, ENPL7B, and ENPL7C, together create the MailMan message containing data from the project application. The entry point "I" is called from routine ENPL7A. This routine sets up additional segments for the electronic transmission of the Project Application.

> ENPL7C ENPL7, ENPL7A, ENPL7B, and ENPL7C, together create the MailMan message containing data from the project application. The entry point "N" is called from routine ENPL7B. This routine sets up the final segments for the electronic transmission of the Project Application and makes the call to MailMan to send the message.

> ENPL8 This routine is referenced in option ENPLM14. This routine controls the batch transmission of 5-Year Facility Plan projects to higher approval authorities. It divides the transmission into messages of up to 10 projects each.

> ENPL8A This routine is referenced by option ENPLM15. This routine controls the individual electronic transmission of a Project for the 5-Year Facility Plan. It is intended for providing updates on individual projects, rather than, the initial transmission.

> ENPL9 This routine is referenced by option ENPLM16. It controls the Project Application Approval Process. This routine checks that the user has the appropriate security key for approval at the Chief Engineer or VAMC Director level.

> ENPLPA This routin e is generated by FileMan from print template ENPLP008. ENPLPA1 This routine is generated by FileMan from print template ENPLP008. ENPLPB This routine is generated by FileMan from print template ENPLP006. ENPLPB1 This routine is generated by FileMan from print template ENPLP006. ENPLPC This routine is generated by FileMan from print template ENPLP005. ENPLPC1 This routine is generated by FileMan from print template ENPLP005. ENPLPD This routine is generated by FileMan from print template ENPLP009. ENPLPD1 This routine is generated by FileMan from print template ENPLP009.

> Routine Descriptions

> ENPOST ENPROJ

> ENPROJ1 ENPROJ2 ENPROJ3 ENPROJ7

> ENPROJ8 ENPROJ9

> ENPRP ENPRP1 ENPRP2 ENPRP3 ENPRP4 ENPRP5 ENPRP6 ENSA

> ENSA1

> Post-initialization routine for the Engineering package. Converts data elements and re-indexes if necessary.

> Entry point to the Project Tracking module; contains hardcoded menu driver for module.

> Sets local variables for report 10-0051. Collects milestone dates into local arrays.

> Collects A/E and Contractor data into local variables.

> First stage in electronic transmission of 10-0051. Gives user the choice of sending one project or all of them for which the MONTHLY UPDATES field is set to "YES". Also asks about overwriting previous values.

> Formats the 10-0051 into local array "MSG(1,".

> Places the electronic 10-0051 into a Network Mail message and sends it. Also stores transmitted data as the "previous values".

> Produces hard-copy Construction Project Progress Reports (VA Form 10-0051). Prints the header segment of the 10-0051.

> Prints milestone dates and completion percentages. Prints milestone dates and completion percentages. Prints milestone dates and completion percentages. Prints the Architect/Engineer data block.

> Prints the Contractor data block.

> Initiates the upload and processing of data acquired via an automated electrical safety analyzer (namely the MedTester, manufactured by Dynatech Nevada). Calls UPLD^ENSA1 to read MedTester data into the ^ENG("TMP" global and exits gracefully if input data are not successfully read. If MedTester data is to be used to close out a PM worklist, this routine establishes the identity of that worklist. This routine also determines whether or not a paper copy of test results is desired (line PAPER) and then calls PROCS^ENSA1 to begin processing.

> Acquires physical data from a MedTester (program segment UPLD) and places them in temporary storage in the ^ENG("TMP" global.

> Program segments PROCS through OTHER break down the test report into its constituent parts and store them in local variables.

> Program segment UPDT makes the appropriate calls to properly update the equipment record and (potentially) the Work Order file.

> Routine ENSA7 is invoked if hardcopy test results have been requested.

Routine Descriptions

> ENSA2 Attempts look-up based on VA PM Number (program segment PMN). Updates basic inventory data elements (program segment UPDATE) and handles Exception Messages.

> ENSA3 Attempts Equipment file look-up on the basis of MODEL and SERIAL NUMBER (program segment NOLBL). Contains exit logic (program segments ERR and EXIT) for the MedTester module.

> ENSA4 Attempts to post completed electrical safety inspections to the Equipment Histories by closing out PM work orders.

> ENSA5 Attempts to post completed electrical safety inspections directly to the Equipment History sub-file.

> ENSA6 Explains the concept of "Exception Messages" to the user and checks (program segment WOCHK) to be sure that the inspection in question has not already been posted.

> ENSA7 Actually prints the paper copy of the numerical test results, if desired. Also warns the user of any inconsistency between control number (interpreted as EQUIPMENT ID#) and MODEL-SERIAL NUMBER (program segment DEVCK).

> ENSA8 Handles the case of equipment that fails an automated electrical safety test (via the MedTester). Annotates a regular work order if one exists. Otherwise this routine automatically creates a new one.

> ENSA9 Generates an uns cheduled work order.

> ENSED Screen Server/Edit/Display module used to edit/display construction project information.

> ENSED0 Continuation of routine ENSED. ENSED1 Continuation of routine ENSED. ENSED2 Continuation of routine ENSED.

> ENSP Keys and replacement schedules; contains hardcoded menu for module. ENSP1 Space module room and lock reports.

> ENSP2 Sets variable for space formatted display; contains hardcoded menu for space survey report selection.

> ENSP3 Room space formatted display.

> ENSP4 Removes dangling pointers for the Engineering Lock files.

> ENSP5 Presents data extracts from the Engineering Space file in comma separated format for acceptance by spreadsheets.

> Routine Descriptions

> ENSP6 Main driver for leased space options. ENTEXT Parses text into 80 character segments.

> ENTIDD Software called by input transforms and cross-references. ENTIEQE New routine invoked by the ENIT INVENTORY EDIT option.

> ENTINSD New routine invoked by new style MUMPS cross-references on the NON-SPACE FILE LOCATION and LOCATION fields to trigger other fields and generate bulletins.

> ENTINSR New routine invoked by the ENIT NON-SPACE FILE LOC RPT option. ENTIRA New routine invoked by the ENIT ASSIGN RESP option.

> ENTIRC New routine invoked by the ENIT CERTIFY RESP option. ENTIRN New routine invoked by the ENIT RESP NOTIFY option. ENTIRRE New routine invoked by the ENIT EQUIP RPT option.

> ENTIRRH New routine to print a hand receipt.

> ENTIRRH1 New routine to print a hand receipt (continuation).

> ENTIRRI New routine invoked by the ENIT INDV RESP RPT (COM) and ENIT INDV RESP RPT (IT) options.

> ENTIRRNA New routine invoked by the ENIT RESP NOT ASSIGNED RPT option. ENTIRRU New routine invoked by the ENIT RESP UNSIGNED RPT option.

> ENTIRRX New routine invoked by the ENIT SIGN EXCEPT RPT option. ENTIRS New routine invoked by the ENIT RESP SIGN option.

> ENTIRT New routine invoked by the ENIT TERMINATE RESP option. ENTIRX New routine invoked by the ENIT TRANSFER RESP option. ENTIUTL New routine containing various utilities for IT equipment tracking. ENTIUTL1 New routine containing various utilities for IT Equipment tracking. ENTIUTL2 New routine containing various utilities for IT Equipment tracking.

> ENWAPRE Pre-init for the ENWAI\* routines. These routines install the new work actions. This must be done prior to installation of Engineering 7.0 so that routine ENPOST will be able to convert existing data.

Routine Descriptions

> ENWARD Allows end-users of the Electronic Work Order module to edit work requests which they themselves have entered, but only until such time as Engineering Service transfers them from their temporary receiving area to a working shop. Editing is governed by input template ENWOWARD (File 6920) unless ENZWOWARD has been defined.

> Program segment WRDCK allows end-users to check the status of any Engineering work order in the system; but contains no edit capability. Routines ENEWOD and ENEWOD1 are invoked.

> ENWARD1 Produces a list of incomplete Engineering work orders for end-users of the Electronic Work Order module. List may be generated by LOCATION, by SERVICE, or by the DHCP user who physically entered such requests.

> ENWARD2 Continuation of ENWARD1. Evaluates work orders included in the Incomplete Work Order cross-reference (subscripted as "X","UNCOMP") in accordance with criteria established in routine ENWARD1. Matches are stored in

> the ^UTILITY global (subscript "ENEQ",\$J). Once the ^UTILITY global is built, data elements from the subject work orders are extracted and presented to the user in summary form (line tag PRNTWO through line tag NEXT). If the Incomplete Work Order List is directed to a CRT, the user can obtain an expanded (screen) display of any work order on the list (program segment EXPAND). This segment invokes routine ENEWOD. Hard copy work order printouts are available once the call to ENEWOD has been made.

> ENWO Contains subroutines for work order edits, closing out of work ord ers and equipment histories; also contains hardcoded menu for module.

> ENWO1 Processes Engineering work orders currently on file, via program segments ENT (work order edit) and CLSOUT (close out completed work orders). This functionality is intended for the use of Engineering personnel.

> Program segments EQHIV and EQHI generate equipment Service Reports from the Work Order file. The print specification is contained in FileMan print template EN EQ HIST (File 6920). These Service Reports can differ significantly from the Equipment Histories produced from the Equipment file (see routine ENEQRP1). Work orders that are not yet completed will be reflected in the Service Report but not in the Equipment History. Work orders that have been archived will be reflected in the Equipment History but not in the Service Report. Sites that delete PM work orders during close out of PM worklists (and most sites do this) will find that completed PM work orders are reflected in Equipment Histories but not in Service Reports; whereas incomplete PM work orders are reflected in Service Reports but not Equipment Histories.

> ENWO2 Processes DISAPPROVAL of Engineering work orders. Intended for use by Engineering personnel, mainly in dispositioning Electronic Work Orders. The work order close out process references input template ENWODISAP unless a template named ENZWODISAP has been defined.

> Program segment MSG is actually called by a MUMPS cross-reference on the STATUS field (#32) of the Work Order file (#6920). Whenever the status of a work order is changed to DISAPPROVED, the package will attempt to send a MailMan message to the individual who entered the request in the first place. The Engineering employee who disapproves the work order will appear as the SENDER of this message.

> Routine Descriptions

> ENWOCOMP ENWOD ENWOD1 ENWOD2

> ENWOD3 ENWOINV

> ENWONEW

> ENWONEW1

> ENWONEW2 ENWOP

> ENWOP1 ENWOP2

> ENWOP3

> Tests to see if Work Order is completed.

> Driver for the formatted work order display/edit.

> Builds local array for formatted work order display/edit. Prints formatted work order.

> This routine executes ^%ZOSF("TEST") to check for the existence of locally developed preamble and postamble routines (which must be named ENZWO1 and ENZWO2, respectively).

> ENZWO1 (if it exists) should consist of one or more WRITE commands. Output from this routine will appear at the top of the formatted work orders.

> ENZWO2 (if it exists) should also consist of one or more WRITE commands. Output from this routine will appear at the bottom of the formatted work orders.

> Continuation of formatted work order print (routine ENWOD2).

> Called by cross-reference on the EQUIPMENT ID \# field of the Work Order file. Transfers basic inventory information into the Work Order file (or deletes it) when a value is entered (or deleted) in the EQUIPMENT ID \# field.

> Creates new Engineering work orders. Shop and date are incorporated into the computer generated work order number. Work orders may be edited and/or printed immediately after being entered. Sites that have elected to have new work orders printed automatically will not be asked the "Print this work order?" question.

> Transfers an existing Engineering work order to a different shop. A new work order number is created, but the internal entry number of the subject work order is not affected. The ORIGINAL WORK ORDER \# is never changed by the transfer process. User will be asked if he/she wants to edit work order.

> Edit will be screen driven except in the case of Electronic Work Orders. For Electronic Work Orders the edit will be via FileMan using input template ENWOWARDXFER; except that if the site has defined an input template named ENZWOWARDXFER then it will be used instead of ENWOWARDXFER.

> Continuation of ENWONEW.

> Prints incomplete work orders (by shop) in accordance with criteria established by routine ENWOST. Invoked by ENWOST.

> Writes the synopsis (2 or 3 lines) of each incomplete work order.

> Gives the counts (by shop) of incomplete work orders. Invoked by routine ENWOST.

> Checks incomplete work orders to see if they meet search criteria. Collects local variables and invokes the print logic (ENWOP1).

Routine Descriptions

> ENWOREP Prints (or re-prints) all Engineering work orders entered between user- specified START and STOP dates. Can be run for one particular Engineering Section or for ALL Sections. Work order selection is made on the basis of WORK ORDER \# (.01 field of File \#6920).

> ENWOST Generates work order status by Employee, Location, Owner/ Department or Shop; also contains hardcoded menu for type of status requested.

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 6910 ENG INIT PARAMETERS

> Engineering site parameter file. There should only be ONE entry in this file. If there is more than one entry, the routines will not know which one to believe and are likely to produce unexpected results.

> ENGINEERING COMPUTER PORT

> Used by package specific device selection logic to assist users in identifying output devices. As a rule, only hardcopy print devices should be contained in this file. The intent is to discourage users from inadvertently sending output to a CRT or some other device not intended for printing.

> ENG SOFTWARE OPTIONS

> Used by developers to contain information that governs the performance of selected options. When choices have to be made and there is no clear consensus among stations as to which choice is most advantageous, an attempt is usually made to make the subject parameter site selectable by including it in this file.

> 6910.9 ENG DJ SCREEN

> File of screens used by Engineering Screen Handler.

> 6911 EQUIPMENT CATEGORY

> This file contains default PM (preventive maintenance) parameters for device types. The intent is to give facilities a means of scheduling PM inspections for a given device type (defibrillator, transformer, electrical generator, etc.) without having to explicitly edit the record of each individual piece of equipment. If the PM parameters in the Equipment file (File 6914) do not agree with the corresponding PM parameters in this file, the information in the Equipment file will take precedence.

> 6912 MANUFACTURER LIST FILE

> List of manufacturers. Centrally maintained, courtesy of Engineering Service Center, St. Louis.

> 6914 EQUIPMENT INV.

> Repository of all capital assets. Typically used by Engineering and Supply Services. Ultimately envisioned as a "front-end" for a central capital assets tracking program, such as LOG1 and/or ISMS.

> <span id="_bookmark16" class="anchor"></span>File List

> CMR

> Consolidated Memoranda of Receipt in use at your facility. Basic instrument for establishing accountability for non-expendable equipment.

> PM PROCEDURES

> File of formal procedures used at the host site in the performance of scheduled maintenance (PMI).If a facility wants their source documents in electronic format and is willing to accept the limitations of the FileMan word-processing editor, then the actual step by step text of a PM Procedure may be stored in this file.

> 6916 BERS SURVEY

> Used for submission of an annual report on Biomedical Engineering Resources. This report is prepared by each site and submitted to the National Engineering Service Center in St.

> Louis.

> HAND RECEIPT TEXT

> This file contains versions of the hand receipt text displayed to users when they accept responsibility for IT equipment. The text versions are distributed via nationally issued patches to the Engineering package. For each version a checksum is calculated to detect unauthorized modifications.

> IT ASSIGNMENT

> This file contains assignments of responsibility for IT equipment. The data is only intended to be updated via package options. Key data values are protected by encryption once the owner has accepted responsibility via electronic signature.

> 6917 CATEGORY STOCK NUMBER

> Classification scheme for non-expendable equipment.

> 6919 ENG ARCHIVE LOG

> Permanent record of every archival episode performed within the Engineering package.

> 6920 WORK ORDER \#

> Repository of all work requests directed to Engineering Service. Main file used by the Work Order module.

> 6920.1 NEW WORK ACTION

> Standardized file of Engineering work actions. Introduced with Engineering Version 7. A single work order may have more than one work action associated with it.

> 6921 WORK CENTER CODE

> A list of codes which subdivide Engineering Cost Centers into Work Centers.

> 6922 ENGINEERING SECTION LIST

> A list of functional sections within Engineering Service.

File List

> 6928.3 ENG BUILDING

> A simple file of physical buildings. A "division designation" may be included if needed to distinguish between two buildings having the same number. Suppose, for example, there were two buildings numbered 100 at VAMC St. Louis, one at the John Cochran Division and one at Jefferson Barracks. These two buildings could be entered separately as 100-JC and 100-JB; where "JB" and "JC" are division designators. The same strategy may be useful at facilities that support outpatient clinics, Regional Offices, national cemeteries, etc.

> 6929 ENG EMPLOYEE

> Should contain all Engineering employees who may be associated with a Work Order, whether or not they actually have access to this computer.

> 7335.7 REGULATORY AGENCY

> File of Regulatory Agencies for documenting citations.

> 7336.3 OFM SPACE CLASSIFICATION

> This file is used for Minor Design and Minor Misc. Prioritization Methodology. Here points are given according to the type of space undergoing 100% renovation or new construction.

> 7336.6 OFM H089 CHAPTERS

> This contains the H-08-9 Chapters for Space Planning. It is used to identify areas where space is added or renovated in construction projects.

> OFM PROJ CATEGORY

> File of Construction Project functional categories.

> OFM BUDGET CATEGORY File of

> Construction Project budget categories.

> The following files are distributed with data.

> BARCODE PROGRAM (Overwrite) SPECIALTY COMMANDS (Overwrite) ENG SOFTWARE OPTIONS (Overwrite)

> ENG DJ SCREEN (Overwrite) MANUFACTURER LIST (Overwrite)

> HAND RECEIPT TEXT (Overwrite) CATEGORY STOCK NUMBER (Overwrite)

> NEW WORK ACTION (Overwrite) WORK CENTER CODE (Overwrite) FSA-ACCIDENT ACTIVITY (Merge) FSA-ACCIDENT NATURE (Overwrite) FSA-DIVISION/SERVICE(Merge)

> PROJECT STATUS (Overwrite) ENG SPACE FUNCTIONS (Merge) ENG SPACE UTILITIES (Merge)

> REGULATORY AGENCY (Overwrite)

> File List

> OFM SPACE CLASSIFICATION (Overwrite)

> OFM H089 CHAPTERS (Overwrite) OFM PROJ CATEGORY (Overwrite) OFM BUDGET CATEGORY (Overwrite)

File List

> File List

## Pointer Relationships of Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> •

- ENGINEERING PACKAGE
- FILE FIELD STRUCTURE - POINTER RELATIONS

> •

#### •FILE NAME (NUMBER): BARCODE PROGRAM (446.4)

> •GLOBAL LOCATION: ^PRCT(446.4,

> •

> •DESCRIPTION: This file contains bar code programs and data uploaded from the

> •bar code reader to be used as part of the Bar code Inventory process.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

> •NOTE) There are no files currently pointing to this file.

> •

- FILE 446.4, BARCODE PROGRAM POINTS TO THE FOLLOWING FILES

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 21%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>•</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>FIELD NO. FIELD NAME</p></li>
</ul></td>
<td><blockquote>
<p>FILE NO.</p>
</blockquote></td>
<td><blockquote>
<p>FILE NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•(SUBFIELD)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>.09 SPECIALTY COMMANDS</p></li>
</ul></td>
<td><blockquote>
<p>446.6</p>
</blockquote></td>
<td><blockquote>
<p>SPECIALITY COMMANDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>.1 CREATED BY</p></li>
</ul></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><p>2 DATE/TIME OF DATA UPLOAD</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>(.02) UPLOAD USER</p></li>
</ul></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### •FILE NAME (NUMBER): SPECIALITY COMMANDS (446.6)

> •GLOBAL LOCATION: ^PRCT(446.6,

> •

> •DESCRIPTION: This file contains the Specialty Commands for the bar code reader

> •and printer to be used as part of the Bar code Inventory process.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 446.6, SPECIALITY COMMANDS

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 446.4 BARCODE PROGRAM .09 SPECIALTY COMMANDS

> •

> •NOTE) This file does not currently point to any other file.

> •

#### •FILE NAME (NUMBER): ENG INIT PARAMETERS (6910)

> •GLOBAL LOCATION: ^DIC(6910,

> •

> •DESCRIPTION: Engineering site parameter file. There should only be ONE entry in

> •this file. If there is more than one entry, the routines will not know which

> •one to believe and are likely to produce unexpected results.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*•

> •

> •NOTE) There are no files currently pointing to this file.

> •

- FILE 6910, ENG INIT PARAMETERS POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- 5 TEMPORARY WORK ORDER SECT\* 6922 ENGINEERING SECTION LIST

> •

> •NOTE) \* Names longer than 25 characters have been truncated.

#### •FILE NAME (NUMBER): ENGINEERING COMPUTER PORT (6910.1)

> •GLOBAL LOCATION: ^DIC(6910.1,

> •

> •DESCRIPTION: Used by package specific device selection logic to assist users in

> •

> identifying output devices. As a rule, only hardcopy print devices should be

File List

> •contained in this file. The intent is to discourage users from inadvertently

> •sending output to a CRT or some other device not intended for printing.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

> •NOTE) There are no files currently pointing to this file.

> •

- FILE 6910.1, ENGINEERING COMPUTER PORT POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- .01 DEVICE \# 3.5 DEVICE

> •

#### •FILE NAME (NUMBER): ENG SOFTWARE OPTIONS (6910.2)

> •GLOBAL LOCATION: ^ENG(6910.2,

> •

> •DESCRIPTION: Used by developers to contain information that governs the

> •performance of selected options. When choices have to be made and there is no

> •clear consensus among stations as to which choice is most advantageous, an

> •attempt is usually made to make the subject parameter site selectable by

> •including it in this file.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

> •NOTE) There are no files currently pointing to this file.

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): ENG DJ SCREEN (6910.9)

> •GLOBAL LOCATION: ^ENG(6910.9,

> •

> •DESCRIPTION: File of screens used by Engineering Screen Handler.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

> •NOTE) There are no files currently pointing to this file.

> •

> •NOTE) This file does not currently point to any other file.

> •

> File List

#### •FILE NAME (NUMBER): EQUIPMENT CATEGORY (6911)

> •GLOBAL LOCATION: ^ENG(6911,

> •

> •DESCRIPTION: This file contains default PM (preventive maintenance) parameters

> •for device types. The intent is to give facilities a means of scheduling PM

> •inspections for a given device type (defibrillator, transformer, electrical

> •generator, etc) without having to explicitly edit the record of each individual

> •piece of equipment. If the PM parameters in the EQUIPMENT file (File 6914) do

> •not agree with the corresponding PM parameters in this file, the information in

> •the EQUIPMENT file will take precedence.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6911, EQUIPMENT CATEGORY

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6914 EQUIPMENT INV. 6 EQUIPMENT CATEGORY

> •

- FILE 6911, EQUIPMENT CATEGORY POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- 1
- (.01)

> RESPONSIBLE SHOP

> RESPONSIBLE SHOP 6922 ENGINEERING SECTION LIST

- 1 RESPONSIBLE
- \(1\) TECHNICIAN
- 1 RESPONSIBLE
- \(3\) FREQUENCY
- \(4\) PROCEDURE

> •

> SHOP SHOP

> 6929 ENG EMPLOYEE

> 6914.2 PM PROCEDURES

#### •FILE NAME (NUMBER): MANUFACTURER LIST FILE (6912)

> •GLOBAL LOCATION: ^ENG("MFG",

> •

> •DESCRIPTION: List of manufacturers. Centrally maintained, courtesy of

> •Engineering Service Center, St. Louis.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6912, MANUFACTURER LIST FILE

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6914 EQUIPMENT INV. 1 MANUFACTURER
- 6916 I.A.1. NAME 5 I.A.1. NAME
- \(8\) 7b. MFG/EQUIP TYPE/MOD#
- (.01) 7b. MFG NAME
- 15 VI.A. CONTRACT SERVICE
- \(2\) MANUFACTURER NAME
- 6920 WORK ORDER \# 21.9 MANUFACTURER

> •

> •NOTE) This file does not currently point to any other file.

> •

File List

#### •FILE NAME (NUMBER): EQUIPMENT INV. (6914)

> •GLOBAL LOCATION: ^ENG(6914,

> •

> •DESCRIPTION: Repository of all capital assets. Typically used by Engineering

> •and Supply Services. Ultimately envisioned as a "front-end" for a central

> •capital assets tracking program, such as LOG1 and/or ISMS.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6914, EQUIPMENT INV.

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6914 EQUIPMENT INV. 2 PARENT SYSTEM
- 6920 WORK ORDER \# 18 EQUIPMENT ID#

> •

- FILE 6914, EQUIPMENT INV. POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>•</p>
</blockquote></th>
<th>1</th>
<th><blockquote>
<p>MANUFACTURER</p>
</blockquote></th>
<th><blockquote>
<p>6912</p>
</blockquote></th>
<th><blockquote>
<p>MANUFACTURER LIST FILE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>PARENT SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>6914</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENT INV.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>EQUIPMENT CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>6911</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENT CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>FEDERAL SUPPLY CLASSIFICA*</p>
</blockquote></td>
<td>441.2</td>
<td><blockquote>
<p>* NON EXISTENT FILE *</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>VENDOR POINTER</p>
</blockquote></td>
<td><blockquote>
<p>440</p>
</blockquote></td>
<td><blockquote>
<p>VENDOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>13.5</p>
</blockquote></td>
<td><blockquote>
<p>ACQUISITION SOURCE</p>
</blockquote></td>
<td>420.8</td>
<td><blockquote>
<p>SOURCE CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY STOCK NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>6917</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY STOCK NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>CMR</p>
</blockquote></td>
<td>6914.1</td>
<td><blockquote>
<p>CMR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE POINTER</p>
</blockquote></td>
<td><blockquote>
<p>49</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>6928</p>
</blockquote></td>
<td><blockquote>
<p>ENG SPACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td>(.01)</td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td><blockquote>
<p>6922</p>
</blockquote></td>
<td><blockquote>
<p>ENGINEERING SECTION LIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td>(1)</td>
<td><blockquote>
<p>TECHNICIAN</p>
</blockquote></td>
<td><blockquote>
<p>6929</p>
</blockquote></td>
<td><blockquote>
<p>ENG EMPLOYEE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
<p>•</p>
</blockquote></td>
<td colspan="2"><ol start="3" type="1">
<li><p>FREQUENCY</p></li>
<li><blockquote>
<p>PROCEDURE</p>
</blockquote></li>
</ol></td>
<td>6914.2</td>
<td><blockquote>
<p>PM PROCEDURES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>COST CENTER</p>
</blockquote></td>
<td>420.1</td>
<td><blockquote>
<p>COST CENTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>SUBACCOUNT</p>
</blockquote></td>
<td>420.2</td>
<td><blockquote>
<p>SUBACCOUNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> •NOTE) \* Names longer than 25 characters have been truncated.

> File List

#### •FILE NAME (NUMBER): CMR (6914.1)

> •GLOBAL LOCATION: ^ENG(6914.1,

> •

> •DESCRIPTION: Consolidated Memoranda of Receipt in use at your facility. Basic

> •instrument for establishing accountability for non-expendable equipment.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6914.1, CMR

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6914 EQUIPMENT INV. 19 CMR

> •

- FILE 6914.1, CMR POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- .5 SERVICE 49 SERVICE/SECTION
- 1 RESPONSIBLE OFFICIAL 200 NEW PERSON

> •

> •

#### •FILE NAME (NUMBER): PM PROCEDURES (6914.2)

> •GLOBAL LOCATION: ^ENG(6914.2,

> •

> •DESCRIPTION: File of formal procedures used at the host site in the performance

> •of scheduled maintenance (PMI). If a facility wants their source documents in

> •electronic format and is willing to accept the limitations of the FileMan

> •word-processing editor, then the actual step by step text of a PM Procedure may

> •be stored in this file.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6914.2, PM PROCEDURES

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6911 RESPONSIBLE SHOP 1 RESPONSIBLE SHOP
- \(3\) FREQUENCY
- \(4\) PROCEDURE
- 6914 RESPONSIBLE SHOP 30 RESPONSIBLE SHOP
- \(3\) FREQUENCY
- \(4\) PROCEDURE

> •

> •NOTE) This file does not currently point to any other file.

> •

File List

#### FILE NAME (NUMBER): BERS SURVEY (6916)

> GLOBAL LOCATION: ^ENGS(6916,

> DESCRIPTION: Used for submission of an annual report on Biomedical Engineering Resources. This report is prepared by each site and submitted to the National Engineering Service Center in St. Louis.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> NOTE) There are no files currently pointing to this file.

> FILE 6916, BERS SURVEY POINTS TO THE FOLLOWING FILES

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 36%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FIELD NO.</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NAME</p>
</blockquote></th>
<th>FILE</th>
<th><blockquote>
<p>NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>(SUBFIELD)</p>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>I.A.1. NAME</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(8)</p>
</blockquote></td>
<td><blockquote>
<p>7b. MFG/EQUIP TYPE/MOD#</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(.01)</p>
</blockquote></td>
<td><blockquote>
<p>7b. MFG NAME</p>
</blockquote></td>
<td>6912</td>
<td></td>
<td><blockquote>
<p>MANUFACTURER LIST FILE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>VI.A. CONTRACT SERVICE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(2)</p>
</blockquote></td>
<td><blockquote>
<p>MANUFACTURER NAME</p>
</blockquote></td>
<td>6912</td>
<td></td>
<td><blockquote>
<p>MANUFACTURER LIST FILE</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### FILE NAME (NUMBER): HAND RECEIPT TEXT (6916.2)

> GLOBAL LOCATION: ^ENG(6916.2,

> DESCRIPTION: This file contains versions of the hand receipt text displayed to users when they accept responsibility for IT equipment. The text versions are distributed via nationally issued patches to the Engineering package. For each version a checksum is calculated to detect unauthorized modifications.

> \*\*\* FILE FLOW DIAGRAM \*\*\* FILES POINTING TO FILE 6916.2, HAND RECEIPT TEXT

> FILE NO. FILE NAME FIELD NO. FIELD NAME

> (SUBFILE)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 34%" />
<col style="width: 10%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>6916.3</p>
</blockquote></th>
<th><blockquote>
<p>IT ASSIGNMENT</p>
</blockquote></th>
<th>5</th>
<th><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>6916.3</p>
</blockquote></td>
<td><blockquote>
<p>IT ASSIGNMENT</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>PREVIOUS SIGNATURES</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>(1)</td>
<td></td>
<td><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> NOTE) This file does not currently point to any other file.

#### FILE NAME (NUMBER): IT ASSIGNMENT (6916.3)

> GLOBAL LOCATION: ^ENG(6916.3,

> DESCRIPTION: This file contains assignments of responsibility for IT equipment. The data is only intended to be updated via package options. Key data values are protected by encryption once the owner has accepted responsibility via electronic signature.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> NOTE) There are no files currently pointing to this file.

> FILE 6916.3, IT ASSIGNMENT POINTS TO THE FOLLOWING FILES:

> FIELD NO. FIELD NAME FILE NO. FILE NAME (SUBFILE)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>EQUIPMENT</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>6914</p>
</blockquote></th>
<th><blockquote>
<p>EQUIPMENT INV.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>OWNER</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>ASSIGNED BY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>HAND RECEIPT</p>
</blockquote></td>
<td><blockquote>
<p>TEXT</p>
</blockquote></td>
<td><blockquote>
<p>6916.2</p>
</blockquote></td>
<td><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>CERTIFIED BY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>ENDED BY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PREVIOUS SIGNATURES</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(1)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></td>
<td><blockquote>
<p>6916.2</p>
</blockquote></td>
<td><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(3)</p>
</blockquote></td>
<td><blockquote>
<p>CERTIFIED BY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> File List

#### FILE NAME (NUMBER): CATEGORY STOCK NUMBER (6917)

> GLOBAL LOCATION: ^ENCSN(6917,

> DESCRIPTION: Classification scheme for non-expendable equipment.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6917, CATEGORY STOCK NUMBER

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 34%" />
<col style="width: 28%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NO.</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(SUBFIELD)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6914</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENT INV.</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY STOCK</p>
</blockquote></td>
</tr>
</tbody>
</table>

> NUMBER FILE 6917, CATEGORY STOCK NUMBER POINTS TO THE FOLLOWING FILES

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 13%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FIELD NO. FIELD NAME (SUBFIELD)</p>
</blockquote></th>
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5 SKU</p>
</blockquote></td>
<td><blockquote>
<p>420.5</p>
</blockquote></td>
<td><blockquote>
<p>* NON EXISTENT FILE *</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6 FSC CODE</p>
</blockquote></td>
<td><blockquote>
<p>441.2</p>
</blockquote></td>
<td><blockquote>
<p>* NON EXISTENT FILE *</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8 SUBACCOUNT</p>
</blockquote></td>
<td><blockquote>
<p>420.2</p>
</blockquote></td>
<td><blockquote>
<p>SUBACCOUNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11 ACTIVATED BY</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13 DEACTIVATED BY</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15 EDITED BY</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16 VENDOR</p>
<p>(.01) VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>440</p>
</blockquote></td>
<td><blockquote>
<p>VENDOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FILE NAME (NUMBER): ENG ARCHIVE LOG (6919)</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> GLOBAL LOCATION: ^ENG(6919,

> DESCRIPTION: Permanent record of every archival episode performed within the Engineering package.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> NOTE) There are no files currently pointing to this file. NOTE) This file does not currently point to any other file.

#### FILE NAME (NUMBER): WORK ORDER \# (6920)

> GLOBAL LOCATION: ^ENG(6920,

> DESCRIPTION: Repository of all work requests directed to Engineering Service. Main file used by the Work Order module.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6920, WORK ORDER \#

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NO. FIELD NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(SUBFIELD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410</p>
</blockquote></td>
<td><blockquote>
<p>CONTROL POINT ACTIVITY</p>
</blockquote></td>
<td><blockquote>
<p>49 SORT GROUP</p>
</blockquote></td>
</tr>
</tbody>
</table>

> FILE 6920, WORK ORDER \# POINTS TO THE FOLLOWING FILES

> FIELD NO. FIELD NAME FILE NO. FILE NAME (SUBFIELD)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 15%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>3</th>
<th><blockquote>
<p>LOCATION</p>
</blockquote></th>
<th>6928</th>
<th><blockquote>
<p>ENG SPACE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7.5</p>
</blockquote></td>
<td><blockquote>
<p>ENTERED BY</p>
</blockquote></td>
<td>200</td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>SHOP</p>
</blockquote></td>
<td>6922</td>
<td><blockquote>
<p>ENGINEERING SECTION LIST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>PRIMARY TECH ASSIGNED</p>
</blockquote></td>
<td>6929</td>
<td><blockquote>
<p>ENG EMPLOYEE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16.5</p>
</blockquote></td>
<td><blockquote>
<p>TECHNICIANS ASSIGNED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>(.01)</td>
<td><blockquote>
<p>ASSIGNED TECH</p>
</blockquote></td>
<td>6929</td>
<td><blockquote>
<p>ENG EMPLOYEE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16.5</p>
</blockquote></td>
<td><blockquote>
<p>TECHNICIANS ASSIGNED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>(2)</td>
<td><blockquote>
<p>SHOP</p>
</blockquote></td>
<td>6922</td>
<td><blockquote>
<p>ENGINEERING SECTION LIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENT ID#</p>
</blockquote></td>
<td>6914</td>
<td><blockquote>
<p>EQUIPMENT INV.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21.9</p>
</blockquote></td>
<td><blockquote>
<p>MANUFACTURER</p>
</blockquote></td>
<td>6912</td>
<td><blockquote>
<p>MANUFACTURER LIST FILE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>OWNER/DEPARTMENT</p>
</blockquote></td>
<td>49</td>
<td><blockquote>
<p>SERVICE/SECTION</p>
</blockquote></td>
</tr>
</tbody>
</table>

File List

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>31</p>
</blockquote></th>
<th><blockquote>
<p>PARTS ORDERED ON</p>
</blockquote></th>
<th><blockquote>
<p>ACC.#</p>
</blockquote></th>
<th><blockquote>
<p>410</p>
</blockquote></th>
<th><blockquote>
<p>CONTROL POINT ACTIVITY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>WORK ACTION</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(.01)</p>
</blockquote></td>
<td><blockquote>
<p>WORK ACTION</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6920.1</p>
</blockquote></td>
<td><blockquote>
<p>NEW WORK ACTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35.5</p>
</blockquote></td>
<td><blockquote>
<p>WORK CENTER CODE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6921</p>
</blockquote></td>
<td><blockquote>
<p>WORK CENTER CODE</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### FILE NAME (NUMBER): NEW WORK ACTION (6920.1)

> GLOBAL LOCATION: ^ENG(6920.1,•

> DESCRIPTION: Standardized file of Engineering work actions. Introduced with Engineering Version 7. A single work order may have more than one work action associated with it.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6920.1, NEW WORK ACTION

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 26%" />
<col style="width: 32%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th>FILE</th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th>FIELD NO.</th>
<th><blockquote>
<p>FIELD NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(SUBFIELD)</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6920</p>
</blockquote></td>
<td>WORK</td>
<td><blockquote>
<p>ACTION</p>
</blockquote></td>
<td>35</td>
<td><blockquote>
<p>WORK ACTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(.01)</td>
<td><blockquote>
<p>WORK ACTION</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 6920.5 WORK ACTION 1 NEW WORK ACTION

> NOTE) This file does not currently point to any other file.

#### FILE NAME (NUMBER): WORK CENTER CODE (6921)

> GLOBAL LOCATION: ^DIC(6921,

> DESCRIPTION: A list of codes which subdivide Engineering Cost Centers into Work Centers.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6921, WORK CENTER CODE

> FILE NO. FILE NAME FIELD NO. FIELD NAME (SUBFIELD)

> 6920 WORK ORDER \# 35.5 WORK CENTER CODE

> NOTE) This file does not currently point to any other file.

#### FILE NAME (NUMBER): ENGINEERING SECTION LIST (6922)

> GLOBAL LOCATION: ^DIC(6922,

> DESCRIPTION: A list of functional sections within Engineering Service.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6922, ENGINEERING SECTION LIST

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NO.</p>
</blockquote></th>
<th><blockquote>
<p>FIELD NAME</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(SUBFIELD)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6910</p>
</blockquote></td>
<td><blockquote>
<p>ENG INIT PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>TEMPORARY WORK ORDER</p>
</blockquote></td>
<td><blockquote>
<p>SECT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6911</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(.01)</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6914</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(.01)</p>
</blockquote></td>
<td><blockquote>
<p>RESPONSIBLE SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6920</p>
</blockquote></td>
<td><blockquote>
<p>WORK ORDER #</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ASSISTING TECH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(2)</p>
</blockquote></td>
<td><blockquote>
<p>SHOP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6929</p>
</blockquote></td>
<td><blockquote>
<p>ENG EMPLOYEE</p>
</blockquote></td>
<td><blockquote>
<p>.3</p>
</blockquote></td>
<td><blockquote>
<p>SHOP</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> FILE 6922, ENGINEERING SECTION LIST POINTS TO THE FOLLOWING FILES

<table style="width:100%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 30%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FIELD NO. FIELD NAME</p>
</blockquote></th>
<th><blockquote>
<p>FILE NO.</p>
</blockquote></th>
<th><blockquote>
<p>FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>(SUBFIELD)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 DEVICE</p>
</blockquote></td>
<td><blockquote>
<p>3.5</p>
</blockquote></td>
<td><blockquote>
<p>DEVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 PM MONTH</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \(1\) TECHNICIAN

> (.01) TECHNICIAN 6929 ENG EMPLOYEE

> File List

#### FILE NAME (NUMBER): FSA-2162 REPORT (6924)

> GLOBAL LOCATION: ^ENG("FSA",

> DESCRIPTION: Information taken from accident reports.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> NOTE) There are no files currently pointing to this file.

> FILE 6924, FSA-2162 REPORT POINTS TO THE FOLLOWING FILES

> FIELD NO. FIELD NAME FILE NO. FILE NAME (SUBFIELD)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 38%" />
<col style="width: 19%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>24</p>
</blockquote></th>
<th><blockquote>
<p>ACCIDENT ACTIVITY</p>
</blockquote></th>
<th>6924.1</th>
<th><blockquote>
<p>FSA-ACCIDENT ACTIVITY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/DIVISION #</p>
</blockquote></td>
<td>6924.3</td>
<td><blockquote>
<p>FSA-DIVISION/SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>INJURY/ILLNESS NATURE</p>
</blockquote></td>
<td>6924.2</td>
<td><blockquote>
<p>FSA-ACCIDENT NATURE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ENGINEERING PACKAGE

> FILE FIELD STRUCTURE - POINTER RELATIONS

#### FILE NAME (NUMBER): FSA-ACCIDENT ACTIVITY (6924.1)

> GLOBAL LOCATION: ^ENG(6924.1,

> DESCRIPTION: Standardized functional activities.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6924.1, FSA-ACCIDENT ACTIVITY FILE NO. FILE NAME FIELD NO. FIELD NAME

> (SUBFIELD)

> 6924 FSA-2162 REPORT 24 ACCIDENT ACTIVITY

> NOTE) This file does not currently point to any other file.

#### FILE NAME (NUMBER): FSA-ACCIDENT NATURE (6924.2)

> GLOBAL LOCATION: ^ENG(6924.2,

> DESCRIPTION: Physiological manifestation of accident.

> \*\*\* FILE FLOW DIAGRAM \*\*\*

> FILES POINTING TO FILE 6924.2, FSA-ACCIDENT NATURE FILE NO. FILE NAME FIELD NO. FIELD NAME

> (SUBFIELD)

> 6924 FSA-2162 REPORT 30 INJURY/ILLNESS NATURE

> NOTE) This file does not currently point to any other file.

File List

#### •FILE NAME (NUMBER): FSA-DIVISION/SERVICE (6924.3)

> •GLOBAL LOCATION: ^ENG(6924.3,

> •

> •DESCRIPTION: File of functional divisions within a Medical Center for purposes

> •of cataloging Accident Reports.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6924.3, FSA-DIVISION/SERVICE

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6924 FSA-2162 REPORT 25 SERVICE/DIVISION \#

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): CONSTRUCTION PROJECT (6925)

> •GLOBAL LOCATION: ^ENG("PROJ",

> •

> •DESCRIPTION: File of delegated projects. Fund amounts should be recorded in

> •whole dollars only.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6925, CONSTRUCTION PROJECT

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 DOMINOS 225 DOMINOS
- (.01) DOMINO PROJECT
- 6928.3 ENG BUILDING 20 PROJECT NO.

> •

- FILE 6925, CONSTRUCTION PROJECT POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 12%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>•</th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>MEDICAL CENTER</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>INSTITUTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td><blockquote>
<p>6925.2</p>
</blockquote></td>
<td><blockquote>
<p>PROJECT STATUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>15.3</p>
</blockquote></td>
<td><blockquote>
<p>OLD MEDICAL CENTER</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>15.8</p>
</blockquote></td>
<td><blockquote>
<p>OLD STATUS</p>
</blockquote></td>
<td><blockquote>
<p>6925.2</p>
</blockquote></td>
<td><blockquote>
<p>PROJECT STATUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>158.1</p>
</blockquote></td>
<td><blockquote>
<p>PROJECT CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.8</p>
</blockquote></td>
<td><blockquote>
<p>OFM PROJ CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>158.2</p>
</blockquote></td>
<td><blockquote>
<p>BUDGET CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.9</p>
</blockquote></td>
<td><blockquote>
<p>OFM BUDGET CATEGORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>159.2</p>
</blockquote></td>
<td><blockquote>
<p>OLD PROJECT CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.8</p>
</blockquote></td>
<td><blockquote>
<p>OFM PROJ CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>159.3</p>
</blockquote></td>
<td><blockquote>
<p>OLD BUDGET CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.9</p>
</blockquote></td>
<td><blockquote>
<p>OFM BUDGET CATEGORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
<p>•</p>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>164</p>
<p>(3)</p>
<p>177</p>
</blockquote></td>
<td><blockquote>
<p>CITATIONS</p>
<p>CITING AUTHORITY BUILDING NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>7335.7</p>
</blockquote></td>
<td><blockquote>
<p>REGULATORY AGENCY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td>(.01)</td>
<td><blockquote>
<p>BUILDING NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>6928.3</p>
</blockquote></td>
<td><blockquote>
<p>ENG BUILDING</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>H089</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>•</td>
<td>(.01)</td>
<td><blockquote>
<p>H089 CHAPTER NAME</p>
</blockquote></td>
<td><blockquote>
<p>7336.6</p>
</blockquote></td>
<td><blockquote>
<p>OFM H089 CHAPTERS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>225</p>
</blockquote></td>
<td><blockquote>
<p>DOMINOS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>•</td>
<td>(.01)</td>
<td><blockquote>
<p>DOMINO PROJECT</p>
</blockquote></td>
<td><blockquote>
<p>6925</p>
</blockquote></td>
<td><blockquote>
<p>CONSTRUCTION PROJECT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>245</p>
<p>248</p>
</blockquote></td>
<td><blockquote>
<p>CHIEF ENGINEER NAME</p>
<p>VAMC DIRECTOR/DESIGNEE NA*</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>264</p>
</blockquote></td>
<td><blockquote>
<p>SPACE USE FOR PRIORITIZAT*</p>
</blockquote></td>
<td><blockquote>
<p>7336.3</p>
</blockquote></td>
<td><blockquote>
<p>OFM SPACE CLASSIFICATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td><blockquote>
<p>279.1</p>
</blockquote></td>
<td><blockquote>
<p>TRANSMITTER 5YR PLAN</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>•</td>
<td><blockquote>
<p>279.3</p>
</blockquote></td>
<td><blockquote>
<p>TRANSMITTER PROJ APPLICAT*</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>•</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>•NOTE) * Names longer than 25 characters have been truncated.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### •FILE NAME (NUMBER): PROJECT STATUS (6925.2)

> •GLOBAL LOCATION: ^ENG(6925.2,

> •

> •DESCRIPTION:

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

> File List

- FILES POINTING TO FILE 6925.2, PROJECT STATUS

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 CONSTRUCTION PROJECT 6 STATUS

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): EMPLOYEE(KEYS) (6926)

> •GLOBAL LOCATION: ^ENG("KEY",

> •

> •DESCRIPTION: This file contains the names of employees who have been issued

> •keys and the keys they have been issued.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6926, EMPLOYEE(KEYS)

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6927 ISSUED TO 5 ISSUED TO
- (.01) ISSUED TO

> •

- FILE 6926, EMPLOYEE(KEYS) POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- .4 SERVICE 49 SERVICE/SECTION
- 1 KEYS ISSUED
- (.01) KEYS ISSUED 6927 LOCKS

> •

File List

#### •FILE NAME (NUMBER): LOCKS (6927)

> •GLOBAL LOCATION: ^ENG("LK",

> •

> •DESCRIPTION: Information concerning locks used in the Medical Center; such as

> •control keys, master keys, pathways, etc.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6927, LOCKS

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6926 KEYS ISSUED 1 KEYS ISSUED
- (.01) KEYS ISSUED
- 6928 ENG SPACE 2 KEY

> •

- FILE 6927, LOCKS POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- 5 ISSUED TO
- (.01) ISSUED TO 6926 EMPLOYEE(KEYS)

> •

> •

#### •FILE NAME (NUMBER): ENG SPACE (6928)

> •GLOBAL LOCATION: ^ENG("SP",

> •

> •DESCRIPTION: Main file used by the space module. It contains detailed

> •information on each room within the Medical Center.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6928, ENG SPACE

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6914 EQUIPMENT INV. 24 LOCATION
- 6920 WORK ORDER \# 3 LOCATION

> •

- FILE 6928, ENG SPACE POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 37%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>.51</p></li>
</ul></th>
<th><blockquote>
<p>BUILDING FILE POINTER</p>
</blockquote></th>
<th><blockquote>
<p>6928.3</p>
</blockquote></th>
<th><blockquote>
<p>ENG BUILDING</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>1.5</p></li>
</ul></td>
<td><blockquote>
<p>SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>49</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><p>2</p></li>
</ul></td>
<td><blockquote>
<p>KEY</p>
</blockquote></td>
<td><blockquote>
<p>6927</p>
</blockquote></td>
<td><blockquote>
<p>LOCKS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>2.6</p></li>
</ul></td>
<td><blockquote>
<p>FUNCTION</p>
</blockquote></td>
<td><blockquote>
<p>6928.1</p>
</blockquote></td>
<td><blockquote>
<p>ENG SPACE FUNCTIONS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><p>4.9</p></li>
</ul></td>
<td><blockquote>
<p>H-08-9 CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>7336.6</p>
</blockquote></td>
<td><blockquote>
<p>OFM H089 CHAPTERS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>14</p></li>
</ul></td>
<td><blockquote>
<p>UTILITIES</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><ul>
<li><p>(.01) UTILITIES</p></li>
</ul></td>
<td><blockquote>
<p>6928.2</p>
</blockquote></td>
<td><blockquote>
<p>ENG SPACE UTILITIES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> •

> File List

#### •FILE NAME (NUMBER): ENG SPACE FUNCTIONS (6928.1)

> •GLOBAL LOCATION: ^ENG(6928.1,

> •

> •DESCRIPTION: Functional areas commonly found in VA facilities.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6928.1, ENG SPACE FUNCTIONS

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6928 ENG SPACE 2.6 FUNCTION

> •

> •NOTE) This file does not currently point to any other file.

> •

#### •FILE NAME (NUMBER): ENG SPACE UTILITIES (6928.2)

> •GLOBAL LOCATION: ^ENG(6928.2,

> •

> •DESCRIPTION: Common hospital utilities.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6928.2, ENG SPACE UTILITIES

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6928 UTILITIES 14 UTILITIES
- (.01) UTILITIES

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): ENG BUILDING (6928.3)

> •GLOBAL LOCATION: ^ENG(6928.3,

> •

> •DESCRIPTION: A simple file of physical buildings. A 'division designation' may •be included if needed to distinguish between two buildings having the same •number.

> Suppose, for example, there were two buildings numbered 100 at VAMC St. •Louis, one at the John Cochran Division and one at Jefferson Barracks. These •two buildings could be entered separately as 100-JC and 100-JB; where 'JB' and •'JC' are division designators. The same strategy may be useful at facilities •that support outpatient clinics, Regional Offices, national cemeteries, etc.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6928.3, ENG BUILDING

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 BUILDING NBR BUILDING NBR
- (.01) BUILDING NUMBER
- 6928 ENG SPACE .51 BUILDING FILE POINTER

> •

- FILE 6928.3, ENG BUILDING POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 21%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>•</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>OWNER</p>
</blockquote></th>
<th><blockquote>
<p>STATE</p>
</blockquote></th>
<th>5</th>
<th><blockquote>
<p>STATE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>5.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PROPERTY STATE</p>
</blockquote></td>
<td>5</td>
<td><blockquote>
<p>STATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PROJECT NO.</p>
</blockquote></td>
<td>6925</td>
<td><blockquote>
<p>CONSTRUCTION PROJECT</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### •FILE NAME (NUMBER): ENG EMPLOYEE (6929)

> •GLOBAL LOCATION: ^ENG("EMP",

> •

> •DESCRIPTION: Should contain all Engineering employees who may be associated

> •with a Work Order, whether or not they actually have access to this computer.

> •

File List

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 6929, ENG EMPLOYEE

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6911 RESPONSIBLE SHOP 1 RESPONSIBLE SHOP
- \(1\) TECHNICIAN
- 6914 RESPONSIBLE SHOP 30 RESPONSIBLE SHOP
- \(1\) TECHNICIAN
- 6920 WORK ORDER \# 16 PRIMARY TECH ASSIGNED
- ASSISTING TECH
- (.01) ASSIGNED TECH
- 6922 PM MONTH 3 PM MONTH
- \(1\) TECHNICIAN
- (.01) TECHNICIAN

> •

- FILE 6929, ENG EMPLOYEE POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 27%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>•</p>
</blockquote></th>
<th><blockquote>
<p>.3</p>
</blockquote></th>
<th><blockquote>
<p>SHOP</p>
</blockquote></th>
<th><blockquote>
<p>6922</p>
</blockquote></th>
<th><blockquote>
<p>ENGINEERING SECTION</p>
</blockquote></th>
<th><blockquote>
<p>LIST</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>COST CENTER</p>
</blockquote></td>
<td><blockquote>
<p>420.1</p>
</blockquote></td>
<td><blockquote>
<p>COST CENTER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>•</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### •FILE NAME (NUMBER): REGULATORY AGENCY (7335.7)

> •GLOBAL LOCATION: ^OFM(7335.7,

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 7335.7, REGULATORY AGENCY

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 CITATIONS 164 CITATIONS
- \(3\) CITING AUTHORITY

> •

- FILE 7335.7, REGULATORY AGENCY POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

- 5 STATE 5 STATE

> •

> File List

#### •FILE NAME (NUMBER): OFM SPACE CLASSIFICATION (7336.3)

> •GLOBAL LOCATION: ^OFM(7336.3,

> •

> •DESCRIPTION: This file is used for Minor Design and Minor Miscellaneous

> •Prioritization Methodology. Here points are given according to the type of

> •space undergoing 100% renovation or new construction.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 7336.3, OFM SPACE CLASSIFICATION

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 CONSTRUCTION PROJECT 264 SPACE USE FOR PRIORITIZAT

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): OFM H089 CHAPTERS (7336.6)

> •GLOBAL LOCATION: ^OFM(7336.6,

> •

> •DESCRIPTION: This contains the H-08-9 Chapters for Space Planning. It is used

> •to identify areas where space is added or renovated in construction projects.

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 7336.6, OFM H089 CHAPTERS

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 H089 180 H089
- (.01) H089 CHAPTER NAME
- 6928 ENG SPACE 4.9 H-08-9 CRITERIA

> •

> •NOTE) This file does not currently point to any other file.

> •

> •

#### •FILE NAME (NUMBER): OFM PROJ CATEGORY (7336.8)

> •GLOBAL LOCATION: ^OFM(7336.8,

> •

> •DESCRIPTION:

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

- FILES POINTING TO FILE 7336.8, OFM PROJ CATEGORY

> •

> •FILE NO. FILE NAME FIELD NO. FIELD NAME

- (SUBFIELD)

> •

- 6925 CONSTRUCTION PROJECT 158.1 PROJECT CATEGORY

> •

- FILE 7336.8, OFM PROJ CATEGORY POINTS TO THE FOLLOWING FILES

> •

- FIELD NO. FIELD NAME FILE NO. FILE NAME

> •(SUBFIELD)

> •

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>8</p></li>
</ul></th>
<th><blockquote>
<p>MA BUDGET CATEGORY</p>
</blockquote></th>
<th>7336.9</th>
<th>OFM</th>
<th><blockquote>
<p>BUDGET</p>
</blockquote></th>
<th><blockquote>
<p>CATEGORY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>9</p></li>
</ul></td>
<td><blockquote>
<p>MI BUDGET CATEGORY</p>
</blockquote></td>
<td>7336.9</td>
<td>OFM</td>
<td><blockquote>
<p>BUDGET</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><p>10</p></li>
</ul></td>
<td><blockquote>
<p>MM BUDGET CATEGORY</p>
</blockquote></td>
<td>7336.9</td>
<td>OFM</td>
<td><blockquote>
<p>BUDGET</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>11</p></li>
</ul></td>
<td><blockquote>
<p>NRM BUDGET CATEGORY</p>
</blockquote></td>
<td>7336.9</td>
<td>OFM</td>
<td><blockquote>
<p>BUDGET</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> •

> •

#### •FILE NAME (NUMBER): OFM BUDGET CATEGORY (7336.9)

> •GLOBAL LOCATION: ^OFM(7336.9,

> •

> •DESCRIPTION:

> •

- \*\*\* FILE FLOW DIAGRAM \*\*\*

> •

File List

> FILES POINTING TO FILE 7336.9, OFM BUDGET CATEGORY• FILE NO. FILE NAME FIELD NO. FIELD NAME (SUBFIELD)•

> 6925 CONSTRUCTION PROJECT 158.2 BUDGET CATEGORY

> 7336.8 OFM PROJ CATEGORY 8 MA BUDGET CATEGORY•

> NOTE) This file does not currently point to any other file.••

> <span id="_bookmark17" class="anchor"></span>File List

## Files with Security Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DD RD WR DEL LAYGO

> NAME NUMBER ACCESS ACCESS ACCESS ACCESS ACCESS

<table style="width:100%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 14%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>- ENG INIT PARAMETERS</p>
</blockquote></th>
<th><blockquote>
<p>6910</p>
</blockquote></th>
<th colspan="2">#</th>
<th>e</th>
<th colspan="2"></th>
<th><blockquote>
<p>e</p>
</blockquote></th>
<th><blockquote>
<p>#</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENGINEERING COMPUTER</p>
</blockquote></td>
<td><blockquote>
<p>PORT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>6910.1</p>
</blockquote></td>
<td>#</td>
<td colspan="2"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENG SOFTWARE OPTIONS</p>
</blockquote></td>
<td>6910.2</td>
<td colspan="2">#</td>
<td>e</td>
<td colspan="2"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENG DJ SCREEN</p>
</blockquote></td>
<td>6910.9</td>
<td colspan="2">#</td>
<td>#</td>
<td colspan="2"></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EQUIPMENT CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>6911</p>
</blockquote></td>
<td colspan="2">#</td>
<td>e#</td>
<td colspan="2"></td>
<td><blockquote>
<p>e#</p>
</blockquote></td>
<td>e#</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MANUFACTURER LIST FILE</p>
</blockquote></td>
<td><blockquote>
<p>6912</p>
</blockquote></td>
<td colspan="2">#</td>
<td>e</td>
<td colspan="2"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EQUIPMENT INV.</p>
</blockquote></td>
<td><blockquote>
<p>6914</p>
</blockquote></td>
<td colspan="2">#</td>
<td>E</td>
<td colspan="2"></td>
<td><blockquote>
<p>#e</p>
</blockquote></td>
<td>#e</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CMR</p>
</blockquote></td>
<td>6914.1</td>
<td colspan="2">#</td>
<td>#e</td>
<td colspan="2"></td>
<td><blockquote>
<p>#e</p>
</blockquote></td>
<td>#e</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PM PROCEDURES</p>
</blockquote></td>
<td>6914.2</td>
<td colspan="2">#</td>
<td>E</td>
<td colspan="2"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BERS SURVEY</p>
</blockquote></td>
<td><blockquote>
<p>6916</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">e</td>
<td></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HAND RECEIPT TEXT</p>
</blockquote></td>
<td><blockquote>
<p>6916.2</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IT ASSIGNMENT</p>
</blockquote></td>
<td>6916.3</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CATEGORY STOCK NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>6917</p>
</blockquote></td>
<td>#</td>
<td></td>
<td>e</td>
<td></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENG ARCHIVE LOG</p>
</blockquote></td>
<td><blockquote>
<p>6919</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WORK ORDER #</p>
</blockquote></td>
<td><blockquote>
<p>6920</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td></td>
<td colspan="2">e</td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NEW WORK ACTION</p>
</blockquote></td>
<td>6920.1</td>
<td>#</td>
<td></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WORK CENTER CODE</p>
</blockquote></td>
<td><blockquote>
<p>6921</p>
</blockquote></td>
<td>#</td>
<td></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENGINEERING SECTION LIST</p>
</blockquote></td>
<td><blockquote>
<p>6922</p>
</blockquote></td>
<td>#</td>
<td>e</td>
<td></td>
<td>e</td>
<td colspan="2"></td>
<td><blockquote>
<p>e FSA-</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2162 REPORT</p>
</blockquote></td>
<td><blockquote>
<p>6924</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td>E</td>
<td></td>
<td>e</td>
<td colspan="2"></td>
<td><blockquote>
<p>E FSA-</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ACCIDENT ACTIVITY 6924.1 \# e e e FSA-ACCIDENT

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NATURE</p>
</blockquote></th>
<th></th>
<th colspan="5"><blockquote>
<p>6924.2 # e e e FSA-DIVISION/SERVICE</p>
</blockquote></th>
<th colspan="2">6924.3</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>e e CONSTRUCTION PROJECT 6925</p>
</blockquote></td>
<td colspan="2">#</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>e E</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>PROJECT STATUS</p>
</blockquote></td>
<td><blockquote>
<p>6925.2</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2">@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>EMPLOYEE(KEYS)</p>
</blockquote></td>
<td><blockquote>
<p>6926</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">E</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>LOCKS</p>
</blockquote></td>
<td><blockquote>
<p>6927</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">E</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ENG SPACE</p>
</blockquote></td>
<td><blockquote>
<p>6928</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2">E</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>ENG SPACE</p>
</blockquote></td>
<td><blockquote>
<p>FUNCTIONS</p>
</blockquote></td>
<td><blockquote>
<p>6928.1</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">e</td>
<td><blockquote>
<p>e</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ENG SPACE</p>
</blockquote></td>
<td><blockquote>
<p>UTILITIES</p>
</blockquote></td>
<td><blockquote>
<p>6928.2</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">e</td>
<td><blockquote>
<p>e</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>ENG BUILDING</p>
</blockquote></td>
<td><blockquote>
<p>6928.3</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>e</p>
</blockquote></td>
<td colspan="2">E</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ENG EMPLOYEE</p>
</blockquote></td>
<td><blockquote>
<p>6929</p>
</blockquote></td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>#e</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>#e</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>#e</p>
</blockquote></td>
<td><blockquote>
<p>#e</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>REGULATORY AGENCY</p>
</blockquote></td>
<td><blockquote>
<p>7335.7</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2">@</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>OFM SPACE CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>7336.3</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2">@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>OFM H089 CHAPTERS</p>
</blockquote></td>
<td><blockquote>
<p>7336.6</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>#e</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>#e</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>#e</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>OFM PROJ CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.8</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2">@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>OFM BUDGET CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>7336.9</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td colspan="2">@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nonexpendable Equipment Module

> The DHCP nonexpendable equipment file is contained within the Engineering package. Acquisition and Material Management Service personnel engaged in property management activities will need access to selected menu options within the Engineering namespace. Menu option ENMM MGR, Nonexpendable Equipment Module (A&MM), is intended to meet the needs of these users. Users of these options should hold the ENEDNX security key. Not all PPM employees will need to hold keys to all the sub-options contained in ENMM MGR so these options may also be assigned individually. Note that holding the ENEDNX key does not automatically give the menu options to the holder. The menus must be specifically assigned. Users of these options should refer to the documentation for the Equipment Management module.

> IT Equipment Module

> Patch EN\*7\*87 introduced a new top level menu designed for IT staff. The menu is IT Equipment Module \[ENIT MGR\]. Users can view and update the non- expendable equipment inventory for IT equipment. The menu also contains options to assign responsibility for IT equipment to individuals and monitor IT equipment. Users must hold the EN IT INVENTORY security key to access the Inventory Edit (IT) option. The EN IT ASSIGNMENT security key is required to create, transfer, and terminate assignments of responsibility for IT equipment. This key also provides access to the Add Entry to New Person File option. Other options on the menu, such as the reports, are not locked by a security key.

> Menu Structure

> ENGINEERING MAIN MENU

> WORK ORDER & MERS PROJECT PLANNING PROJECT TRACKING EQUIPMENT MANAGEMENT

> SPACE/FACILITY MANAGEMENT PROGRAM MANAGEMENT

> 2162 REPORT OF ACCIDENT

> ASSIGN (TRANSFER) ELECTRONIC WORK ORDERS

> WORK ORDER & MERS

> Enter New Work Order Edit Work Order Data Close Out Work Order Display Work Order

> Incomplete Work Order Status

> Incomplete Work Orders by Employee Incomplete Work Orders by Location Incomplete Work Orders by Shop

> Incomplete Work Orders by Owner/Department Transfer W.O. to Another Shop

> Print Equip. History by Entry Number Disapprove Work Order

> Reprint Work Orders (All Shops) Print PM Manhours

Exported Options

> PROJECT PLANNING

> 5 Yr Plan Project E/E

> Project Application E/E (VAF 10-1193) Environmental Analysis E/E (VAF 10-1193a) Activations E/E

> Report/Print Menu

> Minor/Minor Misc Prioritization NRM Prioritization Scoring Sheet

> Environmental Analysis VAF 10-1193a Project Application VAF 10-1193

> 5 Yr Plan Report Approval of Project Application Electronic Transmission Menu

> Batch Transmit 5-Yr Plan Projects Individual 5-Yr Plan Project Transmission Project Application Send

> PROJECT TRACKING

> Enter Project Data Screen Review All Data

> Preliminary Data Enter/Edit Approved Dates Screen Edit Revised Dates Screen Edit Actual Dates Screen Edit A/E Data Screen Edit Contractor Data Screen Edit

> Changes & Remarks Screen Edit Print Project Status Report Print All Project Status Reports Transmit 10-0051 Electronically

Exported Options

> EQUIPMENT MANAGEMENT

> New Inventory Entry Multiple Inventory Entry Inventory Edit

> Display Equipment Record Equipment Reports ...

> Specific Equipment History Equipment Category History Inventory Listing ...

> CMR Inventory (EIL) Equipment Category Inventory Location Inventory

> Using Service Inventory Responsible Shop Inventory Use Status Inventory

> Warranty List Replacement Listing Failure Rate Report PM Workload Analysis

> Direct Posting to Equipment Histories PM Parameters ...

> Display Specific Device PM Schedule Display Equipment Category PM Schedule Print PM Procedure

> Enter/Edit Specific Device PM Schedule Enter/Edit Equipment Category PM Schedule Enter/Edit PM Procedure

> Generate PM Schedule ...

> Monthly PM List Weekly PM List

> Delete PM Work Orders

> EQUIPMENT MANAGEMENT, continued

> Record Equipment PMI ...

> Close Out PM Work Orders

> Rapid Closeout of PM Work Orders Record Single Device PMI

> Bar Coded PMI Functions ...

> Download PM Program to Portable Bar Code Reader Upload Data From Portable Bar Code Reader Restart Processing of Bar Coded PMI

> Upload Data from MedTester Rapid Deferral of PM Worklist Print PM Manhours

> Print Bar Code Labels for Equipment Management ...

> Equipment Labels ...

> Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

> Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

> Equipment Labels by Equipment ID#

> Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

> Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

Exported Options

> EQUIPMENT MANAGEMENT, continued

> Location Labels ...

> WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

> ALL Bar Coded Location Labels

> Bar Coded Equipment Inventory Management ...

> Download NX Program to Portable Bar Code Reader Upload Data From Portable Bar Code Reader Inventory Exception Listing

> Manual Update of Equipment Inventory

> Restart Processing of Uploaded NX Inventory Data

> NONEXPENDABLEEQUIPMENT

> Equipment Enter/Edit (NX) ...

> New Inventory Entry Inventory Edit

> Display Equipment Record Multiple Inventory Entry

> Manual Update of Equipment Inventory Equipment Management Reports (NX) ...

> Specific Equipment History CMR Inventory (EIL) Warranty List Replacement Listing Location Inventory

> Using Service Inventory Use Status Inventory

> Bar Code Features (NX Equipment) ...

> Equipment Labels ...

> Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

> Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

> Equipment Labels by Equipment ID#

> Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

> Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

Exported Options

> NONEXPENDABLE EQUIPMENT, continued

> Location Labels ...

> WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

> ALL Bar Coded Location Labels Bar Code Features

> Download NX Program to Portable Bar Code Reader Upload Data From Portable Bar Code Reader Restart Processing of Uploaded NX Inventory Data Inventory Exception Listing

> NX (Nonexpendable Equipment) Utilities ...

> CMR File Enter/Edit

> Category Stock Number Enter/Edit

> PROGRAM MANAGEMENT

> Engineering Computer Port Section List

> Work Center Code Engineering Employee File

> Enter/Edit Equipment Category PM Schedule Manufacturer

> ENG SITE PARAMETERS Enter/Edit

> SOFTWARE OPTIONS Enter/Edit Engineering Archive Module

> Find & Assemble Records Archive & Verify Records Delete Archive Global Recall Archive Global Review Activity Log

> Biomedical Engineering Resource Survey Entering Data into the BERS Survey File Print Personnel Survey Listing

> Print Contract Survey Listing Print General Survey Listing Print Additional Survey Listing

> Work Action

Exported Options

> SPACE/FACILITY MANAGEMENT

> Space Management ...

> Enter New Room Space Data Display/Edit Room Data

> Finish Replacement Schedules Report Menu ... Replacement Schedule for All Finishes Ceiling Replacement Schedule

> Wall Replacement Schedule Floor Replacement Schedule Space Survey Report Menu ...

> Room/Keying/Function Report Space Survey by Room Service Space Survey Function Space Survey Building Space Survey

> RCS 10-0141 Report

> Building Management RCS 10-203, VAF 10-6007a Non-Space File Location Report

> Key/Lock Management ...

> Key Distribution by Employee Enter/Edit Lock Number File Enter/Edit

> Print Key Distribution By Employee Print Employee List sorted by Key Print Employee List by Service

> Export Facility Management Data ...

> Output Service/NSF spreadsheet Output Function/NSF Spreadsheet Output RCS 10-0141 spreadsheet

> SPACE/FACILITY MANAGEMENT, continued

> Facility Management Utilities ... Edit Space Functions file Edit Space Utilities file

> Remove Dangling Pointers in Lock file Building File Enter/Edit

> Print All Building Data Leased Space Options ...

> Enter/Edit All Lease Fields (BUILDING FILE) Enter/Edit Lease Vendor (BUILDING FILE) Print Leased Space Survey

> Planning Space Program Menu ...

> Building File Enter/Edit Enter/Edit Room Planning Data Print Building/Project Space Plan

> 2162 REPORT OF ACCIDENT

> Enter 2162 Report

> Display 2162 Report

> Edit 2162 Report

> Service/Division Summary Report Injury Cause Summary Report Accident Nature Summary Report Specific Location Summary Report

> ASSIGN (TRANSFER) ELECTRONIC WORK ORDERS

Exported Options

> IT EQUIPMENT MODULE (ENIT MGR)

> Inventory Edit (IT) Display Equipment Record

> Bar Code Features (NX Equipment) ...

> Equipment Labels ...

> Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

> Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

> Equipment Labels by Equipment ID#

> Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

> Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

> Location Labels ...

> WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

> ALL Bar Coded Location Labels

> Download NX Program to Portable Bar Code Reader Upload Data From Portable Bar Code Reader Restart Processing of Uploaded NX Inventory Data Inventory Exception Listing

> Specific Equipment History Display/Edit Room Data

> Non-Space File Location Report

> IT EQUIPMENT MODULE (ENIT MGR) , continued

> IT Equipment Responsibility ...

> Assign Responsibility Terminate Responsibility Transfer Responsibility Certify Hard Copy Signature

> Print Hand Receipt for an Individual Add Entry to New Person File

> IT Equipment Report Menu ...

> Individual Responsibility for IT Assets Report Unassigned IT Asset Report

> Assignments Pending Acceptance Report Tracked IT Assets Report

> Signature Exception Report Assignment Inquiry

> IT OWNER MENU

> Accept IT Responsibility

> Individual Responsibility for IT Assets Report Print My Hand Receipt

> Assignment Inquiry

> FILES POINTING TO FILE 7336.9, OFM BUDGET CATEGORY• FILE NO. FILE NAME FIELD NO. FIELD NAME (SUBFIELD)•

> 6925 CONSTRUCTION PROJECT 158.2 BUDGET CATEGORY

> 7336.8 OFM PROJ CATEGORY 8 MA BUDGET CATEGORY•

> NOTE) This file does not currently point to any other file.••

Exported Options

> Exported Options

> Option List

> NAME: ENACTUAL MENU TEXT: Actual Dates Screen Edit TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit actual milestone dates on Construction Project(s). ROUTINE: PROJ6^ENPROJ

> UPPERCASE MENU TEXT: ACTUAL DATES SCREEN EDIT

> NAME: ENAE MENU TEXT: A/E Data Screen Edit TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit basic information on architectural firms retained by facility for specific projects.

> ROUTINE: PROJ7^ENPROJ

> UPPERCASE MENU TEXT: A/E DATA SCREEN EDIT

> NAME: ENAPPROV MENU TEXT: Approved Dates Screen Edit TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit 'approved' dates on delegated projects. Approved dates indicate when certain project milestones were originally scheduled. Adherence to these dates is usually important in terms of keeping obligations consistent with an established spending plan.

> ROUTINE: PROJ4^ENPROJ

> UPPERCASE MENU TEXT: APPROVED DATES SCREEN EDIT

> NAME: ENAR MENU TEXT: Engineering Archive Module TYPE: menu CREATOR: 187

> DESCRIPTION: The Engineering Archive module presently services the Work Order and 2162 Accident Report files. It allows individual records to be stored on tape and purged from the disk.

> ITEM: ENAR-ASSEMBLE SYNONYM: 1

> ITEM: ENAR-ARCHIVE SYNONYM: 2

> ITEM: ENAR-DELETE SYNONYM: 3

> ITEM: ENAR-RECALL SYNONYM: 4

> ITEM: ENAR-LOG SYNONYM: 5

> EXIT ACTION: D OUT^ENAR TIMESTAMP: 55586,57291 UPPERCASE MENU TEXT: ENGINEERING ARCHIVE MODULE

> NAME: ENAR-ARCHIVE MENU TEXT: Archive & Verify Records TYPE: run routine CREATOR: 187

> DESCRIPTION: Moves a collection of records (archive set) from the archive global to tape. This function should be executed immediately after "Find and Assemble Records".

> ROUTINE: A^ENAR

> UPPERCASE MENU TEXT: ARCHIVE & VERIFY RECORDS

> NAME: ENAR-ASSEMBLE MENU TEXT: Find & Assemble Records TYPE: run routine CREATOR: 187

> DESCRIPTION: Searches the database and finds the individual records to be archived, after which it moves them to an archive global and simultaneously purges them from disk. The user is asked for record type, station number, and sort parameters. Records may be archived for an entire fiscal year, or a specific quarter. Completed work orders may be archived by shop (all shops, one shop, or all shops but one). Since this function actually purges data from disk, you should backup your system before executing "Find and Assemble Records". Users should be kept off the system until "Find and Assemble" and "Archive and Verify" have run to completion.

> ROUTINE: G^ENAR

> UPPERCASE MENU TEXT: FIND & ASSEMBLE RECORDS

> NAME: ENAR-DELETE MENU TEXT: Delete Archive Global TYPE: run routine CREATOR: 187

> DESCRIPTION: Kills the archive global, which may be thought of as a temporary storage area. The archive global holds records in the process of being archived, as

> Exported Options

> well as records which have been recalled from an archive tape for inspection via File Manager. "Delete Archive Global" should be executed after "Archive and Verify" and after "Recall Archive Global" (once the recalled records have been inspected and/or printed).

> ROUTINE: D^ENAR

> UPPERCASE MENU TEXT: DELETE ARCHIVE GLOBAL

> NAME: ENAR-LOG MENU TEXT: Review Activity Log TYPE: run routine CREATOR: 187

> DESCRIPTION: Displays a chronological listing of everything that has been done with a given archive set.

> ROUTINE: L^ENAR UPPERCASE MENU TEXT: REVIEW ACTIVITY LOG

> NAME: ENAR-RECALL MENU TEXT: Recall Archive Global TYPE: run routine CREATOR: 187

> DESCRIPTION: Restores records from an archive tape into the archive global, where they may be examined via File Manager. User may recall an entire tape or search a tape for a specific record.

> ROUTINE: R^ENAR

> UPPERCASE MENU TEXT: RECALL ARCHIVE GLOBAL

> NAME: ENBCEE ALL

> MENU TEXT: Equipment Labels by Equipment ID# TYPE:

> run routine CREATOR: 187

> DESCRIPTION: Prints bar coded equipment labels for each and every entry in the Equipment file.

> ROUTINE: ALL^ENLBL5

> UPPERCASE MENU TEXT: EQUIPMENT LABELS BY EQUIPMENT

> NAME: ENBCEE CAT

> MENU TEXT: Equipment Category Bar Code Labels TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar coded equipment labels for all pieces of equipment in specified category.

> ROUTINE: CAT^ENLBL3

> UPPERCASE MENU TEXT: EQUIPMENT CATEGORY BAR CODE LA

> NAME: ENBCEE CMR

> MENU TEXT: CMR Bar Code Labels (EQUIPMENT)

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code labels for all equipment on a specified CMR. ROUTINE: CMR^ENLBL5

> UPPERCASE MENU TEXT: CMR BAR CODE LABELS (EQUIPMENT

> NAME: ENBCEE LID MENU TEXT: Bar Code Labels by LOCAL ID

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints EQUIPMENT LABEL's for a range of LOCAL IDENTIFIERS. ROUTINE: LOCID^ENLBL15

> UPPERCASE MENU TEXT: BAR CODE LABELS BY LOCAL ID

> Exported Options

> NAME: ENBCEE PM MENU TEXT: Bar Code Labels by PM Number TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar coded equipment labels for a specified range of Property Management numbers.

> ROUTINE: PM^ENLBL10

> UPPERCASE MENU TEXT: BAR CODE LABELS BY PM NUMBER

> NAME: ENBCEE PMLIST

> MENU TEXT: Bar Code Labels in Conjunction with PM Worklist TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar coded equipment labels for each piece of equipment on a monthly PM worklist. User specifies the worklist by responding to prompts for date (month and year only) and shop.

> ROUTINE: WRKLST^ENLBL11

> UPPERCASE MENU TEXT: BAR CODE LABELS IN CONJUNCTION

> NAME: ENBCEE PO

> MENU TEXT: Bar Code Labels for a Purchase Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints a bar coded EQUIPMENT LABEL for each item on a specific purchase order.

> ROUTINE: PO^ENLBL12

> UPPERCASE MENU TEXT: BAR CODE LABELS FOR A PURCHASE

> NAME: ENBCEE RM

> MENU TEXT: Bar Code Labels by Specific Location (ROOM) TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code labels for each piece of equipment in a specified room. Sites must be using the Space file (#6928) in order to profit from using this option.

> ROUTINE: RM^ENLBL6

> UPPERCASE MENU TEXT: BAR CODE LABELS BY SPECIFIC LO

> NAME: ENBCEE SD MENU TEXT: Single Device Bar Code Label TYPE: run routine CREATOR: 187

> DESCRIPTION: Print bar code label for one specific piece of equipment. ROUTINE: SD^ENLBL3

> UPPERCASE MENU TEXT: SINGLE DEVICE BAR CODE LABEL

> NAME: ENBCEE SRVC

> MENU TEXT: Bar Code Labels by Using Service

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar coded EQUIPMENT LABEL's for all devices that are identified in the Equipment file as belonging to a particular SERVICE.

> ROUTINE: SRVC^ENLBL12

> UPPERCASE MENU TEXT: BAR CODE LABELS BY USING SERVI

> NAME: ENBCEE WING

> MENU TEXT: Bar Code Labels by General Location (WING) TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code labels for each piece of equipment located on a specified WING, where WING is taken from the Space file (#6928).

> ROUTINE: WING^ENLBL6

> UPPERCASE MENU TEXT: BAR CODE LABELS BY GENERAL LOC

> Exported Options

> NAME: ENBCLBL MGR

> MENU TEXT: Print Bar Code Labels for Equipment Management TYPE: menu CREATOR: 187

> DESCRIPTION: Generates bar code labels (location labels and equipment labels) for equipment management applications. Designed for use with a dedicated bar code printer. ITEM: ENBCLBLEE SYNONYM: 1

> ITEM: ENBCLBLSP SYNONYM: 2

> TIMESTAMP: 55586,57318

> UPPERCASE MENU TEXT: PRINT BAR CODE LABELS FOR EQUI

> NAME: ENBCLBLEE MENU TEXT: Equipment Labels TYPE: menu CREATOR: 187

> DESCRIPTION: Prints bar coded equipment labels. Cohorts of labels (ex: labels by CMR, labels by Equipment Category, etc.) will be sorted by LOCATION

> unless the user specifies otherwise.

> ITEM: ENBCEE CAT SYNONYM: 1

> ITEM: ENBCEE CMR SYNONYM: 2

> ITEM: ENBCEE PM SYNONYM: 3

> ITEM: ENBCEE WING SYNONYM: 4

> ITEM: ENBCEE RM SYNONYM: 5

> ITEM: ENBCEE SD SYNONYM: 6

> ITEM: ENBCEE ALL SYNONYM: 7

> ITEM: ENBCEE PMLIST SYNONYM: 8

> ITEM: ENBCEE PO SYNONYM: 9

> ITEM: ENBCEE LID SYNONYM: 10

> ITEM: ENBCEE SRVC SYNONYM: 11

> TIMESTAMP: 55586,57336 UPPERCASE MENU TEXT: EQUIPMENT LABELS

> NAME: ENBCLBLSP MENU TEXT: Location Labels TYPE: menu CREATOR: 187

> DESCRIPTION: Driver option to print bar coded location labels. ITEM: ENBCSP WING SYNONYM: 1

> ITEM: ENBCSP BLDG SYNONYM: 2

> ITEM: ENBCSP RM SYNONYM: 3

> ITEM: ENBCSP ALL SYNONYM: 4

> TIMESTAMP: 55586,57312 UPPERCASE MENU TEXT: LOCATION LABELS

> NAME: ENBCNX MGR

> MENU TEXT: Bar Coded Equipment Inventory Management TYPE: menu CREATOR: 187

> DESCRIPTION: Driver for NX inventory functions. ITEM: ENBCNXDNLD SYNONYM: 1

> ITEM: ENBCUPLD SYNONYM: 2

> ITEM: ENBCNXCMR SYNONYM: 3

> ITEM: ENBCNXMAN SYNONYM: 4

> ITEM: ENBCNXRES SYNONYM: 5

> TIMESTAMP: 55586,57321

> UPPERCASE MENU TEXT: BAR CODED EQUIPMENT INVENTORY

> NAME: ENBCNXCMR MENU TEXT: Inventory Exception Listing TYPE: run routine CREATOR: 187

> DESCRIPTION: Produces a list of those items on a specified CMR that have not been located in the course of a physical inventory.

> ROUTINE: EN^ENEQNX4

> UPPERCASE MENU TEXT: INVENTORY EXCEPTION LISTING

> Exported Options

> NAME: ENBCNXDNLD

> MENU TEXT: Download NX Program to Portable Bar Code Reader TYPE: action CREATOR: 187

> DESCRIPTION: Downloads an IRL (Interactive Reader Language) program to a portable bar code reader.

> ENTRY ACTION: I \$D(^DIC(6910,1,0)) S ENSTA=""""\_\$P(^(0),U,2)\_"""",ENCTID="ENNX " D ^ENCTBAR

> UPPERCASE MENU TEXT: DOWNLOAD NX PROGRAM TO PORTABL

> NAME: ENBCNXMAN

> MENU TEXT: Manual Update of Equipment Inventory TYPE: run routine CREATOR: 187

> DESCRIPTION: Uses FileMan to update physical inventory data on individual entries in the Equipment file.

> ROUTINE: EN^ENEQNX5

> UPPERCASE MENU TEXT: MANUAL UPDATE OF EQUIPMENT INV

> NAME: ENBCNXRES

> MENU TEXT: Restart Processing of Uploaded NX Inventory Data TYPE: run routine CREATOR: 187

> DESCRIPTION: Used to resume processing of NX inventory that has been

> uploaded from a portable bar code reader. User will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload must be re• started from the beginning.

> ROUTINE: RES^ENEQNX1

> UPPERCASE MENU TEXT: RESTART PROCESSING OF UPLOADED

> NAME: ENBCPM MGR MENU TEXT: Bar Coded PMI Functions TYPE: menu CREATOR: 187

> DESCRIPTION: Driver for bar coded Preventive Maintenance functions. Will prompt you to either (1) download a data acquisition program to a bar code reader, (2) upload collected data from a bar code reader, or (3) restart processing of a previously uploaded data set.

> ITEM: ENBCPMDNLD SYNONYM: 1

> ITEM: ENBCUPLD SYNONYM: 2

> ITEM: ENBCPMRES SYNONYM: 3

> TIMESTAMP: 55586,57323

> UPPERCASE MENU TEXT: BAR CODED PMI FUNCTIONS

> NAME: ENBCPMDNLD

> MENU TEXT: Download PM Program to Portable Bar Code Reader TYPE: action CREATOR: 187

> DESCRIPTION: Downloads an IRL (Interactive Reader Language) program to a portable bar code reader. The IRL program records PM inspections.

> ENTRY ACTION: I \$D(^DIC(6910,1,0)) S ENSTA=""""\_\$P(^(0),U,2)\_"""",ENCTID="ENPM " D DNLD^ENBCPM1

> UPPERCASE MENU TEXT: DOWNLOAD PM PROGRAM TO PORTABL

> NAME: ENBCPMRES

> MENU TEXT: Restart Processing of Bar Coded PMI TYPE: run routine CREATOR: 187

> DESCRIPTION: Used to resume processing of PMI list that has been uploaded from a portable bar code reader. User will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload must be re-started from the beginning.

> ROUTINE: RES^ENBCPM1

> UPPERCASE MENU TEXT: RESTART PROCESSING OF BAR CODE

> Exported Options

> NAME: ENBCSP ALL MENU TEXT: ALL Bar Coded Location Labels TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code labels for all entries in the Space file (#6928). ROUTINE: ALL^ENLBL4

> UPPERCASE MENU TEXT: ALL BAR CODED LOCATION LABELS

> NAME: ENBCSP BLDG MENU TEXT: BUILDING Bar Code Labels

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code LOCATION LABELS for all rooms in a specified BUILDING, where BUILDING is taken to be the second piece (with '-' as delimiter) of the NAME field from the Space file (#6928).

> ROUTINE: BLDG^ENLBL4

> UPPERCASE MENU TEXT: BUILDING BAR CODE LABELS

> NAME: ENBCSP RM MENU TEXT: ROOM Bar Code Label

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code label for specified room. Room in question must first exist in the Space file (#6928).

> ROUTINE: RM^ENLBL4 UPPERCASE MENU TEXT: ROOM BAR CODE LABEL

> NAME: ENBCSP WING MENU TEXT: WING Bar Code Labels

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints bar code LOCATION LABELS for all rooms in a specified WING, where WING is as defined in the Space file (#6928).

> ROUTINE: WING^ENLBL4

> UPPERCASE MENU TEXT: WING BAR CODE LABELS

> NAME: ENBCUPLD

> MENU TEXT: Upload Data From Portable Bar Code Reader TYPE: run routine CREATOR: 187

> DESCRIPTION: Calls a routine that causes a portable bar code reader to upload its data to DHCP.

> ROUTINE: ENCTREAD

> UPPERCASE MENU TEXT: UPLOAD DATA FROM PORTABLE BAR

> NAME: ENCCLERK MENU TEXT: Engineering Cost Control Clerk Main Menu

> TYPE: menu CREATOR: 187

> DESCRIPTION: This Menu is set up for the Cost Account Clerk. Sites will probably want to add selected IFCAP options to this 'menu' item.

> ITEM: ENPROJ SYNONYM: 1

> ITEM: DIUSER SYNONYM: 2

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55586,57262 TIMESTAMP OF PRIMARY MENU: 53512,52393 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENCHANGES MENU TEXT: Changes & Remarks Screen Edit TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit summary of change orders and narrative remarks. ROUTINE: PROJ8^ENPROJ

> UPPERCASE MENU TEXT: CHANGES & REMARKS SCREEN EDIT

> Exported Options

> NAME: ENCMR MENU TEXT: CMR File Enter/Edit TYPE: edit CREATOR: 187

> LOCK: ENEDNX

> DESCRIPTION: For maintaining the list of CMR (Consolidated Memoranda of Receipt) in use at your facility. This option is usually held by your PPM Chief and/or his designee.

> DIC {DIC}: ENG(6914.1, DIC(0): AEQLM

> DIE: ENG(6914.1, DR {DIE}: .01:99 UPPERCASE MENU TEXT: CMR FILE ENTER/EDIT

> NAME: ENCONTR MENU TEXT: Contractor Data Screen Edit TYPE: run routine CREATOR: HEIBY,D

> DESCRIPTION: Enter/edit basic information on prime construction contractor for a delegated project.

> ROUTINE: PROJC^ENPROJ

> UPPERCASE MENU TEXT: CONTRACTOR DATA SCREEN EDIT

> NAME: ENCSN

> MENU TEXT: Category Stock Number Enter/Edit

> TYPE: edit CREATOR: 187

> LOCK: ENEDNX

> DESCRIPTION: Intended for maintenance of Category Stock Number file. This option should be held by no more than one or two persons at each site, at the discretion of A&MM.

> DIC {DIC}: ENCSN(6917, DIC(0): AEMQL

> DIE: ENCSN(6917, DR {DIE}: \[ENCSN\] UPPERCASE MENU TEXT: CATEGORY STOCK NUMBER ENTER/ED

> NAME: ENDSY MENU TEXT: Display Work Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Display existing work request in a screen format. Facility exists for editing work order once it has been displayed.

> ROUTINE: DSY^ENWO1 UPPERCASE MENU TEXT: DISPLAY WORK ORDER

> NAME: ENEMP MENU TEXT: Engineering Employee File TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit Engineering Employee file. File should contain entries for all personnel who may be wholly or partially responsible for completing work requests.

> ROUTINE: EMP^ENMAN

> UPPERCASE MENU TEXT: ENGINEERING EMPLOYEE FILE

> NAME: ENENT MENU TEXT: Edit Work Order Data TYPE: run routine CREATOR: 187

> DESCRIPTION: Edit work request in line by line FileMan mode. ROUTINE: ENT^ENWO1

> UPPERCASE MENU TEXT: EDIT WORK ORDER DATA

> NAME: ENEQ-FAILURE MENU TEXT: Failure Rate Report TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints a synopsis of the repair history of user specified device types.

> ROUTINE: F1^ENEQRP3 UPPERCASE MENU TEXT: FAILURE RATE REPORT

> Exported Options

> NAME: ENEQ-INVENTORY MENU TEXT: Inventory Listing TYPE: menu CREATOR: 187

> DESCRIPTION: Contains options to print data from the EQUIPMENT INV. File (#6914). ITEM: ENEQINV1 SYNONYM: 1

> ITEM: ENEQINV2 SYNONYM: 2

> ITEM: ENEQINV3 SYNONYM: 3

> ITEM: ENEQINV4 SYNONYM: 4

> ITEM: ENEQINV5 SYNONYM: 5

> ITEM: ENEQINV6 SYNONYM: 6

> ENTRY ACTION: D HDR^ENEQRPI TIMESTAMP: 55586,57301 UPPERCASE MENU TEXT: INVENTORY LISTING

> NAME: ENEQ-PLANNER MENU TEXT: PM Workload Analysis TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints a breakdown of scheduled PMI hours by month for a given shop. Intended as a tool in balancing PM workload.

> UPPERCASE MENU TEXT: PM WORKLOAD ANALYSIS

> NAME: ENEQ-REPLACE MENU TEXT: Replacement Listing TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints all entries in the EQUIPMENT INV. file scheduled for replacement within a user specified time interval.

> ROUTINE: R^ENEQRP1 UPPERCASE MENU TEXT: REPLACEMENT LISTING

> NAME: ENEQ-REPORTS MENU TEXT: Equipment Reports TYPE: menu CREATOR: 187

> DESCRIPTION: Contains options to print data from the EQUIPMENT INV. file (#6914).

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 27%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ITEM: ENIN-HIST-SPECIFIC</p>
</blockquote></th>
<th>SYNONYM: 1</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENIN-HIST-GENERIC</p>
</blockquote></td>
<td>SYNONYM: 2</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENEQ-INVENTORY</p>
</blockquote></td>
<td>SYNONYM: 3</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENEQ-WARRANTY</p>
</blockquote></td>
<td>SYNONYM: 4</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENEQ-REPLACE</p>
</blockquote></td>
<td>SYNONYM: 5</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENEQ-FAILURE</p>
</blockquote></td>
<td>SYNONYM: 6</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENEQ-PLANNER</p>
</blockquote></td>
<td>SYNONYM: 7</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENEQPOST</p>
</blockquote></td>
<td>SYNONYM: 8</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENTRY ACTION: D HDR^ENEQRP</p>
</blockquote></td>
<td>TIMESTAMP:</td>
<td><blockquote>
<p>55613,31339</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UPPERCASE MENU TEXT: EQUIPMENT</p>
</blockquote></td>
<td><blockquote>
<p>REPORTS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> NAME: ENEQ-WARRANTY MENU TEXT: Warranty List

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Prints all devices whose warranties are scheduled to expire within a user specified time interval.

> ROUTINE: W^ENEQRP1 UPPERCASE MENU TEXT: WARRANTY LIST

> NAME: ENEQHID

> MENU TEXT: Print Equip. History by Entry Number TYPE: run routine CREATOR: 187

> DESCRIPTION: Print summary of work orders against an individual equipment record. No restrictions as to how equipment look-up is performed.

> ROUTINE: EQHI^ENWO1

> UPPERCASE MENU TEXT: PRINT EQUIP. HISTORY BY ENTRY

> Exported Options

> NAME: ENEQINV1 MENU TEXT: CMR Inventory

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Inventory listing by CMR. Produces a document suitable for signature of Responsible Official.

> ROUTINE: CMR^ENEQRPI UPPERCASE MENU TEXT: CMR INVENTORY

> NAME: ENEQINV2 MENU TEXT: Equipment Category Inventory TYPE: run routine CREATOR: 187

> DESCRIPTION: Inventory listing by device type (c.f., File 6911). ROUTINE: DTYP^ENEQRPI

> UPPERCASE MENU TEXT: EQUIPMENT CATEGORY INVENTORY

> NAME: ENEQINV3 MENU TEXT: Location Inventory TYPE: run routine CREATOR: 187

DESCRIPTION: Inventory listing by device location.

> ROUTINE: LOC^ENEQRPI UPPERCASE MENU TEXT: LOCATION INVENTORY

> NAME: ENEQINV4 MENU TEXT: Using Service Inventory TYPE: run routine CREATOR: 187

> DESCRIPTION: Inventory listing by using service. Note that the using service is not necessarily the owning service (ex: a VCR may be used in Dental but owned by Medical Media Production). Owning service is established via the CMR.

> ROUTINE: SRV^ENEQRPI

> UPPERCASE MENU TEXT: USING SERVICE INVENTORY

> NAME: ENEQINV5 MENU TEXT: Responsible Shop Inventory TYPE: run routine CREATOR: 187

> DESCRIPTION: Inventory listing by responsible shop. ROUTINE: SHOP^ENEQRPI

> UPPERCASE MENU TEXT: RESPONSIBLE SHOP INVENTORY

> NAME: ENEQINV6 MENU TEXT: Use Status Inventory TYPE: run routine CREATOR: 187

> DESCRIPTION: Inventory listing by use status. ROUTINE: STUS^ENEQRPI

> UPPERCASE MENU TEXT: USE STATUS INVENTORY

> NAME: ENEQPOST

> MENU TEXT: Direct Posting to Equipment Histories TYPE: run routine CREATOR: HEIBY,D

> DESCRIPTION: A utility for posting activities to Equipment Histories without going thru the Work Order module.

> ROUTINE: EN^ENEQP

> UPPERCASE MENU TEXT: DIRECT POSTING TO EQUIPMENT HI

> NAME: ENETRANSFER

> MENU TEXT: Assign (Transfer) Electronic Work Orders TYPE: run routine CREATOR: 187

> DESCRIPTION: Used to transfer work orders entered via CRT by non-Engineering personnel from a 'receiving area' (essentially a fictitious shop) to a working shop.

> ROUTINE: ENETRAN

> UPPERCASE MENU TEXT: ASSIGN (TRANSFER) ELECTRONIC W

> Exported Options

> NAME: ENEUSER1 MENU TEXT: Equipment Management TYPE: menu CREATOR: 187

> DESCRIPTION: Gives access to the Preventive Maintenance module. ITEM: ENPM SYNONYM: 1

> ITEM: ENPMS SYNONYM: 2

> ITEM: ENPMR SYNONYM: 3

> ENTRY ACTION: D HDR^ENEQ TIMESTAMP: 55586,57295 TIMESTAMP OF PRIMARY MENU: 53920,41795

> UPPERCASE MENU TEXT: EQUIPMENT MANAGEMENT

> NAME: ENFS-2162 MENU TEXT: 2162 Report of Accident TYPE: menu CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - FORM 2162 ITEM: ENFS-2162-ENTER SYNONYM: 1

> ITEM: ENFS-2162-DISPLAY SYNONYM: 2

> ITEM: ENFS-2162-EDIT SYNONYM: 3 ITEM: ENFS-2162-SERVICE SUMMARY SYNONYM: 4 ITEM: ENFS-2162-INJURY SUMMARY SYNONYM: 5 ITEM: ENFS-2162-ACC. NATURE SUMMARY SYNONYM: 6 ITEM: ENFS-2162-LOCATION SUMMARY SYNONYM: 7

> ENTRY ACTION: D INIT^ENFSA,HDR^ENFSA TIMESTAMP: 55586,57271 UPPERCASE MENU TEXT: 2162 REPORT OF ACCIDENT

> NAME: ENFS-2162-ACC. NATURE SUMMARY

> MENU TEXT: Accident Nature Summary Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - FM 2162 REPORT BY ACCIDENT NATURE

> ROUTINE: P30^ENFSA1

> UPPERCASE MENU TEXT: ACCIDENT NATURE SUMMARY REPORT

> NAME: ENFS-2162-DISPLAY MENU TEXT: Display 2162 Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - DISPLAY 2162 REPORT ROUTINE: R3^ENFSA UPPERCASE MENU TEXT: DISPLAY 2162 REPORT

> NAME: ENFS-2162-EDIT MENU TEXT: Edit 2162 Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - EDIT 2162 REPORT ROUTINE: R2^ENFSA UPPERCASE MENU TEXT: EDIT 2162 REPORT

> NAME: ENFS-2162-ENTER MENU TEXT: Enter 2162 Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - ENTER 2162 REPORT ROUTINE: R1^ENFSA UPPERCASE MENU TEXT: ENTER 2162 REPORT

> NAME: ENFS-2162-INJURY SUMMARY MENU TEXT: Injury Cause Summary Report TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - FM 2162 REPORT BY INJURY CAUSE ROUTINE: P20^ENFSA1

> UPPERCASE MENU TEXT: INJURY CAUSE SUMMARY REPORT

> Exported Options

> NAME: ENFS-2162-LOCATION SUMMARY

> MENU TEXT: Specific Location Summary Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - FM 2162 REPORT BY LOCATION ROUTINE: P40^ENFSA1

> UPPERCASE MENU TEXT: SPECIFIC LOCATION SUMMARY REPO

> NAME: ENFS-2162-SERVICE SUMMARY

> MENU TEXT: Service/Division Summary Report

> TYPE: run routine CREATOR: 187

> DESCRIPTION: ENGINEERING ACCIDENT REPORTING MODULE - FM 2162 REPORT BY SERVICE ROUTINE: P10^ENFSA1

> UPPERCASE MENU TEXT: SERVICE/DIVISION SUMMARY REPOR

> NAME: ENGSADDPRT1

> MENU TEXT: Print Additional Survey Listing

> TYPE: print CREATOR: 187

> DESCRIPTION: Print 'Additional Support Areas' listing from Biomedical Engineering Resources Survey (BERS) file.

> DIC {DIP}: ENGS(6916, PG: 1

> L.: 0 FLDS: \[ENGSADDITIONAL\]

> UPPERCASE MENU TEXT: PRINT ADDITIONAL SURVEY LISTIN

> NAME: ENGSCONPRT1 MENU TEXT: Print Contract Survey Listing TYPE: print CREATOR: 187

> DESCRIPTION: Print information on equipment service contracts from the Biomedical Engineering Resources Survey (BERS) file.

> DIC {DIP}: ENGS(6916, PG: 1

> L.: 0 FLDS: \[ENGSCONTRACT\]

> UPPERCASE MENU TEXT: PRINT CONTRACT SURVEY LISTING

> NAME: ENGSGENPRT1 MENU TEXT: Print General Survey Listing TYPE: print CREATOR: 187

> DESCRIPTION: Print general information from the Biomedical Engineering Resources Survey (BERS) file.

> DIC {DIP}: ENGS(6916, PG: 1

> L.: 0 FLDS: \[ENGSGENERAL\]

> UPPERCASE MENU TEXT: PRINT GENERAL SURVEY LISTING

> NAME: ENGSMENU

> MENU TEXT: Biomedical Engineering Resource Survey TYPE: menu CREATOR: 187

> DESCRIPTION: Driver option for Biomedical Engineering Resources Survey module. This module collects data on how individual facilities maintain their biomedical equipment and instrumentation. Data from all sites is aggregated once a year by the Engineering Service Center in St. Louis.

> UPPERCASE MENU TEXT: BIOMEDICAL ENGINEERING RESOURC NAME: ENGSSURPRT1

> MENU TEXT: Print Personnel Survey Listing

> TYPE: print CREATOR: 187

> DESCRIPTION: Print Engineering personnel data from the Biomedical Engineering Resources Survey (BERS) file.

> DIC {DIP}: ENGS(6916, PG: 1

Exported Options

> L.: 0 FLDS: \[ENGSPERSONNEL\]

> UPPERCASE MENU TEXT: PRINT PERSONNEL SURVEY LISTING

> NAME: ENGSSURVEYINPUT

> MENU TEXT: Entering Data into the BERS Survey File TYPE: edit CREATOR:

> DESCRIPTION: Data entry option for Biomedical Engineering Resources Survey (BERS)file. Data elements in this file are updated annually by each facility and thensent to the Engineering Service Center in St. Louis. Reports are aggregated for useby VACO program officials.

> DIC {DIC}: ENGS(6916, DIC(0): AELQM

> DIC(A): Enter Survey Year and Hospital Number:

> DIE: ENGS(6916, DR {DIE}: \[ENGSURVEY\]

> DIC {DIP}: ENGS(6916, TIMESTAMP OF PRIMARY MENU: 54545,43576 UPPERCASE MENU TEXT: ENTERING DATA INTO THE BERS SU

> NAME: ENIN-ENTER-MULTI MENU TEXT: Multiple Inventory Entry TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter several like items (e.g.; 50 new electric beds) into the EQUIPMENT INV. file (#6914) without having to enter common information each time.

> ROUTINE: ME^ENEQ1

> UPPERCASE MENU TEXT: MULTIPLE INVENTORY ENTRY

> NAME: ENIN-HIST-GENERIC MENU TEXT: Equipment Category History TYPE: run routine CREATOR:

> DESCRIPTION: A synopsis of the maintenance costs for a given device type. ROUTINE: HD^ENEQRP2

> UPPERCASE MENU TEXT: EQUIPMENT CATEGORY HISTORY

> NAME: ENIN-HIST-SPECIFIC MENU TEXT: Specific Equipment History TYPE: run routine CREATOR: 187

> DESCRIPTION: Print-out of repair history of a specific entry in EQUIPMENT INV. file. ROUTINE: HS^ENEQRP1

> UPPERCASE MENU TEXT: SPECIFIC EQUIPMENT HISTORY

> Exported Options

> NAME: ENINV MENU TEXT: Equipment Management TYPE: menu CREATOR:

> DESCRIPTION: Contains options for maintaining the EQUIPMENT INV. file (#6914) and for managing the PMI program.

> ITEM: ENINVNEW SYNONYM: 1

> DISPLAY ORDER: 1

> ITEM: ENIN-ENTER-MULTI SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: ENINV EDIT SYNONYM: 3

> ITEM: ENINVINV SYNONYM: 4

> ITEM: ENEQ-REPORTS SYNONYM: 5

> ITEM: ENPM SYNONYM: 6

> ITEM: ENPMS SYNONYM: 7

> ITEM: ENPMR SYNONYM: 8

> ITEM: ENBCLBL MGR SYNONYM: 9

> ITEM: ENBCNX MGR SYNONYM: 10

> EXIT ACTION: D EXIT^ENEQ ENTRY ACTION: D INIT^ENEQ,HDR^ENEQ TIMESTAMP: 55586,57320

> UPPERCASE MENU TEXT: EQUIPMENT MANAGEMENT

> NAME: ENINV EDIT MENU TEXT: Inventory Edit TYPE: run routine CREATOR:

> DESCRIPTION: Edit the record of an existing piece of equipment. The .01 field(ENTRY NUMBER) is assigned by the system when an item is first added to the EQUIPMENT INV. file and may not be edited. This option gives access to both Supply and Engineering fields.

> ROUTINE: EDA^ENEQ1 UPPERCASE MENU TEXT: INVENTORY EDIT

> NAME: ENINVINV MENU TEXT: Display Equipment Record TYPE: run routine CREATOR:

> DESCRIPTION: Display selected fields from the EQUIPMENT INV. file. Repair history IS ROUTINE: DS^ENEQ1

> UPPERCASE MENU TEXT: DISPLAY EQUIPMENT RECORD

> NAME: ENINVNEW MENU TEXT: New Inventory Entry TYPE: run routine CREATOR:

> DESCRIPTION: Add a new item to the EQUIPMENT INV. file (#6914). ROUTINE: EN^ENEQ1 UPPERCASE MENU TEXT: NEW INVENTORY ENTRY

> NAME: ENIT ADD NEW PERSON MENU TEXT: Add Entry to New Person File TYPE: run routine CREATOR:

> LOCK: EN IT ASSIGNMENT PACKAGE: ENGINEERING

> DESCRIPTION: Add an entry to the NEW PERSON file. A person should only be added with this option if they will NOT be provided a user account to sign on the computer, but will be assigned responsibility for IT equipment.

> ROUTINE: ADDNP^ENITUTL

> UPPERCASE MENU TEXT: ADD ENTRY TO NEW PERSON FILE

> NAME: ENIT ASSIGN INQ (COM) MENU TEXT: Assignment Inquiry TYPE: inquire CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Inquiry to an assignment of responsibility for IT equipment. Only assignments for the user can be selected.

> DIC {DIC}: ENG(6916.3, DIC(0): AEMQ

> DIC(S): I \$P(^(0),U,2)=DUZ FLDS: \[ENIT ASSIGNMENT INQ\] DIC {DIQ}: ENG(6916.3, DIQ(0): C

> UPPERCASE MENU TEXT: ASSIGNMENT INQUIRY

> NAME: ENIT ASSIGN INQ (IT) MENU TEXT: Assignment Inquiry TYPE: inquire CREATOR:

> PACKAGE: ENGINEERING

Exported Options

> DESCRIPTION: Inquiry to an assignment of responsibility for IT equipment. DIC {DIC}: ENG(6916.3, DIC(0): AEMQ

> FLDS: \[ENIT ASSIGNMENT INQ\] DIC {DIQ}: ENG(6916.3,

> DIQ(0): C UPPERCASE MENU TEXT: ASSIGNMENT INQUIRY

> NAME: ENIT ASSIGN RESP MENU TEXT: Assign Responsibility TYPE: run routine CREATOR:

> LOCK: EN IT ASSIGNMENT PACKAGE: ENGINEERING

> DESCRIPTION: Assign responsibility for IT equipment inventory items to individuals. Only equipment on a CMR that has IT TRACKING set to YES can be assigned.

> ROUTINE: ENITRA

> UPPERCASE MENU TEXT: ASSIGN RESPONSIBILITY

> NAME: ENIT CERTIFY RESP MENU TEXT: Certify Hard Copy Signature TYPE: run routine CREATOR:

> LOCK: EN IT ASSIGNMENT PACKAGE: ENGINEERING

> DESCRIPTION: This option enables an IT person to certify that an assigned person has signed a hard copy hand receipt accepting responsibility for tracked IT equipment. This option is expected to be used only when the assigned person does not have access to VistA in order to directly, electronically sign for the equipment.

> ROUTINE: ENITRC

> UPPERCASE MENU TEXT: CERTIFY HARD COPY SIGNATURE

> NAME: ENIT EQUIP RPT MENU TEXT: Tracked IT Assets Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Report of equipment inventory that has a CMR value with IT TRACKING equal to YES. The report can be run for specific equipment, groups of equipment, or all tracked IT equipment.

> ROUTINE: ENITRRE

> UPPERCASE MENU TEXT: TRACKED IT ASSETS REPORT

> NAME: ENIT INDV RESP RPT (COM)

> MENU TEXT: Individual Responsibility for IT Assets Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Report of all IT equipment currently assigned to the user. ROUTINE: ENITRRI

> UPPERCASE MENU TEXT: INDIVIDUAL RESPONSIBILITY FOR

> NAME: ENIT INDV RESP RPT (IT)

> MENU TEXT: Individual Responsibility for IT Assets Report [TYPE: run routine](http://www.va.gov/vdl/application.asp?appid=37) CREATOR:

> PACKAGE: ENGINEERING E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: Report of all IT equipment currently assigned to a specific responsible individual.

> EXIT ACTION: K ENITMENU ENTRY ACTION: S ENITMENU=1 ROUTINE: ENITRRI

> UPPERCASE MENU TEXT: INDIVIDUAL RESPONSIBILITY FOR

> NAME: ENIT INVENTORY EDIT MENU TEXT: Inventory Edit (IT)

> TYPE: run routine CREATOR:

> LOCK: EN IT INVENTORY PACKAGE: ENGINEERING

> DESCRIPTION: Edit the record of an existing piece of equipment. This option gives access to fields editable by IT personnel. Only equipment that has a CMR with IT TRACKING set to YES can be selected via this option.

> ROUTINE: ENITEQE UPPERCASE MENU TEXT: INVENTORY EDIT (IT)

> NAME: ENIT MGR MENU TEXT: IT Equipment Module

> Exported Options

> TYPE: menu CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: This is a top level menu designed for IT personnel. ITEM: ENIT INVENTORY EDIT SYNONYM: 1

> ITEM: ENINVINV SYNONYM: 2

> ITEM: ENMMBC SYNONYM: 3

> ITEM: ENIN-HIST-SPECIFIC SYNONYM: 4

> ITEM: ENSPROOMD SYNONYM: 5 ITEM: ENIT NON-SPACE FILE LOC RPT SYNONYM: 6 ITEM: ENIT RESP MENU SYNONYM: 7

> TIMESTAMP: 61003,35612 TIMESTAMP OF PRIMARY MENU: 61018,43454 UPPERCASE MENU TEXT: IT EQUIPMENT MODULE

> NAME: ENIT NON-SPACE FILE LOC RPT

> MENU TEXT: Non-Space File Location Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: This report generates a list of equipment that has a value in the NON-SPACE FILE LOCATION field. Equipment should only have a value in this field when the LOCATION field can not be updated because an appropriate location is not available in the ENG SPACE file. Ideally, equipment will not remain on this report for an extended period.

> ROUTINE: ENITNSR

> UPPERCASE MENU TEXT: NON-SPACE FILE LOCATION REPORT

> NAME: ENIT OWNER MENU MENU TEXT: IT Owner Menu TYPE: menu CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Menu intended for users that may be assigned responsibility for IT equipment. It contains options to list and accept responsibility for assigned IT equipment.

> ITEM: ENIT INDV RESP RPT (COM) DISPLAY ORDER: 2 ITEM: ENIT RESP SIGN DISPLAY ORDER: 1 ITEM: ENIT PRINT HAND RCPT (COM) DISPLAY ORDER: 3 ITEM: ENIT ASSIGN INQ (COM) DISPLAY ORDER: 4

> TIMESTAMP: 60998,62500 TIMESTAMP OF PRIMARY MENU: 61018,43454 UPPERCASE MENU TEXT: IT OWNER MENU

> NAME: ENIT PRINT HAND RCPT (COM) MENU TEXT: Print My Hand Receipt

> TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: This option enables the user to print hand receipts for IT items assigned to the user.

> ROUTINE: ASK^ENITRRH

> UPPERCASE MENU TEXT: PRINT MY HAND RECEIPT

> NAME: ENIT PRINT HAND RCPT (IT)

> MENU TEXT: Print Hand Receipt for an Individual TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: This option enables IT personnel to print hard copy hand receipt for an individual.

> ROUTINE: ASK^ENITRRH

> UPPERCASE MENU TEXT: PRINT HAND RECEIPT FOR AN INDI

> NAME: ENIT RESP MENU MENU TEXT: IT Equipment Responsibility TYPE: menu CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: This is the menu for the equipment responsibility options. ITEM: ENIT TERMINATE RESP DISPLAY ORDER: 2

> ITEM: ENIT TRANSFER RESP DISPLAY ORDER: 3

> ITEM: ENIT ASSIGN RESP DISPLAY ORDER: 1

> ITEM: ENIT CERTIFY RESP DISPLAY ORDER: 4

Exported Options

> ITEM: ENIT RESP RPT MENU DISPLAY ORDER: 7

> ITEM: ENIT ADD NEW PERSON DISPLAY ORDER: 6 ITEM: ENIT PRINT HAND RCPT (IT) DISPLAY ORDER: 5

> TIMESTAMP: 61003,35584

> UPPERCASE MENU TEXT: IT EQUIPMENT RESPONSIBILITY

> NAME: ENIT RESP NOT ASSIGNED RPT MENU TEXT: Unassigned IT Asset Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Report of tracked IT Assets that are not currently assigned to a responsible individual. Assets are considered to be tracked IT assets if their CMR value has IT TRACKING set to YES.

> ROUTINE: ENITRRNA

> UPPERCASE MENU TEXT: UNASSIGNED IT ASSET REPORT

> NAME: ENIT RESP NOTIFY

> MENU TEXT: Notify User of IT Assignments Requiring Signature TYPE: action CREATOR:

> PACKAGE: ENGINEERING E ACTION PRESENT: YES

> DESCRIPTION: Provides user with notification during sign-on of any IT equipment assignments of responsibility that require their signature. IT assignments must be re-signed by the anniversary date of their previous signature.

> ENTRY ACTION: D ^ENITRN

> UPPERCASE MENU TEXT: NOTIFY USER OF IT ASSIGNMENTS

> NAME: ENIT RESP RPT MENU MENU TEXT: IT Equipment Report Menu TYPE: menu CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Menu of IT equipment reports.

> ITEM: ENIT INDV RESP RPT (IT) DISPLAY ORDER: 1 ITEM: ENIT EQUIP RPT DISPLAY ORDER: 4

> ITEM: ENIT SIGN EXCEPT RPT DISPLAY ORDER: 5 ITEM: ENIT RESP NOT ASSIGNED RPT DISPLAY ORDER: 2 ITEM: ENIT RESP UNSIGNED RPT DISPLAY ORDER: 3

> ITEM: ENIT ASSIGN INQ (IT) DISPLAY ORDER: 6 TIMESTAMP: 60998,62601

> UPPERCASE MENU TEXT: IT EQUIPMENT REPORT MENU

> NAME: ENIT RESP SIGN MENU TEXT: Accept IT Responsibility TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: The user will accept responsibility for assigned IT equipment by this option.This option allows a user to sign to reaffirm the acceptance, as well as, enter the initial acceptance.

> ROUTINE: ENITRS

> UPPERCASE MENU TEXT: ACCEPT IT RESPONSIBILITY

> NAME: ENIT RESP UNSIGNED RPT

> MENU TEXT: Assignments Pending Acceptance Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Report of equipment with IT assignments that have not yet been signed.

> ROUTINE: ENITRRU

> UPPERCASE MENU TEXT: ASSIGNMENTS PENDING ACCEPTANCE

> NAME: ENIT SIGN EXCEPT RPT MENU TEXT: Signature Exception Report TYPE: run routine CREATOR:

> PACKAGE: ENGINEERING

> DESCRIPTION: Report assignments of IT responsibility with the most recent signature at least one year old as of a user specified date.

> Exported Options

> ROUTINE: ENITRRX

> UPPERCASE MENU TEXT: SIGNATURE EXCEPTION REPORT

> NAME: ENIT TERMINATE RESP MENU TEXT: Terminate Responsibility TYPE: run routine CREATOR:

> LOCK: EN IT ASSIGNMENT PACKAGE: ENGINEERING

> DESCRIPTION: This option enables the user to terminate one or more active responsibilities from a list of responsibilities based on an equipment item or a person.

> ROUTINE: ENITRT

> UPPERCASE MENU TEXT: TERMINATE RESPONSIBILITY

> NAME: ENIT TRANSFER RESP MENU TEXT: Transfer Responsibility TYPE: run routine CREATOR:

> LOCK: EN IT ASSIGNMENT PACKAGE: ENGINEERING

> DESCRIPTION: This option terminates selected responsibilities and creates new responsibilities for equipment under another person.

> ROUTINE: ENITRX

> UPPERCASE MENU TEXT: TRANSFER RESPONSIBILITY

> NAME: ENIT USER ACCOUNT TERMINATED

> MENU TEXT: IT Notification of Terminated User with Equipment TYPE: action CREATOR:

> PACKAGE: ENGINEERING E ACTION PRESENT: YES

> DESCRIPTION: This option should be attached to XU USER TERMINATE to notify IT when a user with active IT equipment responsibilities is terminated as a VistA user.

> ENTRY ACTION: D USRTRM^ENITUTL

> UPPERCASE MENU TEXT: IT NOTIFICATION OF TERMINATED

> NAME: ENMAN MENU TEXT: Program Management TYPE: menu CREATOR:

> LOCK: ENMGR

> DESCRIPTION: Intended for use by Engineering Application Manager in maintaining files used by the Engineering package.

> ITEM: ENMANUFAC SYNONYM: 6

> ITEM: ENPORT SYNONYM: 1

> ITEM: ENSECTION SYNONYM: 2

> ITEM: ENWORK CTR SYNONYM: 3

> ITEM: ENEMP SYNONYM: 4

> ITEM: ENWORK ACTION SYNONYM: 11

> ITEM: ENAR SYNONYM: 9

> ITEM: ENPM5 SYNONYM: 5

> ITEM: ENSITE SYNONYM: 7

> ITEM: ENSWOPT SYNONYM: 8

> ITEM: ENGSMENU SYNONYM: 10

> EXIT ACTION: D EXIT^ENMAN ENTRY ACTION: D INIT^ENMAN

> TIMESTAMP: 55586,57331 UPPERCASE MENU TEXT: PROGRAM MANAGEMENT

> Exported Options

> NAME: ENMANUFAC MENU TEXT: Manufacturer TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit of the MANUFACTURER file. This file is maintained by the Engineering Service Center in cooperation with the Region 2 ISC. Sites may add entries as necessary, using a ZZ namespace convention. Application managers should check carefully to insure that any local entries are not, in fact, duplications.

> ROUTINE: MAN^ENMAN UPPERCASE MENU TEXT: MANUFACTURER

> NAME: ENMGR MENU TEXT: Engineering Main Menu TYPE: menu CREATOR: 187

> DESCRIPTION: Engineering Main Menu for the Manager ITEM: ENWO SYNONYM: WO

> DISPLAY ORDER: 1

> ITEM: ENPROJ SYNONYM: TRK

> DISPLAY ORDER: 3

> ITEM: ENINV SYNONYM: EQ

> DISPLAY ORDER: 4

> ITEM: ENSP SYNONYM: SP

> DISPLAY ORDER: 5

> ITEM: ENMAN SYNONYM: ENM

> DISPLAY ORDER: 5

> ITEM: ENFS-2162 SYNONYM: FSA DISPLAY ORDER: 7

> ITEM: ENPLM01 SYNONYM: PLAN

> DISPLAY ORDER: 2

> ITEM: ENETRANSFER SYNONYM: XFER DISPLAY ORDER: 8

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55630,56164 TIMESTAMP OF PRIMARY MENU: 55189,29894 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENMM MGR

> MENU TEXT: Nonexpendable Equipment Module (A&MM) TYPE: menu CREATOR: 187

> DESCRIPTION: Top level menu option for Personal Property Management using AEMS/MERS (Automated Engineering Management System and Medical Equipment Reporting System).

> ITEM: ENMMEE SYNONYM: 1

> ITEM: ENMMREP SYNONYM: 2

> ITEM: ENMMBC SYNONYM: 3

> ITEM: ENMM UTIL SYNONYM: 4

> TIMESTAMP: 55586,57347

> UPPERCASE MENU TEXT: NONEXPENDABLE EQUIPMENT MODULE

> NAME: ENMM UTIL

> MENU TEXT: NX (Nonexpendable Equipment) Utilities TYPE: menu CREATOR: 187

> DESCRIPTION: Includes options used to maintain anciliary files that are necessary for Personal Property Management under AEMS/MERS.

> ITEM: ENCMR SYNONYM: 1

> ITEM: ENCSN SYNONYM: 2

> TIMESTAMP: 55586,57343

> UPPERCASE MENU TEXT: NX (NONEXPENDABLE EQUIPMENT) U

> Exported Options

> NAME: ENMMBC

> MENU TEXT: Bar Code Features (NX Equipment)

> TYPE: menu CREATOR: 187

> DESCRIPTION: Collection of options designed for use in bar coding nonexpendable equipment and in using bar code to maintain CMR inventories.

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 38%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ITEM: ENBCLBLEE</p>
</blockquote></th>
<th>SYNONYM:</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENBCLBLSP</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENBCNXDNLD</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENBCUPLD</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENBCNXRES</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENBCNXCMR</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIMESTAMP: 55586,57344</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> UPPERCASE MENU TEXT: BAR CODE FEATURES (NX EQUIPMEN

> NAME: ENMMEE MENU TEXT: Equipment Enter/Edit (NX) TYPE: menu CREATOR: 187

> DESCRIPTION: Collection of options for entering data into the AEMS/MERS Equipment file.

> ITEM: ENINVNEW SYNONYM: 1

> ITEM: ENINV EDIT SYNONYM: 2

> ITEM: ENINVINV SYNONYM: 3

> ITEM: ENIN-ENTER-MULTI SYNONYM: 4

> ITEM: ENBCNXMAN SYNONYM: 5

> TIMESTAMP: 55586,57346

> UPPERCASE MENU TEXT: EQUIPMENT ENTER/EDIT (NX)

> NAME: ENMMREP

> MENU TEXT: Equipment Management Reports (NX) TYPE:

> menu CREATOR: 187

> DESCRIPTION: Collection of AEMS/MERS outputs that are thought to be of interest to the Property Management Section of A&MM.

> ITEM: ENIN-HIST-SPECIFIC SYNONYM: 1

> ITEM: ENEQINV1 SYNONYM: 2

> ITEM: ENEQ-WARRANTY SYNONYM: 3

> ITEM: ENEQ-REPLACE SYNONYM: 4

> ITEM: ENEQINV3 SYNONYM: 5

> ITEM: ENEQINV4 SYNONYM: 6

> ITEM: ENEQINV6 SYNONYM: 7

> TIMESTAMP: 55586,57345

> UPPERCASE MENU TEXT: EQUIPMENT MANAGEMENT REPORTS (

> NAME: ENPLM01 MENU TEXT: Project Planning TYPE: menu CREATOR: .5

> DESCRIPTION: This is the root menu option for Project Planning module of construction, including selections for 5-Yr Plan and 1193 submission, and prioritization methodology for NRM, Minor, and Minor Miscellaneous projects. ITEM: ENPLM02 SYNONYM: 1

> ITEM: ENPLM05 SYNONYM: 2

> ITEM: ENPLM09 SYNONYM: 3

> ITEM: ENPLM18 SYNONYM: 4

> ITEM: ENPLM12 SYNONYM: 5

> ITEM: ENPLM13 SYNONYM: 7

> ITEM: ENPLM16 SYNONYM: 6

> ENTRY ACTION: W @IOF,!!?18,"PROJECT PLANNING OPTIONS",!!

> TIMESTAMP: 55634,35082 UPPERCASE MENU TEXT: PROJECT PLANNING

> Exported Options

> NAME: ENPLM02 MENU TEXT: 5-Yr Plan Project E/E

> TYPE: run routine CREATOR: .5

> DESCRIPTION: This option enables entry of information that appears on 5-Yr Plan for each project.

> ROUTINE: ENT^ENPL4

> UPPERCASE MENU TEXT: 5-YR PLAN PROJECT E/E

> NAME: ENPLM03

> MENU TEXT: Minor/Minor Misc Prioritization

> TYPE: run routine CREATOR: .5

> DESCRIPTION: This option performs the Prioritization Methodology for Minor Design and Minor Miscellaneous projects and then prints report to screen or Scoring sheet on 80 column printer.

> ROUTINE: A^ENPL3A

> UPPERCASE MENU TEXT: MINOR/MINOR MISC PRIORITIZATIO

> NAME: ENPLM04

> MENU TEXT: NRM Prioritization Scoring Sheet TYPE:

> print CREATOR: .5

> DESCRIPTION: This option prints the NRM Prioritization Methodology Scoring sheet on terminal display or 80 column printer.

> DIC {DIP}: ENG("PROJ", L.: 0

> FLDS: \[ENPLP003\] BY: .01 DIS(0): I \$D(^ENG("PROJ",D0,0)),\$P(^(0),U,6)="NR" UPPERCASE MENU TEXT: NRM PRIORITIZATION SCORING SHE

> NAME: ENPLM05

> MENU TEXT: Project Application E/E (VAF 10-1193) TYPE: run routine CREATOR: .5

> DESCRIPTION: This option enables entering all information required for forms VAF 10-1193, VAF 10-1193a and prioritization methodology scoring sheets.

> ROUTINE: ENT^ENPL2

> UPPERCASE MENU TEXT: PROJECT APPLICATION E/E (VAF 1

> NAME: ENPLM06

> MENU TEXT: Project Application VAF 10-1193 (132 columns) TYPE: run routine CREATOR: .5

> DESCRIPTION: This option prints the project application (VAF 10-1193 Rev. 12/92) on a 132 column printer. It is recommended that you queue the

> printing. ROUTINE: ENPL10

> UPPERCASE MENU TEXT: PROJECT APPLICATION VAF 10-119

> NAME: ENPLM08

> MENU TEXT: Environmental Analysis VAF 10-1193a (132 columns) TYPE: run routine CREATOR: .5

> DESCRIPTION: This option prints the EMIS Construction Program Environmental Analysis form VAF 10-1193a on a 132 column printer.

> ROUTINE: A^ENPL11

> UPPERCASE MENU TEXT: ENVIRONMENTAL ANALYSIS VAF 10•

> NAME: ENPLM09

> MENU TEXT: Environmental Analysis E/E (VAF 10-1193a) TYPE: run routine CREATOR: .5

> DESCRIPTION: This option enables entry of information which appears on VAF 10• 1193a.

> ROUTINE: ENT^ENPL6

> UPPERCASE MENU TEXT: ENVIRONMENTAL ANALYSIS E/E (VA

> NAME: ENPLM11

> MENU TEXT: 5-Yr Plan Report (132 columns)

> TYPE: run routine CREATOR: .5

> DESCRIPTION: This option prints the 5-Yr Plan, selecting items on the basis of Funding Year A/E, Funding Year Construction, Project Status and Five Year Plan Status fields.

> Exported Options

> ROUTINE: IN^ENPL5

> UPPERCASE MENU TEXT: 5-YR PLAN REPORT (132 COLUMNS)

> NAME: ENPLM12 MENU TEXT: Report/Print Menu TYPE: menu CREATOR: .5

> DESCRIPTION: This is the print menu for the construction planning module. ITEM: ENPLM03 SYNONYM: 1

> ITEM: ENPLM04 SYNONYM: 2

> ITEM: ENPLM06 SYNONYM: 3

> ITEM: ENPLM08 SYNONYM: 4

> ITEM: ENPLM11 SYNONYM: 5

> ENTRY ACTION: W @IOF,!!,?18,"PROJECT PLANNING PRINT OPTIONS",!!

> TIMESTAMP: 55635,34946 UPPERCASE MENU TEXT: REPORT/PRINT MENU

> NAME: ENPLM13 MENU TEXT: Electronic Transmission Menu TYPE: menu CREATOR: .5

> LOCK: ENPLK003

> DESCRIPTION: This menu contains options for electronic transmission of 5-Yr Plan and Project Application data elements.

> ITEM: ENPLM14 SYNONYM: 1

> ITEM: ENPLM15 SYNONYM: 2

> ITEM: ENPLM17 SYNONYM: 3

> EXIT ACTION: W @IOF

> ENTRY ACTION: W @IOF,!!,?18,"PROJECT TRANSMISSION OPTIONS",!! TIMESTAMP: 55614,37950

> UPPERCASE MENU TEXT: ELECTRONIC TRANSMISSION MENU

> NAME: ENPLM14

> MENU TEXT: Batch Transmit 5-Yr Plan Projects TYPE: run routine CREATOR: .5 LOCK: ENPLK003

> DESCRIPTION: This option prompts the user for the Station and Fiscal Year of the 5-Yr Plan and then creates the MailMan message to transmit the data for the 5-Yr Plan from the site to the higher approval authorities.

> EXIT ACTION: W @IOF ROUTINE: ENPL8 UPPERCASE MENU TEXT: BATCH TRANSMIT 5-YR PLAN PROJE

> NAME: ENPLM15

> MENU TEXT: Individual 5-Yr Plan Project Transmission TYPE: run routine CREATOR: .5 LOCK: ENPLK003

> DESCRIPTION: This option requests the project number and Fiscal Year of the 5-Yr Plan and then creates the MailMan message to send the project's data to the higher approval authorities.

> EXIT ACTION: W @IOF ROUTINE: ENPL8A UPPERCASE MENU TEXT: INDIVIDUAL 5-YR PLAN PROJECT T

> Exported Options

> NAME: ENPLM16

> MENU TEXT: Approval of Project Application

> TYPE: run routine CREATOR: .5

> DESCRIPTION: This option controls the Chief Engineer's and VAMC Director's sign off on the project application. The Security Key ENPLK001 controls the Chief Engineer's approval. The Security Key ENPLK002 controls the VAMC Director's approval. The Chief Engineer must sign off before the VAMC Director. Both must approve before the project application can be transmitted electronically to higher approval authorities.

> ROUTINE: ENPL9

> UPPERCASE MENU TEXT: APPROVAL OF PROJECT APPLICATIO

> NAME: ENPLM17 MENU TEXT: Project Application Send TYPE: run routine CREATOR: .5

> LOCK: ENPLK003

> DESCRIPTION: This option loads the data for a selected project into a MailMan message and transmits the data to higher approval authorities.

> EXIT ACTION: W @IOF ROUTINE: ENPL7 UPPERCASE MENU TEXT: PROJECT APPLICATION SEND

> NAME: ENPLM18 MENU TEXT: Activations E/E TYPE: run routine CREATOR: ENGUSER, ONE

> DESCRIPTION: This option enables enter/edit of project activations information. ROUTINE: ACT^ENPL2 UPPERCASE MENU TEXT: ACTIVATIONS E/E

> NAME: ENPM MENU TEXT: PM Parameters TYPE: menu CREATOR: 187

> DESCRIPTION: Contains options for enrolling devices and device types in the PMI program. ITEM: ENPM1 SYNONYM: 1

> ITEM: ENPM2 SYNONYM: 2

> ITEM: ENPM3 SYNONYM: 3

> ITEM: ENPM4 SYNONYM: 4

> ITEM: ENPM5 SYNONYM: 5

> ITEM: ENPM6 SYNONYM: 6

> ENTRY ACTION: D HDR^ENEQPMP TIMESTAMP: 55586,57251 UPPERCASE MENU TEXT: PM PARAMETERS

> NAME: ENPM1

> MENU TEXT: Display Specific Device PM Schedule TYPE: run routine CREATOR: 187

> DESCRIPTION: Displays in a screen format the PM schedule of a specific device (discrete entry in File 6914, EQUIPMENT INV.). Editing not allowed.

> ROUTINE: PMSD^ENEQPMP1

> UPPERCASE MENU TEXT: DISPLAY SPECIFIC DEVICE PM SCH

> NAME: ENPM10 MENU TEXT: Delete PM Work Orders TYPE: run routine CREATOR: 187

> DESCRIPTION: Intended to enable you to delete PM work orders in order to conserve disk space. Deletion of PM work orders via this option will not remove an existing record of the PMI from the equipment history. Deletion of any work order via the EDIT WORK ORDER option WILL remove the corresponding entry from the equipment history. If you intend to record PMI's in the equipment history, you should not delete PM work orders until after they have been recorded.

> ROUTINE: DEL^ENEQPMS4

> UPPERCASE MENU TEXT: DELETE PM WORK ORDERS

> Exported Options

> NAME: ENPM2

> MENU TEXT: Display Equipment Category PM Schedule TYPE: run routine CREATOR: 187

> DESCRIPTION: Displays in screen format the PM schedule of a given device type (discrete entry in File 6911, DEVICE NAME). This is best thought of as the default PM schedule for all devices of the given type. No editing.

> ROUTINE: DTD^ENEQPMP1

> UPPERCASE MENU TEXT: DISPLAY EQUIPMENT CATEGORY PM

> NAME: ENPM3 MENU TEXT: Print PM Procedure TYPE: run routine CREATOR: 187

> DESCRIPTION: Print out the title and text (if stored) of a specified PM procedure.

> ROUTINE: PROCD^ENEQPMP2 UPPERCASE MENU TEXT: PRINT PM PROCEDURE

> NAME: ENPM4

> MENU TEXT: Enter/Edit Specific Device PM Schedule TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter or change the PM schedule for a specified device (discrete entry in File 6914, EQUIPMENT INV.). This option will have no affect on other entries of the same device type.

> ROUTINE: PMSE^ENEQPMP

> UPPERCASE MENU TEXT: ENTER/EDIT SPECIFIC DEVICE PM

> NAME: ENPM5

> MENU TEXT: Enter/Edit Equipment Category PM Schedule TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter or change the PM schedule for a specified device type (such as DEFIBRILLATORS, GENERATORS-ELECTRICAL, etc.). A device type is formally defined as a discrete entry in the Equipment Category file. When a device type PM schedule is entered or changed, the user will be given the opportunity to apply the new schedule to all existing devices of the specified type.

> ROUTINE: DTE^ENEQPMP1

> UPPERCASE MENU TEXT: ENTER/EDIT EQUIPMENT CATEGORY

> NAME: ENPM6 MENU TEXT: Enter/Edit PM Procedure TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter procedures to be followed in performing PMI's. The procedure identifier will be printed on PM worksheets as a reminder to the tech, and will become a part of the equipment history whenever a scheduled PMI is recorded. It is recommended that the full text of PM procedures be stored in this file if time and disk space permit.

> ROUTINE: PROCE^ENEQPMP2

> UPPERCASE MENU TEXT: ENTER/EDIT PM PROCEDURE

> NAME: ENPM7 MENU TEXT: Monthly PM List

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Print PMI worksheet(s) for monthly PMI's. These worksheets will include scheduled ANNUAL, SEMI-ANNUAL, QUARTERLY, BI-MONTHLY, and MONTHLY

> PMI's.

> ROUTINE: MNTH^ENEQPMS1 UPPERCASE MENU TEXT: MONTHLY PM LIST

> NAME: ENPM8 MENU TEXT: Weekly PM List

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Print PMI worksheet(s) to include WEEKLY and BI-WEEKLY PMI's. You will be prompted for a week number (1 thru 5). BI-WEEKLY PMI's will appear on worksheets for

> weeks 1 and 3.

> ROUTINE: WK^ENEQPMS1 UPPERCASE MENU TEXT: WEEKLY PM LIST

> NAME: ENPMHOURS MENU TEXT: Print PM Manhours TYPE: print CREATOR: ENGUSER , TWO

> Exported Options

> DESCRIPTION: Prints total manhours expended on preventive maintenance by shop and by month for each technician. These manhours are automatically recorded when PM work orders are closed out.

> New with Engineering Version 7.

> DIC {DIC}: DIC(6922, DIC(0): AEQM

> DIC {DIP}: DIC(6922, L.: 0

> FLDS: \[EN PM HOURS\] BY: \[EN PM HOURS\] UPPERCASE MENU TEXT: PRINT PM MANHOURS

> NAME: ENPMINSP MENU TEXT: Engineering PM Clerk Main Menu TYPE: menu CREATOR: 187

> DESCRIPTION: This menu is set up for PM Inspector ITEM: ENWO SYNONYM: 1

> ITEM: ENINV SYNONYM: 2

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55586,57263 TIMESTAMP OF PRIMARY MENU: 53501,40523 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENPMR MENU TEXT: Record Equipment PMI TYPE: menu CREATOR: 187

> DESCRIPTION: Contains options to record PM inspections. This process essentially closes a PM work order and posts the activity to the equipment

> history.

> ITEM: ENPMR1 SYNONYM: 1

> ITEM: ENPMR2 SYNONYM: 2

> ITEM: ENPMR3 SYNONYM: 3

> ITEM: ENSA1 SYNONYM: 5

> ITEM: ENPMRDEFRL SYNONYM: 6

> ITEM: ENBCPM MGR SYNONYM: 4

> ITEM: ENPMHOURS SYNONYM: 7

> TIMESTAMP: 55595,60729

> UPPERCASE MENU TEXT: RECORD EQUIPMENT PMI

> NAME: ENPMR1 MENU TEXT: Close Out PM Work Orders TYPE: run routine CREATOR: 187

> DESCRIPTION: Close out a PM work list entry by entry. User is asked for a complete specification of the first PM work order; after that the system assumes the shop, month, and type (MONTHLY or WEEKLY) of work list.

> ROUTINE: CO^ENEQPMR1

> UPPERCASE MENU TEXT: CLOSE OUT PM WORK ORDERS

> NAME: ENPMR2

> MENU TEXT: Rapid Closeout of PM Work Orders

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Closes out an entire PM worklist. User is prompted for any PM work orders that are to be closed out individually. All work orders on the specified list which are not closed out individually will be assigned a PM status of PASSED and default values (if any) for time and materials. This option may take a while to run, so the user is given the opportunity to free his terminal. Freeing the terminal causes this option to begin to run immediately as a background job. This option may slow the system noticeably and it may be desireable to assign this task a lower priority than interactive jobs.

> ROUTINE: RCO^ENEQPMR2

> UPPERCASE MENU TEXT: RAPID CLOSEOUT OF PM WORK ORDE

> Exported Options

> NAME: ENPMR3 MENU TEXT: Record Single Device PMI TYPE: run routine CREATOR: 187

> DESCRIPTION: May be used to record a PMI on any specified device, irregardless of whether or not it is on an active PMI list. One use envisioned for this is recording the results of 'area sweeps'. If the specified device is in the scheduled PMI program and it appears that a PMI recorded via this option may make it desireable to change the scheduled FREQUENCY or the STARTING MONTH, the user will be afforded an opportunity to do so.

> ROUTINE: SDPM^ENEQPMR4

> UPPERCASE MENU TEXT: RECORD SINGLE DEVICE PMI

> NAME: ENPMRDEFRL MENU TEXT: Rapid Deferral of PM Worklist TYPE: run routine CREATOR: 187

> DESCRIPTION: Defers all entries on a user specified PM worklist. All work orders on subject worklist are given a PM Status of DEFERRED and a close out date of TODAY. Time and Materials are not posted. This option is intended to be run only if you want to post DEFERRAL's of all open line items (PM work orders) on subject worklist to Equipment Histories.

> This option is not intended for use in cases where there is some expectation that you may wish to otherwise close-out the PM worklist in question at some later date. That is to say, once a scheduled preventive maintenance inspection task has been recorded as DEFERRED it will be difficult to change it to PASSED.

> ROUTINE: ENEQPMR6

> UPPERCASE MENU TEXT: RAPID DEFERRAL OF PM WORKLIST

> NAME: ENPMS MENU TEXT: Generate PM Schedule TYPE: menu CREATOR: 187

> DESCRIPTION: Contains options for printing PMI work sheets and for deletion of PM work orders.

> ITEM: ENPM7 SYNONYM: 1

> ITEM: ENPM8 SYNONYM: 2

> ITEM: ENPM10 SYNONYM: 3

> ENTRY ACTION: D HDR^ENEQPMS TIMESTAMP: 55586,57294 UPPERCASE MENU TEXT: GENERATE PM SCHEDULE

> NAME: ENPORT MENU TEXT: Engineering Computer Port TYPE: run routine CREATOR: 187

> DESCRIPTION: Used to specify those ports on the Engineering system that are suitable for output of hard-copy reports.

> ROUTINE: PORT^ENMAN

> UPPERCASE MENU TEXT: ENGINEERING COMPUTER PORT

> NAME: ENPREL MENU TEXT: Preliminary Data Screen TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit the most fundamental elements of a delegated construction project.

> ROUTINE: PROJ3^ENPROJ

> UPPERCASE MENU TEXT: PRELIMINARY DATA SCREEN

> Exported Options

> NAME: ENPROJ MENU TEXT: Project Tracking TYPE: menu CREATOR: 187

> DESCRIPTION: Main driver option for Construction Project module. ITEM: ENPROJXMIT SYNONYM: 12

> ITEM: ENPROJ TKR SYNONYM: 1

> ITEM: ENSCREEN SYNONYM: 2

> ITEM: ENPREL SYNONYM: 3

> ITEM: ENAPPROV SYNONYM: 4

> ITEM: ENREV SYNONYM: 5

> ITEM: ENACTUAL SYNONYM: 6

> ITEM: ENAE SYNONYM: 7

> ITEM: ENCHANGES SYNONYM: 9

> ITEM: ENPROJSTAT SYNONYM: 10

> ITEM: ENPROJ10 SYNONYM: 11

> ITEM: ENCONTR SYNONYM: 8

> ENTRY ACTION: D HDR^ENPROJ TIMESTAMP: 55612,51281 UPPERCASE MENU TEXT: PROJECT TRACKING

> NAME: ENPROJ TKR MENU TEXT: Enter Project Data TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit of construction project tracking data in line by line FileMan format.

> ROUTINE: PROJ^ENPROJ UPPERCASE MENU TEXT: ENTER PROJECT DATA

> NAME: ENPROJ10

> MENU TEXT: Print All Project Status Reports

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Print hardcopy 10-0051 of all construction projects for which the MONTHLY PRINT-OUT field is set to 'YES'.

> ROUTINE: ALL^ENPRP

> UPPERCASE MENU TEXT: PRINT ALL PROJECT STATUS REPOR

> NAME: ENPROJSTAT MENU TEXT: Print Project Status Report TYPE: run routine CREATOR: 187

> DESCRIPTION: Generate hardcopy 10-0051 for a specific construction project. ROUTINE: SINGLE^ENPRP

> UPPERCASE MENU TEXT: PRINT PROJECT STATUS REPORT

> NAME: ENPROJXMIT

> MENU TEXT: Transmit 10-0051 Electronically

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Packs 10-0051's into Network MailMan messages and routes them to the Office of Facilities in VACO.

> ROUTINE: ENPROJ7

> UPPERCASE MENU TEXT: TRANSMIT 10-0051 ELECTRONICALL

> NAME: ENREV MENU TEXT: Revised Dates Screen Edit TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit revised dates (if any) of project milestones. These dates must be exact (month-day-year) and should reflect any discrepancies between original schedule and current best estimates.

> ROUTINE: PROJ5^ENPROJ

> UPPERCASE MENU TEXT: REVISED DATES SCREEN EDIT

> Exported Options

> NAME: ENSA1 MENU TEXT: Upload Data from MedTester TYPE: run routine CREATOR: 187

> DESCRIPTION: Reads data from MedTester (Electrical Safety Analyzer manufactured by Dynatech Nevada, Inc.) and posts electrical safety inspections to Equipment Histories.

> ROUTINE: EN^ENSA

> UPPERCASE MENU TEXT: UPLOAD DATA FROM MEDTESTER

> NAME: ENSCREEN MENU TEXT: Screen Review All Data TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter/edit construction project data using a screen server. ROUTINE: PROJ2^ENPROJ

> UPPERCASE MENU TEXT: SCREEN REVIEW ALL DATA

> NAME: ENSEC MENU TEXT: Engineering Secretary Main Menu TYPE: menu CREATOR: 187

> DESCRIPTION: This menu is used by the Engineering secretaries. Most sites will probably want to add selected IFCAP options to this 'menu' item.

> ITEM: ENPROJ SYNONYM: 1

> ITEM: ENEUSER1 SYNONYM: 2

> ITEM: ENSP SYNONYM: 3

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55630,56164 TIMESTAMP OF PRIMARY MENU: 53512,52393 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENSECFORM MENU TEXT: Engineering Foreman Main Menu TYPE: menu CREATOR: 187

> DESCRIPTION: This Menu is set up for the Section Foreman. ITEM: ENWO SYNONYM: 1

> ITEM: ENINV SYNONYM: 2

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55586,57263 TIMESTAMP OF PRIMARY MENU: 53501,40523 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENSECTION MENU TEXT: Section List

> TYPE: run routine CREATOR: 187 DESCRIPTION: Editing of the engineering section file.

> ROUTINE: SEC^ENMAN UPPERCASE MENU TEXT: SECTION LIST

> NAME: ENSITE

> MENU TEXT: ENG SITE PARAMETERS Enter/Edit

> TYPE: edit CREATOR: 187

> DESCRIPTION: Used to set up the Engineering Site parameters. Certain entries in this file are mandatory if a site intends to transmit 10-0051's (Construction Project Tracking Reports) electronically and/or allow computerized entry of work requests non-Engineering personnel.

> DIC {DIC}: DIC(6910, DIC(0): AEMQ

> DIE: DIC(6910, DR {DIE}: 1:99 UPPERCASE MENU TEXT: ENG SITE PARAMETERS ENTER/EDIT

Exported Options

> NAME: ENSP MENU TEXT: Space/Facility Management TYPE: menu CREATOR: .5

> DESCRIPTION: Main driver option for Engineering Facility Management package. ITEM: ENSP1 SYNONYM: 1

> ITEM: ENSP2 SYNONYM: 2

> ITEM: ENSPUTL SYNONYM: 4

> ITEM: ENSP3 SYNONYM: 3

> ITEM: ENSP-LEASE SYNONYM: 5

> ITEM: ENSP-PLAN SYNONYM: 6

> ENTRY ACTION: D HDR^ENSP TIMESTAMP: 55630,56224 TIMESTAMP OF PRIMARY MENU: 54540,68963

> UPPERCASE MENU TEXT: SPACE/FACILITY MANAGEMENT

> NAME: ENSP-137-AMIS

> MENU TEXT: Building Management RCS 10-203, VAF 10-6007a TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates a square footage report in the AMIS format needed by Building Management.

> ROUTINE: PR137^ENSP

> UPPERCASE MENU TEXT: BUILDING MANAGEMENT RCS 10-203

> NAME: ENSP-LEASE MENU TEXT: Leased Space Options TYPE: menu CREATOR: .5

> DESCRIPTION: Driver for leased space data entry and printing. ITEM: ENSP-LEASE1 SYNONYM: 1

> ITEM: ENSP-LEASE2 SYNONYM: 2

> ITEM: ENSP-LEASE3 SYNONYM: 3 TIMESTAMP: 55630,56773

> UPPERCASE MENU TEXT: LEASED SPACE OPTIONS

> NAME: ENSP-LEASE1

> MENU TEXT: Enter/Edit All Lease Fields (BUILDING FILE) TYPE: run routine CREATOR: .5

> DESCRIPTION: Maintain information on leased space. ROUTINE: L^ENSP6

> UPPERCASE MENU TEXT: ENTER/EDIT ALL LEASE FIELDS (B

> NAME: ENSP-LEASE2

> MENU TEXT: Enter/Edit Lease Vendor (BUILDING FILE) TYPE: run routine CREATOR: .5

> DESCRIPTION: Edits name and address of lessor. ROUTINE: VEN^ENSP6

> UPPERCASE MENU TEXT: ENTER/EDIT LEASE VENDOR (BUILD

> NAME: ENSP-LEASE3 MENU TEXT: Print Leased Space Survey TYPE: run routine CREATOR: .5

> DESCRIPTION: Prints the standard information on leased rooms. ROUTINE: P^ENSP6

> UPPERCASE MENU TEXT: PRINT LEASED SPACE SURVEY

> Exported Options

> NAME: ENSP-PLAN MENU TEXT: Planning Space Program Menu TYPE: menu CREATOR:

> DESCRIPTION: Menu for options to be used for entering space planning data for construction projects.

> ITEM: ENSPUTL3 SYNONYM: 1

> ITEM: ENSP-PLAN2 SYNONYM: 3

> ITEM: ENSP-PLAN1 SYNONYM: 2 TIMESTAMP: 55630,56230

> UPPERCASE MENU TEXT: PLANNING SPACE PROGRAM MENU

> NAME: ENSP-PLAN1 MENU TEXT: Enter/Edit Room Planning Data TYPE: run routine CREATOR:

> DESCRIPTION: Option to edit only fields related to space planning criteria ROUTINE: EP^ENSP6

> UPPERCASE MENU TEXT: ENTER/EDIT ROOM PLANNING DATA

> NAME: ENSP-PLAN2

> MENU TEXT: Print Building/Project Space Plan TYPE: run routine CREATOR:

> DESCRIPTION: Option to print planning data based on building and criteria chapter. Report is sorted by PROJECT NUMBER.

> ROUTINE: PP^ENSP6

> UPPERCASE MENU TEXT: PRINT BUILDING/PROJECT SPACE P

> NAME: ENSP1 MENU TEXT: Space Management TYPE: menu CREATOR:

> E ACTION PRESENT: YES

> DESCRIPTION: Main driver option for Engineering Space Package. ITEM: ENSPROOM SYNONYM: 1

> ITEM: ENSPROOMD SYNONYM: 2

> ITEM: ENSP4 SYNONYM: 3

> ITEM: ENSP5 SYNONYM: 4

> ITEM: ENIT NON-SPACE FILE LOC RPT SYNONYM: 5

> ENTRY ACTION: D HDR^ENSP TIMESTAMP: 60933,35507 TIMESTAMP OF PRIMARY MENU: 54540,68963

> UPPERCASE MENU TEXT: SPACE MANAGEMENT

> NAME: ENSP144 MENU TEXT: RCS 10-0141 Report

> TYPE: run routine CREATOR:

> DESCRIPTION: Report to aid in preparing CDR data for Fiscal Service.

> ROUTINE: PR144^ENSP UPPERCASE MENU TEXT: RCS 10-0141 REPORT

> NAME: ENSP2 MENU TEXT: Key/Lock Management TYPE: menu CREATOR:

> DESCRIPTION: Main driver option for Engineering Lock/key management. ITEM: ENSPEDKEY SYNONYM: 1

> ITEM: ENSPLOCK SYNONYM: 2

> ITEM: ENSPEMP SYNONYM: 3

> ITEM: ENSPKEY SYNONYM: 4

> ITEM: ENSPSRV SYNONYM: 5

> ENTRY ACTION: D HDR^ENSP ROUTINE: PRFRS^ENSP

> TIMESTAMP: 55630,56222 TIMESTAMP OF PRIMARY MENU: 54540,68963 UPPERCASE MENU TEXT: KEY/LOCK MANAGEMENT

> Exported Options

> NAME: ENSP3

> MENU TEXT: Export Facility Management Data

> TYPE: menu CREATOR: .5

> DESCRIPTION: These options will output several reports in a form suitable to capture in ASCII format to use in several popular MS-DOS PC spreadsheets for better analysis and graphic capability.

> ITEM: ENSP3-SERVICE-NSF SYNONYM: 1

> ITEM: ENSP3-FUNCTION-NSF SYNONYM: 2

> ITEM: ENSP3-RCS10-0141 SYNONYM: 3 TIMESTAMP: 55630,56191

> UPPERCASE MENU TEXT: EXPORT FACILITY MANAGEMENT DAT

> NAME: ENSP3-FUNCTION-NSF

> MENU TEXT: Output Function/NSF Spreadsheet

> TYPE: run routine CREATOR: .5

> DESCRIPTION: Output an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

> ROUTINE: FUNC^ENSP5 TIMESTAMP: 55036,67259 UPPERCASE MENU TEXT: OUTPUT FUNCTION/NSF SPREADSHEE

> NAME: ENSP3-RCS10-0141

> MENU TEXT: Output RCS 10-0141 spreadsheet

> TYPE: run routine CREATOR: .5

> DESCRIPTION: Output an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

> ROUTINE: RCS^ENSP5

> UPPERCASE MENU TEXT: OUTPUT RCS 10-0141 SPREADSHEET

> NAME: ENSP3-SERVICE-NSF

> MENU TEXT: Output Service/NSF spreadsheet

> TYPE: run routine CREATOR: .5

> DESCRIPTION: Output an ASCII file that can be captured via a smart terminal for loading into a commercial spreadsheet product.

> ROUTINE: SER^ENSP5 TIMESTAMP: 54942,75356 UPPERCASE MENU TEXT: OUTPUT SERVICE/NSF SPREADSHEET

> NAME: ENSP4

> MENU TEXT: Finish Replacement Schedules Report Menu TYPE: menu CREATOR: .5

> DESCRIPTION: Driver option for printing scheduled replacement dates for room finishes.

> ITEM: ENSPFRS1 SYNONYM: 1

> ITEM: ENSPFRS2 SYNONYM: 2

> ITEM: ENSPFRS3 SYNONYM: 3

> ITEM: ENSPFRS4 SYNONYM: 4

> ROUTINE: PRFRS^ENSP TIMESTAMP: 55630,56208 UPPERCASE MENU TEXT: FINISH REPLACEMENT SCHEDULES R

> NAME: ENSP5 MENU TEXT: Space Survey Report Menu TYPE: menu CREATOR: .5

> DESCRIPTION: Driver option for Engineering Space Reports. ITEM: ENSPRMKY SYNONYM: 1

> ITEM: ENSPRM SYNONYM: 2

> ITEM: ENSPSER SYNONYM: 3

> ITEM: ENSPFUNC SYNONYM: 4

> ITEM: ENSPBLDG SYNONYM: 5

> ITEM: ENSP144 SYNONYM: 6

> ITEM: ENSP-137-AMIS SYNONYM: 7 TIMESTAMP: 55630,56220

> UPPERCASE MENU TEXT: SPACE SURVEY REPORT MENU

> NAME: ENSPBLDG MENU TEXT: Building Space Survey TYPE: run routine CREATOR: .5

> DESCRIPTION: Prints principal fields from Engineering Space file. Sorts first by building, then by room.

> ROUTINE: PRBLDG^ENSP

> UPPERCASE MENU TEXT: BUILDING SPACE SURVEY

> Exported Options

> NAME: ENSPEDKEY

> MENU TEXT: Key Distribution by Employee Enter/Edit TYPE: run routine CREATOR: .5

> DESCRIPTION: Enter/edit list of door keys assigned to individual employees. ROUTINE: EMKY^ENSP

> UPPERCASE MENU TEXT: KEY DISTRIBUTION BY EMPLOYEE E

> NAME: ENSPEMP

> MENU TEXT: Print Key Distribution By Employee TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of employees to whom door keys have been individually assigned. Information on keys assigned is provided.

> ROUTINE: PREMP^ENSP

> UPPERCASE MENU TEXT: PRINT KEY DISTRIBUTION BY EMPL

> NAME: ENSPFRS1

> MENU TEXT: Replacement Schedule for All Finishes TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of scheduled replacement dates for walls, floors, and ceilings.

> ROUTINE: FRS4^ENSP

> UPPERCASE MENU TEXT: REPLACEMENT SCHEDULE FOR ALL F

> NAME: ENSPFRS2 MENU TEXT: Ceiling Replacement Schedule TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of scheduled ceiling replacements, by date. ROUTINE: FRS1^ENSP

> UPPERCASE MENU TEXT: CEILING REPLACEMENT SCHEDULE

> NAME: ENSPFRS3 MENU TEXT: Wall Replacement Schedule TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of scheduled wall replacements, by date. ROUTINE: FRS2^ENSP

> UPPERCASE MENU TEXT: WALL REPLACEMENT SCHEDULE

> NAME: ENSPFRS4 MENU TEXT: Floor Replacement Schedule TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of scheduled floor replacements, by date. ROUTINE: FRS3^ENSP

> UPPERCASE MENU TEXT: FLOOR REPLACEMENT SCHEDULE

> NAME: ENSPFUNC MENU TEXT: Function Space Survey TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates list of rooms sorted by designated function. ROUTINE: PRFUNC^ENSP

> UPPERCASE MENU TEXT: FUNCTION SPACE SURVEY

> Exported Options

> NAME: ENSPKEY

> MENU TEXT: Print Employee List sorted by Key TYPE: run routine CREATOR: .5

> DESCRIPTION: Prints list of all employees (if any) who have been issued door keys within a user-specified range of keys.

> ROUTINE: PRKEY^ENSP

> UPPERCASE MENU TEXT: PRINT EMPLOYEE LIST SORTED BY

> NAME: ENSPLOCK MENU TEXT: Lock Number File Enter/Edit TYPE: run routine CREATOR: .5

> DESCRIPTION: Enter/edit information on door locks, by control number. ROUTINE: KLOCK^ENSP

> UPPERCASE MENU TEXT: LOCK NUMBER FILE ENTER/EDIT

> NAME: ENSPRM MENU TEXT: Space Survey by Room TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates print-out of space data sorted by room number. ROUTINE: PRRM^ENSP

> UPPERCASE MENU TEXT: SPACE SURVEY BY ROOM

> NAME: ENSPRMKY MENU TEXT: Room/Keying/Function Report TYPE: run routine CREATOR: .5

> DESCRIPTION: Room listing with keys that open room. ROUTINE: INIT^ENSP1

> UPPERCASE MENU TEXT: ROOM/KEYING/FUNCTION REPORT

> NAME: ENSPROOM MENU TEXT: Enter New Room Space Data TYPE: run routine CREATOR: .5

> DESCRIPTION: Enter/edit of space data for any selected room using standard FileMan functionality.

> ROUTINE: SP^ENSP

> UPPERCASE MENU TEXT: ENTER NEW ROOM SPACE DATA

> NAME: ENSPROOMD MENU TEXT: Display/Edit Room Data TYPE: run routine CREATOR: .5

> DESCRIPTION: Enter/edit space data using a screen server. ROUTINE: ENT^ENSP2

> UPPERCASE MENU TEXT: DISPLAY/EDIT ROOM DATA

> NAME: ENSPSER MENU TEXT: Service Space Survey TYPE: run routine CREATOR: .5

> DESCRIPTION: Generates listing of space data sorted by owning service. Allows full listing or a summary of square foot figures only.

> ROUTINE: PRSER^ENSP

> UPPERCASE MENU TEXT: SERVICE SPACE SURVEY

> NAME: ENSPSRV

> MENU TEXT: Print Employee List by Service

> TYPE: run routine CREATOR: .5

> DESCRIPTION: List employees and keys in order by service, page break on each service. For review, by Service, of key holders

> ROUTINE: PRSRV^ENSP

> UPPERCASE MENU TEXT: PRINT EMPLOYEE LIST BY SERVICE

> Exported Options

> NAME: ENSPUTL MENU TEXT: Facility Management Utilities TYPE: menu CREATOR: .5

> DESCRIPTION: Used to edit files associated with the facility mngt package and other utilities for the package

> ITEM: ENSPUTL1 SYNONYM: 1

> ITEM: ENSPUTL2 SYNONYM: 2

> ITEM: ENSPUTL-CLEAN SYNONYM: 3

> ITEM: ENSPUTL3 SYNONYM: 4

> ITEM: ENSPUTL4 SYNONYM: 5

> TIMESTAMP: 55630,56231

> UPPERCASE MENU TEXT: FACILITY MANAGEMENT UTILITIES

> NAME: ENSPUTL-CLEAN

> MENU TEXT: Remove Dangling Pointers in LOCK file TYPE: run routine CREATOR: .5

> DESCRIPTION: Deletion of an employee name in the EMPLOYEE(KEYS) file 6926 sometimes leaves dangling pointers in the ISSUED TO field of the LOCKS file 6927.

> This can be cleaned up safely with this option. Run anytime necessary. ROUTINE: EN^ENSP4

> UPPERCASE MENU TEXT: REMOVE DANGLING POINTERS IN LO

> NAME: ENSPUTL1 MENU TEXT: Edit Space Functions file TYPE: run routine CREATOR: .5

> DESCRIPTION: Allows editing of the function file pointed to by the Space file ROUTINE: FUNC^ENSP

> UPPERCASE MENU TEXT: EDIT SPACE FUNCTIONS FILE

> NAME: ENSPUTL2 MENU TEXT: Edit Space Utilities file TYPE: run routine CREATOR: .5

> DESCRIPTION: Allows editing of the Utilities file pointed to by the Space file ROUTINE: UTL^ENSP

> UPPERCASE MENU TEXT: EDIT SPACE UTILITIES FILE

> NAME: ENSPUTL3 MENU TEXT: Building File Enter/Edit TYPE: edit CREATOR: .5

> DESCRIPTION: Use this option to maintain the Eng Building file (#6928.3). The BUILDING (or BUILDING-DIVISION) portion of the ROOM NUMBER field of entries in the Eng Space file must match an entry in this Eng Building file.

> Limited fields will be presented if the building ownership is listed as PLANNED. DIC {DIC}: ENG(6928.3, DIC(0): AEMQL

> DIE: ENG(6928.3, DR {DIE}: \[ENSP-BLDG-P\] UPPERCASE MENU TEXT: BUILDING FILE ENTER/EDIT

> NAME: ENSPUTL4 MENU TEXT: Print All Building Data TYPE: print CREATOR: .5

> DESCRIPTION: Print all Building Data from ENG BUILDING file DIC {DIP}: ENG(6928.3, L.: 0

> FLDS: \[CAPTIONED\] BY: @.01;S1 DHD: REPORT OF ALL BUILDING DATA

> UPPERCASE MENU TEXT: PRINT ALL BUILDING DATA

> Exported Options

> NAME: ENSWOPT MENU TEXT: SOFTWARE OPTIONS Enter/Edit TYPE: edit CREATOR: 187

> DESCRIPTION: Enables user to choose the manner in which selected AEMS/MERS features will operate at his/her site.

> DIC {DIC}: ENG(6910.2, DIC(0): AEQM

> DIE: ENG(6910.2, DR {DIE}: \[ENSWOPT\] UPPERCASE MENU TEXT: SOFTWARE OPTIONS ENTER/EDIT

> NAME: ENWCLERK MENU TEXT: Engineering Work Control Clerk Main Menu

> TYPE: menu CREATOR: 187

> DESCRIPTION: This Menu is set up for the Work Order Clerk ITEM: ENWO SYNONYM: 1

> ITEM: DIUSER SYNONYM: 2

> EXIT ACTION: D EXIT^EN ENTRY ACTION: D INIT^EN,HDR^EN

> TIMESTAMP: 55586,57261 TIMESTAMP OF PRIMARY MENU: 53501,40523 UPPERCASE MENU TEXT: ENGINEERING MAIN MENU

> NAME: ENWO MENU TEXT: Work Order & MERS TYPE: menu CREATOR: 187

> DESCRIPTION: Main driver for Work Order module. ITEM: ENWONEW SYNONYM: 1

> ITEM: ENENT SYNONYM: 2

> ITEM: ENDSY SYNONYM: 4

> ITEM: ENEQHID SYNONYM: 7

> ITEM: ENWOCLOSE SYNONYM: 3

> ITEM: ENWO-STATUS-(XQ) SYNONYM: 5

> ITEM: ENWO-TRANSFER SYNONYM: 6

> ITEM: ENWODISAP SYNONYM: 8

> ITEM: ENWOREP SYNONYM: 9

> ITEM: ENPMHOURS SYNONYM: 10

> EXIT ACTION: K ENSHKEY ENTRY ACTION: D HDR^ENWO

> TIMESTAMP: 55613,31493 UPPERCASE MENU TEXT: WORK ORDER & MERS

> NAME: ENWO-STATS-DPT

> MENU TEXT: Incomplete W.O. Status by Owner/Department TYPE: run routine CREATOR: 187

> DESCRIPTION: List of incomplete work requests by requesting service. ROUTINE: O^ENWOST

> UPPERCASE MENU TEXT: INCOMPLETE W.O. STATUS BY OWNE

> NAME: ENWO-STATS-EMP

> MENU TEXT: Incomplete W.O. Status by Employee TYPE: run routine CREATOR: 187

> DESCRIPTION: List of incomplete work requests by assigned technician. User is prompted to select the ENGINEERING EMPLOYEE of interest, from among those who belong to the chosen shop. If you simply press \<RETURN\> instead of selecting a technician, the system will then allow you to enter the word 'NOT' and thereby produce a list of incomplete work orders that are not assigned to anyone.

> ROUTINE: E^ENWOST

> UPPERCASE MENU TEXT: INCOMPLETE W.O. STATUS BY EMPL

> NAME: ENWO-STATS-LOC

> MENU TEXT: Incomplete W.O. Status by Location TYPE: run routine CREATOR: 187

> DESCRIPTION: List of incomplete work requests by location. ROUTINE: L^ENWOST

> UPPERCASE MENU TEXT: INCOMPLETE W.O. STATUS BY LOCA

> NAME: ENWO-STATS-SHOP

> MENU TEXT: Incomplete W.O. Status by Shop

> TYPE: run routine CREATOR: 187

> DESCRIPTION: List of incomplete work requests by assigned Engineering Section. ROUTINE: S^ENWOST

> UPPERCASE MENU TEXT: INCOMPLETE W.O. STATUS BY SHOP

> Exported Options

> NAME: ENWO-STATUS-(HC) MENU TEXT: Incomplete Work Order Status TYPE: run routine CREATOR: 187

> DESCRIPTION: Driver for Incomplete Work Order Status reports using hard code. ROUTINE: ENWOST

> UPPERCASE MENU TEXT: INCOMPLETE WORK ORDER STATUS

> NAME: ENWO-STATUS-(XQ) MENU TEXT: Incomplete Work Order Status TYPE: menu CREATOR: 187

> DESCRIPTION: Driver for Incomplete Work Order Status reports using menu options.

> UPPERCASE MENU TEXT: INCOMPLETE WORK ORDER STATUS

> NAME: ENWO-TRANSFER MENU TEXT: Transfer W.O. to Another Shop TYPE: run routine CREATOR: 187

> DESCRIPTION: Transfer an existing Work Request from one Engineering Section to another. ROUTINE: TRANS^ENWONEW1

> UPPERCASE MENU TEXT: TRANSFER W.O. TO ANOTHER SHOP

> NAME: ENWOCLOSE MENU TEXT: Close Out Work Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Close out an open work request. Entry of DATE COMPLETE removes a work order from the incomplete list.

> ROUTINE: CLSOUT^ENWO1

> UPPERCASE MENU TEXT: CLOSE OUT WORK ORDER

> NAME: ENWODISAP MENU TEXT: Disapprove Work Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Use this option to record disapproval action on a work request. It is anticipated that this option will be most useful at facilities which allow entry of work requests into AEMS/MERS by personnel outside of Engineering Service.

> ROUTINE: DISAP^ENWO2

> UPPERCASE MENU TEXT: DISAPPROVE WORK ORDER

> NAME: ENWOEDIT-WARD MENU TEXT: Edit Electronic Work Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Permits non-Engineering users to edit work requests which were input via the 'Electronic Work Order Request' option. Once work orders have been transferred by Engineering Service to a working shop they may no longer be edited via this option, but users may check their status.

> ROUTINE: WRDEDT^ENWARD

> UPPERCASE MENU TEXT: EDIT ELECTRONIC WORK ORDER

> Exported Options

> NAME: ENWONEW MENU TEXT: Enter New Work Order TYPE: run routine CREATOR: 187

> DESCRIPTION: Enter a new work request. Option requires knowledge of which shop (Engineering Section) should receive the assignment.

> ENTRY ACTION: D SSHOP^ENWO S:ENSHKEY'\>0 XQUIT="" ROUTINE: ENG^ENWONEW

> UPPERCASE MENU TEXT: ENTER NEW WORK ORDER

> NAME: ENWONEW-WARD MENU TEXT: Request Electronic Work Order TYPE: action CREATOR: 187

> DESCRIPTION: Entry of Engineering work requests by non-Engineering personnel. Intent is to reduce volume of written work orders and to reduce telephone calls to Engineering Work Control desk. Assumes that AEMS/MERS has been integrated with CORE systems so that all DHCP users have access to the Engineering package.

> EXIT ACTION: K ENSHKEY

> ENTRY ACTION: S ENDR=\$S(\$D(^DIE("B","ENZWOWARD")):"\[ENZWOWARD\]",1:"\[ENWOWARD\]"

> ) D INIT^EN,WARD^ENWONEW

> UPPERCASE MENU TEXT: REQUEST ELECTRONIC WORK ORDER

> NAME: ENWOREP

> MENU TEXT: Reprint Work Orders (All Shops)

> TYPE: run routine CREATOR: 187

> DESCRIPTION: Reprints work orders entered within a user selected date range. The 'date portion' of the Work Order Number is used to determine when work orders are entered. Work orders from all shops will be included. The intent of the option is to give users a means of batch printing at the end of each day all work orders entered during the day.

> ROUTINE: ENWOREP

> UPPERCASE MENU TEXT: REPRINT WORK ORDERS (ALL SHOPS

> NAME: ENWORK ACTION MENU TEXT: Work Action TYPE: edit CREATOR: 187

> DESCRIPTION: edit work action file

> DIC {DIC}: ENG(6920.1, DIC(0): "AEQM"

> DIE: ENG(6920.1, DR {DIE}: 1 UPPERCASE MENU TEXT: WORK ACTION

> NAME: ENWORK CTR

> TYPE: run routine

> DESCRIPTION: edit work center code ROUTINE: WCC^ENMAN

> MENU TEXT: Work Center Code CREATOR: 187

> UPPERCASE MENU TEXT: WORK CENTER CODE

> NAME: ENWOST-WARD

> MENU TEXT: Incomplete Work Orders (ELECT WO MODULE) TYPE: run routine CREATOR: 187

> DESCRIPTION:

> Lists incomplete work orders. Will list by:

1.  Person who originally entered work request, or
2.  Service/Section, or
3.  Location of work.

> Developed in support of electronic work request module (ward work orders). ROUTINE: SE^ENWARD1

> UPPERCASE MENU TEXT: INCOMPLETE WORK ORDERS (ELECT

> Exported Options

> NAME: ENWOSTATUS-WARD

> MENU TEXT: Electronic Work Order Status Check TYPE: run routine CREATOR: 187

> DESCRIPTION: Enables users outside of Engineering Service to view the status of work orders, including those entered as Electronic Work Order Requests. This option does not allow any changes to be made to the work order record.

> ROUTINE: WRDCK^ENWARD

> UPPERCASE MENU TEXT: ELECTRONIC WORK ORDER STATUS C

> NAME: ENWOWARD MENU TEXT: Electronic Work Requests TYPE: menu CREATOR: 187

> DESCRIPTION: Main option for entry and status checking of Engineering work requests by DHCP users outside of Engineering Service.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ITEM: ENWOEDIT-WARD</p>
</blockquote></th>
<th><blockquote>
<p>SYNONYM: 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENWONEW-WARD</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYM: 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: ENWOSTATUS-WARD</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYM: 3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITEM: ENWOST-WARD</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYM: 4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIMESTAMP: 55586,57324</p>
</blockquote></td>
<td><blockquote>
<p>TIMESTAMP OF PRIMARY MENU: 53998,40903</p>
</blockquote></td>
</tr>
</tbody>
</table>

> UPPERCASE MENU TEXT: ELECTRONIC WORK REQUESTS

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Cross-references can be retrieved using the List File Attributes option in FileMan. If further explanation is required, see the On-Line Documentation section in this Manual.

> Cross References

> The following cross-references were introduced by Patch EN\*7.0\*100 for support of the Real Time Location System (RTLS) interface. The files modified were the ENGINEERING INV. file (#6914) and ENG SPACE file (#6928).

> TRADITIONAL CROSS-REFERENCE LIST -- FILE \#6914 05/18/16 PAGE 1

> New MUMPS cross-references added to support the RTLS interface with Engineering are listed below.

> The Description field of PHYSICAL INVENTORY DATE (#23) and LOCATION (#24) were expanded to include a note about the role of RTLS in updating the fields. The ‘AB’ cross-reference on the field \#.01 of the Responsible Shop multiple was updated with new text to explain its function.

> File \#6914

> Traditional Cross-References:

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>A1</p>
</blockquote></th>
<th><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></th>
<th><blockquote>
<p>ACQUISITION DATE (6914,13)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the AQUISITION DATE is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A2</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY STOCK NUMBER (6914,18)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the CATEGORY STOCK NUMBER is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A3</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>CMR (6914,19)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the CMR is changed a notification is sent out to update the Real Time Location System (RTLS) database. 1)= D WC^VIAATRI(6914,DA)</p>
<p>2)= D WC^VIAATRI(6914,DA)</p>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A4</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>USE STATUS (6914,20)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the USE STATUS is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A5</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE POINTER (6914,21)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the SERVICE POINTER is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol></td>
</tr>
</tbody>
</table>

> NOREINDEX)= 1

> Subfile \#6914.04

> Traditional Cross-References:

> A6 MUMPS WHOLE FILE (#6914)

> Field: RESPONSIBLE SHOP (6914.04,.01)

> Description: After the RESPONSIBLE SHOP is changed a notification is sent out to update the Real Time Location System (RTLS) database.

1.  = D WC^VIAATRI(6914,DA(1))
2.  = D WC^VIAATRI(6914,DA(1))

> NOREINDEX)= 1

> AB REGULAR WHOLE FILE (#6914)

> Field: RESPONSIBLE SHOP (6914.04,.01)

> Description: This cross reference keeps track of the Engineering Section shop responsible for performing maintenance on a given piece of equipment.

> 1)= S ^ENG(6914,"AB",\$E(X,1,30),DA(1),DA)=""

> 2)= K ^ENG(6914,"AB",\$E(X,1,30),DA(1),DA)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>A7</p>
</blockquote></th>
<th><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></th>
<th><blockquote>
<p>STATION NUMBER (6914,60)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the STATION NUMBER is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A8</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>PARENT SYSTEM (6914,2)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the PARENT SYSTEM is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A9</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>MFGR. EQUIPMENT NAME (6914,3)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the MFGR. EQUIPMENT NAME is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> A10 MUMPS

> Field: DISPOSITION DATE (6914,22)

> Description: After the DISPOSITION DATE is changed a notification is sent out to update the Real Time Location System (RTLS) database.

1)  = D WC^VIAATRI(6914,DA)
2)  = D WC^VIAATRI(6914,DA)

> NOREINDEX)= 1

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AS</p>
</blockquote></th>
<th><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></th>
<th><blockquote>
<p>ENTRY NUMBER (6914,.01)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the ENTRY NUMBER is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AT</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>MANUFACTURER (6914,1)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the MANUFACTURER is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AU</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>MODEL (6914,4)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the MODEL is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AV</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>SERIAL # (6914,5)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the SERIAL # is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AW</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENT CATEGORY (6914,6)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the EQUIPMENT CATEGORY is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AX</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF ENTRY (6914,7)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the TYPE OF ENTRY is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AY</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
<p>Field:</p>
</blockquote></td>
<td><blockquote>
<p>PURCHASE ORDER # (6914,11)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>Description:</td>
<td><blockquote>
<p>After the PURCHASE ORDER # is changed a notification is sent out to update the Real Time Location System (RTLS) database.</p>
</blockquote>
<ol type="1">
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
<li><p>= D WC^VIAATRI(6914,DA)</p></li>
</ol>
<blockquote>
<p>NOREINDEX)= 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AZ</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Field: TOTAL ASSET VALUE (6914,12)

> Description: After the TOTAL ASSET VALUE is changed a notification is sent out to update the Real Time Location System (RTLS) database.

1)  = D WC^VIAATRI(6914,DA)
2)  = D WC^VIAATRI(6914,DA)

> NOREINDEX)= 1

> Fields in File \#6914 with DESCRIPTION text added. Notice the reference to RTLS in the text added.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 24%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>DATA</th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>GLOBAL</p>
</blockquote></th>
<th><blockquote>
<p>DATA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ELEMENT</td>
<td><blockquote>
<p>TITLE</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 6914,23 PHYSICAL INVENTORY DATE 2;13 DATE

> INPUT TRANSFORM: S %DT="E",%DT(0)="-NOW" D ^%DT K %DT S X=Y K:Y\<

> 1 X

> LAST EDITED: SEP 24, 2013

> HELP-PROMPT: Future dates are not allowed.

> DESCRIPTION: Date of last physical inventory of this item (CMR reconciliation). Intent is to populate this field automatically via physical inventory software using bar code technologies.

> Completion of a Preventive Maintenance Inspection will also update this field, provided that the PM STATUS does not contain 'DEFERRED'.

> For equipment with an RTLS tag ID defined, the physical inventory date is generated by RTLS tag readers.

> 6914,24 LOCATION 3;5 POINTER TO ENG SPACE FILE (#6928)

> LAST EDITED: SEP 24, 2013

> HELP-PROMPT: Enter as ROOM-BUILDING (or select a SYNONYM).

> DESCRIPTION: Physical location of this item at the facility.

> For equipment being tracked by RTLS, the location is populated by the AEMS-MERS RTLS interface.

> =============================================================================== INDEX AND CROSS-REFERENCE LIST -- FILE \#6928, FIELD \#.01 05/18/16 PAGE 1

> Traditional Cross-References:

> AG MUMPS

> Field: ROOM NUMBER (6928,.01)

> Description: After the ROOM NUMBER is changed a notification is sent out to update the Real Time Location System (RTLS) database.

1)  = D WC^VIAATRI(6928,DA)
2)  = D WC^VIAATRI(6928,DA)

> NOREINDEX)= 1

> <span id="_bookmark20" class="anchor"></span>6916 6912 420.24106920.1

> 69206914.26911

> 6914

> 420.8

> 4406921

> 441.2

> 6917

> 6910 6922

> 6910.1

> 6929 420.1

> 6914.13.56919200

> 49 6926

> 6910.2

> 6919.1

> 6928.1 6928 6927

> 6910.5

> 6919.2

> 6928.2

> 6928.3

> 6910.9

> 6925 7335.7

> 6924

> 4

> 7336.9 7336.6

> 7336.8

> 7336.3

> 6249.1 6924.2 6924.3

> File Diagram

# Archiving/Purging Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Engineering Archive module presently services the Work Order and 2162 Accident Report files. It allows individual records to be stored on tape and then purged from the disk.

> Pointers to external files are replaced by the equivalent text before records are saved to tape.

> Data definitions are stored on the same tapes as the records themselves. The Recall option uses these data definitions to automatically construct a temporary file for the storage and display of archived records. VA FileMan may be used to print information from these temporary files. There is no provision for restoring archived records back into the production file from which they were extracted.

> Find & Assemble Records

> Searches the database to find the individual records to be archived, moves them to an archive global, and simultaneously purges them from the production file. The user is asked for record type, station number, and sort parameters. Records may be archived for an entire fiscal year, or a specific quarter. Completed work orders may be archived by shop (all shops, one shop, or all shops but one). Since this function actually purges data from disk, you may wish to backup your system before executing "Find and Assemble Records".

> Archive & Verify Records

> Moves a collection of records (archive set) from the archive global to tape. This function should be executed immediately after "Find and Assemble Records".

> Delete Archive Global

> Kills the archive global, which may be thought of as a temporary storage area. The archive global holds records in the process of being archived, as well as records that have been recalled from an archive tape for inspection via VA FileMan. "Delete Archive Global" should be executed after "Archive and Verify" and after "Recall Archive Global" (once the recalled records have been inspected and/or printed).

> Recall Archive Global

> Restores records from an archive tape into the archive global, where they may be examined via VA FileMan. The user may recall an entire tape or search a tape for a specific record.

> Review Activity Log

> Displays a chronological listing of everything that has been done with a given archive set.

> Archiving/Purging Data

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are two supported entry points in the Engineering package.

> PO^ENLIB2

> This entry point may be called to populate selected data elements in the Equipment file using information obtainable from the purchase order. These data elements are FUND CONTROL POINT, COST CENTER, SUBACCOUNT, VENDOR, SERVICE, and SOURCE CODE.

> There are two required variables.

> X must contain the purchase order number

> DA must contain the equipment entry number (IEN)

> ACCX^ENLIB2

> This entry point may be called to update the STATUS of a Work Order based on information contained in an associated Control Point Activity Transaction.

> There is one required variable.

> X must contain the internal entry number (IEN) of the work order to be updated

> Callable Routines

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 7.0 of Engineering requires these versions (or later) of the following DHCP CORE packages: VA Kernel Version 6.5;

> VA FileMan Version 18.0; and VA MailMan Version 3.1

> There is an integration agreement between Engineering and IFCAP.

1.  IFCAP and Engineering may share the Barcode Program file (446.4), Engineering has permission to distribute this file, but IFCAP has control over it.
2.  Entry of an Engineering work order in the SORT GROUP field of the Control Point Activity file will automatically update the work order STATUS. This is accomplished via a call to entry point ACCX^ENLIB2.
3.  Entry of a Control Point Activity Transaction in the PARTS ORDERED field of the Work Order file will enable users to view (but not to edit) the Control Point Activity from the Engineering Work Order module. This is accomplished via a call to entry point ^PRCSP13.

> External Relations

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All bottom-level menu options in the Engineering package are independent and can stand alone.

> Internal Relations

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The SACC has approved ENLO, ENHI and ENSHKEY as package-wide variables.

1.  STANDARD SECTION: 4B Package-wide variables DATE GRANTED: SEP 21,1989

> ENLO, ENHI, and ENSHKEY are package-wide variables for use in the Engineering package.

2.  STANDARD SECTION: 5D1 Line format, 1st line DATE GRANTED: OCT 11,1989

> Engineering routines that contain data definitions used in package specific archiving may have first line tags that differ from the routine name. These routines are automatically renamed by routine

> ENARG1 prior to their actual use and are in compliance with the SACC at that time.

> Package-Wide Variables

# On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is recommended that you print the Engineering package data dictionaries immediately after you load the software. This is done through the VA FileMan option "List File Attributes". The file range for the Engineering package is 6910 - 6929, inclusive; and files 7330 - 7339.9. You may specify

> a Standard or Brief Data Dictionary as your needs require.

> The first part of each Data Dictionary (in a Standard listing) is a list of other files that point to Medicine file fields. The second part is a listing of the Cross-references for that file and a brief description of its purpose.

> To learn more about the options for the Engineering package, one may either print a more detailed option list (including things such as entry/exit actions, Menu type, etc.) or D ^XUP, select XUMAINT, and then select a specific option.

> Usng on-line documentation is the best way to obtain the most current information available. Further information for generating On-line documentation is provided in the Kernel documentation. This can be obtained either from your IRM or your local ISC.

> On-line Documentation

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ALD - Abbreviation for appropriation, limitation, department.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CMR - Consolidated Memorandum of Receipt. The basic instrument by which accountability for capital equipment is recorded.
> Configuration-A particular selection of hardware and software resources that are tailored to provide optimum usage of ADP systems. This includes the type of CPU, type and number of disk drives, type and number of terminals, amount of main storage and so on.
> Criticality - An index used by the package to rank the importance of performing preventive maintenance inspections on a particular device.
> DHCP - Decentralized Hospital Computer Program-The name of the effort to install computer systems in the Veterans Administration Department of Medicine and Surgery's hospitals.
> FileManager - Also known as VA FileMan. A set of MUMPS routines used to enter, maintain, access and manipulate related data in a file. It is the basic system
> used by all VA applications in creating files.
> Information Systems Center (ISC) - One of the VA's seven regional offices for the management and development of application software. The ISCs are also responsible for providing support to field sites and for training personnel.
> IRL - Interactive Reader Language. Proprietary language used by the Intermec line of
> portable bar code readers.
> IT – Information Technology.
> MailMan - An electronic mail, teleconferencing, and networking system which is an integral part of the Kernel.
> MUMPS - Massachusetts General Hospital Utility Multi-Programming System.
> This is
> the computer language used by all VA DHCP applications.
> Glossary
> NXRN# - A sequential number assigned by centralized CMR Management System in
> Austin.
> Service Pointer - The functional entity (generally a service) within the facility that uses the device.
> Site Configurable - A term used to refer to features in the system which can be tailored
> according to the needs of particular sites.
