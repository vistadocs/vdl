---
title: SAGG Version 2 User Manual
doc_type: UM
doc_label: User Manual
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
  - software
  - span
  - kmps
  - table
  - global
  - class
  - manual
  - collection
  - contents
page_count: 0
word_count: 4162
section_count: 6
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Stat_Analysis_Global_Growth_(SAGG)/kmps2_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Stat_Analysis_Global_Growth_(SAGG)/kmps2_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=115"
---

---
title: |
  Statistical Analysis of Global Growth (SAGG) 2.0

  User Manual
---

![](sagg-version-2-user-manual/001.png)

December 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Systems Engineering (ESE)

Capacity and Performance Engineering (CPE)

#### <span id="_Toc56819127" class="anchor"></span>Revision History

Documentation Revisions

<u>Table 1</u> displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<caption><p><span id="_Ref439227578" class="anchor"></span>Table . Documentation revision history</p></caption>
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
<td><p>Patch SAGG 2.0 updates the SAGG PROJECT package to Version 2.0. This version removes support for DSM/MSM and now uses APIs from the CM TOOLS package, which are <em>not</em> SAGG specific. The only operating systems now supported are Cache for Windows and Cache for VMS. Other documentation updates:</p>
<ul>
<li><p>The KMPS-SAGG mail group is no longer in use. The KMP-CAPMAN is now used for all notifications.</p></li>
<li><p>There are no new options, and they all work the same except for [KMPS SAGG STATUS]. This option now uses ListManager to the display is different.</p></li>
</ul>
<p>Software: <strong>SAGG 2.0</strong>.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/--/2005</td>
<td>2.0</td>
<td><p>Reformatted document to follow current ISS standards.</p>
<p>Reviewed document and edited for the “Data Scrubbing” and the “PDF 508 Compliance” projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with “000” or “666.”</p>
<p>Patient or user names are formatted as follows: KMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/--/1998</td>
<td>1.0</td>
<td>Initial Statistical Analysis of Global Growth (SAGG) 1.8 software documentation creation.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Ref439227578" class="anchor"></span>Table . Documentation revision history

Patch Revisions

For a complete list of patches related to this software, see the Patch Module on FORUM.

Contents

<span id="_Toc439236018" class="anchor"></span>Figures and Tables

Figures

Tables

<span id="_Toc439236019" class="anchor"></span>Orientation

How to Use this Manual

The purpose of this manual is to provide information about the Statistical Analysis of Global Growth (SAGG) 2.0 software. This manual defines the use of this software as a resource to Information Resource Management (IRM) staff responsible for capacity management functions at the site. It also highlights the use of the options that are available both locally at the site and nationally on FORUM.

Throughout this manual, advice and instructions are offered regarding the use of the Statistical Analysis of Global Growth (SAGG) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

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

