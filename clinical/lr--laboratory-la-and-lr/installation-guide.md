---
title: Laboratory Version 5.2  Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: 
patch_ver: 5.2
patch_id: 
group_key: "LR::5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - laboratory
  - filed
  - nothing
  - installation
  - time
  - deleted
  - does
  - removed
  - exist
  - your
page_count: 0
word_count: 8790
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lab5_2ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lab5_2ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

Decentralized Hospital Computer Program

LABORATORYINSTALLATION GUIDE

October 1994

Information Systems Center

Dallas, Texas

Preface

The Laboratory Installation Guide Version 5.2 is designed to provide the Department of Veterans Affairs Medical Center (VAMC), Information Resource Management Service (IRM), and the Laboratory Information Manager (LIM) with the necessary technical information required to install and implement Laboratory V. 5.2 software package.

This Installation Guide contain instructions for establishing a Laboratory First Time Installation environment, Laboratory V. 5.2 installation process, post-installation instructions, and a troubleshooting section.

Instructions for setting package parameters, making site specific changes, and other post-installation setup tasks are provided in the Laboratory Technical Manual and the Planning and Implementation Guide V. 5.2.

Table of Contents

Introduction

Installation Requirements

Pre-Installation Instructions

Laboratory First Time Installation

Begin First Time Installation Steps

Post-Installation Instructions Laboratory First Time

Post-Installation Instructions First Time - Laboratory Information Manager (LIM)

Laboratory Version 5.2 Upgrade

Begin Laboratory Version 5.2 Upgrade Installation Steps

Post-Installation Instructions

All Sites:

VAX Sites:

486 Sites Only:

Laboratory Information Manager (LIM):

Troubleshooting

Reprint Exception Report For LR52\* Routines

Restart Exception Report

