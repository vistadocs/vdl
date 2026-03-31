---
title: Clinical Lexicon Version 2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: LEX
app_name: Lexicon Utility
section: CLI
app_status: active
pkg_ns: LEX
patch_ver: 2
patch_id: LEX*2
group_key: "LEX:LEX:2"
file_numbers: []
security_keys: []
menu_options: 6
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - class
  - strong
  - table
  - style
  - width
  - even
  - defaults
  - lexicon
  - contents
page_count: 0
word_count: 7074
section_count: 16
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lexicon_Utility/lexum2_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lexicon_Utility/lexum2_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=76"
---

> ![](clinical-lexicon-version-2-user-manual/001.png)

Lexicon Utility

> User Manual

![](clinical-lexicon-version-2-user-manual/002.png)

> Version 2.0

> September 1996

> Revised Apr 21, 2014

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Office of Enterprise Development (OED)

> Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 58%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>05/06/2009</p>
</blockquote></td>
<td><blockquote>
<p>LEX*2.0*62</p>
<p>Options to allow advanced date testing</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/21/2014</p>
</blockquote></td>
<td><blockquote>
<p>LEX*2.0*80</p>
<p>ICD-10 Implementation in the Lexicon</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/02/2014</p>
</blockquote></td>
<td><blockquote>
<p>Tech writer review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> <u>Table of Contents</u>

