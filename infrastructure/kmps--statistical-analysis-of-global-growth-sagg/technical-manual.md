---
title: SAGG Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: KMPS
app_name: Statistical Analysis of Global Growth (SAGG)
section: INF
app_status: active
pkg_ns: KMPS
patch_ver: 2
patch_id: KMPS*2
group_key: "KMPS:KMPS:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - sagg
  - table
  - software
  - contents
  - kmps
  - global
  - span
  - class
  - manual
  - version
page_count: 0
word_count: 5196
section_count: 16
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Stat_Analysis_Global_Growth_(SAGG)/kmps2_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Stat_Analysis_Global_Growth_(SAGG)/kmps2_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=115"
---

---
title: |
  Statistical Analysis of Global Growth (SAGG) 2.0

  Technical Manual
---

![](sagg-version-2-technical-manual/001.png)

December 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Systems Engineering (ESE)

Capacity and Performance Engineering (CPE)

<span id="_Toc56819127" class="anchor"></span>

Revision History

Documentation Revisions

<u>Table 1</u> displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<caption><p><span id="_Ref439237473" class="anchor"></span>Table 1. Documentation revision history</p></caption>
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
<td>12/30/2015</td>
<td>4.1</td>
<td><p>Updated document based on Statistical Analysis of Global Growth *SAGG) updates based on Kernel Patch XU*8.0*568.</p>
<p>Software: <strong>SAGG 2.0</strong>.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/--/2015</td>
<td>4.0</td>
<td><p>This patch enables SAGG to run on Linux based systems. It also does <em>not</em> collect metrics on all volume sets.</p>
<p>Software: <strong>SAGG 2.0</strong>.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/--/2007</td>
<td>3.0</td>
<td><p>Patch SAGG v2.0 updates the SAGG PROJECT package to version 2.0. This version removes support for DSM/MSM and now uses API's from the CM TOOLS package that are <em>not</em> SAGG specific. The only operating systems now supported are Cache for Windows and Cache for VMS. Other documentation updates:</p>
<p>The KMPS-SAGG mail group is no longer in use. The KMP-CAPMAN is now used for all notifications.</p>
<p>There are no new options, and they all work the same except for [KMPS SAGG STATUS]. This option now uses ListManager to the display is different.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/--/2005</td>
<td>2.0</td>
<td><p>Reformatted document to follow current ISS standards.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
<p>Patient or user names are formatted as follows: KMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/--/1998</td>
<td>1.0</td>
<td>Initial Statistical Analysis of Global Growth (SAGG) 1.8 software documentation creation.</td>
<td>SAGG Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref439237473" class="anchor"></span>Table 1. Documentation revision history

Patch Revisions

For a complete list of patches related to this software, see the Patch Module on FORUM.

Contents

<span id="_Toc439250745" class="anchor"></span>Tables and Figures

Figures

