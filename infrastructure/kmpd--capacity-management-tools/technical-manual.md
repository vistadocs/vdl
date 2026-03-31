---
title: Capacity Management Tools Version 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: KMPD
app_name: Capacity Management Tools
section: INF
app_status: active
pkg_ns: KMPD
patch_ver: 3
patch_id: KMPD*3
group_key: "KMPD:KMPD:3"
file_numbers: 
  - 8973
security_keys: []
menu_options: 4
description: 
audience: 
keywords: 
  - tools
  - kmpd
  - table
  - capacity
  - contents
  - management
  - software
  - class
  - routine
  - timing
page_count: 0
word_count: 13368
section_count: 29
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0tm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0tm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=129"
---

---
title: |
  Capacity Management Tools 3.0

  Technical Manual
---

![](capacity-management-tools-version-3-technical-manual/001.png)

December 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Systems Engineering (ESE)

Capacity and Performance Engineering (CPE)

<span id="revision_history" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref437518632" class="anchor"></span>Table . Documentation revision history</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 45%" />
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
<td>12/29/2015</td>
<td>1.2</td>
<td><p>Updated document based on Capacity Management Tools Patch KMPD*3.0*3.</p>
<p>Software: <strong>CM Tools 3.0</strong>.</p></td>
<td><p>REDACTED (CPE): St Petersburg Field Office</p>
<p>Technical Writer: REDACTED</p></td>
</tr>
<tr class="even">
<td>10/--/2015</td>
<td>1.1</td>
<td><p>Corrected reports to reflect both foreground and background CPRS coversheet load timings.</p>
<p>Software: <strong>CM Tools 3.0</strong>.</p></td>
<td>REDACTED (CPE): St Petersburg Field Office</td>
</tr>
<tr class="odd">
<td>09/20/2012</td>
<td>1.0</td>
<td><p>Initial Capacity Management (CM) Tools software and documentation release.</p>
<p>Software: <strong>CM Tools 3.0</strong>.</p></td>
<td><p>Capacity Planning Development Team:</p>
<ul>
<li><p>Development Manager—REDACTED</p></li>
<li><p>Developer—REDACTED</p></li>
<li><p>Software Quality Assurance (SQA)—REDACTED</p></li>
<li><p>Technical Writer—REDACTED</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref437518632" class="anchor"></span>Table . Documentation revision history

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Contents

<span id="_Toc439223687" class="anchor"></span>Tables

<span id="_Toc18284794" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of Capacity Management (CM) Tools software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)—System administrators and Capacity Management personnel at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Product Development (PD)—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the VistA System Monitor (VSM) 1.0 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) Product Development (PD) Intranet Website.

![](capacity-management-tools-version-3-technical-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 2</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-technical-manual/003.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](capacity-management-tools-version-3-technical-manual/004.png) | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref345831418" class="anchor"></span>Table . Documentation symbol/term descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begins with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*“ is defined in the Approved Application Abbreviations document and “\<*N*\>“ represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in Capacity Planning (KMPD) test patient and user names would be documented as follows:

