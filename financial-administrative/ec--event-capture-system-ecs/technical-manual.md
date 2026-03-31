---
title: Event Capture Version 2.0 GUI Technical Manual (Updated EC*2*170)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: GUI  (Updated EC*2*170)
app_code: EC
app_name: Event Capture System (ECS)
section: FIN
app_status: active
pkg_ns: EC
patch_ver: 2.0
patch_id: EC*2.0
group_key: "EC:EC:2.0"
file_numbers: []
security_keys: []
menu_options: 50
description: 
audience: 
keywords: 
  - description
  - parameter
  - span
  - table
  - event
  - routine
  - return
  - contents
  - class
  - capture
page_count: 0
word_count: 9532
section_count: 29
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=39"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Event Capture System 2.0

  Graphical User Interface

  Technical Manual
---

![](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/001.png)

August 2024

Office of Information and Technology

Revision History

<table>
<caption><p><span id="_Ref100844431" class="anchor"></span>Table Required VistA Software Products</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 49%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8/2024</td>
<td>2.7</td>
<td><p>Updated for Patch EC*2.0*169</p>
<p>Updated patch number and release date throughout document</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>04/2024</td>
<td>2.6</td>
<td><p>Updated for Patch EC*2.0*165</p>
<p>Updated patch number and release date throughout document</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>10/2023</td>
<td>2.5</td>
<td><p>Updated for Patch EC*2.0*164</p>
<p>Updated patch number and release date throughout document</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>06/2023</td>
<td>2.4</td>
<td><p>Updated for Patch EC*2.0*159</p>
<p>Updated patch number and release date throughout document</p>
<p>Added data pieces, number 8 and 9, to RPC <a href="#GETPRODEFS">EC GETPRBLST</a></p>
<p>Updated Figure 6 Reports Menu Screen without ECMGR Option, and Figure 7 Reports Menu Screen with ECMGR Options to reflect new report names</p>
<p>Updated language in section 12.1 for error correction</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>11/2022</td>
<td>2.3</td>
<td><p>Updated for Patch EC*2.0*161</p>
<p>Updated patch number and release date throughout document</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>07/2022</td>
<td>2.2</td>
<td><p>Updated for Patch EC*2.0*158</p>
<p>Updated patch number and release date throughout document</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>02/01/2022</td>
<td>2.1</td>
<td><p>Updated for Patch EC*2.0*156</p>
<p>Updated patch number and release date throughout document</p>
<p>Removed heading for “Namespace” under 2.1</p>
<p>Renamed section 5.2 from “Menu Outline” to “Main Menu Options”</p>
<p>Renamed section 5.3 from “Menu Diagram” to “Submenu Options”</p>
<p>Moved former section 12.1 (“Online Help”) to section 12, General Troubleshooting bullet items</p>
<p>Updated Figure 6 and Figure 7 to reflect new report (Procedure Summary)</p>
<p>Added content to section 7.1 - Integration Control Registrations</p>
<p>Added content to 7.3 - Remote Procedure Calls</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>03/22/2021</td>
<td>2.0</td>
<td><p>Document Updated for Patch 152</p>
<p>New Content Added as per Latest Template</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>04/13/2020</td>
<td>1.1</td>
<td>Document Updated for Patch 148</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>11/21/2018</td>
<td>1.0</td>
<td>Initial Document Release</td>
<td>TeamSMS/Leidos</td>
</tr>
</tbody>
</table>

<span id="_Ref100844431" class="anchor"></span>Table Required VistA Software Products

Table of Contents

Table of Figures

