---
title: List Manager 1.0 Developer's Guide
doc_type: DG
doc_label: Developer Guide
doc_layer: anchor
doc_subject: Developer's Guide
app_code: VALM
app_name: List Manager
section: INF
app_status: active
pkg_ns: VALM
patch_ver: 1.0
patch_id: VALM*1.0
group_key: "VALM:VALM:1.0"
file_numbers: []
security_keys: []
menu_options: 21
description: 
audience: 
keywords: 
  - valm
  - manager
  - table
  - line
  - contents
  - span
  - your
  - strong
  - array
  - protocol
page_count: 0
word_count: 20760
section_count: 20
table_count: 11
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/List_Manager/valm_1_0_dg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/List_Manager/valm_1_0_dg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=14"
---

---
title: |
  <span id="_Toc137738635" class="anchor"></span>List Manager 1.0

  <span id="_Toc137738636" class="anchor"></span>Developer’s Guide
---

![](list-manager-1-0-developer-s-guide/001.png)

March 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="revision_history" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref431821080" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 15%" />
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
<td>03/05/2025</td>
<td>3.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated all formatting and style to follow current OIT standards and style guidelines.</p></li>
<li><p><u>Table 10</u>: Corrected index line reference in the <a href="#VALMAR_IDX_Variable"><strong>@VALMAR@("IDX")</strong></a> example.</p></li>
</ul></td>
<td>VistA Infrastructure Shared Services (VISS) Development Team</td>
</tr>
<tr class="even">
<td>03/19/2024</td>
<td>3.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>2.3.3</u>:Removed references to VALMINIT and to now use KIDS to install List Manger.</p></li>
<li><p>Section 508 conformance updates:</p></li>
</ul>
<ul>
<li><blockquote>
<p>Marked all decorative images throughout.</p>
</blockquote></li>
<li><blockquote>
<p>Changed all absolute URLs to relative URLs throughout.</p>
</blockquote></li>
</ul>
<ul>
<li><p>Update reference to the Network File System (NFS; formerly known as the Anonymous Directories).</p></li>
</ul></td>
<td>VISS Development Team</td>
</tr>
<tr class="odd">
<td>06/30/2023</td>
<td>3.0</td>
<td><p>Updates:</p>
<ul>
<li><p>Reformatted document to follow current documentation standards and style guidelines.</p></li>
<li><p>Added image and table captions throughout.</p></li>
<li><p>Verified document is Section 508 conformant.</p></li>
<li><p>List Manager Patch VALM*1.0*10: Updated the <u>EN^VALM2(): Generic Selector</u> API: Updated the <strong>Options</strong> input parameter.</p></li>
</ul>
<p><strong>ListMan 1.0</strong></p></td>
<td>VISS Development Team</td>
</tr>
<tr class="even">
<td>04/09/2012</td>
<td>2.0</td>
<td><p>Updates: Miscellaneous.</p>
<p><strong>ListMan 1.0</strong></p></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
<tr class="odd">
<td>07/1995</td>
<td>1.0</td>
<td><p>Initial List Manager (ListMan ) 1.0 Developer’s Guide.</p>
<p><strong>ListMan 1.0</strong></p></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref431821080" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc192050535" class="anchor"></span>List of Figures

<span id="_Toc192050536" class="anchor"></span>List of Tables

<span id="_Toc192050537" class="anchor"></span>Orientation

How to Use this Manual