- KMPDPATIENT,ONE or KMPDUSER,ONE
- KMPDPATIENT,TWO or KMPDUSER,TWO
- KMPDPATIENT,THREE or KMPDUSER,THREE
- KMPDPATIENT,14 or KMPDUSER,14
- Etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and can be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](capacity-management-tools-version-3-technical-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](capacity-management-tools-version-3-technical-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

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

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](capacity-management-tools-version-3-technical-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](capacity-management-tools-version-3-technical-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](capacity-management-tools-version-3-technical-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about the Capacity Management Tools software should consult the following:

- *Capacity Management Tools Installation Guide*
- *Capacity Management Tools User Manual*
- *Capacity Management Tools Technical Manual* (this manual)
- Capacity Management (CM) Tools Online Help file (i.e., CM_Tools_3_0.chm)
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](capacity-management-tools-version-3-technical-manual/010.png) REF: See the [Capacity Management Tools manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=129).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
    - [Namespace](#namespace)
    - [^KMPD Global](#kmpd-global)
    - [Check CM Tools Background Driver Option](#check-cm-tools-background-driver-option)
  - [Maintenance](#maintenance)
    - [CP Tools Manager Menu](#cp-tools-manager-menu)
    - [CM Tools Background Driver Option](#cm-tools-background-driver-option)
- [Files](#files)
  - [Files](#files-1)
  - [Templates](#templates)
- [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
  - [Translation](#translation)
  - [Journaling](#journaling)
  - [Protection](#protection)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [Options with Parents](#options-with-parents)
    - [Capacity Planning Menu](#capacity-planning-menu)
    - [Capacity Planning Mail Group Edit Option](#capacity-planning-mail-group-edit-option)
    - [CP Tools Manager Menu](#cp-tools-manager-menu-1)
    - [CP Environment Check Option](#cp-environment-check-option)
    - [Start/Stop Timing Collection Option](#startstop-timing-collection-option)
    - [Edit CP Parameters File Option](#edit-cp-parameters-file-option)
    - [Timing Monitor Option](#timing-monitor-option)
    - [CP Tools Reports Menu](#cp-tools-reports-menu)
    - [Timing Reports Menu](#timing-reports-menu)
    - [Average Daily Coversheet Load Option](#average-daily-coversheet-load-option)
    - [Average Hourly Coversheet Load Option](#average-hourly-coversheet-load-option)
    - [Detailed Daily Coversheet Load Option](#detailed-daily-coversheet-load-option)
    - [Detailed Hourly Coversheet Load Option](#detailed-hourly-coversheet-load-option)
    - [Threshold Alert Option](#threshold-alert-option)
    - [Real-Time Threshold Alert Option](#real-time-threshold-alert-option)
    - [Real-Time Average Hourly Coversheet Load Option](#real-time-average-hourly-coversheet-load-option)
  - [Options without Parents](#options-without-parents)
    - [CM Tools Background Driver Option](#cm-tools-background-driver-option-1)
  - [Server Options](#server-options)
    - [CP Echo Server Option](#cp-echo-server-option)
  - [Protocols](#protocols)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines](#callable-routines)
  - [Controlled Subscription APIs](#controlled-subscription-apis)
- [External Relations](#external-relations)
  - [VistA Software Requirements](#vista-software-requirements)
  - [DBA Approvals and Integration Agreements](#dba-approvals-and-integration-agreements)
    - [IAs—Current List for CM Tools as Custodian](#iascurrent-list-for-cm-tools-as-custodian)
    - [IAs—Detailed Information](#iasdetailed-information)
    - [IAs—Current List for CM Tools as Subscriber](#iascurrent-list-for-cm-tools-as-subscriber)
- [Internal Relations](#internal-relations)
  - [Option Dependencies](#option-dependencies)
  - [Relationship of CM Tools Software with VistA](#relationship-of-cm-tools-software-with-vista)
    - [CPRS GUI 23.0 and OE/RR 3.0](#cprs-gui-230-and-oerr-30)
    - [HL7 1.6](#hl7-16)
  - [VistA Monitor](#vista-monitor)
  - [Namespace](#namespace-1)
- [Software-wide and Key Variables](#software-wide-and-key-variables)
- [SAC Exemptions](#sac-exemptions)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
    - [Mail Groups](#mail-groups)
    - [Alerts](#alerts)
    - [Bulletins](#bulletins)
  - [Remote Systems](#remote-systems)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [Official Policies](#official-policies)
The Capacity Management (CM) Tools software is a fully automated support tool developed by Capacity Planning (CP) Service. CM Tools are designed for Information Resource Management (IRM) and system administrators responsible for the capacity planning functions at their site, as well as Veterans Health Information Systems and Technology Architecture (VistA) software developers.
![](capacity-management-tools-version-3-technical-manual/011.png) CAUTION: *Before* installing a later version of the CM Tools GUI software, you *must* first uninstall/remove any existing/previous version of the CM Tools GUI software.
![](capacity-management-tools-version-3-technical-manual/012.png) DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7.
The CM Tools are used to measure system performance, data growth, Computerized Patient Record System (CPRS) coversheet load times, option and protocol execution, and provide various data reports. There are also tools for developers: global lister, error lister, routine search, and evaluate M code.
CM Tools entails the capture of all Veterans Health Information Systems and Technology Architecture (VistA) Health Level Seven (HL7) workload specifics from participating sites. This HL7 workload data is then summarized on a weekly basis and is automatically transferred via network mail (i.e., VistA MailMan) to the Capacity Planning (CP) National Database.
The Department of Veterans Affairs (VA) developed the Capacity Management Tools software in order to obtain more accurate information regarding the current and future VistA HL7 workload data at VA sites.
Installing the CM Tools software creates the collection process mechanism and other necessary components of the software. The fully automated data collection mechanism entails capturing all VistA HL7 workload specifics at the site into the ^TMP(“KMPDH”,\$J) temporary collection global. The collection mechanism is continuously monitoring each process on the system while trapping VistA HL7 workload data.
On a nightly basis, the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] moves the data within the ^TMP(“KMPDH”,\$J) temporary collection global to the CM HL7 DATA file (#8973.1).Upon completion, the temporary data within the ^TMP(“KMPDH”,\$J) temporary collection global is purged.
The CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] monitors and trims (records deleted) the following files to ensure that the correct maximum number of day’s data is maintained as determined by the appropriate CP parameters:
- CM HL7 DATA file (#8973.1)—The maximum amount of data collected is determined by the Purge HL7 Data After CP parameter.
- CP TIMING file (#8973.2)—The maximum amount of data collected is determined by the Purge Timing Data After CP parameter.
![](capacity-management-tools-version-3-technical-manual/013.png) REF: For more information on the CP parameters, see the “Edit CP Parameters File” section in Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.
On a nightly basis, the CM Tools Background Driver option automatically compresses the information contained within the CP TIMING file (#8973.2) into daily statistics. These daily statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.
Also, each Sunday night, the CM Tools Background Driver option automatically compresses the information contained within both the CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.
The data is also available on Capacity Planning (CP) Service’s Intranet Websites:
- Statistics—Provides statistics for each listed site: http://vaww.vista.med.va.gov/capman/site_statistics.asp
- Projections—Provides data trends for each listed site: http://vaww.vista.med.va.gov/capman/site_projections.asp
IRM staff utilizes the options that are available at the site to manage this software. IRM staff responsible for capacity planning tasks at the site can use these options to review system workload trends. Additionally, the IRM staff can review specific VistA HL7 workload data.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the initial setup procedures are performed as detailed in the *Capacity Management (CM) Tools Installation Guide*, the software basically operates transparent to IRM with minimal impact on system resources. The software uses the Kernel-supplied TaskMan utility to schedule a background task and it is then rescheduled to run on a regular nightly basis. The nightly time frame for data file upload was chosen in order to minimize network impact.

![](capacity-management-tools-version-3-technical-manual/014.png) REF: For more information on initial setup procedures, see the “Preliminary Consideration” section in the *Capacity Management Tools Installation Guide*.

![](capacity-management-tools-version-3-technical-manual/015.png) REF: For more information on CM Tools and CM Tool-related options, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Service has been given the KMP\* namespace for both routines and globals. The Capacity Management Tools Software utilizes the KMP<u>D</u> namespace for its routines and global. Therefore, you should review your translation table settings to determine the proper placement for the KMP\* global namespace.

### ^KMPD Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools 3.0 software installation creates the ^KMPD global to store the following files:

- CP CODE EVALUATOR file (#8972.1)—Stores Code Evaluator data.
- CP DATA ELEMENTS file (#8972.3)—Static file that stores the data elements names.
- CP PARAMETERS file (#8973)—Static file.
- CM HL7 DATA file (#8973.1)—Records are trimmed nightly.
- CP TIMING file (#8973.2)—Records are trimmed nightly.
- CP REPORTS file (#8973.3)—Contains the name of the CM Tools reports available from the GUI Reports tab.

The CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files in the ^KMPD global are trimmed (records deleted) by the nightly CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] to contain a maximum number of day’s data as determined by the appropriate CP parameters in the CP PARAMETERS file (#8973) .

![](capacity-management-tools-version-3-technical-manual/016.png) REF: For more information on the CP parameters, see the “Edit CP Parameters File” section in Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

### Check CM Tools Background Driver Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM staff should use the CP Environment Check option \[KMPD STATUS\] to ensure that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is scheduled to run daily at 1:30 a.m.

If the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is *not* shown as being scheduled to run in the future, the IRM staff should use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], to schedule the KMPD BACKGROUND DRIVER option to run daily at 1:30 a.m.

![](capacity-management-tools-version-3-technical-manual/017.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

![](capacity-management-tools-version-3-technical-manual/018.png) REF: For more information on the Background Driver option, see the “<u>CM Tools Background Driver</u>”section in Chapter <u>6</u>, “<u>Exported Options</u>.”

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information throughout this manual is meant to help IRM in the maintenance of the software. The discussion that follows covers the options available to assist IRM in that maintenance.

### CP Tools Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All options for the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\] can be found under the Capacity Planning menu \[XTCM MAIN\]. The XTCM MAIN menu is found under the Eve menu and should be assigned to IRM staff members who support this software and other capacity planning tasks.

![](capacity-management-tools-version-3-technical-manual/019.png) REF: For more information on the CP Tools Manger Menu, see the “<u>CP Tools Manager Menu</u>“ section in Chapter <u>6</u>, “<u>Exported Options</u>,” in this manual or Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

### CM Tools Background Driver Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM staff should first invoke the CP Environment Check option \[KMPD STATUS\], which is located under the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\], to ensure that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is scheduled to run daily at 1:30 a.m.

If the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is *not* shown as being scheduled to run in the future, the CP Environment Check option \[KMPD STATUS\] prompts to queue the task every night at 1:30 a.m. Alternately, you can also use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], to schedule the KMPD BACKGROUND DRIVER option to run daily at 1:30 a.m.

![](capacity-management-tools-version-3-technical-manual/020.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

![](capacity-management-tools-version-3-technical-manual/021.png) REF: For more information on the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\], see the “<u>CM Tools Background Driver</u>“ section in Chapter <u>6</u>, “<u>Exported Options</u>,” in this manual or Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the files exported with Capacity Management (CM) Tools, including the file number, file name, global location, and description of the files.

![](capacity-management-tools-version-3-technical-manual/022.png) REF: For more information on the CM Tools globals, see Chapter <u>4</u>, “<u>Global Translation, Journaling, and Protection</u>.”

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Management Tools 3.0 exports the following files:

<table>
<caption><p><span id="_Toc439224980" class="anchor"></span>Table . CM Tools—Files</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>File Number</th>
<th>File Name</th>
<th>Global</th>
<th>File Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8972.1</td>
<td>CP CODE EVALUATOR</td>
<td>^KMPD(8972.1</td>
<td><p>This file holds data for the Code Evaluator. The Code Evaluator allows programmers to test the efficiency of M code changes.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="even">
<td>8972.3</td>
<td>CP DATA ELEMENTS</td>
<td>^KMPD(8972.3</td>
<td>This is a static file that contains the names of the data elements used by Capacity Planning. This file comes with data and should <em>not</em> be edited in any way.</td>
</tr>
<tr class="odd">
<td>8973</td>
<td>CP PARAMETERS</td>
<td>^KMPD(8973</td>
<td><p>This file was created to contain the parameters and data for the following:</p>
<p>Current versions/patches of Capacity Planning applications: Resource Usage Monitor (RUM), Statistical Analysis of Global Growth (SAGG), and Capacity Management (CM) Tools.</p>
<p>Start, stop, and delta times for all daily/weekly background jobs.</p>
<p>The number of weeks to keep data: RUM, HL7, and Timing.</p>
<p>Current facility CPU data:</p>
<p>Node</p>
<p>Type of CPU</p>
<p>Number of processors</p>
<p>Processor speed</p>
<p>Amount of memory</p></td>
</tr>
<tr class="even">
<td>8973.1</td>
<td>CM HL7 DATA</td>
<td>^KMPD(8973.1</td>
<td><p>This file stores VistA HL7 workload information.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="odd">
<td>8973.2</td>
<td>CP TIMING</td>
<td>^KMPD(8973.2</td>
<td><p>This file stores the timing statistics that are gathered when the Start/Stop Timing Collection option [KMPD TMG START/STOP] is set to “running.” During the day, timing data is saved into the temporary ^KMPTMP(“KMPDT”) global. Each night a background job compiles this temporary data into daily statistics and stores this data in File #8973.1 (CP Timing). The data in File #8973.1 is purged each night to ensure only 30 days of data exist.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="even">
<td>8973.3</td>
<td>CP REPORTS</td>
<td>^KMPD(8973.3</td>
<td><p>This file contains the name of the CM Tools reports available from the GUI Reports tab.</p>
<p>This file comes with data and should <em>not</em> be edited in any way.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc439224980" class="anchor"></span>Table . CM Tools—Files

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Management Tools 3.0 exports the following templates:

| Template                              | Description                                                                           |
|---------------------------------------|---------------------------------------------------------------------------------------|
| LIST MANAGER TEMPLATE \[KMPD STATUS\] | This template is used to display the status (environment) check for each application. |

<span id="_Toc439224981" class="anchor"></span>Table . CM Tools—Exported templates

# Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following globals are distributed with the Capacity Management Tools software:

<table>
<caption><p><span id="_Toc439224982" class="anchor"></span>Table . CM Tools—Globals distributed</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Global</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^KMPD</td>
<td><p>The ^KMPD global contains the following files:</p>
<ul>
<li><p>CP CODE EVALUATOR file (#8972.1)</p></li>
<li><p>CP DATA ELEMENTS file (#8972.3)</p></li>
<li><p>CP PARAMETERS file (#8973)</p></li>
<li><p>CM HL7 DATA file (#8973.1)</p></li>
<li><p>CP TIMING file (#8973.2)</p></li>
</ul>
<p>Each night this global is trimmed (records deleted) automatically to contain the correct maximum number of day’s data as determined by the appropriate CP parameters. This global is trimmed by the CM Tools Background Driver option [KMPD BACKGROUND DRIVER], which is scheduled to run daily at 1:30 a.m.</p></td>
</tr>
<tr class="even">
<td>^KMPTMP(“KMPDT”)</td>
<td><p>The ^KMPTMP(“KMPDT”) temporary collection global contains Timing data for the CPRS Coversheet.</p>
<p>Data within this global is compiled and moved into the CP TIMING file (#8973.2). Upon completion, the data within the ^KMPTMP(“KMPDT”) temporary collection global is purged.</p>
<p>![](capacity-management-tools-version-3-technical-manual/023.png) <strong>NOTE:</strong> Data for Foreground coversheet section loads are stored in ^KMPTMP(“KMPDT”,”ORWCV-FT”). Data for Background coversheet section loads are stored in ^KMPTMP(“KMPDT”,”ORWCV”). Depending on system configuration coversheet sections can be loaded in the foreground, background, or a combination of the two (<em>not recommended</em>). If a section is <em>not</em> explicitly set to dis-allow background processing then it is by default processed in the background.</p></td>
</tr>
<tr class="odd">
<td>^TMP(“KMPDH”,$J)</td>
<td>The ^TMP(“KMPDH”,$J) temporary collection global contains data that is gathered from the VistA Health Level Seven (HL7) software by the CM Tools Background Driver option [KMPD BACKGROUND DRIVER], which is scheduled to run daily at 1:30 a.m.<br />
<br />
Data within this global is compiled and moved into the CM HL7 DATA file (#8973.1). Upon completion, the data within the ^TMP(“KMPDH”,$J) temporary collection global is purged.</td>
</tr>
</tbody>
</table>

<span id="_Toc439224982" class="anchor"></span>Table . CM Tools—Globals distributed

## Translation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the translation requirements/recommendations for the CM Tools globals:

| Global  | Translation                                                                                                                                                              |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ^KMPD   | Mandatory, if the operating system supports this function. It is recommended that all Capacity Planning (CP) globals be translated to the same volume set (i.e., KMP\*). |
| ^KMPTMP | Mandatory, if the operating system supports this function. It is recommended that all Capacity Planning (CP) globals be translated to the same volume set (i.e., KMP\*). |

<span id="_Ref332204375" class="anchor"></span>Table . CM Tools—Global translation requirements/recommendations

## Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the journaling requirements/recommendations for the CM Tools globals:

| Global  | Journaling                                                 |
|---------|------------------------------------------------------------|
| ^KMPD   | Mandatory, if the operating system supports this function. |
| ^KMPTMP | *Not* recommended.                                         |

<span id="_Ref332204400" class="anchor"></span>Table . CM Tools—Global journaling requirements/recommendations

## Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> lists the protection settings for the CM Tools globals:

<table>
<caption><p><span id="_Ref332204416" class="anchor"></span>Table . CM Tools—Global protection settings</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Global Name</th>
<th>Caché Protection</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^KMPD</td>
<td><p>Owner: RW</p>
<p>Group: RW</p>
<p>World: RW</p>
<p>Network: RW</p></td>
</tr>
<tr class="even">
<td>^KMPTMP</td>
<td><p>Owner: RW</p>
<p>Group: RW</p>
<p>World: RW</p>
<p>Network: RW</p></td>
</tr>
</tbody>
</table>

<span id="_Ref332204416" class="anchor"></span>Table . CM Tools—Global protection settings

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains a list of the routines exported with the Capacity Management Tools software (routines are listed alphabetically). A brief description of the routines is provided.

<table>
<caption><p><span id="_Toc439224986" class="anchor"></span>Table . CM Tools—Routines</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine Name</th>
<th>Routine Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPDBD01</td>
<td><p>This routine uses a Health Level Seven (HL7) API call to transfer HL7 data to the CM HL7 DATA file (#8973.1). This routine is called by the CM Tools Background Driver option [KMPD BACKGROUND DRIVER].</p>
<p>Every Sunday night, this routine creates weekly statistics from the data within the CM HL7 DATA file (#8973.1) and uploads this information to the Capacity Planning National Database.</p>
<p>This routine monitors and trims (records deleted) the following files to ensure that the correct maximum number of days data is maintained as determined by the CP parameters:</p>
<p>CM HL7 DATA file (#8973.1)—The maximum amount of data collected is determined by the Purge HL7 Data After CP parameter.</p>
<p>CP TIMING file (#8973.2)—The maximum amount of data collected is determined by the Purge Timing Data After CP parameter.</p></td>
</tr>
<tr class="even">
<td>KMPDECH</td>
<td>This routine is part of the VistA Monitor program. It sends a return message from the site to the Capacity Planning National Database.</td>
</tr>
<tr class="odd">
<td>KMPDHU01<br />
KMPDHU02<br />
KMPDHU03</td>
<td><p>This routine compiles and compresses the Health Level Seven (HL7) data into daily and weekly statistics. These routines are called by the KMPDBD01 routine.</p>
<p>Daily (every night)—These routines take data from the ^KMPTMP(“KMPD” global and compress it into daily statistics and save it into the CM HL7 DATA file (#8973.1).</p>
<p>Weekly (every Sunday night)—These routines upload the weekly HL7 statistical data stored in the CM HL7 DATA file (#8973.1) to the Capacity Planning National Database.</p></td>
</tr>
<tr class="even">
<td>KMPDPOST</td>
<td><p>This routine schedules the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] to run every night at 1:30 a.m.</p>
<p>This routine updates the CM TOOLS CURRENT VERSION field (#.02) in the CP PARAMETERS file (#8973).</p>
<p>It is a post-install routine.</p></td>
</tr>
<tr class="odd">
<td>KMPDRDAT</td>
<td>This routine sends daily coversheet load data to the Capacity Planning National Database.</td>
</tr>
<tr class="even">
<td>KMPDSS</td>
<td><p>CM Tools Status—This routine is associated with the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] and displays the current status of the CM Tools Background Driver. It is called by the CP Environment Check option [KMPD STATUS].</p>
<p>This routine also shows information on the following files:</p>
<p>CM HL7 DATA file (#8973.1)</p>
<p>CP TIMING file (#8973.2)—Only displays information if the file has data.</p>
<p>If the background task is <em>not</em> listed as being scheduled, this routine notifies users in the report output. Users should then queue the task to run every night at 1:30 a.m.</p></td>
</tr>
<tr class="odd">
<td>KMPDSS1</td>
<td>CP Status—This routine is associated with the CP Environment Check option [KMPD STATUS].</td>
</tr>
<tr class="even">
<td>KMPDSSD</td>
<td>CM Tools Status—This routine is associated with the CP Environment Check option [KMPD STATUS] for HL7 and CM Tools-related data.</td>
</tr>
<tr class="odd">
<td>KMPDSSD1</td>
<td>CM Tools Status—This routine is associated with the CP Environment Check option [KMPD STATUS] for HL7 and CM Tools-related data. It includes remote users when listing members of KMP-APMAN mail group.</td>
</tr>
<tr class="even">
<td>KMPDSSR</td>
<td>CP Status: Resource Usage Monitor (RUM)—This routine is associated with the CP Environment Check option [KMPD STATUS] for RUM-related data. It also checks the Statistical Analysis of Global Growth (SAGG) environment to use ListMan.</td>
</tr>
<tr class="odd">
<td>KMPDSSS</td>
<td>CP Status: Statistical Analysis of Global Growth (SAGG)—This routine is associated with the CP Environment Check option [KMPD STATUS] for SAGG-related data.</td>
</tr>
<tr class="even">
<td>KMPDTM</td>
<td>This routine runs the Timing Monitor option [KMPD TMG MONITOR].</td>
</tr>
<tr class="odd">
<td>KMPDTP1<br />
KMPDTP2<br />
KMPDTP3<br />
KMPDTP4<br />
KMPDTP5<br />
KMPDTP6<br />
KMPDTP7</td>
<td>Report routines.</td>
</tr>
<tr class="even">
<td><p>KMPDTU01<br />
KMPDTU02<br />
KMPDTU10<br />
KMPDTU11</p>
<p>KMPDU<br />
KMPDU1<br />
KMPDU11<br />
KMPDU2<br />
KMPDU3<br />
KMPDU4<br />
KMPDU5<br />
KMPDU6<br />
KMPDU7<br />
KMPDU7A</p>
<p>KMPDUG<br />
KMPDUG1<br />
KMPDUG2<strong><br />
</strong>KMPDUGV</p>
<p>KMPDUT<br />
KMPDUT1<br />
KMPDUT2<br />
KMPDUT4<br />
KMPDUT4A<br />
KMPDUT4B<br />
KMPDUT4C<br />
KMPDUT5<br />
<br />
KMPDUTL<br />
KMPDUTL1<br />
KMPDUTL2<br />
KMPDUTL3<br />
KMPDUTL4<br />
KMPDUTL5<br />
KMPDUTL6<br />
KMPDUTL7<br />
KMPDUTL8</p></td>
<td>Generic utility routines that are called by varying Capacity Management Tools routines.</td>
</tr>
</tbody>
</table>

<span id="_Toc439224986" class="anchor"></span>Table . CM Tools—Routines

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists and briefly describes the options that are exported with or related to the Capacity Management Tools software.

![](capacity-management-tools-version-3-technical-manual/024.png) REF: For more detailed information on the Capacity Management Tools-related options, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

## Options *with* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 10</u> lists the options that are exported with or related to the Capacity Management Tools software. Options are listed hierarchically:

<table>
<caption><p><span id="_Ref332204438" class="anchor"></span>Table . CM Tools—Exported options <em>with</em> parents</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Menu Text</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XTCM MAIN</td>
<td>Capacity Planning</td>
<td>Menu</td>
</tr>
<tr class="even">
<td>KMP MAIL GROUP EDIT</td>
<td>Capacity Planning Mail Group Edit</td>
<td>Action</td>
</tr>
<tr class="odd">
<td>KMPD CM TOOLS MANAGER MENU</td>
<td>CP Tools Manager Menu</td>
<td>Menu</td>
</tr>
<tr class="even">
<td>KMPD STATUS</td>
<td>CP Environment Check option</td>
<td>Run Routine:<br />
<br />
EN^KMPDSS</td>
</tr>
<tr class="odd">
<td>KMPD TMG START/STOP</td>
<td>Start/Stop Timing Collection</td>
<td>Run Routine:<br />
<br />
SST^KMPDSS</td>
</tr>
<tr class="even">
<td>KMPD PARAM EDIT</td>
<td>Edit CP Parameters File option</td>
<td>Run Routine:<br />
<br />
PRM^KMPDSS</td>
</tr>
<tr class="odd">
<td>KMPD TMG MONITOR</td>
<td>Timing Monitor option</td>
<td>Run Routine:<br />
<br />
KMPDTM</td>
</tr>
<tr class="even">
<td>KMPD CM TOOLS REPORTS</td>
<td>CP Tools Reports</td>
<td>Menu</td>
</tr>
<tr class="odd">
<td>KMPD TMG REPORTS</td>
<td>Timing Reports</td>
<td>Menu</td>
</tr>
<tr class="even">
<td>KMPD TMG AVG TTL</td>
<td>Average Daily Coversheet Load</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP1</td>
</tr>
<tr class="odd">
<td>KMPD TMG HRLY TTL</td>
<td>Average Hourly Coversheet Load</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP3</td>
</tr>
<tr class="even">
<td>KMPD TMG DLY TTL DETAIL</td>
<td>Detailed Daily Coversheet Load</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP2</td>
</tr>
<tr class="odd">
<td>KMPD TMG HRLY TTL DETAIL</td>
<td>Detailed Hourly Coversheet Load</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP4</td>
</tr>
<tr class="even">
<td>KMPD TMG TTL ALERT</td>
<td>Threshold Alert</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP5</td>
</tr>
<tr class="odd">
<td>KMPD TMG TTL ALERT RT</td>
<td>Real-Time Threshold Alert</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP6</td>
</tr>
<tr class="even">
<td>KMPD TMG HRLY TTL RT</td>
<td>Real-Time Average Hourly Coversheet Load</td>
<td>Run Routine:<br />
<br />
EN^KMPDTP7</td>
</tr>
</tbody>
</table>

<span id="_Ref332204438" class="anchor"></span>Table . CM Tools—Exported options *with* parents

### Capacity Planning Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Planning menu \[XTCM MAIN; Synonym: CM\] is located under the Operations Management menu \[XUSITEMGR\], which is located under Kernel’s Systems Manager Menu \[Eve\]. This menu holds all the currently available capacity planning options. The XTCM MAIN menu can be assigned to the IRM staff members who support this software and other capacity planning tasks.

The Capacity Planning menu-related options that are discussed in the CM Tools documentation include the following:

- Capacity Planning Mail Group Edit option
- CP Tools Manager Menu and subordinate options

### Capacity Planning Mail Group Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Planning Mail Group Edit option \[KMP MAIL GROUP EDIT; Synonym: CPG\] is located under the Capacity Planning menu \[XTCM MAIN\]. It is used to edit KMP-CAPMAN mail group. It is used to edit the KMP-CAPMAN mail group. The KMP-CAPMAN mail group is defined with the installation of the CM Tools software.

### CP Tools Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU; Synonym: TLS\] is located under the Capacity Planning menu \[XTCM MAIN\]. The CP Tools Manager Menu contains the following options:

- CP Environment Check \[KMPD STATUS\]
- Start/Stop Timing Collection \[KMPD TMG START/STOP\]
- Edit CP Parameters File \[KMPD PARAM EDIT\]
- Timing Monitor \[KMPD TMG MONITOR\]
- CP Tools Reports \[KMPD CM TOOLS REPORTS\]

### CP Environment Check Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Environment Check option \[KMPD STATUS; Synonym: STA\] is located under the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\]. It allows users to check the capacity planning environment at their site. It displays data from the following areas:

- Health Level Seven (HL7)
- Resource Usage Monitor (RUM)
- Statistical Analysis of Global Growth (SAGG)
- Timing

Depending on the report data option chosen (i.e., HL7, RUM, SAGG, or Timing), this option identifies the number of entries within the following files (listed alphabetically by file name):

- CM HL7 DATA file (#8973.1)
- CP TIMING file (#8973.2)
- RESOURCE USAGE MONITOR file (#8971.1)
- SAGG PROJECT file (#8970.1)

Additionally, this option shows the reschedule frequency of the following options (listed alphabetically by option name):

- CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\].
- RUM Background Driver option \[KMPR BACKGROUND DRIVER\].
- SAGG Master Background Task option \[KMPS SAGG REPORT\].

### Start/Stop Timing Collection Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Start/Stop Timing Collection option \[KMPD TMG START/STOP; Synonym: SST\] is located under the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\]. It is used to initiate or stop the CM Tools collection routines to begin or stop collecting VistA HL7 workload data.

### Edit CP Parameters File Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit CP Parameters File option \[KMPD PARAM EDIT; Synonym: PRM\] is located on the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\]. It allows editing of the Capacity Planning (CP) parameters in the CP PARAMETERS file (#8973).

![](capacity-management-tools-version-3-technical-manual/025.png) NOTE: The VistA Monitor-related parameters (i.e., scheduled down time parameters) that are entered with the Edit CP Parameters File option \[KMPD PARAM EDIT\] are monitored by the CP Echo Server server-type option \[KMPD ECHO\].  
  
REF: For more detailed information on the CP Echo Server server-type option \[KMPD ECHO\], see the “<u>CP Echo Server</u>” section.

### Timing Monitor Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Timing Monitor option \[KMPD TMG MONITOR; Synonym: TMT\] is located on the <u>CP Tools Manager Menu</u> \[KMPD CM TOOLS MANAGER MENU\]. This option updates itself automatically and displays the average number of seconds it takes Computerized Patient record System (CPRS) coversheets to load in a period of time. Data is displayed in a bar graph. The x-axis of the bar graph indicates the hours of the day (from 0 up to 23) and the y-axis indicates the average number of seconds it takes to load CPRS coversheets. This option can be left running on a terminal continuously collecting data.

The Timing Monitor displays data for each hour of the day and each new hour as it comes up (i.e., 0–23 hours). It updates the data according to the value in the MONITOR UPDATE RATE - MINUTES field (#19.01) in the CP PARAMETERS file (#8973). If there is no entry in Field \#19.01, the default is every 10 minutes. The CPRS coversheet load data is displayed in a bar graph for each hour the Timing Monitor is running. If the Timing Monitor is run continuously, the cycle repeats every 24 hours overlaying/replacing previous data and adjusting the bar graph accordingly. The bar graph is also adjusted for the latest information gathered based on the value in the MONITOR UPDATE RATE - MINUTES field (#19.01) in the CP PARAMETERS file (#8973).

The Timing Monitor also displays an Alert Message near the bottom of the screen if the average number of seconds to load a CPRS coversheet exceeds the value of the MONITOR ALERT - SECONDS field (#19.02) in the CP PARAMETERS file (#8973). If there is no entry in Field \#19.02, the default is 30 seconds. Both of these parameters can be edited using the Edit CP Parameters File option \[KMPD PARAM EDIT\].

### CP Tools Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Tools Reports menu \[KMPD CM TOOLS REPORTS; Synonym: RPT\] is located under the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\]. It contains the Timing Reports \[KMPD TMG REPORTS\] option.

### Timing Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Timing Reports menu \[KMPD TMG REPORTS; Synonym: TMG\] is located under the CP Tools Reports menu \[KMPD CM TOOLS REPORTS\]. It contains the following report options:

- Average Daily Coversheet Load \[KMPD TMG AVG TTL\]
- Average Hourly Coversheet Load \[KMPD TMG HRLY TTL\]
- Detailed Daily Coversheet Load \[KMPD TMG DLY TTL DETAIL\]
- Detailed Hourly Coversheet Load \[KMPD TMG HRLY TTL DETAIL\]
- Threshold Alert \[KMPD TMG TTL ALERT\]
- Real-Time Threshold Alert \[KMPD TMG TTL ALERT RT\]
- Real-Time Average Hourly Coversheet Load \[KMPD TMG HRLY TTL RT\]
- Reports display both Foreground and Background coversheet section timings.

### Average Daily Coversheet Load Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Average Daily Coversheet Load option \[KMPD TMG AVG TTL; Synonym: AVD\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the daily average time-to-load value for the coversheet at a site. Average time-to-load values are given for either daily prime time or non-prime time periods.

### Average Hourly Coversheet Load Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Average Hourly Coversheet Load option \[KMPD TMG HRLY TTL; Synonym: AVH\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly average time-to-load value for the coversheet at a site over a 24-hour period.

### Detailed Daily Coversheet Load Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Detailed Daily Coversheet Load option \[KMPD TMG DLY TTL DETAIL; Synonym: DTD\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the daily time-to-load values for the coversheet at a site. The report breaks the time-to-load metrics into ten second groupings.

### Detailed Hourly Coversheet Load Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Detailed Hourly Coversheet Load option \[KMPD TMG HRLY TTL DETAIL; Synonym: DTH\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly time-to-load values for the coversheet at a site. The report breaks the time-to-load metrics into ten second groupings.

### Threshold Alert Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Threshold Alert option \[KMPD TMG TTL ALERT; Synonym: TAL\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the particular coversheet loads that had excessive time-to-load values. This report searches for a particular person, client name, or Internet Protocol (IP) address.

### Real-Time Threshold Alert Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Real-Time Threshold Alert option \[KMPD TMG TTL ALERT RT; Synonym: RTA\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the particular coversheet loads that have excessive time-to-load values for TODAY (real-time). This report searches for a particular person, client name, or Internet Protocol (IP) address.

### Real-Time Average Hourly Coversheet Load Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Real-Time Average Hourly Coversheet Load option \[KMPD TMG HRLY TTL RT; Synonym: RAV\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly average time-to-load value for the coversheet at a site over a 24-hour period.

## Options *without* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following option does *not* appear on any menu:

<table>
<caption><p><span id="_Toc439224988" class="anchor"></span>Table . CM Tools—Exported options <em>without</em> parents</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Menu Text</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPD BACKGROUND DRIVER</td>
<td>CM Tools Background Driver</td>
<td>Run Routine:<br />
<br />
KMPDBD01</td>
</tr>
</tbody>
</table>

<span id="_Toc439224988" class="anchor"></span>Table . CM Tools—Exported options *without* parents

### CM Tools Background Driver Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is *not* assigned to any menu. This option is scheduled through TaskMan to start the Capacity Management Tools software’s background routine.

This option compresses the CM Tools statistics located in the CM HL7 DATA file (#8973.1) into daily statistics. This option *must* be queued to run each day on off hours.

![](capacity-management-tools-version-3-technical-manual/026.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

This option should be (re)scheduled with the Schedule/Unschedule Options option \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\].

![](capacity-management-tools-version-3-technical-manual/027.png) REF: For more information on any of these options, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

## Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Management Tools 3.0 exports the following server option:

<table>
<caption><p><span id="_Toc439224989" class="anchor"></span>Table . CM Tools—Exported server options</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Menu Text</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPD ECHO</td>
<td>CP Echo Server</td>
<td>Server:<br />
<br />
KMPDECH</td>
</tr>
</tbody>
</table>

<span id="_Toc439224989" class="anchor"></span>Table . CM Tools—Exported server options

![](capacity-management-tools-version-3-technical-manual/028.png) REF: For more information on server options, see Chapter 11, “Server Options,” in the *Kernel Systems Management Guide*.

### CP Echo Server Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Echo Server option \[KMPD ECHO\] is a server-type option and is *not* assigned to any menu. This option is part of the VistA Monitor program.

The VistA Monitor allows Health Systems Implementation Training and Enterprise Support (HSITES) to determine if a site is down (*not* operating). The process is as follows:

1.  A message is sent from the Capacity Planning National Database to each site every 20 minutes.
10. The message is received at the site via the CP Echo Server server-type option \[KMPD ECHO\].
11. The KMPD ECHO server option at the site then triggers a bulletin that sends an e-mail message back to the Capacity Planning National Database.
12. If the Capacity Planning National Database has *not* received a return message from the site (e.g., for an hour or more), and there are no entries in the SCHEDULED DOWN TIME START (#5.01) and SCHEDULED DOWN TIME STOP (#5.02) fields, then the site is considered to be in an unscheduled down time state, and a message is sent to a mail group notifying members of the situation.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software does *not* export any protocols with this version.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software contains two files that are purged:

- CM HL7 DATA (#8973.1)
- CP TIMING file (#8973.2)

Every Sunday night, the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] monitors and trims (records deleted) the following files to ensure that the correct maximum number of day’s data is maintained as determined by the appropriate CP parameters:

- CM HL7 DATA file (#8973.1)—Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- CP TIMING file (#8973.2)—Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Since the Capacity Management Tools software automatically maintains a fixed amount of data at the site, archiving functions are *not* necessary and are *not* provided.

![](capacity-management-tools-version-3-technical-manual/029.png) REF: For more information on the CM Tools Background Driver option and the CP parameters, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resource usage data is accumulated into the ^TMP(“KMPDH”,\$J) temporary collection global and is purged (killed) daily at 1:30 a.m. by the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] after being moved into the following files:

- CM HL7 DATA (#8973.1)
- CP TIMING file (#8973.2)

![](capacity-management-tools-version-3-technical-manual/030.png) REF: For more information on the ^TMP(“KMPDH”,\$J) global, see Chapter <u>4</u>, “<u>Global Translation, Journaling, and Protection</u>.”

The CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] monitors and trims (records deleted) the following files to ensure that the correct maximum number of day’s data is maintained as determined by the appropriate CP parameters:

- CM HL7 DATA file (#8973.1)—Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- CP TIMING file (#8973.2)—Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973) . This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Since the Capacity Management Tools software automatically maintains a fixed amount of data at the site, purging functions are *not* necessary and are *not* provided.

![](capacity-management-tools-version-3-technical-manual/031.png) REF: For more information on the CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files, see Chapter <u>3</u>, “<u>Files</u>.”

![](capacity-management-tools-version-3-technical-manual/032.png) REF: For more information on the CM Tools Background Driver option and CP parameters, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Capacity Management Tools software does *not* provide any callable routine entry points (i.e., Application Program Interfaces \[APIs\]) that are available for general use (i.e., Supported APIs).

## Controlled Subscription APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 13</u> lists the Controlled Subscription APIs for Capacity Management Tools. These are callable routines for which you *must* obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.

<table>
<caption><p><span id="_Ref308163350" class="anchor"></span>Table : Supported Capacity Management Tools for which an IA is required (Controlled Subscription APIs)</p></caption>
<colgroup>
<col style="width: 91%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>API, Description, Input Parameters/Input Variables, and Example</th>
<th>IA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Name:</strong> TIMING^KMPDTU11()</p>
<p><strong>Description:</strong> API to Start and Stop gathering Timing stats for Capacity Planning. This API is designed to allow packages to put hooks into a routine to gather timing data (how long it takes to run).</p>
<p><strong>Input Parameters/Input Variables:</strong></p>
<ul>
<li><p>KMPDSS: Subscript (free text) used to identify timing data.</p></li>
<li><p>KMPDNODE: Node name (free text).</p></li>
<li><p>KMPDST: Start/Stop - 1 = start timing, 2 = stop timing</p></li>
<li><p>KMPDHTM: Current time in $H format (optional).</p></li>
<li><p>KMPDUZ: Current DUZ of user (optional).</p></li>
<li><p>KMPDCL: Client name (free text). If <em>not</em> defined the current IO(“CLNM”) is used (optional).</p></li>
</ul>
<p><strong>Example to <mark><em>Start</em> TIMING</mark>:</strong></p>
<p>&gt;<strong><mark>D TIMING^KMPDTU11(“ORWCV”,”673AAA”,1,$H,$G(DUZ))</mark></strong></p>
<p><strong>Example to <mark><em>Stop</em> TIMING</mark>:</strong></p>
<p>&gt;<strong><mark>D TIMING^KMPDTU11(“ORWCV”,”673AAA”,2)</mark></strong></p></td>
<td>5003</td>
</tr>
<tr class="even">
<td><p><strong>Name:</strong> ^KMPTMP(“KMPDT”) -- CAPACITY PLANNING TIMING METRIC DATA</p>
<p><strong>Description:</strong> RK: Generate Capacity Planning (CP) timing metric data for capacity planning purposes.</p>
<p>![](capacity-management-tools-version-3-technical-manual/033.png) <strong>NOTE:</strong> Sites <em>must</em> use the TIMING^KMPDTU11() API described above to generate timing data.</p></td>
<td>4313</td>
</tr>
</tbody>
</table>

<span id="_Ref308163350" class="anchor"></span>Table : Supported Capacity Management Tools for which an IA is required (Controlled Subscription APIs)

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software relies on the following VistA software to run effectively (listed alphabetically):

<table>
<caption><p><span id="_Toc439224991" class="anchor"></span>Table . CM Tools—External Relations: VistA software</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 10%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Software</th>
<th>Version</th>
<th>Patch Information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Computerized Patient Record System (CPRS) GUI</p></li>
<li><p>Order Entry/Results Reporting (OE/RR)</p></li>
</ul></td>
<td><ul>
<li><p>23.0</p></li>
<li><p>3.0</p></li>
</ul></td>
<td><p>Fully patched.</p>
<p>![](capacity-management-tools-version-3-technical-manual/034.png) CAUTION: The CM Tools software loads without CPRS GUI 23 and OE/RR 3.0; however, in order to start collecting timing data and enable the data collection and report-related CM Tools software options, Patch OR*3.0*209 <em>must</em> also be installed.</p></td>
</tr>
<tr class="even">
<td>Health Level Seven (HL7)</td>
<td>1.6</td>
<td><p>Fully patched.</p>
<p>![](capacity-management-tools-version-3-technical-manual/035.png) CAUTION: The CM Tools software loads without HL7 Patch #79 (i.e., HL*1.6*79); however, in order to start collecting HL7 statistics, HL7 Patch #79 <em>must</em> also be installed.<br />
<br />
HL*1.6*79 installs the $$CM^HLUCM API. The $$CM^HLUCM API contains code that enables the collection of HL7 usage information from the VistA environment.</p></td>
</tr>
<tr class="odd">
<td>Resource Usage Monitor (RUM)</td>
<td>2.0</td>
<td>Fully patched.</td>
</tr>
<tr class="even">
<td>Statistical analysis of Global Growth (SAGG)</td>
<td>1.8</td>
<td>Fully patched.</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>8.0</td>
<td>Fully patched.</td>
</tr>
<tr class="even">
<td>Kernel Toolkit</td>
<td>7.3</td>
<td>Fully patched.</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>8.0</td>
<td>Fully patched.</td>
</tr>
<tr class="even">
<td>RPC Broker Client Agent (i.e., CLAGENT.exe)</td>
<td>1.0</td>
<td><p>Fully patched.</p>
<p>![](capacity-management-tools-version-3-technical-manual/036.png) <strong>NOTE:</strong> The CLAGENT.exe <em>must</em> be running in the background. This software is distributed with the CPRS GUI software.</p></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>22.0</td>
<td>Fully patched.</td>
</tr>
</tbody>
</table>

<span id="_Toc439224991" class="anchor"></span>Table . CM Tools—External Relations: VistA software

![](capacity-management-tools-version-3-technical-manual/037.png) NOTE: These software applications *must* be properly installed and *fully* patched prior to installing CM Tools 3.0. You can obtain all released GUI and VistA M server software via the Product Support (PS) Anonymous Directories.  
  
VistA M server patches (including patch description and installation instructions) are available from the Patch module on FORUM or through normal procedures. Patches *must* be installed in published sequence.

## DBA Approvals and Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are *not* available to the general programming public.

This version of Capacity Management (CM) Tools software is *not* dependent on any agreements.

### IAs—Current List for CM Tools as Custodian

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain the current list of IAs, if any, to which the CM Tools software (KMPD) is a custodian, perform the following procedures:

1.  Sign on to the FORUM system (forum.va.gov).
13. Go to the DBA menu \[DBA\].
14. Select the Integration Agreements Menu option \[DBA IA ISC\].
15. Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].
16. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].
17. When this option prompts you for a package, enter CAPACITY MANAGEMENT TOOLS or KMPD.
18. All current IAs to which the Capacity Planning (CP) Service’s CM Tools software is a custodian are listed.

### IAs—Detailed Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain detailed information on a specific integration agreement, perform the following procedures:

1.  Sign on to the FORUM system (forum.va.gov).
19. Go to the DBA menu \[DBA\].
20. Select the Integration Agreements Menu option \[DBA IA ISC\].
21. Select the Inquire option \[DBA IA INQUIRY\].
22. When prompted for “INTEGRATION REFERENCES,” enter the specific integration agreement number of the IA you would like to display.
23. The option then lists the full text of the IA you requested.

### IAs—Current List for CM Tools as Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain the current list of IAs, if any, to which the CM Tools software (KMPD) is a subscriber, perform the following procedures:

1.  Sign on to the FORUM system (forum.va.gov).
24. Go to the DBA menu \[DBA\].
25. Select the Integration Agreements Menu option \[DBA IA ISC\].
26. Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].
27. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].
28. When prompted with “START WITH SUBSCRIBING PACKAGE,” enter KMPD (uppercase). When prompted with “GO TO SUBSCRIBING PACKAGE,” enter KMPD (uppercase).
29. All current IAs to which the Capacity Planning (CP) Service’s CM Tools software is a subscriber are listed.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Option Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All options in the Capacity Management Tools software under the CP Tools Manager Menu \[KMPD MANAGER MENU\] can function independently.

Only TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], can invoke the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\].

![](capacity-management-tools-version-3-technical-manual/038.png) REF: For more information regarding the Capacity Management Tools options, see Chapter 3, “CM Tools: Options,” in the *Capacity Management Tools User Manual*.

## Relationship of CM Tools Software with VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS GUI 23.0 and OE/RR 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of Capacity Management Tools software loads without CPRS GUI 23 and OE/RR 3.0; however, in order to start collecting timing data and enable the data collection and report-related CM Tools software options, Patch OR\*3.0\*209 *must* also be installed.

![](capacity-management-tools-version-3-technical-manual/039.png) REF: For more information on the CM Tools report-related software options, see the “<u>Timing Reports</u>” section in Chapter <u>6</u>, “<u>Exported Options</u>.”

### HL7 1.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of Capacity Management Tools software loads without VistA Health Level Seven (HL7) Patch HL\*1.6\*79; however, in order to start collecting HL7 statistics, HL7 Patch \#79 *must* also be installed.

HL7 Patch \#79 created the following three APIs, which are used for calculating the volume of HL7 activity at a site over a user-defined period of time:

- \$\$CM^HLUCM
- \$\$CM2^HLUCM
- \$\$CM2F^HLUCM

These APIs calculate the volume of HL7 activity over a period of time. The information collected includes the following:

- Total number characters in the messages.
- Total Number of messages or message units.
- Total time elapsed for transmission of messages.

![](capacity-management-tools-version-3-technical-manual/040.png) REF: For more information regarding VistA HL7 Patch HL\*1.6\*103 and the APIs, see the HL\*1.6\*103 patch description in the Patch Module on FORUM.

## VistA Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Monitor allows Health Systems Implementation Training and Enterprise Support (HSITES) to determine if a site is down (*not* operating). The Capacity Planning National Database sends a message every 20 minutes to all sites. The message is received at each site via the CP Echo Server server-type option \[KMPD ECHO\]. A turn-around message is then sent from the site to the Capacity Planning National Database.

![](capacity-management-tools-version-3-technical-manual/041.png) REF: For more information on the VistA monitor and the CP Echo Server server-type option, see the “Edit CP Parameters File” section in Chapter 3, “CM Tools Options,” in the *Capacity Management Tools User Manual*.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Service has been given the KMP\* namespace for both routines and globals. The Capacity Management Tools software utilizes the KMP<u>D</u> namespace for its routines and global. Therefore, you should review your translation table settings to determine the proper placement for the KMP\* global namespace.

# Software-wide and Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software does *not* employ the use of software-wide or key variables.

# SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management (CM) Tools software falls under the Kernel software umbrella; therefore, CM Tools has the same Kernel Programming Standards and Conventions (SAC) exemptions (e.g., exemptions to use operating system-specific variables and functions).

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* special legal requirements involved in the use of the Capacity Management Tools software.

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Capacity Management Tools software creates the following mail group:

| Name       | Description                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------|
| KMP-CAPMAN | This mail group receives messages for all Capacity Management-related software (e.g., Capacity Management Tools, SAGG, and RUM). |

<span id="_Toc439224992" class="anchor"></span>Table . CM Tools—Mail Groups

### Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Capacity Management Tools software does *not* make use of alerts.

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Management Tools 3.0 creates the following bulletin:

<table>
<caption><p><span id="_Toc439224993" class="anchor"></span>Table . CM Tools—Bulletins</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Subject</th>
<th>Message</th>
<th>Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPD ECHO</td>
<td>CP Echo Server Error</td>
<td>The ‘CP Echo Server’ [KMPD ECHO] encountered an error.</td>
<td><p>The following parameters are included in this bulletin:</p>
<ul>
<li><p>Date/Time: |1|—The date and time (in human-readable format) when the server request was received.</p></li>
<li><p>Sender: |2|—The name of the sender of the server request.</p></li>
<li><p>Option name: |3|—The name of the option that was requested by Mailman.</p></li>
<li><p>Subject: |4|—The subject of the message that requested a server.</p></li>
<li><p>Message #: |5|—The internal number of the message requesting a server.</p></li>
<li><p>Comments: |6|—Comments appended to the bulletin. These may include errors trapped by the server software or operating system, as well as general purpose messages.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc439224993" class="anchor"></span>Table . CM Tools—Bulletins

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Capacity Management Tools software transmits the following to the Capacity Planning National Database located at the Albany OI Field Office:

- VistA Health Level Seven (HL7) Workload Information—VistA HL7 workload data is summarized and transmitted on a weekly basis.
- VistA Timing Data—Timing data is summarized and transmitted on a daily and weekly basis.

Data collected is automatically transferred via network mail (i.e., VistA MailMan) to the Capacity Planning National Database. The data is displayed graphically on the Capacity Planning Statistics Intranet website.

![](capacity-management-tools-version-3-technical-manual/042.png) REF: For more information on the Capacity Planning National Database and data display, see the “Statistics and Projections”section in Chapter 2, “CM Tools: Software Overview and Use,” in the *Capacity Management Tools User Manua*l.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No *non*-VA products are embedded in or required by this version of the Capacity Management Tools software, other than those provided by the underlying operating systems.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* electronic signatures used within this version of the Capacity Management Tools software.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* specific security keys exported with this version of the Capacity Management Tools software.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Capacity Management Tools software establishes the following security over its files:

| File Number | File Name         | DD    | RD    | WR    | DEL   | LAYGO | AUDIT |
|-------------|-------------------|-------|-------|-------|-------|-------|-------|
| 8972.1      | CP CODE EVALUATOR | @ | @ | @ | @ | @ | @ |
| 8972.3      | CP DATA ELEMENTS  | @ | @ | @ | @ | @ | @ |
| 8973        | CP PARAMETERS     | @ | @ | @ | @ | @ | @ |
| 8973.1      | CM HL7 DATA       | @ | @ | @ | @ | @ | @ |
| 8973.2      | CP TIMING         | @ | @ | @ | @ | @ | @ |
| 8973.3      | CP REPORTS        | @ | @ | @ | @ | @ | @ |

<span id="_Toc439224994" class="anchor"></span>Table . CM Tools—VA FileMan file protection

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special legal requirements involved in the use of the Capacity Management Tools software interface.

Distribution of the Capacity Management Tools software is unrestricted.

<span id="_Toc423486600" class="anchor"></span>

Glossary

| Term              | Description                                                                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAPACITY PLANNING | The process of assessing a system’s capacity and evaluating its efficiency relative to workload in an attempt to optimize system performance. (Formerly known as Capacity Management.)                     |
| CM TOOLS          | Capacity Management Tools. A fully automated support tool developed by Capacity Planning (CP) Service, which entails the daily capture of VistA HL7 workload information from participating sites. |
| COVERSHEET        | The Computerized Patient Record System (CPRS) coversheet, which is the main CPRS page. This main page is a screen of the CPRS patient chart that displays an overview of the patient’s record.             |
| PRIME TIME HOURS  | Prime time hours are 8:00 a.m. to 5:00 p.m. (17:00) Monday through Friday, *excluding* holidays. Non-prime time hours are all other hours (i.e., weekends, nights and holidays).                           |

<span id="_Toc439224995" class="anchor"></span>Table 18. Capacity Management Tools glossary terms

![](capacity-management-tools-version-3-technical-manual/043.png) REF: For a list of commonly used terms and definitions, see the OI&T Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

<span id="_Toc439223762" class="anchor"></span>Index

A

Acronyms

Intranet Website, 32

ACTIVE by Custodial Package Option, 24

Alerts, 29

Archiving, 20

Assumptions, xi

Average Daily Coversheet Load Option, 13, 16

Average Hourly Coversheet Load Option, 13, 16

B

Background Driver Option

Purge HL7 Data After Parameter, 1, 4, 5, 10, 17, 20

Purge Timing Data After Parameter, 1, 4, 5, 10, 17, 20

Background Job

CM Tools Background Driver Scheduling Frequency, 3, 4, 5, 8, 17, 20

Bulletins

KMPD ECHO, 29

C

Callable Routines, 22

Controlled Subscription API, 22

Callout Boxes, x

Capacity Planning

Mail Group Edit Option, 13, 14

Menu, 4, 13, 14

National Database, 1, 2, 10, 19, 27, 30

Projections Website, 2

Statistics Website, 2, 30

CM HL7 DATA File (#8973.1), 1, 2, 3, 4, 5, 6, 8, 10, 15, 17, 20, 30

CM Tools

Background Driver Option, 1, 2, 3, 4, 8, 10, 15, 17, 20, 26

Startup/Stop Process, 15

CM TOOLS CURRENT VERSION Field (#.02), 10

Collection Globals

KMPD, 8

KMPTMP(”KMPDT”), 8

TMP(”KMPDH”,\$J), 1, 8, 20

Contents, iv

Controlled Subscription API, 22

Conventions

Documentation, ix

Coversheets, 16, 17

CPRS Coversheet Load Times, 15, 16

CP CODE EVALUATOR File (#8972.1), 3, 6, 8, 30

CP DATA ELEMENTS File (#8972.3), 3, 6, 8, 30

CP Echo Server Option, 18, 19, 27

CP Environment Check Option, 3, 4, 10, 11, 13, 15

CP PARAMETERS File (#8973), 3, 4, 5, 6, 8, 10, 15, 16, 17, 20, 21, 30

CP REPORTS File (#8973.3), 3, 7, 30

CP TIMING File (#8973.2), 1, 2, 3, 4, 5, 6, 8, 10, 15, 17, 20, 30

CP Tools Manager Menu, 4, 13, 14, 15, 16, 26

CP Tools Reports Menu, 13, 16

CPE

Website, xii

CPRS

Coversheet Load Times, 15, 16

Patches

OR\*3.0\*209, 26

Custodial Package Menu, 24

D

Data Dictionary

Data Dictionary Utilities Menu, xi

Listings, xi

Databases

Capacity Planning National Database, 1, 2, 10, 19, 27, 30

DBA Approvals, 24

DBA IA CUSTODIAL MENU, 24

DBA IA CUSTODIAL Option, 24

DBA IA INQUIRY Option, 24

DBA IA ISC Menu, 24, 25

DBA IA SUBSCRIBER MENU, 25

DBA IA SUBSCRIBER Option, 25

DBA Menu, 24, 25

Dependencies

Options, 26

Detailed Daily Coversheet Load Option, 13, 17

Detailed Hourly Coversheet Load Option, 13, 17

Disclaimers

Documentation, viii

Software, viii

Documentation

Conventions, ix

Symbols, ix

Documentation Disclaimer, viii

Documentation Navigation, x

E

Edit CP Parameters File Option, 13, 15

Electronic Signatures, 30

EN^KMPDSS Routine, 13

EN^KMPDTP1 Routine, 13

EN^KMPDTP2 Routine, 13

EN^KMPDTP3 Routine, 13

EN^KMPDTP4 Routine, 13

EN^KMPDTP5 Routine, 14

EN^KMPDTP6 Routine, 14

EN^KMPDTP7 Routine, 14

Eve Menu, 4, 14

Exemptions

SAC, 28

Exported Options, 13

External Relations, 23

F

Fields

CM TOOLS CURRENT VERSION (#.02), 10

MONITOR ALERT - SECONDS (#19.02), 16

MONITOR UPDATE RATE - MINUTES (#19.01), 16

SCHEDULED DOWN TIME START (#5.01), 19

SCHEDULED DOWN TIME STOP (#5.02), 19

FileMan File Protection, 30

Files, 6

CM HL7 DATA (#8973.1), 1, 2, 3, 4, 5, 6, 8, 10, 15, 17, 20, 30

CP CODE EVALUATOR (#8972.1), 3, 6, 8, 30

CP DATA ELEMENTS (#8972.3), 3, 6, 8, 30

CP PARAMETERS (#8973), 3, 4, 5, 6, 8, 10, 15, 16, 17, 20, 21, 30

CP REPORTS (#8973.3), 3, 7, 30

CP TIMING (#8973.2), 1, 2, 3, 4, 5, 6, 8, 10, 15, 17, 20, 30

RESOURCE USAGE MONITOR (#8971.1), 15

SAGG PROJECT (#8970.1), 15

Security, 30

G

Globals

Journaling, 9

KMPD, 3, 8

KMPD(8972.1 Sub-global, 6

KMPD(8972.3 Sub-global, 6

KMPD(8973 Sub-global, 6

KMPD(8973.1 Sub-global, 6

KMPD(8973.1) Sub-global, 4, 5, 17

KMPD(8973.2 Sub-global, 6

KMPD(8973.2) Sub-global, 4, 5, 17

KMPD(8973.3 Sub-global, 7

KMPTMP(”KMPDT”), 8

Protection, 9

TMP(”KMPDH”,\$J), 1, 8, 20

Translation, 9

Translation, Journaling, and Protection, 8

Glossary, 32

Intranet Website, 32

H

Help

At Prompts, xi

Online, xi

Question Marks, xi

History, Revisions to Documentation and Patches, iii

HL7 Patches

HL\*1.6\*79, 23, 26

HL7 Workload Data, 1, 2, 6

Home Pages

Acronyms Intranet Website, 32

Adobe Website, xii

Capacity Planning Projections Website, 2

Capacity Planning Statistics Website, 2, 30

CPE Website, xii

Glossary Intranet Website, 32

VA Software Document Library (VDL), xii

How to

Obtain Technical Information Online, xi

Use this Manual, viii

I

Implementation, 3

Implementation and Maintenance, 3

Inquire Option, 24

Integration Agreements, 24

Current List for CM Tools

Custodian, 24

Subscriber, 25

Detailed Information, 24

Integration Agreements Menu Option, 24, 25

Intended Audience, viii

Interfacing, 30

Internal Relations, 26

Introduction, 1

J

Journaling, 9

Globals, 8

K

Keys, 30

KMP MAIL GROUP EDIT Option, 13, 14

KMP-APMAN Mail Group, 11

KMP-CAPMAN Mail Group, 14, 29

KMPD BACKGROUND DRIVER Option, 1, 3, 4, 5, 8, 10, 15, 17, 20, 26

KMPD CM TOOLS MANAGER MENU, 4, 13, 14, 15, 16

KMPD CM TOOLS REPORTS Menu, 13, 16

KMPD ECHO Bulletin, 29

KMPD ECHO Server Option, 18, 19, 27

KMPD Global, 3, 8

KMPD MANAGER MENU, 26

KMPD PARAM EDIT Option, 13, 15

KMPD STATUS

Option, 3, 4, 10, 11, 13, 15

Template, 7

KMPD TMG AVG TTL Option, 13, 16

KMPD TMG DLY TTL DETAIL Option, 13, 17

KMPD TMG HRLY TTL DETAIL Option, 13, 17

KMPD TMG HRLY TTL Option, 13, 16

KMPD TMG HRLY TTL RT Option, 14, 17

KMPD TMG MONITOR Option, 11, 13, 15

KMPD TMG REPORTS Menu, 13, 16, 17

KMPD TMG START/STOP Option, 13, 15

KMPD TMG TTL ALERT Option, 14, 17

KMPD TMG TTL ALERT RT Option, 14, 17

KMPD(8972.1 Sub-global, 6

KMPD(8972.3 Sub-global, 6

KMPD(8973 Sub-global, 6

KMPD(8973.1 Sub-global, 6

KMPD(8973.1) Sub-global, 4, 5, 17

KMPD(8973.2 Sub-global, 6

KMPD(8973.2) Sub-global, 4, 5, 17

KMPD(8973.3 Sub-global, 7

KMPDBD01 Routine, 10, 17

KMPDECH Routine, 10, 18

KMPDHU01 Routine, 10

KMPDHU02 Routine, 10

KMPDHU03 Routine, 10

KMPDPOST Routine, 10

KMPDRDAT Routine, 10

KMPDSS Routine, 10

KMPDSS1 Routine, 10

KMPDSSD Routine, 11

KMPDSSD1 Routine, 11

KMPDSSR Routine, 11

KMPDSSS Routine, 11

KMPDTM Routine, 11, 13

KMPDTP1 Routine, 11

KMPDTP2 Routine, 11

KMPDTP3 Routine, 11

KMPDTP4 Routine, 11

KMPDTP5 Routine, 11

KMPDTP6 Routine, 11

KMPDTP7 Routine, 11

KMPDTU01 Routine, 11

KMPDTU02 Routine, 11

KMPDTU10 Routine, 11

KMPDTU11 Routine, 11

KMPDU Routine, 11

KMPDU1 Routine, 11

KMPDU11 Routine, 11

KMPDU2 Routine, 11

KMPDU3 Routine, 11

KMPDU4 Routine, 11

KMPDU5 Routine, 11

KMPDU6 Routine, 11

KMPDU7 Routine, 11

KMPDU7A Routine, 11

KMPDUG Routine, 11

KMPDUG1 Routine, 11

KMPDUG2 Routine, 11

KMPDUGV Routine, 11

KMPDUT Routine, 11

KMPDUT1 Routine, 11

KMPDUT2 Routine, 11

KMPDUT4 Routine, 11

KMPDUT4A Routine, 11

KMPDUT4B Routine, 11

KMPDUT4C Routine, 11

KMPDUT5 Routine, 11

KMPDUTL Routine, 11

KMPDUTL1 Routine, 11

KMPDUTL2 Routine, 11

KMPDUTL3 Routine, 11

KMPDUTL4 Routine, 11

KMPDUTL5 Routine, 11

KMPDUTL6 Routine, 11

KMPDUTL7 Routine, 11

KMPDUTL8 Routine, 11

KMPR BACKGROUND DRIVER Option, 15

KMPS SAGG REPORT Option, 15

KMPTMP(”KMPDT”) Global, 8

L

List File Attributes Option, xi

LIST MANAGER TEMPLATE, 7

M

Mail Groups, 29

KMP-APMAN, 11

KMP-CAPMAN, 14, 29

Maintenance, 4

Menus

Capacity Planning, 4, 13, 14

CP Tools Manager Menu, 4, 13, 14, 15, 16, 26

CP Tools Reports, 13, 16

Custodial Package Menu, 24

Data Dictionary Utilities, xi

DBA, 24, 25

DBA IA CUSTODIAL MENU, 24

DBA IA ISC, 24, 25

DBA IA SUBSCRIBER MENU, 25

DBA Option, 24, 25

Eve, 4, 14

Integration Agreements Menu, 24, 25

KMPD CM TOOLS MANAGER MENU, 4, 13, 14, 15, 16

KMPD CM TOOLS REPORTS, 13, 16

KMPD MANAGER MENU, 26

KMPD TMG REPORTS, 13, 16, 17

Operations Management, 14

Subscriber Package Menu, 25

Systems Manager Menu, 14

Taskman Management, 4, 5, 18, 26

Timing Reports, 13, 16, 17

XTCM MAIN, 4, 13, 14

XUSITEMGR, 14

XUTM MGR, 4, 5, 18, 26

MONITOR ALERT - SECONDS Field (#19.02), 16

MONITOR UPDATE RATE - MINUTES Field (#19.01), 16

Monitors

Timing, 15

VistA, 10, 15, 19, 27

N

Namespace, 3, 27

National Database

Capacity Planning, 1, 2, 10, 19, 27, 30

O

Obtaining

Data Dictionary Listings, xi

Official Policies, 31

Online

Documentation, xi

Technical Information, How to Obtain, xi

Operations Management Menu, 14

Options

ACTIVE by Custodial Package, 24

Average Daily Coversheet Load, 13, 16

Average Hourly Coversheet Load, 13, 16

Capacity Planning, 4, 13, 14

Capacity Planning Mail Group Edit, 13, 14

CM Tools Background Driver, 1, 2, 3, 4, 8, 10, 15, 17, 20, 26

CP Environment Check, 3, 4, 10, 11, 13, 15

CP Tools Manager Menu, 4, 13, 14, 15, 16, 26

CP Tools Reports, 13, 16

Custodial Package Menu, 24

Data Dictionary Utilities, xi

DBA, 24, 25

DBA IA CUSTODIAL, 24

DBA IA CUSTODIAL MENU, 24

DBA IA INQUIRY, 24

DBA IA ISC, 24, 25

DBA IA SUBSCRIBER MENU, 25

DBA IA SUBSCRIBER Option, 25

DBA Option, 24, 25

Dependencies, 26

Detailed Daily Coversheet Load, 13, 17

Detailed Hourly Coversheet Load, 13, 17

Edit CP Parameters File, 13, 15

Eve, 4, 14

Exported, 13

Server, 18

With Parents, 13

Without Parents, 17

Inquire, 24

Integration Agreements Menu, 24, 25

KMP MAIL GROUP EDIT, 13, 14

KMPD BACKGROUND DRIVER, 1, 3, 4, 5, 8, 10, 15, 17, 20, 26

KMPD CM TOOLS MANAGER MENU, 4, 13, 14, 15, 16

KMPD CM TOOLS REPORTS, 13, 16

KMPD MANAGER MENU, 26

KMPD PARAM EDIT, 13, 15

KMPD STATUS, 3, 4, 10, 11, 13, 15

KMPD TMG AVG TTL, 13, 16

KMPD TMG DLY TTL DETAIL, 13, 17

KMPD TMG HRLY TTL, 13, 16

KMPD TMG HRLY TTL DETAIL, 13, 17

KMPD TMG HRLY TTL RT, 14, 17

KMPD TMG MONITOR, 11, 13, 15

KMPD TMG REPORTS, 13, 16, 17

KMPD TMG START/STOP, 13, 15

KMPD TMG TTL ALERT, 14, 17

KMPD TMG TTL ALERT RT, 14, 17

KMPR BACKGROUND DRIVER, 15

KMPS SAGG REPORT, 15

List File Attributes, xi

Operations Management, 14

Print ACTIVE by Subscribing Package, 25

Real-Time Average Hourly Coversheet Load, 14, 17

Real-Time Threshold Alert, 14, 17

RUM Background Driver, 15

SAGG Master Background Task, 15

Schedule/Unschedule Options, 4, 5, 18, 26

Server, 18

CP Echo Server, 18, 19, 27

KMPD ECHO, 18, 19, 27

Single, Without Parents, 17

Start/Stop Timing Collection, 13, 15

Subscriber Package Menu, 25

Systems Manager Menu, 14

Taskman Management, 4, 5, 18, 26

Threshold Alert, 14, 17

Timing Monitor, 11, 13, 15

Timing Reports, 13, 16, 17

With Parents, 13

Without Parents, 17

XTCM MAIN, 4, 13, 14

XUSITEMGR, 14

XUTM MGR, 4, 5, 18, 26

XUTM SCHEDULE, 4, 5, 18, 26

Orientation, viii

P

Parameters

Purge HL7 Data After, 1, 4, 5, 10, 17, 20

Purge Timing Data After, 1, 4, 5, 10, 17, 20

Patches

HL\*1.6\*79, 23, 26

OR\*3.0\*209, 26

Revisions, iii

Policies, Official, 31

Print ACTIVE by Subscribing Package Option, 25

PRM^KMPDSS Routine, 13

Protection, 9

Globals, 8

Protocols, 19

PS Anonymous Directories, xii

Purge HL7 Data After Parameter, 1, 4, 5, 10, 17, 20

Purge Timing Data After Parameter, 1, 4, 5, 10, 17, 20

Purging, 20

Q

Question Mark Help, xi

R

Real-Time Average Hourly Coversheet Load Option, 14, 17

Real-Time Threshold Alert Option, 14, 17

Reference Materials, xii

Relations

CPRS GUI 23.0 and OE/RR 3.0, 26

External, 23

Internal, 26

VistA, 26

VistA HL7 1.6, 26

Remote Systems, 30

RESOURCE USAGE MONITOR File (#8971.1), 15

Revision History, iii

Patches, iii

Routines

Callable, 22

Controlled Subscription API, 22

EN^KMPDSS, 13

EN^KMPDTP1, 13

EN^KMPDTP2, 13

EN^KMPDTP3, 13

EN^KMPDTP4, 13

EN^KMPDTP5, 14

EN^KMPDTP6, 14

EN^KMPDTP7, 14

KMPDBD01, 10, 17

KMPDECH, 10, 18

KMPDHU01, 10

KMPDHU02, 10

KMPDHU03, 10

KMPDPOST, 10

KMPDRDAT, 10

KMPDSS, 10

KMPDSS1, 10

KMPDSSD, 11

KMPDSSD1, 11

KMPDSSR, 11

KMPDSSS, 11

KMPDTM, 11

KMPDTM, 13

KMPDTP1, 11

KMPDTP2, 11

KMPDTP3, 11

KMPDTP4, 11

KMPDTP5, 11

KMPDTP6, 11

KMPDTP7, 11

KMPDTU01, 11

KMPDTU02, 11

KMPDTU10, 11

KMPDTU11, 11

KMPDU, 11

KMPDU1, 11

KMPDU11, 11

KMPDU2, 11

KMPDU3, 11

KMPDU4, 11

KMPDU5, 11

KMPDU6, 11

KMPDU7, 11

KMPDU7A, 11

KMPDUG, 11

KMPDUG1, 11

KMPDUG2, 11

KMPDUGV, 11

KMPDUT, 11

KMPDUT1, 11

KMPDUT2, 11

KMPDUT4, 11

KMPDUT4A, 11

KMPDUT4B, 11

KMPDUT4C, 11

KMPDUT5, 11

KMPDUTL, 11

KMPDUTL1, 11

KMPDUTL2, 11

KMPDUTL3, 11

KMPDUTL4, 11

KMPDUTL5, 11

KMPDUTL6, 11

KMPDUTL7, 11

KMPDUTL8, 11

List, 10

PRM^KMPDSS, 13

SST^KMPDSS, 13

RUM Background Driver Option, 15

S

SAC Exemptions, 28

SAGG Master Background Task Option, 15

SAGG PROJECT File (#8970.1), 15

Schedule/Unschedule Options Option, 4, 5, 18, 26

SCHEDULED DOWN TIME START Field (#5.01), 19

SCHEDULED DOWN TIME STOP Field (#5.02), 19

Security, 29

Files, 30

Keys, 30

Management, 29

Server Options, 18

CP Echo Server, 18, 19, 27

KMPD ECHO, 18, 19, 27

Signatures, Electronic, 30

Single Options, Without Parents, 17

Software Disclaimer, viii

Software Product Security, 29

Software-wide and Key Variables, 28

SST^KMPDSS Routine, 13

Start/Stop Timing Collection Option, 13, 15

Startup/Stop Process

CM Tools, 15

Subscriber Package Menu Option, 25

Symbols

Found in the Documentation, ix

Systems Manager Menu, 14

T

Tables, vii

Taskman Management Menu, 4, 5, 18, 26

Templates, 7

KMPD STATUS, 7

LIST MANAGER TEMPLATE, 7

Threshold Alert Option, 14, 17

Time-To-Load Values, 16, 17

Timing Monitor, 15

Timing Monitor Option, 11, 13, 15

Timing Reports Menu, 13, 16, 17

TMP(”KMPDH”,\$J) Global, 1, 8, 20

Translation, 9

Globals, 8

U

URLs

Acronyms Intranet Website, 32

Adobe Website, xii

CPE Website, xii

Glossary Intranet Website, 32

VA Software Document Library (VDL), xii

V

VA FileMan File Protection, 30

VA Software Document Library (VDL)

Website, xii

Variables

Key, 28

Software-wide, 28

Vista Monitor, 10, 15, 19, 27

VistA Software Requirements, 23

W

Web Pages

Capacity Planning

Projections Website, 2

Statistics Website, 2, 30

Websites

Acronyms Intranet Website, 32

Adobe Website, xii

CPE, xii

Glossary Intranet Website, 32

VA Software Document Library (VDL), xii

Workload

Trends, 2

VistA HL7, 1, 2, 6

X

XTCM MAIN Menu, 4, 13, 14

XUSITEMGR Menu, 14

XUTM MGR Menu, 4, 5, 18, 26

XUTM SCHEDULE Option, 4, 5, 18, 26