---
title: VIST Version 4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: ANRV
app_name: Visual Impairment Service Team (VIST)
section: CLI
app_status: active
pkg_ns: ANRV
patch_ver: 4
patch_id: ANRV*4
group_key: "ANRV:ANRV:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vist
  - table
  - contents
  - install
  - installation
  - files
  - during
  - routines
  - visual
  - impairment
page_count: 0
word_count: 1002
section_count: 11
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Visual_Impair_Svc_Team_(VIST)/vist_4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=106"
---

![](vist-version-4-installation-guide/001.png)

VISUAL IMPAIRMENT SERVICE TEAM(VIST)Installation Guide(Revised)

June 1998

Office of the Chief Information Officer

Table of Contents

Introduction [1](#introduction)

Pre Installation [1](#pre-installation)

Options to be Deleted during Install [2](#options-to-be-deleted-during-install)

Templates to be Deleted during Install [2](#templates-to-be-deleted-during-install)

Routines to Delete [5](#routines-to-delete)

Routines [5](#routines)

Installation [5](#installation)

Sample KIDS Install [5](#sample-kids-install)

Post Installation [8](#post-installation)

System Configuration [8](#system-configuration)

Resources Requirements [8](#_Toc415556445)

Routine Mapping [8](#_Toc415556446)

Journaling Globals [8](#_Toc415556447)

Files [9](#files)

Security Keys [9](#security-keys)

Technical Assistance [9](#technical-assistance)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre Installation](#pre-installation)
  - [Options to be Deleted during Install](#options-to-be-deleted-during-install)
  - [Templates to be Deleted during Install](#templates-to-be-deleted-during-install)
  - [Routines to Delete](#routines-to-delete)
- [Routines](#routines)
- [Installation](#installation)
  - [Sample KIDS Install](#sample-kids-install)
- [Post Installation](#post-installation)
  - [System Configuration](#system-configuration)
  - [Resources Requirements](#resources-requirements)
  - [Routine Mapping](#routine-mapping)
  - [Journaling Globals](#journaling-globals)
- [Files](#files)
  - [Security Keys](#security-keys)
  - [Technical Assistance](#technical-assistance)
> It is recommended that this software be loaded into a test account before going into production.
> It is *very important* to read these instructions completely before installing this software! Read these instructions through at least once before attempting to install.
During the installation of VIST V. 4.0, all data entered using the class III Blind Rehabilitation software will be moved into the new files created for VIST V. 4.0. This conversion time will vary depending on the amount of patient information that was entered into the class III files.
> This version (4.0) of the Visual Impairment Service Team software package can only be run with a standard M operating system. It also requires the following VA software applications:
> <u>Package</u> <u>Minimum Version Needed</u>
> VA FileMan 21.0
> Kernel 8.0
> Patient Information
> Management System (PIMS) 5.3
> Fee Basis 3.5
> The above software is not included in this package and must be installed before this package is completely functional.

# Pre Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(1\) Performing a system backup before running the KIDS install is highly recommended. We also recommend that you install the Visual Impairment Service Team (VIST) package with no VIST users on the system.

> \(2\) System Configuration: ^ANRV is a new global and will need to be journaled after installation. There are no specific guidelines for system configuration or global placement for the VIST software.

> \(3\) Installation time will take 10 to 15 minutes. The times for the installation will depend on the amount of data in your system and whether you are using a VAX or PC. Installation will take longer on a VAX system.

> \(4\) To begin installing the VIST package use the *Kernel Installation & Distribution System* \[XPD MAIN\] option. Load the ANRV_4_0.KID distribution file using the option *Load a Distribution* \[XPD LOAD DISTRIBUTION\]. Next, you can verify routine checksums using the option *Verify Checksums in Transport Global* \[XPD PRINT CHECKSUM\]. Finally, install the package using the Install Package(s) \[XPD INSTALL BUILD\] option. An example of the installation process is included in this section.

## Options to be Deleted during Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                     |                             |
|---------------------|-----------------------------|
| Option Name     | Menu Text               |
| ANRV ASSESSMENT INQ | Individual Assessment - Old |

## Templates to be Deleted during Install 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                       |          |
|-----------------------|----------|
| Input             | File |
| ANRV EDIT CHECKLIST   | 623061   |
| ANRV EDIT LETTER      | 623033   |
| ANRV VIST PARM        | 623050   |
| ANRVACE               | 623036   |
| ANRVEID               | 623158   |
| ANRVRE                | 623158   |
| ANRVRRE               | 623160   |
|                       |          |
| Print             | File |
| ANRV ADDRESS LIST     | 623158   |
| ANRV ADDRESS LIST HDR | 623158   |
| ANRV AGE LIST         | 623158   |
| ANRV ASSESSMENT INQ   | 623158   |
| ANRV BIRTH LIST       | 623158   |
| ANRV CHECKLIST        | 623061   |
| ANRV CITY LIST        | 623158   |
| ANRV CLAIM REC INQ    | 623036   |
| ANRV COUNTY LIST      | 623158   |
| ANRV DECEASED LIST    | 623158   |
| ANRV ELIG AMIS LIST   | 623158   |
| ANRV EYE DIAG INQ     | 623158   |
| ANRV EYE DIAG LIST    | 623158   |
| ANRV EYE DIAG NAR     | 623158   |
| ANRV EYE DIAG PRINT   | 623158   |

|                     |          |
|---------------------|----------|
| Print (cont’d)  | File |
| ANRV FEE PT         | 623158   |
| ANRV INC AMIS       | 623158   |
| ANRV MAIL LABELS    | 623158   |
| ANRV ML BY CITY     | 623158   |
| ANRV ML BY COUNTY   | 623158   |
| ANRV POS LIST       | 623158   |
| ANRV PRINT LETTER   | 623158   |
| ANRV REFERRAL LIST  | 623158   |
| ANRV REVIEW INQ     | 623158   |
| ANRV ROSTER A/R     | 623158   |
| ANRV STATE LIST     | 623158   |
| ANRV ZIP CODE LIST  | 623158   |
| ANRVACP             | 623036   |
| ANRVAP              | 623158   |
| ANRVED              | 623158   |
| ANRVFVD             | 623158   |
| ANRVID              | 623158   |
| ANRVPR              | 623160   |
| ANRVREV             | 623158   |
| ANRVRP1             | 623158   |
| ANVRRL              | 623160   |
|                     |          |
| Sort            | File |
| ANRV ADDRESS LIST   | 623158   |
| ANRV AGE LIST       | 623158   |
| ANRV BIRTH LIST     | 623158   |
| ANRV CHECKLIST      | 623061   |
| ANRV CITY LIST      | 623158   |
| ANRV COUNTY LIST    | 623158   |
| ANRV DECEASED LIST  | 623158   |
| ANRV ELIG AMIS LIST | 623158   |
| ANRV EYE DIAG LIST  | 623158   |
| ANRV EYE DIAG NAR   | 623158   |
| ANRV EYE DIAG PRINT | 623158   |
| ANRV FEE PT         | 623158   |
| ANRV INC AMIS       | 623158   |
| ANRV MAIL LABELS    | 623158   |
| ANRV ML BY CITY     | 623158   |
| ANRV ML BY COUNTY   | 623158   |
| ANRV ML BY STATE    | 623158   |
| ANRV POS LIST       | 623158   |
| Sort (cont’d)   | File |
| ANRV REFERRAL LIST  | 623158   |
| ANRV STATE LIST     | 623158   |
| ANRV ZIP CODE LIST  | 623158   |
| ANRVACP             | 623036   |
| ANRVAD              | 623158   |
| ANRVAP              | 623158   |
| ANRVED              | 623158   |
| ANRVFVD             | 623158   |
| ANRVID              | 623158   |
| ANRVPR              | 623160   |
| ANRVREV1            | 623158   |
| ANRVRP1             | 623158   |
| ANRVRRL             | 623160   |

## Routines to Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ANRVPRE, ANRVPST, ANRVZ\*, and ANRV1\* routines will be deleted.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of routines you will see for VIST when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (*First Line Routine Print*) to print a list of just the first line of each ANRV\* routine.

|          |         |         |         |          |
|----------|---------|---------|---------|----------|
| ANRVAM1  | ANRVAM2 | ANRVAP  | ANRVDEL | ANRVLET  |
| ANRVML   | ANRVML1 | ANRVML2 | ANRVML3 | ANRVML4  |
| ANRVPOST | ANRVPR  | ANRVPR1 | ANRVPR2 | ANRVRP   |
| ANRVRP2  | ANRVRP3 | ANRVRP4 | ANRVRP5 | ANRVRP6  |
| ANRVRP7  | ANRVRP8 | ANRVRP9 | ANRVRRL | ANRVSITE |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Sample KIDS Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\><u>D ^XUP</u>

Setting up programmer environment

Terminal Type set to: <u>C-VT100</u>

Select OPTION NAME: <u>XPD MAIN</u> Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option: <u>INSTALL</u>ation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>LOAD</u> a Distribution

Enter a Host File: ANRV_4_0.KID

KIDS Distribution saved on Jun 10, 1998@18:31:57

Comment: Visual Impairment Service Team (VIST) 4.0

This Distribution contains Transport Globals for the following Package(s):

Visual Impairment Service Team (VIST) 4.0

Want to Continue with Load? YES// <u>\<Enter\></u>

Loading Distribution...

Visual Impairment Service Team (VIST) 4.0

Use INSTALL NAME: Visual Impairment Service Team (VIST) 4.0 to install this Distribution.

> Note: At this point, you can run the *Verify Checksum in Transport Global* \[XPD PRINT CHECKSUM\] option. If any of the routine checksums failed, you should not proceed with the installation process. Contact your distributing CIO Field Office.

Select Installation Option: <u>INSTA</u>ll Package(s)

Select INSTALL NAME: Visual Impairment Service Team (VIST) 4.0 Loaded from Distribution 6/10/98@12:58:45

=\> VIST 4.0 ;Created on Mar 23, 1998@12:57:50

This Distribution was loaded on Jun 10, 1998@12:58:45 with header of

VIST TEST INSTALL ;Created on Jun 10, 1998@12:57:50

It consisted of the following Install(s):

Visual Impairment Service Team (VIST) 4.0

Visual Impairment Service Team (VIST) 4.0

Install Questions for Visual Impairment Service Team (VIST) 4.0

Incoming Files:

2040 VIST ROSTER

2041 VIST PARAMETERS

2041.5 VIST EYE DIAGNOSIS (including data)

2041.6 VIST CHECKLIST OPTIONS (including data)

2041.7 VIST BENEFITS AND SERVICES CHECKLIST (including data)

2042 VIST REFERRAL FACILITY (including data)

2042.5 VIST REFERRAL ROSTER

2043 VIST LETTER (including data)

2043.5 VARO CLAIMS

2044 VIST LOCAL BENEFITS AND SERVICES (including data)

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Want to MOVE routines to other CPUs? NO// <u>\<ENTER\></u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: *\[Select Print Device\]*

Install Started for Visual Impairment Service Team (VIST) 4.0 :

Jun 10, 1998@14:28:59

Installing Routines:.......................

Jun 10, 1998@14:29:04

Installing Data Dictionaries: ...........

Jun 10, 1998@14:29:20

Installing Data:

Jun 10, 1998@14:29:23

Installing PACKAGE COMPONENTS:

Installing FUNCTION..

Installing PRINT TEMPLATE...................................................

.....

Installing SORT TEMPLATE...................................................

Installing INPUT TEMPLATE................

Installing OPTION.....................................................

Jun 10, 1998@14:30:25

Running Post-Install Routine: ^ANRVPOST.

Updating Routine file......

Updating KIDS files.......

Visual Impairment Service Team (VIST) 4.0 Installed.

Jun 10, 1998@14:30:33..

Install Message sent \#26535

An Option(s) has been added by this build.

Electing to rebuild menus now is highly recommended.

Do you want to rebuild Menu's now? Y// <u>NO</u> *\[It is recommended that you respond “No” to this prompt.\]*

# Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the installation of VIST V. 4.0, all data entered using the class III Blind Rehabilitation software will be moved into the new files created for VIST V. 4.0. This conversion time will vary depending on the amount of patient information that was entered into the class III files.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ^ANRV is a new global and will need to be journaled after installation. There are no specific guidelines for system configuration or global placement for the Visual Impairment Service Team software.

<span id="_Toc415556445" class="anchor"></span>

## Resources Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version (4.0) of VIST contains approximately 25 routines including all ANRV\* routines and compiled templates that take up approximately 69 K disk space.

<span id="_Toc415556446" class="anchor"></span>

## Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is not necessary to map routines.

<span id="_Toc415556447" class="anchor"></span>

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the ^ANRV global be journaled after installation.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires the 10 files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

> The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use VA FileMan option *List File Attributes* \[DILIST\]*,* under *Data Dictionary Utilities* \[DI DDU\], to print the DDs. The following are the files for which you should print DDs:

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

-------------------------------------------------------------------------------

2040 VIST ROSTER YES NO NO

2041 VIST PARAMETERS YES NO NO

2041.5 VIST EYE DIAGNOSIS YES NO YES MERG NO NO

2041.6 VIST CHECKLIST OPTIONS YES NO YES MERG NO NO

2041.7 VIST BENEFITS AND SERVICES YES NO NO

CHECKLIST

2042 VIST REFERRAL FACILITY YES NO YES MERG NO NO

2042.5 VIST REFERRAL ROSTER YES NO NO

2043 VIST LETTER YES NO YES MERG NO NO

2043.5 VARO CLAIMS YES NO NO

2044 VIST LOCAL BENEFITS AND YES NO YES MERG NO NO

SERVICES

The namespace for the VIST package is ANRV.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are *no* security keys for the VIST software package.

## Technical Assistance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you experience problems of a technical nature with this software package, you are encouraged to contact the CUSTOMER SERVICE NATIONAL HELP DESK.