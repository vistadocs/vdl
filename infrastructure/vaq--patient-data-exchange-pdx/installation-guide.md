---
title: PDX V. 1.5 Release Notes Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes
app_code: VAQ
app_name: Patient Data Exchange (PDX)
section: INF
app_status: active
pkg_ns: VAQ
patch_ver: 1.5
patch_id: VAQ*1.5
group_key: "VAQ:VAQ:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: PDX V. 1.5 uses the newest version of the List Manager which was released with V. 5.3 of PIMS. PIMS V. 5.3 was mandated for October 1, 1993.
audience: 
keywords: 
  - added
  - filed
  - table
  - edit
  - patient
  - group
  - contents
  - protocol
  - transactions
  - release
page_count: 0
word_count: 6460
section_count: 9
table_count: 39
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: November 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=22"
---

---
title: Patient Data Exchange (PDX) Release Notes & Installation Guide
---

![](pdx-v-1-5-release-notes-installation-guide/001.png)

Office of Information and Technology (OI&T)

Software Version 1.5

Original Software Release: November 1993

Revised Documentation Release: February 2015

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 51%" />
<col style="width: 37%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>2/2015</td>
<td>Converted document to MS-Word 2007 format and incorporated <em><u>some</u></em> format changes from the ProPath User Guide Template.</td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="odd">
<td>1/10/05</td>
<td><p>Reformatted document to follow ISS styles and guidelines, no other content updates made.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: NHEPATIENT,[N] or NHEUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., NHEPATIENT, ONE, NHEPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="even">
<td>11/1993</td>
<td>Initial Patient Data Exchange V. 1.5 software documentation creation.</td>
<td>Albany, NY OIFO</td>
</tr>
</tbody>
</table>

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

Contents

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the installation and use of the Patient Data Exchange (PDX) software within Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure and Security Services (ISS) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                   |                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                        | Description                                                                                      |
| ![](pdx-v-1-5-release-notes-installation-guide/002.png)    | Used to inform the reader of general information including references to additional reading material |
| ![](pdx-v-1-5-release-notes-installation-guide/003.png) | Used to caution the reader to take special notice of critical information                            |

<span id="_Ref6202021" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/005.png) | Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. In character-based mode, users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- M programming language

It provides an overall explanation of the use of the Patient Data Exchange (PDX) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the VHA OI Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> REDACTED

Reference Materials

Readers who wish to learn more about Patient Data Exchange (PDX) documentation should consult the following:

- *Patient Data Exchange (PDX) Installation Guide & Release Notes* (this manual)
- *Patient Data Exchange (PDX) Technical Manual*
- *Patient Data Exchange (PDX) Security Guide*
- *Patient Data Exchange (PDX) User Manual*
- The Patient Data Exchange Home Page at the following Web address:

> REDACTED

> This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

