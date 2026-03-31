---
title: EN Version 7 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
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
description: - [## Introduction](#introduction) - [Related Manuals](#related-manuals) - [Functional Description](#functional-description) - [Orientation](#orientation) - [Standard Conventions](#standard-conventions) - [Menu Structure](#menu-structure) - [Package Management](#package-management) - [Special Menu O
audience: 
keywords: 
  - equipment
  - work
  - project
  - number
  - order
  - date
  - edit
  - code
  - report
  - engineering
page_count: 0
word_count: 97394
section_count: 16
table_count: 144
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 2
revision_newest: 06/11/97
revision_oldest: 06/11/97
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/EN_7_0_UM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/EN_7_0_UM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=37"
---

## Table of Contents

  - [## Introduction](#introduction)
    - [Related Manuals](#related-manuals)
    - [Functional Description](#functional-description)
  - [Orientation](#orientation)
    - [Standard Conventions](#standard-conventions)
    - [Menu Structure](#menu-structure)
  - [Package Management](#package-management)
    - [Special Menu Options](#special-menu-options)
    - [A&MM Nonexpendable Equipment Options](#amm-nonexpendable-equipment-options)
    - [Generation of On-line Documentation](#generation-of-on-line-documentation)
  - [Package Operation](#package-operation)
    - [VistA Engineering Work Order Module](#vista-engineering-work-order-module)
  - [Year Facility Plan and Project Applications](#year-facility-plan-and-project-applications)
    - [Five Year Facility Plan (FYFP) Menu](#five-year-facility-plan-fyfp-menu)
    - [Edit 5-Yr Plan Project.](#edit-5-yr-plan-project)
    - [Activations E/E](#activations-ee)
    - [Five Year Facility Plan Report (132 columns)](#five-year-facility-plan-report-132-columns)
    - [Validate 5-Yr Plan Projects.](#validate-5-yr-plan-projects)
    - [Communication Log](#communication-log)
    - [Transmit 5-Yr Plan Projects.](#transmit-5-yr-plan-projects)
    - [Project Applications](#project-applications)
    - [Activations E/E](#activations-ee-1)
    - [Environmental Analysis E/E (VAF 10-1193a)](#environmental-analysis-ee-vaf-10-1193a)
    - [Approval of Project Application](#approval-of-project-application)
    - [Reports](#reports)
    - [Validate Project Applications](#validate-project-applications)
    - [Transmit Project Applications](#transmit-project-applications)
    - [Communication Log Display for a Project](#communication-log-display-for-a-project)
  - [Project Tracking](#project-tracking)
    - [Enter Project Data](#enter-project-data)
    - [Screen Review All Data](#screen-review-all-data)
    - [Preliminary Data Screen](#preliminary-data-screen)
    - [Approved Dates Screen Edit.](#approved-dates-screen-edit)
    - [Revised Dates Screen Edit](#revised-dates-screen-edit)
    - [Actual Dates Screen Edit.](#actual-dates-screen-edit)
    - [A/E-Contractor Data Screen Edit](#ae-contractor-data-screen-edit)
    - [Contractor Data Screen Edit](#contractor-data-screen-edit)
    - [Changes & Remarks Screen Edit](#changes-remarks-screen-edit)
    - [Print Project Status Report](#print-project-status-report)
    - [Print All Project Status Reports](#print-all-project-status-reports)
    - [Transmit 10-0051 Electronically](#transmit-10-0051-electronically)
  - [Equipment Management](#equipment-management)
    - [New Inventory Entry](#new-inventory-entry)
    - [Multiple Inventory Entry.](#multiple-inventory-entry)
    - [Inventory Edit.](#inventory-edit)
    - [Display Equipment Record](#display-equipment-record)
    - [PM Parameters](#pm-parameters)
    - [Generate PM Schedule](#generate-pm-schedule)
    - [Record Equipment PMI](#record-equipment-pmi)
    - [Print Bar Code Labels for Equipment Management](#print-bar-code-labels-for-equipment-management)
    - [Bar Coded Equipment Inventory Management](#bar-coded-equipment-inventory-management)
    - [Purchase Order Group Edit](#purchase-order-group-edit)
    - [Lockout/Tagout Enter/Edit](#lockouttagout-enteredit)
    - [Turn-In/Disposition Equipment](#turn-indisposition-equipment)
    - [Equipment Enter/Edit (NX)](#equipment-enteredit-nx)
    - [Equipment Management Reports (NX)](#equipment-management-reports-nx)
    - [Bar Code Features (NX Equipment)](#bar-code-features-nx-equipment)
    - [NX (Nonexpendable Equipment) Utilities](#nx-nonexpendable-equipment-utilities)
    - [FAP Documents (Code Sheets)](#fap-documents-code-sheets)
    - [Fixed Assets Reports](#fixed-assets-reports)
    - [Import Utility](#import-utility)
  - [Program Management](#program-management)
    - [Engineering Computer Port](#engineering-computer-port)
    - [Section List](#section-list)
    - [Work Center Code](#work-center-code)
    - [Engineering Employee File](#engineering-employee-file)
    - [Enter/Edit Equipment Category PM Schedule](#enteredit-equipment-category-pm-schedule)
    - [Manufacturer](#manufacturer)
    - [Eng Site Parameters Enter/Edit](#eng-site-parameters-enteredit)
    - [Software Options Enter/Edit](#software-options-enteredit)
    - [Engineering Archive Module](#engineering-archive-module)
    - [Biomedical Engineering Resource Survey](#biomedical-engineering-resource-survey)
    - [Work Action](#work-action)
  - [Space/Facility Management](#spacefacility-management)
    - [Space Management](#space-management)
    - [Key/Lock Management](#keylock-management)
    - [Export Facility Management Data](#export-facility-management-data)
    - [Facility Management Utilities](#facility-management-utilities)
    - [Leased Space Options](#leased-space-options)
    - [Planning Space Program Menu](#planning-space-program-menu)
  - [Report of Accident](#report-of-accident)
    - [Enter 2162 Report](#enter-2162-report)
    - [Display 2162 Report](#display-2162-report)
    - [Edit 2162 Report](#edit-2162-report)
    - [Summary Reports (options 5-8)](#summary-reports-options-5-8)
  - [Assign (Transfer) Electronic Work Orders](#assign-transfer-electronic-work-orders)
  - [IT Equipment Module](#it-equipment-module)
    - [Inventory Edit (IT)](#inventory-edit-it)
    - [Non-Space File Location Report](#non-space-file-location-report)
    - [IT Equipment Responsibility](#it-equipment-responsibility)
    - [Assign Responsibility](#assign-responsibility)
    - [Terminate Responsibility](#terminate-responsibility)
    - [Transfer Responsibility](#transfer-responsibility)
    - [Certify Hard Copy Signature](#certify-hard-copy-signature)
    - [Print Hand Receipt for an Individual](#print-hand-receipt-for-an-individual)
    - [Add Entry to New Person File](#add-entry-to-new-person-file)
    - [IT Equipment Report Menu](#it-equipment-report-menu)
    - [Individual Responsibility for IT Assets Report](#individual-responsibility-for-it-assets-report)
    - [Unassigned IT Asset Report](#unassigned-it-asset-report)
    - [Assignments Pending Acceptance Report](#assignments-pending-acceptance-report)
    - [Tracked IT Assets Report](#tracked-it-assets-report)
    - [Signature Exception Report](#signature-exception-report)
    - [Assignment Inquiry](#assignment-inquiry)
    - [IT Owner Menu](#it-owner-menu)
  - [Glossary](#glossary)
  - [Appendices](#appendices)
    - [A.1. Electronic Work Orders](#a1-electronic-work-orders)
    - [A.2. Using Portable Bar Code Readers and Electrical Safety Analyzers with VISTA](#a2-using-portable-bar-code-readers-and-electrical-safety-analyzers-with-vista)
    - [A.3. Downloading and Uploading](#a3-downloading-and-uploading)
    - [A.4. Bar Code Based Equipment Inventory of Nonexpendable (NX) Equipment and Preventive Maintenance Inspections](#a4-bar-code-based-equipment-inventory-of-nonexpendable-nx-equipment-and-preventive-maintenance-inspections)
    - [A.5. Using the Bar Code Functions](#a5-using-the-bar-code-functions)
    - [A.6. Electrical Safety Analyzer Interface](#a6-electrical-safety-analyzer-interface)
  - [Index](#index)
---
title: |
  Engineering
  User Manual
---
![](en-version-7-user-manual/001.png)
October 2024
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
Preface
This User Manual presents the major features of the Engineering system, utilizing the system screens and menus. This manual may be used by anyone having access to the system, from a novice user to a system manager, as a quick reference text and as a guide to understanding the package as a whole.
Revision History
Initiated on 12/29/04.
<table>
<caption><p>Table 1: 5-Yr Plan Project E/E</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 51%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description (Patch # if applicable)</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/16/24</td>
<td>1.4</td>
<td><p>Updated with patch EN*7.0*106</p>
<ul>
<li><p>Added PENT-ANNUAL and QUAD-ANNUAL options to the Data Dictionary in <a href="#PENT_ANNAUL_QUAD_ANNUAL">Section 7.5.4</a></p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/15/24</td>
<td>1.3</td>
<td><p>Updated with patch EN*7.0*105</p>
<ul>
<li><p>Added section 7.19 <a href="#import-utility">Import Utility</a></p></li>
<li><p>Updated entire manual to VA documentation standards.</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>04/2008</td>
<td>1.2</td>
<td><p>Updated with Patch EN*7*87,</p>
<p>IT EQUIPMENT TRACKING ENHANCEMENT</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.1</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.0</td>
<td>Pdf file checked for accessibility to readers with disabilities.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>
Table 1: 5-Yr Plan Project E/E
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Engineering package, otherwise known as Automated Engineering Management System /Medical Equipment Reporting System (AEMS/MERS) was released on a national basis in 1985. It is the outgrowth of work that was begun at the ANYCITY VA Medical Center in the late 1970s.

In September of 1988, Engineering Service and the Office of Acquisition and Materiel Management (A&MM) jointly decided that the Engineering Equipment file should become a shared resource. This version of Engineering includes all data elements required for establishing and maintaining Integrated Supply Management System (ISMS) nonexpendable equipment records.

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Engineering package frequently invokes VA Kernel Version 6.5 or later and VA FileMan Version 18.0 or later for device selection, task queuing, data entry, and data presentation. Users who are unfamiliar with VA Kernel and/or VA FileMan are advised to consult the appropriate VA Kernel and/or VA FileMan reference manuals. Technical aspects of the Engineering package are addressed in the Engineering Technical Manual.

### Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VISTA Engineering package consists of nine (9) separate but interrelated modules.

1.  Work Order and MERS
2.  Project Planning
3.  Project Tracking
4.  Equipment Management
5.  Space/Facility Management
6.  Program Management
7.  2162 Accident Reporting
8.  Assign (Transfer) Electronic Work Orders
9.  IT Equipment Tracking

Work Order and MERS

The Work Order and MERS module generates control numbers for Engineering work requests and provides a means for assigning work requests to specific Engineering shops, assigning personnel to work orders, and charging work orders to specific pieces of equipment. It is the basis for automated repair histories on all types of equipment. Although preventive maintenance inspections are scheduled and recorded using the Equipment Management module, the actual PM work orders that constitute a PM worklist are physically stored in the Work Order file. Special

options exist for displaying incomplete work orders and for transferring electronic work orders (work requests typed into VISTA by end-users and not by Engineering) from a "receiving area" to a working shop.

#### Project Planning

The Project Planning module provides enter/edit options for information that appears on the 5-Year Plan for each project; information required for forms VAF 10- 1193; VAF 10-1193a; and NRM, Minor, and Minor Misc. Prioritization Scoring Sheets.

The Approval of Project Application option controls the Chief Engineer's and VAMC Director's sign off on the project application. The security key ENPLK001 controls the Chief Engineer's approval. The security key ENPLK002 controls the VAMC Director's approval. The Chief Engineer must sign off before the VAMC Director.

Both must approve before the project application can be transmitted electronically to higher approval authorities.

The Report/Print Menu options provide printouts of the reports and forms required by project planning.

The Electronic Transmission Menu contains options for electronic transmission of the 5-Year Plan and Project Application data elements.

#### Project Tracking

The Project Tracking module is used to record significant events during construction and non-recurring maintenance projects when the management of such a project has been delegated to the facility. Selected data elements are extracted from the Construction Project file and electronically transmitted to the Regional Construction Office and VACO. In this way, up-to-date project tracking information is made available to all interested parties with a minimum of data entry.

The content of the most recent electronic project progress report is always available for reference. Printouts of progress reports will include an asterisk beside data that differs from what was previously reported. If progress reports are directed to a CRT, changes will be highlighted.

#### Equipment Management

The Equipment Management module contains the options to maintain inventory and preventive maintenance information, print bar code labels, download control programs to portable bar code readers, upload data from portable bar code readers to VISTA, and to manage CMR (Consolidated Memoranda of Receipt).

Equipment records generally exist for non-expendable personal property, building service equipment, and for equipment that is classified as expendable from the

Introduction

materiel management point of view but which must be periodically inspected by Engineering. These inspections are necessary to satisfy the requirements of JCAHO (Joint Commission on the Accreditation of Healthcare Organizations) and/or other regulatory bodies. The Equipment Management module includes all options necessary for establishing and maintaining a comprehensive preventive maintenance program. Bar coding is now an integral part of the equipment management strategies.

The reports available through the Equipment Management module include:

- Repair histories,
- CMR listings,
- Aggregated repair histories (by Equipment Category),
- Warranty expiration listings,
- Equipment replacement listings,
- Equipment with high failure rates,
- Preventive maintenance workload (by shop).

The Equipment Management module is tightly coupled to the Work Order module. Equipment histories are automatically updated as work orders are closed out.

Redundant data entry is avoided whenever possible.

Although entries in the equipment repair histories are most commonly made by the system when work orders are closed out, users can also make entries without going through the Work Order module. Equipment records to be updated by direct posting may be selected individually or they may be contained in a VA FileMan sort template. If a sort of template is used, it must begin with "ENPOST."

#### Program Management

The Program Management module contains options for site-specific population and/or maintenance of files used in the Engineering package. This option is only available to the Engineering Applications Manager or Engineering Site Manager. It is where the various lists are established and maintained. The Engineering Employee file and the Equipment Category list must be maintained on a continuing basis. Populated copies of the Equipment Category file are available from your supporting ISC upon request.

#### Space/Facility Management

The Space/Facility Management module is used to maintain data on physical locations within the host facility (usually a VA Medical Center). Data elements include square footage; wall, ceiling and floor finishes; window types and treatments; and other architectural features. This module also provides control of locks and keys throughout a facility. Bar coded location labels are printed from the Space file based on room number. Facilities that intend to take advantage of the bar code features in the Equipment Management module should ensure that the building file is completely current and that the Space file contains at least a room.

number (including building and division, if applicable) for each physical location. The proper format for a room number (which must be unique and unambiguous) is Room-Building-Division. Most single division facilities will need to enter only Room- Building.

#### Accident Reporting

The 2162 Accident Reporting module collects the data elements of VA Form 2162 so that accidents and on-the-job injuries can be aggregated and analyzed by Service/Section, cause of accident, nature of accident, etc.

#### Assign (Transfer) Electronic Work Orders

The Assign (Transfer) Electronic Work Orders option was developed to facilitate the process of transferring electronic work orders from the receiving area(s) to a working shop. Users may also disapprove electronic work orders when necessary. In such a case, the COMMENTS field is automatically mailed to whoever entered the work order, along with the information that their request has been disapproved.

#### IT Equipment Tracking

The IT Equipment Module allows IT personnel to view and update the non- expendable equipment inventory for IT equipment. It allows IT staff to assign responsibility for IT equipment to individuals and allows individuals to sign electronic hand receipts for the assigned equipment.

IT equipment is identified based on the CMR (EIL) field. If an equipment item is on a CMR with IT TRACKING equal to YES, the equipment is considered tracked IT equipment. The CMR File Enter/Edit \[ENCMR\] option can be used by Acquisition & Materiel Management (A&MM) to edit the IT TRACKING field.

Only tracked IT equipment can be edited using the Inventory Edit (IT) option. All tracked IT equipment is expected to be assigned to individual IT owners.

The IT Equipment Tracking module is tightly coupled with the Equipment Management module.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An overall introduction to the Engineering system, the menu structure, and the VA FileMan conventions used are given in the beginning of the manual. After reviewing this information, the remaining sections may be examined according to user interest and need.

The Engineering package is accessed through a general menu, with an extended sub menu system for each of the general options. The documentation is written based on a system using Kernel 6.5, which is the minimum Kernel version required by the package. If installed on a system using Kernel 7.0, menu options that lead to sub menus will be followed by three leader dots. While actual menus are shown through third-level sub menus, the options appearing on lower-level menus are fully discussed.

The Engineering package does not use help frames. Information is usually available at system prompts by typing \<?\>. Some prompts allow entry of \< ??\> for additional information.

### Standard Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A knowledge of general VA FileMan system protocol is all that is required to use the Engineering package. VA FileMan presents the user with line-by-line information, to which the user may enter responses at system prompts.

The following conventions are used:

1.  Most of the prompts contain help or information texts. To view these, enter a \<?\> at the given prompt.
2.  Many of the prompts contain defaults. For example, "Would you like to review the item information? NO//" has a "no" response as a default. Enter a carriage return.

\<RET\> to select the default or enter an alternative response to override the default.

3.  Dates may be entered using the standard VISTA formats of 1 Jan 81, or using the month first, Jan 1 1981, 1/1/81 or 010181. If the year is not entered, the current year is automatically entered. To enter the current date, users may enter a \< T\> for "today", \<T-1\> for the previous date, \< T-3W \> for three weeks before the current date, \<T+1\> for the next day, and so on. Hours may be entered by typing a number between .5 and 9999.
4.  Lists of items for viewer selection are generated at some prompts. Entering an \< ^\> will halt the generation of the list and entering a \< RET\> will continue the listing at the "Choose N-N: //" prompt, where N-N is the range from the first to last list items.

August 1993 Engineering V. 7.0 User Manual 2-1

5.  For item selection, users may enter the number of the option, or the first few letters of the item name.
6.  If a prompt requires line number selection, a range of items m may be selected by placing a semicolon between the beginning and ending numbers, as in \< 1;3\> for items 1 through 3.

Most of the Engineering system options contain screen displays of information. These follow the same conventions as line entry, with several additions.

1.  Entry of \<^\> at any screen selection will terminate the editing session.
2.  Entry of \<^D\> will take the user to the next screen (if any).
3.  Entry of \<^U\> will take the user to the previous screen (if any).
4.  Users may jump to any item on the screen by entering \< ^\> followed by the item number, such as \<^6\>.
5.  Entering \<?\> or \<??\> at any screen item will display available help text at the bottom of the screen.
6.  Entry of \<^C\> will display the available screen commands at the bottom of the screen.
7.  Users are occasionally asked if they want to "Repaint screen". If the screen has scrolled upward for any reason, it should be repainted.

The Engineering system does not use help frames. As stated above, information is usually available at system prompts, at which \<?\> will access the information. Some prompts allow entry of \< ??\> for additional information.

### Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ENGINEERING MAIN MENU

WORK ORDER & MERS PROJECT PLANNING PROJECT TRACKING EQUIPMENT MANAGEMENT

SPACE/FACILITY MANAGEMENT PROGRAM MANAGEMENT

2162 REPORT OF ACCIDENT

ASSIGN (TRANSFER) ELECTRONIC WORK ORDERS

#### WORK ORDER & MERS

Enter New Work Order Edit Work Order Data Close Out Work Order Display Work Order

Incomplete Work Order Status

Incomplete Work Orders by Employee Incomplete Work Orders by Location Incomplete Work Orders by Shop

Incomplete Work Orders by Owner/Department Transfer W.O. to Another Shop

Print Equip. History by Entry Number Disapprove Work Order

Reprint Work Orders (All Shops) Print PM Manhours

#### PROJECT PLANNING

5 Year Plan Project E/E

Project Application E/E (VAF 10-1193) Environmental Analysis E/E (VAF 10-1193a) Activations E/E

Report/Print Menu

Minor/Minor Misc Prioritization NRM Prioritization Scoring Sheet

Environmental Analysis VAF 10-1193a Project Application VAF 10-1193

5 Year Plan Report Approval of Project Application Electronic Transmission Menu

Batch Transmit 5-Year Plan Projects Individual 5-Year Plan Project Transmission Project Application Send

#### PROJECT TRACKING

Enter Project Data Screen Review All Data

Preliminary Data Enter/Edit Approved Dates Screen Edit Revised Dates Screen Edit Actual Dates Screen Edit A/E Data Screen Edit Contractor Data Screen Edit

Changes & Remarks Screen Edit Print Project Status Report

Print All Project Status Reports Transmit 10-0051 Electronically

#### EQUIPMENT MANAGEMENT

New Inventory Entry Multiple Inventory Entry Inventory Edit

Display Equipment Record Equipment Reports...

Specific Equipment History Equipment Category History Inventory Listing...

CMR Inventory (EIL) Equipment Category Inventory Location Inventory

Using Service Inventory Responsible Shop Inventory Use Status Inventory

Warranty List Replacement Listing Failure Rate Report PM Workload Analysis

Direct Posting to Equipment Histories PM Parameters...

Display Specific Device PM Schedule Display Equipment Category PM Schedule Print PM Procedure

Enter/Edit Specific Device PM Schedule Enter/Edit Equipment Category PM Schedule Enter/Edit PM Procedure

Generate PM Schedule...

Monthly PM List Weekly PM List

Delete PM Work Orders

Record Equipment PMI...

Close Out PM Work Orders

Rapid Closeout of PM Work Orders Record Single Device PMI

Bar Coded PMI Functions...

Download PM Program to Portable Bar Code Reader Upload Data from Portable Bar Code Reader

Restart Processing of Bar-Coded PMI Upload Data from MedTester

Rapid Deferral of PM Worklist Print PM Manhours

Print Bar Code Labels for Equipment Management...

Equipment Labels...

Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

Equipment Labels by Equipment ID#

Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

Location Labels...

WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

ALL Bar-Coded Location Labels

Bar Coded Equipment Inventory Management...

Download NX Program to Portable Bar Code Reader Upload Data from Portable Bar Code Reader Inventory Exception Listing

Manual Update of Equipment Inventory

Restart Processing of Uploaded NX Inventory Data

#### NONEXPENDABLE EQUIPMENT

Equipment Enter/Edit (NX)...

New Inventory Entry Inventory Edit

Display Equipment Record Multiple Inventory Entry

Manual Update of Equipment Inventory Equipment Management Reports (NX)...

Specific Equipment History CMR Inventory (EIL) Warranty List

Replacement Listing Location Inventory Using Service Inventory Use Status Inventory

Bar Code Features (NX Equipment) ...

Equipment Labels...

Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

Equipment Labels by Equipment ID#

Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

#### NONEXPENDABLE EQUIPMENT, continued

Location Labels...

WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

ALL Bar-Coded Location Labels Bar Code Features

Download NX Program to Portable Bar Code Reader Upload Data from Portable Bar Code Reader

Restart Processing of Uploaded NX Inventory Data Inventory Exception Listing

NX (Nonexpendable Equipment) Utilities...

CMR File Enter/Edit

Category Stock Number Enter/Edit

#### PROGRAM MANAGEMENT

Engineering Computer Port Section List

Work Center Code Engineering Employee File

Enter/Edit Equipment Category PM Schedule Manufacturer

ENG SITE PARAMETERS Enter/Edit

SOFTWARE OPTIONS Enter/Edit Engineering Archive Module.

Find & Assemble Records Archive & Verify Records Delete Archive Global Recall Archive Global Review Activity Log

Biomedical Engineering Resource Survey Entering Data into the BERS Survey File Print Personnel Survey Listing

Print Contract Survey Listing Print General Survey Listing Print Additional Survey Listing

Work Action

#### SPACE/FACILITY MANAGEMENT

Space Management...

Enter New Room Space Data Display/Edit Room Data

Finish Replacement Schedules Report Menu ... Replacement Schedule for All Finishes Ceiling Replacement Schedule

Wall Replacement Schedule Floor Replacement Schedule Space Survey Report Menu ...

Room/Keying/Function Report Space Survey by Room Service Space Survey Function Space Survey Building Space Survey

RCS 10-0141 Report

Building Management RCS 10-203, VAF 10-6007a Non-Space File Location Report

Key/Lock Management ...

Key Distribution by Employee Enter/Edit Lock Number File Enter/Edit

Print Key Distribution by Employee Print Employee List sorted by Key Print Employee List by Service

Export Facility Management Data ...

Output Service/NSF spreadsheet Output Function/NSF Spreadsheet Output RCS 10-0141 spreadsheet.

Facility Management Utilities ... Edit Space Functions File Edit Space Utilities file.

Remove Dangling Pointers in Lock file Building File Enter/Edit

Print All Building Data Leased Space Options...

Enter/Edit All Lease Fields (BUILDING FILE) Enter/Edit Lease Vendor (BUILDING FILE) Print Leased Space Survey

Planning Space Program Menu ... Building File Enter/Edit Enter/Edit Room Planning Data Print Building/Project Space Plan

#### 2162 REPORT OF ACCIDENT

Enter 2162 Report

Display 2162 Report

Edit 2162 Report Service/Division Summary Report Injury Cause Summary Report Accident Nature Summary Report

Specific Location Summary Report

#### ASSIGN (TRANSFER) ELECTRONIC WORK ORDERS

IT EQUIPMENT MODULE (ENIT MGR)

Inventory Edit (IT) Display Equipment Record

Bar Code Features (NX Equipment) ...

Equipment Labels...

Equipment Category Bar Code Labels CMR Bar Code Labels (EQUIPMENT) Bar Code Labels by PM Number

Bar Code Labels by General Location (WING) Bar Code Labels by Specific Location (ROOM) Single Device Bar Code Label

Equipment Labels by Equipment ID#

Bar Code Labels in Conjunction with PM Worklist Bar Code Labels for a Purchase Order

Bar Code Labels by LOCAL ID Bar Code Labels by Using Service

Location Labels...

WING Bar Code Labels BUILDING Bar Code Labels ROOM Bar Code Label

ALL Bar-Coded Location Labels

Download NX Program to Portable Bar Code Reader Upload Data from Portable Bar Code Reader Restart Processing of Uploaded NX Inventory Data Inventory Exception Listing

Specific Equipment History Display/Edit Room Data

Non-Space File Location Report

#### IT EQUIPMENT MODULE (ENIT MGR), continued

IT Equipment Responsibility...

Assign Responsibility Terminate Responsibility Transfer Responsibility Certify Hard Copy Signature

Print Hand Receipt for an Individual Add Entry to New Person File

IT Equipment Report Menu...

Individual Responsibility for IT Assets Report Unassigned IT Asset Report

Assignments Pending Acceptance Report Tracked IT Assets Report

Signature Exception Report Assignment Inquiry

#### IT OWNER MENU

Accept IT Responsibility

Individual Responsibility for IT Assets Report Print My Hand Receipt

Assignment Inquiry

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, there are no legal requirements pertaining to the package.

Detailed information on all site parameters is available on-line. Simply enter \< ??\> when prompted for a selection.

### Special Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are five (5) options that may be useful as Primary Menu options for users who have limited needs for access to the Engineering Package. They are:

ENPMINSP (Engineering PM Clerk Main Menu) ENCCLERK (Engineering Accounting Clerk Main Menu) ENSEC (Engineering Secretary Main Menu) ENSECFORM (Engineering Foreman Main Menu) ENWCLERK (Engineering Work Control Main Menu)

### A&MM Nonexpendable Equipment Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VISTA nonexpendable equipment file is contained within the Engineering package. Acquisition and Material Management Service personnel engaged in property management activities will need access to selected menu options within the Engineering namespace. Menu option ENMM MGR, Nonexpendable Equipment (A&MM), is intended to meet the needs of these users. Users of these options should hold the ENEDNX security key. However, note that holding the ENEDNX key does not automatically give the menu options to the holder. The menus must be specifically assigned. Users of these options should refer to the documentation for the Equipment Management module. Not all PPM employees will need to hold keys to all of the sub- options contained in ENMM MGR so these options may also be assigned individually.

### Generation of On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On-line documentation of data dictionaries and routines may be generated through VA FileMan and the Kernel %Index routines.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Engineering Work Order Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Engineering Work Order Module (together with the Electronic Work Order Module) is intended as a tool for acquiring, assigning, and recording unscheduled work requests. It is tightly integrated with the Engineering Equipment Module. Note that the *V*ist*A* Engineering Package is also known as AEMS/MERS.

There are two basic types of work orders, scheduled (preventive maintenance) and unscheduled (all other). Scheduled (or "PM") work order numbers always begin with the character string "PM-". They are actually generated from within the Equipment Module and are normally closed out there as well. PM work orders are essentially line items on the PM worklists that are printed regularly by shop. They are posted to the equipment repair histories at close out time. PM work orders may be edited and closed out via the Work Order Module, but the developers don't recommend it.

The equipment PM schedules (as well as the repair histories) are stored in the Equipment Inv. file. There is also an Equipment Category file that contains standard PM schedules for many different types of equipment. Maintaining the Equipment Category file will automatically maintain the PM schedules for all equipment records that point to it. Options for maintaining both the Equipment Inv. file and the Equipment Category file are found in the Equipment Module.

Unscheduled work orders may be entered either by Engineering Service (using the New Work Order option (ENWONEW)) or by the actual requester (using the Electronic Work Order option (ENWOWARD)). Entries made by the requester are called "electronic work orders" and are processed a little differently from those entered by Engineering. Requesters are not prompted for quite as much information. In particular, they are not expected to know what Engineering Section (or shop) will be assigned to do the work. Electronic work orders are routed to a receiving area (integrated sites usually have two or more such receiving areas) for processing. Someone in Engineering must use the Assign (Transfer) Electronic Work Orders option (ENETRANSFER) to examine unassigned electronic work orders on a regular basis. They should either be assigned to an Engineering Section or disapproved. In the case of disapproval, the Engineering user is asked to make relevant comments and a disapproval message is automatically sent to the requester.

Engineering Sections were originally organized as conventional trade shops (electrical, plumbing, biomedical, etc.), but some facilities have converted to multi­ disciplinary teams assigned to certain areas. The package will support either approach, or a combination of the two. The only restriction on the assignment of Engineering Sections is that section numbers in the ranges of 90-99, 190-199, 290- 299...990-999 must be reserved for use as electronic work order receiving areas. The Engineering Section file tells the system how much information to request during work order close out. Work order numbers contain the abbreviation of the shop to which the work order is currently assigned and the date on which that work order number was generated. The Engineering Section file is maintained from within the Engineering Program Management Module.

The Edit Work Order Data (ENENT) and Close Out Work Order (ENWOCLOSE) options use the roll-and-scroll edit features of VA FileMan. The Display Work Order option (ENDSY) shows an entire work order in screen format. Users may edit or print the work order from within the screen. They may also request information from the Control Point Activity file. Display Work Order option is often the most frequently used option in the module.

Note that changes to the status of an electronic work order may cause an e-mail message to be sent to the requester. This will happen if the requester has asked for such notification or if the Engineering Software Option for NOTIFICATION requires it. The standard message will clearly describe the work order in question, but sites may enter additional text via the Engineering Site Parameters file if they so desire. The Engineering Software Options file also allows you to have incoming inspection work orders generated automatically whenever an entry is made to the Equipment Inv. file. Engineering Software options and Engineering Site Parameters are maintained from within the Engineering Program Management Module.

When a work order contains a pointer to the Equipment Inv. file, equipment data in the work order itself (model, serial number, etc.) is automatically acquired from the Equipment Inv. file. If your Equipment Inv. file is adequately maintained it should never be necessary to manually enter any equipment information into the work order except the equipment entry itself. When work orders containing a pointer to the Equipment Inv. file are closed out, the equipment repair history is automatically updated.

The labor cost for each work order is computed by the system based on the time charged to each Engineering employee and the wage rate of that employee in the Engineering Employee file. The Engineering Employee file should be updated whenever a wage rate changes and is maintained from within the Engineering Program Management Module.

The Incomplete Work Order Status option (ENWO-STATUS-(XQ)) allows users to list incomplete work orders for an Engineering technician, a specific room, a range of locations, a shop, or an owning service. The list is in summary format, but if you send it to a terminal you can easily get complete information on any incomplete work order that appears.

Work orders in progress may be transferred from one shop to another via the Transfer W.O. to Another Shop option (ENWO-TRANSFER). This option will automatically change the work order number to something that's appropriate for

the new shop. The system keeps a permanent record of the original work order number and has a record of the current work order number, but anything in between will be lost. For example, if an electronic work order is first assigned to the biomedical shop and then transferred to the electric shop, you can look it up by its original work order number (containing the abbreviation of a receiving area) or its current work order number (containing the abbreviation of the electric shop), but not by the work order number that it had while it was assigned to the biomedical shop.

The Print Equip. History by Entry Number option (ENEQHID) allows you to view the service history of a piece of equipment by looking directly at the Work Order file. This option is similar to the Specific Item History option (ENIN-HIST- SPECIFIC) in the Equipment Module but displays different information. Also note that incomplete work orders will be included with Print Equip. History by Entry Number but not with Specific Item History. On the other hand, archived work orders will be included with Specific Item History but not with Print Equip. History by Entry Number.

The Disapprove Work Order option (ENWODISAP) gives Engineering employees who hold it the ability to disapprove work requests. As previously stated, an e-mail message is automatically sent to the person who entered the work order that is being disapproved.

The Reprint Work Orders (All Shops) option (ENWOREP) will reprint open work orders from all shops based on the work order number. All work orders whose number falls within a user specified date range will be printed. The intent of this option is to give sites a means of batch printing all work orders that were entered in the course of a day.

The Print PM Manhours option (ENPMHOURS) yields a list of time spent on preventive maintenance inspections. The list includes information from a user selected range of shops for a user selected range of PM dates (month and year only). The list is sorted by shop, and then by PM date and employee within each shop.

The Condition Code of Equipment Edit option (ENEQCC) allows users to edit the condition code field on individually selected pieces of equipment. Allowable values are LIKE NEW, GOOD, and POOR. If sites choose to maintain this condition code (which is stored in the Equipment Inv. file) they normally set their Engineering Section file so that it will be updated as part of work order close out, but Condition Code of Equipment Edit is an alternative mechanism.

The Multiple Work Order Entry option (ENWOMULTI) will create (and close, if you so desire) unscheduled work orders for a list of equipment items. A new work order is entered in full for one piece of equipment. After this step, a list of other equipment items is selected from the Equipment Inv. file. The system then creates new work orders for each selected equipment item by copying the original work order and extracting equipment specific information (location, serial number, etc.) from the Equipment Inv. file. The developers' expectation is that this option may be especially useful in responding to hazard alerts and recall notices.

The Work Order module is accessed from the Engineering Main Menu. The option is selected from the menu by entering the first few unique characters, ("W" in this case) or alternately the corresponding synonym "WO".

The Work Order module should be used when performing operations on work orders. Using FileMan to enter or edit this data is not the preferred method. The following is a display of the procedure for entering the Work Order module.

#### Work Order & MERS

WO Work Order & MERS PLAN Project Planning TRK Project Tracking

EQ Equipment Management ENM Program Management

SP Space/Facility Management FSA 2162 Report of Accident

XFER Assign (Transfer) Electronic Work Orders

Select Engineering Main Menu Option: WO Work Order & MERS

#### Enter New Work Order

This option is used to enter a new work order into the computer. When the computer asks if you want to enter a new work order, enter \< Y\> for yes or \<N\> for no. A work order number will be generated for each work order entered. For example, B891106-001 is a biomedical work order initiated during 1989, the 11th month on the 6th day. The number after the dash tells us that this is the first work order generated that day in the biomedical shop.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
2.  Edit Work Order Data
3.  Close Out Work Order
4.  Display Work Order
5.  Incomplete Work Order Status ...
6.  Transfer W.O. to Another Shop
7.  Print Equip. History by Entry Number
8.  Disapprove Work Order
9.  Reprint Work Orders (All Shops)
10. Print PM Manhours
11. 11 Condition Code of Equipment Edit
12. Multiple Work Order Entry

The following example illustrates the process of entering a new work order.

Select Work Order & MERS Option: 1 Enter New Work Order

Select ENGINEERING SECTION LIST: ??

The Engineering Section List is developed on-site using the Program Management option.

Choose from:

| 1   |     | OFFICE OF THE CHIEF  |
|-----|-----|----------------------|
| 2   |     | ADMIN.+CLER.         |
| 3   |     | SUPERVISORY OPERAT.  |
| 4   |     | UTILITY OPERATIONS   |
| 5   |     | AIR CONDITIONING PLT |
|     | ^   |                      |

Table 2 Project Application E/E (VAF 10-1193)

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF

Want to enter a new work order?

Enter Yes or No: YES// \<RET\>

WORK ORDER \#: OC970424-003 (APR 24, 1997@16:32)

Next, the date is requested. If the date is the day of entry, only \< RET\> has to be pressed and the date and time will be entered as shown.

REQUEST DATE: APR 24,1997@16:32// ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

You may omit the precise day, as: JAN, 1957

Date (and time if desired) when work request was originally entered.

REQUEST DATE: APR 24,1997@16:32// \<RET\>

REQUEST MODE: COMPUTER// ??

Indicator of how the work was actually requested. Choose from:

P PHONE

W WRITTEN

D DELIVERED

V VERBAL

C COMPUTER

REQUEST MODE: COMPUTER// \<RET\> COMPUTER

EQUIPMENT ID#: 21// ??

Entry in the Equipment File (#6914) to which this work order is to be.

charged.

Choose from:

| 1   | 2221       | IN USE    |
|-----|------------|-----------|
| 2   | 91120526   | TURNED IN |
| 3   | 3290A00220 | IN USE    |
| 4   | 3301A01107 | IN USE    |

If an equipment entry is specified, the computer will extract available data from the Equipment Inventory file to populate the Work Order fields such as location, owner/department, etc.

> ^

EQUIPMENT ID#: 21// \<RET\>

LOCATION: 221-114// ??

Physical location where work is to be performed.

Choose from:

102-148 MEDICINE

103-110-JC EXAM/TREATMENT ROOM

148 C

110

^

CCU

EXAM/TREATMENT ROOM MEDICINE

LOCATION: 221-114// \<RET\>

BED \#:??

> Optional field. Filled in at time of request if the work requested is.

> associated with a specific bed in a patient room.

BED \#: \<RET\>

TASK DESCRIPTION (60 char): The equipment needs to be cleaned.

STATUS: IN PROGRESS// ??

Added with Version 6.4. May be helpful when printing reports of M&R activity.

Choose from:

1.  IN PROGRESS
2.  PENDING
3.  WAITING ON PARTS
4.  WAITING ON VENDOR SERVICE

STATUS: IN PROGRESS// \<RET\> IN PROGRESS CONTACT PERSON: ??

> This is the person to be contacted if there are questions about the

> nature of the work that has been requested.

CONTACT PERSON: ENTECH, ONE

PHONE:??

Telephone number or extension of the individual requesting the work.

PHONE: 5155551211

DATE ASSIGNED: APR 24,1997// \<RET\> (APR 24, 1997)

The PRIMARY TECH ASSIGNED must be someone in the file of Engineering employees. This file is established by the Engineering Applications Manager. If all the technicians have last names starting with different letters, only the first letter of the last name needs to be entered. The computer will pick up the rest of the name from the file. The PRIMARY TECH (if any) is automatically included by the system as an ASSIGNED TECH (multiple) on the subject work order.

Frequently, several employees may be assigned to the same work order. On occasion, they may be from different shops. The ASSIGNED TECH is used to record this information. The ASSIGNED TECH field has entry areas for the number of hours worked, and for the shop to which that employee is assigned. It is here that the number of hours and total labor cost is calculated. The PRIMARY TECH ASSIGNED is only used to show who is responsible for the work. If this person also performed work, s/he should also be entered as an ASSIGNED TECH.

PRIMARY TECH ASSIGNED: ??

Technician who bears primary responsibility for completion of task.

Choose from:

1.  ENTECH,
13. TWO ENTECH,
14. THREE ENTECH,
15. FOUR ENTECH,
16. FIVE

PRIMARY TECH ASSIGNED: ENTECH, FOUR

The PRIORITY of the request is the next item. It must be answered with one of the possible responses listed in the display below. Once the single letter is entered, the computer will display the priority name. The default PRIORITY is "A" for average.

Work orders with a priority of "HIGH" or "EMERGENCY" will be shown in bold type on the Incomplete Work Order Status screens.

PRIORITY: A// ??

Relative priority of this work request.

Choose from:

> E EMERGENCY

H HIGH

An AVERAGE

L LOW

M MODIFICATION PRIORITY: A//

> \<RET\> AVERAGE

The OWNER/DEPARTMENT must be selected from the list of entries in the Service/Section file. You may enter the first letter of an OWNER/ DEPARTMENT, and the system will display names that start with that letter.

OWNER/DEPARTMENT: MAS 5.0 USERS// ??

The service or section for whom work is to be performed.

Choose from:

ACQUISITION &

MATERIAL MGMT 90

BLIND REHABILITATION

BUILDING MANAGEMENT

DENTAL

ENGINEERING

FISCAL 04

> ^

OWNER/DEPARTMENT: MAS 5.0 USERS// INFORMATION

1.  INFORMATION RESOURCES MGMT IRM
2.  INFORMATION SYSTEMS CENTER

CHOOSE 1-2: 2

WORK ACTION the next field, is a list composed of tasks which may be involved when completing a Work Order. The list is established by the Engineering Applications Manager.

Select WORK ACTION: ??

Type of work performed or requested.

Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3 DAMAGE/ABUSE D1

^

Select WORK ACTION: PREVENTIVE MAINTENANCE P2

The WORK CENTER CODE is a five-digit number. The first three digits indicate the cost center. The code is a breakdown of work in a particular cost center. For example, biomedical is cost center 555, so its work center codes range from 55501 to 55599.

Since the list of work center codes contains 431 different codes, this is not a practical list for display. You can input the first three digits, display the ones that relate to a cost center, and then choose the correct one. When "555" was entered for this example, the computer displayed five work center codes at a time and prompted for a choice or to continue. The 40th code displayed was chosen.

| WORK CENTER CODE: | ??                            |     |
|-------------------|-------------------------------|-----|
| September 1997    | Engineering V.7.0 User Manual | 4-7 |
|                   | Patch EN\*7\*35               |     |

Category of task to which this work order most closely corresponds.

Choose from:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 12%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>50100</p>
<p>50101</p>
<p>50102</p>
<p>50103</p>
<p>50104</p>
<p>50105</p>
<p>50106</p>
<p>50107</p>
<p>50108</p>
<p>50109</p>
<p>50200</p></th>
<th colspan="2"><p>50100/ENG.SUPERVISION</p>
<p>50101/ANNUAL LEAVE</p>
<p>50102/SICK LEAVE</p>
<p>50103/HOLIDAY LEAVE</p>
<p>50104/AWOL and LWOP</p>
<p>50105/OTHER LEAVE</p>
<p>50106/OTHER TIME</p>
<p>50107/ADMIN. &amp; CLERICAL</p>
<p>50108/SUPERVISION</p>
<p>50109/TRAINING</p>
<p>50200/UTILITY OPERATIONS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>^</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">WORK CENTER CODE: COMMENTS:</td>
<td>55611</td>
<td>55611/WARD FURNITURE &amp; EQUIP, REPAIR</td>
</tr>
<tr class="odd">
<td>1&gt;</td>
<td>&lt;RET&gt;</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

An option to close the work order is presented next. If answered \< YES\>, the following set of questions is asked.

Do you want to CLOSE this work order now? Enter Yes or No: NO// YES

WORK PERFORMED (140 char max):

Select ASSIGNED TECH: ENTECH, FOUR// ASSIGNED TECH: ENTECH , FOUR // HOURS:

SHOP: // BIOMEDICAL Select ASSIGNED TECH:

TOTAL MATERIAL COST:

VENDOR SERVICE COST:

DATE COMPLETE (or closed): T (JUNE 24,1997)

If your site has selected AUTO PRINT OF NEW WORK ORDERS as a software option, the work order will automatically print on the device designated for your shop. Otherwise, you will see a dialogue similar to the following.

Print this work order? Enter Yes or No: YES// N

Want to enter a new work order? Enter Yes or No: NO// NO

If this response is \<Y\>, the entry process repeats itself; if the response is \< N\>, the user is returned to the Work Order & MERS option menu.

#### Edit Work Order Data

This option is used to edit previously entered work orders. The computer steps through this option on a line-by-line basis. If you want to change data, you revise the data by typing it after "//". Most fields require the same information as requested in Enter New Work Order.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
17. Edit Work Order Data
18. Close Out Work Order
19. Display Work Order
20. Incomplete Work Order Status ...
21. Transfer W.O. to Another Shop
22. Print Equip. History by Entry Number
23. Disapprove Work Order
24. Reprint Work Orders (All Shops)
25. Print PM Manhours
26. Condition Code of Equipment Edit
27. Multiple Work Order Entry

The following information provides instructions for editing work order data. In the example, a complete list of work orders was requested but only a few are shown. A complete listing is not practical in an operating system since the list may contain several thousand work orders. The specific work order number should be entered, but if you enter the first part of it, the computer will display a list of all work orders beginning at the information entered.

As you step through the work order by pressing \< RET\> or changing the data, you view the data one line at a time. Sites are free to customize this data input template to meet local needs. If your site has done this then the prompts that you see may be different from what is shown here.

Select Work Order & MERS Option: 2 Edit Work Order Data

Select WORK ORDER \#: OC970424-003 221-114 PREVENTIVE MAINTENANCE WORK ORDER \#: OC970424-003// ??

Identifier of each individual work action. Composed of the shop abbreviation, date generated, and a computer-generated sequential component. Users may delete work orders when necessary, but they should never change a work order number.

WORK ORDER \#: OC970424-003// \<RET\>

REQUEST DATE: APR 24,1997@16:32// ??

Date (and time if desired) when work request was originally entered.

REQUEST DATE: APR 24,1997@16:32// \<RET\>

CONTACT PERSON: ENTECH, ONE// ??

This is the person to be contacted if there are questions about the nature of the work that has been requested.

CONTACT PERSON: ENTECH, ONE// \<RET\>

PHONE: (515)555-1211// ??

Telephone number or extension of the individual requesting the work.

PHONE: (515)555-1211// \<RET\>

EQUIPMENT ID#: 21// ??

Entry in the Equipment File (#6914) to which this work order is to be charged.

Choose from:

| 1   | 2221       | IN USE    |
|-----|------------|-----------|
| 2   | 91120526   | TURNED IN |
| 3   | 3290A00220 | IN USE    |
| 4   | 3301A01107 | IN USE    |
| 5   | 3301A01105 | IN USE    |
| 6   | 3301A01104 | TURNED IN |

EQUIPMENT ID#: 21// \<RET\>

CONDITION CODE: ??

Condition code of equipment is normally determined by an Engineering technician and entered during close out of a work order. The code is:

1.  LIKE NEW - Like new condition, good performance record, low service cost.
28. GOOD Middle of service life, fair performance record, increasing service cost.
29. POOR Approaching end of service life, poor performance record, high service cost, consider budgeting for replacement.

Choose from:

1.  LIKE NEW
30. GOOD
31. POOR

CONDITION CODE: \<RET\>

OWNER/DEPARTMENT: INFORMATION SYSTEMS CENTER// ??

The service or section for whom work is to be performed.

Choose from:

ACQUISITION & MATERIAL MGMT 90

BLIND REHABILITATION BUILDING MANAGEMENT DENTAL

ENGINEERING FISCAL 04

INFORMATION RESOURCES MGMT IRM INFORMATION SYSTEMS CENTER

^

OWNER/DEPARTMENT: INFORMATION SYSTEMS CENTER// \<RET\>

Select ASSIGNED TECH: ENTECH, FOUR// ??

1 ENTECH, FOUR

Engineering employee(s) assigned to this work order.

Choose from: ENTECH, TWO ENTECH , THREE ENTECH , FOUR ENTECH , F IVE

Select ASSIGNED TECH: ENTECH, FOUR// \<RET\> ASSIGNED TECH: ENTECH , FOUR// \<RET\> HOURS: ??

Number of hours (to the nearest tenth) spent on this work order by this employee.

HOURS: \<RET\>

SHOP: BIOMEDICAL// ??

Engineering section under whose direction this work was performed.

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS
5.  AIR CONDITIONING PLT
6.  BOILER PLANT

^

SHOP: BIOMEDICAL// \<RET\>

Select ASSIGNED TECH: ??

1 ENTECH, FOUR

Engineering employee(s) assigned to this work order.

Choose from: ENTECH, TWO ENTECH , THREE ENTECH , FOUR ENTECH , F IVE ENTECH , S IX

Select ASSIGNED TECH: \<RET\>

Select WORK ACTION: PREVENTIVE MAINTENANCE// ??

1 PREVENTIVE MAINTENANCE Type of work performed or requested.

Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3 DAMAGE/ABUSE D1 ELECTRICAL SAFETY E1

EVALUATION (Equipment) E2

^

Select WORK ACTION: PREVENTIVE MAINTENANCE// \<RET\>

STATUS: IN PROGRESS// ??

Added with Version 6.4. May be helpful when printing reports of M&R activity.

Choose from:

1.  IN PROGRESS
2.  PENDING
3.  WAITING ON PARTS
4.  WAITING ON VENDOR SERVICE STATUS: IN PROGRESS// \<RET\>

WORK CENTER CODE: 55611/WARD FURNITURE & EQUIP, REPAIR

// ??

Category of task to which this work order most closely corresponds.

Choose from:

| 50100 | 50100/ENG.SUPERVISION |
|-------|-----------------------|
| 50101 | 50101/ANNUAL LEAVE    |
| 50102 | 50102/SICK LEAVE      |
| 50103 | 50103/HOLIDAY LEAVE   |
| 50104 | 50104/AWOL and LWOP   |

^

WORK CENTER CODE: 55611/WARD FURNITURE & EQUIP, REPAIR

//

TOTAL HOURS: ??

Total man-hours by all assigned employees. Calculated by the system automatically.

TOTAL HOURS (between .1 and 9999) can be entered. The system will automatically total the hours of all ASSIGNED TECHS and present this number as the default.

TOTAL HOURS: \<RET\>

TOTAL MATERIAL COST: ??

Approximate cost of materials needed to complete this task.

MATERIAL SERVICE COST may not exceed \$99,999,999.

TOTAL MATERIAL COST: \<RET\>

VENDOR SERVICE COST: ??

Approximate cost of vendor services needed to complete this task.

VENDOR SERVICE COST may not exceed \$99,999,999.

VENDOR SERVICE COST: \<RET\>

WORK PERFORMED (140 char max): ??

Brief description of work actually performed (may be extracted from COMMENTS field). The WORK PERFORMED field will be saved in the EQUIPMENT (Inventory) File (No. 6914) where it will be a permanent part of the device history. In contrast, the COMMENTS field will be removed from disk (on­ line) storage when the work order is archived.

WORK PERFORMED (140 char max): \<RET\>

COMMENTS:

1\> \<RET\>

DATE COMPLETE (or closed): ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. You may omit the precise day, as: JAN, 1957

Date on which work order is closed out.

DATE COMPLETE (or closed): \<RET\>

Select WORK ORDER \#: \<RET\>

At the end of the entry, the computer will prompt for another Work Order \#. If you press \<RET\>, you will return to the Work Order & MERS option menu.

#### Close Out Work Order

During the close out of a work order, users will be prompted for the Work Order number, the Equipment ID#, the manufacturer, model, serial number, the assigned tech, hours, total material cost, work performed, date complete, and comments. If an Equipment ID# is entered then the manufacturer, model, and serial number will be extracted from the Equipment Inv. file.

> **NOTE:** Whatever is entered as Work Performed will be posted to the Equipment History as the work order is being closed out. Comments are retained in the Work Order file but are not posted to the Equipment History.

Sites are free to modify the input template for work order closeout.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
2.  Edit Work Order Data
3.  Close Out Work Order
4.  Display Work Order
5.  Incomplete Work Order Status ...
6.  Transfer W.O. to Another Shop
7.  Print Equip. History by Entry Number
8.  Disapprove Work Order
9.  Reprint Work Orders (All Shops)
10. Print PM Manhours
11. Condition Code of Equipment Edit
12. Multiple Work Order Entry

The following example illustrates the process of closing out a work order.

Select Work Order & MERS Option: 3 Close Out Work Order

Select WORK ORDER \#: OC970424-003 221-114 PREVENTIVE MAINTENANCE EQUIPMENT ID#: 21// ??

Entry in the Equipment File (#6914) to which this work order is to be charged.

Choose from:

| 1   | 2221       | IN USE    |
|-----|------------|-----------|
| 2   | 91120526   | TURNED IN |
| 3   | 3290A00220 | IN USE    |
| 4   | 3301A01107 | IN USE    |
| 5   | 3301A01105 | IN USE    |

^

EQUIPMENT ID#: 21// \<RET\>

CONDITION CODE: ??

Condition code of equipment is normally determined by an Engineering technician and entered during close out of a work order. The code is:

1)  LIKE NEW - Like new condition, good performance record, low service cost.
2)  GOOD - Middle of service life, fair performance record, increasing service cost.
3)  POOR - Approaching end of service life, poor performance record, high service cost, consider budgeting for replacement.

Choose from:

| 1   | LIKE NEW |
|-----|----------|
| 2   | GOOD     |
| 3   | POOR     |

CONDITION CODE: \<RET\>

Select ASSIGNED TECH: ENTECH, FOUR// ??

1 ENTECH, FOUR

Engineering employee(s) assigned to this work order.

Choose from:

ENTECH, TWO ENTECH , THREE ENTECH , FOUR ENTECH , F IVE ENTECH , S IX

Select ASSIGNED TECH: ENTECH, FOUR// \<RET\> ASSIGNED TECH: ENTECH , FOUR// \<RET\> HOURS: ??

Number of hours (to the nearest tenth) spent on this work order by this employee.

HOURS: \<RET\>

SHOP: BIOMEDICAL// ??

Engineering section under whose direction this work was performed.

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS

^

SHOP: BIOMEDICAL// \<RET\>

Select ASSIGNED TECH: ??

1 ENTECH, FOUR

Engineering employee(s) assigned to this work order.

Choose from: ENTECH, TWO ENTECH , THREE ENTECH , FOUR ENTECH , F IVE ENTECH , S IX

Select ASSIGNED TECH: \<RET\>

Select WORK ACTION: PREVENTIVE MAINTENANCE// ??

1 PREVENTIVE MAINTENANCE Type of work performed or requested.

Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3 DAMAGE/ABUSE D1 ELECTRICAL SAFETY E1

EVALUATION (Equipment) E2

^

Select WORK ACTION: PREVENTIVE MAINTENANCE// \<RET\>

TOTAL MATERIAL COST: ??

Approximate cost of materials needed to complete this task.

TOTAL MATERIAL COST: \<RET\>

VENDOR SERVICE COST: ??

Approximate cost of vendor services needed to complete this task.

VENDOR SERVICE COST: \<RET\>

WORK PERFORMED (140 char max): ??

Brief description of work actually performed (may be extracted from COMMENT S field). The WORK PERFORMED field will be saved in the EQUIPMENT (Inventory)

File (No. 6914) where it will be a permanent part of the device history. In contrast, the COMMENTS field will be removed from disk (on-line) storage when the work order is archived.

WORK PERFORMED (140 char max): \<RET\>

COMMENTS:

1\> \<RET\>

DATE COMPLETE (or closed): APR 30,1997// ??

Date on which work order is closed out.

DATE COMPLETE (or closed): APR 30,1997// \<RET\> (APR 30, 1997) Select WORK ORDER \#: \<RET\>

> **NOTE:** Manufacturer, Model, and Serial Number fields are determined and shown by the system once the Equipment ID# has been entered. Engineering sections that have EXPANDED WORK ORDER CLOSEOUT set to "YES" will display these fields during the closeout.

#### Display Work Order

This option is principally used to review and enter/edit work orders. Users must enter the Work Order Number. A list of other possible entry answers is obtained by typing a \<?\> after Select WORK ORDER \#.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
32. Edit Work Order Data
33. Close Out Work Order
34. Display Work Order
35. Incomplete Work Order Status ...
36. Transfer W.O. to Another Shop
37. Print Equip. History by Entry Number
38. Disapprove Work Order
39. Reprint Work Orders (All Shops)
40. Print PM Manhours
41. Condition Code of Equipment Edit
42. Multiple Work Order Entry

The following example illustrates the process of displaying a work order.

Select Work Order & MERS Option: 4 Display Work Order Select WORK ORDER \#: ?

Use 'E.value' to list W.O. s whose EQUIPMENT ID# equals 'value' Use 'L.value' to list W.O.s whose LOCATION starts with 'value.’

Answer with WORK ORDER \#, or ORIGINAL WORK ORDER \#, or LOCATION, or

TASK DESCRIPTION (60 char), or EQUIPMENT ID#, or LOCAL IDENTIFIER, or

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>PMI NUMBER</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Do you want the entire 204-Entry WORK ORDER # List? Select WORK ORDER #: OC970424-003 221-114</td>
<td><p><strong>N</strong> (No)</p>
<p>PREVENTIVE MAINTENANCE</p></td>
</tr>
<tr class="even">
<td>WORK ORDER # OC970424-003</td>
<td></td>
</tr>
</tbody>
</table>

1\) PRIMARY EMPL: ENTECH, FOUR 2) REQ DATE: APR 24,1997@16:32

3\) REQ MODE: COMPUTER 4) LOCATION: 221-114

5\) BED \#: 6) STATUS: COMPLETED

TASK DESC: PREVENTIVE MAINTENANCE

CONTACT: ENTECH, ONE 9) PHONE: (515)555-1211

10\) ENTERED BY: ENTECH, SEVEN 11) SHOP: OFFICE OF THE CHIEF

12\) DATE ASSIGNED: 04/24/97 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 21 15) LOCAL ID:

16\) EQUIP CAT: BED-ELECTRIC 17) CONDITION:

MFGR: ENMFGR, ONE

MODEL: 2300 20) SERIAL \#: 7888UYHG

21\) OWNER/DEPT: INFORMATION SYSTEMS CENTER 22) PM \#: 6530-6723

23\) PARTS ORDER: 24) WORK ACTION: P2

WORK CTR: 55611/WARD FURNITURE & EQUIP, REPAIR

TOTAL HOURS: 27) TOTAL MATERIAL COST:

28\) TOTAL LABOR COST: 29) VENDOR SERVICE COST:

30\) \*ASSIGNED TECH\* 31) DATE COMPLETE: APR 30,1997 \#1: ENTECH, FOUR HRS: SHOP: BIOMEDICAL

WORK PERFORMED:

COMMENTS:

WARRANTY EXPIRATION: \*\*06/30/97\*\*

> **NOTE:** Equipment must be isolated and rendered inoperative prior to service.

\[OTHER OPEN WORK ORDERS FOR THIS EQUIPMENT\]

Work Order \# Task Description

B970131-001 TEST OF FLAGGING (Hazard) PM-B9705M-003 QUARTERLY PMI HOSPITAL BEDS

OC970424-002 replacement equipment OC970424-001 Electric bed replacement B970203-001 TEST OF RIGHT EQ WO

A complete list of work orders would not be practical to display due to the number of work orders.

The screen display for this option contains exactly the same data as option \#2 but all the entries are displayed on the CRT at the same time. This is extremely useful when editing or reviewing the work order entries.

After the display "ENTER/EDIT NO. (1-33, D(DISPLAY), AC(ACCOUNT),

P(PRINT)):" appears on the CRT screen, you can enter or edit the data by typing one of the display selection numbers 1-33 and pressing \< RET\>. By typing \<D\> and pressing \<RET\>, you are able to repeat the display. If a transaction number has been entered in the PARTS ORDER \# field (23), you can see a display of that transaction (order) by entering \< AC\>. There has to be an entry for parts order number for there to be a TRANSACTION STATUS REPORT.

ENTER/EDIT (1-33 D(DISPLAY), AC(ACCOUNT), P(PRINT)): EXIT// AC

OBLIGATION TRANSACTION STATUS DISPLAY FEB 22,1111@14:19:58

Transaction Number: TEST2 Transaction Type: OBLIGATION A&MM Status:

Temporary Trans. Number: TEST2 Control Point: 101 Form Type: NON-REPETITIVE (2237) ORDER

Date of Request: JAN 25,1990 Date Required: JUL 1,1111

Est. Delivery Date: Date Received:

Vendor: ACE ELECTRONICS P.O. Vendor:

Committed (Estimated) Cost: \$30.00 Date Committed: Obligated (Actual) Cost: \$0.00 Date Obligated:

Purchase Order/Obligation No.: Accounting Data: 3600151.001 3040/2 CALM \$ Amount: \$50.00 CALM Date:

CALM Transaction Code:

Return to Service Comments:

Comments:

OBLIGATION TRANSACTION STATUS DISPLAY FEB 22,1111@14:20:21

Transaction Number: TEST2 Transaction Type: OBLIGATION

Requester: ENTECH, E IGHT Form Type: NON-REPETITIVE (2237) ORDER

Requester's Title: ENTECH, NINE Requesting Service: ENGINEERING Approving Official: Inventory Dist. Point:

Appr. Official's Title: Cost Center:

Date Signed (Approved):

Deliver To/Location:

Classification of Request: REPAIR PARTS Sort Group: BM890922-001

Would you like to review the item information for this request? NO// Y (YES)

This display cannot be edited. Typing \< YES\> at the item information review prompt will display all items ordered.

OBLIGATION TRANSACTION STATUS DISPLAY - ITEM INFORMATION

Transaction Number: TEST2 Transaction Type: OBLIGATION

STOCK NUMBER ITEM DESCRIPTION QUANTITY U/I UNIT COST

\|1 ITEM ID NO. 1, (NSN: \| \| \|

| \|6515-00-123-2345), POWER | SUPPLY | \|  |     | \|  | \|    |     |
|----------------------------|--------|-----|-----|-----|-------|-----|
| \|FINE                     |        | \|  | 1   | \|  | EA \| | 50  |
| \|                         |        | \|  |     | \|  | \|    |     |

Press \<RETURN\> to continue...

Pressing \<RET\> at the end of the display will return you to the work order request display screen. After entering \< RET\> at the final prompt of the work order display, the user returns to the Work Order & MERS options menu.

#### Incomplete Work Order Status

Under the Incomplete Work Order Status option, you may select one of the five categories listed below to generate a particular type of status report.

- Employee
- One Room
- Location Search
- Owner/Department
- Shop

> **NOTE:** You will be asked how many days old a work order must be in order to be included in the status report, whether PM work orders should be included, and whether you want a list of work orders or just a count. You are asked for an Engineering Section at the beginning and then given an opportunity to select ALL shops after all other questions have been answered.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
43. Edit Work Order Data
44. Close Out Work Order
45. Display Work Order
46. Incomplete Work Order Status ...
47. Transfer W.O. to Another Shop
48. Print Equip. History by Entry Number
49. Disapprove Work Order
50. Reprint Work Orders (All Shops)
51. Print PM Manhours
52. Condition Code of Equipment Edit
53. Multiple Work Order Entry

The menu providing the Incomplete Work Order Status options is listed below.

Select Work Order & MERS Option: 5 Incomplete Work Order Status

1.  Incomplete Work Orders by Employee
54. Incomplete Work Orders for One Room
55. Incomplete Work Orders by Location Search
56. Incomplete Work Orders by Shop
57. Incomplete Work Orders by Owner/Department

Incomplete W.O. Status by Employee

This option generates a list of incomplete work requests by assigned technician. The user is prompted to select the ENGINEERING EMPLOYEE of interest, from among those who belong to the chosen shop. If you simply press \<RETURN\>

instead of selecting a technician, the system will then allow you to enter the word “NOT” and thereby produce a list of incomplete work orders that are not assigned to anyone.

Select Incomplete Work Order Status Option: 1 Incomplete Work Orders by Employee Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// ??

Choose from:

1 OFFICE OF THE CHIEF

2 ADMIN.+CLER.

3 SUPERVISORY OPERAT.

4 UTILITY OPERATIONS

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// OFFICE OF THE CHIEF

Select EMPLOYEE NAME (press \<ENTER\> for unassigned): ??

Choose from: ENTECH, TWO ENTECH , THREE ENTECH , FOUR ENTECH , F IVE

Select EMPLOYEE NAME (press \<ENTER\> for unassigned): \<RET\>

Type 'NOT' to get unassigned work orders: EXIT// NOT

At least how many days old?: (0-999): 0// ??

This response must be a number.

At least how many days old?: (0-999): 0// \<RET\>

Include PM Work Orders? NO// ??

If you answer 'YES' the Incomplete Work Order list will contain PM work orders. To get a list of 'regular' work orders only, just say 'NO'.

Include PM Work Orders? NO// YES

Count(s) only? NO// ??

Enter either 'Y' or 'N'. Count(s) only? NO// \<RET\>

For ALL shops (say 'NO' if you only want OFFICE OF THE CHIEF)? No// (No)

Select output device: \<RET\>

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

The first screen of incomplete work orders is shown in the following display.

INCOMPLETE WORK ORDERS (OFFICE OF THE CHIEF) MAY 5,1997@11:39 Page 1

WORK ORDER REQ DATE LOCATION EQUIP ID# CONTACT PRI. STAT EMPL ASSIGNED TASK DESCRIPTION

ACC \# S/P VENDOR P.O. \# EST.DEL. DEL.COMP.

OC970424-001 04/24/97 221-114 21 AVER 1

Electric bed replacement

OC970408-001 04/08/97 AVER 1

Issued for delete pm work order.

1 TO 2 FOR EXPANDED DISPLAY: EXIT// 2

The above display can have three lines of data for each work order. If the information for the third line does not exist, no space is allowed for the line. If "2" is entered, the following expanded display for the second Work Order is obtained.

WORK ORDER \# OC970408-001

PRIMARY EMPL: 2) REQ DATE: APR 8,1997@14:10

3\) REQ MODE: COMPUTER 4) LOCATION:

5\) BED \#: 6) STATUS: IN PROGRESS

TASK DESC: Issued for delete pm work order.

CONTACT: 9) PHONE:

10\) ENTERED BY: ENTECH, SEVEN 11) SHOP: OFFICE OF THE CHIEF

12\) DATE ASSIGNED: 04/08/97 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 15) LOCAL ID:

16\) EQUIP CAT: 17) CONDITION:

MFGR:

MODEL: 20) SERIAL \#:

21\) OWNER/DEPT: 22) PM \#:

23\) PARTS ORDER: 24) WORK ACTION:

WORK CTR:

TOTAL HOURS: 27) TOTAL MATERIAL COST:

28\) TOTAL LABOR COST: 29) VENDOR SERVICE COST:

30\) \*ASSIGNED TECH\* 31) DATE COMPLETE:

WORK PERFORMED:

COMMENTS:

ENTER/EDIT (1-33), D(DISPLAY), AC(ACCOUNT), P(PRINT)): EXIT// \<RET\>

As seen from this display, you can ask for the display to be repeated by entering.

\<D\>. If parts have been ordered, entering \< AC\> will access the TRANSACTION STATUS REPORT. If no parts have been ordered, there will be no display. When?

\<P\> is entered, you will be prompted to select a printer.

#### Incomplete Work Orders for One Room

This option generates a list of incomplete work orders for a specific entry in the Space file (#6928).

Select Incomplete Work Order Status Option: 2 Incomplete Work Orders for One Room

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// ??

Choose from:

1 OFFICE OF THE CHIEF

2 ADMIN.+CLER.

3 SUPERVISORY OPERAT.

4 UTILITY OPERATIONS

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// \<RET\>

Select ENG SPACE ROOM NUMBER: ??

Choose from:

| 100-110-JC | 110  | CCU | MEDICINE                   |                   |
|------------|------|-----|----------------------------|-------------------|
| 101-148    | 148  | C   | EXAM/TREATMENT ROOM        |                   |
| 102-148    | 148  | C   | EXAM/TREATMENT ROOM        |                   |
| 103-110-JC | 110  | CCU | MEDICINE                   |                   |
| 105-148    | 148  | C   | EXAM/TREATMENT ROOM        |                   |
| 200-110A   | 110A | A2  | LABORATORY LAB             |                   |
| 200-140    | 140  | F1  | MEDICAL ADMINISTRATION     | OFFICE, SECRETARY |
| 200-148    | 148  | A   | LAB                        |                   |
| 201-114    | 114  |     | INFORMATION SYSTEMS CENTER | OFFICE            |

^

Select ENG SPACE ROOM NUMBER: 201-114 114 INFORMATION SYSTEMS C ENTER OFFICE

At least how many days old?: (0-999): 0// ??

This response must be a number.

At least how many days old?: (0-999): 0// \<RET\>

Include PM Work Orders? NO// YES

Count(s) only? NO// ??

Enter either 'Y' or 'N'. Count(s) only? NO//

For ALL shops (say 'NO' if you only want OFFICE OF THE CHIEF)? No// \<RET\> (No)

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

INCOMPLETE WORK ORDERS (OFFICE OF THE CHIEF) MAY 5,1997@15:09 Page 1

WORK ORDER REQ DATE LOCATION EQUIP ID# CONTACT PRI. STAT EMPL ASSIGNED TASK DESCRIPTION

ACC \# S/P VENDOR P.O. \# EST.DEL. DEL.COMP.

There are no incomplete work orders that meet the search criteria in the OFFICE OF THE CHIEF Shop.

#### Status of Incomplete Work Orders by Location

This option is very similar to Status by Employee except that here you are asked to supply the location in question and an output device. The computer then prints or displays all the incomplete work orders whose location equals or contains the location entered by the user.

Select Incomplete Work Order Status Option: 3 Incomplete Work Orders by Location Search

Select ENGINEERING SECTION LIST: ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS
5.  AIR CONDITIONING PLT

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF

Should all LOCATIONS be included? YES// ??

Enter 'NO' if you want to screen your list by DIVISION, BUILDING, WING, and/or ROOM. If you enter 'YES' then all locations will be included and the sort order will be DIVISION, BUILDING, WING, and finally ROOM.

Should all LOCATIONS be included? YES// NO

Select one of the following:

1.  DIV, BLDG, WING, ROOM
2.  DIV, WING, BLDG, ROOM
3.  DIV, BLDG, ROOM
4.  BLDG, WING, ROOM
5.  WING, BLDG, ROOM
6.  BLDG, ROOM
7.  WING, ROOM
8.  ROOM

Choose 'SELECT BY' Parameters: 3// 1 DIV, BLDG, WING, ROOM Would you like to specify a range of LOCATIONS? NO// ?

Enter 'YES' if you want only some DIVISIONS, BUILDINGS, WINGS, or ROOMS. Enter 'NO' if you want to include all LOCATIONS.

Would you like to specify a range of LOCATIONS? NO//\< RET\> At least how many days old?: (0-999): 0// ??

This response must be a number.

At least how many days old?: (0-999): 0// \<RET\>

Include PM Work Orders? NO// YES

Count(s) only? NO// ?? Enter either 'Y' or 'N'. Count(s) only? NO// \<RET\>

For ALL shops (say 'NO' if you only want OFFICE OF THE CHIEF)? No// (No)

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

INCOMPLETE WORK ORDERS (OFFICE OF THE CHIEF) MAY 6,1997@09:44 Page 1

WORK ORDER REQ DATE LOCATION EQUIP ID# CONTACT PRI. STAT EMPL ASSIGNED TASK DESCRIPTION

ACC \# S/P VENDOR P.O. \# EST.DEL. DEL.COMP.

OC970424-002 04/24/97 221-114 21 ENTECH, ONE AVER 1

ENTECH, FOUR replacement equipment

OC970424-001 04/24/97 221-114 21 AVER 1

Electric bed replacement

1 TO 2 FOR EXPANDED DISPLAY: EXIT// \<RET \>

As in the first status option, you can have an expanded display of any work order (illustrated in the preceding examples) and can go from that to the TRANSACTION STATUS REPORT if parts have been ordered.

By pressing \<RET\>, you return to the Incomplete W.O. Status Category menu.

#### Status of Incomplete Work Orders by Shop

In this option the computer prompts you for the name of the Shop, number of days old and then prints out all incomplete work orders assigned to that section. This option also prompts for whether PM work orders should be included in the display. An expanded display of any Work Order shown is also available.

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS
5.  AIR CONDITIONING PLT

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// \<RET\>

At least how many days old?: (0-999): 0// ??

This response must be a number.

At least how many days old?: (0-999): 0// \<RET\>

Include PM Work Orders? NO// ??

If you answer 'YES' the Incomplete Work Order list will contain PM work orders. To get a list of 'regular' work orders only, just say 'NO'.

Include PM Work Orders? NO// YES YES Count(s) only? NO// ??

Enter either 'Y' or 'N'. Count(s) only? NO// \<RET\>

For ALL shops (say 'NO' if you only want OFFICE OF THE CHIEF)? No// \<RET\> (No)

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

INCOMPLETE WORK ORDERS (OFFICE OF THE CHIEF) MAY 6,1997@12:06 Page 1

WORK ORDER REQ DATE LOCATION EQUIP ID# CONTACT PRI. STAT EMPL ASSIGNED TASK DESCRIPTION

ACC \# S/P VENDOR P.O. \# EST.DEL. DEL.COMP.

OC970424-002 04/24/97 221-114 21 ENTECH, ONE AVER 1

ENTECH, FOUR replacement equipment

OC970424-001 04/24/97 221-114 21 AVER 1

Electric bed replacement

OC970408-001 04/08/97 AVER 1

Issued for delete pm work order.

1.  TO 3 FOR EXPANDED DISPLAY: EXIT// \< RET\>

#### Status of Incomplete Work Orders by Owner/Department

This option is nearly identical to the earlier options except that the computer prompts you for the name of the Owner/Department in question and then prints out all incomplete work orders assigned to that area.

Select Incomplete Work Order Status Option: 5 Incomplete Work Orders by Owner/Department

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS
5.  AIR CONDITIONING PLT
6.  BOILER PLANT
7.  SEWAGE PLANT

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF// Select SERVICE/SECTION NAME:??

Choose from:

ACQUISITION & MATERIAL MGMT 90

BLIND REHABILITATION

BUILDING MANAGEMENT DENTAL

ENGINEERING FISCAL 04

^

Select SERVICE/SECTION NAME: INFO

<table>
<colgroup>
<col style="width: 73%" />
<col style="width: 9%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>INFORMATION RESOURCES MGMT</p></li>
<li><p>INFORMATION SYSTEMS CENTER CHOOSE 1-2: <strong>2</strong></p></li>
</ol></th>
<th></th>
<th>IRM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>At least how many days old?: (0-999):</td>
<td>0//</td>
<td>??</td>
</tr>
<tr class="even">
<td>This response must be a number.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>At least how many days old?: (0-999): Include PM Work Orders? NO// <strong>??</strong></td>
<td>0//</td>
<td>&lt;RET&gt;</td>
</tr>
</tbody>
</table>

If you answer 'YES' the Incomplete Work Order list will contain PM work orders. To get a list of 'regular' work orders only, just say 'NO'.

Include PM Work Orders? NO// YES

Count(s) only? NO// ??

Enter either 'Y' or 'N'. Count(s) only? NO// \<RET\>

For ALL shops (say 'NO' if you only want OFFICE OF THE CHIEF)? No// (No)

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

INCOMPLETE WORK ORDERS (OFFICE OF THE CHIEF) MAY 6,1997@12:30 Page 1

| WORK ORDER    | REQ DATE LOCATION EQUIP ID# |        |         | CONTACT |          | PRI. STAT |
|---------------|-----------------------------|--------|---------|---------|----------|-----------|
| EMPL ASSIGNED | TASK DESCRIPTION            |        |         |         |          |           |
| ACC \#        | S/P                         | VENDOR | P.O. \# |         | EST.DEL. | DEL.COMP. |

OC970424-002 04/24/97 221-114 21 ENTECH, ONE AVER 1

ENTECH, FOUR replacement equipment

1.  TO 1 FOR EXPANDED DISPLAY: EXIT// \<RET \>

#### Transfer W.O. to Another Shop

Under this option an existing work order assigned to a particular shop may be re­ assigned to a new shop. The request date will remain the same. However, a new work order number will be generated based upon the time the request for transfer is made.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
58. Edit Work Order Data
59. Close Out Work Order
60. Display Work Order
61. Incomplete Work Order Status ...
62. Transfer W.O. to Another Shop
63. Print Equip. History by Entry Number
64. Disapprove Work Order
65. Reprint Work Orders (All Shops)
66. Print PM Manhours
67. Condition Code of Equipment Edit
68. Multiple Work Order Entry

The following example illustrates the process of transferring a work order to another shop.

Select Work Order & MERS Option: 6 Transfer W.O. to Another Shop Select ENGINEERING SECTION LIST: ??

Choose from:

1.  OFFICE OF THE CHIEF
69. ADMIN.+CLER.
70. SUPERVISORY OPERAT.
71. UTILITY OPERATIONS
72. AIR CONDITIONING PLT
73. BOILER PLANT
74. SEWAGE PLANT

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF

Transfer a work order from OFFICE OF THE CHIEF to another shop?

| Enter Yes or No: YES//  | \<RET\>       |         |                          |
|-------------------------|---------------|---------|--------------------------|
| Select WORK ORDER \#:   | OC970424-001  | 221-114 | Electric bed replacement |
| Transfer to which shop: | 50 INSPECTION |         |                          |

New WORK ORDER \#: IN970506-001

Edit this work order?

Enter Yes or No: YES// NO

Transfer a work order from OFFICE OF THE CHIEF to another shop? Enter Yes or No: NO// \<RET\>

#### Print Equip. History by Entry Number

An Equipment History, derived from previously entered work orders, is provided containing all work order numbers, device/description of work, equipment identification, total hours, total material cost, and turnaround time. This Equipment History is retrieved by Entry number. It may be called up by other identifiers than the Entry number. The following display is used for entering this option.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
75. Edit Work Order Data
76. Close Out Work Order
77. Display Work Order
78. Incomplete Work Order Status ...
79. Transfer W.O. to Another Shop
80. Print Equip. History by Entry Number
81. Disapprove Work Order
82. Reprint Work Orders (All Shops)
83. Print PM Manhours
84. Condition Code of Equipment Edit
85. Multiple Work Order Entry

The following example illustrates the process of printing equipment history by entry number.

Select Work Order & MERS Option: 7 Print Equip. History by Entry Number Select EQUIPMENT ENTRY \#: 50

50 91120508 BED (ONE WARD) TURNED IN

50 MHZ EISA PC 8 AB34300UER COMPUTER-PC-ADMINISTRATIVE T URNED IN

CHOOSE 1-2: 2 8

Compiling SORT TEMPLATE \[ENWOHIST2970507.103839\]

..

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

WORK ORDER HISTORY MAY 7,1997 10:38 PAGE 1 EQUIPMENT ID#: 8 CONDITION: CRITICALITY:

MANUF: DIGITAL EQUIP MODEL: 450STPCT25AA SERIAL: AB34300UER

WORK ORDER \# TASK DESCRIPTION WORK ACTION

| VENDOR       | TOTAL | TOTAL         | ENG. TURN   | TECH TURN   |
|--------------|-------|---------------|-------------|-------------|
| SERVICE COST | HOURS | MATERIAL COST | AROUND TIME | AROUND TIME |

COMMENTS

PM-OC9704M-002 PREVENTIVE MAINTENANCE

0.80 0 0

OC970505-001 Preventive maintenance requested.

PREVENTIVE MAINTENANCE

|       | 20.00 | 1.00 | 20.00 | 0   | 0   |
|-------|-------|------|-------|-----|-----|
|       |       |      |       |     |     |
| TOTAL | 20.00 | 1.80 | 20.00 | 0   | 0   |
| COUNT | 1     | 2    | 1     | 2   | 2   |
| MEAN  | 20.00 | 0.90 | 20.00 | 0   | 0   |

Press \<RETURN\> to continue.

Select EQUIPMENT ENTRY \#: \< RET\>

The headings indicate the data that can be obtained from this display. This data would be useful for replacement decisions on equipment.

Return to the Work Order & MERS option menu by pressing \< RET\> after the above display.

> **NOTE:** You may also obtain a type of Equipment Repair History from within the Equipment Management module (option ENIN-HIST-SPECIFIC). There are two major differences.

1.  Incomplete work orders will appear on a Work Order History, but not on the Equipment Management History.
2.  PM work orders that have been deleted will appear on the Equipment Management History, but not on a Work Order History.

#### Disapprove Work Order

This option records disapproval of a work request. Facilities which allow entry of Work Orders by non-Engineering personnel (commonly known as Electronic Work Requests) will probably make the greatest use of this option.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
86. Edit Work Order Data
87. Close Out Work Order
88. Display Work Order
89. Incomplete Work Order Status ...
90. Transfer W.O. to Another Shop
91. Print Equip. History by Entry Number
92. Disapprove Work Order
93. Reprint Work Orders (All Shops)
94. Print PM Manhours
95. Condition Code of Equipment Edit
96. Multiple Work Order Entry

The following example illustrates the process of disapproving a work order.

Select Work Order & MERS Option: 8 Disapprove Work Order

Select WORK ORDER \#: B970408-004 102-148 OPEN WORK ORDER

TASK DESCRIPTION (60 char): OPEN WORK ORDER// Open for miscellaneous preventive maintenance.

COMMENTS:

1\> \<RET\>

DATE COMPLETE (or closed): T// ??

Date on which work order is closed out.

DATE COMPLETE (or closed): T// \<RET\> (MAY 08, 1997)

Disapproval of an Electronic Work Order will automatically generate a MailMan message to the person who entered the request. This message will contain your COMMENTS. For this feature to work properly, you must enter your COMMENTS before you enter the DATE COMPLETE (or closed).

#### Reprint Work Orders (All Shops)

This option will reprint the work orders that were created within a specified range of dates. Reprint can be requested for all sections, or for a particular section entered after the default "ALL//" prompt. Work orders that have already been closed out will not be reprinted. Due to the length of this display, a single work order will be used to illustrate this feature. Here is an example of the process.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
97. Edit Work Order Data
98. Close Out Work Order
99. Display Work Order
100. Incomplete Work Order Status ...
101. Transfer W.O. to Another Shop
102. Print Equip. History by Entry Number
103. Disapprove Work Order
104. Reprint Work Orders (All Shops)
105. Print PM Manhours
106. Condition Code of Equipment Edit
107. Multiple Work Order Entry

The following example illustrates the process of reprinting a work order for all shops.

Select Work Order & MERS Option: 9 Reprint Work Orders (All Shops) For Engineering SECTION: ALL// ??

Choose from:

1.  OFFICE OF THE CHIEF
108. ADMIN.+CLER.
109. SUPERVISORY OPERAT.
110. UTILITY OPERATIONS
111. AIR CONDITIONING PLT
112. BOILER PLANT

^

For Engineering SECTION: ALL// 1 OFFICE OF THE CHIEF Start DATE:??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the PAST. You may omit the precise day, as: JAN, 1957

Start DATE: 4/1/97 (APR 01, 1997)

Stop DATE: 5/1/97 (MAY 01, 1997)

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

WORK ORDER \# OC970424-002

1\) PRIMARY EMPL: ENTECH, FOUR 2) REQ DATE: APR 24,1997@15:55

3\) REQ MODE: COMPUTER 4) LOCATION: 221-114

5\) BED \#: 6) STATUS: IN PROGRESS

TASK DESC: replacement equipment

CONTACT: ENTECH, ONE 9) PHONE: (515) 555-1211

10\) ENTERED BY: ENTECH, SEVEN 11) SHOP: OFFICE OF THE CHIEF

12\) DATE ASSIGNED: 04/24/97 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 21 15) LOCAL ID:

16\) EQUIP CAT: BED-ELECTRIC 17) CONDITION:

MFGR: ENMFGR, ONE

MODEL: 2300 20) SERIAL \#: 7888UYHG

21\) OWNER/DEPT: INFORMATION SYSTEMS CENTER 22) PM \#: 6530-6723

23\) PARTS ORDER: 24) WORK ACTION: E2

WORK CTR: 50200/UTILITY OPERATIONS

TOTAL HOURS: 10 27) TOTAL MATERIAL COST:

28\) TOTAL LABOR COST: 162.3 29) VENDOR SERVICE COST:

30\) \*ASSIGNED TECH\* 31) DATE COMPLETE: \#1: ENTECH, FOUR HRS: 10 SHOP: BIOMEDICAL

WORK PERFORMED:

COMMENTS:

Press \<RETURN\> to continue, '^' to escape... WARRANTY EXPIRATION: \*\*06/30/97\*\*

> **NOTE:** Equipment must be isolated and rendered inoperative prior to service.

\[OTHER OPEN WORK ORDERS FOR THIS EQUIPMENT\]

Work Order \# Task Description

B970131-001 TEST OF FLAGGING (Hazard) PM-B9705M-003 QUARTERLY PMI HOSPITAL BEDS

IN970506-001 Electric bed replacement B970203-001 TEST OF RIGHT EQ WO

#### Print PM Manhours

This option provides a report on the total manhours expended on preventive maintenance by shop and by month for each technician. These manhours are automatically recorded when PM work orders are closed out.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
113. Edit Work Order Data
114. Close Out Work Order
115. Display Work Order
116. Incomplete Work Order Status ...
117. Transfer W.O. to Another Shop
118. Print Equip. History by Entry Number
119. Disapprove Work Order
120. Reprint Work Orders (All Shops)
121. Print PM Manhours
122. Condition Code of Equipment Edit
123. Multiple Work Order Entry

The following example illustrates the process of printing PM Manhours.

Select Work Order & MERS Option: 10 Print PM Manhours

Previous selection: ENGINEERING SECTION not null START WITH ENGINEERING SECTION: FIRST// ??

Engineering Shop or Receiving Area for electronic work orders. Receiving Areas should be numbered so that they end with 90 thru 99, inclusive (ex: 90,91,190,295, etc.). Working shops should not be given numbers within the range reserved for Receiving Areas.

Previous selection: ENGINEERING SECTION not null START WITH ENGINEERING SECTION: FIRST// \<RET\>

Previous selection: PM MONTH not null

START WITH PM MONTH: FIRST// ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. You may omit the precise day, as: JAN, 1957

Previous selection: PM MONTH not null START WITH PM MONTH: FIRST// \<RET\>

DEVICE: \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

PREVENTIVE MAINTENANCE MANHOURS MAY 13,1997 11:37 PAGE 1

PM MONTH TECHNICIAN MANHOURS

ENGINEERING SECTION: BIOMEDICAL

| DEC 1993   |                      |     | ENTECH, F IVE     |     | 0.80   |        |
|------------|----------------------|-----|-------------------|-----|--------|--------|
| JUN 1995   |                      |     | ENTECH, TEN       |     | 0.80   |        |
| MAY 1996   |                      |     | ENTECH, FOUR      |     | 268.00 |        |
| JUL 1996   |                      |     | ENTECH, FOUR      |     | 160.00 |        |
| NOV 1996   |                      |     | ENTECH, FOUR      |     | 2.40   |        |
| DEC 1996   |                      |     | ENTECH, TEN       |     | 0.60   |        |
| FEB 1997   |                      |     | ENTECH, FOUR      |     | 2.40   |        |
| PREVENTIVE | MAINTENANCE MANHOURS |     | MAY 13,1997 11:37 |     |        | PAGE 2 |
| PM MONTH   | TECHNICIAN           |     | MANHOURS          |     |        |        |

APR 1997 ENTECH, TEN 1.00

ENTECH, FOUR 0.80

MAY 1997 ENTECH, FOUR 804.00

NOV 1997 ENTECH, FOUR 0.00

ENTECH, S IX 0.00

APR 1998 ENTECH, TEN 1.60

ENGINEERING SECTION: ELECTRIC

NOV 1997 ENTECH1, ONE 0.00

#### Condition Code of Equipment Edit

This option is used to access a utility for updating the condition code of equipment without closing an associated work order.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
124. Edit Work Order Data
125. Close Out Work Order
126. Display Work Order
127. Incomplete Work Order Status ...
128. Transfer W.O. to Another Shop
129. Print Equip. History by Entry Number
130. Disapprove Work Order
131. Reprint Work Orders (All Shops)
132. Print PM Manhours
133. Condition Code of Equipment Edit
134. Multiple Work Order Entry

The following example illustrates the Condition Code of Equipment Edit.

Select Work Order & MERS Option: 11 Condition Code of Equipment Edit Select EQUIPMENT INV. ENTRY NUMBER: ??

Choose from:

2221 IN USE

91120526 TURNED IN

3 3290A00220 IN USE

4 3301A01107 IN USE

5 3301A01105 IN USE

^

Select EQUIPMENT INV. ENTRY NUMBER: 50

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 32%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1</p>
<p>2</p></th>
<th colspan="3"><p>50 91120508</p>
<p>50 MHZ EISA PC 8</p></th>
<th>BED (ONE WARD) AB34300UER</th>
<th><p>TURNED IN</p>
<p>COMPUTER-PC-ADMINISTRATIVE</p></th>
<th>T</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">URNED IN</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">CHOOSE 1-2:</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">CONDITION CODE:</td>
<td>??</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Condition code of equipment is normally determined by an Engineering technician and entered during close out of a work order. The code is:

1.  LIKE NEW - Like new condition, good performance record, low service cost.
135. GOOD - Middle of service life, fair performance record, increasing service cost.
136. POOR - Approaching end of service life, poor performance record, high service cost, consider budgeting for replacement.

Choose from:

1.  LIKE NEW
137. GOOD
138. POOR

CONDITION CODE: 2 GOOD

Select EQUIPMENT INV. ENTRY NUMBER: \<RET\>

#### Multiple Work Order Entry

This option allows the user to create (and optionally close) multiple work orders for equipment. First, a new work order is entered in full (see Enter New Work Order if explanations of the prompts are needed) and then additional equipment is selected.

Equipment can be selected by equipment category, manufacturer, and/or model. Alternatively, equipment can be individually specified. The computer will create new work orders for each selected equipment item by copying the original work order. Equipment-specific data on the work orders (e.g. location, serial number, etc.) will be obtained from the Equipment Inv. file.

ENGINEERING WORK ORDER MODULE

1.  Enter New Work Order
139. Edit Work Order Data
140. Close Out Work Order
141. Display Work Order
142. Incomplete Work Order Status ...
143. Transfer W.O. to Another Shop
144. Print Equip. History by Entry Number
145. Disapprove Work Order
146. Reprint Work Orders (All Shops)
147. Print PM Manhours
148. Condition Code of Equipment Edit
149. Multiple Work Order Entry

The following example illustrates the Multiple Work Order Entry.

Select Work Order & MERS Option: 12 Multiple Work Order Entry Enter a new equipment work order and copy it (Y/N)? YES// Select ENGINEERING SECTION LIST: biomedICAL.

WORK ORDER \#: B970707-001 (JUL 07, 1997@15:23) REQUEST DATE: JUL 7,1997@15:23//

REQUEST MODE: COMPUTER// COMPUTER EQUIPMENT ID#: 8978899

LOCATION: 201-110// BED \#:

TASK DESCRIPTION (60 char): The Coulter counter is clogged and needs flushing. STATUS: IN PROGRESS// IN PROGRESS

CONTACT PERSON: ENDIR, ONE

PHONE: 3014273700

DATE ASSIGNED: JUL 7,1997// (JUL 07, 1997) PRIMARY TECH ASSIGNED: ENTECH1, THREE PRIORITY: A// AVERAGE

OWNER/DEPARTMENT: INFORMATION SYSTEMS CENTER// labORATORY

Select WORK ACTION: genERAL REPAIR (In-house) G1 WORK CENTER CODE:??

WORK CENTER CODE: 55511 55511/CLINICAL LAB EQUIP, REPAIR COMMENTS:

1\>

Do you want to CLOSE this work order now (Y/N)? NO//

Do you want to print this work order (Y/N)? YES// n NO Select one of the following:

SEARCH EQUIPMENT FILE BY CATEGORY, MANUFACTURER, OR MODEL

INDIVIDUALLY SELECT EQUIPMENT

Choose desired method to select additional equipment.

USE METHOD:: 1// 1 SEARCH EQUIPMENT FILE BY CATEGORY, MANUFACTURER, OR MODEL

Select items with EQUIPMENT CATEGORY: defib.

1.  DEFIBRILLATOR
150. DEFIBRILLATOR ANALYZER ANALYZER-DEFIBRILLATOR CHOOSE 1-2: 1

Select items with MANUFACTURER:?

Firm that actually manufactured this equipment, not necessarily the company from which it was purchased.

Select items with MANUFACTURER: \<RET\> Select items with MODEL:??

Model number or designation, normally assigned by manufacturer. Spaces and punctuation may be included.

Select items with MODEL: \<RET\>

Work Orders will be copied for 6 items of equipment OK to Proceed: (Y/N/L):??

Select appropriate action.

YES to create work orders for selected equipment NO to select different equipment.

LIST to list currently selected equipment.

^ to exit and delete original work order

OK to Proceed: (Y/N/L): L LIST DEVICE: HOME// UCX/TELNET

Multiple Work Order Equipment List JUL 07, 1997 page 1 Control \# Equipment Category Manufacturer Model

(Master Equipment Work Order) B970707-001 IN PROGRESS

1 DEFIBRILLATOR ENMFGR, TWO 8700

(Equipment Selected)

64 DEFIBRILLATOR ENMFGR, THREE LIFEPAK6

151 DEFIBRILLATOR ENMFGR, FOUR JS20

DEFIBRILLATOR

DEFIBRILLATOR

DEFIBRILLATOR

DEFIBRILLATOR

Work Orders will be copied for 6 items of equipment OK to Proceed: (Y/N/L): y YES

Should all new work orders be printed? (Y/N)? NO// y YES Select DEVICE NAME: 2// LAT-QUME LAT \_LTA

Copying work order for selected equipment......

All work orders created.

Select output device for list or enter '^' to suppress report DEVICE: HOME// UCX/TELNET

| Multiple Work            | Order Equipment List      | JUL 07, 1997 | page 1 |
|--------------------------|---------------------------|--------------|--------|
| Work Order \# Control \# | Status Equipment Category | Manufacturer | Model  |

(Master Equipment Work Order) B970707-001 IN PROGRESS

1 DEFIBRILLATOR ENMFGR, TWO 8700

(Equipment Work Orders Copied from Master) B970707-002 IN PROGRESS

64 DEFIBRILLATOR ENMFGR, THREE LIFEPAK6

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 39%" />
<col style="width: 26%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>B970707-003</th>
<th>IN PROGRESS</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>151</p>
<p>B970707-004</p></td>
<td><p>DEFIBRILLATOR</p>
<p>IN PROGRESS</p></td>
<td>ENMFGR, FOUR</td>
<td>JS20</td>
</tr>
<tr class="even">
<td>198</td>
<td>DEFIBRILLATOR</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>B970707-005</td>
<td>IN PROGRESS</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Year Facility Plan and Project Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The original Project Planning menu option contained all the options relevant to Project Applications and the 5 Year Facility Plan. It has now been split into two menu options: one for 5 Year Facility Plan and one for Project Applications. The new menu structure more clearly indicates which options are applicable to the Five-Year Plan process and which options are applicable to the Project Application process. The options are selected from the Engineering main menu by entering the first few letters of the option or the synonym s "FYFP" for the 5 Year Facility Plan options or "APPL" for the Project Applications options.

AUTOMATED ENGINEERING MANAGEMENT SYSTEM VERSION 7

WASH.ENC

Jul 20, 1995 10:52:54 am

Select Engineering Main Menu Option:?

WO Work Order & MERS ...

FYFP Five Year Facility Plan (FYFP) ... APPL Project Applications ...

TRK Project Tracking ...

EQ Equipment Management ... ENM Program Management ...

SP Space/Facility Management ... FSA 2162 Report of Accident ...

XFER Assign (Transfer) Electronic Work Orders

Enter ?? for more options, ??? for brief descriptions,? OPTION for help text.

### Five Year Facility Plan (FYFP) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Engineering Main Menu Option: fyfp Five Year Facility Plan (FYFP) Edit 5-Yr Plan Project.

Activations E/E

Five Year Facility Plan Report (132 columns) Validate 5-Yr Plan Projects.

Transmit 5-Yr Plan Projects Communication Log Display for a Project

Edit 5-Yr Plan Project Option name: ENXFM02.

This option enables entry of information that appears on the 5-Yr Plan for each project.

Activations E/E Option name: ENXFM18

This option enables enter/edit of project activations information.

Five Year Facility Plan Report (132 columns) Option name: ENXFM11

This option prints the 5-Yr Plan, selecting items on the basis of Funding Year A/E, Funding Year Construction, FY Rent Starts, and Project Status fields. The range of plan years printed can be selected with the Start with Year: and the Go to Year: prompts. The output can be further modified with the Level of Detail: prompt. Take the default responses to these three prompts to generate a standard 5-Yr Plan report.

Validate 5-Yr Plan Projects Option name: ENXFMFV.

This option validates selected construction and lease projects. Only data which pertains to the Five-Year Facility Plan (FYFP) is checked. Any validation errors or warnings are listed in a detailed report.

Transmit 5-Yr Plan Projects Option name: ENXFMFX.

This option transmits construction and lease project data to the Regional Construction Database for selected projects. Only data which is pertinent to the Five-Year Facility Plan (FYFP) is sent. Selected projects are automatically validated prior to the actual transmission. The transmitter is a recipient of any created mail messages that are sent to the Regional Construction Database.

Communication Log Display for a Project Option name: ENXFM20 This option displays the communication log for a selected project. The

communication log contains information on network messages exchanged between the site and the regional construction database. "5-Yr" indicates Five Year Plan related messages and "Appl" indicates project application related messages.

### Edit 5-Yr Plan Project.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows those fields which either control or are controlled by other fields. The right-hand column shows the controlling conditions. The controlling condition must be true for the field to be asked.

| 5-Yr Plan Project E/E     | Controlling Conditions          |
|-------------------------------|-------------------------------------|
| BONUS CATEGORY                | PROGRAM is NRM                      |
| AMBULATORY CARE PERCENTAGE    | PROGRAM is NRM                      |
| FUNDING YEAR - A/E            | PROGRAM is Major, Minor, Minor-     |
|                               | Misc, or NRM                        |
| ESTIMATED A/E COST (FYFP)     | PROGRAM is Major, Minor, Minor-     |
|                               | Misc, or NRM                        |
| FUNDING YEAR - CONST          | PROGRAM is Major, Minor, Minor-     |
|                               | Misc. or NRM                        |
| ESTIMATED CONST COST (FYFP)   | PROGRAM is Major, Minor, Minor-     |
|                               | Misc. or NRM                        |
| LEASE TYPE                    | PROGRAM equals LEASE                |
| PROPOSED LEASE TERM           | PROGRAM equals LEASE                |
| RENTABLE SQ FT                | PROGRAM equals LEASE                |
| NET PARKING CHANGE            | PROGRAM equals LEASE                |
| FY AWARD LEASE                | PROGRAM equals LEASE                |
| ESTIMATED LUMP SUM COST       | PROGRAM equals LEASE                |
| FY RENT STARTS                | PROGRAM equals LEASE                |
| ESTIMATED ANNUAL RENT COST    | PROGRAM equals LEASE                |
| EXISTING SPACE ANNUAL RENT    | LEASE TYPE equals NEW               |
|                               | LEASE/EXISTING PRESENCE or          |
|                               | SUCCEDING                           |
| EXISTING SPACE RENTABLE SQ FT | LEASE TYPE equals NEW               |
|                               | LEASE/EXISTING PRESENCE or          |
|                               | SUCCEDING                           |
| EDIT ACTIVATIONS?             | Only asked if a funding year is the |
|                               | budget year or budget year +1       |
| ACTIVATION RESOURCES REQ IN   | Edit Activations is answered YES    |
| FY                            |                                     |
| ADDITIONAL FTEE               | Edit Activations is answered YES    |
| RECURRING PS                  | Edit Activations is answered YES    |
| EQUIPMENT \$                  | Edit Activations is answered YES    |
| RECURRING ALL OTHER \$        | Edit Activations is answered YES    |
| NONRECURRING ALL OTHER        | Edit Activations is answered YES    |
| TRAVEL .007                   | Edit Activations is answered YES    |
| BUILDING NUMBER               | PROGRAM is Major, Minor, Minor-     |
|                               | Misc, or NRM                        |
| MCPS SCORE                    | PROGRAM is MAJOR                    |
| NHCU BEDS (NEW)               | PROJECT CATEGORY or BONUS           |
|                               | CATEGORY contains NHCU              |
| NHCU BEDS (RENOVATED)         | PROJECT CATEGORY or BONUS           |
|                               | CATEGORY contains NHCU              |
| NHCU BEDS (CONVERTED)         | PROJECT CATEGORY or BONUS           |
|                               | CATEGORY contains NHCU              |

Select Five Year Facility Plan (FYFP) Option: edit 5-Yr Plan Project.

Budget Year of 5-Yr Plan: (1995-2099): 1997//??

Enter a Fiscal Year between 1995 and 2099

> **NOTE:** This is the Plan's, not the Project's Budget Year

This year enables differentiation among current, budget and out year projects.

Budget Year of 5-Yr Plan: (1995-2099): 1997// Select PROJECT NUMBER:??

Choose from:

999-00-101 SEALCOAT PARKING LOTS PH II

999-01-101 ENERGY AUDIT

...

...

999-383 RENOVATE MED/CLINICAL

999-399 TEST OF MINOR PROJECT TRANSMISSION

^

You may enter a new CONSTRUCTION PROJECT, if you wish

ENTER THE OFFICIALLY ASSIGNED PROJECT NUMBER (must begin with 3

numerics and use dashes as delimiters)

Must begin with station number. Enter '??' for more help. Select PROJECT NUMBER: 999-97-110 NHCU BED CONVERSION PROJECT NUMBER: 999-97-110//

MEDICAL CENTER: ANYCITY//??

Facility where the work is being performed. May indicate.

a division or other functional element (National Cemetery, Regional Office, satellite clinic, etc.) if appropriate.

| Choose from:              |          |       |       |
|---------------------------|----------|-------|-------|
| VASITE.VA.GOV             | ANYSTATE |       | 590   |
| ISCEXAMPLE                | ANYSTATE | ISC   | 12000 |
| VA MED CENTER             | ANYSTATE |       | 111   |
| ANYCITY                   | ANYPLACE | MC(M) | 999   |
| MEDICAL CENTER: ANYCITY// |          |       |       |

A new DIVISION (#6910.3) file has been added. It contains a list of valid divisions for a multi-divisional facility. It can be edited using the DIVISION \[ENDIV\] option on the Program Management menu. There is no need to enter any divisions if it is not applicable for your site. The DIVISION (#176) field in the CONSTRUCTION PROJECT (#6925) file has been changed to point to the new Division file.

DIVISION:??

This field is used to identify the division of a multi-divisional facility. It can be used to generate a division specific report when printing the Five-Year Facility Plan.

Choose from: ALPHA BETA DIVISION

DIVISION:

Project titles entered with lowercase letters will automatically be converted to all uppercase letters. This change has been made to promote consistency in national databases and reports.

PROJECT TITLE: NHCU BED CONVERSION//??

Official title of project.

PROJECT TITLE: NHCU BED CONVERSION// FACILITY TYPE: VETERANS HEALTH ADMIN//??

This field is important to enable restriction of Project Functional and Budget Categories and to enable reporting by Facility Type. Note: The cross reference was added to 2 reasons: a) Facilitate reporting by facility type. b) Force the filing by DIE so that the selection screens

/Filters work properly for Functional and Budget Categories. Choose from:

VHA VETERANS HEALTH ADMIN VBA VETERANS BENEFITS ADMIN

NCS NATIONAL CEMETERY SERVICE FACILITY TYPE: VETERANS HEALTH ADMIN//

PROGRAM: NRM//??

This field is a set of codes used to classify program type. Choose from:

MA MAJOR

MI MINOR

MM MINOR MISC.

NR NRM

| OT  | OTHER         |
|-----|---------------|
| LE  | LEASE         |
| SL  | STATION LEVEL |

A capture of the dialogue for the LEASE prompts may be seen following this capture.

PROGRAM: NRM// STATUS: PLAN//??

The default STATUS when entering a new project is "DRAFT". The status must be changed to "DESIGN PROGRAM", "A/E", "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", "AUTHORIZED", "INVITATION FOR BID", "BID OPEN" or "CONSTRUCTION" to be included as a

current year project in the Five-Year Plan. The status must be changed to "PLAN", "NEW PROJECT APPLICATION", "DESIGN PROGRAM", "A/E" "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", or

"AUTHORIZED" to be included as a budget year or later project in the Five-Year Plan.

DRAFT PROJECT PLAN

NEW PROJECT APPLICATION AUTHORIZED

A/E

INVITATION FOR BID, BID OPEN, CONSTRUCTION COMPLETED, PROJECT CANCELED, UNAPPROVED/VIABLE, NON-VIABLE

Present status of the project.

Choose from: A/E AUTHORIZED BID OPEN CANCELED

COMPLETED PROJECT CONSTRUCTION DRAFT PROJECT

INVITATION FOR BID

NEW PROJECT APPLICATION NON-VIABLE

PLAN UNAPPROVED/VIABLE

STATUS: PLAN//

PROJECT CATEGORY: PATIENT ENVIRONMENT/PRIVACY//??

This field is a pointer to the OFM Project Category File (#7336.8). The field designates the project functional category, and determines prioritization points for NRM, Minor, and Minor Misc. programs.

Choose from: ARCHITECTURAL BARRIERS ASBESTOS

...

...

WASTE MANAGEMENT WINDOWS

PROJECT CATEGORY: PATIENT ENVIRONMENT/PRIVACY//

There is a new required field for NRM projects called BONUS CATEGORY (#158.8). This field is scope dependent and 'Not Applicable' should be entered as the Bonus Category if none of the other choices involve 50% or more of the project scope.

BONUS CATEGORY: NHCU//??

This field designates the bonus category which involves 50% or more of the project scope and determines prioritization points for NRM projects. 'Not Applicable' should be selected if none of the other choices meet the 50% scope requirement.

Choose from: AMBULATORY CARE EDUCATION ENERGY

NHCU

NOT APPLICABLE RESEARCH

BONUS CATEGORY: NHCU//

There is a new field for NRM projects called AMBULATORY CARE PERCENTAGE (#158.9). It should be entered for all NRM 5-Yr Plan projects.

AMBULATORY CARE PERCENTAGE: 90//??

This field contains the project scope percentage for ambulatory care.

AMBULATORY CARE PERCENTAGE: 90//

The BUDGET CATEGORY defaults are provided based on the PROJECT CATEGORY entered for Major, Minor, and Minor Misc projects, and should be accepted unless otherwise approved by the Regional Office. NRM budget categories should be selected based on guidance in the call letter for the NRM program.

BUDGET CATEGORY: NHCU BED CONV//??

This field is a pointer to the OFM Budget Category File (#7336.9). The field designates the project budget category. Choices are screened based on program type.

Choose from: ASBESTOS/IH BIOMEDICAL BOILERS/INCINERATORS ENERGY

FIRE AND SAFETY HVAC

NHCU

NHCU BED CONV OTHER

STRUCTURAL IMPROVEMENTS UTILITY SYSTEMS

BUDGET CATEGORY: NHCU BED CONV// FUNDING YEAR - A/E: 1997//??

This field contains the fiscal year for which A/E is funded or proposed.

FUNDING YEAR - A/E: 1997//

The estimated cost for construction projects (Major, Minor, Minor Misc, and NRM) will be entered into two new fields, ESTIMATED A/E COST (FYFP) and ESTIMATED CONST COST (FYFP), instead of using the single ESTIMATED COST FOR 5 YR PLAN field. Values entered into these fields will automatically be rounded up to the next thousand.

ESTIMATED A/E COST (FYFP): 11000//??

This field contains the estimated A/E cost of the project for the Five-Year Facility Plan (FYFP). It will be used on the FYFP in the project's Funding Year - A/E. The total estimated cost of the project is the sum of this field and the ESTIMATED CONST COST (FYFP) field.

ESTIMATED A/E COST (FYFP): 11000// FUNDING YEAR - CONST: 1997//??

Fiscal year for which construction is funded or proposed.

FUNDING YEAR - CONST: 1997//

ESTIMATED CONST COST (FYFP): 100000//??

This field contains the estimated construction cost of the project for the Five-Year Facility Plan (FYFP). It will be used on the FYFP in the project's Funding Year - Const. The total estimated cost of the project is the sum of this field and the ESTIMATED A/E COST (FYFP) field.

ESTIMATED CONST COST (FYFP): 100000//

The PROJECT DESCRIPTION (SHORT) field is for a short (approx. 3 lines) project description. A longer description may be entered in the LONG DESCRIPTION field during the Project Application Enter/Edit.

PROJECT DESCRIPTION (SHORT):

1\>Convert building to NHCU beds.

EDIT Option:

The JUSTIFICATION (SHORT) field is for a short (approx. 3 lines) project justification. A longer justification may be entered in the LONG JUSTIFICATION field during the Project Application Enter/Edit.

JUSTIFICATION (SHORT):

1\>Population in nursing home is projected to increase.

EDIT Option:

Edit Activations? Y//?? Enter 'Y' or 'N'.

Activations are funding and FTEE resources required to bring the subject area of the construction or maintenance project up to full operational capacity.

Activations data is required only for Budget Year and Budget Year +1.

Edit Activations? Y// ACTIVATIONS

ACTIVATION RESOURCES REQ IN FY: 1998//??

This field contains the fiscal year activation resources are required.

ACTIVATION RESOURCES REQ IN FY: 1998// ADDITIONAL FTEE: 1//??

This field contains the total Additional FTEE number as documented in the detailed activation documentation.

ADDITIONAL FTEE: 1// RECURRING PS: 0//??

This field contains the total Recurring Personnel Service (PS) funds in accordance with the Additional FTEE.

RECURRING PS: 0// EQUIPMENT \$: 13500//??

This field contains the total activation equipment funds required to support the project with the following exception. For NRM projects, any equipment items (or systems) that cost over \$250,000 should NOT be included in this figure since such high-cost equipment must be applied for separately under the High-Cost Equipment Program. For Leases and Minor, Minor Misc and Major projects, any equipment items (or systems) that cost

\$250,000 should be included in this figure since such high-cost equipment cannot be applied for under the High-Cost Equipment Program.

EQUIPMENT \$: 13500// RECURRING ALL OTHER \$: 0//??

This field contains the total Recurring All Other Funds required to support the project.

RECURRING ALL OTHER \$: 0// NONRECURRING ALL OTHER: 2000//??

This field contains the total Non-Recurring All Other funds required to support the project.

NONRECURRING ALL OTHER: 2000// TRAVEL .007: 50//??

This field contains the total Travel .007 funds required to support the project.

TRAVEL .007: 50//

CITATIONS is a multiple field for entering citations issued to the site.

CITATIONS

Select CITATION NAME: JCAHO CITED//??

JCAHO CITED

This field contains the name of any citations associated with a project. (e.g. JCAHO citations)

If a citation is entered here, the following fields are presented.

Select CITATION NAME: JCAHO CITED// CITATION NAME: JCAHO CITED// DATE: DEC 25,1994//??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. This field contains the date the citation was issued.

DATE: DEC 25,1994//

CITING AUTHORITY: JOINT COMM ON ACCREDITATION HEALTH CARE ORG

// ??

This field contains a pointer to the Regulatory Agency File (#7335.7).

Choose from:

ASSOC FOR ACCREDITATION OF LAB CITY

COLLEGE OF AMERICAN PATHOLOGISTS’ COUNTY

ENVIRONMENTAL PROTECTION AGENCY FOOD AND DRUG ADMINISTRATION GENERAL ACCOUNTING OFFICE INSPECTOR GENERAL DVA

JOINT COMM ON ACCREDITATION HE NATIONAL FIRE PROTECTION ASSOC NUCLEAR REGULATORY COMMISSION OCCUPATIONAL SAFETY AND HEALTH OTHER

REGIONAL SAFETY & FIRE PROTECT STATE

UNIFORM FEDERAL ACCESSIBILITY

CITING AUTHORITY: JOINT COMM ON ACCREDITATION HEALTH CARE ORG

// PAGE: 1//??

This field contains the page number in the citing agency's report that contains the citation.

PAGE: 1//

OFFICIALS NAME: ENTECH1, FOUR// ??

This field contains the name of the official issuing the citation.

OFFICIALS NAME: ENTECH1, FOUR// OFFICIALS TITLE: INSPECTOR// ??

This field contains the title of the official issuing the citation.

OFFICIALS TITLE: INSPECTOR//

CORRECTION \>50% PROJECT SCOPE: YES//??

This field is a set of codes (Yes or No) used to determine if correction of the citation is greater than 50% of the project scope. The field is used to determine if prioritization points will be awarded for NRM and Minor/Minor Misc. programs.

Choose from:

1 YES

0 NO

CORRECTION \>50% PROJECT SCOPE: YES// Select CITATION NAME:

EQUIPMENT OVER \$250K

This is a multiple entry field for equipment over \$250K.

Select EQUIPMENT OVER \$250K NAME: BLOWER//??

BLOWER

This field contains a 3–30-character name for an equipment item over.

\$250,000.

Select EQUIPMENT OVER \$250K NAME: BLOWER// EQUIPMENT OVER \$250K ITEM: BLOWER// QUANTITY: 1//??

This field contains the quantity of the equipment item.

QUANTITY: 1//

UNIT COST: 256000//??

This field contains the unit cost of the equipment item.

UNIT COST: 256000// ADDITIONAL/REPLACEMENT: ADDITIONAL//??

This field identifies equipment over \$250K as additional or replacement equipment.

Choose from:

ADDITIONAL

R REPLACEMENT ADDITIONAL/REPLACEMENT: ADDITIONAL//

Select EQUIPMENT OVER \$250K NAME:

Select BUILDING NUMBER: 114//??

114

This field contains a building number associated with the project.

Choose from:

1

2

5

7

28

85

110

114

135

0001

100-OPC

101-OPC

201-OPC

Select BUILDING NUMBER: 114// NHCU BEDS (NEW): 0//??

Number of nursing home beds to be created via project.

NHCU BEDS (NEW): 0//

NHCU BEDS (RENOVATED): 0//??

Net (+/-) nursing home care beds impacted by this project.

NHCU BEDS (RENOVATED): 0// NHCU BEDS (CONVERTED): 30//??

Number of beds to be converted into nursing home beds via this project.

NHCU BEDS (CONVERTED): 30//

Validating Projects.

No validation problems found Select PROJECT NUMBER:

Dialogue for LEASE prompts.

If you are entering a Leased Space project, you will see the following prompts after PROGRAM:

PROGRAM: LEASE// STATUS: PLAN//

PROJECT CATEGORY: DIRECT PATIENT CARE// BUDGET CATEGORY: VACO//

LEASE TYPE: NEW LEASE/EXISTING PRESENCE//??

This field contains the type of lease. New Lease/New Presence is a first-time lease where no presence exists and there is no existing lease. New Lease/Existing Presence is a lease where there is a change in location, increase or decrease in space, or some change other than a re-negotiation of cost and all renewal options have expired. A Succeeding lease is a lease where there is no change other than cost and all lease renewal options have expired. An Expedited lease is a lease, fully funded by the facility, that meets the terms of the Expedited Lease Directive. An Enhanced Use lease is a lease where costs are shared between the VA and an outside source such as state, city, county government or private enterprise.

Choose from:

| NN  | NEW LEASE/NEW PRESENCE      |
|-----|-----------------------------|
| NE  | NEW LEASE/EXISTING PRESENCE |
| SU  | SUCCEEDING                  |
| EX  | EXPEDITED                   |
| EU  | ENHANCED USE                |

LEASE TYPE: NEW LEASE/EXISTING PRESENCE// PROPOSED LEASE TERM: 5//??

This field contains the term of the lease in years, including all renewal options.

PROPOSED LEASE TERM: 5//

RENTABLE SQ FT: 1000//??

This field contains the total net square feet to be used by the VA occupants. Include any waiting space or common areas. If waiting space is shared by tenants other than the VA, estimate and apportion the space. Do not include corridors, equipment rooms, telephone closets, etc. in the rentable square feet.

RENTABLE SQ FT: 1000// NET PARKING CHANGE:??

This field contains the change (if any) in the number of parking stalls available.

NET PARKING CHANGE:

FY AWARD LEASE: 1997//??

This field contains the fiscal year the lease cost and/or build-out funds are obligated against the lease contract.

FY AWARD LEASE: 1997//

ESTIMATED LUMP SUM COST: 13000//??

This field contains the estimated lump sum cost paid up-front for

build-out or modifications to the property made at the request of and paid for by the VA.

ESTIMATED LUMP SUM COST: 13000// FY RENT STARTS: 1997//??

This field contains the fiscal year that monthly lease payments commence. This may differ from the award date due to build-out or a negotiated delay of occupancy.

FY RENT STARTS: 1997//

ESTIMATED ANNUAL RENT COST: 120000//??

This field contains the total of the annual lease costs based on the 12-month period from the start of the lease.

ESTIMATED ANNUAL RENT COST: 120000// EXISTING SPACE ANNUAL RENT: 1234//??

This field contains the total annual lease costs based on the last 12-month period of the lease for the existing presence of a Succeeding or New Lease/Existing Presence type lease.

EXISTING SPACE ANNUAL RENT: 1234// EXISTING SPACE RENTABLE SQ FT: 300//??

This field contains the rentable square feet for the existing presence of a Succeeding or New Lease/Existing Presence type lease. Rentable square feet are the total net square footage used by VA occupants, including any waiting space or common areas. If waiting space is shared by tenants other than the VA, estimate and apportion the space. Do not include corridors, equipment rooms, telephone closets, etc. in the rentable square feet.

EXISTING SPACE RENTABLE SQ FT: 300// PROJECT DESCRIPTION (SHORT):

1\>This is the project description EDIT Option:

JUSTIFICATION (SHORT):

1\>This is the short justification.

EDIT Option:

Edit Activations? Y//??

### Activations E/E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit 5-Yr Plan Project.

\> Activations E/E

Five Year Facility Plan Report (132 columns) Validate 5-Yr Plan Projects.

Transmit 5-Yr Plan Projects Communication Log Display for a Project

Select Five Year Facility Plan (FYFP) Option: Activations E/E

Select PROJECT NUMBER: 999-383 RENOVATE MED/CLINICAL ACTIVATION RESOURCES REQ IN FY: 1997//??

This field contains the fiscal year activation resources are required.

ACTIVATION RESOURCES REQ IN FY: 1997// ADDITIONAL FTEE: 2//??

This field contains the total Additional FTEE number as documented in the detailed activation documentation.

ADDITIONAL FTEE: 2// RECURRING PS: 70000//??

This field contains the total Recurring Personnel Service (PS) funds in accordance with the Additional FTEE.

RECURRING PS: 70000// RECURRING ALL OTHER \$: 1//??

This field contains the total Recurring All Other Funds required to support the project.

RECURRING ALL OTHER \$: 1// EQUIPMENT \$: 1826000//??

This field contains the total activation equipment funds required to support the project with the following exception. For NRM projects, any equipment items (or systems) that cost over \$250,000 should NOT be included in this figure since such high-cost equipment must be applied for separately under the High-Cost Equipment Program. For Leases and Minor, Minor Misc and Major projects, any equipment items (or systems) that cost

\$250,000 should be included in this figure since such high-cost equipment cannot be applied for under the High-Cost Equipment Program.

EQUIPMENT \$: 1826000//

NONRECURRING ALL OTHER: 400000//??

This field contains the total Non-Recurring All Other funds required to support the project.

NONRECURRING ALL OTHER: 400000// TRAVEL .007: 9132//??

This field contains the total Travel .007 funds required to support the project.

TRAVEL .007: 9132//

### Five Year Facility Plan Report (132 columns)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5-Yr Plan Report Modifications:

| a\. | The output order has been changed to print all the year summary pages,    |
|-----|---------------------------------------------------------------------------|
|     | then the equipment pages, then the detail pages sorted by project number, |
|     | and finally the plan summary page.                                        |
| b\. | Network and VISN fields have been added to the ENG INIT                   |
|     | PARAMETERS file. If these fields are populated using the "ENG SITE        |
|     | PARAMETERS Enter/Edit" option, the information will be included in the    |
|     | header of the Five-Year Facility Plan report.                             |
| c\. | The Year Summary page has been modified to include Lease projects.        |
|     | Leases will be included in the year that corresponds to the FY RENT       |
|     | STARTS. The ESTIMATED ANNUAL RENT will be shown in the cost               |
|     | column. Expedited leases will be printed, but will not be included in the |
|     | count of leases.                                                          |

4.  The Equipment page has been modified to include a Lease section.
5.  The Detail page has been modified to use a new format. Different formats will be used for lease and construction projects.

> **NOTE:** Because of the built-in footers, it is advisable not to use a number higher than 60 to designate page length (i.e., DEVICE: HOME// :132;60)

*Reminder:* The A/E or Construction funding year of a project must be the current year (Budget year 1) or later. Current year projects must also have one the following statuses: "DESIGN PROGRAM", "A/E", "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", "AUTHORIZED", "INVITATION FOR BID", "BID OPEN" or "CONSTRUCTION". Budget and Out-

Year Projects must have one of the following statuses: "PLAN", "NEW PROJECT APPLICATION", "DESIGN PROGRAM", "A/E", "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", or "AUTHORIZED". The 3­

digit Project Number prefix must agree with the Station Number of the Institution selected, and the Program must not be blank.

Edit 5-Yr Plan Project Activations E/E

\> Five Year Facility Plan Report (132 columns) Validate 5-Yr Plan Projects

Transmit 5-Yr Plan Projects Communication Log Display for a Project

Select Five Year Facility Plan (FYFP) Option: five Year Facility Plan Report

(132 columns)

Budget Year of 5-Yr Plan: (1993-2099): 1997//?? Enter the 4-digit Budget Year of the Plan.

Budget Year of 5-Yr Plan: (1993-2099): 1997// \<RET\>

Select INSTITUTION NAME: 999//??

Choose from:

VASITE.VA.GOV ANYSTATE 590

ISCEXAMPLE ANYSTATE ISC 12000

VA MED CTR B ANYSTATE 111

ANYCITY ANYPLACE MC(M) 999

Select INSTITUTION NAME: 999// ANYCITY ANYPLACE MC(M) 999

> **NOTE:** The DIVISION prompt will only appear if your site is marked as Multi- Divisional in the Engineering Init Parameters file.

Select Division to be included in report or leave blank for all Select DIVISION NAME:??

Choose from: ALPHA BETA DIVISION

Select DIVISION NAME: \<RET\>

Start with year: 1996//??

Enter a 4-digit year from 1996 to 2001 or FUTURE Select one of the following:

1996 CURRENT YR

1997 BUDGET YR

1998 BUDGET YR+1

1999 BUDGET YR+2

2000 BUDGET YR+3

2001 BUDGET YR+4 FUTURE FUTURE YEARS

Start with year: 1996// \<RET\> CURRENT YR Go to year: FUTURE//??

Enter FUTURE or a four-digit year from 1996 to 2001 Select one of the following:

| 1996     | CURRENT YR  |     |                             |     |
|----------|-------------|-----|-----------------------------|-----|
| Year |             |     | Five Year Facility Plan |     |
|          |             |     | Project Applications    |     |
| 1997     | BUDGET YR   |     |                             |     |
| 1998     | BUDGET YR+1 |     |                             |     |
| 1999     | BUDGET YR+2 |     |                             |     |
| 2000     |             |     | BUDGET YR+3                 |     |
| 2001     |             |     | BUDGET YR+4                 |     |
| FUTURE   |             |     | FUTURE YEARS                |     |

Go to year: FUTURE// \<RET\> YEARS Level of detail: DEFAULT//??

L (LOWEST) Prints only project list pages.

S (SUMMARY) Prints project list and final summary pages. E (EQUIPMENT) Prints equipment page only.

D (DEFAULT) Prints project list, final summary,

and equipment list pages. Prints detail pages for BUDGET and BUDGET+1 years.

H (HIGHEST) Prints project list, final summary,

and equipment list pages. Prints detail pages for BUDGET through BUDGET+4 years.

Enter a code (L, S, E, D, or H) Select one of the following:

L LOWEST

S SUMMARY

E EQUIPMENT

D DEFAULT

H HIGHEST

Level of detail: DEFAULT// \<RET\>

DEVICE: HOME// ;132 LAN

> **NOTE:** Some Project Detail pages have been omitted to save space.

CURRENT YEAR APPROVED PROJECT LIST (FY 1996)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION</th>
<th>PROJ #</th>
<th>TITLE</th>
<th>COST</th>
<th>PROGRAM</th>
<th>PROJECT</th>
<th>MCPS</th>
<th>CITED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(in $000)</td>
<td></td>
<td>CATEGORY</td>
<td>SCORE</td>
<td>DEFICIENCY</td>
</tr>
<tr class="even">
<td>ALPHA</td>
<td><p>383</p>
<p>271</p></td>
<td>RENOVATE MED/CLINICAL RENOVATE OUTPATIENT CLINIC</td>
<td><p>$ 110 D</p>
<p>$ 667</p></td>
<td>MINOR MI-MISC</td>
<td>CLINICAL IMPROVEMENT OUTPATIENT IMPROVEME</td>
<td></td>
<td>JCAHO</td>
</tr>
<tr class="odd">
<td></td>
<td>96-101</td>
<td>RENOVATE 2CS</td>
<td>$ 110</td>
<td>NRM</td>
<td>CONSULTANT STUDY</td>
<td></td>
<td>JCAHO</td>
</tr>
<tr class="even">
<td></td>
<td>96-102</td>
<td>REPL MAIN ENTRANCE/VESTIBULE</td>
<td>$ 350</td>
<td>NRM</td>
<td>BUILDING SHELLS/INTE</td>
<td></td>
<td>NONE</td>
</tr>
</tbody>
</table>

---------­

TOTAL COST (Excluding Expedited Leases) \$ 1,237

Project Count LEASE (excludes Expedited) = 0 MAJOR = 0 MINOR = 1 MINOR MISC = 1 NRM = 2

- C = Construction dollars only D = Design dollars only

Page 1 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

FIVE YEAR FACILITY PLAN

VAMC: ANYCITY, DC (999) Region: 1 VISN: 3 Network: TRI-STATE BUDGET YEAR PROJECT LIST (FY 1997)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION PROJ</th>
<th>#</th>
<th>TITLE</th>
<th>COST</th>
<th>* PROGRAM</th>
<th>PROJECT</th>
<th>MCPS</th>
<th>CITED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALPHA 97-901</td>
<td></td>
<td>LEASE PROJECT</td>
<td><p>(in $000)</p>
<p>$ 120</p></td>
<td>LEASE</td>
<td><p>CATEGORY</p>
<p>DIRECT PATIENT CARE</p></td>
<td>SCORE</td>
<td><p>DEFICIENCY</p>
<p>JCAHO</p></td>
</tr>
</tbody>
</table>

97-902 EXPEDITED LEASE PROJECT \$ 25

DIVISION 499 OUTPATIENT CLINIC \$ 20,000

383 RENOVATE MED/CLINICAL \$ 990 C DIVISION 399 TEST OF MINOR PROJECT TRANSMIS \$ 70 D.

| 299     | RENOV. NUCLEAR MEDICINE | \$      | 650 | MI-MISC | GENERAL            | NONE  |
|---------|-------------------------|---------|-----|---------|--------------------|-------|
| 97-101A | SBESTOS PROJECT         | \$      | 130 | NRM     | ASBESTOS           | OTHER |
| 97-102  | RENOV. NURSE STATIONS,  | PH 6 \$ | 300 | NRM     | MINOR IMPROVEMENTS | NONE  |

LEASE ADMINISTRATION Non-MAJOR CLINICAL IMPROVEMENT 10.5 Non-MINOR CLINICAL IMPROVEMENT JCAHO

MINOR SEISMIC OTHER

- C = Construction dollars only D = Design dollars only

Page 2 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

BUDGET YEAR PROJECT LIST (FY 1997)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION</th>
<th>PROJ #</th>
<th>TITLE</th>
<th><p>COST</p>
<p>(in $000)</p></th>
<th>*PROGRAM</th>
<th><p>PROJECT</p>
<p>CATEGORY</p></th>
<th><p>MCPS</p>
<p>SCORE</p></th>
<th><p>CITED</p>
<p>DEFICIENCY</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"></td>
<td>97-103</td>
<td>REPL ROOFS/INST SAFETY RAILS</td>
<td>$500</td>
<td>NRM</td>
<td>ROOFS</td>
<td></td>
<td>NONE</td>
</tr>
<tr class="even">
<td>97-110</td>
<td>NHCU BED CONVERSION</td>
<td>$111</td>
<td>NRM</td>
<td>PATIENT ENVIRONMENT/</td>
<td></td>
<td>JCAHO</td>
</tr>
<tr class="odd">
<td>97-111</td>
<td>PROJECT TITLE</td>
<td>$5</td>
<td>NRM</td>
<td>ASBESTOS</td>
<td></td>
<td>NONE</td>
</tr>
<tr class="even">
<td>DIVISION</td>
<td>97-199</td>
<td>TEST OF NRM FIELDS TRANSFER</td>
<td>$110</td>
<td>NRM</td>
<td>BUILDING SHELLS/INTE</td>
<td></td>
<td>JCAHO</td>
</tr>
</tbody>
</table>

---------­

TOTAL COST (Excluding Expedited Leases) \$ 22,986

Project Count LEASE (excludes Expedited) = 1 MAJOR = 1 MINOR = 2 MINOR MISC = 1 NRM = 6

- C = Construction dollars only D = Design dollars only

Page 3 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

FIVE YEAR FACILITY PLAN

VAMC: ANYCITY, DC (999) Region: 1 VISN: 3 Network: TRI-STATE BUDGET YEAR PLUS ONE PROJECT LIST (FY 1998)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION</th>
<th>PROJ #</th>
<th>TITLE</th>
<th><p>COST</p>
<p>(in $000)</p></th>
<th>*PROGRAM</th>
<th><p>PROJECT</p>
<p>CATEGORY</p></th>
<th><p>MCPS</p>
<p>SCORE</p></th>
<th><p>CITED</p>
<p>DEFICIENCY</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

98-901 PARKING GARAGE LEASE \$ 150 LEASE PARKING NONE

ALPHA 98-999 TEST OF LEASE PROJECT TRANSMIS \$ 96 LEASE DIRECT PATIENT CARE JCAHO, RSFPE

302 STREETS/PARKING \$ 290 D MINOR GENERAL NONE

| 98-101 REPL NORMAL ELECT. DIST., PH 1                    | \$1,056 | NRM | ELECTRICAL         |            | NONE                  |
|----------------------------------------------------------|---------|-----|--------------------|------------|-----------------------|
| 98-102 RENOVATE NURSE STATIONS, PH 8 \$                  | 300     | NRM | MINOR IMPROVEMENTS |            | NONE                  |
| TOTAL COST (Excluding Expedited Leases) \$ 2,592         |         |     |                    |            |                       |
| Project Count LEASE (excludes Expedited) = 2 MAJOR = 0   |         |     | MINOR = 2          | MINOR MISC | = 0 NRM = 2           |
| \* C = Construction dollars only D = Design dollars only |         |     |                    |            |                       |
| Page 4                                                   |         |     |                    |            | JUL 20, 1995@11:49:54 |
| Enter RETURN to continue or '^' to exit: \<RET\>     |         |     |                    |            |                       |

DIVISION 399 TEST OF MINOR PROJECT TRANSMIS \$ 700 C MINOR SEISMIC OTHER

BUDGET YEAR PLUS TWO PROJECT LIST (FY 1999)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION PROJ #</th>
<th>TITLE</th>
<th><p>COST</p>
<p>(in $000)</p></th>
<th>*PROGRAM</th>
<th><p>PROJECT</p>
<p>CATEGORY</p></th>
<th><p>MCPS</p>
<p>SCORE</p></th>
<th><p>CITED</p>
<p>DEFICIENCY</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

302 STREETS/PARKING \$ 2,610 C MINOR GENERAL NONE

306 RELOCATE NURSING SUPPT \$ 290 D MINOR GENERAL NONE

---------­

TOTAL COST (Excluding Expedited Leases) \$ 2,900

Project Count LEASE (excludes Expedited) = 0 MAJOR = 0 MINOR = 2 MINOR MISC = 0 NRM = 0

- C = Construction dollars only D = Design dollars only

Page 5 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

FIVE YEAR FACILITY PLAN

VAMC: ANYCITY, DC (999) Region: 1 VISN: 3 Network: TRI-STATE BUDGET YEAR PLUS THREE PROJECT LIST (FY 2000)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 27%" />
<col style="width: 12%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION</th>
<th>PROJ #</th>
<th>TITLE</th>
<th><p>COST</p>
<p>(in $000)</p></th>
<th colspan="2">*PROGRAM</th>
<th><p>PROJECT</p>
<p>CATEGORY</p></th>
<th><p>MCPS</p>
<p>SCORE</p></th>
<th><p>CITED</p>
<p>DEFICIENCY</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>306</p>
<p>00-101</p></td>
<td>RELOCATE NURSING SUPPT SEALCOAT PARKING LOTS PH II</td>
<td colspan="2"><p>$ 2,610 C</p>
<p>$ 250</p></td>
<td>MINOR NRM</td>
<td>GENERAL BOILER</td>
<td></td>
<td>NONE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2">---------­</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

TOTAL COST (Excluding Expedited Leases) \$ 2,860

Project Count LEASE (excludes Expedited) = 0 MAJOR = 0 MINOR = 1 MINOR MISC = 0 NRM = 1

- C = Construction dollars only D = Design dollars only

Page 6 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

BUDGET YEAR PLUS FOUR PROJECT LIST (FY 2001)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>DIVISION</th>
<th>PROJ #</th>
<th>TITLE</th>
<th><p>COST</p>
<p>(in $000)</p></th>
<th>* PROGRAM</th>
<th><p>PROJECT</p>
<p>CATEGORY</p></th>
<th><p>MCPS</p>
<p>SCORE</p></th>
<th><p>CITED</p>
<p>DEFICIENCY</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>01-101</td>
<td>ENERGY AUDIT</td>
<td>$ 50</td>
<td>NRM</td>
<td>CONSULTANT STUDY</td>
<td></td>
<td>NONE</td>
</tr>
<tr class="even">
<td></td>
<td>01-102</td>
<td>REPLACE ROOFS</td>
<td>$ 375</td>
<td>NRM</td>
<td>ROOFS</td>
<td></td>
<td>NONE</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>---------­</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

TOTAL COST (Excluding Expedited Leases) \$ 425

Project Count LEASE (excludes Expedited) = 0 MAJOR = 0 MINOR = 0 MINOR MISC = 0 NRM = 2

- C = Construction dollars only D = Design dollars only

Page 7 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

FIVE YEAR FACILITY PLAN

VAMC: ANYCITY, DC (999) Region: 1 VISN: 3 Network: TRI-STATE FUTURE YEARS PROJECT LIST

| DIVISION PROJ \# | TITLE           | COST (in \$000) | \*PROGRAM | PROJECT CATEGORY |
|------------------|-----------------|-----------------|-----------|------------------|
| 02-901           | LEASE LAB SPACE | \$ 75           | LEASE     | RESEARCH         |

310 RENOVATE WING 3B \$ 1,207 MINOR PATIENT ENVIRONMENT/

245 ENCLOSE NHCU PATIO \$ 368 MI-MISC NHCU

02-101 TUCKPOINT/WATERPROOF EXTERIOR \$ 438 NRM BUILDING SHELLS/INTE

02-118 REPLACE INTERIOR LIGHTING \$ 888 C NRM ELECTRICAL

---------­

TOTAL COST (Excluding Expedited Leases) \$ 2,976

Project Count LEASE (excludes Expedited) = 1 MAJOR = 0 MINOR = 1 MINOR MISC = 1 NRM = 2

- C = Construction dollars only D = Design dollars only

Page 8 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

EQUIPMENT OVER \$250K LIST

PROJ \# TITLE FUNDING YR EQUIPMENT NAME ADD/ QTY TOT COST CONST/RENT REPL (in \$000)

LEASE PROJECTS:

| 97-901          | LEASE PROJECT                  | 1997 | MRI         | A   | 2   | \$ 600                |     |
|-----------------|--------------------------------|------|-------------|-----|-----|-----------------------|-----|
| 98-999          | TEST OF LEASE PROJECT TRANSMIS | 1998 | MRI         | A   | 1   | \$ 276                |     |
| TOTAL           |                                |      |             |     |     | \$ 876                |     |
| MAJOR PROJECTS: |                                |      |             |     |     |                       |     |
| TOTAL           |                                |      |             |     |     | \$                    | 0   |
| MINOR PROJECTS: |                                |      |             |     |     |                       |     |
| 399             | TEST OF MINOR PROJECT TRANSMIS | 1998 | FIRST ITEM  | A   | 2   | \$ 552                |     |
| 399             | TEST OF MINOR PROJECT TRANSMIS | 1998 | SECOND ITEM | R   | 1   | \$ 304                |     |
| TOTAL           |                                |      |             |     |     | \$ 856                |     |
|                 |                                |      | Page 9      |     |     | JUL 20, 1995@11:49:54 |     |

Enter RETURN to continue or '^' to exit: \<RET\>

FIVE YEAR FACILITY PLAN

VAMC: ANYCITY, DC (999) Region: 1 VISN: 3 Network: TRI-STATE EQUIPMENT OVER \$250K LIST

| PROJ \# | TITLE | FUNDING YR | EQUIPMENT | NAME | ADD/ | QTY | TOT | COST   |
|---------|-------|------------|-----------|------|------|-----|-----|--------|
|         |       | CONST/RENT |           |      | REPL |     | (In | \$000) |

MINOR MISC. PROJECTS:

TOTAL \$ 0

NRM PROJECTS:

| 97-101 ASBESTOS PROJECT            | 1997 | BLOWER    | A     |     | 1   | \$250    |
|------------------------------------|------|-----------|-------|-----|-----|----------|
| 97-110 NHCU BED CONVERSION         | 1997 | BLOWER    | A     |     | 1   | \$256    |
| 97-199 TEST OF NRM FIELDS TRANSFER | 1997 | EQUIPMENT | ONE   | A   | 1   | \$250    |
| 97-199 TEST OF NRM FIELDS TRANSFER | 1997 | EQUIPMENT | TWO   | R   | 2   | \$600    |
| 97-199 TEST OF NRM FIELDS TRANSFER | 1997 | EQUIPMENT | THREE | A   | 3   | \$825    |
| TOTAL                              |      |           |       |     |     | \$ 2,181 |

> **NOTE:** Equipment not included for projects in current year (1996) or future years (\>2001).

Page 10 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

PROJECT NUMBER: 999-299 TITLE: RENOV. NUCLEAR MEDICINE FACILITY TYPE: VHA DIVISION:

PROGRAM: MINOR MISC. MCPS SCORE: N/A

PROJECT CATEGORY: GENERAL \# NEW NHCU BEDS: N/A

BONUS CATEGORY: N/A \# NHCU BEDS RENOVATED: N/A

AMBULATORY CARE PERCENTAGE: N/A \# NHCU BEDS CONVERTED: N/A BUDGET CATEGORY: MISCELLANEOUS PROJECTS

FUNDING YEAR ESTIMATED COST (in \$000)

| DESIGN       | 1997 | \$ 65  |
|--------------|------|--------|
| CONSTRUCTION | 1997 | \$ 585 |
| TOTAL        |      | \$ 650 |

Enter RETURN to continue or '^' to exit: \<RET\>

ACTIVATIONS: FISCAL YEAR REQUIRED: 1998 (costs in \$000) ADD'L FTEE REQUIRED: 0.00 EQUIPMENT: \$ 0

| RECURRING PS:            | \$ 0 | RECURRING ALL OTHER: | \$ 0 |
|--------------------------|------|----------------------|------|
| NON-RECURRING ALL OTHER: | \$ 6 | TRAVEL .007:         | \$ 0 |

EQUIPMENT OVER \$250K: NAME ADD/REPL QUANTITY TOTAL COST (in \$000)

none listed.

BUILDINGS: 114

CITED DEFICIENCY: NONE

Enter RETURN to continue or '^' to exit: \<RET\>

SHORT DESCRIPTION: This project will renovate and partially reconfigure Nuclear Medicine service will be upgrading the utilities.

SHORT JUSTIFICATION: The Nuclear Medicine service is functionally, environmentally, and aesthetically deficient.

Enter RETURN to continue or '^' to exit: \<RET\>

Page 11 JUL 20, 1995@11:49:54

PROJECT NUMBER: 999-383 TITLE: RENOVATE MED/CLINICAL FACILITY TYPE: VHA DIVISION:

PROGRAM: MINOR MCPS SCORE: N/A

PROJECT CATEGORY: CLINICAL IMPROVEMENT \# NEW NHCU BEDS: N/A BONUS CATEGORY: N/A \# NHCU BEDS RENOVATED: N/A

AMBULATORY CARE PERCENTAGE: N/A \# NHCU BEDS CONVERTED: N/A BUDGET CATEGORY: CLINICAL IMPROVEMENTS

FUNDING YEAR ESTIMATED COST (in \$000)

DESIGN 1996 \$ 110

CONSTRUCTION 1997 \$ 990

TOTAL \$ 1,100

Enter RETURN to continue or '^' to exit:

ACTIVATIONS: FISCAL YEAR REQUIRED: 1997 (costs in \$000)

ADD'L FTEE REQUIRED: 2.00 EQUIPMENT: \$ 1,826

| RECURRING PS:            | \$ 70  | RECURRING ALL OTHER: | \$ 0 |
|--------------------------|--------|----------------------|------|
| NON-RECURRING ALL OTHER: | \$ 400 | TRAVEL .007:         | \$ 9 |

EQUIPMENT OVER \$250K: NAME ADD/REPL QUANTITY TOTAL COST (in \$000) TOTAL COST \$ 0

BUILDINGS:

CITED DEFICIENCY: JCAHO

Enter RETURN to continue or '^' to exit: \<RET\>

SHORT DESCRIPTION: RENOVATION, EXPANSION, AND UPGRADE OF 10000 S.F. OF SPACE TO CORRECT DEFICIENCIES IN FOUR SECTIONS OF MEDICAL SERVICE INCLUDING PULMONARY, RESPIRATORY, GASTROENTEROLOGY, AND CARDIOLOGY LAB. FDP ACTION \# S18.

SHORT JUSTIFICATION: QUALITY OF SPACE IS POOR. TREATMENT ROOMS OPEN DIRECTLY TP A PUBLIC CORRIDOR AND THERE IS POOR CIRCULATION IN LAB ABD TESTING ROOMS. PROCEDURES OCCUR BEHIND CUBICLE CURTAINS RATHER THAN PRIVATE ROOMS.

Enter RETURN to continue or '^' to exit: \<RET\>

Page 13 JUL 20, 1995@11:49:54

PROJECT NUMBER: 999-97-110 TITLE: NHCU BED CONVERSION FACILITY TYPE: VHA DIVISION:

PROGRAM: NRM MCPS SCORE: N/A

PROJECT CATEGORY: PATIENT ENVIRONMENT/PRIVACY \# NEW NHCU BEDS: 0

BONUS CATEGORY: NHCU \# NHCU BEDS RENOVATED: 0

AMBULATORY CARE PERCENTAGE: 90 \# NHCU BEDS CONVERTED: 30 BUDGET CATEGORY: NHCU BED CONV FUNDING YEAR ESTIMATED COST (in \$000)

| DESIGN       | 1997 | \$ 11  |
|--------------|------|--------|
| CONSTRUCTION | 1997 | \$ 100 |
| TOTAL        |      | \$ 111 |

Enter RETURN to continue or '^' to exit: \<RET\>

ACTIVATIONS: FISCAL YEAR REQUIRED: 1998 (costs in \$000)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>RECURRING PS:</th>
<th>$ 0</th>
<th>RECURRING ALL</th>
<th>OTHER:</th>
<th>$ 0</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NON-RECURRING ALL OTHER:</p>
<p>EQUIPMENT OVER $250K: NAME</p></td>
<td>$ 2</td>
<td><p>TRAVEL .007:</p>
<p>ADD/REPL</p></td>
<td>QUANTITY</td>
<td><p>$ 0</p>
<p>TOTAL</p></td>
<td>COST (in $000)</td>
</tr>
</tbody>
</table>

ADD'L FTEE REQUIRED: 1.00 EQUIPMENT: \$ 14

none listed.

BUILDINGS: 114

CITED DEFICIENCY: JCAHO

Enter RETURN to continue or '^' to exit: \<RET\>

SHORT DESCRIPTION:

SHORT JUSTIFICATION:

Convert building to NHCU beds.

Population in nursing home is projected to increase.

Page 19 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

PROJECT NUMBER: 999-97-199 TITLE: TEST OF NRM FIELDS TRANSFER FACILITY TYPE: VHA DIVISION: DIVISION

PROGRAM: NRM MCPS SCORE: N/A

PROJECT CATEGORY: BUILDING SHELLS/INTERIORS \# NEW NHCU BEDS: 10

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 10%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 14%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><p>AMBULATORY CARE PERCENTAGE: 49</p>
<p>FUNDING YEAR</p></th>
<th>ESTIMATED</th>
<th>COST</th>
<th>(In</th>
<th>$000)</th>
<th>#</th>
<th>NHCU</th>
<th>BEDS</th>
<th><p>CONVERTED: 0</p>
<p>APPROVED</p></th>
<th>COST (in $000)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DESIGN 1997</td>
<td>$</td>
<td>10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$</td>
<td>10</td>
</tr>
<tr class="even">
<td>CONSTRUCTION 1997</td>
<td>$</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$</td>
<td>100</td>
</tr>
<tr class="odd">
<td>TOTAL</td>
<td>$</td>
<td>110</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$</td>
<td>110</td>
</tr>
</tbody>
</table>

BONUS CATEGORY: NHCU \# NHCU BEDS RENOVATED: 11

BUDGET CATEGORY: NHCU BED CONV

Enter RETURN to continue or '^' to exit: \<RET\>

ACTIVATIONS: FISCAL YEAR REQUIRED: 1997 (costs in \$000)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>RECURRING PS:</th>
<th>$ 1</th>
<th>RECURRING ALL</th>
<th>OTHER:</th>
<th>$ 3</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NON-RECURRING ALL OTHER:</p>
<p>EQUIPMENT OVER $250K: NAME</p></td>
<td>$ 4</td>
<td><p>TRAVEL .007:</p>
<p>ADD/REPL</p></td>
<td>QUANTITY</td>
<td><p>$ 5</p>
<p>TOTAL</p></td>
<td>COST (in $000)</td>
</tr>
</tbody>
</table>

ADD'L FTEE REQUIRED: 2.00 EQUIPMENT: \$ 300

none listed.

BUILDINGS: 100-OPC,101-OPC,1,2,5,7,28,85,110,114,135,0001,201-OPC CITED DEFICIENCY: JCAHO

Enter RETURN to continue or '^' to exit: \<RET\>

SHORT DESCRIPTION: Project description of the project entry which is being used to test the transfer of fields contained in an NRM program project.

SHORT JUSTIFICATION:

Short justification of the project with is being used to test the transfer of NRM fields.

Page 21 JUL 20, 1995@11:49:54

Enter RETURN to continue or '^' to exit: \<RET\>

LEASE PROJECT DETAIL

PROJECT NUMBER: 999-98-999 TITLE: TEST OF LEASE PROJECT TRANSMISSION FACILITY TYPE: VHA DIVISION: ALPHA

PROGRAM: LEASE

PROJECT CATEGORY: DIRECT PATIENT CARE BUDGET CATEGORY: VACO

LEASE TYPE: NEW LEASE/EXISTING PRESENCE PROPOSED LEASE TERM: 5 YEARS

RENTABLE SQ FT: 8,200 NET PARKING: 5

|             | FUNDING YEAR | ESTIMATED | COST | (in \$000)    |
|-------------|--------------|-----------|------|---------------|
| AWARD LEASE | 1998         | \$        | 5    | (Lump Sum)    |
| RENT STARTS | 1998         | \$        | 96   | (Annual Rent) |
| TOTAL       |              | \$        | 101  |               |

EXISTING SPACE RENTABLE SQ FT: 1,314 EXISTING SPACE ANNUAL RENT: \$12,345

Enter RETURN to continue or '^' to exit: \<RET\>

ACTIVATIONS: FISCAL YEAR REQUIRED: 1998 (costs in \$000)

ADD'L FTEE REQUIRED: 1.25 EQUIPMENT: \$ 2

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 9%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>RECURRING PS:</th>
<th>$ 1</th>
<th>RECURRING ALL OTHER:</th>
<th>$</th>
<th>3</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NON-RECURRING ALL OTHER:</td>
<td>$ 4</td>
<td>TRAVEL .007:</td>
<td>$</td>
<td>6</td>
</tr>
<tr class="even">
<td><p>EQUIPMENT OVER $250K: NAME</p>
<p>MRI</p></td>
<td></td>
<td>ADD/REPL ADDITIONAL</td>
<td>QUANTITY 1</td>
<td><p>TOTAL COST (in $000)</p>
<p>$ 276</p></td>
</tr>
<tr class="odd">
<td>TOTAL COST</td>
<td></td>
<td></td>
<td></td>
<td>$ 276</td>
</tr>
</tbody>
</table>

CITED DEFICIENCY: JCAHO, RSFPE

Enter RETURN to continue or '^' to exit: \<RET\>

SHORT DESCRIPTION: This is a test of the five-year plan ability to process and transmit lease projects accurately and completely.

SHORT JUSTIFICATION: This long line contains justification for the lease project. If this space is not leased then patient care will be adversely impacted. End of the long justification line which does not contain a carriage return.

Enter RETURN to continue or '^' to exit: \<RET\>Page 27 JUL 20, 1995@11:49:54

PLAN SUMMARY BY PROGRAMS AND FISCAL YEARS (in \$000)

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>CNT</th>
<th><p>MAJOR</p>
<p>COST</p></th>
<th>CNT</th>
<th><p>MINOR</p>
<p>COST</p></th>
<th>CNT</th>
<th><p>MINOR MISC</p>
<p>COST</p></th>
<th>CNT</th>
<th><p>NRM</p>
<p>COST</p></th>
<th><p>CONST</p>
<p>CNT</p></th>
<th><p>TOTAL</p>
<p>COST</p></th>
<th><p>LEASE</p>
<p>CNT</p></th>
<th><p>TOTAL</p>
<p>COST</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FY 1996 0</td>
<td><p>$</p>
<p>0</p></td>
<td>1</td>
<td>$ 110</td>
<td>1</td>
<td>$ 667</td>
<td>2</td>
<td>$ 460</td>
<td>4</td>
<td>$ 1,237</td>
<td>0</td>
<td><p>$</p>
<p>0</p></td>
</tr>
<tr class="odd">
<td>===</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>==</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>=======</td>
</tr>
<tr class="even">
<td>FY 1997 1</td>
<td>$ 20,000</td>
<td>2</td>
<td>$ 1,060</td>
<td>1</td>
<td>$ 650</td>
<td>6</td>
<td>$ 1,156</td>
<td>10</td>
<td>$ 22,866</td>
<td>1</td>
<td>$ 120</td>
</tr>
<tr class="odd">
<td>FY 1998 0</td>
<td>$ 0</td>
<td>2</td>
<td>$ 990</td>
<td>0</td>
<td>$ 0</td>
<td>2</td>
<td>$ 1,356</td>
<td>4</td>
<td>$ 2,346</td>
<td>2</td>
<td>$ 246</td>
</tr>
<tr class="even">
<td>FY 1999 0</td>
<td>$ 0</td>
<td>2</td>
<td>$ 2,900</td>
<td>0</td>
<td>$ 0</td>
<td>0</td>
<td>$ 0</td>
<td>2</td>
<td>$ 2,900</td>
<td>0</td>
<td>$ 0</td>
</tr>
<tr class="odd">
<td>FY 2000 0</td>
<td>$ 0</td>
<td>1</td>
<td>$ 2,610</td>
<td>0</td>
<td>$ 0</td>
<td>1</td>
<td>$ 250</td>
<td>2</td>
<td>$ 2,860</td>
<td>0</td>
<td>$ 0</td>
</tr>
<tr class="even">
<td>FY 2001 0</td>
<td>$ 0</td>
<td>0</td>
<td>$ 0</td>
<td>0</td>
<td>$ 0</td>
<td>2</td>
<td>$ 425</td>
<td>2</td>
<td>$ 425</td>
<td>0</td>
<td>$ 0</td>
</tr>
<tr class="odd">
<td>===</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>==</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>=======</td>
</tr>
<tr class="even">
<td>PLAN TOTAL 1</td>
<td>$ 20,000</td>
<td>4</td>
<td>$ 7,560</td>
<td>1</td>
<td>$ 650</td>
<td>11</td>
<td>$ 3,187</td>
<td>17</td>
<td>$ 31,397</td>
<td>3</td>
<td>$ 366</td>
</tr>
<tr class="odd">
<td>FY FUTURE 0</td>
<td><p>$</p>
<p>0</p></td>
<td>1</td>
<td>$ 1,207</td>
<td>1</td>
<td>$ 368</td>
<td>2</td>
<td>$ 1,326</td>
<td>4</td>
<td>$ 2,901</td>
<td>1</td>
<td>$ 75</td>
</tr>
<tr class="even">
<td>===</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>==</td>
<td>========</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>=======</td>
<td>===</td>
<td>========</td>
</tr>
<tr class="odd">
<td>PLAN+FUTURE1</td>
<td>$ 20,000</td>
<td>5</td>
<td>$ 8,767</td>
<td>2</td>
<td>$ 1,018</td>
<td>13</td>
<td>$ 4,513</td>
<td>21</td>
<td>$ 34,298</td>
<td>4</td>
<td>$ 441</td>
</tr>
</tbody>
</table>

PLAN and PLAN+FUTURE counts only include split year projects once and may not equal the sum of the year counts. Lease column excludes Expedited leases.

Enter RETURN to continue or '^' to exit: \<RET\>

Page 28 JUL 20, 1995@11:49:54

### Validate 5-Yr Plan Projects.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Five Year Facility Plan Project Applications

Projects will no longer be automatically deleted after editing when problems are found with the required fields. Instead, projects will be validated after editing and when selected for transmission. Invalid projects cannot be transmitted to the Regional Construction Database. A detailed report of any validation problems will be available. New options, Validate Five Year Plan Projects \[ENPLFV\] and Validate Project Applications \[ENPLAV\], have been added to allow validation to be performed whenever desired.

Edit 5-Yr Plan Project Activations E/E

Five Year Facility Plan Report (132 columns)

\> Validate 5-Yr Plan Projects Transmit 5-Yr Plan Projects

#### Communication Log Display for a Project

Select Five Year Facility Plan (FYFP) Option: Validate 5-Yr Plan Projects.

Select one of the following:

1.  INDIVIDUAL PROJECTS
2.  FROM LIST OF FYFP PROJECTS RETURNED TO SITE
3.  ALL PROJECTS IN FIVE YEAR FACILITY PLAN

Choose method of project selection: 3 ALL PROJECTS IN FIVE YEAR FACILITY PLAN Budget Year of 5-Yr Plan: (1993-2099): 1997//??

Enter the 4-digit Budget Year of the Plan.

Budget Year of 5-Yr Plan: (1993-2099): 1997// \<RET\>

Select INSTITUTION NAME: 999//??

Choose from:

| VASITE.VA.GOV | ANYSTATE |       | 590   |
|---------------|----------|-------|-------|
| ISCEXAMPLE    | ANYSTATE | ISC   | 12000 |
| VA MED CTR    | ANYSTATE |       | 111   |
| ANYCITY       | ANYPLACE | MC(M) | 999   |

Select INSTITUTION NAME: 999// ANYCITY ANYPLACE MC(M) 999

Validating Projects.............................

1 out of 29 selected projects failed the validation checks.

1 out of 29 selected projects passed the validation checks with warnings. Do you want a detailed report? YES//??

Enter either 'Y' or 'N'.

Do you want a detailed report? YES// \<RET\>

DEVICE: HOME// \<RET\> LAN

Five Year Facility Plan Validation Results JUL 20, 1995 page 1

Project: 999-271 (passed with warnings)

W\) ESTIMATED A/E COST (67000) does not match APPROVED A/E FUNDING (60000)

Project: 999-97-111 (failed)

E\) PROJECT DESCRIPTION (SHORT) is required.

E\) JUSTIFICATION (SHORT) is required.

E\) ACTIVATION YEAR (1996) is before FUNDING YEAR - CONST (1997).

5)  ESTIMATED CONST COST (FYFP) required for FUNDING YEAR - CONST (1997).

> **NOTE:** E) = Error which prevents transmission W) = Warning Enter RETURN to continue or '^' to exit: \<RET\>

#### Validate 5-Yr Plan Projects.

Projects will no longer be automatically deleted after editing when problems are found with the required fields. Instead, projects will be validated after editing and when selected for transmission. Invalid projects cannot be transmitted to the Regional Construction Database. A detailed report of any validation problems will be available. New options, Validate Five Year Plan Projects \[ENPLFV\] and Validate Project Applications \[ENPLAV\], have been added to allow validation to be performed whenever desired.

Edit 5-Yr Plan Project Activations E/E

Five Year Facility Plan Report (132 columns)

\> Validate 5-Yr Plan Projects Transmit 5-Yr Plan Projects

Communication Log Display for a Project

Select Five Year Facility Plan (FYFP) Option: Validate 5-Yr Plan Projects.

Select one of the following:

1.  INDIVIDUAL PROJECTS
2.  FROM LIST OF FYFP PROJECTS RETURNED TO SITE
3.  ALL PROJECTS IN FIVE YEAR FACILITY PLAN

Choose method of project selection: 3 ALL PROJECTS IN FIVE YEAR FACILITY PLAN Budget Year of 5-Yr Plan: (1993-2099): 1997//??

Enter the 4-digit Budget Year of the Plan.

Budget Year of 5-Yr Plan: (1993-2099): 1997// \<RET\>

Select INSTITUTION NAME: 999//??

Choose from:

| VASITE.VA.GOV | ANYSTATE |     |     | 590   |
|---------------|----------|-----|-----|-------|
| ISCEXAMPLE    | ANYSTATE |     | ISC | 12000 |
| VA MED CTR    | ANYSTATE |     |     | 111   |
| ANYCITY       | ANYPLACE |     |     | 999   |

Select INSTITUTION NAME: 999// ANYCITY ANYPLACE MC(M) 999

Validating Projects.............................

1 out of 29 selected projects failed the validation checks.

1 out of 29 selected projects passed the validation checks with warnings. Do you want a detailed report? YES//??

Enter either 'Y' or 'N'.

Do you want a detailed report? YES// \<RET\>

DEVICE: HOME// \<RET\> LAN

The following example uses Option 3.

Select one of the following:

1.  INDIVIDUAL PROJECTS
2.  FROM LIST OF FYFP PROJECTS RETURNED TO SITE
3.  ALL PROJECTS IN FIVE YEAR FACILITY PLAN

Choose method of project selection: 3 ALL PROJECTS IN FIVE YEAR FACILITY PLAN Budget Year of 5-Yr Plan: (1993-2099): 1997//??

Enter the 4-digit Budget Year of the Plan.

Budget Year of 5-Yr Plan: (1993-2099): 1997// \<RET\>

Select INSTITUTION NAME: 999//??

Choose from:

| VASITE.VA.GOV | ANYSTATE |     |     | 590   |
|---------------|----------|-----|-----|-------|
| ISCEXAMPLE    | ANYSTATE |     | ISC | 12000 |
| VA MED CTR    | ANYSTATE |     |     | 111   |
| ANYCITY       | ANYPLACE |     |     | 999   |

Select INSTITUTION NAME: 999// ANYCITY ANYPLACE MC(M) 999

Validating Projects............................

No validation problems found.

Do you want to Queue Transmission? Y// \<RET\>

28 Five Year Plan projects were queued for transmission.

### Communication Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Communication Log for a selected project. It contains information on network messages exchanged between the site and the regional construction database.

Transmit 5-Yr Plan Projects Edit 5-Yr Plan Project Activations E/E

Five Year Facility Plan Report (132 columns) Validate 5-Yr Plan Projects.

### Transmit 5-Yr Plan Projects.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\> Communication Log Display for a Project

Select Five Year Facility Plan (FYFP) Option: communication Log Display for a

| Project                        | CONSTRUCTION PROJECT LIST | JUL 20,1995        | 12:03 PAGE 1 |     |
|--------------------------------|---------------------------|--------------------|--------------|-----|
| Select PROJECT NUMBER: 999-383 | RENOVATE MED/CLINIC       | AL                 |              |     |
| DEVICE:                        | LAN                       | RIGHT MARGIN: 80// | \<RET\>      |     |

COMMUNICATION LOG PROJECT \# :999-383

07/12/95 08:44 5-Yr Site transmitted project to region

07/12/95 09:46 5-Yr Region ADDED proj. transmitted at 07/12/95 08:44 07/13/95 10:19 5-Yr Region (SCOTT A BAUMANN) Returned Project to Site:

Select PROJECT NUMBER:

### Project Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AUTOMATED ENGINEERING MANAGEMENT SYSTEM VERSION 7

WASH.ENC

Jul 20, 1995 10:52:54 am

WO Work Order & MERS ...

FYFP Five Year Facility Plan (FYFP) ...

APPL Project Applications ...

TRK Project Tracking ...

EQ Equipment Management ... ENM Program Management ...

SP Space/Facility Management ... FSA 2162 Report of Accident ...

XFER Assign (Transfer) Electronic Work Orders

Edit Project Application Option name: ENXFM05.

This option enables entering all information required for forms VAF 10-1193, VAF 10-1193a and prioritization methodology scoring sheets.

Activations E/E Option name: ENXFM18

This option enables enter/edit of project activations information.

Environmental Analysis E/E (VAF 10-1193a) Option name: ENXFM09 This option enables entry of information which appears on VAF 10-1193a.

Approval of Project Application Option name: ENXFM16

This option controls the Chief Engineer's and VAMC Director's sign off on the project application. The Security Key ENPLK001 controls the Chief Engineer's approval. The Security Key ENPLK002 controls the VAMC Director's approval. The Chief Engineer must sign off before the VAMC Director. Both must approve before the project application can be transmitted electronically to higher approval authorities.

Reports Option name: ENXFMAR Report menu for project applications.

Validate Project Applications Option name: ENXFMAV.

This option validates selected construction and lease projects. Only data which pertains to a project application is checked. Any validation errors or warnings are listed on a detailed report.

Transmit Project Applications Option name: ENXFMAX.

This option transmits construction and lease project data to the Regional Construction Database for selected projects. All data pertinent to a project application is sent. Selected projects are automatically validated prior to the actual transmission. The transmitter is a recipient of any created mail messages that are sent to the Regional Construction Database.

Communication Log Display for a Project Option name: ENXFM20 This option displays the communication log for a selected project. The

communication log contains information on network messages exchanged between the site and the regional construction database. "5-Yr" indicates Five Year Plan related messages and "Appl" indicates project application related messages.

Edit Project Application

\> Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports...

Validate Project Applications Transmit Project Applications

Communication Log Display for a Project

The following table shows those fields which either control or are controlled by other fields. The right-hand column shows the controlling conditions. The controlling condition must be true for the field to be asked.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Project Application E/E (VAF 10­1193</strong></th>
<th><strong>Controlling Conditions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SEISMIC AREA</td>
<td><p>PROJECT CATEGORY contains.</p>
<p>SEISMIC</p></td>
</tr>
<tr class="even">
<td>PROJECT CATEGORY &gt;75% SCOPE</td>
<td>PROGRAM is MINOR or MINOR MISC</td>
</tr>
<tr class="odd">
<td>BONUS CATEGORY</td>
<td>Program is NRM</td>
</tr>
<tr class="even">
<td>AMBULATORY CARE PERCENTAGE</td>
<td>Program is NRM</td>
</tr>
<tr class="odd">
<td>SIR RATING</td>
<td><p>PROGRAM not NRM or BONUS</p>
<p>CATEGORY is Energy</p></td>
</tr>
<tr class="even">
<td>APPROVED IN 5 YR ENERGY PLAN</td>
<td><p>PROGRAM not NRM or BONUS</p>
<p>CATEGORY is Energy</p></td>
</tr>
<tr class="odd">
<td>NHCU BEDS (NEW)</td>
<td><p>PROJECT CATEGORY or BONUS</p>
<p>CATEGORY contains NHCU and</p>
<p>FACILITY TYPE is VHA</p></td>
</tr>
<tr class="even">
<td>NHCU BEDS (RENOVATED)</td>
<td><p>PROJECT CATEGORY or BONUS</p>
<p>CATEGORY contains NHCU and</p>
<p>FACILITY TYPE is VHA</p></td>
</tr>
<tr class="odd">
<td>NHCU BEDS (CONVERTED)</td>
<td><p>PROJECT CATEGORY or BONUS</p>
<p>CATEGORY contains NHCU and</p>
<p>FACILITY TYPE is VHA</p></td>
</tr>
<tr class="even">
<td>FUNDING YEAR - A/E</td>
<td><p>PROGRAM is Major, Minor, Minor-</p>
<p>Misc. or NRM</p></td>
</tr>
<tr class="odd">
<td>FUNDING YEAR - CONST</td>
<td><p>PROGRAM is Major, Minor, Minor-</p>
<p>Misc. or NRM</p></td>
</tr>
<tr class="even">
<td>VAMC PRIORITY</td>
<td>PROGRAM not Major</td>
</tr>
<tr class="odd">
<td><p>EMERGENCY/INTERIM</p>
<p>APPLICATION</p></td>
<td>PROGRAM is not MAJOR</td>
</tr>
<tr class="even">
<td>EQUIPMENT OVER $250K</td>
<td><p>EQUIPMENT OVER $250K</p>
<p>APPLICATION is Yes</p></td>
</tr>
<tr class="odd">
<td>BUILDING NUMBER</td>
<td><p>Program is Major, Minor, Minor- Misc,</p>
<p>or NRM</p></td>
</tr>
<tr class="even">
<td>NET BED CHANGE</td>
<td>FACILITY TYPE equals VHA</td>
</tr>
<tr class="odd">
<td>MCPS SCORE</td>
<td>PROGRAM equals MAJOR</td>
</tr>
<tr class="even">
<td>EPA REPORTABLE</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="odd">
<td>EPA REPORTING CATEGORY</td>
<td>EPA REPORTABLE is Yes</td>
</tr>
<tr class="even">
<td><p>TOTAL FACTORED SQUARE</p>
<p>FOOTAGE</p></td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="odd">
<td>TOTAL M AND R COSTS</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="even">
<td>TOTAL BSEA COSTS</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="odd">
<td>TOTAL BSER COSTS</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="even">
<td>TOTAL MI COSTS</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="odd">
<td>NRM CONTINGENCY PCT</td>
<td>PROGRAM equals NRM</td>
</tr>
<tr class="even">
<td>TOTAL MAJOR/MINOR/MINOR MISC. CONSTRUCTION COST LOW BID</td>
<td>PROGRAM does not equal NRM</td>
</tr>
<tr class="odd">
<td>IMPACT JUSTIFICATION</td>
<td>IMPACT COST is greater than 0</td>
</tr>
<tr class="even">
<td>Edit Activations?</td>
<td><p>Only asked if a funding year is the</p>
<p>budget year or budget year +1</p></td>
</tr>
<tr class="odd">
<td>ACTIVATION RESOURCES REQ IN FY</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="even">
<td>ADDITIONAL FTEE</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="odd">
<td>RECURRING PS</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="even">
<td>EQUIPMENT $</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="odd">
<td>RECURRING ALL OTHER $</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="even">
<td>NONRECURRING ALL OTHER</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="odd">
<td>TRAVEL .007</td>
<td>Edit Activations is YES</td>
</tr>
<tr class="even">
<td>SPACE USE FOR PRIORITIZATION</td>
<td>PROGRAM is MINOR or MINOR MISC</td>
</tr>
<tr class="odd">
<td><p>ENVIRONMENTAL ASSESSMENT</p>
<p>REQD</p></td>
<td><p>Remaining fields for Environmental Analysis will only be asked if this field.</p>
<p>was answered YES</p></td>
</tr>
</tbody>
</table>

Select Project Applications Option: Edit Project Application Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT, PROJECT NUMBER: 999-97-101//

MEDICAL CENTER: ANYCITY//??

Facility where the work is being performed. May indicate.

a division or other functional element (National Cemetery, Regional Office, satellite clinic, etc.) if appropriate.

Choose from:

| VASITE.VA.GOV | ANYSTATE |       | 590   |
|---------------|----------|-------|-------|
| ISCEXAMPLE    | ANYSTATE | ISC   | 12000 |
| VA MED CTR    | ANYSTATE |       | 111   |
| ANYCITY       | ANYPLACE | MC(M) | 999   |

MEDICAL CENTER: ANYCITY// DIVISION:??

This field is used to identify the division of a multi-divisional facility. It can be used to generate a division specific report when printing the Five-Year Facility Plan.

A new DIVISION (#6910.3) file has been added. It contains a list of valid divisions for a multi-divisional facility. It can be edited using the DIVISION \[ENDIV\] option on the Program Management menu. There is no need to enter any divisions if it is not applicable for your site. The DIVISION (#176) field in the CONSTRUCTION PROJECT (#6925) file has been changed to point to the new Division file.

Choose from: ALPHA BETA DIVISION

DIVISION:

PROJECT TITLE: ASBESTOS PROJECT//??

Official title of project.

Project titles entered with lowercase letters will automatically be converted to all uppercase letters. This change has been made to promote consistency in national databases and reports.

PROJECT TITLE: ASBESTOS PROJECT// FACILITY TYPE: VETERANS HEALTH ADMIN//??

This field is important to enable restriction of Project Functional and Budget Categories and to enable reporting by Facility Type. Note: The cross reference was added to 2 reasons: a) Facilitate reporting by facility type. b) Force the filing by DIE so that the selection screens

/Filters work properly for Functional and Budget Categories. Choose from:

| VHA | VETERANS HEALTH ADMIN     |
|-----|---------------------------|
| VBA | VETERANS BENEFITS ADMIN   |
| NCS | NATIONAL CEMETERY SERVICE |

FACILITY TYPE: VETERANS HEALTH ADMIN// PROGRAM: NRM//??

This field is a set of codes used to classify program type. Choose from:

MA MAJOR

MI MINOR

MM MINOR MISC.

NR NRM

OT OTHER

LE LEASE

SL STATION LEVEL PROGRAM: NRM//

The default STATUS is "DRAFT PROJECT" for a new entry, or the status as shown in the last Five-Year Plan. The status must be changed to "NEW PROJECT APPLICATION", "DESIGN PROGRAM", "A/E", "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", "AUTHORIZED", "INVITATION FOR BID", "BID OPEN", or "CONSTRUCTION" before the project will be eligible for approval by the Chief Engineer and Facility Director/Designee.

STATUS: NEW PROJECT APPLICATION//??

DRAFT PROJECT PLAN

NEW PROJECT APPLICATION AUTHORIZED

A/E

INVITATION FOR BID, BID OPEN, CONSTRUCTION COMPLETED, PROJECT CANCELED, UNAPPROVED/VIABLE, NON-VIABLE

Present status of the project.

Choose from: A/E AUTHORIZED BID OPEN CANCELED

COMPLETED PROJECT CONSTRUCTION DRAFT PROJECT

INVITATION FOR BID

NEW PROJECT APPLICATION NON-VIABLE

PLAN UNAPPROVED/VIABLE

STATUS: NEW PROJECT APPLICATION// PROJECT CATEGORY: ASBESTOS//??

This field is a pointer to the OFM Project Category File (#7336.8). The field designates the project functional category, and determines prioritization points for NRM, Minor, and Minor Misc. programs.

Choose from: ARCHITECTURAL BARRIERS ASBESTOS

...

...

WASTE MANAGEMENT WINDOWS

PROJECT CATEGORY: ASBESTOS//

here is a new required field for NRM projects called BONUS CATEGORY (#158.8). This field is scope dependent and 'Not Applicable' should be entered as the Bonus Category if none of the other choices involve 50% or more of the project scope.

BONUS CATEGORY: NOT APPLICABLE//??

This field designates the bonus category which involves 50% or more of the project scope and determines prioritization points for NRM projects. 'Not Applicable' should be selected if none of the other choices meet the 50% scope requirement.

Choose from: AMBULATORY CARE EDUCATION ENERGY

NHCU

NOT APPLICABLE RESEARCH

BONUS CATEGORY: NOT APPLICABLE//

This new field for NRM projects called AMBULATORY CARE PERCENTAGE (#158.9) should be entered for all NRM projects.

AMBULATORY CARE PERCENTAGE: 0//??

This field contains the project scope percentage for ambulatory care.

AMBULATORY CARE PERCENTAGE: 0//

The BUDGET CATEGORY defaults are provided based on the PROJECT CATEGORY entered for Major, Minor, and Minor Misc projects, and should be accepted unless otherwise approved by the Regional Office. NRM budget categories should be selected based on guidance in the call letter for the NRM program.

BUDGET CATEGORY: ASBESTOS/IH//??

This field is a pointer to the OFM Budget Category File (#7336.9). The field designates the project budget category. Choices are screened based on program type.

Choose from: ASBESTOS/IH BIOMEDICAL BOILERS/INCINERATORS ENERGY

FIRE AND SAFETY HVAC

NHCU

NHCU BED CONV OTHER

STRUCTURAL IMPROVEMENTS UTILITY SYSTEMS

BUDGET CATEGORY: ASBESTOS/IH// FUNDING YEAR - A/E: 1997//??

This field contains the fiscal year for which A/E is funded or proposed.

FUNDING YEAR - A/E: 1997// FUNDING YEAR - CONST: 1997//??

Fiscal year for which construction is funded or proposed.

FUNDING YEAR - CONST: 1997//

CITATIONS is a multiple field for entering citations issued to the site.

CITATIONS

Select CITATION NAME: EPA CITED ASBESTOS//??

EPA CITED ASBESTOS

This field contains the name of any citations associated with a project. (e.g. JCAHO citations)

Select CITATION NAME: EPA CITED ASBESTOS// CITATION NAME: EPA CITED ASBESTOS// DATE: MAR 9,1993//??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T -1(for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. This field contains the date the citation was issued.

DATE: MAR 9,1993//

CITING AUTHORITY: ENVIRONMENTAL PROTECTION AGENCY

// ??

This field contains a pointer to the Regulatory Agency File (#7335.7).

CHOOSE FROM:

ASSOC FOR ACCREDITATION OF LAB CITY

COLLEGE OF AMERICAN PATHOLOGIS COUNTY

ENVIRONMENTAL PROTECTION AGENC FOOD AND DRUG ADMINISTRATION GENERAL ACCOUNTING OFFICE INSPECTOR GENERAL DVA

JOINT COMM ON ACCREDITATION HE NATIONAL FIRE PROTECTION ASSOC NUCLEAR REGULATORY COMMISSION OCCUPATIONAL SAFETY AND HEALTH OTHER

REGIONAL SAFETY & FIRE PROTECT STATE

UNIFORM FEDERAL ACCESSIBILITY

CITING AUTHORITY: ENVIRONMENTAL PROTECTION AGENCY

// PAGE: 1//??

This field contains the page number in the citing agency's report that contains the citation.

PAGE: 1//

OFFICIALS NAME: ENTECH1, F IVE//??

This field contains the name of the official issuing the citation.

CITATIONS

Select CITATION NAME: EPA CITED ASBESTOS// CITATION NAME: EPA CITED ASBESTOS//??

This field contains the name of any citations associated with a project. (e.g. JCAHO citations)

CITATION NAME: EPA CITED ASBESTOS// DATE: MAR 9,1993//??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. This field contains the date the citation was issued.

DATE: MAR 9,1993//

CITING AUTHORITY: ENVIRONMENTAL PROTECTION AGENCY

// ??

This field contains a pointer to the Regulatory Agency File (#7335.7).

Choose from:

ASSOC FOR ACCREDITATION OF LAB

CITY

COLLEGE OF AMERICAN PATHOLOGIS COUNTY

ENVIRONMENTAL PROTECTION AGENC FOOD AND DRUG ADMINISTRATION GENERAL ACCOUNTING OFFICE INSPECTOR GENERAL DVA

JOINT COMM ON ACCREDITATION HE NATIONAL FIRE PROTECTION ASSOC NUCLEAR REGULATORY COMMISSION OCCUPATIONAL SAFETY AND HEALTH OTHER

REGIONAL SAFETY & FIRE PROTECT STATE

UNIFORM FEDERAL ACCESSIBILITY

CITING AUTHORITY: ENVIRONMENTAL PROTECTION AGENCY

// PAGE: 1//??

This field contains the page number in the citing agency's report that contains the citation.

PAGE: 1//

OFFICIALS NAME: ENTECH1, F IVE// ??

This field contains the name of the official issuing the citation.

OFFICIALS NAME: ENTECH1, F IVE// OFFICIALS TITLE: INSPECTOR// ??

This field contains the title of the official issuing the citation.

OFFICIALS TITLE: INSPECTOR//

CORRECTION \>50% PROJECT SCOPE: YES//??

This field is a set of codes (Yes or No) used to determine if correction of the citation is greater than 50% of the project scope. The field is used to determine if prioritization points will be awarded for NRM and Minor/Minor Misc. programs.

Choose from:

1 YES

0 NO

CORRECTION \>50% PROJECT SCOPE: YES// Select CITATION NAME:

VAMC PRIORITY: 1//??

This field contains the priority \# assigned to the project by the facility.

VAMC PRIORITY: 1// EMERGENCY/INTERIM APPLICATION:??

This field is used to identify project applications that are emergency or interim. Minor Appeals are considered Interim.

Choose from:

E EMERGENCY

I INTERIM

EMERGENCY/INTERIM APPLICATION:

EQPMT OVER \$250K APPLICATION: YES//??

This field is used to identify projects that have equipment costing more than \$250K.

Choose from:

Y YES

N NO

This is a multiple entry field for equipment over \$250K.

EQPMT OVER \$250K APPLICATION: YES// EQUIPMENT OVER \$250K

Select EQUIPMENT OVER \$250K NAME: BLOWER//??

BLOWER

This field contains a 3–30-character name for an equipment item over.

\$250,000.

Select EQUIPMENT OVER \$250K NAME: BLOWER// QUANTITY: 1//??

This field contains the quantity of the equipment item.

QUANTITY: 1//

UNIT COST: 250000//??

This field contains the unit cost of the equipment item.

UNIT COST: 250000// ADDITIONAL/REPLACEMENT: ADDITIONAL//??

This field identifies equipment over \$250K as additional or replacement equipment.

Choose from:

ADDITIONAL

R REPLACEMENT ADDITIONAL/REPLACEMENT: ADDITIONAL//

Select EQUIPMENT OVER \$250K NAME:

Select BUILDING NUMBER: 114//??

114

This field contains a building number associated with the project.

Choose from:

1

2

5

7

28

85

110

114

135

0001

100-OPC

101-OPC

201-OPC

Select BUILDING NUMBER: 114// BLDG OCCUPANCY: OTHER//??

This field is used to identify occupancy of buildings affected. (VAF 10­ 1193, Block 10)

Choose from:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th>PATIENT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>ADMINISTRATIVE</td>
</tr>
<tr class="even">
<td>3</td>
<td>QUARTERS</td>
</tr>
<tr class="odd">
<td>4</td>
<td><ol start="4" type="1">
<li><p>AMBULATORY CARE</p></li>
</ol></td>
</tr>
<tr class="even">
<td>5</td>
<td><ol start="5" type="1">
<li><p>OTHER</p></li>
</ol></td>
</tr>
</tbody>
</table>

BLDG OCCUPANCY: OTHER// NET BED CHANGE: 0//??

This field contains the net change in authorized beds.

NET BED CHANGE: 0//

5 YR FACILITY PLAN FY: 1996//??

This field contains the fiscal year the project is planned for on the approved 5-Year facility plan.

5 YR FACILITY PLAN FY: 1996// NET PARKING CHANGE: 0//??

This field contains the change (if any) in the number of parking stalls available.

NET PARKING CHANGE: 0//

PROJECT DESCRIPTION (SHORT) is for a short (approx. 3 lines). project description.

PROJECT DESCRIPTION (SHORT):

1\>Remove asbestos materials from piping and walls.

EDIT Option:

The LONG DESCRIPTION field may be used for a description of more than 3 lines.

LONG DESCRIPTION:

1\>?

PROJECT JUSTIFICATION (SHORT):

1\>This project is required because of the possibility of asbestos exposure 2\>during maintenance in affected areas.

EDIT Option:

The LONG JUSTIFICATION field may be used for a justification of more than 3 lines.

LONG JUSTIFICATION:

1\>

The WORKLOAD JUSTIFICATION field is for a brief declaration of workload data that justifies the project (i.e., Is the Workload approved? What is the approval date? What workload model version was used?).

WORKLOAD JUSTIFICATION:

1\>

PROJECT SCOPE

The next field is a multiple entry pointer to the OFM H089 Chapters file (7336.6) for entry of H089 chapter codes.

Select H089 CHAPTER NAME: CLINICAL SERVICES ADMINISTRATION

//

H089 CHAPTER NAME: CLINICAL SERVICES ADMINISTRATION

// ??

This field contains the name of an H08-9 chapter associated with project.

NOT APPLICABLE (999) has been added as a H089 Chapter.

Choose from:

A & MM ADMINISTRATION 284

A & MM SUPPLY, PROCESSING AND 285

...

...

VETERANS OUTREACH PROGRAM 306

VOLUNTARY SERVICE 290

H089 CHAPTER NAME: CLINICAL SERVICES ADMINISTRATION // NEW NET SQ FT: 2873//??

This field contains the new net square footage for the associated H08-9 chapter.

NEW NET SQ FT: 2873//

NEW GROSS SQ FT: 2890//??

This field contains the new gross square footage for the associated H08-9 chapter.

NEW GROSS SQ FT: 2890// RENOVATED NET SQ FT: 3783//??

This field contains the renovated net square footage for the associated H08-9 chapter.

RENOVATED NET SQ FT: 3783// RENOVATED GROSS SQ FT: 8387//??

This field contains the renovated gross square footage for the associated H08-9 chapter.

RENOVATED GROSS SQ FT: 8387// Select H089 CHAPTER NAME:

SITE ISSUES:??

This field contains a short (1-90 character) statement on the status of the site and any effect on the project.

SITE ISSUES:

HISTORICAL ISSUES:??

This field contains a short (1-90 character) statement on the status of "Historical" issues in and around the project and any resulting effect on the project.

HISTORICAL ISSUES:

ENVIRONMENTAL ISSUES:??

This field contains a short (1-90 character) statement on the status of "Environmental" issues in and around the project and any resulting effect on the project. Reference form VAF 10-1193a "EMIS Construction Program Environmental Analysis".

ENVIRONMENTAL ISSUES:

SEISMIC ISSUES:,// ??

This field contains a short (1-90 character) statement on the status of "Seismic" issues in and around the project and any resulting effect on the project.

SEISMIC ISSUES:,//

HAZARDOUS MATERIALS ISSUES:??

This field contains a short (1-90 character) statement on the status of

"Asbestos or other hazardous materials" issues in and around the project and any resulting effect on the project.

HAZARDOUS MATERIALS ISSUES:

TRANSPORT ISSUES:??

This field contains a short (1-90 character) statement on the status of "vertical or horizontal transportation systems" issues in and around the project and any resulting effect on the project.

TRANSPORT ISSUES:

PARKING ISSUES:??

This field contains a short (1-90 character) statement on the status of "Parking and/or Roads" issues in and around the project and any resulting effect on the project.

PARKING ISSUES:

PLANNED CONSTRUCTION METHOD: CONTRACT//??

Set of codes for the planned construction method of the project. Choose from:

| 1   | CONTRACT      |
|-----|---------------|
| 2   | P&H           |
| 3   | STATION LABOR |
| 4   | SBA 8(a)      |
| 5   | DESIGN/BUILD  |
| 6   | LEASE         |

PLANNED CONSTRUCTION METHOD: CONTRACT//

Is this project reportable to the EPA per the NRM Call Letter criteria?

EPA REPORTABLE: YES//??

Indicates if a NRM project meets the criteria of an environmental project which should be reported to the Environmental Protection Agency on the

A-106 report. The criteria can be found in the NRM Call Letter for project applications. If this field is YES, an EPA Reporting Category must also be specified.

Choose from:

Y YES

N NO

EPA REPORTABLE: YES//

The VA is required to generate the A-106 report for the Environmental Protection Agency. To support the A-106 report, the new EPA REPORTING CATEGORY (#158.7) field will need to be specified on project applications for NRM projects which meet the criteria of an EPA reportable project per the NRM Project Application Call Letter.

EPA REPORTING CATEGORY: ASBESTOS//??

This field is required for environmental NRM projects. It is used to generate the A-106 report required by the Environmental Protection Agency.

Choose from:

ASBESTOS

EPA REPORTING CATEGORY: ASBESTOS//

TOTAL FACTORED SQUARE FOOTAGE may be obtained from the approved Region \#4 database. TOTAL FACTORED SQUARE FOOTAGE, TOTAL M&R COSTS, TOTAL BSEA, TOTAL BSER, TOTAL MI COSTS, and NRM

CONTINGENCY PCT are only asked for NRM programs.

TOTAL FACTORED SQUARE FOOTAGE: 22876//??

This field contains the Total Factored Square Footage as derived from the National Survey of Building Square Footage for NRM Funding Distribution. The field is used to determine the factored square footage prioritization points for NRM project applications.

TOTAL FACTORED SQUARE FOOTAGE: 22876// TOTAL M AND R COSTS:??

This field contains the total Maintenance & Repair costs as listed on VAF 10-6238.

TOTAL M AND R COSTS:

TOTAL BSEA COSTS:??

This field contains the total Building Service Equipment Additional (BSEA) costs as listed on VAF 10-6238. BSEA labor costs should be included in MI.

TOTAL BSEA COSTS:

TOTAL BSER COSTS:??

This field contains the total Building Service Equipment Replacement (BSER) costs as listed on VAF 10-6238.

TOTAL BSER COSTS:

TOTAL MI COSTS:??

This field contains the total Minor Improvement (MI) costs as listed on VAF 10-6238.

TOTAL MI COSTS:

NRM CONTINGENCY PCT:??

This field contains the NRM program Construction Contingency's Percentage.

NRM CONTINGENCY PCT:

IMPACT COST:??

This field contains the Total Impact costs as listed on the VAF 10-6238.

IMPACT COST:

If an IMPACT COST greater than 0 has been entered, a required word processing field called IMPACT JUSTIFICATION will follow. It is printed on the last page of the 1193 and replaces the IMPACT ISSUES field.

TECHNICAL SERVICES \$:??

This field contains the total Technical Services dollars as listed on VAF 10-6238.

TECHNICAL SERVICES \$:

Edit Activations? Y//?? Enter 'Y' or 'N'.

Activations are funding and FTEE resources required to bring the subject area of the construction or maintenance project up to full operational capacity.

Edit Activations? Y//

ACTIVATION RESOURCES REQ IN FY: 1997//??

This field contains the fiscal year activation resources are required.

ACTIVATION RESOURCES REQ IN FY: 1997//

ADDITIONAL FTEE: 1//??

This field contains the total Additional FTEE number as documented in the detailed activation documentation.

ADDITIONAL FTEE: 1// RECURRING PS: 49000//??

This field contains the total Recurring Personnel Service (PS) funds in accordance with the Additional FTEE.

RECURRING PS: 49000//

RECURRING ALL OTHER \$: 2874//??

This field contains the total Recurring All Other Funds required to support the project.

RECURRING ALL OTHER \$: 2874// EQUIPMENT \$: 28767//??

This field contains the total activation equipment funds required to support the project with the following exception. For NRM projects, any equipment items (or systems) that cost over \$250,000 should NOT be included in this figure since such high-cost equipment must be applied for separately under the High-Cost Equipment Program. For Leases and Minor, Minor Misc and Major projects, any equipment items (or systems) that cost

\$250,000 should be included in this figure since such high-cost equipment cannot be applied for under the High-Cost Equipment Program.

EQUIPMENT \$: 28767// NONRECURRING ALL OTHER: 296//??

This field contains the total Non-Recurring All Other funds required to support the project.

NONRECURRING ALL OTHER: 296// TRAVEL .007: 260//??

This field contains the total Travel .007 funds required to support the project.

TRAVEL .007: 260//

Select DOMINO PROJECT: 999-95-101//??

999-95-101

This multiple field points to projects, in the Construction Project File (#6925), that must be started prior to the current project, due to a domino relationship.

Choose from:

| 999-00-101 | SEALCOAT PARKING LOTS PH II        |
|------------|------------------------------------|
| 999-01-101 | ENERGY AUDIT                       |
| ...        |                                    |
| ...        |                                    |
| 999-98-901 | PARKING GARAGE LEASE               |
| 999-98-999 | TEST OF LEASE PROJECT TRANSMISSION |

Select DOMINO PROJECT: 999-95-101// DOMINO PROJECT: 999-95-101//

### Activations E/E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit Project Application

\> Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports...

Validate Project Applications Transmit Project Applications

Communication Log Display for a Project Select Project Applications Option: activations E/E

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT ACTIVATION RESOURCES REQ IN FY: 1997//??

This field contains the fiscal year activation resources are required.

ACTIVATION RESOURCES REQ IN FY: 1997// ADDITIONAL FTEE: 1//??

This field contains the total Additional FTEE number as documented in the detailed activation documentation.

ADDITIONAL FTEE: 1// RECURRING PS: 49000//??

This field contains the total Recurring Personnel Service (PS) funds in accordance with the Additional FTEE.

RECURRING PS: 49000//

RECURRING ALL OTHER \$: 2874//??

This field contains the total Recurring All Other Funds required to support the project.

RECURRING ALL OTHER \$: 2874// EQUIPMENT \$: 28767//??

This field contains the total activation equipment funds required to support the project with the following exception. For NRM projects, any equipment items (or systems) that cost over \$250,000 should NOT be included in this figure since such high-cost equipment must be applied for separately under the High-Cost Equipment Program. For Leases and Minor, Minor Misc and Major projects, any equipment items (or systems) that cost

\$250,000 should be included in this figure since such high-cost equipment cannot be applied for under the High-Cost Equipment Program.

EQUIPMENT \$: 28767// NONRECURRING ALL OTHER: 296//??

This field contains the total Non-Recurring All Other funds required to support the project.

NONRECURRING ALL OTHER: 296// TRAVEL .007: 260//??

This field contains the total Travel .007 funds required to support the project.

TRAVEL .007: 260// Select PROJECT NUMBER:

### Environmental Analysis E/E (VAF 10-1193a)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit Project Application Activations E/E

\> Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports ...

Validate Project Applications Transmit Project Applications

Communication Log Display for a Project

Select Project Applications Option: environmental Analysis E/E (VAF 10-1193a)

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT ENVIRONMENTAL ASSESSMENT REQD: YES//??

This field is a set of codes used to identify projects requiring an environmental assessment. (VAF 10-1193a, Block 4)

Choose from:

Y YES

N NO

ENVIRONMENTAL ASSESSMENT REQD: YES// ENVIRONMENT IMPACT STMT REQD: YES//??

This field is a set of codes (Yes or No) indicating the need for an environmental impact statement by the facility. (VAF 10-1193a, Block 5) Choose from:

Y YES

N NO

ENVIRONMENT IMPACT STMT REQD: YES// ADDITIONAL DOCUMENTATION REQD: YES//??

This field is a set of codes (Yes or No) indicating the need for additional documentation by the facility. (VAF 10-1193a, Block 6)

Choose from:

Y YES

N NO

ADDITIONAL DOCUMENTATION REQD: YES// FURTHER REQD ACTION: Y//??

This field contains specification of further action required by the facility. (VAF 10-1193a, Block 7)

FURTHER REQD ACTION: Y// EVALUATOR:??

This field contains the name of the evaluator. (VAF 10-1193a, Block 8) EVALUATOR:

DATE OF EVALUATION:??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

This field contains the date of environmental evaluation. (VAF 10-1193a, Block 8)

DATE OF EVALUATION:

ACQUIRES OR DISPOSES LAND: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project acquires or disposes of land. (VAF 10-1193a, Block A1) Choose from:

Y YES

N NO

ACQUIRES OR DISPOSES LAND: YES// A1 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for ACQUIRES OR DISPOSES LAND. (VAF 10-1193a, Block A1)

A1 LAND USE TEXT:

AFFECTS WETLANDS/FLOOD PLAINS: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project involves land located in a wetland or floodplain. (VAF 10­ 1193a, Block A2)

Choose from:

Y YES

N NO

AFFECTS WETLANDS/FLOOD PLAINS: YES// A2 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for AFFECTS WETLANDS/FLOOD PLAINS. (VAF 10-1193a, Block A2)

A2 LAND USE TEXT:

INVOLVES STORM WATER RUNOFF: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project involves storm water run-off and retainage. (VAF 10-1193a, Block A3)

Choose from:

Y YES

N NO

INVOLVES STORM WATER RUNOFF: YES// A3 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for INVOLVES STORM WATER RUNOFF. (VAF 10-1193a, Block A3)

A3 LAND USE TEXT:

CONFLICTS W LOCAL ZONING: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project conflicts with local zoning and planning regulations. (VAF 10-1193a, Block A4)

Choose from:

Y YES

N NO

CONFLICTS W LOCAL ZONING: YES// A4 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for CONFLICTS W LOCAL ZONING. (VAF 10-1193a, Block A4)

A4 LAND USE TEXT:

DISLOCATES PEOPLE/RESIDENCES: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project dislocates persons, residences, or causes a major population shift. (VAF 10-1193a, Block A5)

Choose from:

Y YES

N NO

DISLOCATES PEOPLE/RESIDENCES: YES//

A5 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for DISLOCATES PEOPLE/RESIDENCES.

A5 LAND USE TEXT:

AFFECTS PROTECTED FAUNA/FLORA: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project affects protected wildlife or vegetation. (VAF 10-1193a, Block A6)

Choose from:

Y YES

N NO

AFFECTS PROTECTED FAUNA/FLORA: YES// A6 LAND USE TEXT:??

Specification of standards used, and project elements analyzed for AFFECTS PROTECTED FAUNA/FLORA. (VAF 10-1193a, Block A6)

A6 LAND USE TEXT:

OUTSIDE CONST GT 10000 SQ FT: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project involves 'outside' construction of more than 10,000 sq. ft. (VAF 10-1193a, Block B1)

Choose from:

Y YES

N NO

OUTSIDE CONST GT 10000 SQ FT: YES// B1 CONSTRUCTION TEXT:??

Specification of standards used, and project elements analyzed for OUTSIDE CONST GT 10000 SQ FT. (VAF 10-1193a, Block B1)

B1 CONSTRUCTION TEXT:

INCREASE OFF SITE TRAFFIC \>10%: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project increases off-site traffic flow by more than 10%. (VAF 10­ 1193a, Block B2)

Choose from:

Y YES

N NO

INCREASE OFF SITE TRAFFIC \>10%: YES// B2 CONSTRUCTION TEXT:??

Specification of standards used, and project elements analyzed for INCREASE OFF SITE TRAFFIC \>10%. (VAF 10-1193a, Block B2)

B2 CONSTRUCTION TEXT:

SIGNIF ALTER OFF SITE TRAFFIC: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project significantly alters off-site traffic flow. (VAF 10-1193a, Block B3)

Choose from:

Y YES

N NO

SIGNIF ALTER OFF SITE TRAFFIC: YES// B3 CONSTRUCTION TEXT:??

Specification of standards used, and project elements analyzed for SIGNIF ALTER OFF SITE TRAFFIC. (VAF 10-1193a, Block B3)

B3 CONSTRUCTION TEXT:

INVOLVE HISTORIC AREA/BLDGS: YES//??

This field is a set of codes (Yes or No) indicating whether or not the

proposed project involves a historically designated building or area. (VAF 1193a, Block B4)

Choose from:

Y YES

N NO

INVOLVE HISTORIC AREA/BLDGS: YES// B4 CONSTRUCTION TEXT:??

Specification of standards used, and project elements analyzed for INVOLVE HISTORIC AREA/BLDGS. (VAF 10-1193a, Block B4)

B4 CONSTRUCTION TEXT:

EMISSION/WATER QUALITY PROBLEM: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project conflicts with local, state, or federal standards regarding emissions, water quality, or toxic substances. (VAF 10-1193a, Block C1)

Choose from:

Y YES

N NO

EMISSION/WATER QUALITY PROBLEM: YES// C1 EMISSION/TOXINS TEXT:??

Specification of standards used, and project elements analyzed for EMISSION/WATER QUALITY PROBLEM. (VAF 10-1193a, Block C1)

C1 EMISSION/TOXINS TEXT:

PUBLIC CONTROVERSY: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project has a known potential for public controversy. (VAF 10­ 1193a, Block D1)

Choose from:

Y YES

N NO

PUBLIC CONTROVERSY: YES//

D1 PUBLIC CONTROVERSY TEXT:??

Specification of standards used, and project elements analyzed for PUBLIC CONTROVERSY. (VAF 10-1193a, Block D1)

D1 PUBLIC CONTROVERSY TEXT:

CONFLICT LOCAL/STATE REGS: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project conflict with local or state regulations. (VAF 10-1193a, Block D2)

Choose from:

Y YES

N NO

CONFLICT LOCAL/STATE REGS: YES// D2 PUBLIC CONTROVERSY TEXT:??

Specification of standards used, and project elements analyzed for CONFLICT LOCAL/STATE REGS. (VAF 10-1193a, Block D2)

D2 PUBLIC CONTROVERSY TEXT:

OVERLOAD UTILITY SYS CAPACITY: YES//??

This field is a set of codes (Yes or No) indicating whether or not the proposed project overloads the available utility system capacity. (VAF 10­ 1193a, Block D3)

Choose from:

Y YES

N NO

OVERLOAD UTILITY SYS CAPACITY: YES// D3 UTILITY OVERLOAD TEXT:??

Specification of standards used, and project elements analyzed for OVERLOAD UTILITY SYS CAPACITY.

D3 UTILITY OVERLOAD TEXT: Select PROJECT NUMBER:

### Approval of Project Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Approval of Project Application option controls the Chief Engineer's and VAMC Director's sign off on the project application. Project Status must be set to "NEW PROJECT APPLICATION", "DESIGN PROGRAM", "A/E", "SCHEMATICS", "DESIGN DEVELOPMENT", "CONSTRUCTION DOCUMENTS", "AUTHORIZED", "INVITATION FOR BID", "BID OPEN", or "CONSTRUCTION."

before the project can be approved. The security key ENPLK001 controls the Chief Engineer's approval. The security key ENPLK002 controls the VAMC Director's approval. The Chief Engineer must sign off before the VAMC Director. Both must approve before the project application can be transmitted electronically to higher approval authorities.

Chief Engineer and VAMC Director approvals of a project application will be considered current for six months. Any approvals performed over six months ago will need to be redone prior to transmission of the project application. The Approval of Project Application \[ENPLM16\] option has been modified to update the signed name and date whenever an application is re-approved. Previously, just pressing return at the approval prompt did not update the approval name or date of re­ approved applications.

Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a)

\> Approval of Project Application Reports...

Validate Project Applications Transmit Project Applications

Communication Log Display for a Project

Select Project Applications Option: approval of Project Application

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT

Project Number: 999-97-101 Title: ASBESTOS PROJECT Program: NRM Category: ASBESTOS

Do you wish to view a project summary:? NO// y YES

VHA PROJECT APPLICATION - SIGN OFF SUMMARY PROJECT NUMBER 999-97-101

PROJECT PROGRAM: NRM FACILITY PRIORITY: 1

FACILITY: ANYCITY TOTAL PROJECT SCORE: 51 PROJECT TITLE: ASBESTOS PROJECT

EMERGENCY APPLICATION: NO EQUIPMENT OVER \$250K APPLICATION: YES

| Five Year Facility Plan               |                                      |
|---------------------------------------|--------------------------------------|
| Project Applications                  |                                      |
| BUILDING NUMBER(S): 114               |                                      |
| BUILDING OCCUPANCY: OTHER             |                                      |
| PROJECT CATEGORY: ASBESTOS            |                                      |
| BUDGET CATEGORY: ASBESTOS/IH          |                                      |
| NET BED CHANGE: 0                     | NET PARKING CHANGE: 0                |
| LISTED ON 5 YR FACILITY PLAN: YES     | 5-YR FACILITY PLAN FY: 1996          |
| NEW NET SQ. FT.: 2873                 | NEW GROSS SQ. FT.: 2890              |
| RENOVATED NET SQ. FT.: 3783           | RENOVATED GROSS SQ. FT.: 8387        |
| AE \$ REQUIRED IN FY: 1997            | CONSTRUCTION \$ REQUIRED IN FY: 1997 |
| PLANNED CONSTRUCTION METHOD: CONTRACT | TOTAL PROJECT COSTS: \$ 0            |
| PROJECT DESCRIPTION:                  |                                      |

Remove asbestos materials from piping and walls. PROJECT JUSTIFICATION:

This project is required because of the possibility of asbestos exposure during maintenance in affected areas.

WORKLOAD:

Project was previously approved by ENDI R, ONE on AUG 18, 1995@11:18:20 Do you want to change the approval status? NO// y YES

VAMC DIRECTOR APPROVED: YES//??

This field contains a set of codes (Yes or No) indicating that the proposal has been prepared and submitted in accordance with instructions, all supporting data that is required is forwarded, and is practical from a facility viewpoint. The field triggers fields 248, VAMC DIRECTOR/

DESIGNEE NAME, and 249, VAMC DIRECTOR SIGN DATE.

Choose from:

Y YES

N NO

VAMC DIRECTOR APPROVED: YES// YES

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

\> Reports...

Validate Project Applications Transmit Project Applications

Communication Log Display for a Project Select Project Applications Option: reports.

Project Application VAF 10-1193 (132 columns) Environmental Analysis VAF 10-1193a (132 columns) Minor/Minor Misc Prioritization

NRM Prioritization Scoring Sheet

> **NOTE:** Because many of the reports have footers, it is advisable not to use a number higher than 60 to designate page length (i.e., DEVICE: HOME// ;132;60 LAN)

Five Year Facility Plan Project Applications

Project Application VAF 10-1193 (132 columns)

Some of the information printed on the 1193 is computed based on other data.

TOTAL CONST. COST (LOW BID)

= TOTAL M AND R COSTS + TOTAL BSEA COSTS + TOTAL BSER COSTS + TOTAL MI COSTS.

CONTINGENCY \$

= TOTAL CONST. COST (LOW BID) \* NSM CONTINGENCY PCT rounded

up to the next thousand.

TECHNICAL SERVICES %

= TECHNICAL SERVICES \$ / TOTAL CONST. COST (LOW BID) \* 100

TOTAL PROJECT COSTS

= TOTAL CONST. COST (LOW BID) + CONTINGENCY \$ + IMPACT COST + TECHNICAL SERVICES \$.

TOTAL CONST. COST (LOW BID)

= MINOR/MAJOR CONST COSTS.

CONST. CONTINGENCY

Computed based on H089 new and renovated gross sq ft.

= 7.5% if there is any renovated gross sq ft.

= 5 % if there is only new gross sq ft.

= 7.5% if there is not any new or renovated gross sq ft.

TECHNICAL SERVICES %

= TECHNICAL SERVICES \$ / MINOR/MAJOR CONST. COSTS \* 100

TOTAL PROJECT COSTS

= MINOR/MAJOR CONST. COSTS + CONTINGENCY \$ + IMPACT COST + TECHNICAL SERVICES \$

66\. EQUIP OVER \$250K

= Sum of costs (UNIT COST \* QUANTITY) for any EQUIPMENT OVER

\$250K

69\. TOTAL PROJECT SCORE

NRM: see NRM PRIORITIZATION SCORING SHEET for details. MINOR or MINOR MISC: see MINOR/MINOR MISC PRIORITIZATION

SCORING SHEET for details. MAJOR: = MCPS SCORE.

> **NOTE:** Because this report has footers, it is advisable not to use a number higher than 60 to designate page length (i.e., DEVICE: HOME// ;132;60 LAN)

Select Reports Option: project Application VAF 10-1193 (132 columns )

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT DEVICE: HOME// \<RET\> LAN

Must Support 132 Character Display DEVICE: HOME// ;132;60 LAN

VHA PROJECT APPLICATION

EXECUTIVE SUMMARY

\*\*\*\*\*\*\*\*\*\*\* GENERAL DATA \*\*\*\*\*\*\*\*\*\*\*

1\. PROJECT PROGRAM: NRM 2. REGION: 1 3. FACILITY PRIORITY: 1

FACILITY: ANYCITY DIVISION:

PROJECT TITLE: ASBESTOS PROJECT 6. PROJECT NUMBER: 999-97-101

| 7\. | EMERGENCY : NO | 8\. | EQUIPMENT OVER : YES | 9\. BUILDING | : 114 |
|-----|----------------|-----|----------------------|--------------|-------|
|     | APPLICATION    |     | \$250K APPLICATION   | NUMBER(S)    |       |

10\. BUILDING OCCUPANCY: OTHER 11a. PROJECT CATEGORY: ASBESTOS

11b. BONUS CATEGORY: NOT APPLICABLE 11c. SIR RATING: 2.00 11d. % ENERGY TARGET ACHIEVED: (Region enters)

12a. BUDGET CATEGORY: ASBESTOS/IH 12b. EPA CATEGORY: ASBESTOS

13\. NET BED CHANGE: 0 14. LISTED ON 5 YR FACILITY PLAN: YES 15. 5-YR FACILITY PLAN FY: 1996

NET PARKING CHANGE: 0

PROJECT DESCRIPTION: Remove asbestos materials from piping and walls.

PROJECT JUSTIFICATION: This project is required because of the possibility of asbestos exposure during maintenance in affected areas.

WORKLOAD:

FDP UPDATE COMPLETED: \* Reserved for Future Use \*

DEPARTMENT/SERVICE OR TECHNICAL 22. FDP CRITICAL 23. FDP CORRECTIVE DEFICIENCIES TO BE ADDRESSED RATING ACTION \#

\* Reserved for Future Use \*

PROJECT SCOPE:

CODE 26. DEPARTMENT/SERVICE 27. NEW 28. RENOVATED

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 35%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>214</th>
<th>CLINICAL SERVICES ADMINISTRATION</th>
<th>NSF 2873</th>
<th>GSF 2890</th>
<th>NSF 3783</th>
<th>GSF 8387</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>31.-39. (ISSUES)</td>
<td><p>29.-30. NSF &amp; GSF TOTALS:</p>
<p>SITE:</p></td>
<td>2873</td>
<td>2890</td>
<td>3783</td>
<td>8387</td>
</tr>
</tbody>
</table>

HISTORICAL:

ENVIRONMENTAL:

SEISMIC:, HAZARDOUS MAT'LS:

TRANSPORT:

PARKING:

IMPACT: Information (if any) moved to Impact Justification on page 3.

VAF 10-1193 REVISED 5/95 p.1

Hit \<RETURN\> to Continue; '^' to Quit \<RET\>

| VHA | PROJECT APPLICATION | PROJECT NUMBER | COST DATA              |
|-----|---------------------|----------------|------------------------|
|     | EXECUTIVE SUMMARY   | 999-97-101     | \*\*\*\*\*\*\*\*\*\*\* |

40\. CONSTRUCTION METHOD PLANNED: CONTRACT 41. AE \$ REQUIRED IN FY: 1997 42. CONST \$ REQUIRED IN FY: 1997

| 43\. NRM COSTS: YES               |     |     | 44\. MAJOR/MINOR/MINOR MISC. COSTS: NO |     |
|-----------------------------------|-----|-----|----------------------------------------|-----|
| 45\. TOTAL M&R COSTS:             |     |     |                                        |     |
| 46\. TOTAL BSEA COSTS:            |     |     |                                        |     |
| 47\. TOTAL BSER COSTS:            |     |     |                                        |     |
| 48\. TOTAL MI COSTS:              |     |     |                                        |     |
| 49\. TOTAL CONST. COST (LOW BID): |     | 0   | 54\. TOTAL CONST. COST (LOW BID):      |     |
| 50\. CONST CONTCY % AND \$:       |     | 0   | 55\. CONST CONTCY % AND \$:            | %   |
| 51\. IMPACT COSTS:                |     |     | 56\. IMPACT COSTS:                     |     |
| 52\. TECHNICAL SERVICES % AND \$  |     |     | 57\. TECHNICAL SERVICES % AND \$       | %   |

53\. TOTAL PROJECT COSTS: 0 58. TOTAL PROJECT COSTS:

\*\*\*\*\*\*\*\*\*\*\* ACTIVATION DATA \*\*\*\*\*\*\*\*\*\*\*

250000

\*\*\*\*\*\*\*\*\*\*\* SIGNATURES \*\*\*\*\*\*\*\*\*\*\*

70\. CHIEF ENGINEERING SVC/DESIGNEE: ENCHIEF, ONE 71. DATE: 07/17/95

72\. DIRECTOR FACILITY/DESIGNEE: ENDIR, ONE 73. DATE: 09/27/94

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

74\. REGION PROJECT VALIDATION: 75. DATE:

VAF 10-1193 REVISED 5/95 p.2

VHA PROJECT APPLICATION PROJECT NUMBER

EXECUTIVE SUMMARY 999-97-101

DETAILED PROJECT DESCRIPTION: DETAILED PROJECT JUSTIFICATION: IMPACT JUSTIFICATION:

VAF 10-1193 REVISED 5/95 p.3

Hit \<RETURN\> to Continue.

Select PROJECT NUMBER:

Environmental Analysis VAF 10-1193a (132 columns)

> **NOTE:** Because this report has footers, it is advisable not to use a number higher than 60 to designate page length (i.e., DEVICE: HOME// ;132;60 LAN)

Select Reports Option: environmental Analysis VAF 10-1193a (132 columns)

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT DEVICE: ;132;60 LAN

EMIS CONSTRUCTION PROGRAM ENVIRONMENTAL ANALYSIS RCS 13-37

DATE PRINTED: AUG 10,1995 14:32 1. CONSTRUCTION PROJECT NO.: 999-97-101 TO: ADCMD For Operations (138) 2. FACILITY LOCATION DIVISION

Veterans Administration Central Office ANYCITY, D.C. 20420 ANYCITY, DC

SECTION I - GENERAL DATA

3\. PROJECT TITLE: ASBESTOS PROJECT

SECTION II - ENVIRONMENTAL DATA

|                                    |     | A. FACILITY REVIEW | B. VACO/REGION REVIEW |      |
|------------------------------------|-----|--------------------|-----------------------|------|
| 4\. ENVIRONMENTAL ASSESSMENT       |     | REQUIRED           |                       |      |
| 5\. ENVIRONMENTAL IMPACT STATEMENT |     | REQUIRED           |                       |      |
| 6\. ADDITIONAL DOCUMENTATION       |     | REQUIRED           |                       |      |
| 7\. FURTHER ACTION REQUIRED        |     | Y                  |                       |      |
| 8\. EVALUATED                      | BY  | DATE               | BY                    | DATE |

SECTION III - ENVIRONMENTAL ANALYSIS

Environmental Elements: A 'Yes' will require an Assessment.

Specify standards used and project elements analyzed, of the Specific Element or provide additional documentation.

9\. LAND USE

DOES PROPOSED PROJECT:

A1. Acquire or dispose of land? YES A2. Involve land located in a wetland or flood plain? YES

A3. Involve storm-water run-off and retainage? YES

A4. Conflict with local zoning and planning regulations? YES

A5. Dislocate persons, residences, or cause major population shift? YES

A6. Affect protected wildlife or vegetation? YES

CONSTRUCTION/BUILDINGS DOES PROPOSED PROJECT:

B1. Involve 'outside construction of more than 10,000 sq. ft.? YES

B2. Increase off-site traffic flow by more than 10%? YES

B3. Significantly alter off-site traffic flow. YES

B4. Involve a historically designated building or area? YES

EMISSION, WATER, AND TOXIC SUBSTANCES DOES PROPOSED PROJECT:

C1. Conflict with local, state, or federal YES standards?

CULTURAL, COMMUNITY, LEGISLATIVE DOES PROPOSED PROJECT:

D1. Have known potential for public controversy? YES

D2. Conflict with local or state regulations? YES

D3. Overload available utility system capacity? YES

VA FORM 10-1193a FEB 1979

Select PROJECT NUMBER:

#### Minor/Minor Misc Prioritization

Scores are computed as follows:

1.  Cited JCAHO/AALAC/CAP Accreditation Deficiency Based on CITING AUTHORITY, DATE, CORRECTION \>50% PROJECT SCOPE

Citation must have been issued within the last 6 years and more than 50% of the project scope must be for correction of the deficiency.

10 Pts-Repeat Citation, 5 Pts-list Citation, 0 Pts-No Citation

2.  Safety: Handicapped (UFAS), EPA/NRC, Fire/Safety (RSFPE}, OSHA Based on CITING AUTHORITY, DATE, CORRECTION \>50% PROJECT SCOPE

Citation must have been issued within the last 6 years and more than 50% of the project scope must be for correction of the deficiency.

10 Pts-Repeat Citation, 5 Pts-list Citation, 0 Pts-No Citation

> 3\. Space Based on SPACE USE FOR PRIORITIZATION

14 AMBULATORY CARE

14 DIRECT PATIENT CARE (WARDS)

14 DOMICILLIARY

14 FEMALE PRIVACY

14 NHCU

10 24 HR DIRECT PATIENT C ER/OR

8 24 HR ANCILLARY PATIENT CARE

6 12 HR DIRECT PATIENT CARE RMS/MHC

4 12 HR INDIRECT CARE

2 ADMINISTRATIVE AREAS

0 NOT APPLICABLE

> 4\. Energy Conservation Based on SIR RATING 5.01+ 5 Pts

4.01-\>5 4 Pts

3.01-\>4 3 Pts

2.01-\>3 2 Pts

1.01-\>2 1 Pts

0-\>1 0 Pts

5.  Category Bonus Based on PROJECT CATEGO RY. No points are given if Space Points were taken.

5 Pts - Research, and Education

10 Pts - Preservation of Structure (Seismic Only) Area Cat I. 5 Pts - Preservation of Structure (Seismic Only) Area Cat II. O Pts - Preservation of Structure (Seismic Only) Area Cat III.

10 Pts - Critical Building Systems: Electric, HVAC, Boiler, Computer, Telephone, Utility Systems, and Elevator.

10 Pts - Fire and Safety

6.  VAMC Priority

Based on VAMC PRIORITY

MINOR MISC: 1st = 12 Pts, 2nd = 9 Pts., MINOR: Priority points not calculated.

Select Reports Option: minor/Minor Misc Prioritization

Select PROJECT NUMBER: 999-383 RENOVATE MED/CLINICAL DEVICE: HOME// ;80 LAN

FY 1996 MINOR DESIGN PRIORITIZATION SCORING SHEET

Medical Center: ANYCITY

Project Title: Project \#

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><p>RENOVATE MED/CLINICAL</p>
<p>Category: CLINICAL IMPROVEMENT</p></th>
<th></th>
<th></th>
<th></th>
<th>999-383</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TOTAL ESTIMATED: Construction</td>
<td>Cost: 0</td>
<td></td>
<td></td>
<td>Design Cost:</td>
<td>0</td>
</tr>
<tr class="even">
<td>Activations FY: 1997 Additional FTEE Required:</td>
<td></td>
<td>2.00</td>
<td>Recurring</td>
<td>PS $:</td>
<td>70,000</td>
</tr>
</tbody>
</table>

Non-Recurring All Other \$: Travel .007 \$:

400,000 Equipment \$: 1,826,000

9,132 Recurring all other \$: 1

Major/Minor Funded Projects to which Domino

\# Title Type

Equipment Over \$250K:

Name: A/R: Qty: \$

Brief Project Description:

RENOVATION, EXPANSION, AND UPGRADE OF 10000 S.F. OF SPACE TO CORRECT DEFICIENCIES IN FOUR SECTIONS OF MEDICAL SERVICE INCLUDING PULMONARY, RESPIRATORY, GASTROENTEROLOGY, AND

CARDIOLOGY LAB. FDP ACTION \# S18.

1.  Cited JCAHO/AALAC/CAP Accreditation Deficiency.

Date Page Name/Title

1.  3 MAY 1995 3 ENUSER1, E IGHT/INSPECTOR

POINTS

5

2.  Safety: Handicapped (UFAS), EPA/NRC, Fire/Safety (RSFPE), OSHA. Date Page Name/Title

0

3.  Space:

Not Applicable 0

4.  Energy Conservation:

Not Applicable 0

5.  Category Bonus (Scope Dependent):

Not Applicable 0

FACTOR SUBTOTAL 5

Project \#: 999-383

6.  VAMC Priority: \[Rank and Submit 2 Minor Design projects\]

PRIORITY 2 UNK

Select PROJECT NUMBER: \<RET\>

#### NRM Prioritization Scoring Sheet

Energy points have been replaced by Bonus Category points. Activation data, equipment list, and short description are no longer printed on the score sheet.

Scores are computed as follows:

1.  FACILITY PRIORITY SCORE based on VAMC PRIORITY 1st = 30 Pts, 2nd = 28 Pts, etc.
2.  TOTAL FACTORED SQUARE FOOTAGE SCORE based on TOTAL FACTORED SQUARE FOOTAGE

2,000,001+ 8 Pts

1,000,000-\>2,000,000 6 Pts

500,000-\>999,999 4 Pts

1-\>499,999 2 Pts

3.  PROJECT CATEGORY SCORE based on PROJECT CATEGORY

15 Pts - Special Initiatives: Female Patient Privacy, Architectural barriers, TB Infectious Control, Fire Sprinklers 2000, and Patient/Environment Privacy

12 Pts - Utility systems: Electrical, HVAC, Boilers, Incinerator, Utility Systems, Bldg. Service Equipment, Underground Storage Tanks, Laundry, Elevators, and Nurse Call.

10 Pts - Environmental, and Waste Management.

4 Pts - Communications: Telephones, Master TVs and Computer. 2 Pts - System Retrofit: Signage/Graphics, and Security Items.

0 Pts - Other Improvements: Biomedical, Minor Improvements, and Consultant Study.

4.  BONUS CATEGORY based on BONUS CATEGORY 8 Pts - Ambulatory Care.

0 Pts - Education, Research, NHCU, and Not Applicable.

0-10 Pts - Energy

based on SIR RATING and % ENERGY TARGET ACHIEVED

0-5 Pts from SIR RATING: 4+ 5 Pts

2-\>3.99 4 Pts

1-\>1.99 3 Pts

0-\>.99 0 Pts

0-5 Pts from % ENERGY TARGET ACHIEVED:

0-\>49.99 5 Pts

50-\>59.99 4 Pts

60-\>69.99 3 Pts

70-\>79.99 2 Pts

8O-\>89.99 1 Pts

90+ 0 Pts

> **NOTE:** % ENERGY TARGET ACHIEVED is not entered by the facility and therefore points cannot be calculated. This data will be maintained and used in prioritization scoring by higher approval authorities.

5.  CITATIONS based on CITATIONS.

12 are points given if there are any citations within last 6 years for which the CORRECTION \>50% PROJECT SCOPE is YES.

Select Reports Option: norm Prioritization Scoring Sheet

START WITH PROJECT NUMBER: FIRST// 999-97 GO TO PROJECT NUMBER: LAST// 999-97-900 DEVICE: ;80 LAN

FY 1997

NRM PRIORITIZATION METHODOLOGY PROJECT SCORING SHEET

VAMC: ANYCITY

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 31%" />
<col style="width: 5%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 15%" />
<col style="width: 6%" />
<col style="width: 18%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6">Proj Title: ASBESTOS PROJECT</th>
<th colspan="2"></th>
<th colspan="5">Proj #: 999-97-101</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="13">Total Est: Construction Cost: 0 Design Cost:</td>
</tr>
<tr class="even">
<td colspan="2">1</td>
<td colspan="4">FACILITY PRIORITY:</td>
<td colspan="2"></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="4">Facility priority for Project:</td>
<td colspan="2">1</td>
<td>POINTS:</td>
<td colspan="4">30</td>
</tr>
<tr class="even">
<td colspan="2">2</td>
<td colspan="4">TOTAL FACTORED SQUARE FOOTAGE:</td>
<td colspan="2"></td>
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="4">Total Factored Square Footage:</td>
<td colspan="2">22876</td>
<td>POINTS:</td>
<td colspan="4">2</td>
</tr>
<tr class="even">
<td colspan="3">3 PROJECT CATEGORY: Category: ASBESTOS</td>
<td colspan="3"></td>
<td colspan="3">POINTS:</td>
<td>7</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">4 BONUS CATEGORY: Category: NOT APPLICABLE</td>
<td colspan="3"></td>
<td colspan="3">POINTS:</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><p>Ambulatory Care Percentage: SIR Rating: N/A</p>
<p>% of Energy Target Achieved:</p></td>
<td colspan="3"><p>0</p>
<p>N/A</p></td>
<td colspan="3"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">5</td>
<td>CITATIONS:</td>
<td colspan="2"></td>
<td colspan="4">POINTS:</td>
<td colspan="3">12</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td>Date of citation:</td>
<td colspan="2">MAR</td>
<td colspan="4">9,1993</td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td>Citing authority:</td>
<td colspan="6">ENVIRONMENTAL PROTECTION AGENCY</td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td>Survey official's name:</td>
<td colspan="6">ENUSER1, F IVE</td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td colspan="4">TOTAL POINTS:</td>
<td colspan="3">51</td>
<td></td>
</tr>
</tbody>
</table>

FY 1997

NRM PRIORITIZATION METHODOLOGY PROJECT SCORING SHEET

VAMC: ANYCITY

Proj Title: NHCU BED CONVERSION Proj \#: 999-97-110

Total Est: Construction Cost: 0 Design Cost:

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 24%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1 FACILITY PRIORITY:</p>
<p>Facility priority for Project:</p></th>
<th>POINTS:</th>
<th>0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2 TOTAL FACTORED SQUARE FOOTAGE: Total Factored Square Footage:</td>
<td>POINTS:</td>
<td>0</td>
</tr>
<tr class="even">
<td><p>3 PROJECT CATEGORY:</p>
<p>Category: PATIENT ENVIRONMENT/PRIVACY</p></td>
<td>POINTS:</td>
<td>15</td>
</tr>
<tr class="odd">
<td>4 BONUS CATEGORY: Category: NHCU</td>
<td>POINTS:</td>
<td>0</td>
</tr>
<tr class="even">
<td>Ambulatory Care Percentage: 90</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

SIR Rating: N/A

% of Energy Target Achieved: N/A

5 CITATIONS:

Date of citation:

DEC 25,1994

POINTS: 12

Citing authority: Survey official's name:

JOINT COMM ON ACCREDITATION HEALTH CARE ORG

ENUSER1, FOUR

TOTAL POINTS: 27

### Validate Project Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Projects are longer be automatically deleted after editing when problems are found with the required fields. Instead, projects are validated after editing and when selected for transmission. Invalid projects cannot be transmitted to the Regional Construction Database. A detailed report of any validation problems is available.

New options, Validate Five Year Plan Projects \[ENPLFV\] and Validate Project Applications \[ENPLAV\], have been added to allow validation to be performed whenever desired.

Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports...

\> Validate Project Applications Transmit Project Applications

Communication Log Display for a Project

Select Project Applications Option: validate Project Applications

Select one of the following:

1.  INDIVIDUAL PROJECTS
2.  FROM LIST OF PROJECT APPLICATIONS RETURNED TO SITE

| Choose method of project selection: 1 |         | INDIVIDUAL PROJECTS |
|---------------------------------------|---------|---------------------|
| Select PROJECT NUMBER: 999-97-101     |         | ASBESTOS PROJECT    |
| Select PROJECT NUMBER:                | \<RET\> |                     |
| Validating Projects.                  |         |                     |

This project failed the validation checks.

Do you want a detailed report? YES// \<RET\>

DEVICE: HOME// \<RET\> LAN

Project Application Validation Results JUL 20, 1995 page 1

Project: 999-97-101 (failed)

5)  VAMC Director approval date (Sep 27, 1994) is over 6 months old.

> **NOTE:** E) = Error which prevents transmission W) = Warning Enter RETURN to continue or '^' to exit: \<RET\>

### Transmit Project Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Send Project Application \[ENPLM17\] option has been replaced by the Transmit Project Application \[ENPLAX\] option found on the Project Application \[ENPLA\] menu. Projects can be individually selected or chosen from a list of project applications which have been returned to the site for editing.

Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports...

Validate Project Applications

\> Transmit Project Applications Communication Log Display for a Project

Select Project Applications Option: transmit Project Applications

Select one of the following:

1.  INDIVIDUAL PROJECTS
2.  FROM LIST OF PROJECT APPLICATIONS RETURNED TO SITE
3.  SELECTED PROJECTS FROM PROGRAM-YEAR LIST

| Choose method of project selection: |            | 1   | INDIVIDUAL PROJECTS |
|-------------------------------------|------------|-----|---------------------|
| Select PROJECT NUMBER:              | 999-97-101 |     | ASBESTOS PROJECT    |
| Select PROJECT NUMBER:              | \<RET\>    |     |                     |
| Validating Projects.                |            |     |                     |

No validation problems found.

Do you want to Queue Transmission? Y// \<RET\>

1 Project Application was queued for transmission.

### Communication Log Display for a Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Communication Log for a selected project. It contains information on network messages exchanged between the site and the regional construction database.

Edit Project Application Activations E/E

Environmental Analysis E/E (VAF 10-1193a) Approval of Project Application

Reports...

Validate Project Applications Transmit Project Applications

\> Communication Log Display for a Project

Select Project Applications Option: communication Log Display for a Project

Select PROJECT NUMBER: 999-97-101 ASBESTOS PROJECT DEVICE: \<RET\> LAN RIGHT MARGIN: 80//

CONSTRUCTION PROJECT LIST JUL 20,1995 13:54 PAGE 1 COMMUNICATION LOG

PROJECT \# :999-97-101

07/12/95 08:44 5-Yr Site transmitted project to region

07/12/95 09:46 5-Yr Region ADDED proj. transmitted at 07/12/95 08:44

Select PROJECT NUMBER: \<RET\>

CARDIOLOGY LAB. FDP ACTION \# S18.

Cited JCAHO/AALAC/CAP Accreditation Deficiency.

Date Page Name/Title

3 MAY 1995 3 ENUSER1, E IGHT/INSPECTOR

POINTS

5

1.  Safety: Handicapped (UFAS), EPA/NRC, Fire/Safety (RSFPE), OSHA. Date Page Name/Title

0

2.  Space:

Not Applicable 0

3.  Energy Conservation:

Not Applicable 0

4.  Category Bonus (Scope Dependent):

Not Applicable 0

FACTOR SUBTOTAL 5

Project \#: 999-383

5.  VAMC Priority: \[Rank and Submit 2 Minor Design projects\]

PRIORITY 2 UNK

Select PROJECT NUMBER: \<RET\>

Approved Dates Screen Edit

Enter/edit approved dates on delegated projects. Approved dates indicate when certain project milestones were originally scheduled. Adherence to these dates is usually important in terms of keeping obligations consistent with an established spending plan.

Revised Dates Screen Edit

Enter/edit revised dates (if any) of project milestones. These dates must be exact (month-day-year) and should reflect any discrepancies between original schedule and current best estimates.

Actual Dates Screen Edit

Enter/edit actual milestone dates on Construction Project(s).

A/E Data Screen Edit

Enter/edit basic information on architectural firms retained by facility for specific projects.

Contractor Data Screen Edit

Enter/edit basic information on prime construction contractor for a delegated project.

Changes & Remarks Screen Edit

Enter/edit summary of change orders and narrative remarks.

Print Project Status Report

Generate hardcopy 10-0051 for a specific construction project.

Print All Project Status Reports

Print hardcopy 10-0051 of all construction projects for which the MONTHLY PRINT-OUT field is set to "YES".

Transmit 10-0051 Electronically

Packs 10-0051s into Network MailMan messages and routes them to the Office of Facilities in VACO.

## Project Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter Project Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ---\> 1 Enter Project Data

2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit 10 Print Project Status Report

11 Print All Project Status Reports 12 Transmit 10-0051 Electronically

In this option, you can enter project data as a new project is opened. You can also edit an existing project from this option.

Select Project Tracking Option: 1 Enter Project Data

To use this option, enter the construction project number. Typing \< ??\>\<RET\> after Select CONSTRUCTION PROJECT NUMBER will list all current construction project numbers.

Select Project Tracking Option: 1 Enter Project Data Select CONSTRUCTION PROJECT, PROJECT NUMBER: ??

CHOOSE FROM:

| 999-011 | BUILD HOSPITAL ANNEX         |
|---------|------------------------------|
| 999-012 | RENOVATE CLINICAL LABORATORY |
| 999-014 | EXPAND CLINICAL WARDS        |

Must begin with station number. Enter '??' for more help.

The principal identifier of entries in the CONSTRUCTION PROJECT file. Format should be either 'SSS-NNN' or 'SSS-YY-NNN'; where SSS is the facility number and NNN is a sequential project number.

YY is usually the fiscal year for which an NRM request is being submitted but may also be used for a two-character alphabetic project category designation.

Note that the facility number need not always be the number of the VAMC. For example, if you are reporting on a National Cemetery project the first 3 digits will generally be the facility number of the National Cemetery itself.

If you have questions about official project numbers, please consult your Project Manager in the Region.

Select CONSTRUCTION PROJECT, PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

If you enter a new Construction Project number, the CONSTRUCTION PROJECT TITLE is requested. After entering the title, the PROJECT NUMBER will be displayed.

PROJECT NUMBER: 999-011//

REPORT PERIOD END is the date for the end of the period covered by the report. If a date is already on the project, it is displayed with the "//". A \<?\> entered here will show the different formats for entering dates.

REPORTING PERIOD (Month/Year):??

Current reporting period. Used by Regional Offices for tracking project milestones over time.

Enter MONTH and YEAR only. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the PAST. You may omit the precise day, as: JAN, 1957

REPORTING PERIOD (Month/Year):

PROJECT TITLE will be asked next and can be changed by typing a new title.

PROJECT TITLE: BUILD HOSPITAL ANNEX Replace??

Official title of project.

PROJECT TITLE: BUILD HOSPITAL ANNEX Replace MONTHLY UPDATES: NO//??

This field determines whether or not a project will be included when Progress Reports of 'all projects' are requested. This field is examined when 10-0051's are transmitted electronically as well as when paper records are produced.

CHOOSE FROM:

Y YES

N NO

MONTHLY UPDATES: NO//

MEDICAL CENTER: ANYCITY, DC, VAMC//??

Facility where the work is being performed. May indicate.

a division or other functional element (National Cemetery, Regional Office, satellite clinic, etc.) if appropriate.

CHOOSE FROM:

VASITE ANYSTATE VAMC 590

ANYCITY, DC, VAMC ANYPLACE 999

MEDICAL CENTER: ANYCITY, DC, VAMC// FUNDING YEAR - A/E: 1993//??

This field contains the fiscal year for which A/E is funded or proposed.

FUNDING YEAR - A/E: 1993// FUNDING YEAR - CONST: 1993//??

Fiscal year for which construction is funded or proposed.

FUNDING YEAR - CONST: 1993// APPROVED A/E FUNDING:??

Amount (in whole dollars) authorized for A/E at the time project is approved.

APPROVED A/E FUNDING:

APPROVED CONSTRUCTION:??

Amount (in whole dollars) authorized for construction at the time project is approved.

APPROVED CONSTRUCTION:

STATUS: PLAN//??

Present status of the project.

CHOOSE FROM:

A/E

BID OPEN BO CANCELED

COMPLETED PROJECT CP CONSTRUCTION

CONSTRUCTION DRAWINGS CD DESIGN DRAWINGS DD DESIGN PROGRAM

DRAFT PROJECT

INVITATION FOR BID IFB

NEW PROJECT APPLICATION NP NON-VIABLE NV

PLAN PY

PROPOSED FOR BUDGET SCHEMATICS

STATION LEVEL PROJECT UNAPPROVED/VIABLE

STATUS: PLAN// DESIGN METHOD:??

Indicates the design method. CHOOSE FROM:

1.  A/E
2.  SBA 8(a)
3.  VAMC

DESIGN METHOD:

CONSTR. METHOD:??

Indicates the construction method. CHOOSE FROM:

1.  CONTRACT
2.  P&H
3.  STATION LABOR
4.  SBA 8(a)
5.  DESIGN/BUILD
6.  LEASE

CONSTR. METHOD:

% DESIGN PROGRAM COMPL:??

Completion percentage of design program (if applicable).

% DESIGN PROGRAM COMPL:

% SCHEMATICS COMPLETE:??

Current estimate of work done on schematics. Expressed as a percentage of completion.

% SCHEMATICS COMPLETE:

% DESIGN DRAWINGS COMPL: 50//??

Current estimate of how much work has been done on project design. Expressed as percentage of completion.

% DESIGN DRAWINGS COMPL: 50//

%CONST DRAWINGS COMP:??

Current estimate of the status of construction (working) drawings. Expressed as a percentage of completion.

%CONST DRAWINGS COMP:

% CONSTRUCTION COMPLETE: 0//??

Current estimate of construction works actually performed. Expressed as a percentage of completion.

% CONSTRUCTION COMPLETE: 0//

Many of the following fields require entering dates. An explanation of valid date formats is shown for DESIGN PROGRAM START. These formats apply to the other date fields as well.

DESIGN PROGRAM START (PLANNED): MAY 25,1993//??

Planned start of design program. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the PAST. You may omit the precise day, as: JAN, 1957

DESIGN PROGRAM START (PLANNED): MAY 25,1993// DESIGN PROGRAM COMP. (PLANNED): MAY 25,1993//??

Planned completion of design program.

DESIGN PROGRAM COMP. (PLANNED): MAY 25,1993// ADVERTISE FOR A/E (PLANNED): MAY 25,1993//??

Planned date for A/E advertisement.

ADVERTISE FOR A/E (PLANNED): MAY 25,1993// SELECT A/E (PLANNED): MAY 25,1993//

Planned selection date for A/E. A/E AWARD (PLANNED): MAY 25,1993//??

Planned A/E award date.

A/E AWARD (PLANNED): MAY 25,1993//

START SCHEMATICS (PLANNED): MAY 25,1993//??

Planned date for the start of schematic plans.

START SCHEMATICS (PLANNED): MAY 25,1993// COMPLETE SCHEMATICS (PLANNED): MAY 25,1993//??

Original (approved) target date for completion of preliminary plans.

COMPLETE SCHEMATICS (PLANNED): MAY 25,1993//

START DESIGN DRWGS. (PLANNED): MAY 25,1993//??

Planned (approved) start of design drawings.

START DESIGN DRWGS. (PLANNED): MAY 25,1993// COMPL. DESIGN DRWGS. (PLANNED): MAY 25,1993//??

Planned (approved) completion of design drawings.

COMPL. DESIGN DRWGS. (PLANNED): MAY 25,1993// START CONST. DRWGS. (PLANNED): MAY 25,1993//??

Original (approved) date for start of working drawings.

START CONST. DRWGS. (PLANNED): MAY 25,1993// COMPL. CONST. DRWGS. (PLANNED): MAY 25,1993//??

Original (approved) target date for completion of construction drawings.

COMPL. CONST. DRWGS. (PLANNED): MAY 25,1993// ISSUE IFB (PLANNED): MAY 25,1993//??

Original (approved) target date for issuance of Invitation for Bids.

ISSUE IFB (PLANNED): MAY 25,1993// BID OPEN (PLANNED): MAY 25,1993//??

Original (approved) target date for bid openings.

BID OPEN (PLANNED): MAY 25,1993//

CONSTRUCTION AWARD (PLANNED): MAY 25,1993//??

Original (approved) target date for award of construction contract(s).

CONSTRUCTION AWARD (PLANNED): MAY 25,1993// CONSTRUCTION START (PLANNED): MAY 25,1993//??

Original (approved) target date for start of construction.

CONSTRUCTION START (PLANNED): MAY 25,1993// CONST. COMPLETE (PLANNED):??

Original (approved) target date by which construction is to be substantially complete.

CONST. COMPLETE (PLANNED):

ACTIVATION (PLANNED):??

Original (approved) target date for project activation.

ACTIVATION (PLANNED):

DESIGN PROGRAM START (REVISED):??

Revised design program start date.

DESIGN PROGRAM START (REVISED):

DESIGN PROGRAM COMP. (REVISED):??

Revised design program completion date.

DESIGN PROGRAM COMP. (REVISED):

ADVERTISE FOR A/E (REVISED):??

Revised date for A/E advertisement.

ADVERTISE FOR A/E (REVISED):

SELECT A/E (REVISED):??

Revised date for selection of A/E. SELECT A/E (REVISED):

A/E AWARD (REVISED):??

Revised date for A/E award.

A/E AWARD (REVISED):

START SCHEMATICS (REVISED):??

Current (revised) estimate of starting date for development of schematics.

START SCHEMATICS (REVISED):

COMPL. SCHEMATICS (REVISED):??

Current (revised) estimate as to when schematics will be complete.

COMPL. SCHEMATICS (REVISED):

START DESIGN DRWGS. (REVISED):??

Revised date for start of design drawings.

START DESIGN DRWGS. (REVISED):

COMPL. DESIGN DRWGS. (REVISED):??

Revised date for completion of design drawings.

COMPL. DESIGN DRWGS. (REVISED):

START CONST. DRWGS. (REVISED):??

Current (revised) estimate of the starting date for development of construction drawings.

START CONST. DRWGS. (REVISED):

COMPL. CONST. DRWGS. (REVISED):??

Current (revised) estimate of the target date for completion of construction drawings.

COMPL. CONST. DRWGS. (REVISED):

ISSUE IFB (REVISED):??

Current (revised) estimate of the target date for issuance of the Invitation for Bids.

ISSUE IFB (REVISED):

BID OPEN (REVISED):??

Current (revised) estimate of the target date for bid openings.

BID OPEN (REVISED):

CONSTRUCTION AWARD (REVISED):??

Current (revised) estimate of the target date for award of the construction contract(s).

CONSTRUCTION AWARD (REVISED):

CONSTRUCTION START (REVISED):??

Current (revised) estimate of the target date for the start of construction.

CONSTRUCTION START (REVISED):

CONST. COMPLETE (REVISED):??

Current (revised) target date by which it is expected that construction will be substantially complete.

CONST. COMPLETE (REVISED):

ACTIVATION (REVISED):??

Revised date for project activation.

ACTIVATION (REVISED):

DESIGN PROGRAM START (ACTUAL):??

Actual date of design program start.

DESIGN PROGRAM START (ACTUAL):

DESIGN PROGRAM COMPL. (ACTUAL):??

Actual date of design program completion.

DESIGN PROGRAM COMPL. (ACTUAL):

AUTHOR. LTR. REC'D. (ACTUAL):??

Actual date of Issue Letter. This is the transmittal used by regions to formally approve a project.

AUTHOR. LTR. REC'D. (ACTUAL):

ADVERTISE FOR A/E (ACTUAL):??

Date of advertisement for Architect/Engineer.

ADVERTISE FOR A/E (ACTUAL):

SELECT A/E (ACTUAL):??

Actual date of selection of Architect/Engineer.

SELECT A/E (ACTUAL):

A/E AWARD (ACTUAL):??

Date of contract award to Architect/Engineer.

A/E AWARD (ACTUAL):

START SCHEMATICS (ACTUAL):??

Actual date on which schematic plans were begun.

START SCHEMATICS (ACTUAL):

COMPL. SCHEMATICS (ACTUAL):??

Date on which schematic plans were actually completed.

COMPL. SCHEMATICS (ACTUAL):

START DESIGN DRWGS. (ACTUAL):??

Actual start of design drawings.

START DESIGN DRWGS. (ACTUAL):

COMPL. DESIGN DRWGS. (ACTUAL):??

Actual completion date for design drawings.

COMPL. DESIGN DRWGS. (ACTUAL):

START CONST. DRWGS. (ACTUAL):??

Date on which construction drawings were begun.

START CONST. DRWGS. (ACTUAL):

COMPL. CONST. DRWGS. (ACTUAL):??

Actual date on which construction drawings were completed.

COMPL. CONST. DRWGS. (ACTUAL):

ISSUE IFB (ACTUAL):??

Actual date of issuance of Invitation for Bids.

ISSUE IFB (ACTUAL):

BID OPEN (ACTUAL):??

Actual date of bid opening.

If the date is omitted, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc. You may enter a time, such as NOON, MIDNIGHT or NOW.

BID OPEN (ACTUAL):

CONSTRUCTION AWARD (ACTUAL):??

Actual date of award of construction contract.

CONSTRUCTION AWARD (ACTUAL):

CONSTRUCTION START (ACTUAL):??

Date on which construction actually began.

CONSTRUCTION START (ACTUAL):

CONST. COMPLETE (ACTUAL):??

Actual date on which construction was judged to be substantially complete.

CONST. COMPLETE (ACTUAL): ACTIVATION (ACTUAL):??

Actual date of project activation.

ACTIVATION (ACTUAL): A/E CONTRACT \#:??

Official identifier of contract with Architect/Engineer for project design and related services.

A/E CONTRACT \#:

A/E NAME:??

Name of Architect/Engineer firm retained for this project.

A/E NAME:

A/E ADDR1:??

First line of Architect/Engineer address. May be up to 35 characters long and should generally contain the street address or post office box (or equivalent).

A/E ADDR1:

A/E ADDR2:??

Second (and final) line of Architect/Engineer address. May be up to

35 characters long and should generally contain the city, state, and zip code.

A/E ADDR2:

A/E FUND CONTROL POINT:??

Fund control point (IFCAP) for design obligations.

A/E FUND CONTROL POINT:

A/E AWARD AMOUNT:??

Original A/E award obligation.

A/E AWARD AMOUNT:

A/E STUDY:??

Amount obligated to A/E for performance of a formal study.

A/E STUDY:

A/E SCHEMATICS:??

Amount obligated for Architect/Engineer services in development of schematics. Round to nearest whole dollar.

A/E SCHEMATICS:

A/E DESIGN DEVELOPMENT:??

Amount obligated to A/E for design development. Round to nearest whole dollar.

A/E DESIGN DEVELOPMENT:

A/E CONST DOCUMENTS:??

Amount obligated for Architect/Engineer services in development of working drawings and specifications. Round to nearest whole dollar.

A/E CONST DOCUMENTS:

A/E SITE SURVEY:??

Amount obligated to Architect/Engineer for services in

making site surveys and related activities. Round to nearest whole dollar.

A/E SITE SURVEY:

A/E CONST PER SERVCS:??

Amount obligated to Architect/Engineer for services to the

medical center during the course of the actual construction period. Round to nearest whole dollar.

A/E CONST PER SERVCS:

A/E OTHER SERVICES:??

Amount obligated to A/E for services not otherwise classified.

A/E OTHER SERVICES:

A/E SA ADDITION (#):??

SA stands for supplemental agreement.

Number of A/E supplemental agreements that add to the cost of design.

A/E SA ADDITION (#):

A/E SA ADDITIONS (\$):??

SA stands for supplemental agreement.

Total cost of A/E supplemental agreements that increase design costs.

A/E SA ADDITIONS (\$):

A/E SA DEDUCTIONS (#):??

SA stands for supplemental agreements.

Number of A/E supplemental agreements that reduce design cost.

A/E SA DEDUCTIONS (#):

A/E SA DEDUCTIONS (\$):??

SA stands for supplemental agreements.

Total dollar value of all A/E supplemental agreements that decrease design cost.

A/E SA DEDUCTIONS (\$):

CONST. CONTRACT \#:??

Unique identifier (contract number) of contract with a construction firm for the actual construction portion of this project.

CONST. CONTRACT \#:

CONTR. NAME:??

Name of the firm chosen as the prime (or sole) contractor for the construction portion of this project.

CONTR. NAME:

CONTR. ADDR1:??

First line of the construction contractor's two-line mailing address. Should generally contain the street address or post office box (or equivalent).

CONTR. ADDR1:

CONTR. ADDR2:??

Second (and last) line of the construction contractor's mailing address. Should generally contain the city, state, and zip code.

CONTR. ADDR2:

CONSTRUCTION AWARD:??

Amount of original construction award. Should not include P&H (purchase and hire) or supplemental agreements (if any).

CONSTRUCTION AWARD:

P&H LABOR TO DATE:??

Total expenditure on purchase and hire labor to date.

in order to award the contract without exceeding available funding.

P&H LABOR TO DATE:

P&H MATERIALS TO DATE:??

Total expenditure on purchase and hire materials to date.

P&H MATERIALS TO DATE:

CONST SA ADDITIONS (#):??

SA stands for supplemental agreement.

Total number of supplemental agreements that added to the construction cost.

CONST SA ADDITIONS (#):

CONST SA ADDITIONS (\$):??

SA stands for supplemental agreements.

The sum of the dollar value (rounded to the nearest dollar) of all supplemental agreements that increase the cost of the project.

CONST SA ADDITIONS (\$):

CONST SA DEDUCTIONS (#):??

SA stands for supplemental agreements.

Total number of supplemental agreements that decreased the construction cost.

CONST SA DEDUCTIONS (#):

CONST SA DEDUCTIONS (\$):??

SA stands for supplemental agreements.

The sum (to the nearest whole dollar) of all supplemental agreements that decreased the cost of construction on an approved.

project.

CONST SA DEDUCTIONS (\$):

CONST FUND CONTROL PT:??

Fund control point (IFCAP) for construction obligations.

CONST FUND CONTROL PT:

TIME EXTENSION (DAYS):??

Time extension granted contractor, usually as a result of supplemental agreements.

TIME EXTENSION (DAYS):

REMARKS:

You are ready to enter a line of text.

If you have no text to enter, just press the return key. Type 'CONTROL-I' (or TAB key) to insert tabs.

When text is output, these formatting rules will apply:

1)  Lines containing only punctuation characters, or lines containing tabs will stand by themselves, i.e., no wrap-around.
2)  Lines beginning with spaces will start on a new line.
3)  Expressions between '\|' characters will be evaluated as 'computed-field expressions and then be printed as evaluated.

thus '\|NAME\|' would cause the current name to be inserted in the text.

- Want to see a list of allowable formatting 'WINDOWS'? NO// (NO) 1\>

PROGRESS NOTE:?

ANSWER MUST BE 1-235 CHARACTERS IN LENGTH PROGRESS NOTE:

Select CONSTRUCTION PROJECT NUMBER:

The system will then prompt for a new project number. If you do not wish to go to another project number, you can press \< RET\>, which will return you to the Project Tracking Options menu.

### Screen Review All Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a screen review of all the project data. Enter the project number and the screen will display page one as shown on the printout below.

PROJECT TRACKING OPTIONS

> 1 Enter Project Data

> ---\>2 Screen Review All Data

3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit 10 Print Project Status Report

11 Print All Project Status Reports 12 Transmit 10-0051 Electronically

Select Construction Project Option: 2 Screen Review All Data

CONSTRUCTION PROJECT (999-011) PAGE 1

| 1   | PROJECT NUMBER:         |         | 999-011              |
|-----|-------------------------|---------|----------------------|
| 2   | REPORTING PERIOD        |         | (Month/Year):        |
| 3   | PROJECT TITLE:          |         | BUILD HOSPITAL ANNEX |
| 4   | MONTHLY UPDATES:        |         | NO                   |
| 5   | MEDICAL CENTER:         |         | ANYCITY, DC, VAMC    |
| 6   | FUNDING YEAR            | \- A/E: | 1993                 |
| 7   | FUNDING YEAR - CONST:   |         | 1993                 |
| 8   | APPROVED A/E FUNDING:   |         |                      |
| 9   | APPROVED CONSTRUCTION:  |         |                      |
| 10  | TOTAL FUNDS APPROVED:   |         | 0                    |
| 11  | STATUS:                 |         | A/E                  |
| 12  | DESIGN METHOD:          |         |                      |
| 13  | CONSTR. METHOD:         |         |                      |
| 14  | % DESIGN PROGRAM COMPL: |         |                      |
| 15  | % SCHEMATICS COMPLETE:  |         |                      |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

The eight screens present the information in the order that it was entered. The ability to make changes in any line entry is provided at the bottom of the screen. Select more than one line number at a time by putting a semicolon between the numbers. If they are consecutively numbered lines, the beginning and ending numbers can be entered with a colon between them. You can go to the next page by pressing \< RET\> or go backwards by entering a minus sign. You have the option of terminating the screen option by using the \<^\> for "QUIT" or a \<^^\> for rapid out. Both actions accomplish the same thing.

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  % DESIGN DRAWINGS COMPL: 50
2.  %CONST DRAWINGS COMP:
3.  % CONSTRUCTION COMPLETE: 0
4.  DESIGN PROGRAM START (PLANNED): MAY 25, 1993
5.  DESIGN PROGRAM COMP. (PLANNED): MAY 25, 1993
6.  ADVERTISE FOR A/E (PLANNED): MAY 25, 1993
7.  SELECT A/E (PLANNED): MAY 25, 1993
8.  A/E AWARD (PLANNED): MAY 25, 1993
9.  START SCHEMATICS (PLANNED): MAY 25, 1993
10. COMPLETE SCHEMATICS (PLANNED): MAY 25, 1993
11. START DESIGN DRWGS. (PLANNED): MAY 25, 1993
12. COMPL. DESIGN DRWGS. (PLANNED): MAY 25, 1993
13. START CONST. DRWGS. (PLANNED): MAY 25, 1993
14. COMPL. CONST. DRWGS. (PLANNED): MAY 25, 1993
15. ISSUE IFB (PLANNED): MAY 25, 1993

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 3

1.  BID OPEN (PLANNED): MAY 25, 1993
2.  CONSTRUCTION AWARD (PLANNED): MAY 25, 1993
3.  CONSTRUCTION START (PLANNED): MAY 25, 1993
4.  CONST. COMPLETE (PLANNED):
5.  ACTIVATION (PLANNED):
6.  DESIGN PROGRAM START (REVISED):
7.  DESIGN PROGRAM COMP. (REVISED):
8.  ADVERTISE FOR A/E (REVISED):
9.  SELECT A/E (REVISED):
10. A/E AWARD (REVISED):
11. START SCHEMATICS (REVISED):
12. COMPL. SCHEMATICS (REVISED):
13. START DESIGN DRWGS. (REVISED):
14. COMPL. DESIGN DRWGS. (REVISED):
15. START CONST. DRWGS. (REVISED):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 4

1.  COMPL. CONST. DRWGS. (REVISED):
2.  ISSUE IFB (REVISED):
3.  BID OPEN (REVISED):
4.  CONSTRUCTION AWARD (REVISED):
5.  CONSTRUCTION START (REVISED):
6.  CONST. COMPLETE (REVISED):
7.  ACTIVATION (REVISED):
8.  DESIGN PROGRAM START (ACTUAL):
9.  DESIGN PROGRAM COMPL. (ACTUAL):
10. AUTHOR. LTR. REC'D. (ACTUAL):
11. ADVERTISE FOR A/E (ACTUAL):
12. SELECT A/E (ACTUAL): MAY 24, 1993
13. A/E AWARD (ACTUAL):
14. START SCHEMATICS (ACTUAL):
15. COMPL. SCHEMATICS (ACTUAL):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 5

1.  START DESIGN DRWGS. (ACTUAL):
2.  COMPL. DESIGN DRWGS. (ACTUAL):
3.  START CONST. DRWGS. (ACTUAL):
4.  COMPL. CONST. DRWGS. (ACTUAL):
5.  ISSUE IFB (ACTUAL):
6.  BID OPEN (ACTUAL):
7.  CONSTRUCTION AWARD (ACTUAL):
8.  CONSTRUCTION START (ACTUAL):
9.  CONST. COMPLETE (ACTUAL):
10. ACTIVATION (ACTUAL):
11. A/E CONTRACT \#:
12. A/E NAME:
13. A/E ADDR1:
14. A/E ADDR2:
15. A/E FUND CONTROL POINT:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

|     | CONSTRUCTION PROJECT    | (999-011) | PAGE 6 |
|-----|-------------------------|-----------|--------|
| 1   | A/E STUDY:              |           |        |
| 2   | A/E SCHEMATICS:         |           |        |
| 3   | A/E DESIGN DEVELOPMENT: |           |        |
| 4   | A/E CONST DOCUMENTS:    |           |        |
| 5   | A/E SITE SURVEY:        |           |        |
| 6   | A/E CONST PER SERVCS:   |           |        |
| 7   | A/E OTHER SERVICES:     |           |        |
| 8   | A/E SA ADDITION (#):    |           |        |
| 9   | A/E SA ADDITIONS (\$):  |           |        |
| 10  | A/E SA DEDUCTIONS (#):  |           |        |
| 11  | A/E SA DEDUCTIONS (\$): |           |        |
| 12  | A/E AWARD AMOUNT:       |           |        |
| 13  | A/E SA NET (\$):        | 0         |        |
| 14  | A/E OBLIGATED:          | 0         |        |
| 15  | TOTAL PROJ OBLIGATION:  | 0         |        |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT)

| ("^^" RAPID OUT)             |           |        |
|------------------------------|-----------|--------|
| CONSTRUCTION PROJECT         | (999-011) | PAGE 7 |
| 1 CONST. CONTRACT \#:        |           |        |
| 2 CONTR. NAME:               |           |        |
| 3 CONTR. ADDR1:              |           |        |
| 4 CONTR. ADDR2:              |           |        |
| 5 P&H LABOR TO DATE:         |           |        |
| 6 P&H MATERIALS TO DATE:     |           |        |
| 7 CONST SA ADDITIONS (#):    |           |        |
| 8 CONST SA ADDITIONS (\$):   |           |        |
| 9 CONST SA DEDUCTIONS (#):   |           |        |
| 10 CONST SA DEDUCTIONS (\$): |           |        |
| 11 CONSTRUCTION AWARD:       |           |        |
| 12 TOTAL P&H:                | 0         |        |
| 13 CONST SUPPL (NET \$):     | 0         |        |
| 14 TOTAL CONST OBLIGATION:   | 0         |        |
| 15 TOTAL PROJ OBLIGATION:    | 0         |        |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 8

1.  CONST FUND CONTROL PT:
2.  TIME EXTENSION (DAYS):
3.  REMARKS: (WORD PROCESSING)
4.  PROGRESS NOTE:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

The fourth entry on page 8 of the printout is a word processing field which will allow several lines of comments. When the 10-0051 reports are transmitted electronically, the PROGRESS NOTE is automatically saved in the REMARKS field for future reference. When the printout indicates (DATA) on this line, there are remarks. The remarks can be viewed by entering "4".

### Preliminary Data Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preliminary Data Screen gives the first fifteen entries of the project information.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data

> ---\> 3 Preliminary Data Screen

4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit 10 Print Project Status Report

11 Print All Project Status Reports 12 Transmit 10-0051 Electronically

Select Project Tracking Option: 3 Preliminary Data Screen

Select CONSTRUCTION PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

CONSTRUCTION PROJECT (999-011) PAGE 1

1.  PROJECT NUMBER: 999-011
2.  REPORTING PERIOD (Month/Year):
3.  PROJECT TITLE: BUILD HOSPITAL ANNEX
4.  MONTHLY UPDATES: NO
5.  MEDICAL CENTER: ANYCITY, DC, VAMC
6.  FUNDING YEAR - A/E: 1993
7.  FUNDING YEAR - CONST: 1993
8.  APPROVED A/E FUNDING:
9.  APPROVED CONSTRUCTION:
10. TOTAL FUNDS APPROVED: 0
11. STATUS: A/E
12. DESIGN METHOD:
13. CONSTR. METHOD:
14. GROSS SQUARE FEET:
15. % DESIGN PROGRAM COMPL:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  % SCHEMATICS COMPLETE:
2.  % DESIGN DRAWINGS COMPL: 50
3.  % CONST DRAWINGS COMP:
4.  % CONSTRUCTION COMPLETE: 0

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

The above information can be edited in the same manner as was shown in the section Screen Review All Data. Pressing \< RET\> will return you to the Project Tracking Options menu.

### Approved Dates Screen Edit.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to edit the Approved Dates fields.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen

> ---\> 4 Approved Dates Screen Edit

5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit
10. 10 Print Project Status Report
11. Print All Project Status Reports
12. 12 Transmit 10-0051 Electronically

Select Construction Project Option: 4 Approved Dates Screen Edit

Select Project Tracking Option: Preliminary Data Screen

Select CONSTRUCTION PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

CONSTRUCTION PROJECT (999-011) PAGE 1

1.  DESIGN PROGRAM START (PLANNED): MAY 25, 1993
2.  DESIGN PROGRAM COMP. (PLANNED): MAY 25, 1993
3.  ADVERTISE FOR A/E (PLANNED): MAY 25, 1993
4.  SELECT A/E (PLANNED): MAY 25, 1993
5.  A/E AWARD (PLANNED): MAY 25, 1993
6.  START SCHEMATICS (PLANNED): MAY 25, 1993
7.  COMPLETE SCHEMATICS (PLANNED): MAY 25, 1993
8.  START DESIGN DRWGS. (PLANNED): MAY 25, 1993
9.  COMPL. DESIGN DRWGS. (PLANNED): MAY 25, 1993
10. START CONST. DRWGS. (PLANNED): MAY 25, 1993
11. COMPL. CONST. DRWGS. (PLANNED): MAY 25, 1993
12. ISSUE IFB (PLANNED): MAY 25, 1993
13. BID OPEN (PLANNED): MAY 25, 1993
14. CONSTRUCTION AWARD (PLANNED): MAY 25, 1993
15. CONSTRUCTION START (PLANNED): MAY 25, 1993

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  CONST. COMPLETE (PLANNED):
2.  ACTIVATION (PLANNED):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

Any of the information in the above printout can be changed by entering the entry number and then changing the information. Upon pressing \< RET\>, you will return to the Project Tracking Options menu.

### Revised Dates Screen Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section gives you the opportunity to edit all the revised dates on the project.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit

> ---\> 5 Revised Dates Screen Edit

6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit 10 Print Project Status Report

11 Print All Project Status Reports 12 Transmit 10-0051 Electronically

Select Construction Project Option: 5 Revised Dates Screen Edit

Select Project Tracking Option: 5 Revised Dates Screen Edit

Select CONSTRUCTION PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

CONSTRUCTION PROJECT (999-011) PAGE 1

1.  DESIGN PROGRAM START (REVISED):
2.  DESIGN PROGRAM COMP. (REVISED):
3.  ADVERTISE FOR A/E (REVISED):
4.  SELECT A/E (REVISED):
5.  A/E AWARD (REVISED):
6.  START SCHEMATICS (REVISED):
7.  COMPL. SCHEMATICS (REVISED):
8.  START DESIGN DRWGS. (REVISED):
9.  COMPL. DESIGN DRWGS. (REVISED):
10. START CONST. DRWGS. (REVISED):
11. COMPL. CONST. DRWGS. (REVISED):
12. ISSUE IFB (REVISED):
13. BID OPEN (REVISED):
14. CONSTRUCTION AWARD (REVISED):
15. CONSTRUCTION START (REVISED):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  CONST. COMPLETE (REVISED):
2.  ACTIVATION (REVISED):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

As these dates become available, they can be entered using this screen display. Indicate the item number and then make the change when the computer prompts for the item.

### Actual Dates Screen Edit.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for editing the actual dates from the screen. The screen display for this option is indicated below.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit

> ---\> 6 Actual Dates Screen Edit

7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit 10 Print Project Status Report

11 Print All Project Status Reports 12 Transmit 10-0051 Electronically

Select Construction Project Option: 6 Actual Dates Screen Edit

Select Project Tracking Option: 6 Actual Dates Screen Edit

Select CONSTRUCTION PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

CONSTRUCTION PROJECT (999-011) PAGE 1

1.  DESIGN PROGRAM START (ACTUAL):
2.  DESIGN PROGRAM COMPL. (ACTUAL):
3.  AUTHOR. LTR. REC'D. (ACTUAL):
4.  ADVERTISE FOR A/E (ACTUAL):
5.  SELECT A/E (ACTUAL): MAY 24, 1993
6.  A/E AWARD (ACTUAL):
7.  START SCHEMATICS (ACTUAL):
8.  COMPL. SCHEMATICS (ACTUAL):
9.  START DESIGN DRWGS. (ACTUAL):
10. COMPL. DESIGN DRWGS. (ACTUAL):
11. START CONST. DRWGS. (ACTUAL):
12. COMPL. CONST. DRWGS. (ACTUAL):
13. ISSUE IFB (ACTUAL):
14. BID OPEN (ACTUAL):
15. CONSTRUCTION AWARD (ACTUAL):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  CONSTRUCTION START (ACTUAL):
2.  CONST. COMPLETE (ACTUAL):
3.  ACTIVATION (ACTUAL):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

This information can be edited or changed by entering the item number and then making the changes the computer requests.

### A/E-Contractor Data Screen Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the editing of architectural engineer-contractor information.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit

> ---\> 7 A/E Data Screen Edit

8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit
10. 10 Print Project Status Report
11. Print All Project Status Reports
12. 12 Transmit 10-0051 Electronically

Select Construction Project Option: 7 A/E-Contractor Data Screen Edit

Select Project Tracking Option: 7 A/E Data Screen Edit

Select CONSTRUCTION PROJECT NUMBER: 999-011 BUILD HOSPITAL ANNEX

PAGE 1

OTHER SERVICES:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  A/E CONTRACT \#:
2.  A/E FUND CONTROL POINT:
3.  A/E NAME:
4.  A/E ADDR1:
5.  A/E ADDR2:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

This information can be edited by indicating the item number and then making the changes as the computer requests them. Upon pressing \< RET\>, you will return to the Project Tracking Options menu.

### Contractor Data Screen Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen allows entry of information about the contractor and the construction.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit

> ---\> 8 Contractor Data Screen Edit

8.  Changes & Remarks Screen Edit
9.  10 Print Project Status Report
10. Print All Project Status Reports
11. 12 Transmit 10-0051 Electronically

Select Construction Project Option: 8 Contractor Data Screen Edit

CONSTRUCTION PROJECT (999-011) PAGE 1

1.  CONST. CONTRACT \#:
2.  CONTR. NAME:
3.  CONTR. ADDR1:
4.  CONTR. ADDR2:
5.  P&H LABOR TO DATE:
6.  P&H MATERIALS TO DATE:
7.  CONST SA ADDITIONS (#):
8.  CONST SA ADDITIONS (\$):
9.  CONST SA DEDUCTIONS (#):
10. CONST SA DEDUCTIONS (\$):
11. CONSTRUCTION AWARD:
12. TOTAL P&H: 0
13. CONST SUPPL (NET \$): 0
14. TOTAL CONST OBLIGATION: 0
15. TOTAL PROJ OBLIGATION: 0

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT (999-011) PAGE 2

1.  CONST FUND CONTROL PT:
2.  TIME EXTENSION (DAYS):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

### Changes & Remarks Screen Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number of change orders and the dollar amounts can be adjusted using this option. The Remarks field, which contains information to be electronically transferred via a 10-0051 maintenance report, may also be added (refer to Option 12, "Transmit Data Electronically," for additional information).

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit

> ---\> 9 Changes & Remarks Screen Edit

> 10 Print Project Status Report

1.  Print All Project Status Reports
2.  12 Transmit 10-0051 Electronically

Select Construction Project Option: 9 Changes & Remarks Screen Edit

OPTION 9 CHANGES & REMARKS SCREEN EDIT

Select Project Tracking Option: 9 Changes & Remarks Screen Edit

| Select CONSTRUCTION PROJECT NUMBER: 999-011 |                           |                   | BUILD HOSPITAL ANNEX |
|---------------------------------------------|---------------------------|-------------------|----------------------|
|                                             | CONSTRUCTION PROJECT      | (999-011)         | PAGE 1               |
| 1                                           | CONST SA ADDITIONS (#):   |                   |                      |
| 2                                           | CONST SA ADDITIONS (\$):  |                   |                      |
| 3                                           | CONST SA DEDUCTIONS (#):  |                   |                      |
| 4                                           | CONST SA DEDUCTIONS (\$): |                   |                      |
| 5                                           | CONST SUPPL (NET \$):     | 0                 |                      |
| 6                                           | TOTAL CONST OBLIGATION:   | 0                 |                      |
| 7                                           | TIME EXTENSION (DAYS):    |                   |                      |
| 8                                           | TOTAL PROJ OBLIGATION:    | 0                 |                      |
| 9                                           | REMARKS:                  | (WORD PROCESSING) |                      |
| 10                                          | PROGRESS NOTE:            |                   |                      |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

### Print Project Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Project Status Report option gives a printout of the DM&S Project Progress Report RCS 10-311. This computer printout can be submitted to Central Office in place of VA FORM 10-0051s that have been submitted in the past.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit

> ---\>10 Print Project Status Report

11. Print All Project Status Reports
12. 12 Transmit 10-0051 Electronically

Select Construction Project Option: 10 Print Project Status Report

If the report is done on the screen, \< RET\> can be entered and then the computer will prompt with a right margin. If you wish to change this, you can type in a new number. The report requires four screen displays. \< RET\> has to be entered after each screen in order to access the next one.

When produced from a printer, the report is continuous, as shown below. When the printout for the particular project is completed, \< RET\> can be entered to access the Project Tracking Options menu.

- Select Project Tracking Option: 10 Print Project Status Report
- Select CONSTRUCTION PROJECT NUMBER: 999-92-001a RENOVATE HEMATOLOGY LAB
- DEVICE: HOME// LASERDP DEVELOPMENT
- DO YOU WANT YOUR OUTPUT QUEUED? NO// Q• •Y (YES)
- Requested Start Time: NOW// (MAY 26, 1993@11:50:47)

VETERANS HEALTH ADMINISTRATION PROJECT PROGRESS REPORT FACILITY: ANYCITY, DC, VAMC FACILITY TYPE: VHA

PROJECT NUMBER: 999-92-001A REPORTING PERIOD: APR 1993 TITLE: RENOVATE HEMATOLOGY LAB

PROGRAM: NR STATUS: PLAN

PROJECT CATEGORY: FIRE AND SAFETY BUDGET CATEGORY: FIRE AND SAFETY

FY METHOD

\# NEW NHCU BEDS:

\# NHCU BEDS RENOVATED: \# NHCU BEDS CONVERTED:

\$ APPROVED \$ OBLIGATED.

| PROJECT              | PLANNED | PLANNED | REVISED/ACTUAL | PREVIOUSLY | PERCENT  |
|----------------------|---------|---------|----------------|------------|----------|
| MILESTONE            | QUARTER | DATE    | DATE           | REPORTED   | COMPLETE |
| Design Program Start | 93.1    | 12-92   | 12-28-92A      |            |          |
| Design Prog Complete | 93.1    | 12-92   | 01-06-93A      |            | 100      |
| Auth Letter Received |         |         | 01-11-93A      |            |          |
| Advertise for A/E    | 93.2    | 01-93   | 01-16-93A      |            |          |
| Select A/E           | 93.2    | 01-93   | 01-21-93A      |            |          |
| A/E Award            | 93.2    | 01-93   | 01-26-93A      |            |          |
| Start Schematics     | 93.2    | 01-93   | 01-31-93A      |            |          |
| Complete Schematics  | 93.2    | 01-93   | 02-06-93A      |            | 100      |
| Start DD             | 93.2    | 01-93   | 02-11-93A      |            |          |
| Complete DD          | 93.2    | 02-93   | 02-16-93A      |            | 100      |
| Start CD             | 93.2    | 02-93   | 02-21-93A      |            |          |
| Complete CD          | 93.2    | 02-93   | 02-26-93A      |            | 100      |
| Issue IFB            | 93.2    | 02-93   | 03-04-93A      |            |          |
| Bid Open             | 93.2    | 02-93   | 03-09-93A      |            |          |
| Construction Award   | 93.2    | 03-93   | 03-14-93A      |            |          |
| Construction Start   | 93.2    | 03-93   | 03-23-93A      |            |          |

Construction Complete 93.3 05-93 06-15-93 30

Activation 93.4 07-93 08-01-93

ARCHITECT/ENGINEER CONTRACT DATA Contract: 590-00234 \$: 10500 FCP: 384-A/E

| A/E Name and Address:                 |      | Study:                 | 1000  |
|---------------------------------------|------|------------------------|-------|
| DESIGNS IN TYME                       |      | Schematics:            | 2000  |
| 1289 BROAD CREEK ROAD                 |      | Design Drawings:       |       |
| POQUOSON, VA. 23423                   |      | Construction Drawings: | 7000  |
| \*\* A/E Supplemental Agreements \*\* |      | Site Survey:           |       |
| Add \#: 2 \$:                         | 1000 | Const Period Services: |       |
| Ded \#: 1 \$:                         | 300  | Other:                 | 500   |
| Net \$:                               | 700  | Subtotal:              | 10500 |

CONSTRUCTION CONTRACT DATA Contract: 590-00219 \$: 112500 FCP: 385-CONST

Contractor Name and Address: \*\* P&H OBLIGATIONS (if applicable) \*\* VA BUILDERS Labor (to date): 1200

2000 EASY STREET Matrls (to date): 500

GRAFTON, VA 23612 TOTAL P&H: 1700

\*\*\*\*\*\*\*\*\*\*\* Construction Supplemental Agreements (Change Orders) \*\*\*\*\*\*\*\*\*\*\*\*

> **NOTE:** First electronic progress notes on this project. Select CONSTRUCTION PROJECT, PROJECT NUMBER:

### Print All Project Status Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print All Project Status Reports provides the same information as the previous option. In this case you will get a printout for each active project. This would normally be done on the printer and provide for all the project reports at one time that have to be submitted to Central Office.

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit
10. 10 Print Project Status Report

> ---\>11 Print All Project Status Reports

> 12 Transmit 10-0051 Electronically

Every project for which the MONTHLY UPDATES field is set to "YES" will be represented in the output from this option.

### Transmit 10-0051 Electronically

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option places 10-0051 reports into MailMan messages, and routes them to the Office of Facilities at VACO.

If the site AEMS/MERS system is not physically connected to the site VISTA computers, or linked to IDCU in some way, this option should be disabled by entering something in the OUT OF ORDER MESSAGE field.

PROJECT TRACKING OPTIONS

1.  Enter Project Data
2.  Screen Review All Data
3.  Preliminary Data Screen
4.  Approved Dates Screen Edit
5.  Revised Dates Screen Edit
6.  Actual Dates Screen Edit
7.  A/E-Contractor Data Screen Edit
8.  Contractor Data Screen Edit
9.  Changes & Remarks Screen Edit
10. Print Project Status Report
11. Print All Project Status Reports

> ---\>12 Transmit 10-0051 Electronically

Select Project Tracking Option: 12 Transmit 10-0051 Electronically

Electronic Transmission of VHA Project Progress Report Form 10-0051 Transmit report(s) for:

1.  One project, or
2.  All projects.

Enter a number (1-2): 1.

HEMATOLOGY LAB

| 1   | PROJECT NUMBER:         | 999-011              |
|-----|-------------------------|----------------------|
| 2   | REPORTING PERIOD        | (Month/Year          |
| 3   | PROJECT TITLE:          | BUILD HOSPITAL ANNEX |
| 4   | MONTHLY UPDATES:        | NO                   |
| 5   | MEDICAL CENTER:         | ANYCITY, DC, VAMC    |
| 6   | FUNDING YEAR - A/E:     | 1993                 |
| 7   | FUNDING YEAR - CONST:   | 1993                 |
| 8   | APPROVED A/E FUNDING:   |                      |
| 9   | APPROVED CONSTRUCTION:  |                      |
| 10  | TOTAL FUNDS APPROVED:   | 0                    |
| 11  | STATUS:                 | A/E                  |
| 12  | DESIGN METHOD:          |                      |
| 13  | CONSTR. METHOD:         |                      |
| 14  | % DESIGN PROGRAM COMPL: |                      |
| 15  | % SCHEMATICS COMPLETE:  |                      |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT PAGE 2

1.  % DESIGN DRAWINGS COMPL: 50
2.  %CONST DRAWINGS COMP:
3.  % CONSTRUCTION COMPLETE: 0
4.  DESIGN PROGRAM START (PLANNED): MAY 25, 1993
5.  DESIGN PROGRAM COMP. (PLANNED): MAY 25, 1993
6.  ADVERTISE FOR A/E (PLANNED): MAY 25, 1993
7.  SELECT A/E (PLANNED): MAY 25, 1993
8.  A/E AWARD (PLANNED): MAY 25, 1993
9.  START SCHEMATICS (PLANNED): MAY 25, 1993
10. COMPLETE SCHEMATICS (PLANNED): MAY 25, 1993
11. START DESIGN DRWGS. (PLANNED): MAY 25, 1993
12. COMPL. DESIGN DRWGS. (PLANNED): MAY 25, 1993
13. START CONST. DRWGS. (PLANNED): MAY 25, 1993
14. COMPL. CONST. DRWGS. (PLANNED): MAY 25, 1993
15. ISSUE IFB (PLANNED): MAY 25, 1993

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

|     | CONSTRUCTION PROJECT                       | PAGE 3       |
|-----|--------------------------------------------|--------------|
| 1   | BID OPEN (PLANNED):                        | MAY 25, 1993 |
| 2   | CONSTRUCTION AWARD (PLANNED): MAY 25, 1993 |              |
| 3   | CONSTRUCTION START (PLANNED): MAY 25, 1993 |              |
| 4   | CONST. COMPLETE (PLANNED):                 |              |
| 5   | ACTIVATION (PLANNED):                      |              |
| 6   | DESIGN PROGRAM START (REVISED):            |              |
| 7   | DESIGN PROGRAM COMP. (REVISED):            |              |
| 8   | ADVERTISE FOR A/E (REVISED):               |              |
| 9   | SELECT A/E (REVISED):                      |              |
| 10  | A/E AWARD (REVISED):                       |              |
| 11  | START SCHEMATICS (REVISED):                |              |
| 12  | COMPL. SCHEMATICS (REVISED):               |              |
| 13  | START DESIGN DRWGS. (REVISED):             |              |
| 14  | COMPL. DESIGN DRWGS. (REVISED):            |              |
| 15  | START CONST. DRWGS. (REVISED):             |              |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT PAGE 4

1.  COMPL. CONST. DRWGS. (REVISED):
2.  ISSUE IFB (REVISED):
3.  BID OPEN (REVISED):
4.  CONSTRUCTION AWARD (REVISED):
5.  CONSTRUCTION START (REVISED):
6.  CONST. COMPLETE (REVISED):
7.  ACTIVATION (REVISED):
8.  DESIGN PROGRAM START (ACTUAL):
9.  DESIGN PROGRAM COMPL. (ACTUAL):
10. AUTHOR. LTR. REC'D. (ACTUAL):
11. ADVERTISE FOR A/E (ACTUAL):
12. SELECT A/E (ACTUAL): MAY 24, 1993
13. A/E AWARD (ACTUAL):
14. START SCHEMATICS (ACTUAL):
15. COMPL. SCHEMATICS (ACTUAL):

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT PAGE 5

1.  START DESIGN DRWGS. (ACTUAL):
2.  COMPL. DESIGN DRWGS. (ACTUAL):
3.  START CONST. DRWGS. (ACTUAL):
4.  COMPL. CONST. DRWGS. (ACTUAL):
5.  ISSUE IFB (ACTUAL):
6.  BID OPEN (ACTUAL):
7.  CONSTRUCTION AWARD (ACTUAL):
8.  CONSTRUCTION START (ACTUAL):
9.  CONST. COMPLETE (ACTUAL):
10. ACTIVATION (ACTUAL):
11. A/E CONTRACT \#:
12. A/E NAME:
13. A/E ADDR1:
14. A/E ADDR2:
15. A/E FUND CONTROL POINT:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

|     | CONSTRUCTION PROJECT    | PAGE 6 |
|-----|-------------------------|--------|
| 1   | A/E AWARD AMOUNT:       |        |
| 2   | A/E STUDY:              |        |
| 3   | A/E SCHEMATICS:         |        |
| 4   | A/E DESIGN DEVELOPMENT: |        |
| 5   | A/E CONST DOCUMENTS:    |        |
| 6   | A/E SITE SURVEY:        |        |
| 7   | A/E CONST PER SERVCS:   |        |
| 8   | A/E OTHER SERVICES:     |        |
| 9   | A/E SA ADDITION (#):    |        |
| 10  | A/E SA ADDITIONS (\$):  |        |
| 11  | A/E SA DEDUCTIONS (#):  |        |
| 12  | A/E SA DEDUCTIONS (\$): |        |
| 13  | A/E SA NET (\$):        | 0      |
| 14  | A/E OBLIGATED:          | 0      |
| 15  | TOTAL PROJ OBLIGATION:  | 0      |

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT PAGE 7

1.  CONST. CONTRACT \#:
2.  CONTR. NAME:
3.  CONTR. ADDR1:
4.  CONTR. ADDR2:
5.  CONSTRUCTION AWARD:
6.  P&H LABOR TO DATE:
7.  P&H MATERIALS TO DATE:
8.  TOTAL P&H: 0
9.  CONST SA ADDITIONS (#):
10. CONST SA ADDITIONS (\$):
11. CONST SA DEDUCTIONS (#):
12. CONST SA DEDUCTIONS (\$):
13. CONST SUPPL (NET \$): 0
14. TOTAL CONST OBLIGATION: 0
15. TOTAL PROJ OBLIGATION: 0

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

CONSTRUCTION PROJECT PAGE 8

1.  CONST FUND CONTROL PT:
2.  TIME EXTENSION (DAYS):
3.  REMARKS: (WORD PROCESSING)
4.  PROGRESS NOTE:

CHANGE NUMBERS? (SEPARATE WITH ;) (USE : FOR RANGES)(+P -P TO PAGE)("^" QUIT) ("^^" RAPID OUT)

Requested Start Time: NOW// (MAY 26, 1993@12:00:28)

PROGRESS NOTES

The last page of the transmission contains a text field called "Progress Notes". This free-text field has a maximum of 235 characters and is transmitted as part of the 10­ 0051 in place of the Remarks field used in the screen display. After transmission, the current Progress Note is automatically filed in the Remarks field with a notation of the date it was sent to the Regional Office and VACO. The Progress Note is then cleared.

out to make ready for the next update. In this manner, each station maintains a perpetual record of every Progress Note that was ever transmitted.

This field may also be edited from any Screen Edit option.

Upon exit, the user is returned to the Project Tracking Options menu.

## Equipment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Equipment Management module has been modified to act as a front-end to the Fixed Assets Package (FAP). Fixed Assets is a subsystem of the Financial Management System (FMS), and it will become the corporate database for capitalized non- expendable (NX) equipment.

The Equipment Management module is entered from the Engineering Main Menu. The option is selected from the menu by entering the first few unique characters of the name (EQ). This option is primarily used for equipment inventory tracking and maintenance purposes. FileMan may be used to enter the data, but screen entry of data is the desired method. For illustration purposes, the first menu item, New Inventory Entry, will be displayed using both FileMan and regular screen entry.

This module has an extensive sub menu system, as shown in the Orientation section of the manual.

AUTOMATED ENGINEERING MANAGEMENT SYSTEM VERSION 7

Select Engineering Main Menu Option:?

WO Work Order & MERS ...

FYFP Five Year Facility Plan (FYFP) ... APPL Project Applications ...

TRK Project Tracking ...

EQ Equipment Management ...

ENM Program Management ...

SP Space/Facility Management ... FSA 2162 Report of Accident ...

XFER Assign (Transfer) Electronic Work Orders

Select Engineering Main Menu Option: EQ Equipment Management ENGINEERING EQUIPMENT MANAGEMENT MODULE Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports ...
6.  PM Parameters ...
7.  Generate PM Schedule ...
8.  Record Equipment PMI ...
9.  Print Bar Code Labels for Equipment Management ...
10. Bar Coded Equipment Inventory Management ...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
    1.  Turn-In/Disposition Equipment

New Inventory Entry

Add a new item to the EQUIPMENT INV. file (#6914).

Multiple Inventory Entry

Enter several like items (e.g., 50 new electric beds) into the EQUIPMENT INV. file (#6914) without having to enter common information each time.

Inventory Edit

Edit the record of an existing piece of equipment. The .01 field (ENTRY NUMBER) is assigned by the system when an item is first added to the EQUIPMENT INV. file and may not be edited.

This option gives access to both Supply and Engineering fields.

Display Equipment Record

Display selected fields from the EQUIPMENT INV. file. Repair history is not displayed via this option.

Equipment Reports

Contains options to print data from the EQUIPMENT INV. file (#6914).

PM Parameters

Contains options for enrolling devices and device types in the PMI program.

Generate PM Schedule

Contains options for printing PMI work sheets and for deletion of PM work orders.

Record Equipment PMI

Contains options to record PM inspections. This process essentially closes a PM work order and posts the activity to the equipment history.

Print Bar Code Labels for Equipment Management

Generates bar code labels (location labels and equipment labels) for equipment management applications. Designed for use with a dedicated bar code printer.

Bar Coded Equipment Inventory Management

Driver for NX inventory functions.

Purchase Order Group Edit

Edit a group of existing items in the inventory file without having to enter common data for each item. Equipment is initially selected by purchase order \#. Therefore, the purchase order \# field must already be populated before this option can be used to edit equipment. Equipment with the same purchase order \# is selected for editing based on the equipment category, manufacturer, and model fields.

Lockout/Tagout Enter/Edit

Allows users to specify that equipment records (File \#6914) and/or equipment categories (File \#6911) are subject to lockout/tagout requirements. Lockout/tagout stipulates that the affected equipment must be rendered inoperative (usually by opening and tagging a circuit breaker) before the equipment is serviced.

The intent is to protect maintenance personnel.

Turn-In/Disposition Equipment

This option can be used to quickly update equipment records for the turn-in or final disposition of equipment not reported to Fixed Assets.

If you attempt to apply this option to an item that has been reported to Fixed Assets, the system will tell you that it can't proceed and will instruct you to initiate an FD document from within the FAP system.

### New Inventory Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Screen Entry (or Screen Handler)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

Select Equipment Management Option: 1 New Inventory Entry Screen entry? YES// ??

Enter 'Y' for screen handler, 'N' for standard FileMan. Screen entry? YES// YES

Enter a new equipment inventory item? NO// YES

Please enter SERIAL \# if available. Otherwise press \<return\>. SERIAL \#:??

Serial number. Assigned by manufacturer. Should be unique within model.

and manufacturer. Use numbers, upper case letters, punctuation, and spaces as needed.

SERIAL \#: \<RET\>

...Setting up new equipment record.

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 3%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Equipment Display (screen 1 of 3)</th>
<th></th>
<th>06/16/97</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 ENTRY #(R): 83</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><p>MANUFACTURER: ENMFGR, F IVE</p></li>
<li><p>MODEL: GJ2194</p></li>
</ol></td>
<td>4</td>
<td>SN: Q010D7164</td>
</tr>
<tr class="odd">
<td>5 CSN: ..................</td>
<td>6</td>
<td>LIFE EXPECTANCY: 10</td>
</tr>
</tbody>
</table>

7 MFGR EQPT NAME: ULTRAVIOLET LAMP

8 CMR: 280 9 CATEGORY: .........................

10 P.O. NO.: A9633 11 ACQ. METHOD: PURCHASED 12 VENDOR: ....................................

13 LEASE COST: ....... 14 ASSET VALUE: 324.48

15 ACQ. DATE: FEB 1980 16 WARRANTY EXP. DATE: FEB 1981

17 REPLACEMENT DATE: FEB 1993 18 SOURCE: 2

19 TYPE: NON-EXPENDABLE EQPT 20 REPLACING: ....................

Equipment Display (screen 2 of 3) 06/16/97

\*\*\*ENTRY NUMBER:83\*\*\*

1 USE STATUS: IN USE 2 PARENT SYSTEM: ..........

3 SERVICE: ....................4 NXRN: 16389

| 5 LOCATION: GE26-01-JB          | 6 LAST INVENTORIED: ...........     |
|---------------------------------|-------------------------------------|
| 7 VA PM NUMBER: 6530-5531       | 8 LOCAL IDENTIFIER: ............... |
| 9 SERVICE CONTRACT: ...         | 10 CONTRACT COST: .........         |
| 11 JCAHO: YES                   | 12 RUC: ........................    |
| 13 TURN-IN DATE: ............   | 14 FINAL DISP DATE: ............    |
| 15 DISP METHOD: ............... |                                     |

16 ORIG. VALUE(R): ............17 DISP VALUE: ............

18 COMMENTS(W): ... 19 SPEX(W): ...

20 LOCKOUT REQUIRED? (R): ... 21 CONDITION CODE: ........

22 OWNING STATION NUMBER: .....

Equipment Display (screen 3 of 3) 06/16/97

\*\*\*ENTRY NUMBER:83\*\*\*

1 CONTROLLED ITEM?: ... 2 CAPITALIZED?: NO

3 FUND: ...... 4 FCP: ..............................

5 BOC: ....

6 SGL ACCOUNT: 6100 7 A/O: ....

8 EQUITY ACCOUNT: ....................

You can enter ^C (case sensitive) at any field to see the command menu display for the screen editor.

COMMANDS

^ -- Quit @ -- Delete data

^nn -- Go to the 'nn' statement CR -- Go to the next statement

^C -- Command menu display \< -- Go to previous statement

^N -- New Record ?? -- For more information about field

-- Space bar, recall previous answer? -- Information about field

^D -- Down page ^U -- Up page

If security key ENEDPM is held, then PM parameters can be edited as follows:

Would you like to include this item in the PM program? YES// \<RET\>

There is no EQUIPMENT CATEGORY on file for this item. Would you like to enter one now? Yes// \<RET\> (Yes)

EQUIPMENT CATEGORY: ?

Category of device (ex: DEFIBRILLATOR, AIR CONDITIONER, etc.) to which this piece of equipment belongs. Useful in establishing and maintaining preventive maintenance schedules.

EQUIPMENT CATEGORY: \<RET\>

Select RESPONSIBLE SHOP: ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.

Select RESPONSIBLE SHOP: \<RET\>

If the Software option "ASK INCOMING INSPECTION Work Order" is set, a work order can be created during entry of new equipment.

Create an Incoming Inspection Work Order? YES// ??

Enter either 'Y' or 'N'.

Create an Incoming Inspection Work Order? YES// \<RET\>

Select ENGINEERING SECTION LIST: INSPECTION// ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.

Select ENGINEERING SECTION LIST: INSPECTION// \<RET\>

WORK ORDER \#: IN970224-001 PRIMARY TECH ASSIGNED: ??

Select current employees only.

Answer with ENG EMPLOYEE NAME Choose from:

ENUSER, TWO ENUSER , THREE ENUSER , FOUR

PRIMARY TECH ASSIGNED: \<RET\>

CONTACT PERSON: ENUSER, ONE// \<RET\>

PHONE: \<RET\>

COMMENTS:

1\> \<RET\>

Print this work order? YES// \<RET\>

Select output device: \<RET\>

RETURN DISPLAY

DEVICE: HOME// Eng Printer RIGHT MARGIN: 80// \<RET\>

WORK ORDER \# IN970224-001

1\) PRIMARY EMPL: 2) REQ DATE: FEB 24,1997@12:16

3\) REQ MODE: COMPUTER 4) LOCATION:

5\) BED \#: 6) STATUS: IN PROGRESS

7)  TASK DESC: Incoming Inspection
8)  CONTACT: ENUSER, SEVEN 9) PHONE:

10\) ENTERED BY: ENUSER, SEVEN 11) SHOP: INSPECTION

12\) DATE ASSIGNED: 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 75 15) LOCAL ID:

16\) EQUIP CAT: 17) CONDITION:

18) MFGR:
19) MODEL: 20) SERIAL \#:

21\) OWNER/DEPT: 22) PM \#:

23\) PARTS ORDER: 24) WORK ACTION: I1

25) WORK CTR:
26) TOTAL HOURS: 27) TOTAL MATERIAL COST:

28\) TOTAL LABOR COST: 29) VENDOR SERVICE COST:

30\) \*ASSIGNED TECH\* 31) DATE COMPLETE:

32) WORK PERFORMED:
33) COMMENTS:

Press \<RETURN\> to continue, '^' to escape...

Enter a new equipment inventory item? NO// \<RET\>

If security key ENFACS is held, then an FA Document can be generated for capitalized NX equipment as follows:

You have just entered an Equipment Record that is both NONEXPENDABLE and CAPITALIZED. Do you wish to send an FA document to Austin? YES// \<RET\>

Enter a new equipment inventory item? No// \<RET\> (No)

#### FileMan Entry

The following dialogue shows the FileMan entry with explanations of each field.

\`Select Equipment Management Option: 1 New Inventory Entry Screen entry? YES// NO

Enter a new equipment inventory item? NO// YES

Please enter SERIAL \# if available. Otherwise press \<return\>. SERIAL \#:??

Serial number. Assigned by manufacturer. Should be unique within model.

and manufacturer. Use numbers, upper case letters, punctuation, and spaces as needed.

SERIAL \#: \<RET\>

...Setting up new equipment record.

MANUFACTURER: ?

Firm that actually manufactured this equipment, not necessarily the company from which it was purchased.

Answer with MANUFACTURER LIST FILE MFGID, or MFG/DIV, or PSEUDONYM

MANUFACTURER: \<RET\>

MODEL:??

Model number or designation, normally assigned by manufacturer. Spaces and punctuation may be included.

MODEL: \<RET\>

SERIAL \#:??

Serial number. Assigned by manufacturer. Should be unique within model and manufacturer. Use numbers, upper case letters, punctuation, and spaces as needed.

SERIAL \#: \<RET\>

CATEGORY STOCK NUMBER: ?

If a category stock number was entered, then the life expectancy will be extracted from the Category Stock number file.

Pointer to Category Stock Number File. This file was introduced to VISTA with Version 6.5 of the Engineering Package and is maintained by Acquisition and Materiel Management (Cataloging).

Answer with CATEGORY STOCK NUMBER NAME, or BRIEF DESCRIPTION

CATEGORY STOCK NUMBER: \<RET\>

LIFE EXPECTANCY: ??

Number of years for which this device is expected to provide useful and economical service. Generally determined by Supply Service on the basis of cumulative experience.

LIFE EXPECTANCY: \<RET\>

MFGR. EQUIPMENT NAME: ??

Brief narrative description of item. For NX (non-expendable) equipment, this data element can be triggered in from the Category Stock Number file if your site chooses to do so.

MFGR. EQUIPMENT NAME: \<RET\>

CMR:?

Consolidated Memorandum of Receipt. The basic instrument by which accountability for capital equipment is established.

Answer with CMR NAME, or SERVICE, or RESPONSIBLE OFFICIAL

CMR: \<RET\>

EQUIPMENT CATEGORY: ?

Category of device (ex: DEFIBRILLATOR, AIR CONDITIONER, etc.) to which this piece of equipment belongs. Useful in establishing and maintaining preventive maintenance schedules.

Answer with EQUIPMENT CATEGORY NAME, or SYNONYM

EQUIPMENT CATEGORY: \<RET\>

PURCHASE ORDER \#: ??

If this Purchase Order can be found in IFCAP, the system will automatically attempt to extract SERVICE, FUND CONTROL POINT, VENDOR, SOURCE, BUDGET OBJECT CODE, STANDARD GENERAL LEDGER, FUND, ADMINISTRATIVE/OFFICE, and EQUITY ACCOUNT from IFCAP. This IFCAP data is then stuffed into the equipment record, but only if the equipment record does not already contain this information. Data from IFCAP does not overwrite data already stored in the Equipment Inv. file.

VA Purchase Order number. May be assigned by the facility or perhaps by

a centralized purchasing unit of the Office of Acquisitions and Material Management.

PURCHASE ORDER \#: \<RET\>

VENDOR POINTER: ?

Vendor from whom unit was actually purchased.

VENDOR POINTER: \<RET\>

ACQUISITION METHOD: ??

Set of codes which establishes whether or not the facility legally owns the equipment.

Choose from:

CHOOSE FROM:

'C' FOR CONSTRUCTED

'G' FOR GIFT/BEQUEST/DONATION 'L' FOR LEASED

'M' FOR LEASED/PURCHASED 'O' FOR OTHER

'P' FOR PURCHASED 'R' FOR TRANSFERRED 'T' FOR TRADED

'X' FOR EXCESS

'1' FOR ON LOAN TO VAMC ACQUISITION METHOD: \<RET\>

TOTAL ASSET VALUE: ??

Cost of this equipment at the time of purchase. This field is likely to become the basis for estimating depreciated value and replacement cost.

TOTAL ASSET VALUE: \<RET\>

ACQUISITION DATE: ?

Date of acceptance of this equipment by the agency. Month and year are generally sufficient.

ACQUISITION DATE: \<RET\>

WARRANTY EXP. DATE: ??

Date on which repairs to this item become the sole responsibility of the government. Generally stipulated in the contract or sales agreement.

WARRANTY EXP. DATE: \<RET\>

REPLACEMENT DATE: ??

Date on which this equipment is scheduled for replacement. Month and year are sufficient. When equipment is entered, this field should be the ACQUISITION DATE plus the LIFE EXPECTANCY. As scheduled REPLACEMENT DATE

is approached, however, it may be necessary to revise it. Such revisions do not always alter the official LIFE EXPECTANCY.

REPLACEMENT DATE: \<RET\>

ACQUISITION SOURCE: ??

Source of acquisition for this piece of equipment.

Choose from:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><p>0</p>
<p>1</p>
<p>2</p>
<p>3</p>
<p>4</p></th>
<th><p>Defense Supply Agency</p>
<p>VA Servicing Supply Depot Open Market</p>
<p>GSA Supply Depot</p>
<p>VA Decentralized Schedule</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td>Federal Prison Industries</td>
</tr>
<tr class="even">
<td><p>6</p>
<p>7</p></td>
<td><p>Fed. Supply Sched. or OGA Contracts</p>
<p>Consolidated Procurement</p></td>
</tr>
<tr class="odd">
<td><p>9</p>
<p>B</p></td>
<td><p>Marketing Center</p>
<p>Combination of 2,4,6</p></td>
</tr>
</tbody>
</table>

Answer with SOURCE CODE, or ABBREVIATION

ACQUISITION SOURCE: \<RET\>

TYPE OF ENTRY: ??

Discriminates between entries for which a CMR Official is legally responsible and those that are accounted for in other ways.

Choose from:

NX NON-EXPENDABLE EQPT

BSE BUILDING SERVICE EQPT

EXP EXPENDABLE EQPT TYPE OF ENTRY: \<RET\>

REPLACING (ENTRY NUMBER): ??

If this item was acquired as REPLACEMENT EQUIPMENT, then the old ENTRY NUMBER of the item which it replaced should appear in this field.

REPLACING (ENTRY NUMBER): \<RET\>

USE STATUS: ??

Tells the user whether or not the equipment is currently in active use.

Choose from:

| 1           | IN USE         |
|-------------|----------------|
| 2           | OUT OF SERVICE |
| 3           | LOANED OUT     |
| 4           | TURNED IN      |
| 5           | LOST OR STOLEN |
| USE STATUS: | \<RET\>        |

PARENT SYSTEM: ?

If Item A is a component of Item B, then the PARENT field of Item A should contain the CONTROL NUMBER of Item B. If Item B is, in turn,

a component of an even larger Item C; then the PARENT field of Item B should contain the CONTROL NUMBER of Item C, and so on.

Inventory items with no entry in the PARENT field are either free standing devices or major systems with one or more levels of components beneath them.

An item must already be in the EQUIPMENT file before it can be named as the PARENT of another item.

SERVICE POINTER: ?

The functional entity (generally a service) within the facility that uses the device. SERVICE POINTER: \<RET\>

LOCATION:?

Physical location of this item at the facility.

Enter as ROOM-BUILDING or select a SYNONYM.

LOCATION: \<RET\>

VA PM NUMBER: ??

Property management number. Assigned by Supply Service upon receipt of new equipment. Should be unique within the facility. First four digits correspond to the Federal Supply Classification number.

VA PM NUMBER: \<RET\>

LOCAL IDENTIFIER: ??

An optional identifier that has meaning to the facility. Most sites prefer to make these identifiers unique.

LOCAL IDENTIFIER: \<RET\>

SERVICE CONTRACT: ??

YES indicates that device in question is under a service contract with an entity outside the medical center. A more comprehensive module for service contracts is being developed jointly by AEMS/MERS and IFCAP and will appear in a future release.

Choose from:

Y YES

N NO

SERVICE CONTRACT: \<RET\>

JCAHO:??

New Joint Commission standards for accreditation of health care facilities require (in part) that a "separable inventory" of equipment be maintained. This flag should be set to 'YES' for items subject to review by Joint Commission surveyors.

Choose from:

Y YES

N NO

JCAHO: \<RET\>

REPLACEMENT UPDATE CODE: ??

Replacement information needed by A&MM. Choose from:

| 4   | NOT TO BE REPLACED                      |
|-----|-----------------------------------------|
| 5   | TO BE REPLACED UNDER ACTIVATION PROJECT |
| 6   | ON ORDER                                |

REPLACEMENT UPDATE CODE: \<RET\>

STATION NUMBER: ??

Station number of the facility that owns this equipment. If this equipment is owned by a national cemetery that is serviced by a VAMC, then the station number of the cemetery should appear in this field.

STATION NUMBER: \<RET\>

CONTROLLED ITEM?: ??

Prior approval of VACO is required. Choose from:

1.  NO
2.  YES

CONTROLLED ITEM?: \<RET\>

CAPITALIZED?: ??

Reserved for future use.

Choose from:

1.  NO
2.  YES

CAPITALIZED?: \<RET\>

FUND CONTROL POINT: ??

Fund Control Point from which item was originally procured. If unknown, leave blank.

FUND CONTROL POINT: \<RET\>

BUDGET OBJECT CODE: ??

An accounting classification.

Choose from:

| 3105 | TRUST EQUIPMENT                              |
|------|----------------------------------------------|
| 3109 | INVALID LIFTS, OTHER DEVICES & EQUIPMENT     |
| 3110 | TRANSPORTATION EQUIPMENT, PASSENGER VEHICLES |
| 3112 | TRANSPORTATION EQUIP, NONPASSENGER VEHICLES  |
| 3120 | NONEXPENDIBLE FURNITURE & FIXTURES           |
| 3121 | OFFICE EQUIPMENT                             |
| 3122 | OFFICE AUTOMATION/WORD PROCESSING, PURCHASED |
| 3123 | ADP EQUIPMENT                                |
| 3124 | ADP SOFTWARE                                 |
| 3125 | TELECOMMUNICATIONS EQUIPMENT                 |
| 3130 | MEDICAL, DENTAL & SCIENTIFIC EQUIPMENT       |
| 3150 | UTILITY & OPERATING EQUIPMENT                |
| 3160 | EQUIPMENT UNDER CAPITAL LEASE                |

BUDGET OBJECT CODE:

STANDARD GENERAL LEDGER: ??

In accordance with the VA administrative accounting system. Only a limited number of Standard General Ledger Accounts are appropriate for use with non-expendable equipment.

Choose from:

| 1756 |     | INVALID LIFTS, OTHER DEVICES      |
|------|-----|-----------------------------------|
| 1811 |     | EQUIPMENT UNDER CAPITAL LEASE     |
| 1830 |     | ADP SOFTWARE                      |
| 6100 |     | EXPENSED NX EQUIPMENT (ALL TYPES) |

STANDARD GENERAL LEDGER: \<RET\>

FUND:??

The Fund Code (from the Treasury Symbol) under which this equipment was procured.

Choose from:

4014 Canteen Service

4048 Compensated Work Therapy

4138 Medical Facilities Revolving Fund

Answer with NX FUND NX FUND CODE, or BRIEF DESCRIPTION

ADMINISTRATION/OFFICE: ??

An accounting classification.

| Choose | from: |                                            |
|--------|-------|--------------------------------------------|
| 10     |       | Veterans’ Health Administration            |
| 20     |       | Veterans Benefits Administration           |
| 40     |       | National Cemetery Service                  |
| 90     |       | Office of Acquisition & Materiel Mgmnt     |
| 04     |       | Office of Finance and Info Resources Mgmnt |
| 08     |       | Office of Facilities                       |

ADMINISTRATION/OFFICE: \<RET\>

EQUITY ACCOUNT: ??

An accounting classification used primarily in cost distribution reports. Choose from:

3299 MEDICAL

3210 NON-MEDICAL

3402 DONATED EQUITY ACCOUNT: \<RET\>

COMMENTS:

1\> \<RET\>

EDIT Option: \<RET\>

SPEX:

1\> \<RET\>

If security key ENEDPM is held, then PM parameters can be edited as follows.

Would you like to include this item in the PM program? YES// \<RET\>

There is no EQUIPMENT CATEGORY on file for this item. Would you like to enter one now? Yes// \<RET\> (Yes)

Would you like to include this item in the PM program? YES// \<RET\>

Equipment Category is DEFIBRILLATOR

Would you like to see the standard PM schedule for this Equipment Category? Yes// \<RET\> (Yes)

Example:

Equipment Category: DEFIBRILLATOR

Should this item be given the standard PM schedule for devices of category DEFIBRILLATOR? Yes// \<RET\> (Yes)

If the Software option "ASK INCOMING INSPECTION Work Order" is set, a work order can be created during entry of new equipment.

Create an Incoming Inspection Work Order? YES// \<RET\> Select ENGINEERING SECTION LIST: INSPECTION// \<RET\> WORK ORDER \#: \<RET\> IN970304-002

PRIMARY TECH ASSIGNED: \<RET\> CONTACT PERSON: ENTECH, ONE// \<RET\> PHONE: \<RET\>

COMMENTS:

1\> \<RET\>

Print this work order? YES// \<RET\>

| Select output device: |         |         | \<RET\>    |                    |         |
|-----------------------|---------|---------|------------|--------------------|---------|
| RETURN                | DISPLAY |         |            |                    |         |
| DEVICE: HOME//        |         | \<RET\> | UCX/TELNET | RIGHT MARGIN: 80// | \<RET\> |

WORK ORDER \# IN970304-002

1\) PRIMARY EMPL: 2) REQ DATE: MAR 4,1997@12:07

3\) REQ MODE: COMPUTER 4) LOCATION:

5\) BED \#: 6) STATUS: IN PROGRESS

7)  TASK DESC: Incoming Inspection
8)  CONTACT: ENUSER, SEVEN 9) PHONE:

10\) ENTERED BY: ENUSER, SEVEN 11) SHOP: INSPECTION

12\) DATE ASSIGNED: 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 83 15) LOCAL ID:

16\) EQUIP CAT: DEFIBRILLATOR 17) CONDITION:

18) MFGR:
19) MODEL: 20) SERIAL \#:

21\) OWNER/DEPT: 22) PM \#:

23\) PARTS ORDER: 24) WORK ACTION: I1

25) WORK CTR:
26) TOTAL HOURS: 27) TOTAL MATERIAL COST:

28\) TOTAL LABOR COST: 29) VENDOR SERVICE COST:

30\) \*ASSIGNED TECH\* 31) DATE COMPLETE:

32) WORK PERFORMED:
33) COMMENTS:

Enter a new equipment inventory item? NO//

If security key ENFACS is held, then an FA Document can be generated for capitalized NX equipment. Once an entry in the Equipment Inv. file has been established in the Fixed Assets system, data fields which are of interest to Fixed Assets cannot be edited using the standard equipment edit options. Instead an FAP Document must be used to update these fields. The FAP Document will update both the Equipment Inv. file and the Fixed Assets system. The dialogue for generating the FA Document follows.

You have just entered an Equipment Record that is both NONEXPENDABLE and CAPITALIZED. Do you wish to send an FA document to Austin? YES// \<RET\>

Enter a new equipment inventory item? No// \<RET\>

FAP Documents are discussed in the Nonexpendable Equipment Module section of this chapter.

### Multiple Inventory Entry.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter multiple inventory entries of a particular item type.

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

Select Equipment Management Option: 2 Multiple Inventory Entry Enter multiple equipment inventory items? NO// ??

This option allows a rapid entry of multiple items which are alike, e.g. 25 new electric beds.

Enter YES or NO

Enter multiple equipment inventory items? NO// YES

Screen entry? YES// ??

Enter 'Y' for screen handler, 'N' for standard FileMan. Proceed by entering the first item in full.

Enter Return to continue or “^” to quit.

Next, the opportunity is given to enter information about the remaining items.

For each additional equipment entry, enter:

SERIAL \#, LOCATION, VA PM NUMBER, and LOCAL IDENTIFIER (if any).

Enter another item? YES// ??

Enter YES to add another similar equipment item. Enter another item? YES// \<RET\>

...Setting up new equipment record.

> **NOTE:** If your original entry had a PARENT SYSTEM, you will be prompted for PARENT SYSTEM here. Likewise, if your original entry was replacement equipment, you will also be prompted for REPLACING (ENTRY NUMBER). If an incoming inspection work order was created for the first entry then the system will automatically create incoming inspection work orders for the subsequent entries.

Equipment ID: 97 SERIAL \#: \<RET\> LOCATION:??

Physical location of this item at the facility.

Choose from:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">100-110-JC</th>
<th>110</th>
<th>CCU</th>
<th>MEDICINE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2" rowspan="2"><p>101-148</p>
<p>102-148</p>
<p>103-110-JC</p></td>
<td rowspan="2"><p>148</p>
<p>148</p>
<p>110</p></td>
<td><p>C</p>
<p>C</p></td>
<td rowspan="2"><p>EXAM/TREATMENT ROOM</p>
<p>EXAM/TREATMENT ROOM MEDICINE</p></td>
</tr>
<tr class="even">
<td>CCU</td>
</tr>
<tr class="odd">
<td>LOCATION:</td>
<td colspan="2">&lt;RET&gt;</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">VA PM NUMBER:</td>
<td>??</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Property management number. Assigned by Supply Service upon receipt of new equipment. Should be unique within the facility. First four digits correspond to the Federal Supply Classification number.

VA PM NUMBER: \<RET\>

LOCAL IDENTIFIER: ??

An optional identifier that has meaning to the facility. Most sites prefer to make these identifiers unique.

LOCAL IDENTIFIER: \<RET\>

Enter another item? YES// N (NO)

### Inventory Edit.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit previously entered equipment data. When selected, the system presents an editable screen display of the data.

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports ...
6.  PM Parameters ...
7.  Generate PM Schedule ...
8.  Record Equipment PMI ...
9.  Print Bar Code Labels for Equipment Management ...
10. Bar Coded Equipment Inventory Management ...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
13. Turn-In/Disposition Equipment

Select Equipment Management Option: 3 Inventory Edit Select EQUIPMENT ENTRY \#: 83

Select EQUIPMENT ENTRY \#: ??

'EC.value' =\> equipment whose EQUIP. CATEGORY starts with 'value' 'LI.value' =\> equipment whose LOCAL ID starts with 'value' 'LO.value' =\> equipment whose LOCATION starts with 'value' 'MA.value' =\> equipment whose MANUFACTURER starts with 'value' 'MF.value' =\> equipment whose MFGR. EQUIP. NAME starts with 'value' 'MO.value' =\> equipment whose MODEL starts with 'value'

'SN.value' =\> equipment whose SERIAL NUMBER starts with 'value' Choose from:

'^' TO STOP: ^

Equipment is cross-referenced by the various fields referred to above, which are used in selecting the desired Equipment Inventory.

Select EQUIPMENT ENTRY \#: 83

Inventory Edit uses the same screen presentation and fields as seen in the New Inventory Entry. The editing of PM parameters is still controlled by the ENEDPM security key.

The symbol "R" after a field indicates that the user may not change its value.

The following message is displayed if you attempt to make an inappropriate change to the CMR field while there are active IT assignments for the equipment item you selected.

Equipment has an active IT assignment.

New CMR must be excess (99x) or have IT TRACKING = YES. Press \<RETURN\> to continue...

> **NOTE:** Users who do not hold the ENEDNX security key will not be allowed to edit the CATEGORY STOCK NUMBER, COST, ACQUISITION METHOD, or CMR

data for equipment records whose TYPE is "NX". These users will not have access to the third screen.

### Display Equipment Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the display and entry/edit of previously entered records. It is not possible to edit equipment records using this option. Records are displayed using the same screens as New Inventory Entry.

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports...
6.  PM Parameters...
7.  Generate PM Schedule...
8.  Record Equipment PMI...
9.  Print Bar Code Labels for Equipment Management...
10. Bar Coded Equipment Inventory Management...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
13. Turn-In/Disposition Equipment

This option allows the display and entry/edit of previously entered records. It is not possible to edit equipment records using this option. Records are displayed using the same screens as New Inventory Entry.

#### Equipment Reports

Equipment Reports contains options to print data from the Equipment Inv. file. As the reports can be quite lengthy, it is recommended that the options be run during off-peak hours.

1.  New Inventory Entry
151. Multiple Inventory Entry
152. Inventory Edit
153. Display Equipment Record
154. Equipment Reports ...
155. PM Parameters ...
156. Generate PM Schedule ...
157. Record Equipment PMI ...
158. Print Bar Code Labels for Equipment Management ...
159. Bar Coded Equipment Inventory Management ...
160. Purchase Order Group Edit
161. Lockout/Tagout Enter/Edit
162. Turn-In/Disposition Equipment

Select Equipment Management Option: 5 Equipment Reports The following reports are available:

1.  Specific Equipment History

    Print-out of repair history of a specific entry in Equipment Inv. file.
163. Equipment Category History

     A synopsis of the maintenance costs for a given Equipment Category.
164. Inventory Listing.

     Contains options to print data from the Equipment Inv. file.
165. Warranty List

     Prints all devices whose warranties are scheduled to expire within a user specified time interval.
166. Replacement Listing

     Prints all entries in the Equipment Inv. file scheduled for replacement within a user specified time interval.
167. Failure Rate Report

     Prints a synopsis of the repair history of user specified Equipment Categories.
168. PM Workload Analysis

     Prints a breakdown of scheduled PMI hours by month for a given shop. Intended as a tool in balancing PM workload.
169. Direct Posting to Equipment Histories

     A utility for posting activities to Equipment Histories without going through the Work Order module.
170. Parent System/Component Hierarchy Report

     Prints a hierarchical list of a parent system and all of its components. Components are indented and listed beneath their parent system. Items that are components of a component in the specified system are included.
171. Lockout/Tagout Flag Reports

     Reports of Lockout/Tagout flags set by Equipment Record (file \#6914) and/or Equipment Category file (#6911).

#### Specific Equipment History

| Select Equipment Reports Option:     |         |            | Specific Equipment History |         |
|--------------------------------------|---------|------------|--------------------------------|---------|
| Select EQUIPMENT ENTRY \#:           |         | 79         |                                |         |
| Select output device: RETURN DISPLAY |         |            |                                |         |
| DEVICE: HOME//                       | \<RET\> | UCX/TELNET | RIGHT MARGIN: 80//             | \<RET\> |

REPAIR HISTORY: 79 MAR 26,1997 Pg 1

Acq Date: Acq Value: \$ LE: SN:

Criticality: Condition:

REFERENCE WORK ORDER PM HRS LABOR\$ MAT'L\$ VENDOR\$ TOTAL\$ WORKER

--- -

970326-P2 OC970326-001 40.0 740 300 200 1240 ENUSER1, ONE

FIX BROKEN PART

\_\_\_\_

TOTAL 40.0 740 300 200 1240

> **NOTE:** It is also possible to extract a type of Equipment History from the Work Order module (option ENEQHID). There are two differences.

1.  PM work orders that have been deleted will appear on Equipment module histories (above) but not on histories from the Work Order module.
2.  Incomplete work orders will appear on histories from the Work Order module but not on histories from the Equipment module (above).

#### Equipment Category History

This option prints a synopsis of the maintenance costs for a given Equipment Category.

Select Equipment Reports Option: 2 Equipment Category History Select EQUIPMENT CATEGORY NAME: ??

Choose from:

AIR CONDITIONER (THRU WALL) AMPLIFIER & SIGNAL CONDITIONER ANALYZER

ANALYZER-ANESTHESIA ANALYZER-BACTERIAL ANALYZER-BLOOD

^

Select EQUIPMENT CATEGORY NAME: BED-ELECTRIC

Include TURNED IN and LOST OR STOLEN Equipment? YES// ??

Enter YES to include equipment with a USE STATUS of TURNED IN or LOST OR STOLEN when repair statistics are computed. If included, the age of this equipment will be determined by comparing the Turn-In (or Disposition) Date with the Acquisition Date.

Enter YES or NO.

Include TURNED IN and LOST OR STOLEN Equipment? YES// \<RET\>

Select output device: \<RET\>

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

| compiling the data............      |        |      |       |      |        |        |       |         |
|-------------------------------------|--------|------|-------|------|--------|--------|-------|---------|
| BED-ELECTRIC Equipment Type History |        |      |       |      |        |        | MAR   | 26,1997 |
| Equipment Type: BED-ELECTRIC        |        |      |       |      |        |        |       |         |
| Number of Units: 9                  |        |      |       |      |        |        |       |         |
| Average Age: 0.73 Years             |        |      |       |      |        |        |       |         |
| EQUIPMENT COSTS LABOR MATERIAL      |        |      |       |      |        | VENDOR | TOTAL | HOURS   |
| PER ITEM 4.33 0.00                  |        |      |       |      |        | 0.00   | 4.33  | 0.27    |
| PER YEAR 53.09 0.00                 |        |      |       |      |        | 0.00   | 53.09 | 3.27    |
| PER ITEM                            | PER    | YEAR | 5.90  | 0.00 |        | 0.00   | 5.90  | 0.36    |
| TOTAL                               |        |      | 38.95 | 0.00 |        | 0.00   | 38.95 | 2.40    |
| VISITS                              | REPAIR |      |       | PMI  | VENDOR | OTHER  | TOTAL |         |
| PER ITEM                            | 0.0    |      |       | 0.3  | 0.0    | 0.0    | 0.3   |         |
| PER YEAR                            |        |      | 0.0   | 4.1  | 0.0    | 0.0    | 4.1   |         |
| PER ITEM                            | PER    | YEAR | 0.0   | 0.5  | 0.0    | 0.0    | 0.5   |         |
| TOTAL                               |        |      | 0.0   | 3.0  | 0.0    | 0.0    | 3.0   |         |

#### Inventory Listing

The Inventory Listing option has a separate sub menu containing seven options for the generation of a report by CMR, Equipment Category, device location, using service, responsible shop, or use status. The CMR Inventory option uses sort template ENCMR and print template ENCMR to produce an official CMR (Consolidated Memorandum of Receipt) document. This document is to be signed by the official responsible for the CMR each time a physical inventory is taken.

CMR (Consolidated Memorandum of Receipt) reports are normally sorted by CMR and then by category stock number within CMR.

Patch EN\*7\*19 modified the CMR Report and introduced a new report called Nonexpendable Expensed Inventory. The CMR report only includes equipment that is capitalized or whose category stock number (CSN) begins with 10 (Firearms), 23 (Motor Vehicles), or 70 (ADP). The Nonexpendable Expensed Inventory report includes equipment that is not included on the CMR report.

Inventory Listing Version 7.0

| 1   | CMR Inventory                    |
|-----|----------------------------------|
| 2   | Equipment Category Inventory     |
| 3   | Location Inventory               |
| 4   | Using Service Inventory          |
| 5   | Responsible Shop Inventory       |
| 6   | Use Status Inventory             |
| 7   | Nonexpendable Expensed Inventory |

CMR Inventory (EIL)

This option generates the Equipment Inventory Listing (EIL) report. Equipment that is belongs to the user specified CMR and is either capitalized or whose category stock number beings with 10 (firearms), 23 (motor vehicles) or 70 (ADP) is printed on this report. A page suitable

for the signature of the Responsible Official is printed when the output is directed to a printer.

See the Nonexpendable Expensed Inventory report to print equipment that belongs to a CMR but does not meet the other criteria for inclusion on the Equipment Inventory Listing report.

Equipment Category Inventory

Inventory listing by device type (cf: File 6911).

Location Inventory

Inventory listing by device location.

Using Service Inventory

Inventory listing by using service. Note that the using service is not necessarily the owning service (ex: a VCR may be used in

Dental but owned by Medical Media Production). Owning service is established via the CMR.

Responsible Shop Inventory

Inventory listing by responsible shop.

Use Status Inventory

Inventory listing by use status.

Nonexpendable Expensed Inventory

This option generates the Nonexpendable Expensed Inventory report. Equipment that is belongs to the user specified CMR and is not capitalized and whose category stock number does not be with 10 (firearms), 23 (motor vehicles) or 70 (ADP) is printed on this report.

See the CMR Inventory (EIL) report to print accountable equipment that belongs to a CMR.

#### Inventory Listing Option 1. CMR Inventory

Select Inventory Listing Option: 1 CMR Inventory (EIL) Start WITH: 112??

Start WITH:?

Answer with CMR NAME, or SERVICE, or RESPONSIBLE OFFICIAL, or ALTERNATE RESPONSIBLE OFFICIAL

Do you want the entire 72-Entry CMR List? N (No) Start WITH: 160 LABORATORY

Go TO: 160

Should the COMMENTS field be printed? NO// y YES DEVICE: HOME// ENG PRINTER RIGHT MARGIN: 80//

EQUIPMENT INVENTORY LISTING (EIL) JUL 10,1997 08:04 PAGE 1 FOR EIL: 160 LABORATORY SERVICE

ENTRY \# STN FUND SGL LEASE COST ASSET VALUE LAST INVENTORIED

­

CATEGORY STOCK NUMBER: 6515-285575 (DEFIBRILLATOR CARDIAC) DEFIBRILLATOR, CARDIAC. AN APPARATUS USED TO COUNTERACT FIBRILLATION BY APPLICATION OF ELECTRIC IMPULSES TO THE HEART.

1 AMAF 1750 7200.00

MFGR NAME: ENMFGR, S IX

MANF: HEWLETT PACKARD/MEDICAL PROD

MODEL: 8700 SERIAL: 8978899

VA PM \#: 7530-4565 LOCAL ID:

USE STATUS: IN USE USING SVC: INFORMATION SYSTEMS CENTER

LOCATION: 201-110 PREVIOUS:

CONDITION: ACQ METH: PURCHASED

ACQ DATE: JUN 4,1986 LE: 8 REPL DATE: JUN 4,1994 COMMENTS:

SPEX:

CATEGORY STOCK NUMBER: 7025-386116 (KEYBOARD AUX COMP SYS)

KEYBOARD, AUXILIARY, COMPUTER SYSTEM. AN AUXILIARY KEYBOARD, DIRECTLY CONNECTED TO THE COMPUTER BY CABLES ORTRANSMISSION LINES, ENABLING DIRECT ENTRY OF INFORMATION. ITEM MAY BE USED FOR VALIDATION PURPOSES, DIRECT ACCESS TO MEMORY FILES, AND TIME-SHARING SYSTEMS THAT REQUIRE SEVERAL TYPES OF INTERMIXED DATA FORMATS TO BEPROCESSED IN REAL-TIME MODE.

154

MFGR NAME: ENMFGR, SEVEN

MANF: ENMFGR, E IGHT

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 32%" />
<col style="width: 43%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>MODEL: 4200</p>
<p>.</p></th>
<th colspan="2">SERIAL: 12345678</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">.</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>EQUIPMENT FOR EIL:</td>
<td><p>INVENTORY LISTING (EIL)</p>
<p>160 LABORATORY SERVICE</p></td>
<td>JUL 10,1997 08:05</td>
<td>PAGE 21</td>
</tr>
</tbody>
</table>

ENTRY \# STN FUND SGL LEASE COST ASSET VALUE LAST INVENTORIED

­

CATEGORY STOCK NUMBER: 2350-629155 (SNOWMOBILE)

SNOWMOBILE. A SELF-PROPELLED, POWERED MOTOR VEHICLE DESIGNED FOR TRAVELING OVER SNOW. IT IS USUALLY EQUIPPED WITH STEERABLE RUNNERS AT THE FRONT AND ENDLESS TRACKS AT THE REAR.

178 AMAF 1750 5000.00

MFGR NAME: ENMFGR, NINE

EQUIPMENT INVENTORY LISTING (EIL) JUL 10,1997 SIGNATURE PAGE

EIL: 160

LABORATORY SERVICE

I UNDERSTAND MY RESPONSIBILITIES LISTED IN VA MANUAL MP-2, SUBCHAPTER E, SUBPART 108-25.50 AND THAT I MAY BE HELD LIABLE UNDER CONDITIONS THEREIN. I ASSUME RESPONSIBILITY FOR ITEMS LISTED ABOVE WHICH WERE ON HAND ON THE DATE SIGNED.

I PERSONALLY REVIEWED AND EVALUATED THE NEED FOR THE EQUIPMENT ASSIGNED TO MY ACTIVITY AND FIND THAT:

| \| \| | \(1\) | ALL EQUIPMENT IS ESSENTIAL FOR THE PROPER FUNCTIONING OF THIS ACTIVITY OR, |
|-------|-------|----------------------------------------------------------------------------|
| \| \| | \(2\) | THE ATTACHED VA FORM(S) 90-2237-ADP HAS (HAVE) BEEN PREPARED               |
|       |       | TO TURN IN THE EQUIPMENT DETERMINED TO BE EXCESS TO THE NEEDS              |
|       |       | OF THIS ACTIVITY OR,                                                       |
| \| \| | \(3\) | THE ATTACHED VA FORM(S) 10-1274, RESEARCH EQUIPMENT AVAILABLE TO           |
|       |       | VA REGIONAL RESEARCH EQUIPMENT PROGRAM HAS (HAVE) BEEN PREPARED FOR        |
|       |       | DISPOSITION AS APPROPRIATE IN ACCORDANCE WITH MP-2, SUBCHAPTER H,          |
|       |       | 108-43 OR,                                                                 |
| \| \| | \(4\) | THE ITEM(S) LISTED ON ATTACHED REPORT OF SURVEY FORM(S), VA 90-1217,       |
|       |       | IS (ARE) MISSING OR DAMAGED. IT IS UNDERSTOOD THAT ACCOUNTABILITY          |
|       |       | WILL BE DROPPED FROM THE EIL BUT MY RESPONSIBILITY FOR SUCH ITEMS          |
|       |       | WILL BE TERMINATED ONLY WHEN FINAL SURVEY ACTION HAS BEEN COMPLETED.       |

I ALSO CERTIFY THAT ANY PERSONALLY OWNED PROPERTY WHICH HAS BEEN PLACED INTO OFFICIAL USE HAS BEEN LISTED ON VA FORM 90-2235 (LIST OF PERSONALLY OWNED PROPERTY PLACED IN OFFICIAL USE) AND HAS BEEN SUBMITTED THROUGH THE PROPER CHANNELS FOR APPROVAL.

SIGNATURE:

TITLE:

DATE:

#### Inventory Listing Option 2. Equipment Category Inventory

Select Inventory Listing Option: 2 Equipment Category Inventory START WITH EQUIPMENT CATEGORY: FIRST//??

TO SORT IN SEQUENCE, STARTING FROM A CERTAIN EQUIPMENT CATEGORY, TYPE THAT EQUIPMENT CATEGORY

'@' MEANS 'INCLUDE NULL EQUIPMENT CATEGORY FIELDS' START WITH EQUIPMENT CATEGORY: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

EQUIPMENT INV. LIST MAR 30,1993 10:20 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE REPL. DATE ACQ. VALUE CAT STOCK \# NXRN \# LAST INVENTORIED LOCATION USE STATUS

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>8</th>
<th>AIR CONDITIONER</th>
<th></th>
<th colspan="2">ENGINEERING SVC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>MAR 17,1993</td>
<td>MAR 17,2008</td>
<td>50.00</td>
<td><p>6150-439347</p>
<p>IN USE</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>AIR CONDITIONER</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

13 AIR CONDITIONER

EQUIPMENT INV. LIST

ENTRY NUMBER EQUIPMENT CATEGORY

PM NUMBER ACQ. DATE REPL. DATE NXRN \# LAST INVENTORIED LOCATION

MAR 30,1993 10:20 PAGE 2 USING SERVICE

ACQ. VALUE CAT STOCK \#

USE STATUS

3805-438395

EQUIPMENT INV. LIST

ENTRY NUMBER EQUIPMENT CATEGORY

PM NUMBER ACQ. DATE REPL. DATE NXRN \# LAST INVENTORIED LOCATION

IN USE

MAR 30,1993 10:20 PAGE 3 USING SERVICE

ACQ. VALUE CAT STOCK \#

USE STATUS

4 COUNTER-BLOOD CELL CLINICAL LABORATORY PM00000025 AUG 1,1111 AUG 1,2004 500 6630-438414

414 25-7A IN USE

Press \<RETURN\> to continue...

#### Inventory Listing Option 3. Location Inventory

Select Inventory Listing Option: 3 Location Inventory DEVICE: LAN RIGHT MARGIN: 80//

EQUIPMENT INV. LIST MAR 30,1993 10:21 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE REPL. DATE ACQ. VALUE CAT STOCK \# NXRN \#

LAST INVENTORIED LOCATION USE STATUS

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>7</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2">CLINICAL LABORATORY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>222222222</p>
<p>2222</p></td>
<td colspan="2">JAN 26,1993</td>
<td colspan="2"><p>JAN 26,2003</p>
<p>25-7A</p></td>
<td>1400</td>
<td><p>3550-438952</p>
<p>IN USE</p></td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2">COUNTER-BLOOD</td>
<td>CELL</td>
<td></td>
<td colspan="2">CLINICAL LABORATORY</td>
</tr>
<tr class="odd">
<td><p>PM00000025</p>
<p>414</p></td>
<td>AUG</td>
<td>1,1111</td>
<td>AUG</td>
<td><p>1,2004</p>
<p>25-7A</p></td>
<td>500</td>
<td><p>6630-438414</p>
<p>IN USE</p></td>
</tr>
</tbody>
</table>

Press \<RETURN\> to continue...

#### Inventory Listing Option 4. Using Service Inventory

Select Inventory Listing Option: 4 Using Service Inventory START WITH SERVICE POINTER: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

EQUIPMENT INV. LIST

ENTRY NUMBER EQUIPMENT CATEGORY

PM NUMBER ACQ. DATE REPL. DATE NXRN \# LAST INVENTORIED LOCATION

MAR 30,1993 10:21 PAGE 1 USING SERVICE

ACQ. VALUE CAT STOCK \#

USE STATUS

4 COUNTER-BLOOD CELL CLINICAL LABORATORY

7

EQUIPMENT INV. LIST

ENTRY NUMBER EQUIPMENT CATEGORY

PM NUMBER ACQ. DATE REPL. DATE NXRN \# LAST INVENTORIED LOCATION

MAR 30,1993 10:21 PAGE 2 USING SERVICE

ACQ. VALUE CAT STOCK \#

USE STATUS

8 AIR CONDITIONER ENGINEERING SVC

MAR 17,1993 MAR 17,2008 50.00 6150-439347

IN USE

#### Inventory Listing Option 5. Responsible Shop Inventory

Select Inventory Listing Option: 5 Responsible Shop Inventory

Important note: SHOP NAME(S) MUST BE ENTERED IN RESPONSE TO THE 'START WITH' AND 'GO TO' PROMPTS. NUMBERS WILL NOT BE UNDERSTOOD BY THE SORT LOGIC.

START WITH RESPONSIBLE SHOP: FIRST// DEVICE: LAN RIGHT MARGIN: 80//

EQUIPMENT INV. LIST MAR 30,1993 10:22 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE REPL. DATE ACQ. VALUE CAT STOCK \# NXRN \# LAST INVENTORIED LOCATION USE STATUS

RESPONSIBLE SHOP: BIOMEDICAL

4 COUNTER-BLOOD CELL CLINICAL LABORATORY PM00000025 AUG 1,1111 AUG 1,2004 500 6630-438414

414 25-7A IN USE

5

6 BACKHOE IRM

IN USE

EQUIPMENT INV. LIST

ENTRY NUMBER EQUIPMENT CATEGORY

PM NUMBER ACQ. DATE REPL. DATE NXRN \# LAST INVENTORIED LOCATION

MAR 30,1993 10:22 PAGE 2 USING SERVICE

ACQ. VALUE CAT STOCK \#

USE STATUS

RESPONSIBLE SHOP: HEAT AND AIR CONDITION

12. AIR CONDITIONER
13. AIR CONDITIONER

#### Inventory Listing Option 6. Use Status Inventory

Select Inventory Listing Option: 6 Use Status Inventory START WITH CMR: FIRST//

START WITH USE STATUS: FIRST// DEVICE: LAN RIGHT MARGIN: 80//

EQUIPMENT INV. LIST MAR 30,1993 10:22 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE REPL. DATE ACQ. VALUE CAT STOCK \# NXRN \# LAST INVENTORIED LOCATION USE STATUS

CMR: LAB EQUIP

4 COUNTER-BLOOD CELL CLINICAL LABORATORY PM00000025 AUG 1,1111 AUG 1,2004 500 6630-438414

414. 25-7A IN USE

#### Inventory Listing Option 7 - Nonexpendable Expensed Inventory

Select Inventory Listing Option: 7 Nonexpendable Expensed Inventory

Start WITH:??

Choose from:

100 DENTAL

110 DIETETIC

130 ENGINEERING

.

19W MEDICAL MEDIA

^

Start WITH: 130 ENGINEERING Go TO: 130

Should the COMMENTS field be printed? NO// y YES DEVICE: HOME// UCX/TELNET RIGHT MARGIN: 80//

NON-EXPENDABLE EXPENSED INVENTORY JUL 10,1997 08:06 PAGE 1 FOR EIL: 130 ENGINEERING SERVICE

ENTRY \# STN FUND SGL LEASE COST ASSET VALUE LAST INVENTORIED

­

CATEGORY STOCK NUMBER: 5820-439321 (RECE RADIO PAGING SYS)

RECEIVER, RADIO (PAGING SYSTEM). AN ITEM DESIGNED TO BE WORN BY KEY PERSONNEL OF AN ORGANIZATION FOR THE PURPOSE OF NOTIFYING THEM TO CONTACT THE CALLER WHO WILL RELAY A MESSAGE THAT HAS BEEN RECEIVED FOR THEM. IT IS DESIGNED FOR ONE WAY PAGE CALLS AND USUALLY HAS A SPRING TYPE POCKET CLIP, AND IS BATTERY OPERATED.

47 6100

MFGR NAME: ENMFGR1, TWO

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MANF: ENMFGR1, THREE</p>
<p>MODEL: AO3CJC24681</p></th>
<th></th>
<th></th>
<th>SERIAL: 12345678</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA PM #:</td>
<td></td>
<td></td>
<td>LOCAL ID:</td>
</tr>
<tr class="even">
<td>USE STATUS: IN USE</td>
<td></td>
<td></td>
<td>USING SVC: INFORMATION SYSTEMS CENTER</td>
</tr>
<tr class="odd">
<td>LOCATION:</td>
<td></td>
<td></td>
<td>PREVIOUS:</td>
</tr>
<tr class="even">
<td>CONDITION:</td>
<td></td>
<td></td>
<td>ACQ METH: PURCHASED</td>
</tr>
<tr class="odd">
<td>ACQ DATE:</td>
<td>LE:</td>
<td>15</td>
<td>REPL DATE:</td>
</tr>
</tbody>
</table>

COMMENTS:

KEYNOTE PAGERS 164.525 TONE & VOICE WITH GROUP CODE ACTIVATION GROUP NUMBER 233 TO ACTIVATE CODE

SPEX:

NON-EXPENDABLE EXPENSED INVENTORY JUL 10,1997 08:06 PAGE 12 FOR EIL: 130 ENGINEERING SERVICE

ENTRY \# STN FUND SGL LEASE COST ASSET VALUE LAST INVENTORIED

­

CATEGORY STOCK NUMBER: 6515-438301 (MONITOR CARDIAC)

MONITOR, CARDIAC. AN ELECTRONIC ITEM DESIGNED TO PROVIDE A CONTINUOUS AUDIBLE AND/OR VISUAL INDICATION OF HEART RATE AND RHYTHM AND MAY ALSO BE DESIGNED TO DISPLAY ELECTROCARDIOGRAM AND PULSE WAVEFORMS. IT IS USEDFOR DETECTION OF CARDIAC ARREST, ARRHYTHMIAS, OR SUBSTANTIAL DROP IN BLOOD PRESSURE DURING SURGERY, AND IS COMPLETE WITH ALARM. MAY CONSIST OF A NEEDLE INDICATOR OR BUILT-IN CARDIOSCOPE. MAY BE THE RACK MOUNTING (PLUG-IN) OR SELF-CONTAINED, CABINET TYPE.

27 5964.97

MFGR NAME:

MANF: ENMFGR, TWO

MODEL: 78510B SERIAL: 2622A08744

VA PM \#: 6515-7630 LOCAL ID:

USE STATUS: IN USE LOCATION: A208-01-JC CONDITION:

ACQ DATE: MAR 1988

USING SVC:

PREVIOUS:

ACQ METH: PURCHASED LE: 8 REPL DATE: MAR 1998

COMMENTS:

SPEX:

TOTAL 0.00 6637.97

COUNT 8

#### Warranty List

The fourth Equipment Reports option allows the display of a warranty expiration list, with entry number, equipment category, owning service, PM number, acquisition date, acquisition value, and location being displayed.

Select Equipment Reports Option: 4 Warranty List START WITH WARRANTY EXP. DATE: FIRST// ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. You may omit the precise day, as: JAN, 1957

Date on which repairs to this item become the sole responsibility of the government. Generally stipulated in the contract or sales agreement.

START WITH WARRANTY EXP. DATE: FIRST// \<RET\> DEVICE: UCX/TELNET RIGHT MARGIN: 80//

\<RET\>

WARRANTY EXPIRATION LIST MAR 31,1997 15:35 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE ACQ. VALUE LOCATION CAT STOCK \#

WARRANTY EXP. DATE: JUN 1993

62 COPIER MEDICAL ADMINISTRATION JUN 1992 6200.00 100-110-JC 5835-238864

WARRANTY EXP. DATE: DEC 25,1996

18. ACQUISITION & MATERIAL MGMT

6515-8934 JAN 20,1996 6150.00 105-148 6630-185880

WARRANTY EXP. DATE: DEC 31,1996

19. INFORMATION RESOURCES MGMT

6515-8921 JUN 30,1996 7234.00 102-148 6640-095680

WARRANTY EXP. DATE: MAR 6,1997

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 26%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>58</th>
<th>COMPUTER TERMINAL/DISPLAY DEC 6,1996 275.00</th>
<th>ENGINEERING 204-114</th>
<th>7025-438122</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>59</p>
<p>^</p></td>
<td>COMPUTER TERMINAL/DISPLAY</td>
<td>ENGINEERING</td>
<td></td>
</tr>
</tbody>
</table>

#### Replacement Listing

The fifth option for Equipment Reports prints all entries in the Equipment Inv. file which are scheduled for replacement within the time interval specified.

Select Equipment Reports Option: 5 Replacement Listing START WITH REPLACEMENT DATE: FIRST// \<RET\>

DEVICE: \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

REPLACEMENT LISTING MAR 31,1997 16:58 PAGE 1 ENTRY NUMBER EQUIPMENT CATEGORY USING SERVICE

PM NUMBER ACQ. DATE ACQ. VALUE LOCATION CAT STOCK \# CONDITION

REPLACEMENT DATE: OCT 18,1999

1 BUILDING MANAGEMENT

OCT 18,1992 9056.94 102-148 3610-438993

REPLACEMENT DATE: FEB 4,2001

3 INFORMATION RESOURCES MGMT

FEB 4,1993 500.00 102-148 7025-628324

REPLACEMENT DATE: FEB 18,2001

| 4           |         | MEDICINE |             |      |
|-------------|---------|----------|-------------|------|
| FEB 18,1993 | 6570.40 | 213-114  | 6515-438660 |      |
| 6           |         | MEDICINE |             |      |
| FEB 18,1993 | 5670.50 | 303-110  | 6515-438660 | POOR |

#### Failure Rate Report

This option prints a synopsis of the repair history for the Equipment Category specified by the user.

Select Equipment Reports Option: 6 Failure Rate Report

Do you wish to analyze all equipment in the inventory? No// ?

Alternately, you may elect to have a specific EQUIPMENT CATEGORY analyzed.

Do you wish to analyze all equipment in the inventory? No// Y (Yes) Starting date for this report: 7/1/95 (JUL 01, 1995)

Ending date for this report: (7/1/95 - 7/11/97): t (JUL 11, 1997) Please enter the minimum number of repair episodes necessary.

for inclusion in this report. (1-99 per item) ?

Enter the number of repair episodes per item necessary before that item is to be identified as meeting the failure rate criteria (whole number only).

Please enter the minimum number of repair episodes necessary for inclusion in this report. (1-99 per item) 1

Include all vendor activity, (work actions beginning with a 'V')? No// ?

This report will consider all entries in the Equipment Histories that are identified as 'General Repair' items. You may also include entries that are identified as 'Vendor Service' items by answering \[Y\]es at this prompt.

Include all vendor activity, (work actions beginning with a 'V')? No// Y (Yes) Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

compiling the data........................

EQUIPMENT REPAIRS (ALL EQUIPMENT) JUL 11,1997@08:56 Page 1 From: 07-01-95 To: 07-11-97

Reference Entry \# Hrs Labor\$ Mat'l\$ Vndr\$ Total\$ Worker

-----------

| 970710-G1 | 198 | 3.6 | 44.35 | 37.45 | 0.00 | 81.80 | ENUSER1, NINE |
|-----------|-----|-----|-------|-------|------|-------|---------------|
| 970710-G1 | 199 | 3.6 | 44.35 | 37.45 | 0.00 | 81.80 | ENUSER1, NINE |
| 970709-G1 | 200 | 4.5 | 45.00 | 40.25 | 0.00 | 85.25 | ENUSER2, TEN  |
| 970709-G1 | 201 | 3.6 | 44.35 | 37.45 | 0.00 | 81.80 | ENUSER1, NINE |

\_\_\_\_\_\_\_\_\_\_ TOTAL 15.3 178.05 152.60 0.00 330.65

#### PM Workload Analysis

This option for Equipment Reports prints a breakdown of scheduled PMI hours by month for a given shop. This display is to be used to help balance the preventive maintenance workload.

Select Equipment Reports Option: 7 PM Workload Analysis Select ENGINEERING SECTION LIST: ELE

1.  ELECTRIC
2.  ELEVATORS(M&R)
3.  ELEVATORS(OPERATORS) CHOOSE 1-3: 1

Should results be broken out by TECHNICIAN? NO// \<RET\> YES Include ALL technicians? YES// \<RET\>

Select output device:

RETURN DISPLAY

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

compiling data

PM Workload Analysis: ELECTRIC Shop APR 1,1997 Responsible Technician: ENUSER, TWO

| Month | Item Count\* Standard | Hours |
|-------|-----------------------|-------|
| JAN   | 0                     | 0.0   |
| FEB   | 0                     | 0.0   |
| MAR   | 1                     | 3.7   |
| APR   | 9                     | 10.8  |
| MAY   | 0                     | 0.0   |
| JUN   | 0                     | 0.0   |
| JUL   | 0                     | 0.0   |
| AUG   | 0                     | 0.0   |
| SEP   | 0                     | 0.0   |
| OCT   | 0                     | 0.0   |
| NOV   | 0                     | 0.0   |
| DEC   | 0                     | 0.0   |

---------- -------------­

COUNT\*\* 10

TOTAL 14.5

- Count of items to be inspected in month indicated.

\*\*Count of all items for which this technician has PM responsibility. Enter RETURN to continue or '^' to exit:

PM Workload Analysis: ELECTRIC Shop APR 1,1997 Responsible Technician: ENUSER, FOUR

| Month | Item Count\* | Standard Hours |
|-------|--------------|----------------|
| JAN   | 0            | 0.0            |
| FEB   | 0            | 0.0            |
| MAR   | 0            | 0.0            |
| APR   | 0            | 0.0            |
| MAY   | 1            | 1.4            |
| JUN   | 0            | 0.0            |
| JUL   | 0            | 0.0            |
| AUG   | 0            | 0.0            |
| SEP   | 0            | 0.0            |
| OCT   | 0            | 0.0            |
| NOV   | 0            | 0.0            |
| DEC   | 0            | 0.0            |
|       | ----------   | -------------­  |

COUNT\*\* 1

TOTAL 1.4

- Count of items to be inspected in month indicated.

\*\*Count of all items for which this technician has PM responsibility.

Note that the item count may add in the same piece of equipment more than once, as the piece may very well be subject to more than one PM in the course of a year.

#### Direct Posting to Equipment Histories

This option is really not a report, but rather a utility that allows posting of activities to Equipment Histories without going through the Work Order module.

Select Equipment Reports Option: 8 Direct Posting to Equipment Histories

This is a utility for posting information directly to the AEMS-MERS Equipment History sub-file.

Are you sure you want to proceed? NO// y YES

One way of specifying the equipment records to be impacted is to perform a search of the Equipment Inv. file (#6914) using VA FileMan and store the results in a Sort template. At this point, the system will ask if such a template is to be used:

Are the Equipment Records to be found in a SORT template? NO// \<RET\>

Select EQUIPMENT INV.: ?

Answer with EQUIPMENT INV. ENTRY NUMBER, or MANUFACTURER, or MFGR. EQUIPMENT NAME, or MODEL, or MODEL(C), or SERIAL \#, or SERIAL \#(C), or EQUIPMENT CATEGORY, or PURCHASE ORDER \#, or CATEGORY STOCK NUMBER, or LOCATION, or VA PM NUMBER, or LOCAL IDENTIFIER

Do you want the entire 95-Entry EQUIPMENT INV. List? N (No)

Select EQUIPMENT INV.: defibRILLATOR.

| 1   | 1   | 8978899       | DEFIBRILLATOR | IN USE | 7530-4565 |
|-----|-----|---------------|---------------|--------|-----------|
| 2   | 64  | 32781         | DEFIBRILLATOR | IN USE | 6515-6328 |
| 3   | 151 | 00002         | DEFIBRILLATOR |        | 6515-0001 |
| 4   | 198 | DEFIBRILLATOR |               | IN USE |           |
| 5   | 199 | DEFIBRILLATOR |               | IN USE |           |

Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 1

| Select EQUIPMENT INV.: | 32781 64        | 32781 DEFIBRILLATOR | IN USE 65 |
|------------------------|-----------------|---------------------|-----------|
| 15-6328                |                 |                     |           |
| Select EQUIPMENT INV.: | 78 89445A70 | BED-ELECTRIC IN USE | 6530-7187 |
| Select EQUIPMENT INV.: | 80 89445A04 | BED-ELECTRIC IN USE | 6530-6590 |

Shall we save these ENTRY NUMBERS in a SORT template for future use? NO// y YES Name of SORT template. Must begin with 'ENPOST': ENPOSTTST

OK to create new SORT template? YES// y YES

Enter as much information as may apply. Select NEW WORK ACTION: ?

Answer with NEW WORK ACTION NAME, or HISTORY CODE, or SYNONYM

Do you want the entire 31-Entry NEW WORK ACTION List? y (Yes) Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3

^

Select NEW WORK ACTION: P2 PREVENTIVE MAINTENANCE P2 WORK ORDER REFERENCE:??

Enter 3 to 12 characters. Optional.

WORK ORDER REFERENCE: \< RET\>

Select one of the following: P PASSED

3.  CORRECTIVE ACTION REQUIRED
4.  DEFERRED

PM STATUS: CORRECTIVE ACTION REQUIRED TOTAL HOURS: (0-2080): 150

LABOR COST: (0-999999): 3000

MATERIAL COST: (0-999999): 1500 VENDOR COST: (0-999999): \<RET\> WORKER: ENTECH, ONE// ??

This response can be free text.

WORKER: ENTECH, ONE// \<RET\>

WORK PERFORMED: ??

Free text. 60 character maximum.. WORK PERFORMED: \<RET\>

1

64

78

80

Once the posting has been accomplished, the system will list all the equipment records that were affected.

#### Parent System/Component Hierarchy Report

This option prints a hierarchical list of a parent system and all of its components. Components are indented and listed beneath their parent system. Items that are components of a component in the specified system are included.

Select Equipment Reports Option: 9 Parent System/Component Hierarchy Report Do you want a report for ALL systems? NO// ??

Enter YES to generate a report for all systems.

The computer will identify all the topmost parent systems by looping through the entire Equipment file. A complete system hierarchy will be printed for each of the topmost parent systems which includes all of their components.

It may take a while to search the entire Equipment file.

Enter NO to generate a report for just one system. Enter YES or NO

Do you want a report for ALL systems? NO// YES

Select the 1st field (required) to print for each equipment item. Select FIELD: EQUIPMENT CATEGORY// ??

Choose from:

.01

.5

.6

1

2

ENTRY NUMBER ENTERED BY DATE ENTERED MANUFACTURER PARENT SYSTEM

^

Select FIELD: EQUIPMENT CATEGORY// \<RET\>

Field EQUIPMENT CATEGORY can be 50 characters long. You may want to just print a portion of this field. Number of characters to print: (1-50): 20// 30.

Select the 2nd field (optional) to print for each equipment item. Select FIELD: SERIAL \#

Field SERIAL \# can be 30 characters long.

You may want to just print a portion of this field. Number of characters to print: (1-30): 20// 30.

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

PARENT SYSTEM/COMPONENT HIERARCHY JUL 11, 1997@09:07:02 page 1

for ALL SYSTEMS print field(s): EQUIPMENT CATEGORY and SERIAL \#

78BED-ELECTRIC 89445A70 (3 comp.)

180 4736583920

181 64736485

182 236453

165 (1 comp.)

166POSITIONER 86950498374657

211RADIOGRAPHIC UNIT (DIAGNOSTIC) 10215 (5 comp.)

212TABLE-EXAMINING E12

213INJECTOR-ANGIOGRAPHIC DST8433

214MONITOR-VIDEO SNA713

215TABLE-EXAMINING XG342

216RADIOGRAPHIC UNIT (DIAGNOSTIC) FDXZII END OF REPORT

#### Lockout/Tagout Flag Reports

Select Equipment Reports Option: 10 Lockout/Tagout Flag Reports

1.  Equipment Categories with Lockout/Tagout SET
2.  Equipment Records with Lockout/Tagout SET
3.  Equip with Lockout/Tagout CLEAR but Category SET

#### Lockout/Tagout Flag Reports Option 1. Equipment Categories with Lockout/Tagout SET

Prints from Equipment Category file (#6911).

Select Lockout/Tagout Flag Reports Option: 1 Equipment Categories with Lockout/ Tagout SET

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80// \< RET\>

EQUIPMENT CATEGORIES with 'LOCKOUT REQUIRED?' Flag set to 'YES' Page 1 JUL 11,1997@10:00

DEFIBRILLATOR (7 Equipment Records)

COMPUTER TERMINAL/DISPLAY (0 Equipment Records) AIR CONDITIONER (THRU WALL) (2 Equipment Records) BED-ELECTRIC (2 Equipment Records)

#### Lockout/Tagout Flag Reports Option 2. Equipment Records with Lockout/Tagout SET

Prints from the Equipment Inv. file (#6914).

Select Lockout/Tagout Flag Reports Option: 2 Equipment Records with Lockout/Tag out SET.

Sort Report by EQUIPMENT CATEGORY? YES// \< RET\>

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80// \< RET\>

EQUIPMENT with 'LOCKOUT REQUIRED?' Flag 'SET' JUL 11,1997@10:01 Page 1

ENTRY \# Equipment Category Manufacturer Equipment Name Location Manufacturer Model Serial Number

162 AIR CONDITIONER (THR

A T SURGICAL SSDASD S22222

195 AIR CONDITIONER (THR

AFFILIATED HOSPITAL PROD/SHAMPAI 123445553313333444444

78 BED-ELECTRIC A219A-01-JC

HILL ROM 894A50 89445A70

64 DEFIBRILLATOR A218A-01-JC

| 200 | DEFIBRILLATOR | DEFIBRILLATOR | 9-223      |
|-----|---------------|---------------|------------|
| 201 | DEFIBRILLATOR | DEFIBRILLATOR | 9-224      |
| 14  | PROJECTOR     | PROJECTOR     | A206-01-JC |

EASTMAN KODAK/CUSTOMER EQUIP SVC 5400 352662

#### Lockout/Tagout Flag Reports Option 3. Equip with Lockout/Tagout CLEAR but Category SET

Prints list of Equipment Records (file \#6914) that have the LOCKOUT REQUIRED? clear (not set to 'YES') but belonging to an Equipment Category (file \#6911) for which the LOCKOUT REQUIRED? field is 'YES'.

Such records, if any exist, would represent exceptional situations.

Select Lockout/Tagout Flag Reports Option: 3 Equip with Lockout/Tagout CLEAR but Category SET

DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

'LOCKOUT REQUIRED?' Flag Exception List JUL 11,1997@10:01 Page 1 (Flag is CLEAR for these ENTRIES, but their EQUIPMENT CATEGORY Flag is SET) ENTRY \# Equipment Category Manufacturer Equipment Name Location

Manufacturer Model Serial Number

1 DEFIBRILLATOR DEFIBRILLATOR W/O MONITOR 201-110

HEWLETT PACKARD/MEDICAL PROD 8700 8978899

80 BED-ELECTRIC A219B-01-JC

HILL ROM 894A50 89445A04

### PM Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for enrolling devices and Equipment Category in the PMI program. PM Parameters has a sub menu containing six options. An example of each option will be presented.

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

Select Equipment Management Option: 6 PM Parameters

PREVENTIVE MAINTENANCE PARAMETERS

Version 7

1.  Display Specific Device PM Schedule
2.  Display Equipment Category PM Schedule
3.  Print PM Procedure
4.  Enter/Edit Specific Device PM Schedule
5.  Enter/Edit Equipment Category PM Schedule
6.  Enter/Edit PM Procedure
7.  Reassign a Technician's PM Responsibilities

Select PM Parameters Option:

#### Display Specific Device PM Schedule

Select PM Parameters Option: 1 Display Specific Device PM Schedule

Select EQUIPMENT INV. ENTRY NUMBER: 21 7888UYHG BED-ELECTRIC IN USE 6530-6723

Equipment ID \#: 21 BED-ELECTRIC

PM \#: 6530-6723 Local ID: S/N: 7888UYHG

Lockout Required? YES

BIOMEDICAL SHOP

Tech: ENTECH, FOUR Starting Month: FEB Skip Months: Criticality: 6

Frequency (multiple):

QUARTERLY 0.8 hrs \$0 (est) Level: N/A Proc Ref: BME-1 Title: HOSPITAL BEDS

Tech: ENTECH, TWO

Skip Months: Frequency (multiple):

ELECTRIC SHOP

Starting Month: APR Criticality: 6

ANNUAL 1.2 hrs \$80 (est) Level: N/A

#### Display Equipment Category PM Schedule

Select PM Parameters Option: 2 Display Equipment Category PM Schedule Select EQUIPMENT CATEGORY NAME: BED-ELECTRIC

Equipment Category: BED-ELECTRIC

BIOMEDICAL SHOP

Tech: ENUSER, FOUR Starting Month: FEB

Skip Months: Criticality: 6

Frequency (multiple):

QUARTERLY 0.8 hrs \$0 (est) Level: N/A Proc Ref: BME-1 Title: HOSPITAL BEDS

Tech: ENUSER, TWO

Skip Months: Frequency (multiple):

ELECTRIC SHOP

Starting Month: APR Criticality: 6

ANNUAL 1.2 hrs \$80 (est) Level: N/A

#### Print PM Procedure

| START WITH PM REFERENCE: FIRST// A GO TO PM REFERENCE: LAST// Z DEVICE: RIGHT MARGIN: 80// |                 |                   |       |        |
|--------------------------------------------------------------------------------------------|-----------------|-------------------|-------|--------|
| PMI Procedure(s) PM REFERENCE                                                              |                 | MAR 2,1993 SOURCE | 10:28 | PAGE 1 |
|                                                                                            | PROCEDURE TITLE |                   |       |        |
| TEXT                                                                                       |                 |                   |       |        |

BED01 BED, ELEC 21-SA ASHE

1.  Remove covers from motor assembly.
2.  Lubricate bearings and worm gears.
3.  Inspect belts for any sign of wear and replace if necessary.
4.  Replace plastic drive gear attached to shaft of electric motor located in main housing.
5.  Replace all covers.

#### Enter/Edit Specific Device PM Schedule

This option allows you to enter or edit a PM schedule for a specific piece of equipment. Users may specify whether or not a display of the PM schedule is desired.

Select PM Parameters Option: 4 Enter/Edit Specific Device PM Schedule

| Select | EQUIPMENT INV. | ENTRY NUMBER: 1 |        |           |
|--------|----------------|-----------------|--------|-----------|
| 1      | 1 8978899      | DEFIBRILLATOR   | IN USE | 7530-4565 |

2 1 193 05305003H1 IN USE

3 1125EA03 112 IN USE

4 1757B 108 3305096 IN USE 6910-5109

5 17B 166 86950498374657 POSITIONER IN USE 7310-9876

Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1

Would you like to see the existing PM schedule for this device? Yes// Y (Yes)

Equipment ID \#: 1 DEFIBRILLATOR

PM \#: 7530-4565 Local ID: S/N: 8978899

BIOMEDICAL SHOP

Tech: ENUSER, ONE Starting Month: MAR

Skip Months: Criticality: 1

Frequency (multiple):

ANNUAL 40.0 hrs \$500 (est) Level: 6 SEMI-ANNUAL 15.0 hrs \$50 (est) Level: 3,5 Proc Ref: DEFIB4 Title: ASHE-DEFIBRILLATOR

MONTHLY 0.4 hrs \$0 (est) Level: N/A

ELECTRIC SHOP

Tech: Starting Month:

Skip Months: Criticality:

Frequency (multiple):

Press \<RETURN\> to continue..\< RET\>.

Select RESPONSIBLE SHOP: ELECTRIC// \< RET\>

RESPONSIBLE SHOP: ELECTRIC// \< RET\> TECHNICIAN:?

The Engineering Service employee who normally does the PM work on this piece of equipment for this shop.

TECHNICIAN: ENUSER, ONE

STARTING MONTH: MAR MAR SKIP MONTHS:??

A range of months (inclusive) during which PMI's are to be suspended. For example, an entry of 'NOV-MAR' for an air-conditioner would suppress the scheduling of any PMIs in NOV, DEC, JAN, FEB, and MAR.

Some care needs to be taken when using this field. If you want an ANNUAL inspection, for instance, be sure that the STARTING MONTH is not within the range specified by the SKIP MONTHS; otherwise the ANNUAL PMI will never be scheduled.

Entries must take the form 'MMM-NNN', where MMM is a three-character abbreviation of the first month for which PMII’s are to be suspended and NNN is a three-character abbreviation for the last month for which PMI's are to be suspended. Valid abbreviations are JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, and DEC.

SKIP MONTHS: \< RET\> CRITICALITY:??

An index of the importance of performing PMIs on this device. Enter an integer between 1 and some upper limit not greater than 99 (most sites use

10 or 20). The closer the values are to the upper limit the more critical the PMI's become. A value of 1 would indicate that PMIs are desirable but far from essential (least critical).

When PM worklists are generated, the system will ask if all devices should be included or just those whose CRITICALITY is within a certain user selectable range (say, 7 to 10). This is intended as a means of adjusting workload to match available resources.

Use of this feature is left entirely to the discretion of each site. If a CRITICALITY range is selected, the system will ask the user whether devices having no CRITICALITY should be included or excluded.

CRITICALITY: 10

This is intended as a means of adjusting workload to match available resources. Use of this feature is left entirely to the discretion of each site. If a range of 1 through 10 seems like overkill, you may wish to restrict yourself to 5 through 10 instead. If all PMIs are deemed to be a high priority and adequate resources are available, there is probably no need to use this feature at all.

Select FREQUENCY:??

Make a separate entry for each category (MONTHLY, QUARTERLY, etc.) of PMI that is to be scheduled for this device. The PM module looks at this field in conjunction with the STARTING MONTH when PM lists are generated.

Let's consider a fairly complex example: a device with SEMI-ANNUAL, QUARTERLY, and MONTHLY PMI's and a STARTING MONTH of MAR. Assuming no entry for SKIP MONTHS, the following PMI's will be scheduled:

SEMI-ANNUAL in MAR and SEP; QUARTERLY in JUN and DEC.

MONTHLY in APR, MAY, JUL, AUG, OCT, NOV, JAN and FEB.

Choose from:

An ANNUAL

S SEMI-ANNUAL

Q QUARTERLY

M MONTHLY

BM BI-MONTHLY

23. WEEKLY

BW BI-WEEKLY

N NONE

BA BI-ANNUAL

TA TRI-ANNUAL

<span id="PENT_ANNAUL_QUAD_ANNUAL" class="anchor"></span>PA PENT-ANNUAL

QA QUAD-ANNUAL

Select FREQUENCY: A (ANNUAL)

Are you adding 'ANNUAL' as a new FREQUENCY (the 1ST for this RESPONSIBLE SHOP)

? No// y (Yes)

HOURS (Estimated): 40

MATERIAL COST (Estimated): 500

LEVEL:??

Each scheduled PMI may be composed of some combination of one or more of the following discrete levels of activity:

Level 1 - Visual inspection only.

Level 2 - Check and adjust operator controls; Level 3 - Electrical safety analysis.

Level 4 - Minor parts replacement; Level 5 - Major parts replacement; Level 6 - Complete overhaul.

LEVEL is an optional field and is intended to accommodate the needs of certain facilities with highly developed PM programs. Entries for LEVEL (if any) will be printed on the PM worklist as a reminder to the responsible technician.

If more than one number applies, separate numbers a comma.

LEVEL: 6

PROCEDURE:?

Enter the abbreviation (4 to 10 characters) of the PROCEDURE to be followed in performing this category of PMI on this device. The title (as well as the abbreviation) of the PM PROCEDURE will appear on PM worksheets for reference.

If disk space permits, the actual procedure itself may be entered in the TEXT field of the PM PROCEDURES file (Number 6914.2) and printed on demand.

In any event, the procedure should be on file and readily accessible to the technician performing the work.

^

You may enter a new PM PROCEDURES, if you wish ANSWER MUST BE 2-20 CHARACTERS IN LENGTH PROCEDURE: DEFIB4 ASHE-DEFIBRILLATOR

Select FREQUENCY: S (SEMI-ANNUAL)

Are you adding 'SEMI-ANNUAL' as a new FREQUENCY (the 2ND for this RESPONSIBLE

SHOP)? No// y (Yes)

HOURS (Estimated): 15

MATERIAL COST (Estimated): 50

LEVEL: 3,5

PROCEDURE:

Select FREQUENCY: \< RET\>

When display of the PM schedule is not required, users enter all additional information in the order of the system prompts. Any information previously entered is displayed within the prompt itself.

#### Enter/Edit Equipment Category PM Schedule

This option allows you to enter/edit the PM schedule for a category of equipment.

Select PM Parameters Option: 5 Enter/Edit Equipment Category PM Schedule

Select EQUIPMENT CATEGORY NAME: DEFIBRILLATOR

Equipment Category: DEFIBRILLATOR Lockout Required?: YES.

BIOMEDICAL SHOP

Tech: ENUSER2, ONE Starting Month: MAR

Skip Months: Criticality: 1

Frequency (multiple):

ANNUAL 40.0 hrs \$500 (est) Level: 6 SEMI-ANNUAL 15.0 hrs \$50 (est) Level: 3,5 Proc Ref: DEFIB4 Title: ASHE-DEFIBRILLATOR

MONTHLY 0.4 hrs \$0 (est) Level: N/A

\`Press \<RETURN\> to continue... \< RET\> NAME: DEFIBRILLATOR// ??

A category of devices that receive the same frequencies and types of preventive maintenance inspections.

NAME: DEFIBRILLATOR// \< RET\>

Select SYNONYM: CARDIOLIFE (NIHON KOHDEN)// ??

Choose from:

CARDIOLIFE (NIHON KOHDEN) HEART STATION (KONTRON) LIFEPAK (PHYSIO-CONTROL) MEDIC (BURDICK)

A multiple-valued field intended to allow for selection of Equipment Category in more than one way. For example: the category named ELECTROCARDIOGRAPH should have ECG and EKG as synonyms.

Select SYNONYM: CARDIOLIFE (NIHON KOHDEN)// \< RET\> Select RESPONSIBLE SHOP: BIOMEDICAL// \< RET\>

RESPONSIBLE SHOP: BIOMEDICAL// \< RET\> TECHNICIAN: ENUSER2, ONE// \< RET\> STARTING MONTH: MAR// \< RET\>

SKIP MONTHS: \< RET\> CRITICALITY: 1// \< RET\>

Select FREQUENCY: MONTHLY// \< RET\> FREQUENCY: MONTHLY// \< RET\>

HOURS (Estimated): .4// \< RET\> MATERIAL COST (Estimated): \< RET\> LEVEL: \< RET\>

PROCEDURE: \< RET\> Select FREQUENCY: \< RET\>

JCAHO:??

Joint Commission on the Accreditation of Healthcare Organizations (JCAHO) standards require that a "separable inventory" be maintained of devices that are of interest to the JCAHO. If this flag in the Equipment Category File is set to 'YES' then all equipment added under that category will have its individual JCAHO field set to 'YES'.

Choose from:

Y YES

N NO

JCAHO: \< RET\>

Are you finished with this Equipment Category? Yes// \< RET\> (Yes) Do you wish to assign this PM schedule to ALL existing equipment records in the category of DEFIBRILLATOR? No// ??

'YES' will cause the system to immediately find every equipment record of type BED­ ELECTRIC and assign each of them the PM schedule just entered. The ENTRY NUMBER of each affected equipment record will be displayed at your terminal, but you will not be asked to confirm the transaction unless you say that you want to.

The ID# of each affected device will be displayed at your terminal, but you will not be asked to confirm the transaction unless you have said that you want to.

Once this process has begun, it should not be interrupted.

Do you wish to assign this PM schedule to ALL existing equipment records in the category of DEFIBRILLATOR? No// y (Yes)

Do you wish to confirm each transaction? No// ??

You should enter 'YES' if you want to apply the revised schedule to some.

BED-ELECTRIC's but not others. Enter 'NO' if you want the revised schedule applied to all equipment of type BED-ELECTRIC.

Do you wish to confirm each transaction? No// \< RET\> (No)

| 1   | 7530-4565 |
|-----|-----------|
| 64  | 6515-6328 |
| 151 | 6515-0001 |
| 198 |           |
| 199 |           |
| 200 |           |

201

Press \<RETURN\> to continue...

Select EQUIPMENT CATEGORY NAME:

If a new PM schedule is applied to existing devices, the STARTING MONTH will be handled differently from the other fields. If the EQUIPMENT CATEGORY contains a STARTING MONTH, that STARTING MONTH will be applied to existing devices. If, however, the EQUIPMENT CATEGORY does not include a STARTING MONTH, the STARTING MONTH of existing devices will remain unchanged. That is, STARTING MONTHs will never be deleted from the Equipment Inv. file via this option.

If preventive maintenance work on items in an equipment category is scheduled to occur over a period of months (ten items for May, six items for June, etc.) two approaches may be taken. The first is to set up equipment categories such as Analyzer- Glucose, Analyzer-Gas, and so on, and enter a month for each category. The second approach is to edit the EQUIPMENT INV. file, entering a month for each item in a selected equipment category.

#### Enter/Edit PM Procedure

Select PM Parameters Option: 6 Enter/Edit PM Procedure\_ Select PM PROCEDURES PM REFERENCE: CLEAN

PROCEDURE TITLE: CLEAN SOURCE:??

Source of the PM instructions. Could be the equipment manufacturer or some authoritative and/or knowledgeable organization (ex: ASHE, VACO, NEMA, etc). Use of this field is optional.

SOURCE:

TEXT:

1\>

Select PM PROCEDURES PM REFERENCE:

Entering a \<RET\> returns the viewer to the PM Parameters option screen.

#### Reassign a Technician's PM Responsibilities

This option is used to change the preventive maintenance (PM) schedules by replacing one technician by a different technician. This change can be limited to PMs by one responsible shop or done for all responsible shops. Both the Equipment Category and Equipment Inv. files will be updated.

Select PM Parameters Option: 7 Reassign a Technician's PM Responsibilities Replace this TECHNICIAN: ??

Choose from: ENUSER, TWO ENUSER , THREE ENUSER , FOUR ENUSER , F IVE ENUSER , S IX ENUSER1 , ONE ENUSER , TEN ENUSER1 , TWO ENUSER1 , S IX ENUSER1 , SEVEN

Replace this TECHNICIAN: ENUSER, FOUR

With this TECHNICIAN: ??

Choose from: ENUSER, TWO ENUSER , THREE ENUSER , FOUR ENUSER , F IVE ENUSER , S IX ENUSER1 , ONE ENUSER , TEN ENUSER1 , TWO ENUSER1 , S IX ENUSER1 , SEVEN

With this TECHNICIAN: ENUSER1, SEVEN

Select one of the following:

ONE RESPONSIBLE SHOP

ALL RESPONSIBLE SHOPS

For PM schedules by: ALL// \<RET\> RESPONSIBLE SHOPS Do you want to individually edit each entry? NO// ??

If YES is entered here, the system will pause after each entry for which TECHNICIAN ENUSER, FOUR has been changed and allow you to edit the TECHNICIAN field.

Enter YES or NO

Do you want to individually edit each entry? NO// \<RET\>

All occurrences of TECHNICIAN in both the EQUIPMENT CATEGORY and EQUIPMENT INV. preventive maintenance schedules will be changed from ENUSER, FOUR to ENUSER1 , SEVEN.

This change will be made for the PM schedules of ALL responsible shops.

OK to Proceed? \<RET\>

This is a required response. Enter '^' to exit.

OK to Proceed? YES

Updating EQUIPMENT CATEGORY file

1.  entries were changed.

Updating EQUIPMENT INV. file

11 entries were changed.

### Generate PM Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for printing PMI work sheets and for deleting PM work orders. The explanatory help prompts, as well as examples of each option, are listed in this section.

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports ...
6.  PM Parameters ...
7.  Generate PM Schedule ...
8.  Record Equipment PMI ...
9.  Print Bar Code Labels for Equipment Management ...
10. Bar Coded Equipment Inventory Management ...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
13. Turn-In/Disposition Equipment The following options are available:

Monthly PM List

Print PMI worksheet(s) for monthly PMIs. These worksheets will include scheduled ANNUAL, SEMI-ANNUAL, QUARTERLY, BI-MONTHLY, and MONTHLY PMIs.

Weekly PM List

Print PMI worksheet(s) to include WEEKLY and BI-WEEKLY PMIs. You will be prompted for a week number (1 through 5). BI-WEEKLY PMIs will appear on worksheets for weeks 1 and 3.

Delete PM Work Orders

Intended to enable you to delete PM work orders in order to conserve disk space. Deletion of PM work orders via this option will not remove an existing record of the PMI from the Equipment History. Deletion of any work order via the EDIT WORK ORDER option WILL remove the corresponding entry from the Equipment History. If you intend to record PMIs in the Equipment History, you should not delete PM work orders until after they have been recorded.

#### Monthly PM List

Select Generate PM Schedule Option: 1 Monthly PM List

GENERATE MONTHLY PM LIST(S)

VERSION 7

Select Month: JUL 1997// \< RET\> (JUL 1997) Sort by: (E, P, I,L,C,S or ? for Help) L// ??

If you have previously set PM Sort using Software Options Enter/Edit on the Program Management menu, you will not be asked this prompt.

All PM lists are sorted by shop, and within shop they may be sorted again by RESPONSIBLE TECHNICIAN. You must now choose how this list should be sorted further. You have the following choices:

'E' for Equipment Entry \# 'P' for PM \#

'I' for Local Identifier 'L' for Location

'C' for Equipment Category 'S' for Owning Service

Sort by: (E, P, I, L,C,S or ? for Help) L// C

For all EQUIPMENT CATEGORIES? Yes//??

Please enter 'Y'es or 'N'o.

For all EQUIPMENT CATEGORIES? Yes// \<RET\> (Yes)

Within CATEGORY, shall worklist be sorted by LOCATION? Enter Yes or No: YES//??

If you want this list to be ordered by LOCATION within CATEGORY, please enter 'YES', otherwise enter 'NO' and items will be ordered by EQUIPMENT ENTRY NUMBER.

Enter Yes or No: YES// \<RET\>

Shall all LOCATIONS be included? YES//??

Enter 'NO' if you want to screen your worklist by DIVISION, BUILDING, WING, and/or ROOM. If you enter 'YES' then all LOCATIONS will be included. The sort order will be DIVISION, BUILDING, WING, and finally ROOM.

Shall all LOCATIONS be included? YES// \<RET\>

Shall worklist be sorted by RESPONSIBLE TECHNICIAN? YES// /??

Enter 'YES' if you want your worklist sorted by RESPONSIBLE TECHNICIAN, with page breaks between each TECH. If you enter 'NO' then equipment items will be selected without regard to RESPONSIBLE TECH.

Shall worklist be sorted by RESPONSIBLE TECHNICIAN? YES// \< RET\> For all TECH's:? Yes//??

You may select all TECH's or one specific TECH. Enter 'Y'es for a worklist which includes all equipment, regardless of RESPONSIBLE TECHNICIAN.

For all TECH's:? Yes// \< RET\> (Yes)

Shall 'OUT OF SERVICE' equipment be included in worklist? YES//??

Enter 'YES' if you want equipment entries with a USE STATUS of 'OUT OF SERVICE' to appear on this PM worklist. Otherwise enter 'NO'.

Shall 'OUT OF SERVICE' equipment be included in worklist? YES// \< RET\> For what levels of CRITICALITY: ALL//??

This feature enables you to print a 'partial' PMI list, containing only those devices whose 'CRITICALITY' falls within a certain range.

For example, if your site ranks devices from 1 to 10 (10 being most critical) and circumstances are such that you only have resources for a limited number of PMIs in a given month, you may wish to enter something like '6-10'. This will mean that PMI's which would normally be scheduled for devices in the criticality range 1-5 will be suppressed, as will entries with 'CRITICALITY' greater than 10, but since your site only uses 1 thru 10 there shouldn't be any.

The system will not attempt to re-schedule these PMIs for the next month, because that would tend to defeat any efforts to balance the PM workload.

In short, this feature is not intended for routine use but rather as a systematic approach to dealing with an exceptional situation.

Entries must be in the form 'M-N' where M and N are integers in the range of

1 to 99 and M is less than or equal to N.

For what levels of CRITICALITY: ALL// \< RET\> For all shops? Yes//??

You may generate worklists for ALL shops or for ONE PARTICULAR shop. For all shops? Yes// \< RET\> (Yes)

DEVICE: HOME// 3 ENG PRINTER RIGHT MARGIN: 80//

Monthly PM List: BOILER PLANT Shop for 7/97 Printed: 07/14/97 Page 1 Order: CATEGORY (All)

Includes OUT OF SERVICE Equip. Responsible Tech: NUTT, Q.Q.

Entry \# Equipment Category Model Serial Number \[ROOM-BLDG-DIV (Wing)\] Manufacturer Equipment Name Local ID Status PM \# Manufacturer Service

Work Order Number

5 NONE 926929

A202D-01-JC FLAME FAILURE CONTROL IN USE 4410-0012 ENUSER2, TWO

Proc: Crit: Freq: A Level: N/A

PM-BP9707M-001 Initials: Date: Hours: (3) Cost:

PM Status (circle): P C D0 D1 D2 D3 Condition: LN G P Press \<RETURN\> to continue, '^' to escape...

Monthly PM List: PREV.MAINT. INSPECT Shop for 7/97 Printed: 07/14/97 Page 33 Order: CATEGORY (All)

Includes OUT OF SERVICE Equip. Responsible Tech: STAFF

Entry \# Equipment Category Model Serial Number \[ROOM-BLDG-DIV (Wing)\] Manufacturer Equipment Name Local ID Status PM \# Manufacturer Service

Work Order Number

195 AIR CONDITIONER (THRU WALL) 1234455533133334

AFFILIATED HOSPITAL PROD/SHAMP AUDIOLOGY AND SPEECH PATHOLO

Proc: Crit: Freq: BM Level: N/A IMPORTANT: Device MUST be isolated & rendered inoperative before servicing.

PM-PM9707M-001 Initials: Date: Hours: (5) Cost: (45)

PM Status (circle): P C D0 D1 D2 D3 Condition: LN G P Press \<RETURN\> to continue, '^' to escape...

#### Weekly PM List

GENERATE WEEKLY PM LIST(S)

VERSION 7

Select Month: JUL 1997// \< RET\> (JUL 1997)

Week number (enter an integer from 1 to 5, or '^' to escape): 1 Sort by: (E, P,I,L,C,S or ? for Help) L// C

For all EQUIPMENT CATEGORIES? Yes// \< RET\> (Yes)

Within CATEGORY, shall worklist be sorted by LOCATION? Enter Yes or No: YES// \< RET\>

Shall all LOCATIONS be included? YES// \< RET\>

Shall worklist be sorted by RESPONSIBLE TECHNICIAN? YES// \< RET\> For all TECH's:? Yes// \< RET\> (Yes)

Shall 'OUT OF SERVICE' equipment be included in worklist? YES// \< RET\> For what levels of CRITICALITY: ALL// \< RET\>

For all shops? Yes// \< RET\> (Yes)

DEVICE: HOME// 3 ENG PRINTER RIGHT MARGIN: 80//

Weekly PM List: BIOMEDICAL Shop for 7/97 Week: 1 07/14/97 Page 1 Order: CATEGORY (All)

Includes OUT OF SERVICE Equip. Responsible Tech: ENUSER2, THREE

Entry \# Equipment Category Model Serial Number \[ROOM-BLDG-DIV (Wing)\] Manufacturer Equipment Name Local ID Status PM \# Manufacturer Service

Work Order Number

| 7          | X-RAY GENERATOR \#A201 |                      | NONE    |         | NONE       |            |
|------------|------------------------|----------------------|---------|---------|------------|------------|
| \*173      |                        | HUMIDIFIER-MEDICAL   |         |         |            |            |
| IN USE     | 6515-5098              | PURITAN BENNETT CORP |         |         |            |            |
| Proc: 1234 |                        |                      | Crit: 8 | Freq: W | Level: N/A | JCAHO: YES |

PM-B9707W1-001 Initials: Date: Hours: (2) Cost:

PM Status (circle): P C D0 D1 D2 D3 Condition: LN G P Press \<RETURN\> to continue, '^' to escape...

18 580430 NONE

GE05-01-ET BRAIN LESION MAKER

IN USE 6640-5138 AUTOGENIC/CYBORG RESEARCH

Proc: BMET 004 Crit: Freq: W Level: N/A

PM-B9707W1-002 Initials: Date: Hours: (1) Cost: (100)

PM Status (circle): P C D0 D1 D2 D3 Condition: LN G P Press \<RETURN\> to continue, '^' to escape...

#### Delete PM Work Orders

Select Generate PM Schedule Option: delete PM Work Orders Which do you wish to delete?

1.  Individual work order(s), or
2.  An entire PM work list. Select 1 or 2:??

Enter '1' to delete individual PM work orders or '2' to delete a specific worklist (MONTHLY or WEEKLY) for an entire shop.

> **NOTE:** Deletion of PM work orders which have been closed out does NOT remove them from the equipment history.

#### Option 1 Individual work order(s)

Select 1 or 2: 1

Please enter first work order to be deleted??

Choose from:

PM-B9609M-001 PM-B9609M-002 PM-B9609M-003 PM-B9611M-001

PM-B9611M-002 221-114

PM-B9611M-003 221-114

PM-B9611M-004 301-110

PM-B9611M-005 221-114

Please enter first work order to be deleted PM-B9609M-001

PM-B9609M-001 Are you sure? Yes// \<RET\> (Yes)

> **NOTE:** You will be prompted to delete each successive work order. If you enter

\<RET\> the work order will be deleted. Enter an ^ to exit from the option.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Next work order: PM-B9609M-002//</th>
<th>&lt;RET&gt;</th>
<th>(Yes)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">Next work order: PM-B9609M-003//</td>
<td>^</td>
<td></td>
</tr>
<tr class="even">
<td><p>1</p>
<p>2</p>
<p>3</p></td>
<td><p>Monthly PM List Weekly PM List</p>
<p>Delete PM Work Orders</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Option 2 An Entire PM Work List

Select Generate PM Schedule Option: 3 Delete PM Work Orders Which do you wish to delete?

1.  Individual work order(s), or
2.  An entire PM work list. Select 1 or 2: 2

Select ENGINEERING SECTION LIST: 35 BIOMEDICAL

Select Month: JUL 1997// \< RET\> (JUL 1997) MONTHLY or WEEKLY PM list: MONTHLY//??

A MONTHLY PMI list contains work orders for ANNUAL, SEMI-ANNUAL, QUARTERLY, BI-MONTHLY, and MONTHLY preventive maintenance inspections.

A WEEKLY PMI list is for WEEKLY and BI-WEEKLY inspections.

MONTHLY or WEEKLY PM list: MONTHLY// WEE \[ *This prompt is case sensitive*\] Which week? 1

This option will delete the entire WEEKLY PM List of the BIOMEDICAL Shop for JULY, 1997 (Week 1).

Just a moment, please...

There are 2 PM work orders on this list. Deletion of these work orders will

not affect equipment histories. Are you sure you want to proceed? Yes// \< RET\> (Yes) Requested Start Time: NOW// \< RET\> (JUL 14, 1997@10:50:42)

### Record Equipment PMI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment P MI ...                          |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

This option is used to close out PM worklists, by specific entry or by worklist. It is also used to record a PMI on a given device. The option has a seven-item sub menu. Due to the complexity of the bar code process, the fourth and fifth options are explained in detail in the Attachments section of this manual. The remaining options are presented with actual examples.

1.  Close Out PM Work Orders
2.  Rapid Closeout of PM Work Orders
3.  Record Single Device PMI
4.  Bar Coded PMI Functions
5.  Upload Data from MedTester
6.  Rapid Deferral of PM Worklist
7.  Print PM Manhours

Close Out PM Work Orders

Close out a PM work list entry by entry. User is asked for a complete specification of the first PM work order; after that the system assumes the shop, month, and type (MONTHLY or WEEKLY) of work list.

Rapid Closeout of PM Work Orders

Closes out an entire PM worklist. User is prompted for any PM work orders that are to be closed out individually. All work orders on the specified list which are not closed out individually will be assigned a PM status of PASSED and default values (if any) for time and materials. This option may take a while to run, so the user is given the opportunity to free his terminal. Freeing the terminal causes this option to begin to run immediately as a background job. This option may slow the system noticeably and it may be desirable to assign this task a lower priority than interactive jobs.

Record Single Device PMI

May be used to record a PMI on any specified device, regardless of whether or not it is on an active PMI list. One use envisioned for this is recording the results of area sweeps. If the specified device is in the scheduled PMI program and it appears that a PMI recorded via this option may make it desirable to change the scheduled FREQUENCY or the STARTING MONTH, the user will be afforded an opportunity to do so.

Bar Coded PMI Functions

Driver for bar coded Preventive Maintenance functions. Will prompt you too either.

\(1\) download a data acquisition program to a bar code reader,

\(2\) upload collected data from a bar code reader, or

\(3\) restart processing of a previously uploaded data set.

Upload Data from MedTester

Reads data from MedTester (Electrical Safety Analyzer manufactured by Dynatech Nevada, Inc.) and posts electrical safety inspections to Equipment Histories.

Rapid Deferral of PM Worklist

Defers all entries on a user specified PM worklist. All work orders on subject worklist are given a PM Status of DEFERRED and a close out date of TODAY. Time and Materials are not posted. This option is intended to be run only if you want to post DEFERRALs of all open line items (PM work orders) on subject worklist to Equipment Histories.

This option is not intended for use in cases where there is some expectation that you may wish to otherwise close-out the PM worklist in question at some later date. That is to say, once a scheduled preventive maintenance inspection task has been recorded as DEFERRED it will be difficult to change it to PASSED.

Print PM Manhours

Prints total manhours expended on preventive maintenance by shop and by month for each technician. These manhours are automatically recorded when PM work orders are closed out.

#### Close Out PM Work Orders

Select Record Equipment PMI Option: 1 Close Out PM Work Orders

The following prompt only appears if the site parameter option field "DELETE PM WORK ORDERS?" is null. If the site parameter option field has been set to No or Yes, this prompt is bypassed.

Should PM work orders be deleted after close out? YES// ??

Deletion of PM work orders after they have been closed out is recommended for sites that are short on disk space. The results of the PMI will be posted to the equipment history file before the PM work order is deleted.

If disk space is not a problem, then you may wish to retain PM work orders in accordance with your established archive criteria. In this way, the Work Order \# File will reflect scheduled as well as unscheduled workload.

For estimating purposes, each PM work order will consume about 300 bytes of disk space (or about 3 such work orders per block).

Should PM work orders be deleted after close out? YES// N

Please enter first PM work order to be closed: PM-B9611M-009 201-114

WORK ORDER \#: PM-B9611M-009// \<RET\> REQUEST DATE: NOV 7,1996// \<RET\> LOCATION: 201-114// ??

Physical location where work is to be performed.

Choose from:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>100-110-JC</th>
<th>110</th>
<th>CCU</th>
<th>MEDICINE</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><p>101-148</p>
<p>102-148</p>
<p>103-110-JC</p></td>
<td rowspan="2"><p>148</p>
<p>148</p>
<p>110</p></td>
<td><p>C</p>
<p>C</p></td>
<td colspan="2" rowspan="2"><p>EXAM/TREATMENT ROOM</p>
<p>EXAM/TREATMENT ROOM MEDICINE</p></td>
</tr>
<tr class="even">
<td>CCU</td>
</tr>
<tr class="odd">
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">LOCATION: 201-114//</td>
<td>201-114</td>
<td>114</td>
<td>INFORMATION SYSTEMS CENTER</td>
</tr>
</tbody>
</table>

OFFICE

Select ASSIGNED TECH: ENUSER, FOUR// ??

1 ENUSER, FOUR

Engineering employee(s) assigned to this work order.

Choose from: ENUSER, TWO ENUSER , THREE ENUSER , FOUR

Select ASSIGNED TECH: ENUSER, FOUR// \<RET\> ASSIGNED TECH: ENUSER , FOUR// \<RET\> HOURS: .8// ??

Number of hours (to the nearest tenth) spent on this work order by this employee.

HOURS: .8// \<RET\>

SHOP: BIOMEDICAL// \<RET\>

Select ASSIGNED TECH: \<RET\>

Select WORK ACTION: PREVENTIVE MAINTENANCE// ??

1 PREVENTIVE MAINTENANCE Type of work performed or requested.

Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3

^

Select WORK ACTION: PREVENTIVE MAINTENANCE// \<RET\>

PM STATUS:??

Outcome of preventive maintenance inspection. Useable for PM work orders only.

Choose from:

P PASS

C CORRECTIVE ACTION TAKEN/REQUESTED D0 DEFERRED

D1 DEFERRED, COULD NOT LOCATE

D2 DEFERRED, IN USE

D3 DEFERRED, OUT OF SERVICE OR LOANED OUT PM STATUS: \<RET\>

TOTAL MATERIAL COST: ??

Approximate cost of materials needed to complete this task.

TOTAL MATERIAL COST: \<RET\>

VENDOR SERVICE COST: ??

Approximate cost of vendor services needed to complete this task.

VENDOR SERVICE COST: \<RET\>

WORK PERFORMED (140 char max): QUARTERLY PMI HOSPITAL BEDS

Replace \<RET\>

CONDITION CODE: ??

Condition code of equipment is normally determined by an Engineering technician and entered during close out of a work order. The code is:

1)  LIKE NEW - Like new condition, good performance record, low service cost.
2)  GOOD - Middle of service life, fair performance record, increasing service cost.
3)  POOR - Approaching end of service life, poor performance record, high service cost, consider budgeting for replacement.

Choose from:

1.  LIKE NEW
2.  GOOD
3.  POOR

CONDITION CODE: \<RET\>

DATE COMPLETE (or closed): APR 9,1997// ??

Next work order: PM-B9611M-010// ^

Work orders are automatically generated for failed preventive maintenance inspections if the preventive maintenance is recorded via bar code reader or electrical safety analyzer. If being done manually, the user will be prompted for the creation of a regular work order.

At this point, the user is returned to the Record Equipment PMI menu.

#### Rapid Closeout of PM Work Orders

Select Record Equipment PMI Option: 2 Rapid Closeout of PM Work Orders Select Worklist Month: JUL 1997// \< RET\> (JUL 1997)

Select ENGINEERING SECTION LIST: 22 AIR CONDITIONING MONTHLY or WEEKLY PM List: MONTHLY// \< RET\>

COMPLETION DATE (future dates will not be accepted). MONTH and YEAR are required, DAY is optional: JUL 1997// \< RET\> (JUL 1997)

Do you wish to substitute one technician for another? NO//??

If all of the work assigned to TECHNICIAN A has actually been done by TECHNICIAN B then you should enter 'YES' at this point and then 'Replace' TECHNICIAN A 'With' TECHNICIAN B.

Do you wish to substitute one technician for another? NO// \< RET\>

This option will scan the MONTHLY PM Worklist of the AIR CONDITIONING Shop for JULY, 1997. It will automatically assign a PM Status of 'PASSED.'

and a completion date of JUL 1997 to each work order on the list, except for those that you close out individually.

Default values for labor and material costs (if any) from the Equipment File will be posted to the Equipment History during Rapid Close Out.

Are you sure you want to proceed? No// y (Yes)

Please enter any PM work orders (or the sequential portion thereof) that you wish to close out individually. Press \<RETURN\> to terminate the process.

Work order (ex: 'PM-A9707M-001' or just '1'):?? Choose from:

PM-A9707M-001 A208-01-JC

PM-A9707M-002 A212-01-JC

Please enter an existing PM work order, or the sequential portion thereof. If there are no work orders to be closed out individually, enter \<cr\>.

Would you like a list of existing work orders? Yes// \< RET\> (Yes) PM-A9707M-002

Work order (ex: 'PM-A9707M-001' or just '1'): PM-A9707M-002

WORK ORDER \#: PM-A9707M-002// REQUEST DATE: JUL 14,1997// LOCATION: A212-01-JC//

Select ASSIGNED TECH: ENUSER2, FOUR//

ASSIGNED TECH: ENUSER2, FOUR// HOURS: .5//

SHOP: AIR CONDITIONING// Select ASSIGNED TECH:

Select WORK ACTION: PREVENTIVE MAINTENANCE// PM STATUS:

TOTAL MATERIAL COST: 20// VENDOR SERVICE COST:

WORK PERFORMED (140 char max): MONTHLY PMI Level 1,2,3

Replace CONDITION CODE:

DATE COMPLETE (or closed): JUL 14,1997//

Next work order (or sequential portion), \<RETURN\> to quit: \< RET\>

The following work orders will be unaffected by Rapid Close Out: PM-A9707M-002

All other work orders on the MONTHLY PM list for the AIR CONDITIONING Shop for JULY, 1997 are subject to Rapid Close Out.

Would you like to specify starting and stopping points for?

Rapid Close Out? No//??

If you want to close out only a portion of a PM worklist, you may specify the first and last work orders that you want Rapid Close Out to operate on.

> **NOTE:** Rapid Close Out will close the first and the last and everything in between.

Would you like to specify starting and stopping points for Rapid Close Out? No// \< RET\> (No)

Would you like to free up this terminal? Yes// n (No)

#### Record Single Device PMI

Select Record Equipment PMI Option: 3 Record Single Device PMI Select ENGINEERING SECTION LIST: ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF

Select Month: APR 1997// \<RET\> (APR 1997)

Are you recording a WEEKLY PMI? No// \<RET\> (No)

Do you want to retain PM work orders in your Work Order File after they have been posted to the Equipment History? No// ??

This prompt only appears if the site parameter option field "DELETE PM WORK ORDERS?" is null. If the site parameter option field has been set to No or Yes, this prompt is bypassed.

Deletion of PM work orders after they have been closed out is recommended for sites that are short on disk space. The results of the PMI will be posted to the equipment history file before the PM work order is deleted.

If disk space is not a problem, then you may wish to retain PM work orders in accordance with your established archive criteria. In this way, the Work Order \# File will reflect scheduled as well as unscheduled workload.

For estimating purposes, each PM work order will consume about 300 bytes of disk space (or about 3 such work orders per block).

Do you want to retain PM work orders in your Work Order File after they have been posted to the Equipment History? No// Y (Yes)

Select EQUIPMENT ENTRY \#: 50

1.  50 91120508 BED (ONE WARD) TURNED IN
2.  50 MHZ EISA PC 8 AB34300UER COMPUTER-PC-ADMINISTRATIVE T URNED IN

CHOOSE 1-2: 2 8

WORK ORDER \#: PM-OC9704M-002// ??

Identifier of each individual work action. Composed of the shop abbreviation, date generated, and a computer-generated sequential component. Users may delete work orders when necessary, but they should never change a work order number.

WORK ORDER \#: PM-OC9704M-002// \<RET\> REQUEST DATE: APR 9,1997// \<RET\> LOCATION: 301-110// ??

Physical location where work is to be performed.

Choose from:

100-110-JC 110

101-148 148

102-148 148

^

CCU MEDICINE

C EXAM/TREATMENT ROOM

C EXAM/TREATMENT ROOM

LOCATION: 301-110// \<RET\>

Select ASSIGNED TECH: ENUSER, FOUR// ??

1 ENUSER, FOUR

Engineering employee(s) assigned to this work order.

Select ASSIGNED TECH: ENUSER, FOUR// \<RET\> ASSIGNED TECH: ENUSER , FOUR// \<RET\> HOURS: .8// ??

Number of hours (to the nearest tenth) spent on this work order by this employee.

HOURS: .8// \<RET\>

SHOP: BIOMEDICAL// ??

Engineering section under whose direction this work was performed.

SHOP: BIOMEDICAL// \<RET\>

Select ASSIGNED TECH: \<RET\>

Select WORK ACTION: PREVENTIVE MAINTENANCE// ??

1 PREVENTIVE MAINTENANCE Type of work performed or requested.

Choose from:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3

^

Select WORK ACTION: PREVENTIVE MAINTENANCE// \<RET\>

PM STATUS:??

Outcome of preventive maintenance inspection. Useable for PM work orders only.

Choose from:

P PASS

C CORRECTIVE ACTION TAKEN/REQUESTED D0 DEFERRED

D1 DEFERRED, COULD NOT LOCATE

D2 DEFERRED, IN USE

D3 DEFERRED, OUT OF SERVICE OR LOANED OUT PM STATUS: \<RET\>

TOTAL MATERIAL COST: ??

Approximate cost of materials needed to complete this task.

TOTAL MATERIAL COST: \<RET\>

VENDOR SERVICE COST: ??

Approximate cost of vendor services needed to complete this task.

VENDOR SERVICE COST: \<RET\>

WORK PERFORMED (140 char max): OFF-SCHEDULE PMI// ??

Brief description of work actually performed (may be extracted from COMMENTS field). The WORK PERFORMED field will be saved in the EQUIPMENT (Inventory) File (No. 6914) where it will be a permanent part of the device history. In contrast, the COMMENTS field will be removed from disk (on-line) storage when the work order is archived.

WORK PERFORMED (140 char max): OFF-SCHEDULE PMI// \<RET\>

CONDITION CODE: ??

Condition code of equipment is normally determined by an Engineering technician and entered during close out of a work order. The code is:

1)  LIKE NEW - Like new condition, good performance record, low service cost.
2)  GOOD - Middle of service life, fair performance record, increasing service cost.
3)  POOR - Approaching end of service life, poor performance record, high service cost, consider budgeting for replacement.

Choose from:

1.  LIKE NEW
2.  GOOD
3.  POOR

CONDITION CODE: \<RET\>

DATE COMPLETE (or closed): APR 9,1997// \<RET\>

#### Bar Coded PMI Functions

| 1   | Download PM Program to Portable Bar Code Reader |
|-----|-------------------------------------------------|
| 2   | Upload Data from Portable Bar Code Reader       |
| 3   | Restart Processing of Bar-Coded PMI             |

#### Bar Coded PMI Functions Option 1. Download PM Program to Portable Bar Code Reader

Select Bar Coded PMI Functions Option: 1 Download PM Program to Portable Bar Code Reader

Select PM Inspector: ??

Choose from: ENUSER, TWO ENUSER , THREE ENUSER , FOUR ENUSER , F IVE

Select PM Inspector: ENUSER, FOUR

OK, enter the device to which the bar code reader is connected. DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

\### WARNING: When a program is sent to the barcode reader, ALL DATA stored on the barcode reader will be LOST! Make sure that previous users of this barcode reader have no need for data, if any, that might exist on the reader.

Please follow the following steps:

1)  If you have not already done so, you may now connect up the barcode reader to the output device.
2)  After you have connected the barcode reader to the device, clear the barcode reader by turning the reader off and back on.
3)  After you have completed the above steps, press the return.

key to start sending the program to the barcode reader. If you want to abort this option, enter a ^ and return.

OK, you must now enter either a return ...

... or an '^' return:

Download time: 8 sec.

#### Bar Coded PMI Functions Option 2. Upload Data from Portable Bar Code Reader

Select Bar Coded PMI Functions Option: 2 Upload Data from Portable Bar Code Reader Enter the device to which the bar code reader is connected.

Device: TRAKKER RM 221

\>\>\>Use the TRANSMIT option on the bar code reader to start sending data: Thank you. Data is now being received....

OK, you are loading data on APR 28, 1993@13:03:15...

... using the BAR CODE program PREVENTIVE MAINTENANCE

Reading bar code reader....

...........

Data transmission complete. Number of records read: 12.

For which month do you wish to record PMI's: APR 1993//2-93 (FEB 1993)

Are you recording a MONTHLY (as opposed to a WEEKLY) worklist? YES// (YES) Select ENGINEERING SECTION LIST: BIOMEDICAL

Should existing PM work orders be deleted after close out? YES// (YES)

The system is now ready to update the Equipment File on the basis of data acquired from the portable bar code reader.

Data that cannot be processed normally will be reported as Exception Messages. These messages will provide notification of such things as missing bar code labels and database inconsistencies.

Exception Messages will also be printed for devices that FAIL their PM inspection. Regular work orders will be automatically generated. The PM work order will be closed with a reference to the regular work order.

You must now select a hard copy device (printer) to receive PMI Exception Messages.

You may enter the letter 'Q' and then select a device if you wish to schedule this data processing task for some later time.

Select Device for PMI Exception Messages: HOME//

BAR CODED PMI EXCEPTION MESSAGES APR 28, 1993

Global Reference: ^PRCT (446.4,4,2,1,1, Page 1

Equipment Entry \#5 FAILED PMI. CORRECTIVE ACTION REQUIRED.

Label scanned as: 999 EE5 Location: 25-7A PM work order PM-B9304M-001 is being closed out.

Regular work order B930308-001 is open.

Problem description: UNIT INOPERATIVE. REPAIR IN PROGRESS. (Time: .2 hrs)

PM Work Order already posted for Equipment ID#: 6 Label scanned as: 999-EE6 Location: 25-7A.

Equipment Entry \# 4 FAILED PMI. CORRECTIVE ACTION REQUIRED.

Label scanned as: 999EE4 Location: 25-7A PM work order PM-B9304M-003 is being closed.

Regular work order B930428-002 has been generated.

Problem Description: KNOB MISSING. PARTS NEEDED. (Time: .7 hrs)

#### Bar Coded PMI Functions Option 3. Restart Processing of Bar-Coded PMI

Select Bar Coded PMI Functions Option: 3 Restart Processing of Bar-Coded PMI Enter PROCESS ID: ENPM

Enter TIME STAMP of process to be restarted: 2930428.140043.

For which month do you wish to record PMI's: MAY 1993//4-93 (APR 1993)

Are you recording a MONTHLY (as opposed to a WEEKLY) worklist? YES// (YES) Select ENGINEERING SECTION LIST: BIOMEDICAL

Should existing PM work orders be deleted after close out? YES//

The system is now ready to update the Equipment File on the basis of data acquired from the portable bar code reader.

Data that cannot be processed normally will be reported as Exception Messages. These messages will provide notification of such things as missing bar code labels and database inconsistencies.

Exception Messages will also be printed for devices that FAIL their PM inspection. Regular work orders will be automatically generated. The PM work order will be closed with a reference to the regular work order.

You must now select a hard copy device (printer) to receive PMI Exception Messages.

You may enter the letter 'Q' and then select a device if you wish to schedule this data processing task for some later time.

Select Device for PMI Exception Messages: HOME// LAN

Further information on Bar Code PMIs can be found in the Attachments section of this manual.

#### Upload Data from MedTester

Select Record Equipment PMI Option: 5 Upload Data from MedTester Enter the device to which the MedTester is connected.

DEVICE: MED MEDTESTER RM 221

...OK, use the MedTester 'PALL' function to send the data. Please

be sure that you are connected to a MedTester COMM port and that the MedTester PRINTER port is OFF..............................

MedTester UPLOAD MODULE:

Should data from the MedTester be used to close out work orders on a PM worklist? YES//?

If MedTester is being used in conjunction with a specific Preventive Maintenance worklist, you should answer 'YES' to this question. You will then be asked to identify the worklist.

If you say 'NO' at this point, safety tests stored in the MedTester will be posted to the Equipment Histories without affecting a PM worklist in any way.

Press \<RETURN\> to continue...

MedTester UPLOAD MODULE:

Should data from the MedTester be used to close out work orders on a PM worklist? YES// (YES)

For which month do you wish to record PMI's: APR 1993// (APR 1993)

Are you recording a MONTHLY (as opposed to a WEEKLY) worklist? YES// (YES) Select ENGINEERING SECTION LIST: BIOMEDICAL

Should existing PM work orders be deleted after close out? YES//

The system is now ready to update the Equipment File on the basis of data acquired from the MedTester.

If the system encounters data that cannot be processed in the normal fashion it will give you written notice in the form of a MedTester Exception Message.

These messages will provide notification of such things as test failures and database inconsistencies.

If a device fails a MedTester test sequence, the site is expected to evaluate the failure and issue a regular work order for corrective action. If a PM work order exists for such a device and if you have elected to use MedTester data to close out that worklist, then the PM status will be set to 'CORRECTIVE ACTION TAKEN/REQUESTED' but the PM work order will remain open, and nothing will be posted to the Equipment History. Once corrective action

has been taken, then the PM work order should be closed out manually. The WORK PERFORMED field should contain a reference to the regular work order.

You will soon select a hard copy device (printer) to receive MedTester Exception Messages, but first we need to know whether or not you want paper copies of the actual test results.

Do you want a paper copy of test results (will print on same device as Exception Messages)? NO// Y (YES)

Select Device for EXCEPTION MESSAGES: HOME// ^& WORK BENCH RIGHT MARGIN: 80// DO YOU WANT YOUR OUTPUT QUEUED? NO// (NO)

MedTester REC \#4

SEQUENCE: 5 DATE: 11/20/92 TIME: 6:23:32

OPERATOR CODE: 1

DEVICE INFORMATION (\* Item not found in Equipment File \*) TYPE: MANF: LOC: 201-114

MODEL: SN: CN: 6515-5419

PHYSICAL INSPECTION LOVELY

| LINE VOLTAGES      |        |      |        |           |
|--------------------|--------|------|--------|-----------|
| L1-L2              | L1-GND |      | L2-GND |           |
| 124.7              |        | .7   | 125.2  | VOLTS RMS |
| GROUND RESISTANCE: | .010   | OHMS |        |           |

LEAKAGE TESTS, EQUIPMENT POWER OFF

CASE EXT LEAD, NORM POL, CLSD GND .0 uAMPS RMS

CASE EXT LEAD, NORM POL, OPEN GND 93.9 uAMPS RMS

CASE EXT LEAD, REV POL, OPEN GND 96.7 uAMPS RMS LEAKAGE TESTS, EQUIPMENT POWER ON

CASE EXT LEAD, REV POL, OPEN GND 96.3 uAMPS RMS

CASE EXT LEAD, NORM POL, OPEN GND 94.9 uAMPS RMS

CASE EXT LEAD, NORM POL, CLSD GND .1 uAMPS RMS EUT CURRENT DRAWN: .2 amps

COMMENTS: NOTHING FURTHER NEXT TEXT DUE DATE:

LOOK-UP ON EQUIPMENT FILE FAILED.

Control Number: 6515-5419 Location: 201-114 Attempt was by PM#: 6515-5419

Further information on using the MedTester can be found in the Attachments section of this manual.

#### Rapid Deferral of PM Worklist

Select Record Equipment PMI Option: 6 Rapid Deferral of PM Worklist Select Month: APR 1997// \<RET\> (APR 1997)

Select ENGINEERING SECTION LIST: ??

Choose from:

1.  OFFICE OF THE CHIEF
2.  ADMIN.+CLER.
3.  SUPERVISORY OPERAT.
4.  UTILITY OPERATIONS

^

Select ENGINEERING SECTION LIST: OFFICE OF THE CHIEF MONTHLY or WEEKLY PM List: MONTHLY// ??

A MONTHLY PMI list contains work orders for ANNUAL, SEMI-ANNUAL, QUARTERLY, BI-MONTHLY, and MONTHLY preventive maintenance inspections.

A WEEKLY PMI list is for WEEKLY and BI-WEEKLY inspections. MONTHLY or WEEKLY PM List: MONTHLY//

Should PM work orders be deleted after close out? YES// ??

Deletion of PM work orders after they have been closed out is recommended for sites that are short on disk space. The results of the PMI will be posted to the equipment history file before the PM work order is deleted.

If disk space is not a problem, then you may wish to retain PM work orders in accordance with your established archive criteria. In this way, the Work Order \# File will reflect scheduled as well as unscheduled workload.

For estimating purposes, each PM work order will consume about 300 bytes of disk space (or about 3 such work orders per block).

Should PM work orders be deleted after close out? YES// N

This option will scan the MONTHLY PM Worklist of the OFFICE OF THE CHIEF Shop for APRIL, 1997.

It will automatically assign a PM Status of 'DEFERRED' and a close out date of APR 9,1997 to each work order on the list.

Default values for labor and material costs (if any) from the Equipment File will NOT be posted to the Equipment History during RAPID DEFERRAL.

Are you sure you want to proceed? No// Y (Yes)

Would you like to specify starting and stopping points for Rapid Deferral? No// ??

If you want to defer only a portion of a PM worklist, you may specify the first and last work orders that you want Rapid Deferral to operate on.

Everything between and including these two work orders will be DEFERRED. Please enter the entire work order numbers (ex: 'PM-E9702M-102').

Would you like to specify starting and stopping points for Rapid Deferral? No// \<RET\> (No)

Would you like to free up this terminal? Yes// N (No) Rapid deferral now in progress.

If you want to defer only a portion of a PM worklist, you may specify the first and last work orders that you want Rapid Deferral to operate on. Everything between and including these two work orders will be DEFERRED. Please enter the entire work order numbers (ex: "PM-E9302M-102").

There is no further screen display at this point.

The user is returned to the Record Equipment PMI menu.

#### Print PM Manhours

Select Record Equipment PMI Option: 7 Print PM Manhours

- Previous selection: ENGINEERING SECTION not null START WITH ENGINEERING SECTION: FIRST// ??

Engineering Shop or Receiving Area for electronic work orders. Receiving Areas should be numbered so that they end with 90 thru 99, inclusive (ex: 90,91,190,295, etc.). Working shops should not be given numbers within the range reserved for Receiving Areas.

- Previous selection: ENGINEERING SECTION not null START WITH ENGINEERING SECTION: FIRST// \<RET\>
- Previous selection: PM MONTH not null

START WITH PM MONTH: FIRST// ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. You may omit the precise day, as: JAN, 1957

- Previous selection: PM MONTH not null START WITH PM MONTH: FIRST// \<RET\>

DEVICE: \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

PREVENTIVE MAINTENANCE MANHOURS APR 9,1997 16:16 PAGE 1

PM MONTH TECHNICIAN MANHOURS

ENGINEERING SECTION: BIOMEDICAL

| DEC 1993 | ENUSER, F IVE | 0.80   |
|----------|---------------|--------|
| JUN 1995 | ENUSER, TEN   | 0.80   |
| MAY 1996 | ENUSER, FOUR  | 268.00 |
| JUL 1996 | ENUSER, FOUR  | 160.00 |
| NOV 1996 | ENUSER, FOUR  | 2.40   |
| DEC 1996 | ENUSER, TEN   | 0.60   |
| FEB 1997 | ENUSER, FOUR  | 2.40   |

PREVENTIVE MAINTENANCE MANHOURS APR 9,1997 16:16 PAGE 2

PM MONTH TECHNICIAN MANHOURS

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 47%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>APR 1997</th>
<th>ENUSER, TEN ENUSER , FOUR</th>
<th><p>1.00</p>
<p>0.80</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAY 1997</td>
<td>ENUSER, FOUR</td>
<td>804.00</td>
</tr>
<tr class="even">
<td>NOV 1997</td>
<td>ENUSER, FOUR ENUSER , S IX</td>
<td><p>0.00</p>
<p>0.00</p></td>
</tr>
<tr class="odd">
<td>APR 1998</td>
<td>ENUSER, TEN</td>
<td>1.60</td>
</tr>
</tbody>
</table>

ENGINEERING SECTION: ELECTRIC

NOV 1997 ENUSER1, ONE 0.00

### Print Bar Code Labels for Equipment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

Select Equipment Management Option: 9 Print Bar Code Labels for Equipment Management

Select Equipment Labels Option:

1.  Equipment Labels
2.  Location Labels

The Print Bar Code Labels for Equipment Management option allows users to print bar code equipment or location labels for different sort categories. The labels may be printed with a companion listing which lists the sort of category, description, manufacturer, model, and related information.

#### Equipment Labels

1.  Equipment Category Bar Code Labels
2.  CMR Bar Code Labels (EQUIPMENT)
3.  Bar Code Labels by PM Number
4.  Bar Code Labels by General Location (WING)
5.  Bar Code Labels by Specific Location (ROOM)
6.  Single Device Bar Code Label
7.  Equipment Labels by Equipment ID#
8.  Bar Code Labels in Conjunction with PM Worklist
9.  Bar Code Labels for a Purchase Order
10. Bar Code Labels by LOCAL ID
11. Bar Code Labels by Using Service

Equipment Category Bar Code Labels

Prints bar coded equipment labels for all pieces of equipment in specified category.

CMR Bar Code Labels (EQUIPMENT)

Prints bar code labels for all equipment on a specified CMR.

Bar Code Labels by PM Number

Prints bar coded equipment labels for a specified range of Property Management numbers.

Bar Code Labels by General Location (WING)

Prints bar code labels for each piece of equipment located on a specified wing, where wing is taken from the Space file (#6928).

Bar Code Labels by Specific Location (ROOM)

Prints bar code labels for each piece of equipment in a specified room. Sites must be using the Space file (#6928) in order to profit from using this option.

Single Device Bar Code Label

Print bar code label for one specific piece of equipment.

Equipment Labels by Equipment ID#

Prints bar coded equipment labels for each and every entry in the Equipment Inv. file.

Bar Code Labels in Conjunction with PM Worklist

Prints bar coded equipment labels for each piece of equipment on a monthly PM worklist. User specifies the worklist by responding to prompts for date (month and year only) and shop.

Bar Code Labels for a Purchase Order

Prints a bar coded equipment label for each item on a specific purchase order.

Bar Code Labels by LOCAL ID

Prints equipment labels for a range of local identifiers.

Bar Code Labels by Using Service

Prints bar coded equipment labels for all devices that are identified in the Equipment Inv. file as belonging to a particular service.

#### 1 Equipment Category Bar Code Labels

The first sub option of the Equipment Labels option, Equipment Category Bar Code Labels, is used to illustrate the option.

Select Equipment Labels Option: 1 Equipment Category Bar Code Labels New labels only? YES//??

The system records the printing of equipment bar code labels. If you do not wish to have labels printed again if they have already been printed at least once, please enter 'YES' at this time.

Select Equipment Labels Option: 1 Equipment Category Bar Code Labels New labels only? YES// Y

Would you like a companion listing for this set of labels? YES// \< RET\> (YES) Select PRINTER for Companion Listing:??

The following information is available: All Printers

Complete Device Listing Extended Help \[UNAVAILABLE\]

Select one (A, P,C,D, or E): P INTERMEC8646 COMPUTER ROOM LASER2FL SECOND FLOOR LASER2FP 2ND FLOOR OFFICES

LASERP LOUNGE LASERTJ TRAILER

LASERTL TRAILER LASERTP DEVELOPMENT PRINTER TRAILER COMPRESSED PRINT

Select PRINTER for Companion Listing: LASERTP DEVELOPMENT Select EQUIPMENT CATEGORY NAME:?

ANSWER WITH EQUIPMENT CATEGORY NAME CHOOSE FROM:

DEFIBRILLATOR

DISPLAY CENTRAL STATION ELECTROCARDIOGRAPH

PUMP PERFUSION STAMP TIME-DATE

Select EQUIPMENT CATEGORY NAME: DEFIBRILLATOR

Sort labels by LOCATION? YES// (YES) Select BARCODE PRINTER: LASERTP DEVELOPMENT DO YOU WANT YOUR OUTPUT QUEUED? NO// (NO)

If a site loads the Engineering package without using the Engineering Site Parameters option, the following label is produced.

![](en-version-7-user-manual/002.png)

A companion listing for a label of this type follows:

COMPANION LISTING (Bar Code Labels) Page 1

CMR 112 (ENUSER2, FIVE) FEB 22, 1990@14:50

Equip ID \*Description\*

60

Man: HEWLETT PACKARD

Model: 1518LP Servc: SURGICAL

Location: 4D WEST

DEFIBRILLATOR (LINE POWERED) Cat: DEFIBRILLATOR S/N: 999

Status: IN USE PM#: 7530-9876

If a site runs the Engineering Site parameters Enter/Edit option to customize bar code labels, a label of the following type is produced.

![](en-version-7-user-manual/003.png)

#### Location Labels

The Location Labels sub option of the Print Bar Code Labels for Equipment Management option prints bar code labels sorted by location. The format for the labels is essentially the same. The ROOM Bar Code Label will be used to illustrate this option.

Select Print Bar Code Labels for Equipment Management Option: 2 Location Labels

| 1   | WING Bar Code Labels          |
|-----|-------------------------------|
| 2   | BUILDING Bar Code Labels      |
| 3   | ROOM Bar Code Label           |
| 4   | ALL Bar-Coded Location Labels |

WING Bar Code Labels

Prints bar code location labels for all rooms in a specified wing, where wing is as defined in the Space file (#6928).

BUILDING Bar Code Labels

Prints bar code location labels for all rooms in a specified building, where building is taken to be the second piece (with "-"as delimiter) of the Name field from the Space file (#6928).

ROOM Bar Code Label

Prints bar code label for specified room. Room in question must first exist in the Space file (#6928).

ALL Bar-Coded Location Labels

Prints bar code labels for all entries in the Space file (#6928).

Option 3 is used to illustrate the creation of location labels.

3\. ROOM Bar Code Labels

Select Location Labels Option: 3 ROOM Bar Code Labels Select ENG SPACE ROOM NUMBER:?

ANSWER WITH ENG SPACE ROOM NUMBER, OR WING CHOOSE FROM:

102-114 114 4D-WEST

102A-114 114

Select ENG SPACE ROOM NUMBER: 102A-114 114

Select BARCODE PRINTER: XXXX

DO YOU WANT YOUR OUTPUT QUEUED? NO// (NO)

If a site loads the Engineering package without using the Engineering Site Parameters option, the following label is produced. If the SPACE FUNCT ON LOCATION LABEL? parameter has been set to “YES” the first 20 characters of the space function will be printed instead of “\*LOCATION LABEL\*”

![](en-version-7-user-manual/004.png)

### Bar Coded Equipment Inventory Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

Two types of bar code labels are necessary for equipment management. They are commonly referred to as *location labels* and *equipment labels*. The Engineering package contains software to generate both types. To conduct a CMR (Consolidated Memorandum of Receipt) inventory, users will scan a location label (affixed to a door frame) and then scan the equipment labels on every piece of equipment in that physical location. When all the equipment in a given room has been scanned, the user will scan the location label again to "close out" that location. The user will then move to the next room and repeat the process. At some point, the user will upload data from the portable bar code reader into VISTA. The Engineering package will automatically use the data to update individual records in the Equipment Inv. file.

The package expects that a Trakker Model 9440 (or equivalent) portable bar code reader will be used for bar code-based equipment inventory and for bar code based preventive maintenance inspections.

Two programs are included which may be downloaded from VISTA to the Trakkers. One is for equipment inventory; the other is for preventive maintenance. These programs are written in a language called IRL (Interactive Reader Language), which is the native instruction set for this brand of portable bar code reader.

The IRL programs (to be downloaded to the Trakkers) and actual data sets (once they have been uploaded from the Trakkers) are both stored in the same file. The file is called Barcode Program (File \#446.4). This file, together with all software necessary for uploading and downloading, is included in the Engineering package.

The Bar-Coded Equipment Inventory Management options include:

1.  Download NX Program to Portable Bar Code Reader
172. Upload Data from Portable Bar Code Reader
173. Inventory Exception Listing
174. Manual Update of Equipment Inventory
175. Restart Processing of Uploaded NX Inventory Data

Download NX Program to Portable Bar Code Reader

Downloads an IRL (Interactive Reader Language) program to a portable bar code reader.

Upload Data from Portable Bar Code Reader

Calls a routine that causes a portable bar code reader to upload its data to VISTA.

Inventory Exception Listing

Produces a list of those items on a specified CMR that have not been located in the course of a physical inventory.

Manual Update of Equipment Inventory

Uses FileMan to update physical inventory data on individual entries in the Equipment Inv. file.

Restart Processing of Uploaded NX Inventory Data

Used to resume processing of NX inventory that has been uploaded from a portable bar code reader. User will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload must be re-started from the beginning.

#### Download NX Program to Portable Bar Code Reader

> **NOTE:** This option uses an automated process to download bar code data.

To use this option, enter the name of the bar code program for downloading, and the device to which the bar code reader is connected, at the screen prompts.

Select Bar Coded Equipment Inventory Management Option: 1 Download NX Program to Portable Bar Code Reader

OK, enter the device to which the bar code reader is connected. DEVICE: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80// \<RET\>

\### WARNING: When a program is sent to the barcode reader, ALL DATA stored on the barcode reader will be LOST! Make sure that previous users of this barcode reader have no need for data, if any, that might exist on the reader.

Please follow the following steps:

1)  If you have not already done so, you may now connect up the barcode reader to the output device.
2)  After you have connected the barcode reader to the device, clear the barcode reader by turning the reader off and back on.
3)  After you have completed the above steps, press the return.

key to start sending the program to the barcode reader. If you want to abort this option, enter a ^ and return.

OK, you must now enter either a return ...

... or an '^' return:

Download time: 11 sec.

At this point, the program is loaded directly into the device. When downloading is completed, the message "OK, you may now disconnect the bar code reader" is displayed.

#### Upload Data From Portable Bar Code Reader

This option calls a routine that causes a portable bar code reader to upload its data to VISTA.

Enter the device to which the bar code reader is connected.

DEVICE: 64 RM 221 RIGHT MARGIN: 80//

...OK, use the Transmit option on the bar code reader to start sending the data...

OK, you are logging data on JUN 18,1111@09:46...

...using the BAR CODE program NON-EXPENDABLE

Reading bar code reader.....

....................................................................................

....................................................................................

....................................................................................

....................................

....................................................................................

....................................................................................

....................................................................................

....................................

....................................................................................

....................................................................................

....................................................................................

....................................

.................

Number of records read: 986.

The system is now ready to update the EQUIPMENT INV. file on the basis of data acquired from the portable bar code reader. If the system encounters data that cannot be processed in the normal fashion, it will give written notice in the form of an Exception Message. These messages will provide notification of such things as missing bar code labels and database inconsistencies.

You must now select a hard copy device (printer) to receive Exception Messages. You may enter the letter Q and then select a device if you wish to schedule this data processing task for some later time.

You can abort this process by up arrowing out at the Exception Messages prompt. The system then gives you a process ID, so that the user can restart the session at a later time, using the fifth option, Restart Processing of Uploaded NX Inventory Data.

Select Device for Exception Messages: HOME//^ FATAL ERROR OR USER ABORT.

Process ID is: ENNX Time stamp is: 2910618.0946.

Please make a note of this information, as you will need it to RESTART processing of the data on file.

#### Inventory Exception Listing

This option produces a list of those items on a specified CMR that have not been located in the course of a physical inventory.

Select Bar Coded Equipment Inventory Management Option: 3 Inventory Exception Listing

Report equipment not inventoried since: JUL 1,1997// \< RET\> (JUL 01, 1997) For all CMR's? NO// \< RET\>

Select CMR NAME: 110 DIETETICS

Check All NX equipment? YES//??

Enter NO if you only want to check for physical inventory of accountable NX equipment. This consists of capitalized equipment and equipment whose category stock number (CSN)

begins with 10, 23, or 70 (firearms, motor vehicles, or ADP).

Enter YES to check all equipment on CMR. Check All NX equipment? YES// \< RET\>

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

EXCEPTION LIST (NX INVENTORY) JUL 14,1997 Page 1

All NX Equipment Not Inventoried Since Jul 01, 1997 for CMR: 110 DIETETICS

Equipment ID# PM Number Location Previous Location Last Inventoried Manufacturer Equipment Name Use Status

1 7530-4565 201-110

DEFIBRILLATOR W/O MONITOR IN USE

| 21         | B7310-5113 | GE08-01-JB |
|------------|------------|------------|
| FOOD TRUCK |            | IN USE     |
| 154        | 7025-7488  | A202-01-JC |
| DEC        |            | IN USE     |
| 180        |            | 201        |
|            |            | IN USE     |
| 181        | 6530-43909 | 201        |
|            |            | IN USE     |
| 182        | 6530-9876  | 201        |

IN USE

1.  Items Not Inventoried (out of 6 items that met selection criteria). Enter RETURN to continue or '^' to exit:

#### Manual Update of Equipment Inventory

This option uses FileMan to update physical inventory data on individual entries in the Equipment Inv. file.

Select Bar Coded Equipment Inventory Management Option: 4 Manual Update of Equipment Inventory

Select EQUIPMENT ENTRY \#: ??

'EC.value' =\> equipment whose EQUIP. CATEGORY starts with 'value' 'LI.value' =\> equipment whose LOCAL ID starts with 'value' 'LO.value' =\> equipment whose LOCATION starts with 'value' 'MA.value' =\> equipment whose MANUFACTURER starts with 'value' 'MF.value' =\> equipment whose MFGR. EQUIP. NAME starts with 'value' 'MO.value' =\> equipment whose MODEL starts with 'value'

1 2221 IN USE

2 91120526 TURNED IN

3 3290A00220 IN USE

4 3301A01107 IN USE

'SN.value' =\> equipment whose SERIAL NUMBER starts with 'value' Choose from:

Select EQUIPMENT ENTRY \#: 50

1.  50 91120508 BED (ONE WARD) TURNED IN
2.  50 MHZ EISA PC 8 AB34300UER COMPUTER-PC-ADMINISTRATIVE T URNED IN

CHOOSE 1-2: 1

Entry Number: 50

Location: 201-114 Previous location: 221-114 Last inventoried: APR 24,1997

Do you wish to update this record? Yes// \<RET\> (Yes) LOCATION: 201-114// ??

Physical location of this item at the facility.

Choose from:

100-110-JC 110

101-148 148

102-148 148

103-110-JC 110

105-148 148

^

CCU MEDICINE

C EXAM/TREATMENT ROOM

C EXAM/TREATMENT ROOM CCU MEDICINE

C EXAM/TREATMENT ROOM

LOCATION: 201-114// 101-148 148 C EXAM/TREATMENT ROOM

Select EQUIPMENT ENTRY \#: 50

1.  50 91120508 BED (ONE WARD) TURNED IN
2.  50 MHZ EISA PC 8 AB34300UER COMPUTER-PC-ADMINISTRATIVE T URNED IN

CHOOSE 1-2: 1

Entry Number: 50

Location: 101-148 Previous location: 201-114 Last inventoried: APR 24,1997

Do you wish to update this record? Yes// N (No)

#### Restart Processing of Uploaded NX Inventory Data

This option is used to resume processing of NX inventory that has been uploaded from a portable bar code reader. Users will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload must be re-started from the beginning.

Enter PROCESS ID: ENNX

Enter TIME STAMP of process to be restarted: 2910618.0946.

The system is now ready to update the EQUIPMENT INV. file on the basis of data acquired from the portable bar code reader.

If the system encounters data that cannot be processed in the normal fashion, it will give you written notice in the form of an Exception Message. These messages will provide notification of such things as missing bar code labels and database inconsistencies.

Now select a hard copy device (printer) to receive Exception Messages.

You may enter the letter Q and then select a device if you wish to schedule this data processing task for some later time.

Select Device for Exception Messages: HOME// 67 WORK BENCH

### Purchase Order Group Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports ...
6.  PM Parameters ...
7.  Generate PM Schedule ...
8.  Record Equipment PMI ...
9.  Print Bar Code Labels for Equipment Management ...
10. Bar Coded Equipment Inventory Management ...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
13. Turn-In/Disposition Equipment

Edit a group of existing items in the inventory file without having to enter common data for each item. Equipment is initially selected by purchase order number (#).

Therefore, the purchase order \# field must already be populated before this option can be used to edit equipment. Equipment with the same purchase order \# is selected for editing by line item.

<table>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Equipment Management Option: <strong>11</strong> Purchase Order Group Edit Multiple Equipment Edit</th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th>PURCHASE ORDER #: <strong>A12345</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>13 Equipment Items found with Purchase Order # = A12345</p>
<p>Line Equipment Category Manufacturer Model</p></td>
<td>Count</td>
</tr>
<tr class="even">
<td>1 BED (ONE WARD) STRYKER 2020</td>
<td>8</td>
</tr>
<tr class="odd">
<td>2 COMPUTER TERMINAL/DISPLA DIGITAL EQUIP VT320</td>
<td>2</td>
</tr>
<tr class="even">
<td>3 AUTO/SEDAN FORD MOTOR/AUTOMOTIVE unspecified</td>
<td>1</td>
</tr>
<tr class="odd">
<td>4 unspecified ACME LAB X1000</td>
<td>1</td>
</tr>
<tr class="even">
<td>5 unspecified COBE LAB 8900</td>
<td>1</td>
</tr>
</tbody>
</table>

Select line(s) to edit: (1-5): 1,4.

9 Equipment Items will be edited.

Select FIELD: ??

Choose from:

15. LIFE EXPECTANCY
16. REPLACEMENT DATE
17. NXRN \#
18. CATEGORY STOCK NUMBER

^

Select FIELD: 18 CATEGORY STOCK NUMBER CATEGORY STOCK NUMBER: ??

Pointer to Category Stock Number File. This file was introduced to VISTA with Version 6.5 of the Engineering Package and is maintained by Acquisition and Materiel Management (Cataloging).

Choose from:

1005-000667

1005-001067

1005-001837

1005-001948

GUN PELLET MACHINE GUN REVOLVER RIFLE

^

CATEGORY STOCK NUMBER: 6530-439473 BED ADJUSTABLE

Select FIELD: LOCATION

LOCATION can be individually entered for each equipment item. Should LOCATION be asked for each of the 9 items? NO// LOCATION:??

Physical location of this item at the facility.

| Choose from: |     |     |                            |                  |        |
|--------------|-----|-----|----------------------------|------------------|--------|
| 221-114      | 114 |     | INFORMATION SYSTEMS CENTER |                  | OFFICE |
| 243-140      | 140 | F1  | MEDICAL ADMINISTRATION     |                  | OFFICE |
| 301-110      | 110 | 3W  | SURGERY                    | BED ROOM - 4 BED |        |
| 302-110      | 110 | 3W  | SURGERY                    | BED ROOM - 4 BED |        |
|              | ^   |     |                            |                  |        |

LOCATION: 201-114 114 INFORMATION SYSTEMS CENTER OFFICE Select FIELD: \<RET\>

Do you want to replace any existing PM data? NO// \<RET\>

OK to update the 9 selected items? YES.........

Would you like a list of modified equipment? YES

DEVICE: HOME// \<RET\> UCX/TELNET \<RET\>

Multiple Edit of Equipment Report APR 10, 1997 page 1

| Edited Field(s)                     | New Value   |     |     |
|-------------------------------------|-------------|-----|-----|
| CATEGORY STOCK NUMBER               | 6530-439473 |     |     |
| LOCATION                            | 201-114     |     |     |
| List of Modified Equipment 43 44 45 | 46          | 47  | 48  |
| 49 50 56                            |             |     |     |

### Lockout/Tagout Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

| 1   | New Inventory Entry                                |
|-----|----------------------------------------------------|
| 2   | Multiple Inventory Entry                           |
| 3   | Inventory Edit                                     |
| 4   | Display Equipment Record                           |
| 5   | Equipment Reports ...                              |
| 6   | PM Parameters ...                                  |
| 7   | Generate PM Schedule ...                           |
| 8   | Record Equipment PMI ...                           |
| 9   | Print Bar Code Labels for Equipment Management ... |
| 10  | Bar Coded Equipment Inventory Management ...       |
| 11  | Purchase Order Group Edit                          |
| 12  | Lockout/Tagout Enter/Edit                          |
| 13  | Turn-In/Disposition Equipment                      |

This option allows users to specify that equipment records (file \#6914) and/or equipment categories (file \#6911) are subject to lockout/tagout requirements. Lockout/tagout stipulates that the affected equipment must be rendered inoperative (usually by opening and tagging a circuit breaker) before the equipment is serviced.

Select Equipment Management Option: 12 Lockout/Tagout Enter/Edit Select one of the following:

S Set

C Cleared

Should 'LOCKOUT REQUIRED?' Flag be SET or CLEARED: Set// ??

Enter a code from the list.

Select one of the following: S Set

3.  Cleared

Should 'LOCKOUT REQUIRED?' Flag be SET or CLEARED: Set// \<RET \>

Select one of the following:

1.  Equipment Categories
2.  Equipment Entries

SET 'LOCKOUT REQUIRED?' Flag by: 1// ??

This utility is to manage (SET or CLEAR) the LOCKOUT REQUIRED field in the Equipment File. You may specify changes to all equipment belonging to selected EQUIPMENT CATEGORIES (Option 1) or you may select Equipment Records individually (Option 2).

Please enter '1' or '2' or '^' to escape.

Select one of the following:

1.  Equipment Categories
2.  Equipment Entries

SET 'LOCKOUT REQUIRED?' Flag by: 1// \<RET\> Equipment Categories Select EQUIPMENT CATEGORY NAME: ??

Choose from:

AIR CONDITIONER (THRU WALL) AMPLIFIER & SIGNAL CONDITIONER ANALYZER

^

Select EQUIPMENT CATEGORY NAME: BED

1.  BED (ONE WARD)
2.  BED-ELECTRIC
3.  BED-FLOTATION THERAPY
4.  BED-FLUOROSCOPIC
5.  BEDPAN WASHER WASHER-BEDPAN

Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 2

Would you like to add another Equipment Category: (Y/N/L): NO// \<RET\>

Select DEVICE for Action Taken Report: HOME// \<RET\> UCX/TELNET RIGHT MARGIN: 80//

\<RET\>

'LOCKOUT REQUIRED?' Flag SET for ... APR 10,1997@11:08 Page 1

ENTRY \# Equipment Category Manufacturer Equipment Name Location Manufacturer Model Serial Number

| 21          | BED-ELECTRIC | ELECTIC BED | 221-114    |
|-------------|--------------|-------------|------------|
| ENMFGR, ONE |              | 2300        | 7888UYHG   |
| 22          | BED-ELECTRIC | ELECTIC BED | 221-114    |
| ENMFGR, ONE |              | 2300        | 67YYGTH    |
| 24          | BED-ELECTRIC | ELECTIC BED | 100-110-JC |
| ENMFGR, ONE |              | 2300        | 786YYU8    |
| 25          | BED-ELECTRIC | ELECTIC BED | 100-110-JC |
| ENMFGR, ONE |              | 2300        | 789IIKI88  |
| 26          | BED-ELECTRIC | ELECTIC BED | 221-114    |
| ENMFGR, ONE |              | 2300        | 788UU7YY6  |
| 27          | BED-ELECTRIC | ELECTIC BED | 221-114    |
| ENMFGR, ONE |              | 2300        | 675TT54R   |
| 28          | BED-ELECTRIC | ELECTIC BED |            |
| ENMFGR, ONE |              | 2300        | 7886YUU7   |
| 29          | BED-ELECTRIC | ELECTIC BED | 221-114    |
| ENMFGR, ONE |              | 2300        | 78UIIUY76  |

Press \<RETURN\> to continue, or '^' to escape...

### Turn-In/Disposition Equipment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING EQUIPMENT MANAGEMENT MODULE

Version 7

1.  New Inventory Entry
2.  Multiple Inventory Entry
3.  Inventory Edit
4.  Display Equipment Record
5.  Equipment Reports ...
6.  PM Parameters ...
7.  Generate PM Schedule ...
8.  Record Equipment PMI ...
9.  Print Bar Code Labels for Equipment Management ...
10. Bar Coded Equipment Inventory Management ...
11. Purchase Order Group Edit
12. Lockout/Tagout Enter/Edit
13. Turn-In/Disposition Equipment

This option can be used to quickly update equipment records for the turn-in or final disposition of equipment not reported to Fixed Assets. The new option uses input templates to control which fields are changed or edited. The ENEQTURN template is used for turn-in and the ENEQDISP template is used for final disposition. If local templates ENZEQTURN or ENZEQDISP are created, they will be used in place of the national templates.

Select Equipment Management Option: 13 Turn-In/Disposition Equipment Select EQUIPMENT ENTRY \#: 50

Entry \#: 50 Mfg. Name: BED Mfg: ENMFGR1, FOUR

Mod: 2020 Ser \#: 91120508

Cat: BED (ONE WARD) Acq Date: OCT 15, 1996

Select TURN-IN or FINAL DISPOSITION (enter '^' to quit): ??

Enter a code from the list.

Select one of the following: T TURN-IN

4.  FINAL DISPOSITION

Select TURN-IN or FINAL DISPOSITION (enter '^' to quit): \<RET\>

This is a required response. Enter '^' to exit.

Select TURN-IN or FINAL DISPOSITION (enter '^' to quit): TURN-IN

> **NOTE:** Some data fields are automatically modified. USE STATUS: TURNED IN// ??

Tells the user whether or not the equipment is currently in active use.

Choose from:

1.  IN USE
2.  OUT OF SERVICE
3.  LOANED OUT
4.  TURNED IN
5.  LOST OR STOLEN USE STATUS: TURNED IN// \<RET\> CMR:??

Consolidated Memorandum of Receipt. The basic instrument by which accountability for capital equipment is established.

Choose from:

90 MAS 5.0 USERS

100 DENTAL

130 ENGINEERING

131 ENGINEERING

^

CMR: \<RET\>

LOCATION: 201-114// ??

Physical location of this item at the facility.

Choose from:

100-110-JC 110 CCU MEDICINE

101-148 148 C EXAM/TREATMENT ROOM

102-148 148 C EXAM/TREATMENT ROOM

103-110-JC 110 CCU MEDICINE

221-114 114 INFORMATION SYSTEMS CENTER OFFICE

243-140 140 F1 MEDICAL ADMINISTRATION OFFICE

301-110 110 3W SURGERY BEDROOM - 4 BED

302-110 110 3W SURGERY BEDROOM - 4 BED

^

LOCATION: 201-114// \<RET\>

TURN-IN DATE: OCT 21,1996// ?

Date on which item is turned over to A&MM for disposition. At this point it should be removed from the using service CMR.

TURN-IN DATE: OCT 21,1996// \<RET\>

COMMENTS:

1\> \<RET\>

Checking for inconsistencies...OK

Nonexpendable Equipment Module (A&MM)

The Nonexpendable Equipment (ENMM MGR) menu is a specially assigned menu option not available to all users. It is generally used by the PPM Chief and designee in A&MM.

Select OPTION NAME: ENMM MGR Nonexpendable Equipment Module (A&MM)

| 1   | Equipment Enter/Edit (NX) ...              |
|-----|--------------------------------------------|
| 2   | Equipment Management Reports (NX) ...      |
| 3   | Bar Code Features (NX Equipment) ...       |
| 4   | NX (Nonexpendable Equipment) Utilities ... |
| 5   | FAP Documents (Code Sheets) ...            |
| 6   | Fixed Assets Reports ...                   |

### Equipment Enter/Edit (NX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Collection of options for entering data into the AEMS/MERS Equipment Inv. file.

Equipment Management Reports (NX)

Collection of AEMS/MERS outputs that are thought to be of interest to the Property Management Section of A&MM.

Bar Code Features (NX Equipment)

Collection of options designed for use in bar coding nonexpendable equipment and in using bar code to maintain CMR inventories.

NX (Nonexpendable Equipment) Utilities

Includes options used to maintain ancillary files that are necessary for Personal Property Management under AEMS/MERS.

FAP Documents (Code Sheets)

This menu contains options to validate or transmit FAP code sheets.

Fixed Assets Reports

This menu option contains reports on FAP documents.

Equipment Enter/Edit (NX)

The options on this menu have been described in previous sections of this chapter.

Select Nonexpendable Equipment Module (A&MM) Option: 1 Equipment Enter/Edit (NX)

| 1   | New Inventory Entry                  |
|-----|--------------------------------------|
| 2   | Inventory Edit                       |
| 3   | Display Equipment Record             |
| 4   | Multiple Inventory Entry             |
| 5   | Manual Update of Equipment Inventory |
| 6   | Purchase Order Group Edit            |
| 7   | Turn-In/Disposition Equipment        |

Display Equipment Record

Display selected fields from the EQUIPMENT INV. file. Repair history is not displayed via this option.

Inventory Edit

Edit the record of an existing piece of equipment. The .01 field (ENTRY NUMBER) is assigned by the system when an item is first added to the EQUIPMENT INV. file and may not be edited.

This option gives access to both Supply and Engineering fields.

Manual Update of Equipment Inventory

Uses FileMan to update physical inventory data on individual entries in the Equipment Inv. file.

Multiple Inventory Entry

Enter several like items (e.g., 50 new electric beds) into the EQUIPMENT INV. file (#6914) without having to enter common information each time.

New Inventory Entry

Add a new item to the EQUIPMENT INV. file (#6914).

Purchase Order Group Edit

Edit a group of existing items in the inventory file without having to enter common data for each item. Equipment is initially selected by purchase order \#. Therefore, the purchase order \# field must already be populated before this option can be used to edit equipment. Equipment with the same purchase order \# is selected for editing by line item.

Turn-In/Disposition Equipment

This option can be used to quickly update equipment records for the turn-in or final disposition of equipment not reported to Fixed Assets.

### Equipment Management Reports (NX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of the options on this menu have been described in previous sections of this chapter. Accountable NX for Station and Check of Equipment Capitalization are shown in this section.

1.  Specific Equipment History
176. CMR Inventory (EIL)
177. Warranty List
178. Replacement Listing
179. Location Inventory
180. Using Service Inventory
181. Use Status Inventory
182. Nonexpendable Expensed Inventory
183. Accountable NX for Station
184. Parent System/Component Hierarchy Report
185. Check of Equipment Capitalization

Specific Equipment History

Print-out of repair history of a specific entry in EQUIPMENT INV. file.

CMR Inventory (EIL)

This option generates the Equipment Inventory Listing (EIL) report. Equipment that is belongs to the user specified CMR and is either capitalized or whose category stock number beings with 10 (firearms), 23 (motor vehicles) or 70 (ADP) is printed on this report. A page suitable

for the signature of the Responsible Official is printed when the output is directed to a printer.

Warranty List

Prints all devices whose warranties are scheduled to expire within a user specified time interval.

Replacement Listing

Prints all entries in the EQUIPMENT INV. file scheduled for replacement within a user specified time interval.

Location Inventory

Inventory listing by device location.

Using Service Inventory

Inventory listing by using service. Note that the using service is not necessarily the owning service (ex: a VCR may be used in Dental but owned by Medical Media Production). Owning service is established via the CMR.

Use Status Inventory

Inventory listing by use status.

Nonexpendable Expensed Inventory

This option generates the Nonexpendable Expensed Inventory report. Equipment that is belongs to the user specified CMR and is not capitalized and whose category stock number does not be with 10 (firearms), 23 (motor vehicles) or 70 (ADP) is printed on this report.

See the CMR Inventory (EIL) report to print accountable equipment that belongs to a CMR.

Accountable NX for Station

This option generates a list of capitalized equipment sorted by category stock number and CMR for a specified station. Equipment must be on a CMR in order to be included in this report. Non-expendable expensed equipment which is accountable (firearms, motor vehicles, and ADP) can optionally.

be included in the output.

Parent System/Component Hierarchy Report

Prints a hierarchical list of a parent system and all of its components. Components are indented and listed beneath their parent system. Items that are components of a component in the specified system are included.

Check of Equipment Capitalization

This option generates a report of equipment items which appear to have.

unusual combinations in the TOTAL ASSET VALUE and CAPITALIZED? fields. Capitalized equipment is reported when it's Type Entry is blank. Capitalized NX equipment is reported when it's CMR does not begin with one of the standard two-digit values, or it's Standard General Ledger is blank. Equipment items with a disposition date are excluded from the report. This report. This report searches the entire Equipment Inv. file and may take some time to run.

These equipment items should be checked to ensure that the data in the Equipment Inv. file is accurate.

See the Nonexpendable Expensed Inventory report to print equipment that belongs to a CMR but does not meet the other criteria for inclusion on the Equipment Inventory Listing report.

#### Accountable NX for Station

One report, Accountable NX for Station has been added to menu option 2. The other reports appear on the ENEQ REPORTS menu and have been described under that heading.

This option generates a list of capitalized equipment sorted by category.

stock number and CMR for a specified station. Equipment must be on a CMR in order to be included in this report. Non-expendable expensed equipment which is accountable (firearms, motor vehicles, and ADP) can optionally.

be included in the output.

Select Equipment Management Reports (NX) Option: 9 Accountable NX for Station STATION NUMBER: 999// \<RET\>

Include Accountable NX-Expensed Equipment? YES// \<RET\>

DEVICE: HOME// \<RET\> LAN RIGHT MARGIN: 80// \<RET\>

ACCOUNTABLE NX EQUIP. FOR STATION: 999 APR 04, 1996@10:47:31 page 1

EQUIPMENT ACQ FUND SGL ASSET VALUE LE REPL LOCATION CMR ENTRY \# DATE DATE ROOM-BLDG-DIV

­

RIFLE (CSN: 1005-001948)

1013 / 6100 \$1,000.00 20 / 23E-135 161

| (CSN TOTAL \#1                | \$1,000.00)   |     |         |     |
|-------------------------------|---------------|-----|---------|-----|
| SHOTGUN (CSN: 1005-002137)    |               |     |         |     |
| 1006 / 6100                   | \$1,000.00 20 | /   | 23E-135 | 780 |
| (CSN TOTAL \#1                | \$1,000.00)   |     |         |     |
| AUTO AMBUL (CSN: 2310-003324) |               |     |         |     |

1161 02/96 AMAF \$9,200.00 7 02/03 101-114A 130

Manf: ENMFGR1, F IVE

Model: N100C S/N: GFGF54545

| 1025          | /          | 6100 | \$1,000.00 7 | /   | 23E-135 | 451 |
|---------------|------------|------|--------------|-----|---------|-----|
| PM: 7800-7888 |            |      |              |     |         |     |
|               | (CSN TOTAL | \#2  | \$10,200.00) |     |         |     |

BUS MOTOR (CSN: 2310-008591)

1100 03/94 AMAF 1750 \$56,040.00 8 03/02 13V

PM: 3770-9030 Manf: ENMFGR1, S IX

Model: Econoline S/N: w5207

(CSN TOTAL \#1 \$56,040.00) TRUCK CARGO (CSN: 2320-438836)

1023 / 6100 \$1,000.00 9 / 23E-135 300

(CSN TOTAL \#1 \$1,000.00) TRUCK DUMP (CSN: 2320-438839)

1130 11/95 AMAF \$11,630.85 10 11/05 995

Manf: ENMFGR1, SEVEN

Model: C100 S/N: 123456

(CSN TOTAL \#1 \$11,630.85) TRUCK VAN (CSN: 2320-438847)

1020 / 6100 \$1,000.00 7 / 23E-135 260

(CSN TOTAL \#1 \$1,000.00) TRAILER LOW BED (CSN: 2330-438830)

1019 / 6100 \$1,000.00 10 / 23E-135 230

(CSN TOTAL \#1 \$1,000.00)

ACCOUNTABLE NX EQUIP. FOR STATION: 999 APR 04, 1996@10:47:31 page 48

EQUIPMENT ACQ FUND SGL ASSET VALUE LE REPL LOCATION CMR ENTRY \# DATE DATE ROOM-BLDG-DIV

­

TOTALS COUNT ASSET VALUE

| SGL    | 1561     | 4     | \$ 23,600.00      |
|--------|----------|-------|-------------------|
| SGL    | 1750     | 65    | \$ 101,126,838.55 |
| SGL    | 1751     | 5     | \$ 102,160.00     |
| SGL    | 1754     | 1     | \$ 5,001.00       |
| SGL    | 1811     | 1     | \$ 101.00         |
| SGL    | 1830     | 1     | \$ 7,000.00       |
| SGL    | 6100     | 14    | \$ 38,020.00      |
| SGL    | \<null\> | 14    | \$ 162,127.12     |
|        |          | ----- | ---------------­   |
| REPORT | TOTAL    | 105   | \$ 101,464,847.67 |

#### Check of Equipment Capitalization

This report prints a list of equipment items which appear to have unusual combinations in the TOTAL ASSET VALUE and CAPITALIZED? fields. Capitalized NX equipment whose CMR does not begin with one of the standard two-digit values is also listed.

The report should be used to assist with identification of equipment which may not have been appropriately marked as capitalized. The capitalized field is important for identification of equipment which is of interest to FAP.

Select Comparison Reports (AEMS/MERS vs LOG1) Option: cap Check of Equipment Capitalization

This report searches the entire equipment file and may take some time to complete. Consider queuing this report to run after-hours. DEVICE: HOME// \<RET\> LAN RIGHT MARGIN: 80// \<RET\>

CHECK OF EQUIPMENT CAPITALIZATION NOV 27, 1995@14:53:08 page 1 TYPE ASSET

EQUIP ID# ENTRY CMR VALUE CAPITALIZED

| 1050 | NX  | 160 | 23500   |     | Check capitalization |
|------|-----|-----|---------|-----|----------------------|
| 1057 | NX  |     |         | YES | Check capitalization |
|      |     |     |         |     | Check CMR            |
|      |     |     |         |     | SGL is blank         |
| 1058 | NX  |     | 10100   | YES | Check CMR            |
| 1059 | NX  |     |         | YES | Check capitalization |
|      |     |     |         |     | Check CMR            |
|      |     |     |         |     | SGL is blank         |
| 1064 |     | 205 | 7800    |     | Check capitalization |
| 1068 | NX  | 160 | 8623.43 | YES | SGL is blank         |

6 questionable equipment items found.

### Bar Code Features (NX Equipment)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Equipment Labels...
186. Location Labels...
187. Download NX Program to Portable Bar Code Reader
188. Upload Data from Portable Bar Code Reader
189. Restart Processing of Uploaded NX Inventory Data
190. Inventory Exception Listing

Equipment Labels

Prints bar coded equipment labels. Cohorts of labels (ex: labels by CMR, labels by Equipment Category, etc.) will be sorted by LOCATION unless the user specifies otherwise.

Location Labels

Driver option to print bar coded location labels.

Download NX Program to Portable Bar Code Reader

Downloads an IRL (Interactive Reader Language) program to a portable bar code reader.

Upload Data from Portable Bar Code Reader

Calls a routine that causes a portable bar code reader to upload its data to VISTA.

Restart Processing of Uploaded NX Inventory Data

Used to resume processing of NX inventory that has been uploaded from

a portable bar code reader. User will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload.

must be re-started from the beginning.

Inventory Exception Listing

Produces a list of those items on a specified CMR that have not been located in the course of a physical inventory.

### NX (Nonexpendable Equipment) Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Nonexpendable Equipment module (A&MM) Option: 4 NX (Nonexpendable Equipment) Utilities

| 1   | CMR File Enter/Edit              |
|-----|----------------------------------|
| 2   | Category Stock Number Enter/Edit |
| 3   | National EIL Enter/Edit          |

CMR File Enter/Edit

For maintaining the list of CMR (Consolidated Memoranda of Receipt) in use at your facility. This option is usually held by your PPM Chief and/or his designee.

Category Stock Number Enter/Edit

Intended for maintenance of Category Stock Number file. This option should be held by no more than one or two persons at each site, at the discretion of A&MM.

National EIL Enter/Edit

This option is used to edit the National EIL file. This file contains the list of valid Equipment Inventory Listing (EIL) codes as determined by VACO. This file is used to associate EIL codes with cost centers.

#### CMR File Enter/Edit

Select NX (Nonexpendable Equipment) Utilities Option: CMR File Enter/Edit Select CMR NAME: ??

Choose from:

100 DENTAL

110 DIETETIC

130 ENGINEERING

42B ACQUISITION & MATERIEL MGMNT

Name of CMR.

Select CMR NAME: 160 LABORATORY NAME: 160// \< RET\>

SERVICE: LABORATORY//??

Service to which this CMR is assigned.

SERVICE: LABORATORY// \< RET\> BRIEF DESCRIPTION (Optional): ??

A means for sites to briefly describe the purpose of this CMR, if they find it useful to do so.

BRIEF DESCRIPTION (Optional): \< RET\> RESPONSIBLE OFFICIAL: ??

Employee currently responsible for items on this CMR.

RESPONSIBLE OFFICIAL: \< RET\> PHONE (RESP OFFICIAL): ??

PHONE (RESP OFFICIAL): \< RET\> LAST RECONCILED: ??

Date on which this CMR was last reconciled with centralized non-­ expendable equipment records (Log 1 or ISMS).

LAST RECONCILED: \< RET\> RESEARCH?:??

Intent of this field is to provide a means of flagging equipment purchased and maintainable with research funds. Please enter 'YES' if and only if this is a research CMR.

Choose from:

Y YES

N NO

RESEARCH?: \< RET\> STATION NUMBER: ??

Station number of the facility that owns the assets in this CMR. For example, if this CMR is for a national cemetery which is serviced by.

a VAMC then the entry in this field should be the station number of the national cemetery.

Entries must match an entry in the ALTERNATE STATION NUMBER field (multiple) of the Eng Init Parameters File (#6910).

STATION NUMBER: \< RET\>

Equipment Management Nonexpendable Equipment Module (A&MM)

IT TRACKING: YES//???

If a CMR has IT TRACKING set to YES, the equipment on that Equipment Inventory List (EIL) can be edited using options on the IT Equipment Module menu. Additionally, all equipment on such EILs will be expected to be assigned to individual IT owners.

Choose from:

1 YES

0 NO

IT TRACKING: YES// \<RET\>

ALTERNATE RESPONSIBLE OFFICIAL: ??

A person authorized to act for the RESPONSIBLE OFFICIAL. This is an

optional data element to be used at the discretion of each facility. ALTERNATE RESPONSIBLE OFFICIAL: \<RET\>

DAYS BETWEEN RETURNS: ??

This is the maximum number of days before an equipment item must be returned to be serviced and physically inventoried.

DAYS BETWEEN RETURNS: \<RET\>

LOAN FORM PHONE: ??

This is the telephone number to be called concerning loan forms for equipment on this CMR.

LOAN FORM PHONE: (555) 555-5555// \<RET\>

> **NOTE:** If CMR data is changed, the system will automatically update equipment records belonging to that CMR with the new information. In cases where affected equipment has been reported to FAP, the system will note that and instruct you to enter the appropriate FAP document.

#### Category Stock Number Enter/Edit

Select NX (Nonexpendable Equipment) Utilities Option: 2 Category Stock Number Enter/Edit

Select CATEGORY STOCK NUMBER NAME: ??

CHOOSE FROM:

1005-000667 GUN PELLET CROSMAN

2340-438835 SCOOTER MOTOR

2340-629016 MOTO 2WHTHRU10HP150CC

YOU MAY ENTER A NEW CATEGORY STOCK NUMBER, IF YOU WISH

Answer must be 4 numerics, a dash (-), and then 6 numerics.

Format entries as 4 numbers followed by dash (-) followed by 6 numbers. Select CATEGORY STOCK NUMBER NAME: 2340-438835 ENMFGR1, EIGHT NAME: 2340-438835// \<RET\>

LIFE EXPECTANCY: 8// \<RET\>

BRIEF DESCRIPTION: ENMFGR1, EIGHT Replace

\<RET\>

SPECIAL HANDLING CODE: ??

Indicates that the Category Stock Number in question is subject to special reporting requirements. This data element was explicitly added to VISTA in the summer of 1111. '0' indicates COMPUTERS (ADP/WP); '1' indicates CCTV (CLOSED CIRCUIT TV); '2' indicates AUDIOVISUAL (OTHER THAN CCTV); and '3' indicates PRINTING AND REPRODUCTION. Numbers '4' thru '9' are reserved.

'1' indicates CCTV (CLOSED CIRCUIT TV)

'2' indicates AUDIOVISUAL (OTHER THAN CCTV) '3' indicates PRINTING & REPRODUCTION.

CHOOSE FROM:

1.  Auto Data Process Equip
2.  Closed Circuit TV (CCTV)
3.  Audio Visual Equip
4.  Print & Repro Equip

SPECIAL HANDLING CODE:. \<RET\>.............

NOMENCLATURE:

1\>SCOOTER, MOTOR. A DROP FRAME VEHICLE HAVING TWO WHEELS, ONE BEHIND

2\>THE OTHER, OR CONSISTING OF ONE FRONT ANDTWO

3\>REAR WHEELS, OR ONE REAR AND TWO FRONT WHEELS; STEERED

4\>WITH A HANDLEBAR OR WHEEL AND PROPELLED BY

5\>AN ELECTRIC OR GASOLINE MOTOR DRIVING THROUGH SPROCKETS

6\>AND CHAINS, PULLEYS AND BELTS, OR A SHAFT

7\>TO THE REAR WHEELS.

8\> \<RET\>

EDIT Option: \<RET\>

Select CATEGORY STOCK NUMBER NAME: \<RET\>

#### National EIL Enter/Edit

Select NX (Nonexpendable Equipment) Utilities Option: National EIL Enter/Edit the National EIL file should only be changed at the direction of

VACO. If the cost center associated with an EIL code is changed then FR Documents will automatically be generated in order to update the cost center value in Fixed Assets. A FR Document will be sent for each equipment item that belongs to a CMR that starts with the EIL code and is currently established in Fixed Assets.

Select NATIONAL EIL CODE: ??

Choose from:

10. DENTAL
11. DIETETICS
12. MEDICAL EDUCATION

^

You may enter a new NATIONAL EIL, if you wish Answer must be 2 characters in length.

Select NATIONAL EIL CODE: 17 LIBRARY

...OK? Yes// \< RET\> (Yes) DESCRIPTION: LIBRARY//??

Description of the EIL code.

DESCRIPTION: LIBRARY// \< RET\> COST CENTER: 822600//??

Cost Center (if any) that is linked to the EIL code. This will be used as the cost center of any equipment entries whose CMR begins with the national EIL code.

COST CENTER: 822600// \< RET\> Select NATIONAL EIL CODE:\< RET\>

### FAP Documents (Code Sheets)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu is used to transmit the Fixed Asset Documents from AEMS/MERS to FAP. An equipment entry is considered to be established in Fixed Assets if there is an FA Document (Acquisition) on file for that entry which has not been followed by a later FD Document (Disposition). There are five different FAP Documents. The FA Document *cannot* be sent for equipment which is already established in Fixed Assets. The FB, FC, FD, and FR Documents *can only* be sent for equipment entries which are already established in the Fixed Assets system.

| FA1 | Send a Single FA Document                          |
|-----|----------------------------------------------------|
| FA2 | Batch Send FA Documents (by CMR)                   |
| FA3 | Batch Send FA Documents (by Station)               |
| FB  | Better An Equipment Record (FB Document)           |
| FC  | Acquisition Data Edit (FC Document)                |
| FD  | Disposition an Asset (FD Document)                 |
| FR  | Financial Data Edit (FR Document)                  |
| V1  | FAP Validity Check for A Single Item (FA Document) |
| V2  | FAP Validity Check by CMR (FA Documents)           |
| V3  | FAP Validity Check by Station n (FA Documents)     |
| AV  | Adjustment Voucher Entry                           |
|     | Recalculate FAP Balances                           |

Send a Single FA Document

This option will send a FA Document (code sheet) to the Fixed Assets package (FAP) in Austin for a selected equipment entry. Appropriate data

is extracted from the Equipment Inv. file and used to populate the code sheet.

FA Documents will not be created for equipment entries already established in FAP.

Batch Send FA Documents (by CMR)

This option will send FA Documents (code sheets) to the Fixed Assets package (FAP) in Austin for equipment belonging to a specified CMR.

Appropriate data will be extracted from the Equipment Inv. file and used to populate the code sheets. Only equipment which is capitalized (CAPITALIZED field = YES) will be considered. FA Documents will not be created for equipment entries already established in FAP.

Batch Send FA Documents (by Station)

This option will send FA Documents (code sheets) to the Fixed Assets package (FAP) in Austin for equipment belonging to a specified Station. Appropriate data will be extracted from the Equipment Inv. file and used to

populate the code sheets. Only equipment which is capitalized (CAPITALIZED field = YES) and on a CMR (CMR field not blank) will be considered. FA Documents will not be created for equipment entries already established in FAP.

Better An Equipment Record (FB Document)

This option is used to record a betterment or upgrade to a recorded fixed asset. The information is transmitted to FAP.

Acquisition Data Edit (FC Document)

This option is used to record changes or adjustments to a recorded fixed asset. The information is transmitted to FAP.

Disposition an Asset (FD Document)

This option records the disposition of a fixed asset due to sale, destruction, trade-in, etc. The information is transmitted to FAP.

Financial Data Edit (FR Document)

This document is used to edit documents that cannot be changed with an FC document.

FAP Validity Check for A Single Item (FA Document)

This option will perform a validity check on an entry in the Equipment file to determine if a FA Document (code sheet) can be created for that entry.

FAP Validity Check By CMR (FA Documents)

This option will perform validity checks on equipment belonging to a specified CMR to determine if FA Documents (code sheets) can be created for those equipment entries. Only capitalized (CAPITALIZED field = YES) equipment will be considered. Equipment which is already established in Fixed Assets will not be checked.

FAP Validity Check by Station (FA Documents)

This option will perform validity checks on equipment belonging to a station to determine if FA Documents (code sheets) can be created for those equipment entries. Only capitalized (CAPITALIZED field = YES) equipment which is on a CMR (CMR field not blank) will be considered. Equipment which is already established in Fixed Assets will not be checked.

Adjustment Voucher Entry

This option is used to create an adjustment voucher for an existing FAP Document.

Recalculate FAP Balances

Dollar balances (by Station, Fund, SGL, and month) are maintained in the FAP BALANCES file and printed on the Voucher Summary report. This option can be used to recalculate the balances if they appear incorrect.

The net \$ activity for a specified month will be computed from the individual FAP code sheets. The results are then compared to the values maintained in the FAP BALANCES file. If there are any discrepancies, the recalculated values can be used to update the FAP BALANCES file.

The following Equipment Inventory file fields are of interest to Fixed Assets:

| Field \# | Field Name              | On Screen | Screen Position | User Edit via FAP Document |
|----------|-------------------------|-----------|-----------------|----------------------------|
| 18       | CATEGORY STOCK NUMBER   | 1         | 5               | FC-00                      |
| 15       | LIFE EXPECTANCY         | 1         | 6               | FC-00                      |
| 19       | CMR                     | 1         | 8               | FR                         |
| 20.1     | ACQUISITION METHOD      | 1         | 11              | FC-00                      |
| 12       | TOTAL ASSET VALUE       | 1         | 14              | FB adds, FC adjusts by net |
| 13       | ACQUISITION DATE        | 1         | 15              | FC-00                      |
| 16       | REPLACEMENT DATE        | 1         | 17              | FC-00                      |
| 7        | TYPE OF ENTRY           | 1         | 19              |                            |
| 20.5     | TURN-IN DATE            | 2         | 13              | FD-T                       |
| 22       | DISPOSITION DATE        | 2         | 14              | FD-D                       |
| 31       | DISPOSITION METHOD      | 2         | 15              | FD-D                       |
| 32       | DISPOSITION VALUE       | 2         | 16              | FD-D                       |
| 60       | STATION NUMBER          | 2         | 18              |                            |
| 34       | CAPITALIZED?            | 3         | 2               |                            |
| 62       | FUND                    | 3         | 3               | FR                         |
| 35       | FUND CONTROL POINT      | 3         | 4               | FR                         |
| 61       | BUDGET OBJECT CODE      | 3         | 5               | FR                         |
| 38       | STANDARD GENERAL LEDGER | 3         | 6               |                            |
| 63       | ADMINISTRATIVE/OFFICE   | 3         | 7               | FR                         |
| 64       | EQUITY ACCOUNT          | 3         | 8               |                            |

Note that some fields can’t be changed while the asset is established in Fixed Assets.

FD-T and FD-D represent FD Documents for Turn-In and Final Disposition respectively.

FC-00 represents a FC Document used to change a FA Document (betterment 00).

#### Send a Single FA Document

This option is used to send a single equipment record from AEMS/MERS to the corporate data base (FAP) in Austin.

Select FAP Documents (Code Sheets) Option: FA1 Send a Single FA Document This option TRANSMITS FA Documents (code sheets) for specified equipment.

Select EQUIPMENT ENTRY \#: ??

'EC.value' =\> equipment whose EQUIP. CATEGORY starts with 'value' 'LI.value' =\> equipment whose LOCAL ID starts with 'value' 'LO.value' =\> equipment whose LOCATION starts with 'value' 'MA.value' =\> equipment whose MANUFACTURER starts with 'value' 'MF.value' =\> equipment whose MFGR. EQUIP. NAME starts with 'value' 'MO.value' =\> equipment whose MODEL starts with 'value'

'SN.value' =\> equipment whose SERIAL NUMBER starts with 'value' Choose from:

Select EQUIPMENT ENTRY \#: 8978899 1 8978899

DEFIBRILLATOR IN USE 7530-4565

Should an Adjustment Voucher be created? YES//??

Adjustment Vouchers are used to inform Fiscal personnel of FAP transactions that Fiscal must take action on.

Enter YES or NO

Should an Adjustment Voucher be created? YES// \< RET\>

A.V. REASON:??

Choose from: EIL TO EXCESS TO EIL

INVENTORY PICK UP OTHER

SGL TO SGL

A.V. REASON: OTHER// exCESS TO EIL

A.V. COMMENTS:

1\> Had too many.

2\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES Adjustment Voucher was created.

Equipment Entry \#: 1 was transmitted. Select EQUIPMENT ENTRY \#:

#### Batch Send FA Documents by CMR

This option is used to send equipment records by CMR from AEMS/MERS to the corporate database (FAP) in Austin.

Select FAP Documents (Code Sheets) Option: fa2 Batch Send FA Documents (by CMR) This option TRANSMITS FA Documents (code sheets)

for all equipment that belongs to a specified CMR. Select CMR NAME: ??

Choose from:

| 100 | DENTAL    |
|-----|-----------|
| 110 | DIETETIC  |
| .   |           |
| .   |           |
| 451 | VOLUNTARY |
|     | ^         |

Select CMR NAME: 205 MEDICAL

Now select the device to print results on. DEVICE: HOME// \<RET\> LAN

FA DOCUMENT TRANSMISSION FOR CMR: 205 APR 04, 1996@11:58:08 page 1

11 records have been processed from CMR: 205.

4 records were sent to FAP.

4 were not sent due to already being established in FAP.

3 were not sent due to validation problems.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 52%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Equipment Records</th>
<th>not sent because of validation</th>
<th>problems:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Entry #</p>
<p>1065</p></td>
<td><p>Reason</p>
<p>Missing Acquisition Date</p></td>
<td></td>
</tr>
<tr class="even">
<td>1066</td>
<td>Missing Acquisition Date</td>
<td></td>
</tr>
<tr class="odd">
<td>1173</td>
<td>Missing Fund</td>
<td></td>
</tr>
<tr class="even">
<td>1173</td>
<td>Missing A.O. Code</td>
<td></td>
</tr>
<tr class="odd">
<td>1173</td>
<td>Missing Equity Account</td>
<td></td>
</tr>
</tbody>
</table>

#### Batch Send FA Documents by Station

This option will send FA Documents (code sheets) to the Fixed Assets package (FAP) in Austin for equipment belonging to a specified Station. Appropriate data will be extracted from the Equipment Inv. file and used to populate the code sheets. Only equipment which is capitalized (CAPITALIZED field = YES) and on a CMR (CMR field not blank) will be considered. FA Documents will not be created for equipment entries already established in FAP.

Select FAP Documents (Code Sheets) Option: FA3 Batch Send FA Documents (by Station) This option TRANSMITS FA Documents (code sheets)

for all equipment that belongs to a specified Station.

STATION NUMBER: 999// \< RET\>

Now select the device to print results on. DEVICE: HOME// \< RET\> UCX/TELNET

FA DOCUMENT TRANSMISSION FOR STATION: 999 JUL 16, 1997@15:30:20 page 1

29 records have been processed from STATION: 999.

2 records were sent to FAP.

8 were not sent due to already being established in FAP.

19 were not sent due to validation problems.

Equipment Records not sent because of validation problems:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Entry #</th>
<th rowspan="2"><p>Reason</p>
<p>Missing General Ledger Account Missing Category Stock Number Missing Fund</p>
<p>Missing A.O. Code</p>
<p>Missing Budget Object Code Missing Equity Account</p></th>
</tr>
<tr class="odd">
<th><p>42</p>
<p>42</p>
<p>42</p>
<p>42</p>
<p>42</p>
<p>42</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>45</p>
<p>45</p>
<p>45</p>
<p>45</p>
<p>45</p>
<p>45</p></td>
<td><p>Missing General Ledger Account Missing Category Stock Number Missing Fund</p>
<p>Missing A.O. Code</p>
<p>Missing Budget Object Code Missing Equity Account</p></td>
</tr>
<tr class="even">
<td><p>51</p>
<p>51</p>
<p>51</p>
<p>51</p>
<p>51</p>
<p>51</p></td>
<td><p>Missing General Ledger Account Missing Category Stock Number Missing Fund</p>
<p>Missing A.O. Code</p>
<p>Missing Budget Object Code Missing Equity Account</p></td>
</tr>
<tr class="odd">
<td><p>63</p>
<p>63</p>
<p>63</p>
<p>63</p>
<p>63</p>
<p>63</p></td>
<td><p>Missing General Ledger Account Missing Category Stock Number Missing Fund</p>
<p>Missing A.O. Code</p>
<p>Missing Budget Object Code</p>
<p>Missing Equity Account</p></td>
</tr>
</tbody>
</table>

#### Better An Equipment Record (FB Document)

This document records a betterment or upgrade to a recorded fixed asset and transmits the information to FAP.

Select EQUIPMENT ENTRY \#: 8978899 1 8978899 DEFIBRILLATOR IN USE 7530-4565

Current Asset Value is \$7200.00

DESCRIPTION: Description of the betterment ACQUISITION DATE: t (JUL 16, 1997) ACQUISITION METHOD:??

This is the method by which the betterment was acquired; purchased, leased, etc.

Choose from:

C CONSTRUCTED

G GIFT/BEQUEST/DONATION

12. LEASED
13. LEASED/PURCHASED
15. OTHER
16. PURCHASED

R TRANSFERRED

T TRADED

24. EXCESS

ACQUISITION METHOD: p PURCHASED BETTERMENT VALUE:??

This is the total value of the betterment.

BETTERMENT VALUE: 1000.00

Should an Adjustment Voucher be created? YES// y YES

A.V. REASON:??

Choose from:

ASSET VALUE VARIANCE/ADJUSTMEN OTHER

A.V. REASON: aSSET VALUE VARIANCE/ADJUSTMEN

A.V. COMMENTS:

1\> explain the adjustment voucher

2\>

EDIT Option:\< RET\>

Is adjustment voucher correct? y YES

Sure you want to process this betterment? YES// \< RET\> Updating the Equipment File...

Sending FB document to FAP. Adjustment Voucher was created.

#### Acquisition Data Edit (FC Document)

This document records changes or adjustments to recorded fixed assets and transmits the information to FAP. The dialogue is different depending on the BETTERMENT NUMBER chosen.

Select FAP Documents (Code Sheets) Option: fc Acquisition Data Edit (FC Document) Select EQUIPMENT ENTRY \#: 1 8978899 DEFIBRILLATOR IN USE 75

30-4565

BETTERMENT NUMBER: 00// \< RET\>

CATEGORY STOCK NUMBER: 6515-438660// \< RET\> DEFIBRILL-CARDIOSCOPE ACQUISITION DATE: JUN 4,1986// \< RET\> (JUN 04, 1986)

ACQUISITION METHOD: P// \< RET\> PURCHASED USEFUL LIFE: 8// \< RET\>

SUMMARY ASSET VALUE: 7200.00// \< RET\>

REPLACEMENT DATE: JUN 4,1994// June 4, 1998 (JUN 04, 1998)

Should an Adjustment Voucher be created? YES// \< RET\>

A.V. REASON:??

Choose from:

ASSET VALUE VARIANCE/ADJUSTMEN OTHER

A.V. REASON: aSSET VALUE VARIANCE/ADJUSTMEN

A.V. COMMENTS:

1\> repair extended life

2\>\< RET\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES

Sure you want to process these changes? YES// \< RET\> Updating the Equipment File...

Sending FC document to FAP...

Adjustment Voucher was created.

#### Disposition an Asset (FD Document )

This document records the disposition of a fixed asset due to sale, destruction, trade-in, etc. The information is transmitted to FAP. The dialogue is different depending on whether TURN-IN or DISPOSITION is chosen.

Select FAP Documents (Code Sheets) Option: fd Disposition an Asset (FD Document

)

Select EQUIPMENT ENTRY \#: 1 8978899 DEFIBRILLATOR IN USE 75

30-4565

TURN-IN OR DISPOSITION?:??

Since FD documents may be used in moving an asset to EXCESS as well as in processing final disposition, we must ask the user which he wants to do. This response tells us whether to update the TURN-IN DATE or the DISPOSITION DATE.

Choose from:

T TURN-IN

D FINAL DISPOSITION TURN-IN OR DISPOSITION?: t TURN-IN

TURN-IN DATE: t (JUL 16, 1997) DISPOSITION AUTHORITY: 00000//??

This is the authority under which the item was disposed of.

DISPOSITION AUTHORITY: 00000// \< RET\>

When equipment is turned-in, its TOTAL ASSET VALUE must be changed to the fair market value per VA Accounting Standards. NOTE: The current TOTAL ASSET VALUE will automatically be saved in the ORIGINAL ASSET VALUE field.

Current TOTAL ASSET VALUE: 8,200.00

Acquisition Date: Jun 04, 1986 Life Expectancy: 8

Replacement Date: Jun 04, 1998 Condition:

Repair Costs (excluding preventive maintenance)

Labor\$:3,000 Material\$: 1,500 Vendor\$: 0 Total\$: 4,500

FAIR MARKET VALUE: ??

The estimated, realistic dollar value of an asset when categorized as "VA Excess" personal property. This value will replace the current TOTAL ASSET VALUE in the Equipment Inv. file. Note that the current TOTAL ASSET VALUE will automatically be saved as the ORIGINAL ASSET VALUE.

VA Accounting Standards require capitalized nonexpendable property to be recorded in the "Excess" Standard General Ledger (SGL) 1561 at its "Expected Net Realizable Value".

FAIR MARKET VALUE: 5000.00

Should an Adjustment Voucher be created? YES// \< RET\>

A.V. REASON:??

Choose from: ABANDONED/DESTROYED DISPOSAL/EXCESS-SOLD DISPOSAL/SCRAP DISPOSAL/TRADE-IN EIL TO EXCESS

EXCESS TO EIL EXCESS/TRANSFERRED TO OGA EXCESS/TRANSFERRED WITHIN VA OTHER

REPORT OF SURVEY SGL TO SGL

A.V. REASON: EXCESS TO EIL

A.V. COMMENTS:

1\> Had too many of them

2\>\< RET\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES

Sure, you want to process this disposition? YES// \< RET\> Updating the Equipment File...

Sending FD document to FAP. Adjustment Voucher was created.

Editing Equipment Data

USE STATUS: TURNED IN// \< RET\>

CMR: 996// \< RET\> SUPPLY Excess

STANDARD GENERAL LEDGER: 1561// \< RET\> PROPERTY PENDING DISPOSAL

Should a FA Document also be sent? YES// \< RET\> Should an Adjustment Voucher be created? YES// \< RET\>

A.V. REASON:??

Choose from: EIL TO EXCESS TO EIL

INVENTORY PICK UP OTHER

SGL TO SGL

A.V. REASON: EXCESS TO EIL

A.V. COMMENTS:

1\> had too many

2\>\< RET\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES

Sending FA document to FAP... Adjustment Voucher was created.

#### Financial Data Edit (FR Document )

This document is used to edit financial documents that cannot be changed with an FC document.

Select FAP Documents (Code Sheets) Option: fr Financial Data Edit (FR Document) Select EQUIPMENT ENTRY \#: 1 8978899 DEFIBRILLATOR TURNED IN

NEW FUND: AMAF//??

Financial classification of appropriation (based online of business).

Choose from:

4014 Canteen Service

4048 Compensated Work Therapy

4138 Medical Facilities Revolving Fund 4538 Parking Facilities

4539 Franchise Fund

6019 Shared Medical Equipment Purchase 4537B Supply Fund

5014A1 Medical Care Cost Recovery 8129G National Cemetery Gift Fund 8180S General Post Fund

AMAF Assets and Miscellaneous Accounts Fund

NEW FUND: AMAF// \< RET\> Assets and Miscellaneous Accounts Fund NEW ADMINISTRATIVE/OFFICE: 10//??

New A/O (10 for VHA, 20 for VBA, etc.).

Choose from:

10 Veterans Health Administration

20 Veterans Benefits Administration

40 National Cemetery Service

90 Office of Acquisition & Materiel Mgmnt

04 Office of Finance and Info Resources Mgmnt 08 Office of Facilities

NEW ADMINISTRATIVE/OFFICE: 10// \< RET\> Veterans Health Administration NEW FUND CONTROL POINT:??

Used to derive the ACC (field \#31). Free text required because Fund Control Points are subject to change.

NEW FUND CONTROL POINT: \< RET\>

NEW BOC: 3130// \< RET\> MEDICAL, DENTAL & SCIENTIFIC EQUIPMENT NEW CMR: 996// \< RET\> SUPPLY Excess

Should an Adjustment Voucher be created? YES// \< RET\>

A.V. REASON:?

Select reason for adjustment voucher. Applicable reasons for FR Document

Answer with AV REASON NAME

Do you want the entire AV REASON List? y (Yes) Choose from:

FUND TO FUND OTHER

A.V. REASON: fUND TO FUND

A.V. COMMENTS:

1\> sent somewhere else.

2\>\< RET\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES

Sure you want to process these changes? YES// \< RET\> Updating the AEMS/MERS Equipment File.

Sending FR document to FAP. Adjustment Voucher was created.

#### FAP Validity Check for A Single Item (FA Document)

This option will perform a validity check on an entry in the Equipment Inv. file to determine if a FA Document (code sheet) can be created for that entry.

| Select FAP Documents (Code Sheets) Option: |      | v1  | FAP Validity Check for A Single Item (FA |        |           |
|--------------------------------------------|------|-----|------------------------------------------|--------|-----------|
| Document)                                  |      |     |                                          |        |           |
| Select EQUIPMENT INV. ENTRY NUMBER:        | 1071 |     | DEFIBRILLATOR                            | IN USE | 7800-8978 |

Looks OK!

If information is missing, you will receive a message similar to the following.

This record would not have been sent to FAP! Reasons:

Missing Type of Entry Asset not capitalized.

#### FAP Validity Check By CMR (FA Documents)

This option will perform validity checks on equipment belonging to a specified CMR to determine if FA Documents (code sheets) can be created for those equipment entries. Only capitalized (CAPITALIZED field = YES) equipment will be considered.

Equipment which is already established in Fixed Assets will not be checked.

Select FAP Documents (Code Sheets) Option: v2 FAP Validity Check by CMR (FA Documents) This option VALIDATES FA Documents (code sheets)

for all equipment that belongs to a specified CMR. Select CMR NAME:??

Choose from:

100 DENTAL

110 DIETETIC

451 VOLUNTARY

^

Select CMR NAME: 381 MEDICAL ADMINISTRATION

Now select the device to print results on. DEVICE: HOME// \<RET\> LAN

FA DOCUMENT VALIDITY CHECK FOR CMR: 381 APR 04, 1996@10:29:05 page 1

5 records have been processed from CMR: 381.

0 records would have been sent to FAP.

2.  would not have been sent due to already being established in FAP.
3.  would not have been sent due to validation problems.

Equipment Records not sent because of validation problems: Entry \# Reason

1125 Acquisition Month Missing

1125 Replacement Month Missing

1126 Acquisition Month Missing

1126 Replacement Month Missing

1127 Acquisition Month Missing

1127. Replacement Month Missing

#### FAP Validity Check by Station (FA Documents)

This option will perform validity checks on equipment belonging to a station to determine if FA Documents (code sheets) can be created for those equipment entries. Only capitalized (CAPITALIZED field = YES) equipment which is on a CMR (CMR field not blank) will be considered. Equipment which is already established in Fixed Assets will not be checked.

Select FAP Documents (Code Sheets) Option: v3 FAP Validity Check by Station (FA Documents)

This option VALIDATES FA Documents (code sheets)

for all equipment that belongs to a specified Station.

STATION NUMBER: 999// \<RET\>

Now select the device to print results on. DEVICE: HOME// \<RET\> LAN

FA DOCUMENT VALIDITY CHECK FOR STATION: 999 APR 04, 1996@10:29:38 page 1

85 records have been processed from STATION: 999.

28 records would have been sent to FAP.

44 would not have been sent due to already being established in FAP.

13 would not have been sent due to validation problems.

Equipment Records not sent because of validation problems: Entry \# Reason

9 Missing Acquisition Date

9 Missing Life Expectancy

9 Invalid CSN

1065 Missing Acquisition Date

1066 Missing Acquisition Date

1068 Missing General Ledger Account 1068 Missing Category Stock Number 1068 Missing Fund

1068 Missing A.O. Code

1068 Missing Budget Object Code

1068 Missing Equity Account

1117 Acquisition Month Missing

1120 Missing Type of Entry

1125 Acquisition Month Missing

1125 Replacement Month Missing

1126 Acquisition Month Missing

1126 Replacement Month Missing

1127 Acquisition Month Missing

1127 Replacement Month Missing

1170 Not non-expendable

1171 Missing General Ledger Account

1171 Missing Fund

1171 Missing A.O. Code

1171 Missing Budget Object Code

1171 Missing Equity Account

1172 Missing A.O. Code

1172 Missing Equity Account

1173 Missing Fund

1173 Missing A.O. Code

1173 Missing Equity Account

#### Adjustment Voucher Entry

Select FAP Documents (Code Sheets) Option: AV Adjustment Voucher Entry Select Type of FAP Document: (FA/FB/FC/FD/FR):??

Choose the type of FAP Document for which an Adjustment Voucher should be created. After the type is chosen, you will be asked to select the specific FAP Document.

Select one of the following: FA FA DOCs

FB FB DOCs

FC FC DOCs

FD FD DOCs

FR FR DOCs

Select Type of FAP Document: (FA/FB/FC/FD/FR): FA DOCs

| 1         | 07-16-97 | 5007N0012 | 8978899       | DEFIBRILLATOR | TURNED IN |
|-----------|----------|-----------|---------------|---------------|-----------|
| 7530-4565 |          |           |               |               |           |
| 1         | 07-16-97 | 5007N0015 | 8978899       | DEFIBRILLATOR | TURNED IN |
| 7530-4565 |          |           |               |               |           |
| 178       | 07-16-97 | 5007N0013 | 4758694949494 |               | IN USE    |
| 196       | 06-11-97 | 9997N0001 |               |               | IN USE    |

Select FA DOCUMENT (by Transaction Number or Equipment ENTRY \#):?? Choose from:

Select FA DOCUMENT (by Transaction Number or Equipment ENTRY \#): 178 475

8694949494 IN USE 07-16-97 5007N0013

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 34%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 7%" />
<col style="width: 2%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>ADJ. VOUCHER DATE/TIME</th>
<th><p>TRANSACTION .............</p>
<p>CODE NUMBER DATE</p></th>
<th></th>
<th>STN</th>
<th></th>
<th>FUND</th>
<th></th>
<th>SGL NET AMOUNT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EQUIP #:</td>
<td><p>FA 5007N0013 07/16/97</p>
<p><strong>178</strong> SNOWMOBILE</p></td>
<td></td>
<td>500</td>
<td></td>
<td>AMAF</td>
<td></td>
<td>1750 5,000.00</td>
</tr>
</tbody>
</table>

Should an Adjustment Voucher be created? YES// y YES

A.V. REASON:??

Choose from: EIL TO EXCESS TO EIL

INVENTORY PICK UP OTHER

SGL TO SGL

A.V. REASON: EXCESS TO EIL

A.V. COMMENTS:

1\> Global warming made equipment unnecessary.

2\>\< RET\>

EDIT Option: \< RET\>

Is adjustment voucher correct? y YES Adjustment Voucher was created.

Select Type of FAP Document: (FA/FB/FC/FD/FR):

#### Recalculate FAP Balances

Dollar balances (by Station, Fund, SGL, and month) are maintained in the FAP BALANCES file and printed on the Voucher Summary report. This option can be used to recalculate the balances if they appear incorrect.

The net \$ activity for a specified month will be computed from the individual FAP code sheets. The results are then compared to the values maintained in the FAP BALANCES file. If there are any discrepancies, the recalculated values can be used to update the FAP BALANCES file.

Select FAP Documents (Code Sheets) Option: recalculate FAP Balances Enter month to recalculate: Mar 1996// \<RET\> (MAR 1996)

You have chosen to recalculate the \$ from FAP transactions during the month of Mar 1996.

OK to proceed? y YES

Calculating net activity from transactions... Comparing FAP BALANCES file with transactions... Comparing transactions with FAP BALANCES file...

No problems were found.

### Fixed Assets Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fixed Assets reports are intended for use during monthly reconciliation and can be compared with the Inventory Report (Report ID: RGLLIAV) which is produced by the FMS system.

Select Nonexpendable Equipment Module (A&MM) Option: 6 Fixed Assets Reports

Voucher Summary for Station Adjustment Voucher Report

Document History (FAP) for Equipment, Equipment Not Reported to FAP Excessed Equipment Report

Summary of SGL Balances Transaction Register (FAP Documents)

Voucher Summary for Station

This option generates a voucher summary report for a specified station and accounting period. The data is obtained from FAP documents which have an impact on dollars for a Fund and Standard General Ledger. The output can be used to reconcile FAP transactions with FMS transactions. The Inventory Report (Report ID: RGLLIAV) from FMS is the anticipated source of information on FMS transactions.

Adjustment Voucher Report

This option generates a report of adjustment vouchers for a selected date range. Adjustment vouchers are used to communicate information to Fiscal concerning selected FAP Documents. Each adjustment voucher is associated with one FAP Document. Not all FAP Documents have an adjustment voucher.

It is recommended that this option be scheduled to automatically print on a daily basis (via TaskManager). If automatically queued, the report will include all adjustment vouchers created on the previous day.

Document History (FAP) for Equipment

This option lists Fixed Assets (FAP) documents (code sheets) which have been sent for a specified equipment item.

Equipment Not Reported to FAP

This option generates a report of capitalized non-expendable (NX) equipment which is not currently established in Fixed Assets (FAP). Equipment which has a disposition date will not be included in the output.

This report is intended to identify equipment items which should be established in Fixed Assets by transmission of a FA Document (code sheet).

It is recommended that this option be scheduled to automatically print on a weekly basis (via TaskManager).

Excessed Equipment Report

This option generates a report of FA Documents (code sheets) which were transmitted to FAP for standard general ledger 1561 (excess). This list is intended to identify equipment assets which should have been picked up in the FMS excess account by Fiscal Service.

It is recommended that this option be scheduled to automatically print on a monthly basis (via TaskManager). If automatically queued, the report will include FA Documents transmitted within the last 30 days or so.

Summary of SGL Balances

This option generates a report of closing dollar balances by Standard General Ledger for a specified month. This data is obtained from FAP Documents (FA, FB, FC, FD, and FR) that have been sent by the site. The output is sorted by Station and optionally by Fund.

Transaction Register (FAP Documents)

This option generates a list of FAP Documents for a specified date range.

#### Voucher Summary for Station

Only FAP documents which impact the dollars for a fund or SGL are included in the output. (e.g. an FC document which only changed the CMR value will not be listed on this voucher summary). The output is sorted by Fund, SGL, and transaction date/time.

The Voucher Summary asks for a station, start date, and end date. The start date defaults to the first day of the previous month. The end date defaults to the last day of the month which was selected for the start date.

Select Fixed Assets Reports Option: voucher Summary for Station, STATION NUMBER: 999// \< RET\>

Start Date: 6/1/97// \< RET\> (JUN 01, 1997) End Date: 6/30/97// \< RET\> (JUN 30, 1997)

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

VOUCHER SUMMARY FOR STATION: 999 JUL 17, 1997@09:35:56 page 1 FUND: AMAF MISC ACCOUNTING PERIOD FROM 6/1/97 TO 6/30/97.

NET AMOUNT EQUIP P.O.#

\$0.00

1,000.00 A33004

-1,000.00 A33004

0.00

\$0.00

\$0.00

6,175.00 A11002

5,570.40 A22002

5,570.40 A22002

5,570.40 A22002

5,570.40 A22002

TRANSACTION EQUIP ID# CODE NUMBER DATE

SGL: 1561 EXCESS

Opening Balance for Jun 1997: FA 9997N0011 6/11/97 204

FD 9997N0002 6/11/97 204

G/L Acct 1561 Net Activity: Closing Balance for Jun 1997:

SGL: 1750 NX EQUIP

Opening Balance for Jun 1997: FA 9997N0001 6/11/97 196

| FA  | 9997N0002 | 6/11/97 | 198 |
|-----|-----------|---------|-----|
| FA  | 9997N0003 | 6/11/97 | 199 |
| FA  | 9997N0004 | 6/11/97 | 200 |
| FA  | 9997N0005 | 6/11/97 | 201 |

VOUCHER SUMMARY FOR STATION: 999

JUL 17, 1997@09:35:56

page 2

FUND: AMAF MISC ACCOUNTING PERIOD FROM 6/1/97 TO 6/30/97

TRANSACTION EQUIP ID# NET AMOUNT EQUIP P.O.# CODE NUMBER DATE

­

SGL: 1750 NX EQUIP (continued)

FA 9997N0007 6/11/97 203 8,246.00 A33002

FA 9997N0008 6/11/97 204 7,417.23 A33004

FA 9997N0009 6/11/97 205 7,417.23 A33004

FA 9997N0010 6/11/97 206 7,417.23 A33004

FC 9997N0001 6/11/97 204 33.27 A33004

FD 9997N0001 6/11/97 204 -7,450.50 A33004

G/L Acct 1750 Net Activity: 51,537.06

Closing Balance for Jun 1997: \$51,537.06

#### Adjustment Voucher Report

Select Fixed Assets Reports Option: adjustment Voucher Report Start Date: T-1// \< RET\> (JUL 16, 1997)

End Date: Jul 16, 1997// \< RET\> (JUL 16, 1997)

Sort by person that created the Adj. Voucher? NO// y YES Include all users? YES// \< RET\>

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

ADJUSTMENT VOUCHERS JUL 17, 1997@09:36:35 page 1 FROM 7/16/97 TO 7/16/97 (SORT BY USER FOR ALL USERS)

A.V.s by: ENDI R, ONE

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 2%" />
<col style="width: 41%" />
<col style="width: 2%" />
<col style="width: 7%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>ADJ. VOUCHER DATE/TIME</th>
<th></th>
<th><p>...... TRANSACTION STN</p>
<p>CODE NUMBER DATE</p></th>
<th></th>
<th>FUND</th>
<th></th>
<th>SGL</th>
<th></th>
<th>NET AMOUNT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/16/97@15:28</td>
<td></td>
<td>FA 5007N0012 07/16/97 500</td>
<td></td>
<td>AMAF</td>
<td></td>
<td>1750</td>
<td></td>
<td>7,200.00</td>
</tr>
</tbody>
</table>

EQUIP \#: 1 DEFIBRILLATOR W/O MONITOR

P.O. \#: A006754 A.V. REASON: EXCESS TO EIL COMMENTS: Had too many.

07/16/97@15:38 FB 5007N0002 07/16/97 500 AMAF 1750 1,000.00 EQUIP \#: 1 DEFIBRILLATOR W/O MONITOR

P.O. \#: A006754 A.V. REASON: ASSET VALUE VARIANCE/ADJUSTMENT (+) (-) COMMENTS: explain the adjustment voucher.

07/16/97@15:40 FC 5007N0002 07/16/97 500 AMAF 1750 0.00

EQUIP \#: 1 DEFIBRILLATOR W/O MONITOR

P.O. \#: A006754 A.V. REASON: ASSET VALUE VARIANCE/ADJUSTMENT (+) (-) Transaction: FC-5007N0002 (continued)

COMMENTS: repair extended life

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 43%" />
<col style="width: 11%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><p>07/16/97@15:42 FD EQUIP #: 1</p>
<p>P.O. #: A006754</p></th>
<th><p>5007N0003 07/16/97 500 AMAF DEFIBRILLATOR W/O MONITOR</p>
<p>A.V. REASON: EXCESS TO EIL</p></th>
<th>1750</th>
<th>-8,200.00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>COMMENTS: Had too</td>
<td>many of them</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>07/16/97@15:43 FA EQUIP #: 1</p>
<p>P.O. #: A006754</p>
<p>COMMENTS: had too</p></td>
<td><p>5007N0015 07/16/97 500 AMAF DEFIBRILLATOR W/O MONITOR</p>
<p>A.V. REASON: EXCESS TO EIL</p>
<p>many</p></td>
<td>1561</td>
<td>5,000.00</td>
</tr>
<tr class="odd">
<td><p>07/16/97@15:45 FR EQUIP #: 1</p>
<p>P.O. #: A006754</p></td>
<td><p>5007N0002 07/16/97 500 AMAF DEFIBRILLATOR W/O MONITOR</p>
<p>A.V. REASON: FUND TO FUND</p></td>
<td>1561</td>
<td>0.00</td>
</tr>
</tbody>
</table>

COMMENTS: sent somewhere else

07/16/97@16:01 FA 5007N0013 07/16/97 500 AMAF 1750 5,000.00 EQUIP \#: 178 SNOWMOBILE

P.O. \#: A40020 A.V. REASON: EXCESS TO EIL COMMENTS: Global warming made equipment unnecessary.

TOTALS:

| 500 | AMAF  | 1561 5,000.00   |
|-----|-------|-----------------|
| 500 | AMAF  | 1750 5,000.00   |
|     |       | ---------------­ |
| 500 | AMAF  | TOTAL 10,000.00 |
|     |       | ---------------­ |
| 500 | TOTAL | 10,000.00       |

================

USER TOTAL 10,000.00

#### Document History (FAP) for Equipment

This option lists Fixed Assets (FAP) documents (code sheets) which have been sent for a specified equipment item.

Select Fixed Assets Reports Option: document History (FAP) for Equipment Select EQUIPMENT ENTRY \#: 8978899 1 8978899 DEFIBRILLATOR TURNED

IN 7530-4565

Include transaction details? YES// \< RET\>

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

FAP DOCUMENT HISTORY FOR EQUIPMENT JUL 17, 1997@09:37:40 page 1 ENTRY \#: 1 CURRENT VALUE: \$5,000.00

TRANSACTION

STA SGL DOCUMENT VALUE SENDER ASSET VALUE

NBR AFTER DOCUMENT

CODE\* NUMBER DATE

FA 00 5007N0012 07/16/97 500 1750 \$7,200.00 BARKER \$7,200.00

CSN: 6515-438660 (DEFIBRILL-CARDIOSCOPE)

| NATIONAL EIL: 11   | COST CENTER: 824300 | ACQ METH: PURCHASED     |
|--------------------|---------------------|-------------------------|
| ACQ DATE: 06/04/86 | LE: 8               | REPL DATE: 06/04/94     |
| BOC: 3130          | A/O: 10             | EQUITY ACCOUNT: MEDICAL |
| P.O.#: A006754     |                     |                         |

FB 01 5007N0002 07/16/97 500 1750 \$1,000.00 BARKER \$8,200.00

DESCRIPTION: Description of the betterment P.O.#: A006754 ACQ DATE: 07/16/97 ACQ METH: PURCHASED

\* Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. FAP DOCUMENT HISTORY FOR EQUIPMENT JUL 17, 1997@09:37:40 page 2

ENTRY \#: 1 CURRENT VALUE: \$5,000.00

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TRANSACTION STA</p>
<p>CODE* NUMBER DATE NBR</p></th>
<th><p>SGL DOCUMENT</p>
<p>VALUE</p></th>
<th>SENDER</th>
<th><p>ASSET AFTER</p>
<p>VALUE DOCUMENT</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FC</p>
<p>00 5007N0002</p>
<p>07/16/97 500</p>
<p>P.O.#:</p></td>
<td><p>1750</p>
<p>A006754</p>
<p>$7,200.00</p></td>
<td>ENDI R, ONE</td>
<td>$8,200.00</td>
</tr>
</tbody>
</table>

REPL DATE CHANGED OLD: Jun 04, 1994 NEW: Jun 04, 1998

FD T 5007N0003 07/16/97 500 1750 ENDI R, ONE \$8,200.00

TURN-IN DATE: 07/16/97 DISP AUTHORITY: 00000

FA 00 5007N0015 07/16/97 500 1561 \$5,000.00 ENDI R, ONE \$5,000.00

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>NATIONAL EIL: 99</th>
<th>CSN: 6515-438660 COST CENTER:</th>
<th>(DEFIBRILL-CARDIOSCOPE) ACQ METH: PURCHASED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACQ DATE: 06/04/86</td>
<td>LE:</td>
<td>REPL DATE: //</td>
</tr>
<tr class="even">
<td><p>BOC: 3130</p>
<p>P.O.#: A006754</p></td>
<td>A/O: 10</td>
<td>EQUITY ACCOUNT: MEDICAL</td>
</tr>
</tbody>
</table>

\* Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

FAP DOCUMENT HISTORY FOR EQUIPMENT JUL 17, 1997@09:37:40 page 3 ENTRY \#: 1 CURRENT VALUE: \$5,000.00

TRANSACTION

STA

NBR SGL DOCUMENT VALUE SENDER ASSET

VALUE

AFTER

DOCUMENT

CODE\* NUMBER DATE

FR 5007N0002 07/16/97 500 1561 BARKER \$5,000.00

\* Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Select EQUIPMENT ENTRY \#:

#### Equipment Not Reported to FAP

This option generates a report of capitalized nonexpendable (NX) equipment which is not currently established in Fixed Assets (FAP). Equipment which has a disposition date will not be included in the output. This report is intended to identify equipment items which should be established in Fixed Assets by transmission of a FA Document (code sheet).

Is recommended that this option be scheduled to automatically print on a weekly basis (via TaskManager).

Select Fixed Assets Reports Option: Equipment Not Reported to FAP

This report searches the entire equipment file and may take some time to complete.

Consider queuing this report to run after-hours. DEVICE: HOME// \< RET\>

UCX/TELNET RIGHT MARGIN: 80//

CAPITALIZED NX EQUIP. NOT REPORTED TO FAP JUL 17, 1997@09:37:58 page 1.

| ENTRY# |     | ACQ. DATE |     | ASSET VALUE  |     | STATION FUND |     | SGL |     | CSN |     | CMR |
|--------|-----|-----------|-----|--------------|-----|--------------|-----|-----|-----|-----|-----|-----|
| 42     |     | MAY 1989  |     | \$115,748.20 |     | 999          |     |     |     |     |     | 041 |
| 45     |     | DEC 1987  |     | \$5,066.24   |     | 999          |     |     |     |     |     | 13A |
| 51     |     | JUN 1988  |     | \$110,000.00 |     | 999          |     |     |     |     |     | 20G |
| 63     |     | DEC 1987  |     | \$11,434.77  |     | 999          |     |     |     |     |     | 43C |
| 64     |     | NOV 1985  |     | \$6,068.25   |     | 999          |     |     |     |     |     | 422 |
| 65     |     | OCT 1987  |     | \$10,502.00  |     | 999          |     |     |     |     |     | 43F |
| 66     |     | NOV 1990  |     | \$8,479.94   |     | 999          |     |     |     |     |     | 43F |
| 67     |     | APR 1988  |     | \$17,150.00  |     | 999          |     |     |     |     |     | 20D |
| 68     |     | NOV 1989  |     | \$9,591.00   |     | 999          |     |     |     |     |     | 20C |
| 78     |     | FEB 1988  |     | \$5,468.75   |     | 999          |     |     |     |     |     | 422 |
| 80     |     | MAR 1988  |     | \$5,593.75   |     | 999          |     |     |     |     |     | 422 |
| 84     |     | JAN 1989  |     | \$6,486.00   |     | 999          |     |     |     |     |     | 423 |
| 89     |     | OCT 1987  |     | \$14,442.69  |     | 999          |     |     |     |     |     | 43B |
| 91     |     | FEB 1986  |     | \$17,100.00  |     | 999          |     |     |     |     |     | 20B |
| 102    |     | DEC 1989  |     | \$17,518.32  |     | 999          |     |     |     |     |     | 37A |
| 106    |     | OCT 1985  |     | \$9,406.07   |     | 999          |     |     |     |     |     | 170 |
| 110    |     | MAR 1990  |     | \$5,588.00   |     | 999          |     |     |     |     |     | 13B |
| 126    |     | DEC 1989  |     | \$17,518.33  |     | 999          |     |     |     |     |     | 37A |
| 133    |     | NOV 1987  |     | \$6,817.32   |     | 999          |     |     |     |     |     | 19A |

19 capitalized NX equipment entries have not been reported to Fixed Assets.

Enter RETURN to continue or '^' to exit:

#### Excessed Equipment Report

This option generates a report of FA Documents (code sheets) which were transmitted to FAP for standard general ledger 1561 (excess). This list is intended to identify equipment assets which should have been picked up in the FMS excess account by Fiscal Service.

It is recommended that this option be scheduled to automatically print on a monthly basis (via TaskManager). If automatically queued, the report will include FA Documents transmitted within the last 30 days or so.

Select Fixed Assets Reports Option: Excessed Equipment Report

Start Date: 6/17/97// \< RET\> (JUN 17, 1997)

End Date: 7/17/97// \< RET\> (JUL 17, 1997)

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">FA DOCUMENTS FOR EXCESS EQUIP. (SGL 1561) ACCOUNTING PERIOD FROM 6/17/97 TO 7/17/97</th>
<th colspan="2">JUL 17, 1997@09:38:17</th>
<th>page 1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STATION FUND</td>
<td>TRANSACTION</td>
<td></td>
<td>EQUIPMENT</td>
<td>ASSET VALUE</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>CODE NUMBER</td>
<td>DATE</td>
<td>ENTRY #</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><p>500 AMAF FA 5007N0015 7/16/97</p>
<p>Enter RETURN to continue or '^' to exit:</p></td>
<td>1</td>
<td>5,000.00</td>
<td></td>
</tr>
</tbody>
</table>

#### Summary of SGL Balances

Select Fixed Assets Reports Option: summary of SGL Balances

Enter month of desired closing balances: Jun 1997// \< RET\> (JUN 1997) Report SGL totals by Fund? YES// \< RET\>

DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

Jun 1997 CLOSING BALANCES FOR STATION: 500 JUL 17, 1997@09:38:32 page 1

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th>FUND</th>
<th><p>STANDARD</p>
<p>GENERAL</p>
<p>LEDGER</p></th>
<th><p>TOTAL</p>
<p>ASSET</p>
<p>VALUE</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5014A1</td>
<td>1751</td>
<td>$ 6,194.48</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>----------------­</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>$ 6,194.48</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>----------------­</td>
</tr>
</tbody>
</table>

STATION TOTAL \$ 6,194.48

Enter RETURN to continue or '^' to exit:

Jun 1997 CLOSING BALANCES FOR STATION: 999 JUL 17, 1997@09:38:32 page 2 STANDARD TOTAL

GENERAL ASSET FUND LEDGER VALUE

------ -------- ----------------­ AMAF 1750 \$ 51,537.06

----------------­

\$ 51,537.06

----------------­

STATION TOTAL \$ 51,537.06

Enter RETURN to continue or '^' to exit:

#### Transaction Register (FAP Documents)

Select Fixed Assets Reports Option: transaction Register (FAP Documents) Start Date: 6/1/97// \< RET\> (JUN 01, 1997)

End Date: 6/30/97// \< RET\> (JUN 30, 1997)

Include Adjustment Voucher data? YES// \< RET\> DEVICE: HOME// \< RET\> UCX/TELNET RIGHT MARGIN: 80//

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 1

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FA 00 9997N0001 06/11/97 999 AMAF 1750 6,175.00 ENCHI EF, ONE

ENTRY \#: 196 CSN: 6530-439473 (BED ADJUSTABLE)

NATIONAL EIL: 20 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 01/09/92 LE: 12 REPL DATE: 01/09/04.

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A11002

FA 00 9997N0002 06/11/97 999 AMAF 1750 5,570.40 ENCHI EF, ONE

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ENTRY #: 198</p>
<p>NATIONAL EIL: 20</p></th>
<th>CSN: 6515-438660 COST CENTER:</th>
<th>(DEFIBRILL-CARDIOSCOPE) ACQ METH: PURCHASED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACQ DATE: 02/18/93</td>
<td>LE: 8</td>
<td>REPL DATE: 02/18/01</td>
</tr>
<tr class="even">
<td>BOC: 3130</td>
<td>A/O: 10</td>
<td>EQUITY ACCOUNT: MEDICAL</td>
</tr>
<tr class="odd">
<td>P.O.#: A22002</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

\* Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 2

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FA 00 9997N0003 06/11/97 999 AMAF 1750 5,570.40 ENCHI EF, ONE

ENTRY \#: 199 CSN: 6515-438660 (DEFIBRILL-CARDIOSCOPE) NATIONAL EIL: 20 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 02/18/93 LE: 8 REPL DATE: 02/18/01.

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A22002

FA 00 9997N0004 06/11/97 999 AMAF 1750 5,570.40 ENCHI EF, ONE

ENTRY \#: 200 CSN: 6515-438660 (DEFIBRILL-CARDIOSCOPE) NATIONAL EIL: 20 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 02/18/93 LE: 8 REPL DATE: 02/18/01.

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A22002

\* Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 3

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FA 00 9997N0005 06/11/97 999 AMAF 1750 5,570.40 ENCHI EF, ONE

ENTRY \#: 201 CSN: 6515-438660 (DEFIBRILL-CARDIOSCOPE) NATIONAL EIL: 20 COST CENTER: ACQ METH: PURCHASED

ACQ DATE: 02/18/93 LE: 8 REPL DATE: 02/18/01

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A22002

FA 00 5007N0006 06/11/97 500 AMAF 1751 5,844.48 ENCHI EF, ONE

ENTRY \#: 202 CSN: 7021-438121 (COMPUTER DIGITAL) NATIONAL EIL: 78 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 11/10/93 LE: 8 REPL DATE: 11/10/01.

BOC: 3123 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A33001

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

| TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 |          |     |      | JUL 17, 1997@09:38:47 |            |               | page 4 |
|---------------------------------------------|----------|-----|------|-----------------------|------------|---------------|--------|
| ...... TRANSACTION .......                  |          | STN | FUND | SGL                   | NET AMOUNT | SENDER        |        |
| CODE\* NUMBER                               | DATE     |     |      |                       |            |               |        |
|                                             |          |     |      |                       |            |               |        |
| FA 00 9997N0007                             | 06/11/97 | 999 | AMAF | 1750                  | 8,246.00   | ENCHI EF, ONE |        |

ENTRY \#: 203 CSN: 3610-438992 (COPY & DUP MACH THER)

NATIONAL EIL: 18 COST CENTER: ACQ METH: PURCHASED

ACQ DATE: 09/23/93 LE: 10 REPL DATE: 09/23/03

BOC: 3121 A/O: 10 EQUITY ACCOUNT: MEDICAL

P.O.#: A33002

FA 00 9997N0008 06/11/97 999 AMAF 1750 7,417.23 ENCHI EF, ONE

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ENTRY #: 204</p>
<p>NATIONAL EIL: 10</p></th>
<th>CSN: 6520-439367 COST CENTER:</th>
<th>(CHAIR DENTAL OPERTING) ACQ METH: PURCHASED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACQ DATE: 10/06/94</td>
<td>LE: 15</td>
<td>REPL DATE: 06/11/12</td>
</tr>
<tr class="even">
<td>BOC: 3130</td>
<td>A/O: 10</td>
<td>EQUITY ACCOUNT: MEDICAL</td>
</tr>
<tr class="odd">
<td>P.O.#: A33004</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 5

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FA 00 9997N0009 06/11/97 999 AMAF 1750 7,417.23 ENCHI EF, ONE

ENTRY \#: 205 CSN: 6520-439367 (CHAIR DENTAL OPERTING) NATIONAL EIL: 10 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 10/06/94 LE: 15 REPL DATE: 06/11/12.

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A33004

FA 00 9997N0010 06/11/97 999 AMAF 1750 7,417.23 ENCHI EF, ONE

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ENTRY #: 206</p>
<p>NATIONAL EIL: 10</p></th>
<th>CSN: 6520-439367 COST CENTER:</th>
<th>(CHAIR DENTAL OPERTING) ACQ METH: PURCHASED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACQ DATE: 10/06/94</td>
<td>LE: 15</td>
<td>REPL DATE: 06/11/12</td>
</tr>
<tr class="even">
<td>BOC: 3130</td>
<td>A/O: 10</td>
<td>EQUITY ACCOUNT: MEDICAL</td>
</tr>
<tr class="odd">
<td>P.O.#: A33004</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 6

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FB 01 5007N0001 06/11/97 500 AMAF 1751 350.00 ENCHI EF, ONE

ENTRY \#: 202 DESCRIPTION: ADDITIONAL MEMORY (16M) P.O.#: A33001 ACQ DATE: 06/11/97 ACQ METH: PURCHASED

FC 00 9997N0001 06/11/97 999 AMAF 1750 33.27 ENCHI EF, ONE

ENTRY \#: 204 P.O.#: A33004

ASSET VALUE CHANGED OLD: 7417.23 NEW: 7450.50

AV REASON: ASSET VALUE VARIANCE DATE: JUN 11, 1997 BY: ENCHI EF, ONE

AV COMMENTS: Additional charges will be incurred.

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 7

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FR 5007N0001 06/11/97 500 AMAF 1751 -6,194.48 ENCHI EF, ONE

5014A1 1751 6,194.48

ENTRY \#: 202

FUND CHANGED OLD: AMAF NEW: 5014A1.

COST CENTER CHANGED OLD: NEW: 847000

AV REASON: FUND TO FUND DATE: JUN 11, 1997 BY: ENCHI EF, ONE

AV COMMENTS: Originally picked up in wrong Fund.

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

| Equipment Management                        |           |          |     |      |                     |            |               |        |
|---------------------------------------------|-----------|----------|-----|------|---------------------|------------|---------------|--------|
| Nonexpendable Equipment Module (A&MM)       |           |          |     |      |                     |            |               |        |
| TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 |           |          |     |      | JUL 17, 1997@09:38: |            | 47            | page 8 |
| ...... TRANSACTION .......                  |           |          | STN | FUND | SGL                 | NET AMOUNT | SENDER        |        |
| CODE\* NUMBER                               |           | DATE     |     |      |                     |            |               |        |
|                                             |           |          |     |      |                     |            |               |        |
| FD T                                        | 9997N0001 | 06/11/97 | 999 | AMAF | 1750                | -7,450.50  | ENCHI EF, ONE |        |

ENTRY \#: 204 TURN-IN DATE: 06/10/97 DISP AUTHORITY: 00000

FA 00 9997N0011 06/11/97 999 AMAF 1561 1,000.00 ENCHI EF, ONE

ENTRY \#: 204 CSN: 6520-439367 (CHAIR DENTAL OPERTING) NATIONAL EIL: 99 COST CENTER: ACQ METH: PURCHASED ACQ DATE: 10/06/94 LE: REPL DATE: //

BOC: 3130 A/O: 10 EQUITY ACCOUNT: MEDICAL P.O.#: A33004

AV REASON: EIL TO EXCESS DATE: JUN 11, 1997 BY: ENCHI EF, ONE

AV COMMENTS: Moving to excess account.

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

TRANSACTION REGISTER FROM 6/1/97 TO 6/30/97 JUL 17, 1997@09:38:47 page 9

...... TRANSACTION ....... STN FUND SGL NET AMOUNT SENDER CODE\* NUMBER DATE

­

FD D 9997N0002 06/11/97 999 AMAF 1561 -1,000.00 ENCHI EF, ONE

ENTRY \#: 204 DISP DATE: 06/11/97 DISP AUTHORITY: 00000 SELLING PRICE: 0.00 DISP METHOD: SCRAPPED

Betterment \# follows FB and FC. T (Turn-In) or D (Final Disp.) follows FD. Enter RETURN to continue or '^' to exit:

### Import Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VistA Option to Import data from an input file into the EQUIPMENT INV. File (#6914)

VistA Option

EN IMPORT NEW EQUIP INV. RECS

Input File

A Microsoft Excel worksheet should be used to create the new data which should be exported when complete to a tab-delimited text file.

The first row of the spreadsheet contains all the names of the fields to be imported, and match to the data dictionary of the EQUIPMENT INVENTORY File (#6914). Note that the order of the columns in the spreadsheet is not important because the code in routine ENIMPORT will use the names not the order of the columns.

Only NEW records are created. NO existing records are updated.

Structure of the input Microsoft Excel file

The input file, as stated above, must be in tab-delimited text format. This is a screen snapshot of the top left corner of a sample spreadsheet in the XLSX format prior to export to the tab-delimited text format:

Figure 1 Input Microsoft Excel File

![](en-version-7-user-manual/005.png)

The spreadsheet has 37 columns. 10 of these are ignored during the input process because they are either auto created during the update by triggers from another field or are there for informational purposes only. 27 columns/VistA fields are imported.

|           |     | COLUMN | VISTA FIELD NAME        | TYPE IF NOT TEXT |     | POINTER TO FILE | VALIDATE API (M CODE) | IGNORED IN IMPORT? |
|-----------|-----|--------|-------------------------|------------------|-----|-----------------|-----------------------|--------------------|
| 1         |     | A      | MANUFACTURER            |                  |     | 6912            |                       |                    |
| 2         |     | B      | SERIAL \#               |                  |     |                 | VALSN                 |                    |
| 3         |     | C      | MODEL                   |                  |     |                 |                       |                    |
| 4         |     | D      | CATEGORY STOCK NUMBER   |                  |     | 6917            |                       |                    |
| 5         |     | E      | LIFE EXPECTANCY         | AUTOFILL         |     |                 |                       |                    |
| 6         |     | F      | MFGR. EQUIPMENT NAME    |                  |     |                 |                       |                    |
| 7         |     | G      | CMR                     |                  |     | 6914.1          |                       |                    |
| 8         |     | H      | EQUIPMENT CATEGORY      |                  |     | 6911            |                       |                    |
| 9         |     | I      | ADDITIONAL INFORMATION  |                  |     |                 |                       | IGNORE             |
| 10        |     | J      | PURCHASE ORDER \#       |                  |     |                 |                       |                    |
| 11        |     | K      | ACQUISITION METHOD      | SET              |     |                 |                       |                    |
| 12        |     | L      | VENDOR POINTER          | AUTOFILL         |     | 440             |                       |                    |
| 13        |     | M      | LEASE COST              |                  |     |                 | VALMAX                |                    |
| 14        |     | N      | TOTAL ASSET VALUE       |                  |     |                 | VALMAX                |                    |
| 15        |     | O      | ACQUISITION DATE        | DATE             |     |                 | VALDA                 |                    |
| 16        |     | P      | WARRANTY EXP. DATE      | DATE             |     |                 | VALDA                 |                    |
| 17        |     | Q      | REPLACEMENT DATE        | AUTOFILL         |     |                 |                       |                    |
| 18        |     | R      | ACQUISITION SOURCE      |                  |     | 420.8           |                       |                    |
| 19        |     | S      | TYPE OF ENTRY           | SET              |     |                 |                       |                    |
| 20        |     | T      | USE STATUS              | SET              |     |                 |                       |                    |
| 21        |     | U      | PARENT SYSTEM           |                  |     | 6914            | VALPARNT              |                    |
| 22        |     | V      | SERVICE POINTER         | AUTOFILL         |     | 49              |                       |                    |
| 23        |     | W      | LOCATION OF ITEM        |                  |     |                 |                       | IGNORE             |
| 24        |     | X      | LOCATION                |                  |     | 6928            |                       |                    |
| 25        |     | Y      | LOCAL IDENTIFIER        |                  |     |                 | VALLCLID              |                    |
| 26        |     | Z      | STATION NUMBER          |                  |     |                 |                       |                    |
| 27        |     | AA     | CONTROLLED ITEM?        | SET              |     |                 |                       |                    |
| 28        |     | AB     | INVESTMENT CATEGORY     | SET              |     |                 |                       |                    |
| 29        |     | AC     | FUND                    |                  |     | 6914.6          |                       |                    |
| 30        |     | AD     | FUND CONTROL POINT      |                  |     |                 |                       |                    |
| 31        |     | AE     | BUDGET OBJECT CODE      |                  |     | 6914.4          |                       |                    |
| 32        |     | AF     | STANDARD GENERAL LEDGER | AUTOFILL         |     | 6914.3          |                       |                    |
| 33        |     | AG     | ADMINSTRATIVE OFFICE    |                  |     | 6914.7          |                       |                    |
| 34        |     | AH     | EQUITY ACCOUNT          | SET              |     |                 |                       |                    |
| 35        |     | AI     | ASSET TAG \#            |                  |     |                 |                       | IGNORE             |
| 36        |     | AJ     | MACHINE TYPE            |                  |     |                 |                       | IGNORE             |
| 37        |     | AK     | COMMENTS                | WP               |     |                 |                       |                    |
|           |     |        |                         |                  |     |                 |                       |                    |
| IGNORED:  |     |        | 5                       |                  |     |                 |                       |                    |
| AUTOFILL: |     |        | 5                       |                  |     |                 |                       |                    |
| PROCESS:  |     |        | 27                      |                  |     |                 |                       |                    |

Row \#1 is a list of the VistA field names.

Row \#2 is a memo row showing the VistA file and fields. It is not used in the import process.

Row \#3 is a memo showing validation criteria and is not used for validation in the import process.

Note that there is a “mapping” table in the import routine ENIMPORT which maps row 1 names to VistA field names. These are initially the same (one to one), but the table is there for any future changes. Also, the columns in row \#1 can be in any order, it is the field name that is important.

VistA routine ENIMPORT

This was a new routine that was introduced in patch EN\*7.0\*105. It is invoked by the VistA option EN IMPORT NEW EQUIP INV. RECS

This is the logic in the routine:

1.  User is prompted for the type of run as follows:
    1.  (C)heck the file – all entries in the file are checked for validity and an error report is displayed on the screen for capture. NOTE that the data dictionary for file \#6914 is used by the utility routine to execute the correct validity check – NOT row 3 of the input file, which is informational only.
    2.  (I)mport the file – all entries are checked (as they were for (C) above) and, if there are no errors at all in the input file, all entries are imported into the file, and a log file is written containing all the Internal Entry Numbers (IENs) of the new records.
    3.  (R)ollback – The user selects a log file which is indicate by username, date, and time. All the new records that were created by the run creating the log file will be deleted from file \#6914.
2.  User is asked for the folder which contains the tab-delimited text input file.
3.  User is asked for the name of the tab-delimited text input file.
4.  If the Check option has been selected, the user is asked for the maximum number of records to be checked for validity. If the field is skipped, all records will be checked.
5.  During the update process, data is retrieved from each row in the spreadsheet, and an API in the existing routine - ENR^ENEQ - is called to create a “stub” record for the new entry. This code locks the file, gets the next record number, creates the stub record in the file, then unlocks the file. After this, action returns to the routine ENIMPORT, where all the fields in the row are entered into the record which was just created (with another lock/unlock).

Sample run showing errors in the input file.

Select OPTION NAME: EN IMPORT NEW EQUIP. INV. RECS

Select one of the following: ENIMPORT_EN_7_105_Unit_Test 760 error.txt'

C Check the input file for errors.

I Import the input file.

R Roll back an import.

Enter response: C// heck the input file for errors.

Enter PATH to file ex: c:\anyfolder\\ /srv/vista/patches/PUB/ (Example: please enter your connected folder)

Enter FILE NAME ex: New_Equip.txt: 2024_09_12_EQUIP_760.txt (Example: please enter your file name)

Loading tab-delimited file into VistA log file from /srv/vista/patches/PUB/ 2024_09_12_EQUIP_760.txt

Start LOGGING your screen now, and accept if you are ready to continue? YES//

Log file for this run is: ^XTMP("EN-IMPORT-20240125@095427",1) \[USER_NAME\]

: JAN 26, 2024@09:54:27 -- EN Equipment file \# 6914 - imported data

Err# 1 Row: 4 Col: "A" (MANUFACTURER) MISSING DATA - "ACME LABXXX" not found in

MANUFACTURER LIST FILE (#6912)

Err# 2 Row: 5 Col: "B" (SERIAL \#) DATA TOO LONG - \[67J184100156/12015XXXXXXXXXX

XXX\] is 31 chs long and exceeds the maximum length for INVENTORY INV. file (#691

4\) field SERIAL \# (#5) which is 30 chs

Err# 3 Row: 6 Col: "C" (MODEL) DATA TOO LONG - \[119261XXXXXXXXXXXXXXXXXXXXXXXXX

\] is 31 chs long and exceeds the maximum length for INVENTORY INV. file (#6914)

field MODEL (#4) which is 30 chs.

Err# 4 Row: 7 Col: "D" (CATEGORY STOCK NUMBER) MISSING DATA - "7025-438135XX" not found in CATEGORY STOCK NUMBER file (#6917)

Err# 5 Row: 8 Col: "F" (MFGR. EQUIPMENT NAME) DATA TOO LONG - \[CENTRIFUGEXXXXXX

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\] is 81 chs long.

and exceeds the maximum length for INVENTORY INV. file (#6914) field MFGR. EQU

IPMENT NAME (#3) which is 80 chs.

Err# 6 Row: 9 Col: "G" (CMR) MISSING DATA - "786XX" not found in CMR file (#691

4.1)

Err# 7 Row: 10 Col: "H" (EQUIPMENT CATEGORY) MISSING DATA - "CAVATRONXXXXXXXXXX

XXXXXXXXXXXXXXXXXXXXX" not found in EQUIPMENT CATEGORY file (#6911)

Err# 8 Row: 11 Col: "J" (PURCHASE ORDER \#) DATA TOO LONG - \[766-E20002XXXXX\] is.

15 chs long and exceeds the maximum length for INVENTORY INV. file (#6914) field.

PURCHASE ORDER \# (#11) which is 12 chs.

Err# 9 Row: 12 Col: "K" (ACQUISITION METHOD) MISSING SET - SET field \[ACQUISIT.

ION METHOD\] does not contain "PURCHASEDXX". File \#6914, ACQUISITION METHOD (#20.

1\)

CHECKFILE - Now on row \#13

Err# 10 Row: 13 Col: "M" (LEASE COST) VALIDATION FAILURE - 9999999999 maximum.

value of 9,999,999 exceeded.

Err# 11 Row: 14 Col: "N" (TOTAL ASSET VALUE) VALIDATION FAILURE - 9999999999

maximum value of 9,999,999 exceeded.

Err# 12 Row: 15 Col: "O" (ACQUISITION DATE) VALIDATION FAILURE - 9/25/2023XX is.

an invalid date

Err# 13 Row: 16 Col: "P" (WARRANTY EXP. DATE) VALIDATION FAILURE - 9/24/2024XX

is an invalid date.

Err# 14 Row: 17 Col: "R" (ACQUISITION SOURCE) DATA TOO LONG - \[BX\] is 2 chs long.

and exceeds the maximum length for POINTER to SOURCE CODE file (#420.8)

Err# 15 Row: 18 Col: "S" (TYPE OF ENTRY) MISSING SET - SET field \[TYPE OF ENTR

Y\] does not contain "NON-EXPENDABLE EQPTXX". File \#6914, TYPE OF ENTRY (#7)

Err# 16 Row: 19 Col: "T" (USE STATUS) MISSING SET - SET field \[USE STATUS\] doe.

s does not contain "IN USEXX". File \#6914, USE STATUS (#20)

Err# 17 Row: 20 Col: "U" (PARENT SYSTEM) VALIDATION FAILURE - 35000 Parent

record does not exist in file \#6914.

Err# 18 Row: 21 Col: "X" (LOCATION) MISSING DATA - "149-1-766AXXX" not found in

ENG SPACE file (#6928)

Err# 19 Row: 22 Col: "Y" (LOCAL IDENTIFIER) DATA TOO LONG - \[PAN1XXXXXXXXXXXXXX

X\] is 19 chs long and exceeds the maximum length for INVENTORY INV. file (#6914)

field LOCAL IDENTIFIER (#26) which is 15 chs.

CHECKFILE - Now on row \#23

Err# 20 Row: 23 Col: "Z" (STATION NUMBER) DATA TOO LONG - \[766XXX\] is 6 chs long.

and exceeds the maximum length for INVENTORY INV. file (#6914) field STATION N

UMBER (#60) which is 5 chs.

Err# 21 Row: 24 Col: "AA" (CONTROLLED ITEM?) MISSING SET - SET field \[CONTROLL

ED ITEM?\] does not contain "NOXX". File \#6914, CONTROLLED ITEM? (#33)

Err# 22 Row: 25 Col: "AB" (INVESTMENT CATEGORY) MISSING SET - SET field \[INVES

TMENT CATEGORY\] does not contain "NOT CAPITALIZED/ACCOUNTABLEXXXX". File \#6914,

INVESTMENT CATEGORY (#34)

Err# 23 Row: 26 Col: "AC" (FUND) DATA TOO LONG - \[AMAFMCXXX\] is 9 chs long and

exceeds the maximum length for POINTER to NX FUND file (#6914.6)

Err# 24 Row: 27 Col: "AD" (FUND CONTROL POINT) DATA TOO LONG - \[XXXXXXXXXXXXXXX

XXXXXXXXXXXXXXXXXXXX\] is 35 chs long and exceeds the maximum length for INVENTOR.

Y INV. file (#6914) field FUND CONTROL POINT (#35) which is 30 chs

Err# 25 Row: 28 Col: "AE" (BUDGET OBJECT CODE) DATA TOO LONG - \[3130XXX\] is 7 chs long and exceeds the maximum length for POINTER to NX BOC file (#6914.4)

Err# 26 Row: 29 Col: "AG" (ADMINSTRATIVE OFFICE) DATA TOO LONG - \[10XXX\] is 5 chs long and exceeds the maximum length for POINTER to NX A/O file (#6914.7)

Err# 27 Row: 30 Col: "AH" (EQUITY ACCOUNT) MISSING SET - SET field \[EQUITY ACC

OUNT\] does not contain "MEDICALXXX". File \#6914, EQUITY ACCOUNT (#64)

------------------------------------------------------------

Summary of error types:

1\. Data exceeds maximum length for field: 11

2\. Missing entries in POINTED-TO file: 5

3\. SET field does not contain field value: 6

4\. Validation Failed: 5

------------------------------------------------------------

\#ERROR RECORDS: 27

\#GOOD RECORDS: 0

Last record in the EQUIPMENT INV. file is: 33688.

End the LOGGING to your screen now then press Enter.

Sample run showing a valid input file, and an update to file \#6914.

Select OPTION NAME: EN IMPORT NEW EQUIP. INV.

Select one of the following:

C Check the input file for errors.

I Import the input file.

R Roll back an import.

Enter response: C// Import the input file.

Enter PATH to file ex: c:\anyfolder\\ /srv/vista/patches/PUB/ (Example: please enter your connected folder)

Enter FILE NAME ex: New_Equip.txt: 2024_09_12_EQUIP_760.txt (Example: please enter your file name)

Loading tab-delimited file into VistA log file from /srv/vista/patches/PUB/ 2024_09_12_EQUIP_760.txt

Start LOGGING your screen now, and accept if you are ready to continue? YES//

Log file for this run is: ^XTMP("EN-IMPORT-20240125@095427",1) \[USER_NAME\]

: JAN 26, 2024@09:54:27 -- EN Equipment file \# 6914 - imported data

\#ERROR RECORDS: 0

\#GOOD RECORDS: 1

Last record in the EQUIPMENT INV. file is: 33689.

1 record was added to the EQUIPMENT INV file (#6914)

End the LOGGING to your screen now then press Enter.

We can see that a new record was created in file \#6914: 33689

Display the record that was created in the EQUIPMENT INV. File

FileMan Inquiry:

Select OPTION: 5 INQUIRE TO FILE ENTRIES

Output from what File: EQUIPMENT INV.// (32486 entries)

Select EQUIPMENT INV. ENTRY NUMBER: 33689 67J184100156/12015 CAVATRON

IN USE PAN1

Another one:

Standard Captioned Output? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record Number

(IEN)

Display Audit Trail? No// NO

NUMBER: 33689 ENTRY NUMBER: 33689

MFGR. EQUIPMENT NAME: CENTRIFUGE TYPE OF ENTRY: NON-EXPENDABLE EQPT

ENTERED BY: NEEDHAM, MALCOLM K DATE ENTERED: JAN 26, 2024

EQUIPMENT CATEGORY: CAVATRON MODEL: 119261

SERIAL \#: 67J184100156/12015 MANUFACTURER: ACME LAB

MODEL(C): 119261 SERIAL \#(C): 67J18410015612015.

PURCHASE ORDER \#: 766-E20002 TOTAL ASSET VALUE: 99999

ACQUISITION DATE: SEP 25, 2023 WARRANTY EXP. DATE: SEP 24, 2024

LIFE EXPECTANCY: 4 CATEGORY STOCK NUMBER: 7025-438135

CMR: 786 REPLACEMENT DATE: SEP 25, 2027

LEASE COST: 99999 ACQUISITION SOURCE: B

USE STATUS: IN USE SERVICE POINTER: OI&T (R01N19CHY)

ACQUISITION METHOD: PURCHASED LOCATION: 149-1-766A.

LOCAL IDENTIFIER: PAN1

COMMENTS: TEST THE WORD PROCESSING FIELD

CONTROLLED ITEM?: NO

INVESTMENT CATEGORY: NOT CAPITALIZED/ACCOUNTABLE

FUND CONTROL POINT: NDCONTROLPOINT TEXT

STANDARD GENERAL LEDGER: 1750 STATION NUMBER: 766

BUDGET OBJECT CODE: 3130 FUND: AMAFMC

ADMINISTRATION/OFFICE: 10 EQUITY ACCOUNT: MEDICAL

REPORTED TO FAP (c): 0

Rolling back an update

If it is necessary to undo an update that is made by the utility to file \#6914, use the Rollback option.

Select OPTION NAME: EN IMPORT NEW EQUIP. INV.

Select one of the following:

C Check the input file for errors.

I Import the input file.

R Roll back an import.

Enter response: C// Roll back an import.

How many days back (0=Today only): (0-90): 0//

1\. \[USER_NAME\]: JAN 26, 2024@11:11:53 -- EN Equipment file \# 6914 - import

ed data

Is this the file you need? YES//

Start LOGGING your screen now, and accept if you are ready to continue? YES//

IEN 33689 CENTRIFUGE removed.

End the LOGGING to your screen now then press Enter

## Program Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Program Management option is entered from the Engineering Main Menu. The option is selected from the menu by entering the first few unique characters or the synonym "ENM".

This option is only available to the Engineering Applications Manager or Engineering Site Manager. It is where the various lists are established and maintained. The Engineering Employee file and the Equipment Device Type list must be maintained on a continuing basis for the system to be up to date.

AUTOMATED ENGINEERING MANAGEMENT SYSTEM

|      | VERSION 7.0                              |
|------|------------------------------------------|
| WO   | Work Order & MERS                        |
| PLAN | Project Planning                         |
| TRK  | Project Tracking                         |
| EQ   | Equipment Management                     |
| ENM  | Program Management                       |
| SP   | Space/Facility Management                |
| FSA  | 2162 Report of Accident                  |
| XFER | Assign (Transfer) Electronic Work Orders |

Select Engineering Main Menu Option: ENM Program Management ENGINEERING PROGRAM MANAGEMENT ROUTINE

> ---\>1 Engineering Computer Port

2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 1 Engineering Computer Port

### Engineering Computer Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to specify those ports that are suitable for hard-copy reports. The Computer Port file is a pointer to the Device file.

Select ENGINEERING COMPUTER PORT DEVICE \#: ?

ANSWER WITH ENGINEERING COMPUTER PORT DEVICE \# CHOOSE FROM:

1 CONSOLE

3 ENG PRINTER

64 M&R FOREMAN

71 OPERATIONS

YOU MAY ENTER A NEW ENGINEERING COMPUTER PORT, IF YOU WISH ANSWER WITH DEVICE NAME

DO YOU WANT THE ENTIRE 42-ENTRY DEVICE LIST? N (NO) Select ENGINEERING COMPUTER PORT DEVICE \#: 3

..OK? YES// Y (YES) ENG PRINTER

DEVICE \#: 3// DEVICE \# TRIGGERED: 3//

DEVICE DESCRIPTION: ENG PRINTER//

Select ENGINEERING COMPUTER PORT DEVICE \#:

### Section List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is where the Engineering Section List is developed and maintained. This system comes with a 32-entry Engineering Section list.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

> 1 Engineering Computer Port

> ---\>2 Section List

3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 2 Section List

Select ENGINEERING SECTION LIST: ?

ANSWER WITH ENGINEERING SECTION LIST SECTION NUMBER

20 SUPERVISORY(M&R) 21

22 AIR CONDITIONING ...............................23 REFR

24 ELEVATORS(M&R) ............................ ... 25 PLUM

26 MACHINE ........................... 27 SHEET M

28 WELDING ........................... 29 MOTOR V

30 CARPENTRY .......................... 31 MASONRY

32 LOCKSMITH .......................... 33 MAINTIN

34 STRUCT+FAC, OTHER ............................. 35 BIOM

36 PREV. MAINT. INSPECTION .......................... 90 HOLDING

YOU MAY ENTER A NEW ENGINEERING SECTION LIST, IF YOU WISH ANSWER MUST BE 3-21 CHARACTERS IN LENGTH

Select ENGINEERING SECTION LIST:

If an existing section number is entered, you can step through and edit ENGINEERING SECTION, ABBREVIATION, and DEVICE assigned to that section as shown below:

Select ENGINEERING SECTION LIST: 35 BIOMEDICAL ENGINEERING SECTION: BIOMEDICAL//

ABBREVIATION: B//

The device chosen will be used for automatic printing of new work orders, if automatic printing has been selected through the Software Options Enter/Edit.

DEVICE: 65//

Select ENGINEERING SECTION LIST: 21 ELECTRIC ENGINEERING SECTION: ELECTRIC//

ABBREVIATION: E// DEVICE: 64//

Select ENGINEERING SECTION LIST: 1 OFFICE OF THE CHIEF ENGINEERING SECTION: OFFICE OF THE CHIEF// ABBREVIATION: OC//

DEVICE: 67//

Select ENGINEERING SECTION LIST:

A new Engineering section could be added here or one of the existing sections could be deleted.

When no Engineering section needs to be added or edited, pressing \< RET\> at the "Select ENGINEERING SECTION LIST" prompt will return you to the Program Management option menu.

Important Note:

Engineering Section numbers 90 through 99 should be used ONLY for a receiving area for electronic work orders and other administrative requests.

### Work Center Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the editing, addition, and deletion of work center codes.

1.  Engineering Computer Port
2.  Section List

> ---\>3 Work Center Code

4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 3 Work Center Code

Select WORK CENTER CODE NAME: ?

ANSWER WITH WORK CENTER CODE NAME

DO YOU WANT THE ENTIRE 431-ENTRY WORK CENTER CODE LIST? YES

51105 ............................................... 51105/OTHER LEAVE

51106 ................................................ 51106/OTHER TIME

51108 51108/SUPERVISION

51109 51109/TRAINING

51200 ......................................... 51200/INCINERATOR PLANT '^' TO STOP: ^

YOU MAY ENTER A NEW WORK CENTER CODE, IF YOU WISH

ENTER THE WORK CENTER NUMBER (5 DIGITS), A SLASH, AND THE WORK CENTER NAME (E.G.,50102/SICK LEAVE).

ANSWER MUST BE 3-40 CHARACTERS

This example contains only a sampling of the work center codes.

When a work center code is entered, the following display, which may be edited, is shown:

Select WORK CENTER CODE NAME: 55555 55555/NEUROLOGY EQUIP, PREV MAINT NAME: 55555/NEUROLOGY EQUIP, PREV MAINT Replace

A work center code can be added or deleted as shown in the following examples:

Select WORK CENTER CODE NAME: 55655/ETC OTHER

ARE YOU ADDING A NEW WORK CENTER CODE (THE 432ND)? Y (YES) NAME: 55655/ETC OTHER

WORK CENTER CODE: 55655// NAME: 55655/ETC OTHER//

Select WORK CENTER CODE NAME: 55655 55655/ETC OTHER NAME: 55655/ETC OTHER// @

SURE YOU WANT TO DELETE THE ENTIRE '55655/ETC OTHER' WORK CENTER CODE?

Y (YES)

Select WORK CENTER CODE NAME:

Pressing \<RET\> instead of entering a work center code will return you to the Program Management option Menu.

### Engineering Employee File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Engineering Employee file will have to be generated locally by the Engineering Applications Manager. Many of the programs require the entering of an employee's name which will not be accepted unless it is in this file and is spelled in exactly the same manner. This file should contain a list of all employees who may be wholly or partially responsible for completing work requests. This option can be used to review and edit employee data as well as to add new employees.

On entering this option, \<?\> can be entered to get a list of all employees.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code

> ---\>4 Engineering Employee File

5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 4 Engineering Employee File

Select ENG EMPLOYEE NAME: ?

ANSWER WITH ENG EMPLOYEE NAME CHOOSE FROM:

ENUSER2, S IX

ENUSER2, SEVEN ENUSER2, E IGHT ENUSER2, NINE ENUSER3 , TEN ENUSER3 , ONE ENUSER3 , TWO ENUSER3 , THREE ENUSER3 , FOUR

YOU MAY ENTER A NEW ENG EMPLOYEE, IF YOU WISH

ANSWER MUST BE 3-30 CHARACTERS IN LENGTH AND CONTAIN A COMMA IE-. LAST NAME, FIRST NAME

It is very important that all employees to whom work may be assigned be entered in this file, not just those who use the computer directly. If you are not certain how an employee's name was entered, you can enter the first letter of the last name and then choose from the computer-generated listing. Great care should be taken to avoid duplicate entries in this file.

The following example shows the information on file for a specific employee.

Select ENG EMPLOYEE NAME: ENUSER2, SEVEN

NAME: ENUSER2, SEVEN// ORGANIZATIONAL TITLE: LABORER// SHOP: OFFICE OF THE CHIEF// HOME STREET ADDRESS: NO \#//

HOME CITY, STATE, ZIP: NO WHERESVILLE, PA// HOME PHONE:

GRADE/STEP: 9/5// WAGE: 10//

STATION: ANYCITY// ACTIVITY: 1//

ID#: 999//

COST CENTER: 150001/OFFICE OF THE CHIEF, ENGINEERING STATUS: PERM//

CLASSIFICATION SERIES: 456// POS. \#: 345// ??

ANSWER MUST BE 3-6 CHARACTERS IN LENGTH POS. \#: 345//

CLASSIFICATION TITLE: LABORER// HOSP. TELE. EXT.: 6101// Select ENG EMPLOYEE NAME:

A new employee can be entered by entering the last name first, a comma, and then the first name.

Select ENG EMPLOYEE NAME: ENUSER3, F IVE

ARE YOU ADDING 'ENUSER3, F IVE' AS A NEW ENG EMPLOYEE (THE 9TH)? Y (YES)

NAME: ENUSER3, F IVE//

ORGANIZATIONAL TITLE: ASST. CHIEF

SHOP comes from the ENGINEERING SECTION LIST.

SHOP: ?

ANSWER WITH ENGINEERING SECTION LIST SECTION NUMBER

DO YOU WANT THE ENTIRE 31-ENTRY ENGINEERING SECTION LIST, LIST? N (NO) SHOP: 1 OFFICE OF THE CHIEF

HOME STREET ADDRESS: 55129 N THIRD

HOME CITY, STATE, ZIP: N. LITTLE ROCK, AR 72115 HOME PHONE: 555-8000

The GRADE/STEP and the WAGE are requested next. The WAGE can be entered as dollars and cents. It does not have to be a whole number.

GRADE/STEP: 13/5 WAGE: 18.25 STATION: ?

ANSWER MUST BE 1-30 CHARACTERS IN LENGTH STATION:

ACTIVITY has to be a number between 1 and 99. The ID \# is limited to 3 digits. The COST CENTER to which the employee is assigned is also requested.

ACTIVITY: ?

TYPE A WHOLE NUMBER BETWEEN 1 AND 99 ACTIVITY: 1

ID#: ?

TYPE EMPLOYEE ID NUMBER USE 999 IF NONE ASSIGNED ID#: 561

COST CENTER: ?

ANSWER WITH COST CENTER NAME

DO YOU WANT THE ENTIRE COST CENTER LIST? N (N)

COST CENTER: 850100 850100 Office of the Chief Engineering Service

The STATUS of an employee can be chosen from the following three codes.

STATUS: ? CHOSE FROM:

T TEMP

P PERM

V VACATED

STATUS: P PERM

CLASSIFICATION SERIES: ?

ANSWER MUST BE 1-15 CHARACTERS IN LENGTH

CLASSIFICATION SERIES: 801 POS. \#: ?

ANSWER MUST BE 3-6 CHARACTERS IN LENGTH POS. \#: 8356

CLASSIFICATION TITLE:?

ANSWER MUST BE 3-30 CHARACTERS IN LENGTH CLASSIFICATION TITLE: ENGINEER, GENERAL HOSP. TELE. EXT.: 1151

Select ENG EMPLOYEE NAME:

When \<RET\> is entered instead of employee name, the computer will return to the Program Management option menu.

### Enter/Edit Equipment Category PM Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter or change the PM schedule for a specified device type (such as defibrillators, generators-electrical, etc.). A device type is formally defined as a discrete entry in the Equipment Category file. When a device type PM schedule is entered or changed, the user will be given the opportunity to apply the new schedule to all existing devices of the specified type.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File

> ---\>5 Enter/Edit Equipment Category PM Schedule

6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 5 Enter/Edit Equipment Category PM Schedule

This option is used to enter or change the PM schedule for a specified device type. A "device type" is formally defined as a discrete entry in the Equipment Category file, such as defibrillator, bar code reader, generator, etc.

Select EQUIPMENT CATEGORY NAME:? ANSWER WITH EQUIPMENT CATEGORY NAME

CHOOSE FROM:

DEFIBRILLATOR

DISPLAY CENTRAL STATION ELECTROCARDIOGRAPH

PUMP PERFUSION STAMP TIME-DATE

YOU MAY ENTER A NEW EQUIPMENT CATEGORY, IF YOU WISH

ANSWER MUST BE 1-50 CHARACTERS IN LENGTH AND CONTAIN NO COMMAS (,) Select EQUIPMENT CATEGORY NAME: DEFIBRILLATOR

A screen display of information concerning responsible technician, schedule, and cost is then displayed. All information may be edited at the prompts following the display.

Equipment Category: DEFIBRILLATOR

BIOMEDICAL SHOP

Tech: ENUSER, TWO

Starting Month: JAN Skip Mo Critical

Frequency (multiple):

ANNUAL 1.0 hrs \$300 (est) Level: 2 Proc: REPLACE BATTERIES

MONTHLY 0.5 hrs \$0 (est) Level: 1 Proc: PERFORMANCE Press \<RETURN\> to continue...

NAME: DEFIBRILLATOR//

Select SYNONYM: DEFIB//??

A multiple-valued field intended to allow for selection of Equipment Category in more than one way. For example: the category named ELECTROCARDIOGRAPH should have ECG and EKG as synonyms.

Select RESPONSIBLE SHOP: BIOMEDICAL// RESPONSIBLE SHOP: BIOMEDICAL//

TECHNICIAN: ENUSER3, S IX//??

The Engineering Service employee who normally does the PM work on this piece of equipment

for this shop.

STARTING MONTH: JAN//??

STARTING MONTH is used by the PM module as a criterion in determining when a PM is due. Let's consider the following example: an item subject to MONTHLY, QUARTERLY, and ANNUAL PM inspections. If STARTING MONTH were set to FEB; an ANNUAL inspection would be scheduled in FEB; QUARTERLY inspections in MAY, AUG, and NOV; and MONTHLY inspections in MAR, APR, JUN, JUL, SEP, OCT, DEC, and JAN.

If STARTING MONTH is left blank, JAN will be assumed. CHOOSE FROM:

1.  JAN
2.  FEB
3.  MAR
4.  APR

> 5 MAY

6.  JUN
7.  JUL
8.  AUG
9.  SEP
10. OCT
11. NOV
12. DEC

STARTING MONTH: JAN//

SKIP MONTHS:??

A range of months (inclusive) during which PMI's are to be suspended. For example, an entry of 'NOV-MAR' for an air-conditioner would suppress the scheduling of any PMIs in NOV, DEC, JAN, FEB, and MAR.

Some care needs to be taken when using this field. If you want an annual inspection, for instance, be sure that the STARTING MONTH is not within the range specified by the SKIP MONTHS; otherwise the ANNUAL PMI will never be scheduled.

Entries must take the form 'MMM-NNN', where MMM is a three-character abbreviation of the first month for which PMI's should be suspended and NNN is a three-character abbreviation of the last month for which PMI's should be suspended. Valid abbreviations are JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, and DEC.

SKIP MONTHS:

CRITICALITY: 10//??

An index of the importance of performing PMIs on this device. Enter an integer from 1 to

10, where 10 indicates that PMIs are extremely critical and 1 indicates that PMIs are

desirable but far from essential ................................................

(least critical).

When PM worklists are generated, the system will ask if all devices should be included or just those whose CRITICALITY is within a certain user specified range (say, 7 to 10). This is intended as a means of adjusting workload to match available resources.

Use of this feature is left entirely to the discretion of each site. If

a range of 1 through 10 seems like overkill, you may wish to restrict yourself to 5 through 10 instead. If all PMIs are deemed to be a high priority and adequate resources are available, there is probably no need to use this feature at all.

Devices with no entry for CRITICALITY will never be excluded from a PM worklist on the basis of a user specified CRITICALITY range which includes devices of CRITICALITY 10.

CRITICALITY: 10//

Select FREQUENCY: ANNUAL//??

Make a separate entry for each category (MONTHLY, QUARTERLY, etc.) of PMI that is to be scheduled for this device. The PM module looks at this field in conjunction with the STARTING MONTH when PM lists are generated.

Let's consider a fairly complex example: a device with SEMI-ANNUAL, QUARTERLY, and MONTHLY PMI's and a STARTING MONTH of MAR. Assuming no entry for SKIP MONTHS, the following PMI's will be scheduled:

SEMI-ANNUAL in MAR and SEP; QUARTERLY in JUN and DEC.

MONTHLY in APR, MAY, JUL, AUG, OCT, NOV, JAN, and FEB. CHOOSE FROM:

A ANNUAL

S SEMI-ANNUAL

Q QUARTERLY

M MONTHLY

BM BI-MONTHLY

W WEEKLY

BW BI-WEEKLY

N NONE

FREQUENCY: ANNUAL//

HOURS (Estimated): 1//??

Approximate amount of time required for this PMI (standard hours), to the nearest tenth of an hour. This value will be recorded in the EQUIPMENT HISTORY field when a PM is closed out unless another (more precise) value is explicitly entered.

MATERIAL COST (Estimated): 300//??

Estimated material cost for this PMI (standard cost). This cost will be charged to the piece of equipment whenever a PMI of this type is closed out unless another (more precise) value is entered at close-out time.

MATERIAL COST (Estimated): 150// LEVEL: 2//??

Each scheduled PMI may be composed of some combination of the following discrete levels of activity:

Level 1 - Visual inspection only.

Level 2 - Check and adjust operator controls; Level 3 - Electrical safety analysis.

Level 4 - Minor parts replacement; Level 5 - Major parts replacement; Level 6 - Complete overhaul.

LEVEL is an optional field and is intended to accommodate the needs of certain facilities with highly developed PM programs. Entries for LEVEL (if any) will appear on the PM worklist as a reminder to the responsible technician.

PROCEDURE: REPLACE BATTERIES//??

Enter the abbreviation (4 to 10 characters) of the PROCEDURE to be followed when performing this Preventive Maintenance Inspection. The full title (as well as the abbreviation) of the PM PROCEDURE will appear on the computer-generated worklist for reference.

If disk space permits, the actual step-by-step procedure may be entered in the TEXT field of the PM PROCEDURES file (Number 6914.2) and printed out on demand. In any event, the PMI procedure should be on file in some form and readily accessible to the technician performing the work.

CHOOSE FROM: BUFF FLOORS CALIBRATE CHANGE OIL CLEAN VACUUM POOL

PROCEDURE:

Select FREQUENCY:

When a device type PM schedule is entered or changed, the user will be given the opportunity to apply the new schedule to all existing devices of the specified type.

Are you finished with this Equipment Category? YES// (YES)

Do you wish to assign this PM schedule to ALL existing devices in the category of DEFIBRILLATOR? NO//?

'YES' will cause the system to immediately find every device of type DEFIBRILLATOR and assign each of them the PM schedule just entered.

The ID# of each affected device will be displayed at your terminal, but you will not be asked to confirm the transaction unless you have said that you want to.

Once this process has begun, it should not be interrupted.

Are you finished with this Equipment Category? YES// (YES)

Do you wish to assign this PM schedule to ALL existing devices in the category of DEFIBRILLATOR? NO// (NO)

### Manufacturer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option maintains the Manufacturer List file.

This file is maintained by the Engineering Service Center in cooperation with the ANYCITY ISC. Sites may add entries as necessary, using a ZZ namespace convention. Application managers should check carefully to ensure that any local entries are not duplications.

On entering this option, the computer will ask for a manufacturer which can be entered by name or common pseudonym. In the following example, HP has been entered for Hewlett-Packard.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule

> ---\>6 Manufacturer

7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 6 Manufacturer Select MANUFACTURER LIST FILE MFG/DIV:??

CHOOSE FROM:

1 ENMFGR1, NINE C it yv ill e

.

.

21 ENMFGR2, TEN Newark '^' TO STOP: ^

Select MANUFACTURER LIST FILE MFG/DIV: ENMFGR1, NINE

ENMFGR1, NINE C it yville

ENMFGR2, ONE Skokie CHOOSE 1-2: 1

MFG/DIV: ENMFGR1, NINE//

MFG'S FULL LENGTH NAME: ENMFGR1, NINE

Replace

DIVISION:

STREET: One Security Drive// CITY: C it yville//

STATE: KY// ZIP: 40356//

PHONE: (606) 885-9411//

Select PSEUDONYM: IBM/GENERAL SYS (ALSO SEE MFG \#1107)//??

1 IBM/GENERAL SYS (ALSO SEE MFG \#1107)

Select PSEUDONYM: IBM/GENERAL SYS (ALSO SEE MFG \#1107)

//

Information on the manufacturer including full name, division, address and phone number is accessed through this option. New manufacturers for a local list can be added, but they must start with ZZ, and contain no dashes.

Pressing \<RET\> will return to the Program Management option menu.

### Eng Site Parameters Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to edit the site parameters for employee costs, 2237 form used,

and other information. Certain entries in this file are mandatory if a site intends to transmit 10-0051s (Construction Project Tracking Reports) electronically and/or allow computerized entry of work requests by non-Engineering personnel.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer

> ---\>7 ENG SITE PARAMETERS Enter/Edit

8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 7 Engineering Site Parameters Enter/Edit

Select ENG INIT PARAMETERS STATION NAME:? ANSWER WITH ENG INIT PARAMETERS STATION NAME:

ANYCITY, DC

Select ENG INIT PARAMETERS STATION NAME: ANYCITY, DC STATION NUMBER: 999//

TYPE OF 2237 FORM:

PM HOURLY LABOR COST: ??

Default value. If a device has an entry for estimated PM hours AND an entry for responsible tech, the labor cost will be taken from the Engineering Employee File (No. 6929). If there is an entry for estimated hours but

NO entry for responsible tech, then this hourly figure will be used to compute total labor cost.

PM HOURLY LABOR COST:

DELETE PM WORK ORDERS?:??

Setting this field to 'YES' will cause PM work orders to be deleted from the system at close out time. Deletion of PM work orders is strongly recommended for sites that are short on disk space. The PMI will be posted to the equipment history (File 6914) before the actual work order is deleted.

CHOOSE FROM:

Y YES

N NO

DELETE PM WORK ORDERS?:

TEMPORARY WORK ORDER SECTION: RECEIVING//??

Intended for use at sites that allow direct entry of Engineering work orders by end-users. Since assignment of work requests to specific shops is an Engineering responsibility; 'electronic work orders' are initially directed to a 'fictitious shop' (or receiving area). Engineering should clean out a receiving area at least once a day. Electronic work orders may be transferred to working shops or disapproved.

The system will keep a permanent record of the number originally assigned to each work order. This number may always be used to look up the request, no matter how many times it's transferred. Initial requesters may edit their requests; but not after Engineering has transferred them. 'Fictitious' shops should have numbers in the range of 90 to 99, inclusive. Multi-division sites may have more than one receiving area.

If there is more than one receiving area AND if this field (TEMPORARY WORK ORDER SECTION) is left blank; end-users will be asked to specify the appropriate receiving area when they enter a work order.

REGION: 2//

EQPT CAT ON BAR CODE LABEL?:??

Should be set to 'YES' if you want to print the EQUIPMENT CATEGORY at the top of your bar-coded EQUIPMENT LABELs (instead of the words 'EQUIPMENT LABEL'. Due to space limitations on label stock, only the

first twenty (20) characters of the EQUIPMENT CATEGORY will be printable.

CHOOSE FROM:

1 YES

0 NO

EQPT CAT ON BAR CODE LABEL?:

Select EQPT LABEL PRINT FIELD:??

Enter the FIELD NUMBER (from the Equipment File) of a field that you want to have printed (in human readable format) on your bar-coded EQUIPMENT LABELs. Please do not enter more than two (2) such fields. If more than two fields are specified, the system will accept the first two and ignore all others.

MULTIPLE fields, WORD PROCESSING fields, and COMPUTED fields should not be selected for inclusion on bar coded EQUIPMENT LABELs.

ANSWER WITH EQPT LABEL PRINT FIELD

YOU MAY ENTER A NEW EQPT LABEL PRINT FIELD, IF YOU WISH

Type a Number between 1 and 9999999999, 4 Decimal Digits Select EQPT LABEL PRINT FIELD:

Select COMP LIST PRINT FIELD: ??

Enter the FIELD NUMBER (from the Equipment File) of a field that you want to have printed on the 'Companion Listings' that are produced along with bar coded EQUIPMENT LABELs. Please do not enter more than two such fields.

Fields selected for inclusion (in human readable format) on bar code labels are NOT automatically printed on Companion Listings.

MULTIPLE fields, WORD PROCESSING fields, and COMPUTED fields cannot be printed on Companion Lists.

SPACE FUNCT ON LOCATION LABEL?:??

If set to 'YES' and if a SPACE FUNCTION exists for the subject location, then the first 20 characters of the SPACE FUNCTION will be printed at the top of your bar-coded LOCATION LABELS. CHOOSE FROM:

1.  NO
2.  YES

SPACE FUNCT ON LOCATION LABEL?:

Select ENG INIT PARAMETERS STATION NAME:

Pressing \<RET\> will return to the Program Management option menu.

### Software Options Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit

> ---\>8 SOFTWARE OPTIONS Enter/Edit

9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey 11 Work Action

Select Program Management Option: 8 Software Options Enter/Edit

The Software Options Enter/Edit allows site-specific control of the following AEMS/MERS features:

Auto Print New W.O.

Equipment Replacement Template Expanded PM Work Orders Inventory Template

PM Device Type Identifier PM Sort

Print Bar Codes on W.O. Safety Printout

Space Survey Printout Warranty Expiration Template

Each feature has an explanation of its function, and the special settings for implementing the feature. The lines of the explanatory text may be edited at the site. All of the features are optional.

Each feature will be presented in this section.

Select ENG SOFTWARE OPTIONS FEATURE NAME:? ANSWER WITH ENG SOFTWARE OPTIONS FEATURE NAME CHOOSE FROM:

AUTO PRINT NEW W.O.

EQUIPMENT REPLACEMENT TEMPLATE EXPANDED PM WORK FORDER INVENTORY TEMPLATE

PM DEVICE TYPE IDENTIFIER PM SORT

PRINT BAR CODES ON W.O. SAFETY PRINTOUT

SPACE SURVEY PRINTOUT WARRANTY EXPIRATION TEMPLATE

Select ENG SOFTWARE OPTIONS FEATURE NAME: AUTO PRINT NEW W.O. CHOICES:

'S' WILL PRINT A SHORT SUMMARY WORK ORDER EACH TIME A NEW ONE IS ENTERED 'L' WILL PRINT A LONG W.O. EACH TIME ONE IS ENTERED

'N' WILL SUSPEND THE PRINTING OF NEWLY ENTERED WORK ORDERS. SELECTION:

Select ENG SOFTWARE OPTIONS FEATURE NAME: EXPANDED PM WORK ORDERS

'Y' will cause all the equipment related fields in PM work orders to be filled in using data from the Equipment File.

If this option is not set to 'Y', the system will produce skeleton PM work orders in order to conserve disk space. Note that information from the Equipment File is always printed on the PM worklists.

SELECTION:

Select ENG SOFTWARE OPTIONS FEATURE NAME: EQUIPMENT REPLACEMENT TEMPLATE

CHOICES:

One standard output of the AEMS/MERS Equipment Management Module is a listing of all non-expendable equipment due for replacement within a user specified date range. The fields to be printed on this list are defined by output template 'ENEQ REPLACEMENT'.

If you so desire, you can specify that a different set of fields be printed at your facility. To do this, simply set this software option to 'L' and create print template 'ENZEQ REPLACEMENT'.

Choices are 'L' for local, or

'S' for standard (default).

SELECTION: S//

Select ENG SOFTWARE OPTIONS FEATURE NAME: INVENTORY TEMPLATE

CHOICES:

One standard output of the VISTA Equipment Management Module is a listing of all non-expendable equipment sorted by CMR, EQUIPMENT CATEGORY, LOCATION, OWNING SERVICE, RESPONSIBLE SHOP, or USE STATUS. The standard print for these reports is defined by output template 'ENEQ EQUIP. LIST'. If you so desire, you can use a different output template at your facility. To do this, just enter an 'L' for this software option and be sure to call your local template 'ENZEQ EQUIP. LIST'.

Choices are 'L' for local, or

'S' for standard (default).

SELECTION: S//

Select ENG SOFTWARE OPTIONS FEATURE NAME: PM DEVICE TYPE IDENTIFIER

CHOICES:

'E' will stand for EQUIPMENT CATEGORY 'M' will stand for MFG. EQUIPMENT NAME

This option determines what is printed on PMI worklists under the heading of 'Equip Category'. EQUIPMENT CATEGORY will be printed unless 'M' is explicitly entered as the option of choice.

SELECTION: E//

Select ENG SOFTWARE OPTIONS FEATURE NAME: PM SORT

PM worklists are automatically sorted by responsible shop, and by technician within shop. Within tech, a site may choose to have worklists sorted by PM \#; Local Identifier; Location; Equipment Category or Owning Service. Choices are, therefore:

'P' for PM \#

'I' for Local Identifier 'L' for Location

'C' for Equipment Category 'S' for Owning Service.

If no choice is made via this file, the user will be asked for a 'Sort By' parameter each time a worklist is requested. Note that all data for the worklists come from the Equipment File.

SELECTION:

Select ENG SOFTWARE OPTIONS FEATURE NAME: PRINT BAR CODES ON W.O. CHOICES:

'Y' will cause bar code to be printed at the bottom of hard-copy work orders, provided the printer is capable of printing bar code. 'N' will cause work orders to be printed without bar code.

SELECTION: N//

Select ENG SOFTWARE OPTIONS FEATURE NAME: SAFETY PRINTOUT

CHOICES:

'L' FOR LOCAL TEMPLATE (TEMPLATE NAME MUST BE 'ENZFSA1') 'S' FOR STANDARD TEMPLATE

SELECTION: S//

Select ENG SOFTWARE OPTIONS FEATURE NAME: SPACE SURVEY PRINTOUT

CHOICES:

'L' for local template (template name must be 'ENZSPRM'). 'S' for standard template ('ENSPRM').

SELECTION: S//

Select ENG SOFTWARE OPTIONS FEATURE NAME: WARRANTY EXPIRATION TEMPLATE

CHOICES:

One standard output of the AEMS/MERS Equipment Management Module is a list of equipment whose warranty expires within a user.

specified date range. The standard output for this report is defined by print template 'ENEQ WARRANTY'.

If you so desire, you may create a different template for use at your facility. To make this work, you should enter an 'L' for this option and create a print template named 'ENZEQ WARRANTY'.

Choices are 'L' for local template, or

'S' for standard template (default).

### Engineering Archive Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Engineering Archive module presently services the Work Order and 2162 Accident Report files. It allows individual records to be stored on tape and then purged from the disk.

Pointers to external files are replaced by the equivalent text before records are saved to tape.

Data definitions are stored on the same tapes as the records themselves. The recall option uses these data definitions to automatically construct a temporary file for the storage and display of archived records. VA FileMan may be used to print information from these temporary files. There is no provision for restoring archived records back into the production file from which they were extracted.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit

> ---\>9 Engineering Archive Module

10. Biomedical Engineering Resource Survey
11. Work Action

#### Select Program Management Option: 9 Engineering Archive Module.

1.  Find & Assemble Records

Searches the database and finds the individual records to be archived, after which it moves them to an archive global and simultaneously purges.

them from the production file. The user is asked for record type, station number, and sort parameters. Records may be archived for an entire fiscal year, or a specific quarter. Completed work orders may be archived by shop (all shops, one shop, or all shops but one).

Since this function actually purges data from disk, you may wish to back up your system before executing "Find and Assemble Records".

2.  Archive & Verify Records.

Moves a collection of records (archive set) from the archive global to tape.

This function should be executed immediately after "Find and Assemble Records".

3.  Delete Archive Global

Kills the archive global, which may be thought of as a temporary storage area. The archive global holds records in the process of being archived, as well as records which have been recalled from an archive tape for inspection via VA FileMan. "Delete Archive Global" should be executed after "Archive and Verify" and after "Recall Archive Global" (once the recalled records have been inspected and/or printed).

4.  Recall Archive Global.

Restores records from an archive tape into the archive global, where they may be examined via FileMan. The user may recall an entire tape or search a tape for a specific record.

5.  Review Activity Log

Displays a chronological listing of everything that has been done with a given archive set.

#### Find & Assemble Records

Select Engineering Archive Module Option: 1 Find & Assemble Records ARCHIVAL FILE TYPES:

7.0T3

AVAILABLE FILES:

1.  WORK ORDERS
2.  2162 ACCIDENT REPORTS Select AVAILABLE FILE: 1 WORK ORDERS Station Number: 590

Is this correct? YES// (YES)

Do you wish to archive by fiscal YEAR or QUARTER (Y or Q) Y// SELECT FISCAL YEAR: 93 //88?

Include all shops? YES// (YES)

- You have requested to locate all completed work orders for all shops, in Fiscal Year 88
- IS IT O.K. TO PROCEED? NO// Y (YES) Now searching data base.

Hold on, this could take a while Elapsed time: 0.15 minutes.

3 Records were found meeting the archive criteria.

Is it O.K. to accept these data? YES// (YES)

The identification reference, 590.2930426.1253

has been entered into the Engineering Archive File.

Would you care to add your own local description and location for this archival episode? YES// (YES)

Engineering Archive Log Screen 04/23/93

1 ARCHIVE I.D.(R):590.2930426.1253

2 RECORDS TYPE(R): ENG. WORK ORDERS 3 FILE TYPE VERSION(R):1

4 DATA START DATE (R): OCT 1987 5 DATA ENDING DATE(R): SEP 30,1988

6 NO. RECORDS SAVED(R):3 7 PHYS. LOCATION: CABINET \#2

8.  OPT. SEARCH PARAMS. (R): NONE
9.  TAPE DESCRIPTION: WORK ORDERS - 1988

Please confirm, is this the expected archive record? YES// Transferring data dictionary.

Now extracting data from your files, this could take a while....

Elapsed time: 0.03 minutes.

- Records gathering complete.

\<cr\> to continue.

#### Archive & Verify Records.

Select Engineering Archive Module Option: 2 Archive & Verify Records ARCHIVAL FILE TYPES:

7.0T3

AVAILABLE FILES:

1.  WORK ORDERS
2.  2162 ACCIDENT REPORTS Select AVAILABLE FILE: 1 WORK ORDERS

Engineering Archive Log Screen 04/23/93

| 1 ARCHIVE I.D.(R):590.2930426.1253     |                                    |
|----------------------------------------|------------------------------------|
| 2 RECORDS TYPE(R): ENG. WORK ORDERS    | 3 FILE TYPE VERSION(R):1           |
| 4 DATA START DATE (R): OCT 1987        | 5 DATA ENDING DATE(R): SEP 30,1988 |
| 6 NO. RECORDS SAVED(R):3               | 7 PHYS. LOCATION: CABINET \#2      |
| 8 OPT. SEARCH PARAMS. (R): NONE        |                                    |
| 9 TAPE DESCRIPTION: WORK ORDERS - 1988 |                                    |

Please confirm, is this the expected archive record? YES//

- Please load WRITE ENABLED tape and bring on-line now Press \<RETURN\> to continue.

DEVICE: MT TAPE DRIVE ADDRESS/PARAMETERS: (FORMAT="VAL4”: BLOCKSIZE=1024)// R EWIND? NO// Y

(YES)

Beginning output......................

Elapsed time: 0.22 minutes.

Archive complete, care to verify? YES// (YES)

ARCHIVAL DEVICE: HOME// TAPE COMPUTER ROOM ADDRESS/PARAMETERS: ("CVAL4"::2048) REWIND? NO// Y (YES)

Do you prefer a record-for-record verify? NO// Y (YES) Header OK

..Beginning full verify Elapsed time: 0.05 minutes.

Please label your tape clearly for future reference

verify completed.

\<cr\> to continue.

#### Delete Archive Global

Select Engineering Archive Module Option: 3 Delete Archive Global ARCHIVAL FILE TYPES:

7.0T3

AVAILABLE FILES:

1.  WORK ORDERS
2.  2162 ACCIDENT REPORTS Select AVAILABLE FILE: 1 WORK ORDERS

Engineering Archive Log Screen 04/23/93

1 ARCHIVE I.D.(R):590.2930426.1253

2.  RECORDS TYPE(R): ENG. WORK ORDERS
3.  FILE TYPE VERSION(R):1
4.  DATA START DATE (R): OCT 1987
5.  DATA ENDING DATE(R): SEP 30,1988
6.  NO. RECORDS SAVED(R):3
7.  PHYS. LOCATION: CABINET \#2
8.  OPT. SEARCH PARAMS. (R): NONE
9.  TAPE DESCRIPTION: WORK ORDERS - 1988

Tape written on: APR 23, 1993@12:56

with header: WO ARCHIVE, ID# "590.2930426.1253", 3 RECORDS SAVED

Please confirm, is this the expected archive record? YES// OK to delete this global? NO// Y (YES)

Archive global deleted.

\<cr\> to continue.

#### Recall Archive Global.

Select Engineering Archive Module Option: 4 Recall Archive Global ARCHIVAL FILE TYPES:

7.0T3

AVAILABLE FILES:

1.  WORK ORDERS
2.  2162 ACCIDENT REPORTS Select AVAILABLE FILE: 1 WORK ORDERS

Please load ARCHIVE Tape and bring on-line now Press \<RETURN\> to continue.

ARCHIVAL DEVICE: HOME// TAPE COMPUTER ROOM ADDRESS/PARAMETERS: ("CVAL4"::2048) REWIND? NO// Y (YES)

Engineering Archive Log Screen 04/23/93 1 ARCHIVE I.D.(R):590.2930426.1253

2.  RECORDS TYPE(R): ENG. WORK ORDERS
3.  FILE TYPE VERSION(R):1
4.  DATA START DATE (R): OCT 1987
5.  DATA ENDING DATE(R): SEP 30,1988
6.  NO. RECORDS SAVED(R):3
7.  PHYS. LOCATION: CABINET \#2
8.  OPT. SEARCH PARAMS. (R): NONE
9.  TAPE DESCRIPTION: WORK ORDERS - 1988

Tape written on: APR 23, 1993@12:56

with header: WO ARCHIVE, ID# "590.2930426.1253", 3 RECORDS SAVED

Is this the tape you want? YES//

Recall all records? YES// (YES) Now fetching global...

I'll print a dot for each 10 nodes, so you'll know I'm not asleep.

ARCHIVAL DEVICE: HOME// TAPE COMPUTER ROOM ADDRESS/PARAMETERS: ("CVAL4"::2048) REWIND? NO// Y (YES)

......................

The global is now on the system disk Elapsed time: 0.13 minutes Initializing archive file...

Initializing data dictionary for this tape. Routine ENARX101 filed.

Routine ENARX102 filed.

Routine ENARX11 filed.

Routine ENARX12 filed.

Routine ENARX13 filed.

Routine ENARX14 filed.

Routine INIT filed.

Routine INIT1 filed. Routine INIT2 filed. Routine INIT3 filed.

THIS VERSION OF 'ENARX11' WAS CREATED ON JAN 25, 1111

(AT AEMS Development BY VA FileMan V.17.32)

TO SET UP FOR YOU THE FOLLOWING FILE:

6919.1 WO ARCHIVE

NOTE --YOU ALREADY FHAVE 'WO ARCHIVE' FILE

SHALL I WRITE OVER EXISTING DATA DEFINITIONS? NO// Y (YES) SHALL I WRITE OVER FILE SECURITY CODES? NO// (N0)

ARE YOU SURE EVERYTHING'S OK? Y (YES)

...SORRY, HOLD ON.....

OK, I'M DONE.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

O.K. Archive film is ready.

#### Review Activity Log

Select Engineering Archive Module Option: 5 Review Activity Log Select ENG ARCHIVE LOG ARCHIVE I.D.: 590.2930426.1253

Select output device: HOME.

ARCHIVE Log for:590.2930426.1253

RECORDS TYPE: ENG. WORK ORDERS FILE VERSION(R):1 START DATE: OCT 1987 STOP DATE: SEP 30,1988 OPT. PARAMETERS.: NONE.

RECORDS SAVED:3 PHYSICAL LOCATION: TAPE CABINET \#2 TAPE DESCRIPTION: WORK ORDERS - 1988

\-

ACTIVITY DATE ACTIVITY TYPE REQUESTOR

| \-                           |       |                  |                |
|------------------------------|-------|------------------|----------------|
| APR 26,1993                  | 12:53 | Assemble records | ENUSER3, SEVEN |
| APR 26,1993                  | 12:55 | Purge live data  | ENUSER3, SEVEN |
| APR 26,1993                  | 12:56 | Archive global   | ENUSER3, SEVEN |
| APR 26,1993                  | 12:58 | Verify global    | ENUSER3, SEVEN |
| APR 26,1993                  | 12:59 | Delete global    | ENUSER3, SEVEN |
| APR 26,1993                  | 13:01 | Recall archive   | ENUSER3, SEVEN |
| Press \<RETURN\> to continue |       |                  |                |

### Biomedical Engineering Resource Survey

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This module collects data on how individual facilities maintain their biomedical equipment and instrumentation. Data from all sites is aggregated once a year by the Engineering Service Center in St. Louis.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module

> ---\>10 Biomedical Engineering Resource Survey

11. Work Action

Select Program Management Option: 10 Biomedical Engineering Resource Survey

1.  Entering Data into the BERS Survey File
2.  Print Personnel Survey Listing
3.  Print Contract Survey Listing
4.  Print General Survey Listing
5.  Print Additional Survey Listing

#### Entering Data into the BERS Survey File

Select Biomedical Engineering Resource Survey Option: 1 Entering Data into the BERS Survey File

Enter Survey Year and Hospital Number: ??

93999

VAMC: 93999//?

Enter last two digit of year concatenated with three-digit hospital code: i.e., 87657:

Ex: 87668 for Year 87 Station 668. VAMC: 93999//

HOSPCODE: 999//?

Enter hospital code i.e., 657 for St. Louis HOSPCODE: 999//

VAMC ADDRESS: 123 HERE//?

Enter City, State, & Zip, i.e., St. Louis, MO 63125 VAMC ADDRESS: 123 HERE//

FYEARRPT: 93//?

Enter last two digits of Survey year, i.e., for 1986 enter only 86.

FYEARRPT: 93//

Select I.A.1. NAME: ENUSER2, SEVEN//? ANSWER WITH I.A.1. NAME

CHOOSE FROM:

1 ENUSER2, SEVEN

YOU MAY ENTER A NEW I.A.1. NAME, IF YOU WISH

Enter Person's LastName, FirstName Select I.A.1. NAME: ENUSER2, SEVEN//

I.A.1. NAME: ENUSER2, SEVEN//

2\. ABBREVIATED CLASS TITLE:?

Enter Abbreviated title i.e., BE or BMET or MER or ET

2.  ABBREVIATED CLASS TITLE:

2a. TYPE OF CLASSIFICATION: BIOMEDICAL ENGINEER

// ?

Choose one of the above!!! CHOOSE FROM:

T TECHNICIAN

B BIOMEDICAL ENGINEER

O OTHER CLERICAL SUPPORT

2a. TYPE OF CLASSIFICATION: BIOMEDICAL ENGINEER

// B BIOMEDICAL ENGINEER

3.  ORGANIZATIONAL TITLE:?

Enter Position Title. Ex:: Supervisory Technician or Staff Engineer

3.  ORGANIZATIONAL TITLE:
4.  PAYPLAN/CLASS:?

Enter Pay plan. Ex: WG-4305 or GS-607 etc.

4.  PAYPLAN/CLASS:

4a. GRADE/STEP:?

Example 9/3 or 11/2 or 12/5 4a. GRADE/STEP:

5.  EMPLOYEE STATUS:? CHOOSE FROM:

F FULL-TIME

PT PART-TIME

PY PART-YEAR

S SHARED

5.  EMPLOYEE STATUS: F FULL-TIME 5a. No. OF MONTHS WORKED: 8// 5b. SHARED BY:?

ENTER ALL SERVICES BY NAME & PERCENT i.e. RESEARCH 20% 5b. SHARED BY:

6.  ANNUAL SALARY:?

Enter employee's annual salary.

6.  ANNUAL SALARY:

Select 7a. GENERAL EXPERTISE:? ANSWER WITH 7a. GENERAL EXPERTISE

YOU MAY ENTER A NEW 7a. GENERAL EXPERTISE, IF YOU WISH

Enter General Area of Expertise (limit of 4); REF CIRCULAR 10-84-206 PARA 7(a)

Select 7a. GENERAL EXPERTISE:

Select 7b. MFG NAME:?

ANSWER WITH 7b. MFG/EQUIP TYPE/MOD#

YOU MAY ENTER A NEW 7b. MFG/EQUIP TYPE/MOD#, IF YOU WISH ENTER MANUFACTURER'S NAME!!!

ANSWER WITH MANUFACTURER LIST FILE MFGID, OR PSEUDONYM

DO YOU WANT THE ENTIRE 4584-ENTRY MANUFACTURER LIST FILE LIST? N (NO)

Select 7b. MFG NAME: EO

1.  HP/ANALYTICAL ENMFGR2, TWO Avondale
2.  HP/CALCULATOR ENMFGR2, THREE Fort Collins
3.  HP/MEDICAL PROD ENMFGR, TWO Waltham CHOOSE 1-3: 2 ENMFGR2, THREE

EQUIPMENT TYPE:?

Enter Generic Name of Equipment, EQUIPMENT TYPE: COMPUTER

MODEL:?

If more than one model use, as separator MODEL:

Select 7b. MFG NAME:?

ANSWER WITH 7b. MFG/EQUIP TYPE/MOD#:

1 ENMFGR2, THREE

YOU MAY ENTER A NEW 7b. MFG/EQUIP TYPE/MOD#, IF YOU WISH ENTER MANUFACTURER'S NAME!!!

ANSWER WITH MANUFACTURER LIST FILE MFGID, OR PSEUDONYM

DO YOU WANT THE ENTIRE 4584-ENTRY MANUFACTURER LIST FILE LIST? N (NO)

Select 7b. MFG NAME:

Select I.A.1. NAME:

II.A. WORK AREA (SQFT):?

Enter Work Area Space in Square Feet.

1.  WORK AREA (SQFT):
2.  STORAGE AREA (SQFT):?

Enter the storage space in square feet.

II.B. STORAGE AREA (SQFT):

II.C. BME OFFICE (SQFT):?

Enter BME Office space in square feet.

II.C. BME OFFICE (SQFT):

III.A. TOTAL ACQUISITION COST:?

Enter Total Test Equipment Acquisition cost.

III.A. TOTAL ACQUISITION COST:

IV.A. COST OF PARTS:?

Enter Cost of parts used for inhouse repairs & added to stock during the reporting period.

IV.A. COST OF PARTS:

V.A. COST OF REPAIRS (NON):?

ENTER COSTS OF PARTS & LABOR FOR VENDOR REPAIRS (NON-CONTRACT)

V.A. COST OF REPAIRS (NON):

IV.B. COST OF X-RAY PART N/T:?

ENTER COST OF X-RAY PARTS ALONE (NO TUBES)

IV.B. COST OF X-RAY PART N/T:

IV.C. COST OF X-RAY (TUBES):?

ENTER COSTS OF X-RAY TUBES ONLY (NOT TO INCLUDE ANY PROVIDED BY CONTRACTS OR ONE-TIME SERVICE COSTS)

IV.C. COST OF X-RAY (TUBES):

V.B. COST OF X-RAY CALLS:?

ENTER COSTS OF X-RAY CALLS IN LIEU OF CONTRACT SERVICE.

V.B. COST OF X-RAY CALLS:

Select VI.A. CONTRACT SERVICE: LAB//?

ANSWER WITH VI.A. CONTRACT SERVICE CONTRACT NUMBER CHOOSE FROM:

1.  OTHER
2.  LAB

YOU MAY ENTER A NEW VI.A. CONTRACT SERVICE, IF YOU WISH

Enter "L" or "R" or "N" to enter new contracts: CHOOSE FROM:

L LAB

R RAD

14. NUC
15. OTHER

Select VI.A. CONTRACT SERVICE: LAB// L (LAB)

VI.A. CONTRACT SERVICE: LAB// COMPANY NAME:?

Enter Company Name providing service (NO DEPOTS) COMPANY NAME:

MANUFACTURER NAME: ENMFGR2, TWO//?

Enter Manufacturer's Name:

ANSWER WITH MANUFACTURER LIST FILE MFGID, OR PSEUDONYM

DO YOU WANT THE ENTIRE 4584-ENTRY MANUFACTURER LIST FILE LIST? N (NO) MANUFACTURER NAME: ENMFGR2, TWO//

TYPE OF EQUIPMENT:?

Enter type of equipment name, i.e., Auto microbic System TYPE OF EQUIPMENT:

MODEL \#:?

Enter model numbers separated by commas, i.e., S+,33, MD MODEL \#:

EQUIPMENT COST (ACQST):?

Enter Equipment Cost (Acquisition): EQUIPMENT COST (ACQST):

CONTRACT COST:?

Enter Contract Cost (Actual Expense): CONTRACT COST:

CONTRACT PERIOD:?

Enter Contract Period (# Months 1-12): CONTRACT PERIOD:

CONTRACT TYPE: FULL SERVICE//?

Select from displayed list ONLY CHOOSE FROM:

F FULL SERVICE

PM PREVENTIVE MAINTENANCE ONLY S SAFETY INSPECTION

SP SERVICE PLUS PARTS

P PARTIAL SERVICE

PO PARTS ONLY CONTRACT TYPE: FULL SERVICE// ADDITIONAL COST:?

ENTER ADDITIONAL COSTS FOR PARTS & SERVICES PROVIDED BY VENDOR (IN ADDITION TO CONTRACT COSTS).

ADDITIONAL COST:

Select VI.A. CONTRACT SERVICE:?

ANSWER WITH VI.A. CONTRACT SERVICE CONTRACT NUMBER CHOOSE FROM:

1.  OTHER
2.  LAB

YOU MAY ENTER A NEW VI.A. CONTRACT SERVICE, IF YOU WISH

Enter "L" or "R" or "N" to enter new contracts: CHOOSE FROM:

L LAB

R RAD

14. NUC
15. OTHER

Select VI.A. CONTRACT SERVICE:

Select VII. ADDITIONAL SUPPORT AREAS: RESEARCH//? ANSWER WITH VII. ADDITIONAL SUPPORT AREAS:

1 RESEARCH

YOU MAY ENTER A NEW VII. ADDITIONAL SUPPORT AREAS, IF YOU WISH CHOOSE FROM:

1.  RESEARCH
2.  COMMUNICATION
3.  OFFICE EQUIPMENT
4.  ENTERTAINMENT
5.  EDUCATIONAL EQUIPMENT
6.  ADP EQUIPMENT
7.  OTHER

Select VII. ADDITIONAL SUPPORT AREAS: RESEARCH//

VII\. ADDITIONAL SUPPORT AREAS: RESEARCH//? • • TYPE OF EQUIPMENT:?

ENTER TYPE OF EQUIPMENT. (MUST BE 1-45 CHARACTERS): TYPE OF EQUIPMENT:

FTEE REQUIRED:?

Enter number of FTEE required FTEE REQUIRED:

ESTIMATED ACQ VAL OF INV SRVCD:?

ENTER Estimated Acquisition value of inventory serviced: ESTIMATED ACQ VAL OF INV SRVCD:

NUMBER OF UNITS INVOLVED:?

Enter number of units in support area NUMBER OF UNITS INVOLVED:

PARTS COST:?

Enter Dollar value of Parts Cost PARTS COST:

PARTS COST INC ELSEWHERE:?

If parts cost is included elsewhere in report, give brief description of location, i.e., under lab contracts etc.

PARTS COST INC ELSEWHERE:

COMMENTS:

1\>? • •

Select VII. ADDITIONAL SUPPORT AREAS:

Enter Survey Year and Hospital Number:

#### Print Personnel Survey Listing

Select Biomedical Engineering Resource Survey Option: 2 Print Personnel Survey Listing

SORT BY: VAMC//

START WITH VAMC: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

BIOMEDICAL RESOURCES PERSONNEL SURVEY LISTING

- JUL 8,1993 10:01 PAGE 1

•-------------------------------------------------------------------------------­

- VAMC: 87668
- HOSPCODE:
- VAMC ADDRESS:
- FYEARRPT:
- VAMC: 93999
- HOSPCODE: 999
- VAMC ADDRESS: 123 HERE
- FYEARRPT: 93
- I.A.1. NAME: ENUSER2, SEVEN
- 2\. ABBREVIATED CLASS TITLE:
- 2a. TYPE OF CLASSIFICATION: BIOMEDICAL ENGINEER
- 3\. ORGANIZATIONAL TITLE:
- 4\. PAYPLAN/CLASS:
- 4a. GRADE/STEP:
- 5\. EMPLOYEE STATUS: FULL-TIME
- 5a. No. OF MONTHS WORKED: 8
- 5b. SHARED BY:
- 6\. ANNUAL SALARY:
- 7a. GENERAL EXPERTISE:
- 7b. SPECIFIC SKILLS:
- MFG NAME: ENMFGR2, THREE
- EQUIPMENT TYPE: COMPUTER
- MODEL:

#### Print Contract Survey Listing

Select Biomedical Engineering Resource Survey Option: 3 Print Contract Survey Listing

SORT BY: VAMC//

START WITH VAMC: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

BIOMEDICAL RESOURCES SURVEY CONTRACT LISTING APR 8,1993 14:39 PAGE 1 VAMC: 87668

VI.A. CONTRACT SERVICE

VAMC: 93999

VI.A. CONTRACT SERVICE OTHER COMPANY NAME:

MANUFACTURER NAME: ENMFGR2, THREE

TYPE OF EQUIPMENT:

MODEL: \# ACQUISITION COST: \$ CONTRACT COST: \$ CONTRACT PERIOD:

CONTRACT TYPE:

ADDITIONAL COST: \$

#### Print General Survey Listing

Select Biomedical Engineering Resource Survey Option: 4 Print General Survey Listing

SORT BY: VAMC//

START WITH VAMC: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

BIOMEDICAL RESOURCES GENERAL SPECIFICATIONS SURVEY LISTING

APR 8,1993 14:39 PAGE 1

VAMC: 87668

1.  WORK AREA (SQFT):
2.  STORAGE AREA (SQ. FT.):
3.  BME OFFICE (SQ. FT.):

III.A. TOTAL ACQUISITION COST: \$

V.A. COST OF REPAIRS (NON): \$

1.  COST OF PARTS: \$
2.  COST OF X-RAY PART N/T: \$
3.  COST OF X-RAY (TUBES): \$

V.B. COST OF X-RAY CALLS: \$

BIOMEDICAL RESOURCES GENERAL SPECIFICATIONS SURVEY LISTING

APR 8,1993 14:39 PAGE 2

VAMC: 93999

1.  WORK AREA (SQFT):
2.  STORAGE AREA (SQ. FT.):
3.  BME OFFICE (SQ. FT.):

III.A. TOTAL ACQUISITION COST: \$

V.A. COST OF REPAIRS (NON): \$

1.  COST OF PARTS: \$
2.  COST OF X-RAY PART N/T: \$
3.  COST OF X-RAY (TUBES): \$

V.B. COST OF X-RAY CALLS: \$

#### Print Additional Survey Listing

Select Biomedical Engineering Resource Survey Option: 5 Print Additional Survey Listing

SORT BY: VAMC//

START WITH VAMC: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

BIOMEDICAL RESOURCES SURVEY ADDITIONAL SUPPORT LISTING

APR 8,1993 14:39 PAGE 1

VAMC: 87668

VII\. ADDITIONAL SUPPORT AREAS VAMC: 93999

7.  ADDITIONAL SUPPORT AREAS

### Work Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the entering of work action names. On entering this option, the computer will ask Select WORK ACTION NAME.

ENGINEERING PROGRAM MANAGEMENT ROUTINE

1.  Engineering Computer Port
2.  Section List
3.  Work Center Code
4.  Engineering Employee File
5.  Enter/Edit Equipment Category PM Schedule
6.  Manufacturer
7.  ENG SITE PARAMETERS Enter/Edit
8.  SOFTWARE OPTIONS Enter/Edit
9.  Engineering Archive Module
10. Biomedical Engineering Resource Survey

> ---\> 11 Work Action

Select Program Management Option: 11 Work Action

Select NEW WORK ACTION NAME:?? CHOOSE FROM:

BEYOND ECONOMICAL REPAIR B1 CONSULTATION C1

CONTRACTOR ASSISTANCE C2 COULD NOT DUPLICATE C3 DAMAGE/ABUSE D1 ELECTRICAL SAFETY E1

EVALUATION (Equipment) E2 FABRICATION F1

GENERAL REPAIR (In-house) G1

HAZARD ALERT (Equipment) H1 INCOMING INSPECTION I1

INSERVICE EDUCATION (Provide) I2 INSERVICE EDUCATION (Receive) I3 INSTALLATION I4

KEY FABRICATION K1 LOCK CHANGE L1 MISCELLANEOUS M1

MODIFICATION (Equipment) M2 OPERATOR ERROR O1 PERFORMANCE VERIFICATION P1 PREVENTIVE MAINTENANCE P2 PROJECT SUPPORT P3

RELOCATION (Equipment) R1 REMOVAL (Equipment) R2

RENOVATION (Space) R3

SPACE & UTILITY CERTIFICATION S1 UTILITY SYSTEM FAILURE U1

VENDOR SERVICE (Contract) V1

VENDOR SERVICE (Off site repair V2 VENDOR SERVICE (On site repair V3 VENDOR SERVICE (Warranty) V4

Select NEW WORK ACTION NAME: P1 PERFORMANCE VERIFICATION P1 Select SYNONYM: TEST, PERFORMANCE//??

TEST, PERFORMANCE

Informal name for physical location. Example: 'KITCHEN', 'SICU', etc. It's permissible for more than one location to have the same synonym.

Select SYNONYM: TEST, PERFORMANCE//

Select NEW WORK ACTION NAME:

This option allows users to add SYNONYMS to existing Work Actions in order to facilitate lookups. Additions or deletions of WORK ACTIONS themselves should not be made without first consulting with IRM Service.

When no other entries are required under this option, \< RET\> is pressed to access the Program Management option menu.

## Space/Facility Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Space/Facility Management module is entered from the Engineering Main Menu.

AUTOMATED ENGINEERING MANAGEMENT SYSTEM

|      | VERSION 7.0                              |
|------|------------------------------------------|
| WO   | Work Order & MERS                        |
| PLAN | Project Planning                         |
| TRK  | Project Tracking                         |
| EQ   | Equipment Management                     |
| ENM  | Program Management                       |
| SP   | Space/Facility Management                |
| FSA  | 2162 Report of Accident                  |
| XFER | Assign (Transfer) Electronic Work Orders |

Select Engineering Main Menu Option: SP Space/Facility Management The following menu will then be displayed:

ENGINEERING SPACE/FACILITY MANAGEMENT

1.  Space Management
2.  Key/Lock Management
3.  Export Facility Management Data
4.  Facility Management Utilities
5.  Leased Space Options
6.  Planning Space Program Menu

Space Management

This is the main driver option for Engineering Space package.

Key/Lock Management

This is the main driver option for Engineering lock/key management.

Export Facility Management Data

These options output reports in an ASCII format suitable for capturing.

to use in several popular MS-DOS PC spreadsheets for better analysis and graphic capability.

Facility Management Utilities

These options are used to edit files associated with facility management and other utilities for the package.

Leased Space Options

Driver for leased space data entry and printing.

Planning Space Program Menu

Menu for options to be used for entering space planning data for construction projects.

Each of these options can be selected by entering the appropriate number and then pressing \<RET\>. Each of these options will be explained in the following sections.

Package Operation – Space/Facility Management

### Space Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ---\>1 Space Management

2.  Key/Lock Management
191. Export Facility Management Data
192. Facility Management Utilities
193. Leased Space Options
194. Planning Space Program Menu

The Space Management option has the following options:

Enter New Room Space Data.

Enter/edit of space data for any selected room using standard FileMan functionality.

Display/Edit Room Data

Enter/edit space data using a screen server.

Finish Replacement Schedules Report Menu

Driver option for printing scheduled replacement dates for room finishes.

Space Survey Report Menu

Driver option for Engineering Space Reports.

Non-Space File Location Report

This report generates a list of equipment that has an entry in the NON-SPACE FILE LOCATION field. (See page 12-5 for complete documentation).

#### Enter New Room Space Data.

This option uses the edit option of FileMan to add new and edit existing entries in the Space Management file. Choose a room number and edit each field as necessary. The fields will be presented one at a time in standard FileMan format.

More functionalities have been added to aid handling of multi-division facilities, space planning criteria and leased space.

The following is an example of all the fields the user is prompted with after selecting Option l. A question mark (?) was entered at each prompt to display the help information available. It is important to note that for multi-building facilities, the room number should include the building number in the format ROOM NO. - BLDG. NO.

Select Space Management Option: 1 Enter New Room Space Data Select ENG SPACE ROOM NUMBER:??

CHOOSE FROM:

25-7A 7A EAST CLINICAL LABORATORY LAB DNG DINING ROOM

Enter as 'ROOM-BUILDING'; or 'ROOM-BUILDING-DIVISION' at two-division facilities and other sites where building numbers may be duplicated. The Building File (6928.3) is used for data validation.

Identifier of a physical location (room). With the advent of bar coding, it is essential that this field uniquely and unambiguously specify a particular location. Entries may consist of one, two, or three pieces. Hyphens (if present) are treated as delimiters between pieces. First piece (always present) is room designation, second piece (optional) is building designation, and third piece (optional) is division designation (may be used for outpatient clinics, regional offices, etc. as well as for formal divisions).

It is anticipated that most sites will use two-piece entries. True single-building facilities may use one-piece entries. Multi-division facilities and sites supporting remote offices where duplicate building numbers may be a problem should use three- piece entries.

Entry of a two-piece ROOM NUMBER will automatically populate the BUILDING field. Entry of a three-piece ROOM NUMBER will automatically populate the BUILDING and DIVISION fields.

Hyphens must not be used as anything other than delimiters between ROOM, BUILDING, and DIVISION.

Select ENG SPACE ROOM NUMBER: 25-7A 7A EAST CLINICAL LABORATORY LAB ROOM NUMBER: 25-7A//

BUILDING NUMBER: 7A//??

Assigned number of the BUILDING. This field is populated automatically when ROOM NUMBERS are entered as 'ROOM-BUILDING'.

BUILDING NUMBER: 7A// DIVISION:

WING: EAST//??

Intended as a means of defining functional groupings of physical locations. WINGs may or may not equate to an extension or annex of a building, and/or a clinical specialty area (ex: surgical wing) of a hospital. Used in the Equipment Management Module. In sorting a Preventive Maintenance Worklist by LOCATION, the system will attempt to sort by WING rather than ROOM NUMBER.

WING: EAST//

SERVICE: CLINICAL LABORATORY//??

CHOOSE FROM: CLINICAL LABORATORY

ENGINEERING SVC IRM

SERVICE: CLINICAL LABORATORY// c• • KEY:??

1111

KEY: 1111

Select OTHER KEY:??

Enter multiple free text entries for other keys that have been added to this Lock other than the one selected in the KEY field. The KEY field is a pointer to the LOCK file.

Select OTHER KEY:

FUNCTION: LAB//??

This field points to function file for selection of rooms primary use.

FUNCTION: LAB// LENGTH IN FT.: 55 WIDTH IN FT.: 25• CEILING HT: 10 NET SQ.FT.:

SPACE GUIDE:

H-08-9 CRITERIA:??

Criteria Chapter from H-08-9 Space Planning Criteria. Especially important when entering a project space plan (IMFP).

CHOOSE FROM:

A & MM ADMINISTRATION 284

A & MM SUPPLY, PROCESSING AND 285

VOCATIONAL REHABILITATION AND 828

VOLUNTARY SERVICE 290

H-08-9 CRITERIA:

BEDS:

BED TYPE:

SPECIAL CHARACTERISTICS:

WALL:??

CHOOSE FROM:

VP VINYL PAPER

CT CERAMIC TILE

PT PAINT

WP WOOD PANELING

BL BLOCK

PL PLASTER

OT OTHER WALL: PL PLASTER

WALL FINISH DESCRIPTION:

WALL REPLACEMENT DATE: 1-1-92 (JAN 01, 1992) FLOOR:??

TYPE OF FLOOR FINISH MATERIAL CHOOSE FROM:

CP CARPET

TL TILE

CT CERAMIC TILE

CE CONCRETE

SV SHEET VINYL

CF CONDUCTIVE FLOORING

TE TERRAZZO FLOOR: TL TILE

FLOOR FINISH DESCRIPTION:

FLOOR REPLACEMENT DATE:??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. You may omit the precise day, as: JAN, 1957

FLOOR REPLACEMENT DATE: 02/02/89 (FEB 02, 1989) CEILING:??

CHOOSE FROM:

G GRID

P PLASTER

C CONCRETE

O OTHER

CEILING: G GRID

CEILING FINISH DESCRIPTION:

CEILING REPLACEMENT DATE: 03/03/93 (MAR 03, 1993)

Select LIGHTING:?? CHOOSE FROM:

F FLUORESCENT

I INCANDESCENT

O OTHER

Select LIGHTING: F (FLUORESCENT)• FIXTURE QTY: 10

WATTAGE: 100

Select LIGHTING:

WINDOWS: 5 WINDOW TYPE:??

CHOOSE FROM:

SS SINGLE HUNG/SINGLE GLAZED

SD SINGLE HUNG/DOUBLE GLAZED

DS DOUBLE HUNG/SINGLE GLAZED

DD DOUBLE HUNG/DOUBLE GLAZED

O OTHER

WINDOW TYPE: SD SINGLE HUNG/DOUBLE GLAZED DRAPES:

CUB. CTNS.:

DOORS:

Select UTILITIES:?? CHOOSE FROM:

A/C - CENTRAL

ELEC-208V +

PAGING SYSTEM '^' TO STOP:

Select UTILITIES: A/C - CENTRAL

ARE YOU ADDING 'A/C - CENTRAL' AS A NEW UTILITIES (THE 1ST FOR THIS ENG SPACE

)? Y

(YES)

Select UTILITIES:

BLDG MNGT AMIS CLASS:??

Entry indicates one of the 14 divisions on the AMIS form VA-10-6007a.

This will be used to generate a report from the Space Survey Report

menu for use by Building Management Service for quarterly AMIS reporting. CHOOSE FROM:

1.  PSYCHIATRY
2.  INTERMEDIATE
3.  MEDICINE
4.  NEUROLOGY
5.  R.M.S.
6.  S.C.I.
7.  SURGERY
8.  N.H.C.U.
9.  DOMICILIARY
10. CLINICS
11. DENTAL
12. RESEARCH
13. ADMIN.
14. OTHER

BLDG MNGT AMIS CLASS: 12 RESEARCH RCS 10-0141(14-4):??

CHOOSE FROM:

Y YES

N NO

RCS 10-0141(14-4):

COMMENTS:

1\>

Select ENG SPACE ROOM NUMBER:

You may enter another room number at the above prompt or press \< RET\> to return to the Space Management option main menu.

#### Display/Edit Room Data

This option shows a room entry with all its associated data on the screen at one time. All fields will be displayed and can be viewed, edited, or printed on another device.

This is an easy method of printing data on individual rooms, for use in the Space committee, or for whenever a quick picture of a room is needed.

The following is an example of the screen display for room 25-7A. Each of the fields on the screen can be edited by selecting the field number.

Select ENG SPACE ROOM NUMBER: 25-7A 7A EAST CLINICAL LABORATORY LAB SINGLE ROOM DATA DISPLAY

1\) ROOM NO. : 25-7A 2) BUILDING \#: 7A

3\) WING : EAST 4) SERVICE : CLINICAL LABORATORY

5\) ROOM KEY : 1111 6) FUNCTION : LAB

7\) NO. OF BED: 8) SPEC CHAR.:

9\) LENGTH : 55 10) WIDTH : 24 11) NET SF:

12)WALL : PL 13) FLOOR :TL 14) CEILING: G

15)REPL.DT: 01/01/92 16) REPL.DT:02/02/89 17) REPL.DT:03/03/93

18)LIGHTING : F QUANTITY : 10 WATTAGE : 100

19\) WINDOW QTY: 5 20) WINDOW TYPE: SD

21\) DRAPE NO.: 22) CUB. CTNS.:

23\) DOOR QTY : 24) RCS 10-0141:

25) UTILITIES: A/C - CENTRAL
26) COMMENTS:
27) SYNONYM:

Choose Item to Enter/Edit (2-27, D(DISPLAY), P(PRINT)): EXIT//

Want to view another? YES// N (NO)

> **NOTE:** Users who do not hold the ENROOM security key will not be allowed to edit data via this option.

#### Finish Replacement Schedules Report Menu

Fields have been added to record the estimated replacement dates for ceilings, walls, and floors. These dates can be sorted, and a replacement schedule printed through the use of this option. The menu includes the four options shown below.

Finish Replacement Schedules Report Menu

1.  Replacement Schedule for All Finishes
2.  Ceiling Replacement Schedule
3.  Wall Replacement Schedule
4.  Floor Replacement Schedule

Select Finish Replacement Schedules Report Option:

An example of each report is included at the end of this section. Replacement Schedule for All Finishes

This option prints out a range of user selected rooms with dates for all finishes on a 132-column printout sorted by room number.

Ceiling Replacement Schedule

This option prints a range of dates for ceiling replacement only, sorted by date.

Wall Replacement Schedule

This option prints a range of dates for wall finish replacement only, sorted by date.

Floor Replacement Schedule

This option prints a range of dates for floor finish replacement only, sorted by date.

1.  Replacement Schedule for All Finishes

ROOM FINISH REPLACEMENT SCHEDULE FEB 1,1990 13:35 PAGE 1

Select Finish Replacement Schedules Report Menu Option: 1 Replacement Schedule for All Finishes

START WITH ROOM NUMBER: FIRST// • • DEVICE: LAN RIGHT MARGIN: 132//

ROOM FINISH REPLACEMENT SCHEDULE MAR 31,1993 13:48 PAGE 1 BUILDING

ROOM NUMBER, NUMBER SERVICE WALL REPL FLOOR CEILING

DATE REPL DATE REPL DATE

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>25-7A</th>
<th>7A</th>
<th>CLINICAL</th>
<th>LABORATORY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>01/01/92</p>
<p>DNG</p>
<ul>
<li><p>ROOM FINISH</p></li>
</ul></td>
<td><p>02/02/89 03/03/93</p>
<p>REPLACEMENT SCHEDULE</p></td>
<td></td>
<td>MAR 31,1993 13:48 PAGE 2</td>
</tr>
</tbody>
</table>

BUILDING

ROOM NUMBER NUMBER SERVICE WALL REPL FLOOR CEILING

DATE REPL DATE REPL DATE

LVR

2.  Ceiling Replacement Schedule

Select Finish Replacement Schedules Report Menu Option: 2 Ceiling Replacement Schedule

START WITH CEILING REPLACEMENT DATE: FIRST// DEVICE: LAN RIGHT MARGIN: 132//

ROOM FINISH REPLACEMENT SCHEDULE MAR 31,1993 13:48 PAGE 1 BUILDING

ROOM NUMBER NUMBER SERVICE CEILING FINISH DESCR. REPL DATE

CEILING REPLACEMENT DATE: MAR 3,1993

25-7A 7A CLINICAL LABORATORY GRID 03/03/93

3.  Wall Replacement Schedule

Select Finish Replacement Schedules Report Menu Option: 3 Wall Replacement Schedule START WITH WALL REPLACEMENT DATE: FIRST//

DEVICE: LAN RIGHT MARGIN: 132//

ROOM FINISH REPLACEMENT SCHEDULE MAR 31,1993 13:48 PAGE 1

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>ROOM NUMBER WALL</th>
<th><p>BUILDING NUMBER</p>
<p>FINISH DESCR.</p></th>
<th>SERVICE REPL DATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">WALL REPLACEMENT DATE: JAN 1,1992</td>
</tr>
<tr class="even">
<td>25-7A</td>
<td>7A</td>
<td>CLINICAL LABORATORY</td>
</tr>
<tr class="odd">
<td>PLASTER</td>
<td></td>
<td>01/01/92</td>
</tr>
</tbody>
</table>

4.  Floor Replacement Schedule

Select Finish Replacement Schedules Report Menu Option: 4 Floor Replacement Schedule

START WITH FLOOR REPLACEMENT DATE: FIRST// DEVICE: LAN RIGHT MARGIN: 132//

ROOM FINISH REPLACEMENT SCHEDULE MAR 31,1993 13:49 PAGE 1 BUILDING

ROOM NUMBER NUMBER SERVICE

FLOOR FINISH DESCR. REPL DATE

FLOOR REPLACEMENT DATE: FEB 2,1989

25-7A 7A CLINICAL LABORATORY TILE 02/02/89

#### Space Survey Report Menu

The Space Survey Report Menu has the following options:

1.  Room/Keying/Function Report

Room listing with keys that open room.

2.  Space Survey by Room

Generates print-out of space data sorted by room number.

3.  Service Space Survey

Generates listing of space data sorted by owning service. Allows full listing or a summary of square foot figures only.

4.  Function Space Survey

Generates list of rooms sorted by designated function.

5.  Building Space Survey

Prints principal fields from Engineering Space file. Sorts first by building, then by room.

6.  RCS 10-0141 Report

Report to aid in preparing CDR data for Fiscal Service.

7.  Building Management RCS 10-203, VAF 10-6007a

Generates a square footage report in the AMIS format needed by Building Management.

These reports are now sorted by DIVISION as well as BUILDING.

1.  Room/Keying/Function Report

The Room/Keying/Function Report is an 80-column report that ties the Lock and Space files together. It prints the Room Number and Function from the Space file and the different levels of keying information from the Lock file. This presents a report of all of the keying information about a single room or group or rooms.

This option will also allow sorting by Service with a secondary sort on

the key name and a tertiary sort in room order under each key. The report sections are segregated for clarity and therefore make an excellent keying plan document for each service.

PAGE 1

ROOM MST SUB

NUMBER GGM KEY MST KEY .............................................. OTHER

| 111     |     | ...................................................................  |      |
|---------|-----|----------------------------------------------------------------------|------|
| 115     |     | ...................................................................  |      |
| 123     |     | ...................................................................  |      |
| 152     |     | ...................................................................  |      |
| 277     |     | ...................................................................  |      |
| 434     |     | ...................................................................  |      |
| 456     |     | ...................................................................  |      |
| 564     | YES | 31 ................................................................. |      |
| 789     | YES | 31 ................................................................. |      |
| 100-1   |     | ...................................................................  |      |
| 101-1   |     | ...................................................................  |      |
| 102-24  | YES | ENG ................................................................ | FLR  |
| 106-11  | YES | ENG ................................................................ | FLR  |
| 111-B   |     | ...................................................................  |      |
| 1D-145  |     | ...................................................................  |      |
| 100     |     | ...................................................................  |      |
| 2-4-203 |     | ...................................................................  |      |
| 4-10    |     | ............................................................... GGGM |      |
| 4-105   |     | ...................................................................  |      |
| 444-1   |     | ...................................................................  |      |
| A-111   |     | ...................................................................  |      |
| ASYLUM  |     | ............................................................... GGGM |      |
| BMED    |     | ...................................................................  |      |
| C-124   |     | ...................................................................  |      |
| C123-1  |     | ...................................................................  |      |
| D-144   | YES | MM-1 ............................................................... | SS-1 |

2.  Space Survey by Room

This option prints a l32-column report sorted by room number that has most of the pertinent data fields associated with the Space file. The report loses clarity when printed on the 80-column screen since it is designed for l32-column paper. Most terminals can be switched to l32-column for displaying this report on the screen.

- Select Space Survey Report Menu Option: 2 Space Survey by Room
- START WITH BUILDING NUMBER: FIRST//
- START WITH ROOM NUMBER: FIRST//
- DEVICE:;;690 0 LAN RIGHT MARGIN: 80// 132

ENGINEERING SPACE INVENTORY (132 col.) JUL 20,1993 08:57 PAGE 1

> B W D

> NET E N R 14

> ROOM NUMBER WING SERVICE KEY FUNCTION S.F. D WALL FLOOR CEILING LIGHTING D S -4

> --------------------------------------------------------------------------------

> BUILDING NUMBER: 100

> 101-100-JC CLINICAL LABORA LAB

> 102-100-JC

> 12-100-JC CLINICAL LABORA LAB 400 VINYL PAPER CARPET GRID FLOURESCENT 4 2 YES

200-100-JC CLINICAL LABORA 11124 LAB 900 PLASTER TILE YES

BUILDING NUMBER: 120

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>210E-120</p></li>
</ul></th>
<th>CLINICAL LABORA BUILDING NUMBER: 7A</th>
<th colspan="7" rowspan="2"></th>
</tr>
<tr class="odd">
<th><ul>
<li><p>210-7A</p></li>
</ul></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>25-7A</p></li>
</ul></td>
<td>EAST CLINICAL LABORA 1111 LAB</td>
<td>1000</td>
<td>PLASTER</td>
<td>TILE</td>
<td>GRID</td>
<td>FLOURESCENT</td>
<td>5</td>
<td>YES</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="6" rowspan="5"></td>
</tr>
<tr class="odd">
<td>30-7A</td>
<td>CLINICAL LABORA STORAGE, GENERAL</td>
<td>160</td>
</tr>
<tr class="even">
<td><ul>
<li><p>LVR</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>----</td>
</tr>
<tr class="even">
<td><ul>
<li><p>TOTAL</p></li>
</ul></td>
<td></td>
<td>2460</td>
</tr>
</tbody>
</table>

Press \<RETURN\> to continue.

3.  Service Space Survey

This option has the same format as option 2 except that it sorts the list by Owning Service and subtotals the Net Square Footage for each service.

- Select Space Survey Report Menu Option: 3 Service Space Survey
- Want just a net square foot and room count summary? NO// (NO)
- START WITH BUILDING NUMBER: FIRST//
- START WITH SERVICE: FIRST//
- START WITH ROOM NUMBER: FIRST//
- DEVICE:;;60 LAN RIGHT MARGIN: 80// 132

ENGINEERING SPACE INVENTORY BY OWNING SERVICE JUL 20,1993 08:58 PAGE 1

> B W D

> NET E N R 14

> ROOM NUMBER WING SERVICE KEY FUNCTION S.F. D WALL FLOOR CEILING LIGHTING D S -4

--------------------------------------------------------------------------------------

> BUILDING NUMBER: 100

> 101-100-JC CLINICAL LABORA LAB

> 12-100-JC CLINICAL LABORA LAB 400 VINYL PAPER CARPET GRID FLOURESCENT 4 2 YES

200-100-JC CLINICAL LABORA 11124 LAB 900 PLASTER TILE YES

> SUBTOTAL 1300

> BUILDING NUMBER: 120

> 210E-120 CLINICAL LABORA

> ----

> SUBTOTAL 0

> BUILDING NUMBER: 7

> 25-7A EAST CLINICAL LABORA 1111 LAB 1000 PLASTER TILE GRID FLOURESCENT 5 YES 3

> 0-7A CLINICAL LABORA STORAGE, GENERAL 160

> ----

> SUBTOTAL 1160

> ----

> TOTAL 2460

Press \<RETURN\> to continue.

4.  Function Space Survey

This option is the same as Option 3 except it sorts by function and sub-totals Net Square footage by function.

- Select Space Survey Report Menu Option: 4 Function Space Survey
- Want just a net square foot and room count summary? NO// (NO)
- START WITH BUILDING NUMBER: FIRST//
- START WITH FUNCTION: FIRST//
- START WITH ROOM NUMBER: FIRST//
- DEVICE:;;60 LAN RIGHT MARGIN: 80// 132

ENGINEERING SPACE INVENTORY BY ROOM FUNCTION JUL 20,1993 08:58 PAGE 1

> B W D

> NET E N R 14

> ROOM NUMBER WING SERVICE KEY FUNCTION S.F. D WALL FLOOR CEILING LIGHTING D S -4

--------------------------------------------------------------------------------------

> BUILDING NUMBER: 100

> 101-100-JC CLINICAL LABORA LAB

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>12-100-JC</p></li>
</ul></th>
<th>CLINICAL LABORA</th>
<th>LAB</th>
<th>400</th>
<th>VINYL PAPER</th>
<th>CARPET</th>
<th>GRID</th>
<th>FLOURESCENT</th>
<th>4</th>
<th>2</th>
<th>YES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>200-100-JC</td>
<td>CLINICAL LABORA 11124</td>
<td>LAB</td>
<td>900</td>
<td>PLASTER</td>
<td>TILE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>YES</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>SUBTOTAL</p></li>
</ul></td>
<td></td>
<td></td>
<td>1300</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

BUILDING NUMBER: 7A

25-7A EAST CLINICAL LABORA 1111 LAB 1000 PLASTER TILE GRID FLOURESCENT 5 YES

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 37%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>SUBTOTAL</p></li>
<li><p>30-7A</p></li>
</ul></th>
<th>CLINICAL LABORA</th>
<th><p>1000</p>
<p>STORAGE, GENERAL 160</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>----</td>
</tr>
<tr class="even">
<td><ul>
<li><p>SUBTOTAL</p></li>
</ul></td>
<td></td>
<td>160</td>
</tr>
</tbody>
</table>

5.  Building Space Survey

This option is the same as Option 4 except that it sorts by Building and gives subtotals by building. This would be useful for multi-building facilities.

- Select Space Survey Report Menu Option: 5 Building Space Survey
- Want just a net square foot and room count summary? NO// (NO)
- START WITH BUILDING NUMBER: FIRST//
- START WITH ROOM NUMBER: FIRST//
- DEVICE:;;60 LAN RIGHT MARGIN: 80// 132

ENGINEERING SPACE INVENTORY BY BUILDING JUL 20,1993 08:55 PAGE 1

<table style="width:100%;">
<colgroup>
<col style="width: 64%" />
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 4%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>B</p></li>
</ul></th>
<th></th>
<th></th>
<th>W</th>
<th>D</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>NET E</p></li>
</ul></td>
<td></td>
<td></td>
<td>N</td>
<td>R 14</td>
</tr>
<tr class="even">
<td><ul>
<li><p>ROOM NUMBER WING SERVICE KEY FUNCTION S.F. D WALL</p></li>
</ul></td>
<td>FLOOR</td>
<td>CEILING LIGHTING</td>
<td>D</td>
<td>S -4</td>
</tr>
</tbody>
</table>

--------------------------------------------------------------------------------------

BUILDING NUMBER: 100

101-100-JC CLINICAL LABORA LAB

102-100-JC

12-100-JC CLINICAL LABORA LAB 400 VINYL PAPER CARPET GRID FLOURESCENT 4 2 YES

200-100-JC CLINICAL LABORA 11124 LAB 900 PLASTER TILE YES

SUBTOTAL 1300

BUILDING NUMBER: 120

210E-120 CLINICAL LABORA

SUBTOTAL 0

BUILDING NUMBER: 7A

210-7A

25-7A EAST CLINICAL LABORA 1111 LAB 1000 PLASTER TILE GRID FLOURESCENT 5 YES

30-7A CLINICAL LABORA STORAGE, GENERAL 160

----

SUBTOTAL 1160

TOTAL 2460

Press \<RETURN\> to continue.

6.  RCS 10-0141 Report

This option gives a subtotal for each service that has been indicated to fall under the RCS 10-0l41 report for Fiscal Service. Each room that is to be charged to the cost accounting report should be marked with a \< Y\> in the RCS l0-0l4l field of the space file.

Select Space Survey Report Menu Option: 6 RCS 10-0141 Report

- START WITH BUILDING NUMBER: FIRST//
- START WITH SERVICE: FIRST//
- DEVICE:;;60 LAN RIGHT MARGIN: 80// 132

RCS 14-4 REPORTABLE SPACE SORTED BY SERVICE JUL 20,1993 08:56 PAGE 1

NET SQ.FT.

•-----------------------------------------------------------------------------------RCS 10-0141(14-4): YES

BUILDING NUMBER: 100

SERVICE: CLINICAL LABORATORY

SUBTOTAL 1300.0

SUBCOUNT 2

SUBMEAN 650.0

BUILDING NUMBER: 7A

SERVICE: CLINICAL LABORATORY

SUBTOTAL 1000.0

SUBCOUNT 1

SUBMEAN 1000.0

TOTAL 2300.0

COUNT 3

MEAN 766.7

Press \<RETURN\> to continue.

7.  Building Management RCS 10-203, VAF 10-6007a

This option will generate a square footage report in the AMIS format needed by Building Management.

BUILDING MANAGEMENT AMIS REPORT, RCS 10-203 MAR 31,1993 13:53 PAGE 1 NET SQ.FT.

TOTAL 345600.0

COUNT 210

BUILDING MANAGEMENT AMIS REPORT, RCS 10-203 FEB 22,1111 09:21 PAGE 1 NET SQ.FT.

BLDG MNGT AMIS CLASS: MEDICINE

| SUBTOTAL | 7000.0 |
|----------|--------|
| SUBCOUNT | 1      |
| SUBMEAN  | 7000.0 |
| TOTAL    | 7000.0 |
| COUNT    | 1      |
| MEAN     | 7000.0 |

BUILDING MANAGEMENT AMIS REPORT, RCS 10-203 FEB 22,1111 09:21 PAGE 1 NET SQ.FT.

BLDG MNGT AMIS CLASS: PHYSICAL PLANT

### Key/Lock Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENGINEERING SPACE/FACILITY MANAGEMENT

> 1 Space Management

> ---\> 2 Key/Lock Management

3.  Export Facility Management Data
4.  Facility Management Utilities
5.  Leased Space Options
6.  Planning Space Program Menu The options for Key/Lock Management are:

Key Distribution by Employee Enter/Edit

Enter/edit list of door keys assigned to individual employees.

Lock Number File Enter/Edit

Enter/edit information on door locks, by control number.

Print Key Distribution by Employee

Generates list of employees to whom door keys have been individually assigned. Information on keys assigned is provided.

Print Employee List sorted by Key

Prints list of all employees (if any) who have been issued door keys within a user-specified range of keys.

Print Employee List by Service

Lists employees and keys in order by service, page break on each service. For review, by Service, of key holders

#### Key Distribution by Employee Enter/Edit

This option serves the same purpose as the earlier releases. Keys are assigned to employees for accountability. NOTE: Employees must be entered under this option in order to run the print options of the Key/Lock Management option.

The following is an example of all the fields the user is prompted with after selecting option 3. Two question marks were entered at each prompt to display the help information available.

Select EMPLOYEE(KEYS): ??

Select EMPLOYEE(KEYS): ENUSER2, SEVEN•

ARE YOU ADDING 'ENUSER2, SEVEN' AS A NEW EMPLOYEE(KEYS) (THE 7TH)? Y (YES) EMPLOYEE: ENUSER2, SEVEN//

SERVICE: ENG//??

CHOOSE FROM:

CLINICAL LABORATORY ENGINEERING SVC

IRM

SERVICE: ENG• //CLINICAL LABORATORY ID NUMBER: ??

Select KEYS ISSUED: ??

1111

Select KEYS ISSUED: 1111

ARE YOU ADDING '1111' AS A NEW KEYS ISSUED (THE 1ST FOR THIS EMPLOYEE(KEYS))? Y (YES)

Select DATE ISSUED: T-10 MAR 21, 1993•

ARE YOU ADDING 'MAR 21, 1993' AS A NEW DATE ISSUED (THE 1ST FOR THIS KEYS ISSUED)? Y (YES)

QUANTITY ISSUED: ??

Enter the quantity of this key number that was issued to the employee on this particular date only. The total quantity from all dates will be calculated.

by the system.

QUANTITY ISSUED: 1 TOTAL QUANTITY ISSUED:??

Enter the total of this key issued on all recorded dates.

TOTAL QUANTITY ISSUED: 1 Select KEYS ISSUED:

Select EMPLOYEE(KEYS):

You may enter another name at the above prompt or press \< RET\> to return to the Space/Facility Management option main menu.

#### Lock Number File Enter/Edit

This option serves the same purpose as before in that information can be entered or edited on the facility's locks.

In the following example, a question mark has been entered after each field to display the help information available.

Select LOCKS KEY: GA-1 KEY: GA-1// ?

ANSWER MUST BE 1-10 CHARACTERS IN LENGTH KEY: GA-1//

CTRL KEY:

GGM: YES// ?

| CHOOSE FROM: |       |                  |
|--------------|-------|------------------|
|              | Y     | KEYED TO GGM     |
|              | N     | NOT KEYED TO GGM |
| GGM:         | YES// |                  |

Select MASTER: ENG// ??

MASTER KEYS FOR THIS LOCK ENTER MASTER KEYS FOR THIS LOCK

Select MASTER: ENG// Select SUB-MASTER: FLR// ?

ANSWER WITH SUB-MASTER: 1 FLR YOU MAY ENTER A NEW SUB-MASTER, IF YOU WISH ANSWER MUST BE 1-4 CHARACTERS IN LENGTH ENTER SUB-MASTER KEYS FOR THIS LOCK

Select SUB-MASTER: FLR// Select LOCKS KEY:

You may enter another key at the above prompt or press \< RET\> to return to the Space/Facility Management Option main menu.

#### Print Key Distribution by Employee

This option prints a list, sorted by employee, of employees and the keys that they are accountable for. After selecting this option you are asked which employee you wish to start with and go to, and then prompted for an output device.

START WITH EMPLOYEE: FIRST// ENUSER3, E IGHT

GO TO EMPLOYEE: LAST//

DEVICE: HOME// RIGHT MARGIN: 79//

Return to the Space Management option main menu by pressing \< RET\>.

The following page is an example of a printout of the Key Distribution by Employee Report.

KEY DISTRIBUTION REPORT SORTED BY EMPLOYEE MAR 31,1993 21:05

EMPLOYEE ............................................................ SERVICE ID

...................................................................

ENUSER3, EIGHT ...... .............................................................

ENUSER3, NINE ..... ..............................................................

ENUSER4, TEN .... ...............................................................

... ................................................................

.. .................................................................

. ..................................................................

ENUSER4, TEN ...............................................................

ENUSER4, ONE ...............................................................

ENUSER4, TWO ...............................................................

...................................................................

ENUSER4, THREE . ..................................................................

...................................................................

ENUSER4, FOUR ....... ............................................................

...................................................................

ENUSER4, FIVE . ..................................................................

ENUSER4, SIX ...............................................................

ENUSER4, SEVEN ...............................................................

ENUSER4, EIGHT ENGINEERING .......................................................

#### Print Employee List Sorted by Key

This option, while similar to option 5, is more oriented to keys. It presents a list, sorted by key number, of data about the lock and includes the employees that hold the key.

After selecting this option you are asked which key you wish to start with and then prompted for an output device.

START WITH KEY: FIRST// GA-1 GO TO KEY: LAST// GA-2

DEVICE: HOME// RIGHT MARGIN: 80//

KEY/LOCK REPORT WITH EMPLOYEE DISTRIBUTION............ MAR 30,1993 15:37 PG 1

KEY GGM ................................................................... M

...................................................................

GA-1 ...............................................................

GA-2 NOT KEYED TO GGM .......................................................... GA

#### Print Employee List by Service

This option, while similar to option 5, is more oriented to employee service. It presents a list, sorted by service, of data about the lock and includes the employees that hold the key. A page break is made for each service.

After selecting this option you are asked which key you wish to start with and then prompted for an output device.

START WITH SERVICE: FIRST// LABORATORY START WITH EMPLOYEE: FIRST//

DEVICE: HOME RIGHT MARGIN: 80//

Service Key Holders by Employee Name JUN 7,1111 13:15 PAGE 1

ID KEYS

EMPLOYEE SERVICE NUMBER .......................... ISSUED QTY

ENUSER2, SEVEN CLINICAL LABORATORY 322 ............................. 1111 1

ENUSER4, NINE IRM 277 ....................................

ENUSER5, TEN LABORATORY

### Export Facility Management Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Space Management
2.  Key/Lock Management

> ---\> 3 Export Facility Management Data

4.  Facility Management Utilities
5.  Leased Space Options
6.  Planning Space Program Menu

The Export Facility Management Data options are:

Output Service/NSF Spreadsheet

Output an ASCII file that can be captured via a smart terminal for loading into a commercial spreadsheet product.

Output Function/NSF Spreadsheet

Output an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

Output RCS 10-0141 Spreadsheet

Output an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

#### Output Service/NSF Spreadsheet

This option outputs an ASCII file that can be captured via a smart terminal for loading into a commercial spreadsheet product. The following prompts are generated.

Report sorted by Service is Requested

I must do a FileMan sort to organize the data you want to export. The data will Print in FileMan format on your screen. At the end of the print you will be instructed on how to capture the data you have requested.

No Device Selection will be asked. This option cannot be queued.

Press \<RETURN\> when ready, or '^' to escape. START WITH SERVICE: FIRST//

ENG SPACE STATISTICS JAN 8,1992 09:20 PAGE 1 NET SQ.FT.

TOTAL 0.0

COUNT 0

Press \<RETURN\> to continue.

Ready to list Spreadsheet data in Comma Separated Value (CSV) format.

Turn on your ASCII file capture feature and save an MS-DOS file with an extension of CSV, i.e. ASCII file name = CSV

At the end of the data listing, turn off your ASCII file capture feature and then open the CSV file in your spreadsheet program to produce graphs.

> **NOTE:** The last cell of your spreadsheet will contain extraneous text. You'll probably want to delete it.

Press \<RETURN\> when ready, or '^' to escape. Facility Management Data

Service Report

Net Square Foot and Room Count Report

SERVICE, COUNT, NET SQUARE FT.

Turn off data capture, Press \<RETURN\> when ready.

I still have this data stored and can list it for capture again without re-running the FileMan sort in case you missed it the first time.

Want to list the data again? NO// (NO)

Upon exit, the user returns to the Export Facility Management Data menu.

#### Output Function/NSF Spreadsheet

This option outputs an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

Report sorted by Function is requested.

I must do a FileMan sort to organize the data you want to export. The data will Print in FileMan format on your screen. At the end of the print you will be instructed on how to capture the data you have requested.

No Device Selection will be asked. This option cannot be queued.

Press \<RETURN\> when ready, or '^' to escape. START WITH FUNCTION: FIRST//

ENG SPACE STATISTICS JAN 8,1992 09:21 PAGE 1 NET SQ.FT.

TOTAL 0.0

COUNT 0

Press \<RETURN\> to continue.

Ready to list Spreadsheet data in Comma Separated Value (CSV) format.

Turn on your ASCII file capture feature and save an MS-DOS file with an extension of CSV, i.e. ASCII file name = CSV

At the end of the data listing, turn off your ASCII file capture feature and then open the CSV file in your spreadsheet program to produce graphs.

> **NOTE:** The last cell of your spreadsheet will contain extraneous text. You'll probably want to delete it.

Press \<RETURN\> when ready, or '^' to escape. Facility Management Data

Function Report

Net Square Foot and Room Count Report

FUNCTION, COUNT, NET SQUARE FT.

Turn off data capture, Press \<RETURN\> when ready.

I still have this data stored and can list it for capture again without re-running the FileMan sort in case you missed it the first time.

Want to list the data again? NO// (NO)

Upon exit, the user returns to the Export Facility Management Data menu.

#### Output RCS 10-0141 spreadsheet

This option outputs an ASCII file that can be captured via a smart terminal for use in a commercial spreadsheet.

Report by EUO 14-4 Services is requested.

I must do a FileMan sort to organize the data you want to export. The data will Print in FileMan format on your screen. At the end of the print you will be instructed on how to capture the data you have requested.

No Device Selection will be asked. This option cannot be queued.

Press \<RETURN\> when ready, or '^' to escape.

START WITH SERVICE: FIRST//

ENG SPACE STATISTICS JAN 8,1992 09:21 PAGE 1 NET SQ.FT.

TOTAL 0.0

COUNT 0

Press \<RETURN\> to continue.

Ready to list Spreadsheet data in Comma Separated Value (CSV) format.

Turn on your ASCII file capture feature and save an MS-DOS file with an extension of CSV, i.e. ASCII file name = CSV

At the end of the data listing, turn off your ASCII file capture feature and then open the CSV file in your spreadsheet program to produce graphs.

> **NOTE:** The last cell of your spreadsheet will contain extraneous text. You'll probably want to delete it.

Press \<RETURN\> when ready, or '^' to escape. Facility Management Data

RCS 14-4 Report

Net Square Foot and Room Count Report

SERVICE, COUNT, NET SQUARE FT.

Turn off data capture, Press \<RETURN\> when ready.

I still have this data stored and can list it for capture again without re-running the FileMan sort in case you missed it the first time.

Want to list the data again? NO// (NO)

Upon exit, the user returns to the Export Facility Management Data menu.

### Facility Management Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Space Management
2.  Key/Lock Management
3.  Export Facility Management Data

> ---\> 4 Facility Management Utilities

5.  Leased Space Options
6.  Planning Space Program Menu

The Space Management Utilities provide a quick and efficient means of entering and editing building sites, building space, and space utilities.

1.  Edit Space Functions file.
2.  Edit Space Utilities file.
3.  Remove Dangling Pointers in LOCK File
4.  Building File Enter/Edit
5.  Print All Building Data

Select Space Management Utilities Option:

The four sub options share the same entry and editing format. An example of each is presented below.

#### Edit Space Functions File

Use this option to enter or edit space functions into the space file.

Select ENG SPACE FUNCTIONS NAME:? ANSWER WITH ENG SPACE FUNCTIONS NAME

DO YOU WANT THE ENTIRE 108-ENTRY ENG SPACE FUNCTIONS LIST? Y (YES) CHOOSE FROM:

ADMINISTRATIVE ASSISTANT AGENT CASHIER

ANIMAL QUARTERS ASSISTANT DIRECTOR ASSOCIATE DIRECTOR BATH, RESIDENT ON-CALL BATH/SHOWER ROOM

BED ROOM - 1 BED, BEDROOM - ISOLATION '^' TO STOP: ^

YOU MAY ENTER A NEW ENG SPACE FUNCTIONS, IF YOU WISH

ANSWER MUST BE 3-30 CHARACTERS IN LENGTH. LOCAL NAMES MUST START WITH 'ZZ'.

YOU CANNOT EDIT THE NATIONAL PORTION OF THE FUNCTION FILE. Select ENG SPACE FUNCTIONS NAME: BOILER PLANT

NAME: BOILER PLANT// CRITERIA SPACE (NSF):??

Amount of space (net square feet) authorized by H-08 Program Guides for this particular function.

CRITERIA SPACE (NSF):

Upon exit, the user is returned to the Facility Management Utilities menu.

#### Edit Space Utilities File.

This option is used to enter a new utility into the Space Management file.

Select ENG SPACE UTILITIES UTILITY:? ANSWER WITH ENG SPACE UTILITIES UTILITY

DO YOU WANT THE ENTIRE 31-ENTRY ENG SPACE UTILITIES LIST? Y (YES) CHOOSE FROM:

A/C - CENTRAL A/C - ROOM

AIR-COMPRESSED CCTV

COMPUTER MODEM COMPUTER PRINTER COMPUTER TERMINAL DUMBWAITER

ELEC-208V + ELEC-EMERGENCY '^' TO STOP: ^

YOU MAY ENTER A NEW ENG SPACE UTILITIES, IF YOU WISH ANSWER MUST BE 3-30 CHARACTERS IN LENGTH

Select ENG SPACE UTILITIES UTILITY: CCTV UTILITY: CCTV//

Select ENG SPACE UTILITIES UTILITY:

Upon exit, the user is returned to the Facility Management Utilities menu.

#### Remove Dangling Pointers in LOCK File

This function will remove dangling pointers, if they exist, in the lock file. There is no screen display.

Upon exit, the user is returned to the Facility Management Utilities menu.

#### Building File Enter/Edit

Select Facility Management Utilities Option: 4 Building File Enter/Edit Select ENG BUILDING NAME:??

CHOOSE FROM:

1

5

9

24

7A

8-DX

Building identifier. Used for data validation when entries are made in the Space File. Building NAME should consist of either one or two pieces, separated by the hyphen ("-"). The rule is this:

1.  Sites where building designations are unique in and of themselves should have one-piece entries in this file. Building NAMEs should not contain any hyphens.
2.  Sites where building designations are not necessarily unique (multi-division sites and perhaps sites that support remote clinics and/or other quasi-independent offices) should use a two-piece format. The second piece should designate the division, outpatient clinic, Regional Office, etc. Building NAMEs should contain only one hyphen, which will be treated as the delimiter between 'building' and 'division'.

Building NAMEs should be kept as short as possible since they will be printed on each bar-coded LOCATION LABEL. It will be difficult to fit lengthy building NAMEs onto bar code labels.

of standard size. Assuming three-inch width and Code 39 symbology, bar coded LOCATION LABEL's can accommodate about thirteen (13) characters total. In particular, it is suggested that 'division' designations be no more than two or three characters long.

Select ENG BUILDING NAME: 24 NAME: 24//

OWNERSHIP: VAMC//??

Denotes whether or not space is being leased, owned by a VA department, or entered for project planning purposes.

CHOOSE FROM:

| V   | VAMC              |
|-----|-------------------|
| L   | LEASED            |
| P   | PLANNED           |
| VBA | VET BENEFITS ADM  |
| NCS | NAT CEMETARY SERV |

OWNERSHIP: VAMC// V VAMC OWNER:??

The name of the individual, corporation, or government agency that owns the building. Especially important in the case of leased space.

OWNER: VAMC OWNER ADDRESS1:

OWNER ADDRESS2:

OWNER CITY:

OWNER STATE:

OWNER ZIP CODE:

PROPERTY ADDRESS1:??

Pertains to address of the property, PROPERTY ADDRESS1:

PROPERTY ADDRESS2:

PROPERTY CITY:

PROPERTY STATE:

PROPERTY ZIP CODE:

CONTRACT \#:??

Contract under which building is leased.

CONTRACT \#:

LEASE TYPE: ??

Type of leasing agreement. CHOOSE FROM:

C CAPITAL

O OPERATING

OTHER OTHER LEASE TYPE:

LEASE CONTACT PERSON: ??

Name of person (Lessor) to contact for information on this lease, LEASE CONTACT PERSON:

CONTACT PHONE NUMBER: ??

Phone number of lessor contact person CONTACT PHONE NUMBER:

BASE TERM (MONTHS): ??

Term of lease.

BASE TERM (MONTHS):

RENEWAL TERM (MONTHS): ??

Period for which lease may be renewed once the BASE TERM has expired.

RENEWAL TERM (MONTHS):

DATE SIGNED: ??

Date on which current leasing documents were signed. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. DATE SIGNED:

BEGINNING DATE: ??

Starting date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

BEGINNING DATE:

ENDING DATE: ??

Expiration date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. ENDING DATE:

NET USABLE SQUARE FEET: 950//??

Net Usable area in square feet.

NET USABLE SQUARE FEET: 950// GROSS SQUARE FEET: ??

Gross square feet of building.

GROSS SQUARE FEET:

TOTAL RENT (INCLUDE UTILITIES): ??

Annual rent paid for use of this building. Should include all utilities (estimate if necessary).

TOTAL RENT (INCLUDE UTILITIES):

ACTIVATION COSTS: ??

Cost of activating this building for VA use.

Total Dollars received for activation. Future software releases may provide a more detailed breakdown of activation costs.

ACTIVATION COSTS:

SPEC. PURPOSE ALTERATION COST: ??

Cost of making this space usable for a special purpose.

SPEC. PURPOSE ALTERATION COST:

PERSONNEL ASSIGNED: 25//??

Engineering FTEE assigned to work in this building.

PERSONNEL ASSIGNED: 25// ANCILLARY COSTS: ??

Cost of ancillary services, equipment, maintenance contracts, etc.

ANCILLARY COSTS:

FUNDING SOURCE: MEDICAL CENTER//??

Funding source for this lease or project. CHOOSE FROM:

VACO VACO REAL ESTATE VAMC MEDICAL CENTER

REG REGION

OTHER OTHER

FUNDING SOURCE: MEDICAL CENTER// PROJECT NO.: ??

Field used to reference a construction project for which a space plan is being developed.

A space plan (IMFP) can be entered room by room under a proposed real Building Number or a fabricated Building Number. Each Room in the Space file for this project MUST reference this building number for sorting and planning purposes.

CHOOSE FROM:

| 999-011     | BUILD HOSPITAL ANNEX         |
|-------------|------------------------------|
| 999-012     | RENOVATE CLINICAL LABORATORY |
| 999-014     | EXPAND CLINICAL WARDS        |
| 999-016     | NURSING HOME CONSTRUCTION    |
| 999-020     | ROADWAY REPAIR               |
| 999-92-001A | RENOVATE HEMATOLOGY LAB      |
| 999-92-002  | RENOVATE MORGUE              |
| 999-93-005  | REBUILD COMPUTER ROOM        |
| 999-95-002  | ASBESTOS PROJECT             |
| 999-95-013  | RENOVATE HISTOLOGY WARD      |
| 999-95-020  | NURSING HOME RENOVATION      |

PROJECT NO.:

REMARKS:

1\>

Select ENG BUILDING NAME:

Upon exit, the user is returned to the Facility Management Utilities menu.

#### Print All Building Data

This option is designed to print a captioned report of all data for all buildings.

Select Facility Management Utilities Option: 5 Print All Building Data START WITH NAME: FIRST//

DEVICE: ;132 LAN

REPORT OF ALL BUILDING DATA APR 27,1993 14:09 PAGE 1

| NAME: 1                          | OWNER: ATT               |
|----------------------------------|--------------------------|
| OWNER ADDRESS1: 2304 ANYVILLE RD | OWNER CITY: CI TY SPRING |
| OWNER STATE: ANYPLACE            | OWNER ZIP CODE: 20000    |
| OWNERSHIP: LEASED                |                          |

NAME: 9

OWNER ADDRESS1: 2403 ANYVILLE RD OWNER STATE: ANYPLACELEASE TYPE: CAPITAL

RENEWAL TERM (MONTHS): 60 BEGINNING DATE: JAN 1, 1990 OWNER ZIP CODE: 23000

NET USABLE SQUARE FEET: 12000 ACTIVATION COSTS: 15000

PERSONNEL ASSIGNED: 65

OWNER: ATT

OWNER CITY: CI TY SPRING CONTRACT \#: 23000

BASE TERM (MONTHS): 60 DATE SIGNED: DEC 1, 1989

ENDING DATE: DEC 31, 1995 OWNERSHIP: LEASED

TOTAL RENT (INCLUDE UTILITIES): 100000 SPEC. PURPOSE ALTERATION COST: 15000 FUNDING SOURCE: ENREALEST, ONE

### Leased Space Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Leased Space options allow entry of information that is pertinent only to leased space and separate reporting from owned space.

1.  Space Management
2.  Key/Lock Management
3.  Export Facility Management Data
4.  Facility Management Utilities

> ---\> 5 Leased Space Options

6.  Planning Space Program Menu

Select Space/Facility Management Option: 5 Leased Space Options

1.  Enter/Edit All Lease Fields (BUILDING FILE)
2.  Enter/Edit Lease Vendor (BUILDING FILE)
3.  Print Leased Space Survey

#### Enter/Edit All Lease Fields (BUILDING FILE)

Select Leased Space Options Option: 1 Enter/Edit All Lease Fields (BUILDING FILE)

Select ENG BUILDING NAME: 9

OWNERSHIP: LEASED//??

Denotes whether or not space is being leased, owned by a VA department, or entered for project planning purposes.

CHOOSE FROM:

| V   | VAMC              |
|-----|-------------------|
| L   | LEASED            |
| P   | PLANNED           |
| VBA | VET BENEFITS ADM  |
| NCS | NAT CEMETARY SERV |

\*OWNERSHIP: LEASED// OWNER: ATT//??

The name of the individual, corporation, or government agency that owns the building. Especially important in the case of leased space.

OWNER: ATT//

OWNER ADDRESS1: 2403 ANYVILLE RD//??

Street address of the building's owner (line 1).

OWNER ADDRESS1: 2403 ANYVILLE RD// OWNER ADDRESS2: ??

Street address of building's owner (line 2).

OWNER ADDRESS2:

OWNER CITY: CI TY SPRING//??

Pertains to the building's owner.

OWNER CITY: CI TY SPRING//

OWNER STATE: ANYPLACE//??

Pertains to building's owner.

CHOOSE FROM:

ANYPLACE ANYSTAT

OWNER STATE: ANYPLACE// OWNER ZIP CODE: 20000//??

Pertains to building's owner.

OWNER ZIP CODE: 20000// PROPERTY ADDRESS1: ??

Pertains to address of the property, PROPERTY ADDRESS1:

PROPERTY ADDRESS2: ??

Pertains to address of property, PROPERTY ADDRESS2:

PROPERTY CITY: ??

Pertains to address of property, PROPERTY CITY:

PROPERTY STATE: ???

Pertains to State in which property resides CHOOSE FROM:

ANYPLACE ANYSTATE

PROPERTY STATE:

PROPERTY ZIP CODE: ??

Pertains to address of property, PROPERTY ZIP CODE:

CONTRACT \#: 23000//??

Contract under which building is leased.

CONTRACT \#: 23000// LEASE TYPE: CAPITAL//??

Type of leasing agreement. CHOOSE FROM:

| C     | CAPITAL   |
|-------|-----------|
| O     | OPERATING |
| OTHER | OTHER     |

LEASE TYPE: CAPITAL// LEASE CONTACT PERSON: ??

Name of person (Lessor) to contact for information on this lease, LEASE CONTACT PERSON:

CONTACT PHONE NUMBER: ??

Phone number of lessor contact person CONTACT PHONE NUMBER:

LEASE PROPERTY/SITE NAME: ??

Text name of Property/Building. Common name of site to be used as a more descriptive field than the Building Number field.

LEASE PROPERTY/SITE NAME:

BASE TERM (MONTHS): 60//??

Term of lease.

BASE TERM (MONTHS): 60// RENEWAL TERM (MONTHS): 60//??

Period for which lease may be renewed once the BASE TERM has expired.

RENEWAL TERM (MONTHS): 60// DATE SIGNED: DEC 1,1989//??

Date on which current leasing documents were signed. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. DATE SIGNED: DEC 1,1989//

BEGINNING DATE: JAN 1,1990//??

Starting date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. BEGINNING DATE: JAN 1,1990//

ENDING DATE: DEC 31,1995//??

Expiration date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. ENDING DATE: DEC 31,1995//

NET USABLE SQUARE FEET: 12000//??

Net Usable area in square feet.

NET USABLE SQUARE FEET: 12000// GROSS SQUARE FEET: ??

Gross square feet of building.

GROSS SQUARE FEET:

TOTAL RENT (INCLUDE UTILITIES): 100000//??

Annual rent paid for use of this building. Should include all utilities (estimate if necessary).

TOTAL RENT (INCLUDE UTILITIES): 100000// ACTIVATION COSTS: 15000//??

Cost of activating this building for VA use.

Total Dollars received for activation. Future software releases may provide a more detailed breakdown of activation costs.

ACTIVATION COSTS: 15000//

SPEC. PURPOSE ALTERATION COST: 15000//??

Cost of making this space usable for a special purpose.

SPEC. PURPOSE ALTERATION COST: 15000// PERSONNEL ASSIGNED: 65//??

Engineering FTEE assigned to work in this building.

PERSONNEL ASSIGNED: 65// ANCILLARY COSTS:??

Cost of ancillary services, equipment, maintenance contracts, etc.

ANCILLARY COSTS:

\*FUNDING SOURCE: ENREALEST, ONE//??

Funding source for this lease or project. CHOOSE FROM:

ERO ENREALEST, ONE

VAMC MEDICAL CENTER

REG REGION

OTHER OTHER

FUNDING SOURCE: ENREALEST, ONE// PROJECT NO.: ??

Field used to reference a construction project for which a space plan is being developed.

A space plan (IMFP) can be entered room by room under a proposed real Building Number or a fabricated Building Number. Each Room in the Space file for this project MUST reference this building number for sorting and planning purposes.

PROJECT NO.:

\*REMARKS:

1\>??• •• •

Select ENG BUILDING NAME:

\*If ownership is selected as PLANNED, only these fields are presented.

#### Enter/Edit Lease Vendor (BUILDING FILE)

Enter/Edit Lease Vendor stores address information of the leased space provider.

Select Leased Space Options Option: 2 Enter/Edit Lease Vendor (BUILDING FILE) Select ENG BUILDING NAME: ??

CHOOSE FROM:

1

5

9

24

7A

8-DX STUDIO A STUDIO B

Select ENG BUILDING NAME: 1 OWNER: ??

The name of the individual, corporation, or government agency that owns the building. Especially important in the case of leased space.

OWNER: ATT

ADDRESS1: 2304 ANYVILLE RD ADDRESS2:

CITY: CI TY SPRING

STATE: MD

ZIP CODE: 20910

Select ENG BUILDING NAME:

#### Print Leased Space Survey.

A report on leased space may be printed using this option.

Select Leased Space Options Option: 3 Print Leased Space Survey START WITH BUILDING NUMBER: FIRST//

START WITH ROOM NUMBER: FIRST// DEVICE: LAN RIGHT MARGIN: 80//

ENGINEERING SPACE SURVEY OF LEASED ROOMS MAR 31,1993 14:11 PAGE 1

B

ROOM BLDG NET E

NUMBER NO. WING SERVICE KEY FUNCTION (FREE TEXT) S.F. D

FLOOR

CEILING W D

N R 14

WALL

LIGHTING D S -4

OWNERSHIP: LEASED

25-7A 7A EAST CLINICAL LABORA 1111 LAB

TILE

GRID FLUORESCENT 5

---­

PLASTER

SUBTOTAL 0

---­

TOTAL 0

Press \<RETURN\> to continue.

### Planning Space Program Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Space Management
2.  Key/Lock Management
3.  Export Facility Management Data
4.  Facility Management Utilities
5.  Leased Space Options

> ---\>6 Planning Space Program Menu

Select Space/Facility Management Option: 6 Planning Space Program Menu

1.  Building File Enter/Edit
2.  Enter/Edit Room Planning Data
3.  Print Building/Project Space Plan

#### Building File Enter/Edit

Use this option to maintain the Eng Building file (#6928.3). The BUILDING (or BUILDING-DIVISION) portion of the ROOM NUMBER field of entries in the Eng Space file must match an entry in this Eng. Building file.

Limited fields will be presented if the building ownership is listed as PLANNED.

Select Planning Space Program Menu Option: 1 Building File Enter/Edit Select ENG BUILDING NAME: ??

CHOOSE FROM:

1

5

9

24

7A

8-DX

Building identifier. Used for data validation when entries are made in the Space File. Building NAME should consist of either one or two pieces, separated by the hyphen ("-"). The rule is this:

1.  Sites where building designations are unique in and of themselves should have one-piece entries in this file. Building NAMEs should not contain any hyphens.
2.  Sites where building designations are not necessarily unique (multi-division sites and perhaps sites that support remote clinics and/or other quasi-independent offices) should use a two-piece format. The second piece should designate the division, outpatient clinic, Regional Office, etc. Building NAMEs should contain only one hyphen, which will be treated as the delimiter between 'building' and 'division'.

Building NAMEs should be kept as short as possible since they will be printed on each bar-coded LOCATION LABEL. It will be difficult to fit lengthy building NAMEs onto bar code labels.

of standard size. Assuming three-inch width and Code 39 symbology, bar coded LOCATION LABEL's can accommodate about thirteen (13) characters total. In particular, it is suggested that 'division' designations be no more than two or three characters long.

Select ENG BUILDING NAME: 1 NAME: 1//

OWNERSHIP: LEASED//??

Denotes whether or not space is being leased, owned by a VA department, or entered for project planning purposes.

CHOOSE FROM:

V VAMC

| L   | LEASED            |
|-----|-------------------|
| P   | PLANNED           |
| VBA | VET BENEFITS ADM  |
| NCS | NAT CEMETARY SERV |

OWNERSHIP: LEASED// OWNER: ATT//??

The name of the individual, corporation, or government agency that owns the building. Especially important in the case of leased space.

OWNER: ATT//

OWNER ADDRESS1: 2304 ANYVILLE RD//??

Street address of the building's owner (line 1).

OWNER ADDRESS1: 2304 ANYVILLE RD// OWNER ADDRESS2: ??

Street address of building's owner (line 2).

OWNER ADDRESS2:

OWNER CITY: CI TY SPRING//??

Pertains to the building's owner.

OWNER CITY: CI TY SPRING//

OWNER STATE: ANYPLACE//??

Pertains to building's owner.

CHOOSE FROM:

ANYPLACE ANYSTATE

OWNER STATE: ANYPLACE// OWNER ZIP CODE: 20000//??

Pertains to building's owner.

OWNER ZIP CODE: 20000// PROPERTY ADDRESS1: ??

Pertains to address of the property, PROPERTY ADDRESS1:

PROPERTY ADDRESS2: ??

Pertains to address of property, PROPERTY ADDRESS2:

PROPERTY CITY: ??

Pertains to address of property, PROPERTY CITY:

PROPERTY STATE: ??

Pertains to State in which property resides.

CHOOSE FROM:

ANYPLACE ANYSTATE

PROPERTY STATE:

PROPERTY ZIP CODE: ??

Pertains to address of property, PROPERTY ZIP CODE:

CONTRACT \#: ???

Contract under which building is leased.

CONTRACT \#:

LEASE TYPE: ??

Type of leasing agreement. CHOOSE FROM:

C CAPITAL

O OPERATING

OTHER OTHER LEASE TYPE:

LEASE CONTACT PERSON: ??

Name of person (Lessor) to contact for information on this lease, LEASE CONTACT PERSON:

CONTACT PHONE NUMBER: ??

Phone number of lessor contact person CONTACT PHONE NUMBER:

BASE TERM (MONTHS): ??

Term of lease.

BASE TERM (MONTHS):

RENEWAL TERM (MONTHS): ???

Period for which lease may be renewed once the BASE TERM has expired.

RENEWAL TERM (MONTHS):

DATE SIGNED: ??

Date on which current leasing documents were signed. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. DATE SIGNED:

BEGINNING DATE: ??

Starting date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. BEGINNING DATE:

ENDING DATE: ??

Expiration date of current lease. Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc. T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR. ENDING DATE:

NET USABLE SQUARE FEET: ??

Net Usable area in square feet.

NET USABLE SQUARE FEET:

GROSS SQUARE FEET: ??

Gross square feet of building.

GROSS SQUARE FEET:

TOTAL RENT (INCLUDE UTILITIES): ??

Annual rent paid for use of this building. Should include all utilities (estimate if necessary).

TOTAL RENT (INCLUDE UTILITIES):

ACTIVATION COSTS: ??

Cost of activating this building for VA use.

Total Dollars received for activation. Future software releases may provide a more detailed breakdown of activation costs.

ACTIVATION COSTS:

SPEC. PURPOSE ALTERATION COST: ??

Cost of making this space usable for a special purpose.

SPEC. PURPOSE ALTERATION COST:

PERSONNEL ASSIGNED: ??

Engineering FTEE assigned to work in this building.

PERSONNEL ASSIGNED:

ANCILLARY COSTS: ??

Cost of ancillary services, equipment, maintenance contracts, etc.

ANCILLARY COSTS:

FUNDING SOURCE: ??

Funding source for this lease or project. CHOOSE FROM:

ERO ENREALEST, ONE

VAMC MEDICAL CENTER

REG REGION

OTHER OTHER FUNDING SOURCE:

PROJECT NO.: ??

Field used to reference a construction project for which a space plan is being developed.

A space plan (IMFP) can be entered room by room under a proposed real Building Number or a fabricated Building Number. Each Room in the Space file for this project MUST reference this building number for sorting and planning purposes.

PROJECT NO.:

REMARKS:

1\>

Select ENG BUILDING NAME: 25•

ARE YOU ADDING '25' AS A NEW ENG BUILDING (THE 17TH)? N (NO)•??

Select ENG BUILDING NAME: 24 NAME: 24//

OWNERSHIP: VAMC// OWNER: VAMC// OWNER ADDRESS1: OWNER ADDRESS2: OWNER CITY:

OWNER STATE:

OWNER ZIP CODE:

PROPERTY ADDRESS1: PROPERTY ADDRESS2: PROPERTY CITY:

PROPERTY STATE:

PROPERTY ZIP CODE: CONTRACT \#:

LEASE TYPE:

LEASE CONTACT PERSON:

CONTACT PHONE NUMBER:

BASE TERM (MONTHS): RENEWAL TERM (MONTHS):

DATE SIGNED:

BEGINNING DATE:

ENDING DATE:

NET USABLE SQUARE FEET: 950// GROSS SQUARE FEET:

TOTAL RENT (INCLUDE UTILITIES): ACTIVATION COSTS:

SPEC. PURPOSE ALTERATION COST: PERSONNEL ASSIGNED: 25// ANCILLARY COSTS:

FUNDING SOURCE: MEDICAL CENTER// PROJECT NO.:

REMARKS:

1\>

#### Enter/Edit Room Planning Data

This option is used to edit only those fields related to space planning criteria.

Select Planning Space Program Menu Option: 2 Enter/Edit Room Planning Data Enter Planning Data for this Room Number

Select ENG SPACE ROOM NUMBER:??

CHOOSE FROM:

25-7A 7A EAST CLINICAL LABORATORY LAB DNG DINING ROOM

Enter as 'ROOM-BUILDING'; or 'ROOM-BUILDING-DIVISION' at two-division facilities and other sites where building numbers may be duplicated. The Building File (6928.3) is used for data validation.

Identifier of a physical location (room). With the advent of bar coding, it is essential that this field uniquely and unambiguously specify a particular location. Entries may consist of one, two, or three pieces.

Hyphens (if present) are treated as delimiters between pieces. First piece (always present) is room designation, second piece (optional) is building designation, and third piece (optional) is division designation (may be used for outpatient clinics, regional offices, etc. as well as for formal divisions).

It is anticipated that most sites will use two-piece entries. True single-building facilities may use one-piece entries. Multi-division facilities and sites supporting remote offices where duplicate building numbers may be a problem should use three-piece entries.

Entry of a two-piece ROOM NUMBER will automatically populate the BUILDING field. Entry of a three-piece ROOM NUMBER will automatically populate the BUILDING and DIVISION fields.

Hyphens must not be used as anything other than delimiters between ROOM, BUILDING, and DIVISION.

Select ENG SPACE ROOM NUMBER: 25-7A 7A EAST CLINICAL LABORATORY LAB

ROOM NUMBER: 25-7A//

SERVICE: CLINICAL LABORATORY//??

CHOOSE FROM:

CLINICAL LABORATORY ENGINEERING SVC

IRM

SERVICE: CLINICAL LABORATORY// FUNCTION: LAB//??

This field points to function file for selection of rooms primary use.

CHOOSE FROM:

ADMINISTRATIVE ASSISTANT AGENT CASHIER

X-RAY CONTROL ROOM X-RAY ROOM

FUNCTION: LAB// NET SQ.FT.:??

Actual Net Square foot for this room. May be compared to Criteria if Criteria (IMFP) has been calculated and entered.

NET SQ.FT.:

SPACE GUIDE:??

Net Square feet for this room/function as per IMFP space criteria SPACE GUIDE:

H-08-9 CRITERIA:??

Criteria Chapter from H-08-9 Space Planning Criteria. Especially important when entering a project space plan (IMFP).

CHOOSE FROM:

A & MM ADMINISTRATION 284

A & MM SUPPLY, PROCESSING AND 285

VOCATIONAL REHABILITATION AND 828

VOLUNTARY SERVICE 290

H-08-9 CRITERIA:

SPECIAL CHARACTERISTICS:?? SPECIAL CHARACTERISTICS: COMMENTS:

1\>? • •

Select ENG SPACE ROOM NUMBER:

#### Print Building/Project Space Plan

This option prints planning data based on building and criteria chapter. The report is sorted by PROJECT NUMBER.

Report will be segregated by PROJECT NUMBER in the Building File.

START WITH PROJECT NO.: FIRST//

START WITH BUILDING FILE POINTER: FIRST// START WITH H-08-9 CRITERIA: FIRST//

DEVICE: LAN RIGHT MARGIN: 80//

SPACE PLANNING PRINTOUT MAY 3,1993 15:58 PAGE 1 NET SPACE

ROOM NUMBER SERVICE FUNCTION SQ.FT. GUIDE

PROJECT NO.999-011

BUILDING FILE POINTER: 7A

H-08-9 CRITERIA: DAY HOSPITAL

| 25-7A    | CLINICAL LABORATORY | LAB              | 1000   | 1200   |
|----------|---------------------|------------------|--------|--------|
| 30-7A    | CLINICAL LABORATORY | STORAGE, GENERAL | 160    | 100    |
|          |                     |                  |        |        |
| SUBTOTAL |                     |                  | 1160   | 1300   |
| SUBCOUNT |                     |                  | 2      | 2      |
| SUBMEAN  |                     |                  | 580.00 | 650.00 |
|          |                     |                  |        |        |
| TOTAL    |                     |                  | 1160   | 1300   |
| COUNT    |                     |                  | 2      | 2      |
| MEAN     |                     |                  | 580.00 | 650.00 |

Press \<RETURN\> to continue

## Report of Accident

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 2162 Report of Accident option employs a package called the Screen Handler, which allows screen formatting of file records. The entry is "painted" on the screen, allowing many fields to be viewed simultaneously.

AUTOMATED ENGINEERING MANAGEMENT SYSTEM VERSION 7.0

WO Work Order & MERS PLAN Project Planning

TRK Project Tracking

EQ Equipment Management

ENM Program Management

SP Space/Facility Management

FSA 2162 Report of Accident

XFER Assign (Transfer) Electronic Work Orders

Select Engineering Main Menu Option: FSA 2162 Report of Accident The options for 2162 Accident Reporting are:

ENGINEERING ACCIDENT REPORTING MODULE

1.  Enter 2162 Report
2.  Display 2162 Report
3.  Edit 2162 Report
4.  Service/Division Summary Report
5.  Injury Cause Summary Report
6.  Accident Nature Summary Report
7.  Specific Location Summary Report

Any one of the options can be selected by typing the appropriate number or by typing the first few alpha characters of the menu name and then pressing \< RET\> or

\<ENTER \>. The main menu may be returned to by pressing \< ENTER \> or \<RET\>.

The Enter, Edit, and Display options use the Engineering Screen Handler. Please refer to the Introduction section of this manual for some helpful tips on using the Engineering Screen Handler.

### Enter 2162 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using this option, you can enter 2162 accident data, in nearly an identical sequence to the paper form VA 2162 (Nov 1983). There are three additions which are not part of the standard form. Two questions are, "Did the injury involve a needle stick?" and "Is the report complete?" The third difference is that the computer automatically generates a local Engineering number as the first data entry for each record. The first two digits are the fiscal year while the last four digits are sequentially incremented throughout the year.

It is strongly recommended that this number not be edited. While the traditional 2162 CASE NUMBER could have been used as the first data entry for each record, experience has shown that reports of accidents are sometimes filed for events that are officially non-reportable, hence the need for a local numbering field.

Report of Accident (screen 1 of 5) 04/01/93

1.  LOCAL ENGINEERING \#(R):930002
2.  CASE NUMBER:....

3 REPORT TYPE: ............

4 RESULT: ................. 5 ACCIDENT CLASS: .............

6 OCCURRENCE DATE: ................. 7 OCCURRENCE TIME:....

8 SITE: ...............................

9 SPECIFIC LOCATION: .........................

10 TORT CLAIM: ................

If \<??\> is entered for help messages, an opportunity is given to repaint the screen. It is recommended that the screen be repainted if the help message is more than a few lines long. Otherwise the cursor may appear to be in another field.

2 ANSWER MUST BE 4 DIGITS IN LENGTH

3 REPORT TYPE: .................................................................

.................................................................

4 RESULT

CHOOSE FROM: ..........................................

.................................................................

CHOOSE FROM:

"I" FOR INITIAL .................................................................

................................................................ "P" FOR PROPERTY ONLY

"S" FOR SUPPLEMENTAL .................................................................

"I" ............................................................

FOR ILLNESS OR INJURY

"C" FOR CORRECTED .................................................................

................................................................... "B" FOR BOTH

5 ACCIDENT CLASS .................................................................

................................................................ 7

OCCURRENCE TIME:

CHOOSE FROM: ..........................................

.................................................................

ENTER MILITARY TIME (0000-2400

"A" FOR MOTOR VEHICLE .................................................................

HRS.)

"B" FOR LABORATORY .................................................................................

"C" FOR OFFICE .................................................................................

.................................................................................

| "G" | FOR ASSEMBLY .............................................................. |                                                                     |
|-----|-----------------------------------------------------------------------------|---------------------------------------------------------------------|
| "J" | FOR PATIENT CARE .......................................................... |                                                                     |
| "L" | FOR STORAGE                                                                 |                                                                     |
| "M" | FOR GROUNDS                                                                 |                                                                     |
| "N" | FOR DIETETICS                                                               |                                                                     |
| "Z" | FOR OTHER                                                                   |                                                                     |
| 8   | SITE                                                                        | ................................................................... |
|     |                                                                             | ................................................................... |

CHOOSE FROM: ...............................................................

................................................................... "A" FOR ON REPORTING ACTIVITY PROPERTY

"B" FOR OFF REPORTING ACTIVITY PROPERTY

9.  SPECIFIC LOCATION

ANSWER MUST BE 4-25 CHARACTERS IN LENGTH

10. TORT CLAIM CHOOSE FROM:

"Y" FOR YES, IS POSSIBLE

"N" FOR NO, NOT POSSIBLE .........................................................

...................................................................

Report of Accident (screen 2 of 5) 04/01/93

\*\*\*LOCAL ENGINEERING \#:930002\*\*\*

1 LAST NAME OF INVOLVED: ................ 2 FIRST/MIDDLE INITIALS:.. 3 SSN: ............ 4 SEX: ......

5 PERSONNEL STATUS: ............. 6 AGE: ..........

7 PAY PLAN:.. 8 OCCUPATIONAL CODE:..... 9 GRADE:..

10 HOME ADDRESS (W):.....

11 HOME PHONE \#: ............ 12 WORK PHONE \#: .................

5 SELECT CODE, N.E.C. MEANS NOT ELSEWHERE CLASSIFIED CHOOSE FROM:

1.  FOR EMPLOYEE
2.  FOR VOLUNTEER
3.  FOR CONTRACTOR
4.  FOR INPATIENT
5.  FOR OUTPATIENT
6.  FOR STUDENT
7.  FOR VISITOR

> Z FOR PERSON N.E.C.

7.  ANSWER MUST BE 2 CHARACTERS IN LENGTH, (e.g. GS, WG, WS, etc.)
8.  OCCUPATIONAL CODE

ANSWER MUST BE 5 DIGITS IN LENGTH (E.G. 00858)

Report of Accident (screen 3 of 5) 04/01/93

\*\*\*LOCAL ENGINEERING \#:930002\*\*\*

1 CA1/CA2:.... 2 TIME ON DUTY:.. 3 DUTY STATUS: ......................

4 ACCIDENT ACTIVITY: ..............................

5 SERVICE/DIVISION \#:....

6 SEVERITY OF INJURY: ...................... 7 CULMINATION: ..................

8 RESTRICTED WORKDAYS:.... 9 LOST WORKDAYS:....

10 INJURY/ILLNESS NATURE: ........................................

11 BODY PART AFFECTED: ...................

12 CAUSE OF INJURY: ...........................

13 NEEDLE STICK?:................................

1 CA1/CA2 ...............................................................

......................................................................................

2 TIME ON DUTY

CHOOSE FROM: ...............................................................

........................ ENTER NEAREST NUMBER OF WHOLE HOURS ON DUTY

"Y" FOR YES "N" FOR NO

3 DUTY STATUS ......................................................................................

......................................................................................

CHOOSE FROM: ...............................................................

| "A" | FOR FULL TIME EMPL ON DUTY ................................................ |
|-----|-----------------------------------------------------------------------------|
| "B" | FOR TEMP EMPL ON DUTY                                                       |
| "C" | FOR PART TIME EMPL ON DUTY                                                  |
| "D" | FOR NON-PAID EMPL ON DUTY                                                   |
| "Z" | FOR STATUS N.E.C.                                                           |

4.  ACCIDENT ACTIVITY

SELECT MOST APPROPRIATE ACTIVITY CHOOSE FROM:

AA-ADMINISTRATION...................................................................

....................................................................................

GA-MATERIAL HANDLING/STORAGE

BA-CONSTRUCTION .............................................................

....................................................................................

HA-TRAINING

CA-MAINTENANCE & REPAIR.............................................................

.................................................... IA-RECREATIONAL

DA-PATIENT CARE .............................................................

....................................................................................

JA-LABORATORY & RESEARCH

EA-FOOD SERVICE .............................................................

....................................................................................

KA-MOTOR VEHICLES/TRANS.

FA-CLEANING & BLDG MANAGEMENT.......................................................

ZA-ACTIVITY/OPERATION N.E.C.

5.  SERVICE/DIVISION \# CHOOSE FROM

9999 N.E.C.

0000 DIRECTOR (VAMC)

0160 DENTAL

0181 HOSPITAL BASED HOME CARE

6.  SEVERITY OF INJURY CHOOSE FROM:

"1" FOR NO TREATMENT REQUIRED "2" FOR FIRST AID ONLY

"3" FOR MEDICAL TREATMENT ONLY "4" FOR DIAGNOSIS OF ILLNESS "5" FOR DISABLING

"8" FOR FATALITY

7.  CULMINATION CHOOSE FROM:

"1" FOR NO RESTRICTION "2" FOR RESTRICTED

"4" FOR PERMANENT TRANSFER "5" FOR TERMINATED

10. INJURY CHOOSE FROM:

AB-AMPUTATION ..............................................................

FA-OCCUPATIONAL SKIN DISEASE

AF-BURN ..............................................................

GA-DUST DISEASE OF LUNGS

BA-LACERATION/ABRASION/PUNCTURE ....................................................

HA-RESP. COND. FROM TOXIC AGEN

BI-CONTUSION/BRUISE ..............................................................

IA-POISONING/TOXIC AG. SYSTEMI

DC-FRACTURE/BRUISE ..............................................................

JA-DISORDERS FROM PHYS.AGENTS

DE-SPRAIN/STRAIN ..............................................................

KA-DISORDER FROM REPEAT TRAUMA

EW-INJURY N.E.C. ..............................................................

LZ-ILLNESS N.E.C.

10. BODY PART AFFECTED CHOOSE FROM:

"01" FOR HEAD

"16" FOR CHEST OR ABDOMEN "45" FOR BACK

"46" FOR SHOULDER/ARM/HAND

"61" FOR HIP/LEG/FOOT

11. CAUSE OF INJURY CHOOSE FROM:

"A" FOR STRUCK AGAINST "B" FOR STRUCK BY

"D" FOR SLIP/TRIP/FALL

"F" FOR CAUGHT IN/UNDER OR BETWEEN "I" FOR ILLNESS

"J" FOR OVER EXERTION "K" FOR ELECTRIC CURRENT

"L" FOR EXTREME TEMPERATURE "M" FOR CHEMICALS

"O" FOR RADIATION "T" FOR ASSAULT

"X" FOR CAUSE N.E.C.

12. NEEDLESTICK

'Y' FOR YES INJURY INVOLVED NEEDLE

'N' FOR NO INJURY DID NOT INVOLVE NEEDLE

Report of Accident (screen 4 of 5) 04/01/93

\*\*\*LOCAL ENGINEERING \#:930002\*\*\*

1 PROPERTY OWNERSHIP: ....................... 2 AMOUNT OF DAMAGE: ..........

3 PROPERTY DAMAGED: .................. 4 YEAR MANUFACTURED:..

5 WEATHER FACTOR: ....................

6 SOURCE OF ACCIDENT: ....................................

7 CAUSE OF ACCIDENT: ........................

8 ADDITIONAL CAUSE: ........................

9 FIRE-FORM OF IGNITION: .................................

10 FIRE..MATERIAL BURNED: .............. 11 FIRE..MATERIAL FORM: .........

12 BEST PREVENTATIVE: .................................

13 CORRECTIVE ACTION: ......................

1 PROPERTY OWNERSHIP ...........................................................

|              | 2                    | AMOUNT OF DAMAGE                     |
|--------------|----------------------|--------------------------------------|
| CHOOSE FROM: |                      | TYPE AN AMOUNT BETWEEN 0 AND 9999999 |
| DOLLARS,     |                      | "A"VETERAN’S ADMINISTRATION          |
| "C"          | OTHER FEDERAL AGENCY |                                      |
| "H"          | PRIVATE              |                                      |
| "L"          | OWNERSHIP N.E.C.     |                                      |

3 PROPERTY DAMAGED

CHOOSE FROM:

"AA" FOR MOTOR VEHICLE ............................................................

"IA" .................................................. FOR FURNITURE

"AG" FOR OTHER VEHICLE ............................................................

"JA" .................................................... FOR RECORDS

"EA" FOR BLDG. STRUCTURE ..........................................................

"KA"............................................. FOR TREES/GRASS/PLANTS

"FA" FOR EQUIPMENT ................................................................

............................................................... "BA"

FOR BEDDING/CLOTHES

"GA" FOR SUPPLIES .................................................................

............................................................... "CA" FOR INTERIOR FINISH

...................................................................

................................................................... "HA" FOR TRASH/RUBBISH

...................................................................

................................................................... "ZA" FOR PROPERTY N.E.C.

5.  WEATHER FACTOR CHOOSE FROM:

"A" FOR SNOW/ICE .................................................................

................................................................ "F" FOR HUMIDITY

"B" FOR DUST/STORM ...............................................................

"H" ......................................................... FOR FOG

"C" FOR LIGHTENING ...............................................................

"J" ........................................................ FOR RAIN

"D" FOR HIGH TEMPERATURE .........................................................

"N" FOR WINDSTORM

"E" FOR LOW TEMPERATURE ..........................................................

"P" FOR WEATHER N.E.C.

...................................................................

................................................................... "Z" FOR WEATHER NOT A FACTOR

6.  SOURCE OF ACCIDENT CHOOSE FROM:

"01AA" FOR UNPOWERED EQUIPMENT/FURNISHINGS/SUPPLIES "11AA" FOR POWERED EQUIP/APPLIANCES/SUPPLIES

"33AA" FOR BLDG. MATERIAL, FURNITURE OR CONDITION "44AA" FOR TOXIC SUBSTANCE/RADIATION EXPOSURE "77AA" FOR VEHICLE

"81AA" FOR PERSON

"82ZZ" FOR SOURCE N.E.C.

7 CAUSE OF ACCIDENT .....................................................................................

8 ................................................. ADDITIONAL CAUSES

CHOOSE FROM: ..............................................................

....................................................... CHOOSE FROM:

"AA" FOR EQUIPMENT OR ENVIRONMENT .................................................

"AA" FOR EQUIPMENT OR ENVIRONMENT

"BA" FOR PERSON .....................................................................................

............................................................... "BA"

FOR PERSON

"CA" FOR NATURE .....................................................................................

............................................................... "CA"

FOR NATURE

"FA" FOR CAUSE UNKNOWN ............................................................

"ZZ" ........................................ FOR NO ADDITIONAL CAUSE

.....................................................................................

.....................................................................................

9 FIRE FORM OF IGNITION .....................................................................................

10 FIRE MATERIAL BURNED

LEAVE BLANK IF FIRE NOT INVOLVED.....................................................

CHOOSE FROM:

CHOOSE FROM: ..............................................................

............................................................... "11"

FOR GAS

"21" FOR ELECTRIC ARC .............................................................

"21" ..................................................... FOR LIQUID "31" FOR SMOKING MATERIAL(CIGARETTES, ETC)"31" ............................ FOR SOLID "61" FOR SOURCE N.E.C. ............................................................

"41" ............................................... FOR LIQUID & GAS

"71" FOR SOURCE UNKNOWN .............................................................

"71".................................................... FOR SOLID & GAS

.....................................................................................

................................................................... "81" FOR SOLID & LIQUID

11. FIRE MATERIAL FORM

ENTER "GZ" FOR ALL FIRES, OTHERWISE LEAVE BLANK CHOOSE FROM:

"GZ" FOR ALL FIRES

12. BEST PREVENTATIVE

CHOOSE FROM:

"A" FOR TRAINING .................................................................

................................................................ "F" FOR IMPROVED WRITTEN PROCEDURES

"B" FOR MORE STAFF ...............................................................

"G" ........................... FOR MORE FUNDS FOR HAZARD ELIMINATION "C" FOR MOTIVATION ...............................................................

"H" .......................................... FOR PERSONNEL ACTION

"D" FOR BETTER EQUIP/MATERIAL ....................................................

"I" FOR PREVENTATIVE N.E.C.

"E" FOR BETTER PLANNING & COORD ..................................................

"Z" FOR NONE

13. CORRECTIVE ACTION

CHOOSE FROM:

"A" FOR TAKEN

"B" FOR REQUIRED & ANTICIPATED "C" FOR REQUESTED

"D" FOR NONE

Report of Accident (screen 5 of 5) 04/01/93

\*\*\*LOCAL ENGINEERING \#:930002\*\*\*

1 ACCIDENT NARRATIVE (W):.....

2 WITNESSES: .................................................................

3 CORRECTIVE NARRATION (W):.....

4 INITIATOR NAME: .................... 6 DATE SIGNED(IN): ............

5 TITLE(IN): .................... 7 PHONE \#(IN): ............

8 REVIEW AUTHORITY NAME: .................... 10 DATE SIGNED(RA): ............

9 TITLE(RA): .................... 11 PHONE \#(RA): ............

12 EVALUATION OF REPORT (W):.....

13 REPORT STATUS: ............................

1 ACCIDENT NARRATIVE:

1\> THIS WORD PROCESSING FIELD SHOULD BE USED

2\> TO GIVE A DESCRIPTION OF THE ACCIDENT.

13 REPORT STATUS CHOOSE FROM:

"Y" FOR YES, 2162 REPORT COMPLETED "N" FOR NO, 2162 REPORT NOT COMPLETED

### Display 2162 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display 2162 Report uses the Screen Handler in a display only mode to allow data review of a specific report. Each report is cross-referenced by CASE NUMBER, LAST NAME OF INVOLVED, and SSN. They may be looked up by any of those values.

The screen display is the same as the Enter 2162 Report screen. However, data in word processing fields does not display.

### Edit 2162 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Nearly identical in function to the Enter 2162 Report, the Edit option first requests the local Engineering Report \#. The report file is cross-referenced by CASE NUMBER, LAST NAME OF INVOLVED, and SSN. The report may be looked-up by any of these values.

Previous entries for the report will be shown and can be edited. You can access each field in turn using the \< RET\> key or a specific field by entering \< ^\> and the field number. The text in a word processing field will be displayed at the bottom of the screen.

Screens 1 and 5 are shown below as examples.

REPORT OF ACCIDENT (SCREEN 1 OF 5)

1 LOCAL ENGINEERING \#(R):860001 ................................................ 2 CAS

3 REPORT TYPE: INITIAL ..........................................................

5 ACCIDENT CLASS: PATIENT CARE .................................................. 6

7 OCCURRENCE TIME:1333 .........................................................

9 SPECIFIC LOCATION: B2-2 CCU ................................................... 10

...................................................................

...................................................................

...................................................................

REPORT OF ACCIDENT (SCREEN 5 OF 5)

1 ACCIDENT NARRATIVE(W): .................................................... 2

3 CORRECTIVE NARRATION: ..................................................... 4

5 TITLE: NURSE ...............................................................

7 PHONE \#:1111 ..............................................................

9 TITLE: SERVICE CHIEF .......................................................

11 PHONE \#:3333 .............................................................

13 REPORT STATUS: YES, 2162 REPORT COMPLETED

ACCIDENT NARRATIVE:

1\>THIS IS A NARRATIVE OF THE ACCIDENT

2\>HERE IS THE SECOND LINE OF TEXT

EDIT OPTION: .................................................................

...................................................................

### Summary Reports (options 5-8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently there are four summary reports. Each of these reports is identical in format, differing only in record selection criteria. In each case, one or all of the criteria elements may be selected (e.g., a single service or all services). Within that selection the time frames MONTHLY, QUARTERLY, or YEARLY may be specified, as well as the option of selecting every record on file.

The following is an example of a summary report generated for a particular service, \#0018, for a given quarter. The report heading is slightly modified, in order to fit on the page.

ENGINEERING ACCIDENT REPORTING MODULE

1.  Enter 2162 Report
2.  Display 2162 Report
3.  Edit 2162 Report
4.  Service/Division Summary Report
5.  Injury Cause Summary Report
6.  Accident Nature Summary Report
7.  Specific Location Summary Report

Select 2l62 Report of Accident Option: Service/Division Summary Report

MONTHLY QUARTERLY YEARLY

ACCIDENT REPORT INTERVAL

................................................................ 1.

................................................................ 2.

................................................................ 3.

................................................................ 4.

ALL REPORTS

SELECT ACCIDENT REPORT INTERVAL: EXIT//

If Select ACCIDENT REPORT INTERVAL is answered with a \< RET\>, the following message appears after which the user is returned to the above menu.

USER ABORT

\<cr\> to continue.

If an interval is selected, the following dialogue precedes the display.

SELECT OPTIONS: EXIT// 2 QUARTERLY SELECT FISCAL YEAR: 86//

SELECT QUARTER: 2//

DO YOU WANT ALL SERVICES LISTED? (Y/N)? NO// (NO)

Select FSA-DIVISION/SERVICE DIV./SERVICE \#: 0118 ENGINEERING

DEVICE: HOME// 3 ENGINEERING RIGHT MARGIN: 132//

one moment please

ACCIDENT REPORT SUMMARY:0118 SERVICE

FROM: JAN 1, 1986 TO:MAR 31, 1986 SEP 9,1986 PAGE 1 LOCAL

\# OCCURRENCE ................................................................ LAST NA

INJURY/ILLNESS ....................................................................

.....................................................................................

SERVICE/DIVISION \#:0118 .............................................................

86001 MAR 21, 1986 ................................................................. DEMETRA

DE-SPRAIN/STRAIN ....................................................................

86002 MAR 21, 1986 ................................................................. DUDLEY

BA-LACERATION........................................................................

Supplementary Notes:

The coding criteria used has been taken from the leaflet, "CODING INSTRUCTIONS (VA FORM 2162, REPORT OF ACCIDENT)", and therefore should be directly applicable. The pointer file, DIVISION/SERVICE number, is extracted from MP-3, Part III, Appendix 3C. This file contains the list of acceptable codes and should not be altered.

## Assign (Transfer) Electronic Work Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Assign Electronic Work Orders menu option (ENETRANSFER) is used for transferring requests from a receiving area to a working shop. This option displays summary information (including TASK DESCRIPTION, PRIORITY, REQUEST DATE, and REQUESTER) for each work order that is awaiting transfer. If the work request involves a piece of equipment, the EQUIPMENT ID# and EQUIPMENT CATEGORY is also displayed. There is a notation as to whether or not the Electronic Work Order contains COMMENTS from the requester. The header of this summary display tells how many requests are pending. You can assign one particular Electronic Work Order, or a group of them. You can also disapprove electronic work orders when necessary.

If only one receiving area is needed at your facility, it should be entered into the Engineering Section file and then into the TEMPORARY WORK ORDER SECTION field of the Eng Init Parameters file. If two or more receiving areas are needed, they should all be entered into the Engineering Section file, but the TEMPORARY WORK ORDER SECTION should be left blank. The SECTION NUMBER of all receiving areas should be in the range of 90 to 99 (inclusive).

AUTOMATED ENGINEERING MANAGEMENT SYSTEM VERSION 7.0

WO Work Order & MERS PLAN Project Planning TRK Project Tracking

EQ Equipment Management ENM Program Management SP Space Management FSA 2162 Report of Accident

XFER Assign (Transfer) Electronic Work Orders

Select Engineering Main Menu Option: XFER Assign (Transfer) Electronic Work Orders Req Date Location Equip ID Priority Cmnts

Task Description Contact Person Entered by

| 1 =\> RA930407-001                  | MAR 17,1993 | 10  | 4                       | AVERAGE        | YES |
|-------------------------------------|-------------|-----|-------------------------|----------------|-----|
| Routine maintenance Coulter Counter |             |     | ENUSER2, SEVEN          | ENUSER5, ONE   |     |
| Name: COULTER COUNTER               |             |     | Cat: COUNTER-BLOOD CELL |                |     |
| 2 =\> RA930408-001                  | APR 8,1993  | 10  | 3                       | AVERAGE        | YES |
| REMOVE OLD ANALYZER                 |             |     | ENUSER3, SEVEN          | ENUSER3, SEVEN |     |
| Name: ICE MAKER                     |             |     | Cat:                    |                |     |

TRANSFER NUMBERS? (Separate with ;) (Use : for Range)('ALL' for all 2) WORK ORDER \# RA930407-001

1)  PRIMARY EMPL: ENUSER2 , SEVEN 2) REQ DATE: MAR 17,1993

3\) REQ MODE: PHONE 4) LOCATION: 25-7A

5\) BED \#: 6) STATUS: WAITING ON PARTS

7)  TASK DESC: Routine maintenance Coulter Counter
8)  CONTACT: ENUSER2, SEVEN 9) PHONE: 5554273728

10\) ENTERED BY: ENUSER3 , SEVEN 11) SHOP: RECEIVING AREA

12\) DATE ASSIGNED: 03/17/93 13) PRIORITY: AVERAGE

14\) EQUIP ID#: 4 15) LOCAL ID:

16) EQUIP CAT: COUNTER-BLOOD CELL
17) MFGR: NATIONAL INSTRUMENT
18) MODEL: N320A 19) SERIAL \#: AE02847L29

20\) OWNER/DEPT: CLINICAL LABORATORY 21) PM \#: PM00000025 22) PARTS ORDER: 999-93-2-044-0001 23) WORK ACTION: P2

24) WORK CTR: 55510/CLINICAL LAB EQUIP, PREV MAINT
25) TOTAL HOURS: 26) TOTAL MATERIAL COST:

27\) TOTAL LABOR COST: 28) VENDOR SERVICE COST:

29\) \*ASSIGNED TECH\* 30) DATE COMPLETE: \#1: ENUSER2, SEVEN HRS: SHOP: BIOMEDICAL

31) WORK PERFORMED: SOME WORK
32) COMMENTS: (Press \<RETURN\> to continue...)

WARRANTY EXPIRATION: \*\*07/31/96\*\* (Original Work Order: B930317-001)

Ready to transfer RA930407-001 Routine maintenance Coulter Counter Transfer to shop ('^'to EXIT, '^D' to DISAPPROVE): BIOMEDICAL 4

Edit this work order? YES// N (NO)•

Pending Elect Work Orders (1 in RECEIVING AREA) APR 21,1993@15:41 Pg 1 Work Order \# Req Date Location Equip ID Priority Cmnts Task Description Contact Person Entered by

| 2 =\> RA930408-001  | APR 8,1993 | 10  | 3              | AVERAGE        | YES |
|---------------------|------------|-----|----------------|----------------|-----|
| REMOVE OLD ANALYZER |            |     | ENUSER3, SEVEN | ENUSER3, SEVEN |     |
| Name: ICE MAKER     |            |     | Cat:           |                |     |

TRANSFER NUMBERS? (Separate with ;) (Use : for Range)('ALL' for all 1) ('^' to EXIT)(RETURN to Continue)

## IT Equipment Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of the options in the IT Equipment Module have been documented in previous sections of this manual. In those cases, the page references are noted, and a brief description of the features is provided below. All other options are documented in this chapter.

1.  Inventory Edit (IT)
2.  Display Equipment Record (See page 7-19)
3.  Bar Code Features (NX Equipment) ... (See page 7-102)
4.  Specific Equipment History (See page 7-21)
5.  Display/Edit Room Data (See page 9-6)
6.  Non-Space File Location Report
7.  IT Equipment Responsibility...

Inventory Edit (IT)

This option allows you to edit the record for an existing piece of equipment. Only equipment that has a CMR with IT TRACKING set to YES may be selected.

Display Equipment Record

Display selected fields from the EQUIPMENT INV. file. Repair history is not displayed via this option.

Bar Code Features (NX Equipment)

Collection of options designed for use in bar coding nonexpendable equipment and in using bar code to maintain CMR inventories.

Equipment Labels

Prints bar coded equipment labels. Cohorts of labels (ex: labels by CMR, labels by Equipment Category, etc.) will be sorted by LOCATION unless the user specifies otherwise.

Location Labels

Driver option to print bar coded location labels.

Download NX Program to Portable Bar Code Reader

Downloads an IRL (Interactive Reader Language) program to a portable bar code reader.

Upload Data from Portable Bar Code Reader

Calls a routine that causes a portable bar code reader to upload its data to VISTA.

Restart Processing of Uploaded NX Inventory Data

Used to resume processing of NX inventory that has been uploaded from a portable bar code reader. User will need PROCESS ID and TIME STAMP from failed process. If this information is unavailable, data upload must be re- started from the beginning.

Inventory Exception Listing

Produces a list of those items on a specified CMR that have not been located in the course of a physical inventory.

Specific Equipment History

Print-out of repair history of a specific entry in Equipment Inv. file.

Display/Edit Room Data

This option shows a room entry with all its associated data on the screen at one time. All fields will be displayed and can be viewed, edited, or printed on another device.

Non-Space File Location Report

This report generates a list of equipment that has an entry in the NON-SPACE FILE LOCATION field. Equipment should only have a value in this field when the LOCATION field cannot be updated because an appropriate location is not available in the ENG SPACE file. Ideally, equipment will not remain on this report for an extended period of time.

IT Equipment Responsibility...

This is the menu for the equipment responsibility options.

### Inventory Edit (IT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to edit the record for an existing piece of equipment. Only equipment that has a CMR with IT TRACKING set to YES may be selected.

This option is locked with the EN IT INVENTORY security key.

Following is a list of the fields displayed on the Inventory Edit (IT) screen with a brief description.

LOCATION - The physical location of the equipment. Only entries from the ENG SPACE file (#6928) may be entered. You may enter a ?? for a list. If you don’t find an appropriate location, you may enter a free-text location in the NON-SPACE FILE LOCATION field. See that field’s description for more information.

NON-SPACE FILE LOCATION - The purpose of this field is to allow you to enter a free-text value when there is not a suitable location in the ENG SPACE (#6928) file to select. The entry of a free-text location will result in Engineering staff automatically being notified via e-mail of the need for a new location. Once the new location is added to the ENG SPACE file, the engineering user can respond on the mail message that the location has been added and then IT staff can use this option to update the equipment location. The NON-SPACE FILE LOCATION entry is automatically deleted when the LOCATION field is changed.

IT REMOTE LOCATION - This field is used to store information such as the address and phone number for IT equipment that is taken off site.

CMR- The Consolidated Memorandum of Receipt (CMR) for this piece of equipment. This field cannot be deleted and can only be changed to a CMR that also has IT TRACKING = YES.

USING SERVICE - The service within the facility that uses the equipment. Enter a question mark for a list of available choices.

UPDATE INVENTORY DATE? – Enter a Yes to update the LAST INVENTORIED field to the current date.

LAST INVENTORIED - This field may only be changed to the current date. You must enter YES at the previous field (UPDATE INVENTORY DATE?) to automatically update this field to the current date.

IT COMMENTS - This is a word processing field. A \<RET\> in this field will drop you into the editor. Once the comments are entered or edited, the screen will redisplay with the new information.

Inventory Edit (IT)

Entry \#: 1159

Mfgr: DELL COMPUTER

Model: X1330P81 Serial \#: DELL199384AE

XPS M1330 Notebook PC

LOCATION: NON-SPACE FILE LOCATION: TEST ROOM

IT REMOTE LOCATION (Press \<PF1\>Z for zoom editor):

CMR: 78A USING SERVICE: INFORMATION RESOURCES MGMT UPDATE INVENTORY DATE?: LAST INVENTORIED(R):

IT COMMENTS (wp): \[ENCRYPTED\]

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field. COMMAND: Press \<PF1\>H for help Insert

### Non-Space File Location Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report generates a list of equipment that has an entry in the NON-SPACE FILE LOCATION field. Equipment should only have a value in this field when the LOCATION field cannot be updated because an appropriate location is not available in the ENG SPACE file. Ideally, equipment will not remain on this report for an extended period of time.

DEVICE: HOME// \<RET\> UCX/TELNET

NON-SPACE FILE LOCATION REPORT FEB 13, 2008@16:09:59 page 1 EQUIP ID \# NON-SP DATE ENTERED BY LOCATION

NON-SPACE FILE LOCATION: CONFERENCE ROOM A410

1088 JAN 14, 2008 ITUSER, ONE 201-114

NON-SPACE FILE LOCATION: OPS LAB

1150 FEB 05, 2008 ITUSER, TWO 231-114

NON-SPACE FILE LOCATION: TEST ROOM 1100 FEB 11, 2008 ITUSER, TWO

1159 FEB 13, 2008 ITUSER, THREE

NON-SPACE FILE LOCATION: Trailer A Bldg 1 1087 JAN 11, 2008 ITUSER, FOUR

### IT Equipment Responsibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the menu for the equipment responsibility options.

Assign Responsibility Terminate Responsibility Transfer Responsibility Certify Hard Copy Signature

Print Hand Receipt for an Individual Add Entry to New Person File

IT Equipment Report Menu...

### Assign Responsibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to assign responsibility for IT equipment inventory items to individuals. Only equipment on a CMR that has IT TRACKING set to YES can be assigned.

The software allows you to assign responsibility for a single piece of equipment to more than one individual.

This option is locked with the EN IT ASSIGNMENT security key.

Assign Responsibility

Selecting accountable IT equipment to be assigned...

Select one of the following: E ENTRY \#

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Specify method to select equipment by: E// \<RET\> NTRY \#

Select EQUIPMENT ENTRY \#: 1142 121132 PRINTER IN USE

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 2%" />
<col style="width: 28%" />
<col style="width: 2%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Entry #</th>
<th></th>
<th>CMR</th>
<th></th>
<th>Location</th>
<th></th>
<th>Using Service</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1142</p>
<p>PRINTER</p></td>
<td></td>
<td>780</td>
<td></td>
<td>44G-107</td>
<td></td>
<td>INFORMATION RESOURCES MGMT</td>
</tr>
</tbody>
</table>

Mfgr: OKIDATA

Model: ML320 Serial \#: 121132

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 2%" />
<col style="width: 17%" />
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 2%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Responsible</th>
<th>Person</th>
<th></th>
<th>Assigned DT</th>
<th></th>
<th>Status</th>
<th></th>
<th>Status DT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ITUSER, ONE</p>
<p>Do you want</p></td>
<td colspan="2">to select this item?</td>
<td><p>JAN 15, 2008</p>
<p>YES</p></td>
<td></td>
<td>ASSIGNED</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Select EQUIPMENT ENTRY \#: 1100 2UA537008M COMPUTER-PC-ADMINISTRATIVE IN USE

Entry \# CMR Location Using Service

1100 78A INFORMATION RESOURCES MGMT DC 5100 COMPUTER

Mfgr: HEWLETT PACKARD/DESKTOP COMPUTER

Model: DC5100 Serial \#: 2UA537008M

| Responsible Person |     | Assigned DT  |     | Status   |     | Status DT |
|--------------------|-----|--------------|-----|----------|-----|-----------|
| ITUSER, ONE        |     | JAN 15, 2008 |     | ASSIGNED |     |           |

ITUSER, SEVENTYFOUR FEB 06, 2008 ASSIGNED

Do you want to select this item? YES

Select EQUIPMENT ENTRY \#: \<RET\>

2 equipment item(s) selected.

Do you want to print a list of the equipment? YES// \<RET\> YES Do you want the brief display format? YES// NO

DEVICE: HOME// \<RET\> UCX/TELNET

IT EQUIPMENT REPORT FEB 14, 2008@15:24:48 page 1

for selected equipment sorted by Entry \#

Entry \#: 1100 CMR: 78A Using Service: INFORMATION RESOURCES MGMT

Location: Svc of Location:

Mfgr Name: DC 5100 COMPUTER

Mfgr: HEWLETT PACKARD/DESKTOP COMPUTER

Model: DC5100 Ser. \#: 2UA537008M

IT Comments: Encrypted.

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

Assign: 02/06/08 ITUSER, SEVENTYFOUR Status: ASSIGNED

Entry \#: 1142 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: 44G-107 Svc of Location: Mfgr Name: PRINTER

Mfgr: OKIDATA

Model: ML320 Ser. \#: 121132

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

Count of IT equipment items on report = 2 Enter RETURN to continue or '^' to exit: \<RET\>

Selecting person(s) to be assigned responsibility... Select NEW PERSON NAME: ITUSER, TWO TI

Assign responsibility to ITUSER, TWO? YES Select Another NEW PERSON NAME: \<RET\>

1.  person(s) selected.

OK to create assignments? YES// \<RET\>

2.  equipment assignment(s) created.

### Terminate Responsibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to terminate one or more active responsibilities. The IT assignment can be selected by either the equipment entry number or the name of the person assigned that responsibility.

This option is locked with the EN IT ASSIGNMENT security key.

Select IT Equipment Responsibility Option: TERMInate Responsibility Select one of the following:

E EQUIPMENT

P PERSON

Specify method for selecting IT assignments: EQUIPMENT.

Select EQUIPMENT ENTRY \#: 1159 DELL199384AE COMPUTER-MICRO IN USE

ACTIVE IT RESPONSIBILITIES Screen 1 of 1 ID# ENTRY \# MFG EQUIP NAME OWNER STATUS

| 1 1159 |     | XPS M1330 Notebook | P ITUSER, ONE |     | SIGNED |
|--------|-----|--------------------|---------------|-----|--------|
| 2 1159 |     | XPS M1330 Notebook | P ITUSER, TWO |     | SIGNED |

Enter a list or range to select (1-2): Quit//2 OK to terminate assignments? NO// YES

1 IT responsibilities were terminated. Enter RETURN to continue or '^' to exit:

### Transfer Responsibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to transfer responsibility for selected equipment from one person to another person, by terminating the original responsibility and creating a new one.

If the equipment is transferred to the user performing the transfer of responsibility, and a \<RET\> is entered after the transfer is completed, you will be asked if “you want to sign to accept responsibility now”. A YES at this prompt will drop you into the Accept IT Responsibility functionality. Please see the Accept IT Responsibility option documentation in this section for more information.

This option is locked with the EN IT ASSIGNMENT security key.

Select one of the following: E EQUIPMENT

P PERSON

Specify method for selecting IT assignments: e EQUIPMENT

Select EQUIPMENT ENTRY \#: 1088 BJ292940 PRINTER IN USE

ACTIVE IT RESPONSIBILITIES Screen 1 of 1 ID# ENTRY \# MFG EQUIP NAME OWNER STATUS

| 1 1088 |     | PRINTER, INK JET, PO ITUSER, | ONE |     | CERTIFIED |
|--------|-----|------------------------------|-----|-----|-----------|
| 2 1088 |     | PRINTER, INK JET, PO ITUSER, | TWO |     | ASSIGNED  |

Enter a list or range to select (1-2): Quit//1

Select person for new assignment: ITUSER, THREE ITUSER, THREE 10B/ISC1 SUPV. APPLICATIONS SUPPORT

Assign responsibility to ITUSER, THREE? NO// y YES OK to transfer assignments? NO// y YES

1 IT responsibilities were terminated.

1 assignments were created.

Enter RETURN to continue or '^' to exit: \<RET\>

Do you want to sign to accept responsibility now? NO// YES

Government Furnished Equipment (GFE) USAGE GUIDELINES

- Do not loan GFE to anyone.
- Do not install personal software.
- Save data only to secure locations, such as FIPS 140-2 compliant storage devices.
- Do not attach non-approved portable storage devices to this equipment.
- Secure and store GFE under lock and key when not in use.
- Do not check GFE as checked luggage when traveling.
- Do not modify the configuration of the GFE.

USER RESPONSIBILITIES

- I understand this equipment is provided for official use only.
- I understand the transit of VA Information off-site is strictly prohibited unless accompanied by express written authorization.
- I am required by my supervisor to utilize this equipment to perform the duties of my job.
- I accept responsibility for the equipment identified above issued to me by the Department of Veterans Affairs.
- I fully understand that I could be billed for the replacement cost for any damage or loss occurring as a result of negligence.
- I have read and understand current VA Security Directive 6500 and any subsequent revisions or recensions.
- I will care for and protect equipment from loss or damage and will notify IT staff of any loss, damage or operational failures incurred.
- I understand that it is my responsibility to periodically return the equipment for routine maintenance.

OK to sign? NO// YES

Enter your Current Signature Code: \<Electronic Signature\> SIGNATURE VERIFIED

1 assignment records were signed.

Select one of the following: E EQUIPMENT

P PERSON

Specify method for selecting IT assignments: ^

### Certify Hard Copy Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows an IT employee to certify that an assigned person has signed a hard copy hand receipt accepting responsibility for tracked IT equipment. This option is expected to be used only when the assigned person does not have access to VistA in order to electronically sign for the equipment.

This option is locked with the EN IT ASSIGNMENT security key.

Select NEW PERSON NAME: ENGUSER, ONE OE 10B/ISC1 SUPV. APPLICATIONS SUPPORT

IT RESPONSIBILITIES TO CERTIFY FOR ENGUSER, ONE Screen 1 of 1 ID# ENTRY \# MFG EQUIP NAME MODEL SERIAL#

| 1 1088 |     | PRINTER, INK JET, PO BJC80         |     | BJ292940  |
|--------|-----|------------------------------------|-----|-----------|
| 2 1094 |     | SCANNER FI-4750                    |     | S03028X83 |
| 3 1151 |     | Inspiron 1721 Notebook I1721-ST001 |     | DL94872   |

Enter a list or range to select (1-3): Quit//1 OK to continue? NO// YES

Government Furnished Equipment (GFE) USAGE GUIDELINES

- Do not loan GFE to anyone.
- Do not install personal software.
- Save data only to secure locations, such as FIPS 140-2 compliant storage devices.
- Do not attach non-approved portable storage devices to this equipment.
- Secure and store GFE under lock and key when not in use.
- Do not check GFE as checked luggage when traveling.
- Do not modify the configuration of the GFE.

USER RESPONSIBILITIES

- I understand this equipment is provided for official use only.
- I understand the transit of VA Information off-site is strictly prohibited unless accompanied by express written authorization.
- I am required by my supervisor to utilize this equipment to perform the duties of my job.
- I accept responsibility for the equipment identified above issued to me by the Department of Veterans Affairs.
- I fully understand that I could be billed for the replacement cost for any damage or loss occurring as a result of negligence.
- I have read and understand current VA Security Directive 6500 and any subsequent revisions or recensions.
- I will care for and protect equipment from loss or damage and will notify IT staff of any loss, damage or operational failures incurred.
- I understand that it is my responsibility to periodically return the equipment for routine maintenance.

Is this the text on the signed, printed hand receipt? NO// YES

Date person signed hard copy hand receipt: (2/10/2008 - 2/14/2008): T (FEB 14, 2008) OK to certify? NO// YES

Enter your Current Signature Code: \<Electronic Signature\> SIGNATURE VERIFIED

1 assignment records were certified.

Enter RETURN to continue or '^' to exit: ^

### Print Hand Receipt for an Individual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows IT personnel to print a hard copy hand receipt for a selected individual who currently has assigned responsibility for IT equipment.

The printout of an individual's signed, active assignments also serves as the loan form for Government Furnished IT Equipment.

The Equipment Return Date on the loan form is determined by adding the DAYS BETWEEN RETURNS value from the CMR file to the PHYSICAL INVENTORY DATE (i.e. Last Inventoried) of the equipment item. A default of 90 days is used if a value is not specified for the applicable CMR. If the equipment does not have an inventory date, the current date is reported as the equipment return date.

The DAYS BETWEEN RETURNS value is entered/edited using the CMR File Enter/Edit option.

You will have the option of choosing one of the following print options.

DATE OF SIGNATURE - allows you to select assignments signed electronically or via wet signature on a given date, regardless of current status.

SIGNED - allows you to select active assignments signed electronically or via wet signature.

UNSIGNED - allows you to select active assignments not signed, either electronically or via wet signature or signed documents where the signature date is more than 359 days ago. (You must re-sign by the one-year anniversary of the previous signature.)

If an unsigned hard copy hand receipt is printed and signed, it must then be certified electronically, using the Certify Hard Copy Signature option.

Print Hand Receipt for an Individual Select one of the following:

D DATE OF SIGNATURE

S SIGNED

U UNSIGNED

Print Hand Receipt for Unsigned or Signed IT assignments: UNSIGNED// SIGNED

Select NEW PERSON NAME: ITUSER, ONE OI 10B/ISC1 SUPV. APPLICATIONS SUPPORT DEVICE: HOME// \<RET\> UCX/TELNET

IT HAND RECEIPT/LOAN FORM FOR GOVERNMENT FURNISHED EQUIPMENT (GFE) Page 1

Electronic Accepted Substitute for VA Form 0887(a/b)

STATION: 660 ASSIGNED TO: ITUSER, ONE Printed 4/1/08@10:38

ENTRY \# MFG EQUIP NAME MODEL SERIAL#

6987 PRINTER LA75 TY71627761

Signed: MAR 31, 2008 Certified by: ITSUPERVISOR, ONE

Issued By: ITUSER, TWO Contact \#: 555-555-5555 Equipment Return Date: 4/1/08.

13815 PRINTER 2225D 2804S02966

Signed: Mar 31, 2008@15:00:05 Signature: /ES/ONE ITUSER

Issued By: ITUSER, TWO Contact \#: 555-555-5555 Equipment Return Date: 5/1/08.

Government Furnished Equipment (GFE) USAGE GUIDELINES

- Do not loan GFE to anyone.
- Do not install personal software.
- Save data only to secure locations, such as FIPS 140-2 compliant storage devices.
- Do not attach non-approved portable storage devices to this equipment.
- Secure and store GFE under lock and key when not in use.
- Do not check GFE as checked luggage when traveling.
- Do not modify the configuration of the GFE.

USER RESPONSIBILITIES

IT HAND RECEIPT/LOAN FORM FOR GOVERNMENT FURNISHED EQUIPMENT (GFE) Page 2

Electronic Accepted Substitute for VA Form 0887(a/b)

STATION: 999 ASSIGNED TO: ITUSER, ONE Printed 4/1/08@11:10

- I understand this equipment is provided for official use only.
- I understand the transit of VA Information off-site is strictly prohibited unless accompanied by express written authorization.
- I am required by my supervisor to utilize this equipment to perform the duties of my job.
- I accept responsibility for the equipment identified above issued to me by the Department of Veterans Affairs.
- I fully understand that I could be billed for the replacement cost for any damage or loss occurring as a result of negligence.
- I have read and understand current VA Security Directive 6500 and any subsequent revisions or recensions.
- I will care for and protect equipment from loss or damage and will notify IT staff of any loss, damage or operational failures incurred.
- I understand that it is my responsibility to periodically return the equipment for routine maintenance.

### Add Entry to New Person File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to add an entry to the NEW PERSON file. A person should only be added through this option if that person will NOT be provided a user account to sign onto the computer but will be assigned responsibility for IT equipment.

This option is locked with the EN IT ASSIGNMENT security key.

Add Entry to New Person File

This option should only be used to add a person to the NEW PERSON (#200) file when that person will be assigned responsibility for IT equipment but is not already in the file and will NOT be given a user account to sign on the computer.

Do you want to add an entry to the NEW PERSON file? NO// y YES Enter NEW PERSON's name (Family, Given Middle Suffix): ITUSER, ONE JR

Are you adding 'ITUSER, ONE JR' as a NEW PERSON (the 2370TH)? No// Y (Yes)

Checking SOUNDEX for matches. No matches found.

Name components.

FAMILY (LAST) NAME: ITUSER// \<RET\> GIVEN (FIRST) NAME: ONE// \<RET\> MIDDLE NAME: \<RET\>

SUFFIX: JR// \<RET\>

Now for the Identifiers.

INITIAL: OI

SSN: 000066600 SEX: \<RET\> NPI: \<RET\>

### IT Equipment Report Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu provides the following reports for monitoring and tracking IT equipment.

Individual Responsibility for IT Assets Report Unassigned IT Asset Report

Assignments Pending Acceptance Report Tracked IT Assets Report

Signature Exception Report Assignment Inquiry

### Individual Responsibility for IT Assets Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display or print a report for a specific individual who currently has assigned responsibility for IT equipment.

Select NEW PERSON NAME: ITUSER, ONE OI 10B/ISC1.

Include ended assignments? NO// \<RET\>

DEVICE: HOME// \<RET\> UCX/TELNET

INDIVIDUAL RESPONSIBILITY REPORT FEB 14, 2008@10:01:49 page 1

for ITUSER, ONE sorted by location

Entry \#: 1006 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: 201-114 Svc of Location: INFORMATION SYSTEMS CENTER Mfgr Name: TERMINAL DISPLAY, AMBER SCREEN, VT520

Mfgr: DIGITAL COMPUTER CONT

Model: VT520 Ser. \#: SWC1234

Assign Date: JAN 17, 2008 Status: CERTIFIED Status Date: 01/17/08 Count of IT equipment items on report = 1

### Unassigned IT Asset Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display/print a report of tracked IT assets where responsibility is not currently assigned to an individual. Assets are considered to be tracked IT assets if their CMR value has IT TRACKING set to YES.

Several methods for selection and sorting are available. You also have the option of printing either a brief or full display.

Unassigned IT Asset Report

Select one of the following:

An ALL-TRACKED IT EQUIPMENT

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Specify method to select equipment by: ALL TRACKED IT EQUIPMENT Select one of the following:

E ENTRY \#

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Sort equipment by: ENTRY \#

Do you want the brief display format? YES// NO DEVICE: HOME// UCX/TELNET

IT EQUIPMENT NOT ASSIGNED REPORT FEB 14, 2008@10:40 page 1.

for All tracked IT equipment sorted by Entry \#

Entry \#: 8 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: Svc of Location: Mfgr Name: 50 MHZ EISA PC

Mfgr: DIGITAL EQUIP

Model: 450STPCT25AA Ser. \#: AB34300UER

Count of IT equipment items on report = 1 Enter RETURN to continue or '^' to exit:

### Assignments Pending Acceptance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display or print a list of equipment with IT assignments that have not yet been signed. There are several methods for selection and sorting available. You also have the option of printing either a brief or full display. The example that follows shows the brief display, followed by the full display for the same user entries.

Assignments Pending Acceptance Report Select one of the following:

An ALL-TRACKED IT EQUIPMENT

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Specify method to select equipment by: LOCATION Select ENG SPACE ROOM NUMBER: OFFSITE

Select one of the following: E ENTRY \#

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Sort equipment by: ENTRY \#

Do you want the brief display format? YES// \<RET\>

DEVICE: HOME// \<RET\> UCX/TELNET

Brief Display

Assignments Pending Acceptance Report FEB 14, 2008@10:20:52 page 1 for Location: OFFSITE sorted by Entry \#

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 28%" />
<col style="width: 2%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Entry #</th>
<th>CMR</th>
<th>Location</th>
<th></th>
<th>Using Service</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1086</p>
<p>COMPUTER</p>
<p>Assign:</p></td>
<td><p>780</p>
<p>01/15/08</p></td>
<td><p>OFFSITE</p>
<p>ITUSER, ONE</p></td>
<td></td>
<td><p>INFORMATION RESOURCES MGMT</p>
<p>Status: ASSIGNED</p></td>
</tr>
<tr class="even">
<td><p>1130</p>
<p>DC 5100</p>
<p>Assign:</p></td>
<td><p>780</p>
<p>COMPUTER 01/15/08</p></td>
<td><p>OFFSITE</p>
<p>ITUSER, ONE</p></td>
<td></td>
<td><p>INFORMATION RESOURCES MGMT</p>
<p>Status: ASSIGNED</p></td>
</tr>
<tr class="odd">
<td><p>1134</p>
<p>DC 5100</p>
<p>Assign:</p></td>
<td><p>780</p>
<p>COMPUTER 01/15/08</p></td>
<td><p>OFFSITE</p>
<p>ITUSER, ONE</p></td>
<td></td>
<td><p>INFORMATION RESOURCES MGMT</p>
<p>Status: ASSIGNED</p></td>
</tr>
<tr class="even">
<td>1161</td>
<td>78A</td>
<td>OFFSITE</td>
<td></td>
<td>INFORMATION RESOURCES MGMT</td>
</tr>
<tr class="odd">
<td>Assign:</td>
<td>01/17/08</td>
<td>ITUSER, TWO</td>
<td></td>
<td>Status: ASSIGNED</td>
</tr>
</tbody>
</table>

Count of IT equipment items on report = 4 Count of unsigned assignments on report = 4

Enter RETURN to continue or '^' to exit:

Full Display

Assignments Pending Acceptance Report FEB 14, 2008@10:27:11 page 1 for Location: OFFSITE sorted by Entry \#

Entry \#: 1086 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: OFFSITE Svc of Location:

Mfgr Name: COMPUTER Mfgr: MICRON CORPORATION

Model: T2400 Ser. \#: 4321

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

Entry \#: 1130 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: OFFSITE Svc of Location:

Mfgr Name: DC 5100 COMPUTER

Mfgr: HEWLETT PACKARD/DESKTOP COMPUTER

Model: DC5100 Ser. \#: 2UA537009Z

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

Entry \#: 1134 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: OFFSITE Svc of Location:

Mfgr Name: DC 5100 COMPUTER

Mfgr: HEWLETT PACKARD/DESKTOP COMPUTER

Model: DC5100 Ser. \#: 2UA5370093

Enter RETURN to continue or '^' to exit:

Assignments Pending Acceptance Report FEB 14, 2008@10:27:11 page 2 for Location: OFFSITE sorted by Entry \#

Entry \#: 1134 (continued)

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

Entry \#: 1161 CMR: 78A Using Service: INFORMATION RESOURCES MGMT

Location: OFFSITE Svc of Location:

Mfgr Name:

Mfgr: MICRON CORPORATION

Model: Transport T2400 Ser. \#: 4279964-0001

IT Remote Location: That place were the buffalo don't roam nor antelope play.

IT Comments: Encrypted.

Assign: 01/17/08 ITUSER, TWO Status: ASSIGNED

Count of IT equipment items on report = 4 Count of unsigned assignments on report = 4 Enter RETURN to continue or '^' to exit:

### Tracked IT Assets Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display or print a report of equipment inventory that has a CMR value with IT TRACKING equal to YES. The report can be run for specific equipment, groups of equipment, or all tracked IT equipment.

Tracked IT Assets Report

Select one of the following:

An ALL-TRACKED IT EQUIPMENT

E ENTRY \#

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Specify method to select equipment by: LOCATION.

Select ENG SPACE ROOM NUMBER: 221-114 114 INFORMATION SYSTEMS CE NTER OFFICE

Select one of the following: E ENTRY \#

C CMR

U USING SERVICE

L LOCATION

S SERVICE OF LOCATION

Sort equipment by: SERVICE OF LOCATION

Do you want the brief display format? YES// \<RET\>

DEVICE: HOME// \<RET\> UCX/TELNET

IT EQUIPMENT REPORT FEB 15, 2008@10:00:21 page 1

for Location: 221-114 sorted by Service of Loc.

Entry \# CMR Location Using Service

1124 780 221-114 INFORMATION RESOURCES MGMT

DC 5100 COMPUTER

Assign: 01/15/08 ITUSER, ONE Status: ASSIGNED

1125 780 221-114 INFORMATION RESOURCES MGMT

DC 5100 COMPUTER

Assign: 01/15/08 ITUSER, TWO Status: ASSIGNED

Count of IT equipment items on report = 2 Enter RETURN to continue or '^' to exit:

### Signature Exception Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display or print a report of assignments of IT responsibility with the most recent signature at least one year old as of a specified date.

Signature Exception Report

Select one of the following:

E ELECTRONICALLY SIGNED

C CERTIFIED HARD COPY SIGNATURE

B BOTH

Select type of signature to check: BOTH// \<RET\>

Report signatures at least 1 year old as of: Feb 13, 2008// 2/15/08

DEVICE: HOME// \<RET\> UCX/TELNET

SIGNATURE EXCEPTION REPORT FEB 14, 2008@16:14:50 page 1

for signatures at least one year old as of Feb 15, 2008

Owner Entry \# Status, Status Date

ENUSER, ONE 1091 SIGNED 01/11/07 DEC MULTIPLEXOR

ENUSER, ONE 1092 SIGNED 01/11/07 UPS COMPUTER UNIT

XPS M1330 Notebook PC

ENUSER, TWO 1006 CERTIFIED 01/17/07 TERMINAL DISPLAY, AMBER SCREEN, VT520

ENUSER, THREE 1138 CERTIFIED 01/14/07 PRINTER, INK JET, PORTABLE

ENUSER, THREE 1152 CERTIFIED 01/14/07.

Inspiron 1721 Notebook PC

ENUSER, FOUR 1017 SIGNED 01/18/07 SWITCH LINE SHARING

ENUSER, FOUR 1095 SIGNED 01/15/07 BAR CODE PRINTER

ENUSER, FIVE 1128 SIGNED 01/16/07 DC 5100 COMPUTER

Enter RETURN to continue or '^' to exit:

SIGNATURE EXCEPTION REPORT FEB 14, 2008@16:14:50 page 2

for signatures at least one year old as of Jan 31, 2009

| Owner        |     | Entry \# |     | Status |     | Status Date |
|--------------|-----|----------|-----|--------|-----|-------------|
| ENUSER, FIVE |     | 1132     |     | SIGNED |     | 01/10/07    |

DC 5100 COMPUTER

ENUSER, SIX 1087 CERTIFIED 01/11/07 XPS 6600 COMPUTER

ENUSER, SIX 1148 CERTIFIED 01/11/07.

22-Inch Widescreen LCD Monitor

ENUSER, SIX 1152 CERTIFIED 01/11/07.

Inspiron 1721 Notebook PC

ENUSER, SIX 1153 CERTIFIED 01/11/07.

19-Inch Widescreen LCD Monitor Count of signatures on report = 13

### Assignment Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display or print information on all of your IT equipment assignments of responsibility by the entry number for the piece of equipment or the person assigned responsibility.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>Select IT</th>
<th colspan="3">ASSIGNMENT EQUIPMENT:</th>
<th>??</th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Choose 1101</td>
<td colspan="3"><p>from:</p>
<p>ENUSER, ONE</p></td>
<td>ASSIGNED</td>
<td>2UA537008N</td>
<td colspan="2">IN USE</td>
</tr>
<tr class="even">
<td colspan="4">1159 ENGSER, ONE IN USE</td>
<td>SIGNED</td>
<td>DELL199384AE</td>
<td>COMPUTER-MICRO</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4">Select IT ASSIGNMENT EQUIPMENT:</td>
<td>1159</td>
<td>DELL199384AE</td>
<td>COMPUTER-MICRO</td>
<td>IN USE</td>
</tr>
<tr class="even">
<td colspan="2">ENUSER, ONE</td>
<td>SIGNED</td>
<td colspan="2"></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">DEVICE: <strong>&lt;RET&gt;</strong></td>
<td>UCX/TELNET</td>
<td colspan="2">Right Margin:</td>
<td colspan="3">80// &lt;RET&gt;</td>
</tr>
</tbody>
</table>

IT ASSIGNMENT FEB 13,2008 09:08 PAGE 1

EQUIPMENT: 1159 OWNER: ENUSER, ONE STATUS(c): SIGNED STATUS DATE(c): 02/12/08

ASSIGNED: FEB 12,2008 13:47 BY: ENUSER, TWO

SIGNED: FEB 12,2008 13:55 TEXT VERSION: 1 FROM PATCH: EN\*7\*87 CERTIFIED: BY:

ENDED: BY:

PREVIOUS SIGNATURES:

Select IT ASSIGNMENT EQUIPMENT:

### IT Owner Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IT Owner Menu contains options intended for any individual that could be assigned responsibility for IT equipment.

Accept IT Responsibility

Individual Responsibility for IT Assets Report Print My Hand Receipt

Assignment Inquiry

#### Accept IT Responsibility

This option is used to accept responsibility for assigned IT equipment. It allows you to enter the initial acceptance with your electronic signature code or reaffirm the acceptance (re-sign) before it expires. You must re-sign by the one-year anniversary (359 days) of the previous signature.

Government Furnished Equipment (GFE) Usage Guidelines and User Responsibilities are displayed on the screen. Your electronic signature certifies that you understand and will comply with these guidelines and responsibilities.

Select IT Owner Menu Option: Accept IT Responsibility

IT RESPONSIBILITIES REQUIRING SIGNATURE BY ENGUSER, One Screen 1 of 1

| ID# ENTRY \# |     | MFG EQUIP NAME MODEL          |     | SERIAL#      |
|--------------|-----|-------------------------------|-----|--------------|
| 1 1101       |     | DC 5100 COMPUTER DC5100       |     | 2UA537008N   |
| 2 1159       |     | XPS M1330 Notebook P X1330P81 |     | DELL199384AE |

Enter a list or range to select (1-2): Quit//2 OK to continue? NO// YES

Government Furnished Equipment (GFE) USAGE GUIDELINES

- Do not loan GFE to anyone.
- Do not install personal software.
- Save data only to secure locations, such as FIPS 140-2 compliant storage devices.
- Do not attach non-approved portable storage devices to this equipment.
- Secure and store GFE under lock and key when not in use.
- Do not check GFE as checked luggage when traveling.
- Do not modify the configuration of the GFE.

USER RESPONSIBILITIES

- I understand this equipment is provided for official use only.
- I understand the transit of VA Information off-site is strictly prohibited unless accompanied by express written authorization.
- I am required by my supervisor to utilize this equipment to perform the duties of my job.
- I accept responsibility for the equipment identified above issued to me by the Department of Veterans Affairs.
- I fully understand that I could be billed for the replacement cost for any damage or loss occurring as a result of negligence.
- I have read and understand current VA Security Directive 6500 and any subsequent revisions or recensions.

OK to sign? NO// YES

Enter your Current Signature Code: \<Electronic Signature\> SIGNATURE VERIFIED

3.  assignment records were signed.

#### Individual Responsibility for IT Assets Report

This report shows information on all IT equipment currently assigned to you. You may also choose to include assignments that have ended.

Select IT Owner Menu Option: Individual Responsibility for IT Assets Report Include ended assignments? NO// \<RET\>

DEVICE: HOME// \<RET\> UCX/TELNET

INDIVIDUAL RESPONSIBILITY REPORT FEB 13, 2008@07:40:44 page 1

for ENUSER, ONE sorted by location

Entry \#: 1101 CMR: 780 Using Service: INFORMATION RESOURCES MGMT

Location: Svc of Location:

Mfgr Name: DC 5100 COMPUTER

Mfgr: HEWLETT PACKARD/DESKTOP COMPUTER

Model: DC5100 Ser. \#: 2UA537008N

Assign Date: FEB 12, 2008 Status: ASSIGNED Status Date: 02/12/08.

Entry \#: 1159 CMR: 78A Using Service: INFORMATION RESOURCES MGMT

Location: 231-114 Svc of Location: Mfgr Name: XPS M1330 Notebook PC

Mfgr: DELL COMPUTER

Model: X1330P81 Ser. \#: DELL199384AE

Assign Date: FEB 12, 2008 Status: SIGNED Status Date: 02/12/08 Count of IT equipment items on report = 2

#### Print My Hand Receipt

This option allows you to print a hard copy hand receipt for IT items assigned to you. The printout of an individual's signed, active assignments also serves as the loan form for Government Furnished IT Equipment.

The Equipment Return Date on the loan form is determined by adding the DAYS BETWEEN RETURNS value from the CMR file to the PHYSICAL INVENTORY DATE (i.e. Last Inventoried) of the equipment item. A default of 90 days is used if a value is not specified for the applicable CMR. If the equipment does not have an inventory date, the current date is reported as the equipment return date.

You will have the option of choosing one of the following print options.

DATE OF SIGNATURE - allows you to select assignments signed electronically or via wet signature on a given date, regardless of current status.

SIGNED - allows you to select active assignments signed electronically or via wet signature.

UNSIGNED - allows you to select active assignments not signed, either electronically or via wet signature or signed documents where the signature date is more than 359 days ago. (You must re-sign by the one-year anniversary of the previous signature.)

Print My Hand Receipt

Select one of the following:

D DATE OF SIGNATURE

S SIGNED

U UNSIGNED

Print Hand Receipt for Unsigned or Signed IT assignments: UNSIGNED// SIGNED

Select NEW PERSON NAME: ITUSER, ONE OI 10B/ISC1 SUPV. APPLICATIONS SUPPORT DEVICE: HOME// \<RET\> UCX/TELNET

IT HAND RECEIPT/LOAN FORM FOR GOVERNMENT FURNISHED EQUIPMENT (GFE) Page 1

Electronic Accepted Substitute for VA Form 0887(a/b)

STATION: 660 ASSIGNED TO: ITUSER, ONE Printed 4/1/08@10:38

ENTRY \# MFG EQUIP NAME MODEL SERIAL#

6987 PRINTER LA75 TY71627761

Signed: MAR 31, 2008 Certified by: ITSUPERVISOR, ONE

Issued By: ITUSER, TWO Contact \#: 555-555-5555 Equipment Return Date: 4/1/08.

13815 PRINTER 2225D 2804S02966

Signed: Mar 31, 2008@15:00:05 Signature: /ES/ONE ITUSER

Issued By: ITUSER, TWO Contact \#: 555-555-5555 Equipment Return Date: 5/1/08.

Government Furnished Equipment (GFE) USAGE GUIDELINES

- Do not loan GFE to anyone.
- Do not install personal software.
- Save data only to secure locations, such as FIPS 140-2 compliant storage devices.
- Do not attach non-approved portable storage devices to this equipment.
- Secure and store GFE under lock and key when not in use.
- Do not check GFE as checked luggage when traveling.
- Do not modify the configuration of the GFE.

USER RESPONSIBILITIES

IT HAND RECEIPT/LOAN FORM FOR GOVERNMENT FURNISHED EQUIPMENT (GFE) Page 2

Electronic Accepted Substitute for VA Form 0887(a/b)

STATION: 999 ASSIGNED TO: ITUSER, ONE Printed 4/1/08@11:10

- I understand this equipment is provided for official use only.
- I understand the transit of VA Information off-site is strictly prohibited unless accompanied by express written authorization.
- I am required by my supervisor to utilize this equipment to perform the duties of my job.
- I accept responsibility for the equipment identified above issued to me by the Department of Veterans Affairs.
- I fully understand that I could be billed for the replacement cost for any damage or loss occurring as a result of negligence.
- I have read and understand current VA Security Directive 6500 and any subsequent revisions or recensions.
- I will care for and protect equipment from loss or damage and will notify IT staff of any loss, damage or operational failures incurred.
- I understand that it is my responsibility to periodically return the equipment for routine maintenance.

#### Assignment Inquiry

This option allows you to display or print information on all of your IT equipment assignments of responsibility.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>Select IT</th>
<th colspan="3">ASSIGNMENT EQUIPMENT:</th>
<th>??</th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Choose 1101</td>
<td colspan="3"><p>from:</p>
<p>ENUSER, ONE</p></td>
<td>ASSIGNED</td>
<td>2UA537008N</td>
<td colspan="2">IN USE</td>
</tr>
<tr class="even">
<td colspan="4">1159 ENUSER, ONE IN USE</td>
<td>SIGNED</td>
<td>DELL199384AE</td>
<td>COMPUTER-MICRO</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4">Select IT ASSIGNMENT EQUIPMENT:</td>
<td>1159</td>
<td>DELL199384AE</td>
<td>COMPUTER-MICRO</td>
<td>IN USE</td>
</tr>
<tr class="even">
<td colspan="2">ENUSER, ONE</td>
<td>SIGNED</td>
<td colspan="2"></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="2">DEVICE: <strong>&lt;RET&gt;</strong></td>
<td>UCX/TELNET</td>
<td colspan="2">Right Margin:</td>
<td colspan="3">80// &lt;RET&gt;</td>
</tr>
</tbody>
</table>

IT ASSIGNMENT FEB 13,2008 09:08 PAGE 1

EQUIPMENT: 1159 OWNER: ENUSER, ONE STATUS(c): SIGNED STATUS DATE(c): 02/12/08

ASSIGNED: FEB 12,2008 13:47 BY: ENUSER, TWO

SIGNED: FEB 12,2008 13:55 TEXT VERSION: 4 FROM PATCH: EN\*7\*1000 CERTIFIED: BY:

ENDED: BY:

PREVIOUS SIGNATURES:

Select IT ASSIGNMENT EQUIPMENT:

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ALD - Abbreviation for appropriation, limitation, department.
CMR - Consolidated Memorandum of Receipt. The basic instrument by which accountability for capital equipment is recorded.
Configuration-A particular selection of hardware and software resources that are tailored to provide optimum usage of ADP systems. This includes the type of CPU, type and number of disk drives, type and number of terminals, amount of main storage and so on.
Criticality - An index used by the package to rank the importance of performing preventive maintenance inspections on a particular device.
VISTA - Decentralized Hospital Computer Program-The name of the effort to install computer systems in the Veterans Administration Department of Medicine and Surgery's hospitals.
FileManager - Also known as VA FileMan. A set of MUMPS routines used to enter, maintain, access and manipulate related data in a file. It is the basic system.
used by all VA applications in creating files.
Information Systems Center (ISC) - One of the VA's seven regional offices for the management and development of application software. The ISCs are also responsible for providing support to field sites and for training personnel.
IRL - Interactive Reader Language. Proprietary language used by the Intermec line of portable bar code readers.
IT – Information Technology.
MailMan - An electronic mail, teleconferencing, and networking system which is an integral part of the Kernel.
MUMPS - Massachusetts General Hospital Utility Multi-Programming System. This is the computer language used by all VA VISTA applications.
NXRN# - A sequential number assigned by centralized CMR Management System in Austin.
Service Pointer - The functional entity (generally a service) within the facility that uses the device.
Glossary
Site Configurable - A term used to refer to features in the system which can be tailored according to the needs of particular sites.

## Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A.1. Electronic Work Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic work orders are simply work requests that are entered into VISTA by the person who actually wants the work done. The objective of the Electronic Work Order module is to relieve Engineering Services of a major data entry task so that they will be better able to concentrate on the technical aspects of work control, especially in areas that are scrutinized by the JCAHO.

Users of the electronic work order module are usually given the menu option ENWOWARD (Electronic Work Requests), most commonly as a secondary menu option.

1.  Request Electronic Work Order (ENWONEW-WARD)

This option was developed for non-Engineering personnel to use when entering Electronic Work Orders. This option uses input template ENWOWARD in prompting for information. Sites are free to customize this template or to create one of their own. If an input template named ENZWOWARD exists, the Engineering package will use it in preference to ENWOWARD. The system will automatically generate a permanent identifier, called the ORIGINAL WORK ORDER NUMBER, for each work request.

2.  Edit Electronic Work Order (ENWOEDIT-WARD)

The VISTA user who physically enters an Electronic Work Order is allowed to edit it, but only until such time as Engineering Service assigns it to a working shop.

This edits feature uses the same input template as the Request option.

3.  Electronic Work Order Status Check (ENWOSTATUS-WARD)

This option allows users to check the status of any Engineering Work Order. Workorder information is displayed on a CRT screen and may be printed if necessary. It is not possible to edit a work order from within this option. Data elements from which potentially sensitive information can be deduced (such as LABOR COST) are omitted from this display.

4.  Incomplete Work Orders (ENWOST-WARD)

This option provides a list of incomplete work orders that were either associated with a given location, requested by a specific service or section, physically entered by a particular VISTA user.

If you select (1), you will be prompted for a WING or BUILDING. All incomplete work orders for that location will be listed. Option (2) prompts you for a selection from File 49 (Service/Section). Option (3) will ask for the name of a VISTA user and then list all incomplete work orders that were entered by this individual.

The list includes CURRENT WORK ORDER \#, REQUEST DATE, STATUS, LOCATION, PRIORITY, EQUIPMENT ID# (if applicable), and TASK.

DESCRIPTION. If CRT display is chosen, the user can request an expanded display. EMERGENCY and HIGH PRIORITY work orders are highlighted on CRT screens.

When an Electronic Work Order is entered, it immediately receives what is known as its ORIGINAL WORK ORDER NUMBER. This is a permanent identifier of each work request and will never change, no matter how many times a work order is transferred between shops. When checking the status of a work request, users can always use the ORIGINAL WORK ORDER NUMBER to call it up. Work orders can also be called up quickly by LOCATION or by TASK DESCRIPTION.

The system automatically records the VISTA user who physically enters each Electronic Work Order. This individual may be the actual requester but could also be someone who simply entered the work order on behalf of the requester. If questions arise concerning an Electronic Work Order, Engineering Service will first attempt to contact the REQUESTER (also known as CONTACT PERSON) rather than the person by whom the work order was physically entered.

Engineering Service has the prerogative of disapproving Electronic Work Requests. When this happens, a MailMan message is automatically sent to the person who entered the work order. The message will contain the COMMENTS field from the Electronic Work Order itself. It should be standard procedure for anyone who disapproves a work order to enter the reasons for doing so in the COMMENTS field *before closing the work order*.

### A.2. Using Portable Bar Code Readers and Electrical Safety Analyzers with VISTA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Downloading and Uploading

Connecting to VISTA

Downloading and uploading require that the Trakker Bar Code Reader or the MedTester Electrical Safety Analyzer be physically connected to VISTA. This can be accomplished in several ways.

Dedicated port: Define the port as though the Trakker or MedTester were a VT-100 data terminal. Be sure that the baud rate and other basic data communication parameters of the dedicated port match those of the Trakker or MedTester. The principal disadvantage to the use of dedicated ports is inconvenience. All uploading and downloading would have to be done at a very limited number of locations.

Wedge: Special wedges can be purchased that will allow Trakkers or MedTesters to share a data line with a CRT. Different types of wedges are available, and specific installation instructions should be provided by the manufacturer. Not all wedges are designed for both downloading and uploading, and users must therefore be very careful when purchasing hardware of this type.

Auxiliary CRT port: The DEC VT-320 is strongly recommended since it supports full bidirectional data communication through its aux port allowing both downloading and uploading capabilities. The overwhelming majority of CRTs on today's market are NOT capable of this.

Trakker 9440 Bar Code Reader Connection

A special RS-232 cable with a Trakker connector on one end and a standard DB-25 female connector on the other should be procured for each Trakker unit. You will need a cable with a six-pin modular plug on one end and a male DB-25 connector on the other. The recommended configuration is:

SIX-PIN DB-25 MALE

MODULAR PLUG CONNECTOR

================= ============== 2 ---------------------------------------2

3 ------------------------------------------ 7

5 ------------------------------------------ 3

6 ------------------------------------------ 6

This configuration allows the Trakker 9440 to supply the DATA SET READY signal (pin 6) which must be present in order for a VT-320 aux port to be enabled.

The PRINTER SET-UP SCREEN of the VT-320 will allow you to configure the CRT for use with a Trakker 9440. Use the following steps to get to this screen.

1.  hold the SHIFT key and press SET-UP.
2.  use the right arrow key to move the cursor to the box labeled "Printer.”
3.  press the ENTER key.

From this point, you can set the software selectable features of the aux port. Many of the settings for the Aux port must match the settings of the Trakker.

1.  Speed: 1200 (must match)
2.  Printer to Host Communication: This MUST be set to Printer to Host.
3.  Print Mode: Normal Print Mode
4.  XOFF: XOFF
5.  Bits and Parity: 8 bits, no parity (must match)
6.  Stop Bit: 1 stop bit (must match)
7.  Print Region: Print Full Page
8.  Printed Data Type: National Only
9.  Print Terminator: No Terminator

If you elect to interface your Trakker to VISTA via a DECSERVER, the following setup should work:

=========================================================

| Character Size: 8 Input Speed: | 1200           |          |
|--------------------------------|----------------|----------|
| Flow Control: XON              | Output Speed:  | 1200     |
| Parity: NONE Stop Bits: 1      | Modem Control: | Disabled |
| Access: Remote                 | Local Switch:  | None     |
| Backward Switch: None          | Name:          | LC-6-16  |
| Break: Disabled                | Session Limit: | 4        |
| Forward Switch: None           | Type:          | ANSI     |

Preferred Service: None Authorized Groups: 0

(Current) Groups: 0

==================================================

Trakker Configuration

To configure the Trakker 9440 for operation with VISTA

1.  Turn the Trakker on by pressing the \< on-off \> key. The unit should perform a brief self-test and then display a "Ready" prompt.
2.  Hold down the \<CTRL \> key and press \<E\>. The words "CONFIGURATION MENU:" should appear.

You are now in the configuration mode. Use the \< enter \> key to step through the basic operating parameters. Unless otherwise instructed, use the \< space \> key to make your selections.

1.  Press the \<enter \> key until you are prompted to "Select or modify operating parameters?". The word "NO" will appear on the fourth Trakker display line. Change "NO" to "YES" using the \< space \> key. The following parameters are recommended:
    1.  BEEP VOLUME: Set this according to your preference.
    2.  DISPLAY MODE: BUFFERED
    3.  CHARACTER SET: US-ASCII
    4.  CPU RESP REQD MODE: DISABLED
    5.  PREAMBLE A REQUIRED: NO
    6.  LASER SCANNER MODE: ONE-SHOT TRIGGER
    7.  APPEND TIME TO DATA: NO
    8.  TIME IN SECONDS: NO
    9.  RESUME IRL PROGRAM: NO
    10. AUTOMATIC SHUT-OFF: 10 (designates amount of time in minutes)
    11. BACKLIGHT TIMEOUT: 10 (designates amount of time in minutes)
2.  The next configuration heading is "Select or modify comm protocol?". Use the

\<space \> key to select "POINT TO POINT". Selections must match the configuration of the VISTA port. Recommended settings are:

1.  CHECK CTS: NO
2.  XON: \<CTRL \> \<Q\>. "DC1" should appear on the last Trakker display line. Press

\<enter \>to continue.

3.  XOFF: \<CTRL \>\<S\>. Observe "DC3" and press \< enter \>to continue.
4.  BAUD RATE: 9600 (match VISTA port)
5.  PARITY: DISABLED
6.  DATA BITS: 8 (match VISTA port)
7.  STOP BITS: 1 (match VISTA port)
8.  TIMEOUT DELAY: 10 (seconds)
9.  INTERCHAR DELAY: 50 MS (milliseconds)
10. TURNAROUND DELAY: 0 (zero)
3.  The Trakker is now configured for use with VISTA. Press the \<ALT\>\<E\> (for escape) to save any changes. These settings will remain in a non-volatile

section of Trakker memory until the Trakker is re-configured. If you want to exit the configuration mode without saving any changes, hold down the \< CTRL \>\<Z\> instead.

MedTester Electrical Safety Analyzer Connection

The aux port of the VT-320 is a six-pin modular jack, so you will need a cable with a six-pin modular plug on one end and a female DB-25 connector on the other. The proper configuration is:

SIX-PIN DB-25 FEMALE

MODULAR PLUG CONNECTOR

=============== ============= 5 ---------------------------------------------------------- 2

2 ---------------------------------------------------------- 3

3 ---------------------------------------------------------- 7

1

6

With this configuration, the VT-320 supplies the DATA SET READY signal to itself (by virtue of the connection between pin 1 and pin 6). This signal must be present in order for a VT-320 aux port to be enabled.

The PRINTER SET-UP SCREEN of the VT-320 will allow you to configure the CRT for use with a MedTester. To get to this screen:

1.  hold the \<SHIFT \> key and press \<SET-UP \>
2.  use the right arrow to move the cursor to the box labeled "Printer",
3.  press the \<ENTER \> key.

From this point, you can set the software selectable features of the aux port. Many of the settings for the MedTester must match the settings of the AUX port. The following settings are recommended.

1.  Speed: 9600 or less (must match)
2.  Printer to Host Communication: MUST be set to Printer to Host
3.  Print Mode: Normal Print Mode
4.  XOFF: not used.
5.  Bits and Parity: 8 bits, no parity (must match)
6.  Stop Bit: 1 stop bit (must match)
7.  Print Region: Print Full Page
8.  Printed Data Type: National Only
9.  Print Terminator: No Terminator

Terminal Type and Device File

You will also need appropriate entries in the Terminal Type and Device files. The following examples are known to work with either the Trakker or the MedTester.

In the Terminal Type file: NAME: C-BCAUX(VT320)

OPEN PRINTER PORT: W \*27,"\[5i" CLOSE PRINTER PORT: W \*27,"\[4i"

In the Device file:

NAME: BCAUX(VT320)

\$I: 0

LOCATION OF TERMINAL: HOME (AUX PORT) SUBTYPE: C-BCAUX(VT320)

When prompted for the "device to which the Trakker (or MedTester) is connected" you should select "BCAUX(VT320)".

### A.3. Downloading and Uploading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data acquired and stored on the Trakker or the MedTester is uploaded to VISTA to update the facility database. Uploading may be done at the end of each workday, or at other convenient intervals. Both of the Trakker downloading programs will warn the user if the Trakker is about to run out of storage space. If you see this warning, you should plan to upload your data as soon as possible.

Trakker 9440 Bar Code Reader

The Trakker 9440 portable bar code reader can be programmed using a language called IRL. Only one IRL program can reside on a Trakker at any given time.

Trakkers that are used for more than one application will need to be downloaded with the correct IRL program whenever the application changes.

Engineering includes two (2) IRL programs. The programs are:

1.  ENNX for bar code-based equipment inventory
2.  ENPM for bar code based Preventive Maintenance Inspection.

The Engineering Menu Options for downloading and uploading between Trakkers and VISTA are:

1.  Download NX Program to Portable Bar code Reader (ENBCNXDNLD)
2.  Download PM Program to Portable Bar code Reader (ENBCPMDNLD)
3.  Upload Date from Portable Bar code Reader (ENBCUPLD)

Note that the same option (ENBCUPLD) is used for uploading either equipment inventory data or PMI data. The content of the uploaded data set allows VISTA to automatically determine what the data represents and how it is to be processed.

MedTester Electrical Safety Analyzer

The Engineering Menu Option for uploading data from a MedTester to VISTA is "Upload Data from MedTester" (ENSA1).

SPECIAL NOTES

Although the PRINTER port of a MedTester has a DB-25 connector, it is a parallel (and not a serial) interface. Connection of MedTesters with VISTA must be accomplished via a MedTester COMM port.

It is believed that the MedTester 5000 does not support the XON/XOFF data communication protocol. This should not be a serious problem, but it does have the following implications:

1.  If you are connecting a MedTester to the aux port of a CRT, the baud rate of the aux port must not be faster than the baud rate of the CRTs main communication port.
2.  If it appears that you are losing characters in the data upload process, you may be able to solve the problem by reducing the baud rate.

### A.4. Bar Code Based Equipment Inventory of Nonexpendable (NX) Equipment and Preventive Maintenance Inspections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A data acquisition program must be downloaded to your portable bar code reader. For Equipment Inventory use menu option "Download NX Program to Portable Bar Code Reader" (ENBCNXDNLD ); for Preventive Maintenance Inspections use menu option "Download PM Program to Portable Bar Code Reader" (ENBCPMDNLD). If you need a detailed explanation of this process, please refer to the section entitled *Using Portable Bar Code Readers and Electrical Safety Analyzers with VISTA.*

Whenever you turn on a Trakker, it should execute a self-test and then display a "Ready" prompt. To begin, you should:

1.  Simultaneously hold down the \<CTRL \> key and press \<Enter \>
2.  Press \<B\> (for "begin").

If you find this start-up sequence cumbersome, you may wish to print the sequence in bar code and affix the label to the Trakker. Then you will be able to perform the startup sequence simply by scanning this label.

If data is already stored on your Trakker you will see a message that looks something like the following.

\*\*\* WARNING \*\*\* Data exists on

this bar code reader. The first record in this file

is ID SAW9.21.90?

Do you want to purge this file...

...(Y/N)?

The first record in a Trakker file is called the File ID. If a Trakker file exists, the File ID will appear on the sixth line of the Trakker start-up message, immediately to the right of the character string "ID" (as shown above). Users of Trakkers will key in this File ID before beginning to collect data. File IDs should normally consist of the user's initials and the date. This way, if you happen to start up a Trakker that someone else has been using you can immediately tell who was using it and when.

You will need to respond to the "Do you want to purge this file?" prompt. Say \< N\> if you want to add to the data already stored; \<Y\> if you want to delete what's there and start fresh.

If there is no stored data, or if there is data and you purge it, the Trakker will prompt you for a File ID. Please enter your initials and the current date. No special format is required, and the Trakker will accept and store virtually anything that does not exceed 37 characters.

There may be times when you cannot successfully scan a bar code label. Perhaps it is torn, smudged, or otherwise damaged. When this happens you can use the Trakker keyboard to enter data. Both location labels and equipment labels have the bar-coded data printed in human readable form directly below the bar code. Be sure to key in all the characters (including spaces and hyphens) exactly as they appear on the label. To enter a hyphen, first press the \< ALT\> key and then the

\<Space \> key. Location labels should look something like "SP201-110A". Equipment labels should be of the form "999EE12409".

In these two examples, "SP" and "EE" are what is known as "application codes"; "201" is a room number; "110A" is a building number; "999" is a station number; and "12409" is the ENTRY NUMBER of a particular piece of equipment in the Equipment file.

If a piece of equipment does not have a bar code label but does have a PM (Property Management) label; you may use the Trakker keypad to enter the PM Number. Be sure to include the hyphen. All entries of the form "nnnn-nnnn" or "nnnn-nnnna" (where "n" can be any digit and "a" can be any alphabetic character) will be interpreted by the Trakker as a PM Number. Examples might include "7025-0908" and/or "70250908A".

> **NOTE:** The quotation marks in the examples given above are used purely to enhance the readability of this document. You should not include quotation marks when keying data into the Trakker.

If a piece of equipment does not have either a bar code label or a PM label, you can still capture it in your inventory. Press the key labeled \< F4\>. It is at the upper right corner of the keypad. The Trakker will automatically prompt you for MODEL, SERIAL NUMBER, and DESCRIPTION. The description may not exceed forty characters in length. If there is a VISTA equipment record whose MODEL and SERIAL NUMBER match your entries, the Engineering package will update that record.

To exit an option and get back to the Trakker's main menu, enter a period (\<.\>). Equipment Inventory

The VISTA Equipment Management module has been designed for use with Building Service Equipment as well as Non-Expendable (or CMR) Equipment. It is also used with personal property that is not classified as non-expendable by

Acquisition and Materiel Management Service but requires routine tracking and inspection by Engineering Service to meet quality assurance requirements (i.e., JCAHO, NFPA). It is quite permissible for expendable equipment to be included in the Equipment file.

The Trakker will display the station number that was downloaded as part of the data acquisition program. If what you see displayed does not match your station number, contact your Application Coordinator and/or your Information Resources Management Service before proceeding.

At some point in the inventory process, you will probably want to perform an "Inventory Exception Listing" (menu option ENBCNXCMR). This option will look at the equipment record of every item on the subject CMR and list all those that were NOT located during the current inventory. This listing is called an Exception List.

> **NOTE:** Items whose USE STATUS is "TURNED IN" or "LOST OR STOLEN"

will NOT appear on CMR Exception Lists.

The starting date of the current inventory is specified by the user at the time the option is run. The default will be the first day of the current month, but any date may be selected. The ending date is always the date on which the option is run.

Preventive Maintenance Inspections

The intent of bar-coded PMI functionality is to provide a tool that can be used to improve the accuracy and timeliness with which PM worklists are closed out. Whenever bar code readers are used in posting completed PMIs to Equipment Histories, the LOCATION and PHYSICAL INVENTORY DATE fields in the equipment record will be updated automatically.

Note that when downloading the PMI data acquisition program to a portable bar code reader, you will be required to select a PM Inspector from the Engineering Employee file. This is the individual whose name will be recorded in the WORKER field of the Equipment History. The wage rate of this individual (as stored in the Engineering Employee file) will be used to compute chargeable labor costs. If two or more technicians are to share the same bar code reader, then a download of the PMI data acquisition program must be performed each time the bar code reader changes hands. It is always necessary to upload any existing data BEFORE downloading a data acquisition program. Uploading and downloading operations should not take more than a few minutes.

The Trakker will display your station number, followed by the PM Inspector of Record. Both of these data elements are downloaded as part of the data acquisition.

program. If the station number that you see displayed does not match your station number or if the PM Inspector shown is not what you intended to download, you should repeat the download procedure and/or contact your Engineering Application Coordinator or Information Resources Management Service before proceeding.

Once basic inventory information has been updated, the Engineering package will post the PM inspection. A check is first made of the existing Equipment History. If a PMI of the type specified in the selection of a PM worklist has already been posted, no action will be taken. In other words, if you're using a Trakker to close out a MONTHLY worklist for a specific shop and a MONTHLY PM inspection by that shop has already been posted for the piece of equipment in question; then the data uploaded from the Trakker will have no effect except to update LOCATION, PREVIOUS LOCATION, and PHYSICAL INVENTORY DATE.

If the PMI has not already been posted, the system checks to see if there is an open PM work order. If so (and if the equipment PASSED its PMI), the PM work order is closed and posted. If time and material costs were entered into the Trakker, these uploaded data elements will be used in closing the PM work order. If time and materials were not recorded, the default values (if present) will be used.

If the piece of equipment FAILED its PMI, notification will be provided in the form of a PMI Exception Message. The PM work order will be referenced in the Exception Message, but it will not be closed, and nothing will be posted to the Equipment History.

If a PMI has not already been posted and there is no open PM work order, the system will attempt to post the PMI directly to the Equipment History. It is possible to use a Trakker to close out a PM worklist that hasn't been generated. If you were to do this and then generate the worklist, equipment for which PMIs had already been posted via the Trakker would not appear on your worklist. Perhaps one could view this as a crude step in the direction of "area maintenance".

A piece of equipment should never simply FAIL a Preventive Maintenance Inspection. When equipment does not PASS a PMI, a regular work order should be issued to correct the problem (unless a decision is made to TURN-IN the equipment instead). When the PM work order is finally closed, its status should be "CORRECTIVE ACTION TAKEN/REQUESTED" and its WORK PERFORMED

field should contain a reference to the regular work order.

### A.5. Using the Bar Code Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trakker will now give you the appropriate options. Option 1 is different for each task while options 2 and 3 operate similarly.

Equipment Inventory ................................ ................................ ........................

Preventive Maintenance Inspection

1\. Take Inventory.......................................................................................................

1.  Record PMI

2\. Transmit Data .......................................................................................................

2.  Transmit Data

3\. Review/Delete ........................................................................................................

3.  Review/Delete

Option 1Take Inventory is used to acquire and store equipment inventory data. The process is begun by scanning the location label found on the doorjamb of the main entrance to the room that you wish to inventory. This "opens" that particular location. You should then scan the bar-coded equipment label on each piece of equipment found in that room. When all equipment labels in the open location have been scanned, you should scan the location label again as you leave the room. This tells the Trakker to "close" that location.

Record PMI is used to acquire and store preventive maintenance data. The process is begun by scanning the location label found on the doorjamb of the main entrance to the room where the equipment to be inspected is located. This "opens" that particular location.

Scan the bar-coded equipment label on the first piece of equipment to be inspected. The Trakker prompts you as follows:

Enter P for PASS or F for FAIL:

If you enter \<P\>, you will see the following:

Press F1 for detail or ENTER to cont...

If you press the \<F1\> key (located at the upper left corner of the keypad), the Trakker will prompt you for time and materials. Please enter time in hours (use no more than two decimal places) and material costs in dollars. It is recommended that you round off to the nearest whole dollar, but decimal numbers are accepted.

If you press \<Enter \> instead of \<F1\>, the Trakker will prompt you for the next equipment label.

Reader ready...

If you enter \<F\> in response to the following prompt,

Enter P for PASS or F for FAIL:

you will be asked to describe the problem that caused the piece of equipment to fail its PMI. The exact prompts will look like the following.

Describe problem (40 char max):

Time (hours):

When you reach the point where there is no more equipment to be inspected in the open location, you should scan the location label again as you leave the room. This tells the Trakker to "close" that location.

Option 2Transmit Data is used to transfer data collected and stored on a Trakker up to VISTA. The process is called "uploading" and is fully described in the section entitled *Using Portable Bar Code Readers and Electrical Safety Analyzers with VISTA.*Option 3Review/Delete is used to examine (and perhaps delete) data stored on a Trakker. If you select this option, the Trakker will immediately display the last data element that was entered. You will be prompted to enter \< D\> to delete the data element, \< Q\> to go back to the main menu, or \< C\> to display the next previous data element. If you choose to delete a data element, the Trakker will replace it with the character string "\*\*\*\*\*". When data is uploaded from the Trakker to VISTA, the Engineering package will ignore any such data elements.

This feature can be especially useful if you are interrupted while using the Trakker. Trakkers are normally programmed to turn themselves off after a period of inactivity in order to conserve battery power. If this happens and you forget exactly where you were in the data acquisition process, use the Review/Delete option to look at the last few data elements.

When you transfer data from a Trakker up to VISTA it is stored in the "DATE/TIME OF DATA UPLOAD" (multiple) field of the Bar code file. The file used for Equipment Inventory is called "NON-EXPENDABLE" and its IDENTIFIER field is "ENNX". The file used for Preventive maintenance Inspections is called.

"PREVENTIVE MAINTENANCE" and its IDENTIFIER field is "ENPM". The

Engineering package will automatically recognize the type of data that has been uploaded and will give you a choice of either processing the data set immediately or queuing this task. More specifically, the system will echo the number of records read and then prompt you either for the identity of the PM worklist you wish to close out or for a device on which to print "Exception Messages" (by entering the letter \< Q\> and then a device, you can schedule the data processing task to run during non-peak hours).

> **NOTE:** If the bar code reader contains completed PMIs for equipment that is not on the subject worklist, the PMIs will be posted directly to the Equipment Histories. A PM work order will not be created in these cases. If the subject worklist is subsequently generated (or re-generated), this equipment will not appear.

Exception Messages are a means of notifying you of situations that may require special attention. These situations will include missing bar code labels, data base inconsistencies, "foreign" (belonging to another VA facility) equipment or instances where a piece of equipment did not pass the PMI..

If a piece of equipment was recorded by means of its PM number or physical description, the bar code label is presumed to be missing. If the system attempts to process what appears to be an equipment label and no corresponding equipment record can be found, notice of a possible data base inconsistency will be given. If the station number of an equipment label does not match the station number of the host facility, that piece of equipment is recognized as belonging to another VA site.

In processing an equipment inventory data set, the following updates are made:

1.  The existing content of the LOCATION field is moved to a field called PREVIOUS LOCATION,
2.  The current location (from the Trakker) is placed in the LOCATION field, and
3.  The current date (the date on which inventory data is processed by the Engineering package) is recorded as the PHYSICAL INVENTORY DATE.

If another user is editing an equipment record at precisely the time when this automatic update is attempting to run, you will receive a PMI Exception Message to that effect. You should perform a manual update of any such records to ensure that they are complete and correct. Menu options "Manual Update of Equipment Inventory" (ENBCNXMAN) and "Record Single Device PMI" (ENPMR3) may be used for this purpose.

### A.6. Electrical Safety Analyzer Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Engineering package contains the software necessary for acquiring and processing data from an automated electrical safety analyzer (ESA). These data may be used to:

1.  close out individual PM work orders on a PM worklist
2.  post electrical safety inspections directly to Equipment Histories

This module is designed to work with the MedTester 5000 (or equivalent), manufactured by Dynatech Nevada. This device happened to be the only automated electrical safety analyzer that was commercially available when the Engineering package was developed. The ANYCITY Information Systems Center is committed to the development of similar interfaces for any and all commercially available automated electrical safety analyzers. An interface for the TurboTester, manufactured by Biotech Incorporated, is currently in progress.

The overall sequence of events is as follows:

1.  upload all data.
2.  examine and process each individual test.

Before the data processing task is begun, users of this module will be asked:

1.  whether or not ESA data is to be used in conjunction with a PM worklist (if so, the user is also asked to specify the worklist)
2.  which device is to be used for printing "Exception Messages”?
3.  whether or not paper copies of test results are desired

The following information is needed to specify a particular PM worklist.

1.  the Engineering shops.
2.  the month and year
3.  the type of worklist (MONTHLY or WEEKLY)
4.  in the case of a WEEKLY worklist, the week number (1 through 5)

Exception Messages are intended to inform the user of situations that may require special attention. They will be generated when:

1.  the equipment under test (EUT) does not seem to exist in the Equipment file.
2.  the equipment record of the EUT is being edited by another user.
3.  the EUT has failed to pass its inspection.

An Exception Message is also generated if an ESA test has already been used to close out a PM work order from the specified worklist for the EUT. In such a case, the Equipment History will remain unchanged.

If you have opted to get a paper copy of all test results, the copies will be printed as the uploaded data is being processed. Specific test results will not be stored within

the Engineering package. The fact that the EUT passed an electrical safety inspection will be posted to the Equipment History. These postings should be sufficient for Equipment Management purposes. Sites are encouraged NOT to keep paper records of specific electrical safety tests.

The physical connection of the MedTester ESA to your VISTA system is explained in the section entitled *Using Portable Bar Code Readers and Electrical Safety Analyzers with VISTA*. Users of the MedTester can program the instrument (via the CONFIG sub-option of the CASO option) to prompt for any or all of the following data elements:

1.  OPERATOR CODE
2.  DEVICE TYPE
3.  MANUFACTURER CODE
4.  LOCATION
5.  MODEL NUMBER
6.  SERIAL NUMBER
7.  CONTROL NUMBER
8.  PHYSICAL INSPECTION

The OPERATOR CODE may not exceed six (6) characters in length. If this data element is present, the Engineering package will interpret it as the internal entry number of the electrical safety inspector in the Eng Employee file. Sites may obtain this information by using the FileMan print option. Specify NAME and NUMBER when prompted for print fields.

Other data elements that have particular meaning to the Engineering package are LOCATION, MODEL NUMBER, SERIAL NUMBER, and CONTROL NUMBER.

The maximum length for each of these MedTester data elements is sixteen (16) characters.

LOCATION should conform to conventions established for the Eng Space file. The proper format is ROOM-BUILDING-DIVISION (where DIVISION is optional).

It is possible to enter LOCATION into the MedTester by scanning bar coded location labels produced with the package. This may not be as convenient as it sounds, because the electrical safety inspector would need to reach the location label with a scanning wand while the MedTester was plugged in and close to the EUT. If LOCATION is entered by scanning location labels, the Engineering package will automatically strip off the two-character application code ("SP" in this case) before updating the equipment record.

EXAMPLE: Room 234 of Building 114 would be scanned in as "SP234-114" but would be posted to the equipment record as "234-114".

Once ESA data have been physically uploaded from the MedTester and the user has specified how these data are to be processed, the system will begin to look at individual test records. At this point, all uploaded data will reside on VISTA in a temporary storage area.

The first order of business is to identify the EUT. This is normally done on the basis of the Control Number that's entered into the MedTester by the electrical safety inspector immediately before the actual test sequence begins. The easiest way of entering control Numbers is by scanning a bar coded equipment label. Bar code wands are available (as a hardware option) for MedTesters. You may also enter either the PM Number (ex: "7025-9802") or the exact content of the bar-coded equipment label (ex: "680 EE1209") via the MedTester keyboard.

> **NOTE:** The quotation marks that appear above are intended solely to enhance the readability of this document. You should not enter these quotation marks into the MedTester.

Instead of (or in addition to) the Control Number, users of the MedTester may enter Model Number and Serial Number.

If the Control Number exists and looks like a bar coded equipment label, the system will attempt a direct look-up within the Equipment file. If the Control Number looks like a VA PM Number, the system will try a look-up using the appropriate cross-reference of the Equipment file. If the Control Number does not exist or does not look like a bar coded equipment label or VA PM Number, the system will attempt to look-up the EUT using Model Number and Serial Number. If this attempt is unsuccessful (either because these data elements were not entered into the ESA or because they can't be found in the Equipment file) the system will generate an Exception Message and move on to the next test record.

If look-up by Control Number is successful (either directly or by PM Number) and if Model Number and Serial Number were uploaded from the ESA, the system will compare the Model Number and Serial Number from the ESA with what is on file in the equipment record. Discrepancies will be reported in the form of Exception Messages. The content of the Control Number will be presumed correct.

If the EUT can be identified in the equipment file, its equipment record is updated as follows:

1.  The current LOCATION in the equipment record is moved to the field called PREVIOUS LOCATION.
2.  The LOCATION data element from the MedTester is stored in the LOCATION field of the equipment record.
3.  The date on which the electrical safety test was actually performed is stored in the PHYSICAL INVENTORY DATE field of the equipment record (this date is automatically captured by the MedTester and included as part of the uploaded test results).

If the uploaded test results are to be processed in conjunction with a PM worklist, the system will check the Equipment History to see if the specified PMI has already been recorded. If so, an Exception Message is generated (more for information than for action) and the Equipment History is left unchanged. If not, the system checks the Work Order file for an open PM work order of the specified type. If there is one (and assuming that the EUT did not fail its test), the system will now close it out. If a PM work order of the specified type does not exist, the system will post the performance of an electrical safety inspection directly to the Equipment History.

If an OPERATOR CODE equal to the internal entry number of a record in the Eng Employee file was uploaded from the MedTester, then the NAME of this Eng Employee will be posted as the WORKER and his salary (from the Eng Employee file) will be used to compute the LABOR COST. OPERATOR CODE will override any default value (in the form of RESPONSIBLE TECHNICIAN) that is established when a PM work order is originally generated.

If the EUT failed its test sequence, an Exception Message is generated, and the relevant PM work order (if one exists) will not be closed out. Nothing will be posted to the Equipment History. Comments entered by the electrical safety inspector into the ESA will be included in the Exception Message.

Test limits for resistance, case leakage, lead leakage, and isolation leakage are programmed into the MedTester. If these values (which can be modified on site) are exceeded by the EUT, test failure is automatic.

The electric safety inspector can cause any test to be interpreted as a failure by beginning his MedTester COMMENTS with the pound sign (#).

EXAMPLE: If a piece of equipment has a worn or frayed power cord but does not yet exceed the maximum allowable leakage currents, the PMI inspector may wish to enter the following comment:

\#POWER CORD MUST BE REPLACED

MedTester COMMENTS may not exceed forty (40) characters.

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2162 REPORT OF ACCIDENT, 2, 7
5-Yr Plan, 3, 43, 44, 46, 48, 53, 54, 55, 65, 66, 67
A/E-Contractor, 115, 122
Accept IT Responsibility, 8, 324, 334
Accountable NX for Station, 206, 207, 208
Acquisition Data Edit, 214, 215, 221
Activations, 3, 43, 45, 46, 49, 53, 54, 65, 66, 67, 68, 69, 71, 79, 80, 81, 84, 85, 91, 94, 95, 96
Actual Dates Screen, 114
Add Entry to New Person File, 328
Additional Survey Listing, 270
Adjustment Voucher Report, 230
Approval of Project, 84
Approved Dates Screen, 111
Archive, 6, 245, 247, 248, 250, 253, 254, 256, 258, 259, 260, 261, 262, 263, 264, 271
Archive & Verify, 6, 260, 261
Assign (Transfer) Electronic Work Orders, 7, 10, 10, 13, 43, 68, 128, 244, 272, 307, 317
Assign Responsibility, 322
Assignment Inquiry, 8, 329, 333, 334, 337
Assignments Pending Acceptance Report, 8, 329, 330, 331
Auto Print New, 256
Bar Code Labels, 187
Bar Coded Equipment Inventory, 5, 128, 129, 130, 141, 142, 144, 145, 164, 171, 176, 188, 192, 193, 194, 196, 197, 198, 201, 202
Bar Coded PMI Functions, 4, 176, 177, 182, 183, 184
Batch Send FA Documents by CMR, 218
Batch Send FA Documents by Station, 219
BERS Survey File, 6, 264
Better An Equipment Record, 214, 215, 220
Building Data, 297
Building File, 294
BUILDING FILE, 298, 300
Building Management RCS 10-203, VAF 10-6007a, 6, 280, 286
Building Space Survey, 6, 279, 284
Building/Project Space Plan, 305
Category Stock Number Enter/Edit, 213
Ceiling Replacement, 278
Certify Hard Copy Signature, 325
Changes & Remarks, 117
Check of Equipment Capitalization, 209
CITATIONS, 50
Close Out PM Work Orders, 177
CMR File Enter/Edit, 212
CMR Inventory, 149
Computer Port, 245
Contract Survey Listing, 269
Contractor Data, 116
Dangling Pointers in LOCK File, 294
Delete Archive Global, 6, 260, 262
Direct Posting to Equipment Histories, 159
Disapprove Work Order, 35
Display 2162 Report, 314
Display Equipment Category PM Schedule, 164
Display Equipment Record, 143
Display Work Order, 24
Disposition an Asset, 221
Document History (FAP) for Equipment, 231
Download NX Program, 194, 319
Download PM Program, 4, 182, 346
Edit 2162 Report, 314
Edit Work Order Data, 18
Electrical Safety Analyzer, 353
Electrical Safety Analyzers, 340
Employee File, 247
Employee List, 289
Eng Site Parameters, 254
Enter Project Data, 98
Enter/Edit PM Procedure, 170
Environmental Analysis, 81
Equipment Category Inventory, 151
Equipment Category PM Schedule, 168, 250
Equipment History, 4, 5, 8, 22, 34, 145, 146, 160, 172, 180, 181, 185, 186, 206, 319, 320, 349, 350, 354, 356
Equipment Labels, 188, 210
Equipment Management, 8, 128, *See* Bar Code Labels
EQUIPMENT MANAGEMENT, 3
Equipment Not Reported to FAP, 228, 232
Equipment Replacement Template, 256
Equipment Reports, 144
Excessed Equipment Report, 228, 233
EXPANDED PM WORK ORDERS, 257
Export Facility Management Data, 7, 272, 273, 286, 290, 291, 292, 293, 297, 301
Facility Management, 9, 272
FACILITY MANAGEMENT, 6
Failure Rate Report, 145, 157
FAP Documents, 214, 217, 219, 221, 222, 223, 224, 225, 226, 227, 228
FAP Validity Check By CMR, 216, 224
FAP Validity Check by Station, 216, 225
FAP Validity Check For A Single Item, 224
FB Document, 214
FD Document, 222
Financial Data Edit, 223
Find & Assemble Records, 260
Fixed Assets Reports, 204, 227
Floor Replacement, 279
FR Document, 214, 216, 223
Function Space Survey, 279, 283
General Survey Listing, 269
Generate PM Schedule, 171
Incomplete Work Orders, 3, 29, 30, 31, 32, 339
Individual Responsibility for IT Assets, 329, 335
Inventory, 130, 140, 142, 145, 147, 148, 149, 207, 211, 320
Inventory Edit (IT), 320
Inventory Exception Listing, 196
Inventory Listing, 149, 151, 152, 153, 154
IT Equipment Module, 319
IT EQUIPMENT MODULE, 8
IT Equipment Report Menu, 329
IT Equipment Responsibility, 322
IT Owner Menu, 334
IT OWNER MENU, 8
Key Distribution by Employee, 287, 288
Key/Lock Management, 286
Leased Space, 297, 300
Location Inventory, 152, 207
Location Labels, 191, 211
Lock Number File, 288
Manual Update of Equipment Inventory, 194, 197, 205
Manufacturer, 253
MedTester, 177, 184
Menu Structure, 2
Minor/Minor Misc Prioritization, 3, 86, 89
Multiple Inventory. *See* Inventory
National EIL Enter/Edit, 211, 214
Nonexpendable Equipment, 9, 211
NONEXPENDABLE EQUIPMENT, 5
Non-Space File Location Report, 274, 321
NRM Prioritization Scoring Sheet, 91
NSF Spreadsheet, 290, 291
Personnel Survey Listing, 268
Planning Space Program, 301
PM DEVICE TYPE IDENTIFIER, 258
PM Parameters, 163
PM Sort, 256
PM Workload Analysis, 158
Portable Bar Code Reader, 194
Portable Bar Code Readers, 340
Preventive Maintenance Inspections, 346
Print Bar Codes On W.O., 256
Print Employee List by Service, 7, 287, 289
Print Employee List sorted by Key, 7, 287
Print Equip. History, 34
Print Hand Receipt for an Individual, 327
Print PM Manhours, 38
Print PM Procedure, 165
Print Project Status Report, 118
Priority points, 90
Program Management, 244
PROGRAM MANAGEMENT, 6
Project Application. *See* Approval of Project
Project Application Reports, 84
Project Application VAF, 3, 86
Project Applications, 68
Rapid Closeout of PM Work Orders, 176, 179
Rapid Deferral of PM Worklist, 177, 185
RCS 10-0141 Report, 279
RCS 10-0141 spreadsheet, 292
RCS 10-0141 Spreadsheet, 290
Recalculate FAP Balances, 216, 227
Recall Archive, 262
Record Equipment PMI, 175
Record Single Device PMI, 177, 180
Replacement Listing, 145, 156, 207
Replacement Schedules, 273, 277
Reprint Work Orders, 36
Responsible Shop Inventory, 153, *See* Inventory
Review Activity Log, 263
Revised Dates, 113
Room Data, 273, 277, 320
Room Space, 273, 274
Room/Keying/Function Report, 279, 280
SAFETY PRINTOUT, 258
Section List, 245
Send a Single FA Document, 217
Signature Exception Report, 332
Software Options, 256
Space Functions File, 293
Space Management, 273
Space Survey by Room, 279
Space Survey Printout, 257
Space Survey Report Menu, 273, 279
Space Utilities, 293
Space/Facility Management. *See* Facility Management
Specific Device PM Schedule, 164, 165
Specific Equipment History. *See* Equipment History, *See* Equipment History
Summary of SGL Balances, 228, 233
Terminate Responsibility, 324
Tracked IT Assets Report, 332
Trakker, 340
Transaction Register, 228, 234
TRANSACTION STATUS REPORT, 25
Transfer Responsibility, 324
Transfer W.O., 33
Transmit 10-0051 Electronically, 122
Transmit Project Applications, 95
Unassigned IT Asset Report, 329
Upload Data, 184, 195
Uploaded NX Inventory Data, 194, 198
Use Status Inventory, 149, 154, *See* Inventory
Using Service Inventory, 153, *See* Inventory
Validate 5-Yr Plan. *See* 5-Yr Plan, *See* 5-Yr Plan
Validate Project Applications, 94
Voucher Summary for Station, 227, 228
Wall Replacement, 278
Warranty List, 145, 155
Work Action, 270
Work Center Code, 248
Work Order and MERS, 7
WORK ORDER HISTORY, 35
