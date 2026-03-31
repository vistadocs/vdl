---
title: XU*8*512 Trainee Registration Core Dataset
doc_type: SUP
doc_label: Supplement
doc_layer: patch
doc_subject: Trainee Registration Core Dataset
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*512
group_key: "XU:XU:8"
file_numbers: 
  - 200
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - trainee
  - class
  - strong
  - table
  - clinical
  - registered
  - registration
  - contents
  - report
  - reports
page_count: 0
word_count: 24481
section_count: 43
table_count: 74
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu8_0p512sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu8_0p512sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

![](xu-8-512-trainee-registration-core-dataset/001.png)

TRAINEE REGISTRATION CORE DATASET (FORMERLY CLINICAL TRAINEE CORE DATASET)

Supplement to Patch Description

Kernel Patch XU\*8.0\*251

June 2003

Revised: Kernel Patch XU\*8.0\*512 & 540

January 2010

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Common Services (CS)

<span id="_Toc209429662" class="anchor"></span>Revision History

Documentation History

The following table displays the revision history for this document. Revisions to the documentation are based on continuous dialog with Infrastructure and Security Services (ISS) Technical Writers and evolving industry standards and styles.

Table i. Documentation History

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 53%" />
<col style="width: 30%" />
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
<td>November 2008</td>
<td><p>Updates:</p>
<ul>
<li><p>Changed mail group references from "REDACTED" to "REDACTED" as per Kernel Patch XU*8.0*540.</p></li>
<li><p>Made minor updates for formatting and organizational references.</p></li>
</ul></td>
<td><p>Oakland Office of Information Field Office (OIFO):</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>October 2005</td>
<td><p>Trainee Registration Core Dataset software is updated with Kernel Patch XU*8.0*398. A simple edit was made to screen prompts. The before and after is shown as follows:</p>
<ul>
<li><p>Before: "Is this person a Registered Trainee?"</p></li>
<li><p>After: "Is this person an active Trainee?"</p></li>
</ul></td>
<td><p>Oakland OIFO and Office of Academic Affiliations:</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>August 2005</td>
<td>Trainee Registration Core Dataset (formerly Clinical Trainee Core Dataset) software is updated with Kernel Patch XU*8.0*344 in support of VHA Directive 2003-032, Clinical Trainee Registration.</td>
<td><p>Oakland OIFO and Office of Academic Affiliations:</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>January 2005</td>
<td><p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects</p>
<ul>
<li><p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards. Conventions for displaying TEST data is documented in the Orientation section of this manual.</p></li>
<li><p><strong>PDF 508 Compliance</strong>—The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></li>
</ul></td>
<td><p>Oakland OIFO:</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>June 2003</td>
<td><p>Clinical Trainee Core Dataset documentation, Kernel Patch XU*8.0*251.</p>
<p>Kernel Patch XU*8.0*251 has been created in support of VHA Directive 2003-032, Clinical Trainee Registration.</p></td>
<td><p>Oakland OIFO and Office of Academic Affiliations:</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
</tbody>
</table>

Patch History

For the current patch history related to this software, please refer to the Patch Module on FORUM.

Contents

<span id="_Toc475930734" class="anchor"></span>Figures and Tables

Figures

