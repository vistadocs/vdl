---
title: LR*5.2*59 Laboratory Archiving Technical and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Laboratory Archiving Technical and
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*59
group_key: "LR:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - archive
  - archived
  - wkld
  - archival
  - lrar
  - activity
  - table
  - contents
  - date
  - archiving
page_count: 0
word_count: 7198
section_count: 18
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lrar.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lrar.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

![](lr-5-2-59-laboratory-archiving-technical-and-user-guide/001.png)

REVISIONLABORATORY ENHANCED ARCHIVINGTECHNICAL RELEASE NOTESANDUSER NOTESPatch LR\*5.2\*59

October 1996

Software Service

Clinical Ancillary Product Line

Table of Contents

Introduction

Menu Change

Installation Notes

KIDS Installation Instructions

Installation Example

Routine Deletion

Post Installation Instructions

Data Dictionary Updates

New File

New Fields

New Extract Templates

Updated Data Dictionaries

Option Updates

New Options

Option Name Changes

Routines

New Routines

Modified Routine

Integration Agreement

User Notes

Menu Change

Archival Process

Lab Archival Activity

Steps to Complete Archival Activity

How to Access Archiving Options

Option Examples

Select Entries to Archive 64.1

Cancel Option

Delete Archived File Entries Option

Verify Files for Archiving

Archive Wkld Data file 64.1

Write Data to Off-line Media

Clear Archived Wkld Data file 64.19999

Read Data from Off-line Media

Purge Wkld Data file 64.1

Workload Reports from Archived Files

Lab Monthly Workloads Report

Treating Specialty Workload Report

Workload Cost Report by Major Section

Workload Statistics by Major Section

Lab Archival Activity Report

Appendix