VistA documentation can be downloaded from the Enterprise VistA Support (EVS) anonymous directories or from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](pdx-v-1-5-release-notes-installation-guide/008.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/009.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Release Notes](#release-notes)
    - [User Release Notes](#user-release-notes)
    - [Technical Release Notes](#technical-release-notes)
- [Installation Guide](#installation-guide)
    - [Introduction](#introduction)
    - [Software Integration](#software-integration)
    - [Software Initialization/Conversion Time Estimates](#software-initializationconversion-time-estimates)
    - [Resource Requirements](#resource-requirements)
    - [Pre-Installation](#pre-installation)
  - [## Appendix A—Version 1.0 Routines](#appendix-aversion-10-routines)
  - [Appendix B—Version 1.5 Routines](#appendix-bversion-15-routines)
  - [Appendix C—PDX V. 1.5 Sample Installation](#appendix-cpdx-v-15-sample-installation)
  - [Appendix D—File Descriptions](#appendix-dfile-descriptions)
  - [Appendix E—File Conversion](#appendix-efile-conversion)

### User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Patient Data Exchange (PDX) software is a set of modules designed to manage the transfer of patient information (demographics, episode of care, medication, and diagnostic evaluations) between VA Medical Centers using the MailMan electronic mail utility. Once transferred, this information may be combined with pertinent local information and assembled into a coherent composite record.
PDX V. 1.5 still uses the five main functions for sending, receiving, and displaying patient data. PDX V. 1.5 has been totally redesigned using the List Manager for the user interface. A new file design was implemented to ease the move to an HL7 messaging architecture.

#### Functionality Changes

A. The biggest change is in the user interface. PDX V. 1.5 uses the List Manager extensively. The List Manager is a tool designed to display a list of items to the user. It allows the user to browse back and forth through the items one at a time or by screen. It also allows the user to select items from the list to perform some kind of action. List Manager was initially released as part of MAS V. 5.2 for the scheduling application. It will be released in its own name space with the PIMS V. 5.3 release. This is the version PDX uses.
B. The other big change is the ability to send/request Health Summary components. Health Summary components are being added to provide clinical information from other facilities. This information will be "display only" and *cannot* be uploaded. The following Health Summary components have been provided.
|                             |                           |                           |
|-----------------------------|---------------------------|---------------------------|
| Adverse Reactions/Allergies | Clinical Warnings         | Crisis Notes              |
| Dietetics                   | Lab Blood Availability    | Lab Blood Transfusions    |
| Lab Chemistry & Hematology  | Lab Cumulative-Selected   | Lab Cumulative-Selected 1 |
| Lab Cumulative-Selected 2   | Lab Cumulative-Selected 3 | Lab Cumulative-Selected 4 |
| Lab Cytopathology           | Lab Microbiology          | Lab Microbiology Brief    |
| Lab Orders                  | Lab Orders Brief          | Lab Surgical Pathology    |
| Lab Tests Selected          | MAS ADT History           | MAS Admissions/Discharges |
| MAS Clinic Visits Future    | MAS Clinic Visits Past    | MAS Demographics          |
| MAS Demographics Brief      | MAS Disabilities          | MAS Discharge Diagnosis   |
| MAS Discharges              | MAS Procedures ICD Codes  | MAS Surgeries ICD         |
| MAS Transfers               | MAS Treating Specialty    | Medicine Summary          |
| Orders Current              | Pharmacy Intravenous      | Pharmacy Outpatient       |
| Pharmacy Unit Dose          | Progress Notes            | Progress Notes Brief      |
| Radiology Impression        | Radiology Profile         | Radiology Status          |
| Surgery Reports             | Surgery Reports Brief     | Vital Signs               |
| Vital Signs Selected        |                           |                           |
C. The interface for requesting/sending PDX information provides the ability to place time and occurrence limits on appropriate data segments. When defining the data segment to use, the user will be prompted for time and/or occurrence limits if the data segment is a Health Summary component which requires limits. A default value for each limit will be taken from the VAQ - PARAMETER file which the user may accept or change. Time and occurrence limits will be checked against the maximum values of information the facility is willing to release without user intervention.
D. Other components added as "display only":
- Means Test
- Copay
E. Other segment changes:
- Pharmacy is now two separate components (long and short)
- A PDX prefix was attached to all the V. 1.0 components
F. The ability to send/request a predefined group of segments. PDX V. 1.0 provided the ability to transfer patient demographics and pharmacy data within a single transmission. V. 1.5 will enable the user to request only those segments of data that are of interest to the user. With this capability, users and application programs can limit their request to only Pharmacy, PIMS, Copay, or certain Health Summary data.
G. The ability to send/request data for a patient from multiple sites and multiple segments. In PDX V. 1.0, you did not get the option to select the data you wanted. It was predetermined for you. In V. 1.5, you will be able to select any combination of the components.
H. To expedite user selection of data segments, it will be possible for users to predefine groups of commonly used data segments. These segment groups will work much like mail groups in that the user may enter a group name to select all segments contained in the group.
I. To expedite user selection of facilities, it will be possible to predefine groups of commonly used facilities. These facility groups will work much like mail groups.
J. The ability to request data on behalf of another user. This is a new feature for PDX V. 1.5. It allows multiple people to be notified via a mail message when data is returned. This could be done for people who do not have access to PDX.
K. The ability to include requested information in a mail message. This is a new feature of PDX V. 1.5. It allows the requested data to be included in the notification message. The prompt will allow the input of local mail groups.
L. The ability to authenticate users via electronic signature. This was added as a security measure to ensure the identity of the requester. All users will have to set up an electronic signature.
M. The ability to encrypt data using existing data encryption methods. This was added as an optional security measure. Sites wishing to encrypt certain fields for security reasons will have to turn the flag on and add those fields to the VAQ - encrypted fields file (#394.73).
N. An application program interface (API) will be provided so that PDX functions can be directly called by other VistA applications.
O. Sensitive Patient—When data pertaining to a sensitive patient is transferred, the data will be treated as sensitive at the receiving facility.
P. A status screen was added to send/request PDX information. The status screen will indicate current information already on file or pending requests for the selected patient. If desired, the user may display information already on file.
Q. The comments on "process external" have been expanded from 80 characters to a word-processing field. This will allow the user to enter as much information as needed.
R. Load/Edit was enhanced by running all patients through the PIMS duplicate check.
S. Display PDX by user—This option will display all current transactions originated by the user.
T. System reports enhanced by providing more predefined and customizable sort. New reports were added showing transactions which require manual processing and transactions which are currently on file.
> U. Security keys have been placed on the following options.
| \# | Mnemonic | Option         | Key   | Sub Option key |
|--------|--------------|--------------------|-----------|--------------------|
| 1\.    | LD           | Load/Edit PDX Data | VAQ LOAD  | none               |
| 2\.    | PRGE         | Purging            | VAQ PURGE | none               |
| 3\.    | RPT          | System Reports     | VAQ RPT   | VAQ RPT USER       |
| 4\.    | EDT          | PDX Edit Files     | none      | VAQ EDIT FILE      |
<span id="_Toc412806928" class="anchor"></span>Table 1‑1: PDX options with security keys

### Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The technical release notes outline changes made to Patient Data Exchange (PDX) files, routines, templates, options, mail groups, and bulletins.

#### Files

PDX V. 1.5 required a full redesign of the file structure. Because of this, the files used in V. 1.0 are being marked for deletion. The following table correlates V. 1.0 files to their V. 1.5 counterparts.
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 33%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name (V 1.0)</strong></th>
<th><strong>File #</strong></th>
<th><strong>File Name (V. 1.5)</strong></th>
<th><strong>File #</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PDX TRANSACTION</td>
<td>394</td>
<td>VAQ - TRANSACTION</td>
<td>394.61</td>
</tr>
<tr class="even">
<td>PDX DATA</td>
<td>394.1</td>
<td>VAQ - DATA</td>
<td>394.62</td>
</tr>
<tr class="odd">
<td>PDX PARAMETER</td>
<td>394.2<strong><sup>*</sup></strong></td>
<td><p>VAQ - PARAMETER</p>
<p>VAQ - RELEASE GROUP</p></td>
<td><p>394.81</p>
<p>394.82</p></td>
</tr>
<tr class="even">
<td>PDX STATUS</td>
<td>394.3</td>
<td>VAQ - STATUS</td>
<td>394.85</td>
</tr>
<tr class="odd">
<td>PDX STATISTICS</td>
<td>394.4</td>
<td>VAQ - WORKLOAD</td>
<td>394.87</td>
</tr>
</tbody>
</table>
<span id="_Toc412806929" class="anchor"></span>Table 1‑2: PDX file correlation from version 1.0 to version 1.5
<sup>\*</sup>Information contained in File \#394.2 was broken into two files.
When PDX V. 1.5 is installed, information contained in V. 1.0 files will be transferred to the new files. After doing this, V. 1.0 files will be marked for deletion. Deletion of V. 1.0 files will be done during the installation of PDX V. 2.0.
New Files
| File Name           | File \# | Description                                                                                                                                                             |
|-------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VAQ - DATA SEGMENT      | 394.71      | Defines each segment currently supported by PDX                                                                                                                             |
| VAQ - ENCRYPTION METHOD | 394.72      | Defines each encryption method currently supported by PDX                                                                                                                   |
| VAQ - ENCRYPTED FIELDS  | 394.73      | Contains all fields that should be encrypted in PDX requests and unsolicited PDXs transmitted by the facility. This file is only active when encryption has been turned on. |
| VAQ - OUTGOING GROUP    | 394.83      | Contains groups of facilities commonly accessed by PDX                                                                                                                      |
| VAQ - SEGMENT GROUP     | 394.84      | Contains groups of data segments commonly referenced by the facility                                                                                                        |
| VAQ - AUTO-NUMBERING    | 394.86      | Used to implement auto-numbering in PDX. Fields with auto-numbering capability will have an entry in this file.                                                             |
| VAQ - WORK              | 394.88      | Contains the type of work being tracked by the VAQ - WORKLOAD file                                                                                                          |
<span id="_Toc412806930" class="anchor"></span>Table 1‑3: PDX V. 1.5 new files

#### Routines

PDX V. 1.5 required a full redesign of all routines. Because of this, the routines used in V. 1.0 are being deleted during the install process. The following table provides the routine naming conventions followed for this version.
| Functional Area          | Namespace |
|------------------------------|---------------|
| Bulletins                    | VAQBULxx      |
| Cross-references             | VAQXRFxx      |
| Data Display                 | VAQDISxx      |
| Database Interface           | VAQDBIxx      |
| Encryption/Decryption        | VAQHSHxx      |
| Exported Routines            | VAQPSExx      |
| Inits                        | VAQIxxxx      |
| Load/Edit PDX Data           | VAQLEDxx      |
| Message Administration       | VAQADMxx      |
| Message Construction         | VAQCONxx      |
| Message Filing               | VAQFILxx      |
| Message Parsing              | VAQPARxx      |
| Onits                        | VAQOxxxx      |
| PDX Data Lookup              | VAQUPDxx      |
| Post Inits                   | VAQPSTxx      |
| Process External PDX Request | VAQEXTxx      |
| Purging                      | VAQPURxx      |
| Request Patient Information  | VAQREQxx      |
| Send Unsolicited PDX         | VAQUNSxx      |
| System Administration        | VAQADSxx      |
| User Authentication          | VAQAUTxx      |
| User Interface               | VAQUINxx      |
| Utility Routines             | VAQUTLxx      |
<span id="_Toc412806931" class="anchor"></span>Table 1‑4: Routine naming conventions
|                                                                                                                |                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/010.png) | The list of V. 1.0 routines being deleted and a complete list of V. 1.5 routines can be found in the "Installation Guide" section and Appendices in this manual. |

#### Templates

A. Print Templates
> VAQ PRINT STATS from PDX V. 1.0 is replaced by VAQ WORK-LOAD REPORT. This report is associated with VAQ - WORKLOAD file (#394.87).
> The following new print templates have been added:
- VAQ CUR. TRANSACTIONS REPORT associated with VAQ - TRANSACTION file (#394.61)
- VAQ REQUIRES PROCESSING REPORT associated with VAQ - TRANSACTION file (#394.61)
- VAQ DATA SEGMENT LIST associated with VAQ - DATA SEGMENT file (#394.71)
> B. Sort Templates
> The following templates, all of which are associated with VAQ -WORKLOAD file (#394.87), replace VAQ SORT STATS from PDX V. 1.0.
- VAQ WORK-LOAD BY DATE
- VAQ WORK-LOAD BY FACILITY
- VAQ WORK-LOAD BY PATIENT
- VAQ WORK-LOAD BY WORK
> The following new sort templates (all associated with VAQ - TRANSACTION file (#394.61)) have been added.
- VAQ REQUIRES PROCESSING
- VAQ TRANSACTIONS BY AUTHORIZER
- VAQ TRANSACTIONS BY DATE SENT
- VAQ TRANSACTIONS BY FACILITY
- VAQ TRANSACTIONS BY PATIENT
- VAQ TRANSACTIONS BY RECEIPT
- VAQ TRANSACTIONS BY REQUESTOR
- VAQ TRANSACTIONS BY STATUS
> C. Input Templates
> The following new input templates have been added.
- VAQ EDIT FILE (#394.71) allow for modification to time and occurrence limits
- VAQ EDIT FILE (#394.73) allows encrypted fields to be added/edited/deleted
- VAQ EDIT FILE (#394.81) allows modification to the site's VAQ - PARAMETER
- file (#394.81)
- VAQ EDIT FILE (#394.82) allows release groups to be added/edited/deleted
- VAQ EDIT FILE (#394.83) allows outgoing groups to be added/edited/deleted
- VAQ EDIT FILE (#394.84) allows all segment groups to be added/edited/deleted
- VAQ EDIT FILE (PRIVATE) (#394.84) allows private segment groups to be added/edited/deleted
- VAQ EDIT FILE (PUBLIC) (#394.84) allows public segment groups to be added/edited/deleted

#### Options

All V. 1.0 options have been deleted except VAQ-PDX-SERVER and VAQ PDX PURGE.
|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/011.png) | For a list of deleted options, please refer to Table 2‑3: Obsolete/Deleted PDX options in the "Installation Guide" section of this manual. |
The new options are as follows.
- VAQ (EDIT) ENCRY FIELD
- VAQ (EDIT) MAX LIMITS
- VAQ (EDIT) OUTGOING GROUP
- VAQ (EDIT) PARAMETER
- VAQ (EDIT) RELEASE GROUP
- VAQ (EDIT) SEGMENT GRP - ALL
- VAQ (EDIT) SEGMENT GRP - PRIV
- VAQ (EDIT) SEGMENT GRP - PUBL
- VAQ (MENU) CUR TRANSACTIONS
- VAQ (MENU) DISPLAY PDX
- VAQ (MENU) EDIT FILES
- VAQ (MENU) MAIN
- VAQ (MENU) PURGING
- VAQ (MENU) SYSTEM REPORTS
- VAQ (MENU) WORK-LOAD
- VAQ PDX DISPLAY (TRN)
- VAQ PDX DISPLAY (USER)
- VAQ PDX LOAD/EDIT
- VAQ PDX PROCESS EXTERNAL
- VAQ PDX PURGE
- VAQ PDX REQUEST
- VAQ PDX UNSOLICITED
- VAQ PURGE BY ENTERED DATE
- VAQ PURGE BY ENTERED LIFE
- VAQ REQUIRES PROCESSING
- VAQ TRANSACTIONS BY AUTHORIZER
- VAQ TRANSACTIONS BY DATE SENT
- VAQ TRANSACTIONS BY FACILITY
- VAQ TRANSACTIONS BY PATIENT
- VAQ TRANSACTIONS BY RECEIPT
- VAQ TRANSACTIONS BY REQUESTOR
- VAQ TRANSACTIONS BY STATUS
- VAQ TRANSACTIONS USER DEFINED
- VAQ WORKLOAD BY DATE
- VAQ WORKLOAD BY FACILITY
- VAQ WORKLOAD BY PATIENT
- VAQ WORKLOAD BY WORK
- VAQ WORKLOAD USER DEFINED
- VAQ-PDX-SERVER

#### Mail Groups

The V. 1.0 mail group VAQ PDX USER has been deleted and replaced by the following.
- VAQ PDX ERRORS all PDX errors
- VAQ MANUAL PROCESSING those transactions that require manual processing
- VAQ UNSOLICITED RECEIVED receipt of an unsolicited request
In PDX V. 1.5, specialized mail groups were set up to allow PDX support personnel to only subscribe to those groups which meet their needs and eliminate unwanted messages.

#### Bulletins

The following V. 1.0 bulletins have been deleted.
- VAQ PDX SERVER - PROCESS
- VAQ PDX SERVER - RETURNED
- VAQ PDX SERVER - UNSOLICITED
|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/012.png) | The V. 1.5 messages are not in the BULLETIN file (#3.6) and are produced by the PDX routines. These routines are contained in the subname space VAQBUL\*. |

# Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PDX V. 1.5 uses the newest version of the List Manager which was released with V. 5.3 of PIMS. PIMS V. 5.3 was mandated for October 1, 1993.

Please instruct PDX users to set up an electronic signature code. This can be accomplished through the Edit Electronic Signature Code option of the User's Toolbox menu.

It is recommended you slave print the installation process. The data printed out during the post-init should be reviewed.

### Software Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A. The following software versions (or higher) must be installed prior to loading this version of PDX.

> Kernel 7.0

> VA FileMan 19.0

> VA MailMan 7.0

> PIMS 5.3

> Pharmacy 5.6

> Integrating Billing 1.5

> Health Summary 1.2

> OE/RR 1.96

> Allergy Tracking 2.2

B. Integration between PDX V. 1.0 and PDX V. 1.5.

> PDX V. 1.0 is not forward compatible with PDX V. 1.5 unless patch VAQ\*1\*11 has been applied by V. 1.0 sites.

> The message structure for PDX transmissions has been changed with this version. V. 1.5 sites are able to accept messages in V. 1.0 format. If the V. 1.5 site must respond to the message (e.g., return requested data), it sends the response in the appropriate V. 1.0 format.

> However, there is a problem when a V. 1.5 site originates communication with a site using V. 1.0 (e.g., sends a PDX Request or an Unsolicited PDX). The V. 1.0 site cannot interpret the format and the message is lost. This patch will make it possible for V. 1.0 sites to receive these PDX messages.

> After the patch is installed, the V. 1.0 site will automatically request a retransmission for each PDX Request or Unsolicited PDX from the V. 1.5 site. This is accomplished without user intervention. The retransmission will be sent in the proper format.

|                                                                                                                |                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/013.png) | The extractions for PDX V. 1.0 and PDX V. 1.5 are different and some fields may be in different formats. |

C. The following IB routines are distributed with this version of PDX to allow copay to be an extractable component:
- IBAPDX
- IBAPDX0
- IBAPDX1.
D. GMTSPDX is distributed with this version of PDX to allow for the extraction of the Health Summary components. This routine uses the spooler. If a spooler is not set up at your site, the site will not be able to transmit Health Summary Data. This is significant to note, as it effects the major enhancement to PDX V. 1.5.

### Software Initialization/Conversion Time Estimates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information was derived from the alpha and beta sites. The information presented are averages. Actual times may vary depending on system utilization. The total install process not including the conversion takes on average one hour or less.

| Step   | MSM                                      | VAX                       |
|------------|----------------------------------------------|-------------------------------|
| VAQINIT    | 2 min                                        | 3 min                         |
| CONVERSION | 4 min per transaction (avg)<sup>\*</sup> | 5 min per transaction (avg)\* |

<span id="_Toc412806932" class="anchor"></span>Table 2‑1: Estimated installation time per operating system

<sup>\*</sup>These numbers were calculated during peak usage. Conversion time for non-peek was about 1 minute per transaction.

| Site   | Conversion Time | Transactions Converted |
|------------|---------------------|----------------------------|
| Boston MA  | 37 hrs              | 2673 (VAX)                 |
| Bedford MA | 4 hrs               | 180 (VAX)                  |

<span id="_Toc412806933" class="anchor"></span>Table 2‑2: Sample conversion data per site

Users can be brought back on the system before the conversion has finished. Converted transactions will become available for use as they complete the conversion process. Transactions in the process of conversion will not be available for use.

### Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites will see growth in the following three PDX files.

- VAQ - Transaction file (394.61) 200 bytes per entry\*
- VAQ - Data file (394.62) 50 bytes per entry\*
- VAQ - Workload file (394.87) 110 bytes per entry\*

\*Since variable fields are in these records, average record size was determined by sampling test sites.

It was determined that a single transaction on average will generate 185 data records. This was determined by taking the total number of entries in the VAQ - DATA file and dividing by the total number of entries in the VAQ - TRANSACTION file.

Disk storage requirements are estimated at approximately 10K per transaction. This was determined by taking the 185 data records at 50 bytes each plus a single transaction record at 200 bytes plus a variable number of workload records at 110 bytes each and dividing the total by 1024 bytes.

Global Growth can be controlled by the purge features of PDX.

### Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Insure that the patches which affect the PDX purge routine, VAQPRG, have been installed. These are VAQ\*1\*8 and VAQ\*1\*15.

2\. Request PDX staff to process all V. 1.0 requests. This will cut down on conversion time.

3\. Run V. 1.0 purger.

> This can be accomplished by rescheduling the start time of the background job (VAQ PDX PURGE) to current date and time plus two minutes.

> Go into the Task Manager and select Schedule/Unschedule Options. At the "Select OPTION to schedule or reschedule" prompt, enter VAQ PDX PURGE. Enter the current date/time at the "Queued to run at what time:" prompt.

4\. Determine how PDX V. 1.0 has been distributed (PDX main menu or custom menus) by running Option Access By User. This report is under the Menu Management menu.

5\. (optional) Back up System(s).

6\. Remove VAQ namespaced routines from the routine map. V. 1.0 had recommended mapping of the following routines:

- VAQDSP3
- VAQDSP6
- VAQUTL
- VAQUTL1
- VAQUTL2

7\. A spooling device must be installed in order to transmit Health Summary data. Typically VAX sites will already have one installed, while 486 sites will not. 486 sites should refer to the 486 Cookbook for assistance in setting up the spooler. The Health Summary Developers recommend allocating 2 Mb of disk space for the spooler.

8\. Determine Spool device name.

9\. The POSTMASTER must be given access to the spool device used by your facility. This can be accomplished by using the Edit an Existing User option \[XUSEREDIT\] and entering YES to the ALLOWED TO USE SPOOLER field.

#### Installation

1\. Request PDX users to be off the system.

2\. Sign into UCI where the software will be initially installed (use 40K partition for MSM).

3\. Disable Journaling.

4\. Delete VAQ namespaced routines.

D ^%RDELETE (VAX) or D ^%RDEL (MSM)

Routine(s) ? \> VAQ\*

Routine(s) ? \> -VAQWK *(do not delete this routine - used by PIMS)*

<span id="_Toc412806934" class="anchor"></span>Figure 2‑1: Deleting VAQ namespaced routines

|                                                                                                                |                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/014.png) | For deleted routines, please refer to Appendix A—Version 1.0 Routines. |

5\. Load PDX V. 1.5 tape/disk using routine restore.

|                                                                                                                |                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/015.png) | Sites using MSM will find the name of the file containing the routines on the disk label. |

> D ^%RR

|                                                                                                                |                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| ![](pdx-v-1-5-release-notes-installation-guide/016.png) | For a distributed routine list, please refer to Appendix B—Version 1.5 Routines. |

6\. Verify integrity values.

> D ^VAQNTEG

7\. Setup system variables.

> D ^XUP

> Verify DUZ, DT, DTIME, and U are defined and DUZ(0)="@". The DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize.

8\. D ^VAQINIT

> (Follow Appendix C for VAQINIT responses.)

> Please answer all initialization questions carefully.

> It is strongly recommended you take the bolded responses from the guide.

> A file conversion will be queued at the end of the initialization process. This utility has been included for your convenience. If you do not want to run the conversion, you must enter an up-arrow (^) when prompted for the conversion's device. Please refer to Appendix E if you have chosen to skip the conversion or the file conversion does not run to completion.

9\. Update Health Summary Site Parameter option.

> The GMTS IRM/ADPAC PARAMETER EDIT option must be modified to prompt for the SPOOL DEVICE NAME. This is done by adding ";.04" to the end of the existing DR {DIE} field. A sample of this is shown below.

D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: EVE

Select Systems Manager Menu Option: MENU MANAGEMENT

Select Menu Management Option: EDIT OPTIONS

Select OPTION to edit: GMTS IRM/ADPAC PARAMETER EDIT

NAME: GMTS IRM/ADPAC PARAMETER EDIT Replace ^DR {DIE}

DR {DIE}: .02;.03// .02;.03;.04

NO UP-ARROW: ^ *(user to enter up-arrow)*

Select OPTION NAME: GMTS IRM/ADPAC MAINT MENU

Select Health Summary IRM Maintenance Menu Option: 7 \<Enter\> Edit Health Summary Site Parameters

Select HEALTH SUMMARY PARAMETERS: HOSPITAL

PROMPT FOR ACTION PROFILE:// \<Enter\> (*take the value in field*)

INCLUDE COMMENTS FOR LABS:// \<Enter\> (*take the value in field*)

SPOOL DEVICE NAME: *\< enter device name \>*

<span id="_Toc412806935" class="anchor"></span>Figure 2‑2: Modifying the GMTS IRM/ADPAC PARAMETER EDIT option

10\. Using the Mail Group Edit option \[XMEDITMG\], add members to the newly created mail groups. The mail groups are as follows:

- VAQ PDX ERRORS—It is recommended that the System Manager be added to this group in order to monitor incoming messages which <u>cannot</u> be served (errors). These messages are saved in S.VAQ-PDX-SERVER mail basket.
- VAQ MANUAL PROCESSING
- VAQ UNSOLICITED RECEIVED

11\. The PDX server (VAQ-PDX-SERVER) needs to be edited in order to associate a mail group with the server. The mail group to add is VAQ PDX ERRORS. The installer will also have to change the server action from QUEUE SERVER ROUTINE to RUN IMMEDIATELY.

> \>D ^XUP

> Setting up programmer environment

> Terminal Type set to: C-VT100

> Select OPTION NAME: EVE \<Enter\> Systems Manager Menu

> Select Systems Manager Menu Option: Menu Management

> Select Menu Management Option: Edit options

> Select OPTION to edit: VAQ-PDX-SERVER \<Enter\> PDX Server

> NAME: VAQ-PDX-SERVER// ^SERVER ACTION

> SERVER ACTION: QUEUE SERVER ROUTINE// RUN IMMEDIATELY

> SERVER MAIL GROUP: VAQ PDX ERRORS// ^

<span id="_Toc412806936" class="anchor"></span>Figure 2‑3: Changing the PDX Server action to RUN IMMEDIATELY

12\. Enter Task Manager and select Schedule/Unschedule Options. At the "Select OPTION to schedule or reschedule" prompt, enter VAQ PDXPURGE and enter the values for the following fields. Fields not listed need to be reviewed for site specific values.

QUEUED TO RUN AT WHAT TIME: T+15@2400

RESCHEDULING FREQUENCY: 15D

<span id="_Toc412806937" class="anchor"></span>Figure 2‑4: Scheduling the VAQ PDX PURGE option

13\. Verify that the global attributes of ^VAT are as follows.

- SYSTEM = RWD
- WORLD = RWD
- GROUP = RWD
- UCI = RWD

14\. For all other systems move PDX routines, and translate ^VAT (if necessary).

15\. Delete obsolete options:

| \# | Option Name         | Option Text                                   |
|--------|-------------------------|---------------------------------------------------|
| 1      | VAQ PDX                 | PDX Menu                                          |
| 2      | VAQ PDX DISPLAY         | Display PDX Data                                  |
| 3      | VAQ PDX DISPLAY MAS     | Extended - View A Specific PDX                    |
| 4      | VAQ PDX DISPLAY MAS/PHA | Extended - View A Specific PDX                    |
| 5      | VAQ PDX DISPLAY PHA     | Extended - View A Specific PDX                    |
| 6      | VAQ PDX LOAD            | Load/Edit Patient File with PDX Information       |
| 7      | VAQ PDX PRINT MAS       | Brief - View Most Recent PDX From A Site          |
| 8      | VAQ PDX PRINT MAS/PHA   | Brief - View Most Recent PDX From A Site          |
| 9      | VAQ PDX PRINT PHA       | Brief - View Most Recent PDX From A Site          |
| 10     | VAQ PDX PROCESS         | Process External PDX Request                      |
| 11     | VAQ PDX SHOW MAS        | MAS - Display PDX's MAS Information               |
| 12     | VAQ PDX SHOW MAS/PHA    | Both - Display PDX's MAS & Pharmacy Information   |
| 13     | VAQ PDX SHOW PHA        | Pharmacy - Display PDX's Pharmacy Information     |
| 14     | VAQ PDX STAT DAY        | Today - Print Entries Made Today                  |
| 15     | VAQ PDX STAT GEN        | General - Print Entries Made During A Given Range |
| 16     | VAQ PDX STATS           | Statistics File Toolbox                           |

<span id="_Ref93196031" class="anchor"></span>Table 2‑3: Obsolete/Deleted PDX options

16\. Delete obsolete templates:

- Input Templates - None
- Sort Templates - VAQ SORT STATS
- Print Templates- VAQ PRINT STATS

17\. Delete obsolete mail group:

- VAQ PDX USERS

18\. Delete obsolete bulletins:

- VAQ PDX SERVER-PROCESS
- VAQ PDX SERVER-RETURNED
- VAQ PDX SERVER-UNSOLICITED

19\. Delete the initialization routines VAQIN\*, VAQON\*, and VAQPSL\*.  
  
Do not delete VAQINITY.

20\. At the end of the process, a mail message is sent to the development OIFO indicating that the install is complete.

21\. Enable Journaling.

## ## Appendix A—Version 1.0 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| VAQADD   | VAQADD1  | VAQADD2  | VAQADD3  | VAQADD4  | VAQADD5  | VAQADD7  | VAQDBUG  |
| VAQDBUG1 | VAQDBUG2 | VAQDSP1  | VAQDSP10 | VAQDSP11 | VAQDSP12 | VAQDSP13 | VAQDSP14 |
| VAQDSP15 | VAQDSP2  | VAQDSP3  | VAQDSP3A | VAQDSP4  | VAQDSP5  | VAQDSP6  | VAQDSP7  |
| VAQDSP8  | VAQDSP9  | VAQIN001 | VAQIN002 | VAQIN003 | VAQIN004 | VAQIN005 | VAQIN006 |
| VAQIN007 | VAQIN008 | VAQIN009 | VAQIN010 | VAQIN011 | VAQIN012 | VAQIN013 | VAQIN014 |
| VAQIN015 | VAQINIT  | VAQINIT0 | VAQINIT1 | VAQINIT2 | VAQINIT3 | VAQMAS   | VAQMAS1  |
| VAQMAS1A | VAQMAS2  | VAQMAS2A | VAQMAS3  | VAQMAS4  | VAQMAS5  | VAQMAS6  | VAQMAS6A |
| VAQNTEG  | VAQPHA1  | VAQPRG   | VAQPRT   | VAQPRT1  | VAQRQP   | VAQRQP1  | VAQRQR   |
| VAQRQR1  | VAQRQU   | VAQST1   | VAQST2   | VAQST3   | VAQUTL   | VAQUTL1  | VAQUTL2  |

72 routines

## Appendix B—Version 1.5 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|
| VAQADM2  | VAQADM21 | VAQADM22 | VAQADM23 | VAQADM5  | VAQADM50 | VAQADM51 | VAQADS01 |
| VAQAUT   | VAQBUL   | VAQBUL01 | VAQBUL02 | VAQBUL03 | VAQBUL04 | VAQBUL05 | VAQBUL06 |
| VAQBUL07 | VAQCON   | VAQCON0  | VAQCON1  | VAQCON2  | VAQCON3  | VAQCON4  | VAQCON5  |
| VAQCON6  | VAQCON7  | VAQCON8  | VAQCON93 | VAQCON94 | VAQCON95 | VAQCON96 | VAQCON97 |
| VAQCON98 | VAQCON99 | VAQDBI   | VAQDBIH1 | VAQDBIH2 | VAQDBIH3 | VAQDBII1 | VAQDBIM  |
| VAQDBIM0 | VAQDBIM1 | VAQDBIM2 | VAQDBIM3 | VAQDBIM4 | VAQDBIP  | VAQDBIP1 | VAQDBIP2 |
| VAQDBIP3 | VAQDBIP4 | VAQDBIP5 | VAQDBIP6 | VAQDBIP7 | VAQDBIP8 | VAQDIS01 | VAQDIS10 |
| VAQDIS11 | VAQDIS12 | VAQDIS15 | VAQDIS16 | VAQDIS17 | VAQDIS20 | VAQDIS21 | VAQDIS22 |
| VAQDIS23 | VAQDIS24 | VAQDIS25 | VAQDIS26 | VAQDIS27 | VAQDIS28 | VAQDIS29 | VAQDIS30 |
| VAQDIS31 | VAQDIS32 | VAQDIS33 | VAQDIS40 | VAQDIS41 | VAQDIS42 | VAQDIS43 | VAQEXT01 |
| VAQEXT02 | VAQEXT03 | VAQEXT04 | VAQEXT05 | VAQEXT06 | VAQFIL10 | VAQFIL11 | VAQFIL12 |
| VAQFIL13 | VAQFIL14 | VAQFIL15 | VAQFIL16 | VAQFIL17 | VAQFIL18 | VAQFILE  | VAQFILE1 |
| VAQHSH   | VAQHSH1  | VAQIN001 | VAQIN002 | VAQIN003 | VAQIN004 | VAQIN005 | VAQIN006 |
| VAQIN007 | VAQIN008 | VAQIN009 | VAQIN010 | VAQIN011 | VAQIN012 | VAQIN013 | VAQIN014 |
| VAQIN015 | VAQIN016 | VAQIN017 | VAQIN018 | VAQIN019 | VAQIN020 | VAQIN021 | VAQIN022 |
| VAQIN023 | VAQIN024 | VAQIN025 | VAQIN026 | VAQIN027 | VAQIN028 | VAQIN029 | VAQIN030 |
| VAQIN031 | VAQIN032 | VAQIN033 | VAQIN034 | VAQIN035 | VAQIN036 | VAQIN037 | VAQIN038 |
| VAQIN039 | VAQIN040 | VAQIN041 | VAQIN042 | VAQIN043 | VAQIN044 | VAQIN045 | VAQIN046 |
| VAQIN047 | VAQIN048 | VAQIN049 | VAQIN050 | VAQIN051 | VAQIN052 | VAQIN053 | VAQIN054 |
| VAQIN055 | VAQIN056 | VAQIN057 | VAQIN058 | VAQIN059 | VAQIN060 | VAQIN061 | VAQIN062 |
| VAQIN063 | VAQIN064 | VAQIN065 | VAQIN066 | VAQIN067 | VAQIN068 | VAQIN069 | VAQIN070 |
| VAQINIT  | VAQINIT1 | VAQINIT2 | VAQINIT3 | VAQINIT4 | VAQINIT5 | VAQINITY | VAQLED01 |
| VAQLED02 | VAQLED03 | VAQLED04 | VAQLED05 | VAQLED07 | VAQLED09 | VAQLED10 | VAQNTEG  |
| VAQNTEG0 | VAQON001 | VAQON002 | VAQON003 | VAQON004 | VAQON005 | VAQONIT  | VAQONIT1 |
| VAQONIT2 | VAQONIT3 | VAQPAR1  | VAQPAR10 | VAQPAR11 | VAQPAR6  | VAQPAR60 | VAQPAR61 |
| VAQPSE01 | VAQPSE02 | VAQPSE03 | VAQPSE04 | VAQPSL   | VAQPSL1  | VAQPSL2  | VAQPSL3  |
| VAQPST01 | VAQPST02 | VAQPST03 | VAQPST04 | VAQPST05 | VAQPST10 | VAQPST20 | VAQPST21 |
| VAQPST22 | VAQPST23 | VAQPST24 | VAQPST25 | VAQPST30 | VAQPST31 | VAQPST40 | VAQPUR   |
| VAQPUR10 | VAQPUR11 | VAQREQ01 | VAQREQ02 | VAQREQ03 | VAQREQ04 | VAQREQ05 | VAQREQ06 |
| VAQREQ07 | VAQREQ08 | VAQREQ09 | VAQREQ10 | VAQREQ11 | VAQUIN01 | VAQUPD1  | VAQUPD2  |
| VAQUPD25 | VAQUTL1  | VAQUTL2  | VAQUTL3  | VAQUTL4  | VAQUTL92 | VAQUTL93 | VAQUTL94 |
| VAQUTL95 | VAQUTL96 | VAQUTL97 | VAQUTL98 | VAQUTL99 | VAQXRF1  | VAQXRF2  | VAQXRF3  |

256 routines

## Appendix C—PDX V. 1.5 Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^VAQINIT

This version (#1.5) of 'VAQINIT' was created on 12-NOV-1993

(at PDX DEVELOPMENT (PRIMARY), by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

142.99 HEALTH SUMMARY PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'HEALTH SUMMARY PARAMETERS' File.

394 \*PDX TRANSACTION

\*BUT YOU ALREADY HAVE 'PDX TRANSACTION' AS FILE \#394!

Shall I change the NAME of the file to \*PDX TRANSACTION? NO// YES

394 \*PDX TRANSACTION

> **NOTE:** You already have the '\*PDX TRANSACTION' File.

394.1 \*PDX DATA

\*BUT YOU ALREADY HAVE 'PDX DATA' AS FILE \#394.1!

Shall I change the NAME of the file to \*PDX DATA? NO// YES

394.1 \*PDX DATA

> **NOTE:** You already have the '\*PDX DATA' File.

394.2 \*PDX PARAMETER

\*BUT YOU ALREADY HAVE 'PDX PARAMETER' AS FILE \#394.2!

Shall I change the NAME of the file to \*PDX PARAMETER? NO// YES

394.2 \*PDX PARAMETER

> **NOTE:** You already have the '\*PDX PARAMETER' File.

394.3 \*PDX STATUS (including data)

\*BUT YOU ALREADY HAVE 'PDX STATUS' AS FILE \#394.3!

Shall I change the NAME of the file to \*PDX STATUS? NO// YES

394.3 \*PDX STATUS (including data)

> **NOTE:** You already have the '\*PDX STATUS' File.

I will OVERWRITE your data with mine.

394.4 \*PDX STATISTICS

\*BUT YOU ALREADY HAVE 'PDX STATISTICS' AS FILE \#394.4!

Shall I change the NAME of the file to \*PDX STATISTICS? NO// YES

394.61 VAQ - TRANSACTION

394.62 VAQ - DATA

394.71 VAQ - DATA SEGMENT (including data)

I will OVERWRITE your data with mine.

394.72 VAQ - ENCRYPTION METHOD (including data)

I will OVERWRITE your data with mine.

394.73 VAQ - ENCRYPTED FIELDS (including data)

I will MERGE your data with mine.

394.81 VAQ - PARAMETER

394.82 VAQ - RELEASE GROUP

394.83 VAQ - OUTGOING GROUP

394.84 VAQ - SEGMENT GROUP

394.85 VAQ - STATUS (including data)

I will OVERWRITE your data with mine.

394.86 VAQ - AUTO-NUMBERING

394.87 VAQ - WORKLOAD

394.88 VAQ - WORK (including data)

I will OVERWRITE your data with mine.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<YES\>

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<Enter\>

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<Enter\>

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<Enter\>

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// \<Enter\>

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<Enter\>

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<Enter\>

ARE YOU SURE EVERYTHING'S OK? NO// YES

...SORRY, LET ME THINK ABOUT THAT A MOMENT............................

'VAQ (EDIT) ENCRY FIELDS' Option Filed

'VAQ (EDIT) MAX LIMITS' Option Filed

'VAQ (EDIT) OUTGOING GROUP' Option Filed

'VAQ (EDIT) PARAMETER' Option Filed

'VAQ (EDIT) RELEASE GROUP' Option Filed

'VAQ (EDIT) SEGMENT GRP - ALL' Option Filed

'VAQ (EDIT) SEGMENT GRP - PRIV' Option Filed

'VAQ (EDIT) SEGMENT GRP - PUBL' Option Filed

'VAQ (MENU) CUR TRANSACTIONS' Option Filed

'VAQ (MENU) DISPLAY PDX' Option Filed

'VAQ (MENU) EDIT FILES' Option Filed

'VAQ (MENU) MAIN' Option Filed

'VAQ (MENU) PURGING' Option Filed

'VAQ (MENU) SYSTEM REPORTS' Option Filed

'VAQ (MENU) WORK-LOAD' Option Filed

'VAQ PDX DISPLAY (TRN)' Option Filed

'VAQ PDX DISPLAY (USER)' Option Filed

'VAQ PDX LOAD/EDIT' Option Filed

'VAQ PDX PROCESS EXTERNAL' Option Filed

'VAQ PDX PURGE' Option Filed

'VAQ PDX REQUEST' Option Filed

'VAQ PDX UNSOLICITED' Option Filed

'VAQ PURGE BY ENTERED DATE' Option Filed

'VAQ PURGE BY ENTERED LIFE' Option Filed

'VAQ REQUIRES PROCESSING' Option Filed

'VAQ TRANSACTIONS BY AUTHORIZER' Option Filed

'VAQ TRANSACTIONS BY DATE SENT' Option Filed

'VAQ TRANSACTIONS BY FACILITY' Option Filed

'VAQ TRANSACTIONS BY PATIENT' Option Filed

'VAQ TRANSACTIONS BY RECEIPT' Option Filed

'VAQ TRANSACTIONS BY REQUESTOR' Option Filed

'VAQ TRANSACTIONS BY STATUS' Option Filed

'VAQ TRANSACTIONS USER DEFINED' Option Filed

'VAQ WORKLOAD BY DATE' Option Filed

'VAQ WORKLOAD BY FACILITY' Option Filed

'VAQ WORKLOAD BY PATIENT' Option Filed

'VAQ WORKLOAD BY WORK' Option Filed

'VAQ WORKLOAD USER DEFINED' Option Filed

'VAQ-PDX-SERVER' Option Filed...............................

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

Begin of Post Init Process

Installing protocols for use by the list processor

This version of 'VAQONIT' was created on 21-JUL-1993

(at PDX DEVELOPMENT (PRIMARY), by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on PLEASE..........................

'VAQ ADD PATIENT' Protocol Filed

'VAQ ADD/EDIT REQUEST' Protocol Filed

'VAQ CHANGE PATIENT' Protocol Filed

'VAQ COPY REQUEST' Protocol Filed

'VAQ CREATE REQUEST' Protocol Filed

'VAQ DIS ALL SEGMENT' Protocol Filed

'VAQ DIS SELECTED SEGMENT' Protocol Filed

'VAQ DIS1 (MENU)' Protocol Filed

'VAQ DISPLAY BY REQUESTOR' Protocol Filed

'VAQ DISPLAY PDX' Protocol Filed

'VAQ DISPLAY SELECT' Protocol Filed

'VAQ DUPLICATE' Protocol Filed

'VAQ LOAD DATA' Protocol Filed

'VAQ LOAD EDIT' Protocol Filed

'VAQ LOAD FIELD' Protocol Filed

'VAQ NEW PATIENT' Protocol Filed

VAQ DUPLICATE added as item to VAQ NEW PATIENT.

'VAQ PDX1 (MENU)' Protocol Filed

VAQ DISPLAY PDX added as item to VAQ PDX1 (MENU).

VAQ CREATE REQUEST added as item to VAQ PDX1 (MENU).

'VAQ PDX10 (MENU)' Protocol Filed

VAQ DISPLAY BY REQUESTOR added as item to VAQ PDX10 (MENU).

'VAQ PDX11 (MENU)' Protocol filed

VAQ DIS SELECTED SEGMENT added as item to VAQ PDX11 (MENU).

VAQ DIS ALL SEGMENT added as item to VAQ PDX11 (MENU).

'VAQ PDX12 (MENU)' Protocol filed

'VAQ PDX2 (MENU)' Protocol Filed

VAQ CHANGE PATIENT added as item to VAQ PDX2 (MENU).

VAQ ADD/EDIT REQUEST added as item to VAQ PDX2 (MENU).

VAQ TRANSMIT REQUEST added as item to VAQ PDX2 (MENU).

VAQ COPY REQUEST added as item to VAQ PDX2 (MENU).

'VAQ PDX3 (MENU)' Protocol Filed

VAQ PROCESS MANUAL added as item to VAQ PDX3 (MENU).

'VAQ PDX4 (MENU)' Protocol Filed

VAQ PROCESS RELEASE added as item to VAQ PDX4 (MENU).

VAQ PROCESS REJECT added as item to VAQ PDX4 (MENU).

'VAQ PDX5 (MENU)' Protocol Filed

VAQ LOAD EDIT added as item to VAQ PDX5 (MENU).

'VAQ PDX6 (MENU)' Protocol Filed

VAQ LOAD DATA added as item to VAQ PDX6 (MENU).

VAQ LOAD FIELD added as item to VAQ PDX6 (MENU).

'VAQ PDX7 (MENU)' Protocol Filed

VAQ ADD PATIENT added as item to VAQ PDX7 (MENU).

'VAQ PDX8 (MENU)' Protocol Filed

VAQ DUPLICATE added as item to VAQ PDX8 (MENU).

VAQ NEW PATIENT added as item to VAQ PDX8 (MENU).

'VAQ PDX9 (MENU)' Protocol Filed

VAQ DISPLAY SELECT added as item to VAQ PDX9 (MENU).

'VAQ PROCESS MANUAL' Protocol Filed

'VAQ PROCESS REJECT' Protocol Filed

'VAQ PROCESS RELEASE' Protocol Filed

'VAQ TRANSMIT REQUEST' Protocol Filed

OK, Protocol Installation is Complete.

Protocol install completed

Installing list templates for use by list processor

'VAQ DIS MIN NUPD' List Template...Filed.

'VAQ DIS MIN UPD' List Template...Filed.

'VAQ DIS PATIENT PDX9' List Template...Filed.

'VAQ DIS REQUESTOR PDX10' List Template...Filed.

'VAQ DISPLAY DATA PDX12' List Template...Filed.

'VAQ DISPLAY MINIMUM' List Template...Filed.

'VAQ DISPLAY SEGMENT PDX11' List Template...Filed.

'VAQ DUPLICATE PDX8' List Template...Filed.

'VAQ LED DIFFERENCES PDX6' List Template...Filed.

'VAQ LED STATUS PDX5' List Template...Filed.

'VAQ MATCHES PDX8' List Template...Filed.

'VAQ PROCESS PDX3' List Template...Filed.

'VAQ PROCESS PDX4' List Template...Filed.

'VAQ REQUEST PDX2' List Template...Filed.

'VAQ STATUS PDX1' List Template...Filed.

\*\* List Template install completed

\>\>\> Exported routines will now be loaded

Copying of VAQPSE01 into GMTSPDX Done

Copying of VAQPSE02 into IBAPDX Done

Copying of VAQPSE03 into IBAPDX0 Done

Copying of VAQPSE04 into IBAPDX1 Done

Done

Initialization of VAQ Parameter file *(See Appendix D \#1)*

Enter missing field(s)

Default Time Limit:

Default Occurrence Limit:

\*\* Missing fields added, initialization complete

Updating pointers to Health Summary components and initializing

maximum time and occurrence limits (when appropriate)........

Updating completed

Initialization of VAQ - Auto-numbering file

\*\* Initialization of VAQ - Auto-numbering file complete

Initialization of VAQ - Encrypted Fields File... (add/edit/delete)

Select VAQ - ENCRYPTED FIELDS Encrypt Field: *(See Appendix D \#2)*

\*\* Initialization of VAQ - Encrypted Fields File complete

Initialization of VAQ - Release Group File...

Updating VAQ - Release Group file from version 1.0

Update from version 1 completed

Add/Edit/Delete entries in VAQ - Release Group

Select VAQ - RELEASE GROUP Remote Facility: *(See Appendix D \#3)*

\*\* Initialization of VAQ - Release Group File complete

Initialization of VAQ - Outgoing Group File... (add/edit/delete)

Select VAQ - OUTGOING GROUP Group Name: *(See Appendix D \#4)*

\*\* Initialization of VAQ - Outgoing Group File complete

Initialization of VAQ - Segment Group File...

Creating a segment group called "ALL"

This group will contain all data segments

Adverse Reactions/Allergies - added

Clinical Warnings - added

Crisis Notes - added

Dietetics - added

Integrated Billing - added

Lab Blood Availability - added

Lab Blood Transfusions - added

Lab Chemistry & Hematology - added

Lab Cumulative-Selected - added

Lab Cumulative-Selected 1 - added

Lab Cumulative-Selected 2 - added

Lab Cumulative-Selected 3 - added

Lab Cumulative-Selected 4 - added

Lab Cytopathology - added

Lab Microbiology - added

Lab Microbiology Brief - added

Lab Orders - added

Lab Orders Brief - added

Lab Surgical Pathology - added

Lab Tests Selected - added

MAS ADT History - added

MAS Admissions/Discharges - added

MAS Clinic Visits Future - added

MAS Clinic Visits Past - added

MAS Demographics - added

MAS Demographics Brief - added

MAS Disabilities - added

MAS Discharge Diagnosis - added

MAS Discharges - added

MAS Minimum Patient Information - added

MAS Procedures ICD Codes - added

MAS Registration Information - added

MAS Surgeries ICD Codes - added

MAS Transfers - added

MAS Treating Specialty - added

Means Test Information - added

Medication Profile - Long Form - added

Medication Profile - Short For - added

Medicine Summary - added

Orders Current - added

Pharmacy Intravenous - added

Pharmacy Outpatient - added

Pharmacy Unit Dose - added

Progress Notes - added

Progress Notes Brief - added

Radiology Impression - added

Radiology Profile - added

Radiology Status - added

Surgery Reports - added

Surgery Reports Brief - added

Vital Signs - added

Vital Signs Selected - added

Done

Create entries in Segment Groups for Health Summary Type File? NO// \<Enter\>

Add/Edit/Delete entries in VAQ - Segment Group File

Select VAQ - SEGMENT GROUP Group Name: *(See Appendix D \#5)*

\*\* Initialization of VAQ - Segment Group File complete

Creating Mail Groups for PDX

'VAQ PDX ERRORS' mail group created

'VAQ MANUAL PROCESSING' mail group created

'VAQ UNSOLICITED RECEIVED' mail group created

Mail Groups created

\- Conversion of version 1.0 files will now be tasked -

Entering 'HOME' as the device for output will cause conversion

to be run without an output device. It is recommended that a

device be chosen so that errors during the conversion can be

reported.

Entering '^' as the device for output will skip the conversion

process. Please refer to the INSTALLATION GUIDE if you choose

to do this.

Enter device to use during conversion: HOME// {*conditional response}{If you have chosen to convert V. 1.0 data, respond as follows:}*

Enter device to use during conversion: HOME// \<DEVICE\> {*user should enter adevice on the system*}

Requested Start Time: NOW// \<Enter\>

Conversion tasked (TASK \#)

*{If you have chosen not to convert V. 1.0 data, respond as follows:}*

Enter device to use during conversion: HOME// ^

\- Conversion will not be done at this time -

To run conversion at a later date the entry point TASK^VAQPST20

should be used.

If you have chosen to skip the conversion the entry point

DELETE^VAQPST24(1) must be used in order to delete entries

contained in the 1.0 files.

*{The following information will be printed after answering the device prompt shown above.}*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*IMPORTANT \* The following things need to be done.

\*

\* - Members need to be added to the newly created mail groups.

\* The option is XMEDITMG.

\*

\* - The PDX Server (VAQ-PDX-SERVER) needs to be edited in order

\* to associate a mail group with the server. The mail group

\* to add is 'VAQ PDX ERRORS'. The installer will also have

\* to change the server action from 'QUEUE SERVER ROUTINE' to

\* 'RUN IMMEDIATELY'

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

In order to effectively use PDX, the following terminal type attributes

must be defined for each terminal type used. Please verify these

attributes against the Terminal Type file at your facility.

Attribute Value for a VT series terminal

--------- ------------------------------

Form Feed \#,\$C(27,91,50,74,27,91,72)

XY CRT W \$C(27,91)\_(DY+1)\_\$C(59)\_(DX+1)\_\$C(72)

Erase to End of Page \$C(27,91,74)

Insert Line \$C(27)\_"\[1L"

Underline On \$C(27,91,52,109)

Underline Off \$C(27,91,109)

High Intensity \$C(27,91,49,109)

Normal Intensity \$C(27,91,109)

Save Cursor Position \$C(27,55)

Restore Cursor Position \$C(27,56)

Set Top/Bottom Margin \$C(27,91)\_(+IOTM)\_\$C(59)\_(+IOBM)\_\$C(114)

Post init process completed

\>

<span id="_Toc412806939" class="anchor"></span>Figure C-1: Sample PDX V. 1.5 installation at the Albany OIFO

## Appendix D—File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VAQ - Parameter file (#394.81)

> This file contains site specific information concerning the use of PDX. This file is initialized from V. 1.0 data

> 2\. VAQ - Encrypted Fields file (#394.73)

> This file contains all fields that should be encrypted when PDX Requests and Unsolicited PDXs are transmitted by the facility. This file is only relevant when encryption has been turned on. The installer has the option to populate this file at this time. Entries are not required.

> 3\. VAQ - Release Group file (#394.82)

> This file contains the facilities that have been granted "automatic processing". In order for a request to be automatically processed, the requesting facility must have an entry in this file. This file has been populated from the entries found in V. 1.0. The init also allows the installer to make changes to this file at this time.

> 4\. VAQ - Outgoing Group file (#394.83)

> This file contains groups of facilities commonly accessed by PDX. This will work much like mail groups. When requesting a PDX, you could access an outgoing group called G.BETA. This would be the equivalent of entering in the beta sites individually.

> 5\. VAQ - Segment Group file (#394.84)

> This file contains groups of data segments commonly referenced by the facility. Groups marked as PUBLIC may be referenced by all users of PDX. Groups marked as PRIVATE may only be referenced by the individual that created the group. This works the same as mail groups and outgoing groups (i.e., G.CLINICAL - this could contain any combination of the Health Summary components).

## Appendix E—File Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the conversion does not run to completion, the entry point TASK^VAQPST20 should be used to requeue the conversion. This is the same entry point used by the post-init, and all prompts and responses will be consistent with those previously mentioned.

If you would prefer to run the conversion in the foreground (i.e., from your terminal), the entry point INTER^VAQPST20 should be used. If you do not want information concerning the conversion printed to the current device, the entry point NONINTER^VAQPST20 should be used.

If you choose not to run the conversion, the data contained in the V. 1.0 files should still be deleted. To do this, the entry point DELETE^VAQPST24 should be used. If you want information concerning the deletion printed to the current device, a parameter of "1" should be passed.

Sample PDX Calls from Programmer Mode

| Call                 | Description                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------|
| D TASK^VAQPST20      | Prompts for device and queues conversion (choose the HOME device if silent mode is desired). |
| D NONINTER^VAQPST20  | Runs conversion in silent mode (nothing printed).                                            |
| D INTER^VAQPST20     | Runs conversion using current device.                                                        |
| D DELETE^VAQPST24( ) | Deletes entries in V. 1.0 files in silent mode (nothing printed).                            |
| D DELETE^VAQPST24(1) | Deletes entries in V. 1.0 files using current device.                                        |

<span id="_Toc412806940" class="anchor"></span>Table E-1: Sample PDX calls from Programmer Mode