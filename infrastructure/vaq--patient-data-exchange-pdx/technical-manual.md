---
title: PDX V. 1.5 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
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
description: 
audience: 
keywords: 
  - table
  - contents
  - software
  - patient
  - span
  - class
  - manual
  - edit
  - technical
  - documentation
page_count: 0
word_count: 3619
section_count: 5
table_count: 14
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=22"
---

---
title: <span id="_Toc412805077" class="anchor"></span>Patient Data Exchange (PDX) Technical Manual
---

![](pdx-v-1-5-technical-manual/001.png)

Office of Information and Technology (OI&T)

Software Version 1.5

Original Software Release: November 1993

Revised Documentation Release: October 2023

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 48%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/16/2023</td>
<td>5.0</td>
<td>VAQ*1.5*46:<br />
Added <a href="#VAQUTL1">VAQUTL50</a> to the PDX Routine List<br />
<br />
Removed the prefixes (chapter number, glossary, index) from each page number. Deleted the index but kept all the index entries, which will enable the index to be rebuilt if necessary.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>02/27/2015</td>
<td>4.0</td>
<td>Converted document to MS-Word 2007 format and incorporated <em><u>some</u></em> format changes from the ProPath User Guide Template.</td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="odd">
<td>01/11/2005</td>
<td>3.0</td>
<td><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="even">
<td>09/27/2004</td>
<td>2.0</td>
<td><p>Reformatted document to follow ISS styles and guidelines, no other content updates made.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: PDXPATIENT,[N] or PDXUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., PDXPATIENT, ONE, PDXPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul></td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="odd">
<td>11/1993</td>
<td>1.0</td>
<td>Initial Patient Data Exchange V. 1.5 software documentation creation.</td>
<td>Albany, NY OIFO</td>
</tr>
</tbody>
</table>

Contents

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the Patient Data Exchange (PDX) software within Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure and Security Services (ISS) software products.

The Patient Data Exchange (PDX) Technical manual is comprised of discrete sections which detail various technical characteristics of the VistA PDX software. This manual was produced to provide necessary information for use in the technical operation of the PDX software, V. 1.5. It should be noted that this manual is intended for use by technical computer personnel and is not designed for use by the typical end user.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

| Symbol                                                                                                            | Description                                                                                          |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-technical-manual/002.png)    | Used to inform the reader of general information including references to additional reading material |
| ![](pdx-v-1-5-technical-manual/003.png) | Used to caution the reader to take special notice of critical information                            |

<span id="_Ref6202021" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