Archiving Menu \[LRAR ARCHIVE MAIN MENU\]

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Menu Change](#menu-change)
- [Installation Notes](#installation-notes)
  - [KIDS Installation Instructions](#kids-installation-instructions)
    - [Installation Example](#installation-example)
    - [Routine Deletion](#routine-deletion)
  - [Post Installation Instructions](#post-installation-instructions)
- [Data Dictionary Updates](#data-dictionary-updates)
  - [New File](#new-file)
  - [New Fields](#new-fields)
  - [95.11,20 ENDING DATE DATE](#951120-ending-date-date)
  - [## New Extract Templates](#new-extract-templates)
  - [Updated Data Dictionaries](#updated-data-dictionaries)
- [Option Updates](#option-updates)
  - [New Options](#new-options)
  - [Option Name Changes](#option-name-changes)
- [Routines](#routines)
  - [New Routines](#new-routines)
  - [Modified Routine](#modified-routine)
  - [Integration Agreement](#integration-agreement)
- [User Notes](#user-notes)
    - [Steps to Complete Archival Activity](#steps-to-complete-archival-activity)
  - [How to Access Archiving Options](#how-to-access-archiving-options)
    - [Option Examples](#option-examples)
  - [Workload Reports from Archived Files](#workload-reports-from-archived-files)
    - [Lab Monthly Workloads Report](#lab-monthly-workloads-report)
    - [Treating Specialty Workload Report](#treating-specialty-workload-report)
    - [Workload Cost Report by Major Section](#workload-cost-report-by-major-section)
    - [Example](#example)
    - [Workload Statistics by Major Section](#workload-statistics-by-major-section)
  - [Lab Archival Activity Report](#lab-archival-activity-report)
- [Appendix](#appendix)
- [## Archiving Menu \[LRAR ARCHIVE MAIN MENU\]](#archiving-menu-lrar-archive-main-menu)
This documentation for Patch LR\*5.2\*59 is designed to provide the Department of Veterans Affairs Medical Center (VAMC), Information Resource Management Service (IRM), and the Laboratory Information Manager (LIM) with the necessary technical information required to install and implement Laboratory Enhanced Archiving. The User Notes section is a training and reference guide.
The purpose of this patch is to provide archiving, purging, and storage capabilities for the following Laboratory data files:
> WORKLOAD DATA (#64.1)
> LAB MONTHLY WORKLOADS (#67.9)

## Menu Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Archive Lab Data options for the LAB DATA file (#63) that were under the Lab Liaison menu are now located under the new Archiving menu \[LRAR ARCHIVE MAIN MENU\]. The functionalities of the Archive Lab Data options are the same.

> **NOTE:** This document is a revision of the November 1995 documentation for the Laboratory Enhanced Archiving. Please replace the old version with this October 1996 revision.

# Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Enhanced Archiving patch does not require any setup by the Laboratory Information Manager (LIM).

All users can remain on the system during the installation. However, be sure no one is using the current Laboratory Archiving options during the installation.

The initialization process for this patch at the test sites took approximately one minute during a period of relatively low system activity.

> **NOTE:** Laboratory Version 5.2, FileMan V. 21, and patches DI\*21\*6, DI\*21\*8, DI\*21\*17, DI\*21\*27, and patch LR\*5.2\*105 *must* be installed before this patch.

## KIDS Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be loaded with users on the system. Do not run installation while the current Laboratory Archiving options are in use. Installation will take less than three minutes.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation and Distribution System Menu, select the Installation menu.

3\. From this menu, you may elect to use the following options (when prompted for INSTALL NAME, enter LR\*5.2\*59):

1.  

Backup a Transport Global option creates a backup message of any routines exported with the patch. It will *not* backup any other changes such as DDs or templates.

2.  
3.  

Compare Transport Global to Current System option allows you to view all changes made during the patch installation. It compares all components of the patch (routines, DDs, templates, etc.).Verify Checksums in Transport Global option allows you to ensure the integrity of the routines that are in the transport global.

4\. Use the Install Package(s) option and select the package LR\*5.2\*59.

5\. When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//, respond NO.

6\. MSM sites: answer YES when asked if you want to move the routines to other systems and indicate the appropriate CPUs.

7\. Once the installation has run to completion, you may delete the LRARIPRE and LRARIPOS routines.

### Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA MailMan 7.1 service for LABUSER, ONE@DEV. VA.GOV

You last used MailMan: 9 Oct 96 10:31

You have 1 new message.

Subj: LR\*5.2\*59 \[#58844\] 9 Oct 96 14:25 EDT 9034 Lines

From: \<NPM \[#20979431\]@XXXXX.XX.XXX\> in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

\$TXT Created by LABUSER,ONE at DEV.VA.GOV (KIDS) on WEDNESDAY, 0

10/9/96 at 10:54

=============================================================================

Run Date: OCT 9, 1996 Designation: LR\*5.2\*59

Package: LR - LAB SERVICE Priority: Mandatory

Version : 5.2 Status: Released

=============================================================================

...

Subject: ARCHIVING ENHANCEMENT

Category:

\- Enhancement (Mandatory)

Description:

============

...

Select MESSAGE Action: IGNORE (in IN basket)// X

Select PackMan function: ?

Answer with PackMan function NUMBER, or NAME

Choose from:

1 ROUTINE LOAD

2 GLOBAL LOAD

3 PACKAGE LOAD

4 SUMMARIZE MESSAGE

5 PRINT MESSAGE

6 INSTALL/CHECK MESSAGE

7 INSTALL SELECTED ROUTINE(S)

8 TEXT PRINT/DISPLAY

9 COMPARE MESSAGE

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 142 Message \#58844 Unloading KIDS Distribution LR\*5.2\*59

LR\*5.2\*59.

Want to Continue with Load? YES//\<RET\>

Loading Distribution...

...

Select PackMan function:\<RET\>

Select MESSAGE Action: IGNORE (in IN basket)// ^

Select MailMan Menu Option: ^KIDS Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option: ?

Edits and Distribution ...

Utilities ...

Installation ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Kernel Installation & Distribution System Option: INSTALLATION

Select Installation Option: ?

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Installation Option: BACKUP a Transport Global

Select INSTALL NAME: LR\*5.2\*59 Loaded from Distribution 10/9/96@14:48:47

=\> LR\*5.2\*59

This Distribution was loaded on Oct 15, 1996@14:48:47 with header of

LR\*5.2\*59

It consisted of the following Install(s):

LR\*5.2\*59

Subject: LR\*5.2\*59 BACKUP

Loading Routines for LR\*5.2\*59..................................................

Send mail to: LABUSER, ONE Last used MailMan: 9 Oct 96 08:12

Select basket to send to: IN//\<RET\>

And send to:

Select Installation Option: VERIFY Checksums in Transport Global

Select INSTALL NAME: LR\*5.2\*59 Loaded from Distribution 10/15/96@14:48 :48

=\> LR\*5.2\*59

DEVICE: HOME// PRINTER

PACKAGE: LR\*5.2\*59 Oct 15, 1996 2:48 am PAGE 1

------------------------------------------------------------------------------

50 Routine checked, 0 failed.

Select Installation Option: INSTALL Package(s)

Select INSTALL NAME: LR\*5.2\*59 Loaded from Distribution 10/15/96@14:49:40

=\> LR\*5.2\*59

This Distribution was loaded on Oct 15, 1996@14:49:40 with header of

LR\*5.2\*59

It consisted of the following Install(s):

LR\*5.2\*59

Will first run the Environment Check Routine, LR59

Environment Check is Ok ---

Install Questions for LR\*5.2\*59

64.19999 ARCHIVED WKLD DATA

> **NOTE:** You already have the 'ARCHIVED WKLD DATA' File.

67.99999 ARCHIVED LAB MONTHLY WORKLOADS

> **NOTE:** You already have the 'ARCHIVED LAB MONTHLY WORKLOADS' File.

95.11 LAB ARCHIVAL ACTIVITY

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<RET\>

Install Started for LR\*5.2\*59 :

Oct 15, 1996@14:51:50

Installing Routines

Oct 15, 1996@14:51:54

Running Pre-Install Routine: ^LRARIPRE

\>\>\> Deleting OLD 'LAB' ARCHIVE FILES.

DELETING ARCHIVED WKLD DATA FILE.

DELETING ARCHIVED LAB MONTHLY WORKLOADS FILE.

DELETING ARCHIVED BLOOD INVENTORY FILE.

The data dictionaries for these files will be reinstalled during the inits.

Installing Data Dictionaries:

Oct 15, 1996@14:52:03

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing OPTION

Oct 15, 1996@14:52:17

Running Post-Install Routine: ^LRARIPOS\>\>\> Deleting OLD 'LAB' ARCHIVING options in OPTION file.

LR ARCHIVE CLEAR

----------------

REMOVED from 'LR ARCHIVE MENU' menu...

'LR ARCHIVE CLEAR' REMOVED from OPTION file...

LR ARCHIVE DATA

---------------

REMOVED from 'LR ARCHIVE MENU' menu...

'LR ARCHIVE DATA' REMOVED from OPTION file...

LR ARCHIVE MENU

---------------

REMOVED from 'LRLIASON' menu...

REMOVED from 'LRLIAISON' menu...

'LR ARCHIVE MENU' REMOVED from OPTION file...

LR ARCHIVE NP CONVERSION

------------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE NP CONVERSION' REMOVED from OPTION file...

LR ARCHIVE PURGE

----------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE PURGE' REMOVED from OPTION file...

LR ARCHIVE READ MEDIA

---------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE READ MEDIA' REMOVED from OPTION file...

LR ARCHIVE RESTORE

------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE RESTORE' REMOVED from OPTION file...

LR ARCHIVE SEARCH

-----------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE SEARCH' REMOVED from OPTION file...

LR ARCHIVE WRITE MEDIA

----------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'LR ARCHIVE WRITE MEDIA' REMOVED from OPTION file...

Removing Print template LR ARCHIVE EXTRACT 65

Removing Print template LR ARCHIVE EXTRACT 67.9

Removing Print template LR ARCHIVE EXTRACT 64.1

Linking LRAR ARCHIVE MAIN MENU option to LRLIAISON ...

Added option LRAR ARCHIVE MAIN MENU to LRLIAISON.

Installation of patch LR\*5.2\*59 completed.

Updating Routine file...

Updating KIDS files...

LR\*5.2\*59 Installed.

Oct 15, 1996@14:52:26------------------------------------------------------------------------------

+------------------------------------------------------------+

100% \| 25 50 75 \|

Complete +------------------------------------------------------------+

Install Completed

### Routine Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the conclusion of the installation process, the following seven routines were moved to LRAR namespace and should be deleted:

LRCHIV LRCHIV ;SLC/RWF - SET UP O("S") VARIABLES FOR ARCHIVE. ;2/5/91 12:30

LRCHIVD LRCHIVD;SLC/MRH/DALISC/FHS - DEARCHIVE FROM ^LAR TO ^LR ;2/5/91 12:31

LRCHIVE LRCHIVE;SLC/RWF - REMOVE OLD DATA FROM PT. FILE ;8/10/89 11:11 ;

LRCHIVK LRCHIVK;SLC/RWF - REMOVE OLD LAB DATA ; 12/14/87 15:46 ;

LRNPXA LRNPXA ;SLC/MRH/FHS - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

LRNPXA0 LRNPXA0;SLC/MRH/FHS/J0 - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

LRNPXA1 LRNPXA1;SLC/MRH/FHS/JB0 - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains post installation instructions for IRM Service to implement the Lab Archiving once the LR\*5.2\*59 installation is complete.

All Sites

Security Key: IRM Service assigns the LRAR ARCHIVE key to persons who perform laboratory archiving functions. This key locks the Archiving Menu \[LRAR ARCHIVE MAIN MENU\] option.

> **NOTE:** The Laboratory Information Manager (LIM) is responsible for designating security key assignments.

# Data Dictionary Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LRAR is the package file entry namespace for Laboratory Enhanced Archiving Patch LR\*5.2\*59.

## New File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one new file created with Laboratory Enhanced Archiving Patch LR\*5.2\*59:

LAB ARCHIVAL ACTIVITY file (#95.11) ^LAB (95.11,

This file stores information and status of lab data archiving activities.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

95.11,.01 ARCHIVE NUMBER NUMBER

This is a sequential number of an archive activity. Example: Archival activity number 1 would be the first archive performed.

95.11,1 FILE POINTER TO FILE

This is the source file.

95.11,2 SEARCH TEMPLATE POINTER TO SORT TEMPLATE FILE

This is the sort/search template for this archival activity.

95.11,3 PRINT TEMPLATE POINTER TO PRINT TEMPLATE FILE

This is the extract print template used in this archival activity.

95.11,4 SELECT DATE DATE

This is the select date of the archival activity.

95.11,5 ARCHIVER POINTER TO NEW PERSON FILE (#200)

This is the name of the user who is performing the archiving.

95.11,6 NUMBER OF ITEMS TO ARCHIVE NUMBER

This is the number of items to archive.

95.11,7 ARCHIVAL STATUS SET

This is the status of the archival activity.

95.11,7.5 SELECTOR POINTER TO NEW PERSON FILE (#200)

This is the person who selected entries for archival.

95.11,8 PURGER POINTER TO NEW PERSON FILE (#200)

This is the person who performs the purge.

95.11,9 ARCHIVE DATE DATE

This is the archive date of this archival activity.

95.11,10 PURGE DATE DATE

This is the purge date of this archival activity.

95.11,11 DATE LAST PRINTED DATE

This is the date that the listing of items to be archived was last printed.

95.11,12 ARCHIVING ACTION IN PROGRESS SET

Entry will be made here by the system when user begins performing some action to this archival activity and will be deleted when action is complete, to lock out other users.

95.11,13 DATE/TIME ACTIVITY BEGAN DATE

This is the date/time the archiving action currently in progress began.

95.11,14 USER PERFORMING ACTION POINTER TO NEW PERSON FILE (#200)

This is the user that initiated the archiving action.

95.11,15 DESTINATION FILE POINTER TO FILE

This field holds the number of the destination file for this archival activity.

95.11,16 ARCHIVE DEVICE LABEL FREE TEXT

This field holds the label information that identifies your archival medium.

95.11,18 ARCHIVE TASK NUMBER FREE TEXT

This is the task number of the Archive data option for this Lab archival activity.

95.11,19 BEGINNING DATE DATE

The selected date to begin archiving.

## 95.11,20 ENDING DATE DATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The selected date to end archiving.

## ## New Extract Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LRAR ARCHIVE 67.9

LRAR ARCHIVE WKLD DATA 64.1

## Updated Data Dictionaries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ARCHIVED WKLD DATA file (#64.19999)

ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999)

# Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 33 new options exported with Patch LR\*5.2\*59. Descriptions for the new options provided by this patch are as follows.

Lab Archival Activity Report LRAR ARCHIVAL ACTIVITY REPORT

This option allows you to print archival activity information. You may see archival performed, purges performed, the status of the activity, and entries that were not moved.

Routine: LRARREP

Archive Wkld Data file 64.1 NAME: LRAR ARCHIVE 64.1

This option allows you to archive data from WKLD DATA file (#64.1). Data in the specified date range moves to the ARCHIVED WKLD DATA file (#64.19999).

Routine: LRARWKD1

Archive Lab Monthly Workloads file 67.9 LRAR ARCHIVE 67.9

This option allows you to archive data from File \#67.9 for archival purposes. Data in the specified date range moves to the ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999).

Routine: LRARLMW1

Clear Data from the LAR Global LRAR ARCHIVE CLEAR

Data found in the Search Archive option is temporarily removed by this option.

Routine: CLEAN^LRARCHIV

Find Patient's Archived data LRAR ARCHIVE DATA

Once data for a patient is archived, the storage location of the data is saved with the patient's remaining data. This information can be found using this option.

Routine: FIND^LRARCHD

Archive Lab Data 63 LRAR ARCHIVE LAB DATA

Data from laboratory can be archived or restored with these options.

ITEM: LRAR ARCHIVE SEARCH SYNONYM: 1

ITEM: LRAR ARCHIVE WRITE MEDIA SYNONYM: 2

ITEM: LRAR ARCHIVE CLEAR SYNONYM: 3

ITEM: LRAR ARCHIVE READ MEDIA SYNONYM: 4

ITEM: LRAR ARCHIVE PURGE SYNONYM: 5

ITEM: LRAR ARCHIVE DATA SYNONYM: 6

ITEM: LRAR ARCHIVE RESTORE SYNONYM: 8

ITEM: LRAR ARCHIVE NP CONVERSION SYNONYM: 7

Archiving Menu LRAR ARCHIVE MAIN MENU

NAME: LRAR ARCHIVE MAIN MENU MENU TEXT: Archiving Menu

TYPE: menu CREATOR: LABUSER, ONE

LOCK: LRAR ARCHIVE PACKAGE: LABORATORY ARCHIVING

DESCRIPTION: This is the main menu for Lab archiving. Options in this menu

include Archive lab data, Archive Wkld Data, and Archive Lab Monthly

Workloads.

ITEM: LRAR ARCHIVE LAB DATA SYNONYM: ALD

DISPLAY ORDER: 1

ITEM: LRAR ARCHIVE WKLD DATA SYNONYM: AWD

DISPLAY ORDER: 2

ITEM: LRAR ARCHIVE MONTHLY WKLD 67.9 SYNONYM: ALMW

DISPLAY ORDER: 3

ITEM: LRAR ARCHIVE WKLD REPORTS SYNONYM: AWR

DISPLAY ORDER: 4

ITEM: LRAR ARCHIVAL ACTIVITY REPORT SYNONYM: AAR

DISPLAY ORDER: 5

ITEM: LRAR CANCEL ARCHIVAL ACTIVITY SYNONYM: CAA

DISPLAY ORDER: 6

ITEM: LRAR VERIFY FILES SYNONYM: VF

DISPLAY ORDER: 8

ITEM: LRAR DELETE ARCHIVED ENTRIES SYNONYM: DEL

DISPLAY ORDER: 7  
Archive Lab Monthly Workloads 67.9 LRAR ARCHIVE MONTHLY WKLD 67.9

This is the menu to archive LAB MONTHLY WORKLOADS file (#67.9).

ITEM: LRAR SELECT ENTRIES 67.9 DISPLAY ORDER: 1

ITEM: LRAR ARCHIVE 67.9 DISPLAY ORDER: 2

ITEM: LRAR WRITE MEDIA 67.99999 DISPLAY ORDER: 3

ITEM: LRAR CLEAR 67.99999 DISPLAY ORDER: 4

ITEM: LRAR READ MEDIA 67.99999 DISPLAY ORDER: 5

ITEM: LRAR PURGE 67.9 DISPLAY ORDER: 6

Convert Archived Data to use NEW PERSON file LRAR ARCHIVE NP

CONVERSION

After previously archived data is restored to the ^LAR global, run this option to convert any records that were not converted during the install of LAB V5.2. Do this before moving the data back into the ^LR global. Records previously converted will be unaffected.

Routine: LRARNPXA

Purge Data Found in the Search Option LRAR ARCHIVE PURGE

Data found in the Search Archive option is stored in the ^LAR global. Data is removed from the Lab Data file (#63) (^LR global) based on the data in the ^LAR global. The ^LAR data must be written to separate media, the Clear archive option run, the data read back from the media, then this option can be run to complete the archive. Note that the data is removed from both the ^LR and the ^LAR globals.

Routine: PURGE^LRARCHIV

Read Data from Off-line Media LRAR ARCHIVE READ MEDIA

After the ^LAR global is cleared, the data is read back in to verify and purge what has been archived.

Entry Action: W !!,"The site manager should determine the method of data retrieval of the",!,"^LAR global."

Restore Archived Data to LR Global LRAR ARCHIVE RESTORE

Used to restore data into the LR global that has been archived.

Routine: LRARCHD

Search for Lab Data to Archive LRAR ARCHIVE SEARCH

Data to be archived must be older than the beginning of the month three months ago, on a patient not currently on a ward, and on a permanent page. If the data is before the time specified above it will be purged if unverified. Microbiology, Anatomic Pathology, and Blood Bank data are not archived.

Routine: SEARCH^LRARCHIV

Archive Wkld Data 64.1 LRAR ARCHIVE WKLD DATA

This is the menu to archive WKLD DATA file (#64.1).

ITEM: LRAR SELECT ENTRIES 64.1 DISPLAY ORDER: 1

ITEM: LRAR ARCHIVE 64.1 DISPLAY ORDER: 2

ITEM: LRAR WRITE MEDIA 64.19999 DISPLAY ORDER: 3

ITEM: LRAR CLEAR 64.19999 DISPLAY ORDER: 4

ITEM: LRAR READ MEDIA 64.19999 DISPLAY ORDER: 5

ITEM: LRAR PURGE 64.1 DISPLAY ORDER: 6

Workload Reports from Archived Files LRAR ARCHIVE WKLD REPORTS

This menu contains all archived workload reports.

ITEM: LRARCAM4

ITEM: LRARCPTS

ITEM: LRARCML

ITEM: LRARCMA

Write Data to Off-line Media LRAR ARCHIVE WRITE MEDIA

After having created entries in the ^LAR global, the data is written to off-line media for purposes of long term storage. ENTRY ACTION: W !!,"The site manager should determine the method of data storage of the",!,"^LAR global."

Cancel Lab Archival Activity LRAR CANCEL ARCHIVAL ACTIVITY

This option allows you to cancel a lab archival activity. This is necessary if you begin the archival process and then decide not to purge.

Routine: ENTC^LRARU

Clear Archived Wkld Data file 64.19999 LRAR CLEAR 64.19999

This option clears the data from ARCHIVED WKLD DATA file (#64.19999). All data is removed from File \#64.19999.

Routine: CLEAR^LRARWKD

Clear Archived Lab Monthly Workloads file 67.99999 LRAR CLEAR 67.99999

This option clears the data from the ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999). All data is removed from File \#67.99999.

Routine: CLEAR^LRARLMW

Delete Archived File Entries LRAR DELETE ARCHIVED ENTRIES

This option deletes existing archived file entries in the Archived Wkld Data (#64.19999) or Archived Lab Monthly (#67.99999) files once the Lab archival activity is canceled.

Routine: DEL^LRARU

Purge Wkld Data file 64.1 LRAR PURGE 64.1

This option purges data from WKLD DATA file 64.1. Data is removed from File \#64.1 based on the data in ARCHIVED WKLD DATA file (#64.19999). Once this option is run, the data cannot be restored electronically to File \#64.1. This option also deletes all data from the File \#64.19999.

Routine: LRARPW

Purge Lab Monthly Workloads file 67.9 LRAR PURGE 67.9

This option allows you to purge data from File \#67.9 for archival purposes. The purging of data is based on the data in ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999). Once this option is run, the data cannot be restored electronically to File \#67.9. This option also deletes all data from the File \#67.99999.

Routine: LRARPLM

Read Data from Off-line Media LRAR READ MEDIA 64.19999

After having cleared the entries in the ARCHIVED WKLD DATA file (#64.19999), the data can be read back in to verify what has been archived.

Entry Action: W!!,"The site manager should determine the method of data retrieval “,!,”of the Archived Wkld Data File \#64.19999."

Read Data from Off-line Media LRAR READ MEDIA 67.99999

After having cleared the entries in the ARCHIVED LAB MONTHLY WORKLOADS (#67.99999), the data should be read back in to verify what has been archived. Entry Action: W!!,"The site manager should determine the method of data retrieval",!,"of the ARCHIVED LAB MONTHLY WORKLOADS file (#67.9999)."

Select Entries to Archive 64.1 LRAR SELECT ENTRIES 64.1

This option allows you to select entries in the WKLD DATA file (#64.1) for archival by date. You can also print the entries selected.

Routine: LRARWKD

Select Entries to Archive LRAR SELECT ENTRIES 67.9

This option allows you to select entries in the LAB MONTHLY WORKLOADS file (#67.9) for archival by date. You can also print the entries selected.

Routine: LRARLMW

Verify Files for Archiving LRAR VERIFY FILES

This option allows the LIM to verify the data in either the WKLD DATA, or LAB MONTHLY WORKLOADS files. This option should be run *before* archiving any of these files. It is *very* important to fix the problems in the source data, or the records with bad data are not archived.

Routine: VER^LRARVER

Write Data to Off-line Media LRAR WRITE MEDIA 64.19999

After having created entries in the ARCHIVED WKLD DATA file (#64.19999), the data should be written to off-line media for purposes of long term storage.

Entry Action: S LRART=64.1

Routine: WRITE^LRARU1

Write Data to Off-line Media LRAR WRITE MEDIA 67.99999

After having created entries in the ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999), the data should be written to off-line media for purposes of long-term storage.

ENTRY ACTION: S LRART=67.9

Routine: WRITE^LRARU1

Lab Monthly Workloads LRARCAM4

This option provides a report based on treating specialty codes. This report is derived from the ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999).

Routine: LRARCAM4

Workload Statistics By Major Section LRARCMA

Archived workload report summed by LAB division, major section and subsection.

Routine: LRARCMA

Workload Cost Report By Major Section LRARCML

Archived workload report summed by major section and lab subsection.

Routine: LRARCML

Treating Specialty Workload Report LRARCPTS

Archived Treating Specialty WKLD Workload report.

Routine: LRARCPTS

## Option Name Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old Option New Option

LR ARCHIVE CLEAR LRAR CLEAR

LR ARCHIVE DATA LRAR ARCHIVE

LR ARCHIVE MENU LRAR ARCHIVE MAIN MENU

LR ARCHIVE NP CONVERSION LRAR ARCHIVE NP CONVERSION

LR ARCHIVE PURGE LRAR PURGE

LR ARCHIVE READ MEDIA LRAR READ MEDIA

LR ARCHIVE RESTORE LRAR ARCHIVE RESTORE

LR ARCHIVE SEARCH LRAR ARCHIVE SEARCH

LR ARCHIVE WRITE MEDIA LRAR WRITE MEDIA

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 50 routines (49 new, and 1 modified) associated with this patch:

## New Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LRARC1 LRARC1A LRARCAM4 LRARCAM5 LRARCAM6 LRARCAM7 LRARCAM8 LRARCAM9

LRARCHD LRARCHE LRARCHIV LRARCHK LRARCMA LRARCMA1 LRARCMA2 LRARCMA3

LRARCML LRARCML1 LRARCML2 LRARCML3 LRARCMR LRARCMR1 LRARCMR2 LRARCPTS

LRARCR1 LRARCR1A LRARCR2 LRARCR3 LRARCR3A LRARCR3B LRARCR4 LRARCTS1

LRARCU LRARIPOS LRARIPRE LRARLMW LRARLMW1 LRARNPX LRARNPX0 LRARNPX1

LRARNTEG LRARPLM LRARPW LRARREP LRARU LRARU1 LRARVER LRARWKD

LRARWKD1

## Modified Routine 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LRCAPML

## Integration Agreement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The integration agreement for Laboratory Enhanced Archiving is listed on the Data Base Administrator (DBA) menu on FORUM. Use the Inquire option on the Integration Agreements menu to examine DBIA# 1618 on the VA FILEMAN Custodial Package.

# User Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Enhanced Archiving Patch LR\*5.2\*59 provides archiving capability for the following Laboratory files:

• WKLD DATA (#64.1)

• LAB MONTHLY WORKLOADS (#67.9)

The benefit of archiving workload data is to regain disk space from the ^LRO global. The archive stores the data in resolved format so that additional files are not needed to utilize the archived data.

The FileManager Extract Tool is used to move the data from the source file to a destination (archive) file. If the data is a pointer value, the Extract Tool transforms the data so that it is in the resolved textual state once it is transferred to the destination file. You can restore data from the archive file to a medium of choice. After the data from the archive file has been copied to external media, the data can then be purged from the source file. Once the data is purged from the source file, it is not possible to restore the data to the source.

The data from the storage media can be restored to the archive file. The data dictionary for the archive file contains no pointer fields.

Reporting capabilities include workload reports from archived workload files. For extended search and reporting capabilities, it may be advantageous to store the data to an off-line medium. The data may then be manipulated by several application software, for example, Access, Excel, Word, etc.

CAUTION

- 
- 
- 
- 
- 
- 
- 
- 
- 

## ## ## ## - 
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 
- 
- 
- 
- 

The Verify and Archive options are very resource intensive and should be queued to run during off hours and with a low priority.Be sure to queue the Archive Wkld Data 64.1 option during hours of low activitybecause of possible effects on system performance.The archive temporarily requires additional disk space. Source data of 1K requires 1 to 1.5K to store the data in the archived data files, ARCHIVED WKLD DATA (#64.19999)and ARCHIVED LAB MONTHLY WORKLOADS (#67.99999). These archived data files are stored in the ^LAR global. You need to ensure that there is enough disk space before archiving.NOTESA file can have only *one* archival activity at a time. A second archive from a file cannot be performed until the active archival activity is completed either by purging or canceling.The LAB ARCHIVAL ACTIVITY file (#95.11), which is a new file, contains a brief history that describes who performed the various archival activity steps and when the steps were completed.You can cancel your archival activity, by using the Cancel option, at any time before the Purge option.To access the archiving options you must own the LR SUPERVISOR, LR LIAISON, and LRAR ARCHIVE security keys.The archiving process temporarily uses additional disk space and if disk space is already critical, sufficient space may not be available for archiving.It is recommended to archive data on a quarterly basis. Archive job should be queued to run during off-hours and at a low priority.Menu ChangeThe Archive Lab Data options for the LAB DATA file (#63) that were under the Lab Liaison menu are now located under the new Archiving menu \[LRAR ARCHIVE MAIN MENU\]. The functionalities of the Archive Lab Data options are the same, only the namespace and location are changed.  
Archival Process![](lr-5-2-59-laboratory-archiving-technical-and-user-guide/002.png)Lab Archival ActivityLab archival activity is tracked using the new LAB ARCHIVAL ACTIVITY file (#95.11). This file holds the following information:the internal entry number of the NEW PERSON file (#200) (DUZ) of the individual performing the archival activitythe status of the archival activity (e.g., ARCHIVED, PURGED, or CLEARED)the dates on which the archival activities were performedthe number of entries archivedthe source file numberthe search/sort and print templates used in the archival activity

This information is retrieved by using the Lab Archival Activity Report option.

### Steps to Complete Archival Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For an archival activity to be completed the following options must be performed:

> 1\. Select (using the appropriate Select Entries to Archive options)

> 2\. Verify (using the Verify Files for Archiving option)

> 3\. Archive (using the appropriate new Archive options)

> 4\. Write data to off-line media (using the appropriate Write Data to Off-line Media options)

> 5\. Clear (using the appropriate Clear Archived options)

> 6\. Read data from off-line media (using the appropriate Read Data from Off-line Media options)

> 7\. Purge (using the appropriate Purge options)

## How to Access Archiving Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supervisor menu \[LRSUPERVISOR\]

Lab Liaison menu \[LRLIASON\]

Archiving Menu \[LRAR ARCHIVE MAIN MENU\]

> ALD Archive lab data 63 ...

> AWD Archive Wkld Data 64.1 ...

> ALMW Archive Lab Monthly Workloads 67.9 ...

> AWR Workload Reports from Archived Files ...

> AAR Lab Archival Activity Report

> CAA Cancel Lab Archival Activity

> DEL Delete Archived File Entries

> VF Verify Files for Archiving

### Option Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For demonstration purposes, we have selected the sub options under the Archive Wkld Data 64.1. The functionalities of the sub options for Archive Lab Monthly Workloads 67.9 are similar.

The archival process consists of the following options:

#### Select Entries to Archive 64.1

The Select Entries to Archive 64.1 option initiates the archival activity. The entries are selected and an entry in the Lab Archival Activity file is created. After you use this option, the LAB ARCHIVAL ACTIVITY file (#95.11) entry is marked with the status of *selected*. If an unfinished archival activity exists for a file and you select this same file for a subsequent archival activity, you see the following message:

There is an outstanding archival activity.

Please finish or cancel this activity before you begin another.

This option selects the entries for archiving. The user enters a range of dates or other selection criteria for data to be archived. Printing of entries selected is optional. The user can select which fields to print.

Example

This option allows you to select entries in the WKLD DATA file (#64.1) for archival by date. You can optionally print the selected entries and choose which fields to print.

Select Archive Wkld Data 64.1 Option: SELECT Entries to Archive 64.1

First enter a date range selection to archive the

WKLD DATA file (64.1).

\*\*\*\* Date Range Selection \*\*\*\*

Beginning DATE: 1 1 96 (JAN 01, 1996)

Ending DATE: 3 31 96 (MAR 31, 1996)

WOULD YOU LIKE TO PRINT SELECTED ENTRIES? YES// \<RET\>

FIRST PRINT FIELD: .01 INSTITUTION

THEN PRINT FIELD: DATE (multiple)

THEN PRINT DATE SUB-FIELD: .01 DATE

THEN PRINT DATE SUB-FIELD: \<RET\>

THEN PRINT FIELD: \<RET\>

DEVICE: PRINTER

WKLD DATA LIST JUL 12,1996 08:53 PAGE 1

INSTITUTION DATE

------------------------------------------------------------------------------

XXXXXX,XX JAN 4,1996

XXXXXX,XX MAR 19,1996

XXXXX, XX JAN 3,1996

XXXXX, XX JAN 4,1996

XXXXX, XX JAN 22,1996

XXXXX, XX FEB 12,1996

XXXXX, XX FEB 14,1996

XXXXX, XX FEB 21,1996

XXXXX, XX FEB 22,1996

XXXXX, XX FEB 27,1996

XXXXX, XX MAR 11,1996

XXXXX, XX MAR 13,1996

XXXXX, XX MAR 18,1996

XXXXX, XX MAR 19,1996

XXXXX, XX MAR 22,1996

XXXXXX X JAN 10,1996

XXXXXX X JAN 26,1996

XXXXXX X FEB 6,1996

XXXXXX X FEB 15,1996

XXXXXX X MAR 4,1996

XXXXXX X MAR 13,1996

XXXXXX X JAN 1,1996

XXXXXX X JAN 3,1996

XXXXXX X JAN 4,1996

XXXXXX X JAN 5,1996

#### Cancel Option

You can cancel an archival activity any time before the entries are purged by using the Cancel option. This is necessary if you begin the archival process and then decide not to purge.

After you cancel an archival activity, the LAB ARCHIVAL ACTIVITY file (#95.11) reference to the archival activity is deleted.

NOTES

- 
- 
- 

#### #### - 
- 
- 

To delete archived file entries, press \<RET\> at the Delete the archived file entries created by this lab archival activity? YES// prompt.To retain the archived file entries without purging data from the source file, enter NO at the prompt.To delete the retained archived file entries before beginning another archival activity, use the Delete Archived File Entries option.ExampleSelect Archiving Menu Option: CANCEL Lab Archival ActivityCANCEL WHICH LAB ARCHIVING SELECTION: ??Choose from: 1 WKLD DATA 07-11-96 LABUSER, ONE PURGED LABUSER, ONE 2 WKLD DATA 07-13-96 LABUSER, TWO ARCHIVED LABUSER, TWO 3 LAB MONTHLY WORKLOADS 07-13-96 LABUSER, ONE PURGED LABUSER, ONE CANCEL WHICH LAB ARCHIVING SELECTION: 2 WKLD DATA 07-13-96 LABUSER, TWO ARCHIVED LABUSER, TWOAre you sure you want to CANCEL this LAB ARCHIVING ACTIVITY? NO// YESThis archival activity has already updated the archived file.Delete the archived file entries created by this lab archival activity? YES// \<RET\>I will now CLEAR out the global.\>\>\> DONE \<\<\<  
Delete Archived File Entries OptionThis option deletes retained archived file entries in the Archived Wkld Data (#64.19999) or Archived Lab Monthly (#67.99999) files once the laboratory archival activity is canceled.ExampleSelect Archiving Menu Option: DELETE Archived File Entries Select one of the following: 1 ARCHIVED WKLD DATA 2 ARCHIVED LAB MONTHLY WORKLOADSFILE: 1 ARCHIVED WKLD DATAI will now CLEAR out the global.Done.  
Verify Files for ArchivingSelect the file you want to verify, WKLD DATA, or LAB MONTHLY WORKLOADS.Select either the whole file or selected entries to archive. To verify only selected entries, you must select entries to archive before running this option. Verifying the whole file is not recommended because of the lengthy processing time.Select device to print the report.

Example

Select Archiving Menu Option: VF Verify Files for Archiving

Select one of the following:

1 WKLD DATA

2 LAB MONTHLY WORKLOADS

FILE: 1 WKLD DATA

Select one of the following:

1 WHOLE FILE

2 Selected entries for archiving

NUMBER: 2 Selected entries for archiving

DEVICE: HOME// PRINTER

Verify Fields File: 64.1 WKLD DATA JUL 12, 1996 PAGE 1

Entry \# Name

Field Name (Field \#) Type ERROR

------------------------------------------------------------------------------

578 578

2960227 2960227 (DATE)

70 70 (WKLD CODE)

817 817 (ACCESSION WKLD CODE TIME)

TREATING SPECIALITY (#16) POINTER No 'B' in pointed-to File

578 578

2960227 2960227 (DATE)

329 329 (WKLD CODE)

817 817 (ACCESSION WKLD CODE TIME)

TREATING SPECIALITY (#16) POINTER No 'B' in pointed-to File

578 578

2960322 2960322 (DATE)

70 70 (WKLD CODE)

700 700 (ACCESSION WKLD CODE TIME)

TREATING SPECIALITY (#16) POINTER No 'P' in pointed-to File

578 578

2960322 2960322 (DATE)

329 329 (WKLD CODE)

700 700 (ACCESSION WKLD CODE TIME)

TREATING SPECIALITY (#16) POINTER No 'P' in pointed-to File

> **NOTE:** The next step is the Archive option. Before you can run the Archive option, you must run the Select Entries option.

Select Archiving Menu Option: AWD Archive Wkld Data 64.1

Select Entries to Archive 64.1

Archive Wkld Data file 64.1

Write Data to Off-line Media

Clear Archived Wkld Data file 64.19999

Read Data from Off-line Media

Purge Wkld Data file 64.1

#### Archive Wkld Data file 64.1

This option calls the FileMan Extract Tool to copy the data from the source file to the archived data file. All entries within the date range or other selection criteria are copied to an archived data file. If the data is a pointer value, it is copied in its resolved textual form.

Archive Workload Data Task StatisticsThe following information shows a queued and interactive session for one day of data at an alpha site.Session 1: QueuedGlobal Archived ^LRO(64.1,583,1,2960919)Queued Start Time 1800 hoursTime Completed 2233 hoursElapsed Time 4 hours 33 minutesBlock Size 887 blocksArchived file size: ^LAR(64.19999) block size: 1841 blocksSession 2: InteractiveGlobal Archived ^LRO(64.1,583,1,2960919)Start Time 1055 hoursTime Completed 1213 hoursElapsed Time 1 hour 58 minutesBlock Size 897 blocksArchived file size: ^LAR(64.19999) block size: 1838 blocksNOTE: This job should be queued to run during off hours and at a low priority.

Example:

Select Archive Wkld Data 64.1 Option: ARCHIVE Wkld Data file 64.1

You should not archive or purge until DSS extraction has been completed.

Please consult with DSS coordinator.

Archiving WKLD DATA file

Beginning date: JAN 1,1996

Ending date: MAR 31,1996

ARE YOU SURE YOU WANT TO CONTINUE? NO// YES

Start archiving and PRINT error report on device: PRINTER

The following records in the file were not moved because of one or more errors:

Entry \# 700029 was NOT processed because:

The value '700029' is not a valid pointer to File \#4.

Entry \# 2960227,578, was NOT processed because:

The value 'B' is not a valid pointer.

Entry \# 2960322,578, was NOT processed because:

The value 'P' is not a valid pointer.

\*\*\* PLEASE KEEP THIS FOR FUTURE REFERENCE \*\*\*

#### Write Data to Off-line Media

The data in the archived data file is transferred to off-line media. The site manager determines the method of data storage of the archived data file. This option checks the status of the tasked archive job for completion and provides the opportunity to enter the archive device label into the LAB ARCHIVAL ACTIVITY file (#95.11).

> **NOTE:** When moving data to a PC to manipulate with FileMan, include the data dictionary and data in the archived file. In this case, use KIDS to generate a build that contains the data and the data dictionary. You can then save the build to off-line media. When retrieving data from long term storage, this ensures the data dictionaries are the same. For more information regarding KIDS, refer to the Kernel V. 8.0 Systems Manual.

Example 1: Incomplete Tasked Archive Job

Select Archive Wkld Data 64.1 Option: Write data to off-line media

The site manager should determine the method of data storage of the

Archived Wkld Data File 64.19999

I cannot find an archival activity for this file in the archived status.

The following Archival Activity is in progress--no access allowed!

JUL 14, 1996@13:49:32 STARTED: JUL 14,1996@13:49:32 BY: LABUSER, ONE

Example 2: Completed Tasked Archive Job

Select Archive Wkld Data 64.1 Option: WRITE data to off-line media

The site manager should determine the method of data storage of the

Archived Wkld Data File 64.19999

ARCHIVE DEVICE LABEL: ARCHIVE WKLD DATA 7/14/96 SSNOTE: The next step is the Clear option. Before you can run the Clear option, you must run the Archive option.

#### Clear Archived Wkld Data file 64.19999

This option deletes the data in the archived data file.

Example

Select Archive Wkld Data 64.1 Option: CLEAR Archived Wkld Data file 64.19999

This will clear the data from the Archived Wkld Data file.

ARE YOU SURE YOU WANT TO DO THIS? YES// \<RET\>

I will now CLEAR out the global.

\>\>\> DONE \<\<\<

#### Read Data from Off-line Media

The archived data file is read from the off-line media to verify the readability of the backup. The site manager should determine the method of data retrieval of the file.

Example

Select Archive Wkld Data 64.1 Option: READ data from off-line media

The site manager should determine the method of data retrieval

of the Archived Wkld Data File 64.19999.

> **NOTE:** The next step is the Purge option. Before you can run the Purge option, you must run the Clear option.

#### Purge Wkld Data file 64.1

This option purges the records in the source file that were moved successfully into the archived data file. Once this option is run, the archived data file is cleared.

Example

Did you make a backup of the ARCHIVED WKLD DATA file (64.19999)? YES

Did you check the backup of the ARCHIVED WKLD DATA file? YES

Okay to delete WKLD DATA entries? YES

Purging...

DONE.

I will now CLEAR out the Archived Workload Data global.

\>\>\>DONE\<\<\<

## Workload Reports from Archived Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These reports are similar to the Workload Reports option, in Laboratory V. 5.2, except for the modifications to print from the archived data files.

### Lab Monthly Workloads Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example

Select Workload Reports from Archived Files Option: Lab Monthly Workloads

Select Division: XXXXXX X// \<RET\> TEXAS 7000

Select Month: 3 96 MAR 1996

Select Month: \<RET\>

Select one of the following:

1 All workload

2 LMIP reportable workload

3 Non-LMIP workload

Enter the number for the workload data to report: 1// \<RET\> All workload

Select one of the following:

1 CDR report

Enter the number for the report(s) you want printed: 1// \<RET\> CDR report

CDR format selection:

Select one of the following:

1 Detailed report

2 Summary report

Enter response: 1 Detailed report

DEVICE: PRINTER

DO YOU WANT YOUR OUTPUT QUEUED? NO// YES (YES)

Requested Start Time: NOW// \<RET\> (OCT 11, 1996@12:32:50)

ARCHIVED RCS-CDR/LMIP REPORT

ALL WORKLOAD DATA FOR: MAR 1996 Page 1

Total Count for Report = 30

PTF Treating Specialty

\[ 1110 \] CARDIOLOGY = 1 3.3 %

\[ 1110 \] PULMONARY, NON-TB = 18 60.0 %

\[ 1610 \] INTERMEDIATE MEDICINE = 9 30.0 %

\[ 2000 \] AMBULATORY CARE = 2 6.7 %

ARCHIVED RCS-CDR/LMIP REPORT

ALL WORKLOAD DATA FOR: MAR 1996 Page 2

Total Count for Report = 30

Service Listing

INTERMEDIATE MED = 9 30.0 %

MEDICINE = 19 63.3 %

\[ 2000 \] AMBULATORY CARE = 2 6.7 %

ARCHIVED RCS-CDR/LMIP REPORT

ALL WORKLOAD DATA FOR: MAR 1996 Page 3

Total Count for Report = 30

Billing Bed Section

GENERAL MEDICAL CARE = 19 63.3 %

INTERMEDIATE CARE = 9 30.0 %

\[ 2000 \] AMBULATORY CARE = 2 6.7 %

++Ab ID w Antihuman CNT = 2

\[ 1110 \] PULMONARY, NON-TB 1 50.0 %

+Antibody Detection Type & Scr CNT = 16

\[ 1110 \] PULMONARY, NON-TB 6 37.5 %

\[ 1610 \] INTERMEDIATE MEDICINE 2 12.5 %

ABO Cell Serum and Rh(D) CNT = 16

\[ 1110 \] CARDIOLOGY 1 6.3 %

\[ 1110 \] PULMONARY, NON-TB 4 25.0 %

\[ 1610 \] INTERMEDIATE MEDICINE 3 18.8 %

Antihuman Globulin Test CNT = 15

\[ 1110 \] PULMONARY, NON-TB 5 33.3 %

Autopsy Attendant CNT = 2

\[ 2000 \] AMBULATORY CARE 1 50.0 %

Compatibility Test Crossmatch CNT = 9

\[ 1110 \] PULMONARY, NON-TB 2 22.2 %

\[ 1610 \] INTERMEDIATE MEDICINE 1 11.1 %

Extraction w Organic Solvent CNT = 6

\[ 1610 \] INTERMEDIATE MEDICINE 3 50.0 %

Initial Handling Clerical Aut CNT = 2

\[ 2000 \] AMBULATORY CARE 1 50.0 %

Venipuncture Travel Time CNT = 0

### Treating Specialty Workload Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example

Select Workload Reports from Archived Files Option: TREATING Specialty Workload Report

Would you like the report in PTF Treating Specialty ? No// \<RET\> (No)

SELECT ALL INSTITUTIONS? YES// NO

Select ARCHIVED WKLD DATA INSTITUTION: XXXXXX X// \<RET\>

BEGINNING DATE/TIME: T-31//6 1 96 (JUN 01, 1996)

ENDING DATE/TIME: T//9 30 96 (SEP 30, 1996)

Select one of the following:

Y YES

N NO

Do you want to select accession areas (YES or NO) : NO// \<RET\>

SUMMARY REPORT ONLY? NO// YES

DEVICE: PRINTER

TREATING SPECIALTY ARCHIVED WORKLOAD REPORT

XXXXXX X PAGE 1

REPORT DATE RANGE: JUN 1,1996 - SEP 30,1996

SUMMARY

TREATING SPECIALTY UNIT COUNT % TOTAL COST %

CARDIOLOGY 16 14.3 12.30 10.4

EMERGENCY ROOM 4 3.6 3.40 2.9

MEDICINE 92 82.1 102.05 86.7

### Workload Cost Report by Major Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Workload Reports from Archived Files Option: WORKLOAD Cost Report By Major Section

PRINT THE COMMENT PAGES? NO// \<RET\>

SELECT ALL INSTITUTIONS? YES// NO

Select ARCHIVED WKLD DATA INSTITUTION: XXXXXX X// \<RET\>

BEGINNING DATE/TIME: T-31//6 1 96 (JUN 01, 1996)

ENDING DATE/TIME: T//9 30 96 (SEP 30, 1996)

Select one of the following:

Y YES

N NO

Do you want to select accession areas (YES or NO) : NO// \<RET\>

SUMMARY REPORT ONLY? NO// YES

DEVICE: PRINTER

.................

ARCHIVED WORKLOAD COST REPORT BY MAJOR SECTION Page 1

REPORT DATE RANGE: JUN 1,1996 - SEP 30,1996

-----------------------------------------------------------------------------

COMBINED SUMMARY

MAJOR SECTION LAB SUBSECTION UNIT COUNT % TOTAL COST %

BLOOD BANK BLOOD BANK 1 0.8 0.00 0.0

CHEMISTRY SPEC CHEMISTRY 63 48.1 12.90 11.0

CHEMISTRY CHEMISTRY 48 36.6 91.05 77.3

CHEMISTRY MANUAL CHEM 3 2.3 3.00 2.5

HEMATOLOGY COAG 1 0.8 0.00 0.0

HEMATOLOGY DIFFS, PLT. EST 6 4.6 4.40 3.7

MICROBIOLOGY MICROBIOLOGY 4 3.1 6.40 5.4

MICROBIOLOGY URINALYSIS 5 3.8 0.00 0.0

COMBINED GRAND TOTAL 131 117.75

ARCHIVED WORKLOAD INPUT MANUALLY Page 2

REPORT DATE RANGE: JUN 1,1996 - SEP 30,1996

\[Includes all manual archived workload data for date range\]

Workload Procedure Code STANDARD QC REPEAT MANUAL

----------------------------------------------------------------------------

+ABO Cell and Rh(D) Typing~S-P 86081.3387 3 2 12 0

+Sodium~ABBOTT TDX 84295.3049 3 2 12 0

+Sodium~SYNCHRON CX3 84295.3120 0 1 0 0

ABO Cell Serum and Rh(D) 86082.0000 1 2 3 4

Concentration of Specimen Dial 82062.0000 3 2 12 0

Extraction w Organic Solvent 82063.0000 0 1 0 0

Osmotic fragility~ABBOTT TDX .3049 0 2 0 0

Venipuncture Outpatient 89343.0000 0 0 0 30

Venipuncture Travel Time 89341.0000 0 0 0 21

Grand SQRM Totals: 10 12 39 55

### Workload Statistics by Major Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example

Select Workload Reports from Archived Files Option: Workload Statistics By Major Section

PRINT THE COMMENT PAGES? NO//\<RET\>

SELECT ALL INSTITUTIONS? YES// NO

Select ARCHIVED WKLD DATA INSTITUTION: XXXXXX X//\<RET\>

BEGINNING DATE/TIME: T-31//6 1 96 (JUN 01, 1996)

ENDING DATE/TIME: T//9 30 96 (SEP 30, 1996)

Select one of the following:

Y YES

N NO

Do you want to select accession areas (YES or NO) : NO// \<RET\>

SUMMARY REPORT ONLY? NO//\<RET\>

DEVICE: PRINTER

.................

ARCHIVED WORKLOAD STATISTICS BY MAJOR SECTION Page 1

REPORT DATE RANGE: JUN 1,1996 - SEP 30,1996

------------------------------------------------------------------------------

COMBINED SUMMARY

MAJOR SECTION LAB SUBSECTION TOTAL

BLOOD BANK BLOOD BANK NUMBER : 1

PERCENT : 0.8

CHEMISTRY SPEC CHEMISTRY NUMBER : 63

PERCENT : 48.1

CHEMISTRY CHEMISTRY NUMBER : 48

PERCENT : 36.6

CHEMISTRY MANUAL CHEM NUMBER : 3

PERCENT : 2.3

HEMATOLOGY COAG NUMBER : 1

PERCENT : 0.8

HEMATOLOGY DIFFS, PLT. ES NUMBER : 6

PERCENT : 4.6

MICROBIOLOGY MICROBIOLOGY NUMBER : 4

PERCENT : 3.1

MICROBIOLOGY URINALYSIS NUMBER : 5

PERCENT : 3.8

GRAND TOTAL 131

ARCHIVED WORKLOAD INPUT MANUALLY Page 2

REPORT DATE RANGE: JUN 1,1996 - SEP 30,1996

\[Includes all manual archived workload data for date range\]

Workload Procedure Code STANDARD QC REPEAT MANUAL

------------------------------------------------------------------------------

+ABO Cell and Rh(D) Typing~S-P 86081.3387 3 2 12 0

+Sodium~ABBOTT TDX 84295.3049 3 2 12 0

+Sodium~SYNCHRON CX3 84295.3120 0 1 0 0

ABO Cell Serum and Rh(D) 86082.0000 1 2 3 4

Concentration of Specimen Dial 82062.0000 3 2 12 0

Extraction w Organic Solvent 82063.0000 0 1 0 0

Osmotic fragility~ABBOTT TDX .3049 0 2 0 0

Venipuncture Outpatient 89343.0000 0 0 0 30

Venipuncture Travel Time 89341.0000 0 0 0 21

Grand SQRM Totals: 10 12 39 55

## Lab Archival Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print archival activity data. You can see archival performed and purges performed, the status of the activity, error and exception report for an archival activity. An exception is when an item in the source file could not be moved to the destination file. The exceptions are listed under The following records in the file were not moved because of one or more errors:. Be sure to check for errors and exceptions *before* moving data to off-line media.

Example

Select LAB ARCHIVAL ACTIVITY ARCHIVE NUMBER: 37 WKLD DATA 07-12-96

LABUSER, ONE ARCHIVED LABUSER, ONE

DEVICE: HOME// PRINTER

ARCHIVAL ACTIVITY REPORT Page 1

Date/Time Printed

JUL 15,1996@08:53

ARCHIVE NUMBER: 37

FILE: WKLD DATA

DESTINATION FILE: ARCHIVED WKLD DATA

ARCHIVAL STATUS: ARCHIVED

SELECT DATE: JUL 12, 1996

SELECTOR: LABUSER, ONE

ARCHIVE DATE: JUL 12, 1996

ARCHIVER: LABUSER, ONE

ARCHIVE TASK NUMBER:

PURGE DATE:

PURGER:

ARCHIVE DEVICE LABEL:

BEGINNING DATE: JAN 01, 1996

ENDING DATE: MAR 31, 1996

The following records in the file were not moved because of one or more errors:

Entry \# 700029 was NOT processed because:

The value '700029' is not a valid pointer to File \#4.

Entry \# 2960227,578, was NOT processed because:

The value 'B' is not a valid pointer.

Entry \# 2960322,578, was NOT processed because:

The value 'P' is not a valid pointer.

\*\*\* PLEASE KEEP THIS FOR FUTURE REFERENCE \*\*\*

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## Archiving Menu \[LRAR ARCHIVE MAIN MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ALD Archive lab data 63

\| 1 Search for lab data to archive

\| 2 Write data to off-line media

\| 3 Clear data from the LAR global

\| 4 Read data from off-line media

\| 5 Purge data found in the Search option

\| 6 Find patient's archived data

\| 7 Convert archived data to use New Person file

\| 8 Restore archived data to LR global

AWD Archive Wkld Data 64.1

\| Select Entries to Archive 64.1

\| Archive Wkld Data file 64.1

\| Write Data to Off-line Media

\| Clear Archived Wkld Data file 64.19999

\| Read Data from Off-line Media

\| Purge Wkld Data file 64.1

ALMW Archive Lab Monthly Workloads 67.9

\| Select Entries to Archive

\| Archive Lab Monthly Workloads file 67.9

\| Write Data to Off-line Media

\| Clear Archived Lab Monthly Workloads file 67.99999

\| Read Data from Off-line Media

\| Purge Lab Monthly Workloads file 67.9

AWR Workload Reports from Archived Files

\| Lab Monthly Workloads

\| Treating Specialty Workload Report

\| Workload Statistics By Major Section

\| Workload Cost Report By Major Section

AAR Lab Archival Activity Report

CAA Cancel Lab Archival Activity

DEL Delete Archived File Entries

VF Verify Files for Archiving