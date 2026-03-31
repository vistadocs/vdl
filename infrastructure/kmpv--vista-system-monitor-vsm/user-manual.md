---
title: VSM Version 4 User Manual
doc_type: UM
doc_label: User Manual
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
menu_options: 0
description: 
audience: 
keywords: 
  - monitor
  - vista
  - table
  - strong
  - span
  - class
  - contents
  - metrics
  - manual
  - version
page_count: 0
word_count: 6275
section_count: 14
table_count: 9
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=218"
---

---
title: |
  <span id="_Toc186420068" class="anchor"></span>VistA System Monitor (VSM) 4.0

  User Manual
---

![](vsm-version-4-user-manual/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Software Product Management (SPM)

Capacity and Performance Engineering (CPE)

<span id="revision_history" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref431821080" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 29%" />
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
<p><u>Table 3</u>:</p>
<ul>
<li><p>Changed Field #1.05 in File #8969 from TASKMAN SCHEDULE FREQUENCY to <a href="#HTTP_REQUEST_MAX_LENGTH_Field"><strong>HTTP REQUEST MAX LENGTH</strong></a>.</p></li>
<li><p>Changed Field #1.06 in File #8969 from TASKMAN SCHEDULE START to <a href="#MONITOR_START_DELAY_Field"><strong>MONITOR START DELAY</strong></a>.</p></li>
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
<li><p>Section <u>1.1</u>: Added reference to “InterSystems’ IRIS.”</p></li>
<li><p>Section <u>1.2</u>: Updated failsafe bullets.</p></li>
<li><p>Sections <u>2.2.1</u> and <u>2.2.2</u>: Removed references to VistA TaskMan in the Intro text.</p></li>
<li><p>Updated <u>Table 3</u>: Added Note to <strong>TASKMAN SCHEDULE FREQUENCY</strong>, <strong>TASKMAN SCHEDULE START</strong>, and <strong>TASKMAN OPTION</strong> entries.</p></li>
<li><p>Section <u>2.2.6</u>: Updated intro text.</p></li>
</ul></td>
<td><ul>
<li><p>Capacity and Performance Engineering (CPE) Development Team</p></li>
<li><p>VISS Tech Writer</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>07/01/2021</td>
<td>1.1</td>
<td>Updates for Patch KMP*4.0*2: Added the new Time Drift metric to <u>Table 4</u>.</td>
<td>CPE Development Team</td>
</tr>
<tr class="even">
<td>07/22/2020</td>
<td>1.0</td>
<td><p>Initial VistA System Monitor (VSM) 3.0 User Manual:</p>
<ul>
<li><p>Upgraded to real time VistA System Monitor.</p></li>
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
<li><p>Vista coversheet Monitor (VCSM).</p></li>
<li><p>VistA Error Trap Monitor (VETM).</p></li>
</ul></td>
<td>CPE Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref431821080" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Table of Contents

<span id="_Toc156894624" class="anchor"></span>List of Figures

<span id="_Toc156894625" class="anchor"></span>List of Tables

<span id="_Toc436814072" class="anchor"></span>Orientation

How to Use this Manual

The purpose of this guide is to provide instructions for use and maintenance of the Veterans Health Information Systems and Technology Architecture (VistA) Capacity and Performance Engineering (CPE) VistA System Monitor (VSM) 4.0 software, which is the third iteration of data collected as the overall capability has progressed.

Throughout this manual, advice and instructions are offered regarding the use of the VSM software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

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

This manual provides an overall explanation of using the VistA System Monitor (VSM) 4.0, which is the third iteration of data collected as the overall capability has progressed software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA internet and intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Software Product Management (SPM) intranet website.

![](vsm-version-4-user-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA intranet service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](vsm-version-4-user-manual/003.png)   | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](vsm-version-4-user-manual/004.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref511630286" class="anchor"></span>Table 2: VSM MANAGEMENT Display Description

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*” is defined in the Approved Application Abbreviations document and “\<*N*\>” represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in VSM (KMPV) test patient and user names would be documented as follows:

- KMPVPATIENT,ONE or KMPVUSER,ONE
- KMPVPATIENT,TWO or KMPVUSER,TWO
- KMPVPATIENT,THREE or KMPVUSER,THREE

  KMPVPATIENT,14 or KMPVUSER,14
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](vsm-version-4-user-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](vsm-version-4-user-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to the toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](vsm-version-4-user-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](vsm-version-4-user-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](vsm-version-4-user-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about VSM should consult the following:

- *VistA System Monitor (VSM) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *VistA System Monitor (VSM) User Manual* (this manual)
- *VistA System Monitor (VSM) Technical Manual*
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

Redacted VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>

![](vsm-version-4-user-manual/010.png) REF: See the [VistA System Monitor (VSM) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=218).

Unredacted VistA documentation and software can be downloaded from the Product Support (PS) Network File Share (NFS) (formerly known as the “Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Data Collection](#data-collection)
    - [VistA Timed Collection Monitor (VTCM)](#vista-timed-collection-monitor-vtcm)
    - [VistA Storage Monitor (VSTM)](#vista-storage-monitor-vstm)
    - [VistA Business Event Monitor (VBEM)](#vista-business-event-monitor-vbem)
    - [VistA Message Count Monitor (VMCM)](#vista-message-count-monitor-vmcm)
    - [VistA HL7 Monitor (VHLM)](#vista-hl7-monitor-vhlm)
    - [VistA Coversheet Monitor (VCSM)](#vista-coversheet-monitor-vcsm)
    - [VistA Error Trap Monitor (VETM)](#vista-error-trap-monitor-vetm)
  - [Data Storage and Analysis](#data-storage-and-analysis)
  - [Package Management](#package-management)
- [VSM Operation](#vsm-operation)
  - [VSM MANAGEMENT Option](#vsm-management-option)
  - [Status and Operational Actions](#status-and-operational-actions)
    - [Start Monitor Action](#start-monitor-action)
    - [Stop Monitor Action](#stop-monitor-action)
    - [View CFG Action](#view-cfg-action)
    - [Allow Test Action](#allow-test-action)
    - [Contact Info Action](#contact-info-action)
    - [DEL—Delete Data Action](#deldelete-data-action)
- [Appendix A—VistA System Monitor (VSM) Metrics](#appendix-avista-system-monitor-vsm-metrics)
  - [VistA Timed Collection Monitor (VTCM)](#vista-timed-collection-monitor-vtcm-1)
  - [VistA Storage Monitor (VSTM)](#vista-storage-monitor-vstm-1)
  - [VistA Business Event Monitor (VBEM)](#vista-business-event-monitor-vbem-1)
  - [VistA Message Count Monitor (VMCM)](#vista-message-count-monitor-vmcm-1)
  - [VistA HL7 Monitor (VHLM)](#vista-hl7-monitor-vhlm-1)
  - [VistA Coversheet Monitor (VCSM)](#vista-coversheet-monitor-vcsm-1)
  - [VistA Error Trap Monitor (VETM)](#vista-error-trap-monitor-vetm-1)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA System Monitor (VSM) 3.0 software is intended to collect Caché and VistA metrics related to system capacity and business usage. The package is made up of the following seven collectors:

- VistA Timed Collection Monitor (VTCM)—Collects Caché metrics at regularly scheduled intervals such that they can be used in conjunction with metrics gathered via other deployed collection tools.
- VistA Storage Monitor (VSTM)—Collects storage metrics for each database twice monthly. This now includes the size of each global and information regarding the “0” node of each VistA file.
- VistA Business Event Monitor (VBEM)—Collects Caché metrics for VistA functions (Menu Options, TaskMan Jobs and Remote Procedure Calls).
- VistA Message Count Monitor (VMCM)—Collects inbound and outbound Health Level Seven (HL7) and HL7 Optimized (HLO) message counts per logical link at regularly scheduled intervals.
- VistA HL7 Monitor (VHLM)—Collects metadata about HL7 messages (SYNC and ASYNC) as well as HLO messages at regularly scheduled intervals.
- VistA Coversheet Monitor (VCSM)—Collects timing and metadata for CPRS coversheet loads at regularly scheduled intervals.
- VistA Error Trap Monitor (VETM)—Collects error trap data at regularly scheduled intervals.

This data is used for understanding VistA systems as they relate to the infrastructure on which they are deployed.

VSM provides automated VistA monitoring services developed by Capacity and Performance Engineering (CPE). This entails the daily capture of VistA-related Caché metrics. These metrics are automatically transferred to the CPE national database for storage and analysis.

This software is designed to be fully automated, *not* needing support from the local or regional system administrators. However, support features are available for both local support staff and remote CPE engineers for situations that may call for hands on support.

The current version of this software is intended for VistA sites running on InterSystems’ Caché or IRIS.

## Data Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM monitors are designed to collect data over the course of each day:

1.  Data is transferred to the CPE national database at each collection interval.
2.  Upon receipt of this data the national server sends an acknowledgement to the site.
3.  Once the site receives this acknowledgement it immediately deletes that data from its system.
4.  If data is *not* received it will be stored on the VistA system and resent up to the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file at which time it will be purged. This is set to seven (7) days by default.

As a failsafe:

- A<span id="purge_function" class="anchor"></span> purge function is executed: At 12:01 each morning the Cachè Task Manager runs the KMPVRUN routine. This routine is responsible for starting each individual monitor. Prior to starting each monitor, the KMPVRUN routine calls PURGEDLY^KMPVCBG. This line tag/routine deletes any data that is older than the number of days specified in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for that monitor type.
- A “warning” message is sent to the CPE support email address if data is found older than 1 day.
- There is a “kill switch” available to the sites in case of emergency. This is detailed in Section <u>2.2.6</u>, “<u>DEL—Delete Data Action</u>.”
- Lastly, there is also an application programming interface (API) that CPE can call to stop monitors and delete data on a node by node basis if necessary.

### VistA Timed Collection Monitor (VTCM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Timed Collection Monitor (VTCM) is intended to collect and send Caché metrics on a regularly scheduled interval. By default, this interval is every five (5) minutes and should *not* be changed without consultation with CPE support. Data collected includes the following metrics:

- Global References
- Routine Lines Executed
- Physical Block READs/WRITEs

If the data is *not* successfully received, then it is stored on site for retransmission.

There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/011.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA Storage Monitor (VSTM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Storage Monitor (VSTM) is intended to collect storage metrics twice monthly (i.e., the 1<sup>st</sup> and the 15<sup>th</sup> of each month). Data collected includes:

- Total Storage Per Directory (Cachè.dat file)
- Global Sizes
- Zero Node Metadata

  If the data is *not* successfully received, then it is stored on site for retransmission.

  There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/012.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA Business Event Monitor (VBEM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Business Event Monitor (VBEM) is intended to collect and send Cache metrics for the following VistA functions on a regularly scheduled interval:

- Menu Options
- TaskMan Jobs
- Remote Procedure Calls

By default, this interval is every five (5) minutes and should *not* be changed without consultation with CPE support. Data collected includes the following metrics: functionality for VistA functions. This functionality replaced the legacy Resource Utilization Monitor (RUM). Data collected includes:

- CPU Time
- Routine Lines
- Global References
- Occurrences

  If the data is *not* successfully received, then it is stored on site for retransmission.

  There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/013.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA Message Count Monitor (VMCM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Message Count Monitor (VMCM) is intended to collect and send HL7 and HLO message counts on logical links on a regularly scheduled interval. By default, this interval is every 15 minutes and should *not* be changed without consultation with CPE support. Data collected include inbound and outbound message counts from logical links as well as HLO queues.

If the data is *not* successfully received, then it is stored on site for retransmission.

There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/014.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA HL7 Monitor (VHLM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA HL7 Monitor (VHLM) is intended to collect and send metadata about both HL7 and HLO messages. By default, this interval is every 15 minutes and should *not* be changed without consultation with CPE support. Data collected includes:

- Message Size
- Logical Link
- Sending/Receiving Application
- Sending/Receiving Locations
- Subscriber Protocol

  If the data is *not* successfully received, then it is stored on site for retransmission.

  There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/015.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA Coversheet Monitor (VCSM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista Coversheet Monitor (VCSM) is intended to collect and send coversheet timing and metadata on a regularly scheduled interval. By default, this interval is every 15 minutes and should *not* be changed without consultation with CPE support. Data collected includes:

- Coversheet Processing Time
- User Information
- Patient DFN

  If the data is *not* successfully received, then it is stored on site for retransmission.

  There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/016.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

### VistA Error Trap Monitor (VETM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista Error Trap Monitor (VETM) is intended to collect and send error trap data on a regularly scheduled interval. By default, this interval is every 15 minutes and should *not* be changed without consultation with CPE support. Data collected includes:

- Error Name
- Error Location
- Line Causing the Error

If the data is *not* successfully received, then it is stored on site for retransmission.

There is a [purge function](#purge_function) that is executed every morning. This function deletes data that is older than the value set in the DAYS TO KEEP DATA (#1.01) field in the VSM CONFIGURATION (#8969) file for this monitor.

![](vsm-version-4-user-manual/017.png) REF: For functional and operational details, see Section <u>2</u>, “<u>VSM Operation</u>.”  
  
A list of metrics collected by this monitor can be found in “<u>Appendix A—VistA System Monitor (VSM) Metrics</u>.”

## Data Storage and Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data transferred to the CPE national server is stored in Caché Object/SQL tables. This data is then used for CPE analysts supporting operations and business functions.

The data collected at the VistA sites is collected in a fashion that allows CPE to directly correlate VSM data with that collected from other monitoring and collection tools currently in use. This data is used for purposes, such as:

- Capacity Planning
- System/Infrastructure Engineering
- Business Analysis
- Application Performance Monitoring

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is intended to run automatically in the background and should require no operational support under normal operations. However, for those times where support is needed there are two mechanisms within this package to provide such functionality:

- Local Operational Support: There is a List Manager Application installed with this package that allows the local support staff to:
- Start and stop monitors.
- View operational parameters.
- Configure operational parameters.
- Delete all locally stored data in case of emergency.

![](vsm-version-4-user-manual/018.png) REF: These actions are documented in Section <u>2</u>, “<u>VSM Operation</u>.”

- National CPE Support: This software can be managed remotely allowing for changes in configuration as needed.

# VSM Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VSM MANAGEMENT Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option is located under the Capacity Planning \[XTCM MAIN\] menu, as shown in <u>Figure 1</u>:

<span id="_Ref437588400" class="anchor"></span>Figure 1: VSM Management Menu

> Select Systems Manager Menu Option: <span class="mark">Capacity Planning</span>

> RUM RUM Manager Menu ...

> CPG Capacity Planning Mail Group Edit

> TLS CP Tools Manager Menu ...

> <span class="mark">VSM VSM MANAGEMENT</span>

> Select Capacity Planning Option: <span class="mark">VSM MANAGEMENT</span>

![](vsm-version-4-user-manual/019.png) NOTE: The VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option requires the user to hold the KMPVOPS security key.

The VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option displays the VSM MANAGEMENT List Manager application, as shown in <u>Figure 2</u>:

<span id="_Ref511630258" class="anchor"></span>Figure 2: VSM Management Display

![](vsm-version-4-user-manual/020.png)

This option provides status and operational actions for each monitor installed (see Section <u>2.2</u>, “<u>Status and Operational Actions</u>”). Installed monitors are listed with their Monitor Key and Full Name for clear identification.

<u>Table 2</u> lists the information displayed for each monitor:

| Field Caption | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| Monitor       | The four-character Monitor Key associated with the specific monitor.              |
| Status        | ON or OFF status of monitor.                                                  |
| Days Not Sent | This is the number of days where data has not been received by the national database. |
| Version       | Current version number of the monitor.                                                |

<span id="_Ref511632380" class="anchor"></span>Table 3: View Configuration Field Definitions

![](vsm-version-4-user-manual/021.png) REF: Screen shots and descriptions of each action in the “VSM MANAGEMENT” screen are listed in Section <u>2.2</u>, “<u>Status and Operational Actions</u>.”

## Status and Operational Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start Monitor Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STRT (Start Monitor) action sets the ONOFF (#.02) field in the VSM CONFIGURATION (#8969) file to 1 (ON) for the given monitor.

Upon starting a monitor, a message is sent to the CPE national server to automatically update its configuration file with the new monitor state.

<span id="_Toc156894607" class="anchor"></span>Figure 3: Start Monitor

![](vsm-version-4-user-manual/022.png)

### Stop Monitor Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STOP (Stop Monitor) action sets the ONOFF (#.02) field in the VSM CONFIGURATION (#8969) file to 0 (OFF) for the given monitor.

The specified monitor stops collecting metrics upon its next iteration as it checks the value of the ONOFF (#.02) field in the VSM CONFIGURATION (#8969) file prior to each execution. Upon stopping a monitor, a message is sent to the CPE national server to automatically update its configuration file with the new monitor state.

![](vsm-version-4-user-manual/023.png) NOTE: The monitors collect data via routines running on each individual node as started by the Caché Task Manager. Once stopped and then restarted, collections do *not* resume until the next day when the Caché Task Manager starts the monitors on each node.

<span id="_Toc156894608" class="anchor"></span>Figure 4: Stop Monitor

![](vsm-version-4-user-manual/024.png)

### View CFG Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIEW (View CFG \[configuration\]) action opens a read-only ScreenMan display. This provides an at-a-glance view of how the selected monitor is configured (<u>Figure 5</u>). Displayed fields are from the VSM CONFIGURATION (#8969) file. A definition of these fields is listed in <u>Table 3</u>.

<span id="_Ref437586460" class="anchor"></span>Figure 5: View Configuration

![](vsm-version-4-user-manual/025.png)

<u>Table 3</u> lists and defines the fields in the VSM CONFIGURATION (#8969) file:

<table>
<caption><p><span id="_Ref511629825" class="anchor"></span>Table 4: VistA Timed Collection Monitor (VTCM) Metrics</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 65%" />
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
<td><strong>Four</strong> letter acronym used to identify specific monitor.</td>
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
<td>Number of days that unsent data is allowed to remain in <strong>^KMPTMP("KMPV"</strong> before the purge routine kills it. Limited to <strong>3-7</strong> days. Data older than this value is deleted; regardless of reason it has <em>not</em> been sent to the national database, in order to assure global does <em>not</em> grow unchecked.</td>
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
<td>If set to <strong>YES</strong>, this allows the monitors to run on test systems. Otherwise, monitors exit if the current UCI is <em>not</em> set as <strong>PROD</strong> per <strong>^%ZOSF(“UCI”)</strong>.</td>
</tr>
<tr class="even">
<td><span id="HTTP_REQUEST_MAX_LENGTH_Field" class="anchor"></span>HTTP REQUEST MAX LENGTH</td>
<td>8969, 1.05</td>
<td>This number represents the maximum number of characters that can be sent in a single HyperText Transport Protocol (HTTP) Request body.</td>
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
<td><p>The <strong>KMPVRUN</strong> routine executes daily immediately after midnight:</p>
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
<td><strong>Deprecated.</strong></td>
</tr>
<tr class="even">
<td>LAST STOP TIME</td>
<td>8969, 2.02</td>
<td><strong>Deprecated.</strong></td>
</tr>
<tr class="odd">
<td>LAST RUN TIME</td>
<td>8969, 2.03</td>
<td><strong>Deprecated.</strong></td>
</tr>
<tr class="even">
<td>NATIONAL DATA EMAIL ADDRESS</td>
<td>8969, 3.01</td>
<td><strong>Deprecated:</strong> Messages are now sent via HyperText Transport Protocol (HTTP).</td>
</tr>
<tr class="odd">
<td>NATIONAL SUPPORT EMAIL ADDRESS</td>
<td>8969, 3.02</td>
<td>Email address used to send messages to the CPE VistA CP mail group.</td>
</tr>
<tr class="even">
<td>VSM CFG EMAIL ADDRESS</td>
<td>8969, 3.03</td>
<td><strong>Deprecated:</strong> Messages are now sent via HTTP.</td>
</tr>
<tr class="odd">
<td>LOCAL SUPPORT EMAIL ADDRESS</td>
<td>8969, 3.04</td>
<td>Optional email address for local support personnel. If present any email that would be sent to the national support group also goes to the local support group.</td>
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
<li><p>HTTP: Standard port <strong>80</strong>.</p></li>
<li><p>HTTPS: Port <strong>443</strong>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>API KEY</td>
<td>8969, 4.04</td>
<td>Header key for Amazon Web Services (AWS) API Gateway.</td>
</tr>
</tbody>
</table>

<span id="_Ref511629825" class="anchor"></span>Table 4: VistA Timed Collection Monitor (VTCM) Metrics

### Allow Test Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TEST (Allow Test) action opens an editable ScreenMan display. This allows the user to change the ALLOW TEST SYSTEM (#1.04) field in the VSM CONFIGURATION (#8969) file to YES or NO. If this value is set to NO, then the monitor will *not* run on a test system.

- Changes *must* be saved upon exiting the ScreenMan display in order to take effect.
- Changes take effect immediately.

Upon editing a monitor configuration parameter, a message is sent to the CPE national server to automatically update its configuration file with the new monitor state.

<span id="_Toc156894610" class="anchor"></span>Figure 6: Allow Test

![](vsm-version-4-user-manual/026.png)

### Contact Info Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INFO (Contact Info) action displays the name of the CPE email group that should be contacted with any questions or problems.

<span id="_Toc156894611" class="anchor"></span>Figure 7: Contact Info

![](vsm-version-4-user-manual/027.png)

### DEL—Delete Data Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEL (Delete Data) action is *<u>for emergency use only</u>*. This action deletes *<u>all</u>* data residing on the back-end node for the specified monitor and sets the ONOFF (#.02) field in the VSM CONFIGURATION (#8969) file to OFF (0). This action is effectively an emergency “kill switch”. If data needs to be deleted on front-end nodes contact CPE to execute an API to accomplish this.

Upon deletion of data, a message is sent to the CPE national server to automatically update its configuration file and alert CPE support that there is an emergency.

![](vsm-version-4-user-manual/028.png) CAUTION: This action can be taken *without* consultation with CPE support staff. However, it should only be taken in the case of an emergency, such as an unchecked growth in global size due to unforeseen circumstances. This option is effectively a monitor “kill switch.”

<span id="_Toc156894612" class="anchor"></span>Figure 8: Delete Data

![](vsm-version-4-user-manual/029.png)

# Appendix A—VistA System Monitor (VSM) Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Timed Collection Monitor (VTCM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the metrics collected by the VistA Timed Collection Monitor (VTCM):

| Metric – Per Second           | Metric – Per Count                                |
|-------------------------------|---------------------------------------------------|
| Disk Reads per Second         | Application Errors                                |
| Disk Writes per Second        | Block collisions                                  |
| Global References per Second  | Block Collision Samples                           |
| Global Sets per Second        | Cache Efficiency                                  |
| Journal Entries per Second    | CSP Sessions                                      |
| Logical Reads per Second      | ECP Application Server Rate                       |
| Routine Commands per Second   | ECP Data Server Rate                              |
| Routine References per Second | Global References per Second (InterSystems count) |
| Metrics - Status          | License Current                                   |
| Database Space                | License High                                      |
| ECP Application Server        | License Limit                                     |
| ECP Database Server           | Processes                                         |
| Journal Space                 | Serious Alerts                                    |
| Journal Status                | Time Drift                                        |
| Last Backup                   | Metrics - Memory                              |
| Lock Table                    | Total SMH Memory Used                             |
| Shadow Server                 | SMH Pages Used                                    |
| Shadow Source                 | Configure SMH Memory                              |
| System Uptime                 | Total Shared Memory Heap                          |
| Write Daemon                  | Total Available SMH Pages                         |
|                               | Total Available Memory SMT Table                  |
|                               | Total Available Memory General String Table       |

<span id="_Ref511629863" class="anchor"></span>Table 5: VistA Storage Monitor (VSTM) Metrics

## VistA Storage Monitor (VSTM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> lists the metrics collected by the VistA Storage Monitor (VSTM):

| Metric - Storage    | Metric – Zero Node                       |
|---------------------|------------------------------------------|
| Database            | Maximum size allowed for database growth |
| Disk                | Current size of database in MBs          |
| Directory           | Available disk space for database in MBs |
| Max Size MB         | File Number                              |
| Current Size MB     | File Name                                |
| Block Size          | Global Root                              |
| Blocks per Map      | Version                                  |
| Free Space MB       | Entries                                  |
| Free Blocks         | Last ID                                  |
| Is System Directory | Metrics - Globals                    |
| Expansion Size MB   | Directory                                |
| Disk Free Space MB  | Name                                     |
|                     | Allocated MB                             |
|                     | Used MB                                  |

<span id="_Ref511629924" class="anchor"></span>Table 6: VistA Business Event Monitor (VBEM) Metrics

## VistA Business Event Monitor (VBEM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the metrics collected by the VistA Business Event Monitor (VBEM):

| Metrics           | Dimensions      |
|-------------------|-----------------|
| Occurrences       | Event           |
| CPU Time          | Event Namespace |
| Routine Commands  | Event Package   |
| Global References | Event Source    |
| Elapsed Time      | Event Type      |
| Process Count     | Parent Event    |

<span id="_Ref511629975" class="anchor"></span>Table 7: VistA Message Count Monitor (VMCM) Metrics

## VistA Message Count Monitor (VMCM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the metrics collected by the VistA Message Count Monitor (VMCM):

| Metric                                  | Metric                                |
|-----------------------------------------|---------------------------------------|
| HL7 Messages Received per Logical Link  | HL7 Messages To Send per Logical Link |
| HL7 Messages Processed per Logical Link | HL7 Messages Sent per Logical Link    |
| HLO Messages Sent                       | HLO Messages Received                 |
| Link Name                               | Link State                            |

<span id="_Ref511630018" class="anchor"></span>Table 8: VistA HL7 Monitor (VHLM) Metrics

## VistA HL7 Monitor (VHLM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> lists the metrics collected by the VistA HL7 Monitor (VHLM):

| Metric                          | Metric                      |
|---------------------------------|-----------------------------|
| Application Acknowledgment Time | Commit Acknowledgement Time |
| Event Count                     | Event Protocol              |
| Event Type                      | Header Type                 |
| HLO Type                        | Logical Link                |
| Message Length                  | Message Type                |
| Priority                        | Queue                       |
| Receiving Application           | Receiving Site FQDN         |
| Receiving Site Number           | Sending Site Application    |
| Sending Site FQDN               | Sending site Number         |
| Subscriber Protocol             | Synchronization Type        |
| Transmission Time               | Transmission Type           |

<span id="_Toc156894621" class="anchor"></span>Table 9: VistA Coversheet Monitor (VCSM) Metrics

## VistA Coversheet Monitor (VCSM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 9</u> lists the metrics collected by the VistA Coversheet Monitor (VCSM):

| Metric                     | Metric               |
|----------------------------|----------------------|
| Foreground Foreground Time | Background Time      |
| Client DUZ                 | Client Name (system) |
| Client IP                  | Patient DFN          |

<span id="_Toc156894622" class="anchor"></span>Table 10: VistA Error Trap Monitor (VETM) Metrics

## VistA Error Trap Monitor (VETM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 10</u> lists the metrics collected by the VistA Error Trap Monitor (VETM):

| Metric                | Metric     |
|-----------------------|------------|
| Error Number          | Timestamp  |
| Database              | Instance   |
| Node Type             | Error      |
| Last Global Reference | Current IO |
| ZA Value              | ZB Value   |
| Current ZIO           | Job Number |
| Process Name          | Username   |
| Alternate Job Number  | Line       |