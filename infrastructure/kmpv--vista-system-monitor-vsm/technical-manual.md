---
title: VSM Version 4 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: KMPV
app_name: VistA System Monitor (VSM)
section: INF
app_status: active
pkg_ns: KMPV
patch_ver: 4
patch_id: KMPV*4
group_key: "KMPV:KMPV:4"
file_numbers: 
  - 8969
security_keys: []
menu_options: 1
description: "--- title: | <span id=\\"_Toc186420068\\" class=\\"anchor\\"></span>VistA System Monitor (VSM) 4.0"
audience: 
keywords: 
  - strong
  - table
  - class
  - monitor
  - contents
  - kmpv
  - span
  - vista
  - metric
  - routine
page_count: 0
word_count: 15389
section_count: 46
table_count: 12
figure_count: 2
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=218"
---

---
title: |
  <span id="_Toc186420068" class="anchor"></span>VistA System Monitor (VSM) 4.0

  Technical Manual
---

![](vsm-version-4-technical-manual/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Software Product Management (SPM)

Capacity and Performance Engineering (CPE)

<span id="revision_history" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref431821080" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 44%" />
<col style="width: 28%" />
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
<td>01/22/2024</td>
<td>1.3</td>
<td><p>Updates for Patch KMP*4.0*4:</p>
<ul>
<li><p>Updated <u>Figure 1</u>.</p></li>
<li><p>Updated <u>Table 2</u>:</p></li>
</ul>
<ul>
<li><p>Changed Field #1.05 in File #8969 from TASKMAN SCHEDULE FREQUENCY to <a href="#HTTP_REQUEST_MAX_LENGTH_Field"><strong>HTTP REQUEST MAX LENGTH</strong></a>.</p></li>
<li><p>Changed Field #1.06 in File #8969 from TASKMAN SCHEDULE START to <a href="#MONITOR_START_DELAY_Field"><strong>MONITOR START DELAY</strong></a>.</p></li>
</ul>
<ul>
<li><p>Updated <u>Table 5</u>:</p></li>
</ul>
<ul>
<li><p>Moved the <strong>SETRETRY</strong> and <strong>DBTIMCHK</strong> entries.</p></li>
<li><p>Removed the <strong>RERROR</strong> entry.</p></li>
</ul>
<ul>
<li><p>Updated <u>Table 6</u>, <u>Table 7</u>, <u>Table 8</u>, <u>Table 9</u>, <u>Table 10</u>, and <u>Table 11</u>:</p></li>
</ul>
<ul>
<li><p>Moved the <strong>SETRETRY</strong> entry.</p></li>
<li><p>Removed the <strong>RERROR</strong> entry.</p></li>
</ul>
<ul>
<li><p>Updated <u>Table 12</u>:</p></li>
</ul>
<ul>
<li><p>Moved <strong>KMPWEB</strong> tag in the <a href="#KMPVRUN_Routine"><strong>KMPVRUN</strong></a> routine.</p></li>
<li><p>Deleted the <strong>PERFCHK</strong> tag from the <a href="#KMPVRUN_Routine"><strong>KMPVRUN</strong></a> routine.</p></li>
<li><p>Added <strong>PACKAGES</strong> tag to the <a href="#KMPUTLW_Routine"><strong>KMPUTLW</strong></a> routine.</p></li>
</ul>
<ul>
<li><p>Updated <u>Table 13</u>: Added the <strong>/StartMonitor</strong> and <strong>/GetRetryData</strong> URL paths.</p></li>
<li><p>Section <u>10.2</u>: Updated fourth and last bullet under “Data transmissions” list.</p></li>
</ul></td>
<td><ul>
<li><p>Capacity and Performance Engineering (CPE) Development Team</p></li>
<li><p>VistA Infrastructure Shared Services (VISS) Tech Writer</p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/14/2023</td>
<td>1.2</td>
<td><p>Updates for Patch KMP*4.0*3:</p>
<ul>
<li><p>Updated organizational references throughout: Changed references from “Enterprise Program Management Office (EPMO)” to “Software Product Management (SPM).</p></li>
<li><p>Edited monitor text to reflect no longer using TaskMan:</p></li>
</ul>
<ul>
<li><p>Step 3 in Sections <u>1.1.1.1</u>, <u>1.1.1.2</u>, <u>1.2.1.1</u>, <u>1.2.1.2</u>, <u>1.3.1.1</u>, <u>1.3.1.2</u>, <u>1.4.1.1</u>, <u>1.4.1.2</u>, <u>1.5.1.1</u>, <u>1.5.1.2</u>, <u>1.6.1.1</u>, <u>1.6.1.2</u>, <u>1.7.1.1</u>, and <u>1.7.1.2</u>.</p></li>
</ul>
<ul>
<li><p>Updated Sections <u>1.1.3</u>, <u>1.2.3</u>, <u>1.3.3</u>, <u>1.4.3</u>, <u>1.5.3</u>, <u>1.6.3</u>, and, <u>1.7.3</u> to better depict the metric transmission process</p></li>
<li><p>Updated <u>Table 2</u>: Added Note to <strong>TASKMAN SCHEDULE FREQUENCY</strong>, <strong>TASKMAN SCHEDULE START</strong>, and <strong>TASKMAN OPTION</strong> entries.</p></li>
<li><p>Updated <u>Table 5</u>: Added <strong>SETRETRY</strong> and <strong>DBTIMCHK</strong> entries.</p></li>
<li><p>Updated <u>Table 6</u>, <u>Table 7</u>, <u>Table 8</u>, <u>Table 9</u>, <u>Table 10</u>, and <u>Table 11</u>: Added <strong>SETRETRY</strong> entry.</p></li>
<li><p>Updated <u>Table 12</u>: Deleted the tags from routines:</p></li>
</ul>
<ul>
<li><p><strong>KMPVCBG</strong>:</p></li>
</ul>
<ul>
<li><p><strong>STOPJOB(KMPVMKEY)</strong></p></li>
<li><p><strong>DUPEJOB(KMPMKEY)</strong></p></li>
</ul>
<ul>
<li><p><strong>KMPUTLW</strong>:</p></li>
</ul>
<ul>
<li><p><strong>PACKAGES</strong></p></li>
<li><p><strong>KMPSSL</strong></p></li>
</ul>
<ul>
<li><p><strong>KMPSYNTH</strong>: <strong>KMPSSL</strong></p></li>
<li><p>Deleted routines: <strong>KMPPST3</strong>, <strong>KMPPST3A</strong>, and <strong>KMPPST3B</strong>.</p></li>
<li><p>Updated <strong>ERREXIT</strong> entry in the <strong>KMPVRUN</strong> routine.</p></li>
</ul>
<ul>
<li><p>Updated Section <u>8.3.3</u>: <u>Figure 21</u>.</p></li>
</ul></td>
<td><ul>
<li><p>Capacity and Performance Engineering (CPE) Development Team</p></li>
<li><p>VISS Tech Writer</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>07/01/2021</td>
<td>1.1</td>
<td>Updates for Patch KMP*4.0*2: Added new line tags in <strong>KMPVRUN</strong> entry in <u>Table 12</u>.</td>
<td>CPE Development Team</td>
</tr>
<tr class="even">
<td>07/22/2020</td>
<td>1.0</td>
<td><p>Initial VistA System Monitor (VSM) 3.0 Technical Manual:</p>
<ul>
<li><p>Upgraded to real time VistA System Monitor 3.0:</p></li>
<li><p>Changed transmission to real time using HyperText Transport Protocol (HTTP).</p></li>
<li><p>Updated the following monitors:</p></li>
</ul>
<ul>
<li><p>VistA Timed Collection Monitor (VTCM)</p></li>
<li><p>VistA Storage Monitor (VSTM)</p></li>
<li><p>VistA Business Event Monitor (VBEM)</p></li>
<li><p>VistA Message Count Monitor (VMCM)</p></li>
<li><p>VistA HL7 Monitor (VHLM)</p></li>
</ul>
<ul>
<li><p>Added the following new monitors:</p></li>
</ul>
<ul>
<li><p>Vista Coversheet Monitor (VCSM)</p></li>
<li><p>VistA Error Trap Monitor (VETM).</p></li>
</ul></td>
<td>CPE Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref431821080" class="anchor"></span>Table : Documentation Symbol Descriptions

Table of Contents

<span id="_Toc146547896" class="anchor"></span>List of Figures

<span id="_Toc146547897" class="anchor"></span>List of Tables

<span id="_Toc436814072" class="anchor"></span>Orientation

How to Use this Manual

The purpose of this guide is to provide instructions for use and maintenance of the Veterans Health Information Systems and Technology Architecture (VistA) Capacity and Performance Engineering (CPE) VistA System Monitor (VSM) 4.0 software, which is the third iteration of data collected as the overall capability has progressed.

Throughout this manual, advice and instructions are offered regarding the use of the VSM software and the functionality it provides for VistA software products.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Software Product Management (SPM)—System engineers and Capacity Management personnel responsible for enterprise capacity planning and system architecture.
- System Administrators—System administrators and Capacity Management personnel at local and regional Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- SPM Developers—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the VistA System Monitor (VSM) 4.0 software which is the third iteration of data collected as the overall capability has progressed; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Software Product Management (SPM) Intranet website.

![](vsm-version-4-technical-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](vsm-version-4-technical-manual/003.png)    | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](vsm-version-4-technical-manual/004.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref118123824" class="anchor"></span>Table : VSM CONFIGURATION (#8969) File—Field Descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*”is defined in the Approved Application Abbreviations document and “\<*N*\>” represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in VSM (KMP) test patient and user names would be documented as follows:

- KMPVPATIENT,ONE or KMPVUSER,ONE
- KMPVPATIENT,TWO or KMPVUSER,TWO
- KMPVPATIENT,THREE or KMPVUSER,THREE
- KMPVPATIENT,14 or KMPVUSER,14
- Etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](vsm-version-4-technical-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](vsm-version-4-technical-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to the toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](vsm-version-4-technical-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](vsm-version-4-technical-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](vsm-version-4-technical-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

<span id="_Toc397138035" class="anchor"></span>

Reference Materials

Readers who wish to learn more about VSM should consult the following:

- *VistA System Monitor (VSM) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *VistA System Monitor (VSM) User Manual*
- *VistA System Monitor (VSM) Technical Manual* (this manual)
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

Redacted versions of the VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>

![](vsm-version-4-technical-manual/010.png) REF: See the [VistA System Monitor (VSM) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=218).

Unredacted versions of the VistA documentation and software can be downloaded from the Product Support (PS) Network File Share (NFS) (formerly known as the “Anonymous Directories.

# Process Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Process Overview](#process-overview)
  - [VistA Timed Collection Monitor (VTCM) Specific Process](#vista-timed-collection-monitor-vtcm-specific-process)
    - [VTCM Monitor—Starting and Stopping](#vtcm-monitorstarting-and-stopping)
    - [VTCM Metric Collection](#vtcm-metric-collection)
    - [VTCM Metric Transmission](#vtcm-metric-transmission)
  - [VistA Message Count Monitor (VMCM) Specific Process](#vista-message-count-monitor-vmcm-specific-process)
    - [VMCM Monitor—Starting and Stopping](#vmcm-monitorstarting-and-stopping)
    - [VMCM Metric Collection](#vmcm-metric-collection)
    - [VMCM Metric Transmission](#vmcm-metric-transmission)
  - [VistA HL7 Monitor (VHLM) Specific Process](#vista-hl7-monitor-vhlm-specific-process)
    - [VHLM Monitor—Starting and Stopping](#vhlm-monitorstarting-and-stopping)
    - [VHLM Metric Collection](#vhlm-metric-collection)
    - [VHLM Metric Transmission](#vhlm-metric-transmission)
  - [VistA Storage Monitor (VSTM) Specific Process](#vista-storage-monitor-vstm-specific-process)
    - [VSTM Monitor—Starting and Stopping](#vstm-monitorstarting-and-stopping)
    - [VSTM Metric Collection](#vstm-metric-collection)
    - [VSTM Metric Transmission](#vstm-metric-transmission)
  - [VistA Business Event (VBEM) Specific Process](#vista-business-event-vbem-specific-process)
    - [VBEM Monitor—Starting and Stopping](#vbem-monitorstarting-and-stopping)
    - [VBEM Metric Collection](#vbem-metric-collection)
    - [VBEM Metric Transmission](#vbem-metric-transmission)
  - [VistA Coversheet Monitor (VCSM) Specific Process](#vista-coversheet-monitor-vcsm-specific-process)
    - [VCSM Monitor—Starting and Stopping](#vcsm-monitorstarting-and-stopping)
    - [VCSM Metric Collection](#vcsm-metric-collection)
    - [VCSM Metric Transmission](#vcsm-metric-transmission)
  - [VistA Error Trap Monitor (VETM) Specific Process](#vista-error-trap-monitor-vetm-specific-process)
    - [VETM Monitor—Starting and Stopping](#vetm-monitorstarting-and-stopping)
    - [VETM Metric Collection](#vetm-metric-collection)
    - [VETM Metric Transmission](#vetm-metric-transmission)
- [Files](#files)
  - [VSM CONFIGURATION (#8969) File; Global: ^KMPV(8969](#vsm-configuration-8969-file-global-kmpv8969)
    - [Data Dictionary](#data-dictionary)
    - [VSM CONFIGURATION (#8969) File—Field Descriptions](#vsm-configuration-8969-filefield-descriptions)
  - [VSM MONITOR DEFAULTS (#8969.02) File; Global: ^KMPV(8969.02](#vsm-monitor-defaults-896902-file-global-kmpv896902)
    - [Data Dictionary](#data-dictionary-1)
    - [Field Descriptions](#field-descriptions)
  - [VSM CACHE TASK LOG (#8969.03) File; Global: ^KMPV(8969.03](#vsm-cache-task-log-896903-file-global-kmpv896903)
    - [Data Dictionary](#data-dictionary-2)
    - [Field Descriptions](#field-descriptions-1)
  - [^KMPTMP(“KMPV”—Temporary Data Storage](#kmptmpkmpvtemporary-data-storage)
    - [VTCM Usage of ^KMPTMP](#vtcm-usage-of-kmptmp)
    - [VSTM Usage of ^KMPTMP](#vstm-usage-of-kmptmp)
    - [VMCM Usage of ^KMPTMP](#vmcm-usage-of-kmptmp)
    - [VHLM Usage of ^KMPTMP (SYNC/ASYNC)](#vhlm-usage-of-kmptmp-syncasync)
    - [VBEM Usage of ^KMPTMP](#vbem-usage-of-kmptmp)
    - [VCSM Usage of ^KMPTMP](#vcsm-usage-of-kmptmp)
    - [VETM Usage of ^KMPTMP](#vetm-usage-of-kmptmp)
- [Routines](#routines)
  - [VistA Timed Collection Monitor (VTCM) Specific Routine](#vista-timed-collection-monitor-vtcm-specific-routine)
  - [VistA Message Count Monitor (VMCM) Specific Routine](#vista-message-count-monitor-vmcm-specific-routine)
  - [VistA HL7 Monitor (VHLM) Specific Routine](#vista-hl7-monitor-vhlm-specific-routine)
  - [VistA Storage Monitor (VSTM) Specific Routine](#vista-storage-monitor-vstm-specific-routine)
  - [VistA Business Event Monitor (VBEM) Specific Routine](#vista-business-event-monitor-vbem-specific-routine)
  - [VistA Coversheet Monitor (VCSM) Specific Routine](#vista-coversheet-monitor-vcsm-specific-routine)
  - [VistA Error Trap Monitor (VETM) Specific Routine](#vista-error-trap-monitor-vetm-specific-routine)
  - [VSM Utility Routines](#vsm-utility-routines)
- [Exported Options](#exported-options)
  - [KMPV VSM MANAGEMENT Menu Option](#kmpv-vsm-management-menu-option)
  - [KMPV VTCM DATA RETRANSMISSION Option](#kmpv-vtcm-data-retransmission-option)
  - [KMPV VMCM DATA RETRANSMISSION Option](#kmpv-vmcm-data-retransmission-option)
  - [KMPV VHLM DATA RETRANSMISSION Option](#kmpv-vhlm-data-retransmission-option)
  - [KMPV VSTM DATA RETRANSMISSION Option](#kmpv-vstm-data-retransmission-option)
  - [KMPV VBEM DATA RETRANSMISSION Option](#kmpv-vbem-data-retransmission-option)
  - [KMPV VCSM DATA RETRANSMISSION Option](#kmpv-vcsm-data-retransmission-option)
  - [KMPV VETM DATA RETRANSMISSION Option](#kmpv-vetm-data-retransmission-option)
  - [KMPV-CLIENT-SRV Option—Deprecated](#kmpv-client-srv-optiondeprecated)
  - [KMPV MANAGEMENT MENU](#kmpv-management-menu)
- [Archiving](#archiving)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
- [External Relationships](#external-relationships)
  - [Caché Task Manager](#caché-task-manager)
  - [Dependencies](#dependencies)
    - [Packages](#packages)
- [Internal Relationships](#internal-relationships)
  - [LIST TEMPLATE (#409.61) File](#list-template-40961-file)
    - [KMPV MANAGEMENT List Template](#kmpv-management-list-template)
  - [PROTOCOL (#101) File](#protocol-101-file)
    - [KMPV START MONITOR Protocol](#kmpv-start-monitor-protocol)
    - [KMPV STOP MONITOR Protocol](#kmpv-stop-monitor-protocol)
    - [KMPV VIEW CFG Protocol](#kmpv-view-cfg-protocol)
    - [KMPV ALLOW TEST SYSTEM Protocol](#kmpv-allow-test-system-protocol)
    - [KMPV CONTACT Protocol](#kmpv-contact-protocol)
    - [KMPV DELETE DATA Protocol](#kmpv-delete-data-protocol)
    - [KMPV MANAGEMENT MENU Protocols](#kmpv-management-menu-protocols)
  - [FORM (#.403) File](#form-403-file)
    - [KMPV EDIT CONFIGURATION Form](#kmpv-edit-configuration-form)
    - [KMPV VIEW CONFIGURATION Form](#kmpv-view-configuration-form)
    - [Database Integration Agreements (IAs)](#database-integration-agreements-ias)
- [Global Variables](#global-variables)
- [Security](#security)
  - [Mail Group](#mail-group)
  - [Remote Systems](#remote-systems)
  - [Archiving](#archiving-1)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [References](#references)
- [Troubleshooting](#troubleshooting)
  - [Operational Support](#operational-support)
  - [VA Enterprise Service Desk (ESD) Support](#va-enterprise-service-desk-esd-support)
The Veterans Health Information Systems and Technology Architecture (VistA) System Monitor (VSM) 4.0 software is intended to collect Caché and VistA metrics related to system capacity and business usage. The package is made up of multiple collectors. The following seven collectors are deployed:
- [VistA Timed Collection Monitor (VTCM)](#vista-timed-collection-monitor-vtcm-specific-process)—Collects Caché metrics at regularly scheduled intervals such that they can be used in conjunction with metrics gathered via other deployed collection tools.
- [VistA Message Count Monitor (VMCM)](#vista-message-count-monitor-vmcm-specific-process)—Collects inbound and outbound Health Level Seven (HL7) and HL7 Optimized (HLO) message counts per logical link at regularly scheduled intervals.
- [VistA HL7 Monitor (VHLM)](#VMCM_metric_transmission_step_1)—Collects metadata about HL7 messages (SYNC and ASYNC) as well as HLO messages at regularly scheduled intervals.
- [VistA Storage Monitor (VSTM)](#VHLM_metric_transmission_step_1)—Collects storage metrics for each database twice monthly. This now includes the size of each global and information regarding the “0” node of each VistA file.
- [VistA Business Event Monitor (VBEM)](#_Toc489614196)—Collects Caché metrics for VistA functions (Menu Options, TaskMan Jobs and Remote Procedure Calls).
- [VistA Coversheet Monitor (VCSM)](#VBEM_metric_transmission_step_1)—Collects timing and metadata for CPRS coversheet loads at regularly scheduled intervals.
- [VistA Error Trap Monitor (VETM)](#VCSM_metric_transmission_step_1)—Collects data from the sites Kernel Error Trap, ERROR LOG (#3.075) file, at regularly scheduled intervals.
This data is used for understanding VistA systems as they relate to the infrastructure on which they are deployed.
As a general rule, any VSM monitor follows the following process (specifics for any monitor are listed below separately):
1.  Metrics are either collected on a periodic basis or aggregated to a similar time period. This allows metrics to be used in conjunction with those from other tools already being used within the VA.
10. Metrics are transferred from the VistA sites to the VSM national database via HyperText Transport Protocol (HTTP) or HyperText Transport Protocol Secure (HTTPS) per the monitors collection interval.
11. A purge function is executed: At 12:01 each morning the Cachè Task Manager runs the KMPVRUN routine. This routine is responsible for starting each individual monitor. Prior to starting each monitor, the KMPVRUN routine calls PURGEDLY^KMPVCBG. This line tag/routine deletes any data that is older than the number of days specified in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for that monitor type.
In some cases, the collection routine may need to run on each separate node of a VistA system. This is accomplished via a task in the Caché Task Manager. The Caché Task Manager executes a routine each morning immediately after midnight. This routine looks at each monitor in the VSM CONFIGURATION (#8969) file. It first checks to see if the monitor’s ONOFF (#.02) field value is set to ON. If so, it checks to see if the monitor has an entry in its CACHE DAILY TASK (#1.03) field. This field represents the name of the collection routine for a given monitor. If there is an entry in this field, then the Caché task executes the RUN line tag of this routine.

## VistA Timed Collection Monitor (VTCM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VTCM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VTCM Monitor

To start the VTCM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STRT action.
3.  Choose VTCM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VTCM entry.

![](vsm-version-4-technical-manual/011.png) NOTE: Collection of metrics does *not* commence until the next execute of the Caché Task Manager task.

#### Stopping VTCM Monitor

To stop the VTCM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STOP action.
3.  Choose VTCM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VTCM entry.

The collector stops upon its next iteration as it checks the ONOFF (#.02) field value before each collection.

![](vsm-version-4-technical-manual/012.png) NOTE: If the collection job is stopped via the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, then metric collection does *not* restart until 12:01 AM on the following day. If needed, collection can be started manually, but *must* be done on each separate node. To do this, enter the following at a programmer prompt on each node:

D RUN^KMPVVTCM

### VTCM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VTCM metrics are collected via calls to the %ZOSVKSD routine from the KMPTCMRT routine. This routine reads values from the following API calls:

- \##class(SYS.Stats.Dashboard).Sample()
- \##class(SYS.Stats.Routine).Sample()
- \##class(%SYSTEM.Config.SharedMemoryHeap).GetUsageSummary()
- \##class(%SYSTEM.Config.SharedMemoryHeap).FreeCount()

These calls are executed on a periodic basis as specified by the COLLECTION INTERVAL (#1.02) field in the VSM CONFIGURATION (#8969) file entry for VTCM. The default value is every five (5) minutes.

Metrics are stored for the day in the ^KMPTMP(“KMPV”,“VTCM” global by day (\$H), node and time slot.

![](vsm-version-4-technical-manual/013.png) REF: For details on file metrics, see Section <u>1.1.3</u>.

The collection routine, KMPVVTCM, runs until the start of a new day (new \$H value) unless the ONOFF (#.02) field value is set to OFF via the VSM MANAGEMENT menu option. Upon the next iteration of the collection process, the monitor checks this value and quits if turned OFF. If the monitor is turned OFF and back ON, metric collection does *not* resume until the start of the next day when the Caché Task Manager starts that day’s collection.

### VTCM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VTCM metric transmission process:

1.  <span id="VTCM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
2.  <span id="VTCM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
2.  Site immediately deletes that data.
3.  VTCM metric transmission process completed (skip [Step 3](#VTCM_metric_transmission_step_3)).
3.  <span id="VTCM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
4.  Site repeats Steps [1](#VTCM_metric_transmission_step_1)-[2](#VTCM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
5.  Site purges the data.

## VistA Message Count Monitor (VMCM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VMCM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VMCM Monitor

To start the VMCM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STRT action.
3.  Choose VMCM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VMCM entry.

![](vsm-version-4-technical-manual/014.png) NOTE: Collection of metrics does *not* commence until the next execute of the Caché Task Manager task.

#### Stopping VMCM Monitor

To stop the VMCM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STOP action.
3.  Choose VMCM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VMCM entry.

The collector stops upon its next iteration as it checks the ONOFF (#.02) field value before each collection.

![](vsm-version-4-technical-manual/015.png) NOTE: If the collection job is stopped via the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option then metric collection does *not* restart until 12:01 AM on the following day. If needed, collection can be started manually. To do this, enter the following at a programmer prompt on the back-end node:

D RUN^KMPVVMCM

### VMCM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VMCM metrics are collected via the routine KMPMCMRT. This routine reads values from the ^HLCS global. It iterates through the HL7 logical links and records messages received, messages processed, message to send and messages sent. Also, it looks at the ^HLSTATS global to get HLO messages sent and received.

These calls are executed on a periodic basis as specified by the COLLECTION INTERVAL (#1.02) field in the VSM CONFIGURATION (#8969) file entry for VMCM. The default value is every 15 minutes.

Metrics are transmitted to the national database after each collection via an HTTP message.

![](vsm-version-4-technical-manual/016.png) REF: For details on file metrics, see Section [1.2.3](#vmcm-metric-transmission).

The collection routine, KMPMCMRT, runs until the start of a new day (new \$H value) unless the ONOFF (#.02) field value is set to OFF via the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option. Upon the next iteration of the collection process, the monitor checks this value and quits if turned OFF. If the monitor is turned OFF and back ON, metric collection does *not* resume until the start of the next day when the Caché Task Manager starts that day’s collection.

### VMCM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VMCM metric transmission process:

1.  <span id="VMCM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
4.  <span id="VMCM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
6.  Site immediately deletes that data.
7.  VMCM metric transmission process completed (skip [Step 3](#VMCM_metric_transmission_step_3)).
5.  <span id="VMCM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
8.  Site repeats Steps [1](#VMCM_metric_transmission_step_1)-[2](#VMCM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
9.  Site purges the data.

## VistA HL7 Monitor (VHLM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VHLM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VHLM Monitor

To start the VHLM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
12. Choose the STRT action.
13. Choose VHLM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VHLM entry.

![](vsm-version-4-technical-manual/017.png) NOTE: Collection of metrics from the previous day will begin at the next scheduled TaskMan run.

#### Stopping VHLM Monitor

To stop the VHLM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STOP action.
3.  Choose VHLM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VHLM entry.

### VHLM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHLM metrics are collected via the routine KMPHLMRT. This routine reads values from the following globals:

- HL7 Messages:
- ^HL(772,
- ^HLMA
- HLO Messages:
- ^HLA
- ^HLB

It extracts metadata from each HL7 and HLO message in those globals from the previous day. Metrics include the following:

- Total Number of Characters
- Sending Application
- Receiving Application
- Message Protocol

  It does *not* collect any Personal Identifiable Information (PII)/ Personally-Identifiable Health Information (PHI) data.

![](vsm-version-4-technical-manual/018.png) REF: For details on file metrics, see Section [1.3.3](#_VHLM_Metric_Transmission).

<span id="_VHLM_Metric_Transmission" class="anchor"></span>

The collection routine, KMPHLMRT, runs until the start of a new day (new \$H value) unless the ONOFF (#.02) field value is set to OFF via the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option. Upon the next iteration of the collection process, the monitor checks this value and quits if turned OFF. If the monitor is turned OFF and back ON, metric collection does *not* resume until the start of the next day when the Caché Task Manager starts that day’s collection.

### VHLM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VHLM metric transmission process:

1.  <span id="VHLM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
6.  <span id="VHLM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
10. Site immediately deletes that data.
11. VHLM metric transmission process completed (skip [Step 3](#VHLM_metric_transmission_step_3)).
7.  <span id="VHLM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
12. Site repeats Steps [1](#VHLM_metric_transmission_step_1)-[2](#VHLM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
13. Site purges the data.

## VistA Storage Monitor (VSTM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VSTM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VSTM Monitor

To start the VSTM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STRT action.
3.  Choose VSTM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VSTM entry.

![](vsm-version-4-technical-manual/019.png) NOTE: Collection of metrics does *not* commence until the next execute of the Caché Task Manager task.

#### Stopping VSTM Monitor

To stop the VSTM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STOP action.
3.  Choose VSTM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VSTM entry.

The collector stops upon its next iteration as it checks the ONOFF (#.02) field value before each collection.

![](vsm-version-4-technical-manual/020.png) NOTE: The VSTM collector runs on the 1<sup>st</sup> and the 15<sup>th</sup> of each month.

### VSTM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSTM metrics are collected via the KMPSTMRT routine. This routine executes a portion the %FreeCnt routine logic to collect storage metrics for each database. It calls the legacy Statistical Analysis of Global Growth (SAGG) software to get global sizes and “0” node data.

![](vsm-version-4-technical-manual/021.png) REF: For details on file metrics, see Section [1.4.3](#vstm-metric-transmission).

### VSTM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VSTM metric transmission process:

1.  <span id="_Toc489614196" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
14. <span id="VSTM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
14. Site immediately deletes that data.
15. VSTM metric transmission process completed (skip [Step 3](#VSTM_metric_transmission_step_3)).
1.  <span id="VSTM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
16. Site repeats Steps [1](#_Toc489614196)-[2](#VSTM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
17. Site purges the data.

## VistA Business Event (VBEM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VBEM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VBEM Monitor

To start the VBEM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STRT action.
3.  Choose VBEM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VBEM entry.

![](vsm-version-4-technical-manual/022.png) NOTE: The collection of VBEM metrics begins immediately.

#### Stopping VBEM Monitor

To stop the VBEM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
2.  Choose the STOP action.
3.  Choose VBEM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VBEM entry.

The collector stops immediately.

### VBEM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VBEM metrics are collected via the KMPBEMRT routine. This routine reads the following values on a periodic basis as specified by the COLLECTION INTERVAL (#1.02) field in the VSM CONFIGURATION (#8969) file entry for VBEM:

- CPU
- Lines
- Commands
- GloRefs

The default value is every five (5) minutes.

![](vsm-version-4-technical-manual/023.png) REF: For details on file metrics, see Section [1.5.3](#vbem-metric-transmission).

The metric collection starts/stops immediately based on the ON/OFF switch in the VSM MANAGEMENT menu option.

### VBEM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VBEM metric transmission process:

1.  <span id="VBEM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
15. <span id="VBEM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
18. Site immediately deletes that data.
19. VBEM metric transmission process completed (skip [Step 3](#VBEM_metric_transmission_step_3)).
1.  <span id="VBEM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
20. Site repeats Steps [1](#VBEM_metric_transmission_step_1)-[2](#VBEM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
21. Site purges the data.

## VistA Coversheet Monitor (VCSM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VCSM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VCSM Monitor

To start the VCSM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
4.  Choose the STRT action.
5.  Choose VCSM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VCSM entry.

![](vsm-version-4-technical-manual/024.png) NOTE: The collection of VCSM metrics begins immediately.

#### Stopping VCSM Monitor

To stop the VCSM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
4.  Choose the STOP action.
5.  Choose VCSM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VCSM entry.

The collector stops immediately.

### VCSM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VCSM metrics are collected via the KMPCSMRT routine. This routine reads the following values on a periodic basis as specified by the COLLECTION INTERVAL (#1.02) field in the VSM CONFIGURATION (#8969) file entry for VCSM:

- Foreground Time
- Background Time
- Client Internet Protocol (IP) Address
- Patient Data File Number (DFN)[^1]

The default value is every five (5) minutes.

![](vsm-version-4-technical-manual/025.png) REF: For details on file metrics, see Section [<u>1.6.3</u>](#vbem-metric-transmission).

The metric collection starts/stops immediately based on the ON/OFF switch in the VSM MANAGEMENT menu option.

### VCSM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VCSM metric transmission process:

1.  <span id="VCSM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
16. <span id="VCSM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
22. Site immediately deletes that data.
23. VCSM metric transmission process completed (skip [Step 3](#VCSM_metric_transmission_step_3)).
1.  <span id="VCSM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
24. Site repeats Steps [1](#VCSM_metric_transmission_step_1)-[2](#VCSM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
25. Site purges the data.

## VistA Error Trap Monitor (VETM) Specific Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VETM Monitor—Starting and Stopping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting VETM Monitor

To start the VETM monitor, do the following:

1.  Use the VSM MANAGEMENT menu option.
6.  Choose the STRT action.
7.  Choose VETM at the monitor prompt. This sets the ONOFF (#.02) field to ON in the VSM CONFIGURATION (#8969) file for the VETM entry.

![](vsm-version-4-technical-manual/026.png) NOTE: The collection of VETM metrics begins immediately.

#### Stopping VETM Monitor

To stop the VETM monitor, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option, which is located under the Capacity Planning \[XTCM MAIN\] menu.
6.  Choose the STOP action.
7.  Choose VETM at the monitor prompt. This sets the ONOFF (#.02) field to OFF in the VSM CONFIGURATION (#8969) file for the VETM entry.

The collector stops immediately.

### VETM Metric Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VETM metrics are collected via the KMPETMRT routine. This routine reads the following values on a periodic basis as specified by the COLLECTION INTERVAL (#1.02) field in the VSM CONFIGURATION (#8969) file entry for VETM:

- Error
- Line
- Job Number
- Current IO

The default value is every 15 minutes.

![](vsm-version-4-technical-manual/027.png) REF: For details on file metrics, see Section [<u>1.7.3</u>](#vbem-metric-transmission).

### VETM Metric Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the VETM metric transmission process:

1.  <span id="VETM_metric_transmission_step_1" class="anchor"></span>Site transfers data to the CPE national database at each collection interval.
17. <span id="VETM_metric_transmission_step_2" class="anchor"></span>If CPE national database receives data, the following occurs:
1.  CPE National server sends an acknowledgement to the site upon receipt of the data.
26. Site immediately deletes that data.
27. VETM metric transmission process completed (skip [Step 3](#VETM_metric_transmission_step_3)).
18. <span id="VETM_metric_transmission_step_3" class="anchor"></span>If CPE national database does *not* receive data, the following occurs:
1.  Site stores the data on the VistA system until it reaches the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file. This is set to seven (7) days by default.
28. Site repeats Steps [1](#VETM_metric_transmission_step_1)-[2](#VETM_metric_transmission_step_2) until either of the following occurs:
- Data is successfully sent to the CPE national database.
- System reaches the date value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.
29. Site purges the data.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the files associated with the VistA System Monitor (VSM) application. The files are:

- <u>VSM CONFIGURATION (#8969) File; Global: ^KMPV(8969</u>
- <u>VSM MONITOR DEFAULTS (#8969.02) File; Global: ^KMPV(8969.02 - Deprecated</u>
- <u>VSM CACHE TASK LOG (#8969.03) File; Global: ^KMPV(8969.03</u>
- <u>^KMPTMP(“KMPV”—Temporary Data Storage</u>:
- [VTCM Usage of ^KMPTMP](#vtcm-usage-of-kmptmp)
- [VSTM Usage of ^KMPTMP](#vstm-usage-of-kmptmp)
- [VMCM Usage of ^KMPTMP](#_VMCM_Usage_of)
- [VHLM Usage of ^KMPTMP (SYNC/ASYNC)](#_VHLM_Usage_of)
- [VHLM Usage of ^KMPTMP (HLO)](#_VHLM_Usage_of_1)
- [VBEM Usage of ^KMPTMP](#vbem-usage-of-kmptmp)
- VCSM Usage of ^KMPTMP
- VETM Usage of ^KMPTMP

## VSM CONFIGURATION (#8969) File; Global: ^KMPV(8969

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref146542769" class="anchor"></span>Figure : VSM CONFIGURATION (#8969) File—Data Dictionary

STORED IN ^KMPV(8969, (7 ENTRIES) SITE: TEST.CENTRAL-TEXAS.MED.VA.GOV UCI:

XVT,ROU (VERSION 4.0)

-------------------------------------------------------------------------------

This file contains current configuration data related to the daily operation of

each monitor deployed.

CROSS

REFERENCED BY: MONITOR KEY(B)

^KMPV(8969,D0,0)= (#.01) MONITOR KEY \[1F\] ^ (#.02) ONOFF \[2S\] ^ (#.03) FULL

==\>NAME \[3F\] ^ (#.04) VERSION \[4N\] ^ (#.05) VERSION INSTALL

==\>DATE \[5D\] ^

^KMPV(8969,D0,1)= (#1.01) DAYS TO KEEP DATA \[1N\] ^ (#1.02) COLLECTION

==\>INTERVAL \[2N\] ^ (#1.03) CACHE DAILY TASK \[3F\] ^ (#1.04)

==\>ALLOW TEST SYSTEM \[4S\] ^ (#1.05) HTTP REQUEST MAX LENGTH

==\>\[5N\] ^ (#1.06) MONITOR START DELAY \[6N\] ^ (#1.07) TASKMAN

==\>OPTION \[7F\] ^ (#1.08) START PERFMON \[8S\] ^ (#1.09) ENCRYPT

==\>\[9S\] ^

^KMPV(8969,D0,2)= (#2.01) LAST START TIME \[1D\] ^ (#2.02) LAST STOP TIME \[2D\]

==\>^ (#2.03) LAST RUN TIME \[3N\] ^

^KMPV(8969,D0,3)= (#3.01) NATIONAL DATA EMAIL ADDRESS \[1F\] ^ (#3.02) NATIONAL

==\>SUPPORT EMAIL ADDRESS \[2F\] ^ (#3.03) VSM CFG EMAIL ADDRESS

==\>\[3F\] ^ (#3.04) LOCAL SUPPORT EMAIL ADDRESS \[4F\] ^

^KMPV(8969,D0,4)= (#4.01) NATIONAL IP ADDRESS \[1F\] ^ (#4.02) NATIONAL FQDN

==\>\[2F\] ^ (#4.03) NATIONAL PORT \[3N\] ^ (#4.04) APIKEY \[4F\] ^

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

^DIST(.403,149)= KMPV EDIT CONFIGURATION

^DIST(.404,526)= KMPV EDIT CFG

^DIST(.404,529)= KMPV EDIT TITLE

^DIST(.403,150)= KMPV VIEW CONFIGURATION

^DIST(.404,527)= KMPV VIEW CFG

^DIST(.404,528)= KMPV VIEW TITLE

### VSM CONFIGURATION (#8969) File—Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc146548025" class="anchor"></span>Table : VSM MONITOR DEFAULTS (#8969.02) File—Field Descriptions</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Field Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MONITOR KEY</td>
<td>8969, .01</td>
<td><strong>Four</strong> Letter acronym used to identify specific monitor.</td>
</tr>
<tr class="even">
<td>ONOFF</td>
<td>8969, .02</td>
<td>Flag used to stop or continue monitor collection.</td>
</tr>
<tr class="odd">
<td>FULL NAME</td>
<td>8969, .03</td>
<td>Descriptive name for specific monitor. Usually related to the Monitor Key. For example, <strong>VTCM</strong> = <strong>VistA Timed Collection Monitor</strong>.</td>
</tr>
<tr class="even">
<td>VERSION</td>
<td>8969, .04</td>
<td>Current version of VSM software.</td>
</tr>
<tr class="odd">
<td>INSTALL DATE</td>
<td>8969, .05</td>
<td>Date current version of software was installed.</td>
</tr>
<tr class="even">
<td>DAYS TO KEEP DATA</td>
<td>8969, 1.01</td>
<td>Number of days that unsent data is allowed to remain in <strong>^KMPTMP(“KMPV”</strong> before the purge routine kills it. Limited to <strong>3-7 days</strong>. Data older than this value is deleted; regardless of the reason it has <em>not</em> been sent to the national database, in order to assure global does <em>not</em> grow unchecked.</td>
</tr>
<tr class="odd">
<td>COLLECTION INTERVAL</td>
<td>8969, 1.02</td>
<td>The number in minutes used to gather or aggregate metrics. Monitors that collect metrics on a periodic basis use this value to wait between collections. Monitors that collect data continuously use this value for aggregation of metrics.</td>
</tr>
<tr class="even">
<td>CACHE DAILY TASK</td>
<td>8969, 1.03</td>
<td>The name of the routine, if applicable, to start each day’s collection. The Caché Task Manager calls the <strong>RUN</strong> line tag of this routine at the start of every day. This allows collection tasks to run on each node of a VistA system: <strong>front-end</strong> and <strong>back-end</strong>.</td>
</tr>
<tr class="odd">
<td>ALLOW TEST SYSTEM</td>
<td>8969, 1.04</td>
<td>If set to <strong>YES,</strong> this allows the monitors to run on test systems. Otherwise monitors exit if the current UCI is <em>not</em> set as <strong>PROD</strong> per <strong>^%ZOSF(“UCI”)</strong>.</td>
</tr>
<tr class="even">
<td><span id="HTTP_REQUEST_MAX_LENGTH_Field" class="anchor"></span>HTTP REQUEST MAX LENGTH</td>
<td>8969, 1.05</td>
<td>This number represents the maximum number of characters that can be sent in a single HTTP Request body.</td>
</tr>
<tr class="odd">
<td><span id="MONITOR_START_DELAY_Field" class="anchor"></span>MONITOR START DELAY</td>
<td>8969, 1.06</td>
<td>This number represents the maximum number of seconds to delay starting the VSM monitors. The purpose is to lower the arrival rate of HTTP messages at the receiving application.</td>
</tr>
<tr class="even">
<td>TASKMAN OPTION</td>
<td>8969, 1.07</td>
<td><strong>Deprecated.</strong> The OPTION (#19) file entry used by TaskMan to schedule the daily background jobs.</td>
</tr>
<tr class="odd">
<td>START PERFMON</td>
<td>8969, 1.08</td>
<td><p>The <a href="#KMPVRUN_Routine"><strong>KMPVRUN</strong></a> routine executes daily immediately after midnight:</p>
<ul>
<li><p>If <strong>START PERFMON</strong> is set to <strong>1</strong>, then this routine attempts to start the Performance Monitor if it is <em>not</em> running.</p></li>
<li><p>If <strong>START PERFMON</strong> is set to <strong>0</strong>, this section of code is skipped.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>ENCRYPT</td>
<td>8969, 1.09</td>
<td><ul>
<li><p>If set to <strong>1</strong> (<strong>YES</strong>), then VSM HTTP requests are sent using Secure Socket Layer (SSL)/Transport Layer Security (TLS) encryption (HTTPS).</p></li>
<li><p>If set to <strong>0</strong> (<strong>NO</strong>), then HTTP requests will be sent <em>without</em> SSL/TLS encryption (HTTP).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>LAST START TIME</td>
<td>8969, 2.01</td>
<td><strong>Deprecated.</strong> Time last TaskMan task was started for a specific monitor.</td>
</tr>
<tr class="even">
<td>LAST STOP TIME</td>
<td>8969, 2.02</td>
<td><strong>Deprecated.</strong> Time last TaskMan task completed for a specific monitor.</td>
</tr>
<tr class="odd">
<td>LAST RUN TIME</td>
<td>8969, 2.03</td>
<td><strong>Deprecated.</strong> Time in seconds from start to completion of most recent run for a specific monitor TaskMan task.</td>
</tr>
<tr class="even">
<td>NATIONAL DATA EMAIL ADDRESS</td>
<td>8969, 3.01</td>
<td><strong>Deprecated.</strong> Email address used to send metric data to the national Capacity and Performance Engineering (CPE) database.</td>
</tr>
<tr class="odd">
<td>NATIONAL SUPPORT EMAIL ADDRESS</td>
<td>8969, 3.02</td>
<td>Email address used to send messages to the CPE VistA CP mail group.</td>
</tr>
<tr class="even">
<td>VSM CFG EMAIL ADDRESS</td>
<td>8969, 3.03</td>
<td><strong>Deprecated.</strong> Email address used to send data other than daily metrics to CPE national database.</td>
</tr>
<tr class="odd">
<td>LOCAL SUPPORT EMAIL ADDRESS</td>
<td>8969, 3.04</td>
<td>Optional email address for local support personnel. If present, any email that would be sent to the national support group also goes to the local support group.</td>
</tr>
<tr class="even">
<td>NATIONAL IP ADDRESS</td>
<td>8969, 4.01</td>
<td>This field holds the IP address of the national system receiving VSM metric data transmissions.</td>
</tr>
<tr class="odd">
<td>NATIONAL FQDN</td>
<td>8969, 4.02</td>
<td>This field holds the fully qualified domain name of the service receiving metric data from VSM.</td>
</tr>
<tr class="even">
<td>NATIONAL PORT</td>
<td>8969, 4.03</td>
<td><p>This field contains the port number of the national service receiving VSM metrics. This field is only used if the following ports are <em>not</em> to be used:</p>
<ul>
<li><p>HTTP: Standard port <strong>&lt;REDACTED&gt;</strong>.</p></li>
<li><p>HTTPS: Port <strong>&lt;REDACTED&gt;</strong>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>API KEY</td>
<td>8969, 4.04</td>
<td>Header key for Amazon Web Services (AWS) API Gateway.</td>
</tr>
</tbody>
</table>

<span id="_Toc146548025" class="anchor"></span>Table : VSM MONITOR DEFAULTS (#8969.02) File—Field Descriptions

## VSM MONITOR DEFAULTS (#8969.02) File; Global: ^KMPV(8969.02

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548002" class="anchor"></span>Figure : VSM MONITOR DEFAULTS (#8969.02) File—Data Dictionary

CROSS REFERENCED BY: MONITOR KEY(B)

 

^KMPV(8969.02,D0,0)= (#.01) MONITOR KEY \[1F\] ^ (#.02) DAYS TO KEEP DATA \[2N\] ^

(#.03) COLLECTION INTERVAL \[3N\] ^ (#.04) CACHE DAILY TASK \[4F\] ^

(#.05) ALLOW TEST SYSTEM \[5S\] ^ (#.06) TASKMAN SCHEDULE FREQUENCY \[6F\] ^

(#.07) TASKMAN SCHEDULE START \[7F\] ^ (#.08) TASKMAN OPTION \[8F\] ^

KMPV(8969.02,D0,1)= (#1.01) NATIONAL DATA EMAIL ADDRESS \[1F\] ^

(#1.02) NATIONAL SUPPORT EMAIL ADDRESS \[2F\] ^ (#1.03) VSM CFG EMAIL ADDRESS \[3F\] ^

### Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc146548026" class="anchor"></span>Table : VSM CACHE TASK LOG (#8969.03) File—Field Descriptions</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Field Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MONITOR KEY</td>
<td>8969.02, .01</td>
<td><strong>Two</strong> to <strong>four</strong> letter acronyms used to identify specific monitor.</td>
</tr>
<tr class="even">
<td>DAYS TO KEEP DATA</td>
<td>8969.02, .02</td>
<td>Number of days that unsent data is allowed to remain in <strong>^KMPTMP(“KMPV”</strong> before the purge routine kills it. Limited to <strong>3-7 days</strong>. Data older than this value is deleted; regardless of the reason it has <em>not</em> been sent to the national database, in order to assure global does <em>not</em> grow unchecked.</td>
</tr>
<tr class="odd">
<td>COLLECTION INTERVAL</td>
<td>8969.02, .03</td>
<td>The number in minutes used to gather or aggregate metrics. Monitors that collect metrics on a periodic basis use this value to wait between collections. Monitors that collect data continuously use this value for aggregation of metrics.</td>
</tr>
<tr class="even">
<td>CACHE DAILY TASK</td>
<td>8969.02, .04</td>
<td>The name of the routine, if applicable, to start each day’s collection. The Caché Task Manager calls the <strong>RUN</strong> line tag of this routine at the start of every day. This allows collection tasks to run on each node of a VistA system: <strong>front-end</strong> and <strong>back-end</strong>.</td>
</tr>
<tr class="odd">
<td>ALLOW TEST SYSTEM</td>
<td>8969.02, .05</td>
<td>If set to <strong>YES,</strong> this allows the monitors to run on test systems. Otherwise monitors exit if the current UCI is <em>not</em> set as <strong>PROD</strong> per <strong>^%ZOSF(“UCI”)</strong>.</td>
</tr>
<tr class="even">
<td>TASKMAN SCHEDULE FREQUENCY</td>
<td>8969.02, .06</td>
<td>The value used to automatically reschedule the TaskMan tasks. (e.g., <strong>1D</strong> or <strong>1W</strong>).</td>
</tr>
<tr class="odd">
<td>TASKMAN SCHEDULE START</td>
<td>8969.02, .07</td>
<td>The time each monitor's TaskMan task should be scheduled. (e.g., <strong>T+1@0001</strong>).</td>
</tr>
<tr class="even">
<td>TASKMAN OPTION</td>
<td>8969.02, .08</td>
<td>The OPTION (#19) file entry used by TaskMan to schedule the daily background jobs.</td>
</tr>
<tr class="odd">
<td>START PERFMON</td>
<td>8969.02, .09</td>
<td><p>The <strong>KMPVRUN</strong> routine executes daily immediately after midnight:</p>
<ul>
<li><p>If <strong>START PERFMON</strong> is set to <strong>1</strong>, then this routine attempts to start the Performance Monitor if it is <em>not</em> running.</p></li>
<li><p>If <strong>START PERFMON</strong> is set to <strong>0</strong>, this section of code is skipped.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>ENCRYPT</td>
<td>8969.02, .1</td>
<td><ul>
<li><p>If set to <strong>1</strong> (<strong>YES</strong>), then VSM HTTP requests are sent using SSL/TLS encryption (HTTPS).</p></li>
<li><p>If set to <strong>0</strong> (<strong>NO</strong>), then HTTP requests are sent without SSL/TLS encryption (HTTP).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>NATIONAL DATA EMAIL ADDRESS</td>
<td>8969.02, 1.01</td>
<td>Email address used to send metric data to the national CPE database.</td>
</tr>
<tr class="even">
<td>NATIONAL SUPPORT EMAIL ADDRESS</td>
<td>8969.02, 1.02</td>
<td>Email address used to send messages to the CPE VistA CP mail group.</td>
</tr>
<tr class="odd">
<td>VSM CFG EMAIL ADDRESS</td>
<td>8969.02, 1.03</td>
<td>Email address used to send data other than daily metrics to CPE national database.</td>
</tr>
<tr class="even">
<td>NATIONAL IP ADDRESS</td>
<td>8969.02, 2.01</td>
<td>This field holds the IP address of the national system receiving VSM metric data transmissions.</td>
</tr>
<tr class="odd">
<td>NATIONAL FQDN</td>
<td>8969.02, 2.02</td>
<td>This holds the fully qualified domain name of the service receiving metric data from VSM.</td>
</tr>
<tr class="even">
<td>NATIONAL PORT</td>
<td>8969.02, 2.03</td>
<td><p>This contains the port number of the national service receiving VSM metrics. This field is only used if the following ports are <em>not</em> to be used:</p>
<ul>
<li><p>HTTP: Standard port <strong>&lt;REDACTED&gt;</strong>.</p></li>
<li><p>HTTPS: port <strong>&lt;REDACTED&gt;</strong>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>API KEY</td>
<td>8969.02, 2.04</td>
<td>Header key for AWS API Gateway.</td>
</tr>
</tbody>
</table>

<span id="_Toc146548026" class="anchor"></span>Table : VSM CACHE TASK LOG (#8969.03) File—Field Descriptions

## VSM CACHE TASK LOG (#8969.03) File; Global: ^KMPV(8969.03

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548003" class="anchor"></span>Figure : VSM CACHE TASK LOG (#8969.03) File—Data Dictionary

CROSS REFERENCED BY: DATE(B)

 

INDEXED BY: DATE & NODE (C)

 

^KMPV(8969.03,D0,0)= (#.01) DATE \[1D\] ^ (#.02) NODE \[2F\] ^ (#.03) VTCM RUNTIME \[3D\] ^

(#.04) VSTM RUNTIME \[4D\] ^ (#.05) VMCM RUNTIME \[5D\]

### Field Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name   | Field Number | Description                                                                                    |
|--------------|--------------|------------------------------------------------------------------------------------------------|
| DATE         | 8969.03, .01 | Run date for specific monitor as started from The Caché Task Manager.                          |
| NODE         | 8969.03, .02 | Specific node on which collection routine was run.                                             |
| VTCM RUNTIME | 8969.03, .03 | Time the VistA Timed Collection Monitor (VTCM) was started in VA FileMan date/time format. |
| VSTM RUNTIME | 8969.03, .04 | Time the VistA Storage Monitor (VSTM) was started in VA FileMan date/time format.          |
| VMCM RUNTIME | 8969.03, .05 | Time the VistA Message Count Monitor (VMCM) was started in VA FileMan date/time format.    |

<span id="_Ref118127128" class="anchor"></span>Table : VTCM Routine

## ^KMPTMP(“KMPV”—Temporary Data Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^KMPTMP is a temporary global used by multiple KMP packages including KMPV – VistA System Monitor.

![](vsm-version-4-technical-manual/028.png) CAUTION: This global is *not* in VA FileMan format and should *not* be journaled.

The following sections document how the VSM monitors use this global.

### VTCM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VTCM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “VTCM”, “TEMP”) holds metrics from the previous collection. These are used to determine the difference between the previous and current collections to provide metrics/second.
- ^KMPTMP (“KMPV”, “VTCM”, “RETRY”) holds JavaScript Object Notation (JSON) strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VTCM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

### VSTM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSTM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “VSTM”, “TRANSMIT”) temporarily collates collected data from transmission.
- ^KMPTMP (“KMPV”, “VSTM”, “RETRY”) holds JSON strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VSTM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

<span id="_VMCM_Usage_of" class="anchor"></span>

### VMCM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VMCM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “VMCM”, “PREVIOUS”) holds metrics from the previous collection. This is used to find the number of messages per the current time period.
- ^KMPTMP (“KMPV”, “VMCM”, “TRANSMIT”) temporarily collates collected data from transmission.
- ^KMPTMP (“KMPV”, “VMCM”, “RETRY”) holds JSON strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VMCM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

### VHLM Usage of ^KMPTMP (SYNC/ASYNC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHLM^KMPTMP (SYNC/ASYNC) usage:

- ^KMPTMP (“KMPV”, “VHLM”, “TRANSMIT”) temporarily collates collected data from transmission.
- ^KMPTMP (“KMPV”, “VHLM”, “RETRY”) holds JSON strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VHLM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

### VBEM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VBEM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “VBEM”, “DLY”) stores raw metrics as they are collected upon execution of:
- Menu Options
- RPC Calls
- TaskMan Options
- ^KMPTMP (“KMPV”, “VBEM”, “COMPRESS”) aggregates metrics, removing the individual job numbers.
- ^KMPTMP (“KMPV”, “VBEM”, “TRANSMIT”) temporarily collates collected data from transmission.
- ^KMPTMP (“KMPV”, “VBEM”, “RETRY”) holds JSON strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VBEM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

### VCSM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VCSM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “KMPDT”, “ORWCV”) backgrounds Coversheet Timings based on actual RPC events.
- ^KMPTMP (“KMPV”, “KMPDT”, “ORWCV-FT”) foregrounds Coversheet Timings based on actual RPC events.
- ^KMPTMP (“KMPV”, “VCSM”, “TRANSMIT”) temporarily collates collected data from transmission.
- ^KMPTMP (“KMPV”, “VCSM”, “RETRY”) holds JSON strings for messages sent to the national database that received no acknowledgement. It attempts to resend via the KMPV VCSM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

### VETM Usage of ^KMPTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VETM^KMPTMP usage:

- ^KMPTMP (“KMPV”, “VETM”, “TEMP”) stores the last error number transmitted.
- ^KMPTMP (“KMPV”, “VETM”, “RETRY”) holds JSON strings for messages sent to the national database that received no Acknowledgement. It attempts to resend via the KMPV VETM DATA RETRANSMISSION tasked option once a day up to the number of days specified in the DAYS TO KEEP DATA (#1.01) configuration field in the VSM CONFIGURATION (#8969) file.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the routines and line tags for VistA System Monitor (VSM) monitors. The routines include:

- <u>VistA Timed Collection Monitor (VTCM) Specific Routine</u>
- [VistA Message Count Monitor (VMCM) Specific Routines](#vista-message-count-monitor-vmcm-specific-routine)
- [VistA HL7 Monitor (VHLM) Specific Routines](#vista-hl7-monitor-vhlm-specific-routine)
- <u>VistA Storage Monitor (VSTM) Specific Routine</u>
- [VistA Business Event Monitor (VBEM) Specific Routines](\l)
- [VistA Coversheet Monitor (VCSM) Specific Routines](#vista-coversheet-monitor-vcsm-specific-routine)
- [VistA Error Trap Monitor (VETM) Specific Routines](#vista-error-trap-monitor-vetm-specific-routine)
- <u>VSM Utility Routines</u>

## VistA Timed Collection Monitor (VTCM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPTCMRT |          | Collect Caché Metrics for the VistA Timed Collection Monitor.                                                 |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | DBTIMCHK | Calculates the delta in system time between the application servers and the database server.                      |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193520" class="anchor"></span>Table : VMCM Routine

## VistA Message Count Monitor (VMCM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPMCMRT |          | Collect message metrics for the VistA Message Count Monitor.                                                  |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | HLODAILY | Collect HLO metrics.                                                                                              |
|              | CALCDELT | Calculate the delta between the previous and current collections.                                                 |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193629" class="anchor"></span>Table : VHLM Routine

## VistA HL7 Monitor (VHLM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPHLMRT |          | Collect HL7/HLO metrics for the VistA HL7 Monitor.                                                            |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193732" class="anchor"></span>Table : VSTM Routine

## VistA Storage Monitor (VSTM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPSTMRT |          | Collect storage metrics for the VistA Storage Monitor.                                                        |
|              | RUN      | Entry point. Calls the STORAGE, ZERONODE, *and* GLOBALS line tags.                                                |
|              | STORAGE  | Collects storage metrics and sends to the national database via an HTTP request.                                  |
|              | ZERONODE | Collects zero node metrics and sends to the national database via an HTTP request.                            |
|              | GLOBALS  | Collects global size metrics and sends to the national database via an HTTP request.                              |
|              | CALC     | Converts storage metrics to MB or GB.                                                                             |
|              | GETDB    | Configuration specific information based on operating system.                                                     |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193772" class="anchor"></span>Table : VBEM Routine

## VistA Business Event Monitor (VBEM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPBEMRT |          | Collect event metrics for the VistA Business Event Monitor.                                                   |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193807" class="anchor"></span>Table : VCSM Routine

## VistA Coversheet Monitor (VCSM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPCSMRT |          | Collect coversheet load metrics for the VistA Coversheet Monitor.                                             |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | ORONE    | Collates metrics if coversheets only run in foreground or background.                                             |
|              | ORBOTH   | Collates metrics if coversheets run in both foreground and background.                                            |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref118193813" class="anchor"></span>Table : VETM Routine

## VistA Error Trap Monitor (VETM) Specific Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Routine      | Line Tag | Description                                                                                                       |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------|
| KMPETMRT |          | Collect error metrics for the VistA Error Trap Monitor.                                                       |
|              | RUN      | Entry point: Manages configuration and kicks off individual collections.                                          |
|              | COLLECT  | Collect metrics and send to national database via HTTP requests.                                                  |
|              | SETRETRY | Attempts to save data for retry the next morning. Captures errors, such as String Too Long, and sends alerts. |
|              | RETRY    | Transmit data that was *not* successfully sent on previous attempts.                                              |

<span id="_Ref74734211" class="anchor"></span>Table : VSM Utility Routines

## VSM Utility Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref146542684" class="anchor"></span>Table : VSM Utility REST Class</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 35%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Line Tag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>KMPVCCFG</strong></td>
<td></td>
<td><strong>VSM Configuration Functions.</strong></td>
</tr>
<tr class="even">
<td></td>
<td>CFGARR(KMPVMKEY,KMPVCFG,<br />
KMPVFLAG</td>
<td>Return configuration by monitor in array.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETDEF(KMPVMKEY,KMPVDEF,<br />
KMPVFLAG)</td>
<td>Return default configuration in array.</td>
</tr>
<tr class="even">
<td></td>
<td>CFGSTR(KMPVMKEY,KMPVFLAG)</td>
<td>Return configuration in <strong>^</strong>-delimited string.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETVAL(KMPVMKEY,KMPVFLD,<br />
KMPVFILE,KMPVFLAG)</td>
<td>Retrieve value from VSM CONFIGURATION (#8969) or VSM MONITOR DEFAULTS (#8969.02) files.</td>
</tr>
<tr class="even">
<td></td>
<td>SETONE(KMPVMKEY,KMPVFNAM,KMPVNVAL,KMPVERR,KMPVLOG)</td>
<td>Set a value into the VSM CONFIGURATION (#8969) file.</td>
</tr>
<tr class="odd">
<td></td>
<td>SETVALS(KMPVMKEY,KMPVFVAL,<br />
KMPVERR,KMPVLOG)</td>
<td>Set multiple values into the VSM CONFIGURATION (#8969) file.</td>
</tr>
<tr class="even">
<td></td>
<td>RESTCFG(KMPVMKEY)</td>
<td>Restore default configuration to VSM CONFIGURATION (#8969) file.</td>
</tr>
<tr class="odd">
<td></td>
<td>STRSTP(KMPVMKEY,KMPVSTIME)</td>
<td>Record run time values.</td>
</tr>
<tr class="even">
<td></td>
<td>SYSCFG()</td>
<td>Return system configuration values.</td>
</tr>
<tr class="odd">
<td></td>
<td>MONSTAT(KMPVTEXT)</td>
<td>Return status information for all configured monitors.</td>
</tr>
<tr class="even">
<td></td>
<td>USERNAME(KMPVDUZ)</td>
<td>Return users name from <strong>DUZ</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>PROD()</td>
<td>Return “<strong>Prod</strong>” if production; otherwise, return “<strong>Test</strong>”.</td>
</tr>
<tr class="even">
<td></td>
<td>SITEINFO</td>
<td>Returns the site’s name, domain, sitecode, and Production status.</td>
</tr>
<tr class="odd">
<td></td>
<td>SLOT(KMPTIME, KMPSINT,KMPTFORM)</td>
<td>Determines the time “slot” based on how the monitor is configured.</td>
</tr>
<tr class="even">
<td></td>
<td>ISBENODE(KMPNODE)</td>
<td>Determines if the current node is a “<strong>back-end</strong>” or “<strong>front-end</strong>”.</td>
</tr>
<tr class="odd">
<td><strong>KMPVCBG</strong></td>
<td></td>
<td><strong>VSM Background Utility Functions.</strong></td>
</tr>
<tr class="even">
<td></td>
<td>MONLIST(KMPVML)</td>
<td>Return list of configured monitors.</td>
</tr>
<tr class="odd">
<td></td>
<td>STARTALL</td>
<td>Starts up all monitors – called by <strong>ZSTU</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>STOPALL</td>
<td>Stops all monitors.</td>
</tr>
<tr class="odd">
<td></td>
<td>ALLOW(KMPVMKEY)</td>
<td>Sets the value for <strong>ALLOW TEST</strong> for a given monitor.</td>
</tr>
<tr class="even">
<td></td>
<td>STARTMON(KMPVMKEY)</td>
<td>Schedule transmission task in TaskMan and set ONOFF (#.02) field to <strong>ON</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>STOPMON(KMPVMKEY)</td>
<td>Un-schedule transmission task in TaskMan and set ONOFF (#.02) field to <strong>OFF</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>RESCH(KMPVMKEY,KMPVERR)</td>
<td>Reschedule transmission task in TaskMan.</td>
</tr>
<tr class="odd">
<td></td>
<td>DESCH(KMPVMKEY,KMPVERR)</td>
<td>De-schedule transmission task in TaskMan.</td>
</tr>
<tr class="even">
<td></td>
<td>PURGEDLY(KMPVMKEY)</td>
<td>Purge any data older than VSM CONFIGURATION (#8969) file specifies.</td>
</tr>
<tr class="odd">
<td></td>
<td>KMPVTSK</td>
<td>For legacy compatibility – calls TASK^KMPTASK.</td>
</tr>
<tr class="even">
<td></td>
<td>ROUTCHK(KMPROUT)</td>
<td>Determines if a routine is running.</td>
</tr>
<tr class="odd">
<td></td>
<td>CANMESS(MTYPE,KMPVMKEY,<br />
KMPVSITE,KMPVD)</td>
<td>Repeatable, configured mail messages.</td>
</tr>
<tr class="even">
<td></td>
<td>SUPMSG(KMPVTEXT)</td>
<td>Send email to national and local support mail groups.</td>
</tr>
<tr class="odd">
<td></td>
<td>DBAMSG(KMPVTEXT)</td>
<td>Send email to local support mail group.</td>
</tr>
<tr class="even">
<td></td>
<td>CFGMSG(KMPVRQNAM)</td>
<td>Send configuration data to update Location Table at National VSM Database.</td>
</tr>
<tr class="odd">
<td><strong>KMPVLM</strong></td>
<td></td>
<td><strong>List Manager Functions.</strong></td>
</tr>
<tr class="even">
<td></td>
<td>EN</td>
<td>Main entry point for VSM MANAGEMENT menu option.</td>
</tr>
<tr class="odd">
<td></td>
<td>HDR</td>
<td>Header Code.</td>
</tr>
<tr class="even">
<td></td>
<td>INIT</td>
<td>Initialize variables and list array.</td>
</tr>
<tr class="odd">
<td></td>
<td>BUILD</td>
<td>Build array with collector status information.</td>
</tr>
<tr class="even">
<td></td>
<td>STARTMON</td>
<td>Supports List Manager protocol <strong>STRT Start Monitor</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>STOPMON</td>
<td>Supports List Manager protocol <strong>STOP Stop Monitor</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>TESTSYS</td>
<td>Allows the end user to change the value for ALLOW TEST SYSTEM.</td>
</tr>
<tr class="odd">
<td></td>
<td>CONTACT</td>
<td>Displays the CPE VSM email group name.</td>
</tr>
<tr class="even">
<td></td>
<td>VIEWCFG</td>
<td>Supports List Manager protocol <strong>VIEW View CFG</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>EDITCFG</td>
<td>Supports List Manager protocol <strong>EDIT Edit CFG</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>RESTCFG</td>
<td>Supports List Manager protocol <strong>REST Restore CFG</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>KILL(KMPVMKEY)</td>
<td>Supports List Manager protocol <strong>DEL Delete Data</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>PICKMON()</td>
<td>Supports selection of Monitor Type for List Manager functions.</td>
</tr>
<tr class="odd">
<td></td>
<td>REFRESH</td>
<td>Refresh display.</td>
</tr>
<tr class="even">
<td></td>
<td>HELP</td>
<td>Help code.</td>
</tr>
<tr class="odd">
<td></td>
<td>EXIT</td>
<td>Exit code.</td>
</tr>
<tr class="even">
<td></td>
<td>EXPND</td>
<td>Expand code.</td>
</tr>
<tr class="odd">
<td><span id="KMPVRUN_Routine" class="anchor"></span><strong>KMPVRUN</strong></td>
<td></td>
<td><strong>VSM Caché Task Manager Driver.</strong></td>
</tr>
<tr class="even">
<td></td>
<td>RUN</td>
<td>Loop VSM CONFIGURATION (#8969) file and run collection routine for monitors set to <strong>ON</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>CLEANUP</td>
<td>Purge old data in VSM CACHE TASK LOG (#8969.03) file and release lock.</td>
</tr>
<tr class="even">
<td></td>
<td>KMPWEB</td>
<td>Creates SSL Configuration and Web Application classes if they do <em>not</em> exist.</td>
</tr>
<tr class="odd">
<td></td>
<td>ERREXIT</td>
<td>Error trap to ensure routine returns from <strong>%SYS</strong> namespace.</td>
</tr>
<tr class="even">
<td></td>
<td>ZSTU</td>
<td>Called from <strong>ZSTU</strong> on startup. Checks that necessary classes exist and starts monitors on a failover event.</td>
</tr>
<tr class="odd">
<td><span id="KMPUTLW_Routine" class="anchor"></span><strong>KMPUTLW</strong></td>
<td></td>
<td><strong>VSM Utility Routine.</strong></td>
</tr>
<tr class="even">
<td></td>
<td>POST</td>
<td>Sends the HTTP request to the national database.</td>
</tr>
<tr class="odd">
<td></td>
<td>INFOMSG(KMPVTEXT)</td>
<td>Sends email to VSM support.</td>
</tr>
<tr class="even">
<td></td>
<td>CANMSG(MTYPE, KMPMKEY,KMPSITE,KMPD)</td>
<td>Sends pre-configured messages for specific cases.</td>
</tr>
<tr class="odd">
<td></td>
<td>CFGMSG</td>
<td>Sends configuration data to the national database.</td>
</tr>
<tr class="even">
<td></td>
<td>RETRY</td>
<td>Executes the <strong>RETRY</strong> function of the specific monitors.</td>
</tr>
<tr class="odd">
<td></td>
<td>CTMLOG</td>
<td>Sends the contents of the VSM CACHE TASK LOG (#8969.03) file.</td>
</tr>
<tr class="even">
<td></td>
<td>PACKAGES</td>
<td>Get data from the PACKAGE (#9.4) file.</td>
</tr>
<tr class="odd">
<td></td>
<td>SITE</td>
<td>Creates the <strong>SITE</strong> section of the JSON configuration message.</td>
</tr>
<tr class="even">
<td></td>
<td>CPF</td>
<td>Creates the <strong>CPF</strong> section of the JSON configuration message.</td>
</tr>
<tr class="odd">
<td></td>
<td>MON</td>
<td>Creates the <strong>MONITOR</strong> section of the JSON configuration message.</td>
</tr>
<tr class="even">
<td></td>
<td>TSTAMP(KMPDAY, KMPFORMAT, KMPTZ)</td>
<td>Formats an ODBC timestamp string.</td>
</tr>
<tr class="odd">
<td></td>
<td>SHORTDATE</td>
<td>Formats an ODBC date string.</td>
</tr>
<tr class="even">
<td></td>
<td>UTC</td>
<td>Creates a timestamp in Linux UTC format.</td>
</tr>
<tr class="odd">
<td></td>
<td>NODETYPE</td>
<td>Returns the type of node.</td>
</tr>
<tr class="even">
<td><strong>KMPUTLW2</strong></td>
<td></td>
<td><strong>VSM Utility Routine.</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>EVTPKG(KMPOPT)</td>
<td>Returns the Event Name, Parent Event Name, Event Type, and Event Source.</td>
</tr>
<tr class="even">
<td></td>
<td>CALCEVT(KMPOPT)</td>
<td>Determines if the event is an RPC, Protocol, or Option.</td>
</tr>
<tr class="odd">
<td></td>
<td>CALCPKG(KMPENAMEZ)</td>
<td>Determines the Package Name of the event.</td>
</tr>
<tr class="even">
<td></td>
<td>RESERVED(KMPENAME)</td>
<td>Determines if the event is part of the RPC Broker, VistALink Handler, TaskMan, or Menu Driver.</td>
</tr>
<tr class="odd">
<td></td>
<td>RESPACK(KMPENAME)</td>
<td>Returns the package information for reserved packages.</td>
</tr>
<tr class="even">
<td></td>
<td>SETCFG(KMPCFG)</td>
<td>Function to update the current configuration of a monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETERR(KMPRET, KMPREQ)</td>
<td>Returns data from the Kernel Error Trap, ERROR LOG (#3.075) file.</td>
</tr>
<tr class="even">
<td><strong>KMPTASK</strong></td>
<td></td>
<td><strong>VSM Utility Routine.</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>TASK(KMPVNSP)</td>
<td>Creates task in the Cache Task Manager. If it exists, it reports on status.</td>
</tr>
<tr class="even">
<td></td>
<td>SETRT</td>
<td>Manages requests to change real time status of monitors.</td>
</tr>
<tr class="odd">
<td></td>
<td>VTCMLEG</td>
<td>Sets values needed for legacy <strong>VTCM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VTCMRT</td>
<td>Sets values needed for real time <strong>VTCM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VSTMLEG</td>
<td>Sets values needed for legacy <strong>VSTM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VSTMRT</td>
<td>Sets values needed for real time <strong>VSTM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VBEMLEG</td>
<td>Sets values needed for legacy <strong>VBEM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VBEMRT</td>
<td>Sets values needed for real time <strong>VBEM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VMCMLEG</td>
<td>Sets values needed for legacy <strong>VMCM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VMCMRT</td>
<td>Sets values needed for real time <strong>VMCM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VHLMLEG</td>
<td>Sets values needed for legacy <strong>VHLM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VHLMRT</td>
<td>Sets values needed for real time <strong>VHLM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VCSMLEG</td>
<td>Sets values needed for legacy <strong>VCSM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VCSMRT</td>
<td>Sets values needed for real time <strong>VCSM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>VETMLEG</td>
<td>Sets values needed for legacy <strong>VETM</strong>.</td>
</tr>
<tr class="even">
<td></td>
<td>VETMRT</td>
<td>Sets values needed for real time <strong>VETM</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>ENABLE</td>
<td>Edits the Out Of Order Message for legacy Options.</td>
</tr>
<tr class="even">
<td></td>
<td>KMPOPTS</td>
<td>Creates array of options for <strong>ENABLE</strong>.</td>
</tr>
<tr class="odd">
<td></td>
<td>GLOSTATS(KMPDIRS)</td>
<td>Drives collection of Global Size metrics.</td>
</tr>
<tr class="even">
<td></td>
<td>GLOSET(KMPDIR)</td>
<td>Collates Global Size metrics.</td>
</tr>
<tr class="odd">
<td></td>
<td>ZERO</td>
<td>Collects <strong>zero</strong> node data.</td>
</tr>
<tr class="even">
<td><strong>KMPSYNTH</strong></td>
<td></td>
<td><strong>Collection of callable Synthetic Transactions.</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>SYNRCMD</td>
<td>Synthetic transaction to execute routine commands.</td>
</tr>
<tr class="even">
<td></td>
<td>ONE</td>
<td>Supports SYNRCMD.</td>
</tr>
<tr class="odd">
<td></td>
<td>TWO</td>
<td>Supports SYNRCMD.</td>
</tr>
<tr class="even">
<td></td>
<td>SYNFILE</td>
<td>Synthetic transaction to write and read from a file.</td>
</tr>
<tr class="odd">
<td></td>
<td>SYNVPR</td>
<td>Synthetic transaction to execute the V<strong>PR GET PATIENT DATA</strong> function (does <em>not</em> return actual data).</td>
</tr>
<tr class="even">
<td></td>
<td>PATLIST</td>
<td>Returns information of Patients to drive SYNVPR and CPRS Coversheet loads.</td>
</tr>
<tr class="odd">
<td></td>
<td>STATS</td>
<td>Calculates <strong>VBEM</strong> data for transactions.</td>
</tr>
<tr class="even">
<td></td>
<td>LOREM</td>
<td>Lorem Ipsum text for the <strong>SYNFILE</strong> function.</td>
</tr>
</tbody>
</table>

<span id="_Ref146542684" class="anchor"></span>Table : VSM Utility REST Class

| URL Path          | Method | Purpose                                                                           |
|-------------------|--------|-----------------------------------------------------------------------------------|
| /GetNode          | GET    | Returns the node receiving the request.                                           |
| /GetConfiguration | GET    | Returns configuration information from the CPF file and individual Monitors.      |
| /GetHttpMetrics   | GET    | Returns the status and timings of HTTP posts from VistA.                          |
| /KillData         | GET    | Provides a means to stop monitors and delete data in case of an emergency.        |
| /StartMonitor     | GET    | Provides a means to start monitors remotely.                                      |
| /GetRetryData     | GET    | Provides visibility into the “retry” node in ^KMPTMP.                     |
| /GetConfig        | POST   | Returns configuration information from the CPF file and individual Monitors.      |
| /SetConfig        | POST   | Provides means to update monitor configuration.                                   |
| /GetError         | POST   | Returns data from the VistA error trap.                                           |
| /GetCtmLog        | POST   | Returns entries from the VSM CACHE TASK LOG (#8969.03) file for debugging.        |
| /GetPatientList   | POST   | Returns data for use in synthetic transactions.                                   |
| /Retry            | POST   | Triggers a resend of any data that failed to transmission in last seven days. |
| /GetPackages      | POST   | Returns a list of packages from the Package file.                                 |
| /GetHttpMetrics   | POST   | Returns the status and timings of HTTP posts from VistA.                          |
| /ImAlive          | POST   | Returns OK (ping).                                                            |
| /SynthRcmd        | POST   | Runs a VSM synthetic transaction – gets timing of action.                         |
| /SynthFile        | POST   | Runs a VSM synthetic transaction – gets timing of action.                         |
| /SynthVpr         | POST   | Runs a VPR synthetic transaction – gets timing of action.                         |

<span id="_Ref437518640" class="anchor"></span>Table : Caché Task Manager Task Values

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the options in the OPTION (#19) file exported with VistA System Monitor (VSM).

## KMPV VSM MANAGEMENT Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548004" class="anchor"></span>Figure : KMPV VSM MANAGEMENT Menu Option

NAME: KMPV VSM MANAGEMENT MENU TEXT: VSM MANAGEMENT

TYPE: run routine CREATOR: L,J

LOCK: KMPVOPS ROUTINE: EN^KMPVLM

UPPERCASE MENU TEXT: VSM MANAGEMENT

## KMPV VTCM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548005" class="anchor"></span>Figure : KMPV VTCM DATA RETRANSMISSION Option

NAME: KMPV VTCM DATA RETRANSMISSION MENU TEXT: KMPV VTCM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VTCM metrics that did not send

successfully.

ROUTINE: RETRY^KMPTCMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VTCM DATA RETRANSMISSION

## KMPV VMCM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548006" class="anchor"></span>Figure : KMPV VMCM DATA RETRANSMISSION Option

NAME: KMPV VMCM DATA RETRANSMISSION MENU TEXT: KMPV VMCM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VMCM metrics that did not send

successfully.

ROUTINE: RETRY^KMPMCMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VMCM DATA RETRANSMISSION

## KMPV VHLM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548007" class="anchor"></span>Figure : KMPV VHLM DATA RETRANSMISSION Option

NAME: KMPV VHLM DATA RETRANSMISSION MENU TEXT: KMPV VHLM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VHLM metrics that did not send

successfully.

ROUTINE: RETRY^KMPHLMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VHLM DATA RETRANSMISSION

## KMPV VSTM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548008" class="anchor"></span>Figure : KMPV VSTM DATA RETRANSMISSION Option

NAME: KMPV VSTM DATA RETRANSMISSION MENU TEXT: KMPV VSTM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

PACKAGE: CAPACITY MANAGEMENT - VSM

DESCRIPTION: Background task to resend any VSTM metrics that did not send

successfully.

ROUTINE: RETRY^KMPSTMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes

UPPERCASE MENU TEXT: KMPV VSTM DATA RETRANSMISSION

## KMPV VBEM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548009" class="anchor"></span>Figure : KMPV VBEM DATA RETRANSMISSION Option

NAME: KMPV VBEM DATA RETRANSMISSION MENU TEXT: KMPV VBEM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VBEM metrics that did not send

successfully.

ROUTINE: RETRY^KMPBEMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VBEM DATA RETRANSMISSION

## KMPV VCSM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 16: KMPV VCSM DATA RETRANSMISSION Option

NAME: KMPV VCSM DATA RETRANSMISSION MENU TEXT: KMPV VCSM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VCSM metrics that did not send

successfully.

ROUTINE: RETRY^KMPCSMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VCSM DATA RETRANSMISSION

## KMPV VETM DATA RETRANSMISSION Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 17: KMPV VETM DATA RETRANSMISSION Option

NAME: KMPV VETM DATA RETRANSMISSION MENU TEXT: KMPV VETM DATA RETRANSMISSION

TYPE: run routine CREATOR: L,J

DESCRIPTION: Background task to resend any VETM metrics that did not send

successfully.

ROUTINE: RETRY^KMPETMRT SCHEDULING RECOMMENDED: YES

KEEP FROM DELETING: Yes UPPERCASE MENU TEXT: KMPV VETM DATA RETRANSMISSION

## KMPV-CLIENT-SRV Option—Deprecated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548010" class="anchor"></span>Figure : KMPV-CLIENT-SRV Option

NAME: KMPV-CLIENT-SRV MENU TEXT: KMPV-CLIENT-SRV

TYPE: server CREATOR: L,J

ROUTINE: KMPVCSRV SERVER ACTION: RUN IMMEDIATELY

SERVER MAIL GROUP: CPE-CP-SUPPORT

SUPRESS BULLETIN: NO (DEFAULT) SEND A BULLETIN

UPPERCASE MENU TEXT: KMPV-CLIENT-SRV

![](vsm-version-4-technical-manual/029.png) NOTE: The KMPV-CLIENT-SRV option will remain at the sites; however, it would only be used if a rollback to a previous version is required.

## KMPV MANAGEMENT MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For details on this menu, see Section <u>8.2.7</u>.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data is removed continuously from the sites. There are no special archiving procedures required with the VistA System Monitor (VSM) 4.0 software.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VSM callable routines, entry points, or Application Programming Interfaces (APIs) that can be called by other software.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Caché Task Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 14</u> details the parameters used to enter the task in the Caché Task Manager to start the VSM monitors on each node. This is created by running the KMPVTSK line tag of the KMPVCBG routine. The person running this line tag/routine *must* have either of the following roles:

- %All
- %Manager

| Field                                  | Entry                                                                                           |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| Task Name:                             | KMPVRUN                                                                                     |
| Description:                           | Start VSM Collection Drivers                                                                |
| Namespace to run task in:              | Default routine namespace - usually 3-letter site acronym (e.g., CTX for Central Texas) |
| Task type:                             | RunLegacyTask                                                                               |
| ExecuteCode:                           | D RUN^KMPVRUN                                                                               |
| Task priority:                         | Priority Normal                                                                             |
| Run task as this user:                 | Username of person setting up task                                                          |
| Open output file when task is running? | No                                                                                          |
| Output file:                           | Leave blank                                                                                 |
| Reschedule task after system restart?  | Yes                                                                                         |

<span id="_Ref44945336" class="anchor"></span>Table : VSM Required Packages

The task should be scheduled to run once daily at 1:00 AM.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM is dependent on the legacy VistA software in <u>Table 15</u>:

| Software       | Version | Patch Information |
|----------------|---------|-------------------|
| Kernel         | 8.0     | Fully patched     |
| Kernel Toolkit | 7.3     | Fully patched     |
| VA FileMan     | 22.2    | Fully patched     |
| MailMan        | 8.0     | Fully patched     |

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists entries in various VistA files necessary for the operation of VistA System Monitor (VSM).

## LIST TEMPLATE (#409.61) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KMPV MANAGEMENT List Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548011" class="anchor"></span>Figure : KMPV MANAGEMENT List Template

NAME: KMPV MANAGEMENT TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80 TOP MARGIN: 8

BOTTOM MARGIN: 15 OK TO TRANSPORT?: NOT OK

USE CURSOR CONTROL: YES PROTOCOL MENU: KMPV MANAGEMENT MENU

SCREEN TITLE: VSM MANAGEMENT ALLOWABLE NUMBER OF ACTIONS: 2

AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ITEM NAME: Monitor COLUMN: 2

WIDTH: 45 DISPLAY TEXT: Monitor

ITEM NAME: Status COLUMN: 47

WIDTH: 6 DISPLAY TEXT: Status

DEFAULT VIDEO ATTRIBUTES: R

ITEM NAME: Days Not Sent COLUMN: 55

WIDTH: 13 DISPLAY TEXT: Days Not Sent

ITEM NAME: Version COLUMN: 70

WIDTH: 7 DISPLAY TEXT: Version

EXIT CODE: D EXIT^KMPVLM HEADER CODE: D HDR^KMPVLM

HELP CODE: D HELP^KMPVLM ENTRY CODE: D INIT^KMPVLM

## PROTOCOL (#101) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KMPV START MONITOR Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548012" class="anchor"></span>Figure : KMPV START MONITOR Protocol

NAME: KMPV START MONITOR ITEM TEXT: Start Monitor

TYPE: action CREATOR: L,J

ENTRY ACTION: D STARTMON^KMPVLM TIMESTAMP: 63417,37931

### KMPV STOP MONITOR Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548013" class="anchor"></span>Figure : KMPV STOP MONITOR Protocol

NAME: KMPV STOP MONITOR ITEM TEXT: Stop Monitor

TYPE: action CREATOR: L,J

ENTRY ACTION: D STOPMON^KMPVLM TIMESTAMP: 63417,37989

### KMPV VIEW CFG Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548014" class="anchor"></span>Figure : KMPV VIEW CFG Protocol

NAME: KMPV VIEW CFG ITEM TEXT: View CFG

TYPE: action CREATOR: L,J

ENTRY ACTION: D VIEWCFG^KMPVLM TIMESTAMP: 63417,38175

### KMPV ALLOW TEST SYSTEM Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548015" class="anchor"></span>Figure : KMPV ALLOW TEST SYSTEM Protocol

NAME: KMPV ALLOW TEST SYSTEM ITEM TEXT: Allow Test

TYPE: action CREATOR: L,J

ENTRY ACTION: D TESTSYS^KMPVLM TIMESTAMP: 65457,38632

### KMPV CONTACT Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548016" class="anchor"></span>Figure : KMPV CONTACT Protocol

NAME: KMPV CONTACT ITEM TEXT: Contact Info

TYPE: action CREATOR: L,J

ENTRY ACTION: D CONTACT^KMPVLM TIMESTAMP: 65457,38770

### KMPV DELETE DATA Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548017" class="anchor"></span>Figure : KMPV DELETE DATA Protocol

NAME: KMPV DELETE DATA ITEM TEXT: Delete Data

TYPE: action CREATOR: L,J

ENTRY ACTION: D KILL^KMPVLM TIMESTAMP: 63417,35298

### KMPV MANAGEMENT MENU Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols on the KMPV MANAGEMENT MENU (<u>Figure 18</u>) are stored in the PROTOCOL (#101) file:

<span id="_Ref510082676" class="anchor"></span>Figure : KMPV MANAGEMENT MENU

NAME: KMPV MANAGEMENT MENU ITEM TEXT: KMPV MANAGEMENT MENU

TYPE: menu CREATOR: L,J

COLUMN WIDTH: 26 MNEMONIC WIDTH: 6

ITEM: KMPV START MONITOR MNEMONIC: STRT

SEQUENCE: 1

ITEM: KMPV STOP MONITOR MNEMONIC: STOP

SEQUENCE: 2

ITEM: KMPV VIEW CFG MNEMONIC: VIEW

SEQUENCE: 3

ITEM: KMPV DELETE DATA MNEMONIC: DEL

SEQUENCE: 6

ITEM: KMPV ALLOW TEST SYSTEM MNEMONIC: TEST

SEQUENCE: 5

ITEM: KMPV CONTACT MNEMONIC: INFO

SEQUENCE: 4

 

HEADER: D SHOW^VALM MENU PROMPT: Select Action

TIMESTAMP: 63452,46698

## FORM (#.403) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KMPV EDIT CONFIGURATION Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548019" class="anchor"></span>Figure : KMPV EDIT CONFIGURATION Form

NAME: KMPV EDIT CONFIGURATION READ ACCESS: @

WRITE ACCESS: @ CREATOR: 520791172

DATE CREATED: OCT 14, 2014@14:28 DATE LAST USED: OCT 31, 2014@12:04

PRIMARY FILE: 8969 DISPLAY ONLY: NO

FORM ONLY: NO COMPILED: YES

PAGE NUMBER: 1 PAGE COORDINATE: 1,1

PAGE NAME: Page 1

BLOCK NAME: KMPV EDIT CFG BLOCK ORDER: 1

BLOCK COORDINATE: 1,1 TYPE OF BLOCK: EDIT

BLOCK NAME: KMPV EDIT TITLE BLOCK ORDER: 2

BLOCK COORDINATE: 16,1 TYPE OF BLOCK: DISPLAY

### KMPV VIEW CONFIGURATION Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc146548020" class="anchor"></span>Figure : KMPV VIEW CONFIGURATION Form

NAME: KMPV VIEW CONFIGURATION READ ACCESS: @

WRITE ACCESS: @ CREATOR: 520791172

DATE CREATED: OCT 15, 2014@08:48 DATE LAST USED: OCT 31, 2014@12:03

PRIMARY FILE: 8969 DISPLAY ONLY: YES

FORM ONLY: NO COMPILED: YES

PAGE NUMBER: 1 PAGE COORDINATE: 1,1

PAGE NAME: Page 1

BLOCK NAME: KMPV VIEW CFG BLOCK ORDER: 1

BLOCK COORDINATE: 1,1 TYPE OF BLOCK: DISPLAY

BLOCK NAME: KMPV VIEW TITLE BLOCK ORDER: 2

BLOCK COORDINATE: 16,1 TYPE OF BLOCK: DISPLAY

### Database Integration Agreements (IAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref119483736" class="anchor"></span>Figure : VSM Database Integration Agreements (IAs)

This version of VSM software is dependent on the following Integration Agreements

IA#: Name-Components: Usage:

----- ---------------- ------

10097 %ZOSV-GETENV, \$\$OS, \$\$VERSION Supported

10112 VASITE-\$\$SITE Supported

10060 New Person File Supported

10035 Patient File Supported

3027 Security/Sensitive Record access Supported

2734 MESSAGE & MAILBOX UTILITIES API-\$\$NETNAME Supported

10073 MAILMAN: Message Body Access, including Servers-REC Supported

4440 DBIA4440 Supported

1966 DBIA1966 Subscription

6877 Read access to HL7 Message Text file for capacity planning Private

6878 Read access to FILE 773 for capacity planning Private

6882 Read access to HLO Message Body file for capacity planning Private

6883 Read access to HLO Messages file for capacity planning Private

6247 Direct KMPV read to KMPTMP Private

7135 VPR GET PATIENT DATA XML Private

7136 VPR GET PATIENT DATA JSON Private

7138 DIRECT READ OF ERROR LOG FILE Private

7139 DIRECT READ OF ERROR TRAP SUMMARY FILE Private

10046 XUWORKDAY Supported

10103 XLFDT Supported

6342 Kernel-Storage Private

# Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VSM global variables.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM support can be reached by emailing VA IT EPMO CPE VistA System Monitor\<REDACTED\>

![](vsm-version-4-technical-manual/030.png) NOTE: There are no VSM bulletins or alerts.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data collected does *not* contain:

- Personal Health Information (PHI).
- Patient, clinician, or financial data collected.

Examples of data collected include:

- Number of global READs/WRITEs per time period.
- Amount of storage space used by the system in question.

Data transmissions:

- VTCM data is sent to the CPE national database per configured collection interval.
- VMCM data is sent to the CPE national database per configured collection interval.
- VHLM data is sent to the CPE national database per configured collection interval.
- VSTM data is transmitted on the 1<sup>st</sup> and 3<sup>rd</sup>Saturday of each month.
- VBEM data is sent to the CPE national database per configured collection interval.
- VCSM data is sent to the CPE national database per configured collection interval.
- VETM data is sent to the CPE national database per configured collection interval.
- If the VistA site receives an HTTP 200 in response, it will delete the data on the site. If an HTTP code other than 200 is received, then the data will be put into the “retry” node of ^KMPTMP for attempted resend up to the number of days in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file.

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For VSM archiving information, see Section <u>5</u>, “<u>Archiving</u>.”

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM software operates on standard VistA software and hardware.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM does *not* use electronic signatures.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM does *not* distribute any security menus or options.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KMPVOPS security key is needed to access the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option. This security key should only be given to those who manage VSM.

<span id="_Toc146548022" class="anchor"></span>Figure : KMPVOPS Security Key

NAME: KMPVOPS DESCRIPTIVE NAME: VSM OPERATIONS LOCK

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a list of files exported with VSM, see Section <u>2</u>, “<u>Files</u>.”

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a list of document and other references, see the “[Reference Materials](#_Toc397138035)” section.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues or anomalies related to the VistA System Monitor (VSM) 4.0 software.

## Operational Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is intended to run automatically in the background and should require no operational support under normal operations. However, for those times where support is needed there are two mechanisms within this package to provide such functionality:

- Local Operational Support: There is a List Manager Application installed with this package that allows the local support staff to:
- Start and stop monitors
- View operational parameters
- Delete all locally stored data in case of emergency

![](vsm-version-4-technical-manual/031.png) REF: These actions are documented in Section 2, “VSM Operation” section in the *VistA System Monitor (VSM) User Manual*.

- National CPE Support: Additionally, this software has the capability to receive requests for the same functions via HTTP requests from the CPE national database.
- The CPE support team can be reached via email at VA IT EPMO CPE VistA System Monitor \<REDACTED\>.

## VA Enterprise Service Desk (ESD) Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Information Technology (IT) support 24 hours a day, 365 days a year contact the VA Enterprise Service Desk (ESD):

- Enter an Incident or Request ticket in the Information Technology Service Management (ITSM) ServiceNow (SNOW) system via the YourIT shortcut on your workstation.
- Phone: \<REDACTED\> or \<REDACTED\>
- ITSM Tool—ServiceNow site: \<REDACTED\>

[^1]: This is the IEN (.001 Field) in the PATIENT (#2) file.