![](sagg-version-2-user-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 2</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](sagg-version-2-user-manual/003.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](sagg-version-2-user-manual/004.png) | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref345831418" class="anchor"></span>Table . Documentation symbol/term descriptions

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
- References to “\<Enter\>“ within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](sagg-version-2-user-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](sagg-version-2-user-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

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

![](sagg-version-2-user-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](sagg-version-2-user-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](sagg-version-2-user-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

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
- *Statistical Analysis of Global Growth (SAGG) User Manual* (this manual)
- *Statistical Analysis of Global Growth (SAGG) Technical Manual*
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](sagg-version-2-user-manual/010.png) REF: See the [Statistical Analysis of Global Growth (SAGG) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=115).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Functional Description and Use of Software](#functional-description-and-use-of-software)
  - [System Requirements](#system-requirements)
    - [Software Dependencies](#software-dependencies)
    - [Upgrading from a Previous Version of SAGG Related to Patch XU\8.0\456](#upgrading-from-a-previous-version-of-sagg-related-to-patch-xu80456)
    - [Virgin Installations of SAGG Related to Patch XU\8.0\456](#virgin-installations-of-sagg-related-to-patch-xu80456)
  - [Software Management](#software-management)
- [# SAGG Project Manager Menu](#sagg-project-manager-menu)
  - [Check SAGG Environment Option](#check-sagg-environment-option)
  - [Stop SAGG Collection Option](#stop-sagg-collection-option)
  - [SAGG Master Background Task Option](#sagg-master-background-task-option)
- [<span id="Toc439236032" class="anchor"></span>Index](#span-idtoc439236032-classanchorspanindex)
The Office of Information and Technology (OI&T) developed the Statistical Analysis of Global Growth (SAGG) software in order to obtain more accurate information regarding the current and future Veterans Health Information Systems and Technology Architecture (VistA) database growth rates at the VA Medical Centers (VAMCs).
The Statistical Analysis of Global Growth (SAGG) software is intended to be used by Information Resource Management (IRM) staff responsible for the capacity management functions at their facility. The SAGG software allows the facility to review database, software, and file size information.
The SAGG software is strongly dependent on the site to schedule and run the collection task on a regular basis. Menus and options are provided locally at the site to allow IRM staff to accomplish and monitor this task.
The collection task obtains information on the production global, software, and file information from the site and automatically transfers this data via network mail to the Capacity Planning (CP) National Database.
The information in the CP National Database is fully accessible by all sites through the national FORUM system. Menus and options are provided nationally giving the site the ability to review the growth trends of their database, software, and files.

# Functional Description and Use of Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Statistical Analysis of Global Growth (SAGG) software is a fully automated support tool developed by the Capacity Planning (CP) team, which entails the monthly capture of global database, software, and file size information from participating sites.

This version of the software can be installed over any previous versions of SAGG without any adverse problems. The current version of the software is compatible with Caché for Windows and Caché for VMS operating systems.

Installing the SAGG Project software creates the collection process mechanism and other necessary components of the software. The fully automated data collection cycle entails capturing all production global, software, and file specifics at the site into a temporary ^XTMP(“KMPS”) collection global. Once collected, the information is converted into an electronic mail message that is automatically transferred via network mail and merged into a Capacity Planning (CP) National Database. The temporary collection global is then deleted from the site’s system. The site also receives a summary of the global statistical data in the form of an electronic turn-around message.

IRM staff uses the options that are locally available at the site to manage this software. IRM staff responsible for capacity management tasks at the site can also use the options available on FORUM. The options on FORUM allow them to review growth trends of their database, software, and file size.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The original distribution of the Statistical Analysis of Global Growth (SAGG) software 2.0, Patch KMPS\*2\*0, was dependent on Patches KMPD\*2.0\*6 and XU\*8.0\*456. Patch KMPS\*2\*0 is a Kernel Installation and Distribution System (KIDS) software release. SAGG Installation Instructions can be found in the description for Patch KMPS\*2\*0, located on the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FOURM.

### Upgrading from a Previous Version of SAGG Related to Patch XU\*8.0\*456

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](sagg-version-2-user-manual/011.png) CAUTION: If your site is upgrading from a previous version of SAGG, Patch XU\*8.0\*456 *must* be installed for SAGG 2.0 to work with Caché 5.2.

### Virgin Installations of SAGG Related to Patch XU\*8.0\*456

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](sagg-version-2-user-manual/012.png) CAUTION: If your site is installing SAGG for the first time, Patch XU\*8.0\*456 *must* be installed for the SAGG Master Background Task Option \[KMPS SAGG REPORT\] to work.

## Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG software is managed locally by IRM staff through the SAGG Project Manager Menu \[KMPS SAGG MANAGER\], which is located under the Capacity Management menu \[XTCM MAIN\]. The XTCM MAIN menu is found under the Kernel Eve menu and should be assigned to IRM staff members who support this software and other capacity planning tasks.

Additionally, these same IRM staff members should also have the SAGG Access to Albany CIOFO Menu \[A1B9 IFO FORUM TO IFO ALBANY\] assigned to them on FORUM. This menu allows them to review growth trends of their database, software, and file size.

# # SAGG Project Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the SAGG Project Manager Menu \[KMPS SAGG MANAGER\] that is located locally at the site. This menu helps the site manage the SAGG (Statistical Analysis of Global Growth) Project. This is broken down by the individual options with a discussion of each option and examples of user interaction. This portion should be thought of and used as a reference guide to the local options within the software.

<span id="_Toc439232434" class="anchor"></span>Figure . SAGG Project Manager Menu options

SAGG Project Manager Menu \[KMPS SAGG MANAGER\]

Check SAGG Environment \[KMPS SAGG STATUS\]

Stop SAGG Collection \[KMPS SAGG STOP\]

## Check SAGG Environment Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Check SAGG Environment option \[KMPS SAGG STATUS\] checks the environment of the SAGG (Statistical analysis of Global Growth) Project. In addition to providing information regarding the SAGG collection routines, this option checks the status of SAGG patch installation at the site.

<span id="_Toc439232435" class="anchor"></span>Figure . Check SAGG Environment option—Sample user dialogue and report

KMPD STATUS Jul 10, 2007 13:58:28 Page: 1 of 3

Environment Check for

KMPS v2.0

Current Status.............. SCHEDULED

SAGG Master Background Task. KMPS SAGG REPORT

QUEUED TO RUN AT............ AUG 04, 2007@19:30 (Saturday)

RESCHEDULING FREQUENCY...... 28 days

TASK ID..................... 7902547

QUEUED BY................... POSTMASTER (Active)

Temporary collection global.

^XTMP(“KMPS”)............... NOT Present

SAGG Project will collect metrics on ALL volumes

Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span> NEXT SCREEN

KMPD STATUS Jul 10, 2007 13:58:28 Page: 2 of 3

Environment Check for

KMPS v2.0

\# of

File Entries

------------------------- -------

8970.1-SAGG PROJECT 1

SAGG routines............... 7 Routines - No Problems

Node/CPU Data............... ISC1A1 AlphaServer ES40 (2)

ISC1A2 AlphaServer ES40 (2)

ISC1A3 hp AlphaServer ES80 7/1000 (4)

ISC1A4 hp AlphaServer ES80 7/1000 (4)

Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span> NEXT SCREEN

KMPD STATUS Jul 10, 2007 13:58:28 Page: 3 of 3

Environment Check for

KMPS v2.0

KMP-CAPMAN Mail Group....... KMPSEMPLOYEE,ONE

KMPSEMPLOYEE,TWO

KMPSEMPLOYEE,THREE (DISUSER)

KMPSEMPLOYEE,FOUR

SAGG = Statistical Analysis of Global Growth

## Stop SAGG Collection Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop SAGG Collection option \[KMPS SAGG STOP\] informs the SAGG Project collection routines to begin an orderly shutdown process. Each collection routine stops after reaching an appropriate break point.

<span id="_Toc439232436" class="anchor"></span>Figure . Stop SAGG Collection option—Sample user dialogue and report

SAGG Project Status

KMPS v2.0

The ‘SAGG Master Background Task’ \[KMPS SAGG REPORT\] is

Scheduled to run as Task ID 3883 on JUN 26, 1998 @ 19:00 mailto:1998@19:00

every 28 days.

XTMP(“KMPS”) Global Location: VAH,VAA

The temporary collection global (i.e., ^XTMP(“KMPS”)) has data.

The SAGG Project routines are still running on:

ROU, VAA, VBB, VCC

Press \<RETURN\> to continue: <span class="mark">\<Enter\></span>

Do you wish to manually STOP the SAGG Project collection routines

(Y/N)? N// <span class="mark">?</span>

Enter either ‘Y’ or ‘N’.

Do you wish to manually STOP the SAGG Project collection routines (Y/N)? N// <span class="mark">YES</span>

The SAGG Project collection routines have been notified to

begin an orderly shut-down process.

## SAGG Master Background Task Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SAGG Master Background Task option \[KMPS SAGG REPORT\] is *not* assigned to any menu. This option is scheduled through TaskMan to start SAGG Project’s master collection routine in the background. This option should be rescheduled with the Schedule/Unschedule Options \[XUTM SCHEDULE\] under the Taskman Management menu for every 28 days to ensure same day-of-week collection cycles. If this option does *not* execute properly, a warning message is sent to the KMPS-SAGG mail group.

<u>Figure 4</u> shows an example of a typical display when using the Schedule/Unschedule Options:

<span id="_Ref439234208" class="anchor"></span>Figure . SAGG Master Background Task option—Sample user dialogue and report

Select OPTION to schedule or reschedule: <span class="mark">KMPS SAGG REPORT\<Enter\></span> (R)

Edit Option Schedule

Option Name: KMPS SAGG REPORT

Menu Text: SAGG Master Background Task TASK ID: 3883

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUN 26,1998@19:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 28D

TASK PARAMETERS:

SPECIAL QUEUEING:

COMMAND: Press \<PF1\>H for help Insert

<span id="_Hlt424356320" class="anchor"></span>

Glossary

| Term                | Description                                                                                                                                                                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BLOCK               | A unit of measure of the size of the disk used by both the operating system and M platforms. Caché BLOCKS are typically 8192 bytes (8k).                                                                                                                                     |
| CAPACITY PLANNING   | The process of assessing a system’s capacity and evaluating its efficiency relative to workload in an attempt to optimize system performance.                                                                                                                                |
| COLLECTION CYCLE    | Occurs when the SAGG background task begins obtaining data regarding the size and efficiency of the globals on the monitored volume sets. Additionally, software and file information is collected. Normally, a site should schedule the collection cycle for every 28 days. |
| COMPLEXITY LEVEL    | A ranking order for sites based on calculated workload needs. Four levels exist with 1 being the largest and 4 being the smallest type facility.                                                                                                                             |
| DATA BLOCK          | A component of the global tree-structure that is used by the M platform to contain the actual information.                                                                                                                                                                   |
| DATABASE            | A set of information, consisting of at least one file, which is specific for a given purpose. The VistA database is composed of a number of VA FileMan files.                                                                                                                |
| DISK MODEL RANK     | A ranking order for sites based on calculated disk capacity needs.                                                                                                                                                                                                           |
| GLOBAL              | Tree-structured system of nodes containing common data. M platforms store data on the disk in the form of global arrays. A global is composed of both pointer and data blocks.                                                                                               |
| GLOBAL EFFICIENCY   | Determines the amount of space used within the entire block structure of a particular global. A higher efficiency indicates that the global is compacted, and therefore, using less disk space.                                                                              |
| GLOBAL SIZE         | Determines the amount of pointer and data blocks used by a particular global.                                                                                                                                                                                                |
| MAP                 | Composed of subunits called blocks. A map consists of 400 blocks.                                                                                                                                                                                                            |
| MODEL RANK          | A ranking order for sites based on calculated VistA workload needs.                                                                                                                                                                                                          |
| POINTER BLOCK       | A component of the global tree-structure that is used by the M platform to find the location of data blocks.                                                                                                                                                                 |
| SAGG                | Statistical Analysis of Global Growth. A fully automated support tool developed by the Capacity Planning (CP) team, which entails the monthly capture of global, database, software, and file size information from participating sites.                                     |
| SESSION NUMBER      | Timestamp of when the collection cycle was run. The session number is defined from the +\$H system variable.                                                                                                                                                                 |
| TURN-AROUND MESSAGE | The mail message that is returned to the KMPS-SAGG mail group detailing the database and global growth over the previous reported session.                                                                                                                                   |
| ZEROTH NODE         | The number of file entries is stored within the zeroth node of VistA software files. This information is used to determine software file growth statistics.                                                                                                                  |

<span id="_Toc439232352" class="anchor"></span>Table . Statistical Analysis of Global Growth glossary terms

![](sagg-version-2-user-manual/013.png) REF: For a list of commonly used terms and definitions, see the OI&T Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

# <span id="_Toc439236032" class="anchor"></span>Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

A1B9 IFO FORUM TO IFO ALBANY Menu, 3

Acronyms

Intranet Website, 9

Assumptions, ix

C

Callout Boxes, viii

Capacity Planning Menu, 3

Check SAGG Environment option, 4

Collection Global, 2

Contents, iv

Conventions

Documentation, vii

CP National Database, 1, 2

CPE

Website, ix

D

Data Dictionary

Data Dictionary Utilities Menu, ix

Listings, ix

Description, Functional, 2

Disclaimers

Documentation, vi

Software, vi

Documentation

Conventions, vii

Revisions, ii

Symbols, vii

Documentation Disclaimer, vi

Documentation Navigation, viii

E

Eve Menu, 3

F

Figures, v

FORUM, iii, 1, 2, 3

Functional Description, 2

G

Globals

^XTMP, 2

Glossary, 8

Intranet Website, 9

H

Help

At Prompts, ix

Online, ix

Question Marks, ix

History

Revisions, ii

Home Pages

Acronyms Intranet Website, 9

Adobe Website, x

CPE Website, ix

Glossary Intranet Website, 9

VA Software Document Library (VDL), x

How to

Obtain Technical Information Online, ix

Use this Manual, vi

I

Implementation, 2

installation of SAGG

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

upgrading from previous version, 2

Virgin, 2

Intended Audience, vi

Introduction, 1

K

KMP-CAPMAN Mail Group, 7

KMPD\*2.0\*6, 2

KMPS SAGG MANAGER Menu, 3, 4

KMPS SAGG REPORT Option, 2, 7

KMPS SAGG STOP Option, 6

KMPS\*2\*0, 2

L

List File Attributes Option, ix

M

Mail Groups

KMP-CAPMAN, 7

Menus

A1B9 IFO FORUM TO IFO ALBANY, 3

Capacity Planning Menu, 3

Data Dictionary Utilities, ix

Eve, 3

KMPS SAGG MANAGER, 3, 4

SAGG Access to Albany CIOFO Menu, 3

SAGG Project Manager Menu, 3, 4

Taskman Management menu, 7

XTCM MAIN, 3

N

National Database, Capacity Planning, 1, 2

O

Obtaining

Data Dictionary Listings, ix

Online

Documentation, ix

Technical Information, How to Obtain, ix

Option

Check SAGG Environment, 4

Options

A1B9 IFO FORUM TO IFO ALBANY, 3

Capacity Planning Menu, 3

Data Dictionary Utilities, ix

Eve, 3

KMPS SAGG MANAGER, 3, 4

KMPS SAGG REPORT, 7

KMPS SAGG STOP, 6

List File Attributes, ix

SAGG Access to Albany CIOFO Menu, 3

SAGG Master Background Task, 7

SAGG Project Manager Menu, 3, 4

Schedule/Unschedule Options, 7

Stop SAGG Collection, 6

Taskman Management menu, 7

XTCM MAIN, 3

XUTM SCHEDULE, 7

Orientation, vi

P

Patch KMPD\*2.0\*6, 2

Patch KMPS\*2\*0, 2

Patch XU\*8.0\*456, 2

Patches

Revisions, iii

PS Anonymous Directories, x

Q

Question Mark Help, ix

R

Reference Materials, ix

Revision History, ii

Documentation, ii

Patches, iii

S

SAGG

Description, 2

Software management, 3

SAGG Access to Albany CIOFO Menu, 3

SAGG Master Background Task Option, 2, 7

SAGG Project Collection Routines

Shutdown Process, 6

SAGG Project Manager Menu, 3, 4

Schedule/Unschedule Options, 7

Shutdown Process

SAGG Project Collection Routines, 6

Software

Management, 3

Software Disclaimer, vi

Stop SAGG Collection Option, 6

Symbols

Found in the Documentation, vii

System Requirements, 2

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

upgrading from previous version, 2

Virgin installation, 2

T

Tables, v

Taskman Management Menu, 7

U

upgrading from a previous version of SAGG, 2

URLs

Acronyms Intranet Website, 9

Adobe Website, x

CPE Website, ix

Glossary Intranet Website, 9

VA Software Document Library (VDL), x

V

VA Software Document Library (VDL)

Website, x

Virgin installations of SAGG, 2

KMPS SAGG REPORT, 2

SAGG Master Background Task Option, 2

W

Websites

Acronyms Intranet Website, 9

Adobe Website, x

CPE, ix

Glossary Intranet Website, 9

VA Software Document Library (VDL), x

X

XTCM MAIN Menu, 3

XTMP Global, 2

XTMP(”KMPS”) Collection Global, 2

XU\*8.0\*456, 2

XUTM SCHEDULE Option, 7