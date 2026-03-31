---
title: Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: and Kernel Toolkit 7.3
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: 
  - 4
  - 200
  - 8933
  - 8991
security_keys: []
menu_options: 65
description: 
audience: 
keywords: 
  - strong
  - class
  - even
  - colspan
  - kernel
  - routine
  - span
  - options
  - table
  - edit
page_count: 0
word_count: 124918
section_count: 44
table_count: 17
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: July 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 and Kernel Toolkit 7.3

  Technical Manual
---

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/001.png)

July 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc244336446" class="anchor"></span>Revision History

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><blockquote>
<p><span id="_Ref87258570" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 30%" />
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
<td>07/31/2025</td>
<td>5.16</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated external document links to open documents in a new window.</p></li>
<li><p>Replaced the “Documentation Navigation” section with the “<a href="#_Hlt425841091">Internal Word Navigation Links Setup Steps</a>” section.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>06/16/2025</td>
<td>5.15</td>
<td><p>Updates for Kernel Patch XU*8.0*807:</p>
<ul>
<li><p>Updated <u>Table 9</u>: Added the following routines:</p></li>
</ul>
<ul>
<li><p><a href="#XUP807_Routine"><strong>XUP807</strong></a></p></li>
<li><p><a href="#XUXTADAPI_Routine"><strong>XUXTADAPI</strong></a></p></li>
<li><p><a href="#XUXTADAPI2_Routine"><strong>XUXTADAPI2</strong></a></p></li>
<li><p><a href="#XUXTADAPI3_Routine"><strong>XUXTADAPI3</strong></a></p></li>
<li><p><a href="#XUXTADASK1_Routine"><strong>XUXTADASK1</strong></a></p></li>
<li><p><a href="#XUXTADDILG_Routine"><strong>XUXTADDILG</strong></a></p></li>
<li><p><a href="#XUXTADDT1_Routine"><strong>XUXTADDT1</strong></a></p></li>
<li><p><a href="#XUXTADPRT1_Routine"><strong>XUXTADPRT1</strong></a></p></li>
<li><p><a href="#XUXTADPRT2_Routine"><strong>XUXTADPRT2</strong></a></p></li>
<li><p><a href="#XUXTADSSE_Routine"><strong>XUXTADSSE</strong></a></p></li>
<li><p><a href="#XUXTADSSEF_Routine"><strong>XUXTADSSEF</strong></a></p></li>
</ul>
<ul>
<li><p>Updated <u>Table 24</u>: Added the following options: <a href="#XUXTAD_SERVICE_SECTION_EDIT_Option">XUXTAD SERVICE/SECTION EDIT</a></p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>05/28/2025</td>
<td>5.15</td>
<td><p>Updates for Kernel Patch XU*8.0*799, which enhances Kernel to support the Master Veteran Index (MVI) implementation of Enterprise User Identity when adding or editing entries in the NEW PERSON (#200) file in VistA:</p>
<ul>
<li><p>Modified Section <u>2.5</u>, “<u>Kernel System Parameters (#8989.3) File</u>,” <u>Table 3</u>: Added the <a href="#NEW_PERSON_FIELD_MONITOR_PURGE_Field">NEW PERSON FIELD MONITOR PURGE (#875) field</a></p></li>
<li><p>Modified Section <u>3.2</u>, “<u>Production Account Routines</u>;” <u>Table 9</u>:</p></li>
</ul>
<ul>
<li><p>Added the following new routines:</p></li>
</ul>
<ul>
<li><p><a href="#XU8P799_Routine"><strong>XU8P799</strong></a></p></li>
<li><p><a href="#XUIAMDD1_Routine"><strong>XUIAMDD1</strong></a></p></li>
<li><p><a href="#XUIAMNPB_Routine"><strong>XUIAMNPB</strong></a></p></li>
<li><p><a href="#XUIAMPR_Routine"><strong>XUIAMPR</strong></a></p></li>
<li><p><a href="#XUIAMPR1_Routine"><strong>XUIAMPR1</strong></a></p></li>
<li><p><a href="#XUIAMXML2_Routine"><strong>XUIAMXML2</strong></a></p></li>
</ul>
<ul>
<li><p>Modified the following existing routines:</p></li>
</ul>
<ul>
<li><p><a href="#XUESSO2_Routine"><strong>XUESSO2</strong></a></p></li>
<li><p><a href="#XUIAMXML_Routine"><strong>XUIAMXML</strong></a></p></li>
<li><p><a href="#XUMVINPU_Routine"><strong>XUMVINPU</strong></a></p></li>
<li><p><a href="#XUS1_Routine"><strong>XUS1</strong></a></p></li>
<li><p><a href="#XUSERNEW_Routine"><strong>XUSERNEW</strong></a></p></li>
<li><p><a href="#XUSTERM_Routine"><strong>XUSTERM</strong></a></p></li>
</ul>
<ul>
<li><p>Modified Section <u>4.1.1</u>, “<u>Globals—VA-FileMan-Compatible Storage</u>:” <u>Table 12</u>: Modified the <a href="#XTV_Global"><strong>^XTV</strong></a> global: Added File #8933.1.</p></li>
<li><p>Modified Section <u>4.2.1</u>, “<u>Kernel and Kernel Toolkit Export Files</u>:” <u>Table 15</u>:</p></li>
</ul>
<ul>
<li><p>Added the <a href="#NEW_PERSON_FIELD_MONITOR_File">NEW PERSON FIELD MONITOR (#8933.1)</a> file.</p></li>
<li><p>Modified the <a href="#NEW_PERSON_File">NEW PERSON (#200)</a>Added the <strong>AVIAM</strong> new style record cross-reference (x-ref) to various fields in the NEW PERSON (#200) file.</p></li>
</ul>
<ul>
<li><p>Added Section <u>4.3.2</u>, “<u>NEW PERSON File—Audit Fields</u>:” Added NEW PERSON (#200) file fields that are now audited.</p></li>
<li><p>Modified Section <u>5.3.1</u>, “<u>Kernel</u>:” <u>Table 24</u>:</p></li>
</ul>
<ul>
<li><p>Added the following new options:</p></li>
</ul>
<ul>
<li><p><a href="#MPI_New_Person_Feild_Mon_Btch_Upd_Option">MPI NEW PERSON FIELD MONITOR BATCH UPDATE</a> [<a href="#XUS_IAM_NPFM_BATCH_UPDATE_Option">XUS IAM NPFM BATCH UPDATE</a>]</p></li>
<li><p><a href="#MPI_New_Person_Field_Mon_Purge_Option">MPI NEW PERSON FIELD MONITOR PURGE</a> [<a href="#XUS_IAM_NPFM_PURGE_Option">XUS IAM NPFM PURGE</a>]</p></li>
<li><p><a href="#XUS_IAM_USER_TERMINATE_Option"><strong>XUS IAM USER TERMINATE</strong> [XUS IAM USER TERMINATE]</a></p></li>
<li><p><a href="#XUSERTEM_Option"><strong>Template User Add</strong> [XUSERTEM]</a></p></li>
<li><p><a href="#XUSERBLK_TEMPLATE_Option"><strong>Template Grant Access by Profile [</strong>XUSERBLK TEMPLATE<strong>]</strong></a></p></li>
</ul>
<ul>
<li><p>Modified the following existing options:</p></li>
</ul>
<ul>
<li><p><a href="#XU_USER_TERMINATE_Option"><strong>User terminate event</strong> [XU USER TERMINATE]</a></p></li>
<li><p><a href="#Add_a_New_User_to_the_System_Option"><strong>Add a New User to the System</strong></a> [<a href="#XUSERNEW_Option">XUSERNEW</a>]</p></li>
</ul>
<ul>
<li><p>Modified Section <u>15.7</u>, “<u>File Security</u>:” <u>Figure 21</u>: Added security for File #8933.1.</p></li>
<li><p>Changed references from “Software Product Management (SPM)” to “Product Delivery Service (PDS)” throughout.</p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref87258570" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc95124664" class="anchor"></span>List of Figures

<span id="_Toc205036065" class="anchor"></span>List of Tables

<span id="_Toc234301877" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instruction are offered about Kernel 8.0 and Kernel Toolkit 7.3 routines, files, options, application program interfaces (APIs), direct mode utilities, and other system-related information provided for overall Veterans Health Information Systems and Technology Architecture (VistA) system management and application developers.

Intended Audience

The intended audience of this manual is the following stakeholders:

- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Product Delivery Service (PDS)—VistA legacy development teams.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

<span id="disclaimers" class="anchor"></span>Disclaimers

<span id="software_disclaimer" class="anchor"></span>Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/003.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per VHA Directive 2004-038, this routine should not be modified.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/004.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimers

The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                              | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/005.png)   | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/006.png) | CAUTION/DISCLAIMER: Used to caution the reader to take special notice of critical information.                  |

<span id="_Toc193532635" class="anchor"></span>Table 2: Parameters—Kernel Site Parameter Files

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- \<Application Name/Abbreviation/Namespace\>PATIENT,\<N\>
- \<Application Name/Abbreviation/Namespace\>USER,\<N\>

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Kernel (XU or KRN) test patient and user names would be documented as follows:

KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; … KRNPATIENT,14; and so on.

KRNUSER,ONE; KRNUSER,TWO; KRNUSER,THREE; … KRNUSER,14; and so on.

- “Snapshots” of computer commands and online displays (that is screen captures/dialogs) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts will be bold typeface and highlighted in yellow (such as <span class="mark">\<Enter\></span>).
- Emphasis within a dialog box will be highlighted in blue (such as <span class="mark">STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- References to “<span class="mark">\<Enter\></span>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M “\>” prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (such as the XUPROGMODE security key).

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/008.png) NOTE: Other software code (such as Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

<span id="_Hlt425841091" class="anchor"></span>Internal Word Navigation Links Setup Steps

This document uses Microsoft® Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar for all Word documents, see the *Tech Writer Tips: Internal Word Navigation Links Setup* (VA Intranet) document.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/009.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/010.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/011.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about Kernel should consult the following:

- *Kernel Release Notes*
- *Kernel Installation Guide*
- *Kernel 8.0 Systems Management: \<Function\> User Guides*
- *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual* (this manual)
- *Kernel Security Tools Manual*
- Kernel VA Intranet Website.

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at the following website: [Adobe Website](http://www.adobe.com/)

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: [VDL Website](https://www.va.gov/vdl/)

VistA documentation and software can also be downloaded from the Network File Share (NFS) repository.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Kernel](#kernel)
  - [Kernel Toolkit](#kernel-toolkit)
    - [Multi-Term Look-Up (MTLU)](#multi-term-look-up-mtlu)
    - [Duplicate Resolution Utilities](#duplicate-resolution-utilities)
  - [Purpose](#purpose)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Installation](#installation)
  - [Namespace](#namespace)
  - [Kernel Site Parameters](#kernel-site-parameters)
  - [Kernel 8.0 Site Parameters File Changes](#kernel-80-site-parameters-file-changes)
  - [Kernel System Parameters (#8989.3) File](#kernel-system-parameters-89893-file)
  - [Kernel Parameters (#8989.2) File](#kernel-parameters-89892-file)
  - [Kernel Parameter Definitions (#8989.51) File](#kernel-parameter-definitions-898951-file)
    - [XPAREDIT Routine](#xparedit-routine)
  - [Audit-Related Site Parameters](#audit-related-site-parameters)
  - [Spooler Site Parameters](#spooler-site-parameters)
  - [TaskMan Site Parameters](#taskman-site-parameters)
  - [Implementing Multi-Term Look-Up](#implementing-multi-term-look-up)
  - [Implementing Duplicate Resolution Utilities](#implementing-duplicate-resolution-utilities)
    - [Data Storage](#data-storage)
    - [Retention](#retention)
    - [Resource Requirements](#resource-requirements)
    - [Programmer Notes](#programmer-notes)
    - [Merge Process](#merge-process)
  - [Configuring VAX/Alpha Performance Monitor (VPM)](#configuring-vaxalpha-performance-monitor-vpm)
- [Routines](#routines)
  - [Manager Account Routines](#manager-account-routines)
  - [Production Account Routines](#production-account-routines)
  - [Additional Routines Installed by Virgin Install](#additional-routines-installed-by-virgin-install)
  - [Mapping Routines](#mapping-routines)
- [Files](#files)
  - [Globals](#globals)
    - [Globals—VA-FileMan-Compatible Storage](#globalsva-fileman-compatible-storage)
    - [Globals—Non-VA-FileMan-Compatible Storage](#globalsnon-va-fileman-compatible-storage)
    - [Globals—Storage Used for Additional Files during Virgin Install](#globalsstorage-used-for-additional-files-during-virgin-install)
  - [Files](#files-1)
    - [Kernel and Kernel Toolkit Export Files](#kernel-and-kernel-toolkit-export-files)
    - [Additional Files Installed During Virgin Installation](#additional-files-installed-during-virgin-installation)
  - [Fields](#fields)
    - [PERSON CLASS (#8932.1) File](#person-class-89321-file)
    - [NEW PERSON File—Audit Fields](#new-person-fileaudit-fields)
- [Exported Options](#exported-options)
  - [Menu Tree Roots](#menu-tree-roots)
  - [Menu Tree Diagrams](#menu-tree-diagrams)
    - [Generating Menu Diagrams](#generating-menu-diagrams)
    - [Systems Manager Menu \[EVE\]](#systems-manager-menu-eve)
    - [XUCORE](#xucore)
    - [XUTIO](#xutio)
    - [XUMAINT](#xumaint)
    - [XUSITEMGR](#xusitemgr)
    - [XUPROG](#xuprog)
    - [XU-SPL-MGR](#xu-spl-mgr)
    - [XUSPY](#xuspy)
    - [XUTM MGR](#xutm-mgr)
    - [XUSER](#xuser)
    - [Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\]](#parent-of-queuable-options-ztmqueuable-options)
    - [SYSTEM COMMAND OPTIONS \[XUCOMMAND\]](#system-command-options-xucommand)
    - [Extended-Action Options](#extended-action-options)
    - [Protocols](#protocols)
    - [Server Options](#server-options)
    - [Options Attached to Menus for Other Software](#options-attached-to-menus-for-other-software)
    - [DEA ePCS Utility](#dea-epcs-utility)
  - [Options—Listed Alphabetically by Name](#optionslisted-alphabetically-by-name)
    - [Kernel](#kernel-1)
    - [Toolkit](#toolkit)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Entry Points](#callable-entry-points)
- [Direct Mode Utilities](#direct-mode-utilities)
- [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [External Relations](#external-relations)
  - [External Relations with Other VistA Software](#external-relations-with-other-vista-software)
  - [External Relations with M Operating Systems](#external-relations-with-m-operating-systems)
  - [Required Software](#required-software)
  - [DBA Approvals and Integration Control Registration (ICRs)](#dba-approvals-and-integration-control-registration-icrs)
    - [ICRs—Current List for Kernel or Kernel Toolkit as Custodian](#icrscurrent-list-for-kernel-or-kernel-toolkit-as-custodian)
    - [ICRs—Detailed Information](#icrsdetailed-information)
    - [ICRs—Current List for Kernel or Kernel Toolkit as Subscriber](#icrscurrent-list-for-kernel-or-kernel-toolkit-as-subscriber)
- [Internal Relations](#internal-relations)
  - [Independence of Options](#independence-of-options)
- [Software-Wide Variables](#software-wide-variables)
- [SACC Exemptions](#sacc-exemptions)
- [Global Protection, Translation, and Journaling](#global-protection-translation-and-journaling)
  - [Globals in Production Account](#globals-in-production-account)
- [Security](#security)
  - [Security Management](#security-management)
  - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
    - [Mail Groups](#mail-groups)
    - [Alerts](#alerts)
    - [Bulletins](#bulletins)
  - [Remote Systems](#remote-systems)
  - [Interfaces](#interfaces)
  - [Electronic Signatures](#electronic-signatures)
    - [Electronic Signature Restrictions](#electronic-signature-restrictions)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [Contingency Planning](#contingency-planning)
  - [Official Policies](#official-policies)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)

## Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel is the intermediary layer between the host operating system and other Veterans Health Information Systems and Technology Architecture (VistA) software applications, so that VistA software can coexist in a standard operating-system-independent computing environment. Kernel provides a standard and consistent user and developer interface between software applications and the underlying M implementation.

It provides the underlying computing environment for all VistA users. VistA system administrators can track users and resolve problems using Kernel options. VistA application developers rely on tools provided by Kernel to perform routine programming tasks.

By offering a computing environment that hides the *non*-standard features of M, Kernel frees VistA users, system administrators, and developers from dependence on any one vendor’s M implementation. This allows VistA to shift easily to new hardware and software platforms as information technology (IT) advances.

## Kernel Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit is a robust set of tools developed to aid the VistA development community in analysis, writing, and testing code. It is a set of generic tools that are used by development teams, software quality assurance (SQA), and system administrators to support distinct tasks.

Kernel Toolkit provides utilities for the management and definition of development projects. Many of these utilities have been used by the San Francisco Information Systems Center (ISC) for internal management and have proven valuable. Kernel Toolkit provides many programming and system management tools and interacts directly with the underlying M (aka MUMPS \[Massachusetts General Hospital Utility Multi-Programming System\]) environment in many ways.

It includes the following tools:

- <u>Multi-Term Look-Up (MTLU)</u>
- <u>Duplicate Resolution Utilities</u>

### Multi-Term Look-Up (MTLU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many medical information systems depend on the standardized encoding of diagnoses and procedures for reports, searches, and statistics. The following files are among some of the more critical files:

- ICD DIAGNOSIS (#80)
- ICD OPERATIONS/PROCEDURE (#80.1)
- CPT (#81)

The Multi-Term Look-Up utility increases the accessibility of the information in these files by associating user-supplied words or phrases with terms found in a more descriptive, FREE TEXT field.

Multi-Term Look-Up enables:

- Local setup of virtually any reference file.
- Developers to modify the behavior of the "special" lookup by defining shortcuts, keywords, or synonyms.

Multi-Term Look-Up integrates with any package that uses a reference file, which has been entered in a site's LOCAL LOOKUP (#8984.4) file.

### Duplicate Resolution Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duplicate Resolution Utilities give developers a “shell” that allows their users to check their data files for duplicate records and merge the records if any are found. These utilities provide the functionality of combining duplicate records based on conditions established in customized applications. The following two files are used to do this:

- DUPLICATE RECORD (#15)
- DUPLICATE RESOLUTION (#15.1)

The Merge Shell was developed by the Indian Health Service (IHS) to support their Multi-Facility Integration project.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this manual is to provide information about the structure of the set of software utilities known as Kernel and Kernel Toolkit. Two other major affiliated software applications, VA FileMan and MailMan, are excluded, since they are documented elsewhere. This material is presented for reference by VistA system administrators, application developers, and other Kernel/Kernel Toolkit users.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information in this section is meant to help system administrators implement and maintain Kernel and Kernel Toolkit.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/012.png) REF: For recommendations regarding global mapping, journaling, translation, and replication in Kernel and Kernel Toolkit, see the “<u>Mapping Routines</u>” and “<u>Global Protection, Translation, and Journaling</u>” sections.  
  
For recommendations regarding archiving and purging in Kernel and Kernel Toolkit, see the “<u>Archiving and Purging</u>” section.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the appropriate patch installation instructions for Kernel and Kernel Toolkit Patches on FORUM.

Installing Kernel both on a system having a previous version of Kernel present and on a system without Kernel (a “virgin” install) is explained in the *Kernel Installation Guide*. It also contains many requirements and recommendations regarding how Kernel should be configured. Be sure to read it before attempting to install Kernel.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/013.png) REF: For more detailed information on installing Kernel and Kernel Toolkit, see the *Kernel Installation Guide* located on the VA Software document Library (VDL) at: [VDL Kernel Application Documents](http://www.quadramed.com/?appid=10)

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel and Kernel Toolkit routine namespaces include:

- XDR\*
- XG\*
- XI\*
- XLF\*
- XPAR\*
- XPD\*
- XQ\*
- XT\*
- XU\*
- ZIS\*
- ZOS\*
- ZTM\*
- ZU\*

## Kernel Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the Kernel site parameters that can be set to customize the operation of the various components of Kernel.

## Kernel 8.0 Site Parameters File Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0 exports three central site parameter files:

<table>
<caption><p><span id="_Ref355158573" class="anchor"></span>Table 3: Parameters—KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KERNEL SYSTEM PARAMETERS (#8989.3)</td>
<td><p>Kernel’s main site parameters. These parameters were formerly stored in the MAILMAN SITE PARAMETERS (#4.3) file but are now stored in this file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/014.png) <strong>REF:</strong> For information on this parameter file, see the “<u>Kernel System Parameters (#8989.3) File</u>” section.</p></td>
</tr>
<tr class="even">
<td>KERNEL PARAMETERS (#8989.2)</td>
<td><p>This file holds parameters that Kernel uses, which the site is allowed to change. It is <em>not</em> restricted solely to site parameters. The file makes use of a DEFAULT value field and a REPLACEMENT value field for each parameter.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/015.png) <strong>REF:</strong> For information on this parameter file, see the “<u>Kernel Parameters (#8989.2) File</u>” section.</p></td>
</tr>
<tr class="odd">
<td>PARAMETER DEFINITION (#8989.51) file</td>
<td><p>This file holds additional Kernel parameter definitions.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/016.png) <strong>REF:</strong> For information on this parameter file, see the “<u>Kernel Parameter Definitions (#8989.51) File</u>” section.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref355158573" class="anchor"></span>Table 3: Parameters—KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)

## Kernel System Parameters (#8989.3) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel system parameters are stored in the KERNEL SYSTEM PARAMETERS (#8989.3) file.

<span id="_Toc205036170" class="anchor"></span>Figure 1: Parameters—Enter/Edit Kernel Site Parameters Menu Option

Operations Management ... \[XUSITEMGR\]

Kernel Management Menu... \[XUKERNEL\]

Enter/Edit Kernel Site Parameters \[XUSITEPARM\]

<table>
<caption><p><span id="_Ref501696480" class="anchor"></span>Table 4: Parameters—KERNEL PARAMETERS (#8989.2) File (Listed Alphabetically by Name)</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AGENCY CODE (#9)</td>
<td>This field defines what agency uses this computer. It sets a flag that can be accessed by applications programs that need to know this information.</td>
</tr>
<tr class="even">
<td>ASK DEVICE TYPE AT SIGN-ON (#205)</td>
<td><p>This is the default for whether a user/terminal should be asked for their Terminal Type at signon. This is overridden by a similar field in the DEVICE (#3.5) and NEW PERSON (#200) files:</p>
<ul>
<li><p>If set to <strong>YES</strong>, then an <strong>ANSI DA</strong> is sent to the terminal to collect the terminal’s DEVICE ATTRIBUTES message. If it is a known one, then the Terminal Type is set to this; otherwise, the user is prompted.</p></li>
<li><p>If set to <strong>NO</strong>, then the one from the LAST SIGN-ON field or device subtype is used.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>AUTO-GENERATE ACCESS CODES (#11)</td>
<td><p>If this field is set to <strong>YES</strong>, the person assigning Access Codes <em>must</em> choose one of the automatically generated codes that are presented.</p>
<p>If this field is set to <strong>NO</strong>, other codes are only accepted.</p></td>
</tr>
<tr class="even">
<td>BYPASS DEVICE LOCK-OUT (#211)</td>
<td><p>Setting this field to <strong>YES</strong> causes all device lockout checking to be bypassed. This means that during signon the checks against the DEVICE (#3.5) file for the following fields will be skipped:</p>
<ul>
<li><p>OUT-OF-SERVICE DATE (#6)</p></li>
<li><p>SECURITY (#15)</p></li>
<li><p>PROHIBITED TIMES FOR SIGN-ON (#2009).</p></li>
</ul>
<p>It can be overridden by the PERFORM DEVICE CHECKING (#51.91) field in the DEVICE (#3.5) file.</p></td>
</tr>
<tr class="odd">
<td>DEFAULT # OF ATTEMPTS (#202)</td>
<td>This is the default number of attempts that a user is allowed when trying to sign on before the device is locked. This field is overridden by the # OF ATTEMPTS (#51.2) field in the DEVICE (#3.5) file. ALL checking for device lockout can be bypassed by setting the BYPASS DEVICE LOCK-OUT (#211) field.</td>
</tr>
<tr class="even">
<td>DEFAULT AUTO-MENU (#206)</td>
<td>This is the default for whether auto-menu is turned <strong>ON</strong> or <strong>OFF</strong>. It is overridden by the AUTO MENU (#51.6) field in the DEVICE (#3.5) file.</td>
</tr>
<tr class="odd">
<td>DEFAULT INSTITUTION (#217)</td>
<td>This field defines a default institution that will be assigned to the user’s institution [<strong>DUZ(2)</strong>] for any user that does <em>not</em> have one.</td>
</tr>
<tr class="even">
<td>DEFAULT LANGUAGE (#207)</td>
<td>This is the default language used to set the <strong>DUZ(“LANG”)</strong> flag for each user. VA FileMan uses this setting to enable the display of language-specific dates and times, numeric formats, and dialogs.</td>
</tr>
<tr class="odd">
<td>DEFAULT LOCK-OUT TIME (#203)</td>
<td>This is the default time in seconds that a locked device <em>must</em> be idle before another signon attempt is allowed. This time is overridden by the LOCK-OUT TIME (#51.3) field in the DEVICE (#3.5) file. ALL checking for device lockout is ignored if the BYPASS DEVICE LOCK-OUT (#211) field is set to <strong>YES</strong>.</td>
</tr>
<tr class="even">
<td>DEFAULT MULTIPLE SIGN-ON (#204)</td>
<td><p>This is the default value for whether users may sign on at more than one terminal at a time. It is overridden by the following fields:</p>
<ul>
<li><p>DEFAULT MULTIPLE SIGN-ON (#204) field in the DEVICE (#3.5)</p></li>
<li><p>MULTIPLE SIGN-ON (#200.04) field in the NEW PERSON (#200) file.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DEFAULT TIMED-READ (SECONDS) (#210)</td>
<td>This is the default time-out for all <strong>READ</strong>s and is overridden by the TIMED READ (# OF SECONDS) (#51.1) field in the DEVICE (#3.5) file.</td>
</tr>
<tr class="even">
<td>DEFAULT TYPE-AHEAD (#209)</td>
<td>This is the default as to whether type-ahead is allowed. It is overridden by the TYPE-AHEAD (#51.9) field in the DEVICE (#3.5) file.</td>
</tr>
<tr class="odd">
<td>DEVICE TO AUDIT (#212.1) Multiple</td>
<td><p>This Multiple (subfile) holds a list of devices that are to be audited when device auditing is activated.</p>
<p>The <strong>.01</strong> field is referenced when the FAILED ACCESS ATTEMPT AUDIT (#212.5) field is set to <strong>D</strong> or <strong>DR</strong>. It specifies the logical names of the devices on which to audit failed attempts.</p></td>
</tr>
<tr class="even">
<td>FAILED ACCESS ATTEMPT AUDIT (#212.5)</td>
<td><p>This field indicates whether an audit log is to be generated for failed access attempts. Audits can be done for all devices or specified devices only. Recording of what is entered is optional.</p>
<p>Entries include:</p>
<ul>
<li><p><strong>A—</strong>All devices/no text recorded.</p></li>
<li><p><strong>D—</strong>Specified devices/no text recorded.</p></li>
<li><p><strong>AR—</strong>All devices/text recorded.</p></li>
<li><p><strong>DR—</strong>Specified devices/text recorded.</p></li>
<li><p><strong>N—</strong>No audit.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>INITIATE AUDIT (#19.4)</td>
<td>This field indicates the date when an audit begins. The OPTION AUDIT (#19) field defines the nature of the audit that is performed. Auditing is only done if there is both INITIATE AUDIT (#19.4) and TERMINATE AUDIT (#19.5) field data.</td>
</tr>
<tr class="even">
<td>INTERACTIVE USER’S PRIORITY (#216)</td>
<td>This field changes the priority of interactive users on the system at signon time. There is a danger that using this field will cause the users to have poor response time from the computer. Valid values range from <strong>1</strong> to <strong>10</strong>.</td>
</tr>
<tr class="odd">
<td>IP SECURITY ON (#405.1)</td>
<td><p>This field turns on or off the IP security “Three strikes and you are out” code. This locks an IP address if there are too many failed/invalid signon attempts. It is like the device lockout.</p>
<ul>
<li><p>Use the <strong>Release IP lock</strong> [XU IP RELEASE] option to release the lock on an IP address.</p></li>
<li><p>Use the <strong>Edit Site IP lockout</strong> [XU SITE LOCKOUT] option to edit the Kernel System Parameters for IP lockout and/or User lockout and Terminal server list entry.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>LIFETIME OF VERIFY CODE (#214)</td>
<td>This is the number of days that a Verify Code remains valid. After this time the user <em>must</em> choose a new Verify Code.</td>
</tr>
<tr class="odd">
<td>LOG RESOURCE USAGE? (#300)</td>
<td>This <strong>YES/NO</strong> field indicates whether resource usage data, such as CPU seconds, DIO, BIO, and so on, is collected in <strong>^XUCP(</strong>. If this field is set to <strong>YES</strong>, every time a user goes in and out of an option each time is recorded.</td>
</tr>
<tr class="even">
<td>LOG SYSTEM RT? (#41, 6)</td>
<td>A subfield in the VOLUME SET (#41) Multiple. Setting this subfield to <strong>YES</strong> enables system response time logging, which only takes place if the necessary code exists in the application software.</td>
</tr>
<tr class="odd">
<td>MAX SIGNON ALLOWED (#41, 2)</td>
<td>A subfield in the VOLUME SET (#41) Multiple. This subfield defines the maximum number of jobs that <strong>XUS</strong> or RPC Broker allows to sign on to this VOLUME SET or CPU. It is the number of processes (interactive, background, and system) that can be active on the machine at any one time. When reached, Kernel prohibits logons.</td>
</tr>
<tr class="even">
<td>MAX SPOOL DOCUMENT LIFE-SPAN (#31.3)</td>
<td><p>This field controls the number of days that a spooled document is allowed to remain in the spooler before deletion by the <strong>Purge old spool documents</strong> [XU-SPL-PURGE] option, which needs to be set up to run in the background. Valid values range from <strong>1</strong> to <strong>365</strong>; <strong>Zero</strong> decimals.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/017.png) <strong>REF:</strong> For more information on spooler site parameters, see the “<u>Spooler Site Parameters</u>” section.</p></td>
</tr>
<tr class="odd">
<td>MAX SPOOL DOCUMENTS PER USER (#31.2)</td>
<td><p>This field limits the number of spooled documents that any user can have on the system. <em>Recommended</em> values from <strong>10</strong> to <strong>100</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/018.png) <strong>REF:</strong> For more information on spooler site parameters, see the “<u>Spooler Site Parameters</u>” section.</p></td>
</tr>
<tr class="even">
<td>MAX SPOOL LINES PER USER (#31.1)</td>
<td><p>This field holds the maximum number of lines of spooled output a user is allowed. If the user has more than this number, then they are <em>not</em> allowed to spool any more until some of their spooled documents are deleted. This only controls the granting of new spool documents and does <em>not</em> terminate the number of lines that are transferred into the spool data file. Valid values range from <strong>1</strong> to <strong>9999999</strong>; <em>recommended</em> value <strong>9999</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/019.png) <strong>REF:</strong> For more information on spooler site parameters, see the “<u>Spooler Site Parameters</u>” section.</p></td>
</tr>
<tr class="odd">
<td>NAMESPACE TO AUDIT (#19.2) Multiple</td>
<td>This Multiple (subfile) holds a list of software namespaces to audit. All options within a namespace are audited if the OPTION AUDIT (#19) Field is set to <strong>s</strong> (specific options).</td>
</tr>
<tr class="even">
<td><span id="NEW_PERSON_FIELD_MONITOR_PURGE_Field" class="anchor"></span>NEW PERSON FIELD MONITOR PURGE (#875) field</td>
<td><p>This field indicates the number of days that transmitted records in the NEW PERSON FIELD MONITOR (#8933.1) file should be maintained before being purged/deleted. The number of days entered can range from <strong>10</strong> to <strong>999</strong>. The XU*8.0*799 post-install routine initialized this field to <strong>365</strong> days.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/020.png) <strong>NOTE:</strong> This field was added with Kernel Patch XU*8.0*799.</p></td>
</tr>
<tr class="odd">
<td>NEW PERSON IDENTIFIERS (#21)</td>
<td>This field holds M code to set the <strong>DR</strong> variable to the string of fields (<em>not</em> a template) to be used as identifiers when adding entries to the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td>OPTION AUDIT (#19)</td>
<td><p>This field indicates what should be audited between the INITIATE AUDIT (#19.4) date and TERMINATE AUDIT (#19.5) date fields.</p>
<p>Valid values include:</p>
<ul>
<li><p><strong>n—</strong>No audit.</p></li>
<li><p><strong>a—</strong>All options audited.</p></li>
<li><p><strong>s—</strong>Specific options audited.</p></li>
<li><p><strong>u—</strong>Users audited.</p></li>
</ul>
<p>The OPTION TO AUDIT (#19.1) Multiple along with the NAMESPACE TO AUDIT (#19.2) Multiple hold the lists of specific options that would be audited (choosing <strong>s</strong>). The USER TO AUDIT (#19.3) Multiple holds the list of users that would be audited (choosing <strong>u</strong>).</p></td>
</tr>
<tr class="odd">
<td>OPTION TO AUDIT (#19.1) Multiple</td>
<td>This Multiple (subfile) holds a list of options to audit if the OPTION AUDIT (#19) field is set to <strong>s</strong> (specific options).</td>
</tr>
<tr class="even">
<td>ORGANIZATION (#200.2)</td>
<td><p>Use this Identity and Access Management (IAM) field to identify the organization of this VistA instance. For internally authenticated users, this field matches the SUBJECT ORGANIZATION (#205.2) field of the user identified in the NEW PERSON (#200) file. For the VA, this field should always contain the following value:</p>
<p><strong>Department Of Veterans Affairs</strong></p></td>
</tr>
<tr class="odd">
<td>ORGANIZATION ID (#200.3)</td>
<td><p>Use this Identity and Access Management (IAM) field to uniquely identify the organization of this VistA instance. For internally authenticated users, this field matches the SUBJECT ORGANIZATION ID (#205.3) field of the user identified in the NEW PERSON (#200) file. For the VA, this field should always contain the following value:</p>
<p><strong>urn:oid:2.16.840.1.113883.4.349</strong></p></td>
</tr>
<tr class="even">
<td>ROUTINE MONITORING (#9.8)</td>
<td><p>This field supports routine auditing. It controls how the routine monitoring program behaves; whether to look at all routines or just selected name spaces.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/021.png) <strong>REF:</strong> For more information, see the <em>Kernel Security Tools Manual</em>.</p></td>
</tr>
<tr class="odd">
<td>ROUTINE N-SPACE TO MONITOR (#9.81) Multiple</td>
<td><p>This Multiple (subfile) supports routine auditing. If the routine monitoring program is to look at namespaces, then this Multiple lists the namespaces that it looks at. For example, an entry of <strong>XU*</strong> causes it to look at all routines that start with <strong>XU</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/022.png) <strong>REF:</strong> For more information, see the <em>Kernel Security Tools Manual</em>.</p></td>
</tr>
<tr class="even">
<td>SECURITY TOKEN SERVICE (#200.1)</td>
<td><p>When using brokered authentication with a security token issued by a Security Token Service (STS), this field contains the identification of the issuer of the token. The STS is trusted by both the client and the service to provide interoperable security tokens.</p>
<p>Security Assertion Markup Language (SAML) tokens are standards-based <strong>XML</strong> tokens that are used to exchange security information, including:</p>
<ul>
<li><p>Attribute statements</p></li>
<li><p>Authentication decision statements</p></li>
<li><p>Authorization decision statements</p></li>
</ul>
<p>They can be used as part of a Single Sign-On (SSO) solution allowing a client to talk to services running on disparate technologies. For the VA, this field should always contain the following value:</p>
<p><strong>&lt;REDACTED&gt;.va.gov</strong></p></td>
</tr>
<tr class="odd">
<td><span id="SIGN_ON_LOG_RETENTION_sys_parameter" class="anchor"></span>SIGN-ON LOG RETENTION (#221)</td>
<td><p>This parameter determines the number of entries (number of days) to retain data in the Kernel SIGN-ON LOG (#3.081) file (sign-on log). Larger values will consume more disk space; so, sites should evaluate the impact on data storage <em>before</em> changing the default value of <strong>365 days</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/023.png) <strong>REF:</strong> This parameter was added with Kernel Patch XU*8.0*756.</p></td>
</tr>
<tr class="even">
<td>TERMINATE AUDIT (#19.5)</td>
<td>This field indicates when the audit ends. The start date is set in the INITIATE AUDIT ($19.4) field.</td>
</tr>
<tr class="odd">
<td>USER TO AUDIT (#19.3) Multiple</td>
<td>This Multiple (subfile) holds a list of users to audit their option use, if the OPTION AUDIT (#19) field is set to <strong>u</strong> (users audited).</td>
</tr>
<tr class="even">
<td>VOLUME SET (#41) Multiple</td>
<td><p>This is the name of each CPU or Volume Set in the domain. Within each Volume Set, you can set:</p>
<ul>
<li><p>MAX SIGN-ON ALLOWED (#41, 2)</p></li>
<li><p>LOG SYSTEM RT? (#41, 6).</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref501696480" class="anchor"></span>Table 4: Parameters—KERNEL PARAMETERS (#8989.2) File (Listed Alphabetically by Name)

## Kernel Parameters (#8989.2) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel does *not* export an option to edit these parameters. The KERNEL PARAMETERS (#8989.2) file holds parameters that Kernel uses, and the site is allowed to change. It is *not* restricted solely to site parameters. The file makes use of a DEFAULT (#3) value field and a REPLACEMENT (#4) value field for each parameter. Rather than having a specific field for each parameter, one Multiple holds all parameters.

<u>Table 4</u> lists the active parameters that Kernel currently stores in the KERNEL PARAMETERS (#8989.2) file file:

| Parameters             | Description                                                                                                                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUEDIT CHARACTERISTICS | You can enter the name of a replacement for the standard Edit User Characteristics template in the REPLACEMENT (#4) field. Kernel will then use the replacement for the Edit User Characteristics \[XUSEREDITSELF\] option.                           |
| XUEXISTING USER        | You can enter the name of a template to use in the Edit an Existing User \[XUSEREDIT\] option in the REPLACEMENT (#4) field. Kernel uses the replacement template for the Edit an Existing User \[XUSEREDIT\] option.                             |
| XUNEW USER             | You can enter the name of a template to use in the Add a New User to the System \[XUSERNEW\] option in the REPLACEMENT (#4) field. Kernel will then use the replacement template for the Add a New User to the System \[XUSERNEW\] option.        |
| XUREACT USER           | You can enter the name of a template to use in the Reactivate a User \[XUSERREACT\] option in the REPLACEMENT (#4) field. Kernel will then use the replacement template for the Reactivate a User \[XUSERREACT\] option.                          |
| XUSER COMPUTER ACCOUNT | You can enter the name of a help frame in the REPLACEMENT (#4) field. Kernel will then use the replacement help frame instead of the standard one when printing the computer access letter from the Add a New User to the System \[XUSERNEW\] option. |

<span id="_Ref354660023" class="anchor"></span>Table 5: Parameters—PARAMETER DEFINITION (#8989.51) File (Listed Alphabetically by Name)

## Kernel Parameter Definitions (#8989.51) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional Kernel parameters are stored in the PARAMETER DEFINITION (#8989.51) file.

<table>
<caption><p><span id="_Toc193532640" class="anchor"></span>Table 6: Parameters—Audit-Related Parameters from the KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XPAR ALL ENTITIES</strong></td>
<td>All Entities: This is a “dummy” parameter definition that is used by <strong>XPARLIST</strong> to get a list of all entities. The ALLOWABLE ENTITIES (#51, 30) Multiple field for this parameter should list all entities defined in PARAMETERS.</td>
</tr>
<tr class="even">
<td><strong>XPAR MY NEW PARAM</strong></td>
<td>Test MY new parameters.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST DATE/TIME</strong></td>
<td>Test <strong>DATE/TIME</strong>: Test parameter entry for a single valued date.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST FREE TEXT</strong></td>
<td>Test <strong>FREE TEXT</strong>: Test parameter entry for single valued <strong>FREE TEXT</strong>.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST M CODE</strong></td>
<td>Test <strong>XPAR</strong> entry with a value of M code.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST ME</strong></td>
<td>TEST ME.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST MULT FREE TEXT</strong></td>
<td>Test entry for showing how to add to a <strong>FREE TEXT</strong> with multiple instances. Enter a string of <strong>5-15</strong> characters.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST MULTIPLE</strong></td>
<td><p>Test Everything: This is a test of a parameter that allows multiple instances and multiple entities.</p>
<ul>
<li><p>PRECEDENCE: 1<br />
ENTITY FILE: SYSTEM</p></li>
<li><p>PRECEDENCE: 2<br />
ENTITY FILE: DIVISION</p></li>
<li><p>PRECEDENCE: 3<br />
ENTITY FILE: SERVICE</p></li>
<li><p>PRECEDENCE: 4<br />
ENTITY FILE: LOCATION</p></li>
<li><p>PRECEDENCE: 5<br />
ENTITY FILE: PACKAGE</p></li>
<li><p>PRECEDENCE: 6<br />
ENTITY FILE: CLASS</p></li>
<li><p>PRECEDENCE: 7<br />
ENTITY FILE: TEAM</p></li>
<li><p>PRECEDENCE: 8<br />
ENTITY FILE: USER</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST MULTIPTR</strong></td>
<td>Test Multiple <strong>POINTER</strong>.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST NUMERIC</strong></td>
<td>Test <strong>NUMERIC</strong>: Test parameter entry for <strong>NUMERIC</strong> data.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST POINTER</strong></td>
<td>Test <strong>POINTER</strong>: Test parameter entry for <strong>POINTER</strong> types.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST PWP</strong></td>
<td>Test Multiple <strong>WORD-PROCESSING</strong> (WP) with <strong>POINTER</strong> Instance.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST SET OF CODES</strong></td>
<td>Test <strong>SET OF CODES</strong>: Test parameter entry of a <strong>SET OF CODES</strong>.</td>
</tr>
<tr class="even">
<td><strong>XPAR TEST WP</strong></td>
<td>Test WP: Test parameter entry for <strong>WORD-PROCESSING</strong> (WP) values.</td>
</tr>
<tr class="odd">
<td><strong>XPAR TEST YES/NO</strong></td>
<td>Test Yes/No.</td>
</tr>
<tr class="even">
<td><strong>XPD PATCH HFS SERVER</strong></td>
<td>Patch module HFS server: This parameter holds the name of the server to send email to when a KIDS Host File Server (HFS) file is made.</td>
</tr>
<tr class="odd">
<td><strong>XQ MENUMANAGER PROMPT</strong></td>
<td><p>This parameter allows sites to change the default <strong>&lt; TEST ACCOUNT&gt;</strong> prompt to another value, such as <strong>&lt;LEGACY SYSTEM&gt;</strong> in menu prompts of non-production VistA systems. The text defined by this parameter is inserted in the MenuMan (Menu Manager) prompts. If no text is defined, the hard-coded default is “ <strong>&lt; TEST ACCOUNT&gt;</strong>”. Alternatives could be:</p>
<ul>
<li><p>“ <strong>&lt;LEGACY SYSTEM&gt;</strong>”</p></li>
<li><p>“ <strong>&lt;CONTINGENCY&gt;</strong>”</p></li>
<li><p>“ <strong>&lt;READ ONLY&gt;</strong>”</p></li>
<li><p>Or any other value from <strong>3</strong> to <strong>20</strong> characters, depending on the purpose of the non-production VistA system.</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/024.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*614.</p></td>
</tr>
<tr class="even">
<td><strong>XQAL BACKUP REVIEWER</strong></td>
<td><p>Backup Reviewer for Unprocessed Alerts: This parameter contains information about the Backup Reviewer for unprocessed alerts. This person is sent the alerts for the specified entity that remain unprocessed by the original recipients.</p>
<ul>
<li><p>PRECEDENCE: 50<br />
ENTITY FILE: SYSTEM</p></li>
<li><p>PRECEDENCE: 40<br />
ENTITY FILE: DIVISION</p></li>
<li><p>PRECEDENCE: 35<br />
ENTITY FILE: SERVICE</p></li>
<li><p>PRECEDENCE: 1<br />
ENTITY FILE: USER</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XU SIG BLOCK DISABLE</strong></td>
<td><p><span id="XU_80_679_parameter" class="anchor"></span>Determines whether restrictions are active:</p>
<ul>
<li><p>If the parameter is set to <strong>ON</strong> (<strong>1</strong>), then restrictions are active, and Electronic Signature Block edits are disabled for users without the <strong>XUSIG</strong> security key.</p></li>
<li><p>If the parameter is set to <strong>OFF</strong> (<strong>0</strong>), then restrictions are <em>not</em> active, and Electronic Signature Block edits are enabled for all users.</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/025.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*679.</p></td>
</tr>
<tr class="even">
<td><strong>XU522</strong></td>
<td><p>Determines whether old-style (less secure) Compensation and Pension Record Interchange (CAPRI) logins are permitted and logged. Enter any of the following values:</p>
<ul>
<li><p><strong>Y</strong> (<strong>YES</strong>)<strong>—</strong>To disable old-style CAPRI logins (default).</p></li>
<li><p><strong>E</strong> (<strong>ERROR</strong>)<strong>—</strong>To disable old-style CAPRI logins and trap attempts.</p></li>
<li><p><strong>N</strong> (<strong>NO</strong>)<strong>—</strong>To leave old-style CAPRI logins enabled.</p></li>
<li><p><strong>L</strong> (<strong>DEBUG</strong>)<strong>—</strong>To leave old-style CAPRI logins enabled but trap attempts.</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/026.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*522.</p></td>
</tr>
<tr class="odd">
<td><strong>XU594</strong></td>
<td><p>This parameter skips the code that Kernel Patch XU*8.0*543 uses. If XU*8.0*543 broke the iMedConsent application, this parameter should be set to <strong>YES</strong>. The default is <strong>NO</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/027.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*594.</p></td>
</tr>
<tr class="even">
<td><strong>XU645</strong></td>
<td><p>This parameter determines if a terminated user’s information should be deleted:</p>
<ul>
<li><p>A <strong>NO</strong> value means you do <em>not</em> want to purge the terminated user information. This was requested by the Office of Inspector General (OIG) when they want all user information preserved.</p></li>
<li><p>A <strong>YES</strong> value means to purge the information, which is normal operating procedure.</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/028.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*645.</p></td>
</tr>
<tr class="odd">
<td><strong>XUEPCS REPORT DEVICE</strong></td>
<td><p>e-Prescribing of Controlled Substances (ePCS) Device Definition for Reports: Enter a device from the DEVICE (#3.5) file for the ePCS report output.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/029.png) <strong>NOTE:</strong> This parameter was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td><strong>XUS CCOW VAULT PARAM</strong></td>
<td>CCOW Vault Parameter: This parameter holds the application passcode for the CCOW vault.</td>
</tr>
<tr class="odd">
<td><strong>XUS-XUP SET ERROR TRAP</strong></td>
<td><p>Set Error Trap in <strong>XUP</strong>: This parameter controls if <strong>XUP</strong> will set up an ERROR trap for the user:</p>
<ul>
<li><p>PRECEDENCE: 1<br />
ENTITY FILE: USER</p></li>
<li><p>PRECEDENCE: 2<br />
ENTITY FILE: SYSTEM</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUS-XUP VPE</strong></td>
<td><p>Drop into VPE: This parameter controls if a user when exiting <strong>XUP</strong> is dropped into VPE or right to the “<strong>&gt;</strong>“ prompt:</p>
<ul>
<li><p>PRECEDENCE: 1<br />
ENTITY FILE: USER</p></li>
<li><p>PRECEDENCE: 2<br />
ENTITY FILE: SYSTEM</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSC1 DEBUG</strong></td>
<td>Set Debug mode for <strong>XUSC1</strong>: This parameter controls if the <strong>XUSC1</strong> client code records debug information into the <strong>^TMP</strong> global.</td>
</tr>
<tr class="even">
<td><strong>XUSNPI QUALIFIED IDENTIFIER</strong></td>
<td>NPI QUALIFIED IDENTIFIER: This is a mapping of <strong>NPI ID</strong> name to the files that hold the data.</td>
</tr>
</tbody>
</table>

<span id="_Toc193532640" class="anchor"></span>Table 6: Parameters—Audit-Related Parameters from the KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)

### XPAREDIT Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the XPAREDIT routine to update the parameters in the PARAMETER DEFINITION (#8989.51) file.

To edit the DEA ePCS Utility parameter, perform the following procedure:

1.  From the Programmer prompt, enter the following code:

D ^XPAREDIT

2.  At the “Select PARAMETER DEFINITION NAME:” prompt, enter the parameter you want to edit.

> <span id="_Toc205036171" class="anchor"></span>Figure 2: Parameters—XPAREDIT Routine: Editing Parameters in the PARAMETER DEFINITION (#8989.51) File

\><span class="mark">D ^XPAREDIT</span>

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME:

## Audit-Related Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc205036172" class="anchor"></span>Figure 3: Parameters—Audit-Related Menu Options

System Security... \[XUSPY\]

Audit Features ... \[XUAUDIT MENU\]

Maintain System Audit Options... \[XUAUDIT MAINT\]

Establish System Audit Parameters \[XUAUDIT\]

You can edit audit-related site parameters located in the KERNEL SYSTEM PARAMETERS (#8989.3) file using the Establish System Audit Parameters \[XUAUDIT\] option (the fields are also reachable from the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option).

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/030.png) REF: For more information on auditing, see the *Kernel Security Tools Manual*.

<table>
<caption><p><span id="_Toc193532642" class="anchor"></span>Table 7: Parameters—Spooler-Related Parameters from the KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameters (Fields)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEVICE TO AUDIT (#212.1) Multiple</td>
<td><p>This Multiple (subfile) holds a list of devices that are to be audited when device auditing is activated.</p>
<p>The <strong>.01</strong> field is referenced when the FAILED ACCESS ATTEMPT AUDIT (#212.5) field is set to <strong>D</strong> or <strong>DR</strong>. It specifies the logical names of the devices on which to audit failed attempts.</p></td>
</tr>
<tr class="even">
<td>FAILED ACCESS ATTEMPT AUDIT (#212.5)</td>
<td><p>This field indicates whether an audit log is to be generated for failed access attempts. Audits can be done for all devices or specified devices only. Recording of what is entered is optional:</p>
<p>Entries include:</p>
<ul>
<li><p><strong>A—</strong>All devices/no text recorded.</p></li>
<li><p><strong>D—</strong>Specified devices/no text recorded.</p></li>
<li><p><strong>AR—</strong>All devices/text recorded.</p></li>
<li><p><strong>DR—</strong>Specified devices/text recorded.</p></li>
<li><p><strong>N—</strong>No audit.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>INITIATE AUDIT (#19.4)</td>
<td>This field indicates the date when an audit begins. The OPTION AUDIT (#19) field defines the nature of the audit that is performed. Auditing is only done if there is both INITIATE AUDIT (#19.4) and TERMINATE AUDIT (#19.5) field data.</td>
</tr>
<tr class="even">
<td>NAMESPACE TO AUDIT (#19.2) Multiple</td>
<td>This Multiple (subfile) holds a list of software namespaces to audit. All options within a namespace are audited if the OPTION AUDIT (#19) Field is set to <strong>s</strong> (specific options).</td>
</tr>
<tr class="odd">
<td>OPTION AUDIT (#19)</td>
<td><p>This field indicates what should be audited between the INITIATE AUDIT (#19.4) date and TERMINATE AUDIT (#19.5) date fields.</p>
<p>Valid values include:</p>
<ul>
<li><p><strong>n—</strong>No audit.</p></li>
<li><p><strong>a—</strong>All options audited.</p></li>
<li><p><strong>s—</strong>Specific options audited.</p></li>
<li><p><strong>u—</strong>Users audited.</p></li>
</ul>
<p>The OPTION TO AUDIT (#19.1) Multiple along with the NAMESPACE TO AUDIT (#19.2) Multiple hold the lists of specific options that would be audited (choosing <strong>s</strong>). The USER TO AUDIT (#19.3) Multiple holds the list of users that would be audited (choosing <strong>u</strong>).</p></td>
</tr>
<tr class="even">
<td>OPTION TO AUDIT (#19.1) Multiple))</td>
<td>This Multiple (subfile) holds a list of options to audit if the OPTION AUDIT (#19) field is set to <strong>s</strong> (specific options).</td>
</tr>
<tr class="odd">
<td>TERMINATE AUDIT (#19.5)</td>
<td>This field indicates when audit ends. The start date is set in the INITIATE AUDIT (#19.4) field.</td>
</tr>
<tr class="even">
<td>USER TO AUDIT (Multiple; #19.3)</td>
<td>This Multiple (subfile) holds a list of users to audit their option use, if the OPTION AUDIT (#19) field is set to <strong>u</strong> (users audited).</td>
</tr>
</tbody>
</table>

<span id="_Toc193532642" class="anchor"></span>Table 7: Parameters—Spooler-Related Parameters from the KERNEL SYSTEM PARAMETERS (#8989.3) File (Listed Alphabetically by Field Name)

## Spooler Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc205036173" class="anchor"></span>Figure 4: Spooler Site Parameters Edit Menu Option

Spool Management... \[XU-SPL-MGR\]

Spooler Site Parameters Edit \[XU-SPL-SITE\]

You can edit spooler-related site parameters located in the KERNEL SYSTEM PARAMETERS (#8989.3) file with the Spooler Site Parameters Edit \[XU-SPL-SITE\] option (the fields are also reachable from the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option).

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/031.png) REF: For more information on the Spooler, see the “Spooling” section in the [*Kernel 8.0 Systems Management: Device Handler User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf).

| Fields                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAX SPOOL LINES PER USER (#31.1)     | This field holds the maximum number of lines of spooled output a user is allowed. If the user has more than this number, then they are *not* allowed to spool any more until some of their spooled documents are deleted. This only controls the granting of new spool documents and does *not* terminate the number of lines that are transferred into the spool data file. Valid values range from 1 to 9999999; *recommended* value 9999. |
| MAX SPOOL DOCUMENT LIFE-SPAN (#31.3) | This field controls the number of days that a spooled document is allowed to remain in the spooler before deletion by the Purge old spool documents \[XU-SPL-PURGE\] option, which needs to be set up to run in the background. Valid values range from 1 to 365; Zero decimals.                                                                                                                                                         |
| MAX SPOOL DOCUMENTS PER USER (#31.2) | This field limits the number of spooled documents that any user can have on the system. *Recommended* value from 10 to 100.                                                                                                                                                                                                                                                                                                                      |

<span id="_Ref333475181" class="anchor"></span>Table 8: Routines—Manager Account Routines

## TaskMan Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three separate groups of site parameters for TaskMan. They are stored in the following files:

- TASKMAN SITE PARAMETERS (#14.7)
- UCI ASSOCIATION (#14.6)
- VOLUME SET (#14.5)

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/032.png) REF: For information about configuring TaskMan’s site parameters, see the “TaskMan System Management: Configuration” section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf).

## Implementing Multi-Term Look-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementing Multi-Term Look-Up requires:

- Central Processing Unit (CPU) capacity: 3%.
- Disk Space: 20,000 bytes. However, this depends on the number of entries in the following files:
- LOCAL KEYWORD (#8984.1)
- LOCAL SHORTCUT (#8984.2)
- LOCAL SYNONYM (#8984.3)

The Multi-Term Look-Up utility has one parameter, which can be adjusted to meet the needs of an individual site. Whenever a new file is entered through the Add Entries To Look-Up File \[XTLKMODPARS\] option, an additional MUMPS cross-reference is necessary on a FREE TEXT field of the new file. This reference converts the FREE TEXT field into keywords to be used in the search. To use the full functionality of the package, the cross-reference entry on the FREE TEXT field should match the INDEX (#.03) field in the LOCAL LOOKUP (#8984.4) file. <u>Figure 5</u> is an example for the ICD DIAGNOSIS (#80) file where AIHS is entered on the FREE TEXT field as a cross-reference. AIHS, therefore, *must* match the entry made at the Local Look-up INDEX prompt in the Add Entries To Look-Up File \[XTLKMODPARS\] option.

<span id="_Ref513707709" class="anchor"></span>Figure 5: Multi-Term Look-Up—Sample System Prompts and User Entries: Entering a Cross-Reference on a Field in a File

Select OPTION: <span class="mark">UTILITY FUNCTIONS</span>

Select UTILITY OPTION: <span class="mark">CROSS-REFERENCE A FIELD</span>

MODIFY WHAT FILE: ICD DIAGNOSIS// <span class="mark">ICD DIAGNOSIS \<Enter\></span> (12535 entries)

Select FIELD: <span class="mark">DESCRIPTION</span>

CURRENT CROSS-REFERENCE IS MUMPS 'D' INDEX OF FILE

CHOOSE E (EDIT)/D (DELETE)/C (CREATE): <span class="mark">C</span>

WANT TO CREATE A NEW CROSS-REFERENCE FOR THIS FIELD? NO// <span class="mark">Y \<Enter\></span> (YES)

CROSS-REFERENCE NUMBER: 2// <span class="mark">\<Enter\></span>

Select TYPE OF INDEXING: REGULAR// <span class="mark">MUMPS</span>

WANT CROSS-REFERENCE TO BE USED FOR LOOKUP AS WELL AS FOR SORTING? YES// <span class="mark">N \<Enter\></span> (NO)

SET STATEMENT: <span class="mark">S %="^ICD9(""AIHS"",I,DA)" D S^XTLKWIC</span>

KILL STATEMENT: <span class="mark">S %="^ICD9(""AIHS"",I,DA)" D K^XTLKWIC</span>

INDEX: AC// <span class="mark">AIHS</span>

...

DO YOU WANT TO CROSS-REFERENCE EXISTING DATA NOW? YES// <span class="mark">Y \<Enter\></span> (YES)

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT.................

.....................................................

\><span class="mark">D ^XUP</span>

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: <span class="mark">APPLI \<Enter\></span> CATION UTILITIES XTMENU Application Utilities

Multi-Term Lookup Main Menu ...

Select Application Utilities Option: <span class="mark">MULTI \<Enter\></span>-Term Lookup Main Menu

Multi-Term Lookup (MTLU)

Print Utility

Utilities for MTLU ...

Select Multi-Term Lookup Main Menu Option: <span class="mark">UTIL \<Enter\></span> cities for MTLU

KL Delete Entries From Look-up

ST Add Entries To Look-Up File

Add/Modify Utility ...

Select Utilities for MTLU Option: <span class="mark">ST \<Enter\></span> Add Entries To Look-Up File

Select LOCAL LOOKUP NAME: <span class="mark">ICD DIAGNOSIS</span>

ARE YOU ADDING 'ICD DIAGNOSIS' AS A NEW LOCAL LOOKUP (THE 3RD)? <span class="mark">Y \<Enter\></span> (YES)

LOCAL LOOKUP NAME: ICD DIAGNOSIS// <span class="mark">\<Enter\></span>

LOCAL LOOKUP DISPLAY PROTOCOL: <span class="mark">\<Enter\></span>

INDEX: <span class="mark">AIHS</span>

...Ok, will now setup KEYWORD and SHORTCUT file DD's

to allow terms for 'ICD DIAGNOSIS' entries...

PREFIX: M// <span class="mark">?</span>

Answer must be a unique prefix, 1-10 characters in length

PREFIX: M// <span class="mark">D</span>

\<REMINDER\> Using 'Edit File', set the lookup routine, XTLKDICL, in 'ICD DIAGNOSIS DD

Select LOCAL LOOKUP NAME: <span class="mark">\<Enter\></span>

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/033.png) NOTE: Using the VA FileMan Edit File \[DIEDIT\] option, enter XTLKDICL at the “Look-Up Program” prompt. Data should be cross-referenced when installing the cross-reference. If *not*, data should be re-indexed after hours, since this can be CPU intensive.

## Implementing Duplicate Resolution Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementing Duplicate Resolution Utilities requires the following resources and familiarity with the following processes:

- <u>Data Storage</u>
- <u>Retention</u>
- <u>Resource Requirements</u>
- <u>Programmer Notes</u>
- <u>Merge Process</u>

### Data Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each entry in the DUPLICATE RECORD (#15) file takes approximately 500 bytes, depending on the number of tests that are used and the number of packages that are affected by the record merge.

Each entry in the DUPLICATE RESOLUTION (#15.1) file takes approximately 28K, depending on the number of tests that need to be run.

### Retention

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data in the duplicate record is *not* meant to be purged or archived. If one chose to, they could purge the verified *non*-duplicates, but this means that when the duplicate checking utilities are run these entries are put back in the DUPLICATE RECORD (#15) file and requires somebody to verify it again.

### Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One terminal and one printer are required. A slave printer to the terminal would be very beneficial.

### Programmer Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Developers need to determine if the merging of two file entries affects their package in such a way that they need to have their own unique merge that deals with only their package's files.

The following conditions usually mean that a developer must write their own unique merge:

1.  The patient POINTER field is defined as a NUMERIC or FREE TEXT field rather than a POINTER.
1.  The developer wants their end-users to complete some task prior to the merge occurring.
2.  There are compound cross-references that include the patient POINTER on another field, but the cross-reference is *not* triggered by the changing of the patient POINTER.
3.  The Merge (Duplicate Resolution Utilities) does *not* do what the package developer desires.

### Merge Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a description of what occurs during the merge:

1.  Checks the base file (such as PATIENT \[#2\] file) to see if it exists.
4.  Check the PT nodes \[such as ^DD(2,0,"PT",\] and any false positives are removed.
5.  Creates a list of files and fields within those files that point to the file being merged (such as in this example the file being merged is the PATIENT \[#2\] file).

If a file is pointing to the file being merged by its .01 field, and if that .01 field is DINUM, then all files/fields that point to that file are also gathered. The DINUM rule also applies to that file and any files pointing to it, to any depth.

6.  Checks each file/field and re-points/merges as follows:
- If the field pointing is *not* a .01 field, the "from entry" is changed to the "to entry".
- If the field pointing is the .01 field but *not*DINUM, the "from entry" is changed to the "to entry".
- Each pointing .01DINUM field is handled as follows:
- If the .01DINUM field is at the file level, ^DIT0 is called to merge the "from entry" to the "to entry" and then the "from entry" is deleted. ^DIT0 merges field by field but does *not* change any value in the "to entry". That means that NULL fields in the "to entry" get the value from the same field in the "from entry" if it is *not*NULL, and valued fields in the "to entry" remain the same. ^DIT0 also merges Multiples:
- If a Multiple entry in the "from entry" *cannot* be found in the "to entry", it is added to the "to entry".
- If a Multiple entry in the "from entry" can be found in the "to entry", then that Multiple entry is merged field by field.
- If the .01DINUM field is at the subfile level (in a Multiple), it is handled as follows:
- If there is a "from entry" but no "to entry", the "from entry" is added to the "to entry", changing the .01 field value in the process, and the "from entry" is deleted.
- If there is a "from entry" and a "to entry", the "from entry" is deleted and the "to entry" remains unchanged.

If it is determined that a developer *must* have their own unique merge that deals with their files, they *must* make the appropriate entries in the PACKAGE (#9.4) file. If they must have some sort of action taken by end-users prior to the merging of the records, they *must* update the MERGE PACKAGES Multiple in the DUPLICATE RECORD (#15) file for that pair of records.

The following explains the entries that need to be made in the PACKAGE (#9.4) file:

- In your PACKAGE (#9.4) file make an entry in the AFFECTS RECORD MERGE (#20) field.
- In the .01 field, enter the file affected (such as PATIENT \[#2\] file).
- In the NAME OF MERGE ROUTINE (#9.402,3) field enter the name of your merge routine, which is executed through indirection by Duplicate Resolution Utilities. If you leave this field blank but still place an entry in the PACKAGE (#9.4) file, Duplicate Resolution Utilities assumes that you have some sort of interactive merge process that your end users must complete prior to the main merge occurring. It also assumes that this interactive merge process is on a separate option within the developer's package options. The values of the two records being merged are placed in:

^TMP("XDRMRGFR",\$J,XDRMRG("FR")

And

^TMP("XDRMRGTO",\$J,XDRMRG("TO")

These should be referenced by the developer if they need any certain field values since the values may have been changed prior to the execution of their merge routine.

- In the RECORD HAS PACKAGE DATA (#9.402,4) field you would enter a string of M executable code that is passed the XDRMRG("FR") variable (the "from record" IEN) and set XDRZ to 0. The code should SET XDRZ=1 if XDRMRG("FR") has data within your package files.

Remember to only make these entries in the PACKAGE (#9.4) file if the normal merge does *not* suffice for your package. If you have an entry in the PACKAGE (#9.4) file, the repointing and merging as described above does *not* take place for those files within your package entry.

If you leave the NAME OF MERGE ROUTINE (#9.402,3) field blank, it is assumed that you have some sort of interactive merge process that must occur prior to the main merging of the two records. At the completion of your interactive merge process the developer *must* set the STATUS (#15.01101,.02) field of the MERGE PACKAGES (#15,1101) Multiple field for their package in the DUPLICATE RECORD (#15) file entry to Ready. This *must* be done using VA FileMan, because of the trigger that is on the STATUS (#15.01101,.02) field. Once all MERGE PACKAGE entries have a STATUS of Ready, the main merging of the two records can occur.

## Configuring VAX/Alpha Performance Monitor (VPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data from the VAX/Alpha Performance Monitor is stored in the ^XUCM global. This global grows at a rate of approximately 80k/day/node. A task can be queued to automatically keep this global purged. Raw data occupies most of this growth rate and can be retained a shorter period (1-3 months), while the daily averages in the CM DAILY STATISTICS (#8986.6) file should be retained considerably longer. This ensures its usefulness for trend analysis and other computations.

The VAX/Alpha Performance Monitor (VPM) requires that TaskMan be set to run with a DCL context *prior* to configuring the performance monitor's site files. To configure the CM SITE PARAMETERS (#8986.095) and CM SITE NODENAMES (#8986.3) files, run the Setup Performance Monitor option.

After editing these files, the host directory and DCL command files (XUCMVPM.COM and XUCMMONITOR.COM) are created by TaskMan. An alert is sent to you once this is complete. Re-run this option whenever CPUs are added/removed from your configuration.

Using the TaskMan Schedule/Unschedule Options \[XUTM SCHEDULE\] option queue XUCM TASK VPM to run *hourly*. This option is the data collection driver for the VMS Monitor and checks for and loads new data into the CM DISK DRIVE RAW DATA (#8986.5) and CM NODENAME RAW DATA (#8986.51) files. Each data collection runs for 15 minutes using 10 second sample intervals (rather than the default 3 second interval). Queue the XUCM TASK NIT option to run in the early a.m., (such as 0001 hours). This option compiles workday averages, mails server messages, and collects "static" information (such as node and hardware types). Finally, this option files selected RTHIST data and restarts RTHIST data collections for the next 24 hours.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides information related to all executable routines exported with Kernel and Kernel Toolkit. Do *not* delete any routines except any initialization routines, which *can* be deleted *after* installation.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/034.png) NOTE: This chapter lists the routines alphabetically and by category. Other routine information, such as the Routine Description, Size Histogram, Routine %Index, and so on, can be generated using Kernel Utilities.

## Manager Account Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> lists the Manager Account routines:

| Routine      | Description                                                                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| %ZIS     | Device Handler.                                                                                                                                                                   |
| %ZIS1    | Device Handler: Device input.                                                                                                                                                     |
| %ZIS2    | Device Handler: Checks.                                                                                                                                                           |
| %ZIS3    | Device Handler: Device types and parameters.                                                                                                                                      |
| %ZIS5    | Device lookup.                                                                                                                                                                    |
| %ZIS6    | Device Handler: Resources.                                                                                                                                                        |
| %ZIS7    | Device Handler: Help.                                                                                                                                                             |
| %ZISC    | Close logic for devices.                                                                                                                                                          |
| %ZISP    | Collect screen parameters: Graphic set.                                                                                                                                           |
| %ZISS    | Collect screen parameters.                                                                                                                                                        |
| %ZISS1   | Collect screen parameters (continued).                                                                                                                                            |
| %ZISS2   | Collect screen parameters: Graphic set.                                                                                                                                           |
| %ZISUTL  | Device Handler: Utility routine.                                                                                                                                                  |
| %ZTER    | Kernel Error Trap to log errors.                                                                                                                                                  |
| %ZTER1   | Kernel Error Trap to log errors (continued).                                                                                                                                      |
| %ZTLOAD  | TaskMan: Application Program Interface: Entry Points.                                                                                                                             |
| %ZTLOAD1 | TaskMan: Application Program Interface: Part 1: Queue.                                                                                                                        |
| %ZTLOAD2 | TaskMan: Application Program Interface: Part 2: Queue.                                                                                                                        |
| %ZTLOAD3 | TaskMan: Task Requeue.                                                                                                                                                            |
| %ZTLOAD4 | TaskMan: Application Program Interface: Is Queued?                                                                                                                                |
| %ZTLOAD5 | TaskMan: Application Program Interface: Task status.                                                                                                                              |
| %ZTLOAD6 | TaskMan: Application Program Interface: Dequeue.                                                                                                                                  |
| %ZTLOAD7 | TaskMan: Utilities.                                                                                                                                                               |
| %ZTM     | TaskMan: Manager: Part 1: Main Loop.                                                                                                                                          |
| %ZTM0    | TaskMan: Manager: Part 2: Begin.                                                                                                                                              |
| %ZTM1    | TaskMan: Manager: Part 3: Validate Task.                                                                                                                                      |
| %ZTM2    | TaskMan: Manager: Part 4: Link Handling 1.                                                                                                                                |
| %ZTM3    | TaskMan: Manager: Part 5: Link Handling 2.                                                                                                                                |
| %ZTM4    | TaskMan: Manager: Part 6: Waiting List.                                                                                                                                       |
| %ZTM5    | TaskMan: Manager: Part 7: Short Subroutines.                                                                                                                                  |
| %ZTM6    | TaskMan: Manager: Part 8: Load Balancing.                                                                                                                                     |
| %ZTMOVE  | Easier multi-CPU routine transfers.                                                                                                                                               |
| %ZTMS    | TaskMan: Submanager: Part 1: Entry and Trap functions.                                                                                                                        |
| %ZTMS0   | TaskMan: Submanager: Part 2: Trap functions.                                                                                                                                  |
| %ZTMS1   | TaskMan: Submanager: Part 3: Loop and Get Task.                                                                                                                               |
| %ZTMS2   | TaskMan: Submanager: Part 4: Unload, Get Device.                                                                                                                              |
| %ZTMS3   | TaskMan: Submanager: Part 5: Run Task.                                                                                                                                        |
| %ZTMS4   | TaskMan: Submanager: Part 6: Setup, Cleanup.                                                                                                                                  |
| %ZTMS7   | TaskMan: Submanager: GetNext.                                                                                                                                                     |
| %ZTMSH   | TaskMan: Submanager: Utility: Header Page.                                                                                                                                        |
| XUCIDTM  | Swap UCIs DSM-11.                                                                                                                                                                 |
| XUCIMSM  | Swap UCIS for MSM-UNIX.                                                                                                                                                           |
| XUCIMSQ  | Swap UCIs M/SQL.                                                                                                                                                                  |
| XUCIVXD  | Swap UCIs VAX/DSM.                                                                                                                                                                |
| ZIS4VXD  | Device Handler: Spool specific code (VAX DSM).                                                                                                                                    |
| ZISETDTM | Initialize DEVICE (#3.5) file for D7. This routine initializes the DEVICE (#3.5) file with the current port number or updates the device file if new hardware has been added. |
| ZISETMSM | Initialize DEVICE (#3.5) file for MSM-68. This routine initializes the DEVICE (#3.5) file with the current port number.                                                           |
| ZISETVXD | Initialize DEVICE (#3.5) file. This routine initializes the DEVICE (#3.5) file with the current port number.                                                                      |
| ZISFMSM  | HOST files: Code for MSM.                                                                                                                                                         |
| ZISFVXD  | HOST files: Code for VAX DSM.                                                                                                                                                     |
| ZISHMSM  | Host files: Control for MSM.                                                                                                                                                      |
| ZISHVXD  | VAX DSM Host file control.                                                                                                                                                        |
| ZISX     | Executes nodes in the ^%ZIS global.                                                                                                                                           |
| ZOSFMSM  | Sets up ^%ZOSF for MSM-UNIX systems.                                                                                                                                          |
| ZOSFVXD  | ZOSF table for VAX DSM 3.3, 4, and 6.                                                                                                                                         |
| ZOSV2VXD | Capacity Management: Performance Data.                                                                                                                                            |
| ZOSVMSM  | MSM-PC/PLUS: \$View commands.                                                                                                                                                 |
| ZOSVVXD  | View commands and special functions.                                                                                                                                          |
| ZTBKCDTM | DTM: Block count.                                                                                                                                                                 |
| ZTBKCMSM | MSM: Block count.                                                                                                                                                                 |
| ZTBKCVXD | VAX DSM: Block count.                                                                                                                                                             |
| ZTMB     | TaskMan: Manager: Boot/ Option: ZTMRESTART.                                                                                                                                   |
| ZTMCHK   | TaskMan: Option: ZTMCHECK: Part 1.                                                                                                                                        |
| ZTMCHK1  | TaskMan: Option: ZTMCHECK: Part 2.                                                                                                                                        |
| ZTMDCL   | TaskMan: Run TaskMan with a DCL context.                                                                                                                                          |
| ZTMGRSET | Set up the Production account for the system.                                                                                                                                     |
| ZTMKU    | TaskMan: Option: ZTMWAIT/RUN/STOP.                                                                                                                                            |
| ZTMON    | TaskMan: Option: ZTMON: Part 1: Main Loop.                                                                                                                                |
| ZTMON1   | TaskMan: Option: ZTMON: Part 2: Main Loop.                                                                                                                                |
| ZUA      | Audit access.                                                                                                                                                                     |

<span id="_Ref333475204" class="anchor"></span>Table 9: Routines—Kernel and Toolkit Production Account Routines

## Production Account Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 9</u> lists the Production account routines for Kernel and Toolkit:

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/035.png) NOTE: The Kernel and Kernel Toolkit routine namespaces include: “XDR\*,” “XG\*,” “XI\*,” “XLF\*,” “XPAR\*,” “XPD\*,” “XQ\*,” “XT\*,” “XU\*,” “ZIS\*,” “ZOS\*,” “ZTM\*,” and “ZU\*.”

<table>
<caption><p><span id="_Ref373831370" class="anchor"></span>Table 10: Routines—Kernel and Toolkit Production Account Routines Released with Broker Security Enhancement (BSE)</p></caption>
<colgroup>
<col style="width: 0%" />
<col style="width: 25%" />
<col style="width: 73%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th colspan="2">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XDR2NULL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRCNT</strong></td>
<td colspan="2">Tally records by STATUS and MERGE STATUS fields.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDADD</strong></td>
<td colspan="2"><p>This routine makes the entries in the DUPLICATE RECORD (#15) file.</p>
<p>Called by: <strong>XDRDUP</strong></p>
<p>Calls: <strong>FILE^DICN</strong>, <strong>DIE</strong>, <strong>EN^XDRMAIN</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDADDS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDADJ</strong></td>
<td colspan="2"><p>This routine is executed by a MUMPS cross-reference on the MERGE STATUS field of the DUPLICATE RECORD (#15) file only when the STATUS is set to <strong>Merged</strong>. This routine checks for entries in the file that are affected by the merging of this entry and adjusts their <strong>.01</strong> and <strong>.02</strong> fields accordingly. The problem being addressed is as follows:</p>
<ul>
<li><p><strong>1</strong> to <strong>5</strong> If <strong>5</strong> to <strong>10</strong> merged first, <strong>1</strong> to <strong>10</strong></p></li>
<li><p><strong>5</strong> to <strong>10</strong> then other entries would <strong>5</strong> to <strong>10</strong></p></li>
<li><p><strong>5</strong> to <strong>20</strong> be adjusted as follows: <strong>10</strong> to <strong>20</strong></p></li>
</ul>
<p>Or, if both <strong>1</strong> to <strong>5</strong> and <strong>1</strong> to <strong>10</strong> existed at the time of the merge, the <strong>1</strong> to <strong>5</strong> entry would be deleted.</p>
<p>The STATUS (#.03) field is re-indexed because it sets cross-references based on the values in the <strong>.01</strong> and <strong>.02</strong> fields. Triggers are <em>not</em> fired for the <strong>.01</strong>, <strong>.02</strong>, or <strong>.03</strong> fields.</p>
<p>Entries previously resolved are ignored.</p>
<p>Called by: Cross-reference on MERGE STATUS field of DUPLICATE RECORD (#15) file entry.</p>
<p>Calls: <strong>EN^XDRDUP</strong>, <strong>DIK</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDCOMP</strong></td>
<td colspan="2"><p>This routine compares <strong>two</strong> file records through the Duplicate Checker algorithm.</p>
<p>Calls: <strong>%ZIS</strong>, <strong>%ZISC</strong>, <strong>%ZTLOAD</strong>, <strong>DIC</strong>, <strong>DIR</strong>, <strong>EN^DITC</strong>, <strong>FILE^XDRDQUE</strong>, <strong>XDRDSCOR</strong>, <strong>XDRDUP</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDDATA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDEDT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDEFLG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDFPD</strong></td>
<td colspan="2">Find all potential duplicates for an entry in a file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDLIST</strong></td>
<td colspan="2"><p>This routine is responsible for the printing of various reports from the DUPLICATE RECORD (#15) file. It prints listings of potential duplicates, ready, and not ready to merge verified duplicates.</p>
<p>Calls: <strong>EN1^DIP</strong>, <strong>DIR</strong>, <strong>FILE^XDRDQUE</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDMAIN</strong></td>
<td colspan="2"><p>This is the main driver for the duplicate checking routines.</p>
<p>Calls: <strong>NOW^%DTC</strong>, <strong>DIE</strong>, <strong>DIK</strong>, <strong>XDRDPDTI</strong>, <strong>XDRDUP</strong>, <strong>XDREMSG</strong>, <strong>XDRMAINI</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDOC</strong></td>
<td colspan="2">Additional routine documentation.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDOC1</strong></td>
<td colspan="2"><strong>XDRDOC</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDOC2</strong></td>
<td colspan="2"><strong>XDRDOC</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDPDTI</strong></td>
<td colspan="2"><p>This routine is called by <strong>XDRDMAIN</strong> when the Potential Duplicate threshold has been raised. This routine <strong>$ORDER</strong>s through the "<strong>APOT</strong>" cross-reference on the DUPLICATE RECORD (#15) file and deletes all entries that have a DC Dupe Match Score that does <em>not</em> meet the Potential Duplicate Threshold value. It also updates the DC POTENTIAL DUPE THRESHOLD%. It should be noted that if a person changes the weights of the Duplicate Tests, they should delete all Potential Duplicates, Unverified and rerun the Duplicate Resolution search.</p>
<p>Called by: <strong>XDRDMAIN</strong></p>
<p>Calls: <strong>DIE</strong>, <strong>DIK</strong>, <strong>EN^XDRDUP</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDPICK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDPRE1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDPREL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDPRG2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDPRGE</strong></td>
<td colspan="2"><p>This routine enables the Duplicate Resolution Manager to purge the DUPLICATE RECORD (#15) file. They can purge Potential Duplicates, Verified Non-Duplicates, or both. Verified Duplicates <em>cannot</em> be purged until FileMan institutes some sort of archival or merged node.</p>
<p>Calls: <strong>%ZTLOAD</strong>, <strong>DIC</strong>, <strong>DIR</strong>, <strong>DIK</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDQUE</strong></td>
<td colspan="2"><p>This routine starts and stops the Duplicate Checking software when it is running in the background. If no search is running, it allows the user to queue a search to start up. If a search has been halted, they may continue the search starting at the point they halted.</p>
<p>Called by: <strong>XDRDCOMP</strong>, <strong>XDRDLIST</strong>, <strong>XDRDSCOR</strong>, <strong>XDRMADD</strong></p>
<p>(All these calls by above are if <strong>XDRFL</strong> is undefined)</p>
<p>Calls: <strong>%ZTLOAD</strong>, <strong>DIC</strong>, <strong>Y^DIQ</strong>, <strong>DIR</strong>, <strong>CHECK^XDRU1</strong>, <strong>XDRCNT</strong>, <strong>XDRDFPD</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDSCOR</strong></td>
<td colspan="2"><p>This routine sets the scores for the Duplicate Checking algorithm.</p>
<p>Called by: <strong>XDRDCOMP</strong>, <strong>XDRDFPD</strong>, <strong>XDRDUP</strong>, <strong>XDRMADD</strong>, <strong>XDRMAINI</strong></p>
<p>Calls: <strong>FILE^XDRDQUE</strong>, <strong>XDREMSG</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDSHOW</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDSTAT</strong></td>
<td colspan="2"><p>This routine displays the status of a particular search for duplicates.</p>
<p>Calls: <strong>DIC</strong>, <strong>Y^DIQ</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDUP</strong></td>
<td colspan="2"><p>This routine does the actual checking of two records and makes the determination if they are potential duplicates.</p>
<p>Called by: <strong>XDRDADJ</strong>, <strong>XDRDCOMP</strong>, <strong>XDRDMAIN</strong>, <strong>XDRMADD</strong></p>
<p>Calls: <strong>EN^DIQ1</strong>, <strong>XDRDADD</strong>, <strong>XDRDSCOR</strong>, <strong>XDREMSG</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDVAL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRDVAL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRDVAL2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDREMSG</strong></td>
<td colspan="2"><p>This routine is responsible for either sending error messages to the user, or if the calling routine is running in the background, it sends a bulletin to the people in the duplicate manager mail group if one is defined.</p>
<p>The meanings of <strong>XDRERR</strong> are as follows:</p>
<ul>
<li><p><strong>1—</strong>The candidate collection routine is undefined.</p></li>
<li><p><strong>2—</strong>The candidate collection routine is not present.</p></li>
<li><p><strong>3—</strong>The potential duplicate threshold is undefined.</p></li>
<li><p><strong>4—</strong>There are no duplicate tests entered for this duplicate resolution entry.</p></li>
<li><p><strong>5—</strong>The global root node in <strong>DIC</strong> is undefined.</p></li>
<li><p><strong>6—</strong>No entry in DUPLICATE RESOLUTION (#15.1) file for this file.</p></li>
<li><p><strong>7—</strong>The <strong>From</strong> and <strong>To</strong> records are undefined.</p></li>
<li><p><strong>8—</strong>The test routine is not present.</p></li>
<li><p><strong>9—</strong>The routine defined as the pre-merge routine is not present.</p></li>
<li><p><strong>10—</strong>The routine defined as the post-merge routine is not present.</p></li>
<li><p><strong>11—</strong>The routine defined as the verified msg routine is not present.</p></li>
<li><p><strong>12—</strong>The routine defined as the merged msg routine is not present.</p></li>
<li><p><strong>13—</strong>Non-interactive merge style not allowed with <strong>DINUM</strong> files for merge entries.</p></li>
</ul>
<p>Called by: <strong>XDRDMAIN</strong>, <strong>XDRDSCOR</strong>, <strong>XDRDUP</strong>, <strong>XDRMAINI</strong>, <strong>XDRU1</strong></p>
<p>Calls: <strong>XMB</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRHLP</strong></td>
<td colspan="2">Contains code for executable help from the DUPLICATE RECORD (#15) and DUPLICATE RESOLUTION (#15.1) files.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRLRFIX</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMADD</strong></td>
<td colspan="2"><p>Adds entries to the DUPLICATE RECORD (#15) file with a status of Verified Duplicates.</p>
<p>Calls: <strong>DIC</strong>, <strong>FILE^DICN</strong>, <strong>DIE</strong>, <strong>FILE^XDRDQUE</strong>, <strong>XDRDSCOR</strong>, <strong>XDRDUP</strong>, <strong>EN^XDRMAIN</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMAIN</strong></td>
<td colspan="2"><p>Main Driver for the merge portion of the Duplicate Merge Utilities.</p>
<p>Called by: <strong>XDRDADD</strong>, <strong>XDRMADD</strong></p>
<p>Calls: <strong>DIC</strong>, <strong>DIE</strong>, <strong>DIR</strong>, <strong>XDRMAINI</strong>, <strong>XDRMPACK</strong>, <strong>XDRMRG</strong>, <strong>XDRMSG</strong>, <strong>XDRMVFY</strong></p>
<ul>
<li><p><strong>EN—</strong>Entry point for automatic merge.</p></li>
<li><p><strong>EN1—</strong>Entry point for looping through verified ready to merge duplicates.</p></li>
<li><p><strong>EN2—</strong>Entry point to select verified ready to merge duplicate pair.</p></li>
<li><p><strong>EN3—</strong>Entry point to select unverified potential duplicate pair.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMAINI</strong></td>
<td colspan="2"><p>Initialization routine for <strong>XDRMAIN</strong> and <strong>XDRDMAIN</strong>.</p>
<p>Called by: <strong>XDRDMAIN</strong>, <strong>XDRMAIN</strong></p>
<p>Calls: <strong>DIC</strong>, <strong>XDRDSCOR</strong>, <strong>XDREMSG</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMERG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMERG0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMERG1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMERG2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMERGA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMERGB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMERGC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMPACK</strong></td>
<td colspan="2"><p>This routine is responsible for checking PACKAGE (#9.4) file for unique package merges and for checking these package's files to see if they have data for the merged "from" record.</p>
<p>Called by: <strong>XDRMAIN</strong></p>
<p>Calls: <strong>DIE</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMRG</strong></td>
<td colspan="2"><p>This is the routine that does the actual merging of the duplicate records.</p>
<p>Called by: <strong>XDRMAIN</strong></p>
<p>Calls: <strong>DIE</strong>, <strong>DIK</strong>, <strong>EN^DIT0</strong>, <strong>DITM2</strong>, <strong>EN^DITMGMRG</strong>, <strong>LOCK^XDRU1</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMRG1</strong></td>
<td colspan="2"><p>This routine is the error trap for <strong>XDRMRG</strong>.</p>
<p>Calls: <strong>%ET</strong>, <strong>DIE</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRMSG</strong></td>
<td colspan="2"><p>This routine is responsible for the sending of the verified and merged messages.</p>
<p>Called by: <strong>XDRMAIN</strong></p>
<p>Calls: <strong>XMB</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRMVFY</strong></td>
<td colspan="2"><p>This routine is responsible for verifying potential duplicates.</p>
<p>Called by: <strong>XDRMAIN</strong></p>
<p>Calls: <strong>DIE</strong>, <strong>DIR</strong>, <strong>EN^DITC</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPREL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRPREI</strong></td>
<td colspan="2">This is a pre-<strong>init</strong> routine for the <strong>XDR</strong> package that deletes the DUPLICATE RECORD (#15) and DUPLICATE RESOLUTION (#15.1) files' dictionaries.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPTCAN</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRPTCLN</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPTDOB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRPTDOD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPTLSD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRPTMMN</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPTN</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRPTSSN</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRPTSX</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRRMRG0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRRMRG1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRRMRG2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRU</strong></td>
<td colspan="2"><p>This routine is a utility routine for the merge software; it does some testing for the merge software and provides the locking subroutines for the merge.</p>
<p>Called by: <strong>XDRDQUE</strong>, <strong>XDRMRG</strong></p>
<p>Calls: <strong>XDREMSG</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XDRUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XDRVCHEK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XGF</strong></td>
<td colspan="2">Graphics functions.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XGFDEMO</strong></td>
<td colspan="2">Demonstrate graphics functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XGFDEMO1</strong></td>
<td colspan="2">Demonstrate graphics functions (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XGKB</strong></td>
<td colspan="2">Read with escape processing.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XGKB1</strong></td>
<td colspan="2">Read with escape processing (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XGS</strong></td>
<td colspan="2">Screen primitives.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XGSA</strong></td>
<td colspan="2">Screen attribute primitives.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XGSBOX</strong></td>
<td colspan="2">Screen rectangular region primitives.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XGSETUP</strong></td>
<td colspan="2">Set up KWAPI environment.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XGSW</strong></td>
<td colspan="2">Screen window primitives.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDEX</strong></td>
<td colspan="2">The <strong>XIND*</strong> series of routines is the VA Cross-referencer. These routines are saved in the Manager's account as <strong>%IND*</strong> routines.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX1</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX10</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX11</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX2</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX3</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX4</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX5</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX51</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX52</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX53</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX6</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX7</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XINDX8</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XINDX9</strong></td>
<td colspan="2"><strong>%INDEX</strong> continued.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XIPENV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XIPMAIL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XIPMAILA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XIPMAILB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XIPPOST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XIPSRVR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XIPSYNC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XIPUTIL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XIPUTIL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XIPXREF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFCRC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFDT</strong></td>
<td colspan="2"><strong>DATE/TIME</strong> functions.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFDT1</strong></td>
<td colspan="2"><strong>DATE/TIME</strong> functions (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFDT2</strong></td>
<td colspan="2"><strong>DATE/TIME</strong> functions: Schedule.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFDT3</strong></td>
<td colspan="2"><strong>DATE/TIME</strong> functions: Schedule (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFDT4</strong></td>
<td colspan="2"><strong>DATE/TIME</strong> functions: Exclude time.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFHYPER</strong></td>
<td colspan="2">Hyperbolic math functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFIPV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFLTR</strong></td>
<td colspan="2">Print big letters.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFLTR1</strong></td>
<td colspan="2">Set up letters.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFMSMT</strong></td>
<td colspan="2">Measurement functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFMSMT2</strong></td>
<td colspan="2">Measurement functions (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFMTH</strong></td>
<td colspan="2">Math functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFMTH1</strong></td>
<td colspan="2">Math functions (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNAME</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNAME1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNAME2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNAME3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNAME4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNAME5</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNAME6</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNAME7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNAME8</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNENV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNP152</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFNP176</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFNSLK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFSHAN</strong></td>
<td colspan="2">Secure Hash Algorithm (SHA) APIs.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XLFSTR</strong></td>
<td colspan="2">String functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XLFUTL</strong></td>
<td colspan="2">Utility functions: Check digit.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPAR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPAR1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPAR2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPAR3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPARDD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPARDD1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPARDD2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPARDDAC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPAREDIT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPAREDT1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPAREDT2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPAREDT3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPARLIST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPARTPV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPARTPV1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPARY26</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPARZUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XPDANLYZ1_Routine" class="anchor"></span><strong>XPDANLYZ1</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span id="XPDANLYZ2_Routine" class="anchor"></span><strong>XPDANLYZ2</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XPDANLYZ3_Routine" class="anchor"></span><strong>XPDANLYZ3</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span id="XPDANLYZ4_Routine" class="anchor"></span><strong>XPDANLYZ4</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XPDANLYZ5_Routine" class="anchor"></span><strong>XPDANLYZ5</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span id="XPDANLYZ6_Routine" class="anchor"></span><strong>XPDANLYZ6</strong></td>
<td>VistA Build Analyzer Utility. Released with Kernel Patch XU*8.0*782.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDB1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDCOM</strong></td>
<td colspan="2">Compare transport global.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDCOMF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDCOMG</strong></td>
<td colspan="2">Compare globals.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDCOML</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDCPU</strong></td>
<td colspan="2">Code that updates each CPU.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDDCS</strong></td>
<td colspan="2">Display checksum for a package.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDDI</strong></td>
<td colspan="2">KIDS: Display an installation.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDDP</strong></td>
<td colspan="2">KIDS: Display a package.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDDP1</strong></td>
<td colspan="2">KIDS: Display a package.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDDPCK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDE</strong></td>
<td colspan="2">KIDS: Package edit.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDER</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDET</strong></td>
<td colspan="2">KIDS: Input transforms and help for the BUILD (#9.6) file and INSTALL (#9.7) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDGCDEL</strong></td>
<td colspan="2">KIDS: Delete specified objects, if <em>not</em> required.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDH</strong></td>
<td colspan="2">KIDS: Help for answering installation questions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDI</strong></td>
<td colspan="2">KIDS: Installation process.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDI1</strong></td>
<td colspan="2">KIDS: Installation process (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIA</strong></td>
<td colspan="2">KIDS: Install pre/post actions for Kernel Files.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIA0</strong></td>
<td colspan="2">KIDS: Install pre/post actions for Kernel Files (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIA1</strong></td>
<td colspan="2">KIDS: Install pre/post actions for Kernel Files (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIA2</strong></td>
<td colspan="2">KIDS: Delete options and clean up <strong>POINTER</strong>s.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIA3</strong></td>
<td colspan="2">KIDS: Delete options and clean up <strong>POINTER</strong>s.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDID</strong></td>
<td colspan="2">KIDS: Display installation progress.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIGP</strong></td>
<td colspan="2">KIDS: Load global distribution.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIJ</strong></td>
<td colspan="2">KIDS: Installation job.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIJ1</strong></td>
<td colspan="2">KIDS: Installation job.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIK</strong></td>
<td colspan="2">KIDS: Install Kernel files and VA FileMan files.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIL</strong></td>
<td colspan="2">KIDS: Load distribution global.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIL1</strong></td>
<td colspan="2">KIDS: Load distribution global (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN001</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN002</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN003</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN004</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN005</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN006</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN007</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN008</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN009</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00A</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00B</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00C</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00D</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00E</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00F</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00G</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00H</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00I</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00J</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00K</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00L</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00M</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00N</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00O</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00P</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00Q</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00R</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIN00S</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIN00T</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDINIT</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDINIT1</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDINIT2</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDINIT3</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDINIT4</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDINIT5</strong></td>
<td colspan="2">KIDS: Init routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIP</strong></td>
<td colspan="2">KIDS: Install PACKAGE (#9.4) and ROUTINE (#9.8) file.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIPM</strong></td>
<td colspan="2">KIDS: Load a Packman message.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIQ</strong></td>
<td colspan="2">KIDS: Install questions.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIR</strong></td>
<td colspan="2">KIDS: Install restart.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDIST</strong></td>
<td colspan="2">KIDS: Site tracking.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDIU</strong></td>
<td colspan="2">KIDS: Unload/Convert/Rollup distribution global.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDKEY</strong></td>
<td colspan="2">KIDS: Tools to work on keys.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDKRN</strong></td>
<td colspan="2">KIDS: Installation program.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDMENU</strong></td>
<td colspan="2">KIDS: Manage menu items.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDNTEG</strong></td>
<td colspan="2">KIDS: Package checksum checker.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDPINIT</strong></td>
<td colspan="2">KIDS: Load a Packman message using KIDS.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDPROT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDR</strong></td>
<td colspan="2">KIDS: Routine file edit.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDRSUM</strong></td>
<td colspan="2">KIDS: Routine checksum utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDT</strong></td>
<td colspan="2">KIDS: Transport a package.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDTA</strong></td>
<td colspan="2">KIDS: Build actions for Kernel files.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDTA1</strong></td>
<td colspan="2">KIDS: Build actions for Kernel files (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDTA2</strong></td>
<td colspan="2">KIDS: Build actions for Kernel files (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDTC</strong></td>
<td colspan="2">KIDS: Transport calls.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDTP</strong></td>
<td colspan="2">KIDS: Transport using a Packman message.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDUTL</strong></td>
<td colspan="2">KIDS: Returns parameters of check point.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XPDUTL1</strong></td>
<td colspan="2">KIDS: Returns parameters of check point.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XPDV</strong></td>
<td colspan="2">KIDS: Verify build.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ</strong></td>
<td colspan="2">MenuMan: Menu driver: Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ1</strong></td>
<td colspan="2">MenuMan: Menu driver: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ11</strong></td>
<td colspan="2">MenuMan: Menu utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ12</strong></td>
<td colspan="2">MenuMan: Utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ2</strong></td>
<td colspan="2">MenuMan: Menu lister and utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ21</strong></td>
<td colspan="2">MenuMan: Option: <strong>XUUSERDISP</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ3</strong></td>
<td colspan="2">MenuMan: Clean up dangling <strong>POINTER</strong>s in option or help frame files.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ31</strong></td>
<td colspan="2">MenuMan: Menu management reports.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ32</strong></td>
<td colspan="2">MenuMan: List users with specified menu.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ33</strong></td>
<td colspan="2">MenuMan: Remove unreferenced options.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ4</strong></td>
<td colspan="2">MenuMan: Menu diagram with entry/exit actions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ41</strong></td>
<td colspan="2">MenuMan: Menu diagram with entry/exit actions (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ5</strong></td>
<td colspan="2">MenuMan: Menu edit utilities <strong>Edit Option</strong> [XUEDITOPT].</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ55</strong></td>
<td colspan="2">MenuMan: Search for user’s access to an option.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XW55SPEC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ6</strong></td>
<td colspan="2">MenuMan: Bulk key distribution.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ61</strong></td>
<td colspan="2">MenuMan: Bulk editorship assignment.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ62</strong></td>
<td colspan="2">MenuMan: Generalized file lookup utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ6A</strong></td>
<td colspan="2">MenuMan: Bulk key distribution (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ6B</strong></td>
<td colspan="2">MenuMan: Bulk key distribution (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ7</strong></td>
<td colspan="2">MenuMan: Microsurgery of <strong>XUTL</strong> menu trees.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ71</strong></td>
<td colspan="2">MenuMan: Lookup response to menu prompt.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ72</strong></td>
<td colspan="2">MenuMan: Jump (<strong>“^</strong>) utilities: Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ72A</strong></td>
<td colspan="2">MenuMan: Jump (<strong>“^</strong>) utilities: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ73</strong></td>
<td colspan="2">MenuMan: Rubber Band Jump (<strong>^^</strong>) processor.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ74</strong></td>
<td colspan="2">MenuMan: Phantom Jump processor.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ75</strong></td>
<td colspan="2">MenuMan: Lookup response for jumps.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ8</strong></td>
<td colspan="2">MenuMan: Build menu trees.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ81</strong></td>
<td colspan="2">MenuMan: Build menu trees (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ82</strong></td>
<td colspan="2">MenuMan: Clean old <strong>$JOB</strong> data out of <strong>XUTL(“XQ”,</strong> and others.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ83</strong></td>
<td colspan="2">MenuMan: Find <strong>^XUTL</strong> nodes needing surgery.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ83A</strong></td>
<td colspan="2">MenuMan: Microsurgery on menu trees to add a new item to a menu.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ83D</strong></td>
<td colspan="2">MenuMan: Microsurgery on menu trees for item deleted from menu.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ83R</strong></td>
<td colspan="2">MenuMan: Microsurgery on <strong>^XUTL(“XQO”,</strong> nodes for regular modifications to options.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ88</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ8A</strong></td>
<td colspan="2">MenuMan: Rebuild menus in all production accounts.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ9</strong></td>
<td colspan="2">MenuMan: Restrict availability of options.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ91</strong></td>
<td colspan="2">MenuMan: Restrict availability of options (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQ92</strong></td>
<td colspan="2">MenuMan: <strong>DATE/TIME</strong> for prohibited Time/Day.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQ93</strong></td>
<td colspan="2">MenuMan: <strong>DATE/TIME</strong> for prohibited Time/Day (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQA366PO</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQABELOG</strong></td>
<td colspan="2">Alpha/Beta: Log alpha/beta errors received.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQABERR</strong></td>
<td colspan="2">Alpha/Beta: Track errors in alpha/beta routines back to OITFO.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQABLIST</strong></td>
<td colspan="2">Alpha/Beta: List usage of options in alpha/beta test.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQABLOAD</strong></td>
<td colspan="2">Alpha/Beta: Set up if alpha/beta test site.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQABTMP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQAL173P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQAL285P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALBUTL</strong></td>
<td colspan="2">Alerts: Utilities for OE/RR notifications.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALDATA</strong></td>
<td colspan="2">Alerts: Provide data on alerts.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALDEL</strong></td>
<td colspan="2">Alerts: Delete.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALDOIT</strong></td>
<td colspan="2">Alerts: Handler.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALERT</strong></td>
<td colspan="2">Alerts: Handler.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALERT1</strong></td>
<td colspan="2">Alerts: Handler.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALFWD</strong></td>
<td colspan="2">Alerts: Forward.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALGUI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALMAKE</strong></td>
<td colspan="2">Alerts: High level setup.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALSET</strong></td>
<td colspan="2">Alerts: Setup.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALSET1</strong></td>
<td colspan="2">Alerts: Setup.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALSUR1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQALSUR2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQALSURO</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQARPRT1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQARPRT2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQCHK</strong></td>
<td colspan="2">MenuMan: Check security on option # <strong>XQCY</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQCHK1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQCHK2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQCHK3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQCS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQDATE</strong></td>
<td colspan="2">MenuMan: Return Human readable date.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQH</strong></td>
<td colspan="2">MenuMan: Help Processor.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQH0</strong></td>
<td colspan="2">MenuMan: Help Processor (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQH1</strong></td>
<td colspan="2">MenuMan: Help Processor (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQH2</strong></td>
<td colspan="2">MenuMan: Help Processor (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQH3</strong></td>
<td colspan="2">MenuMan: Help frame cross-reference by parent.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQH4</strong></td>
<td colspan="2">MenuMan: Help frame lister.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQH5</strong></td>
<td colspan="2">MenuMan: Help frame lister (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQHLP</strong></td>
<td colspan="2">MenuMan: Menu helper.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQKEY</strong></td>
<td colspan="2">MenuMan: Key and lock utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQLOCK</strong></td>
<td colspan="2">MenuMan: Find all the keys in the tree.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQLOCK1</strong></td>
<td colspan="2">MenuMan: Utilities for keys in the tree.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOO</strong></td>
<td colspan="2">MenuMan: Out-of-Order, man.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQOO1</strong></td>
<td colspan="2">MenuMan: Out-of-Order set calls.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOO2</strong></td>
<td colspan="2">MenuMan: Out-of-Order manager utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQOO3</strong></td>
<td colspan="2">MenuMan: Out-of-Order utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOPED</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQOR</strong></td>
<td colspan="2">MenuMan: Prepare to unwind options.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOR1</strong></td>
<td colspan="2">MenuMan: Main unwinding loop.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQOR2</strong></td>
<td colspan="2">MenuMan: Process extended actions: Protocols.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOR3</strong></td>
<td colspan="2">MenuMan: Process Menus: Protocol menus.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQOR4</strong></td>
<td colspan="2">MenuMan: Process <strong>^^</strong> jump.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORD</strong></td>
<td colspan="2">MenuMan: Dialog utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORD1</strong></td>
<td colspan="2">MenuMan: Process Menus: WP during dialog.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORD101</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORDD1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORM</strong></td>
<td colspan="2">MenuMan: Menu utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORM1</strong></td>
<td colspan="2">MenuMan: Display selections and prompt.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORM2</strong></td>
<td colspan="2">MenuMan: Lookup for menu utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORM3</strong></td>
<td colspan="2">MenuMan: Lookup for menu utility (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORM4</strong></td>
<td colspan="2">MenuMan: Menu messages.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORM5</strong></td>
<td colspan="2">MenuMan: Menu help.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQORMX</strong></td>
<td colspan="2">MenuMan: Compile formatted menus.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQORO</strong></td>
<td colspan="2">MenuMan: Order Entry calls.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQOROP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQP46INI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQP50</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSET</strong></td>
<td colspan="2">MenuMan: Rebuild display/user <strong>XUTL(“XQO”)</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMD</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation (SMD): Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMD1</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMD2</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation: Part <strong>3</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMD21</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation: Part <strong>4</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMD3</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMD31</strong></td>
<td colspan="2">MenuMan: Secure Menu Delegation utilities (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMD4</strong></td>
<td colspan="2">MenuMan: Edit a user’s options.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMD5</strong></td>
<td colspan="2">MenuMan: Secure menu delegate edit user options.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMD6</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMDCPY</strong></td>
<td colspan="2">MenuMan: Copy one user (primary and secondary menus, keys, files) to another user.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSMDFM</strong></td>
<td colspan="2">MenuMan: Permit user to build limited VA FileMan options.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSMDP</strong></td>
<td colspan="2">MenuMan: Post Init for XQSMD Kernel 6.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSRV</strong></td>
<td colspan="2">MenuMan: Server message processor.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSRV1</strong></td>
<td colspan="2">MenuMan: Server option utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSRV2</strong></td>
<td colspan="2">MenuMan: Server task handler.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSRV3</strong></td>
<td colspan="2">MenuMan: Server to MailMan utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSRV4</strong></td>
<td colspan="2">MenuMan: Server utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSRV5</strong></td>
<td colspan="2">MenuMan: Check out a server option server.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSTCK</strong></td>
<td colspan="2">MenuMan: Stack utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQSUITE</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQSUITE1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQT</strong></td>
<td colspan="2">MenuMan: Menu template loader.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQT1</strong></td>
<td colspan="2">MenuMan: Menu template processor.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQT2</strong></td>
<td colspan="2">MenuMan: Define a path template.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQT3</strong></td>
<td colspan="2">MenuMan: Create menu templates (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQT4</strong></td>
<td colspan="2">MenuMan: Menu template utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQT5</strong></td>
<td colspan="2">MenuMan: Menu template utilities (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQTOC</strong></td>
<td colspan="2">MenuMan: Time Out/Continue/Jump Start.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQUIT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XQUSR</strong></td>
<td colspan="2">MenuMan: Option: <strong>Display User Characteristics</strong> [XUUSERDISP].</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XQUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT73P113</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XT73P129</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT73P132</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XT73P133</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT73P136</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XT73P33</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT73P34</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XT73P44</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT73P94</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XT73P98</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XT95POST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTDEBUG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTDEBUG1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTDEBUG2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTDEBUG3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTDEBUG4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTDEBUG5</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTDEBUG6</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTDEBUG7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTDEBUG8</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTECGLO</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTECLIPS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTECROU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTEDTVXD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTER</strong></td>
<td colspan="2">Error Processing: Option: <strong>Error Trap Display</strong> [XUERTRAP].</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTER1</strong></td>
<td colspan="2">Error Processing: Kernel Error Trap Display.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTER1A</strong></td>
<td colspan="2">Error Processing: VA error reporting.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTER1A1</strong></td>
<td colspan="2">Error Processing: VA error reporting (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTER1B</strong></td>
<td colspan="2">Error Processing: Package-specific variable identification.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTER2</strong></td>
<td colspan="2">Error Processing: Modification of <strong>%XTER</strong> for use with VAX DSM.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTERPUR</strong></td>
<td colspan="2">Error Processing: Delete entries from Error Trap.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTERSUM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTERSUM1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTERSUM3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTERSUM4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTFC1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTFCE</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTFCE1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTHC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTHC10</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTHC10A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTHCDEM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTHCURL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTHCUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTID</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTID1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTIDCTX</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTIDSET</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTIDTBL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTIDTERM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTIDTRM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTKERM1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTKERM2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTLATSET</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTMLOG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTMLOG1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTMLOPAR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTMLOSKT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTMRPAR1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTMRPAR2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTMRPRNT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTMUNIT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTPMKPCF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTPMKPP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTPMKPTC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTPMNEX7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTPMSTA2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTPMSTAT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTPOST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTRCMP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTRMON</strong></td>
<td colspan="2">Watch for changes in routine checksums.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTRUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTRUTL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTRUTL2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTSUMBLD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTSUMCK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XTSUMCK1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XTVNUM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><strong>XTVRC1</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XTVRC1A</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8343P</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8343Q</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8343R</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8343S</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8375P</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P125</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P132</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P1321Error! Bookmark not defined.</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P1322</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P135</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P137</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P204</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P246</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P260</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P264</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P264A</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P292</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P295</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P297</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P307</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P314</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P317</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P324</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P327</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P328</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P328A</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P328B</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P328C</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P328D</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P330X</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P332</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P334</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P344</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P352</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P354</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P356</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P360</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P365</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P369</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P370</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P373</strong></td>
<td colspan="2">TBD.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>XU8P377</strong></td>
<td colspan="2">This routine was exported with Kernel Patch XU*8.0*377. This routine inactivates old Person Class entries.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>XU8P377D</strong></td>
<td colspan="2"><p>This routine was exported with Kernel Patch XU*8.0*377. This routine lists all users that will have their Person Class inactivated by Kernel Patch XU*8.0*377. In the report, the column <strong>DISUSER</strong> will indicate either of the following:</p>
<ul>
<li><p><strong>NO—</strong>An active user account.</p></li>
<li><p><strong>YES—</strong>A <em>non</em>-active user account.</p></li>
</ul>
<p>Sites <em>must</em> manually update the new Person Class entries for these users.</p></td>
</tr>
<tr class="odd">
<td><strong>XU8P378</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P378A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P378B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P378C</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P378E</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P381</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P386</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P387</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P387X</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P410</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P413</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P420</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P426</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P428</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P432</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P436</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P43P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P440</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P444</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P446Error! Bookmark not defined.</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P452</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P453</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P455</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P459</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P463</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P466</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P467</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P467A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P469</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P480</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P481</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P483</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P487</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P497</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P497A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P499</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P504Error! Bookmark not defined.</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P509</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P509A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P509B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P509C</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P509D</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P511</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P514</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P518</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P524</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P531</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P531A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P531B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P536</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P540</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P541</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P541A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P543</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P545</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P545A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P546</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P560</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P571</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P572</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P580</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P581</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P582</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P584</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P585</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P586</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P591</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P598</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P599</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P601</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P601A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P601B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P604</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P608</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P608B</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P616</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8P638</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU8P672E</strong></td>
<td colspan="2">Kernel Patch XU*8.0*672 environment check routine.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XU8P689_Routine" class="anchor"></span><strong>XU8P689</strong></td>
<td colspan="2">Post install routine for Kernel Patch XU*8.0*689.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XU8P799_Routine" class="anchor"></span><strong>XU8P799</strong></td>
<td colspan="2">Kernel Patch XU*8.0*799 post-install routine that initializes the NEW PERSON FIELD MONITOR PURGE (#875) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file with a default value of <strong>365 (days)</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8PATCH661POST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XU8PE689_Routine" class="anchor"></span><strong>XU8PE689</strong></td>
<td colspan="2">Environment check routine for Kernel Patch XU*8.0*689.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XU8PS629</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUA4A7</strong></td>
<td colspan="2">Give entries into <strong>F6</strong> a Provider key.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUA4A71</strong></td>
<td colspan="2">Better Soundex. Extrinsic function call with string, returns converted string.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUA4A72</strong></td>
<td colspan="2"><p>Better Soundex. Extrinsic function call with string, returns converted string.</p>
<p>This routine was exported with Kernel Patch XU*8.0*27. This routine provides the Person Class APIs.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/036.png) <strong>REF:</strong> For more information on the Person Class APIs, see the <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>.</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUA4A73</strong></td>
<td colspan="2">Better Soundex. Extrinsic function call with string, returns converted string.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUAF4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUAPURGE</strong></td>
<td colspan="2">Purge <strong>%ZUA</strong> global files.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUBA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCERT</strong></td>
<td colspan="2">Kernel PKI Certificate Utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCERT1</strong></td>
<td colspan="2">Kernel PKI Certificate Utilities (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCIDTM</strong></td>
<td colspan="2">Swap UCIs: DSM-11.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCIGTM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCIMSM</strong></td>
<td colspan="2">Swap UCIs: MSM-UNIX.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCIMSQ</strong></td>
<td colspan="2">Swap UCIs: M/SQL.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCIONT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCIVXD</strong></td>
<td colspan="2">Swap UCIs: VAX/DSM.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMNIT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMNIT1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMNIT2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMNIT4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMNT3A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMPA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMPR17</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMVPI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMVPM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMVPM1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCMXDR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCMXUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS1E</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS1R</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS1RB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS2E</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS2R</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS2RB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS4E</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS4R</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS4RB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS6R</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS8E</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS8R</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCS8RB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCS8RG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSCDE</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSCDG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSCDR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSCDRB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSPRG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSRV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSTM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSTME</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSUTL3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSXCD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSXDR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSXGR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUCSXRT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUCSXST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUDHGUI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUDHRES</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUDHSET</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUDHUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUEPCSED</strong></td>
<td colspan="2">ePCS Utilities and Reports. RPC to handle ePCS data changes<br />
(Released with XU*8.0*580).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUEPCSRT</strong></td>
<td colspan="2">ePCS Utilities and Reports<br />
(Released with XU*8.0*580).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUEPCSU1</strong></td>
<td colspan="2">Routine supporting the manual entry of DEA information into the DEA Numbers (#8991.9) file. Released with Kernel Patch XU*8.0*689.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUEPCSUT_Routine" class="anchor"></span><strong>XUEPCSUT</strong></td>
<td colspan="2">Routine supporting the manual entry of DEA information into the DEA Numbers (#8991.9) file. Released with Kernel Patch XU*8.0*689.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUEPCSVR_Routine" class="anchor"></span><strong>XUEPCSVR</strong></td>
<td colspan="2">Routine supporting the ePCS Graphical User Interface (GUI) version check. Released with Kernel Patch XU*8.0*689.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUESSO1</strong></td>
<td colspan="2">Single Sign-On Utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUESSO2_Routine" class="anchor"></span><strong>XUESSO2</strong></td>
<td colspan="2">Enhanced Single Sign-On Utilities. This utility identifies a VistA user for auditing and Health Insurance Portability and Accountability Act (HIPAA) requirements. The SEX (#4) and DOB (#5) fields in the NEW PERSON (#200) file were updated with Kernel Patch XU*8.0*799.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUESSO3</strong></td>
<td colspan="2">Enhanced Single Sign-On Utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUESSO4</strong></td>
<td colspan="2">Enhanced Single Sign-On Utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUFILE</strong></td>
<td colspan="2">Assign and delete file access.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUFILE0</strong></td>
<td colspan="2">Assign and delete file access (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUFILE1</strong></td>
<td colspan="2">Assign and delete file access (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUFILE3</strong></td>
<td colspan="2">File access control for Kernel 8.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUGET</strong></td>
<td colspan="2">Package integrity checker.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUGOT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUGOT1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUHUI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUHUI236</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUHUIHL7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUHUIMSG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUIAMDD1_Routine" class="anchor"></span><strong>XUIAMDD1</strong></td>
<td colspan="2">This routine added as part of the Kernel Patch XU*8.0*799 contains the “<strong>AVIAM</strong>” cross-reference logic to create entries in the NEW PERSON FIELD MONITOR (#8933.1) file and is executed for the monitored fields in the NEW PERSON (#200) file that have been updated and need transmitted to Person Service Identity Management (PSIM).</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUIAMNPB_Routine" class="anchor"></span><strong>XUIAMNPB</strong></td>
<td colspan="2"><p>This routine added as part of the Kernel Patch XU*8.0*799 runs two options:</p>
<ul>
<li><p><a href="#XUS_IAM_NPFM_BATCH_UPDATE_Option">XUS IAM NPFM BATCH UPDATE</a></p></li>
<li><p><a href="#XUS_IAM_NPFM_PURGE_Option">XUS IAM NPFM PURGE</a></p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUIAMPR_Routine" class="anchor"></span><strong>XUIAMPR</strong></td>
<td colspan="2">Identity and Access Management (IAM) ProvisioningAdd/Update of a NEW PERSON. Kernel Patch XU*8.0*799 updated the Enterprise New Person Search logic to add a user to the NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUIAMPR1_Routine" class="anchor"></span><strong>XUIAMPR1</strong></td>
<td colspan="2">IAM ProvisioningAdd/Update of a NEW PERSON (Continued). Kernel Patch XU*8.0*799 updated the Enterprise New Person Search logic to add a user to the NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUIAMXML_Routine" class="anchor"></span><strong>XUIAMXML</strong></td>
<td colspan="2">IAM Enterprise NEW PERSON probabilistic search. Kernel Patch XU*8.0*799 added a new application programming interface (API) to query Person Service Identity Management (PSIM) for person with additional prompted traits (i.e., NAME, SSN, DOB, SEX) when the initial lookup by EMAIL or NETWORK USERNAME fails.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUIAMXML2_Routine" class="anchor"></span><strong>XUIAMXML2</strong></td>
<td colspan="2">Continuation of the IAM Enterprise NEW PERSON probabilistic search. Kernel Patch XU*8.0*799 added a new application programming interface (API) to query Person Service Identity Management (PSIM) for person with additional prompted traits (i.e., NAME, SSN, DOB, and SEX) when the initial lookup by EMAIL or NETWORK USERNAME fails.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINCON</strong></td>
<td colspan="2">Builds accessible file multiple.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINEACH</strong></td>
<td colspan="2">Code that needs to be run on each CPU.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINEND</strong></td>
<td colspan="2">Post Install for Kernel 8.0.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINENV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINOK</strong></td>
<td colspan="2">Check to see if it is OK to load.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINP275</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINP313</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINP337</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINP348</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINPCH</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINPCH2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINPCH3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINPCH4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINPRE</strong></td>
<td colspan="2">Kernel 8 pre-initialization.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINPRE1</strong></td>
<td colspan="2">Kernel 8 pre-initialization.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINTSK</strong></td>
<td colspan="2">TaskMan: Version 7.1 post-Init.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUINTSK1</strong></td>
<td colspan="2">TaskMan: Version 7.1 post-Init.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUINTSK2</strong></td>
<td colspan="2">Reschedule tasks in <strong>IO</strong>, <strong>JOB</strong>, <strong>LINK</strong> queues.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XULM</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XULM1</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XULMLD</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XULMLOG</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XULMOUT</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XULMP</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XULMRPC</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XULMU</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XULMUI</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XULMUI1</strong></td>
<td colspan="2">Kernel Lock Manger utility.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF04</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF04H</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF04P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF04Q</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF1H</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF218</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF218A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF218Z</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF261P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF299</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF333</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF382</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF390</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF397</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF416</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF479P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF4A</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF4H</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF4L0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF4L1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF4L2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF502</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF502P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF512F</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF555P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF5AT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF5AU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF5BYT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF5I</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF5II</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMF654</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF654P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFEIMF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFENV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFH</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFH4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFHM</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFHPQ</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFHPR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFI0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFMD5</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFMFE</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFMFI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFP4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFP4C</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFP4Z</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFP512</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFP513</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFPFT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFPMFS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFPOST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFPZL7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFQR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFX</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFXACK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFXH</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFXHL7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFXI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFXP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFXP1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMFXP2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMFXR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMPI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUMVIENU</strong></td>
<td colspan="2">Entry point and processing routine for the <strong>XUS MVI ENRICH NEW PERSON</strong> RPC for adding and updating a record in the NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMVINPA</strong></td>
<td colspan="2">Processing routine for adding a new record in the NEW PERSON (#200) file, which is associated with the <strong>XUS MVI ENRICH NEW PERSON</strong> RPC.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUMVINPU_Routine" class="anchor"></span><strong>XUMVINPU</strong></td>
<td colspan="2">This routine was modified with Kernel Patch XU*8.0*799 to validate that the National Provider Identifier (NPI) entry to be deleted is already populated in the EFFECTIVE DATE/TIME (#42) Multiple before attempting to delete it from the record in the NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUOAAHL7</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUOAAUTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUP</strong></td>
<td colspan="2">Set up environment for developers.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUP468</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUP522</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUP569</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUP807_Routine" class="anchor"></span><strong>XUP807</strong></td>
<td colspan="2">Kernel Patch XU*8.0*807 Post Install routine. Verifies the correct options are in place. See the Patch Description (PD).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPARAM</strong></td>
<td colspan="2">Look up parameter substitute, KSP values.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPCF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPCH117</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPCSRVR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPOS259</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPRE247</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPROD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPS309P</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSB01</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSCLR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSGS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSHL7B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSNAME</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSNM1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSORG</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSPAID</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSPD1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSPRA</strong></td>
<td colspan="2">Build PRA segment</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSQRY</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSSTF</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUPSUTL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUPSUTQ</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XURTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XURTL1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XURTL2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XURTL3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XURTLC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XURTLK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS</strong></td>
<td colspan="2">Signon.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUS1_Routine" class="anchor"></span><strong>XUS1</strong></td>
<td colspan="2">Signon. Kernel Patch XU*8.0*799 modified this routine so the LAST SIGN-ON DATE/TIME (#202) field is filed via VA FileMan (instead of hard set), so the cross-references fire.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS11</strong></td>
<td colspan="2">Read and store <strong>DA</strong> from terminals.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUS1A</strong></td>
<td colspan="2">Signon: Overflow from <strong>XUS1</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS1B</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUS2</strong></td>
<td colspan="2">Check or return user attributes.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS3</strong></td>
<td colspan="2">Signon.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUS3A</strong></td>
<td colspan="2">Change UCIs.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS4</strong></td>
<td colspan="2">Access Code generator.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUS5</strong></td>
<td colspan="2">Resume logic for continue.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS6</strong></td>
<td colspan="2">Clear users at startup.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUS9</strong></td>
<td colspan="2">Find a user.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUS91</strong></td>
<td colspan="2">Report of users signed on.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSAML</strong></td>
<td colspan="2">Kernel SAML Token Implementation.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSAP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSAP1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSBSE1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSBSE2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSC1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSC1C</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSC1S</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSC1S1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSCLEAN</strong></td>
<td colspan="2">Cleanup before exit.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSCNT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSECAD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSECBUL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSER</strong></td>
<td colspan="2">A common set of user functions.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSER1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUSER2_Routine" class="anchor"></span><strong>XUSER2</strong></td>
<td colspan="2">A common set of user functions.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUSER3_Routine" class="anchor"></span><strong>XUSER3</strong></td>
<td colspan="2">A common set of user functions.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSERBLK</strong></td>
<td colspan="2">Bulk user (NEW PERSON) computer access.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUSERNEW_Routine" class="anchor"></span><strong>XUSERNEW</strong></td>
<td colspan="2">Runs the <a href="#Add_a_New_User_to_the_System_Option"><strong>Add a New User to the System</strong></a> [<a href="#XUSERNEW_Option">XUSERNEW</a>] option. Patch XU*8.0*799 modified the <strong>Add a New User to the System</strong> [XUSERNEW] option to incorporate the Enterprise New Person Search logic to add users.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSERP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSESIG</strong></td>
<td colspan="2">Enter or change electronic signature code.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSESIG1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSESIG2</strong></td>
<td colspan="2"><p>Determines whether the <strong>XU SIG BLOCK DISABLE</strong> parameter is set to a value of <strong>ON</strong> (<strong>1</strong>), and whether the user is assigned the <strong>XUSIG</strong> security key. If the parameter is set to <strong>ON</strong>, users without the security key <em>cannot</em> edit the following Electronic Signature fields in the NEW PERSON (#200) file:</p>
<ul>
<li><p>DEGREE (#10.6)</p></li>
<li><p>SIGNATURE BLOCK PRINTED NAME (#20.2)</p></li>
<li><p>SIGNATURE BLOCK TITLE (#20.3)</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSESIG3</strong></td>
<td colspan="2">Edits entries for the DEGREE (#10.6) field in the NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSFACHK</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSG</strong></td>
<td colspan="2">Signon from GUI screen.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSG1</strong></td>
<td colspan="2">Signon from GUI screen (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSHSH</strong></td>
<td colspan="2">Password encryption.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSHSHP</strong></td>
<td colspan="2">Hashing routine for sig block in NEW PERSON (#200) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSKAAJ</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSKAAJ1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSMGR</strong></td>
<td colspan="2">Security utilities.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPI1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIDA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIE1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIE2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIE3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIED</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIUT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIX1</strong></td>
<td colspan="2">NPI extract report.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIX2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIX3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIX4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIX5</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIXI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSNPIXU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSP557</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUSPURGE_Routine" class="anchor"></span><strong>XUSPURGE</strong></td>
<td colspan="2">Purge routine for <strong>XUSEC</strong>. Kernel Patch XU*8.0*756 enhanced the <strong>SCPURG^XUSPURGE</strong> routine. It updated the <strong>Purge Sign-on Log</strong> [XUSCZONK] option so that it protects sign-on log entries for at least the number of days specified by the ISO or the default <strong>365 days</strong> as defined in the <a href="#SIGN_ON_LOG_RETENTION_sys_parameter"><strong>SIGN-ON LOG RETENTION (#221)</strong></a> parameter field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSRA</strong></td>
<td colspan="2">Remote access control.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSRB</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSRB1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSRB2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSRB4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSRB5</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSSPKI</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST01</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST02</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST04</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST05</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST06</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST08</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST09</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST12</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST13</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST15</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST17</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST18</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST19</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST20</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST21</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST22</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST24</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST25</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST26</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST27</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST28</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUST29</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUST35</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSTAT</strong></td>
<td colspan="2">User/CPU stats from signon log: Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSTAT1</strong></td>
<td colspan="2">User/CPU stats from signon log: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSTAT2</strong></td>
<td colspan="2">User/CPU stats from signon log: Part <strong>3</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSTAX</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUSTERM_Routine" class="anchor"></span><strong>XUSTERM</strong></td>
<td colspan="2">Deactivate user. Corrected issue in Kernel Patch XU*8.0*799 to allow subscribers to be called when a user is deactivated, and the “<strong>Purge</strong>” flag is <em><strong>not</strong></em> set.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSTERM1</strong></td>
<td colspan="2">Deactivate user (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSTERM2</strong></td>
<td colspan="2">User terminate, package file run</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUSTZ</strong></td>
<td colspan="2">Security Twilight Zone.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUSTZIP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMD</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMDEL</strong>: Part <strong>1</strong>: Single.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMD1</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMDEL</strong>: Part <strong>2</strong>: Bulk Delete.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMDEVQ</strong></td>
<td colspan="2">Device call and queue in one place.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMDQ</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMDQ</strong>: Part <strong>1</strong>: Single.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMDQ1</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMDQ</strong>: Part <strong>2</strong>: Bulk <strong>DQ</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMG145</strong></td>
<td colspan="2">TaskMan: Globals: Code for VOLUME SET (#14.5) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMG146</strong></td>
<td colspan="2">TaskMan: Globals: Cross-references for UCI ASSOCIATION (#14.6) file.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMG14P</strong></td>
<td colspan="2">TaskMan: Globals: Cross-references for VOLUME SET (#14.5) and MUMPS OPERATING SYSTEM (#.7) files.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMG19</strong></td>
<td colspan="2">TaskMan: Code for OPTION SCHEDULING (#19.2) file.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMG43</strong></td>
<td colspan="2">TaskMan: Globals: Cross-references for KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMHR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMK</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMCLEAN/ZTMQCLEAN</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMKA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMKE</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTME LOG*</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMKE1</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTME SCREEN*</strong>: Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMKE2</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTME SCREEN*</strong>: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMONH</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMON</strong>: Part <strong>3</strong>: Help Driver.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMONH1</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMON</strong>: Part <strong>4</strong>: Help Modules.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMONH2</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMON</strong>: Part <strong>5</strong>: Help Modules.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMOPT</strong></td>
<td colspan="2">One-time queue and Schedule option code.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMPCH</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMQ</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMINQ</strong>: Show task lists.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMQ0</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMINQ</strong>: Part <strong>2</strong>: Modules.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMQ1</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMINQ</strong>: Part <strong>3</strong>: Modules.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMQ2</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMINQ</strong>: Part <strong>4</strong>: Modules.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMQ3</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMINQ</strong>: Part <strong>5</strong>: Modules.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMQH</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMR</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMR1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMRJD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMRJD1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMRP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMRP1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMSYNC</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTA</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTAL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTDL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTED</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTEIO</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTEP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTES</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTLD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTLU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTP</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTP0</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTP1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTPD</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTPU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTR1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTR2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTR3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTR4</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTS</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTU</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTUL</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTZ</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTZ1</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMTZ2</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMTZ3</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMUSE</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMUSER</strong>: Part <strong>1</strong>: Driver.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMUSE1</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMUSER</strong>: Part <strong>2</strong>: Print.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMUSE2</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMUSER</strong>: Part <strong>3</strong>: Edit.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUTMUSE3</strong></td>
<td colspan="2">TaskMan: Option: <strong>XUTMUSER</strong>: Part <strong>3</strong>: Help.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUTMUTL</strong></td>
<td colspan="2">TaskMan: Utility.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUVERIFY</strong></td>
<td colspan="2">Checks a user’s Access and Verify Codes.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUWORKDY</strong></td>
<td colspan="2">Workdays: Monday – Friday.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUXCTY</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUXPRT</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUXTADAPI_Routine" class="anchor"></span><strong>XUXTADAPI</strong></td>
<td colspan="2">Service/Section APIs. This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUXTADAPI2_Routine" class="anchor"></span><strong>XUXTADAPI2</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUXTADAPI3_Routine" class="anchor"></span><strong>XUXTADAPI3</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUXTADASK1_Routine" class="anchor"></span><strong>XUXTADASK1</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUXTADDILG_Routine" class="anchor"></span><strong>XUXTADDILG</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUXTADDT1_Routine" class="anchor"></span><strong>XUXTADDT1</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUXTADPRT1_Routine" class="anchor"></span><strong>XUXTADPRT1</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUXTADPRT2_Routine" class="anchor"></span><strong>XUXTADPRT2</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="even">
<td><span id="XUXTADSSE_Routine" class="anchor"></span><strong>XUXTADSSE</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="odd">
<td><span id="XUXTADSSEF_Routine" class="anchor"></span><strong>XUXTADSSEF</strong></td>
<td colspan="2">This routine was released with Kernel Patch XU*8.0*807.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XUYDEV</strong></td>
<td colspan="2">TBD.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZISEDIT</strong></td>
<td colspan="2">Device edit.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZISPL</strong></td>
<td colspan="2">Utilities for spooling.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZISPL1</strong></td>
<td colspan="2">Utilities for spooling (continued).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZISPL2</strong></td>
<td colspan="2">Spooler cleanup.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZISX</strong></td>
<td colspan="2">Executes nodes in <strong>^%ZIS</strong> global.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZTMB</strong></td>
<td colspan="2">TaskMan: Manager: Boot/ Option: <strong>ZTMRESTART</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZTMCHK</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMCHECK</strong>: Part <strong>1</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZTMCHK1</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMCHECK</strong>: Part <strong>2</strong>.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZTMKU</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMWAIT/RUN/STOP</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZTMON</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMON</strong>: Part <strong>1</strong> (Main Loop).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZTMON1</strong></td>
<td colspan="2">TaskMan: Option: <strong>ZTMON</strong>: Part <strong>2</strong> (Main Loop).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZUA</strong></td>
<td colspan="2">Audit access.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZUMSM</strong></td>
<td colspan="2">MSM-NT and MSM-UNIX: Tie all user terminals to this routine.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZUVXD</strong></td>
<td colspan="2">DSM: Tie all terminals to this routine.</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref373831370" class="anchor"></span>Table 10: Routines—Kernel and Toolkit Production Account Routines Released with Broker Security Enhancement (BSE)

| Routine      | Description                                                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUSBSE1  | This Kernel routine contains various functions and procedures used by Broker Security Enhancement (BSE). It was released with the BSE (that is Kernel Patch XU\*1.1\*404). |
| XUSBSE2  | This Kernel routine contains various functions and procedures used by BSE. It was released with BSE (that is Kernel Patch XU\*1.1\*404).                                   |
| XUSBSEUT | This Kernel routine is the BSE unit test routine. It was released with BSE (that is Kernel Patch XU\*1.1\*404).                                                            |
| XUSRB    | This Kernel routine contains various functions and procedures used by BSE. It was modified and released with BSE (that is Kernel Patch XU\*1.1\*404).                      |

<span id="_Ref333475221" class="anchor"></span>Table 11: Routines—Virgin Installs

## Additional Routines Installed by Virgin Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 11</u> lists the additional XV routines that are brought in by a virgin installation for the production account:

| Routine      | Description                                 |
|--------------|---------------------------------------------|
| XVIRENV  | Environment check for virgin Installations. |
| XVIRPOST | Post Init for virgin installations.         |

<span id="_Ref333475291" class="anchor"></span>Table 12: Globals—VA FileMan-Compatible Storage

## Mapping Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine mapping; is at the discretion of the systems manager. The RTHIST routines provide a method for each site to determine the extent to which certain routines are used.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/037.png) REF: For a list of *recommended* routine mapping, see the “Installing Kernel 8.0 in a 7.1 Environment” section in the *Kernel Installation Guide*. Under the “Installation Instructions” section, see the “Implement Routine Mapping (DSM for OpenVMS only)” section. Recommended routines to map are listed there.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains information on all files and globals distributed with Kernel and Kernel Toolkit. The file information includes file numbers, file names, global location, and brief file descriptions.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/038.png) REF: <u>Table 14</u> lists other files that are brought in during a virgin installation.

File number ranges for Kernel and Kernel Toolkit are as follows:

- 3.05 – 3.084
- 3.1 - 3.54
- 4.00 - 4.11
- 5.00 - 5.00
- 7 - 7.1
- 9.2 - 9.8
- 10
- 11
- 13
- 14.4 - 14.8
- 15 – 15.4
- 19.00 – 19.2
- 40.5
- 49
- 101.00
- 200 – 201
- 8932.10 - 8935.91
- 8980 - 8980.22
- 8984.1 – 8984.4
- 8989.2 – 8989.3
- 8991 – 8992.1

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/039.png) REF: For a detailed list of the files exported with Kernel and Kernel Toolkit, see <u>Table 15</u>.

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Globals—VA-FileMan-Compatible Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Kernel/Kernel Toolkit globals are compatible with VA FileMan files. The Kernel/Kernel Toolkit files are listed in order of the global in which they are stored:

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/040.png) NOTE: In <u>Table 12</u>, those globals specific to Kernel Toolkit are notated under the “Global Name” column and those files specific to Kernel Toolkit within other globals are noted under the “File Number” column.

<table>
<caption><p><span id="_Ref87258684" class="anchor"></span>Table 13: Globals—<em>Not</em> VA FileMan-Compatible Storage</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Global Name</th>
<th>File Number</th>
<th>File Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>^DIC</strong></td>
<td>3.1</td>
<td>TITLE</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>INSTITUTION</td>
</tr>
<tr class="odd">
<td></td>
<td>4.1</td>
<td>FACILITY TYPE</td>
</tr>
<tr class="even">
<td></td>
<td>4.11</td>
<td>AGENCY</td>
</tr>
<tr class="odd">
<td></td>
<td>9.2</td>
<td>HELP FRAME</td>
</tr>
<tr class="even">
<td></td>
<td>9.4</td>
<td>PACKAGE</td>
</tr>
<tr class="odd">
<td></td>
<td>9.8</td>
<td>ROUTINE</td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td>OPTION</td>
</tr>
<tr class="odd">
<td></td>
<td>19.1</td>
<td>SECURITY KEY</td>
</tr>
<tr class="even">
<td></td>
<td>19.2</td>
<td>OPTION SCHEDULING</td>
</tr>
<tr class="odd">
<td></td>
<td>49</td>
<td>SERVICE/SECTION</td>
</tr>
<tr class="even">
<td><strong>^DIZ<br />
(Toolkit)</strong></td>
<td>8980</td>
<td>KERMIT HOLDING</td>
</tr>
<tr class="odd">
<td><strong>^HOLIDAY</strong></td>
<td>40.5</td>
<td>HOLIDAY</td>
</tr>
<tr class="even">
<td><strong>^XLM</strong></td>
<td>8993</td>
<td>XULM LOCK DICTIONARY</td>
</tr>
<tr class="odd">
<td></td>
<td>8993.1</td>
<td>XULM LOCK MANAGER PARAMETERS</td>
</tr>
<tr class="even">
<td></td>
<td>8993.2</td>
<td>XULM LOCK MANAGER LOG</td>
</tr>
<tr class="odd">
<td><strong>^XPD</strong></td>
<td>9.6</td>
<td>BUILD</td>
</tr>
<tr class="even">
<td></td>
<td>9.7</td>
<td>INSTALL</td>
</tr>
<tr class="odd">
<td><strong>^XT<br />
(Toolkit)</strong></td>
<td>8984.1</td>
<td>LOCAL KEYWORD</td>
</tr>
<tr class="even">
<td></td>
<td>8984.2</td>
<td>LOCAL SHORTCUT</td>
</tr>
<tr class="odd">
<td></td>
<td>8984.3</td>
<td>LOCAL SYNONYM</td>
</tr>
<tr class="even">
<td></td>
<td>8984.4</td>
<td>LOCAL LOOKUP</td>
</tr>
<tr class="odd">
<td><span id="XTV_Global" class="anchor"></span><strong>^XTV</strong></td>
<td>8933.1</td>
<td>NEW PERSON FIELD MONITOR</td>
</tr>
<tr class="even">
<td></td>
<td>8989.2</td>
<td>KERNEL PARAMETERS</td>
</tr>
<tr class="odd">
<td></td>
<td>8989.3</td>
<td>KERNEL SYSTEM PARAMETERS</td>
</tr>
<tr class="even">
<td></td>
<td>8991<br />
(Toolkit)</td>
<td>XTV ROUTINE CHANGES</td>
</tr>
<tr class="odd">
<td></td>
<td>8991.19<br />
(Toolkit)</td>
<td>XTV VERIFICATION PACKAGE</td>
</tr>
<tr class="even">
<td></td>
<td>8991.2<br />
(Toolkit)</td>
<td>XTV GLOBAL CHANGES</td>
</tr>
<tr class="odd">
<td></td>
<td>8991.5</td>
<td>XQAB ERRORS LOGGED</td>
</tr>
<tr class="even">
<td></td>
<td>8991.6</td>
<td>XUEPCS DATA FILE</td>
</tr>
<tr class="odd">
<td></td>
<td>8991.7</td>
<td>XUEPCS PSDRPH AUDIT FILE</td>
</tr>
<tr class="even">
<td></td>
<td>8991.8</td>
<td>DEA BUSINESS ACTIVITY CODES</td>
</tr>
<tr class="odd">
<td></td>
<td>8991.9</td>
<td>DEA NUMBERS</td>
</tr>
<tr class="even">
<td></td>
<td>8992</td>
<td>ALERT</td>
</tr>
<tr class="odd">
<td></td>
<td>8992.1</td>
<td>ALERT TRACKING</td>
</tr>
<tr class="even">
<td></td>
<td>8992.2</td>
<td>ALERT RECIPIENT TYPE</td>
</tr>
<tr class="odd">
<td></td>
<td>8992.3</td>
<td>ALERT CRITICAL TEXT</td>
</tr>
<tr class="even">
<td></td>
<td>8995.9</td>
<td>BINARY OBJECT</td>
</tr>
<tr class="odd">
<td><strong>^XUSEC</strong></td>
<td>3.081</td>
<td>SIGN-ON LOG</td>
</tr>
<tr class="even">
<td></td>
<td>19.081</td>
<td>AUDIT LOG FOR OPTIONS</td>
</tr>
<tr class="odd">
<td><strong>^VA</strong></td>
<td>15<br />
(Toolkit)</td>
<td>DUPLICATE RECORD</td>
</tr>
<tr class="even">
<td></td>
<td>15.1<br />
(Toolkit)</td>
<td>DUPLICATE RESOLUTION</td>
</tr>
<tr class="odd">
<td></td>
<td>200</td>
<td>NEW PERSON</td>
</tr>
<tr class="even">
<td><strong>^%ZIS</strong></td>
<td>3.2</td>
<td>TERMINAL TYPE</td>
</tr>
<tr class="odd">
<td></td>
<td>3.22</td>
<td>DA RETURN CODES</td>
</tr>
<tr class="even">
<td></td>
<td>3.23</td>
<td>LINE/PORT ADDRESS</td>
</tr>
<tr class="odd">
<td></td>
<td>3.5</td>
<td>DEVICE</td>
</tr>
<tr class="even">
<td></td>
<td>14.5</td>
<td>VOLUME SET</td>
</tr>
<tr class="odd">
<td></td>
<td>14.6</td>
<td>UCI ASSOCIATION</td>
</tr>
<tr class="even">
<td></td>
<td>14.7</td>
<td>TASKMAN SITE PARAMETERS</td>
</tr>
<tr class="odd">
<td></td>
<td>14.71</td>
<td>TASKMAN MONITOR</td>
</tr>
<tr class="even">
<td></td>
<td>14.72</td>
<td>TASKMAN SNAPSHOT</td>
</tr>
<tr class="odd">
<td><strong>^%ZISL</strong></td>
<td>3.54</td>
<td>RESOURCE</td>
</tr>
<tr class="even">
<td></td>
<td>14.8</td>
<td>TASK SYNC FLAG</td>
</tr>
<tr class="odd">
<td><strong>^%ZTER</strong></td>
<td>3.075</td>
<td>ERROR LOG</td>
</tr>
<tr class="even">
<td></td>
<td>3.076</td>
<td>ERROR MESSAGES</td>
</tr>
<tr class="odd">
<td><strong>^%ZTSK</strong></td>
<td>14.4</td>
<td>TASKS</td>
</tr>
<tr class="even">
<td><strong>^%ZUA</strong></td>
<td>3.05</td>
<td>FAILED ACCESS ATTEMPTS LOG</td>
</tr>
<tr class="odd">
<td></td>
<td>3.07</td>
<td>PROGRAMMER MODE LOG</td>
</tr>
</tbody>
</table>

<span id="_Ref87258684" class="anchor"></span>Table 13: Globals—*Not* VA FileMan-Compatible Storage

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/041.png) REF: There are other VA FileMan files stored in the ^DIC global. You should review the *VA FileMan Technical Manual* for information on those files.

### Globals—Non-VA-FileMan-Compatible Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several additional Kernel/Kernel Toolkit globals that are *not* compatible with VA FileMan files. These include the globals listed in <u>Table 13</u>:

| Global      | Description                                       |
|-------------|---------------------------------------------------|
| ^XTMP   | Storage location for inter-process temporary data |
| ^XUTL   | Compiled menu system                              |
| ^%ZOSF  | Operating system-specific information             |
| ^%ZTSCH | TaskMan schedule of tasks                         |

<span id="_Ref95191340" class="anchor"></span>Table 14: Globals—Storage Used for Additional Files during Virgin Installation

In addition, many Kernel and Kernel Toolkit routines make use of the ^TMP global for temporary storage space.

### Globals—Storage Used for Additional Files during Virgin Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 14</u> lists the additional global storage used by files brought in by Kernel 8.0 Virgin Install:

| Global Name | File Number | File Name                          |
|-------------|-------------|------------------------------------|
| ^DIC    | 4.2         | (Exported with MailMan) DOMAIN     |
|             | 5           | STATE                              |
|             | 7           | PROVIDER CLASS                     |
|             | 7.1         | SPECIALITY                         |
|             | 10          | RACE                               |
|             | 11          | MARITAL STATUS                     |
|             | 13          | RELIGION                           |
| ^XMB    | 3.8         | (Exported with MailMan) MAIL GROUP |

<span id="_Ref161620537" class="anchor"></span>Table 15: Files—Distributed with Kernel and Kernel Toolkit

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Kernel and Kernel Toolkit Export Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 15</u> lists the files exported with Kernel and Kernel Toolkit:

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/042.png) NOTE: In <u>Table 15</u>, those files exported with Kernel Toolkit are noted under the “File \#” column. Those files that are *not* notated are exported with Kernel.

<table style="width:100%;">
<caption><p><span id="_Ref87258807" class="anchor"></span>Table 16: Files—Kernel Virgin Installation Files</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 9%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>File #</th>
<th>File Name</th>
<th>Global Location</th>
<th>Description</th>
<th>Data w/ File</th>
<th>Data Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3.05</td>
<td>FAILED ACCESS ATTEMPTS LOG</td>
<td><strong>^%ZUA(3.05,</strong></td>
<td>Once the maximum signon attempts limit has been exceeded, an entry is made in this file to record all available information about the failed signon attempt. Information includes the <strong>DATE/TIME</strong>, CPU, UCI, device, and, if known, user. The text entered for each attempt is recorded when it does <em>not</em> match existing codes. This file is <em>not</em> cross-referenced.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.07</td>
<td>PROGRAMMER MODE LOG</td>
<td><strong>^%ZUA(3.07,</strong></td>
<td>Entrance into <strong>Programmer</strong> mode through the menu system is automatically logged in this file. It points to the NEW PERSON (#200) file to identify the user. It is <em>not</em> cross-referenced.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.075</td>
<td>ERROR LOG</td>
<td><strong>^%ZTER(1,</strong></td>
<td>This file maintains a log of the errors occurring during use of the system. Errors are entered into this log by the Error Trap established for the user by ZU or application programs calling <strong>%ZTER</strong> when an error occurs. The entries are all entered by the routine <strong>%ZTER</strong>. There is no need for a user to make a manual entry into this file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.076</td>
<td>ERROR MESSAGES</td>
<td><strong>^%ZTER(2,</strong></td>
<td>This file contains several of the abbreviations used to indicate the type of error encountered. The most important ones are those which are indicated as fatal errors warranting termination of the job after logging of the error.</td>
<td>YES</td>
<td>Merge</td>
</tr>
<tr class="odd">
<td>3.077</td>
<td>ERROR TRAP SUMMARY</td>
<td><strong>^%ZTER(3.077,</strong></td>
<td>This file captures the VistA errors at each site. These findings can be used locally and pushed to a central repository to help prioritize the efforts to seal up the hot spots in the applications.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.081</td>
<td>SIGN-ON LOG</td>
<td><strong>^XUSEC(0,</strong></td>
<td>This file records signon/signoff times by user, device, job, UCI, and CPU. It is cross-referenced by user, device, and signoff time.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.083</td>
<td>LOCKED IP or DEVICE</td>
<td><strong>^XUSEC(3,</strong></td>
<td><p>This file holds the IP address or domain name of a system that has failed to successfully signon within the limits imposed.</p>
<p>Once the lock out time has passed, the record is removed, so it would be normal for this file to have no records most of the time.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.084</td>
<td>FAILED SIGNON ATTEMPTS</td>
<td><strong>^XUSEC(4,</strong></td>
<td><p>This file holds the count of signon attempts from an IP address or domain. This is to prevent a user from disconnecting after each try.</p>
<p>Once a signon is successful, the record is removed, so it would be normal for this file to have no records most of the time.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.1</td>
<td>TITLE</td>
<td><strong>^DIC(3.1,</strong></td>
<td>This file can be used to indicate a user’s title. It is pointed to by the NEW PERSON (#200) file. It is only cross-referenced by name.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.2</td>
<td>TERMINAL TYPE</td>
<td><strong>^%ZIS(2,</strong></td>
<td>This file is pointed to by the Subtype field of the DEVICE (#3.5) file. This file can hold vendor-specific code to characterize a terminal type. For example, escape sequences can be entered in the Open and Close Execute fields to set pitch or font. This file is also pointed to by the NEW PERSON (#200) file to record signon subtype characteristics by user. Data is distributed with this file to support screen-handling capabilities. This data overwrites existing data for those terminal types of the same name. However, terminal types for printers are <em>not</em> affected, since the data that is distributed is for a subset of known CRTs. The Kernel Virgin Install distribution will seed a more complete set of terminal types including those for printers as well as CRTs. However, the Kernel Virgin Install should only be performed once and only on a system where there is no pre-existing Kernel. The data in this file is cross-referenced by name and synonym.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="odd">
<td>3.22</td>
<td>DA RETURN CODES</td>
<td><strong>^%ZIS(22,</strong></td>
<td>This file holds the translation between the ANSI DA return code and the name in the TERMINAL TYPE (#3.2) file that should be associated with the return code.</td>
<td>YES</td>
<td>Merge</td>
</tr>
<tr class="even">
<td>3.23</td>
<td>LINE/PORT ADDRESS</td>
<td><strong>^%ZIS(3.23,</strong></td>
<td>This file associates device(s)/subtype(s) with line/port addresses. The line/port address should be entered when editing the name field of this file. This address can be obtained by using the OS-specific function <strong>$ZIO</strong> on VAX DSM. To establish an association with a Device and Terminal Type, the DEVICE and SUBTYPE fields of this file <em>must</em> store the appropriate values that correspond to entries in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files. This file is cross-referenced by name and device.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.5</td>
<td>DEVICE</td>
<td><strong>^%ZIS(1,</strong></td>
<td>This file defines all input/output devices that can be accessed from this CPU (definitions are <em>not</em> account-specific). Each device is identified with a unique name. Each is associated with a <strong>$I</strong> value which may correspond with a hardware port or, on layered systems, a host file or directory. If there are several devices for the same volume set and <strong>$I</strong>, one may be given signon system status. This file is cross-referenced by name, <strong>$I</strong>, volume set (CPU), and signon/system device. It is also cross-referenced by local synonym, mnemonic, subtype, and form currently mounted.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.51</td>
<td>SPOOL DOCUMENT</td>
<td><strong>^XMB(3.51,</strong></td>
<td>This file stores the name of spool documents created by the Kernel spooler (that is <strong>%ZIS4</strong>) for all operating systems. It does <em>not</em> hold the text of the documents themselves. That text is first spooled to spool space, then moved into the <strong>^XMB</strong> global as a mail message. This file does, however, provide the mechanism for securing spool space for and during spooling. It is cross-referenced by NAME, USER, OTHER AUTHORIZED USERS, SPOOL DATA, and SPOOL NUMBER.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.519</td>
<td>SPOOL DATA</td>
<td><strong>^XMBS(3.519,</strong></td>
<td>This is the holding file for spool documents until moved to a mail message or deleted.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>3.54</td>
<td>RESOURCE</td>
<td><strong>^%ZISL(3.54</strong></td>
<td>This file is for internal use by TaskMan and the Device Handler in the sequential processing of tasks. Jobs that have been sent to a resource-type device are monitored according to fields in this file. To accommodate the Device Handler’s need to write to but rarely read from this file, the translated <strong>^%ZISL</strong> global is used. This file is cross-referenced by name and job number.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>3.6</td>
<td>BULLETIN</td>
<td><strong>^XMB(3.6,</strong></td>
<td><p>Bulletins are “Super” messages. Each Bulletin has a text and a subject just like a normal message. But, embedded within either the subject or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a Mail Group that is associated with the bulletin.</p>
<p>Bulletins are processed by MailMan either because of a special cross reference type of VA FileMan, or because of a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points.</p>
<p>VA FileMan sets up code that issues a bulletin automatically when the special cross-reference type is created. In either case, the parameters that go into the text and/or the subject make each bulletin unique.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>4</td>
<td>INSTITUTION</td>
<td><strong>^DIC(4,</strong></td>
<td>This file contains a listing of VA institutions. It is cross-referenced by name and station number. The Number field is no longer meaningful (it previously referenced the station number).</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>4.001</td>
<td>MASTER FILE PARAMETERS</td>
<td><strong>^DIC(4.001,</strong></td>
<td><p>The file holds parameters related to the Master File Server (MFS).</p>
<p>The parameters map HL7 segment data to standard FileMan data files. Local modifications to this file will seriously disrupt standard file updating and have negative consequences to existing VistA applications.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/043.png) CAUTION: Do <em>not</em> edit this file!</p></td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="even">
<td>4.005</td>
<td>MD5 Signature</td>
<td><strong>^DIC(4.005,</strong></td>
<td><p>This file stores parameters related to the <strong>MD5</strong> signature of the Master File Server (MFS).</p>
<p>For each domain (Allergy, Vitals), the parameters define the file’s fields to be included in <strong>MD5</strong> hash procedure. Local modifications to this file will seriously disrupt standard file updating and have negative consequences to existing VistA applications.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/044.png) CAUTION: Do <em>not</em> edit this file!</p></td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td>4.009</td>
<td>STANDARD TERMINOLOGY VERSION F</td>
<td><strong>^DIC(4.009,</strong></td>
<td><p>This file stores the last Version of Standard Terminology update.</p>
<p>The file entry is set within MFS. Local modifications to this file will seriously disrupt standard file updating and have negative consequences to existing VistA applications.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/045.png) CAUTION: Do <em>not</em> edit this file!</p></td>
<td>YES</td>
<td></td>
</tr>
<tr class="even">
<td>4.05</td>
<td>INSTITUTION ASSOCIATION TYPES</td>
<td><strong>^DIC(4.05,</strong></td>
<td>This file links entries in the INSTITUTION (#4) file into associations that are meaningful.</td>
<td>YES</td>
<td>Merge</td>
</tr>
<tr class="odd">
<td>4.1</td>
<td>FACILITY TYPE</td>
<td><strong>^DIC(4.1,</strong></td>
<td>This file is pointed to by the Institution file. It contains a list of facility codes that were previously stored in the VA Type Code field of the Institution file. This file is distributed with data, and the new data should overwrite the old. It is cross-referenced by name and full name.</td>
<td>YES</td>
<td>Merge</td>
</tr>
<tr class="even">
<td>4.11</td>
<td>AGENCY</td>
<td><strong>^DIC(4.11,</strong></td>
<td>This file replaces the <strong>SET OF CODES</strong> field AGENCY that had been used in the INSTITUTION (#4) file.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="odd">
<td>5</td>
<td>STATE</td>
<td><strong>^DIC(5,</strong></td>
<td><p>This file contains the name of the state (or outlying area) as issued by the Department of Veterans Affairs (VA) and issued in M-1, Part I, Appendix B.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/046.png) CAUTION: These entries should remain as distributed and should not be edited or updated unless done through a software upgrade or under direction of VA Central Office.</p></td>
<td>YES</td>
<td></td>
</tr>
<tr class="even">
<td>5.12</td>
<td>POSTAL CODE</td>
<td><strong>^XIP(5.12</strong></td>
<td><p>This file stores all known Postal Codes as well as other associated information related to the Postal Code. Although the original data in this file only contains US Postal Codes, the file has been designed to allow non-US Postal Codes to be added in the future if desired.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/047.png) CAUTION: Do <em>not</em> point directly to this file until you get an Integration Control Registration (ICR).</p></td>
<td>YES</td>
<td>Replace</td>
</tr>
<tr class="odd">
<td>5.13</td>
<td>COUNTY CODE</td>
<td><strong>^XIP(5.13,</strong></td>
<td><p>This file contains all known US County Federal Information Processing Standards (FIPS) codes according to the United States Geological Survey (USGS), Department of Housing and Urban Development (HUD), and the United States Postal Service (USPS).</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/048.png) CAUTION: Do <em>not</em> point directly to this file until you get an ICR. The <em>only</em> file that is allowed to point directly to this file is the POSTAL CODE (#5.12) file.</p></td>
<td>YES</td>
<td>Replace</td>
</tr>
<tr class="even">
<td>7</td>
<td>PROVIDER CLASS</td>
<td><strong>^DIC(7,</strong></td>
<td>This file stores the provider classes. It is pointed to by the PROVIDER CLASS (#53.5) field of the NEW PERSON (#200) file.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7.1</td>
<td>SPECIALITY</td>
<td><strong>^DIC(7.1,</strong></td>
<td>This file stores the specialties. It is pointed to by the SPECIALTY (#442121.04) sub-field of the of the CONSULTANT’S LICENSES (#442121) file.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9.2</td>
<td>HELP FRAME</td>
<td><strong>^DIC(9.2,</strong></td>
<td>This file contains the text of help frames created through the Help Processor (<strong>XQH</strong>). Help frames can be associated with options or with data dictionary fields to provide online instruction. The file is cross-referenced by name, header, date entered, author, and editor.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>9.4</td>
<td>PACKAGE</td>
<td><strong>^DIC(9.4,</strong></td>
<td>The top level of a PACKAGE (#9.4) file entry for software now stores static software information. The PACKAGE (#9.4) file stores mainly static software information that is <em>not</em> version-specific, as well as the patch history of the software. KIDS updates the VERSION (Multiple) field. Patch installations update the PATCH APPLICATION HISTORY (Multiple) field, which is within the VERSION (Multiple) field. Most other fields have been designated for removal at the top level of the PACKAGE (#9.4) file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>9.6</td>
<td>BUILD</td>
<td><strong>^XPD(9.6,</strong></td>
<td>This file identifies the elements of a software application that will be transported by the Kernel Installation &amp; Distribution System (KIDS). All components of the software (that is templates, options, security keys, and so on) <em>must</em> be listed in this file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>9.7</td>
<td>INSTALL</td>
<td><strong>^XPD(9.7,</strong></td>
<td>This file contains the installation information for a site from the Kernel Installation &amp; Distribution System (KIDS). This file should <em>not</em> be edited. All information is updated when new software is installed at a site.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>9.8</td>
<td>ROUTINE</td>
<td><strong>^DIC(9.8,</strong></td>
<td>This file documents system routines. Parameters and entry points can be described. When running <strong>%INDEX</strong>, some fields will be given values as the <strong>%INDEX</strong> verification tool locates variables, globals, and routine references. When using the <strong>%Z</strong> editor, the EDIT HISTORY (Multiple) field will be filled in with date, device, user, and UCI. The <strong>%ZOSF(“TEST”)</strong> node can be executed, checking <strong>$T</strong>, to determine whether a routine listed in this file exists in the current account. This file is cross-referenced by name.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>10</td>
<td>RACE</td>
<td><strong>^DIC(10,</strong></td>
<td>This file contains the list of valid races. The allowable entries are maintained by VA Central Office and, as such, alteration and/or addition of entries is <em>not</em> allowed.</td>
<td>YES</td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>MARITAL STATUS</td>
<td><strong>^DIC(11,</strong></td>
<td>This file currently consists of six entries that are distributed by the MAS development team. Alteration of any of the six entries or addition of entries to this file that are <em>not</em> distributed by the MAS developers may have a negative impact on the performance of the MAS module as well as other modules.</td>
<td>YES</td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>RELIGION</td>
<td><strong>^DIC(13,</strong></td>
<td>This file currently contains <strong>84</strong> entries. These entries are determined by VACO MAS. This file should <em>not</em> be added to nor should entries in it be altered or deleted by the facility. Entry, edit, or deletion of these entries could have severe negative effects on the performance of the MAS module.</td>
<td>YES</td>
<td></td>
</tr>
<tr class="even">
<td>14.4</td>
<td>TASKS</td>
<td><strong>^%ZTSK(</strong></td>
<td>This file describes TaskMan‘s main file of jobs to start. Because TaskMan works on this file from many UCIs, it does <em>not</em> use VA FileMan to manipulate it. There are no cross-references on this file and there are no fields that can be edited; use TaskMan options for that. The file can be searched, sorted and printed. The third piece of the <strong>Zero</strong> node is only updated when the <strong>Queuable Task Log Cleanup</strong> [XUTM QCLEAN] option runs. Some applications still do their own setting into this global and wipe out the <strong>Zero</strong> node. The storage of the symbol table is <em>not</em> in a VA FileMan-compatible format.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>14.5</td>
<td>VOLUME SET</td>
<td><strong>^%ZIS(14.5</strong></td>
<td>This file describes the volume sets available in the current multiprocessor network. The information pertaining to each volume set is used primarily by Kernel, especially TaskMan. The UCIs that make up each volume set can be determined by using the cross-reference in the UCI Association Table file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>14.6</td>
<td>UCI ASSOCIATION</td>
<td><strong>^%ZIS(14.6,</strong></td>
<td>This file contains information that indicates which UCIs on different volume sets are equivalent. This information allows the running of tasks that need a device only available on a different volume set, even if the UCI on the other volume set has another name.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>14.7</td>
<td>TASKMAN SITE PARAMETERS</td>
<td><strong>^%ZIS(14.7,</strong></td>
<td>This file should be used by the system manager to tune TaskMan to the site’s specific needs. Entries are identified by the CPU and volume set, so that parameters can be set differently for different nodes that share a single volume set, and so on. Changes to any of the fields automatically causes all accessible Task Managers on the system to update their local copies of the parameters.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>14.72</td>
<td>TASKMAN SNAPSHOT</td>
<td><strong>^%ZIS(14.72,</strong></td>
<td>This file holds TaskMan Snapshot data. This is a snapshot of the counts in the TaskMan <strong>^%ZTSCH</strong> global. There should be no user entry of this data. It is just for reporting.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>14.8</td>
<td>TASK SYNC FLAG</td>
<td><strong>^%ZISL(14.8,</strong></td>
<td>This file holds the task synchronization flags that control whether a task can run or <em>must</em> wait.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>15<br />
(Toolkit)</td>
<td>DUPLICATE RECORD</td>
<td><strong>^VA(15,</strong></td>
<td>This file is designed to analyze and resolve duplicate record problems from various data files (such as PATIENT [#2] file). The “from” and “to” records are identified, the match status is reported, and the user initiating the process is noted. This file is cross-referenced by Status and From-record.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>15.1<br />
(Toolkit)</td>
<td>DUPLICATE RESOLUTION</td>
<td><strong>^VA(15.1,</strong></td>
<td>This file facilitates duplicate checking and merging of files that have entries in the DUPLICATE RECORD (#15) file. It provides the overall control information that software developers need to identify duplicates within their files and then to merge the duplicate entries.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>15.2<br />
(Toolkit)</td>
<td>XDR MERGE PROCESS</td>
<td><strong>^VA(15.2,</strong></td>
<td>When a merge process is set up, all its information is stored in this file. Once a merge process has completed, that entry can be purged using the <strong>Purge Merge Process File</strong> [XDR PURGE2] option in the Managers menu.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>15.3<br />
(Toolkit)</td>
<td>XDR REPOINTED ENTRY</td>
<td><strong>^VA(15.3,</strong></td>
<td>This file records the entry number of the <strong>FROM</strong> record that is merged into the <strong>TO</strong> record. This can be used for VA FileMan to determine which entries were merged, so the IEN of the FROM record will <em>not</em> be reused.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>15.4<br />
(Toolkit)</td>
<td>MERGE IMAGES</td>
<td><strong>^XDRM(</strong></td>
<td>This file stores an image of the pairs of entries in files that were merged immediately prior to the actual merge. In addition, there is also a record of the locations of <strong>POINTER</strong> values that were changed during the merge process.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>OPTION</td>
<td><strong>^DIC(19,</strong></td>
<td>Information in this file drives the menu system. Options are created, associated with others on menus, locked, set out-of-order, assigned prohibited times or devices, or given entry/exit actions. The <strong>Edit Options</strong> [XUEDITOPT] option of the <strong>Menu Management</strong> [XUMAINT] menu should be used (instead of VA FileMan), so that the global root (<strong>DIC</strong>) and other such fields are given the correct values. Options can be tailored by setting VA FileMan variables using this file. The Order Enter/Results Reporting (OE/RR) software is accessed by using the appropriate option type. It is cross-referenced by name, menu text, uppercase menu text, type, item, synonym, help frame, out-of-order message, lock, prohibited times, restricted devices, and priority.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>19.081</td>
<td>AUDIT LOG FOR OPTIONS</td>
<td><strong>^XUSEC(19,</strong></td>
<td>The KERNEL SYSTEM PARAMETERS (#8989.3) file establishes when and how a log of option usage will be recorded in this file. For the indicated time-period, all specified options, namespaces, and users will be audited. It is recommended that when audits are run, the number of audited entities be minimized so that disk space is <em>not</em> inadvertently wasted. This file is cross-referenced by option.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>19.1</td>
<td>SECURITY KEY</td>
<td><strong>^DIC(19.1,</strong></td>
<td>This file holds the names of security keys that are used to lock options. To lock an option, the name of the key is entered in the Lock field of the OPTION (#19) file. To permit a user to unlock the option, the user’s name is entered in the Holder field of this file. It is cross-referenced by name and holder.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>19.2</td>
<td>OPTION SCHEDULING</td>
<td><strong>^DIC(19.2,</strong></td>
<td>This file holds records that relate to the scheduling of options to run on a schedule or occasionally on a one-time basis. There is one record for each time that an option is scheduled. This allows one option to be scheduled to run on more than one CPU or at more than one time without having to duplicate the option in the OPTION (#19) file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>19.8</td>
<td>MENUMAN QUICK HELP</td>
<td><strong>^DIC(19.8,</strong></td>
<td>This file holds help text to be displayed in the ScreenMan edit form for the menu file. It only changes when there are changes to the Menu system.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="even">
<td>20</td>
<td>NAME COMPONENTS</td>
<td><strong>^VA(20,</strong></td>
<td><p>This file, introduced with Name Standardization (Patch XU*8.0*134), stores the component parts of a person’s name in the following fields:</p>
<ul>
<li><p>FAMILY (LAST) NAME (#1)</p></li>
<li><p>GIVEN (FIRST) NAME (#2)</p></li>
<li><p>MIDDLE NAME (#3)</p></li>
<li><p>PREFIX (#4)</p></li>
<li><p>SUFFIX (#5)</p></li>
<li><p>DEGREE (#6)</p></li>
</ul>
<p>The “source name” that has these components is identified by the following three fields:</p>
<ul>
<li><p>FILE (#.01)</p></li>
<li><p>FIELD (#.02)</p></li>
<li><p>IENS (#.03)</p></li>
</ul>
<p>The “<strong>ANAME</strong>” cross-reference on the FAMILY (LAST) NAME, GIVEN (FIRST) NAME, MIDDLE NAME, and SUFFIX fields keep each component in synchronization with the corresponding source name. In the case of Patch XU*8.0*134, the source name is the NAME (#.01) field of the NEW PERSON (#200) file.</p>
<p>The DEGREE and PREFIX fields are <em>not</em> considered part of a standard name but can be used to build formatted names for display.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>40.5</td>
<td>HOLIDAY</td>
<td><strong>^HOLIDAY(</strong></td>
<td>This file records institutional holidays. It is referenced by the <strong>XUWORKDY</strong> routine and is <em>not</em> distributed with data. It is cross-referenced by date.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>46.11</td>
<td>RAI MDS MONITOR</td>
<td><strong>^DGRU(46.11,</strong></td>
<td><p>This file stores the modified and original contents of the <strong>#.01</strong> field of the Master file entry and file reference information.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/049.png) <strong>NOTE:</strong> RAI/MDS = Resident Assessment Instrument/Minimum Data Set.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>49</td>
<td>SERVICE/<br />
SECTION</td>
<td><strong>^DIC(49,</strong></td>
<td>This file is a list of the services and sections within the services. Some of the entries may be “MIS COSTING SECTIONS” for use with the cost accounting part of the Management Information System software. A section is an MIS section if there is a code entered in the field called MIS COSTING CODE. In the cost accounting system, all medical center costs are tied to a particular section. When MIS sections change, do <em>not</em> delete the old section. Instead, change the fields under the multiple field called “DATE CLOSED” to identify which sections are no longer in use.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>101</td>
<td>PROTOCOL</td>
<td><strong>^ORD(101,</strong></td>
<td>This file contains the orderables and methods for accomplishing orders (protocols) within Order Entry/Results Reporting (OE/RR).</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>200</td>
<td><span id="NEW_PERSON_File" class="anchor"></span>NEW PERSON</td>
<td><strong>^VA(200,</strong></td>
<td><p>This file contains data on employees, users, practitioners, and so on, that was previously stored in the User, Person, Provider, and other files. VistA software developers <em>must</em> check with the Kernel developers to see that a given number/namespace is available for use.</p>
<p>Kernel Patch XU*8.0*799 added the <strong>AVIAM</strong> new style record cross-reference (x-ref) to various fields in the NEW PERSON (#200) file. The <strong>AVIAM</strong> cross-reference allows the Master Veteran Index (MVI) to capture changes on the following fields in the NEW PERSON (#200) file, which will add/update entries in the NEW PERSON FIELD MONITOR (#8933.1) file to identify those NEW PERSON (#200) fields that have been changed for the user that day and need to be transmitted/broadcasted out to Person Service Identity Management (PSIM):</p>
<ul>
<li><p>NAME (#.01)</p></li>
<li><p>EMAIL ADDRESS (#.151)</p></li>
<li><p>SEX (#4)</p></li>
<li><p>DOB (#5)</p></li>
<li><p>DISUSER (#7)</p></li>
<li><p>SSN (#9)</p></li>
<li><p>TERMINATION DATE (#9.2)</p></li>
<li><p>NPI (#41.99)</p></li>
<li><p>PRIMARY MENU OPTION (#201)</p></li>
<li><p>LAST SIGN-ON DATE/TIME (#202)</p></li>
<li><p>SECID (#205.1)</p></li>
<li><p>SUBJECT ORGANIZATION (#205.2)</p></li>
<li><p>SUBJECT ORGANIZATION ID (#205.3)</p></li>
<li><p>UNIQUE USER ID (#205.4)</p></li>
<li><p>ADUPN (#205.5)</p></li>
</ul>
<p>NETWORK USERNAME (#501.1)</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>201</td>
<td>USER CLASS</td>
<td><strong>^VA(201,</strong></td>
<td>This file is used for identifying the kinds of all other entries in the NEW PERSON (#200) file that are <em>not</em> providers identified with PERSON CLASS.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="odd">
<td><span id="File_8932_1" class="anchor"></span>8932.1</td>
<td>PERSON CLASS</td>
<td><strong>^USC(8932.1,</strong></td>
<td><p>This file stores the Centers for Medicare &amp; Medicaid Services (CMS) Health Care Financing Administration (HCFA) provider type data.</p>
<p>In 2001, ANSI ASC X12N asked the National Uniform Claim Committee (NUCC) to become the official maintainer of the Health Care Provider Taxonomy List (provider type).</p>
<p>PERSON CLASS is to be used for identifying provider types for roll-ups.</p>
<p>Patches need to review the technical description in the INDIVIDUAL/NON (#90002) field. This field is in the Indian Health Service (HIS) numberspace and is for their use pending development and deployment of a file to support a Non-Individual taxonomy.</p>
<p>PERSON CLASS is intended for Individuals. As of August 30, 2002, IHS has added entries for non-Individuals to the file. Patches should take that into account when planning how to load new data.</p>
<p>Per VHA Directive 2005-044, this file has been “locked down” by Data Standardization (DS). The file definition (that is data dictionary) <em>shall not</em> be modified. All additions, changes and deletions to entries in the file <em>shall</em> be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).</p></td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="even">
<td>8932.2</td>
<td>PROGRAM OF STUDY</td>
<td><strong>^USC(8932.2,</strong></td>
<td>This file stores the names and information of programs of study.</td>
<td>YES</td>
<td>Replace</td>
</tr>
<tr class="odd">
<td>8933.1</td>
<td><span id="NEW_PERSON_FIELD_MONITOR_File" class="anchor"></span>NEW PERSON FIELD MONITOR</td>
<td><strong>^XTV(8933.1</strong></td>
<td>This file serves as a container to track the changes to NEW PERSON (#200) fields that need to be broadcast out to the Person Service Identity Management (PSIM) system via Web Services.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8980<br />
(Toolkit)</td>
<td>KERMIT HOLDING</td>
<td><strong>^DIZ(8980,</strong></td>
<td><p>This file provides storage for data being transferred by the KERMIT protocol. By default, the data can only be accessed by the user that created it.</p>
<p>The <strong>Kermit Menu</strong> [XT-KERMIT] can be used to send and receive data with this file. The menu also allows the creator of the data to permit access by others.</p>
<p>This file is cross-referenced by Name, Creator, and Access Allowed to a user.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8980.2</td>
<td>PKI Digital Signatures</td>
<td><strong>^XUSSPKI(8980.2,</strong></td>
<td>This file stores the Public Key Infrastructure (PKI) digital signatures.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8980.22</td>
<td>PKI CRL URLS</td>
<td><strong>^XUSSPKI(8980.22,</strong></td>
<td>This file stores the Universal Resource Locator’s (URL) for the Certificate Revocation List’s (CRL) from the Certificate Distribution Points (CDP) in the users Public Key Infrastructure (PKI) Certificate. These URL’s are sent up to a Windows server to keep a database of Certificate Revocation’s up to date.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8984.1<br />
(Toolkit)</td>
<td>LOCAL KEYWORD</td>
<td><strong>^XT(8984.1,</strong></td>
<td><p>The lookup entry (or code) can be associated with multiple key words or key phrases. The entry is displayed if the user enters all or any part of a key phrase.</p>
<p>Lookups are performed in the following order:</p>
<ol type="1">
<li><p>SHORTCUT—Stops here if a match is found.</p></li>
<li><p>SYNONYM.</p></li>
<li><p>KEYWORD.</p></li>
</ol></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8984.2<br />
(Toolkit)</td>
<td>LOCAL SHORTCUT</td>
<td><strong>^XT(8984.2,</strong></td>
<td>This is a word or phrase that will be used <em>exclusively</em> to find an entry. During a lookup, this file is checked first. If a shortcut matches the user’s entry, the corresponding entry is displayed, and no other lookups will be performed.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8984.3<br />
(Toolkit)</td>
<td>LOCAL SYNONYM</td>
<td><strong>^XT(8984.3,</strong></td>
<td><p>Synonyms are single terms that can be associated with one or more TERMS in the lookup file (tokens in the MTLU cross-reference). For example, “CANCER” can be associated with each of the specific forms of cancer that might be found.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/050.png) <strong>NOTE:</strong> If the user enters a phrase, all terms in the phrase <em>must</em> be true to get a match; therefore, “LUNG CANCER” might significantly restrict the search.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8984.4<br />
(Toolkit)</td>
<td>LOCAL LOOKUP</td>
<td><strong>^XT(8984.4,</strong></td>
<td>This file defines other files that have been configured for Multi-term lookups, along with the name of the file’s MTLU cross-reference.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8989.2</td>
<td>KERNEL PARAMETERS</td>
<td><strong>^XTV(8989.2,</strong></td>
<td>This file holds parameters that Kernel uses, and the site is allowed to change. For example, the Computer Account Letter. Kernel loads its standard name into the file and if the site builds a new letter, then they can enter a replacement name that will be used in place of the standard one.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8989.3</td>
<td>KERNEL SYSTEM PARAMETERS</td>
<td><strong>^XTV(8989.3,</strong></td>
<td>This file holds the site parameters for this installation of Kernel. It has only one entry, the domain name of the installation site. Some parameters are defined by the systems manager during the installation process. These include Agency, Volume Set Multiple, Default parameters. Others can be edited after installation. Spooling and Audit parameters can be established. Priorities can be set for interactive users and for TaskMan. Defaults for fields (such as timed read, auto-menu, and ask device) are defined for use when <em>not</em> otherwise specified for a user or device.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8989.51</td>
<td>PARAMETER DEFINITION</td>
<td><strong>^XTV(8989.51,</strong></td>
<td>This file contains the characteristics of parameters. Entries in this file <em>must</em> be namespaced.</td>
<td>YES</td>
<td>Replace</td>
</tr>
<tr class="even">
<td>8991<br />
(Toolkit)</td>
<td>XTV ROUTINE CHANGES</td>
<td><strong>^XTV(8991,</strong></td>
<td><p>This file records the most current version of a routine, and information about changes that have occurred in that routine in prior versions. Routines are checked for any changes by using the <strong>Update with current routines</strong> [XTVR UPDATE] option, which enters any changes noted and updates the most current version. There is no need for manual entry into this file.</p>
<p>Use the <strong>Routine Compare - Current with Previous</strong> [XTVR COMPARE] option to obtain listings of the changes recorded for the routines from the most recent to earlier changes.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8991.19<br />
(Toolkit)</td>
<td>XTV VERIFICATION PACKAGE</td>
<td><strong>^XTV(8991.19,</strong></td>
<td>This file indicates the file numbers for the main files and namespaces for options, keys, and so on, which are to be included as a part of a package undergoing verification. This file determines the files and other entries to be included by the routines that are used in preparing and comparing the XTV GLOBAL CHANGES file.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8991.2<br />
(Toolkit)</td>
<td>XTV GLOBAL CHANGES</td>
<td><strong>^XTV(8991.2,</strong></td>
<td>This file records the state of a given verification package in terms of DD entries, options, keys, templates, and so on for comparison with a subsequent version of the package.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8991.5</td>
<td>XQAB ERRORS LOGGED</td>
<td><strong>^XTV(8991.5,</strong></td>
<td>This file maintains a log of errors occurring at alpha/beta test sites.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8991.6</td>
<td>XUEPCS DATA</td>
<td><strong>^XTV(8991.6,</strong></td>
<td>This file is used for the DEA ePCS project (Kernel Patch XU*8.0*580). It stores audit data for ePCS-related fields that have been modified.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8991.7</td>
<td>XUEPCS PSDRPH AUDIT</td>
<td><strong>^XTV(8991.7,</strong></td>
<td>This file is used for the DEA ePCS project (Kernel Patch XU*8.0*580). It stores audit data when a user is allocated or de-allocated the <strong>PSDRPH</strong> security key.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8991.8</td>
<td>DEA BUSINESS ACTIVITY CODES</td>
<td><strong>^XTV(8991.8,</strong></td>
<td>This file is associated with the DEA numbers and provider information in the DEA NUMBERS (#8991.9) file. This file links a provider with the type of service provided. It contains BUSINESS ACTIVITY CODES that are supplied by the DOJ/DEA web service.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="odd">
<td>8991.9</td>
<td>DEA NUMBERS</td>
<td><strong>^XTV(8991.9,</strong></td>
<td>This file is designed to contain demographic and permission information about a provider related to the ability to order controlled substance prescriptions.</td>
<td>NO</td>
<td></td>
</tr>
<tr class="even">
<td>8992</td>
<td>ALERT</td>
<td><strong>^XTV(8992,</strong></td>
<td><p>This file keeps track of alerts pending processing for each user. The main entry for each record is a <strong>POINTER</strong> to the NEW PERSON (#200) file. A Multiple field under each user records the:</p>
<ul>
<li><p>Date and time an alert was generated.</p></li>
<li><p>Unique ID associated with the alert.</p></li>
<li><p>Text for display.</p></li>
<li><p>(Optional) Routine entry point or option for use in processing the alert.</p></li>
<li><p>(Optional) Data string associated with the alert.</p></li>
</ul></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8992.1</td>
<td>ALERT TRACKING</td>
<td><strong>^XTV(8992.1,</strong></td>
<td><p>This file tracks the content and interactions with an alert. Every alert that is generated is initially filed within this file. Each entry has the date and time the alert was generated, which user generated the alert, whether the alert was generated in a background task, what action was to be taken, if any (the entry point or option name to be used), and the data string, if any, for use with the alert. There is a multiple field which also identifies each user that the alert was sent to, when the user initially saw the displayed text, when the alert was selected for processing, when the processing was completed, and when the alert was deleted after processing or associated with another user’s processing, or when the alert was deleted by a cleanup operation.</p>
<p>Unless a longer lifetime is specified for the specific alert, it is deleted from the file after <strong>30 days</strong>. If a longer lifetime is specified, it will <em>not</em> be deleted until after that period passes.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8992.2</td>
<td>ALERT RECIPIENT TYPE</td>
<td><strong>^XTV(8992.2,</strong></td>
<td>This file was added with Kernel Patch XU*8.0*285. This file was added to contain indicators as to why an alert was sent.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8992.3</td>
<td>ALERT CRITICAL TEXT</td>
<td><strong>^XTV(8992.3,</strong></td>
<td><p>This file makes it easier for packages or sites to specify text that should be used to indicate an alert to be marked as <strong>Critical</strong>. It contains those text strings that are identified as indicating a <strong>Critical</strong>-type alert. This checking is <em>not</em> case sensitive, and if the identified string is immediately preceded by either of the following words, it will <em>not</em> be indicated as a <strong>Critical</strong>-type alert:</p>
<ul>
<li><p><strong>NOT</strong></p></li>
<li><p><strong>NON<br />
</strong></p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/051.png) <strong>NOTE:</strong> This file was added with Kernel Patch XU*8.0*513.</p>
<p>Using this file means that the package or site can add desired text for identification as <strong>Critical</strong>-type by using Integration Control Registration (ICR) #6869, ALERT CRITICAL TEXT LOOKUP AND EDIT. This is a “Controlled Subscription” type ICR that allows application development teams to release patches that update the ALERT CRITICAL TEXT (#8992.3) file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/052.png) CAUTION: Application development teams making changes to the ALERT CRITICAL TEXT (#8992.3) file are responsible for confirming the change does <em>not</em> affect Kernel’s reporting of Critical-type alerts.<br />
<br />
Adding an entry with Critical-type text to the ALERT CRITICAL TEXT (#8992.3) file reports any alert containing that text as Critical. Careful analysis is necessary to confirm changes do <em>not</em> cause malfunction of any VistA alerts. When creating a new entry in the ALERT CRITICAL TEXT (#8992.3) file, it is <em>recommended</em> the associated application be indicated in the CREATING PACKAGE (#.03) field. Thus, any inquiries regarding the Critical alert text can be directed to the appropriate development team. Also, the description included in the PACKAGE-ID (#.02) field in the ALERT CRITICAL TEXT (#8992.3) file should be reviewed to determine if it <em>must</em> be defined. That field's description indicates that data in this field can further screen alerts from being reported as critical. Its use should be understood when adding entries to the ALERT CRITICAL TEXT (#8992.3) file.</p></td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="even">
<td>8993</td>
<td>XULM LOCK DICTIONARY</td>
<td><strong>^XLM(8993,</strong></td>
<td>This file contains descriptions and specifications for locks held by various applications. The Lock Manager uses it to provide information and guidance to the user about locks found in the lock table.</td>
<td>YES</td>
<td>Over-write</td>
</tr>
<tr class="odd">
<td>8993.1</td>
<td>XULM LOCK MANAGER PARAMETERS</td>
<td><strong>^XLM(8993.1,</strong></td>
<td>This is the parameter file for the Kernel Lock Manager. It should contain only one entry.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8993.2</td>
<td>XULM LOCK MANAGER LOG</td>
<td><strong>^XLM(8993.2,</strong></td>
<td>This file records each instance of the Kernel Lock Manager being used to terminate a process and the locks that the process held.</td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>8994</td>
<td>REMOTE PROCEDURE</td>
<td><strong>^XWB(8994,</strong></td>
<td><p>This file is owned by RPC Broker. This file is used as a repository of server-based procedures in the context of the Client/Server architecture. By using the Remote Procedure Call (RPC) Broker, applications running on client workstations can invoke (call) the procedures in this file to be executed by the server and the results are returned to the client application.</p>
<p>Each remote procedure entry is associated with an entry point (ROUTINE with optional TAG). Calls to these procedures can include parameters of different value types. The resulting value of the call can be either a string, a list of strings, or a word-processing string as indicated by the RETURN VALUE TYPE (.04) field.</p>
<p>The remote procedure may be available for use by anyone, or its use may be restricted to one or more applications. The range of availability is indicated by the AVAILABILITY field.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/053.png) <strong>NOTE:</strong> If there is no entry in the AVAILABILITY field, then the procedure is assumed to be PUBLIC.</p>
<p>A remote procedure can be removed from service for a time-period by setting the INACTIVE field. A request for use of a procedure, which is marked inactive, will result in an error being returned to the originating application.</p></td>
<td>NO</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8994.5</td>
<td>REMOTE APPLICATION</td>
<td><strong>^XWB(8994.5,</strong></td>
<td><p>This file is owned by RPC Broker and used by Kernel security to identify remote applications. Kernel uses this file to identify external applications in the SIGN-ON LOG (#3.081) file and for assigning a role-based user context to authenticated applications.</p>
<p>The REMOTE APPLICATION file was introduced as part of the Broker Security Enhancement (BSE) to secure access through the remote user or visitor approach by GUI applications (formerly known as the CAPRI approach for the first application to use this access style). The remote visitor access permits applications where users need to access many sites to do so without requiring a separate Access Code and Verify Code at each site.</p>
<p>Following the Broker Security Enhancement, applications can use the remote visitor access only if they have an entry in this file with a one-way hash of a secure phrase. Identification of an entry in the file is based on the application passing in the original phrase, which is then hashed and used for a cross-reference lookup. The application <em>must</em> have at least one entry in the CALLBACKTYPE sub-file indicating:</p>
<ul>
<li><p>A connection type.</p></li>
<li><p>A valid address for the authenticating server.</p></li>
<li><p>A connection port number.</p></li>
</ul>
<p>This information is necessary for the remote server to directly connect the authenticating server to obtain the demographic information necessary to create or match the visitor entry in the NEW PERSON (#200) file. The application also specifies the desired context option for the user, and this is given to the remote visitor instead of the application having to figure out how to set this value.</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref87258807" class="anchor"></span>Table 16: Files—Kernel Virgin Installation Files

### Additional Files Installed During Virgin Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Virgin Installation brings in the additional files listed in <u>Table 16</u>:

| File \# | File Name      | Global Location | Description                                                                                                                                                                                                                                                                                                          | Data w/ File | Data Setting |
|---------|----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
| 3.8     | MAIL GROUP     | ^XMB(3.8,   | (Exported with MailMan) This file holds the names of all groups and their members known to MailMan.                                                                                                                                                                                                                  | NO           | N/A          |
| 4.2     | DOMAIN         | ^DIC(4.2,   | (Exported with MailMan) This file names all nodes to which MailMan messages can be routed. Each name in this file corresponds to the right side of a MailMan address, the part following the @ symbol.                                                                                                           | NO           | N/A          |
| 5       | STATE          | ^DIC(5,     | This file contains a list of state names and abbreviations.                                                                                                                                                                                                                                                          | YES          | Overwrite    |
| 7       | PROVIDER CLASS | ^DIC(7,     | This file identifies various classifications or types of providers.                                                                                                                                                                                                                                                  | NO           | N/A          |
| 7.1     | SPECIALITY     | ^DIC(7.1,   | This file identifies locally added specialties and their associated services.                                                                                                                                                                                                                                        | NO           | N/A          |
| 10      | RACE           | ^DIC(10,    | This file currently consists of seven entries. The allowable entries are established by VACO MAS. Entries in this file should *not* be altered or added to. To do so may have a negative impact on the performance of the MAS module as well as other modules.                                                       | YES          | Overwrite    |
| 11      | MARITAL STATUS | ^DIC(11,    | This file currently consists of six entries, which are distributed by the MAS development team. Alteration of any of the six entries or addition of entries to this file which are *not* distributed by the MAS developers may have a negative impact on the performance of the MAS module as well as other modules. | YES          | Overwrite    |
| 13      | RELIGION       | ^DIC(13,    | This file currently contains 30 entries. These entries are determined by VACO MAS. This file should *not* be added to nor should entries in it be altered or deleted by the facility. Entry, edit, or deletion of these entries could have severe negative effects on the performance of the MAS module.         | YES          | Overwrite    |

<span id="_Ref378686662" class="anchor"></span>Table 17: Field List—PERSON CLASS (#8932.1) File (Kernel Patch XU\*8.0\*27)

## Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PERSON CLASS (#8932.1) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PERSON CLASS (#8932.1) file contains the Health Care Financing Administration (HCFA) taxonomy that reflects provider type. It contains the fields in <u>Table 17</u>:

<table>
<caption><p><span id="_Ref87256657" class="anchor"></span>Table 18: Field List—Assigning Person Class to Providers Software (that is Kernel Patches XU*8.0*27, 377, and 531)</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Field #</th>
<th>Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.001</td>
<td>NUMBER</td>
<td>This is a number field to allow adding new entries by number.</td>
</tr>
<tr class="even">
<td>.01</td>
<td>PROVIDER TYPE</td>
<td><p>This is Level I of the National Uniform Claim Committee (NUCC) structure of the Provider Taxonomy.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/054.png) <strong>REF:</strong> For more information on the NUCC, please visit the NUCC website located at the following Web address: <a href="https://www.nucc.org/">NUCC Website</a></p></td>
</tr>
<tr class="odd">
<td>.011</td>
<td>PROVIDER TYPE CODE</td>
<td>This is Level I, Provider Type—<strong>2</strong>-byte alphanumeric, consisting of the <strong>1<sup>st</sup></strong> and <strong>2<sup>nd</sup></strong> characters of <strong>X12 CODE</strong>, which is a code that identifies a major grouping of services or occupations of health care providers.</td>
</tr>
<tr class="even">
<td>1</td>
<td>CLASSIFICATION</td>
<td>This is the <strong>CMS (X12)</strong> Classification (Level <strong>II</strong>). Values <em>must</em> be from <strong>3</strong> to <strong>65</strong> characters in length.</td>
</tr>
<tr class="odd">
<td>1.1</td>
<td>CLASSIFICATION CODE</td>
<td>This is Level II, Classification Code—<strong>2</strong>-byte alphanumeric consisting of the <strong>3<sup>rd</sup></strong> and <strong>4<sup>th</sup></strong> characters of the <strong>X12 CODE</strong>, which is a code that identifies more specific services or occupations within the health care provider type. The coding is based on licensed provider classifications.</td>
</tr>
<tr class="even">
<td>2</td>
<td>AREA OF SPECIALIZATION</td>
<td>This is Level III in NUCC’s structure of the Provider Taxonomy. It is the most specific but sometimes defines a “sub-category” of Classification. Values <em>must</em> be from <strong>2</strong> to <strong>75</strong> characters in length.</td>
</tr>
<tr class="odd">
<td>2.1</td>
<td>AREA OF SPECIALIZATION CODE</td>
<td><p>This is Level III, Area of Specialization—<strong>5</strong>-byte alphanumeric consisting of the <strong>5<sup>th</sup></strong> through <strong>9<sup>th</sup></strong> characters of the <strong>X12 CODE</strong>, which is a code that identifies:</p>
<ul>
<li><p>Provider’s specialization.</p></li>
<li><p>Segment of the population that a health care provider chooses to service.</p></li>
<li><p>Specific medical service.</p></li>
<li><p>Specialization in treating a specific disease.</p></li>
<li><p>Any other descriptive characteristic about the providers practice relating to the services rendered.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>3</td>
<td>STATUS</td>
<td><p>This field allows old entries to be disabled <em>without</em> removing them from the table. Valid values are:</p>
<ul>
<li><p><strong>a—</strong>Active</p></li>
<li><p><strong>i—</strong>Inactive</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>4</td>
<td>DATE INACTIVATED</td>
<td>This field holds the date that a Provider Class was inactivated.</td>
</tr>
<tr class="even">
<td>5</td>
<td>VA CODE</td>
<td>This field holds the <strong>7</strong>-character VA assigned code for national rollup.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>X12 CODE</td>
<td><p>This is the code assigned by American National Standards Institute (ANSI) <strong>X12</strong>. <strong>X12</strong> published the joint <strong>X12N</strong> and Centers for Medicare &amp; Medicaid Service (CMS) Health Care Provider Taxonomy following the June 1997 <strong>X12</strong> meeting.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/055.png) <strong>NOTE:</strong> ANSI <strong>X12</strong> subcommittee <strong>N</strong> covers standards in the insurance industry, including health insurance; hence these are <strong>X12N</strong> standards.<br />
<br />
“X12N standards include transactions for claims/encounters, attachments, enrollment, disenrollment, eligibility, payment/remittance advice, premium payments, first report of injury, claim status, referral certification/authorization, and coordination of benefits.”<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/056.png) <strong>NOTE:</strong> A revised ANSI X12N 837 Professional Health Care Claim Companion Document was created in 2005.</p></td>
</tr>
<tr class="even">
<td>7</td>
<td>reserved</td>
<td>This field is only used with a conversion routine for updates to the file. Any data is only used by an update routine.</td>
</tr>
<tr class="odd">
<td>8</td>
<td>SPECIALTY CODE</td>
<td>This field holds the <strong>2</strong>-character specialty code associated with the classification.</td>
</tr>
<tr class="even">
<td>11</td>
<td>DEFINITION</td>
<td>Enter the definition of this Provider Type. Types with <strong>X12</strong> codes are defined by the National Uniform Claim Committee (NUCC), provided by various sources.</td>
</tr>
<tr class="odd">
<td>90002</td>
<td>INDIVIDUAL/NON</td>
<td><p>This field indicates whether the entry is for an Individual or for a Non-Individual. Valid values are:</p>
<ul>
<li><p><strong>I—</strong>Individual</p></li>
<li><p><strong>N—</strong>Non-Individual</p></li>
</ul>
<p>This field was added at the request of Indian Health Service (IHS) in their numberspace, until the file supporting Non-Individual taxonomies can be defined.</p>
<p>Currently, the <strong>X12 CODE</strong> definition does <em>not</em> explicitly indicate whether an entry is for an Individual or for a Non-Individual, either in value or structure definition.</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Excerpt taken from the "X12N" topic on the University of Miami; Miller School of Medicine website: <a href="http://privacy.med.miami.edu/glossary/xd_x12n.htm">Miller School of Medicine Glossary Website</a>, last modified May 11, 2005 (RC)<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Ref87256657" class="anchor"></span>Table 18: Field List—Assigning Person Class to Providers Software (that is Kernel Patches XU\*8.0\*27, 377, and 531)

The field in <u>Table 18</u> was exported with the Assigning Person Class to Providers software (that is Kernel Patch XU\*8.0\*27):

<table>
<caption><p><span id="_Ref324240367" class="anchor"></span>Table 19: Protocols—Extended-Action Options</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>File Number</th>
<th>File Name</th>
<th>Field Name and Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>200</td>
<td>NEW PERSON</td>
<td>PERSON CLASS (#.05) field</td>
<td><p>This is a Multiple field. It includes the following subfields:</p>
<ul>
<li><p>NUMBER (#.001).</p></li>
<li><p>PERSON CLASS (#.01)—<strong>POINTER</strong> to the PERSON CLASS (#8932.1) file.</p></li>
<li><p>EFFECTIVE DATE (#2)—The date the PERSON CLASS became effective.</p></li>
<li><p>EXPIRATION DATE (#3)—The date the PERSON CLASS is no longer valid.</p></li>
</ul>
<p>Kernel Patch XU*8.0*27 added the PERSON CLASS field to the following Kernel options:</p>
<ul>
<li><p><strong>Edit an Existing User</strong> [XUSEREDIT]</p></li>
<li><p><strong>Add a New User to the System</strong> [XUSERNEW]</p></li>
<li><p><strong>Reactivate a User</strong> [XUSERREACT]</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref324240367" class="anchor"></span>Table 19: Protocols—Extended-Action Options

### NEW PERSON File—Audit Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To support the enterprise provisioning of users and allow for monitoring of user profile changes, Kernel Patch XU\*8.0\*799 made Data Dictionary (DD) changes that enabled auditing for the following fields in the NEW PERSON (#200) file:

- EMAIL ADDRESS (#.151)
- NPI ENTRY STATUS (#41.98)
- NPI (#41.99)
- SECID (#205.1)
- SUBJECT ORGANIZATION (#205.2)
- SUBJECT ORGANIZATION ID (#205.3)
- UNIQUE USER ID (#205.4)
- ADUPN (#205.5)
- NETWORK USERNAME (#501.1)

To verify what fields are audited in the NEW PERSON (#200) file, do the following:

<span id="_Toc129437982" class="anchor"></span>Figure 6: Verifying Audited FieldsNEW PERSON (#200) File

\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT100

Select OPTION NAME: <span class="mark">XT-OPTION TEST \<Enter\></span> Test an option not in your menu

Test an option not in your menu

Option entry to test: <span class="mark">AUDIT MENU \<Enter\></span> DIAUDIT Audit Menu

<span class="mark">Fields Being Audited</span>

Monitor a User

Purge Data Audits

Purge DD Audits

Turn Data Audit On/Off

Show Past Changes To Data Dictionaries

Select Audit Menu \<TEST ACCOUNT\> Option: <span class="mark">FIELDS BEING AUDITED</span>

START WITH What File: NEW PERSON TREATING FACILITY LIST// <span class="mark">200 \<Enter\></span> NEW PERSON

(399 entries)

GO TO What File: NEW PERSON// <span class="mark">\<Enter\></span> (399 entries)

DEVICE: <span class="mark">0;80;99999 \<Enter\></span> UCX/TELNET

AUDITED FIELDS MAR 25, 2021@15:07 PAGE 1

FILE NUMBER LABEL TYPE AUDIT

--------------------------------------------------------------------------------

<span class="mark">200 .151 EMAIL ADDRESS FREE TEXT YES, ALWAYS</span>

200 9.2 TERMINATION DATE DATE/TIME YES, ALWAYS

200 11 VERIFY CODE FREE TEXT YES, ALWAYS

<span class="mark">200 41.98 NPI ENTRY STATUS SET YES, ALWAYS</span>

<span class="mark">200 41.99 NPI FREE TEXT YES, ALWAYS</span>

<span class="mark">200 205.1 SECID FREE TEXT YES, ALWAYS</span>

<span class="mark">200 205.2 SUBJECT ORGANIZATION FREE TEXT YES, ALWAYS</span>

<span class="mark">200 205.3 SUBJECT ORGANIZATION FREE TEXT YES, ALWAYS</span>

<span class="mark">200 205.4 UNIQUE USER ID FREE TEXT YES, ALWAYS</span>

<span class="mark">200 205.5 ADUPN FREE TEXT YES, ALWAYS</span>

<span class="mark">200 501.1 NETWORK USERNAME FREE TEXT YES, ALWAYS</span>

200 501.2 SUBJECT ALTERNATIVE FREE TEXT YES, ALWAYS

Fields Being Audited

Monitor a User

Purge Data Audits

Purge DD Audits

Turn Data Audit On/Off

Show Past Changes To Data Dictionaries

Select Audit Menu \<TEST ACCOUNT\> Option:

Auditing of the fields <span class="mark">highlighted in blue</span> were added with Kernel Patch XU\*8.0\*799.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists the options exported with Kernel and Kernel Toolkit.

## Menu Tree Roots

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel exports three separate menu trees. They are:

- Systems Manager Menu \[EVE\]—Eve is used by the systems manager to get to other menus. Eve contains the following submenus:
- Core Applications \[XUCORE\]
- Device Management \[XUTIO\]
- Menu Management \[XUMAINT\]
- Operations Management \[XUSITEMGR\]
- Programmer Options \[XUPROG\]
- Spool Management \[XU-SPL-MGR\]
- System Security \[XUSPY\]
- Taskman Management \[XUTM MGR\]
- User Management \[XUSER\]
- SYSTEM COMMAND OPTIONS \[XUCOMMAND\]—This menu holds the common menu options executable from anywhere in the menu processor.
- Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\]—This menu has no parent; it collects all parentless Kernel options that are intended to be scheduled through the TaskMan Schedule/Unschedule Options \[XUTM SCHEDULE\] option.

## Menu Tree Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu tree diagrams for the menus described in the “<u>Menu Tree Roots</u>” section are presented in this section.

- The menu tree diagram for the Systems Manager Menu \[EVE\] \] is broken into the individual menu trees for each EVE option.
- The menu tree diagrams for the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] and the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menus are presented intact.

### Generating Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To generate a menu tree diagram, perform the following procedure:

1.  From the Systems Manager Menu \[EVE\], select the Menu Management option \[XUMAINT\].
3.  At the “Select Menu Management Option:” prompt, select the Display Menus and Options option \[XQDISPLAY OPTIONS\]:
4.  At the “Select Display Menus and Options Option:” prompt, select the Diagram Menus option \[XUUSERACC\].
5.  At the “Select USER (U.xxxxx) or OPTION (O.xxxxx) name:” prompt, enter O.*XXXXXXXX*, where “*XXXXXXXX*” is the option name you want diagrammed (such as O.XUMAINT for the Menu Management menu).
6.  At the “DEVICE: HOME//”and “Right Margin: 80//” prompts, press Enter to display the diagram to the screen.

<span id="_Toc205036176" class="anchor"></span>Figure 7: Menus—Generating Menu Diagrams: Sample from OAKTST “Gold” Account

Core Applications ...

Device Management ...

FM VA FileMan ...

Manage Mailman ...

<span class="mark">Menu Management ...</span>

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

HL7 HL7 Main Menu ...

VDEF VDEF Configuration and Status ...

Application Utilities ...

Capacity Planning ...

Fileman Access for the OIG ...

Select Systems Manager Menu Option: <span class="mark">MENU \<Enter\></span> Management

Edit options

Key Management ...

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

<span class="mark">Display Menus and Options ...</span>

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management Option: <span class="mark">DISPLAY \<Enter\></span> Menus and Options

Abbreviated Menu Diagrams

<span class="mark">Diagram Menus</span>

Menu Diagrams (with Entry/Exit Actions)

Option Function Inquiry

Print Option File

Select Display Menus and Options Option: <span class="mark">DIAGRAM \<Enter\></span> Menus

Select USER (U.xxxxx) or OPTION (O.xxxxx) name: <span class="mark">O.XUMAINT \<Enter\></span> Menu Management

DEVICE: HOME// <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">Menu Management (XUMAINT)</span>

\|

\|

--------------------------------------------------------- Edit options

\[XUEDITOPT\]

----- Key Management ------------------------------------ Allocation of

\[XUKEYMGMT\] Security Keys

\| \[XUKEYALL\]

\|

\|---------------------------------------------- De-allocation of

\| Security Keys

\| \[XUKEYDEALL\]

\|

\|---------------------------------------------- Enter/Edit of

\| Security Keys

\| \[XUKEYEDIT\]

\|

\|---------------------------------------------- All the Keys a

\| User Needs

\| \[XQLOCK1\]

\|

\|---------------------------------------------- Allocate/De-Allo

\| cate Exclusive

\| Key(s) \[XUEXKEY\]

\| \*\*LOCKED:

\| XUEXKEY\*\*

\|

\|---------------------------------------------- Change user’s

\| allocated keys

\| to delegated

\| keys

\| \[XQKEYALTODEL\]

\|

\|---------------------------------------------- Delegate keys

\| \[XQKEYDEL\]

\|

\|---------------------------------------------- Keys For a Given

\| Menu Tree

\| \[XQLOCK2\]

\|

\|---------------------------------------------- List users

\| holding a

\| certain key

\| \[XQSHOKEY\]

\|

\|---------------------------------------------- Remove delegated

\| keys \[XQKEYRDEL\]

\|

\|---------------------------------------------- Show the keys of

a particular

user \[XQLISTKEY\]

...

### Systems Manager Menu \[EVE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Systems Manager Menu \[EVE\] contains the following menu trees:

- <u>XUCORE</u>
- <u>XUTIO</u>
- <u>XUMAINT</u>
- <u>XUSITEMGR</u>
- <u>XUPROG</u>
- <u>XU-SPL-MGR</u>
- <u>XUSPY</u>
- <u>XUTM MGR</u>
- <u>XUSER</u>
- <u>Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\]</u>
- <u>SYSTEM COMMAND OPTIONS \[XUCOMMAND\]</u>

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/057.png) REF: Each of these menu trees is listed individually in the sections that follow.

### XUCORE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc205036177" class="anchor"></span>Figure 8: XUCORE—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Core Applications (XUCORE)

\|

\|

### XUTIO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355101510" class="anchor"></span>Figure 9: XUTIO—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Device Management (XUTIO)

\|

\|

--------------------------------------------- Change Device’s Terminal Type

\[XUCHANGE\]

--------------------------------------------- Device Edit \[XUDEV\]

--------------------------------------------- Terminal Type Edit \[XUTERM\]

--------------------------------------------- Display Device Data

\[XUDISPLAY\]

--------------------------------------------- List Terminal Types \[XULIST\]

--------------------------------------------- Clear Terminal \[XUSERCLR\]

--------------------------------------------- Loopback Test of Device Port

\[XUTLOOPBACK\]

--------------------------------------------- Send Test Pattern to Terminal

\[XUTTEST\]

--------------------------------------------- Out of Service Set/Clear

\[XUOUT\]

--------------------------------------------- Clear all resources \[XUDEV

RES-CLEAR\]

--------------------------------------------- Clear one Resource \[XUDEV

RES-ONE\]

--------------------------------------------- Current Line/Port Address

\[XUDEV LINEPORT ADDR CURRENT\]

--------------------------------------------- DA Return Code Edit \[XU DA

EDIT\]

----- Device Edit \[XUDEVEDIT\] -------------PQ Print Queue Edit \[XUDEVEDITPQ\]

\|

\|-------------------------------ALL Edit All Device Fields

\| \[XUDEVEDITALL\]

\|

\|-------------------------------HFS Host File Server Device Edit

\| \[XUDEVEDITHFS\]

\|

\|-------------------------------RES Resource Device Edit

\| \[XUDEVEDITRES\]

\|

\|-------------------------------SPL Spool Device Edit

\| \[XUDEVEDITSPL\]

\|

\|-------------------------------TRM TRM or VTRM Device Edit

\[XUDEVEDITTRM\]

--------------------------------------------- Edit Line/Port Addresses

\[XUDEV LINEPORT ADDR EDIT\]

--------------------------------------------- Line/Port Address report

\[XUDEV LINEPORT ADDR RPT\]

### XUMAINT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355097730" class="anchor"></span>Figure 10: XUMAINT—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Menu Management (XUMAINT)

\|

\|

--------------------------------------------------------- Edit options

\[XUEDITOPT\]

----- Key Management ------------------------------------ Allocation of

\[XUKEYMGMT\] Security Keys

\| \[XUKEYALL\]

\|

\|---------------------------------------------- De-allocation of

\| Security Keys

\| \[XUKEYDEALL\]

\|

\|---------------------------------------------- Enter/Edit of

\| Security Keys

\| \[XUKEYEDIT\]

\|

\|---------------------------------------------- All the Keys a

\| User Needs

\| \[XQLOCK1\]

\|

\|---------------------------------------------- Allocate/De-Allo

\| cate Exclusive

\| Key(s) \[XUEXKEY\]

\| \*\*LOCKED:

\| XUEXKEY\*\*

\|

\|---------------------------------------------- Change user’s

\| allocated keys

\| to delegated

\| keys

\| \[XQKEYALTODEL\]

\|

\|---------------------------------------------- Delegate keys

\| \[XQKEYDEL\]

\|

\|---------------------------------------------- Keys For a Given

\| Menu Tree

\| \[XQLOCK2\]

\|

\|---------------------------------------------- List users

\| holding a

\| certain key

\| \[XQSHOKEY\]

\|

\|---------------------------------------------- Remove delegated

\| keys \[XQKEYRDEL\]

\|

\|---------------------------------------------- Show the keys of

a particular

user \[XQLISTKEY\]

----- Secure Menu --------------------------------------- Select Options

Delegation to be Delegated

\[XQSMD MGR\] \[XQSMD ADD\]

\|

\|---------------------------------------------- List Delegated

\| Options and

\| their Users

\| \[XQSMD BY

\| OPTION\]

\|

\|---------------------------------------------- Print All

\| Delegates and

\| their Options

\| \[XQSMD BY USER\]

\|

\|---------------------------------------------- Remove Options

\| Previously

\| Delegated \[XQSMD

\| REMOVE\]

\|

\|---------------------------------------------- Replicate or

\| Replace a

\| Delegate \[XQSMD

\| REPLICATE\]

\|

\|---------------------------------------------- Show a

\| Delegate’s

\| Options \[XQSMD

\| SHOW\]

\|

\|-------------------- Delegate’s Menu --------- Build a New Menu

\| Management \[XQSMD BUILD

\| \[XQSMD USER MENU\]

\| MENU\]

\| \|

\| \|-------------------- Edit a User’s

\| \| Options \[XQSMD

\| \| EDIT OPTIONS\]

\| \|

\| \|-------------------- Copy Everything

\| \| About an Option

\| \| to a New Option

\| \| \[XQCOPYOP\]

\| \|

\| \|-------------------- Copy One Users

\| \| Menus and Keys

\| \| to others \[XQSMD

\| \| COPY USER\]

\| \|

\| \|-------------------- Limited File

\| Manager Options

\| (Build) \[XQSMD

\| LIMITED FM

\| OPTIONS\]

\| \*\*LOCKED:

\| XQSMDFM\*\*

\|

\|

\|---------------------------------------------- Specify

Allowable New

Menu Prefix

\[XQSMD SET

PREFIX\]

--------------------------------------------------------- Restrict

Availability of

Options

\[XQRESTRICT\]

--------------------------------------------------------- Option Access By

User \[XUOPTWHO\]

--------------------------------------------------------- List Options by

Parents and Use

\[XUXREF\]

--------------------------------------------------------- Fix Option File

Pointers

\[XQOPTFIX\]

----- Help Processor ------------------------------------ Display/Edit

\[XQHELP-MENU\] Help Frames

\| \[XQHELP-DISPLAY\]

\|

\|---------------------------------------------- List Help Frames

\| \[XQHELP-LIST\]

\|

\|---------------------------------------------- New/Revised Help

\| Frames

\| \[XQHELP-UPDATE\]

\|

\|---------------------------------------------- Cross Reference

\| Help Frames

\| \[XQHELP-XREF\]

\|

\|---------------------------------------------- Assign Editors

\| \[XQHELP-ASSIGN\]

\|

\|---------------------------------------------- Unassign Editors

\| \[XQHELP-DEASSIGN

\| \]

\|

\|---------------------------------------------- Fix Help Frame

File Pointers

\[XQHELPFIX\]

-----------------------------------------------------OPED Screen-based

Option Editor

\[XQOPED\]

----- Display Menus ------------------------------------- Abbreviated Menu

and Options Diagrams

\[XQDISPLAY \[XUUSERACC2\]

OPTIONS\]

\|

\|---------------------------------------------- Diagram Menus

\| \[XUUSERACC\]

\|

\|---------------------------------------------- List

\| Unreferenced

\| Menu Options \[XQ

\| LIST

\| UNREFERENCED

\| OPTIONS\]

\|

\|---------------------------------------------- Menu Diagrams

\| (with Entry/Exit

\| Actions)

\| \[XUUSERACC1\]

\|

\|---------------------------------------------- Option Function

\| Inquiry

\| \[XUINQUIRE\]

\|

\|---------------------------------------------- Print Option

File \[XUPRINT\]

----- Menu Rebuild -------------------------------------- Build Primary

Menu Menu Trees

\[XQBUILDMAIN\] \[XQBUILDTREE\]

\|

\|---------------------------------------------- Is there a menu

\| rebuild running

\| right now?

\| \[XQRIGHTNOW\]

\|

\|---------------------------------------------- Kick Off Micro

\| Surgery

\| \[XQKICKMICRO\]

\|

\|---------------------------------------------- Most Recent Menu

\| Rebuilds

\| \[XQSHOWBUILDS\]

\|

\|---------------------------------------------- Single User Menu

Tree Rebuild

\[XQBUILDUSER\]

----- Out-Of-Order Set ---------------------------------- Create a Set of

Management Options To Mark

\[XQOOMAIN\] Out-Of-Order

\| \[XQOOMAKE\]

\|

\|---------------------------------------------- List Defined

\| Option Sets

\| \[XQOOSHOW\]

\|

\|---------------------------------------------- Mark Option Set

\| Out-Of-Order

\| \[XQOOFF\]

\|

\|---------------------------------------------- Options in the

\| Option File that

\| are Out-Of-Order

\| \[XQOOSHOFIL\]

\|

\|---------------------------------------------- Protocols Marked

\| Out-Of-Order in

\| Protocol File

\| \[XQOOSHOPRO\]

\|

\|---------------------------------------------- Recover deleted

\| option set

\| \[XQOOREDO\]

\|

\|---------------------------------------------- Remove

\| Out-Of-Order

\| Messages from a

\| Set of Options

\| \[XQOON\]

\|

\|---------------------------------------------- Toggle

options/protocol

s on and off

\[XQOOTOG\]

--------------------------------------------------------- See if a User

Has Access to a

Particular

Option

\[XQOPACCESS\]

--------------------------------------------------------- Show Users with

a Selected

primary Menu

\[XUXREF-2\]

### XUSITEMGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355102664" class="anchor"></span>Figure 11: XUSITEMGR—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Operations Management (XUSITEMGR)

\|

\|

--------------------------------------------------------- System Status

\[XUSTATUS\]

--------------------------------------------------------- Introductory

text edit

\[XUSERINT\]

--------------------------------------------------------- CPU/Service/User

/Device Stats

\[XUSTAT \]

--IPV IPv4 and IPv6 ----------------------------------VAL Validate IPv4

Address Tools and IPv6 address

\[XLFIPV IPV4 \[XLFIPV

IPV6 MENU\] VALIDATE\]

\|

\|-------------------------------------------IP4 Convert any IP

\| address to IPv4

\| \[XLFIPV

\| FORCEIP4\]

\|

\|-------------------------------------------IP6 Convert any IP

\| address to IPv6

\| \[XLFIPV

\| FORCEIP6\]

\|

\|-------------------------------------------CON Convert any IP

\| address per

\| system settings

\| \[XLFIPV CONVERT\]

\|

\|-------------------------------------------VER Show system

settings for

IPv6 \[XLFIPV

VERSION\]

-LOCK Lock Manager ------------------------------------LM Kernel Lock

Menu \[XULM LOCK Manager \[XULM

MANAGER MENU\] LOCK MANAGER\]

\*\*LOCKED: XULM

LOCKS\*\*

\|

\|------------------------------------------EDIT Edit Lock

\| Dictionary \[XULM

\| EDIT LOCK

\| DICTIONARY\]

\|

\|-------------------------------------------LOG View Lock

\| Manager Log

\| \[XULM VIEW LOCK

\| MANAGER LOG\]

\|

\|------------------------------------------SITE Edit Lock

\| Manager

\| Parameters \[XULM

\| EDIT PARAMETERS\]

\|

\|------------------------------------------PURG Purge Lock

Manager Log

\[XULM PURGE LOCK

MANAGER LOG\]

------------------------------------------------------RJD Kill off a

users' job

\[XURESJOB\]

\*\*LOCKED:

XUMGR\*\*

----- Alert Management ------------------------------SURO Alerts -

\[XQALERT MGR\] Set/Remove

\| Surrogate for

\| User \[XQALERT

\| SURROGATE

\| SET/REMOVE\]

\|

\|---------------------------------------------- Delete Old (\>14

\| d) Alerts

\| \[XQALERT DELETE

\| OLD\]

\|

\|---------------------------------------------- Make an alert on

\| the fly \[XQALERT

\| MAKE\]

\|

\|---------------------------------------------- Purge Alerts for

\| a User \[XQALERT

\| BY USER DELETE\]

\| \*\*LOCKED:

\| XQAL-DELETE\*\*

\|

\|---------------------------------------------- Set Backup

\| Reviewer for

\| Alerts \[XQAL SET

\| BACKUP REVIEWER\]

\|

\|---------------------------------------------- Surrogate for

which Users?

\[XQAL SURROGATE

FOR WHICH USERS\]

----- Alpha/Beta Test ----------------------------------- Actual Usage of

Option Usage Alpha/Beta Test

Menu \[XQAB MENU\] Options \[XQAB

\| ACTUAL OPTION

\| USAGE\]

\|

\|---------------------------------------------- Low Usage

\| Alpha/Beta Test

\| Options \[XQAB

\| LIST LOW USAGE

\| OPTS\]

\|

\|---------------------------------------------- Print Alpha/Beta

\| Errors

\| (Date/Site/Num/R

\| ou/Err) \[XQAB

\| ERR

\| DATE/SITE/NUM/RO

\| U/ERR\]

\|

\|---------------------------------------------- Send Alpha/Beta

Usage to

Developers \[XQAB

AUTO SEND\]

--------------------------------------------------------- Clean old Job

Nodes in XUTL

\[XQ XUTL \$J

NODES\]

--------------------------------------------------------- Delete Old (\>14

d\) Alerts

\[XQALERT DELETE

OLD\]

--------------------------------------------------------- Foundations

Management \[XOBU

SITE SETUP MENU\]

--------------------------------------------------------- Institution File

Query / Update

\[XUMF

INSTITUTION\]

\*\*LOCKED: XUMF

INSTITUTION\*\*

----- Kernel -------------------------------------------- Ask if

Management Menu Production

\[XUKERNEL\] Account \[XU SID

\| ASK\]

\| \*\*LOCKED:

\| XUMGR\*\*

\|

\|---------------------------------------------- Edit

\| Logical/Physical

\| Mapping \[XU SID

\| EDIT\]

\|

\|---------------------------------------------- Edit Site IP

\| lockout \[XU SITE

\| LOCKOUT\]

\|

\|---------------------------------------------- Enter/Edit

\| Kernel Site

\| Parameters

\| \[XUSITEPARM\]

\|

\|---------------------------------------------- Error Trap Param

\| Edit \[XUER EDIT

\| PARAMS\]

\|

\|---------------------------------------------- Institution DEA#

\| edit

\| \[XU-INSTITUTION-

\| DEA\]

\| \*\*LOCKED:

\| XUMGR\*\*

\|

\|---------------------------------------------- Institution Edit

\| \[XU-INSTITUTION-

\| E\]

\|

\|---------------------------------------------- Kernel New

\| Features Help

\| \[XUVERSIONEW-HEL

\| P\]

\|

\|---------------------------------------------- Kernel Parameter

\| File Edit \[XU

\| PARAM\]

\|

\|---------------------------------------------- Kernel PKI

\| Parameter Edit

\| \[XUSSPKI EDIT\]

\|

\|---------------------------------------------- Load Institution

\| NPI values \[XUMF

\| LOAD NPI\]

\| \*\*UNAVAILABLE\*\*

\|

\|-------------------- NPF cleanup main -----STA XUPS ASSESSMENT

\| menu \[XUPS NPF STATS \[XUPS

\| CLEANUP MAIN ASSESSMENT

\| MENU\] STATS\]

\| \|

\| \|-----------------DET XUPS ASSESSMENT

\| \| DETAIL \[XUPS

\| \| ASSESSMENT

\| \| DETAIL\]

\| \|

\| \|-----------------PRE XUPS PREUPDATE

\| \| NPF REPORTS

\| \| \[XUPS PREUPDATE

\| \| NPF REPORTS\]

\| \|

\| \|-----------------UPD XUPS UPDATE NEW

\| PERSON FILE DATA

\| \[XUPS UPDATE NEW

\| PERSON FILE\]

\|

\|

\|---------------------------------------------- Release IP lock

\[XU IP RELEASE\]

--------------------------------------------------------- Post sign-in

Text Edit

\[XUSERPOST\]

----- RPC Broker ---------------------------------------- RPC Listener

Management Menu Edit \[XWB

\[XWB MENU\] LISTENER EDIT\]

\|

\|---------------------------------------------- Start All RPC

\| Broker Listeners

\| \[XWB LISTENER

\| STARTER\]

\|

\|---------------------------------------------- Stop All RPC

\| Broker Listeners

\| \[XWB LISTENER

\| STOP ALL\]

\|

\|---------------------------------------------- Clear XWB Log

\| Files \[XWB LOG

\| CLEAR\]

\|

\|---------------------------------------------- Debug Parameter

\| Edit \[XWB DEBUG

\| EDIT\]

\|

\|---------------------------------------------- View XWB Log

\[XWB LOG VIEW\]

----- User Management -------------------------------FIND Find a user \[XU

Menu \[XUOPTUSER\] FINDUSER\]

\|

\|-------------------------------------------PXY Proxy User List

\| \[XUSAP PROXY

\| LIST\]

\|

\|---------------------------------------------- List users

\| \[XUSERLIST\]

\|

\|---------------------------------------------- Print Sign-on

\| Log \[XUSC LIST\]

\|

\|---------------------------------------------- Proxy

\| (Connector)

\| Detail Report

\| \[XUSAP PROXY

\| CONN DETAIL ALL\]

\|

\|---------------------------------------------- Proxy

\| (Connector)

\| Inquire \[XUSAP

\| PROXY CONN

\| DETAIL INQ\]

\|

\|---------------------------------------------- Release user

\| \[XUSERREL\]

\|

\|---------------------------------------------- Remote Access

\| User Sign-on Log

\| \[XUSEC REMOTE

\| ACCESS\]

\|

\|---------------------------------------------- User Inquiry

\| \[XUSERINQ\]

\|

\|---------------------------------------------- User Status

\| Report

\| \[XUUSERSTATUS\]

\|

\|---------------------------------------------- Users with

Foreign Visits

\[XUS VISIT

USERS\]

### XUPROG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355159640" class="anchor"></span>Figure 12: XUPROG—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Programmer Options (XUPROG)

\*\*LOCKED: XUPROG\*\*

\|

\|

-KIDS Kernel ------------ Edits and ----------------------------- Create a

Installati Distributi Build

on & on \[XPD Using

Distributi Namespace

on System ON MENU\] \[XPD BUILD

\[XPD MAIN\] \| NAMESPACE\]

\*\*LOCKED: \|

XUPROG\*\* \|

\| \|

\| \|---------------------------------- Copy Build

\| \| to Build

\| \| \[XPD COPY

\| \| BUILD\]

\| \|

\| \|---------------------------------- Edit a

\| \| Build \[XPD

\| \| EDIT

\| \| BUILD\]

\| \|

\| \|---------------------------------- Transport

\| \| a

\| \| Distributi

\| \| on \[XPD

\| \| TRANSPORT

\| \| PACKAGE\]

\| \|

\| \|---------------------------------- Old

\| \| Checksum

\| \| Update

\| \| from Build

\| \| \[XT-RTN CS

\| \| UPDATE\]

\| \|

\| \|---------------------------------- Old

\| \| Checksum

\| \| Edit

\| \| \[XT-RTN CS

\| \| EDT\]

\| \|

\| \|---------------------------------- Routine

\| \| Summary

\| \| List

\| \| \[XT-BLD

\| \| RTN LIST\]

\| \|

\| \|---------------------------------- Version

\| Number

\| Update

\| \[XT-VERSIO

\| N NUMBER\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|

\|-------------- Utilities ----------------------------- Build File

\| \[XPD Print \[XPD

\| UTILITY\] PRINT

\| \| BUILD\]

\| \|

\| \|---------------------------------- Install

\| \| File Print

\| \| \[XPD PRINT

\| \| INSTALL

\| \| FILE\]

\| \|

\| \|---------------------------------- Edit

\| \| Install

\| \| Status

\| \| \[XPD EDIT

\| \| INSTALL\]

\| \|

\| \|---------------------------------- Convert

\| \| Loaded

\| \| Package

\| \| for

\| \| Redistribu

\| \| tion \[XPD

\| \| CONVERT

\| \| PACKAGE\]

\| \|

\| \|---------------------------------- Display

\| \| Patches

\| \| for a

\| \| Package

\| \| \[XPD PRINT

\| \| PACKAGE

\| \| PATCHES\]

\| \|

\| \|---------------------------------- Purge

\| \| Build or

\| \| Install

\| \| Files \[XPD

\| \| PURGE

\| \| FILE\]

\| \|

\| \|---------------------------------- Rollup

\| \| Patches

\| \| into a

\| \| Build \[XPD

\| \| ROLLUP

\| \| PATCHES\]

\| \|

\| \|---------------------------------- Update

\| \| Routine

\| \| File \[XPD

\| \| ROUTINE

\| \| UPDATE\]

\| \|

\| \|---------------------------------- Verify a

\| \| Build \[XPD

\| \| VERIFY

\| \| BUILD\]

\| \|

\| \|---------------------------------- Verify

\| Package

\| Integrity

\| \[XPD

\| VERIFY

\| INTEGRITY\]

\|

\|

\|-------------- Installati----------------------------1 Load a

\| on \[XPD Distributi

\| INSTALLATI on \[XPD

\| ON MENU\] LOAD

\| \*\*LOCKED: DISTRIBUTI

\| XUPROGMODE ON\]

\| \*\*

\| \|

\| \|---------------------------------2 Verify

\| \| Checksums

\| \| in

\| \| Transport

\| \| Global

\| \| \[XPD PRINT

\| \| CHECKSUM\]

\| \|

\| \|---------------------------------3 Print

\| \| Transport

\| \| Global

\| \| \[XPD PRINT

\| \| INSTALL\]

\| \|

\| \|---------------------------------4 Compare

\| \| Transport

\| \| Global to

\| \| Current

\| \| System

\| \| \[XPD

\| \| COMPARE TO

\| \| SYSTEM\]

\| \|

\| \|---------------------------------5 Backup a

\| \| Transport

\| \| Global

\| \| \[XPD

\| \| BACKUP\]

\| \|

\| \|---------------------------------6 Install

\| \| Package(s)

\| \| \[XPD

\| \| INSTALL

\| \| BUILD\]

\| \|

\| \|---------------------------------- Restart

\| \| Install of

\| \| Package(s)

\| \| \[XPD

\| \| RESTART

\| \| INSTALL\]

\| \|

\| \|---------------------------------- Unload a

\| Distributi

\| on \[XPD

\| UNLOAD

\| DISTRIBUTI

\| ON\]

\|

\|

\|-------------- Patch ------------1 Patch ------------1 Patch

Monitor Processing Inquiry

Main Menu \[XTPM \[XTPM

\[XTPM PATCH PATCH

PATCH PROCESSING INQUIRY\]

MONITOR \]

MAIN MENU\] \|

\| \|

\| \|-------------2 Edit Patch

\| \| Informatio

\| \| n \[XTPM

\| \| EDIT

\| \| PATCH\]

\| \|

\| \|-------------3 Mark a

\| Non-Kids

\| Patch as

\| Complete

\| \[XTPM

\| COMPLETE A

\| NON-KIDS

\| PATCH\]

\|

\|

\|-------------2 Patch ------------1 Complete

\| Reports Patch

\| \[XTPM Installati

\| PATCH on History

\| REPORTS\] \[XTPM

\| \| COMPLETE

\| \| PATCH

\| \| HISTORY\]

\| \|

\| \|-------------2 Uninstalle

\| \| d Patches

\| \| by

\| \| Compliance

\| \| Date \[XTPM

\| \| UNINSTALLE

\| \| D BY

\| \| COMPLIANCE

\| \| \]

\| \|

\| \|-------------3 Uninstalle

\| \| d Patch

\| \| Listing -

\| \| Alphabetic

\| \| al \[XTPM

\| \| UNINSTALLE

\| \| D PATCHES\]

\| \|

\| \|-------------4 Patches

\| \| Due in the

\| \| Next Seven

\| \| Days \[XTPM

\| \| PATCHES

\| \| DUE NEXT 7

\| \| DAYS\]

\| \|

\| \|-------------5 Past Due

\| \| Patch

\| \| Report

\| \| \[XTPM PAST

\| \| DUE PATCH

\| \| REPORT\]

\| \|

\| \|-------------6 Patch

\| \| Statistics

\| \| by

\| \| Reporting

\| \| Group

\| \| \[XTPM

\| \| PATCH

\| \| STATISTICS

\| \| \]

\| \|

\| \|-------------7 Patch

\| Statistics

\| by

\| Compliance

\| Date \[XTPM

\| PATCH

\| STATS BY

\| COMPLIANCE

\| \]

\|

\|

\|-------------3 Patch ------------1 Edit the

Monitor Patch

Management Monitor

\[XTPM Parameter

PATCH File \[XTPM

MANAGEMENT EDIT PATCH

\] MONITOR

\| PARAMS\]

\|

\|-------------2 Rerun the

Nightly

Patch

Monitor

\[XTPM

RERUN

NIGHTLY\]

\*\*LOCKED:

XTPM PATCH

MONITOR

MGR\*\*

-------------------------------------------------------------NTEG Build an

‘NTEG’

routine

for a

package

\[XTSUMBLD\]

---------------------------------------------------------------PG Programmer

mode

\[XUPROGMOD

E\]

\*\*LOCKED:

XUPROGMODE

\*\*

----------------------------------------------------------------- Calculate

and Show

Checksum

Values

\[XTSUMBLD-

CHECK\]

----------------------------------------------------------------- Delete

Unreferenc

ed Options

\[XQ

UNREF’D

OPTIONS\]

----- Error ---------------------------------------------------P1 Print 1

Processing occurence

\[XUERRS\] of each

\| error for

\| T-1

\| (QUEUE)

\| \[XUERTRP

\| PRINT T-1

\| 1 ERR\]

\|

\|----------------------------------------------------P2 Print 2

\| occurrence

\| s of

\| errors on

\| T-1

\| (QUEUED)

\| \[XUERTRP

\| PRINT T-1

\| 2 ERR\]

\|

\|-----------SUM Error --------------------------------- Annotate

\| Summary an Error

\| Menu \[XUER \[XUER

\| SUMMARY\] NOTE\]

\| \|

\| \|---------------------------------- Inquire

\| \| Error

\| \| Summary

\| \| \[XUER

\| \| SUMMARY

\| \| INQUIRE\]

\| \|

\| \|---------------------------------- Purge

\| \| Error Trap

\| \| Summary

\| \| \[XUER

\| \| PURGE

\| \| ERROR

\| \| SUMMARY\]

\| \|

\| \|---------------------------------- Summary

\| \| Most

\| \| Recent

\| \| Errors

\| \| \[XUER

\| \| SUMMARY

\| \| MOST

\| \| RECENT\]

\| \|

\| \|---------------------------------- Top Errors

\| \| \[XUER

\| \| SUMMARY

\| \| TOP\]

\| \|

\| \|---------------------------------- Update

\| Error Trap

\| Summary

\| \[XUER

\| UPDATE

\| DEMAND/BAT

\| CH\]

\|

\|

\|------------------------------------------------------ Clean

\| Error Trap

\| \[XUERTRP

\| CLEAN\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|------------------------------------------------------ Error Trap

\| Display

\| \[XUERTRAP\]

\|

\|------------------------------------------------------ Interactiv

\| e Print of

\| Error

\| Messages

\| \[XUERTRP

\| PRINT

\| ERRS\]

\|

\|------------------------------------------------------ Remove a

TYPE of

error

\[XUERTRP

TYPE\]

----------------------------------------------------------------- Global

Block

Count \[XU

BLOCK

COUNT\]

----------------------------------------------------------------- List

Global

\[XUPRGL\]

\*\*LOCKED:

XUPROGMODE

\*\*

----------------------------------------------------------------- Map

Pointer

Relations

\[DI DDMAP\]

----------------------------------------------------------------- Number

base

changer

\[XT-NUMBER

BASE

CHANGER\]

\*\*LOCKED:

XUPROGMODE

\*\*

----- Routine --------------------------------------------------- %Index of

Tools Routines

\[XUPR-ROUT \[XUINDEX\]

INE-TOOLS\]

\|

\|------------------------------------------------------ Check

\| Routines

\| on Other

\| CPUs \[XUPR

\| RTN

\| CHKSUM\]

\|

\|------------------------------------------------------ Compare

\| local/nati

\| onal

\| checksums

\| report \[XU

\| CHECKSUM

\| REPORT\]

\|

\|------------------------------------------------------ Compare

\| routines

\| on tape to

\| disk

\| \[XUPR-RTN-

\| TAPE-CMP\]

\|

\|------------------------------------------------------ Compare

\| two

\| routines

\| \[XT-ROUTIN

\| E COMPARE\]

\|

\|------------------------------------------------------ Delete

\| Routines

\| \[XTRDEL\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|------------------------------------------------------ First Line

\| Routine

\| Print \[XU

\| FIRST LINE

\| PRINT\]

\|

\|------------------------------------------------------ Flow Chart

\| Entire

\| Routine

\| \[XTFCR\]

\|

\|------------------------------------------------------ Flow Chart

\| from Entry

\| Point

\| \[XTFCE\]

\|

\|------------------------------------------------------ Group

\| Routine

\| Edit

\| \[XTRGRPE\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|------------------------------------------------------ Input

\| routines

\| \[XUROUTINE

\| IN\]

\| \*\*LOCKED:

\| XUPROG\*\*

\|

\|------------------------------------------------------ List

\| Routines

\| \[XUPRROU\]

\|

\|------------------------------------------------------ Load/refre

\| sh

\| checksum

\| values

\| into

\| ROUTINE

\| file \[XU

\| CHECKSUM

\| LOAD\]

\|

\|------------------------------------------------------ Output

\| routines

\| \[XUROUTINE

\| OUT\]

\|

\|------------------------------------------------------ Routine

\| Edit \[XUPR

\| RTN EDIT\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|------------------------------------------------------ Routines

\| by Patch

\| Number

\| \[XUPR RTN

\| PATCH\]

\|

\|------------------------------------------------------ Variable

\| changer

\| \[XT-VARIAB

\| LE

\| CHANGER\]

\| \*\*LOCKED:

\| XUPROGMODE

\| \*\*

\|

\|------------------------------------------------------ Version

Number

Update

\[XT-VERSIO

N NUMBER\]

\*\*LOCKED:

XUPROGMODE

\*\*

----------------------------------------------------------------- Test an

option not

in your

menu

\[XT-OPTION

TEST\]

\*\*LOCKED:

XUMGR\*\*

----- Verifier -------------------------------------------------- Update

Tools Menu with

\[XTV MENU\] current

\| routines

\| \[XTVR

\| UPDATE\]

\|

\|------------------------------------------------------ Routine

\| Compare -

\| Current

\| with

\| Previous

\| \[XTVR

\| COMPARE\]

\|

\|------------------------------------------------------ Accumulate

\| Globals

\| for

\| Package

\| \[XTVG

\| UPDATE\]

\|

\|------------------------------------------------------ Edit

\| Verificati

\| on Package

\| File \[XTV

\| EDIT VERIF

\| PACKAGE\]

\|

\|------------------------------------------------------ Global

\| Compare

\| for

\| selected

\| package

\| \[XTVG

\| COMPARE\]

\|

\|------------------------------------------------------ Last

\| Routine

\| Change

\| Date

\| Recorded

\| \[XTVR MOST

\| RECENT

\| CHANGE

\| DATE\]

\|

\|------------------------------------------------------ UNDO Edits

(Restore

to Older

Version of

Routine)

\[XTVR

RESTORE

PREV

ROUTINE\]

### XU-SPL-MGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355161063" class="anchor"></span>Figure 13: XU-SPL-MGR—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Spool Management (XU-SPL-MGR)

\|

\|

----- Delete A Spool Document

\[XU-SPL-DELETE\]

----- Edit User’s Spooler Access

\[XU-SPL-USER\]

----- List Spool Documents

\[XU-SPL-LIST\]

----- Print A Spool Document

\[XU-SPL-PRINT\]

----- Spooler Site Parameters Edit

\[XU-SPL-SITE\]

### XUSPY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355162102" class="anchor"></span>Figure 14: XUSPY—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Information Security Officer Menu (XUSPY)

\|

\|

----- User ------------------------------------------------------ User

Security Inquiry

Menu \[XUSERINQ\]

\[XUSER SEC

OFCR\]

\|

\|------------------------------------------------------ List users

\| \[XUSERLIST

\| \]

\|

\|------------------------------------------------------ User

\| Status

\| Report

\| \[XUUSERSTA

\| TUS\]

\|

\|------------------------------------------------------ Find a

\| user \[XU

\| FINDUSER\]

\|

\|------------------------------------------------------ Switch

\| Identities

\| \[XUTESTUSE

\| R\]

\|

\|------------------------------------------------------ Show the

\| keys of a

\| particular

\| user

\| \[XQLISTKEY

\| \]

\|

\|------------------------------------------------------ See if a

\| User Has

\| Access to

\| a

\| Particular

\| Option

\| \[XQOPACCES

\| S\]

\|

\|------------------------------------------------------ User Audit

\| Display

\| \[XUUSEROPT

\| \]

\|

\|------------------------------------------------------ Deactivate

\| a User

\| \[XUSERDEAC

\| T\]

\|

\|------------------------------------------------------ Reactivate

\| a User

\| \[XUSERREAC

\| T\]

\|

\|------------------------------------------------------ ISO’s

\| Terminated

\| User

\| Report

\| \[XUSEC ISO

\| TERMINATIO

\| N REPORT\]

\|

\|------------------------------------------------------ Up Arrow

Delimited

Terminatio

n Report

\[XUSEC UP

ARROW TERM

REPORT\]

----- Fileman --------------------------------------------------- Inquiry to

Security a User’s

Menu File

\[XUFILEACC Access

ESS SEC \[XUFILEINQ

OFCR\] UIRY\]

\|

\|------------------------------------------------------ List

\| Access to

\| Files by

\| File

\| number

\| \[XUFILELIS

\| T\]

\|

\|------------------------------------------------------ Print

\| Users

\| Files

\| \[XUFILEPRI

\| NT\]

\|

\|------------------------------------------------------ Delete

\| Users’

\| Access to

\| a Set of

\| Files

\| \[XUFILESET

\| DELETE\]

\|

\|------------------------------------------------------ Single

\| file

\| add/delete

\| for a user

\| \[XUFILESIN

\| GLEADD\]

\|

\|-------------- Fileman ------------------------------- Print File

Access for Entries

the ISO \[DIPRINT\]

\[XUDIACCES

S FOR ISO\]

\|

\|---------------------------------- Search

\| File

\| Entries

\| \[DISEARCH\]

\|

\|---------------------------------- Inquire to

\| File

\| Entries

\| \[DIINQUIRE

\| \]

\|

\|-------------- Audit Menu -------- Fields

\| \[DIAUDIT\] Being

\| \*\*LOCKED: Audited

\| XUAUDITING \[DIAUDITED

\| \*\* FIELDS\]

\| \|

\| \|-------------- Data

\| \| Dictionari

\| \| es Being

\| \| Audited

\| \| \[DIAUDIT

\| \| DD\]

\| \|

\| \|-------------- Purge Data

\| \| Audits

\| \| \[DIAUDIT

\| \| PURGE

\| \| DATA\]

\| \|

\| \|-------------- Purge DD

\| \| Audits

\| \| \[DIAUDIT

\| \| PURGE DD\]

\| \|

\| \|-------------- Turn Data

\| Audit

\| On/Off

\| \[DIAUDIT

\| TURN

\| ON/OFF\]

\|

\|

\|---------------------------------- List File

Attributes

\[DILIST\]

----- Menu and -------------------------------------------------- Option

Option Function

Security Inquiry

\[XU SEC \[XUINQUIRE

OFCR\] \]

\|

\|------------------------------------------------------ Option

\| Access By

\| User

\| \[XUOPTWHO\]

\|

\|------------------------------------------------------ Print

\| Option

\| File

\| \[XUPRINT\]

\|

\|------------------------------------------------------ Diagram

\| Menus

\| \[XUUSERACC

\| \]

\|

\|------------------------------------------------------ Abbreviate

\| d Menu

\| Diagrams

\| \[XUUSERACC

\| 2\]

\|

\|------------------------------------------------------ Show Users

\| with a

\| Selected

\| primary

\| Menu

\| \[XUXREF-2\]

\|

\|------------------------------------------------------ List users

\| holding a

\| certain

\| key

\| \[XQSHOKEY\]

\|

\|------------------------------------------------------ Keys For a

\| Given Menu

\| Tree

\| \[XQLOCK2\]

\|

\|-------------- Secure -------------------------------- Show a

\| Menu Delegate’s

\| Delegation Options

\| \[XQSMD SEC \[XQSMD

\| OFCR\] SHOW\]

\| \|

\| \|---------------------------------- List

\| \| Delegated

\| \| Options

\| \| and their

\| \| Users

\| \| \[XQSMD BY

\| \| OPTION\]

\| \|

\| \|---------------------------------- Print All

\| Delegates

\| and their

\| Options

\| \[XQSMD BY

\| USER\]

\|

\|

\|------------------------------------------------------ Option

\| Audit

\| Display

\| \[XUOPTDISP

\| \]

\|

\|------------------------------------------------------ Audited

\| Options

\| Log

\| \[XUOPTLOG\]

\|

\|------------------------------------------------------ Audited

Options

Purge

\[XUOPTPURG

E\]

----- System ---------------------------------------------------- Establish

Audit Menu System

\[XUAUDIT Audit

MAINT\] Parameters

\| \[XUAUDIT\]

\|

\|------------------------------------------------------ Display

\| the Kernel

\| Audit

\| Parameters

\| \[XU-SPY-SH

\| OW\]

\|

\|------------------------------------------------------ Server

\| audit

\| display

\| \[XUSERVDIS

\| P\]

\|

\|------------------------------------------------------ Super

\| Search

\| Message

\| File \[XM

\| SUPER

\| SEARCH\]

\| \*\*LOCKED:

\| XM SUPER

\| SEARCH\*\*

\|

\|------------------------------------------------------ Bulletin

\| Selection

\| \[DG

\| BULLETIN

\| LOCAL\]

\|

\|------------------------------------------------------ Patient

\| Inquiry

\| \[DG

\| PATIENT

\| INQUIRY\]

\|

\|------------------------------------------------------ MAS

Parameter

Entry/Edit

\[DG

PARAMETER

ENTRY\]

----- Access ---------------------------------------------------- Display of

Monitor Programmer

Menu Mode Entry

\[XUMNACCES List

S\] \[XUPMDISP\]

\|

\|------------------------------------------------------ Programmer

\| Mode Entry

\| Log Purge

\| \[XUPMPURGE

\| \]

\|

\|------------------------------------------------------ Failed

\| Access

\| Attempts

\| Log

\| \[XUFAIL\]

\|

\|------------------------------------------------------ Failed

\| Access

\| Attempts

\| Log Purge

\| \[XUFPURGE\]

\|

\|------------------------------------------------------ Device

\| Failed

\| Access

\| Attempts

\| \[XUFDEV\]

\|

\|------------------------------------------------------ User

\| Failed

\| Access

\| Attempts

\| \[XUFDISP\]

\|

\|------------------------------------------------------ Print

\| Sign-on

\| Log \[XUSC

\| LIST\]

\|

\|------------------------------------------------------ Direct-mod

e

Programmer

Access

Audit

\[XUPROGAUD

\]

----- Security -------------------------------------------------- Display

Officer User

Menu \[DG Access to

SECURITY Patient

OFFICER Record \[DG

MENU\] SECURITY

\*\*LOCKED: DISPLAY

DG LOG\]

SECURITY \*\*LOCKED:

OFFICER\*\* DG

\| SECURITY

\| OFFICER\*\*

\|

\|------------------------------------------------------ Enter/Edit

\| Patient

\| Security

\| Level \[DG

\| SECURITY

\| ENTER/EDIT

\| \]

\| \*\*LOCKED:

\| DG

\| SENSITIVIT

\| Y\*\*

\|

\|------------------------------------------------------ Purge

\| Non-sensit

\| ive

\| Patients

\| from

\| Security

\| Log \[DG

\| SECURITY

\| PURGE

\| PATIENTS\]

\| \*\*LOCKED:

\| DG

\| SECURITY

\| OFFICER\*\*

\|

\|------------------------------------------------------ Purge

\| Record of

\| User

\| Access

\| from

\| Security

\| Log \[DG

\| SECURITY

\| PURGE LOG\]

\| \*\*LOCKED:

\| DG

\| SECURITY

\| OFFICER\*\*

\|

\|---------------------------------------------------EXP ISO

\| Sensitive

\| Records

\| Report-Exp

\| ort \[DG

\| SENSITIVE

\| RCDS

\| RPT-EXPORT

\| \]

\|

\|---------------------------------------------------FMT ISO

Sensitive

Records

Report-For

matted

Report \[DG

SENSITIVE

RCDS

RPT-FORMAT

\]

### XUTM MGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355162246" class="anchor"></span>Figure 15: XUTM MGR—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Taskman Management (XUTM MGR)

\|

\|

--------------------------------------------------------- Schedule/Unsched

ule Options

\[XUTM SCHEDULE\]

--------------------------------------------------------- One-time Option

Queue \[XU OPTION

QUEUE\]

----- Taskman ----------------------------------------MTM Monitor Taskman

Management \[XUTM ZTMON\]

Utilities \[XUTM

UTIL\]

\|

\|---------------------------------------------- Check Taskman’s

\| Environment

\| \[XUTM CHECK ENV\]

\|

\|-------------------- Edit Taskman ------------ Site Parameters

\| Parameters \[XUTM Edit \[XUTM

\| PARAMETER EDIT\] BVPAIR\]

\| \|

\| \|-------------------- UCI Association

\| \| Table Edit \[XUTM

\| \| UCI\]

\| \|

\| \|-------------------- Volume Set Edit

\| \[XUTM VOLUME\]

\|

\|

\|---------------------------------------------- Restart Task

\| Manager \[XUTM

\| RESTART\]

\|

\|---------------------------------------------- Place Taskman in

\| a WAIT State

\| \[XUTM WAIT\]

\|

\|---------------------------------------------- Remove Taskman

\| from WAIT State

\| \[XUTM RUN\]

\|

\|---------------------------------------------- Stop Task

\| Manager \[XUTM

\| STOP\]

\|

\|-------------------- Taskman Error ----------- Show Error Log

\| Log \[XUTM ERROR\] \[XUTM ERROR

\| \| SHOW\]

\| \|

\| \|-------------------- Clean Error Log

\| \| Over Range Of

\| \| Dates \[XUTM

\| \| ERROR LOG CLEAN

\| \| RANGE\]

\| \|

\| \|-------------------- Purge Error Log

\| \| Of Type Of Error

\| \| \[XUTM ERROR

\| \| PURGE TYPE\]

\| \|

\| \|-------------------- Delete Error Log

\| \| \[XUTM ERROR

\| \| DELETE\]

\| \|

\| \|-------------------- List Error

\| \| Screens \[XUTM

\| \| ERROR SCREEN

\| \| LIST\]

\| \|

\| \|-------------------- Add Error

\| \| Screens \[XUTM

\| \| ERROR SCREEN

\| \| ADD\]

\| \|

\| \|-------------------- Edit Error

\| \| Screens \[XUTM

\| \| ERROR SCREEN

\| \| EDIT\]

\| \|

\| \|-------------------- Remove Error

\| Screens \[XUTM

\| ERROR SCREEN

\| REMOVE\]

\|

\|

\|---------------------------------------------- Clean Task File

\| \[XUTM CLEAN\]

\|

\|---------------------------------------------- Change tasks

\| device \[XUTM RP\]

\|

\|---------------------------------------------- Problem Device

\| Clear \[XUTM

\| PROBLEM CLEAR\]

\|

\|---------------------------------------------- Problem Device

\| report. \[XUTM

\| PROBLEM DEVICES\]

\|

\|---------------------------------------------- Repoint waiting

\| tasks to a new

\| port/device

\| \[XUTM REPNT\]

\|

\|---------------------------------------------- SYNC flag file

control \[XUTM

SYNC\]

--------------------------------------------------------- List Tasks \[XUTM

INQ\]

--------------------------------------------------------- Dequeue Tasks

\[XUTM DQ\]

--------------------------------------------------------- Requeue Tasks

\[XUTM REQ\]

--------------------------------------------------------- Delete Tasks

\[XUTM DEL\]

--------------------------------------------------------- Print Options

that are

Scheduled to run

\[XUTM BACKGROUND

PRINT\]

--------------------------------------------------------- Cleanup Task

List \[XUTM TL

CLEAN\]

--------------------------------------------------------- Print Options

Recommended for

Queueing \[XUTM

BACKGROUND

RECOMMENDED\]

### XUSER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355162905" class="anchor"></span>Figure 16: XUSER—Menu Tree Diagram: Sample from OAKTST “Gold” Account

User Management (XUSER)

\|

\|

----------------------------------------------------------------- Add a New

User to

the System

\[XUSERNEW\]

----------------------------------------------------------------- Grant

Access by

Profile

\[XUSERBLK\]

\*\*LOCKED:

XUMGR\*\*

----------------------------------------------------------------- Edit an

Existing

User

\[XUSEREDIT

\]

----------------------------------------------------------------- Deactivate

a User

\[XUSERDEAC

T\]

----------------------------------------------------------------- Reactivate

a User

\[XUSERREAC

T\]

----------------------------------------------------------------- List users

\[XUSERLIST

\]

----------------------------------------------------------------- User

Inquiry

\[XUSERINQ\]

----------------------------------------------------------------- Switch

Identities

\[XUTESTUSE

R\]

----- File ------------------------------------------------------ Grant

Access Users’

Security Access to

\[XUFILEACC a Set of

ESS\] Files

\| \[XUFILEGRA

\| NT\]

\|

\|------------------------------------------------------ Copy One

\| User’s

\| File

\| Access to

\| Others

\| \[XUFILECOP

\| Y\]

\|

\|------------------------------------------------------ Single

\| file

\| add/delete

\| for a user

\| \[XUFILESIN

\| GLEADD\]

\|

\|------------------------------------------------------ Inquiry to

\| a User’s

\| File

\| Access

\| \[XUFILEINQ

\| UIRY\]

\|

\|------------------------------------------------------ List

\| Access to

\| Files by

\| File

\| number

\| \[XUFILELIS

\| T\]

\|

\|------------------------------------------------------ Print

\| Users

\| Files

\| \[XUFILEPRI

\| NT\]

\|

\|------------------------------------------------------ Delete

\| Users’

\| Access to

\| a Set of

\| Files

\| \[XUFILESET

\| DELETE\]

\|

\|------------------------------------------------------ Remove All

\| Access

\| from a

\| Single

\| User

\| \[XUFILEREM

\| OVEALL\]

\|

\|------------------------------------------------------ Take away

\| All access

\| to a File

\| \[XUFILEDEL

\| ETE\]

\|

\|------------------------------------------------------ Assign/Del

ete a File

Range

\[XUFILERAN

GEASSIGN\]

----------------------------------------------------------------- Clear

Electronic

signature

code

\[XUSESIG

CLEAR\]

\*\*LOCKED:

XUMGR\*\*

----------------------------------------------------------------- Electronic

Signature

Block Edit

\[XUSESIG

BLOCK\]

----------------------------------------------------------------- List

Inactive

Person

Class

Users

\[XU-INACTI

VE PERSON

CLASS

USERS\]

----- Manage ---------------------------------------------------- Purge

User File Inactive

\[XUSER Users’

FILE MGR\] Attributes

\| \[XUSERPURG

\| EATT\]

\|

\|------------------------------------------------------ Purge Log

\| of Old

\| Access and

\| Verify

\| Codes

\| \[XUSERAOLD

\| \]

\|

\|------------------------------------------------------ Reindex

the users

key’s

\[XUSER KEY

RE-INDEX\]

----- OAA ------------------------------------------------------E Edit

Trainee

Registrati Registrati

on Menu on Data

\[XU-CLINIC \[XU-CLINIC

AL TRAINEE AL TRAINEE

MENU\] EDIT\]

\|

\|-----------------------------------------------------I Trainee

\| Registrati

\| on Inquiry

\| \[XU-CLINIC

\| AL TRAINEE

\| INQUIRY\]

\|

\|-------------R Trainee ----------- Local ------------- List of

Reports Trainee Active

Menu Registrati Registered

\[XU-CLINIC on Reports Trainees

AL TRAINEE \[XU-CLINIC \[XU-CLINIC

REPORTS\] AL LOCAL AL ACTIVE

\| REPORTS\] TRAINEE\]

\| \|

\| \|-------------- List of

\| \| All

\| \| Registered

\| \| Trainees

\| \| \[XU-CLINIC

\| \| AL TRAINEE

\| \| LIST\]

\| \|

\| \|-------------- List of

\| \| Inactive

\| \| Registered

\| \| Trainees

\| \| \[XU-CLINIC

\| \| AL

\| \| INACTIVE

\| \| TRAINEE\]

\| \|

\| \|-------------- Total

\| Count of

\| Registered

\| Trainees

\| \[XU-CLINIC

\| AL TRAINEE

\| DB COUNT\]

\|

\|

\|-------------- Trainee ----------- Trainee

Transmissi Transmissi

on Reports on Report

to OAA by Date

\[XU-CLINIC \[XU-CLINIC

AL TRANS AL TRAINEE

REPORTS\] TRANSA\]

\|

\|-------------- Trainee

\| Transmissi

\| on Report

\| by Range

\| \[XU-CLINIC

\| AL TRAINEE

\| TRANSC\]

\|

\|-------------- Trainee

Transmissi

on Report

Selectable

Items

\[XU-CLINIC

AL TRAINEE

TRANSB\]

----------------------------------------------------------------- Person

Class Edit

\[XU-PERSON

CLASS

EDIT\]

----------------------------------------------------------------- Reprint

Access

agreement

letter

\[XUSERREPR

INT\]

### Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355164144" class="anchor"></span>Figure 17: ZTMQUEUABLE OPTIONS—Menu Tree Diagram: Sample from OAKTST “Gold” Account

Parent of Queuable Options (ZTMQUEUABLE OPTIONS)

\|

\|

----- Automatic Deactivation of Users

\[XUAUTODEACTIVATE\]

----- Clear all users at startup

\[XUSER-CLEAR-ALL\]

----- Copy the compiled menus from the

print server \[XU-486 MENU COPY\]

----- Error trap Auto clean \[XUERTRP

AUTO CLEAN\]

----- Errors Logged in Alpha/Beta Test

(QUEUED) \[XQAB ERROR LOG XMIT\]

----- Monitor Routines for Changes

\[XTRMONITOR\]

----- Non-interactive Build Primary

Menu Trees \[XQBUILDTREEQUE\]

----- One-time Option Start (Internal

Use Only) \[XU OPTION START\]

----- Print 1 occurence of each error

for T-1 (QUEUE) \[XUERTRP PRINT

T-1 1 ERR\]

----- Print 2 occurrences of errors on

T-1 (QUEUED) \[XUERTRP PRINT T-1 2

ERR\]

----- Purge of the %ZUA global.

\[XUSAZONK\]

----- Purge old spool documents

\[XU-SPL-PURGE\]

----- Purge Sign-On log \[XUSCZONK\]

----- Queuable Task Log Cleanup \[XUTM

QCLEAN\]

----- Unlinked payers notification

\[IBCNE EIV PAYER LINK NOTIFY\]

### SYSTEM COMMAND OPTIONS \[XUCOMMAND\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref355164301" class="anchor"></span>Figure 18: XUCOMMAND—Menu Tree Diagram: Sample from OAKTST “Gold” Account

SYSTEM COMMAND OPTIONS (XUCOMMAND)

\|

\|

------------------------------------------------------PRN Print File

Entries

\[DIPRINT\]

------------------------------------------------------INQ Inquire to File

Entries

\[DIINQUIRE\]

---LP Library Patron -------PLR Patron Requests

Options \[LBRY for the Local

PATRON OPTIONS\] Library \[LBRY

\| PATRON REQUESTS\]

\| \*\*UNAVAILABLE\*\*

\|

\|

\|-----------------RFP Reports for ----------PLH History of

Patrons \[LBRY Check-in \[LBRY

PATRONS REPORTS\] HIST CHK-IN\]

\|

\|-----------------JTA Journal Title

\| Availability

\| Inquiry \[LBRY

\| PATRON TITLES\]

\|

\|-----------------SLJ Subject List of

Journals

Available \[LBRY

PATRON SUBJECT\]

-TBOX User’s Toolbox ------------------------------------ Change my

\[XUSERTOOLS\] Division \[XUSER

\| DIV CHG\]

\|

\|---------------------------------------------- Display User

\| Characteristics

\| \[XUUSERDISP\]

\|

\|---------------------------------------------- Edit User

\| Characteristics

\| \[XUSEREDITSELF\]

\|

\|---------------------------------------------- Electronic

\| Signature code

\| Edit \[XUSESIG\]

\|

\|-------------------- Menu Templates ---------- Create a new

\| \[XQTUSER\] menu template

\| \| \[XQTNEW\]

\| \|

\| \|-------------------- Delete a Menu

\| \| Template

\| \| \[XQTKILL\]

\| \|

\| \|-------------------- List all Menu

\| \| Templates

\| \| \[XQTSHO\]

\| \|

\| \|-------------------- Rename a menu

\| \| template

\| \| \[XQTRNAM\]

\| \|

\| \|-------------------- Show all options

\| in a Menu

\| Template

\| \[XQTLIST\]

\|

\|

\|-------------------- Spooler Menu ------------ Allow other

\| \[XU-SPL-MENU\] users access to

\| \| spool documents

\| \| \[XU-SPL-ALLOW\]

\| \|

\| \|-------------------- Browse a Spool

\| \| Document

\| \| \[XU-SPL-BROWSE\]

\| \|

\| \|-------------------- Delete A Spool

\| \| Document

\| \| \[XU-SPL-DELETE\]

\| \|

\| \|-------------------- List Spool

\| \| Documents

\| \| \[XU-SPL-LIST\]

\| \|

\| \|-------------------- Make spool

\| \| document into a

\| \| mail message

\| \| \[XU-SPL-MAIL\]

\| \|

\| \|-------------------- Print A Spool

\| Document

\| \[XU-SPL-PRINT\]

\|

\|

\|---------------------------------------------- Switch UCI \[XU

\| SWITCH UCI\]

\|

\|---------------------------------------------- TaskMan User

\| \[XUTM USER\]

\|

\|---------------------------------------------- User Help

\[XUUSERHELP\]

--TIU Personal -----------------------------------------1 Personal

Preferences \[TIU Preferences \[TIU

PERSONAL PERSONAL

PREFERENCE MENU\] PREFERENCES\]

\|

\|---------------------------------------------2 Document List

Management \[TIU

PREFERRED

DOCUMENT LIST\]

-------------------------------------------------------VA View Alerts

\[XQALERT\]

--------------------------------------------------------- Continue

\[XUCONTINUE\]

--------------------------------------------------------- Copy Routines to

Another UCI

\[A1CI MOVE

ROUTINE\]

--------------------------------------------------------- Dispense Drug

Look-Up \[PSJU

INQ DRUG\]

--------------------------------------------------------- Halt \[XUHALT\]

----- MailMan Menu -----------------------------------NML New Messages and

\[XMUSER\] Responses

\| \[XMNEW\]

\|

\|-------------------------------------------RML Read/Manage

\| Messages

\| \[XMREAD\]

\|

\|-------------------------------------------SML Send a Message

\| \[XMSEND\]

\|

\|---------------------------------------------- Query/Search for

\| Messages

\| \[XMSEARCH\]

\|

\|-------------------------------------------AML Become a

\| Surrogate

\| (SHARED,MAIL or

\| Other)

\| \[XMASSUME\]

\|

\|-------------------- Personal ---------------- User Options

\| Preferences \[XM Edit

\| PERSONAL MENU\] \[XMEDITUSER\]

\| \|

\| \|-------------------- Banner Edit

\| \| \[XMBANNER\]

\| \|

\| \|-------------------- Surrogate Edit

\| \| \[XMEDITSURR\]

\| \|

\| \|-------------------- Message Filter

\| \| Edit \[XM FILTER

\| \| EDIT\]

\| \|

\| \|-------------------- Delivery Basket

\| \| Edit \[XM

\| \| DELIVERY BASKET

\| \| EDIT\]

\| \|

\| \|-----------------GML Enroll in (or

\| \| Disenroll from)

\| \| a Mail Group

\| \| \[XMENROLL\]

\| \|

\| \|-------------------- Personal Mail

\| \| Group Edit

\| \| \[XMEDITPERSGROUP

\| \| \]

\| \|

\| \|-------------------- Forwarding

\| Address Edit

\| \[XMEDITFWD\]

\| \*\*LOCKED:

\| XMNET\*\*

\|

\|

\|-------------------- Other MailMan ----------- Report on

\| Functions Later’d Messages

\| \[XMOTHER\] \[XMLATER-REPORT\]

\| \|

\| \|-------------------- Change/Delete

\| \| Later’d Messages

\| \| \[XMLATER-EDIT\]

\| \|

\| \|-------------------- Mailbox Contents

\| \| List

\| \| \[XMBASKLIST\]

\| \|

\| \|-----------------LML Load PackMan

\| Message \[XMPACK\]

\| \*\*LOCKED:

\| XUPROGMODE\*\*

\|

\|

\|-------------------- Help (User/Group -------- User Information

Info., etc.) \[XMHELPUSER\]

\[XMHELP\]

\|

\|-------------------- Group

\| Information

\| \[XMHELPGROUP\]

\|

\|-------------------- Remote User

\| Information

\| \[XMHELPLNK\]

\|

\|-------------------- New Features in

\| MailMan

\| \[XM-NEW-FEATURES

\| \]

\|

\|-------------------- General MailMan

\| Information

\| \[XMHELPALL\]

\|

\|-------------------- Questions and

\| Answers on

\| MailMan

\| \[XMHELPQUEST\]

\|

\|-------------------- Manual for

MailMan Users

\[XMHELP-ON-LINE-

USER_MANUAL\]

----- NOIS \[FSC MENU ------------------------------------ New Call \[FSC

NOIS\] NEW CALL\]

\|

\|---------------------------------------------- Edit Call \[FSC

\| EDIT CALL\]

\|

\|---------------------------------------------- Close Call \[FSC

\| CLOSE CALL\]

\|

\|---------------------------------------------- View Calls \[FSC

\| VIEW CALLS\]

\|

\|---------------------------------------------- List Calls \[FSC

\| LIST CALLS\]

\|

\|---------------------------------------------- Query Calls \[FSC

\| QUERY CALLS\]

\|

\|---------------------------------------------- Reports \[FSC

\| REPORTS\]

\|

\|---------------------------------------------- File Setup \[FSC

\| FILE SETUP\]

\|

\|---------------------------------------------- Schedules/Events

\[FSC EVENTS\]

--------------------------------------------------------- Restart Session

\[XURELOG\]

--------------------------------------------------------- Restore Other

Jobs you Own

\[A1CI RJD OWN

JOBS\]

--------------------------------------------------------- Swap to TST uci

\[A1CI SUP UCI

SWAP\]

--------------------------------------------------------- Time \[XUTIME\]

--------------------------------------------------------- Where am I?

\[XUSERWHERE\]

### Extended-Action Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XU USER SIGN-ON   | This is a protocol option to link other software applications that want to know about a user signon event. The protocols *must not* READ/WRITE to the screen because it may be doing a GUI signon. They can set text that is displayed to the user by calling SET^XUS1A(string). The first character should be a ! to cause the text to be placed on a new line. DUZ will be defined but other variables may *not* be. It is called from the XUS1A routine.                                                                                                                                    |
| XU USER START-UP  | Added with Kernel Patch XU\*8.0\*593, this is a protocol option used exclusively during a VistA user signon event. Items attached to this option are “TYPE: action” options in the OPTION (#19) file, which can be used for software-specific actions that prompt users for input upon VistA signon before their Primary menu option is displayed. Unlike the User sign-on event \[XU USER SIGN-ON\] option, it can provide interactive prompting to users. It is *not* used for GUI signon. It is called from the XQ12 routine.                                                                   |
| XU USER TERMINATE | This is a protocol option to link other software applications that want to know about a USER TERMINATE event. Other software can attach to this protocol option, and they will be called when a user is terminated. The call is just after the users Access and Verify Codes have been removed. DUZ will be the person that is running the terminate option. XUIFN points to the NEW PERSON (#200) file entry that is being terminated. Returns selected File \#200 data to XUSR(field name) array for NEW PERSON components. It is called in the XUSTERM routine from the XUSERP routine. |

<span id="_Ref26533411" class="anchor"></span>Table 20: Protocols—Lock Manager Utility

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XULM DISPLAY SYSTEM LOCKS | This List Template action protocol displays a list of the system locks. System locks are generally ignored within the Lock Manager. They are locks held by VASS software, such as the Kernel or HL7 package.                                                                                                                                                         |
| XULM LOCK MANAGER MENU    | This is the protocol menu for the Kernel Lock Manager List Manager screen.                                                                                                                                                                                                                                                                                           |
| XULM REFRESH LOCKS        | This List Manager action protocol re-builds the list of locks by reading the lock table.                                                                                                                                                                                                                                                                             |
| XULM SELECT LOCK          | This action allows a user to select a lock from the list. It then displays a new screen with detailed information about the lock.                                                                                                                                                                                                                                    |
| XULM GO TO                | This List Manager action asks the user where he wants to go to on the list and then shifts the display to that location.                                                                                                                                                                                                                                             |
| XULM SORT/SCREEN LOCKS    | This action provides the user with several options for how the list locks should be displayed. The options include sorting the list by patient name, sorting the list by the user name, sorting the list by the lock string, or screening the entries by lock reference, which means that only locks that relate to a specific file will be included in the display. |
| XULM SELECT NODE          | This action allows the user to select either a single computer node or all the computer nodes. If the user selects a single node, then the display of locks will include only locks placed by processes running on that node.                                                                                                                                        |
| XULM SINGLE LOCK MENU     | This is the protocol menu for the XULM DISPLAY SINGLE LOCK List Template.                                                                                                                                                                                                                                                                                        |
| XULM TERMINATE PROCESS    | This List Manager action protocol will terminate the process that is currently selected.                                                                                                                                                                                                                                                                             |

<span id="_Toc193532662" class="anchor"></span>Table 21: Options—Server Options

### Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref197063753" class="anchor"></span>Table 22: Options—Attached to Menus for Other Software</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XQAB ERROR LOG SERVER</strong></td>
<td><p>This server option stores data sent by the <strong>Errors Logged in Alpha/Beta Test (QUEUED)</strong> [XQAB ERROR LOG XMIT] option back to the developing site (usually an OITFO). As a server request to which the mail messages containing data on the types and frequencies of errors associated with a software application in alpha or beta test, this option starts a routine that processes the message contents and stores the data in the XQAB ERRORS LOGGED (#8991.5) file (<strong>^XTV(8991.5,...</strong>). The contents of the file can be processed using several options or using VA FileMan directly. The file contains data on the:</p>
<ul>
<li><p>Type of error.</p></li>
<li><p>Routine involved.</p></li>
<li><p>Option that was in use at the time of the error.</p></li>
<li><p>Date.</p></li>
<li><p>Number of errors for that date, by site (and if multiple Error Traps are used at a site, by the VOL,UCI).</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XQSCHK</strong></td>
<td>This server option tests other server options by examining the host OPTION (#19) file and returning the data associated with the target server option. A message is sent to the host site with the name of the server option to be examined on the first line of the message.</td>
</tr>
<tr class="odd">
<td><strong>XQSPING</strong></td>
<td>This is a PING server option that works like PING under TCP/IP. If you send a message to this sever option it sends it back to you, thereby showing that the network mail channel is open.</td>
</tr>
<tr class="even">
<td><strong>XU-PING-SERVER</strong></td>
<td>This is a PING server option that works like PING under TCP/IP. If you send a message to this server option, it sends it back to you.</td>
</tr>
</tbody>
</table>

<span id="_Ref197063753" class="anchor"></span>Table 22: Options—Attached to Menus for Other Software

### Options Attached to Menus for Other Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option                 | Description                                                                                          |
|------------------------|------------------------------------------------------------------------------------------------------|
| XT-KERMIT SPOOL DL | “Download a Spool file entry”; attached to Kernel Toolkit’s Kermit menu \[XT-KERMIT MENU\] menu. |

<span id="_Ref87258875" class="anchor"></span>Table 23: Options—DEA ePCS Utility

### DEA ePCS Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*580 was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility using Public Key Infrastructure (PKI). The DEA ePCS Utility consists of the standalone menu and options listed in <u>Table 23</u>:

<table>
<caption><p><span id="_Ref324243012" class="anchor"></span>Table 24: Options—Exported Kernel Options</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XU EPCS UTILITY FUNCTIONS</strong></td>
<td><p>The <strong>ePCS DEA Utility Functions</strong> [XU EPCS UTILITY FUNCTIONS] menu is the main menu for the DEA ePCS Utility. This menu includes the following options to print reports and utility functions:</p>
<ul>
<li><p><strong>Print DEA Expiration Date Null</strong> [XU EPCS EXP DATE].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p></li>
<li><p><strong>Print DISUSER DEA Expiration Date Null</strong> [XU EPCS DISUSER EXP DATE].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p></li>
<li><p><strong>Print DEA Expiration Date Expires 30 days</strong> [XU EPCS XDATE EXPIRES].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p></li>
<li><p><strong>Print DISUSER DEA Expiration Date Expires 30 days</strong> [XU EPCS DISUSER XDATE EXPIRES]. Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p></li>
<li><p><strong>Print Prescribers with Privilege</strong> [XU EPCS PRIVS].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Print DISUSER Prescribers with Privileges</strong> [XU EPCS DISUSER PRIVS].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Print PSDRPH Key Holders</strong> [XU EPCS PSDRPH].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Print Setting Parameters Privileges</strong> [XU EPCS SET PARMS].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Print Audits for Prescriber Editing</strong> [XU EPCS PRINT EDIT AUDIT].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Task Changes to DEA Prescribing Privileges Report</strong> [XU EPCS LOGICAL ACCESS].</p>
<p>Out of Order Message: <strong>PLACED OUT OF ORDER BY</strong> <strong>XU*8*765</strong></p></li>
<li><p><strong>Task Allocation Audit of PSDRPH Key Report</strong> [XU EPCS PSDRPH AUDIT].</p>
<p>Out of Order Message: <strong>PLACED OUT OF ORDER BY</strong> <strong>XU*8*765</strong></p></li>
<li><p><strong>Allocate/De-Allocate of PSDRPH Key</strong> [XU EPCS PSDRPH KEY].</p>
<p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
<li><p><strong>Edit Facility DEA# and Expiration Date</strong> [XU EPCS EDIT DEA# AND XDATE].<br />
Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XU EPCS EDIT DEA# AND XDATE</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Edit Facility DEA# and Expiration Date</strong> [XU EPCS EDIT DEA# AND XDATE] option allows users to edit the facility DEA number and Expiration Date in the Institution file (#4).</p></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS EXP DATE</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Print DEA Expiration Date Null</strong> [XU EPCS EXP DATE] option prints all active users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XU EPCS DISUSER EXP DATE</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Print DISUSER DEA Expiration Date Null</strong> [XU EPCS DISUSER EXP DATE] option prints all <strong>DISUSER</strong>ed users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>TERMINATION DATE</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS XDATE EXPIRES</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Print DEA Expiration Date Expires 30 days</strong> [XU EPCS XDATE EXPIRES] option prints all active users with DEA # and where the DEA EXPIRATION DATE expires within <strong>30</strong> days. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XU EPCS DISUSER XDATE EXPIRES</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Print DISUSER DEA Expiration Date Expires 30 days</strong> [XU EPCS DISUSER XDATE EXPIRES] option prints all <strong>DISUSER</strong>ed users with DEA # and where the DEA EXPIRATION DATE expires within <strong>30</strong> days. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS PRIVS</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong>.</p>
<p>The <strong>Print Prescribers with Privileges</strong> [XU EPCS PRIVS] option prints all active users who have privileges to any of the SCHEDULEs <strong>II</strong> through <strong>V</strong> and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>DEA#</p></li>
<li><p>VA#</p></li>
<li><p>SCHEDULESs</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XU EPCS DISUSER PRIVS</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Print DISUSER Prescribers with Privileges</strong> [XU EPCS DISUSER PRIVS] option prints all <strong>DISUSER</strong>ed users who have privileges to any of the SCHEDULEs <strong>II</strong> through <strong>V</strong> and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>DEA#</p></li>
<li><p>TERMINATION DATE</p></li>
<li><p>VA#</p></li>
<li><p>SCHEDULESs</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS PSDRPH</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Print PSDRPH Key Holders</strong> [XU EPCS PSDRPH] option prints all active users holding the <strong>PSDRPH</strong> security key. This report sorts by Division, and within DIVISION, it sorts by NAME. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>GIVEN BY (Person Who Assigned Key)</p></li>
<li><p>DATE GIVEN (Date Assigned)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XU EPCS SET PARMS</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Print Setting Parameters Privileges</strong> [XU EPCS SET PARMS] option prints all active users holding the <strong>XUEPCSEDIT</strong> security key. This option identifies individuals responsible for setting the parameters.</p></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS PRINT EDIT AUDIT</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Print Audits for Prescriber Editing</strong> [XU EPCS PRINT EDIT AUDIT] option prints information related to the editing of prescriber information.</p></td>
</tr>
<tr class="even">
<td><strong>XU EPCS LOGICAL ACCESS</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Task Changes to DEA Prescribing Privileges Report</strong> [XU EPCS LOGICAL ACCESS] option prints the setting or change to DEA prescribing privileges related to issuance of a controlled substance prescription.</p>
<p>This option only prints data from the previous day and with data that has been modified. The data is retrieved from the XUEPCS DATA (#8991.6) file.</p>
<p>This option should be scheduled to run daily.</p></td>
</tr>
<tr class="odd">
<td><strong>XU EPCS PSDRPH AUDIT</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765.</strong></p>
<p>The <strong>Task Allocation Audit of PSDRPH Key Report</strong> [XU EPCS PSDRPH AUDIT] option prints the allocation of the <strong>PSDRPH</strong> security key.</p>
<p>This option only prints data from the previous day and with data that has been modified. The report prints data for the archive XUEPCS PSDRPH AUDI T (#8991.7) file.</p>
<p>This option should be scheduled to run daily.</p></td>
</tr>
<tr class="even">
<td><strong>XU EPCS PSDRPH KEY</strong></td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689.</strong></p>
<p>The <strong>Allocate/De-Allocate of PSDRPH Key</strong> [XU EPCS PSDRPH KEY] option allows users to allocate or de-allocate the <strong>PSDRPH</strong> security key.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref324243012" class="anchor"></span>Table 24: Options—Exported Kernel Options

## Options—Listed Alphabetically by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each option listed in this section includes the following information:

- Option Name
- Option Text
- Type
- Routine/Action
- Description (including any lock, entry action, and exit action information).

### Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 24</u> lists the options that are distributed with Kernel and Kernel Toolkit for these namespaces: “XDR\*,” “XI\*,” “XPAR\*,” “XPD\*,” “XQ\*,” and “XU\*” (listed alphabetically by option name):

<table style="width:100%;">
<caption><p><span id="_Ref87259290" class="anchor"></span>Table 25: Options—Exported Toolkit Options</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Type</th>
<th>Routine / Action / RPC / Other<br />
(Based on Type)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XDR ADD VERIFIED DUPS</td>
<td><strong>Add Verified Duplicate Pair</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRMADD</strong></p></td>
<td><p>This option adds a pair of records that are <em>not</em> already identified as potential or verified duplicates to the DUPLICATE RECORD (#15) file. The pair goes through comparisons (Duplicate Tests). The comparison results in a computed value based on similarity of one record to the other. The resulting value is measured against the Potential Duplicate Threshold Percentage. When the record pair scores evaluate above this percentage, they are considered potential duplicates and are placed in the DUPLICATE RECORD (#15) file.</p>
<p>If the user has the <strong>XUMGR</strong> security key, the user has the option to bypass the Potential Duplicate Threshold Percentage thereby adding the pair directly to the DUPLICATE RECORD (#15) file.</p></td>
</tr>
<tr class="even">
<td>XDR ANCILLARY REVIEW</td>
<td><strong>Ancillary Data Review</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRRMRG0</strong></p></td>
<td>This option is used by the ancillary services to verify potential duplicates. This option is used when a user is <em>not</em> notified by an alert.</td>
</tr>
<tr class="odd">
<td>XDR APPROVE FOR MERGE</td>
<td><strong>Approve verified duplicates for merging</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>APPROVE^XDRMERGA</strong></p></td>
<td>The coordinator or team responsible for Duplicate Resolution to give final approval for selected duplicate pairs to be included in the next merge process uses this option.</td>
</tr>
<tr class="even">
<td>XDR AUTO MERGE</td>
<td><strong>Automatically Merge all Ready Verified Duplicates</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>S XDRM(“AUTO”)=““ D EN1^XDRMAIN K XDRM</strong></p>
</blockquote></td>
<td>This option non-interactively merges all verified duplicate pairs that are ready to be merged. This option may take some time, depending on how many verified duplicate pairs there are to be merged.</td>
</tr>
<tr class="odd">
<td>XDR CHECK MERGE PROCESS STATUS</td>
<td><strong>Check Merge Process Status (reverse order)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHECK^XDRMERG2</strong></p></td>
<td><p>This option indicates the status of a selected merge process (or all of them) displaying the information provided by the last checkpoint during its operation. This information includes the file that is being processed, which stage it is in, and the last internal entry processed.</p>
<p>Kernel Toolkit Patch XT*7.3*46 reversed the order of printing from last to first.</p></td>
</tr>
<tr class="even">
<td>XDR CHECK PAIR</td>
<td><strong>Check Pair of Records to see if Duplicates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDCOMP</strong></p></td>
<td>This option allows the input of two records and then run them through the Duplicate Resolution software to see what their Match Score would be. It does <em>not</em> add records to the DUPLICATE RECORD (#15) file.</td>
</tr>
<tr class="odd">
<td>XDR DISPLAY SEARCH STATUS</td>
<td><strong>Display Search Status</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDSTAT</strong></p></td>
<td><p>This option displays the status of a selected search for duplicates. It is locked with the <strong>XDR</strong> security key.</p>
<p>The status can be any of the following:</p>
<ul>
<li><p><strong>RUNNING</strong></p></li>
<li><p><strong>HALTED</strong></p></li>
<li><p><strong>ERROE(STOP)</strong></p></li>
<li><p><strong>COMPLETED</strong></p></li>
</ul>
<p>If you are checking the status to make sure the Duplicate Checking software is running you <em>must</em> make sure that <em>not</em> only is the STATUS stated to be <strong>RUNNING</strong> but also that the COUNT, which is the number of records that have been checked for duplicates, is also steadily increasing. If the COUNT is <em>not</em> increasing notify your site manager.</p></td>
</tr>
<tr class="even">
<td>XDR EDIT DUP RECORD STATUS</td>
<td><strong>Edit Duplicate Record Status</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDEDT</strong></p></td>
<td>This option edits the STATUS (#.03) field of the DUPLICATE RECORD (#15) file entry. It would be used when a pair was identified as Verified Duplicate or Verified Not A Duplicate and you want to change the status back to Potential Duplicate, Unverified.</td>
</tr>
<tr class="odd">
<td>XDR EDIT DUP RESOLUTION FILE</td>
<td><strong>Edit Duplicate Resolution File</strong></td>
<td>ScreenMan</td>
<td></td>
<td>This option edits the values used by the Duplicate Resolution software for determining whether to add an entry or <em>not</em>. Once you find the sequence of scores that best fit your facility, it is recommended that you do <em>not</em> change these values.</td>
</tr>
<tr class="even">
<td>XDR FIND POTENTIAL DUPLICATES</td>
<td><strong>Find Potential Duplicates for an Entry in a File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDFPD</strong></p></td>
<td>This option finds all potential duplicates for an entry in a file. Any potential duplicate pairs are then added to the DUPLICATE RECORD (#15) file. The user is prompted to enter the file and then to select an entry within that file.</td>
</tr>
<tr class="odd">
<td>XDR MAIN MENU</td>
<td><strong>Duplicate Resolution System</strong></td>
<td>Menu</td>
<td><p>Exit Action:</p>
<p><strong>W:$D(IOF) @IOF K AUPNLK(“ALL”)</strong></p>
<p><strong>Entry Action:</strong></p>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution System Menu”,! S AUPNLK(“ALL”)=“”</strong></p></td>
<td><p>This is the Duplicate Resolution System main menu. It is locked with the <strong>XDR</strong> security key. It includes the following options:</p>
<ul>
<li><p><strong>XDR OPERATIONS MENU</strong></p></li>
<li><p><strong>XDR UTILITIES MENU</strong></p></li>
<li><p><strong>XDR MANAGER UTILITIES<br />
</strong></p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/058.png) <strong>REF:</strong> For more information on the XDR* options, see the <em>Duplicate Record Merge: Patient Merge</em> documentation located on the VDL at: <a href="http://www.usps.com/zip4/citytown.htm?appid=2">VDL Duplicate Record Merge: Patient Merge Application Documents</a></p></td>
</tr>
<tr class="even">
<td>XDR MANAGER UTILITIES</td>
<td><strong>Manager Utilities</strong></td>
<td>Menu</td>
<td><p>Exit Action:</p>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution System Menu”,!</strong></p>
<p>Entry Action:</p>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Manager Utilities Menu”,!</strong></p></td>
<td><p>This menu controls access to various manager utilities. These utilities include Automatically merging ready to merge duplicates, Editing the DUPLICATE RESOLUTION (#15.1) file, and Purging the DUPLICATE RECORD (#15) File. This option is locked with the <strong>XDRMGR</strong> security key. It includes the following options:</p>
<ul>
<li><p><strong>XDR EDIT DUP RESOLUTION FILE</strong></p></li>
<li><p><strong>XDR PRELIMINARY SCAN</strong></p></li>
<li><p><strong>XDR PRELIMINARY SCAN LIST</strong></p></li>
<li><p><strong>XDR SEARCH ALL</strong></p></li>
<li><p><strong>XDR MERGE READY DUPLICATES</strong></p></li>
<li><p><strong>XDR STOP MERGE PROCESS</strong></p></li>
<li><p><strong>XDR RESTART MERGE PROCESS</strong></p></li>
<li><p><strong>XDR PURGE</strong></p></li>
<li><p><strong>XDR PURGE2</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XDR MERGE READY DUPLICATES</td>
<td><strong>Schedule Process to Merge Verified Duplicates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>QUE^XDRMERG0</strong></p></td>
<td>This option merges all entries that currently are ready to merge verified duplicate pairs that are <em>not</em> included in another merge process.</td>
</tr>
<tr class="even">
<td>XDR MERGE SELECTED PAIR</td>
<td><strong>Merge Selected Verified Duplicate Pair</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XDRMAIN</strong></p></td>
<td>This option selects a certain ready to merge verified duplicate pair for merging.</td>
</tr>
<tr class="odd">
<td>XDR OPERATIONS MENU</td>
<td><strong>Operations</strong></td>
<td>Menu</td>
<td><p>Exit Action:</p>
<blockquote>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution System Menu”,!</strong></p>
</blockquote>
<p>Entry Action:</p>
<blockquote>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution Operations Menu”,!</strong></p>
</blockquote></td>
<td><p>This menu contains options for running duplicate check searches and verifying and merging duplicate pairs. It includes the following options:</p>
<ul>
<li><p><strong>XDR DISPLAY SEARCH STATUS</strong></p></li>
<li><p><strong>XDR APPROVE FOR MERGE</strong></p></li>
<li><p><strong>XDR VERIFY ALL</strong></p></li>
<li><p><strong>XDR ANCILLARY REVIEW</strong></p></li>
<li><p><strong>XDR CHECK MERGE PROCESS STATUS</strong></p></li>
<li><p><strong>XDR STOP MERGE PROCESS</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XDR PRELIMINARY SCAN</td>
<td><strong>Preliminary Scan of File for errors</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDPREL</strong></p></td>
<td>This option scans through a file selected for Duplicate Resolution to check for entries within the file that are missing identifiers (which are presumed to be significant data elements) or have other problems.</td>
</tr>
<tr class="odd">
<td>XDR PRELIMINARY SCAN LIST</td>
<td><strong>List file entries identified in preliminary scan</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDPRE1</strong></p></td>
<td>This option generates a list of those entries in the file that were identified as lacking a <strong>Zero</strong> node, having a bad SSN value, or missing one or more of the identifiers in the file.</td>
</tr>
<tr class="even">
<td>XDR PRINT LIST</td>
<td><strong>Print List of File Duplicates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDLIST</strong></p></td>
<td>This option prints a list of file duplicates. You can choose to print potential duplicates, verified ready to merge duplicates, not ready to merge verified duplicates, and merged verified duplicates. You can also choose to print a brief listing or a captioned listing.</td>
</tr>
<tr class="odd">
<td>XDR PURGE</td>
<td><strong>Purge Duplicate Record File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDPRGE</strong></p></td>
<td>This option purges entries in the DUPLICATE RECORD (#15) file; you can purge just the Potential Duplicates, the Verified Non-Duplicates, or both. This option should only be used by the site manager.</td>
</tr>
<tr class="even">
<td>XDR PURGE2</td>
<td><strong>Purge Merge Process File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDPRG2</strong></p></td>
<td>This option purges selected entries in the XDR MERGE PROCESS (#15.2) file. This option should only be used by the site manager.</td>
</tr>
<tr class="odd">
<td>XDR RESTART MERGE PROCESS</td>
<td><strong>Restart a merge process</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RESTART^XDRMERGA</strong></p></td>
<td>This option schedules the restart of a merge process at the current time or at some point in the future.</td>
</tr>
<tr class="even">
<td>XDR SCAN POSSIBLE DUPLICATES</td>
<td><strong>Scan Possible Duplicates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDDATA</strong></p></td>
<td><p>This option provides a rapid scan of possible duplicates by listing the <strong>Zero</strong> node of the PATIENT (#2) file for each individual.</p>
<p>If the output is <em>not</em> queued to a printer, then the data will be sent to the VA FileMan Browser for examination.</p></td>
</tr>
<tr class="odd">
<td>XDR SEARCH ALL</td>
<td><strong>Start/Halt Duplicate Search</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDQUE</strong></p></td>
<td><p>This utility searches a selected file for potential duplicates.</p>
<p>It provides a choice of two methods. A Basic search starts at the beginning of a file and checks each record against a selected subgroup of potential duplicates. A new search takes records that have been edited and checks them against a select subgroup of records. This is a tasked job that can be started and halted until the entire file has been checked.</p></td>
</tr>
<tr class="even">
<td>XDR STOP MERGE PROCESS</td>
<td><strong>STOP an active merge process</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>STOP^XDRMERGA</strong></p></td>
<td>This option stops a currently running merge process and any associated threads.</td>
</tr>
<tr class="odd">
<td>XDR TALLY STATUS FIELDS</td>
<td><strong>Tally STATUS and MERGE STATUS fields</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRCNT</strong></p></td>
<td>This option produces a summary report of how many records are Verified Duplicates, Verified Not Duplicates, or Potential Duplicates, Unverified. The total number of records merged and ready to be merged will be displayed.</td>
</tr>
<tr class="even">
<td>XDR UTILITIES MENU</td>
<td><strong>Utilities</strong></td>
<td>Menu</td>
<td><p>Exit Action:</p>
<blockquote>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution System Menu”,!</strong></p>
</blockquote>
<p>Entry Action:</p>
<blockquote>
<p><strong>W:$D(IOF) @IOF W !,”Duplicate Resolution Utilities Menu”,!</strong></p>
</blockquote></td>
<td><p>This menu gives access to various Duplicate Resolution Utilities. It includes the following options:</p>
<ul>
<li><p><strong>XDR ADD VERIFIED DUPS</strong></p></li>
<li><p><strong>XDR CHECK MERGE PROCESS STATUS</strong></p></li>
<li><p><strong>XDR CHECK PAIR</strong></p></li>
<li><p><strong>XDR DISPLAY SEARCH STATUS</strong></p></li>
<li><p><strong>XDR EDIT DUP RECORD STATUS</strong></p></li>
<li><p><strong>XDR FIND POTENTIAL DUPLICATES</strong></p></li>
<li><p><strong>XDR PRINT LIST</strong></p></li>
<li><p><strong>XDR SCAN POSSIBLE DUPLICATES</strong></p></li>
<li><p><strong>XDR TALLY STATUS FIELDS</strong></p></li>
<li><p><strong>XDR VIEW DUPLICATE RECORD</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XDR VALID CHECK</td>
<td><strong>Identify Potential Merge Problems</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XDRDVAL1</strong></p></td>
<td>This option identifies potential merge problems.</td>
</tr>
<tr class="even">
<td>XDR VERIFY ALL</td>
<td><strong>Verify Potential Duplicates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XDRDPICK</strong></p></td>
<td>This option marks a potential duplicate as an actual duplicate (or mark a potential duplicate pair as <strong>VERIFIED - NOT DUPLICATES</strong>). The “from” and “to” records are identified and all top-level PATIENT (#2) file fields resolved, and a bulletin generated informing the Verified Duplicate mail group of the actual duplicate. If there is no interactive package merge that needs to take place, the merge process will also occur.</td>
</tr>
<tr class="odd">
<td>XDR VERIFY SELECTED PAIR</td>
<td><strong>Verify Selected Potential Duplicate Pair</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN3^XDRMAIN</strong></p></td>
<td>This option selects a Potential Duplicate pair and verify as either Verified Non-Duplicate or Verified Duplicate. The merge process will then be initiated if there are no package interactive merges that need to occur.</td>
</tr>
<tr class="even">
<td>XDR VIEW DUPLICATE RECORD</td>
<td><strong>View Duplicate Record Entries</strong></td>
<td>Inquire</td>
<td></td>
<td>This option allows you to view Duplicate Record entries in a captioned format.</td>
</tr>
<tr class="odd">
<td>XIP SYNCHRONIZE COUNTY</td>
<td><strong>Queuable Synchronize County Multiple With 5.13</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D DEQUE^XIPSYNC</strong></p>
</blockquote></td>
<td><p>This option synchronizes the master COUNTY CODE (#5.13) file and the STATE (#5) file’s COUNTY Multiple.</p>
<p>No output device is needed. It is recommended that this option have a scheduling frequency of every three months, at a time when little to no patient registration activity will be taking place.</p></td>
</tr>
<tr class="even">
<td>XIP ZIP CODE LIST</td>
<td><strong>ZIP Code List</strong></td>
<td>Print</td>
<td></td>
<td>This option produces a report of selected ZIP codes so that they can be compared to the U.S. Postal Service’s website located at: <a href="http://www.usps.com/zip4/citytown.htm">USPS Zip Code Website</a></td>
</tr>
<tr class="odd">
<td>XIPMAILSERVER</td>
<td><strong>Check file 5.13 &amp; file 5</strong></td>
<td>Server</td>
<td><p>Routine:</p>
<p><strong>XIPMAIL</strong></p></td>
<td><p>This is a server option that checks the COUNTY CODE (#5.13) and STATE (#5) files. It also checks the STATE (#5) file for any states that are <em>not</em> recognized by the Corporate Franchise Data Center (CFD).</p>
<p>Server Fields:</p>
<ul>
<li><p>SERVER ACTION: RUN IMMEDIATELY</p></li>
<li><p>SERVER MAIL GROUP: XIP SERVER RESPONSE</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XIPSRVR</td>
<td><strong>Postal Code Update Server</strong></td>
<td>Server</td>
<td><p>Routine:</p>
<p><strong>E1^XIPSRVR</strong></p></td>
<td><p>This option takes the data contained within a message on FORUM and modifies the POSTAL CODE (#5.12) file as follows:</p>
<ul>
<li><p>Adds a new postal code</p></li>
<li><p>Inactivates the postal code</p></li>
<li><p>Edits the postal code</p></li>
</ul>
<p>Server Fields:</p>
<ul>
<li><p>SERVER ACTION: RUN IMMEDIATELY</p></li>
<li><p>SERVER AUDIT: NO</p></li>
<li><p>SERVER REPLY: NO REPLY</p></li>
<li><p>SUPRESS BULLETIN: YES</p></li>
<li><p>SAVE REQUEST: SAVE REQUEST IN POSTMASTER BASKET</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XLFIPV CONVERT</td>
<td><strong>Convert any IP address per system settings</strong></td>
<td></td>
<td></td>
<td>(Released with Patch XU*8.0*605)</td>
</tr>
<tr class="even">
<td>XLFIPV FORCEIP4</td>
<td><strong>Convert any IP address to IPv4</strong></td>
<td></td>
<td></td>
<td>(Released with Patch XU*8.0*605)</td>
</tr>
<tr class="odd">
<td>XLFIPV FORCEIP6</td>
<td><strong>Convert any IP address to IPv6</strong></td>
<td></td>
<td></td>
<td>(Released with Patch XU*8.0*605)</td>
</tr>
<tr class="even">
<td>XLFIPV IPV4 IPV6 MENU</td>
<td><strong>IPV—IPv4 and IPv6 Address Tools</strong></td>
<td>Menu</td>
<td></td>
<td><p>This option was released with Patch XU*8.0*605. It includes the following options:</p>
<ul>
<li><p><strong>XLFIPV CONVERT</strong></p></li>
<li><p><strong>XLFIPV FORCEIP4</strong></p></li>
<li><p><strong>XLFIPV FORCEIP6</strong></p></li>
<li><p><strong>XLFIPV VALIDATE</strong></p></li>
<li><p><strong>XLFIPV VERSION</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XLFIPV VALIDATE</td>
<td><strong>Validate IPv4 and IPv6 address</strong></td>
<td></td>
<td></td>
<td>(Released with Patch XU*8.0*605)</td>
</tr>
<tr class="even">
<td>XLFIPV VERSION</td>
<td><strong>Show system settings for IPv6</strong></td>
<td></td>
<td></td>
<td>(Released with Patch XU*8.0*605)</td>
</tr>
<tr class="odd">
<td>XPAR EDIT BY TEMPLATE</td>
<td><strong>Edit Parameter Values with Template</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D SELTED^XPAREDT3</strong></p>
</blockquote></td>
<td>This option prompts for a Parameter template and then uses the selected template to edit parameter values.</td>
</tr>
<tr class="even">
<td>XPAR EDIT KEYWORD</td>
<td><strong>Edit Parameter Definition Keyword</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the KEYWORD field in the PARAMETER DEFINITION (#8989.51) file.</td>
</tr>
<tr class="odd">
<td>XPAR EDIT PARAMETER</td>
<td><strong>Edit Parameter Values</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D ^XPAREDIT</strong></p>
</blockquote></td>
<td>This option calls the low-level parameter editor that allows you to edit the values for every parameter. Normally, VistA software applications supply other means of editing parameters.</td>
</tr>
<tr class="even">
<td>XPAR LIST BY ENTITY</td>
<td><strong>List Values for a Selected Entity</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D ALLENTS^XPARLIST</strong></p>
</blockquote></td>
<td>This option prompts the user for the entry of an entity (such as location, user, and so on) and lists all value instances for that entity.</td>
</tr>
<tr class="odd">
<td>XPAR LIST BY PACKAGE</td>
<td><strong>List Values for a Selected Package</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D ALLPKG^XPARLIST</strong></p>
</blockquote></td>
<td>This option prompts the user for a VistA software application and lists all parameter values for the selected application.</td>
</tr>
<tr class="even">
<td>XPAR LIST BY PARAM</td>
<td><strong>List Values for a Selected Parameter</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D ALLPARS^XPARLIST</strong></p>
</blockquote></td>
<td>This option prompts the user for a parameter (that is defined in the PARAMETER DEFINITION [#8989.51] file) and lists all value instances for that parameter.</td>
</tr>
<tr class="odd">
<td>XPAR LIST BY TEMPLATE</td>
<td><strong>List Values for a Selected Template</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<blockquote>
<p><strong>D TMPLT^XPARLIST()</strong></p>
</blockquote></td>
<td>This option prompts the user for a Parameter template. Depending on the definition of the template, additional information may be requested, and then the parameter values defined by the template are displayed.</td>
</tr>
<tr class="even">
<td>XPAR MENU TOOLS</td>
<td><strong>General Parameter Tools</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains general purpose tools for managing parameters. It includes the following options:</p>
<ul>
<li><p><strong>XPAR LIST BY PARAM</strong></p></li>
<li><p><strong>XPAR LIST BY ENTITY</strong></p></li>
<li><p><strong>XPAR LIST BY PACKAGE</strong></p></li>
<li><p><strong>XPAR LIST BY TEMPLATE</strong></p></li>
<li><p><strong>XPAR EDIT PARAMETER</strong></p></li>
<li><p><strong>XPAR EDIT BY TEMPLATE</strong></p></li>
<li><p><strong>XPAR EDIT KEYWORD<br />
</strong></p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/059.png) <strong>REF:</strong> For more information on the XPAR* APIs, see the <em>Parameter Tools Supplement to Patch Description: XT*7.3*26</em> documentation located on the VDL at: <a href="http://www.va.gov/vdl/application.asp?appid=12">VDL Kernel Toolkit Application Documents</a></p></td>
</tr>
<tr class="odd">
<td>XPD BACKUP</td>
<td><strong>Backup a Transport Global</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XPDIB</strong></p></td>
<td>This option creates a MailMan message that will back up all current routines on your system that would be replaced by the packages (VistA M-based software applications) in this Transport Global. Those components that are <em>not</em> routines <em>must</em> be backed up separately if they need to be preserved.</td>
</tr>
<tr class="even">
<td>XPD BUILD NAMESPACE</td>
<td><strong>Create a Build Using Namespace</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BUILD^XPDE</strong></p></td>
<td>This option creates a new entry in the BUILD (#9.6) file and populates the entry using a namespace.</td>
</tr>
<tr class="odd">
<td>XPD COMPARE TO SYSTEM</td>
<td><strong>Compare Transport Global to Current System</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XPDCOM</strong></p></td>
<td>This option lets you compare the components of a transport global, which is currently loaded in the <strong>XTMP</strong> global, to your current system.</td>
</tr>
<tr class="even">
<td>XPD CONVERT PACKAGE</td>
<td><strong>Convert Loaded Package for Redistribution</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XPDIU</strong></p></td>
<td>This option changes a package (VistA M-based software application) that was loaded on your system, to a package that can be transported in a distribution. The loaded package will be unloaded from your system and deleted from the INSTALL (#9.7) file. A BUILD (#9.6) file entry will be created for this package. You can use the Transport a Distribution option [XPD TRANSPORT PACKAGE] to create a new distribution with this package.</td>
</tr>
<tr class="odd">
<td>XPD COPY BUILD</td>
<td><strong>Copy Build to Build</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>COPY^XPDE</strong></p></td>
<td>This option copies one entry in the BUILD (#9.6) file to another.</td>
</tr>
<tr class="even">
<td>XPD DISTRIBUTION MENU</td>
<td><strong>Edits and Distribution</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to create, edit, and transport a package (VistA M-based software application). It includes the following options:</p>
<ul>
<li><p><strong>XPD BUILD NAMESPACE</strong></p></li>
<li><p><strong>XPD COPY BUILD</strong></p></li>
<li><p><strong>XPD EDIT BUILD</strong></p></li>
<li><p><strong>XPD TRANSPORT PACKAGE</strong></p></li>
<li><p><strong>XT-BLD RTN LIST</strong></p></li>
<li><p><strong>XT-VERSION NUMBER</strong></p></li>
<li><p><strong>XT-RTN CS EDT</strong></p></li>
<li><p><strong>XT-RTN CS UPDATE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XPD EDIT BUILD</td>
<td><strong>Edit a Build</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EDIT^XPDE</strong></p></td>
<td>This option lets you edit BUILD (#9.6) file entries.</td>
</tr>
<tr class="even">
<td>XPD EDIT INSTALL</td>
<td><strong>Edit Install Status</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the STATUS and the INSTALL COMPLETE TIME fields in the INSTALL (#9.7) file.</td>
</tr>
<tr class="odd">
<td>XPD INSTALL BUILD</td>
<td><strong>Install Package(s)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XPDI</strong></p></td>
<td><p>This option starts the install process for all packages (VistA M-based software applications) in a Transport Global that are part of a distribution.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/060.png) <strong>NOTE:</strong> You <em>must</em> load the distribution <em>before</em> you can use this option to install it.</p></td>
</tr>
<tr class="even">
<td>XPD INSTALLATION MENU</td>
<td><strong>Installation</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to load, install, and restart the install of a KIDS Distribution. It includes the following options:</p>
<ul>
<li><p><strong>XPD LOAD DISTRIBUTION</strong></p></li>
<li><p><strong>XPD PRINT CHECKSUM</strong></p></li>
<li><p><strong>XPD PRINT INSTALL</strong></p></li>
<li><p><strong>XPD COMPARE TO SYSTEM</strong></p></li>
<li><p><strong>XPD BACKUP</strong></p></li>
<li><p><strong>XPD INSTALL BUILD</strong></p></li>
<li><p><strong>XPD RESTART INSTALL</strong></p></li>
<li><p><strong>XPD UNLOAD DISTRIBUTION</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XPD LOAD DISTRIBUTION</td>
<td><strong>Load a Distribution</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDIL</strong></p></td>
<td>This option loads a KIDS distribution. A distribution is a Host File Server (HFS) file that contains one or more transport globals.</td>
</tr>
<tr class="even">
<td>XPD MAIN</td>
<td><strong>Kernel Installation &amp; Distribution System</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to prepare a VistA M-based module for distribution and install the module at a site. It includes the following options:</p>
<ul>
<li><p><strong>XPD DISTRIBUTION MENU</strong></p></li>
<li><p><strong>XPD UTILITY</strong></p></li>
<li><p><strong>XPD INSTALLATION MENU</strong></p></li>
<li><p><strong>XPD AUTOMATIC PATCHING MENU</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XPD PRINT BUILD</td>
<td><strong>Build File Print</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDDP</strong></p></td>
<td>This option prints the contents of an entry in the BUILD (#9.6) file.</td>
</tr>
<tr class="even">
<td>XPD PRINT CHECKSUM</td>
<td><strong>Verify Checksums in Transport Global</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDDCS</strong></p></td>
<td>This option verifies the checksums for the components of a Transport Global and reports any checksums that are incorrect.</td>
</tr>
<tr class="odd">
<td>XPD PRINT INSTALL</td>
<td><strong>Print Transport Global</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XPDDP</strong></p></td>
<td>This option lets you print the contents of a Transport Global that is currently loaded in the <strong>^XTMP</strong> global.</td>
</tr>
<tr class="even">
<td>XPD PRINT INSTALL FILE</td>
<td><strong>Install File Print</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDDI</strong></p></td>
<td>This option prints the contents of an entry in the INSTALL (#9.7) file.</td>
</tr>
<tr class="odd">
<td>XPD PRINT PACKAGE PATCHES</td>
<td><strong>Display Patches for a Package</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDDPCK</strong></p></td>
<td>This option prints all patches installed for a package (VistA M-based software application). It displays the Date Installed and who installed the patches. It optionally prints the description of the patch. All information comes from the PACKAGE (#9.4) file.</td>
</tr>
<tr class="even">
<td>XPD PURGE FILE</td>
<td><strong>Purge Build or Install Files</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PURGE^XPDR</strong></p></td>
<td>This option purges entries in the BUILD (#9.6) or INSTALL (#9.7) files. You are prompted for the version numbers to retain.</td>
</tr>
<tr class="odd">
<td>XPD RESTART INSTALL</td>
<td><strong>Restart Install of Package(s)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XPDIR</strong></p></td>
<td>This option restarts the install process for packages (VistA M-based software applications) in a transport global.</td>
</tr>
<tr class="even">
<td>XPD ROLLUP PATCHES</td>
<td><strong>Rollup Patches into a Build</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDER</strong></p></td>
<td>This option finds all the patches for a package (VistA M-based software application) and adds their BUILD (#9.6) file definition to the package BUILD (#9.6) file definition. This enables you to create a single BUILD (#9.6) file entry that contains the definition for a patched package.</td>
</tr>
<tr class="odd">
<td>XPD ROUTINE UPDATE</td>
<td><strong>Update Routine File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>UPDT^XPDR</strong></p></td>
<td>This option lets you update the ROUTINE (#9.8) file by adding existing routine names from the current system. You enter the namespaces for the routines being updated and the namespaces of the routines to be excluded from the update. Optionally, this option goes through the ROUTINE (#9.8) file and deletes any local routine names that no longer exist on the system. Any routine listed as national will <em>not</em> be removed from the file.</td>
</tr>
<tr class="even">
<td>XPD TRANSPORT PACKAGE</td>
<td><strong>Transport a Distribution</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XPDT</strong></p></td>
<td>This option uses entries in the BUILD (#9.6) file to create a Transport Global to export packages (VistA M-based software applications). If you choose a Host File Server (HFS) file as an output device, the Transport Global is written to the <strong>HFS</strong> file, creating a distribution. If you do <em>not</em> choose a device, the Transport Global is written to the <strong>^XTMP</strong> global on your system.</td>
</tr>
<tr class="odd">
<td>XPD UNLOAD DISTRIBUTION</td>
<td><strong>Unload a Distribution</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XPDIU</strong></p></td>
<td>This option removes the Transport Global and packages (VistA M-based software applications in the INSTALL (#9.7) file for a loaded distribution. It also removes any dangling packages in the Transport Global. You can only select the starting package.</td>
</tr>
<tr class="even">
<td><span id="XPD_UTILITY_Option" class="anchor"></span>XPD UTILITY</td>
<td><strong>Utilities</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to print and verify a BUILD (#9.6) file \ entry. It also contains options to maintain the ROUTINE (#9.8) file.</p>
<p>This menu contains the following options:</p>
<ul>
<li><p><strong>Build Analyzer Main Menu</strong> [<strong>XPDANLYZ MAIN MENU]</strong> (added with Kernel Patch XU*8.0*782)</p></li>
<li><p><strong>Build File Print</strong> [<strong>XPD PRINT BUILD]</strong></p></li>
<li><p><strong>Install File Print</strong> [<strong>XPD PRINT INSTALL FILE]</strong></p></li>
<li><p><strong>Edit Install Status</strong> [<strong>XPD EDIT INSTALL</strong>]</p></li>
<li><p><strong>Convert Loaded Package for Redistribution</strong> [<strong>XPD CONVERT PACKAGE</strong>]</p></li>
<li><p><strong>Display Patches for a Package</strong> [<strong>XPD PRINT PACKAGE PATCHES</strong>]</p></li>
<li><p><strong>Purge Build or Install Files</strong> [<strong>XPD PURGE FILE</strong>]</p></li>
<li><p><strong>Rollup Patches into a Build</strong> [<strong>XPD ROLLUP PATCHES</strong>]</p></li>
<li><p><strong>Update Routine File</strong> [<strong>XPD ROUTINE UPDATE</strong>]</p></li>
<li><p><strong>Verify a Build</strong> [<strong>XPD VERIFY BUILD</strong>]</p></li>
<li><p><strong>Verify Package Integrity</strong> [<strong>XPD VERIFY INTEGRITY</strong>]</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XPD VERIFY BUILD</td>
<td><strong>Verify a Build</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>VER^XPDE</strong></p></td>
<td>This option verifies the contents of a build. It checks that every component that is listed in the build still exists on your system. You should use it before you export a package (VistA M-based software application).</td>
</tr>
<tr class="even">
<td>XPD VERIFY INTEGRITY</td>
<td><strong>Verify Package Integrity</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XPDDCS</strong></p></td>
<td>This option checks the integrity of a package (VistA M-based software application) on your system. It compares the current checksums with the checksums sent with the distribution.</td>
</tr>
<tr class="odd">
<td><span id="XPDANLYZ_MAIN_MENU_Menu" class="anchor"></span>XPDANLYZ MAIN MENU</td>
<td><strong>Build Analyzer Main Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides options to analyze the components of a VistA build to identify adherence to standards and best practices.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/061.png) <strong>NOTE:</strong> This menu was released with Kernel Patch XU*8.0*782.</p></td>
</tr>
<tr class="even">
<td><span id="XPDANLYZ_Option" class="anchor"></span>XPDANLYZ</td>
<td><strong>KIDS Build Analyzer</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>START^XPDANLYZ1(4)</strong></td>
<td><p>This option goes through components of a build looking for inconsistencies with standards and practices.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/062.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*782.</p></td>
</tr>
<tr class="odd">
<td><span id="XPDANLYZ_DEL_Option" class="anchor"></span>XPDANLYZ_DEL</td>
<td><strong>Delete Build Analyzer Text Files</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>FSHOW^XPDANLYZ5</strong></td>
<td><p>This option looks for text files on the system beginning with <strong>XPBA</strong> allowing the user to delete one or more of them.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/063.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*782.</p></td>
</tr>
<tr class="even">
<td><span id="XPDANLYZ_SQA_Option" class="anchor"></span>XPDANLYZ_SQA</td>
<td><strong>KIDS Build Analyzer - Full SQA Search</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>START^XPDANLYZ1(5)</strong></td>
<td><p>This option reviews components of a VistA build, checking for inconsistencies with standards and practices. It is like the XPDANLYZ option; however, this option shows all lines with the search items in the SQA review.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/064.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*782.</p></td>
</tr>
<tr class="odd">
<td>XQ LIST UNREFERENCED OPTIONS</td>
<td><strong>List Unreferenced Menu Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LIST^XQ33</strong></p></td>
<td>(Released with Patch XU*8.0*614) This option runs a report listing unreferenced options in the OPTION (#19) file. It lists entries that are <em>not</em> assigned to any user or attached to any other menu option. It does <em>not</em> include options that are assigned in TaskMan or have the KEEP FROM DELETING (#209.2) field set to “<strong>Yes</strong>”.</td>
</tr>
<tr class="even">
<td>XQ UNREF’D OPTIONS</td>
<td><strong>Delete Unreferenced Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ33</strong></p></td>
<td>This option can be used to examine those options that are <em>not</em> on any menu, are <em>not</em> used as primary or secondary options, and are <em>not</em> tasked to run. The user may then decide in each case whether to delete the unreferenced option.</td>
</tr>
<tr class="odd">
<td>XQ XUTL $J NODES</td>
<td><strong>Clean old Job Nodes in XUTL</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ82</strong></p></td>
<td><p>This option should be scheduled to run once a day after midnight.</p>
<p>It can be run from a host system script to get non-global files like <strong>^TMP</strong>.</p>
<p>This option cleans up several temporary globals that applications may have left behind or got left because of trapping and error or other abnormal job termination.</p>
<p>This option causes old job-related nodes that may remain in the following globals to be removed:</p>
<ul>
<li><p><strong>^XUTL(“XQ”,$J,</strong></p></li>
<li><p><strong>^UTILITY($J,</strong></p></li>
<li><p><strong>^TMP($J,</strong></p></li>
</ul>
<p>An old job node is one that was started seven days prior to the current day, irrespective of the time of day. Does <em>not</em> have a <strong>^XUTL(“XQ”,$J,“KEEPALIVE”)</strong> node with a more current date in <strong>$H</strong> format. If it has a <strong>^XUTL(“XQ”,$J,“ZTSKNUM”)</strong> node and a lock of <strong>^%ZTSCH(“TASK”,tasknumber)</strong> is in place it will <em>not</em> be purged.</p>
<p>It looks at <strong>^UTILITY($J)</strong> and <strong>^TMP($J)</strong> for entries without a <strong>^XUTL(“XQ”,$J)</strong> to kill. It looks at <strong>^UTILITY(namespace,$J)</strong> and <strong>^TMP(namespace,$J)</strong> for entries without a <strong>^XUTL(“XQ”,$J)</strong> to kill.</p>
<p>It looks for <strong>^XTMP(namespace)</strong> entries without a <strong>Zero</strong> node or the <strong>Zero</strong> node date is less than today.</p>
<p>It looks for signon log “<strong>CUR</strong>”, “<strong>AS1</strong>” and “<strong>AS2</strong>” cross-reference entries more than seven days old and sets the current date as the signoff value and sets the FORCE CLOSE field to “<strong>Yes</strong>”.</p>
<p>It clears menu build nodes in <strong>^XUTL(“XQO”,n,“^BUILD”)</strong>.</p>
<p>It clears any <strong>^DISV</strong> data for terminated users.</p></td>
</tr>
<tr class="even">
<td>XQAB ACTUAL OPTION USAGE</td>
<td><strong>Actual Usage of Alpha/Beta Test Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ACTUAL^XQABLIST</strong></p></td>
<td>This option is available for listing actual usage of options within a package that is in alpha or beta testing. It lists only those options that have been accessed one or more times since the last installation of the package.</td>
</tr>
<tr class="odd">
<td>XQAB AUTO SEND</td>
<td><strong>Send Alpha/Beta Usage to Developers</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DOMAIL^XQABLIST</strong></p></td>
<td><p>This option is set up to automatically send to the developing OITFO information on the usage of options in those packages currently in test status.</p>
<p>If it is selected manually, it sends similar messages as well.</p></td>
</tr>
<tr class="even">
<td>XQAB ERR DATE/SITE/NUM/ROU/ERR</td>
<td><strong>Print Alpha/Beta Errors (Date/Site/Num/Rou/Err)</strong></td>
<td>Print</td>
<td></td>
<td><p>This option prints a listing of alpha/beta test errors reported from the test sites. The print is for a range of dates and lists the sites, the number of the errors reported by a site, the routine involved, and the error text. The range of dates, sites, and routine names are user selectable. The output format includes:</p>
<ul>
<li><p>Date of Errors</p></li>
<li><p>Site.name</p></li>
<li><p>Number.of.errors</p></li>
<li><p>Routine</p></li>
<li><p>Error.text</p></li>
</ul>
<p>The subtotals and totals are given for number of errors.</p></td>
</tr>
<tr class="odd">
<td>XQAB ERROR LOG SERVER</td>
<td><strong>Handle Alpha/Beta Errors Logged at Sites</strong></td>
<td>Server</td>
<td><p>Routine:</p>
<p><strong>XQABELOG</strong></p>
<ul>
<li><p>Suppress Bulletin: <strong>YES, SUPRESS IT</strong></p></li>
<li><p>Server Action: <strong>RUN IMMEDIATELY</strong></p></li>
<li><p>Server Reply: <strong>NO REPLY (DEFAULT)</strong></p></li>
</ul></td>
<td><p>This SERVER option stores data sent by the XQAB ERROR LOG XMIT option back to the developing site (usually an OITFO). As a server to which the mail messages containing data on the types and frequencies of errors associated with an application package in alpha or beta test, this option starts a routine that processes the message contents and stores the data in File #8991.5 (<strong>^XTV(8991.5,...</strong>). The contents of the file can be processed using several options or use by VA FileMan directly. The file contains data on the following:</p>
<ul>
<li><p>Type of error</p></li>
<li><p>Routine involved</p></li>
<li><p>Option that was in use at the time of the error</p></li>
<li><p>Date</p></li>
<li><p>Number of errors for that date, by site (and if multiple Error Traps are used at a site, by the VOL,UCI)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQAB ERROR LOG XMIT</td>
<td><strong>Errors Logged in Alpha/Beta Test (QUEUED)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQABERR</strong></p>
<p>Scheduling Recommended: <strong>YES</strong></p></td>
<td><p>This option identifies any errors associated with an application package hat is in either alpha or beta test. The identified errors are combined in a mail message that includes the following:</p>
<ul>
<li><p>Type of error</p></li>
<li><p>Routine involved</p></li>
<li><p>Date (usually the previous day)</p></li>
<li><p>Option that was being used at the time of the error</p></li>
<li><p>Number of times the error was logged.</p></li>
<li><p>Volume and UCI are included so that stations with error logs being maintained on different CPUs can run the task on each different system.</p></li>
</ul>
<p>This option was designed to be tasked. It does <em>not</em> require a device and generates a mail message to the developing OITFO. An alpha or beta package is indicated by the presence of the package (and its namespaces in the ALPHA/BETA TEST PACKAGE (#32) Multiple field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.</p>
<p>The option should usually be scheduled to run after midnight and scheduled for re-queuing at a daily interval.</p></td>
</tr>
<tr class="odd">
<td>XQAB LIST LOW USAGE OPTS</td>
<td><strong>Low Usage Alpha/Beta Test Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LOW^XQABLIST</strong></p></td>
<td>This option is available for obtaining a listing of options that are in a package under alpha or beta testing and have low levels of use since the last installation of the package. An option with low use is any option in the package namespaces with <strong>Zero</strong> to <strong>five</strong> accesses.</td>
</tr>
<tr class="even">
<td>XQAB MENU</td>
<td><strong>Alpha/Beta Test Option Usage Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu option is available for accessing the following options related to usage of options in alpha or beta test packages:</p>
<ul>
<li><p><strong>XQAB ACTUAL OPTION USAGE</strong></p></li>
<li><p><strong>XQAB LIST LOW USAGE OPTS</strong></p></li>
<li><p><strong>XQAB AUTO SEND</strong></p></li>
<li><p><strong>XQAB ERR DATE/SITE/NUM/ROU/ERR</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XQAL ALERT LIST FROM DATE</td>
<td><strong>List Alerts for a user from a specified</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XQARPRT2</strong></p></td>
<td><p>This option reports all alerts from the ALERT TRACKING (#8992.1) file for a selected user within a specified date range. If an end date is <em>not</em> specified, the report does <em>not</em> run.</p>
<p>The listing includes the following:</p>
<ul>
<li><p>Internal Entry Number (IEN) for the alert in the ALERT TRACKING (#8992.1) file.</p></li>
<li><p>Date and time the alert was generated.</p></li>
<li><p>Message text of the alert.</p></li>
<li><p>Information about any option or routine to be executed for processing the alert.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQAL CRITICAL ALERT COUNT</td>
<td><strong>Critical Alerts Count Report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CRITICAL^XQARPRT1</strong></p></td>
<td><p>This option generates a report of users who have alerts defined as <strong>Critical</strong> based upon inclusion of text entries from the ALERT CRITICAL TEXT (#8992.3) file between the specified start and end dates. For example, <strong>Critical</strong>-type alerts contain the following words:</p>
<ul>
<li><p><strong>ABNL IMA</strong></p></li>
</ul>
<blockquote>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/065.png) <strong>NOTE:</strong> This entry was added with Kernel Patch XU*8.0*690.</p>
</blockquote>
<ul>
<li><p><strong>ABNORMAL IMA</strong></p></li>
<li><p><strong>CRITICAL</strong></p></li>
<li><p><strong>POSSIBLE MALIG</strong></p></li>
</ul>
<p>How the report is presented depends on the order by which method the user selects:</p>
<ul>
<li><p><strong>Name—</strong>Report lists items alphabetized by name.</p></li>
<li><p><strong>Number—</strong>Report list items in descending order for the number of <strong>Critical</strong>-type alerts present.</p></li>
</ul>
<p>Kernel Patch XU*8.0*690 modified the <strong>Critical Alerts Count Report</strong> output, so any <strong>Critical</strong>-type alerts preceded with the words "<strong>NOT</strong>" or “<strong>NON</strong>”, the only two supported <strong>Critical</strong>-type alert negation indicators, are automatically screened from this report.</p>
<p>For each user who has the specified number of <strong>Critical</strong>-type alerts or more, the report includes the following:</p>
<ul>
<li><p><strong>Name—</strong>User name.</p></li>
<li><p><strong>Service/Section—</strong>Section/Service for the user.</p></li>
<li><p><strong>Alerts—</strong>Number of alerts in the ALERT (#8992) file.</p></li>
<li><p><strong>Last Sign-on—</strong>Last sign-on date.</p></li>
<li><p><strong>CRIT—</strong>Number of alerts with <strong>Critical</strong>-type text.</p></li>
<li><p><strong>Alert—</strong>Date of the oldest alert.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XQAL GUI ALERTS</td>
<td><strong>Kernel GUI Alerts</strong></td>
<td>Broker (Client / Server)</td>
<td></td>
<td><p>This is the context option for the Kernel Alert components:</p>
<ul>
<li><p>RPC: <strong>XQAL GUI ALERTS</strong></p></li>
<li><p>RPC: <strong>XUS KEY CHECK</strong></p></li>
<li><p>RPC: <strong>DDR DELETE ENTRY</strong></p></li>
<li><p>RPC: <strong>DDR FILER</strong></p></li>
<li><p>RPC: <strong>DDR FIND1</strong></p></li>
<li><p>RPC: <strong>DDR FINDER</strong></p></li>
<li><p>RPC: <strong>DDR GET DD HELP</strong></p></li>
<li><p>RPC: <strong>DDR GETS ENTRY DATA</strong></p></li>
<li><p>RPC: <strong>DDR KEY VALIDATOR</strong></p></li>
<li><p>RPC: <strong>DDR LISTER</strong></p></li>
<li><p>RPC: <strong>DDR LOCK/UNLOCK NODE</strong></p></li>
<li><p>RPC: <strong>DDR VALIDATOR</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQAL NO BACKUP REVIEWER</td>
<td><strong>No Alert Backup Reviewer</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RPT1^XUP468</strong></p></td>
<td>This option runs the report that generates a list of active users/providers that hold the <strong>ORES</strong> security key and backup reviewers for alerts.</td>
</tr>
<tr class="odd">
<td>XQAL PATIENT ALERT LIST</td>
<td><strong>Patient Alert List for specified date</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DTPT^XQARPRT2</strong></p></td>
<td><p>This option obtains a list of alerts for a specified patient from the ALERT TRACKING (#8992.1) file for a selected date.</p>
<p>A prompt is provided to obtain a quick scan listing of dates with at least some alerts for the patient on it based on OR and DVB alerts (other patient-related alerts need to be identified by looking at each alert’s message text and are included in the full list, but <em>not</em> the quick scan).</p>
<p>The listing includes:</p>
<ul>
<li><p>Internal entry number for the alert in the ALERT TRACKING (#8992.1) file</p></li>
<li><p>Date and time the alert was generated</p></li>
<li><p>Message text of the alert</p></li>
<li><p>Information about any option or routine to be executed for processing the alert</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQAL REPORTS MENU</td>
<td><strong>Report Menu for Alerts</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides several options for generating reports on alerts for users or patients. It includes the following options:</p>
<ul>
<li><p><strong>XQAL USER ALERTS COUNT</strong></p></li>
<li><p><strong>XQAL CRITICAL ALERT COUNT</strong></p></li>
<li><p><strong>XQAL ALERT LIST FROM DATE</strong></p></li>
<li><p><strong>XQAL PATIENT ALERT LIST</strong></p></li>
<li><p><strong>XQAL VIEW ALERT TRACKING ENTRY</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XQAL SET BACKUP REVIEWER</td>
<td><strong>Set Backup Reviewer for Alerts</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BKUPREVW^XQALDEL</strong></p></td>
<td>This option provides a mechanism for a user to set entries into the PARAMETERS (#8989.5) file that will assign an individual as Backup Reviewer for alerts if there is a date specified for Days For Backup Reviewer in the Alert. If this is the case, an alert that remains unread for the indicated number of days will be forwarded to the Backup Reviewer found for the lowest level for the user in the PARAMETERS (#8989.5) file starting with User, and progressing through OERR Team, Service, Division, up to System.</td>
</tr>
<tr class="even">
<td>XQAL SURROGATE FOR WHICH USERS</td>
<td><strong>Surrogate for which Users?</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>GETFOR^XQALSURO</strong></p></td>
<td>This option provides a view of which users have specified a selected user as surrogates for themselves.</td>
</tr>
<tr class="odd">
<td>XQAL USER ALERTS COUNT</td>
<td><strong>User Alerts Count Report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XQARPRT1</strong></p></td>
<td><p>This option generates a report on users who have more than a specified number of alerts in the ALERT (#8992) file. This report also includes users who have alerts defined as <strong>Critical</strong> based upon inclusion of text entries from the ALERT CRITICAL TEXT (#8992.3) file. For example, <strong>Critical</strong>-type alerts containing the following words:</p>
<ul>
<li><p><strong>ABNL IMA</strong></p></li>
</ul>
<blockquote>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/066.png) <strong>NOTE:</strong> This entry was added with Kernel Patch XU*8.0*690.</p>
</blockquote>
<ul>
<li><p><strong>ABNORMAL IMA</strong></p></li>
<li><p><strong>CRITICAL</strong></p></li>
<li><p><strong>POSSIBLE MALIG</strong></p></li>
</ul>
<p>Kernel Patch XU*8.0*690 modified the <strong>User Alerts Count Report</strong> output, so any <strong>Critical</strong>-type alerts preceded with the words "<strong>NOT</strong>" or “<strong>NON</strong>”, the only two supported <strong>Critical</strong>-type alert negation indicators, are automatically screened from this report.</p>
<p>The report covers a specified range of dates, and can be sorted by any of the following data:</p>
<ul>
<li><p>User name.</p></li>
<li><p>Number of alerts.</p></li>
<li><p>Service/Section.</p></li>
</ul>
<p>In addition, the report in each of these formats may be generated by Divisions if desired.</p>
<p>For each user who has the specified number of alerts or more, the report includes the following:</p>
<ul>
<li><p><strong>Name—</strong>User name.</p></li>
<li><p><strong>Service/Section—</strong>Section/Service for the user.</p></li>
<li><p><strong>Alerts—</strong>Number of alerts in the ALERTS (#8992) file.</p></li>
<li><p><strong>Last Sign-on—</strong>Last sign-on date.</p></li>
<li><p><strong>CRIT—</strong>Number of alerts with <strong>Critical</strong>-type text.</p></li>
<li><p><strong>Alert—</strong>Date of the oldest alert.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQAL VIEW ALERT TRACKING ENTRY</td>
<td><strong>View data for Alert Tracking file entry</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>VIEWTRAK^XQARPRT2</strong></p></td>
<td>This option can be used to view data for one or more entries in the ALERT TRACKING (#8992.1) file in captioned format. The internal entry numbers for the entries to be displayed <em>must</em> be entered individually.</td>
</tr>
<tr class="odd">
<td>XQALERT</td>
<td><strong>View Alerts</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DOIT^XQALERT</strong></p>
<p>Exit Action:</p>
<p><strong>K:$D(ORVP) ORVP</strong></p></td>
<td>This option selects alerts or notifications produced by application packages for viewing or to perform any actions associated with the alert or notification received.</td>
</tr>
<tr class="even">
<td>XQALERT BY USER DELETE</td>
<td><strong>Purge Alerts for a User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>USERDEL^XQALERT</strong></p></td>
<td>This option permits users holding the <strong>XQAL-DELETE</strong> security key to delete alerts for another user. This is intended for when a user has been inactive for a time-period (such as vacation, and so on) and has accumulated several alerts that should <em>not</em> need processing.</td>
</tr>
<tr class="odd">
<td><span id="XQALERT_DELETE_OLD_Option" class="anchor"></span>XQALERT DELETE OLD</td>
<td><strong>Delete Old (&gt;14 d) Alerts</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OLDDEL^XQALERT</strong></p></td>
<td><p>This option removes alerts that remain in the ALERT (#8992) file Applications can set a retention date (or even keep indefinitely for some clinical alerts). The <strong>&gt;14d</strong> is the default if a retention date is <em>not</em> set.</p>
<p>Kernel Patch XU*8*798 addressed accidental purging of alerts by eliminating interactive use of the <strong>Delete Old (&gt;14 d) Alerts</strong> [XQALERT DELETE OLD] option. This option remains on the <strong>Alert Management</strong> [XQALERT MGR] and <strong>Operations Management</strong> [XUSITEMGR] menus, but you are only able to invoke it from TaskMan.</p></td>
</tr>
<tr class="even">
<td>XQALERT MAKE</td>
<td><strong>Make an alert on the fly</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQALMAKE</strong></p></td>
<td>This option creates an alert and sends it to users or mail groups on-the-fly.</td>
</tr>
<tr class="odd">
<td>XQALERT MGR</td>
<td><strong>Alert Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides a menu of options for managing alerts. These options include the ability to delete options based on time or a particular user, to generate a new alert, and so on. It includes the following options:</p>
<ul>
<li><p><strong>XQALERT BY USER DELETE</strong></p></li>
<li><p><strong>XQALERT DELETE OLD</strong></p></li>
<li><p><strong>XQALERT MAKE</strong></p></li>
<li><p><strong>XQALERT SURROGATE SET/REMOVE</strong></p></li>
<li><p><strong>XQAL SURROGATE FOR WHICH USERS</strong></p></li>
<li><p><strong>XQAL SET BACKUP REVIEWER</strong></p></li>
<li><p><strong>XQAL REPORTS MENU</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQALERT SURROGATE SET/REMOVE</td>
<td><strong>Alerts - Set/Remove Surrogate for User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OTHRSURO^XQALSURO</strong></p></td>
<td><p>System administrators or ADPACs can use this option to set or remove a surrogate for receiving alerts for a user. The option prompts for a user to be selected, then is ready to specify a new surrogate for the selected user, or to remove the current surrogate for that user.</p>
<p>This option is <em>not</em> needed by the individual users who may select to name or remove a surrogate as one of the options while processing alerts (or, if no alerts are present for the user, as his only option on selecting alert processing).</p></td>
</tr>
<tr class="odd">
<td>XQBUILDMAIN</td>
<td><strong>Menu Rebuild Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the main menu for all menu rebuild options. It includes the following options:</p>
<ul>
<li><p><strong>XQSHOWBUILDS</strong></p></li>
<li><p><strong>XQKICKMICRO</strong></p></li>
<li><p><strong>XQRIGHTNOW</strong></p></li>
<li><p><strong>XQBUILDTREE</strong></p></li>
<li><p><strong>XQBUILDUSER</strong></p></li>
</ul>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XQBUILDTREE</td>
<td><strong>Build Primary Menu Trees</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BUILD^XQ81</strong></p></td>
<td>This option can be used to force the rebuilding of the tree structures used for the <strong>^JUMP</strong>. Whenever an item in a menu is modified, the tree <em>must</em> get rebuilt. This happens automatically the first time it is referenced but forcing the rebuild can often save time. The rebuilding of all trees can be queued.</td>
</tr>
<tr class="odd">
<td>XQBUILDTREEQUE</td>
<td><strong>Non-interactive Build Primary Menu Trees</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>QUE^XQ81</strong></p>
<p>Exit Action:</p>
<p><strong>;S XQSTOP=$$HTE^XLFDT($H),^FINN(DT,”STOP”)=XQSTOP K XQSTOP</strong></p></td>
<td><p>This option may be queued to run at a given frequency (such as daily) and does <em>not</em> require interaction with a user at the time it is run.</p>
<p>Other than being non-interactive it does the same job as <strong>XQBUILDTREE</strong> with specification of no verification and queue the job.</p></td>
</tr>
<tr class="even">
<td>XQBUILDUSER</td>
<td><strong>Single User Menu Tree Rebuild</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>USER^XQ84</strong></p></td>
<td><p>(Released with Patch XU*8.0*614) This option collects the menus that a user has in the primary and secondary fields of the OPTION (#19) file and then rebuilds the menu tree. It is attached to the <strong>Menu Rebuild Menu</strong> [XQBUILDMAIN] option.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/067.png) <strong>NOTE:</strong> Other users might have the same menu tree, but this will only rebuild the menu tree for the selected user.</p></td>
</tr>
<tr class="odd">
<td>XQCOPYOP</td>
<td><strong>Copy Everything About an Option to a New Option</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ11</strong></p></td>
<td>This option does a <strong>%RCR</strong> copy of one option’s fields into a new option. It also tries to enforce namespacing rules when the new option is named.</td>
</tr>
<tr class="even">
<td>XQDIAGMENU</td>
<td><strong>Menu Diagrams</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains the various methods of diagramming menus. It includes the following methods:</p>
<ul>
<li><p><strong>XUUSERACC</strong></p></li>
<li><p><strong>XUUSERACC2</strong></p></li>
<li><p><strong>XUUSERACC1</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XQDISPLAY OPTIONS</td>
<td><strong>Display Menus and Options</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is a menu of options that help the user display menus and their options. It includes the following options:</p>
<ul>
<li><p><strong>XUINQUIRE</strong></p></li>
<li><p><strong>XUPRINT</strong></p></li>
<li><p><strong>XUUSERACC1</strong></p></li>
<li><p><strong>XUUSERACC2</strong></p></li>
<li><p><strong>XUUSERACC</strong></p></li>
<li><p><strong>XQ LIST UNREFERENCED</strong> <strong>OPTIONS</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQHELP-ASSIGN</td>
<td>Assign Editors</td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XQ61</strong></p></td>
<td>This option allows the author of a help frame to assign editors. A help frame is editable thru <strong>^E</strong> by the author, the editors, and anyone holding the <strong>XUAUTHOR</strong> security key.</td>
</tr>
<tr class="odd">
<td>XQHELP-DEASSIGN</td>
<td><strong>Unassign Editors</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XQ61</strong></p></td>
<td>This option allows the author of a help frame to take away edit privileges previously assigned.</td>
</tr>
<tr class="even">
<td>XQHELP-DISPLAY</td>
<td><strong>Display/Edit Help Frames</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQH</strong></p></td>
<td>This option displays the text of a help frame, and allows for the edit of the name, header, text, or related frames.</td>
</tr>
<tr class="odd">
<td>XQHELPFIX</td>
<td><strong>Fix Help Frame File Pointers</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S %=0 D ENASK^XQ3</strong></p></td>
<td>This option scans through the HELP FRAME (#9.2) file for dangling <strong>POINTER</strong>s. It deletes keywords that point to help frames that no longer exist.</td>
</tr>
<tr class="even">
<td>XQHELP-LIST</td>
<td><strong>List Help Frames</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQH4</strong></p></td>
<td>This option lists the help frames, progressing through the tree. Several different formats are available.</td>
</tr>
<tr class="odd">
<td>XQHELP-MENU</td>
<td><strong>Help Processor</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu option contains several functions for entering help text, displaying it, and listing it. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XQHELP-DISPLAY</strong> (1)</p></li>
<li><p><strong>XQHELP-LIST</strong> (2)</p></li>
<li><p><strong>XQHELP-UPDATE</strong> (3)</p></li>
<li><p><strong>XQHELP-XREF</strong> (4)</p></li>
<li><p><strong>XQHELP-ASSIGN</strong> (5)</p></li>
<li><p><strong>XQHELP-DEASSIGN</strong> (6)</p></li>
<li><p><strong>XQHELPFIX</strong> (7)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQHELP-UPDATE</td>
<td><strong>New/Revised Help Frames</strong></td>
<td>Print</td>
<td></td>
<td>This option produces a VA FileMan listing of help frames sorted by DATE LAST UPDATED. It allows you to view any recently created or revised frames. You can also sort by package prefix.</td>
</tr>
<tr class="odd">
<td>XQHELP-XREF</td>
<td><strong>Cross Reference Help Frames</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQH3</strong></p></td>
<td>Lists all the help frames for a specified package, showing parent frames, linked to menu options, and invoked routines.</td>
</tr>
<tr class="even">
<td>XQKEYALTODEL</td>
<td><strong>Change user’s allocated keys to delegated keys</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ATOD^XQ6</strong></p></td>
<td><p>This option prompts for a user and uses <strong>%XY^%RCR</strong> to make all security keys the user holds delegated security keys, so that the user can give them to others.</p>
<p>This option is locked with the <strong>ADP</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XQKEYDEL</td>
<td><strong>Delegate keys</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN3^XQ6</strong></p></td>
<td><p>This option delegates security keys to a user, so that user can then give them out to other users. It also allows other users to delegate them in return.</p>
<p>This option is locked with the <strong>ADP</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XQKEYRDEL</td>
<td><strong>Remove delegated keys</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN4^XQ6</strong></p></td>
<td>This option removes security keys previously delegated to a user.</td>
</tr>
<tr class="odd">
<td>XQKICKMICRO</td>
<td><strong>Kick Off Micro Surgery</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHEK^XQ83</strong></p>
<p>Entry Action:</p>
<p><strong>W !!,?5,$S($D(^DIC(19,”AT”)):”Done.”,1:”Nothing to rebuild.”)</strong></p></td>
<td>When certain changes are made to the OPTION (#19) file those changes are recorded in the <strong>^DIC(19,“AT”)</strong> cross-reference. Micro surgery is the software in <strong>^XQ83*</strong> that uses this data to rebuild the compiled menu trees in <strong>^DIC(19,“AXQ”)</strong>. Micro surgery is normally triggered when a user logs into a system, but this option allows the programmer to start it manually if minor changes are made to the OPTION (#19) file, which do <em>not</em> merit a complete rebuild. If there is nothing in the “<strong>AT</strong>” cross-reference to work on, the option responds with: “Nothing to rebuild.” If there is work to do, then the option responds with: “<strong>Done</strong>,” which means that Micro surgery has been started.</td>
</tr>
<tr class="even">
<td>XQLISTKEY</td>
<td><strong>Show the keys of a particular user</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LIST^XQ6</strong></p></td>
<td>This option lists the security keys held by a particular user.</td>
</tr>
<tr class="odd">
<td>XQLOCK1</td>
<td><strong>All the Keys a User Needs</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XQLOCK</strong></p></td>
<td>This option invokes a routine that follows the menu trees of a user and collects all security keys into a list that are needed to effectively use a menu.</td>
</tr>
<tr class="even">
<td>XQLOCK2</td>
<td><strong>Keys For a Given Menu Tree</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XQLOCK</strong></p></td>
<td>This option runs a routine that searches the children of a given parent option and compiles a list of the security keys needed for that menu tree.</td>
</tr>
<tr class="odd">
<td>XQOOFF</td>
<td><strong>Mark Option Set Out-Of-Order</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OFFOP^XQOO1</strong></p></td>
<td>This option marks an option set Out-Of-Order.</td>
</tr>
<tr class="even">
<td>XQOOMAIN</td>
<td><strong>Out-Of-Order Set Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes the following options:</p>
<ul>
<li><p><strong>XQOOMAKE</strong></p></li>
<li><p><strong>XQOOFF</strong></p></li>
<li><p><strong>XQOON</strong></p></li>
<li><p><strong>XQOOSHOFIL</strong></p></li>
<li><p><strong>XQOOSHOW</strong></p></li>
<li><p><strong>XQOOSHOPRO</strong></p></li>
<li><p><strong>XQOOREDO</strong></p></li>
<li><p><strong>XQOOTOG</strong></p></li>
</ul>
<p>This option is locked with the <strong>ADP</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XQOOMAKE</td>
<td><strong>Create a Set of Options To Mark Out-Of-Order</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XQOO</strong></p></td>
<td>This option creates a set of options to mark Out-Of-Order.</td>
</tr>
<tr class="even">
<td>XQOON</td>
<td><strong>Remove Out-Of-Order Messages from a Set of Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ONOP^XQOO1</strong></p></td>
<td>This option removes Out-Of-Order messages from a set of options.</td>
</tr>
<tr class="odd">
<td>XQOOREDO</td>
<td><strong>Recover deleted option set</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REBLD^XQOO1</strong></p></td>
<td>This option recovers an option set that has been deleted from the <strong>^XTMP</strong> global by looping through the OPTION (#19) and PROTOCOL (#101) files to find all that have a particular Out-Of-Order message. It rebuilds the option set in the <strong>^XTMP</strong> global.</td>
</tr>
<tr class="even">
<td>XQOOSHOFIL</td>
<td><strong>Options in the Option File that are Out-Of-Order</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LALL^XQOO3</strong></p></td>
<td>This option presents a list of options in the OPTION (#19) file that are currently marked Out-Of-Order.</td>
</tr>
<tr class="odd">
<td>XQOOSHOPRO</td>
<td><strong>Protocols Marked Out-Of-Order in Protocol File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LAPR^XQOO3</strong></p></td>
<td>This option presents a list of protocols in the PROTOCOL (#101) file that are currently marked as Out-Of-Order.</td>
</tr>
<tr class="even">
<td>XQOOSHOW</td>
<td><strong>List Defined Option Sets</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XQOO2</strong></p></td>
<td>This option lists the option sets that have been created in <strong>^XUTL</strong> by their names.</td>
</tr>
<tr class="odd">
<td>XQOOTOG</td>
<td><strong>Toggle options/protocols on and off</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TOG^XQOO1</strong></p></td>
<td>This option writes or removes Out-Of-Order messages from individual options or protocols.</td>
</tr>
<tr class="even">
<td>XQOPACCESS</td>
<td><strong>See if a User Has Access to a Particular Option</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OPACCES^XQCHK</strong></p></td>
<td>This option prompts for an option name and the name of a user and then searches the user’s menu trees to see if the user has access to the option. It also checks to see if the user has the security key for a locked option.</td>
</tr>
<tr class="odd">
<td>XQOPED</td>
<td><strong>Screen-based Option Editor</strong></td>
<td>ScreenMan</td>
<td><p>Entry Action:</p>
<p><strong>D EA^XQOPED</strong></p>
<p>Exit Action:</p>
<p><strong>D XA^XQOPED</strong></p></td>
<td><p>This option runs the ScreenMan option editor form <strong>XQEDTOPT</strong>.</p>
<p>This option is locked with the <strong>ADP</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XQOPTFIX</td>
<td><strong>Fix Option File Pointers</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S %=1 D ENASK^XQ3</strong></p></td>
<td>This option scans through the OPTION (#19) file for dangling <strong>POINTER</strong>s. It deletes menu items that point to options that no longer exist.</td>
</tr>
<tr class="odd">
<td>XQORPHANOPTIONS</td>
<td><strong>Non-queuable options with no parents</strong></td>
<td>Menu</td>
<td></td>
<td>The options on this menu should <em>not</em> be assigned to a user’s menu. They are also <em>not</em> queueable, so they do <em>not</em> appear on the <strong>ZTQUEUABLE OPTIONS</strong> menu. They are collected on this menu, so that they are <em>not</em> accidentally deleted from the system.</td>
</tr>
<tr class="even">
<td>XQRESTRICT</td>
<td><strong>Restrict Availability of Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ9</strong></p></td>
<td><p>This option assigns various sorts of restrictions to options. The following fields can be set, for individual options or groups of options:</p>
<ul>
<li><p>LOCK</p></li>
<li><p>PROHIBITED TIMES</p></li>
<li><p>SPECIFY DEVICES</p></li>
<li><p>PRIORITY</p></li>
<li><p>OUT OF ORDER</p></li>
</ul>
<p>This option is locked with the <strong>ADP</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XQRIGHTNOW</td>
<td><strong>Is there a menu rebuild running right now?</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>NOW^XQ84</strong></p></td>
<td>This option checks the various flags set in <strong>^DIC(19,“AXQ”,“P0”)</strong> to determine if there is menu rebuild activity on your system right now.</td>
</tr>
<tr class="even">
<td>XQSCHK</td>
<td><strong>Server-type Option Test Server</strong></td>
<td>Server</td>
<td><p>Routine:</p>
<p><strong>XQSRV5</strong></p>
<p>Server Action: <strong>RUN IMMEDIATELY</strong></p></td>
<td>This server-type option tests other servers by examining the host OPTION (#19) file and returning the data associated with the target server. A message is sent to the host site with the name of the server option to be examined on the first line of the message.</td>
</tr>
<tr class="odd">
<td>XQSHOKEY</td>
<td><strong>List users holding a certain key</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SHOW^XQ6</strong></p></td>
<td>This option displays all the holders of a certain security key.</td>
</tr>
<tr class="even">
<td>XQSMD ADD</td>
<td><strong>Select Options to be Delegated</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQSMD</strong></p></td>
<td>This option delegates the management of a set of options (or remove options already delegated) to a particular user or set of users.</td>
</tr>
<tr class="odd">
<td>XQSMD BUILD MENU</td>
<td><strong>Build a New Menu</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BUILD^XQSMD4</strong></p></td>
<td>This option allows the delegated menu manager to build (create) new menus from the ones that are allowed.</td>
</tr>
<tr class="even">
<td>XQSMD BY OPTION</td>
<td><strong>List Delegated Options and their Users</strong></td>
<td>Print</td>
<td></td>
<td>This option prints the Secure Menu Delegation (SMD) options and the users that can delegate them.</td>
</tr>
<tr class="odd">
<td>XQSMD BY USER</td>
<td><strong>Print All Delegates and their Options</strong></td>
<td>Print</td>
<td></td>
<td>This option prints the users that have SMD and the options that they can delegate.</td>
</tr>
<tr class="even">
<td>XQSMD COPY USER</td>
<td><strong>Copy One Users Menus and Keys to others</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQSMDCPY</strong></p></td>
<td><p>This option copies the primary menu and secondary menu options from one user to one or more others. The only options transferred are those that have been delegated to the current user. Likewise, keys that are held by the selected user can be copied to the recipient users if the current user has been delegated this capacity as well.</p>
<p>This option provides an application coordinator the ability to produce users that have the capabilities of a current user (such as a ward clerk, scheduling clerk, and so on).</p></td>
</tr>
<tr class="odd">
<td>XQSMD EDIT OPTIONS</td>
<td><strong>Edit a User’s Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ENTRY^XQSMD5</strong></p></td>
<td>Allows user to edit primary and secondary user options.</td>
</tr>
<tr class="even">
<td>XQSMD LIMITED FM OPTIONS</td>
<td><strong>Limited File Manager Options (Build)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQSMDFM</strong></p></td>
<td><p>This option permits a user to build limited PRINT, EDIT, or INQUIRE options. The user <em>must</em> have one or more <strong>ALLOWABLE MENU PREFIX</strong> and the <strong>XQSMDFM</strong> security keys.</p>
<ul>
<li><p><strong>Edit Option</strong>—To build an edit option, the user <em>must</em> have an edit template to use.</p></li>
<li><p><strong>Print Option</strong>—To build a print option, the user <em>must</em> have both a SORT template and a PRINT template.</p></li>
<li><p><strong>Inquire Option</strong>—To build an inquire option the user can have a print template or can specify the file to use.</p></li>
</ul>
<p>The option is entered among the user’s delegated options, so that they can be included on a menu built under the Secure Menu Delegation or given to other users as secondary options. The name of the option is restricted to the namespace designated in the ALLOWABLE MENU PREFIX followed by a <strong>Z</strong> and then identifying text.</p></td>
</tr>
<tr class="odd">
<td>XQSMD MGR</td>
<td><strong>Secure Menu Delegation</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu manages the Secure Menu Delegation system. For those who are allowed to add and remove options from delegated sets of options. It includes the following options:</p>
<ul>
<li><p><strong>XQSMD ADD</strong></p></li>
<li><p><strong>XQSMD REMOVE</strong></p></li>
<li><p><strong>XQSMD BY OPTION</strong></p></li>
<li><p><strong>XQSMD BY USER</strong></p></li>
<li><p><strong>XQSMD USER MENU</strong></p></li>
<li><p><strong>XQSMD SHOW</strong></p></li>
<li><p><strong>XQSMD REPLICATE</strong></p></li>
<li><p><strong>XQSMD SET PREFIX</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQSMD REMOVE</td>
<td><strong>Remove Options Previously Delegated</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XQSMD</strong></p>
<p>Help Frame: <strong>XQSMD-OPTION</strong></p></td>
<td>Removes options from already established delegates.</td>
</tr>
<tr class="odd">
<td>XQSMD REPLICATE</td>
<td><strong>Replicate or Replace a Delegate</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQSMD3</strong></p>
<p>Help Frame: <strong>XQSMD-REPLICATE</strong></p></td>
<td>This option transfers the set of options delegated to a particular user to another user; optionally, allowing the original user’s delegated options to be removed.</td>
</tr>
<tr class="even">
<td>XQSMD SEC OFCR</td>
<td><strong>Secure Menu Delegation</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes Secure Menu Delegation options for reviewing the delegates and the options which they may delegate. It includes the following options:</p>
<ul>
<li><p><strong>XQSMD SHOW</strong></p></li>
<li><p><strong>XQSMD BY OPTION</strong></p></li>
<li><p><strong>XQSMD BY USER</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XQSMD SET PREFIX</td>
<td><strong>Specify Allowable New Menu Prefix</strong></td>
<td>Edit</td>
<td></td>
<td>Permits the user to give another user an Allowable New Menu Prefix for purposes of Secure Menu Delegation (SMD), so that the delegate can build new menus from the options that have been delegated.</td>
</tr>
<tr class="even">
<td>XQSMD SHOW</td>
<td><strong>Show a Delegate’s Options</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SHOW^XQSMD21</strong></p></td>
<td>This option shows you who created a delegate, when, and what delegation level they are; as well as all options delegated to that person, when each was delegated, and by whom.</td>
</tr>
<tr class="odd">
<td>XQSMD USER MENU</td>
<td><strong>Delegate’s Menu Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the Secure Menu Delegation (SMD) menu that is given to individuals who can modify other’s primary or secondary menus. It includes the following options:</p>
<ul>
<li><p><strong>XQSMD BUILD MENU</strong></p></li>
<li><p><strong>XQSMD EDIT OPTIONS</strong></p></li>
<li><p><strong>XQSMD LIMITED FM OPTIONS</strong></p></li>
<li><p><strong>XQSMD COPY USER</strong></p></li>
<li><p>XQCOPYOP</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XQSPING</td>
<td><strong>TCP/IP Type Ping Server</strong></td>
<td>Server</td>
<td><ul>
<li><p>Server Action: <strong>RUN IMMEDIATELY</strong></p></li>
<li><p>Server Audit: <strong>NO</strong></p></li>
<li><p>Suppress Bulletin: <strong>YES, SUPRESS IT</strong></p></li>
<li><p>Server Reply: <strong>REPLY ON ERROR ONLY</strong></p></li>
</ul></td>
<td>This is a PING server that works like PING under TCP/IP. If you send a message to this sever it sends it back to you, thereby showing that the network mail channel is open.</td>
</tr>
<tr class="odd">
<td>XQTKILL</td>
<td><strong>Delete a Menu Template</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>KILL^XQT4</strong></p></td>
<td>Removes a menu template from the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td>XQTLIST</td>
<td><strong>Show all options in a Menu Template</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LIST^XQT4</strong></p></td>
<td>List out all options in a particular menu template.</td>
</tr>
<tr class="odd">
<td>XQTNEW</td>
<td><strong>Create a new menu template</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQT2</strong></p></td>
<td>This option invokes a routine that walks the user through the menu trees creating a new menu template.</td>
</tr>
<tr class="even">
<td>XQTRNAM</td>
<td><strong>Rename a menu template</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RNAM^XQT4</strong></p></td>
<td>This option renames a particular menu template.</td>
</tr>
<tr class="odd">
<td>XQTSHO</td>
<td><strong>List all Menu Templates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SHO^XQT4</strong></p></td>
<td>This option lists all menu templates for the invoking user along with the first two options in that template.</td>
</tr>
<tr class="even">
<td>XQTUSER</td>
<td><strong>Menu Templates</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the user’s menu of menu template utilities. It includes the following options:</p>
<ul>
<li><p><strong>XQTSHO</strong></p></li>
<li><p><strong>XQTLIST</strong></p></li>
<li><p><strong>XQTKILL</strong></p></li>
<li><p><strong>XQTRNAM</strong></p></li>
<li><p><strong>XQTNEW</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU BLOCK COUNT</td>
<td><strong>Global Block Count</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTBKC</strong></p></td>
<td>This option counts the number of data blocks in a global.</td>
</tr>
<tr class="even">
<td>XU CHECKSUM LOAD</td>
<td><strong>Load/refresh checksum values into ROUTINE file</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LOAD^XUGOT</strong></p></td>
<td>This option updates the ROUTINE (#9.8) file with the latest checksum values from FORUM.</td>
</tr>
<tr class="odd">
<td>XU CHECKSUM REPORT</td>
<td><strong>Compare local/national checksums report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REPORT^XUGOT1</strong></p></td>
<td><p>This option compares checksums for routines to the values in the ROUTINE (#9.8) file. It provides a report listing routines that differ by patch or version, version or patch is correct, but checksums are off, local routines being tracked and information <em>not</em> on record for a patch (such as test patches).</p>
<p>Nationally released routines’ checksums are sent by Master File Updates to the local ROUTINE (#9.8) file automatically. Local sites may also record checksums in the CHECKSUM VALUE field in the ROUTINE (#9.8) file. To compare local routines which are being tracked, the CHECKSUM REPORT field should be set to “<strong>Local report</strong>”.</p></td>
</tr>
<tr class="even">
<td>XU DA EDIT</td>
<td><strong>DA Return Code Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUS11</strong></p></td>
<td>This option runs a routine to allow the setup and editing of the DA RETURNS CODE (#3.22) file.</td>
</tr>
<tr class="odd">
<td>XU EPCS</td>
<td><strong>User start-up event</strong></td>
<td>Extended Action</td>
<td></td>
<td><p>Released with Kernel Patch XU*8.0*580, this option is used exclusively during a VistA user signon event. Items listed in this option are “<strong>TYPE:action</strong>” options in the OPTION (#19) file that can be used to prompt users for input upon VistA signon and before their Primary menu option is displayed. It will <em>not</em> be used for GUI signons. It is called from <strong>XQ12</strong> routine.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/068.png) <strong>REF:</strong> For instructions on how to use this option, see Kernel Patch XU*8.0*593 and the <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>.</p></td>
</tr>
<tr class="even">
<td>XU EPCS DISUSER EXP DATE</td>
<td><strong>Print DISUSER DEA Expiration Date Null</strong></td>
<td>Print</td>
<td></td>
<td><p>Released with Kernel Patch XU*8.0*580, this option prints all <strong>DISUSER</strong>ed users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>TERMINATION DATE</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU EPCS DISUSER PRIVS</td>
<td><strong>Print DISUSER Prescribers with Privileges</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></td>
<td><p>Released with Kernel Patch XU*8.0*580, this option prints all <strong>DISUSER</strong>ed users who have privileges to any of the SCHEDULEs <strong>II</strong> through <strong>V</strong> and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>DEA#</p></li>
<li><p>TERMINATION DATE</p></li>
<li><p>VA#</p></li>
<li><p>SCHEDULESs</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU EPCS DISUSER XDATE EXPIRES</td>
<td><strong>Print DISUSER DEA Expiration Date Expires 30 days</strong></td>
<td>Print</td>
<td></td>
<td><p>This option prints all <strong>DISUSER</strong>ed users with a DEA# and where the DEA EXPIRATION DATE expires within <strong>30</strong> days. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/069.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS EDIT DATA</td>
<td><strong>ePCS Edit Prescriber Data</strong></td>
<td>Broker (Client/ Server)</td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></p>
<p>RPCs:</p>
<ul>
<li><p><strong>XU EPCS EDIT</strong></p></li>
<li><p><strong>XUS KEY CHECK</strong></p></li>
<li><p><strong>DDR DELETE ENTRY</strong></p></li>
<li><p><strong>DDR FILER</strong></p></li>
<li><p><strong>DDR FIND1</strong></p></li>
<li><p><strong>DDR FINDER</strong></p></li>
<li><p><strong>DDR GET DD HELP</strong></p></li>
<li><p><strong>DDR GETS ENTRY DATA</strong></p></li>
<li><p><strong>DDR KEY VALIDATOR</strong></p></li>
<li><p><strong>DDR LISTER</strong></p></li>
<li><p><strong>DDR LOCK/UNLOCK NODE</strong></p></li>
<li><p><strong>DDR VALIDATOR</strong></p></li>
<li><p><strong>XWB GET VARIABLE VALUE</strong></p></li>
<li><p><strong>XUS PKI SET UPN</strong></p></li>
<li><p><strong>XUS PKI GET UPN</strong></p></li>
</ul></td>
<td><p>This is a Broker-type context option that is given to those individuals who are permitted to edit the data related to e-prescribing of controlled substances. It includes the <strong>XQAL GUI ALERTS</strong> option.</p>
<p>This option is locked with the <strong>XUEPCSEDIT</strong> security key.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/070.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td>XU EPCS EDIT DEA# AND XDATE</td>
<td><strong>Edit Facility DEA# and Expiration Date</strong></td>
<td>Edit</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></td>
<td><p>This option edits the FACILITY DEA NUMBER (#52) and FACILITY DEA EXPIRATION DATE (#52.1) fields in the INSTITUTION (#4) file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/071.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS EXP DATE</td>
<td><strong>Print DEA Expiration Date Null</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765</strong></td>
<td><p>This option prints all active users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/072.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td>XU EPCS LOGICAL ACCESS</td>
<td><strong>Task Changes to DEA Prescribing Privileges Report</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765</strong></p>
<p>Routine:</p>
<p><strong>RPT1^XUEPCSRT</strong></p></td>
<td><p>This tasked option prints the setting or change to DEA prescribing privileges related to issuance of a controlled substance prescription.</p>
<p>This option only prints data from the previous day and with data that has been modified. The data is retrieved from the XUEPCS DATA (#8991.6) file.</p>
<p>This option should be scheduled to run daily.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/073.png) <strong>NOTE:</strong> No data is displayed to the screen; the data is printed to the device indicated by the <strong>XUEPCS REPORT DEVICE</strong> parameter.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/074.png) CAUTION: Verify that the XUEPCS REPORT DEVICE parameter has been set <em>before</em> using this option.<br />
<br />
To set the parameter, see the “Set the XUEPCS REPORT DEVICE Parameter” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf"><em>Kernel 8.0 Systems Management: Device Handler User Guide</em></a>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/075.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS PRINT EDIT AUDIT</td>
<td><strong>Print Audits for Prescriber Editing</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></p>
<p>Routine:</p>
<p><strong>PRINT^XUEPCSED</strong></p></td>
<td><p>This option prints information related to the editing of prescriber information.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/076.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td>XU EPCS PRIVS</td>
<td><strong>Print Prescribers with Privileges</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></td>
<td><p>This option prints all active users who have privileges to any of the SCHEDULEs <strong>II</strong> through <strong>V</strong> and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>DEA#</p></li>
<li><p>VA#</p></li>
<li><p>SCHEDULESs</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/077.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS PSDRPH</td>
<td><strong>Print PSDRPH Key Holders</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></td>
<td><p>This option prints all active users holding the <strong>PSDRPH</strong> security key. This report sorts by Division, and within DIVISION, it sorts by NAME. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p>GIVEN BY (Person Who Assigned Key)</p></li>
<li><p>DATE GIVEN (Date Assigned)</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/078.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td>XU EPCS PSDRPH AUDIT</td>
<td><strong>Task Allocation Audit of PSDRPH Key Report</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765</strong></p>
<p>Routine:</p>
<p><strong>RPT2^XUEPCSRT</strong></p></td>
<td><p>This tasked option prints the allocation of the <strong>PSDRPH</strong> security key.</p>
<p>This option only prints data from the previous day and with data that has been modified. The report prints data for the archive XUEPCS PSDRPH AUDIT (#8991.7) file.</p>
<p>This option should be scheduled to run daily.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/079.png) <strong>NOTE:</strong> No data is displayed to the screen; the data is printed to the device indicated by the <strong>XUEPCS REPORT DEVICE</strong> parameter.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/080.png) CAUTION: Verify that the XUEPCS REPORT DEVICE parameter has been set <em>before</em> using this option.<br />
<br />
To set the parameter, see the “Set the XUEPCS REPORT DEVICE Parameter” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf"><em>Kernel 8.0 Systems Management: Device Handler User Guide</em></a>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/081.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS PSDRPH KEY</td>
<td><strong>Allocate/De-Allocate of PSDRPH Key</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></p>
<p>Routine:</p>
<p><strong>PSDKEY^XUEPCSRT</strong></p></td>
<td><p>This option allows users to allocate or de-allocate the <strong>PSDRPH</strong> security key.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/082.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="even">
<td>XU EPCS SET PARMS</td>
<td><strong>Print Setting Parameters Privileges</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*689</strong></td>
<td><p>This option prints all active users holding the <strong>XUEPCSEDIT</strong> security key. This option identifies individuals responsible for setting the parameters.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/083.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU EPCS UTILITY FUNCTIONS</td>
<td><strong>ePCS DEA Utility Functions</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is DEA ePCS Utility main menu. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XU EPCS EXP DATE</strong><br />
(1; SYNONYM: 1)</p></li>
<li><p><strong>XU EPCS DISUSER EXP</strong> <strong>DATE</strong><br />
(2; SYNONYM: 2)</p></li>
<li><p><strong>XU EPCS XDATE EXPIRES</strong><br />
(3; SYNONYM: 3)</p></li>
<li><p><strong>XU EPCS DISUSER XDATE EXPIRES</strong><br />
(4; SYNONYM: 4)</p></li>
<li><p><strong>XU EPCS PRIVS</strong><br />
(5; SYNONYM: 5)</p></li>
<li><p><strong>XU EPCS DISUSER PRIVS</strong><br />
(6; SYNONYM: 6)</p></li>
<li><p><strong>XU EPCS PSDRPH</strong><br />
(7; SYNONYM: 7)</p></li>
<li><p><strong>XU EPCS SET PARMS</strong><br />
(8; SYNONYM: 8)</p></li>
<li><p><strong>XU EPCS PRINT EDIT AUDIT</strong><br />
(9; SYNONYM: 9)</p></li>
<li><p><strong>XU EPCS LOGICAL ACCESS</strong><br />
(10; SYNONYM: 10)</p></li>
<li><p><strong>XU EPCS PSDRPH AUDIT</strong><br />
(11; SYNONYM: 11)</p></li>
<li><p><strong>XU EPCS PSDRPH KEY</strong><br />
(12; SYNONYM: 12)</p></li>
<li><p><strong>XU EPCS EDIT DEA# AND XDATE</strong><br />
(13; SYNONYM: 13)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU EPCS XDATE EXPIRES</td>
<td><strong>Print DEA Expiration Date Expires 30 days</strong></td>
<td>Print</td>
<td>Out of Order Message: <strong>PLACED OUT OF ORDER BY XU*8*765</strong></td>
<td><p>This option prints all active users with a DEA# and where the DEA EXPIRATION DATE expires within <strong>30</strong> days. This option prints the following data:</p>
<ul>
<li><p>NAME</p></li>
<li><p>DEA#</p></li>
<li><p>DEA EXPIRATION DATE</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/084.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XU FINDUSER</td>
<td><strong>Find a user</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUS9</strong></p></td>
<td>This option finds a user that is currently signed on to the system in this UCI group. If the user is on this CPU, it also shows the menu path. It uses the “CUR” cross-reference on the SIGN-ON LOG (#3.081) file.</td>
</tr>
<tr class="even">
<td>XU FIRST LINE PRINT</td>
<td><strong>First Line Routine Print</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTP1</strong></p></td>
<td>This option uses the <strong>%ZTP1</strong> utility to print the first line of routines.</td>
</tr>
<tr class="odd">
<td>XU IP RELEASE</td>
<td><strong>Release IP lock</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>X6IP^XUSTZIP</strong></p></td>
<td>This option releases the lock on an IP address caused by too many invalid signon attempts.</td>
</tr>
<tr class="even">
<td>XU NOP MENU</td>
<td><strong>Do nothing menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu is just a placeholder for some special access methods.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/085.png) CAUTION: Do <em>not</em> place any new items in the menu multiple.</p></td>
</tr>
<tr class="odd">
<td>XU OPTION QUEUE</td>
<td><strong>One-time Option Queue</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMOPT</strong></p></td>
<td>This option allows any option that is in the OPTION (#19) file with the SCHEDULING RECOMMENDED field set to <strong>Yes</strong>, to be set up for one-time queuing.</td>
</tr>
<tr class="even">
<td>XU OPTION START</td>
<td><strong>One-time Option Start (Internal Use Only)</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>N XQY,XQY0 S XQY0=$G(^DIC(19,XUXQM,0)),XQT=$P(XQY0,U,4) I $L(XQT),”APR”[XQT S XQY=XUXQM D ZTSK2^XQ1 Q</strong></p></td>
<td><p>This option works with XU OPTION QUEUE (<strong>One-time Option Queue</strong>) to allow site managers to schedule an option that usually runs on a cycle without disrupting that cycle.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/086.png) This option should <em>not</em> be used directly, either from a menu or through the Schedule/Unschedule Options [XUTM SCHEDULE] option; it is used internally by XU OPTION QUEUE to make that option work correctly.</p></td>
</tr>
<tr class="odd">
<td>XU PROC CNT CLUP</td>
<td><strong>XUS Process count cleanup</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLEAR^XUSCNT(0)</strong></p></td>
<td>This option is only needed for GT.M sites. This is the Kernel process count cleanup routine. It checks the entries in <strong>XUTL(“XUSYS”,$J)</strong> to see if they are still active, and if <em>not</em>, removes the entry. For GT.M sites only, schedule this option to run between every <strong>1</strong> to <strong>8</strong> hours.</td>
</tr>
<tr class="even">
<td>XU SEC OFCR</td>
<td><strong>Menu and Option Security</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes options to allow the user to review options. It includes the following options:</p>
<ul>
<li><p><strong>XUINQUIRE</strong></p></li>
<li><p><strong>XUOPTWHO</strong></p></li>
<li><p><strong>XUPRINT</strong></p></li>
<li><p><strong>XUUSERACC</strong></p></li>
<li><p><strong>XUUSERACC2</strong></p></li>
<li><p><strong>XUXREF-2</strong></p></li>
<li><p><strong>XQSHOKEY</strong></p></li>
<li><p><strong>XQLOCK2</strong></p></li>
<li><p><strong>XQSMD SEC OFCR</strong></p></li>
<li><p><strong>XUOPTDISP</strong></p></li>
<li><p><strong>XUOPTLOG</strong></p></li>
<li><p><strong>XUOPTPURGE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU SID ASK</td>
<td><strong>Ask if Production Account</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ASK^XUPROD</strong></p></td>
<td><p>This option allows the user to claim that the current account is the Production account and set the SID into the KERNEL SYSTEM PARAMETERS (#8989.3) file.</p>
<p>This option is locked with the <strong>XUMGR</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XU SID EDIT</td>
<td><strong>Edit Logical/Physical Mapping</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EDIT^XUPROD</strong></p></td>
<td>This option lets you edit the two fields that are used in the SID code to map a logical name in the Cache <strong>cpf</strong> file to the Physical name that is returned by a <strong>$ZU(12,”“)</strong> call.</td>
</tr>
<tr class="odd">
<td>XU SID STARTUP</td>
<td><strong>Startup PROD check</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHECK^XUPROD</strong></p></td>
<td>This option should run at every startup to check if the current SID matches the stored SID. To do this, the option needs to be in the OPTION SCHEDULING (#19.2) file with the SPECIAL QUEUEING field set to Startup Persistent.</td>
</tr>
<tr class="even">
<td>XU SITE LOCKOUT</td>
<td><strong>Edit Site IP lockout</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>N DA,DR,DIE S DA=1,DR=“[XUSITEIP]”,DIE=8989.3 D XUDIE^XUS5</strong></p></td>
<td>This option edits the KERNEL SYSTEM PARAMETERS (#8989.3) file for IP lockout, User lockout, and Terminal server list entry.</td>
</tr>
<tr class="odd">
<td>XU SWITCH UCI</td>
<td><strong>Switch UCI</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SWITCH^XUS3A</strong></p></td>
<td>This option switches UCIs.</td>
</tr>
<tr class="even">
<td>XU USER ADD</td>
<td><strong>New User Event</strong></td>
<td>Extended Action</td>
<td><p>Entry Action:</p>
<p><strong>D GET^XUSERP(XUIEN,.XUSR)</strong></p></td>
<td><p>This is a protocol to link other software applications that want to know about a USER ADD event. Other packages can attach to this protocol option, and they are called when a new USER is Added. At the end of editing, the user data XU USER CHANGE protocol is called. <strong>DUZ</strong> is the person that is running the add user option. XUIFN points to the NEW PERSON (#200) file entry that has been added. It returns selected File #200 data to XUSR(field name) array for NEW PERSON components. It is called from <strong>XUSERNEW</strong> by <strong>XUSERP</strong>. It includes the following option:</p>
<ul>
<li><p><strong>PSB BCBU PMU MESSAGE BUILDER</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU USER CHANGE</td>
<td><strong>User Change Event</strong></td>
<td>Extended Action</td>
<td><p>Entry Action:</p>
<p><strong>D GET^XUSERP(XUIEN,.XUSR)</strong></p></td>
<td><p>This is a protocol to link other software applications that want to know about a USER CHANGE event. Other packages can attach to this protocol option, and they are called when a user is Edited. <strong>DUZ</strong> is the person that is running the edit user option. <strong>XUIFN</strong> points to the NEW PERSON (#200) file entry that has been changed. It returns selected File #200 data to XUSR(field name) array for NEW PERSON components. It includes the following option:</p>
<ul>
<li><p><strong>PSB BCBU PMU MESSAGE BUILDER</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU USER SIGN-ON</td>
<td><strong>User sign-on event</strong></td>
<td>Extended Action</td>
<td></td>
<td><p>This is a protocol option to link other software applications that want to know about a user signon event. The protocols <em>must</em> <em>not</em> <strong>READ/WRITE</strong> to the screen, because it may be doing a GUI signon. They can set text that is displayed to the user by calling <strong>SET^XUS1A(string)</strong>. The first character should be a <strong>!</strong> to cause the text to be placed on a new line. <strong>DUZ</strong> is defined but other variables may <em>not</em> be. It is called from <strong>XUS1A</strong>. It includes the following options:</p>
<ul>
<li><p><strong>PRSAZ SUP ALERTS</strong></p></li>
<li><p><strong>RA SIGN-ON MSG</strong></p></li>
<li><p><strong>VAFC EXCEPTION NOTIFIER</strong></p></li>
<li><p><strong>RG EXCEPTION NOTIFIER</strong></p></li>
<li><p><strong>ASL ESIG ACCESS AGREEMENT</strong></p></li>
<li><p><strong>ADR PURCHASE CARD ACTIONS</strong></p></li>
<li><p><strong>AEA CMR TURN IN ALERT</strong></p></li>
<li><p><strong>AEA PPM TURN IN ALERT</strong></p></li>
<li><p><strong>AEA WHSE TURN IN ALERT</strong></p></li>
<li><p><strong>ENIT RESP NOTIFY</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU USER START-UP</td>
<td><strong>User start-up event</strong></td>
<td>Extended Action</td>
<td><p>Routine:</p>
<p><strong>XQ12</strong></p></td>
<td><p>This is a protocol option that is used exclusively during a VistA user signon event. Items attached to this option are “<strong>TYPE:action</strong>” options in the OPTION (#19) file, which can be used to prompt users for input upon VistA signon and before their Primary menu option is displayed. Unlike the XU USER SIGN-ON option, it can provide interactive prompting to users. It is <em>not</em> used for GUI signon.</p>
<p>For example, The KEEP FROM DELETING (#209.2) field has been set to <strong>Yes</strong> on the <strong>User start-up event</strong> [XU USER START-UP] option.</p>
<p>This option is called from the <strong>XQ12</strong> routine.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/087.png) <strong>NOTE:</strong> This option was released with Kernel Patch XU*8.0*593.</p></td>
</tr>
<tr class="even">
<td><span id="XU_USER_TERMINATE_Option" class="anchor"></span>XU USER TERMINATE</td>
<td><strong>User terminate event</strong></td>
<td>Extended Action</td>
<td><p>Entry Action:</p>
<p><strong>D GET^XUSERP(XUIEN,.XUSR)</strong></p></td>
<td><p>This is a protocol to link other software applications that want to know about a USER TERMINATE event. Other applications can attach to this protocol option, and they will be called when a USER is terminated. The call is just after the user’s Access and Verify Codes have been removed. <strong>DUZ</strong> is the person that is running the terminate option. <strong>XUIFN</strong> points to the NEW PERSON (#200) file entry that is being terminated. It returns selected File #200 data to XUSR(field name) array for NEW PERSON components. It is called in XUSTERM from XUSERP. It includes the following options:</p>
<ul>
<li><p><strong>USR USER TERMINATE</strong></p></li>
<li><p><strong>GMRC TERMINATE CLEANUP</strong></p></li>
<li><p><strong>OR TERMINATE CLEANUP</strong></p></li>
<li><p><strong>PRCS TERMINATE</strong></p></li>
<li><p><strong>AEA XU TERMINATE REMOTE</strong></p></li>
<li><p><strong>TIU TEMPLATE USER DELETE</strong></p></li>
<li><p><strong>PSB BCBU PMU MESSAGE BUILDER</strong></p></li>
<li><p><strong>ENIT USER ACCOUNT TERMINATED</strong></p></li>
</ul>
<p>While unit testing the <strong>XUS IAM USER TERMINATE</strong> with Kernel Patch XU*8.0*799, it was determined that if the “Purge Flag”, which was released in patch XU*8.0*645, is <em>not</em> set that the subscribers to the <strong>XU USER TERMINATE</strong> Protocol event were <em>not</em> being notified that users were terminated. After some analysis, it was determined that this was an oversight when it was implemented. Therefore, Kernel Patch XU*8.0*799 implemented a minor code change in the <strong>XUSTERM</strong> routine, so that if the “Purge Flag” is <em>not</em> set that any subscribers to the <strong>XU USER TERMINATE</strong> protocol event will still be notified when a user with a future termination date has been terminated.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/088.png) <strong>NOTE:</strong> If the “Purge Flag” is set at the site then subscribers were already being notified of the terminations. This subscriber notification issue would only be encountered when the “<strong>PURGE</strong>” flag was <em>not</em> set at the site.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/089.png) <strong>NOTE:</strong> During Initial Operating Capability (IOC) testing of Kernel Patch XU*8.0*799, it was discovered that if the site is using the <strong>ENGINEERING IT EQUIPMENT MODULE</strong> for tracking user equipment, an increase in daily MailMan messages generated may occur if the user has active equipment assignments, since the subscribers to the <strong>XU USER TERMINATE</strong> protocol event are being notified of termination events regardless of the “<strong>PURGE</strong>” flag setting.</p></td>
</tr>
<tr class="odd">
<td>XU-486 MENU COPY</td>
<td><strong>Copy the compiled menus from the print server</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S SYS=“CS” F S SYS=$O(^%ZIS(14.5,”B”,SYS)) Q:SYS’[“CS” S UCI=“VAH”,%X=“^XUTL(““XQO”“,”,%Y=“^[UCI,SYS]XUTL(““XQO”“,”,%=$E(%Y,1,$L(%Y)-1)_”)” X “K @% D %XY^%RCR”</strong></p></td>
<td><p>(Obsolete) This option is just for the MSM 486 site that run TaskMan only on the print server and need to get updated compiled menus to the Compute servers.</p>
<p>It should be scheduled to run after the menu tree rebuild has finished on the print server. As distributed, it only copies the compiled menus to a UCI named <strong>VAH</strong> on compute servers named <strong>CSA,CSB,…</strong> It uses <strong>%RCR</strong> to copy the data.</p></td>
</tr>
<tr class="even">
<td>XUADISP</td>
<td><strong>Audit Display</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the <strong>Audit Display</strong> menu. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUOPTDISP</strong> (1)</p></li>
<li><p><strong>XUUSEROPT</strong> (2)</p></li>
<li><p><strong>XUFDEV</strong> (3)</p></li>
<li><p><strong>XUFDISP</strong> (4)</p></li>
<li><p><strong>XUPMDISP</strong> (5)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUAUDIT</td>
<td><strong>Establish System Audit Parameters</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S DA=1,DIE=“^XTV(8989.3,”,DR=“[XUAUDIT]” D XUDIE^XUS5 K DA,DIE,DR</strong></p></td>
<td>This option establishes the audit parameters for which option, namespace, user, device, and failed access attempt to audit. Includes date to initiate and terminate this audit function.</td>
</tr>
<tr class="even">
<td>XUAUDIT MAINT</td>
<td><strong>System Audit Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu establishes and maintains audit functions. It includes the following options (listed in display order; no #5):</p>
<ul>
<li><p><strong>XUAUDIT</strong> (1)</p></li>
<li><p><strong>XU-SPY-SHOW</strong> (2)</p></li>
<li><p><strong>XUSERVDISP</strong> (3)</p></li>
<li><p><strong>XM SUPER SEARCH</strong> (4)</p></li>
<li><p><strong>DG BULLETIN LOCAL</strong> (6)</p></li>
<li><p><strong>DG PATIENT INQUIRY</strong> (7)</p></li>
<li><p><strong>DG PARAMETER ENTRY</strong> (8)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUAUDIT MENU</td>
<td><strong>Audit Features</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes options to establish Kernel Audit Parameters and to print/display audit data. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUAUDIT MAINT</strong> (1)</p></li>
<li><p><strong>XUAUDIT RPT</strong> (2)</p></li>
<li><p><strong>XUADISP</strong> (3)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUAUDIT RPT</td>
<td><strong>System Audit Reports</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is a menu of reports pertaining to the audit of options, users, and the system. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUFAIL</strong> (1)</p></li>
<li><p><strong>XUOPTLOG</strong> (2)</p></li>
<li><p><strong>XUSC LIST</strong> (3)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUAUTODEACTIVATE</td>
<td><strong>Automatic Deactivation of Users</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHECK^XUSTERM1</strong></p></td>
<td><p>This option goes through the NEW PERSON (#200) file, and searches for users with a termination date in the past who still have an Access Code. It deletes their Access Code and security keys. It calls the <strong>XU USER TERMINATE</strong> protocol in the OPTION (#19) file, so other applications can take any action needed. If the DELETE ALL MAIL ACCESS field is set, then the user is removed from the MailMan system. This deletes their mail boxes and deletes them from any mail groups.</p>
<p>Patch XU*8*514 implements the Logical Access Controls section of VA Handbook 6500. Item <strong>d</strong> states that accounts are automatically disabled if inactive for <strong>30</strong> days.</p>
<p>The routine checks for users that have an Access Code and a LAST SIGNON DATE (#202) where the LAST SIGNON DATE is more than <strong>30</strong> days old and sets the DISUSER (#7) field flag for the user. If the site has set the ACADEMIC AFFILIATION WAIVER (#13) field to <strong>YES</strong> in the KERNEL SYSTEM PARAMETERS (#8989.3) file, then a <strong>90</strong>-day limit is used in place of <strong>30</strong> days.</p></td>
</tr>
<tr class="even">
<td>XUCHANGE</td>
<td><strong>Change Device’s Terminal Type</strong></td>
<td>Edit</td>
<td></td>
<td>This option changes the TERMINAL TYPE associated with a given device.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL ACTIVE TRAINEE</td>
<td><strong>List of Active Registered Trainees</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a report of active Registered Trainees. The SCHEDULING RECOMMENDED (#209) field has been set to <strong>YES</strong> in case the site decides they want to schedule this report at regular intervals. When manually launching this report, it is recommended that it be QUEUED.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL INACTIVE TRAINEE</td>
<td><strong>List of Inactive Registered Trainees</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a report of inactive Registered Trainees. The SCHEDULING RECOMMENDED (#209) field has been set to <strong>YES</strong> in case the site decides they want to schedule this report at regular intervals. When manually launching this report, it is recommended that it be QUEUED.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL LOCAL REPORTS</td>
<td><strong>Local Trainee Registration Reports</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu option provides various Trainee Registration reports that look at the local database. It includes the following options:</p>
<ul>
<li><p><strong>XU-CLINICAL TRAINEE DB COUNT</strong></p></li>
<li><p><strong>XU-CLINICAL ACTIVE TRAINEE</strong></p></li>
<li><p><strong>XU-CLINICAL INACTIVE TRAINEE</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE LIST</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE COUNT</td>
<td><strong>Count of Clinical Trainee’s</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a reports of the total number of Clinical Trainee’s that have been entered into the NEW PERSON (#200) file.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE DB COUNT</td>
<td><strong>Total Count of Registered Trainees</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a report of the total number of Clinical Trainee’s that have been entered into the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE EDIT DB COUNT</td>
<td><strong>Edit Trainee Registration Data</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S DIC=“^VA(200,”,DIC(0)=“AEMQ”,DIC(“S”)=“I $S($P(^(0),U,11):$P(^(0),U,11)’&lt;$$FMADD^XLFDT(DT,”“-1096”“),1:1)” D ^DIC K DIC Q:Y=-1 S DA=+Y,DR=“[XU-CLINICAL TRAINEE]”,DIE=“^VA(200,” D XUDIE^XUS5 K D0,DA,DIE,DR</strong></p></td>
<td>This option edits the Registered Trainee data.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE INQUIRY</td>
<td><strong>Trainee Registration Inquiry</strong></td>
<td>Inquire</td>
<td></td>
<td>This option displays various attributes of Registered Trainees.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE LIST</td>
<td><strong>List of All Registered Trainees</strong></td>
<td>Print</td>
<td></td>
<td>This option reports both active and inactive Registered Trainees. The SCHEDULING RECOMMENDED (#209) field has been set to <strong>YES</strong> in case the site decides they want to schedule this report at regular intervals. When manually launching this report, it is <em>recommended</em> that it be QUEUED.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE MENU</td>
<td><strong>OAA Trainee Registration Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the primary menu for managing Trainee Registration. It includes the following options:</p>
<ul>
<li><p><strong>XU-CLINICAL TRAINEE EDIT</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE INQUIRY</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE REPORTS</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE REPORTS</td>
<td><strong>Trainee Reports Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the Trainee Registration main reports menu. It includes the following options:</p>
<ul>
<li><p><strong>XU-CLINICAL LOCAL REPORTS</strong></p></li>
<li><p><strong>XU-CLINICAL TRANS REPORTS</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE TRANSA</td>
<td><strong>Trainee Transmission Report by Date</strong></td>
<td>Print</td>
<td></td>
<td>This option produces a report of transmitted trainees by date transmitted to the OAA.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRAINEE TRANSB</td>
<td><strong>Trainee Transmission Report Selectable Items</strong></td>
<td>Print</td>
<td></td>
<td>This option selects a range for date transmitted and a range for the VHA training facility.</td>
</tr>
<tr class="odd">
<td>XU-CLINICAL TRAINEE TRANSC</td>
<td><strong>Trainee Transmission Report by Range</strong></td>
<td>Print</td>
<td></td>
<td>This report displays/prints the Registered Trainee transmission counts for a selected time-period.</td>
</tr>
<tr class="even">
<td>XU-CLINICAL TRANS REPORTS</td>
<td><strong>Trainee Transmission Reports to OAA</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the menu for the Various Trainee Registration transmission reports to the OAA. It includes the following options:</p>
<ul>
<li><p><strong>XU-CLINICAL TRAINEE TRANSA</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE TRANSB</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE TRANSC</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUCOMMAND</td>
<td><strong>SYSTEM COMMAND OPTIONS</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the basic command menu that holds commands executable from anywhere in the menu processor. It includes the following options:</p>
<ul>
<li><p><strong>XUHALT</strong></p></li>
<li><p><strong>XUTIME</strong></p></li>
<li><p><strong>XUCONTINUE</strong></p></li>
<li><p><strong>XURELOG</strong></p></li>
<li><p><strong>XMUSER</strong></p></li>
<li><p><strong>XUSERTOOLS</strong><br />
(SYNONYM: TBOX)</p></li>
<li><p><strong>XQALERT</strong><br />
(SYNONYM: VA)</p></li>
<li><p><strong>ENWOWARD</strong><br />
(SYNONYM: WOR)</p></li>
<li><p><strong>PRSA EMP MENU</strong><br />
(SYNONYM: LEAV)</p></li>
<li><p><strong>ZPBOOK</strong><br />
(SYNONYM: PB)</p></li>
<li><p><strong>ZPSOMD DRUG LOOK-UP</strong><br />
(SYNONYM: FORM)</p></li>
<li><p><strong>452 VA STATION INQ</strong><br />
(SYNONYM: PB)</p></li>
<li><p><strong>RTZ USER MENU</strong><br />
(SYNONYM: RTZ)</p></li>
<li><p><strong>OOPS GUI EMPLOYEE</strong></p></li>
<li><p><strong>XUS SIGNON</strong></p></li>
<li><p><strong>XUS KAAJEE WEB LOGON</strong></p></li>
<li><p><strong>XOBE ESIG USER</strong></p></li>
<li><p><strong>ENIT OWNER MENU</strong><br />
(SYNONYM: IT O)</p></li>
<li><p><strong>EC GUI CONTEXT</strong></p></li>
<li><p><strong>VEJDWPB CORE RPCS</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUCONTINUE</td>
<td><strong>Continue</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XQUR=“CON”,^(“T”)=^XUTL(“XQ”,$J,”T”)-1 G CON^XQ12</strong></p></td>
<td>This option halts processing, allowing for the user to directly proceed to the last option accessed on the next login.</td>
</tr>
<tr class="odd">
<td>XUCORE</td>
<td><strong>Core Applications</strong></td>
<td>Menu</td>
<td><p>Entry Action:</p>
<p><strong>D ^ASTR2,XM^ABOC</strong></p></td>
<td><p>This menu branches to each of the CORE application packages. It includes the following options:</p>
<ul>
<li><p><strong>PSMENU</strong><br />
(DISPLAY ORDER: 10)</p></li>
<li><p><strong>DIUSER</strong><br />
(SYNONYM: FM<br />
DISPLAY ORDER: 17)</p></li>
<li><p><strong>MRMENU</strong><br />
(DISPLAY ORDER: 7)</p></li>
<li><p><strong>FHMGR</strong><br />
(DISPLAY ORDER: 2)</p></li>
<li><p><strong>YSUSER</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>RADIOLOGY SYSTEM</strong><br />
(DISPLAY ORDER: 13)</p></li>
<li><p><strong>CRMGR</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>LRZMENU</strong><br />
(DISPLAY ORDER: 4)</p></li>
<li><p><strong>VOLMENU</strong><br />
(DISPLAY ORDER: 18)</p></li>
<li><p><strong>SOWK</strong><br />
(DISPLAY ORDER: 15)</p></li>
<li><p><strong>DGZMGR</strong><br />
(SYNONYM: PIMS<br />
DISPLAY ORDER: 5)</p></li>
<li><p><strong>FHDMP</strong><br />
(DISPLAY ORDER: 9)</p></li>
<li><p><strong>NURS-SYS-MGR</strong><br />
(SYNONYM: NS)</p></li>
<li><p><strong>ENMGR</strong><br />
(SYNONYM: EN)</p></li>
<li><p><strong>ABSV VAVS MASTER MENU</strong><br />
(SYNONYM: VOL)</p></li>
<li><p><strong>HL MAIN MENU</strong><br />
(SYNONYM: HL7)</p></li>
<li><p><strong>MAG WINDOWS</strong></p></li>
<li><p><strong>RDP1 UTIL MENU</strong><br />
(SYNONYM: RDP)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUDEV</td>
<td><strong>Device Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option changes the device characteristics for a given device.</td>
</tr>
<tr class="odd">
<td>XUDEV LINEPORT ADDR CURRENT</td>
<td><strong>Current Line/Port Address</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W !,”Your current Line/Port address is “_$$LNPRTNAM^%ZISUTL</strong></p></td>
<td>This option identifies your current Line/Port address.</td>
</tr>
<tr class="even">
<td>XUDEV LINEPORT ADDR EDIT</td>
<td><strong>Edit Line/Port Addresses</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the Line/Port addresses.</td>
</tr>
<tr class="odd">
<td>XUDEV LINEPORT ADDR RPT</td>
<td><strong>Line/Port Address report</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a report listing Line/Port Addresses.</td>
</tr>
<tr class="even">
<td>XUDEV RES-CLEAR</td>
<td><strong>Clear all resources</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RELALL^XUDHRES</strong></p></td>
<td><p>This option loops through all entries in the RESOURCE (#3.54) file and removes any slot in use entries.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/090.png) CAUTION: This option should only be used as a TaskMan Startup option or by a knowledgeable site person.</p></td>
</tr>
<tr class="odd">
<td>XUDEV RES-ONE</td>
<td><strong>Clear one Resource</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RELONE^XUDHRES</strong></p></td>
<td>This option clears/resets one entry of one resource. System administrators use this option to clear problems.</td>
</tr>
<tr class="even">
<td>XUDEVEDIT</td>
<td><strong>Edit Devices by Specific Types</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu edits specific types of devices using ScreenMan or edits all device fields. It includes the following options:</p>
<ul>
<li><p><strong>XUDEVEDITSPL</strong><br />
(SYNONYM: SPL)</p></li>
<li><p><strong>XUDEVEDITHFS</strong><br />
(SYNONYM: HFS)</p></li>
<li><p><strong>XUDEVEDITRES</strong><br />
(SYNONYM: RES)</p></li>
<li><p><strong>XUDEVEDITTRM</strong><br />
(SYNONYM: TRM)</p></li>
<li><p><strong>XUDEVEDITALL</strong><br />
(SYNONYM: ALL)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUDEVEDITALL</td>
<td><strong>Edit All Device Fields</strong></td>
<td>Edit</td>
<td></td>
<td>This option will allow the editing of all the fields in the DEVICE (#3.5) file.</td>
</tr>
<tr class="even">
<td>XUDEVEDITCHAN</td>
<td><strong>Network Channel Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHAN^ZISEDIT</strong></p></td>
<td>This is a ScreenMan-oriented edit option for editing synchronous devices.</td>
</tr>
<tr class="odd">
<td>XUDEVEDITHFS</td>
<td><strong>Host File Server Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>HFS^ZISEDIT</strong></p></td>
<td>This is a ScreenMan-oriented edit option for editing Host file devices.</td>
</tr>
<tr class="even">
<td>XUDEVEDITLPD</td>
<td><strong>LPD/VMS Device Edit</strong></td>
<td>ScreenMan</td>
<td></td>
<td>This option calls a ScreenMan form to edit a VMS LPD device.</td>
</tr>
<tr class="odd">
<td>XUDEVEDITMT</td>
<td><strong>Magtape Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>MT^ZISEDIT</strong></p></td>
<td>This is a ScreenMan oriented edit option for editing magtape devices.</td>
</tr>
<tr class="even">
<td>XUDEVEDITRES</td>
<td><strong>Resource Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RES^ZISEDIT</strong></p></td>
<td>This is a ScreenMan-oriented edit option for editing resource devices.</td>
</tr>
<tr class="odd">
<td>XUDEVEDITSPL</td>
<td><strong>Spool Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SPL^ZISEDIT</strong></p></td>
<td>This is a ScreenMan-oriented edit option for editing spool devices.</td>
</tr>
<tr class="even">
<td>XUDEVEDITSYNC</td>
<td><strong>Network Channel Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHAN^ZISEDIT</strong></p></td>
<td>This is a ScreenMan oriented edit option for editing synchronous devices.</td>
</tr>
<tr class="odd">
<td>XUDEVEDITTRM</td>
<td><strong>TRM or VTRM Device Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TRM^ZISEDIT</strong></p></td>
<td>This option calls a ScreenMan form to edit a <strong>TRM</strong> or <strong>VTRM</strong> device.</td>
</tr>
<tr class="even">
<td>XUDIACCESS FOR ISO</td>
<td><strong>Fileman Access for the ISO</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains VA FileMan options. VA FileMan access is basically required until such time as all necessary reports can be generated by standardized menu options. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>DIPRINT</strong> (1)</p></li>
<li><p><strong>DISEARCH</strong> (2)</p></li>
<li><p><strong>DIINQUIRE</strong> (3)</p></li>
<li><p><strong>DIAUDIT</strong> (4)</p></li>
<li><p><strong>DILIST</strong> (5)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUDISPLAY</td>
<td><strong>Display Device Data</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a list of all the devices in the DEVICE file.</td>
</tr>
<tr class="even">
<td>XUEDITOPT</td>
<td>Edit options</td>
<td>Edit</td>
<td><p>Entry Action:</p>
<p><strong>S DLAYGO=19</strong></p>
<p>Exit Action:</p>
<p><strong>K DLAYGO D KICK^XQ7</strong></p></td>
<td>This option creates the building blocks of the menu system. Each option should have an internal name, menu text, a description, and a type. Depending on its type, other fields are filled in.</td>
</tr>
<tr class="odd">
<td>XUER EDIT PARAMS</td>
<td><strong>Error Trap Param Edit</strong></td>
<td>ScreenMan</td>
<td></td>
<td>This option allows the editing of Error Trap parameters in the KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
</tr>
<tr class="even">
<td>XUER NOTE</td>
<td><strong>Annotate an Error</strong></td>
<td>Edit</td>
<td></td>
<td>This option provides a means of letting a programmer annotate an error that has been logged automatically.</td>
</tr>
<tr class="odd">
<td>XUER PURGE ERROR SUMMARY</td>
<td><strong>Purge Error Trap Summary</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PURGE^XTERSUM1</strong></p></td>
<td>This option should be scheduled weekly or monthly to purge the error summary of old errors. It only purges entries where the last error was over <strong>90</strong> days ago.</td>
</tr>
<tr class="even">
<td>XUER SUMMARY</td>
<td><strong>Error Summary Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu holds the Error Summary options. It includes the following options:</p>
<ul>
<li><p><strong>XUER SUMMARY MOST RECENT</strong></p></li>
<li><p><strong>XUER NOTE</strong></p></li>
<li><p><strong>XUER PURGE ERROR SUMMARY</strong></p></li>
<li><p><strong>XUER UPDATE DEMAND/BATCH</strong></p></li>
<li><p><strong>XUER SUMMARY INQUIRE</strong></p></li>
<li><p><strong>XUER SUMMARY TOP</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUER SUMMARY INQUIRE</td>
<td><strong>Inquire Error Summary</strong></td>
<td>Inquire</td>
<td></td>
<td>This option inquires into the ERROR TRAP SUMMARY (#3.077) file.</td>
</tr>
<tr class="even">
<td>XUER SUMMARY MOST RECENT</td>
<td><strong>Summary Most Recent Errors</strong></td>
<td>Print</td>
<td></td>
<td>This option displays the most recent errors in the ERROR TRAP SUMMARY (#3.077) file.</td>
</tr>
<tr class="odd">
<td>XUER SUMMARY TOP</td>
<td><strong>Top Errors</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SHOW^XTERSUM4</strong></p></td>
<td>This option runs a report of the top errors and prints a graph of when they occurred.</td>
</tr>
<tr class="even">
<td>XUER UPDATE DEMAND/BATCH</td>
<td><strong>Update Error Trap Summary</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TODAY^XTERSUM</strong></p></td>
<td>This option is run on demand or by batch to update the ERROR TRAP SUMMARY (#3.077) file from the current Error Trap. This only processes the errors for the current day.<br />
<strong>DO ADD^XTERSUM</strong> to add error from the last <strong>30</strong> days. See the code to reach back even further.</td>
</tr>
<tr class="odd">
<td>XUERRS</td>
<td><strong>Error Processing</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides access to options pertaining to the Error Trap: displaying, printing, and purging errors. It includes the following options:</p>
<ul>
<li><p><strong>XUERTRAP</strong></p></li>
<li><p><strong>XUERTRP PRINT ERRS</strong></p></li>
<li><p><strong>XUERTRP PRINT T-1 1 ERR</strong><br />
(SYNONYM: P1)</p></li>
<li><p><strong>XUERTRP PRINT T-1 2 ERR</strong><br />
(SYNONYM: P2)</p></li>
<li><p><strong>XUERTRP CLEAN</strong></p></li>
<li><p><strong>XUERTRP TYPE</strong></p></li>
<li><p><strong>XUER SUMMARY</strong><br />
(SYNONYM: SUM)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUERTRAP</td>
<td><strong>Error Trap Display</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTER</strong></p></td>
<td>This option displays programmer error messages (operating-system dependent).</td>
</tr>
<tr class="odd">
<td>XUERTRP AUTO CLEAN</td>
<td><strong>Error trap Auto clean</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>AUTO^XTERPUR</strong></p></td>
<td>This is a queueable option to clean up the Error Trap. By default, this option cleans up any errors that were recorded more than <strong>7</strong> days ago. If in the <strong>TaskMan Schedule/Unschedule Options</strong> [XUTM SCHEDULE] option, the TASK PARAMETERS field has another <strong>NUMERIC</strong> value that is used instead.</td>
</tr>
<tr class="even">
<td>XUERTRP CLEAN</td>
<td><strong>Clean Error Trap</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTERPUR</strong></p></td>
<td><p>This option is available to delete old errors from the Error Trap.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUERTRP PRINT ERRS</td>
<td><strong>Interactive Print of Error Messages</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>INTRACT^XTER1A</strong></p></td>
<td>This option provides an interactive print of the first <em><strong>n</strong></em> occurrences of an error (where <em><strong>n</strong></em> is user-selectable) over the specified date range.</td>
</tr>
<tr class="even">
<td>XUERTRP PRINT T-1 1 ERR</td>
<td><strong>Print 1 occurence of each error for T-1 (QUEUE)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ONE^XTER1A</strong></p></td>
<td>This option obtains a listing of the first occurrence of each error recorded on the previous day. It can be queued to run shortly after midnight. If a device is specified, the output is sent to the specified device. If a device is <em>not</em> specified, the output is sent in a mail message to the individual who queued the option to run. It should be set to automatically requeue at a <strong>1D</strong> (every day) interval.</td>
</tr>
<tr class="odd">
<td>XUERTRP PRINT T-1 2 ERR</td>
<td><strong>Print 2 occurrences of errors on T-1 (QUEUED)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TWO^XTER1A</strong></p></td>
<td>This option obtains a listing of the first two occurrences of each error recorded on the previous day. It can be queued to run shortly after midnight. If a device is specified, the output is sent to the specified device. If a device is <em>not</em> specified, the output is sent in a mail message to the individual who queued the option to run. It should be set to automatically requeue at a <strong>1D</strong> (every day) interval.</td>
</tr>
<tr class="even">
<td>XUERTRP TYPE</td>
<td><strong>Remove a TYPE of error</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TYPE^XTERPUR</strong></p></td>
<td>This option removes a type of error.</td>
</tr>
<tr class="odd">
<td>XUEXKEY</td>
<td><strong>Allocate/De-Allocate Exclusive Key(s)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EXCLUSE^XQ6B</strong></p></td>
<td><p>This option can be used to just edit the MUTUALLY EXCLUSIVE KEYS Multiple in the SECURITY KEY (#19.1) file.</p>
<p>This option is locked with the <strong>XUEXKEY</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XUFAIL</td>
<td><strong>Failed Access Attempts Log</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a list by <strong>DATE/TIME</strong> of those users who have failed access into the system.</td>
</tr>
<tr class="odd">
<td>XUFDEV</td>
<td><strong>Device Failed Access Attempts</strong></td>
<td>Print</td>
<td></td>
<td>This option displays failed access attempts; it sorts on device then <strong>DATE/TIME</strong>. It gives a subtotal of attempts for each device and a total of all those attempts requested in the sort. It prompts for a print device to generate a hard copy if desired.</td>
</tr>
<tr class="even">
<td>XUFDISP</td>
<td><strong>User Failed Access Attempts</strong></td>
<td>Print</td>
<td></td>
<td>This option displays the user failed access attempts; it sorts on name then <strong>DATE/TIME</strong> of attempt. It prompts for device. It gives subtotals by user; total for all failed access attempts.</td>
</tr>
<tr class="odd">
<td>XUFILEACCESS</td>
<td><strong>File Access Security</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu gives and takes away files from any user as long as you have the same access and the same files as the user you are granting or taking away the files. It includes the following options:</p>
<ul>
<li><p><strong>XUFILEGRANT</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUFILESETDELETE</strong><br />
(DISPLAY ORDER: 40)</p></li>
<li><p><strong>XUFILEPRINT</strong><br />
(DISPLAY ORDER: 30)</p></li>
<li><p><strong>XUFILELIST</strong><br />
(DISPLAY ORDER: 25)</p></li>
<li><p><strong>XUFILECOPY</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUFILEREMOVEALL</strong><br />
(DISPLAY ORDER: 45)</p></li>
<li><p><strong>XUFILESINGLEADD</strong><br />
(DISPLAY ORDER: 10)</p></li>
<li><p><strong>XUFILEINQUIRY</strong><br />
(DISPLAY ORDER: 20)</p></li>
<li><p><strong>XUFILEDELETE</strong><br />
(DISPLAY ORDER: 50)</p></li>
<li><p><strong>XUFILERANGEASSIGN</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUFILEACCESS SEC OFCR</td>
<td><strong>Fileman Security Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes options to display/print the VA FileMan files users can access. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUFILEINQUIRY</strong> (1)</p></li>
<li><p><strong>XUFILELIST</strong> (2)</p></li>
<li><p><strong>XUFILEPRINT</strong> (3)</p></li>
<li><p><strong>XUFILESETDELETE</strong> (4)</p></li>
<li><p><strong>XUFILESINGLEADD</strong> (5)</p></li>
<li><p><strong>XUDIACCESS FOR OIG</strong> (6)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUFILECOPY</td>
<td><strong>Copy One User’s File Access to Others</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>COPY^XUFILE</strong></p></td>
<td>This option copies the file access that one user holds and give that same access to others.</td>
</tr>
<tr class="even">
<td>XUFILEDELETE</td>
<td><strong>Take away All access to a File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DELF^XUFILE1</strong></p></td>
<td>This option deletes the access all users hold to a particular file. This does <em>not</em> include those users with <strong>Programmer</strong> access [that is <strong>DUZ(0)=“@”</strong>].</td>
</tr>
<tr class="odd">
<td>XUFILEGRANT</td>
<td><strong>Grant Users’ Access to a Set of Files</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUFILE</strong></p></td>
<td><p>This option gives one or more users access to selected files. You can enter an individual file number, a range of numbers, and/or a list of file numbers.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/091.png) <strong>NOTE:</strong> You can only give out access to files to which you have access.</p></td>
</tr>
<tr class="even">
<td>XUFILEINQUIRY</td>
<td><strong>Inquiry to a User’s File Access</strong></td>
<td>Inquire</td>
<td><p>Exit Action:</p>
<p><strong>K %ZISI,DISYS,DP,P,V,W,X1</strong></p></td>
<td>This option shows what kind of file access a particular user has.</td>
</tr>
<tr class="odd">
<td>XUFILELIST</td>
<td><strong>List Access to Files by File number</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ACC^XUFILE1</strong></p></td>
<td>This option lists, by file number, those users who have access to the range of files selected and what that access is.</td>
</tr>
<tr class="even">
<td>XUFILEPRINT</td>
<td><strong>Print Users Files</strong></td>
<td>Print</td>
<td><p>Exit Action:</p>
<p><strong>K %ZISI,B,P,DIJ,DISYS</strong></p></td>
<td>This option lists, by user, each file the user has access to, and what that access is. Users who have no access are <em>not</em> listed.</td>
</tr>
<tr class="odd">
<td>XUFILERANGEASSIGN</td>
<td><strong>Assign/Delete a File Range</strong></td>
<td>Edit</td>
<td><p>Exit Action:</p>
<p><strong>K %X,%Y,DI,DISYS,DQ,V,W</strong></p></td>
<td>This option assigns or deletes a file range for a user. This file range is used when creating a new file. If the range is present, then the user can only create new files whose numbers are within the range.</td>
</tr>
<tr class="even">
<td>XUFILEREMOVEALL</td>
<td><strong>Remove All Access from a Single User</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>DELI^XUFILE1</strong></td>
<td>This option removes all the file access a single user holds.</td>
</tr>
<tr class="odd">
<td>XUFILESETDELETE</td>
<td><strong>Delete Users’ Access to a Set of Files</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUDEL^XUFILE</strong></p></td>
<td>This option deletes the access to files held by one or more users. You can enter an individual file number, a range of numbers, and/or a list of file numbers.</td>
</tr>
<tr class="even">
<td>XUFILESINGLEADD</td>
<td><strong>Single file add/delete for a user</strong></td>
<td>Edit</td>
<td><p>Exit Action:</p>
<p><strong>K V,W,C,DI,DISYS,DQ,%X,%Y,DLAYGO</strong></p></td>
<td>This option adds or deletes the access a user has for a single file.</td>
</tr>
<tr class="odd">
<td>XUFPURGE</td>
<td><strong>Failed Access Attempts Log Purge</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>FAPURGE^XUAPURGE</strong></p></td>
<td>This option asks for a beginning and ending date to purge all those entries in that range. Also, it asks for a <strong>DATE/TIME</strong> when this task will be queued to run.</td>
</tr>
<tr class="even">
<td>XUHALT</td>
<td><strong>Halt</strong></td>
<td>Action</td>
<td><p>ENTRY ACTION:</p>
<p><strong>S:’$D(XQCH) XQCH=“HALT” G:$L(XQCH)&gt;2 HALT^XQ12 S XQUR=“HALT” G XPRMP^XQ12</strong></p></td>
<td>This command terminates processing in MenuMan.</td>
</tr>
<tr class="odd">
<td>XU-INACTIVE PERSON CLASS USERS</td>
<td><strong>List Inactive Person Class Users</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PR^XUBA</strong></p></td>
<td>This option lists users who currently have inactive Person Classes and need to be assigned new Person Classes.</td>
</tr>
<tr class="even">
<td>XUINDEX</td>
<td><strong>%Index of Routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XINDEX</strong></p></td>
<td>This option runs the <strong>%INDEX</strong> routine.</td>
</tr>
<tr class="odd">
<td>XUINDEX2</td>
<td><strong>Structured Routine listing</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XCR^%INDX8</strong></p></td>
<td>This option allows the direct printing of <strong>%INDEX</strong>’s structured routine print.</td>
</tr>
<tr class="even">
<td>XUINQUIRE</td>
<td><strong>Option Function Inquiry</strong></td>
<td>Inquire</td>
<td></td>
<td>This option displays the information known to MenuMan about a given option.</td>
</tr>
<tr class="odd">
<td>XU-INSTITUTION-DEA</td>
<td><strong>Institution DEA# edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the Facility DEA number in the INSTITUTION (#4) file.</td>
</tr>
<tr class="even">
<td>XU-INSTITUTION-E</td>
<td><strong>Institution Edit</strong></td>
<td>ScreenMan</td>
<td></td>
<td>This option edits a subset of the fields in the INSTITUTION (#4) file.</td>
</tr>
<tr class="odd">
<td>XUKERNEL</td>
<td><strong>Kernel Management Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains Kernel management options. It includes the following options:</p>
<ul>
<li><p><strong>XUSITEPARM</strong></p></li>
<li><p><strong>XUVERSIONEW-HELP</strong></p></li>
<li><p><strong>XU-INSTITUTION-E</strong></p></li>
<li><p><strong>XUMF INSTITUTION</strong></p></li>
<li><p><strong>XUMF IMF ADD EDIT</strong></p></li>
<li><p><strong>XUSSPKI EDIT</strong></p></li>
<li><p><strong>XU-INSTITUTION-DEA</strong></p></li>
<li><p><strong>XUPS NPF CLEANUP MAIN MENU</strong></p></li>
<li><p><strong>XU SID ASK</strong></p></li>
<li><p><strong>XU SITE LOCKOUT</strong></p></li>
<li><p><strong>XU IP RELEASE</strong></p></li>
<li><p><strong>XUMF LOAD NPI</strong></p></li>
<li><p><strong>XU SID EDIT</strong></p></li>
<li><p><strong>XUER EDIT PARAMS</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUKEYALL</td>
<td><strong>Allocation of Security Keys</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XQ6</strong></p></td>
<td>This option assigns a set of security keys to an individual user or a single key to a set of users. To be eligible, a security key <em>must</em> be in existence and owned by the user of this option.</td>
</tr>
<tr class="odd">
<td>XUKEYDEALL</td>
<td><strong>De-allocation of Security Keys</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN2^XQ6</strong></p></td>
<td>This option takes away a set of security keys from an individual user or a single security key from a set of users. To be eligible, a security key <em>must</em> be in existence and owned by the user of this option.</td>
</tr>
<tr class="even">
<td>XUKEYEDIT</td>
<td><strong>Enter/Edit of Security Keys</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the descriptions of existing security keys and adds new keys to the system. Holders are specified through the <strong>Allocation of Security Keys</strong> [XUKEYALL] option.</td>
</tr>
<tr class="odd">
<td>XUKEYMGMT</td>
<td><strong>Key Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains all options used to manage security keys. It includes the following options:</p>
<ul>
<li><p><strong>ORLEASE</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUKEYDEALL</strong><br />
(DISPLAY ORDER: 2)</p></li>
<li><p><strong>XUKEYEDIT</strong><br />
(DISPLAY ORDER: 3)</p></li>
<li><p><strong>XQSHOKEY</strong></p></li>
<li><p><strong>XQLISTKEY</strong></p></li>
<li><p><strong>XQKEYDEL</strong></p></li>
<li><p><strong>XQKEYRDEL</strong></p></li>
<li><p><strong>XQKEYALTODEL</strong></p></li>
<li><p><strong>XQLOCK1</strong></p></li>
<li><p><strong>XQLOCK2</strong></p></li>
<li><p><strong>XUEXKEY</strong></p></li>
</ul>
<p>This menu is locked with the <strong>XUSPY</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XULIST</td>
<td><strong>List Terminal Types</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a list of the various terminal types known to the system.</td>
</tr>
<tr class="odd">
<td>XULM EDIT LOCK DICTIONARY</td>
<td><strong>Edit Lock Dictionary</strong></td>
<td>Action</td>
<td></td>
<td>This option allows users to add entries to the lock dictionary or edit existing entries.</td>
</tr>
<tr class="even">
<td>XULM EDIT PARAMETERS</td>
<td><strong>Edit Lock Manager Parameters</strong></td>
<td>Action</td>
<td></td>
<td>This option edits the site parameters for the Kernel Lock Manager.</td>
</tr>
<tr class="odd">
<td>XULM LOCK MANAGER</td>
<td><strong>Kernel Lock Manager</strong></td>
<td>Action</td>
<td>ENTRY ACTION: <strong>D MAIN^XULM</strong></td>
<td>This option allows the user to display the lock table and terminate processes that hold problem locks.</td>
</tr>
<tr class="even">
<td>XULM LOCK MANAGER MENU</td>
<td><strong>Lock Manager Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu holds all the options for the Kernel Lock Manager. It is located on <strong>Operations Management</strong> [XUSITEMGR] menu. It includes the following options:</p>
<ul>
<li><p><strong>XULM LOCK MANAGER</strong><br />
SYNONYM: LM<br />
DISPLAY ORDER: 1</p></li>
<li><p><strong>XULM EDIT LOCK DICTIONARY</strong><br />
SYNONYM: EDIT<br />
DISPLAY ORDER: 4</p></li>
<li><p><strong>XULM PURGE LOCK MANAGER LOG</strong><br />
SYNONYM: PURG<br />
DISPLAY ORDER: 6</p></li>
<li><p><strong>XULM VIEW LOCK MANAGER LOG</strong><br />
SYNONYM: LOG<br />
DISPLAY ORDER: 5</p></li>
<li><p><strong>XULM EDIT PARAMETERS</strong><br />
SYNONYM: SITE<br />
DISPLAY ORDER: 5</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XULM PURGE LOCK MANAGER LOG</td>
<td><strong>Purge Lock Manager Log</strong></td>
<td>Action</td>
<td>ENTRY ACTION: <strong>D PURGE^XULMLOG</strong></td>
<td>This option purges the Lock Manger Log of old entries.</td>
</tr>
<tr class="even">
<td>XULM RPC BROKER CONTEXT</td>
<td><strong>KERNEL LOCK MANAGER</strong></td>
<td>Broker (Client /Server)</td>
<td><ul>
<li><p>RPC: <strong>XULM GET LOCK TABLE</strong><br />
<br />
RPCKEY: <strong>XULM LOCKS</strong></p></li>
<li><p>RPC: <strong>XULM KILL PROCESS</strong><br />
<br />
RPCKEY: <strong>XULM LOCKS</strong></p></li>
</ul></td>
<td>This is the “<strong>B</strong>” type option used by the Kernel Lock Manager.</td>
</tr>
<tr class="odd">
<td>XULM VIEW LOCK MANAGER LOG</td>
<td><strong>View Lock Manager Log</strong></td>
<td>Inquire</td>
<td></td>
<td>This option allows you to view the Kernel Lock Manager Log.</td>
</tr>
<tr class="even">
<td>XUMAINT</td>
<td><strong>Menu Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu allows the systems manager or developer to maintain the menus, options, and security. It includes the following options:</p>
<ul>
<li><p><strong>XUEDITOPT</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUXREF</strong><br />
(DISPLAY ORDER: 8)</p></li>
<li><p><strong>XQHELP-MENU</strong><br />
(DISPLAY ORDER: 12)</p></li>
<li><p><strong>XQRESTRICT</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUOPTWHO</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>XQOPTFIX</strong><br />
(DISPLAY ORDER: 11)</p></li>
<li><p><strong>XQSMD MGR</strong><br />
(DISPLAY ORDER: 4)</p></li>
<li><p><strong>XUKEYMGMT</strong><br />
(DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUXREF-2</strong></p></li>
<li><p><strong>XQOOMAIN</strong></p></li>
<li><p><strong>XQDISPLAY OPTIONS</strong></p></li>
<li><p><strong>XQOPED</strong> (SYNONYM: OPED)</p></li>
<li><p><strong>XQBUILDMAIN</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUMF DMIS ID LOAD</td>
<td><strong>Load DMIS ID’s</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DMIS^XUMF04Q</strong></p></td>
<td><p>This option queues a background job that:</p>
<ul>
<li><p>Queries the Institution Master File (IMF).</p></li>
<li><p>Gets the DoD DMIS ID facilities.</p></li>
<li><p>Populates the local INSTITUTION (#4) file with them.</p></li>
</ul>
<p>This option is locked with the <strong>XUMF INSTITUTION</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XUMF IMF ADD EDIT</td>
<td><strong>IMF edit</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message:</p>
<p><strong>LOG REMEDY TICKET TO CHANGE NATIONAL ENTRY</strong></p></td>
<td><p>This option edits this facility’s (or associated facility’s) address information. The edits update your local INSTITUTION (#4) file</p>
<p><em>and</em> the Institution Master File (IMF) on FORUM.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/092.png) CAUTION: Use extreme care updating this information, because you will be updating not just your own database but the national database as well.</p>
<p>This option is locked with the <strong>XUMF INSTITUTION</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUMF IMF EDIT STATUS</td>
<td><strong>IMF Display Cleanup Status</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message:</p>
<p><strong>DO NOT USE THIS OPTION</strong></p></td>
<td>This option displays the facilities associated with the user and the status of the IMF data cleanup for each facility.</td>
</tr>
<tr class="even">
<td>XUMF INSTITUTION</td>
<td><strong>Institution File Query / Update</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUMF4</strong></p>
<p>Out of Order Message:</p>
<p><strong>Use XUMF LOAD INSTITUTION</strong></p></td>
<td><p>This option provides clean up utilities to check for duplicate station numbers and to get a copy of Institution Master File from FORUM for comparison and update purposes.</p>
<p>The cleanup utilities provide several lists to compare the local INSTITUTION (#4) file with the Institution Master File (IMF) -- the “Gold” file of Institutions complete with all approved station numbers including inactive as well as active station numbers. Utilities will be included to resolve duplicate station numbers and to automatically populate the local INSTITUTION (#4) file with national IMF data.</p>
<p>The INSTITUTION (#4) file cleanup utilities use the query functionality provided by the Master File Server mechanism. An HL7 Master File Query (<strong>MFQ</strong>) message is sent to FORUM to get the IFM. The <strong>MFQ</strong> message is handled by the VistA HL7 package that invokes the Master File Sever (MFS) message handler.</p>
<p>The MFS handler interprets the query and builds/sends the appropriate response to the local site in an HL7 Master File Response (<strong>MFR</strong>) message. The VistA HL7 package invokes the MFS handler on the local site that stores the IMF data in a temporary global. The cleanup utilities use this information for the displays and to automatically update the local INSTITUTION (#4) file.</p>
<p>This option is locked with the <strong>XUMF INSTITUTION</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUMF LOAD INSTITUTION</td>
<td><strong>Update/refresh Institution file with IMF data</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUMF04Q</strong></p></td>
<td><p>This option queries the Institution Master File (IMF) to get the gold file of institutions and automatically updates the local INSTITUTION (#4) file.</p>
<p>This option is locked with the <strong>XUMF INSTITUTION</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XUMF LOAD NPI</td>
<td><strong>Load Institution NPI values</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUMF416</strong></p>
<p>Out of Order Message:</p>
<p><strong>USE XUMF LOAD INSTITUTION</strong></p></td>
<td>This option will execute an HL7 query to FORUM to get the NPI values from the Institution Master File (IMF) and update the local INSTITUTION (#4) file.</td>
</tr>
<tr class="odd">
<td>XUMF335 clean 4.1 and 4</td>
<td><strong>Patch XU*8*335 clean 4.1 and 4</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message:</p>
<p><strong>USE XUMF LOAD INSTITUTION</strong></p></td>
<td><p>This option removes existing entries from the FACILITY TYPE (#4.1) file and gets the “Gold” standard from FORUM. It updates the INSTITUTION (#4) file with IMF data.</p>
<p>This option is locked with the <strong>XUMF INSTITUTION</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XUMNACCESS</td>
<td><strong>Access Monitor Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes options to the <strong>Access Monitor Menu</strong>.</p>
<p>It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUPMDISP</strong> (1)</p></li>
<li><p><strong>XUPMPURGE</strong> (2)</p></li>
<li><p><strong>XUFAIL</strong> (3)</p></li>
<li><p><strong>XUFPURGE</strong> (4)</p></li>
<li><p><strong>XUFDEV</strong> (5)</p></li>
<li><p><strong>XUFDISP</strong> (6)</p></li>
<li><p><strong>XUSC LIST</strong> (7)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUOAA SEND HL7 MESSAGE</td>
<td><strong>Send HL7 PMU message</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OAA^XUOAAHL7</strong></p></td>
<td>This option sends an HL7 PMU message to the Office of Academic Affiliations (OAA).</td>
</tr>
<tr class="even">
<td>XUOPTDISP</td>
<td><strong>Option Audit Display</strong></td>
<td>Print</td>
<td></td>
<td>This display sorts on option then <strong>DATE/TIME</strong>. Also prompts for print device to generate a hard copy of listing.</td>
</tr>
<tr class="odd">
<td>XUOPTLOG</td>
<td><strong>Audited Options Log</strong></td>
<td>Print</td>
<td></td>
<td>This report sorts on <strong>DATE/TIME</strong> then option; it prints all data elements of each entry requested.</td>
</tr>
<tr class="even">
<td>XUOPTPURGE</td>
<td><strong>Audited Options Purge</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OPTPURGE^XUAPURGE</strong></p></td>
<td>This option prompts for a beginning and ending date <em>and</em> time to purge the Option Audit entries. Also, it prompts for when the task will be run.</td>
</tr>
<tr class="odd">
<td>XUOPTUSER</td>
<td><strong>User Management Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains various Kernel options that have to do with managing individual users. It includes the following options:</p>
<ul>
<li><p><strong>XUUSERSTATUS</strong></p></li>
<li><p><strong>XU FINDUSER</strong><br />
(SYNONYM: FIND)</p></li>
<li><p><strong>XUSERREL</strong></p></li>
<li><p><strong>XUSC LIST</strong></p></li>
<li><p><strong>XUSERLIST</strong></p></li>
<li><p><strong>XUSERINQ</strong></p></li>
<li><p><strong>XUSAP PROXY LIST</strong><br />
(SYNONYM: PXY)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUOPTWHO</td>
<td><strong>Option Access By User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ55</strong></p></td>
<td>This option prompts for a menu option and then prints a list of which users can access this option. The list can be printed with or without the menu paths to the option.</td>
</tr>
<tr class="odd">
<td>XUOUT</td>
<td><strong>Out of Service Set/Clear</strong></td>
<td>Edit</td>
<td></td>
<td>This option controls whether a device is Out of Order or <em>not</em>. If set Out of Order by this option, a device <em>cannot</em> be used for logon.</td>
</tr>
<tr class="even">
<td>XU-PERSON CLASS EDIT</td>
<td><strong>Person Class Edit</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S DIC=“^VA(200,”,DIC(0)=“AEMQ”,DIC(“S”)=“I $S($P(^(0),U,11):$P(^(0),U,11)’&lt;DT,1:1)” D ^DIC K DIC Q:Y=-1 S DA=+Y,DR=“[XU-PERSON CLASS]”,DIE=“^VA(200,” D XUDIE^XUS5 K D0,DA,DIE,DR</strong></p></td>
<td><p>This option edits Person Class data. This option is located under the <strong>User Management</strong> [XUSER] menu.</p>
<p>Give this option to any user who needs to edit this data. Users that have been terminated <em>cannot</em> be edited.</p></td>
</tr>
<tr class="odd">
<td>XU-PERSON CLASS REMOVE</td>
<td><strong>Remove a person class entry</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REMOVE^XUA4A72</strong></p></td>
<td>This option should be given only to those persons that the site trusts to remove entries from the Person Class multiple of the NEW PERSON (#200) file. The PERSON CLASS Multiple holds a history, and under normal use, entries should <em>not</em> be removed. This option is to fix real messes.</td>
</tr>
<tr class="even">
<td>XU-PING-SERVER</td>
<td><strong>TCP/IP type PING server</strong></td>
<td>Server</td>
<td><p>Routine:</p>
<p><strong>XTSPING</strong></p></td>
<td>This is a PING server that works like PING under TCP/IP. If you send a message to this server, it will send it back to you.</td>
</tr>
<tr class="odd">
<td>XUPMDISP</td>
<td><strong>Display of Programmer Mode Entry List</strong></td>
<td>Print</td>
<td></td>
<td><p>This option:</p>
<ul>
<li><p>Displays which users entered <strong>Programmer</strong> mode.</p></li>
<li><p>Sorts data by user name and then <strong>DATE/TIME</strong>.</p></li>
<li><p>Prompts for a print device to generate a hard copy if desired.</p></li>
<li><p>Gives a count of entries by user.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUPMPURGE</td>
<td><strong>Programmer Mode Entry Log Purge</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PMPURGE^XUAPURGE</strong></p></td>
<td>This option runs the <strong>XUPMPURG</strong> routine to purge the log of <strong>Programmer</strong> mode entry.</td>
</tr>
<tr class="odd">
<td>XUPR RTN CHKSUM</td>
<td><strong>Check Routines on Other CPUs</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTSUMCK</strong></p></td>
<td>This option compares the checksum for routines on one system to the checksums for the same routines on another system. It is only for sites that have Compute and Print Servers with different routine directories.</td>
</tr>
<tr class="even">
<td>XUPR RTN EDIT</td>
<td><strong>Routine Edit</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>R !,”ROUTINE: “,X:DTIME I X?1A1.7AN X ^%ZOSF(“TEST”) I X “ZL @X ^%Z”</strong></p></td>
<td><p>This option allows developers on the site manager’s staff to edit MUMPS routines.</p>
<p>This option is locked with the security XUPROGMODE key.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/093.png) CAUTION: This option is only for developers.</p></td>
</tr>
<tr class="odd">
<td>XUPR RTN PATCH</td>
<td><strong>Routines by Patch Number</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTPTCH</strong></p></td>
<td>This option prints routines associated with a patch. You <em>must</em> enter a list of routines and then the output displays by patch numbers.</td>
</tr>
<tr class="even">
<td>XUPRGL</td>
<td><strong>List Global</strong></td>
<td>Action</td>
<td><p>Routine:</p>
<p><strong>%G</strong></p>
<p>Entry Action:</p>
<p><strong>D @($S(^%ZOSF(“OS”)[“MSM”:”^%GL”,^%ZOSF(“OS”)[“DTM”:”^%g”,1:”^%G”))</strong></p></td>
<td><p>This option runs the operating system routine to list specified globals:</p>
<ul>
<li><p>For MSM systems: It is <strong>%GL</strong>.</p></li>
<li><p>For other systems: it is <strong>%G</strong>.</p></li>
</ul>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUPRINT</td>
<td><strong>Print Option File</strong></td>
<td>Print</td>
<td></td>
<td>This option produces a formatted listing of the OPTION (#19) file, showing each option and its associated information.</td>
</tr>
<tr class="even">
<td>XUPROG</td>
<td><strong>Programmer Options</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu is used by developers. It includes the following options:</p>
<ul>
<li><p><strong>XUPROGMODE</strong> (SYNONYM: PG)</p></li>
<li><p><strong>XUPRGL</strong></p></li>
<li><p><strong>XUERRS</strong></p></li>
<li><p><strong>XT-NUMBER BASE CHANGER</strong></p></li>
<li><p><strong>XTSUMBLD</strong><br />
(SYNONYM: NTEG)</p></li>
<li><p><strong>DI DDMAP</strong></p></li>
<li><p><strong>XT-OPTION TEST</strong></p></li>
<li><p><strong>XQ UNREF’D OPTIONS</strong></p></li>
<li><p><strong>XUPR-ROUTINE-TOOLS</strong></p></li>
<li><p><strong>XTSUMBLD-CHECK</strong></p></li>
<li><p><strong>XTV MENU</strong></p></li>
<li><p><strong>XPD MAIN</strong><br />
(SYNONYM: KIDS)</p></li>
<li><p><strong>XUROUTINES</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUPROGMODE</td>
<td><strong>Programmer mode</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PRGMODE^%ZOSV</strong></p></td>
<td><p>This option drops the programmer into <strong>Programmer</strong> direct mode.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XUPROTOCOL EDIT</td>
<td><strong>Edit a Protocol</strong></td>
<td>Edit</td>
<td><p>Entry Action:</p>
<p><strong>S DLAYGO=101</strong></p>
<p>Exit Action:</p>
<p><strong>K DLAYGO I $D(NAME) S XQORM=$O(^ORD(101,”B”,NAME,0))_”;ORD(101,” D XREF^XQORM K XQORM,NAME</strong></p></td>
<td>This option creates or edits a protocol.</td>
</tr>
<tr class="odd">
<td>XUPRROU</td>
<td><strong>List Routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTPP</strong></p></td>
<td>This option uses the <strong>%ZTPP</strong> routine to print a listing of the routines.</td>
</tr>
<tr class="even">
<td>XUPR-ROUTINE-TOOLS</td>
<td><strong>Routine Tools</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu includes the group of programmer options that deal with routines. It includes the following options:</p>
<ul>
<li><p><strong>XUINDEX</strong></p></li>
<li><p><strong>XU FIRST LINE PRINT</strong></p></li>
<li><p><strong>XTFCR</strong></p></li>
<li><p><strong>XTFCE</strong></p></li>
<li><p><strong>XUROUTINE IN</strong></p></li>
<li><p><strong>XUPRROU</strong></p></li>
<li><p><strong>XUROUTINE OUT</strong></p></li>
<li><p><strong>XT-ROUTINE COMPARE</strong></p></li>
<li><p><strong>XUPR RTN EDIT</strong></p></li>
<li><p><strong>XT-VARIABLE CHANGER</strong></p></li>
<li><p><strong>XT-VERSION NUMBER</strong></p></li>
<li><p><strong>XTRGRPE</strong></p></li>
<li><p><strong>XUPR-RTN-TAPE-CMP</strong></p></li>
<li><p><strong>XTRDEL</strong></p></li>
<li><p><strong>XUPR RTN PATCH</strong></p></li>
<li><p><strong>XUPR RTN CHKSUM</strong></p></li>
<li><p><strong>XU CHECKSUM REPORT</strong></p></li>
<li><p><strong>XU CHECKSUM LOAD</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUPR-RTN-TAPE-CMP</td>
<td><strong>Compare routines on tape to disk</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TAPE^XTRCMP</strong></p></td>
<td>This option reads a standard DSM <strong>%RS</strong> tape or disk file or M/11 tape and compares the routines on the tape with a routine with the same name in the current account.</td>
</tr>
<tr class="even">
<td>XUPS ASSESSMENT DETAIL</td>
<td><strong>XUPS ASSESSMENT DETAIL</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DETAIL^XUPSCLR</strong></p></td>
<td>List NEW PERSON (#200) file entries that have missing DOB, SSN, or SEX, and NEW PERSON (#200) file statistics.</td>
</tr>
<tr class="odd">
<td>XUPS ASSESSMENT DETAIL</td>
<td><strong>XUPS ASSESSMENT DETAIL</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DETAIL^XUPSCLR</strong></p></td>
<td>This option lists NEW PERSON (#200) file entries that have missing DOB, SSN, or SEX, and NEW PERSON (#200) file statistics.</td>
</tr>
<tr class="even">
<td>XUPS ASSESSMENT STATS</td>
<td><strong>XUPS ASSESSMENT STATS</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>STATS^XUPSCLR</strong></p></td>
<td>List NEW PERSON (#200) file statistics for the cleanup.</td>
</tr>
<tr class="odd">
<td>XUPS ASSESSMENT STATS</td>
<td><strong>XUPS ASSESSMENT STATS</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>STATS^XUPSCLR</strong></p></td>
<td>This option lists NEW PERSON (#200) file statistics for the cleanup.</td>
</tr>
<tr class="even">
<td>XUPS NPF CLEANUP MAIN MENU</td>
<td><strong>NPF cleanup main menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the main menu for the NEW PERSON (#200) file cleanup. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUPS ASSESSMENT STATS</strong><br />
(SYNONYM: STA; DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUPS ASSESSMENT DETAIL</strong><br />
(SYNONYM: DET; DISPLAY ORDER: 2)</p></li>
<li><p><strong>XUPS PREUPDATE NPF REPORTS</strong><br />
(SYNONYM: PRE; DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUPS UPDATE NEW PERSON FILE</strong><br />
(SYNONYM: UPD; DISPLAY ORDER: 4)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUPS PREUPDATE NPF REPORTS</td>
<td><strong>XUPS PREUPDATE NPF REPORTS</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUPSPAID</strong></p>
<p>Entry Action:</p>
<p><strong>S XUPSACT=“PRINT”</strong></p>
<p>Exit Action:</p>
<p><strong>K XUPSACT</strong></p></td>
<td>This option reports on all NEW PERSON (#200) file entries whose Name, DOB, and/or Sex is different from their corresponding PAID EMPLOYEE file entries, as well as the NEW PERSON (#200) file entries that will be updated.</td>
</tr>
<tr class="even">
<td>XUPS PREUPDATE NPF REPORTS</td>
<td><strong>XUPS PREUPDATE NPF REPORTS</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUPSPAID</strong></p>
<p>Entry Action:</p>
<p><strong>S XUPSACT=“PRINT”</strong></p>
<p>Exit Action:</p>
<p><strong>K XUPSACT</strong></p></td>
<td>This option reports on all NEW PERSON (#200) file entries whose NAME, DOB, and/or SEX is different from their corresponding PAID EMPLOYEE file entries, as well as the NEW PERSON (#200) file entries that will be updated.</td>
</tr>
<tr class="odd">
<td>XUPS UPDATE NEW PERSON FILE</td>
<td><strong>XUPS UPDATE NEW PERSON FILE DATA</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUPSPAID</strong></p>
<p>Entry Action:</p>
<p><strong>S XUPSACT=“UPDATE”</strong></p></td>
<td>This option updates NEW PERSON (#200) file entries with data from the PAID EMPLOYEE file.</td>
</tr>
<tr class="even">
<td>XUPS UPDATE NEW PERSON FILE</td>
<td><strong>XUPS UPDATE NEW PERSON FILE DATA</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUPSPAID</strong></p>
<p>Entry Action:</p>
<p><strong>S XUPSACT=“UPDATE”</strong></p></td>
<td>This option updates NEW PERSON (#200) file entries with data from the PAID EMPLOYEE file.</td>
</tr>
<tr class="odd">
<td>XUPS VISTALINK</td>
<td><strong>XUPS VISTALINK</strong></td>
<td>Broker (Client / Server)</td>
<td><p>RPC:</p>
<p><strong>XUPS PERSONQUERY</strong></p></td>
<td>This option is an RPC Broker Client / Server option.</td>
</tr>
<tr class="even">
<td>XUPS VISTALINK</td>
<td><strong>XUPS VISTALINK</strong></td>
<td>Broker (Client/ Server)</td>
<td><p>RPC:</p>
<p><strong>XUPS PERSONQUERY</strong></p></td>
<td>This is an RPC Broker Client/Server option.</td>
</tr>
<tr class="odd">
<td>XURELOG</td>
<td><strong>Restart Session</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S:’$D(XQCH) XQCH=“REST” G:$L(XQCH)&gt;2 REST^XQ12 S XQUR=“REST” G X PRMP^XQ12</strong></p></td>
<td>This option returns a user to the signon logic, so that a session can be restarted <em>without</em> dropping a telecommunication line.</td>
</tr>
<tr class="even">
<td>XURESJOB</td>
<td><p><strong>Kill off a users’ job</strong></p>
<p>Synonym: RJD</p></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W:’$D(^%ZOSF(“RESJOB”)) !,*7,”NOT AVAILABLE” X:$D(^(“RESJOB”)) ^(“RESJOB”)</strong></p>
<p>Exit Action:</p>
<p><strong>D ^XUTMRJD ;call TaskMan utility to adjust the list of running tasks</strong></p></td>
<td><p>This option uses the MUMPS vendor’s exit forcing utility to allow the system manager to forcibly exit MUMPS jobs.</p>
<p>An exit action on this option allows the system manager to adjust TaskMan’s list of running tasks if some of the processes forcibly exited were tasks.</p>
<p>This option is locked with the <strong>XUMGR</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUROUTINE IN</td>
<td><strong>Input routines</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>N % S %=$G(^%ZOSF(“OS”)) D @$S(%[“OpenM”:”^%RI”,%[“DTM”:”^%rload”,%[“GT.M”:”^%RI”,1:”^%RR”)</strong></p></td>
<td><p>Loads routines from an external device, like a host file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/094.png) CAUTION: Do <em>not</em> use this option if you are not sure how to run it!</p></td>
</tr>
<tr class="even">
<td>XUROUTINE OUT</td>
<td><strong>Output routines</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>N % S %=$G(^%ZOSF(“OS”)) D @$S(%[“GT.M”:”^ZRO”,%[“OpenM”:”^%RO”,%[“DTM”:”^%rsave”,1:”^%RS”)</strong></p></td>
<td>This routine outputs routines to an external device, such as a host file.</td>
</tr>
<tr class="odd">
<td>XUROUTINES</td>
<td><strong>Routine Management Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains various Kernel options relating to the management of routines on the system. It includes the following options:</p>
<ul>
<li><p><strong>XTMOVE</strong></p></li>
<li><p><strong>XTRDEL</strong></p></li>
<li><p><strong>XTMOVE-IN</strong></p></li>
<li><p><strong>XUPRROU</strong></p></li>
<li><p><strong>XU FIRST LINE PRINT</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><span id="XUS_IAM_NPFM_BATCH_UPDATE_Option" class="anchor"></span>XUS IAM NPFM BATCH UPDATE</td>
<td><span id="MPI_New_Person_Feild_Mon_Btch_Upd_Option" class="anchor"></span><strong>MPI NEW PERSON FIELD MONITOR BATCH UPDATE</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>EN1^XUIAMNPB</strong></td>
<td><p>This option calls the <strong>EN1^XUIAMNPB</strong> routine. It monitors the NEW PERSON FIELD MONITOR (#8933.1) file for changes to NEW PERSON (#200) fields. The process associated with this option loops through the <strong>AVIAM</strong> cross-reference (x-ref) of the NEW PERSON FIELD MONITOR (#8933.1) file, which is created when a specific list of NEW PERSON (File #200) fields are modified. This modified new person data is transmitted to Person Service Identity Management (PSIM) via the Service Provisioning Markup Language (SPML) using Web Services, and then after transmission the REQUIRES TRANSMISSION (#.03) field is set to <strong>NO</strong> and the LAST TRANSMITTED DATE/TIME (#.04) field is marked as <strong>NOW</strong> in the NEW PERSON FIELD MONITOR (#8933.1) file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/095.png) <strong>NOTE:</strong> This option needs to be scheduled in TaskMan to run every <strong>600 seconds</strong> with SPECIAL QUEUEING defined as <strong>STARTUP</strong>.</p></td>
</tr>
<tr class="odd">
<td><span id="XUS_IAM_NPFM_PURGE_Option" class="anchor"></span>XUS IAM NPFM PURGE</td>
<td><span id="MPI_New_Person_Field_Mon_Purge_Option" class="anchor"></span><strong>MPI NEW PERSON FIELD MONITOR PURGE</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>EN2^XUIAMNPB</strong></td>
<td><p>This option calls the <strong>EN2^XUIAMNPB</strong> routine. It deletes all entries from the NEW PERSON FIELD MONITOR (#8933.1) file that are older than the number of days specified in the NEW PERSON FIELD MONITOR PURGE (#875) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file when the REQUIRES TRANSMISSION (#.03) field in the NEW PERSON FIELD MONITOR (#8933.1) is <em>not</em> equal to <strong>YES</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/096.png) <strong>NOTE:</strong> If the NEW PERSON FIELD MONITOR PURGE (#875) field in the KERNEL SYSTEM PARAMETERS (#8989.3) is <em>not</em> defined, then the number of days will automatically default to <strong>365</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/097.png) <strong>NOTE:</strong> This option needs to be scheduled in TaskMan to run <strong>DAILY</strong> with SPECIAL QUEUEING defined as <strong>STARTUP</strong>.</p></td>
</tr>
<tr class="even">
<td><span id="XUS_IAM_USER_TERMINATE_Option" class="anchor"></span>XUS IAM USER TERMINATE</td>
<td><strong>XUS IAM USER TERMINATE</strong></td>
<td>Action</td>
<td><p>Action Entry:</p>
<p><strong>D FTOP^XUIAMDD1</strong></p></td>
<td>This option was added with Kernel Patch XU*8.0*799. It calls the <strong>FTOP^XUIAMDD1</strong> routine. It was added as an item to the <strong>XU USER TERMINATE</strong> extended action option. The <strong>XUS IAM USER TERMINATE</strong> option allows the Identity Access Management (IAM) team to know when NEW PERSON (#200) file records with future termination dates have been subsequently terminated by the background job <strong>XUAUTODEACTIVATE</strong>. It then triggers the <strong>SPML</strong> message to PSIM, as well as executing any other IAM needed down-stream processes.</td>
</tr>
<tr class="odd">
<td>XUS KAAJEE PROXY LOGON</td>
<td><strong>KAAJEE PROXY BROKER CONTEXT</strong></td>
<td>Broker (Client/ Server)</td>
<td><p>RPC:</p>
<p><strong>XUS KAAJEE GET USER VIA PROXY</strong></p></td>
<td>This is the KAAJEE Application User Broker Context option.</td>
</tr>
<tr class="even">
<td>XUS KAAJEE WEB LOGON</td>
<td><strong>KAAJEE BROKER CONTEXT</strong></td>
<td>Broker (Client / Server)</td>
<td><p>RPCs:</p>
<ul>
<li><p><strong>XUS KAAJEE GET USER INFO</strong></p></li>
<li><p><strong>XUS KAAJEE LOGOUT</strong></p></li>
<li><p><strong>XUS ALLKEYS</strong></p></li>
<li><p><strong>XUS KAAJEE GET CCOW TOKEN</strong></p></li>
</ul></td>
<td>This option is an RPC Broker Client/Server option.</td>
</tr>
<tr class="odd">
<td>XUS NPI CBO LIST</td>
<td><strong>List of NPI data for CBO</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CBOLIST^XUSNPIED</strong></p></td>
<td>This option lists providers related to the NPI rollout. This list is sent to the Chief Business Office (CBO) monthly for tracking status of the rollout.</td>
</tr>
<tr class="even">
<td>XUS NPI ENTER NPI FOR PROVIDER</td>
<td><strong>Add/Edit NPI values for Providers</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLEREDIT^XUSNPIED</strong></p></td>
<td>This option is intended for support staff to be able to enter data related to an NPI value for providers.</td>
</tr>
<tr class="odd">
<td>XUS NPI EXEMPT PROVIDER</td>
<td><strong>Mark/Unmark Provider Exempt from requiring an NPI</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLERXMPT^XUSNPIED</strong></p></td>
<td>Support staff use this option to indicate that a provider who has a Person Class entry relating to a taxonomy value that would normally require and NPI value, as <em>not</em> needing one (such as if the provider were doing administrative work full time).</td>
</tr>
<tr class="even">
<td>XUS NPI EXTRACT REPORT</td>
<td><strong>XUS NPI EXTRACT REPORT</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TASKMAN^XUSNPIX1</strong></p></td>
<td>This option compiles the NPI Extract file and emails it to <strong>&lt;REDACTED&gt;.VA.GOV</strong></td>
</tr>
<tr class="odd">
<td>XUS NPI LOCAL REPORTS</td>
<td><strong>Print Local NPI Reports</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PRINTOPT^XUSNPIED</strong></p></td>
<td>This option generates reports for the local facility on those who are expected to have NPI values entered.</td>
</tr>
<tr class="even">
<td>XUS NPI MENU</td>
<td><strong>NPI (National Provider ID) Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides the ability to enter data for a provider related to the National Provider ID. It includes the following options:</p>
<ul>
<li><p><strong>XUS NPI ENTER NPI FOR PROVIDER</strong></p></li>
<li><p><strong>XUS NPI EXEMPT PROVIDER</strong></p></li>
<li><p><strong>XUS NPI LOCAL REPORTS</strong></p></li>
</ul>
<p>This option is locked with the <strong>XUSNPIMTL</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XUS NPI PROVIDER SELF ENTRY</td>
<td><strong>PROVIDER NPI SELF ENTRY</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>USEREDIT^XUSNPIED</strong></p></td>
<td>This option provides the ability for a provider to enter his/her own NPI value and effective date. It is intended to be attached to the <strong>XU COMMON</strong> menu and checks whether the user selecting it has the need to enter an NPI value.</td>
</tr>
<tr class="even">
<td>XUS NPI SIGNON CHECK</td>
<td><strong>NPI Signon Check</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>D SIGNON^XUSNPIED</strong></p></td>
<td>This option checks a user’s signon to see whether the user needs to enter an NPI value. If so, a message is displayed to the user.</td>
</tr>
<tr class="odd">
<td>XUS PROC CNT CLUP</td>
<td><strong>XUS Process count cleanup</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLEAR^XUSCNT(0)</strong></p></td>
<td>This option is only needed for GT.M sites. For a GT.M site it should be scheduled to run between every <strong>1</strong> to <strong>8</strong> hours. This is the Kernel process count cleanup routine. It checks the entries in <strong>XUTL(“XUSYS”,$J)</strong> to see if they are still active and if <em>not</em> remove the entry.</td>
</tr>
<tr class="even">
<td>XUS SIGNON</td>
<td><strong>Kernel sign-on context</strong></td>
<td>Broker (Client / Server)</td>
<td><p>RPCs:</p>
<ul>
<li><p><strong>XUS SIGNON SETUP</strong></p></li>
<li><p><strong>XUS AV CODE</strong></p></li>
<li><p><strong>XUS INTRO MSG</strong></p></li>
<li><p><strong>XUS CVC</strong></p></li>
<li><p><strong>XUS AV HELP</strong></p></li>
<li><p><strong>XUS DIVISION SET</strong></p></li>
<li><p><strong>XUS GET USER INFO</strong></p></li>
<li><p><strong>XUS DIVISION GET</strong></p></li>
<li><p><strong>XWB GET BROKER INFO</strong></p></li>
<li><p><strong>XUS GET TOKEN</strong></p></li>
<li><p><strong>XUS CCOW VAULT PARAM</strong></p></li>
<li><p><strong>XUS GET CCOW TOKEN</strong></p></li>
</ul></td>
<td>This option is an RPC Broker Client/Server option.</td>
</tr>
<tr class="odd">
<td>XUSAP PROXY LIST</td>
<td><strong>Proxy User List</strong></td>
<td>Print</td>
<td></td>
<td>This option runs a VA FileMan (FM) print to show any users that have a USER CLASS of APPLICATION PROXY or CONNECTOR PROXY.</td>
</tr>
<tr class="even">
<td>XUSAZONK</td>
<td><strong>Purge of the %ZUA global</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PURG^ZUA[MGR]</strong></p>
<p>Entry Action:</p>
<p><strong>S XUSLNT=1</strong></p>
<p>Exit Action:</p>
<p><strong>K XUSLNT</strong></p></td>
<td>This option purges the FAILED ACCESS ATTEMPTS and PROGRAMMER MODE ACCESS logs of all entries older than <strong>30</strong> days.</td>
</tr>
<tr class="odd">
<td>XUSC LIST</td>
<td><strong>Print Sign-on Log</strong></td>
<td>Print</td>
<td></td>
<td>This option prints the SIGN-ON LOG.</td>
</tr>
<tr class="even">
<td>XUSCZONK</td>
<td><span id="Purge_SignOn_log_Option" class="anchor"></span><strong>Purge Sign-On log</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SCPURG^XUSPURGE</strong></p></td>
<td>This option purges the SIGN-ON LOG. Kernel Patch XU*8.0*756 enhanced the <strong>SCPURG^XUSPURGE</strong> routine. It updated this option so that it protects sign-on log entries for at least the number of days specified by the ISO or the default <strong>365 days</strong> as defined in the <a href="#SIGN_ON_LOG_RETENTION_sys_parameter"><strong>SIGN-ON LOG RETENTION (#221)</strong></a> parameter field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
</tr>
<tr class="odd">
<td>XUSEC ISO ACTIVE USER EXTRACT</td>
<td><strong>Special Active User Excel output</strong></td>
<td>Print</td>
<td></td>
<td>This option produces a special Microsoft<sup>®</sup> Excel formatted output.</td>
</tr>
<tr class="even">
<td>XUSEC ISO ACTIVE USER EXTRACT</td>
<td><strong>Special Active User Excel Output</strong></td>
<td>Print</td>
<td></td>
<td><p>The Information Security Officer (ISO) uses this option to extract information to Microsoft<sup>®</sup> Excel for the 2008 SMART Database.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/098.png) <strong>NOTE:</strong> This option was requested by OCIS and released with Kernel Patch XU*8.0*424.</p></td>
</tr>
<tr class="odd">
<td>XUSEC ISO Q TERMINATION REPORT</td>
<td><strong>Queueable ISO Terminated User Report</strong></td>
<td>Print</td>
<td></td>
<td>This is a queueable version of the ISO’s termination date report. The report dates are from the current date minus <strong>eight</strong> (<strong>8</strong>) <strong>days</strong> to the current date minus <strong>one</strong> (<strong>1</strong>) <strong>day</strong>.</td>
</tr>
<tr class="even">
<td>XUSEC ISO TERMINATION REPORT</td>
<td><strong>ISO’s Terminated User Report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EP1^XUSECAD</strong></p></td>
<td>This is the interactive option for the ISOs, where the user can select beginning and ending dates.</td>
</tr>
<tr class="odd">
<td>XUSEC UP ARROW TERM REPORT</td>
<td><strong>Up Arrow Delimited Termination Report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EP1^XUSECAD</strong></p>
<p>Entry Action:</p>
<p><strong>S XUSECU=“</strong></p></td>
<td>This option produces a report that is a caret (<strong>^</strong>; aka <strong>Up-Arrow</strong>) delimited termination report that can be used as a spread sheet. It is suggested that the report be sent to an <strong>HFS</strong> device. If the screen is used, it requires a <strong>132</strong>-column width.</td>
</tr>
<tr class="even">
<td>XUSER</td>
<td><strong>User Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu adds, changes, and deletes users from the NEW PERSON (#200) file, as well as clears devices for signon purposes. It includes the following options:</p>
<ul>
<li><p><strong>XUSERNEW</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUSEREDIT</strong><br />
(DISPLAY ORDER: 15)</p></li>
<li><p><strong>XUSERREACT</strong><br />
(DISPLAY ORDER: 25)</p></li>
<li><p><strong>XUSERDEACT</strong><br />
(DISPLAY ORDER: 20)</p></li>
<li><p><strong>XUTESTUSER</strong><br />
(DISPLAY ORDER: 40)</p></li>
<li><p><strong>XUSERINQ</strong><br />
(DISPLAY ORDER: 35)</p></li>
<li><p><strong>XUFILEACCESS</strong><br />
(DISPLAY ORDER: 45)</p></li>
<li><p><strong>XUSESIG CLEAR</strong><br />
(DISPLAY ORDER: 60)</p></li>
<li><p><strong>XUSERBLK</strong><br />
(DISPLAY ORDER: 10)</p></li>
<li><p><strong>XUSESIG BLOCK</strong></p></li>
<li><p><strong>XUSERREPRINT</strong></p></li>
<li><p><strong>XUSER FILE MGR</strong></p></li>
<li><p><strong>XU-PERSON CLASS EDIT</strong></p></li>
<li><p><strong>XU-CLINICAL TRAINEE MENU</strong></p></li>
<li><p><strong>XUOPTWHO</strong><br />
(SYNONYM: WHO)</p></li>
<li><p><strong>XU-INACTIVE PERSON CLASS USERS</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUSER DIV CHG</td>
<td><strong>Change my Division</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DIVCHG^XUSER1</strong></p></td>
<td><p>This option changes the division to which you are currently assigned. It performs the same function as entering your current division at the “Select DIVISION: default division //” signon prompt.</p>
<p>If you only have one division from which to select, <strong>XUSER DIV CHG</strong> shows you your current division and indicates that you <em>cannot</em> change it.</p></td>
</tr>
<tr class="even">
<td>XUSER FILE MGR</td>
<td><strong>Manage User File</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu manages the NEW PERSON (#200) file. It includes the following options:</p>
<ul>
<li><p><strong>XUSERPURGEATT</strong></p></li>
<li><p><strong>XUSERAOLD</strong></p></li>
<li><p><strong>XUSER KEY RE-INDEX</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUSER KEY RE-INDEX</td>
<td><strong>Reindex the users key’s</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>IXKEY^XUSMGR</strong></p></td>
<td>This option re-indexes the NEW PERSON (#200) file KEY subfield.</td>
</tr>
<tr class="even">
<td>XUSER PC BUILD</td>
<td><strong>User PC build Print</strong></td>
<td>Print</td>
<td></td>
<td><p>This option prints a list of users in the NEW PERSON (#200) file who hold the <strong>PROVIDER</strong> security key <em>and</em> have a Verify Code.</p>
<p>This option is <em>not</em> attached to a menu but can be added to the secondary menu of any user who will be working on this project and then removed when the project is complete.</p>
<p>This option prints the following fields:</p>
<ul>
<li><p>NAME</p></li>
<li><p>PERSON CLASS (<strong>FREE TEXT</strong>)</p></li>
<li><p>PROVIDER TYPE (<strong>SET OF CODES</strong>).</p></li>
</ul>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/099.png) <strong>NOTE:</strong> The last two fields can only contain data at sites that have implemented the Decision Support System (DSS).</p></td>
</tr>
<tr class="odd">
<td>XUSER PC BUILD EDIT</td>
<td><strong>User PC build Edit</strong></td>
<td>Edit</td>
<td></td>
<td><p>This option allows the rapid data entry (R/S) of Person Class data.</p>
<p>This option is <em>not</em> attached to a menu but can be added to the secondary menu of a user who will be performing data entry and then removed when the project is complete.</p></td>
</tr>
<tr class="even">
<td>XUSER SEC OFCR</td>
<td><strong>User Security Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options that allow the user to review users on the system. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XUSERINQ</strong> (1)</p></li>
<li><p><strong>XUSERLIST</strong> (2)</p></li>
<li><p><strong>XUUSERSTATUS</strong> (3)</p></li>
<li><p><strong>XU FINDUSER</strong> (4)</p></li>
<li><p><strong>XUTESTUSER</strong> (5)</p></li>
<li><p><strong>XQLISTKEY</strong> (6)</p></li>
<li><p><strong>XQOPACCESS</strong> (7)</p></li>
<li><p><strong>XUUSEROPT</strong> (8)</p></li>
<li><p><strong>XUSERDEACT</strong> (9)</p></li>
<li><p><strong>XUSERREACT</strong> (10)</p></li>
<li><p><strong>XUSEC ISO TERMINATION REPORT</strong> (11)</p></li>
<li><p><strong>XUSEC UP ARROW TERM REPORT</strong> (12)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUSERAOLD</td>
<td><strong>Purge Log of Old Access and Verify Codes</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>AOLD^XUSPURGE</strong></p></td>
<td>This option purges all inactive Access and Verify Codes that are more than <strong>270</strong> to <strong>400</strong> days old. This allows for the recycling of codes after a minimum of <strong>three</strong> (<strong>3</strong>) changes.</td>
</tr>
<tr class="even">
<td>XUSERBLK</td>
<td><strong>Grant Access by Profile</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSERBLK</strong></p></td>
<td><p>This option adds or edits one or more users according to an existing user profile. The complete profile of the actual or dummy user, menus, and security keys included, is copied to the other users. For new users, security forms are generated. (Use the <strong>Help Processor</strong> [XQHELP-MENU] menu to edit the XUSER COMPUTER ACCOUNT help frame containing the text of the forms.) To route forms, be sure that the user profile has a service/section and that the corresponding entry in the SERVICE/SECTION file has a Coordinator.</p>
<p>This option is locked with the <strong>XUMGR</strong> and <strong>XUADD</strong> security keys and is restricted for use by systems management staff.</p></td>
</tr>
<tr class="odd">
<td><span id="XUSERBLK_TEMPLATE_Option" class="anchor"></span>XUSERBLK TEMPLATE</td>
<td><strong>Template Grant Access by Profile</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>XUSERBLK</strong></td>
<td><p>This option is attached to the <strong>User Management</strong> [XUSER] menu option. It allows for the creation or edit of a template user based on an existing user profile. The template user can then be used as a template profile for adding or editing users with the <strong>Grant Access by Profile</strong> [XUSERBLK] option. This option is locked with the <strong>XUMGR</strong> security key and is restricted for use by systems management staff.</p>
<p>This option was added with Kernel Patch XU*8.0*799.</p></td>
</tr>
<tr class="even">
<td>XUSER-CLEAR-ALL</td>
<td><strong>Clear all users at startup</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUS6</strong></p></td>
<td>This option should be set up in the SPECIAL QUEUING to run whenever TaskMan starts up. It goes through and clears all users signed-on from the multiple signon restriction.</td>
</tr>
<tr class="odd">
<td>XUSERCLR</td>
<td><strong>Clear Terminal</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>X6^XUSMGR</strong></p></td>
<td>This option clears a terminal that has been locked up due to too many errors during signon.</td>
</tr>
<tr class="even">
<td>XUSERDEACT</td>
<td><strong>Deactivate a User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSTERM</strong></p></td>
<td>As of a specified TERMINATION DATE, user is <em>not</em> allowed to sign on to the computer.</td>
</tr>
<tr class="odd">
<td>XUSEREDIT</td>
<td><strong>Edit an Existing User</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S DIC=“^VA(200,”,DIC(0)=“AEMQ”,DIC(“S”)=“I $S($P(^(0),U,11):$P(^(0),U,11)’&lt;DT,1:1)” D ^DIC K DIC Q:Y=-1 S DA=+Y,DR=“[XUEXISTING USER]”,DIE=“^VA(200,” D XUDIE^XUS5 K D0,DA,DIE,DR</strong></p></td>
<td>This option edits a user’s characteristics. Users that have been terminated <em>cannot</em> be edited.</td>
</tr>
<tr class="even">
<td>XUSEREDITSELF</td>
<td><strong>Edit User Characteristics</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EUC^XUS5</strong></p></td>
<td><p>This option edits certain user attributes as defined by the KERNEL SYSTEM PARAMETERS (#8989.3) file. At most, the user can edit the following fields:</p>
<ul>
<li><p>VERIFY CODE</p></li>
<li><p>AUTO-MENU</p></li>
<li><p>TYPE-AHEAD</p></li>
<li><p>NICKNAME</p></li>
</ul>
<p>This can vary at your site. A user can also edit the SUBTYPE of their device.</p></td>
</tr>
<tr class="odd">
<td>XUSERINQ</td>
<td><strong>User Inquiry</strong></td>
<td>Inquire</td>
<td><p>Routine:</p>
<p><strong>USERINQ^XUSMGR</strong></p></td>
<td><p>This option displays various user attributes. If the user is currently signed on, it displays the following:</p>
<ul>
<li><p>Job and device numbers.</p></li>
<li><p>Signon time.</p></li>
<li><p>What option is being executed.</p></li>
</ul>
<p>Otherwise, it displays the last signon time. It also displays which security keys are held by this user.</p></td>
</tr>
<tr class="even">
<td>XUSERINT</td>
<td><strong>Introductory text edit</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W !!,”Enter introductory text to be displayed at each logon”,!! S DIE=“^XTV(8989.3,”,DA=1,DR=240 D ^DIE</strong></p></td>
<td>This option edits the introductory text that is displayed each time the user signs on.</td>
</tr>
<tr class="odd">
<td>XUSERLIST</td>
<td><strong>List users</strong></td>
<td>Print</td>
<td></td>
<td>This message lists users known to the system.</td>
</tr>
<tr class="even">
<td><span id="XUSERNEW_Option" class="anchor"></span>XUSERNEW</td>
<td><span id="Add_a_New_User_to_the_System_Option" class="anchor"></span><strong>Add a New User to the System</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSERNEW</strong></p></td>
<td><p>This option adds a new user to the system.</p>
<p>Kernel Patch XU*8.0*799 modified this option to execute an Enterprise User Search, prompting the user for the individual's Veteran Affairs (VA) email address or their network identification (ID) name to use in the lookup. If a match is <em>not</em> initially found, then additional traits (i.e., Name, SSN, and optionally, their Date of Birth [DOB], and/or Gender) are then prompted for and an additional Enterprise User Search is performed. However, if a user(s) is ultimately found, then their identifying traits from the Enterprise will be displayed for selection. Upon selection of one of these displayed record(s), then the Enterprise traits will be added to the VistA NEW PERSON (#200) file and any traits from VistA <em>not</em> known at the Enterprise (including the Site's Station Number and the user's <strong>DUZ</strong>) will be filed at the Enterprise. If the user is <em>not</em> found at the Enterprise, then a ServiceNow (SNOW) ticket should be logged as all new users being added to VistA should already be known at the Enterprise.</p></td>
</tr>
<tr class="odd">
<td>XUSERPOST</td>
<td><strong>Post sign-in Text Edit</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W !!,”Enter Post Logon Text to be displayed after each logon.”,!! S DIE=“^XTV(8989.3,”,DA=1,DR=245 D ^DIE</strong></p></td>
<td>This option displays the logon text after a user signs onto the system.</td>
</tr>
<tr class="even">
<td>XUSERPURGEATT</td>
<td><strong>Purge Inactive Users’ Attributes</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSTERM1</strong></p></td>
<td>This utility cleans up files. It removes all mailboxes and messages, mail groups, and security keys for users who have been terminated. If any of these users still retain Access Codes, these will be deleted.</td>
</tr>
<tr class="odd">
<td>XUSERREACT</td>
<td><strong>Reactivate a User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REACT^XUSERNEW</strong></p></td>
<td>This option reactivates a user who has a TERMINATION DATE. You are asked to enter their ACCESS CODE. If you give them an Access Code (or if they still have one), their TERMINATION DATE is removed.</td>
</tr>
<tr class="even">
<td>XUSERREL</td>
<td><strong>Release user</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>X8^XUSMGR</strong></p></td>
<td>This option clears the record that a user is signed on to another terminal. It may seem that a user is signed on when there is an abnormal exit, such as an error or entry into <strong>Programmer</strong> mode.</td>
</tr>
<tr class="odd">
<td>XUSERREPRINT</td>
<td><strong>Reprint Access agreement letter</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REPRINT^XUSERNEW</strong></p></td>
<td>This option allows a site manager to reprint the computer access agreement letter. It does <em>not</em> reprint the Access Code on the letter.</td>
</tr>
<tr class="even">
<td><span id="XUSERTEM_Option" class="anchor"></span>XUSERTEM</td>
<td><strong>Template User Add</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSERNEW</strong></p></td>
<td><p>This option was added with Kernel Patch XU*8.0*799. It was attached to the <strong>User Management</strong> [XUSER] menu option. It allows for the creation of New "Template" Users in the NEW PERSON (#200) file as previously accomplished prior to the enhancements by bypassing all NEW Enterprise features detailed in Kernel Patch XU*8.0*799. These "Template" users are used by the <strong>Grant Access By Profile</strong> [XUSERBLK] option.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/100.png) <strong>NOTE:</strong> The <strong>Template User Add</strong> [XUSERTEM] option is basically a copy of the <strong>Add a New User to the System</strong> [XUSERNEW] option, so that when executed it can bypass the Enterprise features, which is determined by the option name passed to the process.</p></td>
</tr>
<tr class="odd">
<td>XUSERTOOLS</td>
<td><strong>User’s Toolbox</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu provides several different utilities designed for the average user. It includes the following options:</p>
<ul>
<li><p><strong>XQTUSER</strong></p></li>
<li><p><strong>XU-SPL-MENU</strong></p></li>
<li><p><strong>XUSEREDITSELF</strong></p></li>
<li><p><strong>XUUSERDISP</strong></p></li>
<li><p><strong>XUUSERHELP</strong></p></li>
<li><p><strong>XUSESIG</strong></p></li>
<li><p><strong>XUTM USER</strong></p></li>
<li><p><strong>XUSER DIV CHG</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUSERVDISP</td>
<td><strong>Server audit display</strong></td>
<td>Print</td>
<td></td>
<td>This option displays the server-type option audit data.</td>
</tr>
<tr class="odd">
<td>XUSERWHERE</td>
<td><strong>Where am I?</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>D GETENV^%ZOSV W !!,”UCI: “,$P(Y,U),” VOLUME SET: “,$P(Y,U,2) W</strong></p>
<p><strong>:$P(Y,U,3)]”“ “ NODE: “,$P(Y,U,3) W !,” DEVICE: “,$I,$S($D(IO(“IP”)):” (“_IO(“</strong></p>
<p><strong>IP”)_”)”,1:”“)</strong></p></td>
<td>This option shows a user their environment. Changed from showing <strong>IO(“ZIO”)</strong> to <strong>IO(“IP”)</strong>.</td>
</tr>
<tr class="even">
<td>XUSESIG</td>
<td><strong>Electronic Signature code Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSESIG</strong></p></td>
<td><p>This option allows users to edit the following fields:</p>
<ul>
<li><p>INITIALS</p></li>
<li><p>SIGNATURE BLOCK TITLE</p></li>
<li><p>ELECTRONIC SIGNATURE CODE</p></li>
<li><p>OFFICE PHONE</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUSESIG BLOCK</td>
<td><strong>Electronic Signature Block Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN^XUSESIG2</strong></p></td>
<td>This option gives access to the Signature Block of the Electronic Signature. This is automatically set by a cross-reference of the NAME field. If it is changed with this option, it <em>must</em> contain the last name from the NAME field. Also, if the NAME field is changed this field will be changed and may need to be re-edited.</td>
</tr>
<tr class="even">
<td>XUSESIG CLEAR</td>
<td><strong>Clear Electronic signature code</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLEAR^XUSESIG</strong></p></td>
<td>This option allows the site manager to clear (delete) a user’s electronic signature code, so they can enter a new one.</td>
</tr>
<tr class="odd">
<td>XUSESIG DEG</td>
<td><strong>EDUCATION (Degree) File Edit</strong></td>
<td>Edit</td>
<td><strong>DIC(20.11,</strong></td>
<td>This option edits degree entries in the EDUCATION (#20.11) file. These entries define valid degrees that users can enter in the DEGREE (#10.6) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td>XUSFACHK</td>
<td><strong>Check Failed Access Log</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>FAILED^XUSFACHK</strong></p></td>
<td><p>This option runs the Failed Access Check routine <strong>XUSFACHK</strong>.</p>
<p>It looks to see if there have been many failed access attempts, since the routine was last run. If it finds that the number of failed access attempts is greater than the limit in the FAILED ATTEMPTS LIMIT - IRM field in the KERNEL SYSTEM PARAMETERS (#8989.3) file during normal business hours (<strong>8:00 a.m.</strong> to <strong>4:30 p.m.</strong>) it sends a message to the mail group stored in the IRM MAIL GROUP field or the limit set in the FAILED ATTEMPTS LIMIT – AOD field in the KERNEL SYSTEM PARAMETERS (#8989.3) file after hours, it sends a message to the mail group in the AFTER HOURS MAIL GROUP.</p></td>
</tr>
<tr class="odd">
<td>XUSITEMGR</td>
<td><strong>Operations Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options of use to the site manager, such as options for managing Kernel site parameters, sign-on log, introductory text, and so on. It includes the following options:</p>
<ul>
<li><p><strong>XUSERINT</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUSTATUS</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUSTAT</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>XQ XUTL $J NODES</strong></p></li>
<li><p><strong>XQAB MENU</strong></p></li>
<li><p><strong>XURESJOB<br />
</strong>(SYNONYM: RJD)</p></li>
<li><p><strong>XUOPTUSER</strong></p></li>
<li><p><strong>XUKERNEL</strong></p></li>
<li><p><strong>XQALERT DELETE OLD</strong></p></li>
<li><p><strong>XUSERPOST</strong></p></li>
<li><p><strong>XQALERT MGR</strong></p></li>
<li><p><strong>XWB MENU</strong></p></li>
<li><p><strong>XOBU SITE SETUP MENU</strong></p></li>
<li><p><strong>XLFIPV IPV4 IPV6 MENU</strong><br />
(SYNONYM: IPV)</p></li>
<li><p><strong>XULM LOCK MANAGER MENU</strong><br />
(SYNONYM: LOCK)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUSITEPARM</td>
<td><strong>Enter/Edit Kernel Site Parameters</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W !!,”Note: the TaskMan site parameters have been moved out of this file.”,!,”Use the Edit TaskMan Parameters option to edit those values.”,! S DA=1,DR=“[XUSITEPARM]”,DIE=8989.3 D XUDIE^XUS5</strong></p>
<p>Exit Action:</p>
<p><strong>K DA,DIE,DR</strong></p></td>
<td>This option edits the KERNEL SYSTEM PARAMETERS (#8989.3) file. It contains fields for default system values, lifetime of Verify Code, auto-generation of Access Codes, and name of user-characteristic edit template.</td>
</tr>
<tr class="odd">
<td>XU-SPL-ALLOW</td>
<td><strong>Allow other users access to spool documents</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the OTHER AUTHORIZED USERS field in the SPOOL DOCUMENT file to allow other users access to a spool document.</td>
</tr>
<tr class="even">
<td>XU-SPL-BROWSE</td>
<td><strong>Browse a Spool Document</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BROWSE^ZISPL</strong></p></td>
<td>This option uses the VA FileMan Browser tool on a Spool Document.</td>
</tr>
<tr class="odd">
<td>XU-SPL-DELETE</td>
<td><strong>Delete A Spool Document</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DELETE^ZISPL</strong></p></td>
<td>Delete a spool document from the SPOOL DOCUMENT file and delete the associated message if they are still linked.</td>
</tr>
<tr class="even">
<td>XU-SPL-LIST</td>
<td><strong>List Spool Documents</strong></td>
<td>Print</td>
<td></td>
<td>This option lists entries in the SPOOL DOCUMENT file.</td>
</tr>
<tr class="odd">
<td>XU-SPL-MAIL</td>
<td><strong>Make spool document into a mail message</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>MAIL^ZISPL</strong></p></td>
<td>This option takes a spool document and posts it as a MailMan message to the user’s <strong>IN</strong> basket. This does <em>not</em> move the data at all but does decrease the number of lines charged to the user.</td>
</tr>
<tr class="even">
<td>XU-SPL-MENU</td>
<td><strong>Spooler Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the menu of options to work with spooled documents after they have been created. It includes the following options:</p>
<ul>
<li><p><strong>XU-SPL-LIST</strong></p></li>
<li><p><strong>XU-SPL-PRINT</strong></p></li>
<li><p><strong>XU-SPL-DELETE</strong></p></li>
<li><p><strong>XU-SPL-MAIL</strong></p></li>
<li><p><strong>XU-SPL-ALLOW</strong></p></li>
<li><p><strong>XU-SPL-BROWSE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU-SPL-MGR</td>
<td><strong>Spool Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the menu for the system administrators to manage the spooler access. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XU-SPL-DELETE</strong> (1)</p></li>
<li><p><strong>XU-SPL-USER</strong> (2)</p></li>
<li><p><strong>XU-SPL-LIST</strong> (3)</p></li>
<li><p><strong>XU-SPL-PRINT</strong> (4)</p></li>
<li><p><strong>XU-SPL-SITE</strong> (5)</p></li>
</ul>
<p>This menu is locked with the <strong>XUMGR</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XU-SPL-PRINT</td>
<td><strong>Print A Spool Document</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>PRINT^ZISPL</strong></p></td>
<td>This option prints a document that has been spooled.</td>
</tr>
<tr class="odd">
<td>XU-SPL-PURGE</td>
<td><strong>Purge old spool documents</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>1^ZISPL2</strong></p></td>
<td>This option should be tasked to run at least once a week to delete spool documents that are older than the number of days in the KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
</tr>
<tr class="even">
<td>XU-SPL-SITE</td>
<td><strong>Spooler Site Parameters Edit</strong></td>
<td>Edit</td>
<td></td>
<td>Edit the site parameters for the Spooler.</td>
</tr>
<tr class="odd">
<td>XU-SPL-USER</td>
<td><strong>Edit User’s Spooler Access</strong></td>
<td>Edit</td>
<td></td>
<td>This option allows the system administrators to edit the spooler fields in the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td>XUSPY</td>
<td><strong>Information Security Officer Menu</strong></td>
<td>Menu</td>
<td><p>Entry Action:</p>
<p><strong>D ^ASTR2</strong></p></td>
<td><p>This menu is for the person serving as the Information Security Officer (ISO). It includes the following options:</p>
<ul>
<li><p><strong>XUSER SEC OFCR</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUFILEACCESS SEC OFCR</strong><br />
(DISPLAY ORDER: 2)</p></li>
<li><p><strong>XU SEC OFCR</strong><br />
(DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUAUDIT MAINT</strong><br />
(DISPLAY ORDER: 4)</p></li>
<li><p><strong>XUMNACCESS</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>DG SECURITY OFFICER MENU</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>XUSEC ISO ACTIVE USER EXTRACT</strong></p></li>
<li><p><strong>452 SECURITY LOG BY USER</strong><br />
(SYNONYM: SL3)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XU-SPY-SHOW</td>
<td><strong>Display the Kernel Audit Parameters</strong></td>
<td>Print</td>
<td></td>
<td>This is an inquire to the KERNEL SYSTEM PARAMETERS (#8989.3) file to show the current AUDIT parameters that are set up.</td>
</tr>
<tr class="even">
<td>XUSSPKI CRL UPLOAD</td>
<td><strong>PKI CRL Upload</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CRLUP^XUSSPKI</strong></p></td>
<td>This option should be scheduled to run <strong>every hour</strong> to send any new URL for the CRLs to be collected by the PKI verification server.</td>
</tr>
<tr class="odd">
<td>XUSSPKI EDIT</td>
<td><strong>Kernel PKI Parameter Edit</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>N DA,DR,DDSFILE S DA=1,DR=“[XUSSPKI]”,DDSFILE=8989.3 D ^DDS</strong></p></td>
<td>This option runs the <strong>XUSSPKI</strong> form to edit the PKI server IP address.</td>
</tr>
<tr class="even">
<td>XUSSPKI UPN SET</td>
<td><strong>ePCS Set SAN from PIV Card</strong></td>
<td>Broker (Client/ Server</td>
<td><p>RPCs:</p>
<ul>
<li><p><strong>XUS PKI GET UPN</strong></p></li>
<li><p><strong>XUS PKI SET UPN</strong></p></li>
</ul></td>
<td><p>This is a Broker-type context option that sets the SUBJECT ALTERNATIVE NAME (#501.2) field (aka SAN field or USER PRINCIPLE NAME) in the NEW PERSON (#200) file from the Personal Identification Verification (PIV) Smart Card. This is used with the DEA ePCS electronic signature (e-sig) to be sure the correct certificate is selected from the PIV card.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/101.png) <strong>NOTE:</strong> This option only needs to be run once for a user at a site.<br />
<br />
It was released with Kernel Patch XU*8.0*580.</p></td>
</tr>
<tr class="odd">
<td>XUSTAT</td>
<td><strong>CPU/Service/User/Device Stats</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUSTAT</strong></p></td>
<td>This option gives you a system utilization report for CPUs, Services, or users.</td>
</tr>
<tr class="even">
<td>XUSTATUS</td>
<td><strong>System Status</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W @IOF N DUZ,DT,DTIME X:$D(^%ZOSF(“SS”))#2 ^(“SS”) D HOME^%ZIS</strong></p></td>
<td>This option uses an operating system utility to show all current jobs signed onto the computer.</td>
</tr>
<tr class="odd">
<td>XUTERM</td>
<td><strong>Terminal Type Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the TERMINAL TYPE (#3.2) file.</td>
</tr>
<tr class="even">
<td>XUTESTUSER</td>
<td><strong>Switch Identities</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TESTM^XUS91</strong></p></td>
<td>This option simulates signing on as another user, and thus, tests out a user’s menus. It assigns all security keys but does <em>not</em> allow for the execution of any options.</td>
</tr>
<tr class="odd">
<td>XUTIME</td>
<td><strong>Time</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>W !!,$$HTE^XLFDT($H,”P”)</strong></p></td>
<td>This command displays the time and date.</td>
</tr>
<tr class="even">
<td>XUTIO</td>
<td><strong>Device Management</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu maintains the DEVICE (#3.5) file, which defines the characteristics of each device attached to the computer. It includes the following options:</p>
<ul>
<li><p><strong>XUTERM</strong><br />
(DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUDEV</strong><br />
(DISPLAY ORDER: 2)</p></li>
<li><p><strong>XUOUT</strong><br />
(DISPLAY ORDER: 10)</p></li>
<li><p><strong>XUDISPLAY</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUCHANGE</strong><br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XULIST</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>XUTTEST</strong><br />
(DISPLAY ORDER: 9)</p></li>
<li><p><strong>XUTLOOPBACK</strong><br />
(DISPLAY ORDER: 8)</p></li>
<li><p><strong>XUSERCLR</strong><br />
(DISPLAY ORDER: 7)</p></li>
<li><p><strong>XU DA EDIT</strong></p></li>
<li><p><strong>XUDEVEDIT</strong></p></li>
<li><p><strong>XUDEV LINEPORT ADDR CURRENT</strong></p></li>
<li><p><strong>XUDEV LINEPORT ADDR EDIT</strong></p></li>
<li><p><strong>XUDEV LINEPORT ADDR RPT</strong></p></li>
<li><p><strong>XUDEV RES-ONE</strong></p></li>
<li><p><strong>XUDEV RES-CLEAR</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUTLOOPBACK</td>
<td><strong>Loopback Test of Device Port</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>D ^%ZIS Q:POP X ^%ZOSF(“EOFF”),^%ZOSF(“TYPE-AHEAD”),”F I=65:1:90 U IO W *I R *X:1 U IO(0) W:X&gt;32 $C(X)” X ^%ZOSF(“EON”),^%ZIS(“C”)</strong></p></td>
<td>This option tests a terminal line with the use of a loopback connection on the line. A loopback connector just ties pins <strong>2</strong>, <strong>3</strong> together.</td>
</tr>
<tr class="even">
<td>XUTM BACKGROUND PRINT</td>
<td><strong>Print Options that are Scheduled to run</strong></td>
<td>Print</td>
<td></td>
<td><p>This option prints a list of options from the OPTION SCHEDULING (#19.2) file that have data in one of the background task fields:</p>
<ul>
<li><p>QUEUED TO RUN AT WHAT TIME</p></li>
<li><p>DEVICE FOR QUEUED JOB OUTPUT</p></li>
<li><p>RESCHEDULING FREQUENCY</p></li>
<li><p>SPECIAL QUEUEING</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUTM BACKGROUND RECOMMENDED</td>
<td><strong>Print Options Recommended for Queueing</strong></td>
<td>Print</td>
<td></td>
<td>This option prints a list of options that have been recommended by the developers for background queueing.</td>
</tr>
<tr class="even">
<td>XUTM BVPAIR</td>
<td><strong>Site Parameters Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option allows the system manager to edit the TASKMAN SITE PARAMETERS (#14.7) file.</td>
</tr>
<tr class="odd">
<td>XUTM CHECK ENV</td>
<td><strong>Check Taskman’s Environment</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ZTMCHK</strong></p></td>
<td>This option checks TaskMan’s environment to make sure that links and global nodes required by TaskMan are present. These checks are the same checks that TaskMan performs every time it is started or restarted.</td>
</tr>
<tr class="even">
<td>XUTM CLEAN</td>
<td><strong>Clean Task File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>OPTION^XUTMK</strong></p></td>
<td><p>This option cleans out the Task Log for the site manager, removing all entries for tasks that have been completed, have been rejected, or have failed with an error. The site manager is asked to specify how old such entries can be before they should be deleted. It then deletes them from <strong>^%ZTSK</strong> for all inactive tasks that are older than that.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/102.png) <strong>NOTE:</strong> This option is <em>not</em> queueable; though, it does create a tasked job to do the actual deletion.<br />
<br />
<strong>ZTMQCLEAN</strong> is the queueable version of this option.</p></td>
</tr>
<tr class="odd">
<td>XUTM DEL</td>
<td><strong>Delete Tasks</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMD</strong></p></td>
<td>This option allows users to dequeue their own tasks and delete them from the Task Log. Users can delete either a single task or a range of tasks. Holders of the <strong>ZTMQ</strong> security key selecting this option can delete any tasks.</td>
</tr>
<tr class="even">
<td>XUTM DQ</td>
<td><strong>Dequeue Tasks</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMDQ</strong></p></td>
<td>This option allows users to dequeue their own tasks. Holders of the <strong>ZTMQ</strong> security key selecting this option can dequeue any tasks.</td>
</tr>
<tr class="odd">
<td>XUTM ERROR</td>
<td><strong>Taskman Error Log</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to help the site manager manage TaskMan’s log of errors. It includes the following options:</p>
<ul>
<li><p><strong>XUTM ERROR SHOW</strong> (1)</p></li>
<li><p><strong>XUTM ERROR LOG CLEAN RANGE</strong> (2)</p></li>
<li><p><strong>XUTM ERROR PURGE TYPE</strong> (3)</p></li>
<li><p><strong>XUTM ERROR DELETE</strong> (4)</p></li>
<li><p><strong>XUTM ERROR SCREEN LIST</strong> (5)</p></li>
<li><p><strong>XUTM ERROR SCREEN ADD</strong> (6)</p></li>
<li><p><strong>XUTM ERROR SCREEN EDIT</strong> (7)</p></li>
<li><p><strong>XUTM ERROR SCREEN REMOVE</strong> (8)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUTM ERROR DELETE</td>
<td><strong>Delete Error Log</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>KILL^XUTMKE</strong></p></td>
<td>This option deletes the Task Error Log.</td>
</tr>
<tr class="odd">
<td>XUTM ERROR LOG CLEAN RANGE</td>
<td><strong>Clean Error Log Over Range Of Dates</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RANGE^XUTMKE</strong></p></td>
<td>This option allows the site manager to remove from TaskMan’s error log all entries that occur on or between two dates. The site manager enters the two dates, first the earlier date and then the later date, and then the option removes the appropriate entries.</td>
</tr>
<tr class="even">
<td>XUTM ERROR PURGE TYPE</td>
<td><strong>Purge Error Log Of Type Of Error</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>TYPE^XUTMKE</strong></p></td>
<td><p>This option provides a way to clean TaskMan’s log of errors. The site manager can enter a string, and this option then deletes every entry in the log that contains that string. For example, if the site manager enters “<strong>&lt;UNDEF&gt;</strong>“, then every error that contains this string will be deleted. Two other examples are <strong>ZTSK+3^XQ1:4</strong> and <strong>E</strong>. The first removes all errors that occurred on the line and command indicated while the second removes <em>all</em> errors whose <strong>$ZE</strong> value contains an <strong>E</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/103.png) <strong>NOTE:</strong> This does <em>not</em> edit the system’s main error log, only TaskMan’s Error Log in the <strong>^%ZTSCH</strong> global.</p></td>
</tr>
<tr class="odd">
<td>XUTM ERROR SCREEN ADD</td>
<td><strong>Add Error Screens</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SCRAD^XUTMKE2</strong></p></td>
<td>This option adds more error screens. An error screen is a string of characters that TaskMan compares to the <strong>$ZE</strong> value of every error it traps. TaskMan only logs those trapped errors whose <strong>$ZE</strong> values do <em>not</em> contain an error screen as a substring. The system manager can choose to have the screen count the number of errors it screens out.</td>
</tr>
<tr class="even">
<td>XUTM ERROR SCREEN EDIT</td>
<td><strong>Edit Error Screens</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SCRED^XUTMKE2</strong></p></td>
<td>This option edits error screens. This involves deciding whether each edited screen should count the errors that occur while the screen is in place, and whether to reset counters for screens that have already counted some screened errors. The screens themselves are just strings of characters that TaskMan compares against the <strong>$ZE</strong> values of all errors it traps. Those errors whose <strong>$ZE</strong> values do <em>not</em> contain any screens as substrings are logged, but those that do are <em>not</em> logged.</td>
</tr>
<tr class="odd">
<td>XUTM ERROR SCREEN LIST</td>
<td><strong>List Error Screens</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SCLIST^XUTMKE1</strong></p></td>
<td>This option displays the error screens that are currently in place. An error screen is a string of characters. Any error that TaskMan logs is checked against the list of error screens. If an error occurs whose <strong>$ZE</strong> string contains a screen as a substring, then that error is <em>not</em> logged. Some error screens count the number of errors that they prevent from being logged.</td>
</tr>
<tr class="even">
<td>XUTM ERROR SCREEN REMOVE</td>
<td><strong>Remove Error Screens</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SCREM^XUTMKE1</strong></p></td>
<td><p>This option removes error screens. Error screens provide the system manager with a way to prevent certain errors from being logged.</p>
<p>TaskMan traps every error caused by its own code or by the code of the tasks it runs, but the only errors logged in the system error log and in TaskMan’s error log are those errors whose <strong>$ZE</strong> values do <em>not</em> contain an error screen as a substring. The system manager can decide whether to count the number of errors screened out.</p></td>
</tr>
<tr class="odd">
<td>XUTM ERROR SHOW</td>
<td><strong>Show Error Log</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LIST^XUTMKE</strong></p></td>
<td>This option displays a simple list of the errors recorded by TaskMan.</td>
</tr>
<tr class="even">
<td>XUTM INQ</td>
<td><strong>List Tasks</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMQ</strong></p></td>
<td>This option lists either all tasks currently queued or else all tasks listed in the Task Log.</td>
</tr>
<tr class="odd">
<td>XUTM MGR</td>
<td><strong>Taskman Management</strong></td>
<td>Menu</td>
<td><p>Entry Action:</p>
<p><strong>W:’$$TM^%ZTLOAD *7,!!,”WARNING -- TASK MANAGER DOESN’T SEEM TO BE RUNNING!!!!”,!!,*7</strong></p></td>
<td><p>This menu is for site managers. It allows the manipulation of TaskMan. It includes the following options:</p>
<ul>
<li><p><strong>XUTM SCHEDULE</strong> (DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUTM BACKGROUND PRINT</strong> (DISPLAY ORDER: 7)</p></li>
<li><p><strong>XUTM DEL</strong> (DISPLAY ORDER: 6)</p></li>
<li><p><strong>XUTM REQ</strong> (DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUTM DQ</strong> (DISPLAY ORDER: 4)</p></li>
<li><p><strong>XUTM UTIL</strong> (DISPLAY ORDER: 2)</p></li>
<li><p><strong>XU OPTION QUEUE</strong> (DISPLAY ORDER: 2)</p></li>
<li><p><strong>XUTM INQ</strong> (DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUTM BACKGROUND RECOMMENDED</strong></p></li>
<li><p><strong>XUTM TL CLEAN</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUTM PARAMETER EDIT</td>
<td><strong>Edit Taskman Parameters</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains the options that edit the TaskMan parameter files. It includes the following options:</p>
<ul>
<li><p><strong>XUTM BVPAIR</strong></p></li>
<li><p><strong>XUTM UCI</strong></p></li>
<li><p><strong>XUTM VOLUME</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUTM PROBLEM CLEAR</td>
<td><strong>Problem Device Clear</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CLEAR^XUTMKA</strong></p></td>
<td>This option clears the Problem Device global.</td>
</tr>
<tr class="even">
<td>XUTM PROBLEM DEVICES</td>
<td><strong>Problem Device report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>EN1^XUTMKA</strong></p></td>
<td>This option runs the <strong>XUTMKA</strong> routine to produce a list of devices that TaskMan is having problems opening. At the end of the report the Problem Device list is cleared.</td>
</tr>
<tr class="odd">
<td>XUTM QCLEAN</td>
<td><strong>Queuable Task Log Cleanup</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMK</strong></p></td>
<td>This option is equivalent to <strong>ZTMCLEAN</strong> except that this option can be scheduled through the <strong>Schedule/Unschedule Options</strong> [XUTM SCHEDULE] option to run periodically. This option only keeps completed entries from the last <strong>seven</strong> (<strong>7</strong>) days, unless overridden by the DAYS TO KEEP OLD TASKS field in the VOLUME SET file, as well as all queued entries.</td>
</tr>
<tr class="even">
<td>XUTM QPROBLEM DEVICES</td>
<td><strong>Queuable Problem Device report</strong></td>
<td>Run Routine</td>
<td><p>Routines:</p>
<p><strong>TASK^XUTMKA</strong></p></td>
<td>This option is for the queueable version of <strong>XUTM PROBLEM DEVICES</strong> option. At the end of the report the Problem Device list is cleared.</td>
</tr>
<tr class="odd">
<td>XUTM REPNT</td>
<td><strong>Repoint waiting tasks to a new port/device</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>REPNT^XUTMRP</strong></p></td>
<td>This option allows the site staff to take all tasks waiting for a given port/LTA device and reschedule them to some new device and/or to a new time. This is useful when a port stops working, and the tasks backed up waiting for it can be sent to another device until it is fixed.</td>
</tr>
<tr class="even">
<td>XUTM REQ</td>
<td><strong>Requeue Tasks</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMR</strong></p></td>
<td><p>This option requeues a user’s own tasks. Users can modify the device that the task is to be run on and the time that the task is to be run.</p>
<p>Holders of the <strong>ZTMQ</strong> security key selecting this option can requeue any tasks and can also modify the task’s priority and partition size.</p></td>
</tr>
<tr class="odd">
<td>XUTM RESTART</td>
<td><strong>Restart Task Manager</strong></td>
<td>Run Routine</td>
<td><p>Out of Order Message:</p>
<p><strong>Not used in RDP environment</strong></p>
<p>Routine:</p>
<p><strong>RESTART^ZTMB</strong></p></td>
<td>This option re-starts TaskMan, if it has failed.</td>
</tr>
<tr class="even">
<td>XUTM RP</td>
<td><strong>Change tasks device</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMRP</strong></p></td>
<td><p>This option allows site staff to indicate a replacement device and to then repoint and waiting and future tasks to the new device.</p>
<p>This is useful when a site renames devices or device becomes dedicated to a special task. This option can also go through the OPTION SCHEDULING (#19.2) file to repoint devices in this file.</p></td>
</tr>
<tr class="odd">
<td>XUTM RUN</td>
<td><strong>Remove Taskman from WAIT State</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>RUN^ZTMKU</strong></p></td>
<td>This option places TaskMan in a <strong>RUN</strong> state, in which TaskMan processes tasks normally, within fifteen seconds.</td>
</tr>
<tr class="even">
<td>XUTM SCHEDULE</td>
<td><strong>Schedule/Unschedule Options</strong></td>
<td>ScreenMan</td>
<td></td>
<td>This option edits the background job fields in the OPTION SCHEDULING (#19.2) file. The result of this action is to schedule or unschedule Task Manager tasks.</td>
</tr>
<tr class="odd">
<td>XUTM SNAPSHOT</td>
<td><strong>Taskman snapshot</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>SNAP^XUTMHR</strong></p></td>
<td>Schedule this option to grab a snapshot of TaskMan work counts and save them in the TASKMAN SNAPSHOT (#14.72) file. When the Task is scheduled, it takes an entry in the TASK PARAMETERS field. This is how many MINUTES to sample for, “<strong>,</strong>” and how many SECONDS to wait between samples. It has a limit of <strong>480</strong> minutes (<strong>8</strong> hours) and a minimum of <strong>2</strong> seconds to wait. At these limits it would record <strong>14400</strong> samples. It defaults to <strong>60</strong> minutes with a sample every <strong>60</strong> seconds if the TASK PARAMETERS field is <em>not</em> filled in.</td>
</tr>
<tr class="even">
<td>XUTM STOP</td>
<td><strong>Stop Task Manager</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>STOP^ZTMKU</strong></p></td>
<td>This option shuts down TaskMan.</td>
</tr>
<tr class="odd">
<td>XUTM SYNC</td>
<td><strong>SYNC flag file control</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMSYNC</strong></p></td>
<td>This option runs the SYNC flag file control.</td>
</tr>
<tr class="even">
<td>XUTM TL CLEAN</td>
<td><strong>Cleanup Task List</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ASK^XUTMRJD</strong></p></td>
<td>This option runs the Cleanup Task List.</td>
</tr>
<tr class="odd">
<td>XUTM UCI</td>
<td><strong>UCI Association Table Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option allows the system manager to edit the UCI ASSOCIATION (#14.6) file.</td>
</tr>
<tr class="even">
<td>XUTM USER</td>
<td><strong>TaskMan User</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUTMUSE</strong></p></td>
<td>This option provides end users with information about their current tasks and with the ability to stop or modify and reschedule those tasks.</td>
</tr>
<tr class="odd">
<td>XUTM UTIL</td>
<td><strong>Taskman Management Utilities</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options to assist in managing TaskMan. It includes the following options:</p>
<ul>
<li><p><strong>XUTM WAIT</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XUTM RUN</strong><br />
(DISPLAY ORDER: 6)</p></li>
<li><p><strong>XUTM STOP</strong><br />
(DISPLAY ORDER: 7)</p></li>
<li><p><strong>XUTM ERROR</strong><br />
(DISPLAY ORDER: 8)</p></li>
<li><p><strong>XUTM CLEAN</strong><br />
(DISPLAY ORDER: 9)</p></li>
<li><p><strong>XUTM CHECK ENV</strong><br />
(DISPLAY ORDER: 2)</p></li>
<li><p><strong>XUTM ZTMON</strong><br />
(SYNONYM: MTM)<br />
(DISPLAY ORDER: 1)</p></li>
<li><p><strong>XUTM PARAMETER EDIT</strong><br />
(DISPLAY ORDER: 3)</p></li>
<li><p><strong>XUTM SYNC</strong></p></li>
<li><p><strong>XUTM RP</strong></p></li>
<li><p><strong>XUTM REPNT</strong></p></li>
<li><p><strong>XUTM PROBLEM DEVICES</strong></p></li>
<li><p><strong>XUTM PROBLEM CLEAR</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUTM VOLUME</td>
<td><strong>Volume Set Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option allows the system manager to edit the Volume Set file.</td>
</tr>
<tr class="odd">
<td>XUTM WAIT</td>
<td><strong>Place Taskman in a WAIT State</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>WAIT^ZTMKU</strong></p></td>
<td>This option places TaskMan in a <strong>WAIT</strong> state, in which TaskMan is active but does <em>not</em> process any tasks, within fifteen seconds.</td>
</tr>
<tr class="even">
<td>XUTM ZTMON</td>
<td><strong>Monitor Taskman</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ZTMON</strong></p></td>
<td>This option continually monitors the status of TaskMan and its queues.</td>
</tr>
<tr class="odd">
<td>XUTTEST</td>
<td><strong>Send Test Pattern to Terminal</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>D ^%ZIS I ‘POP R “HOW MANY LINES? “,X:DTIME U IO S Y=0 X “F X=X:-1 W ! Q:’X F I=1:1:IOM W $C(I+X#96+32)” X ^%ZIS(“C”)</strong></p></td>
<td>This option prints a selected number of nonsense lines on a terminal to test data communications.</td>
</tr>
<tr class="even">
<td>XUUSERACC</td>
<td><strong>Diagram Menus</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>NORMAL^XQ4</strong></p></td>
<td>This option displays all options available to a given user, including all menus and options, according to the security and primary option.</td>
</tr>
<tr class="odd">
<td>XUUSERACC1</td>
<td><strong>Menu Diagrams</strong> (with Entry/Exit Actions)</td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>FULL^XQ4</strong></p></td>
<td><p>This option displays all options available to a given user, including all menus and options, according to the user’s security and primary option. The information displayed includes:</p>
<ul>
<li><p>Entry Actions</p></li>
<li><p>Exit Actions</p></li>
<li><p>Prohibited Times</p></li>
<li><p>Locks</p></li>
<li><p>Option Names</p></li>
<li><p>Synonyms</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XUUSERACC2</td>
<td><strong>Abbreviated Menu Diagrams</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>ABBREV^XQ4</strong></p></td>
<td>This option provides an abbreviated (Option Names, Menu Text, and Synonyms) display of all the options available to a given user, including all menus and options, according to the user’s security and primary menu.</td>
</tr>
<tr class="odd">
<td>XUUSERDISP</td>
<td><strong>Display User Characteristics</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQUSR</strong></p></td>
<td>This option displays the user’s name, location, and characteristics.</td>
</tr>
<tr class="even">
<td>XUUSERHELP</td>
<td><strong>User Help</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XQH=“XQ-USERHELP” D EN^XQH</strong></p></td>
<td>This option displays basic help information for the user.</td>
</tr>
<tr class="odd">
<td>XUUSEROPT</td>
<td><strong>User Audit Display</strong></td>
<td>Print</td>
<td></td>
<td>This option display sorts by user then by option. It also prompts for print device to generate a hard copy listing.</td>
</tr>
<tr class="even">
<td>XUUSERSTATUS</td>
<td><strong>User Status Report</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XUS91</strong></p></td>
<td>This option produces a report of the users currently signed onto this CPU and this UCI. It shows the option they are running and when they signed on, as well as their device and job numbers.</td>
</tr>
<tr class="odd">
<td>XUVERSIONEW-HELP</td>
<td><strong>Kernel New Features Help</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XQH=“XUDOC NEW FEATURES*” D EN^XQH</strong></p></td>
<td>This option directs you to a series of help frames describing the new features of Kernel.</td>
</tr>
<tr class="even">
<td>XUXREF</td>
<td><strong>List Options by Parents and Use</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ31</strong></p></td>
<td><p>This option produces a cross-reference listing of all options, showing their parents on the menu tree, detecting bad <strong>POINTER</strong>s, and showing which options have no parents. It also shows the uses of the option as a:</p>
<ul>
<li><p>Primary menu option</p></li>
<li><p>Secondary menu option</p></li>
<li><p>Tasked option</p></li>
<li><p>Combination of these.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XUXREF-2</td>
<td><strong>Show Users with a Selected primary Menu</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XQ32</strong></p></td>
<td><p>This option generates a listing of those users who have a selected option as their Primary menus option or as a Secondary menu option.</p>
<p>It does <em>not</em> show all users who might have access to a particular option. It only looks at Primary (signon) menus and top-level secondary menu options.</p></td>
</tr>
<tr class="even">
<td><span id="XUXTAD_SERVICE_SECTION_EDIT_Option" class="anchor"></span>XUXTAD SERVICE/SECTION EDIT</td>
<td><strong>Service/Section Edit</strong></td>
<td>Run Routine</td>
<td>Routine: <strong>ENTER^XUXTADSSE</strong></td>
<td><p>This option was created for the <strong>R2 ADPAC CORE MENU</strong> and allows the ADPAC to edit the CHIEF (OR SUPERVISOR) of the SERVICE/SECTION file (#49) entry. This CHIEF field value is used by the Kernel Alert software in conjunction with the CPRS PARAMETER DEFINITION <strong>ORB FORWARD SUPERVISOR</strong>.</p>
<p>When the user has not processed their clinical alert by the instance value of the <strong>ORB FORWARD SUPERVISOR</strong> parameter, the CHIEF (Or SUPERVISOR) documented in the associated SERVICE/SECTION entry will receive a notification.</p>
<p>This option allows the user to edit fields of a Service/Section record via ScreenMan. A Service/Section can be either “<strong>Open</strong>” or “<strong>Closed</strong>” and is shown in the <strong>Status</strong> field of the header section</p>
<p>This option was released with Kernel Patch XU*8.0*807.</p></td>
</tr>
<tr class="odd">
<td>XUZUSER</td>
<td><strong>User Management</strong></td>
<td>Menu</td>
<td><p>Entry Action:</p>
<p><strong>W *27,*43,!!!!!,?20,”USER EDIT MENU”,!</strong></p>
<p>Exit Action:</p>
<p><strong>W *27,*43,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</strong></p></td>
<td><p>This is a basic user management menu. It includes the following options:</p>
<ul>
<li><p><strong>XUSERDEACT</strong></p></li>
<li><p><strong>XUSERINT</strong></p></li>
<li><p><strong>XUSERNEW</strong></p></li>
<li><p><strong>XUSERREACT</strong></p></li>
<li><p><strong>XUSEREDIT</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref87259290" class="anchor"></span>Table 25: Options—Exported Toolkit Options

### Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 25</u> lists the options that are distributed with the Kernel Toolkit software “XT” namespace; listed alphabetically:

<table>
<caption><p><span id="_Ref95212468" class="anchor"></span>Table 26: Options—Kernel Purging Options</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Type</th>
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XT-BLD RTN LIST</td>
<td><strong>Routine Summary List</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>BUILD^XTRUTL</strong></p></td>
<td><p>This option creates a list of routines in a build with before and after checksums, and second line data.</p>
<p>This list can be used in a cut and paste operation when preparing a patch.</p></td>
</tr>
<tr class="even">
<td>XTCM MAIN</td>
<td><strong>Capacity Planning</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu holds all the currently available capacity management functions. It includes the following options:</p>
<ul>
<li><p><strong>KMPS SAGG MANAGER</strong></p></li>
<li><p><strong>KMP MAIL GROUP EDIT</strong><br />
(SYNONYM: CMG)</p></li>
<li><p><strong>KMPR RUM MANAGER MENU</strong><br />
(SYNONYM: RUM)</p></li>
<li><p><strong>KMPD CM TOOLS MANAGER MENU</strong><br />
(SYNONYM: TLS)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTFCE</td>
<td><strong>Flow Chart from Entry Point</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTFCE</strong></p></td>
<td>This option produces a flow chart on the terminal screen of the processing performed from the specified entry point to the termination of processing resulting from that entry point. It also permits the user to expand the code in other routines or entry points referenced by <strong>DO</strong> or <strong>GOTO</strong> commands.</td>
</tr>
<tr class="even">
<td>XTFCR</td>
<td><strong>Flow Chart Entire Routine</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTFCR</strong></p></td>
<td>This option produces a flow chart of the processing performed within a routine.</td>
</tr>
<tr class="odd">
<td>XT-KERMIT EDIT</td>
<td><strong>Edit KERMIT holding file</strong></td>
<td>Edit</td>
<td></td>
<td><p>This option allows the user to edit their own holding file.</p>
<p>They can change the name, Transfer mode, authorized viewers, and the data.</p></td>
</tr>
<tr class="even">
<td>XT-KERMIT MENU</td>
<td><strong>Kermit menu</strong></td>
<td>Menu</td>
<td><p>Entry Action:</p>
<p><strong>D INIT^XTKERM4</strong></p>
<p>Exit Action:</p>
<p><strong>D CLEAN^XTKERM4</strong></p></td>
<td><p>This is the top-level menu for Kermit functions. It gives access to the send, receive, and edit options. It includes the following options:</p>
<ul>
<li><p><strong>XT-KERMIT RECEIVE</strong><br />
(SYNONYM: R)</p></li>
<li><p><strong>XT-KERMIT SEND</strong><br />
(SYNONYM: S)</p></li>
<li><p><strong>XT-KERMIT EDIT</strong><br />
(SYNONYM: E)</p></li>
<li><p><strong>XT-KERMIT SPOOL DL</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XT-KERMIT RECEIVE</td>
<td><strong>Receive KERMIT file</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>R^XTKERMIT</strong></p></td>
<td>This option receives a file over the terminal line from a remote system in the KERMIT protocol.</td>
</tr>
<tr class="even">
<td>XT-KERMIT SEND</td>
<td><strong>Send KERMIT file</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>S^XTKERMIT</strong></p></td>
<td>This option sends a file from the host using the terminal line to a remote system in the KERMIT protocol.</td>
</tr>
<tr class="odd">
<td>XT-KERMIT SPOOL DL</td>
<td><strong>Download a Spool file entry</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>KERMIT^ZISPL</strong></p></td>
<td>This option downloads (sends) a spool document from the SPOOL DOCUMENT (#3.51) file to a local PC using the KERMIT protocol.</td>
</tr>
<tr class="even">
<td>XTLATSET</td>
<td><strong>VAX DSM Device Set-up</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTLATSET</strong></p>
<p>Entry Action:</p>
<p><strong>S DIR(0)=“Y”,DIR(“A”)=“Want to proceed”,DIR(“A”,1)=“Do not use unless you are in the startup account”,DIR(“A”,2)=“where the correct VMS files are present!”,DIR(“B”)=“No”,DIR(“?”)=“See option description” D ^DIR K DIR S:Y’=1!$D(DIRUT) XQUIT=““</strong></p></td>
<td><p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/104.png) CAUTION: Do <em>not</em> run this option without first understanding how it works and what will result. It assumes the existence of a SYSPRINT.COM file, which is a VMS command file originally distributed by the DHCP Cookbook team. The LAT$STARTUP file is also involved in the process.</p>
<p>This option runs the <strong>XTLATSET</strong> routine. The purpose is to allow system managers to keep the Kernel and VMS device tables synchronized with the least amount of effort. Those who prefer to use the VMS editor to modify the VMS device tables according to changes in the Kernel DEVICE (#3.5) file will <em>not</em> want to use this option.</p>
<p>This option can be used when first moving Kernel to a VMS environment. It can be used thereafter to rebuild the files if they are <em>not</em> in sync. When running this option, it is critical to be in the configuration that has a complete Kernel DEVICE (#3.5) file, one with all the VMS devices used by any other configuration. The VMS files that are built are automatically used at the next VMS startup.</p>
<p>This option runs the <strong>XTLATSET</strong> routine to build VMS command files to coordinate the Kernel and VMS device tables. It reads from the Kernel’s DEVICE (#3.5) file for <strong>LTA</strong> devices and writes three VMS command files:</p>
<ul>
<li><p><strong>LT_LOAD.COM</strong> file sets up printers in LATCP.</p></li>
<li><p>The LT_PRT.DAT file is read by <strong>SYSPRINT.COM</strong> to set VMS parameters for printers and other devices and can optionally set up VMS spooling.</p></li>
<li><p>The <strong>TSC_LOAD.COM</strong> file establishes printer parameters to be used in the DEC server’s device tables.</p></li>
</ul>
<p>This option is locked with the <strong>XUMGR</strong> security key.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/105.png) CAUTION: This option should be used with care. The process should be reviewed beforehand to be sure that other VMS device settings are <em>not</em> altered in an unexpected way. It is assumed that the system has been configured with knowledge of the DHCP Cookbook recommendations.</p></td>
</tr>
<tr class="odd">
<td>XTLKLKUP</td>
<td><strong>Multi-Term Lookup (MTLU)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>A^XTLKTICD</strong></p></td>
<td>This is a test lookup option. It is tests what has been entered and how the package does the lookup.</td>
</tr>
<tr class="even">
<td>XTLKMODKY</td>
<td><strong>Keywords</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XTLKOP=“Keywords” D KE^XTLKEFOP K XTLKOP</strong></p></td>
<td>This is the option that allows the user to enter/edit the LOCAL KEYWORD (#8984.1) file.</td>
</tr>
<tr class="odd">
<td>XTLKMODPARK</td>
<td><strong>Delete Entries From Look-up</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>DD^XTLKEFOP</strong></p></td>
<td><p>This option deletes entries out of the LOCAL LOOKUP (#8984.4) file. To do this, there <em>cannot</em> be any Keywords, Shortcuts, or Synonyms associated with the file to be deleted.</p>
<p>This option is locked with the <strong>XTLKZMGR</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XTLKMODPARS</td>
<td><strong>Add Entries To Look-Up File</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>LL^XTLKEFOP</strong></p></td>
<td><p>This option sets entries into the LOCAL LOOKUP (#8984.4) file.</p>
<p>This option is locked with the <strong>XTLKZMGR</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTLKMODSH</td>
<td><strong>Shortcuts</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XTLKOP=“Shortcuts” D SH^XTLKEFOP K XTLKOP</strong></p></td>
<td>This option is to enter/edit Shortcuts in the LOCAL SHORTCUT (#8984.2) file.</td>
</tr>
<tr class="even">
<td>XTLKMODSY</td>
<td><strong>Synonyms</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>S XTLKOP=“Synonyms” D SY^XTLKEFOP K XTLKOP</strong></p></td>
<td>This option is to enter/edit Synonyms in the LOCAL SYNONYM (#8984.3) file.</td>
</tr>
<tr class="odd">
<td>XTLKMODUTL</td>
<td><strong>Add/Modify Utility</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is a menu for the enter/edit options of the KEYWORD, SHORTCUT, and SYNONYM files. It includes the following options (listed in display order):</p>
<ul>
<li><p><strong>XTLKMODSH</strong><br />
(1; SYNONYM: SH)</p></li>
<li><p><strong>XTLKMODKY</strong><br />
(2; SYNONYM: KE)</p></li>
<li><p><strong>XTLKMODSY</strong><br />
(3; SYNONYM: SY)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XTLKPRTUTL</td>
<td><strong>Print Utility</strong></td>
<td>Action</td>
<td><p>Entry Action:</p>
<p><strong>D A^XTLKPRT</strong></p></td>
<td>This option prints out the Keywords, Shortcuts, and Synonyms.</td>
</tr>
<tr class="odd">
<td>XTLKUSER2</td>
<td><strong>Multi-Term Lookup Main Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the main option for the MTLU package. It includes the following options:</p>
<ul>
<li><p><strong>XTLKPRTUTL</strong></p></li>
<li><p><strong>XTLKLKUP</strong></p></li>
<li><p><strong>XTLKUTILITIES</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XTLKUTILITIES</td>
<td><strong>Utilities for MTLU</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is the utilities menu for MTLU. It includes the following options:</p>
<ul>
<li><p><strong>XTLKMODUTL</strong></p></li>
<li><p><strong>XTLKMODPARS</strong> (SYNONYM: ST)</p></li>
<li><p><strong>XTLKMODPARK</strong> (SYNONYM: KL)</p></li>
</ul>
<p>This menu is locked with the <strong>XTLKZMGR</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTMENU</td>
<td><strong>Application Utilities</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains utilities that can be used by an application programmer. It includes the following options:</p>
<ul>
<li><p><strong>XTLKUSER2</strong></p></li>
<li><p><strong>XDR MAIN MENU</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>XTMOVE</td>
<td><strong>Move Routines across Volume Sets</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTMOVE</strong></p></td>
<td><p>This option runs the <strong>%ZTMOVE</strong> routine. It moves routines from one volume set to another. A specified set of routines can be moved to a specified UCI on a different volume set in one step (automatically) or in two steps. The second step requires use of the <strong>Bring in Sent Routines</strong> [XTMOVE-IN] option in the destination UCI/Volume Set. This second option brings in the sent routines by running <strong>IN^%ZTMOVE</strong>.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTMOVE-IN</td>
<td><strong>Bring in Sent Routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>IN^%ZTMOVE</strong></p></td>
<td><p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/106.png) CAUTION: This option is only to be used after invoking the Move Routines across Volume Sets [XTMOVE] option.</p>
<p>When in the destination UCI/Volume Set, this option installs the routines that were previously sent.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XT-NUMBER BASE CHANGER</td>
<td><strong>Number base changer</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTBASE</strong></p></td>
<td><p>This option runs a number base calculator. It allows input in base <strong>2</strong>, <strong>8</strong>, <strong>10</strong>, <strong>16</strong> and displays the number in all <strong>4</strong> bases.</p>
<p>It is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTOOLS</td>
<td><strong>Programmer tools</strong></td>
<td>Menu</td>
<td></td>
<td><p>This is a menu to link and document programmer tools that are part of Kernel. Not all items will make sense to use from a menu. It includes the following options:</p>
<ul>
<li><p><strong>XT-VERSION NUMBER</strong></p></li>
<li><p><strong>XT-VARIABLE CHANGER</strong></p></li>
<li><p><strong>XT-NUMBER BASE CHANGER</strong></p></li>
<li><p><strong>XT-ROUTINE COMPARE</strong></p></li>
<li><p><strong>XTFCR</strong><br />
(SYNONYM: FCR)</p></li>
<li><p><strong>XTFCE</strong><br />
(SYNONYM: FCE)</p></li>
</ul>
<p>This menu is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XT-OPTION TEST</td>
<td><strong>Test an option not in your menu</strong></td>
<td>Action</td>
<td><p>ENTRY ACTION:</p>
<p><strong>S DIC=19,DIC(0)=“AEMQZ”,DIC(“A”)=“Option entry to test: “,DIC(“S”)=“I $P(^(0),U)’[““XUPROG”““ D ^DIC K DIC I Y&gt;0 S XQY=+Y,XQUR=$P(Y,U,2),XQDIC=“U”,XQY0=^DIC(19,XQY,0),^(“T”)=^XUTL(“XQ”,$J,”T”)-1 G M0^XQ</strong></p></td>
<td><p>This option is for in-house testing of options only. It allows the selection of an option from the OPTION (#19) file and then executes it.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/107.png) CAUTION: No security checks are performed; therefore, this option should only be given to developers.</p></td>
</tr>
<tr class="odd">
<td>XT-PURGE ERRORS</td>
<td><strong>Clean Error Trap</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTERPUR</strong></p></td>
<td><p>This option deletes old errors from the Error Trap.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XTQUEUABLE OPTIONS</td>
<td><strong>Toolkit Queuable Options</strong></td>
<td>Menu</td>
<td></td>
<td>This menu, which has no parent, collects all parentless Toolkit options that are intended to be scheduled through the TaskMan <strong>Schedule/Unschedule Options</strong> [XUTM SCHEDULE] option.</td>
</tr>
<tr class="odd">
<td>XTRDEL</td>
<td><strong>Delete Routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>%ZTRDEL</strong></p></td>
<td><p>This option runs the <strong>%ZTRDEL</strong> routine to delete one or more routines.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XTRGRPE</td>
<td><strong>Group Routine Edit</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTRGRPE</strong></p></td>
<td><p>This option calls the <strong>XTRGRPE</strong> routine to edit a group of routines. Once several routines are identified, the Kernel <strong>%Z</strong> editor is called.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTRMONITOR</td>
<td><strong>Monitor Routines for Changes</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTRMON</strong></p></td>
<td>This option schedules the <strong>XTRMON</strong> routine to Monitor routines for changes. It uses the ROUTINE MONITOR field in the KERNEL SYSTEM PARAMETERS (#8989.3) file to control if all routines or just selected <strong>N</strong>-spaces should be monitored. The checksum that is calculated is stored in the routine file along with the date that it changed. It also goes through the ROUTINE (#9.8) file and checks that all routines are still in the UCI. This keeps the ROUTINE (#9.8) file current for KIDS. The output of the routine is the <a href="#XTRMON_bulletin"><strong>XTRMON</strong></a> bulletin that is sent to the attached mail group.</td>
</tr>
<tr class="even">
<td>XT-ROUTINE COMPARE</td>
<td><strong>Compare two routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTRCMP</strong></p></td>
<td>This option compares two routines located in the current account and prints a list of differences. It uses the MailMan compare routine to do the work.</td>
</tr>
<tr class="odd">
<td>XT-RTN CS EDT</td>
<td><strong>Old Checksum Edit</strong></td>
<td>Edit</td>
<td></td>
<td>This option edits the CHECKSUM field in the ROUTINE (#9.8) file that is used by the Routine Summary List.</td>
</tr>
<tr class="even">
<td>XT-RTN CS UPDATE</td>
<td><strong>Old Checksum Update from Build</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>UPDATE^XTRUTL</strong></p></td>
<td>This option updates the old checksum of the routine in a build with the routines current checksum value. This option should be run after a patch has been released and before any new editing of the routines takes place.</td>
</tr>
<tr class="odd">
<td>XTSUMBLD</td>
<td><strong>Build an ‘NTEG’ routine for a package</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTSUMBLD</strong></p></td>
<td>This option gets a package namespace from the PACKAGE (#9.4) file. It then lists routines from the user. It then builds a <strong>&lt;<em>namespace</em>&gt;NTEG</strong> routine that has a checksum for each of the routines. This routine can be run to see if there has been any change to a routine since the <strong>NTEG</strong> routine was built.</td>
</tr>
<tr class="even">
<td>XTSUMBLD-CHECK</td>
<td><strong>Calculate and Show Checksum Values</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>CHCKSUM^XTSUMBLD</strong></p></td>
<td>This option calls <strong>CHCKSUM^XTSUMBLD</strong> to calculate and show the checksum value for one or more routines in the current account. This value is referenced in the Patch Module description for routine patches.</td>
</tr>
<tr class="odd">
<td>XTV EDIT VERIF PACKAGE</td>
<td><strong>Edit Verification Package File</strong></td>
<td>Edit</td>
<td></td>
<td>This option enters or edits files and namespaces in the PACKAGE (#9.4) file.</td>
</tr>
<tr class="even">
<td>XTV MENU</td>
<td><strong>Verifier Tools Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options that are available as tools for verification during program development. It includes the following options:</p>
<ul>
<li><p><strong>XTVR COMPARE</strong><br />
(DISPLAY ORDER: 20)</p></li>
<li><p><strong>XTVR UPDATE</strong><br />
(DISPLAY ORDER: 5)</p></li>
<li><p><strong>XTVG COMPARE</strong></p></li>
<li><p><strong>XTVG UPDATE</strong></p></li>
<li><p><strong>XTV EDIT VERIF PACKAGE</strong></p></li>
<li><p><strong>XTVR MOST RECENT CHANGE DATE</strong></p></li>
<li><p><strong>XTVR RESTORE PREV ROUTINE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XT-VARIABLE CHANGER</td>
<td><strong>Variable changer</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVCHG</strong></p></td>
<td><p>This option runs the <strong>XTVCHG</strong> routine that does a fair job of changing all occurrences of a variable to another. It changes <strong>DO</strong>s and <strong>GOTO</strong>s also but does <em>not</em> change the TAG.</p>
<p>This option is locked with the <strong>XUPROGMODE</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XT-VERSION NUMBER</td>
<td><strong>Version Number Update</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVNUM</strong></p></td>
<td>This option runs the <strong>XTVNUM</strong> routine that updates or sets the version number into a set of routines.</td>
</tr>
<tr class="odd">
<td>XTVG COMPARE</td>
<td><strong>Global Compare for selected package</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVGC2</strong></p></td>
<td>This option produces a listing of changes in the global structure; including file protection and templates, and a previously stored version of the package (using the <strong>Accumulate Global</strong> [XTVGC UPDATE] option).</td>
</tr>
<tr class="even">
<td>XTVG UPDATE</td>
<td><strong>Accumulate Globals for Package</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVGC1</strong></p></td>
<td>This option accumulates the current globals for a package for comparison with subsequent versions. The global data is accumulated for the <strong>^DIC(<em>fn</em>,0, the ^DD(<em>fn</em>,</strong> nodes where <em><strong>fn</strong></em> is an included file number), and the Edit, Print, and Sort templates for the files indicated as related to the package in the PACKAGE (#9.4) file.</td>
</tr>
<tr class="odd">
<td>XTVR COMPARE</td>
<td><strong>Routine Compare - Current with Previous</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVRC2</strong></p></td>
<td>This option compares one or more current routines to previous versions that have been recorded using the Update with current routines option. Differences between the current version and the indicated number of prior versions are noted.</td>
</tr>
<tr class="even">
<td>XTVR MENU</td>
<td><strong>Verifier Tools Menu</strong></td>
<td>Menu</td>
<td></td>
<td><p>This menu contains options that are available as tools for verification during program development. It includes the following options:</p>
<ul>
<li><p><strong>XTVR COMPARE</strong><br />
(DISPLAY ORDER: 20)</p></li>
<li><p><strong>XTVR UPDATE</strong><br />
(DISPLAY ORDER: 5)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVR MOST RECENT CHANGE DATE</td>
<td><strong>Last Routine Change Date Recorded</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVRC1A</strong></p></td>
<td><p>This option lists the most recent date on which a change was recorded for the selected routines. The date piece of the first line of the routine and version and patch information are also displayed. The version number can be changed, and the routine recorded after that date, but the last change date recorded is that date involving a change in more than the second (version number) line.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/108.png) CAUTION: The Update Routine option <em>must</em> have been used one or more times to record the routine and changes to the routine.</p></td>
</tr>
<tr class="even">
<td>XTVR RESTORE PREV ROUTINE</td>
<td><strong>UNDO Edits (Restore to Older Version of Routine)</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVRCRE</strong></p></td>
<td>This option restores a routine back to a previous version that is available in the previous version edits shown by the <strong>Routine Compare</strong> option. The user <em>must</em> specify a routine name to be used for the restored routine that is <em>not</em> currently used, so that no current routine is destroyed because of saving the newly restored routine. After checking that the restored routine is the desired version, the user can rename it as desired.</td>
</tr>
<tr class="odd">
<td>XTVR UPDATE</td>
<td><strong>Update with current routines</strong></td>
<td>Run Routine</td>
<td><p>Routine:</p>
<p><strong>XTVRC1</strong></p></td>
<td>This option records the text of the routines indicated in the file used to maintain changes in routines. Only the last version entered is kept completely, previous entries reflect only the changes in lines added and/or deleted to make the next version. This option records the current routine structure, so that it can be compared with future versions of the routine using the <strong>Routine Compare - Current with Previous</strong> [XTVR COMPARE] option.</td>
</tr>
</tbody>
</table>

<span id="_Ref95212468" class="anchor"></span>Table 26: Options—Kernel Purging Options

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific archiving procedures or recommendations for Kernel or Kernel Toolkit.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides several options to facilitate the purging of Kernel files and the cleanup of Kernel-produced globals. <u>Table 26</u> contains a list of the purging options. The recommended scheduling frequency is shown for some options; all such options are queueable. The Clear All Users at Startup option requires special queueing.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/109.png) REF: The location of a detailed discussion of each option is given in <u>Table 26</u>; unless otherwise noted, the reference given is to a section in the [*Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf).

| Purging Option                               | Frequency    | References for More Information                                                                                                                                                                                                              |
|----------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Audited Options Purge                    |              | Menu Manager: System Management” section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf) and *Kernel Security Tools Manual.*        |
| Automatic Deactivation of Users          | 1 day    | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf)                                    |
| Clean Error Log over Range of Dates      |              | TaskMan: System Management—Operation section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)                                                  |
| Clean Old Job Nodes in ^XUTL             | 7 days   | Menu Management: System Management section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf)                                          |
| Clean Task File                          |              | TaskMan: System Management—Operation section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)                                                  |
| Clear All Users at Startup               |              | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf)                                    |
| Clean Error Trap                         |              | Error Processing section in the [*Kernel 8.0 Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf)                                                                  |
| Deactivate a User                        |              | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf)                                    |
| Delete Error Log                         |              | TaskMan: System Management—Operation section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)                                                  |
| Delete Old (\>14 d) Alerts               | 1 day    | Alerts section in the [*Kernel 8.0 Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf)                                                                            |
| Failed Access Attempts Log Purge         |              | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf) and *Kernel Security Tools Manual* |
| Programmer Mode Entry Log Purge          |              | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf) and *Kernel Security Tools Manual* |
| Purge Error Log of Type of Error         |              | TaskMan: System Management—Operation section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)                                                  |
| Purge Inactive Users’ Attributes         |              | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Toolkit User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.pdf)                                                    |
| Purge Log of Old Access and Verify Codes | (up to site) | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf) and *Kernel Security Tools Manual* |
| Purge of ^%ZUA Global                    | 15 days  | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf)                                    |
| Purge Old Spool Documents                | 7 days   | Spooling section in the [*Kernel 8.0 Systems Management: Device Handler User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf)                                                                |
| Purge Sign-on Log                        | 1 day    | Signon/Security: System Management section in the [*Kernel 8.0 Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf) and *Kernel Security Tools Manual* |
| Queuable Task Log Cleanup                | 1 day    | TaskMan: System Management—Operation section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)                                                  |

<span id="_Ref333475931" class="anchor"></span>Table 27: Kernel and Kernel Toolkit APIs (Callable Entry Points)—Supported and Controlled Subscription

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/110.png) REF: The “KIDS: System Management—Installations” chapter in the [*Kernel 8.0 Systems Management: KIDS User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf) contains recommendations for purging the INSTALL (#9.7) and BUILD (#9.6) files.

# Callable Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists all callable entry points (that is Application Program Interfaces \[APIs\]) that are available for general use with Kernel and Kernel Toolkit (that is supported or controlled subscription).

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/111.png) NOTE: A set of nodes is created during Kernel’s installation that contains operating system-specific code. These nodes are descendent from ^%ZOSF. Most can be executed in application code.  
  
REF: Each operating system node is described in the “Operating System Interface: Programmer Tools” chapter in the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

<u>Table 27</u> lists the Kernel and Kernel Toolkit APIs. It includes the routine name, tag entry point, Integration Control Registration (ICR) number, if any, and a brief description.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/112.png) REF: Every API and executable node is described in detail in the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*. Refer to the appropriate section in that manual for details, including input and output parameters/variables for each API.

<table>
<caption><p><span id="_Ref333475968" class="anchor"></span>Table 28: Direct Mode Utilities</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Entry Point</th>
<th>ICR #</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MXMLDOM</strong></td>
<td>$$ATTRIB</td>
<td>3561</td>
<td>XML—Get Attribute Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$CHILD</td>
<td>3561</td>
<td>XML—Get Child Node</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CMNT</td>
<td>3561</td>
<td>XML—Extract Comment Text (True/False)</td>
</tr>
<tr class="even">
<td></td>
<td>CMNT</td>
<td>3561</td>
<td>XML—Extract Comment Text (True/False)</td>
</tr>
<tr class="odd">
<td></td>
<td>DELETE</td>
<td>3561</td>
<td>XML—Delete Document Instance</td>
</tr>
<tr class="even">
<td></td>
<td>$$EN</td>
<td>3561</td>
<td>XML—Initial Processing, Build In-memory Image</td>
</tr>
<tr class="odd">
<td></td>
<td>$$NAME</td>
<td>3561</td>
<td>XML—Get Element Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$PARENT</td>
<td>3561</td>
<td>XML—Get Parent Node</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SIBLING</td>
<td>3561</td>
<td>XML—Get Sibling Node</td>
</tr>
<tr class="even">
<td></td>
<td>$$TEXT</td>
<td>3561</td>
<td>XML—Get Text (True/False)</td>
</tr>
<tr class="odd">
<td></td>
<td>TEXT</td>
<td>3561</td>
<td>XML—Get Text (True/False)</td>
</tr>
<tr class="even">
<td></td>
<td>$$VALUE</td>
<td>3561</td>
<td>XML—Get Attribute Value</td>
</tr>
<tr class="odd">
<td><strong>MXMLPRSE</strong></td>
<td>EN</td>
<td>4149</td>
<td>XML—Event Driven API</td>
</tr>
<tr class="even">
<td><strong>MXMLUTL</strong></td>
<td>$$SYMENC</td>
<td>4153</td>
<td>XML—Encoded Strings in Messages</td>
</tr>
<tr class="odd">
<td></td>
<td>$$XMLHDR</td>
<td>4153</td>
<td>XML—Message Headers</td>
</tr>
<tr class="even">
<td><strong>XGF</strong></td>
<td>CHGA</td>
<td>3173</td>
<td>Screen Change Attributes</td>
</tr>
<tr class="odd">
<td></td>
<td>CLEAN</td>
<td>3173</td>
<td>Screen/Keyboard Exit and Cleanup</td>
</tr>
<tr class="even">
<td></td>
<td>CLEAR</td>
<td>3173</td>
<td>Screen Clear Region</td>
</tr>
<tr class="odd">
<td></td>
<td>FRAME</td>
<td>3173</td>
<td>Screen Frame</td>
</tr>
<tr class="even">
<td></td>
<td>INITKB</td>
<td>3173</td>
<td>Keyboard Setup Only</td>
</tr>
<tr class="odd">
<td></td>
<td>IOXY</td>
<td>3173</td>
<td>Screen Cursor Placement</td>
</tr>
<tr class="even">
<td></td>
<td>PREP</td>
<td>3173</td>
<td>Screen/Keyboard Setup</td>
</tr>
<tr class="odd">
<td></td>
<td>$$READ</td>
<td>3173</td>
<td>Read Using Escape Processing</td>
</tr>
<tr class="even">
<td></td>
<td>RESETKB</td>
<td>3173</td>
<td>Exit XGF Keyboard</td>
</tr>
<tr class="odd">
<td></td>
<td>RESTORE</td>
<td>3173</td>
<td>Screen Restore</td>
</tr>
<tr class="even">
<td></td>
<td>SAVE</td>
<td>3173</td>
<td>Screen Save</td>
</tr>
<tr class="odd">
<td></td>
<td>SAY</td>
<td>3173</td>
<td>Screen String</td>
</tr>
<tr class="even">
<td></td>
<td>SAYU</td>
<td>3173</td>
<td>Screen String with Attributes</td>
</tr>
<tr class="odd">
<td></td>
<td>SETA</td>
<td>3173</td>
<td>Screen Video Attributes</td>
</tr>
<tr class="even">
<td></td>
<td>WIN</td>
<td>3173</td>
<td>Screen Text Window</td>
</tr>
<tr class="odd">
<td rowspan="5"><strong>XIPUTIL</strong></td>
<td>CCODE</td>
<td>3618</td>
<td>FIPS Code Data</td>
</tr>
<tr class="even">
<td>$$FIPS</td>
<td>3618</td>
<td>FIPS Code for ZIP Code</td>
</tr>
<tr class="odd">
<td>$$FIPSCHK</td>
<td>3618</td>
<td>Check for FIPS Code</td>
</tr>
<tr class="even">
<td>POSTAL</td>
<td>3618</td>
<td>ZIP Code Information</td>
</tr>
<tr class="odd">
<td>POSTALB</td>
<td>3618</td>
<td>Active ZIP Codes</td>
</tr>
<tr class="even">
<td rowspan="2"><strong>XLFCRC</strong></td>
<td>$$CRC16</td>
<td>3156</td>
<td>Cyclic Redundancy Code <strong>16</strong></td>
</tr>
<tr class="odd">
<td>$$CRC32</td>
<td>3156</td>
<td>Cyclic Redundancy Code <strong>32</strong></td>
</tr>
<tr class="even">
<td><strong>XLFDT</strong></td>
<td>$$%H</td>
<td>10103</td>
<td>Convert Seconds to <strong>$H</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>$$DOW</td>
<td>10103</td>
<td>Day of Week</td>
</tr>
<tr class="even">
<td></td>
<td>$$DT</td>
<td>10103</td>
<td>Current Date (FM Date Format)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FMADD</td>
<td>10103</td>
<td>VA FileMan Date Add</td>
</tr>
<tr class="even">
<td></td>
<td>$$FMDIFF</td>
<td>10103</td>
<td>VA FileMan Date Difference</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FMTE</td>
<td>10103</td>
<td>Convert FM Date to External Format</td>
</tr>
<tr class="even">
<td></td>
<td>$$FMTH</td>
<td>10103</td>
<td>Convert FM Date to <strong>$H</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>$$FMTHL7</td>
<td>10103</td>
<td>Convert FM Date to HL7 Date</td>
</tr>
<tr class="even">
<td></td>
<td>$$HADD</td>
<td>10103</td>
<td><strong>$H</strong> Add</td>
</tr>
<tr class="odd">
<td></td>
<td>$$HDIFF</td>
<td>10103</td>
<td><strong>$H</strong> Difference</td>
</tr>
<tr class="even">
<td></td>
<td>$$HL7TFM</td>
<td>10103</td>
<td>Convert HL7 Date to FM Date</td>
</tr>
<tr class="odd">
<td></td>
<td>$$HTE</td>
<td>10103</td>
<td>Convert <strong>$H</strong> to External Format</td>
</tr>
<tr class="even">
<td></td>
<td>$$HTFM</td>
<td>10103</td>
<td>Convert <strong>$H</strong> to FM Date Format</td>
</tr>
<tr class="odd">
<td></td>
<td>$$NOW</td>
<td>10103</td>
<td>Current Date &amp; Time (FM Format)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SCH</td>
<td>10103</td>
<td>Next Scheduled Runtime</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SEC</td>
<td>10103</td>
<td>Convert <strong>$H</strong>/FM date to Seconds</td>
</tr>
<tr class="even">
<td></td>
<td>$$TZ</td>
<td>10103</td>
<td>Time Zone Offset (GMT)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$WITHIN</td>
<td>NONE</td>
<td>Checks Dates/Times Within Schedule</td>
</tr>
<tr class="even">
<td><strong>XLFHYPER</strong></td>
<td>$$ACOSH</td>
<td>10144</td>
<td>Hyperbolic Arc-cosine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ACOTH</td>
<td>10144</td>
<td>Hyperbolic Arc-cotangent</td>
</tr>
<tr class="even">
<td></td>
<td>$$ACSCH</td>
<td>10144</td>
<td>Hyperbolic Arc-cosecant</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ASECH</td>
<td>10144</td>
<td>Hyperbolic Arc-secant</td>
</tr>
<tr class="even">
<td></td>
<td>$$ASINH</td>
<td>10144</td>
<td>Hyperbolic Arc-sine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ATANH</td>
<td>10144</td>
<td>Hyperbolic Arc-tangent</td>
</tr>
<tr class="even">
<td></td>
<td>$$COSH</td>
<td>10144</td>
<td>Hyperbolic Cosine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$COTH</td>
<td>10144</td>
<td>Hyperbolic Cotangent</td>
</tr>
<tr class="even">
<td></td>
<td>$$CSCH</td>
<td>10144</td>
<td>Hyperbolic Cosecant</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SECH</td>
<td>10144</td>
<td>Hyperbolic Secant</td>
</tr>
<tr class="even">
<td></td>
<td>$$SINH</td>
<td>10144</td>
<td>Hyperbolic Sine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TANH</td>
<td>10144</td>
<td>Hyperbolic Tangent</td>
</tr>
<tr class="even">
<td><strong>XLFIPV</strong></td>
<td>SSCONVERT</td>
<td>5844</td>
<td>Convert any IP Address to Standardized IP Address</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FORCEIP4</td>
<td>5844</td>
<td>Convert any IP Address to IPv4</td>
</tr>
<tr class="even">
<td></td>
<td>$$FORCEIP6</td>
<td>5844</td>
<td>Convert any IP Address to IPv6</td>
</tr>
<tr class="odd">
<td></td>
<td>$$VALIDATE</td>
<td>5844</td>
<td>Validate IP Address Format</td>
</tr>
<tr class="even">
<td></td>
<td>$$VERSION</td>
<td>5844</td>
<td>Show System Settings for IPv6</td>
</tr>
<tr class="odd">
<td><strong>XLFMSMT</strong></td>
<td>$$BSA</td>
<td>3175 &amp; 10143</td>
<td>Body Surface Area</td>
</tr>
<tr class="even">
<td></td>
<td>$$LENGTH</td>
<td>3175 &amp; 10143</td>
<td>Convert Length</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TEMP</td>
<td>3175 &amp; 10143</td>
<td>Convert Temperature</td>
</tr>
<tr class="even">
<td></td>
<td>$$VOLUME</td>
<td>3175 &amp; 10143</td>
<td>Convert Volume</td>
</tr>
<tr class="odd">
<td></td>
<td>$$WEIGHT</td>
<td>3175 &amp; 10143</td>
<td>Convert Weight</td>
</tr>
<tr class="even">
<td><strong>XLFMTH</strong></td>
<td>$$ABS</td>
<td>10105</td>
<td>Absolute Value</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ACOS</td>
<td>10105</td>
<td>Arc-cosine (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ACOSDEG</td>
<td>10105</td>
<td>Arc-cosine (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ACOT</td>
<td>10105</td>
<td>Arc-cotangent (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ACOTDEG</td>
<td>10105</td>
<td>Arc-cotangent (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ACSC</td>
<td>10105</td>
<td>Arc-cosecant (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ACSCDEG</td>
<td>10105</td>
<td>Arc-cosecant (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ASEC</td>
<td>10105</td>
<td>Arc-secant (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ASECDEG</td>
<td>10105</td>
<td>Arc-secant (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ASIN</td>
<td>10105</td>
<td>Arc-sine (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ASINDEG</td>
<td>10105</td>
<td>Arc-sine (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ATAN</td>
<td>10105</td>
<td>Arc-tangent (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$ATANDEG</td>
<td>10105</td>
<td>Arc-tangent (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$COS</td>
<td>10105</td>
<td>Cosine (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$COSDEG</td>
<td>10105</td>
<td>Cosine (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$COT</td>
<td>10105</td>
<td>Cotangent (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$COTDEG</td>
<td>10105</td>
<td>Cotangent (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CSC</td>
<td>10105</td>
<td>Cosecant (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$CSCDEG</td>
<td>10105</td>
<td>Cosecant (Degrees)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$DECDMS</td>
<td>10105</td>
<td>Conv. Decimals to Degrees:Minutes:Seconds</td>
</tr>
<tr class="even">
<td></td>
<td>$$DMSDEC</td>
<td>10105</td>
<td>Conv. Degrees:Minutes:Seconds to Decimal</td>
</tr>
<tr class="odd">
<td></td>
<td>$$DTR</td>
<td>10105</td>
<td>Convert Degrees to Radians</td>
</tr>
<tr class="even">
<td></td>
<td>$$E</td>
<td>10105</td>
<td>e—Natural Logarithm</td>
</tr>
<tr class="odd">
<td></td>
<td>$$EXP</td>
<td>10105</td>
<td>e—Natural Logarithm to the Nth Power</td>
</tr>
<tr class="even">
<td></td>
<td>$$LN</td>
<td>10105</td>
<td>Natural Log (Base <strong>e</strong>)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LOG</td>
<td>10105</td>
<td>Logarithm (Base <strong>10</strong>)</td>
</tr>
<tr class="even">
<td></td>
<td>$$MAX</td>
<td>10105</td>
<td>Maximum of <strong>2</strong> Numbers</td>
</tr>
<tr class="odd">
<td></td>
<td>$$MIN</td>
<td>10105</td>
<td>Minimum of <strong>2</strong> Numbers</td>
</tr>
<tr class="even">
<td></td>
<td>$$PI</td>
<td>10105</td>
<td>PI</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PWR</td>
<td>10105</td>
<td><strong>X</strong> to the <strong>Y</strong> Power</td>
</tr>
<tr class="even">
<td></td>
<td>$$RTD</td>
<td>10105</td>
<td>Convert Radians to Degrees</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SD</td>
<td>10105</td>
<td>Standard Deviation</td>
</tr>
<tr class="even">
<td></td>
<td>$$SEC</td>
<td>10105</td>
<td>Secant (Radians)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SECDEG</td>
<td>10105</td>
<td>Secant (Degrees)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SIN</td>
<td>10105</td>
<td>Sine (Radians)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SINDEG</td>
<td>10105</td>
<td>Sine (Degrees)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SQRT</td>
<td>10105</td>
<td>Square Root</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TAN</td>
<td>10105</td>
<td>Tangent (Radians)</td>
</tr>
<tr class="even">
<td></td>
<td>$$TANDEG</td>
<td>10105</td>
<td>Tangent (Degrees)</td>
</tr>
<tr class="odd">
<td><strong>XLFNAME</strong></td>
<td>$$BLDNAME</td>
<td>3065</td>
<td>Build Name from Component Parts</td>
</tr>
<tr class="even">
<td></td>
<td>$$CLEANC</td>
<td>3065</td>
<td>Name Component Std. Routine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FMNAME</td>
<td>3065</td>
<td>Convert HL7 Formatted Name to Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$HLNAME</td>
<td>3065</td>
<td>Convert Name to HL7 Formatted Name</td>
</tr>
<tr class="odd">
<td></td>
<td>NAMECOMP</td>
<td>3065</td>
<td>Component Parts from Standard Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$NAMEFMT</td>
<td>3065</td>
<td>Formatted Name from Name Components</td>
</tr>
<tr class="odd">
<td></td>
<td>STDNAME</td>
<td>3065</td>
<td>Name Standardization Routine</td>
</tr>
<tr class="even">
<td><strong>XLFNAME2</strong></td>
<td>DELCOMP</td>
<td>3066</td>
<td>Delete Name Components Entry<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td></td>
<td>UPDCOMP</td>
<td>3066</td>
<td>Update Name Components Entry<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XLFNSLK</strong></td>
<td>$$ADDRESS</td>
<td>3056</td>
<td>Conversion (Domain Name to IP Addresses)</td>
</tr>
<tr class="odd">
<td></td>
<td>MAIL</td>
<td>3056</td>
<td>Get IP Addresses for a Domain Name</td>
</tr>
<tr class="even">
<td><strong>XLFSHAN</strong></td>
<td>$$AND</td>
<td>6157</td>
<td>Bitwise Logical AND</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CPUTIME</td>
<td>6157</td>
<td>Return System and User CPU Time</td>
</tr>
<tr class="even">
<td></td>
<td>$$ETIMEMS</td>
<td>6157</td>
<td>Return Elapsed Time in Milliseconds</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FILE</td>
<td>6157</td>
<td>Returns SHA Hash for Specified FileMan File or Subfile Entry</td>
</tr>
<tr class="even">
<td></td>
<td>$$GLOBAL</td>
<td>6157</td>
<td>Returns SHA Hash for a Global</td>
</tr>
<tr class="odd">
<td></td>
<td>$$HOSTFILE</td>
<td>6157</td>
<td>Returns SHA Hash for Specified Host File</td>
</tr>
<tr class="even">
<td></td>
<td>$$LSHAN</td>
<td>6157</td>
<td>Returns SHA Hash for a Long Message</td>
</tr>
<tr class="odd">
<td></td>
<td>$$OR</td>
<td>6157</td>
<td>Bitwise Logical OR</td>
</tr>
<tr class="even">
<td></td>
<td>$$ROUTINE</td>
<td>6157</td>
<td>Returns SHA Hash for a VistA Routine</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SHAN</td>
<td>6157</td>
<td>Returns SHA Hash for a Message</td>
</tr>
<tr class="even">
<td></td>
<td>$$XOR</td>
<td>6157</td>
<td>Bitwise Logical XOR</td>
</tr>
<tr class="odd">
<td><strong>XLFSTR</strong></td>
<td>$$CJ</td>
<td>10104</td>
<td>Center Justify String</td>
</tr>
<tr class="even">
<td></td>
<td>$$INVERT</td>
<td>10104</td>
<td>Invert String</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LJ</td>
<td>10104</td>
<td>Left Justify String</td>
</tr>
<tr class="even">
<td></td>
<td>$$LOW</td>
<td>10104</td>
<td>Convert String to Lowercase</td>
</tr>
<tr class="odd">
<td></td>
<td>$$REPEAT</td>
<td>10104</td>
<td>Repeat String</td>
</tr>
<tr class="even">
<td></td>
<td>$$REPLACE</td>
<td>10104</td>
<td>Replace Strings</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RJ</td>
<td>10104</td>
<td>Right Justify String</td>
</tr>
<tr class="even">
<td></td>
<td>$$SENTENCE</td>
<td>10104</td>
<td>Convert String to Sentence Case</td>
</tr>
<tr class="odd">
<td></td>
<td>$$STRIP</td>
<td>10104</td>
<td>Strip a String</td>
</tr>
<tr class="even">
<td></td>
<td>$$TITLE</td>
<td>10104</td>
<td>Convert String to Title Case</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TRIM</td>
<td>10104</td>
<td>Trim String</td>
</tr>
<tr class="even">
<td></td>
<td>$$UP</td>
<td>10104</td>
<td>Convert String to Uppercase</td>
</tr>
<tr class="odd">
<td><strong>XLFUTL</strong></td>
<td>$$BASE</td>
<td>2622</td>
<td>Convert Between Two Bases</td>
</tr>
<tr class="even">
<td></td>
<td>$$CCD</td>
<td>2622</td>
<td>Append Check Digit</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CNV</td>
<td>2622</td>
<td>Convert Base <strong>10</strong> to Another Base</td>
</tr>
<tr class="even">
<td></td>
<td>$$DEC</td>
<td>2622</td>
<td>Convert Another Base to Base <strong>10</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>$$VCD</td>
<td>2622</td>
<td>Verify Integrity</td>
</tr>
<tr class="even">
<td><strong>^XPAR</strong></td>
<td>ADD</td>
<td>2263</td>
<td>Add Parameter Value</td>
</tr>
<tr class="odd">
<td></td>
<td>CHG</td>
<td>2263</td>
<td>Change Parameter Value</td>
</tr>
<tr class="even">
<td></td>
<td>DEL</td>
<td>2263</td>
<td>Delete Parameter Value</td>
</tr>
<tr class="odd">
<td></td>
<td>EN</td>
<td>2263</td>
<td>Add, Change, Delete Parameters</td>
</tr>
<tr class="even">
<td></td>
<td>ENVAL</td>
<td>2263</td>
<td>Return All Parameter Instances</td>
</tr>
<tr class="odd">
<td></td>
<td>$$GET</td>
<td>2263</td>
<td>Return an Instance of a Parameter</td>
</tr>
<tr class="even">
<td></td>
<td>GETLST</td>
<td>2263</td>
<td>Return All Instances of a Parameter</td>
</tr>
<tr class="odd">
<td></td>
<td>GETWP</td>
<td>2263</td>
<td>Return Word-Processing Text</td>
</tr>
<tr class="even">
<td></td>
<td>NDEL</td>
<td>2263</td>
<td>Delete All Instances of a Parameter</td>
</tr>
<tr class="odd">
<td></td>
<td>PUT</td>
<td>2263</td>
<td>Add/Update Parameter Instance</td>
</tr>
<tr class="even">
<td></td>
<td>REP</td>
<td>2263</td>
<td>Replace Instance Value</td>
</tr>
<tr class="odd">
<td><strong>XPAREDIT</strong></td>
<td>BLDLST</td>
<td>2336</td>
<td>Return All Entities of a Parameter</td>
</tr>
<tr class="even">
<td></td>
<td>EDIT</td>
<td>2336</td>
<td>Edit Instance and Value of a Parameter</td>
</tr>
<tr class="odd">
<td></td>
<td>EDITPAR</td>
<td>2336</td>
<td>Edit Single Parameter</td>
</tr>
<tr class="even">
<td></td>
<td>EN</td>
<td>2336</td>
<td>Parameter Edit Prompt</td>
</tr>
<tr class="odd">
<td></td>
<td>GETENT</td>
<td>2336</td>
<td>Prompt for Entity Based on Parameter</td>
</tr>
<tr class="even">
<td></td>
<td>GETPAR</td>
<td>2336</td>
<td>Select Parameter Definition File</td>
</tr>
<tr class="odd">
<td></td>
<td>TED</td>
<td>2336</td>
<td>Edit Template Parameters (No Dash Dividers)</td>
</tr>
<tr class="even">
<td></td>
<td>TEDH</td>
<td>2336</td>
<td>Edit Template Parameters (with Dash Dividers)</td>
</tr>
<tr class="odd">
<td><strong>XPDID</strong></td>
<td>EXIT</td>
<td>2172</td>
<td>Progress Bar Emulator: Restore Screen, Clean Up Variables, and Display Text</td>
</tr>
<tr class="even">
<td></td>
<td>INIT</td>
<td>2172</td>
<td>Progress Bar Emulator: Initialize Device and Draw Box Borders</td>
</tr>
<tr class="odd">
<td></td>
<td>TITLE</td>
<td>2172</td>
<td>Progress Bar Emulator: Display Title Text</td>
</tr>
<tr class="even">
<td></td>
<td>UPDATE</td>
<td>2172</td>
<td>Update KIDS Install Progress Bar</td>
</tr>
<tr class="odd">
<td><strong>XPDIJ</strong></td>
<td>EN</td>
<td>2243</td>
<td>Task Off KIDS Install<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XPDIP</strong></td>
<td>$$PKGPAT</td>
<td>2067</td>
<td>Update Patch History</td>
</tr>
<tr class="odd">
<td><strong>XPDKEY</strong></td>
<td>DEL</td>
<td>1367</td>
<td>Delete Security Key</td>
</tr>
<tr class="even">
<td></td>
<td>$$LKUP</td>
<td>1367</td>
<td>Look Up Security Key Value</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RENAME</td>
<td>1367</td>
<td>Rename Security Key</td>
</tr>
<tr class="even">
<td><strong>XPDMENU</strong></td>
<td>$$ADD</td>
<td>1157</td>
<td>Add Option to Menu</td>
</tr>
<tr class="odd">
<td></td>
<td>DELETE</td>
<td>1157</td>
<td>Delete Menu Item</td>
</tr>
<tr class="even">
<td></td>
<td>LKOPT</td>
<td>1157</td>
<td>Look Up Option IEN</td>
</tr>
<tr class="odd">
<td></td>
<td>LOCK</td>
<td>1157</td>
<td>Set LOCK Field in OPTION File</td>
</tr>
<tr class="even">
<td></td>
<td>OUT</td>
<td>1157</td>
<td>Edit Option’s Out of Order Message</td>
</tr>
<tr class="odd">
<td></td>
<td>RENAME</td>
<td>1157</td>
<td>Rename Option</td>
</tr>
<tr class="even">
<td></td>
<td>RLOCK</td>
<td>1157</td>
<td>Set REVERSE/NEGATIVE Field in OPTION File</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TYPE</td>
<td>1157</td>
<td>Get Option Type</td>
</tr>
<tr class="even">
<td><strong>XPDPROT</strong></td>
<td>$$ADD</td>
<td>5567</td>
<td>Add Child Protocol to Parent Protocol</td>
</tr>
<tr class="odd">
<td></td>
<td>$$DELETE</td>
<td>5567</td>
<td>Delete Child Protocol from Parent Protocol</td>
</tr>
<tr class="even">
<td></td>
<td>FIND</td>
<td>5567</td>
<td>Find All Parents for a Protocol</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LKPROT</td>
<td>5567</td>
<td>Look Up Protocol IEN</td>
</tr>
<tr class="even">
<td></td>
<td>OUT</td>
<td>5567</td>
<td>Edit Protocol’s Out of Order Message</td>
</tr>
<tr class="odd">
<td></td>
<td>RENAME</td>
<td>5567</td>
<td>Rename Protocol</td>
</tr>
<tr class="even">
<td></td>
<td>$$TYPE</td>
<td>5567</td>
<td>Get Protocol Type</td>
</tr>
<tr class="odd">
<td><strong>XPDUTL</strong></td>
<td>BMES</td>
<td>10141</td>
<td>Output Message with Blank Line</td>
</tr>
<tr class="even">
<td></td>
<td>$$COMCP</td>
<td>10141</td>
<td>Complete Checkpoint</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CURCP</td>
<td>10141</td>
<td>Get Current Checkpoint Name/IEN</td>
</tr>
<tr class="even">
<td></td>
<td>$$INSTALDT</td>
<td>10141</td>
<td>Return All Install Dates/Times</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LAST</td>
<td>10141</td>
<td>Last Software Patch</td>
</tr>
<tr class="even">
<td></td>
<td>MES</td>
<td>10141</td>
<td>Output a Message</td>
</tr>
<tr class="odd">
<td></td>
<td>$$NEWCP</td>
<td>10141</td>
<td>Create a Checkpoint</td>
</tr>
<tr class="even">
<td></td>
<td>$$OPTDE</td>
<td>10141</td>
<td>Disable/Enable an Option</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PARCP</td>
<td>10141</td>
<td>Get Checkpoint Parameter</td>
</tr>
<tr class="even">
<td></td>
<td>$$PATCH</td>
<td>10141</td>
<td>Verify Patch Installation</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PKG</td>
<td>10141</td>
<td>Parse Software Name from Build Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$PRODE</td>
<td>10141</td>
<td>Disable/Enable a Protocol</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RTNUP</td>
<td>10141</td>
<td>Update Routine Action</td>
</tr>
<tr class="even">
<td></td>
<td>$$UPCP</td>
<td>10141</td>
<td>Update Checkpoint</td>
</tr>
<tr class="odd">
<td></td>
<td>$$VER</td>
<td>10141</td>
<td>Parse Version from Build Name</td>
</tr>
<tr class="even">
<td></td>
<td>$$VERCP</td>
<td>10141</td>
<td>Verify Checkpoint</td>
</tr>
<tr class="odd">
<td></td>
<td>$$VERSION</td>
<td>10141</td>
<td>PACKAGE File Current Version</td>
</tr>
<tr class="even">
<td><strong>XQ92</strong></td>
<td>NEXT</td>
<td>10077</td>
<td>Restricted Times Check</td>
</tr>
<tr class="odd">
<td><strong>XQALBUTL</strong></td>
<td>AHISTORY</td>
<td>2788</td>
<td>Get Alert Tracking File Information</td>
</tr>
<tr class="even">
<td></td>
<td>ALERTDAT</td>
<td>2788</td>
<td>Get Alert Tracking File Information</td>
</tr>
<tr class="odd">
<td></td>
<td>DELSTAT</td>
<td>3197</td>
<td>Get User Information and Status for Recent Alert</td>
</tr>
<tr class="even">
<td></td>
<td>NOTIPURG</td>
<td>3010</td>
<td>Purge Alerts Based on Code</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PENDING</td>
<td>2788</td>
<td>Pending Alerts for a User</td>
</tr>
<tr class="even">
<td></td>
<td>$$PKGPEND</td>
<td>2788</td>
<td>Pending Alerts for a User in Specified Software</td>
</tr>
<tr class="odd">
<td></td>
<td>PTPURG</td>
<td>3010</td>
<td>Purge Alerts Based on Patient</td>
</tr>
<tr class="even">
<td></td>
<td>RECIPURG</td>
<td>3010</td>
<td>Purge User Alerts</td>
</tr>
<tr class="odd">
<td></td>
<td>USERDATA</td>
<td>2788</td>
<td>Get User Information for an Alert</td>
</tr>
<tr class="even">
<td></td>
<td>USERLIST</td>
<td>2788</td>
<td>Get Recipient Information for an Alert</td>
</tr>
<tr class="odd">
<td><strong>XQALERT</strong></td>
<td>ACTION</td>
<td>10081</td>
<td>Process an Alert</td>
</tr>
<tr class="even">
<td></td>
<td>DELETE</td>
<td>10081</td>
<td>Clear Obsolete Alerts (Single)</td>
</tr>
<tr class="odd">
<td></td>
<td>DELETEA</td>
<td>10081</td>
<td>Clear Obsolete Alerts (All)</td>
</tr>
<tr class="even">
<td></td>
<td>GETACT</td>
<td>10081</td>
<td>Return Alert Variables</td>
</tr>
<tr class="odd">
<td></td>
<td>PATIENT</td>
<td>10081</td>
<td>Get Alerts for a Patient</td>
</tr>
<tr class="even">
<td></td>
<td>SETUP</td>
<td>10081</td>
<td>Send Alerts</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SETUP1</td>
<td>10081</td>
<td>Send Alerts</td>
</tr>
<tr class="even">
<td></td>
<td>USER</td>
<td>10081</td>
<td>Get Alerts for a User</td>
</tr>
<tr class="odd">
<td><strong>XQALFWD</strong></td>
<td>FORWARD</td>
<td>3009</td>
<td>Forward Alerts</td>
</tr>
<tr class="even">
<td><strong>XQALSURO</strong></td>
<td>$$CURRSURO</td>
<td>2790</td>
<td>Get Current Surrogate for Alerts</td>
</tr>
<tr class="odd">
<td></td>
<td>$$GETSURO</td>
<td>3213</td>
<td>Get Current Surrogate Information</td>
</tr>
<tr class="even">
<td></td>
<td>REMVSURO</td>
<td>2790</td>
<td>Remove Surrogates for Alerts</td>
</tr>
<tr class="odd">
<td></td>
<td>SETSURO1</td>
<td>3213</td>
<td>Establish a Surrogate for Alerts</td>
</tr>
<tr class="even">
<td></td>
<td>SUROFOR</td>
<td>3213</td>
<td>Return a Surrogate’s List of Users</td>
</tr>
<tr class="odd">
<td></td>
<td>SUROLIST</td>
<td>3213</td>
<td>List Surrogates for a User</td>
</tr>
<tr class="even">
<td><strong>XQCHK</strong></td>
<td>$$ACCESS</td>
<td>10078</td>
<td>User Option Access Test</td>
</tr>
<tr class="odd">
<td></td>
<td>OP</td>
<td>10078</td>
<td>Current Option Check</td>
</tr>
<tr class="even">
<td><strong>XQDATE</strong></td>
<td><strong>^XQDATE</strong></td>
<td>10079</td>
<td>Convert <strong>$H</strong> to VA FileMan Format (Obsolete)<br />
(Use <strong>$$FMTE^XLFDT</strong> or <strong>$$HTFM^XLFDT</strong>)</td>
</tr>
<tr class="odd">
<td><strong>XQH</strong></td>
<td>EN</td>
<td>10074</td>
<td>Display Help Frames (Clear Screen)</td>
</tr>
<tr class="even">
<td></td>
<td>EN1</td>
<td>10074</td>
<td>Display Help Frames</td>
</tr>
<tr class="odd">
<td><strong>XQH4</strong></td>
<td>ACTION</td>
<td>10080</td>
<td>Print Help Frame Tree</td>
</tr>
<tr class="even">
<td><strong>XQOR</strong></td>
<td>EN</td>
<td>10101</td>
<td>Navigating Protocols</td>
</tr>
<tr class="odd">
<td></td>
<td>EN1</td>
<td>10101</td>
<td>Navigating Protocols (Entry/Exit Actions Not Executed)</td>
</tr>
<tr class="even">
<td></td>
<td>MSG</td>
<td>10101</td>
<td>Enable HL7 Messaging</td>
</tr>
<tr class="odd">
<td><strong>XQORM</strong></td>
<td>EN</td>
<td>10140</td>
<td>Menu Item Display and Selection</td>
</tr>
<tr class="even">
<td></td>
<td>XREF</td>
<td>10140</td>
<td>Force Menu Recompile</td>
</tr>
<tr class="odd">
<td><strong>XQORM1</strong></td>
<td>DISP</td>
<td>10102</td>
<td>Display Menu Selections From Help Code</td>
</tr>
<tr class="even">
<td><strong>XTHC10</strong></td>
<td>$$GETURL</td>
<td>5553</td>
<td>Return URL Data Using HTTP</td>
</tr>
<tr class="odd">
<td><strong>XTHCURL</strong></td>
<td>$$ENCODE</td>
<td>5554</td>
<td>Encodes a Query String</td>
</tr>
<tr class="even">
<td></td>
<td>$$MAKEURL</td>
<td>5554</td>
<td>Creates a URL from Components</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PARSEURL</td>
<td>5554</td>
<td>Parses a URL</td>
</tr>
<tr class="even">
<td><strong>XTHCUTL</strong></td>
<td>$$DECODE</td>
<td>5555</td>
<td>Decodes a String</td>
</tr>
<tr class="odd">
<td><strong>XTID</strong></td>
<td>GETIREF</td>
<td>4631</td>
<td>Get IREF (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$GETMASTR</td>
<td>4631</td>
<td>Get Master VUID Flag (Term/Concept)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$GETSTAT</td>
<td>4631</td>
<td>Get Status Information (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$GETVUID</td>
<td>4631</td>
<td>Get VUID (Term/Concept)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SCREEN</td>
<td>4631</td>
<td>Get Screening Condition (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SETMASTR</td>
<td>4631</td>
<td>Set Master VUID Flag (Term/Concept)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SETSTAT</td>
<td>4631</td>
<td>Set Status Information (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SETVUID</td>
<td>4631</td>
<td>Set VUID (Term/Concept)</td>
</tr>
<tr class="odd">
<td><strong>XTIDTRM</strong></td>
<td>$$GETRPLC</td>
<td>5078</td>
<td>Get Immediate Replacement Term (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$RPLCLST</td>
<td>5078</td>
<td>Get List of Replacement Terms, w/Optional Status Date and History (Term/Concept)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RPLCMNT</td>
<td>5078</td>
<td>Get Final Replacement Term (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$RPLCTRL</td>
<td>5078</td>
<td>Get Replacement Trail for Term, with Replaced “<strong>BY</strong>” and Replacement “<strong>FOR</strong>” Terms (Term/Concept)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RPLCVALS</td>
<td>5078</td>
<td>Get Field Values of Final Replacement Term (Term/Concept)</td>
</tr>
<tr class="even">
<td></td>
<td>$$SETRPLC</td>
<td>5078</td>
<td>Set Replacement Term (Term/Concept)</td>
</tr>
<tr class="odd">
<td><strong>XTKERM4</strong></td>
<td>RFILE</td>
<td>2075</td>
<td>Add Entries to Kermit Holding File</td>
</tr>
<tr class="even">
<td><strong>XTKERMIT</strong></td>
<td>RECEIVE</td>
<td>10095</td>
<td>Load a File into the Host</td>
</tr>
<tr class="odd">
<td></td>
<td>SEND</td>
<td>10095</td>
<td>Send Data from Host</td>
</tr>
<tr class="even">
<td><strong>XTLKKWL</strong></td>
<td>XTLKKWL</td>
<td>10122</td>
<td>Perform Supported VA FileMan Calls on Files Configured for MTLU</td>
</tr>
<tr class="odd">
<td><strong>XTLKMGR</strong></td>
<td>DK</td>
<td>10153</td>
<td>Delete Keywords from the Local Keyword File</td>
</tr>
<tr class="even">
<td></td>
<td>DLL</td>
<td>10153</td>
<td>Delete an Entry from the Local Lookup File</td>
</tr>
<tr class="odd">
<td></td>
<td>DSH</td>
<td>10153</td>
<td>Delete Shortcuts from the Local Shortcut File</td>
</tr>
<tr class="even">
<td></td>
<td>DSY</td>
<td>10153</td>
<td>Delete Synonyms from the Local Synonym File</td>
</tr>
<tr class="odd">
<td></td>
<td>K</td>
<td>10153</td>
<td>Add Keywords to the Local Keyword File</td>
</tr>
<tr class="even">
<td></td>
<td>L</td>
<td>10153</td>
<td>Define a File in the Local Lookup File</td>
</tr>
<tr class="odd">
<td></td>
<td>LKUP</td>
<td>10153</td>
<td>General Lookup Facility for MTLU</td>
</tr>
<tr class="even">
<td></td>
<td>SH</td>
<td>10153</td>
<td>Add Shortcuts to the Local Shortcut File</td>
</tr>
<tr class="odd">
<td></td>
<td>SY</td>
<td>10153</td>
<td>Add Terms and Synonyms to the Local Synonym File</td>
</tr>
<tr class="even">
<td><strong>XUA4A71</strong></td>
<td>$$EN</td>
<td>3178</td>
<td>Convert String to Soundex</td>
</tr>
<tr class="odd">
<td><strong>XUA4A72</strong></td>
<td>$$CODE2TXT</td>
<td>1625</td>
<td>Get HCFA Text</td>
</tr>
<tr class="even">
<td></td>
<td>$$GET</td>
<td>1625</td>
<td>Get Specialty and Subspecialty for a User</td>
</tr>
<tr class="odd">
<td></td>
<td>$$IEN2CODE</td>
<td>1625</td>
<td>Get VA Code</td>
</tr>
<tr class="even">
<td><strong>XUAF4</strong></td>
<td>$$ACTIVE</td>
<td>2171</td>
<td>Institution Active Facility (True/False)</td>
</tr>
<tr class="odd">
<td></td>
<td>CDSYS</td>
<td>2171</td>
<td>Coding System Name</td>
</tr>
<tr class="even">
<td></td>
<td>CHILDREN</td>
<td>2171</td>
<td>List of Child Institutions for a Parent</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CIRN</td>
<td>2171</td>
<td>Institution CIRN-enabled Field Value</td>
</tr>
<tr class="even">
<td></td>
<td>F4</td>
<td>2171</td>
<td>Institution Data for a Station Number</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ID</td>
<td>2171</td>
<td>Institution Identifier</td>
</tr>
<tr class="even">
<td></td>
<td>$$IDX</td>
<td>2171</td>
<td>Institution IEN (Using Coding System &amp; ID)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$IEN</td>
<td>2171</td>
<td>IEN for Station Number</td>
</tr>
<tr class="even">
<td></td>
<td>$$LEGACY</td>
<td>2171</td>
<td>Institution Realigned/Legacy (True/False)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LKUP</td>
<td>2171</td>
<td>Institution Lookup</td>
</tr>
<tr class="even">
<td></td>
<td>LOOKUP</td>
<td>2171</td>
<td>Look Up Institution Identifier</td>
</tr>
<tr class="odd">
<td></td>
<td>$$MADD</td>
<td>2171</td>
<td>Institution Mailing Address</td>
</tr>
<tr class="even">
<td></td>
<td>$$NAME</td>
<td>2171</td>
<td>Institution Official Name</td>
</tr>
<tr class="odd">
<td></td>
<td>$$NNT</td>
<td>2171</td>
<td>Institution Station Name, Number, and Type</td>
</tr>
<tr class="even">
<td></td>
<td>$$NS</td>
<td>2171</td>
<td>Institution Name and Station Number</td>
</tr>
<tr class="odd">
<td></td>
<td>$$O99</td>
<td>2171</td>
<td>IEN of Merged Station Number</td>
</tr>
<tr class="even">
<td></td>
<td>$$PADD</td>
<td>2171</td>
<td>Institution Physical Address</td>
</tr>
<tr class="odd">
<td></td>
<td>PARENT</td>
<td>2171</td>
<td>Parent Institution Lookup</td>
</tr>
<tr class="even">
<td></td>
<td>$$PRNT</td>
<td>2171</td>
<td>Institution Parent Facility</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RF</td>
<td>NONE</td>
<td>Realigned From Institution Information</td>
</tr>
<tr class="even">
<td></td>
<td>$$RT</td>
<td>NONE</td>
<td>Realigned To Institution Information</td>
</tr>
<tr class="odd">
<td></td>
<td>SIBLING</td>
<td>2171</td>
<td>Sibling Institution Lookup</td>
</tr>
<tr class="even">
<td></td>
<td>$$STA</td>
<td>2171</td>
<td>Station Number for IEN</td>
</tr>
<tr class="odd">
<td></td>
<td>$$TF</td>
<td>2171</td>
<td>Treating Facility (<strong>True/False</strong>)</td>
</tr>
<tr class="even">
<td></td>
<td>$$WHAT</td>
<td>2171</td>
<td>Institution Single Field Information</td>
</tr>
<tr class="odd">
<td><strong>XUDHGUI</strong></td>
<td>DEVICE</td>
<td>3771</td>
<td>GUI Device Lookup</td>
</tr>
<tr class="even">
<td><strong>XUDHSET</strong></td>
<td>$$RES</td>
<td>2232</td>
<td>Set Up Resource Device</td>
</tr>
<tr class="odd">
<td><strong>XUHUI</strong></td>
<td>OPKG</td>
<td>3589</td>
<td>Monitor New Style Cross-referenced Fields</td>
</tr>
<tr class="even">
<td><strong>XULMU</strong></td>
<td>CLEANUP</td>
<td>5832</td>
<td>Lock Manager: Execute the Housecleaning Stack</td>
</tr>
<tr class="odd">
<td></td>
<td>SETCLEAN</td>
<td>5832</td>
<td>Lock Manager: Register a Cleanup Routine</td>
</tr>
<tr class="even">
<td></td>
<td>UNCLEAN</td>
<td>5832</td>
<td>Lock Manager: Remove Entries from the Housecleaning Stack</td>
</tr>
<tr class="odd">
<td></td>
<td>ADDPAT</td>
<td>5832</td>
<td>Lock Manager: Add Patient Identifiers for a Computable File Reference</td>
</tr>
<tr class="even">
<td></td>
<td>PAT</td>
<td>5832</td>
<td>Lock Manager: Get a Standard Set of Patient Identifiers</td>
</tr>
<tr class="odd">
<td><strong>XUMF</strong></td>
<td>$$IEN</td>
<td>3795</td>
<td>Institution IEN (Using IFN, Coding System, &amp; ID)</td>
</tr>
<tr class="even">
<td><strong>XUMFI</strong></td>
<td>MAIN</td>
<td>2171</td>
<td>HL7 Master File Message Builder<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td><strong>XUMFP</strong></td>
<td>MAIN</td>
<td>2171</td>
<td>Master File Parameters<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XUP</strong></td>
<td>$$DTIME</td>
<td>4409</td>
<td>Reset DTIME for USER</td>
</tr>
<tr class="odd">
<td><strong>XUPARAM</strong></td>
<td>$$GET</td>
<td>2542</td>
<td>Get Parameters</td>
</tr>
<tr class="even">
<td></td>
<td>$$KSP</td>
<td>2541</td>
<td>Return Kernel Site Parameter</td>
</tr>
<tr class="odd">
<td></td>
<td>$$LKUP</td>
<td>2542</td>
<td>Look Up Parameters</td>
</tr>
<tr class="even">
<td></td>
<td>SET</td>
<td>2542</td>
<td>Set Parameters</td>
</tr>
<tr class="odd">
<td><strong>XUPROD</strong></td>
<td>PROD</td>
<td>4440</td>
<td>Production as opposed to Test Account</td>
</tr>
<tr class="even">
<td><strong>XUPS</strong></td>
<td>$$IEN</td>
<td>4574</td>
<td>Get IEN Using VPID in File #200</td>
</tr>
<tr class="odd">
<td></td>
<td>$$VPID</td>
<td>4574</td>
<td>Get VPID Using IEN in File #200</td>
</tr>
<tr class="even">
<td><strong>XUPSQRY</strong></td>
<td>EN1</td>
<td>4575</td>
<td>Query New Person File</td>
</tr>
<tr class="odd">
<td><strong>XUS</strong></td>
<td>H</td>
<td>10044</td>
<td>Programmer <strong>Halt</strong></td>
</tr>
<tr class="even">
<td><strong>XUS1A</strong></td>
<td>SET</td>
<td>3057</td>
<td>Output Message During Signon</td>
</tr>
<tr class="odd">
<td><strong>XUS2</strong></td>
<td>AVHLPTXT</td>
<td>4057</td>
<td>Get Help Text<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XUSAP</strong></td>
<td>$$CREATE</td>
<td>4677</td>
<td>Create Application Proxy User</td>
</tr>
<tr class="odd">
<td><strong>XUSCLEAN</strong></td>
<td>KILL</td>
<td>10052</td>
<td>Clear all but Kernel Variables</td>
</tr>
<tr class="even">
<td></td>
<td>TOUCH</td>
<td>10052</td>
<td>Notify Kernel of Tasks that Run <strong>7</strong> Days or Longer</td>
</tr>
<tr class="odd">
<td><strong>XUSER</strong></td>
<td>$$ACTIVE</td>
<td>2343</td>
<td>Status Indicator</td>
</tr>
<tr class="even">
<td></td>
<td><span id="DEA_XUSER_Entry_Point" class="anchor"></span>$$DEA</td>
<td>2343</td>
<td><p>Returns a provider’s active DEA Number.</p>
<p>Modified with Kernel Patches XU*8.0*580 and XU*8.0*689 for ePCS.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><span id="DEAXDT_XUSER_Entry_Point" class="anchor"></span>$$DEAXDT</td>
<td>2343</td>
<td><p>Returns the expiration date of a specific DEA number.</p>
<p>Modified with Kernel Patch XU*8.0*689.</p></td>
</tr>
<tr class="even">
<td></td>
<td><span id="DEASCH_XUSER_Entry_Point" class="anchor"></span>DEASCH</td>
<td>2343</td>
<td><p>Returns the DEA schedules for a specific DEA number.</p>
<p>Modified with Kernel Patch XU*8.0*689</p></td>
</tr>
<tr class="odd">
<td></td>
<td><span id="DETOX_XUSER_Entry_Point" class="anchor"></span>$$DETOX</td>
<td>2343</td>
<td><p>Get Detox/Maintenance ID Number</p>
<p>Added with Kernel Patch XU*8.0*580 for ePCS.</p></td>
</tr>
<tr class="even">
<td></td>
<td>DIV4</td>
<td>2533</td>
<td><p>Get User Divisions</p>
<p>(Controlled Subscription)</p></td>
</tr>
<tr class="odd">
<td></td>
<td>$$LOOKUP</td>
<td>2343</td>
<td>NEW PERSON File Lookup</td>
</tr>
<tr class="even">
<td></td>
<td>$$NAME</td>
<td>2343</td>
<td>Get Name of User</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PROVIDER</td>
<td>2343</td>
<td>Providers in NEW PERSON File</td>
</tr>
<tr class="even">
<td></td>
<td><span id="PRDEA_XUSER_Entry_Point" class="anchor"></span>$$PRDEA</td>
<td>2343</td>
<td><p>Returns a prescriber’s default DEA number, that is flagged as USE FOR INPATIENT ORDERS?</p>
<p>Modified with Kernel Patch XU*8.0*689</p></td>
</tr>
<tr class="odd">
<td></td>
<td><span id="PRSCH_XUSER_Entry_Point" class="anchor"></span>$$PRSCH</td>
<td>2343</td>
<td><p>Returns DEA schedule permissions for a prescriber’s active DEA number.</p>
<p>Modified with Kernel Patch XU*8.0*689.</p></td>
</tr>
<tr class="even">
<td></td>
<td><span id="PRXDT_XUSER_Entry_Point" class="anchor"></span>$$PRXDT</td>
<td>2343</td>
<td><p>Returns the expiration date of a prescriber’s default DEA number, which is flagged as USE FOR INPATIENT ORDERS?</p>
<p>Modified with Kernel Patch XU*8.0*689.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><span id="SDEA_XUSER_Entry_Point" class="anchor"></span>$$SDEA</td>
<td>2343</td>
<td><p>Check for Prescribing Privileges</p>
<p>Added with Kernel Patch XU*8.0*580 for ePCS and modified with Kernel Patch XU*8.0*689.</p></td>
</tr>
<tr class="even">
<td></td>
<td>$$VDEA</td>
<td>2343</td>
<td><p>Check if User Can Sign Controlled Substance Orders</p>
<p>Added with Kernel Patch XU*8.0*580 for ePCS.</p></td>
</tr>
<tr class="odd">
<td><strong>XUSERNEW</strong></td>
<td>$$ADD</td>
<td>10053</td>
<td>Add New User</td>
</tr>
<tr class="even">
<td><strong>XUSESIG</strong></td>
<td><strong>^XUSESIG</strong></td>
<td>936</td>
<td><p>Set Up Electronic Signature Code</p>
<p>(Controlled Subscription)</p></td>
</tr>
<tr class="odd">
<td></td>
<td>SIG</td>
<td>10050</td>
<td>Verify Electronic Signature Code</td>
</tr>
<tr class="even">
<td><strong>XUSESIG1</strong></td>
<td>$$CHKSUM</td>
<td>1557</td>
<td>Build Checksum for Global Root</td>
</tr>
<tr class="odd">
<td></td>
<td>$$CMP</td>
<td>1557</td>
<td>Compare Checksum to <strong>$Name_Value</strong></td>
</tr>
<tr class="even">
<td></td>
<td>$$DE</td>
<td>1557</td>
<td>Decode String</td>
</tr>
<tr class="odd">
<td></td>
<td>$$EN</td>
<td>1557</td>
<td>Encode ESBLOCK</td>
</tr>
<tr class="even">
<td></td>
<td>$$ESBLOCK</td>
<td>1557</td>
<td>Electronic Signature (E-Sig) Fields Required for Hash</td>
</tr>
<tr class="odd">
<td><strong>XUSHSH</strong></td>
<td>$$AESDECR</td>
<td>6189</td>
<td>Returns Plaintext String Value for AES Encrypted Ciphertext Entry</td>
</tr>
<tr class="even">
<td></td>
<td>$$AESENCR</td>
<td>6189</td>
<td>Returns AES Encrypted Ciphertext for String Entry</td>
</tr>
<tr class="odd">
<td></td>
<td>$$B64DECD</td>
<td>6189</td>
<td>Returns Decoded Value for a Base64 String Entry</td>
</tr>
<tr class="even">
<td></td>
<td>$$B64ENCD</td>
<td>6189</td>
<td>Returns Base64 Encoded Value for a String Entry</td>
</tr>
<tr class="odd">
<td></td>
<td>$$RSADECR</td>
<td>6189</td>
<td>Returns Plaintext String Value for RSA Encrypted Ciphertext Entry</td>
</tr>
<tr class="even">
<td></td>
<td>$$RSAENCR</td>
<td>6189</td>
<td>Returns RSA Encrypted Ciphertext for String Entry</td>
</tr>
<tr class="odd">
<td></td>
<td>$$SHAHASH</td>
<td>6189</td>
<td>Returns SHA Hash for a String Entry</td>
</tr>
<tr class="even">
<td><strong>XUSHSHP</strong></td>
<td>DE</td>
<td>10045</td>
<td>Decrypt Data String</td>
</tr>
<tr class="odd">
<td></td>
<td>EN</td>
<td>10045</td>
<td>Encrypt Data String</td>
</tr>
<tr class="even">
<td></td>
<td>HASH</td>
<td>10045</td>
<td>Hash Electronic Signature Code</td>
</tr>
<tr class="odd">
<td><strong>XUSNPI</strong></td>
<td>$$CHKDGT</td>
<td>4532</td>
<td>Validate NPI Format</td>
</tr>
<tr class="even">
<td></td>
<td>$$NPI</td>
<td>4532</td>
<td>Get NPI from Files #200 or #4</td>
</tr>
<tr class="odd">
<td></td>
<td>$$QI</td>
<td>4532</td>
<td>Get Provider Entities</td>
</tr>
<tr class="even">
<td><strong>XUSRB</strong></td>
<td>$$CHECKAV</td>
<td>2882</td>
<td>Check Access/Verify Codes<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td></td>
<td>CVC</td>
<td>4054</td>
<td>VistALink-Change User’s Verify Code<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>$$INHIBIT</td>
<td>3277</td>
<td>Check if Logons Inhibited</td>
</tr>
<tr class="odd">
<td></td>
<td>INTRO</td>
<td>4054</td>
<td>VistALink-Get Introductory Text<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>$$KCHK</td>
<td>2120</td>
<td>Check If User Holds Security Key<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td></td>
<td>LOGOUT</td>
<td>4054</td>
<td>VistALink-Log Out User From M<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>OWNSKEY</td>
<td>3277</td>
<td>Verify Security Keys Assigned to a User</td>
</tr>
<tr class="odd">
<td></td>
<td>SETUP</td>
<td>4054</td>
<td>VistALink-Set Up User’s Partition in M<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>VALIDAV</td>
<td>4054</td>
<td>VistALink-Validate User Credentials<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td><strong>XUSRB1</strong></td>
<td>$$DECRYP</td>
<td>2241</td>
<td>Decrypt String</td>
</tr>
<tr class="even">
<td></td>
<td>$$ENCRYP</td>
<td>2240</td>
<td>Encrypt String</td>
</tr>
<tr class="odd">
<td><strong>XUSRB2</strong></td>
<td>DIVGET</td>
<td>4055</td>
<td>Get Divisions for Current User<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>DIVSET</td>
<td>4055</td>
<td>Set Division for Current User<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td></td>
<td>USERINFO</td>
<td>4055</td>
<td>Get Demographics for Current User<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XUSRB4</strong></td>
<td>$$HANDLE</td>
<td>4770</td>
<td>Return Unique Session ID String</td>
</tr>
<tr class="odd">
<td><strong>XUSTAX</strong></td>
<td>$$TAXIND</td>
<td>4911</td>
<td>Get Taxonomy Code from File #200<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>$$TAXORG</td>
<td>4911</td>
<td>Get Taxonomy Code from File #4<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td><strong>XUTMDEVQ</strong></td>
<td>$$DEV</td>
<td>1519</td>
<td>Force Queueing—Ask for Device</td>
</tr>
<tr class="even">
<td></td>
<td>EN</td>
<td>1519</td>
<td>Run a Task (Directly or Queued)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$NODEV</td>
<td>1519</td>
<td>Run a Task (Force Queueing—No Device Selection)</td>
</tr>
<tr class="even">
<td></td>
<td>$$QQ</td>
<td>1519</td>
<td>Double Queue—Direct Queuing in a Single Call</td>
</tr>
<tr class="odd">
<td></td>
<td>$$REQQ</td>
<td>1519</td>
<td>Schedule Second Part of a Task</td>
</tr>
<tr class="even">
<td><strong>XUTMOPT</strong></td>
<td>DISP</td>
<td>1472</td>
<td>Display Option Schedule</td>
</tr>
<tr class="odd">
<td></td>
<td>EDIT</td>
<td>1472</td>
<td>Edit an Option’s Scheduling</td>
</tr>
<tr class="even">
<td></td>
<td>OPTSTAT</td>
<td>1472</td>
<td>Obtain Option Schedule</td>
</tr>
<tr class="odd">
<td></td>
<td>RESCH</td>
<td>1472</td>
<td>Set Up Option Schedule</td>
</tr>
<tr class="even">
<td><strong>XUTMTP</strong></td>
<td>EN</td>
<td>3521</td>
<td>Display HL7 Task Information<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td><strong>XUVERIFY</strong></td>
<td><strong>^XUVERIFY</strong></td>
<td>10051</td>
<td>Verify Access and Verify Codes</td>
</tr>
<tr class="even">
<td></td>
<td>$$CHECKAV</td>
<td>10051</td>
<td>Check Access/Verify Codes</td>
</tr>
<tr class="odd">
<td></td>
<td>WITNESS</td>
<td>1513</td>
<td>Return IEN of Users with A/V Codes and Security Keys<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td><strong>XUWORKDY</strong></td>
<td><strong>^XUWORKDY</strong></td>
<td>10046</td>
<td>Workday Calculation (Obsolete)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$EN</td>
<td>10046</td>
<td>Number of Workdays Calculation</td>
</tr>
<tr class="even">
<td></td>
<td>$$WORKDAY</td>
<td>10046</td>
<td>Workday Validation</td>
</tr>
<tr class="odd">
<td></td>
<td>$$WORKPLUS</td>
<td>10046</td>
<td>Workday Offset Calculation</td>
</tr>
<tr class="even">
<td><strong>%ZIS</strong></td>
<td><strong>^%ZIS</strong></td>
<td>10086</td>
<td>Standard Device Call</td>
</tr>
<tr class="odd">
<td></td>
<td>HLP1</td>
<td>10086</td>
<td>Display Brief Device Help</td>
</tr>
<tr class="even">
<td></td>
<td>HLP2</td>
<td>10086</td>
<td>Display Device Help Frames</td>
</tr>
<tr class="odd">
<td></td>
<td>HOME</td>
<td>10086</td>
<td>Reset Home Device <strong>IO</strong> Variables</td>
</tr>
<tr class="even">
<td></td>
<td>$$REWIND</td>
<td>10086</td>
<td>Rewind Devices</td>
</tr>
<tr class="odd">
<td><strong>%ZISC</strong></td>
<td><strong>^%ZISC</strong></td>
<td>10089</td>
<td>Close Device</td>
</tr>
<tr class="even">
<td><strong>%ZISH</strong></td>
<td>CLOSE</td>
<td>2320</td>
<td>Close Host File</td>
</tr>
<tr class="odd">
<td></td>
<td>$$DEFDIR</td>
<td>2320</td>
<td>Get Default Host File Directory</td>
</tr>
<tr class="even">
<td></td>
<td>$$DEL</td>
<td>2320</td>
<td>Delete Host File</td>
</tr>
<tr class="odd">
<td></td>
<td>$$FTG</td>
<td>2320</td>
<td>Load Host File into Global</td>
</tr>
<tr class="even">
<td></td>
<td>$$GATF</td>
<td>2320</td>
<td>Copy Global to Host File (Append Existing global Nodes)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$GTF</td>
<td>2320</td>
<td>Copy Global to Host File</td>
</tr>
<tr class="even">
<td></td>
<td>$$LIST</td>
<td>2320</td>
<td>List Directory</td>
</tr>
<tr class="odd">
<td></td>
<td>$$MV</td>
<td>2320</td>
<td>Rename Host File</td>
</tr>
<tr class="even">
<td></td>
<td>OPEN</td>
<td>2320</td>
<td>Open Host File</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PWD</td>
<td>2320</td>
<td>Get Current Directory</td>
</tr>
<tr class="even">
<td></td>
<td>$$STATUS</td>
<td>2320</td>
<td>Return End-of-File (EOF) Status</td>
</tr>
<tr class="odd">
<td><strong>%ZISP</strong></td>
<td>PKILL</td>
<td>3172</td>
<td>Kill Special Printer Variables</td>
</tr>
<tr class="even">
<td></td>
<td>PSET</td>
<td>3172</td>
<td>Set Up Special Printer Variables</td>
</tr>
<tr class="odd">
<td><strong>ZISPL</strong></td>
<td>DSD</td>
<td>1092</td>
<td>Delete Spool Data File Entry<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>DSDOC</td>
<td>1092</td>
<td>Delete Spool Document File Entry<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td><strong>%ZISS</strong></td>
<td>ENDR</td>
<td>10088</td>
<td>Set Up Specific Screen Handling Variables</td>
</tr>
<tr class="even">
<td></td>
<td>ENS</td>
<td>10088</td>
<td>Set Up Screen Handling Variables</td>
</tr>
<tr class="odd">
<td></td>
<td>GKILL</td>
<td>10088</td>
<td><strong>KILL</strong> Graphic Variables</td>
</tr>
<tr class="even">
<td></td>
<td>GSET</td>
<td>10088</td>
<td>Set Up Graphics Variables</td>
</tr>
<tr class="odd">
<td></td>
<td>KILL</td>
<td>10088</td>
<td><strong>KILL</strong> Screen Handling Variables</td>
</tr>
<tr class="even">
<td><strong>%ZISTCP</strong></td>
<td>CALL</td>
<td>2118</td>
<td>Make TCP/IP Connection (Remote System)</td>
</tr>
<tr class="odd">
<td></td>
<td>CLOSE</td>
<td>2118</td>
<td>Close TCP/IP Connection (Remote System)</td>
</tr>
<tr class="even">
<td><strong>%ZISUTL</strong></td>
<td>CLOSE</td>
<td>2119</td>
<td>Close Device with Handle</td>
</tr>
<tr class="odd">
<td></td>
<td>OPEN</td>
<td>2119</td>
<td>Open Device with Handle</td>
</tr>
<tr class="even">
<td></td>
<td>RMDEV</td>
<td>2119</td>
<td>Delete Data Given a Handle</td>
</tr>
<tr class="odd">
<td></td>
<td>SAVDEV</td>
<td>2119</td>
<td>Save Data Given a Handle</td>
</tr>
<tr class="even">
<td></td>
<td>USE</td>
<td>2119</td>
<td>Use Device Given a Handle</td>
</tr>
<tr class="odd">
<td><strong>%ZOSF</strong></td>
<td><strong>^%ZOSF</strong></td>
<td>NONE</td>
<td>Operating System-dependent Logic Global</td>
</tr>
<tr class="even">
<td><strong>%ZOSV</strong></td>
<td>$$ACTJ</td>
<td>10097</td>
<td>Number of Active Jobs</td>
</tr>
<tr class="odd">
<td></td>
<td>$$AVJ</td>
<td>10097</td>
<td>Number of Available Jobs</td>
</tr>
<tr class="even">
<td></td>
<td>DOLRO</td>
<td>3883</td>
<td>Display Local Variables<br />
(Controlled Subscription)</td>
</tr>
<tr class="odd">
<td></td>
<td>$$EC</td>
<td>10097</td>
<td>Get Error Code</td>
</tr>
<tr class="even">
<td></td>
<td>GETENV</td>
<td>10097</td>
<td>Current System Information</td>
</tr>
<tr class="odd">
<td></td>
<td>GETPEER</td>
<td>4056</td>
<td>VistALink-Get IP Address for Current Session<br />
(Controlled Subscription)</td>
</tr>
<tr class="even">
<td></td>
<td>$$LGR</td>
<td>10097</td>
<td>Last Global Reference</td>
</tr>
<tr class="odd">
<td></td>
<td>LOGRSRC</td>
<td>10097</td>
<td>Record Resource Usage (RUM)</td>
</tr>
<tr class="even">
<td></td>
<td>$$OS</td>
<td>10097</td>
<td>Get Operating System Information</td>
</tr>
<tr class="odd">
<td></td>
<td>SETENV</td>
<td>10097</td>
<td>Set VMS Process Name (Caché/OpenVMS Systems)</td>
</tr>
<tr class="even">
<td></td>
<td>SETNM</td>
<td>10097</td>
<td>Set VMS Process Name: Parameter Passing (Caché/OpenVMS Systems)</td>
</tr>
<tr class="odd">
<td></td>
<td>T0 (Obsolete)</td>
<td>10097</td>
<td>(Obsolete) Start RT Measure</td>
</tr>
<tr class="even">
<td></td>
<td>T1 (Obsolete)</td>
<td>10097</td>
<td>(Obsolete) Stop RT Measure</td>
</tr>
<tr class="odd">
<td></td>
<td>$$VERSION</td>
<td>10097</td>
<td>Get OS Version Number or Name</td>
</tr>
<tr class="even">
<td><strong>%ZTER</strong></td>
<td><strong>^%ZTER</strong></td>
<td>1621</td>
<td>Kernel Standard Error Recording Routine</td>
</tr>
<tr class="odd">
<td></td>
<td>APPERROR</td>
<td>1621</td>
<td>Set Application Error Name in Kernel Error Trap Log</td>
</tr>
<tr class="even">
<td></td>
<td>$$NEWERR</td>
<td>1621</td>
<td>Verify Support of Standard Error Trapping (Obsolete)</td>
</tr>
<tr class="odd">
<td></td>
<td>UNWIND</td>
<td>1621</td>
<td>Quit Back to Calling Routine</td>
</tr>
<tr class="even">
<td><strong>%ZTLOAD</strong></td>
<td><strong>^%ZTLOAD</strong></td>
<td>10063</td>
<td>Queue a Task</td>
</tr>
<tr class="odd">
<td></td>
<td>$$ASKSTOP</td>
<td>10063</td>
<td>Stop TaskMan Task</td>
</tr>
<tr class="even">
<td></td>
<td>DESC</td>
<td>10063</td>
<td>Find Tasks with a Description</td>
</tr>
<tr class="odd">
<td></td>
<td>DQ</td>
<td>10063</td>
<td>Unschedule a Task</td>
</tr>
<tr class="even">
<td></td>
<td>ISQED</td>
<td>10063</td>
<td>Return Task Status</td>
</tr>
<tr class="odd">
<td></td>
<td>$$JOB</td>
<td>10063</td>
<td>Return a Job Number for a Task</td>
</tr>
<tr class="even">
<td></td>
<td>KILL</td>
<td>10063</td>
<td>Delete a Task</td>
</tr>
<tr class="odd">
<td></td>
<td>OPTION</td>
<td>10063</td>
<td>Find Tasks for an Option</td>
</tr>
<tr class="even">
<td></td>
<td>PCLEAR</td>
<td>10063</td>
<td>Clear Persistent Flag for a Task</td>
</tr>
<tr class="odd">
<td></td>
<td>$$PSET</td>
<td>10063</td>
<td>Set Task as Persistent</td>
</tr>
<tr class="even">
<td></td>
<td>REQ</td>
<td>10063</td>
<td>Requeue a Task</td>
</tr>
<tr class="odd">
<td></td>
<td>RTN</td>
<td>10063</td>
<td>Find Tasks that Call a Routine</td>
</tr>
<tr class="even">
<td></td>
<td>$$S</td>
<td>10063</td>
<td>Check for Task Stop Request</td>
</tr>
<tr class="odd">
<td></td>
<td>STAT</td>
<td>10063</td>
<td>Task Status</td>
</tr>
<tr class="even">
<td></td>
<td>$$TM</td>
<td>10063</td>
<td>Check if TaskMan is Running</td>
</tr>
<tr class="odd">
<td></td>
<td>ZTSAVE</td>
<td>10063</td>
<td>Build ZTSAVE Array</td>
</tr>
</tbody>
</table>

<span id="_Ref333475968" class="anchor"></span>Table 28: Direct Mode Utilities

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists all Kernel and Kernel Toolkit direct mode utilities. Direct mode utilities can be used from Programmer mode, but developers *cannot* call them from within applications.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/113.png) REF: Every direct mode utility is described in the [*Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf) and *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*. Refer to the indicated section in that manual for details on the use of the utility.

The direct mode utilities in <u>Table 28</u> are listed in routine order and by tag within each routine:

<table>
<caption><p><span id="_Ref354998104" class="anchor"></span>Table 29: Remote Procedure Calls (RPCs)—Kernel and Kernel Toolkit</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 25%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Direct Mode Utility</th>
<th>Description</th>
<th>Reference Documentation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>D ^%G</strong></td>
<td>List Global option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Miscellaneous: Developer Tools</td>
</tr>
<tr class="even">
<td><p>(obsolete) <strong>D ^%INDEX</strong></p>
<p>Use: <strong>D ^XINDEX</strong></p></td>
<td>To run <strong>%INDEX</strong></td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Routine Tools and Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^%RR</strong></td>
<td>Input Routines option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^%RS</strong></td>
<td>Output Routines option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^XQ1</strong></td>
<td>Test an Option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Menu Manager: Programmer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^XTER</strong></td>
<td>Display Error Trap</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Error Processing: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^XTERPUR</strong></td>
<td>Purge Error Log</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Error Processing: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^XTFCR</strong></td>
<td>Flow Chart from Entry Point option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Routine Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^XTRCMP</strong></td>
<td>Compare Two Routines option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D TAPE^XTRCMP</strong></td>
<td>Compare Routines on Tape to Disk option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^XTRGRPE</strong></td>
<td>Group Routine Edit option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D CHCKSUM^XTSUMBLD</strong></td>
<td>Integrity checking utility</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^XTVCHG</strong></td>
<td>Variable Changer option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^XTVNUM</strong></td>
<td>Version Number Update option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ENABLE^XUFILE3</strong></td>
<td>Enable File Access Security System</td>
<td><a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf"><em>Kernel 8.0 Management: Signon/Security User Guide</em></a>; File Access Security</td>
</tr>
<tr class="even">
<td><strong>D ^XUINCON</strong></td>
<td>Run File Access Security Conversion</td>
<td><a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf"><em>Kernel 8.0 Management: Signon/Security User Guide</em></a>; File Access Security</td>
</tr>
<tr class="odd">
<td><strong>D ^XUP</strong></td>
<td>Programmer Sign-On</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Signon/Security: Programmer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^XUS</strong></td>
<td>User Sign-On, No Error Trapping</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Signon/Security: Programmer Tools</td>
</tr>
<tr class="odd">
<td><strong>D H^XUS</strong></td>
<td>Programmer Halt</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Signon/Security: Programmer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^XUSCLEAN</strong></td>
<td>Programmer Halt</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Signon/Security: Programmer Tools</td>
</tr>
<tr class="odd">
<td><strong>X ^%Z</strong></td>
<td>Routine Edit option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Miscellaneous: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^%ZTBKC</strong></td>
<td>Global Block Count</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Operating System Interface: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^ZTEDIT</strong></td>
<td>Install <strong>^%Z</strong> editor</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Miscellaneous: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^%ZTER</strong></td>
<td>Record an error</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^ZTMB</strong></td>
<td>Start TaskMan</td>
<td><a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf"><em>Kernel 8.0 Systems Management: TaskMan User Guide</em></a>; TaskMan: System Management—Configuration</td>
</tr>
<tr class="even">
<td><strong>D RESTART^ZTMB</strong></td>
<td>Restart TaskMan</td>
<td><a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf"><em>Kernel 8.0 Systems Management: TaskMan User Guide</em></a>; TaskMan: System Management—Configuration</td>
</tr>
<tr class="odd">
<td><strong>D ^ZTMCHK</strong></td>
<td>Check TaskMan’s Environment</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^ZTMGRSET</strong></td>
<td>Update <strong>^%ZOSF</strong> Nodes</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Operating System Interface: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D RUN^ZTMKU</strong></td>
<td>Remove TaskMan from a WAIT state</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; TaskMan Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D STOP^ZTMKU</strong></td>
<td>Stop TaskMan</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; TaskMan Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D WAIT^ZTMKU</strong></td>
<td>Place TaskMan in a WAIT state</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; TaskMan Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^ZTMON</strong></td>
<td>Monitor TaskMan</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; TaskMan Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^%ZTPP</strong></td>
<td>List Routines option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="even">
<td><strong>D ^%ZTRDEL</strong></td>
<td>Delete Routines option</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Toolkit: Developer Tools</td>
</tr>
<tr class="odd">
<td><strong>D ^ZU</strong></td>
<td>User Sign-On</td>
<td><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em>; Signon/Security: Developer Tools</td>
</tr>
</tbody>
</table>

<span id="_Ref354998104" class="anchor"></span>Table 29: Remote Procedure Calls (RPCs)—Kernel and Kernel Toolkit

# Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 29</u> lists the Remote Procedure Calls (RPCs) in the Kernel and Kernel Toolkit namespaces as stored in the REMOTE PROCEDURE (#8994) file (listed alphabetically by RPC name):

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/114.png) NOTE: The Kernel and Kernel Toolkit namespaces include: “XDR\*,” “XI\*,” “XPAR\*,” “XPD\*,” “XQ\*,” “XT,” and “XU\*.”

<table>
<caption><p><span id="_Ref14770001" class="anchor"></span>Table 30: Software-Wide Variables—Defined at All Times (listed alphabetically)</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC</th>
<th>ICR #</th>
<th>Tag^Routine</th>
<th>Input Parameters</th>
<th>Output/ Return Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>XDR ADD POTENTIAL PATIENT DUP</strong></p>
<p>Availability: <strong>AGREEMENT</strong></p></td>
<td>5271</td>
<td><strong>ENTRY^XQALGUI</strong></td>
<td><ul>
<li><p><strong>FILE NUMBER:</strong> File number for the file to which the potential duplicate records belong. For example, if the two potential duplicate entries are on the PATIENT file, this value is set to <strong>2</strong>.</p></li>
<li><p><strong>TO_IEN:</strong> Internal Entry Number (IEN) of one of the potential duplicate records. For example, this could be a DFN from the PATIENT (#2) file.</p></li>
<li><p><strong>FROM_IEN:</strong> Internal Entry Number (IEN) of one of the potential duplicate records.<br />
For example, this could be a DFN from the PATIENT (#2) file.</p></li>
</ul></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>Success:</strong> IEN from the DUPLICATE RECORD (#15) file. If no errors occur, and if either an existing record is found, or a new record is added.</p></li>
<li><p><strong>Failure:<br />
-1^Error Message—</strong>If any errors occur.</p></li>
</ul></td>
<td>This RPC adds a record to the VistA DUPLICATE RECORD (#15) file or find an existing record for the pair of potential duplicates passed to the RPC. This was written to allow MPI to add potential duplicate patients to the file when potential duplicates are detected by the Person Service Identity Management (PSIM) probabilistic search.</td>
</tr>
<tr class="even">
<td><p><strong>XDR UPD SUPPR EMAIL</strong></p>
<p>Availability: <strong>AGREEMENT</strong></p></td>
<td>None</td>
<td><strong>ADD^XDRDADDS</strong></td>
<td><ul>
<li><p><strong>FILE NUMBER:</strong> File number for the file that is the <strong>.01</strong> field of a record in the DUPLICATE RESOLUTION (#15.1) file. This is the record that is to be updated by this RPC.</p></li>
<li><p><strong>VALUE:</strong> <em>Must</em> be set to <strong>1</strong> or <strong>0</strong>. This value will be put into the SUPPRESS NEW DUP.</p></li>
<li><p><strong>EMAIL</strong> field.</p></li>
</ul></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>Success: 0—</strong>If no errors occurred.</p></li>
<li><p><strong>Failure:<br />
-1^Error Message—</strong>If errors occurred.</p></li>
</ul></td>
<td><p>This API remotely sets the SUPPRESS NEW DUP EMAIL (#99) field in the DUPLICATE RESOLUTION (#15.1) file.</p>
<p>SUPPRESS NEW DUP EMAIL is set to <strong>1</strong> (Yes) to suppress the email that is normally sent when a new record is added to the DUPLICATE RECORD file by PSIM (that is by a call from routine <strong>XDRDADDS</strong>).</p>
<p>If SUPPRESS NEW DUP EMAIL is set to <strong>0</strong> (No) or <strong>NULL</strong>, the email is sent.</p></td>
</tr>
<tr class="odd">
<td><p><strong>XQAL GUI ALERTS</strong></p>
<p>Availability: <strong>PUBLIC</strong></p></td>
<td>None</td>
<td><strong>ENTRY^XQALGUI</strong></td>
<td><strong>DATA:</strong> Subscripted, and the subscript contains the actual variable name (and can be a global reference), while the value for the variable is the value associated with that <strong>DATA</strong> element.</td>
<td>Array: Contains the return values for the type of call.</td>
<td>This RPC handles the <strong>XUAlert</strong> component.</td>
</tr>
<tr class="even">
<td><p><strong>XU EPCS EDIT</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>None</td>
<td><strong>ENTRY^XUEPCSED</strong></td>
<td><strong>DATA</strong></td>
<td>Single Value</td>
<td><p>This RPC stores information on editing changes in the NEW PERSON (#200) file related to the electronic prescribing of controlled substances.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/115.png) <strong>NOTE:</strong> This RPC was released with Kernel Patch XU*8.0*580.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/116.png) <strong>NOTE:</strong> This RPC was deprecated with Kernel Patch XU*8.0*689 and ePCS GUI v2.</p></td>
</tr>
<tr class="odd">
<td><strong>XULM GET LOCK TABLE</strong></td>
<td>5832</td>
<td><strong>LOCKS^XULMRPC</strong></td>
<td><ul>
<li><p><strong>LOCKGBL:</strong> This is the global reference of the location where the lock table should be returned. Maximum data length: <strong>245</strong>.</p></li>
<li><p><strong>RESULT:</strong> Global location to place the result. Maximum data length: <strong>200</strong>.</p></li>
</ul></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>0</strong> on failure.</p></li>
<li><p><strong>1</strong> on success.</p></li>
</ul></td>
<td>The Lock Manager uses this RPC to obtain the lock table on a specific node. The lock table is returned in a global.</td>
</tr>
<tr class="even">
<td><strong>XULM KILL PROCESS</strong></td>
<td>5832</td>
<td><strong>KILLPROC^XULMRPC</strong></td>
<td><ul>
<li><p><strong>PID:</strong> This is the PID of the process to be <strong>KILL</strong>ed. Maximum data length: <strong>250</strong>.</p></li>
<li><p><strong>RETURN:</strong> This is the global location to return the result. The result should be returned in <strong>^XTMP</strong>, since it is translated between nodes. Maximum data length: <strong>200</strong>.</p></li>
</ul></td>
<td></td>
<td>The Lock Manager uses this RPC to terminate a process.</td>
</tr>
<tr class="odd">
<td><p><strong>XUPS PERSONQUERY</strong></p>
<p>Availability: <strong>PUBLIC</strong></p></td>
<td>None</td>
<td><strong>EN1^XUPSQRY</strong></td>
<td><ul>
<li><p><strong>XUPSLNAM:</strong> Required if lookup by name.</p></li>
<li><p><strong>XUPSFNAM</strong></p></li>
<li><p><strong>XUPSSSN</strong></p></li>
<li><p><strong>XUPSPROV</strong></p></li>
<li><p><strong>XUPSSTN</strong></p></li>
<li><p><strong>XUPSMNM</strong></p></li>
<li><p><strong>XUPSDATE</strong></p></li>
<li><p><strong>XUPSVPID:</strong> Required if lookup by VPID.</p></li>
</ul></td>
<td>Array: Output data stored in a global array.</td>
<td>This RPC performs a person lookup.</td>
</tr>
<tr class="even">
<td><p><strong>XUS ALLKEYS</strong></p>
<p>Agreement: <strong>PUBLIC</strong></p></td>
<td>6287</td>
<td><strong>ALLKEYS^XUSRB</strong></td>
<td><ul>
<li><p><strong>IEN:</strong> This is the IEN or <strong>DUZ</strong> of the user in question. If <em>not</em> passed in, the RPC will use the current <strong>DUZ</strong>.</p></li>
<li><p><strong>FLAG:</strong> Not in use currently.</p></li>
</ul></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>Success:</strong> Returns a list of the names of the security keys the user holds.</p></li>
<li><p><strong>Failure:</strong> Returns <strong>-1</strong> if failed for some reason.</p></li>
</ul></td>
<td>This RPC returns all the KEYS that a user holds. If the <strong>FLAG</strong> is set to some value, the list of KEYS will be screened to only be those for J2EE use. For KAAJEE.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS AV CODE</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>1630</td>
<td><strong>VALIDAV^XUSRB</strong></td>
<td><strong>AVCODE:</strong> <strong>AccessCode_”;”_VerifyCode</strong> in unencrypted form.</td>
<td>Array: It returns an array of values.</td>
<td>This RPC checks if an ACCESS/VERIFY Code pair is valid.</td>
</tr>
<tr class="even">
<td><p><strong>XUS AV HELP</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>None</td>
<td><strong>AVHELP^XUSRB</strong></td>
<td>None</td>
<td>Array: Returns instructions on entering new Access/Verify Codes.</td>
<td>This RPC returns instructions on entering new Access/Verify Codes.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS CCOW VAULT PARAM</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>None</td>
<td><strong>CCOWPC^XUSRB4</strong></td>
<td>None</td>
<td>Returns a value for use with the CCOW vault.</td>
<td>This RPC returns a value for use with the CCOW vault.</td>
</tr>
<tr class="even">
<td><p><strong>XUS CVC</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>6296</td>
<td><strong>CVC^XUSRB</strong></td>
<td>None</td>
<td></td>
<td>This RPC allows the user to change their Verify Code.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS DIVISION GET</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>5198</td>
<td><strong>DIVGET^XUSRB2</strong></td>
<td><strong>IEN:</strong> If passed, this will be the user to get the division info on.</td>
<td>Returns a list of divisions for a user.</td>
<td>This RPC returns a list of divisions for a user.</td>
</tr>
<tr class="even">
<td><p><strong>XUS DIVISION SET</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>5199</td>
<td><strong>DIVSET^XUSRB2</strong></td>
<td><strong>DIV</strong></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>Success: 1</strong> if the value was accepted.</p></li>
<li><p><strong>Failure: 0</strong> if the input was <em>not</em> OK.</p></li>
</ul></td>
<td>This RPC sets the user’s selected Division in <strong>DUZ(2)</strong> during signon.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS GET CCOW TOKEN</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>None</td>
<td><strong>CCOW^XUSRB4</strong></td>
<td>None</td>
<td>Array</td>
<td>This RPC gets a token to save in the CCOW context to aid in signon.</td>
</tr>
<tr class="even">
<td><p><strong>XUS GET TOKEN</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>6813</td>
<td><strong>ASH^XUSRB4</strong></td>
<td>None</td>
<td>Returns: A handle to a token that signs on a new process.</td>
<td>This RPC returns a handle to a token that signs on a new process.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS GET USER INFO</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>2857</td>
<td><strong>USERINFO^XUSRB2</strong></td>
<td>None</td>
<td>Array: Returns information about a user after logon.</td>
<td>This RPC returns information about a user after logon.</td>
</tr>
<tr class="even">
<td><p><strong>XUS GET VISITOR</strong></p>
<p>Agreement: <strong>SUBSCRIPTION</strong></p></td>
<td>5532</td>
<td><strong>GETVISIT^XUSBSE1</strong></td>
<td><strong>TOKEN</strong></td>
<td>Single Value</td>
<td>This controlled-subscription RPC is used by the Broker Security Enhancement (BSE) to check a user’s credentials based on a BSE TOKEN that was passed to identify and authenticate a visiting user. The remote VistA system calls this RPC on the authenticating VistA system to validate if the visiting user is permitted to visit, and if so, obtain the authenticated user’s demographics.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS INTRO MSG</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>1631</td>
<td><strong>INTRO^XUSRB</strong></td>
<td>None</td>
<td>Returns: Introductory text.</td>
<td>This RPC returns the INTRO message from the KERNEL SYSTEM PARAMETERS (#8989.3) file.</td>
</tr>
<tr class="even">
<td><p><strong>XUS KEY CHECK</strong></p>
<p>Agreement: <strong>PUBLIC</strong></p></td>
<td>6286</td>
<td><strong>OWNSKEY^XUSRB</strong></td>
<td><p><strong>KEY:</strong></p>
<ul>
<li><p>If key is a single value, it holds the one key to check.</p></li>
<li><p>If key is an array, then the result is an array that matches the key list with values that match the status of the key check for each key.</p></li>
</ul></td>
<td><p>Array. Returns:</p>
<ul>
<li><p><strong>1—</strong>If the user has the key.</p></li>
<li><p><strong>0—</strong>If the user does <em>not</em> have the key.</p></li>
</ul></td>
<td>This RPC checks if the user (<strong>DUZ</strong>) holds a security key or an array of keys. If a single security key is sent, the result is returned in <strong>R(0)</strong>. If an array is sent down, then the return array has the same order as the calling array.</td>
</tr>
<tr class="odd">
<td><strong>XUS MVI ENRICH NEW PERSON</strong></td>
<td>1059</td>
<td><strong>UPDATE^XUMVIENU</strong></td>
<td><ul>
<li><p><strong>PARAM:</strong> Input array:<strong><br />
</strong><br />
<strong>PARAM("WHO")</strong>=Station Number of requesting station<br />
<strong>PARAM("NPI")</strong>=National Provider Identifier</p></li>
</ul>
<p>Required elements only when <strong>FLAG</strong> input parameter is <strong>A</strong>:<br />
<br />
<strong>PARAM("NAME")</strong>=surname|first name|middle name|suffix|full .01 name</p>
<p>Optional elements (only pass those elements you want to update):<br />
<br />
<strong>PARAM("ADDRESS DATA")</strong>=street address 1|street address 2|street address 3|city|state|zip code|office phone|fax number<br />
<strong>PARAM("SubjectOrgan")</strong>=subject organization<br />
Default: "<strong>Department Of Veterans Affairs</strong>"<br />
<strong>PARAM("SubjectOrganID")</strong>=subject organization id<br />
Default: "<strong>urn:oid:2.16.840.1.113883.4.349</strong>"<br />
<strong>PARAM("ADUPN")</strong>=adupn<br />
<strong>PARAM("AuthWriteMedOrders")</strong>=1 or 0 for YES/NO<br />
Default if <strong>WHO</strong> is 200PIEV and a DEA# is sent: <strong>1</strong> (for YES)<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"DEA")</strong>=Drug Enforcement Agency (DEA) #<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"Detox")</strong>= detox number<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"DEAExpire")</strong>=expiration date (can be future)<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedIINarc")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedIINonNarc")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedIIINarc")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedIIINonNarc")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedIV")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEA",&lt;seq#&gt;,"SchedV")</strong>=1 or 0 for YES/NO<br />
<strong>PARAM("DEGREE")</strong>=degrees (codes delimited by a space)<br />
<strong>PARAM("EMAIL")</strong>=email address<br />
<strong>PARAM("GENDER")</strong>=M or F<br />
<strong>PARAM("Inactivate")</strong>=inactive date (can be future)<br />
<strong>PARAM("NonVAPrescriber")</strong>=1 or 0 for YES/NO<br />
Default if <strong>WHO</strong> is 200PIEV: <strong>1</strong> (for YES)<br />
<strong>PARAM("NTUSERNAME")</strong>=network user name<br />
<strong>PARAM("PersonClass",&lt;seq#&gt;,"PersonClass")</strong>=X12 code value<br />
<strong>PARAM("PersonClass",&lt;seq#&gt;,"PersonClassActive")</strong>=date<br />
Default if not currently active: <strong>TODAY</strong><br />
<strong>PARAM("PersonClass",&lt;seq#&gt;,"PersonClassExpire")</strong>=date<br />
<strong>PARAM("ProviderClass")</strong>=a value from the PROVIDER CLASS (#7) file<br />
<strong>PARAM("ProviderType")</strong>=provider type code|provider type value<br />
<strong>PARAM("Remarks")</strong>=remarks<br />
Default if <strong>WHO</strong> is 200PIEV: "<strong>NON-VA PROVIDER</strong>"<br />
<strong>PARAM("SECID")</strong>=secid<br />
<strong>PARAM("TaxID")</strong>=tax id<br />
<strong>PARAM("Termination")</strong>=termination date</p>
<p>(<em>cannot</em> be future)<br />
<strong>PARAM("Title")</strong>=value from TITLE file (#3.1)<br />
Default if <strong>WHO</strong> is 200PIEV: "<strong>NON-VA PROVIDER</strong>"<br />
<strong>PARAM("UniqueUserID")</strong>=unique user id</p>
<ul>
<li><p><strong>FLAG:</strong> This flag controls whether the RPC is adding a new entry to the NEW PERSON (#200) file or updating an existing entry. Possible values are:</p></li>
</ul>
<ul>
<li><p><strong>U—</strong>Update an existing entry</p></li>
<li><p><strong>A—</strong>Add a new entry</p></li>
</ul></td>
<td><p>Returns:</p>
<ul>
<li><p><strong>Success:</strong><br />
<br />
<strong>DUZ of New Person File entry edited or added</strong>.<br />
Returned if there were no issues adding or editing the entry.<br />
<br />
<strong>DUZ^-1^ErrorMessage</strong><br />
Returned if entry was edited, but some data was not valid and could not be filed.</p></li>
<li><p><strong>Failure:</strong><br />
<br />
<strong>-1^ErrorMessage</strong><br />
<br />
Returned, for example, if required data was <em>not</em> passed; entry could not be added when <strong>FLAG="A"</strong>, or entry could <em>not</em> be found based on the NPI when <strong>FLAG="U"</strong>.</p></li>
</ul></td>
<td><p>This controlled subscription RPC is used exclusively by the Master Veteran Index (MVI) software to update enriched data in the NEW PERSON (#200) file.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/117.png) <strong>NOTE:</strong> This RPC was released with Kernel Patch XU*8.0*711.</p></td>
</tr>
<tr class="even">
<td><p><strong>XUS PKI SET UPN</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>5823</td>
<td><strong>SETUPN^XUSER2</strong></td>
<td><strong>UPN:</strong> This is the SUBJECT ALTERNATIVE NAME from the PIV card.</td>
<td>Single Value</td>
<td>This RPC sets the SUBJECT ALTERNATIVE NAME (#501.2) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS PKI GET UPN</strong></p>
<p>Agreement: <strong>PUBLIC</strong></p></td>
<td>5816</td>
<td><strong>GETUPN^XUSER2</strong></td>
<td>None</td>
<td>Single Value</td>
<td>This RPC gets the SUBJECT ALTERNATIVE NAME (#501.2) field from the NEW PERSON (#200) file. It checks that the correct PIV card has been put into the reader.</td>
</tr>
<tr class="even">
<td><p><strong>XUS SEND KEYS</strong></p>
<p>Agreement: <strong>RESTRICTED</strong></p></td>
<td>1633</td>
<td><strong>SENDKEYS^XUSRB</strong></td>
<td>None</td>
<td>Array: strings that are used in the hashing algorithm. The strings that are returned are picked up from <strong>Z^XUSRB</strong>.</td>
<td>This RPC returns an array of strings that are used in the hashing algorithm. The strings that are returned are picked up from <strong>Z^XUSRB</strong>.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS SET VISITOR</strong></p>
<p>Agreement: <strong>PUBLIC</strong></p></td>
<td>5501</td>
<td><strong>SETVISIT^XUSBSE1</strong></td>
<td>None</td>
<td>Returns: A BSE token string</td>
<td><p>This RPC is run on the Authenticating VistA M Server. It returns a Kernel Authentication Token that identifies the current user.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/118.png) <strong>NOTE:</strong> This RPC was added with the Broker Security Enhancement (BSE) project, which was released with Kernel Patch XU*8.0*404.</p></td>
</tr>
<tr class="even">
<td><p><strong>XUS SIGNON SETUP</strong></p>
<p><strong>Agreement: PUBLIC</strong></p></td>
<td>1632</td>
<td><strong>SETUP^XUSRB</strong></td>
<td></td>
<td>Array</td>
<td>This RPC establishes the environment necessary for DHCP signon</td>
</tr>
<tr class="odd">
<td><p><strong>XWB GET VARIABLE VALUE</strong></p>
<p><strong>Agreement: PUBLIC</strong></p></td>
<td>1629</td>
<td><strong>XWBLIB</strong></td>
<td></td>
<td>Single Value</td>
<td><p>This RPC accepts the name of a variable that will be evaluated, and its value returned to the server. For example, this RPC can be called with a parameter like <strong>DUZ</strong>, which will be returned as <strong>123456</strong>.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/119.png) <strong>NOTE:</strong> This is an RPC Broker namespaced RPC but included here as part of Kernel Patch XU*8.0*580.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref14770001" class="anchor"></span>Table 30: Software-Wide Variables—Defined at All Times (listed alphabetically)

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations with Other VistA Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel establishes external relations with all other VistA software and with the various implementations of ANSI M. Kernel provides a transparent interface between VistA and the host operating system.

All other VistA software depends upon the presence of Kernel, for two main reasons:

- Kernel provides a wealth of application mode entry points that software applications use to solve many common programming problems.
- Kernel provides other VistA applications with portability. To achieve independence from any vendor’s implementation of the M standard, VistA adopted programming standards and conventions that advise software applications to avoid the use of the non-portable features of ANSI M. Though all VistA software depends upon an ANSI M environment, they also depend upon Kernel to replace non-portable features with standard Kernel entry points and services.

## External Relations with M Operating Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel itself depends upon the presence of one of the ANSI M environments it supports. Currently, Caché is the centrally procured M operating systems in use at the VA medical centers and the primary ANSI M environment supported by Kernel. As VistA adjusts its strategies for configuring computer sites, the list of ANSI M environments supported by Kernel continues to change.

Operating system interfaces are involved in each aspect of Kernel. Identifying the M operating system upon Kernel installation starts processes that create the appropriate Kernel environment. To begin, the ^%ZOSF global is built from an operating system-specific routine. By executing nodes of the ^%ZOSF global, implementation-specific functions that are *not* part of ANSI M are possible. Functions include turning echo on or off, allowing type-ahead, or reporting the current UCI.

Other operating system-specific routines distributed with Kernel include:

- %ZIS4 for spooling.
- %ZOSV for system viewing.
- %XUCI for UCI swapping.
- ZU for tied terminals.

The %ZOSV routine contains code that enables use of the VIEW command and \$VIEW function to get information from the operating system. Another routine, TaskMan’s %ZTM, similarly makes possible the use of a protected M procedure, the JOB command, to spawn jobs on a mounted volume set.

Kernel allows processors running different operating systems to be linked. The ^%ZOSF global makes this possible, too. The ^%ZOSF global is never translated, and thus, can retain processor-specific information.

The Manager account is generally reserved for operating system-specific routines and globals. Part of Kernel, however, *must* also reside in this account to take care of certain input/output procedures. To avoid collision with pre-existing operating system routines and globals, Kernel uses the local Z namespace. Globals in the Manager account include:

- ^%ZTSK and ^%ZTSCH for TaskMan
- ^%ZUA for audit data
- %Z as the routine editor

Routines include the %ZTM\* (TaskMan) and %ZIS\* (Device Handler).

Kernel’s use of variables illustrates the way it functions as a buffer between the host operating system and VistA applications. It uses M special variables to create utilities for use by application developers. \$HOROLOG is used by VA FileMan in DATE/TIME routines such as %DT and %DTC, \$JOB is used by TaskMan, and \$IO is used by the Device Handler. In turn, Kernel has key variables that can be referenced by VistA application routines. Perhaps not surprisingly, one of these is DT and another is IO. As VistA system-wide variables, they are documented in the VistA Standards and Conventions (SAC).

## Required Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0 and Kernel Toolkit 7.3 require the following VistA software:

- VA FileMan 22.2
- MailMan 8.0

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/120.png) REF: For more details, see the *Kernel Installation Guide* and *Toolkit Installation Guide*.

## DBA Approvals and Integration Control Registration (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Control Registrations (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are *not* available to the general programming public.

To communicate with the underlying operating system files, Kernel has the approval of the DBA to reference the following globals:

- ^%ET
- ^%IS
- ^%SY
- ^CPU
- ^RTH
- ^SPOOL
- ^SYS

### ICRs—Current List for Kernel or Kernel Toolkit as Custodian

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a current list of ICR to which the Kernel (XU) or Kernel Toolkit (XT) software is a custodian, perform the following procedure:

1.  Sign on to the FORUM system.
7.  Go to the DBA menu \[DBA\].
8.  Select the Integration Agreements Menu option \[DBA IA ISC\].
9.  Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].
10. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].
11. When prompted for a package, enter XU or Kernel, XT, or Toolkit.
12. All current IAs to which the Kernel or Kernel Toolkit software is a custodian are listed.

### ICRs—Detailed Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain detailed information on a specific Integration Control Registration, perform the following procedure:

1.  Sign on to the FORUM system.
13. Go to the DBA menu \[DBA\].
14. Select the Integration Agreements Menu option \[DBA IA ISC\].
15. Select the Inquire option \[DBA IA INQUIRY\].
16. When prompted for “INTEGRATION REFERENCES,” enter the specific Integration Control Registration number of the ICR you would like to display.
17. The option then lists the full text of the ICR you requested.

### ICRs—Current List for Kernel or Kernel Toolkit as Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain the current list of IAs, if any, to which the Kernel (XU) or Kernel Toolkit (XT) software is a subscriber, perform the following procedure:

1.  Sign on to the FORUM system.
7.  Go to the DBA menu \[DBA\].
8.  Select the Integration Agreements Menu option \[DBA IA ISC\].
9.  Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].
10. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].
11. When prompted with “START WITH SUBSCRIBING PACKAGE,” enter XU or KERNEL; XT or TOOLKIT (uppercase).
12. When prompted with “GO TO SUBSCRIBING PACKAGE,” enter XU or KERNEL; XT or TOOLKIT (uppercase).
13. All current IAs to which the Kernel (XU) or Kernel Toolkit (XT) software is a subscriber are listed.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Independence of Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of Kernel’s options can be invoked independently. None requires any special setup to run successfully.

When rearranging options on menus, care should be taken that security is preserved. In several cases, a menu is locked with a security key, but all the options on that menu are *not* locked with the same key. In other cases, items are assumed to be locked because the parent menu itself is locked. So, if an option were placed on another menu, the security on that option could be lost. This situation exists for some options on the following menus:

- Audit Menu (VA FileMan, locked with the XUAUDITING security key)
- Filegrams (locked with the XUFILEGRAM security key)
- KIDS Installation Menu (locked with the XUPROGMODE security key)
- KIDS Main Menu (locked with the XUPROG security key)
- Programmer Options (locked with the XUPROG security key)
- ScreenMan (locked with the XUSCREENMAN security key)
- VA FileMan Management (locked with the XUMGR security key)

# Software-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 30</u> lists the software-wide key variables that can be assumed to be always defined when operating within the menu system, as per Appendix 10-B in of VA’s *Veterans Health Administration Manual M-11(Medical Information Resources Management Office*: *Operations Document)*:

| Variable      | Description                                                                                                                                                                                                                                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DILOCKTM  | VA FileMan's LOCK time out value. This variable is defined and set to 5 seconds when ^XUP is executed, and it is part of the standard VistA Symbol table. All incremental LOCKS *must* have a timeout; the timeout *must not* be less than the value of DILOCKTM. The developer is *not* responsible for defining nor killing DILOCKTM. |
| DT        | Current date in VA FileMan internal format.                                                                                                                                                                                                                                                                                                             |
| DTIME     | Integer value of the number of seconds the user must respond to a timed read. The developer is *not* responsible for defining nor killing DTIME.                                                                                                                                                                                                    |
| DUZ       | Internal entry number (IEN) from the NEW PERSON (#200) file.                                                                                                                                                                                                                                                                                            |
| DUZ(0)    | User’s FILE MANAGER ACCESS CODE string.                                                                                                                                                                                                                                                                                                                 |
| DUZ(2)    | User’s institutional affiliation. It is the internal entry number from the Institution file.                                                                                                                                                                                                                                                            |
| DUZ(“AG”) | User’s agency code.                                                                                                                                                                                                                                                                                                                                     |
| IO        | Hardware name (\$I) of the last selected input/output device.                                                                                                                                                                                                                                                                                       |
| IOF       | Contains the code to issue a form feed for the last selected input/output device.                                                                                                                                                                                                                                                                       |
| IOM       | Column position of the right margin, for the last selected input/output device.                                                                                                                                                                                                                                                                         |
| ION       | Name of the last selected input/output device from the DEVICE (#3.5) file (.01 field value).                                                                                                                                                                                                                                                        |
| IOSL      | Variable indicating the number of lines on the last selected input/output device (such as screen or page length).                                                                                                                                                                                                                                       |
| IOST      | The last selected input/output device’s subtype from the TERMINAL TYPE (#3.2) file (.01 field value).                                                                                                                                                                                                                                               |
| IOT       | Type of the last selected input/output device, such as TRM for terminal.                                                                                                                                                                                                                                                                            |
| U         | This variable is always defined. It is set to the “^” character, which is used as the field separator for data stored in VA FileMan files.                                                                                                                                                                                                          |

<span id="_Ref14769947" class="anchor"></span>Table 31: Variables—Defined While a User is in the Menu System

In addition to the variables described in Appendix 10-B of the M-11 manual, <u>Table 31</u> lists the variables defined by Kernel while a user is in the menu system:

| Variable        | Description                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DUZ(“AUTO”) | Current auto-menu flag.                                                                                                                                                                     |
| DUZ(“LANG”) | Contains a POINTER to VA FileMan’s LANGUAGE (#.85) file, which VA FileMan uses for language-specific displays of prompts, dates and times, and dialogs (from the DIALOG \[#.84\] file). |
| IO(0)       | \$I value of the home device at the time of the call to the Device Handler (^%ZIS).                                                                                                 |
| IOBS        | Contains the code to issue a backspace for last selected input/output device.                                                                                                               |
| IOS         | Internal entry number of the last selected input/output device from the DEVICE (#3.5) file.                                                                                                 |
| IOST(0)     | The last selected input/output device’s subtype from the TERMINAL TYPE (#3.2) file (internal entry number).                                                                                 |
| IOXY        | Value of the XY field from the TERMINAL TYPE (#3.2) file for the last selected input/output device.                                                                                     |

<span id="_Ref14769908" class="anchor"></span>Table 32: Variables—Defined While a User is in the Menu System with Alpha-Beta Tracking

<u>Table 32</u> lists the software-wide variable that is defined within the menu system if alpha-beta tracking is taking place:

| Variable    | Description                                                |
|-------------|------------------------------------------------------------|
| XQABTST | Flag that signals whether alpha-beta testing is in effect. |

<span id="_Ref333475998" class="anchor"></span>Table 33: SAC Exemptions

# SACC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 33</u> lists the Standards and Conventions (SAC) exemptions that currently pertain to Kernel and Kernel Toolkit that were granted by the Programming Standards and Conventions Committee (SACC). <u>Table 33</u> includes the following data:

- Standards Section Number
- Nature of Exemption
- Date Created (Granted)
- Description

<table>
<caption><p><span id="_Ref381880235" class="anchor"></span>Table 34: Globals in Production Account—Protection, Translation and Journaling Information</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 14%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Standards Section Number</th>
<th>Nature of Exemption</th>
<th>Date Created</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>6D</td>
<td><strong>FM compatibility</strong></td>
<td></td>
<td>The <strong>^XUTL</strong> global is exempted from VA FileMan compatibility. It is a <em>non</em>-translated, completely re-creatable global used in MenuMan.</td>
</tr>
<tr class="even">
<td>2</td>
<td>2D2</td>
<td><strong>* and # READs</strong></td>
<td>08/10/1989</td>
<td>The <strong>ZISL*</strong> and <strong>^%Z</strong> editor can use <strong>*</strong> and <strong>#-</strong>readers.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>6D</td>
<td><strong>FM compatibility</strong></td>
<td>08/10/1989</td>
<td><p>The following globals are exempt from VA FileMan compatibility:</p>
<ul>
<li><p><strong>^%Z</strong></p></li>
<li><p><strong>^%ZTSK</strong></p></li>
<li><p><strong>^%ZTSCH</strong></p></li>
<li><p><strong>^%ZOSF</strong></p></li>
<li><p><strong>^%ZIS(“C”)</strong> and <strong>^%ZIS(“H”)</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>1</td>
<td><strong>ANSI</strong></td>
<td>05/14/1990</td>
<td>TaskMan routines can use extended global references.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2B</td>
<td><strong>Exclusive &amp; Argumentless KILL</strong></td>
<td>05/14/1990</td>
<td>The Submanager of TaskMan can use exclusive <strong>KILL</strong> commands in the portion of the Submanager that is responsible for recycling the partition.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2A</td>
<td><strong>H XUS</strong></td>
<td>05/14/1990</td>
<td>The routine <strong>%ZTM</strong> can use the <strong>HALT</strong> command.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2A</td>
<td><strong>OPEN, CLOSE device</strong></td>
<td>05/14/1990</td>
<td>TaskMan routines can use direct <strong>OPEN</strong> and <strong>CLOSE</strong> commands.</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td><strong>ANSI</strong></td>
<td>06/18/1990</td>
<td>Kernel can use operating-specific code, which uses many implementation-specific language features.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>3A</td>
<td><strong>Namespacing</strong></td>
<td>06/18/1990</td>
<td>Kernel can export <strong>Z</strong> namespaced routines and <strong>XUCI*</strong>, <strong>DIDT*</strong>, and <strong>DIRCR</strong> to be renamed as <strong>%</strong> routines when installed.</td>
</tr>
<tr class="even">
<td>10</td>
<td>2B</td>
<td><strong>Exclusive &amp; Argumentless KILL</strong></td>
<td>06/18/1990</td>
<td>The Kernel login (<strong>XUS</strong>) and the Error Trap restore variable routines (<strong>XTER*</strong>) can use exclusive <strong>KILL</strong> statements.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>4A</td>
<td><strong>DUZ-array SET &amp; KILL</strong></td>
<td>06/18/1990</td>
<td><p>The following Kernel routines can <strong>SET</strong> or <strong>KILL</strong> the <strong>DUZ</strong> variable:</p>
<ul>
<li><p><strong>ZTM*</strong></p></li>
<li><p><strong>ZTEDIT3</strong></p></li>
<li><p><strong>XQSMD31</strong></p></li>
<li><p><strong>XQSRV</strong></p></li>
<li><p><strong>XQ1</strong></p></li>
<li><p><strong>XQ12</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>12</td>
<td>2A</td>
<td><strong>OPEN, CLOSE device</strong></td>
<td>06/18/1990</td>
<td>The Device Handler and Kernel Operating-specific code can issue direct <strong>OPEN</strong> and <strong>CLOSE</strong> commands.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>2A</td>
<td><strong>H XUS</strong></td>
<td>06/18/1990</td>
<td>Kernel (Signon/Security) can issue a <strong>HALT</strong> command in the routines <strong>ZU*</strong> without using the <strong>^XUSCLEAN</strong> entry point.</td>
</tr>
<tr class="even">
<td>14</td>
<td>9B</td>
<td><strong>%ZOSF nodes</strong></td>
<td>06/18/1990</td>
<td>Kernel Operating-specific code can make direct calls to operating system routines rather than using the <strong>^%ZOSF</strong> global.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2D2</td>
<td><strong>* &amp; # READs</strong></td>
<td>11/29/1990</td>
<td>Kernel can use a <strong>#255</strong> READ in the <strong>ZOSV*</strong> routines.</td>
</tr>
<tr class="even">
<td>16</td>
<td>2B</td>
<td><strong>Exclusive &amp; Argumentless KILL</strong></td>
<td>02/07/1991</td>
<td>Kernel can use an exclusive <strong>KILL</strong> in the utility to clean up variables when exiting from an option.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>8A</td>
<td><strong>Queueing, $I</strong></td>
<td>07/12/1993</td>
<td>Kernel is granted an exemption for the <strong>XUPR-RTN-TAPE-CMP</strong> option to be <em>non</em>-queueable.</td>
</tr>
<tr class="even">
<td>18</td>
<td>NA</td>
<td>NA</td>
<td>12/07/1994</td>
<td><p>Permanent exemption for Kernel 8.0 to use the following M language Features:</p>
<ul>
<li><p><strong>Merge</strong> Command</p></li>
<li><p><strong>$Order</strong> with two arguments</p></li>
<li><p><strong>$Get</strong> with two arguments</p></li>
<li><p><strong>$Name</strong></p></li>
<li><p>Set <strong>$Extract</strong></p></li>
<li><p>Pattern match with alternation</p></li>
<li><p>Sorts After operator</p></li>
<li><p>Missing parameters in calling list</p></li>
<li><p>Set <strong>$X</strong> and <strong>$Y</strong></p></li>
<li><p><strong>10k</strong> routine size</p></li>
<li><p><strong>$Qlength</strong></p></li>
<li><p><strong>$Qsubscript</strong></p></li>
<li><p><strong>$Principal</strong></p></li>
<li><p>All Structured System Variable Names (SSVNs)</p></li>
<li><p>M standard Error Processing</p></li>
<li><p>Global subscript length <em>not</em> to exceed <strong>240</strong> character (KIDS <em>only</em>) or <strong>200</strong> characters for the remainder of Kernel. Length is determined by algorithm in 1994 draft SAC.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>19</td>
<td>NA</td>
<td>NA</td>
<td>12/07/1994</td>
<td>Permanent exemption for Kernel Installation and Distribution System (KIDS) to Set <strong>DUZ</strong> and <strong>DUZ(0)</strong>.</td>
</tr>
</tbody>
</table>

<span id="_Ref381880235" class="anchor"></span>Table 34: Globals in Production Account—Protection, Translation and Journaling Information

# Global Protection, Translation, and Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An outline of a possible scheme for the management of Kernel globals is presented in this section.

Cookbook recommendations should also be consulted. DSM for OpenVMS sites should refer to the most recent *VAX DSM Systems Guide* (otherwise known as the Cookbook) for recommendations concerning global characteristics.

Kernel’s recommendations and the cookbooks’ recommendations should serve as examples as you manage your site’s global configuration.

## Globals in Production Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref173417736" class="anchor"></span>Table 35: Kernel and Kernel Toolkit Mail Groups</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 33%" />
<col style="width: 23%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>Global Name</th>
<th>DSM for OpenVMS Protection</th>
<th>Translate?</th>
<th>Journal? / Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>^DIC</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td>See <em>VA FileMan Technical Manual</em></td>
</tr>
<tr class="even">
<td><strong>^HOLIDAY</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>^TMP</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
<tr class="even">
<td><strong>^USC</strong></td>
<td>N/A</td>
<td>Yes</td>
<td>The PERSON CLASS file is in the <strong>^USC</strong> global. Please be sure to place this global and add it to your translation tables. This is a static file.</td>
</tr>
<tr class="odd">
<td><strong>^UTILITY</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
<tr class="even">
<td><strong>^VA</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td><strong>^XMB</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td>See <em>MailMan Technical Manual</em></td>
</tr>
<tr class="even">
<td><strong>^XMBS</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td>See <em>MailMan Technical Manual</em></td>
</tr>
<tr class="odd">
<td><strong>^XPD</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>^XTV</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td><strong>^XTMP</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>^XUSEC</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>^XUTL</strong></td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td><ul>
<li><p><strong>^XUTL</strong> = Separate Copy per CPU.</p></li>
<li><p><strong>^XUTL(“XGATR”)</strong> = Translated.</p></li>
<li><p><strong>^XUTL(“XQKB”)</strong> = Translated.</p></li>
<li><p><strong>^XUTL(“XQO”)</strong> = Translated.</p></li>
<li><p><strong>^XUTL(“XQORM”)</strong> = Translated.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><strong>^%ZIS</strong></td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Yes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>^%ZISL</strong></td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Yes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><strong>^%ZOSF</strong></td>
<td><p>System: RWP</p>
<p>World: R</p>
<p>Group: R</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Separate Copy per CPU</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>^%ZTER</strong></td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Yes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><strong>^%ZTSCH</strong></td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Yes*</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>^%ZTSK</strong></td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td><ul>
<li><p>Yes*</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><strong>^%ZUA</strong></td>
<td><p>System: RWP</p>
<p>World: R</p>
<p>Group: RW</p>
<p>UCI: RW</p></td>
<td><ul>
<li><p>Yes</p></li>
</ul></td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Ref173417736" class="anchor"></span>Table 35: Kernel and Kernel Toolkit Mail Groups

There should be only one copy of the TaskMan globals (^%ZTSCH and ^%ZTSK) within TaskMan’s reach. At VA sites, TaskMan’s reach is across all CPUs. Other sites should evaluate TaskMan’s reach in their configurations. Also, at DSM for OpenVMS sites, these globals should *not* be in a volume set that is cluster-mounted across all systems; instead, master from two nodes and DDP server to the other nodes.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/121.png) REF: For more information about TaskMan’s reach, see the [*Kernel 8.0 Systems Management” TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf).

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Otherwise, there are no special legal requirements involved in the use of Kernel.

## Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and Kernel Toolkit did *not* originally create or use any specific mail groups, but it provided fields, files, options, APIs, and utilities for creating/processing mail groups. Through the years, however, Kernel and Kernel Toolkit have distributed the mail groups in <u>Table 35</u>:

| Mail Group Name           | Description |
|---------------------------|-------------|
| XIP POSTAL CODE UPDATE    | TBD         |
| XIP SERVER RESPONSE       | TBD         |
| XQAL UNPROCESSED ALERTS   | TBD         |
| XQSERVER                  | TBD         |
| XTER SUMMARY ERROR        | TBD         |
| XTER SUMMARY LOAD         | TBD         |
| XTPM PATCH MONITOR        | TBD         |
| XTPM PATCH MONITOR USER   | TBD         |
| XUHUI CHANGE EVENT        | TBD         |
| XUMF ERROR                | TBD         |
| XUMF INSTITUTION          | TBD         |
| XUMF NPI                  | TBD         |
| XUMF SERVER               | TBD         |
| XUOAA CLIN TRAINEE        | TBD         |
| XUOAA CLIN TRAINEE TRANS  | TBD         |
| XUSEC/PRS PAID SEPARATION | TBD         |
| XUSSPKI CRL SERVER        | TBD         |

<span id="_Ref354998247" class="anchor"></span>Table 36: Bulletins—Kernel and Kernel Toolkit

### Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and Kernel Toolkit do *not* make use of alerts itself, but it does provide fields, files, options, APIs, and utilities for creating/processing alerts.

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 36</u> lists the bulletins distributed with Kernel and Kernel Toolkit:

<table>
<caption><p><span id="_Ref355083482" class="anchor"></span>Table 37: Security Keys—Kernel and Kernel Toolkit</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Subject</th>
<th>Message</th>
<th>Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XDR ERROR</strong></td>
<td>This bulletin is sent by the Kernel Duplicate Resolution software when an error that halts the process is encountered by a background task. It is only sent if there is an entry in the Duplicate Manager mail group in the DUPLICATE RESOLUTION (#15.1) file.</td>
<td>ERROR DURING DUPLICATE CHECKING OR MERGE</td>
<td><p>|NOWRAP| This is to notify you that an error was encountered while trying to either check for duplicates or during the early merge process of the |1| file.</p>
<p>From DA/DFN: |2|</p>
<p>To DA/DFN: |3|</p>
<p>|4| |5|</p>
<p>|WRAP| |6|</p></td>
<td><ul>
<li><p><strong>1—</strong>File from which the two records come from.</p></li>
<li><p><strong>2—From</strong> record’s DA/DFN.</p></li>
<li><p><strong>3—To</strong> record’s DA/DFN.</p></li>
<li><p><strong>4—</strong>Internal value of the <strong>.01</strong> field of the <strong>From</strong> Record.</p></li>
<li><p><strong>5—</strong>Internal value of the <strong>.01</strong> field of the <strong>To</strong> Record.</p></li>
<li><p><strong>6—</strong>Error condition that was encountered.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XDR MERGED</strong></td>
<td><p>This bulletin is sent by the Kernel Duplicate Resolution software when a Verified Duplicate pair is merged.</p>
<p>This bulletin is sent only if a package merge developer does <em>not</em> have a routine that sends its own customized merge message.</p></td>
<td>NOTIFICATION OF DUPLICATES MERGED</td>
<td><p>|WRAP| The following records from the |1| file have been merged.</p>
<p>|NOWRAP|</p>
<p>From record DA/DFN: |2|</p>
<p>To record DA/DFN: |3|</p>
<p>|4| |5|</p>
<p>|WRAP| The FROM Record has now been merged to the TO Record. |NOWRAP|</p>
<p>|6|</p></td>
<td><ul>
<li><p><strong>1—</strong>File from which the two records come from.</p></li>
<li><p><strong>2—From</strong> record’s DA/DFN.</p></li>
<li><p><strong>3—To</strong> record’s DA/DFN.</p></li>
<li><p><strong>4—</strong>Internal value of the <strong>.01</strong> field of the <strong>From</strong> Record.</p></li>
<li><p><strong>5—</strong>Internal value of the <strong>.01</strong> field of the <strong>To</strong> Record.</p></li>
<li><p><strong>6—</strong>Package merge error listing header.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XDR VERIFIED</strong></td>
<td><p>This bulletin is sent by the Kernel Duplicate Resolution software anytime a pair of Potential Duplicates is reviewed, and the operator determines that the pair is indeed Verified Duplicates.</p>
<p>This bulletin is sent only if a package merge developer does <em>not</em> have a routine that sends its own customized verified message.</p></td>
<td>NOTIFICATION OF VERIFIED DUPLICATES</td>
<td><p>|WRAP| The following records have been identified as Verified Duplicates of the |1| file: |NOWRAP|</p>
<p>From record DA/DFN: |2|</p>
<p>To record DA/DFN: |3|</p>
<p>|4| |5|</p>
<p>|WRAP| The FROM record will be merged to the TO record. Please resolve any package discrepancies so that the merge may proceed.</p></td>
<td><ul>
<li><p><strong>1—</strong>File from which the two records come from.</p></li>
<li><p><strong>2—From</strong> record’s DA/DFN.</p></li>
<li><p><strong>3—To</strong> record’s DA/DFN.</p></li>
<li><p><strong>4—</strong>Internal value of the <strong>.01</strong> field of the <strong>From</strong> Record.</p></li>
<li><p><strong>5—</strong>Internal value of the <strong>.01</strong> field of the <strong>To</strong> Record.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XQSERVER</strong></td>
<td>This is the standard, or default, bulletin used by the menu system to notify system administrators and users about server request events.</td>
<td>Server Request Notice</td>
<td><p>|1|</p>
<p>A request for execution of a server option has been received.</p>
<p>Sender: |2| Option name: |3| Subject: |4| Message #: |5| Comments: |6|</p></td>
<td><ul>
<li><p><strong>1—</strong>Date and time in human-readable form when the server request was received.</p></li>
<li><p><strong>2—</strong>Name of the sender of the server request.</p></li>
<li><p><strong>3—</strong>Name of the option that was requested by Mailman.</p></li>
<li><p><strong>4—</strong>Subject of the message which requested a server.</p></li>
<li><p><strong>5—</strong>Internal number of the message requesting a server.</p></li>
<li><p><strong>6—</strong>Comments appended to the bulleting. These may include errors trapped by the server software and/or the operating system, as well as general purpose messages.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="XTRMON_bulletin" class="anchor"></span><strong>XTRMON</strong></td>
<td>This bulletin is used by the <strong>XTRMON</strong> routine to send mail messages about routines that change in the set of routines being tracked.</td>
<td>Changes to routines</td>
<td>A check of the routines in |3| on |1| showed that |2| routines changed, here is the list:</td>
<td></td>
</tr>
<tr class="even">
<td><strong>XU-INSTALL-DONE</strong></td>
<td>This bulletin sends a message back to the developers when an install has been done.</td>
<td>Install of package done.</td>
<td><p>Package ‘|1|’ version |2| was installed at site |4| by |5|.</p>
<p>Timing data:</p>
<p>INIT started at |6|</p>
<p>Pre-INIT started at |7|</p>
<p>Pre-INIT finished at |8|</p>
<p>Post-INIT started at |9|</p>
<p>and finished at |3|</p>
<p>For a TOTAL of |10| (hh:mm:ss).</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>XUMF ERROR</strong></td>
<td>This bulletin is triggered upon receipt of a Master File Notification message from the Master File Server.</td>
<td>Master File Server - error message</td>
<td><p>The Master File Server has received a Message Acknowledgement (MSA) segment with an Acknowledgement Code indicating an application error for the following message:</p>
<p>HL7 Message ID: |1|</p>
<p>Server message:</p>
<p>|2|</p>
<p>HL7, FM, or other message:</p>
<p>|3|</p>
<p>|4|</p>
<p>This message <em>must</em> be investigated, or the master file related to this message will be out of sync with the national standard table.</p></td>
<td><ul>
<li><p><strong>1—</strong>Message Control ID.</p></li>
<li><p><strong>2—</strong>Message from MFS.</p></li>
<li><p><strong>3—</strong>Message from HL7 application, VA FileMan (FM), or other source.</p></li>
<li><p><strong>4—</strong>FM error message.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUMF INSTITUTION</strong></td>
<td>This bulletin notifies the XUMF INSTITUTION mail group that an unsolicited update message has been received and processed by the Master File Server (MFS) mechanism. An INSTITUTION (#4) file entry has been added / updated.</td>
<td>Master File Server - update notification - INSTITUTION file</td>
<td><p>The following Master File Notification (MFN) message was received and processed by the Master File Server:</p>
<p>HL7 Message ID: |1|</p>
<p>The following INSTITUTION (#4) file entry has been |2|:</p>
<p>IEN: |3| STATION NUMBER: |4|</p>
<p>UPDATED ENTRY</p>
<p>-------------</p>
<p>NAME: |5|</p>
<p>OFFICIAL VA NAME: |6|</p>
<p>FACILITY TYPE: |7|</p>
<p>INACTIVE FACILITY FLAG: |11|</p>
<p>VISN: |13|</p>
<p>PARENT FACILITY: |14|</p>
<p>STREET ADDR. 1: |19|</p>
<p>CITY: |20|</p>
<p>STATE: |12|</p>
<p>ZIP: |22|</p>
<p>ST. ADDR. 1 (MAILING): |23|</p>
<p>CITY (MAILING): |24|</p>
<p>STATE (MAILING): |25|</p>
<p>ZIP (MAILING): |26|</p>
<p>OLD VALUES</p>
<p>----------</p>
<p>NAME: |8|</p>
<p>OFFICIAL VA NAME: |9|</p>
<p>FACILITY TYPE: |10|</p>
<p>INACTIVE FACILITY FLAG: |15|</p>
<p>VISN: |17|</p>
<p>PARENT FACILITY: |18|</p>
<p>STREET ADDR. 1: |27|</p>
<p>CITY: |28|</p>
<p>STATE: |16|</p>
<p>ZIP: |29|</p>
<p>ST. ADDR. 1 (MAILING): |30|</p>
<p>CITY (MAILING): |31|</p>
<p>STATE (MAILING): |32|</p>
<p>ZIP (MAILING): |33|</p></td>
<td><ul>
<li><p><strong>1—</strong>Message ID.</p></li>
<li><p><strong>2—</strong>Added or Updated.</p></li>
<li><p><strong>3—</strong>Internal Entry Number.</p></li>
<li><p><strong>4—</strong>STATION NUMBER.</p></li>
<li><p><strong>5—</strong>NAME.</p></li>
<li><p><strong>6—</strong>OFFICIAL VA NAME.</p></li>
<li><p><strong>7—</strong>FACILITY TYPE.</p></li>
<li><p><strong>8—</strong>OLD NAME.</p></li>
<li><p><strong>9—</strong>OLD OFFICIAL VA NAME.</p></li>
<li><p><strong>10—</strong>OLD FACILITY TYPE.</p></li>
<li><p><strong>11—</strong>INACTIVE FACILITY FLAG.</p></li>
<li><p><strong>12—</strong>STATE.</p></li>
<li><p><strong>13—</strong>VISN.</p></li>
<li><p><strong>14—</strong>PARENT FACILITY.</p></li>
<li><p><strong>15—</strong>OLD INACTIVE FACILITY FLAG.</p></li>
<li><p><strong>16—</strong>OLD STATE.</p></li>
<li><p><strong>17—</strong>OLD VISN.</p></li>
<li><p><strong>18—</strong>OLD PARENT FACILITY.</p></li>
<li><p><strong>19—</strong>STREET ADDR. 1.</p></li>
<li><p><strong>20—</strong>CITY.</p></li>
<li><p><strong>22—</strong>ZIP.</p></li>
<li><p><strong>23—</strong>ST. ADDR. 1 (MAILING).</p></li>
<li><p><strong>24—</strong>CITY (MAILING).</p></li>
<li><p><strong>25—</strong>STATE (MAILING).</p></li>
<li><p><strong>26—</strong>ZIP (MAILING).</p></li>
<li><p><strong>27—</strong>OLD STREET ADDR. 1.</p></li>
<li><p><strong>28—</strong>OLD CITY.</p></li>
<li><p><strong>29—</strong>OLD ZIP.</p></li>
<li><p><strong>30—</strong>OLD ST. ADDR. 1 (MAILING).</p></li>
<li><p><strong>31—</strong>OLD CITY (MAILING).</p></li>
<li><p><strong>32—</strong>OLD STATE (MAILING).</p></li>
<li><p><strong>33—</strong>OLD ZIP (MAILING).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUPROGMODE</strong></td>
<td>User going into <strong>Programmer</strong> mode message.</td>
<td>DROPPING INTO PROGRAMMER MODE</td>
<td>User # |1| has dropped into programmer mode on device |2|</td>
<td><ul>
<li><p><strong>1—</strong>User name.</p></li>
<li><p><strong>2—</strong>Device.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUS ACCESS CODE VIOLATION</strong></td>
<td><p>This bulletin is sent by the Syntax check of the ACCESS CODE field of the USER file, whenever someone tries to assign an ACCESS CODE that is already in use for a different user.</p>
<p>The bulletin goes to whoever is in the mail group, plus the user who tried to input the code.</p></td>
<td>A USER HAS SEEN ANOTHER USER’S ACCESS CODE</td>
<td>The user above tried to assign the ACCESS CODE that already belonged to |1|. |1| should change his/her code as soon as possible, since its secrecy has now been compromised.</td>
<td><ul>
<li><p><strong>1—</strong>Name of the USER whose ACCESS CODE was discovered.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSECURITY</strong></td>
<td>This bulletin is sent by the signon system if a user uses a terminal that has SECURITY to sign on, and his <strong>DUZ(0)</strong> code is <em>not</em> found in the terminal’s SECURITY code, as the FILE MANAGER ACCESS CODE attempts to sign on.</td>
<td>SIGN-ON DISALLOWED ON SECURED TERMINAL</td>
<td>User |1| tried to sign on to device |2|, which has SECURITY code |3|, but |1| has security code ‘|4|’. Use <strong>^UTIO</strong> to edit the device’s SECURITY, if necessary.</td>
<td><ul>
<li><p><strong>1—</strong>Name of User.</p></li>
<li><p><strong>2—</strong>Device.</p></li>
<li><p><strong>3—</strong>Device’s security code.</p></li>
<li><p><strong>4—</strong>User’s security code.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUSERDEAC</strong></td>
<td>This bulletin is sent to the ISO SECURITY mail group when a user gets deactivated.</td>
<td>XUSER DEACTIVATION</td>
<td><p>User name : |1|</p>
<p>Title: |2|</p>
<p>Service: |3|</p>
<p>IEN: |4|</p>
<p>Station #: |5|</p>
<p>was deactivated on |6|.</p></td>
<td><ul>
<li><p><strong>1—</strong>Name of user who gets deactivated.</p></li>
<li><p><strong>2—</strong>Title.</p></li>
<li><p><strong>3—</strong>Service.</p></li>
<li><p><strong>4—</strong>Internal Entry Number (IEN).</p></li>
<li><p><strong>5—</strong>Station Number and Name.</p></li>
<li><p><strong>6—</strong>Deactivation Date.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSERDIS</strong></td>
<td>This bulletin is sent to the ISO SECURITY mail group when a user has the <strong>DISUSER</strong> field set to <strong>YES</strong>.</td>
<td>USER DISUSER</td>
<td><p>User name : |1|</p>
<p>Title: |2|</p>
<p>Service: |3|</p>
<p>IEN: |4|</p>
<p>Station #: |5|</p>
<p>was deactivated on |6|.</p></td>
<td><ul>
<li><p><strong>1—</strong>Name of user who gets deactivated.</p></li>
<li><p><strong>2—</strong>Title.</p></li>
<li><p><strong>3—</strong>Service.</p></li>
<li><p><strong>4—</strong>Internal Entry Number (IEN).</p></li>
<li><p><strong>5—</strong>Station Number and Name.</p></li>
<li><p><strong>6—</strong>Deactivation Date.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUSERTERM</strong></td>
<td>This bulletin is issued whenever a message <em>cannot</em> be delivered after the Simple Mail Transfer Protocol (SMTP) <strong>DATA</strong> command is issued. It indicates that the “<strong>Mail From:</strong>” and <strong>RCPT</strong> (recipient) commands were successfully issued, but that something in the header of the message was rejected, such as duplicate message ID. The error message returned by the remote receiver is included in the bulletin.</td>
<td>USER TERMINATION</td>
<td>USER |1| has been terminated as of |2| The error message was ‘|3|’.</td>
<td><ul>
<li><p><strong>1—</strong>Name of the remote site rejecting the message (may be intermediate relay).</p></li>
<li><p><strong>2—</strong>Title and message number of message which was rejected.</p></li>
<li><p><strong>3—</strong>Rejection message issued by the rejecting receiver.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSIGNON</strong></td>
<td>This bulletin is triggered whenever someone signs on through <strong>XUS</strong>.</td>
<td>USER SIGNING ON</td>
<td>User |2| has signed on at Device |3|.</td>
<td><ul>
<li><p><strong>1—</strong>User number (‘<strong>DUZ</strong>’) of user signing on.</p></li>
<li><p><strong>2—</strong>Name of user.</p></li>
<li><p><strong>3—</strong>Device at which sign-on occurred.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUSLOCK</strong></td>
<td>This bulletin is triggered when the number of bad signons causes a terminal device or IP address to be “locked out”.</td>
<td>DEVICE LOCKED DUE TO BAD SIGN-ONS</td>
<td><p>Device |1| has made |2| bad sign-on attempts and has been locked.</p>
<p>The device will automatically clear after the Lockout time in the Kernel System Parameters. To make the device or IP address useable before the lockout time is up use the “CLEAR TERMINAL” or “Release IP lock” option to make the device available again. Select |3| as the device to release.</p></td>
<td><ul>
<li><p><strong>1—</strong>Name of device being locked.</p></li>
<li><p><strong>2—</strong>Number of bad signons recorded for the device.</p></li>
<li><p><strong>3—</strong>Name of the device to release.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSSPKI CRL SERVER</strong></td>
<td>This bulletin is sent when the CRL UPLOAD TASK has a problem.</td>
<td>CRL UPLOAD MESSAGE</td>
<td><p>At |2| The CRL Upload task reported the following problem.</p>
<p>“|1|”</p>
<p>Be sure that the “CRLService” is running on the server. Try stopping and restarting the service. It should be listening on a specific port.</p></td>
<td><ul>
<li><p><strong>1—</strong>Error message.</p></li>
<li><p><strong>2—</strong>Date time of the message.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUSSPKI SAN</strong></td>
<td><p>This bulletin is sent when the SUBJECT ALTERNATIVE NAME (#501.2) field in the NEW PERSON (#200) file has been changed or deleted. The bulletin is sent to users holding the <strong>PSDMGR</strong> security key.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/122.png) <strong>NOTE:</strong> Released with Kernel Patch XU*8.0*580.</p></td>
<td>“Subject Alternative Name” field</td>
<td>The “Subject Alternative Name” field in New Person File (#200) has been changed or deleted for: <strong>|3|</strong><br />
<br />
Before: <strong>|1|</strong><br />
<br />
After: <strong>|2|</strong></td>
<td><ul>
<li><p><strong>1—</strong>Old value before changed or deleted.</p></li>
</ul>
<ul>
<li><p><strong>2—</strong>New value. If <strong>NULL</strong>, value was deleted.</p></li>
<li><p><strong>3—</strong>Name of the user.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSTIME</strong></td>
<td>This bulletin is triggered by the Signon system if the device being used has a “PROHIBITED SIGN-ON TIMES” value, and somebody has tried to sign on during that prohibited time-period; the prohibited time frame.</td>
<td>SIGN-ON TO A TERMINAL DURING PROHIBITED TIME</td>
<td>“|2|” attempted to sign on to device |1| with code “|3|”, but the device is locked out during the time-period |4|.</td>
<td><ul>
<li><p><strong>1—</strong>Device name (<strong>$I</strong>).</p></li>
<li><p><strong>2—</strong>User name.</p></li>
<li><p><strong>3—</strong>Access Code used for sign-on.</p></li>
<li><p><strong>4—</strong>Time range during which sign-on is prohibited.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>XUTM PROBLEM DEVICES</strong></td>
<td>This bulletin is used by the <strong>XUTMKA</strong> routine to report devices that TaskMan is having problems opening.</td>
<td>Problem Devices</td>
<td>This is the <strong>XUTM PROBLEM DEVICE</strong> bulletin; it reports devices that TaskMan is having problems opening. The list shows the <strong>$I</strong> value for the device.</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>XUVISIT</strong></td>
<td>This is the default <strong>XUESSO</strong> bulletin that is issued at the time a new visitor is entered in the NEW PERSON (#200) file. A “visitor” is a user who has been validated at another VA site and is entered in your data base, so that he or she may look up patient data.</td>
<td>A visitor has been added to your New Person File</td>
<td><p>|1|</p>
<p>A visitor has been added to your New Person File with no Access or Verify Codes.</p>
<p>Name: |2|</p>
<p>DUZ: |3|</p>
<p>This visitor was authenticated at |4|, (|5|). This user has a DUZ of |6| on the authenticating system, and a phone number of |7|.</p>
<p>This is the bulletin named XUVISIT.</p></td>
<td><ul>
<li><p><strong>1—</strong>Title/date of this bulletin.</p></li>
<li><p><strong>2—</strong>Name of the visitor.</p></li>
<li><p><strong>3—DUZ</strong> of this visitor in the New Person File.</p></li>
<li><p><strong>4—</strong>Name of the site where the visitor was authenticated.</p></li>
<li><p><strong>5—</strong>Number of the site where the visitor was authenticated.</p></li>
<li><p><strong>6—</strong>Visitors <strong>DUZ</strong> at the authenticating site.</p></li>
<li><p><strong>7—</strong>Visitor’s phone number at the authenticating site.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref355083482" class="anchor"></span>Table 37: Security Keys—Kernel and Kernel Toolkit

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides options and utilities for accessing remote (and local) systems.

## Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel interfaces with the following VA products:

- Kernel Toolkit 7.3 or higher.
- VA FileMan 22.2 or higher.
- MailMan 8.0 or higher.

The Assigning Person Class to Providers software (that is Kernel Patches XU\*8.0\*27, 377, and 531) allows for interfaces with all VistA Clinical Software developed in-house. It also allows for interfaces with the QuadraMed Encoder Product Suite, which is a Commercial-Off-The-Shelf (COTS; *non*-VA) software product.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/123.png) REF: For more information on QuadraMed products, see the QuadraMed website at the following Web address: [Quadramed Website](https://www.quadramed.com/)

Kernel and Kernel Toolkit do *not* embed or require any special interfaces to any other COTS (*non*-VA) products; other than those provided by the underlying operating systems.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and Kernel Toolkit do *not* use any electronic signatures within the software itself; however, it does provide fields, files, options, APIs, and utilities for creating and processing electronic signatures.

### Electronic Signature Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch XU\*8.0\*679, the system restricts access to electronic signature fields in the NEW PERSON (#200) file for sites that elect to enable this functionality. Prior to Patch XU\*8.0\*679, any user could access the following fields in the NEW PERSON (#200) file through the Electronic Signature options on the VistA User's Toolbox \[XUSERTOOLS\] menu:

- DEGREE (#10.6)
- SIGNATURE BLOCK PRINTED NAME (#20.2)
- SIGNATURE BLOCK TITLE (#20.3)

If restrictions are enabled, then access to these fields is allowed only for users who are assigned the XUSIG security key.

To enable restrictions, authorized site personnel *must* set the XU SIG BLOCK DISABLE general parameter to a value of ON (1). The parameter definition is stored in the PARAMETER DEFINITION (#8989.51) file, and the parameter data is stored in the PARAMETER (#8989.5) file:

- If the XU SIG BLOCK DISABLE parameter is set to ON and the user has the XUSIG security key assigned in the NEW PERSON (#200), then access to the restricted fields is allowed.
- If the XU SIG BLOCK DISABLE parameter is set to ON, but the user does *not* have the XUSIG security key assigned, then access to the restricted fields is *not* allowed.
- If the site leaves the XU SIG BLOCK DISABLE parameter set to OFF (0), then access to all electronic signature fields is allowed.

The following two options on the VistA User's Toolbox \[XUSERTOOLS\] menu were affected by Patch XU\*8.0\*679:

- Electronic Signature Code Edit \[XUSESIG\]
- Electronic Signature Block Edit \[XUSESIG BLOCK\]

If the XU SIG BLOCK DISABLE parameter is set to ON, then only supervisors holding the XUSIG security key can update the SIGNATURE BLOCK PRINTED NAME (#20.2) and SIGNATURE BLOCK TITLE (#20.3) fields through the Electronic Signature Code Edit \[XUSESIG\] option, and the SIGNATURE BLOCK PRINTED NAME (#20.2) and DEGREE (#10.6) fields through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option. In addition, the patch enables access to the SIGNATURE BLOCK TITLE (#20.3) field through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option. This allows supervisors holding the XUSIG security key to enter the SIGNATURE BLOCK TITLE (#20.3) for other users after the XU SIG BLOCK DISABLE parameter is set to ON.

To maintain valid educational credentials, DEGREE (#10.6) field entries made through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option are restricted to valid degrees stored in the EDUCATION (#20.11) file. To support this functionality, Patch XU\*8.0\*679 added the EDUCATION (Degree) File Edit \[XUSESIG DEG\] option to the User Management \[XUSER\] menu. The EDUCATION (Degree) File Edit \[XUSESIG DEG\] option, which is locked by the XUSIG security key, enables maintenance of DEGREE field entries in the EDUCATION (#20.11) file. VistA uses these records to validate user entries when appending one or more degrees to an electronic signature. This validation applies even when the XU SIG BLOCK DISABLE parameter is set to OFF.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/124.png) NOTE: Because VistA automatically cross-references DEGREE (#10.6) field entries in the NEW PERSON (#200) with the DEGREE (#6) field in the NAME COMPONENTS (#20) file, any updates made directly to the DEGREE (#6) field in the NAME COMPONENTS (#20) file will also be validated against degrees in the EDUCATION (#20.11) file.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a list of security keys exported with Kernel and Kernel Toolkit, use the VA FileMan Inquire to File Entries option \[DIINQUIRE\] as shown in <u>Figure 19</u>.

<span id="_Ref333476680" class="anchor"></span>Figure 19: Security Keys—Obtaining Security Key Information for Kernel

Select OPTION: <span class="mark">INQUIRE \<Enter\></span> TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION// <span class="mark">SECURITY \<Enter\></span> KEY (119 entries)

Select SECURITY KEY NAME: <span class="mark">XU</span>

1 XUARCHIVE

2 XUAUDITING

3 XUAUTHOR

4 XUEXKEY

5 XUFILEGRAM

Press \<RETURN\> to see more, ‘^’ to exit this list, OR

CHOOSE 1-5: <span class="mark">\<Enter\></span>...

<table>
<caption><p><span id="_Toc205036230" class="anchor"></span>Table 38: Glossary of Terms and Acronyms</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Security Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XDR</strong></td>
<td>This security key allows access to the Duplicate Resolution System.</td>
</tr>
<tr class="even">
<td><strong>XDRMGR</strong></td>
<td><p>This security key allows a user access to the Kernel Duplicate Resolution Manager Utilities.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/125.png) ATTENTION: This security key should only be given to the people responsible for management of the various Duplicate Resolution packages (such as Patient Registration).</p></td>
</tr>
<tr class="odd">
<td><strong>XQAL-DELETE</strong></td>
<td>This security key permits a user to delete alerts associated with another user. This key <em>must</em> be held for the user to have this capability.</td>
</tr>
<tr class="even">
<td><strong>XQSMDF</strong>M</td>
<td>This security key is required for use of the <strong>XQSMD LIMITED FM</strong> option to permit users to build some options based on VA FileMan templates.</td>
</tr>
<tr class="odd">
<td><strong>XTLKZMGR</strong></td>
<td>This security key unlocks the option to create/modify entries in the ICD files.</td>
</tr>
<tr class="even">
<td><strong>XTLKZUSER</strong></td>
<td>This security key unlocks the <strong>Auto-Coding Utility</strong> [XTLKUSER] menu.</td>
</tr>
<tr class="odd">
<td><strong>XUARCHIVE</strong></td>
<td>This security key is needed to access the <strong>Archiving</strong> menu or to run any of the archiving options.</td>
</tr>
<tr class="even">
<td><strong>XUAUDITING</strong></td>
<td>This security key is needed to access the <strong>Auditing</strong> menu or to run any of the Auditing options.</td>
</tr>
<tr class="odd">
<td><strong>XUAUTHOR</strong></td>
<td>This security key allows the holder to edit all existing help frames, using <strong>^E</strong> when the frame is displayed, as well as allowing the holder to create new frames from within the menu system.</td>
</tr>
<tr class="even">
<td><strong>XUEPCSEDIT</strong></td>
<td><p>This security key is required for individuals who will enter data related to electronic prescribing of controlled substances (eCPS) for providers.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/126.png) CAUTION: The holder of this key <em>CANNOT</em> also hold the XUORES security key. They are exclusive keys and should <em>not</em> both be held by an individual at the same time.</p></td>
</tr>
<tr class="odd">
<td><strong>XUEXKEY</strong></td>
<td>This security key allows access to the <strong>XUEXKEY</strong> option.</td>
</tr>
<tr class="even">
<td><strong>XUFILEGRAM</strong></td>
<td>This security key is needed to access the <strong>Filegram</strong> menu or to run any of the Filegram options except the <strong>View Filegram</strong> option.</td>
</tr>
<tr class="odd">
<td><strong>XULM LOCKS</strong></td>
<td>Controls access to the Kernel Lock Manager.</td>
</tr>
<tr class="even">
<td><strong>XULM SYSTEM LOCKS</strong></td>
<td>Controls access to the system-level locks.</td>
</tr>
<tr class="odd">
<td><strong>XUMF INSTITUTION</strong></td>
<td>This security key locks the <strong>XUMF INSTITUTION</strong> option.</td>
</tr>
<tr class="even">
<td><strong>XUMGR</strong></td>
<td><p>This security key is for users who need to act as site management staff. This key gives the user access to see information that is normally only available to the user that created it. This is a partial list of its uses:</p>
<ul>
<li><p>Allows its holders to create “Routine”-type options in the OPTION (#19) file with bracket syntax ([UCI]) for UCI-switching.</p></li>
<li><p>Allows its holders to see the list of all spool file entries.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUORES</strong></td>
<td><p>This security key is given to <em>Non</em>-VistA persons that are authorized to write orders in the chart.</p>
<p>This security key is typically given to licensed Physicians.</p>
<p>![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/127.png) CAUTION: DO <em>NOT</em> give this security key to anyone who has VistA access. Nor assign it to an individual option or menu.<br />
<br />
Should the person who holds this key become a VistA user then this key should be de-allocated.</p></td>
</tr>
<tr class="even">
<td><strong>XUPROG</strong></td>
<td>Assign this security key to all users allowed to go into programmer options from the menu system.</td>
</tr>
<tr class="odd">
<td><strong>XUPROGMODE</strong></td>
<td>This security key locks the Global List and <strong>Programmer</strong> mode options.</td>
</tr>
<tr class="even">
<td><strong>XUSCREENMAN</strong></td>
<td>This security key is needed to access the <strong>ScreenMan</strong> menu.</td>
</tr>
<tr class="odd">
<td><strong>XUSHOWSSN</strong></td>
<td>This security key allows the user to enter all <strong>9</strong> digits of a person’s Social Security Number (SSN) for look up in the NEW PERSON (#200) file. Any user who does <em>not</em> hold this security key is <em>not</em> allowed to use a <strong>9</strong>-digit SSN lookup on the NEW PERSON (#200) file .</td>
</tr>
<tr class="even">
<td><strong>XUSIG</strong></td>
<td><p>This security key is required to add and edit Electronic Signature fields using the <strong>Electronic Signature code Edit</strong> [XUSESIG] option and <strong>Electronic Signature Block Edit</strong> [XUSESIG BLOCK] options. The following fields in the NEW PERSON (#200) file are affected:</p>
<ul>
<li><p>DEGREE (#10.6)</p></li>
<li><p>SIGNATURE BLOCK PRINTED NAME (#20.2)</p></li>
<li><p>SIGNATURE BLOCK TITLE (#20.3)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XUSNPIMTL</strong></td>
<td>This security key allows users to access the <strong>NPI (National Provider ID)</strong> Menu [XUS NPI MENU] option. This key is normally assigned to the Local NPI Maintenance Team Leader; the person with authority to assign/edit VA Provider NPIs.</td>
</tr>
<tr class="even">
<td><strong>XUSPF200</strong></td>
<td>This security key allows special privileges in the NEW PERSON (#200) file. The first of these is that holders of this key do <em>not</em> have to enter an SSN to add a new person to the file.</td>
</tr>
<tr class="odd">
<td><strong>ZTMQ</strong></td>
<td>This security key allows users to use the advanced features of the TaskMan Dequeue Tasks, Requeue Tasks, and Delete Tasks options.</td>
</tr>
</tbody>
</table>

<span id="_Toc205036230" class="anchor"></span>Table 38: Glossary of Terms and Acronyms

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File number ranges for Kernel and Kernel Toolkit are as follows:

- 3.05 – 3.084
- 3.1 - 3.54
- 4.00 - 4.11
- 5.00 - 5.00
- 7 - 7.1
- 9.2 - 9.8
- 10
- 11
- 13
- 14.4 - 14.8
- 15 – 15.4
- 19.00 – 19.2
- 40.5
- 49
- 101.00
- 200 – 201
- 8932.10 - 8935.91
- 8980 - 8980.22
- 8984.1 – 8984.4
- 8989.2 – 8989.3
- 8991 – 8992.1

To print File Security Access for files for Kernel, go to the Programmer prompt, enter FileMan, and follow the prompts in <u>Figure 20</u>:

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/128.png) NOTE: You can sort by Number and select a range of file numbers. ;Lnn gives you control over column width.

<span id="_Ref87259697" class="anchor"></span>Figure 20: File Security—Sample User Dialog to Obtain File Security

Select OPTION: <span class="mark">PRINT \<Enter\></span> FILE ENTRIES

OUTPUT FROM WHAT FILE: FILE// <span class="mark">\<Enter\></span>

SORT BY: NAME// <span class="mark">NUMBER</span>

START WITH NUMBER: FIRST// <span class="mark">1.0</span>

GO TO NUMBER: LAST// <span class="mark">4.6</span>

WITHIN NUMBER, SORT BY: <span class="mark">\<Enter\></span>

FIRST PRINT ATTRIBUTE: <span class="mark">\[FILE</span>

1 FILE LIST (Aug 01, 1990@18:41) File \#1

2 FILE SECURITY ACCESS

(Aug 16, 2006@11:23) User \#1529 File \#1

3 FILE SECURITY CODES

File \#1

CHOOSE 1-3: <span class="mark">2 \<Enter\></span> (Aug 16, 2006@11:23) User \#1529 File \#1

WANT TO EDIT ‘FILE SECURITY ACCESS’ TEMPLATE? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: FILE SECURITY ACCESS Replace <span class="mark">\<Enter\></span>

READ ACCESS: @// <span class="mark">\<Enter\></span>

WRITE ACCESS: @// <span class="mark">\<Enter\></span>

FIRST PRINT ATTRIBUTE: NUMBER// <span class="mark">NUMBER;L6</span>

THEN PRINT ATTRIBUTE: NAME;L25// <span class="mark">NAME;L30</span>

THEN PRINT ATTRIBUTE: DD ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: RD ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: WR ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: DEL ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: LAYGO ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: AUDIT ACCESS;L3// <span class="mark">\<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">\<Enter\></span>

Heading (S/C): FILE SECURITY ACCESS Replace <span class="mark">\<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">FILE</span>

1 FILE LIST (Aug 01, 1990@18:41) File \#1

2 FILE SECURITY ACCESS

(Jul 10, 2002@10:25) User \#1529 File \#1

CHOOSE 1-2: <span class="mark">2 \<Enter\></span> (Jul 10, 2002@10:25) User \#1529 File \#1

TEMPLATE ALREADY STORED THERE.... OK TO REPLACE? <span class="mark">Y \<Enter\></span> (Yes)

START AT PAGE: 1// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Telnet terminal

<u>Figure 21</u> lists the *recommended* file security settings for access to Kernel and Kernel Toolkit files:

<span id="_Ref333476122" class="anchor"></span>Figure 21: File Security—Recommended Kernel File Security Access

FILE SECURITY ACCESS May 16,2013 11:32 PAGE 1

DD RD WR DEL LAYGO AUDIT

NAME NUMBER ACCESS ACCESS ACCESS ACCESS ACCESS ACCESS

----------------------------------------------------------------------------------------

FAILED ACCESS ATTEMPTS LOG 3.05 @ @ @ @ @

PROGRAMMER MODE LOG 3.07 @ @ @ @ @

ERROR LOG 3.075

ERROR MESSAGES 3.076

ERROR TRAP SUMMARY 3.077

SIGN-ON LOG 3.081 @ @ @ @ @ @

LOCKED IP or DEVICE 3.083 @ @ \# @ @ @

FAILED SIGNON ATTEMPTS 3.084 @ @ \# @ @ @

TITLE 3.1 \# @ @ \# @ \#

TERMINAL TYPE 3.2 \# \# \# \# \#

DA RETURN CODES 3.22

LINE/PORT ADDRESS 3.23 @ @ @ @ @ @

DEVICE 3.5 \# I \# \# \# \#

SPOOL DOCUMENT 3.51 @ @ @ @ @ @

SPOOL DATA 3.519

RESOURCE 3.54

INSTITUTION 4 @ \# @ \#

MASTER FILE PARAMETERS 4.001 @ @ @ @ @ @

MD5 Signature 4.005

STANDARD TERMINOLOGY VERSION F 4.009 @ @ @ @ @ @

INSTITUTION ASSOCIATION TYPES 4.05 @ @ @ @ @

FACILITY TYPE 4.1 @ \# @ @ @

AGENCY 4.11 @ y @ @ @

STATE 5 \# @ \# \# \# @

POSTAL CODE 5.12 @ @ @ @ @

COUNTY CODE 5.13 @ @ @ @ @

PROVIDER CLASS 7 \# \#

SPECIALITY 7.1 \# \#

HELP FRAME 9.2 \# \# \#

PACKAGE 9.4 \# I \# \# \# \#

BUILD 9.6 @ \# \# \# \# \#

INSTALL 9.7 @ \# @ \# @ \#

ROUTINE 9.8 \# I \# \# \# \#

RACE 10 \# d d d

MARITAL STATUS 11 \# d d d

RELIGION 13 \# d d d

TASKS 14.4 @ ^ @ @ @

VOLUME SET 14.5

UCI ASSOCIATION 14.6

TASKMAN SITE PARAMETERS 14.7

TASKMAN SNAPSHOT 14.71 @ @ @ @ @

TASKMAN SNAPSHOT 14.72 @ @ @

TASK SYNC FLAG 14.8 @ @ @ @ @ @

DUPLICATE RECORD 15

DUPLICATE RESOLUTION 15.1 @ \# @ @ \#

XDR MERGE PROCESS 15.2 @ \#

XDR REPOINTED ENTRY 15.3 @ \#

MERGE IMAGES 15.4 @ @ @ @ @ @

OPTION 19 \# \# \# \# \# \#

AUDIT LOG FOR OPTIONS 19.081 @ \# \# \# \# \#

SECURITY KEY 19.1 \# \# \# \# \# \#

OPTION SCHEDULING 19.2 @ @ @ @ @ @

MENUMAN QUICK HELP 19.8 @ @ @ @ @ @

NAME COMPONENTS 20 @ \# \# \# \#

HOLIDAY 40.5 \# \# Dd Dd Dd \#

SERVICE/SECTION 49 \# D d d d

PROTOCOL 101 @ \# \# \#

NEW PERSON 200 \# \# \# \# \#

PERSON CLASS 8932.1 @ ^ @ ^ @

PROGRAM OF STUDY 8932.2 @ ^ @ ^ @

NEW PERSON FIELD MONITOR 8933.1 @ @ @ @ @ @

KERMIT HOLDING 8980 \# \# \#

PKI Digital Signatures 8980.2

PKI CRL URLS 8980.22 \# \# \# \# \# \#

LOCAL KEYWORD 8984.1

LOCAL SHORTCUT 8984.2 @ \# @ @ @ @

LOCAL SYNONYM 8984.3 @ \# @ @ @ @

LOCAL LOOKUP 8984.4 @ \# @ @ @ @

KERNEL PARAMETERS 8989.2 @ @ @ @ @ @

KERNEL SYSTEM PARAMETERS 8989.3 @ @ @ @ @ @

XTV ROUTINE CHANGES 8991 @ @ @ @ @ @

XTV VERIFICATION PACKAGE 8991.19 @ @ @ @ @ @

XTV GLOBAL CHANGES 8991.2 @ @ @ @ @ @

XQAB ERRORS LOGGED 8991.5

XUEPCS DATA FILE 8991.6 @ @ @ @ @ @

XUEPCS PSDRPH AUDIT FILE 8991.7 @ @ @ @ @ @

DEA BUSINESS ACTIVITY CODES 8991.8

DEA NUMBERS 8991.9

ALERT 8992 @ @ @ @ @ @

ALERT TRACKING 8992.1

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/129.png) NOTE: This report was reformatted to fit the display area (smaller font).

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All sites should develop a local contingency plan to be used in the event of software/hardware problems in a production (live) environment. The contingency plan *must* identify the procedure for maintaining functionality provided by this software in the event of system outage.

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

User should refer to [<u>VHA Directive 2012-003, Person Class File Taxonomy</u>](http://www.va.gov/vdl/application.asp?pub_ID=2477), which redefines established policy for assigning Person Class codes to providers in the Veterans Health Information Systems and Technology Architecture (VistA) NEW PERSON (#200) file.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/130.png) REF: For software and documentation disclaimers, see the “[Disclaimers](#disclaimers)” section.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/131.png) REF: For the most recent, current year document revision history, see the “[Revision History](#revision_history)” section.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 30%" />
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
<td>08/06/2024</td>
<td>5.14</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated <u>Table 24</u>: Added content to the <a href="#XQALERT_DELETE_OLD_Option"><strong>XQALERT DELETE OLD</strong></a> entry.</p></li>
<li><p>Updated Section <u>15.2.1</u>: Added <u>Table 35</u>: missing kernel distributed mail groups, which includes the <strong>XQAL UNPROCESSED ALERTS</strong> mail group.</p></li>
<li><p>Based on “Plain Language” guidelines, changed all of the following throughout this document: “<strong>e.g.,</strong>” to “<strong>such as</strong>; “<strong>i.e.,</strong>” to “<strong>that is</strong>”; “<strong>via</strong>” to “<strong>through</strong>” or “<strong>by</strong>” or “<strong>using</strong>”, whichever most appropriate in context; “<strong>etc.</strong>” to “<strong>and so on</strong>”, and “<strong>vs.</strong>” to “<strong>compared with</strong>”.</p></li>
<li><p>Updated all styles and formatting to follow the latest OIT product standards and style guidelines.</p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
<tr class="even">
<td>01/24/2024</td>
<td>5.13</td>
<td><p>Updates for Kernel Patch XU*8.0*756:</p>
<ul>
<li><p><u>Table 3</u>: Added the <a href="#SIGN_ON_LOG_RETENTION_sys_parameter">SIGN-ON LOG RETENTION</a> field entry.</p></li>
<li><p><u>Table 9</u>: Updated the <a href="#XUSPURGE_Routine"><strong>XUSPURGE</strong></a> routine description.</p></li>
<li><p><u>Table 24</u>: Updated the <a href="#Purge_SignOn_log_Option">Purge Sign-On Log [XUSCZONK] option</a> entry.</p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>06/08/2023</td>
<td>5.12</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Removed all prior content updates for Kernel Patch XU*8.0*663 (03/10/2023), since that patch release was changed to “Released In Error.”</p></li>
<li><p>Patch XU*8.0*782, VistA Build Analyzer Utility:</p></li>
</ul>
<ul>
<li><p><u>Table 9</u>: Added the following new routines:</p></li>
</ul>
<ul>
<li><p><a href="#XPDANLYZ1_Routine"><strong>XPDANLYZ1</strong></a></p></li>
<li><p><a href="#XPDANLYZ2_Routine"><strong>XPDANLYZ2</strong></a></p></li>
<li><p><a href="#XPDANLYZ3_Routine"><strong>XPDANLYZ3</strong></a></p></li>
<li><p><a href="#XPDANLYZ4_Routine"><strong>XPDANLYZ4</strong></a></p></li>
<li><p><a href="#XPDANLYZ5_Routine"><strong>XPDANLYZ5</strong></a></p></li>
<li><p><a href="#XPDANLYZ6_Routine"><strong>XPDANLYZ6</strong></a></p></li>
</ul>
<ul>
<li><p><u>Table 24</u>: Added the following new options:</p></li>
</ul>
<ul>
<li><p><a href="#XPDANLYZ_MAIN_MENU_Menu">Build Analyzer Main Menu [XPDANLYZ MAIN MENU]</a> menu</p></li>
<li><p><a href="#XPDANLYZ_Option"><strong>KIDS Build Analyzer</strong> [XPDANLYZ]</a> option</p></li>
<li><p><a href="#XPDANLYZ_DEL_Option"><strong>Delete Build Analyzer Text Files</strong> [XPDANLYZ_DEL]</a> option</p></li>
<li><p><a href="#XPDANLYZ_SQA_Option"><strong>KIDS Build Analyzer - Full SQA Search</strong> [XPDANLYZ_SQA]</a> option</p></li>
</ul>
<ul>
<li><p><u>Table 24</u>: Modified the <a href="#XPD_UTILITY_Option"><strong>Utilities</strong> [XPD UTILITY]</a> menu to add the Build Analyzer Main Menu [XPDANLYZ MAIN MENU] menu.</p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
<tr class="even">
<td>05/24/2023</td>
<td>5.11</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*689: Pharmacy Operational Updates:</p>
<ul>
<li><p><u>Table 9</u>: Added the following new routines:</p></li>
</ul>
<ul>
<li><p><a href="#XU8P689_Routine"><strong>XU8P689</strong></a></p></li>
<li><p><a href="#XU8PE689_Routine"><strong>XU8PE689</strong></a></p></li>
<li><p><a href="\l"><strong>XUEPCSU1</strong></a></p></li>
<li><p><a href="#XUEPCSUT_Routine"><strong>XUEPCSUT</strong></a></p></li>
<li><p><a href="#XUEPCSVR_Routine"><strong>XUEPCSVR</strong></a></p></li>
</ul>
<ul>
<li><p><u>Table 12</u>: Added <strong>^XTV(8991.6)</strong> and <strong>^XTV(8991.7)</strong> globals.</p></li>
<li><p><u>Table 23</u>: Indicated selected DEA e-Prescribing of Controlled Substances (ePCS) Utility options that were placed out of order.</p></li>
<li><p><u>Table 24</u>: Indicated selected DEA ePCS Utility options that were placed out of order.</p></li>
<li><p>“<u>Callable Entry Points</u>“ section in <u>Table 27</u>: Updated the following new and modified APIs:</p></li>
</ul>
<ul>
<li><p><a href="#DEA_XUSER_Entry_Point">$$DEA^XUSER</a></p></li>
<li><p><a href="#DEAXDT_XUSER_Entry_Point">$$DEAXDT^XUSER</a></p></li>
<li><p><a href="#DEASCH_XUSER_Entry_Point">$$DEASCH^XUSER</a></p></li>
<li><p><a href="#DETOX_XUSER_Entry_Point">$$DETOX^XUSER</a></p></li>
<li><p><a href="#PRDEA_XUSER_Entry_Point">$$PRDEA^XUSER</a></p></li>
<li><p><a href="#PRSCH_XUSER_Entry_Point">$$PRSCH^XUSER</a></p></li>
<li><p><a href="#PRXDT_XUSER_Entry_Point">$$PRXDT^XUSER</a></p></li>
<li><p><a href="#SDEA_XUSER_Entry_Point">$$SDEA^XUSER</a></p></li>
</ul>
<ul>
<li><p><u>Table 29</u>: Added note to the <strong>XU EPCS EDIT</strong> RPC regarding RPC deprecation.</p></li>
</ul></td>
<td>Pharmacy Operational Updates</td>
</tr>
<tr class="odd">
<td>03/10/2023</td>
<td>5.8</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated organizational references (such as changed “Enterprise Program Management Office [EPMO]” to “Software Product Management (SPM)”) throughout.</p></li>
<li><p>Updated references to Kernel and Kernel Toolkit manual file names: from “Kernel 8.0 &amp; Kernel Toolkit 7.3 … ” to “Kernel 8.0 and Kernel Toolkit 7.3 … ” for all occurrences.</p></li>
</ul></td>
<td><ul>
<li><p>Master Veteran Index (MVI) Development Team</p></li>
<li><p>VASS Development Team</p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/09/2022</td>
<td>5.9</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*765: Pharmacy Operational Update:</p>
<ul>
<li><p><u>Table 9</u>: Updated <a href="#XUSER2_Routine"><strong>XUSER2</strong></a> routine.</p></li>
<li><p><u>Table 23</u>: Indicated selected DEA ePCS Utility options that were placed out of order.</p></li>
<li><p><u>Table 24</u>: Indicated selected DEA ePCS Utility options that were placed out of order.</p></li>
</ul></td>
<td>Pharmacy Operational Updates</td>
</tr>
<tr class="odd">
<td>04/06/2022</td>
<td>5.7</td>
<td><p>General Updates:</p>
<ul>
<li><p><u>Table 30</u>: Sorted entries alphabetically.</p></li>
<li><p><u>Table 30</u>: Added <strong>DILOCKTM</strong> and <strong>U</strong> variables.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
<tr class="even">
<td>04/05/2022</td>
<td>5.7</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*688: Pharmacy Operational Updates DEA Enhancements:</p>
<ul>
<li><p><u>Table 9</u>: Added <a href="#XUSER3_Routine"><strong>XUSER3</strong></a> routine.</p></li>
<li><p><u>Table 12</u>: Added <strong>^XTV(8991.8)</strong> and <strong>^XTV(8991.9)</strong> globals.</p></li>
<li><p><u>Table 15</u>: Added Files #8991.8 and #8991.9.</p></li>
</ul></td>
<td>Pharmacy Operational Updates Team</td>
</tr>
<tr class="odd">
<td>12/09/2019</td>
<td>5.6</td>
<td><p>Tech Edits for Kernel Patches XU*8.0*607 and 608: Kernel Lock Manager Utility:</p>
<ul>
<li><p><u>Table 9</u>: Added “<strong>XULM</strong>” routines.</p></li>
<li><p><u>Table 12</u>: Added “<strong>XLM</strong>” global.</p></li>
<li><p><u>Table 15</u>: Added “<strong>XULM</strong>” files.</p></li>
<li><p><u>Figure 11</u>: Updated XUSITEMGR menu diagram for the Lock Manager options.</p></li>
<li><p><u>Table 20</u>: Added “<strong>XULM</strong>” protocols.</p></li>
<li><p><u>Table 24</u>: Added “<strong>XULM</strong>” options to and updated options for <strong>Operations Management</strong> [XUSITEMGR] menu.</p></li>
<li><p><u>Table 27</u>: Added “<strong>XULM</strong>” API.</p></li>
<li><p><u>Table 29</u>: Added “<strong>XULM</strong>” RPC.</p></li>
<li><p><u>Table 37</u>: Added “<strong>XULM</strong>” security key.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VistA Infrastructure (VI)/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>07/24/2019</td>
<td>5.5</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*711:</p>
<ul>
<li><p><u>Table 9</u>: Added the <strong>XUMVIENU</strong> and <strong>XUMVINPA</strong> routine entries.</p></li>
<li><p><u>Table 29</u>: Added the <strong>XUS MVI ENRICH NEW PERSON</strong> RPC entry.</p></li>
</ul>
<p>Tech Edits for Kernel Patch XU*8.0*693:</p>
<ul>
<li><p><u>Table 36</u>: Updated the <strong>XUSERDEAC</strong> bulletin entry.</p></li>
<li><p><u>Table 36</u>: Added the <strong>XUSERDIS</strong> bulletin entry.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="odd">
<td>10/11/2018</td>
<td>5.4</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*690:</p>
<ul>
<li><p><u>Table 15</u>: Updated the “ALERT CRITICAL TEXT” file entry.</p></li>
<li><p><u>Table 24</u>: Updated the “XQAL ALERT LIST FROM DATE,” “XQAL CRITICAL ALERT COUNT,” and “XQAL USER ALERTS COUNT” option entries.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>10/09/2018</td>
<td>5.3</td>
<td><p>Tech Edits for Kernel Patch XU*8.0*672:</p>
<ul>
<li><p><u>Table 9</u>: Added the <strong>XU8P672E</strong> routine.</p></li>
<li><p><u>Table 27</u>: Updated the <strong>XPDMENU</strong> entry for Kernel Patch XU*8.0*672: Added the LOCK and RLOCK tags.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="odd">
<td>08/22/2018</td>
<td>5.2</td>
<td><p>Updates for Kernel Patch XU*8.0*679:</p>
<ul>
<li><p>Added Section <u>15.5.1</u>, “<u>Electronic Signature Restrictions</u>.”</p></li>
<li><p><a href="#XU_80_679_parameter"><u>Table 5</u></a>: Added the <strong>XU SIG BLOCK DISABLE</strong> parameter.</p></li>
<li><p><a href="#XU_80_679_routines"><u>Table 9</u></a>: Added the <strong>XUSESIG2</strong> and <strong>XUSESIG3</strong> routines.</p></li>
<li><p><a href="#XU_80_679_options"><u>Table 24</u></a>: Modified the <strong>XUSESIG BLOCK</strong> option (Type and Routine columns) and added the <strong>XUSESIG DEG</strong> option.</p></li>
<li><p><a href="#XU_80_679_key"><u>Table 37</u></a>: Added the <strong>XUSIG</strong> security key.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>08/15/2018</td>
<td>5.1</td>
<td><p>Tech Edits: Final merge of all remaining content in the K<em>ernel Toolkit Technical Manual</em> into the <em>Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual</em> (this manual):</p>
<ul>
<li><p>Added the following sections for Kernel Toolkit:</p></li>
</ul>
<ul>
<li><p>Section <u>1.1</u>, “<u>Kernel</u>.”</p></li>
<li><p>Section <u>1.2</u>, “<u>Kernel Toolkit</u>.”</p></li>
<li><p>Section <u>1.2.1</u>, “<u>Multi-Term Look-Up (MTLU)</u>.”</p></li>
<li><p>Section <u>1.2.2</u>, “<u>Duplicate Resolution Utilities</u>.”</p></li>
<li><p>Section <u>2.11</u>, “<u>Implementing Multi-Term Look-Up</u>.”</p></li>
<li><p>Section <u>2.12</u>, “<u>Implementing Duplicate Resolution Utilities</u>.”</p></li>
<li><p>Section <u>2.13</u>, “<u>Configuring VAX/Alpha Performance Monitor (VPM)</u>.”</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="odd">
<td>01/23/2018</td>
<td>5.0</td>
<td><p>Tech Edits:</p>
<ul>
<li><p><u>Table 29</u>: Changed the <strong>XUS SIGNON SETUP</strong> RPC from “RESTRICTED” to “PUBLIC,” as per developer.</p></li>
<li><p><u>Table 29</u>: Added an “ICR #” column to list any known ICRs associated with RPCs.</p></li>
<li><p><u>Table 29</u>: Updated the <strong>XUS GET VISITOR</strong> and <strong>XUS SET VISITOR</strong> RPCs.</p></li>
<li><p>Updated Section <u>4</u> and <u>Table 15</u>; and Section <u>15.7</u> and <u>Figure 21</u> for missing Toolkit files: 15.2, 15.3, and 15.4.</p></li>
<li><p>Updated many sections with content extracted from the <em>Assign Person Class to Providers Patch Supplement</em> document (such as routines, files, fields, globals, options, and so on).</p></li>
<li><p>Modified/Removed VAH and MGR references:</p></li>
</ul>
<ul>
<li><p>Retitled and updated Section <u>14.1</u> to “Globals in Production Accounts.”</p></li>
<li><p><u>Table 34</u>: Removed reference to “VAH and updated.</p></li>
<li><p><u>Table 34</u>: Merged content from previous table into.</p></li>
<li><p>Deleted Section 14.2, “Globals in MGR Account.”</p></li>
</ul>
<ul>
<li><p>Added Caution note regarding modification of Kernel routines in the <a href="#software_disclaimer">“Software Disclaimer</a>” section.</p></li>
<li><p>Added the “System Management Menus” section and sub-sections from the <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> into this document.</p></li>
<li><p>Replaced “Integration Agreement (IA)” with “Integration Control Registration (ICR)” throughout the document.</p></li>
<li><p>Added <u>Table 10</u> in Section <u>3.2</u>; added routines exported with the Broker Security Enhancement (BSE) software.</p></li>
<li><p><u>Table 29</u>: Updated the <strong>XUS SET VISITOR</strong> RPC.</p></li>
<li><p><u>Figure 11</u> and <u>Table 24</u>: Kernel Patch XU*8.0*605: Added the IPV tool options (<strong>XLFIPV*</strong>).</p></li>
<li><p><u>Table 3</u>: Added the following parameters to the KERNEL SYSTEM PARAMETERS (#8989.3) File:</p></li>
</ul>
<ul>
<li><p>ORGANIZATION (#200.2)</p></li>
<li><p>ORGANIZATION ID (#200.3)</p></li>
<li><p>SECURITY TOKEN SERVICE (#200.1)</p></li>
</ul>
<ul>
<li><p><u>Table 4</u>: Added the <strong>XUEXISTING USER</strong> parameter to the KERNEL PARAMETERS (#8989.2) File.</p></li>
<li><p><u>Table 5</u>: Added the following parameters to the PARAMETER DEFINITION (#8989.51) File:</p></li>
</ul>
<ul>
<li><p><strong>XU522</strong></p></li>
<li><p><strong>XU594</strong></p></li>
<li><p><strong>XU645</strong></p></li>
</ul>
<ul>
<li><p><u>Table 9</u>: Added the following routines:</p></li>
</ul>
<ul>
<li><p><strong>XLFSHAN</strong></p></li>
<li><p><strong>XUCERT</strong></p></li>
<li><p><strong>XUCERT1</strong></p></li>
<li><p><strong>XUESSO1</strong></p></li>
<li><p><strong>XUESSO2</strong></p></li>
<li><p><strong>XUESSO3</strong></p></li>
<li><p><strong>XUESSO4</strong></p></li>
<li><p><strong>XUSAML</strong></p></li>
</ul>
<ul>
<li><p><u>Table 15</u>: Added the REMOTE APPLICATION (#8994.5) file.</p></li>
<li><p><u>Table 24</u>: Added the <strong>RPC Broker Management Menu</strong> [XWB MENU].</p></li>
<li><p><u>Table 29</u>: Changed the XUS GET USER INFO RPC from “PUBLIC’ to “RESTRICTED.”</p></li>
<li><p>Reformatted document to follow latest documentation standards and formatting rules. Also, formatted document for online presentation compared with print presentation (that is for double-sided printing). These changes include:</p></li>
</ul>
<ul>
<li><p>Revised section page setup.</p></li>
<li><p>Removed section headers.</p></li>
<li><p>Revised document footers.</p></li>
<li><p>Removed blank pages between sections.</p></li>
<li><p>Revised all heading style formatting.</p></li>
<li><p>Updated organizational references (such as “Product Development [PD]” to “Enterprise Program Management Office [EPMO]).</p></li>
<li><p>Redacted document for the following information:</p></li>
<li><p>Names (replaced with role and initials).</p></li>
<li><p>Production IP addresses and ports.</p></li>
<li><p>VA Intranet websites.</p></li>
<li><p>Server geographic locations and node names.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>07/19/2017</td>
<td>4.2</td>
<td><p>Tech Edits Kernel Patch XU*8.0*671:</p>
<ul>
<li><p><u>Table 15</u>: Updated Person Class File #<a href="#File_8932_1">8932.1</a>. Added updated description: Per VHA Directive 2005-044, this file has been “locked down” by Data Standardization (DS). The file definition (that is data dictionary) <em>shall not</em> be modified. All additions, changes and deletions to entries in the file <em>shall</em> be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).</p></li>
<li><p>Reviewed the updated section for Section 508 compliance.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td><p>VI/VistA Kernel Development Team</p>
<p>ManTech Mission Solutions &amp; Services Group</p></td>
</tr>
<tr class="odd">
<td>05/31/2013</td>
<td>4.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Updates for Patch XU*8.0*614 based on feedback from developer:</p></li>
</ul>
<ul>
<li><p>“<u>XUMAINT</u>” section and menu tree diagram in <u>Figure 10</u> and in <u>Table 24</u>: Added the <strong>Single User Menu Tree Rebuild</strong> [XQBUILDUSER] option. It was attached to the Menu Rebuild Menu [XQBUILDMAIN] option.</p></li>
<li><p><u>Table 24</u>: Added the XQBUILDMAIN option.</p></li>
<li><p><u>Table 24</u>: Added the XQ LIST UNREFERENCED OPTIONS option.</p></li>
<li><p><u>Table 5</u>: Added the <strong>XQ MENUMANAGER PROMPT</strong> parameter.</p></li>
</ul>
<ul>
<li><p>Updated menu diagrams in Section <u>5.2.2</u> for:</p></li>
</ul>
<ul>
<li><p>XUTIO in <u>Figure 9</u>.</p></li>
<li><p>XUMAINT in <u>Figure 10</u>.</p></li>
<li><p>XUSITEMGR in <u>Figure 11</u>.</p></li>
<li><p>XUPROG in <u>Figure 12</u>.</p></li>
<li><p>XU-SPL-MGR in <u>Figure 13</u>.</p></li>
<li><p>XUSPY in <u>Figure 14</u>.</p></li>
<li><p>XUTM MGR in <u>Figure 15</u>.</p></li>
<li><p>XUSER in <u>Figure 16</u>.</p></li>
<li><p>ZTMQUEUABLE OPTIONS in <u>Figure 17</u>.</p></li>
<li><p>XUCOMMAND in <u>Figure 18</u>.</p></li>
</ul>
<ul>
<li><p><u>Table 3</u>: Added the <strong>IP SECURITY ON</strong> field parameter.</p></li>
<li><p>“<u>Callable Entry Points</u>” section: Reviewed and updated any missing APIs.</p></li>
<li><p>Added bookmarks (identifiers) to all tables for Section 508 conformance.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>04/30/2013</td>
<td>4.0</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated the following sections and tables for Kernel Patch XU*8.0*580:</p></li>
</ul>
<ul>
<li><p><u>Table 5</u>: Added the <strong>XUEPCS REPORT DEVICE</strong> parameter.</p></li>
<li><p><u>Table 9</u> in the “<u>Routines</u>” section: Added the following new <strong>ePCS</strong> routines:</p></li>
</ul>
<ul>
<li><p><strong>XUEPCSED</strong></p></li>
<li><p><strong>XUEPCSRT</strong></p></li>
</ul>
<ul>
<li><p>“<u>Files</u>“ section in <u>Table 15</u>: Added the following new ePCS files:</p></li>
</ul>
<ul>
<li><p>XUEPCS DATA (#8991.6) file</p></li>
<li><p>XUEPCS PSDRPH AUDIT (#8991.7) file</p></li>
</ul>
<ul>
<li><p>“Exported Options” section in <u>Table 24</u>: Added the new ePCS options.</p></li>
<li><p>“<u>Callable Entry Points</u>“ section in <u>Table 27</u>: Added the following new and modified ePCS APIs:</p></li>
</ul>
<ul>
<li><p><strong>$$DEA^XUSER</strong></p></li>
<li><p><strong>$$DETOX^XUSE</strong></p></li>
<li><p><strong>$$SDEA^XUSER</strong></p></li>
<li><p><strong>$$VDEA^XUSER</strong></p></li>
</ul>
<ul>
<li><p>“<u>Remote Procedure Calls (RPCs)</u>“ section in <u>Table 29</u>: Added the following new and modified RPCs:</p></li>
</ul>
<ul>
<li><p><strong>XU EPCS EDIT</strong></p></li>
<li><p><strong>XUS PKI SET UPN</strong></p></li>
<li><p><strong>XUS PKI GET UPN</strong></p></li>
<li><p><strong>XWB GET VARIABLE VALUE</strong></p></li>
</ul>
<ul>
<li><p>“<u>Bulletins</u>” section in <u>Table 36</u>: Added the <strong>XUSSPKI SAN</strong> bulletin.</p></li>
<li><p>“<u>Security Keys</u>” section in <u>Table 37</u>: Added the <strong>XUEPCSEDIT</strong> security key.</p></li>
</ul>
<ul>
<li><p>Reformatted document to follow current style guides and standards.</p></li>
<li><p>Replaced references from “<em>VA FileMan Getting Started Manual</em>” to “<em>VA FileMan User Manual</em>,” since the next VA FileMan 22.<em>n</em> software version will be creating a new “<em>VA FileMan Getting Started Manual</em>.”</p></li>
<li><p>Added the “<u>Kernel Parameter Definitions (#8989.51) File</u>” section and <u>Table 5</u>.</p></li>
<li><p>Added the “<u>Remote Procedure Calls (RPCs)</u>” section and <u>Table 29</u>.</p></li>
<li><p>Added the “<u>Bulletins</u>” section and <u>Table 36</u>.</p></li>
<li><p>Patch XU*8.0*546: Support for Device Hunt Groups was removed. This includes removal of the *HUNT GROUP (#29) and HUNT GROUP DEVICE (#30) fields in the DEVICE (#3.5) file. Sites had to remove any HUNT GROUP devices before installing this patch using VA FileMan to find any existing Hunt Groups. Chapter 18, “Hunt Groups” was deleted from this manual. Also, any references to “Hunt Groups” were removed.</p></li>
<li><p><u>Table 12</u> and <u>Table 15</u>: Patch XU*8.0*285 added the ALERT RECIPIENT TYPE (#8992.2) file.</p></li>
<li><p><u>Table 12</u> and <u>Table 15</u>: Patch XU*8.0*513 added the ALERT CRITICAL TEXT (#8992.3) file.</p></li>
<li><p>Merging <em>Toolkit Technical Manual</em> content into <em>Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual</em>. The Kernel Toolkit documentation set is being combined with the Kernel documentation set. All Kernel Toolkit content will eventually be moved to the appropriate Kernel manual, section, and chapter.<br />
<br />
In the <em>Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual</em>, all Kernel Toolkit references for routines, files, options, APIs, Direct Mode Utilities, and so on have been added to the appropriate chapter/section.</p></li>
<li><p><u>Table 24</u>: Updated option descriptions.</p></li>
<li><p>Changed Kernel document title references.</p></li>
<li><p><em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> (previously known as the <em>Kernel Programmer Manual</em>).</p></li>
<li><p><em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> (previously known as the <em>Kernel Systems Manual</em>).</p></li>
<li><p>Updates based on functionality/changes added with Kernel Patch XU*8.0*593:</p></li>
<li><p><u>Table 19</u>: Added the “XU USER START-UP” entry.</p></li>
<li><p><u>Table 24</u>: Added the “XU USER START-UP” entry.</p></li>
<li><p>Updated references to the VDL.</p></li>
<li><p>Updated all organizational references as needed (such as Enterprise Program Management Office [EPMO], removed all HSD&amp;D references)</p></li>
<li><p>Removed obsolete references to MSM, PDP, 486, VAX Alpha, and so on and changed/updated references to DSM for OpenVMS to Caché where appropriate.</p></li>
<li><p>Updated “<a href="#_Toc234301877">Orientation</a>” section.</p></li>
<li><p>Updated the overall document for current national documentation standards and style guides. For example:</p></li>
<li><p>Changed all Heading <em>n</em> styles to use Arial font.</p></li>
<li><p>Changed all Heading <em>n</em> styles to be left justified.</p></li>
<li><p>Added blue font highlighting and underline to signify internal links to figures, tables, or sections for ease of use, like what one sees to hyperlinks on a Web page.</p></li>
<li><p>Updated document for Section 508 conformance using word’s built-in Accessibility check:</p></li>
</ul>
<ul>
<li><p>Added table bookmarks.</p></li>
<li><p>Added screen tips for all URL links.</p></li>
<li><p>Changed all floating callout boxes to in-line, causing reformatting of numerous dialog screen captures.</p></li>
</ul>
<p><strong>Software Versions:</strong></p>
<ul>
<li><p><strong>Kernel 8.0</strong></p></li>
<li><p><strong>Toolkit 7.3</strong></p></li>
</ul></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="odd">
<td>01/24/2006</td>
<td>3.0</td>
<td><p>Updates:</p>
<ul>
<li><p>Reformatted document to follow the latest ISS SOP Guidelines.</p></li>
<li><p>Updated files, routines, options, APIs, security keys, and so on.</p></li>
</ul>
<p><strong>Software Version: 8.0</strong></p></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="even">
<td>02/03/2005</td>
<td>2.0</td>
<td><p>Reformatted document to follow the latest ISS styles and guidelines. No other content updates have been made regarding released patches at this time.</p>
<p>Reviewed document and edited for the “Data Scrubbing” and the “PDF 508 Compliance” projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to OIT standards and conventions as indicated below:</p>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with “<strong>000</strong>” or “<strong>666</strong>.”</p></li>
<li><p>Patient or user names are formatted as follows: KRNPATIENT,[N] or KRNUSER,[N] respectively, where the N is a number written out and incremented with each new entry (such as KRNPATIENT, ONE, KRNPATIENT, TWO, and so on).</p></li>
<li><p>Other personal demographic-related data (such as addresses, phones, IP addresses, and so on) were also changed to be generic.</p></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (that is accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p>
<p><strong>Software Version: 8.0</strong></p></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
<tr class="odd">
<td>07/--/1995</td>
<td>1.0</td>
<td><p>Initial Kernel 8.0 software and documentation release</p>
<p><strong>Software Version: 8.0</strong></p></td>
<td>VI/VistA Kernel Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc205036168" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Alpha Testing</strong></td>
<td>In VA terminology, Alpha testing is when a VistA test software application is running in a site’s account.</td>
</tr>
<tr class="even">
<td><strong>Audit Access</strong></td>
<td>A user’s authorization to mark the information stored in a computer file to be audited.</td>
</tr>
<tr class="odd">
<td><strong>Auditing</strong></td>
<td>Monitoring computer usage such as changes to the database and other user activity. Audit data can be logged in several VA FileMan and Kernel files.</td>
</tr>
<tr class="even">
<td><strong>Auto Menu</strong></td>
<td>An indication to MenuMan that the current user’s menu items should be displayed automatically. When AUTO MENU is <em>not</em> in effect, the user <em>must</em> enter a question mark at the menu’s select prompt to see the list of menu items.</td>
</tr>
<tr class="odd">
<td><strong>Beta Testing</strong></td>
<td>In VA terminology, Beta testing is when a VistA test software application is running in a Production account.</td>
</tr>
<tr class="even">
<td><strong>Capacity Management</strong></td>
<td>The process of assessing a system’s capacity and evaluating its efficiency relative to workload to optimize system performance. Kernel provides several utilities.</td>
</tr>
<tr class="odd">
<td><strong>Caret</strong></td>
<td>A symbol expressed as <strong>^</strong> (caret). In many M systems, a caret is used as an exiting tool from an option. Also, this symbol is sometimes referred to as the “up-arrow” symbol.</td>
</tr>
<tr class="even">
<td><strong>Checksum</strong></td>
<td>A <strong>NUMERIC</strong> value that is the result of a mathematical computation involving the characters of a routine or file.</td>
</tr>
<tr class="odd">
<td><strong>Cipher</strong></td>
<td>A system that arbitrarily represents each character as one or more other characters.<br />
<br />
(See also: <a href="#ENCRYPTION">ENCRYPTION</a>.)</td>
</tr>
<tr class="even">
<td><strong>CMS</strong></td>
<td>Centers for Medicare &amp; Medicaid Services (related to assigning users to Person Class).</td>
</tr>
<tr class="odd">
<td><strong>Common Menu</strong></td>
<td>Options that are available to all users. Entering <strong>two</strong> question marks (<strong>??</strong>) at the menu’s select prompt displays any SECONDARY MENU OPTIONS available to the signed-on user along with the common options available to all users.</td>
</tr>
<tr class="even">
<td><strong>Compiled Menu System (^XUTL GLOBAL)</strong></td>
<td>Job-specific information that is kept on each CPU so that it is readily available during the user’s session. It is stored in the <strong>^XUTL</strong> global, which is maintained by the menu system to hold commonly referenced information. The user’s place within the menu trees is stored, for example, to enable navigation using menu jumping.</td>
</tr>
<tr class="odd">
<td><strong>Computed Field</strong></td>
<td>This field takes data from other fields and performs a predetermined mathematical function (such as adding two columns together). You do <em>not</em>, however, see the results of the mathematical function on the screen. Only when you are printing or displaying information on the screen do you see the results for this type of field.</td>
</tr>
<tr class="even">
<td><strong>Device Handler</strong></td>
<td>The Kernel module that provides a mechanism for accessing peripherals and using them in controlled ways (such as user access to printers or other output devices).</td>
</tr>
<tr class="odd">
<td><strong>DIFROM</strong></td>
<td>VA FileMan utility that gathers all software components and changes them into routines (<strong>namespaceI*</strong> routines) so that they can be exported and installed in another VA FileMan environment.</td>
</tr>
<tr class="even">
<td><strong>Double Quote (“)</strong></td>
<td>A symbol used in front of a Common option’s menu text or synonym to select it from the Common menu. For example, the five-character string <strong>“TBOX</strong> selects the User’s Toolbox Common option.</td>
</tr>
<tr class="odd">
<td><strong>DR String</strong></td>
<td>The set of characters used to define the <strong>DR</strong> variable when calling VA FileMan. Since a series of parameters may be included within quotes as a literal string, the variable’s definition is often called the <strong>DR</strong> string. To define the fields within an edit sequence, for example, the developer may specify the fields using a <strong>DR</strong> string rather than an INPUT template.</td>
</tr>
<tr class="even">
<td><strong>DUZ(0)</strong></td>
<td>A local variable that holds the FILE MANAGER ACCESS CODE of the signed-on user.</td>
</tr>
<tr class="odd">
<td><span id="ENCRYPTION" class="anchor"></span><strong>Encryption</strong></td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases, encryption algorithms are one directional; that is, they only encode, and the resulting data cannot be unscrambled (such as Access and Verify Codes).</td>
</tr>
<tr class="even">
<td><strong><br />
</strong><span id="FILE_ACCESS_SECURITY_SYSTEM" class="anchor"></span><strong>File Access Security System</strong></td>
<td>Formerly known as <strong>Part 3</strong> of the Kernel <strong>Inits</strong>. If the File Access Security conversion has been run, file-level security for VA FileMan files is controlled by Kernel’s File Access Security system, <em>not</em> by File Manager Access Codes (that is FILE MANAGER ACCESS CODE field).</td>
</tr>
<tr class="odd">
<td><strong>Forced Queuing</strong></td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device will reject it and prompt the user to queue the task instead.</td>
</tr>
<tr class="even">
<td><span id="GO_HOME_JUMP" class="anchor"></span><strong>Go-Home Jump</strong></td>
<td>A menu jump that returns the user to the Primary menu presented at signon. It is specified by entering two carets (<strong>^^</strong>) at the menu’s select prompt. It resembles the Rubber-band Jump but without an option specification after the carets.</td>
</tr>
<tr class="odd">
<td><strong>HCFA</strong></td>
<td>Health Care Financing Administration (related to assigning users to Person Class).</td>
</tr>
<tr class="even">
<td><strong>Help Processor</strong></td>
<td>The <strong>Help Processor</strong> [XQHELP-MENU] menu is a Kernel module that provides a system for creating and displaying online documentation. It is integrated within the menu system so that help frames associated with options can be displayed with a standard query at the menu’s select prompt.</td>
</tr>
<tr class="odd">
<td><strong>Host File Server (HFS)</strong></td>
<td>A procedure available on layered systems whereby a file on the host system can be identified to receive output. It is implemented by the Device Handler’s <strong>HFS</strong> device type.</td>
</tr>
<tr class="even">
<td><strong>Index (%INDEX)</strong></td>
<td>A Kernel utility used to verify routines and other M code associated with a software application. Checking is done according to current ANSI MUMPS standards and VistA programming standards. This tool can be invoked through an option or from direct mode<br />
(&gt;<strong>D ^%INDEX</strong>).</td>
</tr>
<tr class="odd">
<td><strong>Init</strong></td>
<td>Initialization of a software application. <strong>INIT*</strong> routines are built by VA FileMan’s <strong>DIFROM</strong> and, when run, recreate a set of files and other software components.</td>
</tr>
<tr class="even">
<td><strong>Jump</strong></td>
<td><p>In VistA applications, the <strong>Jump</strong> command allows you to go from a particular field within an option to another field within that same option. You can also Jump from one menu option to another menu option without having to respond to all the prompts in between. To jump, type a caret (<strong>^</strong>) and then type the name of the field or option you wish to jump to.</p>
<p>(See also <a href="#GO_HOME_JUMP">GO-HOME JUMP</a>, <a href="#PHANTOM_JUMP">PHANTOM JUMP</a>, <a href="#RUBBER_BAND_JUMP">RUBBER-BAND JUMP</a>, or <a href="#UP_ARROW_JUMP">UP-ARROW JUMP</a>.)</p></td>
</tr>
<tr class="odd">
<td><strong>Jump Start</strong></td>
<td>A logon procedure whereby the user enters the<br />
“<strong>Access Code;Verify Code;option</strong>” to go immediately to the target option, indicated by its menu text or synonym. The jump syntax can be used to reach an option within the menu trees by entering “<strong>Access;Verify;^option</strong>”.</td>
</tr>
<tr class="even">
<td><strong>Kermit</strong></td>
<td>A standard file transfer protocol. It is supported by Kernel and can be set up as an alternate editor.</td>
</tr>
<tr class="odd">
<td><strong>Manager Account</strong></td>
<td>A UCI that can be referenced by non-manager accounts (such as Production accounts). Like a library, the <strong>MGR</strong> UCI holds percent routines and globals (such as <strong>^%ZOSF</strong>) for shared use by other UCIs.</td>
</tr>
<tr class="even">
<td><strong>Menu Cycle</strong></td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. MenuMan keeps track of information (such as the user’s place in the menu trees) according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="odd">
<td><strong>Menu Manager</strong></td>
<td>The Kernel module that controls the presentation of user activities (such as menu choices or options). Information about each user’s menu choices is stored in the Compiled Menu System, the <strong>^XUTL</strong> global, for easy and efficient access.</td>
</tr>
<tr class="even">
<td><strong>Menu System</strong></td>
<td>The overall MenuMan logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td><strong>Menu Template</strong></td>
<td>An association of options as pathway specifications to reach one or more final destination options. The final options <em>must</em> be executable activities and <em>not</em> merely menus for the template to function. Any user can define user-specific MENU templates using the corresponding Common option.</td>
</tr>
<tr class="even">
<td><strong>Menu Trees</strong></td>
<td>The menu system’s hierarchical tree-like structures that can be traversed or navigated, like pathways, to give users easy access to various options.</td>
</tr>
<tr class="odd">
<td><strong>PAC</strong></td>
<td><strong>P</strong>rogrammer <strong>A</strong>ccess <strong>C</strong>ode. An optional user attribute that can function as a second level password into <strong>Programmer</strong> mode.</td>
</tr>
<tr class="even">
<td><strong>Part 3 of the Kernel Init</strong></td>
<td>See <a href="#FILE_ACCESS_SECURITY_SYSTEM">FILE ACCESS SECURITY SYSTEM</a>.</td>
</tr>
<tr class="odd">
<td><strong>Pattern Match</strong></td>
<td>A preset formula used to test strings of data. Refer to your system’s M Language Manuals for information on Pattern Match operations.</td>
</tr>
<tr class="even">
<td><span id="PHANTOM_JUMP" class="anchor"></span><strong>Phantom Jump</strong></td>
<td>Menu jumping in the background. Used by the menu system to check menu pathway restrictions.</td>
</tr>
<tr class="odd">
<td><strong>Primary Menus</strong></td>
<td>The list of options presented at signon. Each user <em>must</em> have a PRIMARY MENU OPTION to sign on and reach MenuMan. Users are given primary menus by system administrators. This menu should include most of the computing activities the user will need.</td>
</tr>
<tr class="even">
<td><strong>Programmer Access</strong></td>
<td>Privilege to become a programmer on the system and work outside many of the security controls of Kernel. Accessing <strong>Programmer</strong> mode from Kernel’s menus requires having the programmer’s at-sign security code, which sets the variable <strong>DUZ(0)=@</strong>.</td>
</tr>
<tr class="odd">
<td><strong>Protocol</strong></td>
<td>An entry in the PROTOCOL (#101) file. Used by the Order Entry/Results Reporting (OE/RR) software to support the ordering of medical tests and other activities. Kernel includes several protocol-type options for enhanced menu displays within the OE/RR software.</td>
</tr>
<tr class="even">
<td><strong>Queuing</strong></td>
<td>Requesting that a job be processed in the background rather than in the foreground within the current session. Kernel’s TaskMan module handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td><strong>Queuing Required</strong></td>
<td>An option attribute that specifies that the option <em>must</em> be processed by TaskMan (the option can only be queued). The option can be invoked, and the job prepared for processing, but the output can only be generated during the specified time periods.</td>
</tr>
<tr class="even">
<td><strong>Resource</strong></td>
<td>A method that enables sequential processing of tasks. The processing is accomplished with a <strong>RES</strong> device type designed by the application programmer and implemented by system administrators. The process is controlled through the RESOURCE (#3.54) file.</td>
</tr>
<tr class="odd">
<td><span id="RUBBER_BAND_JUMP" class="anchor"></span><strong>Rubber-Band Jump</strong></td>
<td>A menu jump used to go out to an option and then return, in a bouncing motion. The syntax of the jump is two carets (<strong>^^</strong>) followed by an option’s menu text or synonym (such as <strong>^^Print Option File</strong>). If the two carets are <em>not</em> followed by an option specification, the user is returned to the primary menu.<br />
<br />
(See also: <a href="#GO_HOME_JUMP">GO-HOME JUMP</a>.)</td>
</tr>
<tr class="even">
<td><strong>Scheduling Options</strong></td>
<td>A way of ordering TaskMan to run an option at a designated time with a specified rescheduling frequency (such as once per week).</td>
</tr>
<tr class="odd">
<td><strong>Scroll/No Scroll</strong></td>
<td>The <strong>Scroll/No Scroll</strong> button (also called <strong>Hold Screen</strong>) allows the user to “<strong>stop</strong>” (No Scroll) the terminal screen when large amounts of data are displayed too fast to read and “<strong>restart</strong>” (Scroll) when the user wishes to continue.</td>
</tr>
<tr class="even">
<td><strong>Secondary Menu Options</strong></td>
<td>Options assigned to individual users to tailor their menu choices. If a user needs a few options in addition to those available on the primary menu, the options can be assigned as secondary options. To facilitate menu jumping, secondary menus should be specific activities, <em>not</em> elaborate and deep menu trees.</td>
</tr>
<tr class="odd">
<td><strong>Secure Menu Delegation (SMD)</strong></td>
<td>A controlled system whereby menus and keys can be allocated by people other than system administrators (such as application coordinators) who have been so authorized. SMD is a part of MenuMan.</td>
</tr>
<tr class="even">
<td><strong>Server Option</strong></td>
<td>In VistA, an entry in the OPTION (#19) file. An automated mail protocol that is activated by sending a message to the server with the “<strong>S.server</strong>” syntax. A server option’s activity is specified in the OPTION (#19) file and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td><strong>Signon/Security</strong></td>
<td>The Kernel module that regulates access to the menu system. It performs several checks to determine whether access can be permitted at a particular time. A log of signons is maintained.</td>
</tr>
<tr class="even">
<td><strong>Special Queueing</strong></td>
<td>An option attribute indicating that TaskMan should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td><strong>Spooler</strong></td>
<td>An entry in the DEVICE (#3.5) file. It uses the associated operating system’s spool facility, whether it’s a global, device, or host file. Kernel manages spooling so that the underlying OS mechanism is transparent. In any environment, the same method can be used to send output to the spooler. Kernel will subsequently transfer the text to a global for subsequent despooling (printing).</td>
</tr>
<tr class="even">
<td><strong>Synonym</strong></td>
<td>In VistA, a field in the OPTION (#19) file. Options can be selected by their menu text or synonym.</td>
</tr>
<tr class="odd">
<td><strong>TaskMan</strong></td>
<td>The Kernel module that schedules and processes background tasks (aka Task Manager).</td>
</tr>
<tr class="even">
<td><strong>Timed Read</strong></td>
<td>The amount of time Kernel will wait for a user response to an interactive <strong>READ</strong> command before starting to halt the process.</td>
</tr>
<tr class="odd">
<td><span id="UP_ARROW_JUMP" class="anchor"></span><strong>Up-Arrow Jump</strong></td>
<td>In the menu system, entering a caret (<strong>^</strong>) followed by an option name accomplishes a jump to the target option without needing to take the usual steps through the menu pathway.</td>
</tr>
<tr class="even">
<td><strong>Z Editor (^%Z)</strong></td>
<td>A Kernel tool used to edit routines or globals. It can be invoked with an option, or from direct mode after loading a routine with <strong>&gt;X ^%Z</strong>.</td>
</tr>
<tr class="odd">
<td><strong>ZOSF Global (^%ZOSF)</strong></td>
<td>The Operating System File—a manager account global distributed with Kernel to provide an interface between VistA software and the underlying operating system. This global is built during Kernel installation when running the manager setup routine (<strong>ZTMGRSET</strong>). The nodes of the global are filled-in with operating system-specific code to enable interaction with the operating system. Nodes in the <strong>^%ZOSF</strong> global can be referenced by application developers so that separate versions of the software need <em>not</em> be written for each operating system.</td>
</tr>
</tbody>
</table>

![](kernel-8-0-and-kernel-toolkit-7-3-technical-manual/132.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.