[Figure 3‑1. Kernel options affected, updated, and created to support Trainee Registration Cord  
Dataset [3-2](#_Ref107302933)](#_Ref107302933)

Tables

<span id="_Toc318186177" class="anchor"></span>

Orientation

How to Use this Manual

This is the supplemental documentation for the VistA Trainee Registration Core Dataset (formerly known as Clinical Trainee Core Dataset) software. It is organized into the following major parts:

1.  Introduction
2.  VistA New Person File―Academic Affiliations Needs
3.  Editing and Displaying VHA Registered Trainee Data
4.  HL7 Interface Specifications
5.  Implementation and Maintenance)

Legal Requirements

There are no special legal requirements involved in the use of Deployment Toolkit (DTK).

Disclaimers

This manual provides an overall explanation of how the Trainee Registration Core Dataset; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Websites on the Internet and VA Intranet for a general orientation to Health*<u>e</u>*Vet. For example, go to the Office of Information & Technology (OI&T) VistA Development VA Intranet Website:

http://vista.med.va.gov

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/002.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA. |

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout this documentation to alert readers to special information. The following table gives a description of each of these symbols:

Table ii. Documentation symbol description

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                         | Description                                                                                                        |
| ![](xu-8-512-trainee-registration-core-dataset/003.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material |
| ![](xu-8-512-trainee-registration-core-dataset/004.png)                                                              | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information               |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/005.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document, located on the Web site listed below, and where "N" represents the first name as a number spelled out and incremented with each new entry.

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/006.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/007.png) | REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Kernel—VistA M Server software (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft® Windows
- M programming language

Reference Material

Readers who wish to learn more about the Trainee Registration Core Dataset software should consult the following:

- Trainee Registration Core Dataset, Supplement to Patch Description
- Installation instructions for this software can be found in the patch description for Kernel Patch XU\*8.0\*512, located in the National Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM.

VistA documentation is made available online in Microsoft Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe® Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe® Systems Incorporated at the following Website:

<http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website:

<http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method REDACTED

|                                                                                                                |                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/008.png) | NOTE: This method transmits the files from the first available FTP server. |

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
  - [Purpose](#purpose)
  - [System Requirements](#system-requirements)
- [VistA New Person File―Academic Affiliations Needs](#vista-new-person-fileacademic-affiliations-needs)
- [Editing and Displaying VHA Registered Trainee Data](#editing-and-displaying-vha-registered-trainee-data)
  - [Kernel Input Options Affected](#kernel-input-options-affected)
  - [How Does an Option's ScreenMan Form Differ from its Corresponding Input Template?](#how-does-an-options-screenman-form-differ-from-its-corresponding-input-template)
  - [Trainee Registration Menu Options](#trainee-registration-menu-options)
  - [Editing Registered Trainee Data for New Person File Entries](#editing-registered-trainee-data-for-new-person-file-entries)
  - [Assign Registered Trainee Options to User(s)](#assign-registered-trainee-options-to-users)
  - [Using the Edit Trainee Registration Data Option](#using-the-edit-trainee-registration-data-option)
  - [Using the Trainee Registration Inquiry Option](#using-the-trainee-registration-inquiry-option)
  - [Kernel User Inquiry Option](#kernel-user-inquiry-option)
  - [Using the Trainee Reports Menu Option](#using-the-trainee-reports-menu-option)
    - [Local Trainee Registration Reports](#local-trainee-registration-reports)
    - [Trainee Transmission Reports to OAA](#trainee-transmission-reports-to-oaa)
  - [Sort Criteria for Customizing Reports](#sort-criteria-for-customizing-reports)
- [HL7 Interface Specifications](#hl7-interface-specifications)
  - [Assumptions](#assumptions)
  - [Sending System and Receiving System](#sending-system-and-receiving-system)
  - [Data Capture and Transmission](#data-capture-and-transmission)
  - [Batch Messages](#batch-messages)
  - [Batch Acknowledgments](#batch-acknowledgments)
  - [HL7 Message Profile for PMU-B02](#hl7-message-profile-for-pmu-b02)
  - [HL7 Control Segments](#hl7-control-segments)
  - [Message Definitions](#message-definitions)
  - [Message Control Segments](#message-control-segments)
    - [Segment Table Definitions](#segment-table-definitions)
    - [BHS—Batch Header Segment (Required, not Repeatable)](#bhsbatch-header-segment-required-not-repeatable)
    - [BTS—Batch Trailer Segment (Required, not Repeatable)](#btsbatch-trailer-segment-required-not-repeatable)
    - [MSH—Message Header Segment (Required, not Repeatable)](#mshmessage-header-segment-required-not-repeatable)
    - [EVN—Event Type Segment (Required, not Repeatable)](#evnevent-type-segment-required-not-repeatable)
    - [STF—Staff Identification (Required, not Repeatable)](#stfstaff-identification-required-not-repeatable)
    - [PRA—Practitioner Detail (Required, Repeatable)](#prapractitioner-detail-required-repeatable)
    - [ORG—Practitioner Organization Unit (Required, Repeatable)](#orgpractitioner-organization-unit-required-repeatable)
    - [EDU—Educational Detail (Required, Repeatable)](#edueducational-detail-required-repeatable)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Software Dependencies](#software-dependencies)
  - [Background Jobs](#background-jobs)
  - [Routines](#routines)
  - [File List](#file-list)
    - ["ATR" New-Style Cross-reference](#atr-new-style-cross-reference)
  - [ScreenMan Forms and Templates](#screenman-forms-and-templates)
  - [Options](#options)
    - [New Kernel Options](#new-kernel-options)
    - [Modified Kernel Options](#modified-kernel-options)
    - [Existing Kernel Options Affected](#existing-kernel-options-affected)
    - [Menu Diagram—OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\]](#menu-diagramoaa-trainee-registration-menu-xu-clinical-trainee-menu)
  - [Archiving and Purging](#archiving-and-purging)
  - [Callable Routines](#callable-routines)
  - [External Interfaces (HL7 Components)](#external-interfaces-hl7-components)
  - [Scheduled Option](#scheduled-option)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [HL7 Protocols](#hl7-protocols)
  - [HL7 Logical Link](#hl7-logical-link)
  - [Mail Group: XUOAA CLIN TRAINEE](#mail-group-xuoaa-clin-trainee)
  - [External Relations](#external-relations)
    - [Software Requirements](#software-requirements)
  - [Internal Relations](#internal-relations)
  - [Namespace](#namespace)
  - [File Numbers](#file-numbers)
  - [Software-wide Variables](#software-wide-variables)
  - [Software Security](#software-security)
    - [Mail Groups](#mail-groups)
    - [Remote Systems](#remote-systems)
    - [Archiving and Purging](#archiving-and-purging-1)
    - [Interfaces](#interfaces)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
This supplemental documentation is intended for use in conjunction with the Veterans Health Information System and Technology Architecture (VistA) Trainee Registration Core Dataset (formerly known as Clinical Trainee Core Dataset) software. It outlines the details of the work involved in this patch for VA facilities.
The original version of this software was developed as Clinical Trainee Core Dataset and was released in Kernel Patch XU\*8.0\*251 in support of VHA Directive 2003-032, Clinical Trainee Registration, to assist the VHA Office of Academic Affiliations (OAA) in capturing core data for VHA clinical trainees that use the VistA system. To achieve this:
- A new PROGRAM OF STUDY file (#8932.2) was created.
- New fields and a cross-reference have been added to the NEW PERSON file (#200).
- Existing ScreenMan forms and input and print templates that are used to edit the data in the NEW PERSON file (#200) were modified to include the new fields.
- A new menu, edit option and form, and inquiry option were provided for entering and viewing clinical trainee data.
|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/009.png) | NOTE: The VistA NEW PERSON file (#200) is exported with Kernel. It resides at each VA facility. Each person/user who has access to the local VistA computer system is entered into this file. It contains specific data on all employees, users, practitioners, and providers who access the local VistA system, and in relation to registered trainees, the "core trainee dataset." The data elements within this file describe the users' characteristics and attributes. Many of them are specifically oriented to the health care field. |
The Trainee Registration Core Dataset entails the following changes:
- The following menu and associated options has been modified, both menu text and ScreenMan form:
- OAA Trainee Registration Menu ... \[XU-CLINICAL TRAINEE MENU\] (menu text formerly named OAA Clinical Trainee)
- Trainee Registration Inquiry \[XU-CLINICAL TRAINEE INQUIRY\] (menu text formerly named Inquiry Clinical Trainee)
- The following new menu and associated options, including new print and sort templates have been added:
- Trainee Reports Menu ... \[XU-CLINICAL TRAINEE REPORTS\]
- Local Trainee Registration Reports ... \[XU-CLINICAL LOCAL REPORTS\]
- List of Active Registered Trainees \[XU-CLINICAL ACTIVE TRAINEE\]
- List of All Registered Trainees \[XU-CLINICAL TRAINEE LIST\]
- List of Inactive Registered Trainees \[XU-CLINICAL INACTIVE TRAINEE\]
- Total Count of Registered Trainees \[XU-CLINICAL TRAINEE DB COUNT\]
- Trainee Transmission Reports to OAA ... \[XU-CLINICAL TRANS REPORTS\]
- Trainee Transmission Report by Date \[XU-CLINICAL TRAINEE TRANSA\]
- Trainee Transmission Report by Range \[XU-CLINICAL TRAINEE TRANSC\]
- Trainee Transmission Report Selectable Items \[XU-CLINICAL TRAINEE TRANSB\]
This supplement provides instructions on how to use this software to populate the NEW PERSON file (#200) with information across all Veterans Health Administration (VHA) facilities. Information such as:
- name
- address
- social security number (SSN)
- discipline of study
- current degree level
- program of study
- VHA training facility
- date HL7 trainee record was built and sent to OAA
- registered trainee verification
- date when registered trainee is no longer designated as such
- start of training
- last year a trainee anticipates being in a training program at the associated VA facility
This supplement also provides documentation on the updates to the HL7 interface, originally implemented with Kernel Patch XU\*8.0\*251 to identify the VistA information that will be shared with the National Trainee Registration Database as part of the Trainee Registration Core Dataset software.
The intended audience for this documentation is Information Resource Management (IRM) and Veterans Affairs Medical Center (VAMC) personnel responsible for the implementation and maintenance of the VistA NEW PERSON file (#200).

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to standardized core data on VHA trainees using VistA is not collected in any systematic way that is electronically retrievable across the VHA's health care system. Basic information on VA trainees, being residents and other health professions students, is needed for the purposes of security, liability and public health issues, recruitment, and various national reports on VHAs academic mission. For clinical trainees who will need access to the patient record as part of their clinical experience, collecting trainee information via VistA is necessary.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA needs to be modified to capture basic information on all Health Professions Trainees who receive some or all of their training at a VA facility so that data may be extracted and rolled up at the national level.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is a Kernel Installation and Distribution System (KIDS) release. Installation Instructions can be found in the description for Kernel Patch XU\*8.0\*512, located on the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM.

This software requires that both Test and Production accounts exist in a standard VistA operating environment in order to function correctly.

In addition to a standard VistA operating environment, the following patches must be installed before running this patch:

<span id="_Toc214422788" class="anchor"></span>Table ‑. Patches required prior to installation of Trainee Registration Core Dataset

| VistA Software and Version | Associated Patch Designation(s) | Brief Patch Description           |
|----------------------------|---------------------------------|-----------------------------------|
| Kernel 8.0                 | XU\*8.0\*398                    | Clinical Core Registration Screen |

# VistA New Person File―Academic Affiliations Needs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the User Manual section of this supplemental documentation for the Trainee Registration Core Dataset (formerly known as Clinical Trainee Core Dataset) software. This section provides instructions on how to use this software to populate the VistA NEW PERSON file (#200) with resident and trainee information for the purposes of security, liability and public health issues, recruitment, and various national reports on VHAs academic mission.

The VistA NEW PERSON file (#200) is exported with Kernel, and resides at each local VA medical facility. Each person/user who has access to the local VistA computer system is entered into this file. It contains specific data on all employees, users, practitioners, and providers who access the local VistA system. The data elements within this file describe the users' characteristics and attributes. Many of them are specifically oriented to the health care field.

The NEW PERSON file (#200) is being adapted to meet the needs of the Office of Academic Affiliations (OAA) for reporting information on individuals from affiliated institutions who are receiving training at a VA Medical Facility (VHA registered trainees) such as medical residents, nursing students, and other trainees who directly or indirectly may provide care to patients. The Trainee Registration Core Dataset software has added the following new fields to the NEW PERSON file (#200):

- CURRENT DEGREE LEVEL (#12.1), added with Kernel Patch XU\*8.0\*251
- PROGRAM OF STUDY (#12.2) added with Kernel Patch XU\*8.0\*251
- LAST TRAINING MONTH & YEAR (#12.3) updated with Kernel Patch XU\*8.0\*344
- VHA TRAINING FACILITY (#12.4) added with Kernel Patch XU\*8.0\*344
- DATE HL7 TRAINEE RECORD BUILT (#12.5) added with Kernel Patch XU\*8.0\*344
- CLINICAL CORE TRAINEE (#12.6) added with Kernel Patch XU\*8.0\*344
- DATE NO LONGER TRAINEE (#12.7) added with Kernel Patch XU\*8.0\*344
- START OF TRAINING (#12.8) added with Kernel Patch XU\*8.0\*344

In addition, the "ATR" cross-reference monitors the following fields in the NEW PERSON file (#200):

- 
- NAME (#.01)
- STREET ADDRESS 1 (#.111)
- STREET ADDRESS 2 (#.112)
- STREET ADDRESS 3 (#.113)
- CITY (#.114)
- STATE (#.115)
- ZIP CODE (#.116)
- SSN (#9)
- EMAIL ADDRESS (#.151)
- CURRENT DEGREE LEVEL (#12.1)
- PROGRAM OF STUDY (#12.2)
- LAST TRAINING MONTH & YEAR (#12.3)
- SERVICE/SECTION (#29)
- TITLE (#8)
- DOB (#5)
- VHA TRAINING FACILITY (#12.4)
- CLINICAL CORE TRAINEE (#12.6)
- DATE NO LONGER TRAINEE (#12.7)
- START OF TRAINING (#12.8)

When data for any of the above fields is modified for a person that is designated a registered trainee, a new cross-reference defined on the NEW PERSON file (#200) sets an index (a global node) that stores the IEN of the record last modified and the date that it was modified. A separate queuable option runs daily, looping through the "ATR" index and via HL7 messages, which sends the registered trainee data to the OAA for each record modified.

|                                                                                                                |                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/010.png) | REF: For more information on tracking changes to registered trainee records, see the "ATR" New-Style Cross-reference" topic in this manual. |

# Editing and Displaying VHA Registered Trainee Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information about the Kernel options both affected by and created to support the Trainee Registration Core Dataset software. It does not attempt to provide detailed information about how to use these Kernel options. This is documented in detail in the "Sign-On/Security" section of the *Kernel Systems Management Guide* located at the following Website:

<http://www.va.gov/vdl/application.asp?appid=10>

## Kernel Input Options Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel options and the associated ScreenMan forms and input templates affected by the Trainee Registration Core Dataset are shown in Table 3‑1. The Kernel options themselves, have not been changed; however, the ScreenMan forms and the input templates used by these options have been modified to give users the ability to edit registered trainee data.

<span id="_Ref22706351" class="anchor"></span>Table ‑. Affected Kernel input options with associated ScreenMan forms and input templates

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 33%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>ScreenMan Form</th>
<th>Input Template</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XUSERNEW</p>
<p>Add a New User to the System</p></td>
<td>XUNEW USER</td>
<td>XUNEW USER</td>
</tr>
<tr class="even">
<td><p>XUSEREDIT</p>
<p>Edit an Existing User</p></td>
<td>XUEXISTING USER</td>
<td>XUEXISTING USER</td>
</tr>
<tr class="odd">
<td><p>XUSERREACT</p>
<p>Reactivate a User</p></td>
<td>XUREACT USER</td>
<td>XUREACT USER</td>
</tr>
</tbody>
</table>

## How Does an Option's ScreenMan Form Differ from its Corresponding Input Template?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionally there is no difference between the ScreenMan forms and input templates invoked by these options. All three options attempt to invoke the associated ScreenMan form first. However, if for some reason the ScreenMan form cannot be invoked (e.g., because the terminal type cannot handle screen-oriented applications), the associated input template for scrolling mode is invoked.

## Trainee Registration Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3‑1 shows the four existing Kernel options affected by and the new OAA Trainee Registration Kernel options for editing and reporting on registered trainees exported with this software. These options are located on their own menu entitled OAA Trainee Registration Menu located on the Kernel User Management menu.

This software also exports a new menu named Trainee Reports Menu \[XU-CLINICAL TRAINEE REPORTS\] and associated options for local VA medical facility report generation. This new menu has been added to the OAA Registered Trainee menu, Figure 3‑1, which is described in more detail in the section "Assign Registered Trainee Options to User(s)" on the following pages.

<span id="_Ref107302933" class="anchor"></span>Figure ‑. Kernel options affected, updated, and created to support Trainee Registration Cord Dataset

Select Systems Manager Menu Option: User Management

Add a New User to the System \[XUSERNEW\]

Edit an Existing User \[XUSEREDIT\]

Reactivate a User \[XUSERREACT\]

User Inquiry \[XUSERINQ\]

.

.

.

OAA OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\]

E Edit Trainee Registration Data \[XU-CLINICAL TRAINEE EDIT\]

I Trainee Registration Inquiry \[XU-CLINICAL TRAINEE INQUIRY\]

R Trainee Reports Menu ... \[XU-CLINICAL TRAINEE REPORTS\]

Local Trainee Registration Reports \[XU-CLINICAL LOCAL REPORTS\]

List of Active Registered Trainees \[XU-CLINICAL ACTIVE TRAINEE\]

List of All Registered Trainees \[XU-CLINICAL TRAINEE LIST\]

List of Inactive Registered Trainees \[XU-CLINICAL INACTIVE  
TRAINEE\]

Total Count of Registered Trainees \[XU-CLINICAL TRAINEE DB COUNT\]

Trainee Transmission Reports to OAA \[XU-CLINICAL TRANS REPORTS\]

Trainee Transmission Report by Date \[XU-CLINICAL TRAINEE TRANSA\]

Trainee Transmission Report by Range \[XU-CLINICAL TRAINEE TRANSC\]

Trainee Transmission Report Selectable Items \[XU-CLINICAL TRAINEE  
TRANSB\]

## Editing Registered Trainee Data for New Person File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This next example will use the screen-oriented display (i.e., the ScreenMan form) to illustrate the changes to the Kernel options. Edits are made to a fictitious user named ONE KRNUSER in the NEW PERSON file (#200). The input template functions similarly, but in scrolling mode.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/011.png) | NOTE: You may edit an existing trainee’s data via any of the Kernel User Management menu options noted above or by using the OAA Trainee Registration Menu’s Edit Trainee Registration Data option. However, you can only create a new trainee record via the Kernel Add a New User to the System menu option. |

After you select the option Edit an Existing User, Kernel prompts you to enter the person's name, as shown in Figure 3‑2.

<span id="_Ref22706484" class="anchor"></span>Figure ‑. Selecting a user in the NEW PERSON file (#200)

Select User Management Option: Edit an Existing User

Select NEW PERSON NAME: KRNUSER,ONE

The option then opens up the first page of the five-page ScreenMan form, as shown in Figure 3‑3.

<span id="_Ref107396372" class="anchor"></span>Figure ‑. Edit an Existing User ScreenMan form, Page 1

Edit an Existing User

NAME: KRNUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> KRNUSER,ONE INITIAL: OK

TITLE: DEVELOPER NICK NAME: PEPI

SSN: 666995556 DOB: MAR 9,1967

DEGREE: MS MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS: DIUSER

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: CLARKSBURG

<u>SERVICE/SECTION</u>: IRM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

The data needed on this page of the ScreenMan form by the Office of Academic Affiliations for registered trainees are TITLE and SSN. Therefore, for registered trainees make sure this data is entered.

The rest of the data needed by the Office of Academic Affiliations is on page 5 of the ScreenMan form. Press \<PageDown\> or \<PF1\>\<DownArrow\> until you reach page 5, or press \<PageUp\> or \<PF1\>\<UpArrow\> to go directly to the page, which is shown in Figure 3‑4.

<span id="_Ref21859393" class="anchor"></span>Figure ‑. Edit an Existing User ScreenMan form, Page 5

Edit an Existing User

NAME: KRNUSER, ONE Page 5 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PERMANENT ADDRESS:

Street 1: 250 Main St.

Street 2:

Street 3:

City: Anytown

State: CALIFORNIA

Zip Code: 99999

E-Mail Address: one.krnuser@med.va.gov

Is this person an active Trainee?: YES

VHA Training Fac.: SAN FRANCISCO

Start Date of Training: JAN 7,2004 Last Training Month & Year: OCT 7,2004

Trainee Inactive (Date):

Program of Study: HEALTH INFORMATION

Current Degree Lvl: MASTER'S

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

For registered trainees, all data on this page should be entered, Figure 3‑4. A YES response to the prompt "Is this person an active Trainee?:" causes the following two things to happen:

- All fields except "Trainee Inactive (Date):," to become editable, listed as follows:
- VHA TRAINING FACILITY (#12.4) added with Patch XU\*8.0\*344
- START OF TRAINING (#12.8) added with Patch XU\*8.0\*344
- LAST TRAINING MONTH & YEAR (#12.3) modified with Patch XU\*8.0\*344
- PROGRAM OF STUDY (#12.2) added with Patch XU\*8.0\*251
- CURRENT DEGREE LEVEL (#12.1) added with Patch XU\*8.0\*251
- The VHA TRAINING FACILITY (#12.4) and PROGRAM OF STUDY (#12.2) fields become required. This means that you *must* have data in this field in order to save your edits and exit the Edit an Existing User option.

## Assign Registered Trainee Options to User(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For users who need the ability to edit trainee data or run reports on registered trainees, the OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\] (the menu text of which was formerly named *OAA Clinical Trainee*) may be assigned.

The following new report options have been added to the OAA Trainee Registration Menu. The new Trainee Reports Menu \[XU-CLINICAL TRAINEE REPORTS\] offers VA facilities registered trainee information from local site databases and information on transmission reports to the OAA.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/012.png) | NOTE: The Kernel User Management menu \[XUSER\], typically used by IRM, is being transported only for purposes of attaching the new Kernel menu option OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\] during installation of this software. No ScreenMan form or input template is associated with this menu option. |

Figure 3‑5 shows a screen capture of the OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\] and options.

<span id="_Ref42070657" class="anchor"></span>Figure ‑. The OAA Trainee Registration Menu

OAA Trainee Registration Menu

E Edit Trainee Registration Data

I Trainee Registration Inquiry

R Trainee Reports Menu ...

Select OAA Trainee Registration Menu Option: r \<Enter\> Trainee Reports Menu

Local Trainee Registration Reports ...

Trainee Transmission Reports to OAA ...

Select Trainee Reports Menu Option: Local Trainee Registration Reports

List of Active Registered Trainees

List of All Registered Trainees

List of Inactive Registered Trainees

Total Count of Registered Trainees

Select Local Trainee Registration Reports Option:

Local Trainee Registration Reports ...

Trainee Transmission Reports to OAA ...

Select Trainee Reports Menu Option: Trainee Transmission Reports to OAA

Trainee Transmission Report by Date

Trainee Transmission Report by Range

Trainee Transmission Report Selectable Items

Select Trainee Transmission Reports to OAA Option:

|                                                                                                                |                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/013.png) | NOTE: The OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\] or any of its individual sub-menus can be given as a Secondary Menu Option to the specific user(s) assigned to enter and maintain the registered trainee data in the NEW PERSON file (#200). |

Table 3‑2 shows these Kernel options for creating and editing VHA trainee data in the VistA NEW PERSON file (#200).

- The Edit Trainee Registration Data option \[XU-CLINICAL TRAINEE EDIT\] allows editing of registered trainee data.
- The Trainee Registration Inquiry option \[XU-CLINICAL TRAINEE INQUIRY\] (the menu text of which was formerly named *Inquiry Clinical Trainee*) allows you to produce output displaying registered trainee data.
- The following two options are located on the Trainee Reports Menu \[XU-CLINICAL TRAINEE REPORTS\]. They offer VA facilities trainee data from local site databases and information on transmission reports to the OAA:
- Local Trainee Registration Reports
- Trainee Transmission Reports to OAA

A ScreenMan Form is associated with the Edit Trainee Registration Data option, only. A print template is associated with the inquiry option. No input templates are associated with the new report options; however, they are exported with multiple print and sort templates.

<span id="_Ref42069152" class="anchor"></span>Table ‑. Kernel Registered Trainee options and associated ScreenMan form

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>ScreenMan Form</th>
<th>Print Templates</th>
<th>Sort Templates</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XU-CLINICAL TRAINEE EDIT</p>
<p>Edit Trainee Registration Data</p></td>
<td><p>XU-CLINICAL TRAINEE</p>
<p>XU-CLINICAL TRAINEE DATE</p></td>
<td>None</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>XU-CLINICAL TRAINEE INQUIRY</p>
<p>Trainee Registration Inquiry</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE INQUIRY</td>
<td>None</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL TRAINEE REPORTS]</p>
<p>Trainee Reports Menu</p></td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL LOCAL REPORTS]</p>
<p>Local Trainee Registration Reports</p></td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL ACTIVE TRAINEE]</p>
<p>List of Active Registered Trainees</p></td>
<td>None</td>
<td>XU-CLINICAL ACTIVE TRAINEE</td>
<td>XU-CLINICAL ACTIVE TRAINEE</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE LIST]</p>
<p>List of All Registered Trainees</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE LIST</td>
<td>XU-CLINICAL TRAINEE LIST</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL INACTIVE TRAINEE]</p>
<p>List of Inactive Registered Trainees</p></td>
<td>None</td>
<td>XU-CLINICAL INACTIVE TRAINEE</td>
<td>XU-CLINICAL INACTIVE TRAINEE</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE DB COUNT]</p>
<p>Total Count of Registered Trainees</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE DB COUNT</td>
<td>XU-CLINICAL TRAINEE DB COUNT</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL TRANS REPORTS]</p>
<p>Trainee Transmission Reports to OAA</p></td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE TRANSA]</p>
<p>Trainee Transmission Report by Date</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE TRANSA</td>
<td>XU-CLINICAL TRAINEE TRANSA</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL TRAINEE TRANSC]</p>
<p>Trainee Transmission Report by Range</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE TRANSC</td>
<td>XU-CLINICAL TRAINEE TRANSC</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE TRANSB]</p>
<p>Trainee Transmission Report Selectable Items</p></td>
<td>None</td>
<td>XU-CLINICAL TRAINEE TRANSB</td>
<td>XU-CLINICAL TRAINEE TRANSB</td>
</tr>
</tbody>
</table>

## Using the Edit Trainee Registration Data Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3‑6 illustrates how to access the Edit Trainee Registration Data option from the OAA Trainee Registration Menu:

<span id="_Ref42497773" class="anchor"></span>Figure ‑. Using the Edit Trainee Registration Data option

Select User Management Option: OAA \<Enter\> OAA Trainee Registration Menu

E Edit Trainee Registration Data \[XU-CLINICAL TRAINEE EDIT\]

I Trainee Registration Inquiry \[XU-CLINICAL TRAINEE INQUIRY\]

R Trainee Reports Menu ... \[XU-CLINICAL TRAINEE REPORTS\]

Select OAA Trainee Registration Menu Option: e \<Enter\> Edit Trainee Registration Data

Select NEW PERSON NAME: KRNUSER,ONE\<Enter\>

As was previously mentioned, the Edit Trainee Registration Data option is located on the OAA Trainee Registration Menu. After selecting this option, you will want to select an entry in the NEW PERSON file (#200) at the "Select NEW PERSON NAME:" prompt, shown in Figure 3‑6. A one-page ScreenMan form is then presented, shown in Figure 3‑7:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/014.png) | NOTE: The XUSHOWSSN security key allows users who hold it authority to view Registered Trainee Social Security Numbers (SSNs) in the option Edit Trainee Registration Data (XU-CLINICAL TRAINEE EDIT). If the SSN field is defined, users who are not assigned the XUSHOWSSN security key will only see the last four digits of the Social Security Number (SSN) displayed (e.g., SSN: \*\*\*\*\*1234). If no SSN has been entered, only the following label is displayed: "SSN:". |

<span id="_Ref21859597" class="anchor"></span>Figure ‑. Edit Trainee Registration Data form

Edit Trainee Registration Data

NAME: KRNUSER,ONE SSN: 666995556 Page 1 of 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Is this person an active Trainee?: YES

VHA Training Fac.: SAN FRANCISCO

Start Date of Training: JAN 7,2004 Last Training Month & Year: OCT 2007

Trainee Inactive (Date):

Program of Study: HEALTH INFORMATION

Target Degree Lvl: MASTER'S

Degree: MS Title: DEVELOPER

Service/Section: IRM Date of Birth: MAR 9,1967

Permanent Street 1: 250 Main St.

Permanent Street 2:

Permanent Street 3:

City: Anytown

State: CALIFORNIA Zip Code: 99999

E-Mail Address: one.krnuser@med.va.gov

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

All the data on this form should be filled in for registered trainees, Figure 3‑7 shows that the user has answered YES to this question. A YES response causes the following two things to happen:

- All fields except "Trainee Inactive (Date):," become editable, listed as follows:
- VHA TRAINING FACILITY (#12.4) added with Patch XU\*8.0\*344
- START OF TRAINING (#12.8) added with Patch XU\*8.0\*344
- LAST TRAINING MONTH & YEAR (#12.3) modified with Patch XU\*8.0\*344
- PROGRAM OF STUDY (#12.2) added with Patch XU\*8.0\*251
- CURRENT DEGREE LEVEL (#12.1) added with Patch XU\*8.0\*251
- DEGREE (Field \#10.6)
- TITLE (Field \#8)
- SERVICE/SECTION (Field \#29)
- DOB (Field \#5)
- STREET ADDRESS 1 (Field \#.111)
- STREET ADDRESS 2 (Field \#.112)
- STREET ADDRESS 3 (Field \#.113)
- CITY (Field \#.114)
- STATE (Field \#.115)
- ZIP CODE (Field \#.116)
- E-Mail Address: (field \#.151)
- The VHA TRAINING FACILITY (#12.4) and PROGRAM OF STUDY (#12.2) fields become required. This means that you *must* edit this field in order to save your edits and exit the Edit an Existing User option.

Answering NO to the prompt "Is this person an active Trainee?" jumps you directly to the "Trainee Inactive (Date):" prompt. Respond to this prompt with the date the trainee is no longer participating in a formal academic training experience at your facility and complete filling out the form by updating any changes in the following editable fields:

- DEGREE (Field \#10.6)
- TITLE (Field \#8)
- SERVICE/SECTION (Field \#29)
- DOB (Field \#5)
- all address fields (Fields \#.111, \#.112, \#.113, \#.114, \#.115, and \#.116)
- E-MAIL ADDRESS (Field \#.151)

|                                                                                                                |                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/015.png) | NOTE: Answering No to the prompt "Is this person an active Trainee?" is part of an important new feature of this software as it provides the ability to inactivate and reactivate trainees between clinical rotations or VA training experiences. |

Of particular note, Figure 3‑7 shows that the following registered trainee information has been entered for the user named ONE KRNUSER:

- The Current Degree Level value, "MASTER'S," is the current degree held by the registered trainee upon entry into the current training program or residency at this particular VA medical facility.
- The Current Program of Study value, "HEALTH INFORMATION," is a discipline that best describes the current program of study. Answer this prompt with a selection from the list of pre-defined entries in the PROGRAM OF STUDY file (#8932.2).
- The Last Training Month and Year is "Oct 2007." This is the last year anticipated for training at this particular VAMC.
- The Trainee Inactive Date is only editable if you answer NO to the prompt "Is this person an active Trainee?:." This is the date that the trainee will no longer be an active registered trainee.

## Using the Trainee Registration Inquiry Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3‑8 illustrates how to access the Trainee Registration Inquiry option from the OAA Trainee Registration Menu:

<span id="_Ref42073611" class="anchor"></span>Figure ‑. Using the Trainee Registration Inquiry option

Select User Management Option: OAA\<Enter\> OAA Trainee Registration Menu

E Edit Trainee Registration Data

I Trainee Registration Inquiry

R Trainee Reports Menu ...

Select OAA Trainee Registration Menu Option: I \<Enter\> Trainee Registration Inquiry

Select NEW PERSON NAME: KRNUSER,ONE

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

The Trainee Registration Inquiry option \[XU-CLINICAL TRAINEE INQUIRY\] is located on the OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\]. This option displays various attributes of registered trainees.

Figure 3‑9 shows the output displayed after registered trainee information has been entered for the user ONE KRNUSER.

<span id="_Ref42073864" class="anchor"></span>Figure ‑. Trainee Registration Inquiry option

Registered Trainee Inquiry

KRNUSER,ONE (#76) Last Sign-on: Jun 23, 2005

Office Phone:

E-Mail Address: one.krnuser@med.va.gov SSN: \*\*\*\*\*5556

Title: DEVELOPER

Service/Section: IRM

Address:

250 Main St.

Anytown, CALIFORNIA 99999

Currently a Registered Trainee?: YES Date HL7 Record Built: MAY 5,2005

Date no longer a trainee:

Date started training: JAN 7,2004

Current Degree Lvl: MASTER'S

Program of Study: HEALTH INFORMATION

Last Training Month & Year: Oct 7 2007

VHA Training Facility: SAN FRANCISCO

## Kernel User Inquiry Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Inquiry option and the associated print template affected by the Trainee Registration Core Dataset software are shown in Table 3‑3.

<span id="_Ref22706272" class="anchor"></span>Table ‑. Affected Kernel option with associated print template

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>Print Template</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XUSERINQ</p>
<p>User Inquiry</p></td>
<td>XUSERINQ</td>
</tr>
</tbody>
</table>

The Kernel option itself has not been changed, but the print template has been modified to display the following three fields from the NEW PERSON file for registered trainees:

- CURRENT DEGREE LEVEL (#12.1) added with Patch XU\*8.0\*251
- PROGRAM OF STUDY (#12.2) added with Patch XU\*8.0\*251
- LAST TRAINING MONTH & YEAR (#12.3) modified with Patch XU\*8.0\*344
- VHA TRAINING FACILITY (#12.4) added with Patch XU\*8.0\*344

## Using the Trainee Reports Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trainee Reports Menu option is new with the Trainee Registration Core Dataset software. This option offers the following two report menus, providing VA facilities registered trainee information from local site databases and information on transmission reports to the OAA:

- Local Trainee Registration Reports ...
- Trainee Transmission Reports to OAA ...

|                                                                                                                |                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/016.png) | NOTE: Data for trainee reports can be retrieved as of June 2003, which is the date of the enactment of the VHA Directive 2003-032, Clinical Trainee Registration. There is no existing information on registered trainees before this date. |

### Local Trainee Registration Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3‑10 lists the various trainee registration reports that provide information from local site databases.

<span id="_Ref107398626" class="anchor"></span>Figure ‑. Using the Local Trainee Registration Reports option

Select User Management Option: OAA\<Enter\> OAA Trainee Registration Menu

E Edit Trainee Registration Data

I Trainee Registration Inquiry

R Trainee Reports Menu ...

Select OAA Trainee Registration Menu Option: r\<Enter\> Trainee Reports Menu

Local Trainee Registration Reports ...

Trainee Transmission Reports to OAA ...

Select Trainee Reports Menu Option: local Trainee Registration Reports

List of Active Registered Trainees

List of All Registered Trainees

List of Inactive Registered Trainees

Total Count of Registered Trainees

Select Local Trainee Registration Reports Option:

Examples of all four types of local trainee registration reports, Figure 3‑10, are shown on the next couple of pages.

#### List of Active Registered Trainees

This option produces a list of all local active registered trainees.

<span id="_Toc214422802" class="anchor"></span>Figure ‑. Report option—List of Active Registered Trainees

Select Local Trainee Registration Reports Option: List of Active Registered Trainees

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Active Registered Trainee List JUN 28,2005 13:42 PAGE 1

NAME/LAST4 SERVICE

--------------------------------------------------------------------------------

ACTIVE TRAINEE?: YES

TRAINING FACILITY: SAN FRANCISCO

KRNUSER,TWO(7777) IRM

KRNUSER,ONE(3333) IRM

Sites can schedule this report at regular intervals because the SCHEDULING RECOMMENDED field (#209), located in the OPTION file (#19), is set to YES.

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/017.png) | NOTE: This report can be lengthy depending on the numbers of registered trainees at various sites. Therefore, when producing this report it is recommended that it be queued. |

#### List of All Registered Trainees

This option produces a report, listing both active and inactive local registered trainees.

<span id="_Toc214422803" class="anchor"></span>Figure ‑. Report option—List of All Registered Trainees

Select Local Trainee Registration Reports Option: List of All Registered Trainees

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Registered Trainee List JUN 28,2005 13:51 PAGE 1

NAME/LAST4 SERVICE DATE

------------------------------------------------------------------------------

TRAINEE?: NO

TRAINING FACILITY: BECKLEY VAMC

KRNUSER,FOUR(0001) IRM 04/22/05

TRAINING FACILITY: SAN FRANCISCO

KRNUSER,THREE(5555) IRM 06/24/05

KRNUSER,FIVE(4444) IRM 03/02/05

KRNUSER,SIX(6666) IRM 03/09/05

TRAINEE?: YES

TRAINING FACILITY: SAN FRANCISCO

KRNUSER,TWO(7777) IRM

KRNUSER,ONE(3333) IRM

Sites can schedule this report at regular intervals because the SCHEDULING RECOMMENDED field (#209), located in the OPTION file (#19), is set to YES.

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/018.png) | NOTE: This report can be lengthy depending on the numbers of registered trainees at various sites. Therefore, when producing this report it is recommended that it be queued. |

#### List of Inactive Registered Trainees

This option produces a list of all local inactive registered trainees.

<span id="_Toc214422804" class="anchor"></span>Figure ‑. Report option—List of Inactive Registered Trainees

Select Local Trainee Registration Reports Option: List of Inactive Registered Trainees

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Non-Active Registered Trainees JUN 28,2005 14:06 PAGE 1

NAME/LAST4 SERVICE DATE

------------------------------------------------------------------------------

ACTIVE TRAINEE?: NO

TRAINING FACILITY: BECKLEY VAMC

KRNUSER,FOUR(0001) IRM 04/22/05

TRAINING FACILITY: SAN FRANCISCO

KRNUSER,THREE(5555) IRM 06/24/05

KRNUSER,FIVE(4444) IRM 03/02/05

KRNUSER,SIX(6666) IRM 03/09/05

Sites can schedule this report at regular intervals because the SCHEDULING RECOMMENDED field (#209), located in the OPTION file (#19), is set to YES.

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/019.png) | NOTE: This report can be lengthy depending on the numbers of registered trainees at various sites. Therefore, when producing this report it is recommended that it be queued. |

#### Total Count of Registered Trainees

This option reports the total number of local registered trainees entered into the sites' New Person file (#200). This allows the OAA to compare the number of trainees on their Web site with the total number of trainees in the VistA system, offering them the ability to crosscheck and verify that they are the same totals. This report counts both active and inactive trainees.

<span id="_Toc214422805" class="anchor"></span>Figure ‑. Report option—Total Count of Registered Trainees

Select Local Trainee Registration Reports Option: Total Count of Registered Trainees

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

OAA Registered Trainee Database Count JUN 28,2005 14:10 PAGE 1

------------------------------------------------------------------------------

COUNT 6

### Trainee Transmission Reports to OAA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3‑15 lists the various types of trainee registration transmission reports, which are sent to the Office of Academic Affiliations (OAA).

<span id="_Ref107399024" class="anchor"></span>Figure ‑. Using the Trainee Transmission Reports to OAA option

Select OAA Trainee Registration Menu Option: r\<Enter\> Trainee Reports Menu

Local Trainee Registration Reports ...

Trainee Transmission Reports to OAA ...

Select Trainee Reports Menu Option: Trainee Transmission Reports to OAA

Trainee Transmission Report by Date

Trainee Transmission Report by Range

Trainee Transmission Report Selectable Items

Select Trainee Transmission Reports to OAA Option:

Examples of all three types of trainee registration transmission reports, Figure 3‑15, are shown on the next couple of pages.

#### Trainee Transmission Report by Date

This option produces a report of local registered trainee records sent to the Office of Academic Affiliations (OAA) within a defined date range. VA medical facilities can use the information to verify:

- Which trainee records were sent from a particular site to the OAA on a specific date
- The total record count transmitted

Figure 3‑16 shows the user has elected to produce a report of all trainees sent to the OAA from June 6, 2005 through June 10, 2005.

Trainee records are sorted by the date they were sent to the OAA, shown on the report following the header "DATE TRANSMITTED TO OAA:." The VHA training facility from which the records were created and sent is displayed within each date group, shown on the report following the header "VHA TRAINING FACILITY:." Figure 3‑16 uses the Buffalo VAMC, which is an integrated VA medical facility, as an example. Buffalo, Albany, and Syracuse are shown as the VHA training facilities from which trainee records were transmitted on June 7, 2005 (JUN 7,2005). On June 10, 2005 (JUN 10,2005) trainee records were transmitted to the OAA from Buffalo, only. The trainee names and last four digits of their Social Security Numbers are displayed representing each record sent.

Records are subtotaled at the bottom of each date group, shown on the report following the header "SUBCOUNT." The grand total for all records sent to the OAA within the date range requested at report generation follows the header "COUNT."

The date and time that the report was run is included in the header to the right of the report title.

<span id="_Ref107736163" class="anchor"></span>Figure ‑. Report option—Trainee Transmission Report by Date

Select Trainee Transmission Reports to OAA Option: T

1 Trainee Transmission Report by Date

2 Trainee Transmission Report by Range

3 Trainee Transmission Report Selectable Items

CHOOSE 1-3: 1\<Enter\> Trainee Transmission Report by Date

\* Previous selection: DATE TRANSMITTED TO OAA from May 30, 2005

START WITH DATE HL7 TRAINEE RECORD BUILT: May 30, 2005// 6/6/05 \<Enter\> (JUN 06, 2005)

GO TO DATE HL7 TRAINEE RECORD BUILT: Jun 3, 2005// 6/10/05\<Enter\> (JUN 10, 2005)

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Registered Trainee Transmission Report JUN 29,2005 14:46 PAGE 1

NAME SSN

------------------------------------------------------------------------------

DATE TRANSMITTED TO OAA: JUN 7,2005

VHA TRAINING FACILITY: BUFFALO

KRNUSER,FOURTEEN \*\*\*\*\*0981

-----------------------------------

SUBCOUNT 1

VHA TRAINING FACILITY: SYRACUSE

KRNUSER,THIRTY \*\*\*\*\*5556

-----------------------------------

SUBCOUNT 1

VHA TRAINING FACILITY: ALBANY

KRNUSER,FIFTEEN \*\*\*\*\*3333

KRNUSER,TWENTY \*\*\*\*\*4321

KRNUSER,NINE \*\*\*\*\*1234

KRNUSER,THIRTYFIVE \*\*\*\*\*1212

KRNUSER,TEN \*\*\*\*\*7676

-----------------------------------

SUBCOUNT 5

SUBCOUNT 7

Registered Trainee Transmission Report JUN 29,2005 14:46 PAGE 2

NAME SSN

------------------------------------------------------------------------------

DATE TRANSMITTED TO OAA: JUN 10,2005

VHA TRAINING FACILITY: BUFFALO

KRNUSER,FIVE \*\*\*\*\*5556

-----------------------------------

SUBCOUNT 1

-----------------------------------

SUBCOUNT 1

-----------------------------------

COUNT 8

#### Trainee Transmission Report by Range

This option produces a report showing the total count(s) for local registered trainee records sent to the OAA within a defined period. VA medical facilities can use the information to verify the total number of records sent from the site to the Office of Academic Affiliations (OAA) for any given date.

Figure 3‑17 shows a scenario in which a report is being produced to list the total number of trainees sent to the OAA from June 6, 2005 through June 10, 2005.

Total counts for records sent to the OAA are sorted by the date of transmission, shown on the report following the header "DATE TRANSMITTED TO OAA:." The VHA training facility from which the records were created and sent is displayed within each date group, shown on the report following the header "VHA TRAINING FACILITY:." Figure 3‑17 uses the Buffalo VAMC, which is an integrated VA medical facility, as an example. The report shows the total counts for trainee records sent to the OAA on June 7, 2005 (JUN 7,2005) from the VHA training facilities Buffalo, Albany, and Syracuse. On June 10, 2005 (JUN 10,2005) the report shows that only Buffalo sent trainee records as the total counts are shown for Buffalo, only.

Records are subtotaled at the bottom of each date group, shown on the report following the header "SUBCOUNT." The grand total for all records sent to the OAA within the date range requested at report generation follows the header "COUNT."

The date and time the report was printed is included in the header to the right of the report title.

<span id="_Ref107825159" class="anchor"></span>Figure ‑. Report option—Trainee Transmission Report by Date

Select Trainee Transmission Reports to OAA Option: TRAINEE TRANSMISSION REPORT BY RANGE

1 Trainee Transmission Report by Date

2 Trainee Transmission Report by Range

3 Trainee Transmission Report Selectable Items

CHOOSE 1-3: 2 \<Enter\> Trainee Transmission Report by Range

\* Previous selection: DATE TRANSMITTED TO OAA from May 30,2005 to Jun 6,2005@24:00

START WITH DATE HL7 TRAINEE RECORD BUILT: Jun 6, 2005// 6/6/05 \<Enter\> (JUN 06, 2005)

GO TO DATE HL7 TRAINEE RECORD BUILT: Jun 3, 2005// 6/10/05 \<Enter\> (JUN 10, 2005)

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Summary Registered Trainee Transmission Report

JUN 29,2005 16:19 PAGE 1

------------------------------------------------------------------------------

DATE TRANSMITTED TO OAA: JUN 7,2005

VHA TRAINING FACILITY: BUFFALO

NAME: KRNUSER,FOURTEEN

SUBCOUNT 1

VHA TRAINING FACILITY: SYRACUSE

NAME: KRNUSER,THIRTY

SUBCOUNT 1

VHA TRAINING FACILITY: ALBANY

NAME: KRNUSER,FIFTEEN

NAME: KRNUSER,TWENTY

NAME: KRNUSER,NINE

NAME: KRNUSER,THIRTYFIVE

NAME: KRNUSER,TEN

SUBCOUNT 5

SUBCOUNT 7

DATE TRANSMITTED TO OAA: JUN 10,2005

VHA TRAINING FACILITY: BUFFALO

NAME: KRNUSER,FIVE

SUBCOUNT 1

SUBCOUNT 1

COUNT 8

#### Trainee Transmission Report Selectable Items

This option produces a report of all local trainee records sent to the Office of Academic Affiliations (OAA) defined by the following two ranges:

- Date
- VHA training facility

Integrated VA medical facilities can use this option to report which trainee records were sent to the OAA for either one or all associated facility divisions within a defined date range.

Figure 3‑18 shows an example of a report where the user has elected to print a list of all trainee records sent from the Albany training facility to the OAA between the dates May 16, 2005 through May 20, 2005.

Trainee records are sorted by the date that they were sent to the OAA, shown on the report following the header "DATE TRANSMITTED TO OAA:." The VHA training facility from which the records were created and sent is displayed within each date group, shown on the report following the header "VHA TRAINING FACILITY:." Figure 3‑18 uses the Buffalo VAMC, which is an integrated VA medical facility, as an example. The date range entered from which to report on trainee records sent to the OAA is June 6 2005 through June 10 2005. The VHA training facilities selected are Buffalo and Albany. The report output shows that trainee records were sent to the OAA from both the Buffalo and Albany VHA training facilities on June 7, 2005. On June 10, 2005 (JUN 10,2005) a trainee record was transmitted to the OAA from Buffalo, only. The trainee names and last four digits of their Social Security Numbers are displayed representing each record sent.

Records are subtotaled at the bottom of each date group, shown on the report following the header "SUBCOUNT." The grand total for all records sent to the OAA within the date range requested at report generation follows the header "COUNT."

The date and time that the report was run is included in the header to the right of the report title.

|                                                                                                                |                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/020.png) | NOTE: In VA FileMan, using the values FIRST to LAST to select VHA Training Facilities produces records for all VA medical facilities resident in your local database. |

<span id="_Ref107737729" class="anchor"></span>Figure ‑. Report option—Trainee Transmission Report Selectable Items

Select Trainee Transmission Reports to OAA Option: TR

1 Trainee Transmission Report by Date

2 Trainee Transmission Report by Range

3 Trainee Transmission Report Selectable Items

CHOOSE 1-3: 3 \<Enter\> Trainee Transmission Report Selectable Items

\* Previous selection: DATE TRANSMITTED TO OAA from May 9,2005 to May 13,2005@24:00

START WITH DATE HL7 TRAINEE RECORD BUILT: May 09,2005// 6/6/05 \<Enter\> (JUN 6, 2005)

GO TO DATE HL7 TRAINEE RECORD BUILT: May 13,2005// 6/10/05 \<Enter\> (JUN 10, 2005)

\* Previous selection: VHA TRAINING FACILITY equals BUFFALO

START WITH VHA TRAINING FACILITY: Buffalo// Albany

GO TO VHA TRAINING FACILITY: Buffalo// \<Enter\>

DEVICE: \<Enter\> SYSTEM Right Margin: 80// \<Enter\>

Selectable Registered Trainee Transmission Report

JUN 30,2005 13:25 PAGE 1

NAME SSN

-------------------------------------------------------------------------------

DATE TRANSMITTED TO OAA: JUN 07,2005

VHA TRAINING FACILITY: BUFFALO

KRNUSER,FOURTEEN \*\*\*\*\*0981

-----------------------------------

SUBCOUNT 1

VHA TRAINING FACILITY: ALBANY

KRNUSER,FIFTEEN \*\*\*\*\*3333

KRNUSER,TWENTY \*\*\*\*\*4321

KRNUSER,NINE \*\*\*\*\*1234

KRNUSER,THIRTYFIVE \*\*\*\*\*1212

KRNUSER,TEN \*\*\*\*\*7676

-----------------------------------

SUBCOUNT 5

-----------------------------------

SUBCOUNT 6

-----------------------------------

Selectable Registered Trainee Transmission Report

JUN 30,2005 13:25 PAGE 2

NAME SSN

-------------------------------------------------------------------------------

DATE TRANSMITTED TO OAA: JUN 10,2005

VHA TRAINING FACILITY: BUFFALO

KRNUSER,FIVE \*\*\*\*\*5556

-----------------------------------

SUBCOUNT 1

-----------------------------------

SUBCOUNT 1

-----------------------------------

COUNT 7

## Sort Criteria for Customizing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the VA FileMan conditional sort criteria used in each report on the Trainee Reports Menu \[XU-CLINICAL TRAINEE REPORTS\]. Sites wishing to elaborate upon or create their own local reports can use these sort criteria as a basis to do so. The conditional sort criteria are listed chronologically, beginning with the first sort field in ascending order by option name, menu text, and sort template.

<span id="_Toc214422810" class="anchor"></span>Table ‑. Sort criteria for customizing the List of Active Registered Trainees report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL ACTIVE TRAINEE</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>List of Active Registered Trainees</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL ACTIVE TRAINEE]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>PROGRAM OF STUDY (#12.2) if field value is not null (i.e., empty)</p>
</blockquote></li>
<li><blockquote>
<p>CLINICAL CORE TRAINEE (#12.6) if field equals Y (YES) or is null (i.e., empty)</p>
</blockquote></li>
<li><blockquote>
<p>VHA TRAINING FACILITY (#12.4) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc214422811" class="anchor"></span>Table ‑. Sort criteria for customizing the List of Inactive Registered Trainees report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL INACTIVE TRAINEE</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>List of Inactive Registered Trainees</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL INACTIVE TRAINEE]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>PROGRAM OF STUDY (#12.2) if field value is not null (i.e., empty)</p>
</blockquote></li>
<li><blockquote>
<p>CLINICAL CORE TRAINEE (#12.6) if field equals N (NO)</p>
</blockquote></li>
<li><blockquote>
<p>VHA TRAINING FACILITY (#12.4) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc214422812" class="anchor"></span>Table ‑. Sort criteria for customizing the Total Count of Registered Trainees report

| Option name   | XU-CLINICAL TRAINEE DB COUNT                                  |
|-------------------|-------------------------------------------------------------------|
| Menu text     | Total Count of Registered Trainees                                |
| Sort template | \[XU-CLINICAL TRAINEE DB COUNT\]                                  |
| Sort criteria | PROGRAM OF STUDY (#12.2) if field value is not null (i.e., empty) |

<span id="_Toc214422813" class="anchor"></span>Table ‑. Sort criteria for customizing the List of All Registered Trainees report

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL TRAINEE LIST</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>List of All Registered Trainees</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL TRAINEE LIST]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>PROGRAM OF STUDY (#12.2) if field value is not null (i.e., empty)</p>
</blockquote></li>
<li><blockquote>
<p>CLINICAL CORE TRAINEE (#12.6):</p>
</blockquote></li>
</ol>
<ul>
<li><blockquote>
<p>If field equals Y (YES)</p>
</blockquote></li>
<li><blockquote>
<p>If field equals N (NO)</p>
</blockquote></li>
<li><blockquote>
<p>Null value is equivalent to Yes</p>
</blockquote></li>
</ul>
<ol start="3" type="1">
<li><blockquote>
<p>VHA TRAINING FACILITY (#12.4) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc214422814" class="anchor"></span>Table ‑ Sort criteria for customizing the Trainee Transmission Report by Date

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL TRAINEE TRANSA</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>Trainee Transmission Report by Date</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL TRAINEE TRANSA]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>DATE HL7 TRAINEE RECORD BUILT (#12.5) the user sees:</p>
</blockquote></li>
</ol>
<p>DATE TRANSMITTED TO OAA</p>
<ol start="2" type="1">
<li><blockquote>
<p>All VHA TRAINING FACILITY (#12.4) (includes null values)</p>
</blockquote></li>
<li><blockquote>
<p>NAME (#.01) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc214422815" class="anchor"></span>Table ‑. Sort criteria for customizing the Trainee Transmission Report Selectable Items

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL TRAINEE TRANSB</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>Trainee Transmission Report Selectable Items</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL TRAINEE TRANSB]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>DATE HL7 TRAINEE RECORD BUILT (#12.5) the user sees:</p>
</blockquote></li>
</ol>
<p>DATE TRANSMITTED TO OAA</p>
<ol start="2" type="1">
<li><blockquote>
<p>NAME (#.01) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc251073869" class="anchor"></span>Table ‑. Sort criteria for customizing the Trainee Transmission Report by Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option name</strong></th>
<th><strong>XU-CLINICAL TRAINEE TRANSC</strong></th>
</tr>
<tr class="odd">
<th><strong>Menu text</strong></th>
<th>Trainee Transmission Report by Range</th>
</tr>
<tr class="header">
<th><strong>Sort template</strong></th>
<th>[XU-CLINICAL TRAINEE TRANSC]</th>
</tr>
<tr class="odd">
<th><strong>Sort criteria</strong></th>
<th><ol type="1">
<li><blockquote>
<p>DATE HL7 TRAINEE RECORD BUILT (#12.5) the user sees:</p>
</blockquote></li>
</ol>
<p>DATE TRANSMITTED TO OAA</p>
<ol start="2" type="1">
<li><blockquote>
<p>All VHA TRAINING FACILITY (#12.4) (includes null values)</p>
</blockquote></li>
<li><blockquote>
<p>NAME (#.01) if field value is not null (i.e., empty)</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# HL7 Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface specification is intended to identify the VistA information that will be shared as part of the Trainee Registration Core Dataset project. The sharing of this information will be triggered by specific VistA events. Both the exact events and the messages used to share this data will be reviewed.

The Trainee Registration Core Dataset application will make use of and create messages using the abstract message approach and encoding rules specified by the HL7 standard. The HL7 VistA application will be used for communicating data associated with various events that occur in health care environments.

The formats of these messages conform to HL7 interface standards, Version 2.4.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface documentation assumes that communication between the systems is established and maintained by VistA/Kernel processes. The discussion of specific technical issues related to this aspect of communication is beyond the scope of this chapter. This documentation also assumes a communication server utilizing VistA HL7 Version 1.6 or a similar compatible message communicator. VistA Kernel, MailMan, VA FileMan, and HL7 software applications are assumed the most recent versions and fully patched.

## Sending System and Receiving System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messaging occurs within the context of any VistA system being the originator of the message (Sending System) and a centralized database (Receiving System) located within the VHA Office of Academic Affiliations (OAA).

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updates to the registered trainee data will signal the creation of individual messages. A scheduled (daily) task will build a batch of messages for transmission to the OAA.

|                                                                                                                |                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/021.png) | REF: For more information on a scheduled daily task to build the batch messages for transmission to the VHA Office of Academic Affiliations, please refer to the section titled "Background Jobs" in the "Technical Manual Information" section of this supplement. |

## Batch Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each batch message will consist of PMU-B02 messages. Each message represents a single entry from the NEW PERSON file (#200) that was updated and is a part of the Trainee Registration Core Dataset. Below is an example of a batch of two messages:

<span id="_Toc214422817" class="anchor"></span>Figure ‑. Sample of two batch HL7 messages

BHS^~\|\\^XUOAA PMU^^XUOAA ACK^^20030520123707-0800^^~P~PMU\|B02~2.4^^99820884^

MSH^~\|\\^XUOAA PMU^^^^^^PMU~B02^99820884-2^T^2.4^^^^^USA

EVN^B02^20030519^^^^^662~SAN FRANCISCO

STF^9152~IEN~NEW PERSON^666333333\~\~~USSSA~SS^RTCDDEVELOPER~ONE^^^19810919^^^IRM\~~SERVICE/SECTION^^1301 CLAY STREET, 1301 Clay St., \#1350N, Development & Infrastructure~Veterans Health Administration~Oakland~CA~94612-5217~USA^^20020724132542-0700^^one.rtcdeveloper@med.va.gov^^^DEVELOPER

PRA^^^^^HEALTH INFORMATION\~\~\~~20070600

ORG^1^662~SAN FRANCISCO^IRM\~~SERVICE/SECTION^^^^^~HEALTH INFORMATION~PROGRAM OF STUDY^20020624132542-0700~20020624132542-0700

EDU^1^MAS

MSH^~\|\\^XUOAA PMU^^^^^^PMU~B02^9982783-1^T^2.4^^^^^USA

EVN^B02^20040526^^^^^662~SAN FRANCISCO

STF^9152~IEN~NEW PERSON^666744635\~\~~USSSA~SS^RTCDDEVELOPTER~TWO^^^19551004^^^IRM\~~SERVICE/SECTION^^1301 Clay St., \#1350N, Pharmacy Development~Veterans Health Administration~Oakland~CA~94612~USA^^^^two.rtcddeveloper@med.va.gov  
^^^DEVELOPER

PRA^^^^^DIETETICS\~\~\~~20060600

ORG^1^662~SAN FRANCISCO^IRM\~~SERVICE/SECTION^^^^^~DIETETICS~PROGRAM OF STUDY^20001101~

EDU^1^DOC

BTS^2

## Batch Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since HL7 messaging is being delivered using MailMan, Simple Mail Transport Protocol (SMTP), the OAA opted to not generate an HL7 application acknowledgement. This is because MailMan uses the guaranteed message delivery of SMTP. If the project ever changes to Minimal Lower Level Protocol (MLLP), then the OAA may be required to generate the application acknowledgement.

## HL7 Message Profile for PMU-B02

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a description of an HL7 message profile as defined by the HL7 organization. Z (extended) elements are not used.

<span id="_Toc214422818" class="anchor"></span>Table ‑. HL7 Message Profile for PMU-B02

|                         |                                    |
|-------------------------|------------------------------------|
| Interface ID        |   XUOAA PMU                        |
| Organization        |                                    |
| HL7 Version         |   HL7 2.4                          |
| Spec Version        |   HL7 2.4                          |
| Application Role    |   Sender                           |
| Conformance Type    |  Implementation                    |
| Encodings           |  ER7                               |
| Event Description   |   - Add personnel record           |
| Message Type        |   PMU                              |
| Event Type          |   B02                              |
| Order Control Code  |                                    |
| Message Structure   |   BHS,{MSH,EVN,STF,PRA,ORG,EDU}BTS |
|                         |                                    |
| Structure Type      |   PMU_B01                          |
| Accept Ack          |                                    |
| Application Ack     |                                    |
| Ack Mode            |                                    |
| Static Profile ID   |                                    |
| Dynamic Profile ID  |                                    |

## HL7 Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category; segments are also described. The messages are presented in the following categories:

- Message Control
- Unsolicited Transactions from VistA

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, incoming or outgoing messages are handled or generated based on an event.

In this section and in the sections following, these elements are defined for each message:

- The trigger events.
- The message event code.
- A list of segments used in the message.
- A list of fields for each segment in the message.

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. Square brackets (\[\]) indicate the segment is optional, curly brackets ({}) indicate the segment is repeatable. For each message category there will be a list of HL7 standard segments.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments contained in message-types described in this document. These are generic descriptions. All of the segments described in this section are included in messages in this document. The VistA descriptions and mappings will be as specified here unless otherwise noted.

- BHS—Batch Header Segment (required, *not* repeatable)
- BTS—Batch Trailer Segment (required, *not* repeatable)
- MSH—Message Header (required, *not* repeatable)
- EVN—Event Type Segment (required, *not* repeatable)
- STF—Staff Identification (required, *not* repeatable)
- PRA—Practitioner Detail (required, repeatable)
- ORG—Practitioner Organization Unit (required, repeatable)
- EDU—Educational Detail (required, repeatable)

### Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format on the following pages. Each table includes information such as the sequence number (SEQ), data type (DT), maximum length (LEN), required or optional (R/O), repeatable (RP/#), the table number (TBL \#), the element name, and the VistA description.

Legend

This Legend serves as a key to define the column headings for the segment tables documented on the following pages.

Codes:

- R - required
- RE - required or empty
- C - conditional
- CE - conditional or empty
- O - optional
- NS - not supported
- U - unknown

Abbreviations:

- seq - sequence
- DT - datatype
- Len - length
- Opt - optionality
- Rep - repeatable
- Min - quantity min
- Max - quantity max
- Tbl - table

### BHS—Batch Header Segment (Required, *not* Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc251073871" class="anchor"></span>Table ‑. HL7 Batch Header Segment (BHS)

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Example Value</th>
<th>Seq</th>
<th>Dt</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Min</th>
<th>Max</th>
<th>Tbl</th>
<th>Ref</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Batch Field Separator</td>
<td>^</td>
<td>  1</td>
<td>ST</td>
<td>1</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td>2.16.2.1</td>
</tr>
<tr class="even">
<td><p>Batch Encoding</p>
<p>Characters</p></td>
<td>~|\&amp;</td>
<td>  2</td>
<td>ST</td>
<td>3</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td>2.16.2.2</td>
</tr>
<tr class="odd">
<td><p>Batch Sending</p>
<p>Application</p></td>
<td>XUOAA PMU</td>
<td>  3</td>
<td>ST</td>
<td>15</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.3</td>
</tr>
<tr class="even">
<td><p>Batch Sending</p>
<p>Facility</p></td>
<td></td>
<td>  4</td>
<td>ST</td>
<td>20</td>
<td>  R</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.4</td>
</tr>
<tr class="odd">
<td><p>Batch Receiving</p>
<p>Application</p></td>
<td>XUOAA ACK</td>
<td>5</td>
<td>ST</td>
<td>15</td>
<td>  R</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.3</td>
</tr>
<tr class="even">
<td><p>Batch Receiving</p>
<p>Facility</p></td>
<td></td>
<td>  6</td>
<td>ST</td>
<td>20</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.4</td>
</tr>
<tr class="odd">
<td><p>Batch Creation</p>
<p>Date/Time</p></td>
<td></td>
<td>  7</td>
<td>TS</td>
<td>26</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.7</td>
</tr>
<tr class="even">
<td>Date/Time</td>
<td>20021016154059-0800</td>
<td>  1</td>
<td>NM</td>
<td>0</td>
<td>  R</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td></td>
</tr>
<tr class="odd">
<td>degree of precision</td>
<td></td>
<td>  2</td>
<td> ST</td>
<td>0</td>
<td>  O</td>
<td></td>
<td> </td>
<td> </td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>Batch Security</td>
<td></td>
<td>  8</td>
<td>ST</td>
<td>40</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.8</td>
</tr>
<tr class="odd">
<td>Batch Name/ID/Type</td>
<td>~P~PMU|B02~2.4</td>
<td>  9</td>
<td>ST</td>
<td>20</td>
<td>  R</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.9</td>
</tr>
<tr class="even">
<td>Batch Name/ID/Type_rep</td>
<td></td>
<td>  9</td>
<td>ST</td>
<td>20</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.9</td>
</tr>
<tr class="odd">
<td>Batch Comment</td>
<td></td>
<td>  10</td>
<td> ST</td>
<td>80</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.3.2</td>
</tr>
<tr class="even">
<td>Batch Control ID</td>
<td>99820884</td>
<td>  11</td>
<td> ST</td>
<td>20</td>
<td>  R</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.11</td>
</tr>
<tr class="odd">
<td>Reference Batch Control ID</td>
<td></td>
<td>  12</td>
<td> ST</td>
<td>20</td>
<td>  O</td>
<td>False</td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td>2.16.2.12</td>
</tr>
</tbody>
</table>

### BTS—Batch Trailer Segment (Required, *not* Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422820" class="anchor"></span>Table ‑. HL7 Batch Trailer Segment (BTS)

| Element Name        | Example Value | Seq | DT   | Len  | Opt | Rep   | Min | Max | Tbl | Ref       |
|---------------------|---------------|-----|------|------|-----|-------|-----|-----|-----|-----------|
| Batch Message Count |   2           |   1 |   ST |   10 |  O  | False |   0 |   1 |     |  2.16.3.1 |
| Batch Comment       |               |   2 |   ST |   80 |  O  | False |   0 |   1 |     |  2.16.3.2 |
| Batch Totals        |               |   3 | NM   | 100  |  O  | True  |   0 |   0 |     |  2.16.3.3 |

### MSH—Message Header Segment (Required, *not* Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc251073873" class="anchor"></span>Table ‑. HL7 Message Header Segment (MSH)

| Element Name                            | Example Value | Seq | DT     | Len | Opt | Rep   | Min | Max | Tbl  | Ref       |
|-----------------------------------------|---------------|-----|--------|-----|-----|-------|-----|-----|------|-----------|
| Field Separator                         | ^             | 1   | ST     | 1   | R   | False | 1   | 1   |      | 2.16.9.1  |
| Encoding Characters                     | ~\|\\         | 2   | ST     | 4   | R   | False | 1   | 1   |      | 2.16.9.2  |
| Sending Application                     |               | 3   | HD     | 180 | R   | False | 0   | 0   | 0361 | 2.16.9.3  |
| namespace ID                            | XUOAA PMU     | 1   | IS     | 3   | R   |       |     |     | 0363 |           |
| universal ID                            |               | 2   | ST     | 3   | NS  |       |     |     |      |           |
| universal ID type                       |               | 3   | ID     | 3   | NS  |       |     |     | 0301 |           |
| Sending Facility                        |               | 4   | HD     | 180 | NS  | False | 0   | 0   | 0362 |           |
| namespace ID                            |               | 1   | IS     | 3   | NS  |       |     |     | 0363 |           |
| universal ID                            |               | 2   | ST     | 3   | NS  |       |     |     |      |           |
| universal ID type                       |               | 3   | ID     | 3   | NS  |       |     |     | 0301 |           |
| Receiving Application                   |               | 5   | HD     | 180 | NS  | False | 0   | 0   | 0361 |           |
| namespace ID                            |               | 1   | IS     | 3   | NS  |       |     |     | 0363 |           |
| universal ID                            |               | 2   | ST     | 3   | NS  |       |     |     |      |           |
| universal ID type                       |               | 3   | ID     | 3   | NS  |       |     |     | 0301 |           |
| Receiving Facility                      |               | 6   | HD     | 180 | NS  | False | 1   | 1   | 0362 | 2.16.9.6  |
| namespace ID                            |               | 1   | IS     | 3   | NS  |       |     |     | 0363 |           |
| universal ID                            |               | 2   | ST     | 3   | NS  |       |     |     |      |           |
| universal ID type                       |               | 3   | ID     | 3   | NS  |       |     |     | 0301 |           |
| Date/Time Of Message                    |               | 7   | TS     | 26  | NS  | False | 1   | 1   |      | 2.16.9.7  |
| Date/Time                               |               | 1   | NM     | 0   | NS  |       |     |     |      |           |
| degree of precision                     |               | 2   | ST     | 0   | NS  |       |     |     |      |           |
| Security                                |               | 8   | ST     | 40  | NS  | False | 1   | 1   |      | 2.16.9.8  |
| Message Type                            |               | 9   | CM_MSG | 15  | NS  | False | 1   | 1   | 0076 | 2.16.9.9  |
| message type                            | PMU           | 1   | ID     | 3   | R   |       |     |     | 0076 |           |
| trigger event                           | B02           | 2   | ID     | 3   | R   |       |     |     | 0003 |           |
| message structure                       |               | 3   | ID     | 3   | NS  |       |     |     | 0354 |           |
| Message Control ID                      | 9982783-1     | 10  | ST     | 20  | R   | False | 1   | 1   |      | 2.16.9.10 |
| Processing ID                           |               | 11  | PT     | 3   | R   | False | 1   | 1   |      | 2.16.9.11 |
| processing ID                           | T             | 1   | ID     | 3   | R   |       |     |     | 0103 |           |
| processing mode                         |               | 2   | ID     | 3   | NS  |       |     |     | 0207 |           |
| Version ID                              |               | 12  | VID    | 60  | R   | False | 1   | 1   | 0104 | 2.16.9.12 |
| version ID                              | 2.4           | 1   | ID     | 3   | R   |       |     |     | 0104 |           |
| internationalization code               |               | 2   | CE     | 0   | NS  |       |     |     |      |           |
| international version ID                |               | 3   | CE     | 0   | NS  |       |     |     |      |           |
| Sequence Number                         |               | 13  | NM     | 15  | NS  | False | 0   | 0   |      | 2.16.9.13 |
| Continuation Pointer                    |               | 14  | ST     | 180 | NS  | False | 0   | 0   |      | 2.16.9.14 |
| Accept Acknowledgment Type              |               | 15  | ID     | 2   | NS  | False | 1   | 1   | 0155 | 2.16.9.15 |
| Application Acknowledgment Type         |               | 16  | ID     | 2   | NS  | False | 1   | 1   | 0155 | 2.16.9.16 |
| Country Code                            | USA           | 17  | ID     | 3   | RE  | False | 1   | 1   | 0399 | 2.16.9.17 |
| Character Set                           |               | 18  | ID     | 16  | NS  | False | 0   | 0   | 0211 | 2.16.9.18 |
| Principal Language Of Message           |               | 19  | CE     | 250 | NS  | False | 0   | 0   |      | 2.16.9.19 |
| Alternate Character Set Handling Scheme |               | 20  | ID     | 20  | NS  | False | 0   | 0   | 0356 | 2.16.9.20 |
| Conformance Statement ID                |               | 21  | ID     | 10  | NS  | False | 0   | 0   | 0449 | 2.16.9.21 |

### EVN—Event Type Segment (Required, *not* Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422822" class="anchor"></span>Table ‑. HL7 Event Type Segment (EVN)

| Element Name            | Example Value | Seq | DT  | Len | Opt | Rep   | Min | Max | Tbl  | Ref     |
|-------------------------|---------------|-----|-----|-----|-----|-------|-----|-----|------|---------|
| Event Type Code         | B02           | 1   | ID  | 3   | R   | False |     | 1   | 0003 | 3.4.1.1 |
| Recorded Date/Time      |               | 2   | TS  | 26  | R   | False |     | 1   |      | 3.4.1.2 |
| Date/Time               | 20040526      | 1   | NM  | 0   | R   |       |     |     |      |         |
| degree of precision     |               | 2   | ST  | 0   | NS  |       |     |     |      |         |
| Date/Time Planned Event |               | 3   | TS  | 26  | NS  | False |     | 0   |      | 3.4.1.3 |
| Event Reason Code       |               | 4   | IS  | 3   | NS  | False |     | 0   | 0062 | 3.4.1.4 |
| Operator ID             |               | 5   | XCN | 250 | NS  | False |     | 0   | 0188 | 3.4.1.5 |
| Event Occurred          |               | 6   | TS  | 26  | NS  | False |     | 0   |      | 3.4.1.6 |
| Event Facility          |               | 7   | HD  | 180 | R   | False |     | 0   |      | 3.4.1.7 |
| namespace ID            | 662           | 1   | IS  | 3   | R   |       |     |     |      |         |
| universal ID            | SAN FRANCISCO | 2   | ST  | 30  | R   |       |     |     |      |         |

### STF—Staff Identification (Required, *not* Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422823" class="anchor"></span>Table ‑. HL7 Staff Identification Segment (STF)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Example Value</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Min</th>
<th>Max</th>
<th>Tbl</th>
<th>Ref</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Primary Key Value - STF</td>
<td></td>
<td>1</td>
<td>CE</td>
<td>250</td>
<td>C</td>
<td>False</td>
<td>0</td>
<td>1</td>
<td>9999</td>
<td>15.4.6.1</td>
</tr>
<tr class="even">
<td>identifier</td>
<td>9152</td>
<td>1</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>text</td>
<td>IEN</td>
<td>2</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>name of coding system</td>
<td>NEW PERSON</td>
<td>3</td>
<td>IS</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="odd">
<td>alternate identifier</td>
<td></td>
<td>4</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>alternate text</td>
<td></td>
<td>5</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>name of alternate coding system</td>
<td></td>
<td>6</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="even">
<td>Staff ID Code</td>
<td></td>
<td>2</td>
<td>CX</td>
<td>60</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.2</td>
</tr>
<tr class="odd">
<td>ID</td>
<td>666744635</td>
<td>1</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Check digit</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>code identifying the check digit scheme employed</td>
<td></td>
<td>3</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0061</td>
<td></td>
</tr>
<tr class="even">
<td>assigning authority</td>
<td></td>
<td>4</td>
<td>HD</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>namespace ID</td>
<td>USSSA</td>
<td>1</td>
<td>IS</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>0363</td>
<td></td>
</tr>
<tr class="even">
<td>universal ID</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>universal ID type</td>
<td></td>
<td>3</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0301</td>
<td></td>
</tr>
<tr class="even">
<td>identifier type code (ID)</td>
<td>SS</td>
<td>5</td>
<td>ID</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>0203</td>
<td></td>
</tr>
<tr class="odd">
<td>assigning facility</td>
<td></td>
<td>6</td>
<td>HD</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>effective date (DT)</td>
<td></td>
<td>7</td>
<td>DT</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>expiration date</td>
<td></td>
<td>8</td>
<td>DT</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Staff Name</td>
<td></td>
<td>3</td>
<td>XPN</td>
<td>250</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.3</td>
</tr>
<tr class="odd">
<td>family name</td>
<td></td>
<td>1</td>
<td>FN</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>surname</td>
<td>RTCDDEVELOPTER</td>
<td>1</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>own surname prefix</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>own surname</td>
<td></td>
<td>3</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>surname prefix from partner/spouse</td>
<td></td>
<td>4</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>surname from partner/spouse</td>
<td></td>
<td>5</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>given name</td>
<td>ONE</td>
<td>2</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>second and further given names or initials thereof</td>
<td></td>
<td>3</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>suffix (e.g., JR or III)</td>
<td></td>
<td>4</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>prefix (e.g., DR)</td>
<td></td>
<td>5</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>degree (e.g., MD)</td>
<td></td>
<td>6</td>
<td>IS</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td>0360</td>
<td></td>
</tr>
<tr class="even">
<td>name type code</td>
<td></td>
<td>7</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0200</td>
<td></td>
</tr>
<tr class="odd">
<td>Name Representation code</td>
<td></td>
<td>8</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0465</td>
<td></td>
</tr>
<tr class="even">
<td>name context</td>
<td></td>
<td>9</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>name validity range</td>
<td></td>
<td>10</td>
<td>DR</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>name assembly order</td>
<td></td>
<td>11</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0444</td>
<td></td>
</tr>
<tr class="odd">
<td>Staff Type</td>
<td></td>
<td>4</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0182</td>
<td>15.4.6.4</td>
</tr>
<tr class="even">
<td>Administrative Sex</td>
<td></td>
<td>5</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0001</td>
<td>15.4.6.5</td>
</tr>
<tr class="odd">
<td>Date/Time Of Birth</td>
<td>19810919</td>
<td>6</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.6</td>
</tr>
<tr class="even">
<td>Active/Inactive Flag</td>
<td></td>
<td>7</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0183</td>
<td>15.4.6.7</td>
</tr>
<tr class="odd">
<td>Department</td>
<td></td>
<td>8</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0184</td>
<td>15.4.6.8</td>
</tr>
<tr class="even">
<td>Hospital Service</td>
<td></td>
<td>9</td>
<td>CE</td>
<td>250</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td>0069</td>
<td>15.4.6.9</td>
</tr>
<tr class="odd">
<td>identifier</td>
<td>IRM</td>
<td>1</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>text</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>name of coding system</td>
<td>SERVICE/SECTION</td>
<td>3</td>
<td>IS</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="even">
<td>alternate identifier</td>
<td></td>
<td>4</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>alternate text</td>
<td></td>
<td>5</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>name of alternate coding system</td>
<td></td>
<td>6</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="odd">
<td>Phone</td>
<td></td>
<td>10</td>
<td>XTN</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.10</td>
</tr>
<tr class="even">
<td>Office/Home Address</td>
<td></td>
<td>11</td>
<td>XAD</td>
<td>250</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.11</td>
</tr>
<tr class="odd">
<td>street address (SAD)</td>
<td></td>
<td>1</td>
<td>SAD</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>street or mailing address</td>
<td>1301 Clay Street,<br />
#1350N,<br />
Development &amp; Infrastructure</td>
<td>1</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>street name</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>dwelling number</td>
<td></td>
<td>3</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>other designation</td>
<td>Veterans Health Administration</td>
<td>2</td>
<td>ST</td>
<td></td>
<td>RE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>city</td>
<td>Oakland</td>
<td>3</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>state or province</td>
<td>CA</td>
<td>4</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>zip or postal code</td>
<td>94612-5217</td>
<td>5</td>
<td>ST</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>country</td>
<td>USA</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>0399</td>
<td></td>
</tr>
<tr class="even">
<td>address type</td>
<td></td>
<td>7</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0190</td>
<td></td>
</tr>
<tr class="odd">
<td>other geographic designation</td>
<td></td>
<td>8</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>county/parish code</td>
<td></td>
<td>9</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0289</td>
<td></td>
</tr>
<tr class="odd">
<td>census tract</td>
<td></td>
<td>10</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0288</td>
<td></td>
</tr>
<tr class="even">
<td>address representation code</td>
<td></td>
<td>11</td>
<td>ID</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0465</td>
<td></td>
</tr>
<tr class="odd">
<td>address validity range</td>
<td></td>
<td>12</td>
<td>DR</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Institution Activation Date</td>
<td></td>
<td>12</td>
<td>CM_DIN</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.12</td>
</tr>
<tr class="odd">
<td>date</td>
<td></td>
<td>1</td>
<td>TS</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Date/Time</td>
<td></td>
<td>1</td>
<td>NM</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>degree of precision</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>institution name</td>
<td></td>
<td>2</td>
<td>CE</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Institution Inactivation Date</td>
<td></td>
<td>13</td>
<td>CM_DIN</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.13</td>
</tr>
<tr class="even">
<td>date</td>
<td></td>
<td>1</td>
<td>TS</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time</td>
<td>20020724132542-0700</td>
<td>1</td>
<td>NM</td>
<td></td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>degree of precision</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>institution name</td>
<td></td>
<td>2</td>
<td>CE</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>identifier</td>
<td></td>
<td>1</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>text</td>
<td></td>
<td>2</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>name of coding system</td>
<td></td>
<td>3</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="odd">
<td>alternate identifier</td>
<td></td>
<td>4</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>alternate text</td>
<td></td>
<td>5</td>
<td>ST</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>name of alternate coding system</td>
<td></td>
<td>6</td>
<td>IS</td>
<td></td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td>0396</td>
<td></td>
</tr>
<tr class="even">
<td>Backup Person ID</td>
<td></td>
<td>14</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.14</td>
</tr>
<tr class="odd">
<td>E-Mail Address</td>
<td>one.rtcdperson@med.va.gov</td>
<td>15</td>
<td>ST</td>
<td>40</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.15</td>
</tr>
<tr class="even">
<td>Preferred Method of Contact</td>
<td></td>
<td>16</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0185</td>
<td>15.4.6.16</td>
</tr>
<tr class="odd">
<td>Marital Status</td>
<td></td>
<td>17</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0002</td>
<td>15.4.6.17</td>
</tr>
<tr class="even">
<td>Job Title</td>
<td>DEVELOPER</td>
<td>18</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td>False</td>
<td>1</td>
<td>1</td>
<td></td>
<td>15.4.6.18</td>
</tr>
<tr class="odd">
<td>Job Code/Class</td>
<td></td>
<td>19</td>
<td>JCC</td>
<td>20</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0327</td>
<td>15.4.6.19</td>
</tr>
<tr class="even">
<td>Employment Status Code</td>
<td></td>
<td>20</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0066</td>
<td>15.4.6.20</td>
</tr>
<tr class="odd">
<td>Additional Insured on Auto</td>
<td></td>
<td>21</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0136</td>
<td>15.4.6.21</td>
</tr>
<tr class="even">
<td>Driver's License Number - Staff</td>
<td></td>
<td>22</td>
<td>DLN</td>
<td>25</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.22</td>
</tr>
<tr class="odd">
<td>Copy Auto Ins</td>
<td></td>
<td>23</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0136</td>
<td>15.4.6.23</td>
</tr>
<tr class="even">
<td>Auto Ins. Expires</td>
<td></td>
<td>24</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.24</td>
</tr>
<tr class="odd">
<td>Date Last DMV Review</td>
<td></td>
<td>25</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.25</td>
</tr>
<tr class="even">
<td>Date Next DMV Review</td>
<td></td>
<td>26</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td></td>
<td>15.4.6.26</td>
</tr>
<tr class="odd">
<td>Race</td>
<td></td>
<td>27</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0005</td>
<td>15.4.6.27</td>
</tr>
<tr class="even">
<td>Ethnic Group</td>
<td></td>
<td>28</td>
<td>CE</td>
<td>250</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0189</td>
<td>15.4.6.28</td>
</tr>
<tr class="odd">
<td>Re-activation Approval Indicator</td>
<td></td>
<td>29</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td>False</td>
<td>0</td>
<td>0</td>
<td>0136</td>
<td>15.4.6.29</td>
</tr>
</tbody>
</table>

### PRA—Practitioner Detail (Required, Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422824" class="anchor"></span>Table ‑. HL7 Practitioner Detail Segment (PRA)

| Element Name                                 | Example Value      | Seq | DT     | Len | Opt | Rep   | Min | Max | Tbl  | Ref       |
|----------------------------------------------|--------------------|-----|--------|-----|-----|-------|-----|-----|------|-----------|
| Primary Key Value - PRA                      |                    | 1   | CE     | 250 | NS  | False | 0   | 1   | 9999 | 15.4.5.1  |
| Practitioner Group                           |                    | 2   | CE     | 250 | NS  | False | 0   | 0   | 0358 | 15.4.5.2  |
| Practitioner Category                        |                    | 3   | IS     | 3   | NS  | False | 0   | 0   | 0186 | 15.4.5.3  |
| Provider Billing                             |                    | 4   | ID     | 1   | NS  | False | 0   | 0   | 0187 | 15.4.5.4  |
| Specialty                                    |                    | 5   | CM_SPD | 100 | R   | False | 0   | 0   | 0337 | 15.4.5.5  |
| specialty name                               | HEALTH INFORMATION | 1   | ST     |     | R   |       |     |     |      |           |
| governing board                              |                    | 2   | ST     |     | NS  |       |     |     |      |           |
| eligible or certified                        |                    | 3   | ID     |     | NS  |       |     |     |      |           |
| date of certification                        | 20070600           | 4   | DT     |     | NS  |       |     |     |      |           |
| Practitioner ID Numbers                      |                    | 6   | CM_PLN | 100 | NS  | False | 0   | 0   | 0338 | 15.4.5.6  |
| Privileges                                   |                    | 7   | CM_PIP | 200 | NS  | False | 0   | 0   |      | 15.4.5.7  |
| Date Entered Practice                        |                    | 8   | DT     | 8   | NS  | False | 0   | 0   |      | 15.4.5.8  |
| Institution                                  |                    | 9   | CE     | 250 | NS  | False | 0   | 0   |      | 15.4.5.9  |
| Date Left Practice                           |                    | 10  | DT     | 8   | NS  | False | 0   | 0   |      | 15.4.5.10 |
| Government Reimbursement Billing Eligibility |                    | 11  | CE     | 250 | NS  | False | 0   | 0   | 0401 | 15.4.5.11 |
| Set ID - PRA                                 |                    | 12  | SI     | 60  | NS  | False | 0   | 1   |      | 15.4.5.12 |

### ORG—Practitioner Organization Unit (Required, Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422825" class="anchor"></span>Table ‑. HL7 Practitioner Organization Unit Segment (ORG)

| Element Name                                     | Example Value       | Seq | DT  | Len | Opt | Rep   | Min | Max | Tbl  | Ref       |
|--------------------------------------------------|---------------------|-----|-----|-----|-----|-------|-----|-----|------|-----------|
| Set ID - ORG                                     | 1                   | 1   | SI  | 60  | R   | False | 1   | 1   |      | 15.4.4.1  |
| Organization Unit Code                           |                     | 2   | CE  | 250 | R   | False | 0   | 0   | 0405 | 15.4.4.2  |
| identifier                                       | 662                 | 1   | ST  | 0   | R   |       |     |     |      |           |
| text                                             | SAN FRANCISCO       | 2   | ST  | 3   | R   |       |     |     |      |           |
| name of coding system                            |                     | 3   | IS  | 3   | NS  |       |     |     | 0396 |           |
| alternate identifier                             |                     | 4   | ST  | 3   | NS  |       |     |     |      |           |
| alternate text                                   |                     | 5   | ST  | 3   | NS  |       |     |     |      |           |
| name of alternate coding system                  |                     | 6   | IS  | 3   | NS  |       |     |     | 0396 |           |
| Organization Unit Type Code - ORG                |                     | 3   | CE  | 250 | R   | False | 0   | 0   | 0474 | 15.4.4.3  |
| identifier                                       | IRM                 | 1   | ST  | 0   | R   |       |     |     |      |           |
| text                                             |                     | 2   | ST  | 3   | NS  |       |     |     |      |           |
| name of coding system                            | SERVICE/SECTION     | 3   | IS  | 3   | R   |       |     |     | 0396 |           |
| Alternate identifier                             |                     | 4   | ST  | 3   | NS  |       |     |     |      |           |
| alternate text                                   |                     | 5   | ST  | 3   | NS  |       |     |     |      |           |
| name of alternate coding system                  |                     | 6   | IS  | 3   | NS  |       |     |     | 0396 |           |
| Primary Org Unit Indicator                       |                     | 4   | ID  | 1   | NS  | False | 0   | 0   | 0136 | 15.4.4.4  |
| Practitioner Org Unit Identifier                 |                     | 5   | CX  | 60  | NS  | False | 0   | 0   |      | 15.4.4.5  |
| Health Care Provider Type Code                   |                     | 6   | CE  | 250 | NS  | False | 0   | 0   | 0452 | 15.4.4.6  |
| Health Care Provider Classification Code         |                     | 7   | CE  | 250 | NS  | False | 0   | 0   | 0453 | 15.4.4.7  |
| Health Care Provider Area of Specialization Code |                     | 8   | CE  | 250 | R   | False | 0   | 0   | 0454 | 15.4.4.8  |
| identifier                                       |                     | 1   | ST  | 0   | NS  |       |     |     |      |           |
| text                                             | HEALTH INFORMATION  | 2   | ST  | 3   | R   |       |     |     |      |           |
| name of coding system                            | PROGRAM OF STUDY    | 3   | IS  | 3   | R   |       |     |     | 0396 |           |
| alternate identifier                             |                     | 4   | ST  | 3   | NS  |       |     |     |      |           |
| alternate text                                   |                     | 5   | ST  | 3   | NS  |       |     |     |      |           |
| name of alternate coding system                  |                     | 6   | IS  | 3   | NS  |       |     |     | 0396 |           |
| Effective Date Range                             |                     | 9   | DR  | 52  | R   | False | 0   | 0   |      | 15.4.4.9  |
| range start date/time                            |                     | 1   | TS  | 3   | R   |       |     |     |      |           |
| Date/Time                                        | 20020624132542-0700 | 1   | NM  | 0   | R   |       |     |     |      |           |
| degree of precision                              |                     | 2   | ST  | 0   | NS  |       |     |     |      |           |
| range end date/time                              |                     | 2   | TS  | 3   | R   |       |     |     |      |           |
| Date/Time                                        | 20020624132542-0700 | 1   | NM  | 0   | R   |       |     |     |      |           |
| degree of precision                              |                     | 2   | ST  | 0   | NS  |       |     |     |      |           |
| Employment Status Code                           |                     | 10  | CE  | 250 | NS  | False | 0   | 0   | 0066 | 15.4.6.20 |
| Board Approval Indicator                         |                     | 11  | ID  | 1   | NS  | False | 0   | 0   | 0136 | 15.4.4.11 |
| Primary Care Physician Indicator                 |                     | 12  | ID  | 1   | NS  | False | 0   | 0   | 0136 | 15.4.4.12 |

### EDU—Educational Detail (Required, Repeatable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422826" class="anchor"></span>Table ‑. HL7 Educational Detail Segment (EDU)

| Element Name                                    | Example Value | Seq | DT  | Len | Opt | Rep   | Min | Max | Tbl  | Ref      |
|-------------------------------------------------|---------------|-----|-----|-----|-----|-------|-----|-----|------|----------|
| Set ID - EDU                                    | 1             | 1   | SI  | 60  | R   | False | 1   | 1   |      | 15.4.2.1 |
| Academic Degree                                 | MAS           | 2   | IS  | 10  | R   | False | 1   | 1   | 0360 | 15.4.2.2 |
| Academic Degree Program Date Range              |               | 3   | DR  | 52  | NS  | False | 0   | 0   |      | 15.4.2.3 |
| Academic Degree Program ParticipationDate Range |               | 4   | DR  | 52  | NS  | False | 0   | 0   |      | 15.4.2.4 |
| Academic Degree Granted Date                    |               | 5   | DT  | 8   | NS  | False | 0   | 0   |      | 15.4.2.5 |
| School                                          |               | 6   | XON | 250 | NS  | False | 0   | 0   |      | 15.4.2.6 |
| School Type Code                                |               | 7   | CE  | 250 | NS  | False | 0   | 0   | 0402 | 15.4.2.7 |
| School Address                                  |               | 8   | XAD | 250 | NS  | False | 0   | 0   |      | 15.4.2.8 |

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Technical Manual section of this supplemental documentation for the Trainee Registration Core Dataset (formerly known as Clinical Trainee Core Dataset) software.

This is a Kernel Installation and Distribution System (KIDS) software release.

|                                                                                                                |                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/022.png) | REF: Installation instructions for Trainee Registration Core Dataset can be found in the description for Kernel Patch XU\*8.0\*512, located on the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM. |

## Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

The following minimum VistA software and patches are required:

<span id="_Toc214422827" class="anchor"></span>Table ‑. VistA patches required prior to installation of Trainee Registration Core Dataset

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>VistA Software and Version</th>
<th>Associated Patch Designation(s)</th>
<th>Brief Patch Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HL7 1.6</td>
<td>HL*1.6*96</td>
<td><p>This patch addresses the following:</p>
<p>This patch is the second phase of upgrading VistA HL7 to HL7 version 2.4. This upgrade is limited to Chapter 15, Personnel Management, and is in support of the Trainee Registration Core Dataset, Kernel Patch XU*8.0*251. A final phase to fully upgrade to version 2.4 will be released in the future.</p></td>
</tr>
<tr class="even">
<td>Kernel 8.0</td>
<td>XU*8.0*134</td>
<td>Name Standardization defines a standard way for names to be entered into the NAME field (#.01) of the NEW PERSON file (#200). This will help in uniquely defining all providers in the file. Another benefit to this project will be to help uniquely identify computer users across various VA facilities.</td>
</tr>
<tr class="odd">
<td>Kernel 8.0</td>
<td>XU*8.0*214</td>
<td>This patch was created to support the BVA (Board of Veterans Appeals) project to allow CPRS to restrict the access of users in the NEW PERSON file (#200) to those patients associated with a specific OE/RR LIST.</td>
</tr>
<tr class="even">
<td>Kernel, Version 8.0</td>
<td>XU*8.0*230</td>
<td>This patch was created to allow CPRS to restrict access of users in the NEW PERSON file (#200) to specific CPRS GUI tabs. It involves adding a new multiple in the NEW PERSON file that points to a new file OR CPRS TABS (#101.13). For each entry in the multiple, an effective date and expiration can be assigned.</td>
</tr>
<tr class="odd">
<td>Kernel, Version 8.0</td>
<td>XU*8.0*247</td>
<td><p>This patch addresses the following:</p>
<ul>
<li><p>This patch removes the message "USER has no ACCESS CODE", which appeared in the "Edit an Existing User" Screen of the XUREACT USER form when a user selected the option: REACTIVATE A USER [XUSERREACT] with a person having an access code.</p></li>
<li><p>The field DOB (Date of Birth) is added on the "Edit an Existing User" Screen of the XUEXISTING USER form.</p></li>
<li><p>This patch also deletes the "AF" cross-ref of New Person file #200 for accounts that may have installed XU*8.0*138 entered as error.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use TaskMan to schedule the XUOAA SEND HL7 MESSAGE option on a daily basis. It was originally exported with Kernel Patch XU\*8.0\*251. This background job initializes the generation and sending of the HL7 PMU. XUOAA SEND HL7 MESSAGE batch message, which builds a batch of messages for transmission to the OAA in support of the Trainee Registration Core Dataset functionality.

|                                                                                                                |                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/023.png) | NOTE: At certain times of the year your facility may process large numbers of trainees. During these times of peak trainee registration activity, you may wish to schedule the XUOAA SEND HL7 MESSAGE option to run more frequently to avoid generating large messages. |

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/024.png) | NOTE: The SCHEDULING RECOMMENDED field (#209) is located in the OPTION file (#19). It must be set to "YES" in order to allow for one-time TaskMan scheduling outside the daily scheduled background job. |

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following two Kernel routines are exported with this software:

<span id="_Toc214422828" class="anchor"></span>Table ‑. Routine list

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUSER2</td>
<td><p>This is an existing Kernel routine, which has been modified to add a new REQ entry point that can be called from the XUEXISTING USER, XUNEW USER, XUREACT USER, and XU-CLINICAL TRAINEE forms. This entry point makes Fields #12.1, 12.2, and 12.3 available or unavailable for editing, and makes those fields along with the other fields being tracked by VHA Office of Academic Affiliations required or not required, depending on whether the person is designated as a registered trainee.</p>
<p>The second line of this routine looks like:</p>
<blockquote>
<p>&lt;tab&gt;;;8.0;KERNEL;267,251,344;Jul 10, 1995</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XUOAAHL7</td>
<td><p>This new Kernel routine iterates through the entries updated in the NEW PERSON file (#200) and sends those entries as batch HL7 messages to the Office of Academic Affiliations (OAA) National Registered Trainee Database.</p>
<p>The second line of this routine looks like:</p>
<blockquote>
<p>&lt;tab&gt;;;8.0;KERNEL;251,324,344;Jul 10, 1995</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XUOAAUTL</td>
<td><p>This new Kernel routine screens the INSTITUTION (#4) file for affiliated VA facilities responsible for administering the registered trainee's training program. Only VAMCs and M&amp;ROCs can be selected.</p>
<p>The second line of this routine looks like:</p>
<blockquote>
<p>8.0;KERNEL;344;Jul 10, 1995</p>
</blockquote></td>
</tr>
</tbody>
</table>

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following two files are exported with this software.

<span id="_Toc214422829" class="anchor"></span>Table ‑. NEW PERSON file (#200)—File and field definitions added

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>VistA File &amp; Number</th>
<th>Global Location</th>
<th>Data w/ File?</th>
<th>Field Information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NEW PERSON (#200)</td>
<td>^VA(200,</td>
<td>No</td>
<td><p>This patch adds the following fields to the NEW PERSON file (#200):</p>
<p><strong>Field Name:</strong> LAST TRAINING MONTH &amp; YEAR</p>
<p><strong>Field Number:</strong> 200,12.3</p>
<p><strong>Type:</strong> FREE TEXT</p>
<p><strong>Description:</strong> This is the MONTH and LAST year the trainee anticipates being in a training program at this VA medical facility.</p>
<p><strong>Field Name:</strong> VHA TRAINING FACILITY</p>
<p><strong>Field Number:</strong> 200, 12.4</p>
<p><strong>Type:</strong> POINTER TO INSTITUTION file (#4)</p>
<p><strong>Field Name:</strong> DATE HL7 TRAINEE RECORD BUILT</p>
<p><strong>Field Number:</strong> 200, 12.5</p>
<p><strong>Type:</strong> DATE</p>
<p><strong>Description:</strong> This is the date that the trainee information was built and sent to the OAA server.</p>
<p><strong>Field Name:</strong> CLINICAL CORE TRAINEE</p>
<p><strong>Field Number:</strong> 200, 12.6</p>
<p><strong>Type:</strong> SET</p>
<ul>
<li><p>"Y" FOR YES</p></li>
<li><p>"N" FOR NO</p></li>
</ul>
<p><strong>Description:</strong> This field designates whether or not the person is a registered trainee.</p>
<p><strong>Field Name:</strong> DATE NO LONGER TRAINEE</p>
<p><strong>Field Number:</strong> 200, 12.7</p>
<p><strong>Type:</strong> DATE</p>
<p><strong>Description:</strong> This is the date when registered trainee is no longer a designated as such.</p>
<p><strong>Field Name:</strong> START OF TRAINING</p>
<p><strong>Field Number:</strong> 200, 12.8</p>
<p><strong>Type:</strong> DATE</p></td>
</tr>
<tr class="even">
<td><p>PROGRAM OF STUDY File (#8932.2)</p>
<p>(Exported with Kernel Patch XU*8.0*251.)</p></td>
<td>^USC(8932.2,</td>
<td>Yes</td>
<td><p>This file was originally exported with Kernel Patch XU*8.0*251. It was created to hold the list of the programs of study that can be associated with a registered trainee. This file is pointed to by the new PROGRAM OF STUDY field (#12.2) in the NEW PERSON file (#200).</p>
<p><strong>Field Name:</strong> NAME</p>
<p><strong>Field Number:</strong> 8932.2,.01</p>
<p><strong>Type:</strong> FREE TEXT</p>
<p><strong>Description:</strong> This is the name of the program of study.</p>
<p>The PROGRAM OF STUDY file is sent with the following data:</p>
<ul>
<li><p>AUDIOLOGY</p></li>
<li><p>CHAPLAINCY</p></li>
<li><p>DENTISTRY</p></li>
<li><p>DIETETICS</p></li>
<li><p>HEALTH INFORMATION</p></li>
<li><p>HEALTH SERVICES RESEARCH &amp; DEVELOPMENT</p></li>
<li><p>IMAGING (RADIOLOGIC/ULTRASOUND TECH, ETC.)</p></li>
<li><p>LABORATORY</p></li>
<li><p>MEDICAL STUDENT</p></li>
<li><p>MEDICAL RESIDENT/FELLOW</p></li>
<li><p>MEDICAL POST-RESIDENCY PHYSICIAN IN VA SPECIAL FELLOWSHIP (AMBULATORY</p></li>
<li><p>CARE, NATIONAL QUALITY SCHOLARS, WOMEN'S HEALTH, ETC.)</p></li>
<li><p>MEDICAL/SURGICAL SUPPORT (RESPIRATORY TECH, BIOMED TECH, ETC.)</p></li>
<li><p>NURSE ANESTHETIST</p></li>
<li><p>NURSING</p></li>
<li><p>OPTOMETRY</p></li>
<li><p>PHARMACY</p></li>
<li><p>PHYSICIAN ASSISTANT</p></li>
<li><p>PODIATRY</p></li>
<li><p>PSYCHOLOGY</p></li>
<li><p>REHABILITATION (OT, PT, KT, ETC.)</p></li>
<li><p>SPEECH - LANGUAGE PATHOLOGY</p></li>
<li><p>SOCIAL WORK</p></li>
<li><p>OTHER</p></li>
</ul></td>
</tr>
</tbody>
</table>

### "ATR" New-Style Cross-reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software added a record-level new-style cross-reference to the NEW PERSON file (#200), which sets an index whenever fields for registered trainees being tracked by the Office of Academic Affiliations are changed.

<span id="_Toc214422830" class="anchor"></span>Table ‑. NEW PERSON file (#200)—New-Style Cross-reference added

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>VistA File &amp; Number</th>
<th>Global Location</th>
<th>Data w/ File?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NEW PERSON (#200)</td>
<td>^VA(200,</td>
<td>No</td>
<td><p>This new-style cross-reference has as cross-reference values all the fields in the NEW PERSON file (#200) that are being tracked by the Office of Academic Affiliations for rollup into a centralized database. When any of the fields are edited, the cross-reference logic will set an index entry that corresponds to the edited record. The index entries will look like this:</p>
<blockquote>
<p>^VA(200,"ATR",ien) = FM internal date</p>
<p>"ATR" stands for "ATrainee."</p>
</blockquote>
<p>None of the field-type cross-reference values are used as subscripts in the index, since we are only interested in recording the IENs of the records that are edited and the date the index entry is set. A separate queuable option will loop through the entries in this index, and send via HL7 messages the registered trainee data of each record to the Office of Academic Affiliations.</p>
<p>The "ATR" cross-reference monitors the following fields in the NEW PERSON file (#200):</p>
<ul>
<li><p>NAME (#.01)</p></li>
<li><p>STREET ADDRESS 1 (#.111)</p></li>
<li><p>STREET ADDRESS 2 (#.112)</p></li>
<li><p>STREET ADDRESS 3 (#.113)</p></li>
<li><p>CITY (#.114)</p></li>
<li><p>STATE (#.115)</p></li>
<li><p>ZIP CODE (#.116)</p></li>
<li><p>SSN (#9)</p></li>
<li><p>EMAIL ADDRESS (#.151)</p></li>
<li><p>CURRENT DEGREE LEVEL (#12.1)</p></li>
<li><p>PROGRAM OF STUDY (#12.2)</p></li>
<li><p>LAST TRAINING MONTH &amp; YEAR (#12.3) SERVICE/SECTION (#29)</p></li>
<li><p>TITLE (#8)</p></li>
<li><p>DOB (#5)</p></li>
<li><p>VHA TRAINING FACILITY (#12.4)</p></li>
<li><p>CLINICAL CORE TRAINEE (#12.6)</p></li>
<li><p>DATE NO LONGER TRAINEE (#12.7)</p></li>
<li><p>START OF TRAINING (#12.8)</p></li>
</ul></td>
</tr>
</tbody>
</table>

## ScreenMan Forms and Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is a list of the modified ScreenMan forms, input templates, and associated options exported with this software.

<span id="_Toc214422831" class="anchor"></span>Table ‑. Modified ScreenMan forms, input templates, and associated options

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>ScreenMan Form</th>
<th>Input Template</th>
<th>Option and Menu Text</th>
<th>VistA File &amp; Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUNEW USER</td>
<td>XUNEW USER</td>
<td>XUSERNEW<br />
Add a New User to the System</td>
<td>NEW PERSON (#200)</td>
<td>The form and input template used by the Add a New User to the System option are modified to include the fields in the NEW PERSON file (#200) identified by OAA as registered trainee data elements. Most of the fields that are added already exist in the NEW PERSON file (#200); Among the new fields added to the NEW PERSON file (#200) by this patch is Program of Study. If the person is assigned a Program of Study, it is assumed that the user is a Registered Trainee. If the person entering the data responds "YES" to the prompt "Is this person an active Trainee?" the VHA TRAINING FACILITY (#12.4) field becomes required.</td>
</tr>
<tr class="even">
<td>XUEXISTING USER</td>
<td>XUEXISTING USER</td>
<td>XUSEREDIT<br />
Edit an Existing User</td>
<td>NEW PERSON (#200)</td>
<td><p>The same changes made to the form and input template used by the Add a New User to the System option are made to the form XUEXISTING USER and input template XUEXISTING USER used by the Edit an Existing User option.</p>
<p>![](xu-8-512-trainee-registration-core-dataset/025.png) <strong>NOTE:</strong> Refer to the option "Add a New User to the System" documented in the first entry of this table, for a description of these changes.</p></td>
</tr>
<tr class="odd">
<td>XUREACT USER</td>
<td>XUREACT USER</td>
<td>XUSERREACTReactivate a User</td>
<td>NEW PERSON (#200)</td>
<td><p>The same changes made to the form and input template used by the Add a New User to the System option are made to the XUREACT USER form and the XUREACT USER input template used by the Reactivate a User option.</p>
<p>![](xu-8-512-trainee-registration-core-dataset/026.png) <strong>NOTE:</strong> Refer to the option "Add a New User to the System" documented in the first entry of this table, for a description of these changes.</p></td>
</tr>
</tbody>
</table>

Following is the modified ScreenMan form and associated updated option exported with this software:

<span id="_Toc214422832" class="anchor"></span>Table ‑. Modified ScreenMan form and associated option

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 16%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>ScreenMan Form</th>
<th>Option and Menu Text</th>
<th>VistA File &amp; Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XU-CLINICAL TRAINEE</td>
<td>XU-CLINICAL TRAINEE EDIT<br />
Edit Trainee Registration Data</td>
<td>NEW PERSON (#200)</td>
<td>This option invokes a form that can be used to edit registered trainee data for users in the NEW PERSON file (#200) that haven't been terminated. This option attaches itself to the User Management [XUSER] menu, but each site can make it available to any user entering this data.</td>
</tr>
</tbody>
</table>

Following is the modified print template and associated option exported with this software:

<span id="_Toc214422833" class="anchor"></span>Table ‑. Modified print template and associated option

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 16%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Print Template</th>
<th>Option and Menu Text</th>
<th>VistA File &amp; Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUSERINQ</td>
<td>XUSERINQ<br />
User Inquiry</td>
<td>NEW PERSON (#200)</td>
<td><p>This print template has been modified to display the following fields from the NEW PERSON file (#200) for registered trainees:</p>
<ul>
<li><p>12.1 CURRENT DEGREE LEVEL</p></li>
<li><p>12.2 PROGRAM OF STUDY</p></li>
<li><p>12.3 LAST TRAINING YEAR</p></li>
<li><p>12.4 VHA TRAINING FACILITY</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE INQUIRY</td>
<td>XU-CLINICAL TRAINEE INQUIRY<br />
Trainee Registration Inquiry</td>
<td>NEW PERSON (#200)</td>
<td>This print template is used by the Trainee Registration Inquiry option to display registered trainee data from the NEW PERSON file (#200).</td>
</tr>
</tbody>
</table>

Following are the new print and sort templates and associated new options are exported with this software:

Table ‑8. New print and sort templates and associated new options

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Print &amp; Sort Templates (same name for both)</th>
<th>Option and Menu Text</th>
<th>VistA File &amp; Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XU-CLINICAL ACTIVE TRAINEE</td>
<td><p>[XU-CLINICAL ACTIVE TRAINEE]</p>
<p>List of Active Registered Trainees</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report listing all active registered trainees.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE LIST</td>
<td><p>[XU-CLINICAL TRAINEE LIST]</p>
<p>List of All Registered Trainees</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report, listing both active and inactive local registered trainees.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL INACTIVE TRAINEE</td>
<td><p>[XU-CLINICAL INACTIVE TRAINEE]</p>
<p>List of Inactive Registered Trainees</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report listing all local inactive registered trainees.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE DB COUNT</td>
<td><p>[XU-CLINICAL TRAINEE DB COUNT]</p>
<p>Total Count of Registered Trainees</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report listing the total number of local registered trainees entered into the sites' New Person file (#200).</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE TRANSA</td>
<td><p>[XU-CLINICAL TRAINEE TRANSA]</p>
<p>Trainee Transmission Report by Date</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report listing all local registered trainee records sent to the Office of Academic Affiliations (OAA) within a defined date range.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE TRANSC</td>
<td><p>[XU-CLINICAL TRAINEE TRANSC]</p>
<p>Trainee Transmission Report by Range</p></td>
<td>NEW PERSON (#200)</td>
<td>Produces a report showing the total count(s) for local registered trainee records sent to the OAA within a defined period.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE TRANSB</td>
<td><p>[XU-CLINICAL TRAINEE TRANSB]</p>
<p>Trainee Transmission Report Selectable Items</p></td>
<td>NEW PERSON (#200)</td>
<td><p>Produces a report of all local trainee records sent to the Office of Academic Affiliations (OAA) defined by the following two ranges:</p>
<ul>
<li><p>date</p></li>
<li><p>VHA training facility</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Kernel Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trainee Registration Core Dataset software exports the following new Kernel options.

|                                                                                                                |                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/027.png) | NOTE: There are no ScreenMan Forms associated with these options. |

<span id="_Toc214422835" class="anchor"></span>Table ‑. New Kernel options

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[XU-CLINICAL TRAINEE REPORTS]</p>
<p>Trainee Reports Menu</p></td>
<td><p>This menu holds the following menu options:</p>
<ul>
<li><p>Local Trainee Registration Reports ... [XU-CLINICAL LOCAL REPORTS]</p></li>
<li><p>Trainee Transmission Reports to OAA ... [XU-CLINICAL TRANS REPORTS]</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL LOCAL REPORTS]</p>
<p>Local Trainee Registration Reports</p></td>
<td><p>This menu holds the following options:</p>
<ul>
<li><p>List of Active Registered Trainees [XU-CLINICAL ACTIVE TRAINEE]</p></li>
<li><p>List of All Registered Trainees [XU-CLINICAL TRAINEE LIST]</p></li>
<li><p>List of Inactive Registered Trainees [XU-CLINICAL INACTIVE TRAINEE]</p></li>
<li><p>Total Count of Registered Trainees [XU-CLINICAL TRAINEE DB COUNT]</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL ACTIVE TRAINEE]</p>
<p>List of Active Registered Trainees</p></td>
<td>Produces a report listing all active registered trainees.</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE LIST]</p>
<p>List of All Registered Trainees</p></td>
<td>Produces a report, listing both active and inactive local registered trainees.</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL INACTIVE TRAINEE]</p>
<p>List of Inactive Registered Trainees</p></td>
<td>Produces a report listing all local inactive registered trainees.</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE DB COUNT]</p>
<p>Total Count of Registered Trainees</p></td>
<td>Produces a report listing the total number of local registered trainees entered into the sites' New Person file (#200).</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL TRANS REPORTS]</p>
<p>Trainee Transmission Reports to OAA</p></td>
<td><p>This menu holds the following options:</p>
<ul>
<li><p>Trainee Transmission Report by Date [XU-CLINICAL TRAINEE TRANSA]</p></li>
<li><p>Trainee Transmission Report by Range [XU-CLINICAL TRAINEE TRANSC]</p></li>
<li><p>Trainee Transmission Report Selectable Items [XU-CLINICAL TRAINEE TRANSB]</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE TRANSA]</p>
<p>Trainee Transmission Report by Date</p></td>
<td>Produces a report listing all local registered trainee records sent to the Office of Academic Affiliations (OAA) within a defined date range.</td>
</tr>
<tr class="odd">
<td><p>[XU-CLINICAL TRAINEE TRANSC]</p>
<p>Trainee Transmission Report by Range</p></td>
<td>Produces a report showing the total count(s) for local registered trainee records sent to the OAA within a defined period.</td>
</tr>
<tr class="even">
<td><p>[XU-CLINICAL TRAINEE TRANSB]</p>
<p>Trainee Transmission Report Selectable Items</p></td>
<td><p>Produces a report of all local trainee records sent to the Office of Academic Affiliations (OAA) defined by the following two ranges:</p>
<ul>
<li><p>date</p></li>
<li><p>VHA training facility</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Modified Kernel Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software exports the following modified Kernel options and ScreenMan form:

<span id="_Toc214422836" class="anchor"></span>Table ‑. Modified Kernel option and ScreenMan form

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 26%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>ScreenMan Form</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XU-CLINICAL TRAINEE MENU</p>
<p>OAA Trainee Registration Menu</p></td>
<td>None</td>
<td><p>This menu holds the Edit Trainee Registration Data and Inquiry options:</p>
<ul>
<li><p>Edit Trainee Registration Data<br />
[XU-CLINICAL TRAINEE EDIT]</p></li>
<li><p>Trainee Registration Inquiry<br />
[XU-CLINICAL TRAINEE INQUIRY]</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XU-CLINICAL TRAINEE EDIT</p>
<p>Edit Trainee Registration Data</p></td>
<td>XU-CLINICAL TRAINEE</td>
<td>This option is used to edit the Trainee Registration Core Dataset. Users that have been terminated can't be edited.</td>
</tr>
<tr class="odd">
<td><p>XU-CLINICAL TRAINEE INQUIRY</p>
<p>Trainee Registration Inquiry</p></td>
<td>None</td>
<td>Displays the various attributes of registered trainees.</td>
</tr>
<tr class="even">
<td><p>XUOAA SEND HL7 MESSAGE</p>
<p>Send HL7 PMU message</p></td>
<td>None</td>
<td><p>Initiates the generation of batch HL7 messages to the Office of Academic Affiliations (OAA) if entries (fields) for Registered Trainees have been updated in the NEW PERSON file (#200). This option should be scheduled using TaskMan on a daily basis.</p>
<p>![](xu-8-512-trainee-registration-core-dataset/028.png) <strong>NOTE:</strong> The SCHEDULING RECOMMENDED field (#209) is located in the OPTION file (#19). It must be set to "YES" in order to allow for one-time TaskMan scheduling outside the daily scheduled background job.</p></td>
</tr>
</tbody>
</table>

### Existing Kernel Options Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The input and print templates and the ScreenMan forms called by the Kernel options listed below have been modified, and are exported with this software; however, the options themselves are *not* exported with the patch:

- Add a New User to the System
- Edit an Existing User
- Reactivate a User
- User Inquiry

Table 5‑10 lists the Kernel options on the left with the modified ScreenMan forms and input templates on the right:

<span id="_Ref107380673" class="anchor"></span>Table ‑. Kernel options with associated ScreenMan forms and input templates

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 33%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>ScreenMan Form</th>
<th>Input Template</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XUSERNEW</p>
<p>Add a New User to the System</p></td>
<td>XUNEW USER</td>
<td>XUNEW USER</td>
</tr>
<tr class="even">
<td><p>XUSEREDIT</p>
<p>Edit an Existing User</p></td>
<td>XUEXISTING USER</td>
<td>XUEXISTING USER</td>
</tr>
<tr class="odd">
<td><p>XUSERREACT</p>
<p>Reactivate a User</p></td>
<td>XUREACT USER</td>
<td>XUREACT USER</td>
</tr>
</tbody>
</table>

Table 5‑11 lists the Kernel option on the left with the modified print template on the right:

<span id="_Ref22706794" class="anchor"></span>Table ‑. Kernel option with associated print template

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Option and Menu Text</th>
<th>Print Template</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XUSERINQ</p>
<p>User Inquiry</p></td>
<td>XUSERINQ</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/029.png) | REF: For information on the modifications to the input and print templates and the ScreenMan forms called by these options, see the section "ScreenMan Forms and Templates" in this supplement. |

### Menu Diagram—OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc214422839" class="anchor"></span>Figure ‑. Menu Diagram—OAA Trainee Registration Menu \[XU-CLINICAL TRAINEE MENU\]

OAA Trainee Registration Menu (XU-CLINICAL TRAINEE MENU)

\|

\|

--------------------------------------------------------E Edit Trainee

Registration

Data

\[XU-CLINICAL

TRAINEE EDIT\]

\*\*ENTRY ACTION:

S

DIC="^VA(200,",D

IC(0)="AEMQ",DIC("S")=

"I

\$S(\$P(^(0),U,11)

:\$P(^(0),U,11)'\<\$\$FMAD

D^XLFDT(DT,""-1096""),

1:1)"

D ^DIC K DIC

Q:Y=-1 S

DA=+Y,DR="\[XU-CL

INICAL

TRAINEE\]",DIE="^

VA(200," D

XUDIE^XUS5 K

D0,DA,DIE,DR

--------------------------------------------------------I Trainee

Registration

Inquiry

\[XU-CLINICAL

TRAINEE INQUIRY\]

----R Trainee Reports --------- Local Trainee ----------- List of Active

Menu Registration Registered

\[XU-CLINICAL Reports Trainees

TRAINEE REPORTS\] \[XU-CLINICAL \[XU-CLINICAL

\| LOCAL REPORTS\] ACTIVE TRAINEE\]

\| \|

\| \|-------------------- List of All

\| \| Registered

\| \| Trainees

\| \| \[XU-CLINICAL

\| \| TRAINEE LIST\]

\| \|

\| \|-------------------- List of Inactive

\| \| Registered

\| \| Trainees

\| \| \[XU-CLINICAL

\| \| INACTIVE

\| \| TRAINEE\]

\| \|

\| \|-------------------- Total Count of

\| Registered

\| Trainees

\| \[XU-CLINICAL

\| TRAINEE DB

\| COUNT\]

\|

\|

\|-------------------- Trainee ----------------- Trainee

Transmission Transmission

Reports to OAA Report by Date

\[XU-CLINICAL \[XU-CLINICAL

TRANS REPORTS\] TRAINEE TRANSA\]

\|

\|-------------------- Trainee

\| Transmission

\| Report by Range

\| \[XU-CLINICAL

\| TRAINEE TRANSC\]

\|

\|-------------------- Trainee

Transmission

Report

Selectable Items

\[XU-CLINICAL

TRAINEE TRANSB\]

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no application-specific archiving or purging procedures or recommendations for the Trainee Registration Core Dataset software.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines exported with this software.

## External Interfaces (HL7 Components)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software makes use of HL7 messaging to identify and share VistA information with the Trainee Registration Core Dataset project.

|                                                                                                                |                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/030.png) | REF: For information on message construction for HL7 messaging for the Trainee Registration Core Dataset project, see Chapter 4, "HL7 Interface Specifications," in this supplement. |

Listed as follows are the HL7 Application Parameters, HL Lower Level Protocol Parameters, and HL7 Protocols used for HL7 messaging.

## Scheduled Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: XUOAA SEND HL7 MESSAGE MENU TEXT: Send HL7 PMU message

TYPE: run routine CREATOR: KRNUSER,TWO

PACKAGE: KERNEL

DESCRIPTION: This option is used to send an HL7 PMU message to the Office of

Academic Affiliations (OAA).

ROUTINE: OAA^XUOAAHL7

UPPERCASE MENU TEXT: SEND HL7 PMU MESSAGE

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: XUOAA PMU ACTIVE/INACTIVE: ACTIVE

COUNTRY CODE: USA

NAME: XUOAA ACK ACTIVE/INACTIVE: ACTIVE

COUNTRY CODE: USA

## HL7 Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: XUOAA PMU TYPE: event driver

CREATOR: KRNUSER,TWO

DESCRIPTION: This HL7 event protocol is one of two protocols used to generate

Update Personnel Record (PMU) messages. This particular protocol represents the

sending system.

SENDING APPLICATION: XUOAA PMU TRANSACTION MESSAGE TYPE: PMU

EVENT TYPE: B02 VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: Q

SUBSCRIBERS: XUOAA MFK

NAME: XUOAA MFK TYPE: subscriber

CREATOR: KRNUSER,TWO

DESCRIPTION: This HL7 event protocol is one of two protocols used to generate

Update Personnel Record (PMU) messages. This particular protocol represents the

receiving system.

RECEIVING APPLICATION: XUOAA MFK EVENT TYPE: B02

LOGICAL LINK: XUOAA RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: Q

## HL7 Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUOAA HL7 Logical Link shown in Figure 5‑2 implements an HL7 Lower Level Protocol named (MailMan) as an email exchange.

<span id="_Ref251063443" class="anchor"></span>Figure ‑. XUOAA HL7 logical link

NODE: XUOAA LLP TYPE: MAILMAN

AUTOSTART: Enabled QUEUE SIZE: 10

MAIL GROUP: XUOAA CLIN TRAINEE

|                                                                                                                |                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/031.png) | NOTE: Make sure the AUTOSTART field is set to "enabled" in the HL7 Logical Link XUOAA. Only HL7 logical links with AUTOSTART fields set to "enabled" are automatically started again after the system has been shutdown. |

## Mail Group: XUOAA CLIN TRAINEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This MailMan mail group was originally exported with Kernel Patch XU\*8.0\*251.

<span id="_Toc214422840" class="anchor"></span>Table ‑. Mail group for sending HL7 PMU messages to support Registered Trainee Data Set functionality

| Mail Group Name    | Description                                                                                                                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUOAA CLIN TRAINEE | This is the mail group used by the HL7 MailMan logical link for sending out the HL7 PMU messages to support the Office of Academic Affiliations' Trainee Registration Core Dataset Set project. REMOTE MEMBER: REDACTED |

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

|                                                                                                                |                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/032.png) | REF: For more information on the minimum VistA software and patches that are required by this patch see the "Software Dependencies" portion of the "Technical Manual Information" section of this supplement. |

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New menus and options, listed below, have been created and are exported with this software. Print and sort templates have also been created associated with these options:

- Trainee Reports Menu ... \[XU-CLINICAL TRAINEE REPORTS\]
- Local Trainee Registration Reports ... \[XU-CLINICAL LOCAL REPORTS\]
- List of Active Registered Trainees \[XU-CLINICAL ACTIVE TRAINEE\]
- List of All Registered Trainees \[XU-CLINICAL TRAINEE LIST\]
- List of Inactive Registered Trainees \[XU-CLINICAL INACTIVE TRAINEE\]
- Total Count of Registered Trainees \[XU-CLINICAL TRAINEE DB COUNT\]
- Trainee Transmission Reports to OAA ... \[XU-CLINICAL TRANS REPORTS\]
- Trainee Transmission Report by Date \[XU-CLINICAL TRAINEE TRANSA\]
- Trainee Transmission Report by Range \[XU-CLINICAL TRAINEE TRANSC\]
- Trainee Transmission Report Selectable Items \[XU-CLINICAL TRAINEE TRANSB\]

The print and sort templates have been created to support the Kernel options have been modified, and they are also exported with this release:

- Add a New User to the System \[XUNEW USER\]
- Edit an Existing User \[XUSEREDIT\]
- Reactivate a User \[XUSERREACT\]
- User Inquiry \[XUSERINQ\]

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trainee Registration Core Dataset patch uses the XU namespace, which is a Kernel namespace.

## File Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file numbers and global locations used by this software are listed as follows:

<span id="_Toc214422841" class="anchor"></span>Table ‑. File list

| File \# | Global                                                  |
|---------|---------------------------------------------------------|
| 200     | ^VA(200,                                                |
| 8932.2  | ^USC(8932.2, (Exported with Kernel Patch XU\*8.0\*251.) |

|                                                                                                                |                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/033.png) | NOTE: The CURRENT DEGREE LEVEL field (#12.1) points to the HL7 DEGREE file (#771.9) that complies with the HL7 Standard Table \#360 for Degree. This HL7 file is used by this software and was exported with Patch HL\*1.6\*96. |

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software contains no software-wide variables.

## Software Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This MailMan mail group was originally exported with Kernel Patch XU\*8.0\*251.

<span id="_Toc214422842" class="anchor"></span>Table ‑. Mail group XUOAA CLIN TRAINEE

| Mail Group Name    | Description                                                                                                                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUOAA CLIN TRAINEE | This is the mail group used by the HL7 MailMan logical link for sending out the HL7 PMU messages to support the Office of Academic Affiliations' Trainee Registration Core Dataset Set project. REMOTE MEMBER: REDACTED |

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software uses HL7 to send batch messages to the Office of Academic Affiliations (OAA) designated as a Microsoft Exchange address.

### Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific archiving procedures or recommendations for this software.

### Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized (*not* VA produced) products (hardware and/or software) embedded within or required by this software.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures used in this software.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no options of particular interest to Information Security Officers (ISOs) in this software.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUSHOWSSN security key allows users who hold it authority to view Registered Trainee Social Security Numbers (SSNs) in the option Edit Trainee Registration Data (XU-CLINICAL TRAINEE EDIT). If the SSN field is defined, users who are not assigned the XUSHOWSSN security key will only see the last four digits of the Social Security Number (SSN) displayed (e.g., SSN: \*\*\*\*\*1234). If no SSN has been entered, only the following label is displayed: "SSN:".

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc477786052" class="anchor"></span>Table ‑. File Security

| File \# | File Name        | DD    | RD    | WR    | DEL   | LAYGO | AUDIT |
|---------|------------------|-------|-------|-------|-------|-------|-------|
| 200     | NEW PERSON       | ^ | ^ | ^ |       | ^ |       |
| 8932.2  | PROGRAM OF STUDY | @ |       | ^ | @ | ^ | @ |

|                                                                                                                |                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/034.png) | NOTE: The PROGRAM OF STUDY file (#8932.2) was exported with Kernel Patch XU\*8.0\*251. |

|                                                                                                                |                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-512-trainee-registration-core-dataset/035.png) | NOTE: The CURRENT DEGREE LEVEL field (#12.1) points to the HL7 DEGREE file (#771.9) that complies with the HL7 Standard Table \#360 for Degree. This HL7 file is used by this software and was exported with Patch HL\*1.6\*96. |

<span id="_Toc475930759" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ACCESS CODE</td>
<td>A code that, along with the Verify code, allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than 6 and less than 20 characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. It is used by the Kernel's Sign-on/Security system to identify the user (see Verify Code).</td>
</tr>
<tr class="even">
<td>ALERTS</td>
<td>Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient’s clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</td>
</tr>
<tr class="odd">
<td>ANSI MUMPS</td>
<td>The MUMPS programming language is a standard recognized by the <strong>A</strong>merican <strong>N</strong>ational <strong>S</strong>tandard <strong>I</strong>nstitute (ANSI). MUMPS stands for <strong>M</strong>assachusetts <strong>U</strong>tility <strong>M</strong>ulti-<strong>p</strong>rogramming <strong>S</strong>ystem and is abbreviated as M.</td>
</tr>
<tr class="even">
<td>API</td>
<td><p><strong>A</strong>pplication <strong>P</strong>rogram <strong>I</strong>nterface. VistA Application Program Interfaces (APIs) are units of programming code provided by a custodial development domain to permit developers outside the custodial domain to accomplish a specified purpose. In some programming languages, APIs are called (sub)routines. APIs in VistA may be defined as extrinsic functions, extrinsic special variables, or label references to routines.<br />
<br />
VistA APIs fall into the following three categories:</p>
<ul>
<li><p>The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.</p></li>
<li><p>The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.</p></li>
<li><p>The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.</p></li>
</ul>
<p>These IAs are granted for special cases, transitional problems between versions, and release coordination.</p></td>
</tr>
<tr class="odd">
<td>APPLICATION PACKAGE</td>
<td>Software and documentation that support the automation of a service, such as Laboratory or Pharmacy within VA medical centers. The Kernel application package is like an operating system relative to other VistA applications.</td>
</tr>
<tr class="even">
<td>CALLABLE ENTRY POINT</td>
<td>An authorized programmer call that may be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</td>
</tr>
<tr class="odd">
<td>CARET</td>
<td>A symbol expressed as up caret ("<strong>^</strong>"), left caret ("<strong>&lt;</strong>"), or right caret ("<strong>&gt;</strong>"). In many M systems, a right caret is used as a system prompt and an up caret as an exiting tool from an option. Also known as the up-arrow symbol or shift–6 key.</td>
</tr>
<tr class="even">
<td>CLIENT</td>
<td><p>A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. This term is typically used in an object-oriented environment, where a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</p>
<p>With respect to the M-to-M Broker software, client refers to the "requesting server" that is able to connect to a "receiving server," where both servers reside in VistA on the same or on different VistA M systems.</p></td>
</tr>
<tr class="odd">
<td>COMPONENT</td>
<td>An object-oriented term used to describe the building blocks of GUI applications. A software object that contains data and code. A component may or may not be visible. These components interact with other components on a form to create the GUI user application interface.</td>
</tr>
<tr class="even">
<td>CONTROLLED SUBSCRIPTION INTEGRATION AGREEMENT</td>
<td>This applies where the IA describes attributes/functions that must be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package’s features. For the IA to be approved, the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="odd">
<td>COTS</td>
<td><strong>C</strong>ommercial <strong>O</strong>ff-<strong>t</strong>he-<strong>S</strong>helf. COTS refers to software packages that can be purchased by the public and used in support of VistA.</td>
</tr>
<tr class="even">
<td>DATA DICTIONARY</td>
<td><p>The Data Dictionary is a global containing a description of the kind of data that is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td><strong>D</strong>ata<strong>b</strong>ase <strong>I</strong>ntegration <strong>A</strong>greement, a formal understanding between two or more application packages that describes how data is shared or how packages interact. The DBA maintains a list of DBIAs between package developers, allowing the use of internal entry points or other package-specific features that are not available to the general programming public.</td>
</tr>
<tr class="even">
<td>DDP</td>
<td><strong>D</strong>istributed <strong>D</strong>ata <strong>P</strong>rocessing.</td>
</tr>
<tr class="odd">
<td>DEFAULT</td>
<td>A response the computer considers the most probable answer to the prompt being given. In the roll-and-scroll mode of VistA, the default value is identified by double forward slash marks (<strong>//</strong>) immediately following it. In a GUI-based application the default may be a highlighted button or text. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the <strong>Enter</strong> key. To change the default answer, type in your response.</td>
</tr>
<tr class="even">
<td>DICOM</td>
<td>Digital Imaging and Communication in Medicine</td>
</tr>
<tr class="odd">
<td>DIRECT MODE UTILITY</td>
<td>A programmer call that is made when working in direct programmer mode. A direct mode utility is entered at the M prompt (e.g., &gt;<strong>D ^XUP</strong>). Calls that are documented as direct mode utilities <em>cannot</em> be used in application package code.</td>
</tr>
<tr class="even">
<td>DLL</td>
<td><p><strong>D</strong>ynamic <strong>L</strong>ink <strong>L</strong>ibrary. A DLL allows executable routines to be stored separately as files with a DLL extension. These routines are only loaded when a program calls for them. DLLs provide several advantages:</p>
<ul>
<li><p>DLLs help save on computer memory, since memory is only consumed when a DLL is loaded. They also save disk space. With static libraries, your application absorbs all the library code into your application so the size of your application is greater. Other applications using the same library will also carry this code around. With the DLL, you don’t carry the code itself, you have a pointer to the common library. All applications using it will then share one image.</p></li>
<li><p>DLLs ease maintenance tasks. Because the DLL is a separate file, any modifications made to the DLL will not affect the operation of the calling program or any other DLL.</p></li>
<li><p>DLLs help avoid redundant routines. They provide generic functions that can be utilized by a variety of programs.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>ERROR TRAP</td>
<td>A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</td>
</tr>
<tr class="even">
<td>FORUM</td>
<td>The central e-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the Washington, DC CIO Field Office (162-2).</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser <strong>I</strong>nterface. A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.</td>
</tr>
<tr class="even">
<td>HIS</td>
<td><strong>H</strong>ospital <strong>I</strong>nformation <strong>S</strong>ystem</td>
</tr>
<tr class="odd">
<td>HOST</td>
<td>The term Host is used interchangeably with the term Server.</td>
</tr>
<tr class="even">
<td>ICON</td>
<td>A picture or symbol that graphically represents an object or a concept.</td>
</tr>
<tr class="odd">
<td><p>INTEGRATION AGREEMENTS (IA)</p>
<p>(Formerly known as DATABASE INTEGRATION AGREEMENTS [DBIA])</p></td>
<td>Integration Agreements define an agreement between two or more VistA packages to allow access to one development domain by another. Any package developed for use in the VistA environment is required to adhere to this standard; as such it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. All IAs are recorded in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Technical Services’ Web page.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td><strong>I</strong>nformation <strong>R</strong>esource <strong>M</strong>anagement. A service at VA medical centers responsible for computer management and system security.</td>
</tr>
<tr class="odd">
<td>KERNEL</td>
<td><p>A set of VistA software routines that function as an intermediary between the host operating system and the VistA application packages (e.g., Laboratory, Pharmacy, IFCAP, etc.). Kernel provides a standard and consistent user and program interface between application packages and the underlying M implementation. (VA FileMan and MailMan are self-contained to the extent that they can standalone as verified packages.) Some of Kernel's components are listed below along with their associated namespace assignments:</p>
<ul>
<li><blockquote>
<p>KIDS XPD</p>
</blockquote></li>
<li><blockquote>
<p>Menu Management XQ</p>
</blockquote></li>
<li><blockquote>
<p>Tools XT</p>
</blockquote></li>
<li><blockquote>
<p>Sign-on/Security XU</p>
</blockquote></li>
<li><blockquote>
<p>Device Handling ZIS</p>
</blockquote></li>
<li><blockquote>
<p>Task Management ZTM</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>MENU MANAGER</td>
<td>The Kernel module that controls the presentation of user activities such as menu choices or options. Information about each user’s menu choices is stored in the Compiled Menu System, the ^XUTL global, for easy and efficient access.</td>
</tr>
<tr class="odd">
<td>MULTIPLE</td>
<td>A multiple-valued field; a subfile. In many respects, a multiple is structured like a file.</td>
</tr>
<tr class="even">
<td>MUMPS (ANSI STANDARD)</td>
<td>A programming language recognized by the <strong>A</strong>merican <strong>N</strong>ational <strong>S</strong>tandards <strong>I</strong>nstitute (ANSI). The acronym MUMPS stands for <strong>M</strong>assachusetts General Hospital <strong>U</strong>tility <strong>M</strong>ulti-<strong>p</strong>rogramming <strong>S</strong>ystem and is abbreviated as M.</td>
</tr>
<tr class="odd">
<td>NAMESPACING</td>
<td>A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="even">
<td>NODE</td>
<td>In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name.</td>
</tr>
<tr class="odd">
<td>NT</td>
<td><strong>N</strong>ew <strong>T</strong>echnology.</td>
</tr>
<tr class="even">
<td>OAA</td>
<td><strong>O</strong>ffice of <strong>A</strong>cademic <strong>A</strong>ffiliations.</td>
</tr>
<tr class="odd">
<td>OIFO</td>
<td><strong>O</strong>ffice of <strong>I</strong>nformation <strong>F</strong>ield <strong>O</strong>ffice.</td>
</tr>
<tr class="even">
<td>OPTION</td>
<td>As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. In VistA, an entry in the OPTION file (#19). Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="odd">
<td>PRIVATE INTEGRATION AGREEMENT</td>
<td>Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package’s features. An example would be where one package distributes a patch from another package to ensure smooth installation.</td>
</tr>
<tr class="even">
<td>PROMPT</td>
<td>The computer interacts with the user by issuing questions called <em>prompts</em>, to which the user returns a response.</td>
</tr>
<tr class="odd">
<td>REMOTE PROCEDURE CALL (RPC)</td>
<td>A remote procedure call (RPC) is essentially M code that may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="even">
<td>ROUTINE</td>
<td>A program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines that are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="odd">
<td>SECURITY KEY</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td>SERVER</td>
<td><p>With respect to the M-to-M Broker software, server refers to the "receiving server" that sends the results in a message back to the "requesting server," where both servers reside in VistA on the same or on different VistA M systems.</p>
<p>The server is where VistA M-based data and Business Rules reside, making these resources available to the requesting server.</p>
<p>When the requesting server is receiving the results, it is referred to as the "server."</p></td>
</tr>
<tr class="odd">
<td>SIGN-ON/SECURITY</td>
<td>The Kernel module that regulates access to the menu system. It performs a number of checks to determine whether access can be permitted at a particular time. A log of signons is maintained.</td>
</tr>
<tr class="even">
<td>SUBSCRIPT</td>
<td>A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</td>
</tr>
<tr class="odd">
<td>SUPPORTED REFERENCE INTEGRATION AGREEMENT</td>
<td>This applies where any VistA application may use the attributes/functions defined by the IA (these are also called "<strong>Public</strong>"). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td><strong>T</strong>ransmission <strong>C</strong>ontrol <strong>P</strong>rotocol/<strong>I</strong>nternet <strong>P</strong>rotocol.</td>
</tr>
<tr class="odd">
<td>UCI</td>
<td><strong>U</strong>ser <strong>C</strong>lass <strong>I</strong>dentification, a computing area. The MGR UCI is typically the Manager's account, while VAH or ROU may be Production accounts.</td>
</tr>
<tr class="even">
<td>USER ACCESS</td>
<td><p>This term is used to refer to a limited level of access to a computer system that is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any of VistA's options can be locked with a security key (e.g., XUPROGMODE, which means that invoking that option requires programmer access).</p>
<p>The user's access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="odd">
<td>USER INTERFACE</td>
<td>The way the package is presented to the user, such as Graphical User Interfaces that display option prompts, help messages, and menu choices. A standard user interface can be achieved by using Borland's Delphi Graphical User Interface to display the various menu option choices, commands, etc.</td>
</tr>
<tr class="even">
<td>VA</td>
<td><strong>V</strong>eterans <strong>A</strong>dministration.</td>
</tr>
<tr class="odd">
<td>VERIFY CODE</td>
<td>The Kernel's Sign-on/Security system uses the Verify code to validate the user's identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters: letters (lower- and uppercase), numbers, and, characters that are neither letters nor numbers (e.g., "<strong>#</strong>", "<strong>@</strong>" or "<strong>$</strong>"). If entered incorrectly, the system does not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="even">
<td>VHA</td>
<td><strong>V</strong>eterans <strong>H</strong>ealth <strong>A</strong>dministration.</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td><strong>V</strong>eterans <strong>I</strong>ntegrated <strong>S</strong>ervice <strong>N</strong>etwork.</td>
</tr>
<tr class="even">
<td>VistA</td>
<td><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture. VistA includes the VA's application software (i.e., Microsoft Windows-based and locally developed applications, roll-and-scroll, and interfaces such as software links to commercial packages). In addition, it encompasses the VA's uses of new automated technology including the clinical workstations. VistA encompasses the rich automated environment already present at local VA medical facilities.</td>
</tr>
<tr class="odd">
<td>WINDOW</td>
<td>An object on the screen (dialog) that presents information such as a document or message.</td>
</tr>
<tr class="even">
<td>XML</td>
<td>E<strong>X</strong>tensible <strong>M</strong>arkup <strong>L</strong>anguage. The universal format for structured documents and data on the Web.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-512-trainee-registration-core-dataset/036.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the Glossary Intranet Website:</p>
<p>http://vista.med.va.gov/iss/glossary.asp</p>
<p>For a comprehensive list of acronyms, please visit the Acronyms Intranet Website :</p>
<p>http://vista/med/va/gov/iss/acronyms/index.asp</p></td>
</tr>
</tbody>
</table>

<span id="_Toc475930767" class="anchor"></span>Index

A

Academic Affiliations Needs, 2-1

Acronyms

Website, Glossary, 7

Add a New User to the System, 3-1, 5-8, 5-14

Adobe Website, xiv

Archiving, 5-16, 5-20

Assumptions

About the Reader, xiii

HL7 Interface Specifications, 4-1

ATR New-Style Cross-reference, 5-6

AUDIOLOGY, 5-5

AUTOSTART Field, 5-18

B

Background

Job

XUOAA SEND HL7 MESSAGE, 5-2

Project, 1-2

background job, 5-2

Batch

Acknowledgments, 4-2

Header Segment—BHS, 4-6

Messages, 4-2

HL7 PMU. XUOAA SEND HL7 MESSAGE, 5-2

Trailer Segment—BTS, 4-7

C

Callable Routines, 5-16

CARE, NATIONAL QUALITY SCHOLARS, WOMEN'S HEALTH, ETC.), 5-5

CHAPLAINCY, 5-5

CITY Field (#.114), 3-9

CLINICAL CORE TRAINEE Field (#12.6), 2-1, 5-4

Contents, v

Control Segments

BHS—Batch Header Segment, 4-6

BTS—Batch Trailer Segment, 4-7

EDU—Educational Detail Segment, 4-17

EVN—Event Type Segment, 4-9

Legend, 4-5

MSH—Message Header Segment, 4-7

ORG—Practitioner Organization Unit Segment, 4-15

PRA—Practitioner Detail Segment, 4-14

STF—Staff Identification Segment, 4-9

Cross-references

"ATR" New-Style, 5-6

CURRENT DEGREE LEVEL Field (#12.1), 2-1, 3-4, 3-8, 3-11, 5-3, 5-20, 5-21

Current Program of Study, 3-9

D

Data Capture and Transmission, 4-1

Data Dictionary

HL7 DEGREE File (#771.9), 5-20

NEW PERSON File (#200), 5-19

PROGRAM OF STUDY File (#8932.2), 5-19

DATE HL7 TRAINEE RECORD BUILT Field (#12.5), 2-1, 5-4

DATE NO LONGER TRAINEE Field (#12.7), 2-1, 5-4

DEGREE Field (#10.6), 3-8, 3-9

DENTISTRY, 5-5

DIETETICS, 5-5

Disclaimers, xi

Displaying VHA Registered Trainee Data, 3-1

DOB Field (#5), 3-9

Documentation

History, iii

Symbols, xii

Documentation Conventions, xii

E

Edit an Existing User, 3-1, 3-4, 3-9, 5-8, 5-14

Edit trainee registration data

Current Program of Study, 3-9

Last Training Year, 3-9

Edit Trainee Registration Data, 3-6, 3-8, 5-9, 5-12

Target Degree Lvl, 3-9

Usage, 3-7

Editing and Displaying VHA Registered Trainee Data

Assign Registered Trainee Options to User(s), 3-5

Editing Registered Trainee Data for New Person File Entries, 3-2

input templates, 3-1

NEW PERSON File Entries, 3-2

ScreenMan Form Differ from its Corresponding Input Template?, 3-1

ScreenMan Forms, 3-1

Editing VHA Registered Trainee Data, 3-1

Educational Detail Segment—EDU, 4-17

Electronic Signatures, 5-20

Event Type Segment—EVN, 4-9

External

Interfaces

HL7 Components, 5-16

Relations, 5-18

F

Fields

AUTOSTART, 5-18

CITY (#.114), 3-9

CLINICAL CORE TRAINEE (#12.6), 2-1, 5-4

CURRENT DEGREE LEVEL (#12.1), 2-1, 3-4, 3-8, 3-11, 5-3, 5-20, 5-21

DATE HL7 TRAINEE RECORD BUILT (12.5, 2-1

DATE HL7 TRAINEE RECORD BUILT (12.5), 5-4

DATE NO LONGER TRAINEE (#12.7, 2-1, 5-4

DEGREE (#10.6), 3-8, 3-9

DOB (#5), 3-9

LAST TRAINING MONTH & YEAR (#12.3), 2-1, 3-4, 3-8, 3-11, 5-3

LAST TRAINING YEAR (#12.3), 5-3

NAME (#.01), 5-1

PROGRAM OF STUDY (#12.2), 2-1, 3-4, 3-8, 3-11, 5-3, 5-4

SCHEDULING RECOMMENDED (#209), 5-2, 5-13

SERVICE/SECTION (#29), 3-8, 3-9

START OF TRAINING (#12.8, 2-1, 3-4, 3-8, 5-4

STATE (#.115), 3-9

STREET ADDRESS 1 (#.111), 3-9

STREET ADDRESS 2 (#.112), 3-9

STREET ADDRESS 3 (#.113), 3-9

TITLE (#8), 3-8, 3-9

VHA TRAINING FACILITY (#12.4), 2-1, 3-4, 3-8, 3-9, 3-11, 5-4, 5-8

ZIP CODE (#.116), 3-9

Figures, ix

Files

HL7 DEGREE (#771.9), 5-21

Data Dictionary, 5-20

List, 5-3

NEW PERSON (#200), 1-1, 1-2, 2-1, 2-2, 3-5, 3-8, 4-2, 5-1, 5-4, 5-6, 5-8, 5-9, 5-12, 5-19

Numbers, 5-19

OPTION (#19), 5-2, 5-13

PROGRAM OF STUDY (#8932.2), 1-1, 5-4, 5-19

Security, 5-21

G

Glossary, 1

Website, Glossary, 7

H

HEALTH INFORMATION, 5-5

HEALTH SERVICES RESEARCH & DEVELOPMENT, 5-5

Help at Prompts, xiii

History

Revisions to Documentation and Patches, iii

HL\*1.6\*96, 5-1

HL7 Control Segments, 4-3

HL7 DEGREE File (#771.9), 5-20, 5-21

HL7 Interface Specifications, 4-1

Application Parameters, 5-17

Assumptions, 4-1

Batch Acknowledgments, 4-2

Batch Messages, 4-2

BHS—Batch Header Segment, 4-6

BTS—Batch Trailer Segment, 4-7

Data Capture and Transmission, 4-1

EDU—Educational Detail Segment, 4-17

EVN—Event Type Segment, 4-9

HL7 Control Segments, 4-3

HL7 Logical Link, 5-18

HL7 Message Profile for PMU-B02, 4-3

HL7 Protocols, 5-17

Legend, 4-5

Mail Group, 5-18

Message Control Segments, 4-4

Message Definitions, 4-4

MSH—Message Header Segment, 4-7

ORG—Practitioner Organization Unit Segment, 4-15

PRA—Practitioner Detail Segment, 4-14

Scheduled Option, 5-17

Segment Table Definitions, 4-5

Sending System and Receiving System, 4-1

STF—Staff Identification Segment, 4-9

XUOAA CLIN TRAINEE, 5-18

HL7 Interface Standards, Version 2.4, 4-1

HL7 Message Profile for PMU-B02, 4-3

HL7 PMU. XUOAA SEND HL7 MESSAGE Batch Message, 5-2

Home Pages

Acronyms Website, Glossary, 7

Adobe Website, xiv

Glossary Website, Glossary, 7

VHA Software Document Library (VDL)

Website, xiv

VistA Development Website, xi

How to

Obtain Technical Information Online, xiii

Use this Manual, xi

I

IMAGING (RADIOLOGIC/ULTRASOUND TECH, ETC.), 5-5

Implementation, 5-1

input templates, 5-8

XUEXISTING USER, 3-1, 5-8

XUNEW USER, 3-1, 5-8, 5-14

XUREACT USER, 3-1, 5-8

XUSEREDIT, 5-14

XUSERREACT, 5-14

Installation Instructions, xiv

Interfaces, 5-20

Internal Relations, 5-19

Introduction, 1-1

K

Kernel

Input Options Affected, 3-1

Options, 3-1

User Inquiry Option, 3-11

Kernel Patch XU\*8.0\*251, 1-1

Kernel User Management Menu, 3-5

Keys

Security, 5-21

L

LABORATORY, 5-5

LAST TRAINING MONTH & YEAR Field (#12.3), 2-1, 3-4, 3-8, 3-11, 5-3

LAST TRAINING YEAR Field (#12.3), 5-3

Legal Requirements, xi

List of Active Registered Trainees, 3-6, 3-13, 5-11

List of All Registered Trainees, 3-6, 5-11

List of Inactive Registered Trainees, 3-7, 5-11

Local Trainee Registration Reports, 3-6, 3-12, 5-11

Logical Link

XUOAA

AUTOSTART, 5-18

M

Mail Groups, 5-18

XUOAA CLIN TRAINEE, 5-18, 5-20

Maintenance, 5-1

MEDICAL POST-RESIDENCY PHYSICIAN IN VA SPECIAL FELLOWSHIP (AMBULATORY, 5-5

MEDICAL RESIDENT/FELLOW, 5-5

MEDICAL STUDENT, 5-5

MEDICAL/SURGICAL SUPPORT (RESPIRATORY TECH, BIOMED TECH, ETC.), 5-5

Menu Diagram—\[XU-CLINICAL TRAINEE MENU\], 5-15

menu text

Add a New User to the System, 3-1, 3-2, 5-8, 5-14

Edit an Existing User, 3-1, 3-2, 3-4, 3-9, 5-8, 5-14

Edit Trainee Registration Data, 3-2, 3-6, 3-7, 3-8, 3-10, 5-9, 5-12

Kernel, 3-1

Kernel User Management, 3-5

List of Active Registered Trainees, 3-2, 3-6, 3-12, 5-11

List of All Registered Trainees, 3-2, 3-6, 3-13, 5-11

List of Inactive Registered Trainees, 3-2, 3-7, 3-14, 5-11

Local Trainee Registration Reports, 3-2, 3-6, 3-11, 3-12, 5-11

OAA Trainee Registration Menu, 3-2, 3-5, 3-7, 3-8, 3-10, 5-12

Reactivate a User, 3-1, 3-2, 5-8, 5-14

Send HL7 PMU message, 5-12

Total Count of Registered Trainees, 3-2, 3-7, 3-14, 5-11

Trainee Registration Inquiry, 3-2, 3-6, 3-7, 3-10, 5-9, 5-12

Usage, 3-10

Trainee Reports Menu, 3-2, 3-6, 3-7, 3-10, 3-12, 5-11

Trainee Transmission Report by Date, 3-2, 3-7, 3-15, 5-12

Trainee Transmission Report by Range, 3-2, 3-7, 3-17, 5-12

Trainee Transmission Report Selectable Items, 3-2, 3-7, 3-19, 5-12

Trainee Transmission Reports to OAA, 3-2, 3-7, 3-15, 5-11

User Inquiry, 3-2, 3-11, 5-9, 5-14

Menus, 5-21

Kernel User Management, 3-5

OAA Trainee Registration Menu, 3-5, 3-7, 3-8, 3-10

Message Control Segments, 4-4

Message Definitions, 4-4

Message Header Segment—MSH, 4-7

Messages

HL7 PMU. XUOAA SEND HL7 MESSAGE, 5-2

Messaging, HL7, 4-1

Modified Kernel Options, 5-12

N

NAME Field (#.01), 5-1

Namespace, 5-19

New Kernel Options, 5-11

NEW PERSON File (#200), 1-1, 1-2, 2-1, 2-2, 3-5, 3-8, 4-2, 5-1, 5-4, 5-6, 5-8, 5-9, 5-12

"ATR" New-Style Cross-reference, 5-6

CITY Field (#.114), 3-9

CLINICAL CORE TRAINEE (#12.6), 2-1, 5-4

CURRENT DEGREE LEVEL Field (#12.1), 2-1, 3-4, 3-8, 3-11

Data Dictionary, 5-19

DATE HL7 TRAINEE RECORD BUILT (12.5), 2-1, 5-4

DATE NO LONGER TRAINEE (#12.7), 2-1, 5-4

DEGREE Field (#10.6), 3-8, 3-9

DOB Field (#5), 3-9

input templates, 5-8

LAST TRAINING MONTH & YEAR (#12.3), 2-1, 3-4, 3-8, 3-11, 5-3

New-Style Cross-reference, 5-6

PROGRAM OF STUDY Field (#12.2), 2-1, 3-4, 3-8, 3-11

ScreenMan Forms, 5-8, 5-9

SERVICE/SECTION Field (#29), 3-8, 3-9

START OF TRAINING (#12.8), 2-1, 3-4, 3-8, 5-4

STATE Field (#.115), 3-9

STREET ADDRESS 1 Field (#.111), 3-9

STREET ADDRESS 2 Field (#.112), 3-9

STREET ADDRESS 3 Field (#.113), 3-9

TITLE Field (#8), 3-8, 3-9

VHA TRAINING FACILITY (#12.4), 2-1, 3-4, 3-8, 3-9, 3-11, 5-4, 5-8

ZIP CODE (#.116), 3-9

New-Style Cross-references

"ATR", 5-6

NURSE ANESTHETIST, 5-5

NURSING, 5-5

O

OAA Trainee Registration Menu, 3-5, 3-7, 3-8, 3-10, 5-12

Obtaining

Data Dictionary Listings, xiii

Online

Technical Information, How to Obtain, xiii

OPTION File (#19), 5-2, 5-13

options

Existing Kernel Options Affected, 5-14

Modified Kernel Options, 5-12

New Kernel Options, 5-11

Scheduled, 5-17

XU-CLINICAL ACTIVE TRAINEE, 3-2, 3-6, 3-12, 5-11

XU-CLINICAL INACTIVE TRAINEE, 3-2, 3-7, 3-14, 5-11

XU-CLINICAL LOCAL REPORTS, 3-2, 3-6, 3-11, 3-12, 5-11

XU-CLINICAL TRAINEE DB COUNT, 3-2, 3-7, 3-14, 5-11

XU-CLINICAL TRAINEE EDIT, 3-2, 3-6, 3-7, 3-8, 3-10, 5-9, 5-12

security key XUSHOWSSN, 3-8, 5-21

XU-CLINICAL TRAINEE INQUIRY, 3-2, 3-6, 3-7, 3-10, 5-9, 5-12

XU-CLINICAL TRAINEE LIST, 3-2, 3-6, 3-13, 5-11

XU-CLINICAL TRAINEE MENU, 3-2, 3-5, 3-10, 5-12

XU-CLINICAL TRAINEE REPORTS, 3-2, 3-6, 3-7, 3-10, 3-12, 5-11

XU-CLINICAL TRAINEE TRANSA, 3-2, 3-7, 3-15, 5-12

XU-CLINICAL TRAINEE TRANSB, 3-2, 3-7, 3-19, 5-12

XU-CLINICAL TRAINEE TRANSC, 3-2, 3-7, 3-17, 5-12

XU-CLINICAL TRANS REPORTS, 3-2, 3-7, 3-15, 5-11

XUOAA SEND HL7 MESSAGE, 5-2, 5-12

XUSER, 3-5

XUSEREDIT, 3-1, 3-2, 5-8, 5-14

XUSERINQ, 3-2, 3-11, 5-9, 5-14

XUSERNEW, 3-1, 3-2, 5-8, 5-14

XUSERREACT, 3-1, 3-2, 5-8, 5-14

Options, 5-21

OPTOMETRY, 5-5

Orientation, xi

conventions for displaying TEST data, xii

OTHER, 5-5

P

Patch History, iv

Patch XU\*8.0\*251, 1-1

Patches

HL\*1.6\*96, 5-1

XU\*8.0\*134, 5-1

XU\*8.0\*214, 5-1

XU\*8.0\*230, 5-2

XU\*8.0\*247, 5-2

XU\*8.0\*251, 1-3, 3-21, 3-22, 3-23

patient & user names

test data, xii

PHARMACY, 5-5

PHYSICIAN ASSISTANT, 5-5

PODIATRY, 5-5

Practitioner Detail Segment—PRA, 4-14

Practitioner Organization Unit Segment—ORG, 4-15

print templates

XU-CLINICAL ACTIVE TRAINEE, 3-6, 5-10

XU-CLINICAL INACTIVE TRAINEE, 3-7, 5-10

XU-CLINICAL TRAINEE DB COUNT, 3-7, 5-10

XU-CLINICAL TRAINEE INQUIRY, 3-6, 5-9

XU-CLINICAL TRAINEE LIST, 3-6, 5-10

XU-CLINICAL TRAINEE TRANSA, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSB, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSC, 3-7, 5-10

XUSERINQ, 3-11, 5-9, 5-14

PROGRAM OF STUDY Field (#12.2), 2-1, 3-4, 3-8, 3-11, 5-3, 5-4

PROGRAM OF STUDY File (#8932.2), 1-1, 5-4

AUDIOLOGY, 5-5

CARE, NATIONAL QUALITY SCHOLARS, WOMEN'S HEALTH, ETC.), 5-5

CHAPLAINCY, 5-5

Data Dictionary, 5-19

DENTISTRY, 5-5

DIETETICS, 5-5

HEALTH INFORMATION, 5-5

HEALTH SERVICES RESEARCH & DEVELOPMENT, 5-5

IMAGING (RADIOLOGIC/ULTRASOUND TECH, ETC.), 5-5

LABORATORY, 5-5

MEDICAL POST-RESIDENCY PHYSICIAN IN VA SPECIAL FELLOWSHIP (AMBULATORY, 5-5

MEDICAL RESIDENT/FELLOW, 5-5

MEDICAL STUDENT, 5-5

MEDICAL/SURGICAL SUPPORT (RESPIRATORY TECH, BIOMED TECH, ETC.), 5-5

NURSE ANESTHETIST, 5-5

NURSING, 5-5

OPTOMETRY, 5-5

OTHER, 5-5

PHARMACY, 5-5

PHYSICIAN ASSISTANT, 5-5

PODIATRY, 5-5

PSYCHOLOGY, 5-5

REHABILITATION (OT, PT, KT, ETC.), 5-5

SOCIAL WORK, 5-5

SPEECH - LANGUAGE PATHOLOGY, 5-5

PS Anonymous Directories, xiv

PSYCHOLOGY, 5-5

Purging, 5-16, 5-20

Purpose, 1-3

R

Reactivate a User, 5-8, 5-14

Reactivate a User Option, 3-1

Reader, Assumptions About the, xiii

Reference Materials, xiv

Registered Trainee Data, Edit, 3-1

Assign Registered Trainee Options to User(s), 3-5

Edit Trainee Registration Data, 3-6

input templates, 3-1

Kernel Options, 3-1

NEW PERSON File Entries, 3-2

ScreenMan Forms, 3-1

Trainee Registration Inquiry, 3-6

Registered Trainees, 1-1

REHABILITATION (OT, PT, KT, ETC.), 5-5

Relations

External, 5-18

Internal, 5-19

Remote Systems, 5-20

Reports

List of Active Registered Trainees, 3-13

Local Trainee Registration Reports, 3-12

Total Count of Registered Trainees, 3-14

Trainee Transmission Report by Range, 3-17

Trainee Transmission Reports to OAA, 3-15

Requirements

Dependencies, 5-1

Legal, xi

Software, 5-18

System, 1-3

Revision History, iii

Routines, 5-3

XUOAAHL7, 5-3

XUOAAUTL, 5-3

XUSERNEW, 5-3

S

Scheduled Option, 5-17

SCHEDULING RECOMMENDED Field (#209), 5-2, 5-13

ScreenMan Forms, 5-8

Differ from its Corresponding Input Template?, 3-1

XU-CLINICAL TRAINEE, 5-3, 5-9, 5-12

XUEXISTING USER, 3-1, 5-3, 5-8

XUNEW USER, 3-1, 3-6, 5-3, 5-8

XUREACT USER, 3-1, 5-3, 5-8

XUSEREDIT, 5-14

XUSERNEW, 5-14

XUSERREACT, 5-14

ScreenMan Forms and Templates, 5-8

Security

Keys, 5-21

Segment Table Definitions, 4-5

Send HL7 PMU message, 5-12

Sending System and Receiving System, 4-1

SERVICE/SECTION Field (#29), 3-8, 3-9

Social Security Numbers

test data, xii

SOCIAL WORK, 5-5

Software Dependencies, 5-1

Software Requirements, 5-18

Software Security, 5-20

Archiving, 5-20

Electronic Signatures, 5-20

File Security, 5-21

Interfaces, 5-20

Mail Groups, 5-20

Menus, 5-21

Purging, 5-20

Remote Systems, 5-20

XUSHOWSSN security key, 5-21

Software-wide Variables, 5-20

sort templates

XU-CLINICAL ACTIVE TRAINEE, 3-6, 5-10

XU-CLINICAL INACTIVE TRAINEE, 3-7, 5-10

XU-CLINICAL TRAINEE DB COUNT, 3-7, 5-10

XU-CLINICAL TRAINEE LIST, 3-6, 5-10

XU-CLINICAL TRAINEE TRANSA, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSB, 5-10

XU-CLINICAL TRAINEE TRANSC, 3-7, 5-10

SPEECH - LANGUAGE PATHOLOGY, 5-5

Staff Identification Segment—STF, 4-9

START OF TRAINING Field (#12.8), 2-1, 3-4, 3-8, 5-4

STATE Field (#.115), 3-9

STREET ADDRESS 1 Field (#.111), 3-9

STREET ADDRESS 2 Field (#.112), 3-9

STREET ADDRESS 3 Field (#.113), 3-9

Symbols Found in the Documentation, xii

System Requirements, 1-3

T

Tables, ix

Tables and Figures, ix

Technical Manual Information, 5-1

templates, input

XUEXISTING USER, 5-8

XUNEW USER, 5-8, 5-14

XUREACT USER, 5-8

XUSEREDIT, 5-14

XUSERREACT, 5-14

templates, print

XU-CLINICAL ACTIVE TRAINEE, 3-6, 5-10

XU-CLINICAL INACTIVE TRAINEE, 3-7, 5-10

XU-CLINICAL TRAINEE DB COUNT, 3-7, 5-10

XU-CLINICAL TRAINEE INQUIRY, 3-6, 5-9

XU-CLINICAL TRAINEE LIST, 3-6, 5-10

XU-CLINICAL TRAINEE TRANSA, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSB, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSC, 3-7, 5-10

XUSERINQ, 3-11, 5-9, 5-14

templates, sort

XU-CLINICAL ACTIVE TRAINEE, 3-6, 5-10

XU-CLINICAL INACTIVE TRAINEE, 3-7, 5-10

XU-CLINICAL TRAINEE DB COUNT, 3-7, 5-10

XU-CLINICAL TRAINEE LIST, 3-6, 5-10

XU-CLINICAL TRAINEE TRANSA, 3-7, 5-10

XU-CLINICAL TRAINEE TRANSB, 5-10

XU-CLINICAL TRAINEE TRANSC, 3-7, 5-10

test data

patient & user names, xii

Social Security Numbers, xii

TITLE Field (#8), 3-8, 3-9

Total Count of Registered Trainees, 3-7, 3-14, 5-11

Trainee Registration Inquiry, 3-6, 3-10, 5-9, 5-12

Usage, 3-10

Trainee Reports Menu, 3-6, 5-11

Trainee Transmission Report by Date, 3-7, 5-12

Trainee Transmission Report by Range, 3-7, 3-17, 5-12

Trainee Transmission Report Selectable Items, 3-7, 5-12

Trainee Transmission Reports to OAA, 3-7, 3-15, 5-11

U

URLs

Adobe Website, xiv

VHA Software Document Library (VDL)

Website, xiv

VistA Development

Website, xi

User Inquiry, 3-11, 5-9, 5-14

User Manual, 2-1

Using

Edit Trainee Registration Data, 3-7

Current Program of Study, 3-9

Last Training Year, 3-9

Target Degree Lvl, 3-9

Trainee Registration Inquiry, 3-10

V

Variables, 5-20

VHA Software Document Library (VDL)

Website, xiv

VHA TRAINING FACILITY Field (#12.4), 2-1, 3-4, 3-8, 3-9, 3-11, 5-4, 5-8

W

Web Pages

Acronyms Website, Glossary, 7

Adobe Website, xiv

Glossary Website, Glossary, 7

VHA Software Document Library (VDL)

Website, xiv

Websites

VistA Development Website, xi

X

XU\*8.0\*134, 5-1

XU\*8.0\*214, 5-1

XU\*8.0\*230, 5-2

XU\*8.0\*247, 5-2

XU\*8.0\*251, 1-1, 1-3, 3-21, 3-22, 3-23

XU-CLINICAL ACTIVE TRAINEE, 3-6, 5-10, 5-11

XU-CLINICAL INACTIVE TRAINEE, 3-7, 5-10, 5-11

XU-CLINICAL LOCAL REPORTS, 3-6, 5-11

XU-CLINICAL TRAINEE DB COUNT, 3-7, 5-10, 5-11

XU-CLINICAL TRAINEE EDIT, 3-6, 3-8, 5-9, 5-12

security key XUSHOWSSN, 3-8, 5-21

XU-CLINICAL TRAINEE INQUIRY, 3-6, 3-10, 5-9, 5-12

XU-CLINICAL TRAINEE LIST, 3-6, 5-10, 5-11

XU-CLINICAL TRAINEE MENU, 3-5, 3-10, 5-12

XU-CLINICAL TRAINEE REPORTS, 3-6, 5-11

XU-CLINICAL TRAINEE ScreenMan Form, 5-3, 5-9, 5-12

XU-CLINICAL TRAINEE TRANSA, 3-7, 5-10, 5-12

XU-CLINICAL TRAINEE TRANSB, 3-7, 5-10, 5-12

XU-CLINICAL TRAINEE TRANSC, 3-7, 5-10, 5-12

XU-CLINICAL TRANS REPORTS, 3-7, 5-11

XUEXISTING USER Input Template, 3-1

XUEXISTING USER ScreenMan Form, 3-1, 5-3

XUNEW USER Input Template, 3-1

XUNEW USER ScreenMan Form, 3-1, 3-6, 5-3

XUOAA CLIN TRAINEE Mail Group, 5-18, 5-20

XUOAA SEND HL7 MESSAGE, 5-2, 5-12

XUOAAHL7 Routine, 5-3

XUOAAUTL Routine, 5-3

XUREACT USER Input Template, 3-1

XUREACT USER ScreenMan Form, 3-1, 5-3

XUSER Menu, 3-5

XUSEREDIT, 5-8, 5-14

XUSEREDIT Option, 3-1

XUSEREDIT ScreenMan Form, 5-14

XUSERINQ, 3-11, 5-9, 5-14

XUSERNEW, 5-8, 5-14

XUSERNEW Option, 3-1

XUSERNEW Routine, 5-3

XUSERNEW ScreenMan Form, 5-14

XUSERREACT, 5-8, 5-14

XUSERREACT Option, 3-1

XUSERREACT ScreenMan Form, 5-14

XUSHOWSSN security key, 5-21

Z

ZIP CODE Field (#.116), 3-9