Table of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
    - [Functions of the Software](#functions-of-the-software)
  - [Document Orientation](#document-orientation)
    - [Disclaimers](#disclaimers)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
- [Files](#files)
  - [Global Placement](#global-placement)
  - [File List](#file-list)
    - [List File Attributes](#list-file-attributes)
  - [Templates and File Flow](#templates-and-file-flow)
- [Routines](#routines)
  - [XINDEX](#xindex)
  - [Callable Routines](#callable-routines)
  - [Routine List](#routine-list)
- [Exported Options](#exported-options)
  - [Event Capture Security Keys](#event-capture-security-keys)
  - [Main Menu Options](#main-menu-options)
  - [Submenu Options](#submenu-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-wide Variables](#software-wide-variables)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
    - [VA FileMan Access Codes](#va-fileman-access-codes)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
The Event Capture System (ECS) is a Veterans Health Information Systems and Technology Architecture (VistA) Class I workload reporting system supporting operations of the Department of Veterans Affairs (VA) Managerial Cost Accounting Office (MCAO). There are several Veterans Health Administration (VHA) national programs mandating using ECS instead of, or to augment other workload capture information systems. For example, ECS is used when programs cannot report workload in the form of Current Procedural Terminology (CPT) codes. ECS also allows for more precise workload capture and reporting than otherwise possible through other VistA systems.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture Technical Manual serves a dual purpose:

- Provides technical information to aid the Office of Information and Technology (OIT) staff with implementing and maintaining the software
- Provides security information for Information Security Officers (ISO)

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS captures basic resource utilization data which are reported in VistA and fed to the Decision Support System (DSS) in the DSS ECS monthly extract. The Event Capture software provides a mechanism to track and account for procedures and delivered services that other VistA packages do not handle. The procedures and services tracked through Event Capture are associated with the following:

- The patient to whom they were delivered
- The provider requesting the service or procedure
- The DSS Unit responsible for delivering the service

Information entered into ECS will then be sent electronically to DSS, Patient Care Encounter (PCE), and billing offices for processing which will in turn facilitate workload analysis, cost analysis and transmission of billing.

DSS Units typically represent the smallest identifiable work unit in a clinical service at a medical center. Veterans Affairs Medical Centers (VAMC) define the DSS Units. A DSS Unit can represent any of the following:

- An entire service
- A section of a service
- A small section within a section
- A medical equipment item used in patient procedures

The user must define the following items for every DSS Unit:

- Service: The service associated with the DSS Unit
- Cost Center: The fiscal identifier for the service using the particular DSS Unit
- Medical Specialty: The specialty section associated with the DSS Unit

### Functions of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture with all patches installed provides the following functions:

- Allows each VAMC to utilize the software for its own resource/costing needs
- Implements DSS Units
- Assigns user access to the DSS Units
- Allows single and batch data entry for patient procedures
- Generates reports for workload and other statistical tracking
- Provides a Graphical User Interface (GUI) to the ECS application
- Allows the user to upload patient encounter data to Event Capture from a spreadsheet
- Allows the user to switch between Computerized Patient Record System (CPRS) and ECS without having to log back into the ECS GUI application

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Audience – Advanced users and support personnel for Event Capture.
- Assumptions – This document assumes a sound fundamental knowledge of VistA and Event Capture.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation and additional information for this product—including the *Event Capture User Guide* (UG), and the *Event Capture Deployment, Installation, Back-out, and Rollback Guide* (DIBR)—can be found on the [VA Software Document Library](https://www.va.gov/vdl/search.asp?group=application&terms=ECS) (VDL).
Online technical documentation pertaining to the Event Capture software, in addition to documentation found in the help topics, may be generated through utilization of several Kernel options. These include XINDEX and VA FileMan List File Attributes. Further information about other utilities that supply online technical documentation may be found in the Kernel Reference Manual.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace for Event Capture is EC. The excluded namespaces are ECT, ECW, ECX, and EC1.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are approximately 250 Event Capture routines that take up approximately 997KB of disk space (including pre-initialization and post-initialization routines).

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture is part of a larger integrated medical records system and relies on data from other packages to perform its functions.

Table 1 lists the VistA software products that must be installed before installing Event Capture.

| Product Name                                                | Minimum Version |
|-------------------------------------------------------------|-----------------|
| CPT/Healthcare Common Procedure Coding System (HCPCS) Codes | 6.0             |
| Diagnosis Related Group (DRG) Grouper                       | 18              |
| Kernel                                                      | 8.0             |
| MailMan                                                     | 8.0             |
| Patient Care Encounter (PCE)                                | 1.0             |
| Patient Information Management Service (PIMS)               | 5.3             |
| Registration                                                | 5.2             |
| Remote Procedure Call (RPC) Broker                          | XWB\*1.1\*71    |
| ToolKit                                                     | 7.3             |
| VA FileMan                                                  | 22.2            |

<span id="_Ref100844559" class="anchor"></span>Table FORUM Steps

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the steps in FORUM from the Software Services Primary Menu.

| Step | Custodial Package                 | Subscriber Package                                     |
|------|-----------------------------------|--------------------------------------------------------|
| 1    | DBA MENU                          | DBA MENU                                               |
| 2    | INTEGRATION CONTROL REGISTRATIONS | INTEGRATION CONTROL REGISTRATIONS                      |
| 3    | Custodial Package Menu            | Subscriber Package Menu                                |
| 4    | ACTIVE ICRs by Custodial Package  | Print ACTIVE by Subscribing Package                    |
| 5    | Select PACKAGE NAME: EC       | START WITH SUBSCRIBING PACKAGE: RA// EVENT CAPTURE |
| 6    | DEVICE HOME// \<Enter\>       | GO TO SUBSCRIBING PACKAGE: LAST// EVENT CAPTURE    |
| 7    | This step blank on purpose        | DEVICE: \<Enter\>                                  |

<span id="_Ref100844546" class="anchor"></span>Table File Export

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture does not require site parameters.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information related to files used by the ECS application. It identifies files exported and describes the steps necessary to obtain a list of templates and map the file flow relationships for Event Capture. Event Capture uses a series of FileMan files to store data related to workload entered via the ECS GUI.

## Global Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture with all patches installed creates the following global files: ^EC, ^ECC, ^ECD, ^ECH, ^ECJ, ^ECL, and ^ECR. Global protection and placement should be made on all of them. It is possible that one or more of these global files already exist on your system.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists the Event Capture files with all exported patches installed. VA Directive 6402 Modifications to Standardized National Software, 8/28/2013 governs these files, and can be found at the Department of Veterans Affairs Directives web site (VA Publications).

Use the List File Attributes option in VA FileMan to print the Data Dictionary (DD).

| File Number | File Name                              |
|-------------|----------------------------------------|
| 720.1       | EVENT CAPTURE LOG                      |
| 720.3       | EC EVENT CODE SCREENS                  |
| 720.4       | EC PROCEDURE REASON                    |
| 720.5       | EC EVENT CODE SCREENS/PROC REASON LINK |
| 721         | EVENT CAPTURE PATIENT                  |
| 722         | EVENT CAPTURE PROVIDER                 |
| 723         | MEDICAL SPECIALTY                      |
| 724         | DSS UNIT                               |
| 725         | EC NATIONAL PROCEDURE                  |
| 726         | EVENT CAPTURE CATEGORY                 |

<span id="_Ref100844534" class="anchor"></span>Table Mapping File Flow

### List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following Data Dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data are supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

## Templates and File Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 lists the steps from the VistA Systems Manager Menu to obtain the templates and to map the file flow relationships for Event Capture with all patches installed.

<table>
<caption><p><span id="_Ref100844483" class="anchor"></span>Table VA FileMan Access Codes</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Steps</strong></th>
<th><strong>Templates</strong></th>
<th><p><strong>File Flow</strong></p>
<p><strong>(Relationships between Files)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>VA FileMan</td>
<td>VA FileMan</td>
</tr>
<tr class="even">
<td>2</td>
<td>Print File Entries</td>
<td>Data Dictionary Utilities</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>OUTPUT FROM WHAT FILE:</p>
<p><strong>Print Template</strong> or <strong>Sort Template</strong></p></td>
<td>Map Pointer Relations</td>
</tr>
<tr class="even">
<td>4</td>
<td>SORT BY: Name// <strong>Name</strong></td>
<td>Select PACKAGE NAME: Event Capture</td>
</tr>
<tr class="odd">
<td>5</td>
<td>START WITH NAME: FIRST//EC&lt;<strong>Enter</strong>&gt;</td>
<td>Remove FILE: &lt;<strong>Enter</strong>&gt;</td>
</tr>
<tr class="even">
<td>6</td>
<td>GO TO NAME: ECW// &lt;<strong>Enter</strong>&gt;</td>
<td>Add FILE: (Enter name or file number for files you want to include in the output. This prompt will repeat until the next step.)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>WITHIN NAME, SORT BY: &lt;<strong>Enter</strong>&gt;</td>
<td>Add FILE: &lt;<strong>Enter</strong>&gt;</td>
</tr>
<tr class="even">
<td>8</td>
<td>FIRST PRINT FIELD: Name</td>
<td>Enter name of file group for optional graph header: EVENT CAPTURE// &lt;<strong>Enter</strong>&gt;</td>
</tr>
<tr class="odd">
<td>9</td>
<td>THEN PRINT FIELD: &lt;<strong>Enter</strong>&gt;</td>
<td>DEVICE: HOME// &lt;<strong>Enter</strong>&gt; HOME (CRT)</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Heading (S/C):</p>
<p>PRINT TEMPLATE LIST// &lt;<strong>Enter</strong>&gt;</p></td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>START AT PAGE: 1 &lt;<strong>Enter</strong>&gt;</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>DEVICE: &lt;<strong>Enter</strong>&gt; HOME (CRT) Right Margin: 80// &lt;<strong>Enter</strong>&gt;</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref100844483" class="anchor"></span>Table VA FileMan Access Codes

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains relevant information for ECS GUI application software routines and describes the actions to perform in order to obtain a list of routines supporting ECS that are implemented in the back-end Massachusetts General Hospital Utility Multi-Programming System (MUMPS) environment. Event Capture is comprised of a number of MUMPS routines that enable entering, editing, and deleting of data, as well as producing reports. These routines are used to accomplish user-initiated tasks through the ECS GUI component.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards. The XINDEX output may include the following components: list of compiling errors and warnings, routine listing, local variables, global variables, naked global references, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards that exist in the selected routines, and to see how routines interact with one another. That is, which routines call or are called by other routines.

To run XINDEX for the Event Capture software, specify the following namespace at the "Routine:" prompt: EC\*. Event Capture initialization routines that reside in the User Class Identifier (UCI) in which XINDEX is being run, as well as compiled template routines found within the Event Capture namespace, should be omitted at the "Routine:" prompt. To omit routines from selection, preface the namespace with a tick mark ( ‘ ).

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture software uses Integration Agreement 4460 to call the Application Programmer Interface (API) to store and retrieve data for the PROVIDER MULTIPLE field (#42) in the EVENT CAPTURE PATIENT file (#721).

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following steps from the VistA Systems Manager Menu to obtain the MUMPS routines contained in the Event Capture software:

1.  Programmer Options
2.  Routine Tools
3.  First Line Routine Print
4.  All Routines? No =\> \<Enter\>
5.  Routine: EC\*
6.  Routine: ‘ECT\*
7.  Routine: ‘ECW\*
8.  Routine: ‘ECX\*
9.  Routine: ‘EC1\*
10. Routine: \<Enter\>
11. (A)lpha, (D)ate, (P)atched, OR (S)ize ORDER: A//\<Enter\>
12. Include line (2), Include lines 2&(3), (N)one: None//\<Enter\>
13. DEVICE: HOME// \<Enter\>SSH VIRTUAL TERMINALRight Margin: 80// \<Enter\>

Steps 6 through 9 are to exclude those routines from appearing in the list.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the main menu and submenus available in the ECS GUI application. The user must hold the appropriate security keys in order to access all options.

## Event Capture Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security keys are assigned in VistA using the menu option Key Management, and then choosing the submenu Allocation of Security Keys.

- ECMGR: Gives a user access to the ECS Management Menu. This key is intended to be used only for Event Capture Managers.
- ECACCESS: Gives a user the ability to grant or remove DSS Unit access. Note that if the user also has the ECMGR key, ECACCESS will not have any effect.
- ECALLU: Gives a user access to all DSS Units (super user). This should be assigned only to those managing the software (i.e., holders of the ECMGR key).
- ECNORPT: Restricts the user from access to the Event Capture Reports.
- ECSPSH: Gives a user access to upload data from a spreadsheet.
1.  
- When granting access to DSS Units by user (Figure 1), if the desired name is unavailable, confirm the following:
1.  The user has an active CPRS TAB in the NEW PERSON file (#200).
2.  The user has the OR CPRS GUI CHART option in their secondary menu option.
3.  The user is not DISusered.
4.  The user has the "AUSER" cross-reference in the NEW PERSON file (#200); all active users should already have this.

<span id="_Ref100840860" class="anchor"></span>Figure Grant Access to DSS Units by User

![](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/002.png)

## Main Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture software contains the Data Entry, Spreadsheet, Reports, and Management Menu options. Figure 2 shows these major menu options as they appear in the ECS GUI.

<span id="_Ref100843946" class="anchor"></span>Figure Event Capture Main Menu

![](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/003.png)

In cases where the user has the ECACCESS key, the menu will have an Access by User option in place of the Management Menu option, as shown in Figure 3.

<span id="_Ref100844131" class="anchor"></span>Figure Event Capture Main Menu for Users with ECACCESS Key

![](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/004.png)

## Submenu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 4 shows the submenu items that are available when the Data Entry option is selected from the Main Menu.

<span id="_Ref100844148" class="anchor"></span>Figure Data Entry Menu Screen

![Figure 5 shows the Spreadsheet Upload form that becomes active when the Spreadsheet option is selected from the Main Menu. The user must hold the ECSPSH security key in order to access this screen.](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/005.png)

*Figure 5 shows the Spreadsheet Upload form that becomes active when the Spreadsheet option is selected from the Main Menu. The user must hold the ECSPSH security key in order to access this screen.*

<span id="_Ref100844186" class="anchor"></span>Figure Spreadsheet Menu Screen

![Figure 6 shows the submenu items that are available when the Reports option is selected from the Main Menu and the user does not hold the ECMGR security key.](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/006.png)

*Figure 6 shows the submenu items that are available when the Reports option is selected from the Main Menu and the user does not hold the ECMGR security key.*

<span id="_Ref95910329" class="anchor"></span>Figure Reports Menu Screen without ECMGR Option

![Figure 7 shows the submenu items that are available when the Reports option is selected from the Main Menu and the user holds the ECMGR security key.](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/007.png)

*Figure 7 shows the submenu items that are available when the Reports option is selected from the Main Menu and the user holds the ECMGR security key.*

<span id="_Ref95910343" class="anchor"></span>Figure Reports Menu Screen with ECMGR Options

![Figure 8 shows the submenu items that are available when the Management Menu option is selected from the Main Menu. The user must hold the ECMGR security key in order to access this menu.](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/008.png)

*Figure 8 shows the submenu items that are available when the Management Menu option is selected from the Main Menu. The user must hold the ECMGR security key in order to access this menu.*

<span id="_Ref100844267" class="anchor"></span>Figure Management Menu Screen

![](event-capture-version-2-0-gui-technical-manual-updated-ec-2-170/009.png)

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can set up an ECS mail group in VistA to receive relevant ECS notifications. Contact IT to set up a VistA ECS Mail Group so more than one person receives ECS administrative messages.

More information regarding current ECS package administrative email messages can be obtained from the ECS User Guide, which can be found on the [VDL](#references).

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the Integration Control Registrations (ICRs) created and/or used by ECS. They are categorized by the custodian or subscriber relationship to the software. No private ICRs are documented below.

<u>Custodian:</u>

ICR \#96

- Type: File
- File \#730
- Root: ECC(730,

ICR \#97

- Type: File.
- File \#730
- Root: ECC(730,

ICR \#205

- Type: File
- Root: ECC(723,

ICR \#249

- Type: Other

ICR \#1561

- Type: File
- File \#724
- Root: ECD(

ICR \#1869

- Type: File
- File \#720
- Root: ECP(

ICR \#1870

- Type: File
- File \#720.1
- Root: EC(720.1,

ICR \#1872

- Type: File
- File \#720.3
- Root: ECJ(

ICR \#1873

- Type: File
- File \#721
- Root: ECH(

ICR \#1874

- Type: File
- File \#725
- Root: EC(725,

ICR \#1875

- Type: File
- File \#726
- Root: EC(726,

ICR \#4131

- Type: Routine
- Routine: ECRRPC

ICR \#4460

- Type: Routine
- Routine: ECPRVMUT

ICR \#6009

- Type: File
- File \#720.3
- Root: ECJ(

ICR \#6010

- Type: Routine
- Routine: ECUERPC

ICR \#6011

- Type: Routine
- Routine: ECUERPC1

ICR \#6012

- Type: Routine
- Routine: ECFLRPC

ICR \#6013

- Type: File
- File \#724
- Root: ECD(

ICR \#6016

- Type: Routine
- Routine: ECUMRPC1

ICR \#6155

- Type: File
- File \#200
- Root: VA(200,D0,EC

ICR \#10100

- Type: File
- File \#730
- Root: ECC(730

<u>  
</u><u>Subscriber:</u>

ICR \#322 – DBIA322

- Custodial Package: REGISTRATION
- Usage: Controlled Subscription
- Type: File
- File \#45.7
- Root: DIC(45.7,

ICR \#406 – DBIA406

- Custodial Package: SCHEDULING
- Usage: Controlled Subscription
- Type: Routine
- Routine: SDCO21

ICR \#427 – DBIA427

- Custodial Package: REGISTRATION
- Usage: Controlled Subscription
- Type: File
- File \#8
- Root: DIC(8,

ICR \# 432 — DBIA432

- Custodial Package: KERNEL
- Usage: Controlled Subscription
- Type: File
- File \#49
- Root: DIC(49,

ICR \#491 – DBIA491

- Custodial Package: KERNEL
- Usage: Controlled Subscription
- Type: File
- File \#7
- Root: DIC(7,

ICR \#492 – DBIA492

- Custodial Package: IFCAP
- Usage: Controlled Subscription
- Type: File
- File \#420.1
- Root: PRCD(420.1,

ICR \#510 – DISV

- Custodial Package: VA FILEMAN
- Usage: Controlled Subscription
- Type: File
- File \#
- Root: DISV(

ICR \#954 – DBIA954

- Custodial Package: IFCAP
- Usage: Controlled Subscription
- Type: Routine
- Routine: PRCSREC2

ICR \# 1531 — DBIA1531

- Custodial Package: DSS - DECISION SUPPORT SYSTEM EXTRACT
- Usage: Controlled Subscription
- Type: File
- File \#727.815
- Root: ECX(727.815,

ICR \#1579 – SCHEDULING CLASSIFICATION

- Custodial Package: SCHEDULING
- Usage: Controlled Subscription
- Type: Routine
- Routine: SDCO22

ICR \#1623 – SCDXUAPI - OCCASION OF SERVICE ENTRY

- Custodial Package: SCHEDULING
- Usage: Controlled Subscription
- Type: Routine
- Routine: SCDXUAPI

ICR \#1889 – ADD/EDIT/DELETE PCE DATA SILENTLY

- Custodial Package: PCE PATIENT CARE ENCOUNTER
- Usage: Controlled Subscription
- Type: Routine
- Routine: PXAPI

ICR \#1890 – DBIA1889-B

- Custodial Package: PCE PATIENT CARE ENCOUNTER
- Usage: Controlled Subscription
- Type: Routine
- Routine: PXAPI

ICR \#1902 – DBIA1900-C

- Custodial Package: PCE PATIENT CARE ENCOUNTER
- Usage: Controlled Subscription
- Type: Routine
- Routine: VSIT

ICR \#1905 – RETURN SELECTED VISITS FROM VSIT

- Custodial Package: PCE PATIENT CARE ENCOUNTER
- Usage: Controlled Subscription
- Type: Routine
- Routine: VSIT

ICR \#2058 — PACKAGE FILE LOOKUP

- Custodial Package: KERNEL
- Usage: Controlled Subscription
- Type: File
- File \#9.4
- Root: DIC(9.4,

ICR \#2251 – DBIA-2251

- Custodial Package: KERNEL
- Usage: Controlled Subscription
- Type: File
- File \#4
- Root: DIC(4,

ICR \#2741 – OE/RR calls to GMPLUTL2

- Custodial Package: PROBLEM LIST
- Usage: Controlled Subscription
- Type: Routine
- Routine: GMPLUTL2

ICR \#3371 – ORWU HASKEY

- Custodial Package: ORDER ENTRY/RESULTS REPORTING
- Usage: Controlled Subscription
- Type: Remote Procedure

ICR \#3834 — CSL Cost Center table update

- Custodial Package: COMMUNICATIONS SERVICE LIBRARY
- Usage: Controlled Subscription
- Type: Routine
- Routine: CSLEC

ICR \# 3852 — CSL Cost Center file 536.3

- Custodial Package: COMMUNICATIONS SERVICE LIBRARY
- Usage: Controlled Subscription
- Type: File
- File \#536.3
- Root: CSLCC(

ICR \#3859 – APPOINTMENT DATA BY PATIENT

- Custodial Package: SCHEDULING
- Usage: Controlled Subscription
- Type: Routine
- Routine: SDAMA201

ICR \#4069 — HL7 MESSAGE TEXT FILE (#772)

- Custodial Package: HEALTH LEVEL SEVEN
- Usage: Controlled Subscription
- Type: File
- File \#772
- Root: ECX(772,

ICR \#4255 — CSL REFERENCING PARAMETERS

- Custodial Package: COMMUNICATIONS SERVICE LIBRARY
- Usage: Controlled Subscription
- Type: Other

ICR \#4652 – CLNCHK - SDUTL2 (RESTRICTING STOP CODE)

- Custodial Package: SCHEDULING
- Usage: Supported
- Type: Routine
- Routine: SDUTL2

ICR \#5747 — ICD Data Extraction

- Custodial Package: DRG GROUPER
- Usage: Controlled Subscription
- Type: Routine
- Routine: ICDEX

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the 49 Remote Procedure Call (RPC) entry points and parameters created and/or used by ECS. Click any of the RPCs below to see details.

1.  
2.  [EC CLASHELP](#EC_CLASHELP)
3.  [EC DELETE FILE ENTRY](#EC_DELETE_FILE_ENTRY)
4.  [EC DELETE TEST PATIENT DATA](\l)
5.  [EC DIEDON](#DIEDON)
6.  [EC DSSCATCHECK](#DSSCATCHECK)
7.  [EC FILER](#FILER)
8.  [EC GET DEFAULT PROVIDER](#GET_DEFAULT_PROVIDER)
9.  [EC GETBATPROCS](#GETBATPROCS)
10. [EC GETCAT](#GETCAT)
11. [EC GETCPTLST](#GETCPTLST)
12. [EC GETDATE](#GETDATE)
13. [EC GETDSSECS](#GETDSSECS)
14. [EC GETDSSUNIT](#GETDSSUNIT)
15. [EC GETDSSUNITUSRS](#GETDSSUNITUSRS)
16. [EC GETECLOC](#GETECLOC)
17. [EC GETECSCATS](#GETECSCATS)
18. [EC GETECSCREEN](#GETECSCREEN)
19. [EC GETECSDETAIL](#GETECSDETAIL)
20. [EC GETECSPROCS](#GETECSPROCS)
21. [EC GETENCDXS](#GETENCDXS)
22. [EC GETIEN](#GETIEN)
23. [EC GETLIST](#GETLIST)
24. [EC GETLOC](#GETECLOC)
25. [EC GETNATPX](#GETNATPX)
26. [EC GETPATCH](\l)
27. [EC GETPATCLASTAT](#GETPATCLASTAT)
28. [EC GETPATELIG](#GETPATELIG)
29. [EC GETPATINFO](#GETPATINFO)
30. [EC GETPATPROCS](#GETPATPROCS)
31. [EC GETPRBLST](#GETPRODEFS)
32. [EC GETPRODEFS](#GETPRODEFS)
33. [EC GETPROVIDER](#GETPROVIDER)
34. [EC GETPXLST](#GETPXLST)
35. [EC GETPXMODIFIER](#GETPXMODIFIER)
36. [EC GETPXREASON](#GETPXREASON)
37. [EC GETSCNHELP](#GETSCNHELP)
38. [EC GETUSRDSSUNIT](#GETUSRDSSUNIT)
39. [EC GETVERSION](#GETVERSION)
40. [EC GETVISITINFO](#GETVISITINFO)
41. [EC ICD10IMPLEMEN-TATIONDATE](#ICD10IMPLEMENTATIONDATE)
42. [EC RECENT VISITS](#RECENT_VISITS)
43. [EC REPORTS](#REPORTS)
44. [EC SPACEBAR](#SPACEBAR)
45. [EC VALIDATE SPREADSHEET DATA](#VALIDATE)
46. [ORWU DEVICE](#ORWU_DEVICE)
47. [ORWU HASKEY](#ORWU_HASKEY)
48. [ORWU NEWPERS](#ORWU_NEWPERS)
49. [ORWU USERINFO](#ORWU_USERINFO)
50. [SC PATIENT LOOKUP](#SC_PATIENT_LOOKUP)
1.  <span id="EC_CLASHELP" class="anchor"></span>
2.  EC CLASHELP — Returns the service-connected and related disabilities information for the selected patient.

TAG: CLHLP

ROUTINE: ECUERPC2

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: RPC Broker entry point for classification help

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION:  Input key ECARY consists of the following pieces -

> ECDFN — Patient DFN from file (#2)

> ECKY — Key to provide help on.  Example ECKY='SC' provides help on service connection.

RETURN PARAMETER DESCRIPTION:  Array of help text for classification.

3.  <span id="EC_DELETE_FILE_ENTRY" class="anchor"></span>EC DELETE FILE ENTRY - A general purpose for deletion of entry in ECS files which uses parameters to determine which file and entry to delete.

TAG: ECDEL

ROUTINE: ECUMRPC2

RETURN VALUE TYPE: GLOBAL ARRAY

DESCRIPTION: A general purpose Event Capture routine for deletion of entry in ECS files.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LIST

DESCRIPTION: The input array ECARY contains the file number and the IEN number of the entry to be deleted.

> ECARY("ECFILE") — the file number where the entry to be deleted

> ECARY("IEN") — the entry number to be deleted

| <u>ECFILE</u> | <u>Option</u>         |
|---------------|-----------------------|
| 720.3         | EC Event Code Screens |
| 724           | DSS Unit              |

<span id="_Ref100844468" class="anchor"></span>Table Acronyms

RETURN PARAMETER DESCRIPTION: Returns a flag of success or failure and error message.

4.  EC DELETE TEST PATIENT DATA — Delete test patient data from the EVENT CAPTURE PATIENT file (#721).

TAG: DTPD

ROUTINE: ECUMRPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: This RPC is used to delete any test patient data from the EVENT CAPTURE PATIENT file (#721).

If the patient is identified as a test patient and the procedure associated with the test patient record is not in the range of CH103 to CH109 then the record will be deleted.  If the procedure is in this range for a test patient, the record will not be deleted. Test patients, with procedures in this range, are allowed for recording Chaplain workload.

This RPC can be invoked in two modes.  The first mode, "I" is for gathering information about the account, the date/time of the last deletion, the user who ran the deletion and the status of the deletion process. The second mode, "D", is for deleting patient records as defined above.

Care should be used when running this RPC as the data cannot be restored once deleted. In addition, this process could take a while to complete. The amount of time needed will vary based on the total number of records to be reviewed and the total number of records to be deleted.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: This will hold the mode in which you want to run the RPC. The two possible modes are "I"nformation or "D"elete.

RETURN PARAMETER DESCRIPTION: Depending on the mode, the return results will vary.  

For the "I"nformational mode, the return value will be account type (test or production)^network name^date/time deletion last completed^user who last ran the deletion^status of the deletion (0 not running/1 running).

For the "D"eletion mode, the return value will be 0 if the task couldn't be queued to run in the background or 1 to indicate that it was successfully tasked to the background. <span id="DIEDON" class="anchor"></span>

5.  EC DIEDON — Get the date of death for the patient.

TAG: ECDOD

ROUTINE: ECUERPC2

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: This RPC returns a patient's date of death.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input variable ECARY contains the patient's DFN.

RETURN PARAMETER DESCRIPTION: The RPC returns either of the following pieces of data as output:

> 1\. 0^Patient DFN is not defined

> 2\. DOD internal FileMan format^message when patient died

> 3\. ^ \[if patient is not dead\]

6.  <span id="DSSCATCHECK" class="anchor"></span>EC DSSCATCHECK — Check whether the Category is used in an Event Code Screen.

TAG: CATCHK

ROUTINE: ECUMRPC1

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: Checks whether category is used in an Event Code Screen.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Variable ECARY contains the DSS Unit IEN (file \#724) that will be checked to determine if category exists.

RETURN PARAMETER DESCRIPTION: Returns a value of 1 or 0 indicating whether category is used in Event Code Screen, 1-Yes or 0-No.

7.  <span id="FILER" class="anchor"></span>EC FILER — A general purpose filer which uses parameters to determine which file and field to update.

TAG: FILE

ROUTINE: ECFLRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: A general purpose Event Capture routine used when filing data into ECS files.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LIST

DESCRIPTION: The input array ECARY defines all the fields and values needed for a particular file.  The variable ECARY("ECFILE") must always be set to the file number where data will be saved. The following are the options and files available:

| <u>ECFILE</u> | <u>Option</u>                                        |
|---------------|------------------------------------------------------|
| 4             | Event Capture Locations                              |
| 200           | Allocate/Deallocate users to Unit                    |
| 200A          | Allocate/Deallocate Units to user                    |
| 721           | Event Capture Patient File                           |
| 722           | Event Capture Provider File (Non Licensed Providers) |
| 724           | DSS Unit                                             |
| 720.3         | EC Event Code Screens                                |
| 720.4         | Event Code Reasons                                   |
| 725           | EC Local Procedure                                   |
| 726           | Event Capture Category                               |

<span id="_Ref100844436" class="anchor"></span>Table Glossary of Terms

RETURN PARAMETER DESCRIPTION: Returns a flag of success or failure, or a list of error codes.

8.  <span id="GET_DEFAULT_PROVIDER" class="anchor"></span>EC GET DEFAULT PROVIDER — Get the default provider based on the DSS Unit and the data entry user.

TAG: ECDEFPRV

ROUTINE: ECUERPC2

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: This remote procedure will return the default provider based on the DSS Unit and the user entering data into Event Capture.

If the user is an active provider then they will be the default regardless of the DSS unit's send to PCE setting.

If the user is not an active provider then a check is made to see the last person they referenced in the NEW PERSON file (#200). If that person is an active provider then they will be the default.

If the DSS unit's send to PCE setting is set to send no records then the user will be the default if they are found in the EVENT CAPTURE PROVIDER file (#722).  If the user is not identified as an event capture provider then a check is made to see the last person they referenced in the NEW PERSON file (#200).  If that person is in the EVENT CAPTURE PROVIDER file (#722) then they will be the default.

If none of the checks produces a provider then there will be no default identified.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input variable ECARY contains the IEN of the DSS unit concatenated with the date/time of the procedure. If a date/time isn't sent, today's date will be assumed.

RETURN PARAMETER DESCRIPTION: The RESULTS variable will contain either the IEN^User Name or -1 if no default is found.

9.  <span id="GETBATPROCS" class="anchor"></span>EC GETBATPROCS — Get patient procedures based on the search parameters.

TAG: PROCBAT

ROUTINE: ECUERPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns an array with entries from EVENT CAPTURE PATIENT FILE \#721 for patients for a specific procedure.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrows:

> 1\. ECLOC — Location IEN

> 2\. ECUNT — DSS unit IEN

> 3\. ECC — Category IEN

> 4\. ECP — Procedure IEN

> 5\. ECSD — Start Date

> 6\. ECED — End Date

RETURN PARAMETER DESCRIPTION: Returns an array of Event Capture Patients with the following data:

> 1\. 721 IEN

> 2\. Patient name

> 3\. Procedure Date and Time

> 4\. Primary Diagnosis

> 5\. Ordering Section

> 6\. Associated Clinic

10. <span id="GETCAT" class="anchor"></span>EC GETCAT — Get all Category records from the EVENT CAPTURE CATEGORY file (#726).

TAG: CAT

ROUTINE: ECUMRPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns a list of active and/or inactive categories from file \#726.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Status of A-ctive, I-nactive or B-oth.

RETURN PARAMETER DESCRIPTION: Returns an array with categories. Data pieces as follows:

> 1\. IEN of Category

> 2\. Name of Category

> 3\. Creation Date

> 4\. Inactive Date

11. <span id="GETCPTLST" class="anchor"></span>EC GETCPTLST — Get all CPT codes from the CPT file (#81) that match the search string.

TAG: CPTFND

ROUTINE: ECUMRPC2

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Performs a search on a CPT string and returns an array list of matches from file \#81.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: CPT search string.

RETURN PARAMETER DESCRIPTION: Returns a global array with CPT IEN, code and name respectively.

12. <span id="GETDATE" class="anchor"></span>EC GETDATE — Get the user-entered date in FileMan date format.

TAG: ECDATE

ROUTINE: ECUURPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Broker call returns the client date as a Fileman internal and external date format.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Client entered date and date flag passed in variable ECARY:

> DTSTR — Date String, eg N, T@800, 4/15@1205

> FLG — Date Flag, eg R means time is required

RETURN PARAMETER DESCRIPTION: Returns in variable RETURN:- Fileman internal date^External date format. If date is invalid, returns 0^Invalid Date/Time.

13. <span id="GETDSSECS" class="anchor"></span>EC GETDSSECS — Get a list of Event Code Screens from the EC EVENT CODE SCREENS file (#720.3) based on a DSS Unit.

TAG: DSSECS

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns a list of Event Code Screen from EC EVENT CODE CREENS FILE \#720.3 based on a DSS Unit and location.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the value for DSS Unit

> ECD — DSS Unit IEN

> ECL — Location

RETURN PARAMETER DESCRIPTION: Returns an array with data Event Code screens as follows:

> 1\. 720.3 IEN

> 2\. Procedure 5 digit code and description

> 3\. Location

> 4\. Status (active, inactive)

> 5\. Category description

> 6\. Synonym

14. <span id="GETDSSUNIT" class="anchor"></span>EC GETDSSUNIT — Get the DSS Units from the DSS UNIT file (#724) based on the input parameters.

TAG: DSSUNT

ROUTINE: ECUMRPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns array with active and/or inactive DSS units from file 724.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Optional input variable ECARY containing the following ^ delimited pieces:

> Piece 1 - Active or inactive DSS Units (optional). A-ctive (default), I-nactive, B-oth

> Piece 2 - Specific DSS Unit name (optional)

> Piece 3 - Specific DSS IEN (optional)

> Piece 4 - Specific DSS Unit number (optional)

RETURN PARAMETER DESCRIPTION: The results array contains data for DSS units as follows:

> 1\. IEN of DSS Unit

> 2\. Name of DSS Unit

> 3\. IEN of DSS Unit (repeated)

> 4\. Inactive Flag

> 5\. Send to PCE

> 6\. Unit Number

> 7\. Service

> 8\. Medical Specialty

> 9\. Cost Center

> 10\. Associated Stop Code (if OOS or send no records PCE setting)

> 11\. Category flag

> 12\. Default date entry

> 13\. Credit Stop Code (only if PCE setting is send no records)

> 14\. CHAR4 code (only if PCE setting is send no records)

> 15\. Allow duplicate record filing on spreadsheet upload

15. <span id="GETDSSUNITUSRS" class="anchor"></span>EC GETDSSUNITUSRS — Get the users who have access to the specified DSS Unit.

TAG: ECUSR

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns an array of users with access to a particular DSS unit. User access to a DSS unit is determined from the NEW PERSON file (#200).

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30

DESCRIPTION: DSS unit IEN must be passed in as input parameter.

RETURN PARAMETER DESCRIPTION: Returns an array list with user name and IEN from the NEW PERSON file (#200).

16. <span id="GETECLOC" class="anchor"></span>EC GETECLOC — Get the Event Capture Locations from the INSTITUTION file (#4).

TAG: ECLOC

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns an array with all active Event Capture locations from the INSTITUTION file (#4).

RETURN PARAMETER DESCRIPTION: Returns array with value set to location and location IEN respectively.

17. <span id="GETECSCATS" class="anchor"></span>EC GETECSCATS — Get the Category for an Event Code Screen based on the Location and DSS Unit.

TAG: CAT

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns an array of categories for an Event Code screen based on a specific location and DSS unit.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrow.

> 1\. ECL — Location IEN

> 2\. ECD — DSS Unit IEN

> 3\. ECCSTA — Category status, A-ctive (default), I-nactive, B-oth

RETURN PARAMETER DESCRIPTION: Returns an array of categories with data pieces as follows:

> 1\. Category IEN

> 2\. Category description

18. <span id="GETECSCREEN" class="anchor"></span>EC GETECSCREEN — Get the records from the EC EVENT CODE SCREENS file (#720.3).

TAG: ECSCN

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns a list active, inactive or both of Event Code Screens from EC EVENT CODE SCREENS file (#720.3).

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY can contains the following elements separated by up-arrow.

> STAT — Active and/or inactive Event Code Screens \[A-ctive (default), I-nactive, B-oth\]

> LOCIEN — Location IEN (optional)

> DSSIEN — DSS IEN (optional)

If no parameters are passed, a status of active is assumed as well as all locations.

If an LOC IEN is passed, then only the event codes screens associated with that location are returned.

If a DSS IEN is passed then only the event code screens associated with that DSS Unit are returned.

RETURN PARAMETER DESCRIPTION: The result array contains the following data separated by up-arrow. 

> 1\. 720.3 IEN

> 2\. Location description

> 3\. DSS Unit description

> 4\. Category Description

> 5\. Procedure 5-digit code and description

19. <span id="GETECSDETAIL" class="anchor"></span>EC GETECSDETAIL - Get detailed information for the selected record from the EC EVENT CODE SCREENS file (#720.3).  

TAG: ECSDTLS

ROUTINE: ECUMRPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns details on a specific Event Code Screen from the EC EVENT CODE SCREENS FILE \#720.3.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input parameter ECARY contains the Event code screen IEN.

RETURN PARAMETER DESCRIPTION: The return variable contains the following data separated by up-arrows.

> 1\. 720.3 IEN

> 2\. Event Code Screen name

> 3\. Synonym

> 4\. Volume

> 5\. Associated Clinic

> 6\. Procedure Reason indicator

> 7\. Status

> 8\. Send to PCE status - 1 if sent, 0 if not

20. <span id="GETECSPROCS" class="anchor"></span>EC GETECSPROCS - Get the procedures for an Event Code Screen based on the Location, DSS Unit and Category.  

TAG: PROC

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns an array of procedures for an Event Code screen (file \#720.3). Event code screens are based on location, DSS unit and Category.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrow.

> 1\. ECL — Location IEN

> 2\. ECD — DSS Unit IEN

> 3\. ECC — Category IEN

RETURN PARAMETER DESCRIPTION: Returns an array of procedures. Data pieces as follows:

> 1\. EC National Number SPACE Procedure Name SPACE \[Synonym\]

> 2\. Procedure Code

> 3\. CPT Code

> 4\. Default Volume

> 5\. Event Code Screen IEN

21. <span id="GETENCDXS" class="anchor"></span>EC GETENCDXS - Get the primary diagnosis and any secondary diagnoses for a patient encounter.  

TAG: ENCDXS

ROUTINE: ECUERPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns a patient encounter primary and secondary diagnosis codes from the Event Capture Patient file (#721).

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY has the following pieces of data separated by up-arrows.

> 1\. ECDFN — Patient IEN (#200)

> 2\. ECDT — Procedure date and time (FileMan format)

> 3\. ECL — Location IEN

> 4\. EC4 — Clinic IEN

RETURN PARAMETER DESCRIPTION: Returns an array with patient encounter diagnosis information.

> 1\. Primary/secondary flag (1-primary, 0-secondary)

> 2\. Diagnosis IEN

> 3\. Diagnosis code and description

22. <span id="GETIEN" class="anchor"></span>EC GETIEN — Get the Internal Entry Number (IEN) for a record.

TAG: FNDIEN

ROUTINE: ECUURPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns the IEN from a file.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following elements

> 1\. FIL — File number

> 2\. TXT — .01 description

RETURN PARAMETER DESCRIPTION: Returns a file IEN.

23. <span id="GETLIST" class="anchor"></span>EC GETLIST — Get records from the associated file which match the search criteria entered.

TAG: SRCLST

ROUTINE: ECUMRPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: This call is used to perform a search on a file based on a search string.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input string ECARY contains six pieces separated by "^"

> ECFIL — File to search

> ECSTR — Search string

> ECDIR — Search order

> ECNUM — (Optional) Number of records to return \[DEFAULT: 44\]

> ECADT — (Optional) date to determine clinic status (active/inactive)

> ECLOC — (Optional) location (IEN) to filter associated clinic list

> ECTYPE — (Optional) primary or secondary stop codes desired

> ECOOS — (Optional) Set to "OOS" to only see "OOS" related

RETURN PARAMETER DESCRIPTION: Returns a list of values based on the search criteria.

24. EC GETLOC — Get all Locations from the INSTITUTION file (#4).

TAG: GLOC

ROUTINE: ECUMRPC2

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This broker entry point returns all active, inactive or both locations from file \#4.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values:

> STAT — Active, inactive or both (optional)

RETURN PARAMETER DESCRIPTION: Results array contain the following values:

> 1\.  Location IEN

> 2\.  Location description

> 3\.  State

> 4\.  Current Location Flag

> 5\.  Facility Type

> 6\.  Station Number

25. <span id="GETNATPX" class="anchor"></span>EC GETNATPX — Get the Procedures, both local and national, from the EC NATIONAL PROCEDURE file (#725).

TAG: ECNATPX

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns an array of active, inactive or both of Event Capture national and local Procedures from file \#725.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following subscripted elements:

> ECPX — Procedures to output; L- local, N- National, B- Both

> STAT — Active or inactive EC Nat Codes; A-ctive (default), I-nactive, B-oth

If no values are passed in it defaults to Local and Active.

RETURN PARAMETER DESCRIPTION: Returns an array of EC local/national procedures with the following pieces of data separated by an up-arrow.

> 1\. File \#725 IEN

> 2\. Name

> 3\. National Number

> 4\. Inactive Date

> 5\. Synonym

> 6\. CPT IEN

> 7\. CPT Code

> 8\. CPT Short Name

26. EC GETPATCH — Indicates whether the specified patch has been installed.

TAG: PATCH

ROUTINE: ECUURPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: Broker call checks to see if a patch has been installed. Returns 1 if patch is installed.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input a patch number, ex. EC\*2.0\*28.

RETURN PARAMETER DESCRIPTION: Returns a 1 if patch has been installed, otherwise returns a 0.

27. <span id="GETPATCLASTAT" class="anchor"></span>EC GETPATCLASTAT — Get the patient's classification status based on the date/time of the procedure.

TAG: PATCLAST

ROUTINE: ECUERPC1

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns a patient's in/out status and classifications.

Classifications are: Agent Orange, Ionizing Radiation, SC Condition, Environmental Contaminants, Military Sexual Trauma, Head/Neck Cancer, Combat Veteran, and Project 112/SHAD.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrow.

> 1\. ECDFN — Patient IEN (#2)

> 2\. ECD — DSS Unit IEN (#724)

> 3\. ECDT — Procedure date and time (FileMan format)

RETURN PARAMETER DESCRIPTION: Returns a single line with values for a patient's status and classifications.

Data are delimited by (^) and '~'. Values after the '~' refer to those classifications that must be asked for when the answer to the service-connected classification is 'No'.

Pieces delimited by '^' are:

> 1\. Patient Status: I for inpatient or O for outpatient

> 2-9. Classification:

> 2\. Agent Orange

> 3\. Ionizing Radiation

> 4\. SC Condition

> 5\. Environmental Contaminants

> 6\. Military Sexual Trauma

> 7\. Head/Neck Cancer

> 8\. Combat Veteran

> 9\. Project 112/SHAD

 Data delimited by '~' follow those of '^'. Pieces as follows:

> 1\. Agent Orange

> 2\. Ionizing Radiation

> 3\. Environmental Contaminants<span id="GETPATELIG" class="anchor"></span>

28. EC GETPATELIG — Get a list of the patient's eligibilities.

TAG: ELIG

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns a list of patient eligibilities.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable, ECARY contains the patient IEN (#2).

RETURN PARAMETER DESCRIPTION: Returns an array of patient eligibilities as follows:

> 1\. Primary/secondary Elig flag (Flag 1-primary, 0-secondary)

> 2\. Eligibility IEN

> 3\. Eligibility description

29. <span id="GETPATINFO" class="anchor"></span>EC GETPATINFO — Get specific patient information from the EVENT CAPTURE PATIENT file (#721) based on the input parameter.

TAG: PATINF

ROUTINE: ECUERPC1

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: This is a general purpose call that provides segments of the patient data from the Event Capture Patient File \#721.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input variable ECARY contains the following values:

> ECIEN — Event Capture Patient ien (#2)

> ECTYP — Data type to return. Types are:

> DXS — primary and secondary diagnosis codes

> MOD — modifiers

> CLASS — classification data

> OTH — other type data

RETURN PARAMETER DESCRIPTION: Based on the type data requested, returns one of the following:

> DXS — primary and secondary diagnosis codes

> MOD — modifiers

> CLASS — classification data

> OTH — other type data

30. <span id="GETPATPROCS" class="anchor"></span>EC GETPATPROCS — Get patient procedures from the EVENT CAPTURE PATIENT file (#721) based on the input criteria.

TAG: PATPROC

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns an array of patient entries from EVENT CAPTURE PATIENT FILE \#721 that matches a location, DSS unit, patient DFN, start date and end date.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrows:

> 1\. ECLOC — Location IEN

> 2\. ECPAT — Patient DFN (IEN)

> 3\. ECUNT — DSS Unit IEN

> 4\. ECSD — Start Date

> 5\. ECED — End Date

RETURN PARAMETER DESCRIPTION: Returns an array with Event Capture Patient entries with the following data:

> 1\. 721 IEN

> 2\. Procedure date and time

> 3\. Category

> 4\. Procedure

> 5\. Volume

> 6\. Provider

> 7\. Ordering Section

> 8\. Associated Clinic

> 9\. Primary Diagnoses

> 10\. Provider IEN

31. <span id="GETPRODEFS" class="anchor"></span>EC GETPRBLST — List all problems for an Event Capture patient from the PROBLEM file (#9000011).

TAG: GETPLST

ROUTINE: ECUERPC2

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Returns a problem list for an Event Capture patient.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input value, ECARY, contains the following values separated by "^"

> ECIEN - Event Capture Patient IEN.

> ECSTAT - The status of the problems to retrieve.

> A = Active problems only.

> I = Inactive problems only.

> "" or undefined = all problems regardless of status.

RETURN PARAMETER DESCRIPTION: Returns an array of problem list for an Event Capture patient. Data pieces are:

> 1\. Problem Status

> 2\. ICD Code

> 3\. ICD Code Description

> 4\. Onset Date

> 5\. Date of Last Modified

> 6\. Provider

> 7\. Service

> 8\. Current Coding System Flag(1: Current Coding System, 0: If not)

> 9\. ICD Code IEN

32. EC GETPRODEFS - Get the default Associated Clinic and the default Medical Specialty for the patient procedure.  

TAG: PRDEFS

ROUTINE: ECUERPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: This broker entry point returns the defaults for procedure data entry.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input value, ECARY, contains the following values separated by "^"

> ECL — Location IEN

> ECD — DSS Unit IEN

> ECC — Category IEN

> ECP — Procedure IEN

RETURN PARAMETER DESCRIPTION: Output value, RESULTS, contain the data pieces as follows:

> 1 — Associated Clinic IEN

> 2 — Associated Clinic

> 3 — Medical Speciality IEN

> 4 — Medical Speciality

33. <span id="GETPROVIDER" class="anchor"></span>EC GETPROVIDER — Get the list of providers who were valid on the date of the procedure.

TAG: PRVDER

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns an array of valid providers based on a procedure date.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the procedure date.

RETURN PARAMETER DESCRIPTION: Returns an array of active providers. Data pieces are as follows:

> 1\. IEN of file \#200

> 2\. Provider Name

> 3\. Occupation

> 4\. Speciality

> 5\. Subspecialty

34. <span id="GETPXLST" class="anchor"></span>EC GETPXLST — Get records from either the CPT file (#81) or the EC NATIONAL PROCEDURE file (#725) which match the search string.

TAG: PXFND

ROUTINE: ECUMRPC2

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Performs a search on a procedure string and returns an array list of matches from file \#81 and/or \#725.

User can type:

> 1\. "A.search string" to search file \#81.

> 2\. "B.search string" to search file \#725.

> 3\. "search string" to search both files.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Procedure search string.

RETURN PARAMETER DESCRIPTION: Returns a global array with:

> 1\. Procedure IEN

> 2\. Procedure Code and Name.

35. <span id="GETPXMODIFIER" class="anchor"></span>EC GETPXMODIFIER — Get the CPT modifiers for a procedure based on the procedure date.

TAG: ECPXMOD

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Returns CPT modifier entries for a CPT Procedure based on procedure date.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the following values separated by up-arrows:

> 1\. ECCPT — CPT Code IEN (file \#81)

> 2\. ECDT — Procedure date and time (FileMan format)

RETURN PARAMETER DESCRIPTION: Returns an array of CPT procedure modifiers as follows:

> 1\. 2-character Modifier

> 2\. Modifier Name

> 3\. Modifier IEN (#81.3)

36. <span id="GETPXREASON" class="anchor"></span>EC GETPXREASON — Get the procedure Reasons linked to an Event Code Screen.

TAG: ECPXRS

ROUTINE: ECUMRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: Return array entries with Procedure reasons linked to an Event Code screen.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The Event Code screen IEN from file \#720.3.

RETURN PARAMETER DESCRIPTION: Returns an array with data containing

> 1\. Procedure Reason

> 2\. Procedure Reason IEN from file \#720.4

> 3\. Event Code Screens / Procedure Reason Link IEN from file \#720.5

37. <span id="GETSCNHELP" class="anchor"></span>EC GETSCNHELP — Get the information for the topic help from the HELP FRAME file (#9.2).

TAG: ECHELP

ROUTINE: ECUURPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: PUBLIC

DESCRIPTION: Returns the text from the HELP FRAME file (#9.2) based on a help frame.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: Input variable ECARY contains the name of the help frame.

RETURN PARAMETER DESCRIPTION: Returns an array with help text from the HELP FRAME File (#9.2).

38. <span id="GETUSRDSSUNIT" class="anchor"></span>EC GETUSRDSSUNIT — Get the DSS Units for which the user has access.

TAG: USRUNT

ROUTINE: ECUERPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns an array of DSS units for which the user has access.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input variable ECARY contain the following '^' delimited values.

> 1\. ECL — Location IEN from INSTITUTION file (#4); if defined, gives User's DSS units for a location

> 2\. ECDUZ — IEN from NEW PERSON file (#200); if defined, gives list of DSS Units available to user

> 3\. ECSUMUSR — Set if getting DSS units for the 'Print Category and Procedure Summary Report' (optional)

> 4\. ECDUST — DSS Unit Status (Active/Inactive/Both) if getting units for the 'Print Category and Procedure Summary Report' (optional)

RETURN PARAMETER DESCRIPTION: Returns an array of DSS Units. Data pieces separated by an up-arrow as follows:

> 1\. IEN of DSS UNIT file (#724)

> 2\. Name of DSS Unit

> 3\. Send to PCE Flag

> 4\. Data entry date/time default

39. <span id="GETVERSION" class="anchor"></span>EC GETVERSION — Get the version number of the Event Capture software that is present on the server.

TAG: VERSRV

ROUTINE: ECUURPC

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns the server version of a particular option.  This is used by ECS GUI to determine the current server version of the software.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: ECARY contains the option name and client version of the software.

RETURN PARAMETER DESCRIPTION: Returns the server version of the software.

40. <span id="GETVISITINFO" class="anchor"></span>EC GETVISITINFO — Get patient information related to a visit.

TAG: VISINFO

ROUTINE: ECUERPC2

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: This broker call returns specific EC patient visit data (location, DSS Unit, patient IEN, etc.) based on a Visit Number.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The value ECARY contains the Visit Number IEN (ECVSN) from the VISIT file (#9000010).

RETURN PARAMETER DESCRIPTION: This call returns the following EC patient values separated by an up-arrow (^):

> 1\. Location IEN

> 2\. Location Name

> 3\. DSS Unit IEN

> 4\. DSS Unit Name

> 5\. Send to PCE value

> 6\. Procedure Date/Time FileMan format

> 7\. Procedure Date/Time human readable format

> 8\. Patient DFN

> or (if error):

> 1\. 0

> 2\. Error Message

41. <span id="ICD10IMPLEMENTATIONDATE" class="anchor"></span>EC ICD10IMPLEMENTATIONDATE — Get the date the ICD-10 code set was implemented for Event Capture.

TAG: ICD10

ROUTINE: ECVICDDT

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: The EC ICD10IMPLEMENTATIONDATE RPC returns the Implementation Date of ICD-10 Code Set in MM/DD/YYYY format OR  -1^Error Message.

42. <span id="RECENT_VISITS" class="anchor"></span>EC RECENT VISITS — Get the recent visits for a selected patient.

TAG: RCNTVST

ROUTINE: ECUTL1

RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns the 60 most recent visits/appointments for a selected patient for the selected location.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: ECARY will be sent with two delimited pieces of information.

> DFN — patient's IEN

> LOC — (optional) IEN of the location to filter visits/appts

RETURN PARAMETER DESCRIPTION: Return parameter is an array containing:

> Piece 1 — Date of visit, internal FileMan date

> Piece 2 — Date of Visit (readable) and  Clinic Name

> Piece 3 — Date of Visit (readable)

> Piece 4 — Clinic Name

43. <span id="REPORTS" class="anchor"></span>EC REPORTS — The RPC Broker entry point for EC reports. The input parameter indicates where the output is to be sent - a printer, a device, a queue, or an export file. Some screens (e.g. the Event Code Screens Table) use this RPC to populate the rows of a table.

TAG: RPTEN

ROUTINE: ECRRPC

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: This call is used by all Event Capture GUI reports.  Produces report based on option selected from the Delphi application.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LIST

DESCRIPTION: The input array ECARY will be defined based on the report to be generated. The report handle or type must be defined.  It is also necessary to specify whether the report will be printed to a device or displayed. The following is an example of the variables defined for 'Patient Summary Report':

> ECARY("ECDFN")=170

> ECARY("ECED")=3010430

> ECARY("ECHNDL")="ECPAT"

> ECARY("ECPTYP")="D"

> ECARY("ECRY")=Y

> ECARY("ECSD")=3010401

RETURN PARAMETER DESCRIPTION: Returns the report, or the task number if queued.

44. <span id="SPACEBAR" class="anchor"></span>EC SPACEBAR — Returns the equivalent to the "Spacebar / Return" feature in VistA, retrieving the last record accessed for the specified file.

TAG: ECDEF

ROUTINE: ECUERPC1

RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED

DESCRIPTION: This RPC would return the value equivalent to when the 'Spacebar and Return' keys are entering in the VISTA package.

INPUT PARAMETER: ECARY

PARAMETER TYPE: LITERAL

DESCRIPTION: The input variable ECARY contains the value of the file to obtain the VISTA equivalent of 'spacebar return'.

RETURN PARAMETER DESCRIPTION: The RESULTS variable contains the IEN and the .01 field description.

45. <span id="VALIDATE" class="anchor"></span>EC VALIDATE SPREADSHEET DATA — Perform validation checks for all fields represented by a row in the spreadsheet.

TAG: IN

ROUTINE: ECV1RPC

RETURN VALUE TYPE: ARRAY

AVAILABILITY: PUBLIC

DESCRIPTION: This RPC validates EC spreadsheet data and returns an array containing error messages

INPUT PARAMETER: ECDATA

PARAMETER TYPE: LITERAL

DESCRIPTION: This is a row of data in the spreadsheet

RETURN PARAMETER DESCRIPTION: This is a list of error codes and messages

46. <span id="ORWU_DEVICE" class="anchor"></span>ORWU DEVICE — Get a list of print devices which are registered in VistA.

TAG: DEVICE

ROUTINE: ORWU

RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

APP PROXY ALLOWED: Yes

DESCRIPTION: Returns a list of print devices.

47. <span id="ORWU_HASKEY" class="anchor"></span>ORWU HASKEY — Determine whether the user has a specified security key.

TAG: HASKEY

ROUTINE: ORWU

RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Returns 1 if a user holds a security key, otherwise 0.

48. <span id="ORWU_NEWPERS" class="anchor"></span>ORWU NEWPERS — Get a group of records from the NEW PERSON file (#200) for use in populating a list box.

TAG: NEWPERS

ROUTINE: ORWU

RETURN VALUE TYPE: ARRAY

APP PROXY ALLOWED: Yes

DESCRIPTION: Returns a set of NEW PERSON file (#200) entries for use in a long list box.

49. <span id="ORWU_USERINFO" class="anchor"></span>ORWU USERINFO — Get relevant information for the current user.

TAG: USERINFO

ROUTINE: ORWU

RETURN VALUE TYPE: SINGLE VALUE

APP PROXY ALLOWED: Yes

DESCRIPTION: Returns preferences for the current user.

50. <span id="SC_PATIENT_LOOKUP" class="anchor"></span>SC PATIENT LOOKUP — Get records from the PATIENT file (#2) matching the search criteria.

TAG: FINDP

ROUTINE: SCUTBK11

RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Patient lookup.

This is intended as a temporary RPC until a VA or FileMan component is available. Does a Multiple index lookup on the PATIENT file (#2).  This does not invoke DPTLK.  Given lookup value, this returns a list of the form DFN^patient name^DOB^PID.

Only the first 500 records that match the value are returned.

INPUT PARAMETER: LIST ATTRIBUTES

PARAMETER TYPE: LIST

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Event Capture options are designed to stand alone. Each option can be independently invoked.

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section identifies security measures that must be in place for normal operation of the ECS application. Event Capture security is maintained through the use of security keys, file protection, and option assignment in addition to standard VistA logon security.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps from the VistA Systems Manager Menu to obtain information about the security keys contained in the Event Capture software:

1.  VA FileMan
14. Print File Entries
15. OUTPUT FROM WHAT FILE: PRINT TEMPLATE// Security Key
16. SORT BY: NAME// \<Enter\>
17. START WITH NAME: FIRST// EC
18. GO TO NAME: LAST// ECX
19. WITHIN NAME, SORT BY: \<Enter\>
20. FIRST PRINT FIELD: Name
21. THEN PRINT FIELD: Description
22. THEN PRINT FIELD: \<Enter\>
23. Heading (S/C): SECURITY KEY LIST// \<Enter\>
24. START AT PAGE: 1// \<Enter\>
25. DEVICE: \<Enter\> HOME (CRT) Right Margin: 80// \<Enter\>

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 5 lists the recommended VA FileMan Access Codes for the ECS GUI Software.

| File Number | File Name                          | Data Dictionary (DD) Access | Read (RD) Access | Write (WR) Access | Delete (DEL) Access | Learn-As-You-Go (LAYGO) Access |
|-----------------|----------------------------------------|---------------------------------|----------------------|-----------------------|-------------------------|------------------------------------|
| 720.1           | EVENT CAPTURE LOG                      | @                               |                      |                       |                         |                                    |
| 720.3           | EC EVENT CODE SCREENS                  | @                               |                      |                       |                         |                                    |
| 720.4           | EC PROCEDURE REASON                    | @                               | @                    | @                     | @                       | @                                  |
| 720.5           | EC EVENT CODE SCREENS/PROC REASON LINK | @                               | @                    | @                     | @                       | @                                  |
| 721             | EVENT CAPTURE PATIENT                  | @                               |                      |                       |                         |                                    |
| 722             | EVENT CAPTURE PROVIDER                 |                                 |                      |                       |                         |                                    |
| 723             | MEDICAL SPECIALTY                      | @                               |                      |                       |                         |                                    |
| 724             | DSS UNIT                               | @                               |                      |                       |                         |                                    |
| 725             | EC NATIONAL PROCEDURE                  | @                               |                      |                       |                         |                                    |
| 726             | EVENT CAPTURE CATEGORY                 | @                               |                      |                       |                         |                                    |

Entries in the MEDICAL SPECIALTY file (#723) are set by the MCAO or its designee. Any additions, deletions, or modifications will be distributed nationally through the release of the Event Capture software.

Entries in the EC NATIONAL PROCEDURE file (#725) are also set by the MCAO or its designee. The Event Capture Management Menu provides the option to add locally recognized procedures to this file. Each entry in a file is assigned an Internal Entry Number (IEN) or record number. When the site adds a local entry, the software forces the IEN to be 90000 or higher.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture software does not provide for the archiving or purging of its data.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should have a backup emergency plan in place in the event the system goes down. Technical users of the ECS software should ensure that a local contingency plan is used in the event of application problems in a live environment. The plan should identify the procedure(s) for maintaining the functionality in the event of a system outage. Field Station ISOs can get assistance from the Regional ISO.

General Troubleshooting Tips:

- Throughout the ECS GUI application, click the question mark button (located on the toolbar or at the bottom right corner of the screen) to obtain online information for any screen.
- To obtain online information for a field, select that field and press \<F1\>.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out of the software should only be performed in response to severe system impairment and there is no other option available. Specific back-out guidance is provided in the EC\*2.0\*169 DIBR, which can be found on the [VA Software Documentation Library](https://www.va.gov/vdl/search.asp?group=application&terms=ECS) (VDL).

Please use the VA YourIT service portal to enter a ticket for additional assistance.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enterprise Service Desk (ESD) Provides critical IT support to Veterans Affairs. Contact information can be found online at the VA YourIT service portal.

#### Acronyms

Table 6 lists the acronyms used throughout the ECS Technical Manual and their appropriate descriptions.
| Acronym | Description                                                     |
|---------|-----------------------------------------------------------------|
| API     | Application Programming Interface                               |
| CPRS    | Computerized Patient Record System                              |
| CPT     | Current Procedural Terminology                                  |
| DD      | Data Dictionary                                                 |
| DRG     | Diagnosis Related Group                                         |
| DSS     | Decision Support System                                         |
| EC      | Event Code                                                      |
| ECS     | Event Capture System                                            |
| ESD     | Enterprise Service Desk                                         |
| GUI     | Graphical User Interface                                        |
| HCPCS   | Healthcare Common Procedure Coding System                       |
| IEN     | Internal Entry Number                                           |
| ICR     | Integration Control Registrations                               |
| ISO     | Information Security Officer                                    |
| LAYGO   | Learn-As-You-Go                                                 |
| MCAO    | Managerial Cost Accounting Office                               |
| MUMPS   | Massachusetts General Hospital Utility Multi-Programming System |
| OIT     | Office of Information and Technology                            |
| PCE     | Patient Care Encounter                                          |
| PIMS    | Patient Information Management Service                          |
| RD      | Read Access                                                     |
| RPC     | Remote Procedure Call                                           |
| UCI     | User Class Identifier                                           |
| VA      | Department of Veterans Affairs                                  |
| VAMC    | Veterans Affairs Medical Center                                 |
| VDL     | VA Software Documentation Library                               |
| VHA     | Veterans Health Administration                                  |
| VistA   | Veterans Health Information Systems and Technology Architecture |
| WR      | Write Access                                                    |
This appendix provides a list of the acronyms used in this document and their appropriate descriptions

#### Glossary

Table 7 lists terms used throughout the ECS Technical Manual.
| Term                        | Definition                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Category                    | Provides a common level to group associated procedures. Multiple procedures can be defined for each category.                                                                                                                                                                                                                                                                                                   |
| Cost Center                 | Reveals which service is using the specified DSS Unit. Cost centers are defined in the Fiscal Service cost manuals.                                                                                                                                                                                                                                                                                             |
| DSS Unit                    | Defines the lowest level segment used for tracking hospital resources. These units can be a small work unit within a service, or a large division within a service. Management at each facility is responsible for tailoring the DSS Units to fit its resource/cost reporting needs.                                                                                                                            |
| DSS Unit Number             | Four- to seven-character Department Cost Manager (DCM) department code. MCAO will be providing guidance to VAMCs regarding what they should enter.                                                                                                                                                                                                                                                              |
| Event Capture               | Software designed to provide management tools necessary to track procedures not tracked by other VistA software.                                                                                                                                                                                                                                                                                                |
| Event Code Screen           | Unique combination of location, DSS Unit, category and procedure that defines patient procedures.                                                                                                                                                                                                                                                                                                               |
| FileMan                     | This system implements the VistA database engine and is the basis for several patient safety controls, as well as fiscal integrity controls. It implements security, confidentiality, and privacy controls, and is a critical component in meeting the requirements of Enterprise Architecture.                                                                                                                 |
| Kernel                      | This system implements security, confidentiality, and privacy controls for VistA, including user authentication algorithms. It provides many tools for the safe construction of local software, and it implements many national control files, to include, but not limited to, New Person, Institution, State, etc. This system is a critical component in meeting the requirements of Enterprise Architecture. |
| Location                    | Facility or division name as it appears in the INSTITUTION file (#4).                                                                                                                                                                                                                                                                                                                                           |
| Procedure                   | A specific function performed on, or service provided to, a patient.                                                                                                                                                                                                                                                                                                                                            |
| Provider                    | The person performing the procedure.                                                                                                                                                                                                                                                                                                                                                                            |
| Remote Procedure Call (RPC) | This system supports client and/or server messaging used by CPRS, Bar Code Medication Administration (BCMA), and others, to access the MUMPS database through APIs. It provides a development kit for local development, and it implements security, confidentiality, and privacy controls. This system is a critical component in meeting the requirements of Enterprise Architecture.                         |
Glossary
