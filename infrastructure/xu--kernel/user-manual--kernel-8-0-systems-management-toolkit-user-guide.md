---
title: "Kernel 8.0 Systems Management: Toolkit User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: Toolkit"
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
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - class
  - parameter
  - mark
  - local
  - lookup
  - table
  - contents
  - tools
  - term
page_count: 0
word_count: 11665
section_count: 14
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Toolkit User Guide
---

![](kernel-8-0-systems-management-toolkit-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-toolkit-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref477871111" class="anchor"></span>Table 1: Parameter Entities</p></caption>
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
<td>08/31/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Toolkit User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref477871111" class="anchor"></span>Table 1: Parameter Entities

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="List_of_Figures" class="anchor"></span>List of Figures

<span id="List_of_Tables" class="anchor"></span>List of Tables

[Table 1: Parameter Entities [35](#_Ref477871111)](#_Ref477871111)

[Table 2: Templates—Parameter Tools [38](#_Ref477871593)](#_Ref477871593)

<span id="_Hlt412359042" class="anchor"></span>Orientation

How to Use this Manual

![](kernel-8-0-systems-management-toolkit-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Multi-Term Look-Up (MTLU)](#multi-term-look-up-mtlu)
  - [MTLU Overview](#mtlu-overview)
  - [Introduction to Multi-Term Look-Up (MTLU)](#introduction-to-multi-term-look-up-mtlu)
  - [Functional Description](#functional-description)
  - [Usage Considerations](#usage-considerations)
  - [MTLU User Interface](#mtlu-user-interface)
    - [Multi-Term Look-Up Menu Options](#multi-term-look-up-menu-options)
    - [Using the Multi-Term Lookup (MTLU) Option](#using-the-multi-term-lookup-mtlu-option)
    - [Using the Print Utility Option](#using-the-print-utility-option)
    - [Using the Utilities for MTLU Option](#using-the-utilities-for-mtlu-option)
    - [MTLU Examples](#mtlu-examples)
  - [MTLU Systems Management](#mtlu-systems-management)
    - [Implementation of Multi-Term Look-Up (MTLU)](#implementation-of-multi-term-look-up-mtlu)
- [Parameter Tools](#parameter-tools)
  - [Parameter Tools Introduction](#parameter-tools-introduction)
  - [Parameter Tools Background](#parameter-tools-background)
  - [Parameter Tools Description](#parameter-tools-description)
  - [Parameter Tools Definitions](#parameter-tools-definitions)
    - [Entity](#entity)
    - [Parameter](#parameter)
    - [Instance](#instance)
    - [Value](#value)
    - [Parameter Template](#parameter-template)
  - [Why Use Parameter Tools?](#why-use-parameter-tools)
  - [General Parameter Tools Menu](#general-parameter-tools-menu)
    - [List Values for a Selected Parameter Option](#list-values-for-a-selected-parameter-option)
    - [List Values for a Selected Entity Option](#list-values-for-a-selected-entity-option)
    - [List Values for a Selected Package Option](#list-values-for-a-selected-package-option)
    - [List Values for a Selected Template Option](#list-values-for-a-selected-template-option)
    - [Edit Parameter Values Option](#edit-parameter-values-option)
    - [Edit Parameter Values with Template Option](#edit-parameter-values-with-template-option)
    - [Edit Parameter Definition Keyword Option](#edit-parameter-definition-keyword-option)
  - [Parameter Tools Example](#parameter-tools-example)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Toolkit User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. This section provides descriptive information about the set of software utilities furnished by Kernel Version 8.0 and Kernel Toolkit Version 7.3 (aka “Toolkit”), describing how these tools can be used for the management and definition of development projects.
The major areas of the Kernel Toolkit described in this section are listed below:
- [Multi-Term Look-Up (MTLU)](#multi-term-look-up-mtlu):
Multi-Term Look-Up (MTLU) utilities provide a method of enhancing the lookup capabilities of associated VA FileMan files. Multi-Term Look-Up (MTLU) is an adaptation of a tool developed by the Indian Health Service (IHS), which was originally made generic by the Albany Office of Information Field Office (OIFO). MTLU does the following:
- Tests ICD diagnosis and procedure codes, CPT codes, and other commonly used references that have been entered in the LOCAL LOOKUP (#8984.4) file. Optionally, terms or phrases can be entered into the LOCAL KEYWORD (#8984.1), LOCAL SHORTCUT (#8984.2), or LOCAL SYNONYM (#8984.3) files.
- Prints a list of shortcuts, keywords, or synonyms from a specified reference file in the LOCAL LOOKUP (#8984.4) file.
- Adds or deletes a reference file from a site’s LOCAL LOOKUP (#8984.4) file.
- Enters new or edit existing shortcuts, keywords, or synonyms to the LOCAL LOOKUP (#8984.4) file.
- Routine Tools:
Routine Tools provide a set of generic tools to aid the VistA development community and system administrators in analysis, writing, and testing of code. These tools are used by VistA developers to support distinct tasks. Routine Tools do the following:
- Promote standard program interfaces.
- Check adherence to programming standards and correct syntax with the XINDEX utility.
- Provide standard error trapping, storing, and reporting.
- Customize and tunes site parameters for local requirements.
- Provide M function libraries.
- Provide a portable routine and global editor.
- Provide a Kermit file transfer utility.
- Provide a Multi-Term Look-Up (MTLU) utility for enhanced VA FileMan lookups.
- Provide software project management utilities.
- Verification Tools:
Verification Tools are a set of generic tools to aid the VistA development community and system administrators in reviewing M code. These tools are used by VistA developers to support distinct tasks. Verification Tools provide the following:
- Tools used for comparison of routines and data dictionaries.
- A tool used to record routine text indicated in the file used to maintain changes in routines.
Where applicable, each major area of Kernel Toolkit is described first in terms of its user interface then in terms of system management implications, showing the menu that can be used to accomplish the task at hand.
![](kernel-8-0-systems-management-toolkit-user-guide/004.png) REF: Kernel and Kernel Toolkit Application Programming Interfaces (APIs) are documented in the [*Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet Website.
![](kernel-8-0-systems-management-toolkit-user-guide/005.png) NOTE: The *Parameter Tools Supplement to Patch Description (Patch XT\*7.3\*26)* explains the functions available with the use of the Parameter Tools, provides information on the Kernel PARAMETERS (#8989.5) file, and describes the associated Application Programming Interfaces (APIs).
![](kernel-8-0-systems-management-toolkit-user-guide/006.png) REF: This documentation can be downloaded from the VA Software Document Library (VDL) at: [VDL Kernel Toolkit Application Documents](http://www.va.gov/vdl/application.asp?appID=12)
The following Kernel Toolkit sections were removed from this guide, because they are superseded by subsequent software and documentation changes:
- Duplicate Record Merge:
The Kernel Toolkit “Duplicate Record Merge” documentation is superseded by the *Duplicate Record Merge: Patient Merge* software/documentation (that is Kernel Toolkit patch XT\*7.3\*23).
The Duplicate Record Merge functionality provides a developer Merge Shell with options that allow users to check data files for duplicate entries and merge those entries if any are found. These options provide functionality to combine duplicate records based on conditions established in customized applications. The Merge Shell was originally developed by Indian Health Service (IHS) to support their Multi-Facility Integration Project.
![](kernel-8-0-systems-management-toolkit-user-guide/007.png) REF: For instructions on how to build a merge capability for a file, see the “Toolkit—Developing a File Merge Capability” section in the [*Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf) available on the VA Software Document Library (VDL) at: [VDL Kernel Application Documents](http://www.va.gov/vdl/application.asp?appid=10).
![](kernel-8-0-systems-management-toolkit-user-guide/008.png) REF: The *Duplicate Record Merge: Patient Merge* documentation is available on the VDL at: [VDL Duplicate Record Merge: Patient Merge Application Documents](http://www.va.gov/vdl/application.asp?appid=2).
- Capacity Management:
The Kernel Toolkit “Capacity Management” documentation is superseded by the following software/documentation:
- Capacity Management (CM) Tools 3.0
- Resource Usage Monitor (RUM) 2.0
- Statistical Analysis of Global Growth (SAGG) 2.0
- VistA System Monitor (VSM) 4.0
![](kernel-8-0-systems-management-toolkit-user-guide/009.png) REF: The Capacity Management-related documentation is available on the VDL at:
- Capacity Management (CM) Tools: [VDL CM Tools Application Documents](http://www.va.gov/vdl/application.asp?appid=129)
- Resource Usage Monitor (RUM): [VDL RUM Application Documents](http://www.va.gov/vdl/application.asp?appid=130)
- Statistical Analysis of Global Growth (SAGG): [VDL SAGG Application Documents](http://www.va.gov/vdl/application.asp?appid=115)
- VistA System Monitor (VSM): [VDL VSM Application Documents](https://www.va.gov/vdl/application.asp?appid=218)
Kernel Toolkit Patch XT\*7.3\*102 removed all options, routines, and files associated with the following menus and options:
- VPM VAX/ALPHA Capacity Management
- Move Host File to Mailman \[XTCM DISK2MAIL\]
- Response Time Log Options
The following namespace options and routines were also removed:
- XUCM\*
- XUCS\*
- XURTL\*
- XTCM DISK2MAIL (option)
- XTCMXTCMFILN (routine)
Data dictionaries and data have been deleted for the following VA FileMan compatible files:
- Global ^XUCM:
  - CM DAILY STATISTICS (#8986.6)
  - CM DISK DRIVE RAW DATA (#8986.5)
  - CM METRICS (#8986.4)
  - CM NODENAME RAW DATA (#8986.51)
  - CM SITE DISKDRIVES (#8986.35)
  - CM SITE NODENAMES (#8986.3)
  - CM SITE PARAMETERS (#8986.095)
  - VPM RESPONSE TIME DATA (#8986.098)
- Global ^%ZRTL:
  - RESPONSE TIME (#3.091)
  - RT DATE_UCI,VOL (#3.092)
  - RT RAWDATA (#3.094)
Data has been deleted for the following *non*-VA FileMan compatible global:
- ^%ZRTL(3)
- ^%ZRTL(“RTH”)
![](kernel-8-0-systems-management-toolkit-user-guide/010.png) NOTE: System Managers: The ^XUCM and %ZRTL globals can be removed from your database after installation of Patch XT\*7.3\*10; however, please make sure no local routines access these globals before doing so.

# Multi-Term Look-Up (MTLU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## MTLU Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains an introduction and functional description, site implementation instructions for Multi-Term Look-Up (MTLU), and the option documentation.

## Introduction to Multi-Term Look-Up (MTLU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many medical information systems depend on the standardized encoding of diagnoses and procedures for reports, searches, and statistics. The ICD DIAGNOSIS (#80), ICD OPERATION/PROCEDURE (#80.1), and CPT (#81) files are among some of the more critical files. The Multi-Term Look-Up utility increases the accessibility of the information in these files by associating user-supplied words or phrases with terms found in a more descriptive, free-text field.

Multi-Term Look-Up allows:

- Local setup of virtually any reference file.
- Modification of the behavior of the “special” lookup by defining shortcuts, synonyms, or keywords.

MTLU integrates with any software that uses a reference file that has been entered into a site’s LOCAL LOOKUP (#8984.4) file.

## Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multi-Term Look-Up (MTLU) utility provides a method of enhancing the lookup capabilities of associated software applications. This utility is comprised of the following options:

- Multi-Term Lookup (MTLU) \[XTLKLKUP\] option—Used to test ICD diagnosis and procedure codes, CPT codes, and other commonly used references that have been entered in the LOCAL LOOKUP (#8984.4) file. Optionally, terms or phrases may be entered into the LOCAL KEYWORD (#8984.1), LOCAL SHORTCUT (#8984.2), or LOCAL SYNONYM (#8984.3), files.
- Print Utility \[XTLKPRTUTL\] option—Used to print a list of shortcuts, keywords, or synonyms from a specified reference file in the LOCAL LOOKUP (#8984.4) file. This list can be sorted alphabetically by name or numerically by code.
- Delete Entries from Look-Up \[XTLKMODPARK\] option—Used to delete a reference file from a site’s LOCAL LOOKUP (#8984.4) file. This option should be used as a system administrator/developer utility and can only be accessed by holders of the XTLKZMGR security key.
- Add Entries To Look-Up File \[XTLKMODPARS\] option—Used to add reference files to a site’s LOCAL LOOKUP (#8984.4) file. This option should be used as a system administrator/developer utility and can only be accessed by holders of the XTLKZMGR security key. To add entries with this option, DUZ(0) *must* be set to an at-sign (@; Programmer access).
- Add/Modify Utility \[XTLKMODUTL\] option—Used to enter new or edit existing shortcuts, keywords, or synonyms to the LOCAL LOOKUP (#8984.4) file as described below:
  - Shortcuts \[XTLKMODSH\] option—Used to enter new or edit existing shortcuts to the LOCAL LOOKUP (#8984.4) file.
  - Keywords \[XTLKMODKY\] option—Used to enter new or edit existing keywords to the LOCAL LOOKUP (#8984.4) file.
  - Synonyms \[XTLKMODSY\] option—Used to enter new or edit existing synonyms to the LOCAL LOOKUP (#8984.4) file.

## Usage Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MTLU provides users and developers with the ability to perform specialized lookups on database files using standard VA FileMan calls. These files typically comprise a number or “term” in the .01 field and a longer description or definition in some other field.

In the simplest application of MTLU, a special lookup XTLKDICL routine is defined in the file’s data dictionary (DD), then a MUMPS cross-reference is applied to the description/definition field. Options are available to fully configure a file for use with MTLU. FileMan is used to create/build the cross-reference. To set the cross-reference, text from the selected field is passed to a tokenizing XTLKTOKN routine. Trivial words are filtered by an expanded Key Word In Context (KWIC), and then each remaining token is added to the cross-reference.

To request a lookup, users and developers can pass in words or phrases. Their input is similarly tokenized. However, only terms associated with *all* tokens entered are found. Input can be generalized using partial words or fewer words as well as lexical variants. For example, using the VA FileMan Inquire to File Entries \[DIINQUIRE\] option on the ICD DIAGNOSIS (#80) file one could first enter “MALIG”. MTLU informs the user which terms apply to the search, “MALIG/MALIGNANT”, and that 447 matches are found. To be more specific, the user might enter “MALIG LIP” to request all malignancies associated with the lip. In this case, only 12 matches are found. The user can further screen searches by using the grave accent “Not-Sign” (\`) before a word or phrase. To request all malignancies of the lip *except* those of the lower lip, one could enter “MALIG LIP ‘LOWER” and obtain 10 matches. Though the term “malignancies” may *not* exist in the lookup file, MTLU might still produce a match. When a term contains a suffix that does *not* produce a match, MTLU removes the suffix and continues the search.

![](kernel-8-0-systems-management-toolkit-user-guide/011.png) REF: For more information on the Inquire to File Entries option, see the “Print” section in the *VA FileMan User Manual*.

Three additional files are supplied that can dramatically alter the predictable behavior described above. They are checked in the following order against the user’s entry:

1.  LOCAL SHORTCUT (#8984.2) file: Shortcuts are used to point to a single term. They can be a word or phrase. MTLU checks the user’s entry against this file first for an exact match. If found, the lookup displays only the associated entry. A single shortcut *cannot* point to multiple terms.
1.  LOCAL SYNONYM (#8984.3) file: Synonyms can be associated with many terms in a file because they can be associated with multiple “tokens” rather than a specific term. For example, CANCER can be defined as a synonym of “MALIG”, “TUMOR”, and “LEUKEMIA”. When the user enters CANCER, the lookup finds *all* terms associated with the three tokens as if each had been entered separately. Compared with the example above, CANCER returns 534 matches. CANCER LIP returns the same 12 matches as MALIG LIP.
2.  LOCAL KEYWORD (#8984.1) file: A keyword or phrase can be associated with a single term, much like a shortcut; however, it can also be associated with multiple terms, and multiple keywords can be associated with the same term.

The term SMOKER can be used as a synonym or keyword. As a keyword, one can associate it with a few *specific* diseases. As a synonym, properly selected tokens might result in a display of all smoking-related diseases.

Recall that MALIG results in 447 matches. If this were used as a shortcut to a single entry, MTLU would display only that entry and the remaining 446 would never be displayed.

These files add some control over the behavior of certain lookups. However, developers should use extreme caution when placing entries in these files to ensure that results are predictable and appropriate for both users and other VistA software developers.

The decision to populate them for a given lookup file depends on whether a commonly used word or phrase results in any matches during a lookup. If *not*, it is a candidate. The LOCAL KEYWORD (#8984.1), LOCAL SHORTCUT (#8984.2), and LOCAL SYNONYM (#8984.3) files should only be populated with common words or phrases.

If a search produces no matches, MTLU continues with a standard VA FileMan search.

## MTLU User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Multi-Term Look-Up Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Multi-Term Lookup Main Menu \[XTLKUSER2\], which can be selected from the Application Utilities \[XTMENU\] menu. The options are described in the same order as they appear on the screen, as shown in <u>Figure 1</u>:

<span id="_Ref511379926" class="anchor"></span>Figure 1: Multi-Term Lookup Main Menu Options

Application Utilities ... \[XTMENU\]

<span class="mark">Multi-Term Lookup Main Menu ...</span> \[XTLKUSER2\]

Multi-Term Lookup (MTLU) \[XTLKLKUP\]

Print Utility \[XTLKPRTUTL\]

Utilities for MTLU ... \<Locked with XTLKZMGR\> \[XTLKUTILITIES\]

Delete Entries From Look-up \<Locked with XTLKZMGR\> \[XTLKMODPARK\]

ST Add Entries To Look-Up File \<Locked with XTLKZMGR\> \[XTLKMODPARS\]

Add/Modify Utility... \[XTLKMODUTL\]

Most MTLU options are described using the following methods:

- Introduction—A detailed description of the option is given. The introduction usually contains any necessary special instructions.
- Process Chart—The step-by-step flow of the option is illustrated, showing the various choices allowed at each prompt.
- Examples—In most cases, there is an example of what might appear on the screen when using the option. If the option produces a hardcopy output, an example of the output is usually given.

The phrase “You will be prompted for a device at this step” appears in the process chart when asked for a device. A Standard Device Chart is shown on the next page (see Section <u>2.5.1.1</u>). It aids in answering prompts related to device selection.

The MTLU Process Charts do *not* contain documentation of the system’s response to erroneous input. In certain instances, to preserve the integrity of previously entered data, the system does *not* allow the entry of a caret (^, sometimes referred to as an up-arrow). This might *not* be documented.

#### Standard Device Chart

The chart in <u>Figure 2</u> aids in answering prompts related to device selection:

<span id="_Ref26359217" class="anchor"></span>Figure 2: Standard Device Chart

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 DEVICE: Device name/number

from your DEVICE file (#3.5)

for report to print on..............3

'Q'UEUE to have report

queued to print at a

Later date/time.....................2

\<Enter\> for report to

Print on your screen................3

Up-arrow \<^\>........................6

2 DEVICE: Device name/number from

your DEVICE file (#3.5)

for report to print on..............3

Up-arrow \<^\>........................6

3 RIGHT MARGIN: 132// \*\<Enter\> to accept default,

different RIGHT MARGIN Value, or

up-arrow \<^\>........................6

\*The next step depends on what you entered in Step 1:

Device name/number..................4

"Q".................................5

\<Enter\> (The report appears on your

screen).............................6

4 WANT TO FREE UP THIS

TERMINAL? NO// \<Enter\> to accept default...........6

'Y'ES to free up terminal

during report processing

and to exit from the

system..............................5

Up-arrow \<^\>........................6

5 REQUESTED TIME TO PRINT: \*\<Enter\> to accept default...........6

NOW// \*Later date/time for report

process to begin....................6

Up-arrow \<^\>........................6

\*If \<Enter\> or later date/time is entered, the following

message appears: "REQUEST QUEUED!"

6 Return to the menu.

### Using the Multi-Term Lookup (MTLU) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multi-Term Lookup (MTLU) \[XTLKLKUP\] option is used to test the ICD diagnosis and procedure codes, CPT codes, and other commonly used references that have been entered in the LOCAL LOOKUP (#8984.4) file and have been associated with a shortcut, synonym, or keyword.

The system searches for entries in the following order:

1.  Shortcut
2.  Synonym
3.  Keyword

If you are entering a multi-term narrative (phrase), you can enter double spaces between each term to avoid a search of the LOCAL SHORTCUT (#8984.2) file. When searching for a keyword phrase, the system searches for each word in the phrase and then displays all common entries. For example, if the keyword is FRACTURE FEMUR, the system searches for FRACTURE and then FEMUR and displays only those codes with a diagnosis containing both keywords or synonyms of those words.

The process chart in <u>Figure 3</u> shows the prompts and steps involved in using the Multi-Term Lookup (MTLU) option:

<span id="_Ref511380033" class="anchor"></span>Figure 3: Multi-Term Lookup (MTLU) Option Process Chart

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 Lookup on which file?: Name of entry in LOCAL

LOOKUP file (#8984.4)................2

\<?\> for list of entries..............1

\<Enter\> or up-arrow \<^\>..............4

<u>\_\_\_\_</u>

2 NARRATIVE: Existing shortcut,

synonym, or keyword..................3

If a word, phrase, or symbol is entered that the system cannot

identify, the following appears:

"Narrative contained no usable words.

The following word(s) was not used in this search: {word(s)}

Search was unsuccessful."

The selected code or description is displayed. The system searches

in the following order: shortcut, synonym, then keyword. If more than

one entry is found, they are displayed, and you are prompted to

select one. If only one entry is found, the following appears:

3 OK? Y// \<Enter\> to accept default............4

'N'O.................................4

4 Return to the menu.

<u>Figure 4</u> is an example of what might appear on your screen when using the Multi-Term Lookup (MTLU) option:

<span id="_Ref511380060" class="anchor"></span>Figure 4: Multi-Term Lookup (MTLU) Option—Sample User Entries

Lookup on which file?: <span class="mark">ICD DIAGNOSIS \<Enter\></span>

NARRATIVE: <span class="mark">DIABETES MELLITUS \<Enter\></span>

( DIABETES\|DIABETIC MELLITUS )

....

The following 3 matches were found:

1: 250.00 (250.00)

DIABETES UNCOMPL ADULT/NIDDM

2: 250.40 (250.40)

DIAB RENAL MANIF ADULT/NIDDM

3: 775.0 (775.0)

INFANT DIABET MOTHER SYN

Select 1-3: <span class="mark">2 \<Enter\></span>

### Using the Print Utility Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Utility \[XTLKPRTUTL\] option is used to print a list of shortcuts, keywords, or synonyms from a specified reference file in the LOCAL LOOKUP (#8984.4) file. Both the shortcut and keyword lists can be sorted alphabetically by name or numerically by code. The synonym list, however, only prints alphabetically.

Since these lists can be long and the generation time consuming, it is suggested you queue the report to a device during off hours.

The process chart in <u>Figure 5</u> shows the prompts and steps involved in using the Print Utility option:

<span id="_Ref511380137" class="anchor"></span>Figure 5: Print Utility Option Process Chart

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 Select one of the following:

SH Shortcuts

KE Keyword

SY Synonyms

Print which file?: SH for Shortcuts....................2

KE for Keywords.....................2

SY for Synonym......................3

2 Select one of the following:

A Alphabetic

C Code

Sort By?: 'A'lphabetic........................3

'C'ode..............................3

3 Print {Shortcuts, Keywords, or

Synonyms} for which file?: Name of entry in LOCAL

LOOKUP file (#8984.4)...............4

\<?\> for list of entries.............3

\<Enter\> or up-arrow \<^\>.............5

4 You will be prompted for a device at this step.....................1

5 Return to the menu.

<u>Figure 6</u> is an example of what might appear on your screen when using the Print Utility option (an example of the output generated by this option is provided following the computer dialog in <u>Figure 6</u>):

<span id="_Ref511380176" class="anchor"></span>Figure 6: Print Utility Option—Sample User Entries and Sample Output

Select one of the following:

SH Shortcuts

KE Keywords

SY Synonyms

Print which file?: <span class="mark">SH \<Enter\></span> Shortcuts

Select one of the following:

A Alphabetic

C Code

Sort By?: <span class="mark">A \<Enter\></span> lphabetic

Print Shortcuts for which file?: <span class="mark">CPT \<Enter\></span>

DEVICE:HOME// <span class="mark">\<Enter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

Shortcuts of the CPT file sorted by Name NOV 23, 1994 13:36 PAGE 1

FREQUENTLY USED NARRATIVE ENTRY

---------------------------------------------------------------------------

DREAM 01200

NIGHT 02400

SLEEP 01100

### Using the Utilities for MTLU Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the options and their descriptions that comprise the Utilities for MTLU \[XTLKUTILITIES\] menu. This menu can only be accessed by holders of the XTLKZMGR security key:

- Delete Entries From Look-Up \[XTLKMODPARK\] option—Deletes entries from the LOCAL LOOKUP (#8984.4) file. To do this, there *cannot* be any shortcuts, synonyms, or keywords associated with the file to be deleted. This option should be used as a system administrator/developer utility and can only be accessed by holders of the XTLKZMGR security key.
- Add Entries To Look-Up File \[XTLKMODPARS\] option—Sets entries in the LOCAL LOOKUP (#8984.4) file. This option should be used as a system administrator/developer utility and can only be accessed by holders of the XTLKZMGR security key. To add entries with this option, DUZ(0) *must* be set to an at-sign (@; Programmer access).
- Add/Modify Utility \[XTLKMODUTL\] option—Adds or edits entries in the LOCAL KEYWORD (#8984.1), LOCAL SHORTCUT (#8984.2), and LOCAL SYNONYM (#8984.3) files.

#### Delete Entries from Look-Up Option

The Delete Entries From Look-Up \[XTLKMODPARK\] option is used to delete a reference file from a site’s LOCAL LOOKUP (#8984.4) file.

All shortcuts, synonyms, and keywords associated with the reference file you wish to delete *must* be canceled before you attempt to delete the file.

It should be noted that when a reference file is KILLed through this option, all variable pointers from the LOCAL KEYWORD (#8984.1) and LOCAL SHORTCUT (#8984.2) files are deleted. The special lookup routine for the file is also deleted.

Only holders of the XTLKZMGR security key can access this option.

![](kernel-8-0-systems-management-toolkit-user-guide/012.png) NOTE: Due to the brevity of this option, no process chart has been provided.

<u>Figure 7</u> is an example of what might appear on your screen when using the Delete Entries From Look-Up option:

<span id="_Ref511380639" class="anchor"></span>Figure 7: Delete Entries From Look-Up Option—Sample User Entries

Select LOCAL LOOKUP NAME: <span class="mark">PROCEDURE MODIFIERS \<Enter\></span>

Are you sure you want to delete PROCEDURE MODIFIERS? <span class="mark">YES \<Enter\></span>

Deleting from Local Lookup file.....

Deleting variable pointers from Local Keyword and Shortcut files.

Deleting special lookup routine from PROCEDURE MODIFIERS DD.

#### Add Entries To Look-Up File Option

The Add Entries To Look-Up File \[XTLKMODPARS\] option is used to add/edit reference files to a site’s LOCAL LOOKUP (#8984.4) file.

Examples of files that a site might wish to enter in their LOCAL LOOKUP (#8984.4) file include:

- ICD DIAGNOSIS (#80)
- ICD OPERATION/PROCEDURE (#80.1)
- CPT (#81)

Only holders of the XTLKZMGR security key can access this option. To add entries with this option, DUZ(0) *must* be set to an at-sign (@; Programmer access).

The process chart in <u>Figure 8</u> shows the prompts and steps involved in using the Add Entries To Look-Up File option:

<span id="_Ref511380749" class="anchor"></span>Figure 8: Add Entries To Look-Up File Option Process Chart (1 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 Select LOCAL LOOKUP NAME: Name of new reference

file you wish to enter

in LOCAL LOOKUP (#8984.4) file......2

\<?\> for file list...................1

Name of existing file...............8

\<Enter\> or up-arrow \<^\>............12

2 ARE YOU ADDING {reference

file name} AS A NEW LOCAL

LOOKUP (THE nTH)? 'Y'ES...............................3

'N'O................................1

3 LOCAL LOOKUP NAME:

{reference file name}// \<Enter\> to accept default...........4

Other file name.....................4

4 LOCAL LOOKUP DISPLAY PROTOCOL: Entry point for routine

to determine the display

format..............................5

\<Enter\> to accept the

internal default display

format..............................5

If the entry made at this step is not the same as the

cross reference in the description field of the file,

the software still functions, but it only uses the

keywords entered in the LOCAL LOOKUP (#8984.4) file.

\*Required field

<span id="_Toc193181911" class="anchor"></span>Figure 9: Add Entries To Look-Up File Option Process Chart (2 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

\* 5 INDEX: Cross reference to be

used to create new key-

words...............................6

> **NOTE:** The following message is displayed :

"...Ok, will now setup KEYWORD and SHORTCUT file DD's to allow

terms for {reference file name} entries..."

\* 6 PREFIX: M//: Letter(s) to be used to

identify a variable

pointer.............................7

7 The following reminder message is displayed:

\<REMINDER\> Using 'Edit File', set the lookup routine, XTLKDICL, in

{reference file name} DD ....................................1

The selected file is displayed.

8 ...OK? YES// \<Enter\> to accept default ..........9

'N'O................................1

9 LOCAL LOOKUP NAME:

{reference file name}// \<Enter\> to accept default..........10

Correct file name..................10

10 LOCAL LOOKUP DISPLAY PROTOCOL:

{protocol}// \<Enter\> to accept default..........11

Correct entry point for

routine to set display

format.............................11

\<Enter\> (no default) to

accept the internal

Default display format.............11

11 INDEX: {index}// \<Enter\> to accept default..........12

correct cross reference

to be used to create new

Keywords...........................12

12 Return to the menu.

\*Required field

<u>Figure 10</u> is an example of what might appear on your screen when using the Add Entries To Look-Up File option:

<span id="_Ref507515420" class="anchor"></span>Figure 10: Add Entries To Look-Up File Option—Sample User Entries

Select LOCAL LOOKUP NAME: <span class="mark">PROCEDURE MODIFIERS \<Enter\></span>

ARE YOU ADDING 'PROCEDURE MODIFIERS' AS A NEW LOCAL LOOKUP (THE 4th)? <span class="mark">Y \<Enter\></span> (YES)

LOCAL LOOKUP NAME: PROCEDURE MODIFIERS// <span class="mark">\<Enter\></span>

LOCAL LOOKUP DISPLAY PROTOCOL: <span class="mark">\<Enter\></span>

INDEX: <span class="mark">AIHS \<Enter\></span>

...Ok, will now setup KEYWORD and SHORTCUT file DD's

to allow terms for 'PROCEDURE MODIFIERS' entries...

PREFIX: M// <span class="mark">\<Enter\></span>

\<REMINDER\> Using 'Edit File', set the lookup routine, XTLKDICL, in PROCEDURE MODIFIERS DD

Select LOCAL LOOKUP NAME: <span class="mark">\<Enter\></span>

#### Add/Modify Utility Option

The Add/Modify Utility \[XTLKMODUTL\] option is used to enter new or edit existing shortcuts, keywords, or synonyms to the LOCAL LOOKUP (#8984.4) file.

#### Shortcut

A shortcut is a word or phrase that recognizes one specific code or procedure. If you are adding a shortcut whose text duplicates the first part of an existing entry, you *must* enclose the new shortcut word or phrase in double quotes to prevent the system from matching it to existing terms.

#### Keyword

A keyword is a word or phrase that corresponds to several related codes or procedures. Keywords are typically terms commonly used to describe a clinical entity. Entering a series of keywords separated by single spaces results in all the keywords being added to the specified code.

#### Synonym

A synonym is a word entered to expand the lookup capability of an existing term or terms in the LOCAL LOOKUP (#8984.4) file. Synonyms would be used in cases where several words within the text of codes or procedures have the same diagnostic meaning (such as CANCER and MALIGNANCY). A synonym can be entered for an existing keyword or for a word in the diagnostic description or procedure (such as the term CANCER might be matched to the synonyms MALIGNANCY, LEUKEMIA, and CARCINOMA). When CANCER is referenced in the Multi-Term Lookup (MTLU) \[XTLKLKUP\] option, it recognizes all the codes and descriptions associated with MALIGNANCY, LEUKEMIA, and CARCINOMA.

![](kernel-8-0-systems-management-toolkit-user-guide/013.png) NOTE: A synonym replaces the original word in the lookup process; therefore, to retain the original word in the search, it *must* be matched to itself as well as to other synonyms.

Words used as a Shortcut should never be repeated as Synonyms or Keywords. Since the system searches for shortcuts first and stops when one is found, it *cannot* find duplicated words in the LOCAL SYNONYM (#8984.3) or LOCAL KEYWORD (#8984.1) files. Since searching all files for each word is time consuming, the search is done in this order to speed up the search process.

Since the add/modify functions for Shortcuts, Keywords, and Synonyms are considered separate options, a process chart for each is provided. The charts on the following pages show the prompts and steps involved in using the options in <u>Figure 11</u>:

<span id="_Ref26362264" class="anchor"></span>Figure 11: Add/Modify Utility Menu Options

Select Add/Modify Utility Option: <span class="mark">?? \<Enter\></span>

SH Shortcuts \[XTLKMODSH\]

KE Keywords \[XTLKMODKY\]

SY Synonyms \[XTLKMODSY\]

The Shortcuts \[XTLKMODSH\] option, one of the three selections within the Add/Modify Utility \[XTLKMODUTL\] option, is described in <u>Figure 12</u>.

The process chart in <u>Figure 12</u> shows the prompts and steps involved in using the Add/Modify Utility \[XTLKMODUTL\] option when adding or editing a shortcut:

<span id="_Ref511381133" class="anchor"></span>Figure 12: Add/Modify Utility Option—Shortcuts Process Chart (1 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify

Utility Option: SH for Shortcuts....................2

\<Enter\> or up-arrow \<^\>............11

2 Additions/Modifications to

Shortcuts in which file? Name of entry in local

reference file......................3

\<?\> for list of entries.............2

\<Enter\>.............................1

3 Select LOCAL SHORTCUT

FREQUENTLY USED NARRATIVE: New text you wish to use

as a shortcut.......................4

Existing shortcut term..............8

\<Enter\>.............................1

4 ARE YOU ADDING {'text'} AS

A NEW LOCAL SHORTCUT? 'Y'ES...............................5

'N'O or \<Enter\>.....................3

An at-sign (@) entered at this step deletes the entire entry.

5 LOCAL SHORTCUT FREQUENTLY

USED NARRATIVE: {shortcut}// \<Enter\> to accept default...........6

Other text..........................6

6 LOCAL SHORTCUT ENTRY: Name or number of entry

in LOCAL LOOKUP file

(#8984.4) you wish your

shortcut to reference...............7

<span id="_Toc207521474" class="anchor"></span>Figure 13: Add/Modify Utility Option—Shortcuts Process Chart (2 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

7 If the selected number/name corresponds to more than one entry, they

are shown and you are prompted to choose one. If there is only one

corresponding entry, it is displayed and the following appears:

"...OK? YES// \<Enter\> to accept default...........2

'N'O................................6

8 LOCAL SHORTCUT FREQUENTLY

USED NARRATIVE:{shortcut}// \<Enter\> to accept default...........9

Correct shortcut term...............9

9 LOCAL SHORTCUT ENTRY:

{code}// \<Enter\> to accept default...........2

Correct code.......................10

The selected code is displayed.

10 ...OK? YES// \<Enter\> to accept default...........2

'N'O................................9

11 Return to the menu.

The Keywords \[XTLKMODKY\] option, one of the three selections within the Add/Modify Utility \[XTLKMODUTL\] option, is described below.

The process chart in <u>Figure 14</u> shows the prompts and steps involved in using the Add/Modify Utility \[XTLKMODUTL\] option when adding or editing a Keyword:

<span id="_Ref511381213" class="anchor"></span>Figure 14: Add/Modify Utility Option—Keywords Process Chart

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify

Utility Option: KE for Keywords.....................2

\<Enter\> or up-arrow \<^\>.............7

2 Additions/Modifications to

Keywords in which file? Name of entry in local

reference file......................3

\<?\> for list of entries.............2

\<Enter\>.............................1

3 Which code in the {file

name} file? Code for which you wish

to enter a keyword..................4

4 Select LOCAL KEYWORD NAME: New text you wish to use

as a keyword........................5

Existing keyword term...............6

\<Enter\>.............................1

5 ARE YOU ADDING {'text'} AS

A NEW LOCAL KEYWORD? 'Y'ES...............................6

'N'O or \<Enter\>.....................1

An at-sign (@) entered at this step deletes the entire entry.

6 LOCAL KEYWORD NAME:

{keyword}// \<Enter\> to accept default...........2

Correct keyword term................2

7 Return to the menu.

The Synonyms \[XTLKMODSY\] option, one of the three selections within the Add/Modify Utility \[XTLKMODUTL\] option, is described below.

The process chart in <u>Figure 15</u> shows the prompts and steps involved in using the Add/Modify Utility \[XTLKMODUTL\] option when adding or editing a Synonym:

<span id="_Ref511381272" class="anchor"></span>Figure 15: Add/Modify Utility Option—Adding or Editing a Synonym Process Chart (1 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

1 SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify

Utility Option: SY for Synonyms.....................2

\<Enter\> or up-arrow \<^\>.............9

2 Additions/Modifications to

Synonyms in which file? Name of entry in local

reference file......................3

\<?\> for list of entries.............2

\<Enter\>.............................1

The entry made at this step must be in all upper case

letters.

3 Select LOCAL SYNONYM TERM: New text you wish to use

as a synonym........................4

Existing synonym term...............7

\<Enter\>.............................1

4 ARE YOU ADDING {'text'} AS

A NEW LOCAL SYNONYM? 'Y'ES...............................5

'N'O................................3

An at-sign (@) entered at this step deletes the entire entry.

5 LOCAL SYNONYM TERM:

{synonym}// \<Enter\> to accept default...........6

Other text..........................6

6 LOCAL SYNONYM

Select SYNONYM: Existing term in LOCAL

LOOKUP file (#8984.4) for

which you are entering a

synonym.............................2

<span id="_Toc207521477" class="anchor"></span>Figure 16: Add/Modify Utility Option—Adding or Editing a Synonym Process Chart (2 of 2)

IF USER THEN

STEP AT THIS PROMPT... ANSWERS WITH... STEP

7 TERM: {term entered

at Step 3}// \<Enter\> to accept default...........8

Correct synonym term................8

The entry made at this step must be in all upper case

letters.

8 Select SYNONYM: {term

synonym was entered for}// \<Enter\> to accept default...........2

Correct term........................2

9 Return to the menu.

### MTLU Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of what might appear on your screen when using the Add/Modify Utility \[XTLKMODUTL\] option:

- [Example 1](#example-1) shows a new shortcut entry.
- [Example 2](#example-2) shows a new keyword entry.
- [Example 3](#example-3) shows the editing of an existing synonym entry.

#### Example 1

<u>Figure 17</u> illustrates a new Shortcut entry.

<span id="_Ref511381571" class="anchor"></span>Figure 17: Shortcut Option—Sample User Entries

SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify Utility Option: <span class="mark">SH \<Enter\></span> Shortcuts

Additions/Modifications to Shortcuts in which file? <span class="mark">CPT \<Enter\></span>

Select LOCAL SHORTCUT FREQUENTLY USED NARRATIVE: <span class="mark">COUGH \<Enter\></span>

ARE YOU ADDING 'COUGH' AS A NEW LOCAL SHORTCUT? <span class="mark">Y \<Enter\></span> (YES)

LOCAL SHORTCUT FREQUENTLY USED NARRATIVE: COUGH// <span class="mark">\<Enter\></span>

LOCAL SHORTCUT ENTRY: <span class="mark">31659 \<Enter\></span>

Searching for a CPT 31659 BRONCHOSCOPIC PROCEDURES

...OK? YES// <span class="mark">\<Enter\></span> (YES)

#### Example 2

<u>Figure 18</u> illustrates a new Keyword entry.

<span id="_Ref511381618" class="anchor"></span>Figure 18: Keyword Option—Sample User Entries

SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify Utility Option: <span class="mark">KE \<Enter\></span> Keywords

Additions/Modifications to Keywords in which file?: <span class="mark">CPT \<Enter\></span>

Which code in the CPT file?: <span class="mark">11044 \<Enter\></span> CLEANSING TISSUE/MUSCLE/BONE

Select LOCAL KEYWORD NAME: <span class="mark">TISSUE SKIN \<Enter\></span>

ARE YOU ADDING 'TISSUE SKIN' AS A NEW LOCAL KEYWORD? <span class="mark">Y \<Enter\></span> (YES)

LOCAL KEYWORD NAME: TISSUE SKIN// <span class="mark">\<Enter\></span>

#### Example 3

<u>Figure 19</u> illustrates editing an existing Synonym entry.

<span id="_Ref511381636" class="anchor"></span>Figure 19: Synonym Option—Sample User Entries

SH Shortcuts

KE Keywords

SY Synonyms

Select Add/Modify Utility Option: <span class="mark">SY \<Enter\></span> Synonyms

Additions/Modifications to Synonyms in which file?: <span class="mark">CPT \<Enter\></span>

Select LOCAL SYNONYM TERM: <span class="mark">SLEEP \<Enter\></span>

TERM: SLEEP// <span class="mark">\<Enter\></span>

Select SYNONYM: DREAM// <span class="mark">NIGHT \<Enter\></span>

## MTLU Systems Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Implementation of Multi-Term Look-Up (MTLU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is how a user would configure a new file to be used with MTLU. The file you select would typically contain a free text field that more completely describes the record entry. Users would then use a cross-reference on this text field to perform lookups. MTLU is distinguished from FileMan in that users can enter a narrative or phrase, rather than a single term. The cross-reference can be either a VA FileMan Key Word In Context (KWIC)) cross-reference, or you can create a custom MUMPS cross-reference that calls the routine, ^XTLKWIC (shown in <u>Figure 20</u>). The ICD DIAGNOSIS (#80) file is used as an example.

![](kernel-8-0-systems-management-toolkit-user-guide/014.png) REF: Multi-Term Look-Up (MTLU) Application Programming Interfaces (APIs) are documented in the [*Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet Website.

Once you are in VA FileMan, run the Cross-Reference A Field \[DIXREF\] option, as shown in <u>Figure 20</u>:

<span id="_Ref507574679" class="anchor"></span>Figure 20: VA FileMan Utility Functions Option—Sample User Entries

Select OPTION: <span class="mark">UTILITY FUNCTIONS \<Enter\></span>

Select UTILITY OPTION: <span class="mark">CROSS-REFERENCE A FIELD \<Enter\></span>

MODIFY WHAT FILE: ICD DIAGNOSIS// <span class="mark">\<Enter\></span> ICD DIAGNOSIS

(12535 entries)

Select FIELD: <span class="mark">DESCRIPTION \<Enter\></span>

CURRENT CROSS-REFERENCE IS MUMPS 'D' INDEX OF FILE

CHOOSE E (EDIT)/D (DELETE)/C (CREATE): <span class="mark">C \<Enter\></span>

WANT TO CREATE A NEW CROSS-REFERENCE FOR THIS FIELD? NO// <span class="mark">Y \<Enter\></span> (YES)

CROSS-REFERENCE NUMBER: 2// <span class="mark">\<Enter\></span>

Select TYPE OF INDEXING: REGULAR// <span class="mark">MUMPS \<Enter\></span>

WANT CROSS-REFERENCE TO BE USED FOR LOOKUP AS WELL AS FOR SORTING? YES// <span class="mark">N \<Enter\></span> (NO)

SET STATEMENT: <span class="mark">S %="^ICD9(""AIHS"",I,DA)" D S^XTLKWIC</span>

KILL STATEMENT: <span class="mark">S %="^ICD9(""AIHS"",I,DA)" D K^XTLKWIC</span>

INDEX: AC// <span class="mark">AIHS \<Enter\></span>

...

NO-DELETION MESSAGE: <span class="mark">\<Enter\></span>

DESCRIPTION: <span class="mark">\<Enter\></span>

Edit? NO// <span class="mark">\<Enter\></span>

DO YOU WANT TO CROSS-REFERENCE EXISTING DATA NOW? YES// <span class="mark">Y \<Enter\></span> (YES)

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...

<span id="_Toc193181923" class="anchor"></span>Figure 21: Add Entries To Look-Up File—Sample User Entries

\><span class="mark">D ^XUP \<Enter\></span>

Setting up programmer environment

Terminal Type set to: <span class="mark">C-VT100 \<Enter\></span>

Select OPTION NAME: <span class="mark">APP \<Enter\></span> LICATION UTILITIES XTMENU Application Utilities

Multi-Term Lookup Main Menu ...

Select Application Utilities Option: <span class="mark">MULTI \<Enter\></span> -Term Lookup Main Menu

Multi-Term Lookup (MTLU)

Print Utility

Utilities for MTLU ...

Select Multi-Term Lookup Main Menu Option: <span class="mark">UTIL \<Enter\></span> ities for MTLU

KL Delete Entries From Look-up

ST Add Entries To Look-Up File

Add/Modify Utility ...

Select Utilities for MTLU Option: <span class="mark">ST \<Enter\></span> Add Entries To Look-Up File

Select LOCAL LOOKUP NAME: <span class="mark">ICD DIAGNOSIS \<Enter\></span>

ARE YOU ADDING 'ICD DIAGNOSIS' AS A NEW LOCAL LOOKUP (THE 3RD)? <span class="mark">Y \<Enter\></span> (YES)

LOCAL LOOKUP NAME: ICD DIAGNOSIS// <span class="mark">\<Enter\></span>

LOCAL LOOKUP DISPLAY PROTOCOL: <span class="mark">DSPLYD^XTLKKWLD \<Enter\></span>

INDEX: <span class="mark">AIHS \<Enter\></span>

...Ok, will now setup KEYWORD and SHORTCUT file DD's

to allow terms for 'ICD DIAGNOSIS' entries...

PREFIX: M// <span class="mark">? \<Enter\></span>

Answer must be a unique prefix, 1-10 characters in length

PREFIX: M// <span class="mark">D \<Enter\></span>

\<REMINDER\> Using 'Edit File', set the lookup routine, XTLKDICL, in ICD DIAGNOSIS DD

Select LOCAL LOOKUP NAME: <span class="mark">\<Enter\></span>

If *all* references to a file (by all packages) are to behave as MTLU lookups, add the special lookup routine, ^XTLKDICL, to the file’s DD using the VA FileMan Edit File \[DIEDFILE\] option.

![](kernel-8-0-systems-management-toolkit-user-guide/015.png) REF: For more information on the Edit File \[DIEDFILE\] option, see the “File Utilities” section in the *VA FileMan Advanced User Manual*.

<span id="_Toc193181924" class="anchor"></span>Figure 22: VA FileMan Edit File Option—Sample User Entries

VAH,MTL\><span class="mark">D Q^DI \<Enter\></span>

VA FileMan 20.0

Select OPTION: <span class="mark">UT \<Enter\></span> ILITY FUNCTIONS

Select UTILITY OPTION: <span class="mark">ED \<Enter\></span> IT FILE

MODIFY WHAT FILE: ICD DIAGNOSIS// <span class="mark">\<Enter\></span>

NAME: ICD DIAGNOSIS// <span class="mark">\<Enter\></span>

DESCRIPTION: <span class="mark">\<Enter\></span>

1\>Contains all valid ICD diagnosis codes.

EDIT Option: <span class="mark">\<Enter\></span>

Select APPLICATION GROUP: <span class="mark">\<Enter\></span>

PROGRAMMER: <span class="mark">\<Enter\></span>

VERSION: 9// <span class="mark">\<Enter\></span>

DATA DICTIONARY ACCESS: <span class="mark">\<Enter\></span>

READ ACCESS: <span class="mark">\<Enter\></span>

WRITE ACCESS: <span class="mark">\<Enter\></span>

DELETE ACCESS: <span class="mark">\<Enter\></span>

LAYGO ACCESS: <span class="mark">\<Enter\></span>

AUDIT ACCESS: <span class="mark">\<Enter\></span>

DD AUDIT? NO// <span class="mark">\<Enter\></span>

ASK 'OK' WHEN LOOKING UP AN ENTRY? YES// <span class="mark">\<Enter\></span> (YES)

POST-SELECTION ACTION: <span class="mark">\<Enter\></span>

LOOK-UP PROGRAM: <span class="mark">XTLKDICL</span>

CROSS-REFERENCE ROUTINE: <span class="mark">\<Enter\></span>

Select UTILITY OPTION: <span class="mark">\<Enter\></span>

![](kernel-8-0-systems-management-toolkit-user-guide/016.png) NOTE: The developer might elect to use MTLU only in selected instances. This is accomplished by *not* adding the special lookup routine to the file’s DD. After the file has been added to the LOCAL LOOKUP (#8984.4) file, you can make a developer call to LKUP^XTLKMGR.

![](kernel-8-0-systems-management-toolkit-user-guide/017.png) REF: Multi-Term Look-Up (MTLU) Application Programming Interfaces (APIs) are documented in the [*Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet Website.

# Parameter Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Parameter Tools Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Parameter Tools released with Kernel Toolkit Patch XT\*7.3\*26. It explains the functions available with the use of the Parameter Tools, as well as providing additional explanatory material and a generic example to illustrate the use of the Parameter Tools.

Parameter Tools was designed as a method of managing the definition, assignment, and retrieval of parameters for VistA software applications. A parameter can be defined for various levels at which you want to allow the parameter described (such as software level, system level, division level, location level, user level).

![](kernel-8-0-systems-management-toolkit-user-guide/018.png) REF: For a list and description of the Parameter Tools (XPAR) application programming interfaces (APIs), see the “Toolkit—Parameter Tools” section in the [*Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf).

## Parameter Tools Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA software applications are designed to be used in a variety of ways. Many aspects of site activity vary from one site to another, and thus, there are many possible ways software applications can be used that also vary from one institution to another. Each site has its own requirements—its own settings for each software application. System managers *must* modify the software parameters to fit their requirements.

Previously, each software application had its own files and options, but no two software applications had the site parameters set up the same way or found in the same place. Thus, when a new software application was released, each site would have to look for the location where the settings were stored for that software. Next, they would have to look to see what settings were available and how to set them. Very little about the parameters was uniform from software to software.

With the Computerized Patient Record System (CPRS) software, the idea was born that a parameter file could be created to export with the software. The CPRS parameter file and parameter utility were subsequently modified to create a generic method of exporting and installing other VistA software applications. Most developers were willing to abandon previous methods and use this tool for software they were developing.

Whenever you have an entity with many attributes that apply to it, you can do either of the following:

- Make one big relation to represent that entity.
- Create a "binary" relation to represent the entity. The relation consists of two columns (thus the term binary), one representing the attribute and the other representing the value for that attribute. So, each tuple (that is a data type/data object containing two or more components) of the relation represents a single attribute and its associated value.

![](kernel-8-0-systems-management-toolkit-user-guide/019.png) NOTE: This works only when the individual attributes are independent observations (have no dependencies on anything other than the key that identifies the entity). Such a relation tends to look a lot like a Windows INI file.

Most of the VistA parameter files were very long lists of independent values that pertained to a single entity. In most cases, this entity was the site or system on which the software was running \[like an INI file\]. In other cases, however, the parameter files had multiples that made things more complex. These multiples generally allow parameters to be defined at levels more specific than the site (such as by divisions or hospital location). It seems best to accommodate this by using both an entity identifier and parameter together to name any given value. This yields a relation with a compound key:

Entity \| Parameter = Value

Finally, it seems that multiple-valued parameters (such as collection times) occur often enough that it is worthwhile to add a field to identify the parameter instance. So, the relation becomes:

Entity \| Parameter \| Instance = Value

This is the relation that the PARAMETERS (#8989.5) file is intended to represent.

Software parameter files frequently maintain parameters that apply to the site, a division, or a location. In addition, many parameters that apply to individual users are kept in the NEW PERSON (#200) file. Also, many parameter values are hard coded in individual software routines for the case when the site has *not* set up a value for a given parameter. Entity, then, is implemented as a VARIABLE POINTER.

A given parameter may occur for a variety of entities. In fact, you frequently need to obtain the value of a parameter by following an entity "chain." For example, the Add Orders menu a CPRS user sees may be defined at various levels. Initially, a site generally creates a custom Add Orders menu. Later, hospital locations may each build a custom menu that more specifically meets their needs. Individual users may also have their own Add Orders menus. If no site configuration has been done, the Add Orders menu exported with OE/RR is used. So, when OE/RR needs to display an Add Orders menu, a chain is followed that looks first to see if the user has their own menu. Next, the current location is checked, followed by the site. Finally, if no values exist, the software default menu is used.

In the PARAMETER DEFINITION (#8989.51) file, a multiple lists which entities are valid with a given parameter. These entities are also assigned a precedence, so that it is possible to write functions that will "chain" through entities until a value is found, using the proper sequence.

## Parameter Tools Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XT\*7.3\*26 contains a developer toolset that allows creation of software parameters in a central location. Integration Control Registration (ICRs) 2263 and 2336 define the supported entry points for this application. Kernel Patch XU\*8.0\*201 allows KIDS to transport the parameters.

Parameter Tools is a generic method of handling parameter definition, assignment, and retrieval. A parameter can be defined for various entities where an entity is the level at which you want to allow the parameter defined (such as software level, system level, division level, location level, user level, and so on). A developer can then determine in which order the values assigned to given entities are interpreted.

## Parameter Tools Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are some basic definitions used by Parameter Tools:

- [Entity](#entity)
- [Parameter](#parameter)
- [Instance](#instance)
- [Value](#value)
- [Parameter Template](#parameter-template)

### Entity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An entity is a level at which you can define a parameter. The entities allowed are stored in the PARAMETER ENTITY (#8989.518) file. Kernel Toolkit patches maintain entries in this file. <u>Table 1</u> lists the allowable parameter entries:

| Entity Prefix | Message      | Points To File          |
|---------------|--------------|-------------------------|
| PKG       | Package      | PACKAGE (#9.4)          |
| SYS       | System       | DOMAIN (#4.2)           |
| DIV       | Division     | INSTITUTION (#4)        |
| SRV       | Service      | SERVICE/SECTION (#49)   |
| LOC       | Location     | HOSPITAL LOCATION (#44) |
| TEA       | Team         | TEAM (#404.51)          |
| CLS       | Class        | USR CLASS (#8930)       |
| USR       | User         | NEW PERSON (#200)       |
| BED       | Room-Bed     | ROOM-BED (#405.4)       |
| OTL       | Team (OE/RR) | OE/RR LIST (#100.21)    |
| DEV       | Device       | DEVICE (#3.5)           |

<span id="_Ref477871593" class="anchor"></span>Table 2: Templates—Parameter Tools

Package (PKG), as an entity, allows the software defaults to be handled the same way as other parameters rather than hard-coded.

System (SYS), Division (DIV), Location (LOC), and User (USR) are frequent entries in existing software parameter files (or additions to the NEW PERSON \[#200\] file).

Service (SRV), Team (TEA), and Class (CLS) are referenced frequently by parameters that pertain to Notifications.

The process of exporting software using this kind of parameters file involves sending:

- Parameter definitions that belong to the software (entries in the PARAMETER DEFINITION \[#8989.51\] file).
- Actual parameter instances that point to the software (entries in the PARAMETERS \[#8989.5\] file that have an entity that matches the software).

All the other entries in the PARAMETERS (#8989.5) file (those that correspond to entities other than Package \[PKG\]) would never be exported, as they are only valid for the system on which they reside.

### Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A parameter is the actual name under which values are stored. The name of the parameter *must* be:

- Namespaced
- Unique and start with two uppercase characters

Parameters can be defined to store the typical software parameter data (such as the default add order screen in OE/RR), but they can also be used to store graphical user interface (GUI) application screen settings a user has selected (such as font or window width). With each parameter, a more readable display name can also be defined. When a parameter is defined, the entities that may set that parameter are also defined. The definition of parameters is stored in the PARAMETER DEFINITION (#8989.51) file.

### Instance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An instance is a unique value assigned to an entity/parameter combination. For most parameters, there will only be one instance, that is, instance does *not* apply and is simply set to 1.

However, a parameter can be multi-valued—it can have more than one instance. More than one value can be assigned to the parameter as it relates to a specific entity. For example, lab collection times at a division. For a single entity (division in this case), multiple collection times may exist. Each collection time would be assigned a unique instance.

A parameter is *not* considered multi-valued if it can apply to several entities, but for each entity only one value of the parameter exists. For example, "maximum days for a lab order" can be set for every location in the hospital. However, since there is only one value for each location, "maximum days for a lab order" is *not* multi-valued.

When a parameter that is multi-valued is defined, the instance can be defined as any of the following data types:

- NUMERIC
- DATE/TIME
- POINTER
- SET OF CODES
- FREE TEXT
- YES/NO

The validating logic for an instance is defined the same way as for a value.

### Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A value can be assigned to every parameter for the entities allowed in the parameter definition. Values are stored in the PARAMETERS (#8989.5) file. Fields in the PARAMETERS (#8989.5) file map to DIR fields. DIR is used to validate the data. Values can be any of the following data types:

- NUMERIC
- DATE/TIME
- POINTER
- SET OF CODES
- FREE TEXT
- YES/NO
- WORD-PROCESSING Type

### Parameter Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A PARAMETER template is like an INPUT template. It contains a list of parameters that can be entered through an input session (such as an option). Templates are stored in the PARAMETER TEMPLATE (#8989.52) file. Entries in this file *must* also be namespaced.

<u>Table 2</u> lists the two INPUT templates for adding parameter definitions:

| Template                      | Description                                                |
|-------------------------------|------------------------------------------------------------|
| XPAR SINGLE VALUED CREATE | For adding/editing parameters that will be single valued   |
| XPAR MULTI VALUED CREATE  | For adding/editing parameters that will be multiple valued |

## Why Use Parameter Tools?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The reason a developer would use Parameter Tools is to allow a hierarchical designation of a parameter value. Thus, rather than many parameters that exist now, which are just for the system level or just for a particular clinic, Parameter Tools allows you to define:

- Different levels at which the parameter can be set.
- In what priority the values are used.

Take, for example, setting up a default order menu for a person. Each facility may have a default order menu for their primary care clinicians. Each division may have one that is slightly different if their practices vary enough. For each location, they may set up a different order menu so that users working in a cardiology clinic get a different set of possible orders than those in a dermatology clinic. And there may be reasons to give one specific person a different order menu because they are authorized to prescribe additional medications, because they tend to practice in a different flow, or for other reasons. It's one parameter, but it allows the parameter to be set for multiple entities (at multiple levels).

Those entities are defined in the ICR, but can include:

- Package (PKG, which only developers should set—these are default export values)
- System (SYS, whole medical facility)
- Division (DIV)
- Location (LOC)
- Room-Bed (BED)
- Team (TEA)
- Provider

The PARAMETER DEFINITION (#8989.51) file defines what entities are allowed to be used for a parameter and in which order they are resolved (individual takes precedence over location takes precedence over division takes precedence over system which takes precedence over package). Sometimes you would want to create defaults for your medical center but allow users in a certain area to customize what they see and do for their role.

XPAR finds the appropriate value based on the parameter definitions and settings that may exist. This way, the developer does *not* need to look at multiple different location or person files to determine how the software should operate.

With integrations, this is even more important because it allows facilities to integrate; however, at the same time, continue some business practices based on parameters set at the division level rather than at the system level.

## General Parameter Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The General Parameters Tools \[XPAR MENU TOOLS\] menu (<u>Figure 23</u>), which is located on the Programmer Options \[XUPROG\] menu; locked with the XUPROG security key, provides general purpose options for managing and editing parameters.

<span id="_Ref67479061" class="anchor"></span>Figure 23: General Parameters Tools Menu \[XPAR MENU TOOLS\]

Select Programmer Options \<TEST ACCOUNT\> Option: <span class="mark">General Parameter Tools \<Enter\></span>

LV List Values for a Selected Parameter \[XPAR LIST BY PARAM\]

LE List Values for a Selected Entity \[XPAR LIST BY ENTITY\]

LP List Values for a Selected Package \[XPAR LIST BY PACKAGE\]

LT List Values for a Selected Template \[XPAR LIST BY TEMPLATE\]

EP Edit Parameter Values \[XPAR EDIT PARAMETER\]

ET Edit Parameter Values with Template \[XPAR EDIT BY TEMPLATE\]

EK Edit Parameter Definition Keyword \[XPAR EDIT KEYWORD\]

### List Values for a Selected Parameter Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Values for a Selected Parameter \[XPAR LIST BY PARAM\] option (<u>Figure 24</u>) prompts the user for a parameter defined in the PARAMETER DEFINITION (#8989.51) file and lists all value instances for that parameter.

The synonym for this option is “LV.”

<span id="_Ref67479122" class="anchor"></span>Figure 24: List Values for a Selected Parameter Option—Sample User Entries and Report

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">LV \<Enter\></span> List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: <span class="mark">XUSC1 \<Enter\></span> DEBUG Set Debug mode for XUSC1

Values for XUSC1 DEBUG

Parameter Instance Value

----------------------------------------------------------------------------

SYS: \<*REDACTED1\>*.VA.GOV 1 Enabled

SYS: \<*REDACTED2\>*.VA.GOV 1 Enabled

Type \<Enter\> to continue or '^' to exit:

### List Values for a Selected Entity Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Values for a Selected Entity \[XPAR LIST BY ENTITY\] option (<u>Figure 25</u>) prompts the user for the entry of an entity (such as location, user, and so on) and lists all value instances for that entity.

The synonym for this option is “LE.”

<span id="_Ref67479186" class="anchor"></span>Figure 25: List Values for a Selected Entity Option—Sample User Entries

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">LE \<Enter\></span> List Values for a Selected Entity

Entities may be set for the following:

10 User USR \[choose from NEW PERSON\]

20 Team TEA \[choose from \]

30 Class CLS \[choose from \]

40 Location LOC \[choose from HOSPITAL LOCATION\]

50 Service SRV \[choose from SERVICE/SECTION\]

60 Division DIV \[choose from INSTITUTION\]

70 System SYS \[\<*REDACTED\>*.VA.GOV\]

80 Package PKG \[choose from PACKAGE\]

90 Room-Bed BED \[choose from ROOM-BED\]

100 Team (OE/RR) OTL \[choose from OR TEST\]

110 Device DEV \[choose from DEVICE\]

Enter selection: <span class="mark">10 \<Enter\></span> User NEW PERSON

Select NEW PERSON NAME: <span class="mark">XUUSER,ONE \<Enter\></span> XUUSER,ONE OEX TECHNICAL WRITER

<span id="_Toc207521487" class="anchor"></span>Figure 26: List Values for a Selected Entity Option—Sample Report

Values for USR: XUUSER,ONE

Parameter Instance Value

----------------------------------------------------------------------------

KMPD GUI OPTION GLOBAL LIST 1 2

KMPD GUI OPTION ERROR LIST 1 2

KMPD GUI OPTION ROUTINE SEARCH 1 2

KMPD GUI OPTION LOOKUPS 1 1

KMPD GUI OPTION CODE STATS 1 2

KMPD GUI OPTION CODE EVALUATOR 1 2

KMPD GUI OPTION TIMING MONITOR 1 2

KMPD GUI OPTION ENVIRON CHECK 1 2

KMPD GUI OPTION TOOLS PARAMS 1 2

KMPD GUI OPTION ENVIRON SELECT 1 SAGG

KMPD GUI OPTION RPT 1 2~1

Type \<Enter\> to continue or '^' to exit:

### List Values for a Selected Package Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Values for a Selected Package \[XPAR LIST BY PACKAGE\] option (<u>Figure 27</u>) prompts the user for a package and lists all parameter values for the selected package.

The synonym for this option is “LP.”

<span id="_Ref67479231" class="anchor"></span>Figure 27: List Values for a Selected Package Option—Sample User Entries and Report

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">LP \<Enter\></span> List Values for a Selected Package

Select PACKAGE NAME: <span class="mark">KERNEL \<Enter\></span> XU

Values for PKG: KERNEL

Parameter Instance Value

----------------------------------------------------------------------------

XPAR TEST SET OF CODES 1 Red

XUSNPI QUALIFIED IDENTIFIER Individual_ID VA(200,

XUSNPI QUALIFIED IDENTIFIER Organization_ID DIC(4,

XUSNPI QUALIFIED IDENTIFIER Pharmacy_ID PS(59,

XUSNPI QUALIFIED IDENTIFIER Test_ID TEST

Type \<Enter\> to continue or '^' to exit:

### List Values for a Selected Template Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Values for a Selected Template \[XPAR LIST BY TEMPLATE\] option (<u>Figure 28</u>) prompts the user for a PARAMETER template. Depending on the definition of the template, additional information may be prompted for, and then the parameter values defined by the template are displayed.

The synonym for this option is “LT.”

<span id="_Ref67479274" class="anchor"></span>Figure 28: List Values for a Selected Template Option—Sample User Entries and Report

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">LT \<Enter\></span> List Values for a Selected Template

Select PARAMETER TEMPLATE NAME: <span class="mark">OEX</span>

1 OEX TEST TEMPLATE FOR OEX TEST

2 OEX TEST2 TEMPLATE FOR OEX TEST2

3 OEX TEST3 TEMPLATE FOR OEX TEST3

CHOOSE 1-3: <span class="mark">1 \<Enter\></span> OEX TEST TEMPLATE FOR OEX TEST

Select INSTITUTION NAME: <span class="mark">13TH & MISSION \<Enter\></span> CA D 662BU

Are you adding -1 as a new Instance? Yes// <span class="mark">\<Enter\></span> YES

TEMPLATE FOR OEX TEST for Division: 13TH & MISSION, -1

------------------------------------------------------------------------------

THIS IS OEX TEST

------------------------------------------------------------------------------

Type \<Enter\> to continue or '^' to exit:

### Edit Parameter Values Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Parameter Values \[XPAR EDIT PARAMETER\] option (<u>Figure 29</u>) calls the low-level parameter editor, which allows you to edit the values for every parameter. Normally, packages supply other means of editing parameters.

The synonym for this option is “EP.”

<span id="_Ref67479314" class="anchor"></span>Figure 29: Edit Parameter Values Option—Sample User Entries

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">EP \<Enter\></span> Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: <span class="mark">XUSC1 \<Enter\></span> DEBUG Set Debug mode for XUSC1

--------- Setting XUSC1 DEBUG for System: *\<REDACTED\>*.VA.GOV ---------

Value: Enabled// <span class="mark">? \<Enter\></span>

Enter a code from the list.

Select one of the following:

0 Disabled

1 Enabled

Value: Enabled// <span class="mark">\<Enter\></span>

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME:

### Edit Parameter Values with Template Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Parameter Values with Template \[XPAR EDIT BY TEMPLATE\] option prompts the user for a PARAMETER template and then uses the selected template to edit parameter values.

The synonym for this option is “ET.”

### Edit Parameter Definition Keyword Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Parameter Definition Keyword \[XPAR EDIT KEYWORD\] option allows a user to edit the keyword field in the PARAMETER DEFINITION (#8989.51) file.

The synonym for this option is “EK.”

<span id="_Toc207521491" class="anchor"></span>Figure 30: Edit Parameter Definition Keyword Option—Sample User Entries

Select General Parameter Tools \<TEST ACCOUNT\> Option: <span class="mark">EK \<Enter\></span> Edit Parameter Definition Keyword

Select PARAMETER DEFINITION NAME: <span class="mark">XUSC1 \<Enter\></span> DEBUG Set Debug mode for XUSC1

Select KEYWORD: DEVELOPER// <span class="mark">?? \<Enter\></span>

DEVELOPER

You may enter a new KEYWORD, if you wish

This field provides a list of KEYWORDS that can be used for lookup of

Parameter definitions. It is suggested that each entry only have

one word.

Select KEYWORD: DEVELOPER// <span class="mark">DEBUG \<Enter\></span>

Are you adding 'DEBUG' as a new KEYWORD? No// <span class="mark">Y \<Enter\></span> (Yes)

Select KEYWORD: <span class="mark">\<Enter\></span>

Select PARAMETER DEFINITION NAME:

## Parameter Tools Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following procedure is a simple example of a way you might use the Parameter Tools. Suppose you needed a parameter that could be set as a default for the system (account) and overridden for a given user. Previously, you had to add a field to a software site file (such as the KERNEL SYSTEM PARAMETERS \[#8989.3\] file) and then add a similar field to the NEW PERSON (#200) file. This situation is a perfect use of the Parameter Tools.

1.  You need the equivalent to a data dictionary (DD) entry. <u>Figure 31</u> goes into the PARAMETER DEFINITION (#8989.51) file. In this case, you need a Yes/No Set of Codes. So, this is what you set up:

> <span id="_Ref477870557" class="anchor"></span>Figure 31: Setting Up the PARAMETER DEFINITION (#8989.51) File

Name: <span class="mark">XUS-XUP VPE \<Enter\></span>

DISPLAY TEXT: <span class="mark">Drop into VPE \<Enter\></span>

MULTIPLE VALUED: <span class="mark">N \<Enter\></span> No

VALUE DATA TYPE: <span class="mark">Y \<Enter\></span> yes/no

VALUE HELP: <span class="mark">Should XUP drop the user into the VPE environment? \<Enter\></span>

Description...

PRECEDENCE: <span class="mark">1</span> ENTITY FILE: <span class="mark">USER</span>

PRECEDENCE: <span class="mark">2</span> ENTITY FILE: <span class="mark">SYSTEM</span>

![](kernel-8-0-systems-management-toolkit-user-guide/020.png) NOTE: <u>Figure 31</u> only shows the fields with the data necessary to set up the PARAMETER DEFINITION (#8989.51) file.

<u>Figure 31</u> lists the order that values are looked for and returned. You want a USER value (File \#200) if there is one; otherwise, a SYSTEM value (File \#4.2). It also gives the entities that are allowed to have values of this data. In the place of SYSTEM, you could have used PACKAGE.

3.  You can use ^XPAREDIT to enter a value for your new parameter:

> <span id="_Toc207521493" class="anchor"></span>Figure 32: Use ^XPAREDIT to Enter Value for New Parameter

\><span class="mark">D ^XPAREDIT \<Enter\></span>

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: <span class="mark">XUS-XUP VPE \<Enter\></span> Drop into VPE

XUS-XUP VPE may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 System SYS \[*\<REDACTED\>*.VA.GOV\]

Enter selection: <span class="mark">2 \<Enter\></span> System *\<REDACTED\>*.VA.GOV

----- Setting XUS-XUP VPE for System: *\<REDACTED\>*.VA.GOV ---------

Value: NO

...

4.  How do you get this value out in your VistA application?

> <span id="_Toc207521494" class="anchor"></span>Figure 33: Get Value of New Parameter for VistA Application

\><span class="mark">S X=\$\$GET^XPAR("USR^SYS","XUS-XUP VPE",1,"Q") ;X will be null, 0 or 1.</span>

- First Parameter—Value from USR (User / New Person) or SYS (System)
- Second Parameter—Name of the parameter: "XUS-XUP VPE"
- Third Parameter—Number of Instances. In this example, you only allow one instance (optional, defaults to 1 if *not* passed).
- Fourth Parameter—Format to return: Use "Q" to get the internal value.
5.  Adding the PARAMETER template with VA FileMan, <u>Figure 34</u>:

<span id="_Ref477870128" class="anchor"></span>Figure 34: Adding a Sample Parameter Template

Select PARAMETER DEFINITION NAME: <span class="mark">XUS-XUP VPE \<Enter\></span> Drop into VPE

NAME: XUS-XUP VPE// <span class="mark">\<Enter\></span>

DISPLAY TEXT: Drop into VPE// <span class="mark">\<Enter\></span>

MULTIPLE VALUED: No// <span class="mark">\<Enter\></span>

INSTANCE TERM: <span class="mark">\<Enter\></span>

VALUE TERM: <span class="mark">\<Enter\></span>

PROHIBIT EDITING: <span class="mark">\<Enter\></span>

VALUE DATA TYPE: yes/no// <span class="mark">\<Enter\></span>

VALUE DOMAIN: <span class="mark">\<Enter\></span>

VALUE HELP: Should XUP drop the user into the VPE environment.

VALUE VALIDATION CODE: <span class="mark">\<Enter\></span>

VALUE SCREEN CODE: <span class="mark">\<Enter\></span>

INSTANCE DATA TYPE: <span class="mark">\<Enter\></span>

INSTANCE DOMAIN: <span class="mark">\<Enter\></span>

INSTANCE HELP: <span class="mark">\<Enter\></span>

INSTANCE VALIDATION CODE: <span class="mark">\<Enter\></span>

INSTANCE SCREEN CODE: <span class="mark">\<Enter\></span>

DESCRIPTION:

1\> This parameter controls if a user when exiting XUP is dropped into

2\> VPE or right to the "\>" prompt.

EDIT Option: <span class="mark">\<Enter\></span>

Select PRECEDENCE: 2// <span class="mark">\<Enter\></span>

PRECEDENCE: 2// <span class="mark">\<Enter\></span>

ENTITY FILE: SYSTEM// <span class="mark">\<Enter\></span>

Select PRECEDENCE: <span class="mark">\<Enter\></span>

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-toolkit-user-guide/021.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-toolkit-user-guide/022.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-toolkit-user-guide/023.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.