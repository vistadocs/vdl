---
title: Network Health Exchange Version 5 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: AFJX
app_name: Network Health Exchange (NHE)
section: INF
app_status: active
pkg_ns: AFJX
patch_ver: 5
patch_id: AFJX*5
group_key: "AFJX:AFJX:5"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - health
  - network
  - class
  - routine
  - table
  - patient
  - exchange
  - contents
  - request
  - software
page_count: 0
word_count: 5737
section_count: 6
table_count: 26
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=79"
---

![](network-health-exchange-version-5-technical-manual/001.png)

NETWORK HEALTH EXCHANGE (NHE)TECHNICAL MANUAL

February 1996

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 41%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>02/1996</td>
<td>1.0</td>
<td>Initial Network Health Exchange V. 5.1 software documentation creation.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/18/05</td>
<td>2.0</td>
<td><p>Reformatted document to follow ISS styles and guidelines.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: MMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Revision History [iii](#revision-history)

Figures and Tables [vii](#figures-and-tables)

Orientation [ix](#orientation)

1\. Introduction [1-1](#introduction)

2\. Implementation and Maintenance [2-1](#implementation-and-maintenance)

Manager Menu [2-1](#manager-menu)

Site Management Functions [2-1](#site-management-functions)

3\. Routines [3-1](#routines)

4\. Files [4-1](#files)

File Security [4-1](#file-security)

5\. Exported Options [5-1](#exported-options)

Menus [5-1](#menus)

Menu Options [5-2](#menu-options)

User Menu [5-2](#user-menu)

Manager Menu [5-2](#manager-menu-1)

Site Management Functions [5-3](#site-management-functions-1)

Security Keys [5-3](#security-keys)

Special Security Features [5-3](#special-security-features)

6\. Cross-references [6-1](#cross-references)

7\. Archiving and Purging [7-1](#archiving-and-purging)

Archiving [7-1](#_Toc96838201)

Purging [7-1](#purging)

8\. Callable Routines [8-1](#callable-routines)

9\. External Relations [9-1](#external-relations)

Platform Requirements [9-1](#platform-requirements)

Minimum Requirements [9-1](#minimum-requirements)

Additional Requirements [9-1](#additional-requirements)

DBA Approvals and IAs [9-1](#dba-approvals-and-ias)

10\. Internal Relations [10-1](#internal-relations)

Namespace [10-1](#namespace)

File Numbers [10-1](#file-numbers)

11\. Software-wide Variables [11-1](#software-wide-variables)

Glossary Glossary-[1](#glossary)

Index Index-[1](#index)

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

This is the Technical Manual for the NHE software. It provides the necessary information for the technical operation of the software. It is intended for use by:

- The Site Manager/Information Resource Management (IRM) Service Chief
- ADP Application Coordinator (ADPAC)
- Other technical computer personnel

Throughout this manual, advice and instructions are offered regarding the use and implementation of the Network Health Exchange (NHE) software within Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure and Security Services (ISS) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                   |                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                        | Description                                                                                      |
| ![](network-health-exchange-version-5-technical-manual/002.png) | Used to inform the reader of general information including references to additional reading material |
| ![](network-health-exchange-version-5-technical-manual/003.png) | Used to caution the reader to take special notice of critical information                            |

<span id="_Ref6202021" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

|                                                   |                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/005.png) | Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                   |                                                                                                                            |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. In character-based mode, users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                   |                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- M programming language

It provides an overall explanation of the use of the Network Health Exchange (NHE) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the VHA OI Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> REDACTED

Reference Materials

Readers who wish to learn more about Infrastructure and Security Services (ISS) documentation should consult the following:

- *Network Health Exchange (NHE) Release Notes*
- *Network Health Exchange (NHE) Installation Guide*
- *Network Health Exchange (NHE) Technical Manual* (this manual)
- *Network Health Exchange (NHE) User Manual*
- The Network Health Exchange Home Page at the following Web address:

> REDACTED

> This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-technical-manual/008.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

VistA documentation can be downloaded from the Enterprise VistA Support (EVS) anonymous directories or from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

- Albany OIFO REDACTED
- Hines OIFO [REDACTED](ftp://ftp.fo-hines.med.va.gov)
- Salt Lake City OIFO REDACTED
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/009.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
    - [Manager Menu](#manager-menu)
    - [Site Management Functions](#site-management-functions)
- [Routines](#routines)
- [Files](#files)
    - [File Security](#file-security)
- [Exported Options](#exported-options)
    - [Menus](#menus)
    - [Menu Options](#menu-options)
    - [Security Keys](#security-keys)
    - [Special Security Features](#special-security-features)
- [Cross-references](#cross-references)
- [Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
    - [Platform Requirements](#platform-requirements)
    - [DBA Approvals and IAs](#dba-approvals-and-ias)
- [Internal Relations](#internal-relations)
    - [Namespace](#namespace)
    - [File Numbers](#file-numbers)
- [Software-wide Variables](#software-wide-variables)
  - [Glossary](#glossary)
  - [Index](#index)
Network Health Exchange (NHE) Version 5.1, a component of the Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA), is software that allows Veterans Affairs Medical Centers (VAMC)s to request either complete or pharmacy patient Health Summaries from each other. NHE was created by the Chicago Westside VAMC. This software is being released as an interim bridge to a more fully integrated clinical patient data exchange system.
Network Health Exchange (NHE) was developed at the Chicago Westside Veterans Affairs Medical Center (VAMC) and has evolved over several iterations. The Network Health Exchange is VistA software that provides clinicians with quick and easy access to patients' information from any site where they have been treated. NHE provides the computer mechanism for VAMC clinicians to retrieve clinical patient data from other medical centers. The requester is notified of returned patient data through an alert that appears with the VistA menu system. Patient data is displayed in a format similar to the integrated clinical reports found in Health Summary and can be viewed onscreen or printed.
The NHE software accesses several other VistA files which contain information concerning diagnoses, prescriptions, laboratory tests, radiology exams, hospital admissions, and clinic visits. This allows a clinical staff to take advantage of clinical data supported through VistA.
Network Health Exchange is based on the Health Summary software. However, NHE does not make calls to Health Summary so it is not necessary for a site to install Health Summary nor is familiarity with Health Summary required in order to use NHE.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Network Health Exchange (NHE) Manager menu and the Site Management functions contain the options necessary to administer the NHE software.

### Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manager menu contains options to add or edit sites in the station's VAMC NETWORK HEALTH EXCHANGE file (#537000), to inquire about messages requesting patient data, and to request or print patient data.

### Site Management Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Site Management functions nightly add patients to the VAMC NETWORK PATIENT file (#537010) and purge messages from the NETWORK,HEALTH EXCHANGE mail box. Three server functions process data requests, send an alert to the user when a request is complete, and add patients to the VAMC NETWORK PATIENT file (#537010). These functions are activated by directly accessing the utility or changing the time the routine is run.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains a list of the routines exported with the NHE software. A brief description of the function of each routine is included.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AFJXADHB</td>
<td>Brief NHE patient data request complete</td>
</tr>
<tr class="even">
<td>AFJXADHD</td>
<td>Process info and alert user</td>
</tr>
<tr class="odd">
<td>AFJXADPB</td>
<td>Brief pharmacy NHE patient data request complete</td>
</tr>
<tr class="even">
<td>AFJXALER</td>
<td>Request patient info—Allergy</td>
</tr>
<tr class="odd">
<td>AFJXALRT</td>
<td>Process info and alert user</td>
</tr>
<tr class="even">
<td>AFJXBLOO</td>
<td>Request patient info-Blood transfusions</td>
</tr>
<tr class="odd">
<td>AFJXCAH</td>
<td>Request patient info—Chem and Hematology</td>
</tr>
<tr class="even">
<td>AFJXCAHB</td>
<td>Brief NHE request patient info—Chem and Hem</td>
</tr>
<tr class="odd">
<td>AFJXCAHS</td>
<td>Request brief patient info—Chem and Hematology</td>
</tr>
<tr class="even">
<td>AFJXCYTO</td>
<td>Request patient info</td>
</tr>
<tr class="odd">
<td>AFJXDCS1</td>
<td>From Extract list of DS's with sig status</td>
</tr>
<tr class="even">
<td>AFJXDCSU</td>
<td>From Discharge Summary Component driver</td>
</tr>
<tr class="odd">
<td>AFJXDIE2</td>
<td>Request patient info—Diet</td>
</tr>
<tr class="even">
<td>AFJXDIET</td>
<td>Request patient info—Diet</td>
</tr>
<tr class="odd">
<td>AFJXDISA</td>
<td>Request patient info—Disabilities</td>
</tr>
<tr class="even">
<td>AFJXDM1</td>
<td>Request patient info—Demographics</td>
</tr>
<tr class="odd">
<td>AFJXEND</td>
<td>End of patient info—Demographics</td>
</tr>
<tr class="even">
<td>AFJXINST</td>
<td>Network health exchange install driver</td>
</tr>
<tr class="odd">
<td>AFJXLABO</td>
<td>Request patient info—Lab</td>
</tr>
<tr class="even">
<td>AFJXLRM</td>
<td>Request patient info—Micro</td>
</tr>
<tr class="odd">
<td>AFJXLRM1</td>
<td>Request patient info—Micro</td>
</tr>
<tr class="even">
<td>AFJXLROC</td>
<td>List cleanup</td>
</tr>
<tr class="odd">
<td>AFJXMABX</td>
<td>Print by section NHE</td>
</tr>
<tr class="even">
<td>AFJXMBOX</td>
<td>Search for previously completed Network Health Exchange requests</td>
</tr>
<tr class="odd">
<td>AFJXMEDI</td>
<td>Request patient info—Medicine Summary</td>
</tr>
<tr class="even">
<td>AFJXNTEG</td>
<td>Software checksum checker</td>
</tr>
<tr class="odd">
<td>AFJXORDR</td>
<td>Request patient info—Orders</td>
</tr>
<tr class="even">
<td>AFJXPATL</td>
<td><p>Sends data for VAMC NETWORK PATIENT file</p>
<p>D ^AFJXPATL will send data to be included in VAMC NETWORK PATIENT file to the sites you have added to the VAMC NETWORK HEALTH AUTHORIZED SITES file and for which you have filled in the fields for UPDATE NETWORK IDENTIFIER and the VAMC NETWORK PATIENT file. You will only get data from other sites if you fill in the field to accept their updates. You must answer YES for your own site to also get data added from its files to the VAMC NETWORK PATIENT file. Your own site data must be in this file so that all sites in your network area are synchronized.</p></td>
</tr>
<tr class="odd">
<td>AFJXPATS</td>
<td>Network health cross ref patient</td>
</tr>
<tr class="even">
<td>AFJXPHCY</td>
<td>Auto pharmacy complete</td>
</tr>
<tr class="odd">
<td>AFJXPHIV</td>
<td>Request patient info—Inpatient Pharm</td>
</tr>
<tr class="even">
<td>AFJXPNHA /RF/BC</td>
<td>Auto add patients to db &amp; update network id</td>
</tr>
<tr class="odd">
<td>AFJXPNHF</td>
<td>Print network health ex's for individual</td>
</tr>
<tr class="even">
<td>AFJXPNHI</td>
<td>Print completed network health ex's</td>
</tr>
<tr class="odd">
<td>AFJXPNHT</td>
<td>Get server message and automatically add patient to common db</td>
</tr>
<tr class="even">
<td>AFJXPNHX</td>
<td>Network health exchange message purge</td>
</tr>
<tr class="odd">
<td>AFJXPPED</td>
<td><p>VAMC NETWORK PATIENT file one-time cleanup</p>
<p>![](network-health-exchange-version-5-technical-manual/010.png) At installation, D ^AFJXPPED can be run to clean up theVAMC NETWORK PATIENT file (#537010) if the site has been running a previous version of Network Health Exchange.</p></td>
</tr>
<tr class="even">
<td>AFJXPUL2</td>
<td>Request patient info—Pulmonary function tests</td>
</tr>
<tr class="odd">
<td>AFJXPULM</td>
<td>Request patient info—Pulmonary function tests</td>
</tr>
<tr class="even">
<td>AFJXRADI</td>
<td>Request patient info—Radiology</td>
</tr>
<tr class="odd">
<td>AFJXRALT</td>
<td>Alert user</td>
</tr>
<tr class="even">
<td>AFJXRATS</td>
<td>Request patient info—Radiology</td>
</tr>
<tr class="odd">
<td>AFJXRIMP</td>
<td>Request patient info—Radiology impression</td>
</tr>
<tr class="even">
<td>AFJXSFAL</td>
<td>Server to send alert network health is complete</td>
</tr>
<tr class="odd">
<td>AFJXSPTH</td>
<td>Request patient info—Surgical Path</td>
</tr>
<tr class="even">
<td>AFJXSURY</td>
<td>Request patient info—Surgery</td>
</tr>
<tr class="odd">
<td>AFJXTEMA</td>
<td>One-time automatically add patient to db</td>
</tr>
<tr class="even">
<td>AFJXUNDS</td>
<td>Request patient info—Unit Dose</td>
</tr>
<tr class="odd">
<td>AFJXUNIT</td>
<td>Unit dose routine</td>
</tr>
<tr class="even">
<td>AFJXVISI</td>
<td>Request patient info—Appts</td>
</tr>
<tr class="odd">
<td>AFJXVITA</td>
<td>Request patient info—Vitals</td>
</tr>
<tr class="even">
<td>AFJXVITS</td>
<td>Request patient info—Vitals</td>
</tr>
<tr class="odd">
<td>AFJXWCBP</td>
<td>Request brief pharmacy patient information</td>
</tr>
<tr class="even">
<td>AFJXWCCW</td>
<td>Crisis Note/Clinical Warning</td>
</tr>
<tr class="odd">
<td>AFJXWCL1</td>
<td>Request patient info—Micro</td>
</tr>
<tr class="even">
<td>AFJXWCL2</td>
<td>Request patient info—Micro continued</td>
</tr>
<tr class="odd">
<td>AFJXWCL4</td>
<td>Request patient info—Adm Hist</td>
</tr>
<tr class="even">
<td>AFJXWCL5</td>
<td>Request patient info—ptf codes</td>
</tr>
<tr class="odd">
<td>AFJXWCL7</td>
<td>Request patient info—Adm</td>
</tr>
<tr class="even">
<td>AFJXWCL8</td>
<td>Request patient info—Adm</td>
</tr>
<tr class="odd">
<td>AFJXWCL9</td>
<td>Request patient info—Adm (cont)</td>
</tr>
<tr class="even">
<td>AFJXWCLI</td>
<td>Inquire to network health exchange</td>
</tr>
<tr class="odd">
<td>AFJXWCP1</td>
<td>Network health exchange request patient info</td>
</tr>
<tr class="even">
<td>AFJXWCP3</td>
<td>Inpatient meds</td>
</tr>
<tr class="odd">
<td>AFJXWCP4</td>
<td>Vitals</td>
</tr>
<tr class="even">
<td>AFJXWCP6</td>
<td>Inpt meds</td>
</tr>
<tr class="odd">
<td>AFJXWCP7</td>
<td>Current orders</td>
</tr>
<tr class="even">
<td>AFJXWCP8</td>
<td>Oupatient pharm</td>
</tr>
<tr class="odd">
<td>AFJXWCP9</td>
<td>Lab orders</td>
</tr>
<tr class="even">
<td>AFJXWCPA</td>
<td>Gather patient allergy data (from allergy routine)</td>
</tr>
<tr class="odd">
<td>AFJXWCPB</td>
<td>Brief NHE request patient info</td>
</tr>
<tr class="even">
<td>AFJXWCPC</td>
<td>Cyto extract</td>
</tr>
<tr class="odd">
<td>AFJXWCPD</td>
<td>Display 'VA' symbol</td>
</tr>
<tr class="even">
<td>AFJXWCPE</td>
<td>Radiology profile from hs</td>
</tr>
<tr class="odd">
<td>AFJXWCPF</td>
<td>Dietetics</td>
</tr>
<tr class="even">
<td>AFJXWCPG</td>
<td>Surgical path</td>
</tr>
<tr class="odd">
<td>AFJXWCPH</td>
<td>Request patient info—pharmacy</td>
</tr>
<tr class="even">
<td>AFJXWCPJ</td>
<td>Inpatient meds</td>
</tr>
<tr class="odd">
<td>AFJXWCPL</td>
<td>Chemistry extract</td>
</tr>
<tr class="even">
<td>AFJXWCPM</td>
<td>Request patient info menu</td>
</tr>
<tr class="odd">
<td>AFJXWCPN</td>
<td>Progress notes</td>
</tr>
<tr class="even">
<td>AFJXWCPR</td>
<td>Order inquiry</td>
</tr>
<tr class="odd">
<td>AFJXWCPY</td>
<td>Request pharmacy patient information</td>
</tr>
<tr class="even">
<td>AFJXWCPZ</td>
<td>Multiple functions</td>
</tr>
<tr class="odd">
<td>AFJXWPR2</td>
<td>Request patient info—Progress Notes</td>
</tr>
<tr class="even">
<td>AFJXWPRG</td>
<td>Request patient info—Progress Notes</td>
</tr>
</tbody>
</table>

<span id="_Toc96838217" class="anchor"></span>Table 3‑1: NHE routines

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter includes a list and brief description of files that are exported with the Network Health Exchange software.

There are no files that come with data. Thus, there is no danger of any files overwriting existing data.

| File Number | File Name                        | Global   | Description                                                                                 |
|-----------------|--------------------------------------|--------------|-------------------------------------------------------------------------------------------------|
| 537000          | VAMC NETWORK HEALTH EXCHANGE         | ^AFJ(537000, | This is the tracking file for NHE requests.                                                     |
| 537010          | VAMC NETWORK PATIENT                 | ^AFJ(537010, | This file contains patients seen in the network area.                                           |
| 537015          | VAMC NETWORK HEALTH TYPES            | ^AFJ(537015, | This file contains the components available, the 27 information categories supported by NHE.    |
| 537025          | VAMC NETWORK HEALTH AUTHORIZED SITES | ^AFJ(537025, | This file contains the names of facilities allowed to receive requests for patient information. |

<span id="_Toc96838218" class="anchor"></span>Table 4‑1: NHE files and globals

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no file security on the NHE files: 537000, 537010, 537015, 537025.

Records for patients in the database with an SSN containing five leading zeroes (00000), or two leading EEs, ZZs, or a P (pseudo) will *not* be sent across to other sites.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange (NHE) has two menus:

| Menu Name    | Menu Title Text             | Description                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AFJXNHEX REQUEST | Network Health Exchange Options | This menu comprises options to retrieve patient information from another VAMC site. It permits the retrieval of medical record or pharmacy information and allows that information to be viewed onscreen or printed. It is intended to be used by health professionals who have direct patient care responsibilities and have need for clinical information.                                                   |
| AFJXNHEX MANAGER | Network Health Exchange Manager | This menu contains options that afford managerial control of the operation of the local Network Health Exchange (NHE) software and also allow access to retrieve and print patient data from other VA Medical Centers. The Network Health Exchange Options \[AFJXNHEX REQUEST\] are subsumed under the Manager menu as Option 3. This menu is intended to be used by individuals responsible for managing NHE. |

<span id="_Toc96838219" class="anchor"></span>Table 5‑1: NHE menus

Network Health Exchange (NHE) also has five Site Management Functions. These are utilities for system managers to maintain the NHE software at their site. The functions are activated by directly accessing the utility or by changing the time the routine is run.

### Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### User Menu

The Network Health Exchange Options menu \[AFJXNHEX REQUEST\] is a User-related menu and has the following options:

| Option Name | Option Title Text                             |
|-----------------|---------------------------------------------------|
| AFJXWCPB        | Brief (12 months) Medical Record Information      |
| AFJXWCP1        | Total Medical Record Information                  |
| AFJXWCBP        | Brief (12 months) Pharmacy Information            |
| AFJXWCPY        | Total Pharmacy Information                        |
| AFJXMBOX        | Print (Completed Requests Only)                   |
| AFJXMABX        | Print By Type of Information (Completed Requests) |

<span id="_Toc96838220" class="anchor"></span>Table 5‑2: Network Health Exchange Options menu \[AFJXNHEX REQUEST\] options

#### Manager Menu

The Network Health Exchange Manager menu \[AFJXNHEX MANAGER\] is a Manager-related menu and has the following options:

| Option Name     | Option Title Text                  |
|---------------------|----------------------------------------|
| AFJXNHEX EDIT SITES | Network Health Exchange Add/Edit Sites |
| AFJXNHEX INQUIRE    | Network Health Exchange Inquiry        |
| AFJXNHEX REQUEST    | Network Health Exchange Options        |

<span id="_Toc96838221" class="anchor"></span>Table 5‑3: Network Health Exchange Manager Options menu \[AFJXNHEX MANAGER\] options

#### Site Management Functions

The Network Health Exchange Utilities for Site Management menu provides the following options (functions):

| Function Name    | Function Title Text                   |
|----------------------|-------------------------------------------|
| AFJXNETP             | Network Health Patient Server             |
| AFJXNHDONE           | Network Health Exchange Alert Send Server |
| AFJXSERVER           | Network Health Exchange Data Server       |
| AFJXNH ADD PATIENTS  | Network Health Exchange Add Patients      |
| AFJXNH PURGE NIGHTLY | Network Health Exchange Nightly Purge     |

<span id="_Toc96838222" class="anchor"></span>Table 5‑4: Network Health Exchange Utilities for Site Management options

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no security keys used in the VistA Network Health Exchange (NHE) menu options.

### Special Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange (NHE) generates a bulletin if data is requested for a *sensitive* patient. This bulletin is directed to the same user group (mail group) that currently reviews notices about access to *sensitive* patient records, as specified in the MAS PARAMETERS file (#43).

Records for patients in the database with an SSN containing five leading zeroes (00000), or two leading EEs, ZZs, or a P (pseudo) will not be sent across to other sites.

# Cross-references

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains descriptions of the cross-references on fields in the Network Health Exchange (NHE) files. The cross-references are grouped by file. The field is identified along with the cross-reference's name (or number if there is no name) and a brief description.

VAMC NETWORK HEALTH EXCHANGE File (#537000)

| Field          | Cross-reference ID | Description                                                      |
|--------------------|------------------------|----------------------------------------------------------------------|
| MESSAGE ID         | "B"                    | Ordinary cross-reference to facilitate lookup by MESSAGE ID.         |
| REQUESTING PLACE   | "C"                    | Ordinary cross-reference to facilitate lookup by REQUESTING PLACE.   |
| DATE/TIME RECEIVED | "D"                    | Ordinary cross-reference to facilitate lookup by DATE/TIME RECEIVED. |
| REQUESTOR NAME     | "E"                    | Ordinary cross-reference to facilitate lookup by REQUESTOR NAME.     |
| PATIENT SSN        | "F"                    | Ordinary cross-reference to facilitate lookup by PATIENT SSN.        |

<span id="_Toc96838223" class="anchor"></span>Table 6‑1: VAMC NETWORK HEALTH EXCHANGE file (#537000)—Cross-references

VAMC NETWORK PATIENT File (#537010)

| Field              | Cross-reference ID | Description                                                |
|------------------------|------------------------|----------------------------------------------------------------|
| SOCIAL SECURITY NUMBER | "B"                    | Normal "B" cross-reference on the .01 field.                   |
| NAME                   | "C"                    | Ordinary cross-reference to facilitate lookup by patient name. |

<span id="_Toc96838224" class="anchor"></span>Table 6‑2: VAMC NETWORK PATIENT file (#537010)—Cross-references

VAMC NETWORK HEALTH TYPES File (#537015)

| Field | Cross-reference ID | Description                              |
|-----------|------------------------|----------------------------------------------|
| NAME      | "B"                    | Normal "B" cross-reference on the .01 field. |

<span id="_Toc96838225" class="anchor"></span>Table 6‑3: VAMC NETWORK HEALTH TYPES file (#537015)—Cross-references

VAMC NETWORK HEALTH AUTHORIZED SITES File (#537025)

| Field      | Cross-reference ID | Description                                                            |
|----------------|------------------------|----------------------------------------------------------------------------|
| NAME           | "B"                    | Normal "B" cross-reference (on the .01 field.                              |
| STATION NUMBER | "C"                    | Ordinary cross-reference to facilitate lookup by the STATION NUMBER field. |
| NICKNAME       | "AC"                   | Ordinary cross-reference to facilitate lookup by the NICKNAME field.       |

<span id="_Toc96838226" class="anchor"></span>Table 6‑4: VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025)—Cross-references

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific archiving procedures or recommendations for the Network Health Exchange (NHE) software.

The NHE software contains the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025). There are no archiving procedures for this file.

The volumes of data that NHE references are drawn from other VistA software (e.g., Health Summary). The data for those software applications should be archived or purged according to their associated guidelines. Such archiving and purging does not affect the operation of the NHE software.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NHE contains the following purging option:

| Option Name      | Option Title Text | Description                                                                                                                                                                                                                                                                                                                           |
|----------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AFJXNH PURGE NIGHTLY | NHE Nightly Purge     | This option is used to purge alerts and/or mail messages nightly from the NETWORK,HEALTH EXCHANGE User mail box. Once messages and alerts are older than seven (7) days, they are flagged for purging and automatically purged when this option is run. It should be run each night following the other nightly job, AFJXNH ADD PATIENTS. |

<span id="_Toc96838227" class="anchor"></span>Table 7‑1: NHE purging option

|                                                   |                                                                                                                                                                                           |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-technical-manual/011.png) | At installation, a routine can be run (D ^AFJXPPED) to clean up the VAMC NETWORK PATIENT file (#537010) if the site has been running a previous version of Network Health Exchange (NHE). |

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines (i.e., Application Program Interfaces \[APIs\]) in the Network Health Exchange (NHE) software.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Platform Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Network Health Exchange software requires a standard VistA operating environment to function correctly.

#### Minimum Requirements

At a minimum, in order to run NHE at your site, the following VistA software must be installed:

- Kernel V. 8.0
- VA FileMan V. 21.0 or higher
- MailMan V. 7.1 or higher
- Kernel Toolkit V. 7.3

NHE patient data is displayed in a format similar to the integrated clinical reports found in Health Summary; however, NHE does *not* make calls to Health Summary. Therefore, it is *not* necessary to install Health Summary in order to use NHE.

#### Additional Requirements

There are no additional requirements or special relations between NHE and routines, files, or fields of other software.

### DBA Approvals and IAs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

To obtain the current list of IAs, if any, to which the NHE software is a custodian:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].

> 5\. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].

> 6\. When this option prompts you for a package, enter NHE.

> 7\. All current IAs to which the software is a custodian are listed.

To obtain detailed information on a specific integration agreement:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Inquire option \[DBA IA INQUIRY\].

> 5\. When prompted for "INTEGRATION REFERENCES," enter the specific integration agreement number of the IA you would like to display.

> 6\. The option then lists the full text of the IA you requested.

To obtain the current list of IAs, if any, to which the NHE software is a subscriber:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].

> 5\. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].

> 6\. When prompted with "START WITH SUBSCRIBING PACKAGE," enter NHE.

> 7\. All current IAs to which the software is a subscriber are listed.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NHE Version 5.1 software uses the AFJX namespace.

### File Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files for the NHE software are numbered from 537000 to 537025.

# Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange has no software-wide variables that have received SACC exemptions.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The glossary contains basic terms, acronyms, and definitions used throughout the VistA system, as well as terms specific to the NHE software.
|                                                 |                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADPAC                                           | Automated Data Processing (ADP) Application Coordinator (see Application Coordinator, below).                                                                                                                                                                                                                                                                                                         |
| ALERTS                                          | Brief on-line notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action. |
| APPLICATION COORDINATOR                         | Designated individuals responsible for user-level management and maintenance of a software application (e.g., Laboratory). Also abbreviated as ADPAC (ADP Application Coordinator).                                                                                                                                                                                                                   |
| BULLETINS                                       | Electronic mail messages that are automatically delivered by MailMan under certain conditions. For example, a bulletin can be set up to fire when database changes occur, such as adding a record to the file of users. Bulletins are fired by bulletin-type cross-references.                                                                                                                        |
| EXTRACTOR                                       | A specialized routine designed to scan data files and copy or summarize data for use by another process.                                                                                                                                                                                                                                                                                              |
| FREE TEXT                                       | A type of data field whose permissible values are any combination of numbers, letters, and symbols.                                                                                                                                                                                                                                                                                                   |
| IDCU                                            | The Integrated Data Communications Utility, a wide area network used by VA to interconnect computers for transmitting data between VA sites.                                                                                                                                                                                                                                                          |
| INTERNAL ENTRY NUMBER (IEN)                     | The number used to identify an entry within a file. Every record has a unique internal entry number.                                                                                                                                                                                                                                                                                                  |
| IRM                                             | Information Resource Management. A service at VA medical centers responsible for computer management and system security.                                                                                                                                                                                                                                                                             |
| ISO                                             | Information Security Officer. Person responsible for information security at each VA Medical Center. Works in conjunction with Regional Security Officers (RISOs).                                                                                                                                                                                                                                    |
| MAIL MESSAGE                                    | An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.                                                                                                                                                                                                                                                                     |
| MAS                                             | Medical Administration Service.                                                                                                                                                                                                                                                                                                                                                                       |
| MIRMO                                           | Medical Information Resources Management Office.                                                                                                                                                                                                                                                                                                                                                      |
| MIS                                             | Management Information System.                                                                                                                                                                                                                                                                                                                                                                        |
| NATIONAL NETWORK HEALTH EXCHANGE (NHE) REGISTRY | This VistA software consists of two major components: 1) a local registry for use within a VA health care facility, and 2) a National Registry reflecting the events of care for patients at all VA facilities.                                                                                                                                                                                       |
| RISO                                            | Regional Information Security Officer. Regional representative of VA Medical Center Information Security Officers (ISOs).                                                                                                                                                                                                                                                                             |
| SECURE MENU DELEGATION (SMD)                    | A controlled system whereby menus and keys can be allocated by people other than IRM staff, such as application coordinators, who have been so authorized.                                                                                                                                                                                                                                            |
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-technical-manual/012.png)</td>
<td><p>For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/glossary.asp">http://vista.med.va.gov/iss/glossary.asp</a></p>
</blockquote>
<p>For a list of commonly used acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vista/med/va/gov/iss/acronyms/index.asp">http://vista/med/va/gov/iss/acronyms/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^
^AFJ(537000, Global, 4-1
^AFJ(537015, Global, 4-1
^AFJ(537025, Global, 4-1
^AFJ(537100, Global, 4-1
A
Acronyms (ISS)
Home Page Web Address, Glossary, 2
ACTIVE by Custodial Package Option, 9-1
Add Patients, 5-3
Additional Requirements, 9-1
AFJXADHB Routine, 3-1
AFJXADHD Routine, 3-1
AFJXADPB Routine, 3-1
AFJXALER Routine, 3-1
AFJXALRT Routine, 3-1
AFJXBLOO Routine, 3-1
AFJXCAH Routine, 3-1
AFJXCAHB Routine, 3-1
AFJXCAHS Routine, 3-1
AFJXCYTO Routine, 3-1
AFJXDCS1 Routine, 3-1
AFJXDCSU Routine, 3-1
AFJXDIE2 Routine, 3-1
AFJXDIET Routine, 3-1
AFJXDISA Routine, 3-1
AFJXDM! Routine, 3-1
AFJXEND Routine, 3-1
AFJXINST Routine, 3-1
AFJXLABO Routine, 3-1
AFJXLRM Routine, 3-1
AFJXLRM1 Routine, 3-1
AFJXLROC Routine, 3-1
AFJXMABX Option, 5-2
AFJXMABX Routine, 3-1
AFJXMBOX Option, 5-2
AFJXMBOX Routine, 3-1
AFJXMEDI Routine, 3-1
AFJXNETP Option, 5-3
AFJXNH ADD PATIENTS Option, 5-3
AFJXNH PURGE NIGHTLY Option, 5-3
AFJXNHDONE Option, 5-3
AFJXNHEX EDIT SITES Option, 5-2
AFJXNHEX INQUIRE Option, 5-2
AFJXNHEX MANAGER Menu, 5-1, 5-2
AFJXNHEX REQUEST Menu, 5-1, 5-2
AFJXNTEG Routine, 3-1
AFJXORDR Routine, 3-1
AFJXPATL Routine, 3-1
AFJXPATS Routine, 3-2
AFJXPHCY Routine, 3-2
AFJXPHIV Routine, 3-2
AFJXPNHA /RF/BC Routine, 3-2
AFJXPNHF Routine, 3-2
AFJXPNHI Routine, 3-2
AFJXPNHT Routine, 3-2
AFJXPNHX Routine, 3-2
AFJXPPED Routine, 3-2
AFJXPUL2 Routine, 3-2
AFJXPULM Routine, 3-2
AFJXRADI Routine, 3-2
AFJXRALT Routine, 3-2
AFJXRATS Routine, 3-2
AFJXRIMP Routine, 3-2
AFJXSERVER Option, 5-3
AFJXSFAL Routine, 3-2
AFJXSPTH Routine, 3-2
AFJXSURY Routine, 3-2
AFJXTEMA Routine, 3-2
AFJXUNDS Routine, 3-2
AFJXUNIT Routine, 3-2
AFJXVISI Routine, 3-2
AFJXVITA Routine, 3-2
AFJXVITS Routine, 3-3
AFJXWCBP Option, 5-2
AFJXWCBP Routine, 3-3
AFJXWCCW Routine, 3-3
AFJXWCL1 Routine, 3-3
AFJXWCL2 Routine, 3-3
AFJXWCL4 Routine, 3-3
AFJXWCL5 Routine, 3-3
AFJXWCL7 Routine, 3-3
AFJXWCL8 Routine, 3-3
AFJXWCL9 Routine, 3-3
AFJXWCLI Routine, 3-3
AFJXWCP1 Option, 5-2
AFJXWCP1 Routine, 3-3
AFJXWCP3 Routine, 3-3
AFJXWCP4 Routine, 3-3
AFJXWCP6 Routine, 3-3
AFJXWCP7 Routine, 3-3
AFJXWCP8 Routine, 3-3
AFJXWCP9 Routine, 3-3
AFJXWCPA Routine, 3-3
AFJXWCPB Option, 5-2
AFJXWCPB Routine, 3-3
AFJXWCPC Routine, 3-3
AFJXWCPD Routine, 3-3
AFJXWCPE Routine, 3-3
AFJXWCPF Routine, 3-3
AFJXWCPG Routine, 3-3
AFJXWCPH Routine, 3-3
AFJXWCPJ Routine, 3-3
AFJXWCPL Routine, 3-3
AFJXWCPM Routine, 3-3
AFJXWCPN Routine, 3-3
AFJXWCPR Routine, 3-3
AFJXWCPY Option, 5-2
AFJXWCPY Routine, 3-3
AFJXWCPZ Routine, 3-3
AFJXWPR2 Routine, 3-3
AFJXWPRG Routine, 3-4
Alert Send Server, 5-3
APIs, 8-1
Archiving, 7-1
Assumptions About the Reader, xi
B
Brief (12 months) Medical Record Information Option, 5-2
Brief (12 months) Pharmacy Information Option, 5-2
C
Callable Routines, 8-1
Callout Boxes, x
Contents, v
Cross-references, 6-1
Custodial Package Menu, 9-1
D
Data Dictionary
Data Dictionary Utilities Menu, xi
Listings, xi
Data Server, 5-3
DBA Approvals and IAs, 9-1
DBA IA CUSTODIAL MENU, 9-1
DBA IA CUSTODIAL Option, 9-1
DBA IA INQUIRY Option, 9-2
DBA IA ISC Menu, 9-1, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA IA SUBSCRIBER Option, 9-2
DBA Menu, 9-1, 9-2
Documentation
Revisions, iii
Symbols, ix
E
EVS Anonymous Directories, xii
Exemptions
SACC, 11-1
Exported
Options, 5-1
External
Relations, 9-1
F
Figures and Tables, vii
Files, 4-1
MAS PARAMETERS (#43), 5-3
MESSAGE (#3.9), Glossary, 1
Numbers, 10-1
Security, 4-1
VAMC NETWORK HEALTH AUTHORIZED SITES (#537025), 4-1, 7-1
Cross-references, 6-2
VAMC NETWORK HEALTH EXCHANGE (#537000), 2-1, 4-1
Cross-references, 6-1
VAMC NETWORK HEALTH TYPES (#537015), 4-1
Cross-references, 6-1
VAMC NETWORK PATIENT (#537010), 2-1, 4-1
Cross-references, 6-1
Functions
AFJXNETP, 5-3
AFJXNH ADD PATIENTS, 5-3
AFJXNH PURGE NIGHTLY, 5-3
AFJXNHDONE, 5-3
AFJXSERVER, 5-3
Network Health Exchange Add Patients, 5-3
Network Health Exchange Alert Send Server, 5-3
Network Health Exchange Data Server, 5-3
Network Health Exchange Nightly Purge, 5-3
Network Health Patient Server, 5-3
Site Management, 2-1, 5-3
G
Globals, 4-1
^AFJ(537000,, 4-1
^AFJ(537010,, 4-1
^AFJ(537015,, 4-1
^AFJ(537025,, 4-1
Glossary, 1
Glossary (ISS)
Home Page Web Address, Glossary, 2
H
Help
At Prompts, x
Online, x
Home Pages
Adobe Acrobat Quick Guide Web Address, xii
Adobe Web Address, xii
Health Systems Design and Development (HSD&D) Web Address, xi
ISS Acronyms Home Page Web Address, Glossary, 2
ISS Glossary Home Page Web Address, Glossary, 2
Network Health Exchange Home Page Web Address, xii
VDL Home Page Web Address, xii
How to
Obtain Technical Information Online, x
Use this Manual, ix
I
IAs, 9-1
Implementation, 2-1
Inquire Option, 9-2
Integration Agreements Menu Option, 9-1, 9-2
Internal
Relations, 10-1
Introduction, 1-1
ISS Acronyms
Home Page Web Address, Glossary, 2
ISS Glossary
Home Page Web Address, Glossary, 2
K
Keys
Security, 5-3
L
List File Attributes Option, xi
M
Mail Boxes
NETWORK,HEALTH EXCHANGE User, 2-1
Manager
Menu, 2-1, 5-2
MAS PARAMETERS File (#43), 5-3
Menus, 5-1, 5-2
AFJXNHEX MANAGER, 5-1, 5-2
AFJXNHEX REQUEST, 5-1, 5-2
Custodial Package Menu, 9-1
Data Dictionary Utilities, xi
DBA, 9-1, 9-2
DBA IA CUSTODIAL MENU, 9-1
DBA IA ISC, 9-1, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA Option, 9-1, 9-2
Integration Agreements Menu, 9-1, 9-2
Manager, 2-1, 5-2
Network Health Exchange Manager, 5-1, 5-2
Network Health Exchange Options, 5-1, 5-2
Network Health Exchange Utilities for Site Management, 5-3
Subscriber Package Menu, 9-2
User, 5-2
MESSAGE file (#3.9), Glossary, 1
Minimum Requirements, 9-1
N
Namespace, 10-1
Network Health Exchange
Home Page Web Address, xii
Network Health Exchange Add Patients Option, 5-3
Network Health Exchange Add/Edit Sites Option, 5-2
Network Health Exchange Alert Send Server Option, 5-3
Network Health Exchange Data Server Option, 5-3
Network Health Exchange Inquiry Option, 5-2
Network Health Exchange Manager Menu, 5-1, 5-2
Network Health Exchange Nightly Purge Option, 5-3
Network Health Exchange Options Menu, 5-1, 5-2
Network Health Exchange Options Options Menu, 5-2
Network Health Exchange Utilities for Site Management Menu, 5-3
Network Health Patient Server Option, 5-3
NETWORK,HEALTH EXCHANGE User Mail Box, 2-1
O
Obtaining Data Dictionary Listings, xi
Online
Documentation, x
Help Frames, xi
Technical Information, How to Obtain, x
Options, 5-1, 5-2
ACTIVE by Custodial Package, 9-1
AFJXMABX, 5-2
AFJXMBOX, 5-2
AFJXNETP, 5-3
AFJXNH ADD PATIENTS, 5-3
AFJXNH PURGE NIGHTLY, 5-3
AFJXNHDONE, 5-3
AFJXNHEX EDIT SITES, 5-2
AFJXNHEX INQUIRE, 5-2
AFJXNHEX MANAGER, 5-1, 5-2
AFJXNHEX REQUEST, 5-1, 5-2
AFJXSERVER, 5-3
AFJXWCBP, 5-2
AFJXWCP1, 5-2
AFJXWCPB, 5-2
AFJXWCPY, 5-2
Brief (12 months) Medical Record Information, 5-2
Brief (12 months) Pharmacy Information, 5-2
Custodial Package Menu, 9-1
DBA, 9-1, 9-2
DBA IA CUSTODIAL, 9-1
DBA IA CUSTODIAL MENU, 9-1
DBA IA INQUIRY, 9-2
DBA IA ISC, 9-1, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA IA SUBSCRIBER Option, 9-2
DBA Option, 9-1, 9-2
Exported, 5-1
Inquire, 9-2
Integration Agreements Menu, 9-1, 9-2
List File Attributes, xi
Manager, 2-1, 5-2
Network Health Exchange Add Patients, 5-3
Network Health Exchange Add/Edit Sites, 5-2
Network Health Exchange Alert Send Server, 5-3
Network Health Exchange Data Server, 5-3
Network Health Exchange Inquiry, 5-2
Network Health Exchange Manager, 5-1, 5-2
Network Health Exchange Nightly Purge, 5-3
Network Health Exchange Options, 5-1, 5-2
Network Health Exchange Utilities for Site Management, 5-3
Network Health Patient Server, 5-3
Print (Completed Requests Only), 5-2
Print ACTIVE by Subscribing Package, 9-2
Print By Type of Information (Completed Requests), 5-2
Site Management, 2-1
Subscriber Package Menu, 9-2
Total Medical Record Information, 5-2
Total Pharmacy Information, 5-2
User, 5-2
Orientation, ix
P
Patches
Revisions, iii
Platform Requirements, 9-1
Print (Completed Requests Only) Option, 5-2
Print ACTIVE by Subscribing Package Option, 9-2
Print By Type of Information (Completed Requests) Option, 5-2
Pseudo Patients, 4-1, 5-3
Purging, 7-1
Q
Question Mark Help, x
R
Reader, Assumptions About the, xi
Reference Materials, xii
Relations
External, 9-1
Internal, 10-1
Requirements
Additional, 9-1
Minimum, 9-1
Platform, 9-1
Revision History, iii
Documentation, iii
Patches, iii
Routines, 3-1
AFJXADHB, 3-1
AFJXADHD, 3-1
AFJXADPB, 3-1
AFJXALER, 3-1
AFJXALRT, 3-1
AFJXBLOO, 3-1
AFJXCAH, 3-1
AFJXCAHB, 3-1
AFJXCAHS, 3-1
AFJXCYTO, 3-1
AFJXDCS1, 3-1
AFJXDCSU, 3-1
AFJXDIE2, 3-1
AFJXDIET, 3-1
AFJXDISA, 3-1
AFJXDMI, 3-1
AFJXEND, 3-1
AFJXINST, 3-1
AFJXLABO, 3-1
AFJXLRM, 3-1
AFJXLRM1, 3-1
AFJXLROC, 3-1
AFJXMABX, 3-1
AFJXMBOX, 3-1
AFJXMEDI, 3-1
AFJXNTEG, 3-1
AFJXORDR, 3-1
AFJXPATL, 3-1
AFJXPATS, 3-2
AFJXPHCY, 3-2
AFJXPHIV, 3-2
AFJXPNHA /RF/BC, 3-2
AFJXPNHF, 3-2
AFJXPNHI, 3-2
AFJXPNHT, 3-2
AFJXPNHX, 3-2
AFJXPPED, 3-2
AFJXPUL2, 3-2
AFJXPULM, 3-2
AFJXRADI, 3-2
AFJXRALT, 3-2
AFJXRATS, 3-2
AFJXRIMP, 3-2
AFJXSFAL, 3-2
AFJXSPTH, 3-2
AFJXSURY, 3-2
AFJXTEMA, 3-2
AFJXUNDS, 3-2
AFJXUNIT, 3-2
AFJXVISI, 3-2
AFJXVITA, 3-2
AFJXVITS, 3-3
AFJXWCBP, 3-3
AFJXWCCW, 3-3
AFJXWCL1, 3-3
AFJXWCL2, 3-3
AFJXWCL4, 3-3
AFJXWCL5, 3-3
AFJXWCL7, 3-3
AFJXWCL8, 3-3
AFJXWCL9, 3-3
AFJXWCLI, 3-3
AFJXWCP1, 3-3
AFJXWCP3, 3-3
AFJXWCP4, 3-3
AFJXWCP6, 3-3
AFJXWCP7, 3-3
AFJXWCP8, 3-3
AFJXWCP9, 3-3
AFJXWCPA, 3-3
AFJXWCPB, 3-3
AFJXWCPC, 3-3
AFJXWCPD, 3-3
AFJXWCPE, 3-3
AFJXWCPF, 3-3
AFJXWCPG, 3-3
AFJXWCPH, 3-3
AFJXWCPJ, 3-3
AFJXWCPL, 3-3
AFJXWCPM, 3-3
AFJXWCPN, 3-3
AFJXWCPR, 3-3
AFJXWCPY, 3-3
AFJXWCPZ, 3-3
AFJXWPR2, 3-3
AFJXWPRG, 3-4
S
SACC Exemptions, 11-1
Security
Files, 4-1
Keys, 5-3
Special Features, 5-3
Sensitive Patient Records, 5-3
Site Management
Functions, 5-3
Site Management Functions, 2-1
Software-wide Variables, 11-1
Special Security Features, 5-3
Subscriber Package Menu Option, 9-2
Symbols Found in the Documentation, ix
System Managers
Utilities, 5-1
T
Test Patients, 4-1, 5-3
Total Medical Record Information Option, 5-2
Total Pharmacy Information Option, 5-2
U
URLs
Adobe Acrobat Quick Guide Web Address, xii
Adobe Home Page Web Address, xii
Health Systems Design and Development (HSD&D) Home Page Web Address, xi
Use this Manual, How to, ix
User
Menu, 5-2
Users
NETWORK,HEALTH EXCHANGE Mail Box, 2-1
Using
Adobe Acrobat Reader, xii
Utilities
For System Managers, 5-1
V
VAMC NETWORK HEALTH AUTHORIZED SITES File (#537025), 4-1, 7-1
Cross-references, 6-2
VAMC NETWORK HEALTH EXCHANGE File (#537000), 2-1, 4-1
Cross-references, 6-1
VAMC NETWORK HEALTH TYPES File (#537015), 4-1
Cross-references, 6-1
VAMC NETWORK PATIENT File (#537010), 2-1, 4-1
Cross-references, 6-1
Variables
Software-wide, 11-1
VDL
Home Page Web Address, xii
W
Web Pages
Adobe Acrobat Quick Guide Web Address, xii
Adobe Home Page Web Address, xii
Health Systems Design and Development (HSD&D) Home Page Web Address, xi
ISS Acronyms Home Page Web Address, Glossary, 2
ISS Glossary Home Page Web Address, Glossary, 2
Network Health Exchange Home Page Web Address, xii
VDL Home Page Web Address, xii
