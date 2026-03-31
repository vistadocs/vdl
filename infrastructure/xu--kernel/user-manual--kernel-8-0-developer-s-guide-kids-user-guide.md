---
title: "Kernel 8.0 Developerâ€™s Guide: KIDS User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: KIDS"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - span
  - kids
  - install
  - build
  - class
  - strong
  - table
  - software
  - site
  - routine
page_count: 0
word_count: 21034
section_count: 25
table_count: 10
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259379" class="anchor"></span>Kernel Installation and Distribution System (KIDS) Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-kids-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-kids-user-guide/002.png) REF: For the archived document revision history, see “[Appendix A—Revision History Archive](#appendix-arevision-history-archive).”

<table>
<caption><p><span id="_Ref499704200" class="anchor"></span>Table 1: KIDS—Options Supporting Software Application Builds and Exports</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
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
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide:</em> K<em>ernel Installation and Distribution System (KIDS) Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref499704200" class="anchor"></span>Table 1: KIDS—Options Supporting Software Application Builds and Exports

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc206956180" class="anchor"></span>List of Figures

<span id="_Toc206956181" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-kids-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Developers Tools](#developers-tools)
  - [KIDS Build-related Options](#kids-build-related-options)
  - [Creating Builds](#creating-builds)
    - [Build Entries](#build-entries)
    - [Create a Build Using Namespace](#create-a-build-using-namespace)
    - [Copy Build to Build](#copy-build-to-build)
    - [Edit a Build](#edit-a-build)
    - [Transporting a Distribution](#transporting-a-distribution)
    - [Creating Transport Globals that Install Efficiently](#creating-transport-globals-that-install-efficiently)
  - [Advanced Build Techniques](#advanced-build-techniques)
    - [Environment Check Routine](#environment-check-routine)
    - [PRE-TRANSPORTATION ROUTINE (#900) Field](#pre-transportation-routine-900-field)
    - [Pre- and Post-Install Routines: Special Features](#pre-and-post-install-routines-special-features)
    - [Edit a Build—Screen 4](#edit-a-buildscreen-4)
    - [How to Ask Installation Questions](#how-to-ask-installation-questions)
    - [Using Checkpoints (Pre- and Post-Install Routines)](#using-checkpoints-pre-and-post-install-routines)
    - [Required Builds](#required-builds)
    - [Package File Link](#package-file-link)
    - [Track Package Nationally](#track-package-nationally)
    - [Alpha/Beta Tracking](#alphabeta-tracking)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [UPDATE^XPDID(): Update Install Progress Bar](#updatexpdid-update-install-progress-bar)
    - [Example](#example)
  - [EN^XPDIJ(): Task Off KIDS Install](#enxpdij-task-off-kids-install)
  - [\$\$PKGPAT^XPDIP(): Update Patch History](#pkgpatxpdip-update-patch-history)
  - [\$\$PKGVER^XPDIP(): Update Patch Version](#pkgverxpdip-update-patch-version)
  - [BMES^XPDUTL(): Output a Message with Blank Line](#bmesxpdutl-output-a-message-with-blank-line)
  - [\$\$COMCP^XPDUTL(): Complete Checkpoint](#comcpxpdutl-complete-checkpoint)
  - [\$\$CURCP^XPDUTL(): Get Current Checkpoint Name/IEN](#curcpxpdutl-get-current-checkpoint-nameien)
  - [\$\$INSTALDT^XPDUTL(): Return All Install Dates/Times](#instaldtxpdutl-return-all-install-datestimes)
    - [Example](#example-1)
  - [\$\$LAST^XPDUTL(): Last Software Patch](#lastxpdutl-last-software-patch)
    - [Examples](#examples)
  - [MES^XPDUTL(): Output a Message](#mesxpdutl-output-a-message)
  - [\$\$NEWCP^XPDUTL(): Create Checkpoint](#newcpxpdutl-create-checkpoint)
  - [\$\$OPTDE^XPDUTL(): Disable/Enable an Option](#optdexpdutl-disableenable-an-option)
    - [Example](#example-2)
  - [\$\$PARCP^XPDUTL(): Get Checkpoint Parameter](#parcpxpdutl-get-checkpoint-parameter)
  - [\$\$PATCH^XPDUTL(): Verify Patch Installation](#patchxpdutl-verify-patch-installation)
    - [Example](#example-3)
  - [\$\$PKG^XPDUTL(): Parse Software Name from Build Name](#pkgxpdutl-parse-software-name-from-build-name)
  - [\$\$PRODE^XPDUTL(): Disable/Enable a Protocol](#prodexpdutl-disableenable-a-protocol)
  - [\$\$RTNUP^XPDUTL(): Update Routine Action](#rtnupxpdutl-update-routine-action)
  - [\$\$UPCP^XPDUTL(): Update Checkpoint](#upcpxpdutl-update-checkpoint)
  - [\$\$VER^XPDUTL(): Parse Version from Build Name](#verxpdutl-parse-version-from-build-name)
  - [\$\$VERCP^XPDUTL(): Verify Checkpoint](#vercpxpdutl-verify-checkpoint)
  - [\$\$VERSION^XPDUTL(): Package File Current Version](#versionxpdutl-package-file-current-version)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Kernel Installation and Distribution System (KIDS) Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Developers Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## KIDS Build-related Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get to the KIDS: Kernel Installation & Distribution System \[XPD MAIN\] menu (locked with the XUPROG security key) choose the Programmer Options \[XUPROG\] menu option on the Kernel Systems Manager Menu \[EVE\], as shown in [Figure 1](#_Ref499704125):

<span id="_Ref499704125" class="anchor"></span>Figure 1: KIDS—Edits and Distribution Menu Options

Select Systems Manager Menu Option: <span class="mark">PROGRAMMER OPTIONS \<Enter\></span>

<span class="mark">KIDS Kernel Installation & Distribution System ... \[XPD MAIN\]</span>

\*\*\> Locked with XUPROG

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

ALS MENU TEXT SAMPLE ...

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

M Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options Option: <span class="mark">KIDS \<Enter\></span> Kernel Installation & Distribution

System

<span class="mark">Edits and Distribution ... \[XPD DISTRIBUTION MENU\]</span>

Utilities ... \[XPD UTILITY\]

Installation ... \[XPD INSTALLATION MENU\]

\*\*\> Locked with XUPROGMODE

Select Kernel Installation & Distribution System Option: <span class="mark">EDITS AND DISTRIBUTION \<Enter\></span>

Create a Build Using Namespace

Copy Build to Build

Edit a Build

Transport a Distribution

Old Checksum Update from Build

Old Checksum Edit

Routine Summary List

Version Number Update

Select Edits and Distribution Option:

## Creating Builds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS introduces significant revisions to the process of exporting software applications over the previous export mechanism, DIFROM.

![](kernel-8-0-developer-s-guide-kids-user-guide/004.png) REF: For an introduction to KIDS and a description of the KIDS installation and utility options, see the “KIDS: System Management—Installations” and “KIDS: System Management—Utilities” sections in the [*Kernel Installation and Distribution System (KIDS) User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf).

[Table 1](#_Ref499704200) provides a functional listing of the KIDS options supporting software application (package) export:

| Task Category         | Option Name           | Option Text                    |
|-----------------------|-----------------------|--------------------------------|
| Create Build Entry    | XPD BUILD NAMESPACE   | Create a Build using Namespace |
|                       | XPD COPY BUILD        | Copy Build to Build            |
|                       | XPD EDIT BUILD        | Edit a Build                   |
| Create a Distribution | XPD TRANSPORT PACKAGE | Transport a Distribution       |

<span id="_Toc200269985" class="anchor"></span>Table 2: KIDS—Functional Layout, Edit a Build

This section covers each of these tasks, describing how to accomplish the tasks using KIDS options.

### Build Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS stores the definition of a software application in the BUILD (#9.6) file. Individual entries in the BUILD (#9.6) file are called build entries or builds for short. To export a software application, you *must* first define a build entry for it in the BUILD (#9.6) file.

Unlike DIFROM, where you re-used the same PACKAGE (#9.4) file entry each time you exported a new version of a software application, with KIDS you create a new BUILD (#9.6) file entry each time you export a software application version. One advantage of having one BUILD entry per software application version is that you have a complete history of each version of your software application, which makes it easier to compare previous versions of a software application with the current version.

After you create the build name, KIDS give you the option to choose the type of build you are creating. There are three types from which to choose:

- Single
- Multi-Package
- Global

<span id="_Toc200269981" class="anchor"></span>Figure 2: KIDS—Choosing a Build Type Sample

Select Edits and Distribution Option: <span class="mark">EDIT A BUILD \<Enter\></span>

Select BUILD NAME: <span class="mark">TEST 5.0 \<Enter\></span>

Are you adding 'TEST 5.0' as a new BUILD (the 104TH)? <span class="mark">Y \<Enter\></span> (Yes)

BUILD PACKAGE FILE LINK: <span class="mark">RET \<Enter\></span>

BUILD TYPE: SINGLE PACKAGE// <span class="mark">? \<Enter\></span>

Choose from:

0 SINGLE PACKAGE

1 MULTI-PACKAGE

2 GLOBAL PACKAGE

BUILD TYPE: SINGLE PACKAGE// <span class="mark">GLOBAL \<Enter\></span> GLOBAL PACKAGE

The following KIDS options, described below, support creating and maintaining build entries:

- [Create a Build Using Namespace](#create-a-build-using-namespace)
- [Copy Build to Build](#copy-build-to-build)
- [Edit a Build](#edit-a-build)

### Create a Build Using Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can quickly create a build entry and populate its components by namespace. The Create a Build Using Namespace \[XPD BUILD NAMESPACE\] option searches for all components in the current database matching a given list of namespaces (you can exclude by namespace also). The option searches for components of every type that match the namespaces and populates the build entry with all matches it finds on the system. You can then use the Edit a Build \[XPD EDIT BUILD\] option to fine-tune the build entry.

As well as creating a new build entry, you can use this option to populate an existing build entry by namespace. In this case, you are asked if you want to purge the existing data. If you answer YES, the option purges the build components in the entry and then populates the build components by namespace. If you answer NO, the option merges all components matching the selected namespaces into the existing build entry; it removes nothing already in the current build entry.

The following are Kernel 8.0 component types (listed alphabetically):

- Bulletin
- Dialog
- Form
- Function
- Help Frame
- HL7 Application Parameter
- HL Logical Link
- HL Lower Level Protocol
- Input Template
- List Template
- Mail Group
- Option
- Print Template
- Protocol
- Remote Procedure
- Routine
- Security Key
- Sort Template

<span id="_Toc200269983" class="anchor"></span>Figure 3: KIDS—Populating a Build Entry by Namespace

Select Edits and Distribution Option: <span class="mark">CREATE A BUILD USING NAMESPACE \<Enter\></span>

Select BUILD NAME: <span class="mark">ZXGY 1.0 \<Enter\></span>

Are you adding 'ZXGY 1.0' as a new BUILD (the 14th)? <span class="mark">YES \<Enter\></span>

BUILD PACKAGE FILE LINK: <span class="mark">\<Enter\></span>

Namespace: <span class="mark">ZXG \<Enter\></span>

Namespace: <span class="mark">-ZXGI \<Enter\></span>

Namespace: <span class="mark">\<Enter\></span>

NAMESPACE INCLUDE EXCLUDE

------- -------

ZXG ZXGI

OK to continue? YES// <span class="mark">\<Enter\></span>

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

...Done.

### Copy Build to Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create a new build entry based on a previous entry using the Copy Build to Build \[XPD COPY BUILD\] option. With KIDS, you *must* create a new build entry for each new version of a software application. This option gives you a way to quickly copy a previous build entry to a new entry. You can then use the Edit a Build to fine-tune the copied build entry.

If you choose an existing entry to copy into, the option purges the existing entry first before copying into it.

<span id="_Toc200269984" class="anchor"></span>Figure 4: KIDS—Copying a Build Entry

Select Edits and Distribution Option: <span class="mark">COPY BUILD TO BUILD \<Enter\></span>

Copy FROM what Package: <span class="mark">ZXG TEST 1.0 \<Enter\></span>

Copy TO what Package: <span class="mark">ZXG TEST 1.1 \<Enter\></span>

ARE YOU ADDING 'ZXG TEST 1.1' AS A NEW BUILD (THE 5TH)? <span class="mark">Y \<Enter\></span> (YES)

BUILD PACKAGE FILE LINK: <span class="mark">\<Enter\></span>

OK to continue? YES// <span class="mark">\<Enter\></span>

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND... ...Done.

### Edit a Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Edit a Build option \[XPD EDIT BUILD\], you can create new build entries and edit all parts of existing build entries. Edit a Build is a VA FileMan ScreenMan-driven option. There are four main screens in the Edit a Build option \[XPD EDIT BUILD\]. The following sections describe in detail each part of a build entry and how you can edit each part.

#### KIDS Build Screens

KIDS Build Screens are designed in conjunction with the Edit a Build option to help you plan your build entries.

| Screen   | Build Section             | Build Sub-Section         |
|----------|---------------------------|---------------------------|
| Screen 1 | Build Name                |                           |
|          | Date Distributed          |                           |
|          | Description               |                           |
|          | Environment Check Routine |                           |
|          | Pre-Install Routine       |                           |
|          | Post-Install Routine      |                           |
|          | Pre-Transport Routine     |                           |
|          | Restore Routine           |                           |
| Screen 2 | Files and Data            | Partial DD Definition     |
|          |                           | Send Data Definition      |
| Screen 3 | Build Components          | Print Template            |
|          |                           | Sort Template             |
|          |                           | Input Template            |
|          |                           | Form                      |
|          |                           | Function                  |
|          |                           | Dialog                    |
|          |                           | Bulletin                  |
|          |                           | Mail Group                |
|          |                           | Help Frame                |
|          |                           | Routine                   |
|          |                           | Option                    |
|          |                           | Security Key              |
|          |                           | Protocol                  |
|          |                           | List Template             |
|          |                           | HL7 Application Parameter |
|          |                           | HL Lower Level Protocol   |
|          |                           | HL Logical Link           |
|          |                           | Remote Procedure          |
| Screen 4 | Install Questions         |                           |
|          | Required Builds           |                           |
|          | Package File Link         |                           |
|          | Package Tracking          |                           |

<span id="_Ref503165923" class="anchor"></span>Table 3: KIDS—Data Installation Actions

#### Edit a Build: Name and Version, Build Information

When you invoke the Edit a Build \[XPD EDIT BUILD\] option, KIDS loads a four-page ScreenMan form. The first screen of the form lets you edit the following software application settings:

- Name
- Date Distributed
- Description
- Environment Check Routine
- Pre-Install Routine
- Post-Install Routine
- Pre-Transport Routine
- Restore Routine

#### Build Name

The name of a build entry is where KIDS stores both the software application’s name and version number. The build name *must* be a software application name, followed by a space and then followed by a version number. This means that every version of a software application requires a separate entry in the BUILD (#9.6) file. One way that this is an advantage is that you have a record of the contents of every version of a software application that you export.

<span id="_Toc200269986" class="anchor"></span>Figure 5: KIDS—Screen 1 of Edit a Build Sample

Edit a Build <span class="mark">PAGE 1</span> OF 5

Name: ZXG Test 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

Name: ZXG DEMO 1.0

Date Distributed: AUG 29,2004

Description: Delete Routine

after install

Environment Check Routine: Y/N:

Pre-Install Routine: ZXGPRE Y/N: N

Post-Install Routine: ZXGPOS Y/N: N

Pre-Transportation Routine:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

#### Edit a Build: Files

The second screen of the Edit a Build option is where you enter all the files to export with your software application. For each file, you can choose whether to send data with the file definition.

#### Data Dictionary Update

The installing site is *not* asked whether they want to override data dictionary updates; data dictionary updates are determined entirely by how the developer exports the file. There are two settings in KIDS you can use to determine whether KIDS should update a file’s data dictionary at the installing site:

- YES—If you answer YES to Update the Data Dictionary, the data dictionary is updated at the installing site.
- NO—If you answer NO to Update the Data Dictionary, the only time the data dictionary is updated is if the file does *not* exist on the installing system.

You can enter M code in the Screen to Determine DD Update field. The code should set the value of \$T:

- If \$T is true, KIDS installs the data dictionary.
- If \$T=0, KIDS does *not*.

The screen is only executed if the data dictionary already exists on the installing system, however; if the data dictionary does *not* already exist, the file is installed unconditionally (the screen is *not* executed). You can use the code in this field, for example, to examine the target environment to determine whether to update a data dictionary (providing the data dictionary already exists).

#### Sending Security Codes

With KIDS, you can specify on a file-by-file basis whether to send security codes. For each file, you can set SEND SECURITY CODE to either YES or NO.

If you answer YES to send security codes, KIDS sends the security codes of the files on the development system. KIDS only updates security codes at the installing site on new files (that is files that do *not* already exist), however. Security codes for a file are *not* updated at the installing site if the file already exists.

![](kernel-8-0-developer-s-guide-kids-user-guide/005.png) NOTE: Use VA FileMan’s FILESEC^DDMOD API to set the security access codes for an existing file.  
  
REF: For more information on the FILESEC^DDMOD API, see the “Database Server (DBS) API” section in the *VA FileMan Developer’s Guide* located on the [VA FileMan application on the VDL](https://www.va.gov/vdl/application.asp?appid=5).

<span id="_Toc200269987" class="anchor"></span>Figure 6: KIDS—Screen 2 of Edit a Build: Selecting Files

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG Test 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number

NEW PERSON

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Toc200269988" class="anchor"></span>Figure 7: KIDS—Data Dictionary and Data Settings

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number)

┌───────────────────────── <span class="mark">DD Export Options</span> ────────────────────────────┐

│ │

│ File: NEW PERSON │

│ │

│ Send Full or Partial DD...: PARTIAL │

│ │

│Update the Data Dictionary: YES Send Security Code: NO │

│ │

│Screen to Determine DD Update │

│ │

│ │

│ Data Comes With File...: YES │

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

#### Sending Full or Partial Data Dictionaries

KIDS supports sending out either of the following:

- Full Data Dictionaries (DD)—Entire file definition.
- Partial Data Dictionaries (DD)—Specified fields in a file.

#### Full DD—All Fields

To send the entire data dictionary, answer FULL at the “Send Full or Partial DD” prompt. In this case, *all* field definitions are exported. If you are sending data, you *must* export the FULL data dictionary.

#### Partial DD—Some Fields

You can only send a partial DD if the file already exists at the site. If you answer PARTIAL at the “Send Full or Partial DD” prompt, KIDS lets you choose what data dictionary levels to export.

In the Data Dictionary Number popup window (<u>Figure 9</u>), you can select either one of the following types:

- File Number—Top level of the file.
- Multiple—Sub-data dictionary number (also known as a subfile). You can export any Multiple, no matter how deep (every Multiple’s data dictionary number is selectable).

#### File Number Level

In the Field Number popup window (<u>Figure 10</u>), if you selected the file number type, you could select which fields to export at that data dictionary level:

- If you do *not* specify *any* fields, *no* fields are sent.
- If you do specify fields, only the specified fields are sent. You *cannot* choose any Multiples at this data dictionary level.

#### Multiple Level

In the Field Number popup window (<u>Figure 10</u>), if you selected the Multiple (sub-data dictionary number) type, you could select which fields to export at that sub-data dictionary level:

- If you do *not* specify *any* fields, *all* fields are sent. All fields at this level and their descendants are exported. You *must* do this if the Multiple is *new* at the site.
- If you do specify fields, only the specified fields are sent.

Unlike DIFROM, KIDS does *not* require sending the .01 field of the file if you send a partial data dictionary.

Whenever you export a Multiple, all “parents” of the Multiple all the way up to the .01 field of the file *must* exist at the installing site, or else you *must* export all “parents” (higher data dictionary levels) yourself. Otherwise, the Multiple is *not* installed.

![](kernel-8-0-developer-s-guide-kids-user-guide/006.png) NOTE: Certain attributes (Identifiers, “ID” nodes, and so on) are considered file attributes (as opposed to field attributes), and so are sent only when you send a full DD. They are *not* sent with a partial DD.

<span id="_Toc200269989" class="anchor"></span>Figure 8: KIDS—Data Dictionary Settings Screen—DD Export Options

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number)

┌───────────────────────── <span class="mark">DD Export Options</span> ────────────────────────────┐

│ │

│ File: NEW PERSON │

│ │

│ Send Full or Partial DD...: PARTIAL │

│ │

│Update the Data Dictionary: YES Send Security Code: NO │

│ │

│Screen to Determine DD Update │

│ │

│ │

│ Data Comes With File...: YES │

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref280187172" class="anchor"></span>Figure 9: KIDS—Partial DD: Choosing DD Levels (Top Level and Multiple) to Send; Data Dictionary Number Level

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number)

┌───────────────────────── DD Export Options ────────────────────────────┐

│┌──────────────────────── <span class="mark">Data Dictionary Number</span> ──────────────────────┐│

││ NEW PERSON (File-top level) ││

││ DMMS UNITS (sub-file) ││

││ ALIAS (sub-file) ││

││ DEFINED FORMATS FOR LM (sub-file) ││

││ ││

││ ││

││ ││

││ ││

││ ││

│└──────────────────────────────────────────────────────────────────────┘│

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref280187178" class="anchor"></span>Figure 10: KIDS—Partial DD: Choosing DD Levels (Top Level and Multiple) to Send; Field Number Level

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number)

┌───────────────────────── DD Export Options ────────────────────────────┐

│┌──────────────────────── Data Dictionary Number ──────────────────────┐│

││┌─────────────────────── <span class="mark">Field Number</span> ───────────────────────────────┐││

│││ TEST │││

│││ │││

│││ │││

│││ │││

│││ │││

│││ │││

│││ │││

││└────────────────────────────────────────────────────────────────────┘││

│└──────────────────────────────────────────────────────────────────────┘│

└────────────────────────────────────────────────────────────────────────┘

COMMAND: Press \<PF1\>H for help Insert

#### Choosing What Data to Send with a File

When you send data, you can send all data in a file; however, KIDS also lets you send a subset of a file’s data to installing sites.

In the Screen to Select Data field, you can enter M code to screen data. The M code should SET\$T:

- If \$T is set to 1, the entry is sent.
- If \$T is set to 0, the entry is *not* sent.

When your code for the screen is executed, the local variable Y is set to the Internal Entry Number (IEN) of the entry being screened, and the M naked indicator is set to the global level @fileroot@(Y,0). Therefore, you can use the values of Y and the naked indicator in your screen.

In the DATA LIST field, you can select a search template. The contents of the template are the entries that are exported.

If you choose both a screen and a search template, the screen is applied to the entries stored in the search template.

<span id="_Toc200269991" class="anchor"></span>Figure 11: KIDS—Settings for Sending Data

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

File List (Name or Number)

┌───────────────────────── DD Export Options ────────────────────────────┐

│┌──────────────────────── <span class="mark">Data Export Options</span> ─────────────────────────┐│

││ Site's Data: OVERWRITE ││

││ ││

││ Resolve Pointers: YES May User Override Data Update: YES ││

││ ││

││ Data List: ││

││ ││

││ Screen to Select Data ││

││ ││

││ ││

│└──────────────────────────────────────────────────────────────────────┘│

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

#### Determining How Data is Installed at the Receiving Site

When you send data with a file, KIDS gives you several options about how the data is sent. [Table 3](#_Ref503165923) lists the four ways KIDS can install file entries at the receiving site:

<table>
<caption><p><span id="_Ref195598380" class="anchor"></span>Table 4: KIDS—Option and Protocol Installation Actions</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Installation Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ADD ONLY IF NEW FILE</strong></td>
<td>Installs data at the installing site only if this file is new to the site or if there is no data in this file at the site.</td>
</tr>
<tr class="even">
<td><strong>MERGE</strong></td>
<td><p>If no matching entry is found, the incoming entry is added. When the incoming entry matches an existing entry on the system, site fields that are <em>non</em>-<strong>NULL</strong> are preserved. Only <strong>NULL</strong> fields in a matching site entry are overwritten by incoming values.</p>
<p>KIDS does <em>not</em> send out cross-references with the data. When you merge the data, however, KIDS re-indexes and creates new cross-references. Also, when you merge the data, KIDS does <em>not</em> delete the old cross-references for that data.</p></td>
</tr>
<tr class="odd">
<td><strong>OVERWRITE</strong></td>
<td>If no matching entry is found, the incoming entry is added. When the incoming entry matches an existing entry on the system, site fields that are <em>non</em>-<strong>NULL</strong> are overwritten by incoming data. Values in the site’s fields are preserved when the incoming field value is <strong>NULL</strong>, however.</td>
</tr>
<tr class="even">
<td><strong>REPLACE</strong></td>
<td><p>If no matching entry is found, the incoming entry is added. When the incoming entry matches an existing entry at the top level of a file, all fields in the existing entry that are fields in the incoming data dictionary are purged; then field values for the new entry are brought in. Values in fields that are <em>not</em> part of the incoming data dictionary are preserved.</p>
<p>KIDS does <em>not</em> send out cross-references with the data. When you replace the data, however, KIDS re-indexes and creates new cross-references. Also, when you replace the data, KIDS deletes any old cross-references for that data.</p>
<p>With Multiples, if the <strong>.01</strong> field of an incoming Multiple matches the <strong>.01</strong> field of an existing Multiple, the existing Multiple entry is completely purged, and the data from the incoming Multiple replaces the current Multiple entirely; values for fields in the existing Multiple that are <em>not</em> in the incoming data dictionary are <em>not</em> restored.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref195598380" class="anchor"></span>Table 4: KIDS—Option and Protocol Installation Actions

You can specify different settings for separate files; within a file, however, all data *must* be installed in one of these four ways.

You can give the installing site the choice of overriding the data update. If you set May User Override Data Update to YES, the installing site has the choice of whether to bring in data that has been sent with this file. They are *not* given the choice of how to install data, however (add only if new file instead of merge instead of OVERWRITE instead of REPLACE). If you set this field to NO, the installing site cannot override bringing in data.

#### How KIDS Matches Incoming Entries with Existing Entries

When KIDS installs VA FileMan data, it treats incoming entries differently depending on whether the entry is a new entry for the file *or* the incoming entry matches an existing entry in the file.

KIDS decides if an incoming entry is new or matches an existing entry by checking, in order:

The B index of the file or Multiple, or the .01 field if there is no B index.

1.  The Internal Entry Number (IEN) of the entry (if applicable).
2.  The identifiers of the entry (if applicable).

First, KIDS makes a tentative match based on the B index. If there is no B index, KIDS goes through the .01 field entries of the file one-by-one looking for a match.

![](kernel-8-0-developer-s-guide-kids-user-guide/007.png) NOTE: The “B” cross-reference holds the name as a subscript. The maximum length of subscripts is defined for each operating system and is stored in the MUMPS OPERATING SYSTEM (#.7) file. KIDS uses this length \[for example, 63 (default) or 99\] as the limit of characters to compare.

If a match (either by the B cross-reference or by the first piece of the Zero node) is *not* found, the incoming entry is considered new and is added to the file. If a match or matches are found, two additional checks are made to determine whether any of the existing entries are a match.

KIDS next checks whether the IENs of any tentatively matched entries are related. If the file has a defined .001 field, the IEN is a meaningful attribute of an entry. In this case, the IENs *must* match. If the input transform of the .01 field contains DINUM, it operates the same way as a .001 field. If the IEN is meaningful, and no match is found, the incoming entry is considered new and is added to the file.

If the possibility of a match remains after checking IENs, KIDS performs a final check based on identifiers.

A well-designed file uses one or more identifiers to act as key fields, so that each entry is unique with respect to name and identifiers. If identifiers exist on either the target file or the incoming data dictionary, KIDS checks the values of all such identifier fields. The value of each identifier field *must* be the same for the existing entry and the incoming entry to be considered a match. Only the internal value of the identifier field is checked (so if an identifier is a POINTER field, problems could result). Only identifiers that have valid field numbers are used in this process.

If there is still more than one matching entry after checking .01 fields, IENs, and identifiers, the lowest numbered entry in the site’s file is considered a match for the incoming entry for the file. On the other hand, if no match is found after checking .01 fields, IENs, and identifiers, the entry is considered new and is added to the file.

#### Limited Resolution of Pointers

A feature of data export provided by KIDS is resolving POINTERs. For each file exported with data, you can choose whether to perform POINTER resolution on that file’s POINTER fields (except for .01 fields, identifier fields, and POINTER fields pointing to other POINTER fields).

KIDS does *not* resolve POINTERs for .01 fields and identifier fields in files or Multiples, nor fields that point to other POINTER fields. KIDS can resolve POINTERs, however, for all other POINTER fields in a given file or Multiple.

When you do *not* resolve POINTERs, and the file being installed has POINTER fields, data entries for that file are installed with whatever numerical POINTER values are in the POINTER fields. In which case, there is a good chance that the POINTER fields no longer point to the intended entries in the pointed to file.

Resolution of POINTERs remedies this by exporting the FREE TEXT value of the pointed-to entry. When KIDS has finished installing all files and data entries at the installing site, it begins the process of resolving POINTERs (if any files are set to have POINTERs resolved).

For each field in an entry that is a POINTER field, KIDS does a lookup in the pointed to file for the FREE TEXT value of the original pointed-to entry. If it finds an exact and unique match, it resolves the original POINTER by storing the IEN of the new matching entry in the POINTER field. If it *cannot* find an exact match, because there are no matching entries or there are multiple matching entries, then the POINTER field is left blank, and KIDS displays an error message.

Resolution of POINTERs works with pointed-to entries that are themselves VARIABLE POINTERs. In these cases, it stores the file to which the pointed-to entry was pointing and then resolves the POINTER in the appropriate target file only.

Once all POINTERs are resolved, KIDS re-indexes each file. Each time KIDS finishes resolving POINTER fields in a given file, it re-indexes that file.

#### Re-Indexing Files

Once all new data has been added to all files, KIDS re-indexes the files. If any of the files have compiled cross-references, the compiled cross-reference routines are rebuilt. Then, if any data was sent for a file, KIDS re-indexes *all* traditional cross-references and *all* new-style indexes with an ACTIVITY that contains an I, for *all* the records in the file. Only the SET logic is executed.

#### Data Dictionary Cleanup

If you change the definition of a field or remove a cross-reference, you *must* delete the field or cross-reference or otherwise clean it up on the target account during the Pre-install routine. You *must* completely purge the target site’s data dictionary of the old field definition, even if you are re-using the same node and piece for a new field. This cleanup ensures that the data dictionary does *not* end up with an inconsistent structure after the installation.

You no longer need to clean up WORD-PROCESSING fields in the data dictionary, however. Before KIDS, updated data dictionary field attributes stored in WORD-PROCESSING fields (such as field description or technical description) did *not* completely overwrite a pre-existing attribute when installed. If the incoming value had fewer lines than the pre-existing one, the install of the data dictionary did *not* delete the surplus lines automatically; this deletion had to be done in the pre-install. KIDS, on the other hand, completely replaces the values of WORD-PROCESSING fields in data dictionaries.

#### Edit a Build: Components

In the third screen in the Edit a Build \[XPD EDIT BUILD\] option, you can select the components of a software application to include in the build.

KIDS lets you enter an explicit list of components for each component type. You are *not* restricted by namespace. You can select items for each type of component simply by choosing them. Items can also be selected with the asterisk (\*) wildcard and the exclusion sign (-).

To add an entry to the list when a similarly named entry already exists in the list, use the normal VA FileMan convention of surrounding the entry with quotes. For example, to add ZZTK to the list when ZZTK1 already exists in the list, enter “ZZTK” in quotes.

With most component types, the permissible installation actions are:

- SEND TO SITE
- DELETE AT SITE

Some component types, however, have additional installation actions available; the special cases are discussed on the following pages.

![](kernel-8-0-developer-s-guide-kids-user-guide/008.png) REF: For a list of Kernel component types, see the “[Create a Build Using Namespace](#create-a-build-using-namespace)” section.

<span id="_Ref257006469" class="anchor"></span>Figure 12: KIDS—Screen 3 of Edit a Build: Components

Edit a Build <span class="mark">PAGE 3</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

Build Components

PRINT TEMPLATE (0)

SORT TEMPLATE (0)

INPUT TEMPLATE (0)

FORM (0)

FUNCTION (0)

DIALOG (0)

BULLETIN (0)

MAIL GROUP (0)

HELP FRAME (0)

ROUTINE (0)

OPTION (0)

SECURITY KEY (0)

PROTOCOL (0)

LIST TEMPLATE (0)

HL7 APPLICATION PARAMETE (0)

HL LOWER LEVEL PROTOCOL (0)

HL LOGICAL LINK (0)

REMOTE PROCEDURE (0)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

![](kernel-8-0-developer-s-guide-kids-user-guide/009.png) NOTE: This is an expanded view of this screen to show you all currently available component types. You must scroll through the list to see all available types.

#### Edit a Build: Options and Protocols

Menus and protocols are like other component types, except for menus and protocols, which have more than the standard SEND TO SITE and DELETE AT SITE installation actions.

![](kernel-8-0-developer-s-guide-kids-user-guide/010.png) NOTE: Beginning with Kernel 8.0, you can no longer send out an option with an attached scheduling frequency. Scheduling of options was moved out of the OPTION (#19) file and into the OPTION SCHEDULING (#19.2) file. One advantage to this is that a developer’s scheduling settings no longer overwrites a site’s scheduling settings.

To indicate to the site that an option should be scheduled regularly, you should fill in the SCHEDULING RECOMMENDED field for the option. You can enter YES, NO, or STARTUP. This indicates to the site whether they should regularly schedule the option or *not*. You should list the actual frequency you *recommend* in the option’s description. The site can then use the TaskMan option Print Recommended for Queuing Options to list all options that developers have *recommended* scheduling.

<table>
<caption><p><span id="_Ref72233655" class="anchor"></span>Table 5: KIDS—Key Variables during the Environment Check (listed alphabetically)</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Option/Protocol Installation Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="SEND_TO_SITE_action" class="anchor"></span><strong>SEND TO SITE</strong></td>
<td><p>Menu, option, or protocol is installed at the site; any existing version already at the site is completely purged beforehand, except those options that are currently marked as “Out of Order” (OoO).</p>
<p>![](kernel-8-0-developer-s-guide-kids-user-guide/011.png) <strong>NOTE:</strong> The OUT OF ORDER MESSAGE field (aka OoO field) in the OPTION (#19) file is updated by KIDS during an install. When an option or protocol is sent, KIDS allows the site to disable them during the install. That means KIDS adds the OoO field at the beginning of the install and removes it at the end. In the case where the OoO already exists for an option, KIDS does nothing. Because of this, KIDS does <em>not</em> transport the OoO field. If a developer wants to add or change an OoO, they should use the <strong><a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.pdf#out_xpdmenu">OUT^XPDMENU</a>()</strong>: Edit Option's Out of Order Message API during the post-install.</p></td>
</tr>
<tr class="even">
<td><span id="DELETE_AT_SITE_action" class="anchor"></span><strong>DELETE AT SITE</strong></td>
<td>Menu or protocol is deleted at site.</td>
</tr>
<tr class="odd">
<td><strong>USE AS LINK FOR MENU ITEMS</strong></td>
<td>Designates a menu or protocol to be used as a link. The menu or protocol is <em>not</em> exported to the site; instead, its name is sent so that any item you link to it as a menu item or protocol (and send) becomes a sub-item on the corresponding menu or protocol at the site. KIDS does <em>not</em> disable options and protocols that have an Action of <strong>USE AS LINK FOR MENU ITEMS</strong>.</td>
</tr>
<tr class="even">
<td><strong>MERGE MENU ITEMS</strong></td>
<td><p>All fields in the menu or protocol except for items are purged and replaced by the incoming values for those fields. Any items at the site that do <em>not</em> match incoming items are left as is. Any items that do match incoming items are completely replaced by the incoming items.</p>
<p>The advantage with this action is that it preserves locally added items at the site. The disadvantage is that if you have removed items, the removed items are <em>not</em> purged at the site.</p></td>
</tr>
<tr class="odd">
<td><strong>ATTACH TO MENU</strong></td>
<td>Designates an option or protocol, <em>not</em> exported to the site, to be attached to a menu that is exported. This is used when a menu is sent by KIDS to a site and the developer wants the local option or protocol attached to the menu. The option or protocol is <em>not</em> exported to the site; instead, its name is sent, and the local option or protocol becomes a sub-item on the menu that is sent.</td>
</tr>
<tr class="even">
<td><strong>DISABLE DURING INSTALL</strong></td>
<td>Designates an option or protocol that is <em>not</em> exported to be disabled during the KIDS install process.</td>
</tr>
</tbody>
</table>

<span id="_Ref72233655" class="anchor"></span>Table 5: KIDS—Key Variables during the Environment Check (listed alphabetically)

#### Edit a Build: Routines

Routine selection is done based on POINTERs to entries in the ROUTINE (#9.8) file, but this file is *not* automatically updated when programs are saved and deleted on an M system. So, before adding routines to a build entry, you should run KIDS’ Update Routine File option. Be sure to update all the routines and routine namespaces that you need to select for your build.

When selecting routines for the build, you can select individual routines by typing in their individual names. You can select a namespace group of routines by using the \* wildcard. For example, to include all routines in the namespace XQ, type in XQ\*. You can exclude routines by inserting the - exclusion sign before either a single name or a wild-carded namespace. For example, to exclude all routines in the XQI namespace, type -XQI\*.

For each routine, you can choose one of two actions:

- [SEND TO SITE](#SEND_TO_SITE_action) (default)
- [DELETE AT SITE](#DELETE_AT_SITE_action)

The default action is [SEND TO SITE](#SEND_TO_SITE_action). If you choose [DELETE AT SITE](#DELETE_AT_SITE_action), the routine is deleted at the installing site.

Installers of KIDS software applications have a choice to update routines across multiple CPUs. If they choose to do this, routines are installed (or deleted) across all CPUs the site selects. KIDS displays various status messages while each CPU is updated. Sites cannot automatically install routines in the site’s manager accounts; however, you still *must* instruct the site to manually install any routine that goes in the manager’s account.

<span id="_Toc200269995" class="anchor"></span>Figure 13: KIDS—Choosing Routines

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

BUILD COMPONENTS

┌──────────────────────────── <span class="mark">ROUTINE</span> ───────────────────────────────────┐

│ │

│ +XQSRV4 SEND TO SITE │

│ XQSTCK DELETE AT SITE │

│ XQT SEND TO SITE │

│ XQT1 SEND TO SITE │

│ XQT2 SEND TO SITE │

│ XQT3 SEND TO SITE │

│ XQT4 SEND TO SITE │

│ XQTOC SEND TO SITE │

│ XQUSR SEND TO SITE │

│ │

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

#### Edit a Build: Dialog Entries (DIALOG \[#.84\] File)

VA FileMan supports the capability for other software applications to store their dialog in the VA FileMan DIALOG (#84) file. Some advantages to using the DIALOG (#.84) file for user interaction include:

- Separating user interaction from other program functionality. This is a helpful step for creating GUI interfaces.
- Reusing dialog. When dialog is stored in the DIALOG (#.84) file, it can be re-used.
- Easily generating software application error lists. If error lists are stored in DIALOG (#.84) file, there is a single point of access to print a complete list of errors.
- Implementing alternate language interfaces. Multiple language versions of a dialog can be exported; also, entries for one language’s set of dialogs can be swapped with entries for another language’s set of dialogs.

KIDS allows you to export entries your software application maintains in the DIALOG (#.84) file. Simply select which DIALOG entries you want to include in your software application, as you would for any other software application component, and choose an installation action for each item (the default is [SEND TO SITE](#SEND_TO_SITE_action), the other permissible choice is [DELETE AT SITE](#DELETE_AT_SITE_action)).

![](kernel-8-0-developer-s-guide-kids-user-guide/012.png) REF: For more information on using the DIALOG (#.84) file, see the *VA FileMan Developer’s Guide*.

#### Edit a Build: Forms

You do *not* need to select which blocks to send when you send VA FileMan ScreenMan forms. You only need to select the form; KIDS sends all blocks associated with a form once you have chosen the form.

#### Edit a Build: Templates

When you select PRINT, SORT, or INPUT templates, KIDS appends the file number to the name of the template. This ensures that a unique entry exists for each template (since two templates of the same name could exist for two different files).

<span id="_Toc200269996" class="anchor"></span>Figure 14: KIDS—Selecting Templates

Edit a Build <span class="mark">PAGE 2</span> OF 5

Name: ZXG DEMO 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

BUILD COMPONENTS

┌─────────────────────────── <span class="mark">PRINT TEMPLATE</span> ────────────────────────────┐

│ │

│ +XUSER LIST FILE \#200 SEND TO SITE │

│ XUSERINQ FILE \#200 SEND TO SITE │

│ XUSERVER DISPLAY FILE \#19.081 SEND TO SITE │

│ XUSERVER HEADER FILE \#19.081 SEND TO SITE │

│ XUUFAA FILE \#3.05 SEND TO SITE │

│ XUUFAAH FILE \#3.05 SEND TO SITE │

│ XUUSEROPTH FILE \#19.081 SEND TO SITE │

│ XUUSEROPTP FILE \#19.081 SEND TO SITE │

│ │

│ │

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

### Transporting a Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have created a build entry and added all files and components you want to export, you are ready to export your software application. KIDS uses a transport global as the mechanism to move data. INIT routines are no longer the transport mechanism (which removes the old restrictions on the amount of data you can export). Transport globals can then be written to distributions, which are HFS files. Use the Transport a Distribution \[XPD TRANSPORT PACKAGE\] option to generate transport globals and create distributions.

Depending on how you answer the questions in this option, the transport globals this option generates can be stored in:

- A distribution, which is then ready to export as a Host file.
- A PackMan message (to be sent over the network).
- The ^XTMP global on your local system.

If you choose to transport the distribution through a Host file enter HF after the “Transport through (HF)Host File or (PM)PackMan:” prompt and enter a Host file name after the “Enter a Host File” prompt. The option creates transport globals and puts them in the distribution (HFS file) that you specify.

<span id="_Toc200269997" class="anchor"></span>Figure 15: KIDS—Transport a Distribution Option: Creating a Distribution Sample User Dialogue

Select Edits and Distribution Option: <span class="mark">TRANSPORT A DISTRIBUTION \<Enter\></span>

Enter the Package Names to be transported. The order in which

they are entered will be the order in which they are installed.

First Package Name: <span class="mark">ZXG DEMO 1.0 \<Enter\></span>

Another Package Name: <span class="mark">ZXG TEST 1.0 \<Enter\></span>

Another Package Name: <span class="mark">\<Enter\></span>

ORDER PACKAGE

1 ZXG DEMO 1.0

2 ZXG TEST 1.0

OK to continue? NO// <span class="mark">YES \<Enter\></span>

Transport through (HF)Host File or (PM)PackMan: <span class="mark">HF \<Enter\></span> Host File

Enter a Host File: <span class="mark">ZXG_EXPT.DAT \<Enter\></span>

Header Comment: <span class="mark">EXPORT OF ZXG PACKAGE \<Enter\></span>

ZXG DEMO 1.0...

ZXG TEST 1.0...

Package Transported Successfully

Select Edits and Distribution Option:

If you do *not* enter a Host file name, KIDS creates the transport globals and stores them in your local ^XTMP global but does *not*WRITE them to a distribution file.

If you have previously created a transport global for this software application in the ^XTMP global and it still exists, KIDS asks you if you want to use what was already generated or if you want to re-generate the transport globals instead.

If you want the distribution sent by a PackMan message enter PM after the “Transport through (HF)Host File or (PM)PackMan:” prompt. You can only send *one* transport global per PackMan message, however.

<span id="_Toc200269998" class="anchor"></span>Figure 16: KIDS—Transport a Distribution Option: Sending through Network (PackMan Message) Sample User Dialogue

Select Edits and Distribution Option: <span class="mark">TRANSPORT A DISTRIBUTION \<Enter\></span>

Enter the Package Names to be transported. The order in which

they are entered will be the order in which they are installed.

First Package Name: <span class="mark">TEST 1.1 \<Enter\></span>

Another Package Name: <span class="mark">\<Enter\></span>

ORDER PACKAGE

1 TEST 1.1

OK to continue? NO// <span class="mark">YES \<Enter\></span>

Transport through (HF)Host File or (PM)PackMan: <span class="mark">PM \<Enter\></span> PackMan

TEST 1.1...

No Package File Link

Subject: TEST

Please enter description of Packman Message

<span class="mark">TEST \<Enter\></span>

Created by XUUSER,FIVE at \<REDACTED\>.VA.GOV (KIDS) on MONDAY, 10/07/96 at 15:21

Do you wish to secure this message? No// <span class="mark">? \<Enter\></span>

If you answer yes, this message will be secured to insure that

what you send is what is actually received.

Do you wish to secure this message? No// <span class="mark">Y \<Enter\></span> (Yes)

Enter the scramble hint: <span class="mark">THIS IS A HINT \<Enter\></span>

Enter scramble password:

Securing the message, now. This may take a while !!!

Send mail to: XUUSER,FIVE Last used MailMan: 04 Oct 96 15:28

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And send to: <span class="mark">\<Enter\></span>

#### When to Transport More than One Transport Global in a Distribution

If several software applications are unrelated, they should be sent as separate distributions. This gives the installing site optimum flexibility to decide when to do each installation.

If a group of software applications is to be installed together, however, and if there are dependencies between the software applications, sending the software applications together in one distribution can give you more control over how the group of software applications is installed. If in some cases only software applications A and B should be installed, and in other situations only software applications A and C should be installed, and you can do the determination yourself (in each software application’s environment check routine), sending the group of software applications in a single distribution lets you control which software applications in the distribution are installed.

When you are using PackMan messages to send your software application (rather than using a distribution), you are limited to sending only one transport global per PackMan message.

#### Multi-Package Builds

Multi-Package builds contain a list of other builds and lists their installation order. A Multi-Package build transports this list of builds (template or meta-build).

<span id="_Toc200269999" class="anchor"></span>Figure 17: KIDS—Multi-package Builds Sample

Edit a Build <span class="mark">PAGE 1</span> OF 5

Name: TEST 3.0 TYPE: <span class="mark">MULTI-PACKAGE</span>

--------------------------------------------------------------------------

Name: TEST 3.0

Date Distributed: OCT 9,2004

Description:

Install Order Packages or Patches

1 TEST 1.0

2 TEST 1.1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

#### Exporting Globals with KIDS

KIDS in Kernel 8.0 supports the installation of global distributions (distributions that export globals). KIDS supports the creation of global distributions by developers. Any number of globals can be included in a build. You are given the opportunity to run an environment check before installing the global and post-install routines after installing the globals. You also are given the choice of KILLing globals prior to installing new globals at a site. If you answer NO to this question, the global is merged with any previously installed global at the site.

![](kernel-8-0-developer-s-guide-kids-user-guide/013.png) REF: For more information on global distributions, see the “KIDS: System Management—Installations” section in the [*Kernel 8.0 Systems Management: KIDS User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf#System_Management_Installations).

<span id="_Toc200270000" class="anchor"></span>Figure 18: KIDS—Exporting Global Distributions Sample

Edit a Build <span class="mark">PAGE 1</span> OF 5

Name: TEST 5.0 TYPE: GLOBAL PACKAGE

--------------------------------------------------------------------------

Name: TEST 5.0

Date Distributed: OCT 9,2004

Description:

Environment Check Rtn.: Post-Install Rtn.:

Globals Kill Global Before Install?

TMP(100) NO

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

### Creating Transport Globals that Install Efficiently

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are some choices you can make when designing your build entries, to make your transport globals install efficiently at the receiving site. You can improve the efficiency of exporting data entries using KIDS:

- When exporting data, you can use the ADD IF NEW option to only add entries if the file did *not* exist prior to the installation. Data is only added if the file is created by the installation. You can use this option to avoid re-exporting data for static files.
- When exporting data, send only the data you need to (KIDS no longer forces you to send all data in a file when you only need to send some of the data). You can select a subset of data to send by using a screen, a search template, or both a screen and a search template.
- When exporting data, resolve POINTERs only if necessary, because resolving POINTERs adds significant overhead to the process of loading data entries.

## Advanced Build Techniques

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The previous sections in this section introduced KIDS from the developer’s perspective, describing the basics of how to create build entries and how to transport distributions. This section describes advanced build techniques that developers can use when creating builds. The following subjects are covered:

- [Environment Check Routine](#environment-check-routine)
- [PRE-TRANSPORTATION ROUTINE (#900) Field](#pre-transportation-routine-900-field)
- [Pre- and Post-Install Routines: Special Features](#pre--and-post-install-routines-special-features)
- [Edit a Build—Screen 4](#edit-a-buildscreen-4)
- [How to Ask Installation Questions](#how-to-ask-installation-questions)
- [Using Checkpoints (Pre- and Post-Install Routines)](#using-checkpoints-pre--and-post-install-routines)
- [Required Builds](#required-builds)
- [Package File Link](#package-file-link)
- [Track Package Nationally](#track-package-nationally)
- [Alpha/Beta Tracking](#alphabeta-tracking)

### Environment Check Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS, like DIFROM, lets you specify an environment check routine. Typically, the environment check routine looks at the installing system and determines whether it’s appropriate to install the software application, based on conditions on the installing site’s current system or environment.

You are *not* required to specify an environment check for your software application to be installed. If, however, you have some special checks that you want to make to decide whether it is appropriate to go ahead with the installation, the environment check routine is the place to do it.

KIDS lets you specify the name of the environment check routine in screen one of EDIT A BUILD ([Figure 23](#_Ref257006361)). Any routine that is specified is automatically sent by KIDS. You do *not* have to list the routine in the Build Components section ([Figure 12](#_Ref257006469)).

#### Self-Contained Routine

The environment check routine itself *must* be a single, self-contained routine, because it is the only routine from your build that is loaded on the installing site’s system at the time it is executed by KIDS. Based on what you find out about the installing system during the environment check, you can tell KIDS to do any of the following:

- Continue installing the software application.
- Abort installing the software application.
- Abort installing all software applications (transport globals) in the distribution.

Although output during the pre-install and post-install should be done with the [MES^XPDUTL(): Output a Message](#mesxpdutl-output-a-message) and [BMES^XPDUTL(): Output a Message with Blank Line](#bmesxpdutl-output-a-message-with-blank-line) APIs, during the environment check routine you should use the ^DIR API for READs and can use direct WRITEs.

#### Environment Check is Run Twice

KIDS runs the environment check routine twice. It runs the environment check routine first when the installer loads the transport global from the distribution (with the Load a Distribution \[XPD LOAD DISTRIBUTION\] option).

KIDS runs the environment check a second time when the user runs the Install Package(s) \[XPD INSTALL BUILD\] option to install the software applications in the loaded distribution.

The KIDS key variable XPDENV indicates in which phase (load or install) the environment check is running.

![](kernel-8-0-developer-s-guide-kids-user-guide/014.png) REF: For more information on XPDENV, see the “[Key Variables during Environment Check](#key-variables-during-environment-check)” section.

#### Key Variables during Environment Check

[Table 5](#_Ref72233655) lists the key variables during the environment check (listed alphabetically):

<table>
<caption><p><span id="_Ref332260478" class="anchor"></span>Table 6: KIDS—Actions Based on Environment Check Conclusions</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DIFROM</strong></td>
<td>For backward compatibility, the variable <strong>DIFROM</strong> is available during the environment check, as well as during the pre- and post-install phases of a KIDS installation. <strong>DIFROM</strong> is set to the version number of the incoming software application.</td>
</tr>
<tr class="even">
<td><strong>XPDENV</strong></td>
<td><p>The KIDS key variable <strong>XPDENV</strong> is available during the environment check only. It can have the following values:</p>
<ul>
<li><blockquote>
<p><strong>1—</strong>The environment check is being run by the KIDS <strong>Install Package(s)</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p><strong>0—</strong>The environment check is being run by the KIDS <strong>Load a Distribution</strong> option.</p>
</blockquote></li>
</ul>
<p>You can use <strong>XPDENV</strong> if, for example, there is a check that is valid to perform at install time, but <em>not</em> at load time.</p></td>
</tr>
<tr class="odd">
<td><strong>XPDGREF</strong></td>
<td><p>This variable contains the location of developer-defined information that is used during the install process. The developer can reference this information using the following syntax:</p>
<p><strong>S X=0,X=$O(@XPDGREF@(namespace,X))</strong></p></td>
</tr>
<tr class="even">
<td><strong>XPDNM</strong></td>
<td>The KIDS key variable <strong>XPDNM</strong> is available during the environment check, as well as during the pre- and post-install phases of a KIDS installation. <strong>XPDNM</strong> is set to the name of the transport global currently being installed. It is in the format of the <strong>.01</strong> field of the software application’s BUILD (#9.6) file entry, which is software application name, concatenated with a space, concatenated with version number.</td>
</tr>
<tr class="odd">
<td><strong>XPDNM(“SEQ”)</strong></td>
<td><p>The <strong>XPDNM(“SEQ”)</strong> variable is available during the pre- and post-install and environment check phases of a KIDS installation. <strong>XPDNM(“SEQ”)</strong> is set to one of the following values:</p>
<ul>
<li><blockquote>
<p><strong>Sequence Number—</strong>If build is a patch and the National Patch Module (NPM) created a sequence number.</p>
</blockquote></li>
<li><blockquote>
<p><strong>NULL</strong>.</p>
</blockquote></li>
</ul>
<p>![](kernel-8-0-developer-s-guide-kids-user-guide/015.png) <strong>NOTE:</strong> This variable was released with Kernel Patch XU*8.0*559.</p></td>
</tr>
<tr class="even">
<td><strong>XPDNM(“TST”)</strong></td>
<td><p>The <strong>XPDNM(“TST”)</strong> variable is available during the pre- and post-install and environment check phases of a KIDS installation. <strong>XPDNM(“TST”)</strong> is set to one of the following values:</p>
<ul>
<li><blockquote>
<p><strong>Test Number—</strong>If build is a patch and the National Patch Module (NPM) created a test number.</p>
</blockquote></li>
<li><blockquote>
<p><strong>NULL</strong>.</p>
</blockquote></li>
</ul>
<p>![](kernel-8-0-developer-s-guide-kids-user-guide/016.png) <strong>NOTE:</strong> This variable was released with Kernel Patch XU*8.0*559.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref332260478" class="anchor"></span>Table 6: KIDS—Actions Based on Environment Check Conclusions

#### Package Version or Installing Version

KIDS provides several functions that you can use during the environment check to compare version numbers of the current software application at the site to the incoming transport global:

- [\$\$VER^XPDUTL](#verxpdutl-parse-version-from-build-name)
- [\$\$VERSION^XPDUTL](#versionxpdutl-package-file-current-version)

![](kernel-8-0-developer-s-guide-kids-user-guide/017.png) REF: For more on these APIs, see the “<u>Application Programming Interfaces (APIs)</u>” section in this section.

#### Telling KIDS to Skip Installing or Delete a Routine

During the environment check, you can tell KIDS to skip installing any routine and change the routine’s installation status to [DELETE AT SITE](#DELETE_AT_SITE_action).

For example, suppose you have one version of a routine for GT.M sites and one version for Caché sites. Based on the type of system your environment check finds; you can use the [\$\$RTNUP^XPDUTL(): Update Routine Action](#rtnupxpdutl-update-routine-action) function to tell KIDS which routines to skip installing.

![](kernel-8-0-developer-s-guide-kids-user-guide/018.png) REF: For more information on deleting environment check routines, see the “[Key Parameters during Pre- and Post-Install Routines](#key-parameters-during-pre--and-post-install-routines)” section in this section.

#### Verifying Patch Installation

During the environment check, you can tell KIDS to verify that a particular patch has been installed on a system prior to the installation of your software application.

For example, if your software application is dependent on a particular patch being installed, you can use the [\$\$PATCH^XPDUTL(): Verify Patch Installation](#patchxpdutl-verify-patch-installation) function to have KIDS alert the user that a required patch is *not* installed on their system.

#### Aborting Installations During the Environment Check

In the environment check, you can decide whether an installation should continue or stop, or whether the installation of all transport globals in the distribution should be aborted.

When you abort the installation of a transport global by setting XPDQUIT or XPDABORT, KIDS outputs a message to the effect that a particular transport global in the installation is being aborted. You should also issue your own message when aborting an installation, however, to give the site some diagnostic information as to why you have chosen to abort the install.

[Table 6](#_Ref332260478) lists ways you can ask KIDS to continue or abort an installation, based on the conclusions of your environment check routine:

<table>
<caption><p><span id="_Toc200270005" class="anchor"></span>Table 7: KIDS—Installation: XPDDIQ Array Sample</p></caption>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>KIDS Desired Action<br />
(Based on Environment Check Conclusions)</th>
<th>How to Tell KIDS to Take Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OK to install this transport global.</td>
<td>(Take no action)</td>
</tr>
<tr class="even">
<td>Do <em>not</em> install this transport global and <strong>KILL</strong> it from <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDQUIT =1</strong></td>
</tr>
<tr class="odd">
<td>Do <em>not</em> install this transport global but leave it in <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDQUIT=2</strong></td>
</tr>
<tr class="even">
<td>Abort another transport global named <strong>pkg_name</strong> in distribution and <strong>KILL</strong> it from <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDQUIT(pkg_name)=1</strong></td>
</tr>
<tr class="odd">
<td>Abort another transport global named <strong>pkg_name</strong> in distribution but leave it in <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDQUIT(pkg_name)=2</strong></td>
</tr>
<tr class="even">
<td>Abort all transport globals in distribution and <strong>KILL</strong> them from <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDABORT=1</strong></td>
</tr>
<tr class="odd">
<td>Abort all transport globals in distribution but leave them in <strong>^XTMP</strong>.</td>
<td>&gt;<strong>S XPDABORT=2</strong></td>
</tr>
</tbody>
</table>

<span id="_Toc200270005" class="anchor"></span>Table 7: KIDS—Installation: XPDDIQ Array Sample

![](kernel-8-0-developer-s-guide-kids-user-guide/019.png) NOTE: It is recommended that you use XPDQUIT when you have a distribution that contains multiple builds, and you only want to selectively install a portion of it. Use the XPDABORT to abort the entire installation of a distribution.

#### Controlling the Queuing of the Install Prompt

By default, KIDS allows the installer to run in the future. It does this by allowing the installer to enter Q at the device prompt. If the XPDNOQUE variable is set to 1, then the installer sees the following prompt and *is not* allowed to enter Q:

<span id="_Toc200270003" class="anchor"></span>Figure 19: KIDS—Dialog When the XPDNOQUE Variable is Set to Disable Queuing

Enter the Device you want to print the Install messages.

Enter a '^' to abort the install.

DEVICE: HOME//

#### Controlling the Disable Options/Protocols Prompt

By default, KIDS asks the following question during KIDS installations:

<span id="_Toc200270004" class="anchor"></span>Figure 20: KIDS—”DISABLE” Default Prompt during Installations

Want to DISABLE Scheduled Options, Options, and Protocols? YES//

You can control the way this question is asked by defining the array XPDDIQ(“XPZ1”) during the environment check. The environment check runs once during the installation and prompts the user if it should run during the load. Setting this array only has an effect during the installation. Therefore, you may want to define the array only when XPDENV=1. You can use this array as follows (each node is optional):

| Array Node             | Description                                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XPDDIQ(“XPZ1”)     | (optional) Set to Zero (0) to force answer to NO or set to 1 to force answer to YES. When this node is set, the site is *not* asked the question. |
| XPDDIQ(“XPZ1”,“A”) | (optional) Replace the default question prompt with the value of this node.                                                                                           |
| XPDDIQ(“XPZ1”,“B”) | (optional) Set to new default answer in external form (YES or NO).                                                                                            |

<span id="_Toc200270007" class="anchor"></span>Table 8: KIDS—Environment Check—XPDDIQ Array Sample

#### Controlling the Move Routines to Other CPUs Prompt

By default, KIDS asks the following question during KIDS installations:

<span id="_Toc200270006" class="anchor"></span>Figure 21: KIDS—”MOVE routines” Default Prompt during Installations

Want to MOVE routines to other CPUs? NO//

You can control the way this question is asked by defining the array XPDDIQ(“XPZ2”) during the environment check. The environment check runs twice (once during load and once during installation), but setting this array only has an effect during the installation. Therefore, you may want to define the array only when XPDENV=1. You can use this array as follows (each node is optional):

<table>
<caption><p><span id="_Toc199951051" class="anchor"></span>Table 9: KIDS—Key Parameters during the Pre- and Post-install Routines</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Array Node</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XPDDIQ(“XPZ2”)</strong></td>
<td><p>(optional) Set to:</p>
<ul>
<li><blockquote>
<p><strong>Zero (0)—</strong>Force answer to <strong>NO</strong>.</p>
</blockquote></li>
<li><blockquote>
<p><strong>1—</strong>Force answer to <strong>YES</strong>.</p>
</blockquote></li>
</ul>
<p>When this node is set, the question is <em>not</em> asked.</p></td>
</tr>
<tr class="even">
<td><strong>XPDDIQ(“XPZ2”,“A”)</strong></td>
<td>(optional) Replace the default question prompt with the value of this node.</td>
</tr>
<tr class="odd">
<td><strong>XPDDIQ(“XPZ2”,“B”)</strong></td>
<td>(optional) Set to new default answer in external form (<strong>YES</strong> or <strong>NO</strong>).</td>
</tr>
</tbody>
</table>

<span id="_Toc199951051" class="anchor"></span>Table 9: KIDS—Key Parameters during the Pre- and Post-install Routines

<span id="_Toc200270008" class="anchor"></span>Figure 22: KIDS—Environment Check Routine Sample

ZZUSER1 ;SFISC/RWF - CHECK TO SEE IF OK TO LOAD ; 8 Sep 94 10:39

;;8.0T13;KERNEL;;Aug 01, 1994

N Y

I \$S(\$D(DUZ)\[0:1,\$D(DUZ(0))\[0:1,'DUZ:1,1:0) W !!,\*7,"\>\> DUZ and DUZ(0) must be defined as an active user to initialize." S XPDQUIT=2

I \$D(^DD(200,0))\[0,XPDNM'\["VIRGIN INSTALL" W !!,"You need to install the KERNEL - VIRGIN INSTALL 8.0 package, instead of this package!!" G ABRT

;check for Toolkit 7.3

I \$\$VERSION^XPDUTL("XT")\<7.3 W !!,"You need Toolkit 7.3 installed!" G ABRT

;

W !,"I'm checking to see if it is OK to install KERNEL v",\$P(\$T(+2),";",3)," in this account.",!

W !!,"Checking the %ZOSV routine" D GETENV^%ZOSV

I \$P(Y,"^",4)="" W !,"The %ZOSV routine isn't current.",!,"Check the second line of the routine, or your routine map table." S XPDQUIT=2

;must have Kernel 7.1

S Y=\$\$VERSION^XPDUTL("XU") G:Y\<7.1 OLD

;Test Access to % globals, only check during install

D:\$G(XPDENV) GBLOK

I '\$G(XPDQUIT) W !!,"Everything looks OK, Lets continue.",!

Q

;

OLD W !!,\*7,"It looks like you currently have version ",Y," of KERNEL installed."

W !,\*7,"You must first install KERNEL v7.1 before this version can be installed.",!

;abort install, delete transport global

ABRT S XPDQUIT=1

Q

;

GBLOK ;Check to see if we have WRITE access to needed globals.

W !,"Now to check protection on GLOBALS.",!,"If you get an ERROR, you need to add WRITE access to that global.",!

F Y="^%ZIS","^%ZISL","^%ZTER","^%ZUA" W !,"Checking ",Y S @(Y\_"=\$G("\_Y\_")")

Q

### PRE-TRANSPORTATION ROUTINE (#900) Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE-TRANSPORTATION ROUTINE (#900) field in the BUILD (#9.6) file contains a \[TAG^\]ROUTINE that is run during the transportation process for the Build. This allows developers to populate the transport global using the XPDGREF variable.

Developers can put information in the KIDS Transport Global, which can be used by the Pre-install, Environment Check, and/or Post-install routines. KIDS runs the \[TAG^\]ROUTINE in the PRE-TRANSPORTATION ROUTINE field during the transport process. This routine can use the XPDGREF variable to set nodes in the transport global. For example, enter the following at the Programmer prompt:

\>S @XPDGREF@("My Namespace",1)="Information I need during install"

During the install process, in the Pre-install, Environment Check, and/or Post-install routines, the developer can retrieve the data by using the same variable, XPDGREF. Since these nodes are part of the transport global, they are removed when the install is completed.

<span id="_Ref257006361" class="anchor"></span>Figure 23: KIDS—PRE-TRANSPORTATION ROUTINE Field Sample

Edit a Build <span class="mark">PAGE 1</span> OF 4

Name: TEST 4.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

Name: TEST 4.0

Date Distributed: OCT 9,2004

Description:

Environment Check Routine:

Pre-Install Routine:

Post-Install Routine:

Pre-Transportation Routine: TAG^ROUTINE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND Press PF1H for help Insert

### Pre- and Post-Install Routines: Special Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS, like DIFROM, lets you specify pre-install and post-install routines. Typically, the pre- and post-install routines are used to perform pre-install and post-install conversions. This section describes how to use pre- and post-install routines with KIDS installations.

Pre- and post-routines are optional; you are *not* required to specify them for your software application to be installed. If, however, you have some special actions you want to take, either before or after your installation, the pre- and post-install routines are the places to do it.

KIDS lets you specify the names for pre- and post-install routines in screen one of EDIT A BUILD ([Figure 23](#_Ref257006361)). Any routine that is specified is automatically sent by KIDS. You do *not* have to list the routine in the Build Components section ([Figure 12](#_Ref257006469)).

Two functions can be called during the install process to disable or enable an option or protocol:

- [\$\$OPTDE^XPDUTL(): Disable/Enable an Option](#optdexpdutl-disableenable-an-option)
- [\$\$PRODE^XPDUTL(): Disable/Enable a Protocol](#prodexpdutl-disableenable-a-protocol)

Do *not* set up variables during the pre-install for use during the installation or the post-install, because these variables are lost if the installation aborts midway through and then is restarted by the site using the restart option.

You can reference any routine exported in your build, since all routines with a [SEND TO SITE](#SEND_TO_SITE_action) action are installed by the time the pre- and post-install routines run.

#### Aborting an Installation During the Pre-Install Routine

You can abort an installation during the pre-install routine by setting the XPDABORT variable to 1 and quitting. This is exactly as if the installing site pressed \<CTRL\>C, in the sense that no cleanup is done; options are left disabled. KIDS prints one message to the effect that the install aborted in the pre-install program. If you abort an installation in this manner, you need to tell the site what to do to either re-start the installation or clean up the system from the state it was left in.

#### Setting a File’s Package Revision Data Node (Post-Install)

A new Package Revision Data node can now be updated during the *post*-install. This node is in ^DD(filenumber,0,“VRRV”). It is defined by the developer who distributes the software application and may contain patch or revision information regarding the file. VA FileMan’s \$\$GET1^DID API can be used to retrieve the content of the node and PRD^DILFD API updates the node.

![](kernel-8-0-developer-s-guide-kids-user-guide/020.png) REF: For more information, see the *VA FileMan Developer’s Guide*.

#### Key Parameters during Pre- and Post-Install Routines

| Parameter             | Description                                                                                                                                                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XPD NO_EPP_DELETE | If this parameter is set to 1, KIDS does *not* delete any environment check Pre and Post routines, regardless if the Environment Check routine is marked as “DELETE AT SITE.” By default, this parameter is set to 1 (do *not* delete), so support personnel are able to look at those routines for troubleshooting purposes. |

<span id="_Toc200270010" class="anchor"></span>Table 10: KIDS—Key Variables during the Pre- and Post-install Routines

#### Key Variables during Pre- and Post-Install Routines

<table>
<caption><p><span id="_Toc200270012" class="anchor"></span>Table 11: KIDS—DIR Input Values for KIDS Install Questions</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XPDNM</strong></td>
<td>The <strong>XPDNM</strong> variable is available during the pre- and post-install and environment check phases of a KIDS installation. <strong>XPDNM</strong> is set to the name of the build currently being installed. It is in the format of the <strong>.01</strong> field of the software application’s BUILD (#9.6) file entry, which is software application name, concatenated with a space, concatenated with version number.</td>
</tr>
<tr class="even">
<td><strong>XPDNM(“TST”)</strong></td>
<td><p>Released with Kernel Patch XU*8.0*559, the <strong>XPDNM(“TST”)</strong> variable is available during the pre- and post-install and environment check phases of a KIDS installation. <strong>XPDNM(“TST”)</strong> is set to one of the following values:</p>
<ul>
<li><blockquote>
<p><strong>Test Number—</strong>If build is a patch and the National Patch Module (NPM) created a test number.</p>
</blockquote></li>
<li><blockquote>
<p><strong>NULL</strong>.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>XPDNM(“SEQ”)</strong></td>
<td><p>Released with Kernel Patch XU*8.0*559, the <strong>XPDNM(“SEQ”)</strong> variable is available during the pre- and post-install and environment check phases of a KIDS installation. <strong>XPDNM(“SEQ”)</strong> is set to one of the following values:</p>
<ul>
<li><blockquote>
<p><strong>Sequence Number—</strong>If build is a patch and the National Patch Module (NPM) created a sequence number.</p>
</blockquote></li>
<li><blockquote>
<p><strong>NULL</strong>.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>DIFROM</strong></td>
<td>For backward compatibility, the <strong>DIFROM</strong> variable is available during the pre- and post-install (as well as environment check) phases of a KIDS installation. <strong>DIFROM</strong> is set to the version number of the incoming software application.</td>
</tr>
<tr class="odd">
<td><strong>ZTQUEUED</strong></td>
<td><p>If the <strong>ZTQUEUED</strong> variable is:</p>
<ul>
<li><blockquote>
<p>Present—You know that you are running as a queued installation.</p>
</blockquote></li>
<li><blockquote>
<p><em>Not</em> present—You know that the installer chose to run the installation directly instead of queuing it.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc200270012" class="anchor"></span>Table 11: KIDS—DIR Input Values for KIDS Install Questions

#### NEW the DIFROM Variable When Calling MailMan

You are free to use the MailMan API to send mail messages during pre- and post-install routines (provided MailMan exists on the target system). Make sure that you NEW the DIFROM variable before calling any of the MailMan APIs, however. MailMan APIs can terminate prematurely if the DIFROM variable is present because the DIFROM variable has a special meaning within MailMan.

#### Update the Status Bar During Pre- and Post-Install Routines

During the installation, if the device selected for output is a VT100-compatible (or higher) terminal, KIDS displays the installation output in a virtual window on the terminal. Below the virtual window, a progress bar graphically illustrates the percentage complete that the current part of the installation has reached. KIDS resets the status bar prior to the Pre- and Post-install routines.

![](kernel-8-0-developer-s-guide-kids-user-guide/021.png) REF: For more information on the status (progress) bar, see the “Installation Progress” section in the “KIDS Systems Management Installations” section in the [*Kernel 8.0 Systems Management: KIDS User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf#Installation_Progress).

You can provide a similar status bar for users in the Pre- and Post-Install by doing the following:

1.  SET XPDIDTOT=total number of items.
3.  DO UPDATE^XPDID(current number of items). This moves the status bar.

For example, if you were converting 100 records and want to update the user every time you have completed 10% of the records you would enter the following at the Programmer prompt:

\>SET XPDIDTOT=100

\>F%=1:1:100 D CONVERT I'(%#10) D UPDATE^XPDID(%)

If you wish to display a status bar at various intervals throughout your Pre or Post-install routines, you should reset the status bar. To reset the status bar, enter the following at the Programmer prompt:

\>SET XPDIDTOT=0

\>D UPDATE^XPDID(0)

### Edit a Build—Screen 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen four of the Edit a Build \[XPD EDIT BUILD\] option is where you can set up the install questions, any required builds, PACKAGE (#9.4) file links, and tracking software application information for a build.

<span id="_Toc200270011" class="anchor"></span>Figure 24: KIDS—Screen 4 of Edit a Build Sample

Edit a Build <span class="mark">PAGE 4</span> OF 5

Name: TEST 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

Install Questions

Required Builds

Package File Link...: TEST

Track Package Nationally: NO

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

### How to Ask Installation Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You are *not* required to ask any installation questions for your software application to be installed. If, however, you have some special actions that you can take in your pre-install and post-install processes, and these special actions depend on information you need to get from your installer, then you need a way to ask these questions.

Screen four of the Edit a Build \[XPD EDIT BUILD\] option is where you can set up the install questions for a build.

To ask questions, you need to supply KIDS with the proper DIR input values for each question. Then, KIDS uses the DIR utility to ask installation questions when performing installations. The DIR input values you can supply for each question are:

| DIR Input Value | Description                                |
|-----------------|--------------------------------------------|
| DIR(0)      | Question format.                           |
| DIR(A)      | Question prompt.                           |
| DIR(A,#)    | Additional message before question prompt. |
| DIR(B)      | Default answer.                            |
| DIR(?)      | Simple help string.                        |
| DIR(?,#)    | Additional simple help.                    |
| DIR(??)     | Help frame.                                |

<span id="_Ref62737377" class="anchor"></span>Table 12: KIDS—Functions Using Checkpoints *with* Callbacks

![](kernel-8-0-developer-s-guide-kids-user-guide/022.png) REF: For information on the purpose of these variables, permissible values for them, and which are required versus which are optional, see the *VA FileMan Developer’s Guide*.

#### Question Subscripts

For each question you want to ask, the .01 field of the question (as stored by KIDS) is a subscript. The subscript *must* be in one of two forms:

- Pre-Install Questions—PRE*xxx*
- Post-Install Questions—POS*xxx*

Where “*xxx*” in the subscript can be any string up to 27 characters in length. KIDS asks questions whose subscript starts with PRE during the pre-install and questions whose subscript starts with POS during the post-install.

The order in which questions are asked during the pre- or post-installs is the same as the sorting order of the subscript itself. KIDS asks questions with the lowest sorting subscript first and proceeds to the highest sorting subscript.

#### M Code in Questions

Besides specifying the DIR input variables, you can specify a line of M code that is executed after the DIR input variables have been set up but prior to the VA FileMan ^DIR call. The purpose of this line of M code is so that you can modify the DIR variables, if necessary, before ^DIR is called.

The M code *must* be standalone, however; it cannot depend on any routine in the software application (other than the environment check routine) since no other exported routines besides the environment check routine are loaded on the installing system.

#### Skipping Installation Questions

If you want to prevent a question from being asked, you should KILL the DIR variable in the line of M code for that question (execute K DIR).

#### Accessing Questions and Answers

Once the questions have been asked, the results of the questions are available (during pre-install and post-install only) in the following locations:

- Pre-Install Questions:

XPDQUES(PRExxx)=internal form of answer

XPDQUES(PRExxx, “A”)=prompt

XPDQUES(PRExxx, “B”)=external form of answer

- Post-Install Questions:

XPDQUES(POSxxx)=internal form of answer

XPDQUES(POSxxx, “A”)=prompt

XPDQUES(POSxxx, “B”)=external form of answer

The results of the questions for the pre-install can only be accessed (in XPDQUES) during the pre-install, and the results of the questions for the post-install can only be accessed (in XPDQUES) during the post-install. At all other times, XPDQUES is undefined for pre- and post-install questions.

<span id="_Toc200270013" class="anchor"></span>Figure 25: KIDS—Pre-install Question (Setting Up) Sample

Edit a Build <span class="mark">PAGE 4</span> OF 5

┌───────────────────────── <span class="mark">Install Questions</span> ────────────────────────────┐

│ Name: PRE1 │

│ │

│ DIR(0): YA^^ │

│ │

│ DIR(A): Do you want to run the pre-install conversion? │

│DIR(A,#): │

│ │

│ DIR(B): YES │

│ │

│ DIR(?): Answer YES to run the pre-install conversion, NO to skip it. │

│DIR(?,#): │

│ DIR(??): │

│ │

│ M Code: │

└────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Toc200270014" class="anchor"></span>Figure 26: KIDS—Appearance of Question during Installation

Do you want to run the pre-install conversion? YES// <span class="mark">? \<Enter\></span>

Answer YES to run the pre-install conversion, NO to skip it...

Do you want to run the pre-install conversion? YES//

#### Where Questions Are Asked During Installations

KIDS asks the pre- and post-install questions when a site initiates an installation of the software application. The order of the questions is:

1.  KIDS runs environment check routine, if any.
4.  KIDS asks pre-Install questions.
5.  KIDS asks generic KIDS installation questions.
6.  KIDS asks post-Install questions.
7.  KIDS asks site to queue the installation or run it directly.

### Using Checkpoints (Pre- and Post-Install Routines)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS allows the installing site to restart installations that have aborted. This means that your pre-install and post-install routines *must* be “restart-aware:” that is, they *must* be able to run correctly whether it’s the first time they’re executed or whether it is the nth time through.

KIDS maintains a set of internal checkpoints during an installation. For each phase of the installation (for example, completion of each software application component), it uses a checkpoint to record whether that phase of the installation has completed yet. If an installation errors out, checkpointing allows the installation to be restarted, *not* from the very beginning, but instead only from the last completed checkpoint onward.

In your pre- and post-install routines, you can use your own checkpoints. If there is an error during the pre- or post-install, and you use checkpoints, when the sites restart the installation, it resumes from the last completed checkpoint rather than running through the entire pre- or post-install again.

Another advantage of using checkpoints is that you can record timing information for each phase of your pre- and post-install routines, which allows you to evaluate the efficiency of each phase you define.

There are two distinct types of checkpoints you can create during pre- and post-install routines:

- Checkpoints *with* callbacks
- Checkpoints *without* callbacks.

#### Checkpoints *with* Callbacks

The preferred method of using checkpoints is to use checkpoints with callbacks. When you create a checkpoint with a callback, you give the checkpoint an API (the callback routine). That is all you must do during your pre- or post-install routine, create a checkpoint with a callback. You do *not* have to execute the callback. At the completion of the pre- or post-install routine, KIDS manages the created checkpoints by calling, running, and completing the checkpoint and its callback routine.

The reason to let KIDS execute checkpoints (by creating checkpoints with callbacks) is to ensure that the pre-install or post-install runs in the same way whether it is the first installation pass, or if the installation aborted and has been restarted. If the installation has restarted, KIDS skips any checkpoints in the pre-install or post-install that have completed and only executes the callbacks of checkpoints that have *not* yet completed (and completes them).

In this scenario (checkpoints with callback routines), your pre-install and post-install routine should consist only of calls to the [\$\$NEWCP^XPDUTL(): Create Checkpoint](#newcpxpdutl-create-checkpoint) function to create checkpoints (with callbacks). Once you create all checkpoints for each discrete pre- or post-install task, the pre-install or post-install should quit.

Once the pre- or post-install routine finishes, KIDS executes each created checkpoint (that has a callback) in the order created. If it is the first time through, each checkpoint is executed. If the installation has been restarted, KIDS skips any completed checkpoints and only executes checkpoints that have *not* completed.

The KIDS checkpoint functions that apply when using checkpoints *with* callbacks are summarized in [Table 12](#_Ref62737377) (listed in alphabetic order):

| Function                                                        | Description                                                                                                                                                                                         |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [\$\$CURCP^XPDUTL](#curcpxpdutl-get-current-checkpoint-nameien) | Retrieve current checkpoint name (use during pre- or post-install routine). Useful when using the same tag^routine for multiple callbacks; this is how you determine in which callback you are. |
| [\$\$NEWCP^XPDUTL](#newcpxpdutl-create-checkpoint)              | Create checkpoint (use during pre- or post-install routine only.)                                                                                                                                   |
| [\$\$PARCP^XPDUTL](#parcpxpdutl-get-checkpoint-parameter)       | Retrieve checkpoint parameter (use within callback routine.)                                                                                                                                        |
| [\$\$UPCP^XPDUTL](#upcpxpdutl-update-checkpoint)                | Update checkpoint parameter (use within callback routine.)                                                                                                                                          |

<span id="_Ref503160270" class="anchor"></span>Table 13: KIDS—Functions Using Checkpoints *without* Callbacks

#### Checkpoint Parameter Node

You can store how far you have progressed with a task you are performing in the callback by using a checkpoint parameter node. The [\$\$UPCP^XPDUTL(): Update Checkpoint](#upcpxpdutl-update-checkpoint) function updates the value of a checkpoint’s parameter node; the [\$\$PARCP^XPDUTL(): Get Checkpoint Parameter](#parcpxpdutl-get-checkpoint-parameter) function retrieves the value of a checkpoint’s parameter node.

Being able to update and retrieve a parameter within a checkpoint can be quite useful. For example, if you are converting each entry in a file, as you progress through the file you can update the checkpoint’s parameter node with the Internal Entry Number (IEN) of each entry as you convert it. Then, if the conversion errors out and must be re-started, you can write your checkpoint callback in such a way that it always retrieves the last completed IEN stored in the checkpoint’s parameter node. Then, it can process entries in the file starting from the last completed IEN, rather than the first entry in the file. This is one example of how you can save the site time and avoid re-processing.

The pre-install API in the example in [Figure 27](#_Ref503160166) is PRE^ZZUSER2; the post-install API is POST^ZZUSER2.

<span id="_Ref503160166" class="anchor"></span>Figure 27: KIDS—Using Checkpoints *with* Callbacks: Combined Pre- and Post-install Routine

ZZUSER2 ;RON TEST 1.0 PRE AND POST INSTALL

;;1.0

;build checkpoints for PRE

PRE N %

S %=\$\$NEWCP^XPDUTL("ZZUSER1","PRE1^ZZUSER2","C-")

Q

PRE1 ;check terminal type file

N DA,UPDATE,NAME

;quit if answer NO to question 1

Q:'XPDQUES("PRE1")

S UPDATE=XPDQUES("PRE2")

;write message to user about task

D BMES^XPDUTL("Checking Terminal Type File")

;get parameter value to initialize NAME

S NAME=\$\$PARCP^XPDUTL("ZZUSER1")

F S NAME=\$O(^%ZIS(2,"B",NAME)) Q:\$E(NAME,1,2)'="C-" D

.S DA=+\$O(^%ZIS(2,"B",NAME,0))

.I DA,\$D(^%ZIS(2,DA,1)),\$P(^(1),U,5)\]"" D MES^XPDUTL(NAME\_" still has data in field 5") S:UPDATE \$P(^%ZIS(2,DA,1),U,5)=""

.;update parameter NAME

.S %=\$\$UPCP^XPDUTL("ZZUSER1",NAME)

Q

;build checkpoints for POST

POST N %

S %=\$\$NEWCP^XPDUTL("ZZUSER1","POST1^ZZUSER2")

S %=\$\$NEWCP^XPDUTL("ZZUSER2")

Q

POST1 ;check version multiple

N DA,VER,%

;quit if answer NO to question 1

Q:'XPDQUES("POST1")

;write message to user about task

D BMES^XPDUTL("Checking Package File")

;get parameter value to initialize DA

S DA=+\$\$PARCP^XPDUTL("ZZUSER1")

F S DA=\$O(^DIC(9.4,DA)) Q:'DA D

.S VER=+\$\$PARCP^XPDUTL("ZZUSER2")

.F S VER=\$O(^DIC(9.4,DA,22,VER)) Q:'VER D

..;here is where we could do something

..;update parameter VER

..S %=\$\$UPCP^XPDUTL("ZZUSER2",VER)

.;update parameter DA

.S %=\$\$UPCP^XPDUTL("ZZUSER1",DA),%=\$\$UPCP^XPDUTL("ZZUSER2",VER)

Q

#### Checkpoints *without* Callbacks (Data Storage)

KIDS ignores checkpoints that do *not* have callback routines specified. The ability to create checkpoints without a callback routine is provided mainly as a facility for developers to store information during the pre- or post-install routine. The parameter node of the checkpoint serves as the data storage mechanism. It is *not* safe to store important information in local variables during pre- or post-install routines, because installations can now be re-started in the middle; variables defined prior to the restart may no longer be defined after a restart.

An alternative use lets you expand the scope of checkpoints without callbacks beyond simply storing data. If you want to manage your own checkpoints instead of letting KIDS manage them, you can create checkpoints without callbacks but use them to divide your pre- and post-install routine into phases. Rather than having KIDS execute and complete them (as happens when the checkpoint has a callback routine), you would then be responsible for executing and completing the checkpoints. In this style of coding a pre- or a post-install routine, you would:

1.  Check if each checkpoint exists ([\$\$VERCP^XPDUTL(): Verify Checkpoint](#vercpxpdutl-verify-checkpoint)); if it does *not* exist, create it ([\$\$NEWCP^XPDUTL(): Create Checkpoint](#newcpxpdutl-create-checkpoint)).
8.  Retrieve the current checkpoint parameter as the starting point if you want to ([\$\$PARCP^XPDUTL(): Get Checkpoint Parameter](#parcpxpdutl-get-checkpoint-parameter)); do the work for the checkpoint; update the parameter node if you want to ([\$\$UPCP^XPDUTL(): Update Checkpoint](#upcpxpdutl-update-checkpoint)).
9.  Complete the checkpoint when the work is finished ([\$\$COMCP^XPDUTL(): Complete Checkpoint](#comcpxpdutl-complete-checkpoint)).
10. Proceed to the next checkpoint.

You must do more work this way than if you let KIDS manage the checkpoints (by creating the checkpoints *with* callback routines).

The KIDS checkpoint functions that apply when using checkpoints *without* callbacks are summarized in <u>Table 13</u> (listed in alphabetic order):

| Function                                                  | Description                                                                                    |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [\$\$COMCP^XPDUTL](#comcpxpdutl-complete-checkpoint)      | Complete checkpoint (use during pre- or post-install routine).                                 |
| [\$\$NEWCP^XPDUTL](#newcpxpdutl-create-checkpoint)        | Create checkpoint (use during pre- or post-install routine).                                   |
| [\$\$PARCP^XPDUTL](#parcpxpdutl-get-checkpoint-parameter) | Retrieve checkpoint parameter (use during pre-or post-install routine).                        |
| [\$\$UPCP^XPDUTL](#upcpxpdutl-update-checkpoint)          | Update checkpoint parameter (use during pre- or post-install routine).                         |
| [\$\$VERCP^XPDUTL](#vercpxpdutl-verify-checkpoint)        | Verify if checkpoint exists and if it has completed (use during pre- or post-install routine). |

<span id="_Ref454953738" class="anchor"></span>Table 14: KIDS—Required Builds Installation Actions

### Required Builds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the fourth screen of the Edit a Build \[XPD EDIT BUILD\] option, you can use the “Required Builds” section (that is REQUIRED BUILD \[#11\] Multiple) to enter other builds (that is software applications, or patches) that either warn the installer when they are missing or requires that they be installed before this build is installed. Make an entry in the BUILD (#9.6) file for those software applications or patches *not* installed using KIDS. Include the name and version number in the BUILD (#9.6) file entry.

![](kernel-8-0-developer-s-guide-kids-user-guide/023.png) REF: For the action types available, see [Table 14](#_Ref454953738).

At the installing site, KIDS checks the PACKAGE (#9.4) file, VERSION (#22) Multiple field, and PATCH APPLICATION HISTORY (#9.49,1105) Multiple field to verify that the required build has been installed at that site.

<span id="_Toc200270018" class="anchor"></span>Figure 28: KIDS—Required Builds Sample

Edit a Build <span class="mark">PAGE 4</span> OF 5

Name: TEST 1.0 TYPE: SINGLE PACKAGE

--------------------------------------------------------------------------

Install Questions

Required Builds

TEST 1.1 Don't install, remove global

Package File Link...: TEST

Track Package Nationally: NO

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

| Installation Action              | Description                                                                                                                                                                                                                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WARNING ONLY                 | Warns the installer the listed software application/patch is missing at the site but allows the installation to continue. (Displays a \*\*WARNING\*\* to the installer.)                                                                                                                 |
| DON’T INSTALL, LEAVE GLOBAL  | If the listed software application/patch is missing, this action prevents sites from continuing the installation. It does *not* unload the Transport Global. This allows sites to install the missing item and continue with the installation without having to reload the Transport Global. |
| DON’T INSTALL, REMOVE GLOBAL | If the listed software application/patch is missing, this action prevents sites from continuing the installation. It also unloads the Transport Global.                                                                                                                                      |

<span id="_Toc200270020" class="anchor"></span>Table 15: KIDS—National PACKAGE File Field Updates

### Package File Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the fourth screen of the Edit a Build option, you can link your build to an entry in the national PACKAGE (#9.4) file. Use this link if you want to update the site’s PACKAGE (#9.4) file when the software application you are creating is installed or if you want to use Kernel’s Alpha/Beta Testing module. You can only link to a PACKAGE (#9.4) file entry that is the same name (minus the version number) as the build you are creating.

If you specify a PACKAGE (#9.4) file entry in the PACKAGE FILE LINK field, and the installing site does *not* have a matching entry in their PACKAGE (#9.4) file, KIDS creates a new entry in the installing site’s PACKAGE (#9.4) file.

KIDS checks for duplicate version numbers and patch names when updating the PACKAGE (#9.4) file. When you link to an entry in the PACKAGE (#9.4) file, your installation automatically updates the VERSION (#22) Multiple field in the installing site’s corresponding PACKAGE (#9.4) file entry. KIDS makes a new entry in the VERSION (#22) Multiple field for the version of the software application you are installing. KIDS fills in the following fields in the new VERSION entry:

- VERSION (#22; Multiple \#9.49,.01)
- DATE DISTRIBUTED (#9.49,1)
- DATE INSTALLED AT THIS SITE (#9.49,2)
- INSTALLED BY (#9.49,3)
- DESCRIPTION OF ENHANCEMENTS (#9.49,41)
- PATCH APPLICATION HISTORY (#9.49,1105; Multiple \#9.4901)
- PATCH APPLICATION HISTORY (#9.4901,.01)
- DATE APPLIED (#9.4901,.02)
- APPLIED BY (#9.4901,.03)
- DESCRIPTION (#9.4901,1)

KIDS saves patch names along with their sequence numbers in the PATCH APPLICATION HISTORY (#9.49,1105) Multiple field.

![](kernel-8-0-developer-s-guide-kids-user-guide/024.png) NOTE: This functionality was added with Kernel Patch XU\*8.0\*30.

The Patch Application History sample ([Figure 29](#_Ref36449126)) shows a list of patch names with and without sequence numbers. Those patches without sequence numbers were entered prior to patch XU\*8.0\*30, since no sequence numbers are evident.

In addition, you can choose to update the following field at the top level of the National PACKAGE (#9.4) file:

| PACKAGE (#9.4) File Field Name | Description                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| AFFECTS RECORD MERGE (#20)     | (Multiple) Select files that, if merged, affect this software application. |

<span id="_Toc200270022" class="anchor"></span>Table 16: Alpha/Beta Tracking—KERNEL SYSTEM PARAMETERS (#8989.3) File Field Setup for KIDS

Beyond these fields, KIDS does *not* support maintaining any other information in the PACKAGE (#9.4) file.

<span id="_Ref36449126" class="anchor"></span>Figure 29: KIDS—Patch Application History Sample

Select PATCH APPLICATION HISTORY: 48// <span class="mark">? \<Enter\></span>

Answer with PATCH APPLICATION HISTORY

Choose from:

27

39

41

42

48

45 <span class="mark">SEQ \#41</span>

46 <span class="mark">SEQ \#42</span>

47 <span class="mark">SEQ \#43</span>

You may enter a new PATCH APPLICATION HISTORY, if you wish

Answer must be 8-15 characters in length.

Select PATCH APPLICATION HISTORY: 48// <span class="mark">\<Enter\></span>

PATCH APPLICATION HISTORY: 48// <span class="mark">\<Enter\></span>

DATE APPLIED: SEP 20,1996// <span class="mark">\<Enter\></span>

APPLIED BY: XUUSER,NINETY// <span class="mark">\<Enter\></span>

DESCRIPTION:

1\>This contains fixes related to output fixes for the PCMM software

2\>(distributed as SD\*5.3\*41).

3\>

4\>Both SD\*5.3\*41 and SD\*5.3\*45 must be installed prior to loading this

5\>patch.

### Track Package Nationally

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fourth screen of the Edit a Build option also lets you choose whether to send a message to the National PACKAGE (#9.4) file on FORUM, each time the software application is installed at a site. If you enter YES in the TRACK PACKAGE NATIONALLY field, KIDS sends a message to FORUM when a site installs the software application, provided the following conditions are met:

- The PACKAGE FILE LINK field in the build APIs to an entry in the PACKAGE (#9.4) file.
- The software application is installed at a site that is a primary VA domain.
- The software application is installed in a production UCI.

Answering NO to TRACK PACKAGE NATIONALLY (or leaving it blank) means that KIDS does *not* send a message to FORUM.

### Alpha/Beta Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides a mechanism for tracking and monitoring installation and option usage during the alpha and beta testing phases of VistA software applications. This tool is primarily intended for application developers to use in monitoring the testing process at local test sites.

![](kernel-8-0-developer-s-guide-kids-user-guide/025.png) NOTE: In VA terminology, “Alpha” and “Beta” testing are defined as follows:

- Alpha Testing—VistA test software application that is running in a Test account.
- Beta Testing—VistA test software application that is running in a Production account.

Alpha/Beta Tracking provides the following services to both developers and system administrators:

- Notification when a new alpha or beta software version is installed at a site.
- Periodic option usage reports for alpha or beta options being tracked.
- Periodic listings of errors in the software’s namespace that are currently in alpha or beta test at the site.

The Alpha/Beta Tracking of option usage is transparent to users. If the option counter is turned on, it records the number of times an option is invoked within the menu system when entered in the usual way by [^XUS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf#xus). Options are *not* counted when navigated past during menu jumping. Also, the counter is *not* set when entering the menu system with the developers [^XUP](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf#xup) utility.

Alpha/Beta tracking data is stored in the following Multiples in the KERNEL SYSTEM PARAMETERS (#8989.3) file, which is stored in the ^XTV global:

<table>
<caption><p><span id="_Toc200270023" class="anchor"></span>Table 17: Alpha/Beta Tracking—BUILD (#9.6) File Field Setup for KIDS</p></caption>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Alpha/Beta Tracking Fields:<br />
KERNEL SYSTEM PARAMETERS(#8989.3) File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALPHA/BETA TEST PACKAGE (#32) Multiple</td>
<td>This field stores the list of software namespaces that are currently in alpha or beta test at the site.</td>
</tr>
<tr class="even">
<td>ALPHA,BETA TEST OPTION (#33) Multiple</td>
<td>This field keeps a log of usage of the options associated with an alpha or beta test of VistA software based on the namespace indicated for the alpha or beta test software in the .ALPHA/BETA TEST PACKAGE (#32) Multiple field. This field stores <strong>POINTER</strong>s to entries in the OPTION (#19) file.</td>
</tr>
</tbody>
</table>

<span id="_Toc200270023" class="anchor"></span>Table 17: Alpha/Beta Tracking—BUILD (#9.6) File Field Setup for KIDS

If there are any entries in these Multiples, the menu system’s XQABTST variable is set, and the options are tracked.

Each time any subsequent test software is loaded, the current alpha/beta data is sent to the data tracker (such as developer), and the alpha/beta data is purged from all Multiples.

#### Initiating Alpha/Beta Tracking

To initiate and set up Alpha/Beta Tracking at a test site, developers should do the following:

1.  Create the build entry for the VistA software that is exported to sites.
11. Turn on Alpha/Beta Tracking—In the “Package File Link…” section in the fourth ScreenMan form of the build entry. Developers can turn on Alpha/Beta Tracking by entering YES at the “BUILD TRACK PACKAGE NATIONALLY:” prompt. ALPHA/BETA TESTING (#20) field in the BUILD (#9.6) file.
12. Edit THE BUILD file Entries—Highlight the software name and press the \<Enter\> key. KIDS places you in a ScreenMan form that lets you edit the following Alpha/Beta Tracking-related fields in the BUILD (#9.6) file.

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Alpha/Beta Tracking Fields:<br />
BUILD (#9.6) File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALPHA/BETA TESTING (#20)</td>
<td>This field initiates Alpha/Beta Tracking. Developers should enter <strong>YES</strong> in this field to activate Alpha/Beta Tracking.</td>
</tr>
<tr class="even">
<td>INSTALLATION MESSAGE (#21)</td>
<td>This field sends an installation message when the VistA software application is installed at a site. Developers should answer <strong>YES</strong> if you want the installation message sent to the mail group specified in the ADDRESS FOR USAGE REPORTING (#22) field in the BUILD (#9.6) file.</td>
</tr>
<tr class="odd">
<td>ADDRESS FOR USAGE REPORTING (#22)</td>
<td>This field should be set to the address of the VA MailMan mail group at the developer’s domain. This mail group address is where installation and option usage messages are sent by the Alpha/Beta Tracking code. Also, the domain specified in the address is where server requests are sent from the sites to report errors.</td>
</tr>
<tr class="even">
<td>PACKAGE NAMESPACE OR PREFIX (#23) field</td>
<td>This field is where you identify the alpha/beta VistA software application namespaces to be tracked.</td>
</tr>
</tbody>
</table>

![](kernel-8-0-developer-s-guide-kids-user-guide/026.png) NOTE: At Alpha/Beta Tracking termination, these fields in the BUILD (#9.6) file need to remain populated so the software code knows where to send the final report.

13. Set up the server option at the development domain. This option *must* be set up correctly—In order to track errors at test sites, make sure that the Handle Alpha/Beta Errors Logged at Sites \[XQAB ERROR LOG SERVER\] server option resides at your development site, which should be the domain specified in the ADDRESS FOR USAGE REPORTING (#22) field in the BUILD (#9.6) file for the software build entry.  
      
    This option processes server requests from the test sites, from the Errors Logged in Alpha/Beta Test (QUEUED) \[XQAB ERROR LOG XMIT\] option. The server stores the data from the requests into the XQAB ERRORS LOGGED (#8991.5) file.

![](kernel-8-0-developer-s-guide-kids-user-guide/027.png) REF: For more information on the Errors Logged in Alpha/Beta Test (Queued) \[XQAB ERROR LOG XMIT\] option, see the “[Error Tracking—Alpha/Beta Software Releases](#error-trackingalphabeta-software-releases)” section.

14. Schedule the Errors Logged in Alpha/Beta Test (Queued) \[XQAB ERROR LOG XMIT\] option to run at sites to gather errors and report these to the development server.

![](kernel-8-0-developer-s-guide-kids-user-guide/028.png) REF: For more information on the Errors Logged in the Alpha/Beta Test (Queued) option, see the “[Error Tracking—Alpha/Beta Software Releases](#error-trackingalphabeta-software-releases)” section.

15. Schedule the Send Alpha/Beta Usage to Programmers \[XQAB AUTO SEND\] option at the sites to send mail messages containing option usage.

![](kernel-8-0-developer-s-guide-kids-user-guide/029.png) REF: For more information on the Send Alpha/Beta Usage to Programmers option, see the “[Send Alpha/Beta Usage to Programmers Option](#send-alphabeta-usage-to-programmers-option)” section.

#### Error Tracking—Alpha/Beta Software Releases

As well as tracking option usage and installations, Kernel also lets developers track errors that occur in the namespace of the alpha- or beta-tracked software. To report these errors to developers, the site should schedule the Errors Logged in Alpha/Beta Test (QUEUED) \[XQAB ERROR LOG XMIT\] option. This option *cannot* be run directly; it is located on the ZTMQUEUABLE OPTIONS menu, which is *not* on any Kernel menu tree, as shown in [Figure 30](#_Ref499704237):

<span id="_Ref499704237" class="anchor"></span>Figure 30: KIDS—Errors Logged in Alpha/Beta Test (QUEUED) Option

ZTMQUEUABLE OPTIONS \[ZTMQUEUABLE OPTIONS\]

<span class="mark">Errors Logged in Alpha/Beta Test (QUEUED)</span> <span class="mark">\[XQAB ERROR LOG XMIT\]</span>

The Errors Logged in Alpha/Beta Test (QUEUED) \[XQAB ERROR LOG XMIT\] option identifies any errors associated with an application that is in either alpha or beta test. It collects error information and sends it to a server at the development domain. The developer may ask sites to schedule this option to run at a specified frequency, usually nightly. For example, developers can instruct test sites to schedule it as a task to run daily, after midnight.

The identified errors are combined in a mail message that includes the following information:

- Type of error
- Routine involved
- Date (usually the previous day)
- Option that was being used at the time of the error
- Number of times the error was logged
- Volume
- UCI

![](kernel-8-0-developer-s-guide-kids-user-guide/030.png) NOTE: The volume and UCI are included so that stations with error logs being maintained on different CPUs can run the task on each different system.

#### Monitoring Alpha/Beta Tracking

There are several options available to sites used to monitor the progress of alpha or beta testing. These options are located on the Alpha/Beta Test Option Usage Menu \[XQAB MENU\], which is located on the Operations Management \[XUSITEMGR\] menu:

<span id="_Toc179096463" class="anchor"></span>Figure 31: Alpha/Beta Test Option Usage Menu Options

<span class="mark">Operations Management ...</span> <span class="mark">\[XUSITEMGR\]</span>

<span class="mark">Alpha/Beta Test Option Usage Menu ...</span> <span class="mark">\[XQAB MENU\]</span>

Actual Usage of Alpha/Beta Test Options \[XQAB ACTUAL OPTION USAGE\]

Low Usage Alpha/Beta Test Options \[XQAB LIST LOW USAGE OPTS\]

Print Alpha/Beta Errors (Date/Site/Num/Rou/Err) \[XQAB ERR DATE/SITE/NUM/ROU/ERR\]

Send Alpha/Beta Usage to Programmers \[XQAB AUTO SEND\]

These options are described in the sections that follow.

#### Usage Report Options

To get usage reports during the software alpha/beta testing that is making use of the option counter, system administrators can review the tallies with the following options:

- Actual Usage of Alpha/Beta Test Options \[XQAB ACTUAL OPTION USAGE\]
- Low Usage Alpha/Beta Test Options \[XQAB LIST LOW USAGE OPTS\]

#### Actual Usage of Alpha/Beta Test Options Option

To get actual usage reports during the software alpha/beta testing that is making use of the option counter, system administrators can review the tallies with the Actual Usage of Alpha/Beta Test Options \[XQAB ACTUAL OPTION USAGE\] option. ADPACs may also be interested in being able to generate this information. <u>Figure 32</u> shows a printout of the actual usage of options within the XU namespace:

<span id="_Ref200252350" class="anchor"></span>Figure 32: Actual Usage of Alpha/Beta Test Options Option—Sample Option Usage Report

<span class="mark">OPTION USAGE SINCE 08-05-92</span>

XUSERINQ I 44 User Inquiry

XUUSERDISP R 49 Display User Characteristics

XUFILEACCESS M 50 File Access Management

XUSERBLK R 51 Grant Access by Profile

XUTIME A 53 Time

XUHALT A 71 Halt

XUMAINT M 83 Menu Management

XUSITEMGR M 86 Operations Management

XUSEREDITSELF R 87 Edit User Characteristics

XUSERTOOLS M 129 User's Toolbox

XUSEREDIT A 175 Edit an Existing User

XUPROG M 191 Programmer Options

XUSER M 265 User Edit

XUPROGMODE R 268 Programmer mode

#### Low Usage of Alpha/Beta Test Options Option

A similar report can be obtained of low usage options since the current version of the tracked software was installed, using the Low Usage of Alpha/Beta Test Options \[XQAB LIST LOW USAGE OPTS\] option.

#### Print Alpha/Beta Errors (Date/Site/Num/Rou/Err) Option

The Print Alpha/Beta Errors (Date/Site/Num/Rou/Err) \[XQAB ERR DATE/SITE/NUM/ROU/ERR\] option is used at the development domain, to print error information collected from sites. It does *not* report meaningful information when used at a site.

#### Send Alpha/Beta Usage to Programmers Option

At any time during software alpha/beta testing, system administrators can send an interim summary message back to the developers, with the Send Alpha/Beta Usage to Programmers \[XQAB AUTO SEND\] option.

To receive option usage reports, developers should instruct the sites to schedule this option to run at whatever frequency desired to receive option usage reports. It may be convenient to schedule this task to run, perhaps on a weekly basis; however, the developer may ask system administrators to schedule it to run at a different specified frequency. This option can also be run manually by the sites to send option usage information.

Mail messages are sent to the mail group and domain specified by the national application developer in the build entry for the ADDRESS FOR USAGE REPORTING (#22) field in the BUILD (#9.6) file when they exported the software.

![](kernel-8-0-developer-s-guide-kids-user-guide/031.png) NOTE: Developers/System Administrators, make sure that this mail group exists at the development domain!

#### Terminating Alpha/Beta Tracking

Alpha/Beta Tracking, once initiated for a VistA software application, *must* be turned off when the final version of the software application is released nationally (production). It is the developer’s responsibility to manually stop Alpha/Beta Tracking, terminate the audit, and purge the data when appropriate prior to national release. However, system administrators can also terminate Alpha/Beta Tracking at the local level:

- Local (Test) Software—Developer or system administrators is responsible for terminating Alpha/Beta Tracking at the local site.
- National (Production) Software—Developers are responsible for terminating Alpha/Beta Tracking for software that is released nationally.

Information stored during Alpha/Beta Tracking is purged each time a subsequent test version of the software is installed. A final summary report of option usage is prepared and sent to the developer’s mail group just before the purge.

#### Local (Test) Software Option Usage—Terminating Alpha/Beta Tracking

For *test* versions of the software application that is loaded locally (Test/Production accounts), it is the developer or system administrator’s responsibility to stop Alpha/Beta Tracking, terminate the audit, and purge the data from the KERNEL SYSTEM PARAMETERS (#8989.3) file when appropriate. There is no Kernel option to purge locally collected option counts; purge the data using a global KILL. If a subsequent software version release is another *test* version, Alpha/Beta Tracking is automatically re-initiated and tracking counts are reset back to Zero.

![](kernel-8-0-developer-s-guide-kids-user-guide/032.png) NOTE: If the ALPHA/BETA TESTING (#20) field is set to YES, any subsequent software version should be considered another test software version. If the ALPHA/BETA TESTING (#20) field is still set to NO, then the subsequent software version should be considered a production/release software version.

To manually stop Alpha/Beta Tracking at an individual site, developers or system administrators can use the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option located on the Kernel Management Menu \[XUKERNEL\] to remove the desired entries from the ALPHA/BETA TEST PACKAGE (#32) Multiple and ALPHA,BETA TEST OPTION (#33) Multiple field fields in the KERNEL SYSTEM PARAMETERS (#8989.3) file:

<span id="_Toc179096465" class="anchor"></span>Figure 33: Enter/Edit Kernel Site Parameters—Sample User Dialogue

> Select Kernel Management Menu Option: <span class="mark">ENTER/EDIT KERNEL SITE PARAMETERS \<Enter\></span>

> Note: the TaskMan site parameters have been moved out of this file.

> Use the Edit TaskMan Parameters option to edit those values.

> DEFAULT \# OF ATTEMPTS: 3// <span class="mark">^ALPHA BETA TEST PACKAGE \<Enter\></span>

> Select ALPHA/BETA TEST PACKAGE: ZZLOCAL// <span class="mark">@ \<Enter\></span>

> SURE YOU WANT TO DELETE THE ENTIRE ALPHA,BETA TEST PACKAGE? <span class="mark">Y \<Enter\></span>

> Select ALPHA/BETA TEST PACKAGE: <span class="mark">\<Enter\></span>

> Select ALPHA,BETA TEST OPTION: ZZSAMPLE// <span class="mark">@ \<Enter\></span>

> SURE YOU WANT TO DELETE THE ENTIRE ALPHA,BETA TEST OPTION? <span class="mark">Y \<Enter\></span>

#### National (Production) Software Option Usage—Terminating Alpha/Beta Tracking

For the final version of the software application that is to be released nationally (production), it is the developer’s responsibility to manually stop Alpha/Beta Tracking, terminate the audit, and purge the data from the local Test/Production accounts when appropriate *prior* to national release.

![](kernel-8-0-developer-s-guide-kids-user-guide/033.png) NOTE: For more information on how to terminate Alpha/Bea Tracking at local test sites, see the “[Local (Test) Software Option Usage—Terminating Alpha/Beta Tracking](#local-test-software-option-usageterminating-alphabeta-tracking)” section.

To *manually* stop Alpha/Beta Tracking of nationally released software, developers *must* enter NO in the ALPHA/BETA TESTING (#20) field in the BUILD (#9.6) file for the final build of the production software. When the sites install the build, Alpha/Beta Tracking is shut off.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Kernel Installation and Distribution System (KIDS) APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Function are described below.

![](kernel-8-0-developer-s-guide-kids-user-guide/034.png) NOTE: For all output during pre- and post-installs, use the [MES^XPDUTL(): Output a Message](#mesxpdutl-output-a-message) and [BMES^XPDUTL(): Output a Message with Blank Line](#bmesxpdutl-output-a-message-with-blank-line) APIs. These functions WRITE output to both the INSTALL (#9.7) file and the output device.

## UPDATE^XPDID(): Update Install Progress Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 2172

Description: The UPDATE^XPDID API updates the progress bar to show the percentage complete for the installation of the current number of items specified (that is n input parameter).

Format: UPDATE^XPDID(n)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
16. Set all input variables.
17. Call the API.

Input Variables: XPDIDTOT: (required) This variable is the total number of items that are being updated.

Input Parameters: n: (required) The current number of items being updated.

Output: none.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are converting 100 records and want to update the user every time you have completed 10% of the records you will do the following:

<span id="_Toc199950630" class="anchor"></span>Figure 34: UPDATE^XPDID API—Example

\><span class="mark">Set XPDIDTOT=100</span>

\><span class="mark">F%=1:1:100 D CONVERT I'(%#10) D UPDATE^XPDID(%)</span>

## EN^XPDIJ(): Task Off KIDS Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: KIDS

ICR \#: 2243

Description: The EN^XPDIJ API can be used with XPDA and is defined to task off a KIDS install. This is useful if a large conversion needs to run in the background while users are back on the system. For example, the first KIDS build can install a new version of software, then task off a second cleanup/conversion build. This allows users back onto the system, because the new version install completes and unlocks options and protocols. Meanwhile, the cleanup runs in the background under KIDS and makes use of KIDS checkpoints, restart upon failure, and message logging that can later be accessed in the Install File Print.

Format: EN^XPDIJ(xpda)

Input Parameters: xpda: (required) Internal entry number of the build to be tasked in the INSTALL (#9.7) file.

Output: none.

## \$\$PKGPAT^XPDIP(): Update Patch History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 2067

Description: The \$\$PKGPAT^XPDIP extrinsic function updates the PATCH APPLICATION HISTORY (#9.49,1105) Multiple field of the VERSION (#22) Multiple field in the PACKAGE (#9.4) file. This function can be used during the Pre- or Post-Install routine.

Format: \$\$PKGPAT^XPDIP(package_ien,version,.x)

Input Parameters: package_ien: (required) The software file entry Internal Entry Number (IEN) in the PACKAGE (#9.4) file.

version: (required) This is the software version number. The version number *must* contain a decimal (such as 8.0).

.x: (required) This parameter is required.

Output: returns: Returns:

version ien^patch ien

## \$\$PKGVER^XPDIP(): Update Patch Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 2067

Description: The \$\$PKGVER^XPDIP extrinsic function updates the VERSION (#22) Multiple field in the PACKAGE (#9.4) file. This function can be used during the Pre- or Post-Install routine.

Format: \$\$PKGPAT^XPDIP(package_ien,\[.\]version)

Input Parameters: package_ien: (required) The software file entry Internal Entry Number (IEN) in the PACKAGE (#9.4) file.

\[.\]version: (required) This can be either a string or an array. If it is an array, then it *must* be passed by reference.

- version =version number^date distributed^date installed^installed by user ien
- version(1) = closed global root of the location of the description \[such as ^XTMP(\$J,““WP””)\].

All date values *must* be in internal VA FileMan date format.

The version number *must* contain a decimal (such as 8.0).

Output: returns: Returns:

version ien

## BMES^XPDUTL(): Output a Message with Blank Line

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The BMES^XPDUTL API outputs a message string to the installation device during KIDS installations. A message is also recorded in the INSTALL (#9.7) file entry for the installation. It is like the [MES^XPDUTL(): Output a Message](#mesxpdutl-output-a-message) API, except that it outputs a blank line before it outputs the message, and it does *not* take arrays.

Format: BMES^XPDUTL(msg)

Input Parameters: msg: (required) String to output.

Output: returns: Returns a message string preceded by a blank line to the installation device.

## \$\$COMCP^XPDUTL(): Complete Checkpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$COMCP^XPDUTL extrinsic function completes a checkpoint, in pre- or post-install routines during KIDS installations. Use this only to complete checkpoints that do *not* have callback routines. If the checkpoint has a callback routine, KIDS itself completes the checkpoint. You can only complete checkpoints that are for the same installation phase (pre-install or post-install) that you are currently in.

Use this API only for checkpoints with no callback. KIDS completes checkpoints that have a callback.

Format: \$\$COMCP^XPDUTL(name)

Input Parameters: name: (required) Checkpoint name.

Output: returns: Returns:

- 1—Successfully completed checkpoint.
- 0—Error completing checkpoint.

## \$\$CURCP^XPDUTL(): Get Current Checkpoint Name/IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$CURCP^XPDUTL extrinsic function returns the name of the current checkpoint during KIDS installations. It can be useful if, for example, you use the same tag^routine API for more than one callback. Using this function, you can determine which callback you are in.

Use this API only for checkpoints *with* a callback. It returns the NULL string if you call it when working with a checkpoint with no callback (in which case, you would really be in either the pre- or post-install routine).

Format: \$\$CURCP^XPDUTL(format)

Input Parameters: format: (required) Pass as follows:

- Zero (0)—To return checkpoint name.
- 1—To return checkpoint Internal Entry Number (IEN).

Output: returns: Returns:

- Checkpoint Name—The current checkpoint name.
- NULL String—If *not* currently in a checkpoint callback.

## \$\$INSTALDT^XPDUTL(): Return All Install Dates/Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$INSTALDT^XPDUT extrinsic function retrieves all dates/times that an install was performed for a given install name in the INSTALL (#9.7) file. It returns the results in an array.

![](kernel-8-0-developer-s-guide-kids-user-guide/035.png) NOTE: This API was released with Kernel Patch XU\*8.0\*491.

Format: \$\$INSTALDT^XPDUTL(install,.result)

Input Parameters: install: (required) Name of install in the INSTALL (#9.7) file.

.result: (required) Passed by reference, the name of the array to return values.

Output Parameters: .result: Returns the number of records in the result array:

- result=number of records.
- result(internal DATE/TIME)=“TEST#^SEQ#” (Fields 61^62 from INSTALL \[#9.7\] file).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950631" class="anchor"></span>Figure 35: \$\$INSTALDT^XPDUTL API—Example

\><span class="mark">W \$\$INSTALDT^XPDUTL("XU\*8.0\*491", .RSLT)</span>

1

\><span class="mark">ZW RSLT</span>

RSLT=1

RSLT(3080318.092151)="1^"

## \$\$LAST^XPDUTL(): Last Software Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$LAST^XPDUTL extrinsic function returns the last patch and the date it was applied to the software. The patch also includes the Sequence \# if the last patch was a released patch.

![](kernel-8-0-developer-s-guide-kids-user-guide/036.png) NOTE: This API can be used outside of KIDS.

Format: \$\$LAST^XPDUTL(x\[,y\]\[,z\])

Input Parameters: x: (required) Software name or software namespace within quotes (such as “KERNEL” or “XU”).

y: (optional) Full software version number with decimal point entered within quotes (such as “8.0”). The current version is assumed if this parameter is *not* supplied.

z: (optional) This parameter was added with Kernel Patch XU\*8.0\*559. If set to 1, then only the last *released* patch information is returned.

Output: returns: Returns the last patch information in a caret-delimited string:

- *nnn*^*yyymmdd*—Unreleased patch; where “*nnn*” = patch number and “*yyymmdd*” = date in VA FileMan format.
- *nnn* Seq \#*nnn*^*yyymmdd*—Released patch; where “*nnn*” = patch number, “Seq \#*nnn*” = sequence number for released patch, and “*yyymmdd*” = date in VA FileMan format.
- -1—If either the software or version does *not* exist, or no patches have been applied.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950632" class="anchor"></span>Figure 36: \$\$LAST^XPDUTL API—Example 1

\><span class="mark">S X="KERNEL"</span>

\><span class="mark">S Y="8.0"</span>

\><span class="mark">W \$\$LAST^XPDUTL(X,Y)</span>

543^3110503

#### Example 2

<span id="_Toc199950633" class="anchor"></span>Figure 37: \$\$LAST^XPDUTL API—Example 2

\><span class="mark">S X="KERNEL"</span>

\><span class="mark">S Y="8.0"</span>

\><span class="mark">S Z=1</span>

\><span class="mark">W \$\$LAST^XPDUTL(X,Y,Z)</span>

431 SEQ \#453^3110425.122831

#### Example 3

<span id="_Toc199950634" class="anchor"></span>Figure 38: \$\$LAST^XPDUTL API—Example 3

\><span class="mark">S X="KERNEL"</span>

\><span class="mark">S Y="9.0"</span>

\><span class="mark">S Z=1</span>

\><span class="mark">W \$\$LAST^XPDUTL(X,Y,Z)</span>

-1

For this example, since there is no Kernel 9.0 the expected result is -1.

## MES^XPDUTL(): Output a Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The MES^XPDUTL API outputs a message string to the installation device during KIDS installations. A message is also recorded in INSTALL (#9.7) file entry for the installation.

Format: MES^XPDUTL(\[.\]msg)

Input Parameters: \[.\]msg: (required) Message string to output, either in a variable or passed by reference as an array of strings.

Output: returns: Returns a message string to the installation device.

## \$\$NEWCP^XPDUTL(): Create Checkpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$NEWCP^XPDUTL extrinsic function creates a checkpoint in pre- or post-install routines during KIDS installations. The checkpoint is stored in the INSTALL (#9.7) file.

Pre-and post-install checkpoints are stored separately, so you can use the same name for a pre- and post-install checkpoint if you wish:

- Checkpoints created with this function from the pre-install routine are pre-install checkpoints.
- Checkpoints created during the post-install routine are post-install checkpoints.

You can use \$\$NEWCP^XPDUTL to create a checkpoint with or without a callback. You can also store a value for the parameter node, if you wish.

Checkpoints created with callbacks have that callback automatically executed by KIDS during the appropriate phase of the installation:

- If the checkpoint is created during the pre-install routine, KIDS executes the callback as soon as the pre-install routine completes.
- If the callback is created during the post-install, KIDS executes the callback as soon as the post-install routine completes.
- If multiple checkpoints are created during the pre- or post-install routine, KIDS executes the callbacks (and completes the checkpoints) in the order the corresponding checkpoints were created.

Checkpoints created without a callback *cannot* be executed by KIDS; instead, they provide a way for developers to store and retrieve information during the pre-install and post-install phases. Rather than storing information in a local or global variable, you can store information in a checkpoint parameter node and retrieve it (even if an installation is re-started).

If the checkpoint you are trying to create already exists, the original parameter and callback is *not* overwritten.

Format: \$\$NEWCP^XPDUTL(name\[,callback\]\[,par_value\])

Input Parameters: name: (required) Checkpoint name.

callback: (optional) Callback (^routine or tag^routine reference).

par_value: (optional) Value to which the checkpoint parameter is set.

Output: returns: Returns:

- Internal Entry Number (IEN)—Created checkpoint if newly created or if checkpoint already exists.
- Zero (0)—Error occurred while creating checkpoint.

## \$\$OPTDE^XPDUTL(): Disable/Enable an Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$OPTDE^XPDUTL extrinsic function is used during KIDS installations in a Pre-Init or Post-Init routine. Use this function to disable or enable an option.

Format: \$\$OPTDE^XPDUTL(name,action)

Input Parameters: name: (required) Option name.

action: (required) Set to:

- 1—Enable an option.
- 0—Disable an option.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950635" class="anchor"></span>Figure 39: \$\$OPTDE^XPDUTL API—Example

I \$\$OPTDE^XPDUTL("XMUSER",0) W !,'Option Disabled.'

## \$\$PARCP^XPDUTL(): Get Checkpoint Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$PARCP^XPDUTL extrinsic function retrieves the current value of a checkpoint’s stored parameter during KIDS installations. The parameter is stored in the INSTALL (#9.7) file.

Use this API for checkpoints both with and without callbacks.

Use the optional second parameter to retrieve a pre-install checkpoint’s parameter during a post-install.

Format: \$\$PARCP^XPDUTL(name\[,pre\])

Input Parameters: name: (required) Checkpoint name.

pre: (optional) To retrieve a parameter from a pre-install checkpoint while in the post-install, set this parameter to PRE.

Output: returns: Returns the current parameter node for the checkpoint named in the name input parameter.

## \$\$PATCH^XPDUTL(): Verify Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$PATCH^XPDUTL extrinsic function is used during KIDS installations, during the environment check only. Use this function to verify if a patch has been installed. You can check for patches with or without sequence numbers.

Format: \$\$PATCH^XPDUTL(patch)

Input Parameters: patch: (required) Patch name. Patch name *must* include the full version number with the decimal point, such as XU\*<span class="mark">8.0</span>\*28.

Output: returns: Returns:

- 1—Specified patch was installed on the current system.
- 0—Specified patch was *not* installed on the current system.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Checking for a patch installation. Enter the following at the Programmer prompt:

<span id="_Toc199950636" class="anchor"></span>Figure 40: \$\$PATCH^XPDUTL API—Example

\>I '\$\$PATCH^XPDUTL("XU\*8.0\*28") W !,"You must install patch XU\*8\*28"

## \$\$PKG^XPDUTL(): Parse Software Name from Build Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$PKG^XPDUTL extrinsic function parses the name of a software application from a software application’s build name. You can obtain the name of the build KIDS is installing from the KIDS key variable XPDNM, which is defined throughout a KIDS installation.

Format: \$\$PKG^XPDUTL(buildname)

Input Parameters: buildname: Name of build (.01 field of BUILD \[#9.6\] file).

Output: returns: Returns the software name.

## \$\$PRODE^XPDUTL(): Disable/Enable a Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$PRODE^XPDUTL extrinsic function is used in a Pre-Init or Post-Init routine during KIDS installations. Use this function to disable or enable a protocol.

Format: \$\$PRODE^XPDUTL(name,action)

Input Parameters: name: (required) Protocol name.

action: (required) Enter one of the following values for this parameter:

- 1—Enable a protocol.
- 2—Disable a protocol.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

## \$\$RTNUP^XPDUTL(): Update Routine Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$RTNUP^XPDUTL extrinsic function updates the installation action for a routine during KIDS installations, during the environment check only.

Format: \$\$RTNUP^XPDUTL(routine,action)

Input Parameters: routine: (required) Routine name.

action: (required) Enter one of the following values for this parameter:

- 1—Delete at site.
- 2—Skip installing at site.

Output: returns: Returns:

- 1—Routine found in routine installation list.
- 0—Routine *not* found in routine installation list.

## \$\$UPCP^XPDUTL(): Update Checkpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$UPCP^XPDUTL extrinsic function updates the parameter node of an existing checkpoint, in pre- or post-install routines during KIDS installations. The parameter node is stored in the INSTALL (#9.7) file.

Use this API for checkpoints both with and without callbacks.

During the pre-install, you can only update pre-install checkpoints; during the post-install, you can only update post-install checkpoints.

Format: \$\$UPCP^XPDUTL(name\[,par_value\])

Input Parameters: name: (required) Checkpoint name.

par_value: (optional) Sets checkpoint parameter to this value.

Output: returns: Returns:

- Internal Entry Number (IEN)—Successfully updated checkpoint.
- Zero (0)—Error updating checkpoint.

## \$\$VER^XPDUTL(): Parse Version from Build Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$VER^XPDUTL extrinsic function parses the version of a software application from a software application’s build name. You can obtain the name of the build KIDS is installing from the KIDS key variable XPDNM, which is defined throughout a KIDS installation.

Format: \$\$VER^XPDUTL(buildname)

Input Parameters: buildname: (required) Name of build (.01 field of BUILD \[#9.6\] file).

Output: returns: Returns:

- Version—The version of the build identified in the buildname input parameter.
- NULL—If no match in the BUILD (#9.6) file.

## \$\$VERCP^XPDUTL(): Verify Checkpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$VERCP^XPDUTL extrinsic function checks whether a given checkpoint exists and, if it exists, whether it has completed or *not* during KIDS installations.

Use this API only for checkpoints with no callback.

During the pre-install, you can only verify pre-install checkpoints; during the post-install, you can only verify post-install checkpoints.

Format: \$\$VERCP^XPDUTL(name)

Input Parameters: name: (required) Checkpoint name.

Output: returns: Returns:

- 1—Checkpoint has completed.
- 0—Checkpoint has *not* completed but exists.
- -1—Checkpoint does *not* exist.

## \$\$VERSION^XPDUTL(): Package File Current Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: KIDS

ICR \#: 10141

Description: The \$\$VERSION^XPDUTL extrinsic function obtains the current version of a site’s software application.

Format: \$\$VERSION^XPDUTL(package_id)

Input Parameters: package_id: (required) Software application’s name or namespace, from its entry in the PACKAGE (#9.4) file.

Output: returns: Returns:

- Version—The current version of the software application at the site, according to the software application’s entry in the site’s PACKAGE (#9.4) file.
- NULL—If the software application is *not* matched.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-kids-user-guide/037.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-kids-user-guide/038.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-kids-user-guide/039.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.