1.  [Preface 1](#preface)
    1.  [Scope of the Manual 1](#scope-of-the-manual)
    2.  [Audience 1](#audience)
    3.  [Related Manuals 1](#related-manuals)
2.  [Introduction 2](#introduction)
    1.  [The Lexicon Utility Package 2](#the-lexicon-utility-package)
    2.  [Use with other applications 2](#use-with-other-applications)
    3.  [Direct use by clinicians 2](#direct-use-by-clinicians)
    4.  [Direct use by managers 2](#direct-use-by-managers)
3.  [Orientation 3](#orientation)
    1.  [How to use this manual 3](#how-to-use-this-manual)
    2.  [VistA and Lexicon Utility Conventions 3](#vista-and-lexicon-utility-conventions)
    3.  [Option examples 4](#option-examples)
4.  [Package Management 5](#package-management)
    1.  [Legal Requirements 5](#legal-requirements)
    2.  [Links and Relationships with Other Packages 5](#links-and-relationships-with-other-packages)
    3.  [Menu and Option Assignment 6](#menu-and-option-assignment)
        1.  [Options Recommended for Managers 6](#4.3.1_Options_Recommended_for_Managers)

[4.3.2 Options Recommended for All Users 7](#4.3.2_Options_Recommended_for_All_Users)

[4.3.3 Options for working with ICD/CPT 8](#4.3.3_Options_for_working_with_ICD/CPT)

5.  [Package Operation 10](#5.__Package_Operation)
    1.  [Editing 10](#5.1_Editing)
        1.  [Edit Lexicon Menu 10](#5.1.1_Edit_Lexicon_Menu)
        2.  [Edit Search Threshold for a Coding System 10](#5.1.2_Edit_Search_Threshold_for_a_Coding)
        3.  [Edit Term Definition 11](#5.1.3_Edit_Term_Definition)
        4.  [Edit Shortcuts by Context 12](#5.1.4_Edit_Shortcuts_by_Context)
6.  [Defaults 13](#6._Defaults)
    1.  [Defaults Menu 13](#6.1_Defaults_Menu)
        1.  [Edit User/User Group Defaults 13](#6.1.1_Edit_User/User_Group_Defaults)
        2.  [List User/User Group Defaults 17](#6.1.2_List_User/User_Group_Defaults)
7.  [Lexicon Utility 18](#lexicon-utility)
    1.  [Lexicon Utility Menu 18](#lexicon-utility-menu)
    2.  [Look-up 18](#look-up)
        1.  [Look-up Term 18](#7.2.1_Look-up_Term)
        2.  [User Defaults \[LEX USER DEFAULTS\] 21](#7.2.2_User_Defaults_[LEX_USER_DEFAULTS])
        3.  [Creating a Default 26](#7.2.3__Creating_a_Default)
        4.  [Creating a Default Display 26](#7.2.4_Creating_a_Default_Display)
        5.  [Creating a Default Filter 28](#7.2.5_Creating_a_Default_Filter)
7.  [Glossary 38](#glossary)
8.  [Index 39](#index)

# Preface 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Scope of the Manual](#scope-of-the-manual)
  - [Audience](#audience)
  - [Related Manuals](#related-manuals)
- [Introduction](#introduction)
  - [The Lexicon Utility Package](#the-lexicon-utility-package)
  - [Use with other applications](#use-with-other-applications)
  - [Direct use by clinicians](#direct-use-by-clinicians)
  - [Direct use by managers](#direct-use-by-managers)
- [Orientation](#orientation)
  - [How to use this manual](#how-to-use-this-manual)
  - [VistA and Lexicon Utility Conventions](#vista-and-lexicon-utility-conventions)
  - [Option examples](#option-examples)
- [Package Management](#package-management)
  - [Legal Requirements](#legal-requirements)
  - [Links and Relationships with Other Packages](#links-and-relationships-with-other-packages)
  - [Menu and Option Assignment](#menu-and-option-assignment)
    - [Code Sets Menu](#code-sets-menu)
    - [\[LEX MGR DEFAULTS\]](#lex-mgr-defaults)
    - [\[LEX MGR USER DEFAULTS\]](#lex-mgr-user-defaults)
    - [\[LEX MGR DEFAULTS\]](#lex-mgr-defaults-1)
- [Lexicon Utility](#lexicon-utility)
  - [Lexicon Utility Menu](#lexicon-utility-menu)
  - [Look-up](#look-up)
    - [Currently, there are three types of filters:](#currently-there-are-three-types-of-filters)
    - [Classification Coding System Filter](#classification-coding-system-filter)
    - [Semantics Filter](#semantics-filter)
- [Glossary](#glossary)
- [Index](#index)

## Scope of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual provides descriptions of menus, options, and other information required to effectively use the Lexicon Utility.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual's intended audience is Information Resource Management (IRM) personnel, Applications Coordinators (ADPACs), Clinical Coordinators, and users of packages that include the Lexicon Utility.

> At this printing, Problem List, Text Integration Utility (TIU), and Automated Information Collection System (AICS) V. 2.1 use the Lexicon Utility. Clinical users of these packages would especially benefit from the ‘User Defaults’ and ‘Creating a Default’ sections of this manual.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lexicon Utility Technical Manual/Developer’s Guide Lexicon Utility Installation Guide

> CPT five-digit codes and/or descriptions are © Copyright 1988 American Medical Association. All rights reserved.

# Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The Lexicon Utility Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Provides a basis for a common language of terminology so that all members of a healthcare team may communicate with each other.
- Provides terminology that is well-defined, understandable, unique in concept, and encodable, using a variety of coding schemes.
- Provides the ability to upgrade coding systems (for example, ICD9-CM to ICD-10) and to add, change, and delete codes.
- Provides for a limited view of vocabulary in the form of Lexicon subsets.

## Use with other applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Lexicon Utility is a clinical resource tool useful to other applications. Current VistA applications using the Lexicon Utility include the Problem List, the Text Integration Utility (TIU), and the Automated Information Collection System (AICS).

## Direct use by clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The only clinical user interfaces with this package are in the Lexicon Utility menu option. This menu allows simple searches of the Lexicon Utility in a “stand-alone” environment and lets clinical users set private user defaults.

## Direct use by managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Management user interfaces included with this package allow for editing the definition of an expression, setting or listing user defaults for a single user or user group, and simple searches of the Lexicon in a “stand-alone” environment.

# Orientation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to use this manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Make sure you (or your users) know how to log on, navigate among the menu and options, and respond to prompts for data entry. If necessary, ask your Application Coordinator (ADPAC) or an IRM staff member to help you. The *DHCP User’s Guide to Computing* provides basic information about general computing and your computer system.
2.  Review the *Preface*, the *Table of Contents*, and the *Introduction*, to understand the organization of the Lexicon Utility and this manual.

> Note: The *Introduction* section in this manual presents an overview of the Lexicon Utility program.

> The *Package Management* section in this manual describes some of the special issues for managing the program.

> The *Package Operation* section describes how to use the Lexicon Utility program.

3.  If you are the Application Coordinator, review the *Package Operation* section and then copy and distribute the manual or appropriate sections to individual users, according to the menus assigned by IRM/ADPAC.
4.  Review the specific VistA and Lexicon Utility manual conventions on the following pages.

## VistA and Lexicon Utility Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lexicon Utility uses the same conventions as Lab, Pharmacy, and other VistA packages (see *DHCP User's Guide to Computing* for complete details). Only a few of the special keys and commands are described here.

> \<Enter\> End of response. This indicates the return key in examples of computer dialogs. (On ANSI Standard keyboards, it's the Return or ↵ key). Enter it after every response, when you bypass a prompt, take a default (//), or return to a previous action.

> ? Help with a prompt. If you enter a question mark after a prompt, the computer displays instructions or a list of choices for responding to the current prompt.

> ?? Detailed Help with a prompt. Two (2) question marks usually cause more detailed instructions to appear, or a list of choices.

> // The Lexicon Utility provides a default response. Double slashes mean the program has a default response. This response prints in the prompt immediately before the double slashes. It is either the most likely choice, a previously entered response, or the least harmful choice.

> Example:

> If you wish to select the default response, "NO," just press the enter key, indicated in this manual by \<Enter\>; otherwise, enter a different choice.

> ^ Return to the previous level. A single up-arrow terminates a series of questions and returns you to a previous level. You may need to enter

> ^ several times to exit the program or return to the level you wish. To return to a previous prompt or option, enter ^ and the name of the prompt or option.

> ^(#) Start a selection list over beginning with number \#. The Lexicon Utility lists entries when the response to a query references more than one entry. If there are more than one group of matches to display, you can type ^ followed by an entry number and the display goes backward or forward to that entry on the list.

> ?(#) Print the definition of an entry. The Lexicon Utility lists entries for the user to select. If the entry has a definition, you may view that definition by typing "?" followed by the number of the entry. Entries having a definition are displayed on the selection list and marked with an asterisk “\*”.

## Option examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Menus and examples of computer dialog that you see on the CRT screen are depicted in plain boxes:

> User responses: In computer dialogs, the user response is in boldface.

> The reader is encouraged to work through these examples as a first step in understanding the Lexicon Utility and its capabilities.

# Package Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no specific legal requirements for the Lexicon Utility software (routines and Data Dictionaries). However, the data stored in the globals contains copyright materials taken directly from the VA’s File 81, Current Procedural Terminology (CPT-4). The following copyright notice applies to this package:

> © 1988 American Medical Association

> This also applies to such other date of publication of CPT-4 as defined in the Berne Implementation Act of 1988 (formerly the Copyright Revision Act of 1976). CPT-4 does not include any fee schedules, basic unit values, relative value guides or related listings. The AMA assumes no responsibility for the consequences attributable to or related to any use or interpretation of information contained in or not contained in this publication. The AMA shall not be deemed to be engaged in the practice of medicine or dispensing medical services.

> Printing of any CPT information that is external to the VA (excluding areas of billing or fee basis processing, administrative management, clinical management including research, and patient coding and summarizing) must include the following notice:

#### “CPT five-digit codes and descriptions © 1988 AMA.”

> (Or such other date of publication of the work as defined in the Berne Implementation Act of 1988, formerly the Copyright Revision Act of 1976).”

## Links and Relationships with Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lexicon Utility is closely linked to other applications (e.g., Problem List, TIU). This linkage should remain transparent to users. See the user and technical manuals of those packages for further instructions.

> The Lexicon Utility contains terminology representing major clinical concepts. Each major concept can be expressed in numerous forms such as a definition, a synonym, or lexical variant. These expressions are updated from multiple clinical and non-clinical terminology sources such as Social Work, Nursing, etc., along with the Lexicon itself, which captures terms entered by healthcare providers that are unrecognized by the Lexicon Utility program.

> VA Medical Records Technicians (MRTs), with the help of standardized VA classification system files (e.g., ICD-9, CPT-4, or DSM), update the classification systems. The ability to link multiple codes to a single term allows the flexibility to update

> classification systems as new terminology and coding schemes become available (e.g., ICD 10). The Lexicon Utility does this while retaining backward compatibility with older terms and coding systems. Updates to the Lexicon Utility are sent simultaneously to all VA sites.

## Menu and Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lexicon Utility contains two major menus: the Lexicon Utility menu and the Lexicon Management Menu. Menus and options can be assigned as follows:

1.  <span id="4.3.1_Options_Recommended_for_Managers" class="anchor"></span>Options Recommended for Managers

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Lexicon Management Menu</p>
</blockquote></th>
<th><blockquote>
<p>Menu</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EditUser/User Group Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>List User/User Group Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDD1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit Lexicon</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Edit Term Definition</p>
</blockquote></td>
<td><blockquote>
<p>LEXEDF1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit Shortcuts by Context</p>
</blockquote></td>
<td><blockquote>
<p>LEXSC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lexicon Utility</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Look-up Term</p>
</blockquote></td>
<td><blockquote>
<p>LEXLK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>User Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>LEXDVO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 69%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Lexicon Management Menu</p>
</blockquote></th>
<th><blockquote>
<p><strong>Menu</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LEX MGT MENU</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>This menu option contains three sub-menus.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Defaults Menu</p>
</blockquote></td>
<td><blockquote>
<p><strong>Menu</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX MGR DEFAULTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>This menu option contains two sub-options.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Edit User/User Group Defaults</strong></td>
<td><blockquote>
<p><strong>LEXDMG</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LEX MGR USER DEFAULTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This option allows a manager to modify user defaults for either a single user or a user group (based on service).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>List User/User Group Defaults</strong></td>
<td><blockquote>
<p><strong>LEXDD1</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX MGR LIST DEFAULTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This option allows a manager to list user defaults to a device for either a single user or a user group (based on service).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit Lexicon Menu</p>
</blockquote></td>
<td><blockquote>
<p><strong>Menu</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 77%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>LEX MGR EDIT LEXICON</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>You may only edit certain fields in the Lexicon. This menu option contains sub-options that allow managers to edit those [few] fields.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Edit Search Threshold for a Coding System</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDMGS</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX MGR EDIT SEARCH THRESHOLD</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This allows a manager to edit the search threshold for a coding system. That is the default number of record to examine before prompting the user to continue or refine the search.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Edit Term Definition</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXEDF1</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX MGR EDIT DEFN</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This option lets managers edit the definition of an expression. This definition is accessible during searches using the Lexicon help routine.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Edit Shortcuts by Context</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXSC</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LEX MGR EDIT SHORTCUTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This option lets managers add or delete shortcuts (by context).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lexicon Utility Menu</p>
</blockquote></td>
<td><blockquote>
<p><strong>Menu</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX UTILITY</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This menu option contains two sub-options, "Lexicon Look-up" (to perform simple searches of the Lexicon outside an application) and "Lexicon Look-up Defaults" (to edit a single user's defaults). These options are described below under “Options</p>
<p>recommended for all users.”</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  <span id="4.3.2_Options_Recommended_for_All_Users" class="anchor"></span>Options Recommended for All Users

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Lexicon Utility</p>
</blockquote></th>
<th><blockquote>
<p>Menu</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Look-up Term</p>
</blockquote></td>
<td><blockquote>
<p>LEXLK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>User Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>LEXDVO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>List Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Lexicon Utility Menu</p>
</blockquote></th>
<th><blockquote>
<p><strong>Menu</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LEX UTILITY</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This menu option contains two sub-options: "Lexicon Look-up" (to perform simple searches of the Lexicon outside an application) and "Lexicon Look-up Defaults" (to edit a single user's defaults).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Look-up Term</p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXLK</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX LOOK-UP</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>This option lets a user perform a simple look-up in the Lexicon (outside an application) and displays all the information known about the expression selected (i.e., definitions, classification codes, semantic classifications, etc.).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>User Defaults</p>
</blockquote></td>
<td><blockquote>
<p><strong>Menu</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX USER DEFAULTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This option lets a single user modify his/her defaults (including filter, display format, vocabulary and keywords).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDFL</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LEX USER FILTER</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This option lets the user either select or create their own filter to use while conducting searches in the Lexicon. This filter limits the response of the look-up based on the conditions found in the filter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDCC</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX USER DISPLAY</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This sets the user default that formats the selection list during searches of the Lexicon.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDVO</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LEX USER VOCABULARY</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This option lets the user select a default vocabulary (or subset) of the Lexicon to use during look-up (i.e., Nursing, Social Work, etc.).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Shortcuts</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDCX</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LEX USER SHORTCUTS</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This option lets the user select a default set of shortcuts to use to rapidly access the Lexicon without the benefit of the special look-up.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List Defaults</p>
</blockquote></td>
<td><blockquote>
<p><strong>LEXDDS</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LEX USER DEFAULT LIST</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>This option lets the user list their current defaults to a device (terminal</p>
<p>or printer).</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  <span id="4.3.3_Options_for_working_with_ICD/CPT" class="anchor"></span>Options for working with ICD/CPT

> Code Sets Menu

> ICD-9 Diagnosis Code Set Query LEXQID

> ICD-9 Procedure Code Set Query LEXQIP CPT/HCPCS Procedure Code Set Query LEXQCP CPT Modifier Code Set Query LEXQCM

> ICD/CPT Code Set Change List LEXQC

> Code History LEXQH

### Code Sets Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[LEX CSV\]

> ICD Diagnosis Code Set Query

> \[LEX CSV ICD QUERY\] LEXQID

> This option displays a single versioned entry from the ICD Diagnosis file \#80 based on a date provided by the user. The date may be a future date.

> ICD Procedure Code Set Query

> \[LEX CSV ICP QUERY\] LEXQIP

> This option displays a single versioned entry from the ICD Operations/Procedure file \#80.1 based on a date provided by the user. The date may be a future date.

> CPT/HCPCS Procedure Code Set Query

> \[LEX CSV CPT QUERY\] LEXQCP

> This option displays a single versioned entry from the CPT/HCPCS file \#81 based on a date provided by the user. The date may be a future date.

> CPT Modifier Code Set Query

> \[LEX CSV MOD QUERY\] LEXQCM

> This option displays a single versioned entry from the CPT Modifier file \#81.3 based on a date provided by the user. The date may be a future date.

> ICD/CPT Code Set Change List

> \[LEX CSV ICD/CPT CHANGE LIST\] LEXQC

> This option produces a listing of ICD/CPT changes effective on the date provided by the user.

> Code History

> \[LEX CSV HISTORY\] LEXQH

4.  <span id="5.__Package_Operation" class="anchor"></span><u>Package Operation</u>

> The Lexicon Utility contains clinical major concepts that are expressed in numerous forms such as: Synonyms, Lexical variants, etc.

> It is not a coding system itself, but a mapping utility to link text to standard terminology and codes.

> Version 1.0, called the Clinical Lexicon, was released with Problem List Version 2.0. Version 2.0 of the Lexicon Utility makes major advances over Version 1.0.

> Most users are only aware of the Lexicon Utility when they add a new problem to a patient's problem list. The problem name that the clinician, nurse, or clerk enters is matched by the computer against a term in the lexicon. If there is an exact match, the program adds it to the problem list. If there is more than one term that matches the clinician's entry (for example, there are many variations on Diabetes and Cardiac Arrest), the clinician is prompted to select the closest match. An \* (asterisk) by a term indicates that a definition for that term is available.

> Lexicon Utility options are used primarily for customizing the lexicon to the needs of specific users, to make related applications such as Problem List work more efficiently. The Lexicon Utility is described by sub-menu on the following pages. Numerous examples are included.

1.  <span id="5.1_Editing" class="anchor"></span>Editing
    1.  <span id="5.1.1_Edit_Lexicon_Menu" class="anchor"></span>Edit Lexicon Menu

> \[LEX MGR EDIT LEXICON\]

> This menu currently contains two options: one to edit the definition of a term and one to edit the shortcuts used to access the Lexicon.

2.  <span id="5.1.2_Edit_Search_Threshold_for_a_Coding" class="anchor"></span>Edit Search Threshold for a Coding System

> \[LEX MGR EDIT SEARCH THRESHOLD\]

> This allows a manager to edit the search threshold for a coding system- That is, the default number of records to examine before prompting the user to continue or refine the search.

3.  <span id="5.1.3_Edit_Term_Definition" class="anchor"></span>Edit Term Definition

> \[LEX MGR EDIT DEFN\]

> You can add a definition or edit an existing definition for any expression in the Lexicon Utility. We recommend that this option be given only to managers since it changes the definition of an expression in the Lexicon Utility for all users. The Lexicon Utility places all definitions added or edited at a site into an electronic mail message and sends them back to the <span class="mark">REDACTED</span>.

> The Lexicon Utility can be updated from these messages.

4.  <span id="5.1.4_Edit_Shortcuts_by_Context" class="anchor"></span>Edit Shortcuts by Context

> \[LEX MGR EDIT SHORTCUTS\]

> A shortcut is a frequently used text string that maps directly to one and only one expression in the Lexicon. If a user elects to use shortcuts (selectable as a default) and enters the shortcut during a search, the Lexicon Utility returns the single expression it is mapped to in the database. For instance, if the text string “HTN” was mapped to the expression “Hypertension” then a search for “HTN” would return only “Hypertension” and not the 74 entries in the Lexicon that deal with various forms of hypertension. The Shortcut Context defines how and when the shortcuts are used by the Lexicon Utility; it is possible to define the shortcut “HTN” to retrieve “Hypertension” for the Problem List application, and define “HTN” to retrieve “Essential Hypertension” for another application or clinic.

5.  <span id="6._Defaults" class="anchor"></span><u>Defaults</u>
    1.  <span id="6.1_Defaults_Menu" class="anchor"></span>Defaults Menu

### \[LEX MGR DEFAULTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains two options: one to modify user defaults and one to list user defaults to a device. The manager default options differ from the user default options, which can only modify a single user (self). The manager default options can list and modify user defaults for another user other than yourself, or for a group of users based service.

> Edit User/User Group Defaults \[LEX MGR USER DEFAULTS\] List User/User Group Defaults \[LEX MGR LIST DEFAULTS\]

> These options are described on the following pages.

1.  <span id="6.1.1_Edit_User/User_Group_Defaults" class="anchor"></span>Edit User/User Group Defaults

### \[LEX MGR USER DEFAULTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows management to change the Lexicon Utility look-up defaults for a single user, a user group based on service, or all users. These defaults can be set for one or more applications. In the following example, all of the defaults (filter, display, vocabulary, and shortcuts) are being set for all users within the Nursing service, for the Lexicon Utility only (this does not change any user defaults for the Problem List application). In each case, the default is chosen from a list of exported default values. It is also possible to delete a default value and in some cases create a new default value (i.e., filter and display).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 47%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Applications</p>
</blockquote>
<ol type="1">
<li><p>Lexicon</p></li>
<li><p>Problem List</p></li>
<li><blockquote>
<p>All of the Above Select (1-3): <strong>1</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Lexicon Defaults:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td>Unselected</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td>Unselected</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td>Unselected</td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td>Unselected</td>
</tr>
</tbody>
</table>

> Select default to modify (1-4): 1

> User default search filter

1.  Modify
2.  Delete

> Select: 1// Modify Default Filter

> Search filters (screens) to limit the response

1.  Select from predefined filters
2.  Create your own filter Select: 1// Predefined Set

> 8 Filters found

1.  CPT Only \*
2.  DSM Only \*
3.  ICD Only \*
4.  ICD/CPT Only \*
5.  Nursing Problems/Diagnosis (Less Nursing Interventions) \* Select FILTER 1-5: 5

> Lexicon Defaults:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Filter</p>
</blockquote></th>
<th><blockquote>
<p>Nursing Problems/Diagnosis (Less Nursing</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Interventions)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>Unselected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>Unselected</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>Unselected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Select default to modify (1-4): <strong>2</strong></p>
<p>User default display format</p>
</blockquote>
<ol type="1">
<li><p>Modify</p></li>
<li><p>Delete</p></li>
</ol>
<blockquote>
<p>Select: <strong>1</strong>// Modify Default Display</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 28%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>Display format to be used during look-up</p>
</blockquote>
<ol type="1">
<li><p>Select from predefined display formats</p></li>
<li><blockquote>
<p>Create your own display format Select: <strong>1</strong>// Predefined Set</p>
</blockquote></li>
</ol>
<blockquote>
<p>9 Displays found</p>
</blockquote>
<ol type="1">
<li><p>All Classification Systems *</p></li>
<li><p>ICD Diagnosis (only) *</p></li>
<li><p>ICD Diagnosis and Procedures *</p></li>
<li><p>ICD and CPT codes *</p></li>
<li><blockquote>
<p>ICD, CPT and DSM * Select 1-5: <strong>&lt;Enter&gt;</strong></p>
</blockquote></li>
<li><p>Mental Health (DSM w/ICD) *</p></li>
<li><p>Nursing Diag/Interventions *</p></li>
<li><p>Nursing Diagnosis *</p></li>
<li><blockquote>
<p>VA Commonly Used Systems * Select 1-9: <strong>7</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Lexicon Defaults:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Problems/Diagnosis Interventions)</p>
<p>Nursing Diag/Interventions</p>
</blockquote></td>
<td><blockquote>
<p>(Less</p>
</blockquote></td>
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>Unselected</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>Unselected</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>Select default to modify (1-4): <strong>3</strong></p>
<p>User default vocabulary</p>
</blockquote>
<ol type="1">
<li><p>Modify</p></li>
<li><p>Delete</p></li>
</ol>
<blockquote>
<p>Select: <strong>1</strong>// Modify Default Vocabulary</p>
<p>5 Subsets found</p>
</blockquote>
<ol type="1">
<li><p>Dental *</p></li>
<li><p>Immunologic *</p></li>
<li><p>Nursing *</p></li>
<li><p>Social Work *</p></li>
<li><p>Lexicon *</p></li>
</ol>
<blockquote>
<p>Select SUBSET 1-5: <strong>3</strong></p>
<p>Lexicon Defaults:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>1</p>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
<p>Display</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Nursing Problems/Diagnosis Interventions)</p>
<p>Nursing Diag/Interventions</p>
</blockquote></td>
<td><blockquote>
<p>(Less Nursing</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Nursing</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 58%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>4 Shortcuts Unselected</p>
<p>Select default to modify (1-4): <strong>4</strong></p>
<p>User default shortcut context</p>
</blockquote>
<ol type="1">
<li><p>Modify</p></li>
<li><p>Delete</p></li>
</ol>
<blockquote>
<p>Select: <strong>1</strong>// Modify Default Shortcut Context</p>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>SHORTCUT CONTEXT(s) found</p>
</blockquote></li>
</ol>
<ol type="1">
<li><p>GENERAL CLINIC *</p></li>
<li><p>DIAGNOSIS/PROCEDURES *</p></li>
<li><p>PROBLEM LIST *</p></li>
</ol>
<blockquote>
<p>Select SHORTCUT CONTEXT 1-3: // <strong>1</strong></p>
<p>Lexicon Defaults:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Problems/Diagnosis (Less</p>
</blockquote></td>
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Interventions)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Diag/Interventions</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL CLINIC</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> For users in Service/Section: NURSING SERVICE

> RVICE

> 118

> Replace existing defaults: Yes, existing defaults will be changed

> Existing filter will be replaced Existing display will be replaced Existing vocabulary will be replaced Existing shortcuts will be replaced

1.  <span id="6.1.2_List_User/User_Group_Defaults" class="anchor"></span>List User/User Group Defaults

### \[LEX MGR DEFAULTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows managers to display Lexicon Utility defaults that have been set for users. You can display them for all users, a single user, or users in a specific service or section.

# Lexicon Utility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Lexicon Utility Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[LEX UTILITY\]

> This menu contains the Lexicon Utility’s Look-up and the User Default options. These options are described on the following pages.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Look-up Term</p>
</blockquote></th>
<th><blockquote>
<p>[LEX LOOK-UP]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>User Defaults</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER DEFAULTS]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER FILTER]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER DISPLAY]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER VOCABULARY]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER SHORTCUTS]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List Defaults</p>
</blockquote></td>
<td><blockquote>
<p>[LEX USER DEFAULT LIST]</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Look-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <span id="7.2.1_Look-up_Term" class="anchor"></span>Look-up Term

> \[LEX LOOK-UP\]

> This option lets you look up an expression (term/concept) to see if it exists in the Lexicon, or what variations on the term exist. You can also enter a classification code (i.e., ICD, CPT, etc.) when prompted to “Enter Term/Concept.”

> DEFINITION:

> A vaccine consisting of diphtheria toxoid, tetanus toxoid, and pertussis

> vaccine. It is usually given to infants three times at two-month intervals, generally at 2, 4, and 6 months of age. The vaccine

> protects

> against diphtheria, tetanus, and whooping cough. In most cases

> the few

> vaccine causes only a temporary fever and discomfort, but in a cases serious neurological side effects have been observed.

> SEMANTICS:

> CLASS TYPE

> Chemical and Drugs Pharmacologic Substance

> Immunologic Factor Try another? Yes// \<Enter\> (Yes)

> Enter Term/Concept: 300.1

> Searching for 300.1

> 16 matches found

1.  Hysteria \* (ICD-9-CM 300.10)
2.  Conversion Disorder \* (DSM-IV 300.11) (ICD-9-CM 300.11)
3.  Psychogenic amnesia \* (ICD-9-CM 300.12)
4.  Dissociative Amnesia (DSM-IV 300.12)
5.  Psychogenic fugue (ICD-9-CM 300.13) Select 1-5: 2

> Do you want more information? Yes// \<Enter\> (Yes)

> TERMS:

> Concept: Conversion Disorder

> Directly Linked to Concept/Major Concept

> Synonym: Conversion disorder (or Hysterical neurosis, conversion type)

> Directly Linked to Concept/Other Form

> Synonym: Conversion disorder, psychologic Directly Linked to Concept/Other Form

> Synonym: Conversion Reaction

> Directly Linked to Concept/Other Form

> Synonym: Hysteria, Conversion

> Directly Linked to Concept/Other Form

> Variant: Conversion Disorders

1.  <span id="7.2.2_User_Defaults_[LEX_USER_DEFAULTS]" class="anchor"></span>User Defaults \[LEX USER DEFAULTS\]

> This option lets you change your personal Lexicon User Defaults (this is similar to the management option LEX MGR DEFAULTS except it only affects the current user). In this example, all of the defaults are being set (filter, display, vocabulary and shortcuts) for the current user and only for the Lexicon Utility (the Problem List defaults for this user remain unchanged). At the end of the example, the user chose to display the default values for the current user.

> Select Lexicon Utility Option: 2 User Defaults

1.  Filter
2.  Display
3.  Vocabulary
4.  Shortcuts
5.  List Defaults

> Select User Defaults Option: 1 Filter

> Select application: ??

> Choose from:

> Lexicon LEX

> Problem List GMPL

> Select application: LEXICON Lexicon LEX

> User default search filter

1.  Modify
2.  Delete

> Select: 1// \<Enter\> Modify Default Filter

> Search filters (screens) to limit the response

1.  Select from predefined filters
2.  Create your own filter

> Select: 1// \<Enter\> Predefined Set

8.  Filters found
    1.  CPT Only \*
    2.  DSM Only \*
    3.  ICD Only \*
    4.  ICD/CPT Only \*
    5.  Nursing Problems/Diagnosis (Less Nursing Interventions) \* Select FILTER 1-5: ?4

> ICD/CPT Only

> This screen will filter out all entries not linked to either the International Classification of Diseases and Diagnosis (ICD) or the Current Procedural Terminology (CPT) classification systems.

1.  CPT Only \*
2.  DSM Only \*
3.  ICD Only \*
4.  ICD/CPT Only \*
5.  Nursing Problems/Diagnosis (Less Nursing Interventions) \* Select FILTER 1-5: 4
1.  Filter
2.  Display
3.  Vocabulary
4.  Shortcuts
5.  List Defaults

> Select User Defaults Option: 2 Display

> Select application: LEXICON Lexicon LEX

> User default display format

1.  Modify
2.  Delete

> Select: 1// \<Enter\> Modify Default Display

> Display format to be used during look-up

1.  Select from predefined display formats
2.  Create your own display format Select: 1// \<Enter\> Predefined Set
9.  Displays found
    1.  All Classification Systems \*
    2.  ICD Diagnosis (only) \*
    3.  ICD Diagnosis and Procedures \*
    4.  ICD and CPT codes \*
    5.  ICD, CPT and DSM \* Select 1-5: ?4

> ICD and CPT codes

> Displays diagnostic and procedural classification codes from the International Classification of Diseases/Diagnosis (ICD), and procedural codes from the Current Procedural Terminology (CPT).

1.  All Classification Systems \*
2.  ICD Diagnosis (only) \*
3.  ICD Diagnosis and Procedures \*
4.  ICD and CPT codes \*
5.  ICD, CPT and DSM \* Select 1-5: 4
1.  Filter
2.  Display
3.  Vocabulary
4.  Shortcuts
5.  List Defaults

> Select User Defaults Option: 3 Vocabulary

> Select application: LEXICON Lexicon LEX

> 5 Subsets found

1.  Dental \*
2.  Immunologic \*
3.  Nursing \*
4.  Social Work \*
5.  Lexicon \* Select SUBSET 1-5: ?5

> Lexicon

> This subset contains the entire Lexicon. While it

> is not a true subset (i.e., part of the whole), it is defined here as the default when a more precise subset has not been selected.

1.  Dental \*
2.  Immunologic \*
3.  Nursing \*
4.  Social Work \*
5.  Lexicon \* Select SUBSET 1-5: 5
1.  Filter
2.  Display
3.  Vocabulary
4.  Shortcuts
5.  List Defaults

> Select User Defaults Option: 4 Shortcuts

> Select application: LEXICON Lexicon LEX

> 3 SHORTCUT CONTEXT(s) found

1.  GENERAL CLINIC \*
2.  DIAGNOSIS/PROCEDURES \*
3.  PROBLEM LIST \*

> Select SHORTCUT CONTEXT 1-3: // ?2

> DIAGNOSIS/PROCEDURES

> Keywords for the DIAGNOSIS/PROCEDURES context will always map to a unique concept in the Expression file which has either an ICD code or a CPT code associated with it.

1.  GENERAL CLINIC \*
2.  DIAGNOSIS/PROCEDURES \*
3.  PROBLEM LIST \*
    1.  <span id="7.2.3__Creating_a_Default" class="anchor"></span>Creating a Default

> The Lexicon Utility exports several defaults from which the user may select. In the case of the look-up display and filter, the user may select an option to create their own tailor made display or filter. Creating a display or filter is done by selecting display or filter values from tables supplied with the Lexicon Utility and saving them as a look-up default.

2.  <span id="7.2.4_Creating_a_Default_Display" class="anchor"></span>Creating a Default Display

> During a search of the Lexicon, you may elect to have classification codes (e.g., ICD, CPT, DSM, etc.) displayed, along with the terms on the selection list. You may select from a list of predefined displays or create your own. If you create your own display, you are asked which classification coding systems to include in your display. The following example creates a default display which shows North American Nursing Diagnosis Association (NANDA) codes and ICD codes with the terms during a search:

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 13%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ACR Index for Radiological Diagnosis Display these codes during look-up? No//</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>(No)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AIR Disease/Findings Knowledge Base Display these codes during look-up? No//</p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
<td><blockquote>
<p>(No)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>COS Computer Stored Ambulatory Records Term File Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>CPT Current Procedural Terminology</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>CSP Computer Retrieval of Info. on Scientific Projects Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>CST Coding Symbols Thesaurus for Adverse Reaction Terms Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>DS3 Diagnostic &amp; Statistical Manual of Mental Disorders Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>DS4 Diagnostic &amp; Statistical Manual of Mental Disorders Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>DXP Diagnostic Prompting System</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>ICD International Classification of Diseases, Diagnosis Display these codes during look-up? No// <strong>Y</strong> (Yes)</p>
<p>ICP International Classification of Diseases, Procedures Display these codes during look-up? No// <strong>Y</strong> (Yes)</p>
<p>MCM Glossary of Epidemiology Terms</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>NAN Classification of Nursing Diagnosis</p>
<p>Display these codes during look-up? No// <strong>Y</strong> (Yes)</p>
<p>NIC Nursing Intervention Classifications</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>OMA Omaha Nursing Diagnosis and Interventions</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>SNM Systematized Nomenclature of Medicine</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>UMD Universal Medical Device Nomenclature System Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No)</p>
<p>UWA Glossary of Neuronames</p>
<p>Display these codes during look-up? No// <strong>&lt;Enter&gt;</strong> (No) Display name: <strong>NANDA/ICD</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  <span id="7.2.5_Creating_a_Default_Filter" class="anchor"></span>Creating a Default Filter

> During a search of the Lexicon, you may elect to filter your search and exclude terms which do not meet the filtering criteria. You may select from a list of predefined filters or create your own.

### Currently, there are three types of filters:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Filter based on semantic class and semantic type of a term
- Filter based on classification coding system linked to a term (e.g., ICD, CPT, etc.)
- Filter on a combination of semantics and classifications coding systems

### Classification Coding System Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Creating a filter based on classification coding systems is very similar to creating a display but, instead of displaying the codes, the filter only considers terms in the search which are linked to the selected classification coding systems.

### Semantics Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each concept in the Lexicon has been semantically classed and typed. You may elect to include a semantic class in the search by including it in the default filter (include by class); however, you may not want to include all of the semantic types belonging to the class in the search (exclude by type). Consider the semantic class

> “DISEASE/PATHOLOGIC PROCESS”:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Class</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Disease/Pathologic Process</p>
</blockquote></td>
<td><blockquote>
<p>Pathologic Function</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Disease or Syndrome</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Mental or Behavioral Dysfunction</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Experimental Model of Disease</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Finding</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Laboratory or Test Result</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Sign or Symptom</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Injury or Poisoning</p>
</blockquote></td>
</tr>
</tbody>
</table>

> You may wish to include the semantic class “DISEASE OR PATHOLOGIC PROCESS” but exclude the semantic type, “EXPERIMENTAL MODEL OF DISEASE”. When creating a filter based on semantic classes and type, you are asked to “INCLUDE” semantic classes (14 classes), and then asked if you wish to exclude any semantic types.

> The following example includes the semantic classes “BEHAVIORS” and “DISEASE OR PATHOLOGIC PROCESS” and excludes the semantic type “EXPERIMENTAL MODEL OF DISEASE”:

> belong to an "excluded" semantic type. Do you wish to continue: YES// \<Enter\>

> 1: ACT Activities

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> CODES

> AI/RHEUM COSTAR COSTART

> CPT-4 CRISP DSM-IIIR

> ICD-9 NANDA NUR INTERV SNOMED

> Semantic Types:

> Event, activity, daily or recreational activity, occupational activity, health care activity, research activity, governmental or regulatory activity, educational activity, machine activity, phenomenon or process, human-caused phenomenon or process, environmental effect of humans, natural phenomenon or process

> Include this class: YES// NO

> 2: ANT Anatomy

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> AI/RHEUM AMER COL RADIOLOGY COSTAR

> COSTART CPT-4 CRISP

> ICD-9 NUR INTERV CODES SNOMED UNIV MED DEV

> Semantic Types:

> Anatomical structure, embryonic structure, congenital abnormality, acquired abnormality, fully formed anatomical structure, body system, body part, organ or organ component, tissue, cell, cell component, body location or region, body space or junction, body substance

> Include this class: YES// NO

> 3: BEH Behaviors

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 36%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
<th>CRISP</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td>NANDA</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Semantic Types:

> Behavior, social behavior, individual behavior Include this class: YES// \<Enter\>

> Do you want to "exclude" any of

> the semantic types listed above: NO// \<Enter\>

> 4: CHM Chemical and Drugs

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> AI/RHEUM COSTART CPT-4

> CRISP ICD-9 NUR INTERV

> CODES

> SNOMED UNIV MED DEV

> Semantic Types:

> Chemical, chemical viewed structurally, inorganic chemical, element or ion, isotope, inorganic compound, organic chemical, steroid, eicosanoid, lactam, alkaloid, organophosphorus compound, carbohydrate, lipid, chemical viewed functionally, pharmacologic substance, biomedical or dental material, biologically active substance, neuroreactive substance or biogenic amine, hormone, enzyme, vitamin, prostaglandin, immunologic factor, indicator or reagent, hazardous or poisonous substance

> Include this class: YES// NO

> 5: CON Concepts/Ideas

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 34%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
<p>UNIV MED DEV</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Semantic Types:</p>
<p>Conceptual entity, idea or concept, temporal concept, qualitative concept, quantitative concept, spatial concept, functional concept, intellectual product, language, regulation or law, group attribute</p>
<p>Include this class: YES// <strong>NO</strong></p>
<p>6: DIS Diseases/Pathologic Processes</p>
<p>This Semantic Class contains terms from, or mapped to, the following classification systems:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AI/RHEUM</p>
</blockquote></td>
<td><blockquote>
<p>COSTAR</p>
</blockquote></td>
<td><blockquote>
<p>COSTART</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> SNOMED

> Semantic Types:

> Pathologic function, disease or syndrome, mental or behavioral dysfunction, experimental model of disease, finding, laboratory or test result, sign, symptom, injury or poisoning

> Include this class: YES// \<Enter\>

> Do you want to "exclude" any of

> the semantic types listed above: NO// YES

> Semantic Type: Finding

> This Semantic Type contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 34%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Examples of Semantic Type: Finding

> 1: Abdominal Mass

> 2: Abdominal or pelvic swelling, mass, or lump 3: Abnormal Chest X-Ray

> Exclude this type: NO// \<Enter\>

> Semantic Type: Laboratory or Test Result

> This Semantic Type contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 27%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
<p>NUR INTERV CODES</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
<p>SNOMED</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Examples of Semantic Type: Laboratory or Test Result 1: Electrocardiogram Abnormal</p>
<p>2: Accommodation Error</p>
<p>3: Achlorhydria</p>
<p>Exclude this type: NO// <strong>&lt;Enter&gt;</strong></p>
<p>Semantic Type: Injury or Poisoning</p>
<p>This Semantic Type contains terms from, or mapped to, the following classification systems:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AI/RHEUM</p>
</blockquote></td>
<td><blockquote>
<p>COSTAR</p>
</blockquote></td>
<td><blockquote>
<p>COSTART</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Examples of Semantic Type: Injury or Poisoning

> 1: Abdominal Injuries

> 2: Drug-Induced Abnormalities

> 3: Radiation-Induced Abnormalities Exclude this type: NO// \<Enter\>

> Semantic Type: Pathologic Function

> This Semantic Type contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 41%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Examples of Semantic Type: Pathologic Function

> 1: Abnormal hard tissue formation in pulp 2: Abnormal loss of weight

> 3: Abnormal weight gain Exclude this type: NO// \<Enter\>

> Semantic Type: Disease or Syndrome

> This Semantic Type contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 33%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Examples of Semantic Type: Disease or Syndrome

> 1: Abacterial meningitis

> 2: Acute Abdomen

> 3: Abdominal Cramps Exclude this type: NO// \<Enter\>

> Semantic Type: Mental or Behavioral Dysfunction

> This Semantic Type contains terms from, or mapped to, the following classification systems:

> AI/RHEUM COSTAR COSTART

> CRISP DSM-IIIR ICD-9

> NANDA NUR INTERV CODES SNOMED

Examples of Semantic Type: Mental or Behavioral Dysfunction

> 1: Child Abuse NEC

> 2: Academic skills disorders

> 3: Adjustment Disorder with Anxiety Exclude this type: NO// \<Enter\>

> Semantic Type: Experimental Model of Disease

> This Semantic Type contains terms from, or mapped to, the following classification systems:

> CRISP ICD-9 SNOMED

Examples of Semantic Type: Experimental Model of Disease

> 1: Alloxan Diabetes

> 2: Arthritis, Adjuvant

> 3: Avian Leukosis Exclude this type: NO// YES

> Semantic Type: Signs and Symptoms

> This Semantic Type contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 17%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV</p>
</blockquote></td>
<td><blockquote>
<p>CODES</p>
</blockquote></td>
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Examples of Semantic Type: Signs and Symptoms

> 1: Abdominal Cramps

> 2: Abdominal Distention

> 3: Abdominal Pain

> Exclude this type: NO// \<Enter\>

> 7: GEO Geographic Areas

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> CRISP

> Semantic Types:

> Geographic areas

> Include this class: YES// NO

> 8: GRP Groups

> This Semantic Class contains terms from, or mapped to, the following classification systems:

CRISP DSM-IIIR ICD-9

> NUR INTERV CODES SNOMED

> Semantic Types:

> Group, professional or occupational group, population group, family group, age group, patient or disabled group

> Include this class: YES// NO

> 9: MOL Molecular Biology

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 41%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Semantic Types:

> Macromolecular structure, gene or genome, molecular function, genetic function, cell or molecular dysfunction, molecular biology research technique, molecular sequence, nucleotide sequence, amino acid sequence, carbohydrate sequence, nucleic acid, nucleoside or nucleotide, amino acid, peptide or protein, gene product

> Include this class: YES// NO

> 10: OBJ Physical Objects

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> CODES

> COSTAR COSTART CPT-4

> CRISP ICD-9 NUR INTERV

> SNOMED UNIV MED DEV

> Semantic Types:

> Entity, physical object, manufactured object, medical device, research device, substance, food

> Include this class: YES// NO

> 11: OCC Occupations/Organizations

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 52%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>CPT-4</p>
</blockquote></th>
<th>CRISP</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
<td>SNOMED</td>
</tr>
</tbody>
</table>

> Semantic Types:

Occupation or discipline, biomedical occupation or discipline,

> organization, health care related organization, professional society, self-help or relief organization

> Include this class: YES// NO

> 12: ORG Organisms

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 42%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>COSTAR SNOMED</p>
</blockquote></th>
<th><blockquote>
<p>CRISP</p>
<p>UNIV MED DEV</p>
</blockquote></th>
<th><blockquote>
<p>ICD-9</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Semantic Types:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Organism, plant, alga, fungus, virus, rickettsia or chlamydia, bacterium, animal, invertebrate, vertebrate, amphibian, bird, fish, reptile, mammal, human

> Include this class: YES// NO

> 13: PHY Physiology

> This Semantic Class contains terms from, or mapped to, the following classification systems:

> CODES

> AI/RHEUM COSTAR COSTART

> CPT-4 CRISP DSM-IIIR

> ICD-9 NANDA NUR INTERV SNOMED

> Semantic Types:

> Biologic function, physiologic function, organism function, mental process, organ or tissue function, cell function, organism

> attribute

> Include this class: YES// NO

> 14: PRO Procedures

> This Semantic Class contains terms from, or mapped to, the following classification systems:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 45%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AI/RHEUM</p>
</blockquote></th>
<th><blockquote>
<p>COSTAR</p>
</blockquote></th>
<th><blockquote>
<p>COSTART</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPT-4</p>
</blockquote></td>
<td><blockquote>
<p>CRISP</p>
</blockquote></td>
<td><blockquote>
<p>DSM-IIIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>NUR INTERV CODES</p>
</blockquote></td>
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UNIV MED DEV</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Semantic Types:

> Laboratory procedure, diagnostic procedure, therapeutic or preventive procedure

> Include this class: YES// NO

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TERM</p>
</blockquote></th>
<th><blockquote>
<p>MEANING</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADPAC</p>
</blockquote></td>
<td><blockquote>
<p>Automated Data Processing Application Coordinator-The person assigned by a service to coordinate computer activities</p>
<p>for that service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPT</p>
</blockquote></td>
<td><blockquote>
<p>Current Procedural Terminology, a coding system of medical terms, used for billing purposes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSM</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic and Statistical Manual of Mental Disorders.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Display Codes</p>
</blockquote></td>
<td><blockquote>
<p>In Lexicon Look-up options, <em>Display Codes</em> is a parameter users can set that allows for the display of Classification codes (such as ICD, CPT, DSM, NANDA, etc.) on the selection list during searches.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Expression</p>
</blockquote></td>
<td><blockquote>
<p>The textual means to convey a concept to the user. It can be a major concept, a synonym, or a lexical variant.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>The purpose of a filter is to limit the responses displayed on a selection list during searches to specific categories of terminology.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD</p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resource Management; the VAMC service and the people in it who manage VistA and other computer services for</p>
<p>the medical center.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Major Concept</p>
</blockquote></td>
<td><blockquote>
<p>A unique concept which may have several synonyms or lexical</p>
<p>variants (i.e., plural, acronym, etc.)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NANDA</p>
</blockquote></td>
<td><blockquote>
<p>North American Nursing Diagnosis Association</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NIC</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Intervention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Omaha</p>
</blockquote></td>
<td><blockquote>
<p>Omaha Nursing Diagnosis/Intervention</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Semantic Class/Type</p>
</blockquote></td>
<td><blockquote>
<p>A semantic class can be a subjective grouping of related semantic types (e.g., all chemicals) or a categorical grouping of terms with a common theme.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SNOMED</p>
</blockquote></td>
<td><blockquote>
<p>Systematic Nomenclature of Medicine. A coding system used mostly by the Anatomic Pathology module of the Laboratory</p>
<p>package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>A parameter in Lexicon look-up defaults that allows the user to specify look-up on either the main file containing over 92,241 concepts or a subset of the main file containing a limited</p>
<p>number of concepts based on a service, discipline, or other clinical concept (e.g., Nursing or Social Work subsets).</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ADPAC , 11, 51
> CPT 15, 16, 31, 35, 36, 38, 41, 43, 47, 51
> Display Codes 29, 38, 51
> DSM-III-R 51
> Editing 16, 21
> Expression 9, 15, 17, 21, 22, 29, 31, 33, 37, 51
> Filter 18, 25, 34, 41, 51
> ICD-9-CM 29, 32, 51
> IRM 11, 51
> Legal Requirements 15
> Major Concept 15, 32, 51
> Menus 16, 22, 29, 31, 34
> NANDA 38, 51
> NIC 39, 51
> Omaha 39, 52
> Problem List 9, 15, 25, 34
> Semantic Class/Type 18, 32, 41, 52
> SNOMED 33, 43, 52
> Vocabulary 9, 16, 18, 25, 34, 52