Analysis of Task \#18662

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [# Installation Requirements](#installation-requirements)
- [Pre-Installation Instructions](#pre-installation-instructions)
- [Laboratory First Time Installation](#laboratory-first-time-installation)
  - [Begin First Time Installation Steps](#begin-first-time-installation-steps)
  - [## Post-Installation Instructions Laboratory First Time](#post-installation-instructions-laboratory-first-time)
  - [Post-Installation Instructions First Time - Laboratory Information Manager (LIM)](#post-installation-instructions-first-time-laboratory-information-manager-lim)
- [Laboratory Version 5.2 Upgrade](#laboratory-version-52-upgrade)
  - [Begin Laboratory Version 5.2 Upgrade Installation Steps](#begin-laboratory-version-52-upgrade-installation-steps)
  - [The pre-INIT routines (LRIPRE\) will allow the user to (optionally) print a list of the CAP codes from the LABORATORY TEST file (#60). The CAP code entries will be deleted from the LABORATORY TEST file (#60), and from the AMIS/CAP file (#64). File \#64 will be renamed WKLD CODE file (#64) and a new definition of the file attributes will be created by the LRINIT process.](#the-pre-init-routines-lripre-will-allow-the-user-to-optionally-print-a-list-of-the-cap-codes-from-the-laboratory-test-file-60-the-cap-code-entries-will-be-deleted-from-the-laboratory-test-file-60-and-from-the-amiscap-file-64-file-64-will-be-renamed-wkld-code-file-64-and-a-new-definition-of-the-file-attributes-will-be-created-by-the-lrinit-process)
  - [# Post-Installation Instructions](#post-installation-instructions)
  - [All Sites:](#all-sites)
  - [VAX Sites:](#vax-sites)
  - [Sites Only:](#sites-only)
  - [Laboratory Information Manager (LIM):](#laboratory-information-manager-lim)
- [Troubleshooting](#troubleshooting)
  - [Reprint Exception Report For LR52\ Routines](#reprint-exception-report-for-lr52-routines)
  - [Restart Exception Report](#restart-exception-report)
  - [## Analysis of Task \#18662](#analysis-of-task-18662)
The Laboratory Installation Guide Version 5.2 is designed to provide the Department of Veterans Affairs Medical Center (VAMC), Information Resources Management Service (IRM), and the Laboratory Information Manager (LIM) with the necessary technical information required to successfully install Laboratory Version 5.2 software package. This installation guide is intended for experienced users.
Laboratory First Time Installation
To install the Laboratory software for the first time on your system, you must request an additional tape/disk (LAB5_2.GLB contains the Lab globals) from your respective Information System Center (ISC).
The Laboratory First Time Installation process consists of three steps:
> Step I - LR63INIT (to populate test data names)
> Step II - LAINIT (to load Automated Instrument options)
> Step III - LRINITs (Installation Laboratory V. 5.2)
Laboratory Version 5.2 Installation
The Laboratory Version 5.2 Installation process consists of three steps:
> Step I - Pre-Database Conversion (patch LR\*5.1\*122)
> Step II - Database Conversion
> Step III - Installation Laboratory V. 5.2
> **NOTE:** Pre-Database Conversion is accomplished via patch LR\*5.1\*122.
Step I - Pre-DatabaseConversion (Patch LR\*5.1\*122)
Step I is done via the patch LR\*5.1\*122. This patch is designed to indicate any potential problems during the actual database conversion. It will also provide an estimate of time required to convert the database. This will assist the site in estimating the downtime required for V. 5.2 conversion and installation.
Step II - DatabaseConversion
Step II includes the LR52CNV\* conversion routine set. This routine set must be run immediately prior to Step III. No users should remain on the system during Step II and III.
Step III - Installation (package upgrade Laboratory V. 5.2)
Step III includes the LRINITs. The LRINITs should be run immediately after the COMPLETION of Step II. No users should be on the system during Steps II and III.
Primary Enhancements
There are 14 primary enhancements included in Laboratory V. 5.2 as follows:
1\. Automated collection of Workload Data for all Laboratory Modules
2\. Improved Local and National Management Reports
3\. Archive Workload Data
4\. Automated Method of Workload Data Transmission
5\. Barcode Accession Labels
6\. Conversion of Laboratory data from USER, PROVIDER, and PERSON files pointers to NEW PERSON file (#200) pointers
7\. Removal of Obsolete \$NEXT MUMPS Commands
> Conversion of LOCK MUMPS Commands to LOCK + and LOCK -
8\. Integrated with DMMS/DSS Development Projects
9\. Supports Laboratory Management Index Program (LMIP) reporting requirement
10\. Resolution of High Priority E3Rs, approximately 110.
11\. Automated Reporting of Clinic Stop Codes
12\. A new field called New Person Conversion (#38) under the “MI” subscript and (#.12) under the “CH” subscript has been added to the LAB DATA file (#63). This new field indicates whether a record has been converted to the NEW PERSON file (#200) pointer prior to being archived. The data in this new field will be used when archived data is brought back on-line.
13\. Autopsy reports must now be verified/released in the same manner as surgical path, cytopath, and electron microscopy.
14\. There are 15 new files created with Laboratory V. 5.2 as listed:
> • NON WKLD PROCEDURES file (#64.05) ^LAB (64.05,
> • WKLD DATA file (#64.1) ^LRO (64.1,
> • ARCHIVED WKLD DATA file (#64.19999) ^LRO (64.19999,
> • WKLD SUFFIX CODES file (#64.2) ^LAB (64.2,
> • WKLD LOG file (64.03) ^LRO(64.03,
> • WKLD CODE LAB SECT file (#64.21) ^LAB (64.21,
> • WKLD ITEM FOR COUNT file (#64.22) ^LAB (64.22,
> • WKLD INSTRUMENT MANUFACTURER file (#64.3) ^LAB (64.3,
> • ARCHIVED BLOOD INVENTORY file (#65.9999) ^LRD (65.9999,
> • BLOOD BANK VALIDATION file (#66.2) ^LAB (66.2,
> • OPERATION (MSBOS) file (#66.5) ^LAB (66.5,
> • BLOOD COMPONENT REQUEST file (#66.9) ^LAB (66.9,
> • NON PATIENT WORKLOAD file (#67.4) ^LRT (67.4,
> • ARCHIVED LAB MONTHLY WORKLOADS
> file (#67.99999) ^LRO (67.99999,
> • GROUP USER MANUAL file (#68.45) ^LAB(68.45,
> **NOTE:** A detailed explanation of the enhancements can be found in the Release Notes.

# # Installation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Files to be Overwritten: Sites which have made local modifications to verified released routines or data dictionaries may have them overwritten by this release. Six files are substantially modified in V. 5.2 release. They are LABORATORY TEST file (#60), LAB DATA file (#63), AMIS/CAP file (#64) renamed WKLD CODE file (#64), WORKLOAD file (#67.9) renamed LAB MONTHLY WORKLOADS file (#67.9), ACCESSION file (#68), and the JOURNAL file (#95) renamed LAB JOURNAL file (#95). There is potential for adverse effects even if your site used locally allocated numbering schemes. If your site has made local modifications to data dictionaries, careful review in a test account is strongly advised. Data Dictionaries and data from AMIS/CAP file (#64) and WORKLOAD file (#67.9) are completely deleted and renamed during the installation process. Locally modified data names in LAB DATA file (#63) will not be overwritten. Please refer to the Laboratory Release Notes V. 5.2 for further information on Data Dictionary changes.

> NOTE: The modifications are not limited to the six files listed above.

• Test Account: It would be very advantageous to have a functional test account (UCI) which mimics your site’s production account. If resources allow, a mirror image would be desirable. Perform the installation first in the test account. Resolve any potential problems and conduct staff training before installation into your production account.

• Software Versions Required for Laboratory V. 5.2 Installation:

> Package Versions (or Greater)

> Kernel 7.1

> FileMan 20

> MAS/PIMS 5.3

> Laboratory (if already installed) 5.1 (with patch LR\*5.1\*122 applied)

> OE/RR 2.5

• Laboratory Global Requirements: In general, the laboratory globals (^LR, ^LRO, and ^LAC) represent the globals which tend to expand in size. It is recommended that these globals be placed on a relatively empty disk. The other Lab globals are somewhat static. The size of the dynamic globals can be controlled through the purge or archive functions.

• Disk Requirements: The required size in megabytes is determined by the number of patients seen and the ordering practices of the medical center. The complexity of the medical care delivered appears to correlate well with disk requirements.

It is estimated that the base requirement of disk space would be an increase of 10-15% for complexity level four facility as categorized by the Statistical Analysis of Global Growth (SAGG) report, to a high of 20-30% for complexity level 1, over current disk space levels.

> Complexity Level Disk Growth

> 1 20-30%

> 4 10-15%

A precise prediction cannot be accurately made for any individual facility. Each facility has different data collection/management reporting requirements.

• Hardware Requirements: If you plan to use bar codes, label printers capable of printing bar codes in the format required by the clinical instrumentation used by the Laboratory Service are required. This will allow the use of the accession bar code printing provided in the Laboratory Version 5.2 software. Entries in TERMINAL TYPE file (#3.2) must have proper escape code sequences for “Bar Code On/Bar Code Off” for bar code printers in use.

Video terminals used for viewing laboratory results within and outside of the laboratory should support reverse and blink video. Laboratory Version 5.2 software provides visual alerts of critical patient data on video output. Entries in TERMINAL TYPE file (#3.2) must have proper escape code sequences for “Video On/Video Off” and “Blink On/Blink Off” for video terminals in use.

• Installation Tape/Disk: Laboratory Version 5.2 Installation consist of one tape/disk (LAB5_2 .RTN).

> Laboratory First Time Installation must request one additional tape/disk (LAB5_2.GLB) from your respective Information System Center (ISC).

> NOTE: Patch LR\*5.1\*122 should already be installed.

• File Setup that must be done during Post Installation: All of these steps must be done before Laboratory personnel can use the new version. Other users can be on the system while these actions are taken but Laboratory personnel should not be using the system.

> **NOTE:** Laboratory First Time Installation is not required to perform Step 1. Please proceed to the following steps.

> Step 1. If your site is using the Maximum Surgical Blood Order Schedule (MSBOS) for Blood Bank orders, you must run the File 81 Conversion \[LRBLPOST\] option to convert the entries in the CPT file (#81) to the new OPERATION (MSBOS) file (#66.5).

> Step 2. The following tests are exported with Laboratory V. 5.2 in LAB DATA file (#63). You must remove the “WK- “ from the test name.

> WK-AUTOLOGOUS CYTAPH NOT 1ST WK-FROZEN SECTION BLOCK RUSH

> WK-AUTOLOGOUS CYTAPHERESIS 1ST WK-FROZEN SECTION BLOCK RUSH ADD

> WK-AUTOLOGOUS PLASMAPH NOT 1ST WK-FROZEN SECTION H & E

> WK-AUTOLOGOUS PLASMAPHERESIS 1ST WK-GRID EM

> WK-AUTOLOGOUS WHOLE BLOOD 1ST WK-HOMOLOGOUS CYTAPHERESIS

> WK-AUTOLOGOUS WHOLE BLOOD NOT 1ST WK-HOMOLOGOUS PLASMAPHERESIS

> WK-AUTOPSY H & E WK-HOMOLOGOUS WB DONATION

> WK-AUTOPSY LOG-IN WK-PARAFFIN BLOCK

> WK-AUTOPSY SECTION COMPLETE WK-PARAFFIN BLOCK, ADDITIONAL CUT

> WK-AUTOPSY UNSTAINED SLIDE WK-PATIENT PHENOTYPING

> WK-BLOOD COMPONENT LOG-IN WK-PEDIATRIC UNIT PREPARATION

> WK-COMPONENT PREPARATION WK-PLASTIC SECTION

> WK-CYTOLOGY REPORTING WK-ROUTINE GROSS SURGICAL

> WK-DIRECT CYTAPHERESIS WK-SP SPECIMEN

> WK-DIRECTED CYTAPHERESIS WK-SURG PATH REPORT PREP

> WK-DIRECTED PLASMAPHERESIS WK-SURGICAL PATH REPORTING

> WK-DIRECTED WB DONATION WK-SURGICAL PATHOLOGY LOG-IN

> WK-DONOR ABO/RH RECHECK WK-TECHNICAL ASSISTANCE SURGICAL

> WK-DONOR ABO/RH TESTING WK-THERAPEUTIC CYTAPHERESIS

> WK-DONOR ALT WK-THERAPEUTIC PHLEBOTOMY

> WK-DONOR COMPONENT PREPARATION WK-THERAPEUTIC PLASMAPHERESIS

> WK-DONOR DEFERRAL WK-THICK SECTION EM

> WK-DONOR PHENOTYPING WK-UNIT ABO RECHECK

> WK-DONOR UNIT LABELING WK-UNIT INVENTORY

> WK-DONOR UNIT RELEASE WK-UNIT LOG-IN/SEND-OUT

> WK-EM EMBEDDING WK-UNIT MODIFICATION

> WK-EM LOG-IN WK-UNIT PHENOTYPING

> WK-EM PRINT/ENLARGEMENT WK-UNIT RELEASE

> WK-EM SCAN AND PHOTO WK-UNIT RELOCATION

> WK-EXTENSIVE GROSS SURGICAL WK-UNIT RH RECHECK

> WK-FROZEN SECTION ADDITIONAL CUT WK-WKLD CROSSMATCH

> WK-FROZEN SECTION BLOCK NOT RUSH

> 3\. You will need to create two new entries in the LAB LETTER file (#65.9). One for the Shipping Invoice form and another for the Inventory Worksheet form.

> 4\. The final file change can be done after the Lab package is in use. This involves using the new Administrative Category field in the BLOOD PRODUCT file (#66). For the new Blood Bank Administrative Data \[LRBLA\] option to work, this field must have the proper entries.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• VAX Sites: Increase Source Buffer and Routine Size to the maximum amount for installation. TaskMan jobs should be canceled or rescheduled until after the database conversion and the INITs have been completed. Please refer to the VAX DSM Digital Language Pocket Reference for Source Buffer Size and Symbol Table Size. If further assistance is needed refer to the VAX Help Utility.

Increase in Symbol Table and Source Buffer (routine buffer) size can be accomplished with the following command:

> \$ DSM/ENV= xxx/UCI=VAH/SYM= 100000/SOURCE= 65535

> Where xxx is the name of the local environment for the production account.

• All Sites: It is required during Step II-Database Conversion and Step III-Installation Process that all users must be removed from the system. The database conversion and installation process will progress at a more rapid rate if users are cautioned not to schedule TaskMan jobs during the process. IRM personnel should check the list of scheduled jobs and if conflicts exist, reschedule them for another time after the installation process has completed.

Step II and Step III process queue multiple TaskMan jobs. Completion time for each step will depend upon the number of entries in the LAB DATA file (#63) and the number of jobs that TaskMan must handle. Experience has shown that the Laboratory installation process runs faster when TaskMan jobs not related to Lab are at a minimum.

• Laboratory First Time Installation: Laboratory First Time Installation sites will require the LAB5_2 .RTN (LR63INIT to populate test data names - LAINIT to load Automated Instrument options) and LAB5_2.GLB (Lab global file with populated data files for the installation process). These sites must request the LAB5_2.GLB from your respective Information System Center (ISC) to implement Laboratory V. 5.2.

• Upgrade Installation to Version 5.1: To upgrade to Laboratory V. 5.1 you must obtain assistance from your respective ISC.

• Upgrade Installation to Version 5.2: Sites that have Laboratory V. 5.1 already residing on their system must install patch LR\*5.1\*122 to upgrade to Laboratory V. 5.2.

> Ensure that all Kernel, FileMan, and New Person patches have been installed.

> Providers must be entered into the NEW PERSON file (#200). The Provider Class field (#53.5) must have entries of the providers in the NEW PERSON file (#200) and the Provider security key assigned.

> All data in the AMIS/CAP file (#64) and WORKLOAD file (#67.9) will be deleted and renamed during Version 5.2 installation process. All data in the LR ROUTINE INTERGITY CHECKER file (#69.91) will be purged during this installation process. A final hardcopy printout of workload related reports should be obtained by the Laboratory Service before the LRINITs are run. A listing of CAP Codes in use in LABORATORY TEST file (#60) will be provided before data is actually purged. No listing will be provided for data stored in WORKLOAD file (#67.9).

> Identify all locally modified routines and save under the LRZ namespace. Ensure that functioning Automated Instrument routines are saved under the LAZ namespace.

> Ensure that any site-specific accession label routines are preserved. This can be done by saving the routine as LRLABEL4. The routine LRLABEL4 is not exported.

> All local Laboratory templates and routines must point to the NEW PERSON file (#200) instead of the PROVIDER file (#6), PERSON file (#16), and USER file (#3) after Laboratory V. 5.2 software is installed.

> A day or two before beginning the installation process, use the Purge old orders and accessions \[LROC\] option to remove old data from the ACCESSION file (#68) and LAB ORDER ENTRY file (#69). This will reduce the database search and conversion time. Set number of days that data is to be saved to the lowest tolerable value.

> Make a copy of all LRTASK jobs that your site has queued.

> Run the Check Files For Inconsistencies \[LRCHKFILES\] option. This option will generate a report of potential inconsistencies of data in various files. Resolution of as many inconsistencies as possible will reduce the database search and conversion time.

> The Laboratory Technical Manual provides information on External Routines, External/Internal Relations, Global Journaling, Translation, Replication, and Mapping Routines. Also, included in the Laboratory Technical manual is a listing of all External Routines and External/Internal Relations.

# Laboratory First Time Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory First Time Installation sites will require the LAB5_2.RTN tape/disk containing the LR\* and LA\* routines.

Laboratory First Time Installation sites must request one additional LAB5_2.GLB tape/disk from your respective Information System Center (ISC) containing the Lab globals to implement Laboratory V. 5.2.

The two tapes/disks required for Laboratory First Time Installation process contain the following:

> Tape/Disk Routines/Globals

> LAB5_2.RTN LR52\* conversion routines

> LR\* routines

> LA\* routines (Lab Automated Instruments, for first time sites only)

> LRINIT (Laboratory Service)

> LR63INIT (“CH” Subscript Data Names, for first time sites only)

> Tape/Disk Requested from ISC

> LAB5_2.GLB First Time Installation Globals

> ^LAB(

> ^LRO(

## Begin First Time Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*WARNING: The First Time Installation process must be implemented in the following sequence.

Step 1. Remove ALL users from the system. When you remove the users from the system - DO NOT use the disable Kernel log-on option. This also stops Taskman - which must remain running and functional.

Step 2. Backup and Journaling.

> a\) VAX Sites :

> 1\. Perform a full system backup of your DHCP system.

> 2\. Ensure that you have adjusted Source Buffer and Symbol Table sizes.

> \$ DSM/ENV= xxx/UCI=VAH/SYM= 100000/SOURCE= 65535

> 3\. Stop journaling.

> b\) 486 Sites:

> 1\. Perform a full system backup of your DHCP system.

> 2\. Ensure that all journal spaces have been re-initialized and contain no data.

> 3\. Sign on to the Printer Server where TaskMan is running.

Step 3. Use a terminal which can provide a hard copy of the process. You should now access your system and proceed to the programmer prompt level.

> \>D ^XUP

> Setting up programmer environment

> Access Code: Enter Users Access Code

> Terminal Type set to: C-VT320

> Select OPTION NAME: \<RET\>

> SET DTIME=9999

> This will set your local partition variables. Failure to have proper local variables will cause the environmental check to abort.

Step 4. Load the LAB5_2.RTN tape/disk required for the Laboratory First Time Installation process.

Step 5. Load the LAB5_2.GLB tape/disk.

Step 6.D ^LR63INITExample 1: Installing to an account that is not a first time account.

This version (#5.2) of 'LR63INIT' was created on 20-SEP-1994

(at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

This init will over write your DATA NAMES (#63)

Are you sure this is what you want? NO// Y (YES)

I AM GOING TO SET UP THE FOLLOWING FILES:

63 LAB DATA

> **NOTE:** You already have the 'LAB DATA' File.

Screen on this Data Dictionary did not pass--DD will not be installed!

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...HMMM, HOLD ON

................................................................

..........................................................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Done

Example 2: Installing to an account that is a first time account.

This version (#5.2) of 'LR63INIT' was created on 20-SEP-1994

(at DALLAS ISC - VERIFICATION ACCOUNT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

This init will over write your DATA NAMES (#63)

Are you sure this is what you want? NO// Y (YES)

I AM GOING TO SET UP THE FOLLOWING FILES:

63 LAB DATA

> **NOTE:** You already have the 'LAB DATA' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...SORRY, JUST A MOMENT PLEASE

........................................................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Done

  
Step 7. D ^LAINITExample:

This version (#5.2) of 'LAINIT' was created on 20-SEP-1994

(at GLD,DEV ISC, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Pre-Init Environment Check Completed...

I AM GOING TO SET UP THE FOLLOWING FILES:

62.4 AUTO INSTRUMENT

> **NOTE:** This package also contains INPUT TEMPLATES

> **NOTE:** This package also contains OPTIONS

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...EXCUSE ME, HOLD ON........................................................

'LA 1103' Option Filed

'LA AP FICHE' Option Filed

'LA AUTO ACC' Option Filed

'LA AUTO LLIST' Option Filed

'LA DIR JOB' Option Filed

'LA DOWN' Option Filed

'LA ERR PRINT' Option Filed

'LA INTERFACE' Option Filed

'LA JOB' Option Filed

'LA KB DIFF' Option Filed

'LA LAB TEST' Option Filed

'LA LRLL/AC SWITCH' Option Filed

'LA MI MENU' Option Filed

'LA MI MICROSCAN L/W BUILD' Option Filed

'LA MI SPECIAL CHARCTER LOAD' Option Filed

'LA MI VERIFY AUTO' Option Filed

'LA MI VITEK L/W BUILD' Option Filed

'LA WATCH' Option Filed..

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

\>

  
Step 8.D ^LRINITExample:

This version (#5.2) of 'LRINIT' was created on 20-SEP-1994

(at GLD,DEV ISC, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Checking for required globals.

Global check complete 'OK'

I AM GOING TO SET UP THE FOLLOWING FILES:

60 LABORATORY TEST (including data)

I will OVERWRITE your data with mine.

61 TOPOGRAPHY FIELD

61.1 MORPHOLOGY FIELD

61.2 ETIOLOGY FIELD

61.3 FUNCTION FIELD

61.4 DISEASE FIELD

61.5 PROCEDURE FIELD

61.6 OCCUPATION FIELD

62 COLLECTION SAMPLE

62.05 URGENCY

62.06 ANTIMICROBIAL SUSCEPTIBILITY

62.07 EXECUTE CODE

62.1 DELTA CHECKS

62.2 LAB SECTION

62.3 LAB CONTROL NAME

62.4 AUTO INSTRUMENT

> **NOTE:** You already have the 'AUTO INSTRUMENT' File.

62.5 LAB DESCRIPTIONS

62.55 AGGLUTINATION STRENGTH

62.6 ACCESSION TEST GROUP

63 LAB DATA

> **NOTE:** You already have the 'LAB DATA' File.

63.9999 ARCHIVED LR DATA

64 WKLD CODE (including data)

I will OVERWRITE your data with mine.

64.03 WKLD LOG FILE

64.05 NON WKLD PROCEDURES (including data)

I will OVERWRITE your data with mine.

64.1 WKLD DATA

64.19999 ARCHIVED WKLD DATA

64.2 WKLD SUFFIX CODES (including data)

I will OVERWRITE your data with mine.

64.21 WKLD CODE LAB SECT (including data)

I will OVERWRITE your data with mine.

64.22 WKLD ITEM FOR COUNT (including data)

I will OVERWRITE your data with mine.

64.3 WKLD INSTRUMENT MANUFACTURER (including data)

I will OVERWRITE your data with mine.

64.5 LAB REPORTS

64.6 INTERIM REPORTS

64.7 CUMULATIVE

65 BLOOD INVENTORY

65.4 BLOOD BANK UTILITY

65.5 BLOOD DONOR

65.9 LAB LETTER (including data)

I will MERGE your data with mine.

65.9999 ARCHIVED BLOOD INVENTORY

66 BLOOD PRODUCT

66.2 BLOOD BANK VALIDATION (including data)

I will OVERWRITE your data with mine.

66.5 OPERATION (MSBOS)

66.9 BLOOD COMPONENT REQUEST

67 REFERRAL PATIENT

67.1 RESEARCH

67.2 STERILIZER

67.3 ENVIRONMENTAL

67.4 NON PATIENT WORKLOAD

67.9 LAB MONTHLY WORKLOADS

67.99999 ARCHIVED LAB MONTHLY WORKLOADS

68 ACCESSION

68.2 LOAD/WORK LIST

68.4 WORKLIST HEADINGS

69 LAB ORDER ENTRY

69.1 COLLECTION LIST

69.2 LAB SECTION PRINT

69.9 LABORATORY SITE

69.91 LR ROUTINE INTEGRITY CHECKER (including data)

I will OVERWRITE your data with mine.

95 LAB JOURNAL

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

It appears you are installing DHCP Laboratory Package for the first time.

Purging Obsolete CAP CODES from ^LAB(60)

Also checking for broken pointers to ^DD(63.04,

Purging the CAP CODE file:

......

^LAM( HAS BEEN PURGED

> **NOTE:** The comments above refer to an overlay installation, but as a safety measure, they are included with the first time installation process.

Pre Init completed -- Starting init process

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...................................

............................................................................................................................................................

............................................................................................................................................................................................................................................................

'LRMITS AP' Help Frame filed.

'LRMITS CRITERIA' Help Frame filed.

'LRMITS DEFAULTS' Help Frame filed.

'LRMITS DETAIL' Help Frame filed.

'LRMITS GENERAL' Help Frame filed.

'LRMITS LOS' Help Frame filed.

'LRMITS MERGE' Help Frame filed.

'LRMITS OPTION' Help Frame filed.

'LRMITS OTYPE' Help Frame filed.

'LRMITS PRINT' Help Frame filed.

'LRMITS REPORT TYPES' Help Frame filed.

'LRMITS SORG' Help Frame filed.

'LRMITS TIME RANGE' Help Frame filed

............................................

..............................................................................

..............................................................................

..............................................................................

.........................................

'LR ACC CONTROLS' Option Filed

'LR ACC THEN DATA' Option Filed

'LR ARCHIVE CLEAR' Option Filed

'LR ARCHIVE DATA' Option Filed

'LRAC XREF' Option Filed

> **NOTE:** This printout would continue for about eight pages listing which options were filed.

'LRX4' Option Filed

'LRX5' Option Filed

'LRXOSX' Option Filed

'LRXOSX0' Option Filed

'LRXOSX1' Option Filed

'LRXOSX2' Option Filed

..........................................................

..........................................................

..........................................................

Compiling LRBL DONOR TESTING REPORT print template of File 65.5 .................

......

'LRBLDPT' ROUTINE FILED....

Compiling LRBL DONOR TESTING SUPPLEMENT print template of File 65.5 .............

......

'LRBLDPK' ROUTINE FILED...

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Moving exported 'LR' routines into Surgery name space.

Loading LROSPLG Saving as SROSPLG

Loading LROSPLG1 Saving as SROSPLG1

Loading LROSPLG2 Saving as SROSPLG2

All routines restored

The ASK PROVIDER field (#10) in the Laboratory Site file (#69.9)

is set to Yes to comply with OERR Alert requirements

^LS(95) global is obsolete, it is replaced by ^LAB(95)

Moving LAB JOURNAL Data from ^LS(95) to ^LAB(95)

Transfer complete

The global ^LS(95) will be deleted in a later version.

Updating LR Menu Items

\>\>\> Deleting/repointing 'LAB' options in OPTION file as necessary.

LR CAP

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP ALL URG INPTS

--------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP ALL URG OPTS

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP AUDIT

------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP CODE BY CODE

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP CODE BY NAME

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP COMMENTS

---------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP MANUAL

-------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP MANUAL INPUT

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP REQUEST

--------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SECTION BY CODE

----------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SECTION BY NAME

----------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SERVICE

--------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STAT ON ACC AREA

-----------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS INPTS

------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS ON

---------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS ON ACC AREA

------------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS OPTS

-----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STD/QC/REPS

------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SUB BY SECTION

---------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SUBSECTION

-----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP TEST DICT

----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP1

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP2

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP3

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR REPRINT LABELS

-----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUPRO

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAURV

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUS

-----

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSD

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSE

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSF

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSI

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSM

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSP

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUSTATUS

----------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPE

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPE1

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPE2

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPED

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPL

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPL' REMOVED from OPTION file...

LRCAPS

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRCAPW

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRDIGORD

--------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRDOWN 1

--------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRMITRZ

-------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRMIULDF

--------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRSNOMEDIT

----------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRUAP

-----

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRUDEL

------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRULY

-----

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

Options, Edit,Print and Sort templates removal complete

Linking LA namespaced options to their appropriate LR parents...

Option LA AP FICHE is already attached to LRLIAISON.

Option LA DOWN is already attached to LR DO!.

Option LA INTERFACE is already attached to LRSUPERVISOR.

Option LA MI MENU is already attached to LRMI.

Option LA JOB is already attached to LRLIAISON.

Option LA DOWN is already attached to LA MI MENU.

Done

Removing other obsolete fields

...

Adding new Workload urgencies to file 62.05

Sending Mailman message

I see you are installing Lab for the first time.

AFTER THE INITS HAVE FINISHED YOU SHOULD RUN THE

'POST^LRSETUP' ROUTINE

This will set your data base to day 1 state (No Laboratory Data)

Removing Obsolete ^LAB('X') Global

Post Init Complete

## ## Post-Installation Instructions Laboratory First Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory First Time Sites Only:

• POST^LRSETUP Routine:

> This step should be run with first time installations only. Do not run this routine in an active production account. This sets your Laboratory files to day zero. You will see the following warning before you use this routine.

W !!,"This procedure will purge/kill all entries in the ^LR( global"

W !,"and the ^LRO( global. This should not be ran by any site already"

W !,"running the Laboratory Package. It should only be used by First"

W !,"Time Installation Sites. If you are not a First Time installation"

W !,"DO NOT RUN this routine. If you have questions, contact your "

W !,"Information Systems Center (ISC) before continuing"

• Reschedule your tasked and backup procedures. Ensure that LRTASK\* options have the correct times and output devices.

• Follow local established policy to remove the LRINI\*, LRIP\*, LAINI\*, LAIP\*, LR63I\*, and LR5\* routines.

• Load routines into LR ROUTINE INTEGRITY CHECKER file (#69.91). This step can be done a day or two after the system has become stable.

> Example:

> \> D ^XUP

> Setting up programmer environment

> Select OPTION NAME: LRMENU Laboratory DHCP Menu

> Select Laboratory DHCP Menu Option: SUPervisor menu

> Select Supervisor menu Option: LAB Liaison menu

> Select Lab liaison menu Option: LAB ROUTINE INTEGRITY MENU

> Select LAB ROUTINE INTEGRITY MENU Option: LOAD Integrity File

> Select Version \# 5.2

> ARE YOU ADDING '5.2 AS

> A NEW LR ROUTINE INTEGRITY CHECKER (THE 2ND)? Y (YES)

> LR ROUTINE INTEGRITY CHECKER Distribution Date: JUN 20 94 (JUN 20, 1994)

> DEVICE: HOME// (Enter your site’s printer name) LAN

> **NOTE:** Each Routine will be listed as it is being added to the file.

Laboratory First Time VAX Sites:

• Recommended routines for mapping are LRPARAM, LRO\*, LRU, LRUA, LRV\*, LRX, LRWU\*, LRAPD\*, LRCAPV\*, LRDPA\*, LRWL\*, LRAFUN\*, LRKILL, LRRP\*, LRMIE\*, LRMIBUG, LRMIU\*, LRUP, LRUB, and LRUBL.

• Recommended journaling of Laboratory related globals.

> ^LRO (Mandatory)

> ^LR (Mandatory)

> ^LAM (Mandatory)

> ^LRD (Mandatory)

> ^LAB (Optional)

> ^LRE (Optional)

> ^LRT (Optional)

> **NOTE:** Consult Routine Histogram (^RTHIST) Report for a more precise mapping set.

Laboratory First Time 486 Sites:

1\. Move all LR\*, LA\* (minus INITs), SROSPLG, SROSPLG1, and SROSPLG2 routines to the compute servers and any additional print servers.

2\. There are two print templates associated with BLOOD DONOR file (#65.5) which are compiled at the end of the INITs into LRBLDPT and LRBLDPK routines. Please recompile these templates on the compute (and additional print) servers.

3\. Follow your local system backup and journaling procedures.

## Post-Installation Instructions First Time - Laboratory Information Manager (LIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Remember, this is a first time installation so you must set up the Laboratory site parameters and the files before you use the Laboratory package. For Version 5.2, you must perform the following post installation setup.

> The following changes must be done so that Blood Bank and Anatomic Pathology will work. Some options will be using new fields or new files to Version 5.2 which need to be completed before the options can work properly.

> 1\. For all of the entries in the BLOOD PRODUCT file (#66) which are currently being used, the new Administrative Category field will need to be completed. By using the FileMan option to edit the entries, this can be expedited by simply looping through the entries in the BLOOD PRODUCT file (#66).

> 2\. You need to edit a new entry in the LAB LETTER file (#65.9) which will control the content of the text to appear in the output generated by the Shipping Invoices for Blood Components \[LRBLISH\] option. This was previously hard coded, but it is now determined by the entry in LAB LETTER file (#65.9) which is designated as the “Shipping Invoice”.

> 3\. You need to edit a new entry in the LAB LETTER file (#65.9) which will control the content of the text to appear at the bottom of the Inventory Testing worksheet generated by the Inventory ABO/Rh testing worksheet \[LRBLIW\] option. This was previously hard coded, but it is now determined by the entry in LAB LETTER file (#65.9) which is designated as the “Inventory Worksheet”. This will allow the text to match the key used at that specific facility.

> 5\. The following new WK tests are exported with Laboratory Version 5.2 in LABORATORY TEST file (#60). You must remove the “WK-” from the test name because the routines are hardcoded to look for the specific test names.

> WK-AUTOLOGOUS CYTAPH NOT 1ST WK-FROZEN SECTION BLOCK RUSH

> WK-AUTOLOGOUS CYTAPHERESIS 1ST WK-FROZEN SECTION BLOCK RUSH ADD

> WK-AUTOLOGOUS PLASMAPH NOT 1ST WK-FROZEN SECTION H & E

> WK-AUTOLOGOUS PLASMAPHERESIS 1ST WK-GRID EM

> WK-AUTOLOGOUS WHOLE BLOOD 1ST WK-HOMOLOGOUS CYTAPHERESIS

> WK-AUTOLOGOUS WHOLE BLOOD NOT 1ST WK-HOMOLOGOUS PLASMAPHERESIS

> WK-AUTOPSY H & E WK-HOMOLOGOUS WB DONATION

> WK-AUTOPSY LOG-IN WK-PARAFFIN BLOCK

> WK-AUTOPSY SECTION COMPLETE WK-PARAFFIN BLOCK, ADDITIONAL CUT

> WK-AUTOPSY UNSTAINED SLIDE WK-PATIENT PHENOTYPING

> WK-BLOOD COMPONENT LOG-IN WK-PEDIATRIC UNIT PREPARATION

> WK-COMPONENT PREPARATION WK-PLASTIC SECTION

> WK-CYTOLOGY REPORTING WK-ROUTINE GROSS SURGICAL

> WK-DIRECT CYTAPHERESIS WK-SP SPECIMEN

> WK-DIRECTED CYTAPHERESIS WK-SURG PATH REPORT PREP

> WK-DIRECTED PLASMAPHERESIS WK-SURGICAL PATH REPORTING

> WK-DIRECTED WB DONATION WK-SURGICAL PATHOLOGY LOG-IN

> WK-DONOR ABO/RH RECHECK WK-TECHNICAL ASSISTANCE SURGICAL

> WK-DONOR ABO/RH TESTING WK-THERAPEUTIC CYTAPHERESIS

> WK-DONOR ALT WK-THERAPEUTIC PHLEBOTOMY

> WK-DONOR COMPONENT PREPARATION WK-THERAPEUTIC PLASMAPHERESIS

> WK-DONOR DEFERRAL WK-THICK SECTION EM

> WK-DONOR PHENOTYPING WK-UNIT ABO RECHECK

> WK-DONOR UNIT LABELING WK-UNIT INVENTORY

> WK-DONOR UNIT RELEASE WK-UNIT LOG-IN/SEND-OUT

> WK-EM EMBEDDING WK-UNIT MODIFICATION

> WK-EM LOG-IN WK-UNIT PHENOTYPING

> WK-EM PRINT/ENLARGEMENT WK-UNIT RELEASE

> WK-EM SCAN AND PHOTO WK-UNIT RELOCATION

> WK-EXTENSIVE GROSS SURGICAL WK-UNIT RH RECHECK

> WK-FROZEN SECTION ADDITIONAL CUT WK-WKLD CROSSMATCH

> WK-FROZEN SECTION BLOCK NOT RUSH

> NOTE: To set up the Laboratory site parameters and files refer to the Laboratory Planning and Implementation Guide V. 5.2.

• After successfully testing, return the system to the users.

# Laboratory Version 5.2 Upgrade

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Laboratory First Time Installation sites, please refer to the First Time Installation section of this guide.

> **NOTE:** Sites that will need to upgrade to Laboratory Version 5.1 must obtain assistance from your respective ISC.

Sites that have Laboratory V. 5.1 already residing on their system must install patch LR\*5.1\*122 to upgrade to Laboratory V. 5.2.

Patch LR\*5.1\*122 is REQUIRED. You will not be allowed to proceed with the INIT process without patch LR\*5.1\*122 (pre conversion routine) having been installed.

Review facility policies for procedures concerning the restoration of a full system backup. Restoration of the DHCP database to a condition which existed prior to the beginning of the installation process may become necessary in the event of an unrecoverable error during the installation.

No users should remain on the system during installation. The Installation process includes the LR52CNV\* conversion routine set.

The LR52CNV\* conversion routine set uses the same criteria as the LR5XCNV\* routine set (patch\* 5.1 \*122) to identify all of the areas in the Laboratory database files that point to the USER file (#3), PROVIDER file (#6), and the PERSON file (#16). The LR52CNV\* routine set actually converts the data and writes the converted data to the database. If the conversion routine set finds a record that cannot be converted properly, it will reset the original pointer value in the database preceded by ERR (e.g., ERR12345), note the record on the Exception Report and continue processing. Since the LR52CNV\* conversion routine set is run only once, there is no opportunity to observe the data for the record noted on the Exception Report, or to make modifications to the record data as necessary.

There is an Exception Report for each tasked job. The Exception Report provides a hardcopy of the entries which could not be converted and ensures that each tasked job actually completed. After the installation is completed, you may choose to go back to the Exception Report and correct any data that could not be converted.

All Sites:

It is required to remove all users from the system during the installation process. However, the installation process will progress at a more rapid rate if users are cautioned not to schedule TaskMan jobs during the installation process. IRM staff should check the list of scheduled jobs and reschedule them if necessary.

The installation process queues multiple TaskMan jobs. Therefore, TaskMan must be up and running. Completion time for each step will depend upon the number of entries in the Laboratory data files and the number of jobs that TaskMan must handle.

\*WARNING: Sites which have made local modifications to verified released routines or data dictionaries may have them overwritten by this release. Six files are substantially modified in V. 5.2 release. They are LABORATORY TEST file (#60), LAB DATA file (#63), AMIS/CAP file (#64) renamed WKLD CODE file (#64), WORKLOAD file (#67.9) renamed LAB MONTHLY WORKLOADS file (#67.9), ACCESSION file (#68), and the JOURNAL file (#95) renamed LAB JOURNAL file (#95). There is potential for adverse effects even if your site used locally allocated numbering schemes. If your site has made local modifications to data dictionaries, careful review in a test account is advised. Data Dictionaries and data from Files \#64 and \#67.9 are completely deleted. Locally modified data names in LAB DATA file (#63) will not be overwritten as done in prior versions.

DD DataFile Name Number Action Action

LABORATORY TEST 60 modified workload data deleted

LAB DATA 63 modified modified

AMIS/CAP 64 deleted deleted

renamed

WKLD CODE

WORKLOAD 67.9 deleted deleted

renamed

LAB MONTHLY

WORKLOADS

ACCESSION 68 modified modified

JOURNAL 95 none none

renamed

LAB JOURNAL

## Begin Laboratory Version 5.2 Upgrade Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*WARNING: Ensure that the Cumulative ran successfully for the previous day.

Step 1. Remove ALL users from the system. When you remove the users from the system - DO NOT use the disable Kernel log-on option. This also stops Taskman - which must remain running and functional.

Step 2. Do backup and journaling.

> a\) VAX Sites :

> 1\. Perform a full system backup of your DHCP system.

> 2\. Ensure that you have adjusted Source Buffer and Symbol Table sizes.

> \$ DSM/ENV= xxx/UCI=VAH/SYM= 100000/SOURCE= 65535

> 3\. Stop journaling.

> b\) 486 Sites:

> 1\. Perform a full system backup of your DHCP system.

> 2\. Ensure that all journal spaces have been reinitialized and contain no data.

> 3\. Sign on to the Printer Server where TaskMan is running.

> **NOTE:** 486 Sites, many SETs and KILLs are executed during the conversion and INIT process. It is important to ensure that all journal space is available for use. If a problem with cross system journaling is encountered, please contact your local ISC for assistance.

Step 3.All Sites: Stop all Auto Instrument interfaces. This should be done by entering at the programmers prompt the following line of MUMPS code:

> \>S ^LA("STOP",X) =""

> Where X represents the AUTO INSTRUMENT file (#62.4) internal entry number.

> Example : LSI \#1 X=1, LSI \#2 X=11

> After several minutes have passed, check system status. If the jobs are still active, you must terminate the jobs.

Step 4. Check system status for active jobs. Stop all unnecessary jobs running on the system and reschedule all tasked jobs after the installation process (at least 12 hours after the beginning of LRINITs).

Step 5. Ensure that the printer you intend to use for reports has a new box of paper mounted. One or more reports will be printed out during the conversion process. These reports can be very lengthy.

Step 6. You should now access your system and proceed to the programmers prompt level. Use a terminal which can provide a hardcopy of the process.

At the terminal:

\>D ^XUP

> This will set your local partition variables. Failure to have proper local variables will cause the conversion process to abort. Ensure that DTIME is set to a high value (9999) to prevent timing out during the INIT process.

Step 7. Delete LR\* routines, except LRZ\* (local routines) and LRLABEL4 (local label routine).

Step 8. Check system status to ensure that TaskMan is running.

Step 9. Load the LAB5_2.RTN tape/disk that contains the LR52CNV\* conversion routines.

Step 10. D ^LR52CNVExample:\>D ^LR52CNV

I see you already have a list of CAP codes

from LABORATORY TEST file.

Would you like another? NO// Y (YES)

I will produce a list of CAP codes in your file LABORATORY TEST (#60)

Printer Name HOME// (Enter your site’s printer name)

Report Queued to \<site’s printer\>

PRINTER for EXCEPTION REPORT: (Enter your site’s printer name)

Task 18762 with the description of 'LAB Conversion File 63 (LAB DATA) global from ENTRY \# 0 to ENTRY \# 29999.'

has been scheduled to run NOV 20,1992@08:52:55.

Task \# 18763 with the description of 'LAB Conversion File 63 (LAB DATA) global from ENTRY \# 30000 to ENTRY \# 59999.'

has been scheduled to run NOV 20,1992@08:52:55.

Task \# 18764 with the description of 'LAB Conversion File 63 (LAB DATA) global from ENTRY \# 60000 to ENTRY \# 89999.'

has been scheduled to run NOV 20,1992@08:52:56.

Task \# 18765 with the description of 'LAB Conversion File 65 (BLOOD INVENTORY)'has been scheduled run NOV 20,1992@08:53:17.

Task \# 18766 with the description of 'LAB Conversion File 68 (ACCESSION) area \# 3.'has been scheduled to run NOV 20,1992@08:53:32.

Task \# 18767 with the description of 'LAB Conversion File 68 (ACCESSION) area \# 7.'has been scheduled to run NOV 20,1992@08:53:32.

Task \# 18768 with the description of 'LAB Conversion File 68 (ACCESSION) area \# 9' has been scheduled to run NOV 20,1992@08:53:33.

Task \# 18769 with the description of 'LAB Conversion of File 69 (LAB ORDER) 1990' has been scheduled to run NOV 20,1992@08:54:34.

Task \# 18770 with the description of 'LAB Conversion of File 69 (LAB ORDER) 1991' has been scheduled to run NOV 20,1992@08:54:34.

Task \# 18771 with the description of 'LAB Conversion of File 69 (LAB ORDER) 1992' has been scheduled to run NOV 20,1992@08:54:36

Task \# 18772 with the description of 'LAB Conversion File 63.9999 (ARCHIVED LR DATA)'has been scheduled to run NOV 20,1992@08:54:49.

Step 11. Verify Exception Report as you did for LR5XCNV (in Patch LR\*5.1\*122). Please see the troubleshooting section at the end of this manual for hints on how to solve problems that the Exception Report may show.

Step 12. After all of the tasked conversion have run to completion, obtain a print out of the conversion times.

> LR52TIME provides an approximation of database conversion time and is to be run after the actual conversion routines have completed. A report will be generated which contains the following information:

> a\) Which of the tasks spawned to convert LAB DATA file (#63) took the longest and how long it took to complete.

> b\) Which of all the remaining tasks (those to convert ARCHIVED LR DATA file (#63.999), BLOOD INVENTORY file (#65), ACCESSION file (#68), and LAB ORDER ENTRY file (#69)) took the longest to convert and how long it took to complete.

> c\) What was the overall time for the conversion by finding the difference between the earliest task start time and the latest task end time.

> d\) If any task should fail for any reason and be restarted significantly later than the other tasks, this will naturally skew the overall time.

Example: Approximation database conversion time.

\>D ^LR52TIME

DEVICE: HOME// (Enter your site’s printer name)

------------------------------------------------------------------------------

LAB TIMES FOR ^XTMP("LR5XTIME") NODES 06/29/94 PAGE 1

TIME DIFF

DAYS.HHMM NODE NAME STARTED STOPPED

------------------------------------------------------------------------------

0.0000 ^XTMP("LR5XTIME","LAR-63.9999",1) 06/23/94 @1533 06/23/94 @1534

0.0103 ^XTMP("LR5XTIME","LR-63",1) 01/15/93 @0812 01/15/93 @0915

0.0003 ^XTMP("LR5XTIME","LR-63",2) 01/15/93 @0812 01/15/93 @0816

0.0000 ^XTMP("LR5XTIME","LR-63",3) 01/15/93 @0816 01/15/93 @0816

0.0040 ^XTMP("LR5XTIME","LRD-65") 01/15/93 @0327 01/15/93 @0407

0.0021 ^XTMP("LR5XTIME","LRO-68",10) 01/15/93 @0327 01/15/93 @0348

0.0029 ^XTMP("LR5XTIME","LRO-68",11) 01/15/93 @0327 01/15/93 @0357

0.0035 ^XTMP("LR5XTIME","LRO-68",12) 01/15/93 @0327 01/15/93 @0403

0.0007 ^XTMP("LR5XTIME","LRO-68",15) 01/15/93 @0327 01/15/93 @0335

0.0000 ^XTMP("LR5XTIME","LRO-69",2850000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2860000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2870000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2880000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2890000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2900000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR5XTIME","LRO-69",2910000) 01/15/93 @0427 01/15/93 @0427

0.0018 ^XTMP("LR5XTIME","LRO-69",2920000) 01/15/93 @0427 01/15/93 @0446

0.0012 ^XTMP("LR5XTIME","LRO-69",2930000) 01/15/93 @0427 01/15/93 @0440

0.0000 ^XTMP("LR52TIME","LAR-63.9999",1) 06/23/94 @1533 06/23/94 @1534

0.0103 ^XTMP("LR52TIME","LR-63",1) 01/15/93 @0812 01/15/93 @0915

0.0003 ^XTMP("LR52TIME","LR-63",2) 01/15/93 @0812 01/15/93 @0816

0.0000 ^XTMP("LR52TIME","LR-63",3) 01/15/93 @0816 01/15/93 @0816

0.0040 ^XTMP("LR52TIME","LRD-65") 01/15/93 @0327 01/15/93 @0407

0.0021 ^XTMP("LR52TIME","LRO-68",10) 01/15/93 @0327 01/15/93 @0348

0.0029 ^XTMP("LR52TIME","LRO-68",11) 01/15/93 @0327 01/15/93 @0357

0.0035 ^XTMP("LR52TIME","LRO-68",12) 01/15/93 @0327 01/15/93 @0403

0.0007 ^XTMP("LR52TIME","LRO-68",15) 01/15/93 @0327 01/15/93 @0335

0.0000 ^XTMP("LR52TIME","LRO-69",2850000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2860000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2870000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2880000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2890000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2900000) 01/15/93 @0427 01/15/93 @0427

0.0000 ^XTMP("LR52TIME","LRO-69",2910000) 01/15/93 @0427 01/15/93 @0427

0.0018 ^XTMP("LR52TIME","LRO-69",2920000) 01/15/93 @0427 01/15/93 @0446

0.0012 ^XTMP("LR52TIME","LRO-69",2930000) 01/15/93 @0427 01/15/93 @0440

LR5XTIME - TOTAL TIME: 524.1207

LR5XTIME -- 'LR-63' greatest time difference:

---------------------------------------------

0.0103 ^XTMP("LR5XTIME","LR-63",1) 01/15/93 @0812 01/15/93 @0915

LR5XTIME -- 'other' greatest time difference:

---------------------------------------------

0.0040 ^XTMP("LR5XTIME","LRD-65") 01/15/93 @0327 01/15/93 @0407

LR52TIME - TOTAL TIME: 524.1207

LR52TIME -- 'LR-63' greatest time difference:

---------------------------------------------

0.0103 ^XTMP("LR52TIME","LR-63",1) 01/15/93 @0812 01/15/93 @0915

LR52TIME -- 'other' greatest time difference:

---------------------------------------------

0.0040 ^XTMP("LR52TIME","LRD-65") 01/15/93 @0327 01/15/93 @0407

\*\*\* END OF REPORT \*\*\*NOTES:

• Although this example shows the same time for both LR5XTIME and LR52TIME, your printout may show times that differ.

• When the ^LR52CNV\* conversion routine has successfully run to completion, all associated tasked jobs have run, and all the reports have completed, the New Person pointer conversion is complete. All the exception reports must be printed out before the INITs are run.

## The pre-INIT routines (LRIPRE\*) will allow the user to (optionally) print a list of the CAP codes from the LABORATORY TEST file (#60). The CAP code entries will be deleted from the LABORATORY TEST file (#60), and from the AMIS/CAP file (#64). File \#64 will be renamed WKLD CODE file (#64) and a new definition of the file attributes will be created by the LRINIT process.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 13. D ^LRINITExample:

This version (#5.2) of 'LRINIT' was created on 18-SEP-1994

(at GLD,DEV ISC, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Checking for required globals.

Global check complete 'OK'

Please ensure that the laboratory service has collected all of

workload (AMIS) data to this date. This information will be lost

after V 5.2 is installed.

Please perform Purge old Orders and Accessions Option. This will

reduce the conversion time of the install.

Make a copy of your tasked/startup Laboratory options. You will have

to re-enter the dates and times after the install.

OK to continue ? NO// Y (YES)

I AM GOING TO SET UP THE FOLLOWING FILES:

60 LABORATORY TEST (including data)

> **NOTE:** You already have the 'LABORATORY TEST' File.

I will OVERWRITE your data with mine.

61 TOPOGRAPHY FIELD

> **NOTE:** You already have the 'TOPOGRAPHY FIELD' File.

61.1 MORPHOLOGY FIELD

> **NOTE:** You already have the 'MORPHOLOGY FIELD' File.

61.2 ETIOLOGY FIELD

> **NOTE:** You already have the 'ETIOLOGY FIELD' File.

61.3 FUNCTION FIELD

> **NOTE:** You already have the 'FUNCTION FIELD' File.

61.4 DISEASE FIELD

> **NOTE:** You already have the 'DISEASE FIELD' File.

61.5 PROCEDURE FIELD

> **NOTE:** You already have the 'PROCEDURE FIELD' File.

61.6 OCCUPATION FIELD

> **NOTE:** You already have the 'OCCUPATION FIELD' File.

62 COLLECTION SAMPLE

> **NOTE:** You already have the 'COLLECTION SAMPLE' File.

62.05 URGENCY

> **NOTE:** You already have the 'URGENCY' File.

62.06 ANTIMICROBIAL SUSCEPTIBILITY

> **NOTE:** You already have the 'ANTIMICROBIAL SUSCEPTIBILITY' File.

62.07 EXECUTE CODE

> **NOTE:** You already have the 'EXECUTE CODE' File.

62.1 DELTA CHECKS

> **NOTE:** You already have the 'DELTA CHECKS' File.

62.2 LAB SECTION

> **NOTE:** You already have the 'LAB SECTION' File.

62.3 LAB CONTROL NAME

> **NOTE:** You already have the 'LAB CONTROL NAME' File.

62.4 AUTO INSTRUMENT

> **NOTE:** You already have the 'AUTO INSTRUMENT' File.

62.5 LAB DESCRIPTIONS

> **NOTE:** You already have the 'LAB DESCRIPTIONS' File.

62.55 AGGLUTINATION STRENGTH

> **NOTE:** You already have the 'AGGLUTINATION STRENGTH' File.

62.6 ACCESSION TEST GROUP

> **NOTE:** You already have the 'ACCESSION TEST GROUP' File.

63 LAB DATA

> **NOTE:** You already have the 'LAB DATA' File.

63.9999 ARCHIVED LR DATA

64 WKLD CODE (including data)

\*BUT YOU ALREADY HAVE 'AMIS/CAP' AS FILE \#64!

Shall I change the NAME of the file to WKLD CODE? NO// YES

64 WKLD CODE (including data)

> **NOTE:** You already have the 'WKLD CODE' File.

I will OVERWRITE your data with mine.

64.03 WKLD LOG FILE

64.05 NON WKLD PROCEDURES (including data)

I will OVERWRITE your data with mine.

64.1 WKLD DATA

64.19999 ARCHIVED WKLD DATA

64.2 WKLD SUFFIX CODES (including data)

I will OVERWRITE your data with mine.

64.21 WKLD CODE LAB SECT (including data)

I will OVERWRITE your data with mine.

64.22 WKLD ITEM FOR COUNT (including data)

I will OVERWRITE your data with mine.

64.3 WKLD INSTRUMENT MANUFACTURER (including data)

I will OVERWRITE your data with mine.

64.5 LAB REPORTS

> **NOTE:** You already have the 'LAB REPORTS' File.

64.6 INTERIM REPORTS

> **NOTE:** You already have the 'INTERIM REPORTS' File.

64.7 CUMULATIVE

> **NOTE:** You already have the 'CUMULATIVE' File.

65 BLOOD INVENTORY

> **NOTE:** You already have the 'BLOOD INVENTORY' File.

65.4 BLOOD BANK UTILITY

\*BUT YOU ALREADY HAVE 'BLOOD DONOR UTILITY' AS FILE \#65.4!

Shall I change the NAME of the file to BLOOD BANK UTILITY? NO// YES

65.4 BLOOD BANK UTILITY

> **NOTE:** You already have the 'BLOOD BANK UTILITY' File.

65.5 BLOOD DONOR

> **NOTE:** You already have the 'BLOOD DONOR' File.

65.9 LAB LETTER

> **NOTE:** You already have the 'LAB LETTER' File.

65.9999 ARCHIVED BLOOD INVENTORY

66 BLOOD PRODUCT

> **NOTE:** You already have the 'BLOOD PRODUCT' File.

66.2 BLOOD BANK VALIDATION (including data)

I will OVERWRITE your data with mine.

66.5 OPERATION (MSBOS)

66.9 BLOOD COMPONENT REQUEST

\*BUT YOU ALREADY HAVE 'BLOOD COMPONENT' AS FILE \#66.9!

Shall I change the NAME of the file to BLOOD COMPONENT REQUEST? NO// YES

66.9 BLOOD COMPONENT REQUEST

> **NOTE:** You already have the 'BLOOD COMPONENT REQUEST' File.

67 REFERRAL PATIENT

\*BUT YOU ALREADY HAVE 'REFERRAL' AS FILE \#67!

Shall I change the NAME of the file to REFERRAL PATIENT? NO// YES

67 REFERRAL PATIENT

> **NOTE:** You already have the 'REFERRAL PATIENT' File.

67.1 RESEARCH

> **NOTE:** You already have the 'RESEARCH' File.

67.2 STERILIZER

> **NOTE:** You already have the 'STERILIZER' File.

67.3 ENVIRONMENTAL

> **NOTE:** You already have the 'ENVIRONMENTAL' File.

67.4 NON PATIENT WORKLOAD

67.9 LAB MONTHLY WORKLOADS

\*BUT YOU ALREADY HAVE 'WORKLOAD' AS FILE \#67.9!

Shall I change the NAME of the file to LAB MONTHLY WORKLOADS? NO// YES

67.9 LAB MONTHLY WORKLOADS

> **NOTE:** You already have the 'LAB MONTHLY WORKLOADS' File.

67.99999 ARCHIVED LAB MONTHLY WORKLOADS

68 ACCESSION

> **NOTE:** You already have the 'ACCESSION' File.

68.2 LOAD/WORK LIST

> **NOTE:** You already have the 'LOAD/WORK LIST' File.

68.4 WORKLIST HEADINGS

> **NOTE:** You already have the 'WORKLIST HEADINGS' File.

69 LAB ORDER ENTRY

> **NOTE:** You already have the 'LAB ORDER ENTRY' File.

69.1 COLLECTION LIST

> **NOTE:** You already have the 'COLLECTION LIST' File.

69.2 LAB SECTION PRINT

> **NOTE:** You already have the 'LAB SECTION PRINT' File.

69.9 LABORATORY SITE

> **NOTE:** You already have the 'LABORATORY SITE' File.

69.91 LR ROUTINE INTEGRITY CHECKER (including data)

> **NOTE:** You already have the 'LR ROUTINE INTEGRITY CHECKER' File.

I will OVERWRITE your data with mine.

95 LAB JOURNAL

\*BUT YOU ALREADY HAVE 'JOURNAL' AS FILE \#95!

Shall I change the NAME of the file to LAB JOURNAL? NO// YES

95 LAB JOURNAL

> **NOTE:** You already have the 'LAB JOURNAL' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

I see you already have a list of CAP codes from LABORATORY TEST file.

Would you like another? NO// Y (YES)

I will produce a list of CAP codes in your file LABORATORY TEST (#60)

Printer Name HOME// PRINTER

Purging Obsolete CAP CODES from ^LAB(60)

Also checking for broken pointers to ^DD(63.04,

Purging the CAP CODE file:

.......

Purging ^LAM( HAS BEEN PURGED

Clearing 67.9

Done

Clearing 69.91

Done

Pre Init completed -- Starting init process

...SORRY, LET ME THINK ABOUT THAT A MOMENT

...................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................

'LRMITS AP' Help Frame filed.

'LRMITS CRITERIA' Help Frame filed.

'LRMITS DEFAULTS' Help Frame filed.

'LRMITS DETAIL' Help Frame filed.

'LRMITS GENERAL' Help Frame filed.

'LRMITS LOS' Help Frame filed.

'LRMITS MERGE' Help Frame filed.

'LRMITS OPTION' Help Frame filed.

'LRMITS OTYPE' Help Frame filed.

'LRMITS PRINT' Help Frame filed.

'LRMITS REPORT TYPES' Help Frame filed.

'LRMITS SORG' Help Frame filed.

'LRMITS TIME RANGE' Help Frame filed............................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

.........................................

'LR ACC CONTROLS' Option Filed

'LR ACC THEN DATA' Option Filed

'LR ARCHIVE CLEAR' Option Filed

'LR ARCHIVE DATA' Option Filed

'LR ARCHIVE MENU' Option Filed

'LR ARCHIVE NP CONVERSION' Option Filed

'LR ARCHIVE PURGE' Option Filed

'LR ARCHIVE READ MEDIA' Option Filed

'LR ARCHIVE RESTORE' Option Filed

'LR ARCHIVE SEARCH' Option Filed

'LR ARCHIVE WRITE MEDIA' Option Filed

'LR BARCODE FORMAT LOAD' Option Filed

'LR CAPTT' Option Filed

'LR COUNT ACC TESTS' Option Filed

> **NOTE:** This printout would continue for about eight pages listing which options were filed.

'LRWARDM' Option Filed

'LRWRKINC' Option Filed

'LRWU5' Option Filed

'LRWU6' Option Filed

'LRWU7' Option Filed

'LRX0' Option Filed

'LRX1' Option Filed

'LRX2' Option Filed

'LRX3' Option Filed

'LRX4' Option Filed

'LRX5' Option Filed

'LRXOSX' Option Filed

'LRXOSX0' Option Filed

'LRXOSX1' Option Filed

'LRXOSX2' Option Filed..........................................................

..........................................................

Compiling LRBL DONOR TESTING REPORT print template of File 65.5.................

......

'LRBLDPT' ROUTINE FILED....

Compiling LRBL DONOR TESTING SUPPLEMENT print template of File 65.5.............

......

'LRBLDPK' ROUTINE FILED...

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Moving exported 'LR' routines into Surgery name space.

Loading LROSPLG Saving as SROSPLG

Loading LROSPLG1 Saving as SROSPLG1

Loading LROSPLG2 Saving as SROSPLG2

All routines restored

Updating your AUTOMATED LAB INSTRUMENTS entry in the package

file with the correct current version number (5.2)...

The ASK PROVIDER field (#10) in the Laboratory Site file (#69.9)

is set to Yes to comply with OERR Alert requirements

^LS(95) global is obsolete, it is replaced by ^LAB(95)

Moving LAB JOURNAL Data from ^LS(95) to ^LAB(95)

Transfer complete

The global ^LS(95) will be deleted in a later version.

Updating LR Menu Items

\>\>\> Deleting/repointing 'LAB' options in OPTION file as necessary.

LR CAP

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR CAP' REMOVED from OPTION file...

LR CAP ALL URG INPTS

--------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP ALL URG OPTS

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP AUDIT

------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP CODE BY CODE

-------------------

REMOVED from 'LR CAP3' menu...

'LR CAP CODE BY CODE' REMOVED from OPTION file...

LR CAP CODE BY NAME

-------------------

REMOVED from 'LR CAP3' menu...

'LR CAP CODE BY NAME' REMOVED from OPTION file...

LR CAP COMMENTS

---------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP MANUAL

-------------

REMOVED from 'LRLIASON' menu...

'LR CAP MANUAL' REMOVED from OPTION file...

LR CAP MANUAL INPUT

-------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP REQUEST

--------------

REMOVED from 'LR CAP3' menu...

'LR CAP REQUEST' REMOVED from OPTION file...

LR CAP SECTION BY CODE

----------------------

REMOVED from 'LR CAP3' menu...

'LR CAP SECTION BY CODE' REMOVED from OPTION file...

LR CAP SECTION BY NAME

----------------------

REMOVED from 'LR CAP3' menu...

'LR CAP SECTION BY NAME' REMOVED from OPTION file...

LR CAP SERVICE

--------------

REMOVED from 'LR CAP3' menu...

'LR CAP SERVICE' REMOVED from OPTION file...

LR CAP STAT ON ACC AREA

-----------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS INPTS

------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS ON

---------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS ON ACC AREA

------------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STATS OPTS

-----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP STD/QC/REPS

------------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LR CAP SUB BY SECTION

---------------------

REMOVED from 'LR CAP3' menu...

'LR CAP SUB BY SECTION' REMOVED from OPTION file...

LR CAP SUBSECTION

-----------------

REMOVED from 'LR CAP3' menu...

'LR CAP SUBSECTION' REMOVED from OPTION file...

LR CAP TEST DICT

----------------

REMOVED from 'LR CAP3' menu...

'LR CAP TEST DICT' REMOVED from OPTION file...

LR CAP1

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR CAP1' REMOVED from OPTION file...

LR CAP2

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR CAP2' REMOVED from OPTION file...

LR CAP3

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR CAP3' REMOVED from OPTION file...

LR REPRINT LABELS

-----------------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRAUPRO

-------

REMOVED from 'LRAUP' menu...

'LRAUPRO' REMOVED from OPTION file...

LRAURV

------

REMOVED from 'LRAUP' menu...

'LRAURV' REMOVED from OPTION file...

LRAUS

-----

REMOVED from 'LRAU' menu...

'LRAUS' REMOVED from OPTION file...

LRAUSD

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSD' REMOVED from OPTION file...

LRAUSE

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSE' REMOVED from OPTION file...

LRAUSF

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSF' REMOVED from OPTION file...

LRAUSI

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSI' REMOVED from OPTION file...

LRAUSM

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSM' REMOVED from OPTION file...

LRAUSP

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRAUSP' REMOVED from OPTION file...

LRAUSTATUS

----------

REMOVED from 'LRAUP' menu...

'LRAUSTATUS' REMOVED from OPTION file...

LRCAPE

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPE' REMOVED from OPTION file...

LRCAPE1

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPE1' REMOVED from OPTION file...

LRCAPE2

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPE2' REMOVED from OPTION file...

LRCAPED

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPED' REMOVED from OPTION file...

LRCAPL

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPL' REMOVED from OPTION file...

LRCAPS

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPS' REMOVED from OPTION file...

LRCAPW

------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRCAPW' REMOVED from OPTION file...

LRDIGORD

--------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRDOWN 1

--------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRDOWN 1' REMOVED from OPTION file...

LRMITRZ

-------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRMITRZ' REMOVED from OPTION file...

LRMIULDF

--------

DOES NOT EXIST IN THE 'OPTION' FILE...NOTHING DELETED!

LRSNOMEDIT

----------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LRSNOMEDIT' REMOVED from OPTION file...

LRUAP

-----

REMOVED from 'LRSPP' menu...

REMOVED from 'LRCYP' menu...

REMOVED from 'LRAUP' menu...

REMOVED from 'LREMP' menu...

'LRUAP' REMOVED from OPTION file...

LRUDEL

------

REMOVED from 'LRCYLG' menu...

REMOVED from 'LRSPLG' menu...

REMOVED from 'LRAULG' menu...

REMOVED from 'LREMLG' menu...

'LRUDEL' REMOVED from OPTION file...

LRULY

-----

REMOVED from 'LRCYLG' menu...

REMOVED from 'LRSPLG' menu...

REMOVED from 'LRAULG' menu...

REMOVED from 'LREMLG' menu...

'LRULY' REMOVED from OPTION file...

Options - Edit,Print and Sort templates removal complete

Linking LA namespaced options to their appropriate LR parents...

Option LA AP FICHE is already attached to LRLIAISON.

Option LA DOWN is already attached to LR DO!.

Option LA INTERFACE is already attached to LRSUPERVISOR.

Option LA MI MENU is already attached to LRMI.

Option LA JOB is already attached to LRLIAISON.

Option LA DOWN is already attached to LA MI MENU.

Done

Adjusting your Accession file

......................

Updating the Modified/To From Field in the Blood Bank Module

Moving excepted location x-ref to the 2 node.

Removing other obsolete fields

Adding new Workload urgencies to file 62.05

Removing can be ordered STAT field for Accession Test Group file

Sending Mailman message

Removing Obsolete ^LAB('X') Global

Post Init Complete

You may now start to test the system in preparation of returning users to the system. Exercise ordering, accessioning, verification, and results reporting options used by your site.

## # Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## All Sites:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Restart your LSI (Auto Instrument interface(s)). Send a few test data streams from each interfaced instrument. Ensure that the data is being processed into ^LAH global and is verifiable.

• Reschedule your tasked and backup procedures. Ensure that LRTASK\* options have the correct times and output devices to match your hardcopy printout.

• Follow local established policy to remove the LRINI\*, LRIP\*, LAINI\*, LAIP\*, LR63I\*, and LR5\* routines.

• Load routines into LR ROUTINE INTEGRITY CHECKER file (#69.91). This step can be done a day or two after the system has become stable.

> Example:

> \> D ^XUP

> Setting up programmer environment

> Select OPTION NAME: LRMENU Laboratory DHCP Menu

> Select Laboratory DHCP Menu Option: SUPervisor menu

> Select Supervisor menu Option: LAB Liaison menu

> Select Lab liaison menu Option: LAB ROUTINE INTEGRITY MENU

> Select LAB ROUTINE INTEGRITY MENU Option: LOAD Integrity File

> Select Version \# 5.2

> ARE YOU ADDING '5.2 AS

> A NEW LR ROUTINE INTEGRITY CHECKER (THE 2ND)? Y (YES)

> LR ROUTINE INTEGRITY CHECKER Distribution Date: JUN 20 94 (JUN 20, 1994)

> DEVICE: HOME// (Enter your site’s printer name) LAN

> **NOTE:** Each Routine will be listed as it is being added to the file.

## VAX Sites:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Recommended routines for mapping are LRPARAM, LRO\*, LRU, LRUA, LRV\*, LRX, LRWU\*, LRAPD\*, LRCAPV\*, LRDPA\*, LRWL\*, LRAFUN\*, LRKILL, LRRP\*, LRMIE\*, LRMIBUG, LRMIU\*, LRUP, LRUB, and LRUBL.

• Recommended journaling of Laboratory related globals.

> ^LRO (Mandatory)

> ^LR (Mandatory)

> ^LAM (Mandatory)

> ^LRD (Mandatory)

> ^LAB (Optional)

> ^LRE (Optional)

> ^LRT (Optional)

> **NOTE:** Consult Routine Histogram (^RTHIST) Report for a more precise mapping set.

## Sites Only:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Move all LR\*, LA\* (minus INITs), SROSPLG, SROSPLG1, and SROSPLG2 routines to the compute servers and any additional print servers.

2\. There are two print templates associated with BLOOD DONOR file (#65.5) which are compiled at the end of the INITs into LRBLDPT and LRBLDPK routines. Please recompile these templates on the compute (and additional print) servers.

3\. Follow your local system backup and journaling procedures.

## Laboratory Information Manager (LIM):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a few changes which will have an immediate effect and need to be done. If the changes are not done, Blood Bank and Anatomic Pathology will not work. Some options will be using new fields or new files which need to be complete before the options can work properly.

The Release Notes detail the data dictionary changes and the changes in functionality. Please consult that manual for more detailed discussion about the data dictionary changes that make the following actions necessary.

1\. For all of the entries in the BLOOD PRODUCT file (#66) which are currently being used, the new Administrative Category field will need to be completed. By using the FileMan option to edit the entries, this can be expedited by simply looping through the entries in the BLOOD PRODUCT file (#66).

2\. You need to edit a new entry in the LAB LETTER file (#65.9) which will control the content of the text to appear in the output generated by the Shipping Invoices for Blood Components \[LRBLISH\] option. This was previously hard coded, but it is now determined by the entry in LAB LETTER file (#65.9) which is designated as the ”SHIPPING INVOICE”.

3\. You need to edit a new entry in the LAB LETTER file (#65.9) which will control the content of the text to appear at the bottom of the Inventory Testing worksheet generated by the Inventory ABO/Rh testing worksheet \[LRBLIW\] option. This was previously hard coded, but it is now determined by the entry in LAB LETTER file (#65.9) which is designated as the ”INVENTORY WORKSHEET”. This will allow the text to match the key used at that specific facility.

4\. If you have been using the Maximum Surgical Blood Order Schedule (MSBOS) functionality, you need to use the File 81 Conversion \[LRBLPOST\] option to convert the entries in CPT file (#81) to the new OPERATIONS (MSBOS) file (#66.5). The field in the CPT file (#81) which stores this information is scheduled for deletion in a future version of MAS. This new file in Laboratory is necessary in order to prevent the data from being overwritten each time the CPT file (#81) is released with data. Please note that the Maximum Surgical Blood Order Edit \[LRBLSMS\] option in the Blood Bank menu now points to OPERATIONS (MSBOS) file (#66.5).

5\. The following new WK tests are exported with Laboratory Version 5.2 in LABORATORY TEST file (#60). You must remove the “WK-” from the test name because the routines are hardcoded to look for the specific test names:

> WK-AUTOLOGOUS CYTAPH NOT 1ST WK-FROZEN SECTION BLOCK RUSH

> WK-AUTOLOGOUS CYTAPHERESIS 1ST WK-FROZEN SECTION BLOCK RUSH ADD

> WK-AUTOLOGOUS PLASMAPH NOT 1ST WK-FROZEN SECTION H & E

> WK-AUTOLOGOUS PLASMAPHERESIS 1ST WK-GRID EM

> WK-AUTOLOGOUS WHOLE BLOOD 1ST WK-HOMOLOGOUS CYTAPHERESIS

> WK-AUTOLOGOUS WHOLE BLOOD NOT 1ST WK-HOMOLOGOUS PLASMAPHERESIS

> WK-AUTOPSY H & E WK-HOMOLOGOUS WB DONATION

> WK-AUTOPSY LOG-IN WK-PARAFFIN BLOCK

> WK-AUTOPSY SECTION COMPLETE WK-PARAFFIN BLOCK, ADDITIONAL CUT

> WK-AUTOPSY UNSTAINED SLIDE WK-PATIENT PHENOTYPING

> WK-BLOOD COMPONENT LOG-IN WK-PEDIATRIC UNIT PREPARATION

> WK-COMPONENT PREPARATION WK-PLASTIC SECTION

> WK-CYTOLOGY REPORTING WK-ROUTINE GROSS SURGICAL

> WK-DIRECT CYTAPHERESIS WK-SP SPECIMEN

> WK-DIRECTED CYTAPHERESIS WK-SURG PATH REPORT PREP

> WK-DIRECTED PLASMAPHERESIS WK-SURGICAL PATH REPORTING

> WK-DIRECTED WB DONATION WK-SURGICAL PATHOLOGY LOG-IN

> WK-DONOR ABO/RH RECHECK WK-TECHNICAL ASSISTANCE SURGICAL

> WK-DONOR ABO/RH TESTING WK-THERAPEUTIC CYTAPHERESIS

> WK-DONOR ALT WK-THERAPEUTIC PHLEBOTOMY

> WK-DONOR COMPONENT PREPARATION WK-THERAPEUTIC PLASMAPHERESIS

> WK-DONOR DEFERRAL WK-THICK SECTION EM

> WK-DONOR PHENOTYPING WK-UNIT ABO RECHECK

> WK-DONOR UNIT LABELING WK-UNIT INVENTORY

> WK-DONOR UNIT RELEASE WK-UNIT LOG-IN/SEND-OUT

> WK-EM EMBEDDING WK-UNIT MODIFICATION

> WK-EM LOG-IN WK-UNIT PHENOTYPING

> WK-EM PRINT/ENLARGEMENT WK-UNIT RELEASE

> WK-EM SCAN AND PHOTO WK-UNIT RELOCATION

> WK-EXTENSIVE GROSS SURGICAL WK-UNIT RH RECHECK

> WK-FROZEN SECTION ADDITIONAL CUT WK-WKLD CROSSMATCH

> WK-FROZEN SECTION BLOCK NOT RUSH

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Reprint Exception Report For LR52\* Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the printer failed to produce an Exception Report(s) due to a malfunction of the printer (e.g., paper jam/tear, printer failure, etc.), the report(s) may be selectively reprinted through the use of the LR52CNVP routine. Before invoking this routine, you will need to refer to the “task spawn list” to obtain the File number, Task number, Accession Area number, or any other data as appropriate. You will be prompted for appropriate data.

Example:

\>D ^LR52CNVP

Select one of the following:

1 63

2 63.9999

3 65

4 68

5 69

FILE: 1 63

Enter the TASK \# off of the task spawn list: (0-99999999): 18662

Enter the 'from' entry \# off of the task spawn list: (0-18000000): 0

DEVICE: HOME// \<RET\> LAN

Exception report for file 63: LAB DATA.

Task \# 18662

For entries from 0 to 29999

The value (749) "Non-existent",

in field REQUESTING PERSON, could not be repointed.

This occurred in:

The CHEM, HEM, TOX, RIA, SER, etc.: subfile of "CH" entry: 7119174.92

The LABORATORY DATA FILE: entry: 606

The value (749) "Non-existent",

in field REPORT ROUTING (PROVIDER), could not be repointed.

This occurred in:

The LABORATORY DATA FILE: entry: 1044

The value (155) "Non-existent",

in field PHYSICIAN, could not be repointed.

This occurred in:

The MICROBIOLOGY: subfile of entry: 2921002.112539

The LABORATORY DATA FILE: entry: 1212

## Restart Exception Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a task listed on the “task spawn list” does not have a corresponding Exception Report generated, and a printer problem has been eliminated, the tasked job may have aborted prior to completion. You must restart the Exception Report process by doing the following:

\>D CRASH^LR52CNV

## ## Analysis of Task \#18662

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following analysis of Task \#18662 may be helpful in determining the reason why the entries on this Exception Report were unable to be converted.

> 63 = File \#

> 749 = Internal Entry Number (IEN) of the pointer value stored from File \#6/#16 which was invalid in File 200

> 606 = IEN (LRDFN) of entry in File \# 63

> REQUESTING PERSON = sub-field name under field name of File \# 63

> CHEM, HEM, TOX, RIA, SER, etc. = field name of File \# 63

> 7119174.92 = IEN of multiple entry under LRDFN

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: LAB DATA// 63 LAB DATA (11604 entries)

EDIT WHICH FIELD: ALL// 4 CHEM, HEM, TOX, RIA, SER, etc. (multiple)

EDIT WHICH CHEM, HEM, TOX, RIA, SER, etc. SUB-FIELD: ALL// REQ

1 REQUESTING LOCATION

2 REQUESTING PERSON

CHOOSE 1-2: 2

THEN EDIT CHEM, HEM, TOX, RIA, SER, etc. SUB-FIELD: \<RET\>

THEN EDIT FIELD: \<RET\>

Select LAB DATA LRDFN: 606 606 \<RET\>

Select DATE/TIME SPECIMEN TAKEN: SEP 12,1991@10:00// \<RET\>

7119174.92 2-6-1989@15:30:00

REQUESTING PERSON: 749// \<RET\>

Select DATE/TIME SPECIMEN TAKEN: \<RET\>

Select LAB DATA LRDFN: \<RET\>

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: LAB DATA// 6 PROVIDER (553 entries)

Select PROVIDER NAME: 749 UNKNOWN

ANOTHER ONE: \<RET\>

STANDARD CAPTIONED OUTPUT? YES// \<RET\> (YES)

DISPLAY COMPUTED FIELDS? NO// Y (YES)

NAME: UNKNOWN

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: PROVIDER// 16 PERSON (1438 entries)

Select PERSON NAME: 749 ??

Select PERSON NAME: \<RET\>

Select OPTION: \<RET\>

\>D ^%G

Global ^DIC(16,748:750,0)

DIC(16,748:750,0)

^DIC(16,748,0) = XXXX,G.^^^^^^^^111111811

^DIC(16,750,0) = YYYY,A.^F^2580207^E^2^3^CLINICAL PHARMACIST^25^11111

1812^2910115

Global ^DIC(6,749,0)

DIC(6,749,0)

^DIC(6,749,0) = UNKNOWN

Global ^

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PERSON// 63 LAB DATA (11604 entries)

EDIT WHICH FIELD: ALL// REPORT

1 REPORT ROUTING (LOCATION)

2 REPORT ROUTING (PROVIDER)

CHOOSE 1-2: 2

THEN EDIT FIELD: \<RET\>

Select LAB DATA LRDFN: 606 606

REPORT ROUTING (PROVIDER): 749// \<RET\>

Select LAB DATA LRDFN: \<RET\>  
Possible Actions: In both of the cases above, the problem is precipitated by the fact that at one time an IEN of 749 existed in File \#6 and File \#16. For some reason, the IEN in File \#6 still exists, although with minimal data; however, the IEN is no longer existent in File \#16. The facility may choose one of the following actions:

1\. Repair the entries in File \#6 and in File \#16 if enough data is present. In the above case, enough data does not appear in the file to reconstruct the entry.

2\. Use FileMan as shown above to edit the IEN to point to a valid entry in File \#16 (and File \#200). This could be a catch all entry such as UNKNOWN, UNKNOWN. Remember, the entry in File \#16 must be pointed to by a valid entry in File \#200 in order to convert properly.

3\. If you choose not to alter the data, in which case the Step II conversion process will transpose the data into an error condition, the value at the global location will become 749ERR. In this way, use of FileMan to examine the data entry will show the value as it existed prior to conversion.