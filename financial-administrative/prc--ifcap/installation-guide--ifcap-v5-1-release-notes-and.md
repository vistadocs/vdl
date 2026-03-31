---
title: IFCAP Version 5.1 Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes and
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: []
security_keys: []
menu_options: 0
description: IFCAP V. 5.1 does not introduce new functionality. It is a fully patched version of IFCAP V. 5.0, which depends upon the site’s reference tables (files) being already populated.
audience: 
keywords: 
  - ifcap
  - table
  - contents
  - installation
  - install
  - prcst
  - options
  - distribution
  - order
  - wish
page_count: 0
word_count: 3625
section_count: 18
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

### ![](ifcap-version-5-1-release-notes-and-installation-guide/001.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integrated Funds, Distribution,Control Point Activity, AccountingAnd Procurement (IFCAP)RELEASE NOTESandINSTALLATION GUIDE

October 2000

V*IST*A Technical Services

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [![](ifcap-version-5-1-release-notes-and-installation-guide/001.png)](#ifcap-version-5-1-release-notes-and-installation-guide001png)
- [Preface](#preface)
  - [## Purpose of the Release Notes](#purpose-of-the-release-notes)
  - [## Purpose of the Installation Guide](#purpose-of-the-installation-guide)
  - [## Reference Numbering System](#reference-numbering-system)
- [# Chapter 1 Release Notes](#chapter-1-release-notes)
  - [Overview](#overview)
  - [Types of Changes](#types-of-changes)
    - [New Third Line on Routines](#new-third-line-on-routines)
    - [Remove Obsolete Terminology](#remove-obsolete-terminology)
    - [Corrections to Routines](#corrections-to-routines)
    - [Developer-Initiated Issue](#developer-initiated-issue)
  - [## Alpha/Beta Testing Issue](#alphabeta-testing-issue)
  - [## National On-line Information System (NOIS) Messages](#national-on-line-information-system-nois-messages)
    - [Overview](#overview-1)
    - [NOIS Messages addressed](#nois-messages-addressed)
- [Chapter 2 Introduction to Installation](#chapter-2-introduction-to-installation)
  - [## Overview](#overview-2)
  - [General Information](#general-information)
    - [Namespace](#namespace)
    - [### Package Dependencies](#package-dependencies)
    - [IFCAP File Range](#ifcap-file-range)
    - [### ### Global Placement/Description](#global-placementdescription)
    - [### Required Resources (Hardware/Software)](#required-resources-hardwaresoftware)
    - [Refer to the IFCAP V. 5.1 Technical Manual, under the section entitled "Implementation and Maintenance".](#refer-to-the-ifcap-v-51-technical-manual-under-the-section-entitled-implementation-and-maintenance)
  - [# # Chapter 3 Pre-Installation](#chapter-3-pre-installation)
  - [## Overview](#overview-3)
  - [Advance Pre-Installation Procedures](#advance-pre-installation-procedures)
  - [Immediate Pre-Installation Procedures](#immediate-pre-installation-procedures)
- [Chapter 4 Installation](#chapter-4-installation)
  - [Overview](#overview-4)
  - [Starting the IFCAP Installation](#starting-the-ifcap-installation)
- [9)  Enter YES at the “Want to RUN the Environment Check Routine?” prompt. The environment check routine now runs.](#9-enter-yes-at-the-want-to-run-the-environment-check-routine-prompt-the-environment-check-routine-now-runs)
- [REMINDER for MSM sites: Copy the IFCAP routines, including the compiled template routines, to <u>ALL</u> accounts.](#reminder-for-msm-sites-copy-the-ifcap-routines-including-the-compiled-template-routines-to-uallu-accounts)
    - [### ### Sample Session of IFCAP V. 5.1 Installation](#sample-session-of-ifcap-v-51-installation)
- [\>D ^XUP](#d-xup)
  - [Re-starting the IFCAP Installation](#re-starting-the-ifcap-installation)
- [Chapter 5  Post-Installation](#chapter-5-post-installation)
  - [Assignment of Mail Groups](#assignment-of-mail-groups)

## ## Purpose of the Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Notes section of this document describes the new features and functionality of IFCAP V. 5.1.

## ## Purpose of the Installation Guide 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Installation Guide provides the information necessary to install the IFCAP V. 5.1 software package.

> **NOTE:** The Technical Manual and Security Guide for IFCAP V. 5.1 are presented separately.

## ## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

(This page is intentionally left blank)

Table Of Contents

[5.1 Assignment of Mail Groups [29](#assignment-of-mail-groups)](#assignment-of-mail-groups)

# # Chapter 1 Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP V. 5.1 does not introduce new functionality. It is a fully patched version of IFCAP V. 5.0, which depends upon the site’s reference tables (files) being already populated.

This version was developed because there were more than 225 patches released for IFCAP V. 5.0. As more and more patches were released, it became obvious that not all sites had installed all the patches in the correct sequence. This introduced site-specific errors and problems.

Also, as the VA is moving toward its coreFLS initiative, the release of IFCAP V. 5.1 provides a stable, baseline application at all sites for possible conversion of data.

## Types of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several corrections will be introduced in IFCAP V. 5.1. These changes have no effect on the functionality of the system. The types of corrections are:

- New third line on all routines
- Remove obsolete terminology
- Corrections to routines
- Developer-initiated issue
- Alpha/Beta testing issue

### New Third Line on Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To curtail unauthorized local revisions to IFCAP routines, the following third line is added to all routines:

> “Per VHA Directive 10-93-142, this routine should not be modified.”

### Remove Obsolete Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following obsolete phrases located in on-line help and option descriptions are being revised and replaced where appropriate.

|                                                 |                        |
|-------------------------------------------------|------------------------|
| OBSOLETE PHRASE                             | REPLACEMENT PHRASE |
| Supply                                          | A&MM                   |
| Subaccount                                      | BOC                    |
| CALM                                            | FMS                    |
| Rocky Mountain National Bank OR RMB OR Citibank | Credit Card Vendor     |

### Corrections to Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Removed the text “\<\<= NOT VERIFIED \>” from the end of the first line of the following routines:

> PRCFFU17

> PRCFPR1

> PRCHDAM3

> PRCHDAM5

> PRCHDP5

PRCHDSP4

> PRCHSPD6

> PRCHPAM2

> PRCHPAM4

> PRCHPAM6

> PRCS826

> PRCSAPP2

- Removed the variable “U” from an argument list in a Kill statement at line OUT in routine PRCBR1 to conform to SAC Standard 2.3.1.5.1.
- Removed a blank character at the end of line BEGIN+2 in routine PRCSFMS.

### Developer-Initiated Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CORRECTION TO PROBLEM WITH AMENDING FCP

IFCAP V. 5.0 did not successfully handle the obligation of amended documents if both the FCP and cost center were modified in the same amendment. V. 5.1 corrects this deficiency and allows the obligation process to complete successfully.

## ## Alpha/Beta Testing Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FCP LOOKUP FIXES

> This issue surfaced during the course of alpha and beta testing. The FCP lookup in the following options is corrected so that FCP 007 does not appear in the pick list when one enters a FCP whose numeric part equals the ien of a fund used for a Fund Control Point whose Administrative Office is VHA.

> Display Control Point Official's Balance

> Running Balances

> New 2237

> New 1358

> New Purchase Order

> Amendment to Purchase Order

> Purchase Card Registration

> Assign LOG Department Number to Fund Control Point

## ## National On-line Information System (NOIS) Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As users discover problems with V*IST*A software, they are encouraged to contact the National V*IST*A Support (NVS) staff. NVS will attempt to reproduce the problem. If they find that there is a software problem in the nationally released software, they enter a NOIS and refer it to Technical Services for resolution. NOIS messages are created on the FORUM bulletin board system and are sent as electronic mail to the g.nois FORUM mail group.

### NOIS Messages addressed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following NOIS are being addressed by the release of IFCAP V. 5.1.

#### NOIS Message: ISW-0500-20461

> The second line of routine PRCH58OB is missing a semicolon before the patch list.

(This page is intentionally left blank.)

# Chapter 2 Introduction to Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter discusses prerequisites that must be satisfied before the IFCAP V. 5.1 software can be installed. The following topics are discussed:

- Assigned namespace
- Package dependencies
- File ranges
- System configuration and global placement
- Required hardware and software resources

## General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that IFCAP V. 5.1 be installed first in a site’s test or mirror account, it any exists, prior to installation in the production account.

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP has been assigned PRC as its namespace but it excludes:

- PRCA\* (Accounts Receivable)
- PRCN\* (Equipment/Turn-In Request)
- PRCZ\* (Reserved for local modifications).

### ### Package Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of the following packages must be accomplished for IFCAP V. 5.1 to function properly:

- Kernel V. 8.0
- ToolKit V. 7.3
- VA FileMan V. 22.0
- PIMS V. 5.3 or higher
- Generic Code Sheets V. 2.0
- List Manager V. 1.0
- OE/RR V. 3.0 or higher

### IFCAP File Range 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file range for IFCAP V. 5.1 is 410 through 447, <u>excluding</u> 412, 413, and 430 through 439.9. Files 414, 415, 416, 418, 419, 425 and 429 are not currently in use, but are reserved for the IFCAP package.

### ### ### Global Placement/Description 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure that the listed IFCAP globals are properly set in your production UCI before proceeding:

- ^PRC
- ^PRCD
- ^PRCF
- ^PRCH
- ^PRCP
- ^PRCS
- ^PRCT
- ^PRCU

If not, execute the appropriate utility to set them up. Access Privileges should be RW (Read and Write).

### ### Required Resources (Hardware/Software)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Refer to the IFCAP V. 5.1 Technical Manual, under the section entitled "Implementation and Maintenance".

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## # # Chapter 3 Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter details the procedures to be performed as part of the IFCAP V. 5.1 pre-installation process.

## Advance Pre-Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following procedure may be performed well in advance of your installation of IFCAP V. 5.1. If your site has already run one of these steps previously, it need not be repeated.

1.  Run the A2AP utility for IFCAP 5.0. This utility checks the second line of each routine to check that all expected patches are listed. If you have missing patches, file a NOIS for assistance from NVS.
2.  Install patch PRC\*5\*987 to test the integrity of your IFCAP routines and to identify any local modifications that will be overwritten by installing IFCAP V. 5.1. The report provides a list of IFCAP V 5.0 routines installed on your system. If you find a routine that does not match the standard IFCAP routine and you do not know what modification was made, you can file a NOIS for assistance from NVS.
3.  OPTIONAL: Print the Entry/Exit Actions for your IFCAP V. 5.0 options. This FileMan report will be helpful if you have made any local changes to logic involved upon entering or exiting option.

UCI,VOL\>D Q^DI

> Select OPTION: PRINT FILE ENTRIES

> OUTPUT FROM WHAT FILE: OPTION//

> SORT BY: NAME//

> START WITH NAME: FIRST// PRC

> GO TO NAME: LAST// PRC~

> WITHIN NAME, SORT BY: \$E(#.01,1,4)'="PRCA"

> WITHIN \$E(#.01,1,4)'="PRCA", SORT BY: \$E(#.01,1,4)'="PRCN"

> WITHIN \$E(#.01,1,4)'="PRCN", SORT BY: \$E(#.01,1,4)'="PRCZ"

> WITHIN \$E(#.01,1,4)'="PRCZ", SORT BY:

> STORE IN 'SORT' TEMPLATE:

> FIRST PRINT FIELD: NAME;C1

> THEN PRINT FIELD: ENTRY ACTION;C10

> THEN PRINT FIELD: EXIT ACTION;S1;C10

> THEN PRINT FIELD:

> Heading (S/C): OPTION LIST// IFCAP OPTION ENTRY/EXIT ACTIONS

> STORE PRINT LOGIC IN TEMPLATE:

> START AT PAGE: 1//

> DEVICE: Printer

4.  OPTIONAL: Print the menu options for your IFCAP V. 5.0 system. This FileMan report will be useful if you have added or edited options in the nationally released IFCAP menu as these changes may disappear with the installation of IFCAP V. 5.1.

UCI,VOL\>D Q^DI

> Select OPTION: SEARCH FILE ENTRIES

> OUTPUT FROM WHAT FILE: OPTION//

> -A- SEARCH FOR OPTION FIELD: TYPE

> -A- CONDITION: eqUALS

> -A- EQUALS: menu

> -B- SEARCH FOR OPTION FIELD:

> IF: A// TYPE EQUALS "M" (menu)

> STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: NAME//

> START WITH NAME: FIRST// PRC

> GO TO NAME: LAST// PRC~

> WITHIN NAME, SORT BY: \$E(#.01,1,4)'="PRCA"

> WITHIN \$E(#.01,1,4)'="PRCA", SORT BY: \$E(#.01,1,4)'="PRCN"

> WITHIN \$E(#.01,1,4)'="PRCN", SORT BY: \$E(#.01,1,4)'="PRCZ"

> WITHIN \$E(#.01,1,4)'="PRCZ", SORT BY:

> STORE IN 'SORT' TEMPLATE:

> FIRST PRINT FIELD: \[CAPTIONED

> Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no

> Computed Fields

> Heading (S/C): OPTION SEARCH// IFCAP MENU OPTION SEARCH

> START AT PAGE: 1//

> DEVICE: Printer

5.  OPTIONAL: Print the lock search for IFCAP V. 5.0. This FileMan report helps identify local customization with regard to Security Keys in the LOCK field of an option.

UCI,VOL\>D Q^DI

> Select Option: Search File Entries

> OUTPUT FROM WHAT FILE: // 19 OPTION (11541 entries)

> -A- SEARCH FOR OPTION FIELD: LOCK

> -A- CONDITION: 'NULL

> -B- SEARCH FOR OPTION FIELD:

> IF: A// LOCK NOT NULL

> STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: NAME//

> START WITH NAME: FIRST// PRC

> GO TO NAME: LAST// PRC~

> WITHIN NAME, SORT BY: \$E(#.01,1,4)'="PRCA"

> WITHIN \$E(#.01,1,4)'="PRCA", SORT BY: \$E(#.01,1,4)'="PRCN"

> WITHIN \$E(#.01,1,4)'="PRCN", SORT BY: \$E(#.01,1,4)'="PRCZ"

> WITHIN \$E(#.01,1,4)'="PRCZ", SORT BY:

> STORE IN 'SORT' TEMPLATE:

> FIRST PRINT FIELD: \[CAPTIONED

> Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no

> Computed Fields

> Heading (S/C): OPTION SEARCH// IFCAP OPTIONS WITH LOCKS

> START AT PAGE: 1//

> DEVICE: Printer

## Immediate Pre-Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following procedure should be done immediately before installing IFCAP V. 5.1.

1.  Make sure you have a WORKING backup of your system.
2.  Backup your IFCAP namespace routines (see section ) to a host file.
3.  Ensure you have adequate journaling space.
4.  DSM for Open VMS sites only - Disable routine mapping for routines in the IFCAP namespace (see section ), if mapping is enabled.

> (This page intentionally left blank.)

# Chapter 4 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that IFCAP V. 5.1 be installed in the test or mirror account at the site (if any exists) before installing it into the production account. This version should be installed during off hours while all IFCAP, Fee Basis and Prosthetics users are off the system.

The following installation procedures should be used for all accounts.

## Starting the IFCAP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install IFCAP V. 5.1 software over IFCAP V. 5.0:

1)  FTP the distribution file IFCP5_1.KID from the anonymous.software directory of any of the OI Field Offices and addresses listed below:

Hines REDACTED

Albany REDACTED

Salt Lake REDACTED

2)  Insure all IFCAP, Fee Basis, and Prosthetics users are off the system.
3)  Enter D ^XUP in programming mode to set up all appropriate variables.
4)  Enter XPD MAIN at the “Select OPTION NAME:” prompt to invoke the Kernel Installation & Distribution System.
5)  Enter INSTALL at the “Select Kernel Installation & Distribution System Option:” prompt.
6)  Enter LOAD at the “Select Installation Option:” prompt to load the distribution file into the UCI.
7)  Enter IFCP5_1.KID at the “Enter a Host File:” prompt.
8)  Enter YES at the “Want to Continue with Load?” prompt.

# 9)  Enter YES at the “Want to RUN the Environment Check Routine?” prompt. The environment check routine now runs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10) Enter VERIFY at the “Select Installation Option:” prompt to verify that the transport global has successfully been transmitted.
11) Enter IFCAP 5.1 at the “Select INSTALL NAME:” prompt.
12) Enter where you want the verify report to print at the “DEVICE:” prompt.
13) Enter INSTALL at the “Select Installation Option:” prompt.
14) Enter IFCAP 5.1 at the “Select INSTALL NAME:” prompt. The environment check routine is run again, and a long list of the incoming files displays.
15) Enter YES to the “Want KIDS to Rebuild Menu Trees Upon Completion of Install?” prompt. It is highly recommended that the menu trees be built immediately upon completion of installation because users will not be able to jump properly until they are rebuilt.
16) Enter NO to the “Want KIDS to INHIBIT LOGONs during the install?” prompt.
17) Enter YES to the “Want to DISABLE Scheduled Options, Menu Options, and Protocols?” prompt.
18) At the “Enter options you wish to mark as 'Out Of Order':” prompt, enter the following options:

> FBAA BATCH MENU

> FBAA PHARMACY BATCH OPTIONS

> FBCH BATCH OPTIONS

> FBCNH BATCH MAIN MENU

> PRCF MASTER

> PRCH CARD COORDINATOR MENU

> PRCH DELIVERY ORDER MENU

> PRCH PURCHASE CARD MENU

> PRCHUSER COORDINATOR

> PRCHUSER MASTER

> PRCP MAIN MENU

> PRCP2 MAIN MENU

> PRCPW MAIN MENU

> PRCSCP CLERK

> PRCSCP OFFICIAL

> PRCSREQUESTOR

> RMPR PURCHASING MENU

19) Press \<Enter\> at the “Enter options you wish to mark as 'Out Of Order':” prompt to end your entry of options.
20) Press \<Enter\>at the “Enter protocols you wish to mark as 'Out Of Order':” prompt.
21) Press \<Enter\>at the “Delay Install (Minutes): (0-60):” prompt unless you wish to delay the install time, in which case you should enter the number of minutes the install should be delayed.
22) Enter the device on which you want the installation message to appear at the “DEVICE:” prompt. At this point, the installation begins and continues through the post-init routine.

The installation usually takes under 30 minutes, but may take longer depending on the number of menu trees to be rebuilt.

# REMINDER for MSM sites: Copy the IFCAP routines, including the compiled template routines, to <u>ALL</u> accounts.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### ### Sample Session of IFCAP V. 5.1 Installation  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(User inputs are marked in bold)

# \>D ^XUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INSTALL

ation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: LOAD a Distribution

Enter a Host File: IFCP5_1.KID

KIDS Distribution saved on Jun 27, 2000@22:21:12

Comment: IFCAP 5.1 generated 27 June 2000

This Distribution contains Transport Globals for the following Package(s):

IFCAP 5.1

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

Build IFCAP 5.1 has an Enviromental Check Routine

Want to RUN the Environment Check Routine? YES// YES

IFCAP 5.1

Will first run the Environment Check Routine, PRC51ENV

Use INSTALL NAME: IFCAP 5.1 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: VERIFY Checksums in Transport Global

Select INSTALL NAME: IFCAP 5.1

=\> IFCAP 5.1 generated 27 June 2000 ;Created on Jun 27, 2000

This Distribution was loaded on Jun 29, 2000@08:16:20 with header of

IFCAP 5.1 generated 27 June 2000 ;Created on Jun 27, 2000@22:21:12

It consisted of the following Install(s):

IFCAP 5.1

DEVICE: HOME// \<ENTER\>

PACKAGE: IFCAP 5.1 Jun 29, 2000 8:17 am PAGE 1

-------------------------------------------------------------------------------

1042 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: INSTALL Package(s)

Select INSTALL NAME: IFCAP 5.1 Loaded from Distribution 6/29/00@08:16:20

=\> IFCAP 5.1 generated 27 June 2000 ;Created on Jun 27, 2

This Distribution was loaded on Jun 29, 2000@08:16:20 with header of

IFCAP 5.1 generated 27 June 2000 ;Created on Jun 27, 2000@22:

21:12

It consisted of the following Install(s):

IFCAP 5.1

Checking Install for Package IFCAP 5.1

Will first run the Environment Check Routine, PRC51ENV

Install Questions for IFCAP 5.1

Incoming Files:

410 CONTROL POINT ACTIVITY

> **NOTE:** You already have the 'CONTROL POINT ACTIVITY' File.

410.1 TRANSACTION NUMBER

> **NOTE:** You already have the 'TRANSACTION NUMBER' File.

410.2 CLASSIFICATION OF REQUEST

> **NOTE:** You already have the 'CLASSIFICATION OF REQUEST' File.

410.3 REPETITIVE ITEM LIST

> **NOTE:** You already have the 'REPETITIVE ITEM LIST' File.

410.4 SUB-CONTROL POINT

> **NOTE:** You already have the 'SUB-CONTROL POINT' File.

410.5 CPA FORM TYPE

> **NOTE:** You already have the 'CPA FORM TYPE' File.

410.6 DELIVERY SCHEDULE

> **NOTE:** You already have the 'DELIVERY SCHEDULE' File.

410.7 SORT GROUP

> **NOTE:** You already have the 'SORT GROUP' File.

410.8 DELIVERY POINT

> **NOTE:** You already have the 'DELIVERY POINT' File.

411 ADMIN. ACTIVITY SITE PARAMETER

> **NOTE:** You already have the 'ADMIN. ACTIVITY SITE PARAMETER' File.

411.2 FACILITY TYPE (TEMPORARY)

> **NOTE:** You already have the 'FACILITY TYPE (TEMPORARY)' File.

411.3 IFCAP CONVERSION DISCREPANCY

> **NOTE:** You already have the 'IFCAP CONVERSION DISCREPANCY' File.

411.4 IFCAP CONVERSION ERROR

> **NOTE:** You already have the 'IFCAP CONVERSION ERROR' File.

411.5 IFCAP PARAMETERS

> **NOTE:** You already have the 'IFCAP PARAMETERS' File.

417 FMS TRANSACTIONS

> **NOTE:** You already have the 'FMS TRANSACTIONS' File.

417.1 FMS EXCEPTIONS

> **NOTE:** You already have the 'FMS EXCEPTIONS' File.

420 FUND CONTROL POINT

> **NOTE:** You already have the 'FUND CONTROL POINT' File.

420.1 COST CENTER

> **NOTE:** You already have the 'COST CENTER' File.

420.13 PRCD SD PROGRAM

> **NOTE:** You already have the 'PRCD SD PROGRAM' File.

420.131 PRCD SD FCP/PRJ

> **NOTE:** You already have the 'PRCD SD FCP/PRJ' File.

420.132 PRCD SD OBJECT CLASS

> **NOTE:** You already have the 'PRCD SD OBJECT CLASS' File.

420.133 PRCD SD JOB

> **NOTE:** You already have the 'PRCD SD JOB' File.

420.134 PRCD SD REPORTING CATEGORY

> **NOTE:** You already have the 'PRCD SD REPORTING CATEGORY' File.

420.135 PRCD SD REVENUE SOURCE

> **NOTE:** You already have the 'PRCD SD REVENUE SOURCE' File.

420.136 PRCD SD SUB-REV SOURCE

> **NOTE:** You already have the 'PRCD SD SUB-REV SOURCE' File.

420.137 PRCD SD SUB-OBJ

> **NOTE:** You already have the 'PRCD SD SUB-OBJ' File.

420.138 PRCD SD FMS SECURITY

> **NOTE:** You already have the 'PRCD SD FMS SECURITY' File.

420.14 PRCD FUND

> **NOTE:** You already have the 'PRCD FUND' File.

420.141 PRCD FMS SUB-ALLOWANCE ACCOUNT

> **NOTE:** You already have the 'PRCD FMS SUB-ALLOWANCE ACCOUNT' File.

420.15 PRCD SD ADMINISTRATIVE OFFICE

> **NOTE:** You already have the 'PRCD SD ADMINISTRATIVE OFFICE' File.

420.16 PRCD SD DOCUMENT TYPE

> **NOTE:** You already have the 'PRCD SD DOCUMENT TYPE' File.

420.17 PRCD SD DOCUMENT DATA ELEMENT

> **NOTE:** You already have the 'PRCD SD DOCUMENT DATA ELEMENT' File.

420.18 PRCD REQUIRED FIELDS

> **NOTE:** You already have the 'PRCD REQUIRED FIELDS' File.

420.19 PRCD STANDARD DICTIONARY

> **NOTE:** You already have the 'PRCD STANDARD DICTIONARY' File.

420.1999 PRCD SD STATUS

> **NOTE:** You already have the 'PRCD SD STATUS' File.

420.2 BUDGET OBJECT CODE

> **NOTE:** You already have the 'BUDGET OBJECT CODE' File.

420.3 PRCD FUND/APPROPRIATION CODE

> **NOTE:** You already have the 'PRCD FUND/APPROPRIATION CODE' File.

420.4 CALM/LOG TRANSACTIONS CODE LIST

> **NOTE:** You already have the 'CALM/LOG TRANSACTIONS CODE LIST' File.

420.5 UNIT OF ISSUE

> **NOTE:** You already have the 'UNIT OF ISSUE' File.

420.6 CODE INDEX

> **NOTE:** You already have the 'CODE INDEX' File.

420.7 BUDGET DISTRIBUTION CODES

> **NOTE:** You already have the 'BUDGET DISTRIBUTION CODES' File.

420.8 SOURCE CODE

> **NOTE:** You already have the 'SOURCE CODE' File.

420.9 INTERMEDIATE PRODUCT

> **NOTE:** You already have the 'INTERMEDIATE PRODUCT' File.

420.92 PRCU IFCAP/FMS CONVERSION

> **NOTE:** You already have the 'PRCU IFCAP/FMS CONVERSION' File.

420.96 IFCAP/FMS OBLIGATION RECONCILIATION REPORT

> **NOTE:** You already have the 'IFCAP/FMS OBLIGATION RECONCILIATION REPORT' File.

420.97 IFCAP/FMS FCP RECONCILIATION MESSAGE

> **NOTE:** You already have the 'IFCAP/FMS FCP RECONCILIATION MESSAGE' File.

420.98 IFCAP/FMS FCP RECONCILIATION REPORT

> **NOTE:** You already have the 'IFCAP/FMS FCP RECONCILIATION REPORT' File.

420.99 IFCAP TEMP FCP SNAPSHOT

> **NOTE:** You already have the 'IFCAP TEMP FCP SNAPSHOT' File.

420.9999 PRCD SD STANDARD FOR COPYING

> **NOTE:** You already have the 'PRCD SD STANDARD FOR COPYING' File.

421 FUND DISTRIBUTION

> **NOTE:** You already have the 'FUND DISTRIBUTION' File.

421.1 MULTIPLE DISTRIBUTION

> **NOTE:** You already have the 'MULTIPLE DISTRIBUTION' File.

421.2 CALM/LOG TRANSMISSION RECORD

> **NOTE:** You already have the 'CALM/LOG TRANSMISSION RECORD' File.

421.3 CALM ERROR MESSAGES

> **NOTE:** You already have the 'CALM ERROR MESSAGES' File.

421.4 FISCAL LOCK

> **NOTE:** You already have the 'FISCAL LOCK' File.

421.5 INVOICE TRACKING

> **NOTE:** You already have the 'INVOICE TRACKING' File.

421.6 FUND DISTRIBUTION (TEMP TRANS)

> **NOTE:** You already have the 'FUND DISTRIBUTION (TEMP TRANS)' File.

421.7 INVOICE DLN COUNTER

> **NOTE:** You already have the 'INVOICE DLN COUNTER' File.

421.8 FISCAL STACKED DOCUMENTS

> **NOTE:** You already have the 'FISCAL STACKED DOCUMENTS' File.

421.9 INVOICE PARTIAL COUNTER

> **NOTE:** You already have the 'INVOICE PARTIAL COUNTER' File.

422 CALM/LOG TEMPLATE MAPS

> **NOTE:** You already have the 'CALM/LOG TEMPLATE MAPS' File.

422.2 COUNTER

> **NOTE:** You already have the 'COUNTER' File.

423 CALM/LOG CODE SHEET

> **NOTE:** You already have the 'CALM/LOG CODE SHEET' File.

423.4 ISMS REASON CODES

> **NOTE:** You already have the 'ISMS REASON CODES' File.

423.5 PRC IFCAP MESSAGE ROUTER

> **NOTE:** You already have the 'PRC IFCAP MESSAGE ROUTER' File.

423.6 ISMS/FMS TRANS

> **NOTE:** You already have the 'ISMS/FMS TRANS' File.

423.9 CALM/LOG BATCH TYPE

> **NOTE:** You already have the 'CALM/LOG BATCH TYPE' File.

424 1358 DAILY RECORD

> **NOTE:** You already have the '1358 DAILY RECORD' File.

424.1 1358 AUTHORIZATION DETAIL

> **NOTE:** You already have the '1358 AUTHORIZATION DETAIL' File.

440 VENDOR

> **NOTE:** You already have the 'VENDOR' File.

440.2 DIRECT DELIVERY PATIENTS

> **NOTE:** You already have the 'DIRECT DELIVERY PATIENTS' File.

440.3 VENDOR EDIT

> **NOTE:** You already have the 'VENDOR EDIT' File.

440.5 PURCHASE CARD INFORMATION

> **NOTE:** You already have the 'PURCHASE CARD INFORMATION' File.

440.6 PURCHASE CARD ORDER RECONCILE

> **NOTE:** You already have the 'PURCHASE CARD ORDER RECONCILE' File.

440.7 MONTHLY ACCRUAL

> **NOTE:** You already have the 'MONTHLY ACCRUAL' File.

440.8 PRCH AFC CHARGE TRANSMISSION LOG

> **NOTE:** You already have the 'PRCH AFC CHARGE TRANSMISSION LOG' File.

441 ITEM MASTER

> **NOTE:** You already have the 'ITEM MASTER' File.

441.2 FEDERAL SUPPLY CLASSIFICATION

> **NOTE:** You already have the 'FEDERAL SUPPLY CLASSIFICATION' File.

441.3 FSC GROUP TITLES

> **NOTE:** You already have the 'FSC GROUP TITLES' File.

441.4 DLA/LOG CODES

> **NOTE:** You already have the 'DLA/LOG CODES' File.

441.6 TYPE OF REQUISITION AMENDMENT

> **NOTE:** You already have the 'TYPE OF REQUISITION AMENDMENT' File.

441.7 AMENDMENTS TO DELIVERY SCHEDULES

> **NOTE:** You already have the 'AMENDMENTS TO DELIVERY SCHEDULES' File.

442 PROCUREMENT & ACCOUNTING TRANSACTIONS

> **NOTE:** You already have the 'PROCUREMENT & ACCOUNTING TRANSACTIONS' File.

442.2 TYPE OF AMENDMENT

> **NOTE:** You already have the 'TYPE OF AMENDMENT' File.

442.3 PURCHASE ORDER STATUS

> **NOTE:** You already have the 'PURCHASE ORDER STATUS' File.

442.4 PURCHASE AUTHORITY

> **NOTE:** You already have the 'PURCHASE AUTHORITY' File.

442.5 PAT TYPE

> **NOTE:** You already have the 'PAT TYPE' File.

442.6 PAT NUMBER

> **NOTE:** You already have the 'PAT NUMBER' File.

442.7 ADMINISTRATIVE CERTIFICATIONS

> **NOTE:** You already have the 'ADMINISTRATIVE CERTIFICATIONS' File.

442.8 DELIVERY SCHEDULE (ORDER)

> **NOTE:** You already have the 'DELIVERY SCHEDULE (ORDER)' File.

442.9 ELEC RECEIVING REPORT BATCH

> **NOTE:** You already have the 'ELEC RECEIVING REPORT BATCH' File.

443 REQUEST WORKSHEET

> **NOTE:** You already have the 'REQUEST WORKSHEET' File.

443.1 IFCAP PURGEMASTER WORKLIST

> **NOTE:** You already have the 'IFCAP PURGEMASTER WORKLIST' File.

443.2 IFCAP PURGE PARAMETERS

> **NOTE:** You already have the 'IFCAP PURGE PARAMETERS' File.

443.3 IFCAP PURGE INPROCESS

> **NOTE:** You already have the 'IFCAP PURGE INPROCESS' File.

443.4 TYPE OF SPECIAL HANDLING

> **NOTE:** You already have the 'TYPE OF SPECIAL HANDLING' File.

443.5 P.O./REQUEST/R.R. PRINT LOG

> **NOTE:** You already have the 'P.O./REQUEST/R.R. PRINT LOG' File.

443.6 AMENDMENTS

> **NOTE:** You already have the 'AMENDMENTS' File.

443.75 EDI SENDER

> **NOTE:** You already have the 'EDI SENDER' File.

443.76 EDI ERROR CODES

> **NOTE:** You already have the 'EDI ERROR CODES' File.

443.8 LOCAL PROCUREMENT REASON CODES

> **NOTE:** You already have the 'LOCAL PROCUREMENT REASON CODES' File.

443.9 IFCAP PENDING ARCHIVE

> **NOTE:** You already have the 'IFCAP PENDING ARCHIVE' File.

444 REQUEST FOR QUOTATION

> **NOTE:** You already have the 'REQUEST FOR QUOTATION' File.

444.1 RFQ VENDOR

> **NOTE:** You already have the 'RFQ VENDOR' File.

444.2 SIC CODE

> **NOTE:** You already have the 'SIC CODE' File.

444.21 SIC CODE GROUPS

> **NOTE:** You already have the 'SIC CODE GROUPS' File.

444.3 RFQ COUNTER

> **NOTE:** You already have the 'RFQ COUNTER' File.

444.4 RFQ EDITING PREFERENCE

> **NOTE:** You already have the 'RFQ EDITING PREFERENCE' File.

445 GENERIC INVENTORY

> **NOTE:** You already have the 'GENERIC INVENTORY' File.

445.1 INVENTORY BALANCES

> **NOTE:** You already have the 'INVENTORY BALANCES' File.

445.2 INVENTORY TRANSACTION

> **NOTE:** You already have the 'INVENTORY TRANSACTION' File.

445.3 INTERNAL DISTRIBUTION ORDER/ADJ.

> **NOTE:** You already have the 'INTERNAL DISTRIBUTION ORDER/ADJ.' File.

445.4 STORAGE LOCATION

> **NOTE:** You already have the 'STORAGE LOCATION' File.

445.6 GROUP CATEGORY

> **NOTE:** You already have the 'GROUP CATEGORY' File.

445.7 CASE CARTS

> **NOTE:** You already have the 'CASE CARTS' File.

445.8 INSTRUMENT KITS

> **NOTE:** You already have the 'INSTRUMENT KITS' File.

446 DISTRIBUTION/USAGE HISTORY

> **NOTE:** You already have the 'DISTRIBUTION/USAGE HISTORY' File.

446.1 INVENTORY DISTRIBUTED PATIENT SUPPLIES

> **NOTE:** You already have the 'INVENTORY DISTRIBUTED PATIENT SUPPLIES' File.

446.4 BARCODE PROGRAM

> **NOTE:** You already have the 'BARCODE PROGRAM' File.

446.5 CUSTOM LABEL

> **NOTE:** You already have the 'CUSTOM LABEL' File.

446.6 SPECIALTY COMMANDS

> **NOTE:** You already have the 'SPECIALTY COMMANDS' File.

447 INVENTORY LOCK MANAGEMENT

> **NOTE:** You already have the 'INVENTORY LOCK MANAGEMENT' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// YES

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

Enter options you wish to mark as 'Out Of Order': FBAA BATCH MENU Batch Ma

in Menu

Enter options you wish to mark as 'Out Of Order': FBAA PHARMACY BATCH OPTIONS

Batch Menu - Pharmacy

Enter options you wish to mark as 'Out Of Order': FBCH BATCH OPTIONS Batch

Main Menu - CH

Enter options you wish to mark as 'Out Of Order': FBCNH BATCH MAIN MENU Ba

tch Main Menu - CNH

Enter options you wish to mark as 'Out Of Order': PRCF MASTER Funds Distri

bution & Accounting Menu

Enter options you wish to mark as 'Out Of Order': PRCH CARD COORDINATOR MENU

Purchase Card Coordinator's Menu

Enter options you wish to mark as 'Out Of Order': PRCH DELIVERY ORDER MENU

Delivery Orders Menu

Enter options you wish to mark as 'Out Of Order': PRCH PURCHASE CARD MENU

Purchase Card Menu

Enter options you wish to mark as 'Out Of Order': PRCHUSER COORDINATOR IFC

AP Application Coordinator Menu

Enter options you wish to mark as 'Out Of Order': PRCHUSER MASTER Combined

A&MM Menus

Enter options you wish to mark as 'Out Of Order': PRCP MAIN MENU Primary I

nventory Point Main Menu

Enter options you wish to mark as 'Out Of Order': PRCP2 MAIN MENU Secondar

y Inventory Point Main Menu

Enter options you wish to mark as 'Out Of Order': PRCPW MAIN MENU Warehous

e--General Inventory/Distribution Menu

Enter options you wish to mark as 'Out Of Order': PRCSCP CLERK Control Poi

nt Clerk's Menu

Enter options you wish to mark as 'Out Of Order': PRCSCP OFFICIAL Control

Point Official's Menu

Enter options you wish to mark as 'Out Of Order': PRCSREQUESTOR Requestor'

s Menu

Enter options you wish to mark as 'Out Of Order': RMPR PURCHASING MENU Pur

chasing

Enter options you wish to mark as 'Out Of Order': \<Enter\>

Enter protocols you wish to mark as 'Out Of Order': \<Enter\>

Delay Install (Minutes): (0-60): 0// \<Enter\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for IFCAP 5.1 :

Jun 29, 2000@08:22:46

Build Distribution Date: Jun 27, 2000

Installing Routines:

Jun 29, 2000@08:23:29

Installing Data Dictionaries: .....

Jun 29, 2000@08:24:14

Installing PACKAGE COMPONENTS:

Installing HELP FRAME

Installing BULLETIN

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing FORM

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Option PRCHPM 2237 DEL in Menu PRCHPM UTILITIES \*\*NOT FOUND\*\*

Jun 29, 2000@08:25:52

Running Post-Install Routine: ^PRC51PST

Updating Routine file...

The following Routines were created during this install:

PRCST4

PRCST41

PRCST42

PRCST43

PRCST44

PRCST45

PRCST46

PRCST47

PRCST1

PRCST11

PRCST110

PRCST111

PRCST112

PRCST113

PRCST114

PRCST115

PRCST116

PRCST12

PRCST13

PRCST14

PRCST15

PRCST16

PRCST17

PRCST18

PRCST19

PRCST2

PRCST21

PRCST210

PRCST211

PRCST212

PRCST22

PRCST23

PRCST24

PRCST25

PRCST26

PRCST27

PRCST28

PRCST29

PRCHT2

PRCHT21

PRCHT22

PRCHT23

PRCHT24

PRCST5

PRCST6

PRCST7

PRCBTPT

PRCBTCP

PRCET

PRCSHP

PRCSHH

PRCHIH1

PRCHI1

Updating KIDS files...

IFCAP 5.1 Installed.

Jun 29, 2000@08:26:10

Install Message sent \#8884

Call MENU rebuild

Starting Menu Rebuild: Jun 29, 2000@08:26:14

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

XMUSER MailMan Menu 256 12/20/99 06/28/00

EVE Systems Manager Menu 25 06/29/00 06/28/00

*…(Your site’s primary menus will be listed here)*

Building the Common Options (XUCOMMAND)....

Building secondary menu trees....

Menu Rebuild Complete: Jun 29, 2000@08:31:35

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

## Re-starting the IFCAP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special considerations if the IFCAP installation needs to be re-started. Use the “Restart Install of Package(s)” option in KIDS.

> **WARNING:** Do not attempt to operate any part of IFCAP until you have successfully completed all parts of the installation.

# Chapter 5  Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Assignment of Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-init routine searches every IFCAP mail group to see if the group is defined on your system. If so, no action is taken. If it is not defined, the post-init adds it to your system. A list of the mail groups added appears on the Install File Print report.

If there were mail groups added, please work with your IFCAP Application Coordinator to assign appropriate users to the new mail groups. You can refer to both the Technical and Application Coordinator Manuals for details about these assignments.

(This page intentionally left blank.)