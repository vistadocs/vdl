---
title: CP Flowsheets - Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: plain
doc_subject: CP Flowsheets
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - strong
  - view
  - flowsheet
  - flowsheets
  - class
  - contents
  - table
  - implementation
  - console
  - guide
page_count: 0
word_count: 21260
section_count: 27
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/md_1_p77_impg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/md_1_p77_impg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](cp-flowsheets-implementation-guide/001.png)

Clinical Flow Sheet CliO V2

Implementation GuideMD\*1.0\*77May 2021Department of Veterans AffairsOffice of Information &Technology (OIT)Product Development

This page intentionally left blank for double-sided printing

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Implementation Guide](#implementation-guide)
  - [Product Benefits](#product-benefits)
    - [CP Gateway Service](#cp-gateway-service)
    - [CliO Database](#clio-database)
    - [Terminology Mapping](#terminology-mapping)
  - [CP Flowsheets](#cp-flowsheets)
  - [CP Console](#cp-console)
  - [Intended Audience](#intended-audience)
  - [CP Console Implementation](#cp-console-implementation)
- [Pre-Implementation Planning](#pre-implementation-planning)
  - [General Guidance](#general-guidance)
  - [Software](#software)
  - [Flowsheet Design](#flowsheet-design)
  - [Flowsheet Coordinators](#flowsheet-coordinators)
  - [Contingency Plans](#contingency-plans)
- [CP Console Overview](#cp-console-overview)
  - [CP Console Menu Bar](#cp-console-menu-bar)
    - [File Menu](#file-menu)
    - [Tools Menu](#tools-menu)
    - [Help Menu](#help-menu)
  - [CP Console Tree View](#cp-console-tree-view)
  - [CP Console Detail Area](#cp-console-detail-area)
- [Working with Clinical Flowsheet Views](#working-with-clinical-flowsheet-views)
  - [Importing Views from XML](#importing-views-from-xml)
  - [Customizing Flowsheet Views](#customizing-flowsheet-views)
    - [Making a Copy](#making-a-copy)
    - [Creating a New Flowsheet View](#creating-a-new-flowsheet-view)
    - [### View Terminology Editor](#view-terminology-editor)
    - [Adding Terms to a View](#adding-terms-to-a-view)
    - [Working with Qualifiers](#working-with-qualifiers)
    - [Changing the Display Order of Terms in a View](#changing-the-display-order-of-terms-in-a-view)
    - [Modifying Terms in a View](#modifying-terms-in-a-view)
    - [Removing Terms from a View](#removing-terms-from-a-view)
- [Creating Flowsheets in CP Console](#creating-flowsheets-in-cp-console)
  - [Adding a new Flowsheet](#adding-a-new-flowsheet)
    - [Adding a View to a Flowsheet](#adding-a-view-to-a-flowsheet)
    - [Pages Tab](#pages-tab)
    - [Editing a View Type in a Flowsheet](#editing-a-view-type-in-a-flowsheet)
    - [Removing a View from a Flowsheet](#removing-a-view-from-a-flowsheet)
    - [Changing the Display Order of Views in a Flowsheet](#changing-the-display-order-of-views-in-a-flowsheet)
  - [Creating a Flowsheet Total](#creating-a-flowsheet-total)
    - [Editing the Flowsheet Total](#editing-the-flowsheet-total)
    - [Totals Tab](#totals-tab)
  - [Flowsheet Total](#flowsheet-total)
    - [Understanding Totals Display](#understanding-totals-display)
  - [Setting up Default Shifts](#setting-up-default-shifts)
- [Additional Flowsheet Tasks](#additional-flowsheet-tasks)
  - [Setting up Background Tasks](#setting-up-background-tasks)
    - [CliO Cleanup](#clio-cleanup)
    - [CP Cleanup](#cp-cleanup)
    - [HL7 Cleanup](#hl7-cleanup)
  - [Adding an Instrument](#adding-an-instrument)
    - [Modifying an Existing Instrument](#modifying-an-existing-instrument)
    - [Instrument Definitions](#instrument-definitions)
    - [Attachment Processing](#attachment-processing)
    - [Adding a Configuration for a Bi-Directional Instrument](#adding-a-configuration-for-a-bi-directional-instrument)
  - [Working with Parameters](#working-with-parameters)
    - [CP Parameters](#cp-parameters)
    - [Administering Notification Lists](#administering-notification-lists)
  - [CP ADT Feed Configuration](#cp-adt-feed-configuration)
    - [Current ADT Targets](#current-adt-targets)
    - [Adding an ADT Target](#adding-an-adt-target)
  - [CP Gateway Service Configuration](#cp-gateway-service-configuration)
    - [VistA Server Settings](#vista-server-settings)
    - [Gateway Server Settings](#gateway-server-settings)
  - [Working with Procedure Information](#working-with-procedure-information)
    - [Adding a Procedure](#adding-a-procedure)
    - [Modifying an Existing Procedure](#modifying-an-existing-procedure)
    - [Procedure Definitions](#procedure-definitions)
    - [Allowable Instruments](#allowable-instruments)
    - [Working with the Procedure Worksheet](#working-with-the-procedure-worksheet)
    - [Adding Allowable Instruments](#adding-allowable-instruments)
- [Shortcut Keys](#shortcut-keys)
- [# Glossary](#glossary)
- [Index](#index)
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 56%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>May 2021</td>
<td><p>MD*1.0*77:</p>
<ul>
<li><p>Rearranged the Revision History Table</p></li>
<li><p>Replaced the terminology information site link with the new <strong><u>site</u></strong> link</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>March 2016</td>
<td>Patch MD*1.0*42: Added Section 6.2.4.1, <em>Configuring a Bi-Directional Instrument to Receive Data Only</em> (page <a href="#configuring-a-bi-directional-instrument-to-receive-data-only"><u>64</u></a>).</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>January 2012</td>
<td><p>Deleted sections 3.1.2.4, 3.1.2.5 and 3.1.2.6 and edited section 3.2.1.3 to update Folder View Permissions.</p>
<p>Added sections 6.2.1.1 and 6.6.2.1 describing Make Copy for Instruments and Procedures.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>December 2011</td>
<td>Added note and graphic to step 4 of Section 4.2.7, Modifying Terms in a View. Added new section 3.1.2.3 CP Console Folder View Permissions. Added note to section 3.1.2.8 Export to XML. Added note to section 4.1 Importing Views from XML.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2011</td>
<td>Section 5.2, Creating a Flowsheet Total, replaced figure 5-10, Totals Display from CP Flowsheets. Section 4.1, Importing Views from XML, replaced MD1_0P16_Default_Views.xml with MD1_0P16_Sample_Views.xml. Removed section 5.4.2, Changing the Schedule for a Task.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 2011</td>
<td>Section 5.3.1, Understanding Totals Display, changed “median” of all observations to “average “ of all observations.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2011</td>
<td>Section 5.1, Adding a New Flowsheet: added new step 4 after note, revised step 5.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 2011</td>
<td>Added note about TIU Note Title for Reporting field to section 5.1, step 4.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2011</td>
<td>Added note in section 6.2 regarding legacy devices</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>April 2011</td>
<td>Patch MD*1*16 Released</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
This page intentionally left blank for double-sided printing

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation Guide provides technical information for the implementation of the Clinical Procedures Flowsheets Module. This document provides guidance for Information Resource Management (IRM) technical personnel, Clinical Application Coordinators (CACs), and Flowsheet Coordinators to implement and operate the software. More information can be found in the *Clinical Procedures* (*CP) V1.0 Flowsheets Module User Manual*.

## Product Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Flowsheets patch of the Clinical Procedures (CP) package provides an electronic representation of the traditional paper flowsheet maintained during each inpatient stay. Vitals, Intake/Output, and Wound Documentation are examples of data types that can be recorded via Clinical Flowsheets into the Veterans Health Information System and Technology Architecture (VistA) system. Clinical Flowsheets provides a departure from its predecessor applications by storing collected information as discrete data. Some data elements, such as vital signs, are available to the Vitals Package and Computerized Patient Record System (CPRS). Various reports built on the other data elements are available for CPRS in the form of Text Integration Utilities (TIU) Notes. Additionally, flowsheets is a tool that can be used by clinicians to standardize assessment templates.

There are two ways to enter data into Clinical Flowsheets: manually and via Health Level 7 (HL7) messaging. Any instrument or external system capable of sending HL7 messages can be considered a source of data for Clinical Flowsheets (provided that the HL7 messages conform to Clinical Flowsheets requirements).

Clinical Flowsheets uses VistA Data Extraction Framework (VDEF) support, HL7 messaging, and the CP Gateway service to notify the medical device of the patient’s admission, discharge, and transfer.

MD\*1.0\*16 consists of the following three windows executables components and one Kernel Installation & Distribution System (KIDS) build:

- CPConsole.exe
- CPFlowsheets.exe
- CPGatewayService.exe
- MD1_0P16.KID

### CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Gateway Service is the component that processes HL7 messages.

The CP Gateway Service is composed of two subsystems, one existing solely within VistA, and the other existing as a Windows service that interacts with VistA via the Remote Procedure Call (RPC) Broker. A vendor device sends an observation to VistA inside an HL7 (ORU^R01) inbound message. The message is received by the VistA HL7 system, the patient and device are validated, and it is then forwarded to the Windows-based CP Gateway Service subsystem.

The VistA CP Gateway Service subsystem parses and validates the patient-identifying information and the device identifier. If the patient information and device identifiers are valid, the Windows service is notified that there is a message waiting to be processed in VistA. The Windows service calls into VistA via the RPC Broker to retrieve the HL7 message. The Windows service then parses and validates the observation data and saves the validated information in the Clinical Observations database (CliO) data store.

A Microsoft Windows service was used so that, in the next iteration of CliO, it will be possible to build in the ability to parse and decode images encoded in HL7 messages. Using a Microsoft Windows service also allows the processing of observational data to be offloaded to a second processor, allowing the primary listening process in the HL7 subsystem in VistA to be more responsive.

![](cp-flowsheets-implementation-guide/002.png)

Figure 1‑1 CP Gateway Service

For more information about the CP Gateway Service, refer to the *CP V1.0 Flowsheets Module Installation Guide*.

### CliO Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CliO database provides a standardized terminology data store for all clinical observations throughout the Department of Veterans Affairs (VA).

### Terminology Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Gateway Service provides extensive terminology mapping which translates proprietary labels so the information is understood to represent the same thing and, thus, be stored appropriately. Devices do not always use the same terms to describe the data they transmit. For example, one device may use the term “heart rate,” while another may transmit the same information as “pulse.” This mapping is more efficient than trying to compel each medical device vendor to conform to using standard terminology.

Similarly, CP Flowsheets can display the data to the user using the terminology that is preferred at a given unit or medical center. A flowsheet used by an MICU unit at one hospital can be customized to display “Heart Rate,” while a flowsheet used by a step-down unit may display “HR” or “Pulse.”

## CP Flowsheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets provides an electronic representation of the traditional paper flowsheet. This user-friendly, customizable Graphical User Interface (GUI) provides functionality for data entry, validation and editing, as well as patient management.

- Flowsheets provides electronic flowsheets that can be custom designed for any clinical area of a Medical Center.
- Flowsheets is a tool that can be used by clinicians to standardize assessment templates nationwide.
- Flowsheets provides the ability to report discreet observations data combined with progress notes.
- Flowsheets creates a complete audit trail of patient documentation.

## CP Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console provides the tools to build the flowsheet views and layouts that are used for patient care, for recording vital statistics as necessary. It also provides a means for configuring the CP Gateway Service, assigning permissions to CP Flowsheets users, and system administration.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Implementation Guide is intended for use by Information Resource Support personnel, CACs, and Flowsheet Coordinators. End users should be familiar with the following:

- Windows operating systems
- CPRS functionality

## CP Console Implementation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console is the administration dashboard for implementing and maintaining Clinical Flowsheets and devices for Clinical Procedures. Information Resource Management (IRM) should grant the site’s flowsheet coordinator the MD ADMINISTRATOR key. CP Console is then used to set up views, flowsheets, flowsheet totals, instruments, shifts, scheduled cleanup of unused files, and all the other administrative tasks to customize the application for their site.

# Pre-Implementation Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Guidance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To begin the pre-implementation planning, it is recommended that Medical Center Management support a Clinical Flowsheets Focus Group comprised of representatives from the Chief of Staff’s office, IRM, Nursing, Labor Management, Quality Management, Health Information Management Service (HIMS) and Biomedical Engineering. The focus group would discuss the order of implementation in the facility, new process and procedures for documenting using electronic flowsheets, as well as the third party vendor devices, such as bedside monitors and Clinical Information Systems that may be used in/purchased for Critical Care areas. Additionally, this group would drive the design of the flowsheets as this is site configurable.

This software can be implemented one unit at a time. As with any new software, new processes and procedures are required. For Clinical Flowsheets to be effective and successful, all transactions need to be entered and documented electronically.

> **IMPORTANT:** Installation of MD\*1.0\*16 and MD\*1.0\*12 are a prerequisite for MD\*1.0\*23. Content in this document is based on the assumption that you already have MD\*1.0\*16 installed. In addition, installation of MD\*1.0\*23 is mandatory for all sites that are implementing CP Flowsheets.

## Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Clinical Flowsheets product, MD\*1\*16, was released with the following components:

<u>File Name</u> <u>Contents</u>

MD1_P16.KID MD\*1.0\*16 KIDS Build

MD1_0P16_Sample_Views.xml Sample Views

MD1_0P16CPGatewayServiceSetup.exe MD\*1.0\*16 CP Gateway Service setup file

MD1_0P16_EXES_AND_DOC.zip 12 files indented below

-CliO_Terminology.doc MD\*1.0\*16 Clinical Flowsheets Terminology file

-CPConsole.cnt MD\*1.0\*16 CP Console online Help contents file

-CPConsole.exe MD\*1.0\*16 CP Console Executable

-CPConsole.hlp MD\*1.0\*16 CP Console online Help file

-CPGatewayService.exe MD\*1.0\*16 CP Gateway Service Executable

-MD_1_P16.KID MD\*1.0\*16 KIDS Build     

-MD_1_P16_IG.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module Installation Guide

-MD_1_P16_IMPG.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module Implementation Guide

-MD_1_P16_RN.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module Release Notes

-MD_1_P16_TM.pdf MD\*1.0\*16 Clinical Procedures (CP) Technical Manual and Package Security Guide

-MD_1_P16_UM.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module User Manual

-RoboEx32.dll .DLL file required to access Help files

MD1_0P16_Flowsheets.zip (includes the 4 files indented below)

-CPFlowsheets.exe MD\*1.0\*16 CP Flowsheets Executable

-CPFlowsheets.hlp MD\*1.0\*16 CP Flowsheets online Help file

-CPFlowsheets.cnt MD\*1.0\*16 CP Flowsheets online Help contents file

-RoboEx32.dll .DLL file required to access Help files

## Flowsheet Design

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Console provides the tool to build the flowsheet views and layouts. In the pre-implementation phase, a copy of the current paper flowsheet should be reviewed. The design of the electronic flowsheets can then be established based on the review.

Sample Views are available for import. A copy of these views can be made once imported onto your system, and the copy can then be edited so that it is customized for your facility. You can also create a view from scratch.

CP Flowsheets are built from the CP Views. You can apply the same view to many flowsheets. It is important to remember this because if an edit is done on a CP View, that edit will be reflected on all the CP flowsheets that have that CP view assigned.

## Flowsheet Coordinators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility will need to determine who will have access to build the views and flowsheets. IRM will need to assign permissions as requested. Additional information about permissions is available in Chapter 3: CP Console Overview.

The Flowsheet Coordinator should be given the MD ADMINISTRATOR key, which will give them permissions to all needed functions.

The Flowsheet Coordinator has the following key responsibilities:

- Manages and facilitates installation, implementation, maintenance, enhancements and overall use of CP Flowsheets throughout the medical center through ongoing needs assessments and evaluation processes.
- Serves as site coordinator for implementation and development teams at the facility level, including communication of issues with the executive stakeholders and program team to achieve resolution
- Serves as a liaison to the VISN and national level teams for the CP Flowsheet application, to include facility representation at conference calls and/or educational programs.
- Coordinates and ensures initial and ongoing training for all CP Flowsheet users, including students, and temporary staff.
- Coordinates and ensures initial and ongoing usability assessments for the CP Flowsheet application and hardware systems.
- Facilitates initial and ongoing contingency system management.

## Contingency Plans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contingency procedures should be developed for scheduled and unscheduled downtime and coordinated with stakeholders prior to the implementation of the software. All applicable staff will need to be trained on the contingency plans.

# CP Console Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console is a replacement for CP Manager.

The CP Console window contains the following elements:

- Menu Bar
- Button Bar
- Detail Area
- Tree View

![](cp-flowsheets-implementation-guide/003.png)

Figure 3‑1, CP Console Window

1.  MD\*1.0\*16 disables the use of CP Manager. Use CP Console to perform the functions previously provided by CP Manager.

## CP Console Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Console Menu bar appears along the top of the window, under the Windows title bar. It contains three menu options: File, Tools, and Help.

![](cp-flowsheets-implementation-guide/004.png)

Figure 3‑2, CP Console Menu Bar

### File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the File menu to add new items, rename existing items, delete items, save items, and exit CP Console.

![](cp-flowsheets-implementation-guide/005.png)

Figure 3‑3, File Menu

#### New Menu

The New menu option allows you to create new flowsheets, flowsheet views, flowsheet totals, schedules, and shifts, as well as add instruments and procedures.

![](cp-flowsheets-implementation-guide/006.png)

Figure 3‑4, New Menu

#### Renaming an Item in the Tree View

Use Rename to change the name of an item in the tree view. To rename a flowsheet, a flowsheet total, a flowsheet view, an instrument, a procedure, or a shift, complete the following steps:

1.  In the CP Console tree view, select an item. The worksheet for that item appears.
1.  Click File and select Rename. The Rename \<item\> pop-up appears.

![](cp-flowsheets-implementation-guide/007.png)

Figure 3‑5, Rename Flowsheet

2.  Type a new name.
3.  Click OK. The new name appears in the tree view.

#### Deleting an Item

Use the Delete option to remove an item from the tree view. To delete a flowsheet, a flowsheet total, configuration parameters, or a shift, complete the following steps:

You can also delete items from the CP Console button bar.

![](cp-flowsheets-implementation-guide/008.png)

Figure 3‑6, CP Console Button Bar

2.  Since a Flowsheet is simply a data entity form, deleting a Flowsheet does not give you the ability to delete patient data,. If you remove a term, view, or flowsheet, data still exists but is no longer viewable within Flowsheets.
1.  In the CP Console tree view, select an item. The worksheet for that item appears.
4.  Click File and select Delete. The Confirm pop-up appears.

![](cp-flowsheets-implementation-guide/009.png)

Figure 3‑7, Confirm Delete

5.  Click Yes. The item is removed from the tree view.
3.  From the File menu, you can select Save to retain your additions and changes.
6.  Select Exit to close CP Console.

### Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Tools menu to locate items, assign permissions, refresh user roles, and export and import flowsheet views.

4.  If you make a change in CP Console, you will not see the change until you reload the Flowsheet.

![](cp-flowsheets-implementation-guide/010.png)

Figure 3‑8, Tools Menu

#### Search

On the Tools menu, click Search to look for an item in CP Console, such as a view, instrument, or procedure. Use the Console Find It Utility to perform your search.

![](cp-flowsheets-implementation-guide/011.png)

Figure 3‑9, Console Find It Utility

#### Working with User Permissions

Use the Permissions option to add, remove, and modify users to items in the Tree view (i.e. View, Flowsheet, etc.) of Flowsheets and assign permissions (access) to those items. Any user with the MD ADMINISTRATOR key can assign permissions to any of the items in CP Console. Other users can assign permissions only to the items that they own/control. Security keys assigned to each user determine the overall access they have to CP Console (Refer to the Refresh Roles section for more details). Assigning permissions is a way of giving access to a user who would otherwise not have access to a specific item in the Tree view.

5.  You need MD ADMINISTRATOR to assign any permission to any object or you need to have full access granted to you for items you are assigning to another person.

Highlight the item in the Tree view that you want to give another user permission to configure.

On the Tools menu, click Permissions or click the Permissions button. The Access Control List Manager appears and displays the users and permissions for the highlighted item.

![](cp-flowsheets-implementation-guide/012.png)

Figure 3‑10, Access Control List Manager

Use the Access Control List Manager to add users and their permissions, to change permissions, and to remove users. The Access Control List Manager offers a choice of four permissions that you can assign to a user:

- Read-Only - can only read items (default)
- Read-Write - can read, edit, and save items
- Read-Write-Delete - can read, edit, and save items, as well as delete some items
- Full Control - can do everything, which includes adding and removing users

#### CP Console Folder View Permissions

In CP Console, you need permission via Vista’s XPAR EDIT PARAMETER utility to see various folders in the CP Console tree view. With the proper permissions, you can have access to folders within the CP Console tree view including (VIEW, FS, SHIFT, and TOTALS).

Administrative functionality given by CP Console is no longer controlled primarily by role and security key. The visibility of folders is now controlled by entries in the Kernel Parameters package on a per-user basis. To make a folder visible to a specified user, the name of the folder must be entered EXACTLY as a parameter in XPAR EDIT PARAMETER:.

6.  Security keys will still override settings in XPAR. If a user has MD ADMINISTRATOR, all folders in CP Console will be visible regardless of the folder permissions set in XPAR.”

![](cp-flowsheets-implementation-guide/013.png)

Figure 3‑11, CP Console Folder View Permissions

7.  The MD Admin permission level will continue to have full access to all folders. To add/remove access folders using the XPAR, you will need to contact IRM Support.

#### Refresh Roles

Refresh Roles retrieves the current role (security key) assignments in VistA for the current user and displays them.

To refresh roles, complete the following steps:

1.  From the Tools menu, select Refresh Roles and the Information pop-up appears with the roles assigned to the item selected.

![](cp-flowsheets-implementation-guide/014.png)

Figure 3‑12, User Roles Assigned to Selected Item

- MD ADMINISTRATOR – CP Console requires the VistA MD ADMINISTRATOR role to create items in CP Console. The MD ADMINISTRATOR role includes MD MANAGER abilities with additional capabilities. CP Flowsheets requires the VistA MD ADMINISTRATOR role or the MD HL7 MANAGER role to access the HL7 Monitor. This role allows the holder full control of CP Flowsheets. Assign this role to users responsible for setting up and maintaining CP Console and CP Flowsheets.
- MD MANAGER – This role allows the holder to edit, audit, or rescind someone else’s data. Assign this role to power users of the CP Flowsheets patch to give them enhanced capabilities over a basic Flowsheets user.
- MD HL7 MANAGER - CP Flowsheets requires the VistA MD HL7 MANAGER role or the MD ADMINISTRATOR role to access the HL7 Monitor. Assign this role to a user who will assist with the HL7 messaging component of CP Flowsheets.
- MD READ-ONLY – Assign this role to a user to prevent them from entering data in Flowsheets. DO NOT assign MD READ-ONLY to a user concurrently with any role other than MD HL7 MANAGER. Doing so will lead to unpredictable results. A user with the MD READ-ONLY key may NOT log on to CP Console and will have limited functionality in CP Flowsheets.
- MD TRAINEE - This role has the same capabilities as a basic user except that all observations are unverified; a user who is not a trainee must verify all trainee observations. Assign this role to trainees.

#### Export to XML

Export to XML allows you to save your Instruments, Procedures, or Views to a disk as a backup of your flowsheet layouts. This allows administrators to share views or Flowsheets with other users or sites. To export to XML, complete the following steps:

8.  You must be assigned the role of MD ADMINISTRATOR to use this function.
1.  On the CP Console Tools menu, click Export to XML. The CP Console Export Wizard appears.

![](cp-flowsheets-implementation-guide/015.png)

Figure 3‑13, CP Console Export Wizard

7.  Click Next. The CP Console Export Wizard asks you to select the type of items to export.

![](cp-flowsheets-implementation-guide/016.png)

Figure 3‑14, CP Console Export Wizard Select Type

1.  Select Instruments, Procedures, or Views and click Next. The CP Console Export Wizard asks you to select the instruments, procedures, or views to export.
9.  Import/Export of Views, Procedures, and Instruments are based on folder permissions that are controlled by XPar. You will only have access to Import/Export folders that you have permission to. For example, if you only have access to Views and Procedures you will not be able to import/export Instruments.

![](cp-flowsheets-implementation-guide/017.png)

Figure 3‑15, CP Console Export Wizard

8.  Select the instruments, procedures, or views you want to export (in this example, instruments are being exported). You may select as many as you wish. You may press Ctrl-A to select all of the instruments, procedures, or views. Click Next. The CP Console Export Wizard asks you to enter or select the name of the file to export the selected instruments, procedures, or views.

![](cp-flowsheets-implementation-guide/018.png)

Figure 3‑16, Export Filename and Comments

9.  Export Filename and Comments.
1.  Enter the name of the export file. To change the location where the file will be saved, click Browse and select the location.  
    Or:  
    To replace an existing file with the new export file, or click Browse and select the file to replace. Click Yes when prompted to replace the file.
2.  Optionally, you may add comments in the Comments box. Comments submitted in the Export Wizard will appear in the Import Wizard before you finish importing your views. These will be included in the XML export file.
3.  Click Next. The CP Console Export Wizard displays a preview of the XML file.

![](cp-flowsheets-implementation-guide/019.png)

Figure 3‑17, CP Console Export Wizard File Preview

2.  You can scroll to review the XML file. To export the file, click Next.

![](cp-flowsheets-implementation-guide/020.png)

Figure 3‑18, CP Console Export Wizard Success

3.  When the export is complete, click Finish.

#### Import from XML

You can import Sample views such as a method to share between sites.

### Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help menu provides information about the application and access to online Help.

![](cp-flowsheets-implementation-guide/021.png)

Figure 3‑19, Help Menu

From the Help menu, select About to display information specific to the CP Console application.

Select Contents to display online Help for CP Console.

## CP Console Tree View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the left-hand panel, the CP Console tree view provides access to the following items: Background Task, Flowsheet, Flowsheet Total, Flowsheet View, Instrument, Parameters, Procedure, Schedule, and Shift.

![](cp-flowsheets-implementation-guide/022.png)

Figure 3‑20, CP Console Tree View

## CP Console Detail Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select an item in the CP Console tree view, details for that item appear in the large panel to the right. This is the worksheet where you create, customize, and fine-tune your flowsheet views, flowsheet layouts, and so on.

![](cp-flowsheets-implementation-guide/023.png)

Figure 3‑21, Item Detail Area

The banner appears at the top of every detail area, indicating the name you assign to the item, the type of item you are creating or modifying (flowsheet, view, total), as well as the access level.

This page intentionally left blank for double-sided printing

# Working with Clinical Flowsheet Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section details the basic tasks available within CP Console.

To get started, you will need the following:

- You must have the MD ADMINISTRATOR key
- Access to the CP Console executable
- Menu Option MD CLIO must be assigned

Within CP Console, you can complete the following tasks:

- Import Sample Views
- Customize Flowsheet Views
- Create a Flowsheet
- Add, Edit, or Remove a view from an existing flowsheet

  ![](cp-flowsheets-implementation-guide/024.png)IMPORTANT: If you are importing views from a different site, you need to copy and rename them. See Renaming a Copied View for more details.See Also – Importing Views from XML, step [6](#_Importing_Views_from). If you click yes to the CP Console Import Wizard Confirm Warning message, your imported view will be overwritten. Make sure that you make a copy of the existing view to retain its contents.

<span id="_Importing_Views_from" class="anchor"></span>

## Importing Views from XML

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Views for Flowsheets are available for download. You can copy sample views as a starting point for creating custom views. They are available on the anonymous FTP site as MD1_0P16_Sample_Views.xml [.](file:///C:/VA%20Documents/CLIO/Application%20Data/Microsoft/Local%20Settings/Temporary%20Internet%20Files/Content.Outlook/INTLQ6V7/) Contact your local IRM Support to retrieve this file from the designated FTP server.

You can also follow these steps to import custom views.

1.  On the CP Console Tools menu, click Import from XML. The CP Console Import Wizard appears.

![](cp-flowsheets-implementation-guide/025.png)

Figure 4‑1, CP Console Import Wizard

10. Click Next. The CP Console Import Wizard asks you to enter or select the name of the file to import.

![](cp-flowsheets-implementation-guide/026.png)

Figure 4‑2, CP Console Import Wizard Import Filename

11. Enter MD1_0P16_Sample_Views.xml, or click Browse and select the file to import. The CP Console Import Wizard displays the file header.
10. Import/Export of Views, Procedures, and Instruments are based on folder permissions that are controlled by XPar. You will only have access to Import/Export folders that you have permission to. For example, if you only have access to Views and Procedures, you will not be able to import/export Instruments.

![](cp-flowsheets-implementation-guide/027.png)

Figure 4‑3, CP Console Import Wizard File Header

12. Click Next. The CP Console Import Wizard asks you to select the components to import.

![](cp-flowsheets-implementation-guide/028.png)

Figure 4‑4, CP Console Import Wizard Select Components

13. Press Ctrl-A to select all of the components. Click Next.
14. If you import a view that has a Flowsheets view internal number that is the same as a view that already exists in CP Console, the imported item will overwrite the existing item. The CP Console Import Wizard displays a confirmation box to confirm that you want to overwrite the existing item.

![](cp-flowsheets-implementation-guide/029.png)

Figure 4‑5, CP Console Import Wizard Confirm

WARNING! If you click Yes, it will overwrite the existing item. To import a view and still retain the existing item, before you import the new item, make a copy of the existing item (refer to the Making a Copy section for more details), then import the new item. The import will still overwrite the original item, but it will not overwrite the copy.

11. Sample Views are read-only and cannot be changed.

To confirm the import of the item, click Yes. To retain the existing item and cancel the import of the new item, click No.

If you are importing more than one item that has a Flowsheets internal ID that is the same as a view that already exists in Flowsheets, the CP Console Import Wizard will display a confirmation box for each item.

15. During the import, the CP Console Import Wizard displays a progress report of the components as they are imported.

![](cp-flowsheets-implementation-guide/030.png)

Figure 4‑6, CP Console Import Wizard Progress Report

16. When the import is complete, click Finish.

![](cp-flowsheets-implementation-guide/031.png)

Figure 4‑7, Close Application Confirmation

17. To apply the changes, you must restart CP Console. To close CP Console, click OK.

    After you complete the import and restart CP Console, the views you imported are now available under the Flowsheet View folder as shown below.
12. The views you import will be in an “Inactive” status. These views will need to be “Active” before they are available for use.

The following figure shows what the imported sample views will look like:

![](cp-flowsheets-implementation-guide/032.png)

Figure 4‑8, Imported Views

## Customizing Flowsheet Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to customize the views for your site, complete the following tasks:

- Make a copy of a sample view
- Rename a copied View
- Edit renamed views

  Important: When you are editing a Flowsheet view, you should reload a flowsheet if it has been edited in the console, or close the flowsheet if it is currently being edited. Otherwise, editing a view in CP Console can cause other open flowsheets that use that view to show an error.

### Making a Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make Copy allows you to copy a flowsheet view. The new view will have a Flowsheets internal ID that is different from the view that you copied. This is especially useful when you are customizing views that you have imported.

Warning!: The character limit in the rename field is 43 characters. An error appears if you copy a flowsheet view name longer then 43characters. Rename the flowsheet view to a shorter name before you copy to avoid the error message.

13. If you rename an imported view, it does not change the Flowsheets internal ID and the renamed view could still be overwritten. If you Make a Copy of a view, it is assigned a new Flowsheets internal ID and will not be overwritten later by an imported view.
1.  In the CP Console tree view, select a view. The worksheet for that view appears.
18. On the File menu, click Make Copy or click the Make Copy button.

![](cp-flowsheets-implementation-guide/033.png)

Figure 4‑9, Make Copy Button

19. The Confirm Copy pop-up appears.

![](cp-flowsheets-implementation-guide/034.png)

Figure 4‑10, Confirm Copy

20. Click Yes. The copied view appears in the tree view.

![](cp-flowsheets-implementation-guide/035.png)

Figure 4‑11, Copied View

21. The view you just created is listed in the tree view with the words “Copy of” preceding the name of the view you copied.

#### Renaming a Copied View

After you copy a view, rename the view you just created. To rename a copied view, complete the following steps:

1.  From the buttons at top of the CP Console menu, click Rename.

![](cp-flowsheets-implementation-guide/036.png)

Figure 4‑12, Rename Button

22. The Rename Flowsheet window appears.
23. In the New Name field, rename your flowsheet view.

    ![](cp-flowsheets-implementation-guide/037.png)

Figure 4‑13, Rename Flowsheet

24. Click OK.
25. The renamed Flowsheet View will now appear in the Flowsheet View tree list.

#### Protecting an Imported or Exported View

The following flow diagram illustrates steps you can follow to protect an imported or exported view.

![](cp-flowsheets-implementation-guide/038.png)

Figure 4‑14, Protecting an Imported or Exported View

### Creating a New Flowsheet View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you choose not to copy a view, you can create your own view using the following steps.

You can create views specific to your site to assemble into your customized flowsheets. You can create an unlimited number of views. A flowsheet view is comprised of terms, parameters, and qualifiers. You can assemble one or more flowsheet views into a flowsheet that you use for entering patient data into CP Flowsheets. A customized flowsheet view allows you to add, edit, and remove terms, as well as change the display order of the terms.

To create a flowsheet view:

1.  From the File menu, highlight New and select Flowsheet View. The Create New Flowsheet View pop-up appears.

![](cp-flowsheets-implementation-guide/039.png)

Figure 4‑15, Create New Flowsheet View

26. In the Name box, type a name for the new view. The name appears in the tree view and as the Item Name at the top of the CP Console main window.
27. Click OK. The new Flowsheet View worksheet appears.

![](cp-flowsheets-implementation-guide/040.png)

Figure 4‑16 Flowsheet View Worksheet

28. The name you just added appears in the Display Name box.
29. From the Time Interval list, select a time interval to display across the y-axis (columns).
30. From the X-Axis list, select a list, Terminology or Date/Time, to display across the x-axis (rows).
31. *Optional:* In the Comment box, type additional information about the view.
32. To make the view available in CP Flowsheets, select the Active check box.
33. To be able to switch axes, the intervals (columns) with the lists (rows), select the Allow Pivot check box.
34. Click Save to save your new Flowsheet View.

Flowsheet View Definitions

The following are definitions specific to Flowsheet Views:

Display Name: Display Name describes the flowsheet view with a unique name, so you can identify it in the list of flowsheet views.

Time Interval: Time Interval sets the default time interval for the view display when accessed through CP Flowsheets. Choices range from one minute to 24 hours.

X-Axis: X-Axis sets the column headers along the top of a view to Date/Time or Terminology selections. Y-axis represents data type (rows) along the left side of a view.

Comment: *Optional* – You can provide additional information regarding the flowsheet view.

Active: The flowsheet view is active and available in CP Flowsheets.

- Select the Active check box to make the flowsheet view active and available.
- Clear the Active check box to inactivate the flowsheet view.
14. If the Active check box is not selected, the view does not load and you cannot enter data. A pop-up appears to indicate that the view is not active. The inactive view may display in the report.  
    In the tree view, an active view appears with ![](cp-flowsheets-implementation-guide/041.png).

![](cp-flowsheets-implementation-guide/042.png)

Figure 4‑17 - Active View

Allow Pivot: Allow Pivot switches the x-axis (column) selection to present along the y-axis (row) of a view. You can make the switch while using the flowsheet.  
Select and clear the check box to change the default view of the flowsheet view.

### ### View Terminology Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display Name: You assign a name to the view that appears in CP Flowsheets on your flowsheet.

Use the View Terminology Editor window to add terms (click Add) and to modify existing terms (click Edit).

![](cp-flowsheets-implementation-guide/043.png)

Figure 4‑18, View Terminology Editor

### Adding Terms to a View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the View Terminology Editor window to add terms to a view. To add terms to a view:

1.  Click on the view you would like to modify.
35. Click ![](cp-flowsheets-implementation-guide/044.png). The View Terminology Editor window appears.

![](cp-flowsheets-implementation-guide/045.png)

Figure 4‑19, View Terminology Editor

36. From the Term drop-down list, select a term.
15. The Term list contains terms provided with CP Console. You cannot add terms to the CP Console list. If you need to request or modify a term, refer to the following site for Terminology information:

> [https://dvagov.sharepoint.com/sites/VACOVACOOHIA/Nursing%20Informatics/CCDS/CPFS/CPF/SitePages/Home.aspx](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdvagov.sharepoint.com%2Fsites%2FVACOVACOOHIA%2FNursing%2520Informatics%2FCCDS%2FCPFS%2FCPF%2FSitePages%2FHome.aspx&data=04%7C01%7C%7C463d819e4536453976ee08d90fc756f2%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C637558171089729794%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=Ne1mSwYgBZjHQJIOGbWItfXTfpHQ3Mg00hWsnzheeMo%3D&reserved=0)

37. To set the default unit of measurement, if the selected term requires a default unit, select a unit from the Default Unit drop-down list.  
      
    ForExample:  
    Body temperature is always entered in degrees Fahrenheit. Select Degrees F from the drop-down list. The end user does not need to select Degrees F every time they enter a temperature.
38. *Optional:* Change the display name.  
    The Display Name automatically populates when you select a term.
39. To set a display width, select a width (in number of characters) from the Display Width drop-down list.
40. To set the display columns, if the selected term requires columns, select the number of columns to display from the Display Columns drop-down list.
41. Select the Use Dropdown check box to display the selections in a flowsheet in a drop-down list rather than as radio buttons.
42. From the Term Display Properties box, select one or more check boxes to provide calculations automatically in the view:
- Display Totals Row
- Display Average Row
- Display Count Row
- Display Min Value Row
- Display Max Value Row
- Display Subtotals by Time Interval
- Display Row as Read Only
- Input required for this term

  Refer to the following section, [Term Definitions](#term-definitions) for further detail on the above terms.
43. If the term you select has qualifiers associated with it, you need to make additional selections. Not all terms have qualifiers.
1.  Select one or more check boxes of the available qualifiers.
4.  Select descriptors for the qualifiers from the respective drop-down lists.
5.  Select the appropriate Mandatory check boxes to make qualifiers required fields.

For Example:

Weight has three qualifiers available: Method, Location, and/or Position. Define a method for taking the weight, by selecting a descriptor.

44. Click OK.
45. Click Save.
46. To add additional terms to a view, repeat steps 1-11.

#### Term Definitions

The Term section allows you to customize the term parameters and associated qualifiers.

Term: Term is the approved, standardized wording used for the observed clinical procedure/activity.

Default Unit: Default Unit is the unit of measure at which to set the default. You must select a default unit for a numeric unit.

Example  
Body temperature is always entered in degrees Fahrenheit. Select Degrees F from the drop-down list. Then you do not need to select Degrees F every time you enter a temperature.

Display Name: Display Name describes the selected term with a unique name, so you can identify it in the list of terms.

Display Width: Display Width is the maximum number of characters used in the field.

Display Columns: Display Columns is the number of columns to display in the view.

Use Dropdown: Use Dropdown allows you to display selections in a flowsheet in a drop-down list rather than a radio button options.

Display Only: Display Only prevents you from manually adding data for the observations.

Term Display Properties: You can select one or more properties for the selected term to provide calculations automatically for display in the view.

- Display Totals Row–provides a totals row for observations for display in the view
- Display Average Row–provides an average row for the observations for display in the view
- Display Count Row–provides a count row for the observations (the number of results in a particular column) for display in the view
- Display Min Value Row–provides a minimum value row, a row of the lowest number of observations
- Display Max Value Row–provides a maximum value row, a row of the highest number of observations
- Display Subtotals by Time Interval–provides subtotals by time intervals (calculations automatically by time intervals) for the observations for display in the view
- Display Row as Read Only–allows a row to be labeled *read only* for display in the view
- Input required for this term–indicates whether the term must have observations recorded

### Working with Qualifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A qualifier is an additional choice you can add to a term, such as the examples below. Not all terms have qualifiers. A term can have several qualifiers as specified in the terminology list. Those that display depend on the term you select. If the term you select has qualifiers associated with it, you can make additional selections.

Identify the type of qualifier by selecting the associated check box, such as:

- Method–lift scale, monitor
- Quality–actual, estimated
- Location–L arm, right upper lobe
- Position–sitting, standing
- Product–platelets, 5 percent albumin

Indicate that a qualifier is a required field by selecting a Mandatory check box.

If a qualifier is set to Mandatory, you cannot clear the qualifier from the flowsheet view data entry form.

16. You can clear the qualifiers that are not mandatory with the ESC key.

Select a descriptor for the type of qualifier from the respective drop-down list.

- When you do not select a qualifier, no default appears in the qualifier drop-down.
- When you select a qualifier, it appears in the drop-down as an editable default.
- When you select a qualifier and select mandatory, the qualifier appears in the drop-down and you cannot change it.

For Example:

Systolic Pressure has three qualifiers available: Method, Quality, and/or Position. Define a method for reading systolic pressure by selecting one or more of the qualifiers with associated parameters.

For information on creating a flowsheet view, refer to the Creating a Flowsheet View section in  
Chapter 4.

### Changing the Display Order of Terms in a View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Move Up and Move Down to change the display order of the terms in a view. To change the display order of terms in a view:

1.  Highlight the term you want to move in the display order of the view.
47. Click ![](cp-flowsheets-implementation-guide/046.png) to move the term up in the display order or click ![](cp-flowsheets-implementation-guide/047.png) to move the term down in the display order.
48. Click Save.

### Modifying Terms in a View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the View Terminology Editor window to modify the term qualifiers and associated descriptors of the terms of newly created views, as well as existing views. To edit terms in a view:

1.  Highlight a term from the Terminology list.

![](cp-flowsheets-implementation-guide/048.png)

Figure 4‑20, Terminology List

49. Click ![](cp-flowsheets-implementation-guide/049.png). The View Terminology Editor window appears.

![](cp-flowsheets-implementation-guide/050.png)

Figure 4‑21, View Terminology Editor

50. Change any or all of the parameters in the Term section.
51. If the term has qualifiers, change any or all of the qualifiers/descriptors in the Qualifiers section.

    ![](cp-flowsheets-implementation-guide/051.png)

> Figure 4‑22, Inactive Term

17. An asterisk next to the term indicates an inactive term. Also, when you select an inactive term, a pop-up appears stating that the term is marked inactive.
52. Click OK.
53. Click Save.
54. To edit additional terms in existing views, repeat steps 1-6.

### Removing Terms from a View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Remove to delete terms from a newly created or existing view. To remove terms from a view:

1.  From the Terminology list, highlight a term.

![](cp-flowsheets-implementation-guide/052.png)

Figure 4‑23, Terminology List

55. Click ![](cp-flowsheets-implementation-guide/053.png). Confirm pop-up appears.

![](cp-flowsheets-implementation-guide/054.png)

Figure 4‑24, Confirm Pop-up

56. Click Yes.
57. Click Save.
58. To remove additional terms from a view, repeat steps 1-4.

This page intentionally left blank for double-sided printing.

# Creating Flowsheets in CP Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console allows you to create flowsheet views and flowsheet totals, which you assemble into your individualized flowsheets to meet your site-specific requirements. Although the order in which you create the parts of a Flowsheet is not critical (you may use some sample flowsheet views and totals supplied with Flowsheets), you must have the following components to create a Flowsheet.

- Flowsheet view(s), including sample flowsheet views supplied with Flowsheets, that contain the information you want to include on your Flowsheet. Before publishing a Flowsheet, you must find or create the flowsheet views you wish to include on your Flowsheet.
- Flowsheet total(s) including sample flowsheet totals supplied with Flowsheets, which contain the information you want to include on your Flowsheet. Before publishing a Flowsheet, you must find or create the flowsheet totals you wish to include on your Flowsheet.

To create a Flowsheet in CP Console, complete the following steps:

1.  From the File menu, highlight New and select Flowsheet. The Create New Flowsheet pop-up appears.

![](cp-flowsheets-implementation-guide/055.png)

Figure 5‑1, Create New Flowsheet

59. In the Name box, type a descriptive name for the new flowsheet, for example ICU_VITALS or NHCU_VITALS. The name appears in the tree view and as the Item Name at the top of the CP Console main window.
60. Click OK. The new Flowsheet worksheet appears.

![](cp-flowsheets-implementation-guide/056.png)

Figure 5‑2, New Flowsheet Worksheet

18. Not all users have permissions to create or edit Flowsheets. Refer to the Permissions section for more information.

## Adding a new Flowsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a new flowsheet:

1.  In the Display Name box, type a name for the new flowsheet.
61. To make the flowsheet available in CP Flowsheets, select the Active check box.
62. *Optional:* In the Comment box, type additional information about the flowsheet.
19. This comment is only visible in CP Console.
63. Make sure an appropriate TIU title exists and is active in CPRS.
1.  From the TIU Note Title for reporting list, select a note title to display in CPRS.
20. Selection is most accurately done by copying the TIU note title from CPRS or Vista or paste the title onto a text page, for example, Notepad or MSWord. Copy and paste the title name into the General section - "TIU note title for reporting".

You have the option to QUICKLY type the first 3-4 characters of the TIU note title. However, if you have several note titles that start out with the same 3-4 characters such as NURS, this could cause your system to lock up. Therefore, it is recommended that you copy and paste note contents.

64. Click Add. The New Flowsheet Page window appears.

### Adding a View to a Flowsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the New Flowsheet Page window to add a view to a new or existing flowsheet. To add a view to an existing flowsheet:

1.  Select the Pages tab and click ![](cp-flowsheets-implementation-guide/057.png). The New Flowsheet Page window appears.

![](cp-flowsheets-implementation-guide/058.png)

Figure 5‑3, New Flowsheet Page

65. Select a view from the View drop-down list.
21. The View list contains the flowsheet views you created under Flowsheet View in CP Console, along with any default flowsheet views created by the development team.
66. The Display Name automatically populates when you select a view. If you change the display name, the view name changes in CP Console, and appears as Page Name in a new session of CP Flowsheets.
67. Select a type from the Page Type options: Mandatory, Optional, or Supplemental (defined below)
- Mandatory – mandatory views cannot be closed
- Optional – the optional view is not always displayed. Optional views can be added one at a time (for example, ventilator or pacemaker) and can be turned on or off as necessary and continue to be used with no loss of data.
22. An optional view is configured to document assessments related to singular non-invasive device types where documentation flow is suitable to follow on a continuum with the original entry. 

The optional view is added for initial documentation for a number of hours/days.  The view can be closed after the device is discontinued.  If the device is later placed back into use, adding the optional view again re-activates the original view for continuing documentation.

If you are tracking usage of model numbers, lot numbers, or invasive lines, then configure device assessments in a supplemental view.

- Supplemental – you can use the view, but it is not necessary for all flowsheets; a supplemental view does not display initially, you have to add it to the flowsheet. You can use multiple supplemental views (for example IV bags or multiple wounds). If you close a supplemental view and add a new one, the new one will be blank. The data is locked into that view. The closed supplemental view can still be viewed on the flowsheet and report.
68. Click OK.
69. Click Save.
70. To add additional views to a flowsheet, repeat steps 1-6.
23. There are no restrictions to the number of times a view can be added to a flowsheet.

### Pages Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Pages tab to add, edit, or remove a view, as well as arrange the display order of the views on a flowsheet.

![](cp-flowsheets-implementation-guide/059.png)

Figure 5‑4, Pages Tab

### Editing a View Type in a Flowsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Edit Flowsheet Page window to change a view type in a new or existing flowsheet. To edit a view in a flowsheet:

1.  Select the Pages tab, highlight a view.

![](cp-flowsheets-implementation-guide/060.png)

Figure 5‑5, Pages Tab

71. Click ![](cp-flowsheets-implementation-guide/061.png). The Edit Flowsheet Page window appears.
72. From the View drop-down list, select a view to modify.
73. *Optional:* Change the display name.
74. From the Page Type options, select a Page Type: Mandatory, Optional, or Supplemental.
75. Click OK.
76. Click Save.
77. To edit the page types of additional views, repeat steps 1-7.

### Removing a View from a Flowsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use Remove to delete a view from a flowsheet. To remove a view from a flowsheet, complete the following steps:

1.  Select the Pages tab. Highlight the view to delete.

![](cp-flowsheets-implementation-guide/062.png)

Figure 5‑6, Highlight View to Delete

78. Click ![](cp-flowsheets-implementation-guide/063.png).
79. Click Save.

### Changing the Display Order of Views in a Flowsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Move Up and Move Down to change the display order of the views in a flowsheet. To change the display order of views in a flowsheet, complete the following steps:

1.  Highlight the view you want to move in the display order of a flowsheet.

![](cp-flowsheets-implementation-guide/064.png)

Figure 5‑7, Highlight View to Move

80. Click ![](cp-flowsheets-implementation-guide/065.png) to move the view up in the display order or click ![](cp-flowsheets-implementation-guide/066.png) to move the view down in the display order.
81. Click Save.

## Creating a Flowsheet Total

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flowsheet total allows you to display the sum of numeric observations within that flowsheet view.

24. Totals are based on active date ranges from the displayed flowsheet. The calculation of the totals can include observations that may not be on the displayed flowsheet.

The following screen illustrates the active date ranges from the displayed flowsheet:

![](cp-flowsheets-implementation-guide/067.png)

Figure 5‑8, Active Date Ranges

Additional configuration approaches are addressed in supplemental documentation.

Creating flowsheet totals involves adding and removing terms, as well as changing the display order of the terms.

![](cp-flowsheets-implementation-guide/068.png)

Figure 5‑9, Create a Flowsheet Total

![](cp-flowsheets-implementation-guide/069.png)

Figure 5‑10, Totals Display from CP Flowsheets

To create a flowsheet total:

1.  From the File menu, highlight New and select New Flowsheet Total. The Create a New Flowsheet Total pop-up appears.

![](cp-flowsheets-implementation-guide/070.png)

Figure 5‑11, Create a New Flowsheet Total

82. In the Name box, type a name for the new total. The name appears in the tree view and as the Item Name at the top of the CP Console main window.
83. Click OK. The new Flowsheet Total worksheet appears.

### Editing the Flowsheet Total 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Display Name box, type a name for the new total.
84. To set the default unit, select a unit from the Default Unit drop-down list.
85. From the Decimals box, select the number of decimals for the default unit, 0-8.  
    Default is 2.
86. *Optional:* In the Comment box, type additional information about the flowsheet total.
87. To make the total available in CP Flowsheets, select the Active check box.
88. From the Display Properties box, select one or more check boxes to provide calculations automatically on the view:
- Display Total (All Terms)
- Display Count (All Terms)
- Display Average (All Terms)
- Display Minimum
- Display Maximum

#### Terminology Section

1.  To move a term from the Available Terms list, select the term and click ![](cp-flowsheets-implementation-guide/071.png) to move it into the Selected Terms list.
89. To move a term from the Selected Terms list, select the term and click ![](cp-flowsheets-implementation-guide/072.png) to move it into the Available Terms list.
90. Repeat steps 1 and 2 as many times as is necessary.
91. To arrange the list of Selected Terms in a specific display order, select a term and click ![](cp-flowsheets-implementation-guide/073.png) to move the term up the display order or ![](cp-flowsheets-implementation-guide/074.png) to move the term down the display order.
92. Repeat step 4 until you have the list in specific display order.
93. Click Save.

### Totals Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Flowsheets tree, select the Totals tab to add totals to and remove totals from a flowsheet, as well as, change the display order of totals on a flowsheet.

![](cp-flowsheets-implementation-guide/075.png)

Figure 5‑12, Totals Tab

#### Adding Totals to a Flowsheet

To add a total to a flowsheet:

1.  On the Totals tab, highlight the total in the Available Totals list you want to add.
94. Click ![](cp-flowsheets-implementation-guide/076.png). The total moves to the Assigned Totals list.
95. Click Save.

#### Removing Totals from a Flowsheet

You can use the left arrow to remove a total from a flowsheet. To remove a total from a flowsheet:

1.  On the Totals tab, highlight the total in the Assigned Totals list you want to remove.
96. Click ![](cp-flowsheets-implementation-guide/077.png). The total returns to the Available Totals list.
97. Click Save.

#### Changing the Display Order of Totals in a Flowsheet

Use the up arrow and the down arrow to change the display order of the totals in a flowsheet. To change the display order of the totals:

1.  Highlight the total you want to move in the display order of a flowsheet.
98. Click ![](cp-flowsheets-implementation-guide/078.png) to move the total up in the display order or click ![](cp-flowsheets-implementation-guide/079.png) to move the total down in the display order.
99. Click Save.

## Flowsheet Total

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The flowsheet total allows you to display the sum of all observations of a single type within that flowsheet view. Totals use date ranges from the primary flowsheet form as ranges for the totals. The calculation of the totals uses all the intakes (observations) for a specified date/time range, which includes those that display on the flowsheet, as well as the intakes that do not.

1.  From the File menu, highlight New and select Flowsheet Total. The Create New Flowsheet Total popup appears.

![](cp-flowsheets-implementation-guide/080.png)

Figure 5‑13, Create New Flowsheet Total

2.  In the Name box, type a name for the new Flowsheet Total and click OK
3.  The new Flowsheet Total worksheet appears.

![](cp-flowsheets-implementation-guide/081.png)

Figure 5‑14, Build a Flowsheet Total

### Understanding Totals Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display Name: Display Name describes the flowsheet total; it appears as the title of the report.

Default Unit: Unit of measure that the flowsheet total uses as a default.

Decimals: Number of decimal places for the unit, 0-8; default is 2.

Comment: *Optional* – You can provide additional information regarding the flowsheet total.

Active: The flowsheet total is active and available in CP Flowsheets.

- Select the Active check box to make the flowsheet total active and available.
- Clear the Active check box to inactivate the flowsheet total.
25. If the Active check box is not selected, the flowsheet total does not load and you cannot enter data. A pop-up appears to indicate that the flowsheet total is not active. The inactive flowsheet total may display in the report.  
    In the tree view, an active flowsheet total appears ![](cp-flowsheets-implementation-guide/082.png).

![](cp-flowsheets-implementation-guide/083.png)

Figure 5‑15, Active Flowsheet

Display Properties: Select one or more properties to display on your flowsheet.

- Display Total (All Terms)–sum of all observation amounts
- Display Count (All Terms)–number of results of an observation within a flowsheet view
- Display Average (All Terms)–average of all observations
- Display Minimum–lowest number of observations
- Display Maximum–highest number of observations
- *Display Ratio (Term 1/Term 2)*
- *Display Difference (Term 1–Term 2)*

## Setting up Default Shifts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Flowsheets allows you to set up standard default shifts for your site and departments.

Additional configuration approaches are documented in supplemental documentation.

#### Shift Information Definitions

The following are definitions for Shift Information in CP Console:

Display Name: Display Name describes the shift with a unique name, so you can identify it in the list of shifts.

Active: The shift is active and available in CP Flowsheets.

- Select the Active check box to make the shift active and available.
- Clear the Active check box to inactivate the shift.
26. If the Active check box is not selected, you cannot use the shift in your flowsheets.  
    In the tree view, an active shift appears ![](cp-flowsheets-implementation-guide/084.png).

![](cp-flowsheets-implementation-guide/085.png)

Figure 5‑16, Active Shift

Comment: *Optional* - You can provide additional information regarding the shift.

Start Time: 12:00 AM through 11:45 PM in 15-minute increments.

Stop Time: 12:00 AM through 11:45 PM in 15-minute increments.

#### Adding a Shift

Use the Shift Information worksheet to create your shifts. To add a shift:

1.  From the File menu, highlight New and select Shift. The Create New Shift pop-up appears.

![](cp-flowsheets-implementation-guide/086.png)

Figure 5‑17, Create New Shift

100. In the Name box, type a name for the new shift. The name appears in the tree view and as the Item Name at the top of the CP Console main window.
101. Click OK. The new Shift worksheet appears.

![](cp-flowsheets-implementation-guide/087.png)

Figure 5‑18, Shift Worksheet

102. In the Display Name box, type a name for the new shift.
103. To make the shift available in CP Flowsheets, select the Active check box.
104. *Optional:* In the Comment box, type additional information about the shift.
105. From the Start Time drop-down list, select a begin time.
106. From the Stop Time drop-down list, select an end time.
107. Click Save.

#### Modifying an Existing Shift

Use start and stop times to modify your shifts. To modify an existing shift:

1.  From the CP Console tree view, highlight Shift and expand the folder.
108. Select a shift from the list. In the following figure, the “Days-2” shift is selected.

![](cp-flowsheets-implementation-guide/088.png)

Figure 5‑19, Selected Shift

109. Make the necessary changes to one or more fields of the shift worksheet.
110. Click Save.
111. 

# Additional Flowsheet Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Setting up Background Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console background tasks are system activities (which run in the background) that you can schedule. The three available cleanups address CliO, CP Legacy, and the HL7 Cleanup. These settings are determined according to site policy.

![](cp-flowsheets-implementation-guide/089.png)

Figure 6‑1, Background Tasks

Select one of the background tasks and its properties appear.

![](cp-flowsheets-implementation-guide/090.png)

Figure 6‑2, CliO Cleanup Background Task Properties

- Task ID: The identifier assigned to the task.
- Name: The name of the background task.
- Status: The status of a background task can be Active: Pending or Active: Running.
- Scheduled: Scheduled indicates the date and time the background task begins; the Default is Not Scheduled.

### CliO Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CliO is a database that stores patient observations. You can store data in a variety of formats. Old observations that are not in a state of verified or corrected are purged.

27. If student/trainee documentation is not in a state of verified or corrected, it will also be purged.

To change the scheduling of Clio Cleanup:

1.  Under Background Task, click CliO Cleanup.
112. Click Change.
113. Schedule the task. Refer to the Changing the Schedule for a Task section for more details.

### CP Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Cleanup background task cleans up observations (unencoded or XML data) from instruments (monitors) that are not in a verified state (data that is not clinically relevant). This cleanup is designed to run after data is processed, and deletes the data that is not clinically relevant from both Legacy and CliO. It runs through the UPLOAD ITEM field in the CP RESULT REPORT file (#703.1) and purges unnecessary data from previous uploads.

To change the scheduling of CP Cleanup:

1.  Under Background Task, select CP Cleanup.
114. Click Change.
115. Schedule the task. Refer to Changing the Schedule for a Task for more details.

### HL7 Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Cleanup purges messages not validated that remain more than a number of days set by you, in the HL7 log file.

To change the scheduling of HL7 Cleanup:

1.  Click HL7 Cleanup.
116. Click Change.

Schedule the task. Refer to the Changing the Schedule for a Task section for more details.

## Adding an Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the new instrument worksheet to add new instruments to Clinical Flowsheets. To add an instrument, complete the following steps:

28. The instrument worksheet is for legacy CP instrument connections only. For MD\*1.0\*16 connections, all information required will be exported as part of a centrally maintained mapping file.
1.  From the File menu, highlight New and select Instrument. The Create New Instrument pop-up appears.

![](cp-flowsheets-implementation-guide/091.png)

Figure 6‑3, Create New Instrument

117. In the Name box, type a name for the new instrument. The name appears in the tree view and as the Item Name at the top of the CP Console main window.
118. Click OK. The new Instrument worksheet appears.

![](cp-flowsheets-implementation-guide/092.png)

Figure 6‑4, New Instrument Worksheet

119. *Optional* – In the Comment box, type additional information pertaining to the instrument.
120. In the Print Name box, type the name as you want it to appear on the instrument report.
121. To make the instrument available in CP Flowsheets, select the Active check box.
122. In the Serial Number box, type the serial number of the instrument.
123. From the Notification Mailgroup drop-down list, select a local VistA mailgroup.  
     Click in the box and type an alpha character, such as b, p, or r, at which you want the list of mailgroups to begin.

### Modifying an Existing Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Instrument worksheet to modify the parameters of an existing instrument. To modify an existing instrument, complete the following steps:

1.  In the tree view, highlight Instrument and expand the folder.
124. Select an instrument from the list.

     In the following example, the AWARE instrument is selected.

![](cp-flowsheets-implementation-guide/093.png)

Figure 6‑5, Selected Instrument

125. Make the necessary changes to the fields of the instrument worksheet.
126. Click Save.

#### Using Make Copy for Instruments

Use the Make Copy button to make a copy of an existing instrument for use in creating additional instruments.

Warning!: The character limit in the rename field is 23 characters. An error appears if you copy an instrument name longer than 23 characters. Rename the instrument to a shorter name before you copy to avoid the error message.

1.  In the tree view, highlight and expand the Instrument folder.
2.  Select an existing instrument you want to copy.
3.  Click the Make Copy button on the top of the screen.

![](cp-flowsheets-implementation-guide/094.png)

Figure 6‑6, Make Copy Button

127. The Confirm Copy dialog box is displayed.

![](cp-flowsheets-implementation-guide/095.png)

Figure 6‑7, Confirm Copy

128. Click Yes. The copied instrument appears in the tree view.

#### Renaming a Copied Instrument

After you copy an instrument, rename the instrument you just created. To rename a copied instrument, complete the following steps.

1.  From the buttons at top of the CP Console menu, click Rename.

![](cp-flowsheets-implementation-guide/096.png)

Figure 6‑8, Rename Button

2.  The Rename Instrument window appears.

![](cp-flowsheets-implementation-guide/097.png)

Figure 6‑9, Rename Instrument

3.  In the New Name field, rename the instrument
4.  Click OK.
5.  The renamed instrument appears in the tree view list.

### Instrument Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are definitions specific to Instruments:

Comment: *Optional* – You can provide additional information regarding the instrument.

Print Name: Name of the instrument to print on the instrument report.

Active: The instrument is active and available in CP Flowsheets.

- Select the Active check box to make the instrument active and available to transmit results.
- Clear the Active check box to prevent the instrument from transmitting results.
29. If the Active check box is not selected, you cannot use the instrument in your flowsheets.  
    In the tree view, an active instrument appears.

![](cp-flowsheets-implementation-guide/098.png)

Figure 6‑10, Active Instrument

Serial Number: Serial number of the instrument is assigned by the manufacturer.

Notification Mailgroup: Identify a local VistA mailgroup to notify when a problem arises with an active instrument.

### Attachment Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete the following steps to select and process an attachment:

1.  In the Default Ext box, type the default file extension exported by the vendor.
2.  In the M Routine box, type the routine the instrument uses to process HL7 messages.
3.  From the Pkg Code drop-down list, select the code of the processing package.
4.  Select the Delete when submitted check box if the site does not store a duplicate report or the vendor deletes reports because of storage issues.
5.  From the Valid Attachment Types options, select one or more method of attaching patient data.

The following are Attachment Processing definitions:

Default Ext: Default file extension exported by the vendor (.html, .pdf, .jpg).

M Routine: MUMPS routine used to process the HL7 message from the active instrument.

Pkg Code: Code of the package that processes the active instrument results.

- Medicine – Medicine package
- CP V1.0 – Clinical Procedures v1.0
- CliO – Clinical Observation database

Delete when submitted: Select the check box if the site does not want to store a duplicate report outside of Imaging or the vendor wants to delete files because of storage issues.

Valid Attachment Types: The type of patient data expected from the instrument. Data type indicates to CP Console the kind of data output to expect from the instrument.

- UUEncode (Unix to Unix Encode)–a set of algorithms for converting files into a set of ASCII characters to transmit over a network
- XML (Extensible Markup Language)–a specification for Web documents developed by the World Wide Web Consortium (W3C), the organization that sets standards for the Web; XML is a pared-down version of Standard Generalized Markup Language (SGML)
- XMS–XML Style Sheet
- DLL (Dynamic Link Library)–a library of executable functions or data used by Windows applications
- UNC (Universal/Uniform Naming Convention)–a personal computer (PC) format for specifying the location of resources on a local-area network (LAN)
- Text–Text stored as ASCII codes
- URL (Uniform Resource Locator)–the global address of documents and other resources on the World Wide Web (www)

### Adding a Configuration for a Bi-Directional Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a configuration for a bi-directional instrument, complete the following steps:

1.  If the instrument is bi-directional, select the Bi-Directional Instrument check box.
1.  Type in the IP Address assigned to the instrument, the Port (location) assigned to the instrument, the HL7 Instrument ID for the instrument, and the HL7 UNV SRV ID for the instrument procedure.
6.  From the HL7 Link drop-down list, select the unique link for the instrument.  
    Click in the box and type an alpha character, such as b, p, or r, where you want the list of instrument links to begin.
30. This area of the screen is for informational purposes only.
129. Click Save.

The following are term definitions for bi-directional instruments:

Bi-Directional Instrument: An instrument that both sends and receives data.

IP Address: Each instrument at your facility must have an IP address. An IP address is a string of four integer numbers between 0 and 255 separated by periods.

Port: The location of the instrument to which you send data and from which you receive data.

HL7 Inst ID: The instrument ID in HL7 messages that identifies the instrument. The ID is provided by the vendor.

HL7 Unv Svc ID: The universal service ID for HL7 messages identifies the type of procedure the instrument performs when the instrument is capable of performing more than one procedure.

HL7 Link: There is one unique HL7 link for each instrument.

#### Configuring a Bi-Directional Instrument to Receive Data Only

You can set up a special bi-directional instrument configuration so that CP will send only an “outbound” HL7 message containing CPRS patient information to the instrument. The CP procedure is automatically placed in Complete status after the HL7 message is sent, thus preventing an “inbound” HL7 message containing the test results from being sent back to the CPRS Consult Note.

The physician can then edit the Consult Note by manually pasting in data from a test result reporting system to complete the Consult.

This configuration is beneficial for users of reporting systems—such as the Clinical Assessment, Reporting, and Tracking System for Cardiac Catheterization Laboratories (CART-CL) application—who do not want the test results from the medical instrument to populate the CPRS Consult Note but prefer to manually paste the test results from a different reporting system into the Consult Note.

To implement this configuration, your System Administrator must set a special flag in the CP Instrument File that will trigger the Complete status after the outbound HL7 is sent.

To configure a bi-directional instrument to receive data only, complete the following steps:

1.  Set up a bi-directional instrument configuration as directed in Section 6.2.4.
2.  Submit a request to your System Administrator to set the CONSULT KEEP OPEN field to Yes for the affected instrument in the CP Instrument File (#702.09). Be sure to include the instrument name in your request.

## Working with Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameters are set with CP Console.

You can configure the following items:

- CP ADT Feed
- CP Gateway Configuration,
- CP Parameters

![](cp-flowsheets-implementation-guide/099.png)

Figure 6‑11, CP Console Parameters

### CP Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Procedures system parameters affect all the procedures and instruments. You need to set the common parameters.

![](cp-flowsheets-implementation-guide/100.png)

Figure 6‑12, Clinical Procedures Common Parameter Set

### Administering Notification Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A notification list editor is a tool that is part of the Clinical Procedures Common Parameter Set.

If you experience HL7 errors, the Notification List editor allows you to send a message to the specified member.

To administer notification lists:

1.  Click the Notification Lists button.

![](cp-flowsheets-implementation-guide/101.png)

Figure 6‑13, Notification List Editor

2.  In the Name list, select the list to edit. The members of the list appear in the Members box.
3.  Use the Add, Edit, Remove buttons to edit the list.
4.  Use the Save List button to save the list.
5.  Use the Test button to send a test message to the members of the list.

The following are some additional terms specific to the Clinical Procedures Common Parameter Set:

Clinical Procedures Home Page: The Clinical Procedures Home page appears and directs the browser to this page when accessed. The data in this field is predefined.

Imaging Network Transfer Directory: This is the path to the Imaging network directory used for transferring data.  
Use ![](cp-flowsheets-implementation-guide/102.png) to browse to the appropriate location in the directory.

Observation Retrieval Batch Size (Records): The number of database (DB) records to pull at one time.  
Use the arrows to select a number of DB records to include in the batch.

Unverified Observation Retention (Days): The number of days to keep the unverified observations before purging.  
Use the arrows to select the number of days to retain unverified data.

This is a CLIO Cleanup task.

Instrument Data Retention (Days): The number of days to keep data from an instrument before purging.  
Use the arrows to select the number of days to retain instrument data.

This is a CP Cleanup task.

Clinical Procedures System On Line: The Clinical Procedure System On Line check box allows you to restrict access to Clinical Procedures.

- Select the check box to indicate Clinical Procedures is offline.
- Clear the check box to indicate Clinical Procedures is online.

Offline Message: When the Clinical Procedure System On Line check box is not selected, type a note in the Offline Message box to display when Clinical Procedures is offline.

Allow External Attachments: This affects Legacy CP. This allows you to find external attachments.

- Select the Allow External Attachments? check box to allow external attachments.
- Clear the Allow External Attachments? check box to not allow external attachments.

Bypass CRC Check: Bypass the Cyclical Redundancy Check during startup. On the server you can check the checksum of the running application to verify that it is the same as the checksum of the application distributed; the checksum value is associated with the version number of the software.

- Select the Bypass CRC Check? check box to perform the verification.
- Clear the Bypass CRC Check? check box to not perform the verification.
31. If the checksum values do not match, a message appears indicating the values do not match.

Cache Terminology Files: This is the path to the network directory used for caching terminology files.  
Use ![](cp-flowsheets-implementation-guide/103.png) to browse to the appropriate location.

Notification Lists: Administer the lists used for notification.

## CP ADT Feed Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT (Admission/Discharge/Transfer) system allows VistA to notify third party devices (outgoing data to devices) that a patient was admitted, discharged, or transferred. ADT feed acts as an event handling system. You must configure the dynamic routing system, so that HL7 knows to which system to deliver the ADT messages. Link an ADT target to a protocol. For more information on configuring the CP ADT Feed, refer to the *CP Flowsheets Module V1.0 Installation Guide*.

32. The subscriber protocol (MD DGPM PATIENT MOVEMENT) is provided and you must add it to the ITEM multiple of the DGPM MOVEMENT EVENTS entry in the protocol file. This allows the ADT feed to receive notification of patient movement.

![](cp-flowsheets-implementation-guide/104.png)

Figure 6‑14, ADT Feed Configuration

### Current ADT Targets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove an ADT target, highlight a line and click Delete Selected.

The following are definitions specific to ADT Targets:

Name: Name of the site

Protocol: Name of the subscriber protocol

Division: Division location of patient

Ward: Ward location of patient

Message Type: ADT

Event Type: ADT outbound (from VistA) message types

- A01 Admit/visit notification
- A02 Patient transfer
- A03 Discharge/end visit
- A08 Update patient information
- A11 Cancel admission
- A12 Cancel transfer
- A13 Cancel discharge/end visit

### Adding an ADT Target

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Add ADT Target window to link an ADT target to a protocol. To add an ADT target:

1.  Highlight Parameters in the tree view.
130. Select CP ADT Feed Configuration. The Current ADT Targets window appears.
131. On the Current ADT Targets window, click New. The Add ADT Target window appears.

![](cp-flowsheets-implementation-guide/105.png)

Figure 6‑15, Add ADT Target

132. From the Protocol list, select a protocol by name.
133. From the Division tree view, select an entire division or a ward within a division.  
     (This allows Clinical Flowsheets to filter outbound messages by patient location.)
33. Selecting an entire division will not enable all outbound ADT messaging for the entire division.
134. In the Protocol Link Name box, type the protocol link name.
135. In the HL7 Message Type drop-down, ADT is the default.
136. From the HL7 Event Type drop-down list, select an ADT outbound message type.
137. Click OK.  
       
     Example  
     Protocol: MDSPL001  
     Division: CHEYENNE VAMROC\>C MEDICINE  
     The MDSPL001 protocol receives the ADT A01 message only if the patient is moved, transferred, or discharged from the C MEDICINE location.
138. Repeat steps 4-9 for each HL7 event type you need to link.

## CP Gateway Service Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must install the CP Gateway Service and configure the VistA server settings and the Gateway server settings for messaging to take place between VistA notification and ICU devices.

The CP Gateway Service exists as two subsystems, one solely within VistA, and the other as a Windows service that interacts with VistA by way of the RPC Broker. For more information on configuring the CP Gateway Service, refer to the *CP Flowsheets Module V1.0 Installation Guide*.

Use Gateway Server Settings to configure the gateway to restart automatically when the computer goes down.

![](cp-flowsheets-implementation-guide/106.png)

Figure 6‑16, CP Gateway Configuration Settings

### VistA Server Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These settings allow the Gateway Service to restart automatically:

Access Code: Access code for the VistA service account with RPC Broker Context for CP Gateway (for more details. refer to the *CP Flowsheets Module V1.0 Installation Guide*)

Verify Code: Verify code for the VistA service account with RPC Broker Context for CP Gateway *(*for more details*,* refer to the *CP Flowsheets Module V1.0 Installation Guide)*

VistA server address settings are stored on the workstation in the system registry. They allow the CP Gateway Service to connect to the appropriate VistA system at startup.

RPC Broker Port: Port on which the CP Gateway Service connects to the broker

IP Address: IP address at which the CP Gateway Service connects to the VistA system

### Gateway Server Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are definitions specific to the Gateway Server:

IP Address: Each server must have an IP address. An IP address is a string of numbers with format: xx.xx.xx.xxx. IP address of the workstation on which the CP Gateway Service is installed.

Notify Port: The listening port of the local machine. The port must be open when sending a message to the workstation. The default is 8888.

Log Level: The level of detail to log in the Windows Event Viewer for the CP Gateway Service.

- Critical – severe errors only
- Error – critical + errors that cause instability in the operation of the Gateway Service
- Warning – critical + error + any items captured but allowed the Gateway Service to continue running
- Detail – critical + error + warning + detailed execution trail of everything that the Gateway Service does as it processes HL7 messagesLog Directory: The log file tracks all the background operations and any problems that occur during processing. This is the directory in which the CP Gateway Service stores the logs.  
Type in the location of the log directory.  
The default directory for the log file is C:\\

Days to Retain Data: The number of days to allow processed messages to remain in the log prior to purging. After the number of days indicated, the data is purged during HL7 Log Cleanup.

- Use the arrows to set the number of days to retain messages.
- Leave the field empty or at 0 to retain the data indefinitely.

CP/Imaging Xfer Directory: This is the directory in which Imaging stores CP transfer data.

Data Retrieval Mechanism: The method to use for data retrieval–your data source: VistA Notification or Polling.  
Set the interval to VistA Notification. In VistA Notification, the VistA server will automatically notify the CP Gateway whenever a message arrives that requires processing. This is the preferred setting. Sometimes, however, local business requirements dictate that the Polling option be used. This option acts like the legacy CP Gateway, in that the CP Gateway will be polled periodically for data to process.

Polling Interval: The CP Gateway Service polls for new instrument data to transmit to VistA.  
When you select Polling as the data retrieval mechanism, use the arrows to set the number of seconds between polling operations. A new value becomes effective after the next polling operation.

## Working with Procedure Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Legacy procedure information is populated through the CP DEFINITION file (#702.01), but you need to populate additional fields to complete the process. You can add new procedures and modify existing procedures. In order to use a procedure in a flowsheet, you must select the Active check box to activate it. Also, you need a primary key (MD ADMINISTRATOR or MD MANAGER) to edit and add procedures.

![](cp-flowsheets-implementation-guide/107.png)

Figure 6‑17, Edit Procedure

### Adding a Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the new procedure worksheet to add new procedures to CP Flowsheets. To add a procedure:

1.  From the File menu, highlight New and select Procedure. The Create New Procedure pop-up appears.

![](cp-flowsheets-implementation-guide/108.png)

Figure 6‑18, Create New Procedure

139. In the Name box, type a name for the new procedure.
140. Click OK. The new Procedure worksheet appears.

The name appears in the tree view and as the Item Name at the top of the CP Console main window.

![](cp-flowsheets-implementation-guide/109.png)

Figure 6‑19, Procedure Worksheet

### Modifying an Existing Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Procedure worksheet to modify the parameters of an existing procedure. In the following example, the AIRWAY RESISTENCE procedure is selected.

To modify an existing procedure:

1.  In the tree view, highlight and expand the Procedure folder.
141. Select a procedure from the list.
142. Make the necessary changes to one or more of the fields of the procedure worksheet.
143. Click Save.

#### Using Make Copy for Procedures

Use the Make Copy button to make a copy of an existing procedure for use in creating additional procedures.

Warning!: The character limit in the rename field is 23 characters. An error appears if you copy a procedure name longer than 23 characters. Rename the procedure to a shorter name before you copy to avoid the error message.

1.  In the tree view, highlight and expand the Procedures folder.
2.  Select an existing procedure you want to copy.
3.  Click the Make Copy button on the top of the screen.

![](cp-flowsheets-implementation-guide/110.png)

Figure 6‑20, Make Copy Button

4.  The Confirm Copy dialog box is displayed.

![](cp-flowsheets-implementation-guide/111.png)

Figure 6‑21, Confirm Copy

144. Click Yes. The copied procedure appears in the tree view.

#### Renaming a Procedure

After you copy a procedure, rename the procedure you just created. To rename a copied procedure, complete the following steps:

1.  From the buttons at top of the CP Console menu, click Rename.

![](cp-flowsheets-implementation-guide/112.png)

Figure 6‑22, Rename Button

6.  The Rename Procedure window appears.

![](cp-flowsheets-implementation-guide/113.png)

Figure 6‑23, Rename Procedure

7.  In the New Name field, rename the procedure.
8.  Click OK.
9.  The renamed procedure appears in the tree view list.

### Procedure Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are definitions specific to Procedure:

Treating Specialty: This is the specialty under which the procedure falls. The list comes from the TREATING SPECIALTY file (#45.7).

![](cp-flowsheets-implementation-guide/114.png)

Figure 6‑24, Treating Specialty

Hospital Location: The location in the hospital in which the procedure is performed. The list comes from the HOSPITAL LOCATION file (#44); workload credit for the procedure is tracked through hospital location.

TIU Note Title: The title of an appropriate note with which to reference the active procedure. The list comes from the TIU DOCUMENT file (#8925). This must be a Generic TIU Note title.

Description: This is information describing/identifying the procedure.

External Attachment Directory: This is the directory in which you find attachments. If you select the Require External Data check box, type in the path to the location of the data, or browse to locate a directory.

Require External Data: The procedure requires external attachments, such as an independent report from another facility.

Auto Submit to VistA Imaging: Automatically submit to VistA Imaging when the procedure is processed by a bi-directional instrument and additional data does not need to be matched. When the check box is not selected, the study is in the Ready to Complete status.

High Volume Instrument: A medical device that sends over 200 observations per day.

34. The High Volume Instrument option is not active in this release of Flowsheets. It will be active in the next release

Active: The procedure is active and available in CP Flowsheets.

- Select the Active check box to make the procedure active and available.
- Clear the Active check box to inactivate the procedure.
35. If the Active check box is not selected, you cannot use the procedure in your flowsheets.  
    In the tree view, an active procedure appears ![](cp-flowsheets-implementation-guide/115.png).

![](cp-flowsheets-implementation-guide/116.png)

Figure 6‑25, Active Procedure

Processing Application: Select one application that performs the processing.

- Default (CP)–Clinical Procedures
- Hemodialysis–Hemodialysis package

Processed Results: Processed results indicate whether a final result, multiple results, or a cumulative result is associated with a particular procedure.  
Select one type of result.

- Final Result–default
- Multiple Results–allows creation of a new TIU note for each result sent back
- Cumulative Result–allows a multiple-result device to continuously send results back to the same TIU note

### Allowable Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allowable instruments are a list of instruments providing results for the procedure that appear in the Allowable Instruments group box. If you want to use an external attachment, do not select any instruments.

### Working with the Procedure Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To make a procedure available in CP Flowsheets, complete the following steps:

1.  Click inside the Treating Specialty drop-down list, and type an alpha character, such as c, t, or n, at which you want the list of specialties to begin.
145. From the Hospital Location drop-down list, select a hospital location. Click in the box and type an alpha character, such as c, t, or n, at which you want the list of locations to begin.
146. From the TIU Note Title drop-down list, select a note title to display in CPRS. Click in the box and type an alpha character, such as c, p, or n, at which you want the list of note titles to begin.
147. In the Description box, enter comments to describe the procedure.
148. Select the Require External Data check box for the procedure to allow external attachments.

![](cp-flowsheets-implementation-guide/117.png)

Figure 6‑26, Procedure Worksheet

149. If you select the Require External Data check box, enter the path to the location of the data, or browse to locate a directory in the External Attachment Directory field.
150. Select the Auto Submit to VistA Imaging check box to automatically submit the study to VistA Imaging.
151. Select the High Volume Instrument check box for a frequently used instrument.
152. To make the procedure available in CP Flowsheets, select the Active check box.
153. From the Processing Application options, select either Default (CP) or Hemodialysis.
154. From the Processed Results options, select one: Final Result, Multiple Results, or Cumulative Result.

### Adding Allowable Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add instruments for a procedure:

1.  From the Allowable Instruments list, select all instruments that provide results for the procedure.

![](cp-flowsheets-implementation-guide/118.png)

Figure 6‑27, Allowable Instruments

155. Click Save.

This page intentionally left blank for double-sided printing.

# Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you first open CP Console, you can use Tab and the arrow keys to maneuver through the main window.

The following is a list of shortcut keys for the CP Console main window.

| Option/Text     | Shortcut | Action/Opens            |
|-----------------|----------|-------------------------|
|                 |          |                         |
|                 | Alt, F   | Sets up for shortcuts   |
| File menu       | Alt, I   | Opens the File menu     |
| New             | N        |                         |
| Flowsheet       | F        |                         |
| Flowsheet Total | O        |                         |
| Flowsheet View  | L        |                         |
| Instrument      | I        |                         |
| Procedure       | P        |                         |
| Schedule        | C        |                         |
| Shift           | S        |                         |
| Rename          | R        |                         |
| Delete          | D        |                         |
| Save            | S        |                         |
| Exit            | E        |                         |
|                 |          |                         |
| Tools menu      | Alt, T   | Opens the Tools menu    |
| Search          | S        |                         |
| Permissions     | P        |                         |
| Refresh Roles   | R        |                         |
| Export To XML   | E        |                         |
| Import From XML | I        |                         |
|                 |          |                         |
| Help menu       | Alt, H   | Opens the Help menu     |
| About           | A        | Application information |
| Contents        | C        | Online help             |
|                 |          |                         |

This page intentionally left blank for double-sided printing.

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary is used for the Clinical Flowsheets project and may include terms and definitions not used in this specific document.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>&lt;RET&gt;</strong></td>
<td>Carriage return.</td>
</tr>
<tr class="even">
<td><strong>Access Code</strong></td>
<td>A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.</td>
</tr>
<tr class="odd">
<td><strong>Action</strong></td>
<td>A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.</td>
</tr>
<tr class="even">
<td><strong>ADP</strong></td>
<td>Automated Data Processing</td>
</tr>
<tr class="odd">
<td><strong>ADP Coordinator/­ADPAC/­Application Coordinator</strong></td>
<td>Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.</td>
</tr>
<tr class="even">
<td><strong>ADT</strong></td>
<td>Advanced Data Type (InterSystems Cache). Also Admissions, Discharges, Transfers.</td>
</tr>
<tr class="odd">
<td><strong>AP</strong></td>
<td>Arterial pressure</td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td>Application Programming Interface. An interface that a computer system, library, or application provides in order to accept requests for services from other programs, and/or to allow data to be exchanged between them.</td>
</tr>
<tr class="odd">
<td><strong>Application</strong></td>
<td>A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.</td>
</tr>
<tr class="even">
<td><strong>Archive</strong></td>
<td>The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.</td>
</tr>
<tr class="odd">
<td><strong>Assessment</strong></td>
<td><p>Assessment is the documentation of a clinician’s observations and interpretation of a patient’s clinical state based on a particular set of observations. The documentation is in the form of name-value pairs with values selected from a predetermined set, of name-value pairs in which the value is a number or set of numbers, or of free text.</p>
<p>Examples of assessments from paper ICU flowsheets are coma scale, patient opens eyes, pupil size, reaction to light, and so on.</p></td>
</tr>
<tr class="even">
<td><strong>ASU</strong></td>
<td>Authorization/Subscription Utility. An application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.</td>
</tr>
<tr class="odd">
<td><strong>Attachments</strong></td>
<td><p>Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:<br />
.txt - Text files<br />
.rtf - Rich text files<br />
.jpg - JPEG Images<br />
.jpeg - JPEG Images<br />
.bmp - Bitmap Images<br />
.tiff - TIFF Graphics (group 3 and group 4 compressed and uncompressed types)<br />
.pdf - Portable Document Format<br />
.html - Hypertext Markup Language</p>
<p>.DOC (Microsoft Word) files are not supported. Be sure to convert .doc files to .rtf or to .pdf format.</p></td>
</tr>
<tr class="even">
<td><strong>Background Processing</strong></td>
<td>Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.</td>
</tr>
<tr class="odd">
<td><strong>Background Task</strong></td>
<td>A job running on a computer while simultaneously working on a second job.</td>
</tr>
<tr class="even">
<td><strong>Backup Procedures</strong></td>
<td>The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.</td>
</tr>
<tr class="odd">
<td><strong>Boilerplate Text</strong></td>
<td>A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.</td>
</tr>
<tr class="even">
<td><strong>BP</strong></td>
<td>Blood Pressure.</td>
</tr>
<tr class="odd">
<td><strong>Broker</strong></td>
<td>Software which mediates between two objects, such as a client and a server or a repository and a requestor.</td>
</tr>
<tr class="even">
<td><strong>Browse</strong></td>
<td>Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).</td>
</tr>
<tr class="odd">
<td><strong>Bulletin</strong></td>
<td>A canned message that is automatically sent by MailMan to a user when something happens to the database.</td>
</tr>
<tr class="even">
<td><strong>Business Rule</strong></td>
<td>Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).</td>
</tr>
<tr class="odd">
<td><strong>CAC</strong></td>
<td>Clinical Application Coordinator.</td>
</tr>
<tr class="even">
<td><strong>Care Action</strong></td>
<td>Care action is an intervention scheduled on a patient that may or may not be ordered.</td>
</tr>
<tr class="odd">
<td><strong>CCB</strong></td>
<td>Change Control Board.</td>
</tr>
<tr class="even">
<td><strong>CCDSS</strong></td>
<td>Clinical Care Delivery Support System.</td>
</tr>
<tr class="odd">
<td><strong>CCOW</strong></td>
<td>Clinical Context Object Workgroup. An HL7 standard protocol through which applications can synchronize in real-time, enabling Single Sign On and Context Management.</td>
</tr>
<tr class="even">
<td><strong>CDR</strong></td>
<td>Clinical Data Repository.</td>
</tr>
<tr class="odd">
<td><strong>CIS</strong></td>
<td>Clinical Information System. An ICU Clinical Information System is any hardware/software system that works in concert to collect, store, display, and/or enable manipulation of potential, clinically relevant information. A CIS also acts as an HL7 Gateway. Vendors of monitors and other instruments used in an ICU provide the CIS. The primary distinguishing feature of this CIS is its ability to manually select a subset of all available data and send it to the EMR.</td>
</tr>
<tr class="even">
<td><strong>Class</strong></td>
<td>Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.</td>
</tr>
<tr class="odd">
<td><strong>Clinical Flowsheets</strong></td>
<td>A module of the Clinical Procedures package that allows the collection of discrete data from medical devices or a Clinical Information System. It is a complete HL7 standardized instrument interface developed and owned by the Department of Veterans Affairs. This module is comprised of three components: the CP Flowsheets application, the CP Console application, and the CliO Generic Interface.</td>
</tr>
<tr class="even">
<td><strong>Clinical Reminders</strong></td>
<td>A system which allows caregivers to track and improve preventive healthcare and disease treatment for patients and to ensure timely clinical interventions.</td>
</tr>
<tr class="odd">
<td><strong>CliO</strong></td>
<td>Clinical Observations database.</td>
</tr>
<tr class="even">
<td><strong>CM</strong></td>
<td>Configuration Management.</td>
</tr>
<tr class="odd">
<td><strong>Consult</strong></td>
<td>Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.</td>
</tr>
<tr class="even">
<td><strong>Contingency Plan</strong></td>
<td>A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.</td>
</tr>
<tr class="odd">
<td><strong>CP</strong></td>
<td>Clinical Procedures.</td>
</tr>
<tr class="even">
<td><strong>CP Console</strong></td>
<td>An application used by Administrators to configure the CP Flowsheets application and its interface settings.</td>
</tr>
<tr class="odd">
<td><strong>CP Definition</strong></td>
<td>CP Definitions are procedures within Clinical Procedures.</td>
</tr>
<tr class="even">
<td><strong>CP Flowsheets</strong></td>
<td>A GUI component of the Clinical Flowsheets package. Its primary functions are to provide a means to display data collected from a medical device and to allow manual entry of data. Additional functionality is provided to display and print reports, verify incoming observational data, add comments, correct erroneous information, and submit TIU Notes to CPRS.</td>
</tr>
<tr class="odd">
<td><strong>CP Gateway</strong></td>
<td>The service application that prepares the data contents of HL7 messages for use in CP Hemodialysis. It requires no direct user interaction.</td>
</tr>
<tr class="even">
<td><strong>CP Manager</strong></td>
<td>The CP Manager application is no longer supported after the installation of MD*1.0*16; it has been superseded by CP Console.</td>
</tr>
<tr class="odd">
<td><strong>CP Study</strong></td>
<td>A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.</td>
</tr>
<tr class="even">
<td><strong>CPRS</strong></td>
<td>Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.</td>
</tr>
<tr class="odd">
<td><strong>Data Dictionary</strong></td>
<td>A description of file structure and data elements within a file.</td>
</tr>
<tr class="even">
<td><strong>DBIA</strong></td>
<td>Database Integration Agreement.</td>
</tr>
<tr class="odd">
<td><strong>Delphi</strong></td>
<td>A programming language, also known as Object Pascal.</td>
</tr>
<tr class="even">
<td><strong>Device</strong></td>
<td>A hardware input/output component of a computer system (e.g., CRT, printer).</td>
</tr>
<tr class="odd">
<td><strong>Display Interval</strong></td>
<td>The amount of time that displays in each column of a flowsheet view. Display interval is configurable from 1 minute to 24 hours. Shorter interval settings can improve readability when a large amount of data is received over a short period of time. Longer interval settings allow you to view longer periods of time while reducing the amount of horizontal scrolling necessary to view all columns.</td>
</tr>
<tr class="even">
<td><strong>DLL</strong></td>
<td>Dynamically Linked Library. These files provide the benefit of shared libraries.</td>
</tr>
<tr class="odd">
<td><strong>DOB</strong></td>
<td>Date of Birth.</td>
</tr>
<tr class="even">
<td><strong>Document Class</strong></td>
<td>Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.</td>
</tr>
<tr class="odd">
<td><strong>Document Definition</strong></td>
<td>Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.</td>
</tr>
<tr class="even">
<td><strong>DUZ</strong></td>
<td>Designated user. This is the internal FileMan number for a particular user.</td>
</tr>
<tr class="odd">
<td><strong>Edit</strong></td>
<td>Used to change/modify data typically stored in a file.</td>
</tr>
<tr class="even">
<td><strong>EMR</strong></td>
<td>Electronic Medical Record. Health<em>e</em>Vet, is the permanent medical record for a patient in VistA</td>
</tr>
<tr class="odd">
<td><strong>Field</strong></td>
<td>A data element in a file.</td>
</tr>
<tr class="even">
<td><strong>File</strong></td>
<td>The M construct in which data is stored for retrieval later. A computer record of related information.</td>
</tr>
<tr class="odd">
<td><strong>File Manager or FileMan</strong></td>
<td>Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.</td>
</tr>
<tr class="even">
<td><strong>File Server</strong></td>
<td>A machine where shared software is stored.</td>
</tr>
<tr class="odd">
<td><strong>Flowsheet</strong></td>
<td>A flowsheet is a table, chart, spreadsheet, or other method of displaying data on two axes. One axis represents time intervals and the other axis represents the readings from an ICU monitor documented at the various time intervals.</td>
</tr>
<tr class="even">
<td><strong>Clinical Flowsheet Coordinator</strong></td>
<td>Primary liaison for implementation, maintenance, and evaluation of the CP Flowsheet application at the facility level.</td>
</tr>
<tr class="odd">
<td><strong>Flowsheet view</strong></td>
<td>A customizable subsection (or page) of a flowsheet. Flowsheet views are created by adding and arranging terms and choosing their default qualifiers. Flowsheet views can be set up to display observations, provide a way to manually enter observations, and display reports.</td>
</tr>
<tr class="even">
<td><strong>Fluid off</strong></td>
<td>Cumulative volume of fluid removed from patient.</td>
</tr>
<tr class="odd">
<td><strong>Gateway</strong></td>
<td>The software that performs background processing for Clinical Procedures.</td>
</tr>
<tr class="even">
<td><strong>Global</strong></td>
<td>An M term used when referring to a file stored on a storage medium, usually a magnetic disk.</td>
</tr>
<tr class="odd">
<td><strong>GUI</strong></td>
<td>Graphical User Interface. A Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.</td>
</tr>
<tr class="even">
<td><strong>HDR</strong></td>
<td>Health Data Repository.</td>
</tr>
<tr class="odd">
<td><strong>HEP (CUM)</strong></td>
<td>Cumulative heparin infusion</td>
</tr>
<tr class="even">
<td><strong>HFS</strong></td>
<td>Host File System.</td>
</tr>
<tr class="odd">
<td><strong>HIPAA</strong></td>
<td>Health Insurance Portability and Accountability Act.</td>
</tr>
<tr class="even">
<td><strong>HL7</strong></td>
<td>Health Level 7. A language which various healthcare systems use to interface with one another.</td>
</tr>
<tr class="odd">
<td><strong>HL7 Gateway</strong></td>
<td>Hardware or software provided by a vendor that is able to receive information in a vendor’s proprietary format from one or more ICU monitors and other instruments, to translate the data into standardized HL7 message format, and to pass the messages to other systems.</td>
</tr>
<tr class="even">
<td><strong>HR</strong></td>
<td>Heart Rate.</td>
</tr>
<tr class="odd">
<td><strong>HSD&amp;D</strong></td>
<td>Office of Information (OI), Health Systems Design &amp; Development.</td>
</tr>
<tr class="even">
<td><strong>HSITES</strong></td>
<td>Health Systems Implementation, Training, Education, and Support.</td>
</tr>
<tr class="odd">
<td><strong>ICU</strong></td>
<td>Intensive Care Unit.</td>
</tr>
<tr class="even">
<td><strong>IEN</strong></td>
<td>Internal Entry Number.</td>
</tr>
<tr class="odd">
<td><strong>IJ</strong></td>
<td>Internal Jugular.</td>
</tr>
<tr class="even">
<td><strong>Instrument</strong></td>
<td>An instrument is a device used to perform a medical function on a patient. In Clinical Flowsheets instrument refers to ICU monitors, which are electronic devices that collect and/or display information concerning the physical state of a patient. Usually, the monitor attaches to a patient and takes readings over time without requiring intervention for each reading.</td>
</tr>
<tr class="odd">
<td><strong>Interpreter</strong></td>
<td>Interpreter is a user role exported with USR*1*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.</td>
</tr>
<tr class="even">
<td><strong>IRM</strong></td>
<td>Information Resource Management.</td>
</tr>
<tr class="odd">
<td><strong>IRMS</strong></td>
<td>Information Resource Management Service.</td>
</tr>
<tr class="even">
<td><strong>JCAHO</strong></td>
<td>Joint Commission on Accreditation of Healthcare Organizations.</td>
</tr>
<tr class="odd">
<td><strong>Kernel</strong></td>
<td>A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.</td>
</tr>
<tr class="even">
<td><strong>Key</strong></td>
<td>A level of access assigned to a Flowsheets user that determines which Flowsheets functions the user may perform. Refer to “User Role” in this Glossary.</td>
</tr>
<tr class="odd">
<td><strong>LAYGO</strong></td>
<td>An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.</td>
</tr>
<tr class="even">
<td><strong>LPES/CPS</strong></td>
<td>Legacy Product Enterprise Support/Clinical Product Support. Enterprise Product Support (formerly Enterprise VistA Support).</td>
</tr>
<tr class="odd">
<td><strong>log</strong></td>
<td>A list that provides the time and description of events as they occur.</td>
</tr>
<tr class="even">
<td><strong>M</strong></td>
<td>Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all VistA applications.</td>
</tr>
<tr class="odd">
<td><strong>MailMan</strong></td>
<td>An electronic mail, teleconferencing, and networking system.</td>
</tr>
<tr class="even">
<td><strong>MAP</strong></td>
<td>Mean Arterial Pressure.</td>
</tr>
<tr class="odd">
<td><strong>Menu</strong></td>
<td>A set of options or functions available to users for editing, formatting, generating reports, etc.</td>
</tr>
<tr class="even">
<td><strong>Module</strong></td>
<td>A component of a software application that covers a single topic or a small section of a broad topic.</td>
</tr>
<tr class="odd">
<td><strong>MUMPS</strong></td>
<td>Massachusetts General Hospital Utility Multi-Programming System. Obsolete; now known as "M" programming language.</td>
</tr>
<tr class="even">
<td><strong>Namespace</strong></td>
<td>A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.</td>
</tr>
<tr class="odd">
<td><strong>Network Server Share</strong></td>
<td>A machine that is located on the network where shared files are stored.</td>
</tr>
<tr class="even">
<td><strong>Notebook</strong></td>
<td>This term refers to a GUI screen containing several tabs or pages.</td>
</tr>
<tr class="odd">
<td><strong>NTE</strong></td>
<td>Not To Exceed.</td>
</tr>
<tr class="even">
<td><strong>OI</strong></td>
<td>Office of Information. Formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.</td>
</tr>
<tr class="odd">
<td><strong>option</strong></td>
<td>A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.</td>
</tr>
<tr class="even">
<td><strong>optional page</strong></td>
<td>One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pacemaker) on its own flowsheet view. An Optional Page can display only once in a given flowsheet. If an optional page is closed and then redisplayed, any data previously entered still displays.</td>
</tr>
<tr class="odd">
<td><strong>Package</strong></td>
<td>Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.</td>
</tr>
<tr class="even">
<td><strong>page</strong></td>
<td>This term refers to a tab on a GUI screen or notebook.</td>
</tr>
<tr class="odd">
<td><strong>Password</strong></td>
<td>A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).</td>
</tr>
<tr class="even">
<td><strong>PCE</strong></td>
<td>Patient Care Encounter.</td>
</tr>
<tr class="odd">
<td><strong>PD</strong></td>
<td>Product Development</td>
</tr>
<tr class="even">
<td><strong>Permission</strong></td>
<td>Setting that can be used to allow access to particular views, flowsheets, etc. to one or more specific users and to control the type of access each user has.</td>
</tr>
<tr class="odd">
<td><strong>PIMS</strong></td>
<td>Patient Information Management System.</td>
</tr>
<tr class="even">
<td><strong>Pivot</strong></td>
<td>Swap the axes of a table or chart. This causes the values that were displayed along the vertical axis to be displayed along the horizontal axis and the values that were displayed along the horizontal axis to be displayed along the vertical axis.</td>
</tr>
<tr class="odd">
<td><strong>PM</strong></td>
<td>Project Manager.</td>
</tr>
<tr class="even">
<td><strong>Pointer</strong></td>
<td>A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.</td>
</tr>
<tr class="odd">
<td><strong>PRN</strong></td>
<td>As needed.</td>
</tr>
<tr class="even">
<td><strong>Procedure Request</strong></td>
<td>Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.</td>
</tr>
<tr class="odd">
<td><strong>Program</strong></td>
<td>A set of M commands and arguments, created, stored, and retrieved as a single unit in M.</td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>A set of rules governing communication within and between computing endpoints.</td>
</tr>
<tr class="odd">
<td><strong>PS</strong></td>
<td>Provider Systems.</td>
</tr>
<tr class="even">
<td><strong>PV</strong></td>
<td>Pulmonary Vascular.</td>
</tr>
<tr class="odd">
<td><strong>QG</strong></td>
<td>Quality Gate.</td>
</tr>
<tr class="even">
<td><strong>Qualifiers</strong></td>
<td>A word or phrase that provides specific information about an observation. For example, an observation could have qualifiers such as Unit (f=degrees Fahrenheit, c=degrees Celsius, bpm=beats per minute, rpm=respirations per minute, etc.), Method (Cu=cuff BP, Dop=Doppler BP, etc.), Position (Ly=lying, Si=sitting, St=standing, etc.), Location (La=left arm, LL=left leg, RA=right arm, RL=right leg, etc.), Quality (A=accurate, E=Estimated), etc.</td>
</tr>
<tr class="odd">
<td><strong>Queuing</strong></td>
<td>The scheduling of a process/task to occur later. Queuing is normally done if a task is a heavy user of computer resources.</td>
</tr>
<tr class="even">
<td><strong>RAID</strong></td>
<td>Redundant Array of Inexpensive Disks. A data storage scheme using multiple hard drives to share or replicate data among the drives.</td>
</tr>
<tr class="odd">
<td><strong>Result</strong></td>
<td>A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.</td>
</tr>
<tr class="even">
<td><strong>Routine</strong></td>
<td>A set of M commands and arguments, created, stored, and retrieved as a single unit in M.</td>
</tr>
<tr class="odd">
<td><strong>RPC</strong></td>
<td>Remote Procedure Call. A protocol that allows a computer program running on one host to cause code to be executed on another host.</td>
</tr>
<tr class="even">
<td><strong>Rx</strong></td>
<td>Prescription.</td>
</tr>
<tr class="odd">
<td><strong>SAC</strong></td>
<td>Standards And Conventions.</td>
</tr>
<tr class="even">
<td><strong>Security Key</strong></td>
<td>A function which unlocks specific options and makes them accessible to an authorized user.</td>
</tr>
<tr class="odd">
<td><strong>Sensitive Information</strong></td>
<td>Any information which requires a degree of protection and which should be made available only to authorized users.</td>
</tr>
<tr class="even">
<td><strong>Service</strong></td>
<td>A long-running executable designed to perform specific functions without user intervention. Windows services can be configured to restart automatically when the operating system is rebooted.</td>
</tr>
<tr class="odd">
<td><strong>SGML</strong></td>
<td>Standard Generalized Markup Language.</td>
</tr>
<tr class="even">
<td><strong>Shift</strong></td>
<td>A period of time that can be defined in CP Flowsheets. This often corresponds to the time an individual an individual works.</td>
</tr>
<tr class="odd">
<td><strong>Site Configurable</strong></td>
<td>A term used to refer to features in the system that can be modified to meet the needs of each site</td>
</tr>
<tr class="even">
<td><strong>Software</strong></td>
<td>A generic term for a related set of computer programs, such as an operating system that enables user programs to run.</td>
</tr>
<tr class="odd">
<td><strong>SQA</strong></td>
<td>Software Quality Assurance.</td>
</tr>
<tr class="even">
<td><strong>SRS</strong></td>
<td>Software Requirements Specification.</td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td>Social Security Number.</td>
</tr>
<tr class="even">
<td><strong>Status Symbols</strong></td>
<td>Codes used in order entry and Consults displays to designate the status of the order.</td>
</tr>
<tr class="odd">
<td><strong>STS</strong></td>
<td>Standards and Terminology Services. An initiative to create and maintain standardized terminology throughout the VA by assigning a code to every term.</td>
</tr>
<tr class="even">
<td><strong>Supplemental page</strong></td>
<td>One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pressure wound) on its own flowsheet view. Multiple supplemental pages can be added to a single flowsheet in order to track numerous specific conditions. If a supplemental page is closed and then a new supplemental page is added, the new supplemental page is blank.</td>
</tr>
<tr class="odd">
<td><strong>Tab</strong></td>
<td>One of the five primary GUI screens of the CP Flowsheets application: Flowsheet, Alarms, Reports, Log Files, and HL7 Monitor.</td>
</tr>
<tr class="even">
<td><strong>Task Manager or TaskMan</strong></td>
<td>A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.</td>
</tr>
<tr class="odd">
<td><strong>Term</strong></td>
<td>As used in Flowsheets, a term is any piece of relevant data. A term, like “Blood Pressure” will typically have one or more associated measures, modifiers, or qualifiers.</td>
</tr>
<tr class="even">
<td><strong>Terminology</strong></td>
<td>Standardization of words and terms used in Flowsheets.</td>
</tr>
<tr class="odd">
<td><strong>Title</strong></td>
<td>Titles are definitions for documents. They store the behavior of the documents which use them.</td>
</tr>
<tr class="even">
<td><strong>TIU</strong></td>
<td>Text Integration Utilities.</td>
</tr>
<tr class="odd">
<td><strong>TMP</strong></td>
<td>Trans Membrane Pressure.</td>
</tr>
<tr class="even">
<td><strong>UFR</strong></td>
<td>Ultrafiltration Rate.</td>
</tr>
<tr class="odd">
<td><strong>UI</strong></td>
<td>User Interface.</td>
</tr>
<tr class="even">
<td><strong>UNC</strong></td>
<td>Universal Naming Convention.</td>
</tr>
<tr class="odd">
<td><strong>Untrusted device</strong></td>
<td>A medical instrument which has not been mapped for use with the Clinical Flowsheets package. Data sent from an untrusted device will not display in a flowsheet view until someone reviews it (on the CP Flowsheets Log Files tab) and marks it as verified.</td>
</tr>
<tr class="even">
<td><strong>URL</strong></td>
<td>Uniform Resource Locator. A means of finding a resource (such as a web page or a device) on the Internet.</td>
</tr>
<tr class="odd">
<td><strong>URR</strong></td>
<td>Urea Reduction Ratio. The reduction in urea as a result of dialysis.</td>
</tr>
<tr class="even">
<td><strong>User</strong></td>
<td>A person who enters and/or retrieves data in a system, usually utilizing a CRT.</td>
</tr>
<tr class="odd">
<td><strong>User Class</strong></td>
<td>User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.</td>
</tr>
<tr class="even">
<td><strong>User Role</strong></td>
<td>User Role (in a documentation context). The role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).</td>
</tr>
<tr class="odd">
<td><strong>User Role</strong></td>
<td><p>User Role (in a Flowsheets setup context). The role of a Flowsheets user with respect to which Flowsheets functions the user will have permission to perform. Flowsheets User Role include the following.</p>
<p>• MD ADMINISTRATOR</p>
<p>• MD MANAGER</p>
<p>• MD HL7 MANAGER</p>
<p>• MD READ-ONLY</p>
<p>• MD TRAINEE</p></td>
</tr>
<tr class="even">
<td><strong>Utility</strong></td>
<td>An M program that assists in the development and/or maintenance of a computer system.</td>
</tr>
<tr class="odd">
<td><strong>UUEncoded format</strong></td>
<td>A form of binary to text encoding whose name derives from "Unix-to-Unix encoding”.</td>
</tr>
<tr class="even">
<td><strong>VA</strong></td>
<td>Department of Veterans Affairs. Formerly the Veterans Administration.</td>
</tr>
<tr class="odd">
<td><strong>VAMC</strong></td>
<td>Department of Veterans Affairs Medical Center.</td>
</tr>
<tr class="even">
<td><strong>VDEF</strong></td>
<td>VistA Data Extraction Framework.</td>
</tr>
<tr class="odd">
<td><strong>Verify Code</strong></td>
<td>A unique security code which serves as a second level of security access. Use of this code is site specific. This term is sometimes used interchangeably the term password.</td>
</tr>
<tr class="even">
<td><strong>VHA</strong></td>
<td>Veteran Health Administration.</td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td>Veterans Health Information Systems and Technology Architecture.</td>
</tr>
<tr class="even">
<td><strong>VP</strong></td>
<td>Venous Pressure.</td>
</tr>
<tr class="odd">
<td><strong>VUID</strong></td>
<td>Veterans Health Administration (VHA) Unique Identifier. A unique identifier that specifies individual data elements or observations. In Clinical Flowsheets, each term is assigned a VUID.</td>
</tr>
<tr class="even">
<td><strong>Workstation</strong></td>
<td>A personal computer running the Windows 9x or NT operating system.</td>
</tr>
<tr class="odd">
<td><strong>XML</strong></td>
<td>Extensible Markup Language. A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.</td>
</tr>
<tr class="even">
<td><strong>XMS</strong></td>
<td>Extended Memory Specification. The specification describing the use of extended memory in real mode for storing data.</td>
</tr>
</tbody>
</table>

  
This page intentionally left blank for double-sided printing

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
About 19
Access Control List Manager 12
Add a Procedure 72
Add a Shift 54
Add a View to a Flowsheet 44
Add an ADT Target 68
Add an Instrument 59
Add Terms to a View 35
Add Terms to Flowsheet Totals 50
Add Totals to a Flowsheet 51
B
Background Task
CliO cleanup 58
CP cleanup 58
HL7 cleanup 58
Name 57
Scheduled 57
Status 57
Task ID 57
C
Change the Display Order of Terms 50
Change the Display Order of Terms in a View 38
Change the Display Order of Totals in a Flowsheet 52
Change the Display Order of Views in a Flowsheet 47
CliO Database 2
Contents 19
CP ADT Feed Configuration
Add ADT target 68
Current ADT targets 68
CP Console 3
CP Console Button Bar
Permissions 12
CP Console Detail Area 20
CP Console Functionality
Creating a flowsheet total 48
Creating a flowsheet view 32
CP Console Menu Bar 8
File menu 8
Help menu 19
CP Console Tree View 19
Flowsheet total 52
Parameters 60
Procedure 71
CP Flowsheets 3
CP Gateway 1
CP Gateway Configuration
Gateway server settings 70
VistA server settings 70
CP Gateway Service 1
CP Parameters
Allow CliO cached queries 67
Allow external attachments 66, 67
Bypass CRC check 67
Clinical prodcedures system on line 67
CP common parameter set 66
Imaging network transfer directory 66, 67
Instrument data retention 67
Observation retrieval batch size 66
Unverified observation retention 67
Creating a Flowsheet
Adding a view 44
Adding totals to a flowsheet 51
Changing the display order of totals 52
Changing the display order of view 47
Editing a view 46
Pages tab 45
Removing a view 47
Removing totals from a flowsheet 52
Creating a Flowsheet Total
Adding terms 50
Changing the display order of terms 50
Removing terms 50
Creating a Flowsheet View
Adding terms to a view 35
Changing the display order of terms 38
Editing terms in a view 38
Removing terms from a view 40
D
Delete an Item 10
E
Edit a View in a Flowsheet 46
Edit Terms in a View 38
Exit 11
Export To XML 15
F
File Menu
Deleting an item 10
Exit 11
New 9
Renaming an item 10
Save 11
Flowhseet View
Time interval 33
Flowsheet
Adding a view 44
Adding totals 51
Changing display order of views 47
Changing the display order of totals 52
Editing a view 46
Removing a view 47
Removing totals 52
Flowsheet Total 52
Adding terms 50
Changing the display order of terms 50
Create 48
Decimals 53
Default unit 53
Display properties 53
Removing terms 50
Flowsheet View
Adding terms 35
Allow pivot 33
Changing display order of terms 38
Create 32
Editing terms 38
Qualifiers 37
Removing terms 40
Terminology 34
Terminology editor 34
X-Axis 33
G
Gateway Server Settings
CP/imaging xfer directory 71
Days to retain data 71
Log directory 71
Log level 70
Notify port 70
Polling interval 71
Gatway Server Settings
Data retrieval mechanism 71
H
Help Menu
About 19
Contents 19
I
Instrument
Add 59
Default file extension 63
Delete when submitted 63
HL7 instrument ID 64
HL7 link 63
HL7 universal service ID 64
IP address 64
M routine 63
Pkg code 63
Port 64
Serial number 62
Valid attachment types 63
K
Key
MD ADMINISTRATOR 14
MD MANAGER 14
M
Modify an Existing Procedure 73
Modify an Existing Shift 55
N
New 9
P
Parameters 60
Adding an ADT target 68
CP ADT feed configuration 67
CP gateway configuration 69
CP parameters 65
Permissions 12
Access control list manager 12
Procedure 71
Add 72
Allowable instruments 77
Auto submit to VistA imaging 76
External attachment directory 76
High volume instrument 76
Hospital location 76
Modifying existing 73
Processed results 77
Processing application 77
Require external data 76
TIU note title 76
Treating specialty 76
Product Benefits 1
R
Refresh Roles 12, 14
Remove a View from a Flowsheet 47
Remove Terms from a View 40
Remove Terms from Flowsheet Totals 50
Remove Totals from a Flowsheet 52
Rename 28
Rename an Item 10
S
Save 11
Search 11
Shift
Add 54
Modifing existing 55
Start time 54
Stop time 54
T
Terminology 34
Terminology Editor 34
Default unit 36
Display columns 37
Display only 37
Display width 37
Qualifiers 37
Use dropdown 37
Terminology Mapping 2
Tools Menu
Export to XML 16, 17, 18, 24, 26
Refresh roles 14
Search 11
V
VistA Server Settings
IP address 70
RPC broker port 70
