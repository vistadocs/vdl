---
title: Record Tracking Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: RT
app_name: Record Tracking
section: FIN
app_status: active
pkg_ns: RT
patch_ver: 1
patch_id: RT*1
group_key: "RT:RT:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Installation](#installation) - [# Appendix I](#appendix-i) - [# Appendix II](#appendix-ii) - [# Appendix III](#appendix-iii) 1\. Record Tracking will use ^TMP instead of ^UTILITY for scratch globals. An exception is ^UTILITY("RTDPTSORT") which is used in initialization options and to generate r
audience: 
keywords: 
  - filed
  - rtini
  - routine
  - record
  - added
  - shall
  - write
  - over
  - pull
  - existing
page_count: 0
word_count: 2534
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/30/09
revision_oldest: 3/30/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rtig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rtig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=53"
---

![](record-tracking-version-1-installation-guide/001.png)

Record Tracking V. 2.0Installation GuideNovember 1991

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/30/09

|          |                                       |                     |                      |
|----------|---------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
| 3/30/09  | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# # Installation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Installation](#installation)
- [# Appendix I](#appendix-i)
- [# Appendix II](#appendix-ii)
- [# Appendix III](#appendix-iii)
1\. Record Tracking will use ^TMP instead of ^UTILITY for scratch globals. An exception is ^UTILITY("RTDPTSORT") which is used in initialization options and to generate record retirement pull lists. ^TMP should be configured as a local scratch global on the system just like ^UTILITY.
2\. If you have added any variable pointers to Files 190 or 195.9, it would be a good idea to save a list of the file attributes or a global listing of the dd(195.9,.01,"V" fields of these files. They tend to get mixed up with inits. RT tries to avoid it by not including the variable pointers with the init and then adding, if necessary, with RTIPOST0. If there is a problem, the variable pointers can be easily reset or reordered with FileMan Modify File Attributes. Appendix I shows the distributed variable pointers for Record Tracking.
3\. Record Tracking will use the New Person file (#200). ';DIC(16,' entries in the Borrowers/file areas file (#195.9) will be converted to ';VA(200,' in the postinit routine RTIPOST2.
Saved by %RS from \[COR,VBB\] on 22-OCT-1991 20:45:23.82
Header: RT\*
Restore all (A) or Selected (S) ? \<A\>
RT RTB RTB1 RTB2 RTDEL RTDPA RTDPA1 RTDPA2
RTDPA3 RTDPA31 RTDPA32 RTINI001 RTINI002 RTINI003 RTINI004 RTINI005
RTINI006 RTINI007 RTINI008 RTINI009 RTINI010 RTINI011 RTINI012 RTINI013
RTINI014 RTINI015 RTINI016 RTINI017 RTINI018 RTINI019 RTINI020 RTINI021
RTINI022 RTINI023 RTINI024 RTINI025 RTINI026 RTINI027 RTINI028 RTINI029
RTINI030 RTINI031 RTINI032 RTINI033 RTINI034 RTINI035 RTINI036 RTINI037
RTINI038 RTINI039 RTINI040 RTINI041 RTINI042 RTINI043 RTINI044 RTINI045
RTINI046 RTINI047 RTINI048 RTINI049 RTINI050 RTINI051 RTINI052 RTINI053
RTINI054 RTINI055 RTINI056 RTINI057 RTINI058 RTINI059 RTINI060 RTINI061
RTINI062 RTINI063 RTINI064 RTINI065 RTINI066 RTINI067 RTINI068 RTINI069
RTINI070 RTINI071 RTINI072 RTINI073 RTINI074 RTINI075 RTINI076 RTINI077
RTINI078 RTINI079 RTINI080 RTINI081 RTINI082 RTINI083 RTINI084 RTINI085
RTINI086 RTINI087 RTINI088 RTINI089 RTINI090 RTINI091 RTINI092 RTINI093
RTINI094 RTINI095 RTINIT RTINIT0 RTINIT1 RTINIT2 RTINIT3 RTIPOST0 RTIPOST1 RTIPOST2 RTIPOST3 RTIPOST4 RTIPRE RTL RTL1 RTL2 RTL3 RTLDIV RTM RTMAS RTNQ RTNQ1 RTNQ2 RTNQ21 RTNQ3 RTNQ4 RTNQ41 RTNTEG RTP RTP1 RTP2 RTP3 RTP31 RTP311 RTP32 RTP4 RTP40 RTP41 RTP5 RTP51 RTP6 RTPCAN RTPSET RTPSET1 RTPURGE RTQ RTQ1 RTQ2 RTQ3 RTQ4 RTQ41 RTQ5 RTRAD RTRD RTREP RTREP1 RTRPT RTRPT1 RTRPT2 RTRPT3 RTRPT4 RTRPT5 RTSM RTSM1 RTSM2 RTSM3 RTSM4 RTSM5 RTSM6 RTSM61 RTSM7 RTSM8 RTSM81 RTSYS RTT RTT1 RTT11 RTT12 RTT2 RTT21 RTT3 RTT4 RTTR RTTR1 RTTR11 RTTR2 RTUTL RTUTL1 RTUTL2 RTUTL3 RTUTL4 RTUTL5 RTUTL6
197 routines restored
\>D ^RTINIT
This version (#2) of 'RTINIT' was created on 22-OCT-1991
(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.18)
I HAVE TO RUN A PRE-INITIALIZATION ROUTINE.
Checksum routine created on OCT 22, 1991@19:29:33 by KERNEL V6.5
RT ok
RTB ok
RTB1 ok
RTB2 ok
RTDEL ok
RTDPA ok
........ See Appendix III
If this is the First Installation of Record Tracking, you will want to answer
Yes to all the questions from the DIFROM.
If Record Tracking has already been installed on this system, you should
probably answer NO to the questions 'WANT MY DATA ADDED TO YOURS'.
Two new label print field entries have been added to the Label Print
Field file:
Ward Location and Current Borrower Date/Time
Answer 'YES' to add this data to the Label Print Field file (#194.5).
I AM GOING TO SET UP THE FOLLOWING FILES:
44 HOSPITAL LOCATION (Partial Definition)
> **NOTE:** You already have the 'HOSPITAL LOCATION' File.
Shall I write over the existing Data Definition? YES//
190 RECORDS
> **NOTE:** You already have the 'RECORDS' File.
Shall I write over the existing Data Definition? YES//
190.1 REQUESTED RECORDS
> **NOTE:** You already have the 'REQUESTED RECORDS' File.
Shall I write over the existing Data Definition? YES//
190.2 MISSING RECORDS
> **NOTE:** You already have the 'MISSING RECORDS' File.
Shall I write over the existing Data Definition? YES//
190.3 RECORD MOVEMENT HISTORY
> **NOTE:** You already have the 'RECORD MOVEMENT HISTORY' File.
Shall I write over the existing Data Definition? YES//
194.2 PULL LIST
> **NOTE:** You already have the 'PULL LIST' File.
Shall I write over the existing Data Definition? YES//
194.4 LABEL FORMAT (including data)
> **NOTE:** You already have the 'LABEL FORMAT' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
194.5 LABEL PRINT FIELD (including data)
> **NOTE:** You already have the 'LABEL PRINT FIELD' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// yes \*\*\*\*\*\*\*\* to add 2 new entries \*\*\*
195.1 RECORD TRACKING APPLICATION (including data)
> **NOTE:** You already have the 'RECORD TRACKING APPLICATION' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
195.2 RECORD TYPES (including data)
> **NOTE:** You already have the 'RECORD TYPES' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
195.3 RECORD MOVEMENT TYPES (including data)
> **NOTE:** You already have the 'RECORD MOVEMENT TYPES' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
195.4 RECORD TRACKING SYSTEM PARAMETERS (including data)
> **NOTE:** You already have the 'RECORD TRACKING SYSTEM PARAMETERS' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
195.6 REASONS (including data)
> **NOTE:** You already have the 'REASONS' File.
Shall I write over the existing Data Definition? YES//
Want my data merged with yours? YES// NO
195.9 BORROWERS/FILE AREAS
> **NOTE:** You already have the 'BORROWERS/FILE AREAS' File.
Shall I write over the existing Data Definition? YES//
SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)
> **NOTE:** This package also contains BULLETINS
SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// (YES)
> **NOTE:** This package also contains SORT TEMPLATES
SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)
> **NOTE:** This package also contains INPUT TEMPLATES
SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES//(YES)
> **NOTE:** This package also contains PRINT TEMPLATES
SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES//(YES)
> **NOTE:** This package also contains FUNCTIONS
SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// (YES)
> **NOTE:** This package also contains SECURITY KEYS
SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)
> **NOTE:** This package also contains OPTIONS
SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)
ARE YOU SURE EVERYTHING'S OK? Y (YES)
...HMMM, THIS MAY TAKE A FEW MOMENTS........................................
............................................................................
Compiling Cross-Reference routine.............
...HMMM, LET ME THINK ABOUT THAT A MOMENT...
RTXR1 routine filed
RTXR2 routine filed
RTXR routine filed
Compiling Cross-Reference routine.............
...HMMM, JUST A MOMENT PLEASE...
RTXQ1 routine filed
RTXQ2 routine filed
RTXQ routine filed
Compiling Cross-Reference routine.............
...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...
RTXM1 routine filed
RTXM2 routine filed
RTXM routine filed
Compiling Cross-Reference routine.............
...EXCUSE ME, JUST A MOMENT PLEASE...
RTXP1 routine filed
RTXP2 routine filed
RTXP routine filed
Compiling Cross-Reference routine.............
...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...
RTXB1 routine filed
RTXB2 routine filed
RTXB3 routine filed
RTXB4 routine filed
RTXB5 routine filed
RTXB6 routine filed
RTXB7 routine filed
RTXB8 routine filed
RTXB routine filed......
'RT ATTEMPT-ON-MISSING-REC' BULLETIN FILED-Remember to add its user groups.
'RT CANCELED REQ' BULLETIN FILED -- Remember to add its user groups.
'RT MISSING RECORD' BULLETIN FILED -- Remember to add its user groups.
'RT RECORD DELETION' BULLETIN FILED -- Remember to add its user groups.
'RT RECORD FOUND' BULLETIN FILED -- Remember to add its user groups.
'RT REQUEST/NOTICE TRANSFER' BULLETIN FILED- Remember to add its user groups
............................................................................
............................
'RT INACT-MENU' Option Filed
'RT INACT-PULL-CHARGE' Option Filed
'RT INACT-PULL-CREATE' Option Filed
'RT INACT-PULL-NOT FILLABLE' Option Filed
'RT INACT-PULL-PRINT' Option Filed
'RT INQ-COMBO-TRACE' Option Filed
'RT INQ-INQUIRY' Option Filed
'RT INQ-MEDIUM' Option Filed
'RT INQ-MENU' Option Filed
'RT INQ-SHORT' Option Filed
'RT INQ-TRACE' Option Filed
'RT LBL-FORMATTER' Option Filed
'RT LBL-TEST' Option Filed
'RT MAS-ADMIT-CHART-REQUEST' Option Filed
'RT MAS-ADMITTING' Option Filed
'RT MAS-CHART-PROFILE' Option Filed
'RT MAS-CHART-REQUEST' Option Filed
'RT MAS-EXPED-MENU' Option Filed
'RT MAS-FILE-CLERK-MENU' Option Filed
'RT MAS-FILL-NEXT' Option Filed
'RT MAS-LABEL-PRINT' Option Filed
'RT MAS-MENU' Option Filed
'RT MAS-RE-CHARGE' Option Filed
'RT MAS-SUPER-MENU' Option Filed
'RT OVERALL' Option Filed
'RT PULL-ADD' Option Filed
'RT PULL-CANCEL-PULL-ALL' Option Filed
'RT PULL-CANCEL-PULL-LIST' Option Filed
'RT PULL-CANCEL-REQUEST' Option Filed
'RT PULL-CHANGE-DATE' Option Filed
'RT PULL-CHARGE-OUT' Option Filed
'RT PULL-COMMENT' Option Filed
'RT PULL-CREATE' Option Filed
'RT PULL-LIST-PRINT' Option Filed
'RT PULL-MENU' Option Filed
'RT PULL-MULTI-INSTITUTION' Option Filed
'RT PULL-NOT FILLABLE' Option Filed
'RT RAD-FILE-CLERK-MENU' Option Filed
'RT RAD-JACKET-PROFILE' Option Filed
'RT RAD-JACKET-REQUEST' Option Filed
'RT RAD-MENU' Option Filed
'RT RAD-REG-AREA' Option Filed
'RT RAD-SUPER-MENU' Option Filed
'RT RPT-BORROWERS' Option Filed
'RT RPT-HOME-LIST' Option Filed
'RT RPT-INPATIENT' Option Filed
'RT RPT-LOOSE' Option Filed
'RT RPT-MENU' Option Filed
'RT RPT-MISSING' Option Filed
'RT RPT-OVERDUE' Option Filed
'RT RPT-PENDING-REQUEST' Option Filed
'RT RPT-REQUEST-BY-BORROWER' Option Filed
'RT RPT-REQUEST-TIME' Option Filed
'RT RPT-RETRIEVAL STATS' Option Filed
'RT RTQ-CANCEL' Option Filed
'RT RTQ-DISPLAY' Option Filed
'RT RTQ-EDIT' Option Filed
'RT RTQ-FILL' Option Filed
'RT RTQ-MENU' Option Filed
'RT RTQ-REPRINT' Option Filed
'RT RTQ-REQUEST-REC' Option Filed
'RT SM-ADMITTING' Option Filed
'RT SM-APPL' Option Filed
'RT SM-CLINIC REQUESTS' Option Filed
'RT SM-FILE-REMOTE' Option Filed
'RT SM-FILE-ROOM' Option Filed
'RT SM-MENU' Option Filed
'RT SM-OVERALL' Option Filed
'RT SM-PURGE-AUTOMATIC' Option Filed
'RT SM-PURGE-DATA' Option Filed
'RT SM-REC-1CLINIC-REQUEST' Option Filed
'RT SM-REC-BORROWERS' Option Filed
'RT SM-REC-CLINIC-REQUEST' Option Filed
'RT SM-REC-COMPILE-TERM-DIGIT' Option Filed
'RT SM-REC-DELETE-TERM-DIGIT' Option Filed
'RT SM-REC-IN-PT' Option Filed
'RT SM-REC-INIT' Option Filed
'RT SM-REC-LABELS' Option Filed
'RT SM-REC-MENU' Option Filed
'RT SM-RECOMP' Option Filed
'RT SM-REG-AREA' Option Filed
'RT SYS-APPLICATION' Option Filed
'RT SYS-FILE ROOM' Option Filed
'RT SYS-INDIVD-BORROWERS' Option Filed
'RT SYS-LABELS' Option Filed
'RT SYS-MENU' Option Filed
'RT SYS-MOVEMENT' Option Filed
'RT SYS-PRINT-BOR' Option Filed
'RT SYS-REASONS' Option Filed
'RT SYS-RECORD TYPE' Option Filed
'RT TRANS-CHARGE-OUT' Option Filed
'RT TRANS-CHECK-IN' Option Filed
'RT TRANS-CREATE' Option Filed
'RT TRANS-DELETE' Option Filed
'RT TRANS-INACTIVATE' Option Filed
'RT TRANS-MENU' Option Filed
'RT TRANS-MISSING' Option Filed
'RT TRANS-MOVE-REQ-LAST-VOL' Option Filed
'RT TRANS-NEW-VOL' Option Filed
'RT TRANS-NEW-VOL-MULTI' Option Filed
'RT TRANS-PATIENT' Option Filed
'RT TRANS-RE-CHARGE' Option Filed
'RT TRANS-TRANSFER' Option Filed
'RT TRANS-UPDATE' Option Filed
'RT TRANSFER-BACK' Option Filed
'RT TRANSFER-CREATE' Option Filed
'RT TRANSFER-OUT' Option Filed
'RT TRANSFER-REQUEST' Option Filed..........................................
........................
Compiling RT CHANGE REQUEST STATUS input template of File 190.1...
'RTCS' ROUTINE FILED
Compiling RT CHARGE input template of File 190...
'RTCC' ROUTINE FILED.....
'RTCC2' ROUTINE FILED....
'RTCC3' ROUTINE FILED....
'RTCC4' ROUTINE FILED..
'RTCC5' ROUTINE FILED..
'RTCC1' ROUTINE FILED
Compiling RT MOVEMENT input template of File 190.3......
'RTCM' ROUTINE FILED...
'RTCM1' ROUTINE FILED.
'RTCM2' ROUTINE FILED
Compiling RT NEW RECORD input template of File 190...
'RTCR' ROUTINE FILED.....
'RTCR1' ROUTINE FILED....
'RTCR2' ROUTINE FILED.
'RTCR3' ROUTINE FILED
Compiling RT PULL LIST input template of File 194.2....
'RTCP' ROUTINE FILED....
'RTCP1' ROUTINE FILED.....
'RTCP2' ROUTINE FILED...
'RTCP3' ROUTINE FILED
Compiling RT REQUEST input template of File 190.1..
'RTCU' ROUTINE FILED....
'RTCU2' ROUTINE FILED....
'RTCU3' ROUTINE FILED......
'RTCU4' ROUTINE FILED..
'RTCU1' ROUTINE FILED
Compiling RT HOME LOCATION print template of File 190................
'RTCH' ROUTINE FILED......
Compiling RT MISSING print template of File 190.2..........................
.......
'RTCL' ROUTINE FILED...........
Compiling RT PENDING REQUESTS print template of File 190.1.................
'RTCX' ROUTINE FILED.......
NO SECURITY-CODE PROTECTION HAS BEEN MADE
Post-initialization routine running
Removing 'post-selection' action from ^DD(195.9,0,"ACT")
Checking variable pointers in DD of file \# 190
Checking variable pointers in DD of file \# 195.9
Added variable pointer '200'
Removing 'Person/Provider' variable pointer '16'
Checking Applications in file \#195.1 ...
Added 'New Person' to 'MEDICAL ADMINISTRATION' application-borrowers
Added 'New Person' to 'RADIOLOGY' application-borrowers
Removing 'Provider, Person' from borrowers in file \#195.1
Adding new movements to Record movement type file \#195.3
Added 'TRANSFER CREATE INITIAL' movement for 'MEDICAL ADMINISTRATION'
Added 'TRANSFER RETIRE' movement for 'MEDICAL ADMINISTRATION'
Added 'TRANSFER CREATE INITIAL' movement for 'RADIOLOGY'
Added 'TRANSFER RETIRE' movement for 'RADIOLOGY'
Changing Borrowers/file areas entries to New Person pointers
11 18 26 32 37 311 312 313 314 315 316 317 318 319 320 321 322
323 324 325 326 327 328 329 330 331 332 333 334 335 342 344 347
348 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381
382 383 384 385 386 387 388 389 390 391 392 393 398 399 400 401
402 403 405 406 407 408 409 410 413 418 430 431 432 433 439 440
695 698 711 712 717 718 719
..all done ...
Adding Federal Record Centers to the Institution file \#4 - See Appendix II
Added 'FEDERAL RECORDS CENTER GSA-1 WALTHAM'
Added 'FEDERAL RECORDS CENTER GSA-2 BAYONNE'
Added 'FEDERAL RECORDS CENTER GSA-3 PHILADELPHIA'
Added 'FEDERAL RECORDS CENTER MECHANICSBURG'
Added 'FEDERAL RECORDS CENTER GSA-4 EAST POINT'
Added 'FEDERAL RECORDS CENTER GSA-5 CHICAGO'
Added 'FEDERAL RECORDS CENTER DAYTON'
Added 'FEDERAL RECORDS CENTER GSA-6 KANSAS CITY'
Added 'FEDERAL RECORDS CENTER GSA-7 FORT WORTH'
Added 'FEDERAL RECORDS CENTER GSA-8 DENVER'
Added 'FEDERAL RECORDS CENTER GSA-9 SAN BRUNO'
Added 'FEDERAL RECORDS CENTER LAGUNA NIGUEL'
Added 'FEDERAL RECORDS CENTER GSA-10 SEATTLE'
Added 'NATIONAL RECORDS CENTER WASHINGTON'
Added 'NATIONAL PERSONAL RECORDS CIV ST. LOUIS'
Recompiling the Clinic Setup Template, don't worry
Compiling SDB input template of File 44.....
'SDBT' ROUTINE FILED........
'SDBT1' ROUTINE FILED......
'SDBT2' ROUTINE FILED........
'SDBT3' ROUTINE FILED.....
'SDBT5' ROUTINE FILED.
'SDBT4' ROUTINE FILED.
'SDBT6' ROUTINE FILED
Remember to Recompile Templates on all systems using the
'Re-compile templates' option.
1\. In File 195.4, Record Tracking System Parameters, the MAS, RAD Interfaces status have been set 'DOWN' if this is the first installation of Record Tracking. When RT is live, remember to set them back 'UP'.
2\. In File 195.4, Record Tracking System Parameters, the BATCH RECORD,XRAY REQUESTS is set to NO. You will want to process requests for records, x-rays at night instead of immediately through the TaskManager. Set this parameter to YES when RT is live.
MAKE SURE the RT SM-CLINIC-REQUESTS option is scheduled and runs daily after hours.
MAKE SURE the RT SM-PURGE-AUTOMATIC option is scheduled and runs monthly after hours.
-----------------------------------------------------------------
Please enter your Institution in a new field 30 of file 195.4
-----------------------------------------------------------------
INSTITUTION/STATION NUMBER: 500// 500 ALBANY, NY NEW YORK

# # Appendix I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VARIABLE POINTERS DISTRIBUTED WITH RT v1.35 Beta test

Records

190,.01 ASSOCIATED ENTITY OR ITEM 0;1 VARIABLE POINTER (Required)

FILE ORDER PREFIX LAYGO MESSAGE

2 1 P n PATIENT

Borrower/file areas

195.9,.01 NAME 0;1 VARIABLE POINTER (Required)

FILE ORDER PREFIX LAYGO MESSAGE

44 2 L n LOCATION

200 1 P n PROVIDER PERSON

42 3 W n WARD

4 4 I n INSTITUTION

SCRN FILE 44: S DIC("S")="I ""W""'\[\$P(^(0),U,3),\$S('\$D(^(""I"")):1,'^(""I""):1

,DT\<+^(""I""):1,'\$P(^(""I""),U,2):0,1:DT\>+\$P(^(""I""),U,2))"

SCRN FILE 200: S DIC("S")="I \$S('\$D(^(""I"")):1,'^(""I""):1,1:DT'\>^(""I""))"

SCRN FILE 42: S DIC("S")="I \$S('\$D(^(""I"")):1,\$P(^(""I""),U)'=""I"":1,1:0)"

# # Appendix II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The postinit routine RTIPOST4 will add 16 Federal Record Centers to the INSTITUTION file (#4). If it thinks there are already entries with similar names, it will stop and just list the entries and fields it was going to add. If you already have an entry, it can be edited to conform to the list. Do not delete it. To add new entries called "FEDERAL RECORDS CENTER", use quotation marks with the FileMan name prompt to force the entry.

Some or all of these entries may be made available to use as borrowers for record retirement using the System Definition Menu, Borrower Set-up option. It may be convenient for the file room if a commonly used term for one of these sites is defined as a borrower synonym.

# # Appendix III

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RT\*2\*1 included in the Distribution

....

RTREP ok

RTREP1 ok

RTRPT Calculated 16268866, off by 38992

RTRPT1 ok

RTRPT2 ok

.....

RTRPT5 Calculated 6474287, off by -156040

....