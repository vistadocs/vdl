---
title: ROR*1.5*34 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: null
app_code: ROR
app_name: 'Registry: Clinical Case (CCR)'
section: CLI
app_status: archive
pkg_ns: ROR
patch_ver: 1.5
patch_id: ROR*1.5*34
group_key: ROR:ROR:1.5
file_numbers:
- '12'
- '50.6'
- '798.1'
- '798.2'
- '798.5'
- '798.9'
- '799.31'
- '799.51'
security_keys:
- ROR VA IRM
menu_options: 12
description: This Clinical Case RegistriesInstallation and Implementation Guide provides assistance for installation and implementation of the Clinical Case Registries (CCR) software.
audience: System administrators performing installation
keywords: []
page_count: 0
word_count: 12321
section_count: 14
table_count: 10
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: March 2019
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries_Archive/ror1_5_34ig.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries_Archive/ror1_5_34ig.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=419
audit_applied: '2026-05-31'
master_source: ROR*1.5*34 Installation Guide
master_pub_date: March 2019
consolidated_from: 13 versions
prior_versions:
- ROR*1.5*30 Installation Guide
- ROR*1.5*31 Installation Guide
- ROR*1.5*32 Installation Guide
- ROR*1.5*33 Installation Guide
- ROR*1.5*35 Installation Guide
- ROR*1.5*36 Installation Guide
- ROR*1.5*37 Installation Guide
- ROR*1.5*38 Installation Guide
- ROR*1.5*39 Installation Guide
- ROR*1.5*40 Installation Guide
- ROR*1.5*41 Installation Guide
- ROR*1.5*42 Installation Guide
consolidated_title: installation guide
---

> Clinical Case Registries (CCR)Version 1.5

![](ror-1-5-34-installation-guide/001.png)

Installation and Implementation Guide

Documentation Revised March 2019

For Patch ROR\*1.5\*34<span class="mark">  
</span>

Revision History

<table>
<caption><p><span id="_Ref233443442" class="anchor"></span>Table 1 – Typographical Conventions</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 39%" />
<col style="width: 24%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March, 2019</td>
<td>Final release for Patch ROR*1.5*34. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>July, 2018</td>
<td>Final release for Patch ROR*1.5*33. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>April, 2018</td>
<td>Final release for Patch ROR*1.5*32. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>November, 2017</td>
<td>Final release for Patch ROR*1.5*31. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>May, 2017</td>
<td>Final release for Patch ROR*1.5*30. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>December, 2016</td>
<td>Final release for Patch ROR*1.5*29. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>Harris Project Manager</p>
<p>Software QA Analyst</p>
<p>M Developer</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>May, 2016</td>
<td>Final release for Patch ROR*1.5*28. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software QA Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>November, 2015</td>
<td>Final release for Patch ROR*1.5*26. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>Harris Project Manager</p>
<p>M Developer</p>
<p>PMO Support</p></td>
</tr>
<tr class="odd">
<td>June, 2015</td>
<td>Final release for Patch ROR*1.5*26. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>Harris Project Manager</p>
<p>M Developer</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>June, 2015</td>
<td>Final release for Patch ROR*1.5*25. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>April, 2015</td>
<td>Final release for Patch ROR*1.5*27. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>October, 2014</td>
<td>Final release for Patch ROR*1.5*24. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>August, 2014</td>
<td>Final release for Patch ROR*1.5*22. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="even">
<td>April, 2014</td>
<td>Final release for Patch ROR*1.5*21. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>March, 2013</td>
<td>Final release for Patch ROR*1.5*20. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p>
<p>Tech Writer</p></td>
</tr>
<tr class="even">
<td>August, 2014</td>
<td>Final release for Patch ROR*1.5*19. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>VA Project Manager</p>
<p>HP Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p>
<p>Tech Writer</p></td>
</tr>
<tr class="odd">
<td>August, 2012</td>
<td>Final release for Patch ROR*1.5*19. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p>
<p>Tech Writer</p></td>
</tr>
<tr class="even">
<td>April, 2012</td>
<td>Final release for Patch ROR*1.5*17. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p>
<p>Tech Writer</p></td>
</tr>
<tr class="odd">
<td>September, 2011</td>
<td>Final release for Patch ROR*1.5*15. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p>
<p>Tech Writer</p></td>
</tr>
<tr class="even">
<td>March 2011</td>
<td>Patch ROR*1.5*14. See <em>CCR User Manual</em> for details of enhancements to application.</td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Technical Writer</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p>
<p>Delphi Developer</p></td>
</tr>
<tr class="odd">
<td>September, 2010</td>
<td><p>Updated for Patch ROR1.5*13. See <em>CCR User Manual</em> for details of changes to application.</p>
<p><em>Documentation Change only:</em> Previous references to manual data back pulling have been removed. This process is now automated.</p></td>
<td><p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p>
<p><mark>REDACTED</mark></p></td>
<td><p>Project Manager</p>
<p>Delphi Developer</p>
<p>M Developer</p>
<p>Software Quality Assurance Analyst</p></td>
</tr>
<tr class="even">
<td>April, 2010</td>
<td>Final release for Patch ROR*1.5*10. Added instructions for data Backpull; general updates per comments received; general formatting changes.</td>
<td><mark>REDACTED</mark></td>
<td>Technical Writer</td>
</tr>
</tbody>
</table>

<span id="_Ref233443442" class="anchor"></span>Table 1 – Typographical Conventions

Table of Contents

List of Tables

List of Figures

