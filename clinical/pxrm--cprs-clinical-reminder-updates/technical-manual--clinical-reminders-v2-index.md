---
title: Clinical Reminders Version 2 Index Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: Index
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 3
description: The Clinical Reminders Index global has been designed to provide an index of clinical data, which supports rapid access to clinical data. It is used by Clinical Reminders v2.0, which evaluates reminders in 1/3 to 1/2 the time that v1.5 required. A large part of the speedup can be attributed to the I
audience: 
keywords: 
  - index
  - date
  - pxrmindx
  - table
  - contents
  - clinical
  - reminders
  - global
  - class
  - number
page_count: 0
word_count: 8713
section_count: 25
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_index_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_index_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

Clinical Reminders IndexTechnical Manual

![](clinical-reminders-version-2-index-technical-manual/001.png)

May 2021

Provider Systems

Office of Information and Technology

## REVISION HISTORY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 46%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Pages</strong></th>
<th><strong>Description</strong></th>
<th><p><strong>Developer/</strong></p>
<p><strong>Technical Writer</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>May 2021</td>
<td><a href="#ptf">17</a>, <a href="#order-entry-details">35</a></td>
<td>Changes to 4.9. Added 5.3</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Nov 2016</td>
<td>all</td>
<td>Applied new OI&amp;T format and remediated for Section 508</td>
<td><p><mark>REDACTED</mark></p>
<p>EPMO/BAM</p></td>
</tr>
<tr class="odd">
<td>Aug 2016</td>
<td><a href="#pce">14</a></td>
<td>Added index for V Imm Contra/Refusal Events file (PX*1*215)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Feb 2016</td>
<td><a href="#pce">14</a>, <a href="#vitals">23</a>, <a href="#_LAB">26</a></td>
<td>Change to V Immunization index, per PX*1.0*210</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2014</td>
<td></td>
<td>Many updates per Developer review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Feb 2014</td>
<td><a href="#changes-to-reminder-indexes-made-by-the-clinical-reminders-icd-10-update-project">2</a></td>
<td>Overview of updates per the Reminders ICD-10 Update project</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Feb 2014</td>
<td><a href="#PROBLIST"><u>17</u></a></td>
<td>Change to Problem List index, per GMPL*2.0*44</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Feb 2014</td>
<td><a href="#ptf"><u>17</u></a></td>
<td>Change to Registration index, per DG*5.3*862</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2012</td>
<td></td>
<td>Corrected codes in Registration Index text</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Oct 2008</td>
<td><a href="#mental-health"><u>14</u></a></td>
<td>Updated MH Index</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Dec 2009</td>
<td><a href="#summary"><u>24</u></a></td>
<td>Update MH Index in Summary Table</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Dec 2004</td>
<td></td>
<td>Original release of Reminders Index (PXRM*1*12)</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
# Clinical Reminders Index Global


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [REVISION HISTORY](#revision-history)
- [Clinical Reminders Index Global](#clinical-reminders-index-global)
  - [Introduction](#introduction)
  - [Global Placement](#global-placement)
  - [Journaling](#journaling)
  - [Changes to Reminder Indexes made by the Clinical Reminders ICD-10 Update project](#changes-to-reminder-indexes-made-by-the-clinical-reminders-icd-10-update-project)
    - [Patches in the Clinical Reminders project build](#patches-in-the-clinical-reminders-project-build)
    - [DG\5.3\862](#dg53862)
    - [GMPL\2.0\44](#gmpl2044)
  - [Clinical Reminders Index Management](#clinical-reminders-index-management)
  - [PXRM INDEX BUILD Option](#pxrm-index-build-option)
    - [Error Messages](#error-messages)
  - [Inpatient Pharmacy](#inpatient-pharmacy)
  - [Outpatient Pharmacy](#outpatient-pharmacy)
- [Disable/Enable Reminder Evaluation](#disableenable-reminder-evaluation)
  - [Protocols](#protocols)
- [PXRM INDEX COUNT Option](#pxrm-index-count-option)
- [Index Details](#index-details)
  - [Inpatient Pharmacy](#inpatient-pharmacy-1)
  - [Non-VA Meds](#non-va-meds)
  - [Outpatient Pharmacy](#outpatient-pharmacy-1)
  - [Order Entry](#order-entry)
  - [Lab](#lab)
  - [Mental Health](#mental-health)
  - [PCE](#pce)
  - [Problem List](#problem-list)
  - [Radiology](#radiology)
  - [PTF](#ptf)
  - [Vitals](#vitals)
- [Cross-References](#cross-references)
  - [Using FileMan to obtain detailed Cross-Reference descriptions](#using-fileman-to-obtain-detailed-cross-reference-descriptions)
    - [Method 1, Inquire Option](#method-1-inquire-option)
    - [Method 2, Data Dictionary Utility](#method-2-data-dictionary-utility)
  - [LAB Details](#lab-details)
    - [Routines](#routines)
    - [Lab Indexes](#lab-indexes)
  - [Order Entry Details](#order-entry-details)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Reminders Index global has been designed to provide an index of clinical data, which supports rapid access to clinical data. It is used by Clinical Reminders v2.0, which evaluates reminders in 1/3 to 1/2 the time that v1.5 required. A large part of the speedup can be attributed to the Index, because it provides such an efficient way to find patient data. The Index is a resource that can be used by other packages or site-developed applications whenever they need to find patient data. Use of the Index is supported by subscription to ICR \#4290. This document describes the structure of the Index and how to use it, as well as how to populate it and manage it.

The basic structure of the index is:

^PXRMINDX(FILE NUMBER,”IP”,ITEM,DFN,DATE,DAS)

^PXRMINDX(FILE NUMBER,”PI”,DFN,ITEM,DATE,DAS)

Where “IP” stands for item and patient and “PI” for patient and item.

The “IP” index lets you find all patients with a particular item, while the “PI” index lets you find all items for a patient. DAS stands for DA string, similar to FileMan’s DA array. It is a semicolon-separated string that specifies the exact location in the source global where the data is stored. This can be as simple as the internal entry number (IEN) or can have a number of pieces (for example, a lab test result has four pieces).

Indexes with items that are coded values, such as ICD codes, vary from the basic structure, in order to support look-ups based on data such as primary diagnosis or principal procedure. Details are found in the sections describing each index.

## Global Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This global serves as an index for the clinical data in a number of packages, so it is independent of a particular package. When new data is entered into the globals being indexed, the Index will grow, so it needs to be placed where it has room to grow.

There is a utility for estimating the initial size of the Index. To run this utility at the programmer prompt, type D ESTTASK^PXRMISE. This will start a TaskMan job that estimates the initial size of the index for each global as well as the total size. The information will be delivered in a MailMan message sent to members of the mail group defined in file \#800. The estimated sizes will be given as a number of blocks which are 2K for Caché sites.

We recommend placing ^PXRMINDX in its own volume set. The initial size of the dataset should be based on the estimated size, plus leaving room for growth.

## Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Journaling of PXRMINDX is NOT required, because the index can be rebuilt, if necessary.

## Changes to Reminder Indexes made by the Clinical Reminders ICD-10 Update project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To support the introduction of ICD-10 codes into VistA, Clinical Reminders has taken a very general approach, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon package. In addition to adding ICD-10 codes, SNOMED CT codes are being added. With the release of CPRS 29, SNOMED CT codes can be collected by Problem List and Clinical Reminders will be able to search for them.

### Patches in the Clinical Reminders project build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PX\*1.0\*211 adds a new V-file named V STANDARD CODES that can store codes from any coding system supported by the Lexicon.

The sources of coded data that are indexed are Problem List, PTF, V CPT, V POV and V STANDARD CODES.

For these files, with some exceptions, the first two subscripts of the Index will become

^PXRMINDX(FILE NUMBER,CODING SYSTEM)

Where coding system is the standard three-character Source Abbreviation defined in file \#757.03. The exceptions apply to V CPT and V POV and are described in the PCE section.

### DG\*5.3\*862 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build updates the Clinical Reminders Index cross-references in the PTF file (#45) to accommodate ICD-10 diagnosis and procedure codes. It restructures the PTF portion of the Clinical Reminders Index to a generic format that can support all ICD coding systems. This format is:

^PXRMINDX(45,CODING SYSTEM,"INP",CODE,NODE,DFN,DATE,DAS)

^PXRMINDX(45,CODING SYSTEM,"PNI",DFN,NODE,CODE,DATE,DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer.

The post-install routine will start a background job to rebuild the file \#45 index in the new format.

### GMPL\*2.0\*44

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

^PXRMINDX(9000011,CODING SYSTEM,”ISPP”,CODE,STATUS,PRIORITY,DFN,DLM,DAS)

^PXRMINDX(9000011,CODING SYSTEM,”PSPI”,DFN,STATUS,PRIORITY,CODE,DLM,DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. The post-install routine will start a background job to rebuild the file \#9000011 index in the new format.

## Clinical Reminders Index Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option, PXRM INDEX MANAGEMENT, is a menu containing PXRM INDEX BUILD and PXRM INDEX COUNT.

The index building utility serves two purposes:

1.  It initially populates the indexes by indexing the existing data. It works its way through the entire global, putting entries in the index for each piece of unique patient data it finds.
2.  If the index ever gets corrupted or destroyed, the utility can be used to rebuild the index. Therefore, there is no need to journal the index, since it can be recreated from the original data at any time.

When the index utility finishes indexing a particular global, it sets the following three nodes:

^PXRMINDX(FILE NUMBER,”GLOBAL NAME”)=\$\$GET1^DID(FILE NUMBER,””,””,”GLOBAL NAME”)

^PXRMINDX(FILE NUMBER,”BUILT BY”)=DUZ

^PXRMINDX(FILE NUMBER,”DATE BUILT”)=\$\$NOW^XLFDT

In addition to providing information about who built the index and when it got populated, these nodes can be used to determine when the index is complete and ready for use.

When data is added, edited, or deleted, the indexes are kept current using new-style MUMPS cross-references. These cross-references call APIs that set and kill the index entries.

## PXRM INDEX BUILD Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index build utility can be accessed through the option PXRM INDEX MANAGEMENT or directly via PXRM INDEX BUILD.

Select OPTION NAME: PXRM INDEX BUILD PXRM INDEX BUILD run routine

PXRM INDEX BUILD

Which indexes do you want to (re)build?

1 - LABORATORY TEST (CH, Anatomic Path, Micro)

2 - MENTAL HEALTH

3 - MENTAL HEALTH (MHA3)

4 - ORDER

5 - PTF

6 - PHARMACY PATIENT

7 - PRESCRIPTION

8 - PROBLEM LIST

9 - RADIOLOGY

10 - V CPT

11 - V EXAM

12 - V HEALTH FACTORS

13 - V IMMUNIZATION

14 - V PATIENT ED

15 - V POV

16 - V SKIN TEST

17 - V STANDARD CODES

18 - VITAL MEASUREMENT

Enter your list: (1-18):

It can be used to build or rebuild the indexes for each of the globals, in any combination you want. You can run the build interactively or as a tasked job. Rebuilding an index is not something you would normally want to do. If problems are found with some entries in an index it is better to deal with them on an individual basis. Rebuilding an entire index is a last resort when there is no other way to repair or restore it.

After selecting the globals to be indexed, you will be given the choice of submitting a tasked job or running it interactively. In either case, when the index build completes, members of the mail group defined in file \#800 will be sent a MailMan message that looks something like:

Subj: Index for global AUPNVPED successfully built \[#12184\]

10/03/17@10:25 5 lines

From: POSTMASTER (Sender: DOE,JOHN) In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------

Build of Clinical Reminders index for global AUPNVPED completed.

Build finished at 10/03/2017@10:25:27

288 entries were created.

Elapsed time: 1 secs

0 errors were encountered.

> **NOTE:** If the person who builds the indexes is not a member of the mail group, the messages will not be delivered to the members of the mail group, unless it is a public mail group.

For large globals, the build time can be many hours, so you may want to schedule these builds for overnight or weekends when the system is not under heavy use. The indexes for smaller globals, which require few block splits, can be built quickly (a few minutes), so you have wider latitude in when to build those.

### Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If any entries couldn’t be indexed, the completion message will look something like:

Subj: Index for global PS(55 successfully built \[#12187\] 10/03/17@10:30 6 lines

From: POSTMASTER (Sender: DOE,JOHN) In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------

Build of Clinical Reminders index for global PS(55 completed.

Build finished at 10/03/2017@10:30:07

6416 entries were created.

Elapsed time: 13 secs

136 errors were encountered.

Another MailMan message contains the error information for up to the last N errors. The error information starts with the most recent entry in the global that has an error and progressively works back toward older entries. The number of errors displayed, N, is a site-configurable parameter. The parameter is stored in the CLINICAL REMINDERS PARAMETERS file, \#800, in the field MAXIMUM NUMBER OF INDEX ERRORS, field \#15 of file \#800, Clinical Reminder Parameters. The default value is 200. If you wish to change this, you can use the ENTER OR EDIT FILE ENTRIES FileMan option. If you find a substantial number of errors, it is likely there is a systematic problem, so after determining the cause and solution for the first few errors, you can probably apply the same corrective action to the bulk of them.

The message has the format: global, entry identification, and error message. The error message describes the problem – for example, missing or invalid data. Here is a sample of errors you might see for file \#55:

Subj: CLINICAL REMINDER INDEX BUILD ERROR(S) \[#14895\] 11/19/17@11:50 136 lines

From: POSTMASTER (Sender: DOE,JOHN) In 'IN' basket. Page 1

------------------------------------------------------------------------------

GLOBAL: PS(55 ENTRY: DFN=1 D1=33 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=1 D1=34 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=1 D1=35 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=1 D1=36 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=2 D1=1 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=3 D1=1719 Unit Dose missing stop date

GLOBAL: PS(55 ENTRY: DFN=3 D1=1 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=3 D1=2 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=3 D1=3 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=4 D1=2 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=4 D1=8 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=6 D1=5 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=6 D1=7 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=6 D1=590 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=8 D1=1 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=9 D1=2 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=9 D1=7 D2=1 IV additive missing drug

GLOBAL: PS(55 ENTRY: DFN=10 D1=31 IV missing stop date

GLOBAL: PS(55 ENTRY: DFN=10 D1=32 IV missing stop date

The entry information identifies the exact entry in the global that could not be indexed.

If we examine the last line, it tells us that for ^PS(55,10,”IV”,32,0), there is no stop date, so it can’t be indexed. If you are not familiar with the structure of the global being indexed, it will be helpful to have a data dictionary listing on hand to help you interpret the entry identification information.

Entries that are not indexable will never be found by any application that uses the index to find data. Each site should make a decision concerning what they want to do about non-indexable entries.

## Inpatient Pharmacy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have reported that the bulk of the errors are the same type: missing start date or missing patient.

GLOBAL: ^PS(55, ENTRY: DFN=994 D1=1545755 Unit Dose missing start date

Global ^PS(55,994,,1545755

PS(55,994,,1545755

^PS(55,994,5,1545755,0) = ^^^^^^^^E

^PS(55,994,5,1545755,9,0) = ^55.09D^1^1

GLOBAL: ^PS(55, ENTRY: DFN=388 D1=1804771 Unit Dose missing start date

Global ^PS(55,388,,1804771

PS(55,388,,1804771

^PS(55,388,5,1804771,0) = ^^^^^^^^E

^PS(55,388,5,1804771,9,0) = ^55.09D^1^1

GLOBAL: ^PS(55, ENTRY: DFN=1096 D1=1819001 Unit Dose missing start date

Global ^PS(55,1096,,1819001

PS(55,1096,,1819001

^PS(55,1096,5,1819001,0) = ^^^^^^^^E

^PS(55,1096,5,1819001,9,0) = ^55.09D^1^1

Global ^

GLOBAL: ^PS(55, ENTRY: DFN=1245 D1=16 IV missing start date

Global ^PS(55,1245,,16

PS(55,1245,,16

^PS(55,1245,"IV",16,0) = 16^^^P^^^^INFUSE VIA MINIPUMP^NOW^^1000^^^^0^^S X=PSSTATUS

^PS(55,1245,"IV",16,1) = ONE TIME

^PS(55,1245,"IV",16,2) = 2861123.1008^1^IBG

^PS(55,1245,"IV",16,3) = PROTECT FROM LIGHT/DO NOT REFRIGERATE

^PS(55,1245,"IV",16,6) = 67^20 MG

^PS(55,1245,"IV",16,"A",0) = ^55.04A^1^1

^PS(55,1245,"IV",16,"A",1,0) = 1^D^IBG^COMPUTER DOWN^2861123.1045

^PS(55,1245,"IV",16,"A",2,1,0) = ^55.15^1^1

^PS(55,1245,"IV",16,"A",2,1,1,0) = STATUS^DISCONTINUED^

^PS(55,1245,"IV",16,"AD",0) = ^55.02PA^1^1

^PS(55,1245,"IV",16,"AD",1,0) = 108^20 MG

^PS(55,1245,"IV",16,"SOL",0) = ^55.11IPA^1^1

^PS(55,1245,"IV",16,"SOL",1,0) = 1^10 ML

## Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have reported that the bulk of the errors are the same type: missing drug or missing patient.

GLOBAL: ^PSRX( ENTRY: 200167 missing drug^PSRX(200167,0)=" ^154^^^^^^^^^^^2881118^^^^^^1"

2)="2881118^2881127^^^^^^^1^ "

3)=2881127

"POE")=1

"SIG")="^0"

"STA")=11

"TYPE")=0

GLOBAL: ^PSRX( ENTRY: 5287379 missing DFN

Global ^PSRX(5287379

PSRX(5287379

^PSRX(5287379,0) = 5285540

^PSRX(5287379,2) = ^^^^^^^^^^

^PSRX(5287379,3) =

^PSRX(5287379,"POE") = 1

GLOBAL: ^PSRX( ENTRY: 5288355 missing DFN

Global ^PSRX(5288355

PSRX(5288355

^PSRX(5288355,0) = 5285807

^PSRX(5288355,2) = ^^^^^^^^^^

^PSRX(5288355,3) =

^PSRX(5288355,"POE") = 1

# Disable/Enable Reminder Evaluation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option PXRM INDEX BUILD provides the ability to rebuild selected portions of the Clinical Reminders Index. While an index is rebuilding, any reminder that uses the data from that index cannot be correctly evaluated – it will have the status of CNBD (cannot be determined). In the past, a MailMan message was sent to the Clinical Reminders mail group every time a reminder could not be evaluated because an index was rebuilding. Now, when an index is going to be rebuilt, reminder evaluation will be automatically disabled, meaning that any attempt to evaluate a reminder will result in an immediate return of a CNBD status. The Clinical Maintenance display will include text letting the user know that reminder evaluation is disabled and the reason(s). When the index has finished rebuilding, evaluation will be automatically enabled.

The option PXRM DISABLE/ENABLE EVALUATION provides a manual disable/enable function. If for some reason, reminder evaluation needs to be disabled, it can be done through this option. This option should be given to a very limited number of people and can only be used by holders of the PXRM MANAGER key. When the issue that required disabling evaluation has been handled, reminder evaluation can be enabled again using this same option. Note that this option can be used to enable evaluation even if it was not disabled using this option. For example, if reminder evaluation was automatically disabled for an index rebuild, this option could be used to enable evaluation even though the index is still rebuilding. If that is done, the MailMan messages will start being sent again.

When reminder evaluation is disabled, the following options and protocols will be put out of order.

Options:

PXRM DEF INTEGRITY CHECK ALL

PXRM DEF INTEGRITY CHECK ONE

PXRM ORDER CHECK TESTER

PXRM REMINDERS DUE

PXRM REMINDERS DUE (USER)

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PXRM PATIENT LIST CREATE

PXRM EXTRACT MANUAL TRANSMISSION

When reminder evaluation is again enabled, these options and protocols will be put back in order.

Anytime reminder evaluation is disabled, a message with the subject “REMINDER EVALUATION DISABLED” will be sent to the Clinical Reminders mail group. The message will give the date and time that evaluation was disabled, list the reasons for disabling evaluation, and a search will be made for any Clinical Reminders TaskMan jobs that could be affected. There will be a list of those that are found; it will include the job description, the status (pending or running), and the task number. The results of any jobs that are already running will be unreliable and should be discarded. If possible, these jobs should be stopped, so that they don’t waste system resources. None of the pending jobs should be allowed to start until evaluation is enabled again.

When evaluation is enabled, a message with the subject “REMINDER EVALUATION ENABLED” will be sent to the Clinical Reminders mail group. It will contain the date and time evaluation was disabled and when it was enabled. This gives you the exact period of when evaluation was disabled.

Here are examples of disable and enable messages:

MailMan message for CRMANAGER,TWO

Printed at CPRS30.FO-SLC.MED.VA.GOV 04/16/17@10:32

Subj: REMINDER EVALUATION DISABLED \[#122941\] 04/16/14@10:30 58 lines

From: POSTMASTER (Sender: CRMANAGER, ONE) In 'IN' basket. Page 1

------------------------------------------------------------------------------

Reminder evaluation was disabled on Apr 16, 2017@10:30:42.

Because of this, the following TaskMan jobs can produce erroneous results.

Pending jobs should not be allowed to start until evaluation is enabled.

The results of running jobs should be discarded and if possible, running jobs

should be stopped.

Reason: index rebuild for file \#45.

Reminders Due Report Jobs

Task number - 316820

Status - Active: Running

Time - Feb 08, 2012@12:40:28

User - CRCOORDINATOR, TWO

Reminder Patient List Jobs

Task number - 1980022

Status - Active: Running

Time - Apr 16, 2014@08:00

User - TASKMAN,PROXY USER

Task number - 1980207

Status - Active: Pending

Time - Apr 17, 2014@08:00

User - TASKMAN,PROXY USER

Reminder Extract Jobs

Task number - 342256

Status - Active: Pending

Time - Mar 06, 2012@20:04:25

User - CRCOORDINATOR, SIX

Task number - 1867565

Status - Active: Pending

Time - May 17, 2013@16:44:13

User - CRCOORDINATOR, SIX

Task number - 1902474

Status - Active: Pending

Time - Jul 17, 2013@17:16:30

User - CRCOORDINATOR,TEN

Task number - 1945932

Status - Active: Pending

Time - Oct 22, 2013@12:37:23

User - CRCOORDINATOR, THIRTY

Task number - 1946204

Status - Active: Pending

Time - Oct 23, 2013@12:37:35

User - CRCOORDINATOR, TWO

Task number - 1966964

Status - Active: Pending

Time - Feb 05, 2014@07:54:39

User - CRCOORDINATOR,THREE

Enter message action (in IN basket): Ignore//

Subj: REMINDER EVALUATION ENABLED \[#122942\] 04/16/17@10:30 2 lines

From: POSTMASTER (Sender: CRMANAGER, ONE) In 'IN' basket. Page 1

------------------------------------------------------------------------------

Reminder evaluation was enabled on Apr 16, 2017@10:30:49.

It was disabled on Apr 16, 2017@10:30:42.

Enter message action (in IN basket): Ignore//

# PXRM INDEX COUNT Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index count utility can be accessed through the option PXRM INDEX MANAGEMENT or directly via PXRM INDEX COUNT. This utility provides a count by year of the entries in the index. This will let sites see how their data is distributed on a yearly basis.

The selection for the count utility is identical to the build utility and the results are sent in a MailMan message just like the results of the build utility.

# Index Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Inpatient Pharmacy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 55, Pharmacy Patient. The structure is:

^PXRMINDX(55,”IP”,DRUG,DFN,START,STOP,DAS)

^PXRMINDX(55,”PI”,DFN,DRUG,START,STOP,DAS)

Where DRUG is a pointer to the Drug file (#50), START is the start date, and STOP is the stop date. The API to retrieve the associated data is OEL^PSJPXRM1(DAS,.DATA).

It is documented in ICR \#3836.

## Non-VA Meds 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on the non-VA med multiple of file \#55, Pharmacy Patient. The structure is:

^PXRMINDX(“55NVA”,”IP”,POI,DFN,START,STOP,DAS)

^PXRMINDX(“55NVA”,”PI”,DFN,POI,START,STOP,DAS)

Where POI is a pointer to the Pharmacy Orderable Item file. START is the start date, if it exists; otherwise it is the documented date. STOP is the discontinued date if it exists; otherwise is “U”\_D0. If STOP has the form “U”\_D0 it should be interpreted to mean that no discontinued date exists so the patient is currently taking the non-VA med.

The API to retrieve the associated data is NVA^PSOPXRM1(DAS,.DATA). It is documented in ICR 3793.

## Outpatient Pharmacy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file \#52, Prescription file. The structure is:

^PXRMINDX(52,”IP”,DRUG,DFN,START,STOP,DAS)

^PXRMINDX(52,”PI”,DFN,DRUG,START,STOP,DAS)

Where DRUG is a pointer to Drug file, START is the starting date (RELEASE DATE) and STOP is the stop date ( RELEASE DATE + DAYS SUPPLY). The API to retrieve the associated data is PSRX^PSOPXRM1(DAS,.DATA).

It is documented in ICR \#3793.

## Order Entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 100, Order file. The structure is:

^PXRMINDX(100,”IP”,OI,DFN,START,STOP,DAS)

^PXRMINDX(100,”PI”,DFN,OI,START,STOP,DAS)

Where OI is a pointer to the Orderable Items file, START is the START DATE, and STOP is the STOP DATE. The API to retrieve the associated data is EN^ORX8(DA). Note that DA is the first piece of DAS and the data is returned in the array ORUPCHK.

The API is documented in ICR \#871.

## Lab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 63, Lab Data. The structure is:

Chemistry, Hematology, other Lab Tests

^PXRMINDX(63,”IP”,ITEM,DFN,DATE,DAS)

^PXRMINDX(63,”PI”,DFN,ITEM,DATE,DAS)

Microbiology and Anatomic Path data have an additional index

^PXRMINDX(63,”PDI”,DFN,DATE,ITEM,DAS)

Where DATE is the Date/Time of collection. The structure of ITEM depends on the type of lab data.

For Chemistry, Hematology, and other lab tests, ITEM is numeric and a pointer to the Laboratory Test file.

For Microbiology, ITEM is of the format

"M;\[S T O A M\];#".

where the middle section can be one of:

S is specimen (# is a pointer to the Topography \[SNOMED\] file)

T is test (# is a pointer to the Laboratory Test file)

O is organism (# is a pointer to the Etiology Field \[SNOMED\] file)

A is antibiotic (# is a pointer to the Antimicrobial Susceptibility file)

M is a TB drug (# is the field number of the TB drug - ^DD(63.39,).

For Anatomic Pathology, ITEM is of the format

"A;\[S T O D M E F P I\];#".

where the middle section can be one of:

S is specimen (# is 1.free text value)

T is test (# is a pointer to the Laboratory Test file)

O is organ/tissue (# is a pointer to the Topography \[SNOMED\] file)

D is disease (# is a pointer to Disease Field \[SNOMED\] file)

M is morphology (# is a pointer to the Morphology Field \[SNOMED\] file)

E is etiology (# is a pointer to the Etiology Field \[SNOMED\] file)

F is function (# is a pointer to the Function \[SNOMED\] file

P is procedure (# is a pointer to the Procedure \[SNOMED\] file)

I is ICD (# is a pointer to the ICD DIAGNOSIS file)

Microbiology and Anatomic Pathology data are stored in a complex hierarchy. The ITEM is therefore a compound expression. This allows single elements of data to be easily found. The DAS also depends on the type of lab data. A chemistry test result has four semicolon pieces. Microbiology and Anatomic Pathology can be more complex and have a much more nested structure.

The API to retrieve the associated data is LRPXRM^LRPXAPI(.DATA,DAS,ITEM). This information should be reviewed in the context of other data associated with the specimen. The API is documented in ICR \#4245. The Lab package has other APIs that use these indexes.

## Mental Health 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 601.84, MH Administrations. The structure is:

^PXRMINDX(601.84,”IP”,INS,DFN,DATE,DAS)

^PXRMINDX(601.84,”PI”,DFN,INS,DATE,DAS)

Where INS is a pointer to the MH Instrument file \#601. The API to retrieve the associated data is D ENDAS71^YTQPXRM6(.DATA,DAS).

The API is documented in ICR \#5043.

## PCE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are indexes on all of the V files, with the exception of V Provider and V Treatment. There are two types of indexes for the V files – one for coded values and one for the non-coded values. There is a third type of index for the V Imm Contra/Refusal Events file.

The non-coded values are stored in the following V files:

| V FILE           | FILE NUMBER |
|------------------|-------------|
| V EXAM           | 9000010.13  |
| V HEALTH FACTORS | 9000010.23  |
| V IMMUNIZATION   | 9000010.11  |
| V PATIENT ED     | 9000010.16  |
| V SKIN TEST      | 9000010.12  |

The structure of the index for the non-coded values is:

^PXRMINDX(FILE NUMBER,”IP”,ITEM,DFN,DATE,DAS)

^PXRMINDX(FILE NUMBER,”PI”,DFN,ITEM,DATE,DAS)

Where item is the .01 of the V file (for example, a pointer to the Education Topic file or Health Factor file), and DATE is the Event Date and Time, if it is populated, otherwise it is the Visit/Admit Date&Time.

The V Immunization file has an additional index:

^PXRMINDX(9000010.11,"CVX","IP",CVX_CODE,DFN,DATE,DAS)

^PXRMINDX(9000010.11,"CVX","PI",DFN,CVX_CODE,DATE,DAS)

CVX is the Center for Disease Control’s vaccine administered code.

> **NOTE:** The “ACR” cross-reference on the Immunization file updates the ^PXRMINDX(9000010.11,"CVX") index when an immunization’s CVX code is changed.

Coded values are stored in the following V files:

| V FILE           | FILE NUMBER | CODE TYPE         |
|------------------|-------------|-------------------|
| V CPT            | 9000010.18  | CPT-4             |
| V POV            | 9000010.07  | ICD diagnosis     |
| V STANDARD CODES | 9000010.71  | Any standard code |

Because of the large number of entries, the existing structure of the Index for ICD-9 diagnosis and CPT-4 codes will be left as is:

^PXRMINDX(FILE NUMBER,”IPP”,CODEP,TYPE,DFN,DATE,DAS)

^PXRMINDX(FILE NUMBER,”PPI”,DFN,TYPE,CODEP,DATE,DAS)

Where CODEP is a pointer to the coded value, TYPE is primary procedure for V CPT and primary/secondary for V POV. DATE is the Visit Date.

Starting with the ICD-10 update the structure of the Index will become:

^PXRMINDX(FILE NUMBER,CODING SYSTEM,”IPP”CODE,TYPE,DFN,DATE,DAS)

^PXRMINDX(FILE NUMBER,CODING SYSTEM,”PPI”,DFN,TYPE,CODE,DATE,DAS)

Where CODING SYSTEM is the three-character Source Abbreviation from file \#757.03.

For example, the structure of the V POV Index for ICD-10 diagnosis codes is:

^PXRMINDX(9000010.07,”10D”,”IPP”,CODE,TYPE,DFN,DATE,DAS)

^PXRMINDX(9000010.07,”10D”,”PPI”,DFN,TYPE,CODE,DATE,DAS)

Where CODE is the ICD-10 the code.

The V Imm Contra/Refusal Events is stored in the following V file:

| V FILE                      | FILE NUMBER |
|-----------------------------|-------------|
| V IMM CONTRA/REFUSAL EVENTS | 9000010.707 |

The structure of the index is:

PXRMINDX(9000010.707,"PIC",DFN,IMM,CONTRA/REFUSAL,START,STOP,DAS)

PXRMINDX(9000010.707,"PCI",DFN,CONTRA/REFUSAL,IMM,START,STOP,DAS)

PXRMINDX(9000010.707,"ICP",IMM,CONTRA/REFUSAL,DFN,START,STOP,DAS)

PXRMINDX(9000010.707,"CIP",CONTRA/REFUSAL,IMM,DFN,START,STOP,DAS)

Where IMM is a pointer to the Immunization file; Contra/Refusal is a variable pointer to the Imm Contraindication Reasons (#920.4) or Imm Refusal Reasons (#920.5) files; START is the Event Date and Time, or if Event Date and Time is not populated, the Visit Date/Time will be used instead; STOP is the Warn Until Date, or if Warn Until Date is not populated, 9999999 will be used instead.

The APIs for retrieving the associated date are in routine PXPXRM. There is an entry point for each V file; these are listed in the following table. The APIs are documented in ICR \#4250.

| V FILE                      | PXPXRM ENTRY POINT |
|-----------------------------|--------------------|
| V CPT                       | VCPT(DAS,.DATA)    |
| V EXAM                      | VXAM(DAS,.DATA)    |
| V HEALTH FACTORS            | VHF(DAS,.DATA)     |
| V IMMUNIZATION              | VIMM(DAS,.DATA)    |
| V IMM CONTRA/REFUSAL EVENTS | VICR(DAS,.DATA)    |
| V PATIENT ED                | VPEDU(DAS,.DATA)   |
| V POV                       | VPOV(DAS,.DATA)    |
| V STANDARD CODES            | VSCDATA(DAS,.DATA) |
| V SKIN TEST                 | VSKIN(DAS,.DATA)   |

## Problem List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PROBLIST" class="anchor"></span>The structure of the index is:

^PXRMINDX(9000011,CODING SYSTEM,”ISPP”,CODE,STATUS,PRIORITY,DFN,DLM,DAS)

^PXRMINDX(9000011,CODING SYSTEM,”PSPI”,DFN,STATUS,PRIORITY,CODE,DLM,DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. STATUS is the status of the problem, either active (“A”) or inactive (“I”). PRIORITY can be acute (“A”), chronic (“C”), or null, in which case a “U” is stored. DLM is the Date Last Modified. This structure lets you quickly do things like find active problems whose status is acute.

The API to retrieve the associated data is PROBDATA^GMPLPXRM, it is documented in ICR \#5881.

## Radiology 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 70, Rad/Nuc Med Patient. The structure is:

^PXRMINDX(70,”IP”,PROC,DFN,DATE,DAS)

^PXRMINDX(70,”PI”,DFN,PROC,DATE,DAS)

Where PROC is a pointer to the Rad/Nuc Med Procedures file. The API to retrieve the associated data is EN1^RAPXRM(DAS,.DATA).

The API is documented in ICR \#3731.

## PTF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The structure of the index is:

^PXRMINDX(45,CODING SYSTEM,"INP",CODE,NAME,DFN,DATE,DAS)

^PXRMINDX(45,CODING SYSTEM,"PNI",DFN,NAME,CODE,DATE,DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. NAME is the name of the field where the code is stored.

ICD codes are stored in a number of fields in PTF so the storage node information (NODE) is included in the Index to allow quick searching and retrieval of specific nodes. The following tables summarize the fields that are indexed and their node names.

| Field Number | Field Name                    | Name    |
|--------------|-------------------------------|---------|
| 79           | PRINICIPAL DIAGNOSIS          | DXLS    |
| 80           | PRINICIPAL DIAGNOSIS pre 1986 | PDX     |
| 79.16        | SECONDARY DIAGNOSIS 1         | D SD1   |
| 79.17        | SECONDARY DIAGNOSIS 2         | D SD2   |
| 79.18        | SECONDARY DIAGNOSIS 3         | D SD3   |
| 79.19        | SECONDARY DIAGNOSIS 4         | D SD4   |
| 79.201       | SECONDARY DIAGNOSIS 5         | D SD5   |
| 79.21        | SECONDARY DIAGNOSIS 6         | D SD6   |
| 79.22        | SECONDARY DIAGNOSIS 7         | D SD7   |
| 79.23        | SECONDARY DIAGNOSIS 8         | D SD8   |
| 79.24        | SECONDARY DIAGNOSIS 9         | D SD9   |
| 79.241       | SECONDARY DIAGNOSIS 10        | D SD10  |
| 79.242       | SECONDARY DIAGNOSIS 11        | D SD11  |
| 79.243       | SECONDARY DIAGNOSIS 12        | D SD12  |
| 79.244       | SECONDARY DIAGNOSIS 13        | D SD13  |
| 79.245       | SECONDARY DIAGNOSIS 14        | D SD14  |
| 79.246       | SECONDARY DIAGNOSIS 15        | D SD15  |
| 79.247       | SECONDARY DIAGNOSIS 16        | D SD16  |
| 79.248       | SECONDARY DIAGNOSIS 17        | D SD17  |
| 79.249       | SECONDARY DIAGNOSIS 18        | D SD18  |
| 79.2491      | SECONDARY DIAGNOSIS 19        | D SD19  |
| 79.24911     | SECONDARY DIAGNOSIS 20        | D SD20  |
| 79.24912     | SECONDARY DIAGNOSIS 21        | D SD21  |
| 79.24913     | SECONDARY DIAGNOSIS 22        | D SD22  |
| 79.24914     | SECONDARY DIAGNOSIS 23        | D SD23  |
| 79.24915     | SECONDARY DIAGNOSIS 24        | D SD24  |
| 45.02,5      | ICD 1                         | M ICD1  |
| 45.02,6      | ICD 2                         | M ICD2  |
| 45.02,7      | ICD 3                         | M ICD3  |
| 45.02,8      | ICD 4                         | M ICD4  |
| 45.02,9      | ICD 5                         | M ICD5  |
| 45.02,11     | ICD 6                         | M ICD6  |
| 45.02,12     | ICD 7                         | M ICD7  |
| 45.02,13     | ICD 8                         | M ICD8  |
| 45.02,14     | ICD 9                         | M ICD9  |
| 45.02,15     | ICD 10                        | M ICD10 |
| 45.02,81.01  | ICD 11                        | M ICD11 |
| 45.02,81.02  | ICD 12                        | M ICD12 |
| 45.02,81.03  | ICD 13                        | M ICD13 |
| 45.02,81.04  | ICD 14                        | M ICD14 |
| 45.02,81.05  | ICD 15                        | M ICD15 |
| 45.02,81.06  | ICD 16                        | M ICD16 |
| 45.02,81.07  | ICD 17                        | M ICD17 |
| 45.02,81.08  | ICD 18                        | M ICD18 |
| 45.02,81.09  | ICD 19                        | M ICD19 |
| 45.02,81.1   | ICD 20                        | M ICD20 |
| 45.02,81.11  | ICD 21                        | M ICD21 |
| 45.02,81.2   | ICD 22                        | M ICD22 |
| 45.02,81.3   | ICD 23                        | M ICD23 |
| 45.02,81.4   | ICD 24                        | M ICD24 |
| 45.02,81.4   | ICD 25                        | M ICD25 |

ICD Operation/Procedure Codes

| Field Number | Field Name        | Node Name |
|--------------|-------------------|-----------|
| 45.05,4      | PROCEDURE CODE 1  | P1        |
| 45.05,5      | PROCEDURE CODE 2  | P2        |
| 45.05,6      | PROCEDURE CODE 3  | P3        |
| 45.05,7      | PROCEDURE CODE 4  | P4        |
| 45.05,8      | PROCEDURE CODE 5  | P5        |
| 45.05,9      | PROCEDURE CODE 6  | P6        |
| 45.05,10     | PROCEDURE CODE 7  | P7        |
| 45.05,11     | PROCEDURE CODE 8  | P8        |
| 45.05,12     | PROCEDURE CODE 9  | P9        |
| 45.05,13     | PROCEDURE CODE 10 | P10       |
| 45.05,14     | PROCEDURE CODE 11 | P11       |
| 45.05,15     | PROCEDURE CODE 12 | P12       |
| 45.05,16     | PROCEDURE CODE 13 | P13       |
| 45.05,17     | PROCEDURE CODE 14 | P14       |
| 45.05,18     | PROCEDURE CODE 15 | P15       |
| 45.05,19     | PROCEDURE CODE 16 | P16       |
| 45.05,20     | PROCEDURE CODE 17 | P17       |
| 45.05,21     | PROCEDURE CODE 18 | P18       |
| 45.05,22     | PROCEDURE CODE 19 | P19       |
| 45.05,23     | PROCEDURE CODE 20 | P20       |
| 45.05,24     | PROCEDURE CODE 21 | P21       |
| 45.05,25     | PROCEDURE CODE 22 | P22       |
| 45.05,26     | PROCEDURE CODE 23 | P23       |
| 45.05,27     | PROCEDURE CODE 24 | P24       |
| 45.05,28     | PROCEDURE CODE 25 | P25       |
| 45.01,8      | OPERATION CODE 1  | S1        |
| 45.01,9      | OPERATION CODE 2  | S2        |
| 45.01,10     | OPERATION CODE 3  | S3        |
| 45.01,11     | OPERATION CODE 4  | S4        |
| 45.01,12     | OPERATION CODE 5  | S5        |
| 45.01,13     | OPERATION CODE 6  | S6        |
| 45.01,14     | OPERATION CODE 7  | S7        |
| 45.01,15     | OPERATION CODE 8  | S8        |
| 45.01,16     | OPERATION CODE 9  | S9        |
| 45.01,17     | OPERATION CODE 10 | S10       |
| 45.01,18     | OPERATION CODE 11 | S11       |
| 45.01,19     | OPERATION CODE 12 | S12       |
| 45.01,20     | OPERATION CODE 13 | S13       |
| 45.01,21     | OPERATION CODE 14 | S14       |
| 45.01,22     | OPERATION CODE 15 | S15       |
| 45.01,23     | OPERATION CODE 16 | S16       |
| 45.01,24     | OPERATION CODE 17 | S17       |
| 45.01,25     | OPERATION CODE 18 | S18       |
| 45.01,26     | OPERATION CODE 19 | S19       |
| 45.01,27     | OPERATION CODE 20 | S20       |
| 45.01,28     | OPERATION CODE 21 | S21       |
| 45.01,29     | OPERATION CODE 22 | S22       |
| 45.01,30     | OPERATION CODE 23 | S23       |
| 45.01,31     | OPERATION CODE 24 | S24       |
| 45.01,32     | OPERATION CODE 25 | S25       |

In summary, there are 25 ICD diagnosis codes that can be associated with the discharge. The date for the discharge entries is the discharge date. Movement data is stored in subfile \#45.02 so there are 25 possible ICD diagnosis codes for each movement. The date is the MOVEMENT DATE field \#45.02, 10.

The names DXLS and PDX don’t bear any resemblance to the field names because these fields were renamed from DXLS to PRINCIPAL DIAGNOSIS and PDX to PRINICIPAL DIAGNOSIS pre 1986 after the Index was released.

The ICD procedure codes stored in subfiles \#45.05 and \#45.01 are indexed. The dates for these are the PROCEDURE DATE field \#45.05.01 and SURGERY/PROCEDURE DATE field \#45.01.01 respectively.

The ICD procedure codes stored in the 401P node (fields \#45.01, \#45.02, \#45.03, \#45.04, and \#45.050 are not indexed because they are valid only for admissions prior to 10/01/1987. This is documented in the User Manual – PTF Menu; located in the Admission Discharge Transfer (ADT) section of the VistA Documentation Library.

The ICD diagnosis codes stored in the CPT RECORD DATE/TIME multiple, field \#45.06,.04 are not indexed because CPT data is stored in file \#46 not file \#45.

The API to retrieve the data is PTF^DGPXRM(DAS,.DATA), it is documented in ICR \#4457.

## Vitals 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The index is on file 120.5, GMRV Vital Measurement. The structure is:

^PXRMINDX(120.5,”IP”,VITAL TYPE,DFN,DATE,DAS)

^PXRMINDX(120.5,”PI”,DFN,VITAL TYPE,DATE,DAS)

Where VITAL TYPE is a pointer to the GMRV Vital Type file \#120.51. Entries that are marked as “entered-in-error” are not indexed. The API to retrieve the associated data is EN^GMRVPXRM(.GMRVDATA,DAS).

The API is documented in ICR \#3647.

<span id="summary" class="anchor"></span>Summary of the detailed index structure given above

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 48%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>Package</th>
<th>Structure</th>
<th>Pointer</th>
<th>API</th>
<th>ICR #</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Inpatient Pharmacy</td>
<td><p>^PXRMINDX(55,”IP”,DRUG,DFN,START,<br />
STOP,DAS)</p>
<p>^PXRMINDX(55,”PI”,DFN,DRUG,START,<br />
STOP,DAS)</p></td>
<td>DRUG points to Drug file</td>
<td></td>
<td>3836</td>
</tr>
<tr class="even">
<td>Lab</td>
<td><p>^PXRMINDX(63,”IP”,ITEM,DFN,DATE,DAS)</p>
<p>^PXRMINDX(63,”PI”,DFN,ITEM,DATE,DAS)</p>
<p>^PXRMINDX(63,”PDI”,DFN,,DATE,ITEM,DAS)</p></td>
<td>ITEM is formatted depending on the type of data</td>
<td>LRPXRM^LRPXAPI(.DATA,DAS,ITEM)</td>
<td>4245</td>
</tr>
<tr class="odd">
<td>Mental Health</td>
<td><p>^PXRMINDX(601.84,”IP”,INS,DFN,DATE,DAS)</p>
<p>^PXRMINDX(601.84,”PI”,DFN,INS,DATE,DAS)</p>
<p>^PXRMINDX(601.2,”IP”,INS,DFN,DATE,DAS)</p>
<p>^PXRMINDX(601.2,”PI”,DFN,INS,DATE,DAS)</p></td>
<td>INS pointer to the MH Instrument file</td>
<td>ENDAS71^YTQPXRM6(.DATA,DAS)</td>
<td>5043</td>
</tr>
<tr class="even">
<td>Non-VA meds</td>
<td><p>^PXRMINDX(“55NVA”,”IP”,POI,DFN,START,STOP,DAS)</p>
<p>^PXRMINDX(“55NVA”,”PI”,DFN,POI,START,STOP,DAS)</p></td>
<td></td>
<td>NVA^PSOPXRM1(DAS,.DATA)</td>
<td>3793</td>
</tr>
<tr class="odd">
<td>Order Entry</td>
<td><p>^PXRMINDX(100,”IP”,OI,DFN,DATE,DAS)</p>
<p>^PXRMINDX(100,”PI”,DFN,OI,DATE,DAS)</p></td>
<td>OI points to the Orderable Items file</td>
<td>EN^ORX8(DAS)</td>
<td>871</td>
</tr>
<tr class="even">
<td>Outpatient Pharmacy</td>
<td><p>^PXRMINDX(52,”IP”,DRUG,DFN,START,STOP,DAS)</p>
<p>^PXRMINDX(52,”PI”,DFN,DRUG,START,STOP,DAS)</p></td>
<td>DRUG is a pointer to Drug file</td>
<td>PSRX^PSOPXRM1(DAS,.DATA)</td>
<td>3793</td>
</tr>
<tr class="odd">
<td><p>PCE</p>
<p>V FILES:</p>
<p>V CPT</p>
<p>V EXAM</p>
<p>V HEALTH</p>
<p>FACTORS</p>
<p>V IMMUNI-</p>
<p>ZATION</p>
<p>V PATIENT</p>
<p>ED</p>
<p>V POV</p>
<p>V SKIN TEST V IMM CONTRA/REFUSAL EVENTS</p>
<p>V STANDARD CODES</p></td>
<td><p>Non-coded values:</p>
<p>^PXRMINDX(FILE NUMBER,“IP”,ITEM,DFN, DATE,DAS)</p>
<p>^PXRMINDX(FILE NUMBER,“PI”,DFN,ITEM, DATE,DAS)</p>
<p>Coded values:</p>
<p>^PXRMINDX(FILE NUMBER,CODING SYSTEM,”IPP”,CODE,TYPE,DFN,DATE,DAS)</p>
<p>^PXRMINDX(FILE NUMBER,CODING SYSTEM,”PPI”,DFN,TYPE,CODE,DATE,DAS)</p>
<p>V Immunization:</p>
<p>^PXRMINDX(9000010.11,"CVX","IP",CVX_CODE,DFN,DATE,DAS)</p>
<p>^PXRMINDX(9000010.11,"CVX","PI",DFN,CVX_CODE,DATE,DAS)</p>
<p>V Imm Contra/Refusal Events:</p>
<p>^PXRMINDX(9000010.707,"PIC",DFN,IMM,CONTRA/REFUSAL,START,STOP,DAS)</p>
<p>^PXRMINDX(9000010.707,"PCI",DFN,CONTRA/REFUSAL,IMM,START,STOP,DAS) ^PXRMINDX(9000010.707,"ICP",IMM,CONTRA/REFUSAL,DFN,START,STOP,DAS)</p>
<p>^PXRMINDX(9000010.707,"CIP",CONTRA/REFUSAL,IMM,DFN,START,STOP,DAS)</p></td>
<td>Item is the .01 of the V file, for example a pointer to the Education Topic file or Health Factor file</td>
<td><p>PXPXRM ENTRY POINT</p>
<p>VCPT(DAS,.DATA)</p>
<p>VXAM(DAS,.DATA)</p>
<p>VHF(DAS,.DATA)</p>
<p>VIMM(DAS,.DATA)</p>
<p>VPEDU(DAS,.DATA)</p>
<p>VPOV(DAS,.DATA)</p>
<p>VSCDATA(DAS,.DATA)</p>
<p>VSKIN(DAS,.DATA)</p>
<p>VICR(DAS,.DATA)</p></td>
<td>4250</td>
</tr>
<tr class="even">
<td>Problem List</td>
<td><p>^PXRMINDX(9000011,CODING SYSTEM,”ISPP”,CODE,STATUS,PRIORITY,DFN,DLM,DAS)</p>
<p>^PXRMINDX(9000011,CODING SYSTEM,”PSPI”,DFN,STATUS,PRIORITY,CODE,DLM,DAS)</p></td>
<td>None</td>
<td>PROB^GMPLPXRM</td>
<td>5881</td>
</tr>
<tr class="odd">
<td>Radiology</td>
<td><p>^PXRMINDX(70,”IP”,PROC,DFN,DATE,DAS)</p>
<p>^PXRMINDX(70,”PI”,DFN,PROC,DATE,DAS)</p></td>
<td>PROC points to the Rad/Nuc Med Procedures file</td>
<td>EN1^RAPXRM(DAS,.DATA)</td>
<td>3731</td>
</tr>
<tr class="even">
<td>Registration</td>
<td><p>^PXRMINDX(45,CODING SYSTEM,”INP”,CODE,DFN,DATE,NODE,DAS)</p>
<p>^PXRMINDX(45,CODING SYSTEM,”PNI”,DFN,CODE,DATE,NODE,DAS)</p>
<p>NODE,DAS)</p></td>
<td>None</td>
<td>PTF^DGPXRM(DAS,.DATA)</td>
<td></td>
</tr>
<tr class="odd">
<td>Vitals</td>
<td><p>^PXRMINDX(120.5,”IP”,VITAL TYPE,DFN,DATE,DAS)</p>
<p>^PXRMINDX(120.5,”PI”,DFN,VITAL TYPE,DATE,DAS)</p></td>
<td>VITAL TYPE points to the GMRV Vital Type file</td>
<td>EN^GMRVPXRM(.GMRVDATA,DAS)</td>
<td>3647</td>
</tr>
</tbody>
</table>

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Index is kept current by using new-style FileMan cross-references that fire whenever data is added, edited, or deleted. A list of the cross-references follows.

> **NOTE:** Some of the packages do direct sets of the data into their globals instead of using FileMan. In those cases, the routines where the data is set or killed have been modified to call the package API that does the set or kill of the Index entry.<span id="_LAB" class="anchor"></span>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>File #</th>
<th>File Name</th>
<th>Sub-file #</th>
<th>Sub-file Name</th>
<th>Cross-reference</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>45</td>
<td>PTF</td>
<td></td>
<td></td>
<td><p>ACRDSD1</p>
<p>ACRDSD2</p>
<p>ACRDSD3</p>
<p>ACRDSD4</p>
<p>ACRDSD5</p>
<p>ACRDSD6</p>
<p>ACRDSD7</p>
<p>ACRDSD8</p>
<p>ACRDSD9</p>
<p>ACRDSD10</p>
<p>ACRDSD11</p>
<p>ACRDSD12</p>
<p>ACRDSD13</p>
<p>ACRDSD14</p>
<p>ACRDSD15</p>
<p>ACRDSD16</p>
<p>ACRDSD17</p>
<p>ACRDSD18</p>
<p>ACRDSD19</p>
<p>ACRDSD20</p>
<p>ACRDSD21</p>
<p>ACRDSD22</p>
<p>ACRDSD23</p>
<p>ACRDSD24</p>
<p>ACRDDXLS</p>
<p>ACRDPDX</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>45.01</td>
<td>401</td>
<td><p>ACRPS1</p>
<p>ACRPS2</p>
<p>ACRPS3</p>
<p>ACRPS4</p>
<p>ACRPS5</p>
<p>ACRPS6</p>
<p>ACRPS7</p>
<p>ACRPS8</p>
<p>ACRPS9</p>
<p>ACRPS10</p>
<p>ACRPS11</p>
<p>ACRPS12</p>
<p>ACRPS13</p>
<p>ACRPS14</p>
<p>ACRPS15</p>
<p>ACRPS16</p>
<p>ACRPS17</p>
<p>ACRPS18</p>
<p>ACRPS19</p>
<p>ACRPS20</p>
<p>ACRPS21</p>
<p>ACRPS22</p>
<p>ACRPS23</p>
<p>ACRPS24</p>
<p>ACRPS25</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>45.02</td>
<td>501</td>
<td><p>ACRDM1</p>
<p>ACRDM2</p>
<p>ACRDM3</p>
<p>ACRDM4</p>
<p>ACRDM5</p>
<p>ACRMD6</p>
<p>ACRMD7</p>
<p>ACRDM8</p>
<p>ACRDM9</p>
<p>ACRDM10</p>
<p>ACRDM11</p>
<p>ACRDM12</p>
<p>ACRDM13</p>
<p>ACRDM14</p>
<p>ACRDM15</p>
<p>ACRDM16</p>
<p>ACRDM17</p>
<p>ACRDM18</p>
<p>ACRDM19</p>
<p>ACRDM20</p>
<p>ACRDM21</p>
<p>ACRDM22</p>
<p>ACRDM23</p>
<p>ACRDM24</p>
<p>ACRDM25</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>45.05</td>
<td>601</td>
<td><p>ACRPP1</p>
<p>ACRPP2</p>
<p>ACRPP3</p>
<p>ACRPP4</p>
<p>ACRPP5</p>
<p>ACRPP6</p>
<p>ACRPP7</p>
<p>ACRPP8</p>
<p>ACRPP9</p>
<p>ACRPP10</p>
<p>ACRPP11</p>
<p>ACRPP12</p>
<p>ACRPP13</p>
<p>ACRPP14</p>
<p>ACRPP15</p>
<p>ACRPP16</p>
<p>ACRPP17</p>
<p>ACRPP18</p>
<p>ACRPP19</p>
<p>ACRPP20</p>
<p>ACRPP21</p>
<p>ACRPP22</p>
<p>ACRPP23</p>
<p>ACRPP24</p>
<p>ACRPP25</p></td>
</tr>
<tr class="odd">
<td>52</td>
<td>Prescription</td>
<td></td>
<td></td>
<td>ACRO</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>52.1</td>
<td>Refill</td>
<td>ACRR</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>52.2</td>
<td>Partial Date</td>
<td>ACRP</td>
</tr>
<tr class="even">
<td>55</td>
<td>Pharmacy Patient</td>
<td>55.01</td>
<td>IV</td>
<td>ACRIV</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>55.05</td>
<td>Non-VA meds</td>
<td>ACRNVA</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>55.06</td>
<td>Unit Dose</td>
<td>ACRUD</td>
</tr>
<tr class="odd">
<td>63</td>
<td>Lab Data</td>
<td></td>
<td></td>
<td>None</td>
</tr>
<tr class="even">
<td>70</td>
<td>Rad/Nuc Med Patient</td>
<td>70.03</td>
<td>Examinations</td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>100</td>
<td>Order</td>
<td></td>
<td></td>
<td>None</td>
</tr>
<tr class="even">
<td>120.5</td>
<td>GMRV Vital Measurement</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>601.2</td>
<td>Psych Instrument Patient</td>
<td>601.22</td>
<td>Date</td>
<td>ACR</td>
</tr>
<tr class="even">
<td>9000010.07</td>
<td>V POV</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>9000010.11</td>
<td>V IMMUNIZATION</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="even">
<td>9000010.12</td>
<td>V SKIN TEST</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>9000010.13</td>
<td>V EXAM</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="even">
<td>9000010.16</td>
<td>V PATIENT ED</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>9000010.18</td>
<td>V CPT</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="even">
<td>9000010.23</td>
<td>V HEALTH FACTORS</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>9000010.707</td>
<td>V IMM CONTRA/REFUSAL EVENTS</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="even">
<td>9000010.71</td>
<td>V STANDARD CODES</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
<tr class="odd">
<td>9000011</td>
<td>Problem</td>
<td></td>
<td></td>
<td>ACR01</td>
</tr>
<tr class="even">
<td>9999999.14</td>
<td>Immunization</td>
<td></td>
<td></td>
<td>ACR</td>
</tr>
</tbody>
</table>

## Using FileMan to obtain detailed Cross-Reference descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you wish a more detailed description of any of these cross-references, there are two different ways to get it – both use FileMan.

### Method 1, Inquire Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Inquire option on the Index file.

VA FileMan 22.0

Select OPTION: I INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: INDEX//

Select INDEX: ACR

1 ACR 120.5 Clinical Reminders cross-reference.

2 ACR 70 Clinical Reminders index.

3 ACR 9000010.18 Clinical Reminders index.

4 ACR 9000010.23 Clinical Reminders index.

5 ACR 9000010.11 Clinical Reminders index.

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

6 ACR 9000010.16 Clinical Reminders index.

7 ACR 9000010.07 Clinical Reminders index.

8 ACR 9000010.12 Clinical Reminders index.

9 ACR 9000010.13 Clinical Reminders index.

10 ACR 601.2 Clinical Reminders cross-reference.

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-10: 6 9000010.16 ACR Clinical Reminders index.

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record Number

(IEN)

NUMBER: 279 FILE: 9000010.16

NAME: ACR

SHORT DESCRIPTION: Clinical Reminders index.

TYPE: MUMPS EXECUTION: RECORD

ACTIVITY: IR ROOT TYPE: INDEX FILE

ROOT FILE: 9000010.16 USE: ACTION

DESCRIPTION: This cross-reference builds two indexes. One for finding all

patients with a particular education topic and one for finding all the

education topics a patient has. The indexes are stored in the Clinical

Reminders index global as:

^PXRMINDX(9000010.16,"IP",EDUCATION TOPIC,DFN,VISIT DATE,DAS) and

^PXRMINDX(9000010.16,"PI",DFN,EDUCATION TOPIC,VISIT DATE,DAS) respectively.

SET LOGIC: D SVFILE^PXPXRM(9000010.16,.X,.DA)

KILL LOGIC: D KVFILE^PXPXRM(9000010.16,.X,.DA)

KILL ENTIRE INDEX CODE: K ^PXRMINDX(9000010.16)

ORDER NUMBER: 1 TYPE OF VALUE: FIELD

FILE: 9000010.16 FIELD: .01

SUBSCRIPT NUMBER: 1 COLLATION: forwards

ORDER NUMBER: 2 TYPE OF VALUE: FIELD

FILE: 9000010.16 FIELD: .02

SUBSCRIPT NUMBER: 2 COLLATION: forwards

ORDER NUMBER: 3 TYPE OF VALUE: FIELD

### Method 2, Data Dictionary Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The other way to obtain detailed cross-reference descriptions is to use the Data Dictionary Utility. You can look at an entire file or a sub-file. In the example below, we look at a sub-file.

VA FileMan 22.0

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: PTF//

GO TO WHAT FILE: PTF//

Select SUB-FILE: 601

Select LISTING FORMAT: STANDARD// INDEXES ONLY

What type of cross-reference (Traditional or New)? Both// NEW

Which field: ALL//

DEVICE: ANYWHERE Right Margin: 80//

NEW-STYLE INDEX LIST -- FILE \#45 08/18/04 PAGE 1

------------------------------------------------------------------------------

Subfile \#45.05

New-Style Indexes:

ACRPP1 (#1287) RECORD MUMPS IR ACTION WHOLE FILE (#45)

Short Descr: Clinical Reminders Index for ICD procedure code lookup.

Description: This cross-reference builds two indexes, one for finding

all patients with a particular ICD procedure code and one

for finding all the ICD procedure codes a patient has.

The indexes are stored in the Clinical Reminders Index global as:

^PXRMINDX(45,CODESYS,"INP",CODE,NODE,DFN,DATE,DAS) and

^PXRMINDX(45,CODESYS,"PNI",DFN,NODE,CODE,DATE,DAS)

respectively. CODESYS is the standard three-character

abbreviation for the coding system. DATE is the

surgery/procedure date. NODE is P (for procedure) followed by procedure code number. For example, P1 means it was found on the P node and it was Procedure Code 1. For complete details, see the Clinical Reminders Index Technical Guide/Programmer's Manual.

Set Logic: D SPTFP^DGPTDDCR(.X,.DA,"P",1)

Kill Logic: D KPTFP^DGPTDDCR(.X,.DA,"P",1)

X(1): PROCEDURE DATE (45.05,.01) (Subscr 1) (forwards)

X(2): PROCEDURE CODE 1 (45.05,4) (Subscr 2) (forwards)

The rest of the cross-references on this sub-file have been left out for brevity.

If you know the field number or field name of a field used in the cross-reference, you can select a single cross-reference for display.

VA FileMan 22.0

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: PTF//

GO TO WHAT FILE: PTF//

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// INDEXES ONLY

What type of cross-reference (Traditional or New)? Both// NEW

Which field: ALL// SECONDARY DIAGNOSIS 1

DEVICE: ANYWHERE Right Margin: 80//

NEW-STYLE INDEX LIST -- FILE \#45, FIELD \#79.16 08/18/04 PAGE 1

------------------------------------------------------------------------------

ACRDSD1 (#1263) RECORD MUMPS IR ACTION

Short Descr: Clinical Reminders Index for ICD diagnosis code lookup.

Description: This cross-reference builds two indexes, one for finding all patients with a particular ICD diagnosis code and one for finding all the ICD diagnosis codes a patient has. The indexes are stored in the Clinical Reminders Index global as:

^PXRMINDX(45,CODESYS,"INP",CODE,NAME,DFN,DATE,DAS) and

^PXRMINDX(45,CODESYS,"PNI",DFN,NAME,CODE,DATE,DAS)

respectively. CODESYS is the standard three character abbreviation for the coding system. DATE is the discharge date. If it does not exist then the admission date is used.

NAME is the name of the field where the code is stored. An example is D SD1, where D SD signifies it is a discharge secondary diagnosis. If the TYPE OF RECORD is CENSUS then the entry is not indexed. For complete details, see the Clinical Reminders Index Technical Guide/Programmer's Manual.

Set Logic: D SPTFDD^DGPTDDCR(.X,.DA,"D SD1")

Kill Logic: D KPTFDD^DGPTDDCR(.X,.DA,"D SD1")

X(1): PATIENT (45,.01) (Subscr 1) (forwards)

X(2): ADMISSION DATE (45,2) (Subscr 2) (forwards)

X(3): TYPE OF RECORD (45,11) (Subscr 3) (forwards)

X(4): SECONDARY DIAGNOSIS 1 (45,79.16) (Subscr 4) (forwards)

X(5): DISCHARGE DATE (45,70)

## LAB Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lab results are stored in the Lab Data file \#63. This is a very hierarchical file with a strong dependence on the data dictionary.

The Lab package makes programming calls to update the ^PXRMINDX indexes. Chemistry-type data updates the indexes when results are verified. Anatomic Pathology and Microbiology update indexes when results are reported and/or released. Any changes to existing lab data update the indexes. All indexes are set using SLAB^LRPX and killed using KLAB^LRPX.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Chemistry-type data updates in a central routine.

LRVER3A Chemistry data are updated on verification and editing of verified data. All transactions go through LRVER3A, which stores the results and sets all the cross-references. This routine calls CHSET^LRPX.

LROC It is very rare but chemistry data may be purged during purging of old orders and accessions. This only happens on data that is corrupted and not reportable. This routine calls CHKILL^LRPX.

All Microbiology and Anatomic Pathology data are updated using the same routine, UPDATE^LRPXRM. Adding, editing, or deleting data invokes this call. Results are compared before and after editing. Any change will update the indexes. This routine is called from several routines:

LRAPDA

LRAPDSR

LRMIEDZ

LRMIEDZ2

LRMISTF1

LRMIV

LRMIV1

LRMIV2

### Lab Indexes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^PXRMINDX(63,"PI",DFN,ITEM,DATE,DAS)

This index is used for finding results of tests on a patient.

^PXRMINDX(63,"IP", ITEM,DFN,DATE,DAS)

This index is used for finding patients that have specific lab results.

^PXRMINDX(63,"PDI",DFN,DATE,ITEM,DAS)

This index is only used for Microbiology and Anatomic Pathology and is used for finding results on a patient for a specific time period. Chemistry-type data does not require this because the data are already stored in a similar format in the Lab Data file. Micro and AP data use a compound structure for ITEM (the lab test or other coded result) and the "PDI" index provides a faster path to the results. Also, AP data is broken into four sections: Autopsy, Cytology, Electron Microscopy, and Surgical Pathology. This index collates results by collection date/time regardless of the section; again, making retrieval faster.

## Order Entry Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many of the complex indexes used in Order Entry were created before new-style cross-references existed, therefore the cross-references that set and kill them had to be implemented as MUMPS cross-references. When the routines that set and kill the “AE” and “AR” indexes are called, all the data needed to set and kill the OR portion of the Clinical Reminders Index is available so it was natural to include the sets and kills of the Clinical Reminders Index.

AE MUMPS

Field: STOP DATE (100,22)

Description: ^OR(100,"AE",ORSTOP,ORIFN) Allows retrieval of orders by

expiration date; set only for orders that have not already

completed, expired, or been discontinued or canceled.

1)= D ES^ORDD100A

2)= D EK^ORDD100A

The “AE” cross-reference calls ES^ORDD100A (set) and EK^ORDD100A (kill) and these call SOR^ORPXRM and KOR^ORPXRM to perform the sets and kills of the Clinical Reminders Index.

AR MUMPS

Field: OBJECT OF ORDER (100,.02)

Description: ^OR(100,"AR",ORVP,9999999-ORRDT,ORIFN,ORDA) Allows

retrieval of orders by inverse date released.

1)= N ORDA S ORDA=0 F S ORDA=\$O(^OR(100,DA,8,ORDA)) Q:ORDA

'\>0 D RS^ORDD100(DA,ORDA,X)

2)= N ORDA S ORDA=0 F S ORDA=\$O(^OR(100,DA,8,ORDA)) Q:ORDA

'\>0 D RK^ORDD100(DA,ORDA,X)

The “AR” cross-reference calls RS^ORDD100 (set) and RK^ORDD100 (kill). RS^ORDD100 calls PXRMADD^ORDD100 which then calls SOR^ORPXRM. RK^ORDD100 calls PXRMKILL^ORDD100 which then calls KOR^ORPXRM.