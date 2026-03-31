---
title: Virtual Patient Record (VPR) Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: Virtual Patient Record (VPR)
app_code: VPR
app_name: Virtual Patient Record
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 560
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - strong
  - class
  - table
  - contents
  - even
  - patient
  - span
  - record
  - manual
  - software
page_count: 0
word_count: 9207
section_count: 23
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=197"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Virtual Patient Record (VPR) 1.0

  Technical Manual
---

![](virtual-patient-record-vpr-technical-manual/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Software Product Management (SPM)

<span id="_Toc157048628" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref386466976" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 48%" />
<col style="width: 24%" />
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
<td>01/24/2024</td>
<td>2.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Added Sections <u>2.2.1</u>, “VPR,” and <u>2.2.2</u>, “HealthShare.”</p></li>
<li><p>Updated Table 3: Added the <strong>VPRSDAOB</strong> routine.</p></li>
<li><p>Updated Table 6: Added ICR entries: 7437, 4513, and 5042.</p></li>
<li><p>Update <u>Table 9</u>: Added the <strong>MDC OBSERVATION UPDATE</strong> event protocol.</p></li>
</ul></td>
<td>Virtual Patient Record (VPR) Development Team</td>
</tr>
<tr class="even">
<td>07/05/2023</td>
<td>2.0</td>
<td><p>Updates for VPR Patch VPR*1*31:</p>
<ul>
<li><p><u>Table 3</u>: Added the <strong>VPREVSND</strong>, <strong>VPRP31</strong>, and <strong>VPRSDAIB</strong> entries.</p></li>
<li><p><u>Table 6</u>: Added the <strong>^TIU(8925.7)</strong> entry.</p></li>
<li><p><a href="#glossary">Glossary</a>: Corrected SDA description.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>01/18/2023</td>
<td>1.9</td>
<td><p>Updates for VPR Patch VPR*1*30:</p>
<ul>
<li><p><u>Table 3</u>: Added the <strong>VPREVNT1</strong>, <strong>VPRP29</strong>, <strong>VPRP30</strong>, <strong>VPRSDADG</strong>, <strong>VPRSDAHX</strong>, <strong>VPRSDAM</strong>, <strong>VPRSDAOR</strong>, <strong>VPRSDASR</strong>, and <strong>VPRSDAVF</strong> entries.</p></li>
<li><p><u>Table 6</u>: Added the <strong>6130-DGPTFUT, 4202-ORQ12</strong> and <strong>5925-WVUTL11</strong> entries.</p></li>
<li><p><u>Table 8</u>: Added the <strong>PSO VDEF RDS O13 OP PHARM PPAR VS</strong> and <strong>PSO VDEF RDS O13 OP PHARM PREF VS</strong> entries.</p></li>
<li><p><u>Table 9</u>: Added the <strong>DG PTF ICD PROCEDURE NOTIFIER</strong> entry.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>07/05/2022</td>
<td>1.8</td>
<td><p>Updates:</p>
<ul>
<li><p><u>Table 3</u>: Deleted <strong>VPR17</strong> entry. Added <strong>VPRP26</strong>, <strong>VPRP27</strong>, and <strong>VPRP28</strong> entries.</p></li>
<li><p><u>Table 4</u>: Added <strong>VPR PCMM PTPEVT TASK</strong> entry.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>11/03/2021</td>
<td>1.7</td>
<td><p>Updates:</p>
<ul>
<li><p><u>Table 2</u>: Added <strong>VPR CONTAINER (#560.1) file</strong> entry.</p></li>
<li><p><u>Table 3</u>: Added the <strong>VPRSDAG</strong> entry.</p></li>
<li><p><u>Table 4</u>: Deleted <strong>VPR HS VIEW LOG</strong> entry.</p></li>
<li><p><u>Table 6</u>: Added the <strong>ICR 2974, ^GMPL(125.8)</strong> entry. Deleted the <strong>ICR 5772</strong> entry.</p></li>
<li><p><u>Table 9</u>: Added the <strong>TIU DOCUMENT ACTION EVENT</strong> entry.</p></li>
<li><p>Updated Section <u>10</u>: Added reference to the <strong>VPR CONTAINER (#560.1) file</strong>.</p></li>
<li><p>Updated Section <u>11.3</u> and <u>Figure 4</u>: Added VPR CONTAINER file security access.</p></li>
<li><p><u>Table 12</u>: Added the <strong>CPRS</strong> and <strong>ECR</strong> entry.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>03/26/2021</td>
<td>1.6</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>2.1.2</u>: Added the Emergency Department Information System 2.0 as required software.</p></li>
<li><p><u>Table 3</u>: Added the following entries <strong>VPRENC,</strong> <strong>VPRHST1, VPRHST2, VPRHSX1, VPRHSX2, VPRP11I, VPRP12I, VPRP13I, VPRP14, VPRP16, VPRP17, VPRP20, VPRP24, VPRP5I, VPRP8I, VPRPCMM, VPRSDAC, VPRSDAD, VPRSDAF, VPRSDAT,</strong> and <strong>VPRSDAV</strong>.</p></li>
<li><p><u>Table 4</u>: All entries.</p></li>
<li><p><u>Table 6</u>: Added the following entries: <strong>^EDP(230), DGPFAA, DGPFAAH, PSSUTLA1, WVRPCVPR</strong>, and <strong>XUTMTP</strong>.</p></li>
<li><p>Section <u>8.2</u>: Update text and added reference note.</p></li>
<li><p>Table 8: Deleted an entry.</p></li>
<li><p>Table 9: Added the following entries: <strong>DG PTF ICD DIAGNOSIS NOTIFIER, DG SA FILE ENTRY NOTIFIER, DGPF PRF EVENT, GMRA VERIFY DATA,</strong> and <strong>WV PREGNANCY STATUS CHANGE EVENT</strong>.</p></li>
<li><p>Section <u>11.2</u>: Added description of the <strong>VPR HS ENABLE</strong> security key.</p></li>
<li><p>Section <u>14.1</u>: Added <u>Table 11</u>.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>06/06/2019</td>
<td>1.5</td>
<td><p>Updates for Patch VPR*1.0*10:</p>
<ul>
<li><p>Updated <u>Table 3</u>: Added <strong>VPR15</strong> and <strong>VPRSDAB</strong> entries.</p></li>
<li><p>Updated <u>Table 6</u>: Added ICRs: <strong>7014</strong>, <strong>6978</strong>, <strong>2045</strong>, <strong>7084</strong>, <strong>6980</strong>, and <strong>2200</strong>.</p></li>
<li><p>Updated Section <u>2.1.3</u>: Added the <strong>VPRVDIF,APPLICATION PROXY</strong>.</p></li>
<li><p>Updated Section <u>9</u>: Added VPR SAC Exemption; <u>Table 10</u>.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>04/24/2019</td>
<td>1.4</td>
<td><p>Updates for Patch VPR*1.0*8 and VPR*1.0*14:</p>
<ul>
<li><p>Section <u>1.2</u>: Updated RPC bullet list descriptions.</p></li>
<li><p>Updated File #560 description in <u>Table 2</u>.</p></li>
<li><p>Added the <strong>VPRP10</strong> routine to <u>Table 3</u>.</p></li>
<li><p>Removed <strong>VAFC ADT-A04 SERVER</strong> event protocol from <u>Table 8</u>.</p></li>
<li><p>Added the following event protocols to <u>Table 9</u>:</p></li>
</ul>
<ul>
<li><p><strong>LR7O AP EVSEND OR</strong></p></li>
<li><p><strong>PSB EVSEND VPR</strong></p></li>
<li><p><strong>SCMC PATIENT TEAM CHANGES</strong></p></li>
<li><p><strong>SCMC PATIENT TEAM POSITION CHANGES</strong></p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>11/15/2018</td>
<td>1.3</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>8.4</u>: Added <u>Table 8</u> with listener information and revised <u>Table 9</u> to include listener information.</p></li>
<li><p>Added Section <u>10</u>, “<u>Global Journaling and Placement</u>.”</p></li>
<li><p>Section <u>14</u>. Added and updated the following sections:</p></li>
</ul>
<ul>
<li><p>Section <u>14.1</u>, “<u>Menus and Options</u>.”</p></li>
<li><p>Section <u>14.2</u>, “<u>Protocol Events and Listeners</u>.”</p></li>
<li><p>Section <u>14.3</u>, “<u>Special Instructions for Error Correction</u>.”</p></li>
<li><p>Section <u>14.4</u>, “<u>Enterprise Service Desk and Organizational Contacts</u>. ”</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>11/01/2018</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>1</u>.</p></li>
<li><p>Section <u>2.1.3</u>.</p></li>
<li><p>Section <u>4</u>; <u>Table 3</u>.</p></li>
<li><p>Section <u>8.1</u>; <u>Table 6</u>.</p></li>
<li><p>Section <u>8.2</u>.</p></li>
<li><p>Section <u>8.4</u>; added <u>Table 9</u>.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>10/24/2018</td>
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>1.2</u>; modified historical references to Health Informatics Initiative (hi<sup>2</sup>).</p></li>
<li><p>Section <u>1.4</u>.</p></li>
<li><p>Section <u>2.1</u>, <u>2.1.1</u>, and <u>2.1.2</u>.</p></li>
<li><p>Section <u>2.1.3</u>.</p></li>
<li><p>Section <u>2.1.4</u>.</p></li>
<li><p>Section <u>2.2</u>.</p></li>
<li><p>Section <u>3</u>, <u>Table 2</u>.</p></li>
<li><p>Section <u>4</u>, <u>Table 3</u>; removed checksum and added summary descriptions for each routine listed.</p></li>
<li><p>Section <u>5</u>, <u>Table 4</u>.</p></li>
<li><p>Section <u>6</u>, <u>Table 5</u>.</p></li>
<li><p>Sections <u>7</u>, <u>8</u>, <u>9</u>, <u>10</u>, <u>12</u>, and <u>13</u> and all subsections; mainly stating does not apply to VPR or adding some explanatory text.</p></li>
<li><p>Added Enterprise Service Desk (ESD) contact information to Section <u>14.4</u>.</p></li>
<li><p>Updated the <u>Glossary</u>.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>09/25/2018</td>
<td>1.0</td>
<td><p>Updates for Patch VPR*1.0*8:</p>
<ul>
<li><p>Created a new, separate <em>VPR Technical Manual</em> (this manual).</p></li>
<li><p>Moved other content to a new, separate <em>VPR Developer’s Guide</em>.</p></li>
<li><p>Updated document to follow current documentation standards and style guidelines.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref386466976" class="anchor"></span>Table : Documentation Symbol Descriptions

Table of Contents

<span id="_Toc157048629" class="anchor"></span>List of Figures

<span id="_Toc157048630" class="anchor"></span>List of Tables

<span id="_Ref38421374" class="anchor"></span>Orientation

How to Use this Manual

The *Virtual Patient Record (VPR) Technical Manual* provides information about the technical structure of the VPR software. It includes the following information about VPR:

- <u>Implementation and Maintenance</u>
- <u>Files</u>
- <u>Routines</u>
- <u>Exported Options</u>
- <u>Parameters</u>
- <u>Remote Procedure Calls</u>

![](virtual-patient-record-vpr-technical-manual/002.png) REF: For VPR installation instructions in the Veterans Health Information Systems and Technology Architecture (VistA) environment see the *Virtual Patient Record (VPR) Installation Guide* and any national patch description of the patch being released.

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Software Product Management (SPM)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](virtual-patient-record-vpr-technical-manual/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation of and the functionality contained in Virtual Patient Record (VPR) 1.0; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](virtual-patient-record-vpr-technical-manual/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](virtual-patient-record-vpr-technical-manual/005.png)  | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](virtual-patient-record-vpr-technical-manual/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref528074413" class="anchor"></span>Table : VPR Files

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Virtual Patient Record (VPR) test patient and user names would be documented as follows:

- VPRPATIENT,ONE; VPRPATIENT,TWO; VPRPATIENT,THREE; … VPRPATIENT,14; etc.
- VPRUSER,ONE; VPRUSER,TWO; VPRUSER,THREE; … VPRUSER,14; etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box:
- User’s responses to online prompts are bold typeface and sometimes highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are sometimes represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](virtual-patient-record-vpr-technical-manual/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the MUMPS (M) programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, security keys, and RPCs (e.g., VPR GET PATIENT DATA).

![](virtual-patient-record-vpr-technical-manual/008.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to your customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](virtual-patient-record-vpr-technical-manual/009.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

![](virtual-patient-record-vpr-technical-manual/010.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate topic.  
  
REF: For further information, see the *VA FileMan Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](virtual-patient-record-vpr-technical-manual/011.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about Virtual Patient Record (VPR) should consult the following:

- *Virtual Patient Record (VPR) Installation Guide*
- *Virtual Patient Record (VPR) Technical Manual* (this manual)
- *Virtual Patient Record (VPR) Developer’s Guide*

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA software documentation can be downloaded from the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/>

![](virtual-patient-record-vpr-technical-manual/012.png) REF: VPR manuals are located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=197>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Enhancements](#enhancements)
  - [Background](#background)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Application Proxies](#application-proxies)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
    - [VPR](#vpr)
    - [HealthShare](#healthshare)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Parameters](#parameters)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging and Protocols](#hl7-messaging-and-protocols)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-Wide Variables](#software-wide-variables)
- [Global Journaling and Placement](#global-journaling-and-placement)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [Menus and Options](#menus-and-options)
  - [Protocol Events and Listeners](#protocol-events-and-listeners)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [Glossary](#glossary)
A technical manual is a required end-user document for all Office of Information and Technology (OIT) software releases. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support (PS) personnel.
The intended audience for this document is local information technology (IT) support, management, and development personnel for nationally released software.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide technical information about the Virtual Patient Record (VPR) 1.0 software, which is a developer tool.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR 1.0 was originally developed as a part of the Health Informatics Initiative (hi<sup>2</sup>). It has been expanded to support VA’s interfaces to InterSystems’ Health Connect (HC) and HealthShare (HS).

VPR extracts patient data from domains at a local Veterans Health Information Systems and Technology Architecture (VistA) site to provide a cached view of the patient chart. It provides normalized fields with common field names and data structures across domains.

VPR includes four remote procedure calls (RPCs) that do the following:

- Extract data from VistA in Extensible Markup Language (XML) format.
- Extract VistA data in JavaScript Object Notation (JSON) format.
- Calculates checksums for data returned via the XML or JSON RPC.
- Returns the current VPR RPC version number.

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR Patch VPR\*1\*8 extends the Virtual Patient Record (VPR) application, to provide a new method of retrieving patient health data from a VistA database.

VA FileMan Patch DI\*22.2\*9 released a new VA FileMan utility that provides the ability to map VistA files and fields to other data models and extract that data as XML or JSON objects. Patch VPR\*1\*8 populates the new ENTITY (#1.5) file to map VistA data elements to InterSystems' Summary Data Architecture (SDA) model and use the new supported calls to retrieve the requested data.

Patch VPR\*1\*8 also installs a mechanism to monitor clinical data events in VistA, to enable retrieval of updated information as a patient's data changes. This patch adds new PROTOCOL (#101) file entries and links to appropriate clinical application events; the file and record numbers modified will be collected in the VPR SUBSCRIPTION (#560) file until retrieved and updated.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR RPC for XML-formatted data extraction was initially created in the Nationwide Health Information Network (NwHIN) namespace, which was called NHIN. The NwHIN client used most of the VPR’s extract routines in production to get and share data. After this initial version, VPR RPCs were moved into the VPR’s own (VPR) namespace and renumbered as VPR Version 1.0. NwHIN could continue to use the extract routines in its NHIN namespace, but would need to access VPR 1.0, or subsequent versions, to take advantage of future extract routine enhancements.

![](virtual-patient-record-vpr-technical-manual/013.png) NOTE: After the VPR package installed its RPCs in its own (VPR) namespace with VPR 1.0, NwHIN began to use VPR 1.0 to take advantage of future extract-routine enhancements. The Veterans Health Information Exchange (VHIE) and Joint Legacy Viewer (JLV) are currently the primary users of the RPCs.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information to assist technical support staff with the implementation and maintenance of the software.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR is a typical legacy Veterans Health Information Systems and Technology Architecture (VistA) Kernel Installation and Distribution System (KIDS) software release.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* require any special hardware. It requires the same minimum hardware, servers, virtual systems, workstations, and peripheral devices required by any legacy VistA product.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR expects the following VistA software packages to be installed and fully patched:

- VA FileMan 22.2
- Kernel 8.0
- Adverse Reaction Tracking 4.0
- Care Management 1.0
- Clinical Procedures 1.0
- Clinical Reminders 2.0
- Consult/Request Tracking 3.0
- Emergency Department Information System 2.0
- Enterprise Terminology Service 1.0
- Functional Independence 1.0
- Gen. Med. Rec. – Vitals 5.0
- Hospital Inquiry (HINQ) 4.0
- Integrated Billing 2.0
- Laboratory 5.2
- Lexicon Utility 2.0
- Master Patient Index (MPI) 1.0
- National Drug File 4.0
- Order Entry/Results Reporting 3.0
- Outpatient Pharmacy 7.0
- Patient Care Encounter (PCE) 1.0
- Pharmacy Data Management 1.0
- Problem List 2.0
- Radiology/Nuclear Medicine 5.0
- Registration 5.3
- Scheduling 5.3
- Surgery 3.0
- Text Integration Utilities (TIU) 1.0
- Women’s Health 1.0

You can download the latest versions of VPR software and documentation, including this manual, via SSH File Transfer Protocol (SFTP) from the Product Support (PS) Anonymous Directories.

Patches to the VPR application are available via the National Patch Module (NPM) on FORUM.

### Application Proxies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR package contains the following application proxies for connecting to the local VistA system:

- <u>VPR,APPLICATION PROXY</u>
- <u>VPRVDIF,APPLICATION PROXY</u>

![](virtual-patient-record-vpr-technical-manual/014.png) CAUTION: Do *not* terminate the VPR Application Proxies from the NEW PERSON (#200) file; they *must* remain active.

#### VPR,APPLICATION PROXY

The VPR,APPLICATION PROXY is currently being used by the Joint Legacy Viewer (JLV) and Veterans Health Information Exchange (VHIE) clients.

If your site is experiencing connection issues, verify the VPR entry in the NEW PERSON (#200) file looks like the listing in <u>Figure 1</u>:

<span id="_Ref528072837" class="anchor"></span>Figure : VPR Application Proxy Entry

NAME: <span class="mark">VPR,APPLICATION PROXY</span> DATE ENTERED: SEP 08, 2011

SECONDARY MENU OPTIONS: VPR APPLICATION PROXY

User Class: APPLICATION PROXY ISPRIMARY: Yes

PROVIDER KEY (c): 0

#### VPRVDIF,APPLICATION PROXY

The VPRVDIF,APPLICATION PROXY is currently being used by the Veterans Data Integration and Federation (VDIF) project (HealthShare interface) clients.

![](virtual-patient-record-vpr-technical-manual/015.png) NOTE: The VPRVDIF,APPLICATION PROXY was added with Patch VPR\*1.0\*15.

If your site is experiencing connection issues, verify the VPRVDIF entry in the NEW PERSON (#200) file looks like the listing in <u>Figure 2</u>:

<span id="_Ref10710285" class="anchor"></span>Figure : VPRVDIF Application Proxy Entry

NAME: <span class="mark">VPRVDIF,APPLICATION PROXY</span>         DATE ENTERED: MAY 16, 2019

  CREATOR: VPRUSER,ONE

User Class: APPLICATION PROXY           ISPRIMARY: Yes

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan 22.2 and Kernel 8.0 are required to install and run the VPR application.

VPR provides data from the VA FileMan 22.2 database to InterSystems’ HealthShare (HS) database. VPR runs only inside VistA and does *not* connect to or rely on the HS database.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VPR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* require any special system setup or configuration. It is a standard KIDS installation.

VPR is a developer tool; so, there are no end-user menus or security keys that need to be assigned.

### HealthShare

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR itself requires no setup to function; however, the [Enable Data Monitoring](#Enable_Data_Monitoring_Option) \[[VPR HS ENABLE](#VPR_HS_ENABLE_Option)\] option *must* be used to turn monitoring ON in accounts connected to a HealthShare (HS) server in order for the update list to populate in the ^VPR(“AVPR”) global. The HS team normally performs this task when a Production HealthShare system is stood up.

![](virtual-patient-record-vpr-technical-manual/016.png) CAUTION: In the future, if VA moves away from VPR and HealthShare, Data Monitoring *must* be turned OFF, so the ^VPR(“AVPR”) global does *not* grow indefinitely inside VistA.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the VA FileMan file distributed with VPR:

| File \# | File Name        | Global Location | Description                                                                                                                                                                                                                           |
|---------|------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 560     | VPR SUBSCRIPTION | ^VPR(       | This file contains patients who are monitored for changes to their medical record. It also contains two indices, AVPR and ANEW, to track changes to a patient’s record until retrieved by the Regional Health Connect server. |
| 560.1   | VPR CONTAINER    | ^VPR(560.1, | This file contains information about each SDA container class and how it is implemented, including the VistA source files.                                                                                                            |

<span id="_Ref525553020" class="anchor"></span>Table : VPR Routines

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the VPR routines with a summary description (listed alphabetically by routine name):

| Routine      | Description                                                        |
|--------------|--------------------------------------------------------------------|
| VPRD     | Main driver to serve VistA data as XML via RPC routine.            |
| VPRDCRC  | Compute CRC32 for VistA data routine.                              |
| VPRDGMPL | Problem extract routine for XML.                                   |
| VPRDGMRA | Allergy/Reaction extract routine for XML.                          |
| VPRDGMRC | Consult extract routine for XML.                                   |
| VPRDGMV  | Vitals extract routine for XML.                                    |
| VPRDGPF  | Patient Record Flags extract routine for XML.                      |
| VPRDIB   | Integrated Billing (insurance) extract routine for XML.            |
| VPRDJ    | Main driver to serve VistA data as JSON via RPC routine.           |
| VPRDJ0   | Serve VistA data as JSON via RPC (continued) routine.              |
| VPRDJ00  | Patient demographics extract routine for JSON.                     |
| VPRDJ01  | Orders extract routine for JSON.                                   |
| VPRDJ02  | Problems, Allergies, and Vitals extract routine for JSON.          |
| VPRDJ03  | Consults, Clin Procedures, and CLiO extract routine for JSON.      |
| VPRDJ04  | Appointments and Visits extract routine for JSON.                  |
| VPRDJ04A | Admissions and PTF extract routine for JSON.                       |
| VPRDJ05  | Medications by order extract routine for JSON.                     |
| VPRDJ05V | IV/Infusions extract routine for JSON.                             |
| VPRDJ06  | Laboratory extract routine for JSON.                               |
| VPRDJ07  | Radiology and Surgery extract routine for JSON.                    |
| VPRDJ08  | Text Integration Utilities (TIU) extract routine for JSON.         |
| VPRDJ08A | TIU (continued) extract routine for JSON.                          |
| VPRDJ09  | Patient Care Encounter (PCE) extract routine for JSON.             |
| VPRDJT   | Test VistA data JSON RPC routine.                                  |
| VPRDLR   | Laboratory extract routine for XML.                                |
| VPRDLRA  | Laboratory extract by accession routine for XML.                   |
| VPRDLRO  | Lab extract by order/panel routine for XML.                        |
| VPRDMC   | Clinical Procedures (Medicine) extract routine for XML.            |
| VPRDMDC  | CLiO extract routine for XML.                                      |
| VPRDOR   | Orders extract routine for XML.                                    |
| VPRDPROC | Procedure extract routine for XML.                                 |
| VPRDPS   | Pharmacy extract routine for XML.                                  |
| VPRDPSI  | Inpatient Pharmacy extract routine for XML.                        |
| VPRDPSO  | Outpatient Pharmacy extract routine for XML.                       |
| VPRDPSOR | Medication extract by order routine for XML.                       |
| VPRDPT   | Patient demographics extract routine for XML.                      |
| VPRDPXAM | PCE V Exams extract routine for XML.                               |
| VPRDPXED | PCE V Patient Education extract routine for XML.                   |
| VPRDPXHF | PCE Health Factors extract routine for XML.                        |
| VPRDPXIM | Immunizations extract routine for XML.                             |
| VPRDPXRM | Reminders extract routine for XML.                                 |
| VPRDPXSK | PCE V Skin Tests extract routine for XML.                          |
| VPRDRA   | Radiology extract routine for XML.                                 |
| VPRDRMIM | Functional Independence Measurement (FIM) extract routine for XML. |
| VPRDSDAM | Appointment extract routine for XML.                               |
| VPRDSR   | Surgical Procedures extract routine for XML.                       |
| VPRDTIU  | Text Integration Utility (TIU) extract routine for XML.            |
| VPRDTST  | Test VistA data XML RPC routine.                                   |
| VPRDVSIT | Visit/Encounter extract routine for XML.                           |
| VPREHL7  | VPR HL7 Message Processor routine.                                 |
| VPRENC   | VistA Encounter update routine.                                    |
| VPREVNT  | VistA event listeners routine.                                     |
| VPREVNT1 | VistA event listeners routine.                                     |
| VPREVSND | VistA order event listeners routine.                               |
| VPRHS    | HealthShare (HS) utilities routine.                                |
| VPRHST   | Test HS utilities routine.                                         |
| VPRHST1  | XML or JSON test objects routine.                                  |
| VPRHST2  | SDA upload global monitor routine.                                 |
| VPRHSX   | HS utilities management Options routine.                           |
| VPRHSX1  | HS Mgt Options routine cont.                                       |
| VPRHSX2  | Encounter Upload task monitor routine.                             |
| VPRIDX   | Create AVPR index post install routine.                        |
| VPRJSON  | Decode/Encode JSON routine.                                        |
| VPRJSOND | Decode JSON routine.                                               |
| VPRJSONE | Encode JSON routine.                                               |
| VPRP10   | VPR\*1.0\*10 patch post install routine                            |
| VPRP11I  | VPR\*1.0\*11 patch post install routine.                           |
| VPRP12I  | VPR\*1.0\*12 patch post install routine.                           |
| VPRP13I  | VPR\*1.0\*13 patch post install routine.                           |
| VPRP14   | VPR\*1.0\*14 patch post install routine.                           |
| VPRP15   | VPR\*1.0\*15 patch post install routine.                           |
| VPRP16   | VPR\*1.0\*16 patch post install routine.                           |
| VPRP20   | VPR\*1.0\*20 patch post install routine.                           |
| VPRP24   | VPR\*1.0\*24 patch post install routine.                           |
| VPRP26   | VPR\*1.0\*26 patch post install routine.                           |
| VPRP27   | VPR\*1.0\*27 patch post install routine.                           |
| VPRP28   | VPR\*1.0\*28 patch post install routine.                           |
| VPRP29   | VPR\*1.0\*29 patch post install routine.                           |
| VPRP30   | VPR\*1.0\*30 patch post install routine.                           |
| VPRP31   | VPR\*1.0\*31 patch post install routine.                           |
| VPRP2I   | VPR\*1.0\*2 patch post install routine.                            |
| VPRP5I   | VPR\*1.0\*5 patch post install routine.                            |
| VPRP8I   | VPR\*1.0\*8 patch post install routine.                            |
| VPRPATCH | VPR patch post install routine.                                    |
| VPRPCMM  | PCMM interface routine.                                            |
| VPRPI    | VPR package post install routine.                                  |
| VPRPROC  | Clinical Procedures interface routine.                             |
| VPRSDA   | SDA general utilities routine.                                     |
| VPRSDAB  | SDA Laboratory utilities routine.                                  |
| VPRSDAC  | SDA Consult utilities routine.                                     |
| VPRSDAD  | SDA DPT utilities routine.                                         |
| VPRSDADG | SDA DG utilities routine.                                          |
| VPRSDAF  | SDA Patient Record Flag utilities routine.                         |
| VPRSDAG  | SDA General Medical Record utilities routine.                      |
| VPRSDAHX | SDA Family/Social Hx utilities routine.                            |
| VPRSDAIB | SDA Integrated Billing utilities routine.                          |
| VPRSDAL  | SDA Allergy utilities routine.                                     |
| VPRSDAM  | SDA Scheduling utilities routine.                                  |
| VPRSDAOB | SDA Observation utilities routine.                                 |
| VPRSDAOR | SDA Order utilities routine.                                       |
| VPRSDAP  | SDA Pharmacy utilities routine.                                    |
| VPRSDAQ  | SDA queries routine.                                               |
| VPRSDAR  | SDA Radiology utilities routine.                                   |
| VPRSDASR | SDA Surgery utilities routine.                                     |
| VPRSDAT  | SDA TIU utilities routine.                                         |
| VPRSDAV  | SDA Visit utilities routine.                                       |
| VPRSDAVF | SDA V-file utilities routine.                                      |
| VPRSR    | Surgery interface routine.                                         |
| VPRUTILS | VPR utilities routine.                                             |

<span id="_Ref525553287" class="anchor"></span>Table : VPR Options

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the VPR options (listed alphabetically by option name):

<table>
<caption><p><span id="_Ref525636433" class="anchor"></span>Table : VPR Parameters</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 31%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VPR APPLICATION PROXY</td>
<td><strong>VPR Application Proxy</strong></td>
<td>This option allows the VPR connector proxy access to run the VPR remote procedure calls (RPCs) on this VistA system.</td>
</tr>
<tr class="even">
<td><span id="VPR_HS_ENABLE_Option" class="anchor"></span>VPR HS ENABLE</td>
<td><span id="Enable_Data_Monitoring_Option" class="anchor"></span><strong>Enable Data Monitoring</strong></td>
<td><p>This option enables or disables the tracking of patient data changes in the <strong>^VPR("AVPR")</strong> index, for retrieval by the Regional Health Connect server. This option is locked with the VPR HS ENABLE security key.</p>
<p>![](virtual-patient-record-vpr-technical-manual/017.png) CAUTION: Only use this option at the direction of Health Product Support (HPS) or development staff!</p></td>
</tr>
<tr class="odd">
<td>VPR HS LOG</td>
<td><strong>Data Upload List Log</strong></td>
<td>This option enables VPR to save a copy of the HealthShare upload list in <strong>^XTMP</strong> for testing or debugging purposes, for up to <strong>3 days</strong>. Sites can turn logging on or off here, as well as view the contents of the log.</td>
</tr>
<tr class="even">
<td>VPR HS MENU</td>
<td><strong>VPR HealthShare Utilities</strong></td>
<td>This menu contains utilities for managing the interface between the VPR and the Regional Health Connect (HC) servers.</td>
</tr>
<tr class="odd">
<td>VPR HS MGR</td>
<td><strong>HealthShare Interface Manager</strong></td>
<td>This is the primary menu for managing the VPR interface to HealthShare.</td>
</tr>
<tr class="even">
<td>VPR HS PATIENTS</td>
<td><strong>Inquire to Patient Subscriptions</strong></td>
<td>This option performs a lookup on the PATIENT (#2) file, then displays information about the selected patient's subscription status for HealthShare.</td>
</tr>
<tr class="odd">
<td>VPR HS PUSH</td>
<td><strong>Add Records to Upload List</strong></td>
<td>This option allows a site to add a patient record id(s) to the upload list, if it is suspected that the data cache has gotten out of synch.</td>
</tr>
<tr class="even">
<td>VPR HS SDA MONITOR</td>
<td><strong>SDA Upload List Monitor</strong></td>
<td>This option is a simple monitor of the <strong>^VPR("AVPR")</strong> global, which Health Connect polls every few seconds for data extracts; optionally filtered by patient and container.</td>
</tr>
<tr class="odd">
<td>VPR HS TASK MONITOR</td>
<td><strong>Encounter Transmission Task Monitor</strong></td>
<td>This option checks the status of the task that collects encounters and related records from Patient Care Encounter (PCE) and Text Integration Utilities (TIU) and moves them to the <strong>AVPR</strong> upload list for HealthShare. The task can be restarted here, if needed.</td>
</tr>
<tr class="even">
<td>VPR HS TEST</td>
<td><strong>Test SDA Extracts</strong></td>
<td>This option allows a site to run the data extracts for the Regional Health Connect server to view the SDA objects. No actual data is sent to HealthShare from this option; the results are only displayed on screen for testing or debugging purposes.</td>
</tr>
<tr class="odd">
<td>VPR HS TESTER</td>
<td><strong>Test/Audit VPR Functions</strong></td>
<td>This menu contains options to facilitate the audit and testing of the VPR interface with HealthShare.</td>
</tr>
<tr class="even">
<td>VPR PCMM PTPEVT TASK</td>
<td><strong>Nightly task to find team position changes</strong></td>
<td>This option looks for team position assignment changes and updates the patients in HealthShare linked to those positions. It can be scheduled to run overnight.</td>
</tr>
<tr class="odd">
<td>VPR TEST JSON</td>
<td><strong>View JSON results</strong></td>
<td><p>This option allows testers to run the data extracts for the legacy RPC and view JSON-formatted results.</p>
<p>![](virtual-patient-record-vpr-technical-manual/018.png) <strong>REF:</strong> For a more detailed description and example on the use of this option, see the <em>VPR Developer’s Guide</em>.</p></td>
</tr>
<tr class="even">
<td>VPR TEST XML</td>
<td><strong>View XML results</strong></td>
<td><p>This option allows testers to run the data extracts for the legacy RPC and view XML-formatted results.</p>
<p>![](virtual-patient-record-vpr-technical-manual/019.png) <strong>REF:</strong> For a more detailed description and example on the use of this option, see the <em>VPR Developer’s Guide</em>.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref525636433" class="anchor"></span>Table : VPR Parameters

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> lists the parameters released with VPR 1.0 (listed alphabetically by parameter name):

| VPR Parameter         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VPR OBS VIEW TYPE | This parameter names, or names types of, Clinical Observations (CLiO) observation collections that reside in the supplemental pages of flowsheets and group multiple, related observations. The CLiO groupings have no names or descriptions that other applications can display. By naming (or typing) these collections, the VPR OBS VIEW TYPE parameter enables applications that are interested in specific groups, such as groups that identify an instance of catheter care (e.g., Foley, IV, or drain), to display the information they contain. |
| VPR SYSTEM NAME   | This parameter holds the local VistA system’s name as a hashed hexadecimal (base 16) value. A VPR post-initialization routine calculates this value and places it into the system-level value; it should not be modified.                                                                                                                                                                                                                                                                                                                               |
| VPR VERSION       | This parameter holds the current version number of the VPR data-extract RPCs in the following form: *V.PP*, where *V* is the package version number and *PP* is the latest patch number.                                                                                                                                                                                                                                                                                                                                                        |

<span id="_Ref525556325" class="anchor"></span>Table : VPR ICRs

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no mail groups, alerts, or bulletins released with VPR 1.0.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR subscribes to many public integration control registrations (ICRs; <u>Table 6</u>) and provides a set of public remote procedure calls (RPCs; <u>Table 7</u>).

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the VPR Integration Control Registrations (ICRs) that cover usage of which routines and global references.

<table>
<caption><p><span id="_Ref525631170" class="anchor"></span>Table : VPR Remote Procedure Calls</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 55%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>ICR</th>
<th>Global or Routine Reference<br />
(Global References are prefixed with “^”)</th>
<th>Package</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5703</td>
<td><strong>^AUPNPROB</strong></td>
<td>Problem List</td>
</tr>
<tr class="even">
<td>2028</td>
<td><strong>^AUPNVSIT</strong></td>
<td>Patient Care Encounter (PCE)</td>
</tr>
<tr class="odd">
<td>4295</td>
<td><strong>^AUTTHF</strong></td>
<td>Patient Care Encounter (PCE)</td>
</tr>
<tr class="even">
<td>7014</td>
<td><strong>^DDE</strong></td>
<td>VA FileMan</td>
</tr>
<tr class="odd">
<td>1865</td>
<td><strong>^DGPM</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>3796</td>
<td><strong>^DGS(41.1)</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>767</td>
<td><strong>^DGSL(38.1)</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>733</td>
<td><strong>^DIC(31)</strong></td>
<td>HINQ</td>
</tr>
<tr class="odd">
<td>557</td>
<td><strong>^DIC(40.7)</strong></td>
<td>Scheduling</td>
</tr>
<tr class="even">
<td>723</td>
<td><strong>^DIC(42)</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>5597</td>
<td><strong>^DPT</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>5708</td>
<td><strong>^DPT(D0,.01)</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>6978</td>
<td><strong>^DPT(D0,‘S’)</strong></td>
<td>Scheduling</td>
</tr>
<tr class="even">
<td>7180</td>
<td><strong>^EDP(230)</strong></td>
<td>Emergency Department</td>
</tr>
<tr class="odd">
<td>2974</td>
<td><strong>^GMPL(125.8)</strong></td>
<td>Problem List</td>
</tr>
<tr class="even">
<td>4753</td>
<td><strong>^GMR(120.5)</strong></td>
<td>Gen. Med. Rec. – Vitals</td>
</tr>
<tr class="odd">
<td>6973</td>
<td><strong>^GMR(120.8)</strong></td>
<td>Adverse Reaction Tracking</td>
</tr>
<tr class="even">
<td>3449</td>
<td><strong>^GMR(120.86)</strong></td>
<td>Adverse Reaction Tracking</td>
</tr>
<tr class="odd">
<td>6974</td>
<td><strong>^GMRD(120.82)</strong></td>
<td>Adverse Reaction Tracking</td>
</tr>
<tr class="even">
<td>6975</td>
<td><strong>^GMRD(120.83)</strong></td>
<td>Adverse Reaction Tracking</td>
</tr>
<tr class="odd">
<td>524</td>
<td><strong>^LAB(61)</strong></td>
<td>Laboratory</td>
</tr>
<tr class="even">
<td>525</td>
<td><strong>^LR</strong></td>
<td>Laboratory</td>
</tr>
<tr class="odd">
<td>1963</td>
<td><strong>^LRO(68)</strong></td>
<td>Laboratory</td>
</tr>
<tr class="even">
<td>2407</td>
<td><strong>^LRO(69)</strong></td>
<td>Laboratory</td>
</tr>
<tr class="odd">
<td>5748</td>
<td><strong>^MDC(704.101)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="even">
<td>5809</td>
<td><strong>^MDC(704.102)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="odd">
<td>5999</td>
<td><strong>^MDC(704.1122)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="even">
<td>5995</td>
<td><strong>^MDC(704.116)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="odd">
<td>5996</td>
<td><strong>^MDC(704.1161)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="even">
<td>5810</td>
<td><strong>^MDC(704.117)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="odd">
<td>5811</td>
<td><strong>^MDC(704.118)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="even">
<td>6985</td>
<td><strong>^MDD(702)</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="odd">
<td>5771</td>
<td><strong>^OR(100)</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>6981</td>
<td><strong>^OR(100,D0,4.5)</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>5769</td>
<td><strong>^ORA(102.4)</strong></td>
<td>Care Management</td>
</tr>
<tr class="even">
<td>2638</td>
<td><strong>^ORD(100.01)</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>6982</td>
<td><strong>^ORD(100.98)</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>2843</td>
<td><strong>^ORD(101.43)</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>5909</td>
<td><strong>^PSB(53.79)</strong></td>
<td>Bar Code Med Admin (BCMA)</td>
</tr>
<tr class="even">
<td>4290</td>
<td><strong>^PXRMINDX</strong></td>
<td>Patient Care Encounter (PCE)</td>
</tr>
<tr class="odd">
<td>2480</td>
<td><strong>^RADPT</strong></td>
<td>Radiology/Nuclear Medicine</td>
</tr>
<tr class="even">
<td>2588</td>
<td><strong>^RADPT(‘AO’)</strong></td>
<td>Radiology/Nuclear Medicine</td>
</tr>
<tr class="odd">
<td>5605</td>
<td><strong>^RARPT</strong></td>
<td>Radiology/Nuclear Medicine</td>
</tr>
<tr class="even">
<td>2045</td>
<td><strong>^SCE(‘AVSIT’)</strong></td>
<td>Scheduling</td>
</tr>
<tr class="odd">
<td>5675</td>
<td><strong>^SRF(130)</strong></td>
<td>Surgery</td>
</tr>
<tr class="even">
<td>4872</td>
<td><strong>^SRO(136)</strong></td>
<td>Surgery</td>
</tr>
<tr class="odd">
<td>2321</td>
<td><strong>^TIU(8925.1)</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>5677</td>
<td><strong>^TIU(8925.1)</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>7416</td>
<td><strong>^TIU(8925.7)</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>5678</td>
<td><strong>^TIU(8926.1)</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>4984</td>
<td><strong>^USC(8932.1)</strong></td>
<td>Kernel</td>
</tr>
<tr class="even">
<td>6088</td>
<td><strong>^USR(8930)</strong></td>
<td>Authorization/Subscription Utility</td>
</tr>
<tr class="odd">
<td>6089</td>
<td><strong>^USR(8930.1)</strong></td>
<td>Authorization/Subscription Utility</td>
</tr>
<tr class="even">
<td>2248</td>
<td><strong>DGACT</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>7107</td>
<td><strong>DGPFAA</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>7108</td>
<td><strong>DGPFAAH</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>3860</td>
<td><strong>DGPFAPI</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>6130</td>
<td><strong>DGPTFUT</strong></td>
<td>Registration</td>
</tr>
<tr class="odd">
<td>4457</td>
<td><strong>DGPTPXRM</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>2977</td>
<td><strong>GMPLEDT3</strong></td>
<td>Problem List</td>
</tr>
<tr class="odd">
<td>2741</td>
<td><strong>GMPLUTL2</strong></td>
<td>Problem List</td>
</tr>
<tr class="even">
<td>6082</td>
<td><strong>GMRCAPI</strong></td>
<td>Consult/Request Tracking</td>
</tr>
<tr class="odd">
<td>2980</td>
<td><strong>GMRCGUIB</strong></td>
<td>Consult/Request Tracking</td>
</tr>
<tr class="even">
<td>2740</td>
<td><strong>GMRCSLM1</strong></td>
<td>Consult/Request Tracking</td>
</tr>
<tr class="odd">
<td>1446</td>
<td><strong>GMRVUT0</strong></td>
<td>Gen. Med. Rec. – Vitals</td>
</tr>
<tr class="even">
<td>7437</td>
<td><strong>GMVBMI</strong></td>
<td>Gen. Med. Rec. – Vitals</td>
</tr>
<tr class="odd">
<td>5702</td>
<td><strong>GMVRPCM</strong></td>
<td>Gen. Med. Rec. – Vitals</td>
</tr>
<tr class="even">
<td>5747</td>
<td><strong>ICDEX</strong></td>
<td>DRG Grouper</td>
</tr>
<tr class="odd">
<td>2503</td>
<td><strong>LR7OR1</strong></td>
<td>Laboratory</td>
</tr>
<tr class="even">
<td>2955</td>
<td><strong>LR7OU1</strong></td>
<td>Laboratory</td>
</tr>
<tr class="odd">
<td>4245</td>
<td><strong>LRPXAPI</strong></td>
<td>Laboratory</td>
</tr>
<tr class="even">
<td>4246</td>
<td><strong>LRPXAPIU</strong></td>
<td>Laboratory</td>
</tr>
<tr class="odd">
<td>4230</td>
<td><strong>MDPS1</strong></td>
<td>Clinical Procedures</td>
</tr>
<tr class="even">
<td>5493</td>
<td><strong>ORCD</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>3154</td>
<td><strong>ORQ1</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>4202</td>
<td><strong>ORQ12</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>5704</td>
<td><strong>ORQ12</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>2467</td>
<td><strong>ORX8 [$$OI, $VALUE]</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>3071</td>
<td><strong>ORX8 [$$PKGID]</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>871</td>
<td><strong>ORX8 [EN]</strong></td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>7084</td>
<td><strong>PSOBPSUT</strong></td>
<td>Outpatient Pharmacy</td>
</tr>
<tr class="even">
<td>2400</td>
<td><strong>PSOORRL</strong></td>
<td>Outpatient Pharmacy</td>
</tr>
<tr class="odd">
<td>6980</td>
<td><strong>PSOUTL</strong></td>
<td>Outpatient Pharmacy</td>
</tr>
<tr class="even">
<td>3373</td>
<td><strong>PSSUTLA1</strong></td>
<td>Pharmacy Data Management</td>
</tr>
<tr class="odd">
<td>2200</td>
<td><strong>PSXOPUTL</strong></td>
<td>CMOP</td>
</tr>
<tr class="even">
<td>1894</td>
<td><strong>PXAPI</strong></td>
<td>Patient Care Encounter (PCE)</td>
</tr>
<tr class="odd">
<td>4250</td>
<td><strong>PXPXRM</strong></td>
<td>Patient Care Encounter (PCE)</td>
</tr>
<tr class="even">
<td>4811</td>
<td><strong>PXRMMHV</strong></td>
<td>Clinical Reminders</td>
</tr>
<tr class="odd">
<td>4745</td>
<td><strong>RMIMRP</strong></td>
<td>Functional Independence</td>
</tr>
<tr class="even">
<td>3533</td>
<td><strong>SROESTV</strong></td>
<td>Surgery</td>
</tr>
<tr class="odd">
<td>5546</td>
<td><strong>TIUCNSLT</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>3568</td>
<td><strong>TIUCP</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>2693</td>
<td><strong>TIULQ</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>3058</td>
<td><strong>TIULX</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>2864</td>
<td><strong>TIUPP3</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>5676</td>
<td><strong>TIUSROI</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>4751</td>
<td><strong>TIUSRVLO [$$IMGCNT]</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>2834</td>
<td><strong>TIUSRVLO [$$RESOLVE]</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>2865</td>
<td><strong>TIUSRVLO [CONTEXT]</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>2944</td>
<td><strong>TIUSRVR1</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="odd">
<td>6077</td>
<td><strong>TIUVPR</strong></td>
<td>Text Integration Utilities</td>
</tr>
<tr class="even">
<td>2324</td>
<td><strong>USRLM</strong></td>
<td>Authorization/Subscription Utility</td>
</tr>
<tr class="odd">
<td>325</td>
<td><strong>VADPT2</strong></td>
<td>Registration</td>
</tr>
<tr class="even">
<td>7199</td>
<td><strong>WVRPCVPR</strong></td>
<td>Women’s Health</td>
</tr>
<tr class="odd">
<td>5925</td>
<td><strong>WVUTL11</strong></td>
<td>Women’s Health</td>
</tr>
<tr class="even">
<td>4677</td>
<td><strong>XUSAP</strong></td>
<td>Kernel</td>
</tr>
<tr class="odd">
<td>4911</td>
<td><strong>XUSTAX</strong></td>
<td>Kernel</td>
</tr>
<tr class="even">
<td>3521</td>
<td><strong>XUTMTP</strong></td>
<td>Kernel</td>
</tr>
<tr class="odd">
<td>4513</td>
<td><strong>YTQAPI5</strong></td>
<td>Mental Health</td>
</tr>
<tr class="even">
<td>5042</td>
<td><strong>YTQPXRM3</strong></td>
<td>Mental Health</td>
</tr>
<tr class="odd">
<td>5043</td>
<td><strong>YTQPXRM6</strong></td>
<td>Mental Health</td>
</tr>
</tbody>
</table>

<span id="_Ref525631170" class="anchor"></span>Table : VPR Remote Procedure Calls

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR has no *public* VPR Application Programming Interfaces (APIs), parameters, or variables for use by any other VistA products. VPR is intended to be called by external applications via remote procedure calls (RPCs) or the VA FileMan GET^DDE utility.

![](virtual-patient-record-vpr-technical-manual/020.png) REF: For developer information on how to set up VPR calls, see the *Virtual Patient record (VPR) Developer’s Guide*.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the remote procedure calls (RPCs) released with VPR 1.0 (listed alphabetically by RPC name):

| Remote Procedure Call         | M Entry Point | Category         |
|-------------------------------|---------------|------------------|
| VPR DATA VERSION          | VERSION^VPRD  | Supporting RPC   |
| VPR GET CHECKSUM          | CHECK^VPRDCRC | Supporting RPC   |
| VPR GET PATIENT DATA      | GET^VPRD      | Data Extract RPC |
| VPR GET PATIENT DATA JSON | GET^VPRDJ     | Data Extract RPC |

<span id="_Ref529972790" class="anchor"></span>Table : VPR HL7 Event Protocols and Associated Listeners

## HL7 Messaging and Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* send or receive any Health Level 7 (HL7) messages. VPR adds a listener to the HL7 event protocols listed in <u>Table 8</u>:

| Event Protocol                    | Listener            |
|-----------------------------------|---------------------|
| RMIM DRIVER                       | VPR RMIM EVENTS     |
| PSO VDEF RDS O13 OP PHARM PPAR VS | VPR PSO VDEF EVENTS |
| PSO VDEF RDS O13 OP PHARM PREF VS | VPR PSO VDEF EVENTS |
| VAFC ADT-A08 SERVER               | VPR ADT-A08 CLIENT  |

<span id="_Ref528831855" class="anchor"></span>Table : VPR *Non*-HL7 Event Protocols and Associated Listeners

VPR also monitors the *non*-HL7 event protocols listed in <u>Table 9</u>:

| Event Protocol                     | Listener               |
|------------------------------------|------------------------|
| DG FIELD MONITOR                   | VPR DG UPDATES         |
| DG PTF ICD DIAGNOSIS NOTIFIER      | VPR PTF EVENTS         |
| DG PTF ICD PROCEDURE NOTIFIER      | VPR PTF OP EVENTS      |
| DG SA FILE ENTRY NOTIFIER          | VPR DGS EVENTS         |
| DGPF PRF EVENT                     | VPR PRF EVENTS         |
| DGPM MOVEMENT EVENTS               | VPR INPT EVENTS        |
| FH EVSEND OR                       | VPR XQOR EVENTS        |
| GMPL EVENT                         | VPR GMPL EVENT         |
| GMRA ASSESSMENT CHANGE             | VPR GMRA ASSESSMENT    |
| GMRA ENTERED IN ERROR              | VPR GMRA ERROR EVENTS  |
| GMRA SIGN-OFF ON DATA              | VPR GMRA EVENTS        |
| GMRA VERIFY DATA                   | VPR GMRA EVENTS        |
| GMRC EVSEND OR                     | VPR XQOR EVENTS        |
| IBCN NEW INSURANCE EVENTS          | VPR IBCN EVENTS        |
| LR7O AP EVSEND OR                  | VPR XQOR EVENTS        |
| LR7O CH EVSEND OR                  | VPR XQOR EVENTS        |
| MDC OBSERVATION UPDATE             | VPR OBSERVATION UPDATE |
| OR EVSEND FH                       | VPR NA EVENTS          |
| OR EVSEND GMRC                     | VPR NA EVENTS          |
| OR EVSEND LRCH                     | VPR NA EVENTS          |
| OR EVSEND ORG                      | VPR XQOR EVENTS        |
| OR EVSEND PS                       | VPR NA EVENTS          |
| OR EVSEND RA                       | VPR NA EVENTS          |
| OR EVSEND VPR                      | VPR XQOR EVENTS        |
| PS EVSEND OR                       | VPR XQOR EVENTS        |
| PSB EVSEND VPR                     | VPR PSB EVENTS         |
| PXK VISIT DATA EVENT               | VPR PCE EVENTS         |
| RA EVSEND OR                       | VPR XQOR EVENTS        |
| SCMC PATIENT TEAM CHANGES          | VPR PCMM TEAM          |
| SCMC PATIENT TEAM POSITION CHANGES | VPR PCMM TEAM POSITION |
| SDAM APPOINTMENT EVENTS            | VPR APPT EVENTS        |
| TIU DOCUMENT ACTION EVENT          | VPR TIU RETRACT        |
| WV PREGNANCY STATUS CHANGE EVENT   | VPR PREGNANCY EVENT    |

<span id="_Ref10713709" class="anchor"></span>Table : VPR SAC Exemption

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR simply produces arrays of data strings. VPR is called by external clients, but the VPR application does *not* include or export any web services of its own.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Standards and Conventions (SAC)* document is a set of guidelines and standards that application developers *must* follow. Through a process of quality assurance, software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).

The SACC may grant exemptions from compliance with a particular section of the SAC for a specified timeframe.

<u>Table 10</u> lists the Standards and Conventions (SAC) exemption that was granted for VPR 1.0 on 4/29/2019:

<table>
<caption><p><span id="_Ref67735219" class="anchor"></span>Table : Troubleshooting Common VPR Issues</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Standards Section</th>
<th>Package Name</th>
<th>Package Version</th>
<th>Date Granted</th>
<th>Request Text</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.5.1.4</td>
<td>Virtual Patient Record</td>
<td>VPR*1.0</td>
<td>April 29, 2019</td>
<td><p>The Virtual Patient Record (VPR) application request an exemption to Section 2 of the Standards and Conventions (SAC). VPR wants to use the $Increment function which exists in Cache and isn’t in the 1995 M standard. This function allows multiple processes to increment the same global node without the use of a lock command and thus not creating a ‘race condition’ between multiple processes. VPR subscribes to all clinical Protocols that affect patient care. It tracks all changes in a single file, VPR SUBSCRIPTION (#560), that is monitored by Health Connect. Health Connect checks the “<strong>AVPR</strong>” cross reference using a sequence number, since the changes must be processed in the same sequence they were entered. The use of <strong>$I</strong> allow the cross reference to be created by multiple processes without the use of the lock command. This is what the cross reference looks like:</p>
<p><strong>^VPR("AVPR",seq#,DFN)=ICN^TYPE^ID^ACTION^VISIT</strong></p>
<p>This is from the Cache documents:</p>
<p><strong>$INCREMENT</strong> performs this increment as an atomic operation, which does <em>not</em> require the use of the <strong>LOCK</strong> command.</p>
<p>If multiple processes simultaneously increment the same global through <strong>$INCREMENT</strong>, each process receives a unique, increasing number (or decreasing number if <strong>num</strong> is negative).</p></td>
</tr>
</tbody>
</table>

<span id="_Ref67735219" class="anchor"></span>Table : Troubleshooting Common VPR Issues

![](virtual-patient-record-vpr-technical-manual/021.png) REF: For more information on the SAC or SAC exemptions, see the SACC intranet SharePoint site.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VPR routines, files, or options that *cannot* function independently.

## Software-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* create any software-wide variables.

# Global Journaling and Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR SUBSCRIPTION (#560) file is located in its own global, ^VPR(. The update list accumulates in the ^VPR(“AVPR”) index, so it can be managed as needed.

The VPR CONTAINER (#560.1) file is located in the ^VPRC(560.1) global. It is a small, static file holding implementation details for the SDA container classes.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* distribute any security menus or options.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR distributes one security key, to lock access to the Enable Data Monitoring \[VPR HS ENABLE\] option and prevent inadvertent disabling of the HealthShare interface.

<span id="_Toc157048679" class="anchor"></span>Figure : VPR HS ENABLE Security Key

NAME: VPR HS ENABLE DESCRIPTIVE NAME: Toggle VPR Interface

DESCRIPTION: This key controls access to the 'VPR HS ENABLE' option, which

toggles on/off the population of the upload global for HealthShare. It should only be assigned to primary system administrators.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File number ranges for VPR are 560 through 564. Currently, only the VPR SUBSCRIPTION (#560) and VPR CONTAINER (#560.1) files have been released.

<u>Figure 4</u> lists the *recommended* file security settings for access to the VPR SUBSCRIPTION (#560) and VPR CONTAINER (#560.1) files:

<span id="_Ref333476122" class="anchor"></span>Figure : File Security—Recommended VPR File Security Access

FILE SECURITY ACCESS Sep 25,2018 11:14 PAGE 1

DD RD WR DEL LAYGO AUDIT

NAME NUMBER ACCESS ACCESS ACCESS ACCESS ACCESS ACCESS

-----------------------------------------------------------------------------------

VPR SUBSCRIPTION 560 @ @ @ @ @ @

VPR CONTAINER 560.1 @ @ @ @ @ @

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* use any electronic signatures.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* itself send any data transmissions or make external calls; it is the application being called.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR has no data archiving capabilities.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR does *not* use any *non*-standard or special cross-references.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section anticipates any problems, issues, or items that a user may need assistance with and provide guidance to the extent possible. It includes any general troubleshooting tips.

The Virtual Patient Record (VPR) software is read-only, so that limits what can go wrong.

![](virtual-patient-record-vpr-technical-manual/022.png) REF: For developer information on how to set up VPR calls, see the *Virtual Patient record (VPR) Developer’s Guide*.

## Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the options located on the VPR HealthShare Utilities \[VPR HS MENU\] menu to help troubleshoot the VPR software.

<table>
<caption><p><span id="_Ref83911744" class="anchor"></span>Table : VPR Glossary of Terms and Acronyms</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 31%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th>Issue</th>
<th>Option</th>
<th>Instructions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Data is missing or incorrect in legacy RPC results.</td>
<td><ul>
<li><p><strong>View XML results</strong></p></li>
<li><p><strong>View JSON results</strong></p></li>
</ul></td>
<td>Use either option to view onscreen the data that can be returned via the VPR RPCs.</td>
</tr>
<tr class="even">
<td>Data is missing or incorrect in HealthShare.</td>
<td><ul>
<li><p><strong>Test SDA Extracts</strong></p></li>
<li><p><strong>Add Records to Upload List</strong></p></li>
</ul></td>
<td>Use this Test option to view onscreen the data that can be passed to HealthShare. If an error occurred, see the “<u>Special Instructions for Error Correction</u>” section.</td>
</tr>
<tr class="odd">
<td>A patient is <em>not</em> being tracked in HealthShare.</td>
<td><strong>Inquire to Patient Subscriptions</strong></td>
<td>Use this option to see a patient’s HealthShare subscription status. A patient <em>must</em> have an ICN, and <em>not</em> be merged or marked as a test patient.</td>
</tr>
<tr class="even">
<td>Data events are <em>not</em> processing for HealthShare.</td>
<td><strong>Data Upload List Log</strong></td>
<td>Use this option to capture and review the records sent to HealthShare; the log remains available for up to <strong>3 days</strong>.</td>
</tr>
<tr class="odd">
<td>Encounters and/or documents not flowing to HealthShare</td>
<td><strong>Encounter Transmission Task Monitor</strong></td>
<td>The encounter and document events are hit often, so record identifiers are captured in <strong>^XTMP</strong> where a task runs approximately every <strong>10 minutes</strong> to send them to HealthShare after editing. Use this option to monitor that task and restart it if necessary.</td>
</tr>
<tr class="even">
<td>No data flowing to HealthShare</td>
<td><strong>SDA Upload List Monitor</strong></td>
<td>Use this option to watch the contents of the upload list. HealthShare constantly monitors this list, so record identifiers should come and go from this list quickly.</td>
</tr>
</tbody>
</table>

<span id="_Ref83911744" class="anchor"></span>Table : VPR Glossary of Terms and Acronyms

![](virtual-patient-record-vpr-technical-manual/023.png) REF: For more information on the VPR options, see the “<u>Exported Options</u>” section.

## Protocol Events and Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If any updates are *not* going to HealthShare (HS), the site should check the protocol events and listeners included in this manual. For example, with the Computerized Patient Record System (CPRS) software, it was found that the protocol listeners can be “kicked off” the events if other applications are *not* careful when they update those events in their own patches.

![](virtual-patient-record-vpr-technical-manual/024.png) REF: For more information on the VPR protocol event and listeners, see the “<u>HL7 Messaging and Protocols</u>” section.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR is read-only and makes no changes to the VistA database. If an error is found in the error trap from a VPR call, it is generally due to hitting older data that may be incomplete or does *not* conform to current application requirements.

Sites should review any errors, and address those that are due to bad data. The HealthShare (HS) utility traps M errors when they occur. It then continues with the next record to process, so it may not be obvious at the time that errors occurred. If bad data is corrected, sites can use the Add Records to Upload List \[VPR HS PUSH\] option on the VPR HealthShare Utilities \[VPR HS MENU\] menu to get the record pulled into HS.

Software errors should still be reported via the usual methods ([Enterprise Service Desk](#enterprise-service-desk-and-organizational-contacts) or [YourIT](#yourit)), as VistA Maintenance is currently supporting the legacy RPCs.

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Information Technology (IT) support 24 hours a day, 365 days a year call the VA Enterprise Service Desk:

- Phone: 855-673-4357 or 888-326-6780

Enter an Incident or Request ticket (<span id="yourit" class="anchor"></span>YourIT) in Information Technology Service Management (ITSM) ServiceNow system via the shortcut on your workstation.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term           | Description                                                |
|----------------|------------------------------------------------------------|
| CLiO           | Clinical Observations                                      |
| CPRS           | Computerized Patient Record System                         |
| CRC            | Cyclic Redundancy Check                                    |
| DBIA           | Database Integration Agreement                             |
| DSO            | Development, Security, and Operations                      |
| ECR            | Edge Cache Repository                                      |
| EDIS           | Emergency Department Integration Software                  |
| EHRM           | Electronic Health Record Modernization                     |
| EPMO           | Enterprise Program Management Office                       |
| HC             | InterSystems’ Health Connect                               |
| hi<sup>2</sup> | Health Informatics Initiative                              |
| HMP            | Health Management Platform                                 |
| HS             | InterSystems’ HealthShare.                                 |
| ICR            | Integration Control Registration                           |
| IV             | Intravenous                                                |
| JLV            | Joint Legacy Viewer                                        |
| JSON           | JavaScript Object Notation                                 |
| KIDS           | Kernel Installation and Distribution System                |
| MPI            | Master Patient Index                                       |
| NPM            | National Patch Module                                      |
| NwHIN          | Network Nationwide Health Information Network              |
| OIT            | Office of Information and Technology                       |
| PCE            | Patient Care Encounter                                     |
| PS             | Product Support                                            |
| PTF            | Patient Treatment File                                     |
| RPC            | Remote Procedure Call                                      |
| SAC            | Standards and Conventions                                  |
| SDA            | Summary Document Architecture                              |
| SPM            | Software Product Management                                |
| UID            | Universal Identifier                                       |
| VHIE           | Veterans Health Information Exchange                       |
| VistA          | Veterans Health Information System Technology Architecture |
| VLER           | Virtual Lifetime Electronic Record                         |
| VPR            | Virtual Patient Record                                     |
| XML            | Extensible Markup Language                                 |
AcronymsA table containing acronymns that appear in the document with accompanying expansions