# <span class="mark">Note on Windows 10</span>


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [<span class="mark">Note on Windows 10</span>](#span-classmarknote-on-windows-10span)
- [Introduction](#introduction)
  - [How CCR Works](#how-ccr-works)
  - [Recommended Users](#recommended-users)
  - [Related Documents](#related-documents)
  - [Typographical Conventions Used in the Guide](#typographical-conventions-used-in-the-guide)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [VistA Documentation on the Intranet](#vista-documentation-on-the-intranet)
- [Installing Current CCR 1.5](#installing-current-ccr-15)
- [Installing the Current M Patch](#installing-the-current-m-patch)
- [Installing the Graphical User Interface](#installing-the-graphical-user-interface)
  - [Background Information](#background-information)
  - [Uninstalling Older Software Versions](#uninstalling-older-software-versions)
  - [Installing New GUI](#installing-new-gui)
  - [Configuring Desktop Application Parameters](#configuring-desktop-application-parameters)
  - [Command-Line Switches](#command-line-switches)
- [Special Installation Instructions](#special-installation-instructions)
- [APPENDIX A](#appendix-a)
  - [Back out and Rollback Procedures](#back-out-and-rollback-procedures)
- [Glossary](#glossary)
Currently, the Clinical Case Registries (CCR) application help does NOT work on Windows 10. The issue is being addressed and help will be available in the next patch, ROR\*1.5\*35. In the meantime, please consult the *CCR User Manual* for assistance.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *Clinical Case RegistriesInstallation and Implementation Guide* provides assistance for installation and implementation of the Clinical Case Registries (CCR) software.

## How CCR Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR software application collects data on the population of veterans with certain clinical conditions, namely [Hepatitis C](#Glos_HepatitisC) and/or [Human Immunodeficiency Virus (HIV)](#Glos_HIV) infections at the local and national level as well as 47 local, generic registries. Patients are identified by the existence of a disease-related [International Statistical Classification of Diseases and Related Health Problems, ninth edition (ICD-9)](#Glos_ICD9) or [International Statistical Classification of Diseases and Related Health Problems, tenth edition (ICD-10)](#Glos_ICD10) code or by a positive result on an antibody test. Such patients are added to the registry in a pending state. Pending patients are reviewed by the [local registry](#Glos_LocalRegistry) coordinator and if the data confirm the diagnosis, the local registry coordinator confirms the patient in the registry.

Each night a background process transmits a set of predefined data via [Health Level 7](#Glos_HL7) ([HL7](#Glos_HL7)) message to the national CCR database at the [Corporate Data Center Operations](#Glos_CDCO) (CDCO). Data from both the Hepatitis C and HIV registries are aggregated in the same message. If there is more new data than is allowed by the registry parameter for a single CCR HL7 batch message (the current limit is 5 megabytes), the software will send several messages during a single night. The CCR software creates a limited set of database elements to be stored locally in the [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) ([VistA](#Glos_VistA) ) system, and focuses on assuring that the local listing is complete and accurate, that the desired data elements are extracted, and that data elements are appropriately transmitted to the national database.

Data from the registries is used for both clinical and administrative reporting on both a local and national level. Each facility can produce local reports which show information related to patients seen in their system. Reports from the national database are used to monitor clinical and administrative trends, including issues related to patient safety, quality of care and disease evolution across the national population of patients.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [Information Resource Management](#Glos_IRM) (IRM) staff and CCR [Automated Data Processing Application Coordinator](#Glos_ADPAC) ([ADPAC](#Glos_ADPAC)) are required for the installation of CCR.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- *Clinical Case Registries Release Notes*
- *Clinical Case Registries Technical Manual/Security Guide*
- *Clinical Case Registries User Manual*

## Typographical Conventions Used in the Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fonts and other conventions shown in Table 1 are used throughout this document. Conventions for the use of graphic icons and other symbols are shown in Table 2. Also see Screen Displays and Text Notes for explanations of how computer dialogs are presented.

| Font                           | Used for…                                                        | Examples:                                                                                                                  |
|--------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or address                         | [xxx.xxx.xxx](xxx.xxx.xxx)                                                                                                 |
| Green text, dashed underlining | Hyperlink to a place in this document                            | "CCR accesses several other [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) (VistA) files…" |
| Courier New                    | Patch names                                                      | ROR\*1.5\*2                                                                                                                |
|                                | VistA menu options                                               | "On the PackMan menu, use the INSTALL/CHECK MESSAGE option."                                                               |
|                                | VistA filenames                                                  | XYZ file \#798.1                                                                                                           |
|                                | VistA field names                                                | COMMENT field (#12).                                                                                                       |
| Franklin Gothic Demi bold  | Keyboard keys and on-screen button text                          | \< F1 \>, \< Alt \>, \< L \>, \< Enter \>, \[Delete\] button                                                               |
| Microsoft Sans Serif           | Software Application names                                       | Clinical Case Registries (CCR)                                                                                             |
|                                | Registry names                                                   | CCR:HIV                                                                                                                    |
|                                | [GUI](#Glos_GUI) database field names                            | Comment field                                                                                                              |
|                                | [GUI](#Glos_GUI) report names                                    | Procedures report                                                                                                          |
| Microsoft Sans Serif bold      | [GUI](#Glos_GUI) panel, pane, tab, button and command icon names | Other Registries panel                                                                                                 |
| Times New Roman                | Normal text                                                      | "… designed for use by designated Registry Coordinators, Managers, and Clinicians…."                                       |
| Times New Roman Italic         | Text emphasis                                                    | "It is *very* important…"                                                                                                  |
|                                | National and International Standard names                        | *International Statistical Classification of Diseases and Related Health Problems*                                         |
|                                | Document names                                                   | *Clinical Case RegistriesUser Manual*                                                                                   |

<span id="_Ref233443489" class="anchor"></span>Table 2 – Graphical Conventions

| Graphic                                                                                                                                                                             | Used for…                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ![](ror-1-5-34-installation-guide/002.png)                                | Information of particular interest regarding the current subject matter |
| ![](ror-1-5-34-installation-guide/003.png)                                               | A tip or additional information that may be helpful to the user         |
| ![](ror-1-5-34-installation-guide/004.png) | A warning concerning the current subject matter                         |
| ![](ror-1-5-34-installation-guide/005.png)                    | A guide to which action is to be performed next                         |

<span id="_Ref233529382" class="anchor"></span>Table 3 – Software and Documentation Sources

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this guide, user responses are shown in bold type, but do not appear on the screen as bold. The bold part of the entry is the letter, or letters, that you must type so that the computer can identify the response. In most cases, you only have to enter the first few letters. This increases speed and accuracy.

In [VistA](#Glos_VistA), every response you type must be followed by pressing the \< Return \> key (or \< Enter \> for some keyboards). In VistA screen shots, whenever this key should be pressed, you will see the symbol \<RET\>. This symbol is not shown but is implied if there is bold input.

Within the "roll'n'scroll" part of the system, Help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, or ???).

Within the examples of actual terminal dialogues, additional information about the dialogue may be shown. This information is enclosed in brackets, for example, *{type ward name here},* and it does not appear on the screen.

Computer dialogues appear in Courier font.

Where [graphical](#Glos_GUI) [interface](#Glos_Interface) windows are mentioned, and the user is instructed to click an on-screen button, that button will be shown in Franklin Gothic Demi bold font enclosed in square brackets and/or with a graphic symbol. Example: "Click the \[Submit\] button" or "Click the ![](ror-1-5-34-installation-guide/006.png) button."

All headings and text in this guide are intentionally formatted flush left, regardless of the heading level, to save space and to make for better readability.

In tables which list mandatory steps (as for installation or un-installation), a column is provided at the right-hand side so that users may check () off the step as it is performed.

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Both the CCR 1.5 software distributives and documentation files are available for downloading from the following Office of Information Field Office (OIFO) \[ANONYMOUS SOFTWARE\] directory.

| OIFO       | FTP Address                    | Directory      |
|----------------|------------------------------------|--------------------|
| Hines          | <span class="mark">REDACTED</span> | anonymous.software |
| Salt Lake City | <span class="mark">REDACTED</span> | anonymous.software |

<span id="_Ref234654654" class="anchor"></span>Table 4 – Files Included in Distribution

The ROR\*1.5\*34 (CCR 1.5.34) software and accompanying guides and manuals are distributed as the set of files shown in Table 4. No distribution is being made for the original CCR 1.5 versions. Since some sites may need to access both sets of documents during an interim period, the original CCR 1.5 versions of the documentation will remain available on the [VistA Document Library](#Glos_VDL) ([VDL](#Glos_VDL)) at <http://www.va.gov/vdl/application.asp?appid=126>.

<table>
<caption><p><span id="_Ref234810655" class="anchor"></span>Table 5 – Current CCR 1.5 Patches</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 57%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Contents</strong></th>
<th><strong>Retrieval Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR1_5P34GUI.ZIP</td>
<td><p>Zipped GUI distributive</p>
<p>► CCRSETUP.EXE</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>ROR1_5P34DOC1.ZIP</td>
<td><p>Zipped DOC distributive, which includes both .PDF and .DOCX formats:</p>
<p>► User Manual (ROR1_5_34UM)</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>ROR1_5P34DOC2.ZIP</td>
<td><p>► Installation and Implementation Guide (ROR1_5_34IG)</p>
<p>► Technical Manual / Security Guide (ROR1_5_34TM)</p>
<p>► Release Notes (ROR1_5_34RN)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

<span id="_Ref234810655" class="anchor"></span>Table 5 – Current CCR 1.5 Patches

## VistA Documentation on the Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is available in the VDL. Clinical Case Registries documentation may be found at <http://www.va.gov/vdl/application.asp?appid=126>.

For additional information about the CCR, access the CCR Home Page at the following address: [<span class="mark">REDACTED</span>](file:///C:\Data\VDL_Work\P37\xxx.xxx.xxx).

# Installing Current CCR 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-34-installation-guide/007.png) | Important Note: This patch requires an M patch and a revised Graphical User Interface (GUI) application. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|

<span id="_Toc197844" class="anchor"></span>Table 6 – M Code Installation Instructions

Installing CCR 1.5 current version is a two-step process:

- Installing the Current M Patch
- Installing the Graphical User Interface

<table>
<caption><p><span id="_Ref234283937" class="anchor"></span>Table 7 – Uninstalling Previous GUI Versions</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-34-installation-guide/008.png)</th>
<th><p><strong>Note:</strong> The M routines included in KIDS build ROR 1.5 are listed in the <em>CCR Technical Manual</em>. The second line of each of these routines now looks like:</p>
<p>;;1.5;CLINICAL CASE REGISTRIES;[Patch List];Feb 17, 2006;Build [NN]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref234283937" class="anchor"></span>Table 7 – Uninstalling Previous GUI Versions

# Installing the Current M Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">Please review the section entitled Special Installation Instructions prior to installing the patch.</span>

All CCR patches are available via the National Patch Tracking module in FORUM. All patches contain installation instructions and must be installed in sequence number order. Current patches to CCR 1.5 are listed in Table 5. Please be sure that all previous patches are installed before attempting to install the latest patch. Note that the latest patch is shown at the top of the table.

<table>
<caption><p><span id="_Ref234561281" class="anchor"></span>Table 8 – Installing New GUI</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 74%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>Patches</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR*1.5*34</td>
<td>6 enhancements, 2 fixes. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*33</td>
<td>4 enhancements, 1 modification and 1 fix. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*32</td>
<td>4 enhancements, 1 modification and 4 fixes. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*31</td>
<td>5 enhancements, 2 modifications and 4 fixes. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*30</td>
<td>6 enhancements, 1 fix. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*29</td>
<td>9 enhancements. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*28</td>
<td>6 enhancements, 4 fixes. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*26</td>
<td>9 enhancements, 1 fix. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*27</td>
<td>2 enhancements, 4 modifications and 5 fixes. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*25</td>
<td>3 enhancements and 1 modification. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*24</td>
<td>6 enhancements and 1 fix. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*22</td>
<td>6 enhancements and 2 modifications. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*21</td>
<td>10 enhancements. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*20</td>
<td>1 enhancement. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*19</td>
<td>6 enhancements and 2 modifications. See <em>CCR Release Notes</em>.</td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*18</td>
<td>8 enhancements, 7 modifications and 1 fix. See <em>CCR Release Notes</em>.</td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*17</td>
<td>5 enhancements, 3 modifications and 3 fixes. See <em>CCR Release Notes</em>.</td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*15</td>
<td>9 enhancements, 5 modifications and 2 fixes. See <em>CCR Release Notes</em>.</td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*14</td>
<td>10 enhancements. See <em>CCR Release Notes</em>.</td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*13</td>
<td>1 modification; 1 fix; 8 enhancements. See <em>CCR Release Notes.</em></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*10</td>
<td>5 modifications; 2 fixes; 11 enhancements. See <em>CCR Technical Manual.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*9</td>
<td>Maintenance bug fixes</td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*8</td>
<td>1 fix; 9 enhancements. See <em>CCR Technical Manual.</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*7</td>
<td>1 enhancement: Added generic drug ETRAVIRINE to VA GENERIC file #50.6.</td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*6</td>
<td>1 enhancement: Added generic drug RALTEGRAVIR to VA GENERIC file #50.6.</td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*5</td>
<td><p>1 fix: Resolved issue with Procedures w/o Provider not being sent to <a href="#Glos_AAC">AAC</a>.</p>
<p>1 enhancement: Added drug needed for nightly registry update and <a href="#Glos_DataExtraction">data extraction</a>.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*4</td>
<td>1 enhancement: Added two <a href="#Glos_ICD9">ICD-9</a> codes.</td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*3</td>
<td>2 enhancements: Added Reason for Study data field; added task Control flag.</td>
<td></td>
</tr>
<tr class="odd">
<td>ROR*1.5*2</td>
<td>7 fixes: See <em>CCR Technical Manual</em></td>
<td></td>
</tr>
<tr class="even">
<td>ROR*1.5*1</td>
<td>14 enhancements: See <em>CCR Technical Manual</em></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref234561281" class="anchor"></span>Table 8 – Installing New GUI

Below is a summary of the steps required to install this patch; installation will not take more than five minutes.

This patch can be installed with VistA users online, but Registry users should be logged out of the CCR Registry Application, as a new GUI is to be installed.

| ![](ror-1-5-34-installation-guide/009.png) | Important Note: The nightly task (the \[ROR TASK\] option) must *not* be running during the installation.. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|

<span id="_Ref267557125" class="anchor"></span>Table 9 – Installing New GUI on a File Server

| ![](ror-1-5-34-installation-guide/010.png) | Important Note: TaskMan does *not* need to be STOPPED or placed in a WAIT state. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|

<span id="_Ref234284193" class="anchor"></span>Table 10 – Command Line Switches

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 69%" />
<col style="width: 15%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th colspan="3"><strong>Description</strong></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td colspan="3">Check the user who scheduled the nightly job, ROR TASK. The task must be scheduled by an active user with the ROR VA IRM security key. If the user has been terminated or no longer has the key, make sure the job is removed and re-scheduled by a qualified user.</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td colspan="3"><p>Make sure you have the ROR VA IRM security key. The install cannot be run without the user having this key.</p>
<p>As mentioned the ROR*1.5*34 M code is distributed as a PACKMAN mail message. To access the PACKMAN, read the mailman message.</p>
<p>At the prompt: Enter message action (in IN basket): Ignore// [Type X]<br />
This will drop the user into the Packman option menu.</p></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td colspan="3">On the PackMan menu, use the INSTALL/CHECK MESSAGE option. This option loads the patch into a Transport Global on your system and will run an environment check routine.</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td colspan="3">Exit the Mailman options and access the Kernel Installation and Distribution System (XPD MAIN) menu, select the Installation menu.</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td colspan="3">From this menu, you may elect to use the following options (when prompted for INSTALL NAME, enter <strong>ROR*1.5*34</strong>):</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>a</strong></td>
<td>Verify Checksums in Transport Global: This option will allow you to ensure the integrity of the routines that are in the transport global. Routines are listed in the <em>CCR Technical Manual</em> and the Patch Description.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>b</strong></td>
<td>Print Transport Global: This option will allow you to view the components of the KIDS build.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>c</strong></td>
<td>Compare Transport Global to Current System: This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, Data Dictionaries (DD's), templates, etc.).</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>d</strong></td>
<td>Backup a Transport Global: This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td colspan="3"><p>Select the KIDS option: Install Package (s)<br />
Select Installation &lt;TEST ACCOUNT&gt; Option: 6 Install Package(s)</p>
<p>Select INSTALL NAME: ROR*1.5*34 1/8/19@13:12:16</p>
<p>=&gt; ROR*1.5*34</p>
<p>This Distribution was loaded on Jan 08, 2019@13:12:16 with header of</p>
<p>ROR*1.5*34</p>
<p>It consisted of the following Install(s):</p>
<p>ROR*1.5*34</p>
<p>Checking Install for Package ROR*1.5*34</p>
<p>Will first run the Environment Check Routine, RORP034</p>
<p>Install Questions for ROR*1.5*34</p>
<p>Incoming Files:</p>
<p>798.1 ROR REGISTRY PARAMETERS (including data)</p>
<p>Note: You already have the 'ROR REGISTRY PARAMETERS' File.</p>
<p>I will OVERWRITE your data with mine.</p>
<p>798.2 ROR SELECTION RULE (including data)</p>
<p>Note: You already have the 'ROR SELECTION RULE' File.</p>
<p>I will OVERWRITE your data with mine.</p>
<p>799.31 ROR XML ITEM (including data)</p>
<p>Note: You already have the 'ROR XML ITEM' File.</p>
<p>I will OVERWRITE your data with mine.</p>
<p>799.51 ROR GENERIC DRUG (including data)</p>
<p>Note: You already have the 'ROR GENERIC DRUG' File.</p>
<p>I will OVERWRITE your data with mine.</p>
<p>Maximum number of registry update subtasks: (0-10): 5//</p>
<p>Suspend the post-install during the peak hours ? NO//</p>
<p>Date/Time to run the new registry initialize task: 1/8/19@13:15//</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td colspan="3">When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond "<strong>NO</strong>".</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td colspan="3">When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond "<strong>NO</strong>".</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td colspan="3"><p>Enter the Device you want to print the Install message.</p>
<p>You can queue the install by entering a 'Q' at the device prompt.</p>
<p>Enter '^' to abort the install.</p>
<p>DEVICE: HOME// ;;9999 TELNET PORT</p>
<p>--------------------------------------------------------------------------------</p>
<p>Install Started for ROR*1.5*34 :</p>
<p>Jan 8, 2019@13:17:54</p>
<p>Build Distribution Date: Jan 08, 2019</p>
<p>Installing Routines:</p>
<p>Jan 8, 2019@13:17:54</p>
<p>Running Pre-Install Routine: PRE^RORP034</p>
<p>Verifying installing user has the ROR VA IRM security key</p>
<p>User has the ROR VA IRM key - OK to install</p>
<p>* Checking to be sure ROR INITIALIZE task is not already running</p>
<p>* Checking to be sure ROR TASK is not running</p>
<p>Installing Data Dictionaries:</p>
<p>Jan 08, 2019@13:17:55</p>
<p>Installing Data: ..</p>
<p>Jan 08, 2019@13:17:56</p>
<p>Installing PACKAGE COMPONENTS:</p>
<p>Installing DIALOG</p>
<p>Jan 08, 2019@13:17:56</p>
<p>Running Post-Install Routine: POST^RORP034</p>
<p>POST INSTALL START</p>
<p>&gt;&gt; Adding new LOINC codes to the VA HIV registry parameters</p>
<p>&gt;&gt; Step complete</p>
<p>&gt;&gt; Adding new Future Appointments panel to reports</p>
<p>&gt;&gt; Step complete</p>
<p>Checking VA GENERIC drug file.. COBICISTAT/DARUNAVIR/EMTRICITABINE/TENOFOVIR AF</p>
<p>&gt;&gt; Step complete</p>
<p>&gt;&gt; Adding CPT and ICD-9 procedures to ROR ICD SEARCH file for new registries</p>
<p>&gt;&gt; Step complete</p>
<p>Updating List Items for new registries</p>
<p>&gt;&gt; Step complete</p>
<p>&gt;&gt; Initiating background job to set up registries added with this patch</p>
<p>* Checking for registry(s) to be initialized</p>
<p>The following registry(s) will be populated with new patients:</p>
<p>VA ILD</p>
<p>VA LYMPHOMA</p>
<p>VA NASH</p>
<p>* Storing registry setup parameters</p>
<p>=============================================</p>
<p>Number of registry update (sub)tasks... 5</p>
<p>Suspend the tasks during peak hours.... No</p>
<p>=============================================</p>
<p>The scheduled task number is 2632693</p>
<p>&gt;&gt; Step complete</p>
<p>Updating the Drug matching entries...</p>
<p>Tasking nightly job to gather drug matching...</p>
<p>POST INSTALL COMPLETE</p>
<p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>ROR*1.5*34 Installed.</p>
<p>Jan 08, 2019@13:18:07</p>
<p>Not a production UCI</p>
<p>ROR*1.5*34</p>
<p>Install Completed</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>10</strong></td>
<td colspan="3"><p>The post-initialization routine for this patch will:</p>
<p>- Schedule the Initialize new registries (one time) [ROR</p>
<p>INITIALIZE] task to run. This task sets up and populates the 3</p>
<p>new registries added with this patch.</p>
<ul>
<li><p>Take note of the task # for this job as you will need it later</p></li>
<li><p>Updates data in the following files:</p></li>
</ul>
<blockquote>
<p>ROR REGISTRY PARAMETERS (#798.1)</p>
<p>ROR SELECTION RULE (#798.2)</p>
<p>ROR ICD SEARCH (#798.5)</p>
<p>ROR LAB SEARCH (#798.9)</p>
<p>ROR XML ITEM (#799.31)</p>
<p>ROR GENERIC DRUG (#799.51)</p>
</blockquote>
<p>You will need to periodically check the status of the Schedule the Initialize new registries (one time) [ROR INITIALIZE] task from above.</p>
<p>When this job has completed successfully, check the Registry Update &amp; Data Extraction [ROR TASK] option. If it was not automatically rescheduled by the post-installation, then reschedule it manually.</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

| ![](ror-1-5-34-installation-guide/011.png) | GO TO: Installing the Graphical User Interface |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|

# Installing the Graphical User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Background Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The current CCR [Graphical User Interface](#Glos_GUI) ([GUI](#Glos_GUI)) provides access to both the [Hepatitis C](#Glos_HepatitisC) and [HIV](#Glos_HIV) registries and all local registries.
- It is *strongly recommended* that the CCR GUI be installed on a file server and the CCR application be made available to the CCR users via the [Computerized Patient Record System](#Glos_CPRS) ([CPRS](#Glos_CPRS)) Tools menu. Installing the CCR GUI on workstations is *not recommended*.

| ![](ror-1-5-34-installation-guide/012.png) | Important Note: If you install the Clinical Case Registries (CCR) application on your GFE (*not recommended*), you <u>must</u> have administrator rights on your GFE to execute the CCR installation program (CCRSetup.exe). You should also disable the Host Intrusion Prevention Software (HIPS) software if it exists on your GFE. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Access to the registries is controlled by the [security key](#Glos_SecurityKeys)s within VistA.
- For users who have access to a single registry, its window will be opened automatically by the GUI. Users who have access to multiple registries will be able to select a registry from a list.
- The GUI supports the /NOCCOW command-line parameter that completely disables the [CCOW](#Glos_CCOW) functionality. It also supports the parameter /CCOW=PatientOnly, which disables only the [Single Sign-On](#Glos_SingleSignOn)/User Context (SSO/UC) functionality.

## Uninstalling Older Software Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are doing a first-time installation: There should not be any old software to be uninstalled. If you don't know whether old software is present, use the uninstall procedure in Table 7 just to be sure! If you are certain that no previous GUI software has been installed, you may skip to section 4.3 on page 15.

If you are doing an upgrade: To eliminate any chance for errors, it is *strongly recommended* that any older versions be uninstalled using the instructions in Table 7.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 85%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th><strong>Description</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td>From the <strong>Start</strong> menu, select <strong>Settings</strong>, then <strong>Control Panel</strong>.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><p>![](ror-1-5-34-installation-guide/013.png) Click the <strong>Programs and Features</strong> icon. If you are not using Windows 7, the icon you see may vary.</p>
<p>The <strong>Uninstall or change a program</strong> dialog appears:</p>
<p>![](ror-1-5-34-installation-guide/014.png)</p>
<p><span id="_Toc197849" class="anchor"></span>Figure 1 – Uninstall button</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>2a</strong></td>
<td><p>Look for any entries that include Clinical Case Registries 1.5* (or simply 1.5*) on the program list. If neither of these appears on the program list, skip to Step 7.</p>
<p>Note that releases of the GUI up until 1/13/2010 were shown simply as "1.5.xx" on the program list; following installation of the 1/13/2010 version, it will correctly display on the list as "Clinical Case Registries 1.5.xx."</p>
<p>![](ror-1-5-34-installation-guide/015.png) Select Clinical Case Registries from the list and click the [Uninstall] button at the top of the screen.</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>![](ror-1-5-34-installation-guide/016.png) If prompted, click the [Next] button.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td><p>You will likely see a pop-up, asking you to confirm removal:</p>
<p>![](ror-1-5-34-installation-guide/017.png)</p>
<p><span id="_Toc197850" class="anchor"></span>Figure 2 – Uninstall Confirmation</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td>![](ror-1-5-34-installation-guide/018.png) Confirm the uninstall action by clicking the [Yes] or [OK] button.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>![](ror-1-5-34-installation-guide/019.png) Wait until the Uninstall Wizard completes the removal and then click the [Finish] button.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>Close the <strong>Add or Remove Programs</strong> window and the <strong>Control Panel</strong> window.</td>
<td></td>
</tr>
</tbody>
</table>

## Installing New GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download (see 1.6 above) and install the new [GUI](#Glos_GUI) using the instructions in Table 8.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 86%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th><strong>Description</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td>Download and unzip the ROR1_5P34GUI.ZIP into a temporary directory.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><p>Open the temporary directory and run (double-click) CCRSetup.exe to begin the installation.</p>
<p><strong>Important Note:</strong> You <strong><u>must</u></strong> have administrator rights on the application server to execute the installation program (CCRSetup.exe).</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td><p>Wait until the setup wizard prepares the setup procedure. A welcome message displays:</p>
<p>![](ror-1-5-34-installation-guide/020.png)</p>
<p><span id="_Toc197851" class="anchor"></span>Figure 3 – Setup Wizard Start</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td><p>![](ror-1-5-34-installation-guide/021.png) Click [<u>N</u>ext] to continue the installation.</p>
<p>The Select Destination Location dialog displays:</p>
<p>![](ror-1-5-34-installation-guide/022.png)</p>
<p><span id="_Toc197852" class="anchor"></span>Figure 4 – Setup Wizard Directory Confirmation</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td><p>Select the directory in which to install the CCR GUI. We recommend that you accept the default directory: C:\Program Files (x86)\VistA\Clinical Case Registries\.</p>
<p>![](ror-1-5-34-installation-guide/023.png) To select a different location, click [Browse…] and select the directory.</p>
<p>![](ror-1-5-34-installation-guide/024.png) Click [Next] to continue the installation.</p>
<p>The Select Start Menu Folder dialog displays:</p>
<p>![](ror-1-5-34-installation-guide/025.png)</p>
<p><span id="_Toc197853" class="anchor"></span>Figure 5 – Select Start Menu Folder</p></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><strong>6</strong></td>
<td><p>We recommend that you accept the default directory: Clinical Case Registries.</p>
<p>![](ror-1-5-34-installation-guide/026.png) To select a different location, click [Browse…] and select the directory.</p>
<p>![](ror-1-5-34-installation-guide/027.png) Click [Next] to continue the installation.</p></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td><p>The Select Additional Tasks dialog appears:</p>
<p>![](ror-1-5-34-installation-guide/028.png)</p>
<p><span id="_Toc197854" class="anchor"></span>Figure 6 – Select Additional Tasks</p></td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td><p>If you want a desktop icon, leave the checkbox checked; otherwise, clear the checkbox.</p>
<p>![](ror-1-5-34-installation-guide/029.png) Click [Next] to continue the installation.</p>
<p>The Ready to Install dialog displays:</p>
<p>![](ror-1-5-34-installation-guide/030.png)</p>
<p><span id="_Toc197855" class="anchor"></span>Figure 7 – Ready to Install</p></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><strong>8</strong></td>
<td><p>![](ror-1-5-34-installation-guide/031.png) Review the installation settings and click [Install] to proceed.</p>
<p>The Wizard finishes the installation and a confirmation screen displays:</p></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><p>![](ror-1-5-34-installation-guide/032.png)</p>
<p><span id="_Toc197856" class="anchor"></span>Figure 8 – Installation Confirmation</p></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td>![](ror-1-5-34-installation-guide/033.png) Click [Finish].</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-34-installation-guide/034.png)</th>
<th><p><strong>If you installed the CCR GUI on a file server (recommended):</strong></p>
<p>Continue with Table 9 immediately below.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p><strong>If you installed the CCR GUI on user workstations (not recommended):</strong></p>
<p>Continue with 4.4 on page 23.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 85%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th><strong>Description</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"><strong>10</strong></td>
<td><p><strong>If you installed the CCR GUI on a file server (recommended):</strong></p>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-34-installation-guide/035.png)</th>
<th><strong>Note:</strong> If you have previously set up the CPRS Tools menu (as for a previous version of CCR), you should not have to perform this step. Go to the <a href="#EndNote">End Note</a> on page <a href="#EndNote">26</a>.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Add the corresponding item to the CPRS Tool menu using the CPRS GUI Tools Menu [ORW TOOL MENU ITEMS] option.</p>
<p>It is recommended that you add the item at "User" level.</p>
<p>If you used the default directory for the installation, the "Name=Command" parameter should look like this:</p>
<p>Clinical Case Registries="C:\Program Files (x86)\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /S="<em>{Server IP Address}</em>" /P=<em>{RPC Broker Port}</em></p>
<p>Below is a typical configuration example:</p></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td><p>&gt;<strong>D ^XUP</strong></p>
<p>Setting up programmer environment</p>
<p>Terminal Type set to: C-VT320</p>
<p>Select OPTION NAME: <strong>ORW TOOL MENU ITEMS</strong></p>
<p>CPRS GUI Tools Menu may be set for the following:</p>
<p>1 User USR [choose from NEW PERSON]</p>
<p>2 Location LOC [choose from HOSPITAL LOCATION]</p>
<p>2.5 Service SRV [choose from SERVICE/SECTION]</p>
<p>3 Division DIV [HINES DEVELOPMENT]</p>
<p>4 System SYS [DEV.DEV.FO-HINES.MED.VA.GOV]</p>
<p>9 Package PKG [ORDER ENTRY/RESULTS REPORTING]</p>
<p>Enter selection: <strong>1</strong></p>
<p>Select NEW PERSON NAME: <strong>CCRUSER,ONE</strong></p>
<p>------ Setting CPRS GUI Tools Menu for User: CCRUSER,ONE -------</p>
<p>Select Sequence: <strong>10</strong></p>
<p>Are you adding 10 as a new Sequence? Yes// <strong>&lt;RET&gt;</strong></p>
<p>Sequence: 10// <strong>&lt;RET&gt;</strong></p>
<p>Name=Command: Clinical Case Registries="C:\Program Files (x86)\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /S="10.3.29.201" /P=9200</p>
<p>Select Sequence: <strong>&lt;RET&gt;</strong></p></td>
</tr>
<tr class="odd">
<td><p>Please refer to the GUI Tool Menu Items section of the <em>Computerized Patient Record System (CPRS) v1.0 Setup Guide</em> (<a href="http://www.va.gov/vdl/application.asp?appid=61">http://www.va.gov/vdl/application.asp?appid=61</a>) for more details.</p>
<p>You can also use other command-line parameters described in 4.5 below to further customize the menu item (limit access to a single registry, disable <a href="#Glos_CCOW">CCOW</a>, etc.).</p></td>
</tr>
</tbody>
</table>

## Configuring Desktop Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-34-installation-guide/036.png) | Note: Follow these instructions *only* if you elected to install the GUI on user workstations (not recommended). |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|

There are two ways to configure the GUI for those users who are coordinators of both [Hepatitis C](#Glos_HepatitisC) and [HIV](#Glos_HIV) registries:

- Single shortcut: This is the default. A single shortcut is created on the desktop. When the GUI is launched (or when <u>F</u>ile, <u>O</u>pen is selected from the menu), the user selects the desired registry from the list.
- Separate shortcuts: Two separate shortcuts are created, one for the [Hepatitis C](#Glos_HepatitisC) registry and one for the [HIV](#Glos_HIV) registry. A command-line switch in each shortcut allows access only to a single registry. As a result, the registry selection dialog box is not displayed and the corresponding registry is opened automatically. This can be accomplished by adding the /R parameter after the executable name in the Target field of the shortcut. For example:

![](ror-1-5-34-installation-guide/037.png)

<span id="_Toc197857" class="anchor"></span>Figure 9 – Configuring Desktop Parameters

The <u>T</u>arget field should read…

"C:\Program Files (x86)\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /R="VA HEPC"

## Command-Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can get a list of command-line "switches" supported by the CCR GUI by running the application with the /? or /h parameter. For example:

> Start \| Run \| "C:\Program Files (x86)\VistA\Clinical Case Registries\ClinicalCaseRegistries. exe" /?

| ![](ror-1-5-34-installation-guide/038.png) | Note the use of quotation marks around the "target" application name. These are required when using this method because the C:\Program Files (x86)\Vista directory is typically not in the *path* (the list of directories which the operating system searches for executable files). |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-34-installation-guide/039.png)

<span id="_Toc197858" class="anchor"></span>Figure 10 – Command-Line Switches

The switches are also shown in Table 10 for convenience.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Switch</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/?, -?, /h, -h</td>
<td>Show a list of command-line parameters</td>
</tr>
<tr class="even">
<td>/at, -at</td>
<td>Turn assistive technology mode ON for non-JAWS users</td>
</tr>
<tr class="odd">
<td>/debug, -debug</td>
<td>Run the application in debug mode</td>
</tr>
<tr class="even">
<td>/noccow, /ccow=off,<br />
-noccow, -ccow=off</td>
<td>Completely disable <a href="#Glos_CCOW">CCOW</a> functionality</td>
</tr>
<tr class="odd">
<td>/patientonly, /ccow=patientonly,<br />
-patientonly,<br />
-ccow=patientonly</td>
<td>Disable user context functionality</td>
</tr>
<tr class="even">
<td>/port=, /p=, P=,<br />
-port=, -p=</td>
<td>Port number of the <a href="#Glos_RPCBroker">Remote Procedure Call Broker</a> (<a href="#Glos_RPC">RPC</a>) listener</td>
</tr>
<tr class="odd">
<td>/registry=, /r=, R=,<br />
-registry=, -r=</td>
<td>Registry name</td>
</tr>
<tr class="even">
<td>/server=, /r=, S=,<br />
-server=, -s=</td>
<td>Server name or IP address of the RPC Broker listener</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="EndNote" class="anchor"></span>![](ror-1-5-34-installation-guide/040.png)</th>
<th><p>Upgrading/installation and implementation are complete. Check documentation for further details. If you have not already downloaded the documentation files, see 1.6 Software and Manual Retrieval on page 4.</p>
<p>You may also find the documentation on the <a href="#Glos_VistA">VistA</a> Documentation Library (VDL) at <a href="http://www.va.gov/vdl/application.asp?appid=126">http://www.va.gov/vdl/application.asp?appid=126</a>.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Special Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Effective with ROR\*1.5\*33 (CCR 1.5.33), the patch pre-installation process will automatically unschedule the Registry Update & Data Extraction \[ROR TASK\] option. This option is a nightly scheduled background job that updates the existing registries. CCR patches should not be installed while the ROR TASK background job is running. Prior to ROR\*1.5\*33, the installation instructions in each patch description directed the installer to manually unschedule the ROR TASK job before installing the patch. Now, the pre-installation process determines whether the ROR TASK background job is running. If it is running or it cannot be unscheduled, the patch installation process will stop and the installer will see a message on their display screen.

The patch post-installation process will populate the new registries that were added. This may take up to one or two days depending on the VistA database size and new registry specifications. When the new registries are built the CCR software will automaticlly reschedule the ROR TASK background job to run again. A MailMan message is sent to the patch installer with a message stating the success or failure of rescheduling the ROR TASK background job.

The benefits of this new functionality are:

1)  Prevents patch installers from accidently installing the patch when the ROR TASK background job is running.
2)  Helps the patch installer who forgets to reschedule the ROR TASK background job after the new registries are populated.

The patch installer may continue to manually check the status of the ROR TASK option before installing any new CCR patches, but now it is not required.

# APPENDIX A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back out and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a "one size fits all." The general strategy for VistA rollback is to repair the code with a follow-on patch. The development team recommends that the sites log a CA SDM ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A more complete glossary is included in the *CCR User Manual*.
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term or Acronym</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AAC</td>
<td><em>See</em> <a href="#Glos_AAC">Austin Automation Center</a></td>
</tr>
<tr class="even">
<td><span id="Glos_AIDS" class="anchor"></span>Acquired Immunodeficiency Syndrome (AIDS)</td>
<td>AIDS is a disease of the human immune system caused by the human immunodeficiency virus (<a href="#Glos_HIV">HIV</a>). This condition progressively reduces the effectiveness of the immune system and leaves individuals susceptible to opportunistic infections and tumors.</td>
</tr>
<tr class="odd">
<td>API</td>
<td><em>See</em> <a href="#Glos_API">Application Programmer Interface</a></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a></td>
</tr>
<tr class="odd">
<td>AIDS</td>
<td><em>See</em> <a href="#Glos_AIDS">Acquired Immunodeficiency Syndrome</a></td>
</tr>
<tr class="even">
<td>AITC</td>
<td><em>See</em> <a href="#Glos_AITC">Austin Information Technology Center</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_API" class="anchor"></span>Application Program Interface (API)</td>
<td><p>The interface (calling conventions) by which an application program accesses operating system and other services. An API is defined at source code level and provides a level of abstraction between the application and the <a href="#Glos_Kernel">kernel</a> (or other privileged utilities) to ensure the portability of the code.</p>
<p>An API can also provide an interface between a high level language and lower level utilities and services which were written without consideration for the calling conventions supported by compiled languages. In this case, the API's main task may be the translation of parameter lists from one format to another and the interpretation of call-by-value and call-by-reference arguments in one or both directions.</p></td>
</tr>
<tr class="even">
<td><span id="Glos_AAC" class="anchor"></span>Austin Automation Center (AAC)</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_AITC" class="anchor"></span>Austin Information Technology Center (AITC)</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="even">
<td><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).</td>
</tr>
<tr class="odd">
<td>CCOW</td>
<td><em>See</em> <a href="#Glos_CCOW">Clinical Context Object Workgroup</a></td>
</tr>
<tr class="even">
<td><span id="Glos_CCOW" class="anchor"></span>Clinical Context Object Workgroup (CCOW)</td>
<td><p>CCOW is an <a href="#Glos_HL7">HL7</a> standard protocol designed to enable disparate applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.</p>
<p>CCOW is the primary standard protocol in healthcare to facilitate a process called "Context Management." Context Management is the process of using particular "subjects" of interest (e.g., user, patient, clinical encounter, charge item, etc.) to 'virtually' link disparate applications so that the end-user sees them operate in a unified, cohesive way.</p>
<p>Context Management can be utilized for both CCOW and non-CCOW compliant applications. The CCOW standard exists to facilitate a more robust, and near "plug-and-play" interoperability across disparate applications.</p>
<p>Context Management is often combined with <a href="#Glos_SingleSignOn">Single Sign-On</a> applications in the healthcare environment, but the two are discrete functions. Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</p></td>
</tr>
<tr class="odd">
<td><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td>A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients' healthcare information. CPRS is the Department of Veteran's Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a <a href="#Glos_GUI">graphical user interface</a> version and a character-based <a href="#Glos_Interface">interface</a> version are available. CPRS provides a single interface for health care providers to review and update a patient's medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="even">
<td><span id="Glos_CDCO" class="anchor"></span>Corporate Data Center Operations (CDCO)</td>
<td>Federal data center within the Department of Veterans Affairs (VA). As a franchise fund, or fee-for-service organization, CDCO-Austin provides cost-efficient IT enterprise solutions to support the information technology needs of customers within the Federal sector. Formerly the Austin Automation Center (AAC); formerly the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="even">
<td>DBIA</td>
<td><em>See</em> <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>File Number—the local/facility patient record number (patient file internal entry number)</td>
</tr>
<tr class="even">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td><strong>M</strong> code is not "compiled and linked," so any code is open to anyone to call. The same is true for the data. This permits an incredible level of integration between applications, but it is "too open" for some software architects' liking. The VA has instituted Database Integration Agreements to enforce external policies and procedures to avoid unwanted dependencies.</td>
</tr>
<tr class="odd">
<td><span id="Glos_DataExtraction" class="anchor"></span>Data Extraction Process</td>
<td>This process is run after the registry update process. This function goes through patients on the <a href="#Glos_LocalRegistry">local registry</a> and, depending on their status, extracts all available data for the patient, since the last extract was run. The extract transmits any collected data for the patient to the national database via <a href="#Glos_HL7">HL7</a>.</td>
</tr>
<tr class="even">
<td>Direct Acting Antiviral (DAA)</td>
<td>A medication that interacts directly with viral proteins to inhibit viral replication.</td>
</tr>
<tr class="odd">
<td><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="even">
<td>FORUM</td>
<td>FORUM is the VA's national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The national patch module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (<em>e.g.,</em> a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.</td>
</tr>
<tr class="odd">
<td><span id="Glos_Globals" class="anchor"></span>Globals</td>
<td><p><a href="#Glos_M">M</a> <em>globals</em> are variables which are intrinsically stored in files and persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the <strong>M</strong> statement…</p>
<p>SET ^A("first_name")="Bob"</p>
<p>…will result in a new record being created and inserted in the file structure, persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as <strong>M</strong> globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of <strong>M</strong> is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common <strong>M</strong> programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. <strong>M</strong> allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="even">
<td><span id="Glos_GUI" class="anchor"></span>Graphical User Interface (GUI)</td>
<td><p>A graphical user interface (or GUI, often pronounced "gooey") is a graphical (rather than purely textual) user interface to a computer. A GUI is a particular case of user interface for interacting with a computer which employs graphical images and widgets in addition to text to represent the information and actions available to the user. Usually the actions are performed through direct manipulation of the graphical elements. A GUI takes advantage of the computer's graphics capabilities to make the program easier to use.</p>
<p><em>Sources:</em></p>
<p><a href="http://en.wikipedia.org/wiki/GUI">http://en.wikipedia.org/wiki/GUI</a></p>
<p><a href="http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html">http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html</a></p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>See <a href="#Glos_GUI">Graphical User Interface</a></td>
</tr>
<tr class="even">
<td><span id="Glos_HL7" class="anchor"></span>Health Level 7 (HL7)</td>
<td>One of several American National Standards Institute (ANSI)–accredited Standards Developing Organizations operating in the healthcare arena. "Level Seven" refers to the highest level of the International Standards Organization's (ISO) communications model for Open Systems Interconnection (OSI)— the application level. The application level addresses definition of the data to be exchanged, the timing of the interchange, and the communication of certain errors to the application. The seventh level supports such functions as security checks, participant identification, availability checks, exchange mechanism negotiations and, most importantly, data exchange structuring. HL7 focuses on the interface requirements of the entire health care organization. Source: <a href="http://www.hl7.org/about/">http://www.hl7.org/about/.</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_HepatitisC" class="anchor"></span>Hepatitis C</td>
<td><p>A liver disease caused by the hepatitis C virus (HCV). HCV infection sometimes results in an acute illness, but most often becomes a chronic condition that can lead to cirrhosis of the liver and liver cancer.</p>
<p>See <a href="http://www.cdc.gov/hepatitis/index.htm">http://www.cdc.gov/hepatitis/index.htm</a></p></td>
</tr>
<tr class="even">
<td>HIV</td>
<td>See <a href="#Glos_HIV">Human Immunodeficiency Virus</a></td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>See <a href="#Glos_HL7">Health Level 7</a></td>
</tr>
<tr class="even">
<td><span id="Glos_HIV" class="anchor"></span>Human Immunodeficiency Virus (HIV)</td>
<td><p>HIV is a lentivirus (a member of the retrovirus family) that can lead to acquired immunodeficiency syndrome (<a href="#Glos_AIDS">AIDS</a>), a condition in humans in which the immune system begins to fail, leading to life-threatening opportunistic infections. HIV is different from most other viruses because it attacks the immune system. The immune system gives our bodies the ability to fight infections. HIV finds and destroys a type of white blood cell (T cells or CD4 cells) that the immune system must have to fight disease.</p>
<p>See also <a href="#Glos_AIDS">AIDS</a>.</p>
<p>See <a href="http://www.cdc.gov/hiv/">http://www.cdc.gov/hiv/</a>.</p></td>
</tr>
<tr class="odd">
<td>ICD-9</td>
<td><em>See</em> <a href="#Glos_ICD9">International Statistical Classification of Diseases and Related Health Problems, ninth edition</a></td>
</tr>
<tr class="even">
<td>ICD-10</td>
<td><em>See</em> <a href="#Glos_ICD10">International Statistical Classification of Diseases and Related Health Problems, tenth edition</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td>The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="even">
<td><span id="Glos_Interface" class="anchor"></span>Interface</td>
<td>An interface defines the communication boundary between two entities, such as a piece of software, a hardware device, or a user.</td>
</tr>
<tr class="odd">
<td><span id="Glos_ICD9" class="anchor"></span>International Statistical Classification of Diseases and Related Health Problems, ninth edition (ICD-9)</td>
<td>The ninth edition provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The "-9" refers to the ninth edition of these codes; the tenth edition has been published, but is not in widespread use at this time.</td>
</tr>
<tr class="even">
<td><span id="Glos_ICD10" class="anchor"></span>International Statistical Classification of Diseases and Related Health Problems, tenth edition (ICD-10)</td>
<td>International Statistical Classification of Diseases and Related Health Problems, tenth edition (commonly abbreviated as "ICD-10") consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>See <a href="#Glos_IRM">Information Resource Management</a></td>
</tr>
<tr class="even">
<td><span id="Glos_Kernel" class="anchor"></span>Kernel</td>
<td>The <a href="#Glos_VistA">VistA</a> software that enables VistA applications to coexist in a standard operating system independent computing environment.</td>
</tr>
<tr class="odd">
<td><span id="Glos_KIDS" class="anchor"></span>Kernel Installation and Distribution System (KIDS)</td>
<td>KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td><em>See</em> <a href="#Glos_KIDS">Kernel Installation and Distribution System</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_Library" class="anchor"></span>Library</td>
<td>In programming, a library is a collection of precompiled routines that a program can use. The routines, sometimes called modules, are stored in object format. Libraries are particularly useful for storing frequently used routines because you do not need to explicitly link them to every program that uses them. The linker automatically looks in libraries for routines that it does not find elsewhere.</td>
</tr>
<tr class="even">
<td><span id="Glos_LocalRegistry" class="anchor"></span>Local Registry</td>
<td>The local file of patients that have either passed the selection rules (and therefore been added automatically), or that have been added manually by a designated ICR supervisor.</td>
</tr>
<tr class="odd">
<td><span id="Glos_LOINC" class="anchor"></span>Logical Observation Identifiers Names and Codes (LOINC)</td>
<td>The LOINC database was developed to provide a definitive standard for identifying clinical information in electronic reports. The LOINC database provides a set of universal names and ID codes for identifying laboratory and clinical test results in the context of existing HL7 and other observation report messages.</td>
</tr>
<tr class="even">
<td>LOINC</td>
<td><em>See</em> <a href="#Glos_LOINC">Logical Observation Identifiers Names and Codes</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_M" class="anchor"></span>M</td>
<td><p><strong>M</strong> is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. <a href="#Glos_M">M</a> data structures are sparse, using strings of characters as subscripts.</p>
<p><strong>M</strong> was formerly (and is still commonly) called MUMPS, for <em>Massachusetts General Hospital Utility Multiprogramming System</em>.</p></td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><em>See</em> <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td>Namespace</td>
<td>A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Globals">globals</a>, <a href="#Glos_Routine">routines</a>, and <a href="#Glos_Library">libraries</a>. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In <a href="#Glos_VistA">VistA</a>, namespaces are usually dedicated to a particular function. The <strong>ROR</strong> namespace, for example, is designed for use by <a href="#Glos_CCR">CCR</a>.</td>
</tr>
<tr class="even">
<td>National Case Registry</td>
<td>All sites running the ICR registry transmit their data to this central data registry.</td>
</tr>
<tr class="odd">
<td><span id="Glos_RPC" class="anchor"></span>Remote Procedure Call (RPC)</td>
<td><p>A type of protocol that allows one program to request a service from a program located on another computer network. Using RPC, a system developer need not develop specific procedures for the server. The client program sends a message to the server with appropriate arguments and the server returns a message containing the results of the program executed. In this case, the GUI client uses an RPC to log the user on to <a href="#Glos_VistA">VistA</a>. And to call up, and make changes to, data that resides on a <strong>VistA</strong> server.</p>
<p><em>See also</em> <a href="#Glos_RPCBroker">Remote Procedure Call (RPC) Broker</a></p></td>
</tr>
<tr class="even">
<td><span id="Glos_RPCBroker" class="anchor"></span>Remote Procedure Call (RPC) Broker</td>
<td><p>A piece of middleware software that allows programmers to make program calls from one computer to another, via a network. The <a href="#Glos_RPCBroker">RPC Broker</a> establishes a common and consistent foundation for client/server applications being written under the <a href="#Glos_VistA">VistA</a> umbrella. The RPC Broker acts as a bridge connecting the client application front-end on the workstation (in this case, the Delphi Query Tool application) to the M –based data and business rules on the server. It serves as the communications medium for messaging between VistA client/server applications. Upon receipt, the message is decoded, the requested remote procedure call is activated, and the results are returned to the calling application. Thus, the RPC Broker helps bridge the gap between the traditionally proprietary VA software and other types of software.</p>
<p><em>See also</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></p></td>
</tr>
<tr class="odd">
<td><span id="Glos_Routine" class="anchor"></span>Routine</td>
<td>A section of a software program that performs a particular task. Programs consist of modules, each of which contains one or more routines. The term routine is essentially synonymous with procedure, function, and subroutine.</td>
</tr>
<tr class="even">
<td>RPC</td>
<td><em>See</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td><em>See</em> <a href="#Glos_RPCBroker">Remote Procedure Call Broker</a></td>
</tr>
<tr class="even">
<td><span id="Glos_SecurityKeys" class="anchor"></span>Security Keys</td>
<td>Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The <a href="#Glos_VistA">VistA</a> option file refers to the security key as a "lock." Only those individuals assigned that "lock" can use a particular VistA option or perform a specific task that is associated with that security key/lock.</td>
</tr>
<tr class="odd">
<td><span id="Glos_SingleSignOn" class="anchor"></span>Single Sign On</td>
<td>Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</td>
</tr>
<tr class="even">
<td><span id="Glos_TSPR" class="anchor"></span>Technical Services Project Repository (TSPR)</td>
<td><p>The TSPR is the central data repository and database for VA Health IT (VHIT) project information.</p>
<p><em>See</em> <a href="http://tspr.vista.med.va.gov/tspr/default.htm">http://tspr.VistA.med.va.gov/tspr/default.htm</a></p></td>
</tr>
<tr class="odd">
<td>TSPR</td>
<td><em>See</em> <a href="#Glos_TSPR">Technical Services Project Repository</a></td>
</tr>
<tr class="even">
<td><span id="Glos_UserInterface" class="anchor"></span>User Interface</td>
<td><p>A user interface is the means by which people (the users) interact with a particular machine, device, computer program or other complex tool (the system). The user interface provides one or more means of:</p>
<p>• Input, which allows the users to manipulate the system</p>
<p>• Output, which allows the system to produce the effects of the users' manipulation</p>
<p>The interface may be based strictly on text (as in the traditional "roll and scroll" IFCAP interface), or on both text and graphics.</p>
<p>In computer science and human-computer interaction, the user interface (of a computer program) refers to the graphical, textual and auditory information the program presents to the user, and the control sequences (such as keystrokes with the computer keyboard and movements of the computer mouse) the user employs to control the program.</p>
<p><em>See also</em> <a href="#Glos_GUI">Graphical User Interface</a></p></td>
</tr>
<tr class="odd">
<td>VDL</td>
<td><em>See</em> VistA Software Document Library.</td>
</tr>
<tr class="even">
<td>Vergence</td>
<td>Vergence® software from Sentillion provides a single, secure, efficient and safe point of access throughout the healthcare enterprise, for all types of caregivers and applications. Vergence unifies single sign-on, role-based application access, context management, strong authentication and centralized auditing capabilities into one fully integrated, out-of-the box clinical workstation solution.</td>
</tr>
<tr class="odd">
<td><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td>VistA is a comprehensive, integrated health care information system composed of numerous software modules.</td>
</tr>
<tr class="even">
<td><span id="Glos_VHA" class="anchor"></span>Veterans Health Administration (VHA)</td>
<td>VHA administers the United States Veterans Healthcare System, whose mission is to serve the needs of America's veterans by providing primary care, specialized care, and related medical and social support services.</td>
</tr>
<tr class="odd">
<td><span id="Glos_VISN" class="anchor"></span>Veterans Integrated Service Network (VISN)</td>
<td><a href="#Glos_VHA">VHA</a> organizes its local facilities into networks called VISNS (VA Integrated Service Networks). At the VISN level, VistA data from multiple local facilities may be combined into a data warehouse.</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>See <a href="#Glos_VHA">Veterans Health Administration</a></td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>See <a href="#Glos_VISN">Veterans Integrated Service Networks</a></td>
</tr>
<tr class="even">
<td>VistA</td>
<td>See <a href="#Glos_VistA">Veterans Health Information System and Technology Architecture</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_VDL" class="anchor"></span>VistA Software Document Library (VDL)</td>
<td><p>This web site has documentation on the various nationally released software applications created and/or used by the VA. There are four sections: Clinical, Infrastructure, Financial-Administrative, and Health<em><u>e</u></em>Vet. Typically, the documentation set includes user manual or guide, technical manual or systems management guide, installation guide, release notes, and similar items.</p>
<p><em>See</em> <a href="http://www4.va.gov/vdl/">http://www4.va.gov/vdl/</a></p></td>
</tr>
</tbody>
</table>