[Figure 1. SAGG Project Manager Menu options [7](#_Toc439250784)](#_Toc439250784)

Tables

<span id="_Toc439236019" class="anchor"></span>

Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use and implementation of the Statistical Analysis of Global Growth (SAGG) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

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

![](sagg-version-2-technical-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 2</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](sagg-version-2-technical-manual/003.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](sagg-version-2-technical-manual/004.png) | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref345831418" class="anchor"></span>Table 2. Documentation symbol/term descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*“ is defined in the Approved Application Abbreviations document and “\<*N*\>“ represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in SAGG (KMPS) test patient and user names would be documented as follows:

- KMPSPATIENT,ONE or KMPSUSER,ONE
- KMPSPATIENT,TWO or KMPSUSER,TWO
- KMPSPATIENT,THREE or KMPSUSER,THREE
- KMPSPATIENT,14 or KMPSUSER,14
- Etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and can be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](sagg-version-2-technical-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](sagg-version-2-technical-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

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

![](sagg-version-2-technical-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](sagg-version-2-technical-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](sagg-version-2-technical-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about the Statistical Analysis of Global Growth (SAGG) software should consult the following:

- *Statistical Analysis of Global Growth (SAGG) Installation Guide*
- *Statistical Analysis of Global Growth (SAGG) User Manual*
- *Statistical Analysis of Global Growth (SAGG) Technical Manual* (this manual)
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](sagg-version-2-technical-manual/010.png) REF: See the [Statistical Analysis of Global Growth (SAGG) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=115).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation and System Requirements](#implementation-and-system-requirements)
    - [Software Dependencies](#software-dependencies)
    - [Upgrading from a Previous Version of SAGG Related to Patch XU\8.0\456](#upgrading-from-a-previous-version-of-sagg-related-to-patch-xu80456)
    - [Virgin Installations of SAGG Related to Patch XU\8.0\456](#virgin-installations-of-sagg-related-to-patch-xu80456)
    - [Namespace](#namespace)
  - [Maintenance](#maintenance)
- [Globals](#globals)
  - [Files](#files)
  - [Templates](#templates)
- [Routines](#routines)
- [Key Variables](#key-variables)
- [Exported Options](#exported-options)
  - [SAGG Project Manager Menu](#sagg-project-manager-menu)
    - [Stop SAGG Collection Option](#stop-sagg-collection-option)
    - [Check SAGG Environment Option](#check-sagg-environment-option)
  - [Options Without Parents](#options-without-parents)
    - [SAGG Master Background Task Option](#sagg-master-background-task-option)
  - [Menu/Option Assignment](#menuoption-assignment)
  - [Protocols](#protocols)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
  - [DBA Approvals and Database Integration Agreements](#dba-approvals-and-database-integration-agreements)
- [Internal Relations](#internal-relations)
  - [Relationship of SAGG Software with Kernel](#relationship-of-sagg-software-with-kernel)
  - [Namespace](#namespace-1)
- [Software-wide Variables](#software-wide-variables)
- [SAC Exemptions](#sac-exemptions)
- [Security](#security)
  - [Keys](#keys)
  - [VA FileMan File Protection](#va-fileman-file-protection)
This distribution contains the Statistical Analysis of Global Growth (SAGG) 2.0 software. This version of the software can be installed over any previous versions of SAGG without any adverse problems. The current version of the software is compatible with all current operating system platforms at the medical centers and has minimal impact on the Information Resource Management (IRM) support staff. This software operates on Caché for Windows and Caché for VMS system platforms.
The Veterans Health Administration (VHA) developed the Statistical Analysis of Global Growth (SAGG) software in order to obtain more accurate information regarding the current and future Veterans Health Information Systems and Technology Architecture (VistA) database growth rates at the VA Medical Centers (VAMCs).
SAGG is a fully automated support tool developed by the Capacity Planning (CP) team, which entails the monthly capture of global database, software, and file size information from participating sites.
Installing the SAGG software creates the collection process mechanism and other necessary components of the software. The fully automated data collection cycle entails capturing all production global, software, and file specifics at the site into a temporary ^XTMP("KMPS") collection global. Once collected, the information is converted into an electronic mail message that is automatically transferred via network mail and merged into a CP National Database. The temporary collection global is then deleted from the site's system. The site also receives a summary of the global statistical data in the form of an electronic turn-around message.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the initial setup procedures are performed as detailed in the patch description for KMPS\*2\*0, the collection process basically operates transparent to IRM with minimal impact on system resources. The software uses the Kernel supplied TaskMan utility to schedule the initial global collection cycle, and it is then rescheduled to capture on a regular monthly basis. The monthly time frame for data accumulation was chosen in order to enhance global, software, and file trend analysis.

## Implementation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This distribution of the original Statistical Analysis of Global Growth (SAGG) software Version 2.0, Patch KMPS\*2\*0, was dependent on Patches KMPD\*2.0\*6 and XU\*8.0\*456. Patch KMPS\*2\*0 is a Kernel Installation and Distribution System (KIDS) software release. SAGG Installation Instructions can be found in the description for Patch KMPS\*2\*0, located on the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FOURM.

### Upgrading from a Previous Version of SAGG Related to Patch XU\*8.0\*456

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](sagg-version-2-technical-manual/011.png) CAUTION: If your site is upgrading from a previous version of SAGG, Patch XU\*8.0\*456 *must* be installed for SAGG 2.0 to work with Caché 5.2.

### Virgin Installations of SAGG Related to Patch XU\*8.0\*456

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](sagg-version-2-technical-manual/012.png) CAUTION: If your site is installing SAGG for the first time, Patch XU\*8.0\*456 *must* be installed for the SAGG Master Background Task Option \[KMPS SAGG REPORT\] to work.

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) has been given the KMP\* namespace for both routines and globals. The SAGG software uses the KMPS namespace for its routines and global.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information throughout this manual is meant to help IRM in the maintenance of the software. The discussion that follows covers the options available to assist IRM in that maintenance.

The SAGG software monitors *all* volume sets.

The SAGG software uses the KMP-CAPMAN mail group for distribution of reports and error messages.

The accuracy of the global information from the site is dependent on the SAGG Master Background Task option \[KMPS SAGG REPORT\] running every 28 days. IRM staff should ensure that the background task is scheduled to run by reviewing the Check SAGG Environment option \[KMPS SAGG STATUS\]. If necessary, the background task can be rescheduled with the Schedule/Unschedule Options option \[XUTM SCHEDULE\] located under the Taskman Management menu.

# Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the SAGG 2.0 software globals:

<table>
<caption><p><span id="_Ref439248500" class="anchor"></span>Table 3. SAGG global information</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Global</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPS</td>
<td><p>This global contains data for the SAGG PROJECT file (#8970.1).</p>
<p>This global only contains the SAGG PROJECT file (#8970.1) and is minimal in size. Therefore, this global does <em>not</em> grow large.</p>
<p>The global should be journaled and translated, if the operating system supports these functions.</p>
<p><strong>Journaling:</strong> Mandatory.</p></td>
</tr>
<tr class="even">
<td>XTMP("KMPS")</td>
<td><p>The ^XTMP global is the storage location for inter-process temporary data. The SAGG software uses the ^XTMP("KMPS") sub-node to temporarily store global, software, and file data during the collection cycle. The contents of this sub-node are deleted after completion of the collection cycle.</p>
<p><strong>Per <em>Kernel V. 8.0 Technical Manual</em>:</strong> The ^XTMP global should <em>not</em> be journaled. However, the ^XTMP global should be translated, if the operating system supports this function.</p>
<p><strong>Journaling:</strong> <em>Not</em> recommended.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref439248500" class="anchor"></span>Table 3. SAGG global information

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the SAGG 2.0 software files:

<table>
<caption><p><span id="_Ref439248429" class="anchor"></span>Table 4. SAGG file list</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 45%" />
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
<td>8970.1</td>
<td>SAGG PROJECT</td>
<td>^KMPS(8970.1</td>
<td><p>This file contains the location information for the temporary ^XTMP global and the names of all production volume sets on the system.</p>
<p>No data comes with the file.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref439248429" class="anchor"></span>Table 4. SAGG file list

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* contain any templates.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> lists the SAGG 2.0 software routines:

<table>
<caption><p><span id="_Ref439248323" class="anchor"></span>Table 5. SAGG routine list</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPSGE</td>
<td><p>Master collection routine that is invoked through the TaskMan scheduling options. This routine coordinates the collection of global, software, and file data; then, it sends the collected data to the Capacity Planning (CP) National Database.</p>
<p>![](sagg-version-2-technical-manual/013.png) <strong>NOTE:</strong> This routine has been updated to be compatible with Caché 5.2.</p></td>
</tr>
<tr class="even">
<td>KMPSLK</td>
<td><p>Routine that permits the capture of specific VistA software and file data including system configuration information.</p>
<p>![](sagg-version-2-technical-manual/014.png) <strong>NOTE:</strong> This routine has been updated to be compatible with Caché 5.2.</p></td>
</tr>
<tr class="odd">
<td>KMPSUTL</td>
<td><p>A utility routine that provides several management functions.</p>
<p>![](sagg-version-2-technical-manual/015.png) <strong>NOTE:</strong> This routine has been updated to be compatible with Caché 5.2.</p></td>
</tr>
<tr class="even">
<td>KMPSUTL1</td>
<td><p>A utility routine that provides several management functions.</p>
<p>![](sagg-version-2-technical-manual/016.png) <strong>NOTE:</strong> This routine has been updated to be compatible with Caché 5.2.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref439248323" class="anchor"></span>Table 5. SAGG routine list

# Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the SAGG 2.0 software key variables:

| Name     | Description                                                                  |
|----------|------------------------------------------------------------------------------|
| KMPSMGR  | The name of the MGR UCI as determined by the ^%ZOSF("MGR") variable.         |
| KMPSPROD | The name of the Production UCI as determined by the ^%ZOSF("PROD") variable. |
| KMPSSITE | The station number of the site as determined by \$P(\$\$SITE^VASITE(),U,3).  |
| KMPSX1   | The type of M platform as determined by the ^%ZOSF("OS") variable.           |
| NUM      | The current date in M internal format as given by the +\$H system variable.  |

<span id="_Ref439248036" class="anchor"></span>Table 6. SAGG key variables

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## SAGG Project Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KMPS SAGG MANAGER menu \[KMPS SAGG MANAGER\] is located under the Capacity Planning menu \[XTCM MAIN\]. The XTCM MAIN menu can be assigned to the IRM staff members who support this software and other capacity planning tasks. The SAGG Project Manager Menu contains the following options:

<span id="_Toc439250784" class="anchor"></span>Figure 1. SAGG Project Manager Menu options

SAGG Project Manager Menu \[KMPS SAGG MANAGER\]

Check SAGG Environment \[KMPS SAGG STATUS\]

Stop SAGG Collection \[KMPS SAGG STOP\]

### Stop SAGG Collection Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop SAGG Collection option \[KMPS SAGG STOP\] informs the SAGG software collection routines to begin an orderly shutdown process. Each collection routine stops after reaching an appropriate break point.

### Check SAGG Environment Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Check SAGG Environment option \[KMPS SAGG STATUS\] checks the environment of the SAGG (Statistical analysis of Global Growth) Project. In addition to providing information regarding the SAGG collection routines, this option checks the status of SAGG patch installation at the site.

## Options *Without* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following option does *not* appear on any menu:

### SAGG Master Background Task Option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG Master Background Task option \[KMPS SAGG REPORT\] is *not* assigned to any menu. This option is scheduled through TaskMan to start the SAGG software's master collection routine in the background. This option should be rescheduled with the Schedule/Unschedule Options option \[XUTM SCHEDULE\] under the Taskman Management menu for every 28 days to ensure same day-of-week collection cycles. If this option does *not* execute properly, a warning message is sent to the KMP-CAPMAN mail group.

## Menu/Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KMPS SAGG MANAGER menu is located under the Capacity Planning menu \[XTCM MAIN\]. The XTCM MAIN menu can be assigned to the IRM staff members who support this software and other capacity planning tasks.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* export any protocols.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software contains the SAGG PROJECT file (#8970.1). This file is minimal in size and does *not* experience any growth. Since the SAGG software maintains minimal data at the site, archiving functions are *not* necessary and are *not* provided.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software contains the SAGG PROJECT file (#8970.1). This file is minimal in size and does *not* experience any growth. Global data information is accumulated into the ^XTMP("KMPS") global and is killed after uploading to a mail message, which is forwarded to the Capacity Planning (CP) National Database. Since the SAGG software maintains minimal data at the site, purging functions are *not* necessary and are *not* provided.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* provide any callable entry points that are available for general use.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software relies on the following external VistA software to run effectively:

| Software   | Minimum Version Needed | Patch Information |
|------------|------------------------|-------------------|
| Kernel     | 8.0                    | Fully patched     |
| VA FileMan | 22.0 (or higher)       | Fully patched     |
| MailMan    | 7.1 (or higher)        | Fully patched     |

<span id="_Toc439250791" class="anchor"></span>Table 7. SAGG-required VistA software

SAGG 2.0 uses Kernel %ZOSVKS-namespaced routines that use system specific calls. The Kernel %ZOSVKS-namespaced routines were introduced with the issuance of Kernel Patch XU\*8.0\*90.

All operating system interfaces on which the SAGG software is dependent have been encapsulated into the Kernel %ZOSVKS-namespaced routines. The %ZOSVKS\* routines contain code that enables use of the VIEW command and \$VIEW function to get information from the operating system.

## DBA Approvals and Database Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Database Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are *not* available to the general programming public.

The SAGG 2.0 software is *not* dependent on any agreements.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All options in the SAGG 2.0 software under the SAGG Project Manager Menu \[KMPS SAGG MANAGER\] can function independently. Only the Schedule/Unschedule Options option \[XUTM SCHEDULE\] under the Taskman Management menu can invoke the SAGG Master Background Task option \[KMPS SAGG REPORT\].

## Relationship of SAGG Software with Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAGG 2.0 uses Kernel %ZOSVKS-namespaced routines that use system specific calls. The Kernel %ZOSVKS-namespaced routines were introduced with the issuance of Kernel Patch XU\*8.0\*90.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software has been assigned the KMPS namespace.

Additionally, this version of SAGG uses Kernel %ZOSVKS-namespaced routines that use system-specific calls. The Kernel %ZOSVKS-namespaced routines were introduced with the issuance of Kernel Patch XU\*8.0\*90.

# Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* employ the use of any software-wide variables.

![](sagg-version-2-technical-manual/017.png) REF: For the key variables that are employed within this software, see the “<u>Key Variables</u>” section.

# SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* employ any exemptions from the Programming Standards and Conventions (SAC). Also, SAGG 2.0 uses Kernel %ZOSVKS-namespaced routines that use system-specific calls. The Kernel %ZOSVKS-namespaced routines were introduced with the issuance of Kernel Patch XU\*8.0\*90.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG 2.0 software does *not* distribute any security keys.

## VA FileMan File Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> describes the VA FileMan file protection for the SAGG 2.0 software.

| \#     | Name         | DD    | RD  | WR  | DEL | LAYGO |
|--------|--------------|-------|-----|-----|-----|-------|
| 8970.1 | SAGG PROJECT | @ |     |     |     |       |

<span id="_Ref439247776" class="anchor"></span>Table 8. SAGG file protection

<span id="_Toc423486600" class="anchor"></span>

Glossary

| Term                | Description                                                                                                                                                                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BLOCK               | A unit of measure of the size of the disk used by both the operating system and M platforms.                                                                                                                                                                                 |
| CAPACITY PLANNING   | The process of assessing a system's capacity and evaluating its efficiency relative to workload in an attempt to optimize system performance.                                                                                                                                |
| COLLECTION CYCLE    | Occurs when the SAGG background task begins obtaining data regarding the size and efficiency of the globals on the monitored volume sets. Additionally, software and file information is collected. Normally, a site should schedule the collection cycle for every 28 days. |
| COMPLEXITY LEVEL    | A ranking order for sites based on calculated workload needs. Four levels exist with 1 being the largest and 4 being the smallest type facility.                                                                                                                             |
| DATA BLOCK          | A component of the global tree-structure that is used by the M platform to contain the actual information.                                                                                                                                                                   |
| DATABASE            | A set of information, consisting of at least one file, which is specific for a given purpose. The VistA database is composed of a number of VA FileMan files.                                                                                                                |
| DISK MODEL RANK     | A ranking order for sites based on calculated disk capacity needs.                                                                                                                                                                                                           |
| GLOBAL              | Tree-structured system of nodes containing common data. M platforms store data on the disk in the form of global arrays. A global is composed of both pointer and data blocks.                                                                                               |
| GLOBAL EFFICIENCY   | Determines the amount of space used within the entire block structure of a particular global. A higher efficiency indicates that the global is compacted and, therefore, using less disk space.                                                                              |
| GLOBAL SIZE         | Determines the amount of pointer and data blocks used by a particular global.                                                                                                                                                                                                |
| MAP                 | Composed of subunits called blocks. A map consists of 400 blocks.                                                                                                                                                                                                            |
| MODEL RANK          | A ranking order for sites based on calculated VistA workload needs.                                                                                                                                                                                                          |
| POINTER BLOCK       | A component of the global tree-structure that is used by the M platform to find the location of data blocks.                                                                                                                                                                 |
| SAGG                | Statistical Analysis of Global Growth. A fully automated support tool developed by the Capacity Planning (CP) team, which entails the monthly capture of global, database, software, and file size information from participating sites.                                     |
| SESSION NUMBER      | Timestamp of when the collection cycle was run. The session number is defined from the +\$H system variable.                                                                                                                                                                 |
| TURN-AROUND MESSAGE | The mail message that is returned to the KMP-CAPMAN mail group detailing the database and global growth over the previous reported session.                                                                                                                                  |
| ZEROTH NODE         | The number of file entries is stored within the zeroth node of VistA software files. This information is used to determine software file growth statistics.                                                                                                                  |

<span id="_Toc439250793" class="anchor"></span>Table 9. Statistical Analysis of Global Growth (SAGG) glossary terms

![](sagg-version-2-technical-manual/018.png) REF: For a list of commonly used terms and definitions, see the OI&T Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

<span id="_Toc439250783" class="anchor"></span>Index

\$

\$VIEW Function, 9

%

%ZOSF("MGR") Variable, 6

%ZOSF("OS") Variable, 6

%ZOSF("PROD") Variable, 6

%ZOSVKS Routines, 9, 10

\+

+\$H System Variable, 6

A

Acronyms

Intranet Website, 13

Archiving, 8

Assignment

Menus/Options, 7

Assumptions, x

C

Callable Routines, 8

Callout Boxes, ix

Capacity Planning Menu, 7

Check SAGG Environment option, 7

Commands

VIEW, 9

Contents, iv

Conventions

Documentation, viii

CPE

Website, x

D

Data Dictionary

Data Dictionary Utilities Menu, x

Listings, x

DBA Approvals and Database Integration Agreements, 9

Disclaimers

Documentation, vii

Software, vii

Documentation

Conventions, viii

Revisions, ii

Symbols, viii

Documentation Disclaimer, vii

Documentation Navigation, ix

E

Exemptions

SAC, 10

Exported Options, 7

External Relations, 9

F

Figures and Tables, vi

Files, 4

Protection, 11

SAGG PROJECT (#8970.1), 4, 8, 11

Functions

\$VIEW, 9

G

Globals, 4

KMPS Global, 4

XTMP, 4

XTMP("KMPS"), 1, 4, 8

Glossary, 12

Intranet Website, 13

H

Help

At Prompts, x

Online, x

Question Marks, x

History

Revisions, ii

Home Pages

Acronyms Intranet Website, 13

Adobe Website, xi

CPE Website, x

Glossary Intranet Website, 13

VA Software Document Library (VDL), xi

How to

Obtain Technical Information Online, x

Use this Manual, vii

I

Implementation, 2

installation of SAGG

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

upgrading from previous version, 2

Virgin, 2

Integration Agreements, 9

Intended Audience, vii

Internal Relations, 10

Introduction, 1

J

Journaling, 4

K

Key Variables, 6

Keys, 11

KMP-CAPMAN Mail Group, 12

KMP-CAPMANMail Group, 2, 7

KMPD\*2.0\*6, 2

KMPS Global, 4

KMPS Namespace, 10

KMPS SAGG MANAGER Menu, 7, 10

KMPS SAGG REPORT Option, 2, 7, 10

KMPS SAGG STATUS Option, 2, 7

KMPS SAGG STOP Option, 7

KMPS\*2\*0, 2

KMPSGE Routine, 5

KMPSLK Routine, 5

KMPSMGR Variable, 6

KMPSPROD Variable, 6

KMPSSITE Variable, 6

KMPSUTL Routine, 5

KMPSUTL1 Routine, 5

KMPSX1 Variable, 6

L

List File Attributes Option, x

M

Mail Groups

KMPS-SAGG, 2, 7

Maintenance, 2

Menus

Assignment, 7

Capacity Planning, 7

Data Dictionary Utilities, x

KMPS SAGG MANAGER, 7, 10

SAGG Project Manager Menu, 7, 10

Taskman Management, 3, 7, 10

XTCM MAIN, 7

N

Namespace, 2, 10

KMPS, 10

NUM Variable, 6

O

Obtaining

Data Dictionary Listings, x

Online

Documentation, x

Technical Information, How to Obtain, x

Options

Assignment, 7

Capacity Planning, 7

Check SAGG Environment, 7

Data Dictionary Utilities, x

Exported, 7

KMPS SAGG MANAGER, 7, 10

KMPS SAGG REPORT, 2, 7, 10

KMPS SAGG STATUS, 2, 7

KMPS SAGG STOP, 7

List File Attributes, x

SAGG Master Background Task, 2, 7, 10

SAGG Project Manager Menu, 7, 10

Schedule/Unschedule Options, 3, 7, 10

Status of SAGG Collection Routines, 2

Stop SAGG Collection, 7

Taskman Management, 3, 7, 10

Without Parents, 7

XTCM MAIN, 7

XUTM SCHEDULE, 3, 7, 10

Orientation, vii

P

Patch KMPD\*2.0\*6, 2

Patch KMPS\*2\*0, 2

Patch XU\*8.0\*456, 2

Patches

Revisions, iii

Protocols, 7

PS Anonymous Directories, xi

Purging, 8

Q

Question Mark Help, x

R

Reference Materials, x

Relations

External, 9

Internal, 10

Relationship of SAGG Software with Kernel, 10

Revision History, ii

Documentation, ii

Patches, iii

Routines, 5

%ZOSVKS, 9, 10

KMPSGE, 5

KMPSLK, 5

KMPSUTL, 5

KMPSUTL1, 5

S

SAC Exemptions, 10

SAGG Master Background Task Option, 2, 7, 10

SAGG PROJECT File (#8970.1), 4, 8, 11

SAGG Project Manager Menu, 7, 10

Schedule/Unschedule Options Option, 3, 7, 10

Security, 11

File Protection, 11

Keys, 11

Software Disclaimer, vii

Software-wide Variables, 10

Status of SAGG Collection Routines Option, 2

Stop SAGG Collection Option, 7

Symbols

Found in the Documentation, viii

System Requirements, 2

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

upgrading from previous version, 2

Virgin installation, 2

T

Tables and Figures, vi

Taskman Management Menu, 3, 7, 10

Templates, 4

U

upgrading from a previous version of SAGG, 2

URLs

Acronyms Intranet Website, 13

Adobe Website, xi

CPE Website, x

Glossary Intranet Website, 13

VA Software Document Library (VDL), xi

V

VA FileMan File Protection, 11

VA Software Document Library (VDL)

Website, xi

Variables

^%ZOSF("MGR"), 6

^%ZOSF("OS"), 6

^%ZOSF("PROD"), 6

+\$H System Variable, 6

Key, 6

KMPSMGR, 6

KMPSPROD, 6

KMPSSITE, 6

KMPSX1, 6

NUM, 6

Software-wide, 10

VIEW Command, 9

Virgin installations of SAGG, 2

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

W

Websites

Acronyms Intranet Website, 13

Adobe Website, xi

CPE, x

Glossary Intranet Website, 13

VA Software Document Library (VDL), xi

X

XTCM MAIN Menu, 7

XTMP Global, 4

XTMP("KMPS") Global, 1, 4, 8

XU\*8.0\*456, 2

XUTM SCHEDULE Option, 3, 7, 10