| ![](pdx-v-1-5-technical-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

| ![](pdx-v-1-5-technical-manual/005.png) | Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

| ![](pdx-v-1-5-technical-manual/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|

Help at Prompts

VistA software provides online help and commonly used system default prompts. In character-based mode, users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

| ![](pdx-v-1-5-technical-manual/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- M programming language

It provides an overall explanation of the use of the Patient Data Exchange (PDX) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the VHA OI Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> REDACTED

Reference Materials

Readers who wish to learn more about Patient Data Exchange (PDX) documentation should consult the following:

- *Patient Data Exchange (PDX) Installation Guide & Release Notes*
- *Patient Data Exchange (PDX) Technical Manual* (this manual)
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
<thead>
<tr class="header">
<th>![](pdx-v-1-5-technical-manual/008.png)</th>
<th><p>For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](pdx-v-1-5-technical-manual/009.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
    - [Namespace Conventions](#namespace-conventions)
    - [Integrity Checker](#integrity-checker)
    - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
    - [Resource Requirements](#resource-requirements)
- [Routines](#routines)
    - [Routines to Map](#routines-to-map)
    - [Callable Routines](#callable-routines)
    - [Routine List with Descriptions](#routine-list-with-descriptions)
- [Files](#files)
    - [File List](#file-list)
    - [File Descriptions](#file-descriptions)
    - [File Flow Chart](#file-flow-chart)
    - [| File Name (#)                 | Points To (File & \#)         | Pointed To By (File & \#) |](#file-name-points-to-file-pointed-to-by-file)
    - [Templates](#templates)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
- [External/Internal Relations](#externalinternal-relations)
    - [External Relations](#external-relations)
    - [Internal Relations](#internal-relations)
- [Software-wide Variables](#software-wide-variables)
    - [Key Variables](#key-variables)
  - [Glossary](#glossary)
The Patient Data Exchange (PDX) software is designed to manage the transfer of patient information (demographics, episodes of care, medications, and diagnostic evaluations) between VA facilities using the MailMan electronic mail utility. Once transferred, this information may be combined with pertinent local information and assembled into a coherent composite record.
Requests for PDX data can be processed manually or automatically. For requests to be processed manually, the site would have to be a member of the Release Group and meet the requirements for automatic processing. Records determined to be "sensitive" and those which exceed the maximum time and occurrence limits for Health Summary components may not be returned automatically and will be held for manual processing.
PDX V. 1.5 uses the List Manager utility extensively. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.
The software provides numerous system reports (current transactions and work- load) that allow predefined and customizable sorts.
Options
The Following is a brief description of the major options and menus contained in the PDX software:
- Request PDX for Patient—This option is used to electronically request PDX data for a selected patient from another VA facility(s).
- Unsolicited PDX—This option is used to send PDX information to a remote site without having first received a request.
- Process External PDX—This option is used to process PDX requests received from other VA facilities that do not meet the criteria for automatic processing.
- Load/Edit PDX Data—This option allows you to load or edit data fields in your PATIENT file with data from your PDX file.
- Display PDX Data Menu—This menu allows you to display or print PDX data for a selected patient by either transaction or user who requested the information.
- System Reports Menu:
  - Requires Processing Report—This option is used to print a report of all PDX requests that require manual processing.
  - Current Transactions Report Menu—The options on this menu allow you to print reports of PDX transactions on file by several different sorting methods.
  - Workload Reports Menu—The options on this menu allow you to print workload reports of PDX transactions on file by several different sorting methods.
- PDX Edit Files Menu:
  - Add/Edit Fields to Encrypt—This option provides the ability to encrypt selected data fields in the PDX transmission.
  - Edit Maximum Limits for Automatic Processing—This option is used to edit the maximum time and occurrence limits that your site is willing to allow for automatic processing of a PDX transaction.
  - Add/Edit Outgoing Group—This option is used to create outgoing groups and add/edit/delete remote facilities in those groups.
  - Edit Parameter File—This option is used to set up site specific PDX parameters.
  - Add/Edit Segment Group Options—These three options are used to create segment groups (selected group of data segments).
  - Add/Edit Release Group—This option is used to enter/edit facilities into the release group for automatic processing of PDX requests.
- Purging Menu—These three options provide purging capabilities by default age, user defined age, or user defined date.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users of the PDX software must set up an electronic signature in order to utilize the software. This can be accomplished through the Edit Electronic Signature Code option of the User's Toolbox menu.

As an optional security measure, this software provides the ability to encrypt data using existing data encryption methods. Sites wishing to encrypt certain fields will have to turn the flag on through the Edit Parameter File option and add those fields to the ENCRYPTED FIELD file (#394.73).

All site specific parameters can be established through the Edit Parameter File option of the PDX Edit Files menu.

| ![](pdx-v-1-5-technical-manual/010.png) | For further instruction on implementation of this software, including the setup of the release group and mail groups, please refer to the "Installation Guide" section in the *PDX Release Notes & Installation Guide*. |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the PDX software is VAQ.

### Integrity Checker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VAQNTEG routine checks integrity for other PDX routines.

### SACC Exemptions/Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC exemptions or non-standard code in the PDX software.

### Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites will see growth in the following 3 PDX files.

- VAQ - Transaction file (394.61) 200 bytes per entry\*
- VAQ - Data file (394.62) 50 bytes per entry\*
- VAQ - Workload file (394.87) 110 bytes per entry\*

\*Since variable fields are in these records, average record size was determined by sampling test sites.

It was determined that a single transaction on average will generate 185 data records. This was determined by taking the total number of entries in the VAQ - DATA file and dividing by the total number of entries in the VAQ - TRANSACTION file.

Disk storage requirements are estimated at approximately 10K per transaction. This was determined by taking the 185 data records at 50 bytes each plus a single transaction record at 200 bytes plus a variable number of workload records at 110 bytes each and dividing the total by 1024 bytes.

Global Growth can be controlled by the purge features of PDX.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines to map in the PDX software.

### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \$\$PDX^VAQUIN01

Description

This API can be used for both request and unsolicited request. It utilizes time and occurrence limits for Health Summary, which are pieces on the segment root array. These pieces need to be set by the developer. If these are not included, the defaults in the site's VAQ - PARAMETER file (#394.81) will be used.

Required Variables

> VAQOPT REQ = request, UNS = unsolicited

> VAQDFN IFN of patient in PATIENT file (#2)

> VAQNM Name of patient

> VAQISSN Patient Social Security Number (no dashes)

> VAQIDOB Patient's Date of Birth (external format)

> DOMROOT Array of domains (full global reference)

> SEGROOT Array of segments (full global reference)

> NOTROOT Array of who to notify (only used for request)

> TLIMIT Time limit for Health Summary

> OLIMIT Occurrence limit for Health Summary

External Calls

- LDREQ^VAQREQ06
- LDUNS^VAQREQ06
- PID^VADPT6
- WORKDONE^VAQADS01

Example

> S X=\$\$PDX^VAQUIN01("REQ",DFN,,,,DOMROOT,SEGROOT)

> S X=\$\$PDX^VAQUIN01("UNS",,"PATIENT NAME","123549898",,DOMROOT,SEGROOT)

### Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of routines associated with the PDX software, excluding pre- and post-init routines:

| Routine                                                                                                            | Description                                                                       |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| VAQADM2, VAQADM21                                                                                                      | PDX server main entry point                                                           |
| vaqadm22                                                                                                               | Automatic processing of results                                                       |
| vaqadm23                                                                                                               | Check segments against maximum limits for automatic processing.                       |
| vaqadm5                                                                                                                | Generate PDX transmissions                                                            |
| vaqadm50, vaqadm51                                                                                                     | Main entry point for generating PDX transmissions                                     |
| VAQADS01                                                                                                               | Logs work being done by PDX                                                           |
| VAQAUT                                                                                                                 | User authentication routine                                                           |
| VAQBUL, VAQBUL01, VAQBUL02, VAQBUL03, VAQBUL04, VAQBUL05, VAQBUL06, VAQBUL07                                           | Builds and sends bulletins                                                            |
| VAQCON, VAQCON0                                                                                                        | Build message for transaction                                                         |
| VAQCON1                                                                                                                | Create stub MailMan message                                                           |
| VAQCON2                                                                                                                | Determines MailMan sender                                                             |
| VAQCON3                                                                                                                | Construct user block                                                                  |
| VAQCON4                                                                                                                | Construct domain block                                                                |
| VAQCON5                                                                                                                | Construct segment block                                                               |
| VAQCON6                                                                                                                | Construct patient block                                                               |
| VAQCON7                                                                                                                | Construct data block                                                                  |
| VAQCON8                                                                                                                | Construct display block                                                               |
| VAQCON93, VAQCON94                                                                                                     | Builds and sends PDX V. 1.0 message                                                   |
| VAQCON95                                                                                                               | Builds a pharmacy PDX V. 1.0 message                                                  |
| VAQCON96                                                                                                               | Builds a PIMS PDX V. 1.0 message                                                      |
| VAQCON97, VAQCON98                                                                                                     | Builds a data block for PDX V. 1.0 message                                            |
| VAQCON99                                                                                                               | Builds a header block for PDX V. 1.0 message                                          |
| VAQDBI                                                                                                                 | Extract data segments contained in a PDX transaction                                  |
| VAQDBIH1                                                                                                               | Determines if PDX segment is Health Summary component                                 |
| VAQDBIH2                                                                                                               | Validates time limits of Health Summary component                                     |
| VAQDBIH3                                                                                                               | Determines if PDX segment is Health Summary component (without FM calls)              |
| VAQDBII1                                                                                                               | Holds references to PDX extracted data                                                |
| VAQDBIM, VAQDBIM0                                                                                                      | Extract Means Test data                                                               |
| VAQDBIM1                                                                                                               | Extract Means Test data, screen 1                                                     |
| VAQDBIM2                                                                                                               | Extract Means Test data, screen 2                                                     |
| VAQDBIM3                                                                                                               | Extract Means Test data, screen 3                                                     |
| VAQDBIM4                                                                                                               | Extract Means Test data, screen 4                                                     |
| VAQDBIP                                                                                                                | Extracts PDX information                                                              |
| VAQDBIP1, VAQDBIP2, VAQDBIP5, VAQDBIP8                                                                                 | Extracts PDX pharmacy information                                                     |
| VAQDBIP3                                                                                                               | Extracts PIMS minimum patient dataset information                                     |
| VAQDBIP4, VAQDBIP6, VAQDBIP7                                                                                           | Extracts PIMS registration information                                                |
| VAQDIS01                                                                                                               | Display minimal data                                                                  |
| VAQDIS10                                                                                                               | Display PDX by patient                                                                |
| VAQDIS11                                                                                                               | Selection screen for display by patient                                               |
| VAQDIS12                                                                                                               | Selection screen for display by requestor                                             |
| VAQDIS15                                                                                                               | Display segments for display                                                          |
| VAQDIS16                                                                                                               | General display for all segments                                                      |
| VAQDIS17                                                                                                               | Device selector for display                                                           |
| VAQDIS20                                                                                                               | Sets up state and county variables                                                    |
| VAQDIS21                                                                                                               | Builds display array for minimal data                                                 |
| VAQDIS22, VAQDIS23, VAQDIS24, VAQDIS25, VAQDIS26, VAQDIS27, VAQDIS28, VAQDIS29, VAQDIS30, VAQDIS31, VAQDIS32, VAQDIS33 | Builds display array for PIMS data                                                    |
| VAQDIS40, VAQDIS41, VAQDIS42, VAQDIS43                                                                                 | Builds display array for pharmacy data                                                |
| VAQEXT01, VAQEXT06                                                                                                     | Builds array for manual processing                                                    |
| VAQEXT02, VAQEXT04                                                                                                     | Displays array for manual processing                                                  |
| VAQEXT03                                                                                                               | Process manual PDX transactions                                                       |
| VAQEXT05                                                                                                               | Checks time and occurrence limits for manual processing                               |
| VAQFIL10, VAQFIL11                                                                                                     | Files header block                                                                    |
| VAQFIL12                                                                                                               | Files domain block                                                                    |
| VAQFIL13                                                                                                               | Files user block                                                                      |
| VAQFIL14                                                                                                               | Files comment block                                                                   |
| VAQFIL15                                                                                                               | Files patient block                                                                   |
| VAQFIL16                                                                                                               | Files segment block                                                                   |
| VAQFIL17                                                                                                               | Files display block                                                                   |
| VAQFIL18                                                                                                               | Files all data block                                                                  |
| VAQFILE                                                                                                                | Creates a stub entry in the VAQ - TRANSACTION file                                    |
| VAQFILE1                                                                                                               | Performs add/edit/delete functions on VAQ - DATA file                                 |
| VAQHSH                                                                                                                 | Encrypt a display array                                                               |
| VAQHSH1                                                                                                                | Encrypt/decrypt routines                                                              |
| VAQINITY                                                                                                               | Send install message                                                                  |
| VAQLED01                                                                                                               | Load/edit status screen                                                               |
| VAQLED02                                                                                                               | Sets up differences between PDX and local data base                                   |
| VAQLED03                                                                                                               | Display possible matches screen                                                       |
| VAQLED04                                                                                                               | Creates compare arrays for load/edit                                                  |
| VAQLED05                                                                                                               | Load/edit differences screen                                                          |
| VAQLED07                                                                                                               | Display minimal data, add new patient                                                 |
| VAQLED09                                                                                                               | Load/edit help messages                                                               |
| VAQLED10                                                                                                               | Prompts for patient in load/edit                                                      |
| VAQNTEG, VAQNTEG0                                                                                                      | Integrity routines                                                                    |
| VAQPAR1, VAQPAR10                                                                                                      | Preparse PDX V. 1.0 transmission                                                      |
| VAQPAR11                                                                                                               | Parses data block for PDX V. 1.0 message                                              |
| VAQPAR6, VAQPAR60                                                                                                      | Parses PDX V. 1.0 transmission                                                        |
| VAQPAR61                                                                                                               | Parses PDX V. 1.5 message block                                                       |
| VAQPSE01                                                                                                               | PDX Health Summary driver                                                             |
| VAQPSE02, VAQPSE03                                                                                                     | Extract Means Test billing data for PDX                                               |
| VAQPSE04                                                                                                               | Build display set for extracted PDX billing data                                      |
| VAQPSL, VAQPSL1, VAQPLS2, VAQPSL3                                                                                      | List Manager routines created from list templates                                     |
| VAQPUR, VAQPUR10, VAQPUR11                                                                                             | Purging routines                                                                      |
| VAQREQ01                                                                                                               | Request patient data status screen                                                    |
| VAQREQ02                                                                                                               | Request patient data request screen                                                   |
| VAQREQ03                                                                                                               | Request patient data, ask domain/segment                                              |
| VAQREQ04                                                                                                               | Request patient data, ask segment                                                     |
| VAQREQ05                                                                                                               | Request PDX record, copy domain                                                       |
| VAQREQ06                                                                                                               | Transmit data to VAQ - TRANSACTION file                                               |
| VAQREQ07                                                                                                               | Create notify list, request screen                                                    |
| VAQREQ08                                                                                                               | Comment for unsolicited request                                                       |
| VAQREQ09                                                                                                               | Request patient data help messages                                                    |
| VAQREQ10                                                                                                               | Prompts for patient for request and unsolicited request                               |
| VAQREQ11                                                                                                               | Prompts and checks for time and occurrence limits for request and unsolicited request |
| VAQUIN01                                                                                                               | Programmer entry point for sending PDX requests (API)                                 |
| VAQUPD1                                                                                                                | Recreates all extraction arrays for a transaction                                     |
| VAQUPD2                                                                                                                | Builds display for all segments and transactions                                      |
| VAQUPD25                                                                                                               | Pulls extraction array out of VAQ - DATA file                                         |
| VAQUTL1, VAQUTL2, VAQUTL3, VAQUTL4, VAQUTL50, VAQUTL92, VAQUTL93, VAQUTL94                                             | Utility routines                                                                      |
| VAQUTL95                                                                                                               | Sets commonly used variables                                                          |
| VAQUTL96                                                                                                               | PDX transaction lookup                                                                |
| VAQUTL97                                                                                                               | PDX patient lookup                                                                    |
| VAQUTL98                                                                                                               | Builds various tables                                                                 |
| VAQUTL99                                                                                                               | Various function calls                                                                |
| VAQXRF1, VAQXRF2, VAQXRF3                                                                                              | Builds MUMPS cross-references for PDX files                                           |

Used for formatting only

<span id="_Toc144933379" class="anchor"></span>Figure 3‑1: PDX routine list<span id="VAQUTL1" class="anchor"></span>

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Number             | File Name                    | Global   |
|-----------------------------|----------------------------------|--------------|
| 394                         | <sup>\*</sup>PDX TRANSACTION | ^VAT(394,    |
| 394.1                       | <sup>\*</sup>PDX DATA        | ^VAT(394.1,  |
| 394.2                       | <sup>\*</sup>PDX PARAMETER   | ^VAT(394.2,  |
| 394.3<sup>\*\*\*</sup>  | <sup>\*</sup>PDX STATUS      | ^VAT(394.3,  |
| 394.4                       | \*PDX STATISTICS                 | ^VAT(394.4,  |
| 394.61                      | VAQ - TRANSACTION                | ^VAT(394.61, |
| 394.62                      | VAQ - DATA                       | ^VAT(394.62, |
| 394.71<sup>\*\*\*</sup> | VAQ - DATA SEGMENT               | ^VAT(394.71, |
| 394.72<sup>\*\*\*</sup> | VAQ - ENCRYPTION METHOD          | ^VAT(394.72, |
| 394.73<sup>\*\*\*</sup> | VAQ - ENCRYPTED FIELDS           | ^VAT(394.73, |
| 394.81                      | VAQ - PARAMETER                  | ^VAT(394.81, |
| 394.82                      | VAQ - RELEASE GROUP              | ^VAT(394.82, |
| 394.83                      | VAQ - OUTGOING GROUP             | ^VAT(394.83, |
| 394.84                      | VAQ - SEGMENT GROUP              | ^VAT(394.84, |
| 394.85<sup>\*\*\*</sup> | VAQ - STATUS                     | ^VAT(394.85, |
| 394.86                      | VAQ - AUTO-NUMBERING             | ^VAT(394.86, |
| 394.87                      | VAQ - WORKLOAD                   | ^VAT(394.87, |
| 394.88<sup>\*\*\*</sup> | VAQ - WORK                       | ^VAT(394.88, |

Used for formatting only

<span id="_Toc144933380" class="anchor"></span>Figure 4‑1: PDX file list

<sup>\*</sup>Starred for deletion

<sup>\*\*\*</sup>File comes with data which will overwrite existing data, if specified

### File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VAQ - Transaction File (#394.61)

This file holds information describing each PDX transaction.

#### VAQ - Data File (#394.62)

This file holds the patient information passed through PDX.

#### VAQ - Data Segment File (#394.71)

This file defines each data segment currently supported by PDX.

#### VAQ - Encryption Method File (#394.72)

This file defines each encryption method currently supported by PDX.

#### VAQ - Encrypted Fields File (394.73)

This file contains all fields that should be encrypted in PDX Requests and Unsolicited PDXs transmitted by the facility. This file is only relevant when encryption has been turned on.

#### VAQ - Parameter File (#394.81)

This file contains site specific information concerning the use of PDX.

#### VAQ - Release Group File (#394.82)

This file contains the facilities that have been granted "automatic processing". In order for a request to be automatically processed, the requesting facility must have an entry in this file.

#### VAQ - Outgoing Group File (#394.83)

This file contains groups of facilities commonly accessed using PDX.

#### VAQ - Segment Group File (#394.84)

This file contains groups of data segments commonly referenced by the facility. Groups marked as Public may be referenced by all users of PDX. Groups marked as Private may only be referenced by the individual that created the group.

#### VAQ - Status File (#394.85)

This file defines all possible statuses of a PDX transaction.

#### VAQ - Auto-Numbering File (#394.86)

This file is used to implement auto-numbering in the PDX files. Fields with auto-numbering capability will have an entry in this file.

#### VAQ - WorkLoad File (#394.87)

This file contains statistics concerning the workload done using PDX. PDX workload is considered to be requesting patient information from another facility, manually processing requests from another facility, and uploading PDX data to the Patient File. Work done by the PDX Server is also stored in this file.

#### VAQ - Work File (#394.88)

This file contains the type of work being tracked by the VAQ - WORKLOAD file.

### File Flow Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### | File Name (#)                 | Points To (File & \#)         | Pointed To By (File & \#) |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----------------------------------|-----------------------------------|-------------------------------|
| \*PDX TRANSACTION (#394)          | PATIENT (#2)                      | \*PDX DATA (#394.1)           |
|                                   | \*PDX STATUS (#394.3)             |                               |
| \*PDX DATA (#394.1)               | \*PDX TRANSACTION (#394)          | NA                            |
| \*PDX PARAMETER (#394.2)          | INSTITUTION (#4)                  | NA                            |
|                                   | DOMAIN (#4.2)                     |                               |
| \*PDX STATUS (#394.3)             | NA                                | \*PDX TRANSACTION (#394)      |
|                                   |                                   | \*PDX STATISTICS (#394.4)     |
| \*PDX STATISTICS (#394.4)         | PATIENT (#2)                      | NA                            |
|                                   | \*PDX STATUS (#394.3)             |                               |
| VAQ – TRANSACTION (#\$394.61)     | PATIENT (#2)                      | VAQ – DATA (#394.62)          |
|                                   | NEW PERSON (#200)                 |                               |
|                                   | VAQ - DATA SEGMENT (#394.71)      |                               |
|                                   | VAQ - ENCRYPTION METHOD (#394.72) |                               |
|                                   | VAQ – STATUS (#394.85)            |                               |
|                                   | VAQ - AUTO-NUMBERING (#394.86)    |                               |
| VAQ – DATA (#394.62)              | VAQ – TRANSACTION (#394.61)       | NA                            |
|                                   | VAQ - DATA SEGMENT (#394.71)      |                               |
|                                   | VAQ - AUTO-NUMBERING (#394.86)    |                               |
| VAQ - DATA SEGMENT (#394.71)      | HEALTH SUMMARY COMPONENT (#142.1) | VAQ – TRANSACTION (#394.61)   |
|                                   |                                   | VAQ – DATA (#394.62)          |
|                                   |                                   | VAQ - SEGMENT GROUP (#394.84) |
|                                   |                                   | VAQ – WORKLOAD (#394.87)      |
| VAQ - ENCRYPTION METHOD (#394.72) | NA                                | VAQ – TRANSACTION (#394.61)   |
|                                   |                                   | VAQ – PARAMETER (#394.81)     |
| VAQ - ENCRYPTED FIELDS (#394.73)  | VAQ - AUTO-NUMBERING (#394.86)    | NA                            |
| VAQ – PARAMETER (#394.81)         | INSTITUTION (#4)                  | NA                            |
|                                   | DOMAIN (#4.2)                     |                               |
|                                   | VAQ - ENCRYPTION METHOD (#394.72) |                               |
| VAQ - RELEASEGROUP (#394.82)      | INSTITUTION (#4)                  | NA                            |
|                                   | DOMAIN (#4.2)                     |                               |
|                                   | NEW PERSON (#200)                 |                               |
| VAQ – OUTGOING GROUP (#394.83)    | INSTITUTION (#4)                  | NA                            |
|                                   | DOMAIN (#4.2)                     |                               |
|                                   | NEW PERSON (#200)                 |                               |
| VAQ – SEGMENT GROUP (#394.84)     | NEW PERSON (#200)                 | NA                            |
|                                   | VAQ - DATA SEGMENT (#394.71)      |                               |
| VAQ – STATUS (#394.85)            | NA                                | VAQ – TRANSACTION (#394.61)   |
| VAQ - AUTO-NUMBERING (#394.86)    | NA                                | NA                            |
| VAQ – WORKLOAD (#394.87)          | PATIENT (#2)                      | NA                            |
|                                   | NEW PERSON (#200)                 |                               |
|                                   | VAQ - DATA SEGMENT (#394.71)      |                               |
|                                   | VAQ – WORK (#394.88)              |                               |
| VAQ – WORK (#394.88)              | NA                                | VAQ – WORKLOAD (#394.87)      |

Used for formatting only

<span id="_Toc144933381" class="anchor"></span>Figure 4‑2: PDX file flowchart

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Input Templates

| File# | Template            | Description                          |
|-----------|-------------------------|------------------------------------------|
| 394.71    | VAQ EDIT FILE           | Enter maximum time and occurrence limits |
| 394.73    | VAQ EDIT FILE           | Enter VAQ - ENCRYPTED FIELDS file data   |
| 394.81    | VAQ EDIT FILE           | Enter VAQ - PARAMETER file data          |
| 394.82    | VAQ EDIT FILE           | Enter VAQ - RELEASE GROUP file data      |
| 394.83    | VAQ EDIT FILE           | Enter VAQ - OUTGOING GROUP file data     |
| 394.84    | VAQ EDIT FILE           | Enter segment group data                 |
|           | VAQ EDIT FILE (PRIVATE) | Enter segment group data (private)       |
|           | VAQ EDIT FILE (PUBLIC)  | Enter segment group data (public)        |

Used for formatting only

<span id="_Toc144933382" class="anchor"></span>Figure 4‑3: PDX Input templates

#### Print Templates

| File# | Template                   | Description                      |
|-----------|--------------------------------|--------------------------------------|
| 394.61    | VAQ CUR. TRANSACTIONS REPORT   | Generates current transaction report |
|           | VAQ REQUIRES PROCESSING REPORT | Generates requires processing report |
| 394.71    | VAQ DATA SEGMENT LIST          | Generates data segment listing       |
| 394.87    | VAQ WORK-LOAD REPORT           | Generates workload report            |

Used for formatting only

<span id="_Toc144933383" class="anchor"></span>Figure 4‑4: PDX Print templates

#### Sort Templates

| File# | Template                   | Description                                                                         |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------|
| 394.61    | VAQ REQUIRES PROCESSING        | Sorts transactions by transaction number of those transactions that requires processing |
|           | VAQ TRANSACTIONS BY AUTHORIZER | Sorts transactions by authorizer                                                        |
|           | VAQ TRANSACTIONS BY DATE SENT  | Sorts transactions by date and time of request                                          |
|           | VAQ TRANSACTIONS BY FACILITY   | Sorts transactions by authorizing site                                                  |
|           | VAQ TRANSACTIONS BY PATIENT    | Sorts transactions by patient                                                           |
|           | VAQ TRANSACTIONS BY RECEIPT    | Sorts transactions by date and time of reply                                            |
|           | VAQ TRANSACTIONS BY REQUESTOR  | Sorts transactions by requestor                                                         |
|           | VAQ TRANSACTIONS BY STATUS     | Sorts transactions by current status                                                    |
| 394.87    | VAQ WORK-LOAD BY DATE          | Sorts type of work by date                                                              |
|           | VAQ WORK-LOAD BY FACILITY      | Sorts type of work by remote facility                                                   |
|           | VAQ WORK-LOAD BY PATIENT       | Sorts type of work by patient                                                           |
|           | VAQ WORK-LOAD BY WORK          | Sorts type of work by type of work                                                      |

Used for formatting only

<span id="_Toc144933384" class="anchor"></span>Figure 4‑5: PDX Sort templates

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Data Exchange (VAQ (MENU) MAIN)

> \|

> \|

> --DIS Display PDX Data -------------------------------TRN Display PDX by

> \[VAQ (MENU) Transaction \[VAQ

> DISPLAY PDX\] PDX DISPLAY

> \| (TRN)\]

> \|

> \|------------------------------------------USER Display PDX by

> User \[VAQ PDX

> DISPLAY (USER)\]

> --EDT PDX Edit Files ---------------------------------ENC Add/Edit Fields

> \[VAQ (MENU) EDIT to Encrypt \[VAQ

> FILES\] (EDIT) ENCRY

> \| FIELDS\]

> \| \*\*LOCKED: VAQ

> \| EDIT FILE\*\*

> \|

> \|-------------------------------------------MAX Edit maximum

> \| limits for

> \| automatic

> \| processing \[VAQ

> \| (EDIT) MAX

> \| LIMITS\]

> \| \*\*LOCKED: VAQ

> \| EDIT FILE\*\*

> \|

> \|-------------------------------------------OUT Add/Edit

> \| Outgoing Group

> \| \[VAQ (EDIT)

> \| OUTGOING GROUP\]

> \|

> \|-------------------------------------------PAR Edit Parameter

> \| File \[VAQ (EDIT)

> \| PARAMETER\]

> \| \*\*LOCKED: VAQ

> \| EDIT FILE\*\*

> \|

> \|------------------------------------------PRIV Add/Edit Segment

> \| Group - Private

> \| \[VAQ (EDIT)

> \| SEGMENT GRP -

> \| PRIV\]

> \|

> \|------------------------------------------PUBL Add/Edit Segment

> \| Group - Public

> \| \[VAQ (EDIT)

> \| SEGMENT GRP -

> \| PUBL\]

> \| \*\*LOCKED: VAQ

> \| EDIT FILE\*\*

> \|

> \|-------------------------------------------REL Add/Edit Release

> \| Group \[VAQ

> \| (EDIT) RELEASE

> \| GROUP\]

> \| \*\*LOCKED: VAQ

> \| EDIT FILE\*\*

> \|

> \|-------------------------------------------SEG Add/Edit Segment

> Group - All \[VAQ

> (EDIT) SEGMENT

> GRP - ALL\]

> \*\*LOCKED: VAQ

> EDIT FILE\*\*

> -------------------------------------------------------LD Load/Edit PDX

> Data \[VAQ PDX

> LOAD/EDIT\]

> \*\*LOCKED: VAQ

> LOAD\*\*

> -PRGE Purging \[VAQ ----------------------------------DFLT Purge using

> (MENU) PURGING\] default age \[VAQ

> \*\*LOCKED: VAQ PDX PURGE\]

> PURGE\*\*

> \|

> \|-------------------------------------------AGE Purge using user

> \| defined age \[VAQ

> \| PURGE BY ENTERED

> \| LIFE\]

> \|

> \|------------------------------------------DATE Purge using user

> defined date

> \[VAQ PURGE BY

> ENTERED DATE\]

> ------------------------------------------------------PRO Process External

> PDX \[VAQ PDX

> PROCESS

> EXTERNAL\]

> ------------------------------------------------------REQ Request PDX for

> Patient \[VAQ PDX

> REQUEST\]

> -RPRT System Reports --------------------------------PROC Requires

> \[VAQ (MENU) Processing

> SYSTEM REPORTS\] Report \[VAQ

> \*\*LOCKED: VAQ REQUIRES

> RPT\*\* PROCESSING\]

> \|

> \|----------------TRAN Current --------------FAC Sort by remote

> \| Transactions facility \[VAQ

> \| Report \[VAQ TRANSACTIONS BY

> \| (MENU) CUR FACILITY\]

> \| TRANSACTIONS\]

> \| \|

> \| \|----------------GNRT Sort by user

> \| \| that generated

> \| \| request \[VAQ

> \| \| TRANSACTIONS BY

> \| \| REQUESTOR\]

> \| \|

> \| \|-----------------PAT Sort by

> \| \| patient's name

> \| \| \[VAQ

> \| \| TRANSACTIONS BY

> \| \| PATIENT\]

> \| \|

> \| \|----------------RCVD Sort by date

> \| \| received \[VAQ

> \| \| TRANSACTIONS BY

> \| \| RECEIPT\]

> \| \|

> \| \|----------------RLSD Sort by user

> \| \| that released

> \| \| information \[VAQ

> \| \| TRANSACTIONS BY

> \| \| AUTHORIZER\]

> \| \|

> \| \|----------------SENT Sort by

> \| \| requesting date

> \| \| \[VAQ

> \| \| TRANSACTIONS BY

> \| \| DATE SENT\]

> \| \|

> \| \|----------------STAT Sort by status

> \| \| of transaction

> \| \| \[VAQ

> \| \| TRANSACTIONS BY

> \| \| STATUS\]

> \| \|

> \| \|----------------USER Sort criteria

> \| defined by user

> \| \[VAQ

> \| TRANSACTIONS

> \| USER DEFINED\]

> \| \*\*LOCKED: VAQ

> \| RPT USER\*\*

> \|

> \|

> \|----------------WORK Workload ------------DATE Sort by date

> Reports \[VAQ \[VAQ WORKLOAD BY

> (MENU) DATE\]

> WORKLOAD\]

> \|

> \|-----------------FAC Sort by remote

> \| facility \[VAQ

> \| WORKLOAD BY

> \| FACILITY\]

> \|

> \|-----------------PAT Sort by

> \| patient's name

> \| \[VAQ WORKLOAD BY

> \| PATIENT\]

> \|

> \|----------------USER Sort criteria

> \| defined by user

> \| \[VAQ WORKLOAD

> \| USER DEFINED\]

> \| \*\*LOCKED: VAQ

> \| RPT USER\*\*

> \|

> \|----------------WORK Sort by type of

> work done \[VAQ

> WORKLOAD BY

> WORK\]

> ------------------------------------------------------UNS Unsolicited PDX

> \[VAQ PDX

> UNSOLICITED\]

<span id="_Toc144933385" class="anchor"></span>Figure 5‑1: Exported options—Generated Menu Tree

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving capabilities in the PDX software.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three PDX purging options are available. They provide purging capabilities defined by default age, user defined age, or user defined date. The date the last status was assigned to the transaction is the date used in determining when transactions will be flagged for purging.

#### Purge using default age Option

This option is used to purge PDX transactions and their associated data based on the value found in the PDX parameter, LIFETIME OF DATA. The Purger automatically adds three days to the parameter value. Once transactions are older than this value, they are flagged for purging and automatically purged when this option is utilized. The recommended value for the LIFETIME OF DATA parameter is 15 days.

#### Purge using user defined age Option

This option is used to purge PDX transactions and their associated data based on an age entered by the user. The Purger automatically adds three days to the user-entered value. Once transactions are older than this value, they are flagged for purging and automatically purged when this option is utilized. The default value displayed with the prompt is the entry in the PDX site parameter, LIFETIME FOR DATA.

#### Purge using user defined date Option

This option is used to purge PDX transactions and their associated data based on a date entered by the user (date must be before three days ago). Transactions older than this value will be automatically purged when this option is utilized.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software versions or higher are required in order to install this version of PDX.

> Kernel 7.0

> VA FileMan 19.0

> VA MailMan 7.0

> PIMS 5.3

> Pharmacy 5.6

> Integrating Billing 1.5

> Health Summary 1.2

> OE/RR 1.96

> Allergy Tracking 2.2

### Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any PDX option in the OPTION file (#19) that is a menu option should be able to run independently provided the user has the appropriate keys and VA FileMan access.

# Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-wide variables in the PDX software.

### Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PDX System-wide Variables

> DFN internal entry number of the PATIENT file (#2).

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| DATA SEGMENT   | Comprised of Health Summary, Means Test, Copay, and specially created PDX components.                                                                                                                                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DOMAIN         | A facility's electronic mail address.                                                                                                                                                                                                                                                             |
| MNEMONIC       | A device or code intended to assist memory.                                                                                                                                                                                                                                                       |
| OUTGOING GROUP | A group of remote facilities. Creating outgoing groups allows for expeditious sending of PDX requests as they may be sent to all the facilities contained in the group with one entry, the outgoing group name.                                                                                   |
| PDX            | Patient Data Exchange                                                                                                                                                                                                                                                                             |
| RELEASE GROUP  | A group of sites defined in the VAQ - RELEASE GROUP file through FileMan. Requests for sites you enter in your release group will be processed automatically upon receipt. Conversely, your requests will be processed automatically by sites that have your site defined in their release group. |
| REMOTE SITE    | The facility with which your site is exchanging data. If you are requesting a PDX, the site you are requesting the data from would be the remote site. If you receive a request for a PDX, the site requesting the data would be the remote site.                                                 |
| SEGMENT GROUP  | A group of selected data segments.                                                                                                                                                                                                                                                                |
| TRANSACTION    | A number automatically assigned to a PDX request when the number message is originated and/or received.                                                                                                                                                                                           |
Used for formatting only
<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pdx-v-1-5-technical-manual/011.png)</th>
<th><p>For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/glossary.asp">http://vista.med.va.gov/iss/glossary.asp</a></p>
</blockquote>
<p>For a list of commonly used acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vista/med/va/gov/iss/acronyms/index.asp">http://vista/med/va/gov/iss/acronyms/index.asp</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
