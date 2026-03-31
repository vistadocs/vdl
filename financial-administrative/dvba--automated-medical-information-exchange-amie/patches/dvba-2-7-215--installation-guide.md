---
title: AMIE Version 2.7 Installation Guide 2019
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: DVBA
app_name: Automated Medical Information Exchange (AMIE)
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*215
group_key: "DVBA:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: Automated Medical Information Exchange (AMIE) V. 2.7Installation GuideNovember 2019
audience: 
keywords: 
  - filed
  - dvba
  - error
  - amie
  - message
  - exam
  - routine
  - local
  - after
  - follows
page_count: 0
word_count: 3577
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 2
revision_newest: 10/3/19
revision_oldest: 1/23/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/dvba_27_215_amie_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Medical_Info_Exchg_(AMIE)/dvba_27_215_amie_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=31"
---

![](amie-version-2-7-installation-guide-2019/001.png)

Automated Medical Information Exchange (AMIE) V. 2.7Installation GuideNovember 2019

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 1/23/09

| Date | Description (Patch \# if applic.)                                                           | Project Manager | Technical Writer |
|----------|-------------------------------------------------------------------------------------------------|---------------------|----------------------|
| 10/3/19  | Removed references to the DVBA C Purge 2507 option from pages 6 and 11 for patch DVBA\*2.7\*215 | REDACTED            | REDACTED             |
| 1/23/09  | Reformatted Manual                                                                              |                     | REDACTED             |
|          |                                                                                                 |                     |                      |

Table of Contents

# General Information


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Information](#general-information)
- [Installation Steps](#installation-steps)
- [Sample Installation](#sample-installation)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Post-Init Rerun](#post-init-rerun)
Before you attempt to install this version of AMIE, please be sure that your site is running the following minimum package versions.
VA FileMan V. 20.0
Kernel V. 7.1
MailMan V. 7.1
Kernel Tool Kit V. 7.2
Lab V. 5.0
PIMS V. 5.3
HINQ V. 4.0

# Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Step</u> <u>Description</u>

1\. Resource Requirements

> 2.4k per 2507 exam

> .65k per 7131 request

> Global Growth of Existing Files

> 2507 REQUEST file (#396.3) growth will be negligible.

> FORM 7131 file (#396) may average growth of .5k per record if your site is multidivisional and transfers four reports per request to different divisions.

> 2507 EXAM file (#396.4) will grow by .1k for each exam included on priority insufficient 2507 requests.

> Global Growth from New Files

> .2k per AMIE C&P Exam Tracking Record

> The 2507 INSUFFICIENT REASONS file (# 396.94) will require 2.6k and will not grow.

> There is only a minor demand on space that will be taken up as a result of the post-init process. No more than 10k will be used for new keywords and other data.

> Usage of space may increase depending on the purge parameter, Days to

> Keep 2507 History. See the technical manual for further details.

> The install on an ALPHA site takes approximately 10 minutes, with the post-init taking another 5-10 minutes. The loading of the global tape for an ALPHA takes about 20-30 minutes.

> The install on a MSM site takes approximately 10-15 minutes. The loading of the global tape for a MSM takes about 20 minutes.

2\. Data is being changed and added in both the AMIE files and KERNEL (MTLU) files. It is important to do a system backup before installing.

<u>Step</u> <u>Description</u>

3\. The init can be run with users on the system, but this would have a negative impact on system performance. It is recommended that this init be run after hours. All AMIE users must be off the system(s). This includes users from other VA medical centers and regional offices.

4\. Set the following options to OUT OF ORDER.

> Options

> DVBA MEDICAL ADM 7131 MENU

> DVBA REGIONAL OFFICE MENU

> DVBA C PROCESS MAIL MESSAGE

> DVBA C PHYSICIANS GUIDE

> These options will be brought in by the init in an OUT OF ORDER status.

> Any 2507 exam requests transferred in while the DVBA C PROCESS MAIL MESSAGE option is OUT OF ORDER will not be processed and will need to be retransferred from the remote site.

5\. Sign into the UCI where the package is to be loaded.

6\. Review queued jobs to avoid possible delays or conflicts. If there are any AMIE jobs queued, requeue them for later. Ensure that there are no AMIE users on the system.

7\. Delete all the AMIE DVBA\* and DVBC\* routines. This is to clean up all the unnecessary routines.

8\. Load AMIE V. 2.7 routines.

9\. Run the integ routine as follows: D ^DVBANTEG

<u>Step</u> <u>Description</u>

10\. In order to set up all environment variables, run the following. Insure that

your DUZ(0) equals "@" in order to initialize. Do not enter VA FileMan after ^XUP.

> \>K

> \>D ^XUP

> Setting up programmer environment

> Access Code:

> Terminal Type set to: C-VT100

> Select OPTION NAME:

> \>

11\. D ^DVBAINIT

Be sure to answer the questions carefully. See the sample installation for DVBAINIT responses. After running the init, a mail message will be sent to both the DUZ of the person who ran the init and to the Postmaster. This message will notify the site of any problems during the init. A description of the possible errors that may be reported is contained in Troubleshooting Guide of this Installation Guide.

12\. Delete the init routines DVBAI\*, DVBAON\*, DVBAO0\*.

13\. Move DVBA\* and DVBC\* routines to all systems.

14\. Before loading the new global containing the Physician's Guide, it is recommended you delete the data in the AMIE DOCUMENT file ^DVBP(396.91) and AMIE DOCUMENT TABLE OF CONTENTS file ^DVBP(396.92). D ^XUP followed by the entry point: DELETE ^DVBAPOPU.

<u>Step</u> <u>Description</u>

15\. Load AMIE global.

Use the appropriate vendor supplied utility to restore the global from distributed media (4mm data tape or TK-85 tape). This will load the AMIE DOCUMENT file ^DVBP(396.91) and AMIE DOCUMENT TABLE OF CONTENTS file ^DVBP(396.92). The following table describes the possible distribution sets for the AMIE global.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Media Type</strong></th>
<th><p><strong>Number</strong></p>
<p><strong>of Tapes</strong></p></th>
<th><strong>Format</strong></th>
<th><strong>Remarks</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4mm Data Tape</td>
<td>1</td>
<td>ASU</td>
<td>8192 bpi for MSM sites. Single tape contains two new files in one new global.</td>
</tr>
<tr class="even">
<td>TK-85 Tape</td>
<td>1</td>
<td>VAL5</td>
<td>2048 bpi for ALPHA sites. Single tape contains two new files in one new global.</td>
</tr>
</tbody>
</table>

16\. If applicable, reenable journaling and routine mapping.

17\. Check to make sure that all of the following options are queued through TaskMan. (Refer to the Implementation and Maintenance section of the Technical Manual, if necessary.)

DVBA REGIONAL TASK

DVBA AUTO FINALIZE 7131 TASK

DVBA 7132 TASKMAN

DVBA C PRINT NEW C&P REQ TM

DVBA GENERATE 21-DAY CERTIF

DVBA REGIONAL PURGING PROGRAM

DVBA C CHECK 2507 INTEGRITY TM

<u>Step</u> <u>Description</u>

18\. Remove OUT OF ORDER message from the options and protocol by running the following code.

> \>D OPEN^DVBAPOST

> DVBA MEDICAL ADM 7131 MENU Now in order!

> DVBA REGIONAL OFFICE MENU Now in order!

> DVBA C PROCESS MAIL MESSAGE Now in order!

> DVBA C PHYSICIANS GUIDE Now in order!

> DVBA C&P SCHD EVENT Now in order!

19\. The DVBA 7131 Non-Admitted Vets option on the DVBA REGIONAL OFFICE MENU is now obsolete. This option has been taken off of the AMIE menus. The site is able to remove it from any secondary menus and then delete it.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^DVBAINIT

This version (#2.7) of 'DVBAINIT' was created on 10-APR-1995

(at VASITE CAMPUS DEVELOPMENT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Environment check completed OK!

I AM GOING TO SET UP THE FOLLOWING FILES:

31 DISABILITY CONDITION (Partial Definition)

> **NOTE:** You already have the 'DISABILITY CONDITION' File.

396 FORM 7131

> **NOTE:** You already have the 'FORM 7131' File.

396.1 AMIE SITE PARAMETER

> **NOTE:** You already have the 'AMIE SITE PARAMETER' File.

396.2 AMIE REPORT

> **NOTE:** You already have the 'AMIE REPORT' File.

396.3 2507 REQUEST

> **NOTE:** You already have the '2507 REQUEST' File.

396.4 2507 EXAM

> **NOTE:** You already have the '2507 EXAM' File.

396.5 2507 CANCELLATION REASON (including data)

> **NOTE:** You already have the '2507 CANCELLATION REASON' File.

I will OVERWRITE your data with mine.

396.6 AMIE EXAM (including data)

> **NOTE:** You already have the 'AMIE EXAM' File.

I will OVERWRITE your data with mine.

396.7 2507 BODY SYSTEM (including data)

> **NOTE:** You already have the '2507 BODY SYSTEM' File.

I will OVERWRITE your data with mine.

396.91 AMIE DOCUMENT

> **NOTE:** You already have the 'AMIE DOCUMENT' File.

396.92 AMIE DOCUMENT TABLE OF CONTENTS

> **NOTE:** You already have the 'AMIE DOCUMENT TABLE OF CONTENTS' File.

396.93 EXAM EXCEPTIONS

> **NOTE:** You already have the 'EXAM EXCEPTIONS' File.

396.94 2507 INSUFFICIENT REASONS (including data)

> **NOTE:** You already have the '2507 INSUFFICIENT REASONS' File.

I will OVERWRITE your data with mine.

396.95 AMIE C&P EXAM TRACKING

> **NOTE:** You already have the 'AMIE C&P EXAM TRACKING' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

Removing the 'D' cross-reference from file 396.3

Removing the 'C' cross-reference from 396

...SORRY, I'M WORKING AS FAST AS I CAN..........................................

...............................................................................

'DVBA C 2507 EXAM READY' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'DVBA C 2507 EXAM REOPENED' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'DVBA C EDIT ADDRESS' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'DVBA C NEW C&P VETERAN' BULLETIN FILED -- Remember to add mail groups for new bulletins.......................................................

.................

....

'DVBA 21-DAY/NOT DISCHG RPT' Option Filed

'DVBA 7131 DIVISIONAL TRANSFER' Option Filed

'DVBA 7131 INFORMATION REQUEST' Option Filed

'DVBA 7132 TASKMAN' Option Filed

'DVBA ADMISSION REVIEW' Option Filed

'DVBA ALL ADMISSIONS' Option Filed

'DVBA AUTO FINALIZE 7131 TASK' Option Filed

'DVBA AUTO FINALIZE USER MODE' Option Filed

'DVBA C ADD ADDITIONAL EXAM' Option Filed

'DVBA C AMIS REPORT' Option Filed

'DVBA C C&P LINK MANAGEMENT' Option Filed

'DVBA C C&P MASTER MENU' Option Filed

'DVBA C CANCEL REQUESTS/EXAMS' Option Filed

'DVBA C CHECK 2507 INTEGRITY' Option Filed

'DVBA C CHECK 2507 INTEGRITY TM' Option Filed

'DVBA C EDIT C&P REQUEST INFO' Option Filed

'DVBA C EDIT PAT ADDRESS' Option Filed

'DVBA C ENTER C&P REQUEST' Option Filed

'DVBA C EXAM CHECKLIST' Option Filed

'DVBA C INQUIRY' Option Filed

'DVBA C INSUFFICIENT EXAM RPT' Option Filed

'DVBA C MANUAL C&P XFER RETURN' Option Filed

'DVBA C MEDICAL ADM REPORT MENU' Option Filed

'DVBA C MEDICAL ADMIN C&P MENU' Option Filed

'DVBA C NOT SCHEDULED IN 3 DAYS' Option Filed

'DVBA C PENDING REPORT' Option Filed

'DVBA C PHYSICIANS GUIDE' Option Filed

'DVBA C PRINT FEE COVER SHEET' Option Filed

'DVBA C PRINT FINAL RESULTS' Option Filed

'DVBA C PRINT NEW C&P REQ TM' Option Filed

'DVBA C PRINT NEW C&P REQUESTS' Option Filed

'DVBA C PRINT WORKSHEETS' Option Filed

'DVBA C PROCESS MAIL MESSAGE' Option Filed

'DVBA C REGIONAL OFF RPT MENU' Option Filed

'DVBA C REGIONAL OFFICE MENU' Option Filed

'DVBA C RELEASE C&P REQUESTS' Option Filed

'DVBA C REOPEN REQUEST/EXAMS' Option Filed

'DVBA C REPRINT 2507 FINAL RPT' Option Filed

'DVBA C REQUESTS BY DATE RANGE' Option Filed

'DVBA C RO AMIS 290' Option Filed

'DVBA C SCHEDULE EXAMS' Option Filed

'DVBA C TRANSCRIBE REQUEST DATA' Option Filed

'DVBA C TRANSFER C&P REQUEST' Option Filed

'DVBA COMPETENCY EDIT' Option Filed

'DVBA DISCHARGE RPT' Option Filed

'DVBA EDIT REMARKS' Option Filed

'DVBA FINALIZED REPORT' Option Filed

'DVBA GENERATE 21-DAY CERTIF' Option Filed

'DVBA INCOMPETENT VET REPORT' Option Filed

'DVBA INCOMPLETE REQUEST RPT' Option Filed

'DVBA MANUAL NOTIFY' Option Filed

'DVBA MAS REPRINT 21-DAY CERT' Option Filed

'DVBA MEDICAL ADM 7131 MENU' Option Filed

'DVBA MEDICAL ADM 7132 MENU' Option Filed

'DVBA NEW REQUEST' Option Filed

'DVBA NOTICE/DISCHARGE PRINT' Option Filed

'DVBA PENDING REQUESTS RPT' Option Filed

'DVBA RE-ADMISSION REPORT' Option Filed

'DVBA RE-GENERATE 21-DAY CERTIF' Option Filed

'DVBA REG OFF PATIENT INQ' Option Filed

'DVBA REGIONAL 7132 MENU' Option Filed

'DVBA REGIONAL OFFICE MENU' Option Filed

'DVBA REGIONAL PURGING PROGRAM' Option Filed

'DVBA REGIONAL TASK' Option Filed

'DVBA RELEASE 21-DAY CERT' Option Filed

'DVBA REPORT PENSION/A&A' Option Filed

'DVBA REPRINT NOTICE/DISCHARGE' Option Filed

'DVBA RO PRINT 21-DAY CERT' Option Filed

'DVBA RO REPRINT 21-DAY CERT' Option Filed

'DVBA SERV CONN ADM REPORT' Option Filed

'DVBA SITE PARAMETERS' Option Filed

'DVBA STATUS EDIT' Option Filed

'DVBA STATUS INQUIRY' Option Filed.................................

Compiling DVBA C ADD 2507 PAT input template of File 2..

'DVBAXA' ROUTINE FILED..

'DVBAXA1' ROUTINE FILED.....

'DVBAXA2' ROUTINE FILED..

'DVBAXA3' ROUTINE FILED...

'DVBAXA4' ROUTINE FILED...

'DVBAXA5' ROUTINE FILED...

'DVBAXA6' ROUTINE FILED...

'DVBAXA7' ROUTINE FILED

Compiling DVBA STATUS EDIT input template of File 396....

'DVBAXS' ROUTINE FILED.....

'DVBAXS1' ROUTINE FILED.....

'DVBAXS2' ROUTINE FILED....

'DVBAXS3' ROUTINE FILED....

'DVBAXS4' ROUTINE FILED....

'DVBAXS5' ROUTINE FILED....

'DVBAXS6' ROUTINE FILED....

'DVBAXS7' ROUTINE FILED....

'DVBAXS8' ROUTINE FILED....

'DVBAXS9' ROUTINE FILED..

'DVBAXS10' ROUTINE FILED

Compiling DVBA FINALIZED REPORT print template of File 396........

'DVBAXF' ROUTINE FILED.......

Compiling DVBA STATUS print template of File 396................

......................................................

'DVBAXP' ROUTINE FILED

'DVBAXP1' ROUTINE FILED.................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Setting up List Manager Templates

'DVBA C VIEW EXAMS' List Template...Filed.

'DVBA DISCHARGE TYPES' List Template...Filed.

This version of 'DVBAONIT' was created on 10-APR-1995

(at VASITE CAMPUS DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please..................

'DVBA ACCEPT DISCHARGE TYPES' Protocol Filed

'DVBA ADD DISCHARGE TYPE' Protocol Filed

'DVBA C SUPER QUIT' Protocol Filed

'DVBA C VIEW EXAMS (MENU)' Protocol Filed

'DVBA C VIEW JUMP (ACTION)' Protocol Filed

'DVBA C&P SCHD EVENT' Protocol Filed

'DVBA CREATE DISCHARGE TYPE LIST' Protocol Filed

'DVBA DELETE DISCHARGE TYPES' Protocol Filed

'DVBA DISCHARGE TYPES (MENU)' Protocol Filed

'VALM NEXT SCREEN' Protocol Filed

'VALM PREVIOUS SCREEN' Protocol Filed

'VALM PRINT LIST' Protocol Filed

'VALM QUIT' Protocol Filed

OK, Protocol Installation is Complete.

\- Reindexing the 'AC' cross-reference.

Reindexing of 'AC' complete!

\- Reindexing the 'AF' cross-reference.

Reindexing of 'AF' complete!

\- Reindexing the 'AE' cross-reference.

Reindexing 'AE' for field 23 complete!

\- Checking 2507 purge parameter

\- Updating AMIE Exam file pointers to the 2507 Body System file is complete

0 records were updated.

\- Version 2.6 of AMIE has already been loaded.

There is no need to update the Disability Condition file.

\- Updating the Exam Exceptions file..........

Update of Exam Exceptions file has completed. 9 were updated.

\- Version 2.6 of AMIE has already been loaded.

There is no need to add Long Descriptions to the Disability Condition file.

\- Updating the Local Lookup file for Disability Conditions

An entry for the 'Disability Condition' file in the Local Lookup file already exists. Check the AMIE Install Guide for details.

\- Updating the Local Lookup file for Exam Exceptions

Local Lookup file updated!

\- Adding to Local Keyword File.........................................

........................................................................

........................................................................

........................................................................

........................................................................

.................................

The Local Keyword file has completed update of 21 Keywords!

\- Adding Orphan keywords to Local Keyword File.....

The Local Keyword file has completed update of 2 orphans!

\- Adding to Local Synonym File.

The Local Synonym file has completed update of 0 synonyms!

\- Adding to 2507 Body System File..

I have updated 0 exams to the 2507 Body System File!

\- Adding to AMIE Exam File.............................................

.............................

I have updated 0 exams to the AMIE Exam file.

The Post-Init has completed.

Mail message containing Error Log has been sent.

Check your mail to see this log.

\>

# Troubleshooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section has been added to the Installation Guide to aid IRM with the installation of this version. It is intended to provide some direction to the Computer Specialist performing the installation in the event that the post-initialization routines error and abort back to programmer mode. The specialist performing the installation should note that the following messages will display to the screen during the post-init process. The routines that display these messages are included in the parentheses next to the message.

During the VA List Manager Template Load

> "Setting up List Manager Templates." (DVBAPOST)

During the VA List Manager Protocol Load

> "PROTOCOL INSTALLATION" (DVBAONI\*)

> "OK, Protocol Installation is Complete." (DVBAONIT)~

During the Exam Exceptions File (#396.93) Update

> "Update of Exam Exceptions has completed. {#} were updated." (DVBAORPH)~

During the Disability Condition File (#31) Update

> "Adding Long Description to the Disability Condition file."

> "I have finished updating the long descriptions of the Disability Condition

> file!"

> "I updated {#} disabilities." (DVBAPLNG)~

During the Local Lookup File (#8984.4) Update

> "Updating the Local Lookup file."

> "Local Lookup file updated!" (DVBAPLL)~

During the Local Keyword File (#8984.1) Update

> "Adding to Local Keyword file."

> "The Local Keyword file has completed update of {#} Keywords!" (DVBAPKY)~

During the Local Synonym File (#8984.3) Update

> "Adding to Local Synonym file"

> "The Local Synonym file has completed update of {#} synonyms!" (DVBAPSYN)~

During the 2507 Body System File (#396.7) Update

> "Adding to 2507 Body System file"

> "I have updated {#} exams to the 2507 Body System file." (DVBAPBDY)~

During the AMIE Exam File (#396.6) Update

> "Adding to AMIE Exam file"

> "I have updated {#} exams to the AMIE Exam file!" (DVBAPWKS)~

~ Called from DVBAPOST

At Completion of the Install

> "The Post-Init has completed." (DVBAPOST)

Below are descriptions of specific sections of the post-init routines and an explanation of the proper procedures for resolving problems.

Problem: VA List Manager Template Load

If the post-initialization routines error after the message "Setting up List Manager Templates", but before the message "PROTOCOL INSTALLATION" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D ^DVBAPOST

Problem: VA List Manager Protocol Load

If the post-initialization routines error after the message "PROTOCOL INSTALLATION", but before "OK, Protocol Installation is Complete" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D ^DVBAPOST

Problem: Codes Adding to Disability Condition File (#31)

If the post-initialization routines error after the message "Adding to the Disability Condition file", but before the message "Additions to the Disability Condition file {#} has finished. {#} were added" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN11^DVBAPOST

Problem: Exam EXCEPTIONS File (#396.93) Update

If the post-initialization routines error after the message "OK, Protocol Installation is Complete", but before the message "Update of Exam Exceptions has completed. {#} were updated." is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN10^DVBAPOST

Problem: Disability Condition File (#31) MTLU Update

If the post-initialization routines error after the message "Adding Long Description to the Disability Condition file", but before the message "Updating the Local Lookup file" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN2^DVBAPOST

Problem: Local Lookup File (#8984.4) Update

If the post-initialization routines error after the message "Updating the Local Lookup file", but before the message "Adding To Local Keyword file" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN3^DVBAPOST

Problem: Local Keyword File (#8984.1) Update

If the post-initialization routines error after the message "Adding To Local Keyword file", but before the message "Adding to Local Synonym file" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN5^DVBAPOST

Problem: Local Synonym File (#8984.3) Update

If the post-initialization routines error after the message "Adding To Local Synonym file", but before the message "Adding to 2507 Body System file" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN6^DVBAPOST

Problem: 2507 Body System File (#396.7) Update

If the post-initialization routines error after the message "Adding to 2507 Body System file", but before the message "Adding To AMIE Exam file" is displayed, correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN7^DVBAPOST

Problem: AMIE Exam File (#396.6) Update

If the post-initialization routines error after the message "Adding To AMIE Exam file", but before the completion of the init, the correction should proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

> From programmer mode, set up the proper local variables with the following command: \>D SET^DVBAPOST

> From programmer mode, restart the post-init with the following command:

> \>D EN8^DVBAPOST

Problem: Mail Message Abort

If the post-initialization routines fail to successfully mail the error log to the user, the messages "Mail Message containing Error Log has failed!, "Errors contained in the ^TMP("DVBA",{#}) global", and "Investigate this global to determine any existing problems" will be displayed to the screen. To correct this, proceed as follows.

Diagnose and rectify the cause of the error based on the error message that displays on the abort.

Restart the initialization process as follows.

> From programmer mode, load the error log into a mail message and send it with the following command: \>D MAIL^DVBAPOST

If this error occurs again, proceed as follows.

Use the Global Lister to review the errors listed in the ^TMP("DVBA",\$J) Global.

Correct the errors listed.

KILL the Global TMP("DVBA",\$J).

# Post-Init Rerun

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-init routine has been programmed to allow the user to rerun it should a problem develop and the routine error out. The following entry points have been created. These entry points should be rerun after correction of the specific error that occurred as described below

^DVBAPOST

This routine should be rerun after the correction of an error that occurred while setting up VA FileMan or VA List Manager templates or errors that occurred while setting up VA List Manager protocols.

EN0^DVBAPOST

This entry point should be executed if an error occurs in the post-init while setting up necessary local variables.

EN1^DVBAPOST

This entry point should be executed after the correction of an error that occurs while mailing the bulletin that indicates the pre-init did not run OK.

EN2^DVBAPOST

This entry point should be executed after the correction of an error occurring while updating the LONG DESCRIPTION field (#10) in the Disability Condition file (#31).

EN3^DVBAPOST

This entry point should be executed after the correction of an error occurring while adding Disability Condition file (#31) to the Local LOOKUP file (#8984.4).

EN5^DVBAPOST

This entry point should be executed after the correction of an error occurring while entering keywords into the Multi-Term Lookup files.

EN6^DVBAPOST

This entry point should be executed after the correction of an error occurring while entering synonyms into the Multi-Term Lookup files.

EN7^DVBAPOST

This entry point should be executed after the correction of an error occurring while entering the disability codes into the 2507 Body System file (#396.7).

EN8^DVBAPOST

This entry point should be executed after the correction of an error occurring while entering disability codes into the AMIE Exam file (#396.6).

EN10^DVBAPOST

This entry point should be executed after the correction of an error occurring while entering the exam exceptions into the EXAM EXCEPTIONS file (#396.93).

EN11^DVBAPOST

This entry point should be executed after the correction of an error occurring while adding new entries to the DISABILITY CONDITION file (#31).

MAIL^DVBAPOST

This entry point should be executed after the correction of an error occurring while the post-init is mailing the final bulletin upon completion of the initialization.

After the post-init has completed processing, both the user running the init and the Postmaster will be sent a MailMan message containing a log of any problems that occurred during the init. Listed below are the possible errors that may be reported in the MailMan message or to the screen during the post-init, followed by a brief description of the error and instructions for correcting it.

A. KERNEL v7.2 of MTLU is not installed.

> Consult the AMIE Install Guide for details.

> I am stopping the INIT!

> This message will be generated if the pre-init does not find the correct version of KERNEL in the account into which you are installing. Install the correct version of KERNEL, then run the AMIE init again.

B. The pre-init found a problem in the version of MTLU and KERNEL.

> Please review and correct. See install guide for further details.

> This indicates basically the same thing as the previous error message. Correct it in the same manner and restart the post-init as follows: D EN0^DVBAPOST.

C. XXXX is not a valid exam in the AMIE Exam file. ZZZZ Exam exception not added.

> This error will not stop the successful completion of the post-init. This message indicates that the post-init tried to add the exam exception ZZZZ but was unable to because the AMIE Exam XXXX did not exist in the AMIE EXAM file (#396.6). If this should occur, check the AMIE EXAM file (#396.6) for the existence of this AMIE exam. If it is misspelled, change the spelling to match what is shown in the message. If it is not present, consult your ISC for the proper setting of that exam. If the problem has been corrected, the following routine can be rerun to try again: D ^DVBAORPH.

D. Addition of exam exception ZZZZ has failed. Please consult install guide.

> This error does not stop the successful completion of the post-init. The addition of the exam exception ZZZZ has failed. Check to ensure that the exam exception does not already exist or that the AMIE exam it is pointing to does not exist. This exam information can be obtained at line label TXT of DVBAORPH. Once this problem is corrected, the following routine can be rerun: D ^DVBAORPH.

E. Unable to add the variable pointer to file \####. Check the AMIE Install Guide for details.

> The \#.02 Field of either the Local Keyword file (#8984.1) or the Local Shortcut file (#8984.2) contain variable pointers with a prefix of "DVBA". If this error should occur, contact your ISC.

F. Unable to add the new entry 'Disability Condition' to the Local Lookup file. Check the AMIE Install Guide for details.

> Addition of the new local lookup entry has failed. Check the Local LOOKUP file (#8984.4) for the cause. Once corrected, rerun the post-init in the following fashion: D SET^DVBAPOST,EN3^DVBAPOST.

G. An entry for the 'Disability Condition' file in the Local Lookup file already exists. Check the AMIE Install Guide for details.

> If this error occurs, an entry already exists in the Local LOOKUP file (#8984.4). Check the Local Keyword (#8984.1) and Local Shortcut files, Field \#.02 for the variable pointer to File \#31. If all of these are in place, this section is OK. If not, delete the entry from the Local Lookup file (#8984.4) using VA FileMan. Rerun the post-init as follows: D SET^DVBAPOST,EN3^DVBAPOST.

H. Prefix DVBA not set up on AMIE Site Parameter file. Conversion aborted!

> This message is generated during the update of the Multi-Term Lookup files with keywords. If the pre-init did not properly populate the POST INIT VARIABLES field in the AMIE Site Parameter file (#396.1), the keyword update cannot run and will be aborted before it begins. Correct the value in this field and rerun the post-init as follows: D SET^DVBAPOST,EN5^DVBAPOST.

I. Addition of KEYWORD {keyword} for code {code} has FAILED. Please investigate!

> This message is generated during the update of the Multi-Term Lookup files with keywords. IRM should verify the Local Keyword file (#8984.1) to see that the reported keyword for the reported disability code was not added. IRM will also want to check the value that the post-init is attempting to enter into the ENTRY field of the Local Keyword file (#8984.1).

J. Could not find the {code} in the 'C' X-ref. Please investigate!

> This message is generated during the update of the Multi-Term Lookup files with keywords. IRM should investigate the "C" cross-reference on the Disability Condition file (#31) for the code displayed.

> NOTE: If the update of the Local Keyword file (#8984.1) with keywords aborts to the programmer level, IRM should note the value of DA. First display this local variable with the ZWrite command; then note its value. This will be helpful in determining how the record being written to the Local Keyword file (#8984.1) was left upon the abort.

K. Term {term} Not in Local Lookup File or Addition Failed.

> This error is generated when a problem occurs while adding a medical term to the Local Synonym file (#8984.3). IRM should compare the term in the DVBAPS1 routine and compare it to the Data Dictionary field definitions in the Local Synonym file (#8984.3). For example, a term should be all upper case or the addition will fail. It is also important to note that if a term does not get added to the Local Synonym file (#8984.3), none of its synonyms will be added to the file.

L. Addition of synonym {synonym} to {term} has failed.

> This error is generated when a problem occurs while adding a synonym to a term in the Local Synonym file (#8984.3). IRM should compare the synonym in the DVBAPS1 routine and compare it to the Data Dictionary field definitions in the Local Synonym file (#8984.3). For example, a synonym should be all upper case or the addition will fail.

M. Could not add code {code} to body system {body system}.

> This error is generated when a problem occurs while adding a disability code to a particular body system in the 2507 Body System file (#396.7). IRM should check to see if the disability code is correct in the data routines DVBAPB\*. If it is not correct in the data routines, the correction should be made. If it is a correct disability code, IRM should check its existence in the Disability CONDITION file ^DIC(31). If the disability code does not exist in the Disability CONDITION file (#31), IRM should contact the ISC.

N. Could not find body system {body system}.

> This error is generated when a problem occurs while trying to locate the body system in the 2507 Body System file (#396.7). IRM should check to see if the body system is entered correctly in the data routines DVBAPB\*. If it is not a correct body system, the data routines should be updated. If it is a correct body system, IRM should check for its existence in the 2507 Body System file (#396.7). If the body system does not exist in the 2507 Body System file (#396.7), IRM should contact the ISC.

O. Could not find AMIE exam {worksheet description}.

> This error is generated when a problem occurs while looking for the work sheet in the AMIE Exam file (#396.6). IRM should check to see if the work sheet description is entered correctly in the data routines DVBAPW\*. If the description is not correct in the data routines, the change should be made. If it is a correct work sheet description, IRM should then check for its existence in the AMIE Exam file (#396.6). If the work sheet description is not in the AMIE Exam file (#396.6), IRM should contact the ISC.

P. Addition of exam {code} to {worksheet description} has failed.

> This error is generated when a problem occurs when trying to add a disability code to a work sheet entry in the AMIE Exam file (#396.6). IRM should check to see if the disability code is entered correctly in the data routines DVBAPW\*. If the disability code is not correct in the data routines DVBAPW\*, it should be changed to the correct code. If it is a correct disability code, IRM should then check for its existence in the Disability CONDITION file ^DIC(31). If the disability code is not in the Disability CONDITION file (#31), IRM should contact the ISC.

Q. Problems exists with the disability condition {code}.

Long description NOT added!

> This error is generated when a problem occurs while updating the Long Description field (#10) in the Disability Condition file (#31). This error may result from the lack of a "C" cross-reference on the reported code or a missing zero node for the reported code. IRM should check for the existence of a "C" cross-reference for that code. If that cross-reference exists, the existence of the zero node for internal entry number pointed to by that "C" cross-reference should be checked. The Global Listing utility can be used to aid in this diagnosis. It will be necessary to research and correct this problem. Once corrected, the post-init can be rerun as follows:

> D SET,EN^DVBAPLNG,MAIL^DVBAPOST

R. Unable to get the proper index and prefix from the AMIE Site Parameter file. Check the AMIE install Guide for details.

> This error is generated when a problem occurs while updating the Local LOOKUP file (#8984.4). It indicates either a problem with the data contained in the field Post Init Scratch (#90) in the AMIE Site Parameter file (#396.1) or the current existence of the cross-reference "ADVB" on the Local Shortcut file (#8984.2). IRM should first use VA FileMan to check the value of the field Post Init Scratch (#90) in the AMIE Site Parameter file (#396.1). The value in this field should be "DVBA;ADVB". If this field contains the correct information, IRM should then check for the "ADVB" cross-reference on the Local Shortcut file (#8984.2).

S. Disability Condition {code} was not added. Entry already exists.

> This error is generated when a problem occurs while updating the Disability Condition file (#31) with a new disability code. It indicates that the code displayed is already contained in the Disability Condition file (#31). IRM should use VA FileMan to check for the existence of the code in File \#31. If the code exists, IRM should check for the integrity of the information on that record. If the integrity is OK, there is no problem. If not, the erroneous information should be corrected.

T. Not able to add Disability Condition {code}. Consult the Install Guide.

> This error indicates that the disability condition code was not successfully added to File \#31. IRM should contact the ISC to make arrangements to add the code to the Disability Condition file (#31). This may be done using the Enter/Edit option of VA FileMan and referencing the TXT tag lines in the DVBAPADD routine. IRM may also correct the condition causing the failure and rerun the post-init by calling the tag EN11^DVBAPOST from programmer mode.

U. Mail Message containing Error Log has failed!

Errors contained in the ^TMP("DVBA",{#}) global.

Investigate this global to determine any existing problems

> This error will not be contained in the mail message that includes the error messages. This message is displayed to the screen if a problem occurs while the mail message is being sent. If this message displays to the screen, the mail message will not be received. IRM should first try to mail the message again by calling the entry point MAIL^DVBAPOST from programmer mode. If this does not work, the Global Listing tool can be used to review the errors that occurred during the post-initialization. The Global array ^TMP("DVBA",\$J contains those errors. That global should be KILLed after reviewing the errors and the ^TMP Global.