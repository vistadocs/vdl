---
title: Clinical Lexicon Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
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
menu_options: 0
description: > CPT five-digit codes and/or descriptions only are © Copyright 1988 American Medical Association. All rights reserved.
audience: > The intended audience for this publication is VAMC IRM staff.
keywords: 
  - blockquote
  - class
  - strong
  - table
  - lexicon
  - contents
  - installation
  - style
  - width
  - defaults
page_count: 0
word_count: 6200
section_count: 12
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lexicon_Utility/lexig2_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lexicon_Utility/lexig2_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=76"
---

> ![](clinical-lexicon-version-2-installation-guide/001.png)

LEXICON UTILITY INSTALLATION GUIDE

> Version 2.0

> September 1996

> Department of Veterans Affairs Software Service

> Computerized Patient Record System Product Line

> CPT five-digit codes and/or descriptions only are © Copyright 1988 American Medical Association. All rights reserved.

# Preface 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [General Installation Information](#general-installation-information)
  - [Resource Requirements](#resource-requirements)
  - [Package Components](#package-components)
- [Pre-Installation](#pre-installation)
  - [Required and Recommended Software and Files](#required-and-recommended-software-and-files)
  - [Environment](#environment)
  - [Special Considerations](#special-considerations)
- [Installation](#installation)
  - [Data](#data)
    - [All Sites](#all-sites)
    - [MSM Site](#msm-site)
    - [DSM Site](#dsm-site)
  - [Package](#package)
    - [Load a Distribution](#load-a-distribution)
    - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
    - [Install Package(s)](#install-packages)
    - [Installation Capture Example](#installation-capture-example)
    - [Build File Contents](#build-file-contents)
    - [Install File Contents](#install-file-contents)
- [Post-Installation](#post-installation)
  - [Package Installation Message](#package-installation-message)
  - [Post-Installation Routine Messages](#post-installation-routine-messages)
  - [Post Installation Instructions](#post-installation-instructions)
    - [Options](#options)
    - [Purge Routines](#purge-routines)
    - [Translation](#translation)
    - [Globals](#globals)
    - [Environment](#environment-1)
- [Appendix: Release Notes](#appendix-release-notes)
  - [Changes since version 1.0:](#changes-since-version-10)
- [Index](#index)
> The Lexicon Utility provides a basis for a common language of terminology so that all members of a health care team may communicate with each other. As such, the clinician can either use it alone or in conjunction with another V*IST*A (Veterans Information System Technology Architecture, the new name for DHCP) package such as the Problem List, the Text Integration Utility (TIU) or the Automated Information Collection System (AICS).

#### Scope of the Manual

> This manual provides the information necessary for the efficient and safe installation of the Lexicon Utility.

#### Audience

> The intended audience for this publication is VAMC IRM staff.

#### Related Manuals:

> Lexicon Utility Technical Manual/Developer’s Guide Lexicon Utility User Manual
> Preface
> This page intentionally left blank

# General Installation Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Namespace (*changed*)

> Lexicon Utility V. 2.0: LEX

> ![](clinical-lexicon-version-2-installation-guide/002.png)![](clinical-lexicon-version-2-installation-guide/003.png)![](clinical-lexicon-version-2-installation-guide/004.png)![](clinical-lexicon-version-2-installation-guide/005.png)![](clinical-lexicon-version-2-installation-guide/006.png)![](clinical-lexicon-version-2-installation-guide/007.png)![](clinical-lexicon-version-2-installation-guide/008.png)![](clinical-lexicon-version-2-installation-guide/009.png)The package name, namespace, and global roots have been changed in version 2.0.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 37%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](clinical-lexicon-version-2-installation-guide/010.png)</p>
<blockquote>
<p><strong>Package name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version 1.0 Clinical Lexicon Utility</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version 2.0 Lexicon Utility</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Namespace</p>
</blockquote></td>
<td><blockquote>
<p>GMPT</p>
</blockquote></td>
<td><blockquote>
<p>LEX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Data Global</p>
</blockquote></td>
<td><blockquote>
<p>^GMP</p>
</blockquote></td>
<td><blockquote>
<p>^LEX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Utility Global</p>
</blockquote></td>
<td><blockquote>
<p>^GMPT</p>
</blockquote></td>
<td><blockquote>
<p>^LEXT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](clinical-lexicon-version-2-installation-guide/011.png)We changed the namespace because of an accident, which occurred in August of 1995, in which a developer KILLed ^GMP global instead of the desired ^TMP nodes.

> TMP and GMP differ by one character (T to G), adjacent to each other on the standard QWERTY keyboard, both controlled by the same hand (left) and both controlled by the same finger (left index). The ^LEX global namespace should prove to be much safer than GMP.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> V*IST*A’s Lexicon Utility is a dynamic dictionary of medical terms mapped to coding schemes such as ICD-9, CPT-4, and DSM-IV. The Lexicon Utility can support other coding schemes that are unique to the VA, such as the codes used by the Social Work Service or US Code Title 38 Chapter 4 for Service Connected Disabilities.

> Two globals accompany this package:

> ^LEX Main Lexicon files, contains terminology and lexical information

> ^LEXT Utility and temporary storage file, contains user defaults

> <span id="_bookmark1" class="anchor"></span>Once installed, the Lexicon Utility’s global files remain relatively static with the following three exceptions:

1.  Unresolved Narrative file 757.06 will grow over time. However, after the file size grows to 50 records, the entries in this file are packed into a Mailman message and sent to Salt Lake City IRMFO and the records are deleted.
2.  Subset Definition file 757.2 containing user defaults
3.  Shortcuts file 757.4 containing shortcuts to access the Lexicon data

#### Estimated Disk Space

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 33%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th>75</th>
<th>mb</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Host File</p>
</blockquote></td>
<td>124</td>
<td>mb</td>
</tr>
</tbody>
</table>

- NOTE:
1)  If your site receives the data via a TCP/IP - FTP transfer, you must reserve an additional 124 mb of disk space to accommodate the host file.
2)  If your site does not have the capability of electronic file transfer, and must receive the data on a tape cartridge, you may restore the global directly from the tape without requiring additional disk space.

## Package Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Globals

#### Deleted at Site

> The installation process does not delete any globals. However, we recommend that after installation you delete the ^GMP and ^GMPT globals.

#### Sent to Site

> ^LEX and ^LEXT are new globals for this package and will replace ^GMP and ^GMPT globals (if installed) from the Clinical Lexicon Utility V. 1.0.

> The ^LEX is not included in the KIDS installation. You must load the

> ^LEX data before the installation begins.

> The ^LEXT global is included in the KIDS installation.

#### Data Dictionaries

#### Deleted at Site

> Data dictionaries for the Clinical Lexicon Utility V. 1.0 for ^GMP and GMPT are deleted during the installation. The global is not deleted by the installation.

#### Sent to Site

> All data dictionaries for the Lexicon Utility V. 2.0 for globals ^LEX and LEXT are added to your system during the installation.

#### Files

#### Deleted at Site

> None.

> ![](clinical-lexicon-version-2-installation-guide/012.png)![](clinical-lexicon-version-2-installation-guide/013.png)![](clinical-lexicon-version-2-installation-guide/014.png)![](clinical-lexicon-version-2-installation-guide/015.png)![](clinical-lexicon-version-2-installation-guide/016.png)![](clinical-lexicon-version-2-installation-guide/017.png)![](clinical-lexicon-version-2-installation-guide/018.png)![](clinical-lexicon-version-2-installation-guide/019.png)![](clinical-lexicon-version-2-installation-guide/020.png)![](clinical-lexicon-version-2-installation-guide/021.png)![](clinical-lexicon-version-2-installation-guide/022.png)![](clinical-lexicon-version-2-installation-guide/023.png)![](clinical-lexicon-version-2-installation-guide/024.png)![](clinical-lexicon-version-2-installation-guide/025.png)![](clinical-lexicon-version-2-installation-guide/026.png)![](clinical-lexicon-version-2-installation-guide/027.png)![](clinical-lexicon-version-2-installation-guide/028.png)![](clinical-lexicon-version-2-installation-guide/029.png)![](clinical-lexicon-version-2-installation-guide/030.png)![](clinical-lexicon-version-2-installation-guide/031.png)![](clinical-lexicon-version-2-installation-guide/032.png)![](clinical-lexicon-version-2-installation-guide/033.png)![](clinical-lexicon-version-2-installation-guide/034.png)![](clinical-lexicon-version-2-installation-guide/035.png)![](clinical-lexicon-version-2-installation-guide/036.png)![](clinical-lexicon-version-2-installation-guide/037.png)![](clinical-lexicon-version-2-installation-guide/038.png)![](clinical-lexicon-version-2-installation-guide/039.png)![](clinical-lexicon-version-2-installation-guide/040.png)![](clinical-lexicon-version-2-installation-guide/041.png)![](clinical-lexicon-version-2-installation-guide/042.png)![](clinical-lexicon-version-2-installation-guide/043.png)![](clinical-lexicon-version-2-installation-guide/044.png)![](clinical-lexicon-version-2-installation-guide/045.png)![](clinical-lexicon-version-2-installation-guide/046.png)![](clinical-lexicon-version-2-installation-guide/047.png)![](clinical-lexicon-version-2-installation-guide/048.png)![](clinical-lexicon-version-2-installation-guide/049.png)![](clinical-lexicon-version-2-installation-guide/050.png)![](clinical-lexicon-version-2-installation-guide/051.png)![](clinical-lexicon-version-2-installation-guide/052.png)![](clinical-lexicon-version-2-installation-guide/053.png)![](clinical-lexicon-version-2-installation-guide/054.png)![](clinical-lexicon-version-2-installation-guide/055.png)![](clinical-lexicon-version-2-installation-guide/056.png)![](clinical-lexicon-version-2-installation-guide/057.png)![](clinical-lexicon-version-2-installation-guide/058.png)![](clinical-lexicon-version-2-installation-guide/059.png)![](clinical-lexicon-version-2-installation-guide/060.png)![](clinical-lexicon-version-2-installation-guide/061.png)![](clinical-lexicon-version-2-installation-guide/062.png)![](clinical-lexicon-version-2-installation-guide/063.png)*Sent to Site*

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Entries</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Exported on</strong></p>
<p><strong>(H)ost</strong></p>
<p><strong>(K)ids</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Remarks</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>757</p>
</blockquote></td>
<td><blockquote>
<p>Major Concept Map</p>
</blockquote></td>
<td><blockquote>
<p>99859</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.001</p>
</blockquote></td>
<td><blockquote>
<p>Concept Usage</p>
</blockquote></td>
<td><blockquote>
<p>99859</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.01</p>
</blockquote></td>
<td><blockquote>
<p>Expressions</p>
</blockquote></td>
<td><blockquote>
<p>133676</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.011</p>
</blockquote></td>
<td><blockquote>
<p>Expression Type</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.014</p>
</blockquote></td>
<td><blockquote>
<p>Expression Form</p>
</blockquote></td>
<td>![](clinical-lexicon-version-2-installation-guide/064.png) 12</td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.02</p>
</blockquote></td>
<td><blockquote>
<p>Codes</p>
</blockquote></td>
<td><blockquote>
<p>53130</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.03</p>
</blockquote></td>
<td><blockquote>
<p>Coding Systems</p>
</blockquote></td>
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.04</p>
</blockquote></td>
<td><blockquote>
<p>Excluded Words</p>
</blockquote></td>
<td><blockquote>
<p>127</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/065.png)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.05</p>
</blockquote></td>
<td><blockquote>
<p>Replacement Words</p>
</blockquote></td>
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.06</p>
</blockquote></td>
<td><blockquote>
<p>Unresolved Narratives</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/066.png)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.1</p>
</blockquote></td>
<td><blockquote>
<p>Semantic Map</p>
</blockquote></td>
<td><blockquote>
<p>145581</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.11</p>
</blockquote></td>
<td><blockquote>
<p>Semantic Class</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.12</p>
</blockquote></td>
<td><blockquote>
<p>Semantic Type</p>
</blockquote></td>
<td><blockquote>
<p>133</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.2</p>
</blockquote></td>
<td><blockquote>
<p>Subset Definitions</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>K</p>
</blockquote></td>
<td><blockquote>
<p>Stored in ^LEXT global</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.21</p>
</blockquote></td>
<td><blockquote>
<p>Subsets</p>
</blockquote></td>
<td><blockquote>
<p>6271</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.3</p>
</blockquote></td>
<td><blockquote>
<p>Look-up Screens</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.31</p>
</blockquote></td>
<td><blockquote>
<p>Displays</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>757.4</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>1043</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>757.41</p>
</blockquote></td>
<td><blockquote>
<p>Shortcut Context</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>H</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### ![](clinical-lexicon-version-2-installation-guide/067.png)Routines

#### Deleted at Site

> *Clinical Lexicon Utility V. 1.0*

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GMPTA1</p>
</blockquote></th>
<th><blockquote>
<p>GMPTA2</p>
</blockquote></th>
<th><blockquote>
<p>GMPTA3</p>
</blockquote></th>
<th><blockquote>
<p>GMPTA4</p>
</blockquote></th>
<th><blockquote>
<p>GMPTA5</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GMPTDD1</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDD2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDD3</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDD4</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPTDDT1</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDT2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDT3</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDT4</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDTD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPTDDTF</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDDTV</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDGRP</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDIC1</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDIC2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPTDIC3</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDIC4</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDIC5</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDISP</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDLIM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPTDMGR</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDOVR</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDTSK</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDUSR</p>
</blockquote></td>
<td><blockquote>
<p>GMPTDVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPTDVOC</p>
</blockquote></td>
<td><blockquote>
<p>GMPTEDF1</p>
</blockquote></td>
<td><blockquote>
<p>GMPTEDF2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTERF</p>
</blockquote></td>
<td><blockquote>
<p>GMPTERI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPTHLP</p>
</blockquote></td>
<td><blockquote>
<p>GMPTI*</p>
</blockquote></td>
<td><blockquote>
<p>GMPTLK</p>
</blockquote></td>
<td><blockquote>
<p>GMPTLK2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTNDX1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPTNDX2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTNDX3</p>
</blockquote></td>
<td><blockquote>
<p>GMPTNDX4</p>
</blockquote></td>
<td><blockquote>
<p>GMPTNDX5</p>
</blockquote></td>
<td><blockquote>
<p>GMPTNTEG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPTOLKN</p>
</blockquote></td>
<td><blockquote>
<p>GMPTPRNT</p>
</blockquote></td>
<td><blockquote>
<p>GMPTSEND</p>
</blockquote></td>
<td><blockquote>
<p>GMPTSET2</p>
</blockquote></td>
<td><blockquote>
<p>GMPTSET3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPTSET4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Sent to Site

> *Lexicon Utility V. 2.0*

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>LEXA</p>
</blockquote></th>
<th><blockquote>
<p>LEXA1</p>
</blockquote></th>
<th><blockquote>
<p>LEXA2</p>
</blockquote></th>
<th><blockquote>
<p>LEXA3</p>
</blockquote></th>
<th><blockquote>
<p>LEXA4</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LEXAB</p>
</blockquote></td>
<td><blockquote>
<p>LEXABC</p>
</blockquote></td>
<td><blockquote>
<p>LEXAFIL</p>
</blockquote></td>
<td><blockquote>
<p>LEXAL</p>
</blockquote></td>
<td><blockquote>
<p>LEXAL2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXALK</p>
</blockquote></td>
<td><blockquote>
<p>LEXAM</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR2</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXAR4</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR5</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR6</p>
</blockquote></td>
<td><blockquote>
<p>LEXAR7</p>
</blockquote></td>
<td><blockquote>
<p>LEXAS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXAS2</p>
</blockquote></td>
<td><blockquote>
<p>LEXAS3</p>
</blockquote></td>
<td><blockquote>
<p>LEXAS4</p>
</blockquote></td>
<td><blockquote>
<p>LEXAS5</p>
</blockquote></td>
<td><blockquote>
<p>LEXAS6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXAS7</p>
</blockquote></td>
<td><blockquote>
<p>LEXASC</p>
</blockquote></td>
<td><blockquote>
<p>LEXASO</p>
</blockquote></td>
<td><blockquote>
<p>LEXCODE</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXDCCC</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCCS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCX</p>
</blockquote></td>
<td><blockquote>
<p>LEXDCXS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDD1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXDD2</p>
</blockquote></td>
<td><blockquote>
<p>LEXDD3</p>
</blockquote></td>
<td><blockquote>
<p>LEXDD4</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDSD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXDDSP</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDSS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDT1</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDT2</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDTC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXDDTD</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDTF</p>
</blockquote></td>
<td><blockquote>
<p>LEXDDTV</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFL</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFLC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXDFLS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFLT</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFN</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFN2</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFSB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXDFSE</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFSI</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFSO</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFSS</p>
</blockquote></td>
<td><blockquote>
<p>LEXDFST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXDM</p>
</blockquote></td>
<td><blockquote>
<p>LEXDM2</p>
</blockquote></td>
<td><blockquote>
<p>LEXDM3</p>
</blockquote></td>
<td><blockquote>
<p>LEXDM4</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXDMGO</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMGT</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMGU</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMGV</p>
</blockquote></td>
<td><blockquote>
<p>LEXDSV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXDVO</p>
</blockquote></td>
<td><blockquote>
<p>LEXDVOS</p>
</blockquote></td>
<td><blockquote>
<p>LEXEDF1</p>
</blockquote></td>
<td><blockquote>
<p>LEXEDF2</p>
</blockquote></td>
<td><blockquote>
<p>LEXERF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXERI</p>
</blockquote></td>
<td><blockquote>
<p>LEXHLP</p>
</blockquote></td>
<td><blockquote>
<p>LEXIENV</p>
</blockquote></td>
<td><blockquote>
<p>LEXILG</p>
</blockquote></td>
<td><blockquote>
<p>LEXILGD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXILGO</p>
</blockquote></td>
<td><blockquote>
<p>LEXILGP</p>
</blockquote></td>
<td><blockquote>
<p>LEXILGU</p>
</blockquote></td>
<td><blockquote>
<p>LEXILGX</p>
</blockquote></td>
<td><blockquote>
<p>LEXLGM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXLGM2</p>
</blockquote></td>
<td><blockquote>
<p>LEXLGM3</p>
</blockquote></td>
<td><blockquote>
<p>LEXLGM4</p>
</blockquote></td>
<td><blockquote>
<p>LEXLGM5</p>
</blockquote></td>
<td><blockquote>
<p>LEXLK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXLK2</p>
</blockquote></td>
<td><blockquote>
<p>LEXMTLU</p>
</blockquote></td>
<td><blockquote>
<p>LEXNDX1</p>
</blockquote></td>
<td><blockquote>
<p>LEXNDX2</p>
</blockquote></td>
<td><blockquote>
<p>LEXNDX3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXNDX4</p>
</blockquote></td>
<td><blockquote>
<p>LEXNDX5</p>
</blockquote></td>
<td><blockquote>
<p>LEXNDX6</p>
</blockquote></td>
<td><blockquote>
<p>LEXPL</p>
</blockquote></td>
<td><blockquote>
<p>LEXPLEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXPLIA</p>
</blockquote></td>
<td><blockquote>
<p>LEXPLUP</p>
</blockquote></td>
<td><blockquote>
<p>LEXPRNT</p>
</blockquote></td>
<td><blockquote>
<p>LEXSC</p>
</blockquote></td>
<td><blockquote>
<p>LEXSC2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEXSC3</p>
</blockquote></td>
<td><blockquote>
<p>LEXSET</p>
</blockquote></td>
<td><blockquote>
<p>LEXSET2</p>
</blockquote></td>
<td><blockquote>
<p>LEXSET3</p>
</blockquote></td>
<td><blockquote>
<p>LEXSET4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEXSET5</p>
</blockquote></td>
<td><blockquote>
<p>LEXSRC</p>
</blockquote></td>
<td><blockquote>
<p>LEXTOLKN</p>
</blockquote></td>
<td><blockquote>
<p>LEXU</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### Problem List V. 2.0

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GMPLBLDC</p>
</blockquote></th>
<th><blockquote>
<p>GMPLENFM</p>
</blockquote></th>
<th><blockquote>
<p>GMPLHIST</p>
</blockquote></th>
<th><blockquote>
<p>GMPLUTL1</p>
</blockquote></th>
<th><blockquote>
<p>GMPLX</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *Clinical Lexicon Utility V. 1.0*

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GMPTSET</p>
</blockquote></th>
<th><blockquote>
<p>GMPTU</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- NOTE: These two GMPT\* namespaced routines from the previous version remain to support Database Integration Agreements for the Clinical Lexicon Utility version 1.0.

#### Options

#### Renamed at Site

> ![](clinical-lexicon-version-2-installation-guide/068.png)![](clinical-lexicon-version-2-installation-guide/069.png)*Clinical Lexicon Utility V. 1.0*

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option ...</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/070.png)</p>
<p><strong>Renamed as ...</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Clinical Lexicon Management Menu GMPT CLINICAL LEXICON MGT MENU</p>
</blockquote></td>
<td><blockquote>
<p>Lexicon Management Menu LEX MGT MENU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit a term</p>
<p>GMPT MGR EDIT TERM</p>
</blockquote></td>
<td><blockquote>
<p>Edit Lexicon</p>
<p>LEX MGR EDIT LEXICON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Defaults</p>
<p>GMPT MGR DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>Defaults</p>
<p>LEX MGR DEFAULTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinical Lexicon Utility</p>
<p>GMPT CLINICAL LEXICON UTILITY</p>
</blockquote></td>
<td><blockquote>
<p>Lexicon Utility LEX UTILITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Clinical Lexicon Look-up</p>
<p>GMPT CLINICAL LEXICON LOOK-UP</p>
</blockquote></td>
<td><blockquote>
<p>Look-up Term LEX LOOK-UP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lexicon Look-up Defaults GMPT USER DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>User Defaults</p>
<p>LEX USER DEFAULTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Edit User/User Group Defaults GMPT MGR USER DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>Edit User/User Group Defaults LEX MGR USER DEFAULTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List User/User Group Defaults GMPT MGR LIST DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>List User/User Group Defaults LEX MGR LIST DEFAULTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Edit Term Definition GMPT MGR EDIT DEFN</p>
</blockquote></td>
<td><blockquote>
<p>Edit Term Definition LEX MGR EDIT DEFN</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ![](clinical-lexicon-version-2-installation-guide/071.png)![](clinical-lexicon-version-2-installation-guide/072.png)Problem List V. 2.0

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option ...</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Renamed as ...</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Problem Look-up Defaults GMPL USER SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Problem Look-up Defaults</p>
<p>GMPL USER LOOK-UP DEFAULTS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Renaming existing options to reflect the new option menu tree guarantees option menu assignments made in version 1.0 are retained in version 2.0.

#### Sent to Site

> ![](clinical-lexicon-version-2-installation-guide/073.png)![](clinical-lexicon-version-2-installation-guide/074.png)![](clinical-lexicon-version-2-installation-guide/075.png)![](clinical-lexicon-version-2-installation-guide/076.png)![](clinical-lexicon-version-2-installation-guide/077.png)![](clinical-lexicon-version-2-installation-guide/078.png)![](clinical-lexicon-version-2-installation-guide/079.png)![](clinical-lexicon-version-2-installation-guide/080.png)![](clinical-lexicon-version-2-installation-guide/081.png)![](clinical-lexicon-version-2-installation-guide/082.png)![](clinical-lexicon-version-2-installation-guide/083.png)![](clinical-lexicon-version-2-installation-guide/084.png)![](clinical-lexicon-version-2-installation-guide/085.png)![](clinical-lexicon-version-2-installation-guide/086.png)![](clinical-lexicon-version-2-installation-guide/087.png)![](clinical-lexicon-version-2-installation-guide/088.png)![](clinical-lexicon-version-2-installation-guide/089.png)![](clinical-lexicon-version-2-installation-guide/090.png)![](clinical-lexicon-version-2-installation-guide/091.png)*Lexicon Utility V. 2.0*

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 37%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Menu Text</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Type</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LEX MGT MENU</p>
</blockquote></td>
<td><blockquote>
<p>Lexicon Management Menu</p>
</blockquote></td>
<td><blockquote>
<p>Menu (managers)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX MGR DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX MGR USER DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>Edit User/User Group Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDMG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX MGR LIST DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>List User/User Group Defaults</p>
</blockquote></td>
<td><blockquote>
<p>LEXDD1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX MGR EDIT LEXICON</p>
</blockquote></td>
<td><blockquote>
<p>Edit Lexicon</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX MGR EDIT DEFN</p>
</blockquote></td>
<td><blockquote>
<p>Edit Term Definition</p>
</blockquote></td>
<td><blockquote>
<p>LEXEDF1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX MGR EDIT SHORTCUTS</p>
</blockquote></td>
<td><blockquote>
<p>Edit Shortcuts by Context</p>
</blockquote></td>
<td><blockquote>
<p>LEXSC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX UTILITY</p>
</blockquote></td>
<td><blockquote>
<p>Lexicon Utility</p>
</blockquote></td>
<td><blockquote>
<p>Menu (users)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX LOOK-UP</p>
</blockquote></td>
<td><blockquote>
<p>Look-up Term</p>
</blockquote></td>
<td><blockquote>
<p>LEXLK (demo)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX USER DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>User Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX USER FILTER</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDFL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX USER DISPLAY</p>
</blockquote></td>
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDCC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX USER VOCABULARY</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDVO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEX USER SHORTCUTS</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDCX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LEX USER DEFAULT LIST</p>
</blockquote></td>
<td><blockquote>
<p>List Defaults</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDDS</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ![](clinical-lexicon-version-2-installation-guide/092.png)![](clinical-lexicon-version-2-installation-guide/093.png)![](clinical-lexicon-version-2-installation-guide/094.png)![](clinical-lexicon-version-2-installation-guide/095.png)![](clinical-lexicon-version-2-installation-guide/096.png)![](clinical-lexicon-version-2-installation-guide/097.png)![](clinical-lexicon-version-2-installation-guide/098.png)![](clinical-lexicon-version-2-installation-guide/099.png)![](clinical-lexicon-version-2-installation-guide/100.png)![](clinical-lexicon-version-2-installation-guide/101.png)![](clinical-lexicon-version-2-installation-guide/102.png)![](clinical-lexicon-version-2-installation-guide/103.png)![](clinical-lexicon-version-2-installation-guide/104.png)![](clinical-lexicon-version-2-installation-guide/105.png)![](clinical-lexicon-version-2-installation-guide/106.png)![](clinical-lexicon-version-2-installation-guide/107.png)Problem List V. 2.0

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 30%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](clinical-lexicon-version-2-installation-guide/108.png)</p>
<blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/109.png)</p>
<p><strong>Option Menu Text</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Type</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GMPL USER LOOK-UP DEFAULTS</p>
</blockquote></td>
<td><blockquote>
<p>Problem Look-up Defaults</p>
</blockquote></td>
<td><blockquote>
<p>Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPL USER LOOK-UP FILTER</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>EN1^LEXDFL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPL USER LOOK-UP DISPLAY</p>
</blockquote></td>
<td><blockquote>
<p>Display</p>
</blockquote></td>
<td><blockquote>
<p>EN1^LEXDCC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPL USER LOOK-UP VOCABULARY</p>
</blockquote></td>
<td><blockquote>
<p>Vocabulary</p>
</blockquote></td>
<td><blockquote>
<p>EN1^LEXDVO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMPL USER LOOK-UP SHORTCUTS</p>
</blockquote></td>
<td><blockquote>
<p>Shortcuts</p>
</blockquote></td>
<td><blockquote>
<p>EN1^LEXDCX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMPL USER LOOK-UP LIST</p>
</blockquote></td>
<td><blockquote>
<p>List Current Defaults</p>
</blockquote></td>
<td><blockquote>
<p>EN^LEXDDS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This page intentionally left blank

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required and Recommended Software and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Required Packages

> Packages that the Lexicon Utility either points to or makes direct calls to supported the following entry points:

- Kernel 8.0
- VA Fileman 21
- Kernel Toolkit 7.3

#### Recommended Packages

> Packages which either point to the Lexicon or make direct calls to supported Lexicon Utility entry points:

- Automated Information Collection System (AICS) 2.1
- Problem List 2.0
- PCE Patient/IHS Subset 1.0
- Text Integration Utility 1.0 (when released)

#### Required Files

> ![](clinical-lexicon-version-2-installation-guide/110.png)![](clinical-lexicon-version-2-installation-guide/111.png)![](clinical-lexicon-version-2-installation-guide/112.png)![](clinical-lexicon-version-2-installation-guide/113.png)Files that the Lexicon Utility makes direct global reads to supported fields:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 33%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Global Root</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>^ICD9</p>
</blockquote></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD Diagnosis</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>^ICD0</p>
</blockquote></td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td><blockquote>
<p>ICD Procedures</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>^ICPT</p>
</blockquote></td>
<td><blockquote>
<p>80.1</p>
</blockquote></td>
<td><blockquote>
<p>CPT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>^YSD(627.7)</p>
</blockquote></td>
<td><blockquote>
<p>627.7</p>
</blockquote></td>
<td><blockquote>
<p>DSM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>^VA(200)</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>New Person</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](clinical-lexicon-version-2-installation-guide/114.png)![](clinical-lexicon-version-2-installation-guide/115.png)![](clinical-lexicon-version-2-installation-guide/116.png)The Lexicon Utility reads and writes to this file on supported fields.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](clinical-lexicon-version-2-installation-guide/117.png)</p>
<blockquote>
<p><strong>Global Root</strong></p>
</blockquote></th>
<th><p>![](clinical-lexicon-version-2-installation-guide/118.png)</p>
<blockquote>
<p><strong>File Number</strong></p>
</blockquote></th>
<th><p>![](clinical-lexicon-version-2-installation-guide/119.png)</p>
<blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>^AUPNPROB</p>
</blockquote></td>
<td><blockquote>
<p>9000011</p>
</blockquote></td>
<td><blockquote>
<p>Problem</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### General

#### All Sites

> Back up your system before you install Lexicon Utility V. 2.0. There should be no “clinical” users on the system during install.

> Verify that DUZ, DUZ(“AG”), DT,DTIME, and U are defined and DUZ(0)=”@”.

#### DSM Sites

> Log into the UCI where the Lexicon Utility is to be installed.

#### MSM Sites

> Make sure that journaling is on.

> The Stack/Stap should be increased to at least 20k during installation and operation. We recommend a partition size of 48k during installation and operation.

#### Disable Options

> To protect the environment during install, place the following Options “OUT OF ORDER”:

> GMPL BUILD SELECTION LIST GMPL CLINICAL USER

> GMPL PROBLEM LISTING GMPL USER SCREEN

- NOTE: From the time Clinical Lexicon Utility V. 1.0's Data Dictionaries are deleted until the time Lexicon Utility V. 2.0's Data Dictionaries are installed, the Problem List application (and other applications calling the Lexicon) are unable to locate the Special Lookup and Fileman cannot recognize the new global.

Pre-Installation

#### Initialize New Globals

#### MSM Sites

> Set the new globals to null on the file server: S ^LEX=””

> S ^LEXT=””

> Using the ^%GCH (Global Characteristics) utility, make sure the protection for both ^LEX and ^LEXT are set as follows:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 35%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>System</p>
</blockquote></th>
<th>RWD</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>World</p>
</blockquote></th>
<th>RWD</th>
</tr>
<tr class="header">
<th><blockquote>
<p>Group</p>
</blockquote></th>
<th>RWD</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em><strong>DSM Sites</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>User</p>
</blockquote></td>
<td>RWD</td>
</tr>
</tbody>
</table>

> Set the new globals to null in the UCI where the main Lexicon files will reside:

> S ^LEX=”” S ^LEXT=””

> Using the ^%GLOMAN (Global Management) utility, make sure the protection for both ^LEX and ^LEXT are set as follows:

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 32%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>System</p>
</blockquote></th>
<th>RWP</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>World</p>
</blockquote></th>
<th>RWP</th>
</tr>
<tr class="header">
<th><blockquote>
<p>Group</p>
</blockquote></th>
<th>RWP</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em><strong>Translation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>User</p>
</blockquote></td>
<td>RWP</td>
</tr>
</tbody>
</table>

> We recommend the Lexicon global ^LEX be installed in one UCI and translated to all other UCIs where the Lexicon Utility is installed. This will save on disk space and reduce future maintenance and file update times.

## Special Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pre-Installation Routine

> The Pre-Install routine deletes the data dictionaries for the Clinical Lexicon Utility V. 1.0. Any abort which occurs after the Pre-Install routine has run requires either a full re-install of Clinical Lexicon Utility V. 1.0 (to restore version 1) or a full install of the Lexicon Utility V. 2.0 (to continue to install version 2).

#### Post-Installation Routine

> The Post-Install routine updates the Problem List Problem file \#9000011 where possible. Once you do this, it is not possible to un-install Lexicon Utility version 2.0 and re-install the Clinical Lexicon Utility V. 1.0.

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data global ^LEX is exported as a host file and is obtained via:

1.  File Transfer, TCP/IP, FTP or from network shared resources.
2.  Tape Cassette, when electronic file transfer capability does not exist.

> The ^LEX global has been placed in a host file using the ^%GTO (Global Transfer Output) utility. This file is readable by both DSM and MSM sites.

> ![](clinical-lexicon-version-2-installation-guide/120.png)![](clinical-lexicon-version-2-installation-guide/121.png)![](clinical-lexicon-version-2-installation-guide/122.png)![](clinical-lexicon-version-2-installation-guide/123.png)![](clinical-lexicon-version-2-installation-guide/124.png)![](clinical-lexicon-version-2-installation-guide/125.png)![](clinical-lexicon-version-2-installation-guide/126.png)![](clinical-lexicon-version-2-installation-guide/127.png)![](clinical-lexicon-version-2-installation-guide/128.png)The ^LEX global is exported with all of the indexes intact. This is done to save global load time at the sites.

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 36%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Global Load Times *</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Load Global</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/129.png)</p>
<p><strong>Re-Indexing</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Export with Indexes Intact</p>
</blockquote></td>
<td><blockquote>
<p>45 minutes - 1 hour 15 minutes</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Export without Indexes</p>
</blockquote></td>
<td><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/130.png) 20 minutes - 45 minutes</p>
</blockquote></td>
<td><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/131.png) 12+ hours</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>* Times vary depending on the activity on the system.</p>
</blockquote></td>
<td><blockquote>
<p>![](clinical-lexicon-version-2-installation-guide/132.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](clinical-lexicon-version-2-installation-guide/133.png)Exporting the global with the indexes intact necessitates KILLing any previous version (Alpha or Beta test version) of the ^LEX global on your system.

### All Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sign into the system where you plan to install the Lexicon Utility data global ^LEX (this will probably be the same account where the Clinical Lexicon Utility V. 1.0 ^GMP global is located).

- NOTE: If the ^LEX global exists on your system (i.e., as a prior alpha or beta test version), KILL the ^LEX global before continuing.

### MSM Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- NOTE: Device names and path names may vary from site to site.

#### Load from Host File:

> If your site received the ^LEX data global via TCP/IP, FTP, or a network shared directory, load the global using the ^%GR (Global Restore) utility as follows:

#### Load from Tape:

> If your site received the ^LEX data global on 4mm tape, then load the global using the ^%GR (Global Restore) utility as follows:

<span id="_bookmark7" class="anchor"></span>Installation

### DSM Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- NOTE: Device names and path names may vary from site to site.

#### Load from Host File:

> If your site received the ^LEX data global via TCP/IP - FTP, then load the global using the ^%GTI (Global Transfer Input) utility as follows:

## Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify that DUZ, DUZ(“AG”), DT,DTIME, and U are defined and DUZ(0)=”@”.

### Load a Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Do ^XUP and select the “Kernel Installation & Distribution System” option, then select “Installation” menu.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 52%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>&gt;<strong>D ^XUP</strong></p>
<p>Setting up programmer environment Terminal Type set to: C-VT100 <strong>&lt;Enter&gt;</strong></p>
<p>Select OPTION NAME: <strong>Kernel Installation &amp; Distribution</strong> XPD MAIN Kernel Installation &amp; Distribution System</p>
<p>Edits and Distribution ... Utilities ...</p>
<p>Installation ...</p>
<p>Select Kernel Installation &amp; Distribution System Option: <strong>Installation</strong></p>
<p>Load a Distribution Print Transport Global</p>
<p>Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)</p>
<p>Restart Install of Package(s) Unload a Distribution</p>
<p>Backup a Transport Global</p>
<p>Select Installation Option: <strong>Load a Distribution</strong></p>
<p>Enter a Host File: <strong>LEX_2_0.KID</strong></p>
<p>KIDS Distribution saved on MMM DD, YYYY@HH:MM:SS Comment: Lexicon Utility v 2.0</p>
<p>This Distribution contains Transport Globals for the following Package(s):</p>
<p>LEXICON UTILITY 2.0 GMPL*2.0*7</p>
<p>Want to Continue with Load? YES// <strong>&lt;Enter&gt;</strong> YES Loading Distribution...</p>
<p>Want to RUN the Environment Check Routine? YES// <strong>&lt;Enter&gt;</strong></p>
<p>Will first run the Environment Check Routine, LEXIENV</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Update</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Lexicon Utility v 1.0</p>
</blockquote></td>
<td><blockquote>
<p>Problem List v 2.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>To</p>
</blockquote></td>
<td><blockquote>
<p>Lexicon Utility v 2.0</p>
</blockquote></td>
<td><blockquote>
<p>Problem List v 2.0*7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Use LEXICON UTILITY 2.0 to install this Distribution.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Verify Checksums in Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the "Installation” menu, select “Verify Checksums in Transport Global” to verify that all routines have the correct checksums.

> If there are any discrepancies, do not run the “Install Package(s)” option. Instead, run the “Unload a Distribution” option to remove the transport global from your system and call your IRM Field Office and report the problem.

### Install Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While installing the package, you are asked if you want to disable options. Please disable the following Problem List options:

> GMPL BUILD SELECTION LIST GMPL CLINICAL USER

> GMPL PROBLEM LISTING GMPL USER SCREEN

> From the "Installation” menu, select “Install Package(s)” and proceed with the install.

> If the Installation aborts, run the “Unload a Distribution” option to remove the “LEXICON UTILITY 2.0" transport global from your system. Call your IRM Field Office and report the problem.

### Installation Capture Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following example installation of the Lexicon Utility V. 2.0 was conducted on a DSM system into an account where the Clinical Lexicon Utility V. 1.0 existed. Within the example, MSM specific prompts and responses are added and marked as “MSM only.”

> Symbolic representations, such as MM/DD/YY@HH:MM:SS, are substituted for actual times in the listing below.

> Device ;C-OTHER is used to facilitate the capture.

> Lexicon Utility v 2.0 ;Created on MMM DD, YYYY@HH:MM:SS It consisted of the following Install(s):

> LEXICON UTILITY 2.0 GMPL\*2.0\*7

> Will first run the Environment Check Routine, LEXIENV Install Questions for LEXICON UTILITY 2.0

757. MAJOR CONCEPT MAP

> Note: You already have the 'MAJOR CONCEPT MAP' File.

> 757.001 CONCEPT USAGE

> 757.01 EXPRESSIONS

> Note: You already have the 'EXPRESSIONS' File.

> 757.011 EXPRESSION TYPE

> 757.014 EXPRESSION FORM

> Note: You already have the 'EXPRESSION FORM' File.

2.  CODES

> Note: You already have the 'CODES' File.

3.  CODING SYSTEMS

> Note: You already have the 'CODING SYSTEMS' File.

4.  EXCLUDED WORDS

> Note: You already have the 'EXCLUDED WORDS' File.

5.  REPLACEMENT WORDS

> Note: You already have the 'REPLACEMENT WORDS' File.

6.  UNRESOLVED NARRATIVES

> Note: You already have the 'UNRESOLVED NARRATIVES' File.

1.  SEMANTIC MAP

> Note: You already have the 'SEMANTIC MAP' File.

11. SEMANTIC CLASSES

> Note: You already have the 'SEMANTIC CLASSES' File.

12. SEMANTIC TYPES

> Note: You already have the 'SEMANTIC TYPES' File.

> 757.2 SUBSET DEFINITIONS (including data) Note: You already have the 'SUBSET DEFINITIONS' File. I will OVERWRITE your data with mine.

> 757.21 SUBSETS

> Note: You already have the 'SUBSETS' File.

> 757.3 LOOK-UP SCREENS

> Note: You already have the 'LOOK-UP SCREENS' File.

> 757.31 DISPLAYS

> 757.4 SHORTCUTS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>757.41 SHORTCUT CONTEXT Install Questions for GMPL*2.0*7</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//</p>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSM Only</p>
<p>Want to MOVE routines to other CPUs? NO// <strong>YES</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Enter options you wish to mark as 'Out Of Order': <strong>GMPL BUILD</strong></p>
<p><strong>SELECTION LIST</strong></p>
<p>Build Problem Selection List(s)</p>
<p>Enter options you wish to mark as 'Out Of Order': <strong>GMPL CLINICAL USER</strong></p>
<p>Patient Problem List</p>
<p>Enter options you wish to mark as 'Out Of Order': <strong>GMPL PROBLEM</strong></p>
<p><strong>LISTING</strong></p>
<p>Search for Patients having selected Problem</p>
<p>Enter options you wish to mark as 'Out Of Order': <strong>GMPL USER SCREEN</strong></p>
<p>Problem Look-up Defaults</p>
<p>Enter options you wish to mark as 'Out Of Order': <strong>&lt;Enter&gt;</strong> Enter protocols you wish to mark as 'Out Of Order': <strong>&lt;Enter&gt;</strong> Delay Install (Minutes): (0-60): 0// <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MSM Only - For all volume sets on your system which will use the Lexicon Utility</p>
<p>Please enter VOLUME SET you want me to update. Select VOLUME SET: <strong>PSB</strong></p>
<p>Are you adding ‘PSB’ as a new VOLUME SET (the 1ST for this</p>
<p>INSTALL)? <strong>Y</strong> (YES)</p>
<p>Select VOLUME SET: CSA</p>
<p>Are you adding ‘PSB’ as a new VOLUME SET (the 1ST for this INSTALL)? <strong>Y</strong> (YES)</p>
<p><em>etc.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// <strong>;C-OTHER</strong> VAX</p>
<p>Install Started for LEXICON UTILITY 2.0 :</p>
<p>MMM DD, YYYY@HH:MM:SS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Installing Routines:.....................................................</p>
<p>MMM DD, YYYY@HH:MM:SS</p>
<p>Running Pre-Install Routine: PRE^LEXILG. Saving Lexicon v 1.0 User Defaults</p>
<p>Removing Lexicon v 1.0 from the Multi-Term Look-up Utility (MTLU) Saving Lexicon v 1.0 Pointers</p>
<p>Renaming Lexicon v 1.0 Options</p>
<p>Old Name New Name</p>
<p>GMPT CLINICAL LEXICON MGT MENU LEX MGT MENU</p>
<p>Clinical Lexicon Management Menu Lexicon Management Menu</p>
<p>GMPT MGR EDIT TERM LEX MGR EDIT LEXICON</p>
<p>Edit a term Edit Lexicon</p>
<p>GMPT MGR DEFAULTS LEX MGR DEFAULTS</p>
<p>Defaults Defaults</p>
<p>GMPT CLINICAL LEXICON UTILITY LEX UTILITY</p>
<p>Clinical Lexicon Utility Lexicon Utility</p>
<p>GMPT CLINICAL LEXICON LOOK-UP LEX LOOK-UP</p>
<p>Clinical Lexicon Look-up Look-up Term</p>
<p>GMPT USER DEFAULTS LEX USER DEFAULTS</p>
<p>Lexicon Look-up Defaults User Defaults</p>
<p>GMPT MGR USER DEFAULTS LEX MGR USER DEFAULTS</p>
<p>Edit User/User Group Defaults Edit User/User Group Defaults</p>
<p>GMPT MGR LIST DEFAULTS LEX MGR LIST DEFAULTS</p>
<p>List User/User Group Defaults List User/User Group Defaults</p>
<p>GMPT MGR EDIT DEFN LEX MGR EDIT DEFN</p>
<p>Edit Term Definition Edit Term Definition</p>
<p>GMPL USER SCREEN GMPL USER LOOK-UP DEFAULTS</p>
<p>Problem Look-up Defaults Problem Look-up Defaults Deleting Lexicon v 1.0 Data Dictionaries</p>
<p>This might take quite a while, I've got 15 Data Dictionaries to Delete.</p>
<p>^GMP(757) DD Deleted</p>
<p>^GMP(757.01) DD Deleted</p>
<p>^GMP(757.014) DD Deleted</p>
<p>^GMP(757.02) DD Deleted</p>
<p>^GMP(757.03) DD Deleted</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ^GMP(757.04) DD Deleted

> ^GMP(757.041) DD Deleted

> ^GMP(757.05) DD Deleted

> ^GMP(757.06) DD Deleted

> ^GMP(757.1) DD Deleted

> ^GMP(757.11) DD Deleted

> ^GMP(757.12) DD Deleted

> ^GMPT(757.2) DD Deleted

> ^GMP(757.21) DD Deleted

> ^GMP(757.3) DD Deleted

> Installing Data Dictionaries: ....................

> MMM DD, YYYY@HH:MM:SS

> Installing Data:

> MMM DD, YYYY@HH:MM:SS

> Installing PACKAGE COMPONENTS:

> Installing OPTION......................

> MMM DD, YYYY@HH:MM:SS

> Running Post-Install Routine: POST^LEXILG.

> Restoring Lexicon User Defaults for use with Lexicon v 2.0 Repointing Files/Fields for use with Lexicon v 2.0

> PROBLEM SELECTION CATEGORY CONTENTS SELECTION

> IMP/EXP SELECTION V POV

> PROBLEM

> PROVIDER NARRATIVE

> Checking for GMPT Package file entry (not used in Lexicon v 2.0) GMPT Package File entry was found

> The GMPT namespace was used by the Clinical Lexicon Utility version 1.0. The GMPT Package File entry may be deleted.

> Checking for ^GMP or ^GMPT (not used in Lexicon v 2.0)

> ^GMP Global Found

> ^GMPT Global Found

> Don't forget to delete the ^GMP and ^GMPT globals used by the Clinical Lexicon Utility, version 1.0

> Press \<Return\> to continue \<Enter\>

> Updating Routine file......

> Updating KIDS files.......

> LEXICON UTILITY 2.0 Installed.

> MMM DD, YYYY@HH:MM:SS

### Build File Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines, options and globals) exported with this software.

### Install File Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

# Post-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Package Installation Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Kernel Installation and Distribution System generates a package installation message. This message reports the installation of the Lexicon Utility V. 2.0 on FORUM.

> Example of Lexicon Utility Package Installation message:

## Post-Installation Routine Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Post-Installation routine generates two (2) post-install messages.

#### Lexicon Installation Message

> This message reports the results of the installation of the Lexicon Utility

> V. 2.0 to the Salt Lake City IRM Field Office. The purpose is to check for unusual events in the installation sequence.

> Example of Lexicon Utility Installation message:

#### Problem List Survey Message

> This message reports the results of the Problem List update initiated by the Lexicon Utility V. 2.0 in the Post-Installation routine. It will report the contents of the Problem List Problem file and any updates which occur as a result of the installation of the Lexicon Utility V. 2.0.

> Example of Problem List Survey message:

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reactivate the options that you placed “OUT OF ORDER.” These options include:

> GMPL BUILD SELECTION LIST GMPL CLINICAL USER

> GMPL PROBLEM LISTING

> GMPL USER LOOK-UP DEFAULTS

- NOTE: GMPL USER LOOK-UP DEFAULTS was renamed from GMPL USER SCREEN.

<span id="_bookmark14" class="anchor"></span>Post-Installation

### Purge Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (Optional) Remove the Environment Check, Pre-Installation routine and Post-Installation routine with the LEXI\* namespace.

### Translation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review the translation tables to make sure that the Lexicon Utility data global (^LEX) is appropriately translated.

### Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the Lexicon Utility V. 2.0 is installed in all UCIs where the Clinical Lexicon Utility V. 1.0 was installed, it is safe to delete the ^GMP and

> ^GMPT globals. This will free up approximately 45 mb.

### Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Restore the environment. If you expanded your symbol table, buffer size, or partition size prior to installation, reduce the environment parameters to their original values.

> This page intentionally left blank

# Appendix: Release Notes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Changes since version 1.0:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Terminology Added

> The Common Procedural Terminology (CPT-4) and the Diagnostic and Statistical Manual of Mental Disorders (DSM-IV) have been added to the Lexicon Utility.

#### Namespace LEX Changed

> The namespace was changed from GMPT to LEX. All routines and package variables have been renamed from GMPT\* to LEX\* to conform to the new namespace.

#### Global Root ^LEX Changed

> The global roots have been changed from ^GMP and ^GMPT to ^LEX and

> ^LEXT respectively. This was done to prevent inadvertent deletion of Lexicon data.

> The difference between typing ^TMP and ^GMP is one character on a standard QWERTY keyboard, both controlled by the same finger and located approximately a quarter of an inch from each other.

#### Concept Usage file 757.001 Added

> The Concept Usage file records the usage of Lexicon by applications performing lookups using the Special Lookup Routines. This Concept Usage is later used to determine the order of the selection list during lookup. The more frequently used terms "float" to the top of the list.

#### Expression Type file 757.011 Added

> The Expression Type field (757.01) has been changed from a set of codes to a pointer to the new file Expression Type, \#757.011.

#### Shortcut Functionality Added

> The Shortcuts File 757.4 and the Shortcuts Context file 757.41 were added to support shortcuts by context.

#### Shortcut User Default Added

> Context-sensitive shortcuts have been added as a user default. For example, the user may have one set of shortcuts for searching in the Problem List application and another set defined for another application.

#### Excluded String File Deleted

> Excluded String File \#757.041 was deleted. This file was required to run the Lexicon Special Lookup Routine under the Multi-Term Lookup Utility (MTLU) v 1.0 running on the VAX. With the upgrade of the MTLU and conversion of VAX to Alpha, this file no longer serves a purpose.

#### Silent Lookup Added

> A Silent Lookup was added in support of GUI applications. The Lexicon Special Lookup Routine has been modified to call the Silent Lookup so that the behavior of the "loud" lookup would be identical to the "silent" lookup. This lookup also includes:

1)  Reordering the selection list with the most frequently used at the top.
2)  Placing the exact match at the top of the selection list.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *A*
> AICS 9
> Automated Information Collection System 9
> *B*
> Build File 26
> *C*
> Checksums 18
> CPT file 9
> CPT-4 1, 31
> *D*
> Database Integration Agreements 5
> Delete
> changes 32
> data dictionaries 3, 10, 12
> files 3
> globals 2, 29
> not 27
> package components 2
> routines 4
> safe to 29
> Deleted
> at site 3
> Disk Space 2
> DSM file 9
> DSM-IV 1, 31
> DUZ 10, 17
> *E*
> Environment 29
> *F*
> Fileman 9
> Files 2
> *G*
> Global Management 11
> Global Root 9, 31
> Globals 1, 2, 11, 15, 26, 27, 29
> ^AUPNPROB 9
> ^ICD0 9
> ^ICD9 9
> ^ICPT 9
> ^VA 9
> ^YSD 9
> delete 29
> initialize 11
> install 2, 11, 13
> not delete 2
> root 1
> size 2
> translation 11, 29
> transport 18
> *I*
> ICD Diagnosis file 9
> ICD Procedures file 9
> ICD-9 1
> ICD-9 28
> Indexes. 13
> Install
> data dictionaries 3, 10
> files 4
> globals 2, 11, 13
> routines 4
> Install File 26
> Installation Message 27
> lexicon 27
> package 27
> Problem List 28
> *K*
> Kernel 9
> KIDS 2, 17
> Build File 26
> Install File 26
> load a distribution 17
> transport globals. 18
> unload a distribution 19
> verify checksums 18
> *M*
> Mailman message 2
> *N*
> Namespace 5
> Namespace 1, 29, 31
> New Person file 9
> *O*
> Options
> disable 10, 18
> reactivate 28
> rename 6
> *P*
> Patient Care Encounter 9
> PCE Patient/IHS Subset 9
> Post-Install 12, 27
> Pre-Install 9, 12
> Problem file 9, 12, 28
> Problem List , 5, 6, 7, 9, 10, 28
> options 6, 7, 18
> problem file 12, 28
> routines 5
> shortcuts 32
> survey 28
> Protection 11
> *R*
> Routines
> delete 4
> install 4
> *S*
> Semantic 4
> Shortcuts 7, 32
> file 2, 4, 32
> Special Lookup 10, 27, 31
> Subset Definitions
> file 2, 4
> Subsets 4, 9
> *T*
> Text Integration Utility i
> TIU i
> Toolkit 9
> Translation 11, 29
> Transport Globals 18