This manual provides advice and instruction about ListMan 1.0 Application Programming Interfaces (APIs), Direct Mode Utilities, and other information for Veterans Health Information Systems and Technology Architecture (VistA) application developers.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Software Product Management (SPM)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](list-manager-1-0-developer-s-guide/002.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per [VA Directive 6402](http://www.va.gov/vapubs/viewPublication.asp?Pub_ID=718&FType=2) (pending signature), this routine should not be modified.

![](list-manager-1-0-developer-s-guide/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation of using ListMan; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Software Product Management (SPM) Intranet Website.

![](list-manager-1-0-developer-s-guide/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. [Table 1](#_Ref431821080) gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](list-manager-1-0-developer-s-guide/005.png)  | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](list-manager-1-0-developer-s-guide/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Toc192050654" class="anchor"></span>Table 2: Sample List Manager Display Key

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in ListMan (VALM) test patient and user names would be documented as follows:

VALMPATIENT,ONE;VALMPATIENT,TWO; VALMPATIENT,THREE; … VALMPATIENT,14; etc.

VALMUSER,ONE; VALMUSER,TWO; VALMUSER,THREE; … VALMUSER,14; etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are boldface and (optionally) highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialog box is boldface and (optionally) highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](list-manager-1-0-developer-s-guide/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- Descriptions of Direct Mode utilities are prefaced with the standard M “\>” prompt to emphasize that the call is to be used *only in Direct Mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- The following conventions are used with regards to APIs:
- The following API types are documented:
- Supported:

This applies where any VistA application may use the attributes/functions defined by the Integration Control Registration (ICR); these are also called “Public”. An example is an ICR that describes a standard API. The package that creates/maintains the Supported Reference *must* ensure it is recorded as a Supported Reference in the ICR database. There is no need for other VistA packages to request an ICR to use these references; they are open to all by default.

- Controlled Subscription:

Describes attributes/functions that *must* be controlled in their use. The decision to restrict the Integration Control Registration (ICR) is based on the maturity of the custodian package. Typically, these ICRs are created by the requesting package based on their independent examination of the custodian package’s features. For the ICR to be approved the custodian grants permission to other VistA packages to use the attributes/functions of the ICR; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package.

![](list-manager-1-0-developer-s-guide/008.png) Private APIs are *not* documented.

- Headings for developer API descriptions (e.g., supported for use in applications and on the Database Integration Committee \[DBIC\] list) include the routine tag (if any), the caret (^) used when calling the routine, and the routine name. The following is an example:

EN1^XQH

- For APIs that take input parameter, the input parameter is labeled “required” when it is a required input parameter and labeled “optional” when it is an optional input parameter.
- For APIs that take parameters, parameters are shown in lowercase and variables are shown in uppercase. This is to convey that the parameter name is merely a placeholder; M allows you to pass a variable of any name as the parameter or even a string literal (if the parameter is *not* being passed by reference). The following is an example of the formatting for input parameters:

XGLMSG^XGLMSG(msg_type,\[.\]var\[,timeout\])

- Rectangular brackets \[\] around a parameter are used to indicate that passing the parameter is optional. Rectangular brackets around a leading period \[.\] in front of a parameter indicate that you can optionally pass that parameter by reference.
- All APIs are categorized by function. This categorization is subjective and subject to change based on feedback from the development community. In addition, some APIs could fall under multiple categories; however, they are only listed once under a chosen category.  
    
  APIs within a category are first sorted alphabetically by Routine name and then within routine name are sorted alphabetically by Tag reference. The \$\$, ^, or ^% prefixes on APIs is ignored when alphabetizing.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](list-manager-1-0-developer-s-guide/009.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

Entry Points

For Application Programming Interface (AI) entry points that take input variables, the input variable is labeled optional if it is optional; otherwise, it is a required variable.

For entry points that take parameters, parameters are listed in lowercase. This is to convey that the listed parameter name is merely a placeholder. MUMPS (M) allows you to pass a variable of any name as the parameter or even a string literal (if the parameter is *not* being passed by reference).

The following is an example of the documentation format for input parameters:

D XGLMSG^XGLMSG(msg_type,\[.\]var\[,timeout\])

Rectangular brackets \[ \] around a parameter are used to indicate that passing the parameter is optional. Rectangular brackets around a leading period in front of a parameter indicate that you can optionally pass that parameter by reference.

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

![](list-manager-1-0-developer-s-guide/010.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](list-manager-1-0-developer-s-guide/011.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](list-manager-1-0-developer-s-guide/012.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- ListMan—VistA M Server software
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about ListMan should consult the following:

- *List Manager 1.0 Developer’s Guide* (this manual)
- ListMan VA Intranet Website.

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](list-manager-1-0-developer-s-guide/013.png) REF: List Manager manuals are located on the [List Manager application on the VDL](https://www.va.gov/vdl/application.asp?appid=14).

Unredacted VistA documentation and software can be downloaded from the Network File System (NFS; formerly known as the Anonymous Directories).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [List Manager Main Screen](#list-manager-main-screen)
  - [List Manager Workbench—^VALMWB](#list-manager-workbenchvalmwb)
  - [Installation and Setup](#installation-and-setup)
    - [Major List Manager Components](#major-list-manager-components)
    - [Package Requirements](#package-requirements)
    - [Installation](#installation)
    - [Terminal Type Attributes for List Manager Users](#terminal-type-attributes-for-list-manager-users)
- [How to Make a List Manager Application](#how-to-make-a-list-manager-application)
  - [Define List Template](#define-list-template)
    - [Create a New List Template](#create-a-new-list-template)
    - [Create an Outline Routine](#create-an-outline-routine)
    - [Edit the List Template](#edit-the-list-template)
    - [Edit the Outline Routine](#edit-the-outline-routine)
    - [What Comes Next?](#what-comes-next)
  - [Define List Array](#define-list-array)
    - [Routine to Create List](#routine-to-create-list)
    - [Array to Store the List](#array-to-store-the-list)
    - [Build the List Array Yourself](#build-the-list-array-yourself)
    - [Build the List Array Using List Manager’s API](#build-the-list-array-using-list-managers-api)
  - [Define List Actions](#define-list-actions)
    - [How To Define an Action](#how-to-define-an-action)
    - [How to Select List Items](#how-to-select-list-items)
    - [Using the Entire Screen](#using-the-entire-screen)
    - [When Your Action Completes](#when-your-action-completes)
  - [Define List Menu](#define-list-menu)
    - [Steps to Set Up Your Application’s Menu](#steps-to-set-up-your-applications-menu)
    - [Hidden Menu](#hidden-menu)
    - [Columnar Arrangement of Menu Items](#columnar-arrangement-of-menu-items)
    - [Sub-Menus](#sub-menus)
    - [Overriding the Default Action](#overriding-the-default-action)
  - [Fine Tune Your Application](#fine-tune-your-application)
    - [Entry Selection and Light Bar Scrolling](#entry-selection-and-light-bar-scrolling)
    - [Setting Video Attributes in Your List Line](#setting-video-attributes-in-your-list-line)
    - [Updating Items in the List](#updating-items-in-the-list)
    - [When the User Is In Scrolling Mode (Not Screen Mode)](#when-the-user-is-in-scrolling-mode-not-screen-mode)
    - [Scroll-Locking Columns](#scroll-locking-columns)
    - [Browsing Word-Processing Fields](#browsing-word-processing-fields)
    - [Long Lists](#long-lists)
    - [Calling List Manager and Other Programs from Actions](#calling-list-manager-and-other-programs-from-actions)
  - [Export Your List Manager Application](#export-your-list-manager-application)
    - [Protocols](#protocols)
    - [List Templates](#list-templates)
    - [Before Kernel 8.0](#before-kernel-80)
  - [Example Code](#example-code)
    - [LIST TEMPLATE PROTOCOL MENU](#list-template-protocol-menu)
    - [PROTOCOL Menu](#protocol-menu)
    - [PROTOCOL Action](#protocol-action)
    - [DISPLAY TYPE](#display-type)
    - [Application Code Examples](#application-code-examples)
- [List Template Reference](#list-template-reference)
  - [Fields](#fields)
    - [Demographics Fields](#demographics-fields)
    - [Protocol Information Fields](#protocol-information-fields)
    - [List Region Fields](#list-region-fields)
    - [Other Fields](#other-fields)
    - [MUMPS Code Related Fields](#mumps-code-related-fields)
    - [Caption Line Information Fields](#caption-line-information-fields)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [List Manager Variables](#list-manager-variables)
  - [Kernel Video Variables](#kernel-video-variables)
  - [List Manager Generic Action Protocols](#list-manager-generic-action-protocols)
  - [General APIs](#general-apis)
    - [EN^VALM(): Load a ListMan Template/Application](#envalm-load-a-listman-templateapplication)
    - [SHOW^VALM: Display Menu to User](#showvalm-display-menu-to-user)
    - [PAUSE^VALM1: Pause the Screen](#pausevalm1-pause-the-screen)
    - [RANGE^VALM1: Change Date Range](#rangevalm1-change-date-range)
    - [EN^VALM2(): Generic Selector](#envalm2-generic-selector)
  - [List Line Text APIs](#list-line-text-apis)
    - [FLDUPD^VALM1(): Update Caption Field](#fldupdvalm1-update-caption-field)
    - [\$\$SETFLD^VALM1(): Insert Text in a String](#setfldvalm1-insert-text-in-a-string)
    - [\$\$SETSTR^VALM1(): Set Up String for Display](#setstrvalm1-set-up-string-for-display)
    - [FLDTEXT^VALM10(): Inserts Text in a Column](#fldtextvalm10-inserts-text-in-a-column)
    - [SET^VALM10(): Construct Initial List Array](#setvalm10-construct-initial-list-array)
  - [List Line Video APIs](#list-line-video-apis)
    - [CNTRL^VALM10(): Set Video Attributes](#cntrlvalm10-set-video-attributes)
    - [FLDCTRL^VALM10(): Activate Video Control Sequences](#fldctrlvalm10-activate-video-control-sequences)
    - [RESTORE^VALM10(): Restores Video Attributes](#restorevalm10-restores-video-attributes)
    - [SAVE^VALM10(): Save Current Video Attributes](#savevalm10-save-current-video-attributes)
    - [SELECT^VALM10(): Highlights/Unhighlights Line in List](#selectvalm10-highlightsunhighlights-line-in-list)
    - [WRITE^VALM10(): Re-Write Line to Screen](#writevalm10-re-write-line-to-screen)
  - [Screen Control APIs](#screen-control-apis)
    - [CHGCAP^VALM(): Changes Label on Caption Header](#chgcapvalm-changes-label-on-caption-header)
    - [CLEAR^VALM1: Clean Up Screen after Error Occurs](#clearvalm1-clean-up-screen-after-error-occurs)
    - [FULL^VALM1: Sets Screen to Full Scrolling Region](#fullvalm1-sets-screen-to-full-scrolling-region)
    - [INSTR^VALM1(): Inserts Text on Display Screen](#instrvalm1-inserts-text-on-display-screen)
    - [RE^VALM4: Re-Displays List Header and List Areas](#revalm4-re-displays-list-header-and-list-areas)
    - [CLEAN^VALM10: Kills Data and Video Control Arrays](#cleanvalm10-kills-data-and-video-control-arrays)
    - [KILL^VALM10(): Deletes Video Attributes](#killvalm10-deletes-video-attributes)
    - [MSG^VALM10(): Post Message to “Message Window”](#msgvalm10-post-message-to-message-window)
  - [Conversion APIs](#conversion-apis)
    - [\$\$FDATE^VALM1(): Returns Date in “MM/DD/YY” Format](#fdatevalm1-returns-date-in-mmddyy-format)
    - [\$\$FDTTM^VALM1(): Returns Date/Time in “MM/DD/YY@HH:MM” Format](#fdttmvalm1-returns-datetime-in-mmddyyhhmm-format)
    - [\$\$FTIME^VALM1(): Returns Date/Time in “MMM DD, YYYY@HH:MM” Format](#ftimevalm1-returns-datetime-in-mmm-dd-yyyyhhmm-format)
    - [\$\$LOWER^VALM1(): Converts String from Uppercase to Lowercase](#lowervalm1-converts-string-from-uppercase-to-lowercase)
    - [\$\$NOW^VALM1: Returns Value of “NOW” in External Format](#nowvalm1-returns-value-of-now-in-external-format)
    - [\$\$UPPER^VALM1(): Converts String from Lowercase to Uppercase](#uppervalm1-converts-string-from-lowercase-to-uppercase)
The Veterans Health Information Systems and Technology Architecture (VistA) List Manager (aka ListMan) provides a generic method of presenting lists of items to terminal users. Its core functions are:
- Display a list of items.
- Users can browse through the list.
- Users can select one or more items from the list.
- Users can execute an action for selected list items.
- You can use List Manager recursively within an action.
The *List Manager Developer’s Guide* is designed to provide the Department of Veterans Affairs (VA) developer with “how to” information on creating applications using List Manager. This manual is a full reference for creating List Manager applications.
List Manager was originally developed as an interface for the Scheduling module of VistA’s MAS V. 5.2 package. Since then it has been used as an interface for a number of other applications, including Text Integration Utility (TIU).

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List Manager Main Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 1</u> is an illustration of the components of a typical List Manager display. The screen is divided into three regions:

- Header Area
- List Area
- Action Area

<span id="_Ref137634189" class="anchor"></span>Figure 1: Sample List Manager Display

![](list-manager-1-0-developer-s-guide/014.png)

| Key | Controlled By                                                                   |
|-----|---------------------------------------------------------------------------------|
| 1   | [Header Code](#header-code-100)                                                 |
| 2   | [Expand Code](#expand-code-102-optional)                                        |
| 3   | [Top Margin](#top-margin-.05)                                                   |
| 4   | [Bottom Margin](#bottom-margin-.06), [Right Margin](#right-margin-.04-optional) |
| 5   | [Screen Title](#screen-title-.11-optional-but-recommended-screen-title-field)   |
| 6   | [Caption Line Columns](#CAPTION_LINE_COLUMNS)                                   |
| 7   | [Column](#column-.02)                                                           |
| 8   | [Array Name](#array-name-107-optional)                                          |
| 9   | [Display Text](#display-text-.04-optional)                                      |
| 10  | [Date Range Limit](#date-range-limit-.13-optional)                              |

<span id="_Ref137634893" class="anchor"></span>Table 3: Package Requirements

You are only allowed to directly WRITE to the “Action Area.” The List Manager controls the other two areas. However, you can modify the contents of the “Header Area” and “List Area” by using calls in the [List Manager API](#application-programming-interfaces-apis), and by changing the HEADER and LIST arrays passed to the List Manager.

## List Manager Workbench—^VALMWB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager Workbench (<u>Figure 2</u>) allows the development of a List Manager application without having to move from one development tool to another. Load the Workbench by calling the ^VALMWB routine.

<span id="_Ref138223621" class="anchor"></span>Figure 2: List Manager Workbench

![](list-manager-1-0-developer-s-guide/015.png)

The Workbench allows you to edit all of the data for the following:

- [List Template](#define-list-template)
- [Action Protocols](#define-list-actions)
- [Menu Protocols](#define-list-menu)
- Input Templates
- Routines

In short, every part of a List Manager application.

You can run a List Template from the Workbench. When you run a template, you are prompted for any “setup” code to initialize variables. This is needed if the template is *not* a top-level template. After “running” the template, you are returned to the Workbench. The Workbench itself is a List Manager application.

We *recommend* that you do all List Template development using the Workbench. As new features become available, the Workbench will automatically present them to you.

## Installation and Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Major List Manager Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The major List Manager components include:

- LIST TEMPLATE (#409.61) file.
- PROTOCOL (#101) file.
- Routines in the VALM\* namespace (List Manager routines).
- Routines in the XQOR\* namespace (Protocol Processing routines).

### Package Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the packages and versions that *must* be present for List Manager to run properly:

| Package                              | Version        |
|--------------------------------------|----------------|
| Order Entry Results Reporting (OERR) | 2.5 or greater |
| Kernel                               | 6.5 or greater |

<span id="_Ref137635106" class="anchor"></span>Table 4: Terminal Type Attributes for List Manager Users

### Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Kernel Installation and Distribution System (KIDS) to install the List Manager.

### Terminal Type Attributes for List Manager Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the terminal type attributes that *must* be defined for List Manager users in order to effectively use the List Manager:

| TERMINAL TYPE Field  | Example Field Values for VT-100 Terminal |
|----------------------|------------------------------------------|
| Form Feed            | \#,\$C(27,91,50,74,27,91,72)             |
| XY CRT               | W \$C(27,91),DY+1,\$C(59),DX+1,\$C(72)   |
| Erase to End of Page | \$C(27,91,74)                            |
| Insert Line          | \$C(27,91),“1L”                          |
| Underline On         | \$C(27,91,52,109)                        |
| Underline Off        | \$C(27,91,109                            |
| High Intensity       | \$C(27,91,49,109)                        |
| Normal Intensity     | \$C(27,91,109)                           |
| Save Cursor Position | \$C(27,55)                               |
| Restore Cursor Pos   | \$C(27,56)                               |
| Set Top/Bottom Marg  | \$C(27,91),+IOTM,\$C(59),+IOBM,\$C(114)  |
| SGR Attributes Off   | \$C(27,91,109)                           |

<span id="_Ref138223998" class="anchor"></span>Table 5: List Template Field Categories

# How to Make a List Manager Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Define List Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step to create a List Manager application is to create the List Template for your application. A List Template is the core of a List Manager application; all of the crucial information that determines how a list works is stored in an application’s List Template. The best way to set up (and maintain) a List Template is to use the [Workbench](#list-manager-workbenchvalmwb).

### Create a New List Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you invoke the [Workbench](#list-manager-workbenchvalmwb), it asks you for a List Template name. You can either enter an existing one or create a new one.

### Create an Outline Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Templates depend on calling several subroutines to perform specific actions, including:

- Initializing your application.
- Creating the array of list items that becomes your list.

As such, creating these subroutines is central to your List Template. That is why the next question you are asked after you name your template is “Enter Routine Name: ”.

The [Workbench](#list-manager-workbenchvalmwb) can create an outline routine that contains subroutines to perform all of the functions List Manager requires. Entering a name is optional. However, if you enter a name for a routine, the [Workbench](#list-manager-workbenchvalmwb) creates an outline routine for your application with stub tags and code for the template. The created List Template is then immediately executable.

<u>Figure 3</u> demonstrates how you can use the [Workbench](#list-manager-workbenchvalmwb) to set up an outline routine for your application:

<span id="_Ref137725480" class="anchor"></span>Figure 3: Using the Workbench to Set Up an Outline Routine for Your Application—System Prompts and User Entries

Select LIST TEMPLATE NAME: <span class="mark">ZZLIST</span>

Are you adding 'ZZLIST' as a new LIST TEMPLATE (the 14TH)? <span class="mark">Y \<Enter\></span> (Yes)

\>\>\> The system will create a stub routine...

\>\>\> Enter Routine Name: <span class="mark">ZZLIST</span>

I am going to create a series of 'ZZLIST\*' routines.

Is that OK? Yes// <span class="mark">\<Enter\></span> (Yes)

\>\>\> Building 'ZZLIST' stub routine

ZZLIST has been filed

A fully functional List Manager application (with a “dummy” list of items) has now been created; and you are placed in the [Workbench](#list-manager-workbenchvalmwb) with the new List Template loaded.

### Edit the List Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [Workbench](#list-manager-workbenchvalmwb) lets you edit all of the fields in the List Template. It organizes the fields in a list template into six distinct categories, as shown in <u>Table 5</u>.

<table>
<caption><p><span id="_Toc192050658" class="anchor"></span>Table 6: Outline Routine Tags</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#demographics-fields"><u>Demographics</u></a></td>
<td>Set up the list name, generic prompt, and screen title.</td>
</tr>
<tr class="even">
<td><a href="#protocol-information-fields"><u>Protocol Information</u></a></td>
<td>Set up the menus for your list.</td>
</tr>
<tr class="odd">
<td><a href="#list-region-fields"><u>List Region</u></a></td>
<td>Set the screen region for the list.</td>
</tr>
<tr class="even">
<td><a href="#other-fields"><u>Other Fields</u></a></td>
<td>Set miscellaneous list attributes.</td>
</tr>
<tr class="odd">
<td><a href="#mumps-code-related-fields"><u>MUMPS Code Related</u></a></td>
<td><p>Specify the routines for:</p>
<ul>
<li><p>Header</p></li>
<li><p>Entry</p></li>
<li><p>Exit</p></li>
<li><p>Expand</p></li>
<li><p>Help</p></li>
</ul>
<p>Optionally, enter the array name in which that list is kept. When List Manager creates an outline routine, it uses that routine for most of these tasks.</p></td>
</tr>
<tr class="even">
<td><a href="#caption-line-information-fields"><u>Caption Line Information</u></a></td>
<td>Define the contents of the caption line (list headings).</td>
</tr>
</tbody>
</table>

<span id="_Toc192050658" class="anchor"></span>Table 6: Outline Routine Tags

The [Workbench](#list-manager-workbenchvalmwb) also lets you perform a number of actions beyond editing the List Template. One of the actions you can perform is running the list (Run List action). Try running the list now as set up by default by List Manager. This gives you an idea of what a bare bones List Manager application looks like.

Later, as you add enhancements to your application, you can use the [Workbench](#list-manager-workbenchvalmwb) to edit a number of your List Template’s fields.

### Edit the Outline Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The outline routine that was created contains six specific subroutines (<u>Figure 4</u>). By going through each subroutine, you see the beginning of your application.

<span id="_Ref138235537" class="anchor"></span>Figure 4: Outline Routine Subroutines

ZZKYLM ; ; 08-OCT-1996

;; ;

EN ; -- main entry point for ZZLIST

D EN^VALM("ZZLIST")

Q

;

HDR ; -- header code

S VALMHDR(1)="This is a test header for ZZLIST."

S VALMHDR(2)="This is the second line"

Q

;

INIT ; -- init variables and list array

F LINE=1:1:30 D SET^VALM10(LINE,LINE\_" Line number "\_LINE)

S VALMCNT=30

Q

;

HELP ; -- help code

S X="?" D DISP^XQORM1 W !!

Q

;

EXIT ; -- exit code

Q

;

EXPND ; -- expand code

Q

;

| Outline Routine Tag                                                | Description                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EN                                                             | Application Entry Point: This section of the code in the outline routine is the line of code to independently invoke List Manager and load your List Template (and your list). If you were to make an option for your List Manager application, you would set the option’s RUN ROUTINE field to this tag and routine. |
| HDR                                                            | Header Code: In this very simple section of the outline routine, two nodes of the VALMHDR array are set. These should be set to the text lines to display in the “Header Area” of the List Manager screen. List Manager calls this subroutine when initializing your list.                                        |
| <span id="init_outline_routine_tag" class="anchor"></span>INIT | List Creation: In this section of the outline routine, all the work is done to create the list of items that is displayed to the user by List Manager. Setting up your list is discussed in more detail in the ”[Define List Array](#define-list-array))” section.                                                    |
| HELP                                                           | Help: You can set up custom help in this subroutine. When a user enters a “?” at the menu prompt, your custom help would be called. This is an optional feature.                                                                                                                                                  |
| EXIT                                                           | Exit Code: Use this subroutine to clean up variables and any other exit processing your application needs to perform before exiting.                                                                                                                                                                                  |
| EXPND                                                          | Expand Code: This subroutine is for placing MUMPS (M) code to display a detailed inquiry-type report/screen for a specific entry in the list. This is an advanced, optional feature.                                                                                                                                  |

<span id="_Ref138229204" class="anchor"></span>Table 7: Setting DIR(0) Input Variable to Select Items

In the “[Define List Array](#define-list-array)” section you edit the outline routine’s [INIT](#init_outline_routine_tag) subroutine, replacing the “dummy” list of items created in the stub subroutine with your application’s list items. This is the next step in your application, setting up the list of items for List Manager to display to your list user.

### What Comes Next?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have created a List Template for your application. You have created an outline routine for your application. So, what comes next?

You need to [set up the list of items](#define-list-array) that your application displays to your list user. Setting up the list is the second of four steps in creating a List Manager application.

To add functionality to your application, you need to [create Action-type protocols](#define-list-actions). These are akin to menu options and are the actions available to your list users in the “Action Area” at the bottom of the List Manager screen (<u>Figure 1</u>). These actions let your list users select items and perform actions with the select items. Creating actions is the third of four steps in creating a List Manager application.

Finally, once you create some Action-type protocols, you need to [create a Menu-type protocol](#define-list-menu). Then, attach all of your actions to the Menu-type protocol, and designate the menu protocol as your List Template’s Protocol Menu. Then, run your application and test out all of your actions. Organizing your menu is the fourth of four steps in creating a List Manager application.

## Define List Array

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have created a List Template to define your List Manager application, the next step is to set up the array (list) of items that is displayed to your list user. You set up the list array using M code in the routine specified in the List Template’s [ENTRY CODE](#entry-code-106) field.

### Routine to Create List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine specified in the [ENTRY CODE](#entry-code-106) field in the “[MUMPS Code Related Fields](#mumps-code-related-fields)” section of the [Workbench](#list-manager-workbenchvalmwb) (<u>Figure 2</u>) is what List Manager calls to set up your list. So, you *must* set your list array up in a routine.

If you let List Manager create an outline routine for your List Template, it sets this field in the List Template to the [INIT](#init_outline_routine_tag) label of the routine it creates. In the created outline routine, it sets up a “dummy” list using the [SET^VALM10](#setvalm10-construct-initial-list-array) entry point. If you look at the code it puts in this subroutine, you can see one way to create a list. You can set up a list entirely yourself, or you can use some of List Manager’s entry points. Both methods are described below.

### Array to Store the List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [ARRAY NAME](#array-name-107-optional) field in a List Template, in the “[MUMPS Code Related Fields](#mumps-code-related-fields)” section of the [Workbench](#list-manager-workbenchvalmwb), should contain the name of the array that holds your list of items to be displayed.

![](list-manager-1-0-developer-s-guide/016.png) NOTE: The array name *must* be preceded by a space character. This is needed to allow global specification. VA FileMan does *not* allow “^” as the first character. The array can be either a local or global variable.

The array of list items you create needs to follow the format used in word-processing fields:

^TMP("SDAM",\$J,line \#,0)=display_string

There is one case in which you do *not* need to specify the array name in the [ARRAY NAME](#array-name-107-optional) field. By making calls to [SET^VALM10](#setvalm10-construct-initial-list-array), you can have the List Manager decide where to store the list array. This method of creating a list is discussed in the “<u>Build the List Array Yourself</u>” section.

### Build the List Array Yourself

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a list of items yourself, do the following:

1.  In the routine called by the [ENTRY CODE](#entry-code-106) field of the List Template, make an array of items in the list. Make sure your array is in the same format as word-processing fields, that is, ^TMP(“SDAM”,\$J,line \#,0)=display_string). The list array should start with list item 1, and there should be no gaps in the array line sequence.
2.  It is a good idea to include the line number as the first part of the text of each display line. This aids list users when selecting items.
3.  Set the [ARRAY NAME](#array-name-107-optional) field of the List Template to the name of the array.
4.  Set the [VALMCNT](#VALMCNT_Variable) variable equal to the number of items in your list.
5.  You are done!

Somewhere else, you may want to store a corresponding index of the entry number for items in your list, if your items correspond to entries in a file. Then, when you get to making actions, you are able to associate an item in the list with the entry number from which it came.

### Build the List Array Using List Manager’s API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager provides an API, which includes entry points for creating and maintaining lists.

#### Creating the Array with SET^VALM10

You can create the array entries in your list using the [SET^VALM10](#setvalm10-construct-initial-list-array) entry point. When you do this, you do *not* need to set an explicit array name in the List Templates [ARRAY NAME](#array-name-107-optional) field. List Manager maintains the array itself, without you needing to know where it is stored. If you need to reference lines in the array, you can use the @VALMAR@(\<line \#\>,0) syntax.

To set up and maintain your array using [SET^VALM10](#setvalm10-construct-initial-list-array), do the following:

1.  All of the code that follows should be in the routine called by the [ENTRY CODE](#entry-code-106) field of the List Template.
6.  Keep in mind that your list array should start with list item 1, and that there should be no gaps in the array sequence of lines.
7.  To add a line to the list, make a call to [SET^VALM10](#setvalm10-construct-initial-list-array):

D SET^VALM10(line_num,display_text)

8.  It is a good idea to include the line number as the first part of the text of each display line. This aids list users when selecting items.
9.  If the items in your list correspond to file entries, you may want to keep track of the internal entry number (IEN) for each list item. Simply use the optional third parameter of the [SET^VALM10](#setvalm10-construct-initial-list-array) call to associate an internal entry number with your list item. You can then retrieve the associated internal entry number for any line with the code:

S Y=\$O(@VALMAR@("IDX",56,""))

10. When you are done adding lines to the list, set the [VALMCNT](#VALMCNT_Variable) variable equal to the number of items in your list.
11. You are done!

#### Setting Up Text Lines with Captions and \$\$SETFLD^VALM1

To help formatting each line of text for display, you may want to consider using captions and the [\$\$SETFLD^VALM1](#setfldvalm1-insert-text-in-a-string) API. This lets you format text in a line based on any caption items you may have set up in your List Template. In the “Caption Line Information” section of the [Workbench](#list-manager-workbenchvalmwb), you can enter caption items. Each caption item has the following:

- Name
- Length
- Column position
- Default video attributes
- Display text fields

[\$\$SETFLD^VALM1](#setfldvalm1-insert-text-in-a-string) lets you position pieces of text in your list lines based on how you set up captions for your line in the List Template.

Supposing you have set up four caption items in your List Template, named:

- “LINENO”
- “NAME”
- “INIT”
- “FM ACCESS CODE”

When you create your list array, you could loop through entries in the NEW PERSON (#200) file, and format a line to display for each NEW PERSON entry as follows:

<span id="_Toc192050641" class="anchor"></span>Figure 5: Sample NEW PERSON File Entries Line Display

S LINE=0,EN=.9 F S EN=\$O(^VA(200,EN)) Q:'+EN D

.S LINE=LINE+1

.S ZZNODE0=\$G(^VA(200,EN,0)),LINEVAR=""

.S ZZNA=\$P(ZZNODE0,U,1),ZZIN=\$P(ZZNODE0,U,2),ZZFM=\$P(ZZNODE0,U,4)

.S LINEVAR=\$\$SETFLD^VALM1(LINE\_".",LINEVAR,"<span class="mark">LINENO</span>")

.S LINEVAR=\$\$SETFLD^VALM1(ZZNA,LINEVAR,"<span class="mark">NAME</span>")

.S LINEVAR=\$\$SETFLD^VALM1(ZZIN,LINEVAR,"<span class="mark">INIT</span>")

.S LINEVAR=\$\$SETFLD^VALM1(ZZFM,LINEVAR,"<span class="mark">FM ACCESS CODE</span>")

.D SET^VALM10(LINE,LINEVAR) ; adds formatted line to list array

Now, your lines of text are set up according to your captions in your List Template. And if you adjust the positions of your List Template captions, your text lines are automatically adjusted too!

![](list-manager-1-0-developer-s-guide/017.png) NOTE: If you have a large NEW PERSON (#200) file, and you try this example, make sure you loop only through some subset of it; lists become difficult to use once there are more than a certain number of screens in the list (10 screens in a list is probably a good limit).

#### Setting and Displaying Video Attributes for List Lines with FLDCTRL^VALM10

In the “Caption Line Information” section of the [Workbench](#list-manager-workbenchvalmwb), you can enter caption items. Each caption item has the following:

- Name
- Length
- Column position
- Default video attributes
- Display text fields

This provides a way to organize your lines of text, based on caption positions.

Using the [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences) entry point, you can set the video attributes for different portions of your line based on the default video attributes entered for every caption in the line. For example, you have a caption of length 10 starting at column 40, with a default video attribute of REVERSE. If you call [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences) for a line number, all default video attributes for the line are activated, and the region of that line from column 40 to column 49 are displayed in reverse video.

To activate the default video attributes for all lines in your array, do the following:

1.  Using the [Workbench](#list-manager-workbenchvalmwb), set up caption items for each portion of your display line. Set the default video attributes as desired for each caption item.
2.  After you add each line to the list array, make a call to [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences)(line). So, you need to call [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences) once for each line you add to the array.
3.  When you run your list, each line you called [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences) is displayed with the video attributes set up in the List Template captions.

## Define List Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have created your List Template, and your list, the next step is to create actions for your list. Actions are what appear as menu items in the bottom of the List Manager screen. They allow you to launch any routine from a List Manager menu. Actions are stored as protocols, of TYPE ACTION, in the PROTOCOL (#101) file.

List Manager supplies a set of [pre-defined actions](#list-manager-generic-action-protocols) that you include with your List Manager application. It is usually a good idea to make use some of these, such as [VALM DOWN A LINE](#VALM_DOWN_A_LINE_Protocol), [VALM UP ONE LINE](#VALM_UP_ONE_LINE_Protocol), [VALM NEXT SCREEN](#VALM_NEXT_SCREEN_Protocol), etc. to provide the basic list functionality users expect.

In addition, you will probably want to define your own actions to add your own custom functionality to your list.

### How To Define an Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To define an action, do the following:

1.  From the [Workbench](#list-manager-workbenchvalmwb), choose PE for Protocol Edit.
12. Add a new protocol.
13. Set the new protocol’s TYPE to ACTION.
14. Set the ITEM TEXT field to the menu item text for this action.
15. Set the ENTRY ACTION field to call a routine that performs your action(s).
16. Use the EXIT ACTION field to set List Manager status variables *before* returning control to List Manager.
17. Add your new action-type protocol to the menu-type protocol that is the main menu for your application; this makes it a menu item in List Manager.

![](list-manager-1-0-developer-s-guide/018.png) REF: For information on how to do this, see the “[Define List Menu](#define-list-menu)” section.

The following are some more issues to consider for your actions:

- How to select items from the list in your action.
- How to determine in what Screen Mode the user is located.
- Getting control of the screen.
- What List Manager should do when your action completes.
- How to display a custom message after completing an action.

### How to Select List Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the routine called by an action, you may want to select an item or items from the List Manager list. One easy way to do this is to make a ^DIR call in your action. Set up the DIR(0) input variable to ask for numbers in the range of the entire list, or only what items are displayed on the current screen, as follows (<u>Table 7</u>):

|                                  |                                           |
|----------------------------------|-------------------------------------------|
| List Item Selection              | DIR(0) Input Variable                     |
| 1 item from entire list          | S DIR(0)="N^1:"\_VALMCNT\_":0"            |
| 1 item from current screen       | S DIR(0)="N^"\_VALMBG\_":"\_VALMLST\_":0" |
| Set of items from entire list    | S DIR(0)="L^1:"\_VALMCNT                  |
| Set of items from current screen | S DIR(0)="L^"\_VALMBG\_":"\_VALMLST       |

<span id="_Ref138229342" class="anchor"></span>Table 8: VALMBCK Variable Settings When Returning to the List Manager from a Protocol Action

The interaction with the user takes place in the lower part of the screen. From the output of the ^DIR call, you have the array number(s) of the selected item(s); you can then perform whatever action you would like with the selected item(s). If the user chooses an item or set of items (as reflected in the output variables from the ^DIR call), you can either process the items immediately, or highlight them (current screen only) for further action.

Another way to select entries is to use the List Manager entry point [EN^VALM2](#envalm2-generic-selector). This is a generic selector that prompts the user to select list items from the current screen only.

<u>Figure 6</u> is a sample of the code you could call to select a single entry using [EN^VALM2](#envalm2-generic-selector):

<span id="_Ref137731425" class="anchor"></span>Figure 6: Sample M Code Selecting Single Entry Using EN^VALM2

N ZZVALM,ZZEN

S ZZVALM="DUZ^1^ASDF^ASDF" ;?? Need to confirm how to set this up!

D EN^VALM2(ZZVALM,"O")

S ZZEN=\$O(VALMY("")) ; get line number of selected entry

I '+ZZEN W !,"No Entry Selected!" H 5 Q

W !,"You selected ",@VALMAR@(ZZEN,0) H 5

Q

### Using the Entire Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your action needs control over the entire screen, make a call to [FULL^VALM1](#fullvalm1-sets-screen-to-full-scrolling-region) at the beginning of your action’s code. This call changes the scrolling region to be the full screen, and turns word-wrap on, and all user interaction is in Scrolling Mode. When you return control back to the List Manager, set VALMBCK to “R”. This refreshes the screen and resets the scrolling region as needed by List Manager.

### When Your Action Completes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When returning to the List Manager from a protocol action, make sure the [VALMBCK](#VALMBCK_Variable) variable is set (<u>Table 8</u>). This tells List Manager what to do when returning from your action.

|               |                                                       |
|---------------|-------------------------------------------------------|
| VALMBCK Value | Description                                           |
| R         | Refresh Screen.                                       |
| \<NULL\>  | Clear bottom portion of screen and prompt for action. |
| Q         | Exit (Quit) List Manager.                         |

<span id="_Toc192050661" class="anchor"></span>Table 9: Sample Column Width Settings

If *not* defined after an action, the List Manager acts like it was set to “Q” (Quit).

If you want to display a custom message in the message window after completing an action, set the [VALMSG](#VALMSG_Variable) variable with the text desired. The message area allows up to 50 characters.

![](list-manager-1-0-developer-s-guide/019.png) REF: For more information, see the description of [MSG^VALM10](#msgvalm10-post-message-to-message-window).

## Define List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final step in building a List Manager application is to create the menu for your list. This provides the set of choices at the bottom of the List Manager screen. You can create new actions to add to your menu, and/or use generic List Manager actions as well.

### Steps to Set Up Your Application’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up your application’s menu, do the following:

1.  From the [Workbench](#list-manager-workbenchvalmwb), choose PE for Protocol Edit.
18. Add a new protocol.
19. Set the new protocol’s TYPE to MENU.
20. Set the new protocol’s COLUMN WIDTH as follows:

| \# of Columns Desired | Column Width Setting |
|-----------------------|----------------------|
| 1                     | 1                    |
| 2                     | 40                   |
| 3                     | 26                   |

<span id="_Ref192049733" class="anchor"></span>Table 10: List Manager Variables

21. Set the new protocol’s MNEMONIC WIDTH to a width that provides for the length of your longest menu item mnemonic, plus white space to separate the mnemonics from the menu text. If your longest mnemonic is 2 characters, setting this field to 4 provides 2 characters of white space.
22. Add any actions (either custom actions created by you, or [generic actions](#list-manager-generic-action-protocols)) as ITEMS to the new protocol. You can set a mnemonic and a sequence number for each item.
23. You *must* include the following code in the HEADER field of the menu protocol:

D SHOW^VALM

The [SHOW^VALM](#showvalm-display-menu-to-user) API properly displays the list of actions to the user in the “Action Area.”

24. In the MENU PROMPT field, set the text by which the users will be prompted. For example: “Select Action: ” is a good choice.
25. Once you finish editing the menu protocol, return to the [Workbench](#list-manager-workbenchvalmwb). Set the TYPE OF LIST to PROTOCOL (*not*DISPLAY!). This enables the list to use your new protocol, instead of the standard VALM DISPLAY protocol.
26. Set the PROTOCOL MENU to the name of the menu-type protocol you just created.
27. Test your new menu by choosing “Run List” from the [Workbench](#list-manager-workbenchvalmwb).

You should consider the following additional issues when setting up protocols for use by the List Manager:

- <u>Hidden Menu</u>.
- <u>Columnar Arrangement of Menu Items</u>.
- <u>Sub-Menus</u>.
- <u>Overriding the Default Action</u>.

### Hidden Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the [Workbench](#list-manager-workbenchvalmwb), you can set your list’s Hidden Menu to the name of any menu protocol. This is typically used to provide some of the more basic actions like line up and line down, especially when the main menu has a lot of custom items. By default, the [Workbench](#list-manager-workbenchvalmwb) sets up lists to use the generic [VALM HIDDEN ACTIONS](#VALM_HIDDEN_ACTIONS_Protocol) protocol as the hidden menu. This provides access to all of the generic List Manager actions for negotiating the list. You can set the hidden menu to your own hidden menu, if you wish.

### Columnar Arrangement of Menu Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the number of columns desired for your menu items is more than one and if you want to place each action in a particular column, you should use a SEQUENCE numbering scheme for the items in the menu.

List Manager displays your menu items in the minimum number of rows possible, given the number of items and the number of columns you have specified. It will place items in sequence as follows:

> 1 4 7

> 2 5 8

> 3 6 9

Knowing how List Manager places items, you can use sequencing to control in which column an item is placed.

If the number of items to appear in each column is *not* equal then you *must* add “blank” items and place the blank protocol in the appropriate column as described above.

A “blank” protocol is an action protocol with the ITEM TEXT and ENTRY ACTION fields left blank.

### Sub-Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you use a sub-menu, then the HEADER field\` of the (top menu) should contain a W “”.

### Overriding the Default Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager automatically provides a default action of “Next Screen” or “Quit”. However, you can override this default action by setting the [XQORM(“B”)](#XQORM_B_Variable) variable as part of the ENTRY ACTION code for a PROTOCOL menu.

## Fine Tune Your Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A number of ways that you can fine-tune a basic List Manager application are discussed in the following sections:

- [Entry Selection and Light Bar Scrolling](#_Ref138230068)
- [Setting Video Attributes in Your List Line](#setting-video-attributes-in-your-list-line)
- [Updating Items in the List](#updating-items-in-the-list)
- [When the User Is In Scrolling Mode (not Screen Mode)](#when-the-user-is-in-scrolling-mode-not-screen-mode)
- [Scroll-Locking Columns](#scroll-locking-columns)
- [Browsing Word-Processing Fields](#browsing-word-processing-fields)
- [Long Lists](#long-lists)
- [Calling List Manager and Other Programs from Actions](#calling-list-manager-and-other-programs-from-actions)

### Entry Selection and Light Bar Scrolling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager does *not* support a scrolling “light bar” for entry selection. When the user presses the up and down arrow keys, there is *not* a way to hook those key presses to a scrolling light bar in the list of entries.

For entry selection, the best method is to make sure that in the text of each line, the line number is shown (preferably on the left hand side of the line). Then, you can make your own call using ^DIR, or use the [EN^VALM2](#envalm2-generic-selector) generic selector, to let your users choose entries. If you want to select an entry and perform an action all at once, you can do this. Another style is to have one action that selects entries. You can then use [SELECT^VALM10](#selectvalm10-highlightsunhighlights-line-in-list) to highlight that line of the array. This is useful if there are multiple actions a user can perform on a selected entry or entries. You can let the user select the entries, highlight them, and then have the user perform actions on the set of highlighted entries.

### Setting Video Attributes in Your List Line

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One enhancement you can make to your list application is setting and changing the video attributes in your list lines.

Before you load your list, for example, you can set what the video attributes (highlight, reverse video, underline, or blinking) should be for any given caption field in a line. Do this in the List Template, by editing the Default Video Attributes for your captions. Then, when you build your array list initially, you can activate these List Template attributes for each line by making calls to [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences).

Once your list is already up and displayed, you can still change the video attributes of your lines. To change video attribute based on screen position, use [CNTRL^VALM10](#CNTRL_VALM10). You can save ([SAVE^VALM10](#savevalm10-save-current-video-attributes)) and restore ([RESTORE^VALM10](#restorevalm10-restores-video-attributes)) a line’s video attributes.

You can also select a line using [SELECT^VALM10](#selectvalm10-highlightsunhighlights-line-in-list).

### Updating Items in the List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another enhancement you can make to your list application is actively updating the lines in your list. While you *cannot* add lines to the list, you can change the contents of existing lines. This is useful, particularly if in your actions you are editing file entries, whose contents correspond to what is displayed in your list.

When a user updates an entry, you can update the corresponding list array line with a call to [FLDTEXT^VALM10](#FLDTEXT_VALM10), and then re-paint the line on the display with a call to [WRITE^VALM10](#writevalm10-re-write-line-to-screen). You can also insert text into an existing line based on caption position, using [FLDTEXT^VALM10](#FLDTEXT_VALM10).

### When the User Is In Scrolling Mode (Not Screen Mode)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [VALMCC](#VALMCC_Variable) variable is always available to indicate the user’s screen mode in List Manager:

- 1—Screen Mode
- 0—Scrolling Mode

If the user is signed on to the system using a terminal type that does *not* support the cursor control fields needed by the List Manager, List Manager automatically defaults to Scrolling Mode. This means that the list array and headers will always be totally re-painted to the screen after each action.

There may be times that the application code needs to know if the job is in Scrolling Mode. For example, if only one field in one entry is to be changed as a result of an action and the user was working totally in the “Action Area” of the screen, then the code could simply use the appropriate call to update just that field and set the [VALMBCK](#VALMBCK_Variable) variable to NULL. However, if the user is in Scrolling Mode, then you would *not* update the screen and would set the [VALMBCK](#VALMBCK_Variable) variable to “R”.

### Scroll-Locking Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your list display is going to be more than fits on a user’s screen (greater than 80 or 132 columns), you can set a Scroll Lock, so that to the left of the Scroll Lock, no scrolling occurs. This feature is based on caption fields (another good reason to set up your lines using caption fields). You can only set one caption field as the point at which no scrolling occurs. That field, and everything to the left of it, is stationary when the user scrolls the rest of the list to the right.

### Browsing Word-Processing Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is easy to browse word-processing fields using List Manager. Set the TYPE of your template to DISPLAY. This provides a menu of standard actions (line up, line down, etc.). Then, for the array, simply set the [ARRAY NAME](#array-name-107-optional) field to the global location of your word-processing field. List Manager expects the array to be in the format of a word-processing field, so at that point you are done.

You can also launch the VA FileMan Browser from within List Manager to browse a word-processing field or global array. As different mix of features is offered when browsing word-processing fields with the VA FileMan browser.

### Long Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should not use List Manager to display very long lists of entries. Although there is no limit other than that of system resources on the size of a list, you may find that users have difficulty if there are more than, for example, 10 screens in the list. The exact limit on the number of screens can depend on the type of information in the list, and how willing your user is to go through such a list. At some point, performance also becomes a consideration, especially if you are building your list array.

### Calling List Manager and Other Programs from Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From an action in your List Manager application, you can call List Manager again. It is re-entrant. You can also call other applications, for example ScreenMan, the VA FileMan Browser. You do *not* need to NEW any variables when calling these applications.

## Export Your List Manager Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0’s Kernel Installation and Distribution System (KIDS) made List Manager templates and protocols standard package components. This enables List Manager applications to be distributed just like any other package, using KIDS.

To export your List Manager application, you need to export your application’s protocols and your application’s List Template, as well as routines, options, and any other supporting components.

![](list-manager-1-0-developer-s-guide/020.png) REF: For more information on KIDS, see the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* and *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Kernel 8.0’s Kernel Installation and Distribution System (KIDS), you can include protocols as package components in a KIDS build. You can then export your List Manager application in a KIDS build.

![](list-manager-1-0-developer-s-guide/021.png) REF: For more information on KIDS, see the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* and *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

Prior to Kernel 8.0, in order to export protocols, you would have needed to use the ORVOM tool.

![](list-manager-1-0-developer-s-guide/022.png) REF: For more information of the ORVOM process, see the *Order Entry/Results Reporting Developer’s Guide*.

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Kernel 8.0’s Kernel Installation and Distribution System (KIDS), and with Kernel patch XU\*8.0\*2 installed, you can include List Templates as package components in a KIDS build. You can then export your List Manager application in a KIDS build.

![](list-manager-1-0-developer-s-guide/023.png) REF: For more information on KIDS, see the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* and *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

### Before Kernel 8.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to Kernel 8.0, in order to export List Templates, you would have needed to use the ^VALMW3 List Manager utility.

## Example Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### LIST TEMPLATE PROTOCOL MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 7</u> is an example of a protocol menu that would be attached to a List Template that has a TYPE of PROTOCOL.

<span id="_Ref137734162" class="anchor"></span>Figure 7: Sample Protocol Menu Attached to a List Template with TYPE of PROTOCOL

NAME: SDAM MENU

ITEM TEXT: Appointment Management

TYPE: menu

PACKAGE: SCHEDULING

DESCRIPTION: This menu contains all the activities for the appointment management option.

COLUMN WIDTH: 26

MNEMONIC WIDTH: 4

ITEM: SDAM APPT CHECK IN MNEMONIC: CI SEQUENCE: 11

ITEM: SDAM APPT UNSCHEDULED MNEMONIC: UN SEQUENCE: 12

ITEM: SDAM APPT MAKE MNEMONIC: MA SEQUENCE: 13

ITEM: SDAM APPT CANCEL MNEMONIC: CA SEQUENCE: 21

ITEM: SDAM APPT NO-SHOW MNEMONIC: NS SEQUENCE: 22

ITEM: SDAM LIST MENU MNEMONIC: AL SEQUENCE: 23

ITEM: SDAM PATIENT CHANGE MNEMONIC: PT SEQUENCE: 31

ITEM: SDAM CLINIC CHANGE MNEMONIC: CL SEQUENCE: 32

ITEM: SDAM DATE CHANGE MNEMONIC: CD SEQUENCE: 33

HEADER: D SHOW^VALM

MENU PROMPT: Select Action:

### PROTOCOL Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PROTOCOL menu is a sub-menu of the SDAM APPOINTMENT MENU. Please note the header (<u>Figure 8</u>).

<span id="_Ref138231043" class="anchor"></span>Figure 8: Sample Protocol Menu

NAME: SDAM LIST MENU

ITEM TEXT: Appointment Lists

TYPE: menu

PACKAGE: SCHEDULING

COLUMN WIDTH: 40

ITEM: SDAM LIST CHECKED IN MNEMONIC: CI

ITEM: SDAM LIST NO SHOWS MNEMONIC: NS

ITEM: SDAM LIST ALL MNEMONIC: TA

ITEM: SDAM LIST NO ACTION MNEMONIC: NA

ITEM: SDAM LIST CANCELLED MNEMONIC: CA

ITEM: SDAM LIST FUTURE MNEMONIC: FU

ITEM: SDAM LIST INPATIENT MNEMONIC: IP

ITEM: SDAM LIST NON-COUNT MNEMONIC: NC

EXIT ACTION: S:'\$D(VALMBCK) VALMBCK="" D EXIT^SDAM

ENTRY ACTION: S XQORM(0)="1A"

HEADER: W ""

MENU PROMPT: Select List:

MENU DEFAULT: No Action Taken

### PROTOCOL Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 9</u> is sample PROTOCOL action:

<span id="_Ref138231122" class="anchor"></span>Figure 9: Sample PROTOCOL Action

NAME: SDAM LIST CANCELLED

ITEM TEXT: Cancelled

TYPE: action

PACKAGE: SCHEDULING

DESCRIPTION: This list will display all the cancelled appointments for the date range specified.

ENTRY ACTION: S X="CANCELLED" D LIST^SDAM

Appendix B - Sample List Template File Entries

PROTOCOL TYPE

NAME: SDAM APPT MGT

TYPE OF LIST: PROTOCOL

HIDDEN PROTOCOL MENU: VALM HIDDEN ACTIONS

LEFT MARGIN: 1

RIGHT MARGIN: 80

TOP MARGIN: 5

BOTTOM MARGIN: 14

RIGHT MARGIN: 80

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

ENTITY NAME: Appointment

PROTOCOL MENU: SDAM MENU

SCREEN TITLE: Appt Mgt Module

ALLOWABLE NUMBER OF ACTIONS: 1

DATE RANGE LIMIT: 999

ARRAY NAME: ^TMP("SDAM",\$J)

ITEM NAME: NAME COLUMN: 9 WIDTH: 22 DISPLAY TEXT: Patient or Clinic

ITEM NAME: DATE COLUMN: 32 WIDTH: 20 DISPLAY TEXT: Appt Date/Time

ITEM NAME: STAT COLUMN: 53 WIDTH: 22 DISPLAY TEXT: Status

ITEM NAME: APPT# COLUMN: 5 WIDTH: 3

ITEM NAME: TIME COLUMN: 75 WIDTH: 5

EXPAND CODE: D EN^SDAMEP

EXIT CODE: D FNL^SDAM

HEADER CODE: D HDR^SDAM

HELP CODE: D HLP^SDAM5

ENTRY CODE: D INIT^SDAM

### DISPLAY TYPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 10</u> is a sample DISPLAY type:

<span id="_Ref138231270" class="anchor"></span>Figure 10: Sample DISPLAY Type

NAME: SDAM APPT PROFILE

TYPE OF LIST: DISPLAY

HIDDEN PROTOCOL MENU: VALM HIDDEN ACTIONS

TOP MARGIN: 5

BOTTOM MARGIN: 17

RIGHT MARGIN: 80

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

SCREEN TITLE: Expanded Profile

ALLOWABLE NUMBER OF ACTIONS: 2

ARRAY NAME: ^TMP("SDAMEP",\$J)

EXIT CODE: D FNL^SDAMEP

HEADER CODE: D HDR^SDAMEP

HELP CODE: D HLP^SDAM5

ENTRY CODE: D INIT^SDAMEP

### Application Code Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 11</u> is an example of List Manager application code:

<span id="_Ref137734763" class="anchor"></span>Figure 11: Sample List Manager Application Codes

SDAM ;; - main code

EN ; -- main entry point

K XQORS,VALMEVL D EN^VALM("SDAM APPT MGT")

Q

;

INIT ; -- set up appt man vars and list man array and other vars

K I,X,SDBEG,SDEND,SDB,XQORNOD,SDFN,SDCLN,DA,DR,DIE,DNM,DQ

S DIR(0)="43,213",DIR("A")="Select Patient name or Clinic name"

D ^DIR K DIR I \$D(DIRUT) S VALMQUIT="" G INITQ

S SDY=Y

I SDY\["DPT(" S SDAMTYP="P",SDFN=+SDY D INIT^SDAM1

I SDY\["SC(" S SDAMTYP="C",SDCLN=+SDY D INIT^SDAM3

INITQ Q

;

HDR ; -- screen header set up

N X

I SDAMTYP="P" D HDR^SDAM10

I SDAMTYP="C" D HDR^SDAM3

S X=\$P(SDAMLIST,"^",2)

S VALMHDR(2)=\$\$SETSTR^VALM1(\$\$FDATE^VALM1(SDBEG)\_" thru "\_\$\$FDATE^SSDEND),X,59,22)

Q

;

FNL ; -- what to do upon exiting list man

K ^TMP("SDAM",\$J),^TMP("SDAMIDX",\$J),^TMP("VALMIDX",\$J)

K SDAMCNT,SDFLDD,SDACNT,VALMHCNT,SDPRD,SDFN,SDCLN,SDAMLIST,SDT,SDAT

EG,SDEND,DFN,Y,SDAMTYP,SDY,X,SDCL,Y,SDDA,VALMY

Q

HLP ; -- help for list

I \$D(X),X'\["??" D HLPS,PAUSE^VALM1 G HLPQ

D CLEAR^VALM1

F I=1:1 S SDX=\$P(\$T(HELPTXT+I),";",3,99)

Q:SDX="\$END"

D PAUSE^VALM1:SDX="\$PAUSE" Q:'Y W !,\$S(SDX\["\$PAUSE":"",1:SDX)

W !,"Possible actions are the following:"

D HLPS,PAUSE^VALM1 S VALMBCK="R"

HLPQ K SDX,Y Q

;

HLPS ; -- short help

S X="?" D DISP^XQORM1 W ! Q

;

HELPTXT ; -- help text

;;Enter actions(s) by typing the name(s), or abbreviation(s).

;;

;;ACTION PRE-SELECTION:

;; Actions may be pre-selected by separating them with ";".

;; .

;; .

;; .

SDAMEP ;; - expand code

EN ; Selection of appointment

K ^TMP("SDAMEP",\$J)

S VALMBCK=""

D SEL G ENQ:'\$D(SDW)!(SDERR)

W ! D WAIT^DICD,EN^VALM("SDAM APPT PROFILE")

S VALMBCK="R"

ENQ Q

VALMD ;List Manager Sample Routine; APR 2, 1992

;

EN ; -- option entry point

K XQORS,VALMEVL

D EN^VALM("VALM DEMO APPLICATION")

ENQ Q

;

;

INIT ; -- build array

W ! S DIC("A")="Select Package:",DIC="^DIC(9.4,",DIC(0)="AEMQ" D ^DIC K DIC

I Y\<0 S VALMQUIT="" G INITQ

PKG ; -- entry pt if package known

N VALMX,VALMCNTI,VALMPRO,VALMIFN,X,VALMPRE,Z

S VALMPKG=+Y

D CLEAN^VALM10

S (VALMCNTI,VALMCNT)=0,(VALMPRE,VALMPRO)=\$P(\$G(^DIC(9.4,VALMPKG,0)),U,2)

F S VALMPRO=\$O(^ORD(101,"B",VALMPRO))

Q:\$E(VALMPRO,1,\$L(VALMPRE))'=VALMPRE

S VALMIFN=0 F S VALMIFN=\$O(^ORD(101,"B",VALMPRO,VALMIFN)) Q:'VALMIFN I \$D(^ORD(101,VALMIFN,0)) S VALMX=^(0) D

.S VALMCNTI=VALMCNTI+1 W:(VALMCNTI#10)=0 "."

.S X=\$\$SETFLD^VALM1(VALMCNTI,"","NUMBER")

.S X=\$\$SETFLD^VALM1(\$P(VALMX,U),X,"NAME")

.S X=\$\$SETFLD^VALM1(\$P(VALMX,U,2),X,"TEXT") K Z S \$P(Z,\$E(VALMCNTI),240)=""

.S VALMCNT=VALMCNT+1

.D SET^VALM10(VALMCNT,\$E(X_Z,1,240),VALMCNTI) ; set text

.S ^TMP("VALMZIDX",\$J,VALMCNTI)=VALMCNT_U_VALMIFN

.D:'(VALMCNT#9) FLDCTRL^VALM10(VALMCNT) ; defaults for all fields

.D FLDCTRL^VALM10(VALMCNT,"NUMBER") ; default for 1 field

.D:'(VALMCNT#5) FLDCTRL^VALM10(VALMCNT,"NAME",IOUON,IOUOFF) ; adhoc

D NUL:'VALMCNT

INITQ Q

;

HDR ; -- demo header

N VALMX

S VALMX=\$G(^DIC(9.4,VALMPKG,0)),X=" Package:"\_\$P(VALMX,U)

S VALMHDR(1)=\$\$SETSTR^VALM1("Prefix:"\_\$P(VALMX,U,2),X,63,15)

S VALMHDR(2)="Description: "\_\$E(\$P(VALMX,U,3),1,65)

Q

;

NUL ; -- set null message

I 'VALMCNT D

.F X=" "," No protocols to list." S VALMCNT=VALMCNT+1 D SET^VALM10(VALMCNT,X)

.S ^TMP("VALMZIDX",\$J,1)=1,^(2)=2

Q

;

FNL ; -- clean up

K DIE,DIC,DR,DA,DE,DQ,VALMY,VALMPKG,^TMP("VALMZIDX",\$J)

D CLEAN^VALM10

Q

;

EXP ; -- expand action

D FULL^VALM1

N VALMI,VALMAT,VALMY

D EN^VALM2(XQORNOD(0),"O") S VALMI=0

F S VALMI=\$O(VALMY(VALMI)) Q:'VALMI D

.S VALMAT=\$G(^TMP("VALMZIDX",\$J,VALMI))

.W !!,@VALMAR@(+VALMAT,0),!

.S DA=+\$P(VALMAT,U,2),DIC="^ORD(101,",DR="0"

D EN^DIQ,PAUSE^VALM1

S VALMBCK="R"

Q

;

EDIT ; -- edit action

N VALMA,VALMP,VALMI,VALMAT,VALMY

D EN^VALM2(XQORNOD(0),"O") S VALMI=0 ; allow the user to "O"ptionally answer

F S VALMI=\$O(VALMY(VALMI)) Q:'VALMI D

.D SELECT^VALM10(VALMI,1) ; -- 'select' line

.S VALMAT=\$G(^TMP("VALMZIDX",\$J,VALMI))

.W !!,@VALMAR@(+VALMAT,0)

.S DA=+\$P(VALMAT,U,2),VALMP=\$G(^ORD(101,DA,0)),DIE=19,DR="1" D ^DIE K DIE,DR

.S VALMA=\$G(^ORD(101,DA,0))

.I \$P(VALMP,U,2)'=\$P(VALMA,U,2) D UPD(\$P(VALMA,U,2),"TEXT",.VALMAT)

.D SELECT^VALM10(VALMI,0) ; -- 'de-select' line

S VALMBCK=\$S(VALMCC:"",1:"R")

Q

;

DESC ; -- display description action

N VALMI,VALMY,VALMAT

D EN^VALM2(XQORNOD(0),"OS") S VALMI=0 ; select only a "S"ingle protocols

F S VALMI=\$O(VALMY(VALMI)) Q:'VALMI D

.S VALMAT=+\$P(\$G(^TMP("VALMZIDX",\$J,VALMI)),U,2)

.I '\$D(^ORD(101,VALMAT,1)) W !!,"No Description entered." D AUSE^VALM1 Q

.D WP^VALM("^ORD(101,"\_VALMAT\_",1)",\$P(\$G(^ORD(101,VALMAT,0)),U))

S VALMBCK="R"

Q

;

UPD(TEXT,FLD,VALMAT) ; -- update data for screen

D:VALMCC FLDCTRL^VALM10(+VALMAT,.FLD,.IOINHI,.IOINORM,1)

D FLDTEXT^VALM10(+VALMAT,.FLD,.TEXT)

Q

;

CHG ; -- change package action

K X I \$D(XQORNOD(0)) S X=\$P(\$P(XQORNOD(0),U,4),"=",2)

I X="" R !!,"Select Package: ",X:DTIME

S DIC="^DIC(9.4,",DIC(0)="EMQ" D ^DIC K DIC G CHG:X\["?"

I Y\<0 D G CHGQ

.W !!,\*7,"Package has not been changed."

.W ! S DIR(0)="E" D ^DIR K DIR

.S VALMBCK=""

D PKG,HDR S VALMBCK="R" S VALMBG=1

CHGQ Q

<u>Figure 12</u> is an example of a stub routine created when adding a new List Template using the [Workbench](#list-manager-workbenchvalmwb).

<span id="_Ref137734698" class="anchor"></span>Figure 12: Sample Stub Routines When Adding New List Templates with the Workbench

ZZDEMO ;; 24-JAN-1993

;; ;

EN ; -- main entry point for DOCUMENTATION DEMO

D EN^VALM("DOCUMENTATION DEMO")

Q

;

HDR ; -- header code

S VALMHDR(1)="This is a test header for DOCUMENTATION DEMO."

S VALMHDR(2)="This is the second line"

Q

;

INIT ; -- init variables and list array

F LINE=1:1:30 D SET^VALM10(LINE,LINE\_" Line number"\_LINE)

S VALMCNT=30

Q

;

HELP ; -- help code

S X="?" D DISP^XQORM1 W !!

Q

;

EXIT ; -- exit code

Q

;

EXPND ; -- expand code

Q

;

# List Template Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Demographics Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields are demographic fields:

- [NAME (#.01)](#name-.01)
- [ENTITY NAME (#.09)](#entity-name-.09-optional)
- [SCREEN TITLE (#.11)](#screen-title-.11-optional-but-recommended-screen-title-field)

#### NAME (#.01)

Name of the List Template. The template should be namespaced.

#### ENTITY NAME (#.09) \[Optional\]

This field contains the term that is displayed to the user that best describes the items in the list. This field is used by the select entry point ([EN^VALM2](#envalm2-generic-selector)).

#### SCREEN TITLE (#.11) \[Optional but Recommended\] Screen Title Field

This field contains the text that is displayed/printed in the upper, left-hand corner of the screen display.

The screen title can be changed at run time by setting the [VALM(“TITLE”)](#VALM_TITLE_Variable) variable during [ENTRY CODE](#entry-code-106) or action processing. If you have one basic List Template definition that could be used for more than one application, then setting the [VALM(“TITLE”)](#VALM_TITLE_Variable) variable allows you to re-use the template but change the title as it appears to the user.

### Protocol Information Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields are protocol information fields:

- [TYPE OF LIST (#.02)](#type-of-list-.02)
- [PROTOCOL MENU (#.1)](#protocol-menu-.1)
- [PRINT PROTOCOL (#1.01)](#print-protocol-1.01-optional)
- [HIDDEN MENU (#1.02)](#hidden-menu-1.02-optional-but-recommended)

#### TYPE OF LIST (#.02)

Indicates the type of List Template. The type determines what actions are presented to the user:

- PROTOCOL—Uses the menu protocol specified in the PROTOCOL MENU field.
- DISPLAY—Uses the standard VALM DISPLAY PROTOCOL supplied by the List Manager.

#### PROTOCOL MENU (#.1)

This field contains the name of the protocol menu that is used by the List Manager if the [TYPE OF LIST (#.02)](#type-of-list-.02) fields is “PROTOCOL”. This field is *not* used for “DISPLAY” types.

#### PRINT PROTOCOL (#1.01) \[Optional\]

This field contains the name of the protocol that is called when the user selects the generic Print List action. Normally, this field is blank, and the generic printing action is sufficient.

#### HIDDEN MENU (#1.02) \[Optional but *Recommended*\]

This field contains the name of the protocol menu that the List Manager uses for the “hidden” actions available to the user. Normally, the application enters the [VALM HIDDEN ACTIONS](#VALM_HIDDEN_ACTIONS_Protocol) menu in this field. However, there may be applications that would require a different set of “hidden” actions.

If the List Template has a “hidden” menu defined the List Manager automatically displays help for the hidden menu when the user enters “??”.

### List Region Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields are list region fields:

- [TOP MARGIN (#.05)](#top-margin-.05)
- [BOTTOM MARGIN (#.06)](#bottom-margin-.06)
- [RIGHT MARGIN (#.04)](#right-margin-.04-optional)

#### TOP MARGIN (#.05)

This field contains the number of the top row of the scrolling region where the list is displayed.

#### BOTTOM MARGIN (#.06)

This field contains the number of the bottom row of the scrolling region where the list is displayed.

#### RIGHT MARGIN (#.04) \[Optional\]

This field indicates the maximum number of characters a row can contain. If this parameter is *not* set, 80 is used as the default. Range is 80 to 240 characters.

### Other Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are other fields:

- [OK TO TRANSPORT ? (#.07)](#ok-to-transport-.07)
- [USE CURSOR CONTROL (#.08)](#use-cursor-control-.08)
- [ALLOWABLE NUMBER OF ACTIONS (#.12)](#allowable-number-of-actions-.12)
- [DATE RANGE LIMIT (#.13)](#date-range-limit-.13-optional)
- [AUTOMATIC DEFAULTS (#.14)](#automatic-defaults-.14-optional)

#### OK TO TRANSPORT ? (#.07)

This field indicates to the transport utility if this List Template should be distributed.

![](list-manager-1-0-developer-s-guide/024.png) NOTE: This field is obsolete now that KIDS is used to transport List Manager applications.  
  
REF: For more information on KIDS, see the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* and *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

#### USE CURSOR CONTROL (#.08)

This field indicates whether the cursor positioning and character enhancement capabilities of the device should be used. If set to “NO”, then lists are presented in Scrolling Mode.

#### ALLOWABLE NUMBER OF ACTIONS (#.12)

This field indicates the number of actions a user can select at one time.

For example, if this parameter is set to 1, then the user can only enter one action:

- Allowed: Select Action: NX
- *Not* Allowed: Select Action: NX,EP

If this parameter is *not* entered, then the system defaults to 1.

#### DATE RANGE LIMIT (#.13) \[Optional\]

This field contains the maximum number of days that can be specified by the user while entering a date range. This parameter is only used if the applications calls the List Manager’s date range entry point ([RANGE^VALM1](#rangevalm1-change-date-range)).

#### AUTOMATIC DEFAULTS (#.14) \[optional\]

This field indicates whether List Manager should always supply a default action at the “Select” prompt for “PROTOCOL” type List Templates.

If set to “NO”, a default is *not* provided automatically. It is your responsibility to indicate a default, if desired. This default can be indicated by setting the [XQORM(“B”)](#XQORM_B_Variable) variable as part of the PROTOCOL menu’s [HEADER CODE](#header-code-100). For example:

D SHOW^VALM S XQORM("B")="Your action")

This parameter is only valid for “PROTOCOL” type List Templates.

If the parameter is set to “YES” or is blank, a default is provided by List Manager. If the current screen contains the last line in the list, then the default will be “Quit”; otherwise, it will be "Next Screen". However, as discussed above, you can override this default by setting the [XQORM(“B”)](#XQORM_B_Variable) variable.

### MUMPS Code Related Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are MUMPS code related fields:

- [HEADER CODE (#100)](#header-code-100)
- [ENTRY CODE (#106)](#entry-code-106)
- [EXIT CODE (#105)](#exit-code-105-optional-but-recommended)
- [EXPAND CODE (#102)](#expand-code-102-optional)
- [HELP CODE (#103)](#help-code-103-optional)
- [ARRAY NAME (#107)](#array-name-107-optional)

#### HEADER CODE (#100)

This MUMPS field contains the code that the List Manager executes to create the application-specific screen header array. This header *must* be stored in the [VALMHDR()](#VALMHDR_Variable) variable.

The subscripting for [VALMHDR()](#VALMHDR_Variable) is a simple integer number. For example:

S VALMHDR(1) = "This is the 1st line of the header"

S VALMHDR(2) = "This is the 2nd line of the header"

During action processing, if the header needs to be changed, you can KILL [VALMHDR](#VALMHDR_Variable) and then SET [VALMBCK](#VALMBCK_Variable)=“R”. This causes List Manager to automatically invoke this HEADER CODE, as part of the re-display of the screen.

#### ENTRY CODE (#106)

This field contains MUMPS code that is executed when the List Manager is called. This code is usually used by the application to initialize variables. Any application-specific variables should also be set up here.

List Manager variables to be initialized are:

- [VALMCNT](#VALMCNT_Variable) \[Required\]—The number of lines in the list.
- [VALMBG](#VALMBG_Variable) \[Optional\]—The number of the line you want the List Manager to start displaying from a line other than 1. If *not* defined, it will be set to 1 by List Manager.
- [VALMQUIT](#VALMQUIT_Variable) \[Optional\]—If during the building of the array, the software determines that the List Manager application *cannot* continue, this variable should be set. Setting this variable causes the List Manager to quit the current List Manager application.

The array specified in the [ARRAY NAME](#array-name-107-optional) field is also set up at this time. This array contains the list of items to display. The subscripting of the array should conform to VA FileMan word-processing format.

For example: If [ARRAY NAME](#array-name-107-optional) equals ^TMP(“SDTEST”,\$J), then the list would be stored as follows:

^TMP("SDTEST",\$J,1,0) = " 1 Valmuser,One "

^TMP("SDTEST",\$J,2,0) = " 2/2/93@0800am"

If you plan to use the entry selection call, [EN^VALM2](#envalm2-generic-selector), then the following *must* also be set:

^TMP("SDTEST",\$J,"IDX",\<line \#\>,\<entry \#\>) = ""

The “line \#” corresponds to the 1 and 2 shown in the above example. The “entry \#” corresponds to an entry in your application. In the example, the two lines each correspond to appointment entry number. So, the “IDX” nodes would be set up in the following manner:

^TMP("SDTEST",\$J,"IDX",1,1)=""

^TMP("SDTEST",\$J,"IDX",2,1)=""

![](list-manager-1-0-developer-s-guide/025.png) REF: For more information on that List Template field, see the [ARRAY NAME](#array-name-107-optional) field.

#### EXIT CODE (#105) \[optional but recommended\]

This field contains MUMPS logic that the List Manager executes when the user exits the list. This should be used to clean up variables and any other exit processing the application needs to perform.

#### EXPAND CODE (#102) \[optional\]

This field contains the MUMPS code that displays a detailed inquiry-type report/screen for a specific entry in the list. If this field is filled in, then the standard “DISPLAY” protocol has an “EXPANDED” action.

The standard VALM EXPAND protocol uses this field to expand an entry. If the [TYPE OF LIST](#type-of-list-.02) is PROTOCOL, then add the VALM EXPAND protocol to your custom protocol menu and enter the code in this EXPAND CODE (#102) field.

A possible method for expand is to create another List Template that is a DISPLAY type. You need only build the display array and set this EXPAND CODE (#102) field to be another call to the List Manager, passing in the display template name.

#### HELP CODE (#103) \[optional\]

This field contains the MUMPS code for custom application help. This code is executed when the user types a “?” at the “Select Action: ” prompt.

This field is optional. If this field is left blank, the normal help given by the XQOR\* driver takes effect.

If the List Template has a “hidden” menu defined the List Manager automatically displays help for the hidden menu when the user enters “??”.

#### ARRAY NAME (#107) \[optional\]

This field contains the name of the array that holds the list of items to be displayed. The code specified in the [ENTRY CODE](#entry-code-106) (#106) field *must* create this array initially.

![](list-manager-1-0-developer-s-guide/026.png) NOTE: The array name *must* be preceded by a space character. This is needed to allow global specification. VA FileMan does *not* allow “^” as the first character. The array can be either a local or global variable.

The array needs to follow the format used in word-processing fields (e.g., ^TMP(“SDAM”,\$J,line \#,0)=string).

Finally, you do *not* have to indicate the array in which the list will be located. By making calls to [SET^VALM10](#setvalm10-construct-initial-list-array), you can have the List Manager decide where to store the list array. If you need to reference lines in the array, the use of the @VALMAR@(\<line \#\>,0) syntax is supported. This feature is ideal for a short list of items(e.g., \<10 items).

### Caption Line Information Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="CAPTION_LINE_COLUMNS" class="anchor"></span>The following are caption line information fields:

- [CAPTION LINE COLUMNS (#200)](#CAPTION_LINE_COLUMNS)
- [ITEM NAME (#.01)](#item-name-.01)
- [COLUMN (#.02)](#column-.02)
- [WIDTH (#.03)](#width-.03)
- [DISPLAY TEXT (#.04)](#display-text-.04-optional)
- [DEFAULT VIDEO ATTRIBUTES (#.05)](#default-video-attributes-.05-optional)
- [SCROLL LOCK (#.06)](#scroll-lock-.06-optional)

#### CAPTION LINE COLUMNS (#200) \[Optional\]

This Multiple field contains column definitions for the data displayed in the list. Adding entries to this Multiple is optional. The column parameters are used when the List Manager writes the line indicating the top of the list’s scrolling region.

#### ITEM NAME (#.01)

This field contains the reference name of the column. The [DISPLAY TEXT](#display-text-.04-optional) field contains the text that is used when the caption line is written. The text in this field is used when the application refers to this column during programming.

#### COLUMN (#.02)

This field contains the column number where the data/caption starts.

#### WIDTH (#.03)

This field contains the number of characters this field uses.

#### DISPLAY TEXT (#.04) \[optional\]

This field contains the text that appears on the caption line for this column/field. If the text is longer than the WIDTH parameter, it is truncated to the WIDTH specification when written as part of the caption line. This field is optional and can be left blank.

#### DEFAULT VIDEO ATTRIBUTES (#.05) \[optional\]

This parameter allows you to indicate the default video attributes that should be applied when program calls are made to the [FLDCTRL^VALM10](#fldctrlvalm10-activate-video-control-sequences) entry point.

The following is the list of attributes and abbreviations used for this parameter:

- H—Highlight
- R—Reverse video
- U—Underline
- B—Blinking

#### SCROLL LOCK (#.06) \[Optional\]

If you want to lock one for more columns into place as the user scrolls horizontally through the list, you can place a “Scroll Lock” on the right most column field that should be locked in place on the screen. Only one column can have this “Scroll Lock” parameter set to “YES”. If you attempt to set more than one, the system does *not* allow it and issues a warning.

If this parameter is set to “YES”, this caption field and any other caption field, with a COLUMN parameter set to less than this current caption fields, the List Manage always displays it.

This parameter does *not* need to be filled in for List Templates with a [RIGHT MARGIN](#right-margin-.04-optional) of 80. For those templates with a [RIGHT MARGIN](#right-margin-.04-optional) of over 80, this field also does *not* need to be entered. However, the use of this field allows you to indicate the list’s identification fields for user readability.

Only one caption field can have this parameter set to “YES”.

The local array [VALMDDF()](#VALMDDF_Variable) is available to you at run time. This array is subscripted by the column field’s name and contains information described above:

VALMDDF(\<column name\>)=\<column name\> ^ \<column\> ^ \<width\> ^ \<caption\> ^ \<video\> ^ \<scroll lock\>

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List Manager Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists all of the variables within List Manager that you can either set or refer to in your List Manager application code.

<table>
<caption><p><span id="_Ref137651978" class="anchor"></span>Table 11: Kernel Video Variables</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="VALM_TITLE_Variable" class="anchor"></span><strong>VALM(TITLE)</strong></td>
<td>The screen title can be changed at run time by setting this variable, during ENTRY CODE or action processing. If you are one basic List Template definition that could be used for more than one application, then setting <strong>VALM("TITLE")</strong> allows you to re-use the template but change the title as it appears to the user.</td>
</tr>
<tr class="even">
<td><span id="VALMBCK_Variable" class="anchor"></span><strong>VALMBCK</strong></td>
<td><p>When returning to the List Manager from a protocol action, you should set the <strong>VALMBCK</strong> variable. This tells List Manager what to do when returning from an action. If <em>not</em> defined after an action, List Manager acts as if it was set to "<strong>Q</strong>":</p>
<ul>
<li><p><strong>R—</strong>Refresh screen.</p></li>
<li><p><strong>NULL—</strong>Clear bottom portion of screen and prompt for action.</p></li>
<li><p><strong>Q—</strong>Exit (<strong>Quit</strong>) List Manager.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="VALMBG_Variable" class="anchor"></span><strong>VALMBG</strong></td>
<td><p>An optional variable you can set in the <a href="#init_outline_routine_tag"><strong>INIT</strong></a> code that sets up your list. This tells List Manager what line in your list to start displaying the list in (default is line <strong>1</strong>).</p>
<p>In action protocols, you can also refer to the value of this variable to find the number of the first list line currently displayed on the user’s screen.</p></td>
</tr>
<tr class="even">
<td><span id="VALMCC_Variable" class="anchor"></span><strong>VALMCC</strong></td>
<td><p>Always available to indicate the user’s screen mode:</p>
<ul>
<li><p><strong>1—</strong>Screen Mode.</p></li>
<li><p><strong>0—</strong>Scrolling Mode.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="VALMCNT_Variable" class="anchor"></span><strong>VALMCNT</strong></td>
<td>The number of the lines in the list. In the <a href="#init_outline_routine_tag"><strong>INIT</strong></a> code that sets up the list, you <em>must</em> set <strong>VALMCNT</strong> equal to the number of lines in your list.</td>
</tr>
<tr class="even">
<td><span id="VALMDDF_Variable" class="anchor"></span><strong>VALMDDF()</strong></td>
<td><p>This array is available at runtime. It is subscripted by caption field name, so there is one node per caption field in your List Template. Each node contains the following ^-pieces:</p>
<ul>
<li><p>Caption field name</p></li>
<li><p>Column</p></li>
<li><p>Width</p></li>
<li><p>Caption</p></li>
<li><p>Video (if defined)</p></li>
<li><p>Scroll Lock (if defined)</p></li>
</ul>
<p>For example:</p>
<p><strong>VALMDDF("INIT")=INIT^37^5^Init.</strong></p>
<p><strong>VALMDDF("NAME")=NAME^1^35^ Name^</strong></p></td>
</tr>
<tr class="odd">
<td><span id="VALMHDR_Variable" class="anchor"></span><strong>VALMHDR()</strong></td>
<td><p>The header is stored in <strong>VALMHDR()</strong>. The subscripting for <strong>VALMHDR()</strong> is a simple integer number. For example:</p>
<p><strong>S VALMHDR(1) = "1st line of header"</strong></p>
<p><strong>S VALMHDR(2) = "2nd line of header"</strong></p>
<p>During action processing, if the header needs to be changed, you can <strong>KILL VALMHDR</strong> and then <strong>SET <a href="#VALMBCK_Variable">VALMBCK</a>="R"</strong>. This causes List Manager to automatically invoke what is called by the <a href="#header-code-100">HEADER CODE</a> (#100) field as part of the re-display of the screen.</p></td>
</tr>
<tr class="even">
<td><strong>VALMLST</strong></td>
<td>In action protocols, you can refer to the value of this variable to find the number of the last list line currently displayed on the user’s screen.</td>
</tr>
<tr class="odd">
<td><span id="VALMQUIT_Variable" class="anchor"></span><strong>VALMQUIT</strong></td>
<td>If in the <a href="#init_outline_routine_tag"><strong>INIT</strong></a> code, while building a list, you decide that List Manager should <em>not</em> continue, set the <strong>VALMQUIT</strong> variable to tell List Manager to <strong>Quit</strong>.</td>
</tr>
<tr class="even">
<td><span id="VALMSG_Variable" class="anchor"></span><strong>VALMSG</strong></td>
<td>To display a custom message in the message window after completing an action, set this variable with the desired text (up to <strong>50 characters</strong>).</td>
</tr>
<tr class="odd">
<td><strong>@VALMAR@(#,0)</strong></td>
<td>If you built your array using <a href="#setvalm10-construct-initial-list-array">SET^VALM10</a>, you can use the <strong>@VALMAR@(line#,0)</strong> syntax to reference text lines in the array.</td>
</tr>
<tr class="even">
<td><span id="VALMAR_IDX_Variable" class="anchor"></span><strong>@VALMAR@("IDX")</strong></td>
<td><p>Location of entry index when you set up an array using <a href="#setvalm10-construct-initial-list-array">SET^VALM10</a>, and pass index entries with each line. The relationship of the list line to the indexed value stored in the global referenced by <strong>@VALMAR@("IDX")</strong> is:</p>
<p><strong>^..."IDX",line_num,index_num)=""</strong></p>
<p>To retrieve the entry number indexed for line <strong>56</strong> in the array, you could use:</p>
<p><strong>S Y=$O(@VALMAR@("IDX",56,""))<br />
</strong></p></td>
</tr>
<tr class="odd">
<td><span id="XQORM_B_Variable" class="anchor"></span><strong>XQORM("B")</strong></td>
<td>List Manager automatically provides a default action of “<strong>Next Screen</strong>” or “<strong>Quit</strong>”. However, you can override this default action by setting <strong>XQORM("B")</strong> as part of the ENTRY ACTION code for a <strong>PROTOCOL</strong> menu. Set it to the text of the menu item you would like to be the new default.</td>
</tr>
</tbody>
</table>

<span id="_Ref137651978" class="anchor"></span>Table 11: Kernel Video Variables

## Kernel Video Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 11</u> lists the standard video control variables that you can use in List Manager:

| Attribute             | Variable    |
|-----------------------|-------------|
| Normal Video      | IOINORM |
| High Intensity    | IOINHI  |
| Reverse Video On  | IORVON  |
| Reverse Video Off | IORVOFF |
| Underline On      | IOUON   |
| Underline Off     | IOUOFF  |
| Blink On          | IOBON   |
| Blink Off         | IOBOFF  |

<span id="_Ref137652042" class="anchor"></span>Table 12: List Manager Generic Action Protocols

These variables can be used in ON and OFF parameters outlined in a number of List Manager calls. If other video attributes are needed, you need to make the appropriate call to Kernel’s ENDR^%ZISS entry point to set up variables for those attributes.

The variables listed in <u>Table 11</u> should always remain defined and should not be KILLed by application code.

Finally, you can specify more than one video attribute in a single call by concatenating the variables. For example, “D CNTRL^VALM10(1,20,30,IOINHI_IOUON,IOINORM)” would highlight and underline 30 characters starting at Column 20.

## List Manager Generic Action Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 12</u> lists the generic actions in the PROTOCOL (#101) file that you can use in your List Manager application.

![](list-manager-1-0-developer-s-guide/027.png) NOTE: These generic actions are all attached to the [VALM HIDDEN ACTIONS](#VALM_HIDDEN_ACTIONS_Protocol) protocol. This is so that you can set your list’s HIDDEN MENU protocol to [VALM HIDDEN ACTIONS](#VALM_HIDDEN_ACTIONS_Protocol) and have your list automatically make all of these actions available to your list users.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Protocol Name</th>
<th>Protocol Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="VALM_DOWN_A_LINE_Protocol" class="anchor"></span><strong>VALM DOWN A LINE</strong></td>
<td>Move down a line.</td>
</tr>
<tr class="even">
<td><span id="VALM_UP_ONE_LINE_Protocol" class="anchor"></span><strong>VALM UP ONE LINE</strong></td>
<td>Move up a line.</td>
</tr>
<tr class="odd">
<td><strong>VALM FIRST SCREEN</strong></td>
<td>This action will display the first screen.</td>
</tr>
<tr class="even">
<td><strong>VALM LAST SCREEN</strong></td>
<td>The action will display the last items.</td>
</tr>
<tr class="odd">
<td><span id="VALM_NEXT_SCREEN_Protocol" class="anchor"></span><strong>VALM NEXT SCREEN</strong></td>
<td>This action will allow the user to view the next screen of entries, if any exist.</td>
</tr>
<tr class="even">
<td><strong>VALM PREVIOUS SCREEN</strong></td>
<td>This action will allow the user to view the previous screen of entries, if any exist.</td>
</tr>
<tr class="odd">
<td><strong>VALM PRINT LIST</strong></td>
<td>This action allows the user to print the entire list of entries currently being displayed.</td>
</tr>
<tr class="even">
<td><strong>VALM PRINT SCREEN</strong></td>
<td>This action allows the user to print the current List Manager display screen. The header and the current portion of the list are printed.</td>
</tr>
<tr class="odd">
<td><strong>VALM REFRESH</strong></td>
<td>This actions allows the user to re-display the current screen.</td>
</tr>
<tr class="even">
<td><strong>VALM SEARCH LIST</strong></td>
<td>Finds text in list of entries.</td>
</tr>
<tr class="odd">
<td><strong>VALM TURN ON/OFF MENUS</strong></td>
<td>This toggles the menu of actions to be displayed/not displayed automatically.</td>
</tr>
<tr class="even">
<td><strong>VALM GOTO PAGE</strong></td>
<td>This protocol will allow the user to move to any page in the list.</td>
</tr>
<tr class="odd">
<td><strong>VALM RIGHT</strong></td>
<td>This protocol allows the user to move the screen to the <strong>right</strong> if the List Template is set up for a width of more than <strong>80 characters</strong>.</td>
</tr>
<tr class="even">
<td><strong>VALM LEFT</strong></td>
<td>This protocol allows the user to move the screen to the <strong>left</strong> if the List Template is set up for a width of more than <strong>80 characters</strong>.</td>
</tr>
<tr class="odd">
<td><strong>VALM QUIT</strong></td>
<td>This protocol can be used as a generic “<strong>Quit</strong>” action.</td>
</tr>
<tr class="even">
<td><span id="VALM_HIDDEN_ACTIONS_Protocol" class="anchor"></span><strong>VALM HIDDEN ACTIONS</strong></td>
<td><p>This menu protocol contains all the above action protocols. You usually would specify this protocol as the “Hidden Menu” protocol in the List Template set up.</p>
<p>The Workbench automatically designates this protocol as the “Hidden Menu” protocol when a List Template is initially created.</p></td>
</tr>
</tbody>
</table>

## General APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EN^VALM(): Load a ListMan Template/Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10118

Description: This API invokes ListMan to load a List Manager template/application.

Format: EN^VALM(template_name)

Input Parameters:template_name: (required) This parameter contains the name of a ListMan template/application to load.

Output:None.

### SHOW^VALM: Display Menu to User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10118

Description: Call the SHOW^VALM API in the [HEADER CODE (#100)](#header-code-100) field of all of your menu protocols. This displays the menu to the user.

Format: SHOW^VALM

Input Parameters:None.

Output:None.

### PAUSE^VALM1: Pause the Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This API pauses the screen. The call uses a ^DIR API with DIR(0) set to “E” for end of page. The prompt looks like:

Press RETURN to continue or '^' to exit:

Format: PAUSE^VALM1

Input Parameters:None.

Output:None.

### RANGE^VALM1: Change Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This API lets the user change a date range.

Format: RANGE^VALM1

Input Variables:DATE RANGE LIMIT Field: (required) Value as stored in the LIST TEMPLATE (#409.61) file.

VALMB: (optional) Default beginning date.

Output Variables:VALMBEG: Beginning date in VA FileMan (FM) date format.

VALMEND: Ending date in FM date format.

### EN^VALM2(): Generic Selector

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10119

Description: This API is a generic selector that can be used within an action call.

In order to use this API, the List Manager [ENTRY CODE (#106)](#entry-code-106) field *must* be set up the @VALMAR@(“IDX”) index array. This is done by setting up the list array line-by-line with the [SET^VALM10](#setvalm10-construct-initial-list-array) entry point and associating an IEN (Internal Entry Number) with each line created.

Format: EN^VALM2(valmnod,options)

Input Parameters:valmnod: (required) String in XQORNOD(0)four-piece format:

1.  IEN of selected item.
2.  IEN of menu.
3.  Menu text.
4.  Text user entered to select item.

For example:

S VALMNOD="3^1312^Misc. Consult^3"options: (required) Selection option flags:

- S—User *must* select one and only one number as an entry. The user *cannot* press the Enter key *without* entering a number; however, the user can enter a caret (^) to QUIT the select and exit the API.
- SO—User can select one number or no number, since the selection is optional (“O”). For example: if the option is “SO”, then the user is *not* required to select one number. The user can press the Enter key *without* a number or enter a caret (^) to QUIT the select and exit the API.
- L (default)—User can select numbers in a range, comma-listed, or a combination of both. For example: 1-10,15,20-30. The user *cannot* press the Enter key *without* entering a number range or list; however, the user can enter a caret (^) to QUIT the select and exit the API.
- LO—User can select a number range, number list, combination, or no number, since the selection is optional (“O”). For example: if the option is “LO”, then the user is *not* required to select any numbers. The user can press the Enter key *without* a number or enter a caret (^) to QUIT the select and exit the API.

Output:VALMY(): Array with selected entries as subscripts.

#### Examples

These examples use a modified test version of the EN^VALM2 API to only test the option input parameter choices.

#### Option “S” Example

<span id="_Ref138668793" class="anchor"></span>Figure 13: EN^ZZVALM2T API—Option “S” Example: System Prompts and User Entries

\>D EN^ZZVALM2T("<span class="mark">S</span>")

Select Item:  (1-200): <span class="mark">\<Enter\></span>

<span class="mark">This is a required response. Enter '^' to exit</span>

Select Item:  (1-200): <span class="mark">1-5</span>

<span class="mark">This response must be a number.</span>

Select Item:  (1-200): <span class="mark">1,5</span>

<span class="mark">This response must be a number.</span>

Select Item:  (1-200): <span class="mark">5</span>

Selected Item(s) Output:

<span class="mark">VALMY(5)=""</span>

#### Option “SO” Quit Examples

<span id="_Toc192050650" class="anchor"></span>Figure 14: EN^ZZVALM2T API—Option “SO” Example: System Prompts and User Entries

\>D EN^ZZVALM2T("<span class="mark">SO</span>")

Select Item:  (1-200): <span class="mark">\<Enter\></span>

Selected Item(s) Output:

\>

\>D EN^ZZVALM2T("<span class="mark">SO</span>")

Select Item:  (1-200): <span class="mark">^</span>

Selected Item(s) Output:

\>

#### Option “L” Example

<span id="_Ref138669150" class="anchor"></span>Figure 15: EN^ZZVALM2T API—Option “L” Example: System Prompts and User Entries

\>D EN^ZZVALM2T("<span class="mark">L</span>")

Select Item:  (1-200): <span class="mark">\<Enter\></span>

<span class="mark">This is a required response. Enter '^' to exit</span>

Select Item(s):  (1-200): <span class="mark">1-5,150,199-200</span>

Selected Item(s) Output:

VALMY(1)=""

VALMY(2)=""

VALMY(3)=""

VALMY(4)=""

VALMY(5)=""

VALMY(150)=""

VALMY(199)=""

VALMY(200)=""

#### Option “LO” Quit Examples

<span id="_Toc192050652" class="anchor"></span>Figure 16: EN^ZZVALM2T API—Option “LO” Quit Example: System Prompts and User Entries

\>D EN^ZZVALM2T("<span class="mark">LO</span>")

Select Item(s):  (1-200): <span class="mark">\<Enter\></span>

Selected Item(s) Output:

\>

\>D EN^ZZVALM2T("<span class="mark">LO</span>")

Select Item(s):  (1-200): <span class="mark">^</span>

Selected Item(s) Output:

\>

## List Line Text APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### FLDUPD^VALM1(): Update Caption Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This API updates a specific caption field of a specified list line on the display screen. The field name *must* match a field defined in the [CAPTION LINE COLUMNS (#200)](#CAPTION_LINE_COLUMNS) Multiple field in the LIST TEMPLATE (#409.61) file.

Format: FLDUPD^VALM1(text,field,entry)

Input Parameters:text: (required) Text to insert.

field: (required) Caption field name.

entry: (required) Line number of line in the list.

Output:None.

### \$\$SETFLD^VALM1(): Insert Text in a String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function inserts text in a string based on the column position of Caption fields stored in the current List Template. Typically, this is used when you are building the lines to place in your list’s array. It helps you easily place text strings in your list lines based on the position of caption headers in the active List Template. For example, if your List Template has three captions, you would typically make three calls to this function to construct your line – one call each to insert the text corresponding to each caption header.

Format: S X=\$\$SETFLD^VALM1(text,string,field)

Input Parameters:text: (required) Text to insert.

string: (required) String into which text is to be inserted.

field: (required) Caption field name in list template whose column position determines the position in string to insert text.

Output:return value: Returns string with text inserted.

### \$\$SETSTR^VALM1(): Set Up String for Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function sets up a string for display. Once the string has been set up for display, you would typically set it in the [ARRAY NAME (#107)](#array-name-107-optional) field specified in the List Template. For example:

S ^TMP("SDAM",\$J,SDLN)=XFormat: S X=\$\$SETSTR^VALM1(text,string,column,length)

Input Parameters:text: (required) Text to insert.

string: (required) String into which text is to be inserted.

column: (required) Column position to insert text.

length: (required) Number of characters to clear.

Output:return value: Returns string with text inserted.

#### Examples

\>S X=\$\$SETSTR^VALM1("This","",10,4) W !,X

This

\>S X=\$\$SETSTR^VALM1("is",X,20,2) W !,X

This is

\>S X=\$\$SETSTR^VALM1("an",X,30,2) W !,X

This is an

\>S X=\$\$SETSTR^VALM1("example.",X,40,8) W !,X

This is an example.

<span id="FLDTEXT_VALM10" class="anchor"></span>

### FLDTEXT^VALM10(): Inserts Text in a Column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API inserts text at the column where the specific field starts in a LINE in the list array.

The FIELD name *must* match a field defined in the [CAPTION LINE COLUMNS (#200)](#CAPTION_LINE_COLUMNS) Multiple field of the LIST TEMPLATE (#409.61) file.

Format: FLDTEXT^VALM10(line,field,text)

Input Parameters:line: (required) Line number in list array into which you insert text.

field: (required) Name of a caption field in the List Template. Text is inserted at the column position corresponding to the specified caption field.

text: (required) Text to insert.

Output:None.

### SET^VALM10(): Construct Initial List Array

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API constructs the initial list array before displaying the list to the user. It adds one line at a time to the list array.

![](list-manager-1-0-developer-s-guide/028.png) NOTE: If the List Template does *not* define an [ARRAY NAME](#array-name-107-optional) (#107), then you *must* use this call to build lines in the list array.

Format: SET^VALM10(line,string\[,ien\])

Input Parameters:line: (required) Line number in the array to set line. The list array, when completed, *must* start at line number 1, and there *cannot* be any gaps in the line numbering sequence.

string: (required) Text of the line.

ien: (optional) Entry number to associate with the line. If passed, then the line is also indexed for use by the [EN^VALM2](#envalm2-generic-selector) generic list selection call.

Output:None.

## List Line Video APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CNTRL^VALM10(): Set Video Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API sets the video attributes for a line in the current list.

Format: CNTRL^VALM10(line,column,width,on,off\[,save\])

Input Parameters:line: (required) Line number of line for which you want to set video attributes.

column: (required) Screen column position where code should be invoked.

width: (required) How many screen columns for which the code should be in effect.

on: (required) Beginning control sequence.

![](list-manager-1-0-developer-s-guide/029.png) REF: For a set of variables you can use with this input parameter, see the “[Kernel Video Variables](#kernel-video-variables)” section.

off: (required) Ending control sequence.

![](list-manager-1-0-developer-s-guide/030.png) REF: For a set of variables you can use with this input parameter, see the “[Kernel Video Variables](#kernel-video-variables)” section.

save: (optional) Possible values:

- 1—Save control sequence for later use (to be restored with [RESTORE^VALM10](#restorevalm10-restores-video-attributes)).
- 0Output:None.

### FLDCTRL^VALM10(): Activate Video Control Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API activates the appropriate video control sequences for a LINE in the list array based on the [DEFAULT VIDEO ATTRIBUTES (#.05)](#default-video-attributes-.05-optional) field in the CAPTION LINE definition for the template.

Format: FLDCTRL^VALM10(line\[,field\]\[,on\]\[,off\]\[,save\])

Input Parameters:line: (required) Line number in the list array for which you want to activate video attributes.

field: (optional) If passed, only the video attributes defined for text that falls within the specified caption field are activated. It *must* be the name of a caption field in the List Template.

on: (optional) If defined, then the code in this variable is used at the starting column position to turn on video attributes instead of the default.

![](list-manager-1-0-developer-s-guide/031.png) REF: For a set of variables you can use with this input parameter, see the “[Kernel Video Variables](#kernel-video-variables)” section.

off: (optional) If defined, then the code in this variable is used at the ending column position to turn off video attributes instead of the default.

![](list-manager-1-0-developer-s-guide/032.png) REF: For a set of variables you can use with this input parameter, see the “[Kernel Video Variables](#kernel-video-variables)” section.

save: (optional) Possible values:

- 1—Save control sequence for later use (to be restored with [RESTORE^VALM10](#restorevalm10-restores-video-attributes)).
- 0Output:None.

### RESTORE^VALM10(): Restores Video Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API restores the video attributes that have been saved for the indicated line. This subroutine does *not* re-write the line to the screen; use [WRITE^VALM10](#writevalm10-re-write-line-to-screen) after restoring video attributes to actually WRITE the line.

Format: RESTORE^VALM10(line)

Input Parameters:line: (required) Line number for which you want to restore video attributes.

Output:None.

### SAVE^VALM10(): Save Current Video Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API saves the current video attributes for the indicated line.

Format: SAVE^VALM10(line)

Input Parameters:line: (required) Line number for which you want to save the current video attributes.

Output:None.

### SELECT^VALM10(): Highlights/Unhighlights Line in List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API highlights (selects)/unhighlights (deselects) a line in the list. The API sets up or deletes the proper video controls and then “WRITEs” the line to the screen.

Format: SELECT^VALM10(line,mode)

Input Parameters:line: (required) Line number of line to highlight/unhighlight (select). The line *must* be one that is currently displayed on the screen.

mode: (required) Possible values:

- 1—Highlight (select).
- 0—Unhighlight (deselect) and restore to original state.

Output:None.

### WRITE^VALM10(): Re-Write Line to Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API re-writes a line to the screen.

Format: WRITE^VALM10(line)

Input Parameters:line: (required) Number of the line in the list to re-write to the screen.

Output:None.

## Screen Control APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CHGCAP^VALM(): Changes Label on Caption Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10118

Description: This API changes a label on a caption header for a field defined in the [CAPTION LINE COLUMNS](#CAPTION_LINE_COLUMNS) (#200) Multiple field in the LIST TEMPLATE (#409.61) file.

Format: CHGCAP^VALM(field,label)

Input Parameters:field: (required) Caption field name.

label: (required) Text for caption header.

Output:None.

### CLEAR^VALM1: Clean Up Screen after Error Occurs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: Use this API in Programmer Mode during development to clean up the screen after an error occurs. It changes the screen from Screen Mode to the full scrolling region and clears the screen. Also, it turns off the following:

- Underline
- High Intensity
- Reverse Video
- Blinking

Format: CLEAR^VALM1

Input Parameters:None.Output:None.

### FULL^VALM1: Sets Screen to Full Scrolling Region

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This API sets the screen to the full scrolling region.

Format: FULL^VALM1

Input Parameters:None.Output:None.

### INSTR^VALM1(): Inserts Text on Display Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This API inserts text on the display screen at the row and column specified.

Format: INSTR^VALM1(string,column,row\[,length\]\[,erase\])

Input Parameters:string: (required) String to insert.

column: (required) X coordinate.

row: (required) Y coordinate.

length: (optional) Number of characters to clear.

erase: (optional) If a value (any value) is passed for this parameter, the screen cells from (row,col) to (row,col+length) are erased before the string is displayed.

Output:None.

### RE^VALM4: Re-Displays List Header and List Areas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10120

Description: This API re-displays the list header and list areas for the active list application. It is often used to display the results of a change an action has caused before passing control back to the List Manager.

Normally, you set [VALMBCK](#VALMBCK_Variable)=“R” and then returns control to the List Manager.

Format: RE^VALM4

Input Parameters:None.Output:None.

### CLEAN^VALM10: Kills Data and Video Control Arrays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API KILLs the data and video control arrays associated with the active list. This call is commonly used to KILL the array related data before re-building the array.

Format: CLEAN^VALM10

Input Parameters:None.Output:None.

### KILL^VALM10(): Deletes Video Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API deletes video attributes. If the line input parameter is defined, then only the attributes for that line are deleted.

Format: KILL^VALM10(\[line\])

Input Parameters:line: (optional) Line number for which you want to delete video attributes. If this parameter is *not* passed, then all video attributes for the current list are deleted.

Output:None.

### MSG^VALM10(): Post Message to “Message Window”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10117

Description: This API allows you to immediately post a message to the “message window” located in the lower frame bar of the List Manager display screen.

![](list-manager-1-0-developer-s-guide/033.png) NOTE: To display a custom message when List Manager re-displays the screen after an action is performed, set the [VALMSG](#VALMSG_Variable) variable to the desired message text.

Format: MSG^VALM10(\[message\])

Input Parameters:message: (optional) Text up to 50 characters. If you do *not* pass this string, any custom message currently displayed is turned off, and List Manager’s standard message is re-displayed.

Output:None.

## Conversion APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \$\$FDATE^VALM1(): Returns Date in “MM/DD/YY” Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function returns a date in the following format:

MM/DD/YY

For example: 12/12/22.

Format: S X=\$\$FDATE^VALM1(fmdate)

Input Parameters:fmdate: (required) VA FileMan formatted date.

Output:return value: Returns date in “MM/DD/YY” format.

### \$\$FDTTM^VALM1(): Returns Date/Time in “MM/DD/YY@HH:MM” Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function returns a date/time in the following format:

MM/DD/YY@HH:MM

For example: 12/12/22@09:00Format: S X=\$\$FDTTM^VALM1(fmdate)

Input Parameters:fmdate: (required) VA FileMan formatted date/time.

Output:return value: Returns date/time in “MM/DD/YY@HH:MM” format.

### \$\$FTIME^VALM1(): Returns Date/Time in “MMM DD, YYYY@HH:MM” Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function returns a date/time in the following format:

MMM DD, YYYY@HH:MM

For example: DEC 12, 2022@09:00Format: S X=\$\$FTIME^VALM1(fmdate)

Input Parameters:fmdate: (required) VA FileMan formatted date/time.

Output:return value: Returns date/time in  
“MMM DD, YYYY@HH:MM” format.

### \$\$LOWER^VALM1(): Converts String from Uppercase to Lowercase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function converts a string from uppercase to lowercase. It parses the string using a space, comma, and a “/”. It starts with the second character after each delimiter.

If your line of text contains many consecutive spaces, it is often faster to execute this function as you build each portion of the line, instead of after the line has been completely built.

Format: S X=\$\$LOWER^VALM1(string)

Input Parameters:string: (required) String to convert.

Output:return value: Returns converted string.

#### Example

\>S X="PATIENT,ONE AND/OR PATIENT,TWO"

\>S X=\$\$LOWER^VALM1(X)

\>W X

Patient,One And/Or Patient,Two

### \$\$NOW^VALM1: Returns Value of “NOW” in External Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function returns the value of “NOW” in external format.

Format: S X=\$\$NOW^VALM1

Input Parameters:None.Output:return value: Returns value of “NOW” in [\$\$FTIME^VALM1](#ftimevalm1-returns-datetime-in-mmm-dd-yyyyhhmm-format) format (e.g., “Mar 06, 2023 11:15:29”).

### \$\$UPPER^VALM1(): Converts String from Lowercase to Uppercase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: ListMan

ICR \#: 10116

Description: This extrinsic function converts a string from lowercase to uppercase.

Format: S X=\$\$UPPER^VALM1(string)

Input Parameters:string: (required) String to convert.

Output:return value: Returns converted string.

<span id="_Toc192050636" class="anchor"></span>Index

\$

\$\$FDATE^VALM1, 67

\$\$FDTTM^VALM1, 67

\$\$FTIME^VALM1, 68

\$\$LOWER^VALM1, 68

\$\$NOW^VALM1, 69

\$\$SETFLD^VALM1, 14, 56

\$\$SETSTR^VALM1, 56

\$\$UPPER^VALM1, 69

@

@VALMAR@("IDX") Variables, 45

@VALMAR@(#,0) Variable, 45

A

Action Area, 2, 3, 11, 19, 23

Actions

Calling List Manager and Other Programs from Actions, 24

Creating, 16

Defining, 16

DISPLAY, 36

EXPANDED, 41

How To Define, 16

Overriding the Default Action, 21

Print List, 36

PROTOCOL, 28

PROTOCOL, 36

Supplied by List Manager), 47

ALLOWABLE NUMBER OF ACTIONS (#.12) Field, 38

Anonymous Directories, xviii

API

ENDR^%ZISS, 46

APIs

Conversion, 67

DIR, 49

General, 48

List Line Text, 55

List Line Video, 59

Screen Control, 63

ARRAY NAME (#107) Field, 41, 56, 58

ARRAY NAME Field, 11, 12, 23, 40

Arrays

Build the List Array Using List Manager’s API, 12

Build the List Array Yourself, 12

Creating, 11

Creating the Array with SET^VALM10, 12

Defining, 11

Store the List, 11

VALMHDR, 10

Assumptions, xvii

Attributes

Blink Off, 46

Blink On, 46

High Intensity, 46

Normal Video, 46

Reverse Video Off, 46

Reverse Video On, 46

Setting and Displaying Video Attributes for List Lines with FLDCTRL^VALM10, 15

Setting Video Attributes in Your List Line, 22

Terminal Type Attributes for List Manager Users, 5

Underline Off, 46

Underline On, 46

AUTOMATIC DEFAULTS (#.14) Field, 38

B

Blink Off Attribute, 46

Blink On Attribute, 46

BOTTOM MARGIN (#.06) Fields, 37

Browsing

Word-Processing Fields, 23

Build the List Array Using List Manager’s API, 12

Build the List Array Yourself, 12

C

Calling List Manager and Other Programs from Actions, 24

Callout Boxes, xiii

Calls

DIR, 17, 21

CAPTION LINE COLUMNS (#200) Field, 42, 55, 57, 63

Caption Line Information Fields

CAPTION LINE COLUMNS (#200) Field, 42

COLUMN (#.02) Field, 42

DEFAULT VIDEO ATTRIBUTES (#.05) Field, 43

DISPLAY TEXT (#.04) Field, 42

ITEM NAME (#.01) Field, 42

SCROLL LOCK (#.06) Field, 43

WIDTH (#.03) Field, 42

CHGCAP^VALM, 63

CLEAN^VALM10, 65

CLEAR^VALM1, 63

CNTRL^VALM10, 59

Code

Examples, 26

COLUMN (#.02) Field, 42

COLUMN WIDTH Field, 19

Columnar Arrangement of Menu Items, 20

Columns

Columnar Arrangement of Menu Items, 20

Scroll-Locking, 23

Components

Major List Manager Components, 4

Contents, iv

Conversion APIs, 67

Create a New List Template, 6

Create an Outline Routine, 6

Creating the Array with SET^VALM10, 12

D

Data Dictionary

Data Dictionary Utilities Menu, xvii

Listings, xvii

DATE RANGE LIMIT (#.13) Field, 38

DEFAULT VIDEO ATTRIBUTES (#.05) Field, 43, 60

Define List Actions, 16

Define List Array, 11

Define List Menu, 19

Define List Template, 6

Demographics Fields

ENTITY NAME (#.09) Field, 35

Name field, 35

SCREEN TITLE (#.11) Field, 35

DI DDU Menu, xvii

DILIST Option, xvii

DIR API, 49

DIR Call, 17, 21

DIR(0) Variable, 17

Directories

Anonymous, xviii

Disclaimers

Documentation, xi

Software, x

DISPLAY Action, 36

DISPLAY TEXT (#.04) Field, 42

Documentation

Symbols, xi

Documentation Conventions, xi

Documentation Disclaimer, xi

Documentation Navigation, xvi

E

Edit the List Template, 7

Edit the Outline Routine, 9

EN Outline Routine Tag, 10

EN^VALM, 48

EN^VALM2, 50

ENDR^%ZISS API, 46

ENTITY NAME (#.09) Field, 35

ENTRY ACTION Field, 16, 21

ENTRY CODE (#106) Field, 39, 41, 50

ENTRY CODE Field, 11, 12, 13

Entry Selection, 21

Entry Selection and Light Bar Scrolling, 21

Examples

Code, 26

EXIT ACTION Field, 16

EXIT CODE (#105) Field, 40

EXIT Outline Routine Tag, 10

EXPAND CODE (#102) Field, 41

EXPANDED Action, 41

EXPND Outline Routine Tag, 10

Export Your List Manager Application, 24

Exporting

List Manager Applications, 24

F

Fields

ALLOWABLE NUMBER OF ACTIONS (#.12), 38

ARRAY NAME, 11, 12, 23, 40

ARRAY NAME (#107), 41, 56, 58

AUTOMATIC DEFAULTS (#.14), 38

BOTTOM MARGIN (#.06), 37

CAPTION LINE COLUMNS (#200), 42, 55, 57, 63

COLUMN (#.02), 42

COLUMN WIDTH, 19

DATE RANGE LIMIT (#.13), 38

DEFAULT VIDEO ATTRIBUTES (#.05), 43, 60

DISPLAY TEXT (#.04), 42

ENTITY NAME (#.09), 35

ENTRY ACTION, 16, 21

ENTRY CODE, 11, 12, 13

ENTRY CODE (#106), 39, 41, 50

EXIT ACTION, 16

EXIT CODE (#105), 40

EXPAND CODE (#102), 41

HEADER, 19, 21

HEADER CODE (#100), 39, 45, 49

HELP CODE (#103), 41

HIDDEN MENU (#1.02), 36

ITEM NAME (#.01), 42

ITEM TEXT, 16

MNEMONIC WIDTH, 19

NAME (#.01), 35

OK TO TRANSPORT ? (#.07), 37

PRINT PROTOCOL (#1.01), 36

PROTOCOL MENU, 20

PROTOCOL MENU (#.1), 36

RIGHT MARGIN (#.04), 37, 43

SCREEN TITLE (#.11), 35

SCROLL LOCK (#.06), 43

TOP MARGIN (#.05) Field, 37

TYPE OF LIST, 20

TYPE OF LIST (#.02), 36, 41

USE CURSOR CONTROL (#.08), 38

WIDTH (#.03), 42

Word-Processing

Browsing, 23

Figures, viii

Files

LIST TEMPLATE (#409.61), 4, 50, 55, 57, 63

NEW PERSON (#200), 14, 15

PROTOCOL (#101), 4, 16, 47

Fine Tune Your Application, 21

FLDCTRL^VALM10, 60

FLDTEXT^VALM10, 57

FLDUPD^VALM1, 55

FULL^VALM1, 64

G

General APIs, 48

Generic Actions

Supplied by List Manager, 47

Getting Started, 2

H

HDR Outline Routine Tag, 10

Header Area, 2, 3, 10

HEADER CODE (#100) Field, 39, 45, 49

HEADER Field, 19, 21

Help

At Prompts, xvii

Online, xvii

Question Marks, xvii

HELP CODE (#103) Field, 41

HELP Outline Routine Tag, 10

Hidden Menu, 20, 48

HIDDEN MENU (#1.02) Field, 36

High Intensity Attribute, 46

History, Revisions to Documentation and Patches, ii

Home Pages

Adobe Website, xviii

ListMan Website, xvii

SPM Website, xi

VA Software Document Library (VDL), xviii

How to

Obtain Technical Information Online, xvi

Use this Manual, x

How To Define an Action, 16

How to Make a List Manager Application, 6

How to Select List Items, 17

I

INIT Outline Routine Tag, 10, 44, 45

Installation, 4, 5

INSTR^VALM1, 64

Intended Audience, x

Introduction, 1

ITEM NAME (#.01) Field, 42

ITEM TEXT Field, 16

K

Kernel

Video Variables, 46

Kernel Installation and Distribution System (KIDS), 24, 25, 37

KIDS

Kernel Installation and Distribution System, 24, 25, 37

KILL^VALM10, 66

L

Lines

Updating, 22

List Area, 2, 3

List File Attributes Option, xvii

List Line Text APIs, 55

List Line Video APIs, 59

List Manager

Generic Action Protocols, 47

Main Screen, 2

Workbench

VALMWB, 3

List Region Fields

BOTTOM MARGIN (#.06) Field, 37

RIGHT MARGIN (#.04) Field, 37

TOP MARGIN (#.05) Field, 37

List Template, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 22, 24, 26, 34, 35, 36, 37, 38, 40, 41, 44, 48, 56, 58, 60

Creating, 6

Defining, 6

Editing, 7

LIST TEMPLATE (#409.61) File, 4, 50, 55, 57, 63

ListMan

\$\$FDATE^VALM1, 67

\$\$FDTTM^VALM1, 67

\$\$FTIME^VALM1, 68

\$\$LOWER^VALM1, 68

\$\$NOW^VALM1, 69

\$\$SETFLD^VALM1, 56

\$\$SETSTR^VALM1, 56

\$\$UPPER^VALM1, 69

CHGCAP^VALM, 63

CLEAN^VALM10, 65

CLEAR^VALM1, 63

CNTRL^VALM10, 59

EN^VALM, 48

EN^VALM2, 50

FLDCTRL^VALM10, 60

FLDTEXT^VALM10, 57

FLDUPD^VALM1, 55

FULL^VALM1, 64

INSTR^VALM1, 64

KILL^VALM10, 66

MSG^VALM10, 66

PAUSE^VALM1, 49

RANGE^VALM1, 49

RE^VALM4, 65

RESTORE^VALM10, 61

SAVE^VALM10, 61

SELECT^VALM10, 62

SET^VALM10, 58

SHOW^VALM, 49

Website, xvii

WRITE^VALM10, 62

Lists

Long, 23

Long Lists, 23

M

Major List Manager Components, 4

Menu

Creating, 19

Defining, 19

Menus

Columnar Arrangement of Menu Items, 20

Data Dictionary Utilities, xvii

DI DDU, xvii

Hidden, 20

PROTOCOL, 27

SDAM APPOINTMENT MENU, 27

Steps to Set Up Your Application’s Menu, 19

Sub-Menus, 21

Message Window, 18, 45, 66

MNEMONIC WIDTH Field, 19

Modes

Screen, 22, 63

Scrolling, 22

MSG^VALM10, 66

MUMPS Code Related Fields

ARRAY NAME (#107) Field, 41

ENTRY CODE (#106) Field, 39

EXIT CODE (#105) Field, 40

EXPAND CODE (#102) Field, 41

HEADER CODE (#100) Field, 39

HELP CODE (#103) Field, 41

N

NAME (#.01) Field, 35

Network File System (NFS), xviii

NEW PERSON (#200) File, 14, 15

Normal Video Attribute, 46

O

Obtaining

Data Dictionary Listings, xvii

OK TO TRANSPORT ? (#.07) Field, 37

Online

Documentation, xvii

Technical Information, How to Obtain, xvi

Options

Data Dictionary Utilities, xvii

DI DDU, xvii

DILIST, xvii

List File Attributes, xvii

Orientation, x

Other Fields

ALLOWABLE NUMBER OF ACTIONS (#.12) Field, 38

AUTOMATIC DEFAULTS (#.14) Field, 38

DATE RANGE LIMIT (#.13) Field, 38

OK TO TRANSPORT ? (#.07) Field, 37

USE CURSOR CONTROL (#.08) Field, 38

Outline Routine, 6, 7, 8, 9, 10, 11

Tag

EN, 10

EXIT, 10

EXPND, 10

HDR, 10

HELP, 10

INIT, 10, 44, 45

Overriding the Default Action, 21

P

Package Requirements, 5

Patches

History, iii

PAUSE^VALM1, 49

Print List Action, 36

PRINT PROTOCOL (#1.01) Field, 36

PROTOCOL (#101) File, 4, 16, 47

PROTOCOL Action, 28, 36

Protocol Information Fields

HIDDEN MENU (#1.02) Field, 36

PRINT PROTOCOL (#1.01) Field, 36

PROTOCOL MENU (#.1) Field, 36

TYPE OF LIST (#.02) Field, 36

PROTOCOL Menu, 27

PROTOCOL MENU (#.1) Fields, 36

PROTOCOL MENU Field, 20

Protocols

Supplied by List Manager, 47

VALM DOWN A LINE, 47

VALM FIRST SCREEN, 47

VALM GOTO PAGE, 48

VALM HIDDEN ACTIONS, 48

VALM LAST SCREEN, 47

VALM LEFT, 48

VALM NEXT SCREEN, 47

VALM PREVIOUS SCREEN, 47

VALM PRINT LIST, 47

VALM PRINT SCREEN, 47

VALM QUIT, 48

VALM REFRESH, 47

VALM RIGHT, 48

VALM SEARCH LIST, 47

VALM TURN ON/OFF MENUS, 47

VALM UP ONE LINE, 47

Q

Question Mark Help, xvii

R

RANGE^VALM1, 49

RE^VALM4, 65

Reference Materials, xvii

Reference Type

Supported

\$\$FDATE^VALM1, 67

\$\$FDTTM^VALM1, 67

\$\$FTIME^VALM1, 68

\$\$LOWER^VALM1, 68

\$\$NOW^VALM1, 69

\$\$SETFLD^VALM1, 56

\$\$SETSTR^VALM1, 56

\$\$UPPER^VALM1, 69

CHGCAP^VALM, 63

CLEAN^VALM10, 65

CLEAR^VALM1, 63

CNTRL^VALM10, 59

EN^VALM, 48

EN^VALM2, 50

FLDCTRL^VALM10, 60

FLDTEXT^VALM10, 57

FLDUPD^VALM1, 55

FULL^VALM1, 64

INSTR^VALM1, 64

KILL^VALM10, 66

MSG^VALM10, 66

PAUSE^VALM1, 49

RANGE^VALM1, 49

RE^VALM4, 65

RESTORE^VALM10, 61

SAVE^VALM10, 61

SELECT^VALM10, 62

SET^VALM10, 58

SHOW^VALM, 49

WRITE^VALM10, 62

Requirements

Package, 5

RESTORE^VALM10, 61

Reverse Video Off Attribute, 46

Reverse Video On Attribute, 46

Revision History, ii

Patches, iii

RIGHT MARGIN (#.04) Field, 37, 43

Routine to Create List, 11

Routines

Outline, 8, 9, 10, 11

VALMWB, 3

S

SAVE^VALM10, 61

Screen

Main, 2

Screen Control APIs, 63

Screen Mode, 22, 63

SCREEN TITLE (#.11) Field, 35

Screens

Using the Entire Screen, 18

SCROLL LOCK (#.06) Field, 43

Scrolling Mode, 22

Scroll-Locking Columns, 23

SDAM APPOINTMENT MENU, 27

SELECT^VALM10, 62

Selecting

Entry Selection and Light Bar Scrolling, 21

Items, 21

List Items, 17

SET^VALM10, 58

Setting and Displaying Video Attributes for List Lines with FLDCTRL^VALM10, 15

Setting Up Text Lines with Captions and \$\$SETFLD^VALM1, 14

Setting Video Attributes in Your List Line, 22

Setup, 4

SHOW^VALM, 49

Software Disclaimer, x

Steps to Set Up Your Application’s Menu, 19

Sub-Menus, 21

Symbols

Found in the Documentation, xi

T

Table of Contents, iv

Tables, viii

Terminal Type Attributes for List Manager Users, 5

TOP MARGIN (#.05) Field, 37

TYPE OF LIST (#.02) Field, 36, 41

TYPE OF LIST Field, 20, 36

U

Underline Off Attribute, 46

Underline On Attribute, 46

Updating

List Lines, 22

Updating Items in the List, 22

URLs

Adobe Website, xviii

ListMan Website, xvii

SPM Website, xi

VA Software Document Library (VDL), xviii

USE CURSOR CONTROL (#.08) Field, 38

Use this Manual, How to, x

Using the Entire Screen, 18

V

VA FileMan, xvi, xvii, 11, 23, 24, 40, 41, 50, 67, 68

Browser, 23, 24

VA Software Document Library (VDL)

Website, xviii

VALM

CHGCAP^VALM, 63

EN^VALM, 48

SHOW^VALM, 49

VALM DOWN A LINE Protocol, 47

VALM FIRST SCREEN Protocol, 47

VALM GOTO PAGE Protocol, 48

VALM HIDDEN ACTIONS Protocol, 48

VALM LAST SCREEN Protocol, 47

VALM LEFT Protocol, 48

VALM NEXT SCREEN Protocol, 47

VALM PREVIOUS SCREEN Protocol, 47

VALM PRINT LIST Protocol, 47

VALM PRINT SCREEN Protocol, 47

VALM QUIT Protocol, 48

VALM REFRESH Protocol, 47

VALM RIGHT Protocol, 48

VALM SEARCH LIST Protocol, 47

VALM TURN ON/OFF MENUS Protocol, 47

VALM UP ONE LINE Protocol, 47

VALM(TITLE) Variable, 44

VALM1

\$\$FDATE^VALM1, 67

\$\$FDTTM^VALM1, 67

\$\$FTIME^VALM1, 68

\$\$LOWER^VALM1, 68

\$\$NOW^VALM1, 69

\$\$SETFLD^VALM1, 56

\$\$SETSTR^VALM1, 56

\$\$UPPER^VALM1, 69

CLEAR^VALM1, 63

FLDUPD^VALM1, 55

FULL^VALM1, 64

INSTR^VALM1, 64

PAUSE^VALM1, 49

RANGE^VALM1, 49

VALM10

CLEAN^VALM10, 65

CNTRL^VALM10, 59

FLDCTRL^VALM10, 60

FLDTEXT^VALM10, 57

KILL^VALM10, 66

MSG^VALM10, 66

RESTORE^VALM10, 61

SAVE^VALM10, 61

SELECT^VALM10, 62

SET^VALM10, 58

WRITE^VALM10, 62

VALM2

EN^VALM2, 50

VALM4

RE^VALM4, 65

VALMBCK Variables, 18, 23, 39, 44, 45, 65

VALMBG Variables, 39, 44

VALMCC Variable, 22

VALMCC Variables, 44

VALMCNT Variable, 12, 13

VALMCNT Variables, 39, 44

VALMDDF() Variable, 43, 44

VALMHDR Array, 10

VALMHDR() Variable, 39, 45

VALMQUIT Variable, 45

VALMQUIT Variables, 39, 45

VALMSG Variable, 18, 66

VALMSG Variables, 45

VALMST Variables, 45

VALMWB Routine, 3

Variables

@VALMAR@("IDX"), 45

@VALMAR@(#,0), 45

DIR(0), 17

Kernel Video Variables, 46

VALM(TITLE), 44

VALMBCK, 18, 23, 44, 45

VALMBCK Variables, 39

VALMBG, 39, 44

VALMCC, 22, 44

VALMCNT, 12, 13, 39, 44

VALMDDF(), 43, 44

VALMHDR(), 39, 45

VALMQUIT, 39, 45

VALMQUIT variable, 45

VALMSG, 18, 45, 66

VALMST, 45

XQORM("B"), 46

XQORM(“B”), 38

Variables, List Manager, 44

VariablesVALMBCK, 65

W

Websites

Adobe Website, xviii

ListMan, xvii

SPM, xi

VA Software Document Library (VDL), xviii

What Comes Next?, 10

When the User Is In Scrolling Mode (Not Screen Mode), 22

WIDTH (#.03) Field, 42

Word-Processing Fields

Browsing, 23

Workbench, 3, 4, 6, 7, 8, 11, 14, 15, 16, 19, 20, 34, 48

WRITE^VALM10, 62

X

XQORM("B") Variable, 46

XQORM(“B”) Variable, 38